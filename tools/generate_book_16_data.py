"""
Book 16 Generator: Peter Pan: The Boy Who Would Not Grow Up (J. M. Barrie)
15 Pages, exactly 20 sentences per page = 300 sentences total.
8 Target vocabulary terms per page = 120 vocabulary items total.
Level 1 / Seviye 1 Graded Reader for English learners.
"""

import os
import pprint

BOOK_META = {
    "id": "book_16_peter_pan",
    "title": "Peter Pan: The Boy Who Would Not Grow Up",
    "subtitle": "J. M. Barrie's Timeless Tale of Neverland, Flying, and Eternal Youth",
    "author": "J. M. Barrie",
    "level": "Seviye 1 (A1-A2 Beginner)",
    "target_readers": "İngilizce öğrenenler ve fantastik ada maceralarını sevenler için çift dilli okuma kitabı",
    "total_pages": 15,
    "sentences_per_page": 20,
    "total_sentences": 300,
    "theme_color_primary": "#0D9488",    # Neverland Teal / Lagoon Cyan
    "theme_color_secondary": "#B45309",  # Pirate Gold / Amber
    "theme_color_accent": "#BE123C",     # Hook Crimson
    "theme_color_light": "#F0FDFA"       # Fairy Dust Mist Tint
}

TR_TITLES = [
    "Peter Fidanlıktan İçeri Süzülüyor",
    "Kayıp Gölge ve Yüksük Öpücüğü",
    "Uçmayı Öğrenmek ve Kaçış",
    "Varolmayan Ülke'ye Uçuş",
    "Adanın Gizemli Yaşamı",
    "Wendy Kuşu ve Meşe Palamudu",
    "Yer Altındaki Sıcak Ev",
    "Denizkızları Lagünü",
    "Kaplan Zambağı'nın Kurtarılışı",
    "Yükselen Gelgit ve Asla Kuşu",
    "Wendy'nin Hikayesi ve Hasret",
    "Korsan Baskını ve Pusu",
    "Tinker Bell'in Büyük Fedakarlığı",
    "Korsan Gemisinde Büyük Savaş",
    "Açık Kalan Pencere ve Eve Dönüş"
]

PAGES = [
    # Page 1: Peter Breaks Through
    {
        "page_number": 1,
        "title": "Peter Breaks Through",
        "vocab": [
            ("nursery", "çocuk odası"),
            ("grow", "büyümek"),
            ("tidiness", "düzenlilik, intizam"),
            ("shadow", "gölge"),
            ("drawer", "çekmece"),
            ("drawer", "çekmece"),
            ("maid", "hizmetçi"),
            ("soothe", "teskin etmek, yatıştırmak")
        ],
        "sentences": [
            ("All children, except one, grow up sooner or later in this world.", "Bu dünyada, biri hariç bütün çocuklar er ya da geç büyür.", "Exceptive preposition 'except one'; adverbial phrase 'sooner or later'."),
            ("They soon know that they will grow up, and the way Wendy knew was this.", "Büyüyeceklerini çok geçmeden öğrenirler; Wendy'nin öğrenme şekli ise şöyle oldu.", "Noun clause 'that they will grow up'; cataphoric reference 'was this'."),
            ("One day when she was two years old she was playing in a garden.", "Bir gün, iki yaşındayken bir bahçede oyun oynuyordu.", "Past continuous 'was playing'; age clause 'when she was two'."),
            ("She plucked another flower and ran with it happily to her mother.", "Bir çiçek daha kopardı ve onunla birlikte neşeyle annesine koştu.", "Coordinate past verbs 'plucked and ran'; adverb 'happily'."),
            ("Mrs. Darling put her hand to her heart and cried, 'Oh, why can't you remain like this forever!'", "Bayan Darling elini kalbine koydu ve 'Ah, keşke hep böyle kalsan!' diye haykırdı.", "Idiom 'put hand to heart'; negative modal question expressing wish."),
            ("This was all that passed between them on the subject, but henceforth Wendy knew.", "Bu konuda aralarında geçen konuşmanın tamamı buydu, fakat bundan böyle Wendy biliyordu.", "Relative clause 'all that passed'; adverb 'henceforth'."),
            ("You always know after you are two, because two is the beginning of the end.", "İki yaşından sonra bunu her zaman bilirsiniz, çünkü iki yaş sonun başlangıcıdır.", "Causal clause with 'because'; philosophical idiom 'beginning of the end'."),
            ("The Darlings lived at number fourteen in a quiet London street.", "Darling ailesi, sakin bir Londra sokağındaki on dört numarada yaşıyordu.", "Prepositional phrases indicating address; adjective 'quiet'."),
            ("They had three children named Wendy, John, and little Michael.", "Wendy, John ve küçük Michael adında üç çocukları vardı.", "Past participle phrase 'named Wendy, John, and little Michael'."),
            ("They were so poor that they kept a Newfoundland dog named Nana as their nurse.", "Öyle yoksuldular ki, çocukların dadısı olarak Nana adında bir Newfoundland köpeği tutmuşlardı.", "Result clause 'so poor that'; appositive phrase 'named Nana'."),
            ("Nana was a treasure of a nurse who gave the children their evening baths.", "Nana, akşamları çocukları banyo yaptıran hazine değerinde bir dadıydı.", "Idiom 'a treasure of a nurse'; relative clause with 'who'."),
            ("She carried an umbrella in her mouth when she walked them to school.", "Çocukları okula götürürken ağzında bir şemsiye taşırdı.", "Prepositional phrase 'in her mouth'; time clause 'when she walked them'."),
            ("Mrs. Darling loved tidiness and tidied up her children's minds every night.", "Bayan Darling düzeni çok severdi ve her gece çocuklarının zihinlerini toparlardı.", "Metaphorical verb 'tidied up minds'; coordinate past actions."),
            ("It is the nightly custom of every good mother after her children are asleep.", "Bu, çocukları uyuduktan sonra her iyi annenin gece uyguladığı bir adettir.", "Dummy subject 'It is...'; temporal subordinate clause."),
            ("In the children's minds, she found many strange and colorful things.", "Çocukların zihninde pek çok garip ve renkli şey buldu.", "Prepositional phrase 'in the minds'; coordinate adjectives 'strange and colorful'."),
            ("There were islands, savage beasts, coral reefs, and tiny magic houses.", "Adalar, yırtıcı hayvanlar, mercan resifleri ve minik sihirli evler vardı.", "List of nouns in existential 'There were'."),
            ("Of all the delectable islands the Neverland is the snuggest and most compact.", "Tüm o nefis adalar arasında Varolmayan Ülke en sıcak ve en derli toplu olanıdır.", "Superlatives 'snuggest and most compact'; adjective 'delectable'."),
            ("Mrs. Darling first heard of Peter Pan when tidying up her children's thoughts.", "Bayan Darling, Peter Pan'ın adını ilk kez çocuklarının düşüncelerini toparlarken duydu.", "Time clause with participle 'when tidying up'; proper name 'Peter Pan'."),
            ("One night, she saw a strange boy sitting upon the nursery floor in the moonlight.", "Bir gece, ay ışığında çocuk odasının zemininde oturan tuhaf bir oğlan gördü.", "Perception verb 'saw' + participle 'sitting upon'; adjective 'strange'."),
            ("Before she could reach him, the boy leaped lightly out of the window into the night.", "Kadın ona ulaşamadan önce oğlan pencereden dışarı, gecenin içine doğru hafifçe atlayıverdi.", "Subordinate clause 'before she could reach'; phrasal verb 'leaped out of'.")
        ]
    },
    # Page 2: The Shadow and the Thimble
    {
        "page_number": 2,
        "title": "The Shadow and the Thimble",
        "vocab": [
            ("shadow", "gölge"),
            ("thimble", "dikiş yüksüğü"),
            ("sew", "dikmek"),
            ("soap", "sabun"),
            ("weep", "ağlamak"),
            ("drawer", "çekmece"),
            ("kiss", "öpücük"),
            ("cocky", "kendini beğenmiş, cüretkar")
        ],
        "sentences": [
            ("When Peter leaped through the window, Nana slammed the sash down quickly.", "Peter pencereden atladığında Nana pencere kanadını hızla aşağı çarptı.", "Time clause; phrasal verb 'slammed down'."),
            ("The window snapped Peter's shadow clean off, leaving it trapped in the room.", "Pencere Peter'ın gölgesini tam dibinden kopardı ve odada kapana kısılmış bıraktı.", "Participle clause of result 'leaving it trapped'; adverb 'clean off'."),
            ("Mrs. Darling rolled up the shadow carefully and hid it in a nursery drawer.", "Bayan Darling gölgeyi dikkatle rulo yaptı ve onu çocuk odasındaki bir çekmeceye sakladı.", "Phrasal verb 'rolled up'; prepositional phrase 'in a drawer'."),
            ("A few nights later, while the parents were at a party, Peter returned.", "Birkaç gece sonra, anne baba bir partideyken Peter geri döndü.", "Temporal clause with 'while'; past verb 'returned'."),
            ("A tiny sparkling light, no bigger than a fist, darted into the quiet room.", "Bir yumruktan daha büyük olmayan minicik, ışıltılı bir ışık sessiz odaya daldı.", "Comparative phrase 'no bigger than'; past verb 'darted'."),
            ("It was Tinker Bell, an exquisite fairy dressed in a skeleton leaf.", "Bu, iskelet gibi ince bir yapraktan elbise giymiş enfes bir peri olan Tinker Bell'di.", "Appositive clause; passive participle 'dressed in'."),
            ("Peter flew in silently after her, searching frantically for his missing shadow.", "Peter kayıp gölgesini çılgınca arayarak onun ardından sessizce içeri uçtu.", "Participle phrase 'searching frantically'; prepositional phrase 'after her'."),
            ("He rummaged through the drawers and finally found it rolled up in linen.", "Çekmeceleri altüst etti ve sonunda gölgesini ketenlerin arasına sarılmış halde buldu.", "Phrasal verb 'rummaged through'; past participle 'rolled up'."),
            ("He tried to stick the shadow back on his feet with ordinary bathroom soap.", "Gölgeyi alelade bir banyo sabunuyla ayaklarına tekrar yapıştırmaya çalıştı.", "Infinitive 'to stick back on'; instrument phrase 'with bathroom soap'."),
            ("When soap completely failed, Peter sat on the nursery floor and sobbed aloud.", "Sabun tamamen işe yaramayınca, Peter çocuk odasının zeminine oturdu ve sesli sesli ağladı.", "Time clause 'when soap failed'; past verbs 'sat and sobbed'."),
            ("His sorrowful cries woke Wendy, who sat up in her warm bed.", "Onun kederli haykırışları, sıcak yatağında doğrulan Wendy'yi uyandırdı.", "Relative clause 'who sat up'; adjective 'sorrowful'."),
            ("'Boy, why are you crying?' asked Wendy politely across the moonlit room.", "'Çocuk, neden ağlıyorsun?' diye sordu Wendy ay ışığıyla aydınlanan odada kibarca.", "Direct question; adverb 'politely'."),
            ("Peter stood up and bowed very gracefully to the little girl.", "Peter ayağa kalktı ve küçük kıza çok zarif bir şekilde reverans yaptı.", "Coordinate past verbs 'stood up and bowed'; adverb 'gracefully'."),
            ("'I am not crying about myself, but I cannot get my shadow to stick,' he said.", "'Kendim için ağlamıyorum, fakat gölgemin yapışmasını sağlayamıyorum,' dedi.", "Causative structure 'get my shadow to stick'; negative contrast 'not about... but'."),
            ("Wendy examined the dark silhouette and offered to sew it to his toes.", "Wendy karanlık silueti inceledi ve onu ayak parmaklarına dikmeyi teklif etti.", "Coordinate past verbs 'examined and offered'; infinitive 'to sew'."),
            ("She fetched her needle and thread and stitched the shadow firmly in place.", "İğnesini ve ipliğini getirdi, gölgeyi sağlam bir şekilde yerine dikti.", "Coordinate past verbs 'fetched and stitched'; phrase 'in place'."),
            ("As soon as the shadow was attached, Peter leaped up and crowed with cocky triumph.", "Gölge tutturulur tutturulmaz, Peter yukarı fırladı ve cüretkar bir zaferle horoz gibi öttü.", "Conjunction 'as soon as'; phrase 'crowed with triumph'."),
            ("'How clever I am!' shouted Peter, entirely forgetting Wendy's assistance.", "'Ne kadar da akıllıyım!' diye haykırdı Peter, Wendy'nin yardımını tamamen unutarak.", "Exclamatory structure; participle clause 'entirely forgetting'."),
            ("Wendy felt slightly hurt, but Peter offered her an acorn button as a kiss.", "Wendy biraz incindi, fakat Peter ona bir öpücük niyetine meşe palamudundan bir düğme verdi.", "Copular verb 'felt hurt'; noun phrase 'acorn button'."),
            ("Wendy wore the acorn button on a ribbon around her neck forever after.", "Wendy o meşe palamudu düğmesini o andan sonra boynunda bir kurdeleyle daima taşıdı.", "Prepositional phrases indicating location and time.")
        ]
    },
    # Page 3: Come Away, Come Away! (Tinker Bell's Fairy Dust and Learning to Fly)
    {
        "page_number": 3,
        "title": "Come Away, Come Away!",
        "vocab": [
            ("fairy", "peri"),
            ("dust", "peri tozu"),
            ("pirate", "korsan"),
            ("lagoon", "lagün, deniz kulağı"),
            ("tuck", "yorganı örtmek, sokmak"),
            ("soar", "gökyüzünde süzülmek"),
            ("glide", "kayarcasına uçmak"),
            ("chimney", "baca")
        ],
        "sentences": [
            ("Wendy asked Peter where he lived, and he answered with charming carelessness.", "Wendy Peter'a nerede yaşadığını sordu, o da büyüleyici bir umursamazlıkla cevap verdi.", "Indirect question; noun phrase 'charming carelessness'."),
            ("'Second to the right, and straight on till morning,' said Peter proudly.", "'Sağdan ikinci ve sabaha kadar dosdoğru,' dedi Peter gururla.", "Famous directional quote; adverb 'proudly'."),
            ("He told her that he had run away the day he was born to avoid growing up.", "Büyümekten kaçınmak için doğduğu gün evden kaçtığını ona anlattı.", "Past perfect 'had run away'; infinitive of purpose 'to avoid growing up'."),
            ("He lived in the Neverland with the Lost Boys, who had fallen out of their prams.", "Bebek arabalarından düşmüş olan Kayıp Çocuklar ile birlikte Varolmayan Ülke'de yaşıyordu.", "Relative clause 'who had fallen out'; compound noun 'Lost Boys'."),
            ("'They have no mothers, Wendy, and nobody tells them bedtime stories,' Peter said.", "'Onların anneleri yok Wendy ve kimse onlara uyku vakti hikayeleri anlatmıyor,' dedi Peter.", "Coordinate clauses; compound noun 'bedtime stories'."),
            ("'I could tell them stories and tuck them in at night!' exclaimed Wendy.", "'Onlara hikayeler anlatabilir ve geceleri üzerlerini örtebilirim!' diye haykırdı Wendy.", "Modal 'could tell'; phrasal verb 'tuck in'."),
            ("Wendy woke her brothers John and Michael to share the wondrous news.", "Wendy harika haberi paylaşmak için erkek kardeşleri John ve Michael'ı uyandırdı.", "Infinitive of purpose 'to share'; adjective 'wondrous'."),
            ("'Can you teach us how to fly?' asked John with wide, eager eyes.", "'Bize nasıl uçulacağını öğretebilir misin?' diye sordu John kocaman, hevesli gözlerle.", "Modal question; indirect question clause 'how to fly'."),
            ("'Of course I can,' Peter laughed, 'you just need lovely thoughts and fairy dust.'", "'Elbette öğretebilirim,' diye güldü Peter, 'sadece güzel düşüncelere ve peri tozuna ihtiyacınız var.'", "Coordinate requirements; noun phrase 'fairy dust'."),
            ("Tinker Bell was annoyed, but Peter blew fairy dust over each child.", "Tinker Bell bu duruma sinirlendi fakat Peter her bir çocuğun üzerine peri tozu üfledi.", "Passive adjective 'was annoyed'; preposition 'over each child'."),
            ("'Now wiggle your shoulders and think of wonderful happy things!' called Peter.", "'Şimdi omuzlarınızı oynatın ve harika, mutlu şeyler düşünün!' diye seslendi Peter.", "Imperative coordinates; preposition 'of'."),
            ("Michael tried first and immediately floated up toward the high ceiling.", "İlk Michael denedi ve hemen yüksek tavana doğru yukarı süzüldü.", "Phrasal verb 'floated up toward'; ordinal 'first'."),
            ("John kicked his legs and hovered over the chest of drawers with delight.", "John bacaklarını tekmeledi ve sevinçle çekmeceli dolabın üzerinde havada asılı kaldı.", "Coordinate past verbs 'kicked and hovered'; phrase 'with delight'."),
            ("Wendy rose like a gentle swan, gliding gracefully around the lampshade.", "Wendy narin bir kuğu gibi yükseldi, abajurun etrafında zarifçe süzüldü.", "Simile 'like a gentle swan'; participle phrase 'gliding gracefully'."),
            ("They circled the nursery, laughing and tumbling in the warm air.", "Sıcak havada gülüşerek ve taklalar atarak çocuk odasının etrafında daireler çizdiler.", "Participle phrases describing actions; past verb 'circled'."),
            ("From outside, the stars in the night sky seemed to be calling them.", "Dışarıdan, gece gökyüzündeki yıldızlar sanki onları çağırıyor gibiydi.", "Infinitive construction 'seemed to be calling'."),
            ("'There are pirates, mermaids, and redskins waiting for us!' Peter promised.", "'Bizi bekleyen korsanlar, denizkızları ve kızılderililer var!' diye söz verdi Peter.", "Participial modifier 'waiting for us'; existential 'there are'."),
            ("Peter flew out through the open window, soaring into the dark blue sky.", "Peter açık pencereden dışarı uçtu, koyu mavi gökyüzüne doğru süzüldü.", "Phrasal verb 'flew out through'; participle 'soaring into'."),
            ("Without a single glance backward, the three children flew out after him.", "Geriye tek bir bakış bile atmadan, üç çocuk onun peşinden dışarı uçtular.", "Preposition 'without' + noun; phrasal verb 'flew out after'."),
            ("Behind them, the open nursery window stood empty in the sleeping city.", "Arkalarında, açık çocuk odası penceresi uyuyan şehrin ortasında bomboş kaldı.", "Participial adjective 'sleeping city'; adjective 'empty'.")
        ]
    },
    # Page 4: The Flight to Neverland (Flying Over the Ocean, Spotting the Magical Island)
    {
        "page_number": 4,
        "title": "The Flight to Neverland",
        "vocab": [
            ("flight", "uçuş"),
            ("dusk", "alacakaranlık"),
            ("ocean", "okyanus"),
            ("fatigue", "yorgunluk, bitkinlik"),
            ("plummet", "dimdik düşmek"),
            ("twinkle", "göz kırpmak, parıldamak"),
            ("lagoon", "lagün"),
            ("target", "hedef")
        ],
        "sentences": [
            ("They flew for days and nights, forgetting whether it was yesterday or tomorrow.", "Dün mü yoksa yarın mı olduğunu unutup günlerce ve gecelerce uçtular.", "Duration phrase 'for days and nights'; indirect question 'whether it was'."),
            ("Sometimes they were hungry, and Peter snatched food from birds' beaks.", "Bazen acıkıyorlardı ve Peter kuşların gagalarından yiyecek kapıyordu.", "Past verb 'snatched'; possessive 'birds' beaks'."),
            ("Sometimes they fell asleep while flying, plummeting like stones toward the sea.", "Bazen uçarken uyuyakalıyor, denize doğru taş gibi dimdik düşüyorlardı.", "Simile 'like stones'; temporal participle clause 'while flying'."),
            ("Peter would dart down with incredible speed and catch them just above the waves.", "Peter inanılmaz bir hızla aşağı dalar ve onları tam dalgaların üzerindeyken yakalardı.", "Modal 'would dart' indicating habitual past; adverbial 'just above'."),
            ("Michael was so tiny that Peter carried him by one leg for miles.", "Michael o kadar minikti ki, Peter onu millerce tek bir bacağından tutarak taşıdı.", "Result clause 'so tiny that'; measurement phrase 'for miles'."),
            ("Gradually, the cold gray clouds broke, revealing a brilliant azure sea below.", "Yavaş yavaş soğuk gri bulutlar dağıldı ve aşağıdaki pırıl pırıl masmavi denizi açığa çıkardı.", "Participle clause 'revealing azure sea'; adverb 'gradually'."),
            ("The air grew suddenly warm, fragrant with scents of wild blossoms and pine.", "Hava aniden ısındı, yabani çiçeklerin ve çamın kokularıyla mis gibi koktu.", "Copular verb 'grew warm'; adjective phrase 'fragrant with'."),
            ("'Look!' shouted Peter pointing his sword toward the distant sparkling horizon.", "'Bakın!' diye haykırdı Peter, kılıcını uzaktaki parıldayan ufka doğru uzatarak.", "Participle clause 'pointing his sword'; imperative 'look'."),
            ("There lay the Neverland, basking like a sleeping green dragon in the water.", "İşte orada Varolmayan Ülke, suyun içinde uyuyan yeşil bir ejderha gibi güneşleniyordu.", "Simile 'like a sleeping dragon'; participle 'basking'."),
            ("The children could see the winding river, dark forests, and coral reefs clearly.", "Çocuklar kıvrımlı nehri, karanlık ormanları ve mercan resiflerini açıkça görebiliyorlardı.", "Modal 'could see'; list of geographical features."),
            ("Smoke curled lazily from the pirate campfire on the sandy beach.", "Kumsaldaki korsan kamp ateşinden tembelce dumanlar yükseliyordu.", "Adverb 'lazily'; prepositional phrase 'on the sandy beach'."),
            ("They saw the Jolly Roger, the dark pirate ship anchored in the bay.", "Koyda demirlemiş karanlık korsan gemisi Jolly Roger'ı gördüler.", "Appositive clause; past participle 'anchored in the bay'."),
            ("Peter told them about Captain Jas Hook, the most cruel pirate on the seven seas.", "Peter onlara yedi denizin en zalim korsanı olan Kaptan Jas Hook'tan bahsetti.", "Superlative 'most cruel pirate'; prepositional phrase 'on the seven seas'."),
            ("'He has an iron hook instead of a right hand, and he hates me,' said Peter.", "'Sağ elinin yerinde demir bir kanca var ve benden nefret ediyor,' dedi Peter.", "Prepositional phrase 'instead of a hand'; present tense facts."),
            ("Suddenly, a puff of white smoke erupted from the pirate ship's cannon.", "Birdenbire, korsan gemisinin topundan beyaz bir duman bulutu fışkırdı.", "Past verb 'erupted'; possessive noun phrase."),
            ("A heavy iron cannonball whistled through the air, scattering the little fliers.", "Ağır bir demir gülle havada ıslık çalarak minik uçucuları darmadağın etti.", "Participial clause 'scattering fliers'; past verb 'whistled'."),
            ("The blast separated Wendy and Tinker Bell from Peter and the boys.", "Patlama Wendy ile Tinker Bell'i Peter ve diğer oğlanlardan ayırdı.", "Transitive past 'separated'; compound objects."),
            ("Tinker Bell darted ahead, her bell-like voice tinkling with malicious jealousy.", "Tinker Bell önden hızla uçtu, çan gibi sesi hain bir kıskançlıkla şıngırdadı.", "Absolute construction 'her voice tinkling'; preposition 'with'."),
            ("She hated Wendy and decided to use this dark moment to destroy her.", "Wendy'den nefret ediyordu ve onu yok etmek için bu karanlık andan faydalanmaya karar verdi.", "Infinitive of purpose 'to destroy her'; past verbs 'hated and decided'."),
            ("Wendy flew blindly on, tired, frightened, and guided only by the treacherous fairy.", "Wendy yorgun, korkmuş ve yalnızca o hain perinin rehberliğinde körlemesine uçmaya devam etti.", "Participial adjectives; adverb 'blindly'.")
        ]
    },
    # Page 5: The Island Come to Life
    {
        "page_number": 5,
        "title": "The Island Come to Life",
        "vocab": [
            ("savage", "vahşi"),
            ("crocodile", "timsah"),
            ("tick", "tıkırtı yapmak"),
            ("clock", "saat"),
            ("hook", "kanca"),
            ("dread", "korku, dehşet"),
            ("swallow", "yutmak"),
            ("stalk", "sinsice takip etmek")
        ],
        "sentences": [
            ("The Neverland always woke up into motion whenever Peter Pan returned.", "Peter Pan ne zaman geri dönse, Varolmayan Ülke daima harekete geçerek uyanırdı.", "Time clause with 'whenever'; idiom 'woke into motion'."),
            ("In the middle of the island, the Lost Boys were looking for Peter.", "Adanın tam ortasında Kayıp Çocuklar Peter'ı arıyorlardı.", "Past continuous 'were looking for'; prepositional phrase 'in the middle'."),
            ("Behind the Lost Boys came the bloodthirsty pirates, armed with cutlasses and muskets.", "Kayıp Çocukların ardından palalar ve tüfeklerle kuşanmış kana susamış korsanlar geliyordu.", "Inverted sentence; passive participle modifier 'armed with'."),
            ("Behind the pirates crept the redskin warriors, moving as silently as smoke.", "Korsanların ardından duman kadar sessizce hareket eden kızılderili savaşçılar süzülüyordu.", "Simile 'as silently as smoke'; past verb 'crept'."),
            ("And behind the redskins glided the enormous, hungry crocodile with jaws open.", "Ve kızılderililerin ardından çeneleri açık halde devasa, aç timsah süzülüyordu.", "Inverted sentence; absolute phrase 'with jaws open'."),
            ("They were all walking in a giant circle around the enchanted forest.", "Hepsi büyülü ormanın etrafında dev bir çember halinde yürüyorlardı.", "Past continuous 'were walking'; prepositional phrase 'in a circle'."),
            ("Captain Hook led the pirates, his dark curls falling over his pale face.", "Kaptan Hook korsanlara liderlik ediyor, siyah bukleleri solgun yüzünün üzerine dökülüyordu.", "Absolute construction 'his curls falling'; adjective 'pale'."),
            ("His right hand was gone, replaced by a gleaming, curved iron hook.", "Sağ eli yoktu; yerini parıldayan, kıvrık bir demir kanca almıştı.", "Passive participle 'replaced by'; coordinate adjectives 'gleaming, curved'."),
            ("Peter Pan had cut off Hook's hand in a fierce duel long ago.", "Peter Pan uzun zaman önce çetin bir düelloda Hook'un elini kesmişti.", "Past perfect 'had cut off'; time phrase 'long ago'."),
            ("He had flung the hand to the passing crocodile, who loved the taste.", "Eli oradan geçen ve bu tadı çok seven timsaha fırlatmıştı.", "Relative clause 'who loved the taste'; past perfect 'had flung'."),
            ("Since then, the beast had followed Hook relentlessly across every sea.", "O zamandan beri canavar, her deniz boyunca Hook'u amansızca takip etmişti.", "Present/past perfect with 'since then'; adverb 'relentlessly'."),
            ("Fortunately for Hook, the crocodile had also swallowed a ticking clock.", "Neyse ki Hook için timsah aynı zamanda tıkırdayan bir saat de yutmuştu.", "Adverb 'fortunately'; past perfect 'had swallowed'."),
            ("'Tick, tick, tick!' warned the clock from inside the monster's belly.", "'Tık, tık, tık!' diye canavarın karnının içinden saat uyarı veriyordu.", "Onomatopoeia; prepositional phrase 'from inside belly'."),
            ("Whenever Hook heard that rhythmic ticking, he shuddered in dreadful terror.", "Hook o ritmik tıkırtıyı her duyduğunda, korkunç bir dehşetle ürperirdi.", "Time clause with 'whenever'; past verb 'shuddered'."),
            ("'It will tick until the winding runs down,' muttered Hook with trembling lips.", "'Kurulu zembereği bitene kadar tıkırdayacak,' diye mırıldandı Hook titreyen dudaklarla.", "Time clause 'until runs down'; participial adjective 'trembling'."),
            ("'And when it stops, the beast will catch me unawares and devour me!'", "'Ve durduğunda canavar beni gafil avlayıp yutuverecek!'", "Coordinated future modal clauses; idiom 'catch unawares'."),
            ("The Lost Boys disappeared into their secret underground home under hollow trees.", "Kayıp Çocuklar oyuk ağaçların altındaki gizli yeraltı evlerinde gözden kayboldular.", "Prepositional phrase 'under hollow trees'; past verb 'disappeared'."),
            ("Each boy had his own tree trunk fitted precisely to the size of his body.", "Her oğlanın kendi bedeninin ölçüsüne tam oturan kendi ağaç gövdesi vardı.", "Past participle modifier 'fitted precisely'; possessive 'his own'."),
            ("Above in the clouds, Wendy flew closer and closer to the island floor.", "Yukarıda bulutların arasında Wendy ada zeminine gittikçe daha da yaklaştı.", "Comparative repetition 'closer and closer'; past verb 'flew'."),
            ("Tinker Bell was preparing her wicked ambush from the highest branch.", "Tinker Bell en yüksek daldan hain pususunu hazırlıyordu.", "Past continuous 'was preparing'; superlative 'highest branch'.")
        ]
    },
    # Page 6: The Wendy Bird
    {
        "page_number": 6,
        "title": "The Wendy Bird",
        "vocab": [
            ("arrow", "ok"),
            ("bow", "yay"),
            ("shoot", "vurmak, ateş etmek"),
            ("acorn", "meşe palamudu"),
            ("button", "düğme"),
            ("grief", "keder, elem"),
            ("protect", "korumak"),
            ("weep", "gözyaşı dökmek")
        ],
        "sentences": [
            ("Tinker Bell flew down to the Lost Boys, buzzing like an angry hornet.", "Tinker Bell öfkeli bir eşek arısı gibi vızıldayarak Kayıp Çocukların yanına indi.", "Simile 'like an angry hornet'; past verb 'flew down'."),
            ("She shouted that Peter wanted them to shoot a dangerous creature immediately.", "Peter'ın derhal tehlikeli bir yaratığı vurmalarını istediğini haykırdı.", "Indirect command; adverb 'immediately'."),
            ("'Peter wants you to shoot the Wendy bird!' cried the deceitful fairy.", "'Peter Wendy kuşunu vurmanızı istiyor!' diye haykırdı hilekar peri.", "Direct speech; adjective 'deceitful'."),
            ("The foolish boys looked up and saw a white figure flying in the sky.", "Aptal oğlanlar yukarı baktılar ve gökyüzünde uçan beyaz bir karaltı gördüler.", "Coordinate past verbs 'looked up and saw'; participle 'flying'."),
            ("Tootles, the gentlest boy, fitted an arrow to his bow in eager obedience.", "En nazik oğlan olan Tootles, hevesli bir itaatle yayına bir ok yerleştirdi.", "Superlative appositive 'gentlest boy'; noun phrase 'eager obedience'."),
            ("'Out of the way, Tink!' cried Tootles, drawing the bowstring to his ear.", "'Yoldan çekil Tink!' diye haykırdı Tootles, kirişi kulağına kadar çekerek.", "Imperative phrase; participle clause 'drawing bowstring'."),
            ("He loosed the arrow, and it sped straight into the white breast.", "Oku fırlattı ve ok dosdoğru beyaz göğsün içine saplandı.", "Coordinate past clauses; directional adverb 'straight into'."),
            ("Wendy uttered a faint cry and fluttered helplessly down to the earth.", "Wendy hafif bir çığlık attı ve çaresizce yere doğru çırpınarak düştü.", "Coordinate past actions 'uttered and fluttered'; adverb 'helplessly'."),
            ("She lay motionless upon the green moss with the black arrow in her chest.", "Göğsündeki siyah okla, yeşil yosunların üzerinde hareketsizce yatıyordu.", "Adjective 'motionless'; prepositional phrase 'with arrow in chest'."),
            ("The boys gathered round proudly, believing they had performed a noble deed.", "Soylu bir eylem gerçekleştirdiklerine inanarak oğlanlar gururla etrafında toplandılar.", "Participle clause 'believing they had performed'; adverb 'proudly'."),
            ("Just then, a crow sounded from the sky: Peter Pan had arrived.", "Tam o sırada gökyüzünden bir horoz sesi duyuldu: Peter Pan gelmişti.", "Time phrase 'just then'; past perfect 'had arrived'."),
            ("Peter landed among them with gleaming eyes and asked for their mother.", "Peter parıldayan gözlerle aralarına indi ve annelerinin nerede olduğunu sordu.", "Coordinate past verbs 'landed and asked'; preposition 'among them'."),
            ("'I have brought you a mother to tell stories and care for you,' said Peter.", "'Size hikayeler anlatacak ve size bakacak bir anne getirdim,' dedi Peter.", "Present perfect 'have brought'; coordinate infinitives."),
            ("The boys froze in sheer horror as they realized what they had done.", "Ne yaptıklarını anladıklarında oğlanlar katıksız bir dehşetle donakaldılar.", "Time clause 'as they realized'; noun clause 'what they had done'."),
            ("Tootles dropped his bow, weeping bitterly: 'I have killed our mother!'", "Tootles yayını düşürdü, acı acı ağlayarak: 'Annemizi öldürdüm!' dedi.", "Participle 'weeping bitterly'; present perfect 'have killed'."),
            ("Peter knelt beside Wendy and gently touched the head of the arrow.", "Peter Wendy'nin yanına diz çöktü ve okun ucuna usulca dokundu.", "Coordinate past verbs 'knelt and touched'; adverb 'gently'."),
            ("To his amazement, the sharp arrowhead had not pierced her tender flesh.", "Hayretler içinde gördü ki, keskin ok ucu kızın narin tenini delip geçmemişti.", "Past perfect negative 'had not pierced'; noun phrase 'To his amazement'."),
            ("It had struck the acorn button that Peter had given her in London.", "Ok, Peter'ın Londra'da ona verdiği meşe palamudu düğmesine çarpmıştı.", "Past perfect 'had struck'; relative clause 'that Peter had given'."),
            ("'The kiss saved her life!' cried Peter, his face radiant with joy.", "'Öpücük onun hayatını kurtardı!' diye haykırdı Peter, yüzü sevinçten parıldayarak.", "Absolute construction 'his face radiant with joy'; past verb 'saved'."),
            ("They built a tiny little house around Wendy where she could safely recover.", "Wendy'nin güvenle iyileşebilmesi için etrafına küçücük bir ev inşa ettiler.", "Relative clause of place 'where she could recover'; modal 'could'.")
        ]
    },
    # Page 7: The Home Under the Ground
    {
        "page_number": 7,
        "title": "The Home Under the Ground",
        "vocab": [
            ("hearth", "ocak, şömine"),
            ("subterranean", "yer altı"),
            ("patch", "yama yapmak"),
            ("darning", "çorap örme/yamama"),
            ("cosy", "sıcacık, samimi"),
            ("bedtime", "uyku vakti"),
            ("pretend", "rol yapmak, farz etmek"),
            ("quarrel", "tartışmak, kavga etmek")
        ],
        "sentences": [
            ("Wendy soon recovered completely and was delighted with her new family.", "Wendy çok geçmeden tamamen iyileşti ve yeni ailesinden çok memnun kaldı.", "Adverb 'completely'; passive idiom 'was delighted with'."),
            ("The home under the ground consisted of one huge, warm earthen room.", "Yer altındaki ev, devasa ve sıcak tek bir toprak odadan oluşuyordu.", "Phrasal verb 'consisted of'; compound adjective 'earthen room'."),
            ("A great fireplace was dug into the earth, where a crackling fire burned.", "Toprağın içine, çatırdayan bir ateşin yandığı büyük bir şömine kazılmıştı.", "Passive voice 'was dug'; relative clause 'where a fire burned'."),
            ("There was a large bed on which all the boys slept packed together like sardines.", "Bütün oğlanların konserve balık gibi yan yana sıkışıp uyuduğu büyük bir yatak vardı.", "Relative clause 'on which all slept'; simile 'like sardines'."),
            ("Tinker Bell had her own tiny chamber recessed into the wall with curtains.", "Tinker Bell'in duvara oyulmuş, perdeli minicik kendine ait bir odası vardı.", "Past participle modifier 'recessed into the wall'; possessive 'her own'."),
            ("Wendy became the mother of the household, cooking, sewing, and darning socks.", "Wendy evin annesi oldu; yemek pişirdi, dikiş dikti ve çorapları yamadı.", "Coordinate gerunds describing maternal duties; noun 'household'."),
            ("Peter was the father, who went out on adventures and brought home news.", "Peter ise maceralara çıkan ve eve haberler getiren babaydı.", "Relative clause 'who went out and brought'; coordinate predicates."),
            ("Every evening they sat around the blazing hearth eating pretend meals.", "Her akşam yanan ocağın etrafında oturup mış gibi yapılan yemekleri yerlerdi.", "Participle phrase 'eating pretend meals'; frequency phrase 'every evening'."),
            ("With Peter, make-believe was so real that you could actually choke on pretend food.", "Peter'la rol yapmak öyle gerçekti ki, hayali bir yemek yerken gerçekten boğulabilirdiniz.", "Result clause 'so real that'; modal 'could choke'."),
            ("After supper, Wendy tucked all the boys into the big bed warmly.", "Akşam yemeğinden sonra Wendy bütün çocukları büyük yatağa sıcacık örttü.", "Phrasal verb 'tucked into'; adverb 'warmly'."),
            ("She told them endless enchanting stories about London and their real parents.", "Onlara Londra ve gerçek anne babaları hakkında sonu gelmez büyüleyici hikayeler anlattı.", "Double object verb 'told them stories'; adjective 'enchanting'."),
            ("John and Michael began to forget their mother's face as the weeks drifted by.", "Haftalar akıp geçtikçe John ve Michael annelerinin yüzünü unutmaya başladılar.", "Verb followed by infinitive 'began to forget'; time clause with 'as'."),
            ("Wendy instituted regular school lessons to keep their memories sharp and bright.", "Wendy hafızalarını keskin ve parlak tutmak için düzenli okul dersleri koydu.", "Infinitive of purpose 'to keep memories sharp'; adjective pair 'sharp and bright'."),
            ("Peter refused to study, declaring that school was for children who grow up.", "Peter okula gitmenin büyüyen çocuklara göre olduğunu söyleyerek ders çalışmayı reddetti.", "Verb + infinitive 'refused to study'; participle 'declaring that'."),
            ("He spent his days roaming the lagoons and mocking the proud wild beasts.", "Günlerini lagünlerde dolaşarak ve mağrur vahşi hayvanlarla alay ederek geçirdi.", "Expression 'spent days doing'; coordinate participles."),
            ("The Lost Boys adored Wendy and competed eagerly for her maternal smiles.", "Kayıp Çocuklar Wendy'ye hayran kaldılar ve onun anne şefkati dolu tebessümleri için hevesle yarıştılar.", "Coordinate actions 'adored and competed'; adjective 'maternal'."),
            ("Even Tinker Bell had to admit that the underground home was peaceful.", "Tinker Bell bile yer altındaki bu evin huzurlu olduğunu kabul etmek zorunda kaldı.", "Modal obligation 'had to admit'; noun clause 'that the home was peaceful'."),
            ("Yet outside in the bright sunlight, dangers were gathering across the island.", "Yine de dışarıda, parlak güneş ışığı altında tehlikeler adanın her yanında toplanıyordu.", "Adverb 'yet'; past continuous 'were gathering'."),
            ("Hook was formulating a terrible plan to exterminate Peter and his crew.", "Hook, Peter'ı ve tayfasını yok etmek için korkunç bir plan tasarlıyordu.", "Past continuous 'was formulating'; infinitive of purpose 'to exterminate'."),
            ("The sunny waters of the Mermaids' Lagoon would be their next battleground.", "Denizkızları Lagünü'nün güneşli suları onların bir sonraki savaş alanı olacaktı.", "Modal 'would be'; proper noun 'Mermaids' Lagoon'.")
        ]
    },
    # Page 8: The Mermaids' Lagoon
    {
        "page_number": 8,
        "title": "The Mermaids' Lagoon",
        "vocab": [
            ("lagoon", "lagün"),
            ("mermaid", "denizkızı"),
            ("comb", "taramak / tarak"),
            ("dinghy", "küçük sandal, filika"),
            ("rock", "kaya"),
            ("bask", "güneşlenmek"),
            ("splash", "su sıçratmak"),
            ("treacherous", "hain, tehlikeli")
        ],
        "sentences": [
            ("The Mermaids' Lagoon was the most magical and dangerous spot in Neverland.", "Denizkızları Lagünü, Varolmayan Ülke'deki en büyülü ve en tehlikeli yerdi.", "Superlative phrase 'most magical and dangerous'; proper name."),
            ("The water was coral-pink and azure blue, crystal clear over white sands.", "Su, beyaz kumların üzerinde billur gibi berrak, mercan pembesi ve gök mavisiydi.", "Compound color adjectives; phrase 'crystal clear'."),
            ("Mermaids basked upon Marooners' Rock, combing their long golden hair in the sun.", "Denizkızları güneşte uzun sarı saçlarını tarayarak Terk Edilmişler Kayası'nda güneşlenirlerdi.", "Participle clause 'combing their hair'; proper noun 'Marooners' Rock'."),
            ("They were unfriendly creatures who splashed water at human children disdainfully.", "İnsan çocuklarına küçümseyerek su sıçratan, pek de dost canlısı olmayan yaratıklardı.", "Relative clause 'who splashed water'; adverb 'disdainfully'."),
            ("One sunny afternoon, Wendy and the boys were resting on Marooners' Rock.", "Güneşli bir öğleden sonra Wendy ve oğlanlar Terk Edilmişler Kayası'nda dinleniyorlardı.", "Past continuous 'were resting'; time phrase 'one sunny afternoon'."),
            ("The tide was beginning to rise, licking the edges of the smooth stone.", "Gelgit yükselmeye başlıyor, pürüzsüz taşın kenarlarını yalıyordu.", "Verb + infinitive 'was beginning to rise'; participle 'licking edges'."),
            ("Suddenly, Peter sniffed the air and cried, 'Pirates! Dive into the water!'", "Birdenbire Peter havayı kokladı ve 'Korsanlar! Suya dalın!' diye haykırdı.", "Coordinate past verbs; imperative direct command."),
            ("The boys slipped silently beneath the surface like little brown seals.", "Oğlanlar minik kahverengi foklar gibi sessizce suyun yüzeyinin altına süzüldüler.", "Simile 'like little brown seals'; adverb 'silently'."),
            ("A pirate dinghy approached, rowed by the brutal Smee and the fierce Starkey.", "Gaddar Smee ve yırtıcı Starkey'nin kürek çektiği bir korsan sandalı yaklaştı.", "Passive participle modifier 'rowed by'; descriptive adjectives."),
            ("Tied up in the bottom of the boat was Tiger Lily, the Indian princess.", "Sandalın dibinde eli ayağı bağlanmış halde Kızılderili prensesi Kaplan Zambağı yatıyordu.", "Inverted passive sentence 'Tied up was Tiger Lily'; apposition."),
            ("The pirates intended to leave her on the rock to drown in the rising tide.", "Korsanlar onu yükselen gelgitte boğulması için kayanın üzerinde bırakmaya niyetliydiler.", "Verb + infinitive 'intended to leave'; infinitive of purpose 'to drown'."),
            ("Tiger Lily sat proudly, too brave to beg her captors for mercy.", "Kaplan Zambağı, esir alanlardan merhamet dilenmeyecek kadar cesur, başı dik oturuyordu.", "Structure 'too + adjective + infinitive'; adverb 'proudly'."),
            ("Peter was furious at this cruel and unfair act of pirate cowardice.", "Peter bu zalimce ve haksız korsan korkaklığı karşısında öfkeden küplere bindi.", "Adjective phrase 'furious at'; compound noun 'pirate cowardice'."),
            ("He swam near the boat and imitated Captain Hook's voice with eerie perfection.", "Sandalın yanına yüzdü ve tekinsiz bir kusursuzlukla Kaptan Hook'un sesini taklit etti.", "Coordinate past verbs 'swam and imitated'; prepositional phrase 'with perfection'."),
            ("'Ahoy there, Smee!' called Peter in Hook's exact aristocratic drawl.", "'Hey oradaki, Smee!' diye seslendi Peter, Hook'un tam aristokratik aksanıyla.", "Possessive phrase 'Hook's exact drawl'; direct quotation."),
            ("The two pirates dropped their oars in terrified, unquestioning obedience.", "İki korsan dehşet dolu, sorgusuz sualsiz bir itaatle küreklerini bıraktılar.", "Prepositional phrase 'in obedience'; coordinate adjectives."),
            ("'Cut the redskin's bonds and let her go at once!' ordered the false voice.", "'Kızılderilinin bağlarını çözün ve derhal gitmesine izin verin!' diye emretti sahte ses.", "Imperative coordinate commands; adjective 'false'."),
            ("Smee obediently sliced Tiger Lily's ropes with his knife.", "Smee itaatkar bir tavırla bıçağıyla Kaplan Zambağı'nın iplerini kesti.", "Adverb 'obediently'; possessive noun phrase."),
            ("The princess slipped into the water and swam away toward safety.", "Prenses suya süzüldü ve güvenliğe doğru hızla yüzüp uzaklaştı.", "Coordinate past verbs 'slipped and swam away'; directional preposition 'toward'."),
            ("The real Captain Hook was swimming toward the rock at that very second.", "Gerçek Kaptan Hook ise tam o saniyede kayaya doğru yüzüyordu.", "Past continuous 'was swimming'; emphatic phrase 'at that very second'.")
        ]
    },
    # Page 9: Rescue of Tiger Lily
    {
        "page_number": 9,
        "title": "Duel on Marooners' Rock",
        "vocab": [
            ("duel", "düello"),
            ("imitate", "taklit etmek"),
            ("kite", "uçurtma"),
            ("tide", "gelgit"),
            ("claw", "pençe, tırmalamak"),
            ("perish", "yok olmak, ölmek"),
            ("courage", "cesaret"),
            ("submerge", "suya batmak, sular altında kalmak")
        ],
        "sentences": [
            ("Hook climbed onto Marooners' Rock, gasping for breath and dark with fury.", "Hook, nefes nefese kalmış ve öfkeden kararmış halde Terk Edilmişler Kayası'na tırmandı.", "Participial phrases 'gasping for breath' and 'dark with fury'."),
            ("When Smee reported that he had released the prisoner by Hook's own order, Hook roared.", "Smee mahkumu Hook'un kendi emriyle serbest bıraktığını söyleyince, Hook kükredi.", "Time clause with 'when'; past perfect 'had released'."),
            ("'I gave no such order!' screamed the enraged pirate captain.", "'Ben öyle bir emir vermedim!' diye çığlık attı öfkeden deliye dönen korsan kaptan.", "Past tense negative 'gave no such order'; participial adjective 'enraged'."),
            ("Peter laughed aloud from the water, unable to contain his merry mockery.", "Peter neşeli alayını tutamayarak suyun içinden kahkahayı bastı.", "Adverb 'aloud'; participial clause of result 'unable to contain'."),
            ("Hook drew his cutlass and slashed violently toward the mocking sound.", "Hook palasını çekti ve alaycı sese doğru şiddetle savurdu.", "Coordinate past verbs 'drew and slashed'; participial adjective 'mocking'."),
            ("Peter sprang onto the slippery rock, dagger in hand, ready for combat.", "Peter elinde hançeriyle, savaşa hazır halde kaygan kayanın üzerine fırladı.", "Absolute phrase 'dagger in hand'; adjective 'slippery'."),
            ("They fought fiercely like two wildcats on the tiny narrow ledge.", "Küçücük dar sette iki yaban kedisi gibi kıyasıya savaştılar.", "Simile 'like two wildcats'; adverb 'fiercely'."),
            ("Peter was quick and agile, dodging every deadly thrust of the iron hook.", "Peter çevik ve kıvraktı, demir kancanın her ölümcül hamlesini savuşturuyordu.", "Coordinate predicate adjectives; participle phrase 'dodging thrust'."),
            ("Then Peter bit Hook's hand, and Hook clawed Peter with his curved iron.", "Sonra Peter Hook'un elini ısırdı, Hook da kıvrık demiriyle Peter'ı tırmaladı.", "Coordinate clauses; compound noun 'curved iron'."),
            ("Seeing Peter's blood, the ticking crocodile suddenly surged up from the deep.", "Peter'ın kanını gören tıkırdayan timsah aniden derinliklerden yukarı fırladı.", "Participial clause 'seeing blood'; phrasal verb 'surged up'."),
            ("Hook screamed in panic and leaped into the water, swimming frantically for his ship.", "Hook panik içinde çığlık attı ve suya atlayıp çılgınca gemisine doğru yüzdü.", "Coordinate past verbs 'screamed and leaped'; participle phrase 'swimming frantically'."),
            ("The crocodile pursued him with snapping jaws and relentless rhythm.", "Timsah şakırdayan çeneleri ve amansız ritmiyle onun peşine düştü.", "Prepositional phrase 'with snapping jaws'; participial adjective 'snapping'."),
            ("Meanwhile, the rising tide had nearly submerged Marooners' Rock completely.", "Bu arada yükselen gelgit, Terk Edilmişler Kayası'nı neredeyse tamamen sular altında bırakmıştı.", "Adverb 'meanwhile'; past perfect 'had submerged'."),
            ("Only Wendy and Peter remained on the tiny stone, shivering in the cold spray.", "Küçücük taşın üzerinde sadece Wendy ve Peter kalmıştı, soğuk serpintide titriyorlardı.", "Adverb 'only'; participle clause 'shivering in cold spray'."),
            ("Wendy was too exhausted from the struggle to swim all the way to shore.", "Wendy boğuşmaktan o kadar bitkindi ki kıyıya kadar yüzmesi imkansızdı.", "Structure 'too exhausted... to swim'; prepositional phrase 'to shore'."),
            ("'We are going to drown, Peter,' whispered Wendy holding his hand tight.", "'Boğulacağız Peter,' diye fısıldadı Wendy onun elini sımsıkı tutarak.", "Immediate future 'are going to drown'; participle clause 'holding hand'."),
            ("Peter stood tall, smiled bravely, and looked out into the gathering twilight.", "Peter dimdik durdu, cesurca gülümsedi ve yaklaşan alacakaranlığa doğru baktı.", "Series of coordinated past actions; participial adjective 'gathering'."),
            ("'To die will be an awfully big adventure,' said Peter with shining eyes.", "'Ölmek fevkalade büyük bir macera olacak,' dedi Peter parıldayan gözlerle.", "Famous quotation; infinitive subject 'To die'; adverb 'awfully'."),
            ("Just then, Michael's lost kite drifted low across the darkening lagoon.", "Tam o sırada Michael'ın kayıp uçurtması kararan lagün boyunca alçaktan süzüldü.", "Time phrase 'just then'; participial adjective 'darkening lagoon'."),
            ("Peter grabbed the string and tied it to Wendy, letting the wind carry her home.", "Peter ipi yakaladı ve Wendy'ye bağlayarak rüzgarın onu eve taşımasını sağladı.", "Coordinate past verbs; participle phrase 'letting the wind carry'.")
        ]
    },
    # Page 10: The Never Bird's Nest
    {
        "page_number": 10,
        "title": "The Never Bird's Nest",
        "vocab": [
            ("nest", "yuva"),
            ("egg", "yumurta"),
            ("sail", "yelken açmak / yelken"),
            ("submerge", "su altında kalmak"),
            ("drift", "akıntıyla sürüklenmek"),
            ("gratitude", "şükran, minnettarlık"),
            ("shore", "kıyı, sahil"),
            ("peril", "büyük tehlike")
        ],
        "sentences": [
            ("Wendy was lifted gently into the air by the kite and carried toward the shore.", "Wendy uçurtma sayesinde havaya usulca kalktı ve kıyıya doğru taşındı.", "Passive voice 'was lifted and carried'; instrument phrase 'by the kite'."),
            ("Peter was left entirely alone upon the tiny vanishing rock in the rising tide.", "Yükselen gelgitte yok olmakta olan küçücük kayanın üzerinde Peter yapayalnız kaldı.", "Passive voice 'was left alone'; participial adjective 'vanishing rock'."),
            ("The black waters lapped higher and higher around his bare ankles.", "Kara sular çıplak ayak bileklerinin etrafında gittikçe daha da yükseğe çırpındı.", "Comparative repetition 'higher and higher'; past verb 'lapped'."),
            ("He could not fly because his shoulder was bruised from Hook's savage blow.", "Uçamıyordu çünkü omuzu Hook'un vahşi darbesi yüzünden berelenmişti.", "Causal clause 'because shoulder was bruised'; passive voice."),
            ("Presently, he saw a strange object floating toward him upon the waves.", "Çok geçmeden dalgaların üzerinde kendisine doğru yüzen tuhaf bir nesne gördü.", "Adverb 'presently'; perception verb 'saw' + participle 'floating'."),
            ("It was the Never Bird, sitting stubbornly upon her large floating nest.", "Bu, yüzen büyük yuvasının üzerinde inatla oturan Asla Kuşu idi.", "Participle phrase 'sitting stubbornly'; proper noun 'Never Bird'."),
            ("She was trying desperately to keep her eggs warm despite the churning sea.", "Köpüren denize rağmen yumurtalarını sıcak tutmak için çaresizce çabalıyordu.", "Past continuous 'was trying'; preposition 'despite'."),
            ("Seeing Peter's desperate plight, the brave bird made a noble maternal sacrifice.", "Peter'ın çaresiz durumunu gören cesur kuş, soylu bir annelik fedakarlığı yaptı.", "Participial clause of perception; noun phrase 'maternal sacrifice'."),
            ("She fluttered off the nest, calling to Peter with harsh, urgent cries.", "Sert ve acil haykırışlarla Peter'a seslenerek yuvanın üzerinden havalandı.", "Coordinate participles 'fluttered off and calling'; adjective pair 'harsh, urgent'."),
            ("Peter understood her generous gift and scrambled into the buoyant wicker nest.", "Peter kuşun bu cömert hediyesini anladı ve batmayan hasır yuvanın içine tırmandı.", "Coordinate past verbs; adjective 'buoyant wicker'."),
            ("He placed the delicate white eggs safely inside his hat upon the rock.", "Narin beyaz yumurtaları kayanın üzerine koyduğu şapkasının içine güvenle yerleştirdi.", "Prepositional phrases indicating location; adverb 'safely'."),
            ("He raised his little shirt upon a twig to serve as an improvised sail.", "Derme çatma bir yelken görevi görmesi için minik gömleğini bir dalın üzerine kaldırdı.", "Infinitive of purpose 'to serve as'; compound noun 'improvised sail'."),
            ("The pleasant sea breeze caught the cloth and pushed the nest across the lagoon.", "Tatlı deniz esintisi kumaşı yakaladı ve yuvayı lagün boyunca ileri itti.", "Coordinate past verbs 'caught and pushed'; adjective 'pleasant'."),
            ("Peter sailed proudly through the darkening waters, crowing like a little cockerel.", "Peter minik bir horoz gibi ötüp durarak kararan sularda gururla yelken açtı.", "Simile 'like a cockerel'; participle 'crowing'."),
            ("The Never Bird flew overhead, watching her eggs safely nested inside his cap.", "Asla Kuşu tepeden uçtu, yumurtalarının onun kasketi içine güvenle yerleştiğini izledi.", "Participle clause 'watching her eggs safely nested'."),
            ("Peter reached the sandy shore just as the night fell completely black.", "Gece zifiri karanlığa bürünürken Peter tam vaktinde kumsala ulaştı.", "Time clause 'just as night fell'; compound noun 'sandy shore'."),
            ("The Lost Boys and Wendy rushed down to embrace him with cries of joy.", "Kayıp Çocuklar ve Wendy sevinç çığlıklarıyla ona sarılmak için aşağı koştular.", "Infinitive of purpose 'to embrace'; noun phrase 'cries of joy'."),
            ("Tiger Lily and her proud warriors surrounded their home to stand guard.", "Kaplan Zambağı ve onun gururlu savaşçıları nöbet tutmak için evlerini çembere aldılar.", "Infinitive of purpose 'to stand guard'; past verb 'surrounded'."),
            ("Out of gratitude for her rescue, the braves promised to protect Peter forever.", "Kurtarılmasına duydukları minnetten ötürü savaşçılar Peter'ı sonsuza dek korumaya söz verdiler.", "Prepositional phrase 'out of gratitude'; infinitive 'to protect'."),
            ("Peace reigned over the island, but the black shadow of the pirates drew near.", "Adaya barış hakim oldu fakat korsanların karanlık gölgesi sinsice yaklaşıyordu.", "Coordinate clauses with 'but'; phrasal verb 'drew near'.")
        ]
    },
    # Page 11: The Happy Home and Wendy's Story
    {
        "page_number": 11,
        "title": "Wendy's Story and Homesickness",
        "vocab": [
            ("hearth", "ocak başı"),
            ("story", "hikaye"),
            ("homesick", "ev hasreti çeken"),
            ("window", "pencere"),
            ("parent", "ebeveyn"),
            ("yearn", "hasret çekmek, arzulamak"),
            ("farewell", "veda"),
            ("departure", "ayrılış, yola çıkış")
        ],
        "sentences": [
            ("That evening, the subterranean home was warm, merry, and filled with laughter.", "O akşam, yer altındaki ev sıcacık, neşeli ve kahkahalarla doluydu.", "Coordinate adjectives 'warm, merry'; passive participle 'filled with'."),
            ("Outside in the chill night, Tiger Lily's braves sat silently smoking their pipes.", "Dışarıdaki ayaz gecede Kaplan Zambağı'nın savaşçıları sessizce oturup pipolarını tüttürüyordu.", "Participle phrase 'smoking pipes'; adverb 'silently'."),
            ("Wendy sat in her wicker rocking chair with all the boys huddled around her.", "Wendy bütün oğlanlar etrafına toplanmış halde hasır sallanan sandalyesinde oturuyordu.", "Absolute construction 'boys huddled around'; compound noun 'rocking chair'."),
            ("'Tell us our favorite story, Wendy!' pleaded Michael, resting his head on her lap.", "'Bize en sevdiğimiz hikayeyi anlat Wendy!' diye yalvardı Michael, başını onun kucağına koyarak.", "Participle phrase 'resting his head'; imperative command."),
            ("Wendy smiled tenderly and began the tale of Mr. and Mrs. Darling back in London.", "Wendy şefkatle gülümsedi ve Londra'daki Bay ve Bayan Darling'in hikayesine başladı.", "Coordinate past verbs 'smiled and began'; adverb 'tenderly'."),
            ("'There was once a lovely mother who had three children,' Wendy began softly.", "'Bir zamanlar üç çocuğu olan çok güzel bir anne varmış,' diye başladı Wendy usulca.", "Existential clause 'There was'; relative clause 'who had three children'."),
            ("'And she always kept the bedroom window wide open so they could fly home.'", "'Ve çocuklar eve uçabilsinler diye yatak odasının penceresini daima ardına kadar açık tutarmış.'", "Purpose clause 'so they could fly home'; adverb 'wide open'."),
            ("Peter groaned in bitter disagreement: 'You are wrong about mothers, Wendy.'", "Peter acı bir itirazla inledi: 'Anneler konusunda yanılıyorsun Wendy.'", "Prepositional phrase 'in bitter disagreement'; adjective 'wrong'."),
            ("'Long ago I flew back to my mother, but the window was barred shut.'", "'Uzun zaman önce anneme geri uçtum fakat pencere parmaklıklarla sımsıkı kapatılmıştı.'", "Coordinate clauses; passive resultative 'barred shut'."),
            ("'And another little boy was sleeping happily in my little bed!'", "'Ve benim küçük yatağımda başka bir küçük oğlan neşeyle uyuyordu!'", "Past continuous 'was sleeping'; possessive 'my bed'."),
            ("A terrible chill of anxiety struck through John and Michael's little hearts.", "John ve Michael'ın minik yüreklerine korkunç bir endişe ürpertisi saplandı.", "Past verb 'struck through'; noun phrase 'chill of anxiety'."),
            ("'Wendy, let us go home tonight before our window is barred!' cried John.", "'Wendy, penceremiz kapatılmadan önce bu gece eve gidelim!' diye haykırdı John.", "Imperative 'let us go'; temporal passive clause 'before window is barred'."),
            ("All the Lost Boys pleaded with Wendy to take them along to London.", "Bütün Kayıp Çocuklar onları da Londra'ya götürmesi için Wendy'ye yalvardılar.", "Verb + object + infinitive 'pleaded with Wendy to take'."),
            ("'My mother and father will adopt all of you,' promised Wendy with shining eyes.", "'Annem ve babam hepinizi evlat edinecektir,' diye söz verdi Wendy parıldayan gözlerle.", "Future modal 'will adopt'; prepositional phrase 'with shining eyes'."),
            ("The boys danced for joy, packing their small belongings and hugging Wendy.", "Oğlanlar küçük eşyalarını toplayıp Wendy'ye sarılarak sevinçten dans ettiler.", "Coordinate participles 'packing and hugging'; prepositional phrase 'for joy'."),
            ("Only Peter stood alone by the fire, looking proud, cold, and detached.", "Yalnızca Peter ocağın yanında tek başına dikiliyor, gururlu, soğuk ve mesafeli görünüyordu.", "Coordinate adjectives 'proud, cold, detached'; past verb 'stood'."),
            ("'I am not coming with you,' said Peter, 'I will not grow up.'", "'Sizinle gelmiyorum,' dedi Peter, 'ben büyümeyeceğim.'", "Present continuous for future; modal refusal 'will not grow up'."),
            ("Wendy embraced him with deep sorrow, but Peter turned his face away.", "Wendy derin bir kederle ona sarıldı fakat Peter yüzünü öbür yana çevirdi.", "Phrasal verb 'turned away'; prepositional phrase 'with deep sorrow'."),
            ("'Goodbye, Wendy,' said Peter calmly, 'have a pleasant journey to the mainland.'", "'Hoşça kal Wendy,' dedi Peter sakince, 'anakitaya yolculuğun güzel geçsin.'", "Direct speech; adjective 'pleasant'."),
            ("Suddenly, a terrible sound of war and shrieking broke out above ground.", "Birdenbire yerin üstünden korkunç bir savaş ve çığlık sesi koptu.", "Phrasal verb 'broke out'; coordinate nouns 'war and shrieking'.")
        ]
    },
    # Page 12: The Pirate Ambush
    {
        "page_number": 12,
        "title": "The Pirate Ambush",
        "vocab": [
            ("ambush", "pusu kurmak / pusu"),
            ("slaughter", "katletmek, kılıçtan geçirmek"),
            ("captive", "esir, tutsak"),
            ("tam-tam", "davul sesi, tam-tam"),
            ("treachery", "ihanet, kalleşlik"),
            ("shackle", "zincirlemek / pranga"),
            ("silence", "sessizlik"),
            ("plank", "korsan tahtası")
        ],
        "sentences": [
            ("Hook had broken the ancient jungle truce and attacked the Indian camp by surprise.", "Hook kadim orman barışını bozmuş ve Kızılderili kampına baskınla saldırmıştı.", "Coordinate past perfect verbs; prepositional phrase 'by surprise'."),
            ("The pirates charged with ruthless savagery, scattering the brave warriors.", "Korsanlar acımasız bir vahşetle hücum ederek cesur savaşçıları darmadağın ettiler.", "Participial clause 'scattering warriors'; noun phrase 'ruthless savagery'."),
            ("Tiger Lily and a few surviving braves fled into the safety of the dark forest.", "Kaplan Zambağı ve hayatta kalan birkaç savaşçı karanlık ormanın güvenliğine kaçtılar.", "Participial adjective 'surviving braves'; directional phrase 'into safety'."),
            ("Hook knew that the children underground would listen for the victory tam-tam.", "Hook, yer altındaki çocukların zafer davulunun sesini dinleyeceğini biliyordu.", "Noun clause 'that children would listen for'; compound noun 'victory tam-tam'."),
            ("He ordered a pirate to beat the Indian drum in the rhythm of tribal victory.", "Bir korsana, Kızılderili davulunu kabile zaferi ritmiyle çalmasını emretti.", "Verb + object + infinitive 'ordered to beat'; prepositional phrase 'in rhythm'."),
            ("Below, Peter and the children heard the beating drum and cheered joyfully.", "Aşağıda Peter ve çocuklar vuran davul sesini duydular ve neşeyle tezahürat yaptılar.", "Coordinate past verbs 'heard and cheered'; adverb 'joyfully'."),
            ("'The redskins have won!' cried Peter, 'it is safe for you to go now!'", "'Kızılderililer kazandı!' diye bağırdı Peter, 'artık gitmeniz güvenli!'", "Present perfect 'have won'; dummy subject 'it is safe for you'."),
            ("One by one, the boys scrambled up through their hollow tree trunks.", "Oğlanlar birer birer oyuk ağaç gövdelerinden yukarı tırmandılar.", "Frequency idiom 'one by one'; phrasal verb 'scrambled up through'."),
            ("As each boy emerged into the open air, rough pirate hands seized him.", "Her bir çocuk açık havaya çıktığında, kaba korsan elleri onu yakaladı.", "Time clause with 'as'; past verb 'seized'."),
            ("They were gagged, bound with heavy cords, and tossed aside like sacks of flour.", "Ağızları tıkandı, kalın iplerle bağlandılar ve un çuvalları gibi bir kenara fırlatıldılar.", "Series of passive past verbs; simile 'like sacks of flour'."),
            ("Wendy was captured last, treated with mock politeness by Captain Hook himself.", "En son Wendy yakalandı; bizzat Kaptan Hook tarafından sahte bir nezaketle muamele gördü.", "Passive participle phrase 'treated with mock politeness'; emphatic reflexive."),
            ("The pirates marched the helpless children away toward the Jolly Roger.", "Korsanlar çaresiz çocukları Jolly Roger gemisine doğru yürütüp götürdüler.", "Directional prepositional phrase 'toward the Jolly Roger'."),
            ("Hook remained behind alone, gazing down into Peter's hollow entrance tree.", "Hook geride yapayalnız kaldı, Peter'ın oyuk giriş ağacından aşağıya doğru baktı.", "Coordinate participles 'gazing down'; adjective 'alone'."),
            ("He squeezed his lean body through the narrow hole and dropped into the room.", "Zayıf bedenini dar delikten içeri soktu ve odanın içine indi.", "Coordinate past verbs 'squeezed and dropped'."),
            ("Peter was fast asleep on the large bed, breathing softly with his dagger near.", "Peter koca yatağın üzerinde derin uykudaydı, hançeri yanında usulca nefes alıyordu.", "Absolute phrase 'with dagger near'; idiom 'fast asleep'."),
            ("Hook noticed a glass containing Peter's nightly medicinal draught on the table.", "Hook masanın üzerinde Peter'ın her gece içtiği şifalı ilacını içeren bardağı fark etti.", "Participial adjective 'containing draught'; past verb 'noticed'."),
            ("He pulled a tiny yellow vial of deadly poison from his pocket with a sinister smile.", "Uğursuz bir tebessümle cebinden öldürücü zehirle dolu minik sarı bir şişe çıkardı.", "Prepositional phrase 'with a sinister smile'; compound noun 'deadly poison'."),
            ("He poured five drops of the lethal liquid into Peter's medicine cup.", "Peter'ın ilaç fincanına bu ölümcül sıvıdan beş damla damlattı.", "Past verb 'poured'; compound noun 'lethal liquid'."),
            ("'Now, Peter Pan,' whispered Hook maliciously, 'sleep thy eternal sleep!'", "'Şimdi Peter Pan,' diye fısıldadı Hook sinsice, 'sonsuz uykunu uyu!'", "Archaic possessive 'thy eternal sleep'; adverb 'maliciously'."),
            ("Hook climbed back out into the night, leaving the doomed hero sleeping peacefully.", "Hook karanlık gecenin içine geri tırmandı; kaderine mahkum kahramanı huzurla uyur bıraktı.", "Participle clause 'leaving hero sleeping'; participial adjective 'doomed'.")
        ]
    },
    # Page 13: Tinker Bell Drinks the Poison
    {
        "page_number": 13,
        "title": "Tinker Bell's Sacrifice",
        "vocab": [
            ("poison", "zehir"),
            ("sacrifice", "fedakarlık"),
            ("faint", "güçsüz, zayıf"),
            ("glimmer", "zayıfça parıldamak"),
            ("clap", "alkışlamak"),
            ("believe", "inanmak"),
            ("revive", "canlanmak, hayata dönmek"),
            ("vow", "ant içmek")
        ],
        "sentences": [
            ("Peter woke up suddenly, hearing a soft tapping at his door.", "Peter kapısında hafif bir tıkırtı duyarak aniden uyandı.", "Participle phrase 'hearing a tapping'; adverb 'suddenly'."),
            ("He let in Tinker Bell, who was flying wildly in frantic distress.", "Çılgınca panik içinde uçuşan Tinker Bell'i içeri aldı.", "Relative clause with past continuous 'who was flying wildly'."),
            ("'Wendy and the boys have been captured by the pirates!' she rang out frantically.", "'Wendy ve çocuklar korsanlar tarafından esir alındı!' diye çan gibi çaldı çılgınca.", "Present perfect passive 'have been captured'; adverb 'frantically'."),
            ("Peter sprang to his feet, buckling on his sword with blazing determination.", "Peter alev alev yanan bir kararlılıkla kılıcını kuşanarak ayağa fırladı.", "Participle phrase 'buckling on his sword'; idiom 'sprang to his feet'."),
            ("'I will rescue them!' cried Peter, 'I will save Wendy or die trying!'", "'Onları kurtaracağım!' diye haykırdı Peter, 'Wendy'yi kurtaracağım ya da denerken öleceğim!'", "Future coordinate declarations; idiom 'die trying'."),
            ("He reached for his cup of medicine to drink before departing.", "Yola çıkmadan önce içmek için ilaç fincanına uzandı.", "Phrasal verb 'reached for'; preposition 'before departing'."),
            ("'No, Peter!' shrieked Tinker Bell, 'Hook has poisoned it!'", "'Hayır Peter!' diye çığlık attı Tinker Bell, 'Hook onu zehirledi!'", "Present perfect 'has poisoned'; direct speech."),
            ("Peter laughed in disbelief: 'Hook could never get down here into our home.'", "Peter inanmazlıkla güldü: 'Hook bizim evimize buraya asla inemezdi.'", "Modal 'could never get down'; noun phrase 'in disbelief'."),
            ("He raised the cup to his lips, but Tinker Bell darted between them.", "Fincanı dudaklarına götürdü fakat Tinker Bell fincanla dudaklarının arasına daldı.", "Coordinate past verbs 'raised and darted'; preposition 'between them'."),
            ("She drank the entire poisonous draught in one single, heroic gulp.", "Bütün zehirli ilacı tek bir kahramanca yudumda dikip içti.", "Adjective pair 'entire poisonous'; noun phrase 'heroic gulp'."),
            ("'Tink, why did you do that?' cried Peter in sudden terror.", "'Tink, bunu neden yaptın?' diye haykırdı Peter ani bir dehşet içinde.", "Past question; prepositional phrase 'in sudden terror'."),
            ("The fairy fluttered down to the tabletop, her golden light fading fast.", "Perinin altın ışığı hızla sönerek masanın üzerine doğru kanat çırparak düştü.", "Absolute construction 'her light fading fast'; phrasal verb 'fluttered down'."),
            ("'It was poisoned, Peter,' she whispered in a tiny, dying voice.", "'Zehirliydi Peter,' diye fısıldadı minicik, tükenen bir sesle.", "Prepositional phrase 'in a dying voice'; passive fact."),
            ("'And I think I get well again if children believe in fairies.'", "'Ve sanırım çocuklar perilere inanırsa ben yeniden iyileşirim.'", "Conditional clause 'if children believe'; present simple."),
            ("Peter turned to the dark sleeping world outside and cried with all his soul.", "Peter dışarıdaki karanlık uyuyan dünyaya döndü ve bütün ruhuyla haykırdı.", "Coordinate past verbs 'turned and cried'; phrase 'with all his soul'."),
            ("'Do you believe in fairies?' shouted Peter to every child dreaming across the earth.", "'Perilere inanıyor musunuz?' diye yeryüzünde rüya gören her bir çocuğa haykırdı Peter.", "Direct address question; participial phrase 'dreaming across the earth'."),
            ("'If you believe, clap your hands! Do not let Tink die!'", "'Eğer inanıyorsanız ellerinizi çırpın! Tink'in ölmesine izin vermeyin!'", "Imperative commands; negative imperative 'do not let die'."),
            ("From millions of nurseries across the sleeping world came a roar of clapping hands.", "Uyuyan dünyanın dört bir yanındaki milyonlarca çocuk odasından alkış seslerinin gürültüsü yükseldi.", "Inverted locative sentence; noun phrase 'roar of clapping hands'."),
            ("Tinker Bell's light flashed brilliant, green and bright once more with bursting life.", "Tinker Bell'in ışığı coşan bir hayatla bir kez daha zümrüt gibi parlak ve ışıl ışıl yandı.", "Coordinate adjectives 'brilliant, green, bright'; phrase 'with bursting life'."),
            ("'Now for Captain Hook!' swore Peter, drawing his sword with deadly fury.", "'Şimdi sıra Kaptan Hook'ta!' diye ant içti Peter, ölümcül bir öfkeyle kılıcını çekerek.", "Idiom 'Now for...'; participle phrase 'drawing his sword'.")
        ]
    },
    # Page 14: The Jolly Roger and Hook's End
    {
        "page_number": 14,
        "title": "The Battle on the Jolly Roger",
        "vocab": [
            ("plank", "korsan tahtası"),
            ("sword", "kılıç"),
            ("cabin", "kabin, kamara"),
            ("crocodile", "timsah"),
            ("shriek", "çığlık atmak"),
            ("vanquish", "bozguna uğratmak, yenmek"),
            ("tick", "tıkırdamak"),
            ("deck", "güverte")
        ],
        "sentences": [
            ("The Jolly Roger lay anchored under the misty moon in complete silence.", "Jolly Roger puslu ayın altında tam bir sessizlik içinde demirli yatıyordu.", "Copular past 'lay anchored'; prepositional phrase 'in silence'."),
            ("The plank was prepared, extending out over the dark, shark-infested sea.", "Karanlık, köpekbalıklarıyla kaynayan denizin üzerine doğru uzanan tahta hazırlanmıştı.", "Passive voice 'was prepared'; participle modifier 'extending out'."),
            ("Hook gloated over the bound children lined up upon the wooden deck.", "Hook ahşap güvertede sıraya dizilmiş bağlı çocuklara bakıp kıs kıs güldü.", "Phrasal verb 'gloated over'; participle modifier 'lined up upon deck'."),
            ("'Six of you will walk the plank tonight!' sneered the cruel pirate captain.", "'Altınız bu gece tahtadan denize yürüyecek!' diye alayla sırıttı zalim korsan kaptan.", "Future modal 'will walk'; adjective 'cruel'."),
            ("Wendy stood proudly, refusing to show a single tear of weakness.", "Wendy tek bir zayıflık gözyaşı bile göstermeyi reddederek başı dik durdu.", "Adverb 'proudly'; participle clause 'refusing to show'."),
            ("Suddenly, from the water beneath the ship came a terrifying sound: 'Tick-tick-tick!'", "Birdenbire geminin altındaki sudan dehşet verici bir ses geldi: 'Tık-tık-tık!'", "Inverted sentence; onomatopoeic quotation."),
            ("Hook cowered against the mainmast, shuddering in absolute paralyzed horror.", "Hook ana direğin dibine sindi, tam bir felç edici dehşet içinde titredi.", "Phrasal verb 'cowered against'; participle phrase 'shuddering in horror'."),
            ("The pirates covered their faces, waiting for the dreaded crocodile to board.", "Korsanlar korkunç timsahın gemiye çıkmasını bekleyerek yüzlerini kapattılar.", "Participle phrase 'waiting for crocodile to board'."),
            ("It was not the beast, but Peter Pan himself, imitating the clock as he climbed the chains.", "Gelen canavar değil, zincirlere tırmanırken saati taklit eden Peter Pan'ın ta kendisiydi.", "Negative contrast 'not... but'; participle clause 'imitating clock'."),
            ("Peter slipped into the dark cabin and armed himself with pirate swords.", "Peter karanlık kamaraya süzüldü ve kendini korsan kılıçlarıyla silahlandırdı.", "Coordinate past verbs 'slipped and armed'."),
            ("One by one, pirates sent into the cabin were struck down in total darkness.", "Kamaraya gönderilen korsanlar zifiri karanlıkta birer birer yere serildiler.", "Passive voice 'were struck down'; prepositional phrase 'in total darkness'."),
            ("Peter sprang out upon the open deck, freeing the boys with swift slashes.", "Peter açık güverteye fırladı, seri darbelerle oğlanların bağlarını kesti.", "Phrasal verb 'sprang out upon'; participle phrase 'freeing boys'."),
            ("'I am youth, I am joy, I am a little bird that has broken out of the egg!' cried Peter.", "'Ben gençliğim, ben neşeyim, ben yumurtasını kırmış minik bir kuşum!' diye haykırdı Peter.", "Series of poetic metaphors celebrating freedom."),
            ("The battle raged across the deck, boys and pirates clashing in wild combat.", "Savaş güverte boyunca alevlendi; çocuklar ve korsanlar vahşi bir çarpışmayla kılıç tokuşturdular.", "Absolute construction 'boys and pirates clashing'."),
            ("The Lost Boys fought bravely, driving the superstitious pirates into the sea.", "Kayıp Çocuklar cesurca savaştılar, batıl inançlı korsanları denize döktüler.", "Participle phrase 'driving pirates into sea'."),
            ("Peter crossed blades with Captain Hook in the final decisive duel.", "Peter son ve belirleyici düelloda Kaptan Hook ile kılıç kılıca geldi.", "Idiom 'crossed blades with'; adjective pair 'final decisive'."),
            ("Hook fought with wicked fury, but Peter's agility was too much for the tyrant.", "Hook hain bir öfkeyle savaştı fakat Peter'ın çevikliği tiran için fazlaydı.", "Coordinate clauses with 'but'; noun 'agility'."),
            ("Peter disarmed Hook and pushed him backward to the edge of the ship.", "Peter Hook'un silahını düşürdü ve onu geminin kenarına doğru geri itti.", "Coordinate past verbs 'disarmed and pushed'."),
            ("Hook saw the real crocodile waiting in the black water with jaws wide open.", "Hook gerçek timsahın kara suda çeneleri ardına kadar açık halde beklediğini gördü.", "Perception verb 'saw' + participle 'waiting with jaws open'."),
            ("With a final shriek of terror, Hook plunged into the waiting monster's mouth.", "Son bir dehşet çığlığıyla Hook, bekleyen canavarın ağzının içine yuvarlandı.", "Prepositional phrase 'with a shriek'; past verb 'plunged into'.")
        ]
    },
    # Page 15: The Return Home and the Open Window
    {
        "page_number": 15,
        "title": "The Open Window",
        "vocab": [
            ("nursery", "çocuk odası"),
            ("window", "pencere"),
            ("mother", "anne"),
            ("tears", "gözyaşları"),
            ("bed", "yatak"),
            ("grow", "büyümek"),
            ("remember", "hatırlamak"),
            ("heart", "yürek, kalp")
        ],
        "sentences": [
            ("The Jolly Roger was theirs now, and Peter took the helm dressed as a captain.", "Jolly Roger artık onlarındı ve Peter bir kaptan gibi giyinmiş halde dümene geçti.", "Coordinate clauses; passive participle 'dressed as a captain'."),
            ("With Wendy, John, Michael, and the Lost Boys aboard, they sailed through the sky.", "Wendy, John, Michael ve Kayıp Çocuklar güvertedeyken gökyüzünde yelken açtılar.", "Absolute phrase 'with everyone aboard'; phrasal verb 'sailed through'."),
            ("The pirate ship flew gracefully on fairy dust all the way back to London.", "Korsan gemisi peri tozu sayesinde Londra'ya kadar gökyüzünde zarifçe uçtu.", "Prepositional phrases indicating means and destination."),
            ("Meanwhile in the nursery, Mrs. Darling sat sadly by the open window.", "Bu esnada çocuk odasında Bayan Darling hüzünle açık pencerenin yanında oturuyordu.", "Adverbs 'meanwhile' and 'sadly'; prepositional phrase 'by the window'."),
            ("She had never closed the window, hoping and praying for her children's return.", "Çocuklarının dönüşünü umarak ve dua ederek pencereyi hiçbir zaman kapatmamıştı.", "Past perfect with 'never'; coordinate participles 'hoping and praying'."),
            ("Peter flew ahead into the room first, intending to lock the window against them.", "Peter ilk önce odaya uçtu, pencereyi onların yüzüne kilitlemeye niyetliydi.", "Infinitive of purpose 'to lock against them'; participle 'intending'."),
            ("He saw Mrs. Darling's sleeping face, marked with two sorrowful tears.", "Bayan Darling'in kederli iki damla gözyaşıyla iz bırakmış uyuyan yüzünü gördü.", "Perception verb 'saw' + past participle 'marked with tears'."),
            ("'She loves them so much,' murmured Peter, 'she needs Wendy more than I do.'", "'Onları öyle çok seviyor ki,' diye mırıldandı Peter, 'Wendy'ye benden daha çok ihtiyacı var.'", "Result clause 'loves so much'; comparative 'more than I do'."),
            ("With a noble pang of selflessness, Peter threw the window wide open again.", "Soylu bir fedakarlık sızısıyla Peter pencereyi bir kez daha ardına kadar açtı.", "Prepositional phrase 'with a pang of selflessness'; adverb 'wide open'."),
            ("The three Darling children slipped through the window into their little beds.", "Üç Darling çocuğu pencereden süzülerek küçük yataklarının içine girdiler.", "Phrasal verb 'slipped through into'; possessive 'their beds'."),
            ("When Mrs. Darling opened her eyes, she thought she was still dreaming.", "Bayan Darling gözlerini açtığında hala rüya gördüğünü sandı.", "Time clause 'when she opened'; noun clause 'she was dreaming'."),
            ("Her children jumped into her arms, weeping, kissing, and laughing with joy.", "Çocukları kucağına atıldılar; ağlayarak, öperek ve sevinçle gülerek.", "Series of participles describing emotional reunion."),
            ("Mr. Darling and Nana rushed in, and the nursery erupted in tears of gratitude.", "Bay Darling ve Nana içeri koştular ve çocuk odası şükran gözyaşlarıyla dolup taştı.", "Coordinate past verbs 'rushed in and erupted'."),
            ("The Lost Boys were all adopted into the family and promised to go to school.", "Kayıp Çocukların hepsi aileye evlat edinildiler ve okula gitmeye söz verdiler.", "Passive voice 'were adopted'; verb + infinitive 'promised to go'."),
            ("Peter stood outside on the balcony, watching the happy family through the glass.", "Peter dışarıda balkonda durmuş, camın ardından bu mutlu aileyi izliyordu.", "Participle clause 'watching through glass'; adjective 'happy'."),
            ("He knew that they would all grow up soon, but he would remain young forever.", "Hepsinin çok geçmeden büyüyeceğini biliyordu, fakat kendisi sonsuza dek genç kalacaktı.", "Noun clauses contrasting temporal destinies; modal 'would remain'."),
            ("Wendy promised to fly with him to Neverland every spring for spring-cleaning.", "Wendy bahar temizliği için her ilkbaharda onunla birlikte Varolmayan Ülke'ye uçmaya söz verdi.", "Verb + infinitive 'promised to fly'; prepositional phrase 'for spring-cleaning'."),
            ("Peter took out the acorn button and touched it gently to his lips.", "Peter meşe palamudu düğmesini çıkardı ve onu usulca dudaklarına değdirdi.", "Coordinate past verbs 'took out and touched'; adverb 'gently'."),
            ("He crowed one last triumphant crow and flew off into the starry night.", "Son bir muzaffer horoz sesi koyuverdi ve yıldızlı gecenin içine doğru uçup gitti.", "Coordinate past verbs 'crowed and flew off'; compound adjective 'starry night'."),
            ("And so long as children are gay and innocent and heartless, Peter Pan will fly.", "Ve çocuklar neşeli, masum ve kalpsiz oldukları müddetçe Peter Pan uçmaya devam edecektir.", "Famous concluding line of the book; conditional 'so long as'.")
        ]
    }
]

def generate_data_file():
    data_path = os.path.join(os.path.dirname(__file__), "book_16_data.py")
    
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
        f.write('"""\nBook 16: Peter Pan: The Boy Who Would Not Grow Up (J. M. Barrie)\n')
        f.write('Level 1 Graded Reader — 15 Pages x 20 Sentences = 300 Sentences.\n"""\n\n')
        f.write('BOOK_TITLE = "Peter Pan: The Boy Who Would Not Grow Up (15 Sayfa / 300 Cümle / Graded Reader)"\n')
        f.write('AUTHOR = "J. M. Barrie"\n\n')
        f.write(f"PAGES_DATA = {pprint.pformat(pages_data, indent=4, width=120)}\n")
        
    print(f"Successfully wrote {data_path}")

if __name__ == "__main__":
    generate_data_file()
