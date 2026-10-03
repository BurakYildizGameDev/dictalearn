# DictaLearn — Yapılanlar Raporu (Tamamlanan Aşamalar)

Bu belge, **DictaLearn** (Açık Kaynak İngilizce Dikte & Shadowing Uygulaması) projesinde tamamlanan tüm fazları, mimari kararları, platform uygulamalarını ve teknik detayları özetlemektedir.

---

## 1. Mimari ve Teknoloji Özeti

Proje tek bir monorepo altında, iki bağımsız istemci ve ortak bir ders standardı ile yapılandırılmıştır:

```
├── Web/                     # React 19 + TypeScript + Vite 8 + Tailwind CSS v4 + Web Audio API
├── Android/                 # Kotlin + Jetpack Compose + C++ CMake/NDK + Oboe / MediaPlayer
├── lessons/                 # Platformlar arası taşınabilir ders paketleri (lesson.json schema v1 + audio)
├── PLAN.md                  # 9 fazlı master yol haritası
├── YAPILANLAR.md            # Tamamlanan işlerin detaylı dökümü
└── YAPILACAKLAR.md          # Gelecek fazların detaylı uygulama rehberi
```

---

## 2. Tamamlanan Fazlar ve Teknik Çıktılar

### ✅ Faz 0 — Temel ve İskelet (Web & Android)
- **Web İskeleti (`Web/`)**: Vite 8 + React 19 + TypeScript + Tailwind CSS v4 kurulumu, Vitest test ortamı ve Oxlint linter yapılandırması.
- **Android İskeleti (`Android/`)**: Gradle 8.14 + Android SDK 36 + Kotlin 2.0.21 + Jetpack Compose (Material3) + C++ NDK 28.2 (CMake 3.22.1) iskeleti.
- **Ortak Ders Paketi (`lessons/sample_ch01/`)**: Kamu malı ses dosyası (`audio.wav`) ve şema v1 uyumlu `lesson.json` hazırlandı.
- **CI / GitHub Actions (`.github/workflows/ci.yml`)**: PR ve master push'larında otomatik test ve lint kontrolü.

---

### ✅ Faz 1 — Web MVP (Çekirdek Döngü)
- **F1.1 Ders Yükleyici & Doğrulama (`lesson-validator.ts`, `lesson-loader.ts`)**:
  - Şema v1 kuralları (zorunlu alanlar, sıralı ve çakışmayan zaman aralıkları, pozitif milisaniyeler) saf TypeScript ile doğrulandı.
- **F1.2 Diff Motoru (`diff-engine.ts`)**:
  - Orijinal ve yazılan metni kelime bazında Levenshtein matrisi ile hizalayan, `equal`, `substitute`, `missing`, `extra` durumlarını ve %0-100 doğruluk skorunu hesaplayan motor.
- **F1.3 Web Ses Motoru (`web-audio-engine.ts`)**:
  - Web Audio API `AudioContext` ve `AudioBufferSourceNode` ile donanım saatinde mikrosaniye hassasiyetli `playRange(startMs, endMs)` ve hız yönetimi.
- **F1.4 Oturum Durum Makinesi (`use-study-session.ts`)**:
  - `dictating` ➔ `reviewing` ➔ `shadowing` ➔ `completed` durum akışları.
- **F1.5 & F1.6 Çalışma Arayüzü & Klavye Kısayolları (`StudySessionView.tsx`, `use-shortcuts.ts`)**:
  - **Anti-Cheat Kuralı**: Dikte sırasında orijinal metin ve çeviri DOM'da kesinlikle yer almaz.
  - Kısayollar: `Enter` (Kontrol), `Ctrl+Enter` (Pes Et/Atla), `Ctrl+Space` (Duraklat), `Ctrl+R` (Tekrar Dinle), `Ctrl+1/2/3` (0.75x, 1x, 1.25x hız).

---

### ✅ Faz 2 — Android MVP (Kotlin + C++)
- **F2.1 Android Veri Modelleri & Parser (`LessonModels.kt`, `LessonParser.kt`)**:
  - Kotlin veri sınıfları ve katı JSON doğrulama motoru.
- **F2.2 Android Diff Motoru (`DiffEngine.kt`, `DiffModels.kt`)**:
  - Levenshtein matris tabanlı kelime hizalama algoritması ve kapsamlı JUnit testleri.
- **F2.3 Android Ses Motoru (`AudioEngine.kt`, `MediaPlayerAudioEngine.kt`, `FakeAudioEngine.kt`)**:
  - Milisaniye hassasiyetli aralık çalma, hız kontrolü ve testler için sahte motor (mock).
- **F2.4 Jetpack Compose Arayüzü (`StudySessionScreen.kt`, `StudySessionViewModel.kt`, `DiffViewCompose.kt`)**:
  - StateFlow tabanlı reaktif durum yönetimi, dinamik diff renklendirme (`FlowRow`), klavye ve hız çipleri.
  - Native C++ JNI köprüsü (`native-lib.cpp`, CMake) entegre edildi.

---

### ✅ Faz 3 — Kullanıcı Deneyimi ve Hata Defteri (Her İki Platform)
- **F3.1 Düzeltme Akışı (`reviewing`)**:
  - Hata yapan kullanıcıya orijinal cümle gösterilir ve doğru halini yazması istenir.
  - Anlık düzeltme diff kontrolü; doğru yazıldığında otomatik olarak Shadowing moduna geçilir (`Ctrl+Enter` ile atlanabilir).
- **F3.2 Shadowing / Sesli Tekrar Modu (`shadowing`)**:
  - Cümleyi konuşmacıyla eş zamanlı veya hemen ardından sesli tekrar etme alanı.
  - **Çeviri Aç/Kapa (`Ctrl+T`)**: Varsayılan olarak kapalı tutularak tam odaklanma sağlanır, tek tıkla açılıp kapanabilir.
- **F3.3 Hata Defteri Deposu (`LocalMistakeRepository`, `InMemoryMistakeRepository`)**:
  - İlk denemede yapılan kelime hataları (`substitute`, `missing`) otomatik olarak yerel hafızaya kaydedilir ve frekans analizi yapılır.
- **F3.4 Ders Sonu Özeti Ekranı**:
  - Ortalama doğruluk, kusursuz cümle adedi, toplam tekrar sayısı ve derste en çok hata yapılan kelimelerin rozetlerle listelenmesi.
- **F3.5 Hız Kontrolü ve Kalıcılık**:
  - `0.75x`, `1.0x`, `1.25x` hız seçenekleri Web'de `localStorage`'da kalıcı hale getirildi.

---

### ✅ Faz 4 — Ders Oluşturucu & Dışa Aktarma
- **F4.1 Altyazı Ayrıştırıcıları (`subtitle-parser.ts`, `SubtitleParser.kt`)**:
  - SRT (`00:01:23,456`) ve WebVTT (`00:01:23.456` / `01:23.456`) zaman damgalarını milisaniyeye dönüştüren, HTML/styling etiketlerini temizleyen saf ayrıştırıcı.
  - Otomatik format tanıma (`parseSubtitles`).
- **F4.2 Zip Paketi Alışverişi (`lesson-package.ts`, `LessonPackageManager.kt`)**:
  - Web'de `JSZip`, Android'de `java.util.zip` ile `lesson.json` ve ses dosyasını `.zip` olarak dışa aktarma (download) ve içe aktarma (unzip + validate + URL/Blob oluşturma).
  - Gidiş-dönüş (roundtrip) testleri ile doğrulandı.
- **F4.3 Segment Düzenleyici Arayüzü (`LessonEditorView.tsx`, `LessonEditorScreen.kt`)**:
  - Başlık, Ders ID, ses yükleme, SRT/VTT yükleme, segment ekleme/silme, zaman aralığı düzenleme, **"Test Et"** ile segment sesini dinleme, İngilizce metin ve Türkçe çeviri girişi.
  - "Dersi Başlat" ile anında çalışma moduna aktarma.

### ✅ Faz 5.5 — 25 Kitaplık Seviye 1 (15 Sayfalık) Kademeli Okuma & Dikte Kütüphanesi (%100 Tamamlandı)
- **Kapsam ve Üretim Standartları**:
  - **25 Kitap**: Dünya klasiklerinin CEFR A2-B1 seviyesine uyarlanmış eksiksiz 15'er bölümlük metinleri.
  - **Tam 15 Sayfa x 20 Cümle = 300 Cümle / Kitap**: Kesintisiz 1..300 ID'li toplam **7.500 Cümle**.
  - **Sayfa Başına 8 Hedef Terim = 120 Terim / Kitap**: Toplam **3.000 Hedef Kelime ve Dilbilgisi Notu**.
  - **Milisaniye Senkron Stüdyo Seslendirmesi (Microsoft Edge Neural TTS)**: `en-US-ChristopherNeural` anlatıcı sesiyle, 400ms cümle arası ve 1000ms sayfa sonu duraklamalı, toplam **13 Saat 2 Dakika** süren stüdyo kaydı. Hem **16-bit 24kHz PCM WAV** hem de yüksek kaliteli **MP3** formatlarında üretildi.
  - **16 Sayfalık Profesyonel ReportLab PDF Kitapları**: 1 Kapak + 15 Hikaye Sayfası, taşma yapmayan iki sütunlu (Sol İngilizce, Sağ Türkçe paralel metin) dizgi, alt 8 terimli kelime tahlil kutusu ve `NumberedCanvas` üst/alt bilgi alanı ile toplam **400 Sayfa PDF**.
  - **Çift Yönlü Tam Senkronizasyon**: 25 kitabın tamamı hem `Web/public/lessons/` hem de `Android/app/src/main/assets/lessons/` dizinlerine kopyalandı.
  - **Web Uygulama Entegrasyonu**: `Web/src/App.tsx` içindeki `PRESET_LESSONS` menüsüne 1'den 25'e kadar tüm kitaplar eklendi; Vitest test paketinde tüm 63 test başarıyla geçti.

#### 📚 25 Kitaplık Koleksiyon Envanteri:
| # | Kitap Başlığı ve Kimliği | Yazar / Eser | Cümle | Ses Süresi | PDF | Senkronizasyon |
|---|---|---|:---:|:---:|:---:|:---:|
| 1 | `book_01_the_happy_prince` | Oscar Wilde | 300 | 28.0 dk | 16 syf | ✅ Web & Android |
| 2 | `book_02_the_selfish_giant` | Oscar Wilde | 300 | 27.8 dk | 16 syf | ✅ Web & Android |
| 3 | `book_03_the_nightingale_and_the_rose` | Oscar Wilde | 300 | 28.7 dk | 16 syf | ✅ Web & Android |
| 4 | `book_04_the_devoted_friend` | Oscar Wilde | 300 | 29.4 dk | 16 syf | ✅ Web & Android |
| 5 | `book_05_the_remarkable_rocket` | Oscar Wilde | 300 | 32.8 dk | 16 syf | ✅ Web & Android |
| 6 | `book_06_aesops_fables_part1` | Aesop (Ezop Masalları - 1) | 300 | 31.3 dk | 16 syf | ✅ Web & Android |
| 7 | `book_07_aesops_fables_part2` | Aesop (Ezop Masalları - 2) | 300 | 31.6 dk | 16 syf | ✅ Web & Android |
| 8 | `book_08_the_little_prince` | Antoine de Saint-Exupéry | 300 | 32.1 dk | 16 syf | ✅ Web & Android |
| 9 | `book_09_grimms_fairy_tales` | Brothers Grimm (Grimm Kardeşler) | 300 | 35.1 dk | 16 syf | ✅ Web & Android |
| 10 | `book_10_hans_christian_andersen` | Hans Christian Andersen | 300 | 35.6 dk | 16 syf | ✅ Web & Android |
| 11 | `book_11_alices_adventures_in_wonderland` | Lewis Carroll (Alice) | 300 | 35.9 dk | 16 syf | ✅ Web & Android |
| 12 | `book_12_the_adventures_of_pinocchio` | Carlo Collodi (Pinokyo) | 300 | 37.0 dk | 16 syf | ✅ Web & Android |
| 13 | `book_13_the_wonderful_wizard_of_oz` | L. Frank Baum (Oz Büyücüsü) | 300 | 36.1 dk | 16 syf | ✅ Web & Android |
| 14 | `book_14_the_jungle_book` | Rudyard Kipling (Orman Çocuğu) | 300 | 25.2 dk | 16 syf | ✅ Web & Android |
| 15 | `book_15_the_wind_in_the_willows` | Kenneth Grahame (Söğütlükte Rüzgar) | 300 | 27.7 dk | 16 syf | ✅ Web & Android |
| 16 | `book_16_peter_pan` | J. M. Barrie (Peter Pan) | 300 | 27.2 dk | 16 syf | ✅ Web & Android |
| 17 | `book_17_the_merry_adventures_of_robin_hood` | Howard Pyle (Robin Hood) | 300 | 29.1 dk | 16 syf | ✅ Web & Android |
| 18 | `book_18_king_arthur` | Kral Arthur Efsanesi | 300 | 29.5 dk | 16 syf | ✅ Web & Android |
| 19 | `book_19_gullivers_travels` | Jonathan Swift (Gulliver) | 300 | 29.9 dk | 16 syf | ✅ Web & Android |
| 20 | `book_20_treasure_island` | Robert Louis Stevenson (Define Adası) | 300 | 29.2 dk | 16 syf | ✅ Web & Android |
| 21 | `book_21_around_the_world_in_eighty_days` | Jules Verne (80 Günde Devriâlem) | 300 | 32.3 dk | 16 syf | ✅ Web & Android |
| 22 | `book_22_a_christmas_carol` | Charles Dickens (Noel Şarkısı) | 300 | 34.1 dk | 16 syf | ✅ Web & Android |
| 23 | `book_23_the_secret_garden` | Frances Hodgson Burnett (Gizli Bahçe) | 300 | 32.4 dk | 16 syf | ✅ Web & Android |
| 24 | `book_24_white_fang` | Jack London (Beyaz Diş) | 300 | 32.5 dk | 16 syf | ✅ Web & Android |
| 25 | `book_25_the_time_machine` | H. G. Wells (Zaman Makinesi) | 300 | 30.4 dk | 16 syf | ✅ Web & Android |
| **Σ** | **GENEL TOPLAM (25 KİTAP)** | **DÜNYA KLASİKLERİ KÜTÜPHANESİ** | **7.500** | **13.02 Saat** | **400 syf** | **TAMAMI HAZIR** |

---

## 3. Test ve Kalite Durumu

| Platform | Test Aracı | Test Sayısı | Başarı Oranı | Linter Durumu | Derleme (Build) |
|---|---|---|---|---|---|
| **Web** | Vitest 5 + JSDOM | **63 test** | **%100 PASS** | 0 warning, 0 error (Oxlint) | 336 ms (Vite Production Bundle) |
| **Android** | JUnit 4 + Gradle | **Tüm birim testleri** | **%100 PASS** | 0 blocker error | Debug APK üretildi (`app-debug.apk`) |

---

## 4. Git Commit Geçmişi (Seçkin Kilometre Taşları)

```text
cf6552b feat(book_25): complete 15-page 300-sentence edition of The Time Machine with studio audio, PDF, and app sync
9ffd771 feat(book_24): complete 15-page 300-sentence edition of White Fang with studio audio, PDF, and app sync
68a49be feat(book_23): complete 15-page 300-sentence edition of The Secret Garden with studio audio, PDF, and app sync
010a7b0 feat(book_22): complete 15-page 300-sentence edition of A Christmas Carol with studio audio, PDF, and app sync
99c0fd7 feat(book_21): complete 15-page 300-sentence edition of Around the World in Eighty Days with studio audio, PDF, and app sync
7e33696 feat(book_20): complete 15-page 300-sentence edition of Treasure Island with studio audio, PDF, and app sync
d292845 feat(book_19): complete 15-page 300-sentence edition of Gulliver's Travels with studio audio, PDF, and app sync
f387f7c feat(book_18): complete 15-page 300-sentence edition of King Arthur with studio audio, PDF, and app sync
26ba462 feat(book_17): complete 15-page 300-sentence edition of Robin Hood with studio audio, PDF, and app sync
21735ab feat(book_16): complete 15-page 300-sentence edition of Peter Pan with studio audio, PDF, and app sync
39f5066 feat(book_15): complete 15-page 300-sentence edition of The Wind in the Willows with studio audio, PDF, and app sync
da653e4 feat(book_14): complete 15-page 300-sentence edition of The Jungle Book with studio audio, PDF, and app sync
4019655 feat(book_13): complete 15-page 300-sentence edition of The Wonderful Wizard of Oz with studio audio, PDF, and app sync
aa8809c feat(book_12): complete 15-page 300-sentence edition of The Adventures of Pinocchio with studio audio, PDF, and app sync
ddf26b6 feat(book_11): complete 15-page 300-sentence edition of Alice in Wonderland with studio audio, PDF, and app sync
9643064 feat(book_10): complete 15-page 300-sentence edition of Hans Christian Andersen Tales of Wonder with studio audio, PDF, and app sync
e321194 feat(book_09): complete 15-page 300-sentence edition of Grimm's Fairy Tales with studio audio, PDF, and app sync
073039d feat(book_08): complete 15-page 300-sentence edition of The Little Prince with studio audio, PDF, and app sync
5778781 feat(book_07): complete 15-page 300-sentence edition of Aesop's Fables Part 2 with studio audio, PDF, and app sync
8930f11 feat(book_06): complete 15-page 300-sentence edition of Aesop's Fables Part 1 with studio audio, PDF, and app sync
7db1e22 feat(book_05): complete 15-page 300-sentence edition of The Remarkable Rocket with studio audio, PDF, and app sync
ca3651e feat(book_04): complete 15-page 300-sentence edition of The Devoted Friend with studio audio, PDF, and app sync
ca9597a feat(faz5): add Book 3 (The Nightingale and the Rose) with 15 pages x 20 sentences (300 total sentences)
429c6fb feat(faz5): add Book 2 (The Selfish Giant) with 15 pages x 20 sentences (300 total sentences)
4619cd7 feat(faz5): upgrade Book 1 (The Happy Prince) to 15 pages with 20 sentences per page (300 total sentences)
d6dc947 docs: mark Phase 4 completed in PLAN.md
a035e61 feat: implement lesson creator and editor UI for Web and Android (F4.3)
3be8467 feat: implement zip package import and export with unit tests (F4.2)
0419469 feat: implement SRT and WebVTT subtitle parsers with unit tests (F4.1)
cf1495d docs: mark Phase 3 completed in PLAN.md
120abef feat(android): implement correction flow, shadowing mode, and summary screen (F3.1, F3.2, F3.4, F3.5)
17eb37b feat(android): implement mistake repository and unit tests (F3.3)
2c84afd feat(web): implement full 4-step study session with correction, shadowing, and summary (F3.1, F3.2, F3.4, F3.5)
3e7b3db feat(web): implement mistake repository and error tracking domain (F3.3)
a2508dd feat(android): implement Jetpack Compose UI, ViewModel and MainActivity integration (F2.4)
b418b05 feat(android): implement MediaPlayerAudioEngine and FakeAudioEngine with unit tests (F2.3)
b234d99 feat(android): implement Levenshtein word diff engine with unit tests (F2.2)
378d9b4 feat(android): implement lesson models and JSON parser with unit tests (F2.1)
80ffa0d feat(web): implement study session UI, state machine and shortcuts (F1.4-F1.6)
336ad51 feat(web): implement WebAudioEngine with millisecond playRange precision (F1.3)
2397c88 feat(web): implement Levenshtein word diff engine with 100% test coverage (F1.2)
76ba18d feat(web): implement lesson schema validator and loader (F1.1)
d9735d4 chore(ci): add GitHub Actions workflow for Web test and build (F0.5)
2bc8434 feat(sample): add public-domain sample lesson and audio (F0.3, F0.4)
b85a3fa feat(android): setup C++ CMake NDK native library scaffold (F0.2)
cf2d733 feat(android): scaffold Android project with Gradle and Compose (F0.2)
79bb955 feat(web): scaffold Vite React TypeScript Tailwind app (F0.1)
9ff76f1 docs: initialize DictaLearn master specification and roadmap
```

