# -*- coding: utf-8 -*-
"""
Detects lesson `audio.mp3` files that are actually RIFF/WAV data (renamed WAVs)
and re-encodes them into real CBR MP3 files.

Why: a WAV disguised as MP3 is ~7x larger (150+ MB per book), which makes the
web app download huge files and bloats the Android APK. CBR is used so that
seeking (HTMLAudioElement / MediaPlayer) maps milliseconds to bytes precisely.

Usage:
    python tools/fix_mp3_encoding.py            # fix lessons/ and sync copies
    python tools/fix_mp3_encoding.py --dry-run  # only report

Requires: pip install imageio-ffmpeg  (bundles an ffmpeg binary)
"""
import argparse
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(ROOT, "lessons")
MIRROR_DIRS = [
    os.path.join(ROOT, "Web", "public", "lessons"),
    os.path.join(ROOT, "Android", "app", "src", "main", "assets", "lessons"),
]
BITRATE = "48k"  # matches books 01-25 (speech, 24 kHz mono)


def is_riff(path: str) -> bool:
    with open(path, "rb") as f:
        return f.read(4) == b"RIFF"


def ffmpeg_exe() -> str:
    try:
        import imageio_ffmpeg  # type: ignore

        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        found = shutil.which("ffmpeg")
        if not found:
            sys.exit("ffmpeg not found. Run: pip install imageio-ffmpeg")
        return found


def encode(ffmpeg: str, wav_path: str, mp3_path: str) -> None:
    tmp_path = mp3_path + ".tmp.mp3"
    subprocess.run(
        [
            ffmpeg, "-y", "-loglevel", "error",
            "-i", wav_path,
            "-ac", "1", "-ar", "24000",
            "-codec:a", "libmp3lame", "-b:a", BITRATE,
            tmp_path,
        ],
        check=True,
    )
    os.replace(tmp_path, mp3_path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    ffmpeg = ffmpeg_exe()
    fixed = []
    for lesson_id in sorted(os.listdir(SOURCE_DIR)):
        mp3_path = os.path.join(SOURCE_DIR, lesson_id, "audio.mp3")
        if not os.path.isfile(mp3_path) or not is_riff(mp3_path):
            continue
        size_mb = os.path.getsize(mp3_path) / 1e6
        print(f"[RIFF] {lesson_id}/audio.mp3 ({size_mb:.1f} MB)")
        if args.dry_run:
            continue

        wav_path = os.path.join(SOURCE_DIR, lesson_id, "audio.wav")
        source = wav_path if os.path.isfile(wav_path) else mp3_path
        encode(ffmpeg, source, mp3_path)
        print(f"   -> {os.path.getsize(mp3_path) / 1e6:.1f} MB")
        fixed.append(lesson_id)

    for lesson_id in fixed:
        src = os.path.join(SOURCE_DIR, lesson_id, "audio.mp3")
        for mirror in MIRROR_DIRS:
            dest_dir = os.path.join(mirror, lesson_id)
            if os.path.isdir(dest_dir):
                shutil.copy2(src, os.path.join(dest_dir, "audio.mp3"))
                print(f"   synced -> {os.path.relpath(dest_dir, ROOT)}")

    print(f"Done. Fixed {len(fixed)} file(s).")


if __name__ == "__main__":
    main()
