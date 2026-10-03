# -*- coding: utf-8 -*-
"""
Tools for generating studio audio and syncing lesson data for Book 1:
'The Happy Prince' by Oscar Wilde (15 Pages x 20 Sentences = 300 Sentences).

Generates:
1. audio.wav (lossless 16-bit PCM WAV)
2. audio.mp3 (high-quality studio MP3)
3. Millisecond-exact lesson.json (300 segments)
4. book_01_the_happy_prince.pdf (16-page PDF with cover + 15 story pages)
5. book_preview.md (comprehensive dual-language markdown documentation)
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

try:
    from tools.book_01_data import PAGES_DATA, BOOK_TITLE, AUTHOR
    from tools.build_book_pdf import generate_book_pdf
except ImportError:
    from book_01_data import PAGES_DATA, BOOK_TITLE, AUTHOR
    from build_book_pdf import generate_book_pdf

VOICE = "en-US-ChristopherNeural"  # Studio-grade natural human storyteller voice
INTER_SENTENCE_PAUSE_SEC = 0.40   # 400ms pause between sentences
INTER_PAGE_PAUSE_SEC = 1.00       # 1000ms pause at end of each page (every 20 sentences)


async def synthesize_segment(sem, seg_id, text, voice):
    async with sem:
        communicate = edge_tts.Communicate(text, voice)
        audio_bytes = bytearray()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_bytes.extend(chunk["data"])
        data, sr = sf.read(io.BytesIO(audio_bytes), dtype="float32")
        # Ensure mono
        if len(data.shape) > 1:
            data = data.mean(axis=1)
        return seg_id, data, sr


async def generate_lesson_audio(lesson_path, output_dir, voice=VOICE):
    # Collect all 300 sentences from PAGES_DATA
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

    # Sort results by seg_id
    results.sort(key=lambda x: x[0])

    sample_rate = results[0][2]
    print(f"Audio sample rate: {sample_rate} Hz. Concatenating audio timeline...")

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

        updated_seg = {
            "id": seg["id"],
            "start_ms": start_ms,
            "end_ms": end_ms,
            "text": seg["text"],
            "translation": seg["translation"],
            "notes": seg["notes"],
        }
        updated_segments.append(updated_seg)

        # Longer pause at the end of each 20-sentence page
        is_page_end = ((idx + 1) % 20 == 0) and (idx + 1 < len(results))
        pause_sec = INTER_PAGE_PAUSE_SEC if is_page_end else INTER_SENTENCE_PAUSE_SEC

        pause_samples = int(sample_rate * pause_sec)
        pause_chunk = np.zeros(pause_samples, dtype=np.float32)
        all_audio_chunks.append(pause_chunk)
        current_sample += len(pause_chunk)

    # Lead-out silence (500ms)
    lead_out = np.zeros(int(sample_rate * 0.5), dtype=np.float32)
    all_audio_chunks.append(lead_out)
    current_sample += len(lead_out)

    full_audio = np.concatenate(all_audio_chunks)
    total_duration_sec = len(full_audio) / sample_rate
    print(f"Full narration assembled! Total duration: {total_duration_sec:.1f} s ({total_duration_sec/60:.2f} mins)")

    # Normalize audio to prevent clipping (-1 dB headroom)
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

    # Assemble lesson dictionary
    lesson_data = {
        "schema_version": 1,
        "lesson_id": "book_01_the_happy_prince",
        "title": "The Happy Prince (15 Sayfa / 300 Cümle / Graded Reader)",
        "source_lang": "en",
        "target_lang": "tr",
        "audio_file": "audio.mp3",
        "attribution": {
            "source": "Oscar Wilde / Public Domain / Graded Reader Adaptasyonu (15 Sayfa x 20 Cümle)",
            "license": "Public Domain"
        },
        "segments": updated_segments
    }

    # Write lesson.json
    with open(lesson_path, "w", encoding="utf-8") as f:
        json.dump(lesson_data, f, ensure_ascii=False, indent=2)
    print(f"Updated lesson.json saved with {len(updated_segments)} timed segments.")

    return wav_path, mp3_path, lesson_data


def generate_book_preview_markdown(output_md_path):
    lines = [
        "# 📖 The Happy Prince (Mutlu Prens) — 15 Sayfalık Eksiksiz Kitap",
        "",
        f"> **Yazar**: {AUTHOR}  ",
        "> **Uyarlama**: DictaLearn Seviye 1 (Kademeli Okuyucu / B1)  ",
        "> **Sayfa Sayısı**: 15 Sayfa (Her Sayfada Tam 20 Cümle • Toplam 300 Cümle)  ",
        "> **Seslendirme**: Microsoft Edge Neural TTS (`en-US-ChristopherNeural` - Stüdyo Anlatıcı)  ",
        "> **Dosyalar**: `lesson.json` • `audio.mp3` • `audio.wav` • `book_01_the_happy_prince.pdf`  ",
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
    web_dest = os.path.join(base_repo_dir, "Web", "public", "lessons", "book_01_the_happy_prince")
    android_dest = os.path.join(base_repo_dir, "Android", "app", "src", "main", "assets", "lessons", "book_01_the_happy_prince")

    for dest in [web_dest, android_dest]:
        os.makedirs(dest, exist_ok=True)
        for fname in ["lesson.json", "audio.mp3", "audio.wav", "book_01_the_happy_prince.pdf", "book_preview.md"]:
            src_f = os.path.join(src_dir, fname)
            if os.path.exists(src_f):
                shutil.copy2(src_f, os.path.join(dest, fname))
                print(f"Synced {fname} -> {dest}")


async def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    lesson_dir = os.path.join(base_dir, "lessons", "book_01_the_happy_prince")
    os.makedirs(lesson_dir, exist_ok=True)

    lesson_json_path = os.path.join(lesson_dir, "lesson.json")
    pdf_out = os.path.join(lesson_dir, "book_01_the_happy_prince.pdf")
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

    print("\nAll assets for Book 1 (The Happy Prince) successfully updated and synchronized!")


if __name__ == "__main__":
    asyncio.run(main())
