# DictaLearn

Açık kaynak, klavye ve ses odaklı İngilizce dikte ve çeviri çalışma aracı. 
Bu depo iki ana platform içerir:
- **Web:** React + TypeScript + Vite + Tailwind CSS (GitHub Pages ve masaüstü/mobil web için)
- **Android:** Kotlin + Jetpack Compose + C++ NDK (Yüksek performanslı yerel mobil deneyim için)

Çalışma döngüsü: **Dinle → Yaz → Karşılaştır/Düzelt → Çeviri + Shadowing → Sonraki segment.**

Ürün kapsamı, durum makinesi, kısayol haritası, veri şeması ve fazlara bölünmüş görev listesi `PLAN.md` dosyasındadır. Bir göreve başlamadan önce `PLAN.md`'de o görevin faz bölümünü ve atıf yaptığı tasarım bölümlerini oku.

---

## Proje Yapısı

```text
English Book PDF Reading App/
├── Web/                     # React + TypeScript + Vite + Tailwind CSS
├── Android/                 # Kotlin + Jetpack Compose + C++ NDK
├── lessons/                 # Ortak ders paketleri (sample_ch01: audio.mp3, lesson.json)
├── CLAUDE.md                # Geliştirme kuralları ve komutlar
└── PLAN.md                  # Ayrıntılı geliştirme planı ve durum takibi
```

---

## Temel Komutlar

### Web (`Web/` dizininde)
```bash
npm install                  # Bağımlılıkları yükle
npm run dev                  # Yerel geliştirme sunucusu (Vite)
npm test                     # Vitest testleri
npm run build                # Üretim derlemesi (dist/)
npm run lint                 # ESLint kontrolü
```

### Android (`Android/` dizininde)
```bash
./gradlew assembleDebug      # Debug APK derle
./gradlew test               # Birim testleri çalıştır
./gradlew connectedAndroidTest # Cihaz/Emülatör testleri
```

---

## Mimari Kurallar

### Web Mimarisi (`Web/src/`)
- `domain/`: Saf TypeScript. React, DOM veya tarayıcı bağımlılığı yoktur. Modeller (`lesson`, `segment`), diff motoru ve doğrulama kuralları burada durur.
- `audio/`: `AudioEngine` arayüzü ve tarayıcı için `WebAudioEngine` (Web Audio API ile milisaniye hassasiyetli segment oynatımı).
- `state/`: Oturum durum makinesini (`dictating -> reviewing -> shadowing -> completed`) yöneten hook'lar/context.
- `components/`: Saf kullanıcı arayüzü bileşenleri (Tailwind CSS).

### Android Mimarisi (`Android/app/src/main/`)
- `domain/`: Saf Kotlin (ve isteğe bağlı C++ NDK diff/audio motoru).
- `audio/`: `AudioEngine` arayüzü ve Media3/ExoPlayer veya Oboe C++ uygulaması.
- `ui/`: Jetpack Compose ekranları ve bileşenleri.

### Ortak Veri (`lessons/`)
- `lesson.json` ve ses dosyaları her iki platform için de tek bir standart şemaya (`schema_version: 1`) sahiptir.

---

## Bozulmaması Gereken Kurallar

1. **Kopya koruması:** Orijinal metin ve çeviri, kullanıcı cevabını göndermeden önce DOM / UI ağacında kesinlikle yer almaz. Yalnızca CSS gizleme (`display: none` veya `opacity: 0`) ile saklamak kabul edilmez; DOM'da hiç bulunmamalıdır.
2. **Klavye temizliği:** Dikte ve düzeltme alanlarında otomatik düzeltme (`autocorrect="off"`), kelime tamamlama (`autocomplete="off"`) ve yazım denetimi (`spellcheck="false"`) kapalıdır.
3. **Kısayol güvenliği:** Bir metin alanı odaktayken çıplak tuşlara (Space, harfler) kısayol bağlanmaz. Her durumda çalışan kısayollar `Ctrl` kombinasyonudur (`Ctrl+Space`, `Ctrl+Enter`, `Ctrl+R`).
4. **Zaman formatı:** Tüm zaman değerleri `int` milisaniyedir (`start_ms`, `end_ms`). Kayan noktalı saniye kullanılmaz.
5. **Erişilebilirlik (Diff):** Diff sonucu yalnızca renkle (kırmızı/yeşil) değil, biçimle de ayrışır (üstü çizili, altı çizili).
6. **Açık Lisans:** Repoya yalnızca kamu malı veya açık lisanslı ders içeriği girer.

---

## Kod Stili ve Standartlar

- Kod tanımlayıcıları, yorum satırları ve commit mesajları **İngilizce** yazılır.
- Conventional Commits: `feat:`, `fix:`, `test:`, `docs:`, `chore:`, `refactor:`.
- Bir seferde `PLAN.md`'den tek bir görev yürütülür.
- `domain` ve `diff` için önce testler, sonra kod yazılır (TDD).
- Görev bitiminde ilgili testler çalıştırılır, `PLAN.md`'deki kutu işaretlenir.
