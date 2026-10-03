# -*- coding: utf-8 -*-
"""
Builder pipeline for Book 4: 'The Devoted Friend' (Oscar Wilde).
15 Pages x 20 Sentences = 300 Sentences.

Generates:
1. audio.wav (lossless 16-bit PCM WAV)
2. audio.mp3 (studio MP3)
3. lesson.json (300 timed segments)
4. book_04_the_devoted_friend.pdf (16-page PDF with cover + 15 story pages)
5. book_preview.md (comprehensive dual-language markdown documentation)
6. Automatic sync to Web and Android apps.
"""

import asyncio
import io
import json
import os
import shutil
import sys
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

from book_04_data import PAGES_DATA, BOOK_TITLE, AUTHOR

VOICE = "en-US-ChristopherNeural"  # Studio-grade natural human storyteller voice
INTER_SENTENCE_PAUSE_SEC = 0.40   # 400ms pause between sentences
INTER_PAGE_PAUSE_SEC = 1.00       # 1000ms pause at end of each page (every 20 sentences)


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
        self.setFillColor(colors.HexColor("#B45309"))  # Warm Amber
        self.drawString(36, 810, "DICTALEARN GRADED CLASSICS")

        self.setFont("AppSans", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawRightString(559, 810, f"The Devoted Friend — Oscar Wilde  |  Sayfa {story_page_num} / {total_story_pages}")

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
        textColor=colors.HexColor("#B45309"),
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
        textColor=colors.HexColor("#0D9488"),
        alignment=TA_CENTER,
        spaceAfter=20,
    )

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
        textColor=colors.HexColor("#B45309"),
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
        textColor=colors.HexColor("#0F766E"),
    )

    style_vocab_item = ParagraphStyle(
        "VocabItem",
        fontName="AppSans",
        fontSize=6.8,
        leading=8.8,
        textColor=colors.HexColor("#1E293B"),
    )

    elements = []

    # 1. COVER PAGE
    elements.append(Spacer(1, 25))
    elements.append(Paragraph("★ DICTALEARN GRADED READERS & DICTATION SERIES ★", style_cover_badge))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("THE DEVOTED FRIEND", style_cover_title))
    elements.append(Paragraph("Sadık Dost — 15 Sayfalık Eksiksiz İngilizce Okuma & Dikte Kitabı", style_cover_subtitle))
    elements.append(Paragraph("Oscar Wilde", style_cover_author))

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
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor("#B45309")),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 16),
        ('RIGHTPADDING', (0,0), (-1,-1), 16),
    ]))
    elements.append(cover_table)

    elements.append(Spacer(1, 16))

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
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEF3C7")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#FCD34D")),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    elements.append(guide_table)

    elements.append(PageBreak())

    # 2. STORY PAGES (1 TO 15)
    for p_data in PAGES_DATA:
        page_no = p_data["page_no"]
        page_title = p_data["title"]
        tr_title = p_data["tr_title"]
        sentences = p_data["sentences"]
        vocab_items = p_data.get("vocab_focus", [])

        header_text = f"<b>Bölüm {page_no}: {page_title}</b> <font color='#64748B' size='9'>({tr_title})</font>"
        elements.append(Paragraph(header_text, style_page_header_title))
        elements.append(Spacer(1, 3))

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
        table_style_list = [
            ('BACKGROUND', (0,0), (0,0), colors.HexColor("#F0F9FF")),
            ('BACKGROUND', (1,0), (1,0), colors.HexColor("#FEF3C7")),
            ('BOX', (0,0), (-1,-1), 0.7, colors.HexColor("#CBD5E1")),
            ('INNERGRID', (0,0), (-1,-1), 0.3, colors.HexColor("#E2E8F0")),
            ('TOPPADDING', (0,0), (-1,-1), 1.6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1.6),
            ('LEFTPADDING', (0,0), (-1,-1), 4.5),
            ('RIGHTPADDING', (0,0), (-1,-1), 4.5),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]
        for r_idx in range(1, len(table_rows)):
            if r_idx % 2 == 0:
                table_style_list.append(('BACKGROUND', (0, r_idx), (-1, r_idx), colors.HexColor("#F8FAFC")))

        story_table.setStyle(TableStyle(table_style_list))
        elements.append(story_table)
        elements.append(Spacer(1, 4))

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
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#CCFBF1")),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#F0FDFA")),
            ('BOX', (0,0), (-1,-1), 0.7, colors.HexColor("#5EEAD4")),
            ('INNERGRID', (0,1), (-1,-1), 0.3, colors.HexColor("#CCFBF1")),
            ('TOPPADDING', (0,0), (-1,-1), 1.8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        elements.append(vocab_table)

        if page_no < len(PAGES_DATA):
            elements.append(PageBreak())

    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"PDF Book successfully generated at: {output_pdf_path}")
    return output_pdf_path


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


async def generate_lesson_audio(lesson_path, output_dir, voice=VOICE):
    all_sentences = []
    for page in PAGES_DATA:
        for s in page["sentences"]:
            all_sentences.append({
                "id": s["id"],
                "text": s["text"],
                "translation": s["translation"],
                "notes": s["notes"],
            })

    total_count = len(all_sentences)
    print(f"Total sentences to synthesize: {total_count} (Voice: {voice})")

    sem = asyncio.Semaphore(8)
    tasks = [
        synthesize_segment(sem, s["id"], s["text"], voice)
        for s in all_sentences
    ]

    print("Synthesizing neural audio chunks across worker pool...")
    results = []
    for i, coro in enumerate(asyncio.as_completed(tasks)):
        res = await coro
        results.append(res)
        if (i + 1) % 25 == 0 or (i + 1) == total_count:
            print(f"  -> Synthesized {i + 1}/{total_count} segments...")

    results.sort(key=lambda x: x[0])
    sample_rate = results[0][2]
    print(f"Audio sample rate: {sample_rate} Hz. Assembling audio timeline...")

    all_audio_chunks = []
    current_sample = 0

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

        updated_seg = {
            "id": seg["id"],
            "start_ms": start_ms,
            "end_ms": end_ms,
            "text": seg["text"],
            "translation": seg["translation"],
            "notes": seg["notes"],
        }
        updated_segments.append(updated_seg)

        is_page_end = ((idx + 1) % 20 == 0) and (idx + 1 < len(results))
        pause_sec = INTER_PAGE_PAUSE_SEC if is_page_end else INTER_SENTENCE_PAUSE_SEC

        pause_samples = int(sample_rate * pause_sec)
        pause_chunk = np.zeros(pause_samples, dtype=np.float32)
        all_audio_chunks.append(pause_chunk)
        current_sample += len(pause_chunk)

    lead_out = np.zeros(int(sample_rate * 0.5), dtype=np.float32)
    all_audio_chunks.append(lead_out)
    current_sample += len(lead_out)

    full_audio = np.concatenate(all_audio_chunks)
    total_duration_sec = len(full_audio) / sample_rate
    print(f"Full narration generated! Total duration: {total_duration_sec:.1f} s ({total_duration_sec/60:.2f} mins)")

    max_amp = np.max(np.abs(full_audio))
    if max_amp > 0:
        target_amp = 10 ** (-1.0 / 20.0)  # ~0.891
        full_audio = full_audio * (target_amp / max_amp)

    wav_path = os.path.join(output_dir, "audio.wav")
    mp3_path = os.path.join(output_dir, "audio.mp3")

    print(f"Writing 16-bit PCM WAV to: {wav_path}")
    sf.write(wav_path, full_audio, sample_rate, subtype="PCM_16")

    print(f"Writing studio MP3 to: {mp3_path}")
    sf.write(mp3_path, full_audio, sample_rate)

    lesson_data = {
        "schema_version": 1,
        "lesson_id": "book_04_the_devoted_friend",
        "title": "The Devoted Friend (15 Sayfa / 300 Cümle / Graded Reader)",
        "source_lang": "en",
        "target_lang": "tr",
        "audio_file": "audio.mp3",
        "attribution": {
            "source": "Oscar Wilde / Public Domain / Graded Reader Adaptasyonu (15 Sayfa x 20 Cümle)",
            "license": "Public Domain"
        },
        "segments": updated_segments
    }

    with open(lesson_path, "w", encoding="utf-8") as f:
        json.dump(lesson_data, f, ensure_ascii=False, indent=2)
    print(f"Updated lesson.json saved with {len(updated_segments)} timed segments.")

    return wav_path, mp3_path, lesson_data


def generate_book_preview_markdown(output_md_path):
    lines = [
        "# 📖 The Devoted Friend (Sadık Dost) — 15 Sayfalık Eksiksiz Kitap",
        "",
        f"> **Yazar**: {AUTHOR}  ",
        "> **Uyarlama**: DictaLearn Seviye 1 (Kademeli Okuyucu / B1)  ",
        "> **Sayfa Sayısı**: 15 Sayfa (Her Sayfada Tam 20 Cümle • Toplam 300 Cümle)  ",
        "> **Seslendirme**: Microsoft Edge Neural TTS (`en-US-ChristopherNeural` - Stüdyo Anlatıcı)  ",
        "> **Dosyalar**: `lesson.json` • `audio.mp3` • `audio.wav` • `book_04_the_devoted_friend.pdf`  ",
        "",
        "---",
        ""
    ]

    for p in PAGES_DATA:
        page_no = p["page_no"]
        title = p["title"]
        tr_title = p["tr_title"]
        vocab = p.get("vocab_focus", [])

        lines.append(f"## 📄 Sayfa {page_no}: {title} ({tr_title})")
        lines.append("")
        lines.append("| No | İngilizce Cümle | Türkçe Çeviri | Dilbilgisi & Kelime Notu |")
        lines.append("|---|---|---|---|")

        for s in p["sentences"]:
            sid = s["id"]
            en = s["text"].replace("|", "\\|")
            tr = s["translation"].replace("|", "\\|")
            raw_note = s.get("notes", "")
            if "|" in raw_note:
                raw_note = raw_note.split("|", 1)[1].strip()
            note = raw_note.replace("|", "\\|")
            lines.append(f"| **{sid}** | {en} | {tr} | `{note}` |")

        lines.append("")
        if vocab:
            lines.append("**💡 Hedef Kelimeler:**")
            vocab_strs = [f"`{term}`: {meaning}" for term, meaning in vocab]
            lines.append(" • ".join(vocab_strs))
            lines.append("")
        lines.append("---")
        lines.append("")

    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated preview markdown at: {output_md_path}")


def sync_assets(src_dir, base_repo_dir):
    web_dest = os.path.join(base_repo_dir, "Web", "public", "lessons", "book_04_the_devoted_friend")
    android_dest = os.path.join(base_repo_dir, "Android", "app", "src", "main", "assets", "lessons", "book_04_the_devoted_friend")

    for dest in [web_dest, android_dest]:
        os.makedirs(dest, exist_ok=True)
        for fname in ["lesson.json", "audio.mp3", "audio.wav", "book_04_the_devoted_friend.pdf", "book_preview.md"]:
            src_f = os.path.join(src_dir, fname)
            if os.path.exists(src_f):
                shutil.copy2(src_f, os.path.join(dest, fname))
                print(f"Synced {fname} -> {dest}")


async def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    lesson_dir = os.path.join(base_dir, "lessons", "book_04_the_devoted_friend")
    os.makedirs(lesson_dir, exist_ok=True)

    lesson_json_path = os.path.join(lesson_dir, "lesson.json")
    pdf_out = os.path.join(lesson_dir, "book_04_the_devoted_friend.pdf")
    md_out = os.path.join(lesson_dir, "book_preview.md")

    print("=================================================================")
    print("STEP 1: Generating 300-segment studio audio (Edge Neural TTS)...")
    print("=================================================================")
    await generate_lesson_audio(lesson_json_path, lesson_dir)

    print("\n=================================================================")
    print("STEP 2: Generating 16-page professional PDF book (ReportLab)...")
    print("=================================================================")
    generate_book_pdf(pdf_out)

    print("\n=================================================================")
    print("STEP 3: Generating comprehensive Markdown preview...")
    print("=================================================================")
    generate_book_preview_markdown(md_out)

    print("\n=================================================================")
    print("STEP 4: Syncing all assets to Web and Android apps...")
    print("=================================================================")
    sync_assets(lesson_dir, base_dir)

    print("\nAll assets for Book 4 (The Devoted Friend) successfully created and synchronized!")


if __name__ == "__main__":
    asyncio.run(main())
