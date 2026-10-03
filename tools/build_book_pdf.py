"""
Builds a professional 15-page PDF book for 'The Happy Prince' (Oscar Wilde).
Uses ReportLab with Windows TrueType fonts (Arial/Georgia) for complete Turkish character support.
Outputs:
  lessons/book_01_the_happy_prince/book_01_the_happy_prince.pdf
"""

import json
import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    KeepTogether,
    HRFlowable,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfgen import canvas

def setup_fonts():
    # Register Arial / Georgia from Windows Fonts
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
        self.drawString(40, 810, "DICTALEARN GRADED CLASSICS")

        self.setFont("AppSans", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawRightString(555, 810, f"The Happy Prince — Oscar Wilde  |  Sayfa {story_page_num} / {total_story_pages}")

        # Top Header Divider Line
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.8)
        self.line(40, 802, 555, 802)

        # Running Bottom Footer
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.8)
        self.line(40, 42, 555, 42)

        self.setFont("AppSans-Italic", 7.5)
        self.setFillColor(colors.HexColor("#94A3B8"))
        self.drawString(40, 30, "DictaLearn Open Library • Interaktif Dikte, Okuma ve Shadowing • www.dictalearn.org")

        self.setFont("AppSans-Bold", 8)
        self.setFillColor(colors.HexColor("#334155"))
        self.drawRightString(555, 30, f"{story_page_num}")

        self.restoreState()


def generate_book_pdf(lesson_json_path, output_pdf_path):
    setup_fonts()

    with open(lesson_json_path, "r", encoding="utf-8") as f:
        lesson_data = json.load(f)

    segments = lesson_data.get("segments", [])
    total_segments = len(segments)
    segments_per_page = 4
    total_story_pages = (total_segments + segments_per_page - 1) // segments_per_page

    # Setup Document
    # A4: 595.27 x 841.89 points. Margins: 38 pt left/right, 48 pt top/bottom
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=A4,
        leftMargin=38,
        rightMargin=38,
        topMargin=46,
        bottomMargin=46,
    )

    styles = getSampleStyleSheet()

    # Custom typography styles
    style_cover_badge = ParagraphStyle(
        "CoverBadge",
        fontName="AppSans-Bold",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#0284C7"),
        alignment=TA_CENTER,
        spaceAfter=10,
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
        spaceAfter=14,
    )

    style_cover_author = ParagraphStyle(
        "CoverAuthor",
        fontName="AppSerif-Bold",
        fontSize=15,
        leading=20,
        textColor=colors.HexColor("#D97706"),  # Amber
        alignment=TA_CENTER,
        spaceAfter=24,
    )

    style_page_header_title = ParagraphStyle(
        "PageHeaderTitle",
        fontName="AppSerif-Bold",
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=4,
    )

    style_section_label = ParagraphStyle(
        "SectionLabel",
        fontName="AppSans-Bold",
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#0369A1"),
        spaceAfter=4,
    )

    style_story_text = ParagraphStyle(
        "StoryText",
        fontName="AppSerif",
        fontSize=10.5,
        leading=15.5,
        textColor=colors.HexColor("#1E293B"),
        alignment=TA_JUSTIFY,
        spaceAfter=6,
    )

    style_trans_text = ParagraphStyle(
        "TransText",
        fontName="AppSans",
        fontSize=9.2,
        leading=13.5,
        textColor=colors.HexColor("#334155"),
        alignment=TA_JUSTIFY,
        spaceAfter=5,
    )

    style_note_item = ParagraphStyle(
        "NoteItem",
        fontName="AppSans",
        fontSize=8.3,
        leading=12,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=3,
    )

    elements = []

    # ==========================================
    # 1. COVER PAGE
    # ==========================================
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("★ DICTALEARN GRADED READERS & DICTATION SERIES ★", style_cover_badge))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("THE HAPPY PRINCE", style_cover_title))
    elements.append(Paragraph("Mutlu Prens — 15 Sayfalık Eksiksiz İngilizce Okuma & Dikte Kitabı", style_cover_subtitle))
    elements.append(Paragraph("Oscar Wilde", style_cover_author))

    # Cover Summary Box
    cover_info_html = """
    <b>Kitap Seviyesi:</b> CEFR B1 (Intermediate / Orta Seviye)<br/>
    <b>Sayfa Sayısı:</b> 15 Sayfa (60 Temel Paragraf & Cümle)<br/>
    <b>Ses Formatları:</b> Stüdyo MP3 + Kayıpsız WAV (Christopher Neural Narrator)<br/>
    <b>Metot:</b> Çift Dilli Paralel Metin, Milisaniye Senkron Dikte & Gölgeleme (Shadowing)<br/>
    <b>Kapsam:</b> 180+ Hedef Kelime, Deyimler, Gramer Çözümlemeleri ve Türkçe Çeviriler
    """
    cover_info_p = Paragraph(cover_info_html, ParagraphStyle("CoverInfo", fontName="AppSans", fontSize=9.5, leading=15, textColor=colors.HexColor("#1E293B")))
    cover_table = Table([[cover_info_p]], colWidths=[515])
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
    col1 = Paragraph("<b>🎙️ Doğal Stüdyo Sesi</b><br/>Robotik ve mekanik olmayan, insansı tonlama ve nefes hissiyatına sahip stüdyo seslendirmesi (WAV & MP3).", ParagraphStyle("Col1", fontName="AppSans", fontSize=8.5, leading=12, textColor=colors.HexColor("#334155")))
    col2 = Paragraph("<b>✍️ Dikte & Shadowing</b><br/>DictaLearn Web ve Android uygulamalarında klavye ile yazarak veya sesli tekrar ederek çalışabilirsiniz.", ParagraphStyle("Col2", fontName="AppSans", fontSize=8.5, leading=12, textColor=colors.HexColor("#334155")))
    col3 = Paragraph("<b>📖 Cümle Cümle Analiz</b><br/>Her sayfa 4 cümle içerir. İngilizce metin, Türkçe çeviri ve gramer açıklamaları aynı sayfada sunulur.", ParagraphStyle("Col3", fontName="AppSans", fontSize=8.5, leading=12, textColor=colors.HexColor("#334155")))

    feat_table = Table([[col1, col2, col3]], colWidths=[165, 165, 165])
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
    <b>1. Adım (Dinleme & Okuma):</b> Her sayfadaki İngilizce metni ses dosyası eşliğinde (MP3/WAV) dikkatle dinleyin.<br/>
    <b>2. Adım (Klavye Dikte):</b> DictaLearn uygulamasında cümleyi dinleyip eksiksiz yazın; anlık harf ve kelime farklarını görün.<br/>
    <b>3. Adım (Shadowing & Telaffuz):</b> Spikerin hemen ardından cümleyi yüksek sesle taklit ederek telaffuzunuzu pekiştirin.<br/>
    <b>4. Adım (Kelime & Çeviri Pekiştirme):</b> Sayfanın altındaki kelime tahlilleri ve Türkçe karşılıkları ile anlamı kalıcılaştırın.
    """
    guide_p = Paragraph(guide_html, ParagraphStyle("Guide", fontName="AppSans", fontSize=8.5, leading=13.5, textColor=colors.HexColor("#1E293B")))
    guide_table = Table([[guide_p]], colWidths=[515])
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
    # ==========================================
    page_titles = [
        "The Golden Statue Above the City",
        "The Lonely Swallow Seeks Shelter",
        "A Statue in Tears",
        "The Story of the Palace of Sans-Souci",
        "The Weeping Seamstress and the Sick Child",
        "The Flight Through the Cathedral and City",
        "The Ruby on the Seamstress's Bed",
        "A Strange Feeling of Warmth",
        "The Starving Playwright in the Garret",
        "The Sapphire of the Prince's Eye",
        "The Poor Match-Girl in the Square Below",
        "The Second Sapphire and Pure Blindness",
        "The Swallow Decides to Stay Forever",
        "Winter Frost, Sacrifice and the Frozen Swallow",
        "The Broken Lead Heart and God's Garden",
    ]

    for page_idx in range(total_story_pages):
        start_i = page_idx * segments_per_page
        end_i = min(start_i + segments_per_page, total_segments)
        page_segs = segments[start_i:end_i]

        page_no = page_idx + 1
        page_title = page_titles[page_idx] if page_idx < len(page_titles) else f"Bölüm {page_no}"

        # Page Header Banner
        header_p = Paragraph(f"<b>Bölüm {page_no}: {page_title}</b>", style_page_header_title)
        elements.append(header_p)
        elements.append(Spacer(1, 4))

        # CARD 1: English Text
        elements.append(Paragraph("📖 <b>ENGLISH STORY TEXT (ORİJİNAL İNGİLİZCE METİN)</b>", style_section_label))
        
        story_flowables = []
        for s in page_segs:
            text = f"<b>[{s['id']}]</b> {s['text']}"
            story_flowables.append(Paragraph(text, style_story_text))
        
        story_table = Table([[story_flowables]], colWidths=[515])
        story_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFFFFF")),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
            ('TOPPADDING', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 12),
            ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ]))
        elements.append(story_table)
        elements.append(Spacer(1, 7))

        # CARD 2: Turkish Translation
        elements.append(Paragraph("🇹🇷 <b>TÜRKÇE KARŞILIĞI (PARALEL ÇEVİRİ)</b>", ParagraphStyle("TransLbl", fontName="AppSans-Bold", fontSize=8.5, leading=11, textColor=colors.HexColor("#0D9488"), spaceAfter=3)))
        
        trans_flowables = []
        for s in page_segs:
            t = f"<b>[{s['id']}]</b> {s['translation']}"
            trans_flowables.append(Paragraph(t, style_trans_text))
        
        trans_table = Table([[trans_flowables]], colWidths=[515])
        trans_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0FDFA")),  # Mint / Teal soft background
            ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#5EEAD4")),
            ('TOPPADDING', (0,0), (-1,-1), 7),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 12),
            ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ]))
        elements.append(trans_table)
        elements.append(Spacer(1, 7))

        # CARD 3: Vocabulary and Grammar Focus
        elements.append(Paragraph("💡 <b>KELİME & DİLBİLGİSİ ANALİZİ (VOCABULARY & GRAMMAR FOCUS)</b>", ParagraphStyle("NoteLbl", fontName="AppSans-Bold", fontSize=8.5, leading=11, textColor=colors.HexColor("#B45309"), spaceAfter=3)))
        
        note_flowables = []
        for s in page_segs:
            # Clean up note text (remove 'Sayfa X | ' prefix if present)
            raw_note = s.get("notes", "")
            if "|" in raw_note:
                raw_note = raw_note.split("|", 1)[1].strip()
            note_text = f"• <b>[{s['id']}]</b> {raw_note}"
            note_flowables.append(Paragraph(note_text, style_note_item))

        note_table = Table([[note_flowables]], colWidths=[515])
        note_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFFBEB")),  # Soft amber background
            ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#FCD34D")),
            ('TOPPADDING', (0,0), (-1,-1), 7),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 12),
            ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ]))
        elements.append(note_table)

        if page_no < total_story_pages:
            elements.append(PageBreak())

    # Build Document with NumberedCanvas
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"PDF Book successfully generated at: {output_pdf_path}")
    return output_pdf_path

if __name__ == "__main__":
    lesson_dir = os.path.join(os.path.dirname(__file__), "..", "lessons", "book_01_the_happy_prince")
    lesson_json = os.path.join(lesson_dir, "lesson.json")
    pdf_out = os.path.join(lesson_dir, "book_01_the_happy_prince.pdf")
    generate_book_pdf(lesson_json, pdf_out)
