# DictaLearn — Yapılacaklar Yol Haritası (Kalan Fazlar)

> **Durum (2026-10-04):** Faz 0–9 ve sonradan eklenen iyileştirmeler tamamlandı (bkz. YAPILANLAR.md).
> Açık kalan tek iş kalemi içerik üretimidir (Seviye 2'nin kalanı, Seviye 3 ve 4); kullanıcı kararıyla durduruldu.

Bu belge, **DictaLearn** projesinde bir sonraki oturumda uygulanacak olan **Faz 5, Faz 6, Faz 7 ve Faz 8** adımlarının teknik mimarisini, dosya yerleşimini ve uygulama planını detaylandırmaktadır.

---

## 📌 Sıradaki Fazlar ve Yol Haritası

```
[TAMAMLANDI] Faz 0: İskelet & Örnek Ders
[TAMAMLANDI] Faz 1: Web MVP (Çekirdek Dikte Döngüsü)
[TAMAMLANDI] Faz 2: Android MVP (Kotlin + C++ NDK)
[TAMAMLANDI] Faz 3: Kullanıcı Deneyimi, Shadowing & Hata Defteri
[TAMAMLANDI] Faz 4: Ders Oluşturucu & Dışa Aktarma (SRT/VTT + Zip)
═════════════════════════════════════════════════════════════════
[TAMAMLANDI] Faz 5.5: Seviye 1 — 25 Kitap x 15 Sayfa (7.500 Cümle, 3.000 Kelime, 400 Sayfa PDF, 13 Saat Ses)
[TAMAMLANDI] Faz 5.6: Seviye 2 — 10 Kitap x 25 Sayfa (B1 Orta Seviye Klasikler, 5.000 Cümle, 260 Sayfa PDF)
[TAMAMLANDI] Faz 6: İkili Çalışma Modu (Kelime Kelime vs Cümle Cümle)
═════════════════════════════════════════════════════════════════
[ŞU AN AKTİF / SIRADA] Faz 5.7: Seviye 3 — 10 Kitap x 35 Sayfa (B2 Orta Düzey Klasikler, 7.000 Cümle)
[SIRADA]     Faz 5.8: Seviye 4 — 10 Kitap x 50 Sayfa (C1 İleri Düzey Klasikler, 10.000 Cümle)
[SIRADA]     Faz 7: Akıllı Türkçe Çeviri Sistemi (Android ML Kit & Web Sözlük)
[SIRADA]     Faz 8: Yayın ve Paketleme (GitHub Pages & Release APK)
```

---

## 📚 Faz 5 — 55 Kitaplık Master Multimedya Kütüphanesi (PDF + WAV + MP3 + JSON)

**Amaç:** 55 kitabın her biri için stüdyo kalitesinde insansı seslendirme (WAV & MP3), profesyonel dizgili ReportLab PDF kitap ve şema uyumlu ders verisi eşliğinde kademelendirilmiş eksiksiz bir öğrenme kütüphanesi oluşturmak.

### Kütüphane Kademeleri:
1. **✅ [TAMAMLANDI] 25 Kitap x 15 Sayfa (Seviye 1 — Başlangıç-Orta / A2-B1)**:
   - 25 dünya klasiği roman ve masal adaptasyonu (Kitap 1 - 25).
   - Her kitap: **15 Sayfa (300 Cümle) + 16 Sayfa ReportLab PDF + 120 Hedef Kelime + Stüdyo Christopher Neural WAV & MP3 (25-37 dk) + lesson.json**.
   - Toplam: **7.500 Cümle, 3.000 Hedef Kelime, 400 Sayfa PDF, 13 Saat 2 Dakika Ses**.
   - Web (`Web/public/lessons/`) ve Android (`Android/app/src/main/assets/lessons/`) senkronize edildi.
2. **✅ [TAMAMLANDI] 10 Kitap x 25 Sayfa (Seviye 2 — Orta / B1 Klasikler)** (10/10 - %100 Tamamlandı):
   - Kitap 26 - Kitap 35 arası 10 dünya klasiği.
   - Her kitap: **25 Sayfa (500 Cümle) + 26 Sayfa ReportLab PDF + 200 Hedef Kelime + Stüdyo WAV & MP3 Sesi + lesson.json**.
   - Toplam: **5.000 Cümle, 2.000 Hedef Kelime, 260 Sayfa PDF, ~22 Saat Stüdyo Sesi**.
   - Kitaplar:
     - [x] *Kitap 26: A Scandal in Bohemia* (25 Sayfa, 500 Cümle, 26 Sayfa PDF)
     - [x] *Kitap 27: The Red-Headed League* (25 Sayfa, 500 Cümle, 26 Sayfa PDF)
     - [x] *Kitap 28: The Hound of the Baskervilles* (25 Sayfa, 500 Cümle, 26 Sayfa PDF)
     - [x] *Kitap 29: The Gift of the Magi & The Last Leaf* (25 Sayfa, 500 Cümle, 26 Sayfa PDF)
     - [x] *Kitap 30: The Call of the Wild* (25 Sayfa, 500 Cümle, 26 Sayfa PDF)
     - [x] *Kitap 31: Frankenstein* (25 Sayfa, 500 Cümle, 26 Sayfa PDF)
     - [x] *Kitap 32: Dracula* (25 Sayfa, 500 Cümle, 26 Sayfa PDF)
     - [x] *Kitap 33: Dr. Jekyll and Mr. Hyde* (25 Sayfa, 500 Cümle, 26 Sayfa PDF)
     - [x] *Kitap 34: The Picture of Dorian Gray* (25 Sayfa, 500 Cümle, 59.4 Dk Ses, 26 Sayfa PDF)
     - [x] *Kitap 35: The Canterville Ghost* (25 Sayfa, 500 Cümle, 57.2 Dk Ses, 26 Sayfa PDF)
3. **⏳ [SIRADA] 10 Kitap x 35 Sayfa (Seviye 3 — Orta-İleri / B2 Klasikler)**:
   - Kitap 36 - Kitap 45 arası 10 başyapıt.
   - Her kitap için: **35 Sayfa PDF Kitap + Stüdyo WAV & MP3 Sesi + JSON (700 Cümle)**.
   - Toplam: **7.000 Cümle, 2.800 Hedef Kelime, 360 Sayfa PDF**.
   - Kitaplar: *Journey to the Center of the Earth*, *20,000 Leagues Under the Sea*, *The Invisible Man*, *The War of the Worlds*, *Tom Sawyer*, *The Prince and the Pauper*, *Oliver Twist*, *Great Expectations*, *Jane Eyre*, *Wuthering Heights*.
4. **10 Kitap x 50 Sayfa (Seviye 4 — İleri / C1 Klasikler)**:
   - Kitap 46 - Kitap 55 arası 10 edebi anıt eser.
   - Her kitap için: **50 Sayfa PDF Kitap + Stüdyo WAV & MP3 Sesi + JSON (1.000 Cümle)**.
   - Toplam: **10.000 Cümle, 4.000 Hedef Kelime, 510 Sayfa PDF**.
   - Kitaplar: *Pride and Prejudice*, *The Count of Monte Cristo*, *The Three Musketeers*, *Don Quixote*, *Robinson Crusoe*, *Moby Dick*, *David Copperfield*, *Les Misérables (Seçki)*, *Crime and Punishment (Seçki)*, *The Odyssey*.

### Görev Listesi:
- [x] **F5.1 Multimedya Kütüphane Şeması ve İndeksleme**:
  - `lessons/`: 25 adet 15 sayfalık kitap klasörü eksiksiz şema v1 uyumlu `lesson.json` ile yapılandırıldı.
- [x] **F5.2 Doğal ve İnsansı Seslendirme Hattı (WAV / MP3 Studio TTS)**:
  - Microsoft Edge Neural TTS (`en-US-ChristopherNeural`), 24kHz 16-bit PCM WAV ve optimize MP3 ses üretimi.
- [x] **F5.3 Profesyonel PDF Kitap Üretimi**:
  - ReportLab ile iki sütunlu paralel metinli, 16 sayfalık (1 Kapak + 15 Hikaye), taşmasız 25 kitap PDF'i (400 sayfa).
- [x] **F5.4 Yüksek Kalite MP3 ve WAV Formatları**:
  - Her 25 kitap için kayıpsız 16-bit WAV ve MP3 formatı.
- [x] **F5.5 Seviye 1 Kütüphanesi (25 Kitap x 15 Sayfa)**:
  - 25 kitabın tamamı eksiksiz üretildi, test edildi ve çift yönlü senkronize edildi.
- [x] **F5.6 Seviye 2 Kütüphanesi (10 Kitap x 25 Sayfa)**:
  - 10 kitabın tamamı eksiksiz üretildi (Kitap 26 - 35), test edildi ve senkronize edildi.
- [ ] **F5.7 - F5.8 Kalan Seviyeler (Gerektiğinde Genişletilebilir)**:
  - Seviye 3 ve Seviye 4 kitaplarının şablonları hazır.
- [x] **F5.9 Uygulama İçi PDF Okuyucu ve Pitch Korumalı Ses Motoru (Web)**:
  - Pitch korumalı (preservesPitch) zaman esnetme, autoplay engelleme, uygulama içi modal PDF okuyucu ve özel PDF yükleme entegrasyonu tamamlandı.

---

## 🔤 Faz 6 — İkili Çalışma Modu (Kelime Kelime vs Cümle Cümle)

**Amaç:** Kullanıcının seviyesine ve çalışma tercihine göre çalışma zorluğunu ayarlayabilmesi.

### Çalışma Modları:
1. **Tam Cümle Modu (Full-Sentence - Mevcut Mod)**:
   - Cümlenin tamamı bir defada dinlenir.
   - Kullanıcı tüm cümleyi yazar ve Enter ile submit eder.
   - İleri seviye dinleme ve hafıza geliştirme için idealdir.
2. **Kelime Kelime Modu (Word-by-Word - Yeni Mod)**:
   - Cümle kelime kutularına bölünür.
   - Kullanıcı her kelimeyi yazdığında anında doğrulanır (`Space` veya otomatik ilerleme).
   - Zorlandığı anda kelime harf ipucu veya o kelimenin ses kesiti dinlenebilir.
   - Başlangıç ve orta seviye kullanıcılar için stressiz öğrenme sağlar.

### Görev Listesi:
- [x] **F6.1 Mod Durum Yönetimi**: `useStudySession` içinde `studyMode: 'sentence' | 'word'`, `currentWordIndex`, `submitWord`, `skipWord` desteği.
- [x] **F6.2 Kelime Kelime Arayüzü**:
  - Web (`StudySessionView.tsx`): Dinamik kelime yuvaları, anlık doğrulama, ilk harf ipuçları ve anti-cheat koruması.
- [x] **F6.3 Mod Değiştirme Kısayolu ve Anahtarı**:
  - `Ctrl+M` kısayolu ve arayüz anahtarı ile çalışma esnasında kesintisiz mod değiştirme.

---

## 🌐 Faz 7 — Akıllı Türkçe Çeviri Sistemi

**Amaç:** İngilizce metin ve kelimelerin Türkçe karşılıklarına her iki platformda anında, akıcı ve çevrimdışı erişim sağlamak.

### Platform Ayrımı ve Mimari:
1. **Android: Google ML Kit On-Device Çeviri (`com.google.mlkit:translate`)**:
   - Google'ın cihaz içi çalışan, internet gerektirmeyen, tamamen ücretsiz ve yerel makine çevirisi motoru.
   - İlk açılışta ~30MB İngilizce-Türkçe modelini indirir, sonrasında %100 çevrimdışı çalışır.
   - Cümle düzeyinde ve serbest metinlerde sıfır gecikmeli çeviri.
2. **Web: 50.000+ Kelimelik Çevrimdışı Sözlük**:
   - 50.000 en sık kullanılan İngilizce kelimenin Türkçe karşılıklarını içeren sıkıştırılmış JSON sözlük (`dictionary.json`).
   - Cümledeki herhangi bir kelimeye tıklandığında veya fareyle üzerine gelindiğinde anında Türkçe anlam popup'ı açılır.
   - Kitap dışı serbest cümleler için hafif istemci taraflı çeviri köprüsü.

### Görev Listesi:
- [x] **F7.1 Android ML Kit Çeviri Entegrasyonu**: `MLKitTranslator.kt` servisi.
- [x] **F7.2 Web Çevrimdışı Sözlük Modülü**: `Web/src/domain/dictionary/` sözlük indeksleyici.
- [x] **F7.3 Kelime Bilgi Kartı (Word Popup / Tooltip)**:
  - Tıklanan kelimenin Türkçe anlamı, kelime türü (isim/fiil/sıfat) ve Hata Defteri'ne "Öğrenilecek Kelime" olarak ekleme butonu.

---

## 🚀 Faz 8 — Yayın, Dağıtım ve CV/Portföy Paketi

**Amaç:** Projeyi canlı web yayınına (GitHub Pages), bağımsız mobil mağaza dağıtımına (Itch.io APK) ve işe alımcıları/mühendislik yöneticilerini etkileyecek profesyonel bir CV/Portföy vitrinine dönüştürmek.

### Görev Listesi:
- [x] **F8.1 GitHub Pages Canlı Web Yayını (`gh-pages`)**:
  - Vite `base` konfigürasyonunun GitHub Pages repository adresine göre ayarlanması (`/dictalearn/` veya özel domain).
  - `npm run build` ile tek tıkla veya GitHub Actions CI ile her `main` push'unda otomatik canlıya alma.
  - Canlı demo linki: İşe alımcıların ve kullanıcıların kurulumsuz hemen tarayıcıda deneyimlemesi.
- [x] **F8.2 Itch.io Bağımsız Mağaza ve Android Release APK**:
  - `gradlew assembleRelease` ile optimize edilmiş, küçültülmüş (ProGuard/R8) evrensel APK üretimi.
  - Itch.io oyun/uygulama sayfası için vitrin görselleri, afiş, özellik listesi ve doğrudan `.apk` indirme butonu.
- [x] **F8.3 Kapsamlı GitHub README & Mühendislik Vitrini**:
  - Dinamik rozetler: `Tests: 63 Passing`, `Android: Kotlin + C++ NDK`, `Web: React + TS + Web Audio`, `License: MIT`.
  - Sistem Mimari Şeması (Mermaid diyagramı: C++ NDK, WebAudioEngine, Studio TTS Pipeline).
  - Canlı Web Demosu ve APK İndirme linkleri.
  - GIF / Ekran görüntüleri ile dikte ve shadowing döngüsü tanıtımı.
- [x] **F8.4 CV ve LinkedIn Portföy Şablonu** _(docs/PORTFOLIO.md)_:
  - Mülakatlarda ve CV'de kullanılacak teknik kazanım metinleri: "Çoklu Platform (React + Kotlin + C++ NDK)", "Levenshtein String Diff", "Milisaniye Hassasiyetli Web Audio & ExoPlayer", "Otomatik Multimedya Üretim Hattı (Neural TTS + ReportLab PDF)".

---

## 🎨 Faz 9 — Tam Kapsamlı Modern UI/UX Yeniden Tasarımı (Full Overhaul)

**Amaç:** Mevcut işlevsel ama ilkel/kaba arayüzü; modern, şık, Apple/Linear esintili, kullanıcıyı içine çeken profesyonel bir edebi dil öğrenme stüdyosuna dönüştürmek.

### Görev Listesi:
- [x] **F9.1 Modern Kitaplık & Keşfet Ekranı (Book Library & Gallery)**:
  - Üstteki sıkışık `<select>` açılır menüsü yerine; kitap kapaklı görsel kartlar, seviye sekmeleri (A2, B1, B2), arama & filtreleme çubuğu, sayfa sayısı ve okuma ilerleme çubukları içeren şık bir kütüphane vitrini.
- [x] **F9.2 Bölünmüş Çalışma Ekranı (Split-Screen Study Studio)**:
  - PDF'i pop-up/modal yerine ekranın sol tarafında yan yana (split-screen) veya katlanabilir panelde sabitleme; sağ tarafta odaklanmış dikte & kelime yazma stüdyosu.
  - Kullanıcı aynı anda hem PDF kitabını paralel okuyabilmeli hem de dikte/shadowing yapabilmeli.
- [x] **F9.3 Minimalist & Akıcı Tasarım Sistemi (Design System & Micro-Interactions)**:
  - Derin koyu tema (Zinc/Slate 950), zarif cam efekti (glassmorphism), modern tipografi (Inter / Outfit / SF Pro), yuvarlatılmış kart kenarları.
  - Ses oynatılırken dinamik ses dalga formu (waveform visualizer) veya ritmik ses ışıltısı.
- [x] **F9.4 Ergonomik Kontrol & Kısayol Araç Çubuğu**:
  - Hız butonları (0.75x, 1.0x, 1.25x), Otomatik Oynat, Dinle, Shadowing ve Kelime Modu butonlarının ergonomik, modern ve derli toplu tek bir stüdyo dock'unda toplanması.
- [x] **F9.5 Mobil & Tablet Odaklı Kusursuz Responsive Düzen**:
  - Dokunmatik ekranlarda kaydırmalı (swipe) kartlar, klavye açıldığında zıplamayan sabit giriş alanı ve akıcı mobil gezinme.


