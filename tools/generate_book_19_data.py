"""
Book 19 Generator: Gulliver's Travels (Jonathan Swift)
15 Pages, exactly 20 sentences per page = 300 sentences total.
8 Target vocabulary terms per page = 120 vocabulary items total.
Level 1 / Seviye 1 Graded Reader for English learners.
"""

import os
import pprint

BOOK_META = {
    "id": "book_19_gullivers_travels",
    "title": "Gulliver's Travels: Extraordinary Voyages",
    "subtitle": "Jonathan Swift's Timeless Satire of Lilliput, Giants, Flying Islands, and Reason",
    "author": "Jonathan Swift",
    "level": "Seviye 1 (A1-A2 Beginner)",
    "target_readers": "İngilizce öğrenenler ve klasik seyahatname maceralarını sevenler için çift dilli okuma kitabı",
    "total_pages": 15,
    "sentences_per_page": 20,
    "total_sentences": 300,
    "theme_color_primary": "#0369A1",    # Ocean Sky Blue
    "theme_color_secondary": "#D97706",  # Lilliput Gold / Imperial Amber
    "theme_color_accent": "#DC2626",     # Giant Crimson
    "theme_color_light": "#F0F9FF"       # Seafoam Tint
}

TR_TITLES = [
    "Lilliput'ta Deniz Kazası ve Tutsaklık",
    "İmparator'un Huzurunda Dağ Adam",
    "Saray İp Cambazları ve Eğlenceler",
    "Yüksek Ökçeler ve Yumurta Savaşı",
    "Blefuscu Donanmasının Zapt Edilişi",
    "Saray Yangını ve İhanet Suçlaması",
    "Lilliput'tan Kaçış ve Eve Dönüş",
    "Brobdingnag: Devler Ülkesi",
    "Glumdalclitch ve Minik Bakıcı",
    "Dev Kraliçe'nin Sarayında",
    "Dev Kral ile Felsefi Sohbetler",
    "Kartalın Pençesinde Kurtuluş",
    "Laputa: Uçan Ada ve Lagado Akademisi",
    "Houyhnhnm'ler: Akıl Sahibi Atlar",
    "İnsanlar Diyarına Dönüş ve Hikmet"
]

PAGES = [
    # Page 1: The Shipwreck at Lilliput
    {
        "page_number": 1,
        "title": "Shipwreck at Lilliput",
        "vocab": [
            ("shipwreck", "gemi kazası"),
            ("surgeon", "cerrah, gemi doktoru"),
            ("strand", "karaya vurmak / iplik"),
            ("pygmy", "cüce"),
            ("quiver", "ok kılıfı, sadak"),
            ("fasten", "bağlamak, sabitlemek"),
            ("snout", "burun"),
            ("shout", "haykırmak")
        ],
        "sentences": [
            ("My name is Lemuel Gulliver, and I was born in Nottinghamshire to a modest family.", "Benim adım Lemuel Gulliver ve Nottinghamshire'da mütevazı bir ailenin çocuğu olarak doğdum.", "Passive voice 'was born'; prepositional phrase of origin."),
            ("I studied medicine at Leyden and became a ship's surgeon on voyages across distant oceans.", "Leyden'de tıp okudum ve uzak okyanuslardaki seferlerde gemi cerrahı oldum.", "Coordinate past verbs 'studied and became'; compound noun 'ship's surgeon'."),
            ("In May 1699, I set sail from Bristol aboard the merchant vessel Antelope, bound for the South Seas.", "Mayıs 1699'da, Güney Denizlerine gitmekte olan tüccar gemisi Antelope ile Bristol'den yelken açtım.", "Prepositional phrases indicating date, port, and vessel; participle 'bound for'."),
            ("A furious storm drove our ship against a jagged rock in the East Indies, splitting the hull.", "Kudretli bir fırtına gemimizi Doğu Hint Adaları'ndaki sarp bir kayaya çarptı, tekneyi yardı.", "Coordinate participles describing catastrophe; adjective 'jagged'."),
            ("Six of the crew, including myself, pushed a lifeboat into the churning waves.", "Ben dahil altı mürettebat, köpüren dalgaların içine bir filika indirdik.", "Participial preposition 'including myself'; past verb 'pushed'."),
            ("Within half an hour, our tiny rowboat was overturned by a sudden violent squall.", "Yarım saat içinde minik sandalımız ani ve şiddetli bir sağanakla devrildi.", "Passive voice 'was overturned'; compound noun 'violent squall'."),
            ("I swam as fortune directed me, pushed forward by wind and incoming tide.", "Rüzgar ve gelen gelgitle ileri itilerek, talihin beni yönlendirdiği gibi yüzdüm.", "Passive participle modifier 'pushed forward'; manner clause 'as fortune directed'."),
            ("When my strength was nearly exhausted, my feet miraculously touched bottom.", "Gücüm neredeyse tükenmişken, ayaklarım mucizevi bir şekilde tabana değdi.", "Time clause with 'exhausted'; adverb 'miraculously'."),
            ("I waded ashore through the shallow water and collapsed upon soft green grass.", "Sığ sudan yürüyerek karaya çıktım ve yumuşak yeşil çimenlerin üzerine yığıldım.", "Coordinate past verbs 'waded and collapsed'; adjective 'shallow'."),
            ("I slept deeper and more soundly than ever I remembered in my whole existence.", "Bütün hayatımda hatırladığım her zamankinden daha derin ve mışıl mışıl uyudum.", "Comparative adverbs 'deeper and more soundly'; noun phrase 'whole existence'."),
            ("When I awoke, daylight had arrived, but I found myself unable to rise or stir.", "Uyandığımda gün aydınlanmıştı fakat kendimi kalkamaz ya da kıpırdayamaz halde buldum.", "Time clause with 'awoke'; adjective phrase 'unable to rise or stir'."),
            ("My arms and legs were strongly fastened on each side to the ground with slender pegs.", "Kollarım ve bacaklarım her iki yanımdan ince kazıklarla yere sımsıkı bağlanmıştı.", "Passive voice 'were fastened'; instrument phrase 'with slender pegs'."),
            ("My thick hair was likewise tied down in hundreds of places with thin cords.", "Gür saçlarım da aynı şekilde yüzlerce yerinden ince iplerle aşağı bağlanmıştı.", "Passive voice 'was tied down'; adverb 'likewise'."),
            ("I could only look upward into the dazzling, brilliant glare of the sky.", "Yalnızca gökyüzünün göz alıcı, parlak parıltısına doğru yukarı bakabiliyordum.", "Modal 'could only look'; directional adverb 'upward'."),
            ("Presently, I felt something alive moving gently upon my left leg.", "Çok geçmeden sol bacağımın üzerinde usulca hareket eden canlı bir şey hissettim.", "Perception verb 'felt' + participle 'moving gently'."),
            ("It advanced over my breast until it stood directly beneath my chin.", "Tam çenemin altına gelene kadar göğsümün üzerinden ileri doğru ilerledi.", "Time clause with 'until'; past verb 'advanced'."),
            ("Bending my eyes downward, I perceived a human creature not six inches high.", "Gözlerimi aşağıya doğru çevirerek, on beş santim bile boyu olmayan bir insan yaratığı fark ettim.", "Participle clause 'Bending eyes'; measurement 'not six inches high'."),
            ("He held a tiny bow and arrow in his hands, with a miniature quiver at his back.", "Sırtında minyatür bir sadakla, ellerinde minicik bir yay ve ok tutuyordu.", "Prepositional phrases indicating gear; past verb 'held'."),
            ("Forty more of the same tiny species followed after him, shouting in high, shrill voices.", "Aynı minik türden kırk tanesi daha tiz çığlıklar atarak onun ardından geldi.", "Coordinate participles; adjective pair 'high, shrill'."),
            ("In utter astonishment, I roared so loudly that they all fled backward in panic.", "Tam bir hayret içinde öyle yüksek sesle kükredim ki hepsi panik içinde geriye kaçtılar.", "Result clause 'so loudly that'; prepositional phrase 'In utter astonishment'.")
        ]
    },
    # Page 2: Captive of the Emperor
    {
        "page_number": 2,
        "title": "The Man-Mountain of Mildendo",
        "vocab": [
            ("emperor", "imparator"),
            ("vehicle", "araç, taşıt"),
            ("wagon", "araba, vagon"),
            ("carcase", "gövde, karkas"),
            ("hogshead", "büyük fıçı"),
            ("temple", "tapınak"),
            ("chain", "zincir"),
            ("majesty", "haşmet, majesteleri")
        ],
        "sentences": [
            ("I struggled to break my bonds, wrenching out the wooden pegs on my left side.", "Sol tarafımdaki tahta kazıkları sökerek bağlarımı koparmak için çabaladım.", "Participle clause 'wrenching out pegs'; infinitive 'to break bonds'."),
            ("Instantly, a volley of hundreds of tiny arrows pricked my face and hands like needles.", "Anında yüzlerce minik oktan oluşan bir yaylım ateşi yüzüme ve ellerime iğne gibi battı.", "Simile 'like needles'; past verb 'pricked'."),
            ("I decided it was prudent to lie perfectly still until nightfall arrived.", "Gece çökene kadar tamamen hareketsiz yatmanın tedbirlice bir karar olduğunu düşündüm.", "Noun clause with dummy subject 'it was prudent to lie'; adverb 'perfectly still'."),
            ("Seeing me tranquil, the Lilliputians ceased shooting their needle-like shafts.", "Benim sakinleştiğimi gören Lilliputlular iğneye benzeyen oklarını fırlatmayı bıraktılar.", "Participle clause of perception; verb + gerund 'ceased shooting'."),
            ("They built a wooden platform near my ear, and an important personage addressed me.", "Kulağımın yanına tahta bir platform inşa ettiler ve önemli bir şahsiyet bana hitap etti.", "Coordinate past clauses; noun 'personage'."),
            ("Though I could not understand his tongue, I signified my hunger by putting fingers to my mouth.", "Dilini anlayamasam da parmaklarımı ağzıma götürerek açlığımı belirttim.", "Concession clause with 'though'; preposition 'by' + gerund."),
            ("Ladders were placed against my sides, and hundreds of servants climbed up with baskets.", "Böğrüme merdivenler dayandı ve yüzlerce hizmetkar sepetlerle yukarı tırmandı.", "Passive voice 'were placed'; preposition 'with baskets'."),
            ("I ate entire shoulders of mutton at one mouthful, and whole loaves of bread three at a time.", "Tek bir lokmada bütün bir koyun budunu ve bir seferde üçer üçer koca somun ekmekleri yedim.", "Parallel adverbial phrases describing appetite; past verb 'ate'."),
            ("They rolled two hogsheads of their best wine up to my hand, which I drank at a single gulp.", "En iyi şaraplarından iki koca fıçıyı elime yuvarladılar, ben de onları tek bir yudumda dikip içtim.", "Relative clause 'which I drank'; measurement 'hogshead'."),
            ("A sleeping potion had been mixed into the liquor, causing me to sink into deep slumber.", "İçkinin içine beni derin bir uykuya sevk eden bir uyku iksiri karıştırılmıştı.", "Past perfect passive 'had been mixed'; participle clause 'causing me to sink'."),
            ("Five hundred carpenters built an enormous wooden carriage seven feet long with twenty-two wheels.", "Beş yüz marangoz yirmi iki tekerlekli, yedi fit uzunluğunda devasa tahta bir araba inşa etti.", "Descriptive measurement phrases; numeral 'twenty-two wheels'."),
            ("Nine hundred of the strongest men hoisted my sleeping body upon this colossal engine.", "En güçlü adamlardan dokuz yüzü uyuyan gövdemi bu devasa aracın üzerine kaldırdı.", "Superlative phrase 'strongest men'; transitive past 'hoisted'."),
            ("Fifteen hundred of the Emperor's largest horses dragged the carriage toward the capital.", "İmparator'un en büyük atlarından bin beş yüzü arabayı başkente doğru çekti.", "Measurement subject; directional phrase 'toward the capital'."),
            ("Mildendo, the metropolis of Lilliput, was surrounded by walls two and a half feet high.", "Lilliput'un metropolü Mildendo iki buçuk fit yüksekliğinde surlarla çevriliydi.", "Passive voice 'was surrounded by'; measurement 'two and a half feet high'."),
            ("I was housed in an ancient, abandoned stone temple, the largest building in the realm.", "Ülkedeki en büyük bina olan kadim, terk edilmiş taştan bir tapınağa yerleştirildim.", "Passive voice 'was housed in'; appositive noun phrase."),
            ("My left leg was chained with ninety-one tiny padlocks, allowing me only a little movement.", "Sol bacağım sadece biraz hareket etmeme izin veren doksan bir minik asma kilitle zincirlendi.", "Passive voice 'was chained'; participle clause 'allowing me movement'."),
            ("The Emperor of Lilliput rode up on a spirited charger to inspect the Man-Mountain.", "Lilliput İmparatoru Dağ Adam'ı teftiş etmek için canlı bir savaş atı üzerinde çıkageldi.", "Phrasal verb 'rode up on'; infinitive of purpose 'to inspect'."),
            ("He was taller by the breadth of a human fingernail than any of his courtiers.", "Saray mensuplarının hepsinden bir insan tırnağı genişliği kadar daha uzundu.", "Comparative adjective 'taller by breadth of fingernail'; noun 'courtiers'."),
            ("He held a drawn golden sword to defend himself if I should break my chains.", "Eğer zincirlerimi kıracak olursam kendini savunmak için elinde çekilmiş altın bir kılıç tutuyordu.", "Conditional clause 'if I should break'; infinitive of purpose 'to defend'."),
            ("Six hundred persons were assigned as my domestic servants, providing daily rations.", "Altı yüz kişi günlük erzak sağlayan ev hizmetkarlarım olarak tayin edildi.", "Passive voice 'were assigned'; participle phrase 'providing rations'.")
        ]
    },
    # Page 3: The Diversions of the Court
    {
        "page_number": 3,
        "title": "The Court of Lilliput",
        "vocab": [
            ("diversion", "eğlence, gösteri"),
            ("rope", "ip, urgan"),
            ("thread", "iplik"),
            ("somersault", "takla"),
            ("office", "makam, memuriyet"),
            ("creeping", "emekleme, sürünme"),
            ("favour", "lütuf, iltifat"),
            ("dexterity", "maharet, el çabukluğu")
        ],
        "sentences": [
            ("The Emperor and his court were entertained by extraordinary political diversions.", "İmparator ve sarayı sıra dışı siyasi gösterilerle eğlendirilirdi.", "Passive voice 'were entertained by'; compound adjective 'political diversions'."),
            ("When a great office of state became vacant, candidates competed on a tightrope.", "Devletin büyük bir makamı boşaldığında, adaylar gergin bir ip üzerinde yarıştılar.", "Time clause with 'became vacant'; prepositional phrase 'on a tightrope'."),
            ("Whoever jumped the highest on the slender thread without falling received the appointment.", "Düşmeden incecik ip üzerinde en yükseğe zıplayan kişi tayin edilirdi.", "Relative subject clause 'Whoever jumped'; participle phrase 'without falling'."),
            ("Chief ministers were frequently chosen purely for their dexterity in turning somersaults.", "Başbakanlar sıklıkla sadece takla atmadaki maharetleri yüzünden seçilirdi.", "Passive voice 'were chosen'; adverb 'purely'."),
            ("Another ceremony was performed for the Emperor's favorite courtiers and noblemen.", "Bir başka tören İmparator'un gözde saray mensupları ve soyluları için icra edilirdi.", "Passive voice 'was performed for'; possessive noun phrase."),
            ("The Emperor held a blue silk thread horizontally, two feet above the ground.", "İmparator mavi ipekten bir ipliği yerden iki fit yukarıda yatay olarak tutardı.", "Adverb 'horizontally'; measurement phrase 'two feet above ground'."),
            ("Candidates had to leap over the thread or creep beneath it back and forth.", "Adaylar ipliğin üzerinden atlamak veya altından ileri geri sürünmek zorundaydılar.", "Modal obligation 'had to leap or creep'; prepositional phrases."),
            ("The winner received a blue thread; the second, a red; and the third, a green.", "Birinci mavi bir iplik aldı; ikinci kırmızı, üçüncü ise yeşil.", "Parallel elliptical sentences describing royal honors."),
            ("These colored threads were worn proudly around the waist like badges of distinction.", "Bu renkli iplikler bel çevresinde birer şeref nişanı gibi gururla taşınırdı.", "Simile 'like badges of distinction'; passive voice 'were worn'."),
            ("I gradually learned the Lilliputian language and conversed politely with His Majesty.", "Lilliput dilini yavaş yavaş öğrendim ve Majesteleri ile kibarca sohbet ettim.", "Coordinate past verbs 'learned and conversed'; adverb 'gradually'."),
            ("My gentle behavior and compliance won the confidence of the imperial court.", "Nazik davranışım ve uyum gösterişim imparatorluk sarayının güvenini kazandı.", "Coordinate subjects; past verb 'won'."),
            ("Officers searched my pockets and drew up an inventory of my strange possessions.", "Subaylar ceplerimi aradılar ve garip eşyalarımın bir dökümünü çıkardılar.", "Coordinate past verbs 'searched and drew up'; compound noun 'inventory'."),
            ("They described my watch as a miraculous engine that ticked like an iron heart.", "Saatimi demir bir kalp gibi tıkırdayan mucizevi bir makine olarak tarif ettiler.", "Simile 'like an iron heart'; relative clause 'that ticked'."),
            ("They inspected my comb, snuffbox, handkerchief, and my silver coins with wonder.", "Tarağımı, enfiye kutumu, mendilimi ve gümüş sikkelerimi hayretle incelediler.", "List of objects; prepositional phrase 'with wonder'."),
            ("I surrendered my pistols, firing one into the air to demonstrate its thunder.", "Gök gürültüsünü göstermek için havaya bir el ateş ederek tabancalarımı teslim ettim.", "Participle clause 'firing one'; past verb 'surrendered'."),
            ("Hundreds of soldiers collapsed in terror at the terrifying flash and smoke.", "Korkunç alev ve duman karşısında yüzlerce asker dehşet içinde yere yığıldı.", "Prepositional phrase 'at flash and smoke'; past verb 'collapsed'."),
            ("The Emperor finally granted me my liberty under strict constitutional articles.", "İmparator sonunda katı anayasal maddeler altında bana özgürlüğümü bahşetti.", "Adjective phrase 'strict constitutional articles'; past verb 'granted'."),
            ("I had to swear to assist Lilliput against its enemies and maintain the roads.", "Düşmanlarına karşı Lilliput'a yardım etmeye ve yolları bakımlı tutmaya yemin etmek zorundaydım.", "Coordinate infinitives; modal 'had to swear'."),
            ("My chains were unlocked, and I stood up a free man in the miniature kingdom.", "Zincirlerim açıldı ve minyatür krallıkta özgür bir adam olarak ayağa kalktım.", "Passive coordinate 'chains were unlocked'; past verb 'stood up'."),
            ("The tiny people cheered, hailing the Man-Mountain as their mighty protector.", "Minik halk tezahürat yaptı, Dağ Adam'ı kendi kudretli koruyucuları olarak selamladı.", "Participle phrase 'hailing Man-Mountain'; past verb 'cheered'.")
        ]
    },
    # Page 4: The Blefuscu Threat and the High-Heels
    {
        "page_number": 4,
        "title": "Factions and Foreign Foes",
        "vocab": [
            ("faction", "hizip, fırka"),
            ("heel", "ayakkabı ökçesi"),
            ("dispute", "anlaşmazlık, ihtilaf"),
            ("empire", "imparatorluk"),
            ("schism", "ayrılık, bölünme"),
            ("egg", "yumurta"),
            ("edict", "ferman, buyruk"),
            ("fleet", "donanma")
        ],
        "sentences": [
            ("Reldresal, Principal Secretary for Private Affairs, visited me to explain the empire's troubles.", "Özel İşler Baş Katibi Reldresal, imparatorluğun dertlerini anlatmak için beni ziyaret etti.", "Appositive title; infinitive of purpose 'to explain troubles'."),
            ("He revealed that Lilliput was divided by two furious domestic factions.", "Lilliput'un iki öfkeli yerel hizip tarafından bölündüğünü açıkladı.", "Noun clause with passive; adjective 'domestic factions'."),
            ("The factions were called Tramecksan and Slamecksan, distinguished by their shoe heels.", "Bu hizipler ayakkabı ökçeleriyle ayırt edilen Tramecksan ve Slamecksan olarak adlandırılıyordu.", "Passive voice 'were called'; past participle modifier 'distinguished by'."),
            ("The High-Heels adhered to ancient traditions, while the Low-Heels held imperial power.", "Yüksek Ökçeliler kadim geleneklere bağlıydı, Alçak Ökçeliler ise imparatorluk gücünü elinde tutuyordu.", "Coordinate clauses with 'while'; past verbs 'adhered and held'."),
            ("The Emperor wore only low heels, though one of his heels was a fraction higher than the other.", "Bir ökçesi diğerinden bir parça daha yüksek olsa da İmparator sadece alçak ökçeler giyerdi.", "Concession clause with 'though'; comparative 'higher than the other'."),
            ("This caused the monarch to walk with a peculiar hobble through the palace halls.", "Bu durum hükümdarın saray koridorlarında tuhaf bir aksamayla yürümesine sebep oluyordu.", "Causative structure 'caused monarch to walk'; prepositional phrase."),
            ("Worse still, Lilliput was threatened with invasion by the mighty island empire of Blefuscu.", "Daha da kötüsü Lilliput, kudretli ada imparatorluğu Blefuscu tarafından istila edilmekle tehdit ediliyordu.", "Adverbial modifier 'Worse still'; passive voice 'was threatened with'."),
            ("These two mighty empires had waged bloody warfare for six and thirty moons.", "Bu iki kudretli imparatorluk otuz altı aydır kanlı bir savaş sürdürmekteydi.", "Past perfect continuous sense; archaic numeral 'six and thirty moons'."),
            ("The war originated from a ridiculous dispute over the proper way to break boiled eggs.", "Savaş, haşlanmış yumurtaları kırmanın doğru şekli üzerine gülünç bir anlaşmazlıktan çıkmıştı.", "Phrasal verb 'originated from'; prepositional phrase 'over proper way'."),
            ("Ancient practice commanded all subjects to break eggs at the larger end.", "Kadim adet bütün tebaanın yumurtaları büyük ucundan kırmasını emrediyordu.", "Verb + object + infinitive 'commanded subjects to break'."),
            ("However, the present Emperor's grandfather, when a boy, had cut his finger breaking the big end.", "Ancak şimdiki İmparator'un dedesi bir çocukken büyük ucunu kırarken parmağını kesmişti.", "Parenthetical time phrase 'when a boy'; past perfect 'had cut'."),
            ("The old Emperor immediately published an edict commanding everyone to break the smaller end.", "Eski İmparator derhal herkesin yumurtayı küçük ucundan kırmasını emreden bir ferman yayımladı.", "Participle phrase 'commanding everyone'; past verb 'published'."),
            ("The people resented this decree, leading to six civil rebellions across the empire.", "Halk bu fermanı hazmedemedi ve bu durum imparatorluk genelinde altı iç isyana yol açtı.", "Participle clause of result 'leading to rebellions'; past verb 'resented'."),
            ("Monarchs lost their crowns and lives in the bitter struggle over eggshells.", "Hükümdarlar yumurta kabukları üzerine çıkan bu acı mücadelede taçlarını ve hayatlarını kaybettiler.", "Coordinate direct objects; prepositional phrase 'over eggshells'."),
            ("The Big-Endian rebels found refuge at the court of Blefuscu, plotting invasion.", "Büyük Uçlular isyancıları istila planları yaparak Blefuscu sarayına sığındılar.", "Participle phrase 'plotting invasion'; past verb 'found refuge'."),
            ("The Emperor of Blefuscu had assembled an immense fleet ready to sail upon Lilliput.", "Blefuscu İmparatoru Lilliput üzerine yelken açmaya hazır muazzam bir donanma toplamıştı.", "Past perfect 'had assembled'; adjective phrase 'ready to sail'."),
            ("Reldresal begged me in His Majesty's name to defend the nation from destruction.", "Reldresal milleti yıkımdan korumam için Majesteleri adına bana yalvardı.", "Prepositional phrase 'in His Majesty's name'; infinitive 'to defend'."),
            ("I promised to defend the Emperor's person and state against all foreign aggressors.", "Bütün yabancı saldırganlara karşı İmparator'un şahsını ve devletini koruyacağıma söz verdim.", "Infinitive of purpose; preposition 'against foreign aggressors'."),
            ("I formulated a bold naval strategy to capture the enemy's entire fleet at once.", "Düşmanın bütün donanmasını tek seferde ele geçirmek için cesur bir denizcilik stratejisi hazırladım.", "Infinitive 'to capture'; compound noun 'naval strategy'."),
            ("The fate of two warring empires now rested upon my giant shoulders.", "Savaşan iki imparatorluğun kaderi artık benim dev omuzlarıma dayanıyordu.", "Past verb 'rested upon'; participial adjective 'warring empires'.")
        ]
    },
    # Page 5: The Capture of the Blefuscudian Fleet
    {
        "page_number": 5,
        "title": "The Conquest of the Armada",
        "vocab": [
            ("armada", "armada, donanma"),
            ("channel", "deniz boğazı, kanal"),
            ("cable", "kalın halat"),
            ("hook", "kanca"),
            ("wade", "suda bata çıka yürümek"),
            ("cut", "kesmek"),
            ("triumph", "zafer"),
            ("glory", "şan, şeref")
        ],
        "sentences": [
            ("The channel separating Lilliput from Blefuscu was only eight hundred yards wide.", "Lilliput'u Blefuscu'dan ayıran boğaz sadece sekiz yüz yarda genişliğindeydi.", "Participle modifier 'separating Lilliput'; measurement phrase."),
            ("I consulted experienced sailors to determine the depth of the water across the strait.", "Boğaz boyunca suyun derinliğini belirlemek için tecrübeli denizcilere danıştım.", "Infinitive of purpose 'to determine depth'; past verb 'consulted'."),
            ("They informed me that at high tide it was no more than six feet deep.", "Suların yükseldiği gelgitte suyun altı fitten daha derin olmadığını bana bildirdiler.", "Noun clause with 'that'; comparative 'no more than six feet deep'."),
            ("I ordered a large quantity of the strongest cables and bars of iron to be forged.", "En güçlü halatlardan ve demir çubuklardan büyük bir miktarın dövülmesini emrettim.", "Passive infinitive structure 'to be forged'; past verb 'ordered'."),
            ("I twisted three cables together to make a rope, and bent the iron bars into fifty hooks.", "Bir urgan yapmak için üç halatı birbirine ördüm ve demir çubukları büküp elli kanca yaptım.", "Coordinate past verbs 'twisted and bent'; infinitive of purpose."),
            ("Fastening a hook to each cable, I set out for the northern coast overlooking Blefuscu.", "Her bir halata bir kanca bağlayarak Blefuscu'ya bakan kuzey kıyısına doğru yola çıktım.", "Participle clauses 'Fastening a hook' and 'overlooking Blefuscu'."),
            ("I stripped off my coat, shoes, and stockings, and waded into the salty water.", "Ceketimi, ayakkabılarımı ve çoraplarımı çıkardım ve tuzlu suyun içine daldım.", "Coordinate past verbs 'stripped off and waded into'."),
            ("I swam in the middle for about thirty yards until my feet touched the seabed again.", "Ayaklarım deniz tabanına tekrar değene kadar ortada yaklaşık otuz yarda kadar yüzdüm.", "Time clause with 'until'; past verb 'swam'."),
            ("In less than half an hour, I reached the Blefuscudian harbor where the fleet lay anchored.", "Yarım saatten az bir sürede donanmanın demirli yattığı Blefuscu limanına ulaştım.", "Relative clause of place 'where fleet lay anchored'; time phrase."),
            ("The enemy sailors were so terrified at the sight of me that they leaped overboard.", "Düşman denizciler beni görünce o kadar dehşete düştüler ki denize atladılar.", "Result clause 'so terrified that'; phrasal verb 'leaped overboard'."),
            ("Thirty thousand men swam ashore, screaming with panic across the shallow waters.", "Otuz bin adam sığ sular boyunca panikle çığlıklar atarak kıyıya doğru yüzdü.", "Participle phrase 'screaming with panic'; past verb 'swam ashore'."),
            ("I took my fifty hooks and fastened one to the prow of each royal warship.", "Elli kancamı aldım ve her bir kraliyet savaş gemisinin pruvasına bir tane taktım.", "Coordinate past verbs 'took and fastened'; possessive phrase."),
            ("I tied all the cords together into one great knot at my chest.", "Bütün ipleri göğsümün üzerinde tek bir büyük düğüm halinde birbirine bağladım.", "Prepositional phrase 'into one great knot'; past verb 'tied'."),
            ("The Blefuscudians fired thousands of arrows from the shore, striking my face and hands.", "Blefusculular kıyıdan yüzüme ve ellerime isabet eden binlerce ok attılar.", "Participle phrase 'striking face and hands'; past verb 'fired'."),
            ("I put on my spectacles to protect my eyes from their blinding missiles.", "Gözlerimi onların kör edici oklarından korumak için gözlüklerimi taktım.", "Infinitive of purpose 'to protect eyes'; compound noun 'blinding missiles'."),
            ("Taking my pocket-knife, I cut the anchor cables of fifty large warships.", "Çakımı alarak elli büyük savaş gemisinin çapa halatlarını kestim.", "Participle clause 'Taking pocket-knife'; past verb 'cut'."),
            ("I took the knotted cord in my hand and began to pull the armada through the water.", "Düğümlü urganı elime aldım ve donanmayı suyun içinden çekmeye başladım.", "Coordinate past verbs 'took and began'; infinitive 'to pull'."),
            ("The entire fleet of Blefuscu followed behind me like ducklings behind a mother swan.", "Bütün Blefuscu donanması bir anne kuğunun ardından giden ördek yavruları gibi peşimden geldi.", "Simile 'like ducklings behind a swan'; past verb 'followed'."),
            ("I arrived at the royal port of Lilliput, shouting: 'Long live the Emperor of Lilliput!'", "Lilliput'un kraliyet limanına ulaştım ve haykırdım: 'Çok yaşa Lilliput İmparatoru!'", "Participle phrase 'shouting'; proper royal acclamation."),
            ("The Emperor created me a Nardac on the spot, the highest title of honor in the realm.", "İmparator beni oracıkta ülkedeki en yüksek onur unvanı olan Nardac ilan etti.", "Appositive definition 'highest title of honor'; idiom 'on the spot'.")
        ]
    },
    # Page 6: The Palace Fire and Royal Ingratitude
    {
        "page_number": 6,
        "title": "The Fire and the Ingratitude",
        "vocab": [
            ("palace", "saray"),
            ("fire", "yangın"),
            ("extinguish", "söndürmek"),
            ("empress", "imparatoriçe"),
            ("ingratitude", "nankörlük"),
            ("treason", "vatana ihanet"),
            ("impeach", "suçlamak, yargılamak"),
            ("envy", "haset, kıskançlık")
        ],
        "sentences": [
            ("The Emperor's ambition grew boundless after my glorious naval conquest.", "Şanlı deniz zaferimden sonra İmparator'un hırsı sınır tanımaz bir hal aldı.", "Copular verb 'grew boundless'; adjective 'naval conquest'."),
            ("He desired to reduce Blefuscu into a mere province governed by a viceroy.", "Blefuscu'yu bir vali tarafından yönetilen sıradan bir eyalete indirgemeyi arzuladı.", "Passive participle modifier 'governed by a viceroy'; infinitive 'to reduce'."),
            ("He demanded that I destroy all the Big-Endian exiles and force everyone to break eggs at the small end.", "Büyük Uçlu tüm sürgünleri yok etmemi ve herkesi yumurtayı küçük uçtan kırmaya zorlamamı talep etti.", "Subjunctive coordinate clauses 'destroy and force'; past verb 'demanded'."),
            ("I flatly refused to be an instrument of enslaving a free and valiant people.", "Özgür ve cesur bir halkı köleleştirmenin bir aracı olmayı kesin bir dille reddettim.", "Verb + infinitive 'refused to be'; gerund phrase 'enslaving a people'."),
            ("My refusal provoked the Emperor's secret displeasure and the hatred of his ministers.", "Benim bu reddim İmparator'un gizli hoşnutsuzluğunu ve bakanlarının nefretini körükledi.", "Coordinate objects 'displeasure and hatred'; past verb 'provoked'."),
            ("Flimnap the High Treasurer and Skyresh Bolgolam the Admiral began plotting my downfall.", "Maliye Bakanı Flimnap ile Amiral Skyresh Bolgolam benim çöküşümü planlamaya başladılar.", "Coordinate subjects; verb + gerund 'began plotting'."),
            ("One midnight, I was awakened by the terrified screams of thousands of citizens.", "Bir gece yarısı binlerce yurttaşın dehşet dolu çığlıklarıyla uyandırıldım.", "Passive voice 'was awakened by'; adjective 'terrified screams'."),
            ("The royal palace was in flames, ignited by the carelessness of a maid of honor.", "Kraliyet sarayı bir nedimenin dikkatsizliği yüzünden alevler içinde yanıyordu.", "Passive participle 'ignited by carelessness'; prepositional phrase 'in flames'."),
            ("The Empress's apartment was burning furiously, and their tiny ladders were useless.", "İmparatoriçe'nin dairesi şiddetle yanıyordu ve onların minik merdivenleri hiçbir işe yaramıyordu.", "Coordinate clauses; adjective 'useless'."),
            ("No water buckets could quench the leaping fire threatening the magnificent building.", "Görkemli binayı tehdit eden sıçrayan ateşi hiçbir su kovası söndüremiyordu.", "Negative subject 'No water buckets'; modal 'could quench'."),
            ("I came up to the courtyard and quickly devised an unorthodox method to save the palace.", "Avluya geldim ve sarayı kurtarmak için hızla alışılmadık bir yöntem tasarladım.", "Coordinate past verbs 'came up and devised'; adjective 'unorthodox'."),
            ("Having consumed enormous quantities of wine that evening, I relieved myself upon the flames.", "O akşam muazzam miktarda şarap tüketmiş olduğumdan, alevlerin üzerine işeyiverdim.", "Perfect participle clause 'Having consumed'; euphemistic past 'relieved myself'."),
            ("In three minutes, the fire was totally extinguished, and the rest of the palace was saved.", "Üç dakika içinde yangın tamamen söndürüldü ve sarayın geri kalanı kurtarıldı.", "Coordinate passive clauses 'was extinguished and was saved'."),
            ("However, by the fundamental laws of Lilliput, it was high treason to urinate in the royal precincts.", "Ancak Lilliput'un temel kanunlarına göre kraliyet sınırları içinde küçük abdest bozmak vatana ihanetti.", "Dummy subject 'it was high treason to urinate'; prepositional phrase."),
            ("The Empress was disgusted by my act and vowed never to inhabit those rooms again.", "İmparatoriçe benim bu eylemimden iğrendi ve bir daha o odalarda asla oturmamaya ant içti.", "Passive coordinate 'was disgusted and vowed'; negative infinitive 'never to inhabit'."),
            ("Articles of impeachment were secretly drawn up against me for high treason.", "Vatana ihanet suçlamasıyla aleyhimde gizlice azil maddeleri hazırlandı.", "Passive voice 'were drawn up'; prepositional phrase 'against me'."),
            ("My crimes included extinguishing the fire unlawfully and refusing to subjugate Blefuscu.", "Suçlarım arasında yangını kanunsuz söndürmek ve Blefuscu'yu boyunduruk altına almayı reddetmek vardı.", "List of gerund phrases as predicate nominatives."),
            ("The Emperor and his council debated whether to poison me, starve me, or put out my eyes.", "İmparator ve meclisi beni zehirlemeyi mi, aç bırakmayı mı yoksa gözlerimi oymayı mı tartıştı.", "Indirect question with 'whether to... or'; series of infinitives."),
            ("A faithful courtier slipped out at night and delivered a secret warning to my lodging.", "Sadık bir saray mensubu gece gizlice dışarı süzüldü ve kaldığım yere gizli bir uyarı getirdi.", "Coordinate past verbs 'slipped out and delivered'; compound noun 'secret warning'."),
            ("I realized that even royal gratitude turns swiftly to venomous malice in small minds.", "Küçük zihinlerde kraliyet minnettarlığının bile hızla zehirli bir hınca dönüştüğünü anladım.", "Noun clause 'that gratitude turns to malice'; adverb 'swiftly'.")
        ]
    },
    # Page 7: Escape from Lilliput
    {
        "page_number": 7,
        "title": "Escape from the Pygmy Realm",
        "vocab": [
            ("escape", "kaçmak, kurtulmak"),
            ("harbor", "liman"),
            ("boat", "tekne, sandal"),
            ("drift", "akıntıyla sürüklenmek"),
            ("pardon", "bağışlama"),
            ("homeward", "eve doğru"),
            ("merchant", "tüccar"),
            ("cattle", "sığır, büyükbaş")
        ],
        "sentences": [
            ("Knowing that my eyes were to be put out within days, I resolved to escape immediately.", "Birkaç gün içinde gözlerimin oyulacağını bilerek, derhal kaçmaya karar verdim.", "Participle clause of knowledge; passive periphrastic 'were to be put out'."),
            ("I walked to the coast, stepped into the channel, and waded across to Blefuscu.", "Kıyıya yürüdüm, boğaza adım attım ve yürüyerek Blefuscu'ya geçtim.", "Series of coordinated past action verbs."),
            ("The Emperor of Blefuscu, his royal family, and his court welcomed me with genuine honor.", "Blefuscu İmparatoru, kraliyet ailesi ve sarayı beni gerçek bir onurla karşıladılar.", "Compound subject; prepositional phrase 'with genuine honor'."),
            ("Three days after my arrival, I noticed a strange dark object floating out at sea.", "Gelişimden üç gün sonra denizde uzakta yüzen garip koyu renkli bir nesne fark ettim.", "Time phrase; perception verb 'noticed' + participle 'floating'."),
            ("I waded out and discovered a real, full-sized overturned ship's boat drifting ashore.", "Suda ilerledim ve kıyıya doğru sürüklenen gerçek, tam boy devrilmiş bir gemi filikası keşfettim.", "Coordinate past verbs 'waded and discovered'; compound adjective 'full-sized'."),
            ("With the help of twenty Blefuscudian ships and three thousand sailors, we towed it to port.", "Yirmi Blefuscu gemisi ve üç bin denizcinin yardımıyla onu limana çektik.", "Prepositional phrase of means; past verb 'towed'."),
            ("It had suffered very little damage and was capable of carrying me across the open ocean.", "Çok az hasar görmüştü ve beni açık okyanus boyunca taşımaya muktedirdi.", "Past perfect coordinate with simple past; adjective 'capable of carrying'."),
            ("The Emperor of Lilliput sent a furious envoy demanding that I be returned bound in chains.", "Lilliput İmparatoru zincirlere bağlanmış halde iade edilmemi talep eden öfkeli bir elçi gönderdi.", "Participle phrase with subjunctive 'that I be returned'; past verb 'sent'."),
            ("The generous monarch of Blefuscu politely refused, offering me protection and asylum.", "Blefuscu'nun cömert hükümdarı bana koruma ve sığınma teklif ederek bunu kibarca reddetti.", "Coordinate participles describing diplomatic refusal; adverb 'politely'."),
            ("I spent a month repairing the boat, fitting it with sails made of thirteen folds of linen.", "Tekneyi onarmakla, ona on üç kat ketenden yapılmış yelkenler takmakla bir ay geçirdim.", "Expression 'spent a month doing'; past participle modifier 'made of linen'."),
            ("The Emperor supplied me with the carcasses of one hundred oxen and three hundred sheep.", "İmparator bana yüz öküz ve üç yüz koyun karkası temin etti.", "Prepositional phrase 'with carcasses of oxen'; past verb 'supplied'."),
            ("He gave me fifty bags of gold coins and his own miniature portrait as a parting gift.", "Bana elli torba altın sikke ve bir veda hediyesi olarak kendi minyatür portresini verdi.", "Double object past verb 'gave'; compound noun 'parting gift'."),
            ("I placed six live cows and two live bulls in my pockets to show to my countrymen.", "Vatandaşlarıma göstermek için ceplerime altı canlı inek ve iki canlı boğa koydum.", "Infinitive of purpose 'to show to countrymen'; numeral objects."),
            ("On September 24, 1701, I set sail from Blefuscu, heading homeward into the boundless sea.", "24 Eylül 1701'de uçsuz bucaksız denizin içine, eve doğru yönelerek Blefuscu'dan yelken açtım.", "Participle phrase 'heading homeward'; date phrase."),
            ("On the third day of my voyage, I sighted a sail on the horizon and hoisted my signal flag.", "Yolculuğumun üçüncü gününde ufukta bir yelken gördüm ve işaret bayrağımı çektim.", "Coordinate past verbs 'sighted and hoisted'; time phrase."),
            ("It was an English merchant ship returning from Japan, commanded by Captain John Biddle.", "Kaptan John Biddle'ın komutasında Japonya'dan dönmekte olan bir İngiliz ticaret gemisiydi.", "Participle clause 'returning from Japan'; passive participle modifier 'commanded by'."),
            ("The sailors took me aboard, astonished beyond words by my miniature cattle and sheep.", "Denizciler beni gemiye aldılar; minyatür sığırlarım ve koyunlarım karşısında dilleri tutuldu.", "Passive participle modifier 'astonished beyond words'; past verb 'took aboard'."),
            ("They thought I was raving mad until I produced the tiny living beasts from my pocket.", "Cebimden o minik canlı hayvanları çıkarana kadar aklımı kaçırmış bir deli olduğumu sandılar.", "Time clause with 'until'; past continuous 'was raving mad'."),
            ("I arrived safely in England in April 1702, returning to the open arms of my family.", "Nisan 1702'de ailemin kucağına dönerek İngiltere'ye sağ salim vardım.", "Participle phrase 'returning to open arms'; adverb 'safely'."),
            ("Yet my restless wandering spirit could not long endure the quiet shores of home.", "Fakat benim huzursuz, gezgin ruhum evin sakin kıyılarına uzun süre dayanamadı.", "Adjective pair 'restless wandering'; modal negative 'could not long endure'.")
        ]
    },
    # Page 8: The Great Voyage to Brobdingnag
    {
        "page_number": 8,
        "title": "Brobdingnag: The Giant Continent",
        "vocab": [
            ("giant", "dev"),
            ("monstrous", "devasa, canavarca"),
            ("reaper", "orakçı, ekin biçici"),
            ("corn", "mısır, buğday"),
            ("scythe", "tırpan"),
            ("stride", "büyük adım / adımlamak"),
            ("tremble", "titremek"),
            ("farmer", "çiftçi")
        ],
        "sentences": [
            ("Having stayed only two months with my wife and children, I sailed again on the Adventure.", "Karım ve çocuklarımla sadece iki ay kaldıktan sonra Adventure gemisiyle yeniden denize açıldım.", "Perfect participle clause 'Having stayed'; past verb 'sailed'."),
            ("A violent tempest drove our vessel thousands of leagues off course into the great Pacific.", "Şiddetli bir fırtına gemimizi rotasından binlerce fersah öteye, büyük Pasifik'e sürükledi.", "Measurement phrase 'thousands of leagues'; past verb 'drove'."),
            ("We anchored near a strange, rocky continent to search for fresh drinking water.", "Taze içme suyu aramak için yabancı, kayalık bir kıtanın yakınına demir attık.", "Infinitive of purpose 'to search for water'; past verb 'anchored'."),
            ("I wandered inland alone, admiring the barren crags and towering cliffs of the shore.", "Kıyının çıplak kayalıklarına ve heybetli falezlerine hayran kalarak iç kısımlara tek başıma yürüdüm.", "Participle phrase 'admiring crags'; past verb 'wandered'."),
            ("Returning to the beach, I saw our rowboat fleeing in panic toward the ship.", "Kumsala döndüğümde filikamızın panik içinde gemiye doğru kaçtığını gördüm.", "Participle phrase 'Returning to beach'; perception verb 'saw fleeing'."),
            ("Wading after them through the ocean waves was an enormous creature of monstrous size.", "Okyanus dalgaları arasından onların peşinden suda ilerleyen şey devasa boyutlarda dev bir yaratıktı.", "Inverted locative sentence; participle 'Wading after them'."),
            ("He took strides as tall as church spires, but could not overtake the speeding rowboat.", "Kilise kuleleri kadar yüksek adımlar atıyordu fakat hızla uzaklaşan filikaya yetişemedi.", "Simile 'as tall as church spires'; coordinate clauses with 'but'."),
            ("Terrified, I turned and ran inland as fast as my trembling legs could carry me.", "Dehşete kapılmış halde arkamı döndüm ve titreyen bacaklarımın beni taşıyabildiği kadar hızlı iç kısımlara kaçtım.", "Idiom 'as fast as legs could carry'; past verbs 'turned and ran'."),
            ("I climbed a steep hill and found myself in a vast field of barley forty feet high.", "Dik bir tepeye tırmandım ve kendimi on iki metre yüksekliğinde arpalardan oluşan devasa bir tarlada buldum.", "Reflexive 'found myself'; measurement 'forty feet high'."),
            ("The field was bounded by hedges at least one hundred and twenty feet tall.", "Tarla en az otuz altı metre yüksekliğinde çitlerle çevriliydi.", "Passive voice 'was bounded by'; measurement phrase."),
            ("I came to a stile with four steps, each step six feet high and made of stone.", "Her basamağı iki metre yüksekliğinde ve taştan yapılmış dört basamaklı bir çit merdivenine geldim.", "Absolute description 'each step six feet high'; past verb 'came to'."),
            ("Seven monstrous giants entered the field, armed with scythes as long as six lances.", "Altı mızrak uzunluğunda tırpanlarla kuşanmış yedi devasa dev tarlaya girdi.", "Passive participle modifier 'armed with scythes'; numeral 'Seven giants'."),
            ("They began to reap the corn, advancing toward the spot where I lay hidden.", "Benim saklandığım noktaya doğru ilerleyerek ekinleri biçmeye başladılar.", "Verb + infinitive 'began to reap'; relative clause 'where I lay hidden'."),
            ("One giant reaper approached within ten yards of my hiding place, foot raised high.", "Dev bir orakçı ayağı havaya kalkmış halde saklandığım yerin dokuz metre yakınına kadar yaklaştı.", "Absolute phrase 'foot raised high'; past verb 'approached'."),
            ("Fearing that his next monstrous step would crush me to pieces, I screamed in terror.", "Bir sonraki canavarca adımının beni paramparça edeceğinden korkarak dehşet içinde çığlık attım.", "Participle clause of fear; result phrase 'crush to pieces'."),
            ("The giant stopped, looked down, and spotted me trembling upon the ground.", "Dev durdu, aşağı baktı ve beni yerde titrerken fark etti.", "Series of coordinate past verbs; perception verb 'spotted me trembling'."),
            ("He picked me up very carefully between his forefinger and thumb, inspecting me in wonder.", "Beni hayretle inceleyerek işaret parmağı ile başparmağı arasında çok dikkatlice kaldırdı.", "Participle phrase 'inspecting me in wonder'; phrasal verb 'picked up'."),
            ("I was sixty feet high in the air, dangling like a tiny mouse before his huge eyes.", "Havada on sekiz metre yüksekteydim, onun koca gözleri önünde minik bir fare gibi sallanıyordum.", "Simile 'like a tiny mouse'; measurement phrase 'sixty feet high'."),
            ("I clasped my hands together in supplication, speaking words of humble submission.", "Alçakgönüllü bir teslimiyetin sözlerini söyleyerek ellerimi yalvarışla birbirine kenetledim.", "Participle phrase 'speaking words'; past verb 'clasped'."),
            ("The giant seemed pleased with my voice and placed me gently inside his pocket.", "Dev sesimden memnun kalmış göründü ve beni nazikçe cebinin içine koydu.", "Coordinate past predicates; adjective 'pleased with'.")
        ]
    },
    # Page 9: Glumdalclitch and the Little Nurse
    {
        "page_number": 9,
        "title": "My Little Nurse Glumdalclitch",
        "vocab": [
            ("nurse", "bakıcı"),
            ("cradle", "beşik"),
            ("linen", "keten giysi"),
            ("cat", "kedi"),
            ("purr", "mırıldamak (kedi)"),
            ("gentle", "şefkatli, nazik"),
            ("mischief", "yaramazlık"),
            ("master", "efendi")
        ],
        "sentences": [
            ("The giant farmer carried me home to his farmhouse and placed me on the dinner table.", "Dev çiftçi beni çiftlik evine taşıdı ve yemek masasının üzerine koydu.", "Coordinate past verbs 'carried and placed'; compound noun 'dinner table'."),
            ("His wife shrieked and ran back, terrified as if I were a poisonous toad.", "Karısı çığlık attı ve sanki zehirli bir kara kurbağasıymışım gibi dehşete düşerek geri kaçtı.", "Subjunctive comparison 'as if I were'; coordinate past verbs 'shrieked and ran'."),
            ("Seeing how politely I bowed and spoke, she soon grew fond of me.", "Ne kadar kibarca eğilip konuştuğumu görünce çok geçmeden benden hoşlanmaya başladı.", "Participle clause of perception; idiom 'grew fond of'."),
            ("The farmer's nine-year-old daughter became my special caretaker and protector.", "Çiftçinin dokuz yaşındaki kızı benim özel bakıcım ve koruyucum oldu.", "Compound adjective 'nine-year-old'; coordinate predicate nouns."),
            ("Her name was Glumdalclitch, which in their language meant 'little nurse.'", "Adı Glumdalclitch idi; bu onların dilinde 'küçük bakıcı' anlamına geliyordu.", "Relative clause with past verb; appositive meaning."),
            ("She was exceedingly good-natured, gentle, and barely forty feet tall for her age.", "Son derece iyi huylu, nazik ve yaşına göre ancak on iki metre boyundaydı.", "Coordinate predicate adjectives; measurement phrase 'forty feet tall'."),
            ("She fitted up a doll's cradle with soft blankets and placed me inside to sleep.", "Yumuşak battaniyelerle bir oyuncak bebek beşiğini donattı ve uyumam için beni içine koydu.", "Phrasal verb 'fitted up'; infinitive of purpose 'to sleep'."),
            ("She sewed tiny shirts and coats for me out of fine Brobdingnagian linen.", "İnce Brobdingnag keteninden benim için minik gömlekler ve ceketler dikti.", "Prepositional phrase 'out of fine linen'; past verb 'sewed'."),
            ("She taught me their language patiently, pointing at objects and speaking clearly.", "Nesneleri gösterip net bir şekilde konuşarak bana dillerini sabırla öğretti.", "Coordinate participles 'pointing and speaking'; adverb 'patiently'."),
            ("In the house, I faced many terrifying perils that amused the giant family.", "Evde, dev aileyi eğlendiren pek çok dehşet verici tehlikeyle yüz yüze geldim.", "Relative clause 'that amused the family'; past verb 'faced'."),
            ("A giant house cat leaped onto the table, purring with a roar like twenty watermills.", "Dev bir ev kedisi masaya atladı, yirmi su değirmeni gibi bir kükremeyle mırıldanarak.", "Simile 'like twenty watermills'; participle phrase 'purring with a roar'."),
            ("I drew my hanger and stood firm, which prevented the monster from attacking me.", "Kılıcımı çektim ve dimdik durdum; bu durum canavarın bana saldırmasını engelledi.", "Relative clause of result 'which prevented attacking'; past verbs 'drew and stood'."),
            ("The farmer's infant baby seized me by the waist and popped my head into his mouth.", "Çiftçinin henüz bebek olan çocuğu beni belimden yakaladı ve kafamı ağzının içine soktu.", "Coordinate past verbs 'seized and popped'; prepositional phrase 'by the waist'."),
            ("I roared so loudly that the frightened baby dropped me safely into Glumdalclitch's apron.", "O kadar yüksek sesle kükredim ki korkan bebek beni sağ salim Glumdalclitch'in önlüğüne düşürdü.", "Result clause 'so loudly that'; adverb 'safely'."),
            ("Huge rats the size of mastiffs attacked me, but I killed one with my sword.", "Danua köpeği büyüklüğündeki dev fareler bana saldırdı fakat birini kılıcımla öldürdüm.", "Noun phrase of comparison 'size of mastiffs'; past verb 'killed'."),
            ("Glumdalclitch washed my clothes, brushed my hair, and defended me from every danger.", "Glumdalclitch giysilerimi yıkadı, saçlarımı taradı ve beni her tehlikeden korudu.", "Series of coordinated past action verbs showing devotion."),
            ("Her father, however, saw in me only a lucrative spectacle to make money.", "Ancak babası bende para kazanmak için sadece karlı bir gösteri malzemesi gördü.", "Adjective 'lucrative spectacle'; infinitive of purpose 'to make money'."),
            ("He decided to carry me across the kingdom and exhibit me to paying crowds.", "Beni krallığın dört bir yanına taşıyıp para ödeyen kalabalıklara sergilemeye karar verdi.", "Coordinate infinitives 'to carry and exhibit'; past verb 'decided'."),
            ("Glumdalclitch wept bitterly, fearing that the hard travel would kill her little pet.", "Glumdalclitch zorlu yolculuğun minik evcil hayvanını öldüreceğinden korkarak acı acı ağladı.", "Participle clause of fear; adverb 'bitterly'."),
            ("Thus began my exhausting career as a traveling wonder of the giant realm.", "Böylece devler ülkesinin gezgin bir harikası olarak yorucu kariyerim başlamış oldu.", "Prepositional phrase 'as a traveling wonder'; past verb 'began'.")
        ]
    },
    # Page 10: Exhibited across the Giant Realm
    {
        "page_number": 10,
        "title": "The Wonder of the Realm",
        "vocab": [
            ("spectacle", "gösteri, temaşa"),
            ("fatigue", "yorgunluk, bitkinlik"),
            ("queen", "kraliçe"),
            ("purchase", "satın almak"),
            ("dwarf", "cüce"),
            ("mischief", "yaramazlık, muziplik"),
            ("box", "özel kutu/oda"),
            ("splendor", "ihtişam")
        ],
        "sentences": [
            ("My master carried me to eighteen towns, forcing me to perform ten times a day.", "Efendim beni günde on kez gösteri yapmaya zorlayarak on sekiz kasabaya taşıdı.", "Participle phrase 'forcing me to perform'; prepositional phrases."),
            ("I was made to march on tables, flourish my sword, and drink toasts to the spectators.", "Masa üzerinde yürümeye, kılıcımı sallamaya ve seyircilere kadeh kaldırmaya mecbur bırakıldım.", "Passive infinitive series 'was made to march, flourish, drink'."),
            ("Thousands of giants crowded around, paying high fees to see the tiny creature.", "Binlerce dev minik yaratığı görmek için yüksek ücretler ödeyerek etrafıma üşüştü.", "Participle phrase 'paying high fees'; infinitive of purpose 'to see'."),
            ("The unending labor and constant travel wore down my health until I was reduced to skin and bones.", "Bitmek bilmez çalışma ve sürekli yolculuk bir deri bir kemik kalana kadar sağlığımı yıprattı.", "Time clause with 'until'; idiom 'reduced to skin and bones'."),
            ("My master believed I would die soon and resolved to sell me for whatever he could get.", "Efendim yakında öleceğimi düşündü ve ne koparabilirse beni satmaya karar verdi.", "Coordinate past verbs 'believed and resolved'; noun clause."),
            ("The Queen of Brobdingnag heard of me and commanded that I be brought to the royal court.", "Brobdingnag Kraliçesi beni duydu ve kraliyet sarayına getirilmemi emretti.", "Subjunctive passive clause 'that I be brought'; past verb 'commanded'."),
            ("Her Majesty was so captivated by my speech and manners that she purchased me for a thousand gold pieces.", "Majesteleri konuşmamdan ve terbiyemden öyle büyülendi ki beni bin altın sikke karşılığında satın aldı.", "Result clause 'so captivated that'; prepositional phrase 'for gold pieces'."),
            ("At my earnest request, Glumdalclitch was retained as my official nurse at court.", "Benim samimi ricam üzerine Glumdalclitch sarayda resmi bakıcım olarak alıkonuldu.", "Passive voice 'was retained as nurse'; prepositional phrase 'At earnest request'."),
            ("The Queen had a luxurious traveling box built for me by her master cabinet-maker.", "Kraliçe usta marangozuna benim için lüks bir seyahat kutusu inşa ettirdi.", "Causative structure 'had a box built'; compound noun 'cabinet-maker'."),
            ("It was sixteen feet square and twelve feet high, with sash windows, two beds, and soft chairs.", "On altı fit kare tabanlı ve on iki fit yüksekliğindeydi; kanatlı pencereleri, iki yatağı ve yumuşak sandalyeleri vardı.", "Measurement descriptions; prepositional phrase 'with sash windows'."),
            ("I was placed on the Queen's dining table every day, conversing with the royal family.", "Her gün kraliyet ailesiyle sohbet ederek Kraliçe'nin yemek masasına konuldum.", "Participle phrase 'conversing with family'; passive voice 'was placed'."),
            ("The Queen's dwarf, who was thirty feet tall, hated me out of spiteful jealousy.", "Dokuz metre boyundaki Kraliçe'nin cücesi kindar bir kıskançlıkla benden nefret ediyordu.", "Relative clause 'who was thirty feet tall'; prepositional phrase 'out of jealousy'."),
            ("He constantly played dangerous practical jokes upon my tiny defenseless person.", "Benim minik ve savunmasız şahsıma sürekli tehlikeli eşek şakaları yapıyordu.", "Adverb 'constantly'; noun phrase 'dangerous practical jokes'."),
            ("Once he shook an apple tree over me, dropping an apple as large as a barrel on my back.", "Bir keresinde sırtıma fıçı büyüklüğünde bir elma düşürerek üzerime bir elma ağacını silkeledi.", "Participle phrase 'dropping an apple'; simile 'as large as a barrel'."),
            ("Another time, the malicious dwarf dumped me into a bowl of thick sweet cream.", "Başka bir zaman o hain cüce beni koyu tatlı krema dolu bir kasenin içine boca etti.", "Transitive past 'dumped into'; adjective 'malicious'."),
            ("I was almost drowned before good Glumdalclitch rushed in and fished me out.", "İyi kalpli Glumdalclitch içeri koşup beni dışarı çekmeden önce neredeyse boğuluyordum.", "Passive 'was almost drowned'; time clause with 'before'."),
            ("A monkey once snatched me from my box and carried me to the palace roof.", "Bir maymun bir keresinde beni kutumdan kapıp sarayın çatısına kadar taşıdı.", "Coordinate past verbs 'snatched and carried'; prepositional phrase."),
            ("He stuffed food down my mouth as if I were his young cub, until soldiers rescued me.", "Askerler beni kurtarana kadar sanki kendi yavrusuymuşum gibi ağzımdan içeri yemek tıkıştırdı.", "Subjunctive comparison 'as if I were cub'; time clause with 'until'."),
            ("Despite these hilarious and terrifying perils, I enjoyed the royal favor of the court.", "Bu neşeli ve dehşet verici tehlikelere rağmen sarayın kraliyet iltifatlarının tadını çıkardım.", "Preposition 'despite'; noun phrase 'royal favor'."),
            ("The King took great pleasure in conversing with me about the government of Europe.", "Kral benimle Avrupa'nın hükümet idaresi üzerine sohbet etmekten büyük zevk aldı.", "Idiom 'took great pleasure in'; gerund phrase 'conversing with me'.")
        ]
    },
    # Page 11: Conversations with the Giant King
    {
        "page_number": 11,
        "title": "The Wisdom of the Giant King",
        "vocab": [
            ("monarch", "hükümdar"),
            ("philosophy", "felsefe"),
            ("gunpowder", "barut"),
            ("cannon", "top, batarya"),
            ("parliament", "parlamento"),
            ("virtue", "erdem, fazilet"),
            ("vermin", "haşarat, zararlı yaratık"),
            ("contempt", "küçümseme, hor görme")
        ],
        "sentences": [
            ("The King of Brobdingnag was a wise philosopher-king who loved justice and peace.", "Brobdingnag Kralı adaleti ve barışı seven bilge bir filozof-kraldı.", "Relative clause 'who loved justice'; compound title 'philosopher-king'."),
            ("He ordered me to give him an exact account of the laws, politics, and customs of England.", "İngiltere'nin kanunları, siyaseti ve adetlerine dair ona eksiksiz bir hesap vermemi emretti.", "Verb + object + infinitive 'ordered me to give'; compound noun 'exact account'."),
            ("I described our glorious Parliament, our courts of justice, and our vast national treasury.", "Şanlı Parlamentomuzu, adalet mahkemelerimizi ve devasa ulusal hazinemizi anlattım.", "Series of direct objects with possessive pronouns; past verb 'described'."),
            ("I spoke proudly of our great military victories, our fleets, and our religious factions.", "Büyük askeri zaferlerimizden, donanmalarımızdan ve dini hiziplerimizden gururla bahsettim.", "Adverb 'proudly'; prepositional series 'of victories, fleets, factions'."),
            ("The King listened with grave attention, writing notes in his pocketbook.", "Kral cebindeki deftere notlar yazarak ağırbaşlı bir dikkatle dinledi.", "Participle phrase 'writing notes'; prepositional phrase 'with grave attention'."),
            ("When I finished my boastful discourse, the King asked a series of penetrating questions.", "Övüngen söylevimi bitirdiğimde Kral bir dizi can alıcı soru sordu.", "Time clause with 'finished'; adjective 'penetrating questions'."),
            ("He asked how our lawmakers were chosen and whether money decided political elections.", "Yasa yapıcılarımızın nasıl seçildiğini ve siyasi seçimleri paranın belirleyip belirlemediğini sordu.", "Indirect questions 'how were chosen' and 'whether money decided'."),
            ("He inquired why our courts of law took decades to decide simple commercial disputes.", "Basit ticari anlaşmazlıkları karara bağlamanın neden mahkemelerimizde on yıllar sürdüğünü sordu.", "Indirect question with 'why'; measurement 'took decades'."),
            ("He wondered why we needed standing armies if we were genuinely peaceful people.", "Eğer gerçekten barışçıl insanlarsak neden daimi ordulara ihtiyaç duyduğumuzu merak etti.", "Conditional clause 'if we were peaceful'; compound noun 'standing armies'."),
            ("I offered to teach him the secret formula of gunpowder to win his royal favor.", "Onun kraliyet lütfunu kazanmak için barutun gizli formülünü ona öğretmeyi teklif ettim.", "Infinitive of purpose 'to win favor'; compound noun 'gunpowder'."),
            ("I explained how a small quantity of black dust could blow up whole cities into the air.", "Küçük bir miktar kara tozun bütün şehirleri havaya nasıl uçurabileceğini açıkladı.", "Indirect question clause 'how dust could blow up cities'; modal 'could blow up'."),
            ("I described how cannons could shatter ships and tear thousands of men to pieces.", "Topların gemileri nasıl parçalayabileceğini ve binlerce insanı nasıl lime lime edebileceğini anlattım.", "Coordinate verb phrases; modal 'could shatter and tear'."),
            ("The King was struck with utter horror and disgust at my monstrous proposal.", "Kral benim bu canavarca teklifim karşısında tam bir dehşet ve tiksintiyle sarsıldı.", "Passive voice 'was struck with horror'; prepositional phrase 'at proposal'."),
            ("He commanded me on pain of death never to mention that murderous secret again.", "Ölüm cezası tehdidiyle o kanlı sırrı bir daha asla anmamamı bana emretti.", "Prepositional phrase 'on pain of death'; negative infinitive 'never to mention'."),
            ("He marveled that so diminutive an insect could harbor such bloodthirsty thoughts.", "Bu kadar ufak tefek bir böceğin böylesine kana susamış düşünceler besleyebilmesine hayret etti.", "Noun clause with 'that so diminutive an insect could harbor'; adjective 'bloodthirsty'."),
            ("He picked me up gently in his vast hand and stroked my head sorrowfully.", "Geniş elinin içinde beni nazikçe kaldırdı ve kederle başımı okşadı.", "Coordinate past verbs 'picked up and stroked'; adverb 'sorrowfully'."),
            ("'My little friend,' said the King, 'thy people seem to be the most pernicious race of vermin.'", "'Benim minik dostum,' dedi Kral, 'senin halkın yeryüzündeki en zararlı haşarat ırkı gibi görünüyor.'", "Superlative noun phrase 'most pernicious race of vermin'; direct address."),
            ("'Nature ever suffered to crawl upon the surface of the earth,' concluded the monarch.", "'Doğanın yeryüzünün üzerinde sürünmesine bugüne kadar katlandığı en zararlı yaratıklar,' diyerek sözünü bitirdi hükümdar.", "Philosophical indictment; past verb 'concluded'."),
            ("I felt deeply humiliated by his judgment, though I could not dispute his wisdom.", "Onun bilgeliğine itiraz edemesem de verdiği bu hüküm karşısında kendimi derinden aşağılanmış hissettim.", "Concession clause with 'though'; copular passive 'felt humiliated'."),
            ("A wider perspective of human folly had opened before my astonished eyes.", "Şaşkın gözlerimin önünde insan ahmaklığına dair daha geniş bir ufuk açılmıştı.", "Past perfect 'had opened'; compound noun 'human folly'.")
        ]
    },
    # Page 12: Carried by an Eagle
    {
        "page_number": 12,
        "title": "The Flight of the Traveling Box",
        "vocab": [
            ("box", "seyahat kutusu"),
            ("shore", "deniz kıyısı"),
            ("eagle", "kartal"),
            ("talon", "pençe"),
            ("beak", "gaga"),
            ("plummet", "hızla düşmek"),
            ("float", "suda yüzmek"),
            ("salvation", "kurtuluş")
        ],
        "sentences": [
            ("I had lived two years in Brobdingnag, longing constantly for my homeland and kindred.", "Brobdingnag'da vatanımın ve akrabalarımın hasretini sürekli çekerek iki yıl yaşamıştım.", "Past perfect 'had lived'; participle phrase 'longing constantly'."),
            ("The King and Queen took a journey to the south coast, taking Glumdalclitch and me along.", "Kral ve Kraliçe güney sahiline bir seyahate çıktılar, Glumdalclitch ile beni de yanlarına aldılar.", "Participle phrase 'taking Glumdalclitch and me along'; past verb 'took a journey'."),
            ("I was indisposed and asked to be carried down to the seashore for fresh ocean air.", "Rahatsızlandım ve taze okyanus havası almak için deniz kıyısına götürülmeyi istedim.", "Passive infinitive 'to be carried down'; purpose phrase 'for fresh air'."),
            ("A page boy carried my traveling box down to the rocks, where I lay on my hammock.", "Bir uşak çocuk seyahat kutumu kayalıklara indirdi; orada hamağımda uzandım.", "Relative clause 'where I lay on hammock'; past verb 'carried'."),
            ("The boy went off to hunt for birds' eggs, leaving my box unattended upon the shore.", "Çocuk kutumu kıyıda gözetimsiz bırakarak kuş yumurtaları avlamaya gitti.", "Participle phrase 'leaving box unattended'; phrasal verb 'went off to hunt'."),
            ("Suddenly, I felt a violent jerk that nearly flung me out of my bed.", "Birdenbire beni neredeyse yatağımdan fırlatacak şiddetli bir sarsıntı hissettim.", "Relative clause 'that nearly flung me'; adjective 'violent jerk'."),
            ("The box was lifted rapidly into the air, ascending with terrifying, dizzying speed.", "Kutu korkutucu, baş döndürücü bir hızla yükselerek hızla havaya kalktı.", "Passive voice 'was lifted'; coordinate participles 'ascending with speed'."),
            ("Looking through the sash window, I saw only clouds and boundless empty sky.", "Kanatlı pencereden bakınca sadece bulutları ve uçsuz bucaksız boş gökyüzünü gördüm.", "Participle clause 'Looking through window'; perception verb 'saw'."),
            ("A monstrous eagle had gripped the iron ring on top of my box in its gigantic talons.", "Devasa bir kartal kutumun üstündeki demir halkayı dev pençeleriyle kavramıştı.", "Past perfect 'had gripped'; prepositional phrase 'in gigantic talons'."),
            ("The bird was flying out to sea, intending to smash the box upon a rock and eat me.", "Kuş kutuyu bir kayaya vurup parçalamak ve beni yemek niyetiyle denize doğru uçuyordu.", "Participle phrase 'intending to smash'; past continuous 'was flying'."),
            ("Suddenly, a furious flapping sounded above, accompanied by loud screeching.", "Birdenbire yukarıdan gürültülü ciyaklamalar eşliğinde şiddetli bir kanat çırpma sesi duyuldu.", "Passive participle modifier 'accompanied by screeching'; past verb 'sounded'."),
            ("Two other giant eagles attacked my captor, fighting fiercely for possession of the prey.", "İki diğer dev kartal avın mülkiyeti için kıyasıya savaşarak beni kaçıran kuşa saldırdı.", "Participle phrase 'fighting fiercely'; past verb 'attacked'."),
            ("In the struggle, the eagle released the iron ring, and my box plummeted down.", "Boğuşma esnasında kartal demir halkayı bıraktı ve kutum dimdik aşağı düştü.", "Coordinate past clauses; past verb 'plummeted down'."),
            ("I fell thousands of feet through the air with a whistling rush that took my breath away.", "Nefesimi kesen bir ıslık uğultusuyla havada binlerce fit aşağı düştüm.", "Relative clause 'that took breath away'; past verb 'fell'."),
            ("Crash! The box struck the ocean with a tremendous splash and sank deep into the waves.", "Güm! Kutu muazzam bir şapırtıyla okyanusa çarptı ve dalgaların derinliklerine battı.", "Onomatopoeia; coordinate past verbs 'struck and sank'."),
            ("The water was kept out by tight joints, and the buoyant wooden box bobbed back to the surface.", "Sızdırmaz ek yerleri suyu dışarıda tuttu ve batmayan tahta kutu tekrar yüzeye fırladı.", "Passive voice 'was kept out'; coordinate clause 'box bobbed back'."),
            ("I floated helplessly for hours upon the solitary sea, expecting death at every swell.", "Her dalgada ölümü bekleyerek saatlerce kimsesiz denizin üzerinde çaresizce yüzdüm.", "Participle phrase 'expecting death'; adverb 'helplessly'."),
            ("Presently, I heard a grating sound against the side of the box and shouted in desperation.", "Çok geçmeden kutunun yanına sürtünen bir ses duydum ve çaresizlik içinde bağırdım.", "Coordinate past verbs 'heard and shouted'; participial adjective 'grating sound'."),
            ("An English merchant ship had spotted the strange floating house and sent a boat.", "Bir İngiliz ticaret gemisi bu garip yüzen evi fark etmiş ve bir sandal göndermişti.", "Coordinate past perfect verbs 'had spotted and sent'."),
            ("Carpenters sawed an opening, and I was pulled out into the arms of human sailors.", "Marangozlar bir delik açtılar ve ben insan denizcilerin kollarına çekilip kurtarıldım.", "Coordinate clauses; passive voice 'was pulled out'.")
        ]
    },
    # Page 13: The Flying Island of Laputa
    {
        "page_number": 13,
        "title": "Laputa: The Floating Island",
        "vocab": [
            ("floating", "yüzen, havada asılı duran"),
            ("magnet", "mıknatıs"),
            ("astronomy", "astronomi, gökbilim"),
            ("academy", "akademi"),
            ("speculation", "tefekkür, kurgu"),
            ("flapper", "uyarıcı değnekçi"),
            ("projector", "hayalperest mucit"),
            ("extract", "çıkarmak, özünü almak")
        ],
        "sentences": [
            ("My third voyage took me into the northern Pacific, where our ship was captured by pirates.", "Üçüncü yolculuğum beni gemimizin korsanlar tarafından ele geçirildiği kuzey Pasifik'e götürdü.", "Relative clause of place; passive voice 'was captured'."),
            ("The cruel pirates cast me adrift in a small canoe with paddle and minimal provisions.", "Zalim korsanlar beni bir kürek ve kıt erzakla küçük bir kano içinde denize salıverdiler.", "Idiom 'cast me adrift'; coordinate prepositional objects."),
            ("I landed upon a desolate rocky island and looked up to see a wondrous spectacle.", "Issız kayalık bir adaya çıktım ve harikulade bir gösteri görmek için yukarı baktım.", "Infinitive of purpose 'to see spectacle'; past verbs 'landed and looked'."),
            ("Floating in the sky above me was an inhabited island, circular and made of solid rock.", "Tepemdeki gökyüzünde yüzen şey, dairesel ve masif kayadan yapılmış meskun bir adaydı.", "Inverted locative sentence; passive participle 'made of solid rock'."),
            ("It moved through the air by means of a colossal lodestone or natural magnet in its center.", "Merkezindeki devasa bir manyetit taşı veya doğal mıknatıs vasıtasıyla havada hareket ediyordu.", "Prepositional phrase 'by means of'; compound noun 'colossal lodestone'."),
            ("The island, called Laputa, lowered a rope chair and hoisted me up into their aerial city.", "Laputa adı verilen ada bir halat sandalye indirdi ve beni gökteki şehirlerine yukarı çekti.", "Appositive participle 'called Laputa'; coordinate past verbs."),
            ("The inhabitants were obsessed with abstract geometry, mathematics, and musical theory.", "Ahalisi soyut geometri, matematik ve müzik teorisine kafayı takmıştı.", "Passive idiom 'were obsessed with'; coordinate noun objects."),
            ("Their heads were all inclined to the right or left, with one eye turned directly inward.", "Başlarının hepsi sağa veya sola eğikti; bir gözleri doğrudan içe dönüktü.", "Passive participle modifier 'turned directly inward'; predicate adjectives."),
            ("They were so lost in speculation that they required servants called 'flappers' to awaken them.", "Tefekkür içinde öyle kaybolmuşlardı ki kendilerini uyandırmak için 'şaplakçı' denilen hizmetkarlara muhtaçtılar.", "Result clause 'so lost that'; passive participle 'called flappers'."),
            ("The flapper carried a bladder on a stick filled with dried peas to strike their ears and mouths.", "Şaplakçı kulaklarına ve ağızlarına vurmak için bir sopanın ucunda kurutulmuş bezelyeyle dolu bir kese taşırdı.", "Infinitive of purpose 'to strike'; past participle modifier 'filled with peas'."),
            ("Without a flap on the mouth, a philosopher would forget to speak during conversation.", "Ağzına bir şaplak yemezse, bir filozof sohbet esnasında konuşmayı unutuverirdi.", "Prepositional phrase 'Without a flap'; conditional modal 'would forget'."),
            ("I was granted permission to descend to the terrestrial continent of Balnibarbi below.", "Aşağıdaki Balnibarbi kara kıtasına inmem için bana izin verildi.", "Passive voice 'was granted permission'; infinitive 'to descend'."),
            ("In the grand city of Lagado, I visited the world-famous Grand Academy of Projectors.", "Büyük Lagado şehrinde dünyaca meşhur Hayalperest Mucitler Büyük Akademisi'ni ziyaret ettim.", "Proper capitalized institution; past verb 'visited'."),
            ("Here, professors pursued completely absurd and useless scientific experiments.", "Burada profesörler tamamen saçma ve faydasız bilimsel deneylerin peşinden koşuyorlardı.", "Coordinate adjectives 'absurd and useless'; past verb 'pursued'."),
            ("One projector had spent eight years trying to extract sunbeams out of cucumbers.", "Bir mucit hıyarlardan güneş ışınları çıkarmaya çalışarak sekiz yılını harcamıştı.", "Past perfect continuous sense; infinitive 'to extract'."),
            ("Another was attempting to soften marble into cushions for comfortable chairs.", "Bir başkası rahat sandalyeler için mermeri yumuşatıp yastığa dönüştürmeye çabalıyordu.", "Past continuous 'was attempting'; infinitive 'to soften'."),
            ("A blind architect was designing a method for building houses from the roof downward.", "Kör bir mimar evleri çatıdan aşağıya doğru inşa etmek için bir yöntem tasarlıyordu.", "Compound directional phrase 'from roof downward'; past continuous 'was designing'."),
            ("Philosophers proposed abolishing all spoken words, communicating only by carrying bundles of objects.", "Filozoflar bütün konuşulan kelimeleri kaldırmayı, sadece nesne bohçaları taşıyarak anlaşmayı teklif ettiler.", "Coordinate gerunds 'abolishing and communicating'; manner phrase."),
            ("These intellectual follies had ruined the agriculture, commerce, and happiness of the people.", "Bu entelektüel ahmaklıklar halkın tarımını, ticaretini ve mutluluğunu mahvetmişti.", "Past perfect 'had ruined'; coordinate noun objects."),
            ("I departed from this misguided land, yearning for simple common sense and virtue.", "Basit sağduyunun ve erdemin hasretini çekerek bu yoldan çıkmış diyardan ayrıldım.", "Participle phrase 'yearning for common sense'; past verb 'departed'.")
        ]
    },
    # Page 14: The Land of the Houyhnhnms
    {
        "page_number": 14,
        "title": "The Land of the Houyhnhnms",
        "vocab": [
            ("virtue", "erdem, fazilet"),
            ("reason", "akıl, mantık"),
            ("noble", "asil, soylu"),
            ("steed", "küheylan, at"),
            ("savage", "vahşi yaratık"),
            ("degrade", "alçalmak, yozlaşmak"),
            ("filth", "pislik, murdarlık"),
            ("truth", "hakikat, doğruluk")
        ],
        "sentences": [
            ("On my fourth voyage as captain of the Adventurer, my mutinous crew marooned me ashore.", "Adventurer gemisinin kaptanı olarak dördüncü yolculuğumda, isyancı mürettebatım beni karaya terk etti.", "Prepositional phrase 'as captain'; past verb 'marooned'."),
            ("I walked inland into an idyllic, peaceful country with well-kept pastures and clean streams.", "Bakımlı otlakları ve temiz dereleri olan huzurlu, cennet gibi bir ülkenin iç kısımlarına yürüdüm.", "Compound adjectives 'well-kept, clean'; past verb 'walked inland'."),
            ("Presently, I encountered a herd of hideous, deformed, and disgusting beasts in a field.", "Çok geçmeden bir tarlada çirkin, deforme olmuş ve iğrenç hayvanlardan oluşan bir sürüyle karşılaştım.", "Series of coordinate adjectives; past verb 'encountered'."),
            ("They had human faces, hairy bodies, sharp claws, and behaved with unspeakable filth.", "İnsan yüzleri, kıllı gövdeleri, keskin pençeleri vardı ve tarif edilemez bir pislikle davranıyorlardı.", "Coordinate predicates; noun phrase 'unspeakable filth'."),
            ("To my horror, they surrounded me and leaped into trees, discharging filth upon my head.", "Dehşet içinde gördüm ki etrafımı sardılar ve kafama pislik saçarak ağaçlara tırmandılar.", "Coordinate past verbs; participle phrase 'discharging filth'."),
            ("Suddenly, a dapple-gray horse trotted into the glade with stately, dignified grace.", "Birdenbire kır bir at vakur ve asil bir zarafetle orman açıklığına doğru tırıs gitti.", "Prepositional phrase 'with dignified grace'; past verb 'trotted'."),
            ("The savage monsters scattered in instant terror at the approach of the noble steed.", "Vahşi canavarlar o soylu küheylanın yaklaşmasıyla anlık bir dehşet içinde darmadağın oldular.", "Prepositional phrase 'at approach of steed'; past verb 'scattered'."),
            ("The horse inspected me with calm curiosity, whinnying softly to a chestnut companion.", "At sakin bir merakla beni inceledi, kestane rengi bir yoldaşına usulca kişnedi.", "Coordinate participles; adverb 'softly'."),
            ("They were the Houyhnhnms, a race of rational horses governed purely by reason.", "Onlar Houyhnhnm'lerdi; tamamen akıl ve mantıkla yönetilen rasyonel atlar ırkı.", "Appositive clause; passive participle modifier 'governed purely by reason'."),
            ("The vile, brutish creatures I had encountered were the Yahoos, degraded human beasts.", "Karşılaştığım o alçak, kaba yaratıklar ise yozlaşmış insan hayvanları olan Yahoo'lardı.", "Appositive phrase 'degraded human beasts'; relative clause."),
            ("The dapple-gray master took me to his clean, order-filled home built of timber and thatch.", "Kır efendi beni kereste ve sazdan yapılmış temiz, düzen dolu evine götürdü.", "Past participle modifier 'built of timber'; past verb 'took'."),
            ("I lived among the Houyhnhnms for three glorious years, learning their harmonious language.", "Ahenkli dillerini öğrenerek üç şanlı yıl boyunca Houyhnhnm'ler arasında yaşadım.", "Participle phrase 'learning language'; duration phrase 'for three years'."),
            ("In their tongue, there was no word for 'lie' or 'falsehood', only 'the thing which was not.'", "Onların dilinde 'yalan' veya 'hile' kelimesi yoktu; sadece 'olmayan şey' tabiri vardı.", "Philosophical linguistic detail; negative existential 'there was no word'."),
            ("They knew no war, no crime, no jealousy, no disease, and no corrupt government.", "Ne savaşı, ne suçu, ne kıskançlığı, ne hastalığı, ne de yozlaşmış hükümetleri bilirlerdi.", "Parallel negative objects introduced by repeated 'no'."),
            ("They governed their lives by friendship, benevolence, truth, and temperance.", "Hayatlarını dostluk, iyilikseverlik, hakikat ve ölçülülükle idare ederlerdi.", "Preposition 'by' followed by four classical virtues."),
            ("When I described human wars, gunpowder, lawyers, and greed, my master stood appalled.", "İnsan savaşlarını, barutu, avukatları ve açgözlülüğü anlattığımda efendim dehşet içinde kaldı.", "Time clause with 'described'; predicate adjective 'stood appalled'."),
            ("He concluded that civilized humans were merely Yahoos with a dangerous gift of intellect.", "Medeni insanların sadece aklın tehlikeli bir yeteneğine sahip Yahoo'lar olduğu sonucuna vardı.", "Noun clause 'that humans were Yahoos'; past verb 'concluded'."),
            ("I felt deep shame for my own species and adored the noble virtue of the horses.", "Kendi türümden derin bir utanç duydum ve atların soylu erdemine hayran kaldım.", "Coordinate past verbs 'felt and adored'; noun phrase 'noble virtue'."),
            ("I desired nothing more than to spend the remainder of my earthly days among them.", "Dünyevi günlerimin geri kalanını onların arasında geçirmekten başka hiçbir şey arzulamazdım.", "Comparative structure 'nothing more than to spend'; noun 'remainder'."),
            ("A heavenly paradise of pure reason had banished every trace of human pride.", "Saf aklın cennet gibi diyarı, insan kibrinin her bir izini silip atmıştı.", "Past perfect 'had banished'; compound noun 'pure reason'.")
        ]
    },
    # Page 15: The Return to the World of Men
    {
        "page_number": 15,
        "title": "Return to the World of Men",
        "vocab": [
            ("expel", "kovmak, sınır dışı etmek"),
            ("assembly", "meclis, kurultay"),
            ("canoe", "kano"),
            ("homeland", "anavatan"),
            ("abhor", "nefret etmek, tiksinmek"),
            ("stable", "ahır"),
            ("groom", "at bakıcısı"),
            ("humility", "alçakgönüllülük")
        ],
        "sentences": [
            ("To my profound sorrow, the Grand Assembly of Houyhnhnms decreed my expulsion.", "Büyük kederimle birlikte, Houyhnhnm'lerin Büyük Meclisi benim sınır dışı edilmeme hükmetti.", "Prepositional phrase 'To profound sorrow'; past verb 'decreed'."),
            ("Being an animal resembling a Yahoo, the council feared I might incite the beasts to rebellion.", "Bir Yahoo'ya benzeyen bir hayvan olduğum için meclis canavarları isyana kışkırtabileceğimden korktu.", "Participle clause of cause 'Being an animal'; modal 'might incite'."),
            ("My master wept as he helped me build a sturdy canoe covered with Yahoo skins.", "Yahoo derileriyle kaplı sağlam bir kano inşa etmeme yardım ederken efendim ağladı.", "Time clause with 'as'; past participle modifier 'covered with skins'."),
            ("I fell upon my knees and kissed his hoof in reverent, weeping gratitude.", "Dizlerimin üzerine çöktüm ve hürmetli, ağlayan bir minnetle onun toynağını öptüm.", "Coordinate past verbs 'fell and kissed'; adjective phrase 'reverent gratitude'."),
            ("I sailed away on February 15, 1715, mourning the loss of the only true paradise on earth.", "Yeryüzündeki tek gerçek cennetin kaybına yas tutarak 15 Şubat 1715'te yelken açtım.", "Participle phrase 'mourning the loss'; date phrase."),
            ("I was rescued against my will by a Portuguese ship commanded by the noble Don Pedro de Mendez.", "Soylu Don Pedro de Mendez'in komutasındaki bir Portekiz gemisi tarafından rızam hilafına kurtarıldım.", "Passive voice 'was rescued against my will'; past participle modifier."),
            ("Don Pedro treated me with unmatched Christian charity, courtesy, and brotherly love.", "Don Pedro bana eşsiz bir Hristiyan hayırseverliği, nezaketi ve kardeş sevgisiyle muamele etti.", "Prepositional phrase 'with charity and courtesy'; past verb 'treated'."),
            ("Yet so disgusted was I by human nature that I could scarcely endure his presence.", "Fakat insan doğasından öyle tiksinmiştim ki onun varlığına bile zar zor katlanabiliyordum.", "Inverted result clause 'so disgusted was I that'; adverb 'scarcely'."),
            ("I returned to my home in Redriff in December, reunited with my wife and family.", "Aralık ayında Redriff'teki evime döndüm; karım ve ailemle yeniden bir araya geldim.", "Past participle modifier 'reunited with'; past verb 'returned'."),
            ("When my wife embraced me, I swooned in horror at the touch and smell of a Yahoo.", "Karım bana sarıldığında bir Yahoo'nun dokunuşu ve kokusu karşısında dehşet içinde kendimden geçtim.", "Time clause with 'embraced'; past verb 'swooned in horror'."),
            ("For a full year, I could not bear the sight or conversation of my own children.", "Tam bir yıl boyunca öz çocuklarımın yüzüne bakmaya veya onlarla sohbet etmeye dayanamadım.", "Modal negative 'could not bear'; duration phrase 'For a full year'."),
            ("I bought two horses and spent four hours every day conversing with them in my stable.", "İki at satın aldım ve ahırımda onlarla sohbet ederek her gün dört saat geçirdim.", "Coordinate past verbs 'bought and spent'; gerund phrase 'conversing with them'."),
            ("Their neighing and scent reminded me of the glorious virtues of the Houyhnhnms.", "Onların kişnemesi ve kokusu bana Houyhnhnm'lerin şanlı erdemlerini hatırlattı.", "Coordinate subjects; past verb 'reminded of'."),
            ("Gradually, I learned to tolerate the presence of my family at the far end of the dining table.", "Yavaş yavaş yemek masasının en uzak ucunda ailemin bulunmasına tahammül etmeyi öğrendim.", "Verb + infinitive 'learned to tolerate'; adverb 'gradually'."),
            ("Yet human pride remains to me the most intolerable and ridiculous of all vices.", "Yine de insan kibri bana göre tüm kötülüklerin en katlanılmaz ve en gülünç olanı olarak kalmaktadır.", "Superlative phrase 'most intolerable and ridiculous'; present verb 'remains'."),
            ("That a puny, deformed, disease-ridden Yahoo should be swollen with pride amazes me.", "Ufacık, sakat, hastalıklarla boğuşan bir Yahoo'nun kibirle kabarması beni hayrete düşürüyor.", "Noun clause subject introduced by 'That'; modal 'should be swollen'."),
            ("I wrote these travels not to amuse, but to inform and correct the follies of mankind.", "Bu seyahatleri eğlendirmek için değil, insanlığın ahmaklıklarını bildirmek ve düzeltmek için yazdım.", "Negative contrast 'not to amuse, but to inform'; coordinate infinitives."),
            ("I bid farewell to the reader, entreating him to cast away pride, cruelty, and deceit.", "Kibri, zalimliği ve aldatmayı bir kenara bırakması için yalvararak okuyucuya veda ediyorum.", "Participle phrase 'entreating him to cast away'; present verb 'bid farewell'."),
            ("May the memory of pure reason live forever in the minds of those who seek wisdom.", "Saf aklın hatırası hikmet arayanların zihninde sonsuza dek yaşasın.", "Optative modal 'May the memory live'; relative clause 'who seek wisdom'."),
            ("Thus end the extraordinary travels of Lemuel Gulliver across the kingdoms of the world.", "Böylece Lemuel Gulliver'ın dünya krallıkları boyunca yaptığı olağanüstü seyahatler sona erer.", "Inverted closing sentence 'Thus end the travels'; transitional adverb 'Thus'.")
        ]
    }
]

def generate_data_file():
    data_path = os.path.join(os.path.dirname(__file__), "book_19_data.py")
    
    assert len(PAGES) == 15, f"Expected 15 pages, got {len(PAGES)}"
    total_sentences = 0
    total_vocab = 0
    
    pages_data = []
    
    for i, p in enumerate(PAGES):
        p_num = i + 1
        assert p["page_number"] == p_num, f"Page number mismatch: {p['page_number']} vs {p_num}"
        assert len(p["sentences"]) == 20, f"Page {p_num} has {len(p['sentences'])} sentences, expected 20"
        assert len(p["vocab"]) == 8, f"Page {p_num} has {len(p['vocab'])} vocab, expected 8"
        
        page_sentences = []
        for s_idx, s in enumerate(p["sentences"]):
            total_sentences += 1
            page_sentences.append({
                "id": total_sentences,
                "text": s[0],
                "translation": s[1],
                "notes": s[2]
            })
            
        total_vocab += len(p["vocab"])
        pages_data.append({
            "page_no": p_num,
            "title": p["title"],
            "tr_title": TR_TITLES[i],
            "sentences": page_sentences,
            "vocab_focus": p["vocab"]
        })
        
    assert total_sentences == 300, f"Expected 300 sentences, got {total_sentences}"
    assert total_vocab == 120, f"Expected 120 vocab words, got {total_vocab}"
    
    print(f"Validation passed: {len(PAGES)} pages, {total_sentences} sentences, {total_vocab} vocab items.")
    
    with open(data_path, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nBook 19: Gulliver\'s Travels (Jonathan Swift)\n')
        f.write('Level 1 Graded Reader — 15 Pages x 20 Sentences = 300 Sentences.\n"""\n\n')
        f.write('BOOK_TITLE = "Gulliver\'s Travels: Extraordinary Voyages (15 Sayfa / 300 Cümle / Graded Reader)"\n')
        f.write('AUTHOR = "Jonathan Swift"\n\n')
        f.write(f"PAGES_DATA = {pprint.pformat(pages_data, indent=4, width=120)}\n")
        
    print(f"Successfully wrote {data_path}")

if __name__ == "__main__":
    generate_data_file()
