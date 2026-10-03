# -*- coding: utf-8 -*-
"""
Builds a professional 15-page PDF book for 'The Happy Prince' (Oscar Wilde).
Uses ReportLab with Windows TrueType fonts (Arial/Georgia) for complete Turkish character support.
Outputs:
  lessons/book_01_the_happy_prince/book_01_the_happy_prince.pdf
  (Exact 16-page layout: 1 Cover Page + 15 Story Pages, 20 sentences per story page)
"""

import json
import os
import sys
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
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfgen import canvas

# Import data
try:
    from tools.book_01_data import PAGES_DATA, BOOK_TITLE, AUTHOR, LEVEL
except ImportError:
    from book_01_data import PAGES_DATA, BOOK_TITLE, AUTHOR, LEVEL


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
    """
    Two-pass canvas to dynamically inject page counts and professional running headers/footers.
    """
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
            # Skip running header and footer on cover page
            return

        story_page_num = page_num - 1  # Cover is page 1, story starts at page 2
        total_story_pages = total_pages - 1

        self.saveState()

        # Running Top Header
        self.setFont("AppSans-Bold", 8)
        self.setFillColor(colors.HexColor("#0284C7"))  # Teal / Blue
        self.drawString(36, 810, "DICTALEARN GRADED CLASSICS")

        self.setFont("AppSans", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawRightString(559, 810, f"The Happy Prince — Oscar Wilde  |  Sayfa {story_page_num} / {total_story_pages}")

        # Top Header Divider Line
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.8)
        self.line(36, 802, 559, 802)

        # Running Bottom Footer
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.8)
        self.line(36, 36, 559, 36)

        self.setFont("AppSans-Italic", 7.5)
        self.setFillColor(colors.HexColor("#94A3B8"))
        self.drawString(36, 24, "DictaLearn Open Library • Interaktif Dikte, Okuma ve Shadowing • www.dictalearn.org")

        self.setFont("AppSans-Bold", 8)
        self.setFillColor(colors.HexColor("#334155"))
        self.drawRightString(559, 24, f"Sayfa {story_page_num} / {total_story_pages}")

        self.restoreState()


def generate_book_pdf(output_pdf_path):
    setup_fonts()

    # Setup Document
    # A4: 595.27 x 841.89 points. Margins: 34 pt left/right, 42 pt top/bottom
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=A4,
        leftMargin=34,
        rightMargin=34,
        topMargin=42,
        bottomMargin=42,
    )

    styles = getSampleStyleSheet()

    # Cover typography
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
        fontSize=28,
        leading=34,
        textColor=colors.HexColor("#0F172A"),
        alignment=TA_CENTER,
        spaceAfter=6,
    )

    style_cover_subtitle = ParagraphStyle(
        "CoverSubtitle",
        fontName="AppSans",
        fontSize=13,
        leading=18,
        textColor=colors.HexColor("#475569"),
        alignment=TA_CENTER,
        spaceAfter=12,
    )

    style_cover_author = ParagraphStyle(
        "CoverAuthor",
        fontName="AppSerif-Bold",
        fontSize=15,
        leading=20,
        textColor=colors.HexColor("#D97706"),  # Amber
        alignment=TA_CENTER,
        spaceAfter=20,
    )

    # Story typography
    style_page_header_title = ParagraphStyle(
        "PageHeaderTitle",
        fontName="AppSerif-Bold",
        fontSize=12,
        leading=15,
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
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor("#0F172A"),
    )

    style_tr_sentence = ParagraphStyle(
        "TrSentence",
        fontName="AppSans",
        fontSize=6.8,
        leading=8.8,
        textColor=colors.HexColor("#334155"),
    )

    style_vocab_header = ParagraphStyle(
        "VocabHeader",
        fontName="AppSans-Bold",
        fontSize=7.2,
        leading=9,
        textColor=colors.HexColor("#B45309"),
    )

    style_vocab_item = ParagraphStyle(
        "VocabItem",
        fontName="AppSans",
        fontSize=6.8,
        leading=8.8,
        textColor=colors.HexColor("#1E293B"),
    )

    elements = []

    # ==========================================
    # 1. COVER PAGE (Sayfa 1)
    # ==========================================
    elements.append(Spacer(1, 25))
    elements.append(Paragraph("★ DICTALEARN GRADED READERS & DICTATION SERIES ★", style_cover_badge))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("THE HAPPY PRINCE", style_cover_title))
    elements.append(Paragraph("Mutlu Prens — 15 Sayfalık Eksiksiz İngilizce Okuma & Dikte Kitabı", style_cover_subtitle))
    elements.append(Paragraph("Oscar Wilde", style_cover_author))

    # Cover Summary Box
    cover_info_html = """
    <b>Kitap Seviyesi:</b> CEFR B1 (Intermediate / Orta Seviye)<br/>
    <b>Sayfa Sayısı:</b> 15 Sayfa (Her Sayfada Tam 20 Cümle • Toplam 300 Cümle)<br/>
    <b>Ses Formatları:</b> Stüdyo MP3 + Kayıpsız WAV (Christopher Neural Narrator)<br/>
    <b>Metot:</b> İki Sütunlu Paralel Metin, Milisaniye Senkron Dikte & Gölgeleme (Shadowing)<br/>
    <b>Kapsam:</b> 300+ Cümle Analizi, 120+ Hedef Kelime Odağı ve Türkçe Çeviriler
    """
    cover_info_p = Paragraph(cover_info_html, ParagraphStyle("CoverInfo", fontName="AppSans", fontSize=9.5, leading=15, textColor=colors.HexColor("#1E293B")))
    cover_table = Table([[cover_info_p]], colWidths=[520])
    cover_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor("#0284C7")),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 16),
        ('RIGHTPADDING', (0,0), (-1,-1), 16),
    ]))
    elements.append(cover_table)

    elements.append(Spacer(1, 16))

    # Features 3-Column Box
    col1 = Paragraph("<b>🎙️ Doğal Stüdyo Sesi</b><br/>Robotik olmayan, insansı tonlama ve nefes hissiyatına sahip stüdyo seslendirmesi (WAV & MP3).", ParagraphStyle("Col1", fontName="AppSans", fontSize=8.5, leading=12, textColor=colors.HexColor("#334155")))
    col2 = Paragraph("<b>✍️ Dikte & Shadowing</b><br/>DictaLearn Web ve Android uygulamalarında klavye ile yazarak veya sesli tekrar ederek çalışabilirsiniz.", ParagraphStyle("Col2", fontName="AppSans", fontSize=8.5, leading=12, textColor=colors.HexColor("#334155")))
    col3 = Paragraph("<b>📖 Sayfa Başına 20 Cümle</b><br/>Her sayfada tam 20 cümle yer alır. İngilizce orijinal metin ve Türkçe çeviri yan yana paralel sunulur.", ParagraphStyle("Col3", fontName="AppSans", fontSize=8.5, leading=12, textColor=colors.HexColor("#334155")))

    feat_table = Table([[col1, col2, col3]], colWidths=[168, 168, 168])
    feat_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    elements.append(feat_table)

    elements.append(Spacer(1, 18))

    # Instructions
    guide_html = """
    <b>📘 Bu Kitaptan Nasıl En Yüksek Verim Alınır?</b><br/>
    <b>1. Adım (Dinleme & Okuma):</b> Sayfadaki 20 cümleyi ses dosyası eşliğinde (MP3/WAV) dikkatle dinleyin.<br/>
    <b>2. Adım (Klavye Dikte):</b> DictaLearn uygulamasında cümleyi dinleyip eksiksiz yazın; anlık harf ve kelime farklarını görün.<br/>
    <b>3. Adım (Shadowing & Telaffuz):</b> Spikerin hemen ardından cümleyi yüksek sesle taklit ederek telaffuzunuzu pekiştirin.<br/>
    <b>4. Adım (Kelime & Çeviri Pekiştirme):</b> Sayfa altındaki kelime tahlilleri ve Türkçe karşılıkları ile anlamı kalıcılaştırın.
    """
    guide_p = Paragraph(guide_html, ParagraphStyle("Guide", fontName="AppSans", fontSize=8.5, leading=13.5, textColor=colors.HexColor("#1E293B")))
    guide_table = Table([[guide_p]], colWidths=[520])
    guide_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#93C5FD")),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    elements.append(guide_table)

    elements.append(PageBreak())

    # ==========================================
    # 2. STORY PAGES (1 TO 15)
    # Exactly 20 sentences per page
    # ==========================================
    for p_data in PAGES_DATA:
        page_no = p_data["page_no"]
        page_title = p_data["title"]
        tr_title = p_data["tr_title"]
        sentences = p_data["sentences"]
        vocab_items = p_data.get("vocab_focus", [])

        # Header Title
        header_text = f"<b>Bölüm {page_no}: {page_title}</b> <font color='#64748B' size='9'>({tr_title})</font>"
        elements.append(Paragraph(header_text, style_page_header_title))
        elements.append(Spacer(1, 3))

        # 20 Sentences Parallel Table
        table_rows = []
        # Header Row
        table_rows.append([
            Paragraph("📖 <b>ENGLISH STORY TEXT (ORİJİNAL İNGİLİZCE)</b>", style_col_h_en),
            Paragraph("🇹🇷 <b>PARALEL ÇEVİRİ (TÜRKÇE KARŞILIĞI)</b>", style_col_h_tr)
        ])

        for s in sentences:
            sid = s["id"]
            en_html = f"<b>[{sid}]</b> {s['text']}"
            tr_html = f"<b>[{sid}]</b> {s['translation']}"
            table_rows.append([
                Paragraph(en_html, style_en_sentence),
                Paragraph(tr_html, style_tr_sentence)
            ])

        story_table = Table(table_rows, colWidths=[260, 260])
        table_style_list = [
            ('BACKGROUND', (0,0), (0,0), colors.HexColor("#F0F9FF")),
            ('BACKGROUND', (1,0), (1,0), colors.HexColor("#F0FDFA")),
            ('BOX', (0,0), (-1,-1), 0.7, colors.HexColor("#CBD5E1")),
            ('INNERGRID', (0,0), (-1,-1), 0.3, colors.HexColor("#E2E8F0")),
            ('TOPPADDING', (0,0), (-1,-1), 1.6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1.6),
            ('LEFTPADDING', (0,0), (-1,-1), 4.5),
            ('RIGHTPADDING', (0,0), (-1,-1), 4.5),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]
        # Alternating subtle row colors
        for r_idx in range(1, len(table_rows)):
            if r_idx % 2 == 0:
                table_style_list.append(('BACKGROUND', (0, r_idx), (-1, r_idx), colors.HexColor("#F8FAFC")))

        story_table.setStyle(TableStyle(table_style_list))
        elements.append(story_table)
        elements.append(Spacer(1, 4))

        # Vocabulary Focus Box (8 items in 2 columns)
        v_cells = []
        for term, mean in vocab_items:
            v_cells.append(Paragraph(f"• <b>{term}:</b> {mean}", style_vocab_item))

        while len(v_cells) < 8:
            v_cells.append(Paragraph("", style_vocab_item))

        vocab_header_p = Paragraph("💡 <b>HEDEF KELİME & DİLBİLGİSİ NOTLARI (VOCABULARY & GRAMMAR FOCUS)</b>", style_vocab_header)
        vocab_table_data = [
            [vocab_header_p, ''],
            [v_cells[0], v_cells[4]],
            [v_cells[1], v_cells[5]],
            [v_cells[2], v_cells[6]],
            [v_cells[3], v_cells[7]],
        ]
        vocab_table = Table(vocab_table_data, colWidths=[260, 260])
        vocab_table.setStyle(TableStyle([
            ('SPAN', (0,0), (1,0)),
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#FEF3C7")),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#FFFBEB")),
            ('BOX', (0,0), (-1,-1), 0.7, colors.HexColor("#FCD34D")),
            ('INNERGRID', (0,1), (-1,-1), 0.3, colors.HexColor("#FEF3C7")),
            ('TOPPADDING', (0,0), (-1,-1), 1.8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        elements.append(vocab_table)

        if page_no < len(PAGES_DATA):
            elements.append(PageBreak())

    # Build Document with NumberedCanvas
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"PDF Book successfully generated at: {output_pdf_path}")
    return output_pdf_path


if __name__ == "__main__":
    lesson_dir = os.path.join(os.path.dirname(__file__), "..", "lessons", "book_01_the_happy_prince")
    pdf_out = os.path.join(lesson_dir, "book_01_the_happy_prince.pdf")
    generate_book_pdf(pdf_out)
