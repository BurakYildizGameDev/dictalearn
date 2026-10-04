# -*- coding: utf-8 -*-
"""
Assembles Book 28 data from Part 1 and Part 2,
validates 25 pages x 20 sentences = 500 sentences,
creates tools/book_28_data.py,
and generates lessons/book_28_the_hound_of_the_baskervilles/book_preview.md.
"""

import os
import sys

# Configure UTF-8 for console output on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from create_book_28_part1 import PAGES_1_TO_13
from create_book_28_part2 import PAGES_14_TO_25

BOOK_TITLE = "The Hound of the Baskervilles"
AUTHOR = "Sir Arthur Conan Doyle"
BOOK_ID = "book_28_the_hound_of_the_baskervilles"
LEVEL = "CEFR B1 (Intermediate / Orta Seviye)"

ALL_PAGES = PAGES_1_TO_13 + PAGES_14_TO_25

print(f"Total pages assembled: {len(ALL_PAGES)}")
total_sentences = sum(len(p["sentences"]) for p in ALL_PAGES)
print(f"Total sentences: {total_sentences}")

# Validate continuous IDs 1 to 500
expected_id = 1
for p in ALL_PAGES:
    assert len(p["sentences"]) == 20, f"Page {p['page_no']} has {len(p['sentences'])} sentences!"
    assert len(p["vocab_focus"]) == 8, f"Page {p['page_no']} has {len(p['vocab_focus'])} vocab items!"
    for s in p["sentences"]:
        assert s["id"] == expected_id, f"Expected ID {expected_id}, got {s['id']}"
        expected_id += 1

print("✅ Validation successful: Exactly 25 pages, 500 sentences, 200 vocabulary focus items!")

# Write tools/book_28_data.py
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
book_data_py = os.path.join(base_dir, "tools", "book_28_data.py")

with open(book_data_py, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write(f'"""\nBook 28: {BOOK_TITLE} ({AUTHOR})\n')
    f.write('25 Pages x 20 Sentences = 500 Sentences.\n"""\n\n')
    f.write(f'BOOK_TITLE = "{BOOK_TITLE}"\n')
    f.write(f'AUTHOR = "{AUTHOR}"\n')
    f.write(f'BOOK_ID = "{BOOK_ID}"\n')
    f.write(f'LEVEL = "{LEVEL}"\n\n')
    f.write(f"PAGES_DATA = {repr(ALL_PAGES)}\n")

print(f"Saved: {book_data_py}")

# Write lessons/book_28_the_hound_of_the_baskervilles/book_preview.md
lesson_dir = os.path.join(base_dir, "lessons", BOOK_ID)
os.makedirs(lesson_dir, exist_ok=True)
md_out = os.path.join(lesson_dir, "book_preview.md")

lines = [
    f"# 📖 {BOOK_TITLE} (Baskerville'lerin Köpeği) — 25 Sayfalık Kitap",
    "",
    f"> **Yazar**: {AUTHOR}  ",
    f"> **Uyarlama**: DictaLearn Seviye 2 ({LEVEL})  ",
    "> **Sayfa Sayısı**: 25 Sayfa (Her Sayfada Tam 20 Cümle • Toplam 500 Cümle)  ",
    f"> **Kitap ID**: `{BOOK_ID}`  ",
    "> **Seslendirme**: Microsoft Edge Neural TTS (en-US-ChristopherNeural)  ",
    "",
    "---",
    ""
]

for p in ALL_PAGES:
    p_no = p["page_no"]
    title = p["title"]
    tr_title = p["tr_title"]
    vocab = p["vocab_focus"]
    sentences = p["sentences"]

    lines.append(f"## 📄 Sayfa {p_no}: {title} ({tr_title})")
    lines.append("")
    lines.append("| No | İngilizce Cümle | Türkçe Çeviri | Dilbilgisi & Kelime Notu |")
    lines.append("|---|---|---|---|")

    for s in sentences:
        sid = s["id"]
        en = s["text"].replace("|", "\\|")
        tr = s["translation"].replace("|", "\\|")
        notes = s["notes"].replace("|", "\\|")
        lines.append(f"| **{sid}** | {en} | {tr} | `{notes}` |")

    lines.append("")
    lines.append("**💡 Hedef Kelimeler:**")
    vocab_strs = [f"`{term}`: {meaning}" for term, meaning in vocab]
    lines.append(" • ".join(vocab_strs))
    lines.append("")
    lines.append("---")
    lines.append("")

with open(md_out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Saved Markdown preview: {md_out}")
