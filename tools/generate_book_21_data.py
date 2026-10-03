# -*- coding: utf-8 -*-
"""
Generator script for Book 21: "Around the World in Eighty Days" by Jules Verne.
15 Pages x 20 Sentences = Exactly 300 Sentences (Continuous IDs 1 to 300).
8 Vocabulary Focus items per page = Exactly 120 Target Vocabulary Items.
CEFR Level: A2-B1 Graded Reader Edition.
"""

import os

pages_data = [
    # Page 1 (Sentences 1-20)
    {
        "page_no": 1,
        "title": "Phileas Fogg and Passepartout at Savile Row",
        "tr_title": "Savile Row'da Dakik Beyefendi ve Uşağı",
        "vocab_focus": [
            ("punctual", "dakik, vaktine tam uyan"),
            ("eccentric", "sıra dışı, nev-i şahsına münhasır"),
            ("valet", "özel uşak"),
            ("chronometer", "hassas kronometre, saat"),
            ("routine", "günlük alışkanlık, düzen"),
            ("fireplace", "şömine"),
            ("gentleman", "beyefendi, soylu kişi"),
            ("clockwork", "saat gibi işleyen, dakik")
        ],
        "sentences": [
            {
                "id": 1,
                "text": "In the year 1872, the house at Number 7 Savile Row was inhabited by Mr. Phileas Fogg.",
                "translation": "1872 yılında, Savile Row yedi numaradaki evde Bay Phileas Fogg ikamet ediyordu.",
                "notes": "inhabit: ikamet etmek, yaşamak; Savile Row: Londra'da ünlü cadde"
            },
            {
                "id": 2,
                "text": "He was one of the most enigmatic and punctual gentlemen in all of London society.",
                "translation": "Tüm Londra sosyetesinin en esrarengiz ve en dakik beyefendilerinden biriydi.",
                "notes": "enigmatic: esrarengiz, gizemli; punctual: dakik"
            },
            {
                "id": 3,
                "text": "Little was known of his past, except that he was wealthy and exceptionally polite.",
                "translation": "Zengin ve son derece kibar olduğu dışında geçmişine dair pek az şey biliniyordu.",
                "notes": "exceptionally: fevkalade, son derece; polite: kibar"
            },
            {
                "id": 4,
                "text": "He never seemed to hurry, yet he was never a single second late for any engagement.",
                "translation": "Hiçbir zaman acele ediyor gibi görünmezdi, buna rağmen hiçbir randevusuna bir saniye bile gecikmezdi.",
                "notes": "hurry: acele etmek; engagement: randevu, buluşma"
            },
            {
                "id": 5,
                "text": "His daily routine was regulated with the mechanical precision of a fine astronomical clock.",
                "translation": "Günlük düzeni, hassas bir astronomik saatin mekanik kusursuzluğuyla ayarlanmıştı.",
                "notes": "precision: hassasiyet, dakiklik; daily routine: günlük rutin"
            },
            {
                "id": 6,
                "text": "He rose every morning at eight, took his tea at twenty past eight, and shaved at nine.",
                "translation": "Her sabah tam sekizde uyanır, sekizi yirmi geçe çayını içer ve dokuzda tıraş olurdu.",
                "notes": "twenty past eight: sekizi yirmi geçe; shave: tıraş olmak"
            },
            {
                "id": 7,
                "text": "On that very morning, October the second, he dismissed his servant for bringing shaving water at eighty-four degrees instead of eighty-six.",
                "translation": "Tam o sabah, yani iki Ekim'de, tıraş suyunu seksen altı derece yerine seksen dört derecede getirdiği için uşağını kovdu.",
                "notes": "dismiss: işten çıkarmak, kovmak; instead of: ... yerine"
            },
            {
                "id": 8,
                "text": "A new applicant arrived on the stroke of eleven to be interviewed for the post.",
                "translation": "Saat tam on birde, bu görev için mülakata girmek üzere yeni bir aday kapıyı çaldı.",
                "notes": "on the stroke of eleven: tam saat on bir vurduğunda; applicant: aday"
            },
            {
                "id": 9,
                "text": "He was an energetic thirty-year-old Frenchman named Jean Passepartout.",
                "translation": "Jean Passepartout adında otuz yaşlarında enerjik bir Fransız'dı.",
                "notes": "energetic: enerjik; thirty-year-old: otuz yaşında"
            },
            {
                "id": 10,
                "text": "\"I have had many trades, monsieur: circus rider, tightrope acrobat, and gym teacher,\" Passepartout explained.",
                "translation": "\"Pek çok meslek yaptım mösyö: sirk binicisi, ip cambazı ve jimnastik öğretmeni,\" diye açıkladı Passepartout.",
                "notes": "trade: meslek, zanaat; tightrope acrobat: ip cambazı"
            },
            {
                "id": 11,
                "text": "\"Now I desire only peace, regular hours, and a quiet master in foggy London.\"",
                "translation": "\"Artık sisli Londra'da yalnızca huzur, düzenli saatler ve sakin bir efendi arzuluyorum.\"",
                "notes": "desire: arzulamak; regular hours: düzenli mesai saatleri"
            },
            {
                "id": 12,
                "text": "Mr. Fogg consulted his pocket watch, which showed the hour, minute, and second.",
                "translation": "Bay Fogg saati, dakikayı ve saniyeyi gösteren cep saatine baktı.",
                "notes": "consult: danışmak, bakmak; pocket watch: cep saati"
            },
            {
                "id": 13,
                "text": "\"You suit me well,\" said Mr. Fogg calmly, \"your service begins this moment, at twenty-nine minutes past eleven.\"",
                "translation": "\"Bana gayet uygunsun,\" dedi Bay Fogg sakince, \"hizmetin tam şu an, saat on biri yirmi dokuz geçe başlıyor.\"",
                "notes": "suit well: gayet uygun olmak; calmly: sakince"
            },
            {
                "id": 14,
                "text": "Mr. Fogg took his hat, picked up his umbrella, and left the house for his club.",
                "translation": "Bay Fogg şapkasını aldı, şemsiyesini eline geçirdi ve kulübüne gitmek üzere evden çıktı.",
                "notes": "pick up: eline almak; umbrella: şemsiye"
            },
            {
                "id": 15,
                "text": "Passepartout inspected the quiet mansion, marveling at the neatness of every room.",
                "translation": "Passepartout her odanın düzenine hayran kalarak sessiz köşkü inceledi.",
                "notes": "marvel at: ...e hayran kalmak; neatness: düzen, intizam"
            },
            {
                "id": 16,
                "text": "On the wall hung a precise timetable outlining the master's entire day down to the minute.",
                "translation": "Duvarda, efendinin bütün gününü dakikası dakikasına özetleyen eksiksiz bir çizelge asılıydı.",
                "notes": "timetable: zaman çizelgesi; down to the minute: dakikası dakikasına"
            },
            {
                "id": 17,
                "text": "\"What a wonderful master!\" the Frenchman cried happily, rubbing his hands together.",
                "translation": "\"Ne harika bir efendi!\" diye haykırdı Fransız sevinçle, ellerini birbirine sürterek.",
                "notes": "rub hands: ellerini ovuşturmak; wonderful master: harika efendi"
            },
            {
                "id": 18,
                "text": "\"A living machine, a regular clockwork gentleman! I shall never have to travel again.\"",
                "translation": "\"Yaşayan bir makine, adeta saat gibi işleyen bir beyefendi! Artık asla seyahat etmek zorunda kalmayacağım.\"",
                "notes": "clockwork gentleman: saat gibi dakik beyefendi; travel: seyahat etmek"
            },
            {
                "id": 19,
                "text": "He unpacked his trunk and settled peacefully into his comfortable basement bedroom.",
                "translation": "Bavulunu açtı ve bodrum katındaki konforlu yatak odasına huzur içinde yerleşti.",
                "notes": "unpack trunk: bavulu boşaltmak; basement: bodrum katı"
            },
            {
                "id": 20,
                "text": "Little did he dream that before midnight, he would embark on the wildest voyage in human history.",
                "translation": "Gece yarısından önce insanlık tarihinin en çılgın yolculuğuna çıkacağını rüyasında bile göremezdi.",
                "notes": "embark on: ...e atılmak, çıkmak; wild voyage: çılgın seyahat"
            }
        ]
    },

    # Page 2 (Sentences 21-40)
    {
        "page_no": 2,
        "title": "The Wager at the Reform Club",
        "tr_title": "Reform Kulübü'ndeki Meşhur Bahis",
        "vocab_focus": [
            ("wager", "bahis, iddia"),
            ("bank robber", "banka soyguncusu"),
            ("telegram", "telgraf"),
            ("steamship", "buharlı gemi"),
            ("whist", "vist (popüler bir İngiliz iskambil oyunu)"),
            ("globe", "yerküre, dünya"),
            ("fortune", "servet"),
            ("bet", "bahse girmek")
        ],
        "sentences": [
            {
                "id": 21,
                "text": "At eleven-thirty, Phileas Fogg arrived at the prestigious Reform Club on Pall Mall.",
                "translation": "Saat on bir buçukta, Phileas Fogg Pall Mall caddesindeki saygın Reform Kulübü'ne vardı.",
                "notes": "prestigious: saygın, itibarlı; arrive at: ...e varmak"
            },
            {
                "id": 22,
                "text": "He ate lunch in the grand dining room and spent the afternoon reading the London newspapers.",
                "translation": "Görkemli yemek salonunda öğle yemeğini yedi ve öğleden sonrasını Londra gazetelerini okuyarak geçirdi.",
                "notes": "dining room: yemek salonu; spend time: zaman geçirmek"
            },
            {
                "id": 23,
                "text": "All the journals were discussing the sensational robbery of fifty-five thousand pounds from the Bank of England.",
                "translation": "Bütün gazeteler, İngiltere Merkez Bankası'ndan çalınan elli beş bin sterlinlik sansasyonel soygunu tartışıyordu.",
                "notes": "sensational robbery: sansasyonel soygun; Bank of England: İngiltere Bankası"
            },
            {
                "id": 24,
                "text": "At six o'clock, Fogg's usual whist partners joined him around the green card table.",
                "translation": "Saat tam altıda, Fogg'un mutat vist ortakları yeşil oyun masasının etrafında ona katıldılar.",
                "notes": "usual partners: alışılmış ortaklar; card table: iskambil masası"
            },
            {
                "id": 25,
                "text": "\"The robber must be a clever gentleman,\" remarked Andrew Stuart, an engineer.",
                "translation": "\"Soyguncu zeki bir beyefendi olmalı,\" dedi mühendis Andrew Stuart.",
                "notes": "remark: belirtmek, ifade etmek; clever gentleman: zeki beyefendi"
            },
            {
                "id": 26,
                "text": "\"The world is vast enough for him to hide anywhere without ever being captured.\"",
                "translation": "\"Dünya, yakalanmadan herhangi bir yerde saklanabilmesi için fazlasıyla geniş.\"",
                "notes": "vast: uçsuz bucaksız, devasa; capture: yakalamak"
            },
            {
                "id": 27,
                "text": "\"It was vast once,\" Mr. Fogg replied quietly while shuffling the deck of cards.",
                "translation": "\"Eskiden genişti,\" diye sakince cevap verdi Bay Fogg, iskambil destesini kararken.",
                "notes": "shuffle deck: desteyi karmak; quietly: sessizce, sakince"
            },
            {
                "id": 28,
                "text": "\"What do you mean, once? Has the earth grown smaller?\" laughed another partner.",
                "translation": "\"Eskiden derken neyi kastediyorsunuz? Dünya küçüldü mü yoksa?\" diye güldü diğer bir ortak.",
                "notes": "grow smaller: küçülmek; what do you mean: ne demek istiyorsun?"
            },
            {
                "id": 29,
                "text": "\"Certainly,\" Fogg insisted, \"a man can now circle the globe ten times faster than a hundred years ago.\"",
                "translation": "\"Elbette,\" diye ısrar etti Fogg, \"bir insan artık yerküreyi yüz yıl öncesine göre on kat daha hızlı turlayabilir.\"",
                "notes": "circle the globe: dünyayı dolaşmak; insist: ısrar etmek"
            },
            {
                "id": 30,
                "text": "\"The Morning Chronicle has published a precise calculation showing it can be done in eighty days.\"",
                "translation": "\"Morning Chronicle gazetesi, bunun seksen günde yapılabileceğini gösteren kesin bir hesaplama yayımladı.\"",
                "notes": "calculation: hesaplama; publish: yayımlamak"
            },
            {
                "id": 31,
                "text": "\"That calculation ignores storms, shipwrecks, train derailments, and bad weather!\" Stuart argued.",
                "translation": "\"O hesaplama fırtınaları, gemi kazalarını, tren raydan çıkmalarını ve kötü havayı hiçe sayıyor!\" diye itiraz etti Stuart.",
                "notes": "ignore: görmezden gelmek, saymamak; shipwreck: gemi kazası"
            },
            {
                "id": 32,
                "text": "\"It includes everything,\" Fogg answered steadily, playing his card.",
                "translation": "\"Her şeyi kapsıyor,\" diye kararlı bir tonda yanıt verdi Fogg, kağıdını atarken.",
                "notes": "steadily: kararlılıkla, sarsılmadan; play card: kağıt oynamak"
            },
            {
                "id": 33,
                "text": "\"I will wager four thousand pounds that such a journey is impossible!\" Stuart cried.",
                "translation": "\"Böyle bir yolculuğun imkansız olduğuna dört bin sterlinine bahse girerim!\" diye bağırdı Stuart.",
                "notes": "wager: bahse girmek; impossible: imkansız"
            },
            {
                "id": 34,
                "text": "\"I will bet twenty thousand pounds against anyone that I will make the tour of the world in eighty days or less,\"",
                "translation": "\"Dünya turunu seksen gün veya daha kısa sürede yapacağıma isteyen herkese karşı yirmi bin sterlinimi ortaya koyarım,\"",
                "notes": "bet against: ...e karşı bahse girmek; make the tour: tur yapmak"
            },
            {
                "id": 35,
                "text": "Fogg announced without a trace of emotion on his composed face.",
                "translation": "dedi Fogg, vakur yüzünde en ufak bir duygu kırıntısı bile belirmeden.",
                "notes": "without a trace of emotion: duygu belirtisi olmadan; composed: vakur, sakin"
            },
            {
                "id": 36,
                "text": "The five gentlemen looked at him in shock: twenty thousand pounds was half of his entire fortune.",
                "translation": "Beş beyefendi şaşkınlıkla ona baktı: yirmi bin sterlin onun bütün servetinin tam yarısıydı.",
                "notes": "in shock: şok içinde; entire fortune: tüm servet"
            },
            {
                "id": 37,
                "text": "\"We accept the wager,\" they agreed after whispering among themselves.",
                "translation": "\"Bahsi kabul ediyoruz,\" diyerek aralarında fısıldaştıktan sonra onayladılar.",
                "notes": "accept wager: bahsi kabul etmek; whisper: fısıldaşmak"
            },
            {
                "id": 38,
                "text": "\"Today is Wednesday, October the second,\" Mr. Fogg said, checking his notebook.",
                "translation": "\"Bugün iki Ekim Çarşamba,\" dedi Bay Fogg not defterini kontrol ederek.",
                "notes": "check notebook: not defterini kontrol etmek"
            },
            {
                "id": 39,
                "text": "\"I shall be back in this very room on Saturday, December the twenty-first, at eight forty-five in the evening.\"",
                "translation": "\"Yirmi bir Aralık Cumartesi günü, akşam sekizi kırk beş geçe tam bu odada olacağım.\"",
                "notes": "be back: geri dönmek; in the evening: akşamleyin"
            },
            {
                "id": 40,
                "text": "\"If I am not, the twenty thousand pounds in my bank account belongs to you, gentlemen.\"",
                "translation": "\"Eğer olmazsam, banka hesabımdaki yirmi bin sterlin sizindir beyler.\"",
                "notes": "bank account: banka hesabı; belong to: ...e ait olmak"
            }
        ]
    },

    # Page 3 (Sentences 41-60)
    {
        "page_no": 3,
        "title": "The Departure from London to Suez",
        "tr_title": "Londra'dan Süveyş Kanalı'na Çıkış",
        "vocab_focus": [
            ("carpetbag", "seyahat çantası, halı çanta"),
            ("banknotes", "banknotlar, kağıt para"),
            ("gas jet", "gaz lambası musluğu"),
            ("cab", "kiralık fayton, atlı araba"),
            ("platform", "peron, istasyon peronu"),
            ("passport", "pasaport"),
            ("consul", "konsolos"),
            ("steamer", "buharlı gemi")
        ],
        "sentences": [
            {
                "id": 41,
                "text": "At seven-fifty, Phileas Fogg won the final game of whist, collected his winnings, and walked home.",
                "translation": "Yediyi elli geçe Phileas Fogg son vist oyununu kazandı, kazancını cebine koydu ve eve doğru yürüdü.",
                "notes": "collect winnings: kazancını toplamak; walk home: eve yürümek"
            },
            {
                "id": 42,
                "text": "Passepartout was astonished to see his master return home hours ahead of his timetable.",
                "translation": "Passepartout, efendisinin zaman çizelgesinden saatler önce eve döndüğünü görünce şaşkına döndü.",
                "notes": "astonished: hayretler içinde; ahead of timetable: çizelgenin önünde"
            },
            {
                "id": 43,
                "text": "\"We leave for Dover and Calais in ten minutes,\" Mr. Fogg announced calmly.",
                "translation": "\"On dakika içinde Dover ve Calais'ye gitmek üzere yola çıkıyoruz,\" dedi Bay Fogg sakince.",
                "notes": "leave for: ...e gitmek üzere ayrılmak; calmly: sakince"
            },
            {
                "id": 44,
                "text": "\"We are going around the world!\" the master added without blinking an eye.",
                "translation": "\"Dünyanın etrafını dolaşacağız!\" diye ekledi efendi, gözünü bile kırpmadan.",
                "notes": "around the world: dünya turu; without blinking: göz kırpmadan"
            },
            {
                "id": 45,
                "text": "Passepartout's eyes widened in utter disbelief, his jaw dropping to his chest.",
                "translation": "Passepartout'nun gözleri mutlak bir inanamazlıkla açıldı, ağzı bir karış açık kaldı.",
                "notes": "jaw drop: ağzı açık kalmak; in disbelief: inanmayarak"
            },
            {
                "id": 46,
                "text": "\"Around the world... in eighty days?\" stammered the bewildered Frenchman.",
                "translation": "\"Dünyanın etrafı mı... seksen günde mi?\" diye kekeledi şaşkına dönen Fransız.",
                "notes": "stammer: kekelemek; bewildered: şaşkın, afallamış"
            },
            {
                "id": 47,
                "text": "\"Yes, in eighty days,\" Fogg replied, \"so we haven't a single moment to lose.\"",
                "translation": "\"Evet, seksen günde,\" diye yanıtladı Fogg, \"bu yüzden kaybedecek tek bir anımız bile yok.\"",
                "notes": "not a single moment to lose: kaybedecek tek bir an bile yok"
            },
            {
                "id": 48,
                "text": "\"Pack no trunks; take only a carpetbag with two shirts and three pairs of stockings.\"",
                "translation": "\"Bavul hazırlama; sadece iki gömlek ve üç çift çorap içeren bir seyahat çantası al.\"",
                "notes": "carpetbag: halı heybe / seyahat çantası; stockings: çoraplar"
            },
            {
                "id": 49,
                "text": "Fogg opened a strongbox and pulled out a thick bundle of Bank of England banknotes.",
                "translation": "Fogg bir para kasasını açtı ve kalın bir deste İngiltere Bankası banknotu çıkardı.",
                "notes": "strongbox: para kasası; bundle: deste, demet"
            },
            {
                "id": 50,
                "text": "He placed twenty thousand pounds in cash into the carpetbag to cover all travel expenses.",
                "translation": "Tüm seyahat masraflarını karşılamak üzere seyahat çantasına yirmi bin sterlin nakit para koydu.",
                "notes": "in cash: nakit olarak; travel expenses: seyahat masrafları"
            },
            {
                "id": 51,
                "text": "Passepartout grabbed the heavy bag, his head spinning with confusion and dread.",
                "translation": "Passepartout kafa karışıklığı ve endişeyle başı dönerek ağır çantayı kavradı.",
                "notes": "head spinning: başı dönerek; confusion: şaşkınlık, kafa karışıklığı"
            },
            {
                "id": 52,
                "text": "Just as they shut the street door, Passepartout gave a sudden gasp of horror.",
                "translation": "Tam sokak kapısını kapattıkları sırada, Passepartout dehşetle aniden nefesini tuttu.",
                "notes": "gasp of horror: dehşetle nefesi kesilmek; shut the door: kapıyı kapatmak"
            },
            {
                "id": 53,
                "text": "He had left the gas jet burning in his bedroom, which would run at his own expense until their return!",
                "translation": "Yatak odasındaki gaz lambasını açık unutmuştu; bu da dönene kadar kendi cebine yazacaktı!",
                "notes": "gas jet: gaz lambası musluğu; at one's own expense: kendi masrafına"
            },
            {
                "id": 54,
                "text": "At Charing Cross station, a crowd was waiting to watch the mysterious gentleman depart.",
                "translation": "Charing Cross istasyonunda, gizemli beyefendinin ayrılışını izlemek için bir kalabalık bekliyordu.",
                "notes": "crowd: kalabalık; depart: hareket etmek, yola çıkmak"
            },
            {
                "id": 55,
                "text": "Fogg bought two first-class tickets to Paris and stepped calmly aboard the express train.",
                "translation": "Fogg Paris'e iki birinci mevki bilet satın aldı ve sakince ekspres trene bindi.",
                "notes": "first-class ticket: birinci mevki bilet; step aboard: trene / gemiye binmek"
            },
            {
                "id": 56,
                "text": "The whistle shrieked, the engine puffed steam, and the journey of eighty days commenced.",
                "translation": "Düdük çaldı, lokomotif buhar püskürttü ve seksen günlük yolculuk resmen başladı.",
                "notes": "whistle shriek: düdük çalmak / ötmek; commence: başlamak"
            },
            {
                "id": 57,
                "text": "They crossed the English Channel smoothly and reached Paris by early morning.",
                "translation": "Manş Denizi'ni sarsıntısız geçtiler ve sabahın erken saatlerinde Paris'e ulaştılar.",
                "notes": "English Channel: Manş Denizi; smoothly: sorunsuzca"
            },
            {
                "id": 58,
                "text": "From Paris, the railway carried them across the snowy Alps through the Mont Cenis tunnel into Italy.",
                "translation": "Paris'ten demiryolu onları Mont Cenis tünelinden karlı Alpler'i aşırıp İtalya'ya ulaştırdı.",
                "notes": "snowy Alps: karlı Alpler; railway: demiryolu"
            },
            {
                "id": 59,
                "text": "At Brindisi, they boarded the steamer Mongolia, sailing across the Mediterranean Sea toward Egypt.",
                "translation": "Brindisi'de Mongolia buharlısına bindiler ve Akdeniz üzerinden Mısır'a doğru yelken açtılar.",
                "notes": "board the steamer: buharlı gemiye binmek; Mediterranean Sea: Akdeniz"
            },
            {
                "id": 60,
                "text": "On October the ninth, precisely on schedule, the Mongolia dropped anchor in the harbor of Suez.",
                "translation": "Dokuz Ekim'de, tam vaktinde ve programa uygun olarak Mongolia Süveyş limanına demir attı.",
                "notes": "on schedule: zamanında, plana uygun; drop anchor: demir atmak"
            }
        ]
    },

    # Page 4 (Sentences 61-80)
    {
        "page_no": 4,
        "title": "Detective Fix on the Trail",
        "tr_title": "Dedektif Fix'in Süveyş'teki Şüphesi",
        "vocab_focus": [
            ("detective", "dedektif, sivil polis"),
            ("warrant", "tutuklama müzekkeresi, yakalama emri"),
            ("telegraph", "telgraf çekmek / telgraf cihazı"),
            ("quay", "rıhtım, iskele"),
            ("thief", "hırsız"),
            ("visage", "yüz, çehre"),
            ("consulate", "konsolosluk"),
            ("arrest", "tutuklamak")
        ],
        "sentences": [
            {
                "id": 61,
                "text": "Waiting on the quay of Suez was a nervous, sharp-eyed little man named Inspector Fix.",
                "translation": "Süveyş rıhtımında Müfettiş Fix adında gergin, keskin gözlü ufak tefek bir adam bekliyordu.",
                "notes": "quay: rıhtım; sharp-eyed: keskin gözlü; inspector: müfettiş, komiser"
            },
            {
                "id": 62,
                "text": "He was a detective sent from Scotland Yard to watch for the Bank of England robber.",
                "translation": "İngiltere Bankası soyguncusunu gözetlemek üzere Scotland Yard'dan gönderilmiş bir dedektifti.",
                "notes": "Scotland Yard: Londra polis teşkilatı; watch for: gözetlemek"
            },
            {
                "id": 63,
                "text": "The robber had been described as an aristocratic gentleman traveling alone with lavish sums of cash.",
                "translation": "Soyguncu, yanında yüklü miktarda nakit parayla tek başına seyahat eden aristokrat bir beyefendi olarak tarif edilmişti.",
                "notes": "lavish sum: yüklü miktar; aristocratic: soylu, aristokrat"
            },
            {
                "id": 64,
                "text": "When Phileas Fogg stepped off the steamer to have his passport stamped, Fix gasped.",
                "translation": "Phileas Fogg pasaportuna damga vurdurmak için buharlıdan indiğinde Fix'in soluğu kesildi.",
                "notes": "have passport stamped: pasaportuna damga vurdurmak; gasp: soluğu kesilmek"
            },
            {
                "id": 65,
                "text": "Fogg's cold composure, elegant clothes, and wealthy air matched the telegraphic description perfectly.",
                "translation": "Fogg'un soğuk sükuneti, şık kıyafetleri ve zengin edası telgraftaki tarife tıpatıp uyuyordu.",
                "notes": "cold composure: soğuk sükunet; match perfectly: kusursuz uymak"
            },
            {
                "id": 66,
                "text": "\"He must be the bank robber escaping to India!\" Fix whispered to himself triumphantly.",
                "translation": "\"Hindistan'a kaçan banka soyguncusu bu adam olmalı!\" diye fısıldadı Fix kendi kendine zaferle.",
                "notes": "triumphantly: zafer edasıyla; bank robber: banka soyguncusu"
            },
            {
                "id": 67,
                "text": "Fix followed Passepartout to the British consulate and struck up an innocent conversation.",
                "translation": "Fix İngiliz konsolosluğuna kadar Passepartout'yu takip etti ve masum bir sohbet başlattı.",
                "notes": "strike up conversation: sohbet başlatmak; consulate: konsolosluk"
            },
            {
                "id": 68,
                "text": "The honest Frenchman proudly showed Fix the heavy carpetbag containing twenty thousand pounds.",
                "translation": "Dürüst Fransız, içinde yirmi bin sterlin bulunan ağır heybeyi gururla Fix'e gösterdi.",
                "notes": "proudly: gururla; heavy carpetbag: ağır seyahat çantası"
            },
            {
                "id": 69,
                "text": "\"My master is traveling around the world in eighty days on a foolish wager!\" Passepartout explained.",
                "translation": "\"Efendim saçma bir iddia uğruna seksen günde dünyanın etrafını dolaşıyor!\" diye açıkladı Passepartout.",
                "notes": "foolish wager: ahmakça bahis; around the world: dünya turu"
            },
            {
                "id": 70,
                "text": "This confession convinced Fix that the wager was merely a clever excuse to flee justice.",
                "translation": "Bu itiraf Fix'i, bahsin yalnızca adaletten kaçmak için uydurulmuş zekice bir bahane olduğuna inandırdı.",
                "notes": "confession: itiraf; flee justice: adaletten kaçmak; excuse: bahane"
            },
            {
                "id": 71,
                "text": "Fix immediately sent an urgent telegraph to London requesting a warrant of arrest in Bombay.",
                "translation": "Fix derhal Londra'ya Bombay'da geçerli bir tutuklama müzekkeresi talep eden acil bir telgraf çekti.",
                "notes": "urgent telegraph: acil telgraf; warrant of arrest: tutuklama kararı"
            },
            {
                "id": 72,
                "text": "He bought a ticket on the Mongolia, resolving not to let the suspect out of his sight.",
                "translation": "Şüpheliyi gözünün önünden ayırmamaya ant içerek Mongolia gemisine bir bilet satın aldı.",
                "notes": "suspect: şüpheli kişi; out of sight: gözden ırak"
            },
            {
                "id": 73,
                "text": "The steamer glided through the newly opened Suez Canal into the scorching Red Sea.",
                "translation": "Buharlı gemi yeni açılmış Süveyş Kanalı'ndan geçerek kavurucu Kızıldeniz'e süzüldü.",
                "notes": "glide through: içinden süzülmek; scorching: kavurucu, çok sıcak"
            },
            {
                "id": 74,
                "text": "The heat was stifling, but Phileas Fogg remained seated in the saloon playing whist.",
                "translation": "Sıcaklık boğucuydu fakat Phileas Fogg salonda oturup vist oynamayı sürdürdü.",
                "notes": "stifling heat: boğucu sıcak; saloon: gemi salonu"
            },
            {
                "id": 75,
                "text": "He never looked at the dramatic shores of Arabia or the distant mountains of Africa.",
                "translation": "Arabistan'ın etkileyici kıyılarına veya Afrika'nın uzak dağlarına bir kez olsun bakmadı.",
                "notes": "dramatic shores: etkileyici kıyılar; distant mountains: uzak dağlar"
            },
            {
                "id": 76,
                "text": "To him, every country was merely a hurdle to be crossed without delay.",
                "translation": "Onun için her ülke, gecikmeden aşılması gereken bir engelden ibaretti.",
                "notes": "hurdle: engel; without delay: gecikmeksizin"
            },
            {
                "id": 77,
                "text": "Passepartout, on the other hand, enjoyed the sea breeze and chatted with Fix daily.",
                "translation": "Passepartout ise diğer yandan deniz melteminin tadını çıkarıyor ve her gün Fix ile sohbet ediyordu.",
                "notes": "sea breeze: deniz esintisi; chat daily: her gün sohbet etmek"
            },
            {
                "id": 78,
                "text": "The detective pretended to be a fellow traveler heading toward the Far East.",
                "translation": "Dedektif Uzak Doğu'ya doğru seyahat eden bir yolcu gibi davrandı.",
                "notes": "pretend: -miş gibi davranmak; fellow traveler: yol arkadaşı"
            },
            {
                "id": 79,
                "text": "The Mongolia navigated the Indian Ocean at full steam, making excellent speed.",
                "translation": "Mongolia Hint Okyanusu'nda tam yol ilerleyerek mükemmel bir hız yakaladı.",
                "notes": "at full steam: tam yol, bütün gücüyle; navigate: yol almak"
            },
            {
                "id": 80,
                "text": "On October the twentieth, the ship berthed at Bombay two days ahead of schedule.",
                "translation": "Yirmi Ekim'de gemi, takvimin iki gün önünde Bombay rıhtımına yanaştı.",
                "notes": "berth: rıhtıma yanaşmak; ahead of schedule: takvimin önünde"
            }
        ]
    },

    # Page 5 (Sentences 81-100)
    {
        "page_no": 5,
        "title": "The Steamship Mongolia to Bombay",
        "tr_title": "Moğolistan Buharlısıyla Bombay'a Varış",
        "vocab_focus": [
            ("pagoda", "pagoda, tapınak"),
            ("priest", "rahip, din adamı"),
            ("shoes", "ayakkabılar"),
            ("sacred", "kutsal"),
            ("railway station", "tren garı"),
            ("ticket", "bilet"),
            ("chase", "kovalamaca, takip"),
            ("furious", "öfkeli, hiddetli")
        ],
        "sentences": [
            {
                "id": 81,
                "text": "Phileas Fogg recorded the gained two days in his notebook with cool satisfaction.",
                "translation": "Phileas Fogg kazanılan iki günü serinkanlı bir memnuniyetle not defterine kaydetti.",
                "notes": "cool satisfaction: serinkanlı memnuniyet; record: kaydetmek"
            },
            {
                "id": 82,
                "text": "He instructed Passepartout to purchase train tickets for Calcutta, departing at eight that evening.",
                "translation": "Passepartout'ya o akşam sekizde kalkacak Kalküta trenine bilet almasını tembihledi.",
                "notes": "instruct: talimat vermek; depart: hareket etmek"
            },
            {
                "id": 83,
                "text": "Fix rushed directly to the police headquarters in Bombay to obtain his arrest warrant.",
                "translation": "Fix tutuklama müzekkeresini almak için doğrudan Bombay polis merkezine koştu.",
                "notes": "police headquarters: polis karargahı; obtain: temin etmek, almak"
            },
            {
                "id": 84,
                "text": "To his dismay, the warrant had not arrived from London yet; he was powerless to act.",
                "translation": "Büyük bir hayal kırıklığıyla gördü ki müzekkere henüz Londra'dan ulaşmamıştı; müdahale edemezdi.",
                "notes": "to one's dismay: hayal kırıklığıyla; powerless: çaresiz, yetkisiz"
            },
            {
                "id": 85,
                "text": "Meanwhile, Passepartout was wandering through the vibrant, crowded streets of Bombay.",
                "translation": "Bu sırada Passepartout Bombay'ın cıvıl cıvıl, kalabalık sokaklarında dolaşıyordu.",
                "notes": "wander: avare dolaşmak; vibrant: hayat dolu, capcanlı"
            },
            {
                "id": 86,
                "text": "He marveled at sacred cows, colorful turbans, and fragrant spice markets.",
                "translation": "Kutsal ineklere, rengarenk sarıklara ve mis kokulu baharat pazarlarına hayran kaldı.",
                "notes": "sacred cow: kutsal inek; fragrant: hoş kokulu; turban: sarık"
            },
            {
                "id": 87,
                "text": "Passing the magnificent temple of Malebar Hill, curiosity overcame his common sense.",
                "translation": "Görkemli Malebar Hill tapınağının önünden geçerken merakı sağduyusuna baskın geldi.",
                "notes": "curiosity: merak; overcome common sense: sağduyuya galip gelmek"
            },
            {
                "id": 88,
                "text": "He entered the holy pagoda without removing his shoes, completely ignorant of Indian law.",
                "translation": "Hint yasalarından bihaber olarak ayakkabılarını çıkarmadan kutsal pagodaya adım attı.",
                "notes": "ignorant of law: yasadan habersiz; remove shoes: ayakkabıları çıkarmak"
            },
            {
                "id": 89,
                "text": "Three enraged Hindu priests pounced upon him with furious cries of sacrilege.",
                "translation": "Öfkeden kuduran üç Hindu rahip kutsala saygısızlık haykırışlarıyla üzerine çullandı.",
                "notes": "enraged: çılgına dönmüş; sacrilege: kutsala saygısızlık"
            },
            {
                "id": 90,
                "text": "They tore off his shoes and tried to beat him with heavy sticks.",
                "translation": "Ayakkabılarını ayağından çekip aldılar ve kalın sopalarla onu dövmeye kalkıştılar.",
                "notes": "tear off: çekip koparmak; heavy sticks: kalın sopalar"
            },
            {
                "id": 91,
                "text": "Passepartout used his old circus acrobatics to knock down two priests and bolted away.",
                "translation": "Passepartout eski sirk akrobasi yeteneklerini kullanarak iki rahibi devirdi ve tabanları yağladı.",
                "notes": "bolt away: hızla kaçmak; knock down: yere sermek"
            },
            {
                "id": 92,
                "text": "He ran shoeless and panting all the way to the railway station.",
                "translation": "Tren garına kadar yol boyunca yalınayak ve soluk soluğa koştu.",
                "notes": "shoeless: yalınayak; pant: nefes nefese kalmak"
            },
            {
                "id": 93,
                "text": "He arrived five minutes before eight and confessed his foolish adventure to Mr. Fogg.",
                "translation": "Saat sekize beş kala gara ulaştı ve ahmakça macerasını Bay Fogg'a itiraf etti.",
                "notes": "confess adventure: macerasını itiraf etmek; foolish: ahmakça"
            },
            {
                "id": 94,
                "text": "\"You were foolish,\" Fogg said calmly, \"but here is the train; take your seat.\"",
                "translation": "\"Ahmaklık etmişsin,\" dedi Fogg sakince, \"fakat işte tren geldi; yerine otur.\"",
                "notes": "take seat: yerine oturmak; calmly: sakince"
            },
            {
                "id": 95,
                "text": "Lurking behind a pillar, Detective Fix had overheard the entire incident.",
                "translation": "Bir sütunun arkasına gizlenen Dedektif Fix bütün olaya kulak misafiri olmuştu.",
                "notes": "lurk behind: arkasında pusmak; pillar: sütun"
            },
            {
                "id": 96,
                "text": "\"A religious crime in British India!\" Fix thought gleefully, rubbing his hands.",
                "translation": "\"İngiliz Hindistanı'nda dini bir suç!\" diye düşündü Fix ellerini sevinçle ovuşturarak.",
                "notes": "gleefully: neşeyle, keyifle; religious crime: dini suç"
            },
            {
                "id": 97,
                "text": "\"I can have them arrested in Calcutta for desecrating a temple while waiting for my warrant!\"",
                "translation": "\"Müzekkeremi beklerken bir tapınağa saygısızlık ettikleri gerekçesiyle onları Kalküta'da tutuklatabilirim!\"",
                "notes": "desecrate: kutsala saygısızlık etmek; while waiting: beklerken"
            },
            {
                "id": 98,
                "text": "Fix immediately boarded the same train, resolved to follow the travelers across India.",
                "translation": "Fix, yolcuları Hindistan boyunca takip etmeye kararlı olarak derhal aynı trene bindi.",
                "notes": "resolved: kararlı; follow across: boyunca takip etmek"
            },
            {
                "id": 99,
                "text": "The locomotive gave a mighty whistle and plunged into the dark jungle night.",
                "translation": "Lokomotif güçlü bir düdük çaldı ve ormanın karanlık gecesine daldı.",
                "notes": "mighty whistle: güçlü düdük; plunge into: içine dalmak"
            },
            {
                "id": 100,
                "text": "The great journey across the vast Indian subcontinent had commenced.",
                "translation": "Büyük Hint yarımadasını boydan boya kat edecek muazzam yolculuk başlamıştı.",
                "notes": "subcontinent: alt kıta; vast: uçsuz bucaksız"
            }
        ]
    },

    # Page 6 (Sentences 101-120)
    {
        "page_no": 6,
        "title": "The Great Railway Journey Across India",
        "tr_title": "Hindistan Demiryolunda Beklenmedik Engel",
        "vocab_focus": [
            ("railway", "demiryolu"),
            ("unfinished", "tamamlanmamış, eksik"),
            ("conductor", "kondüktör, bilet memuru"),
            ("obstacle", "engel"),
            ("elephant", "fil"),
            ("howdah", "fil sırtındaki oturak / semer"),
            ("guide", "rehber"),
            ("jungle", "balta girmemiş orman")
        ],
        "sentences": [
            {
                "id": 101,
                "text": "The Great Indian Peninsula Railway rolled swiftly through the dramatic mountains of the Western Ghats.",
                "translation": "Büyük Hint Yarımadası Demiryolu, Batı Gat Dağları'nın etkileyici zirveleri arasından hızla aktı.",
                "notes": "roll swiftly: hızla akıp gitmek; dramatic mountains: sarp dağlar"
            },
            {
                "id": 102,
                "text": "In their carriage sat Sir Francis Cromarty, a British army general stationed in India.",
                "translation": "Kompartımanlarında Hindistan'da görevli bir İngiliz ordusu generali olan Sir Francis Cromarty oturuyordu.",
                "notes": "carriage: vagon, kompartıman; stationed: görevli, konuşlanmış"
            },
            {
                "id": 103,
                "text": "He struck up a conversation with Fogg and was amazed by the gentleman's absolute composure.",
                "translation": "Fogg ile bir sohbet başlattı ve bu beyefendinin mutlak sükuneti karşısında hayrete düştü.",
                "notes": "absolute composure: mutlak sükunet; amazed: hayrete düşmüş"
            },
            {
                "id": 104,
                "text": "At eight the next morning, the train suddenly hissed to a complete stop in the middle of nowhere.",
                "translation": "Ertesi sabah saat sekizde, tren ıssızlığın ortasında tıslayarak aniden tamamen durdu.",
                "notes": "in the middle of nowhere: ıssızlığın / hiçliğin ortasında; hiss to a stop: tıslayarak durmak"
            },
            {
                "id": 105,
                "text": "\"All passengers must get out here!\" the railway conductor shouted down the corridor.",
                "translation": "\"Bütün yolcular burada inmek zorunda!\" diye koridor boyunca bağırdı tren kondüktörü.",
                "notes": "passenger: yolcu; conductor: biletçi, kondüktör"
            },
            {
                "id": 106,
                "text": "\"Why are we stopping at this wretched hamlet?\" asked Sir Francis in great surprise.",
                "translation": "\"Bu sefil köyde neden duruyoruz?\" diye sordu Sir Francis büyük bir şaşkınlıkla.",
                "notes": "wretched hamlet: sefil mezra; great surprise: büyük şaşkınlık"
            },
            {
                "id": 107,
                "text": "\"The railway line is unfinished,\" the conductor replied coolly, shrugging his shoulders.",
                "translation": "\"Demiryolu hattı tamamlanmadı,\" diye yanıtladı kondüktör kayıtsızca, omuzlarını silkerek.",
                "notes": "shrug shoulders: omuz silkmek; unfinished line: tamamlanmamış hat"
            },
            {
                "id": 108,
                "text": "\"There is a gap of fifty miles from here to Allahabad, where the track begins again.\"",
                "translation": "\"Buradan rayların yeniden başladığı Allahabad'a kadar elli millik bir boşluk var.\"",
                "notes": "gap: boşluk, kesinti; track: tren rayı"
            },
            {
                "id": 109,
                "text": "\"Yet the newspapers in London declared the line open!\" Sir Francis cried angrily.",
                "translation": "\"Ama Londra'daki gazeteler hattın açıldığını ilan etmişti!\" diye öfkeyle haykırdı Sir Francis.",
                "notes": "declare: ilan etmek; angrily: öfkeyle"
            },
            {
                "id": 110,
                "text": "\"The papers were mistaken,\" the conductor smiled, \"passengers must find their own conveyance.\"",
                "translation": "\"Gazeteler yanılmış,\" diye gülümsedi kondüktör, \"yolcular kendi araçlarını kendileri bulmalı.\"",
                "notes": "be mistaken: yanılmış olmak; conveyance: taşıt aracı"
            },
            {
                "id": 111,
                "text": "Passepartout was ready to strangle the conductor, his face red with fury.",
                "translation": "Passepartout öfkeden kıpkırmızı kesilmiş yüzüyle kondüktörü boğmaya hazırdı.",
                "notes": "strangle: boğmak; red with fury: öfkeden kıpkırmızı"
            },
            {
                "id": 112,
                "text": "Phileas Fogg, however, did not show the slightest sign of vexation or anger.",
                "translation": "Oysa Phileas Fogg en ufak bir can sıkıntısı veya öfke belirtisi bile göstermedi.",
                "notes": "slightest sign: en ufak işaret; vexation: can sıkıntısı"
            },
            {
                "id": 113,
                "text": "\"We have two days in hand,\" Fogg said calmly, \"an obstacle was foreseen; it will be overcome.\"",
                "translation": "\"Elimizde fazladan iki gün var,\" dedi Fogg sakince, \"bir engel çıkacağı öngörülmüştü; aşılacaktır.\"",
                "notes": "in hand: elde, cepte; foresee: önceden görmek, öngörmek"
            },
            {
                "id": 114,
                "text": "All the horses, carts, and oxen in the village had already been hired by other travelers.",
                "translation": "Köydeki bütün atlar, arabalar ve öküzler diğer yolcular tarafından çoktan kiralanmıştı.",
                "notes": "oxen: öküzler; cart: kağnı, at arabası"
            },
            {
                "id": 115,
                "text": "Passepartout discovered an Indian villager who owned a magnificent trained elephant named Kiouni.",
                "translation": "Passepartout, Kiouni adında eğitimli muazzam bir file sahip bir Hintli köylü buldu.",
                "notes": "trained elephant: eğitimli fil; magnificent: görkemli"
            },
            {
                "id": 116,
                "text": "The owner initially refused to hire the beast, suspecting the Englishmen would mistreat it.",
                "translation": "Sahibi başlangıçta İngilizlerin hayvana kötü davranacağından şüphelenerek hayvanı kiralamayı reddetti.",
                "notes": "initially: başlangıçta; beast: hayvan, canavar"
            },
            {
                "id": 117,
                "text": "Mr. Fogg offered one thousand, then fifteen hundred, and finally two thousand pounds to purchase the elephant outright.",
                "translation": "Bay Fogg fili doğrudan satın almak için önce bin, sonra bin beş yüz, nihayetinde iki bin sterlin teklif etti.",
                "notes": "purchase outright: doğrudan peşin satın almak; offer: teklif etmek"
            },
            {
                "id": 118,
                "text": "The stunned villager instantly accepted this colossal fortune for an animal.",
                "translation": "Şaşkına dönen köylü, bir hayvan için önerilen bu devasa serveti derhal kabul etti.",
                "notes": "colossal fortune: devasa servet; stunned: afallamış"
            },
            {
                "id": 119,
                "text": "A young, intelligent Parsee agreed to serve as their guide and driver for a handsome fee.",
                "translation": "Zeki genç bir Parsi, dolgun bir ücret karşılığında onlara rehberlik ve sürücülük yapmayı kabul etti.",
                "notes": "handsome fee: dolgun ücret; driver: fil sürücüsü"
            },
            {
                "id": 120,
                "text": "They mounted the howdah upon the elephant's back and trotted boldly into the dense forest.",
                "translation": "Filin sırtındaki mahfe köşküne bindiler ve cesurca sık ormanın içine doğru tırısa kalktılar.",
                "notes": "howdah: fil sırtındaki oturak; trot: tırıs gitmek"
            }
        ]
    },

    # Page 7 (Sentences 121-140)
    {
        "page_no": 7,
        "title": "The Rescue of Princess Aouda",
        "tr_title": "Prenses Aouda'nın Cesurca Kurtarılışı",
        "vocab_focus": [
            ("suttee", "sati (dul kadının yakılması töreni)"),
            ("sacrifice", "kurban, kurban etmek"),
            ("funeral pyre", "cenaze odun yığını"),
            ("brahmin", "brahman rahibi"),
            ("opium", "afyon"),
            ("corpse", "ceset"),
            ("rescue", "kurtarmak, kurtarma"),
            ("dawn", "şafak vakti")
        ],
        "sentences": [
            {
                "id": 121,
                "text": "Kiouni marched tirelessly through bamboo groves and tangled creepers under the hot tropical sun.",
                "translation": "Kiouni sıcak tropik güneşin altında bambu korulukları ve sarmaşıklar arasından yorulmak bilmeden ilerledi.",
                "notes": "tirelessly: yorulmak bilmeden; bamboo grove: bambu koruluğu"
            },
            {
                "id": 122,
                "text": "Near the village of Pillaji, the elephant stopped abruptly, sniffing the air with raised trunk.",
                "translation": "Pillaji köyü yakınlarında fil aniden durdu ve havaya kaldırdığı hortumuyla havayı kokladı.",
                "notes": "abruptly: aniden; raised trunk: havaya kalkmış hortum"
            },
            {
                "id": 123,
                "text": "Wild chanting and the rhythmic beat of brass cymbals echoed through the shadowy forest.",
                "translation": "Gölgeli ormanın içinden vahşi ilahiler ve pirinç zillerin ritmik vuruşları yankılandı.",
                "notes": "rhythmic beat: ritmik vuruş; brass cymbal: pirinç zil"
            },
            {
                "id": 124,
                "text": "\"It is a procession of the goddess Kali,\" the Parsee guide whispered, concealing the elephant in thick bushes.",
                "translation": "\"Bu tanrıça Kali'nin bir ayin alayı,\" diye fısıldadı Parsi rehber, fili sık çalılıkların arasına gizleyerek.",
                "notes": "procession: ayin alayı; conceal: gizlemek"
            },
            {
                "id": 125,
                "text": "Through the foliage, they saw fanatical priests escorting a funeral bier carrying an old rajah's corpse.",
                "translation": "Yaprakların arasından, yaşlı bir racanın cesedini taşıyan bir cenaze sedyesine eşlik eden fanatik rahipleri gördüler.",
                "notes": "funeral bier: cenaze sedyesi; corpse: ceset; foliage: yapraklar"
            },
            {
                "id": 126,
                "text": "Behind the dead prince walked a beautiful young woman, weeping bitterly and barely able to stand.",
                "translation": "Ölü prensin arkasında, acı acı ağlayan ve güçlükle ayakta durabilen genç ve güzel bir kadın yürüyordu.",
                "notes": "weep bitterly: acı acı ağlamak; barely able to stand: ayakta zor durmak"
            },
            {
                "id": 127,
                "text": "\"It is a human sacrifice called a suttee!\" Sir Francis explained in horror.",
                "translation": "\"Bu sati adı verilen bir insan kurban töreni!\" diye açıkladı Sir Francis dehşet içinde.",
                "notes": "human sacrifice: insan kurban etme; suttee: sati töreni"
            },
            {
                "id": 128,
                "text": "\"Tomorrow morning at dawn, that young widow will be burned alive alongside her dead husband.\"",
                "translation": "\"Yarın sabah şafak sökerken o genç dul kadın, ölü kocasının yanında diri diri yakılacak.\"",
                "notes": "burn alive: diri diri yakmak; widow: dul kadın; at dawn: şafak vakti"
            },
            {
                "id": 129,
                "text": "\"She is Aouda, the educated daughter of a wealthy merchant from Bombay,\" the guide added softly.",
                "translation": "\"O Bombaylı zengin bir tüccarın iyi eğitim almış kızı Aouda,\" diye ekledi rehber usulca.",
                "notes": "educated: eğitimli; merchant: tüccar"
            },
            {
                "id": 130,
                "text": "\"She has been drugged with opium so that she cannot resist this cruel martyrdom.\"",
                "translation": "\"Bu zalimce işkenceye direnemesin diye afyonla uyuşturulmuş durumda.\"",
                "notes": "drug with opium: afyonla uyuşturmak; cruel martyrdom: zalimce ölüm"
            },
            {
                "id": 131,
                "text": "Phileas Fogg looked at his chronometer and spoke with utter calmness: \"We still have twelve hours in hand.\"",
                "translation": "Phileas Fogg kronometresine baktı ve tam bir sükunetle konuştu: \"Hala elimizde on iki saat var.\"",
                "notes": "utter calmness: tam bir sükunet; chronometer: hassas saat"
            },
            {
                "id": 132,
                "text": "\"I can devote them to saving this unfortunate woman.\"",
                "translation": "\"Bu saati o talihsiz kadını kurtarmaya adayabilirim.\"",
                "notes": "devote to: ...e adamak; unfortunate woman: talihsiz kadın"
            },
            {
                "id": 133,
                "text": "\"You have a noble heart, Mr. Fogg!\" Sir Francis cried, grasping the gentleman's hand.",
                "translation": "\"Asil bir kalbiniz var Bay Fogg!\" diye haykırdı Sir Francis, beyefendinin elini sıkarak.",
                "notes": "noble heart: asil yürek; grasp hand: elini sıkmak"
            },
            {
                "id": 134,
                "text": "That night, they crept up to the temple where Aouda was guarded by armed fanatics.",
                "translation": "O gece, Aouda'nın silahlı fanatikler tarafından korunduğu tapınağa doğru sessizce sokuldular.",
                "notes": "creep up: sessizce sokulmak; guard: korumak, nöbet tutmak"
            },
            {
                "id": 135,
                "text": "They tried to cut through the wooden wall with knives, but guards were watching every angle.",
                "translation": "Bıçaklarla ahşap duvarı kesmeye çalıştılar ancak nöbetçiler her köşeyi gözetliyordu.",
                "notes": "cut through: kesip delmek; watch every angle: her açıyı gözetlemek"
            },
            {
                "id": 136,
                "text": "At sunrise, the young widow was dragged to the wooden pyre soaked in burning oil.",
                "translation": "Güneş doğarken, genç dul kadın yanan yağlara batırılmış odun yığınına sürüklendi.",
                "notes": "funeral pyre: odun yığını; soaked in oil: yağa batırılmış"
            },
            {
                "id": 137,
                "text": "Torches touched the dry wood, and thick clouds of smoke billowed into the morning air.",
                "translation": "Meşaleler kuru odunlara değdi ve yoğun duman bulutları sabah havasına doğru yükseldi.",
                "notes": "torch: meşale; billow: dalga dalga yükselmek"
            },
            {
                "id": 138,
                "text": "Suddenly, a terrifying figure rose from the flaming pyre: the dead rajah appeared to come back to life!",
                "translation": "Birden alev alev yanan odunların arasından korkunç bir silüet doğruldu: ölü raca adeta yeniden dirilmişti!",
                "notes": "come back to life: dirilmek, canlanmak; flaming pyre: alevli odun yığını"
            },
            {
                "id": 139,
                "text": "The priests shrieked in horror and threw themselves flat on their faces before the resurrected ghost.",
                "translation": "Rahipler dehşet içinde çığlıklar attılar ve dirilen hayaletin önünde yüzüstü yere kapandılar.",
                "notes": "shriek in horror: dehşetle çığlık atmak; throw flat: boylu boyunca yere kapanmak"
            },
            {
                "id": 140,
                "text": "The ghost scooped up Princess Aouda in his strong arms and bounded into the bushes: it was Passepartout in disguise!",
                "translation": "Hayalet, Prenses Aouda'yı güçlü kollarına aldı ve çalılıklara doğru sıçradı: bu kılık değiştirmiş Passepartout'ydu!",
                "notes": "scoop up: kucaklayıp kaldırmak; in disguise: kılık değiştirmiş"
            }
        ]
    },

    # Page 8 (Sentences 141-160)
    {
        "page_no": 8,
        "title": "From Calcutta to the Island of Hong Kong",
        "tr_title": "Kalküta'dan Hong Kong Limanına",
        "vocab_focus": [
            ("court", "mahkeme"),
            ("bail", "kefalet bedeli"),
            ("magistrate", "sulh hakimi, yargıç"),
            ("steamer", "buharlı gemi"),
            ("harbor", "liman"),
            ("gratitude", "minnettarlık"),
            ("storm", "fırtına"),
            ("typhoon", "tayfun")
        ],
        "sentences": [
            {
                "id": 141,
                "text": "Before the priests discovered the trick, the elephant dashed away through the jungle at breakneck speed.",
                "translation": "Rahipler bu oyunu fark etmeden önce fil ormanın içinden baş döndürücü bir hızla uzaklaştı.",
                "notes": "breakneck speed: baş döndürücü / son sürat hız; discover trick: hileyi anlamak"
            },
            {
                "id": 142,
                "text": "They reached the station at Allahabad that very morning, safely in time for the train to Calcutta.",
                "translation": "Tam o sabah Allahabad garına ulaştılar ve Kalküta trenine tam vaktinde yetiştiler.",
                "notes": "safely in time: tam vaktinde ve güvenle"
            },
            {
                "id": 143,
                "text": "Mr. Fogg generously gave the faithful elephant Kiouni to the brave Parsee guide as a reward.",
                "translation": "Bay Fogg bir ödül olarak sadık fil Kiouni'yi cesur Parsi rehbere cömertçe hediye etti.",
                "notes": "generously: cömertçe; as a reward: ödül olarak"
            },
            {
                "id": 144,
                "text": "Aouda gradually awoke from her narcotic sleep, weeping with overwhelming gratitude when told of her rescue.",
                "translation": "Aouda afyon uykusundan yavaşça uyandı ve kurtarıldığı anlatılınca derin bir minnettarlıkla ağladı.",
                "notes": "overwhelming gratitude: taşkın minnettarlık; narcotic sleep: uyuşuk uyku"
            },
            {
                "id": 145,
                "text": "She was young, beautifully educated in European manners, and possessed extraordinary grace.",
                "translation": "Gençti, Avrupa terbiyesiyle mükemmel eğitilmişti ve olağanüstü bir zarafete sahipti.",
                "notes": "European manners: Avrupa terbiyesi / adabı; extraordinary grace: olağanüstü zarafet"
            },
            {
                "id": 146,
                "text": "Fogg assured her that she would travel under his protection to relatives in Hong Kong.",
                "translation": "Fogg, Hong Kong'daki akrabalarına kadar kendi koruması altında seyahat edeceği konusunda ona güvence verdi.",
                "notes": "under protection: koruması altında; relative: akraba"
            },
            {
                "id": 147,
                "text": "When they stepped onto the platform at Calcutta, a police constable approached them with a stern salute.",
                "translation": "Kalküta peronuna adım attıklarında, bir polis memuru sert bir selamla yanlarına yaklaştı.",
                "notes": "police constable: polis memuru; stern salute: sert selam"
            },
            {
                "id": 148,
                "text": "\"Mr. Phileas Fogg and Jean Passepartout? You must follow me to the magistrate's court!\"",
                "translation": "\"Bay Phileas Fogg ve Jean Passepartout musunuz? Benimle sulh ceza mahkemesine gelmek zorundasınız!\"",
                "notes": "magistrate's court: sulh ceza mahkemesi; follow: takip etmek"
            },
            {
                "id": 149,
                "text": "Passepartout was terrified, thinking they were being arrested for kidnapping Aouda from the suttee.",
                "translation": "Passepartout, Aouda'yı sati töreninden kaçırdıkları için tutuklandıklarını zannederek dehşete düştü.",
                "notes": "kidnap: kaçırmak; terrified: dehşete kapılmış"
            },
            {
                "id": 150,
                "text": "In the courtroom, three Hindu priests from Bombay stepped forward, holding Passepartout's abandoned shoes.",
                "translation": "Mahkeme salonunda Bombaylı üç Hindu rahip öne çıktı; ellerinde Passepartout'nun geride bıraktığı ayakkabıları tutuyorlardı.",
                "notes": "courtroom: duruşma salonu; step forward: öne çıkmak"
            },
            {
                "id": 151,
                "text": "The judge sentenced Passepartout to fifteen days in prison and Fogg to eight days for masterminding the desecration.",
                "translation": "Yargıç, tapınak saygısızlığını planladığı için Fogg'u sekiz gün, Passepartout'yu ise on beş gün hapis cezasına çarptırdı.",
                "notes": "sentence to prison: hapis cezasına çarptırmak; mastermind: planlamak"
            },
            {
                "id": 152,
                "text": "Detective Fix smiled maliciously from the rear of the courtroom, believing his prey was trapped at last.",
                "translation": "Dedektif Fix avının nihayet tuzağa düştüğüne inanarak salonun arkasından sinsi sinsi gülümsedi.",
                "notes": "maliciously: sinsi / haince; trap: kapana kıstırmak"
            },
            {
                "id": 153,
                "text": "\"How much is the bail?\" Mr. Fogg asked with unruffled calm.",
                "translation": "\"Kefalet bedeli ne kadar?\" diye sordu Bay Fogg istifini bozmadan.",
                "notes": "bail: kefalet ücreti; unruffled calm: istifini bozmayan sükunet"
            },
            {
                "id": 154,
                "text": "\"One thousand pounds for each prisoner,\" the astonished magistrate replied.",
                "translation": "\"Her mahkum için bin sterlin,\" diye yanıt verdi şaşkın yargıç.",
                "notes": "astonished: şaşkın; prisoner: mahkum"
            },
            {
                "id": 155,
                "text": "Mr. Fogg immediately counted out two thousand pounds in crisp banknotes from his magic carpetbag.",
                "translation": "Bay Fogg sihirli seyahat çantasından gıcır gıcır banknotlarla iki bin sterlini derhal sayıp verdi.",
                "notes": "crisp banknotes: gıcır gıcır banknotlar; count out: sayıp vermek"
            },
            {
                "id": 156,
                "text": "Fix clutched his hair in sheer fury as Fogg, Passepartout, and Aouda walked freely out of court.",
                "translation": "Fogg, Passepartout ve Aouda mahkemeden serbestçe çıkıp giderken Fix öfkeden saçını başını yoldu.",
                "notes": "clutch hair: saçını başını yolmak; sheer fury: katıksız öfke"
            },
            {
                "id": 157,
                "text": "They hurried to the port and boarded the steamer Rangoon bound for the British colony of Hong Kong.",
                "translation": "Limana koştular ve İngiliz sömürgesi Hong Kong'a giden Rangoon buharlısına bindiler.",
                "notes": "bound for: ...e gitmekte olan; British colony: İngiliz sömürgesi"
            },
            {
                "id": 158,
                "text": "Fix followed them aboard, raging that the thief was throwing away bank money so carelessly.",
                "translation": "Fix, hırsızın banka parasını böylesine pervasızca saçıp savurmasına köpürerek arkalarından gemiye bindi.",
                "notes": "rage: köpürmek, küplere binmek; throw away money: parayı saçıp savurmak"
            },
            {
                "id": 159,
                "text": "The Rangoon steamed across the South China Sea, where a raging autumn typhoon struck the vessel.",
                "translation": "Rangoon Güney Çin Denizi'nde ilerlerken, azgın bir sonbahar tayfunu gemiyi vurdu.",
                "notes": "typhoon: tayfun; rage: azgınlaşmak, şiddetlenmek"
            },
            {
                "id": 160,
                "text": "Enormous waves battered the hull, delaying their arrival in Hong Kong by over twenty-four hours.",
                "translation": "Devasa dalgalar gövdeyi döverek Hong Kong'a varışlarını yirmi dört saatten fazla geciktirdi.",
                "notes": "batter hull: gövdeyi dövmek; enormous waves: dev dalgalar"
            }
        ]
    },

    # Page 9 (Sentences 161-180)
    {
        "page_no": 9,
        "title": "The Separation in the Opium Den",
        "tr_title": "Hong Kong'da Ayrılık ve Karışıklık",
        "vocab_focus": [
            ("opium den", "afyon batakhanesi"),
            ("pipe", "afyon çubuğu, lüle"),
            ("carnatic", "Karnatik (buharlı gemi adı)"),
            ("pilot boat", "kılavuz teknesi"),
            ("conspiracy", "komplo, tuzak"),
            ("drugged", "uyuşturulmuş"),
            ("stupor", "kendinden geçme, sersemlik"),
            ("typhoon", "tayfun")
        ],
        "sentences": [
            {
                "id": 161,
                "text": "When they reached Hong Kong harbor, they learned that Aouda's rich cousin had moved away to Europe.",
                "translation": "Hong Kong limanına vardıklarında, Aouda'nın zengin kuzeninin Avrupa'ya taşındığını öğrendiler.",
                "notes": "move away: taşınmak, uzaklaşmak; cousin: kuzen"
            },
            {
                "id": 162,
                "text": "Fogg graciously invited the young lady to accompany him all the way to England.",
                "translation": "Fogg, genç hanımefendiyi İngiltere'ye kadar kendisine eşlik etmesi için nezaketle davet etti.",
                "notes": "graciously: nezaketle; accompany: eşlik etmek"
            },
            {
                "id": 163,
                "text": "The next steamer for Yokohama, the Carnatic, had been delayed for repairs and was to sail that evening.",
                "translation": "Yokohama'ya gidecek sıradaki buharlı gemi Carnatic, onarım için gecikmişti ve o akşam yola çıkacaktı.",
                "notes": "delayed for repairs: onarım için gecikmiş; sail: denize açılmak"
            },
            {
                "id": 164,
                "text": "Hong Kong was British soil, but Fix's warrant of arrest still had not arrived from London.",
                "translation": "Hong Kong İngiliz toprağıydı fakat Fix'in tutuklama emri hala Londra'dan ulaşmamıştı.",
                "notes": "British soil: İngiliz toprağı; warrant of arrest: tutuklama kararı"
            },
            {
                "id": 165,
                "text": "Once Fogg reached American territory, Fix would lose all legal jurisdiction forever.",
                "translation": "Fogg Amerikan topraklarına bir kez ayak bastığında, Fix tüm yasal yetkisini sonsuza dek kaybedecekti.",
                "notes": "legal jurisdiction: yasal yetki alanı; American territory: Amerikan toprağı"
            },
            {
                "id": 166,
                "text": "In desperation, Detective Fix decided on a sinister scheme to delay the travelers.",
                "translation": "Çaresizlik içindeki Dedektif Fix, yolcuları geciktirmek için sinsi bir plan kurmaya karar verdi.",
                "notes": "in desperation: çaresizlik içinde; sinister scheme: sinsi plan"
            },
            {
                "id": 167,
                "text": "He invited Passepartout into a dark tavern and revealed his true identity as a police inspector.",
                "translation": "Passepartout'yu karanlık bir meyhaneye davet etti ve bir polis müfettişi olduğunu açıklayarak gerçek kimliğini ifşa etti.",
                "notes": "true identity: gerçek kimlik; reveal: açığa vurmak"
            },
            {
                "id": 168,
                "text": "\"Your master is an infamous thief who robbed fifty-five thousand pounds from the Bank of England!\" Fix insisted.",
                "translation": "\"Efendin, İngiltere Bankası'ndan elli beş bin sterlin çalan azılı bir hırsızdır!\" diye diretti Fix.",
                "notes": "infamous thief: azılı hırsız; rob: soymak"
            },
            {
                "id": 169,
                "text": "\"Never!\" Passepartout cried loyally, \"Mr. Fogg is the noblest gentleman on earth!\"",
                "translation": "\"Asla!\" diye haykırdı Passepartout sadakatle, \"Bay Fogg yeryüzündeki en asil beyefendidir!\"",
                "notes": "loyally: sadakatle; noble gentleman: asil beyefendi"
            },
            {
                "id": 170,
                "text": "Seeing the servant could not be bribed, Fix slipped into an adjoining opium den and ordered a pipe.",
                "translation": "Uşağa rüşvet yediremeyeceğini gören Fix, bitişikteki bir afyon batakhanesine geçti ve bir lüle sipariş etti.",
                "notes": "bribe: rüşvet vermek; opium den: afyon tekkesi"
            },
            {
                "id": 171,
                "text": "He secretly laced Passepartout's tobacco with potent opium until the poor Frenchman collapsed unconscious.",
                "translation": "Zavallı Fransız kendinden geçip bayılana kadar gizlice Passepartout'nun tütününe ağır afyon karıştırdı.",
                "notes": "lace with opium: afyon katmak; collapse unconscious: kendinden geçip yığılmak"
            },
            {
                "id": 172,
                "text": "Fix left him senseless on the floor, knowing Fogg would miss the Carnatic without his servant's warning.",
                "translation": "Uşağın uyarısı olmadan Fogg'un Carnatic gemisini kaçıracağını bilerek onu yerde baygın halde bıraktı.",
                "notes": "senseless: kendinde olmayan, baygın; miss the ship: gemiyi kaçırmak"
            },
            {
                "id": 173,
                "text": "However, Passepartout's subconscious mind managed to drag his staggering body aboard the Carnatic just before departure.",
                "translation": "Ne var ki Passepartout'nun bilinçaltı, kalkıştan hemen önce sendeleyen bedenini Carnatic gemisine sürüklemeyi başardı.",
                "notes": "staggering body: sendeleyen vücut; subconscious: bilinçaltı"
            },
            {
                "id": 174,
                "text": "He fell into a deep stupor in the ship's hold, completely unaware that his master had been left behind.",
                "translation": "Geminin ambarında derin bir komaya girdi; efendisinin geride kaldığından tamamen habersizdi.",
                "notes": "deep stupor: derin koma / baygınlık; left behind: geride kalmış"
            },
            {
                "id": 175,
                "text": "The next morning, Mr. Fogg and Princess Aouda went to the harbor and found the Carnatic gone.",
                "translation": "Ertesi sabah Bay Fogg ve Prenses Aouda limana gittiler ve Carnatic'in çoktan gittiğini gördüler.",
                "notes": "harbor: liman; gone: gitmiş"
            },
            {
                "id": 176,
                "text": "Fix watched from afar, gloating over Fogg's apparent ruin and ruined schedule.",
                "translation": "Fix uzaktan izliyor, Fogg'un apaçık yıkılışı ve altüst olan takvimiyle gizli gizli zevkleniyordu.",
                "notes": "gloat over: zevkten dört köşe olmak; apparent ruin: apaçık yıkım"
            },
            {
                "id": 177,
                "text": "Mr. Fogg did not blink; he immediately searched the docks for another vessel.",
                "translation": "Bay Fogg gözünü bile kırpmadı; rıhtımları başka bir tekne bulmak için derhal taramaya başladı.",
                "notes": "search docks: rıhtımları aramak; not blink: gözünü kırpmamak"
            },
            {
                "id": 178,
                "text": "He found a daring captain named John Bunsby, master of a little pilot boat named the Tankadere.",
                "translation": "Tankadere adındaki küçük kılavuz teknesinin kaptanı olan John Bunsby adında cesur bir denizci buldu.",
                "notes": "pilot boat: kılavuz teknesi; daring captain: cesur kaptan"
            },
            {
                "id": 179,
                "text": "For one hundred pounds a day, Bunsby agreed to sail through dangerous typhoons to Shanghai.",
                "translation": "Günde yüz sterlin karşılığında Bunsby, Şanghay'a ulaşmak için tehlikeli tayfunların arasından yelken açmayı kabul etti.",
                "notes": "per day: günlük; dangerous typhoon: tehlikeli tayfun"
            },
            {
                "id": 180,
                "text": "Fogg generously offered Fix a free passage, unaware that his companion was his sworn pursuer.",
                "translation": "Fogg, yol arkadaşının kendi amansız takipçisi olduğundan habersiz, Fix'e cömertçe ücretsiz bir yolculuk teklif etti.",
                "notes": "free passage: ücretsiz yolculuk; sworn pursuer: amansız takipçi"
            }
        ]
    },

    # Page 10 (Sentences 181-200)
    {
        "page_no": 10,
        "title": "Crossing the Pacific to Yokohama and San Francisco",
        "tr_title": "Büyük Okyanus'u Aşarak San Francisco'ya",
        "vocab_focus": [
            ("schooner", "uskuna"),
            ("rocket", "işaret fişeği"),
            ("acrobat", "cambaz, akrobat"),
            ("circus", "sirk"),
            ("long-nosed", "uzun burunlu"),
            ("reunion", "yeniden kavuşma"),
            ("Pacific", "Büyük Okyanus / Pasifik"),
            ("steamer", "buharlı okyanus gemisi")
        ],
        "sentences": [
            {
                "id": 181,
                "text": "The tiny Tankadere battled gigantic waves and terrifying gales across eight hundred miles of open sea.",
                "translation": "Minik Tankadere açık denizde sekiz yüz mil boyunca dev dalgalarla ve ürkütücü fırtınalarla boğuştu.",
                "notes": "gigantic waves: devasa dalgalar; open sea: açık deniz"
            },
            {
                "id": 182,
                "text": "As they approached Shanghai, the great American mail steamer General Grant was already steaming out of port.",
                "translation": "Şanghay'a yaklaştıklarında, büyük Amerikan posta vapuru General Grant limandan çoktan hareket etmekteydi.",
                "notes": "mail steamer: posta vapuru; steam out: buhar gücüyle limandan çıkmak"
            },
            {
                "id": 183,
                "text": "Captain Bunsby hoisted a distress flag and fired his little brass cannon in signal.",
                "translation": "Kaptan Bunsby bir tehlike bayrağı çekti ve işaret olarak küçük pirinç topunu ateşledi.",
                "notes": "distress flag: tehlike bayrağı; brass cannon: pirinç top"
            },
            {
                "id": 184,
                "text": "The American vessel saw the distress rocket, slowed down, and took the brave travelers aboard.",
                "translation": "Amerikan gemisi tehlike fişeğini gördü, yavaşladı ve cesur yolcuları güverteye aldı.",
                "notes": "slow down: yavaşlamak; take aboard: gemiye almak"
            },
            {
                "id": 185,
                "text": "Meanwhile, the Carnatic had arrived safely in Yokohama with a penniless Passepartout.",
                "translation": "Bu sırada Carnatic gemisi, beş parasız Passepartout ile birlikte Yokohama'ya sağ salim varmıştı.",
                "notes": "penniless: beş parasız, meteliksiz; arrive safely: sağ salim varmak"
            },
            {
                "id": 186,
                "text": "Starving and desperate, the Frenchman wandered through the streets of Yokohama looking for food.",
                "translation": "Açlıktan bitkin ve çaresiz haldeki Fransız, yemek arayarak Yokohama sokaklarında dolaştı.",
                "notes": "starving: açlıktan ölmek üzere; desperate: çaresiz"
            },
            {
                "id": 187,
                "text": "He noticed a colorful poster advertising the Japanese acrobatic troupe of the Honorable Batulcar.",
                "translation": "Saygıdeğer Batulcar'ın Japon akrobasi kumpanyasını tanıtan rengarenk bir afiş fark etti.",
                "notes": "acrobatic troupe: akrobasi kumpanyası; poster: afiş"
            },
            {
                "id": 188,
                "text": "Passepartout applied for work and was hired as a human base for the famous 'Long-Nosed Tengu' pyramid.",
                "translation": "Passepartout işe başvurdu ve ünlü 'Uzun Burunlu Tengu' piramidi için insan tabanı olarak işe alındı.",
                "notes": "apply for work: işe başvurmak; human base: insan tabanı"
            },
            {
                "id": 189,
                "text": "He wore a giant artificial nose made of painted bamboo, balancing six performers upon his shoulders.",
                "translation": "Omuzlarında altı göstericiyi dengelerken boyalı bambudan yapılmış devasa yapay bir burun takıyordu.",
                "notes": "artificial nose: takma / yapay burun; balance performers: sanatçıları dengelemek"
            },
            {
                "id": 190,
                "text": "During the performance, he suddenly spotted Phileas Fogg and Princess Aouda sitting in the front row!",
                "translation": "Gösteri sırasında birdenbire ön sırada oturan Phileas Fogg ve Prenses Aouda'yı gördü!",
                "notes": "front row: ön sıra; spot: gözüne çarpmak, fark etmek"
            },
            {
                "id": 191,
                "text": "\"My master! My dear master!\" the overjoyed Frenchman shouted, abandoning his balance.",
                "translation": "\"Efendim! Sevgili efendim!\" diye haykırdı sevinçten havalara uçan Fransız, dengesini tamamen bırakarak.",
                "notes": "overjoyed: sevinçten çılgına dönmüş; abandon balance: dengeyi bozmak"
            },
            {
                "id": 192,
                "text": "The human pyramid collapsed in a heap of tangled legs, tumbling noses, and screaming acrobats.",
                "translation": "İnsan piramidi; birbirine dolanmış bacaklar, yuvarlanan burunlar ve çığlık atan akrobatlar yığını halinde çöktü.",
                "notes": "tangled legs: dolanmış bacaklar; collapse: çökmek"
            },
            {
                "id": 193,
                "text": "Fogg paid the furious manager a handful of silver dollars and swept Passepartout away in joy.",
                "translation": "Fogg öfkeli müdüre bir avuç gümüş dolar ödedi ve sevinç içinde Passepartout'yu alıp götürdü.",
                "notes": "handful of silver: bir avuç gümüş; sweep away: alıp götürmek"
            },
            {
                "id": 194,
                "text": "Reunited at last, they boarded the Pacific Mail steamship General Grant bound for San Francisco.",
                "translation": "Nihayet yeniden kavuşarak San Francisco'ya gitmekte olan Pacific Mail buharlısı General Grant'e bindiler.",
                "notes": "reunited: yeniden kavuşmuş; bound for: ...e gitmekte olan"
            },
            {
                "id": 195,
                "text": "On deck, Passepartout bumped into Detective Fix and gave him a furious punch in the nose.",
                "translation": "Güvertede Passepartout Dedektif Fix ile burun buruna geldi ve burnunun ortasına öfkeli bir yumruk indirdi.",
                "notes": "punch in the nose: burnuna yumruk atmak; bump into: karşılaşmak"
            },
            {
                "id": 196,
                "text": "\"Have you done?\" Fix asked coolly, wiping blood from his lip.",
                "translation": "\"Rahatladın mı?\" diye sordu Fix serinkanlılıkla, dudağındaki kanı silerek.",
                "notes": "coolly: serinkanlılıkla; wipe blood: kanı silmek"
            },
            {
                "id": 197,
                "text": "\"Now listen to me: on American soil, my warrant is useless; I want Mr. Fogg to reach England as fast as you do.\"",
                "translation": "\"Şimdi beni dinle: Amerikan topraklarında tutuklama emrim geçersiz; ben de en az senin kadar Bay Fogg'un bir an önce İngiltere'ye varmasını istiyorum.\"",
                "notes": "useless: geçersiz, işe yaramaz; American soil: Amerikan toprağı"
            },
            {
                "id": 198,
                "text": "\"I will help you speed up the voyage so that I can arrest him legally on British ground!\"",
                "translation": "\"İngiliz topraklarında onu yasal olarak tutuklayabilmek için yolculuğu hızlandırmanıza yardım edeceğim!\"",
                "notes": "speed up: hızlandırmak; British ground: İngiliz toprağı"
            },
            {
                "id": 199,
                "text": "Passepartout reluctantly agreed to a temporary truce with the persistent detective.",
                "translation": "Passepartout inatçı dedektifle geçici bir ateşkese gönülsüzce razı oldu.",
                "notes": "reluctantly: gönülsüzce; temporary truce: geçici ateşkes"
            },
            {
                "id": 200,
                "text": "On December the third, the General Grant sailed past the Golden Gate into San Francisco harbor on time.",
                "translation": "Üç Aralık'ta General Grant tam vaktinde Golden Gate Boğazı'nı geçerek San Francisco limanına yanaştı.",
                "notes": "Golden Gate: San Francisco boğazı; on time: vaktinde"
            }
        ]
    },

    # Page 11 (Sentences 201-220)
    {
        "page_no": 11,
        "title": "The Transcontinental Railroad Across America",
        "tr_title": "Amerika Kıtasını Baştan Başa Geçiş",
        "vocab_focus": [
            ("transcontinental", "kıtalararası"),
            ("locomotive", "lokomotif"),
            ("buffalo", "bizon, Amerikan bizonu"),
            ("prairie", "kuzey Amerika çayırı, bozkır"),
            ("bridge", "köprü"),
            ("duel", "düello"),
            ("trestle", "ayaklı ahşap köprü iskelesi"),
            ("speed", "sürat, hız")
        ],
        "sentences": [
            {
                "id": 201,
                "text": "Without spending a single hour exploring California, Mr. Fogg boarded the Pacific Railroad train for New York.",
                "translation": "Kaliforniya'yı gezmek için tek bir saat bile harcamayan Bay Fogg, New York'a gidecek Pasifik Demiryolu trenine bindi.",
                "notes": "board the train: trene binmek; Pacific Railroad: Pasifik Demiryolu"
            },
            {
                "id": 202,
                "text": "The journey across the American continent was three thousand seven hundred and eighty-six miles long.",
                "translation": "Amerikan kıtasını baştan başa geçen yolculuk üç bin yedi yüz seksen altı mil uzunluğundaydı.",
                "notes": "American continent: Amerikan kıtası; long: uzunluğunda"
            },
            {
                "id": 203,
                "text": "It was scheduled to take seven days to reach the Atlantic coast.",
                "translation": "Atlantik kıyısına ulaşmasının yedi gün sürmesi planlanmıştı.",
                "notes": "be scheduled to: planlanmış olmak; reach coast: kıyıya ulaşmak"
            },
            {
                "id": 204,
                "text": "The train climbed steadily through the snowy peaks of the Sierra Nevada mountains.",
                "translation": "Tren Sierra Nevada dağlarının karlı dorukları arasından istikrarlı bir şekilde tırmandı.",
                "notes": "climb steadily: istikrarlı tırmanmak; snowy peaks: karlı doruklar"
            },
            {
                "id": 205,
                "text": "Inside the comfortable parlor car, Mr. Fogg and Princess Aouda played whist with Fix and a fellow traveler.",
                "translation": "Konforlu salon vagonunun içinde, Bay Fogg ve Prenses Aouda, Fix ve diğer bir yolcuyla vist oynadılar.",
                "notes": "parlor car: lüks salon vagonu; play whist: vist oynamak"
            },
            {
                "id": 206,
                "text": "Suddenly, the train was halted by an enormous herd of ten thousand shaggy buffaloes.",
                "translation": "Birdenbire tren, on bin yünlü bizondan oluşan devasa bir sürü yüzünden durduruldu.",
                "notes": "buffalo herd: bizon sürüsü; shaggy: yünlü, tüylü"
            },
            {
                "id": 207,
                "text": "The dark living mass crossed the tracks for three whole hours without stopping.",
                "translation": "Bu koyu renkli canlı kütle, hiç durmaksızın tam üç saat boyunca rayların üzerinden geçti.",
                "notes": "living mass: canlı kütle; cross the tracks: rayların üzerinden geçmek"
            },
            {
                "id": 208,
                "text": "Passepartout paced the platform nervously, while Mr. Fogg waited with Olympian serenity.",
                "translation": "Passepartout peronda asabi bir şekilde volta atarken, Bay Fogg tanrısal bir sükunetle bekledi.",
                "notes": "pace nervously: asabi volta atmak; Olympian serenity: sarsılmaz sükunet"
            },
            {
                "id": 209,
                "text": "The train resumed its course, descending the Rocky Mountains into the vast plains of Wyoming.",
                "translation": "Tren yoluna devam ederek Kayalık Dağlar'dan Wyoming'in engin ovalarına doğru alçaldı.",
                "notes": "resume course: seyre devam etmek; vast plains: engin ovalar"
            },
            {
                "id": 210,
                "text": "At Medicine Bow station, the conductor announced that the suspension bridge ahead was completely ruined.",
                "translation": "Medicine Bow istasyonunda kondüktör, ilerideki asma köprünün tamamen harap olduğunu bildirdi.",
                "notes": "suspension bridge: asma köprü; completely ruined: tamamen harap olmuş"
            },
            {
                "id": 211,
                "text": "\"The bridge will not bear the weight of a train; we must wait for the next ferry!\"",
                "translation": "\"Köprü bir trenin ağırlığını taşıyamaz; bir sonraki feribotu beklemek zorundayız!\"",
                "notes": "bear weight: ağırlığı taşımak; ferry: feribot"
            },
            {
                "id": 212,
                "text": "The engine driver, a reckless American, stepped forward with a daring proposal.",
                "translation": "Gözü pek bir Amerikalı olan makinist, cüretkar bir öneriyle öne çıktı.",
                "notes": "engine driver: makinist; daring proposal: cüretkar teklif"
            },
            {
                "id": 213,
                "text": "\"If we back up a mile and rush across at top speed, our momentum will carry us over before the trestle collapses!\"",
                "translation": "\"Bir mil geri gidip son süratle atlarsak, köprü çökmeye fırsat bulamadan ivmemiz bizi karşıya geçirir!\"",
                "notes": "top speed: son sürat; momentum: hareket ivmesi; collapse: çökmek"
            },
            {
                "id": 214,
                "text": "The adventurous passengers shouted in approval, eager not to be delayed.",
                "translation": "Maceraperest yolcular gecikmemek için hevesle bu teklifi alkışlayıp onayladılar.",
                "notes": "approval: onay; eager: hevesli"
            },
            {
                "id": 215,
                "text": "The locomotive reversed, built up maximum steam, and hurled itself forward like a thunderbolt.",
                "translation": "Lokomotif geri gitti, azami buhar basıncına ulaştı ve bir yıldırım gibi kendini ileri fırlattı.",
                "notes": "thunderbolt: yıldırım; maximum steam: azami buhar"
            },
            {
                "id": 216,
                "text": "The train flew across the creaking bridge at eighty miles an hour like a cannon shot.",
                "translation": "Tren, gıcırdayan köprünün üzerinden saatte seksen mil hızla bir top güllesi gibi uçtu.",
                "notes": "creaking bridge: gıcırdayan köprü; cannon shot: top atışı"
            },
            {
                "id": 217,
                "text": "The very second the last carriage touched the opposite bank, the bridge crashed into the abyss below.",
                "translation": "Son vagon karşı kıyıya değdiği tam o saniyede, köprü aşağıdaki uçuruma gürültüyle çöktü.",
                "notes": "opposite bank: karşı kıyı; crash into abyss: uçuruma yuvarlanmak"
            },
            {
                "id": 218,
                "text": "The passengers cheered wildly, while Phileas Fogg calmly recorded his whist score.",
                "translation": "Yolcular çılgınca tezahürat yaparken, Phileas Fogg sakince vist skorunu kaydetti.",
                "notes": "cheer wildly: çılgınca tezahürat yapmak; record score: skoru kaydetmek"
            },
            {
                "id": 219,
                "text": "However, an aggressive passenger named Colonel Stamp Proctor insulted Fogg over a card game.",
                "translation": "Fakat Albay Stamp Proctor adında kavgacı bir yolcu, bir kağıt oyunu yüzünden Fogg'a hakaret etti.",
                "notes": "aggressive passenger: kavgacı yolcu; insult: hakaret etmek"
            },
            {
                "id": 220,
                "text": "A duel with revolvers was arranged to take place in the rear car at the next stop.",
                "translation": "Bir sonraki durakta arka vagonda tabancalarla bir düello yapılması kararlaştırıldı.",
                "notes": "duel with revolvers: tabancayla düello; rear car: arka vagon"
            }
        ]
    },

    # Page 12 (Sentences 221-240)
    {
        "page_no": 12,
        "title": "The Sioux Attack and Buffalo Stampede",
        "tr_title": "Siyu Saldırısı ve Karlı Ovalar",
        "vocab_focus": [
            ("attack", "saldırı, taarruz"),
            ("Sioux", "Siyu yerlileri"),
            ("revolver", "altıpatlar, tabanca"),
            ("locomotive", "lokomotif"),
            ("unhook", "kancasını çıkarmak, ayırmak"),
            ("sledge", "yelkenli kızak"),
            ("snow", "kar"),
            ("heroism", "kahramanlık")
        ],
        "sentences": [
            {
                "id": 221,
                "text": "Just as Fogg and the colonel raised their weapons, terrifying war cries echoed outside the train.",
                "translation": "Tam Fogg ile albay silahlarını kaldırmışken, trenin dışından korkunç savaş çığlıkları yankılandı.",
                "notes": "war cry: savaş çığlığı; raise weapons: silahları kaldırmak"
            },
            {
                "id": 222,
                "text": "A band of two hundred mounted Sioux warriors attacked the speeding carriages with rifles.",
                "translation": "İki yüz atlı Siyu savaşçısından oluşan bir çete, hızla giden vagonlara tüfeklerle saldırdı.",
                "notes": "warriors: savaşçılar; mounted: atlı; speeding carriages: hızla giden vagonlar"
            },
            {
                "id": 223,
                "text": "Bullets shattered the glass windows, and armed passengers immediately fired back in self-defense.",
                "translation": "Kurşunlar cam pencereleri tuzla buz etti ve silahlı yolcular meşru müdafaa amacıyla hemen karşılık verdi.",
                "notes": "shatter glass: camı kırmak; self-defense: meşru müdafaa"
            },
            {
                "id": 224,
                "text": "The Indians leaped onto the carriage roofs, trying to overpower the passengers.",
                "translation": "Kızılderililer vagonların çatılarına sıçrayarak yolcuları etkisiz hale getirmeye çalıştılar.",
                "notes": "leap onto: üzerine sıçramak; overpower: alt etmek, etkisiz hale getirmek"
            },
            {
                "id": 225,
                "text": "The train was approaching Fort Kearney, where an American garrison was stationed.",
                "translation": "Tren, bir Amerikan garnizonunun konuşlandığı Kearney Kalesi'ne yaklaşıyordu.",
                "notes": "garrison stationed: garnizon konuşlanmış; approach: yaklaşmak"
            },
            {
                "id": 226,
                "text": "\"If the train does not stop at the fort, the Indians will massacre us all!\" cried the conductor.",
                "translation": "\"Eğer tren kalede durmazsa, Kızılderililer hepimizi kılıçtan geçirecek!\" diye haykırdı kondüktör.",
                "notes": "massacre: kılıçtan geçirmek, katletmek"
            },
            {
                "id": 227,
                "text": "However, the engineer had been wounded, and the throttle remained wide open.",
                "translation": "Fakat makinist vurulmuştu ve gaz kolu sonuna kadar açık kalmıştı.",
                "notes": "throttle wide open: gaz kolu sonuna kadar açık; wounded: yaralı"
            },
            {
                "id": 228,
                "text": "\"I will unhook the locomotive!\" brave Passepartout declared, slipping out underneath the carriage.",
                "translation": "\"Lokomotifin kancasını ben sökeceğim!\" diye haykırdı cesur Passepartout ve vagonun altına doğru süzüldü.",
                "notes": "unhook: kancayı sökmek; underneath: altından"
            },
            {
                "id": 229,
                "text": "Crawling along the safety chains under heavy gunfire, he reached the coupling between engine and cars.",
                "translation": "Yoğun yaylım ateşi altında emniyet zincirleri boyunca sürünerek lokomotif ile vagonlar arasındaki bağlantıya ulaştı.",
                "notes": "coupling: vagon bağlantısı / kancası; heavy gunfire: yoğun yaylım ateşi"
            },
            {
                "id": 230,
                "text": "With superhuman strength, he pulled out the iron coupling pin just before falling.",
                "translation": "İnsanüstü bir güçle, tam düşmek üzereyken demir bağlantı pimini çekip çıkardı.",
                "notes": "coupling pin: bağlantı pimi; superhuman strength: insanüstü güç"
            },
            {
                "id": 231,
                "text": "The locomotive surged ahead alone, while the detached carriages slowly coasted toward Fort Kearney.",
                "translation": "Lokomotif tek başına ileri fırladı, ayrılan vagonlar ise yavaşlayarak Kearney Kalesi'ne doğru süzüldü.",
                "notes": "detached carriages: ayrılan vagonlar; coast: süzülerek ilerlemek"
            },
            {
                "id": 232,
                "text": "Soldiers rushed out of the fort with fixed bayonets, driving off the attackers.",
                "translation": "Askerler takılı süngüleriyle kaleden fırladılar ve saldırganları püskürttüler.",
                "notes": "fixed bayonet: takılı süngü; drive off: püskürtmek"
            },
            {
                "id": 233,
                "text": "When the roll was called, three passengers were missing: among them was brave Jean Passepartout!",
                "translation": "Yoklama yapıldığında üç yolcunun kayıp olduğu anlaşıldı: aralarında cesur Jean Passepartout da vardı!",
                "notes": "roll called: yoklama yapıldı; missing: kayıp"
            },
            {
                "id": 234,
                "text": "\"He saved our lives,\" Phileas Fogg said gravely, \"I will find him, dead or alive.\"",
                "translation": "\"O bizim hayatımızı kurtardı,\" dedi Phileas Fogg ağırbaşlılıkla, \"ölü ya da diri onu bulacağım.\"",
                "notes": "gravely: ağırbaşlılıkla; dead or alive: ölü ya da diri"
            },
            {
                "id": 235,
                "text": "\"You will forfeit your wager, sir!\" Detective Fix reminded him anxiously.",
                "translation": "\"Bahsinizi kaybedeceksiniz efendim!\" diye endişeyle hatırlattı Dedektif Fix.",
                "notes": "forfeit wager: bahsi kaybetmek / yakmak; anxiously: endişeyle"
            },
            {
                "id": 236,
                "text": "\"Duty before all things,\" Mr. Fogg replied firmly, recruiting thirty volunteer soldiers.",
                "translation": "\"Vazife her şeyden önce gelir,\" diye kararlılıkla yanıtladı Bay Fogg, otuz gönüllü asker toplayarak.",
                "notes": "duty before all: vazife her şeyin önündedir; volunteer: gönüllü"
            },
            {
                "id": 237,
                "text": "He marched into the blizzard all night long, risking his fortune and his life.",
                "translation": "Servetini ve hayatını tehlikeye atarak bütün gece tipi altında yürüdü.",
                "notes": "blizzard: tipi, kar fırtınası; risk life: canını tehlikeye atmak"
            },
            {
                "id": 238,
                "text": "At dawn, Fogg returned triumphantly with the rescued prisoners, unharmed and victorious.",
                "translation": "Şafak sökerken Fogg, kurtarılan esirlerle birlikte burnu bile kanamadan zaferle geri döndü.",
                "notes": "unharmed: zarar görmemiş, sağ salim; victorious: muzaffer"
            },
            {
                "id": 239,
                "text": "However, the scheduled train to New York had departed hours ago: Fogg was now twenty hours behind schedule.",
                "translation": "Fakat New York'a gidecek tarifeli tren saatler önce kalkmıştı: Fogg artık takvimin yirmi saat gerisindeydi.",
                "notes": "behind schedule: takvimin gerisinde; scheduled train: tarifeli tren"
            },
            {
                "id": 240,
                "text": "Fix brought an inventive American who offered to take them across the frozen snowfields in a sail-powered sledge.",
                "translation": "Fix, rüzgar yelkeniyle çalışan bir kızakla onları donmuş karlı ovalardan geçirmeyi teklif eden yaratıcı bir Amerikalı getirdi.",
                "notes": "sail-powered sledge: yelkenli kar kızağı; frozen snowfield: donmuş karlı ova"
            }
        ]
    },

    # Page 13 (Sentences 241-260)
    {
        "page_no": 13,
        "title": "Burning the Ship Henrietta on the Atlantic",
        "tr_title": "Atlantik'te Henrietta Gemisini Yakarak Yarış",
        "vocab_focus": [
            ("sledge", "kızak"),
            ("sail", "yelken"),
            ("coal", "kömür"),
            ("steamer", "buharlı gemi"),
            ("bribe", "rüşvet vermek"),
            ("mutiny", "gemide kumandayı ele alma"),
            ("wood", "ahşap, odun"),
            ("Atlantic", "Atlantik Okyanusu")
        ],
        "sentences": [
            {
                "id": 241,
                "text": "The wooden sledge had large skates and a vast sail that caught the freezing western gale.",
                "translation": "Tahta kızağın büyük kızak patenleri ve dondurucu batı rüzgarını yakalayan devasa bir yelkeni vardı.",
                "notes": "freezing gale: dondurucu fırtına; skates: patenler, kızak demirleri"
            },
            {
                "id": 242,
                "text": "It glided over the icy snow at sixty miles an hour, arriving at Omaha station by afternoon.",
                "translation": "Buzlu karlar üzerinde saatte altmış mil hızla süzüldü ve öğleden sonra Omaha istasyonuna vardı.",
                "notes": "glide over: üzerinde kayıp süzülmek; icy snow: buzlu kar"
            },
            {
                "id": 243,
                "text": "From Omaha, express trains carried them swiftly through Chicago to the bustling city of New York.",
                "translation": "Omaha'dan kalkan ekspres trenler onları Chicago üzerinden hızla hareketli New York şehrine ulaştırdı.",
                "notes": "bustling city: hareketli / kalabalık şehir; swiftly: hızla"
            },
            {
                "id": 244,
                "text": "When they reached the Hudson River quay at eleven-fifteen on December the eleventh, their hearts sank.",
                "translation": "On bir Aralık'ta saat on biri on beş geçe Hudson Nehri rıhtımına vardıklarında yürekleri ağızlarına geldi.",
                "notes": "hearts sank: yürekleri cız etmek, umutları yıkılmak; quay: rıhtım"
            },
            {
                "id": 245,
                "text": "The Liverpool mail steamer China had sailed out into the Atlantic just forty-five minutes earlier.",
                "translation": "Liverpool posta vapuru China, yalnızca kırk beş dakika önce Atlantik'e açılmıştı.",
                "notes": "mail steamer: posta vapuru; forty-five minutes earlier: kırk beş dakika önce"
            },
            {
                "id": 246,
                "text": "No other transatlantic passenger ship was scheduled to depart for the next three days.",
                "translation": "Önümüzdeki üç gün boyunca sefere çıkacak başka hiçbir transatlantik yolcu gemisi bulunmuyordu.",
                "notes": "transatlantic: okyanus aşırı; scheduled to depart: kalkışı planlanmış"
            },
            {
                "id": 247,
                "text": "Phileas Fogg remained completely unperturbed and checked into a nearby hotel for the night.",
                "translation": "Phileas Fogg istifini zerrece bozmadı ve geceyi geçirmek üzere yakındaki bir otele yerleşti.",
                "notes": "unperturbed: sarsılmamış, sakin; check into hotel: otele yerleşmek"
            },
            {
                "id": 248,
                "text": "The next morning, he combed the New York docks until he found an iron trading steamer named the Henrietta.",
                "translation": "Ertesi sabah, Henrietta adında demir bir ticaret buharlısı bulana kadar New York rıhtımlarını didik didik aradı.",
                "notes": "comb docks: rıhtımları taramak; trading steamer: ticaret gemisi"
            },
            {
                "id": 249,
                "text": "Her skipper, Captain Speedy, was a gruff old sailor bound for Bordeaux, France.",
                "translation": "Kaptanı Kaptan Speedy, Fransa'nın Bordeaux limanına gitmekte olan huysuz yaşlı bir denizciydi.",
                "notes": "gruff sailor: huysuz denizci; skipper: gemi kaptanı"
            },
            {
                "id": 250,
                "text": "\"Will you carry us to Liverpool?\" Mr. Fogg asked. \"No, I carry no passengers!\" Speedy snapped.",
                "translation": "\"Bizi Liverpool'a götürür müsünüz?\" diye sordu Bay Fogg. \"Hayır, yolcu taşımam ben!\" diye kestirip attı Speedy.",
                "notes": "snap: terslemek, sertçe çıkışmak; carry passengers: yolcu taşımak"
            },
            {
                "id": 251,
                "text": "\"I will give you two thousand dollars per person to take us to Bordeaux,\" Fogg offered.",
                "translation": "\"Bizi Bordeaux'ya götürmeniz için kişi başı iki bin dolar veririm,\" diye teklif etti Fogg.",
                "notes": "per person: kişi başına; offer: teklif etmek"
            },
            {
                "id": 252,
                "text": "The greedy captain could not resist eight thousand dollars and let them board immediately.",
                "translation": "Açgözlü kaptan sekiz bin dolara direnemedi ve hemen gemiye binmelerine izin verdi.",
                "notes": "greedy: açgözlü; cannot resist: karşı koyamamak"
            },
            {
                "id": 253,
                "text": "Once out on the high seas, Fogg used his banknotes to bribe the crew to his side.",
                "translation": "Açık denize çıkar çıkmaz Fogg, mürettebatı kendi tarafına çekmek için banknotlarıyla onları ikna etti.",
                "notes": "high seas: açık deniz; bribe the crew: tayfayı kendi tarafına bağlamak"
            },
            {
                "id": 254,
                "text": "He locked the howling Captain Speedy safely in his cabin and took command of the vessel himself.",
                "translation": "Avaz avaz bağıran Kaptan Speedy'yi kamarasına emniyetle kilitledi ve geminin kumandasını bizzat devraldı.",
                "notes": "howling: bağırıp çağıran; take command: kumandayı devralmak"
            },
            {
                "id": 255,
                "text": "He altered course directly for Liverpool, driving the engines at top boiler pressure.",
                "translation": "Rotayı doğrudan Liverpool'a çevirdi ve kazanları azami basınçta çalıştırarak makineleri zorladı.",
                "notes": "alter course: rotayı değiştirmek; boiler pressure: kazan basıncı"
            },
            {
                "id": 256,
                "text": "On December the sixteenth, the chief engineer reported that all the coal would be exhausted within twenty-four hours.",
                "translation": "On altı Aralık'ta başçarkçı, bütün kömürün yirmi dört saat içinde tükeneceğini bildirdi.",
                "notes": "chief engineer: başçarkçı; exhaust coal: kömürü tüketmek"
            },
            {
                "id": 257,
                "text": "Mr. Fogg released Captain Speedy and bought the entire wooden superstructure of the ship for sixty thousand dollars.",
                "translation": "Bay Fogg Kaptan Speedy'yi serbest bıraktı ve geminin bütün ahşap üst güvertesini altmış bin dolara satın aldı.",
                "notes": "superstructure: üst güverte yapısı; release: serbest bırakmak"
            },
            {
                "id": 258,
                "text": "Axes were distributed, and the crew chopped down masts, wooden decks, cabins, and furniture for fuel.",
                "translation": "Baltalar dağıtıldı ve mürettebat yakıt yapmak için direkleri, ahşap güverteleri, kamaraları ve mobilyaları parçaladı.",
                "notes": "chop down: balta ile kesmek; furniture for fuel: yakıt için mobilya"
            },
            {
                "id": 259,
                "text": "Feeding on her own wooden hull, the smoking Henrietta ploughed through the stormy Irish Sea.",
                "translation": "Kendi ahşap gövdesiyle beslenen dumanı tüten Henrietta, fırtınalı İrlanda Denizi'ni yarıp geçti.",
                "notes": "feed on hull: kendi gövdesiyle beslenmek; plough through: yarıp geçmek"
            },
            {
                "id": 260,
                "text": "They berthed at Queenstown harbor in Ireland, where an express mail train carried them to Dublin.",
                "translation": "İrlanda'daki Queenstown limanına yanaştılar; oradan ekspres posta treni onları Dublin'e taşıdı.",
                "notes": "berth at harbor: limana yanaşmak; mail train: posta treni"
            }
        ]
    },

    # Page 14 (Sentences 261-280)
    {
        "page_no": 14,
        "title": "Arrest in Liverpool and Despair",
        "tr_title": "Liverpool'da Haksız Tutuklama ve Çaresizlik",
        "vocab_focus": [
            ("customs", "gümrük"),
            ("arrest", "tutuklama"),
            ("warrant", "yakalama müzekkeresi"),
            ("cell", "hücre, zindan"),
            ("ruined", "mahvolmuş, iflas etmiş"),
            ("innocent", "masum"),
            ("punch", "yumruk"),
            ("special train", "özel kiralık tren")
        ],
        "sentences": [
            {
                "id": 261,
                "text": "From Dublin, a fast steamer raced across the Irish Sea to Liverpool harbor.",
                "translation": "Dublin'den kalkan hızlı bir buharlı gemi, İrlanda Denizi'ni aşarak Liverpool limanına vardı.",
                "notes": "race across: hızla geçmek; harbor: liman"
            },
            {
                "id": 262,
                "text": "At twenty minutes to twelve on Saturday, December the twenty-first, Phileas Fogg stepped onto English soil.",
                "translation": "Yirmi bir Aralık Cumartesi günü saat on ikiye yirmi kala, Phileas Fogg İngiliz topraklarına ayak bastı.",
                "notes": "English soil: İngiliz toprağı; step onto: ayak basmak"
            },
            {
                "id": 263,
                "text": "He had nine hours and fifteen minutes left to reach the Reform Club in London.",
                "translation": "Londra'daki Reform Kulübü'ne ulaşmak için önünde dokuz saat on beş dakika kalmıştı.",
                "notes": "nine hours left: dokuz saat kaldı"
            },
            {
                "id": 264,
                "text": "At that very moment, Detective Fix walked up and placed a heavy hand upon Fogg's shoulder.",
                "translation": "Tam o anda Dedektif Fix yaklaştı ve ağır elini Fogg'un omzuna koydu.",
                "notes": "place hand upon: elini üzerine koymak; at that very moment: tam o anda"
            },
            {
                "id": 265,
                "text": "\"In the name of the Queen, I arrest you, Phileas Fogg, for robbing the Bank of England!\" Fix declared.",
                "translation": "\"Kraliçe adına sizi, İngiltere Bankası'nı soymak suçundan tutukluyorum Phileas Fogg!\" diye ilan etti Fix.",
                "notes": "in the name of the Queen: Kraliçe adına; arrest: tutuklamak"
            },
            {
                "id": 266,
                "text": "Passepartout let out a scream of despair, while Princess Aouda looked on in horrified disbelief.",
                "translation": "Passepartout çaresiz bir çığlık attı, Prenses Aouda ise dehşet dolu bir inanamazlıkla baka kaldı.",
                "notes": "scream of despair: çaresizlik çığlığı; horrified disbelief: dehşetli şaşkınlık"
            },
            {
                "id": 267,
                "text": "Phileas Fogg was escorted to a cold stone cell at the Liverpool Custom House and locked inside.",
                "translation": "Phileas Fogg Liverpool Gümrük Binası'ndaki soğuk bir taş hücreye götürüldü ve içeri kilitlendi.",
                "notes": "stone cell: taş hücre; Custom House: gümrük binası"
            },
            {
                "id": 268,
                "text": "He placed his pocket watch on the wooden table and sat motionless upon the bench.",
                "translation": "Cep saatini tahta masanın üzerine koydu ve sıranın üzerinde kıpırdamadan oturdu.",
                "notes": "motionless: hareketsiz; pocket watch: cep saati"
            },
            {
                "id": 269,
                "text": "He was ruined: the wager was lost, his entire fortune gone, and his honor destroyed.",
                "translation": "Mahvolmuştu: iddia kaybedilmiş, bütün serveti gitmiş ve onuru yok edilmişti.",
                "notes": "ruined: mahvolmuş; honor destroyed: onuru zedelenmiş"
            },
            {
                "id": 270,
                "text": "Hours ticked away in deafening silence; the clock showed two o'clock, then two-thirty.",
                "translation": "Saatler sağır edici bir sessizlikte akıp gitti; saat ikiyi, ardından iki buçuğu gösterdi.",
                "notes": "tick away: tıkır tıkır geçmek; deafening silence: sağır edici sessizlik"
            },
            {
                "id": 271,
                "text": "At thirty-three minutes past two, a tremendous commotion erupted outside the cell corridor.",
                "translation": "İkiyi otuz üç geçe, hücre koridorunun dışında büyük bir kargaşa patlak verdi.",
                "notes": "commotion: kargaşa, gürültü patırtı; erupt: patlak vermek"
            },
            {
                "id": 272,
                "text": "The door flew open, and Fix stumbled in, breathless, disheveled, and weeping with remorse.",
                "translation": "Kapı ardına kadar açıldı ve Fix nefes nefese, saçı başı dağınık ve pişmanlıktan ağlayarak içeri daldı.",
                "notes": "stumble in: sendeleyerek içeri girmek; disheveled: dağınık; remorse: pişmanlık"
            },
            {
                "id": 273,
                "text": "\"Forgive me, Mr. Fogg!\" Fix choked out, \"the real bank robber was arrested in Edinburgh three days ago!\"",
                "translation": "\"Beni affedin Bay Fogg!\" diye hıçkırdı Fix, \"gerçek banka soyguncusu üç gün önce Edinburgh'da yakalandı!\"",
                "notes": "forgive: affetmek; choke out: boğazı düğümlenerek söylemek"
            },
            {
                "id": 274,
                "text": "For the first time in his life, Phileas Fogg lost his legendary self-control.",
                "translation": "Hayatında ilk defa Phileas Fogg o dillere destan otokontrolünü kaybetti.",
                "notes": "self-control: otokontrol, özdenetim; legendary: efsanevi"
            },
            {
                "id": 275,
                "text": "He stepped forward, drew back both arms, and knocked Detective Fix senseless with two swift punches.",
                "translation": "İleri doğru bir adım attı, iki kolunu birden gerdi ve iki çevik yumrukla Dedektif Fix'i kendinden geçirdi.",
                "notes": "draw back arms: kollarını geriye çekmek; swift punches: çevik yumruklar"
            },
            {
                "id": 276,
                "text": "Passepartout and Aouda cheered as Fogg walked out into the street and hailed a cab.",
                "translation": "Fogg sokağa çıkıp bir fayton çağırırken Passepartout ve Aouda sevinçle tezahürat yaptılar.",
                "notes": "hail a cab: taksi / fayton çağırmak; cheer: alkışlamak"
            },
            {
                "id": 277,
                "text": "They rushed to the railway station, but the regular express for London had already left.",
                "translation": "Tren garına koştular fakat Londra'ya giden tarifeli ekspres çoktan kalkmıştı.",
                "notes": "rush to station: istasyona koşmak; regular express: tarifeli ekspres"
            },
            {
                "id": 278,
                "text": "Mr. Fogg chartered a special express train for five hundred pounds to race to the capital.",
                "translation": "Bay Fogg başkente yetişmek üzere beş yüz sterlin karşılığında özel bir ekspres tren kiraladı.",
                "notes": "charter a train: özel tren kiralamak; capital: başkent"
            },
            {
                "id": 279,
                "text": "The locomotive dashed through the winter dusk, but track delays slowed their desperate race.",
                "translation": "Lokomotif kış alacakaranlığında hızla aktı fakat raylardaki gecikmeler bu çaresiz yarışı yavaşlattı.",
                "notes": "winter dusk: kış alacakaranlığı; desperate race: çaresiz yarış"
            },
            {
                "id": 280,
                "text": "When they reached the London terminus, the station clock struck ten minutes to nine: they were five minutes late!",
                "translation": "Londra garına vardıklarında istasyon saati dokuza on geçeyi vurdu: beş dakika geç kalmışlardı!",
                "notes": "terminus: son istasyon, gar; five minutes late: beş dakika geç"
            }
        ]
    },

    # Page 15 (Sentences 281-300)
    {
        "page_no": 15,
        "title": "The Gained Day and Victory at the Reform Club",
        "tr_title": "Kazanılan 24 Saat ve Büyük Zafer",
        "vocab_focus": [
            ("meridian", "meridyen, boylam"),
            ("sunrise", "gün doğumu"),
            ("circumnavigation", "dünyayı dolaşma"),
            ("parish", "mahalle kilisesi / cemaati"),
            ("reverend", "rahip, din adamı"),
            ("saloon", "kulüp salonu"),
            ("victory", "zafer"),
            ("marriage", "evlilik")
        ],
        "sentences": [
            {
                "id": 281,
                "text": "Phileas Fogg returned quietly to his house on Savile Row, having accepted his complete ruin.",
                "translation": "Phileas Fogg tam yıkımını kabullenmiş bir halde Savile Row'daki evine sessizce döndü.",
                "notes": "quietly: sessizce; complete ruin: tam yıkım, iflas"
            },
            {
                "id": 282,
                "text": "He shut himself in his room all of Sunday, methodically settling his financial affairs.",
                "translation": "Bütün pazar günü kendini odasına kapattı ve mali işlerini metodik bir şekilde düzenledi.",
                "notes": "shut oneself: kendini kapatmak; financial affairs: mali işler"
            },
            {
                "id": 283,
                "text": "In the evening, he visited Princess Aouda and apologized for bringing her to a home of poverty.",
                "translation": "Akşamleyin Prenses Aouda'yı ziyaret etti ve onu yoksul bir eve getirdiği için özür diledi.",
                "notes": "poverty: yoksulluk; apologize: özür dilemek"
            },
            {
                "id": 284,
                "text": "\"Madam, I was rich when I promised to support you, but now I am ruined,\" he said gently.",
                "translation": "\"Madam, size kol kanat germeye söz verdiğimde zengindim, oysa şimdi mahvoldum,\" dedi nazikçe.",
                "notes": "support: destek olmak, kol kanat germek; ruined: iflas etmiş"
            },
            {
                "id": 285,
                "text": "Aouda looked tenderly into his eyes and replied: \"Mr. Fogg, will you have me as your wife?\"",
                "translation": "Aouda şefkatle onun gözlerinin içine baktı ve cevap verdi: \"Bay Fogg, beni eşiniz olarak kabul eder misiniz?\"",
                "notes": "look tenderly: şefkatle bakmak; wife: eş, hanım"
            },
            {
                "id": 286,
                "text": "\"I love you!\" cried the gentleman, his cold mask melting away as he embraced her.",
                "translation": "\"Sizi seviyorum!\" diye haykırdı beyefendi; kadına sarılırken soğuk maskesi tamamen eriyip gitmişti.",
                "notes": "melt away: eriyip yok olmak; embrace: kucaklamak, sarılmak"
            },
            {
                "id": 287,
                "text": "Fogg called Passepartout and told him to notify the Reverend at Marylebone parish for a Monday wedding.",
                "translation": "Fogg Passepartout'yu çağırdı ve pazartesi günü yapılacak düğün için Marylebone kilisesi rahibine haber vermesini söyledi.",
                "notes": "notify: bildirmek, haber vermek; parish: kilise cemaati"
            },
            {
                "id": 288,
                "text": "Passepartout ran out into the rainy London evening on his joyous errand.",
                "translation": "Passepartout bu sevinçli vazifeyi yerine getirmek için yağmurlu Londra akşamına fırladı.",
                "notes": "joyous errand: sevinçli vazife / görev; run out: dışarı koşmak"
            },
            {
                "id": 289,
                "text": "Twenty minutes later, he burst back into Fogg's study like a madman, his hair standing on end.",
                "translation": "Yirmi dakika sonra saçları diken diken olmuş bir deli gibi Fogg'un çalışma odasına geri daldı.",
                "notes": "burst back: içeri dalmak; hair standing on end: saçları diken diken"
            },
            {
                "id": 290,
                "text": "\"Master! Monsieur! It is impossible! The wedding cannot take place tomorrow!\" he gasped.",
                "translation": "\"Efendim! Mösyö! İmkansız! Düğün yarın yapılamaz!\" diye nefes nefese haykırdı.",
                "notes": "take place: gerçekleşmek, yapılmak; gasp: soluk soluğa kalmak"
            },
            {
                "id": 291,
                "text": "\"Why?\" asked Mr. Fogg. \"Because tomorrow is Sunday, and today is Saturday!\" the Frenchman screamed.",
                "translation": "\"Nedenmiş o?\" diye sordu Bay Fogg. \"Çünkü yarın pazar, bugün ise cumartesi!\" diye bağırdı Fransız.",
                "notes": "scream: haykırmak; because: çünkü"
            },
            {
                "id": 292,
                "text": "By traveling eastward toward the sun, Phileas Fogg had gained twenty-four hours without knowing it!",
                "translation": "Güneşe doğru doğu yönünde seyahat ettiği için Phileas Fogg hiç farkında olmadan yirmi dört saat kazanmıştı!",
                "notes": "gain twenty-four hours: yirmi dört saat kazanmak; eastward: doğuya doğru"
            },
            {
                "id": 293,
                "text": "Each degree of longitude crossed eastwards shortened each day by four minutes, adding up to a full extra day!",
                "translation": "Doğuya doğru aşılan her boylam derecesi her günü dört dakika kısaltmış ve bu da tam bir ek güne ulaşmıştı!",
                "notes": "longitude: boylam; add up to: toplamda ...e ulaşmak"
            },
            {
                "id": 294,
                "text": "\"You have only ten minutes to reach the Reform Club!\" shouted Passepartout, dragging his master outside.",
                "translation": "\"Reform Kulübü'ne varmak için sadece on dakikanız kaldı!\" diye bağırdı Passepartout, efendisini dışarı sürükleyerek.",
                "notes": "ten minutes left: on dakika kaldı; drag outside: dışarı sürüklemek"
            },
            {
                "id": 295,
                "text": "At the Reform Club, the five gentlemen were counting down the seconds around the whist table.",
                "translation": "Reform Kulübü'nde beş beyefendi vist masasının etrafında saniyeleri sayıyordu.",
                "notes": "count down seconds: saniyeleri saymak"
            },
            {
                "id": 296,
                "text": "\"Forty-two minutes past eight... forty-three... forty-four...\" Andrew Stuart called out tense seconds.",
                "translation": "\"Sekizi kırk iki geçiyor... kırk üç... kırk dört...\" diyerek Andrew Stuart gergin saniyeleri saydı.",
                "notes": "tense seconds: gergin saniyeler; call out: sesli saymak"
            },
            {
                "id": 297,
                "text": "On the stroke of eighty-forty-five, the mahogany doors swung open amidst tremendous roaring cheers from the crowd.",
                "translation": "Sekizi kırk beş vurduğu anda, kalabalığın muazzam tezahüratları arasında maun kapılar ardına kadar açıldı.",
                "notes": "on the stroke of: tam vaktinde vurduğunda; roaring cheers: coşkulu tezahüratlar"
            },
            {
                "id": 298,
                "text": "Phileas Fogg stepped into the saloon and said calmly: \"Here I am, gentlemen!\"",
                "translation": "Phileas Fogg salona adım attı ve sakince söyledi: \"İşte geldim beyler!\"",
                "notes": "step into: adım atmak; calmly: sakince"
            },
            {
                "id": 299,
                "text": "He had won the wager, circled the globe in seventy-nine days, and saved his fortune from ruin.",
                "translation": "Bahsi kazanmış, yerküreyi yetmiş dokuz günde dolaşmış ve servetini iflastan kurtarmıştı.",
                "notes": "circle the globe: dünyayı dolaşmak; win the wager: bahsi kazanmak"
            },
            {
                "id": 300,
                "text": "Yet his greatest prize was the charming Princess Aouda, who had made him the happiest of men.",
                "translation": "Yine de onun en büyük ödülü, kendisini insanların en mutlusu yapan büyüleyici Prenses Aouda olmuştu.",
                "notes": "greatest prize: en büyük ödül; charming: büyüleyici, sevimli"
            }
        ]
    }
]

def main():
    total_pages = len(pages_data)
    total_sentences = sum(len(p["sentences"]) for p in pages_data)
    total_vocab = sum(len(p.get("vocab_focus", [])) for p in pages_data)

    print(f"Book 21 Data Verification:")
    print(f"Total Pages: {total_pages} (Target: 15)")
    print(f"Total Sentences: {total_sentences} (Target: 300)")
    print(f"Total Vocab Items: {total_vocab} (Target: 120)")

    assert total_pages == 15, f"Expected 15 pages, got {total_pages}"
    assert total_sentences == 300, f"Expected 300 sentences, got {total_sentences}"
    assert total_vocab == 120, f"Expected 120 vocab items, got {total_vocab}"

    ids = []
    for p in pages_data:
        for s in p["sentences"]:
            ids.append(s["id"])
    assert ids == list(range(1, 301)), "Sentence IDs are not continuous 1..300!"

    out_file = os.path.join(os.path.dirname(__file__), "book_21_data.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('BOOK_TITLE = "Around the World in Eighty Days"\n')
        f.write('AUTHOR = "Jules Verne"\n')
        f.write("PAGES_DATA = ")
        import pprint
        f.write(pprint.pformat(pages_data, indent=4, width=120))
        f.write("\n")

    print(f"Successfully wrote {out_file}")

if __name__ == "__main__":
    main()
