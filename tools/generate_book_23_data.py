# -*- coding: utf-8 -*-
"""
Generator script for Book 23: "The Secret Garden" by Frances Hodgson Burnett.
15 Pages x 20 Sentences = Exactly 300 Sentences (Continuous IDs 1 to 300).
8 Vocabulary Focus items per page = Exactly 120 Target Vocabulary Items.
CEFR Level: A2-B1 Graded Reader Edition.
"""

import os

pages_data = [
    # Page 1 (Sentences 1-20)
    {
        "page_no": 1,
        "title": "There Is No One Left",
        "tr_title": "Kimsesiz Kalan Mary Lennox",
        "vocab_focus": [
            ("tyrannical", "zorba, dediğim dedik"),
            ("cholera", "kolera salgını"),
            ("bungalow", "tek katlı yazlık ev"),
            ("ayah", "aya (Hintli çocuk bakıcısı)"),
            ("orphan", "öksüz, yetim"),
            ("sour", "ekşi suratlı, huysuz"),
            ("neglected", "ilgisiz bırakılmış"),
            ("servant", "hizmetkar")
        ],
        "sentences": [
            {
                "id": 1,
                "text": "When Mary Lennox was sent to Misselthwaite Manor to live with her uncle, everybody said she was the most disagreeable child ever seen.",
                "translation": "Mary Lennox amcasıyla yaşamak üzere Misselthwaite Malikanesi'ne gönderildiğinde, herkes onun şimdiye kadar görülen en sevimsiz çocuk olduğunu söylerdi.",
                "notes": "disagreeable: huysuz, sevimsiz; manor: malikane"
            },
            {
                "id": 2,
                "text": "She had a little thin face, a little thin body, delicate yellow hair, and an sour expression.",
                "translation": "Küçücük zayıf bir yüzü, çelimsiz bir bedeni, cılız sarı saçları ve ekşi bir yüz ifadesi vardı.",
                "notes": "sour expression: ekşi / hoşnutsuz ifade; delicate: narin, cılız"
            },
            {
                "id": 3,
                "text": "Her hair was yellow, and her face was yellow because she had been born in India and had always been sickly.",
                "translation": "Saçları sarıydı ve yüzü de sararmıştı çünkü Hindistan'da doğmuştu ve daima hastalıklı bir çocuk olmuştu.",
                "notes": "sickly: hastalıklı, çelimsiz; born in India: Hindistan'da doğmuş"
            },
            {
                "id": 4,
                "text": "Her father had held a high position under the English Government and was always busy.",
                "translation": "Babası İngiliz Hükümeti emrinde yüksek bir mevkide bulunuyordu ve daima meşguldü.",
                "notes": "high position: yüksek mevki; English Government: İngiliz Hükümeti"
            },
            {
                "id": 5,
                "text": "Her mother had been a great beauty who cared only to go to parties and amuse herself with fashionable people.",
                "translation": "Annesi ise yalnızca partilere gitmeyi ve sosyetik insanlarla eğlenmeyi dert edinen büyük bir güzeldi.",
                "notes": "amuse oneself: eğlenmek, vakit geçirmek; fashionable people: sosyetik insanlar"
            },
            {
                "id": 6,
                "text": "She had not wanted a little girl at all, and so when Mary was born, she handed her over to an Indian Ayah.",
                "translation": "Aslında hiç kız çocuğu istememişti; bu yüzden Mary doğduğunda onu derhal Hintli bir çocuk bakıcısına teslim etti.",
                "notes": "hand over: teslim etmek; Ayah: Hintli dadı / bakıcı"
            },
            {
                "id": 7,
                "text": "The native servants were commanded to obey Mary in everything, so she became tyrannical and selfish.",
                "translation": "Yerli hizmetkarlara Mary'nin her istediğine itaat etmeleri emredilmişti, bu yüzden kız zorba ve bencil biri haline geldi.",
                "notes": "tyrannical: zorba, dediğim dedik; obey: itaat etmek"
            },
            {
                "id": 8,
                "text": "By the time she was nine years old, she was as tyrannical and selfish a little pig as ever lived.",
                "translation": "Dokuz yaşına bastığında, yeryüzünde yaşamış en zorba ve bencil küçük canavar kadar huysuzdu.",
                "notes": "by the time: ...e kadar; selfish: bencil"
            },
            {
                "id": 9,
                "text": "One terribly hot morning, when she was about nine years old, she awoke feeling cross and irritable.",
                "translation": "Yaklaşık dokuz yaşlarında olduğu dayanılmaz derecede sıcak bir sabah, aksi ve asabi hissederek uyandı.",
                "notes": "cross and irritable: aksi ve asabi; awake: uyanmak"
            },
            {
                "id": 10,
                "text": "She was furious because her Ayah did not come to dress her, and new servants looked frightened.",
                "translation": "Bakıcısı onu giydirmeye gelmediği için çok öfkelendi ve ortalıktaki yeni hizmetkarlar dehşet içinde görünüyordu.",
                "notes": "furious: çok öfkeli; frightened: korkmuş"
            },
            {
                "id": 11,
                "text": "Nobody remembered to bring her breakfast, and mysterious wailing sounds came from the servants' quarters.",
                "translation": "Kimse ona kahvaltı getirmeyi akıl etmedi ve hizmetkar koğuşlarından gizemli feryat sesleri yükseldi.",
                "notes": "wailing sounds: feryat sesleri; servants' quarters: hizmetkar koğuşları"
            },
            {
                "id": 12,
                "text": "A deadly cholera outbreak had broken out in its most violent form across the military compound.",
                "translation": "Askeri yerleşkenin her yanına en şiddetli biçimiyle ölümcül bir kolera salgını yayılmıştı.",
                "notes": "cholera outbreak: kolera salgını; military compound: askeri garnizon / lojman"
            },
            {
                "id": 13,
                "text": "People were dying like flies; soldiers and frightened servants fled the infected house in panic.",
                "translation": "İnsanlar sinekler gibi ölüyordu; askerler ve korkuya kapılan hizmetkarlar panik içinde hastalıklı evi terk edip kaçtı.",
                "notes": "dying like flies: sinekler gibi ölmek; infected house: bulaşıcı hastalıklı ev"
            },
            {
                "id": 14,
                "text": "Mary hid herself in the nursery, crying and sleeping through the terrible, deserted day.",
                "translation": "Mary çocuk odasına saklandı; o korkunç, terk edilmiş gün boyunca ağlayıp uyuyarak bekledi.",
                "notes": "nursery: çocuk odası; deserted day: kimsesiz / terk edilmiş gün"
            },
            {
                "id": 15,
                "text": "She ate some dry biscuits and fruit that she found on the sideboard in the dining-room.",
                "translation": "Yemek odasındaki büfede bulduğu birkaç kuru bisküviyi ve meyveyi yedi.",
                "notes": "sideboard: büfe; dry biscuits: kuru bisküviler"
            },
            {
                "id": 16,
                "text": "By evening, an awful stillness fell over the entire bungalow: not a footstep could be heard.",
                "translation": "Akşama doğru bütün yazlık evin üzerine ürkütücü bir sessizlik çöktü: tek bir ayak sesi bile duyulmuyordu.",
                "notes": "awful stillness: ürkütücü sessizlik; bungalow: tek katlı ev"
            },
            {
                "id": 17,
                "text": "Two British officers entered the silent house the next morning, looking for survivors.",
                "translation": "Ertesi sabah hayatta kalanları aramak üzere iki İngiliz subayı sessiz eve girdi.",
                "notes": "officers: subaylar; survivors: hayatta kalanlar"
            },
            {
                "id": 18,
                "text": "\"The father, the mother, and the servants are all dead,\" one officer said solemnly.",
                "translation": "\"Baba, anne ve hizmetkarların hepsi ölmüş,\" dedi subaylardan biri üzüntüyle.",
                "notes": "solemnly: hüzünle, ciddiyetle; all dead: hepsi ölü"
            },
            {
                "id": 19,
                "text": "Then they found Mary standing in the center of the nursery playing with bits of rust-colored earth.",
                "translation": "Sonra Mary'yi çocuk odasının ortasında pas rengi toprak parçalarıyla oynarken buldular.",
                "notes": "center of nursery: çocuk odasının ortası; bits of earth: toprak parçaları"
            },
            {
                "id": 20,
                "text": "\"Poor little thing!\" the officer gasped in amazement, \"There is nobody left here except this lonely child!\"",
                "translation": "\"Zavallı yavrucak!\" diye şaşkınlıkla nefesini tuttu subay, \"Bu yapayalnız çocuktan başka burada hiç kimse kalmamış!\"",
                "notes": "poor little thing: zavallı küçük şey; nobody left: kimse kalmamış"
            }
        ]
    },

    # Page 2 (Sentences 21-40)
    {
        "page_no": 2,
        "title": "The Journey to Misselthwaite Manor",
        "tr_title": "Misselthwaite Malikanesi'ne Yolculuk",
        "vocab_focus": [
            ("manor", "malikane, büyük konak"),
            ("moor", "bozkır, çorak fundalık"),
            ("housekeeper", "kahya kadın"),
            ("hunchback", "kambur"),
            ("gloomy", "kasvetli, iç karartıcı"),
            ("carriage", "atlı fayton, vagon"),
            ("station", "tren garı"),
            ("solitude", "yalnızlık, inziva")
        ],
        "sentences": [
            {
                "id": 21,
                "text": "Mary was taken to England to live with her only living relative, Mr. Archibald Craven.",
                "translation": "Mary, hayattaki tek akrabası olan Bay Archibald Craven ile yaşamak üzere İngiltere'ye götürüldü.",
                "notes": "living relative: hayattaki akraba; taken to: ...e götürüldü"
            },
            {
                "id": 22,
                "text": "He was her uncle, her mother's sister's husband, and lived in Yorkshire at Misselthwaite Manor.",
                "translation": "Annesinin kız kardeşinin kocası olan eniştesiydi ve Yorkshire'daki Misselthwaite Malikanesi'nde yaşıyordu.",
                "notes": "uncle: enişte / amca; manor: malikane"
            },
            {
                "id": 23,
                "text": "People whispered that Mr. Craven was a strange, gloomy hunchback who spoke to almost nobody.",
                "translation": "İnsanlar fısıldaşarak Bay Craven'ın hemen hemen hiç kimseyle konuşmayan tuhaf, kasvetli bir kambur olduğunu söylüyorlardı.",
                "notes": "hunchback: kambur adam; gloomy: kasvetli"
            },
            {
                "id": 24,
                "text": "He lived in a huge, dark house with nearly a hundred rooms shut up and locked.",
                "translation": "Yaklaşık yüz odası kilitlenip kapatılmış devasa, karanlık bir konakta yaşıyordu.",
                "notes": "shut up and locked: kapatılmış ve kilitli; huge dark house: devasa karanlık ev"
            },
            {
                "id": 25,
                "text": "Mrs. Medlock, the stout housekeeper of Misselthwaite Manor, arrived in London to fetch Mary.",
                "translation": "Misselthwaite Malikanesi'nin iri yapılı kahyası Bayan Medlock, Mary'yi almak üzere Londra'ya geldi.",
                "notes": "stout housekeeper: iri yapılı kahya kadın; fetch: alıp getirmek"
            },
            {
                "id": 26,
                "text": "She was a woman with very round, red cheeks, and sharp black eyes in a bonnet with purple ribbons.",
                "translation": "Mor kurdeleli bir başlığın içinde yuvarlak kırmızı yanakları ve keskin siyah gözleri olan bir kadındı.",
                "notes": "bonnet: başlık, bone; red cheeks: kırmızı yanaklar"
            },
            {
                "id": 27,
                "text": "\"I never saw such a plain, sullen little piece of baggage in all my life,\" Mrs. Medlock thought to herself.",
                "translation": "\"Hayatımda bu kadar çirkin ve asık suratlı bir bücür görmedim,\" diye düşündü Bayan Medlock kendi kendine.",
                "notes": "plain: gösterişsiz, çirkin; sullen: asık suratlı, küskün"
            },
            {
                "id": 28,
                "text": "They boarded the train for the north, traveling for hours through rain, fog, and industrial towns.",
                "translation": "Kuzeye giden trene bindiler; yağmur, sis ve sanayi kasabaları arasından saatlerce yolculuk ettiler.",
                "notes": "board train: trene binmek; industrial towns: sanayi kasabaları"
            },
            {
                "id": 29,
                "text": "Mary sat staring coldly out of the window, refusing to speak unless spoken to.",
                "translation": "Mary pencereden dışarı soğukça bakarak oturdu; kendisine sorulmadıkça tek kelime konuşmayı reddetti.",
                "notes": "stare coldly: soğukça bakmak; refuse to speak: konuşmayı reddetmek"
            },
            {
                "id": 30,
                "text": "\"You needn't expect to see Mr. Craven, because ten to one you won't,\" Mrs. Medlock told her bluntly.",
                "translation": "\"Bay Craven'ı görmeyi hiç bekleme, çünkü ona bir ihtimalle onu göremeyeceksin,\" dedi Bayan Medlock dobra dobra.",
                "notes": "bluntly: dobra dobra, açıkça; ten to one: ona bir ihtimal"
            },
            {
                "id": 31,
                "text": "\"He won't be bothered with children; he has a crooked back and shuts himself away from the world.\"",
                "translation": "\"Çocuklarla uğraşacak hali yok; sırtı eğridir ve kendini dünyadan tamamen soyutlamıştır.\"",
                "notes": "crooked back: eğri sırt / kambur; shut oneself away: kendini soyutlamak"
            },
            {
                "id": 32,
                "text": "\"When his lovely young wife died ten years ago, he locked up her favorite walled garden forever.\"",
                "translation": "\"Güzel genç karısı on yıl önce öldüğünde, kadının en sevdiği taş duvarlı bahçeyi sonsuza dek kilitledi.\"",
                "notes": "walled garden: etrafı duvarla çevrili bahçe; lock up: kilitlemek"
            },
            {
                "id": 33,
                "text": "\"He buried the key, and nobody has set foot inside that secret garden since that day.\"",
                "translation": "\"Anahtarı toprağa gömdü ve o günden beri o gizli bahçeye tek bir kişi bile ayak basmadı.\"",
                "notes": "bury key: anahtarı gömmek; set foot inside: içine ayak basmak"
            },
            {
                "id": 34,
                "text": "Mary listened intently, feeling a strange curiosity stir in her heart for the first time.",
                "translation": "Mary dikkatle dinledi; ilk defa kalbinde tuhaf bir merakın uyandığını hissetti.",
                "notes": "listen intently: pürdikkat dinlemek; curiosity stir: merakın uyanması"
            },
            {
                "id": 35,
                "text": "They got off at a small, dark country station where a brougham carriage was waiting.",
                "translation": "Kapalı bir atlı faytonun beklediği küçük, karanlık bir köy istasyonunda indiler.",
                "notes": "brougham: kapalı at arabası; country station: köy istasyonu"
            },
            {
                "id": 36,
                "text": "The coachman closed the door, mounted the box, and whipped the two horses into a fast trot.",
                "translation": "Arabacı kapıyı kapattı, sürücü yerine çıktı ve iki atı hızlı bir tırısa kaldırmak için kırbaçladı.",
                "notes": "coachman: arabacı; mount the box: sürücü koltuğuna çıkmak"
            },
            {
                "id": 37,
                "text": "Rain lashed against the carriage windows as they left the cultivated country roads behind.",
                "translation": "İşlenmiş köy yollarını arkalarında bırakırlarken yağmur faytonun pencerelerini kırbaç gibi dövdü.",
                "notes": "rain lashed: yağmur kırbaç gibi dövdü; cultivated: işlenmiş, tarım arazisi"
            },
            {
                "id": 38,
                "text": "The road climbed higher and higher until there were no more trees, hedges, or houses.",
                "translation": "Yol gittikçe yükseldi, ta ki etrafta artık hiç ağaç, çit veya ev kalmayana dek.",
                "notes": "climb higher: daha yükseğe çıkmak; hedges: çalı çitler"
            },
            {
                "id": 39,
                "text": "\"What is this bleak place?\" Mary asked, peering out into the pitch-black windy darkness.",
                "translation": "\"Burası nasıl kasvetli bir yer böyle?\" diye sordu Mary zifiri karanlık, rüzgarlı geceye bakarak.",
                "notes": "bleak place: kasvetli yer; peer out: gözlerini kısıp dışarı bakmak"
            },
            {
                "id": 40,
                "text": "\"This is the moor,\" Mrs. Medlock replied, \"miles and miles of wild land where nothing grows but heather.\"",
                "translation": "\"Burası bozkır,\" diye yanıtladı Bayan Medlock, \"süpürgeotundan başka hiçbir şeyin yetişmediği millerce uzanan vahşi topraklar.\"",
                "notes": "moor: bozkır, fundalık; heather: funda, süpürgeotu"
            }
        ]
    },

    # Page 3 (Sentences 41-60)
    {
        "page_no": 3,
        "title": "Across the Dark Yorkshire Moor",
        "tr_title": "Karanlık Yorkshire Bozkırında",
        "vocab_focus": [
            ("heather", "süpürgeotu, funda"),
            ("gorse", "katırtırnağı (sarı çiçekli dikenli çalı)"),
            ("tempest", "fırtına, kasırga"),
            ("archway", "kemerli kapı geçidi"),
            ("hall", "giriş holü, sofa"),
            ("portrait", "portre"),
            ("footman", "üniformalı uşak"),
            ("corridor", "koridor")
        ],
        "sentences": [
            {
                "id": 41,
                "text": "The wind rushed across the vast open moor with a wild, roaring, wailing sound like a stormy ocean.",
                "translation": "Rüzgar, fırtınalı bir okyanusu andıran vahşi, uğuldayan ve inleyen bir sesle uçsuz bucaksız bozkırın üzerinden esti.",
                "notes": "wailing sound: inleyen ses; stormy ocean: fırtınalı okyanus"
            },
            {
                "id": 42,
                "text": "Mary thought it sounded like hundreds of people were crying out in pain across the darkness.",
                "translation": "Mary bunun, karanlığın ortasında acı içinde feryat eden yüzlerce insanın sesine benzediğini düşündü.",
                "notes": "cry out in pain: acıyla haykırmak; across darkness: karanlık boyunca"
            },
            {
                "id": 43,
                "text": "The carriage rattled over stones and ruts, pitching and tossing through the black night.",
                "translation": "Fayton taşların ve tekerlek izlerinin üzerinde sarsıldı, zifiri gecede bir sağa bir sola yalpalanarak ilerledi.",
                "notes": "ruts: tekerlek izleri; pitch and toss: yalpalamak, savrulmak"
            },
            {
                "id": 44,
                "text": "At last, the horses turned between two stone pillars topped with carved stone griffins.",
                "translation": "Sonunda atlar, tepesinde oyma taş grifon heykelleri bulunan iki taş sütunun arasından saptı.",
                "notes": "carved stone: oyma taş; stone pillar: taş sütun"
            },
            {
                "id": 45,
                "text": "A long avenue of ancient, twisted trees led toward an enormous, sprawling mansion.",
                "translation": "Asırlık, boğumlu ağaçlardan oluşan uzun bir cadde devasa, geniş bir konağa doğru uzanıyordu.",
                "notes": "sprawling mansion: geniş araziye yayılan konak; avenue: ağaçlıklı yol"
            },
            {
                "id": 46,
                "text": "Misselthwaite Manor looked like a dark castle with a low stone porch and tiny lighted windows.",
                "translation": "Misselthwaite Malikanesi, alçak taş verandası ve minik aydınlatılmış pencereleriyle karanlık bir kaleyi andırıyordu.",
                "notes": "stone porch: taş sundurma / veranda; dark castle: karanlık kale"
            },
            {
                "id": 47,
                "text": "A solemn old man in a black coat opened the massive oak door as the carriage halted.",
                "translation": "Fayton durduğunda, siyah paltolu vakur yaşlı bir adam devasa meşe kapıyı açtı.",
                "notes": "solemn old man: vakur yaşlı adam; massive oak door: devasa meşe kapı"
            },
            {
                "id": 48,
                "text": "It was Pitcher, Mr. Craven's personal valet, who looked at Mary with cold indifference.",
                "translation": "Bu, Mary'ye soğuk bir kayıtsızlıkla bakan, Bay Craven'ın özel uşağı Pitcher'dı.",
                "notes": "cold indifference: soğuk kayıtsızlık; valet: özel uşak"
            },
            {
                "id": 49,
                "text": "\"Mr. Craven has gone to London and does not wish to be disturbed upon his return,\" Pitcher stated curtly.",
                "translation": "\"Bay Craven Londra'ya gitti ve dönüşünde rahatsız edilmek istemiyor,\" dedi Pitcher kısaca.",
                "notes": "state curtly: kestirip atmak, kısa söylemek; disturbed: rahatsız edilmiş"
            },
            {
                "id": 50,
                "text": "\"Take the child straight to her rooms and keep her out of sight.\"",
                "translation": "\"Çocuğu doğrudan odalarına götürün ve göz önünden uzak tutun.\"",
                "notes": "out of sight: gözden ırak, görünmez"
            },
            {
                "id": 51,
                "text": "Mrs. Medlock took Mary's hand and led her down long corridors and up stone stairs.",
                "translation": "Bayan Medlock Mary'nin elinden tuttu ve onu uzun koridorlardan geçirip taş merdivenlerden yukarı çıkardı.",
                "notes": "lead: yol göstermek, götürmek; stone stairs: taş merdivenler"
            },
            {
                "id": 52,
                "text": "They passed dark portraits of men in velvet coats and ladies with lace ruffs staring down from the walls.",
                "translation": "Kadife paltolu erkeklerin ve dantel yakalı hanımların duvarlardan aşağı bakan karanlık portrelerinin önünden geçtiler.",
                "notes": "velvet coat: kadife ceket; lace ruff: dantel yaka; portrait: portre"
            },
            {
                "id": 53,
                "text": "Finally, they arrived at a nursery suite where a cheerful fire was crackling in the grate.",
                "translation": "Sonunda ızgarasında neşeli bir ateşin çıtır çıtır yandığı bir çocuk süitine vardılar.",
                "notes": "crackling fire: çıtırdayan ateş; nursery suite: çocuk dairesi"
            },
            {
                "id": 54,
                "text": "Supper was laid out on a round table: cold beef, potatoes, bread, and a jug of fresh milk.",
                "translation": "Yuvarlak bir masanın üzerine akşam yemeği dizilmişti: soğuk sığır eti, patates, ekmek ve bir sürahi taze süt.",
                "notes": "supper: akşam yemeği; jug of milk: süt sürahisi"
            },
            {
                "id": 55,
                "text": "\"Here are your rooms,\" Mrs. Medlock said sharply, \"you have this nursery and the bedroom next door.\"",
                "translation": "\"İşte senin odaların burası,\" dedi Bayan Medlock sertçe, \"bu çocuk odası ve yandaki yatak odası senin.\"",
                "notes": "say sharply: sertçe söylemek; next door: bitişikteki"
            },
            {
                "id": 56,
                "text": "\"You are not to go wandering about the house; Mr. Craven will not have it!\"",
                "translation": "\"Evin içinde avare avare dolaşmayacaksın; Bay Craven buna asla izin vermez!\"",
                "notes": "wander about: etrafta gezinmek; will not have it: buna izin vermez"
            },
            {
                "id": 57,
                "text": "Mary felt so contrary that she refused to touch the cold supper, crossing her arms stubbornly.",
                "translation": "Mary o kadar huysuz hissediyordu ki kollarını inatla kavuşturup soğuk yemeğe dokunmayı reddetti.",
                "notes": "feel contrary: aksi / huysuz hissetmek; stubbornly: inatla"
            },
            {
                "id": 58,
                "text": "Mrs. Medlock shrugged her shoulders and left the room, locking the door firmly from the outside.",
                "translation": "Bayan Medlock omuzlarını silkti ve kapıyı dışarıdan sıkıca kilitleyerek odadan ayrıldı.",
                "notes": "shrug shoulders: omuz silkmek; lock firmly: sıkıca kilitlemek"
            },
            {
                "id": 59,
                "text": "Mary crawled into the large four-poster bed and listened to the eerie howling of the moor wind.",
                "translation": "Mary dört direkli koca karyolaya tırmandı ve bozkır rüzgarının tekinsiz uğultusunu dinledi.",
                "notes": "four-poster bed: dört direkli karyola; eerie howling: tekinsiz uğultu"
            },
            {
                "id": 60,
                "text": "She felt completely alone in the world, unloved, unwanted, and surrounded by cold stone.",
                "translation": "Dünyada yapayalnız, sevilmeyen, istenmeyen ve soğuk taşlarla çevrili hissetti.",
                "notes": "unloved: sevilmeyen; unwanted: istenmeyen; surrounded: çevrili"
            }
        ]
    },

    # Page 4 (Sentences 61-80)
    {
        "page_no": 4,
        "title": "Martha and the Skipping-rope",
        "tr_title": "Martha ve İp Atlama Neşesi",
        "vocab_focus": [
            ("housemaid", "oda hizmetçisi kız"),
            ("dialect", "Yorkshire ağzı, lehçe"),
            ("cottage", "köy evi, kulübe"),
            ("heather", "süpürgeotu"),
            ("skipping-rope", "atlama ipi"),
            ("bramble", "böğürtlen çalısı"),
            ("curiosity", "merak"),
            ("gardener", "bahçıvan")
        ],
        "sentences": [
            {
                "id": 61,
                "text": "Mary opened her eyes next morning to see a young housemaid kneeling on the hearth cleaning the fireplace.",
                "translation": "Ertesi sabah Mary gözlerini açtığında, şöminenin önünde diz çökmüş ocağı temizleyen genç bir hizmetçi kız gördü.",
                "notes": "housemaid: oda hizmetçisi; kneeling: diz çökmüş"
            },
            {
                "id": 62,
                "text": "Her name was Martha, an honest Yorkshire country girl with a round face and a broad, friendly dialect.",
                "translation": "Adı Martha'ydı; yuvarlak yüzü ve geniş, cana yakın bir Yorkshire şivesi olan dürüst bir köylü kızıydı.",
                "notes": "broad dialect: geniş şive / ağız; country girl: köylü kızı"
            },
            {
                "id": 63,
                "text": "\"Eh, you're awake!\" Martha exclaimed cheerfully, \"I've brought your breakfast of porridge and hot toast.\"",
                "translation": "\"Aa, uyandın demek!\" diye haykırdı Martha neşeyle, \"Sana sıcak lapa ve kızarmış ekmekten kahvaltını getirdim.\"",
                "notes": "awake: uyanık; porridge: yulaf lapası; toast: kızarmış ekmek"
            },
            {
                "id": 64,
                "text": "Mary sat up in bed and waited for the servant to dress her, as her Indian Ayah had always done.",
                "translation": "Mary yatağında doğruldu ve Hintli dadısının daima yaptığı gibi hizmetçinin kendisini giydirmesini bekledi.",
                "notes": "sat up: doğruldu; wait to dress: giydirilmek için beklemek"
            },
            {
                "id": 65,
                "text": "\"Why don't you put on your clothes?\" Martha asked in surprise. \"Are you sick?\"",
                "translation": "\"Neden elbiselerini giymiyorsun?\" diye sordu Martha şaşkınlıkla. \"Hasta mısın yoksa?\"",
                "notes": "put on clothes: kıyafetleri giymek; in surprise: şaşkınlıkla"
            },
            {
                "id": 66,
                "text": "\"My Ayah always dressed me in India!\" Mary answered insolently, stamping her foot on the floor.",
                "translation": "\"Hindistan'da beni daima dadım giydirirdi!\" diye cevap verdi Mary küstahça, ayağını yere vurarak.",
                "notes": "insolently: küstahça; stamp foot: ayağını yere vurmak"
            },
            {
                "id": 67,
                "text": "\"Eh, well! You'll learn to dress yourself here,\" Martha laughed good-naturedly.",
                "translation": "\"Hadi oradan! Burada kendi kendine giyinmeyi öğreneceksin,\" diye iyi niyetle güldü Martha.",
                "notes": "good-naturedly: babacan ve tatlı bir tavırla"
            },
            {
                "id": 68,
                "text": "\"My mother has twelve children in our little cottage, and nobody waits on anybody there!\"",
                "translation": "\"Bizim küçük kulübemizde annemin tam on iki çocuğu var ve orada hiç kimse kimseye hizmetçilik etmez!\"",
                "notes": "cottage: kulübe, köy evi; wait on: birine hizmet etmek"
            },
            {
                "id": 69,
                "text": "Mary felt ashamed and angry, but she managed to button her own shoes and put on her coat.",
                "translation": "Mary utandı ve öfkelendi fakat ayakkabılarını kendi iliklemeyi ve paltosunu giymeyi başardı.",
                "notes": "felt ashamed: utandı; button shoes: ayakkabıları iliklemek"
            },
            {
                "id": 70,
                "text": "Martha told her about her brother Dickon, who was twelve years old and had a pony of his own.",
                "translation": "Martha ona on iki yaşındaki ve kendine ait bir midillisi olan erkek kardeşi Dickon'dan bahsetti.",
                "notes": "pony of his own: kendine ait midilli"
            },
            {
                "id": 71,
                "text": "\"He plays on his wooden pipe, and wild moor animals come running out of bushes to eat from his hand!\"",
                "translation": "\"Tahta kavalını çalar ve vahşi bozkır hayvanları elinden yemek için çalılıklardan koşup gelir!\"",
                "notes": "wooden pipe: tahta flüt / kaval; wild animals: vahşi hayvanlar"
            },
            {
                "id": 72,
                "text": "\"He knows every bird's nest and every fox hole on the whole Yorkshire moor.\"",
                "translation": "\"Bütün Yorkshire bozkırındaki her kuş yuvasını ve her tilki inini avucunun içi gibi bilir.\"",
                "notes": "bird's nest: kuş yuvası; fox hole: tilki ini"
            },
            {
                "id": 73,
                "text": "Mary had never heard of such a boy and felt eager to know more about him.",
                "translation": "Mary böyle bir çocuğu daha önce hiç duymamıştı ve onun hakkında daha çok şey öğrenmek için sabırsızlandı.",
                "notes": "eager to know: öğrenmeye hevesli"
            },
            {
                "id": 74,
                "text": "\"Now wrap yourself up warm and run outside to play,\" Martha instructed kindly.",
                "translation": "\"Şimdi sıkıca sarın ve oynamak için dışarı koş,\" diye tatlı dille tembihledi Martha.",
                "notes": "wrap up warm: sıkıca giyinmek / sarınmak; kindly: tatlı dille"
            },
            {
                "id": 75,
                "text": "\"The fresh moor wind will put some color into your pale yellow cheeks!\"",
                "translation": "\"Bozkırın taze rüzgarı o solgun sarı yanaklarına biraz renk getirecektir!\"",
                "notes": "put color: renk getirmek; pale cheeks: solgun yanaklar"
            },
            {
                "id": 76,
                "text": "Mary went downstairs and walked out into the vast gardens surrounding the old manor.",
                "translation": "Mary alt kata indi ve eski konağı çevreleyen devasa bahçelere doğru yürüdü.",
                "notes": "vast gardens: uçsuz bucaksız bahçeler; surrounding: çevreleyen"
            },
            {
                "id": 77,
                "text": "There were flower gardens with dead brown beds, vegetable gardens, and ancient fruit orchards.",
                "translation": "Kurumuş kahverengi tarhları olan çiçek bahçeleri, sebze bahçeleri ve asırlık meyve bahçeleri vardı.",
                "notes": "flower beds: çiçek tarhları; fruit orchard: meyve bahçesi"
            },
            {
                "id": 78,
                "text": "Beyond the kitchen gardens, she noticed high brick walls completely covered in thick green ivy.",
                "translation": "Mutfak bahçelerinin ilerisinde, tamamen sık yeşil sarmaşıklarla kaplı yüksek tuğla duvarlar fark etti.",
                "notes": "brick walls: tuğla duvarlar; thick green ivy: sık yeşil sarmaşık"
            },
            {
                "id": 79,
                "text": "She walked along the wall looking for an entrance, but could find no door handle or gate anywhere.",
                "translation": "Bir giriş arayarak duvar boyunca yürüdü fakat hiçbir yerde kapı kolu ya da parmaklık bulamadı.",
                "notes": "door handle: kapı kolu; gate: bahçe kapısı"
            },
            {
                "id": 80,
                "text": "\"This must be the garden that has been locked up for ten years!\" Mary whispered in excitement.",
                "translation": "\"On yıldır kilitli tutulan bahçe burası olmalı!\" diye heyecanla fısıldadı Mary.",
                "notes": "locked up: kilitli; whisper in excitement: heyecanla fısıldamak"
            }
        ]
    },

    # Page 5 (Sentences 81-100)
    {
        "page_no": 5,
        "title": "The Robin Redbreast in the Orchard",
        "tr_title": "Meyve Bahçesindeki Kızılgerdan Kuşu",
        "vocab_focus": [
            ("robin", "kızılgerdan kuşu"),
            ("redbreast", "kızıl göğüslü"),
            ("spade", "bel, bahçıvan küreği"),
            ("crusty", "huysuz, ters"),
            ("orchard", "meyve bahçesi"),
            ("chirp", "cıvıldamak"),
            ("perch", "tünemek, konmak"),
            ("ivy", "sarmaşık")
        ],
        "sentences": [
            {
                "id": 81,
                "text": "Mary found an old gardener with a crusty face digging in a vegetable bed with a spade.",
                "translation": "Mary bir sebze tarhında kürekle toprağı kazan huysuz yüzlü yaşlı bir bahçıvan buldu.",
                "notes": "crusty face: huysuz / çatık yüz; dig with spade: kürekle kazmak"
            },
            {
                "id": 82,
                "text": "His name was Ben Weatherstaff, and he looked as surly and contrary as Mary herself.",
                "translation": "Adı Ben Weatherstaff'tı ve en az Mary'nin kendisi kadar asık suratlı ve aksi görünüyordu.",
                "notes": "surly and contrary: huysuz ve aksi"
            },
            {
                "id": 83,
                "text": "\"What is that walled garden over there?\" Mary asked, pointing over the ivy-covered bricks.",
                "translation": "\"Şuradaki duvarla çevrili bahçe nedir?\" diye sordu Mary, sarmaşık kaplı tuğlaları işaret ederek.",
                "notes": "point over: ...in üzerinden işaret etmek; walled garden: duvarlı bahçe"
            },
            {
                "id": 84,
                "text": "\"It has no door, and nobody can go into it, so none of your business!\" the old man grunted.",
                "translation": "\"Kapısı yok ve kimse içine giremez, o yüzden seni hiç ilgilendirmez!\" diye homurdandı yaşlı adam.",
                "notes": "none of your business: seni ilgilendirmez; grunt: homurdanmak"
            },
            {
                "id": 85,
                "text": "Suddenly, a soft little flight through the air ended with a tiny bird alighting on a bare apple bough.",
                "translation": "Birden havadaki hafif bir kanat çırpışı, çıplak bir elma dalına konan küçücük bir kuşla son buldu.",
                "notes": "alight on: üzerine konmak; apple bough: elma dalı"
            },
            {
                "id": 86,
                "text": "It was a robin redbreast with a bright scarlet waistcoat and bright black eyes like dew.",
                "translation": "Parlak kızıl bir yeleği ve çiy damlaları gibi parlak kara gözleri olan bir kızılgerdandı bu.",
                "notes": "robin redbreast: kızılgerdan; scarlet: parlak kırmızı, al"
            },
            {
                "id": 87,
                "text": "The little bird burst into a sweet, cheerful song, tilting his head sideways at Ben Weatherstaff.",
                "translation": "Minik kuş başını Ben Weatherstaff'a doğru yana eğerek tatlı, neşeli bir şarkı şakımaya başladı.",
                "notes": "tilt head: başını eğmek; burst into song: şarkıya başlamak"
            },
            {
                "id": 88,
                "text": "To Mary's astonishment, the grumpy old gardener's face softened into a warm, gentle smile.",
                "translation": "Mary'nin hayreti karşısında, huysuz yaşlı bahçıvanın yüzü sıcacık, tatlı bir tebessümle yumuşadı.",
                "notes": "grumpy gardener: huysuz bahçıvan; soften into smile: gülümsemeyle yumuşamak"
            },
            {
                "id": 89,
                "text": "\"Well, how art thou, little fellow?\" Ben chirped back, whistling softly to the little creature.",
                "translation": "\"Eee, nasılsın bakalım ufaklık?\" diye karşılık verdi Ben, minik yaratığa usulca ıslık çalarak.",
                "notes": "how art thou: nasılsın (eski Yorkshire lehçesi); whistle softly: usulca ıslık çalmak"
            },
            {
                "id": 90,
                "text": "\"He was a lonely orphan bird when he was small,\" Ben explained to Mary with real tenderness.",
                "translation": "\"Küçükken yapayalnız kalmış bir yetim kuştu bu,\" diye açıkladı Ben Mary'ye gerçek bir şefkatle.",
                "notes": "orphan bird: yetim / öksüz kuş; tenderness: şefkat"
            },
            {
                "id": 91,
                "text": "\"We've been friends ever since; he is the only friend I have in all the world.\"",
                "translation": "\"O günden beri dostuz; bütün dünyada sahip olduğum tek dostum odur.\"",
                "notes": "ever since: o günden beri; only friend: tek dost"
            },
            {
                "id": 92,
                "text": "\"I have no friends at all,\" said Mary, realizing for the first time how lonely she truly was.",
                "translation": "\"Benimse hiç dostum yok,\" dedi Mary, ne kadar yapayalnız olduğunu ilk defa kavrayarak.",
                "notes": "realize: fark etmek, kavramak; lonely: yalnız"
            },
            {
                "id": 93,
                "text": "The robin flew closer, hopping from branch to branch, cocking his head at the little girl.",
                "translation": "Kızılgerdan daldan dala sekerek daha da yakına uçtu, başını eğip küçük kıza merakla baktı.",
                "notes": "cock head: başını yana eğmek; hop: sekmek"
            },
            {
                "id": 94,
                "text": "\"Would you make friends with me?\" Mary whispered, stepping forward with cautious gentleness.",
                "translation": "\"Benimle arkadaş olur musun?\" diye fısıldadı Mary, temkinli bir nezaketle ileri doğru bir adım atarak.",
                "notes": "make friends with: ...ile arkadaş olmak; cautious gentleness: temkinli nezaket"
            },
            {
                "id": 95,
                "text": "She spoke in a tone so soft and pleading that the robin did not take flight.",
                "translation": "Öyle yumuşak ve yalvaran bir ses tonuyla konuştu ki kızılgerdan havalanıp kaçmadı.",
                "notes": "pleading tone: yalvaran ton; take flight: havalanıp uçmak"
            },
            {
                "id": 96,
                "text": "He gave a quick chirp and pecked at an earthworm on the freshly turned earth.",
                "translation": "Hafifçe cıvıldadı ve taze altüst edilmiş topraktaki bir solucanı gagalamaya başladı.",
                "notes": "peck: gagalamak; earthworm: yer solucanı"
            },
            {
                "id": 97,
                "text": "\"You have a way with birds, child,\" Ben Weatherstaff remarked, leaning upon his spade.",
                "translation": "\"Kuşlarla iyi anlaşıyorsun çocuk,\" dedi Ben Weatherstaff küreğine yaslanarak.",
                "notes": "have a way with: diliyle iyi anlaşmak; lean upon: üzerine yaslanmak"
            },
            {
                "id": 98,
                "text": "\"He likes thee, and he's as particular about his friends as a bishop!\"",
                "translation": "\"Senden hoşlandı; oysa dostları konusunda bir piskopos kadar titizdir!\"",
                "notes": "particular about: konusunda çok titiz; bishop: piskopos"
            },
            {
                "id": 99,
                "text": "Mary felt a sudden rush of warm happiness in her chest, unlike anything she had known in India.",
                "translation": "Mary göğsünde, Hindistan'da tanıdığı hiçbir şeye benzemeyen ani bir sıcak mutluluk dalgası hissetti.",
                "notes": "rush of happiness: mutluluk dalgası; unlike anything: hiçbir şeye benzemeyen"
            },
            {
                "id": 100,
                "text": "She had found her very first friend, a tiny bird with bright red feathers.",
                "translation": "Parlak kırmızı tüyleri olan minik bir kuşla ilk arkadaşını bulmuştu.",
                "notes": "red feathers: kırmızı tüyler; first friend: ilk dost"
            }
        ]
    },

    # Page 6 (Sentences 101-120)
    {
        "page_no": 6,
        "title": "The Cry in the Lonely Corridor",
        "tr_title": "Issız Koridordaki Gizemli Ağlama Sesi",
        "vocab_focus": [
            ("tapestry", "duvar halısı"),
            ("creaking", "gıcırdayan"),
            ("weeping", "ağlama, hıçkırık"),
            ("corridor", "koridor"),
            ("curtain", "perde"),
            ("key", "anahtar"),
            ("wind", "rüzgar"),
            ("shut up", "kapatılmış, kilitli")
        ],
        "sentences": [
            {
                "id": 101,
                "text": "A few days later, a heavy downpour of rain kept Mary indoors all morning.",
                "translation": "Birkaç gün sonra şiddetli bir sağanak yağmur Mary'yi bütün sabah boyunca içeride tuttu.",
                "notes": "heavy downpour: şiddetli sağanak; indoors: kapalı alanda"
            },
            {
                "id": 102,
                "text": "Bored and lonely, she decided to explore the dark, mysterious rooms of the hundred-room mansion.",
                "translation": "Sıkılmış ve yalnız bir halde, yüz odalı konağın karanlık ve gizemli odalarını keşfetmeye karar verdi.",
                "notes": "bored and lonely: sıkılmış ve yalnız; explore: keşfetmek"
            },
            {
                "id": 103,
                "text": "She walked quietly down long galleries where old tapestries fluttered in the drafty air.",
                "translation": "Eski duvar halılarının cereyanlı havada dalgalandığı uzun galeriler boyunca sessizce yürüdü.",
                "notes": "tapestry: duvar halısı; drafty air: cereyanlı hava"
            },
            {
                "id": 104,
                "text": "She turned handles and peeped into grand ballrooms, silent libraries, and dusty bedrooms with velvet canopies.",
                "translation": "Kapı kollarını çevirdi ve görkemli balo salonlarına, sessiz kütüphanelere ve kadife gölgelikli tozlu yatak odalarına göz attı.",
                "notes": "turn handle: kapı kolunu çevirmek; peep into: içine göz atmak"
            },
            {
                "id": 105,
                "text": "In one room, she found a cabinet filled with hundred miniature painted elephants carved of ivory.",
                "translation": "Odalardan birinde, fildişinden oyulmuş yüz minyatür boyalı filin bulunduğu bir vitrin buldu.",
                "notes": "miniature: minyatür; carved of ivory: fildişinden oyulmuş"
            },
            {
                "id": 106,
                "text": "As she stood admiring the toys, a distinct sound broke the oppressive silence of the corridor.",
                "translation": "Oyuncaklara hayranlıkla bakarken, koridorun boğucu sessizliğini belirgin bir ses böldü.",
                "notes": "oppressive silence: boğucu sessizlik; distinct sound: belirgin ses"
            },
            {
                "id": 107,
                "text": "It was not the wind; it was the unmistakable sound of a child crying in distant pain.",
                "translation": "Bu rüzgar değildi; uzakta acı içinde ağlayan bir çocuğun apaçık sesiydi.",
                "notes": "unmistakable: şüphe götürmez, apaçık; distant pain: uzaktaki acı"
            },
            {
                "id": 108,
                "text": "The wailing was faint, fretful, and muffled by heavy closed doors.",
                "translation": "Ağlama sesi zayıftı, sızlanan bir tondaydı ve ağır kapalı kapılar tarafından boğuluyordu.",
                "notes": "fretful: sızlanan, huysuz; muffled: boğuk, bastırılmış"
            },
            {
                "id": 109,
                "text": "Mary followed the sound down a narrow passageway until Mrs. Medlock suddenly appeared with a bunch of keys.",
                "translation": "Mary elinde bir deste anahtarla birdenbire Bayan Medlock belirine kadar dar bir geçit boyunca sesi takip etti.",
                "notes": "narrow passageway: dar geçit; bunch of keys: anahtar destesi"
            },
            {
                "id": 110,
                "text": "\"What are you doing here?\" the housekeeper demanded in furious anger, grasping Mary's arm.",
                "translation": "\"Senin burada ne işin var?\" diye sordu kahya kadın büyük bir öfkeyle Mary'nin kolunu sıkarak.",
                "notes": "grasp arm: kolunu kavramak / sıkmak; furious anger: hiddetli öfke"
            },
            {
                "id": 111,
                "text": "\"I heard someone crying,\" Mary replied stoutly, \"a child crying in one of these rooms!\"",
                "translation": "\"Ağlayan birini duydum,\" diye kararlılıkla yanıtladı Mary, \"bu odalardan birinde bir çocuk ağlıyor!\"",
                "notes": "reply stoutly: cesurca / kararlılıkla yanıtlamak"
            },
            {
                "id": 112,
                "text": "\"You heard nothing of the sort!\" Mrs. Medlock lied angrily. \"It was the wind blowing down the chimney!\"",
                "translation": "\"Sen öyle bir şey duymadın!\" diye öfkeyle yalan söyledi Bayan Medlock. \"Bacadan aşağı esen rüzgardı o!\"",
                "notes": "nothing of the sort: asla öyle bir şey yok; blow down chimney: bacadan esmek"
            },
            {
                "id": 113,
                "text": "\"Now come back to your nursery, or I'll box your ears and lock you up!\"",
                "translation": "\"Şimdi doğru çocuk odana dön, yoksa kulaklarını çeker ve seni içeri kilitlerim!\"",
                "notes": "box ears: kulağını çekmek; lock up: kilitlemek"
            },
            {
                "id": 114,
                "text": "Mary was dragged back to her room, but she was entirely unconvinced by the housekeeper's lie.",
                "translation": "Mary odasına geri sürüklendi fakat kahyanın yalanına zerre kadar ikna olmadı.",
                "notes": "unconvinced: ikna olmamış; drag back: geri sürüklemek"
            },
            {
                "id": 115,
                "text": "She knew beyond a shadow of doubt that a living child was weeping somewhere in that dark house.",
                "translation": "O karanlık evde bir yerlerde yaşayan bir çocuğun ağladığından zerre kadar şüphe duymuyordu.",
                "notes": "shadow of doubt: şüphe kırıntısı; weeping: ağlayan"
            },
            {
                "id": 116,
                "text": "When Martha returned with dinner, Mary questioned her about the mysterious cries.",
                "translation": "Martha akşam yemeğiyle döndüğünde, Mary ona bu gizemli ağlama seslerini sordu.",
                "notes": "question: sorgulamak, soru sormak; mysterious cries: gizemli çığlıklar"
            },
            {
                "id": 117,
                "text": "Martha turned pale and looked terribly flustered, denying that anyone else lived in the wing.",
                "translation": "Martha'nın beti benzi attı ve son derece telaşlanarak o kanatta başka birinin yaşadığını inkar etti.",
                "notes": "turn pale: beti benzi atmak; flustered: telaşlanmış, kafası karışmış"
            },
            {
                "id": 118,
                "text": "\"It's just the scullery maid having toothache,\" Martha stammered, looking away.",
                "translation": "\"Bulaşıkçı kızın dişi ağrıyordu sadece,\" diye kekeledi Martha, gözlerini kaçırarak.",
                "notes": "scullery maid: bulaşıkçı kız; stammer: kekelemek"
            },
            {
                "id": 119,
                "text": "Mary saw that Martha had been ordered never to speak of the secret inhabitant.",
                "translation": "Mary, gizli sakin hakkında asla konuşmamasının Martha'ya sıkı sıkıya tembihlendiğini anladı.",
                "notes": "secret inhabitant: gizli sakin / konuk; be ordered: emredilmiş olmak"
            },
            {
                "id": 120,
                "text": "The great stone manor was filled with dark, forbidden secrets that Mary was determined to uncover.",
                "translation": "Büyük taş konak, Mary'nin gün yüzüne çıkarmaya kararlı olduğu karanlık ve yasak sırlarla doluydu.",
                "notes": "forbidden secrets: yasak sırlar; determined to uncover: ortaya çıkarmaya kararlı"
            }
        ]
    },

    # Page 7 (Sentences 121-140)
    {
        "page_no": 7,
        "title": "The Key Buried in the Earth",
        "tr_title": "Toprağa Gömülü Paslı Anahtar",
        "vocab_focus": [
            ("gust", "kuvvetli rüzgar esintisi"),
            ("ivy", "sarmaşık"),
            ("rusty", "paslı"),
            ("buried", "gömülü, toprağın altında"),
            ("unlock", "kilidini açmak"),
            ("robin", "kızılgerdan"),
            ("soil", "toprak"),
            ("springtime", "ilkbahar mevsimi")
        ],
        "sentences": [
            {
                "id": 121,
                "text": "The next day, the rain ceased, and the grey sky broke into brilliant patches of blue.",
                "translation": "Ertesi gün yağmur dindi ve gri gökyüzü parlak mavi parçalara ayrıldı.",
                "notes": "rain ceased: yağmur dindi; brilliant patches: parlak parçalar"
            },
            {
                "id": 122,
                "text": "Mary took her skipping-rope which Martha's kind mother had bought for her at the village market.",
                "translation": "Mary, Martha'nın iyi kalpli annesinin köy pazarından kendisi için satın aldığı atlama ipini eline aldı.",
                "notes": "skipping-rope: atlama ipi; village market: köy pazarı"
            },
            {
                "id": 123,
                "text": "She skipped around the gardens, counting her jumps until her cheeks turned rosy and warm.",
                "translation": "Yanakları al al ve sıcacık olana kadar zıplayışlarını sayarak bahçelerin etrafında ip atladı.",
                "notes": "rosy and warm: al al ve sıcacık; count jumps: zıplamaları saymak"
            },
            {
                "id": 124,
                "text": "She reached the long ivy-covered wall bordering the locked garden.",
                "translation": "Kilitli bahçeyi çevreleyen sarmaşık kaplı uzun duvara ulaştı.",
                "notes": "ivy-covered wall: sarmaşıklı duvar; border: çevrelemek, sınır olmak"
            },
            {
                "id": 125,
                "text": "The robin was sitting on top of the wall, watching her with his bright, intelligent eyes.",
                "translation": "Kızılgerdan duvarın tepesinde oturuyor, parlak ve zeki gözleriyle onu izliyordu.",
                "notes": "intelligent eyes: zeki gözler; top of the wall: duvarın tepesi"
            },
            {
                "id": 126,
                "text": "He chirped merrily, then flew down onto a flowerbed where a dog had recently dug a hole.",
                "translation": "Neşeyle cıvıldadı, ardından bir köpeğin yakın zamanda çukur kazdığı bir çiçek tarhına doğru aşağı kondu.",
                "notes": "chirp merrily: neşeyle cıvıldamak; flowerbed: çiçek tarhı"
            },
            {
                "id": 127,
                "text": "Mary skipped over to him, whispering friendly words so as not to startle him.",
                "translation": "Mary onu ürkütmemek için dostça sözler fısıldayarak ip atlayarak yanına gitti.",
                "notes": "startle: ürkütmek, korkutmak; friendly words: dostça sözler"
            },
            {
                "id": 128,
                "text": "As the bird hopped on the freshly turned earth, something metallic caught Mary's eye in the soil.",
                "translation": "Kuş taze altüst edilmiş toprakta sekerken toprağın içindeki madeni bir nesne Mary'nin gözüne çarptı.",
                "notes": "metallic: madeni, metalik; catch eye: gözüne çarpmak"
            },
            {
                "id": 129,
                "text": "It looked like a ring of rusty iron or brass half-buried in the damp ground.",
                "translation": "Nemli toprağa yarı gömülmüş, paslı bir demir ya da pirinç halkayı andırıyordu.",
                "notes": "rusty iron: paslı demir; damp ground: nemli toprak"
            },
            {
                "id": 130,
                "text": "She reached down and pulled it up: it was an old key, heavy and covered with rust.",
                "translation": "Aşağı uzandı ve onu çekip çıkardı: bu eski, ağır ve pasla kaplı bir anahtardı.",
                "notes": "reach down: aşağı uzanmak; covered with rust: pasla kaplı"
            },
            {
                "id": 131,
                "text": "\"Perhaps it has been buried for ten years!\" Mary whispered breathlessly, holding it tight.",
                "translation": "\"Belki de on yıldır gömülüydü bu!\" diye soluk soluğa fısıldadı Mary, onu sıkıca tutarak.",
                "notes": "breathlessly: nefes nefese; hold tight: sıkı tutmak"
            },
            {
                "id": 132,
                "text": "\"Perhaps it is the key to the secret garden!\"",
                "translation": "\"Belki de gizli bahçenin anahtarıdır bu!\"",
                "notes": "key to secret garden: gizli bahçenin anahtarı"
            },
            {
                "id": 133,
                "text": "She slipped the rusty treasure deep into her coat pocket, her heart pounding with excitement.",
                "translation": "Yüreği heyecandan küt küt atarak bu paslı hazineyi paltosunun cebinin derinliklerine soktu.",
                "notes": "heart pounding: yüreği çarparak; rusty treasure: paslı hazine"
            },
            {
                "id": 134,
                "text": "The next morning, the wind was blowing fiercely across the ivy wall.",
                "translation": "Ertesi sabah rüzgar sarmaşıklı duvar boyunca şiddetle esiyordu.",
                "notes": "blow fiercely: şiddetle esmek"
            },
            {
                "id": 135,
                "text": "The robin was perched on a swinging spray of ivy, singing his joyful song.",
                "translation": "Kızılgerdan sallanan bir sarmaşık dalına tünemiş, neşeli şarkısını şakıyordu.",
                "notes": "perch: tünemek; swinging spray: sallanan dal"
            },
            {
                "id": 136,
                "text": "A sudden gust of wind blew aside the heavy trailing curtain of green leaves.",
                "translation": "Ani bir rüzgar esintisi, sarkan yeşil yaprakların ağır perdesini bir kenara savurdu.",
                "notes": "sudden gust: ani rüzgar esintisi; trailing curtain: sarkan perde"
            },
            {
                "id": 137,
                "text": "Mary's heart gave a wild leap: under the parted ivy, she saw the round knob of a locked wooden door!",
                "translation": "Mary'nin kalbi deli gibi çarptı: aralanan sarmaşığın altında kilitli bir ahşap kapının yuvarlak kolunu gördü!",
                "notes": "wild leap: yerinden fırlamak / hoplamak; round knob: yuvarlak tokmak / kol"
            },
            {
                "id": 138,
                "text": "She pushed her hand through the leaves and felt an iron keyhole beneath the lock plate.",
                "translation": "Elini yaprakların arasından uzattı ve kilit plakasının altında demir bir anahtar deliği hissetti.",
                "notes": "keyhole: anahtar deliği; lock plate: kilit aynası"
            },
            {
                "id": 139,
                "text": "With trembling hands, she took the rusty key from her pocket and inserted it into the hole.",
                "translation": "Titreyen elleriyle paslı anahtarı cebinden çıkardı ve deliğin içine soktu.",
                "notes": "trembling hands: titreyen eller; insert into hole: deliğe sokmak"
            },
            {
                "id": 140,
                "text": "It fitted! She turned it with both hands: with a stiff metallic click, the door swung slowly open.",
                "translation": "Tam uydu! İki eliyle birden çevirdi: sert bir madeni tıkırtıyla kapı yavaşça ardına kadar açıldı.",
                "notes": "metallic click: madeni tıkırtı; swung slowly open: yavaşça ardına kadar açıldı"
            }
        ]
    },

    # Page 8 (Sentences 141-160)
    {
        "page_no": 8,
        "title": "Inside the Secret Walled Garden",
        "tr_title": "Taş Duvarlı Gizli Bahçeye Giriş",
        "vocab_focus": [
            ("fairy-land", "periler diyarı"),
            ("rose-trees", "gül ağaçları"),
            ("overgrown", "sarılmış, vahşileşmiş"),
            ("delicate", "narin, ince"),
            ("shoots", "filizler, taze sürgünler"),
            ("alive", "canlı, diri"),
            ("secret", "gizli, sır"),
            ("enchanted", "büyülü, efsunlu")
        ],
        "sentences": [
            {
                "id": 141,
                "text": "Mary slipped through the doorway and closed the heavy oak door behind her.",
                "translation": "Mary kapı aralığından içeri süzüldü ve arkasından ağır meşe kapıyı kapattı.",
                "notes": "slip through: arasından süzülmek; oak door: meşe kapı"
            },
            {
                "id": 142,
                "text": "She stood looking around with breathless wonder: it was the sweetest, most mysterious-looking place anyone could imagine.",
                "translation": "Nefesini tutmuş bir hayranlıkla etrafına bakakaldı: burası insanın hayal edebileceği en tatlı, en gizemli görünümlü yerdi.",
                "notes": "breathless wonder: nefes kesen hayranlık; mysterious-looking: gizemli görünümlü"
            },
            {
                "id": 143,
                "text": "The high stone walls were covered with thick, leafless climbing rose vines.",
                "translation": "Yüksek taş duvarlar, yapraksız kalın sarmaşık gül dallarıyla boydan boya kaplıydı.",
                "notes": "rose vines: gül sarmaşıkları; leafless: yapraksız"
            },
            {
                "id": 144,
                "text": "Their stems were so tangled that they formed lovely grey canopies draping from tree to tree.",
                "translation": "Gövde dalları birbirine öyle dolanmıştı ki ağaçtan ağaca sarkan hoş gri gölgelikler oluşturuyordu.",
                "notes": "tangled: birbirine dolanmış; canopies: gölgelikler"
            },
            {
                "id": 145,
                "text": "Old rose-trees grew wild in the brown grass, spreading out their delicate branches like living lace.",
                "translation": "Yaşlı gül ağaçları kahverengi çimenler arasında vahşice büyümüş, narin dallarını canlı bir dantel gibi yaymıştı.",
                "notes": "rose-trees: gül ağaçları; living lace: canlı dantel"
            },
            {
                "id": 146,
                "text": "\"Is it all dead?\" Mary wondered in a quiet whisper, touching a grey stalk.",
                "translation": "\"Hepsi ölmüş mü acaba?\" diye usulca fısıldayarak merak etti Mary, gri bir dala dokunarak.",
                "notes": "quiet whisper: alçak sesle fısıltı; stalk: dal, gövde"
            },
            {
                "id": 147,
                "text": "The bark was dry, but underneath the wood was green, tender, and moist with sap.",
                "translation": "Ağaç kabuğu kuruydu fakat altındaki odun kısmı yeşildi, körpeydi ve bitki özsuyuyla nemliydi.",
                "notes": "tender: körpe; moist with sap: bitki özsuyuyla nemli"
            },
            {
                "id": 148,
                "text": "\"It's not dead at all!\" she cried with joy. \"The roses are alive, only fast asleep!\"",
                "translation": "\"Hiç de ölmemişler!\" diye sevinçle haykırdı. \"Güller yaşıyor, sadece derin bir uykudalar!\"",
                "notes": "fast asleep: derin uykuda; alive: canlı, diri"
            },
            {
                "id": 149,
                "text": "She looked down at the earth and noticed tiny sharp green points sticking up through the dead grass.",
                "translation": "Toprağa doğru baktı ve ölü çimenlerin arasından sivrilen küçücük sivri yeşil uçlar fark etti.",
                "notes": "sticking up: yukarı doğru çıkan; green points: yeşil uçlar / filizler"
            },
            {
                "id": 150,
                "text": "They were snowdrops, crocuses, and daffodils waking up after a long winter sleep.",
                "translation": "Bunlar uzun bir kış uykusunun ardından uyanmakta olan kardelenler, çiğdemler ve nergislerdi.",
                "notes": "snowdrops: kardelenler; crocuses: çiğdemler; daffodils: nergisler"
            },
            {
                "id": 151,
                "text": "The weeds were choking them, so Mary knelt down with a sharp stick and began weeding the soil.",
                "translation": "Yabani otlar onları boğuyordu, bu yüzden Mary sivri bir çubukla diz çöktü ve topraktaki otları ayıklamaya başladı.",
                "notes": "weeding soil: toprağı yabani otlardan ayıklamak; choke: boğmak"
            },
            {
                "id": 152,
                "text": "She cleared a circle of breathing room around each tiny green sprout.",
                "translation": "Her minik yeşil filizin etrafında nefes alabileceği dairesel bir boşluk açtı.",
                "notes": "breathing room: nefes alma alanı; green sprout: yeşil filiz"
            },
            {
                "id": 153,
                "text": "\"Now you can breathe and grow in the sunshine,\" she spoke lovingly to the flowers.",
                "translation": "\"Artık nefes alabilir ve gün ışığında büyüyebilirsiniz,\" diye sevgiyle konuştu çiçeklerle.",
                "notes": "spoke lovingly: sevgiyle konuştu; grow in sunshine: güneş ışığında büyümek"
            },
            {
                "id": 154,
                "text": "She worked diligently for two happy hours until her hands were covered in dark, fragrant earth.",
                "translation": "Elleri koyu renkli, mis kokulu toprakla kaplanana kadar iki mutlu saat boyunca canla başla çalıştı.",
                "notes": "worked diligently: gayretle çalıştı; fragrant earth: mis kokulu toprak"
            },
            {
                "id": 155,
                "text": "The robin perched on an old apple tree near her, singing as if congratulating her on her work.",
                "translation": "Kızılgerdan yakınındaki yaşlı bir elma ağacına tünemiş, sanki yaptığı işten ötürü onu tebrik edercesine şakıyordu.",
                "notes": "congratulate: tebrik etmek; perched: tünemiş"
            },
            {
                "id": 156,
                "text": "\"This is my own secret world,\" Mary smiled, feeling happier than she had ever been in India.",
                "translation": "\"Burası benim kendi gizli dünyam,\" diye gülümsedi Mary, Hindistan'da olduğu her günden çok daha mutlu hissederek.",
                "notes": "secret world: gizli dünya; feel happier: daha mutlu hissetmek"
            },
            {
                "id": 157,
                "text": "When she returned to the nursery for lunch, her appetite was so hearty that she ate everything on her plate.",
                "translation": "Öğle yemeği için çocuk odasına döndüğünde iştahı öyle açılmıştı ki tabağındaki her şeyi silip süpürdü.",
                "notes": "hearty appetite: kurt gibi iştah; on plate: tabakta"
            },
            {
                "id": 158,
                "text": "\"Well, I never!\" cried Martha, \"The fresh air is making a healthy girl out of you already!\"",
                "translation": "\"Yok artık, gözlerime inanamıyorum!\" diye haykırdı Martha, \"Temiz hava şimdiden seni sapasağlam bir kıza dönüştürüyor!\"",
                "notes": "healthy girl: sağlıklı kız; fresh air: temiz hava"
            },
            {
                "id": 159,
                "text": "Mary asked Martha if she could have a small spade to dig with and some flower seeds to plant.",
                "translation": "Mary Martha'ya, toprağı kazmak için küçük bir bahçıvan küreği ve dikmek için birkaç çiçek tohumu alıp alamayacağını sordu.",
                "notes": "flower seeds: çiçek tohumları; small spade: küçük bahçıvan küreği"
            },
            {
                "id": 160,
                "text": "Martha promised to ask her brother Dickon to buy seeds and a spade at the market and bring them to the manor.",
                "translation": "Martha, kardeşi Dickon'dan pazardan tohum ve kürek alıp malikaneye getirmesini rica edeceğine söz verdi.",
                "notes": "promise: söz vermek; bring to manor: malikaneye getirmek"
            }
        ]
    },

    # Page 9 (Sentences 161-180)
    {
        "page_no": 9,
        "title": "Dickon and the Wild Creatures",
        "tr_title": "Dickon ve Bozkırın Vahşi Dostları",
        "vocab_focus": [
            ("charming", "büyüleyici, cana yakın"),
            ("crow", "karga"),
            ("squirrel", "sincap"),
            ("lamb", "kuzu"),
            ("spade", "kürek"),
            ("seed-packets", "tohum paketleri"),
            ("delight", "büyük sevinç, haz"),
            ("trust", "güven, inanmak")
        ],
        "sentences": [
            {
                "id": 161,
                "text": "A few days later, Mary was walking through the orchard when she heard a strange piping melody.",
                "translation": "Birkaç gün sonra Mary meyve bahçesinde yürürken tuhaf bir kaval ezgisi duydu.",
                "notes": "piping melody: kaval ezgisi; orchard: meyve bahçesi"
            },
            {
                "id": 162,
                "text": "Sitting beneath a tree with his back against the trunk was a boy of about twelve, playing a rough wooden pipe.",
                "translation": "Sırtı ağaç gövdesine yaslanmış halde oturan on iki yaşlarında bir oğlan, kaba tahta bir kaval çalıyordu.",
                "notes": "rough wooden pipe: kaba tahta kaval; trunk: ağaç gövdesi"
            },
            {
                "id": 163,
                "text": "He had a turned-up nose and red cheeks, and his round blue eyes were as clear as the Yorkshire sky.",
                "translation": "Kalkık bir burnu ve al yanakları vardı; yuvarlak mavi gözleri Yorkshire göğü kadar berraktı.",
                "notes": "turned-up nose: kalkık burun; clear as sky: gök kadar berrak"
            },
            {
                "id": 164,
                "text": "Close beside him sat a tame crow, two wild squirrels were nibbling nuts, and a newborn lamb rested by his knee.",
                "translation": "Hemen yanı başında evcil bir karga oturuyor, iki yaban sincabı fındık kemiriyor ve yeni doğmuş bir kuzu dizinin dibinde dinleniyordu.",
                "notes": "tame crow: evcil karga; newborn lamb: yeni doğmuş kuzu; nibble: kemirmek"
            },
            {
                "id": 165,
                "text": "Mary stopped motionless, terrified of frightening away the magical creatures.",
                "translation": "Mary bu efsunlu yaratıkları ürkütüp kaçırmaktan korkarak kıpırdamadan durdu.",
                "notes": "motionless: hareketsiz; magical creatures: efsunlu yaratıklar"
            },
            {
                "id": 166,
                "text": "The boy stopped playing, smiled warmly, and spoke in his soft moorland voice.",
                "translation": "Çocuk çalmayı bıraktı, içtenlikle gülümsedi ve bozkıra özgü yumuşak sesiyle konuştu.",
                "notes": "moorland voice: bozkır şivesi / sesi; smiled warmly: sıcakça gülümsedi"
            },
            {
                "id": 167,
                "text": "\"I'm Dickon,\" he said, \"and thou must be Miss Mary. I've brought thee the garden tools and flower seeds.\"",
                "translation": "\"Ben Dickon'ım,\" dedi, \"sen de Küçük Hanım Mary olmalısın. Sana bahçe aletlerini ve çiçek tohumlarını getirdim.\"",
                "notes": "garden tools: bahçe aletleri; flower seeds: çiçek tohumları"
            },
            {
                "id": 168,
                "text": "He showed her the packet of seeds: mignonette, larkspur, columbine, and sweet peas.",
                "translation": "Ona tohum paketlerini gösterdi: muhabbet çiçeği, hezaren, hasekiküpesi ve kokulu bezelye.",
                "notes": "sweet peas: kokulu bezelye; larkspur: hezaren çiçeği"
            },
            {
                "id": 169,
                "text": "He explained how to sow them in rich soil and water them until they bloomed into lovely colors.",
                "translation": "Onları verimli toprağa nasıl ekeceğini ve güzel renklerle çiçek açana kadar nasıl sulayacağını anlattı.",
                "notes": "sow seeds: tohum ekmek; bloom into colors: renk renk açmak"
            },
            {
                "id": 170,
                "text": "Mary felt that Dickon was the most wonderful person she had ever encountered.",
                "translation": "Mary, Dickon'ın şimdiye kadar karşılaştığı en harika insan olduğunu düşündü.",
                "notes": "most wonderful person: en harika insan; encounter: karşılaşmak"
            },
            {
                "id": 171,
                "text": "She looked around carefully to see that nobody was watching, then made a momentous decision.",
                "translation": "Kimsenin izlemediğinden emin olmak için etrafına dikkatle baktı, ardından çok önemli bir karar verdi.",
                "notes": "momentous decision: hayati / önemli karar; look around: etrafına bakmak"
            },
            {
                "id": 172,
                "text": "\"Can you keep a secret?\" she whispered, trembling with excitement.",
                "translation": "\"Bir sır saklayabilir misin?\" diye fısıldadı heyecandan titreyerek.",
                "notes": "keep a secret: sır saklamak; tremble with excitement: heyecandan titremek"
            },
            {
                "id": 173,
                "text": "\"If I tell a secret, the birds will fly away and tell the foxes,\" Dickon laughed gently.",
                "translation": "\"Eğer bir sırrı açığa vurursam kuşlar uçar gider tilkilere söyler,\" diye tatlı tatlı güldü Dickon.",
                "notes": "tell a secret: sırrı ifşa etmek; laugh gently: tatlıca gülmek"
            },
            {
                "id": 174,
                "text": "\"Aye, I can keep a secret as safe as a badger in his burrow.\"",
                "translation": "\"Merak etme, bir porsuğun ininde saklandığı kadar güvenle sır saklayabilirim.\"",
                "notes": "badger in burrow: inindeki porsuk; keep safe: güvende tutmak"
            },
            {
                "id": 175,
                "text": "Mary took his hand and led him down the path to the ivy-covered wall.",
                "translation": "Mary onun elinden tuttu ve sarmaşık kaplı duvara giden patika boyunca onu götürdü.",
                "notes": "led down the path: patikadan götürdü"
            },
            {
                "id": 176,
                "text": "She pushed aside the trailing leaves, unlocked the heavy door, and pulled Dickon inside.",
                "translation": "Sarkan yaprakları bir kenara itti, ağır kapının kilidini açtı ve Dickon'ı içeri çekti.",
                "notes": "push aside: bir yana itmek; unlock heavy door: ağır kapıyı açmak"
            },
            {
                "id": 177,
                "text": "Dickon stood staring around in utter enchantment: \"Eh! It's a queer, pretty place! It's like a dream!\"",
                "translation": "Dickon tam bir büyülenme içinde etrafına bakakaldı: \"Vay canına! Ne acayip, ne güzel bir yer burası! Adeta bir rüya gibi!\"",
                "notes": "utter enchantment: tam bir büyülenme; like a dream: rüya gibi"
            },
            {
                "id": 178,
                "text": "He inspected the rose branches with an expert eye, touching the moist green stems with tender care.",
                "translation": "Nemli yeşil gövdelere şefkatle dokunarak gül dallarını uzman bir gözle inceledi.",
                "notes": "expert eye: uzman göz; tender care: şefkatli özen"
            },
            {
                "id": 179,
                "text": "\"There's plenty of green wood here,\" he said with joy. \"The roses will bloom by thousands come summertime!\"",
                "translation": "\"Burada bolca canlı yeşil dal var,\" dedi sevinçle. \"Yaz geldiğinde güller binlercesiyle açacak!\"",
                "notes": "plenty of green wood: bolca canlı dal; bloom by thousands: binlercesiyle açmak"
            },
            {
                "id": 180,
                "text": "They worked together all afternoon, weeding, pruning, and planting seeds in the awakening earth.",
                "translation": "Bütün öğleden sonra birlikte çalıştılar; uyanan toprakta yabani otları ayıkladılar, dalları budadılar ve tohumlar ektiler.",
                "notes": "pruning: budama; awakening earth: uyanan toprak"
            }
        ]
    },

    # Page 10 (Sentences 181-200)
    {
        "page_no": 10,
        "title": "The Discovery of Colin in the Bedchamber",
        "tr_title": "Yatak Odasındaki Hasta Colin'in Keşfi",
        "vocab_focus": [
            ("canopy", "gölgelik, cibinlik"),
            ("invalid", "yatalak hasta"),
            ("hysterical", "histerik, kriz geçiren"),
            ("crooked", "eğri, kambur"),
            ("bedridden", "yatağa bağımlı"),
            ("cousin", "kuzen"),
            ("tyrant", "zorba, tiran"),
            ("discovery", "keşif")
        ],
        "sentences": [
            {
                "id": 181,
                "text": "That very night, a fierce tempest raged across the moor, rattling every casement in the manor.",
                "translation": "Tam o gece bozkırda vahşi bir fırtına koptu, malikanedeki bütün pencere kanatlarını sarstı.",
                "notes": "fierce tempest: şiddetli fırtına; casement: pencere kanadı"
            },
            {
                "id": 182,
                "text": "Mary lay awake listening to the storm, when she clearly heard the crying child once more.",
                "translation": "Mary fırtınayı dinleyerek uyanık yatıyordu, derken ağlayan çocuğun sesini bir kez daha açıkça duydu.",
                "notes": "lay awake: uyanık yatmak; once more: bir kez daha"
            },
            {
                "id": 183,
                "text": "Determined to find the truth, she lit a candle and walked softly out into the dark hallway.",
                "translation": "Gerçeği bulmaya kararlı bir şekilde bir mum yaktı ve sessizce karanlık koridora çıktı.",
                "notes": "determined to find truth: gerçeği bulmaya kararlı; dark hallway: karanlık koridor"
            },
            {
                "id": 184,
                "text": "She followed the sobbing voice past tapestry-hung corridors until she reached a heavy wooden door.",
                "translation": "Hıçkırık sesini duvar halılarıyla kaplı koridorlar boyunca takip etti, ta ki ağır ahşap bir kapıya ulaşana dek.",
                "notes": "sobbing voice: hıçkırık sesi; tapestry-hung: halı kaplı"
            },
            {
                "id": 185,
                "text": "She turned the knob and pushed the door open: a fire burned in the grate of a grand bedchamber.",
                "translation": "Kapı kolunu çevirdi ve kapıyı iterek açtı: görkemli bir yatak odasının şöminesinde bir ateş yanıyordu.",
                "notes": "grand bedchamber: görkemli yatak odası; push door open: kapıyı itip açmak"
            },
            {
                "id": 186,
                "text": "Upon a carved four-poster bed draped in rich velvet lay a boy with a pale, sickly face.",
                "translation": "Ağır kadifeyle kaplı oymalı dört direkli bir karyolada solgun, hastalıklı yüzlü bir oğlan çocuğu yatıyordu.",
                "notes": "four-poster bed: dört direkli karyola; sickly face: hastalıklı yüz"
            },
            {
                "id": 187,
                "text": "He had enormous dark eyes, fine grey-white skin, and tangled black hair.",
                "translation": "Kocaman koyu renk gözleri, ince gri-beyaz bir teni ve birbirine dolanmış siyah saçları vardı.",
                "notes": "enormous dark eyes: kocaman kara gözler; tangled hair: dağınık saç"
            },
            {
                "id": 188,
                "text": "He stopped crying and stared at Mary in terror: \"Who are you? Are you a ghost?\"",
                "translation": "Ağlamasını kesti ve dehşet içinde Mary'ye baka kaldı: \"Kimsin sen? Hayalet misin yoksa?\"",
                "notes": "stared in terror: dehşetle baktı; ghost: hayalet"
            },
            {
                "id": 189,
                "text": "\"No, I am Mary Lennox,\" she replied calmly, \"Mr. Archibald Craven is my uncle.\"",
                "translation": "\"Hayır, ben Mary Lennox'ım,\" diye sakince cevap verdi, \"Bay Archibald Craven benim amcam.\"",
                "notes": "reply calmly: sakince cevap vermek"
            },
            {
                "id": 190,
                "text": "\"He is my father!\" the boy gasped. \"I am Colin Craven, his son!\"",
                "translation": "\"O benim babam!\" diye nefesi kesilerek haykırdı oğlan. \"Ben Colin Craven'ım, onun oğluyum!\"",
                "notes": "gasp: nefesi kesilmek; his son: onun oğlu"
            },
            {
                "id": 191,
                "text": "Mary was astounded: neither Mrs. Medlock nor Martha had ever breathed a single word about a son.",
                "translation": "Mary donakaldı: ne Bayan Medlock ne de Martha bir oğul olduğuna dair tek bir kelime bile fısıldamamıştı.",
                "notes": "astounded: afallamış, donakalmış; breathe a word: tek kelime etmek"
            },
            {
                "id": 192,
                "text": "\"Why does nobody speak of you?\" Mary asked, walking to his bedside.",
                "translation": "\"Neden hiç kimse senden bahsetmiyor?\" diye sordu Mary yatağının başucuna yürüyerek.",
                "notes": "walk to bedside: yatak ucuna yürümek; speak of: ...den bahsetmek"
            },
            {
                "id": 193,
                "text": "\"Because my father hates the sight of me,\" Colin sobbed bitterly.",
                "translation": "\"Çünkü babam beni görmekten nefret ediyor,\" diye acı acı hıçkırdı Colin.",
                "notes": "hate sight of: görmekten nefret etmek; sob bitterly: acı acı ağlamak"
            },
            {
                "id": 194,
                "text": "\"My mother died when I was born, and everybody thinks I will grow up a hunchback and die young.\"",
                "translation": "\"Annem ben doğduğumda öldü ve herkes benim kambur büyüyeceğimi ve genç yaşta öleceğimi düşünüyor.\"",
                "notes": "grow up a hunchback: kambur büyümek; die young: genç yaşta ölmek"
            },
            {
                "id": 195,
                "text": "\"They keep me shut up here so that nobody will see my crooked back.\"",
                "translation": "\"Eğri sırtımı kimse görmesin diye beni buraya kilitli tutuyorlar.\"",
                "notes": "crooked back: eğri sırt; shut up: kapatılmış"
            },
            {
                "id": 196,
                "text": "Mary looked at his straight spine and touched his back gently: \"You are not crooked at all!\"",
                "translation": "Mary onun düz omurgasına baktı ve sırtına usulca dokundu: \"Senin sırtın hiç de eğri değil ki!\"",
                "notes": "straight spine: düz omurga; touch gently: usulca dokunmak"
            },
            {
                "id": 197,
                "text": "\"You are just hysterical and weak from lying in bed all day with medicine bottles!\"",
                "translation": "\"Bütün gün ilaç şişeleriyle yatakta yatmaktan ötürü yalnızca histerikleşmiş ve zayıf düşmüşsün!\"",
                "notes": "medicine bottles: ilaç şişeleri; hysterical and weak: histerik ve zayıf"
            },
            {
                "id": 198,
                "text": "Colin was shocked by her blunt honesty, having been obeyed and pampered by terrified servants all his life.",
                "translation": "Colin onun bu dobra dürüstlüğü karşısında şaşkına döndü; çünkü bütün hayatı boyunca korku içindeki hizmetkarlar ona hep boyun eğmiş ve şımartmıştı.",
                "notes": "blunt honesty: dobra dürüstlük; pampered: şımartılmış"
            },
            {
                "id": 199,
                "text": "Instead of growing angry, he found her blunt words fascinating and asked her to stay and talk.",
                "translation": "Öfkelenmek yerine kızın dobra sözlerini büyüleyici buldu ve yanında kalıp konuşmasını rica etti.",
                "notes": "fascinating: büyüleyici; stay and talk: kalıp konuşmak"
            },
            {
                "id": 200,
                "text": "Mary told him about India, the moor, the robin, and the secret walled garden, soothing him to peaceful sleep.",
                "translation": "Mary ona Hindistan'ı, bozkırı, kızılgerdanı ve gizli duvarlı bahçeyi anlattı; onu yatıştırarak huzurlu bir uykuya daldırdı.",
                "notes": "soothe to sleep: ninnileyip uyutmak; peaceful sleep: huzurlu uyku"
            }
        ]
    },

    # Page 11 (Sentences 201-220)
    {
        "page_no": 11,
        "title": "The Tantrum and Mary's Fierce Words",
        "tr_title": "Öfke Nöbeti ve Mary'nin Kararlı Sözleri",
        "vocab_focus": [
            ("tantrum", "öfke nöbeti"),
            ("rage", "hiddet, öfke"),
            ("hump", "kambur, şişlik"),
            ("screaming", "çığlık atan"),
            ("spine", "omurga"),
            ("nerves", "sinirler"),
            ("soothe", "yatıştırmak"),
            ("defiance", "meydan okuma, başkaldırı")
        ],
        "sentences": [
            {
                "id": 201,
                "text": "For several days, Mary visited Colin in secret, reading stories and bringing him new hope.",
                "translation": "Birkaç gün boyunca Mary gizlice Colin'i ziyaret etti, masallar okudu ve ona yeni umutlar aşıladı.",
                "notes": "visit in secret: gizlice ziyaret etmek; new hope: yeni umut"
            },
            {
                "id": 202,
                "text": "However, Colin was used to behaving like an absolute tyrant when he did not get his way.",
                "translation": "Ancak Colin, her istediği yapılmadığında mutlak bir zorba gibi davranmaya alışmıştı.",
                "notes": "used to behaving: davranmaya alışkın; absolute tyrant: mutlak zorba"
            },
            {
                "id": 203,
                "text": "One afternoon, Mary stayed outside working in the garden with Dickon instead of coming to his room.",
                "translation": "Bir öğleden sonra Mary, Colin'in odasına gitmek yerine dışarıda Dickon'la bahçede çalışmaya devam etti.",
                "notes": "instead of: ...in yerine; outside: dışarıda"
            },
            {
                "id": 204,
                "text": "Colin flew into an uncontrollable rage, screaming that he had felt a lump on his back.",
                "translation": "Colin sırtında bir yumru hissettiğini haykırarak kontrol edilemez bir öfke krizine girdi.",
                "notes": "uncontrollable rage: kontrolsüz öfke; lump on back: sırtta şişlik / yumru"
            },
            {
                "id": 205,
                "text": "His terrifying screams echoed through the dark corridors, throwing the entire household into panic.",
                "translation": "Onun korkunç çığlıkları karanlık koridorlarda yankılandı ve bütün ev halkını paniğe sürükledi.",
                "notes": "terrifying screams: korkunç çığlıklar; household: ev halkı"
            },
            {
                "id": 206,
                "text": "Nurses, servants, and Mrs. Medlock stood weeping and wringing their hands, powerless to calm him.",
                "translation": "Hemşireler, hizmetkarlar ve Bayan Medlock onu sakinleştirmekte çaresiz kalarak ağlıyor ve ellerini ovuşturuyordu.",
                "notes": "powerless to calm: sakinleştirmede çaresiz; wring hands: ellerini ovuşturmak"
            },
            {
                "id": 207,
                "text": "Mary marched furiously into the bedchamber and slammed the door behind her.",
                "translation": "Mary büyük bir öfkeyle yatak odasına daldı ve arkasından kapıyı çarparak kapattı.",
                "notes": "slam door: kapıyı çarpmak; marched furiously: öfkeyle içeri dalmak"
            },
            {
                "id": 208,
                "text": "\"Stop it!\" she shouted at the top of her lungs, \"Stop screaming this instant, you wicked boy!\"",
                "translation": "\"Kes şunu!\" diye avazı çıktığı kadar bağırdı, \"Hemen çığlık atmayı kes, seni yaramaz çocuk!\"",
                "notes": "at the top of lungs: avazı çıktığı kadar; wicked boy: yaramaz çocuk"
            },
            {
                "id": 209,
                "text": "\"I can't stop!\" Colin sobbed hysterically. \"I have a hump! I am going to die!\"",
                "translation": "\"Duramıyorum!\" diye histerik bir şekilde hıçkırdı Colin. \"Sırtımda kambur çıktı! Öleceğim ben!\"",
                "notes": "have a hump: kamburu olmak; hysterically: histerikçe"
            },
            {
                "id": 210,
                "text": "\"You haven't got a lump!\" Mary retorted fiercely. \"Turn over and let me look!\"",
                "translation": "\"Sırtında hiçbir yumru falan yok!\" diye sertçe çıkıştı Mary. \"Dön sırtını da bakayım!\"",
                "notes": "retort fiercely: sertçe çıkışmak; turn over: dönmek"
            },
            {
                "id": 211,
                "text": "She pulled off the blankets and ran her small hands firmly down his bare, thin back.",
                "translation": "Battaniyeleri çekip aldı ve küçük ellerini çıplak, zayıf sırtında kararlılıkla gezdirdi.",
                "notes": "pull off blankets: battaniyeleri çekmek; bare thin back: çıplak zayıf sırt"
            },
            {
                "id": 212,
                "text": "\"There is nothing there!\" she pronounced with absolute authority. \"Not a single lump!\"",
                "translation": "\"Orada hiçbir şey yok!\" diye mutlak bir kesinlikle bildirdi. \"Tek bir yumru bile yok!\"",
                "notes": "absolute authority: kesin otorite; not a single lump: tek bir şişlik bile yok"
            },
            {
                "id": 213,
                "text": "\"Your spine is as straight as mine; you're just a silly boy crying about nothing!\"",
                "translation": "\"Senin omurgan da en az benimki kadar düz; sen sadece hiç yere ağlayan aptal bir çocuksun!\"",
                "notes": "straight spine: düz omurga; crying about nothing: hiç yere ağlamak"
            },
            {
                "id": 214,
                "text": "Colin stopped shrieking, blinking at her in stunned silence.",
                "translation": "Colin çığlık atmayı kesti, afallamış bir sessizlik içinde gözlerini kırpıştırarak ona baktı.",
                "notes": "shrieking: çığlık atma; stunned silence: donakalmış sessizlik"
            },
            {
                "id": 215,
                "text": "\"Do you really mean it?\" he whispered, trembling with sudden relief.",
                "translation": "\"Gerçekten ciddi misin?\" diye fısıldadı, ani bir rahatlamayla titreyerek.",
                "notes": "mean it: ciddi olmak; sudden relief: ani rahatlama"
            },
            {
                "id": 216,
                "text": "\"Of course I mean it! If you would get out into the sunshine and eat fresh food, you would be strong!\"",
                "translation": "\"Elbette ciddiyim! Eğer gün ışığına çıksan ve taze yemekler yesen sapasağlam olursun!\"",
                "notes": "get out into sunshine: gün ışığına çıkmak; strong: güçlü"
            },
            {
                "id": 217,
                "text": "The frightened nurses in the doorway stared at Mary as if she were a miracle worker.",
                "translation": "Kapı eşiğindeki korkmuş hemşireler, sanki bir mucize yaratıcısıymış gibi Mary'ye baka kaldılar.",
                "notes": "miracle worker: mucize yaratan kişi; stare: dik dik bakmak"
            },
            {
                "id": 218,
                "text": "Colin took Mary's hand, his wild temper entirely extinguished by her courage.",
                "translation": "Colin Mary'nin elini tuttu; kızın cesareti karşısında hırçın öfkesi tamamen sönüp gitmişti.",
                "notes": "temper extinguished: öfkesi söndü; courage: cesaret"
            },
            {
                "id": 219,
                "text": "\"Will you bring Dickon to see me?\" Colin asked meekly. \"And will you tell me about the secret garden?\"",
                "translation": "\"Dickon'ı beni görmeye getirir misin?\" diye sordu Colin mahcupça. \"Ve bana gizli bahçeyi anlatır mısın?\"",
                "notes": "meekly: mahcupça, uysalca; bring to see: görmeye getirmek"
            },
            {
                "id": 220,
                "text": "\"I will,\" Mary smiled, \"and when spring comes, we will carry you out into the garden itself!\"",
                "translation": "\"Getiririm,\" diye gülümsedi Mary, \"ve bahar geldiğinde seni bizzat bahçenin içine taşıyacağız!\"",
                "notes": "spring comes: bahar gelir; carry out: dışarı taşımak"
            }
        ]
    },

    # Page 12 (Sentences 221-240)
    {
        "page_no": 12,
        "title": "Bringing Colin into the Secret Garden",
        "tr_title": "Colin'in Bahçeye İlk Çıkışı",
        "vocab_focus": [
            ("wheelchair", "tekerlekli sandalye"),
            ("invalid chair", "hasta arabası"),
            ("cushions", "minderler, yastıklar"),
            ("blankets", "battaniyeler"),
            ("ivory", "fildişi rengi"),
            ("wonder", "hayret, hayranlık"),
            ("sunshine", "güneş ışığı"),
            ("tame", "evcil, uysal")
        ],
        "sentences": [
            {
                "id": 221,
                "text": "Dickon came to Colin's room the very next day, bringing a tame young fox and a crow named Soot.",
                "translation": "Dickon hemen ertesi gün Colin'in odasına geldi; yanında evcil genç bir tilki ve İs adında bir karga getirmişti.",
                "notes": "tame fox: evcil tilki; Soot: İs (karganın adı)"
            },
            {
                "id": 222,
                "text": "Colin was enchanted by the animals, laughing aloud for the first time in his life.",
                "translation": "Colin hayvanlar karşısında büyülendi, hayatında ilk defa kahkahalarla güldü.",
                "notes": "laugh aloud: kahkahayla gülmek; enchanted: büyülenmiş"
            },
            {
                "id": 223,
                "text": "They planned Colin's secret excursion into the gardens with military precision.",
                "translation": "Colin'in bahçelere yapacağı gizli geziyi askeri bir titizlikle planladılar.",
                "notes": "excursion: gezi; military precision: askeri titizlik"
            },
            {
                "id": 224,
                "text": "Colin commanded all servants to remain indoors and clear the paths so nobody would watch them.",
                "translation": "Colin bütün hizmetkarların içeride kalmasını ve kimsenin kendilerini izlememesi için yolları boşaltmasını emretti.",
                "notes": "remain indoors: içeride kalmak; clear paths: yolları boşaltmak"
            },
            {
                "id": 225,
                "text": "On a glorious, warm spring morning, Dickon pushed Colin outside in his wheeled invalid chair.",
                "translation": "Muazzam, ılık bir ilkbahar sabahında Dickon, Colin'i tekerlekli hasta arabasıyla dışarı sürdü.",
                "notes": "glorious spring: muazzam ilkbahar; invalid chair: hasta arabası"
            },
            {
                "id": 226,
                "text": "Colin wore a warm coat and had thick blankets tucked carefully around his frail legs.",
                "translation": "Colin sıcak bir palto giymişti ve kalın battaniyeler narin bacaklarının etrafına özenle sarılmıştı.",
                "notes": "tucked carefully: özenle sarılmış; frail legs: narin bacaklar"
            },
            {
                "id": 227,
                "text": "He looked up at the vast blue sky, breathing the fragrant moor air with wide, hungry eyes.",
                "translation": "Kocaman, aç gözlerle mis kokulu bozkır havasını içine çekerek uçsuz bucaksız mavi gökyüzüne baktı.",
                "notes": "fragrant moor air: mis kokulu bozkır havası; breathe: nefes almak"
            },
            {
                "id": 228,
                "text": "\"The sky is so high and blue!\" he breathed in awe, \"I never knew the world was so beautiful!\"",
                "translation": "\"Gökyüzü o kadar yüksek ve mavi ki!\" diye hayranlıkla soludu, \"Dünyanın bu kadar güzel olduğunu hiç bilmezdim!\"",
                "notes": "in awe: hayranlıkla; high and blue: yüksek ve masmavi"
            },
            {
                "id": 229,
                "text": "They rolled down the gravel path, screened by tall shrubs and thick boxwood hedges.",
                "translation": "Yüksek çalılar ve sık şimşir çitlerle gizlenerek çakıllı patikadan aşağı yuvarlandılar.",
                "notes": "screened by: ...ile gizlenmiş; gravel path: çakıllı patika"
            },
            {
                "id": 230,
                "text": "Mary ran ahead, parted the heavy green ivy, and opened the hidden wooden door.",
                "translation": "Mary önden koştu, ağır yeşil sarmaşığı araladı ve gizli ahşap kapıyı açtı.",
                "notes": "run ahead: önden koşmak; parted ivy: aralanan sarmaşık"
            },
            {
                "id": 231,
                "text": "Dickon pushed the wheelchair gently through the opening, and Mary locked the door safely behind them.",
                "translation": "Dickon tekerlekli sandalyeyi kapı aralığından usulca içeri sürdü ve Mary arkalarından kapıyı güvenle kilitledi.",
                "notes": "push wheelchair: tekerlekli sandalyeyi sürmek; lock safely: güvenle kilitlemek"
            },
            {
                "id": 232,
                "text": "Colin gasped in utter ecstasy: they were inside the secret garden at last!",
                "translation": "Colin katıksız bir vecd içinde soluğunu tuttu: nihayet gizli bahçenin içindeydiler!",
                "notes": "utter ecstasy: tam bir vecd / coşku; at last: nihayet"
            },
            {
                "id": 233,
                "text": "The garden had burst into green life: thousands of rosebuds were swelling along the grey stone walls.",
                "translation": "Bahçe yemyeşil bir hayata uyanmıştı: gri taş duvarlar boyunca binlerce gül goncası kabarıyordu.",
                "notes": "burst into life: hayata uyanmak; rosebuds swelling: kabaran gül goncaları"
            },
            {
                "id": 234,
                "text": "Purple flags, golden crocuses, and waving daffodils danced in the gentle spring breeze.",
                "translation": "Mor süsenler, altın sarısı çiğdemler ve salınan nergisler tatlı bahar melteminde dans ediyordu.",
                "notes": "golden crocuses: altın çiğdemler; gentle breeze: tatlı esinti"
            },
            {
                "id": 235,
                "text": "The grass was fresh and bright green, dotted with snowy blossoms fallen from fruit trees.",
                "translation": "Çimenler taze ve parlak yeşildi, meyve ağaçlarından düşen kar beyazı çiçeklerle beneklenmişti.",
                "notes": "snowy blossoms: kar beyazı çiçekler; fresh grass: taze çimen"
            },
            {
                "id": 236,
                "text": "\"I shall get well!\" Colin shouted triumphantly, tears of pure joy rolling down his cheeks.",
                "translation": "\"Ben iyileşeceğim!\" diye zaferle haykırdı Colin, yanaklarından katıksız sevinç gözyaşları süzülerek.",
                "notes": "get well: iyileşmek; triumphantly: zafer edasıyla"
            },
            {
                "id": 237,
                "text": "\"Mary! Dickon! I shall get well and live forever and ever!\"",
                "translation": "\"Mary! Dickon! Ben iyileşeceğim ve sonsuza kadar yaşayacağım!\"",
                "notes": "live forever: sonsuza dek yaşamak"
            },
            {
                "id": 238,
                "text": "The robin flew down to the grass right beside his chair, singing his sweetest, warmest song.",
                "translation": "Kızılgerdan tam sandalyesinin yanındaki çimenlere indi, en tatlı, en sıcak şarkısını şakıdı.",
                "notes": "flew down: aşağı uçtu; sweetest song: en tatlı şarkı"
            },
            {
                "id": 239,
                "text": "Colin reached out his hand, and the bold little bird pecked at a crumb on his palm.",
                "translation": "Colin elini uzattı ve cesur minik kuş avucundaki bir kırıntıyı gagaladı.",
                "notes": "crumb on palm: avuçtaki kırıntı; reach out hand: elini uzatmak"
            },
            {
                "id": 240,
                "text": "A warm flush of health spread over the boy's face: the magic of the garden had begun its healing work.",
                "translation": "Oğlanın yüzüne sıcacık bir sağlık kırmızılığı yayıldı: bahçenin sihri şifa veren işine başlamıştı.",
                "notes": "warm flush of health: sıcacık sağlık kırmızılığı; healing work: şifa çalışması"
            }
        ]
    },

    # Page 13 (Sentences 241-260)
    {
        "page_no": 13,
        "title": "The Miracle of Spring and Green Shoots",
        "tr_title": "İlkbahar Mucizesi ve Yeşil Filizler",
        "vocab_focus": [
            ("spade", "bel, bahçıvan küreği"),
            ("weeding", "ot ayıklama"),
            ("shoots", "sürgünler, taze filizler"),
            ("appetite", "iştah"),
            ("magic", "büyü, mucizevi güç"),
            ("ladder", "merdiven"),
            ("secret", "sır, gizem"),
            ("miracle", "mucize")
        ],
        "sentences": [
            {
                "id": 241,
                "text": "Every single sunny morning, Dickon and Mary brought Colin out into the secret garden.",
                "translation": "Güneşli her sabah Dickon ve Mary, Colin'i gizli bahçeye dışarı çıkardılar.",
                "notes": "sunny morning: güneşli sabah; secret garden: gizli bahçe"
            },
            {
                "id": 242,
                "text": "They sat him upon a soft pile of cushions beneath an apple tree laden with pink blossoms.",
                "translation": "Pembe çiçeklerle yüklü bir elma ağacının altında onu yumuşak bir minder yığınının üzerine oturttular.",
                "notes": "laden with blossoms: çiçeklerle yüklü; pile of cushions: minder yığını"
            },
            {
                "id": 243,
                "text": "Colin helped them pull weeds, dig with a light spade, and plant seeds with his own hands.",
                "translation": "Colin yabani otları ayıklamalarına, hafif bir kürekle kazmalarına ve kendi elleriyle tohum ekmelerine yardım etti.",
                "notes": "pull weeds: ot ayıklamak; light spade: hafif kürek"
            },
            {
                "id": 244,
                "text": "\"The Magic is in this garden!\" Colin declared enthusiastically. \"Magic is making everything grow and live!\"",
                "translation": "\"Sihir bu bahçenin içinde!\" diye coşkuyla ilan etti Colin. \"Sihir her şeyin büyümesini ve yaşamasını sağlıyor!\"",
                "notes": "enthusiastically: coşkuyla; Magic: Sihir / Mucizevi güç"
            },
            {
                "id": 245,
                "text": "The fresh air and physical work worked wonders on the children's pale, frail bodies.",
                "translation": "Temiz hava ve fiziksel çalışma, çocukların solgun ve narin bedenlerinde mucizeler yarattı.",
                "notes": "work wonders: harikalar yaratmak; frail bodies: narin bedenler"
            },
            {
                "id": 246,
                "text": "Mary's yellow face turned pink and round, and her hair grew glossy and thick.",
                "translation": "Mary'nin sararmış yüzü pembeleşip dolgunlaştı ve saçları gürleşip ışıldadı.",
                "notes": "glossy and thick: parlak ve gür; turned pink: pembeleşti"
            },
            {
                "id": 247,
                "text": "Colin's hollow cheeks filled out, and his thin arms and legs grew muscular and brown from the sun.",
                "translation": "Colin'in çökük yanakları doldu; zayıf kolları ve bacakları kaslanıp güneşten esmerleşti.",
                "notes": "hollow cheeks: çökük yanaklar; muscular and brown: kaslı ve esmerleşmiş"
            },
            {
                "id": 248,
                "text": "They developed such ravenous appetites that Martha had to smuggle extra loaves of bread and jugs of milk out to them.",
                "translation": "Öyle kurt gibi bir iştah geliştirdiler ki Martha onlara gizlice fazladan somun ekmekler ve süt sürahileri taşımak zorunda kaldı.",
                "notes": "ravenous appetite: kurt gibi iştah; smuggle: gizlice sokmak / getirmek"
            },
            {
                "id": 249,
                "text": "Mrs. Medlock and Dr. Craven were utterly bewildered by Colin's dramatic improvement.",
                "translation": "Bayan Medlock ve Doktor Craven, Colin'in bu çarpıcı düzelmesi karşısında tamamen afalladılar.",
                "notes": "utterly bewildered: tamamen şaşkına dönmüş; dramatic improvement: çarpıcı iyileşme"
            },
            {
                "id": 250,
                "text": "Colin pretended to still feel tired indoors so they would not suspect his miraculous secret.",
                "translation": "Colin, o mucizevi sırrından şüphelenmesinler diye içerideyken hala yorgunmuş gibi davrandı.",
                "notes": "pretend: -miş gibi yapmak; miraculous secret: mucizevi sır"
            },
            {
                "id": 251,
                "text": "One afternoon, they heard a scraping noise near the high top of the orchard wall.",
                "translation": "Bir öğleden sonra meyve bahçesi duvarının yüksek tepesi yakınında bir sürtünme sesi duydular.",
                "notes": "scraping noise: sürtünme / kazıma sesi; top of wall: duvarın tepesi"
            },
            {
                "id": 252,
                "text": "Ben Weatherstaff's angry, astonished face appeared over the bricks on a ladder!",
                "translation": "Ben Weatherstaff'ın öfkeli, şaşkın yüzü bir merdivenin üzerinde tuğlaların ardından belirdi!",
                "notes": "astonished face: şaşkın yüz; ladder: merdiven"
            },
            {
                "id": 253,
                "text": "\"What are you doing in the locked garden, you meddlesome brat!\" Ben shouted at Mary.",
                "translation": "\"Kilitli bahçede ne işin var senin, seni burnunu her şeye sokan bücür!\" diye bağırdı Ben Mary'ye.",
                "notes": "meddlesome brat: işgüzar bücür; locked garden: kilitli bahçe"
            },
            {
                "id": 254,
                "text": "Then he caught sight of Colin sitting among the flowers and nearly fell off his ladder.",
                "translation": "Ardından çiçeklerin arasında oturan Colin'i fark etti ve az kalsın merdivenden düşüyordu.",
                "notes": "catch sight of: gözüne çarpmak; fall off ladder: merdivenden düşmek"
            },
            {
                "id": 255,
                "text": "\"Lord save us!\" Ben stammered in awe, \"It is the Master's poor crippled boy!\"",
                "translation": "\"Tanrı bizi korusun!\" diye hayretle kekeledi Ben, \"Efendimizin zavallı kötürüm oğlu bu!\"",
                "notes": "poor crippled boy: zavallı kötürüm çocuk; in awe: dehşetle, hayretle"
            },
            {
                "id": 256,
                "text": "Colin's face flushed red with majestic indignation at being called a cripple.",
                "translation": "Colin'in yüzü kendisine kötürüm denilmesine karşı asil bir öfkeyle kıpkırmızı kesildi.",
                "notes": "majestic indignation: asil öfke; called a cripple: kötürüm denmesi"
            },
            {
                "id": 257,
                "text": "\"Do you know who I am?\" Colin commanded in a strong, ringing voice.",
                "translation": "\"Benim kim olduğumu biliyor musun sen?\" diye emretti Colin güçlü, çınlayan bir sesle.",
                "notes": "ringing voice: çınlayan ses; command: emretmek"
            },
            {
                "id": 258,
                "text": "\"Aye, sir,\" Ben sobbed, wiping his old eyes with a ragged sleeve.",
                "translation": "\"Biliyorum efendim,\" diye hıçkırdı Ben, yırtık pırtık koluyla yaşlı gözlerini silerek.",
                "notes": "ragged sleeve: yırtık pırtık kol; wipe eyes: gözlerini silmek"
            },
            {
                "id": 259,
                "text": "\"You have your mother's sweet eyes, but they told us you were crooked and deformed.\"",
                "translation": "\"Annenizin o tatlı gözleri var sizde fakat bize sizin kambur ve sakat olduğunuzu söylemişlerdi.\"",
                "notes": "crooked and deformed: kambur ve sakat; sweet eyes: tatlı gözler"
            },
            {
                "id": 260,
                "text": "\"Come into the garden, Ben Weatherstaff!\" Colin ordered. \"Come down and see for yourself!\"",
                "translation": "\"Bahçeye gir Ben Weatherstaff!\" diye emretti Colin. \"Aşağı in de kendi gözlerinle gör!\"",
                "notes": "see for yourself: kendi gözlerinle görmek; order: emretmek"
            }
        ]
    },

    # Page 14 (Sentences 261-280)
    {
        "page_no": 14,
        "title": "Colin Stands upon His Own Feet",
        "tr_title": "Colin'in Kendi Ayakları Üzerinde Doğruluşu",
        "vocab_focus": [
            ("stand", "ayakta durmak"),
            ("straight", "dimdik, düz"),
            ("muscles", "kaslar"),
            ("miracle", "mucize"),
            ("tears", "gözyaşları"),
            ("strength", "güç, kuvvet"),
            ("rose-tree", "gül ağacı"),
            ("triumph", "büyük zafer")
        ],
        "sentences": [
            {
                "id": 261,
                "text": "Ben Weatherstaff scrambled down the ladder, ran through the door, and entered the secret garden.",
                "translation": "Ben Weatherstaff merdivenden aşağı indi, kapıdan koştu ve gizli bahçeye adım attı.",
                "notes": "scramble down: aceleyle inmek; entered: girdi"
            },
            {
                "id": 262,
                "text": "He stood gazing in astonishment at the flourishing green roses and bright flowerbeds.",
                "translation": "Gürbüzleşen yeşil güllere ve parlak çiçek tarhlarına şaşkınlıkla bakakaldı.",
                "notes": "flourishing: gürbüzleşen, serpilen; astonishment: hayret"
            },
            {
                "id": 263,
                "text": "\"Look at me!\" Colin said proudly, grasping Dickon's strong shoulder.",
                "translation": "\"Bana bak!\" dedi Colin gururla, Dickon'ın güçlü omzuna tutunarak.",
                "notes": "grasp shoulder: omuza tutunmak; proudly: gururla"
            },
            {
                "id": 264,
                "text": "He swung his legs over the cushions, pushed against the ground, and rose slowly upward.",
                "translation": "Bacaklarını minderlerin üzerinden sarkıttı, yerden destek aldı ve yavaşça yukarı doğru doğruldu.",
                "notes": "swing legs: bacakları sarkıtmak; rise upward: yukarı doğrulmak"
            },
            {
                "id": 265,
                "text": "His knees trembled, but he stiffened his back and stood erect upon his own feet!",
                "translation": "Dizleri titredi fakat sırtını dikleştirdi ve kendi ayakları üzerinde dimdik durdu!",
                "notes": "knees trembled: dizleri titredi; stood erect: dimdik ayakta durdu"
            },
            {
                "id": 266,
                "text": "He stood straight as an arrow, holding his head high like a young king in his domain.",
                "translation": "Kendi mülkünde genç bir kral gibi başını dik tutarak ok gibi dümdüz ayakta durdu.",
                "notes": "straight as an arrow: ok gibi dimdik; domain: mülk, hakimiyet alanı"
            },
            {
                "id": 267,
                "text": "\"Look at me, Ben! Am I crooked? Are my legs deformed?\" Colin challenged with flashing eyes.",
                "translation": "\"Bana bak Ben! Ben kambur muyum? Bacaklarım sakat mı benim?\" diye meydan okudu Colin çakmak çakmak gözlerle.",
                "notes": "challenge: meydan okumak; flashing eyes: parıldayan gözler"
            },
            {
                "id": 268,
                "text": "Old Ben fell to his knees in the grass, tears streaming freely down his weathered cheeks.",
                "translation": "İhtiyar Ben çimenlerin üzerine diz çöktü; yıpranmış yanaklarından yaşlar serbestçe süzüldü.",
                "notes": "fall to knees: diz çökmek; weathered cheeks: yıpranmış yanaklar"
            },
            {
                "id": 269,
                "text": "\"No, my boy! No!\" the old gardener wept, \"You're as straight as any lad in Yorkshire!\"",
                "translation": "\"Hayır evladım! Hayır!\" diye ağladı yaşlı bahçıvan, \"Sen Yorkshire'daki herhangi bir delikanlı kadar dimdiksin!\"",
                "notes": "straight as any lad: her delikanlı kadar dimdik"
            },
            {
                "id": 270,
                "text": "\"God bless your mother's sweet eyes, you're the finest boy that ever walked!\"",
                "translation": "\"Tanrı annenin o tatlı gözlerini kutsasın; sen yeryüzünde yürüyen en mükemmel çocuksun!\"",
                "notes": "finest boy: en mükemmel çocuk; walked: yürümüş"
            },
            {
                "id": 271,
                "text": "Colin took one step forward, then another, walking with steady balance across the green lawn.",
                "translation": "Colin ileriye doğru bir adım attı, ardından bir adım daha; yeşil çimenlik boyunca sağlam bir dengeyle yürüdü.",
                "notes": "steady balance: dengeli adımlarla; lawn: çimenlik"
            },
            {
                "id": 272,
                "text": "Mary clapped her hands in wild jubilation, while Dickon laughed his hearty moorland laugh.",
                "translation": "Dickon o içten bozkır kahkahasını atarken Mary çılgınca bir coşkuyla ellerini çırptı.",
                "notes": "clap hands: el çırpmak; wild jubilation: çılgınca coşku"
            },
            {
                "id": 273,
                "text": "Colin walked all the way to an old plum tree, touched its bark, and turned around smiling.",
                "translation": "Colin yaşlı bir erik ağacına kadar yürüdü, kabuğuna dokundu ve gülümseyerek arkasını döndü.",
                "notes": "plum tree: erik ağacı; touched bark: kabuğa dokundu"
            },
            {
                "id": 274,
                "text": "\"Now we four are sworn to secrecy,\" Colin declared, including Ben Weatherstaff in the pact.",
                "translation": "\"Artık dördümüz de sır saklamaya yeminliyiz,\" diye ilan etti Colin, Ben Weatherstaff'ı da bu ahde katarak.",
                "notes": "sworn to secrecy: sır saklamaya yeminli; pact: sözleşme, ahit"
            },
            {
                "id": 275,
                "text": "\"Nobody must know I can walk until my father comes home to Misselthwaite Manor!\"",
                "translation": "\"Babam Misselthwaite Malikanesi'ne dönene kadar yürüyebildiğimi hiç kimse bilmemeli!\"",
                "notes": "nobody must know: kimse bilmemeli; come home: eve dönmek"
            },
            {
                "id": 276,
                "text": "Ben Weatherstaff gladly promised, promising to bring them rare rose cuttings and fertilizer.",
                "translation": "Ben Weatherstaff memnuniyetle söz verdi, onlara nadir gül çelikleri ve gübre getirmeyi vadetti.",
                "notes": "rose cuttings: gül çelikleri / fideleri; fertilizer: gübre"
            },
            {
                "id": 277,
                "text": "Every morning after that, Colin practiced walking, running, and doing gymnastics under Dickon's guidance.",
                "translation": "O günden sonra her sabah Colin, Dickon'ın rehberliğinde yürüyüş, koşu ve jimnastik talimleri yaptı.",
                "notes": "practice walking: yürüyüş talimi yapmak; under guidance: rehberliğinde"
            },
            {
                "id": 278,
                "text": "His muscles grew hard, his chest expanded, and his laughter could be heard ringing through the garden.",
                "translation": "Kasları sertleşti, göğsü genişledi ve kahkahalarının bahçede çınladığı duyulur oldu.",
                "notes": "muscles grew hard: kasları sertleşti; chest expanded: göğsü genişledi"
            },
            {
                "id": 279,
                "text": "The children sang a hymn of gratitude to the sun, the wind, and the magical earth.",
                "translation": "Çocuklar güneşe, rüzgara ve sihirli toprağa minnettarlıkla bir ilahi söylediler.",
                "notes": "hymn of gratitude: şükran ilahisi; magical earth: sihirli toprak"
            },
            {
                "id": 280,
                "text": "Colin was no longer an invalid waiting for death, but a strong, vibrant, joyful boy.",
                "translation": "Colin artık ölümü bekleyen bir yatalak hasta değil; güçlü, capcanlı ve neşe dolu bir çocuktu.",
                "notes": "no longer an invalid: artık yatalak hasta değil; vibrant: capcanlı"
            }
        ]
    },

    # Page 15 (Sentences 281-300)
    {
        "page_no": 15,
        "title": "Archibald Craven Returns Home to Joy",
        "tr_title": "Archibald Craven'ın Dönüşü ve Büyük Mutluluk",
        "vocab_focus": [
            ("wanderer", "avare gezgin"),
            ("vision", "rüya, ilahi esin"),
            ("unlocked", "kilidi açılmış"),
            ("laughter", "kahkaha"),
            ("embrace", "sarılma, kucaklaşma"),
            ("reconciliation", "barışma, kavuşma"),
            ("master", "efendi, köşkün sahibi"),
            ("alive", "canlı, hayatta")
        ],
        "sentences": [
            {
                "id": 281,
                "text": "Meanwhile, Mr. Archibald Craven had been wandering lonely through the distant valleys of Austria and Italy.",
                "translation": "Bu sırada Bay Archibald Craven, Avusturya ve İtalya'nın uzak vadilerinde yapayalnız dolaşıp durmaktaydı.",
                "notes": "wandering lonely: yapayalnız dolaşarak; distant valleys: uzak vadiler"
            },
            {
                "id": 282,
                "text": "For ten long years, he had carried his heavy soul through foreign cities, unable to escape his grief.",
                "translation": "On uzun yıldır kederinden kaçamayarak ağır ruhunu yabancı şehirlerde taşıyıp durmuştu.",
                "notes": "escape grief: kederden kaçmak; heavy soul: ağır kederli ruh"
            },
            {
                "id": 283,
                "text": "One quiet morning beside a sparkling blue lake in the Alps, an extraordinary peace fell over his heart.",
                "translation": "Alpler'deki pırıl pırıl mavi bir gölün kıyısında sakin bir sabah, kalbine olağanüstü bir huzur indi.",
                "notes": "sparkling lake: pırıl pırıl göl; extraordinary peace: olağanüstü huzur"
            },
            {
                "id": 284,
                "text": "That very night, he dreamed he heard his dead wife's sweet voice calling clearly: \"Archie! Archie! In the garden!\"",
                "translation": "Tam o gece rüyasında, ölü karısının tatlı sesinin açıkça çağırdığını duydu: \"Archie! Archie! Bahçedeyim!\"",
                "notes": "dead wife: merhum eş; sweet voice: tatlı ses"
            },
            {
                "id": 285,
                "text": "Next day, a letter arrived from Dickon's wise mother, Susan Sowerby, urging him to return home at once.",
                "translation": "Ertesi gün Dickon'ın bilge annesi Susan Sowerby'den, derhal eve dönmesini rica eden bir mektup ulaştı.",
                "notes": "urge to return: dönmesini rica etmek / istemek; wise mother: bilge anne"
            },
            {
                "id": 286,
                "text": "Mr. Craven packed his bags immediately and traveled across Europe straight back to Yorkshire.",
                "translation": "Bay Craven derhal valizlerini topladı ve Avrupa'yı boydan boya geçerek doğrudan Yorkshire'a döndü.",
                "notes": "pack bags: valizleri toplamak; straight back: dosdoğru geri"
            },
            {
                "id": 287,
                "text": "He arrived at Misselthwaite Manor on a brilliant summer afternoon when all the moor was in purple bloom.",
                "translation": "Bütün bozkırın mor çiçeklere büründüğü pırıl pırıl bir yaz ikindisinde Misselthwaite Malikanesi'ne vardı.",
                "notes": "purple bloom: mor çiçekler; brilliant summer: pırıl pırıl yaz"
            },
            {
                "id": 288,
                "text": "He walked directly to the locked garden, wondering where the buried key had been lost.",
                "translation": "Gömülü anahtarın nerede kaybolduğunu merak ederek doğrudan kilitli bahçeye doğru yürüdü.",
                "notes": "walk directly: doğrudan yürümek; buried key: gömülü anahtar"
            },
            {
                "id": 289,
                "text": "As he approached the ivy wall, he heard children's running footsteps and joyful laughter inside.",
                "translation": "Sarmaşıklı duvara yaklaştığında, içeride koşan çocuk ayak sesleri ve neşeli kahkahalar duydu.",
                "notes": "running footsteps: koşan ayak sesleri; joyful laughter: neşeli kahkahalar"
            },
            {
                "id": 290,
                "text": "Suddenly, the heavy wooden door was flung wide open from within.",
                "translation": "Birden ağır ahşap kapı içeriden ardına kadar açıldı.",
                "notes": "flung wide open: ardına kadar açıldı; from within: içeriden"
            },
            {
                "id": 291,
                "text": "A boy dashed out into the sunlight at full speed, running straight into Mr. Craven's open arms!",
                "translation": "Bir oğlan çocuğu son sürat gün ışığına fırladı ve dosdoğru Bay Craven'ın açık kollarına daldı!",
                "notes": "dash out: dışarı fırlamak; at full speed: son sürat"
            },
            {
                "id": 292,
                "text": "He was tall, handsome, glowing with health, and had his mother's glorious grey eyes.",
                "translation": "Uzun boylu, yakışıklı, sağlıktan parıldayan bir çocuktu ve annesinin o muazzam gri gözlerine sahipti.",
                "notes": "glowing with health: sağlıktan ışıldayan; glorious eyes: muhteşem gözler"
            },
            {
                "id": 293,
                "text": "\"Who are you?\" Mr. Craven gasped, his heart stopping in trembling disbelief.",
                "translation": "\"Kimsin sen?\" diye nefesi kesildi Bay Craven'ın, kalbi titreyen bir inanamazlıkla duracak gibi olarak.",
                "notes": "trembling disbelief: titrek bir inanamama hali; gasp: nefesi kesilmek"
            },
            {
                "id": 294,
                "text": "\"Father!\" the boy shouted joyfully, standing tall and proud before him. \"I am Colin!\"",
                "translation": "\"Baba!\" diye sevinçle haykırdı oğlan, önünde dimdik ve gururla durarak. \"Ben Colin'im!\"",
                "notes": "standing tall: dimdik durarak; proudly: gururla"
            },
            {
                "id": 295,
                "text": "\"It was the garden that made me well, with Mary and Dickon! I am as straight as any boy!\"",
                "translation": "\"Beni iyileştiren bahçe oldu, Mary ve Dickon'la birlikte! Ben her çocuk kadar dimdikim!\"",
                "notes": "made me well: beni iyileştirdi; straight as any boy: her çocuk kadar düzgün"
            },
            {
                "id": 296,
                "text": "Archibald Craven pulled his son to his breast, weeping tears of overwhelming joy and gratitude.",
                "translation": "Archibald Craven oğlunu bağrına bastı; taşkın bir sevinç ve minnettarlık gözyaşları döktü.",
                "notes": "pull to breast: bağrına basmak; overwhelming joy: taşkın sevinç"
            },
            {
                "id": 297,
                "text": "Colin led his father into the garden, showing him the thousand climbing roses blooming in scarlet glory.",
                "translation": "Colin babasını bahçeye soktu; ona al rengi görkemiyle çiçek açan binlerce sarmaşık gülü gösterdi.",
                "notes": "climbing roses: sarmaşık güller; scarlet glory: al rengi ihtişam"
            },
            {
                "id": 298,
                "text": "The dark spell of ten years of sorrow was broken forever in that glorious place.",
                "translation": "On yıllık kederin karanlık büyüsü o muhteşem mekanda sonsuza dek bozuldu.",
                "notes": "spell broken: büyü bozuldu; glorious place: muhteşem yer"
            },
            {
                "id": 299,
                "text": "In the afternoon, the servants of Misselthwaite Manor stood gaping in dumbfounded wonder.",
                "translation": "İkindi vakti Misselthwaite Malikanesi'nin hizmetkarları küçük dillerini yutmuş bir hayranlıkla baka kaldılar.",
                "notes": "dumbfounded wonder: şaşkınlıktan donakalmış hayranlık; gaping: ağzı açık bakmak"
            },
            {
                "id": 300,
                "text": "Walking proudly across the lawn beside the master of the house was young Master Colin, head held high and strong on his own two feet.",
                "translation": "Konağın efendisinin yanında çimenlikte gururla yürüyen kişi; başı dik, kendi iki ayağı üzerinde sapasağlam duran genç Efendi Colin'in ta kendisiydi.",
                "notes": "head held high: başı dik; own two feet: kendi iki ayağı üzerinde"
            }
        ]
    }
]

def main():
    total_pages = len(pages_data)
    total_sentences = sum(len(p["sentences"]) for p in pages_data)
    total_vocab = sum(len(p.get("vocab_focus", [])) for p in pages_data)

    print(f"Book 23 Data Verification:")
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

    out_file = os.path.join(os.path.dirname(__file__), "book_23_data.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('BOOK_TITLE = "The Secret Garden"\n')
        f.write('AUTHOR = "Frances Hodgson Burnett"\n')
        f.write("PAGES_DATA = ")
        import pprint
        f.write(pprint.pformat(pages_data, indent=4, width=120))
        f.write("\n")

    print(f"Successfully wrote {out_file}")

if __name__ == "__main__":
    main()
