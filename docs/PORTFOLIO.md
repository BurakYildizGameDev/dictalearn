# DictaLearn — Portföy ve CV Metinleri

CV, LinkedIn ve mülakatlarda kullanılabilecek, projedeki gerçek çalışmaya dayanan özet metinler.

## Tek satırlık özet

**TR:** Web (React/TypeScript) ve Android (Kotlin/Compose) için çevrimdışı çalışan, 36 kitaplık İngilizce dikte ve
shadowing uygulaması: milisaniye hassas ses, kelime düzeyinde diff, OCR ile PDF'ten ders üretimi ve aralıklı tekrar.

**EN:** Offline-first English dictation & shadowing app for web (React/TypeScript) and Android (Kotlin/Compose):
millisecond-accurate audio ranges, word-level diffing, OCR-based lessons from PDFs and spaced repetition.

## CV maddeleri

- İki platformlu monorepo tasarladım: web (React 19 + TypeScript + Vite) ve Android (Kotlin + Jetpack Compose + C++ NDK).
  Her iki platform tek bir ders şemasını paylaşıyor. Domain katmanları (diff, ilerleme, sözlük, aralıklı tekrar, PDF
  ayrıştırma) platformdan bağımsız ve TDD ile yazıldı.
- Levenshtein tabanlı kelime hizalama motorunu TypeScript ve Kotlin'de birebir aynı davranışla geliştirdim. Sonuçlar renk
  körleri için renge ek olarak biçimle de (üstü çizili / altı çizili / kesikli) ayrışıyor.
- Uzun ses dosyalarında (1 saatlik kitaplar) PCM'e çözme yerine konum takibiyle milisaniye hassas aralık çalma uyguladım.
  Bu, tarayıcıda ~700 MB bellek tüketimini önledi. Android'de MediaPlayer `SEEK_CLOSEST` + asenkron hazırlık kullandım.
- Taranmış PDF'ler için çevrimdışı OCR hattı kurdum: web'de pdf.js + Tesseract.js, Android'de PdfRenderer + ML Kit.
  - İki sütunlu (İngilizce | Türkçe) sayfalarda sütun başlangıcı sayfa bazında öğreniliyor.
  - İngilizce metin, işlev kelimesi oranıyla ayırt ediliyor.
  - İlk 25 sayfa hazır olunca ders açılıyor, kalan sayfalar arka planda ekleniyor.
- 13.000 cümlelik kütüphane için içerik hattı yazdım: nöral TTS seslendirme, ReportLab PDF, 14.000 maddelik çevrimdışı
  sözlük ve 15.155 kelimelik stüdyo sesli telaffuz paketi (edge-tts kelime sınırı zaman damgalarıyla tek dosyada).
- Leitner tabanlı aralıklı tekrar, zor cümle turu, günlük hedef/seri ve CSV/Anki dışa aktarımını iki platformda aynı
  algoritmayla uyguladım.
- Kalite: 178 web + 89 Android birim testi; Playwright ve adb/uiautomator ile 22 + 16 kontrollük uçtan uca test paketleri;
  GitHub Actions ile CI, GitHub Pages yayını ve mimari başına release APK.
- Depo bakımı: 1.8 GB'lık geçmişi `git filter-repo` ve Git LFS ile ~500 MB'a indirdim; WAV olarak kaydedilmiş MP3'leri
  tespit edip gerçek MP3'e dönüştürdüm (~1.8 GB → ~220 MB).

## Mülakatta anlatılabilecek teknik kararlar

| Problem | Karar | Sonuç |
|---|---|---|
| Türkçe Windows'ta tarayıcı yalnızca Türkçe TTS sesi sunuyordu, İngilizce kelimeler anlaşılmıyordu | Kitapların nöral sesiyle önceden üretilmiş kelime "sprite"ları; sistem sesi yalnızca İngilizceyse yedek | Her cihazda aynı stüdyo kalitesi, çevrimdışı |
| OCR, Türkçe harfleri bozuyor ("Öğrenci" → "Ogrenci"), dil filtresi işe yaramıyordu | Harf yerine İngilizce işlev kelimesi oranıyla dil tespiti | Türkçe paralel metin güvenilir biçimde ayıklanıyor |
| Kopya koruması: cevap gönderilmeden metin görünmemeli | Metin ve çeviri DOM/UI ağacına hiç eklenmiyor; kelime modunda sadece çözülen kelimeler ve anlamları | Uçtan uca testlerle doğrulanan kural |
| Büyüyen PDF dersi kayıtlı ilerlemeyi bozabilirdi | Yeni cümleler yalnızca sona ekleniyor (`mergeSentences`, `extendLesson`) | Arka plan taraması sırasında konum kaymıyor |
| Statik barındırma (GitHub Pages) | Hash router, `VITE_BASE`, service worker | Alt yolda çalışan, kurulabilir, çevrimdışı web uygulaması |

## Bağlantılar

- Kaynak kod: https://github.com/BurakYildizGameDev/dictalearn
- Canlı demo: https://burakyildizgamedev.github.io/dictalearn/
- Android APK: https://github.com/BurakYildizGameDev/dictalearn/releases/latest
