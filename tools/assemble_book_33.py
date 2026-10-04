# -*- coding: utf-8 -*-
"""
Assemble Book 33: The Strange Case of Dr. Jekyll and Mr. Hyde (Robert Louis Stevenson)
Merges all 25 pages (500 sentences, 200 vocabulary items),
validates dataset integrity, writes tools/book_33_data.py,
and creates lessons/book_33_dr_jekyll_and_mr_hyde/book_preview.md.
"""

import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from tools.create_book_33_part1 import PAGES_1_TO_8
from tools.create_book_33_part2 import PAGES_9_TO_16
from tools.create_book_33_part3 import PAGES_17_TO_25

ALL_PAGES = PAGES_1_TO_8 + PAGES_9_TO_16 + PAGES_17_TO_25

print(f"Total pages collected: {len(ALL_PAGES)}")

# Validation
assert len(ALL_PAGES) == 25, f"Expected 25 pages, got {len(ALL_PAGES)}"

total_sentences = 0
total_vocab = 0

for idx, page in enumerate(ALL_PAGES, start=1):
    assert page["page_no"] == idx, f"Page number mismatch at index {idx}: {page['page_no']}"
    assert len(page["vocab_focus"]) == 8, f"Page {idx} vocab count is {len(page['vocab_focus'])}, expected 8"
    assert len(page["sentences"]) == 20, f"Page {idx} sentence count is {len(page['sentences'])}, expected 20"
    
    total_vocab += len(page["vocab_focus"])
    for s_idx, s in enumerate(page["sentences"], start=1):
        expected_id = (idx - 1) * 20 + s_idx
        assert s["id"] == expected_id, f"Sentence ID mismatch on page {idx}: got {s['id']}, expected {expected_id}"
        assert s["text"].strip(), f"Empty sentence text on page {idx}, id {s['id']}"
        assert s["translation"].strip(), f"Empty sentence translation on page {idx}, id {s['id']}"
        assert s["notes"].strip(), f"Empty sentence notes on page {idx}, id {s['id']}"
        assert "\n" not in s["text"], f"Sentence {s['id']} has newline in text!"
        assert "\n" not in s["translation"], f"Sentence {s['id']} has newline in translation!"
        assert "\n" not in s["notes"], f"Sentence {s['id']} has newline in notes!"
        total_sentences += 1

print(f"Validation successful! Total pages: {len(ALL_PAGES)}, sentences: {total_sentences}, vocab: {total_vocab}")

# Write tools/book_33_data.py
data_path = os.path.join(os.path.dirname(__file__), "book_33_data.py")
with open(data_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nBook 33: The Strange Case of Dr. Jekyll and Mr. Hyde - Complete Dataset (25 Pages, 500 Sentences, 200 Vocab)\nRobert Louis Stevenson\n"""\n\n')
    f.write(f"BOOK_DATA = {repr(ALL_PAGES)}\n")

print(f"Written book data to {data_path}")

# Create markdown preview
out_dir = os.path.join("lessons", "book_33_dr_jekyll_and_mr_hyde")
os.makedirs(out_dir, exist_ok=True)
md_path = os.path.join(out_dir, "book_preview.md")

with open(md_path, "w", encoding="utf-8") as f:
    f.write("# 📖 The Strange Case of Dr. Jekyll and Mr. Hyde (Dr. Jekyll ve Bay Hyde) — 25 Sayfalık Kitap\n\n")
    f.write("> **Yazar**: Robert Louis Stevenson  \n")
    f.write("> **Uyarlama**: DictaLearn Seviye 2 (CEFR B1 (Intermediate / Orta Seviye))  \n")
    f.write("> **Sayfa Sayısı**: 25 Sayfa (Her Sayfada Tam 20 Cümle • Toplam 500 Cümle)  \n")
    f.write("> **Kitap ID**: `book_33_dr_jekyll_and_mr_hyde`  \n")
    f.write("> **Seslendirme**: Microsoft Edge Neural TTS (en-US-ChristopherNeural)  \n\n")
    f.write("---\n\n")

    for page in ALL_PAGES:
        f.write(f"## 📄 Sayfa {page['page_no']}: {page['title']} ({page['tr_title']})\n\n")
        f.write("| No | İngilizce Cümle | Türkçe Çeviri | Dilbilgisi & Kelime Notu |\n")
        f.write("|---|---|---|---|\n")
        for s in page["sentences"]:
            text = s["text"].replace("|", "\\|")
            tr = s["translation"].replace("|", "\\|")
            notes = s["notes"].replace("|", "\\|")
            f.write(f"| **{s['id']}** | {text} | {tr} | `{notes}` |\n")
        f.write("\n**💡 Hedef Kelimeler:**\n")
        vocab_str = " • ".join([f"`{w}`: {m}" for w, m in page["vocab_focus"]])
        f.write(f"{vocab_str}\n\n")
        f.write("---\n\n")

print(f"Written preview markdown to {md_path}")
