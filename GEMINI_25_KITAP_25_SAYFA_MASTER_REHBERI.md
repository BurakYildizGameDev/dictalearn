# 📚 DictaLearn Seviye 2: 25 Kitap x 25 Sayfa (500 Cümle) Gemini Master Üretim Rehberi

Bu belge, **DictaLearn Seviye 2 (CEFR B1 Orta Düzey)** kütüphanesini oluşturan **25 adet dünya klasiğini**, her biri **tam 25 sayfa (500 cümle)** olacak şekilde Google Gemini'ye (Gemini Advanced / Gemini 2.0 / Google AI Studio) ürettirmek için hazırlanmış **resmi master yönerge ve prompt rehberidir**.

Gemini bu rehberdeki şablona göre üretim yaptığında, çıktısı doğrudan DictaLearn sistemine aktarılmaya hazır hale gelir. Çıktıyı getirdiğinizde sistemimiz otomatik olarak:
1. **26 Sayfalık (1 Kapak + 25 Hikaye Sayfası) ReportLab PDF Kitabını** derler.
2. **Microsoft Edge Neural TTS (`en-US-ChristopherNeural`)** ile 500 cümlenin stüdyo seslendirmesini (MP3 + WAV) yapar.
3. Milisaniye senkron **`lesson.json`** dosyasını üretir.
4. **Web** ve **Android** uygulamalarına tek tıkla senkronize eder.

---

## 🎯 1. Altın Kurallar ve Biçimlendirme Standardı

Gemini'nin çıktısının DictaLearn otomasyonu tarafından hatasız okunabilmesi için aşağıdaki kuralların **tavizsiz** uygulanması şarttır:

1. **Sayfa Sayısı:** Her kitap istisnasız **tam 25 Sayfa** olacaktır.
2. **Cümle Sayısı:** Her sayfada **tam 20 Cümle** bulunacaktır (Ne 19 ne 21). 
   - Kitap genelinde toplam: **25 sayfa × 20 cümle = 500 Cümle**.
3. **Cümle Numaralandırması (ID):** Cümle numaraları 1. sayfadan 25. sayfaya kadar kesintisiz akacaktır:
   - **Sayfa 1:** Cümle 1 – 20
   - **Sayfa 2:** Cümle 21 – 40
   - **Sayfa 3:** Cümle 41 – 60
   - ...
   - **Sayfa 25:** Cümle 481 – 500
4. **Hedef Kelimeler (`vocab_focus`):** Her sayfanın tablosunun hemen altında **tam 8 adet** önemli kelime/deyim ve Türkçe karşılığı yer alacaktır. (Kitap başına toplam 200 kelime/deyim).
5. **Dil ve Seviye:** **CEFR B1 (Intermediate)**. 
   - Cümleler doğal, akıcı, zengin ve edebi İngilizce ile yazılmalı; ortalama 8–18 kelime uzunluğunda olmalıdır.
   - Türkçe çeviriler motamot Google Translate çevirisi değil; akıcı, edebi ve anlamı tam karşılayan kaliteli Türkçe olmalıdır.
6. **Dilbilgisi & Kelime Notu:** Tablonun son sütununda her cümlenin kilit kelimesi, phrasal verb'ü veya gramer yapısı `'kelime/kalıp': açıklama` formatında yer almalıdır.
7. **Özetleme / Atlama Yasağı:** Gemini asla `"..."`, `"[kalan 10 cümle benzer şekilde]"`, `"[vb.]"` gibi kısaltmalar yapamaz. Her 20 cümle tek tek eksiksiz yazılmalıdır.

---

## 📋 2. Standart Markdown Çıktı Şablonu (Gemini'nin Üreteceği Format)

Gemini'nin üreteceği her kitabın `.md` çıktısı birebir bu yapıda olmalıdır:

```markdown
# 📖 {Kitap İngilizce Başlığı} ({Kitap Türkçe Başlığı}) — 25 Sayfalık Kitap

> **Yazar**: {Yazar Adı}  
> **Uyarlama**: DictaLearn Seviye 2 (Kademeli Okuyucu / CEFR B1)  
> **Sayfa Sayısı**: 25 Sayfa (Her Sayfada Tam 20 Cümle • Toplam 500 Cümle)  
> **Kitap ID**: `book_XX_{slug}`  
> **Seslendirme**: Microsoft Edge Neural TTS (en-US-ChristopherNeural)  

---

## 📄 Sayfa 1: {Bölüm İngilizce Başlığı} ({Bölüm Türkçe Başlığı})

| No | İngilizce Cümle | Türkçe Çeviri | Dilbilgisi & Kelime Notu |
|---|---|---|---|
| **1** | English sentence here. | Cümlenin Türkçe çevirisi buraya. | `'key word': Türkçe açıklaması ve dilbilgisi ipucu.` |
| **2** | Another English sentence. | Başka bir Türkçe çeviri cümlesi. | `'phrasal verb': Türkçe anlamı ve zaman yapısı.` |
... (Tam 20 Cümle)
| **20** | Twentieth English sentence. | Yirminci cümlenin Türkçe çevirisi. | `'idiom': Deyimin Türkçe anlamı ve kullanımı.` |

**💡 Hedef Kelimeler:**
`Word 1`: Anlam 1 • `Word 2`: Anlam 2 • `Word 3`: Anlam 3 • `Word 4`: Anlam 4 • `Word 5`: Anlam 5 • `Word 6`: Anlam 6 • `Word 7`: Anlam 7 • `Word 8`: Anlam 8

---

## 📄 Sayfa 2: {Bölüm Başlığı} ({Türkçe Başlık})

| No | İngilizce Cümle | Türkçe Çeviri | Dilbilgisi & Kelime Notu |
|---|---|---|---|
| **21** | Sentence 21 text. | 21. Cümlenin Türkçe çevirisi. | `'notes': açıklama` |
...
| **40** | Sentence 40 text. | 40. Cümlenin Türkçe çevirisi. | `'notes': açıklama` |

**💡 Hedef Kelimeler:**
`Word 1`: Anlam • `Word 2`: Anlam • `Word 3`: Anlam • `Word 4`: Anlam • `Word 5`: Anlam • `Word 6`: Anlam • `Word 7`: Anlam • `Word 8`: Anlam

---
(Sayfa 3'ten 25'e kadar aynı disiplinle devam eder; Sayfa 25, Cümle 500 ile biter.)
```

---

## 🤖 3. Gemini'ye Verilecek Master Sistem İstemi (System Prompt)

Gemini'yi açtığınızda **ilk olarak** aşağıdaki blok mesajı gönderin. Bu komut Gemini'yi "DictaLearn Edebi İçerik Motoru" moduna sokar:

```text
Sen dünyanın en iyi İngilizce öğretmeni, edebi çevirmeni ve CEFR (Avrupa Ortak Dil Kriterleri) içerik geliştiricisisin.
Görevin, DictaLearn interaktif dil ve dikte platformu için dünya edebiyatı klasiklerini CEFR B1 (Intermediate) seviyesine uyarlayarak tam 25 sayfalık (her sayfada tam 20 cümle, toplam 500 cümle) çift dilli (İngilizce-Türkçe) ders ve okuma kitapları üretmektir.

Çıktıyı üretirken aşağıdaki KESİN kurallara uyacaksın:
1. FORMAT: Çıktıyı sadece ve sadece DictaLearn Markdown formatında ve Markdown tablosu olarak vereceksin. Ekstra sohbet cümlesi, giriş veya kapanış yazısı ekleme.
2. SAYFA VE CÜMLE DİSİPLİNİ:
   - Kitap tam 25 sayfadan oluşur.
   - Her sayfada istisnasız tam 20 cümle yer alır. Ne 19 ne 21.
   - Cümle ID'leri Sayfa 1'de 1-20, Sayfa 2'de 21-40 ... Sayfa 25'te 481-500 olarak kesintisiz ilerler. Toplam 500 cümledir.
3. TABLO YAPISI:
   Her sayfa için şu tablo yapısını kuracaksın:
   | No | İngilizce Cümle | Türkçe Çeviri | Dilbilgisi & Kelime Notu |
   Tablonun hemen altına tam 8 adet hedef kelimeyi şu formatta ekleyeceksin:
   **💡 Hedef Kelimeler:**
   `Terim 1`: Anlamı • `Terim 2`: Anlamı • ... • `Terim 8`: Anlamı
4. DİL VE EDEBİ KALİTE:
   - İngilizce cümleler CEFR B1 seviyesinde, doğal, akıcı, zengin edebi dilde, ortalama 10-18 kelime olmalıdır.
   - Türkçe çeviriler motamot çeviri olmayıp, edebiyat kalitesinde doğal Türkçe ifade edilmelidir.
   - 'Dilbilgisi & Kelime Notu' sütununda her cümle için o cümlenin anahtar kelimesi, phrasal verb'ü, gramer yapısı veya deyimi tek tırnak içinde Türkçe açıklamasıyla yer almalıdır (Örn: 'gazing at': dikkatle uzun uzun bakmak; 'used to': geçmişteki alışkanlık).
5. KESİNTİSİZLİK VE ASLA ATLAMA YAPMAMA:
   - Asla "...", "vb.", "[kalan cümleler benzer şekilde devam eder]" gibi kısaltmalar yapma.
   - Her cümleyi tek tek, tam metin olarak yazacaksın.

Bu kuralları anladıysan "Hazırım, hangi kitabı ve hangi sayfaları üretmemi istersiniz?" diye yanıt ver.
```

---

## ⚡ 4. Token Sınırına Takılmama Taktikleri (5'er Sayfalık Blok Stratejisi)

Tek bir mesajda 500 cümle (~8.500 kelime ve tablo biçimlendirmesi) üretmek, Gemini'nin token çıkış sınırını zorlayabilir ve Gemini 12-15. sayfadan sonra metni kesebilir veya özetlemeye başlayabilir.

Bunu önlemek ve her sayfanın **%100 kusursuz, tam 20 cümle ve tam 8 kelime** olmasını garanti altına almak için **5'er sayfalık bloklar (Part 1 - Part 5)** halinde üretmeniz önerilir:

### 🔹 Part 1 İstemi (Sayfa 1 - 5 | Cümle 1 - 100):
```text
Lütfen [KİTAP ADI] için SAYFA 1 ile SAYFA 5 arasını (Cümle 1 - Cümle 100) kurallara tam uyarak üret.
- Her sayfada tam 20 cümle olacak.
- Cümle ID'leri 1'den başlayıp 100'de bitecek.
- Her sayfa sonunda 8 hedef kelime olacak.
```

### 🔹 Part 2 İstemi (Sayfa 6 - 10 | Cümle 101 - 200):
```text
Harika, şimdi SAYFA 6 ile SAYFA 10 arasını (Cümle 101 - Cümle 200) üret.
- Cümle ID'leri 101'den başlayıp 200'de bitecek.
- Her sayfada tam 20 cümle ve 8 hedef kelime.
```

### 🔹 Part 3 İstemi (Sayfa 11 - 15 | Cümle 201 - 300):
```text
Çok iyi, şimdi SAYFA 11 ile SAYFA 15 arasını (Cümle 201 - Cümle 300) üret.
- Cümle ID'leri 201'den başlayıp 300'de bitecek.
- Her sayfada tam 20 cümle ve 8 hedef kelime.
```

### 🔹 Part 4 İstemi (Sayfa 16 - 20 | Cümle 301 - 400):
```text
Devam et, şimdi SAYFA 16 ile SAYFA 20 arasını (Cümle 301 - Cümle 400) üret.
- Cümle ID'leri 301'den başlayıp 400'de bitecek.
- Her sayfada tam 20 cümle ve 8 hedef kelime.
```

### 🔹 Part 5 İstemi (Sayfa 21 - 25 | Cümle 401 - 500 - FİNAL):
```text
Şimdi son bölüm olan SAYFA 21 ile SAYFA 25 arasını (Cümle 401 - Cümle 500) hikayeyi tamamlayarak üret.
- Cümle ID'leri 401'den başlayıp 500'de bitecek.
- Hikaye 500. cümlede tatmin edici bir şekilde sonlanacak.
- Her sayfada tam 20 cümle ve 8 hedef kelime.
```

*Not:* Üretilen 5 parçayı tek bir metin belgesinde alt alta birleştirip `book_preview.md` olarak kaydettiğinizde 500 cümlelik eksiksiz kitabınız hazır olur!

---

## 📚 5. 25 Kitaplık Seviye 2 Kütüphane Kataloğu (Kitap 26 - Kitap 50)

Aşağıda Seviye 2 için seçilen 25 dünya klasiğinin kimlikleri, yazar bilgileri ve **her kitabın hikayesini 25 sayfaya mükemmel şekilde dağıtan bölüm konu başlıkları** yer almaktadır. Gemini'ye doğrudan bu başlıkları vererek hikaye temposunun kusursuz olmasını sağlayabilirsiniz:

---

### 📖 Kitap 26: A Scandal in Bohemia (Bohemya'da Skandal)
- **Kitap ID:** `book_26_a_scandal_in_bohemia`
- **Yazar:** Sir Arthur Conan Doyle (Sherlock Holmes)
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Baker Street 221B'de Sakin Bir Akşam ve Watson'ın Ziyareti*
  2. *Gizemli Mektup ve Bohemya Armalı Şifreli Kağıt*
  3. *Maskeli Yabancının Gelişi ve Kont von Kramm Kimliği*
  4. *Bohemya Kralı'nın Gerçek Kimliğini İtiraf Etmesi*
  5. *Irene Adler Olayı: Şantaj Tehdidi ve Tehlikeli Fotoğraf*
  6. *Kralın Başarısız Girişimleri: Hırsızlar ve Sahte Soygunlar*
  7. *Sherlock Holmes'ün Planı ve Irene Adler'in Evi*
  8. *Holmes'ün Arabacı Kılığında Bilgi Toplaması*
  9. *Briony Lodge Etrafındaki Dedikodular ve Avukat Godfrey Norton*
  10. *Kilisede Beklenmedik Nikah Şahitliği*
  11. *Baker Street'e Dönüş ve Akşam Operasyonu Planı*
  12. *Irene Adler'in Evinin Önündeki Sahte Kavga*
  13. *Holmes'ün Yaşlı Rahip Kılığında Yaralanması*
  14. *Oturma Odasına Taşınma ve Açık Bırakılan Pencere*
  15. *Watson'ın İşareti: Yangın Bombası ve "Yangın Var!" Çığlığı*
  16. *İnsan Doğasının Tepkisi: Irene'in Gizli Bölmeye Koşması*
  17. *Holmes'ün Gizli Bölmenin Yerini Keşfetmesi ve Sessiz Kaçış*
  18. *Sokakta Yürürken Arkadan Gelen Gizemli "İyi Geceler Bay Holmes" Sesi*
  19. *Ertesi Sabah: Kral, Watson ve Holmes Briony Lodge'a Gidiyor*
  20. *Terk Edilmiş Ev ve Hizmetçinin Şaşırtıcı Haberi*
  21. *Irene Adler'in Holmes'e Bıraktığı Mektup Açılıyor*
  22. *Mektubun İçeriği: Rahibin Gerçek Kimliğini Nasıl Anladı?*
  23. *Erkek Kılığına Girip Baker Street'e Kadar Takip Eden Irene Adler*
  24. *Fotoğrafın Güvende Olduğu ve Kralın Artık Özgür Olduğu Garantisi*
  25. *Kralın Şükranı ve Holmes'ün Altın Yüzük Yerine Irene Adler'in Fotoğrafını İstemesi*

---

### 📖 Kitap 27: The Red-Headed League (Kızıl Saçlılar Kulübü)
- **Kitap ID:** `book_27_the_red_headed_league`
- **Yazar:** Sir Arthur Conan Doyle (Sherlock Holmes)
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Baker Street'te Alev Kızılı Saçlı Bir Ziyaretçi: Jabez Wilson*
  2. *Holmes'ün İlginç Gözlemleri ve Wilson'ın Mesleği*
  3. *Gazete İlanı: "Kızıl Saçlılar Kulübü'ne Yüksek Maaşlı Eleman"*
  4. *Wilson'ın Yardımcısı Vincent Spaulding ve İlanın Tavsiyesi*
  5. *Fleet Street'teki İnanılmaz İzdiham: Binlerce Kızıl Saçlı Adam*
  6. *Duncan Ross ile Mülakat ve Wilson'ın İşe Kabulü*
  7. *Tuhaf Görev: Britannica Ansiklopedisi'ni Elle Kopya Etmek*
  8. *Haftalık Dört Sterlin Maaş ve Düzenli Büro Mesaisi*
  9. *Sekiz Hafta Süren Huzurlu Çalışma ve "A" Harfinin Bitmesi*
  10. *Kilitli Kapıdaki Şok Edici Pusula: "Kızıl Saçlılar Kulübü Feshedilmiştir"*
  11. *Wilson'ın Çaresizliği ve Holmes'ün Kahkahaları*
  12. *Büro Sahibini Soruşturma: Duncan Ross Aslında Kim?*
  13. *Yardımcı Vincent Spaulding'in Şüpheli Davranışları ve Karanlık Odası*
  14. *Holmes'ün Saxe-Coburg Meydanı'ndaki Rehinciler Dükkanına Gitmesi*
  15. *Holmes'ün Bastonuyla Kaldırım Taşlarına Vurması*
  16. *Spaulding'in Pantolon Dizlerindeki Çamur İzi İpuçları*
  17. *Dükkanın Arkasındaki Şehir Bankası ve Yeraltı Tüneli Şüphesi*
  18. *Akşam Randevusu: Polis Müfettişi Jones ve Banka Müdürü Merryweather*
  19. *City and Suburban Bank'ın Yeraltı Mahzenine İniş*
  20. *Fransız Altın Külçeleri ve Karanlıkta Sessiz Bekleyiş*
  21. *Zemindeki Taşın Oynaması ve Fener Işığının Belirmesi*
  22. *Ünlü Suçlu John Clay'in Tünelden Çıkışı ve Holmes'ün Baskını*
  23. *Kelepçelenen Soyguncular ve Polisin Başarısı*
  24. *Holmes'ün Dehası: Kızıl Saç İlanının Asıl Amacı Ortaya Çıkıyor*
  25. *Dükkanda Tünel Kazmak İçin Kurulan Sahte Kulüp ve Zekice Çözüm*

---

### 📖 Kitap 28: The Hound of the Baskervilles (Baskerville'lerin Köpeği)
- **Kitap ID:** `book_28_the_hound_of_the_baskervilles`
- **Yazar:** Sir Arthur Conan Doyle (Sherlock Holmes)
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Dr. Mortimer'ın Baker Street'e Gelişi ve Unutulan Baston*
  2. *Baskerville Ailesinin Kadim El Yazması ve Korkunç Lanet Efsanesi*
  3. *Sir Charles Baskerville'in Gece Porsuk Ağaçlı Yoldaki Gizemli Ölümü*
  4. *Cesedin Yanındaki Devasa Tazı Ayak İzleri*
  5. *Yeni Mirasçı Sir Henry Baskerville'in Londra'ya Gelişi*
  6. *Northumberland Otelinde Çalınan Botlar ve İsimsiz Uyarı Mektubu*
  7. *Londra Sokaklarında Faytonla Takip Eden Sakallı Adam*
  8. *Sir Henry'nin Dartmoor Malikanesine Gitme Kararı*
  9. *Holmes'ün Watson'ı Gözlemci Olarak Dartmoor'a Göndermesi*
  10. *Devonshire Kırları ve Bataklıktan Kaçan Firari Mahkum Selden*
  11. *Baskerville Konağı'nın Kasvetli Havası ve Uşak Barrymore*
  12. *Gece Koridorlarda Ağlayan Kadın ve Mumla Verilen Gizli İşaretler*
  13. *Doğa Bilimci Stapleton ve Güzel Kız Kardeşi Beryl ile Tanışma*
  14. *Beryl Stapleton'ın Watson'a Gizli Uyarısı: "Derhal Buradan Kaçın!"*
  15. *Grimpen Bataklığı'nın Ölümcül Çamurları ve Geceleri Gelen Korkunç Uluma*
  16. *Watson'ın Tepelerde Gördüğü Yalnız Siluet: Gizemli Yabancı*
  17. *Terk Edilmiş Taş Kulübede Saklanan Sherlock Holmes ile Karşılaşma*
  18. *Holmes'ün Gizli Araştırmaları ve Stapleton'ın Gerçek Kimliği*
  19. *Bataklıkta Bulunan Ceset: Sir Henry'nin Elbiselerini Giyen Mahkum*
  20. *Baskerville Portreleri ve Stapleton'ın Aile Benzerliği*
  21. *Merrivale Köşkündeki Akşam Yemeği ve Yoğun Sis Dalgası*
  22. *Sir Henry'nin Bataklık Yolunda Tek Başına Yürümesi*
  23. *Sisin İçinden Fırlayan Fosforlu Ateş Saçan Devasa Canavar Köpek*
  24. *Holmes'ün Tabanca Atışları ve Canavarın Etkisiz Hale Getirilmesi*
  25. *Stapleton'ın Bataklığa Kaçışı, Çamura Batışı ve Lanetin Sonu*

---

### 📖 Kitap 29: The Gift of the Magi & The Last Leaf (O. Henry Seçme Öyküler)
- **Kitap ID:** `book_29_the_gift_of_the_magi`
- **Yazar:** O. Henry
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Della'nın Biriktirdiği Bir Dolar Seksen Yedi Sent ve Noel Arifesi*
  2. *Yoksul Daire ve Aynada Parlayan Muhteşem Uzun Saçlar*
  3. *Jim'in Gururu: Dededen Kalma Değerli Altın Cep Saati*
  4. *Della'nın Kararı: Madam Sofronie'nin Kuaför Dükkanına Koşuş*
  5. *Yirmi Dolara Satılan Saçlar ve Şehirdeki Mağazaları Dolaşma*
  6. *Altın Saate Yakışan Kusursuz Platin Zincirin Bulunması*
  7. *Della'nın Eve Dönüşü, Maşayla Bukle Yapma ve Heyecanlı Bekleyiş*
  8. *Jim'in Kapıyı Açması ve Della'nın Kısa Saçlarına Şaşkın Bakışı*
  9. *Della'nın Aşk Dolu Savunması: "Saçlarım Yine Uzar Sevgilim"*
  10. *Jim'in Noel Hediyesi Paketini Açması: Kaplumbağa Kabuğundan Mücevherli Taraklar*
  11. *Della'nın Platin Saat Zincirini Göstermesi ve Jim'in Gülümsemesi*
  12. *Büyük Fedakarlık: Tarakları Almak İçin Satılan Altın Saat*
  13. *Magi'lerin En Yüce Bilgeliği: Birbirine Kalbini Feda Eden İki Aşık*
  14. *Greenwich Village Sanatçı Kolonisi ve Sue ile Johnsy'nin Atölyesi*
  15. *Kasım Soğuğu ve Mahalleyi Kasıp Kavuran Zatürre Salgını*
  16. *Doktorun Acı Teşhisi: Johnsy'nin Yaşama Umudunu Kaybetmesi*
  17. *Pencereden Görünen Karşı Duvar ve Sarmaşık Yaprakları*
  18. *Johnsy'nin Geriye Sayımı: "Son Yaprak Düştüğünde Ben de Öleceğim"*
  19. *Sue'nun Çırpınışı ve Alt Katta Yaşayan İhtiyar Ressam Behrman*
  20. *Behrman'ın Kırk Yıldır Yapmayı Hayal Ettiği Başyapıtı*
  21. *Gece Çıkan Fırtına, Yağan Yağmur ve Şiddetli Rüzgar*
  22. *Sabah Perdenin Açılması: Duvarda Hâlâ Tek Başına Direnen Yeşil Yaprak*
  23. *Johnsy'nin Yaşama Tutunması ve İyileşme Belirtileri*
  24. *Doktorun Ziyareti: Johnsy Kurtuldu Ama Behrman Ağır Zatürre Oldu*
  25. *Gerçek Açıklanıyor: Duvara Gece Fırtınada Çizilen Ölümsüz Başyapıt*

---

### 📖 Kitap 30: The Call of the Wild (Vahşetin Çağrısı)
- **Kitap ID:** `book_30_the_call_of_the_wild`
- **Yazar:** Jack London
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Yargıç Miller'ın Güneşli Santa Clara Vadisi'ndeki Çiftliği ve Buck*
  2. *Bahçıvan Manuel'in Kumara Yenik Düşmesi ve Buck'ı Kaçırması*
  3. *Tren Yolculuğu, Kafesteki Açlık ve Kızıl Kazaklı Adamın Sopası*
  4. *Sopa ve Diş Kanunu: İlkel Yaşama İlk Sert Uyanış*
  5. *Kuzeye Yolculuk: Narwhal Gemisi ve Dyea Sahiline Varış*
  6. *Karla İlk Karşılaşma ve Husky Köpeklerinin Vahşi Dünyası*
  7. *Curly'nin Trajik Sonu ve Buck'ın Asla Düşmemeyi Öğrenmesi*
  8. *Perrault ve Francois'nın Kızak Takımına Katılma*
  9. *Karların Altına Çukur Kazarak Uyumayı Öğrenmek*
  10. *Öncü Köpek Spitz ile Rekabet ve Liderlik Çekişmesi*
  11. *Aç Yabani Köpeklerin Gece Kamp Baskını*
  12. *Buzlu Nehirleri Aşmak ve Klondike Patikalarındaki Sınav*
  13. *Buck ve Spitz'in Dolunay Altındaki Ölüm Kalım Düellosu*
  14. *Buck'ın Zaferi ve Kızak Liderliğini Zorla Alması*
  15. *Posta Servisinde Rekor Hız ve Yorucu Seferler*
  16. *Tükenmiş Köpeklerin Hal, Charles ve Mercedes'e Satılması*
  17. *Beceriksiz Yeni Sahiplerin Açgözlülüğü ve Ağır Kızak Yükü*
  18. *Erimeye Başlayan İlkbahar Buzulları ve White Nehri Kampı*
  19. *John Thornton'ın Müdahalesi ve Buck'ı Dayaktan Kurtarması*
  20. *Kızağın İnce Buzun Kırılmasıyla Sulara Gömülmesi*
  21. *John Thornton'ın Şefkati ve Buck'ın Karşılıksız Aşkı*
  22. *Nehirde Boğulmaktan Kurtarılan Thornton ve Bin Dolarlık Bahis*
  23. *Doğuya Doğru Altın Arayışı ve Issız Vahşi Doğa*
  24. *Ormandan Gelen Kurt Ulumaları ve Buck'ın İçsel Çağrısı*
  25. *Thornton'ın Trajedisi, İntikam ve Kurt Sürüsünün Başına Geçiş*

---

### 📖 Kitap 31: Frankenstein
- **Kitap ID:** `book_31_frankenstein`
- **Yazar:** Mary Shelley
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Kaptan Walton'ın Kuzey Kutbu Mektupları ve Buzlar Arasındaki Gemi*
  2. *Buz Üstünde Süzülen Dev Siluet ve Donmak Üzere Kurtarılan Yabancı*
  3. *Victor Frankenstein'ın Cenevre'deki Mutlu Çocukluk Yılları*
  4. *Elizabeth Lavenza ve Sadık Dost Henry Clerval*
  5. *Ingolstadt Üniversitesi'ne Gidiş ve Doğa Bilimlerine Tutku*
  6. *Yaşamın Sırrını Çözme Hırsı ve Mezarlıklarda Gizli Deneyler*
  7. *Kasım Gecesi Laboratuvar: Yaratığın Sarı Gözlerinin Açılması*
  8. *Victor'ın Dehşete Düşüp Kaçması ve Sinir Krizi*
  9. *Cenevre'den Gelen Acı Haber: Küçük William'ın Öldürülmesi*
  10. *Alpler'e Kaçış ve Montanvert Buzulunda Yaratıkla Karşılaşma*
  11. *Yaratığın Konuşması: Dünyaya Geldiği İlk Anlar ve Ormandaki Açlık*
  12. *Köydeki İnsanların Taşlı Saldırıları ve Bir Kulübeye Sığınma*
  13. *De Lacey Ailesini Duvar Deliğinden İzleme ve İyiliği Öğrenme*
  14. *Kitaplar Bulma, Konuşmayı ve Okumayı Öğrenme Mucizesi*
  15. *Kör Yaşlı Adamla Konuşma ve Çocukların Dehşet İçinde Onu Kovması*
  16. *İnsanlığa Karşı Yemin Edilen Nefret ve Cenevre'ye Yolculuk*
  17. *William'ın Cinayeti ve Justine'in Haksız Yere İdam Edilmesi*
  18. *Yaratığın Tek Dileği: "Bana Benim Gibi Bir Eş Yarat!"*
  19. *Frankenstein'ın İstemeyerek Kabul Etmesi ve İskoçya'ya Gitmesi*
  20. *Orkney Adaları'nda İkinci Yaratığı Parçalaması ve Verilen Yemin: "Düğün Gecende Yanında Olacağım"*
  21. *Henry Clerval'ın Sahilde Bulunan Cansız Bedeni*
  22. *Victor'ın Cenevre'ye Dönüşü ve Elizabeth ile Düğünü*
  23. *Düğün Gecesi Çığlık: Elizabeth'in Yatak Odasında Boğulması*
  24. *Babasının Kahrından Ölümü ve Dünyanın Ucuna Kadar Süren Takip*
  25. *Walton'ın Gemisinde Frankenstein'ın Son Nefesi ve Yaratığın Pişmanlık Gözyaşları*

---

### 📖 Kitap 32: Dracula (Kont Drakula)
- **Kitap ID:** `book_32_dracula`
- **Yazar:** Bram Stoker
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Jonathan Harker'ın Londra'dan Transilvanya'ya Yolculuğu*
  2. *Bistritz Otelinde Köylülerin Haç Vermesi ve Korku Dolu Bakışlar*
  3. *Borgo Geçidi'nde Gece Yarısı Siyah Faytona Aktarma*
  4. *Uçurumun Tepesindeki Kasvetli Drakula Şatosu'na Varış*
  5. *Kont Drakula ile Tanışma: Buz Gibi Eller ve Sivri Dişler*
  6. *Kütüphanede Londra Haritaları ve Emlak Sözleşmeleri*
  7. *Aynada Görünmeyen Kont ve Kan Damlasına Karşı Çılgınlığı*
  8. *Şatoda Bir Tutsak Olduğunu Anlamak: Kilitli Kapılar*
  9. *Yasak Kanatta Üç Dişi Vampirin Gece Saldırısı ve Kont'un Müdahalesi*
  10. *Kont'un Toprak Dolu Tabutta Uyurken Görülmesi ve Jonathan'ın Kaçış Planı*
  11. *Whitby Sahili: Fırtınada Karaya Oturan İnsansız Demeter Gemisi*
  12. *Mina Murray ve Arkadaşı Lucy Westenra'nın Sahildeki Günleri*
  13. *Lucy'nin Gece Uykusunda Mezarlığa Gitmesi ve Boynundaki İki Küçük Delik*
  14. *Lucy'nin Solgunlaşması ve Dr. Seward'ın Akıl Hastanesindeki Renfield*
  15. *Amsterdam'dan Gelen Bilge: Profesör Abraham Van Helsing*
  16. *Odaya Asılan Sarımsak Çiçekleri ve Gece Pencereyi Kıran Kurt*
  17. *Lucy'nin Ölümü ve Gece Parklarda Kaybolan Çocuklar*
  18. *Mezarlık Ziyareti: Tabuttan Çıkan Vampir Lucy ve Kurtarılışı*
  19. *Jonathan Harker'ın Dönüşü ve Drakula'ya Karşı Kurulan Birlik*
  20. *Londra'daki Carfax Malikanesi'ne Baskın ve Kutsal Suyla Arındırma*
  21. *Drakula'nın Gece Mina'nın Odasına Girişi ve Kan Bağı Laneti*
  22. *Mina'nın Hipnoz Edilmesi ve Drakula'nın Gemiyle Kaçış Rotası*
  23. *Transilvanya'ya Geri Takip: Nehir Boyunca Yarış*
  24. *Kar Fırtınası Altında Şato Önündeki Çingeneler ve Tabut Konvoyu*
  25. *Güneş Batarken Kukri Bıçağının Darbesi, Drakula'nın Toza Dönüşmesi ve Huzur*

---

### 📖 Kitap 33: The Strange Case of Dr. Jekyll and Mr. Hyde (Dr. Jekyll ve Bay Hyde)
- **Kitap ID:** `book_33_the_strange_case_of_dr_jekyll_and_mr_hyde`
- **Yazar:** Robert Louis Stevenson
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Avukat Bay Utterson ve Enfield'ın Pazar Yürüyüşleri*
  2. *Londra Ara Sokağındaki Kasvetli Kapı ve Küçük Kıza Çarpan Adam*
  3. *Bay Hyde'ın İğrenç Varlığı ve Saygın Dr. Jekyll Adına Yazılan Çek*
  4. *Dr. Jekyll'ın Tuhaf Vasiyetnamesi: "Her Şey Edward Hyde'a Kalacaktır"*
  5. *Eski Dost Dr. Lanyon'ın Bilimsel Ayrılık İtirafı*
  6. *Karanlık Sokakta Utterson'ın Bay Hyde ile İlk Yüzleşmesi*
  7. *Dr. Jekyll'ın Görkemli Evindeki Akşam Yemeği ve Dostça Uyarı*
  8. *Sir Danvers Carew'in Thames Kıyısında Vahşice Katledilmesi*
  9. *Olay Yerinde Kırık Baston ve Soho'daki Hyde'ın Sığınağı*
  10. *Dr. Jekyll'ın Yemini: "Hyde ile Sonsuza Dek İlişiğimi Kestim"*
  11. *Hyde'ın El Yazısı ile Jekyll'ın Yazısının Gizemli Benzerliği*
  12. *Birkaç Ay Süren İyilik ve Jekyll'ın Sosyal Hayata Dönüşü*
  13. *Dr. Lanyon'ın Ölümcül Korkusu ve Mühürlü Mektubu*
  14. *Laboratuvar Penceresindeki Jekyll'ın Yüzündeki Dehşet Verici Değişim*
  15. *Uşak Poole'un Fırtınalı Gecede Utterson'ın Kapısını Çalması*
  16. *Kilitli Laboratuvar Kapısı Arkasından Gelen Yabancı Ses*
  17. *Şehirdeki Tüm Eczanelerden Aranan Saf Kimyasal Tuzlar*
  18. *Baltayla Kırılan Kapı ve Yerde Zehirlenerek Can Çekişen Hyde*
  19. *Masada Bulunan İtiraflar ve Dr. Lanyon'ın Mühürlü Zarfı*
  20. *Lanyon'ın Anlatımı: Gece Gelen Hyde'ın İksiri İçişi*
  21. *Lanyon'ın Gözleri Önünde Hyde'ın Jekyll'a Dönüşmesi ve Şok*
  22. *Henry Jekyll'ın Tam İtirafı: İnsanın Çift Doğası Kuramı*
  23. *İlk Deney: İksirin Hazzı ve Saf Kötülük Olan Hyde'ın Doğuşu*
  24. *Kontrolden Çıkan Dönüşümler: Uykuda İksirsiz Hyde Olarak Uyanmak*
  25. *Kimyasal Maddenin Tükenmesi, Çaresizlik ve Trajik Son*

---

### 📖 Kitap 34: The Picture of Dorian Gray (Dorian Gray'in Portresi)
- **Kitap ID:** `book_34_the_picture_of_dorian_gray`
- **Yazar:** Oscar Wilde
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Basil Hallward'ın Leylak Kokulu Stüdyosu ve Muhteşem Portre*
  2. *Lord Henry Wotton'ın Ziyareti ve Hayat Üzerine Alaycı Fikirleri*
  3. *Dorian Gray ile Tanışma: Kusursuz Masumiyet ve Gençlik*
  4. *Lord Henry'nin Bahçedeki Zehirli Konuşması: "Gençlikten Değerli Şey Yoktur"*
  5. *Dorian'ın Dileği: "Keşke Ben Hep Genç Kalsam da Tablo Yaşlansa!"*
  6. *Portrenin Bitmesi ve Basil'in Dorian'a Hediyesi*
  7. *Londra'nın Yoksul Tiyatrosu ve Oyuncu Sibyl Vane'e Aşık Olmak*
  8. *Sibyl'ın Kardeşi Jim Vane'in Avustralya'ya Gitmeden Önceki Yemini*
  9. *Romeo ve Juliet Oyunu: Sibyl'ın Gerçek Aşkı Bulup Kötü Oynaması*
  10. *Dorian'ın Acımasızca Kalbini Kırması ve Tiyatroyu Terk Etmesi*
  11. *Eve Dönüş: Tablonun Ağız Kenarındaki Zalimce Kıvrılma*
  12. *Lord Henry'den Gelen Haber: Sibyl Vane'in İntiharı*
  13. *Dorian'ın Pişmanlığı Unutup Estetik Bir Trajedi Olarak Görmesi*
  14. *Tablonun Eski Çocukluk Odasındaki Kilitli Odaya Saklanması*
  15. *Yıllar Geçer: Dorian Hiç Yaşlanmaz Ama Şehirde Skandallar Yayılır*
  16. *Basil Hallward'ın Paris'e Gitmeden Önce Dorian'a Gelmesi*
  17. *Kilitli Odaya Çıkış: Tablodaki Dehşet Verici Çürümüş Yaşlı Yüz*
  18. *Dorian'ın Öfke Krizi ve Basil'i Bıçaklayarak Öldürmesi*
  19. *Eski Kimyager Dost Alan Campbell'a Cesedi Yok Ettirmek*
  20. *Afyon Tekkelerine Kaçış ve Denizci Jim Vane ile Karşılaşma*
  21. *Genç Yüzü Sayesinde Ölümden Kurtuluş Ama Başlayan Paranoya*
  22. *Kır Köşkünde Av Partisi ve Çalılıkta Yanlışlıkla Vurulan Avcı*
  23. *Ölen Adamın Jim Vane Olduğunun Anlaşılması ve Rahatlama*
  24. *Dorian'ın Temiz Bir Hayat Yaşama İsteği ve Tabloyu Tekrar Kontrolü*
  25. *Tablonun Daha da Çirkinleşmesi, Tabloyu Bıçaklama ve Yerde Yaşlı Ceset*

---

### 📖 Kitap 35: The Canterville Ghost (Canterville Hayaleti)
- **Kitap ID:** `book_35_the_canterville_ghost`
- **Yazar:** Oscar Wilde
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Amerikalı Bakan Hiram B. Otis'in Canterville Malikanesini Satın Alması*
  2. *Lord Canterville'in Hayalet Uyarısı ve Amerikan Mantığı*
  3. *Otis Ailesinin Taşınması: Bayan Otis, Washington, Virginia ve İkizler*
  4. *Kütüphane Şöminesindeki Üç Yüz Yıllık Silinmez Kan Lekesi*
  5. *Washington Otis'in Leke Çıkarıcı Çubuğuyla Lekeyi Saniyede Temizlemesi*
  6. *Gece Koridorda Zincir Şakırtıları ve Sir Simon de Canterville*
  7. *Bay Otis'in Hayalete Zincirlerini Yağlasın Diye Makine Yağı Vermesi*
  8. *Gururu Kırılan Hayaletin Şişeyi Yere Fırlatıp Kaçması*
  9. *Her Sabah Farklı Renkte (Zümrüt Yeşili, Kırmızı) Yenilenen Kan Lekesi*
  10. *Hayaletin Zırh Giyip İntikam Alma Planı ve Zırhın Altında Ezilmesi*
  11. *İkizlerin Sapan ve Yastık Tuzakları: Hayaletin Panikle Kaçışı*
  12. *Canterville Hayaletinin Şanlı Tarihi ve Yüzyıllardır Korkuttuğu Soylular*
  13. *Hayaletin Karşılaştığı Sahte Hayalet: İkizlerin Balkabağı Tuzağı*
  14. *Sir Simon'ın Sinir Krizleri Geçirmesi ve Keçe Tabanlı Terlik Giymesi*
  15. *Virginia Otis'in Gizli Odada Ağlayan Yaşlı Hayaleti Bulması*
  16. *Sir Simon'ın İtirafı: Karısını Öldürmesi ve Aç Bırakılarak Ölmesi*
  17. *Üç Yüz Yıldır Uyumayan ve Dinlenemeyen Hayaletin Çilesi*
  18. *Kütüphane Penceresindeki Kadim Kehanet Yazıtı*
  19. *Virginia'nın Sevgi ve Masumiyetle Hayalet İçin Dua Etmeyi Kabul Etmesi*
  20. *Gizli Kapının Açılması ve Virginia'nın Karanlık Boyuta Geçişi*
  21. *Akşam Yemeğinde Virginia'nın Yokluğu ve Bütün Kasabanın Arama Başlatması*
  22. *Gece Yarısı Gök Gürültüsü ve Duvardan Geri Gelen Virginia*
  23. *Kurumuş Badem Ağacının Çiçek Açması: Hayaletin Affedilişi*
  24. *Yeraltı Mahzeninde İskeletin Bulunması ve Görkemli Cenaze Töreni*
  25. *Virginia'nın Dük ile Evlenmesi ve Canterville Bahçesindeki Hatıra*

---

### 📖 Kitap 36: Journey to the Center of the Earth (Dünyanın Merkezine Yolculuk)
- **Kitap ID:** `book_36_journey_to_the_center_of_the_earth`
- **Yazar:** Jules Verne
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Hamburg'da Profesör Otto Lidenbrock ve Eski Rünik El Yazması*
  2. *Şifreli Parşömen: İzlandalı Simyacı Arne Saknussemm'in Mesajı*
  3. *Yeğen Axel'ın Şifreyi Tesadüfen Çözmesi: Sneffels Yanardağı Krateri*
  4. *Lidenbrock'un Büyük Heyecanı ve Axel'ın Endişeleri*
  5. *Hamburg'dan Kopenhag'a ve Oradan Reykjavik'e Deniz Yolculuğu*
  6. *Soğukkanlı ve Sadık İzlandalı Rehber Hans Bjelke ile Tanışma*
  7. *Sneffels Kraterine Tırmanış ve Sönmüş Yanardağın Ağzı*
  8. *Temmuz Güneşinin Gölgesi: Doğru Krater Bacasına İniş*
  9. *Yerin Derinliklerine Urganlarla İniş ve Lav Tünelleri*
  10. *Su Stoğunun Tükenmesi ve Axel'ın Susuzluktan Bayılması*
  11. *Hans'ın Kayayı Delmesi: Kaynar Ama Hayat Kurtaran Hansbach Deresi*
  12. *Yerin Kilometrelerce Altında Dev Kömür ve Fosil Katmanları*
  13. *Axel'ın Labirentte Kaybolması ve Akustik Duvar Sayesinde Sesle Bulunma*
  14. *Büyük Boşluğa Açılış: Yeraltı Akdeniz'i ve Elektrikli Gökyüzü*
  15. *Dev Mantarlar Ormanı ve Tarih Öncesi Bitki Örtüsü*
  16. *Bir Sal İnşa Edilmesi ve Yeraltı Denizine Yelken Açış*
  17. *Oltaya Gelen İlkel Balıklar ve Devasa Deniz Sürüngenleri*
  18. *İhtiyozor ve Pleziyozor'un Sal Yanındaki Korkunç Savaşı*
  19. *Korkunç Yeraltı Fırtınası ve Salın Kayalıklara Çarpması*
  20. *Tarih Öncesi İnsan Kafatası ve Mamut Sürüsünü Güden Dev Çoban*
  21. *Saknussemm'in Baş Harflerinin Kazındığı Tıkalı Kaya Geçidi*
  22. *Geçidi Açmak İçin Barutla Patlatma Yapılması*
  23. *Açılan Uçurumun Denizi Yutması ve Salın Boşluğa Sürüklenişi*
  24. *Yükselen Lav Dalgası: Aktif Bir Yanardağ Bacasından Yukarı Fırlayış*
  25. *Stromboli Adası'nda Akdeniz Güneşi Altında Yeniden Doğuş ve Zafer*

---

### 📖 Kitap 37: Twenty Thousand Leagues Under the Sea (Denizler Altında 20.000 Fersah)
- **Kitap ID:** `book_37_twenty_thousand_leagues_under_the_sea`
- **Yazar:** Jules Verne
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Okyanuslarda Beliren Gizemli ve Hızlı Deniz Canavarı Efsanesi*
  2. *Prof. Pierre Aronnax, Sadık Uşağı Conseil ve Abraham Lincoln Fırkateyni*
  3. *Kanadalı Usta Zıpkıncı Ned Land ile Tanışma*
  4. *Aylarca Süren Pasifik Taraması ve Canavarın Nihayet Görünmesi*
  5. *Zıpkının Çelik Zırhtan Sekmesi ve Fırkateynin Çarpışmada Hasar Alması*
  6. *Aronnax ve Arkadaşlarımızın Denize Düşüşü ve Çelik Gövdeye Sığınış*
  7. *Nautilus'un İçine Alınış ve Maskeli Denizciler*
  8. *Kaptan Nemo ile Tanışma: Özgürlüğün ve Denizlerin Gizemli Hakimi*
  9. *Nautilus'un Harikaları: Elektrik Gücü, Kütüphane ve Sanat Galerisi*
  10. *Dev Cam Pencereden Okyanusun Büyülü Yaşamını İzlemek*
  11. *Dalgıç Kıyafetleriyle Crespo Adası Su Altı Ormanlarında Av*
  12. *Torres Boğazı'nda Mercanlara Oturan Denizaltı ve Yerlilerin Saldırısı*
  13. *Elektrikli Korkuluklar Sayesinde Nemo'nun Savunması*
  14. *Kızıldeniz'den Akdeniz'e: Yeraltı Arap Tüneli Geçişi*
  15. *Girit İsyanı'na Su Altından Gizlice Altın Yardımı Gönderen Nemo*
  16. *Kayıp Kıta Atlantis'in Yıkıntıları Üzerinde Gece Yürüyüşü*
  17. *Sönmüş Bir Yanardağın İçindeki Kömür Madeni Sığınağı*
  18. *Güney Kutbu Buzullarının Altından Geçiş ve Buz Dağında Sıkışma*
  19. *Oksijenin Tükenmesi ve Mürettebatın Buzları Kazarak Kurtulması*
  20. *Bahamalar'da Devasa Mürekkep Balıklarının Nautilus'a Saldırısı*
  21. *Baltalarla Yapılan Kanlı Güverte Savaşı ve Bir Denizcinin Kaybı*
  22. *Nemo'nun Derin Kederi ve Aronnax'ın Kaçış Planları*
  23. *Bilinmeyen Bir Savaş Gemisinin Ateş Açması ve Nemo'nun Acımasız İntikamı*
  24. *Geminin Batırılışı, Nemo'nun Gözyaşları ve Norveç Maelström Girdabı*
  25. *Girdapta Kurtulan Sandal ve Aronnax'ın Dünyaya Dönüşü*

---

### 📖 Kitap 38: The Invisible Man (Görünmez Adam)
- **Kitap ID:** `book_38_the_invisible_man`
- **Yazar:** H. G. Wells
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Kar Fırtınasında Iping Kasabasındaki Coach and Horses Hanına Gelen Yabancı*
  2. *Tepeden Tırnağa Sargılarla Sarılı Adam ve Mavi Gözlükleri*
  3. *Bayan Hall'un Merakı ve Yabancının Soğuk Kabalığı*
  4. *Han Odasına Gelen Sandıklar Dolusu Şişeler ve Kimyasal Deneyler*
  5. *Kasabada Yayılan Dedikodular ve Papazın Evindeki Gizemli Hırsızlık*
  6. *Kiranın İstenmesi ve Yabancının Sargılarını, Burnunu Çıkarması*
  7. *Kafası Olmayan Bir Adam! Handaki İzdiham ve Polisin Şaşkınlığı*
  8. *Elbiselerini Çıkarıp Tamamen Görünmez Olarak Kaçış*
  9. *Kırlarda Serseri Thomas Marvel ile Karşılaşma ve Onu Zorla Yardımcı Yapma*
  10. *Iping'e Dönüp Laboratuvar Defterlerini Handan Çalma Operasyonu*
  11. *Marvel'ın Kitaplarla Kaçmaya Çalışması ve Port Burdock'a Sığınması*
  12. *Jolly Cricketers Meyhanesindeki Çatışma ve Görünmez Adamın Vurulması*
  13. *Yaralı Adamın Lüks Bir Villaya Sığınması: Eski Üniversite Arkadaşı Dr. Kemp*
  14. *Griffin'in Kimliğini Açıklaması ve Kemp'in Şaşkınlığı*
  15. *Griffin'in Hikayesi: Işığın Kırılması ve Kumaşları Görünmez Yapma Keşfi*
  16. *Kedi Üzerinde Deney ve Kendi Vücudunu Görünmez Yapışı*
  17. *Laboratuvarını Yakıp Londra Sokaklarında Çıplak ve Görünmez Kalışı*
  18. *Soğuk, Çamur ve İnsanların Çarpması: Görünmezliğin Korkunç Zorlukları*
  19. *Drury Lane Kostümcüsünden Maske ve Giysi Çalma Macerası*
  20. *Griffin'in Korkunç Planı: "Bir Terör Saltanatı Kuracağız ve Sen Yardım Edeceksin"*
  21. *Kemp'in Polise Haber Vermesi ve Griffin'in İhaneti Anlaması*
  22. *Griffin'in İntikam Yemini: "Bugün Kemp'in İlk İdam Günü Olacak"*
  23. *Kemp'in Evine Kuşatma ve Polis Şefinin Öldürülmesi*
  24. *Kemp'in Kasaba Merkezine Koşması ve Bütün Halkın Griffin'i Sıkıştırması*
  25. *Kalabalığın Linçi, Griffin'in Son Nefesi ve Yavaş Yavaş Görünür Olan Bedeni*

---

### 📖 Kitap 39: The War of the Worlds (Dünyalar Savaşı)
- **Kitap ID:** `book_39_the_war_of_the_worlds`
- **Yazar:** H. G. Wells
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *19. Yüzyılın Sonunda İnsanlığın Kibri ve Mars'tan İzlenen Dünya*
  2. *Ottershaw Rasathanesinde Mars Yüzeyindeki Gaz Patlamaları*
  3. *Woking Yakınlarındaki Horsell Çayırına Düşen Devasa Silindir*
  4. *Silindirin Kapağının Açılması ve İtişip Kakan Meraklı Kalabalık*
  5. *Silindirden Çıkan Dokunaçlı, Devasa Gözlü Korkunç Yaratıklar*
  6. *Beyaz Bayrakla Yaklaşan Barış Heyeti ve İlk Isı Işını Katliamı*
  7. *Çam Ormanlarının Alev Alması ve Anlatıcının Karısını Kaçırması*
  8. *Üç Ayaklı Çelik Savaş Makinelerinin (Tripodlar) Ortaya Çıkışı*
  9. *İngiliz Topçusunun Çaresizliği ve Weybridge Muharebesi*
  10. *Nehirde Bir Tripodun Vurulması ve Marslıların Zehirli Kara Dumanı*
  11. *Londra'da Başlayan Büyük Panik: Milyonların Kaçışı ve Trenlerin Çöküşü*
  12. *Anlatıcının Kardeşinin Kaçışı ve İki Hanımefendiyi Kurtarışı*
  13. *Essex Sahiline Ulaşım ve Vapurla Kaçan Mülteciler*
  14. *Savaş Gemisi HMS Thunder Child'ın İki Tripodu Batırıp Feda Oluşu*
  15. *Anlatıcının Deliren Bir Rahip ile Yıkık Bir Evde Mahsur Kalması*
  16. *Evin Bahçesine Düşen Yeni Silindir ve Marslıların Beslenme Vahşeti*
  17. *Rahibin Çıldırıp Ses Çıkarması ve Marslı Dokunacının Odaya Girişi*
  18. *Kömürlükte Günlerce Aç Susuz Saklanış ve Marslıların Ayrılışı*
  19. *Kızıl Yabani Otların Her Yeri Sarması ve Harabeye Dönen Londra*
  20. *Putney Tepesinde Karşılaşılan Topçu Askeri ve Yeraltı Hayali*
  21. *Terk Edilmiş Londra Sokaklarında Yalnız Yürüyüş*
  22. *Regent's Park'tan Gelen Acı ve Monoton Ses: "Ulla, Ulla, Ulla"*
  23. *Tripodların Hareketsiz Durması ve İçlerindeki Marslıların Ölümü*
  24. *Zaferin Sırrı: İnsanlığın En Küçük Müttefiki Olan Bakteriler*
  25. *Karısıyla Yeniden Buluşma ve Evrende Artık Yalnız Olmadığımız Gerçeği*

---

### 📖 Kitap 40: The Adventures of Tom Sawyer (Tom Sawyer'ın Maceraları)
- **Kitap ID:** `book_40_the_adventures_of_tom_sawyer`
- **Yazar:** Mark Twain
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Polly Teyze'nin Çağrısı ve Reçel Dolabından Kaçan Yaramaz Tom*
  2. *Cumartesi Cezası: Koca Bir Çiti Beyaza Boyama Görevi*
  3. *Tom'un Dehası: Çit Boyamayı Büyük Bir Ayrıcalık Gibi Gösterip Çocukları Kandırma*
  4. *Çocukların Sıraya Girmesi ve Tom'un Elma, Uçurtma ve Ölü Fare Kazanması*
  5. *Kasabaya Yeni Gelen Yargıcın Kızı Becky Thatcher'a Aşık Olma*
  6. *Pazar Okulu ve Biletleri Takasla Toplayıp Hileyle İncil Ödülü Alma*
  7. *Huckleberry Finn ile Tanışma ve Siğil Düşürmek İçin Ölü Kedi Planı*
  8. *Gece Yarısı Mezarlık: Dr. Robinson, Muff Potter ve Kızılderili Joe*
  9. *Mezar Açma Kavgası: Joe'nun Doktoru Öldürüp Suçu Sarhoş Potter'a Atması*
  10. *Tom ve Huck'ın Kanla Yemin Etmesi: "Kimse Bu Sırrı Söylemeyecek!"*
  11. *Vicdan Azabı ve Muff Potter'ın Masum Yere Hapse Atılması*
  12. *Becky ile Bozuşma ve Dünyaya Küsme: Korsan Olma Kararı*
  13. *Tom, Huck ve Joe Harper'ın Jackson Adası'na Kaçışı*
  14. *Adada Kamp Ateşi, Yüzme ve Nehirde Boğulan Çocukları Arayan Vapur*
  15. *Tom'un Gece Gizlice Eve Gelip Polly Teyze'nin Ağlayışını Dinlemesi*
  16. *Kendi Cenaze Törenlerine Katılma: Kilisede Yaşanan Büyük Sevinç*
  17. *Okulda Becky'nin Yırttığı Öğretmen Kitabının Cezasını Tom'un Üstlenmesi*
  18. *Muff Potter'ın Mahkemesi: Tom'un Kürsüye Çıkıp Gerçeği Haykırması*
  19. *Kızılderili Joe'nun Mahkeme Penceresinden Atlayıp Kaçması*
  20. *Perili Evde Hazine Arama ve Joe'nun Altın Dolu Kutuyu Buluşu*
  21. *Kasabanın Pikniği ve McDougal Mağarası Gezisi*
  22. *Tom ve Becky'nin Mağarada Kaybolması, Mumların Tükenmesi*
  23. *Mağara Karanlığında Kızılderili Joe'yu Görmek ve Çıkış Yolu Arayışı*
  24. *Tom'un Uçurtma İpiyle Nehir Kenarında Bir Delik Bulup Kurtulmaları*
  25. *Demir Kapıyla Kilitlenen Mağarada Joe'nun Sonu ve Mağaradaki Altın Hazine*

---

### 📖 Kitap 41: The Prince and the Pauper (Prens ve Dilenci)
- **Kitap ID:** `book_41_the_prince_and_the_pauper`
- **Yazar:** Mark Twain
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Aynı Gün Doğan İki Bebek: Galler Prensi Edward ve Sefil Tom Canty*
  2. *Pudding Lane'de Yoksulluk ve Peder Andrew'dan Latince Öğrenen Tom*
  3. *Tom'un Saray Hayalleri ve Westminster Sarayı Kapısına Gitmesi*
  4. *Nöbetçinin Tom'u İtmesi ve Prens Edward'ın Müdahale Edip İçeri Alması*
  5. *Prens ile Dilencinin Kıyafet Değiştirme Oyunu: İkiz Gibi Benzerlik*
  6. *Edward'ın Dışarı Fırlaması ve Nöbetçilerce Dilenci Sanılarak Kovulması*
  7. *Sarayda Kalan Tom'un Dehşeti: Herkesin Onu Delirdi Sanması*
  8. *Kral VIII. Henry'nin Emri: "Oğlumun Hastalığından Kimse Bahsetmeyecek"*
  9. *Saray Ziyafetleri ve Tom'un Çatal Bıçak Bilmeyen Masumiyeti*
  10. *Edward'ın Londra Sokaklarındaki Sefaleti ve John Canty'nin Dayağı*
  11. *Kralın Ölümü: Sarayda Tom'un Yeni Kral İlan Edilmesi*
  12. *Edward'ı Linçten Kurtaran Soylu Şövalye Miles Hendon*
  13. *Hendon'ın Hendon Hall'daki Mirasından Mahrum Edilişi*
  14. *Edward'ın Hendon'a "Kralın Karşısında Oturma Hakkı" Bağışlaması*
  15. *Tom'un Saraydaki Merhameti: Haksız İdamları Durdurması*
  16. *Edward'ın Hırsız Çetesi Tarafından Kaçırılıp Zindana Atılması*
  17. *Halkın Çektiği Zulmü Bizzat Yaşayarak Öğrenen Gerçek Prens*
  18. *Hendon'ın Edward İçin Kırbaç Cezasını Üstlenmesi*
  19. *Taç Giyme Töreni Günü: Westminster Manastırı'ndaki Görkemli Alay*
  20. *Tom'un Taç Giymek Üzereyken Annesini Görmesi ve Vicdan Azabı*
  21. *Paçavralar İçindeki Edward'ın Manastıra Girişi: "Ben Gerçek Kralım!"*
  22. *Tom'un Derhal Tahttan İnip Edward'ın Önünde Eğilmesi*
  23. *Büyük Devlet Mührünün Kayboluşu ve Edward'ın Sakladığı Yeri Hatırlaması*
  24. *Edward'ın Tahta Çıkması, Tom'u Kraliyet Kardeşi İlan Etmesi*
  25. *Miles Hendon'ın Ödüllendirilmesi ve Adaletli, Merhametli Genç Kralın Hükmü*

---

### 📖 Kitap 42: Oliver Twist
- **Kitap ID:** `book_42_oliver_twist`
- **Yazar:** Charles Dickens
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Yoksullar Evinde Dünyaya Gelen Adsız Bir Bebek ve Annesinin Ölümü*
  2. *Bay Bumble'ın İsim Verme Sistemi ve Yıllar Süren Açlık*
  3. *Tarihi İsyan: "Lütfen Efendim, Biraz Daha Çorba İstiyorum"*
  4. *Beş Sterlin Ödülle Bacacıya Verilmek İstenmesi ve Tabutçunun Yanına Giriş*
  5. *Noah Claypole'un Annesine Hakaret Etmesi ve Oliver'ın İlk Öfke Patlaması*
  6. *Londra'ya Doğru Yetmiş Millik Karlı Kaçış Yürüyüşü*
  7. *Barnet'te Artful Dodger ile Tanışma ve Sıcak Yemek Teklifi*
  8. *Fagin'in Karanlık İnine Giriş: Kızartılan Sosisler ve Mendil Oyunu*
  9. *Dodger ve Bates ile Sokak Devriyesi: Bay Brownlow'un Kitapçı Önünde Soyulması*
  10. *Polisin Oliver'ı Yakalaması ve Yargıç Karşısında Bayılması*
  11. *Brownlow'un Merhameti ve Oliver'ı Şefkatli Evine Alması*
  12. *Duvardaki Kadın Portresi ve Oliver'ın İnanılmaz Yüz Benzerliği*
  13. *Kitapçıya Para Götürürken Bill Sikes ve Nancy Tarafından Kaçırılma*
  14. *Fagin'in Yanına Geri Getiriliş ve Elbiselerinin Çalınması*
  15. *Chertsey'deki Köşk Soygunu Planı ve Sikes'ın Tabancalı Tehdidi*
  16. *Oliver'ın Küçük Pencereden İçeri İtilmesi ve Hizmetçilerce Vurulması*
  17. *Bayan Maylie ve Rose'un Yaralı Oliver'a Sahip Çıkması*
  18. *Köydeki Huzurlu İyileşme Günleri ve Gizemli Monks'un Ortaya Çıkışı*
  19. *Nancy'nin Vicdanı: London Bridge Altında Rose Maylie ile Gizli Buluşma*
  20. *Noah'nın Nancy'yi Takip Etmesi ve Fagin'e Haber Uçurması*
  21. *Bill Sikes'ın Vahşeti: Nancy'nin Korkunç Şekilde Öldürülmesi*
  22. *Katil Sikes'ın Kaçışı ve Londra Çatılarında Kendi İpiyle Boğularak Ölümü*
  23. *Monks'un İtirafı: Oliver'ın Zengin Mirası ve Öz Kardeşi Olduğu Gerçeği*
  24. *Fagin'in İdam Hücresindeki Son Çılgın Gecesi*
  25. *Bay Brownlow'un Oliver'ı Evlat Edinmesi ve Adaletin Huzuru*

---

### 📖 Kitap 43: Great Expectations (Büyük Umutlar)
- **Kitap ID:** `book_43_great_expectations`
- **Yazar:** Charles Dickens
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Sisli Bataklık Mezarlığında Pip ve Anne Babasının Mezar Taşları*
  2. *Ayaklarında Pranga Olan Firari Mahkum Magwitch ile Korkunç Karşılaşma*
  3. *Demircinin Evinden Çalınan Eğik Törpü ve Soğuk Et Turtası*
  4. *Bataklıktaki Askerler, İki Mahkumun Kavgası ve Magwitch'in Pip'i Koruması*
  5. *Demirci Joe Gargery'nin Saf Sevgisi ve Cadaloz Abla*
  6. *Satis House'a Davet: Zamanın Durduğu Karanlık Malikane*
  7. *Gelinliği İçinde Yaşlanan Bayan Havisham ve Kurtlu Düğün Pastası*
  8. *Güzel Ama Kalpsiz Estella: Pip'in Kaba Ellerini ve Botlarını Aşağılaması*
  9. *Pip'in Centilmen Olma Hayali ve Demircilikten Utanmaya Başlaması*
  10. *Londralı Avukat Bay Jaggers'ın Gelişi: "Büyük Umutlar ve Gizemli Bir Hami"*
  11. *Joe'ya Veda ve Londra'ya Centilmen Olmak İçin Yolculuk*
  12. *Barnard's Inn'de Herbert Pocket ile Dostluk*
  13. *Havisham'ın İntikam Planı: Erkeklerin Kalbini Kırmak İçin Yetiştirilen Estella*
  14. *Joe'nun Londra Ziyareti ve Pip'in Aptalca Snopluğu ve Utancı*
  15. *Borçların Katlanması ve Estella'nın Kaba Bentley Drummle ile Flörtü*
  16. *Yirmi Üçüncü Yaş Günü: Fırtınalı Gece Kapıyı Çalan Yaşlı Adam*
  17. *Şok Edici Gerçek: Gizemli Hami Havisham Değil, Avustralya'daki Mahkum Magwitch!*
  18. *İdam Cezası Tehdidi Altındaki Magwitch'i Londra'da Saklama Zorunluluğu*
  19. *Pip'in Kibir ve Servet Hayallerinin Yıkılışı ve Derin Pişmanlık*
  20. *Estella'nın Gerçek Kimliği: Magwitch ile Jaggers'ın Hizmetçisinin Kızı*
  21. *Satis House'da Yangın: Havisham'ın Yanması ve Pip'in Elleriyle Kurtarışı*
  22. *Thames Nehri Üzerinde Kürekle Kaçış Planı ve Hamburg Vapuru*
  23. *Düşman Compeyson'ın Polis Botuyla Yolu Kesmesi ve Nehirde Çatışma*
  24. *Yaralanan Magwitch'in Mahkeme Hücresinde Pip'in Kollarında Ölümü*
  25. *Joe'nun Borçları Ödemesi, Yıllar Sonra Satis House Yıkıntılarında Estella ile Karşılaşma*

---

### 📖 Kitap 44: Jane Eyre
- **Kitap ID:** `book_44_jane_eyre`
- **Yazar:** Charlotte Brontë
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Gateshead Hall'da İstenmeyen Yetim Jane ve John Reed'in Zorbalığı*
  2. *Korkunç Kırmızı Oda Cezası ve Jane'in Baygınlık Geçirmesi*
  3. *Lowood Yetimler Okulu'na Gönderiliş ve Bay Brocklehurst'ün Katılığı*
  4. *Açlık, Soğuk Su ve Aziz Ruhlu Helen Burns ile Dostluk*
  5. *Tifüs Salgını ve Helen'ın Kollarında Cennete Uğurlanışı*
  6. *Jane'in Öğretmen Oluşu ve Bağımsız Bir Hayat İçin Gazete İlanı*
  7. *Thornfield Malikanesi'ne Mürebbiye Olarak Geliş ve Küçük Adèle*
  8. *Bayan Fairfax'ın Sıcaklığı ve Çatı Katından Gelen Garip Kahkaha*
  9. *Hay Hayat Yolu'nda Atıyla Düşen Huysuz Efendi Rochester ile Tanışma*
  10. *Gece Yangını: Rochester'ın Alev Alan Yatağını Jane'in Suyla Söndürmesi*
  11. *Hizmetçi Grace Poole'un Şüpheli Davranışları*
  12. *Malikaneye Gelen Zengin Konuklar ve Blanche Ingram'ın Kibri*
  13. *Falcı Çingene Kılığına Giren Rochester'ın Jane'in Kalbini Yoklaması*
  14. *Mason'ın Jamaika'dan Gelişi ve Gece Çatı Katında Kanlı Yaralanması*
  15. *Bayan Reed'in Ölüm Döşeğindeki İtirafı: Jane'in Zengin Amcasının Mektubu*
  16. *Kestane Ağacı Altında Evlilik Teklifi ve Gece Ağaca Yıldırım Düşmesi*
  17. *Düğün Arifesi: Odadaki Yırtılan Gelinlik Duvağı ve Dehşet Verici Yüz*
  18. *Düğün Töreninin Kesilmesi: "Bu Adam Zaten Evlidir!"*
  19. *Kilitli Çatı Odası: Rochester'ın Deli Karısı Bertha Mason ile Karşılaşma*
  20. *Jane'in Gururu ve İnancı: Metres Olmayı Reddedip Gece Kaçışı*
  21. *Kırlarda Açlık, Dilencilik ve Moor House'da St. John Rivers'ın Kurtarışı*
  22. *Köy Okulu Öğretmenliği ve Amcadan Kalan Yirmi Bin Sterlinlik Miras*
  23. *St. John'ın Hindistan'a Misyonerlik Teklifi ve Jane'in Rüzgarda Duyduğu Ses: "Jane! Jane!"*
  24. *Thornfield'a Koşuş: Yanmış Küller, Bertha'nın İntiharı ve Kör Kalan Rochester*
  25. *Ferndean'de Buluşma: "Sevgilim, Sana Geri Döndüm"*

---

### 📖 Kitap 45: Wuthering Heights (Uğultulu Tepeler)
- **Kitap ID:** `book_45_wuthering_heights`
- **Yazar:** Emily Brontë
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Yeni Kiracı Lockwood'un Fırtınalı Uğultulu Tepeler Ziyareti*
  2. *Heathcliff'in Kabalığı, Vahşi Köpekler ve Gece Odada Mahsur Kalış*
  3. *Pencereyi Kıran Buz Gibi Küçük El: "Ben Catherine Linton, İçeri Al!"*
  4. *Lockwood'un Çığlığı ve Heathcliff'in Pencereye Koşup Ağlayışı*
  5. *Nelly Dean'in Thrushcross Grange'de Anlatmaya Başladığı Geçmiş*
  6. *Bay Earnshaw'un Liverpool'dan Getirdiği Simsiyah Yetim Çocuk: Heathcliff*
  7. *Hindley'nin Nefreti, Catherine'in İse Heathcliff'e Tutkulu Bağlılığı*
  8. *Kırlarda Özgür Çocukluk ve Thrushcross Grange Pencerelerini Gözetleme*
  9. *Catherine'in Köpek Tarafından Isırılması ve Linton Ailesinin Evinde Kalışı*
  10. *Catherine'in Kibar Bir Hanımefendi Olarak Dönüşü ve Heathcliff'in Yalnızlığı*
  11. *Edgar Linton'ın Evlilik Teklifi ve Catherine'in Nelly'ye İtirafı*
  12. *“Ruhlarımız Aynı Hamurdan: Ben Heathcliff'im!” Ama Sosyal Statü Engeli*
  13. *Heathcliff'in Konuşmanın Bir Kısmını Duyup Fırtınada Evi Terk Edişi*
  14. *Üç Yıl Sonra Zengin, Güçlü ve İntikam Dolu Bir Beyefendi Olarak Dönüşü*
  15. *Edgar'ın Kız Kardeşi Isabella'yı Sırf İntikam İçin Kaçırıp Evlenmesi*
  16. *Catherine'in Ağır Hastalığı ve İki Aşığın Yıkıcı Son Kucaklaşması*
  17. *Catherine'in Doğumda Ölümü ve Heathcliff'in Ağaca Başını Vurarak Haykırışı: "Beni Hayalet Olarak Rahatsız Et!"*
  18. *Hindley'nin Kumar Borçlarıyla Uğultulu Tepeler'i Heathcliff'e Kaptırması*
  19. *Küçük Cathy Linton'ın Büyümesi ve Yasak Kırlara Adım Atışı*
  20. *Heathcliff'in Cathy'yi Kaçırıp Hasta Oğlu Linton ile Zorla Evlendirmesi*
  21. *Linton ve Edgar'ın Ölümü: Her İki Malikanenin de Heathcliff'in Eline Geçmesi*
  22. *Nelly'nin Hikayeyi Bitirmesi ve Lockwood'un Şehre Dönüşü*
  23. *Aylar Sonra Lockwood'un Dönüşü: Genç Hareton ile Cathy'nin Aşkı*
  24. *Heathcliff'in Yemeden İçmeden Kesilmesi ve Catherine'in Hayalini Görmesi*
  25. *Yatakta Gülümseyerek Bulunan Cansız Bedeni ve Kırlarda Gezen İki Hayalet*

---

### 📖 Kitap 46: Pride and Prejudice (Aşk ve Gurur)
- **Kitap ID:** `book_46_pride_and_prejudice`
- **Yazar:** Jane Austen
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Bayan Bennet'ın Heyecanı: "Netherfield Park Zengin Bir Genç Tarafından Tutuldu!"*
  2. *Meryton Kasabası Balosu: Sevimli Bay Bingley ve Soğuk Bay Darcy*
  3. *Darcy'nin Kibri: "Elizabeth beni etkileyecek kadar güzel değil"*
  4. *Elizabeth'in Gururunun Kırılması ve Alaycı Neşesi*
  5. *Jane ile Bingley Arasındaki Masum ve Derin Sevgi*
  6. *Jane'in Netherfield'da Yağmurda Hastalanması ve Elizabeth'in Çamurlu Yürüyüşü*
  7. *Darcy'nin Elizabeth'in Zeki Gözlerinden Etkilenmeye Başlaması*
  8. *Kuzen Bay Collins'in Miras ve Evlilik Amacıyla Ziyareti*
  9. *Milis Alayının Yakışıklı Subayı George Wickham ile Tanışma*
  10. *Wickham'ın Yalanları: Darcy'nin Onu Mirastan Mahrum Ettiği İftirası*
  11. *Netherfield Balosu ve Darcy ile Elizabeth'in Gergin Dansı*
  12. *Bay Collins'in Komik Evlilik Teklifi ve Elizabeth'in Sert Reddi*
  13. *Bingley Ailesinin Aniden Londra'ya Kaçışı ve Jane'in Kırık Kalbi*
  14. *Elizabeth'in Rosings Park Ziyareti ve Leydi Catherine de Bourgh'un Kibri*
  15. *Darcy'nin Beklenmedik Evlilik Teklifi: "Sınıf Farkınıza Rağmen Sizi Seviyorum"*
  16. *Elizabeth'in Öfkeli Reddi: "Jane'in Mutluluğunu ve Wickham'ı Mahvettiniz!"*
  17. *Darcy'nin Açıklama Mektubu: Wickham'ın Kız Kardeşi Georgiana'yı Kaçırma Girişimi*
  18. *Elizabeth'in Körlüğünü Fark Etmesi: "Kendimi Ne Kadar Az Tanıyormuşum!"*
  19. *Pemberley Malikanesi Gezisi ve Hizmetçilerin Darcy'yi Övgüleri*
  20. *Darcy ile Gölette Karşılaşma: Kibarlık ve Değişmiş Bir Adam*
  21. *Lydia'nın Wickham ile Kaçtığı Haberi ve Ailenin Felaketi*
  22. *Darcy'nin Gizlice Londra'ya Gidip Parayla Düğünü Yaptırması*
  23. *Bingley'nin Dönüşü ve Jane'e Evlilik Teklifi*
  24. *Leydi Catherine'in Elizabeth'i Tehdit Etmesi ve Elizabeth'in Dik Duruşu*
  25. *Kırlarda Yürüyüş: Darcy ile Elizabeth'in Aşk İtirafı ve Mutlu Çift Düğünü*

---

### 📖 Kitap 47: The Count of Monte Cristo (Monte Kristo Kontu)
- **Kitap ID:** `book_47_the_count_of_monte_cristo`
- **Yazar:** Alexandre Dumas
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Pharaon Gemisinin Marsilya Limanı'na Girişi ve Genç Kaptan Edmond Dantès*
  2. *Kıskanç Kargo Şefi Danglars ve Güzel Nişanlı Mercédès*
  3. *Fernand Mondego'nun Kıskançlığı ve Komplo Mektubunun Yazılışı*
  4. *Düğün Ziyafeti Sırasında Dantès'in Jandarmalarca Tutuklanması*
  5. *Savcı Villefort'un Kendi Babasını Korumak İçin Masum Edmond'ı Kurban Etmesi*
  6. *Karanlık Suların Ortasındaki Korkunç If Şatosu Zindanına Atılış*
  7. *Yıllar Süren Tecrit, Açlık ve İntiharın Eşiğindeki Çaresizlik*
  8. *Hücre Duvarından Gelen Tıkırtı: Bilge Mahkum Rahip Faria ile Tanışma*
  9. *Faria'nın Edmond'a Bilim, Diller, Felsefe ve Komployu Çözmeyi Öğretmesi*
  10. *Monte Kristo Adası'ndaki Kardinal Spada'nın Trilyonluk Gizli Hazinesi*
  11. *Faria'nın Felç Geçirip Ölümü ve Dantès'in Ceset Torbasına Girmesi*
  12. *Denize Fırlatılış: Dalgalarla Boğuşma ve Özgürlüğe İlk Kulaç*
  13. *Kaçakçı Gemisine Kurtarılış ve Monte Kristo Adası'na İlk Ayak Basış*
  14. *Mağaranın Gizli Girişi: Sandıklar Dolusu Altın, Pırlanta ve Zümrütler*
  15. *Sonsuz Zenginlik ve Doğan İntikam Tanrısı: Monte Kristo Kontu*
  16. *Marsilya'ya Dönüş: Babasının Açlıktan Öldüğünü ve Mercédès'in Fernand ile Evlendiğini Öğreniş*
  17. *Eski Dost Morrel'ı İflastan Kurtaran Gizemli Sinbad*
  18. *Roma Karnavalı: Fernand'ın Oğlu Albert de Morcerf'i Haydutlardan Kurtarma*
  19. *Paris Yüksek Sosyetesine Görkemli Giriş ve Düşmanların Karşısına Çıkış*
  20. *Danglars Bankası'nın Sahte Telgraflarla İflasa Sürüklenmesi*
  21. *Fernand'ın Ali Paşa'ya İhanetinin Ortaya Çıkması ve İntiharı*
  22. *Villefort Ailesinin İçindeki Zehirli Cinayetler Zinciri*
  23. *Mercédès'in Kont'un Edmond Olduğunu Anlaması ve Oğlunu Bağışlatması*
  24. *Villefort'un Delirmesi ve Kont'un İlahi Adalet Karşısında Ürperişi*
  25. *Maximilien ile Valentine'in Kavuşması ve Kont'un Son Sözü: "Beklemek ve Umut Etmek"*

---

### 📖 Kitap 48: The Three Musketeers (Üç Silahşörler)
- **Kitap ID:** `book_48_the_three_musketeers`
- **Yazar:** Alexandre Dumas
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *Gaskonyalı Genç D'Artagnan'ın Sarı Atı ve Babasının Kılıcıyla Yola Çıkışı*
  2. *Meung Kasabasında Yara İzli Adamla Kavga ve Tavsiye Mektubunun Çalınışı*
  3. *Paris'te Mösyö de Tréville'in Silahşörler Karargahına Varış*
  4. *Merdivenlerde Çarpışma: Athos, Porthos ve Aramis ile Üç Ayrı Düello Randevusu*
  5. *Carmelites Manastırı Arkasındaki Düello ve Kardinal Richelieu'nün Muhafızları*
  6. *D'Artagnan'ın Silahşörlerin Safına Geçmesi: "Birimiz Hepimiz, Hepimiz Birimiz İçin!"*
  7. *Kral XIII. Louis'nin Silahşörleri Ödüllendirmesi*
  8. *D'Artagnan'ın Ev Sahibinin Eşi Constance Bonacieux'a Aşık Olması*
  9. *Kraliçe Anne ve İngiliz Bakan Buckingham Dükü'nün Gizli Aşkı*
  10. *Kraliçenin Buckingham'a Verdiği On İki Elmas Kolye Ucu*
  11. *Kardinalin Tuzağı: Krala Kolyeli Balo Düzenletmesi ve Milady de Winter*
  12. *Constance'ın Kolyeyi Geri Getirme Görevi İçin D'Artagnan'ı Seçmesi*
  13. *Dört Dostun Londra Yolculuğu ve Yolda Pusuya Düşürülen Dostlar*
  14. *D'Artagnan'ın Tek Başına Manş Denizini Aşıp Londra'ya Ulaşması*
  15. *Milady'nin Çaldığı İki Elmasın Kuyumcuya Gece Boyunca Yeniden Yaptırılışı*
  16. *Paris'e Çılgın Dönüş ve Baloda Kraliçenin Elmaslarla Parlaması*
  17. *Kardinalin Yenilgisi ve D'Artagnan'a Verilen Kraliçe Yüzüğü*
  18. *Constance'ın Kaçırılması ve Athos'un Karanlık Geçmişi (Damgalı Milady)*
  19. *La Rochelle Kuşatması ve Kraliyet Ordusunun Kampı*
  20. *Kırmızı Güvercinlik Hanı: Kardinalin Milady'ye Suikast Emri*
  21. *Saint-Gervais Kalesinde Bahis: Kurşunlar Altında Kahvaltı*
  22. *Milady'nin İngiltere'de Zindana Atılması ve Muhafızı Kandırıp Kaçışı*
  23. *Béthune Manastırı: Milady'nin Constance'ı Zehirleyerek Katletmesi*
  24. *Lys Nehri Kıyısında Gece Yarısı Yargılama ve Milady'nin İdamı*
  25. *Kardinalin D'Artagnan'a Teğmenlik Beratı Vermesi ve Dört Silahşörün Zaferi*

---

### 📖 Kitap 49: Don Quixote (Don Kişot)
- **Kitap ID:** `book_49_don_quixote`
- **Yazar:** Miguel de Cervantes
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *La Mancha'da Şövalye Romanları Okumaktan Aklını Yitiren Soylu Alonso Quijano*
  2. *Paslı Zırhlar, Cılız At Rocinante ve "Don Kişot" İsminin Alınması*
  3. *Köylü Kızı Aldonza'nın Yüce Prenses "Dulcinea del Toboso" Yapılması*
  4. *Köy Hanının Şato Sanılması ve Hancı Tarafından Şövalye İlan Ediliş*
  5. *Tüccarlarla Kavga, Dayak Yiyiş ve Komşusu Tarafından Eve Taşınış*
  6. *Papaz ve Berberin Kütüphanedeki Zararlı Şövalye Romanlarını Yakması*
  7. *Komşu Köylü Sancho Panza'ya Ada Valiliği Vaat Edip Seyis Yapma*
  8. *Gece Yarısı İkinci Sefer: Eşek Sırtındaki Sancho ve Zırhlı Şövalye*
  9. *Yel Değirmenleri Ovası: Don Kişot'un Onları Kötü Devler Sanıp Hücumu*
  10. *Kırılan Mızrak ve Sancho'nun Mantıklı Feryatları*
  11. *Toz Bulutu İçindeki İki Büyük Ordu: Koyun Sürülerine Karşı Savaş*
  12. *Çobanların Taş Yağmuru ve Kaybedilen Dişler*
  13. *Berberin Bakır Tıraş Leğenini "Efsanevi Mambrino Miğferi" Sanmak*
  14. *Kralın Kürek Mahkumlarını "Zulme Uğrayan Masumlar" Diye Serbest Bırakış*
  15. *Nankör Mahkumların Don Kişot ve Sancho'yu Taşlayıp Kaçması*
  16. *Sierra Morena Dağlarında Dulcinea İçin Aşk Çılgınlıkları Yapma*
  17. *Köydeki Dostların Planı: Prenses Micomicona Kılığına Giren Kız*
  18. *Don Kişot'un Tahta Bir Kafese Kapatılıp Eve Büyülenmiş Olarak Getirilişi*
  19. *Üçüncü Sefer: Toboso'ya Gidiş ve Sancho'nun Çirkin Köylü Kızını Büyülü Dulcinea Diye Yutturması*
  20. *Ayna Şövalyesi ile Düello ve Don Kişot'un Şans eseri Zaferi*
  21. *Kafesteki Canlı Aslanla Karşılaşma ve Aslanın Sırtını Dönüp Uyuması*
  22. *Dük ve Düşes'in Sarayı: Sahte Şövalyelik Oyunlarıyla Eğlenme*
  23. *Sancho Panza'nın Barataria Adası Valiliği ve Bilgece Yargılamaları*
  24. *Ak Ay Şövalyesi (Köyün Bilgini Carrasco) ile Barselona Sahilinde Düello ve Yenilgi*
  25. *Yenilgi Şartı Olarak Eve Dönüş, Aklın Başa Gelmesi ve Huzurlu Bir Ölüm*

---

### 📖 Kitap 50: Robinson Crusoe
- **Kitap ID:** `book_50_robinson_crusoe`
- **Yazar:** Daniel Defoe
- **Seviye:** CEFR B1 | 25 Sayfa • 500 Cümle
- **25 Sayfalık Bölüm Akışı:**
  1. *York Kentinde Doğan Robinson'ın Babasının Sözünü Dinlemeyip Denizlere Kaçışı*
  2. *İlk Fırtına, Batış Tehlikesi ve Salé Korsanlarına Esir Düşüş*
  3. *İki Yıl Kölelikten Sonra Balıkçı Teknesiyle Kaçış ve Brezilya'ya Varış*
  4. *Brezilya'da Başarılı Şeker Kamışı Çiftçiliği ve Yeni Bir Ticaret Seferi*
  5. *Karayipler'de Korkunç Fırtına: Geminin Kayalara Çarpıp Batması*
  6. *Bütün Mürettebatın Boğulması ve Robinson'ın Issız Kumsala Çıkışı*
  7. *Ağaçta Geçirilen İlk Korku Dolu Gece ve Kıyıya Yaklaşan Gemi Enkazı*
  8. *Sal İnşa Edip Gemiden Tüfekler, Barut, Aletler, Ekmek ve Yelken Bezi Taşıma*
  9. *Yüksek Tepeden Çevreyi İnceleme: Denizlerle Çevrili Issız Bir Ada!*
  10. *Kayalık Yamaçta Çadır ve Kazıklarla Korunaklı Bir Kale İnşa Etme*
  11. *Tahtaya Çentik Atarak Zamanı Tutma ve Günlük Yazmaya Başlama*
  12. *Deprem, Şiddetli Humma Hastalığı ve İncil Okuyarak Tanrı'ya Sığınma*
  13. *Yabani Keçileri Evcilleştirme ve Süt, Peynir Üretimi*
  14. *Tesadüfen Dökülen Çantadan Çıkan İlk Arpa ve Pirinç Başakları*
  15. *Kilden Çömlek Yapmayı ve Ateşte Ekmek Pişirmeyi Başarmak*
  16. *Ağaç Gövdesini Oyarak Kanoculuk Denemesi ve Akıntıya Kapılma Korkusu*
  17. *On Beşinci Yıl: Kumsalda Görülen Tek Bir İnsan Ayak İzi ve Şok!*
  18. *Yıllarca Mağaralarda Korkuyla Saklanma ve Ek Savunma Duvarları*
  19. *Kumsalda Yamyamların Ateşi ve İnsan Kemikleri Kalıntıları*
  20. *Kurban Edilmek Üzereyken Kaçan Yerliyi Tüfekle Kurtarma*
  21. *Yeni Yoldaşa "Cuma" (Friday) İsmini Verme ve Ona İngilizce Öğretme*
  22. *Cuma'nın Sadakati, Medeniyeti Öğrenmesi ve Birlikte Yapılan Büyük Kano*
  23. *Yeni Yamyam Baskınında Bir İspanyol Denizci ve Cuma'nın Babasını Kurtarma*
  24. *Adaya Demir Atan İsyan Çıkmış İngiliz Gemisi ve Kaptana Yapılan Yardım*
  25. *İsyancıların Bastırılışı, Yirmi Sekiz Yıl Sonra İngiltere'ye Dönüş ve Zenginlik*

---

## 🚀 6. Çıktıyı Alıp Sisteme Getirdiğinizde Ne Yapacağız?

Gemini'den bir kitabın (örneğin `book_26_a_scandal_in_bohemia`) 25 sayfalık `.md` çıktısını aldığınızda işiniz bitti demektir!

Dosyayı proje içinde şu konuma kaydedin (veya içeriğini bana yapıştırın):
`lessons/book_26_a_scandal_in_bohemia/book_preview.md`

Benim hazırladığım otomatik dönüştürücü motor (`tools/build_from_markdown.py`) tek bir komutla:
1. Dosyadaki 25 sayfayı, 500 cümleyi ve 200 kelimeyi doğrular.
2. ReportLab ile **26 sayfalık (1 Kapak + 25 Hikaye Sayfası) profesyonel iki sütunlu PDF kitabını** basar.
3. Microsoft Edge Neural TTS ile **500 cümlenin stüdyo sesini** sentezler, milisaniye zamanlı `lesson.json` dosyasını üretir.
4. Hem **Web** (`Web/public/lessons/`) hem de **Android** (`Android/app/src/main/assets/lessons/`) klasörlerine kopyalar ve uygulamadaki ders seçiciye ekler.

Bu sayede hiçbir token veya API kotası harcamadan kütüphanemizi devasa bir hızla 50 kitaba ulaştıracağız! 🌟
