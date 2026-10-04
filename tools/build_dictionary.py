# -*- coding: utf-8 -*-
"""
Builds the offline English -> Turkish dictionary used by the word info card (Faz 7).

Sources (all project-owned, openly licensed content):
  0. tools/core_vocabulary.py (general meanings of the most frequent words)
  1. `vocab_focus` lists of tools/book_XX_data.py (curated target words, highest priority)
  2. "word: meaning" glosses inside lesson.json segment notes

Output: lessons/dictionary.json, copied to Web/public/lessons and Android assets.

    python tools/build_dictionary.py
"""
import glob
import importlib.util
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "lessons", "dictionary.json")
MIRRORS = [
    os.path.join(ROOT, "Web", "public", "lessons", "dictionary.json"),
    os.path.join(ROOT, "Android", "app", "src", "main", "assets", "lessons", "dictionary.json"),
]

MAX_KEY_WORDS = 4
MAX_MEANING_LEN = 120
NOTE_PART = re.compile(r"^\s*['\"“]?([A-Za-z][A-Za-z'’ -]{0,40}?)['\"”]?\s*:\s*(.+)$")


def normalize_key(word: str) -> str:
    key = word.strip().lower().replace("’", "'")
    key = re.sub(r"\s+", " ", key)
    return key.strip(" '\"-.,;:!?")


def clean_meaning(meaning: str) -> str:
    meaning = re.sub(r"\s+", " ", meaning).strip()
    return meaning.rstrip(" .;,")


def acceptable(key: str, meaning: str) -> bool:
    if not key or not meaning or key.startswith("sayfa"):
        return False
    if len(key.split()) > MAX_KEY_WORDS or len(meaning) > MAX_MEANING_LEN:
        return False
    return True


def load_pages(path: str):
    spec = importlib.util.spec_from_file_location("book_data", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "PAGES_DATA", None) or getattr(module, "BOOK_DATA", None) or []


def main() -> None:
    entries: dict[str, str] = {}

    # General meanings of the most frequent words come first.
    from core_vocabulary import CORE

    for word, meaning in CORE.items():
        key, value = normalize_key(word), clean_meaning(meaning)
        if acceptable(key, value):
            entries.setdefault(key, value)

    for path in sorted(glob.glob(os.path.join(ROOT, "tools", "book_*_data.py"))):
        for page in load_pages(path):
            for word, meaning in page.get("vocab_focus", []):
                key, value = normalize_key(word), clean_meaning(meaning)
                if acceptable(key, value):
                    entries.setdefault(key, value)
    curated = len(entries)

    for path in sorted(glob.glob(os.path.join(ROOT, "lessons", "*", "lesson.json"))):
        if os.path.basename(os.path.dirname(path)).startswith("custom_"):
            continue  # personal lessons are not part of the shared data
        with open(path, encoding="utf-8") as f:
            lesson = json.load(f)
        for segment in lesson["segments"]:
            for part in re.split(r"[;|]", segment.get("notes") or ""):
                match = NOTE_PART.match(part.strip())
                if not match:
                    continue
                key, value = normalize_key(match.group(1)), clean_meaning(match.group(2))
                if acceptable(key, value):
                    entries.setdefault(key, value)

    data = {
        "version": 1,
        "source_lang": "en",
        "target_lang": "tr",
        "license": "DictaLearn core vocabulary + glosses from the lesson content (public domain adaptations)",
        "entries": dict(sorted(entries.items())),
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    for mirror in MIRRORS:
        shutil.copy2(OUT, mirror)

    size_kb = os.path.getsize(OUT) / 1024
    print(f"{len(entries)} entries ({curated} curated) -> {os.path.relpath(OUT, ROOT)} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
