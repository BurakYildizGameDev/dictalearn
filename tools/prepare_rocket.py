# -*- coding: utf-8 -*-
import re

with open("gutenberg_full.txt", "r", encoding="utf-8") as f:
    text = f.read()

rocket_text = text[66542:91242]
cleaned = re.sub(r'\[Picture:[^\]]*\]', '', rocket_text)
# clean characters like smart quotes
cleaned = (
    cleaned.replace("‘", "'")
    .replace("’", "'")
    .replace("“", '"')
    .replace("”", '"')
    .replace("—", " — ")
    .replace("–", " - ")
)

# Break into sentences roughly
sentences = []
for p in cleaned.split("\n\n"):
    p_clean = " ".join(p.split())
    if not p_clean or p_clean.startswith("The Remarkable Rocket"):
        continue
    # split by punctuation keeping quotes
    parts = re.split(r'(?<=[.!?])\s+', p_clean)
    for part in parts:
        part = part.strip()
        if part:
            sentences.append(part)

print(f"Total raw sentences found: {len(sentences)}")
with open("tools/rocket_raw_sentences.txt", "w", encoding="utf-8") as f:
    for i, s in enumerate(sentences, 1):
        f.write(f"{i}: {s}\n")
