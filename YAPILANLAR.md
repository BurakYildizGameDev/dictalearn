# DictaLearn — Yapılanlar Raporu (Tamamlanan Aşamalar)

Bu belge, **DictaLearn** (Açık Kaynak İngilizce Dikte & Shadowing Uygulaması) projesinde tamamlanan tüm fazları, mimari kararları, platform uygulamalarını ve teknik detayları özetlemektedir.

---

## 1. Mimari ve Teknoloji Özeti

Proje tek bir monorepo altında, iki bağımsız istemci ve ortak bir ders standardı ile yapılandırılmıştır:

```
├── Web/                     # React 19 + TypeScript + Vite 8 + Tailwind CSS v4 + Web Audio API
├── Android/                 # Kotlin + Jetpack Compose + C++ CMake/NDK + Oboe / MediaPlayer
├── lessons/                 # Ortak ders paketleri (lesson.json + audio.mp3 + PDF) ve dictionary.json
├── tools/                   # TTS/PDF üretim hattı, sözlük üretici, e2e test script'leri
├── docs/screenshots/        # README görselleri
├── README.md                # Proje vitrini ve kurulum
├── PLAN.md                  # Fazlı master yol haritası ve karar günlüğü
├── YAPILANLAR.md            # Tamamlanan işlerin detaylı dökümü (bu dosya)
└── YAPILACAKLAR.md          # Fazların uygulama rehberi
```

> **Son durum (2026-10-04):** Kitap üretimi dışındaki tüm fazlar tamamlandı. 36 kitap · 13.000 cümle ·
> ~23 saat ses · 14.067 maddelik sözlük. Web 128 + Android 66 birim testi, 16 + 13 uçtan uca kontrol geçiyor.

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
  - _(2026-10-04 güncellemesi: uzun kitaplar için `HTMLAudioElement` + konum takibine geçildi, bkz. Stabilizasyon bölümü.)_
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
  - **Web Uygulama Entegrasyonu**: Kitaplar başlangıçta `PRESET_LESSONS` açılır menüsüne eklendi; 2026-10-04'te yerini kapaklı kütüphane ve `catalog.ts` aldı.

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

### ✅ Faz 5.6 — Seviye 2 Kütüphanesi: 11 Kitap x 25 Sayfa (CEFR B1 Klasikler)

Her kitap: **25 sayfa × 20 cümle = 500 cümle**, 26 sayfalık PDF, 200 hedef kelime, nöral TTS sesi.

| # | Kitap | Yazar | Cümle | Ses | MP3 |
|---|---|---|:---:|:---:|:---:|
| 26 | A Scandal in Bohemia | Arthur Conan Doyle | 500 | 50.9 dk | 18.3 MB |
| 27 | The Red-Headed League | Arthur Conan Doyle | 500 | 54.0 dk | 19.5 MB |
| 28 | The Hound of the Baskervilles | Arthur Conan Doyle | 500 | 52.4 dk | 18.9 MB |
| 29 | The Gift of the Magi & The Last Leaf | O. Henry | 500 | 51.7 dk | 18.6 MB |
| 30 | The Call of the Wild | Jack London | 500 | 53.3 dk | 19.2 MB |
| 31 | Frankenstein | Mary Shelley | 500 | 57.6 dk | 20.7 MB |
| 32 | Dracula | Bram Stoker | 500 | 60.0 dk | 21.6 MB |
| 33 | Dr. Jekyll and Mr. Hyde | Robert Louis Stevenson | 500 | 57.6 dk | 20.7 MB |
| 34 | The Picture of Dorian Gray | Oscar Wilde | 500 | 59.4 dk | 21.4 MB |
| 35 | The Canterville Ghost | Oscar Wilde | 500 | 57.2 dk | 20.6 MB |
| 36 | Journey to the Center of the Earth | Jules Verne | 500 | 56.8 dk | 20.4 MB |
| **Σ** | **11 kitap** | | **5.500** | **~10.2 saat** | **~220 MB** |

> Bu kitapların `audio.mp3` dosyaları ilk üretimde aslında yeniden adlandırılmış WAV verisiydi (kitap başına
> 150–170 MB). `tools/fix_mp3_encoding.py` ile 48 kbps CBR mono MP3'e dönüştürüldü (~1.8 GB → ~220 MB).
> Plandaki 25 kitaplık Seviye 2 hedefi, Seviye 3 ve Seviye 4 kullanıcı kararıyla durduruldu.

---

### ✅ Faz 6 — İkili Çalışma Modu: Kelime Kelime & Cümle Cümle Dikte (F6.1 - F6.3)
- **F6.1 Kelime Ayrıştırma ve Tolerans Motoru (`word-mode.ts`)**:
  - `tokenizeSentenceToWords`: Cümleleri kelime jetonlarına (`WordToken`) ayıran; büyük/küçük harf, noktalama işaretleri ve kesme işaretlerini (`didn't`, `o'clock`) tolere edebilen fonksiyonlar.
  - `checkWordMatch`: Kullanıcının yazdığı kelimeyi hedef kelimeyle esnek ve doğru karşılaştıran algoritma.
- **F6.2 İkili Mod Durum Yönetimi (`use-study-session.ts`)**:
  - `studyMode: 'sentence' | 'word'` durumu, `localStorage` üzerinde kalıcılık.
  - `currentWordIndex`, `typedWord`, `wordFeedback`, `wordMistakeCount` durumları.
  - `submitWord`: Kelime doğruysa yeşil geri bildirimle sıradaki kelimeye geçiş; cümlenin son kelimesi bittiğinde otomatik `shadowing` moduna ilerleme.
  - `skipWord`: Kelimeyi atlayıp doğru halini görme ve hata defterine kaydetme.
- **F6.3 Etkileşimli Arayüz ve Klavye Desteği (`StudySessionView.tsx`)**:
  - Üst gezinme çubuğunda tek tıkla veya `Ctrl+M` kısayoluyla mod değiştirme anahtarı.
  - **Dinamik Kelime Yuvaları**: Bilinen kelimeler yeşil rozetle açılır, sıradaki kelime vurgulanır, henüz gelinmemiş kelimeler kopya çekilmemesi için `••••` şeklinde gizlenir (Anti-cheat).
  - **Işık Hızında Dikte**: Kelime yazılıp **Boşluk** veya **Enter** tuşuna basıldığında anında kontrol edilir; doğruysa input temizlenip sıradaki kelimeye odaklanır.
  - **İpucu Sistemi**: Yanlış yazımda kırmızı uyarı, ilk harf ve harf sayısı ipucu.
  - Kısayollar penceresine `Ctrl+M` ve `Boşluk/Enter` eklendi.

---

### ✅ Faz 6.5 — Mobil Dokunmatik Kontroller & Kelime Kelime Sesli Okuma (F6.4 - F6.7)
- **F6.4 Web Speech API Entegrasyonu (`speech-tts.ts`)**:
  - `window.speechSynthesis` kullanarak sıfır gecikme ile herhangi bir İngilizce kelimeyi sesli olarak telaffuz eden `WordSpeechEngine`.
  - Otomatik okuma (`autoSpeakWord`): Her kelimeye geçildiğinde otomatik telaffuz, Açık/Kapalı geçiş düğmesiyle kontrol.
  - `speakCurrentWord()`, `speakWord(word)`: Aktif kelimeyi veya belirli bir kelimeyi seslendir.
- **F6.5 Harf İpucu Algoritması (`giveLetterHint`)**:
  - Kullanıcı doğru kelimeyi bilemediğinde her basışta bir sonraki harfi doldurarak kademeli ipucu.
  - Örnek: Hedef "every" → 1. ipucu "e", 2. ipucu "ev", 3. ipucu "eve"...
- **F6.6 Ekran Üstü Mobil Dokunmatik Aksiyonlar (Web & Android)**:
  - Tüm klavye kısayolları ekran üstü butonlara taşındı (min 44-48dp dokunma alanı, `active:scale-95` geri bildirim).
  - **Cümle Modu**: 🔊 Dinle (Ctrl+R), ❓ Bilmiyorum / Göster, ✅ Kontrol Et (Enter).
  - **Kelime Modu**: ✅ Kontrol Et, 💡 Harf İpucu Al, 🔊 Kelimeyi Oku, ⏭️ Bu Kelimeyi Atla, 👁️ Tüm Cümleyi Göster.
  - Kelime kartları: Bilinen kelimeler tıklanabilir (🔊 dokunarak dinle), aktif kelime slot'u tıklanabilir (seslendir).
  - **Otomatik Okuma Geçişi**: "Oto-Oku: Açık/Kapalı" butonu ile her kelimeye geçişte otomatik telaffuz.
  - **Cümleyi Dinle**: Üst kontrol çubuğunda cümlenin tamamını audio engine ile dinleme butonu.
  - Input alanlara `inputMode="text"`, `enterKeyHint="go"/"done"` eklenerek mobil sanal klavye deneyimi optimize edildi.
- **F6.7 Android Kelime Modu & TextToSpeech (Jetpack Compose)**:
  - `WordModels.kt`: `WordModeEngine` ile cümle tokenizasyonu, kelime temizleme ve karşılaştırma.
  - `SpeechEngine.kt`: Android `android.speech.tts.TextToSpeech` ile kelime kelime sesli okuma interface'i.
  - `AndroidSpeechEngine.kt`: Locale.US, 0.95x konuşma hızı ile gerçek TTS implementasyonu.
  - `StudySessionViewModel.kt`: `StudyMode.SENTENCE / WORD`, `targetWords`, `currentWordIndex`, `typedWord`, `wordFeedback`, `autoSpeakWord`, `speakCurrentWord()`, `speakWord()`, `giveLetterHint()`, `submitWord()`, `skipWord()`.
  - `StudySessionScreen.kt`: Compose UI'da mod seçici chip'ler, `FlowRow` kelime slot'ları (geçmiş kelime dokunulunca seslendir, aktif kelime slot'u dokunulunca seslendir, gelecek kelimeler maskeli), 48dp dokunmatik aksiyon butonları (Kontrol, Harf İpucu, Oku), ikincil aksiyonlar (Kelimeyi Atla, Tüm Cümleyi Göster).
  - `WordModeTest.kt`: Tokenizasyon, temizleme ve kelime karşılaştırma JUnit testleri.
  - `StudySessionViewModelTest.kt`: Kelime modu akışı, harf ipucu, kelime atlama ve SpeechEngine entegrasyon testi.

---

### ✅ Stabilizasyon ve Hata Düzeltmeleri (2026-10-04)

**Web**
- **Ses motoru (`web-audio-engine.ts`)**:
  - 1 saatlik kitapların ~700 MB PCM'e çözülmesi kaldırıldı; `HTMLAudioElement` + 15 ms konum takibiyle `end_ms`'de durma.
  - Hız düşürülünce cümlenin erken kesilmesi düzeltildi.
  - Gerçek duraklat/devam eklendi (`Ctrl+Space`).
  - Eski yüklemelerin ve kesintiye uğrayan `play()` çağrılarının yarışları load/play token'larıyla engellendi.
  - Tarayıcı otomatik oynatmayı engellerse kullanıcıya uyarı gösteriliyor (`blocked` durumu).
- **Oturum (`use-study-session.ts`)**:
  - "Cevabı göster" artık kaydı iki kez eklemiyor.
  - Kelime modunda aynı kelimedeki tekrar denemeler tek hata sayılıyor; doğruluk gerçek değerle hesaplanıyor.
  - İlk kelimenin TTS'i otomatik çalan cümle sesinin üstüne binmiyor.
  - `goToSegment` / `previousSegment` / `skipSegment` / `restart` eklendi. "Dersi tekrar başlat" artık sayfayı yenileyip başka kitaba atmıyor.
- **Kısayollar:** PLAN §4.2'deki eksikler (`PageUp`/`PageDown`, `F1`, odak dışı `Enter`, `Esc`) eklendi. Dinleyicinin her render'da yeniden bağlanması düzeltildi.
- **PDF yükleme:**
  - MIME tipi boş gelen `.pdf` dosyaları (Windows'ta PDF okuyucu kurulu değilse) artık reddedilmiyor.
  - Aynı dosya tekrar yüklenince IndexedDB'de kopya birikmiyor; eski `active_pdf` kaydı temizlendi.
  - Sayfa içi PDF görüntüleyicisi olmayan tarayıcılarda (Android Chrome) "Aç / İndir" yedek görünümü var.
- **Kalıcı ilerleme (`ProgressStore`):** 300–500 cümlelik kitaplar artık her açılışta 1. cümleden başlamıyor.

**Android**
- **Kütüphane:** Uygulama yalnızca 6 cümlelik demoyu açabiliyordu; 36 kitabın hiçbiri erişilebilir değildi. Kütüphane ekranı eklendi.
- **APK boyutu:** Assets 5.7 GB'tı ve APK'nın 4 GB sınırını aşıyordu. WAV'lar `ignoreAssetsPattern` ile APK'dan çıkarıldı.
- **`MediaPlayerAudioEngine`:**
  - Hız `start()`'tan önce uygulandığı için hiç etki etmiyordu, düzeltildi.
  - `SEEK_CLOSEST` ile hassas başlangıç.
  - Asenkron `prepareAsync`; ana thread bloke olmuyor.
  - Gecikme tabanlı kesme yerine konum takibi.
  - Seek sırasında duraklatma düzgün çalışıyor.
- **ViewModel:**
  - Kelime atlamada sabit `0.8` doğruluk kaldırıldı.
  - `giveUp` sadece dikte durumunda çalışıyor.
  - Gezinme, devam ve yeniden başlatma eklendi.
- **Kalıcılık:** Hata defteri `SharedPreferences`'ta kalıcı (eskiden bellekte tutuluyor, uygulama kapanınca siliniyordu); ilerleme ve ayarlar da kalıcı.
- **Tema:** Açık tema yerine koyu Material 3 tema. Edge-to-edge sayesinde klavye açıkken ayar çubuğu gizleniyor.

---

### ✅ Faz 5.9 — Kütüphane Gezgini ve PDF / Ses Oynatıcı
- **Web (`LibraryView.tsx`, `catalog.ts`):**
  - Kapaklı kitap kartları, seviye sekmeleri, Türkçe karakter duyarsız arama.
  - Kitap başına ilerleme çubuğu ve "Kaldığın yerden devam et" kartı.
  - Hash router (`#/study/<id>`): yenilemede ders korunur, geri tuşu çalışır.
- **Web PDF:**
  - Geniş ekranda yan panel (split view), dar ekranda modal.
  - Kullanıcı PDF'leri IndexedDB'de saklanır, listelenir ve silinebilir.
- **Android:**
  - `LibraryScreen` (adaptif grid, arama, seviye chip'leri).
  - `PdfReaderScreen`: platformun `PdfRenderer`'ı ile sayfa sayfa render; harici kütüphane yok.

### ✅ Faz 7 — Akıllı Türkçe Çeviri Sistemi
- **F7.2 Çevrimdışı sözlük (`tools/build_dictionary.py` → `lessons/dictionary.json`, 14.067 madde, 510 KB):**
  - Elle yazılmış ~500 kelimelik çekirdek liste (`tools/core_vocabulary.py`).
  - 36 kitabın `vocab_focus` listeleri.
  - Ders notlarındaki "kelime: anlam" açıklamaları.
  - Tamamen projenin kendi açık içeriğinden üretildi. Açık lisanslı harici kaynak olmadığından planlanan 50.000 maddeye ulaşılmadı.
- **Sözlük motoru (`dictionary.ts`, `Dictionary.kt`, aynı algoritma):**
  - Çekim eki çözümleme (*packed → pack*, *stories → story*, *stopped → stop*).
  - ~110 düzensiz form (*stood → stand*, *went → go*).
  - Cümle içinde 4 kelimeye kadar deyim eşleştirme (*drift apart*).
- **F7.4 Kelime kartı:**
  - Cevap gönderildikten sonra cümledeki her kelime tıklanabilir. Kopya koruması korunur: dikte sırasında DOM'da yok.
  - Kart içeriği: anlam, TTS telaffuz, "Bilmiyorum, deftere ekle" (`kind: 'unknown'`).
  - Sözlükte bulunmayan kelimeler için kullanıcı tıklamasıyla açılan çevrimiçi çeviri bağlantısı (F7.3).
- **F7.1 Android ML Kit (`MlKitTranslator.kt`):** Kelime kartında "Cümleyi cihazda çevir". EN→TR modeli ilk kullanımda indirilir, sonra internetsiz çalışır.
- **Defterim (web `#/notebook`, Android `NotebookScreen`):** Hata ve bilinmeyen kelimeler sıklık ve anlamlarıyla listelenir; filtrelenip temizlenebilir.

### ✅ Faz 8 — Yayın ve Paketleme
- **F8.1 `deploy-pages.yml`:**
  - `VITE_BASE=/<repo>/` ile derleme ve GitHub Pages'e yayın.
  - Sadece web kopyası için LFS çekilir; LFS nesneleri önbelleğe alınır.
  - Vite eklentisi WAV ve `.md` dosyalarını `dist/`'ten çıkarır (5.7 GB → 529 MB).
  - Kişisel dersler production derlemesinde listelenmez.
- **F8.2 `android-release.yml`:**
  - `v*` etiketinde test + `assembleRelease` çalışır, APK GitHub Release'e eklenir.
  - Release derlemesinde R8 minify ve resource shrinking açık.
  - İmzalama ortam değişkenleri ve repository secret'larıyla yapılır.
- **CI (`ci.yml`):** Web lint/test/build Node 22'ye taşındı (Vite 8 gereği); Android birim testleri eklendi.
- **F8.3 README:** Rozetler, ekran görüntüleri, çalışma döngüsü ve mimari diyagramları, kısayol tablosu, kurulum, testler, yayınlama.

### ✅ Faz 9 — Modern Arayüz
- **F9.1 Kütüphane:** web ve Android.
- **F9.2 Split view:** PDF ve dikte yan yana.
- **F9.3 Tasarım sistemi:**
  - Zinc/indigo palet, serif okuma tipografisi.
  - Ortak `Button` / `Segmented` / `ProgressBar` / `Kbd` bileşenleri.
  - Ses çalarken ekolayzır göstergesi; `prefers-reduced-motion` desteği.
- **F9.4 Ayar dock'u:**
  - Mod, hız, otomatik çal, PDF ve kısayollar tek çubukta.
  - Önceden 3 kez tekrarlanan "Dinle" ve PDF butonları teke indirildi.
- **F9.5 Mobil:** 390 px'de yatay taşma yok; Android'de klavye açılınca ayar çubuğu gizlenir.

### ✅ Kendi PDF'inden Dikte Dersi ve OCR (2026-10-04)
- **Kelime telaffuzu:** Türkçe Windows'ta tarayıcılar yalnızca "Microsoft Tolga (tr-TR)" sesini sunduğu için
  İngilizce kelimeler Türkçe okunuyordu. Bunun yerine stüdyo sesli kelime paketi geldi:
  - `tools/build_word_audio.py`: 15.155 kelime, en-US-ChristopherNeural, 26 harf dosyası, 55 MB.
  - Web ve Android bu paketi kullanır; sistem sesi yalnızca yedektir ve asla İngilizce dışı bir ses seçilmez.
- **PDF → ders:** Yüklenen PDF'in "Dikte" eylemiyle dersi oluşturulur.
  - Cümle ayıklama numaralı paralel metni (`[n]`), başlıkları ve Türkçe metni ayırt eder.
  - Dil tespiti İngilizce işlev kelimesi oranına dayanır; OCR Türkçe harfleri bozsa da çalışır.
- **OCR:** Metin katmanı olmayan sayfalar okunur.
  - Web: pdf.js ile render + Tesseract.js (`public/ocr`, çevrimdışı).
  - Android: `PdfRenderer` + ML Kit metin tanıma.
  - Sütun düzeni: sağ sütun başlangıcı sayfa bazında öğrenilir; OCR'ın bozduğu numaralar ("[s]", "(2]", "[8j") tanınır.
- **İlerlemeli ders:** İlk 25 sayfa okununca ders açılır, kalan sayfalar arka planda devam eder.
  - Yeni cümleler yalnızca sona eklenir, kayıtlı ilerleme bozulmaz.
  - Sayfalar önbelleğe alınır (web: IndexedDB, Android: dosya).
- **Ölçüm (42 sayfalık taranmış test PDF'i):**

  | | İlk 25 sayfa | Ders açıldı | Tüm PDF | Tekrar açılış |
  |---|---|---|---|---|
  | Web | ~97 sn | 451 cümle | 787 cümle | anında |
  | Android | ~51 sn | 461 cümle | 773 cümle | — |

  Beklenen değerler: ~460 ve ~800 cümle.
- **Android PDF ekleme:** Sistem dosya seçicisiyle PDF eklenir. Kütüphanede "Yüklediğin PDF'ler" bölümünde Dikte / Oku / Sil var; cümleler TTS ile okunur.

### ✅ Kelime Bazlı Çeviri (2026-10-04)
- Kelime modunda doğru yazılan her kelimenin altında kısa Türkçe anlamı görünür; cümle anlamıyla birlikte adım adım tamamlanır.
  Web (`StudySessionView`) ve Android (`WordDictation`) aynı davranır.
- `Dictionary.glossForSolvedWord`: yalnızca çözülmüş kelimeler kullanılır. Böylece sıradaki kelimenin anlamı ipucu olmaz;
  deyimler ("high above", "drift apart") tüm kelimeleri çözülünce ilk kelimenin altında görünür.
- `shortGloss`: ilk anlam, en fazla 22 karakter ("toplamak, paketlemek" → "toplamak").
- "Anlamlar: Açık/Kapalı" düğmesi (web'de kalıcı).

### ✅ Defterim için Aralıklı Tekrar (2026-10-04)
- **`SrsStore`** (web: `domain/review/srs.ts`, Android: `domain/review/SrsStore.kt`, aynı algoritma): Leitner kutuları.
  - Aralıklar: bugün, 1, 3, 7, 14, 30 gün.
  - Doğru cevapta kart bir kutu yükselir; yanlış cevapta kutu 0'a döner ve ertesi gün sorulur.
  - Dikte sırasında yeniden kaçırılan kelime de başa döner.
- **Tekrar ekranı** (web `#/review`, Android `ReviewScreen`):
  - Kelime stüdyo sesiyle okunur ve Türkçe anlamı gösterilir; kullanıcı İngilizcesini yazar.
  - Turdaki ilk cevap kutuyu belirler; yanlış bilinen kelimeler turun sonunda bir kez daha çalışılır.
- Defterim'de "Bugün tekrar zamanı gelen N kelime" kartı ve öğrenilen kelime sayısı gösterilir.
- Android'de `java.time` için core library desugaring açıldı (minSdk 24).

### ✅ Repo Bakımı — Git Geçmişi Temizliği ve Git LFS
- Geçmiş değiştirilmeden önce tam yedek alındı: `../DictaLearn-git-backup-2026-10-04.git`.
- `git filter-repo` ile 2.3 GB WAV tüm geçmişten silindi. WAV'lar diskte duruyor, `.gitignore`'da.
- `git lfs migrate import` ile `*.mp3` ve `*.pdf` dosyaları tüm geçmişte LFS'e taşındı (219 dosya).
- Sonuç: `.git` 1.8 GB'tan ~506 MB'a indi (git deposu 5.8 MB + LFS). 100 MB'ı aşan dosya kalmadı.
- Açık lisanslı olmayan kişisel dersler (`custom_*`) repoya girmiyor (CLAUDE.md kural 6).

---

## 3. Test ve Kalite Durumu

| Platform | Katman | Araç | Sonuç |
|---|---|---|---|
| **Web** | Birim + bileşen | Vitest 5 + Testing Library | **166 / 166** |
| **Web** | Uçtan uca | Playwright, gerçek Chromium (`tools/e2e/web_e2e.py`) | **19 / 19** (telaffuz, PDF dersi, aralıklı tekrar dahil) |
| **Web** | Statik analiz | Oxlint + `tsc -b` | 0 uyarı, 0 hata |
| **Android** | Birim | JUnit 4 | **83 / 83** |
| **Android** | Uçtan uca | adb + uiautomator, Pixel 7 API 34 emülatörü (`tools/e2e/android_e2e.py`) | **14 / 14** |
| **Android** | Derleme | Gradle | debug 607 MB · release 591 MB (tüm kitaplar) |

**Uçtan uca testlerin kapsamı:**
- Kütüphane araması ve seviye filtresi.
- Kopya koruması ve klavye ayarları (otomatik düzeltme/tamamlama kapalı).
- Ses aralığının `end_ms`'de bitmesi.
- Klavyeyle tam döngü: düzeltme, kusursuz cevap, pes etme + atlama.
- PageUp/PageDown, cümleye atlama, F1/Esc.
- Yenilemede kaldığın yerden devam.
- Kelime modu: maskeli kelimeler, Boşluk ile kontrol.
- Kelime kartı ve defter; ML Kit çevirisi (Android).
- Ders sonu ekranı ve yeniden başlatma; hız kalıcılığı.
- Kitap 32 sesi; PDF yan panel ve yükleme/silme.
- Mobil taşma olmaması; konsol hatası ve çökme olmaması.

**İnsan doğrulaması önerilen noktalar:**
- Seslendirme kalitesinin kulakla kontrolü.
- Fiziksel Android cihazda deneme.
- Android ekran görüntüleri (headless emülatör boş kare veriyor).

---

## 4. Git Commit Geçmişi

Git geçmişi 2026-10-04'te yeniden yazıldı (WAV temizliği + LFS); bu tarihten önceki commit hash'leri değişti.
Son commit'ler:

```text
dede434 docs: README with screenshots, plan status after full test pass
aa961d7 test: end-to-end suites for web (Playwright) and Android (adb/uiautomator)
6975331 feat(f8): GitHub Pages and Android release workflows
d6ef429 feat(faz7,f5.9): android word card with ML Kit translation, notebook and PDF reader
c56921c feat(faz7): offline dictionary, word info card and mistake notebook (web)
24c7663 docs: document Git LFS setup and WAV/personal lesson policy
de7f8e3 docs: update plan and progress notes
b7de943 feat(android): library screen, persistent progress and mistakes, audio fixes
c1cff81 feat(web): library home, resumable sessions, audio/PDF fixes and UI overhaul
36406bc feat(content): add level 2 library (books 26-36) and fix their audio encoding
1f22064 chore: stop tracking WAV masters and personal lessons
891dc18 feat(faz6): implement word-by-word practice mode with instant checking, hints, slots, and shortcuts
```

Toplam: 64 commit. Tam liste için `git log --oneline`.
