# -*- coding: utf-8 -*-
"""
Device/emulator smoke test of the Android app driven through adb + uiautomator (F2.5 automated part).

    ./gradlew assembleDebug -Pdictalearn.slimAssets=true   # emulators with little storage
    adb install -r app/build/outputs/apk/debug/app-debug.apk
    python tools/e2e/android_e2e.py [path/to/adb]

Starts from a cleared app state. Exits non-zero if a check fails.
"""
import os
import re
import subprocess
import sys
import time

ADB = sys.argv[1] if len(sys.argv) > 1 else "adb"
PKG = "com.dictalearn.app"
ENV = {**os.environ, "MSYS_NO_PATHCONV": "1"}
results: list[tuple[str, bool, str]] = []


def adb(*args: str, check: bool = True) -> str:
    out = subprocess.run([ADB, *args], capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENV)
    if check and out.returncode != 0:
        raise RuntimeError(out.stderr.strip() or out.stdout.strip())
    return out.stdout


def dump() -> str:
    adb("shell", "uiautomator", "dump", "/sdcard/ui.xml")
    return adb("shell", "cat", "/sdcard/ui.xml")


def nodes(xml: str):
    for m in re.finditer(r"<node [^>]*>", xml):
        n = m.group(0)
        text = re.search(r' text="([^"]*)"', n)
        desc = re.search(r'content-desc="([^"]*)"', n)
        b = re.search(r'bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', n)
        if not b:
            continue
        yield (text.group(1) if text else ""), (desc.group(1) if desc else ""), tuple(int(x) for x in b.groups())


def find(label: str, timeout: float = 10.0, exact: bool = True):
    deadline = time.time() + timeout
    while time.time() < deadline:
        for text, desc, bounds in nodes(dump()):
            for value in (text, desc):
                if (value == label) if exact else (label in value):
                    return bounds
        time.sleep(0.7)
    raise AssertionError(f'"{label}" not found on screen')


def visible(label: str, exact: bool = True) -> bool:
    return any(((t == label or d == label) if exact else (label in t or label in d)) for t, d, _ in nodes(dump()))


def tap(label: str, timeout: float = 10.0, exact: bool = True) -> None:
    x1, y1, x2, y2 = find(label, timeout, exact)
    adb("shell", "input", "tap", str((x1 + x2) // 2), str((y1 + y2) // 2))
    time.sleep(0.8)


def type_text(text: str) -> None:
    adb("shell", "input", "text", text.replace(" ", "%s"))
    time.sleep(0.5)


def back() -> None:
    adb("shell", "input", "keyevent", "KEYCODE_BACK")
    time.sleep(1.0)


def back_to_library() -> None:
    """The first BACK may only close the soft keyboard (standard Android behaviour)."""
    for _ in range(3):
        back()
        if visible("Dinle. Yaz. Düzelt."):
            return
    raise AssertionError("did not return to the library")


def check(name: str, fn) -> None:
    try:
        fn()
        results.append((name, True, ""))
        print(f"  PASS  {name}")
    except Exception as exc:  # noqa: BLE001
        results.append((name, False, str(exc)[:200]))
        print(f"  FAIL  {name}: {str(exc)[:200]}")


def crashed() -> str:
    return adb("logcat", "-d", "-s", "AndroidRuntime:E", check=False)


def main() -> int:
    adb("shell", "pm", "clear", PKG)
    adb("logcat", "-c")
    adb("shell", "am", "start", "-n", f"{PKG}/.MainActivity")
    time.sleep(4)

    check("library shows books", lambda: find("The Happy Prince", 20))

    def open_book():
        tap("Mutlu Prens")
        find("Cümle 1 / 300", 20)
        find("Bilmiyorum / Göster")

    check("open book 01 -> study screen", open_book)

    def copy_protection():
        assert not visible("High above the city", exact=False), "sentence visible before answering"

    check("copy protection in dictating", copy_protection)

    def audio():
        tap("Dinle")
        find("Duraklat", 5)
        find("Dinle", 12)  # range ended

    check("audio range plays and stops", audio)

    def review():
        tap("Duyduğun cümleyi buraya yaz…")
        type_text("High above the town")
        adb("shell", "input", "keyevent", "KEYCODE_BACK")  # hide keyboard
        time.sleep(0.6)
        tap("Kontrol Et")
        find("Cümleyi düzelterek yeniden yaz")
        find("column,")  # revealed sentence words are separate clickable nodes

    check("wrong answer -> reviewing with diff", review)

    def word_card():
        tap("column,")
        find("column")
        find("mermer sütun", exact=False)
        tap("Deftere ekle")
        find("Defterde")
        back()

    check("word card: meaning + add to notebook", word_card)

    def mlkit():
        tap("statue")
        tap("Cümleyi cihazda çevir (ML Kit)")
        deadline = time.time() + 120
        while time.time() < deadline:
            xml = dump()
            if "Çevriliyor" not in xml and ("heykel" in xml.lower() or "sütun" in xml or "yapılamadı" in xml):
                break
            time.sleep(2)
        xml = dump()
        assert "yapılamadı" not in xml, "ML Kit translation failed (no network for model download?)"
        assert re.search(r"[çğışöüÇĞİŞÖÜ]", " ".join(t for t, _, _ in nodes(xml))), "no Turkish text"
        back()

    check("ML Kit on-device sentence translation", mlkit)

    def shadowing_next():
        tap("Düzeltmeyi atla")
        find("SHADOWING / SESLI TEKRAR", exact=False)
        tap("Sonraki cümle")
        find("Cümle 2 / 300")

    check("skip correction -> shadowing -> next sentence", shadowing_next)

    def pdf():
        tap("Kitabın PDF'i")
        find("16 sayfa", 20)
        find("Sayfa 1", 20)
        back()
        find("Cümle 2 / 300")

    check("PDF reader renders pages, back returns to study", pdf)

    def resume():
        back_to_library()
        find("KALDIĞIN YERDEN DEVAM ET")
        adb("shell", "am", "force-stop", PKG)
        adb("shell", "am", "start", "-n", f"{PKG}/.MainActivity")
        time.sleep(4)
        find("KALDIĞIN YERDEN DEVAM ET", 15)
        find("Cümle 2 / 300")

    check("progress + continue card survive restart", resume)

    def notebook():
        tap("Defterim")
        find("Defterim")
        find("column")
        find("bilmiyorum")
        back_to_library()

    check("notebook lists the unknown word", notebook)

    def word_mode():
        tap("Devam et")
        find("Cümle 2 / 300", 20)
        adb("shell", "input", "keyevent", "KEYCODE_BACK")
        time.sleep(0.6)
        tap("Kelime")
        find("Kelime 1 /", 10, exact=False)
        assert not visible("eyes", exact=False), "future words visible in word mode"
        adb("shell", "input", "keyevent", "KEYCODE_BACK")  # settings bar hides while the keyboard is open
        time.sleep(0.8)
        tap("Cümle")
        find("Bilmiyorum / Göster")

    check("word mode switch + masked words", word_mode)

    check("no crashes in logcat", lambda: (_ for _ in ()).throw(AssertionError(crashed()[-300:])) if "FATAL" in crashed() else None)

    failed = [r for r in results if not r[1]]
    print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
