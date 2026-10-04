# -*- coding: utf-8 -*-
"""
Universal Markdown-to-Lesson Pipeline Builder for DictaLearn.
Parses Gemini/human-generated structured Markdown book files (e.g., 25 pages x 20 sentences = 500 sentences),
validates the dataset, synthesizes neural studio audio (Edge-TTS), generates ReportLab PDF,
creates millisecond-accurate lesson.json, and synchronizes to Web and Android apps.

Usage:
  python tools/build_from_markdown.py lessons/book_26_a_scandal_in_bohemia/book_preview.md
  python tools/build_from_markdown.py path/to/book.md --validate-only
  python tools/build_from_markdown.py path/to/book.md --skip-audio
"""

import argparse
import asyncio
import io
import json
import os
import re
import shutil
import sys

# Configure UTF-8 for console output on Windows
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import numpy as np
import soundfile as sf
import edge_tts

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfgen import canvas

VOICE = "en-US-ChristopherNeural"
INTER_SENTENCE_PAUSE_SEC = 0.40  # 400ms pause between sentences
INTER_PAGE_PAUSE_SEC = 1.00      # 1000ms pause at page boundaries


def setup_fonts():
    font_arial = "C:/Windows/Fonts/arial.ttf"
    font_arial_bold = "C:/Windows/Fonts/arialbd.ttf"
    font_arial_italic = "C:/Windows/Fonts/ariali.ttf"
    font_georgia = "C:/Windows/Fonts/georgia.ttf"
    font_georgia_bold = "C:/Windows/Fonts/georgiab.ttf"

    if os.path.exists(font_arial):
        pdfmetrics.registerFont(TTFont("AppSans", font_arial))
    if os.path.exists(font_arial_bold):
        pdfmetrics.registerFont(TTFont("AppSans-Bold", font_arial_bold))
    if os.path.exists(font_arial_italic):
        pdfmetrics.registerFont(TTFont("AppSans-Italic", font_arial_italic))

    if os.path.exists(font_georgia):
        pdfmetrics.registerFont(TTFont("AppSerif", font_georgia))
    else:
        pdfmetrics.registerFont(TTFont("AppSerif", font_arial))

    if os.path.exists(font_georgia_bold):
        pdfmetrics.registerFont(TTFont("AppSerif-Bold", font_georgia_bold))
    else:
        pdfmetrics.registerFont(TTFont("AppSerif-Bold", font_arial_bold))


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        page_num = self._pageNumber
        if page_num == 1:
            return

        story_page_num = page_num - 1
        total_story_pages = total_pages - 1

        self.saveState()

        # Running Top Header
        self.setFont("AppSans-Bold", 8)
        self.setFillColor(colors.HexColor("#0284C7"))
        self.drawString(34, 810, "DICTALEARN GRADED CLASSICS & DICTATION SERIES")

        book_header_title = getattr(self, "book_header_title", "Graded Reader")
        self.setFont("AppSans", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawRightString(561, 810, f"{book_header_title}  |  Sayfa {story_page_num} / {total_story_pages}")

        # Top Header Divider Line
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.8)
        self.line(34, 802, 561, 802)

        # Running Bottom Footer
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.8)
        self.line(34, 36, 561, 36)

        self.setFont("AppSans-Italic", 7.5)
        self.setFillColor(colors.HexColor("#94A3B8"))
        self.drawString(34, 24, "DictaLearn Open Library • İnteraktif Dikte, Okuma ve Shadowing • www.dictalearn.org")

        self.setFont("AppSans-Bold", 8)
        self.setFillColor(colors.HexColor("#334155"))
        self.drawRightString(561, 24, f"Sayfa {story_page_num} / {total_story_pages}")

        self.restoreState()


def parse_markdown_book(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract metadata
    book_title_match = re.search(r"^#\s*📖?\s*(.*?)(?:—.*)?$", content, re.MULTILINE)
    book_title = book_title_match.group(1).strip() if book_title_match else os.path.splitext(os.path.basename(md_path))[0]

    author_match = re.search(r">\s*\*\*Yazar\*\*:\s*(.*?)$", content, re.MULTILINE)
    author = author_match.group(1).strip() if author_match else "Unknown Author"

    book_id_match = re.search(r">\s*\*\*Kitap ID\*\*:\s*`?(book_[a-zA-Z0-9_]+)`?", content, re.MULTILINE)
    if book_id_match:
        book_id = book_id_match.group(1).strip()
    else:
        # Fallback to parent directory name if starts with book_
        parent_dir = os.path.basename(os.path.dirname(os.path.abspath(md_path)))
        if parent_dir.startswith("book_"):
            book_id = parent_dir
        else:
            book_id = "book_custom"

    level_match = re.search(r">\s*\*\*Uyarlama\*\*:\s*(.*?)$", content, re.MULTILINE)
    level = level_match.group(1).strip() if level_match else "CEFR B1 (Intermediate)"

    # Split by pages: "## 📄 Sayfa X:" or "## Sayfa X:"
    page_chunks = re.split(r"(?=##\s*📄?\s*Sayfa\s+\d+)", content)
    pages_data = []

    for chunk in page_chunks:
        chunk = chunk.strip()
        if not re.match(r"^##\s*📄?\s*Sayfa\s+\d+", chunk):
            continue

        header_line_match = re.search(r"^##\s*📄?\s*Sayfa\s+(\d+)\s*:\s*(.*?)$", chunk, re.MULTILINE)
        if not header_line_match:
            continue

        page_no = int(header_line_match.group(1))
        full_title_str = header_line_match.group(2).strip()

        # Split English and Turkish title: "Title (Türkçe Başlık)"
        title_match = re.match(r"^(.*?)\s*\((.*?)\)\s*$", full_title_str)
        if title_match:
            title = title_match.group(1).strip()
            tr_title = title_match.group(2).strip()
        else:
            title = full_title_str
            tr_title = full_title_str

        # Parse sentences table
        sentences = []
        lines = chunk.splitlines()
        in_table = False

        for line in lines:
            line = line.strip()
            if not line.startswith("|"):
                continue

            parts = [p.strip() for p in line.split("|")]
            # Format: ['', 'No', 'İngilizce Cümle', 'Türkçe Çeviri', 'Dilbilgisi & Kelime Notu', '']
            if len(parts) < 5:
                continue

            id_str = parts[1].replace("*", "").strip()
            if not id_str.isdigit():
                continue  # header or separator row

            sid = int(id_str)
            en_text = parts[2].strip()
            tr_text = parts[3].strip()
            note_text = parts[4].strip() if len(parts) > 4 else ""

            # Unescape markdown pipes
            en_text = en_text.replace("\\|", "|")
            tr_text = tr_text.replace("\\|", "|")
            note_text = note_text.replace("\\|", "|").strip("`")

            sentences.append({
                "id": sid,
                "text": en_text,
                "translation": tr_text,
                "notes": f"Sayfa {page_no} | {note_text}" if not note_text.startswith("Sayfa") else note_text
            })

        # Parse vocab focus
        vocab_focus = []
        vocab_match = re.search(r"\*\*💡\s*Hedef Kelimeler:\*\*\s*(.*?)(?:\n---|\Z)", chunk, re.DOTALL)
        if vocab_match:
            vocab_raw = vocab_match.group(1).strip()
            items = re.split(r"•", vocab_raw)
            for it in items:
                it = it.strip().strip("`").strip()
                if ":" in it:
                    w, m = it.split(":", 1)
                    vocab_focus.append((w.strip().strip("`"), m.strip()))

        pages_data.append({
            "page_no": page_no,
            "title": title,
            "tr_title": tr_title,
            "vocab_focus": vocab_focus,
            "sentences": sentences
        })

    # Sort pages by page_no
    pages_data.sort(key=lambda p: p["page_no"])

    return {
        "book_title": book_title,
        "author": author,
        "book_id": book_id,
        "level": level,
        "pages_data": pages_data
    }


def validate_book_data(parsed_book):
    pages = parsed_book["pages_data"]
    total_pages = len(pages)
    total_sentences = sum(len(p["sentences"]) for p in pages)
    total_vocab = sum(len(p["vocab_focus"]) for p in pages)

    print("\n🔍 Validating Book Dataset:")
    print(f"  • Title: {parsed_book['book_title']}")
    print(f"  • Author: {parsed_book['author']}")
    print(f"  • Book ID: {parsed_book['book_id']}")
    print(f"  • Pages Detected: {total_pages}")
    print(f"  • Total Sentences: {total_sentences}")
    print(f"  • Total Vocab Terms: {total_vocab}")

    issues = []

    if total_pages == 0:
        issues.append("No valid pages found in markdown file!")

    expected_id = 1
    for p in pages:
        p_no = p["page_no"]
        s_count = len(p["sentences"])
        v_count = len(p["vocab_focus"])

        if s_count != 20:
            issues.append(f"Page {p_no} has {s_count} sentences (expected exactly 20).")

        if v_count != 8 and v_count != 0:
            print(f"  ⚠️ Warning: Page {p_no} has {v_count} vocab items (standard is 8).")

        for s in p["sentences"]:
            if s["id"] != expected_id:
                issues.append(f"Sentence ID mismatch: expected {expected_id}, found {s['id']} on page {p_no}.")
            expected_id += 1

    if issues:
        print("\n❌ Validation Failed with Issues:")
        for iss in issues:
            print(f"  - {iss}")
        return False
    else:
        print("\n✅ Validation Passed! 100% compliant with DictaLearn format.")
        return True


def generate_book_pdf(parsed_book, output_pdf_path):
    setup_fonts()

    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=A4,
        leftMargin=34,
        rightMargin=34,
        topMargin=42,
        bottomMargin=42,
    )

    styles = getSampleStyleSheet()

    style_cover_badge = ParagraphStyle(
        "CoverBadge",
        fontName="AppSans-Bold",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#0284C7"),
        alignment=TA_CENTER,
        spaceAfter=8,
    )
    style_cover_title = ParagraphStyle(
        "CoverTitle",
        fontName="AppSerif-Bold",
        fontSize=24,
        leading=30,
        textColor=colors.HexColor("#0F172A"),
        alignment=TA_CENTER,
        spaceAfter=6,
    )
    style_cover_subtitle = ParagraphStyle(
        "CoverSubtitle",
        fontName="AppSans",
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#475569"),
        alignment=TA_CENTER,
        spaceAfter=10,
    )
    style_cover_author = ParagraphStyle(
        "CoverAuthor",
        fontName="AppSerif-Bold",
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#D97706"),
        alignment=TA_CENTER,
        spaceAfter=18,
    )

    style_page_header_title = ParagraphStyle(
        "PageHeaderTitle",
        fontName="AppSerif-Bold",
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#0F172A"),
    )
    style_col_h_en = ParagraphStyle(
        "ColHEn",
        fontName="AppSans-Bold",
        fontSize=7.2,
        leading=9,
        textColor=colors.HexColor("#0369A1"),
    )
    style_col_h_tr = ParagraphStyle(
        "ColHTr",
        fontName="AppSans-Bold",
        fontSize=7.2,
        leading=9,
        textColor=colors.HexColor("#0D9488"),
    )
    style_en_sentence = ParagraphStyle(
        "EnSentence",
        fontName="AppSerif",
        fontSize=7.0,
        leading=8.8,
        textColor=colors.HexColor("#0F172A"),
    )
    style_tr_sentence = ParagraphStyle(
        "TrSentence",
        fontName="AppSans",
        fontSize=6.6,
        leading=8.4,
        textColor=colors.HexColor("#334155"),
    )
    style_vocab_header = ParagraphStyle(
        "VocabHeader",
        fontName="AppSans-Bold",
        fontSize=7.0,
        leading=8.8,
        textColor=colors.HexColor("#B45309"),
    )
    style_vocab_item = ParagraphStyle(
        "VocabItem",
        fontName="AppSans",
        fontSize=6.6,
        leading=8.4,
        textColor=colors.HexColor("#1E293B"),
    )

    elements = []

    # COVER PAGE
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("★ DICTALEARN GRADED READERS & DICTATION SERIES ★", style_cover_badge))
    elements.append(Spacer(1, 8))
    elements.append(Paragraph(parsed_book["book_title"].upper(), style_cover_title))
    elements.append(Paragraph(f"{parsed_book['book_title']} — {len(parsed_book['pages_data'])} Sayfalık Eksiksiz Okuma & Dikte Kitabı", style_cover_subtitle))
    elements.append(Paragraph(parsed_book["author"], style_cover_author))

    total_s = sum(len(p['sentences']) for p in parsed_book['pages_data'])
    total_p = len(parsed_book['pages_data'])
    cover_info_html = f"""
    <b>Kitap Seviyesi:</b> {parsed_book['level']}<br/>
    <b>Sayfa Sayısı:</b> {total_p} Sayfa (Her Sayfada Tam 20 Cümle • Toplam {total_s} Cümle)<br/>
    <b>Ses Formatları:</b> Stüdyo MP3 + Kayıpsız WAV (Christopher Neural Narrator)<br/>
    <b>Metot:</b> İki Sütunlu Paralel Metin, Milisaniye Senkron Dikte & Gölgeleme (Shadowing)<br/>
    <b>Kapsam:</b> {total_s} Cümle Analizi, {total_p * 8} Hedef Kelime Odağı ve Doğal Türkçe Çeviriler
    """
    cover_table = Table([[Paragraph(cover_info_html, ParagraphStyle("CI", fontName="AppSans", fontSize=9, leading=14))]], colWidths=[520])
    cover_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor("#0284C7")),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
    ]))
    elements.append(cover_table)
    elements.append(Spacer(1, 14))

    col1 = Paragraph("<b>🎙️ Doğal Stüdyo Sesi</b><br/>Robotik olmayan, insansı tonlama ve nefes hissiyatına sahip stüdyo seslendirmesi (WAV & MP3).", ParagraphStyle("Col1", fontName="AppSans", fontSize=8, leading=11, textColor=colors.HexColor("#334155")))
    col2 = Paragraph("<b>✍️ Dikte & Shadowing</b><br/>DictaLearn Web ve Android uygulamalarında klavye ile yazarak veya sesli tekrar ederek çalışabilirsiniz.", ParagraphStyle("Col2", fontName="AppSans", fontSize=8, leading=11, textColor=colors.HexColor("#334155")))
    col3 = Paragraph("<b>📖 Sayfa Başına 20 Cümle</b><br/>Her sayfada tam 20 cümle yer alır. İngilizce orijinal metin ve Türkçe çeviri yan yana paralel sunulur.", ParagraphStyle("Col3", fontName="AppSans", fontSize=8, leading=11, textColor=colors.HexColor("#334155")))

    feat_table = Table([[col1, col2, col3]], colWidths=[168, 168, 168])
    feat_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    elements.append(feat_table)
    elements.append(Spacer(1, 14))

    guide_html = """
    <b>📘 Bu Kitaptan Nasıl En Yüksek Verim Alınır?</b><br/>
    <b>1. Adım (Dinleme & Okuma):</b> Sayfadaki 20 cümleyi ses dosyası eşliğinde dikkatle dinleyin.<br/>
    <b>2. Adım (Klavye Dikte):</b> DictaLearn uygulamasında cümleyi dinleyip eksiksiz yazın; anlık harf ve kelime farklarını görün.<br/>
    <b>3. Adım (Shadowing & Telaffuz):</b> Spikerin hemen ardından cümleyi yüksek sesle taklit ederek telaffuzunuzu pekiştirin.<br/>
    <b>4. Adım (Kelime & Çeviri Pekiştirme):</b> Sayfa altındaki kelime tahlilleri ve Türkçe karşılıkları ile anlamı kalıcılaştırın.
    """
    guide_table = Table([[Paragraph(guide_html, ParagraphStyle("Guide", fontName="AppSans", fontSize=8, leading=12))]], colWidths=[520])
    guide_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#93C5FD")),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    elements.append(guide_table)
    elements.append(PageBreak())

    # STORY PAGES
    for p_data in parsed_book["pages_data"]:
        page_no = p_data["page_no"]
        page_title = p_data["title"]
        tr_title = p_data["tr_title"]
        sentences = p_data["sentences"]
        vocab_items = p_data.get("vocab_focus", [])

        header_text = f"<b>Bölüm {page_no}: {page_title}</b> <font color='#64748B' size='8'>({tr_title})</font>"
        elements.append(Paragraph(header_text, style_page_header_title))
        elements.append(Spacer(1, 2))

        table_rows = [
            [
                Paragraph("📖 <b>ENGLISH STORY TEXT (ORİJİNAL İNGİLİZCE)</b>", style_col_h_en),
                Paragraph("🇹🇷 <b>PARALEL ÇEVİRİ (TÜRKÇE KARŞILIĞI)</b>", style_col_h_tr)
            ]
        ]

        for s in sentences:
            sid = s["id"]
            en_html = f"<b>[{sid}]</b> {s['text']}"
            tr_html = f"<b>[{sid}]</b> {s['translation']}"
            table_rows.append([
                Paragraph(en_html, style_en_sentence),
                Paragraph(tr_html, style_tr_sentence)
            ])

        story_table = Table(table_rows, colWidths=[260, 260])
        story_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), colors.HexColor("#F0F9FF")),
            ('BACKGROUND', (1,0), (1,0), colors.HexColor("#F0FDFA")),
            ('BOX', (0,0), (-1,-1), 0.7, colors.HexColor("#CBD5E1")),
            ('INNERGRID', (0,0), (-1,-1), 0.3, colors.HexColor("#E2E8F0")),
            ('TOPPADDING', (0,0), (-1,-1), 1.4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1.4),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        elements.append(story_table)

        if vocab_items:
            elements.append(Spacer(1, 3))
            vocab_cells = []
            for i in range(0, len(vocab_items), 2):
                pair = vocab_items[i:i+2]
                row_cells = []
                for term, meaning in pair:
                    p_txt = f"• <b>{term}</b>: {meaning}"
                    row_cells.append(Paragraph(p_txt, style_vocab_item))
                while len(row_cells) < 2:
                    row_cells.append(Paragraph("", style_vocab_item))
                vocab_cells.append(row_cells)

            vocab_table = Table(
                [[Paragraph("💡 <b>BU SAYFANIN HEDEF KELİMELERİ VE ANLAMLARI</b>", style_vocab_header), ""]] + vocab_cells,
                colWidths=[260, 260]
            )
            vocab_table.setStyle(TableStyle([
                ('SPAN', (0,0), (1,0)),
                ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#FEF3C7")),
                ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#FFFBEB")),
                ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor("#F59E0B")),
                ('INNERGRID', (0,0), (-1,-1), 0.3, colors.HexColor("#FDE68A")),
                ('TOPPADDING', (0,0), (-1,-1), 1.2),
                ('BOTTOMPADDING', (0,0), (-1,-1), 1.2),
                ('LEFTPADDING', (0,0), (-1,-1), 4),
                ('RIGHTPADDING', (0,0), (-1,-1), 4),
                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ]))
            elements.append(vocab_table)

        elements.append(PageBreak())

    def on_first_page(canvas_obj, doc_obj):
        canvas_obj.book_header_title = f"{parsed_book['book_title']} — {parsed_book['author']}"

    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"✅ Generated Professional PDF: {output_pdf_path}")


async def synthesize_segment(sem, seg_id, text, voice):
    async with sem:
        communicate = edge_tts.Communicate(text, voice)
        audio_bytes = bytearray()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_bytes.extend(chunk["data"])
        data, sr = sf.read(io.BytesIO(audio_bytes), dtype="float32")
        if len(data.shape) > 1:
            data = data.mean(axis=1)
        return seg_id, data, sr


async def generate_lesson_audio(parsed_book, lesson_path, output_dir, voice=VOICE):
    all_sentences = []
    for page in parsed_book["pages_data"]:
        for s in page["sentences"]:
            all_sentences.append({
                "id": s["id"],
                "text": s["text"],
                "translation": s["translation"],
                "notes": s["notes"],
            })

    total_count = len(all_sentences)
    print(f"\n🎙️ Synthesizing {total_count} Neural Audio Segments ({voice})...")

    sem = asyncio.Semaphore(8)
    tasks = [
        synthesize_segment(sem, s["id"], s["text"], voice)
        for s in all_sentences
    ]

    results = []
    for i, coro in enumerate(asyncio.as_completed(tasks)):
        res = await coro
        results.append(res)
        if (i + 1) % 25 == 0 or (i + 1) == total_count:
            print(f"  -> Synthesized {i + 1}/{total_count} segments ({int((i+1)/total_count*100)}%)...")

    results.sort(key=lambda x: x[0])
    sample_rate = results[0][2]

    all_audio_chunks = []
    current_sample = 0

    # Initial lead-in silence (300ms)
    lead_silence = np.zeros(int(sample_rate * 0.3), dtype=np.float32)
    all_audio_chunks.append(lead_silence)
    current_sample += len(lead_silence)

    updated_segments = []

    for idx, (seg_id, audio_data, sr) in enumerate(results):
        seg = next(s for s in all_sentences if s["id"] == seg_id)

        start_ms = int(round((current_sample / sample_rate) * 1000))
        all_audio_chunks.append(audio_data)
        current_sample += len(audio_data)
        end_ms = int(round((current_sample / sample_rate) * 1000))

        updated_segments.append({
            "id": seg["id"],
            "start_ms": start_ms,
            "end_ms": end_ms,
            "text": seg["text"],
            "translation": seg["translation"],
            "notes": seg["notes"]
        })

        # Check pause duration
        is_page_end = (seg_id % 20 == 0)
        pause_sec = INTER_PAGE_PAUSE_SEC if is_page_end else INTER_SENTENCE_PAUSE_SEC

        if idx < len(results) - 1:
            pause_samples = int(sample_rate * pause_sec)
            silence_chunk = np.zeros(pause_samples, dtype=np.float32)
            all_audio_chunks.append(silence_chunk)
            current_sample += pause_samples

    # Trailing silence
    trailing_silence = np.zeros(int(sample_rate * 0.5), dtype=np.float32)
    all_audio_chunks.append(trailing_silence)

    full_audio = np.concatenate(all_audio_chunks)
    total_sec = len(full_audio) / sample_rate
    print(f"Total concatenated audio duration: {total_sec / 60:.2f} minutes ({total_sec:.1f}s)")

    wav_path = os.path.join(output_dir, "audio.wav")
    sf.write(wav_path, full_audio, sample_rate, subtype="PCM_16")
    print(f"Saved PCM WAV: {wav_path}")

    # Generate MP3
    mp3_path = os.path.join(output_dir, "audio.mp3")
    try:
        from pydub import AudioSegment
        audio_seg = AudioSegment.from_wav(wav_path)
        audio_seg.export(mp3_path, format="mp3", bitrate="128k")
        print(f"Exported MP3 (128kbps): {mp3_path}")
    except Exception as e:
        print(f"Warning: pydub export failed ({e}), keeping WAV as primary.")
        shutil.copy2(wav_path, mp3_path)

    # Save lesson.json
    lesson_data = {
        "schema_version": 1,
        "lesson_id": parsed_book["book_id"],
        "title": f"{parsed_book['book_title']} ({len(parsed_book['pages_data'])} Sayfa / {len(all_sentences)} Cümle / Graded Reader)",
        "source_lang": "en",
        "target_lang": "tr",
        "audio_file": "audio.mp3",
        "attribution": {
            "source": f"{parsed_book['author']} / Public Domain / Graded Reader Adaptasyonu ({len(parsed_book['pages_data'])} Sayfa x 20 Cümle)",
            "license": "Public Domain"
        },
        "segments": updated_segments
    }

    with open(lesson_path, "w", encoding="utf-8") as f:
        json.dump(lesson_data, f, ensure_ascii=False, indent=2)
    print(f"Saved lesson.json with {len(updated_segments)} timed segments.")


def sync_assets(book_id, lesson_dir, base_repo_dir):
    web_dest = os.path.join(base_repo_dir, "Web", "public", "lessons", book_id)
    android_dest = os.path.join(base_repo_dir, "Android", "app", "src", "main", "assets", "lessons", book_id)

    for dest in [web_dest, android_dest]:
        os.makedirs(dest, exist_ok=True)
        for fname in os.listdir(lesson_dir):
            if fname.endswith((".json", ".mp3", ".wav", ".pdf", ".md")):
                src_f = os.path.join(lesson_dir, fname)
                shutil.copy2(src_f, os.path.join(dest, fname))
                print(f"  -> Synced {fname} to {dest}")


def update_web_app_presets(parsed_book, base_repo_dir):
    app_tsx = os.path.join(base_repo_dir, "Web", "src", "App.tsx")
    if not os.path.exists(app_tsx):
        return

    with open(app_tsx, "r", encoding="utf-8") as f:
        code = f.read()

    book_id = parsed_book["book_id"]
    if f"id: '{book_id}'" in code:
        print(f"Book '{book_id}' is already registered in Web App.tsx.")
        return

    # Extract book number from book_id (e.g. book_26 -> 26)
    num_match = re.search(r"book_(\d+)", book_id)
    book_num = num_match.group(1) if num_match else "New"

    entry = f"""  {{
    id: '{book_id}',
    name: "{book_num}. {parsed_book['book_title']} ({len(parsed_book['pages_data'])} Sayfa / {sum(len(p['sentences']) for p in parsed_book['pages_data'])} Cümle)",
    jsonUrl: '/lessons/{book_id}/lesson.json',
    audioUrl: '/lessons/{book_id}/audio.mp3',
    pdfUrl: '/lessons/{book_id}/{book_id}.pdf',
  }},
"""

    # Insert before 'sample_ch01' or at end of PRESET_LESSONS
    if "id: 'sample_ch01'" in code:
        code = code.replace("  {\n    id: 'sample_ch01',", f"{entry}  {{\n    id: 'sample_ch01',")
    else:
        code = re.sub(r"(const PRESET_LESSONS: PresetLesson\[\] = \[)", r"\1\n" + entry, code)

    with open(app_tsx, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Successfully added '{book_id}' to Web/src/App.tsx PRESET_LESSONS!")


async def main():
    parser = argparse.ArgumentParser(description="Universal Markdown-to-Lesson Pipeline Builder for DictaLearn.")
    parser.add_argument("markdown_file", help="Path to input markdown preview file")
    parser.add_argument("--validate-only", action="store_true", help="Only validate markdown structure without generating assets")
    parser.add_argument("--skip-audio", action="store_true", help="Skip TTS audio synthesis (PDF and sync only)")
    parser.add_argument("--voice", default=VOICE, help=f"Edge TTS voice (default: {VOICE})")

    args = parser.parse_args()

    md_path = os.path.abspath(args.markdown_file)
    if not os.path.exists(md_path):
        print(f"Error: File not found: {md_path}")
        sys.exit(1)

    base_repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    parsed_book = parse_markdown_book(md_path)

    is_valid = validate_book_data(parsed_book)
    if not is_valid:
        sys.exit(1)

    if args.validate_only:
        print("\nMarkdown validation completed successfully. Exiting (--validate-only).")
        return

    book_id = parsed_book["book_id"]
    lesson_dir = os.path.join(base_repo_dir, "lessons", book_id)
    os.makedirs(lesson_dir, exist_ok=True)

    pdf_out = os.path.join(lesson_dir, f"{book_id}.pdf")
    lesson_json_path = os.path.join(lesson_dir, "lesson.json")

    # Step 1: Copy markdown file to lesson_dir as book_preview.md
    dest_md = os.path.join(lesson_dir, "book_preview.md")
    if os.path.abspath(md_path) != os.path.abspath(dest_md):
        shutil.copy2(md_path, dest_md)
        print(f"Copied source markdown to: {dest_md}")

    # Step 2: Audio Synthesis
    if not args.skip_audio:
        print("\n=======================================================")
        print("STEP 1: Synthesizing Studio Neural TTS Audio...")
        print("=======================================================")
        await generate_lesson_audio(parsed_book, lesson_json_path, lesson_dir, voice=args.voice)
    else:
        print("\nSkipping audio synthesis (--skip-audio specified).")

    # Step 3: PDF Generation
    print("\n=======================================================")
    print("STEP 2: Generating Professional Two-Column PDF...")
    print("=======================================================")
    generate_book_pdf(parsed_book, pdf_out)

    # Step 4: Asset Syncing
    print("\n=======================================================")
    print("STEP 3: Synchronizing Assets to Web & Android Apps...")
    print("=======================================================")
    sync_assets(book_id, lesson_dir, base_repo_dir)

    # Step 5: Web Menu Registration
    update_web_app_presets(parsed_book, base_repo_dir)

    print(f"\n🎉 Successfully processed and deployed '{parsed_book['book_title']}' ({book_id})!")


if __name__ == "__main__":
    asyncio.run(main())
