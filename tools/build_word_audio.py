# -*- coding: utf-8 -*-
"""
Builds the offline word pronunciation pack (studio neural voice instead of the OS text-to-speech).

Why: browsers only expose the voices installed in the OS. On a Turkish Windows that is often just
"Microsoft Tolga (tr-TR)", so English words were read with Turkish phonetics and were unintelligible.

Pipeline:
  1. Collect every word of the bundled lessons + single-word dictionary entries.
  2. Synthesize them with edge-tts (en-US-ChristopherNeural, the narrator of the books) in chunks,
     using WordBoundary events for millisecond timestamps.
  3. Cut each word out of its chunk (dropping the long pauses between words), pack the words of the
     same first letter into one sprite, and encode it as 32 kbps mono MP3.

Output (copied to Web/public and Android assets):
  lessons/word_audio/<letter>.mp3   one sprite per first letter (lazy-loaded by the apps)
  lessons/word_audio/index.json     {"version":1, "words": {"statue": [start_ms, end_ms], ...}}

    python tools/build_word_audio.py            # resumable; synthesized chunks are cached
Requires: pip install edge-tts imageio-ffmpeg
"""
import asyncio
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import wave

import edge_tts

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "lessons", "word_audio")
CACHE_DIR = os.path.join(ROOT, "tools", ".word_audio_cache")
MIRRORS = [
    os.path.join(ROOT, "Web", "public", "lessons", "word_audio"),
    os.path.join(ROOT, "Android", "app", "src", "main", "assets", "lessons", "word_audio"),
]
VOICE = "en-US-ChristopherNeural"
CHUNK = 120
CONCURRENCY = 4
SAMPLE_RATE = 24000
LEAD_MS, TAIL_MS, GAP_MS = 40, 90, 60  # padding around each word in the sprite
WORD_RE = re.compile(r"[a-z][a-z'\-]*")


def ffmpeg() -> str:
    try:
        import imageio_ffmpeg  # type: ignore

        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return shutil.which("ffmpeg") or sys.exit("ffmpeg not found: pip install imageio-ffmpeg")


def normalize(word: str) -> str:
    return re.sub(r"^[^\w']+|[^\w']+$", "", word.lower().replace("’", "'")).strip("'")


def collect_words() -> list[str]:
    words: set[str] = set()
    for path in glob.glob(os.path.join(ROOT, "lessons", "*", "lesson.json")):
        if os.path.basename(os.path.dirname(path)).startswith("custom_"):
            continue
        with open(path, encoding="utf-8") as f:
            for seg in json.load(f)["segments"]:
                for raw in seg["text"].split():
                    w = normalize(raw)
                    if WORD_RE.fullmatch(w):
                        words.add(w)
    dict_path = os.path.join(ROOT, "lessons", "dictionary.json")
    if os.path.exists(dict_path):
        with open(dict_path, encoding="utf-8") as f:
            words |= {k for k in json.load(f)["entries"] if WORD_RE.fullmatch(k)}
    return sorted(words)


async def synthesize(words: list[str], key: str, sem: asyncio.Semaphore) -> tuple[bytes, list]:
    """Returns (mp3 bytes, boundaries) for a chunk; cached on disk so reruns resume."""
    mp3_path = os.path.join(CACHE_DIR, f"{key}.mp3")
    json_path = os.path.join(CACHE_DIR, f"{key}.json")
    if os.path.exists(mp3_path) and os.path.exists(json_path):
        with open(mp3_path, "rb") as f, open(json_path, encoding="utf-8") as j:
            return f.read(), json.load(j)
    async with sem:
        for attempt in range(4):
            try:
                text = ". ".join(w.capitalize() if w == "i" else w for w in words) + "."
                comm = edge_tts.Communicate(text, VOICE, boundary="WordBoundary")
                audio, bounds = bytearray(), []
                async for ch in comm.stream():
                    if ch["type"] == "audio":
                        audio += ch["data"]
                    elif ch["type"] == "WordBoundary":
                        bounds.append([ch["text"], ch["offset"] / 1e4, ch["duration"] / 1e4])
                break
            except Exception as exc:  # network hiccup: retry
                if attempt == 3:
                    raise
                print(f"  retry {key}: {exc}")
                await asyncio.sleep(2 + attempt * 3)
    with open(mp3_path, "wb") as f:
        f.write(audio)
    with open(json_path, "w", encoding="utf-8") as j:
        json.dump(bounds, j)
    return bytes(audio), bounds


def align(words: list[str], bounds: list) -> dict[str, tuple[float, float]]:
    """Maps each expected word to (start_ms, end_ms) in the chunk audio."""
    # A boundary may hold several words ("i. read"); split its time by character length.
    parts: list[tuple[str, float, float]] = []
    for text, offset, duration in bounds:
        tokens = re.findall(r"[a-z0-9']+(?:-[a-z0-9']+)*", text.lower().replace("’", "'"))
        total = sum(len(t) for t in tokens) or 1
        cursor = offset
        for t in tokens:
            span = duration * len(t) / total
            parts.append((t, cursor, cursor + span))
            cursor += span
    result: dict[str, tuple[float, float]] = {}
    i = 0
    for w in words:
        for j in range(i, min(i + 4, len(parts))):  # resync window
            if parts[j][0] == w:
                result[w] = (parts[j][1], parts[j][2])
                i = j + 1
                break
    return result


def decode_pcm(ff: str, mp3: bytes, tmp: str) -> bytes:
    src, dst = tmp + ".mp3", tmp + ".wav"
    with open(src, "wb") as f:
        f.write(mp3)
    subprocess.run([ff, "-y", "-loglevel", "error", "-i", src, "-ac", "1", "-ar", str(SAMPLE_RATE), "-f", "wav", dst], check=True)
    with wave.open(dst) as w:
        pcm = w.readframes(w.getnframes())
    os.remove(src)
    os.remove(dst)
    return pcm


async def main() -> None:
    os.makedirs(CACHE_DIR, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)
    ff = ffmpeg()
    words = collect_words()
    by_letter: dict[str, list[str]] = {}
    for w in words:
        by_letter.setdefault(w[0], []).append(w)
    print(f"{len(words)} words in {len(by_letter)} sprites")

    sem = asyncio.Semaphore(CONCURRENCY)
    jobs = []
    for letter, items in by_letter.items():
        for n in range(0, len(items), CHUNK):
            jobs.append((letter, items[n : n + CHUNK], f"{letter}_{n // CHUNK:03d}"))
    results = await asyncio.gather(*(synthesize(chunk, key, sem) for _, chunk, key in jobs))

    bytes_per_ms = SAMPLE_RATE * 2 / 1000
    index: dict[str, list[int]] = {}
    sprites: dict[str, bytearray] = {}
    missing = 0
    for (letter, chunk, key), (mp3, bounds) in zip(jobs, results):
        pcm = decode_pcm(ff, mp3, os.path.join(CACHE_DIR, f"tmp_{key}"))
        times = align(chunk, bounds)
        sprite = sprites.setdefault(letter, bytearray())
        for w in chunk:
            if w not in times:
                missing += 1
                continue
            start, end = times[w]
            a = max(0, int((start - LEAD_MS) * bytes_per_ms)) & ~1
            b = min(len(pcm), int((end + TAIL_MS) * bytes_per_ms)) & ~1
            begin_ms = round(len(sprite) / bytes_per_ms)
            sprite += pcm[a:b]
            index[w] = [begin_ms, round(len(sprite) / bytes_per_ms)]
            sprite += b"\x00" * (int(GAP_MS * bytes_per_ms) & ~1)

    for letter, pcm in sprites.items():
        wav_path = os.path.join(CACHE_DIR, f"sprite_{letter}.wav")
        with wave.open(wav_path, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(SAMPLE_RATE)
            w.writeframes(bytes(pcm))
        subprocess.run(
            [ff, "-y", "-loglevel", "error", "-i", wav_path, "-codec:a", "libmp3lame", "-b:a", "32k",
             os.path.join(OUT_DIR, f"{letter}.mp3")],
            check=True,
        )
        os.remove(wav_path)

    with open(os.path.join(OUT_DIR, "index.json"), "w", encoding="utf-8") as f:
        json.dump({"version": 1, "voice": VOICE, "words": dict(sorted(index.items()))}, f, separators=(",", ":"))

    for mirror in MIRRORS:
        shutil.rmtree(mirror, ignore_errors=True)
        shutil.copytree(OUT_DIR, mirror)

    size = sum(os.path.getsize(os.path.join(OUT_DIR, n)) for n in os.listdir(OUT_DIR)) / 1e6
    print(f"{len(index)} words packed, {missing} unaligned, {size:.1f} MB -> {os.path.relpath(OUT_DIR, ROOT)}")


if __name__ == "__main__":
    asyncio.run(main())
