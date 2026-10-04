# -*- coding: utf-8 -*-
"""
Full Generator and Assembler for Book 27: The Red-Headed League
Sir Arthur Conan Doyle (Sherlock Holmes)
25 Pages x 20 Sentences = 500 Sentences.
200 Vocabulary Focus items.
CEFR B1 Graded Reader Edition.
"""

import os
import sys

# Configure UTF-8 for console output on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

BOOK_TITLE = "The Red-Headed League"
AUTHOR = "Sir Arthur Conan Doyle"
BOOK_ID = "book_27_the_red_headed_league"
LEVEL = "CEFR B1 (Intermediate / Orta Seviye)"

# Import pages 1 to 3 from create_book_27_part1
from create_book_27_part1 import PAGES_1_TO_13 as INITIAL_PAGES

print(f"Loaded {len(INITIAL_PAGES)} initial pages for Book 27.")
