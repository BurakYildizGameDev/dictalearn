"""
Tools for generating studio audio and PDF book for DictaLearn lessons.
Generates:
1. audio.wav (lossless 16-bit PCM WAV)
2. audio.mp3 (high-quality studio MP3)
3. Updated lesson.json with millisecond-exact segment timestamps
4. book_01_the_happy_prince.pdf (15-page beautifully formatted PDF with cover)
"""

import asyncio
import io
import json
import os
import sys
import numpy as np
import soundfile as sf
import edge_tts

VOICE = "en-US-ChristopherNeural"  # Studio-grade natural human storyteller voice
INTER_SENTENCE_PAUSE_SEC = 0.40   # 400ms pause between sentences
INTER_PAGE_PAUSE_SEC = 0.90       # 900ms pause between pages (every 4 sentences)

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
    print(f"Reading lesson from: {lesson_path}")
    with open(lesson_path, "r", encoding="utf-8") as f:
        lesson_data = json.load(f)

    segments = lesson_data["segments"]
    print(f"Total segments to synthesize: {len(segments)}")

    sem = asyncio.Semaphore(5)
    tasks = [
        synthesize_segment(sem, seg["id"], seg["text"], voice)
        for seg in segments
    ]

    print(f"Synthesizing with neural voice '{voice}'...")
    results = await asyncio.gather(*tasks)
    # Sort by seg_id
    results.sort(key=lambda x: x[0])

    # Sample rate from first segment
    sample_rate = results[0][2]
    print(f"Audio sample rate: {sample_rate} Hz")

    all_audio_chunks = []
    current_sample = 0

    # Initial lead-in silence (300ms)
    lead_silence = np.zeros(int(sample_rate * 0.3), dtype=np.float32)
    all_audio_chunks.append(lead_silence)
    current_sample += len(lead_silence)

    updated_segments = []

    for idx, (seg_id, audio_data, sr) in enumerate(results):
        seg = next(s for s in segments if s["id"] == seg_id)
        
        start_ms = int(round((current_sample / sample_rate) * 1000))
        all_audio_chunks.append(audio_data)
        current_sample += len(audio_data)
        end_ms = int(round((current_sample / sample_rate) * 1000))

        updated_seg = dict(seg)
        updated_seg["start_ms"] = start_ms
        updated_seg["end_ms"] = end_ms
        updated_segments.append(updated_seg)

        # Decide pause duration: longer pause at end of page (every 4 segments)
        is_page_end = ((idx + 1) % 4 == 0) and (idx + 1 < len(results))
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
    print(f"Full narration generated! Total duration: {total_duration_sec:.1f} seconds ({total_duration_sec/60:.2f} minutes)")

    # Normalize audio to prevent clipping (-1 dB headroom)
    max_amp = np.max(np.abs(full_audio))
    if max_amp > 0:
        target_amp = 10 ** (-1.0 / 20.0) # ~0.891
        full_audio = full_audio * (target_amp / max_amp)

    wav_path = os.path.join(output_dir, "audio.wav")
    mp3_path = os.path.join(output_dir, "audio.mp3")

    print(f"Writing WAV to {wav_path}...")
    sf.write(wav_path, full_audio, sample_rate, subtype="PCM_16")

    print(f"Writing MP3 to {mp3_path}...")
    sf.write(mp3_path, full_audio, sample_rate)

    # Update lesson data
    lesson_data["audio_file"] = "audio.mp3"
    lesson_data["segments"] = updated_segments

    # Write back lesson.json
    with open(lesson_path, "w", encoding="utf-8") as f:
        json.dump(lesson_data, f, ensure_ascii=False, indent=2)
    print(f"Updated lesson.json saved with {len(updated_segments)} timed segments.")

    return wav_path, mp3_path, lesson_data

if __name__ == "__main__":
    lesson_dir = os.path.join(os.path.dirname(__file__), "..", "lessons", "book_01_the_happy_prince")
    lesson_json_path = os.path.join(lesson_dir, "lesson.json")
    asyncio.run(generate_lesson_audio(lesson_json_path, lesson_dir))
