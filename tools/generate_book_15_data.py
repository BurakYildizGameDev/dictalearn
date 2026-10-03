"""
Book 15 Generator: The Wind in the Willows (Kenneth Grahame)
15 Pages, exactly 20 sentences per page = 300 sentences total.
8 Target vocabulary terms per page = 120 vocabulary items total.
Level 1 / Seviye 1 Graded Reader for English learners.
"""

import os
import pprint

BOOK_META = {
    "id": "book_15_the_wind_in_the_willows",
    "title": "The Wind in the Willows",
    "subtitle": "Kenneth Grahame's Classic Tale of Riverbank, Friendship, and Adventure",
    "author": "Kenneth Grahame",
    "level": "Seviye 1 (A1-A2 Beginner)",
    "target_readers": "İngilizce öğrenenler ve nehir kıyısı klasiklerini sevenler için çift dilli okuma kitabı",
    "total_pages": 15,
    "sentences_per_page": 20,
    "total_sentences": 300,
    "theme_color_primary": "#1E3A8A",    # Riverbank Navy / Deep Blue
    "theme_color_secondary": "#16A34A",  # Meadow Green
    "theme_color_accent": "#EA580C",     # Toad Amber / Rust
    "theme_color_light": "#EFF6FF"       # Soft River Sky Tint
}

TR_TITLES = [
    "Nehir Kıyısı ve İlk Tanışma",
    "Açık Yol ve Sarı Karavan",
    "Otomobil Çılgınlığı",
    "Vahşi Orman ve Kar Fırtınası",
    "Porsuk'un Sıcak Kapısı",
    "Bay Porsuk'un Ocağı Başında",
    "Toad'u Kurtarma Girişimi",
    "Kırmızı Aslan Hanı ve Kaçış",
    "Mahkeme ve Zindan Cezası",
    "Çamaşırcı Kadın Kılığı",
    "Kanal Mavnası ve Çalınan At",
    "Toad Malikanesi'nin İşgali",
    "Nehrin Altındaki Gizli Tünel",
    "Toad Malikanesi Baskını",
    "Nehir Kıyısında Huzur ve Zafer"
]

PAGES = [
    # Page 1: The River Bank
    {
        "page_number": 1,
        "title": "The River Bank",
        "vocab": [
            ("whitewash", "badana yapmak"),
            ("spring", "ilkbahar"),
            ("burrow", "yer altı ini, köstebek yuvası"),
            ("meadow", "çayır, otlak"),
            ("scent", "koku"),
            ("scuttle", "aceleyle koşuşmak"),
            ("riverbank", "nehir kıyısı"),
            ("oar", "kürek")
        ],
        "sentences": [
            ("The Mole had been working very hard all the morning, spring-cleaning his little home.", "Köstebek bütün sabah küçük evinin bahar temizliğini yaparak çok sıkı çalışmıştı.", "Past perfect continuous 'had been working'; compound noun 'spring-cleaning'."),
            ("First with brooms, then with dusters, then on ladders with a pail of whitewash.", "Önce süpürgelerle, sonra toz bezleriyle, ardından bir kova badanayla merdivenlerin üzerinde.", "Prepositional phrases describing progressive tools."),
            ("Dust filled his throat and his eyes, and splashes of whitewash covered his black fur.", "Toz boğazını ve gözlerini doldurdu, badana sıçrantıları siyah kürkünü kapladı.", "Coordinate clauses with 'and'; noun phrase 'splashes of whitewash'."),
            ("Spring was moving in the air above and in the earth below around him.", "Bahar, hem yukarıdaki havada hem de altındaki toprakta onun etrafında canlanıyordu.", "Parallel prepositional phrases 'in the air above and in the earth below'."),
            ("Suddenly, he flung down his brush on the floor and cried out aloud.", "Aniden fırçasını yere fırlattı ve yüksek sesle bağırdı.", "Irregular past 'flung' (fling); phrasal verb 'cried out'."),
            ("'Bother!' and 'O blow!' and also 'Hang spring-cleaning!' he shouted happily.", "'Canı cehenneme!' ve 'Batsın bahar temizliği!' diye neşeyle haykırdı.", "Colloquial exclamations of annoyance and relief; adverb 'happily'."),
            ("He bolted out of the house without even waiting to put on his coat.", "Ceketini giymeyi bile beklemeden evden yıldırım hızıyla fırlayıp çıktı.", "Phrasal verb 'bolted out of'; preposition 'without' + gerund."),
            ("He scraped and scratched and scrabbled with his little paws toward the sunlight.", "Minik patileriyle gün ışığına doğru kazdı, tırmaladı ve debelendi.", "Alliterative verbs 'scraped, scratched, scrabbled'."),
            ("Pop! His snout came out into the sunlight, and he found himself in warm grass.", "Pat! Burnu gün ışığına çıktı ve kendini ılık çimlerin içinde buldu.", "Onomatopoeic interjection 'Pop!'; reflexive 'found himself'."),
            ("He shook his fur thoroughly to get the dust off his coat.", "Kürkündeki tozu silkelemek için üzerini adamakıllı silkeledi.", "Infinitive of purpose 'to get the dust off'; adverb 'thoroughly'."),
            ("The sunshine struck hot on his fur, and soft breezes caressed his heated brow.", "Güneş ışığı kürküne sıcak vurdu ve tatlı esintiler terlemiş alnını okşadı.", "Irregular past 'struck' (strike); coordinate predicates."),
            ("He crossed several meadows and wandered aimlessly through hedgerows.", "Pek çok çayırı aştı ve çalı çitleri arasında amaçsızca dolaştı.", "Quantifier 'several'; adverb 'aimlessly'."),
            ("Never in his whole underground life had he seen such beauty before.", "Yeraltındaki bütün hayatı boyunca daha önce hiç böylesi bir güzellik görmemişti.", "Inverted negative sentence 'Never... had he seen'."),
            ("Presently, he came to the edge of a full-fed river flowing past.", "Çok geçmeden, yanından çağıldayarak akan coşkun bir nehrin kenarına geldi.", "Adverb 'presently'; participial adjective 'full-fed river'."),
            ("He had never seen a real river in his life before this moment.", "Bu andan önce hayatında gerçek bir nehir hiç görmemişti.", "Past perfect with 'never'; time phrase 'before this moment'."),
            ("The sleek water chattered and bubbled over glistening round pebbles.", "Pırıl pırıl su, parıldayan yuvarlak çakıl taşlarının üzerinden şırıldayarak köpürdü.", "Onomatopoeic verbs 'chattered and bubbled'; adjective 'glistening'."),
            ("As he sat on the grassy bank, he noticed a dark hole in the opposite bank.", "Otlu kıyıda otururken, karşı kıyıda karanlık bir delik fark etti.", "Time clause 'as he sat'; adjective 'opposite'."),
            ("Something bright and small seemed to twinkle right in the heart of it.", "Deliğin tam kalbinde parlak ve küçük bir şey göz kırpar gibiydi.", "Indefinite pronouns with adjectives 'something bright and small'."),
            ("Then two small brown ears and a neat little whiskered face appeared.", "Ardından iki küçük kahverengi kulak ve düzgün, bıyıklı minik bir yüz belirdi.", "Coordinate subjects; adjective 'whiskered'."),
            ("It was the Water Rat, the cheerful master of the sparkling river.", "Bu, çağıldayan nehrin neşeli efendisi Su Sıçanı Ratty idi.", "Apposition identifying the character; adjective 'sparkling'.")
        ]
    },
    # Page 2: The Open Road (Mr. Toad and the Yellow Caravan)
    {
        "page_number": 2,
        "title": "The Open Road",
        "vocab": [
            ("canary", "kanarya sarısı"),
            ("caravan", "karavan, göçebe arabası"),
            ("boast", "övünmek, böbürlenmek"),
            ("restless", "huzursuz, yerinde duramayan"),
            ("fidget", "kıpır kıpır etmek"),
            ("splendid", "muhteşem, görkemli"),
            ("harness", "koşum takımı takmak"),
            ("whim", "anlık heves, kapris")
        ],
        "sentences": [
            ("The Water Rat rowed his little blue boat across to welcome Mole.", "Su Sıçanı, Köstebek'i karşılamak için küçük mavi kayığını karşıya kürekledi.", "Directional adverb 'across'; infinitive of purpose 'to welcome'."),
            ("They immediately became the best of friends, sharing bread and ginger beer.", "Ekmeği ve zencefilli gazozu paylaşarak hemen en yakın dostlar oldular.", "Participial phrase 'sharing bread...'; superlative 'best of friends'."),
            ("A few days later, Ratty took Mole to visit wealthy Mr. Toad at Toad Hall.", "Birkaç gün sonra Ratty, Köstebek'i Toad Konağı'nda zengin Bay Toad'u ziyarete götürdü.", "Time phrase 'a few days later'; proper location 'Toad Hall'."),
            ("Toad Hall was an imposing Tudor mansion of mellow red brick with old lawns.", "Toad Konağı, eski çimenlikleriyle olgun kırmızı tuğladan yapılmış heybetli bir Tudor malikanesiydi.", "Descriptive adjectives 'imposing, mellow'; noun phrase 'Tudor mansion'."),
            ("Mr. Toad was rich, boastful, good-natured, but terribly conceited and restless.", "Bay Toad zengin, övüngen, iyi huyluydu; fakat fena halde kibirli ve huzursuzdu.", "Coordinate personality adjectives; adverb 'terribly'."),
            ("He welcomed them warmly and danced around them with open arms.", "Onları sıcak bir şekilde karşıladı ve kollarını açarak etraflarında dans etti.", "Coordinate past verbs 'welcomed and danced'; manner phrase 'with open arms'."),
            ("'You are just in time!' cried Toad, leading them into the stable yard.", "'Tam vaktinde geldiniz!' diye bağırdı Toad, onları ahır avlusuna doğru götürürken.", "Idiom 'just in time'; participle clause 'leading them'."),
            ("In the yard stood a brand-new gypsy caravan, painted canary-yellow picked out with green.", "Avluda, yeşil işlemelerle süslenmiş kanarya sarısına boyalı, yepyeni bir çingene karavanı duruyordu.", "Inverted sentence; compound adjective 'canary-yellow'."),
            ("'There you are!' shouted Toad, 'there is real life for you in that cart!'", "'İşte buradasınız!' diye bağırdı Toad, 'işte o arabada sizin için gerçek bir hayat var!'", "Exclamatory structure; noun phrase 'real life'."),
            ("'The open road! The dusty highway! Camps, villages, towns, and cities!'", "'Açık yol! Tozlu ana yol! Kamplar, köyler, kasabalar ve şehirler!'", "List of exclamatory noun phrases celebrating freedom."),
            ("Ratty shook his head doubtful, for he loved his quiet river too much.", "Ratty başını şüpheyle salladı, zira sakin nehrini fazlasıyla çok seviyordu.", "Causal coordinating conjunction 'for'; adverbial intensifier 'too much'."),
            ("Mole, however, was fascinated by the shiny yellow cart and its tiny bunks.", "Ancak Köstebek, parıldayan sarı arabadan ve minik ranzalarından büyülenmişti.", "Transitional adverb 'however'; passive voice 'was fascinated by'."),
            ("Toad persuaded them both to climb aboard and set out on a grand tour.", "Toad her ikisini de araca binip büyük bir tura çıkmaları için ikna etti.", "Verb + object + infinitive 'persuaded them to climb'; idiom 'set out'."),
            ("An old gray horse was harnessed to pull the heavy yellow home.", "Ağır sarı evi çekmek için yaşlı gri bir at koşuldu.", "Passive voice 'was harnessed'; infinitive of purpose 'to pull'."),
            ("They set off down the country lane in the glorious afternoon sun.", "Görkemli öğleden sonra güneşinde köy yolu boyunca yola koyuldular.", "Phrasal verb 'set off down'; adjective 'glorious'."),
            ("Toad walked ahead proudly, boasting about how clever and adventurous he was.", "Toad ne kadar zeki ve maceracı olduğuyla övünerek gururla önde yürüdü.", "Participle phrase 'boasting about'; indirect question clause 'how clever he was'."),
            ("They camped that evening in a grassy meadow under the starlit sky.", "O akşam yıldızlı gökyüzünün altındaki çimenli bir çayırda kamp kurdular.", "Compound noun 'starlit sky'; prepositional phrase 'under the sky'."),
            ("Ratty and Mole did all the cooking, cleaning, and feeding of the poor horse.", "Yemek yapmayı, temizliği ve zavallı atı beslemeyi tamamen Ratty ile Mole yaptı.", "Gerund list as direct objects of 'did'; adjective 'poor'."),
            ("Toad simply sprawled on the grass and talked about his endless cleverness.", "Toad ise sadece çimlerin üzerine yayılıp bitmek bilmez zekasından bahsetti.", "Adverb 'simply'; irregular past 'sprawled'."),
            ("A strange roaring sound in the distance was about to change everything.", "Uzaktan gelen tuhaf bir kükreme sesi her şeyi değiştirmek üzereydi.", "Participial phrase 'in the distance'; structure 'was about to change'.")
        ]
    },
    # Page 3: The Motor-Car Madness (Toad Discovers Automobiles)
    {
        "page_number": 3,
        "title": "The Motor-Car Madness",
        "vocab": [
            ("ditch", "hendek"),
            ("splendor", "ihtişam, parıltı"),
            ("wreck", "enkaza çevirmek / enkaz"),
            ("dust", "toz bulutu"),
            ("poop", "korna sesi"),
            ("trance", "kendinden geçme, trans"),
            ("passion", "tutku"),
            ("furious", "küplere binmiş, öfkeli")
        ],
        "sentences": [
            ("The following afternoon, they were strolling peacefully along a dusty high road.", "Ertesi öğleden sonra, tozlu bir ana yol boyunca huzur içinde yürüyorlardı.", "Past continuous 'were strolling'; adverb 'peacefully'."),
            ("The gray horse walked lazily, and Toad talked endlessly of great future travels.", "Gri at tembelce yürüyor, Toad ise gelecekteki büyük yolculuklardan durmaksızın bahsediyordu.", "Adverbs 'lazily' and 'endlessly'; compound noun 'future travels'."),
            ("Suddenly, a faint hum was heard far behind them down the long road.", "Birdenbire, uzun yolun ta gerisinden hafif bir uğultu duyuldu.", "Passive voice 'was heard'; adjective 'faint'."),
            ("The hum grew rapidly into an energetic, droning roar of tremendous speed.", "Uğultu hızla muazzam bir hızın enerjik, vızıldayan kükremesine dönüştü.", "Phrasal development 'grew into'; coordinate adjectives."),
            ("With a blinding cloud of dust, a magnificent motor-car shot past them.", "Kör edici bir toz bulutu eşliğinde, görkemli bir otomobil yanlarından ok gibi fırlayıp geçti.", "Prepositional phrase 'with a blinding cloud'; past verb 'shot past'."),
            ("'Poop-poop!' sounded the brass horn with an arrogant, triumphant blast.", "'Düt-düt!' diye pirinç korna küstah ve muzaffer bir sesle öttü.", "Onomatopoeia; coordinate adjectives 'arrogant, triumphant'."),
            ("The sudden blast terrified the old gray horse pulling the caravan.", "Bu ani ses, karavanı çeken yaşlı gri atı dehşete düşürdü.", "Transitive past verb 'terrified'; participial modifier 'pulling the caravan'."),
            ("The horse reared up on its hind legs and backed straight into a ditch.", "At arka ayakları üzerine şaha kalktı ve dosdoğru bir hendeğe doğru geri geri gitti.", "Phrasal verbs 'reared up' and 'backed into'."),
            ("With a tremendous crash, the canary-colored cart overturned into deep mud.", "Büyük bir gürültüyle, kanarya rengi araba derin çamurun içine devrildi.", "Prepositional phrase 'with a tremendous crash'; past verb 'overturned'."),
            ("Plates shattered, pots rolled into the ditch, and wheels spun uselessly in the air.", "Tabaklar kırıldı, tencereler hendeğe yuvarlandı ve tekerlekler havada nafile döndü.", "Parallel past clauses describing destruction; adverb 'uselessly'."),
            ("Ratty jumped up and down in the road, shaking both fists in furious anger.", "Ratty yolun ortasında öfkeden küplere binmiş halde iki yumruğunu birden sallayarak zıpladı.", "Participial phrase 'shaking both fists'; noun phrase 'furious anger'."),
            ("'You scoundrels!' shouted Rat, 'You road hogs! I will report you to the law!'", "'Sizi alçaklar!' diye bağırdı Rat, 'Sizi yol canavarları! Sizi kanuna şikayet edeceğim!'", "Vocative insults; future modal 'will report'."),
            ("Toad, however, sat in the middle of the dusty road, staring ahead blankly.", "Fakat Toad tozlu yolun ortasında oturmuş, boş gözlerle ileriye bakıyordu.", "Transitional 'however'; participle phrase 'staring ahead blankly'."),
            ("His mouth hung open, and his eyes were fixed on the fading dust cloud.", "Ağzı açık kalmıştı ve gözleri kaybolan toz bulutuna dikilmişti.", "Passive participle 'were fixed on'; participial adjective 'fading'."),
            ("'Poop-poop!' whispered Toad in a state of absolute religious ecstasy.", "'Düt-düt!' diye fısıldadı Toad tam bir dini vecd içinde.", "Prepositional phrase 'in a state of ecstasy'; adjective 'absolute'."),
            ("'The poetry of motion! The real way to travel! The only way to live!'", "'Hareketin şiiri! Seyahat etmenin gerçek yolu! Yaşamanın tek yolu!'", "Parallel exclamations praising speed; infinitive modifiers."),
            ("'He is enchanted!' cried Mole, 'he is completely out of his mind!'", "'Büyülendi!' diye haykırdı Mole, 'tamamen aklını kaçırdı!'", "Passive 'is enchanted'; idiom 'out of his mind'."),
            ("They tried to shake Toad, but he refused to help them right the broken cart.", "Toad'u sarsıp kendine getirmeye çalıştılar ama kırık arabayı düzeltmelerine yardım etmeyi reddetti.", "Verb + infinitive 'refused to help'; transitive verb 'right' meaning to set upright."),
            ("'Nasty, sluggish carts are things of the past!' declared Toad dreamily.", "'Pis, hantal arabalar artık geçmişte kaldı!' dedi Toad rüya görüyormuşçasına.", "Coordinate adjectives 'nasty, sluggish'; idiom 'things of the past'."),
            ("A dangerous obsession had planted its deep seeds inside Toad's reckless brain.", "Tehlikeli bir takıntı, Toad'un pervasız beyninin içine derin tohumlarını ekmişti.", "Past perfect 'had planted'; compound adjective 'deep seeds'."),
        ]
    },
    # Page 4: The Wild Wood (Mole Ventures into the Snow-Covered Forest)
    {
        "page_number": 4,
        "title": "The Wild Wood",
        "vocab": [
            ("wood", "koru, orman"),
            ("stoat", "kakım, dağ gelinciği"),
            ("weasel", "gelincik"),
            ("twilight", "alacakaranlık"),
            ("menace", "tehdit, gözdağı"),
            ("shiver", "titremek"),
            ("panic", "panik, dehşet"),
            ("hollow", "oyuk, kovuk")
        ],
        "sentences": [
            ("Winter arrived, and the river was quiet under cold leaden skies.", "Kış geldi çattı ve nehir kurşuni soğuk gökyüzünün altında sessizleşti.", "Coordinate clauses; compound adjective 'cold leaden'."),
            ("Mole wanted very much to meet the legendary Mr. Badger who lived in the Wild Wood.", "Mole, Vahşi Orman'da yaşayan efsanevi Bay Porsuk ile tanışmayı çok istiyordu.", "Adverbial intensifier 'very much'; relative clause 'who lived in'."),
            ("Ratty warned him that the Wild Wood was dangerous for quiet river dwellers.", "Ratty onu Vahşi Orman'ın sakin nehir sakinleri için tehlikeli olduğu konusunda uyardı.", "Noun clause with 'that'; noun phrase 'river dwellers'."),
            ("'Weasels, stoats, and foxes live there, and they are not always polite,' said Rat.", "'Gelincikler, kakımlar ve tilkiler orada yaşar ve her zaman kibar davranmazlar,' dedi Rat.", "Compound subject; litotes 'not always polite'."),
            ("One cold winter afternoon, while Ratty dozed by the warm fire, Mole slipped outside.", "Soğuk bir kış öğleden sonrasında, Ratty sıcak ateşin yanında uyuklarken, Mole sessizce dışarı süzüldü.", "Temporal subordinate clause with 'while'; phrasal verb 'slipped outside'."),
            ("He walked across the frozen meadows toward the dark wall of the Wild Wood.", "Vahşi Orman'ın karanlık duvarına doğru donmuş çayırlar boyunca yürüdü.", "Directional prepositional phrases 'across... toward'."),
            ("The leafless trees stood like gray specters against the pale winter twilight.", "Yapraksız ağaçlar, solgun kış alacakaranlığına karşı gri hayaletler gibi dikiliyordu.", "Simile 'like gray specters'; preposition 'against'."),
            ("At first, Mole enjoyed the thrill of solitary adventure among the trees.", "İlk başta Mole, ağaçlar arasındaki bu yalnız maceranın heyecanından keyif aldı.", "Time phrase 'at first'; noun phrase 'thrill of solitary adventure'."),
            ("Then the shadows deepened rapidly as the cold winter sun sank down.", "Sonra soğuk kış güneşi batarken gölgeler hızla derinleşti.", "Time clause with 'as'; phrasal verb 'sank down'."),
            ("A hollow whistling sounded through the bare branches like a cruel whisper.", "Çıplak dalların arasından zalimce bir fısıltı gibi uğultulu bir ıslık sesi duyuldu.", "Simile 'like a cruel whisper'; participial adjective 'bare branches'."),
            ("Mole looked around and thought he saw little wicked faces peering out of holes.", "Mole etrafına bakındı ve deliklerden dik dik bakan minik hain yüzler gördüğünü sandı.", "Perception verb 'saw' + participle 'peering out of'."),
            ("Every tree root seemed like an outstretched claw waiting to trip his little feet.", "Her ağaç kökü, minik ayaklarına çelme takmak için bekleyen uzanmış bir pençe gibi görünüyordu.", "Simile 'like an outstretched claw'; infinitive of purpose 'to trip'."),
            ("He began to run, stumbling over hidden rocks and fallen branches.", "Gizli kayaların ve düşmüş dalların üzerinden tökezleyerek koşmaya başladı.", "Verb followed by infinitive 'began to run'; participle clause 'stumbling over'."),
            ("He ran blindly without knowing which direction led back to the river.", "Hangi yönün nehre geri götürdüğünü bilmeden körlemesine koştu.", "Adverb 'blindly'; preposition 'without' + gerund with indirect question."),
            ("A sharp flurry of cold white snow began drifting down upon the forest.", "Soğuk beyaz kardan keskin bir tipi ormanın üzerine savrularak yağmaya başladı.", "Noun phrase 'sharp flurry of snow'; phrasal verb 'drifting down'."),
            ("The terrifying silence of the wild forest surrounded him like an icy prison.", "Vahşi ormanın dehşet verici sessizliği, buzdan bir zindan gibi etrafını sardı.", "Simile 'like an icy prison'; transitive past verb 'surrounded'."),
            ("Mole crawled into the dark hollow of an old beech tree for protection.", "Mole korunmak için yaşlı bir kayın ağacının karanlık oyuğuna sürünerek girdi.", "Prepositional phrase 'into the hollow of'; purpose phrase 'for protection'."),
            ("He covered himself with dead leaves and trembled from exhaustion and panic.", "Üzerini kuru yapraklarla örttü ve bitkinlikten, panikten titredi.", "Coordinate past verbs 'covered and trembled'; preposition 'from' for cause."),
            ("'Ratty! Ratty, where are you?' he whimpered into the gathering blizzard.", "'Ratty! Ratty neredesin?' diye inledi giderek şiddetlenen kar fırtınasının içine.", "Participial adjective 'gathering blizzard'; direct speech."),
            ("The great forest held him trapped inside its cold, merciless heart.", "Ulu orman, onu soğuk ve merhametsiz kalbinin içinde kapana kıstırmıştı.", "Complex transitive structure 'held him trapped'; coordinate adjectives 'cold, merciless'.")
        ]
    },
    # Page 5: Lost in the Blizzard (Mole and Rat Find Shelter at Badger's Door)
    {
        "page_number": 5,
        "title": "Lost in the Blizzard",
        "vocab": [
            ("blizzard", "kar fırtınası, tipi"),
            ("scraper", "kapı önü çamur sıyıracı"),
            ("knocker", "kapı tokmağı"),
            ("iron", "demir"),
            ("wander", "dolaşmak, başıboş gezmek"),
            ("exhausted", "tükenmiş, bitap"),
            ("shout", "bağırmak, haykırmak"),
            ("scrape", "çarpmak, sıyırmak")
        ],
        "sentences": [
            ("Meanwhile, the Water Rat woke from his nap beside the warm fireplace.", "Bu esnada Su Sıçanı, sıcak şöminenin yanındaki uykusundan uyandı.", "Adverb 'meanwhile'; prepositional phrase 'beside the fireplace'."),
            ("He called for Mole, but received no answer throughout the empty rooms.", "Mole'a seslendi fakat boş odaların hiçbirinden cevap alamadı.", "Negative coordinate 'received no answer'; preposition 'throughout'."),
            ("Noticing Mole's boots and coat missing, Ratty guessed his friend's foolish errand.", "Mole'un çizmelerinin ve ceketinin yerinde olmadığını fark eden Ratty, dostunun akılsızca işini tahmin etti.", "Participial clause of cause 'Noticing...'; possessive 'friend's foolish errand'."),
            ("He armed himself with two pistols and a stout cudgel without delay.", "Hiç vakit kaybetmeden yanına iki tabanca ve sağlam bir kalın sopa aldı.", "Reflexive 'armed himself with'; prepositional phrase 'without delay'."),
            ("Ratty stepped courageously out into the freezing storm, tracking Mole's footprints.", "Ratty, Mole'un ayak izlerini takip ederek dondurucu fırtınaya cesurca adım attı.", "Adverb 'courageously'; participle phrase 'tracking footprints'."),
            ("After an hour of searching the shadowy forest, Rat heard a faint whimper.", "Karanlık ormanı bir saat aradıktan sonra Rat hafif bir inleme duydu.", "Prepositional temporal phrase 'after an hour of searching'."),
            ("'Mole! Mole, is that you?' shouted the loyal rat through the falling snow.", "'Mole! Mole sen misin?' diye haykırdı sadık sıçan yağan karın arasından.", "Participial phrase 'through the falling snow'; adjective 'loyal'."),
            ("Mole burst into tears of overwhelming joy as he threw his paws around Rat.", "Mole patilerini Rat'in boynuna sararken ezici bir sevinç gözyaşlarına boğuldu.", "Idiom 'burst into tears of joy'; time clause with 'as'."),
            ("Both friends tried to find their way home, but the deep snow covered every trail.", "İki dost evlerinin yolunu bulmaya çalıştılar ama derin kar her bir patikayı örtmüştü.", "Coordinate clauses with 'but'; determiner 'every trail'."),
            ("The wind wailed furiously, and their little feet grew completely numb with cold.", "Rüzgar öfkeyle uludu ve minik ayakları soğuktan tamamen uyuştu.", "Adverb 'furiously'; copular verb 'grew numb'."),
            ("Suddenly, Mole tripped over something hard buried beneath the snow and cried out.", "Birdenbire Mole karın altına gömülmüş sert bir şeye takılıp düştü ve bağırdı.", "Phrasal verb 'tripped over'; participle modifier 'buried beneath'."),
            ("'I have cut my shin!' wept Mole, sitting down in the white drifts.", "'Kaval kemiğimi kestim!' diye ağladı Mole, beyaz kar yığınlarının içine oturarak.", "Present perfect 'have cut'; participle clause 'sitting down'."),
            ("Ratty examined the wound and carefully cleared away the snow around the spot.", "Ratty yarayı inceledi ve o noktanın etrafındaki karları dikkatlice temizledi.", "Coordinate past verbs 'examined and cleared away'."),
            ("He found a flat piece of iron sticking out of the frozen bank.", "Donmuş setten dışarı uzanan düz bir demir parçası buldu.", "Participle clause 'sticking out of'; compound adjective 'frozen bank'."),
            ("'It is an iron door-scraper!' exclaimed Ratty in triumphant excitement.", "'Bu demirden bir kapı sıyıracı!' diye haykırdı Ratty muzaffer bir heyecanla.", "Prepositional phrase 'in triumphant excitement'; compound noun 'door-scraper'."),
            ("They dug frantically into the snowbank with all their frozen paws.", "Bütün donmuş patileriyle çılgınca kar setini kazdılar.", "Adverb 'frantically'; prepositional phrase 'with all paws'."),
            ("Next they found a thick doormat made of woven coconut fibers.", "Sonra hindistancevizi liflerinden dokunmuş kalın bir kapı paspası buldular.", "Past participle modifier 'made of woven fibers'."),
            ("Finally, their paws uncovered a solid green oak door with a brass knocker.", "Sonunda patileri pirinç tokmaklı masif yeşil bir meşe kapıyı açığa çıkardı.", "Adjective list 'solid green oak'; prepositional phrase 'with a brass knocker'."),
            ("On the brass plate was engraved: MR. BADGER in bold capital letters.", "Pirinç levhanın üzerine koyu büyük harflerle şöyle kazınmıştı: BAY PORSUK.", "Passive inverted structure 'was engraved'; proper name 'MR. BADGER'."),
            ("Rat seized the heavy knocker and struck three mighty blows upon the wood.", "Rat ağır kapı tokmağını kavradı ve ahşabın üzerine üç güçlü darbe indirdi.", "Coordinate past verbs 'seized and struck'; adjective 'mighty'.")
        ]
    },
    # Page 6: Inside Mr. Badger's Kitchen (Hospitality, Fire, and Wisdom)
    {
        "page_number": 6,
        "title": "Mr. Badger's Hearth",
        "vocab": [
            ("hearth", "ocak başı, şömine"),
            ("slippers", "terlik"),
            ("roast", "kızartmak / rosto"),
            ("snug", "sıcacık, korunaklı"),
            ("hospitable", "misafirperver"),
            ("candle", "mum"),
            ("cauldron", "kazan"),
            ("safety", "güvenlik")
        ],
        "sentences": [
            ("Slow bolts were drawn back, and the heavy door creaked slowly open.", "Yavaşça sürgüler geri çekildi ve ağır kapı gıcırdayarak usulca açıldı.", "Passive coordinate clauses 'were drawn back' and 'creaked open'."),
            ("There stood Mr. Badger in a dressing-gown and worn carpet slippers.", "Sabahlığı ve yıpranmış halı terlikleri içinde Bay Porsuk orada dikiliyordu.", "Inverted sentence; compound nouns 'dressing-gown' and 'carpet slippers'."),
            ("He held a glowing candle high, peering gruffly into the white storm.", "Ateş gibi yanan mumu havaya kaldırıp beyaz fırtınanın içine sertçe baktı.", "Participle phrase 'peering gruffly'; adjective 'gruffly'."),
            ("'What, Ratty!' he exclaimed, 'and little Mole too! Come in at once!'", "'Ne, Ratty mi!' diye haykırdı, 've minik Mole da mı! Hemen içeri gelin!'", "Imperative phrase 'come in at once'; familiar interjections."),
            ("He pulled them inside and slammed the thick door shut against the blizzard.", "Onları içeri çekti ve kalın kapıyı tipiye karşı sertçe kapattı.", "Phrasal verb 'pulled inside'; resultative 'slammed shut'."),
            ("They stepped into the largest, warmest brick-floored kitchen they had ever seen.", "Hayatlarında gördükleri en geniş, en sıcak ve tuğla zeminli mutfağa adım attılar.", "Superlatives 'largest, warmest'; past perfect relative clause."),
            ("A magnificent log fire blazed cheerfully on a wide, welcoming hearth.", "Geniş ve kucaklayıcı bir ocakta görkemli bir kütük ateşi neşeyle alev alev yanıyordu.", "Adverb 'cheerfully'; participial adjective 'welcoming hearth'."),
            ("Hams, onions, herbs, and baskets of dried fruit hung from the ceiling beams.", "Tavan kirişlerinden jambonlar, soğanlar, şifalı otlar ve kurutulmuş meyve sepetleri sarkıyordu.", "Compound subject; prepositional phrase 'from ceiling beams'."),
            ("Badger sat them down in comfortable armchairs directly before the fire.", "Porsuk onları doğrudan ateşin önündeki rahat koltuklara oturttu.", "Direct transitive 'sat them down'; adjective 'comfortable'."),
            ("He bathed Mole's injured shin with warm water and healing herbal ointments.", "Mole'un incinen kaval kemiğini ılık su ve şifalı bitkisel merhemlerle yıkadı.", "Compound noun 'healing herbal ointments'; transitive past 'bathed'."),
            ("Soon, a steaming supper of hot soup, cold roast beef, and bread was served.", "Çok geçmeden sıcak çorba, soğuk biftek ve ekmekten oluşan dumanı tüten bir akşam yemeği ikram edildi.", "Passive voice 'was served'; adjective 'steaming'."),
            ("The two tired wanderers ate hungrily until they could eat no more.", "İki yorgun gezgin daha fazla yiyemeyecek hale gelene kadar kurt gibi yediler.", "Adverb 'hungrily'; modal time clause 'until they could eat no more'."),
            ("Badger listened patiently as Ratty told the tale of their fearful misadventure.", "Ratty korkunç talihsizliklerinin hikayesini anlatırken Porsuk sabırla dinledi.", "Adverb 'patiently'; noun phrase 'fearful misadventure'."),
            ("'The Wild Wood is no place for gentle river folk,' Badger said shaking his head.", "'Vahşi Orman nazik nehir ahalisine göre bir yer değildir,' dedi Porsuk başını sallayarak.", "Participle clause 'shaking his head'; noun phrase 'gentle river folk'."),
            ("'Here underground, I am master of everything, and nobody dares disturb me.'", "'Burada yer altında her şeyin efendisi benim ve kimse beni rahatsız etmeye cesaret edemez.'", "Coordinate clauses; verb 'dares disturb'."),
            ("Then Ratty mentioned Mr. Toad's latest insane passion for expensive motor-cars.", "Sonra Ratty, Bay Toad'un pahalı otomobillere olan son delice tutkusundan bahsetti.", "Transitive past 'mentioned'; adjective 'insane'."),
            ("'He has had seven severe crashes already!' groaned Ratty in utter disgust.", "'Şimdiden yedi ağır kaza yaptı bile!' diye inledi Ratty tam bir bıkkınlıkla.", "Present perfect 'has had'; noun phrase 'utter disgust'."),
            ("'He has spent a huge fortune on fines and new machines,' Mole added.", "'Cezalara ve yeni makinelere devasa bir servet harcadı,' diye ekledi Mole.", "Present perfect 'has spent'; compound noun 'huge fortune'."),
            ("Badger stroked his gray chin thoughtfully and made a firm decision.", "Porsuk gri çenesini düşünceli bir tavırla sıvazladı ve kesin bir karar verdi.", "Adverb 'thoughtfully'; compound idiom 'made a firm decision'."),
            ("'When spring arrives, we three will take Toad firmly in hand,' vowed Badger.", "'Bahar geldiğinde biz üçümüz Toad'u sıkı bir terbiyeden geçireceğiz,' diye ant içti Porsuk.", "Time clause 'when spring arrives'; idiom 'take in hand'."),
        ]
    },
    # Page 7: The Intervention (Badger and Friends Try to Reform Toad)
    {
        "page_number": 7,
        "title": "The Intervention at Toad Hall",
        "vocab": [
            ("reform", "ıslah etmek, düzeltmek"),
            ("bedroom", "yatak odası"),
            ("lock", "kilitlemek / kilit"),
            ("fidget", "yerinde duramamak"),
            ("repent", "pişman olmak, tövbe etmek"),
            ("lecture", "öğüt vermek, azarlamak"),
            ("ruin", "mahvetmek, iflas ettirmek"),
            ("guard", "nöbet tutmak / muhafız")
        ],
        "sentences": [
            ("When mild spring returned, Mr. Badger knocked firmly upon Ratty's front door.", "Ilık ilkbahar geri döndüğünde, Bay Porsuk Ratty'nin ön kapısını kararlılıkla çaldı.", "Time clause; adverb 'firmly'."),
            ("'The hour has arrived,' said Badger sternly, 'we must rescue Toad from ruin.'", "'Vakit geldi çattı,' dedi Porsuk sertçe, 'Toad'u iflastan kurtarmalıyız.'", "Present perfect 'has arrived'; modal obligation 'must rescue'."),
            ("The three loyal friends marched up the long carriage drive of Toad Hall.", "Üç sadık dost, Toad Konağı'nın uzun araba yolu boyunca yürüdüler.", "Proper noun 'Toad Hall'; compound noun 'carriage drive'."),
            ("At the door stood a brand-new, bright red racing motor-car with polished brass.", "Kapıda, parlatılmış pirinç aksamlı, yepyeni parlak kırmızı bir yarış otomobili duruyordu.", "Inverted locative sentence; participle 'polished brass'."),
            ("Toad emerged down the steps wearing goggles, a heavy overcoat, and driving gloves.", "Toad gözlüklerini, kalın paltosunu ve sürüş eldivenlerini takmış halde basamaklardan indi.", "Participial phrase 'wearing goggles...'; past verb 'emerged'."),
            ("'Hooray!' cried Toad, 'you are just in time to come for a splendid ride!'", "'Yaşasın!' diye bağırdı Toad, 'muhteşem bir gezintiye çıkmak için tam vaktinde geldiniz!'", "Exclamation; idiom 'just in time'."),
            ("Badger seized him by the collar and led him back inside his own house.", "Porsuk onu yakasından yakaladı ve kendi evinin içine geri soktu.", "Phrasal verb 'led back inside'; prepositional phrase 'by the collar'."),
            ("'Take off those ridiculous rags at once!' ordered Badger with grim authority.", "'O saçma sapan paçavraları derhal çıkar!' diye emretti Porsuk sert bir otoriteyle.", "Imperative 'take off'; noun phrase 'grim authority'."),
            ("Rat and Mole stripped off Toad's driving gear and tossed it into the hall.", "Rat ve Mole, Toad'un sürüş kıyafetlerini üzerinden çıkardılar ve salona fırlattılar.", "Phrasal verb 'stripped off'; coordinate past 'tossed'."),
            ("Badger led the protesting amphibian into the library and closed the door.", "Porsuk itiraz edip duran bu amfibiyi kütüphaneye soktu ve kapıyı kapattı.", "Participial adjective 'protesting'; noun 'amphibian'."),
            ("For an hour, Badger gave Toad a severe, solemn lecture about his reckless behavior.", "Porsuk bir saat boyunca Toad'a pervasız davranışları hakkında ciddi, ağır bir nutuk çekti.", "Duration phrase 'for an hour'; adjective pair 'severe, solemn'."),
            ("When they came out, Toad was sobbing and promising to reform his ways.", "Dışarı çıktıklarında Toad hıçkıra hıçkıra ağlıyor ve artık uslanacağına söz veriyordu.", "Past continuous coordinates 'was sobbing and promising'."),
            ("'Will you give up motor-cars forever?' asked Ratty with great earnestness.", "'Otomobillerden sonsuza dek vazgeçecek misin?' diye sordu Ratty büyük bir ciddiyetle.", "Phrasal verb 'give up'; noun phrase 'great earnestness'."),
            ("Suddenly Toad straightened up, puffed out his chest, and grinned cheekily.", "Birdenbire Toad doğruldu, göğsünü kabarttı ve küstahça sırıttı.", "Coordinated actions 'straightened up, puffed out, grinned'."),
            ("'No!' shouted Toad defiantly, 'I love motor-cars more than life itself!'", "'Hayır!' diye haykırdı Toad meydan okurcasına, 'Otomobilleri hayatın kendisinden bile çok seviyorum!'", "Adverb 'defiantly'; comparative 'more than life itself'."),
            ("'Then we have only one choice,' said Badger calmly to his companions.", "'O halde önümüzde tek bir seçenek var,' dedi Porsuk dostlarına sakince.", "Direct speech; noun phrase 'only one choice'."),
            ("They carried the struggling toad up the grand stairs to his spacious bedroom.", "Çırpınan kurbağayı görkemli merdivenlerden yukarı, geniş yatak odasına taşıdılar.", "Participial adjective 'struggling'; directional phrase 'up the stairs'."),
            ("They locked the heavy door from the outside and pocketed the iron key.", "Ağır kapıyı dışarıdan kilitlediler ve demir anahtarı ceplerine attılar.", "Coordinate past verbs 'locked and pocketed'."),
            ("'We will guard him day and night until the poison leaves his mind,' said Badger.", "'Bu zehir aklından çıkana kadar gece gündüz başında nöbet tutacağız,' dedi Porsuk.", "Future modal 'will guard'; time clause 'until the poison leaves'."),
            ("Toad threw himself upon his soft bed, kicking and screaming with frustration.", "Toad kendisini yumuşak yatağının üzerine attı, hayal kırıklığıyla tepinip çığlıklar savurdu.", "Reflexive 'threw himself'; participle phrases 'kicking and screaming'."),
        ]
    },
    # Page 8: Toad's Escape and Car Theft (The Temptation at the Red Lion Inn)
    {
        "page_number": 8,
        "title": "Escape from the Bedroom",
        "vocab": [
            ("feign", "numara yapmak, taklit etmek"),
            ("sheet", "çarşaf"),
            ("inn", "han, meyhane"),
            ("temptation", "ayartma, nefse uyma"),
            ("crank", "manivela ile çalıştırmak"),
            ("unattended", "sahipsiz, gözetimsiz"),
            ("reckless", "pervasız, düşüncesiz"),
            ("arrogant", "kibirli, mağrur")
        ],
        "sentences": [
            ("Days passed, and Ratty took his turn guarding the imprisoned gentleman.", "Günler geçti ve hapsedilen beyefendiyi koruma sırası Ratty'ye geldi.", "Idiom 'took his turn'; participial adjective 'imprisoned gentleman'."),
            ("Toad pretended to be dangerously sick and groaned pathetically from his bed.", "Toad tehlikeli bir şekilde hastaymış gibi davrandı ve yatağından acıklı acıklı inledi.", "Verb + infinitive 'pretended to be'; adverb 'pathetically'."),
            ("'Dear Ratty, I am dying,' moaned Toad, 'fetch a lawyer and a doctor quickly!'", "'Sevgili Ratty, ölüyorum,' diye inledi Toad, 'çabuk bir avukat ve bir doktor çağır!'", "Present continuous 'am dying'; imperative 'fetch'."),
            ("Tender-hearted Ratty fell for the trick and hurried out to fetch assistance.", "Yufka yürekli Ratty bu oyuna kandı ve yardım getirmek için aceleyle dışarı koştu.", "Idiom 'fell for the trick'; compound adjective 'tender-hearted'."),
            ("As soon as the door closed, Toad leaped out of bed laughing maliciously.", "Kapı kapanır kapanmaz Toad şeytani kahkahalar atarak yataktan fırladı.", "Subordinate clause 'as soon as'; participle phrase 'laughing maliciously'."),
            ("He tied his bedsheets together and knotted one end to the heavy bedpost.", "Yatak çarşaflarını birbirine bağladı ve bir ucunu ağır karyola direğine düğümledi.", "Coordinate past verbs 'tied and knotted'."),
            ("He scrambled down the rope of linen onto the soft garden grass below.", "Keten ipten aşağı kayarak aşağıdaki yumuşak bahçe çimlerinin üzerine indi.", "Phrasal verb 'scrambled down'; noun phrase 'rope of linen'."),
            ("He ran through the orchards until he reached the town of Red Lion.", "Kızıl Aslan kasabasına ulaşana kadar meyve bahçelerinin içinden koştu.", "Preposition 'through'; time clause with 'until'."),
            ("He entered the Red Lion Inn and ordered a lavish hot lunch.", "Kırmızı Aslan Hanı'na girdi ve mükellef, sıcak bir öğle yemeği sipariş etti.", "Coordinate past verbs; adjective 'lavish'."),
            ("While he was eating, a familiar droning hum sounded outside in the courtyard.", "Yemek yerken dışarıdaki avludan tanıdık bir vızıltı uğultusu duyuldu.", "Time clause 'while he was eating'; adjective 'familiar'."),
            ("A gorgeous new motor-car pulled up, and the passengers walked in to dine.", "Muhteşem yeni bir otomobil yanaştı ve yolcular yemek yemek için içeri girdiler.", "Phrasal verb 'pulled up'; infinitive of purpose 'to dine'."),
            ("Toad slipped outside into the empty yard to admire the beautiful vehicle.", "Toad güzel araca hayranlıkla bakmak için boş avluya gizlice süzüldü.", "Phrasal verb 'slipped outside'; infinitive 'to admire'."),
            ("The engine was humming softly, waiting for a driver to command its power.", "Motor usulca mırıldanıyor, gücüne hükmedecek bir sürücüyü bekliyordu.", "Participle phrase 'waiting for a driver to command'."),
            ("'I will just sit in the driver's seat for one single minute,' whispered Toad.", "'Sürücü koltuğuna sadece bir tek dakikalığına oturacağım,' diye fısıldadı Toad.", "Future modal 'will sit'; time phrase 'for one minute'."),
            ("He touched the leather steering wheel, and a wild fire flared in his veins.", "Deri direksiyona dokundu ve damarlarında çılgın bir ateş alevlendi.", "Metaphor 'wild fire flared in his veins'; past verb 'touched'."),
            ("Before he knew what he was doing, he released the brake and pressed the pedal.", "Ne yaptığını bile anlamadan önce el frenini indirdi ve gaza bastı.", "Time clause 'before he knew'; coordinate past verbs."),
            ("The great car leaped forward through the archway onto the open highway.", "Büyük otomobil kemerli kapıdan geçerek açık ana yola doğru ileri fırladı.", "Phrasal verb 'leaped forward through'."),
            ("Toad laughed, sang, and shouted like an arrogant demon of speed.", "Toad hızın kibirli bir iblisi gibi güldü, şarkılar söyledi ve haykırdı.", "Coordinate past verbs; simile 'like an arrogant demon'."),
            ("He flew past wagons, frightened cattle, and pedestrians at reckless velocity.", "Pervasız bir hızla at arabalarının, korkmuş sığırların ve yayaların yanından uçup geçti.", "Preposition 'past'; prepositional phrase 'at reckless velocity'."),
            ("The law was waiting for him just around the next sharp turn.", "Kanun, hemen bir sonraki keskin virajın ardında onu bekliyordu.", "Past continuous 'was waiting'; prepositional phrase 'around the turn'."),
        ]
    },
    # Page 9: The Trial and the Dungeon (Toad Sentenced to Twenty Years)
    {
        "page_number": 9,
        "title": "The Sentence of the Court",
        "vocab": [
            ("court", "mahkeme"),
            ("magistrate", "yargıç, sulh hakimi"),
            ("handcuffs", "kelepçe"),
            ("dungeon", "zindan"),
            ("jailer", "gardiyan"),
            ("insolence", "küstahlık, saygısızlık"),
            ("sentence", "ceza vermek / mahkumiyet"),
            ("weep", "ağlamak, sızlanmak")
        ],
        "sentences": [
            ("Toad's wild joyride ended abruptly against a heavy oak tree in a ditch.", "Toad'un çılgın sefa sürüşü bir hendekteki ağır bir meşe ağacına çarparak aniden bitti.", "Prepositional phrase 'against a heavy oak tree'; adverb 'abruptly'."),
            ("He was surrounded by angry constables and dragged away in heavy iron handcuffs.", "Öfkeli polisler tarafından etrafı sarıldı ve ağır demir kelepçelerle sürüklenerek götürüldü.", "Passive voice coordinates 'was surrounded and dragged away'."),
            ("The courtroom was packed with outraged citizens and stern magistrates.", "Mahkeme salonu öfkeli yurttaşlar ve sert yargıçlarla dolup taşmıştı.", "Passive participle 'packed with'; coordinate adjectives."),
            ("The Chairman of the Bench adjusted his spectacles and glared at the prisoner.", "Heyet Başkanı gözlüklerini düzeltti ve mahkuma dik dik baktı.", "Coordinate past verbs 'adjusted and glared'."),
            ("'You have stolen a motor-car of immense value,' declared the Clerk of the Court.", "'Muazzam değerde bir otomobili çaldınız,' dedi Mahkeme Katibi.", "Present perfect 'have stolen'; noun phrase 'immense value'."),
            ("'You have driven dangerously and endangered innocent human lives.'", "'Tehlikeli araç kullandınız ve masum insan hayatlarını tehlikeye attınız.'", "Present perfect coordinates 'have driven and endangered'."),
            ("'And you were grossly insolent to the rural police officers who arrested you.'", "'Ve sizi tutuklayan kır polislerine karşı son derece saygısız davrandınız.'", "Past tense with adverb 'grossly insolent'; relative clause."),
            ("The magistrates calculated the penalties for each separate crime carefully.", "Yargıçlar her bir suçun cezasını ayrı ayrı dikkatle hesapladılar.", "Adverb 'carefully'; noun phrase 'separate crime'."),
            ("'Twelve months for the theft of the motor-car,' announced the Chairman solemnly.", "'Otomobil hırsızlığı için on iki ay,' diye duyurdu Başkan ciddiyetle.", "Adverb 'solemnly'; prepositional phrase 'for the theft'."),
            ("'Three years for reckless driving on the king's highway.'", "'Kralın anayolunda pervasız sürüş için üç yıl.'", "Prepositional phrase describing crime and duration."),
            ("'And fifteen years for your disgraceful insolence to the police.'", "'Ve polise karşı sergilediğiniz utanç verici küstahlık için on beş yıl.'", "Adjective 'disgraceful'; noun 'insolence'."),
            ("'Totaling twenty years in the darkest dungeon of the ancient castle!'", "'Toplamda kadim kalenin en karanlık zindanında yirmi yıl!'", "Participial phrase 'Totaling twenty years'; superlative 'darkest dungeon'."),
            ("Toad shrieked in absolute terror and fell on his knees begging for mercy.", "Toad tam bir dehşet içinde çığlık attı ve merhamet dileyerek dizlerinin üzerine çöktü.", "Coordinate past verbs; participle phrase 'begging for mercy'."),
            ("The guards seized him by both arms and dragged him through gloomy corridors.", "Muhafızlar onu iki kolundan yakaladı ve kasvetli koridorlar boyunca sürüklediler.", "Coordinate past actions; adjective 'gloomy'."),
            ("They crossed deep moats, clattering drawbridges, and heavy portcullises.", "Derin hendekleri, takırdayan asma köprüleri ve ağır demir kapıları geçtiler.", "Descriptive noun phrases with participles; past verb 'crossed'."),
            ("They thrust poor Toad into a damp, windowless dungeon under the ground.", "Zavallı Toad'u yer altındaki nemli, penceresiz bir zindana tıktılar.", "Past verb 'thrust'; coordinate adjectives 'damp, windowless'."),
            ("The heavy iron door slammed shut with a dreadful, final clang.", "Ağır demir kapı korkunç ve nihai bir madeni sesle kapandı.", "Resultative 'slammed shut'; adjective pair 'dreadful, final'."),
            ("Toad was left alone in pitch darkness with only rusty chains and cold straw.", "Toad zifiri karanlıkta sadece paslı zincirler ve soğuk samanlarla yapayalnız bırakıldı.", "Passive voice 'was left alone'; compound noun 'pitch darkness'."),
            ("He wept bitter tears of self-pity and cursed his foolish vanity.", "Kendine acımanın acı gözyaşlarını döktü ve aptalca kibrine lanetler yağdırdı.", "Coordinate past verbs 'wept and cursed'; noun phrase 'foolish vanity'."),
            ("It seemed that the great and splendid Mr. Toad would rot away forever.", "Görünüşe göre o muhteşem ve görkemli Bay Toad sonsuza dek çürüyüp gidecekti.", "Noun clause 'that Mr. Toad would rot away'; modal 'would rot'."),
        ]
    },
    # Page 10: The Washerwoman's Disguise (Escaping from the Dark Fortress)
    {
        "page_number": 10,
        "title": "The Washerwoman's Disguise",
        "vocab": [
            ("pity", "acımak, merhamet duymak"),
            ("disguise", "kılık değiştirmek / kılık"),
            ("apron", "önlük"),
            ("bonnet", "kadın başlığı"),
            ("wash", "yıkamak"),
            ("bribe", "rüşvet vermek / rüşvet"),
            ("gaoler", "gardiyan (eski yazım)"),
            ("clever", "zeki, kurnaz")
        ],
        "sentences": [
            ("Days turned into weeks, and Toad refused to eat, growing thinner daily.", "Günler haftalara döndü ve Toad yemek yemeyi reddederek günden güne zayıfladı.", "Coordinate clauses; participle clause 'growing thinner daily'."),
            ("The jailer's daughter was a kind girl who felt deep pity for the prisoner.", "Gardiyanın kızı, mahkuma derin bir merhamet duyan nazik bir kızdı.", "Relative clause 'who felt deep pity'; adjective 'kind'."),
            ("She brought him tea, buttered toast, and listened to his tragic stories.", "Ona çay ve tereyağlı kızarmış ekmek getirdi, trajik hikayelerini dinledi.", "Coordinate predicates; adjective 'tragic'."),
            ("Toad's spirits gradually revived under her warm sympathy and attention.", "Toad'un morali kızın sıcak sempatisi ve ilgisi sayesinde yavaş yavaş yerine geldi.", "Past verb 'revived'; prepositional phrase 'under sympathy and attention'."),
            ("One morning, the girl whispered an ingenious escape plan into his ear.", "Bir sabah kız, onun kulağına dahiyane bir kaçış planı fısıldadı.", "Adjective 'ingenious'; prepositional phrase 'into his ear'."),
            ("'My aunt is the castle washerwoman who washes linen for the garrison,' she said.", "'Teyzem garnizonun çamaşırlarını yıkayan kale çamaşırcısıdır,' dedi.", "Relative clause 'who washes linen'; compound noun 'castle washerwoman'."),
            ("'You can give her some gold coins and swap clothes with her.'", "'Ona biraz altın para verip kıyafetlerinizi onunla değiş tokuş edebilirsiniz.'", "Modal 'can give'; coordinate verb 'swap'."),
            ("The washerwoman was summoned, and for a few gold sovereigns she agreed.", "Çamaşırcı kadın çağrıldı ve birkaç altın lira karşılığında kabul etti.", "Passive voice 'was summoned'; prepositional phrase 'for gold sovereigns'."),
            ("Toad put on a cotton print dress, a battered bonnet, and an apron.", "Toad basma bir elbise, hırpalanmış bir kadın başlığı ve bir önlük giydi.", "Coordinate noun objects; adjectives 'print, battered'."),
            ("He carried a heavy basket full of dirty laundry over his arm.", "Kolunun üzerinde kirli çamaşırlarla dolu ağır bir sepet taşıdı.", "Adjective phrase 'full of dirty laundry'; past verb 'carried'."),
            ("With a beating heart, he shuffled past the stern castle guards at dusk.", "Alacakaranlıkta çarpan bir yürekle sert kale muhafızlarının yanından ayaklarını sürüyerek geçti.", "Prepositional phrase 'with a beating heart'; past verb 'shuffled past'."),
            ("'Good night, mother!' chuckled a sentry as Toad passed the iron gates.", "'İyi geceler ana!' diye kıkırdadı bir nöbetçi, Toad demir kapılardan geçerken.", "Direct speech; time clause with 'as'."),
            ("Toad curtsied awkwardly and hurried across the echoing drawbridge.", "Toad beceriksizce reverans yaptı ve yankılanan asma köprünün üzerinden aceleyle geçti.", "Adverb 'awkwardly'; participial adjective 'echoing drawbridge'."),
            ("Once outside the walls, he sprinted into the dark woods as fast as he could.", "Surların dışına çıkar çıkmaz, var gücüyle koşarak karanlık ormana daldı.", "Idiom 'as fast as he could'; phrasal verb 'sprinted into'."),
            ("He had escaped from the grim castle where no prisoner had ever escaped before.", "Daha önce hiçbir mahkumun kaçamadığı o kasvetli kaleden kaçmayı başarmıştı.", "Past perfect 'had escaped'; relative clause 'where no prisoner had escaped'."),
            ("He reached a railway station just as a passenger train was preparing to depart.", "Bir yolcu treni kalkmaya hazırlanırken tam vaktinde bir tren istasyonuna vardı.", "Time clause 'just as train was preparing'; infinitive 'to depart'."),
            ("To his horror, he realized he had left his purse in the prison cell.", "Dehşet içinde, para cüzdanını hapishane hücresinde unuttuğunu fark etti.", "Noun clause 'he had left his purse'; prepositional phrase 'to his horror'."),
            ("He pleaded with the engine-driver, weeping in his washerwoman disguise.", "Çamaşırcı kadın kılığı içinde ağlayarak makinistin ayaklarına kapandı.", "Participle phrase 'weeping in disguise'; phrasal verb 'pleaded with'."),
            ("The kind driver took pity on the supposed old woman and hid him in the tender.", "Müşfik makinist o sözde yaşlı kadına acıdı ve onu kömür vagonuna sakladı.", "Idiom 'took pity on'; past verb 'hid'."),
            ("Toad steamed away into the night, free once more to seek his destiny.", "Toad gecenin içine doğru trenle yol alarak kaderini aramak üzere bir kez daha özgür kaldı.", "Phrasal verb 'steamed away'; infinitive of purpose 'to seek his destiny'.")
        ]
    },
    # Page 11: The Barge-Woman and the Stolen Horse (Toad's Adventures on the Canal)
    {
        "page_number": 11,
        "title": "Adventures on the Canal",
        "vocab": [
            ("canal", "su kanalı"),
            ("barge", "mavna, yük teknesi"),
            ("towpath", "çekek yolu, kanal boyu patika"),
            ("horse", "at"),
            ("drown", "boğulmak / boğmak"),
            ("vanity", "kibir, gösteriş merakı"),
            ("bargain", "pazarlık etmek / anlaşma"),
            ("gypsy", "çingene")
        ],
        "sentences": [
            ("The next morning, Toad walked beside a tranquil canal bordered by willows.", "Ertesi sabah Toad, söğütlerle çevrili sakin bir su kanalının kenarında yürüdü.", "Passive participle modifier 'bordered by willows'; adjective 'tranquil'."),
            ("A long barge glided along, towed by a heavy piebald horse on the path.", "Patikadaki alacalı ağır bir atın çektiği uzun bir mavna suyun üzerinde süzülüyordu.", "Passive participle modifier 'towed by'; adjective 'piebald'."),
            ("A fat, good-natured barge-woman sat at the rudder smoking a short clay pipe.", "Kısa kilden bir pipo tüttüren şişman, iyi huylu bir mavnacı kadın dümende oturuyordu.", "Participle clause 'smoking a clay pipe'; compound adjective 'good-natured'."),
            ("'A fine morning, mother!' called the woman, seeing Toad's washerwoman dress.", "'Güzel bir sabah ana!' diye seslendi kadın, Toad'un çamaşırcı kadın elbisesini görünce.", "Participial clause of perception 'seeing Toad's dress'."),
            ("Toad accepted her offer of a ride and stepped aboard the slow barge.", "Toad kadının tekneye binme teklifini kabul etti ve yavaş mavnaya bindi.", "Coordinate past verbs 'accepted and stepped aboard'."),
            ("The woman soon asked Toad to wash a pile of laundry to pay for his passage.", "Kadın çok geçmeden yol parasını ödemesi için Toad'dan bir yığın çamaşır yıkamasını istedi.", "Verb + object + infinitive 'asked Toad to wash'; purpose phrase 'to pay for'."),
            ("Toad, who had never done honest labor, scrubbed awkwardly with disastrous results.", "Hayatında dürüstçe tek bir iş bile yapmamış olan Toad, felaket sonuçlarla beceriksizce çamaşır çitiledi.", "Relative clause 'who had never done...'; adverb 'awkwardly'."),
            ("He tangled the shirts, spilled soapy water everywhere, and tore a tablecloth.", "Gömlekleri birbirine doladı, sabunlu suyu her yere döktü ve bir masa örtüsünü yırttı.", "Series of past verbs describing ineptitude."),
            ("The furious barge-woman burst out laughing and guessed he was an impostor.", "Öfkeli mavnacı kadın kahkahayı bastı ve onun bir sahtekar olduğunu anladı.", "Idiom 'burst out laughing'; noun clause 'he was an impostor'."),
            ("She seized him by the collar and tossed him headlong into the muddy canal.", "Onu yakasından kavradı ve çamurlu kanalın içine tepeüstü fırlattı.", "Coordinate past actions; adverb 'headlong'."),
            ("Toad splashed, choked, and swam angrily to the opposite towpath.", "Toad sular sıçrattı, tıkandı ve öfkeyle karşı çekek yoluna doğru yüzdü.", "Coordinate verbs 'splashed, choked, swam'; adverb 'angrily'."),
            ("Soaked to the skin, his pride was wounded worse than his soggy body.", "İliğine kadar ıslanmıştı; gururu sırılsıklam gövdesinden bile daha kötü yaralanmıştı.", "Comparative passive 'was wounded worse than'; participle modifier 'soaked to the skin'."),
            ("He saw the barge-horse tethered nearby and untied the halter in revenge.", "Yakına bağlanmış mavna atını gördü ve intikam almak için yularını çözdü.", "Coordinate past verbs; purpose phrase 'in revenge'."),
            ("He mounted the heavy animal and galloped away along the canal bank.", "Ağır hayvanın sırtına bindi ve kanal kıyısı boyunca dörtnala uzaklaştı.", "Coordinate past actions; phrasal verb 'galloped away'."),
            ("Down the road, he encountered an old gypsy cooking breakfast by a caravan.", "Yolun ilerisinde, bir karavanın yanında kahvaltı pişiren yaşlı bir çingene ile karşılaştı.", "Participle phrase 'cooking breakfast'; past verb 'encountered'."),
            ("After a fierce bargaining session, Toad sold the stolen horse for six shillings and a hot pie.", "Çetin bir pazarlık faslının ardından Toad, çalınan atı altı şilin ve sıcak bir börek karşılığında sattı.", "Prepositional phrase 'after bargaining'; past verb 'sold'."),
            ("Eating the warm meat pie, Toad felt his old arrogant pride returning in full force.", "Sıcak etli böreği yerken Toad, o eski kibirli gururunun tüm gücüyle geri döndüğünü hissetti.", "Participle clause 'eating the pie'; perception verb + participle 'felt pride returning'."),
            ("'I am Toad the Great, the clever, the undefeated!' he sang loudly.", "'Ben Muhteşem, zeki ve yenilmez Toad'um!' diye yüksek sesle şarkı söyledi.", "Direct speech; series of proud epithets."),
            ("He strode through the countryside, heading proudly back toward Toad Hall.", "Kırsal alanda gururla adımlar atarak başı dik bir şekilde Toad Konağı'na doğru yöneldi.", "Irregular past 'strode'; participle phrase 'heading proudly toward'."),
            ("Little did he know what terrible disaster had fallen upon his ancestral home.", "Atalarından kalma evinin başına nasıl korkunç bir felaketin geldiğinden hiç mi hiç haberi yoktu.", "Inverted negative structure 'Little did he know'; past perfect relative clause.")
        ]
    },
    # Page 12: The Fall of Toad Hall (Weasels and Stoats Take Over the Mansion)
    {
        "page_number": 12,
        "title": "The Captured Hall",
        "vocab": [
            ("ancestral", "atalardan kalma"),
            ("capture", "ele geçirmek, zaptetmek"),
            ("weasel", "gelincik"),
            ("ferret", "dağ gelinciği / kokarca"),
            ("garrison", "garnizon kurmak"),
            ("disaster", "felaket"),
            ("weep", "ağlamak"),
            ("humiliation", "aşağılanma, zillet")
        ],
        "sentences": [
            ("As Toad drew near his beloved estate, he stopped at Ratty's river home first.", "Toad çok sevdiği mülküne yaklaşırken, önce Ratty'nin nehir evinde durdu.", "Time clause 'as Toad drew near'; ordinal 'first'."),
            ("Water Rat opened the door and gasped in utter bewilderment at the washerwoman.", "Su Sıçanı kapıyı açtı ve çamaşırcı kadın karşısında tam bir şaşkınlıkla nefesini tuttu.", "Coordinate past verbs 'opened and gasped'; noun phrase 'utter bewilderment'."),
            ("'Toad!' cried Ratty, 'is it truly you, dressed in those horrible muddy rags?'", "'Toad!' diye haykırdı Ratty, 'o korkunç çamurlu paçavralar içindeki gerçekten sen misin?'", "Direct question; participial phrase 'dressed in rags'."),
            ("Toad strutted inside, threw off his bonnet, and began bragging about his adventures.", "Toad kasılarak içeri girdi, başlığını fırlatıp attı ve maceralarıyla övünmeye başladı.", "Coordinate past verbs; phrasal verb 'bragging about'."),
            ("'I escaped prison, fooled everyone, stole a horse, and outsmarted the world!' he boasted.", "'Hapisten kaçtım, herkesi kandırdım, bir at çaldım ve bütün dünyayı alt ettim!' diye böbürlendi.", "Series of past tense claims; transitive verb 'outsmarted'."),
            ("Ratty looked at him with sad, troubled eyes and shook his head gravely.", "Ratty ona hüzünlü, kederli gözlerle baktı ve başını ciddiyetle salladı.", "Prepositional phrase 'with sad eyes'; adverb 'gravely'."),
            ("'Stop your foolish bragging, Toad,' said Rat quietly, 'you do not know the news.'", "'Aptalca böbürlenmeyi kes Toad,' dedi Rat sessizce, 'haberlerden haberin yok.'", "Imperative 'stop your bragging'; negative present 'do not know'."),
            ("'What news?' demanded Toad, suddenly feeling a cold dread in his stomach.", "'Ne haberi?' diye sordu Toad, birdenbire midesinde soğuk bir korku hissederek.", "Transitive past 'demanded'; participle phrase 'feeling a cold dread'."),
            ("'Toad Hall has been captured,' whispered the Water Rat with deep sorrow.", "'Toad Konağı ele geçirildi,' diye fısıldadı Su Sıçanı derin bir üzüntüyle.", "Present perfect passive 'has been captured'; prepositional phrase 'with deep sorrow'."),
            ("'The Wild Wooders took advantage of your imprisonment to seize your estate.'", "'Vahşi Ormanlılar mülkünü zapt etmek için senin hapsedilmenden faydalandılar.'", "Idiom 'took advantage of'; infinitive of purpose 'to seize'."),
            ("'Weasels, stoats, and ferrets marched in with rifles and clubs one dark night.'", "'Gelincikler, kakımlar ve kokarcalar karanlık bir gece tüfekler ve sopalarla içeri daldılar.'", "Compound subject; prepositional phrase 'with rifles and clubs'."),
            ("'Badger and I tried to defend it, but they were too numerous and drove us out.'", "'Porsuk ve ben orayı savunmaya çalıştık fakat çok kalabalıktılar ve bizi dışarı sürdüler.'", "Coordinate clauses; phrasal verb 'drove us out'."),
            ("Toad collapsed into a chair, wailing loudly and tearing at his hair.", "Toad avazı çıktığı kadar bağırıp saçını başını yolarak bir sandalyeye yığıldı.", "Coordinate participles 'wailing loudly and tearing'."),
            ("'My beautiful home!' sobbed Toad, 'the banqueting hall! The wine cellars!'", "'Benim güzel evim!' diye hıçkırdı Toad, 'ziyafet salonu! Şarap mahzenleri!'", "Exclamatory noun phrases; past verb 'sobbed'."),
            ("'They are eating your food, drinking your wine, and mocking your name,' said Rat.", "'Senin yiyeceklerini yiyorlar, şarabını içiyorlar ve senin adınla alay ediyorlar,' dedi Rat.", "Parallel present continuous verbs; possessive determiners."),
            ("Just then, Mr. Badger and Mole walked into the room, covered with dust and bandages.", "Tam o sırada Bay Porsuk ve Mole, toz ve sargılar içinde odaya girdiler.", "Time phrase 'just then'; passive participle modifier 'covered with dust'."),
            ("Badger held a thick stick and nodded grimly to the weeping owner of Toad Hall.", "Porsuk kalın bir sopa tutuyordu ve Toad Konağı'nın ağlayan sahibine sertçe başını salladı.", "Coordinate past verbs 'held and nodded'; participial adjective 'weeping owner'."),
            ("'Welcome home, Toad,' said Badger, 'now dry your tears and listen to me.'", "'Evine hoş geldin Toad,' dedi Porsuk, 'şimdi gözyaşlarını kurula ve beni dinle.'", "Imperative coordinate clauses 'dry tears and listen'."),
            ("'We cannot attack the front gates against rifles, but there is a secret way.'", "'Tüfeklere karşı ön kapılara saldıramayız fakat gizli bir yol var.'", "Modal negative 'cannot attack'; existential 'there is'."),
            ("Toad looked up through his swollen eyes, hope rekindling in his bruised heart.", "Toad şişmiş gözlerinin arasından yukarı baktı; hırpalanmış kalbinde umut yeniden yeşerdi.", "Absolute participle clause 'hope rekindling'; adjective 'swollen'."),
        ]
    },
    # Page 13: The Secret Tunnel (Badger's Battle Plan Beneath the River)
    {
        "page_number": 13,
        "title": "The Secret Passage",
        "vocab": [
            ("tunnel", "tünel"),
            ("butler", "kahya, uşak"),
            ("pantry", "kiler"),
            ("scoundrel", "alçak, rezil"),
            ("arm", "silahlandırmak"),
            ("cutlass", "kısa kılıç, pala"),
            ("revelry", "alem, cümbüş"),
            ("stealth", "gizlilik, sinsilik")
        ],
        "sentences": [
            ("Badger sat at the table and leaned forward with an air of absolute secrecy.", "Porsuk masaya oturdu ve tam bir gizlilik havasıyla öne doğru eğildi.", "Coordinate past verbs 'sat and leaned'; noun phrase 'air of secrecy'."),
            ("'Toad's late father showed me a secret tunnel before he died,' whispered Badger.", "'Toad'un merhum babası ölmeden önce bana gizli bir tünel göstermişti,' diye fısıldadı Porsuk.", "Time clause 'before he died'; past perfect / simple past."),
            ("'The tunnel leads from the riverbank directly into the butler's pantry.'", "'Tünel nehir kıyısından dosdoğru kahyanın kilerine çıkıyor.'", "Present tense description; directional phrase 'directly into'."),
            ("'Even Toad himself does not know about this subterranean passageway.'", "'Toad'un kendisi bile bu yeraltı geçidinden haberdar değil.'", "Emphatic reflexive 'Toad himself'; adjective 'subterranean'."),
            ("Toad looked astonished, but remained silent under Badger's severe glare.", "Toad şaşkına döndü ama Porsuk'un sert bakışı altında sessizliğini korudu.", "Coordinate predicates; adjective 'astonished'."),
            ("'Tonight,' continued Badger, 'the Chief Weasel gives a grand banquet to celebrate his victory.'", "'Bu gece,' diye devam etti Porsuk, 'Baş Gelincik zaferini kutlamak için büyük bir ziyafet veriyor.'", "Infinitive of purpose 'to celebrate'; title 'Chief Weasel'."),
            ("'All the weasels will be feasting, drinking, and unarmed in the great hall.'", "'Bütün gelincikler büyük salonda ziyafet çekiyor, içki içiyor ve silahsız olacaklar.'", "Future continuous predicates; coordinate adjectives."),
            ("'Only a few sentries will guard the outer gates and windows.'", "'Sadece birkaç nöbetçi dış kapılarda ve pencerelerde nöbet tutacak.'", "Future modal 'will guard'; adjective 'outer'."),
            ("'We four will enter through the secret pantry and fall upon them like thunder!'", "'Biz dördümüz gizli kilerden gireceğiz ve gök gürültüsü gibi üzerlerine çökeceğiz!'", "Simile 'like thunder'; phrasal verb 'fall upon'."),
            ("The friends spent the rest of the day cleaning weapons and preparing gear.", "Dostlar günün geri kalanını silahları temizleyerek ve teçhizatı hazırlayarak geçirdiler.", "Expression 'spent the day doing'; coordinate gerunds."),
            ("Ratty provided each hero with a sword, a cutlass, a pistol, and a heavy cudgel.", "Ratty her kahramana bir kılıç, bir pala, bir tabanca ve ağır bir sopa temin etti.", "Transitive verb 'provided with'; list of weaponry."),
            ("Mole scouted the edge of the estate in disguise and spread clever false rumors.", "Mole kılık değiştirerek mülkün sınırında keşif yaptı ve akıllıca sahte söylentiler yaydı.", "Coordinate past verbs; compound noun 'false rumors'."),
            ("He tricked the sentries into believing that hundreds of badgers were approaching from the north.", "Nöbetçileri kuzeyden yüzlerce porsuğun yaklaştığına inandırarak kandırdı.", "Idiom 'tricked into believing'; relative clause."),
            ("Night fell, dark, overcast, and silent over the winding river.", "Kıvrıla kıvrıla akan nehrin üzerine gece karanlık, kapalı ve sessizce çöktü.", "Coordinate adjectives 'dark, overcast, silent'; past verb 'fell'."),
            ("The four companions slipped into a small rowboat and glided along the shore.", "Dört yoldaş küçük bir sandala bindiler ve kıyı boyunca süzüldüler.", "Phrasal verb 'slipped into'; coordinate past 'glided'."),
            ("Beneath a curtain of heavy hanging roots, Badger parted the bushes.", "Ağır sarkan köklerden bir perdenin altında Porsuk çalıları araladı.", "Prepositional phrase 'beneath a curtain'; past verb 'parted'."),
            ("A low brick archway opened into the deep, mysterious black subterranean tunnel.", "Alçak tuğla bir kemer, derin ve gizemli kara yeraltı tüneline doğru açılıyordu.", "Adjective string 'deep, mysterious black subterranean'; past verb 'opened'."),
            ("They crawled inside in single file, feeling their way along wet, slimy walls.", "Islak, sümüksü duvarlar boyunca yollarını el yordamıyla bularak tek sıra halinde içeri süründüler.", "Participle phrase 'feeling their way'; manner phrase 'in single file'."),
            ("From ahead, they could hear the faint sounds of music, stamping feet, and wild laughter.", "İleriden müziğin, tepinen ayakların ve çılgın kahkahaların hafif seslerini duyabiliyorlardı.", "Modal perception 'could hear'; list of sounds."),
            ("The hour of retribution for the invaders of Toad Hall had finally arrived.", "Toad Konağı'nı işgal edenler için intikam saati nihayet gelip çatmıştı.", "Past perfect 'had finally arrived'; noun phrase 'hour of retribution'."),
        ]
    },
    # Page 14: The Battle for Toad Hall (Four Friends Reclaim the Great Hall)
    {
        "page_number": 14,
        "title": "The Battle for the Hall",
        "vocab": [
            ("retribution", "hak edilen ceza, intikam"),
            ("cudgel", "kalın sopa, cop"),
            ("rout", "bozguna uğratmak"),
            ("flee", "kaçmak, firar etmek"),
            ("paralyze", "felç etmek, dondurmak"),
            ("scramble", "apar topar kaçışmak"),
            ("reclaim", "geri almak, geri kazanmak"),
            ("triumph", "büyük zafer")
        ],
        "sentences": [
            ("The four companions reached the pantry door and paused to listen closely.", "Dört yoldaş kiler kapısına ulaştılar ve dikkatle dinlemek için durakladılar.", "Coordinate past verbs; infinitive of purpose 'to listen'."),
            ("Inside the banqueting hall, a weasel was singing an insulting song about Mr. Toad.", "Ziyafet salonunun içinde bir gelincik Bay Toad hakkında hakaret dolu bir şarkı söylüyordu.", "Past continuous 'was singing'; participial adjective 'insulting'."),
            ("The audience of stoats and ferrets banged their mugs and cheered insolently.", "Kakımlar ve kokarcalardan oluşan dinleyiciler kupalarını masaya vuruyor ve küstahça alkışlıyordu.", "Coordinate past verbs 'banged and cheered'."),
            ("Toad's green skin turned dark with fury, and his eyes bulged dangerously.", "Toad'un yeşil derisi öfkeden karardı ve gözleri tehlikeli bir şekilde yuvalarından fırladı.", "Coordinate clauses; past verb 'bulged'."),
            ("'The hour has struck!' roared Badger, 'follow me, and give no quarter!'", "'Vakit tamamdır!' diye kükredi Porsuk, 'beni takip edin ve aman vermeyin!'", "Imperative coordinates; idiom 'give no quarter'."),
            ("Badger flung open the pantry door and charged into the brightly lit hall.", "Porsuk kiler kapısını ardına kadar açtı ve ışıl ışıl aydınlatılmış salona hücum etti.", "Coordinate past verbs 'flung open and charged'."),
            ("He brandished his mighty cudgel, striking down weasels with terrible force.", "Kudretli sopasını savurdu, korkunç bir kuvvetle gelincikleri yere serdi.", "Participle phrase 'striking down weasels'; past verb 'brandished'."),
            ("Ratty followed with gleaming cutlass, his whiskers bristling with warlike rage.", "Ratty parıldayan palasıyla onu takip etti, bıyıkları savaşçı bir öfkeyle dikelmişti.", "Absolute construction 'his whiskers bristling'; adjective 'warlike'."),
            ("Mole whirled his quarterstaff like a windmill, shouting his battle cry.", "Mole savaş naraları atarak değneğini bir yel değirmeni gibi fırıl fırıl döndürdü.", "Simile 'like a windmill'; participle phrase 'shouting battle cry'."),
            ("And Toad, roaring with the fury of twenty toads, leaped straight at the Chief Weasel.", "Ve yirmi kurbağanın öfkesiyle kükreyen Toad, dosdoğru Baş Gelincik'in üzerine atladı.", "Participial phrase 'roaring with fury'; past verb 'leaped straight at'."),
            ("The invaders were struck with sheer paralyzing panic at the sudden onslaught.", "İşgalciler bu ani saldırı karşısında katıksız, felç edici bir panikle donakaldılar.", "Passive voice 'were struck with'; adjective 'paralyzing'."),
            ("They thought a hundred furious monsters had dropped from the ceiling upon them.", "Üzerlerine tavandan yüzlerce öfkeli canavarın indiğini sandılar.", "Noun clause with past perfect 'had dropped upon them'."),
            ("Tables overturned, goblets smashed, and candles were extinguished in the chaos.", "Masalar devrildi, kadehler kırıldı ve kargaşada mumlar söndü.", "Series of passive past clauses describing total chaos."),
            ("Weasels and stoats dove through windows, scrambled up chimneys, and squeezed into drains.", "Gelincikler ve kakımlar pencerelerden atladılar, bacalara tırmandılar ve su giderlerine sıkıştılar.", "Series of past action verbs; directional prepositions."),
            ("In less than ten minutes, the magnificent hall was completely cleared of enemies.", "On dakikadan daha az bir sürede görkemli salon düşmanlardan tamamen temizlendi.", "Time phrase 'in less than ten minutes'; passive 'was cleared of'."),
            ("The Chief Weasel lay helpless on the floor, tied hand and foot by Mole.", "Baş Gelincik, Mole tarafından eli ayağı bağlanmış halde yerde çaresiz yatıyordu.", "Past participle modifier 'tied hand and foot'; adjective 'helpless'."),
            ("Toad leaped upon the highest table and shouted for pure uncontrollable joy.", "Toad en yüksek masanın üzerine zıpladı ve katıksız, zaptedilemez bir sevinçle haykırdı.", "Prepositional phrase 'for pure joy'; superlative 'highest table'."),
            ("'The Hall is ours once more!' he cried, 'Toad has vanquished all foes!'", "'Konak bir kez daha bizim oldu!' diye haykırdı, 'Toad bütün düşmanları yendi!'", "Present perfect 'has vanquished'; exclamatory direct speech."),
            ("Badger wiped his sweaty brow and smiled through his battle-worn gray whiskers.", "Porsuk terli alnını sildi ve savaştan yıpranmış gri bıyıklarının arasından gülümsedi.", "Coordinate past verbs; compound adjective 'battle-worn'."),
            ("The ancestral home of the Toad family was reclaimed forever by true friendship.", "Toad ailesinin atalardan kalma evi, gerçek dostluk sayesinde sonsuza dek geri alınmıştı.", "Passive voice 'was reclaimed'; cause phrase 'by true friendship'.")
        ]
    },
    # Page 15: Return of the Master of Toad Hall (Repentance, Honor, and Everlasting Friendship)
    {
        "page_number": 15,
        "title": "The Master of Toad Hall",
        "vocab": [
            ("repentance", "pişmanlık, tövbe"),
            ("humble", "alçakgönüllü"),
            ("banquet", "ziyafet, şölen"),
            ("gratitude", "şükran, minnettarlık"),
            ("compliment", "iltifat"),
            ("modest", "mütevazı"),
            ("unshakable", "sarsılmaz"),
            ("everlasting", "ebedi, sonsuz")
        ],
        "sentences": [
            ("The following morning, sunlight poured through the cleaned stained-glass windows of Toad Hall.", "Ertesi sabah, güneş ışığı Toad Konağı'nın temizlenmiş vitraylı pencerelerinden içeri doldu.", "Past verb 'poured through'; compound noun 'stained-glass windows'."),
            ("The captured weasels were put to work scrubbing the floors and repairing the damage.", "Esir alınan gelincikler yerleri ovma ve hasarı onarma işine koşuldular.", "Passive idiom 'were put to work'; coordinate gerunds."),
            ("Toad wanted to compose a long, boastful song praising his own heroic victory.", "Toad kendi kahramanca zaferini öven uzun, övüngen bir şarkı bestelemek istedi.", "Verb + infinitive 'wanted to compose'; participial phrase 'praising victory'."),
            ("Mr. Badger took him aside and looked at him with stern, affectionate eyes.", "Bay Porsuk onu bir kenara çekti ve ona sert fakat şefkatli gözlerle baktı.", "Coordinate past verbs 'took aside and looked'; coordinate adjectives."),
            ("'No songs, Toad,' said Badger firmly, 'no speeches and no foolish boasting.'", "'Şarkı yok Toad,' dedi Porsuk kararlılıkla, 'konuşma yok ve aptalca böbürlenmek yok.'", "Repeated negative determiner 'no'; adverb 'firmly'."),
            ("'You must show true humility and gratitude to those who saved your honor.'", "'Onurunu kurtaranlara karşı gerçek bir alçakgönüllülük ve minnet göstermelisin.'", "Modal obligation 'must show'; relative clause 'who saved your honor'."),
            ("Toad bowed his head, swallowed his vanity, and accepted the wise bear-like advice.", "Toad başını öne eğdi, kibrini yuttu ve bu bilgece porsuk nasihatini kabul etti.", "Series of past verbs showing genuine transformation."),
            ("That evening, a grand banquet was given for all the friendly animals of the river.", "O akşam, nehrin tüm dost canlısı hayvanları için görkemli bir ziyafet verildi.", "Passive voice 'was given'; prepositional phrase 'for friendly animals'."),
            ("Mole, Ratty, and Badger sat in places of honor beside the reformed host.", "Mole, Ratty ve Porsuk, uslanmış ev sahibinin yanında şeref köşelerine oturdular.", "Compound subject; participial adjective 'reformed host'."),
            ("When the guests praised Toad, he simply smiled modestly and pointed to his friends.", "Konuklar Toad'u övdüklerinde, o sadece mütevazı bir tebessüm etti ve dostlarını işaret etti.", "Time clause 'when guests praised'; adverbs 'simply, modestly'."),
            ("'It was they who planned, fought, and won,' said Toad with quiet sincerity.", "'Planlayan, savaşan ve kazanan onlardı,' dedi Toad sessiz bir samimiyetle.", "Cleft sentence 'It was they who...'; prepositional phrase 'with sincerity'."),
            ("The whole company cheered loudly for the new, wiser, and humble Mr. Toad.", "Bütün davetliler yeni, daha bilge ve alçakgönüllü Bay Toad için coşkuyla tezahürat yaptı.", "Adjective comparative list 'new, wiser, humble'."),
            ("Later that night, the three river friends walked down the avenue under silver moonlight.", "O gecenin ilerleyen saatlerinde, üç nehir dostu gümüşi ay ışığı altında ağaçlıklı yoldan aşağı yürüdüler.", "Time phrase 'later that night'; compound noun 'silver moonlight'."),
            ("The peaceful water of the river lapped gently against the grassy banks.", "Nehrin huzurlu suyu otlu kıyılara karşı tatlı tatlı çırpındı.", "Adverb 'gently'; prepositional phrase 'against grassy banks'."),
            ("Mole took Ratty's paw and smiled with profound, peaceful contentment.", "Mole, Ratty'nin patisini tuttu ve derin, huzurlu bir memnuniyetle gülümsedi.", "Coordinate adjectives 'profound, peaceful'; noun 'contentment'."),
            ("'There is nothing half so much worth doing as simply messing about in boats,' murmured Rat.", "'Şu dünyada kayıklarla öylesine oyalanmak kadar yapmaya değer hiçbir şey yoktur,' diye mırıldandı Rat.", "Famous signature quotation from the classic book."),
            ("Mole agreed with all his heart as they looked out over the sparkling stream.", "Işıl ışıl parlayan akarsuya bakarlarken Mole tüm kalbiyle buna katıldı.", "Idiom 'with all his heart'; time clause with 'as'."),
            ("The Wild Wood was quiet, and peace had returned to the beloved countryside.", "Vahşi Orman sessizdi ve çok sevilen kırsala barış geri dönmüştü.", "Coordinate clauses; past perfect 'had returned'."),
            ("The bonds of their unshakable friendship were sealed forever by the singing water.", "Onların sarsılmaz dostluk bağları, şarkı söyleyen suyun kıyısında sonsuza dek mühürlenmişti.", "Passive voice 'were sealed forever'; participial adjective 'singing water'."),
            ("And so they lived on in honor, joy, and comradeship beside the whispering willows.", "Ve böylece fısıldayan söğütlerin yanı başında onur, neşe ve yoldaşlık içinde yaşamaya devam ettiler.", "Concluding coordinate nouns 'honor, joy, and comradeship'; participial adjective 'whispering willows'.")
        ]
    }
]

def generate_data_file():
    data_path = os.path.join(os.path.dirname(__file__), "book_15_data.py")
    
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
        f.write('"""\nBook 15: The Wind in the Willows (Kenneth Grahame)\n')
        f.write('Level 1 Graded Reader — 15 Pages x 20 Sentences = 300 Sentences.\n"""\n\n')
        f.write('BOOK_TITLE = "The Wind in the Willows (15 Sayfa / 300 Cümle / Graded Reader)"\n')
        f.write('AUTHOR = "Kenneth Grahame"\n\n')
        f.write(f"PAGES_DATA = {pprint.pformat(pages_data, indent=4, width=120)}\n")
        
    print(f"Successfully wrote {data_path}")

if __name__ == "__main__":
    generate_data_file()
