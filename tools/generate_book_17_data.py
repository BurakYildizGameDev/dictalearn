"""
Book 17 Generator: The Merry Adventures of Robin Hood (Howard Pyle)
15 Pages, exactly 20 sentences per page = 300 sentences total.
8 Target vocabulary terms per page = 120 vocabulary items total.
Level 1 / Seviye 1 Graded Reader for English learners.
"""

import os
import pprint

BOOK_META = {
    "id": "book_17_the_merry_adventures_of_robin_hood",
    "title": "The Merry Adventures of Robin Hood",
    "subtitle": "Howard Pyle's Classic Legend of Sherwood Forest, Justice, and Brotherhood",
    "author": "Howard Pyle",
    "level": "Seviye 1 (A1-A2 Beginner)",
    "target_readers": "İngilizce öğrenenler ve ortaçağ kahramanlık efsanelerini sevenler için çift dilli okuma kitabı",
    "total_pages": 15,
    "sentences_per_page": 20,
    "total_sentences": 300,
    "theme_color_primary": "#15803D",    # Sherwood Forest Green
    "theme_color_secondary": "#A16207",  # Lincoln Oak Brown / Gold
    "theme_color_accent": "#B91C1C",     # King's Crimson
    "theme_color_light": "#F0FDF4"       # Soft Forest Glade Tint
}

TR_TITLES = [
    "Robin Hood'un Kanun Kaçağı Oluşu",
    "Köprüdeki Dövüş ve Küçük John",
    "Nottingham'ın Altın Oku",
    "Nehirdeki Keşiş Friar Tuck",
    "Ormandaki Hüzünlü Şövalye",
    "Şerif'in Sherwood Ziyareti",
    "Küçük John Panayırda",
    "Kasap Arabası ve Şerif'in Oyunu",
    "Lehimci ve Kraliyet Fermanı",
    "İpek Giysili Will Scarlet",
    "Allan a Dale'in Düğünü",
    "Gümüş Av Borusunun Sesi",
    "Kral Aslan Yürekli Richard",
    "Kraliyet Sarayı ve Okçuluk",
    "Yeşil Ormanın Ebedi Efsanesi"
]

PAGES = [
    # Page 1: How Robin Hood Came to Be an Outlaw
    {
        "page_number": 1,
        "title": "How Robin Came to Sherwood",
        "vocab": [
            ("outlaw", "kanun kaçağı"),
            ("forester", "ormancı, korucu"),
            ("wager", "iddia, bahis"),
            ("deer", "geyik"),
            ("venison", "geyik eti"),
            ("shaft", "ok sapı/oku"),
            ("flee", "kaçmak"),
            ("bowman", "okçu")
        ],
        "sentences": [
            ("In merry England in the time of old, when good King Henry the Second ruled, lived Robin Hood.", "Eski günlerin neşeli İngiltere'sinde, iyi kalpli İkinci Kral Henry hüküm sürerken, Robin Hood yaşardı.", "Past time phrase; relative time clause 'when King Henry ruled'."),
            ("Robin was a youth of eighteen, tall and straight, with limbs as strong as oak trees.", "Robin on sekiz yaşında, meşe ağaçları kadar güçlü kolları bacakları olan uzun boylu ve dimdik bir gençti.", "Simile 'as strong as oak trees'; appositive description."),
            ("No archer in all Nottinghamshire could draw a cloth-yard shaft with such deadly precision.", "Bütün Nottinghamshire'da hiçbir okçu bir arşınlık oku böylesine ölümcül bir isabetle çekemezdi.", "Negative subject 'no archer'; measurement 'cloth-yard shaft'."),
            ("One bright morning in May, Robin set out toward Nottingham town with his trusty yew bow.", "Mayıs ayının pırıl pırıl bir sabahında Robin, emektar porsuk ağacı yayıyla Nottingham kasabasına doğru yola çıktı.", "Phrasal verb 'set out toward'; compound adjective 'trusty yew bow'."),
            ("The Sheriff of Nottingham had proclaimed a great archery shooting match for a prize.", "Nottingham Şerifi, bir ödül karşılığında büyük bir okçuluk yarışması ilan etmişti.", "Past perfect 'had proclaimed'; noun phrase 'archery shooting match'."),
            ("As Robin strode whistling through Sherwood Forest, he met fifteen royal foresters feasting on beer.", "Robin ıslık çalarak Sherwood Ormanı'nda adımlarken, bira içip ziyafet çeken on beş kraliyet korucusuyla karşılaştı.", "Time clause with 'as'; participle clauses 'whistling' and 'feasting on beer'."),
            ("The foresters mocked the young lad, laughing at his youthful face and rustic bow.", "Ormancılar genç delikanlıyla alay ettiler, onun genç yüzüne ve köylü yayına kahkahalarla güldüler.", "Coordinate participles describing mockery; past verb 'mocked'."),
            ("'What can a stripling like you do with a man's bow?' shouted their insolent leader.", "'Senin gibi bir bıyığı terlememiş çocuk, bir adamın yayıyla ne yapabilir ki?' diye bağırdı küstah liderleri.", "Vocative noun 'stripling'; modal question."),
            ("'I wager twenty marks I can hit that royal stag three score paces away,' answered Robin.", "'Yirmi marka bahse girerim ki altmış adım ötedeki o kraliyet geyiğini vurabilirim,' diye yanıt verdi Robin.", "Verb 'wager'; archaic measurement 'three score paces' (60 paces)."),
            ("The foresters took the wager with scornful laughter, confident he would fail miserably.", "Ormancılar, onun feci şekilde başarısız olacağından emin olarak iddiayı alaycı kahkahalarla kabul ettiler.", "Coordinate predicate; adverb 'miserably'."),
            ("Robin notched a broad arrow, drew the bowstring smoothly to his ear, and loosed the shaft.", "Robin geniş uçlu bir oku taktı, kirişi pürüzsüzce kulağına kadar çekti ve oku salıverdi.", "Series of coordinated past verbs 'notched, drew, loosed'."),
            ("The arrow sped true through the branches and pierced the great stag straight through the heart.", "Ok dalların arasından dosdoğru uçtu ve koca geyiği tam kalbinden vurdu.", "Adverbial modifier 'true'; coordinate past verbs 'sped and pierced'."),
            ("Instead of paying the wager, the furious foresters leaped up with drawn bows.", "Bahsi ödemek yerine, öfkeden deliye dönen ormancılar gerili yaylarıyla ayağa fırladılar.", "Preposition 'instead of' + gerund; participial adjective 'drawn bows'."),
            ("'Thou hast killed the King's deer, which means death on the gallows!' their leader cried.", "'Kralın geyiğini öldürdün, bu da dar ağacında ölüm demektir!' diye haykırdı liderleri.", "Archaic pronouns 'thou hast'; noun clause with 'which means'."),
            ("The forester loosed a treacherous shaft that whistled within an inch of Robin's ear.", "Ormancı, Robin'in kulağının bir parmak yakınından ıslık çalarak geçen haince bir ok fırlattı.", "Relative clause 'that whistled within an inch'; adjective 'treacherous'."),
            ("Robin turned in self-defense and shot an arrow that struck the wicked forester dead.", "Robin meşru müdafaayla geriye döndü ve o hain ormancıyı oracıkta öldüren bir ok attı.", "Prepositional phrase 'in self-defense'; resultative adjective 'struck dead'."),
            ("Knowing the Sheriff would show no mercy, Robin fled into the deep labyrinths of the forest.", "Şerif'in hiç merhamet göstermeyeceğini bilen Robin, ormanın derin labirentlerine doğru kaçtı.", "Participle clause of cause 'Knowing...'; noun phrase 'deep labyrinths'."),
            ("A price of two hundred pounds was set upon his head by the King's proclamation.", "Kralın fermanıyla Robin'in başına iki yüz sterlinlik bir ödül kondu.", "Passive voice 'was set upon his head'; agent phrase 'by proclamation'."),
            ("Robin took an oath that he would rob only the rich and corrupt to feed the poor.", "Robin yoksulları doyurmak için sadece zenginleri ve yozlaşmışları soyacağına yemin etti.", "Noun clause 'that he would rob only...'; infinitive of purpose 'to feed the poor'."),
            ("Thus began the glorious outlaw life of Robin Hood under the greenwood tree.", "Böylece yeşil ağaçların altında Robin Hood'un şanlı kanun kaçağı hayatı başlamış oldu.", "Inverted narrative sentence; transitional adverb 'Thus'.")
        ]
    },
    # Page 2: The Shooting Match at the Bridge (Meeting Little John)
    {
        "page_number": 2,
        "title": "Robin and Little John",
        "vocab": [
            ("plank", "dar köprü tahtası"),
            ("quarterstaff", "kalın değnek, uzun sopa"),
            ("brook", "dere, çay"),
            ("stout", "iri yarı, sağlam"),
            ("tumble", "yuvarlanmak, düşmek"),
            ("splash", "suya düşüş sesi / sıçratmak"),
            ("comrade", "yoldaş, arkadaş"),
            ("christen", "vaftiz etmek, ad koymak")
        ],
        "sentences": [
            ("Robin gathered around him seven score stalwart yeomen dressed in Lincoln green.", "Robin etrafına Lincoln yeşiline bürünmüş yüz kırk babayiğit okçu topladı.", "Archaic number 'seven score' (140); past participle modifier 'dressed in'."),
            ("One sunny afternoon, Robin wandered alone through the forest in search of adventure.", "Güneşli bir öğleden sonra Robin, macera arayışıyla ormanda tek başına dolaşıyordu.", "Prepositional phrase 'in search of adventure'; adverb 'alone'."),
            ("He came to a narrow wooden footbridge crossing a deep and rushing brook.", "Derin ve gürül gürül akan bir derenin üzerinden geçen dar, ahşap bir yaya köprüsüne geldi.", "Participial clause 'crossing a brook'; coordinate adjectives 'deep and rushing'."),
            ("At the opposite end stood a stranger, a giant of a man over seven feet tall.", "Karşı uçta bir yabancı, iki metreden uzun dev gibi bir adam duruyordu.", "Inverted locative sentence; appositive idiom 'a giant of a man'."),
            ("Neither traveler would yield the right-of-way, and they met in the middle of the narrow plank.", "İki yolcu da geçiş hakkını vermek istemedi ve dar tahtanın tam ortasında karşılaştılar.", "Correlative subject 'neither traveler'; noun 'right-of-way'."),
            ("'Give way, fellow!' cried Robin, 'or I will show thee how Nottingham archers fight!'", "'Yol ver adamım!' diye bağırdı Robin, 'yoksa sana Nottingham okçularının nasıl savaştığını gösteririm!'", "Archaic object 'thee'; indirect question 'how archers fight'."),
            ("'Thou talkest like a coward with thy bow against my staff,' scoffed the great stranger.", "'Benim sopama karşı yayınla tam bir korkak gibi konuşuyorsun,' diye alay etti koca yabancı.", "Archaic verbs 'talkest'; preposition 'against'."),
            ("Robin tossed aside his bow and cut a stout six-foot staff of tough seasoned oak.", "Robin yayını bir kenara fırlattı ve sert kurutulmuş meşeden altı ayaklık kalın bir sopa kesti.", "Coordinate past verbs 'tossed and cut'; compound adjective 'six-foot'."),
            ("They engaged in the center of the bridge, their wooden staves clattering like thunder.", "Köprünün ortasında dövüşe tutuştular; tahta sopaları gök gürültüsü gibi takırdıyordu.", "Absolute construction 'staves clattering like thunder'; past verb 'engaged'."),
            ("Robin was quick and struck the giant twice upon the ribs with stinging speed.", "Robin çevikti ve yakıcı bir hızla devin kaburgalarına iki kez vurdu.", "Adjective 'quick'; coordinate predicate with manner phrase 'with stinging speed'."),
            ("The stranger smiled broadly, stood firm like a rock, and swung his heavy cudgel.", "Yabancı genişçe gülümsedi, kaya gibi sağlam durdu ve ağır sopasını savurdu.", "Simile 'like a rock'; series of coordinated past actions."),
            ("With a tremendous crack, the stranger's blow caught Robin full upon the crown.", "Büyük bir çatırtıyla yabancının darbesi Robin'i tam kafasının tepesinden yakaladı.", "Prepositional phrase 'with a crack'; archaic noun 'crown' meaning head."),
            ("Robin lost his footing and tumbled head over heels into the cold foaming water.", "Robin dengesini kaybetti ve soğuk köpüklü suyun içine tepeüstü yuvarlandı.", "Idiom 'lost his footing'; adverbial idiom 'head over heels'."),
            ("Splash! The waters closed over his feathered cap, while the stranger laughed heartily.", "Şapırt! Sular tüylü kasketinin üzerinde kapanırken yabancı içtenlikle kahkahalar attı.", "Onomatopoeia; time clause with 'while'; adverb 'heartily'."),
            ("Robin scrambled onto the grassy bank, dripping wet but laughing with equal good humor.", "Robin sırılsıklam damlayarak fakat aynı neşeyle gülerek çimenli kıyıya tırmandı.", "Participle phrase 'dripping wet but laughing'; coordinate adjectives."),
            ("'Thou art a brave fellow,' cried Robin, 'and hast won the bridge fairly!'", "'Sen cesur bir adamsın,' diye haykırdı Robin, 've köprüyü hakkaniyetle kazandın!'", "Archaic grammar 'Thou art... and hast won'; adverb 'fairly'."),
            ("Robin blew three blasts upon his silver bugle, and forty green-clad yeomen appeared.", "Robin gümüş av borusundan üç ses üfledi ve yeşiller giymiş kırk okçu belirdi.", "Coordinate past clauses; compound adjective 'green-clad'."),
            ("When the outlaws learned the stranger's name was John Little, they roared with laughter.", "Kanun kaçakları yabancının adının John Little (Küçük John) olduğunu öğrenince kahkahalarla kükrediler.", "Time clause with 'when'; phrasal verb 'roared with laughter'."),
            ("'We shall christen thee Little John,' declared Robin, 'for thy mighty, towering stature!'", "'Kocaman, heybetli boyundan ötürü seni Küçük John diye vaftiz edeceğiz!' dedi Robin.", "Archaic direct speech; coordinate adjectives 'mighty, towering'."),
            ("Little John joined the merry band and became Robin's most faithful companion forever.", "Küçük John neşeli çeteye katıldı ve sonsuza dek Robin'in en sadık yoldaşı oldu.", "Coordinate past verbs 'joined and became'; superlative 'most faithful'.")
        ]
    },
    # Page 3: The Golden Arrow of Nottingham
    {
        "page_number": 3,
        "title": "The Golden Arrow of Nottingham",
        "vocab": [
            ("archery", "okçuluk"),
            ("contest", "yarışma, müsabaka"),
            ("arrow", "ok"),
            ("tTarget", "hedef"),
            ("disguise", "kılık değiştirmek"),
            ("quiver", "sadak, okluk"),
            ("beggar", "dilenci"),
            ("triumph", "zafer")
        ],
        "sentences": [
            ("The Sheriff of Nottingham burned with wrath because Robin Hood lived untamed.", "Robin Hood ele geçirilemeden yaşadığı için Nottingham Şerifi öfkeden küplere biniyordu.", "Metaphor 'burned with wrath'; causal clause with 'because'."),
            ("He devised a cunning scheme to entrap the master archer of Sherwood.", "Sherwood'un usta okçusunu tuzağa düşürmek için sinsi bir plan kurdu.", "Infinitive of purpose 'to entrap'; compound adjective 'master archer'."),
            ("He announced a grand archery contest on Nottingham green with a magnificent prize.", "Nottingham meydanında görkemli bir ödülle büyük bir okçuluk yarışması düzenleneceğini duyurdu.", "Transitive past 'announced'; prepositional phrase 'with a magnificent prize'."),
            ("The prize was an arrow made of pure yellow gold with feathers of beaten silver.", "Ödül, dövme gümüşten tüyleri olan saf sarı altından yapılmış bir oktu.", "Passive participle 'made of pure gold'; compound prepositional phrase."),
            ("'Robin is too proud to stay away from such a contest,' said the Sheriff to his men.", "'Robin böylesi bir yarışmadan uzak duramayacak kadar gururludur,' dedi Şerif adamlarına.", "Structure 'too + adjective + infinitive'; preposition 'to his men'."),
            ("Robin heard the news and laughed heartily at the Sheriff's clumsy trap.", "Robin haberi duydu ve Şerif'in sakar tuzağına içtenlikle güldü.", "Coordinate past verbs; possessive noun phrase 'Sheriff's clumsy trap'."),
            ("'We shall go to Nottingham,' Robin announced, 'but not in our Lincoln green coats.'", "'Nottingham'a gideceğiz,' diye duyurdu Robin, 'fakat Lincoln yeşili ceketlerimizle değil.'", "Modal 'shall go'; negative contrast 'not in coats'."),
            ("One hundred and forty yeomen disguised themselves as friars, beggars, and rustics.", "Yüz kırk okçu kendilerini keşişler, dilenciler ve köylüler kılığına soktular.", "Reflexive 'disguised themselves'; preposition 'as' for roles."),
            ("Robin himself wore a tattered beggar's cloak of ragged brown with a patch over one eye.", "Robin'in kendisi, bir gözünün üzerinde yama olan döküntü kahverengi paçavradan bir dilenci pelerini giydi.", "Emphatic reflexive 'Robin himself'; descriptive prepositional phrases."),
            ("A huge crowd gathered around the royal butts on the bright morning of the tournament.", "Turnuvanın pırıl pırıl sabahında kraliyet hedef tahtalarının etrafında dev bir kalabalık toplandı.", "Past verb 'gathered'; compound noun 'royal butts' (archery targets)."),
            ("Target after target was shot down until only three top bowmen remained in the ring.", "Halkada yalnızca en iyi üç okçu kalana kadar hedef üstüne hedef vuruldu.", "Repetitive subject 'Target after target'; passive voice 'was shot down'."),
            ("One was Gilbert of the Red Cap, one was Adam Bell, and the third was the tattered beggar.", "Biri Kırmızı Başlıklı Gilbert, biri Adam Bell, üçüncüsü ise o hırpani dilenciydi.", "Parallel listing of finalists; ordinal 'the third'."),
            ("The target was set at eight score paces, marked with a slender peeled willow wand.", "Hedef sekiz yirmi (160) adıma dikilmişti ve soyulmuş incecik bir söğüt dalıyla işaretlenmişti.", "Passive voice 'was set'; past participle modifier 'marked with'."),
            ("Gilbert stepped forward and shot so close that his arrow touched the willow wand.", "Gilbert öne adım attı ve öyle yakından vurdu ki oku söğüt dalına değdi.", "Result clause 'so close that'; past verb 'touched'."),
            ("The crowd cheered, believing that no man alive could better such miraculous skill.", "Böylesine mucizevi bir ustalığı hayatta olan hiçbir insanın geçemeyeceğine inanarak kalabalık tezahürat yaptı.", "Participle clause 'believing that'; modal 'could better'."),
            ("Then the ragged beggar stepped to the mark, smiling calmly under his battered hood.", "Sonra hırpani dilenci, yıpranmış başlığının altından sakince gülümseyerek atış çizgisine geçti.", "Participle phrase 'smiling calmly'; prepositional phrase 'to the mark'."),
            ("He drew his bowstring to his ear and loosed his gray goose feather without hesitation.", "Kirişini kulağına kadar çekti ve tereddüt etmeden gri kaz tüyü okunu salıverdi.", "Coordinate past verbs 'drew and loosed'; phrase 'without hesitation'."),
            ("His arrow split the willow wand clean in two with a sharp, echoing crack.", "Oku, keskin ve yankılanan bir çatırtıyla söğüt dalını tam ortasından ikiye yardı.", "Idiom 'split clean in two'; prepositional phrase 'with a crack'."),
            ("The crowd went wild with roaring applause, and the Sheriff handed him the Golden Arrow.", "Kalabalık gürleyen alkışlarla kendinden geçti ve Şerif ona Altın Ok'u bizzat takdim etti.", "Idiom 'went wild'; coordinate clause 'handed him the arrow'."),
            ("That evening in Sherwood, Robin laughed merrily as the golden trophy was passed around.", "O akşam Sherwood'da, altın kupa elden ele dolaşırken Robin neşeyle kahkahalar attı.", "Time clause with 'as'; passive voice 'was passed around'.")
        ]
    },
    # Page 4: Robin and the Curtal Friar (Friar Tuck at the River)
    {
        "page_number": 4,
        "title": "Robin and the Curtal Friar",
        "vocab": [
            ("friar", "keşiş, rahip"),
            ("curtal", "kısa cüppeli"),
            ("ford", "sığlık, nehir geçidi"),
            ("ferry", "karşıya taşımak / feribot"),
            ("tonsure", "keşiş tıraşı"),
            ("plash", "su şapırtısı"),
            ("cudgel", "kalın sopa"),
            ("truce", "ateşkes, barış")
        ],
        "sentences": [
            ("Will Scarlet told Robin of a fat, merry friar who lived near Fountain Abbey.", "Will Scarlet, Robin'e Fountain Manastırı yakınlarında yaşayan şişman ve neşeli bir keşişten bahsetti.", "Transitive 'told of'; relative clause 'who lived near'."),
            ("'He can draw a bow and handle a broadsword better than any yeoman in England,' said Will.", "'İngiltere'deki herhangi bir okçudan daha iyi yay çeker ve kılıç sallar,' dedi Will.", "Comparative equality 'better than any yeoman'; modal 'can draw'."),
            ("Robin was eager to meet this fighting man of God and went alone to find him.", "Robin Tanrı'nın bu savaşçı adamıyla tanışmaya çok hevesliydi ve onu bulmak için tek başına gitti.", "Adjective + infinitive 'eager to meet'; past verbs 'was and went'."),
            ("He found the Friar sitting beside a sparkling stream, eating a huge venison pasty.", "Keşişi parıldayan bir akarsuyun yanında oturmuş, devasa bir geyik etli börek yerken buldu.", "Perception verb 'found' + participle phrase 'sitting and eating'."),
            ("The friar wore a steel cap under his hood and a stout broadsword at his belt.", "Keşiş başlığının altına çelik bir miğfer takmış ve kemerine sağlam bir kılıç kuşanmıştı.", "Coordinate direct objects; prepositional phrases."),
            ("Robin drew his sword and pointed across the wide water toward the far bank.", "Robin kılıcını çekti ve geniş suyun üzerinden karşı kıyıya doğru işaret etti.", "Coordinate past verbs 'drew and pointed'; directional phrase 'across water'."),
            ("'Carry me across this stream, thou holy man,' commanded Robin, 'or thy life is forfeit!'", "'Beni bu akarsudan karşıya taşı ey kutsal adam,' diye emretti Robin, 'yoksa canından olursun!'", "Imperative command; archaic condition 'or thy life is forfeit'."),
            ("The friar looked at Robin calmly, stood up, and took the young outlaw upon his back.", "Keşiş sakince Robin'e baktı, ayağa kalktı ve genç kanun kaçağını sırtına aldı.", "Series of coordinated past actions; adverb 'calmly'."),
            ("He waded through the deep cold current and set Robin down on the opposite shore.", "Derin soğuk akıntının içinden bata çıka yürüdü ve Robin'i karşı kıyıya bıraktı.", "Coordinate past verbs 'waded and set down'; adjective 'opposite'."),
            ("Then the friar drew his own gleaming sword with a merry twinkle in his eye.", "Ardından keşiş, gözünde neşeli bir pırıltıyla kendi parıldayan kılıcını çekti.", "Prepositional phrase 'with a twinkle'; adjective 'gleaming'."),
            ("'Now, my fine young gallant,' chuckled the friar, 'carry me back across the stream!'", "'Şimdi benim güzel yiğidim,' diye kıkırdadı keşiş, 'beni nehrin karşısına geri taşı!'", "Direct speech; imperative command 'carry me back'."),
            ("Robin had to obey, so he took the heavy monk upon his shoulders with a groan.", "Robin itaat etmek zorundaydı, bu yüzden inleyerek ağır keşişi omuzlarına aldı.", "Modal of obligation 'had to obey'; manner phrase 'with a groan'."),
            ("Robin struggled through the deep water, breathless under the enormous weight.", "Robin bu devasa ağırlık altında nefes nefese kalarak derin suyun içinde güçlükle ilerledi.", "Adjective 'breathless'; past verb 'struggled through'."),
            ("When they reached the bank, Robin sprang down and ordered the friar to carry him again.", "Kıyıya vardıklarında Robin aşağı atladı ve keşişe kendisini tekrar taşımasını emretti.", "Time clause with 'when'; verb + object + infinitive 'ordered to carry'."),
            ("The friar agreed smilingly and hoisted Robin upon his sturdy shoulders once more.", "Keşiş gülümseyerek kabul etti ve Robin'i sağlam omuzlarına bir kez daha kaldırdı.", "Adverb 'smilingly'; phrasal verb 'hoisted upon'."),
            ("But in the very middle of the stream, where the water was deepest, the friar stopped.", "Fakat akarsuyun tam ortasında, suyun en derin olduğu yerde keşiş duruverdi.", "Emphatic adjective 'very middle'; superlative 'deepest'."),
            ("He shrugged his shoulders, dumping Robin headlong into the icy current with a huge plash.", "Omuzlarını silkti ve büyük bir şapırtıyla Robin'i buz gibi akıntının içine tepeüstü boca etti.", "Participle phrase 'dumping Robin headlong'; noun 'plash'."),
            ("They both reached the shore and fought with swords and staves for three furious hours.", "İkisi de kıyıya çıktılar ve kılıçlar ile sopalarla üç öfkeli saat boyunca savaştılar.", "Duration phrase 'for three hours'; coordinate past verbs."),
            ("Exhausted and laughing, Robin blew his bugle, and Friar Tuck whistled for his hounds.", "Bitkin düşen ve kahkahalar atan Robin borusunu çaldı, Rahip Tuck ise tazılarına ıslık çaldı.", "Coordinate clauses; participial adjectives 'exhausted and laughing'."),
            ("Recognizing each other's valor, they shook hands and Friar Tuck joined the merry band.", "Birbirlerinin cesaretini takdir ederek el sıkıştılar ve Rahip Tuck neşeli çeteye katıldı.", "Participle clause 'Recognizing valor'; coordinate past verbs.")
        ]
    },
    # Page 5: The Sad Knight of the Forest (Sir Richard of the Lea)
    {
        "page_number": 5,
        "title": "The Sad Knight of the Lea",
        "vocab": [
            ("knight", "şövalye"),
            ("debt", "borç"),
            ("abbot", "başkeşiş, manastır yöneticisi"),
            ("sorrow", "keder, üzüntü"),
            ("ransom", "kurtarmalık, fidye"),
            ("lend", "ödünç vermek"),
            ("castle", "kale, şato"),
            ("generosity", "cömertlik")
        ],
        "sentences": [
            ("One afternoon, Little John brought a stranger to the great trysting tree in Sherwood.", "Bir öğleden sonra Küçük John, Sherwood'daki ulu buluşma ağacına bir yabancı getirdi.", "Transitive past 'brought'; compound noun 'trysting tree'."),
            ("The stranger was a knight clad in shabby armor, riding a thin, tired horse.", "Yabancı, zayıf ve yorgun bir ata binmiş, eski püskü zırhlar içinde bir şövalyeydi.", "Passive participle 'clad in shabby armor'; participle phrase 'riding a horse'."),
            ("His head hung low upon his breast, and tears of deep sorrow wet his cheeks.", "Başı göğsünün üzerine düşmüştü ve derin bir kederin gözyaşları yanaklarını ıslatıyordu.", "Coordinate clauses; compound noun 'tears of deep sorrow'."),
            ("Robin welcomed him courteously and set a feast of roast venison and wine before him.", "Robin onu nezaketle karşıladı ve önüne fırında geyik eti ile şaraptan bir ziyafet koydu.", "Adverb 'courteously'; coordinate past verbs 'welcomed and set'."),
            ("After the meal, Robin asked the knight why his spirit was so burdened with grief.", "Yemekten sonra Robin şövalyeye ruhunun neden kederle bu kadar ağırlaştığını sordu.", "Indirect question clause 'why his spirit was burdened'; passive participle."),
            ("'My name is Sir Richard of the Lea,' spoke the knight in a trembling voice.", "'Benim adım Lea'lı Sör Richard,' diye konuştu şövalye titreyen bir sesle.", "Proper name; prepositional phrase 'in a trembling voice'."),
            ("'I am ruined because my son killed a knight in a tournament by accident.'", "'Mahvoldum, çünkü oğlum bir turnuvada kazara bir şövalyeyi öldürdü.'", "Causal clause with 'because'; prepositional phrase 'by accident'."),
            ("'To save my son from prison, I had to borrow four hundred pounds from the Abbot of Saint Mary's.'", "'Oğlumu hapisten kurtarmak için Saint Mary Başkeşişi'nden dört yüz sterlin borç almak zorunda kaldım.'", "Infinitive of purpose 'to save my son'; modal obligation 'had to borrow'."),
            ("'Tomorrow is the day of payment, and if I fail, my ancestral castle is lost forever.'", "'Yarın ödeme günüdür ve eğer ödeyemezsem atalarımdan kalma şatom sonsuza dek elden gidecek.'", "Conditional clause 'if I fail'; passive predicate 'is lost forever'."),
            ("Robin was deeply moved by the noble knight's honest grief and terrible misfortune.", "Robin soylu şövalyenin dürüst kederinden ve korkunç talihsizliğinden derinden etkilendi.", "Passive voice 'was deeply moved by'; coordinate nouns."),
            ("He turned to Little John and asked how much gold they had in their treasury.", "Küçük John'a döndü ve hazinelerinde ne kadar altınları olduğunu sordu.", "Indirect question 'how much gold they had'; past verb 'turned'."),
            ("Little John counted four hundred bright gold pounds from their store of riches.", "Küçük John zenginlik ambarlarından dört yüz parlak altın sterlin saydı.", "Transitive past 'counted'; prepositional phrase 'from their store'."),
            ("'Take this gold, good Sir Richard,' said Robin, handing over the heavy purse.", "'Bu altını al iyi Sör Richard,' dedi Robin ağır keseyi uzatarak.", "Imperative 'take this gold'; participle phrase 'handing over purse'."),
            ("'Pay the greedy Abbot, and keep thy ancestral lands for thy family.'", "'Açgözlü Başkeşiş'e ödemeni yap ve atalarının topraklarını ailen için koru.'", "Coordinate imperatives 'pay and keep'; archaic possessive 'thy'."),
            ("Sir Richard wept tears of overwhelming gratitude and swore an everlasting brotherhood.", "Sör Richard ezici bir minnet gözyaşlarına boğuldu ve ebedi bir kardeşliğe ant içti.", "Coordinate past verbs 'wept and swore'; compound adjective 'everlasting'."),
            ("'I shall repay thee every single penny within one year's time,' promised the knight.", "'Bir yıl içinde sana her bir kuruşunu geri ödeyeceğim,' diye söz verdi şövalye.", "Modal 'shall repay'; time phrase 'within one year's time'."),
            ("Robin also gave him a fine horse, new clothes, and two stout yeomen as escorts.", "Robin ona ayrıca güzel bir at, yeni giysiler ve muhafız olarak iki babayiğit okçu verdi.", "Multiple direct objects; preposition 'as escorts'."),
            ("Sir Richard rode away into the golden sunset, his head held high with honor.", "Sör Richard başı onurla dikilmiş halde altın gün batımına doğru at sürdü.", "Absolute construction 'his head held high'; directional phrase 'into sunset'."),
            ("The greedy Abbot received his money with bitter disappointment, robbed of his prey.", "Açgözlü Başkeşiş avından mahrum kalarak parasını acı bir hayal kırıklığıyla teslim aldı.", "Past participle modifier 'robbed of prey'; prepositional phrase 'with disappointment'."),
            ("True justice had triumphed in Sherwood through the generosity of Robin Hood.", "Sherwood'da gerçek adalet, Robin Hood'un cömertliği sayesinde zafer kazanmıştı.", "Past perfect 'had triumphed'; prepositional phrase 'through generosity'.")
        ]
    },
    # Page 6: The Sheriff Goes a-Hunting
    {
        "page_number": 6,
        "title": "The Sheriff in Sherwood",
        "vocab": [
            ("sheriff", "şerif"),
            ("capture", "yakalamak, tutsak etmek"),
            ("feast", "ziyafet"),
            ("pledge", "kadeh kaldırmak, söz vermek"),
            ("treason", "vatana ihanet"),
            ("ransom", "fidye"),
            ("humiliation", "aşağılanma"),
            ("oath", "yemin")
        ],
        "sentences": [
            ("The Sheriff of Nottingham swore by all the saints that Robin Hood must hang.", "Nottingham Şerifi bütün azizlerin üzerine yemin etti ki Robin Hood mutlaka asılmalıydı.", "Noun clause 'that Robin must hang'; past verb 'swore by'."),
            ("He gathered a troop of armed men and rode boldly into the borders of Sherwood.", "Silahlı adamlardan bir birlik topladı ve cüretkarca Sherwood sınırlarına doğru at sürdü.", "Coordinate past verbs 'gathered and rode'; adverb 'boldly'."),
            ("While his soldiers rested, the Sheriff rode ahead into a secluded glade alone.", "Askerleri dinlenirken Şerif tek başına kuytu bir orman açıklığına doğru ilerledi.", "Temporal clause with 'while'; past verb 'rode ahead'."),
            ("Suddenly, green-clad archers sprang from behind every bush and surrounded his horse.", "Birdenbire her çalının arkasından yeşiller giymiş okçular fırladı ve atının etrafını sardı.", "Coordinate past verbs 'sprang and surrounded'; compound adjective 'green-clad'."),
            ("Little John grasped the Sheriff's bridle with a cheerful and mocking smile.", "Küçük John neşeli ve alaycı bir tebessümle Şerif'in atının dizginini yakaladı.", "Prepositional phrase 'with a cheerful smile'; transitive 'grasped'."),
            ("'Welcome to Sherwood, Lord Sheriff!' cried Little John, 'Robin Hood awaits thee!'", "'Sherwood'a hoş geldiniz Şerif Efendi!' diye haykırdı Küçük John, 'Robin Hood seni bekliyor!'", "Archaic object 'thee'; exclamatory direct speech."),
            ("The Sheriff turned white with terror, realizing he was completely at their mercy.", "Tamamen onların insafına kaldığını anlayan Şerif korkudan bembeyaz kesildi.", "Participle clause 'realizing he was at mercy'; idiom 'turned white'."),
            ("They led him deep into the forest to the great trysting oak tree.", "Onu ormanın derinliklerine, ulu buluşma meşesi ağacına doğru götürdüler.", "Transitive past 'led'; compound noun 'trysting oak tree'."),
            ("Robin Hood bowed low with exaggerated courtly courtesy before his mortal enemy.", "Robin Hood can düşmanının önünde abartılı bir saray nezaketiyle yerlere kadar eğildi.", "Phrasal verb 'bowed low'; prepositional phrase 'with exaggerated courtesy'."),
            ("'Thou art just in time to dine with us on the King's royal venison,' said Robin.", "'Kralın kraliyet geyik etinden bizimle akşam yemeği yemek için tam vaktinde geldin,' dedi Robin.", "Idiom 'just in time'; archaic 'thou art'."),
            ("A magnificent banquet was laid out on the mossy ground beneath the trees.", "Ağaçların altındaki yosunlu zemine görkemli bir ziyafet sofrası kuruldu.", "Passive voice 'was laid out'; adjective 'mossy'."),
            ("The trembling Sheriff was forced to sit on a log and eat his own King's deer.", "Titreyen Şerif bir kütüğe oturup kendi Kralı'nın geyiğini yemeye mecbur bırakıldı.", "Passive structure 'was forced to sit'; participial adjective 'trembling'."),
            ("Robin toasted the Sheriff with wine poured from fine silver goblets.", "Robin güzel gümüş kadehlerden doldurulan şarapla Şerif'in şerefine kadeh kaldırdı.", "Past participle modifier 'poured from goblets'; past verb 'toasted'."),
            ("When the meal concluded, Robin politely requested payment for the dinner.", "Yemek sona erdiğinde Robin kibarca akşam yemeğinin ücretini talep etti.", "Time clause with 'concluded'; adverb 'politely'."),
            ("Little John searched the Sheriff's saddlebags and found three hundred gold pieces.", "Küçük John Şerif'in eyer çantalarını aradı ve üç yüz altın sikke buldu.", "Coordinate past verbs 'searched and found'."),
            ("'This will pay for thy supper and leave a tidy tip for my men,' laughed Robin.", "'Bu akşam yemeğini öder ve adamlarıma da güzel bir bahşiş bırakır,' diye güldü Robin.", "Coordinate modal clauses; adjective 'tidy tip'."),
            ("The Sheriff wept with fury and humiliation as his treasure was divided among the outlaws.", "Hazinesi kanun kaçakları arasında paylaştırılırken Şerif öfke ve aşağılanmayla ağladı.", "Time clause with 'as'; passive voice 'was divided'."),
            ("Before releasing him, Robin made the Sheriff swear a solemn oath on his sword.", "Onu serbest bırakmadan önce Robin, Şerif'e kılıcı üzerine kutsal bir yemin ettirdi.", "Causative structure 'made Sheriff swear'; preposition 'before releasing'."),
            ("The Sheriff had to swear never to harm any greenwood outlaw or enter Sherwood again.", "Şerif bir daha yeşil orman kanun kaçaklarına zarar vermemeye ve Sherwood'a girmemeye yemin etmek zorunda kaldı.", "Infinitive series; modal 'had to swear'."),
            ("He rode back to Nottingham humiliated, poorer, and burning with unspoken revenge.", "Aşağılanmış, daha yoksul ve dile getirilmemiş intikam ateşiyle yanarak Nottingham'a geri döndü.", "Series of predicate adjectives and participles; comparative 'poorer'.")
        ]
    },
    # Page 7: Little John at the Fair
    {
        "page_number": 7,
        "title": "Little John at the Fair",
        "vocab": [
            ("fair", "panayır"),
            ("wrestle", "güreşmek"),
            ("alias", "takma ad"),
            ("prowess", "üstün beceri, maharet"),
            ("quarterstaff", "kalın sopa"),
            ("hire", "işe almak"),
            ("cellar", "mahzen"),
            ("butler", "kahya")
        ],
        "sentences": [
            ("There was a great fair held in Nottingham town on Saint Giles's Day.", "Aziz Giles Günü'nde Nottingham kasabasında büyük bir panayır düzenlendi.", "Passive participle 'held in Nottingham'; proper holiday name."),
            ("Little John begged Robin for permission to visit the fair in disguise.", "Küçük John kılık değiştirerek panayırı ziyaret etmek için Robin'den izin istedi.", "Verb + object 'begged Robin for permission'; infinitive 'to visit'."),
            ("'Go, but keep thy temper and stay out of the Sheriff's sight,' warned Robin.", "'Git, fakat öfkene hakim ol ve Şerif'in gözünden uzak dur,' diye uyardı Robin.", "Imperative coordinates; idiom 'keep thy temper'."),
            ("Little John dressed as a simple countryman and attended the games.", "Küçük John sade bir köylü kılığına büründü ve müsabakalara katıldı.", "Phrasal verb 'dressed as'; coordinate past 'attended'."),
            ("First he entered the wrestling ring and defeated the county champion with ease.", "Önce güreş halkasına girdi ve bölge şampiyonunu kolaylıkla alt etti.", "Coordinate past verbs 'entered and defeated'; phrase 'with ease'."),
            ("Next he took up the bow and split every target wand at eighty paces.", "Sonra yayı eline aldı ve seksen adımdaki her hedef dalını ortadan ikiye yardı.", "Coordinate past verbs 'took up and split'; measurement phrase."),
            ("The Sheriff watched his marvelous feats and was thoroughly enchanted by his strength.", "Şerif onun harikulade gösterilerini izledi ve gücünden fazlasıyla büyülendi.", "Passive voice 'was enchanted by'; coordinate past 'watched'."),
            ("'What is thy name, stout yeoman?' asked the Sheriff, not recognizing the outlaw.", "'Adın nedir yiğit okçu?' diye sordu Şerif, kanun kaçağını tanımayarak.", "Archaic question; participle phrase 'not recognizing'."),
            ("'Men call me Reynold Greenleaf, sir,' replied Little John with a sly bow.", "'Bana Reynold Greenleaf derler efendim,' diye yanıtladı Küçük John kurnazca bir selamla.", "Proper alias; prepositional phrase 'with a sly bow'."),
            ("The Sheriff immediately hired him as his chief bodyguard for twenty marks a year.", "Şerif onu yılda yirmi marka derhal baş koruması olarak işe aldı.", "Transitive past 'hired'; preposition 'as chief bodyguard'."),
            ("For six months, Little John lived in the Sheriff's castle, eating and drinking the best.", "Altı ay boyunca Küçük John Şerif'in kalesinde yaşadı; en iyisini yiyip en iyisini içti.", "Duration phrase 'For six months'; coordinate participles."),
            ("One day when the Sheriff was away hunting, Little John demanded his midday meal.", "Bir gün Şerif uzakta avdayken Küçük John öğle yemeğini talep etti.", "Time clause 'when Sheriff was away'; transitive past 'demanded'."),
            ("The steward refused rudely, locking the pantry door against the giant.", "Kahya kabaca reddetti, kiler kapısını devin yüzüne kilitledi.", "Adverb 'rudely'; participle clause 'locking pantry door'."),
            ("Little John cracked the steward's head, broke open the heavy lock, and entered.", "Küçük John kahyanın kafasını patlattı, ağır kilidi kırıp açtı ve içeri girdi.", "Series of coordinated past actions."),
            ("He sat in the cellar eating cold venison and drinking rich Malmsey wine.", "Mahzende oturup soğuk geyik eti yedi ve nefis Malmsey şarabı içti.", "Coordinate participles describing hearty indulgence."),
            ("The castle cook, a stout swordsman, attacked him with a gleaming blade.", "Sağlam bir kılıç ustası olan kale aşçısı parıldayan bir kılıçla ona saldırdı.", "Apposition identifying cook; past verb 'attacked'."),
            ("They fought fiercely until both grew winded and developed mutual respect.", "Her ikisinin de nefesi kesilip karşılıklı saygı duyana kadar kıyasıya savaştılar.", "Time clause with 'until'; coordinate past verbs."),
            ("'Thou art the finest swordsman I have ever crossed blades with!' laughed Little John.", "'Sen hayatımda kılıç tokuşturduğum en iyi kılıç ustasısın!' diye güldü Küçük John.", "Superlative clause with present perfect 'have ever crossed'."),
            ("He persuaded the cook to pack all the Sheriff's silver plate and join Robin Hood.", "Şerif'in bütün gümüş tabaklarını paketleyip Robin Hood'a katılması için aşçıyı ikna etti.", "Verb + object + infinitive 'persuaded cook to pack'."),
            ("Together they marched out of the castle carrying the Sheriff's silver back to Sherwood.", "Şerif'in gümüşlerini Sherwood'a geri taşıyarak birlikte kaleden çıkıp gittiler.", "Participle phrase 'carrying silver'; phrasal verb 'marched out of'.")
        ]
    },
    # Page 8: The Butcher's Cart
    {
        "page_number": 8,
        "title": "The Butcher of Sherwood",
        "vocab": [
            ("butcher", "kasap"),
            ("cart", "yük arabası"),
            ("market", "pazar yeri"),
            ("bargain", "kelepir, ucuza satmak"),
            ("shilling", "şilin"),
            ("pasture", "otlak, çayır"),
            ("herd", "sürü"),
            ("trick", "kandırmak / hile")
        ],
        "sentences": [
            ("Robin Hood loved nothing better than a merry prank at the Sheriff's expense.", "Robin Hood Şerif'in aleyhine neşeli bir muziplik yapmaktan daha çok hiçbir şeyi sevmezdi.", "Idiom 'at someone's expense'; comparative 'nothing better than'."),
            ("One morning on the highway, he met a young butcher driving a cart to Nottingham market.", "Bir sabah anayolda, Nottingham pazarına at arabası süren genç bir kasapla karşılaştı.", "Participle phrase 'driving a cart'; past verb 'met'."),
            ("Robin bought the cart, horse, and all the meat for five gold pieces on the spot.", "Robin arabayı, atı ve bütün eti oracıkta beş altın sikke karşılığında satın aldı.", "Series of direct objects; idiom 'on the spot'."),
            ("He donned the butcher's blood-stained apron and drove merrily into the market square.", "Kasabın kan lekeli önlüğünü giydi ve neşeyle pazar meydanına doğru arabasını sürdü.", "Coordinate past verbs 'donned and drove'; compound adjective 'blood-stained'."),
            ("He set up a stall among the butchers and began shouting his extraordinary prices.", "Kasapların arasında bir tezgah kurdu ve sıra dışı fiyatlarını bağırmaya başladı.", "Coordinate past verbs; participial adjective 'extraordinary'."),
            ("'Fresh meat for all!' cried Robin, 'three pennies' worth for one single penny!'", "'Herkese taze et!' diye haykırdı Robin, 'üç kuruşluk et sadece bir kuruşa!'", "Exclamatory quotation; idiom 'worth for one penny'."),
            ("Poor women, beggars, and children flocked around his stall, buying meat by the armload.", "Yoksul kadınlar, dilenciler ve çocuklar tezgahının etrafına akın ettiler, kucak dolusu et aldılar.", "Coordinate subjects; participle phrase 'buying meat by the armload'."),
            ("The other butchers grew furious because Robin was underselling them completely.", "Diğer kasaplar öfkeden deliye döndüler çünkü Robin tamamen onların fiyatının altında satıyordu.", "Causal clause with 'because'; transitive past 'underselling'."),
            ("'He must be a prodigal fool who has squandered his father's estate,' whispered the butchers.", "'Babasının mülkünü çarçur etmiş savurgan bir aptal olmalı,' diye fısıldaştı kasaplar.", "Modal deduction 'must be'; relative clause with present perfect."),
            ("The Sheriff heard of this rich, foolish young butcher and invited him to dinner.", "Şerif bu zengin ve aptal genç kasabı duydu ve onu akşam yemeğine davet etti.", "Coordinate past verbs 'heard of and invited'; series of adjectives."),
            ("Over wine, the Sheriff asked if the young butcher had horned beasts to sell.", "Şarap eşliğinde Şerif, genç kasabın satılık boynuzlu hayvanı olup olmadığını sordu.", "Indirect question with 'if'; compound noun 'horned beasts'."),
            ("'Aye, Lord Sheriff,' said Robin, 'five hundred fat horned beasts graze on my pastures.'", "'Evet Şerif Efendi,' dedi Robin, 'otlaklarımda beş yüz semiz boynuzlu hayvan otlar.'", "Direct speech; numeral 'five hundred'."),
            ("'I will sell them to thee for three hundred pieces of gold in cash.'", "'Onları sana nakit üç yüz altın karşılığında satarım.'", "Future modal 'will sell'; prepositional phrase 'for three hundred pieces'."),
            ("The greedy Sheriff greedily agreed, intending to buy the cattle far below market value.", "Açgözlü Şerif, sığırları piyasa değerinin çok altında satın alma niyetiyle hevesle kabul etti.", "Participle phrase 'intending to buy'; adverb 'greedily'."),
            ("The next morning, the Sheriff and the butcher rode together toward Sherwood Forest.", "Ertesi sabah Şerif ve kasap birlikte Sherwood Ormanı'na doğru at sürdüler.", "Directional phrase 'toward Sherwood Forest'."),
            ("As they entered the gloomy woods, the Sheriff grew uneasy and looked about nervously.", "Kasvetli koruya girdiklerinde Şerif huzursuzlandı ve gergin bir şekilde etrafına bakındı.", "Time clause with 'as'; coordinate past verbs 'grew and looked'."),
            ("'I do not like this wild forest,' muttered the Sheriff, 'for Robin Hood haunts it.'", "'Bu vahşi ormanı hiç sevmiyorum,' diye mırıldandı Şerif, 'çünkü Robin Hood buraya dadandı.'", "Causal coordinating conjunction 'for'; transitive verb 'haunts'."),
            ("Suddenly Robin pointed to a herd of a hundred wild royal deer grazing in a glade.", "Birdenbire Robin bir orman açıklığında otlayan yüz vahşi kraliyet geyiği sürüsünü gösterdi.", "Participle phrase 'grazing in a glade'; phrasal verb 'pointed to'."),
            ("'There are my horned beasts, Lord Sheriff!' laughed Robin, blowing his silver horn.", "'İşte benim boynuzlu hayvanlarım Şerif Efendi!' diye güldü Robin, gümüş borusunu üfleyerek.", "Direct quotation; participle phrase 'blowing his horn'."),
            ("The outlaws appeared from the brush, relieved the Sheriff of his gold, and escorted him home.", "Kanun kaçakları çalılıklardan belirdiler, Şerif'i altınlarından hafiflettiler ve onu eve kadar uğurladılar.", "Series of coordinated past actions; idiom 'relieved of gold'.")
        ]
    },
    # Page 9: The Tinker and the King's Warrant
    {
        "page_number": 9,
        "title": "The Tinker and the Warrant",
        "vocab": [
            ("tinker", "lehimci, kalaycı"),
            ("warrant", "ferman, tutuklama emri"),
            ("parchment", "parşömen"),
            ("inn", "han"),
            ("ale", "bira"),
            ("slumber", "derin uyku"),
            ("bribe", "rüşvet"),
            ("revenge", "intikam")
        ],
        "sentences": [
            ("The Sheriff issued a royal warrant on stiff parchment for the capture of Robin Hood.", "Şerif Robin Hood'un yakalanması için sert parşömen üzerine kraliyet tutuklama emri çıkardı.", "Prepositional phrases indicating medium and purpose; past verb 'issued'."),
            ("A wandering tinker named Wat o' the Crabstaff boasted that he would serve the warrant.", "Wat o' the Crabstaff adında gezgin bir lehimci fermanı bizzat tebliğ edeceğini böbürlendi.", "Appositive participle 'named Wat'; noun clause 'that he would serve'."),
            ("Wat marched along the dusty road toward Sherwood, swinging his heavy crabstaff proudly.", "Wat ağır yabani elma sopasını gururla sallayarak Sherwood'a doğru tozlu yolda yürüdü.", "Participle phrase 'swinging his crabstaff'; directional preposition 'toward'."),
            ("Robin met him near the sign of the Blue Boar Inn, disguised as a prosperous yeoman.", "Robin zengin bir köylü kılığına bürünmüş halde Blue Boar Hanı tabelasının yakınında onunla karşılaştı.", "Passive participle modifier 'disguised as'; proper location."),
            ("'Good day, fellow,' greeted Robin, 'what brings thee along this dusty highway?'", "'İyi günler adamım,' diye selamladı Robin, 'seni bu tozlu anayolda hangi rüzgar attı?'", "Archaic greeting; question with 'what brings thee'."),
            ("'I carry a warrant for Robin Hood's arrest, worth one hundred golden pounds!' boasted Wat.", "'Robin Hood'un tutuklanması için yüz altın sterlin değerinde bir ferman taşıyorum!' diye böbürlendi Wat.", "Adjective phrase 'worth one hundred pounds'; past verb 'boasted'."),
            ("'Come into the Blue Boar,' said Robin with a smile, 'and let us drink to thy success.'", "'Blue Boar'a gel,' dedi Robin bir tebessümle, 've senin başarın şerefine içelim.'", "Imperative coordinates; idiom 'drink to thy success'."),
            ("They sat in the taproom, where Robin ordered tankard after tankard of strong ale.", "Robin'in kupa üstüne kupa sert bira sipariş ettiği meyhane salonunda oturdular.", "Relative clause of place; repetitive noun phrase 'tankard after tankard'."),
            ("The tinker drank thirstily and bragged of how he would thrash Robin Hood with his staff.", "Lehimci susamışçasına içti ve sopasıyla Robin Hood'u nasıl pataklayacağını böbürlendi.", "Indirect question 'how he would thrash'; coordinate past verbs."),
            ("Soon the heavy drink overcame Wat, and he fell into a deep, snoring slumber.", "Çok geçmeden ağır içki Wat'ı alt etti ve adam derin, horultulu bir uykuya daldı.", "Coordinate past clauses; compound noun 'snoring slumber'."),
            ("Robin quietly reached into the tinker's pouch and extracted the royal parchment warrant.", "Robin sessizce lehimcinin kesesine uzandı ve kraliyet parşömen fermanını çekip aldı.", "Coordinate past verbs 'reached and extracted'; adverb 'quietly'."),
            ("He paid the innkeeper for his own drink and slipped away into the greenwood.", "Meyhaneciye kendi içkisinin parasını ödedi ve yeşil ormanın içine doğru sıvıştı.", "Coordinate past verbs 'paid and slipped away'."),
            ("When the tinker woke hours later, he had a pounding headache and an empty purse.", "Lehimci saatler sonra uyandığında, zonklayan bir baş ağrısı ve tamtakır bir kesesi vardı.", "Time clause with 'when'; participial adjective 'pounding headache'."),
            ("The landlord demanded ten shillings for all the ale Wat had consumed with his companion.", "Hancı, Wat'ın arkadaşıyla tükettiği bütün bira için on şilin talep etti.", "Relative clause 'Wat had consumed'; transitive past 'demanded'."),
            ("Wat reached for his pouch and found both his money and the King's warrant gone.", "Wat kesesine uzandı ve hem parasının hem de Kralın fermanının yok olduğunu gördü.", "Correlative conjunctions 'both... and'; adjective 'gone'."),
            ("He realized in furious rage that the friendly stranger had been Robin Hood himself.", "O dost canlısı yabancının bizzat Robin Hood olduğunu öfkeli bir hiddetle anladı.", "Noun clause with past perfect; emphatic reflexive 'Robin himself'."),
            ("He grabbed his crabstaff and rushed into Sherwood Forest to exact revenge.", "Yabani elma sopasını kaptı ve intikam almak için Sherwood Ormanı'na daldı.", "Coordinate past verbs; infinitive of purpose 'to exact revenge'."),
            ("He encountered Robin under an oak and challenged him to single combat.", "Meşe ağacının altında Robin'le karşılaştı ve onu teke tek dövüşe davet etti.", "Coordinate past verbs 'encountered and challenged'; phrase 'to single combat'."),
            ("They traded blows until Robin admired the tinker's skill and offered him a place in his band.", "Robin lehimcinin maharetini takdir edip ona çetesinde bir yer teklif edene kadar darbe tokuşturdular.", "Time clause with 'until'; coordinate past verbs 'admired and offered'."),
            ("Wat happily accepted, and Robin gained another stout fighter for the greenwood.", "Wat neşeyle kabul etti ve Robin yeşil orman için bir başka babayiğit savaşçı kazanmış oldu.", "Coordinate independent clauses; adverb 'happily'.")
        ]
    },
    # Page 10: Will Scarlet's Story
    {
        "page_number": 10,
        "title": "The Dandy in Scarlet",
        "vocab": [
            ("scarlet", "al, parlak kırmızı"),
            ("silk", "ipek"),
            ("dandy", "züppe, şık giyimli kimse"),
            ("cousin", "kuzen"),
            ("fencing", "eskrim, kılıç oyunu"),
            ("grief", "keder, elem"),
            ("kinship", "akrabalık"),
            ("sword", "kılıç")
        ],
        "sentences": [
            ("Robin Hood and Little John walked along the sunny forest highway one morning.", "Robin Hood ve Küçük John bir sabah güneşli orman anayolu boyunca yürüyorlardı.", "Subject coordinate; past verb 'walked along'."),
            ("Coming down the path was a finely dressed young gentleman in scarlet silk.", "Patikadan aşağı doğru al ipekler içinde çok şık giyimli genç bir beyefendi geliyordu.", "Inverted locative sentence; passive participle modifier 'finely dressed'."),
            ("His curly yellow hair fell over his shoulders, and he sniffed a scented rose delicately.", "Kıvırcık sarı saçları omuzlarına dökülüyordu ve narin bir şekilde kokulu bir gülü kokluyordu.", "Coordinate clauses; adverb 'delicately'."),
            ("'Behold a sweet popinjay!' whispered Little John, 'he will yield a rich purse.'", "'Şu tatlı züppeye bir bak!' diye fısıldadı Küçük John, 'güzel bir kese bırakacaktır.'", "Imperative 'Behold'; future modal 'will yield'."),
            ("Robin stepped out onto the path and barred the young gentleman's progress.", "Robin patikaya adım attı ve genç beyefendinin ilerlemesini engelledi.", "Coordinate past verbs 'stepped out and barred'."),
            ("'Hold, fair youth,' commanded Robin, 'and share thy purse with the poor of the forest.'", "'Dur güzel genç,' diye emretti Robin, 've keseni ormanın yoksullarıyla paylaş.'", "Coordinate imperatives 'hold and share'; archaic possessive 'thy'."),
            ("The young man stopped, looked at Robin with disdain, and drew a long rapier.", "Genç adam durdu, küçümseyerek Robin'e baktı ve uzun bir meç kılıç çekti.", "Series of coordinated past actions; noun 'disdain'."),
            ("'Out of my way, rustic knave,' replied the youth, 'or I will carve thee like a roast!'", "'Yolumdan çekil seni köylü uşak,' diye yanıtladı genç, 'yoksa seni bir rosto gibi dilimlerim!'", "Vocative insult; simile 'like a roast'."),
            ("Robin drew his broadsword, expecting an easy triumph over the pampered dandy.", "Robin şımartılmış bu züppe karşısında kolay bir zafer bekleyerek kılıcını çekti.", "Participle phrase 'expecting easy triumph'; participial adjective 'pampered'."),
            ("To his astonishment, the youth parried every thrust with lightning elegance.", "Hayretler içinde gördü ki, genç adam her hamleyi şimşek gibi bir zarafetle savuşturuyordu.", "Transitive past 'parried'; noun phrase 'To his astonishment'."),
            ("The stranger danced circles around Robin, disarmed him, and tapped his cheek with the flat blade.", "Yabancı Robin'in etrafında daireler çizdi, silahını düşürdü ve kılıcın yassısıyla yanağına hafifçe dokundu.", "Series of coordinated past verbs showing superior fencing skill."),
            ("Little John leaped forward with his quarterstaff, but Robin raised his hand to stop him.", "Küçük John sopasıyla ileri fırladı fakat Robin onu durdurmak için elini kaldırdı.", "Coordinate clauses with 'but'; infinitive of purpose 'to stop him'."),
            ("'Thou art a master of the blade!' cried Robin generously, 'what is thy true name?'", "'Sen kılıcın tam bir ustasısın!' diye haykırdı Robin cömertçe, 'gerçek adın nedir?'", "Archaic grammar 'Thou art'; adverb 'generously'."),
            ("The young man smiled sadly and replied, 'My name is Will Gamwell of Maxfield.'", "Genç adam hüzünle gülümsedi ve yanıtladı: 'Benim adım Maxfield'lı Will Gamwell.'", "Adverb 'sadly'; predicate nominative."),
            ("Robin gasped in delight: 'Then thou art my own sister's son, my nephew!'", "Robin sevinçle nefesini tuttu: 'O halde sen benim öz kız kardeşimin oğlu, yeğenimsin!'", "Archaic deduction 'thou art'; family relationship."),
            ("They embraced warmly, tears of family reunion filling their eyes.", "Gözlerini aile kavuşmasının gözyaşları doldurarak birbirlerine sıcacık sarıldılar.", "Absolute construction 'tears filling their eyes'; adverb 'warmly'."),
            ("Will explained that he had slain his father's corrupt steward in a fair duel.", "Will, babasının yozlaşmış kahyasını adil bir düelloda öldürdüğünü açıkladı.", "Past perfect 'had slain'; noun phrase 'fair duel'."),
            ("He had fled into Sherwood Forest to seek his famous uncle Robin Hood.", "Meşhur amcası Robin Hood'u aramak için Sherwood Ormanı'na kaçmıştı.", "Infinitive of purpose 'to seek his uncle'; past perfect 'had fled'."),
            ("Robin welcomed him into the greenwood and renamed him Will Scarlet for his brilliant attire.", "Robin onu yeşil ormana kabul etti ve göz alıcı giyimi yüzünden adını Will Scarlet koydu.", "Coordinate past verbs 'welcomed and renamed'; reason phrase 'for his attire'."),
            ("With Will Scarlet beside him, Robin's company grew stronger and bolder than ever.", "Yanında Will Scarlet ile birlikte Robin'in birliği her zamankinden daha güçlü ve cesur oldu.", "Comparative phrase 'stronger and bolder than ever'; absolute modifier.")
        ]
    },
    # Page 11: Allan a Dale's Wedding
    {
        "page_number": 11,
        "title": "Allan a Dale's Wedding",
        "vocab": [
            ("minstrel", "ozan, saz şairi"),
            ("harp", "harp, çalgı"),
            ("bride", "gelin"),
            ("groom", "damat"),
            ("bishop", "piskopos"),
            ("wedding", "düğün"),
            ("rescue", "kurtarmak"),
            ("garland", "çiçek çelengi")
        ],
        "sentences": [
            ("One sunny morning, the outlaws saw a young minstrel walking by, singing cheerfully.", "Güneşli bir sabah kanun kaçakları neşeyle şarkı söyleyerek yürüyüp geçen genç bir ozan gördüler.", "Perception verb 'saw' + participle 'walking by and singing'."),
            ("The next day, they saw the same youth returning, weeping bitterly with his harp broken.", "Ertesi gün aynı gencin arpı kırılmış halde acı acı ağlayarak geri döndüğünü gördüler.", "Absolute construction 'his harp broken'; participle 'returning'."),
            ("Robin stopped the lad and asked the reason for his sudden heartbreaking sorrow.", "Robin delikanlıyı durdurdu ve onun bu ani, yürek parçalayıcı kederinin sebebini sordu.", "Compound adjective 'heartbreaking'; transitive past 'stopped'."),
            ("'My name is Allan a Dale,' wept the youth, 'and my heart is broken in two.'", "'Benim adım Allan a Dale,' diyerek ağladı genç, 've kalbim ikiye bölündü.'", "Passive idiom 'broken in two'; direct speech."),
            ("'The lady I love, fair Ellen, is to be wed today against her will.'", "'Sevdiğim hanımefendi, güzel Ellen, bugün kendi rızası hilafına evlendirilecek.'", "Idiomatic future 'is to be wed'; prepositional phrase 'against her will'."),
            ("'Her greedy father is forcing her to marry a rich, decrepit old knight.'", "'Onun açgözlü babası, zengin ve çökmüş yaşlı bir şövalyeyle evlenmesi için ona baskı yapıyor.'", "Present continuous 'is forcing'; series of adjectives."),
            ("Robin's chivalrous heart burned with indignation at such cruel injustice.", "Robin'in şövalye ruhlu kalbi böylesine zalimce bir adaletsizlik karşısında öfkeyle yandı.", "Metaphor 'burned with indignation'; compound noun 'cruel injustice'."),
            ("'Take heart, Allan,' said Robin, 'thy true love shall marry thee and no other!'", "'Yüreğini ferah tut Allan,' dedi Robin, 'senin gerçek aşkın seninle evlenecek, başkasıyla değil!'", "Imperative 'take heart'; modal 'shall marry'."),
            ("Robin dressed himself in a harper's cloak and hurried to the parish church.", "Robin bir arpçı pelerinine büründü ve cemaat kilisesine doğru aceleyle gitti.", "Reflexive 'dressed himself'; past verb 'hurried'."),
            ("The Bishop of Hereford was presiding over the wedding ceremony with pompous pride.", "Hereford Piskoposu kibirli bir gururla düğün merasimine başkanlık ediyordu.", "Past continuous 'was presiding over'; noun phrase 'pompous pride'."),
            ("The bride arrived in white satin, weeping and trembling beside the ancient groom.", "Gelin beyaz satenler içinde, yaşlı damadın yanında ağlayarak ve titreyerek çıkageldi.", "Participle phrases 'weeping and trembling'; past verb 'arrived'."),
            ("Robin stepped before the altar and cried: 'This wedding shall not proceed!'", "Robin sunağın önüne adım attı ve haykırdı: 'Bu nikah kıyılamaz!'", "Coordinate past verbs; modal prohibition 'shall not proceed'."),
            ("He blew three blasts on his horn, and forty greenwood archers entered the church.", "Borusundan üç ses üfledi ve kırk yeşil orman okçusu kiliseye girdi.", "Coordinate past clauses; compound noun 'greenwood archers'."),
            ("Allan a Dale stepped forward, his eyes shining with passionate devotion.", "Allan a Dale tutkulu bir bağlılıkla gözleri parıldayarak öne doğru adım attı.", "Absolute construction 'his eyes shining'; phrasal verb 'stepped forward'."),
            ("Fair Ellen shrieked with joyful surprise and ran into her true lover's arms.", "Güzel Ellen sevinç dolu bir şaşkınlıkla çığlık attı ve gerçek aşığının kollarına koştu.", "Prepositional phrase 'with joyful surprise'; past verbs 'shrieked and ran'."),
            ("The Bishop and the old knight sputtered with fury, but feared the notched arrows.", "Piskopos ve yaşlı şövalye öfkeden köpürdüler fakat gerilmiş oklardan korktular.", "Coordinate past verbs 'sputtered and feared'; participial adjective 'notched arrows'."),
            ("Friar Tuck stepped forward wearing his holy vestments with a broad grin.", "Rahip Tuck geniş bir sırıtışla kutsal cüppelerini giymiş halde öne çıktı.", "Participle phrase 'wearing vestments'; phrasal verb 'stepped forward'."),
            ("He performed the wedding ceremony right there, marrying Allan to fair Ellen.", "Tam orada nikah merasimini kıydı; Allan ile güzel Ellen'ı evlendirdi.", "Participle clause 'marrying Allan to Ellen'; adverbial 'right there'."),
            ("Robin gifted the bride a golden necklace and hosted a magnificent woodland feast.", "Robin geline altın bir gerdanlık hediye etti ve görkemli bir orman ziyafetine ev sahipliği yaptı.", "Coordinate past verbs 'gifted and hosted'; compound noun 'woodland feast'."),
            ("Allan a Dale sang beautiful songs of love and honor by the greenwood tree.", "Allan a Dale yeşil ağacın yanında aşk ve onur üzerine güzel şarkılar söyledi.", "Prepositional phrase 'by the tree'; adjective 'beautiful'.")
        ]
    },
    # Page 12: The Silver Bugle Horn
    {
        "page_number": 12,
        "title": "The Silver Bugle Call",
        "vocab": [
            ("bugle", "av borusu"),
            ("ambush", "pusu"),
            ("garrison", "garnizon"),
            ("reinforce", "takviye etmek"),
            ("skirmish", "çarpışma, müsademeli kavga"),
            ("archer", "okçu"),
            ("valiant", "yiğit, cesur"),
            ("retreat", "geri çekilmek")
        ],
        "sentences": [
            ("Enraged by Allan a Dale's rescue, the Sheriff gathered two hundred royal soldiers.", "Allan a Dale'in kurtarılmasına öfkelenen Şerif iki yüz kraliyet askeri topladı.", "Past participle modifier 'Enraged by'; numeral 'two hundred'."),
            ("He sent spies into Sherwood to discover the outlaws' secret haunts and pathways.", "Kanun kaçaklarının gizli mekanlarını ve patikalarını keşfetmek için Sherwood'a casuslar gönderdi.", "Infinitive of purpose 'to discover'; possessive noun phrase."),
            ("Robin Hood was walking near the edge of the forest with only Little John.", "Robin Hood sadece Küçük John ile birlikte ormanın sınırına yakın bir yerde yürüyordu.", "Past continuous 'was walking'; prepositional phrase 'near the edge'."),
            ("Suddenly, the forest erupted with the clatter of armored men and drawn swords.", "Birdenbire orman, zırhlı adamların şakırtısı ve çekilmiş kılıçlarla çınladı.", "Prepositional phrase 'with clatter of swords'; past verb 'erupted'."),
            ("A captain shouted, 'Surrender, outlaws, for you are surrounded by the Sheriff's guard!'", "Bir yüzbaşı bağırdı: 'Teslim olun kanun kaçakları, çünkü Şerif'in muhafızları tarafından kuşatıldınız!'", "Imperative 'surrender'; passive voice 'are surrounded by'."),
            ("Robin and Little John backed against a giant oak, their bows bent and ready.", "Robin ve Küçük John dev bir meşeye sırtlarını dayadılar; yayları gerilmiş ve hazırdı.", "Absolute phrase 'bows bent and ready'; phrasal verb 'backed against'."),
            ("'We never surrender to tyrants,' cried Robin, loosing an arrow with deadly aim.", "'Biz tiranlara asla teslim olmayız,' diye haykırdı Robin, ölümcül bir nişanla ok salarak.", "Present simple negative 'never surrender'; participle phrase 'loosing arrow'."),
            ("Little John's shaft struck the captain's shield, piercing the heavy iron plate.", "Küçük John'un oku yüzbaşının kalkanına çarparak ağır demir levhayı delip geçti.", "Participial clause 'piercing heavy plate'; possessive noun phrase."),
            ("The soldiers surged forward, outnumbering the two yeomen twenty to one.", "Askerler iki okçuya karşı yirmiye bir üstünlükle ileri doğru dalga dalga hücum ettiler.", "Participial clause 'outnumbering yeomen'; phrasal verb 'surged forward'."),
            ("Robin drew his silver bugle horn from his belt and set it to his lips.", "Robin kemerinden gümüş av borusunu çıkardı ve onu dudaklarına dayadı.", "Coordinate past verbs 'drew and set'."),
            ("He blew three clear, piercing blasts that echoed across every valley of Sherwood.", "Sherwood'un her vadisinde yankılanan üç berrak ve tiz ses üfledi.", "Relative clause 'that echoed across'; adjective pair 'clear, piercing'."),
            ("The thrilling notes carried miles through the ancient forest like a battle cry.", "Bu heyecan verici nağmeler kadim ormanda bir savaş narası gibi millerce öteye taşındı.", "Simile 'like a battle cry'; measurement phrase 'miles through'."),
            ("From all directions came the rapid patter of running feet in Lincoln green.", "Her yönden Lincoln yeşili içindeki koşan ayakların hızlı tıpırtıları geldi.", "Inverted locative sentence; participial adjective 'running feet'."),
            ("Will Scarlet, Friar Tuck, and one hundred archers burst through the brush with loud cheers.", "Will Scarlet, Rahip Tuck ve yüz okçu gür tezahüratlarla çalılıkları yarıp çıktılar.", "Phrasal verb 'burst through'; compound subject."),
            ("A deadly shower of gray-goose arrows rained down upon the armored soldiers.", "Zırhlı askerlerin üzerine gri kaz tüyü oklardan ölümcül bir sağanak yağdı.", "Metaphor 'shower of arrows rained down'; compound adjective 'gray-goose'."),
            ("The Sheriff's men panicked, broke ranks, and fled in terror toward Nottingham.", "Şerif'in adamları paniklediler, safları bozdular ve dehşet içinde Nottingham'a doğru kaçtılar.", "Series of coordinated past action verbs; directional phrase 'toward Nottingham'."),
            ("Robin forbade his men to pursue the fleeing troops: 'Let them carry the news!'", "Robin adamlarına kaçan birlikleri takip etmeyi yasakladı: 'Bırakın haberi götürsünler!'", "Verb + object + infinitive 'forbade men to pursue'; imperative 'let them carry'."),
            ("The yeomen gathered around their leader, cheering wildly under the sun.", "Okçular liderlerinin etrafında toplandılar, güneşin altında çılgınca tezahürat yaptılar.", "Coordinate actions; adverb 'wildly'."),
            ("Robin held up the silver bugle that had summoned his faithful brothers in peril.", "Robin, tehlike anında sadık kardeşlerini yardıma çağıran o gümüş boruyu havaya kaldırdı.", "Past perfect relative clause 'that had summoned'; prepositional phrase 'in peril'."),
            ("Sherwood remained free, unconquered, and safe in the hands of the Merry Men.", "Sherwood Neşeli Adamlar'ın ellerinde özgür, fethedilmemiş ve güvende kaldı.", "Coordinate predicate adjectives; proper group name 'Merry Men'.")
        ]
    },
    # Page 13: King Richard in Sherwood
    {
        "page_number": 13,
        "title": "The King in Sherwood",
        "vocab": [
            ("monarch", "hükümdar, kral"),
            ("crusade", "haçlı seferi"),
            ("buffet", "yumruk darbesi"),
            ("monk", "keşiş"),
            ("cowl", "keşiş kukuletası"),
            ("pardon", "af, bağışlama"),
            ("allegiance", "bağlılık, sadakat"),
            ("loyalty", "sadakat")
        ],
        "sentences": [
            ("King Richard the Lionheart returned to England from the Holy Land Crusades.", "Aslan Yürekli Kral Richard Kutsal Topraklar Haçlı Seferleri'nden İngiltere'ye döndü.", "Proper royal title; prepositional phrase 'from the Crusades'."),
            ("Hearing endless tales of Robin Hood's defiance, the King decided to see him personally.", "Robin Hood'un meydan okumalarına dair bitmek bilmez hikayeleri duyan Kral, onu bizzat görmeye karar verdi.", "Participle clause of cause 'Hearing tales'; infinitive 'to see him personally'."),
            ("The King and seven knights disguised themselves as holy monks in heavy brown cowls.", "Kral ve yedi şövalye kendilerini ağır kahverengi kukuletalı kutsal keşişler kılığına soktular.", "Reflexive 'disguised themselves'; prepositional phrase 'in heavy cowls'."),
            ("They rode into Sherwood Forest, their saddlebags jingling with royal coin.", "Eyer çantaları kraliyet sikkeleriyle şıngırdayarak Sherwood Ormanı'na doğru at sürdüler.", "Absolute construction 'saddlebags jingling'; directional phrase 'into forest'."),
            ("Robin Hood stepped out from the trees and seized the King's horse by the bridle.", "Robin Hood ağaçların arasından çıktı ve Kral'ın atını dizgininden yakaladı.", "Coordinate past verbs 'stepped out and seized'."),
            ("'Halt, holy fathers,' said Robin, 'we must levy a toll on rich churchmen for the poor.'", "'Durun kutsal pederler,' dedi Robin, 'yoksullar için zengin din adamlarından vergi almalıyız.'", "Modal obligation 'must levy'; purpose phrase 'for the poor'."),
            ("The tall monk laughed heartily and produced a heavy purse of forty gold pounds.", "Uzun boylu keşiş içtenlikle güldü ve kırk altın sterlinlik ağır bir kese çıkardı.", "Coordinate past verbs 'laughed and produced'; numeral 'forty'."),
            ("'I give thee half for charity, and keep half for the King's journey,' said the monk.", "'Yarısını hayır için sana veriyorum, yarısını da Kral'ın yolculuğu için saklıyorum,' dedi keşiş.", "Coordinate present verbs 'give and keep'; possessive 'King's journey'."),
            ("Robin took only twenty pounds and returned the rest with great respect for King Richard.", "Robin sadece yirmi sterlini aldı ve Kral Richard'a duyduğu büyük saygıyla kalanını iade etti.", "Coordinate past verbs 'took and returned'; noun phrase 'great respect'."),
            ("'We love King Richard with all our hearts,' Robin declared, 'and curse his treacherous brother!'", "'Kral Richard'ı bütün kalbimizle seviyoruz,' dedi Robin, 've hain kardeşine lanet okuyoruz!'", "Coordinate declarations of loyalty; adverbial phrase 'with all our hearts'."),
            ("Robin invited the monks to a royal forest banquet under the great trysting tree.", "Robin keşişleri ulu buluşma ağacının altında bir kraliyet orman ziyafetine davet etti.", "Transitive past 'invited'; compound noun 'forest banquet'."),
            ("The outlaws held an archery shooting game, where missing the bullseye cost a buffet on the ear.", "Kanun kaçakları, hedefi ıskalamanın kulağa bir yumruk darbesine mal olduğu bir okçuluk oyunu düzenlediler.", "Relative clause 'where missing cost a buffet'; gerund subject 'missing'."),
            ("When Robin missed by a hair's breadth, he offered his head to the giant monk for punishment.", "Robin kıl payı ıskaladığında, ceza için başını dev keşişe uzattı.", "Time clause with 'missed'; noun phrase 'hair's breadth'."),
            ("The King rolled up his sleeve, revealing an arm like an iron anvil.", "Kral kolunu sıvadı, demir bir örs gibi bir kolu açığa çıkardı.", "Participle clause 'revealing an arm'; simile 'like an iron anvil'."),
            ("He delivered a buffet that sent Robin sprawling across the grass head over heels.", "Robin'i çimlerin üzerinden tepeüstü yuvarlayan müthiş bir yumruk darbesi indirdi.", "Relative clause 'that sent Robin sprawling'; adverbial idiom 'head over heels'."),
            ("Robin scrambled up laughing and rubbing his jaw: 'Thou hast an arm of steel, monk!'", "Robin gülerek ve çenesini ovarak ayağa kalktı: 'Çelik gibi bir kolun var keşiş!'", "Coordinate participles 'laughing and rubbing'; archaic 'thou hast'."),
            ("Just then, Sir Richard of the Lea arrived, recognized his monarch, and knelt in the grass.", "Tam o sırada Lea'lı Sör Richard geldi, hükümdarını tanıdı ve çimlerin üzerine diz çöktü.", "Series of coordinated past actions; transitive 'recognized'."),
            ("The King threw back his cowl, revealing the majestic countenance of Richard the Lionheart.", "Kral kukuletasını geriye attı, Aslan Yürekli Richard'ın haşmetli simasını açığa çıkardı.", "Coordinate participles; adjective 'majestic countenance'."),
            ("All the outlaws fell upon their knees, offering their lives and swords to the King.", "Bütün kanun kaçakları dizlerinin üzerine çöktüler; hayatlarını ve kılıçlarını Kral'a sundular.", "Participle phrase 'offering lives and swords'; phrasal verb 'fell upon'."),
            ("King Richard smiled warmly and granted full royal pardons to Robin and all his men.", "Kral Richard sıcak bir tebessüm etti ve Robin ile tüm adamlarına eksiksiz kraliyet affı bahşetti.", "Coordinate past verbs 'smiled and granted'; compound noun 'royal pardons'.")
        ]
    },
    # Page 14: The Outlaws at the Royal Court
    {
        "page_number": 14,
        "title": "Archers of the Crown",
        "vocab": [
            ("court", "saray, divan"),
            ("pageant", "tören, gösteri"),
            ("tournament", "turnuva"),
            ("yeoman", "okçu muhafız"),
            ("shield", "kalkan"),
            ("service", "hizmet"),
            ("splendor", "ihtişam"),
            ("glory", "şan, şeref")
        ],
        "sentences": [
            ("Robin Hood and his merry men followed King Richard to London in royal procession.", "Robin Hood ve neşeli adamları kraliyet alayı eşliğinde Kral Richard'ı Londra'ya kadar takip ettiler.", "Prepositional phrase 'in royal procession'; past verb 'followed'."),
            ("They exchanged their Lincoln green for fine liveries of scarlet and gold.", "Lincoln yeşili giysilerini al ve altın işlemeli şık üniformalarla değiştirdiler.", "Transitive past 'exchanged for'; coordinate color adjectives."),
            ("Robin was appointed an Earl and Captain of the King's Royal Guard of Archers.", "Robin bir Kont ve Kraliyet Okçu Muhafızları Kaptanı olarak atandı.", "Passive voice 'was appointed'; compound royal titles."),
            ("Little John and Will Scarlet served as officers under his command at Windsor Castle.", "Küçük John ve Will Scarlet Windsor Şatosu'nda onun komutası altında subay olarak görev yaptılar.", "Prepositional phrases indicating role and location; past verb 'served'."),
            ("At royal tournaments, the Sherwood archers amazed the nobility with their unmatched skill.", "Kraliyet turnuvalarında Sherwood okçuları eşsiz maharetleriyle soyluları hayrete düşürdüler.", "Adjective 'unmatched skill'; past verb 'amazed'."),
            ("No French or Scottish knight could withstand the whistling volleys of their heavy shafts.", "Hiçbir Fransız veya İskoç şövalye onların ağır oklarının ıslık çalan yaylım ateşine dayanamazdı.", "Modal negative 'could withstand'; compound noun 'whistling volleys'."),
            ("The people of London cheered whenever the famous outlaws marched through the cobbled streets.", "Meşhur kanun kaçakları taş döşeli sokaklardan ne zaman geçseler Londra halkı tezahürat yapardı.", "Time clause with 'whenever'; past verb 'cheered'."),
            ("Yet as months passed in palace halls, Robin began to feel restless and suffocated.", "Yine de saray salonlarında aylar geçtikçe Robin huzursuz ve boğulmuş hissetmeye başladı.", "Time clause with 'as'; coordinate adjectives 'restless and suffocated'."),
            ("He missed the fresh forest breeze, the whispering leaves, and the singing birds of Sherwood.", "Sherwood'un taze orman esintisini, fısıldayan yapraklarını ve şarkı söyleyen kuşlarını özlüyordu.", "Series of direct objects with descriptive participles; past verb 'missed'."),
            ("Court intrigues and formal banquet robes weighed heavily upon his free spirit.", "Saray entrikaları ve resmi ziyafet kaftanları onun özgür ruhuna ağır bir yük gibi bindi.", "Coordinate subjects; adverb 'heavily'."),
            ("He gazed out of palace windows toward the north, yearning for his ancient green home.", "Saray pencerelerinden kuzeye doğru baktı, kadim yeşil yuvasının hasretiyle yanıp tutuştu.", "Participle phrase 'yearning for green home'; phrasal verb 'gazed out of'."),
            ("Little John felt the same longing, dreaming nightly of the wide rushing brooks.", "Küçük John da aynı hasreti hissetti, her gece gürül gürül akan geniş derelerin rüyasını gördü.", "Participle phrase 'dreaming nightly'; adjective 'same'."),
            ("Robin knelt before King Richard and begged for leave to visit Sherwood once more.", "Robin Kral Richard'ın önünde diz çöktü ve Sherwood'u bir kez daha ziyaret etmek için izin istedi.", "Coordinate past verbs 'knelt and begged'; infinitive 'to visit'."),
            ("'My heart sickens for the greenwood, Sire,' pleaded Robin with tears in his eyes.", "'Yüreğim yeşil orman için yanıp tutuşuyor Efendimiz,' diye yalvardı Robin gözlerinde yaşlarla.", "Direct speech; prepositional phrase 'with tears in eyes'."),
            ("'Go for seven days, Earl Robin,' granted the King, 'and return to thy duty.'", "'Yedi günlüğüne git Kont Robin,' diye izin verdi Kral, 've sonra görevine dön.'", "Imperative coordinates 'go and return'; royal title 'Earl Robin'."),
            ("Robin kissed the King's hand, stripped off his golden court robes, and ran north.", "Robin Kral'ın elini öptü, altın saray kaftanlarını üzerinden çıkardı ve kuzeye koştu.", "Series of coordinated past actions showing eagerness."),
            ("He traveled swiftly until the towering emerald oaks of Sherwood rose on the horizon.", "Ufukta Sherwood'un heybetli zümrüt meşeleri yükselene kadar hızla yol aldı.", "Time clause with 'until'; compound adjective 'towering emerald oaks'."),
            ("He fell to his knees upon the sweet damp moss and wept for pure overwhelming happiness.", "Tatlı nemli yosunların üzerine diz çöktü ve katıksız, ezici bir mutlulukla ağladı.", "Coordinate past verbs 'fell and wept'; adjective string 'pure overwhelming'."),
            ("He raised his silver bugle horn and blew the ancient rallying call of the outlaws.", "Gümüş av borusunu kaldırdı ve kanun kaçaklarının kadim toplanma çağrısını üfledi.", "Coordinate past verbs 'raised and blew'; compound noun 'rallying call'."),
            ("From every thicket and glade, old friends in Lincoln green came running to his side.", "Her çalıdan ve orman açıklığından Lincoln yeşili içindeki eski dostlar koşarak yanına geldiler.", "Participle phrase 'running to his side'; inverted locative structure.")
        ]
    },
    # Page 15: The Return to the Greenwood (Robin's Legend)
    {
        "page_number": 15,
        "title": "The Last Arrow of Robin Hood",
        "vocab": [
            ("legend", "efsane"),
            ("greenwood", "yeşil orman"),
            ("oak", "meşe ağacı"),
            ("grave", "mezar"),
            ("arrow", "ok"),
            ("memory", "hafıza, hatıra"),
            ("immortal", "ölümsüz"),
            ("brotherhood", "kardeşlik")
        ],
        "sentences": [
            ("Robin never returned to the King's court, choosing freedom under the forest canopy instead.", "Robin Kralın sarayına bir daha asla dönmedi, bunun yerine orman örtüsü altındaki özgürlüğü seçti.", "Participle clause of choice 'choosing freedom'; negative past with 'never'."),
            ("For twenty more happy years, he lived as protector of the poor in Sherwood Forest.", "Yirmi mutlu yıl daha Sherwood Ormanı'nda yoksulların koruyucusu olarak yaşadı.", "Prepositional phrase 'as protector of the poor'; duration phrase."),
            ("Neither corrupt sheriffs nor greedy barons ever succeeded in breaking his merry brotherhood.", "Ne yozlaşmış şerifler ne de açgözlü baronlar onun neşeli kardeşliğini bozmayı asla başarabildiler.", "Correlative subjects 'neither... nor'; infinitive 'in breaking'."),
            ("As old age approached, Robin was stricken with a burning fever that sapped his strength.", "Yaşlılık yaklaştığında Robin gücünü tüketen yakıcı bir ateşe yakalandı.", "Passive voice 'was stricken with'; relative clause 'that sapped his strength'."),
            ("Little John carried his beloved master to Kirklees Priory for healing care.", "Küçük John şifa bulması için sevgili efendisini Kirklees Manastırı'na taşıdı.", "Infinitive of purpose 'for healing care'; past verb 'carried'."),
            ("The treacherous Prioress, allied with Robin's enemies, opened his veins to bleed him.", "Robin'in düşmanlarıyla birlik olmuş hain Başrahibe, kanını akıtmak için damarlarını kesti.", "Past participle modifier 'allied with enemies'; infinitive 'to bleed him'."),
            ("She locked him in an upper tower room, leaving the hero to perish from loss of blood.", "Onu üstteki bir kule odasına kilitledi, kahramanı kan kaybından ölüme terk etti.", "Participle clause 'leaving hero to perish'; noun phrase 'loss of blood'."),
            ("Sensing the treachery, Robin weakly gathered his remaining strength one final time.", "İhaneti sezen Robin, kalan gücünü son bir kez zayıfça topladı.", "Participle clause of perception; adverb 'weakly'."),
            ("He raised his silver bugle to his pale lips and blew three faint, dying blasts.", "Gümüş borusunu solgun dudaklarına kaldırdı ve üç zayıf, tükenen ses üfledi.", "Coordinate past verbs 'raised and blew'; adjective pair 'faint, dying'."),
            ("Miles away, Little John heard the feeble notes and knew his master was in mortal peril.", "Millerce ötede Küçük John bu cılız nağmeleri duydu ve efendisinin ölümcül tehlikede olduğunu anladı.", "Coordinate past verbs 'heard and knew'; noun phrase 'mortal peril'."),
            ("He broke down the heavy priory doors and rushed up the stairs into the chamber.", "Ağır manastır kapılarını kırdı ve merdivenleri hızla çıkarak odaya daldı.", "Coordinate past actions; directional phrase 'up the stairs'."),
            ("He knelt beside Robin, weeping tears of agony: 'Master, let me burn this wicked place!'", "Robin'in yanına diz çöktü, ızdırap gözyaşlarıyla ağlayarak: 'Efendim, bu uğursuz yeri yakayım!' dedi.", "Participle phrase 'weeping tears'; imperative 'let me burn'."),
            ("'No, dear John,' whispered Robin gently, 'I have never harmed a woman in all my days.'", "'Hayır sevgili John,' diye fısıldadı Robin usulca, 'bütün ömrüm boyunca tek bir kadına bile zarar vermedim.'", "Present perfect with 'never'; adverb 'gently'."),
            ("'Hand me my trusty yew bow, and let me loose one last shaft through the casement.'", "'Bana emektar porsuk yayımı ver ve pencereden son bir ok fırlatmama izin ver.'", "Coordinate imperatives 'hand and let'; noun 'casement'."),
            ("With Little John supporting his shoulders, Robin drew the string with his dying hands.", "Küçük John omuzlarını desteklerken Robin can çekişen elleriyle kirişi çekti.", "Absolute construction 'Little John supporting'; past verb 'drew'."),
            ("The arrow sped out through the open window, arcing gracefully into the green forest.", "Ok açık pencereden dışarı uçtu, yeşil ormanın içine doğru zarifçe kavis çizdi.", "Coordinate participles 'arcing gracefully'; past verb 'sped out'."),
            ("'Bury me where that arrow falls,' whispered Robin, 'with my bow across my breast.'", "'Beni o okun düştüğü yere gömün,' diye fısıldadı Robin, 'yayım da göğsümün üzerinde olsun.'", "Relative clause of place 'where that arrow falls'; imperative 'bury me'."),
            ("He closed his eyes peacefully, his noble soul departing for a higher realm of justice.", "Soylu ruhu adaletin daha yüce bir diyarına göçerek gözlerini huzur içinde kapattı.", "Absolute construction 'soul departing'; adverb 'peacefully'."),
            ("Little John buried him beneath the great oak where the arrow was found buried in moss.", "Küçük John onu okun yosunların içine saplanmış bulunduğu ulu meşenin altına gömdü.", "Passive relative clause 'where arrow was found buried'; past verb 'buried'."),
            ("And so lives on the immortal legend of Robin Hood, eternal champion of the oppressed.", "Ve böylece ezilenlerin ebedi savunucusu Robin Hood'un ölümsüz efsanesi sonsuza dek yaşamaya devam eder.", "Concluding inverted sentence; title epithet 'eternal champion of the oppressed'.")
        ]
    }
]

def generate_data_file():
    data_path = os.path.join(os.path.dirname(__file__), "book_17_data.py")
    
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
        f.write('"""\nBook 17: The Merry Adventures of Robin Hood (Howard Pyle)\n')
        f.write('Level 1 Graded Reader — 15 Pages x 20 Sentences = 300 Sentences.\n"""\n\n')
        f.write('BOOK_TITLE = "The Merry Adventures of Robin Hood (15 Sayfa / 300 Cümle / Graded Reader)"\n')
        f.write('AUTHOR = "Howard Pyle"\n\n')
        f.write(f"PAGES_DATA = {pprint.pformat(pages_data, indent=4, width=120)}\n")
        
    print(f"Successfully wrote {data_path}")

if __name__ == "__main__":
    generate_data_file()
