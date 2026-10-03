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

---

## 3. Test ve Kalite Durumu

| Platform | Test Aracı | Test Sayısı | Başarı Oranı | Linter Durumu | Derleme (Build) |
|---|---|---|---|---|---|
| **Web** | Vitest 5 + JSDOM | **63 test** | **%100 PASS** | 0 warning, 0 error (Oxlint) | 336 ms (Vite Production Bundle) |
| **Android** | JUnit 4 + Gradle | **Tüm birim testleri** | **%100 PASS** | 0 blocker error | Debug APK üretildi (`app-debug.apk`) |

---

## 4. Git Commit Geçmişi (23 Atomik Commit)

```text
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
