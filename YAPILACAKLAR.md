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
[SIRADA]     Faz 5: 100 Kitaplık Multimedya Kütüphanesi (PDF + WAV + MP4 + JSON)
[SIRADA]     Faz 6: İkili Çalışma Modu (Kelime Kelime vs Cümle Cümle)
[SIRADA]     Faz 7: Akıllı Türkçe Çeviri Sistemi (Android ML Kit & Web Sözlük)
[SIRADA]     Faz 8: Yayın ve Paketleme (GitHub Pages & Release APK)
```

---

## 📚 Faz 5 — 100 Kitaplık Multimedya Kütüphanesi (PDF + WAV + MP4 + JSON)

**Amaç:** 100 kitabın her biri için stüdyo kalitesinde insansı seslendirme (WAV), profesyonel dizgili PDF kitap ve altyazılı senkronize MP4 video eşliğinde kademelendirilmiş eksiksiz bir öğrenme kütüphanesi oluşturmak.

### Kütüphane Kademeleri:
1. **25 Kitap x 15 Sayfa (Seviye 1 — Başlangıç / A1-A2)**:
   - Kısa fabllar, basitleştirilmiş dünya masalları ve temel diyaloglar.
   - Her kitap için: **15 Sayfa PDF Kitap + Stüdyo WAV Sesi + Senkronize MP4 Video + JSON**.
   - Örnekler: *The Happy Prince*, *The Selfish Giant*, *Aesop's Classic Fables*, *The Tortoise and the Hare*, *The Little Red Hen*.
2. **25 Kitap x 25 Sayfa (Seviye 2 — Orta-Alt / B1)**:
   - Popüler kısa klasikler ve macera öyküleri.
   - Her kitap için: **25 Sayfa PDF Kitap + Stüdyo WAV Sesi + Senkronize MP4 Video + JSON**.
   - Örnekler: *A Scandal in Bohemia (Sherlock Holmes)*, *The Gift of the Magi*, *White Fang (Adapted)*, *The Secret Garden (Ch. 1-3)*.
3. **25 Kitap x 35 Sayfa (Seviye 3 — Orta / B2)**:
   - Orta seviye edebi öyküler, gizem ve denemeler.
   - Her kitap için: **35 Sayfa PDF Kitap + Stüdyo WAV Sesi + Senkronize MP4 Video + JSON**.
   - Örnekler: *The Red-Headed League*, *The Picture of Dorian Gray (Selection)*, *The Time Machine (H.G. Wells)*.
4. **25 Kitap x 50 Sayfa (Seviye 4 — İleri / C1)**:
   - İleri seviye orijinal roman bölümleri, felsefi ve edebi başyapıtlar.
   - Her kitap için: **50 Sayfa PDF Kitap + Stüdyo WAV Sesi + Senkronize MP4 Video + JSON**.
   - Örnekler: *Frankenstein*, *Great Expectations*, *Dracula (Excerpts)*, *Pride and Prejudice*.

### Görev Listesi:
- [ ] **F5.1 Multimedya Kütüphane Şeması ve İndeksleme**:
  - `library/index.json`: Kitap ID, başlık, yazar, seviye (1-4), sayfa sayısı (15/25/35/50), tahmini süre, PDF yolu, WAV yolu, MP4 yolu ve kapak resmi.
- [ ] **F5.2 Doğal ve İnsansı Seslendirme Hattı (WAV / Studio TTS)**:
  - Eski mekanik sesler yerine, 2026'nın en iyi açık kaynak ve doğal ses motorları (Kokoro v1.0 veya Microsoft Edge Neural sesleri: Christopher/Guy/Jenny/Ryan) ile stüdyo netliğinde, tonlamalı ve nefes alan ses üretimi.
- [ ] **F5.3 Profesyonel PDF Kitap Üretimi**:
  - 100 kitabın her biri için sayfa sayfa (15, 25, 35, 50 sayfa), kapak, şık tipografi, sayfa numaraları ve alt/yan kelime notları içeren indirilebilir ve okunabilir PDF kitaplar.
- [ ] **F5.4 Senkronize MP4 Video Üretimi**:
  - Ses ile görsel metnin/sayfanın senkron aktığı, cümle/kelime vurgulu video formatı.
- [ ] **F5.5 - F5.8 Kademeli 100 Kitap Üretimi (25x15, 25x25, 25x35, 25x50)**:
  - Her biri için PDF, WAV, MP4 ve JSON paketlerinin eksiksiz oluşturulması.
- [ ] **F5.9 Kütüphane Gezgini ve PDF/Video Oynatıcı (Web & Android)**:
  - Sayfa sayısına (15, 25, 35, 50 sayfa), zorluk seviyesine ve tamamlanma durumuna göre filtreleme/arama ekranı; uygulama içi PDF okuyucu ve MP4 video oynatıcı entegrasyonu.

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
- [ ] **F6.1 Mod Durum Yönetimi**: `StudySession` ve `StudySessionViewModel` içine `studyMode: 'full-sentence' | 'word-by-word'` eklenmesi.
- [ ] **F6.2 Kelime Kelime Arayüzü**:
  - Web (`WordByWordInput.tsx`) ve Android (`WordByWordRow.kt`).
- [ ] **F6.3 Mod Değiştirme Kısayolu ve Anahtarı**:
  - `Ctrl+M` kısayolu veya ekran anahtarı ile çalışma esnasında kesintisiz mod değiştirme.

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

## 🚀 Faz 8 — Yayın ve Paketleme

**Amaç:** Canlı GitHub Pages web sitesi ve son kullanıcıya hazır imzalı Android APK sunmak.

### Görev Listesi:
- [ ] **F8.1 GitHub Pages Otomasyonu**: GitHub Actions ile `Web/dist` çıktısının otomatik `gh-pages` dalına dağıtılması.
- [ ] **F8.2 Android Release İmzalı APK**: Release build pipeline'ı ve APK indirme bağlantısı.
- [ ] **F8.3 Proje Dokümantasyonu**: Detaylı `README.md` (özellikler, ekran görüntüleri, canlı link, kısayol tablosu, APK indirme linki).
