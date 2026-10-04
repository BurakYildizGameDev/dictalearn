# -*- coding: utf-8 -*-
"""
End-to-end test of the web app in a real Chromium (F1.7 automated part).

    cd Web && npm run dev -- --port 5199          # or a preview server of the prod build
    python tools/e2e/web_e2e.py http://localhost:5199/ [screenshot_dir]

Requires: pip install playwright && python -m playwright install chromium
Exits non-zero on the first failed check.
"""
import os
import re
import sys
import time

from playwright.sync_api import Page, expect, sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:5199/"
SHOTS = sys.argv[2] if len(sys.argv) > 2 else None
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEMO = [
    "He packed his small brown suitcase and opened the door.",
    "The morning cold hit him immediately.",
    "He walked down the quiet street toward the station.",
    "The early train was already waiting at the platform.",
    "He found an empty seat next to the window.",
    "The journey was finally about to begin.",
]

results: list[tuple[str, bool, str]] = []


def check(name: str, fn) -> None:
    try:
        fn()
        results.append((name, True, ""))
        print(f"  PASS  {name}")
    except Exception as exc:  # noqa: BLE001 - report every failure kind
        results.append((name, False, str(exc).splitlines()[0][:200]))
        print(f"  FAIL  {name}: {str(exc).splitlines()[0][:200]}")


def shot(page: Page, name: str) -> None:
    if SHOTS:
        page.wait_for_timeout(400)  # let entry animations finish
        page.screenshot(path=os.path.join(SHOTS, f"{name}.png"))


def html_without_inputs(page: Page) -> str:
    return page.evaluate("document.body.innerHTML")


def run() -> int:
    errors: list[str] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chromium")
        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        page = ctx.new_page()
        page.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
        page.on("console", lambda m: m.type == "error" and errors.append(f"console: {m.text}"))

        # ── Library ──────────────────────────────────────────────────────
        page.goto(BASE + "#/")
        page.wait_for_selector("text=Seviye 1")

        def library():
            expect(page.get_by_role("button", name="The Happy Prince — Oscar Wilde")).to_be_visible()
            page.get_by_placeholder("Kitap, yazar ara…").fill("hayalet")
            expect(page.get_by_role("button", name="The Canterville Ghost — Oscar Wilde")).to_be_visible()
            expect(page.get_by_role("button", name="The Happy Prince — Oscar Wilde")).to_have_count(0)
            page.get_by_placeholder("Kitap, yazar ara…").fill("")
            page.get_by_role("group", name="Seviye filtresi").get_by_role("button", name="B1").click()
            expect(page.get_by_role("heading", name="Seviye 1 · A2 · 15 sayfa")).to_have_count(0)
            expect(page.get_by_role("heading", name="Seviye 2 · B1 · 25 sayfa")).to_be_visible()
            page.get_by_role("group", name="Seviye filtresi").get_by_role("button", name="Tümü").click()

        check("library: search + level filter", library)
        shot(page, "web-library")

        # ── Full keyboard loop through the demo lesson ───────────────────
        page.goto(BASE + "#/study/sample_ch01")
        page.wait_for_selector("#dictation-input")

        def copy_protection():
            body = html_without_inputs(page)
            assert DEMO[0] not in body and "suitcase" not in body, "sentence leaked into the DOM"
            assert "Küçük kahverengi" not in body, "translation leaked into the DOM"
            ta = page.locator("#dictation-input")
            assert ta.get_attribute("spellcheck") == "false"
            assert ta.get_attribute("autocomplete") == "off"
            assert ta.get_attribute("autocorrect") == "off"

        check("copy protection + keyboard hygiene in dictating", copy_protection)

        def audio_range():
            page.get_by_role("button", name="Dinle", exact=True).click()
            expect(page.get_by_role("button", name="Duraklat").first).to_be_visible(timeout=3000)
            # sentence 1 is ~4 s; the button must return to "Dinle" when the range ends
            expect(page.get_by_role("button", name="Dinle", exact=True)).to_be_visible(timeout=8000)
            t = page.evaluate("Array.from(document.querySelectorAll('audio')).length")
            assert t == 0, "audio element should not be attached to the DOM"

        check("audio: segment plays and stops at end_ms", audio_range)

        def loop():
            # 1: wrong answer -> reviewing -> correct the sentence -> shadowing -> Enter
            page.locator("#dictation-input").fill("He packed his suitcase and open the door")
            page.keyboard.press("Enter")
            expect(page.get_by_label("Karşılaştırma sonucu")).to_contain_text("Hatalar var")
            expect(page.get_by_label("Orijinal cümle")).to_have_text(DEMO[0])
            shot(page, "web-review")
            page.wait_for_function("document.activeElement && document.activeElement.id === 'correction-input'")
            page.keyboard.type(DEMO[0])
            page.keyboard.press("Enter")
            expect(page.get_by_text("Shadowing / Sesli Tekrar")).to_be_visible()
            page.keyboard.press("Control+t")
            expect(page.get_by_text("Sabahın soğuğu").or_(page.get_by_text("Küçük kahverengi"))).to_be_visible()
            page.wait_for_timeout(120)
            page.keyboard.press("Enter")
            # 2: perfect answer goes straight to shadowing
            page.wait_for_function("document.activeElement && document.activeElement.id === 'dictation-input'")
            page.keyboard.type(DEMO[1].lower().rstrip("."))
            page.keyboard.press("Enter")
            expect(page.get_by_text("Kusursuz")).to_be_visible()
            page.wait_for_timeout(120)
            page.keyboard.press("Enter")
            # 3: give up with Ctrl+Enter, skip correction with Ctrl+Enter
            page.wait_for_function("document.activeElement && document.activeElement.id === 'dictation-input'")
            page.keyboard.press("Control+Enter")
            expect(page.get_by_text("Doğruluk: 0%")).to_be_visible()
            page.keyboard.press("Control+Enter")
            expect(page.get_by_text("Shadowing / Sesli Tekrar")).to_be_visible()
            page.wait_for_timeout(120)
            page.keyboard.press("Enter")
            expect(page.get_by_label("Cümleye git")).to_have_value("4")

        check("keyboard loop: review/correct, perfect, give up + skip", loop)
        shot(page, "web-study")

        def navigation():
            page.locator("body").click(position={"x": 5, "y": 400})
            page.keyboard.press("PageDown")
            expect(page.get_by_label("Cümleye git")).to_have_value("5")
            page.keyboard.press("PageUp")
            expect(page.get_by_label("Cümleye git")).to_have_value("4")
            page.get_by_label("Cümleye git").fill("6")
            page.get_by_label("Cümleye git").press("Enter")
            expect(page.get_by_label("Cümleye git")).to_have_value("6")
            page.keyboard.press("F1")
            expect(page.get_by_role("dialog", name="Klavye kısayolları")).to_be_visible()
            page.keyboard.press("Escape")
            expect(page.get_by_role("dialog", name="Klavye kısayolları")).to_have_count(0)

        check("PageUp/PageDown, jump to sentence, F1/Esc", navigation)

        def resume():
            page.reload()
            page.wait_for_selector("#dictation-input")
            expect(page.get_by_label("Cümleye git")).to_have_value("6")
            expect(page.get_by_text("Kaldığın yerden devam ediyorsun.")).to_be_visible()

        check("progress survives reload (resume)", resume)

        def word_mode():
            page.locator("#dictation-input").focus()
            page.keyboard.press("Control+m")
            page.wait_for_function("document.activeElement && document.activeElement.id === 'word-input'")
            body = html_without_inputs(page)
            assert "journey" not in body, "future words leaked in word mode"
            page.keyboard.type("teh ")  # wrong
            expect(page.get_by_text("Yanlış kelime")).to_be_visible()
            page.locator("#word-input").fill("")
            for w in ["The", "journey", "was", "finally", "about", "to", "begin"]:
                page.locator("#word-input").fill(w)
                page.keyboard.press(" ")
            expect(page.get_by_text("Shadowing / Sesli Tekrar")).to_be_visible()
            page.keyboard.press("Control+m")  # back to sentence mode for later checks
            page.wait_for_timeout(100)
            assert page.evaluate("localStorage.getItem('dictalearn_study_mode')") == "sentence"

        check("word mode: Ctrl+M, Space submits, masked future words", word_mode)

        def word_card():
            sentence = page.get_by_label("Orijinal cümle")
            sentence.get_by_role("button", name="journey", exact=True).click()
            card = page.get_by_role("dialog", name="Kelime kartı: journey")
            expect(card).to_contain_text("yolculuk")
            card.get_by_role("button", name="Bilmiyorum, deftere ekle").click()
            expect(card.get_by_role("button", name="Defterde")).to_be_disabled()
            page.keyboard.press("Escape")
            expect(card).to_have_count(0)
            sentence.get_by_role("button", name="finally", exact=True).click()
            expect(page.get_by_role("dialog", name="Kelime kartı: final").or_(
                page.get_by_role("dialog", name="Kelime kartı: finally"))).to_be_visible()

        check("word card: meaning, add to notebook, Esc", word_card)
        shot(page, "web-word-card")

        def completion():
            page.get_by_role("button", name="Dersi Bitir").click()
            expect(page.get_by_text("Ders tamamlandı")).to_be_visible()
            page.get_by_role("button", name="Dersi Tekrar Başlat").click()
            expect(page.get_by_label("Cümleye git")).to_have_value("1")

        check("completion screen + restart", completion)

        def notebook():
            page.goto(BASE + "#/notebook")
            expect(page.get_by_role("heading", name="Tekrar edilecek kelimeler")).to_be_visible()
            expect(page.get_by_text("journey", exact=True)).to_be_visible()
            expect(page.get_by_text("bilmiyorum", exact=True).first).to_be_visible()

        check("notebook lists missed + unknown words", notebook)

        def spaced_review():
            expect(page.get_by_text("tekrar zamanı gelen", exact=False)).to_be_visible()
            page.get_by_role("button", name="Tekrara başla").click()
            expect(page).to_have_url(re.compile(r"#/review$"))
            box = page.get_by_label("Duyduğun İngilizce kelimeyi yaz")
            for _ in range(60):  # answer everything with "Bilmiyorum" until the summary
                if page.get_by_text("Tekrar tamamlandı").count():
                    break
                if page.get_by_role("button", name="Bilmiyorum").count():
                    page.get_by_role("button", name="Bilmiyorum").click()
                else:
                    box.fill("x")
                    box.press("Enter")
                page.get_by_role("button", name="Devam").click()
            expect(page.get_by_text("Tekrar tamamlandı")).to_be_visible()
            page.get_by_role("button", name="Defterime dön").click()
            expect(page.get_by_role("heading", name="Tekrar edilecek kelimeler")).to_be_visible()

        check("spaced repetition review from the notebook", spaced_review)

        def speed():
            page.evaluate("localStorage.setItem('dictalearn_study_mode', 'sentence')")
            page.goto(BASE + "#/study/sample_ch01")
            page.wait_for_selector("#dictation-input")
            page.locator("body").click(position={"x": 5, "y": 400})
            page.keyboard.press("Control+1")
            expect(page.get_by_title("Hız: 0.75x (Ctrl+1)")).to_have_attribute("aria-pressed", "true")
            assert page.evaluate("localStorage.getItem('dictalearn_audio_speed')") == "0.75"
            page.keyboard.press("Control+2")

        check("speed shortcuts persist", speed)

        def long_book_audio():
            page.goto(BASE + "#/study/book_32_dracula")
            page.wait_for_selector("#dictation-input", timeout=60000)
            page.get_by_role("button", name="Dinle", exact=True).click()
            expect(page.get_by_role("button", name="Duraklat").first).to_be_visible(timeout=5000)
            page.get_by_role("button", name="Duraklat").first.click()
            expect(page.get_by_role("button", name="Dinle", exact=True)).to_be_visible()

        check("book 32 (re-encoded MP3) loads and plays", long_book_audio)

        def pdf_split():
            page.get_by_role("button", name="PDF").click()
            expect(page.get_by_label("PDF Görüntüleyici")).to_be_visible()
            src = page.locator("aside iframe").get_attribute("src")
            assert src and src.endswith("book_32_dracula.pdf"), src
            absolute = page.evaluate("(s) => new URL(s, location.href).href", src)
            r = page.request.get(absolute)
            assert r.ok and r.body()[:4] == b"%PDF", f"pdf not served: {r.status}"

        check("book PDF opens in split view and is served", pdf_split)

        def pdf_upload():
            page.goto(BASE + "#/")
            page.wait_for_selector("text=Seviye 1")
            pdf = open(os.path.join(ROOT, "Web/public/lessons/book_02_the_selfish_giant/book_02_the_selfish_giant.pdf"), "rb").read()
            page.locator("input[type=file]").first.set_input_files({"name": "E2E Kitap.pdf", "mimeType": "", "buffer": pdf})
            expect(page.get_by_role("dialog", name="PDF Görüntüleyici")).to_be_visible()
            page.keyboard.press("Escape")
            page.reload()
            page.wait_for_selector("text=Seviye 1")
            expect(page.get_by_text("E2E Kitap.pdf")).to_be_visible()
            page.get_by_role("button", name="E2E Kitap.pdf dosyasını sil").click()
            page.reload()
            page.wait_for_selector("text=Seviye 1")
            expect(page.get_by_text("E2E Kitap.pdf")).to_have_count(0)

        check("PDF upload (empty MIME), persistence, delete", pdf_upload)

        # Record media playback and OS speech calls to verify which voice is used.
        page.add_init_script("""
            window.__plays = []; window.__tts = []
            const origPlay = HTMLMediaElement.prototype.play
            HTMLMediaElement.prototype.play = function () {
              window.__plays.push({ src: this.src, t: this.currentTime }); return origPlay.call(this)
            }
            if (window.speechSynthesis) {
              const origSpeak = speechSynthesis.speak.bind(speechSynthesis)
              speechSynthesis.speak = (u) => { window.__tts.push({ text: u.text, lang: u.lang, voice: u.voice && u.voice.name }); origSpeak(u) }
            }
        """)

        def word_pronunciation():
            page.goto(BASE + "#/study/sample_ch01")
            page.reload()  # init scripts only run on a new document, not on hash navigation
            page.wait_for_selector("#dictation-input")
            page.get_by_role("button", name="Bilmiyorum / Göster").click()
            page.get_by_label("Orijinal cümle").get_by_role("button", name="suitcase", exact=True).click()
            page.get_by_role("button", name="Telaffuz").click()
            page.wait_for_function("window.__plays.length > 0", timeout=10000)
            plays = page.evaluate("window.__plays")
            index = page.request.get(page.evaluate("(p) => new URL(p, location.href).href", "lessons/word_audio/index.json")).json()
            start = index["words"]["suitcase"][0] / 1000
            assert any(abs(p["t"] - start) < 0.05 for p in plays), f"suitcase sprite not played: {plays}"
            tts = page.evaluate("window.__tts")
            assert not any((t.get("lang") or "").startswith("tr") for t in tts), f"Turkish voice used: {tts}"

        check("word pronunciation uses the studio word pack (never a Turkish voice)", word_pronunciation)

        def pdf_lesson():
            page.goto(BASE + "#/")
            page.wait_for_selector("text=Seviye 1")
            pdf = open(os.path.join(ROOT, "Web/public/lessons/book_03_the_nightingale_and_the_rose/book_03_the_nightingale_and_the_rose.pdf"), "rb").read()
            page.locator("input[type=file]").first.set_input_files({"name": "Nightingale.pdf", "mimeType": "application/pdf", "buffer": pdf})
            page.get_by_role("dialog", name="PDF Görüntüleyici").get_by_role("button", name="Dikte dersi").click()
            page.wait_for_selector("#dictation-input", timeout=60000)
            total = int(page.get_by_label("Cümleye git").get_attribute("max"))
            assert 290 <= total <= 320, f"unexpected sentence count {total}"
            body = page.evaluate("document.body.innerHTML")
            assert "dance with me" not in body, "PDF lesson leaked the sentence before answering"
            page.evaluate("window.__plays = []")
            page.get_by_role("button", name="Dinle", exact=True).click()
            page.wait_for_function("window.__plays.length >= 2 || window.__tts.length >= 1", timeout=15000)
            page.get_by_role("button", name="Bilmiyorum / Göster").click()
            expect(page.get_by_label("Orijinal cümle")).to_contain_text("dance with me")
            expect(page.get_by_role("button", name="PDF")).to_be_visible()
            page.get_by_role("button", name="Duraklat").first.click() if page.get_by_role("button", name="Duraklat").count() else None
            page.goto(BASE + "#/")
            page.wait_for_selector("text=Seviye 1")
            page.get_by_role("button", name="Nightingale.pdf dosyasını sil").click()

        check("uploaded PDF -> dictation lesson (sentences, spoken audio, split view)", pdf_lesson)

        # ── Mobile layout ────────────────────────────────────────────────
        mobile = browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
        m = mobile.new_page()

        def mobile_layout():
            for route in ["#/", "#/study/sample_ch01", "#/notebook"]:
                m.goto(BASE + route)
                m.wait_for_timeout(1500)
                overflow = m.evaluate("document.documentElement.scrollWidth - window.innerWidth")
                assert overflow <= 1, f"horizontal overflow {overflow}px on {route}"

        check("mobile 390px: no horizontal overflow", mobile_layout)
        browser.close()

    real_errors = [e for e in errors if "favicon" not in e]
    check("no console/page errors", lambda: (_ for _ in ()).throw(AssertionError("; ".join(real_errors[:3]))) if real_errors else None)

    failed = [r for r in results if not r[1]]
    print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    t0 = time.time()
    code = run()
    print(f"({time.time() - t0:.0f}s)")
    sys.exit(code)
