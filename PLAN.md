# DictaLearn — Geliştirme Planı

Açık kaynak, klavye ve ses odaklı İngilizce dikte ve çeviri çalışma aracı. "DictaLearn" çalışma başlığıdır.

Bu proje iki hedef platform için tek bir depoda geliştirilir:
1. **Web (`Web/`):** React + TypeScript + Vite + Tailwind CSS (GitHub Pages ve masaüstü/mobil web tarayıcıları).
2. **Android (`Android/`):** Kotlin + Jetpack Compose + C++ NDK (Yüksek performanslı yerel mobil deneyim).

Ortak ders formatı (`lessons/`) her iki platformda da aynı `lesson.json` ve ses dosyasıyla çalışır.

---

## 1. Bu doküman nasıl kullanılır

Depo kökünde iki dosya durur:
- `CLAUDE.md`: Her oturumda geçerli olan kısa mimari kurallar, komutlar ve kısıtlamalar.
- `PLAN.md`: Ayrıntılı tasarım kararları, veri şemaları ve fazlara bölünmüş görev listesi.

### Görev döngüsü

Her görev (`F1.2` gibi) için aynı döngü uygulanır:
1. Görevin kapsamını ve atıf yaptığı tasarım bölümlerini oku.
2. Önce testleri yaz (TDD), sonra uygulamayı geliştir.
3. Test ve analiz çıktılarını doğrula.
4. `PLAN.md`'de ilgili görevin kutusunu `[x]` olarak işaretle.
5. Uygun commit mesajıyla tek bir commit at.

### İşaretler
- `[ ]` yapılacak, `[x]` bitti.
- 👤 insan gerektiren görev: ses dosyası sağlama, kulakla/gözle doğrulama, cihaz testi.

---

## 2. Ürün Özeti

### Amaç
Pasif dinleme alışkanlığını kırıp kullanıcıyı her cümlede dört ayrı beceriyle çalıştırmak:
1. **Dinle:** Cümle yalnızca ses olarak duyulur, metin gizlidir.
2. **Yaz:** Kullanıcı duyduğunu klavyeyle yazar.
3. **Doğrula ve düzelt:** Orijinal metin açılır, farklar kelime kelime gösterilir, hata varsa kullanıcı doğru haliyle yeniden yazar.
4. **Çevir ve seslendir:** Çeviri açılır, kullanıcı cümleyi sesli tekrar eder (shadowing) ve sonraki cümleye geçer.

### İlkeler
- Çevrimdışı ve yerel çalışır. Hesap, sunucu, telemetri yoktur.
- Web sürümü GitHub Pages üzerinde tamamen statik ve ücretsiz barındırılır.
- Masaüstünde fareye dokunmadan tamamen klavye ile kullanılabilir.
- Dersler taşınabilir bir klasördür: bir `lesson.json` ve bir ses dosyası.
- Ders formatı dil çiftinden bağımsızdır (Varsayılan: İngilizce → Türkçe).

### v1 Kapsamı Dışında
Mikrofon kaydı ve telaffuz puanlama, bulut eşitleme, otomatik transkripsiyon, yapay zeka çevirisi.

---

## 3. Mimari ve Tasarım Kararları

| # | Konu | Karar | Gerekçe |
|---|---|---|---|
| 1 | Proje Yapısı | Monorepo (`Web/` ve `Android/`) | Web için React, Android için Kotlin/C++ en iyi deneyimi sunar; tek repoda yönetilir |
| 2 | Ortak Veri | `lessons/<lesson_id>/` | Aynı `lesson.json` ve ses dosyası hem Web hem Android tarafından doğrudan okunur |
| 3 | Web Ses Motoru | `Web Audio API` | Tarayıcıda milisaniye hassasiyetinde kesme, hızlandırma ve anında durdurma |
| 4 | Android Ses Motoru | `Media3 / ExoPlayer` + `C++ Oboe` opsiyonu | Düşük gecikmeli ve kararlı ses çalma |
| 5 | Diff Algoritması | Saf TypeScript & Saf Kotlin/C++ | Kelime düzeyinde Levenshtein hizalaması; dış bağımlılık yok |
| 6 | Depolama | Web: `LocalStorage / IndexedDB`, Android: `Room / JSON File` | Tamamen çevrimdışı, hafif ve taşınabilir |
| 7 | Zaman Birimi | Tamsayı milisaniye (`int`) | Kayan nokta yuvarlama hatalarından kaçınmak |
| 8 | Kısayollar | Duruma duyarlı harita | Yazı yazarken Space tuşunun sesi durdurmasını engellemek |

---

## 4. Teknik Tasarım

### 4.1 Oturum Durum Makinesi

`StudySession` aşağıdaki durumları yönetir:

| Durum | Ekranda ne var | Çıkış |
|---|---|---|
| `dictating` | Ses çalar, yazma alanı odaktadır, orijinal metin ve çeviri DOM'da YOKTUR | `Enter` → `reviewing` |
| `reviewing` | Diff ve orijinal metin. Hata varsa düzeltme alanı açık ve odakta | Hatasızsa `Enter` → `shadowing`. Hatalıysa doğru yazılınca `Enter` → `shadowing` |
| `shadowing` | Orijinal metin, çeviri (aç/kapa), not. Ses tekrar çalınabilir | `Enter` → sonraki segment için `dictating`; son segmentse `completed` |
| `completed` | Ders özeti (doğruluk oranı, hata listesi) | Ders listesine dönüş |

Kurallar:
- `dictating` durumuna girildiğinde segment bir kez kendiliğinden çalar.
- Boş cevapla `Enter` hiçbir şey yapmaz. `Ctrl+Enter` pes etmedir (tüm kelimeler eksik sayılır ve cevabı gösterir).
- `reviewing` içinde düzeltme, cümlenin orijinaline bakılarak baştan yazılmasıdır. `Ctrl+Enter` düzeltmeyi atlar.
- Hata Defteri'ne yalnızca ilk denemenin hataları kaydedilir.

### 4.2 Kısayol Haritası

- `Ctrl` kombinasyonları her durumda çalışır.
- Çıplak tuşlar (`Space`, `R`, `T`) yalnızca hiçbir metin alanı odakta değilken çalışır.

| Kısayol | Eylem | Geçerli Durum |
|---|---|---|
| `Enter` | Kontrol et / düzeltmeyi gönder / sonraki segment | Her durum |
| `Ctrl+Enter` | Pes et ve cevabı göster / düzeltmeyi atla | `dictating`, `reviewing` |
| `Ctrl+Space` | Oynat / duraklat | Her durum |
| `Ctrl+R` | Segmenti baştan çal | Her durum |
| `Ctrl+1` `Ctrl+2` `Ctrl+3` | Hız 0.75x / 1.0x / 1.25x | Her durum |
| `Ctrl+T` | Çeviriyi aç / kapa | `shadowing` |
| `PageUp` `PageDown` | Önceki / sonraki segment | Her durum |
| `F1` | Kısayol yardım penceresi | Her durum |

### 4.3 Diff Motoru

Girdi: `expectedText`, `typedText`, `DiffOptions` (`ignoreCase: true`, `ignorePunctuation: true`).

**Algoritma:**
1. Metinler boşluklardan kelimelere bölünür.
2. Normalizasyon: kesme ve tırnaklar düzleştirilir (`’` → `'`), kelime başı/sonu noktalama temizlenir.
3. Kelime dizileri üzerinde Levenshtein mesafe hizalaması yapılır.
4. Her kelime 4 durumdan birini alır:
   - `equal`: Doğru yazılmış kelime.
   - `substitute`: Yanlış yazılmış kelime (harf farkı vurgulanır).
   - `missing`: Beklenen ama kullanıcının yazmadığı eksik kelime.
   - `extra`: Beklenmeyen fazladan yazılmış kelime.
5. Çıktı: `DiffResult { words, correctCount, expectedCount, accuracy, isPerfect }`.

### 4.4 Ses Motoru Arayüzü (`AudioEngine`)

```typescript
export interface AudioEngine {
  load(urlOrPath: string): Promise<void>;
  playRange(startMs: number, endMs: number): Promise<void>;
  pause(): void;
  resume(): void;
  setSpeed(speed: number): void;
  onRangeComplete(callback: () => void): void;
  onStatusChange(callback: (status: AudioStatus) => void): void;
  dispose(): void;
}
```

### 4.5 Ders Veri Şeması (`lesson.json`)

```json
{
  "schema_version": 1,
  "lesson_id": "sample_ch01",
  "title": "Chapter 1: The Departure",
  "source_lang": "en",
  "target_lang": "tr",
  "audio_file": "audio.mp3",
  "attribution": {
    "source": "LibriVox / Public Domain",
    "license": "Public Domain"
  },
  "segments": [
    {
      "id": 1,
      "start_ms": 0,
      "end_ms": 4800,
      "text": "He packed his small brown suitcase and opened the door.",
      "translation": "Küçük kahverengi bavulunu topladı ve kapıyı açtı.",
      "notes": "packed: düzenli fiil, -ed sonu /t/ okunur"
    },
    {
      "id": 2,
      "start_ms": 4900,
      "end_ms": 8500,
      "text": "The morning cold hit him immediately.",
      "translation": "Sabahın soğuğu anında yüzüne çarptı.",
      "notes": "immediately: zarf (hemen, derhal)"
    }
  ]
}
```

---

## 5. Fazlar ve Görev Listesi

### Faz 0 — Temel ve İskelet (Web & Android)

**Amaç:** Hem Web hem Android tarafında derlenen temiz bir iskelet, örnek kamu malı ders paketi ve CI.

- [x] **F0.1 Web İskeleti:** `Web/` altında Vite + React + TypeScript + Tailwind CSS kurulumu, Vitest test ortamı ve ESLint yapılandırması.
- [x] **F0.2 Android İskeleti:** `Android/` altında Gradle + Kotlin + Jetpack Compose + C++ CMake/NDK iskeleti.
- [x] **F0.3 👤 Örnek Ders:** `lessons/sample_ch01/` klasörüne 30-60 saniyelik kamu malı ses (`audio.wav`) ve doğrulanmış `lesson.json` eklenmesi.
- [x] **F0.4 Web Audio API Denemesi:** Tarayıcıda ses segmenti çalma ve `end_ms` bitiş hassasiyetinin doğrulanması.
- [x] **F0.5 CI Yapılandırması:** GitHub Actions iş akışı: PR ve push'larda Web testleri ve derlemesi.

---

### Faz 1 — Web MVP: Çekirdek Döngü

**Amaç:** Web tarayıcısında örnek dersin klavyeyle baştan sona çalışılabilmesi: Dinle → Yaz → Diff → Sonraki segment.

- [x] **F1.1 Ders Yükleyici & Doğrulama:** `Web/src/domain/lessons/` içinde JSON şeması doğrulayıcı ve yükleyici (Zorunlu alanlar, sıralı zamanlar).
- [x] **F1.2 Diff Motoru:** `Web/src/domain/diff/` içinde kelime düzeyinde Levenshtein hizalaması ve %100 test kapsamı (§4.3 test senaryoları).
- [x] **F1.3 Web Ses Motoru:** `Web/src/audio/` içinde `WebAudioEngine` (Web Audio API ile milisaniye hassasiyetli `playRange`).
- [x] **F1.4 Oturum Durum Yönetimi:** `useStudySession` hook'u: `dictating` -> `reviewing` -> `shadowing` -> `completed` geçişleri.
- [x] **F1.5 Çalışma Ekranı Arayüzü:** Dikte yazma alanı (otomatik tamamlama/düzeltme kapalı), renkli ve biçimli diff görünümü, oynatma butonları.
- [x] **F1.6 Web Kısayolları:** `Enter`, `Ctrl+Enter`, `Ctrl+Space`, `Ctrl+R` kısayollarının metin kutusu odağına göre yönetimi.
- [x] **F1.7 👤 Canlı Web Testi:** Web uygulamasının yerel olarak çalıştırılıp örnek dersin klavyeyle başarıyla tamamlanması. _(Otomatik: `tools/e2e/web_e2e.py`, 16 kontrol, dev + prod derlemesi. Kulakla ses kalitesi kontrolü insan tarafından yapılmalı.)_

---

### Faz 2 — Android MVP: Çekirdek Döngü (Kotlin + C++)

**Amaç:** Android telefonda örnek dersin dokunmatik ve klavye desteğiyle yerel olarak çalışılabilmesi.

- [x] **F2.1 Android Veri Modelleri:** Kotlin veri sınıfları ve `lesson.json` ayrıştırıcısı.
- [x] **F2.2 Android Diff Motoru:** Kotlin veya C++ NDK tabanlı Levenshtein diff motoru ve birim testleri.
- [x] **F2.3 Android Ses Motoru:** Media3 / ExoPlayer (veya Oboe C++) ile milisaniye hassasiyetli aralık çalma.
- [x] **F2.4 Android Jetpack Compose Ekranı:** Dikte giriş kutusu, diff görselleştirmesi ve kontrol butonları.
- [x] **F2.5 👤 Android Cihaz/Emülatör Testi:** APK'nın telefonda çalıştırılıp ses ve yazma akışının doğrulanması. _(Otomatik: `tools/e2e/android_e2e.py`, Pixel 7 API 34 emülatörü, debug + R8 release APK, 13 kontrol. Fiziksel cihaz testi önerilir.)_

---

### Faz 3 — Kullanıcı Deneyimi ve Hata Defteri (Her İki Platform)

**Amaç:** Düzeltme akışının tamamlanması, shadowing adımı ve yanlış kelimelerin Hata Defterine kaydedilmesi.

- [x] **F3.1 Düzeltme Akışı:** `reviewing` durumunda yanlış kelime varsa kullanıcının cümleyi doğru haliyle yeniden yazması.
- [x] **F3.2 Shadowing Adımı:** Çeviri aç/kapa (`Ctrl+T`), cümle notları, sesi tekrar dinleyip sesli tekrar etme.
- [x] **F3.3 Hata Defteri Deposu:** Yanlış yazılan (`substitute`) ve unutulan (`missing`) kelimelerin yerel olarak saklanması.
- [x] **F3.4 Ders Sonu Özeti Ekranı:** Tamamlanan dersteki doğruluk yüzdesi, toplam tekrar sayısı ve hatalı kelimeler.
- [x] **F3.5 Hız Kontrolü:** 0.75x, 1.0x, 1.25x hız seçenekleri ve kalıcılığı.

---

### Faz 4 — Ders Oluşturucu & Dışa Aktarma

**Amaç:** Kullanıcının kendi ses ve altyazı dosyalarından ders üretebilmesi.

- [x] **F4.1 Altyazı Ayrıştırıcıları:** SRT ve VTT dosyalarını segment listesine dönüştüren saf ayrıştırıcı.
- [x] **F4.2 Zip Paketi Alışverişi:** Dersleri `.zip` olarak dışa ve içe aktarma desteği.
- [x] **F4.3 Segment Düzenleyici Arayüzü:** Başlangıç/bitiş zamanlarını ayarlama, metin ve çeviri düzenleme.

---

### Faz 5 — 100 Kitaplık Multimedya Kütüphanesi (PDF + WAV + MP3 + JSON)

**Amaç:** 100 kitabın her biri için stüdyo kalitesinde doğal insan seslendirmesi (WAV & MP3), profesyonel dizgili PDF kitap ve şema uyumlu ders verisi eşliğinde kademelendirilmiş eksiksiz bir öğrenme kütüphanesi oluşturmak.

- [x] **F5.1 Multimedya Kütüphane Şeması ve İndeksleme:** Kitap ID, başlık, yazar, seviye (1-4), sayfa sayısı (15/25/35/50), tahmini süre, PDF/WAV/MP3 dosya yolları ve metaveri yapısı.
- [x] **F5.2 Doğal ve İnsansı Seslendirme Hattı (WAV / MP3 Studio TTS):** Robotik/eski sesler yerine Microsoft Edge Neural sesleri (Christopher/Guy/Jenny/Ryan) ile stüdyo kalitesinde, tonlamalı ve nefes alan kristal netliğinde seslendirme.
- [x] **F5.3 Profesyonel PDF Kitap Üretimi:** 100 kitabın her biri için sayfa sayfa (15, 25, 35, 50 sayfa), kapak, şık tipografi, sayfa numaraları ve alt/yan kelime notları içeren indirilebilir ve okunabilir PDF kitaplar.
- [x] **F5.4 Yüksek Kalite MP3 ve WAV Formatları:** Taşınabilirlik için hafif MP3 ve kayıpsız hassasiyet için WAV formatlarının birlikte sunulması.
- [x] **F5.5 25 Kitap x 15 Sayfa (Seviye 1 — A1/A2):** Fabllar ve temel seviye metinler (PDF + WAV + MP3 + JSON).
- [ ] **F5.6 25 Kitap x 25 Sayfa (Seviye 2 — B1):** Kısa klasikler ve macera öyküleri (PDF + WAV + MP3 + JSON). _(2026-10-04: kitap üretimi kullanıcı kararıyla durduruldu; mevcut: Seviye 1 = 25 kitap, Seviye 2 = 11 kitap.)_
- [ ] **F5.7 25 Kitap x 35 Sayfa (Seviye 3 — B2):** Orta seviye öykü ve gizem metinleri (PDF + WAV + MP3 + JSON). _(2026-10-04: kitap üretimi kullanıcı kararıyla durduruldu; mevcut: Seviye 1 = 25 kitap, Seviye 2 = 11 kitap.)_
- [ ] **F5.8 25 Kitap x 50 Sayfa (Seviye 4 — C1):** İleri seviye romanlar ve derin edebi metinler (PDF + WAV + MP3 + JSON). _(2026-10-04: kitap üretimi kullanıcı kararıyla durduruldu; mevcut: Seviye 1 = 25 kitap, Seviye 2 = 11 kitap.)_
- [x] **F5.9 Kütüphane Gezgini ve PDF/Ses Oynatıcı:** Web ve Android'de sayfa sayısına ve seviyeye göre arama/filtreleme, PDF okuma ve ses dinleme arayüzü. _(Web: kapaklı kütüphane, arama/filtre, yan panel PDF. Android: kütüphane + PdfRenderer okuyucu.)_

---

### Faz 6 — İkili Çalışma Modu (Kelime Kelime vs Cümle Cümle)

**Amaç:** Kullanıcının seviyesine göre çalışma zorluğunu ayarlayabilmesi (Tam cümle veya kelime kelime).

- [x] **F6.1 Mod Durum Yönetimi:** `StudySession` içine `studyMode: 'sentence' | 'word'`, `currentWordIndex`, `submitWord`, `skipWord` desteği eklenmesi.
- [x] **F6.2 Kelime Kelime Arayüzü:** Kelimelerin sırayla yazıldığı, Boşluk/Enter ile anında doğrulandığı, ilk harf ipuçlu ve anti-cheat korumalı kelime modu arayüzü.
- [x] **F6.3 Mod Değiştirme Kısayolu ve Anahtarı:** Çalışma esnasında `Ctrl+M` veya arayüzden tek tıkla iki mod arasında kesintisiz geçiş.

---

### Faz 7 — Akıllı Türkçe Çeviri Sistemi

**Amaç:** İngilizce metin ve kelimelerin Türkçe karşılıklarına anında ve akıcı erişim.

- [x] **F7.1 Android ML Kit On-Device Çeviri:** `com.google.mlkit:translate` ile cihazda %100 çevrimdışı İngilizce → Türkçe cümle ve kelime çevirisi. _(`MlKitTranslator`, kelime kartında "Cümleyi cihazda çevir". Model ilk kullanımda indirilir.)_
- [x] **F7.2 Web Çevrimdışı Sözlük Entegrasyonu:** 50.000+ kelimelik optimize edilmiş hafif sözlük verisi ile kelimeye tıklandığında anında Türkçe anlam popup'ı. _(14.000+ madde: `tools/build_dictionary.py` → `lessons/dictionary.json`; çekim eki ve deyim tanıma. Açık lisanslı harici kaynak olmadığından 50.000 hedefine ulaşılmadı.)_
- [x] **F7.3 Web Dinamik Cümle Çeviricisi:** Kitap dışı serbest cümleler için hafif web çeviri köprüsü. _(Ders cümleleri için hazır çeviri; sözlükte olmayanlar için kullanıcı tıklamasıyla açılan çevrimiçi çeviri bağlantısı. Sunucu/API yok.)_
- [x] **F7.4 Kelime Bilgi Kartı:** Tıklanan kelimenin telaffuzu, Türkçe anlamı ve varsa Hata Defteri'ne "bilmiyorum" olarak ekleme butonu.

---

### Faz 8 — Yayın ve Paketleme

**Amaç:** Canlı GitHub Pages web sitesi ve indirilebilir Android APK.

- [x] **F8.1 GitHub Pages Otomasyonu:** GitHub Actions ile `Web/` derlemesini otomatik `gh-pages` dalına dağıtma. _(`.github/workflows/deploy-pages.yml`, `VITE_BASE`, LFS önbelleği.)_
- [x] **F8.2 Android Release İmzalı APK:** GitHub Actions ile otomatik sürüm APK'sı üretilmesi. _(`.github/workflows/android-release.yml`, R8 + ortam değişkeniyle imzalama.)_
- [x] **F8.3 Belgeler:** `README.md` (ekran görüntüleri, canlı demo linki, kısayol tablosu, kurulum).

---

## 6. Sonraya Bırakılanlar (v1 Kapsamı Dışı)

- Mikrofonla kullanıcının kendi sesini kaydedip orijinalle kıyaslaması.
- Otomatik telaffuz puanlama.
- Otomatik ses transkripsiyonu (Whisper vb.).
- Otomatik yapay zeka çevirisi.
- Bulut hesap ve cihazlar arası eşitleme.

---

## 7. Karar Günlüğü

| Tarih | Karar | Gerekçe |
|---|---|---|
| 2026-10-03 | Web (React/Vite/TS) + Android (Kotlin/C++) ayrımı | Hem GitHub Pages'de anında açılan web sürümü hem de Android'de tavizsiz yerel deneyim sağlamak için. |
| 2026-10-03 | Ortak `lessons/` klasörü | Ders verisinin ve şemasının her iki platformda ortak kullanılmasını sağlamak için. |
| 2026-10-03 | Web Audio API tercihi | Tarayıcıda harici kütüphane olmaksızın en hassas segment durdurma ve hız kontrolü sağlamak için. |
| 2026-10-04 | Kütüphane ana ekran + hash router (`#/study/<id>`) | Uzun `<select>` listesi yerine kapaklı kütüphane; yenilemede ders korunur, GitHub Pages alt yolunda çalışır (`import.meta.env.BASE_URL`). |
| 2026-10-04 | Ders ilerlemesi kalıcı (`ProgressStore`, Web: localStorage, Android: SharedPreferences) | 300-500 cümlelik kitaplarda her açılışta 1. cümleden başlamak kullanılamaz durumdaydı. |
| 2026-10-04 | Uzun derslerde PCM decode yok; Android APK'ya WAV girmez | 1 saatlik sesin AudioBuffer'a çözülmesi ~700 MB bellek; WAV'lar APK'yı 4 GB sınırının üstüne çıkarıyordu. |
| 2026-10-04 | Kitap üretimi 36 kitapta durduruldu | Kullanıcı kararı; F5.6-F5.8 açık kalır. |
| 2026-10-04 | Sözlük proje içeriğinden üretilir (14k madde) | Açık lisanslı 50k EN-TR sözlük kaynağı yok; çevrimdışı ilke korunur. Android'de ML Kit cihaz içi çeviri tamamlar. |
