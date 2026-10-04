# -*- coding: utf-8 -*-
"""
Offline check of the installable web app (production build only; the service worker is disabled in dev).

    cd Web && VITE_BASE=/dictalearn/ npm run build && VITE_BASE=/dictalearn/ npx vite preview --port 5200
    python tools/e2e/pwa_offline.py http://localhost:5200/dictalearn/
"""
import sys

from playwright.sync_api import expect, sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:5200/dictalearn/"
failed = 0


def check(name, fn):
    global failed
    try:
        fn()
        print(f"  PASS  {name}")
    except Exception as exc:  # noqa: BLE001
        failed += 1
        print(f"  FAIL  {name}: {str(exc).splitlines()[0][:200]}")


with sync_playwright() as p:
    browser = p.chromium.launch(channel="chromium")
    ctx = browser.new_context()
    page = ctx.new_page()

    def installable():
        page.goto(BASE)
        page.wait_for_selector("text=Seviye 1")
        manifest = page.evaluate("document.querySelector('link[rel=manifest]').href")
        data = page.request.get(manifest).json()
        assert data["display"] == "standalone" and len(data["icons"]) >= 2, data
        for icon in data["icons"]:
            r = page.request.get(page.evaluate("(s) => new URL(s, document.querySelector('link[rel=manifest]').href).href", icon["src"]))
            assert r.ok and r.headers["content-type"].startswith("image/png"), icon
        assert page.title() == "DictaLearn"
        page.evaluate("navigator.serviceWorker.ready.then(() => true)")
        page.reload()  # let the worker control the page
        page.wait_for_function("navigator.serviceWorker.controller !== null", timeout=15000)

    check("manifest, icons and service worker are installed", installable)

    def study_online_then_offline():
        page.goto(BASE + "#/study/sample_ch01")
        page.wait_for_selector("#dictation-input")
        page.wait_for_timeout(1500)  # lesson.json, audio and word data are cached on first use
        ctx.set_offline(True)
        page.reload()
        page.wait_for_selector("#dictation-input", timeout=15000)
        page.get_by_role("button", name="Bilmiyorum / Göster").click()
        expect(page.get_by_label("Orijinal cümle")).to_contain_text("suitcase")
        page.goto(BASE + "#/")
        page.wait_for_selector("text=Seviye 1")
        ctx.set_offline(False)

    check("library and a previously opened lesson work offline", study_online_then_offline)
    browser.close()

print("PWA offline:", "OK" if failed == 0 else f"{failed} failed")
sys.exit(1 if failed else 0)
