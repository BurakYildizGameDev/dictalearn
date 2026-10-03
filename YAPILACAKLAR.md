# DictaLearn — Yapılacaklar Yol Haritası (Kalan Fazlar)

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
[TAMAMLANDI] Faz 6: İkili Çalışma Modu (Kelime Kelime vs Cümle Cümle)
═════════════════════════════════════════════════════════════════
[SIRADA]     Faz 5.6: Seviye 2 — 25 Kitap x 25 Sayfa (B1 Orta-Alt Klasikler)
[SIRADA]     Faz 5.7: Seviye 3 — 25 Kitap x 35 Sayfa (B2 Orta Düzey Klasikler)
[SIRADA]     Faz 5.8: Seviye 4 — 25 Kitap x 50 Sayfa (C1 İleri Düzey Klasikler)
[SIRADA]     Faz 7: Akıllı Türkçe Çeviri Sistemi (Android ML Kit & Web Sözlük)
[SIRADA]     Faz 8: Yayın ve Paketleme (GitHub Pages & Release APK)
```

---

## 📚 Faz 5 — 100 Kitaplık Multimedya Kütüphanesi (PDF + WAV + MP3 + JSON)

**Amaç:** 100 kitabın her biri için stüdyo kalitesinde insansı seslendirme (WAV & MP3), profesyonel dizgili PDF kitap ve şema uyumlu ders verisi eşliğinde kademelendirilmiş eksiksiz bir öğrenme kütüphanesi oluşturmak.

### Kütüphane Kademeleri:
1. **✅ [TAMAMLANDI] 25 Kitap x 15 Sayfa (Seviye 1 — Başlangıç-Orta / A2-B1)**:
   - 25 dünya klasiği roman ve masal adaptasyonu.
   - Her kitap: **15 Sayfa (300 Cümle) + 16 Sayfa ReportLab PDF + 120 Hedef Kelime + Stüdyo Christopher Neural WAV & MP3 (25-37 dk) + lesson.json**.
   - Toplam: **7.500 Cümle, 3.000 Hedef Kelime, 400 Sayfa PDF, 13 Saat 2 Dakika Ses**.
   - Web (`Web/public/lessons/`) ve Android (`Android/app/src/main/assets/lessons/`) senkronize edildi.
2. **25 Kitap x 25 Sayfa (Seviye 2 — Orta-Alt / B1)**:
   - Popüler kısa klasikler ve macera öyküleri.
   - Her kitap için: **25 Sayfa PDF Kitap + Stüdyo WAV & MP3 Sesi + JSON**.
   - Örnekler: *A Scandal in Bohemia (Sherlock Holmes)*, *The Gift of the Magi*, *White Fang (Expanded)*, *The Secret Garden (Expanded)*.
3. **25 Kitap x 35 Sayfa (Seviye 3 — Orta / B2)**:
   - Orta seviye edebi öyküler, gizem ve denemeler.
   - Her kitap için: **35 Sayfa PDF Kitap + Stüdyo WAV & MP3 Sesi + JSON**.
   - Örnekler: *The Red-Headed League*, *The Picture of Dorian Gray (Selection)*, *The Time Machine (Expanded)*.
4. **25 Kitap x 50 Sayfa (Seviye 4 — İleri / C1)**:
   - İleri seviye orijinal roman bölümleri, felsefi ve edebi başyapıtlar.
   - Her kitap için: **50 Sayfa PDF Kitap + Stüdyo WAV & MP3 Sesi + JSON**.
   - Örnekler: *Frankenstein*, *Great Expectations*, *Dracula (Excerpts)*, *Pride and Prejudice*.

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
- [ ] **F5.6 - F5.8 Kalan Seviyeler (25x25, 25x35, 25x50)**:
  - Seviye 2, Seviye 3 ve Seviye 4 kitaplarının üretimi.
- [ ] **F5.9 Kütüphane Gezgini ve PDF/Ses Oynatıcı (Web & Android)**:
  - Sayfa sayısına (15, 25, 35, 50 sayfa), zorluk seviyesine ve tamamlanma durumuna göre filtreleme/arama ekranı; uygulama içi PDF okuyucu ve ses oynatıcı entegrasyonu.
- [ ] **F5.9 Kütüphane Gezgini ve PDF/Ses Oynatıcı (Web & Android)**:
  - Sayfa sayısına (15, 25, 35, 50 sayfa), zorluk seviyesine ve tamamlanma durumuna göre filtreleme/arama ekranı; uygulama içi PDF okuyucu ve ses oynatıcı entegrasyonu.

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
- [ ] **F7.1 Android ML Kit Çeviri Entegrasyonu**: `MLKitTranslator.kt` servisi.
- [ ] **F7.2 Web Çevrimdışı Sözlük Modülü**: `Web/src/domain/dictionary/` sözlük indeksleyici.
- [ ] **F7.3 Kelime Bilgi Kartı (Word Popup / Tooltip)**:
  - Tıklanan kelimenin Türkçe anlamı, kelime türü (isim/fiil/sıfat) ve Hata Defteri'ne "Öğrenilecek Kelime" olarak ekleme butonu.

---

## 🚀 Faz 8 — Yayın, Dağıtım ve CV/Portföy Paketi

**Amaç:** Projeyi canlı web yayınına (GitHub Pages), bağımsız mobil mağaza dağıtımına (Itch.io APK) ve işe alımcıları/mühendislik yöneticilerini etkileyecek profesyonel bir CV/Portföy vitrinine dönüştürmek.

### Görev Listesi:
- [ ] **F8.1 GitHub Pages Canlı Web Yayını (`gh-pages`)**:
  - Vite `base` konfigürasyonunun GitHub Pages repository adresine göre ayarlanması (`/dictalearn/` veya özel domain).
  - `npm run build` ile tek tıkla veya GitHub Actions CI ile her `main` push'unda otomatik canlıya alma.
  - Canlı demo linki: İşe alımcıların ve kullanıcıların kurulumsuz hemen tarayıcıda deneyimlemesi.
- [ ] **F8.2 Itch.io Bağımsız Mağaza ve Android Release APK**:
  - `gradlew assembleRelease` ile optimize edilmiş, küçültülmüş (ProGuard/R8) evrensel APK üretimi.
  - Itch.io oyun/uygulama sayfası için vitrin görselleri, afiş, özellik listesi ve doğrudan `.apk` indirme butonu.
- [ ] **F8.3 Kapsamlı GitHub README & Mühendislik Vitrini**:
  - Dinamik rozetler: `Tests: 63 Passing`, `Android: Kotlin + C++ NDK`, `Web: React + TS + Web Audio`, `License: MIT`.
  - Sistem Mimari Şeması (Mermaid diyagramı: C++ NDK, WebAudioEngine, Studio TTS Pipeline).
  - Canlı Web Demosu ve APK İndirme linkleri.
  - GIF / Ekran görüntüleri ile dikte ve shadowing döngüsü tanıtımı.
- [ ] **F8.4 CV ve LinkedIn Portföy Şablonu**:
  - Mülakatlarda ve CV'de kullanılacak teknik kazanım metinleri: "Çoklu Platform (React + Kotlin + C++ NDK)", "Levenshtein String Diff", "Milisaniye Hassasiyetli Web Audio & ExoPlayer", "Otomatik Multimedya Üretim Hattı (Neural TTS + ReportLab PDF)".

