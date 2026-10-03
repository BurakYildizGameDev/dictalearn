"""
Book 14 Generator: The Jungle Book: Mowgli of the Free People (Rudyard Kipling)
15 Pages, exactly 20 sentences per page = 300 sentences total.
8 Target vocabulary terms per page = 120 vocabulary items total.
Level 1 / Seviye 1 Graded Reader for English learners.
"""

import os
import pprint

BOOK_META = {
    "id": "book_14_the_jungle_book",
    "title": "The Jungle Book: Mowgli of the Free People",
    "subtitle": "Rudyard Kipling's Classic Tale of Honor, Wilderness, and Brotherhood",
    "author": "Rudyard Kipling",
    "level": "Seviye 1 (A1-A2 Beginner)",
    "target_readers": "İngilizce öğrenenler ve klasik macera sevenler için çift dilli okuma kitabı",
    "total_pages": 15,
    "sentences_per_page": 20,
    "total_sentences": 300,
    "theme_color_primary": "#1B4D3E",    # Deep Jungle Green
    "theme_color_secondary": "#B8860B",  # Dark Goldenrod
    "theme_color_accent": "#C0392B",     # Shere Khan Tiger Amber/Crimson
    "theme_color_light": "#E8F5E9"       # Soft Moss Tint
}

# 15 Pages x 20 sentences = 300 sentences
PAGES = [
    # Page 1: Mowgli's Brothers (The Man-Cub Enters the Cave)
    {
        "page_number": 1,
        "title": "A Man-Cub in the Wolf Cave",
        "vocab": [
            ("jungle", "orman, vahşi doğa"),
            ("cave", "mağara"),
            ("cub", "yavru (kurt/ayı/aslan)"),
            ("naked", "çıplak, savunmasız"),
            ("bold", "cesur, korkusuz"),
            ("shelter", "barınak, sığınak"),
            ("whisper", "fısıldamak"),
            ("gentle", "nazik, yumuşak")
        ],
        "sentences": [
            ("It was seven o'clock of a warm evening in the Seeonee hills.", "Seeonee tepelerinde ılık bir akşam saat yedi sularıydı.", "Past time phrase; 'warm evening' describes climate."),
            ("Father Wolf woke up from his day's rest and stretched his paws.", "Baba Kurt gündüz uykusundan uyandı ve patilerini esnetti.", "Phrasal verb 'wake up'; regular past 'stretched'."),
            ("Mother Wolf lay with her big gray nose dropped across her four tumbling cubs.", "Anne Kurt, büyük gri burnunu yuvarlanan dört yavrusunun üzerine koymuş yatıyordu.", "Irregular verb 'lay' (past of lie); participial adjective 'tumbling'."),
            ("The moon shone into the mouth of the cave where they all lived.", "Ay ışığı, hepsinin birlikte yaşadığı mağaranın ağzına vuruyordu.", "Irregular past 'shone' (shine); relative clause 'where they all lived'."),
            ("Suddenly, a dry rustle sounded among the thick bushes outside.", "Aniden, dışarıdaki sık çalıların arasında kuru bir hışırtı duyuldu.", "Adverb 'suddenly'; preposition 'among' for groups."),
            ("Father Wolf sprang forward with his ears pointed high.", "Baba Kurt kulaklarını dikmiş halde ileriye doğru fırladı.", "Irregular past 'sprang' (spring); participle phrase 'with his ears pointed'."),
            ("Something was coming up the hill in the dark shadows.", "Karanlık gölgelerin içinde bir şey tepeye doğru çıkıyordu.", "Past continuous 'was coming'; indefinite pronoun 'something'."),
            ("Directly in front of him, holding on by a low branch, stood a tiny baby.", "Tam önünde, alçak bir dala tutunarak duran küçücük bir bebek vardı.", "Inverted sentence structure; participial clause 'holding on by'."),
            ("He was a naked brown human baby who could scarcely walk.", "Henüz zar zor yürüyebilen, çıplak, esmer bir insan yavrusuydu.", "Adverb 'scarcely' means barely or hardly."),
            ("The little boy looked up into Father Wolf's face and laughed happily.", "Küçük oğlan Baba Kurt'un yüzüne baktı ve neşeyle güldü.", "Phrasal verb 'look up into'; adverb 'happily'."),
            ("'Is that a man's cub?' asked Mother Wolf softly.", "'O bir insan yavrusu mu?' diye sordu Anne Kurt usulca.", "Direct question; possessive 'man's cub'."),
            ("'I have never seen one before in our hills,' replied Father Wolf.", "'Tepelerimizde daha önce hiç böylesini görmemiştim,' diye yanıtladı Baba Kurt.", "Present perfect with 'never' indicates life experience."),
            ("Father Wolf picked the baby up very carefully between his jaws.", "Baba Kurt bebeği çenelerinin arasına alıp çok dikkatlice kaldırdı.", "Separable phrasal verb 'picked up'; adverb 'carefully'."),
            ("Not a single tooth scratched the tender skin of the child.", "Tek bir diş bile çocuğun narin cildini çizmedi.", "Negative subject 'not a single tooth'; adjective 'tender'."),
            ("He placed the boy down beside his own little cubs.", "Oğlanı kendi minik yavrularının yanına bıraktı.", "Preposition 'beside' means next to."),
            ("The tiny infant pushed his way close to the warm fur.", "Minik bebek sıcak kürkün yanına sokulmak için yol açtı.", "Expression 'push one's way'; comparative closeness 'close to'."),
            ("'He has no fear at all,' said Mother Wolf with a proud smile.", "'Onda hiç korku yok,' dedi Anne Kurt gururlu bir tebessümle.", "Negative expression 'no fear at all'; prepositional phrase 'with a proud smile'."),
            ("The other four wolf cubs nudged their new brother playfully.", "Diğer dört kurt yavrusu yeni kardeşlerini oyunbazca dürttü.", "Past tense 'nudged'; adverb 'playfully'."),
            ("A great shadow fell across the entrance of the dark cave.", "Karanlık mağaranın girişine koca bir gölge düştü.", "Irregular past 'fell' (fall); preposition 'across'."),
            ("The wild law of the jungle was about to be tested.", "Ormanın vahşi kanunları sınanmak üzereydi.", "Idiomatic structure 'was about to' expresses immediate future in the past.")
        ]
    },
    # Page 2: Shere Khan's Claim & Mother Wolf's Defiance
    {
        "page_number": 2,
        "title": "The Tiger and the Mother Wolf",
        "vocab": [
            ("lame", "topal, aksak"),
            ("roar", "kükremek, kükreyiş"),
            ("rage", "öfke, hiddet"),
            ("defend", "savunmak, korumak"),
            ("belong", "ait olmak"),
            ("stripes", "çizgiler (kaplan deseni)"),
            ("fierce", "şiddetli, yırtıcı"),
            ("refuse", "reddetmek, geri çevirmek")
        ],
        "sentences": [
            ("A huge striped head appeared in the narrow entrance of the cave.", "Mağaranın dar girişinde devasa çizgili bir kafa belirdi.", "Adjective 'striped'; noun phrase 'narrow entrance'."),
            ("It was Shere Khan, the great tiger who lived near the Waingunga river.", "Bu, Waingunga nehri yakınlarında yaşayan büyük kaplan Shere Han'dı.", "Relative clause introduced by 'who' defining the tiger."),
            ("His yellow eyes burned with angry greed in the darkness.", "Sarı gözleri karanlıkta öfkeli bir açgözlülükle parlıyordu.", "Metaphorical verb 'burned with'; noun 'greed'."),
            ("'A man-cub entered this cave,' growled the big lame tiger.", "'Bu mağaraya bir insan yavrusu girdi,' diye homurdandı koca topal kaplan.", "Present perfect / simple past; adjective 'lame' means limping."),
            ("'Give him to me at once, for he is my lawful prey!'", "'Onu derhal bana verin, zira o benim meşru avımdır!'", "Imperative sentence; coordinating conjunction 'for' meaning because."),
            ("Father Wolf stood tall and stared into the tiger's eyes.", "Baba Kurt dik durdu ve kaplanın gözlerinin içine baktı.", "Irregular past 'stood' (stand); phrasal verb 'stare into'."),
            ("'The wolves are a free people,' answered Father Wolf firmly.", "'Kurtlar özgür bir halktır,' diye yanıt verdi Baba Kurt kararlılıkla.", "Collective noun 'free people'; adverb 'firmly'."),
            ("'We take orders only from the leader of the pack, not from you.'", "'Biz emirleri sadece sürünün liderinden alırız, senden değil.'", "Negative contrast 'not from you'; noun phrase 'leader of the pack'."),
            ("Shere Khan let out a roar of rage that echoed through the hills.", "Shere Han tepelerde yankılanan bir öfke kükremesi kopardı.", "Phrasal verb 'let out'; relative clause 'that echoed'."),
            ("Mother Wolf shook her gray coat and sprang to the front.", "Anne Kurt gri kürkünü silkeledi ve öne doğru atıldı.", "Irregular past 'shook' (shake); phrasal verb 'spring to'."),
            ("Her green eyes glowed like two green stars against the tiger.", "Yeşil gözleri kaplana karşı iki yeşil yıldız gibi parladı.", "Simile 'like two green stars'; preposition 'against'."),
            ("'The man's cub belongs to me!' she cried fiercely.", "'Bu insan yavrusu bana aittir!' diye haykırdı yırtıcı bir sesle.", "Verb 'belong to'; adverb 'fiercely'."),
            ("'He shall not be killed by your wicked claws!'", "'Senin hain pençelerinle öldürülmeyecek!'", "Archaic/emphatic modal 'shall not be killed' (passive)."),
            ("'He shall live to run with the Free Pack across the valleys.'", "'O, vadiler boyunca Özgür Sürü ile koşmak için yaşayacak.'", "Infinitive of purpose 'to run with'; preposition 'across'."),
            ("'And in the end, lame butcher, he shall hunt you down!'", "'Ve sonunda, seni topal kasap, o senin peşine düşüp seni avlayacak!'", "Vocative phrase 'lame butcher'; phrasal verb 'hunt down'."),
            ("Shere Khan stepped backward into the bushes because he knew her fury.", "Shere Han çalıların arasına doğru geriledi çünkü onun öfkesini biliyordu.", "Phrasal verb 'step backward'; causal conjunction 'because'."),
            ("He knew that fighting a mother wolf in her den meant certain death.", "İnindeki bir anne kurtla savaşmanın kesin ölüm anlamına geldiğini biliyordu.", "Gerund subject 'fighting a mother wolf'; noun 'den'."),
            ("'Each dog barks in his own yard,' muttered the tiger bitterly.", "'Her köpek kendi avlusunda havlar,' diye mırıldandı kaplan acıyla.", "Proverbial expression; adverb 'bitterly'."),
            ("'We shall see what the Pack says at the Council Rock!'", "'Sürünün Konsey Kayası'nda ne diyeceğini hep birlikte göreceğiz!'", "Future clause 'what the Pack says'."),
            ("With a low snarl, the striped beast vanished into the dark jungle.", "Alçak bir homurtuyla çizgili canavar karanlık ormanda gözden kayboldu.", "Prepositional phrase 'with a low snarl'; verb 'vanished'."),
        ]
    },
    # Page 3: The Council Rock and Baloo & Bagheera's Support
    {
        "page_number": 3,
        "title": "The Judgment of the Free Pack",
        "vocab": [
            ("council", "konsey, meclis"),
            ("boulder", "büyük kaya kütlesi"),
            ("panther", "panter"),
            ("bear", "ayı"),
            ("witness", "şahit, tanık"),
            ("ransom", "kurtarmalık, diyet"),
            ("shadow", "gölge"),
            ("accept", "kabul etmek")
        ],
        "sentences": [
            ("Once a month, the Seeonee wolf pack gathered at the Council Rock.", "Ayda bir kez, Seeonee kurt sürüsü Konsey Kayası'nda toplanırdı.", "Frequency phrase 'once a month'; past verb 'gathered'."),
            ("Akela, the great gray Lone Wolf, lay upon the highest boulder.", "Büyük gri Yalnız Kurt Akela, en yüksek kaya kütlesinin üzerinde yatıyordu.", "Apposition 'the great gray Lone Wolf'; superlative 'highest'."),
            ("He guided the pack by his strength and his long wisdom.", "Sürüye gücü ve engin bilgeliğiyle yol gösteriyordu.", "Transitive verb 'guided'; abstract noun 'wisdom'."),
            ("The mother wolves brought forward all the new cubs for inspection.", "Anne kurtlar, denetim için tüm yeni yavruları öne getirdiler.", "Phrasal verb 'brought forward'; noun for purpose 'for inspection'."),
            ("Mother Wolf pushed little Mowgli into the open circle.", "Anne Kurt minik Mowgli'yi açık halkanın ortasına doğru itti.", "Proper name 'Mowgli'; adjective 'open'."),
            ("The child sat on the warm stones and began playing with bright pebbles.", "Çocuk ılık taşların üzerine oturdu ve parlak çakıl taşlarıyla oynamaya başladı.", "Verb followed by gerund 'began playing'; noun 'pebbles'."),
            ("From beyond the rocks, Shere Khan's roaring voice echoed.", "Kayaların ötesinden Shere Han'ın kükreyen sesi yankılandı.", "Preposition 'beyond'; participial adjective 'roaring'."),
            ("'The child is mine!' roared the tiger from the shadows.", "'O çocuk benimdir!' diye kükredi kaplan gölgelerin arasından.", "Possessive pronoun 'mine'; prepositional phrase 'from the shadows'."),
            ("Akela did not even turn his gray head toward the noise.", "Akela gri başını gürültüye doğru çevirmedi bile.", "Negative past 'did not even turn'; directional preposition 'toward'."),
            ("'Who speaks for this cub among the Free People?' asked Akela.", "'Özgür Halk arasında bu yavru için kim söz söyleyecek?' diye sordu Akela.", "Question with subject 'who'; preposition 'among'."),
            ("The law required two members who were not his parents to speak.", "Kanun, çocuğun anne babası olmayan iki üyenin konuşmasını şart koşuyordu.", "Verb 'required' followed by object + infinitive."),
            ("Baloo, the sleepy brown bear who taught the cubs the law, stood up.", "Yavrulara kanunu öğreten uykucu kahverengi ayı Baloo ayağa kalktı.", "Appositive clause with relative pronoun 'who'; phrasal verb 'stood up'."),
            ("'I speak for the man's cub,' said the gentle bear.", "'İnsan yavrusu adına ben söz alıyorum,' dedi nazik ayı.", "Phrasal verb 'speak for'; adjective 'gentle'."),
            ("'A man-cub hurts nobody, and I will personally teach him the Law.'", "'Bir insan yavrusu kimseye zarar vermez ve Kanun'u ona bizzat ben öğreteceğim.'", "Indefinite pronoun 'nobody'; adverb 'personally'."),
            ("'We need another voice,' called Akela into the quiet night.", "'Başka bir sese daha ihtiyacımız var,' diye seslendi Akela sessiz geceye.", "Adjective 'another' with singular countable noun; adjective 'quiet'."),
            ("Then a black shadow dropped silently from a high tree.", "Sonra yüksek bir ağaçtan sessizce kara bir gölge indi.", "Adverb 'silently'; past verb 'dropped'."),
            ("It was Bagheera the Black Panther, ink-black and terrible in strength.", "Bu, mürekkep karası ve müthiş güçlü Kara Panter Bagheera'ydı.", "Compound adjective 'ink-black'; prepositional phrase 'in strength'."),
            ("'To kill a naked cub is shameful,' purred the panther.", "'Çıplak bir yavruyu öldürmek utanç vericidir,' diye mırıldandı panter.", "Infinitive as subject 'To kill...'; adjective 'shameful'."),
            ("'I offer a freshly killed fat bull to buy his life for the pack.'", "'Sürü adına onun canını satın almak için yeni öldürülmüş semiz bir boğa teklif ediyorum.'", "Adverb + participle 'freshly killed'; infinitive 'to buy'."),
            ("The wolves accepted the gift, and Mowgli was welcomed into the pack.", "Kurtlar hediyeyi kabul etti ve Mowgli sürüye resmen kabul edildi.", "Passive voice 'was welcomed into'; coordinating conjunction 'and'."),
        ]
    },
    # Page 4: The Law of the Jungle (Lessons with Wise Baloo)
    {
        "page_number": 4,
        "title": "Lessons of the Green Wilderness",
        "vocab": [
            ("climb", "tırmanmak"),
            ("branch", "ağaç dalı"),
            ("stranger", "yabancı"),
            ("honey", "bal"),
            ("master", "öğrenmek, ustalaşmak / usta"),
            ("swim", "yüzmek"),
            ("obey", "itaat etmek, uymak"),
            ("strike", "vurmak, saldırmak")
        ],
        "sentences": [
            ("Mowgli grew up among the wolf cubs under the hot sun.", "Mowgli, kızgın güneşin altında kurt yavrularının arasında büyüdü.", "Phrasal verb 'grew up'; prepositional phrase 'under the hot sun'."),
            ("Father Wolf taught him his business, and the meaning of every jungle sound.", "Baba Kurt ona işini ve her orman sesinin anlamını öğretti.", "Double object verb 'taught him his business'; noun 'meaning'."),
            ("Every rustle in the grass meant something important for his safety.", "Çimlerdeki her bir hışırtı, onun güvenliği için önemli bir anlam taşıyordu.", "Determiner 'every' with singular noun; adjective 'important'."),
            ("Baloo taught him how to tell a rotten branch from a sound one.", "Baloo ona çürük bir dalı sağlam olanından nasıl ayırt edeceğini öğretti.", "Idiomatic expression 'tell A from B'; adjective 'rotten'."),
            ("He taught him how to speak politely to the wild bees when stealing honey.", "Baloo ona bal çalarken yaban arılarıyla nasıl kibarca konuşulacağını öğretti.", "Adverb 'politely'; participle temporal clause 'when stealing honey'."),
            ("Mowgli learned to swim in the deep mountain pools like an otter.", "Mowgli derin dağ göletlerinde bir su samuru gibi yüzmeyi öğrendi.", "Verb + infinitive 'learned to swim'; simile 'like an otter'."),
            ("He learned to climb trees almost as fast as he could run.", "Ağaçlara neredeyse koşabildiği kadar hızlı tırmanmayı öğrendi.", "Comparative equality 'as fast as'; modal 'could'."),
            ("Bagheera showed him how to walk silently without cracking dry twigs.", "Bagheera ona kuru dalları kırmadan nasıl sessizce yürüneceğini gösterdi.", "Preposition 'without' followed by gerund 'cracking'."),
            ("The boy could hang by his hands from branches for an hour.", "Çocuk kollarından dallara tutunarak bir saat boyunca asılı kalabiliyordu.", "Prepositional phrase 'by his hands'; duration 'for an hour'."),
            ("'The Law of the Jungle is old and true as the sky,' said Baloo.", "'Orman Kanunu gökyüzü kadar eski ve gerçektir,' derdi Baloo.", "Adjective comparison 'old and true as the sky'."),
            ("Mowgli had to memorize the Master Words for every hunting tribe.", "Mowgli her avcı kabile için geçerli Efendi Sözleri'ni ezberlemek zorundaydı.", "Modal of past obligation 'had to'; verb 'memorize'."),
            ("'We be of one blood, ye and I,' was the ancient greeting.", "'Biz aynı kandanız, sen ve ben,' kadim selamlama cümlesiydi.", "Archaic subjunctive grammar 'We be... ye and I'."),
            ("With those words, no bird, snake, or beast would harm him.", "Bu sözlerle hiçbir kuş, yılan ya da canavar ona zarar veremezdi.", "Negative determiner 'no'; conditional modal 'would harm'."),
            ("Sometimes Mowgli grew tired and wanted to play all afternoon.", "Bazen Mowgli yorulur ve bütün öğleden sonra oyun oynamak isterdi.", "Copular verb 'grew tired'; time phrase 'all afternoon'."),
            ("Then Baloo gave him a soft cuff on the ear with his great paw.", "O zaman Baloo kocaman pençesiyle onun kulağına hafif bir tokat indirirdi.", "Noun 'cuff' meaning light slap; preposition 'with'."),
            ("'Better that he be bruised by me than killed by ignorance,' argued Baloo.", "'Cehalet yüzünden öleceğine benim tarafımdan hafifçe hırpalanması daha iyidir,' derdi Baloo.", "Subjunctive 'that he be bruised'; comparative 'better... than'."),
            ("Bagheera often watched their lessons with glowing, approving eyes.", "Bagheera onların derslerini çoğu zaman parıldayan, onaylayan gözlerle izlerdi.", "Adverb of frequency 'often'; participial adjectives 'glowing, approving'."),
            ("The boy was quick, bright, and loved the green wild world.", "Çocuk çevik ve zekiydi, yeşil vahşi dünyayı çok seviyordu.", "Adjectives 'quick, bright'; coordinate predicate."),
            ("Yet there were creatures in the treetops who respected no law at all.", "Yine de ağaç tepelerinde hiçbir kanuna saygı duymayan yaratıklar vardı.", "Adverb 'yet'; relative clause 'who respected no law'."),
            ("Danger was watching the little human boy from the high branches.", "Yüksek dallardan tehlike, küçük insan oğlanını gizlice gözetliyordu.", "Past continuous 'was watching'; personification of 'danger'."),
        ]
    },
    # Page 5: The Bandar-log (The Monkey-People Kidnapped Mowgli)
    {
        "page_number": 5,
        "title": "The Lawless Monkey-People",
        "vocab": [
            ("foolish", "aptalca, akılsız"),
            ("chatter", "gevezelik etmek"),
            ("snatch", "kapıp kaçırmak"),
            ("treetop", "ağaç tepesi"),
            ("leader", "lider, önder"),
            ("mock", "alay etmek"),
            ("shame", "utanç"),
            ("kidnap", "kaçırmak (rehin almak)")
        ],
        "sentences": [
            ("The Bandar-log, or Monkey-People, lived high up in the dense branches.", "Bandar-log, yani Maymun Halkı, sık dalların çok yukarısında yaşardı.", "Parenthetical apposition; prepositional phrase 'high up in'."),
            ("They had no law, no leaders, and no memory of yesterday.", "Onların ne bir kanunu, ne liderleri, ne de dünden kalan bir hafızaları vardı.", "Parallel structure with repeated negative 'no'."),
            ("They spent their hours chattering and bragging about their foolish greatness.", "Vakitlerini gevezelik ederek ve aptalca büyüklükleriyle övünerek geçirirlerdi.", "Expression 'spend hours doing'; phrasal verb 'brag about'."),
            ("Baloo had strictly forbidden Mowgli to talk to any monkey.", "Baloo, Mowgli'nin herhangi bir maymunla konuşmasını kesinlikle yasaklamıştı.", "Past perfect 'had strictly forbidden'; infinitive 'to talk'."),
            ("'They are without shame and have no speech of their own,' warned the bear.", "'Onlarda utanma yoktur ve kendilerine ait bir dilleri bile bulunmaz,' diye uyarmıştı ayı.", "Preposition 'without'; idiomatic phrase 'of their own'."),
            ("One hot day, Mowgli rested peacefully in the shade between his two teachers.", "Sıcak bir günde Mowgli, iki öğretmeninin arasındaki gölgede huzurla dinleniyordu.", "Adverb 'peacefully'; preposition 'between' for two items."),
            ("Suddenly, many hairy arms reached down from the green canopy above.", "Aniden, yukarıdaki yeşil kubbeden aşağıya doğru pek çok kıllı kol uzandı.", "Adverb 'suddenly'; phrasal verb 'reached down'."),
            ("Before Mowgli could cry out, strong fingers snatched him by the waist.", "Mowgli haykıramadan önce, güçlü parmaklar onu belinden yakaladı.", "Conjunction 'before'; verb 'snatched' with preposition 'by the waist'."),
            ("He was yanked violently into the upper branches of the trees.", "Ağaçların üst dallarına doğru şiddetle çekiliverdi.", "Passive voice 'was yanked'; adverb 'violently'."),
            ("Baloo woke up with a roar and began crashing through the undergrowth.", "Baloo bir kükremeyle uyandı ve bodur çalıların arasından gürültüyle koşmaya başladı.", "Coordinate clauses; preposition 'through'."),
            ("Bagheera leaped up the trunk with claws digging into the rough bark.", "Bagheera, pençelerini sert kabuğa geçirerek ağaç gövdesine sıçradı.", "Absolute participle phrase 'with claws digging into'."),
            ("But the monkeys were already high above the reach of any panther.", "Fakat maymunlar bir panterin ulaşabileceği yerin çok üstündeydiler bile.", "Adverb 'already'; noun phrase 'the reach of'."),
            ("They carried Mowgli along the swinging highways of the jungle.", "Mowgli'yi ormanın sallanan ağaç otoyolları boyunca taşıdılar.", "Metaphor 'swinging highways of the jungle'."),
            ("Two strong monkeys held his arms and bounded across wide empty air.", "İki güçlü maymun onun kollarını tutuyor ve geniş boşluklar boyunca sıçrıyordu.", "Parallel verbs 'held' and 'bounded'."),
            ("Mowgli looked down and saw the green earth spinning far below.", "Mowgli aşağı baktı ve yeşil yeryüzünün çok aşağıda fırıl fırıl döndüğünü gördü.", "Perception verb 'saw' followed by participle 'spinning'."),
            ("The monkeys shouted and mocked the furious beasts down on the ground.", "Maymunlar çığlıklar atıyor ve yerdeki öfkeli canavarlarla alay ediyorlardı.", "Past tense 'mocked'; prepositional phrase 'on the ground'."),
            ("'Look at us!' screamed the Bandar-log, 'We are wise and wonderful!'", "'Bize bakın!' diye çığlık attı Bandar-log, 'Biz bilge ve harikayız!'", "Imperative 'look at us'; coordinate adjectives 'wise and wonderful'."),
            ("Mowgli knew that monkeys never kept a single promise or plan.", "Mowgli, maymunların tek bir sözü veya planı asla tutmadığını biliyordu.", "Noun clause 'that monkeys never kept'; quantifier 'a single'."),
            ("He felt dizzy, bruised, and terribly frightened in their rough hands.", "Onların kaba ellerinde başı dönmüş, berelenmiş ve feci halde korkmuş hissediyordu.", "Copular verb 'felt' with coordinate adjectives; adverb 'terribly'."),
            ("He needed to send a message before he vanished completely.", "Tamamen gözden kaybolmadan önce bir haber göndermesi gerekiyordu.", "Infinitive 'to send'; time clause with 'before'."),
        ]
    },
    # Page 6: The Road to the Cold Lairs (Calling Chil the Kite)
    {
        "page_number": 6,
        "title": "A Message in the Sky",
        "vocab": [
            ("kite", "çaylak kuşu"),
            ("soar", "süzülmek, yüksekten uçmak"),
            ("trail", "iz, patika"),
            ("ruins", "harabeler, kalıntılar"),
            ("track", "iz sürmek, takip etmek"),
            ("rescue", "kurtarmak"),
            ("haste", "acele, telaş"),
            ("glance", "göz atmak, bakış")
        ],
        "sentences": [
            ("High above the green jungle canopy, Chil the Kite soared gracefully.", "Yeşil orman örtüsünün çok yukarısında, Çaylak Chil zarifçe süzülüyordu.", "Prepositional phrase 'high above'; adverb 'gracefully'."),
            ("His sharp black eyes watched the forest for any sign of food.", "Keskin siyah gözleri herhangi bir yiyecek işareti bulmak için ormanı gözetliyordu.", "Preposition 'for'; noun phrase 'sign of food'."),
            ("Suddenly, a loud human cry reached his sharp ears from the leaves.", "Aniden, yaprakların arasından keskin kulaklarına gür bir insan haykırışı ulaştı.", "Adjective 'sharp'; prepositional phrase 'from the leaves'."),
            ("'We be of one blood, thou and I!' shouted Mowgli desperately.", "'Biz aynı kandanız, sen ve ben!' diye var gücüyle bağırdı Mowgli çaresizce.", "Archaic greeting 'thou and I'; adverb 'desperately'."),
            ("Chil glanced down through the sunlit branches in great surprise.", "Chil büyük bir şaşkınlıkla güneşli dalların arasından aşağıya baktı.", "Phrasal verb 'glance down'; prepositional phrase 'in great surprise'."),
            ("He saw a little human boy being dragged along by the monkeys.", "Maymunlar tarafından sürüklenip götürülen küçük bir insan çocuğu gördü.", "Passive participle construction 'being dragged along'."),
            ("'Mark my trail!' cried Mowgli as he was carried across the treetops.", "'İzimi takip et!' diye haykırdı Mowgli ağaç tepeleri boyunca taşınırken.", "Imperative 'mark my trail'; passive time clause 'as he was carried'."),
            ("'Tell Baloo and Bagheera that they are taking me to the Cold Lairs!'", "'Baloo ve Bagheera'ya beni Soğuk İnler'e götürdüklerini söyle!'", "Imperative verb 'tell' with indirect object and noun clause."),
            ("Chil the Kite dipped his wings in acknowledgment of the Master Word.", "Çaylak Chil, Efendi Sözü'nün hürmetine kanatlarını aşağı indirerek selam verdi.", "Noun phrase 'in acknowledgment of'; proper noun 'Master Word'."),
            ("'I will tell them, Little Brother,' called the great bird as he turned.", "'Onlara haber vereceğim Küçük Kardeş,' diye seslendi koca kuş geri dönerken.", "Direct speech; time clause 'as he turned'."),
            ("Far down on the dark jungle floor, Baloo and Bagheera ran helplessly.", "Aşağıda, karanlık orman zemininde Baloo ve Bagheera çaresizce koşuyordu.", "Adverbs 'far down' and 'helplessly'."),
            ("They could not leap from branch to branch like the lawless monkeys.", "Kanun tanımaz maymunlar gibi daldan dala atlayamıyorlardı.", "Modal 'could not'; prepositional phrase 'from branch to branch'."),
            ("Suddenly Chil circled low and dropped like a falling leaf before them.", "Birdenbire Chil alçaktan daireler çizdi ve önlerine düşen bir yaprak gibi süzüldü.", "Coordinated verbs 'circled' and 'dropped'; simile 'like a falling leaf'."),
            ("'Mowgli has given the Word!' whistled the kite.", "'Mowgli Söz'ü söyledi!' diye ıslık çaldı çaylak.", "Present perfect 'has given'; proper term 'the Word'."),
            ("'The Bandar-log have carried him across the river to the Cold Lairs.'", "'Bandar-log onu nehrin karşısına, Soğuk İnler'e kaçırdı.'", "Present perfect with collective subject; prepositional phrase 'to the Cold Lairs'."),
            ("Baloo groaned in despair when he heard the dreaded name.", "Baloo o korkunç ismi duyunca umutsuzlukla inledi.", "Prepositional phrase 'in despair'; time clause 'when he heard'."),
            ("The Cold Lairs was an ancient ruined city buried deep in the forest.", "Soğuk İnler, ormanın derinliklerine gömülmüş kadim bir harabe şehirdi.", "Participial phrase 'buried deep in the forest'."),
            ("'We cannot fight the whole monkey tribe alone,' said Bagheera grimly.", "'Bütün maymun kabilesiyle tek başımıza savaşamayız,' dedi Bagheera sertçe.", "Modal 'cannot fight'; adverb 'grimly'."),
            ("'There is only one creature whom the monkeys fear more than death.'", "'Maymunların ölümden bile daha çok korktuğu tek bir yaratık var.'", "Existential 'there is'; relative clause with 'whom'."),
            ("'We must go immediately to Kaa the Rock Python,' declared the panther.", "'Derhal Kaya Pitonu Kaa'ya gitmeliyiz,' dedi panter kararlılıkla.", "Modal of obligation 'must go'; adverb 'immediately'."),
        ]
    },
    # Page 7: The Battle of the Lost City (Kaa's Dance and Rescue)
    {
        "page_number": 7,
        "title": "The Ruins of the Cold Lairs",
        "vocab": [
            ("python", "piton yılanı"),
            ("marble", "mermer"),
            ("palace", "saray"),
            ("dome", "kubbe"),
            ("hiss", "tıslamak"),
            ("terrified", "dehşete düşmüş"),
            ("hypnotize", "hipnotize etmek, büyülemek"),
            ("overwhelm", "alt etmek, ezmek")
        ],
        "sentences": [
            ("Kaa the Rock Python was thirty feet of mottled, cold muscular power.", "Kaya Pitonu Kaa, alacalı ve soğuk kas gücünden oluşan otuz fitlik bir devdi.", "Measurement phrase 'thirty feet of'; compound adjective 'mottled'."),
            ("He had changed his skin recently and was very hungry for a hunt.", "Kısa süre önce derisini değiştirmişti ve avlanmaya çok açtı.", "Past perfect 'had changed'; adjective 'hungry for'."),
            ("When Bagheera explained that the monkeys insulted him, Kaa's eyes flashed.", "Bagheera maymunların kendisine hakaret ettiğini anlatınca, Kaa'nın gözleri parladı.", "Time clause with 'when'; verb 'flashed' indicates anger."),
            ("Together the three mighty hunters raced through the night toward the ruins.", "Birlikte bu üç ulu avcı, gece boyunca harabelere doğru hızla koştular.", "Subject with apposition 'the three mighty hunters'; directional phrase 'toward the ruins'."),
            ("The Cold Lairs stood silent under the cold light of the midnight moon.", "Soğuk İnler, gece yarısı ayının soğuk ışığı altında sessizce duruyordu.", "Copular verb 'stood silent'; prepositional phrase 'under the cold light'."),
            ("Broken marble palaces and crumbling temples lay half-hidden among vines.", "Kırık mermer saraylar ve çöken tapınaklar sarmaşıklar arasında yarı gizli yatıyordu.", "Participial adjectives 'broken, crumbling'; compound adjective 'half-hidden'."),
            ("Mowgli was locked inside a small summerhouse with hundreds of cobras.", "Mowgli yüzlerce kobranın bulunduğu küçük bir yazlık köşkte kilitli tutuluyordu.", "Passive voice 'was locked'; prepositional phrase 'with hundreds of cobras'."),
            ("He quickly gave the Snake's Master Word, and the cobras did not strike him.", "Hemen Yılan Efendi Sözü'nü söyledi ve kobralar ona saldırmadı.", "Coordinate clauses with 'and'; negative past 'did not strike'."),
            ("Suddenly, Bagheera bounded onto the terrace, striking left and right.", "Birdenbire Bagheera terasa fırladı, sağa sola pençe savurdu.", "Participial phrase describing action 'striking left and right'."),
            ("Hundreds of monkeys screamed in fury and swarmed over the black panther.", "Yüzlerce maymun öfkeyle çığlık atıp kara panterin üzerine üşüştü.", "Coordinate past verbs 'screamed' and 'swarmed'."),
            ("They were too numerous for one beast, and Bagheera was nearly overwhelmed.", "Tek bir canavar için çok kalabalıktılar ve Bagheera neredeyse ezilmek üzereydi.", "Structure 'too + adjective + for'; passive 'was nearly overwhelmed'."),
            ("Baloo charged up the terrace with mighty blows, roaring with thunderous fury.", "Baloo gök gürültüsünü andıran bir öfkeyle kükreyerek, kudretli darbelerle terasa daldı.", "Participial phrase 'roaring with thunderous fury'."),
            ("Then a deep, terrifying hiss silenced every creature across the courtyard.", "Sonra derin ve dehşet verici bir tıslama avludaki tüm yaratıkları susturdu.", "Adjective 'terrifying'; transitive past verb 'silenced'."),
            ("Kaa poured his enormous body over the wall like a sliding river.", "Kaa devasa gövdesini kayan bir nehir gibi duvarın üzerinden aşağı akıttı.", "Metaphor 'poured his enormous body'; simile 'like a sliding river'."),
            ("The monkey tribe froze in sheer horror at the sight of the great python.", "Maymun kabilesi, koca pitonu görmenin getirdiği katıksız dehşetle donakaldı.", "Phrasal verb 'froze in'; prepositional phrase 'at the sight of'."),
            ("Kaa broke open the wall of Mowgli's prison with one heavy blow of his head.", "Kaa kafasının tek bir ağır darbesiyle Mowgli'nin zindan duvarını kırıp açtı.", "Phrasal verb 'broke open'; instrument phrase 'with one heavy blow'."),
            ("Mowgli leaped out and embraced Baloo and Bagheera with tears of joy.", "Mowgli dışarı fırladı ve sevinç gözyaşlarıyla Baloo ile Bagheera'ya sarıldı.", "Coordinated actions 'leaped out' and 'embraced'; noun phrase 'tears of joy'."),
            ("Kaa began his mysterious, rhythmic dance under the silver moonlight.", "Kaa gümüşi ay ışığı altında gizemli ve ritmik dansına başladı.", "Adjectives 'mysterious, rhythmic'; prepositional phrase 'under silver moonlight'."),
            ("The monkeys stood like stone, helpless and spellbound by his circling coils.", "Maymunlar onun dönen kıvrımlarıyla büyülenmiş ve çaresizce taş gibi kalakaldılar.", "Simile 'like stone'; coordinate adjectives 'helpless and spellbound'."),
            ("Bagheera led Mowgli away quickly before the serpent's magic took hold.", "Yılanın büyüsü etkisini göstermeden önce Bagheera, Mowgli'yi oradan hızla uzaklaştırdı.", "Phrasal verb 'led away'; idiom 'took hold' means became effective."),
        ]
    },
    # Page 8: The Red Flower (Mowgli Goes to the Village for Fire)
    {
        "page_number": 8,
        "title": "The Terrible Red Flower",
        "vocab": [
            ("flower", "çiçek"),
            ("pot", "çömlek, kap"),
            ("ember", "köz, kor"),
            ("flame", "alev"),
            ("cunning", "kurnaz, sinsi"),
            ("village", "köy"),
            ("rebellion", "isyan, başkaldırı"),
            ("fear", "korkmak / korku")
        ],
        "sentences": [
            ("Years passed in the jungle, and Mowgli grew into a strong young hunter.", "Ormanda yıllar geçti ve Mowgli güçlü, genç bir avcıya dönüştü.", "Phrasal verb 'grew into'; noun phrase 'strong young hunter'."),
            ("His muscles were hard as iron, and he ran as swiftly as a deer.", "Kasları demir gibi sertti ve bir geyik kadar hızlı koşabiliyordu.", "Simile 'hard as iron'; comparative adverb 'as swiftly as'."),
            ("Akela was growing old and could no longer kill his buck with one leap.", "Akela yaşlanıyordu ve artık tek sıçrayışta geyiğini avlayamıyordu.", "Past continuous 'was growing'; negative time phrase 'no longer'."),
            ("Shere Khan noticed the leader's weakness and began whispering among younger wolves.", "Shere Han liderin zayıflığını fark etti ve genç kurtların arasına fısıltı yaymaya başladı.", "Coordinate predicates; gerund 'whispering'."),
            ("He gave them sweet scraps of meat and turned their hearts against Mowgli.", "Onlara tatlı et parçaları verdi ve kalplerini Mowgli'ye karşı kışkırttı.", "Phrasal verb 'turned against'; compound noun 'scraps of meat'."),
            ("Bagheera took Mowgli aside under the shadow of a giant fig tree.", "Bagheera devasa bir incir ağacının gölgesinde Mowgli'yi bir kenara çekti.", "Phrasal verb 'took aside'; prepositional phrase 'under the shadow'."),
            ("'The time has come, Little Brother,' whispered the dark panther softly.", "'Vakit geldi Küçük Kardeş,' diye fısıldadı kara panter usulca.", "Present perfect 'has come'; adverb 'softly'."),
            ("'Akela missed his kill yesterday, and tomorrow the young wolves will depose him.'", "'Akela dün avını kaçırdı ve yarın genç kurtlar onu tahttan indirecek.'", "Time words 'yesterday' and 'tomorrow'; future modal 'will depose'."),
            ("'They hate you because they cannot look you straight in the eyes.'", "'Senden nefret ediyorlar çünkü senin doğrudan gözlerinin içine bakamıyorlar.'", "Causal clause with 'because'; idiom 'look straight in the eyes'."),
            ("'There is only one thing in the world that every beast fears,' Bagheera said.", "'Dünyada her canavarın korktuğu tek bir şey vardır,' dedi Bagheera.", "Relative clause 'that every beast fears'; existential 'there is'."),
            ("'You must go down to the human village and fetch the Red Flower.'", "'İnsan köyüne inip Kırmızı Çiçek'i getirmelisin.'", "Modal 'must go'; proper metaphor 'the Red Flower' for fire."),
            ("No beast in the jungle dared to call fire by its real human name.", "Ormandaki hiçbir canavar ateşi gerçek insani adıyla anmaya cesaret edemezdi.", "Negative subject 'no beast'; verb 'dared to call'."),
            ("Mowgli hurried silently down the valley under the cover of dusk.", "Mowgli alacakaranlığın örtüsü altında vadiden aşağı sessizce aceleyle indi.", "Adverb 'silently'; prepositional phrase 'under the cover of dusk'."),
            ("He peeked through the window of a small mud hut in the village.", "Köydeki küçük bir çamur kulübenin penceresinden içeriye gizlice baktı.", "Past verb 'peeked through'; compound noun 'mud hut'."),
            ("A woman was feeding glowing red embers into a clay pot.", "Bir kadın kilden bir çömleğin içine parıldayan kırmızı korlar koyuyordu.", "Past continuous 'was feeding'; participial adjective 'glowing'."),
            ("When she walked outside to draw water, Mowgli slipped in like a shadow.", "Kadın su çekmek için dışarı çıktığında Mowgli bir gölge gibi içeri süzüldü.", "Time clause 'when she walked'; infinitive of purpose 'to draw water'."),
            ("He grasped the clay pot filled with glowing coals and dry twigs.", "İçi yanan kömürler ve kuru dallarla dolu kil çömleği kavradı.", "Past participle phrase 'filled with glowing coals'."),
            ("He blew on the embers carefully until little yellow flames danced.", "Küçük sarı alevler dans edene kadar korların üzerine dikkatlice üfledi.", "Preposition 'on'; time clause 'until little yellow flames danced'."),
            ("He carried the burning pot back toward the high hills of Seeonee.", "Ateş yanan çömleği Seeonee'nin yüksek tepelerine doğru geri taşıdı.", "Participial adjective 'burning'; directional preposition 'toward'."),
            ("He now held the master weapon that would decide his fate.", "Artık kaderini belirleyecek olan efendi silahı elinde tutuyordu.", "Relative clause 'that would decide his fate'; noun 'weapon'."),
        ]
    },
    # Page 9: Defying Shere Khan at Council Rock with Fire
    {
        "page_number": 9,
        "title": "The Master of Council Rock",
        "vocab": [
            ("blaze", "parlamak, alevlenmek"),
            ("strike", "çarpmak, vurmak"),
            ("whimper", "sızlanmak, inlemek"),
            ("traitor", "hain"),
            ("spark", "kıvılcım"),
            ("triumph", "zafer, utku"),
            ("coward", "korkak"),
            ("tear", "gözyaşı")
        ],
        "sentences": [
            ("The Council Rock was packed with snarling wolves under the moon.", "Konsey Kayası ayın altında hırlaşan kurtlarla dolup taşmıştı.", "Passive participle 'packed with'; participial adjective 'snarling'."),
            ("Akela sat beside his empty rock, battered and silent with old age.", "Akela boş kayasının yanında, yaşlılıktan yıpranmış ve sessizce oturuyordu.", "Coordinate adjectives 'battered and silent'; cause phrase 'with old age'."),
            ("Shere Khan stepped boldly into the circle, surrounded by young rebel wolves.", "Shere Han, etrafını sarmış genç isyancı kurtlarla halkanın içine cüretkarca adım attı.", "Past participle phrase 'surrounded by'; adverb 'boldly'."),
            ("'Give the man-cub to me!' shouted the tiger with greedy arrogance.", "'O insan yavrusunu bana verin!' diye bağırdı kaplan açgözlü bir küstahlıkla.", "Imperative 'give... to me'; noun phrase 'greedy arrogance'."),
            ("'He has lived too long among us, and he is a man after all.'", "'Aramızda çok uzun süre yaşadı ve nihayetinde o bir insan.'", "Present perfect 'has lived'; transitional phrase 'after all'."),
            ("Mowgli walked forward calmly, holding the clay pot behind his back.", "Mowgli elindeki kil çömleği arkasında tutarak sakin adımlarla öne doğru yürüdü.", "Participle clause 'holding the clay pot'; adverb 'calmly'."),
            ("He looked around at the wolves who had once called him brother.", "Vaktiyle kendisine kardeş diyen kurtlara şöyle bir baktı.", "Phrasal verb 'looked around at'; past perfect relative clause 'who had once called'."),
            ("'You have told me often that I am a man,' said Mowgli proudly.", "'Bana sık sık bir insan olduğumu söylediniz,' dedi Mowgli gururla.", "Present perfect 'have told'; noun clause 'that I am a man'."),
            ("'And indeed, I see that you have turned into dogs of Shere Khan.'", "'Ve gerçekten de Shere Han'ın köpeklerine dönüştüğünüzü görüyorum.'", "Phrasal verb 'turned into'; transitional adverb 'indeed'."),
            ("He thrust a dry branch into the pot, and it burst into brilliant fire.", "Çömleğin içine kuru bir dal soktu ve dal birdenbire göz alıcı bir ateşle alev aldı.", "Phrasal verb 'burst into'; adjective 'brilliant'."),
            ("The pack shrank backward in blind terror, whining at the leaping flames.", "Sürü, sıçrayan alevler karşısında inleyerek kör bir dehşet içinde geriye çekildi.", "Past verb 'shrank backward'; participle phrase 'whining at'."),
            ("Mowgli strode toward Shere Khan with the blazing brand raised high.", "Mowgli elinde havaya kaldırdığı alevli meşaleyle Shere Han'a doğru yürüdü.", "Irregular past 'strode' (stride); absolute construction 'with the blazing brand raised'."),
            ("The striped butcher cowered on his belly, whimpering like a beaten dog.", "Çizgili kasap, dövülmüş bir köpek gibi inleyerek karnının üzerine sindi.", "Simile 'like a beaten dog'; coordinate participle 'whimpering'."),
            ("'Up, dog!' cried Mowgli, striking the tiger across the whiskers with fire.", "'Kalk ayağa, seni köpek!' diye haykırdı Mowgli, bıyıklarına ateşle vurarak.", "Imperative 'up, dog!'; participial phrase 'striking the tiger'."),
            ("Sparks flew into Shere Khan's fur, and he shrieked in agony.", "Shere Han'ın kürküne kıvılcımlar saçıldı ve kaplan acı içinde çığlık attı.", "Prepositional phrase 'in agony'; past verb 'shrieked'."),
            ("'Go now, but remember that when I return, I bring your skin!' Mowgli warned.", "'Şimdi defol, ama geri döndüğümde senin postunu getireceğimi unutma!' diye uyardı Mowgli.", "Imperative 'go now'; time clause 'when I return'."),
            ("Shere Khan scrambled down the hillside into the black night.", "Shere Han karanlık gecenin içine doğru dağ yamacından aşağı apar topar kaçtı.", "Phrasal verb 'scrambled down'; directional phrase 'into the black night'."),
            ("Then Mowgli turned to Akela and promised that the old wolf would live in peace.", "Sonra Mowgli Akela'ya döndü ve yaşlı kurdun barış içinde yaşayacağına söz verdi.", "Noun clause 'that the old wolf would live'; prepositional phrase 'in peace'."),
            ("Suddenly, warm drops rolled down Mowgli's cheeks, puzzling the brave boy.", "Birdenbire, Mowgli'nin yanaklarından aşağı sıcak damlalar süzüldü ve bu cesur çocuğu şaşırttı.", "Participial phrase 'puzzling the brave boy'; subject 'warm drops'."),
            ("'Do not be ashamed, Little Brother,' whispered Bagheera, 'they are only tears.'", "'Utanma Küçük Kardeş,' diye fısıldadı Bagheera, 'onlar sadece gözyaşı.'", "Negative imperative 'do not be ashamed'; adverb 'only'."),
        ]
    },
    # Page 10: Mowgli Among the Men (Living with Messua & Grazing Buffaloes)
    {
        "page_number": 10,
        "title": "The Village of the Man-Tribe",
        "vocab": [
            ("plow", "sabanla sürmek"),
            ("buffalo", "manda, su sığırı"),
            ("herd", "sürü (büyükbaş)"),
            ("pasture", "otlak, çayır"),
            ("cloth", "kumaş, giysi"),
            ("hut", "kulübe"),
            ("adopt", "evlat edinmek"),
            ("clumsy", "hantal, sakar")
        ],
        "sentences": [
            ("Mowgli walked down the long mountain slope into the valley of cultivated fields.", "Mowgli uzun dağ yamacından aşağı inerek ekili tarlaların bulunduğu vadiye vardı.", "Adjective 'cultivated'; prepositional phrase 'into the valley'."),
            ("The human village had mud walls, thatched roofs, and loud barking dogs.", "İnsan köyünün çamur duvarları, sazdan çatıları ve havlayan gürültücü köpekleri vardı.", "Coordinate noun phrases with adjectives; participial adjective 'barking'."),
            ("The villagers gathered around him, pointing at his scars and naked chest.", "Köylüler onun yara izlerini ve çıplak göğsünü işaret ederek etrafına toplandılar.", "Participial phrase 'pointing at'; compound noun 'scars and naked chest'."),
            ("A kind woman named Messua looked into his dark eyes and gasped.", "Messua adında müşfik bir kadın onun kara gözlerinin içine baktı ve heyecanla nefesini tuttu.", "Past participle modifier 'named Messua'; coordinate past verbs."),
            ("'He has the eyes of my little boy whom the tiger stole!' she wept.", "'Kaplanın çaldığı küçük oğlumun gözlerine sahip!' diyerek ağladı.", "Relative clause 'whom the tiger stole'; present tense 'has the eyes'."),
            ("Messua took Mowgli into her warm hut and gave him sweet milk and bread.", "Messua Mowgli'yi sıcak kulübesine aldı ve ona tatlı süt ile ekmek verdi.", "Double object construction 'gave him sweet milk and bread'."),
            ("Mowgli found living inside four walls very stifling and uncomfortable.", "Mowgli dört duvar arasında yaşamayı son derece boğucu ve rahatsız edici buldu.", "Complex transitive structure 'found [gerund] [adjectives]'."),
            ("The coarse cloth they put on him felt heavy and itchy against his skin.", "Üzerine giydirdikleri kaba kumaş, tenine ağır ve kaşındırıcı geldi.", "Adjectives 'heavy and itchy'; relative clause 'they put on him'."),
            ("He could not sleep on the raised wooden bed and lay on the earthen floor.", "Yüksek ahşap yatakta uyuyamadı ve toprak zeminin üzerine yattı.", "Coordinate past verbs; compound noun 'earthen floor'."),
            ("Every evening he had to learn human words like plow, coins, and taxes.", "Her akşam saban, madeni para ve vergi gibi insani kelimeleri öğrenmek zorundaydı.", "Modal obligation 'had to learn'; preposition 'like' for examples."),
            ("He thought the villagers were foolish, noisy, and clumsy in their movements.", "Köylülerin hareketlerinde akılsız, gürültücü ve hantal olduklarını düşünüyordu.", "Noun clause 'the villagers were...'; coordinate adjectives."),
            ("To earn his food, Mowgli was put in charge of the village buffalo herd.", "Yiyeceğini hak etmek için Mowgli köyün manda sürüsünün başına verildi.", "Infinitive of purpose 'to earn'; idiom 'put in charge of'."),
            ("Rama, the great leader bull, obeyed Mowgli's commands without question.", "Büyük lider boğa Rama, Mowgli'nin emirlerine sorgusuz sualsiz itaat ediyordu.", "Prepositional phrase 'without question'; proper noun 'Rama'."),
            ("Every morning Mowgli drove the herd out to the wide grassy marshes.", "Her sabah Mowgli sürüyü otlu geniş bataklıklara doğru otlatmaya götürürdü.", "Phrasal verb 'drove out to'; adjective 'grassy'."),
            ("The heavy buffaloes wallowed contentedly in the cool black mud.", "Ağır mandalar serin kara çamurun içinde memnuniyetle yuvarlandılar.", "Adverb 'contentedly'; past verb 'wallowed'."),
            ("Mowgli lay on the back of a huge bull and watched the distant jungle.", "Mowgli dev bir boğanın sırtına uzanıp uzaktaki ormanı izledi.", "Coordinate past verbs; adjective 'distant'."),
            ("He missed the freedom of running with his brothers under the moon.", "Ay ışığı altında kardeşleriyle koşmanın özgürlüğünü çok özlüyordu.", "Gerund object 'running with his brothers'; noun 'freedom'."),
            ("The village boys mocked him because he did not understand their games.", "Köyün çocukları oyunlarını anlamadığı için onunla alay ettiler.", "Causal clause with 'because'; negative past 'did not understand'."),
            ("Mowgli held his temper because he remembered the wise teachings of Baloo.", "Mowgli öfkesine hakim oldu çünkü Baloo'nun bilgece öğretilerini hatırlıyordu.", "Idiom 'held his temper'; possessive 'teachings of Baloo'."),
            ("A gray head appeared at the edge of the tall sugarcane field.", "Uzun şeker kamışı tarlasının kenarında gri bir baş belirdi.", "Prepositional phrase 'at the edge of'; compound noun 'sugarcane field'."),
        ]
    },
    # Page 11: Gray Brother's Warning (The Tiger's Return)
    {
        "page_number": 11,
        "title": "A Messenger in the Cane Field",
        "vocab": [
            ("sugarcane", "şeker kamışı"),
            ("ravine", "derin vadi, geçit"),
            ("revenge", "intikam"),
            ("ambush", "tuzak kurmak / pusu"),
            ("scent", "koku, iz"),
            ("divide", "bölmek, ayırmak"),
            ("cunning", "kurnazlık, hilekarlık"),
            ("trap", "kapana kıstırmak / kapan")
        ],
        "sentences": [
            ("It was Gray Brother, the eldest of Mother Wolf's cubs.", "Bu, Anne Kurt'un yavrularının en büyüğü olan Gri Kardeş'ti.", "Superlative 'eldest'; appositive noun phrase."),
            ("He pressed his cool nose into the palm of Mowgli's hand.", "Soğuk burnunu Mowgli'nin avucunun içine bastırdı.", "Phrasal action 'pressed into'; possessive 'Mowgli's hand'."),
            ("'Shere Khan has returned to the district,' whispered the gray wolf.", "'Shere Han bu bölgeye geri döndü,' diye fısıldadı gri kurt.", "Present perfect 'has returned'; noun 'district'."),
            ("'His burns have healed, and he has sworn to take your life.'", "'Yanıkları iyileşti ve senin canını almaya yemin etti.'", "Present perfect coordinate verbs 'have healed' and 'has sworn'."),
            ("'Where is the striped butcher hiding now?' asked Mowgli sternly.", "'Çizgili kasap şimdi nerede saklanıyor?' diye sordu Mowgli sert bir ifadeyle.", "Present continuous question; adverb 'sternly'."),
            ("'He waits at the great ravine of the Waingunga river,' replied Gray Brother.", "'Waingunga nehrinin büyük geçidinde bekliyor,' diye yanıtladı Gri Kardeş.", "Present tense; prepositional phrase 'at the great ravine'."),
            ("'He ate a full meal this morning and is sleeping heavily in the shade.'", "'Bu sabah karnını tıka basa doyurdu ve gölgede derin uykuda yatıyor.'", "Past + present continuous; adverb 'heavily'."),
            ("Mowgli's eyes sparkled with fierce, calculating determination.", "Mowgli'nin gözleri yırtıcı ve hesaplı bir kararlılıkla parıldadı.", "Coordinate adjectives 'fierce, calculating'; preposition 'with'."),
            ("'A full belly makes a lazy hunter,' said Mowgli with a grim smile.", "'Tıkabasa dolu bir karın, avcıyı tembel yapar,' dedi Mowgli sert bir tebessümle.", "Proverbial statement; noun phrase 'lazy hunter'."),
            ("'We can trap him inside the deep ravine between two steep walls.'", "'İki dik duvar arasındaki derin geçitte onu kapana kıstırabiliriz.'", "Modal 'can trap'; prepositional phrase 'between two steep walls'."),
            ("'How can a single man and one wolf fight a tiger?' asked Gray Brother.", "'Tek bir insan ve bir kurt bir kaplanla nasıl savaşabilir?' diye sordu Gri Kardeş.", "Modal question; singular subjects."),
            ("'We will not fight with our claws, but with the herd,' Mowgli explained.", "'Pençelerimizle değil, sürüyle savaşacağız,' diye açıkladı Mowgli.", "Negative contrast 'not with... but with'; future modal 'will'."),
            ("Akela suddenly stepped out from the bushes to join his brothers.", "Akela kardeşlerine katılmak için aniden çalıların arasından çıkageldi.", "Infinitive of purpose 'to join'; phrasal verb 'stepped out'."),
            ("The old wolf was ready to follow Mowgli's leadership until the end.", "Yaşlı kurt sonuna kadar Mowgli'nin liderliğini takip etmeye hazırdı.", "Adjective + infinitive 'ready to follow'; prepositional phrase 'until the end'."),
            ("'We must divide the herd into two groups,' Mowgli instructed.", "'Sürüyü iki gruba ayırmalıyız,' diye talimat verdi Mowgli.", "Modal of obligation 'must divide'; preposition 'into two groups'."),
            ("'The cows and calves must go to the upper end of the gorge.'", "'İnekler ve buzağılar boğazın yukarı ucuna gitmeli.'", "Compound subject; modal 'must go'."),
            ("'The heavy bulls under Rama will charge down from the lower entrance.'", "'Rama'nın idaresindeki ağır boğalar ise aşağı girişten hücuma geçecek.'", "Future modal 'will charge'; prepositional phrase 'under Rama'."),
            ("The two wolves dashed through the marsh to guide the cows quietly.", "İki kurt inekleri sessizce yönlendirmek için bataklıktan hızla koştular.", "Infinitive of purpose 'to guide'; adverb 'quietly'."),
            ("Mowgli mounted Rama's broad back and whispered into the bull's ear.", "Mowgli Rama'nın geniş sırtına bindi ve boğanın kulağına fısıldadı.", "Coordinated actions 'mounted' and 'whispered'."),
            ("The great trap was set for the lord of the striped skin.", "Çizgili postun efendisi için büyük tuzak kurulmuştu.", "Passive voice 'was set'; title phrase 'lord of the striped skin'."),
        ]
    },
    # Page 12: The Buffalo Charge in the Ravine (Defeat of Shere Khan)
    {
        "page_number": 12,
        "title": "The Thunder of the Herd",
        "vocab": [
            ("gorge", "dar boğaz, kanyon"),
            ("stampede", "izdiham, dehşetle kaçış/hücum"),
            ("hoof", "tutanak, toynak"),
            ("crush", "ezmek, un ufak etmek"),
            ("echo", "yankılanmak"),
            ("avenge", "öcünü almak"),
            ("steep", "sarp, dik"),
            ("triumph", "büyük zafer")
        ],
        "sentences": [
            ("The gorge was narrow, with steep rock walls rising straight up.", "Boğaz dardı ve sarp kaya duvarları dimdik yukarı yükseliyordu.", "Absolute clause 'with steep rock walls rising'; adjective 'narrow'."),
            ("At the bottom of the ravine, Shere Khan woke to a low rumbling sound.", "Geçidin dibinde Shere Han derinden gelen bir uğultu sesine uyandı.", "Phrasal verb 'woke to'; compound noun 'low rumbling sound'."),
            ("The ground under his heavy paws began to tremble with increasing violence.", "Ağır patilerinin altındaki zemin giderek artan bir şiddetle titremeye başladı.", "Verb followed by infinitive 'began to tremble'; prepositional phrase 'with increasing violence'."),
            ("From the upper entrance came a panicked stampede of wild cows.", "Yukarı girişten çılgınca kaçışan vahşi ineklerin izdihamı geldi.", "Inverted locative sentence; adjective 'panicked'."),
            ("The tiger turned to flee down the gorge toward the open plain.", "Kaplan açık ovaya doğru boğazdan aşağı kaçmak için döndü.", "Infinitive of purpose 'to flee'; directional preposition 'toward'."),
            ("But at the lower entrance stood Mowgli on the back of Rama.", "Fakat aşağı girişte Rama'nın sırtında Mowgli duruyordu.", "Inverted sentence; prepositional phrase 'at the lower entrance'."),
            ("Beside him were rows of massive bulls with lowered, sharp horns.", "Onun yanında aşağı indirilmiş keskin boynuzlarıyla sıra sıra devasa boğalar vardı.", "Inverted structure; participial adjective 'lowered'."),
            ("'Charge, Rama!' shouted Mowgli with all the power of his voice.", "'Hücum, Rama!' diye var gücüyle haykırdı Mowgli.", "Imperative 'charge'; prepositional phrase 'with all the power'."),
            ("The bulls plunged forward in an unstoppable wave of muscle and horn.", "Boğalar durdurulamaz bir kas ve boynuz dalgası halinde ileri atıldılar.", "Phrasal verb 'plunged forward'; prepositional phrase 'in an unstoppable wave'."),
            ("Shere Khan was trapped between the two charging herds.", "Shere Han hücuma kalkan iki sürünün arasında kapana kısıldı.", "Passive voice 'was trapped'; preposition 'between'."),
            ("He tried desperately to scramble up the slippery clay walls of the ravine.", "Geçidin kaygan killi duvarlarına tırmanmak için çaresizce çabaladı.", "Infinitive 'to scramble up'; coordinate adjectives 'slippery clay'."),
            ("His heavy belly dragged him down, and his claws found no grip.", "Ağır karnı onu aşağı çekiyordu ve pençeleri tutunacak hiçbir yer bulamadı.", "Coordinate past clauses; noun phrase 'no grip'."),
            ("The thundering hooves struck him like a storm of iron hammers.", "Gürleyen toynaklar demir çekiç fırtınası gibi ona çarptı.", "Simile 'like a storm of iron hammers'; participial adjective 'thundering'."),
            ("Rama smashed into the tiger and trampled him beneath his heavy feet.", "Rama kaplana var gücüyle çarptı ve onu ağır ayaklarının altında çiğnedi.", "Coordinated actions 'smashed into' and 'trampled'; preposition 'beneath'."),
            ("The bulls roared in fury as they swept over the fallen predator.", "Boğalar yere düşen yırtıcının üzerinden geçerken öfkeyle böğürdüler.", "Time clause with 'as'; participial adjective 'fallen predator'."),
            ("When the dust finally cleared, the striped terror was motionless on the ground.", "Toz duman nihayet dağıldığında, çizgili dehşet yerde hareketsiz yatıyordu.", "Time clause 'when the dust cleared'; adjective 'motionless'."),
            ("Shere Khan had met his end, not by human steel, but by jungle justice.", "Shere Han sonunu insan çeliğiyle değil, orman adaletiyle bulmuştu.", "Past perfect 'had met'; negative contrast 'not by... but by'."),
            ("Mowgli leaped down from Rama's back with his sharp hunting knife.", "Mowgli keskin av bıçağıyla Rama'nın sırtından aşağı atladı.", "Phrasal verb 'leaped down from'; prepositional phrase 'with his sharp knife'."),
            ("'I made a promise to the Free Pack,' said Mowgli to the listening wind.", "'Özgür Sürü'ye bir söz vermiştim,' dedi Mowgli dinleyen rüzgara.", "Past tense 'made a promise'; participial adjective 'listening'."),
            ("He began stripping the great striped hide to bring back to Council Rock.", "Konsey Kayası'na geri götürmek üzere koca çizgili postu yüzmeye başladı.", "Gerund object 'stripping'; infinitive of purpose 'to bring back'."),
        ]
    },
    # Page 13: Mowgli the Hunter on Council Rock (Laying the Tiger Skin)
    {
        "page_number": 13,
        "title": "The Skin on the Council Rock",
        "vocab": [
            ("hide", "post, hayvan derisi"),
            ("spread", "yaymak, sermek"),
            ("peg", "kazıkla tutturmak / kazık"),
            ("howl", "ulumak / uluma"),
            ("sorcerer", "büyücü, efsuncu"),
            ("exile", "sürgün etmek / sürgün"),
            ("howl", "ulumak"),
            ("loyal", "sadık, vefalı")
        ],
        "sentences": [
            ("A foolish village hunter named Buldeo arrived and tried to claim the skin.", "Buldeo adında aptal bir köy avcısı çıkageldi ve post üzerinde hak iddia etmeye kalkıştı.", "Coordinate past verbs 'arrived and tried'; infinitive 'to claim'."),
            ("Gray Brother pinned the frightened old hunter to the ground with one growl.", "Gri Kardeş tek bir homurtuyla o korkmuş yaşlı avcıyı yere serdi.", "Phrasal verb 'pinned to'; prepositional phrase 'with one growl'."),
            ("Buldeo ran screaming back to the village, shouting that Mowgli was a sorcerer.", "Buldeo Mowgli'nin bir büyücü olduğunu haykırarak çığlıklar içinde köye geri kaçtı.", "Participle clause 'shouting that...'; noun 'sorcerer'."),
            ("When Mowgli returned to the village, stones flew through the air at him.", "Mowgli köye döndüğünde, havada ona doğru taşlar uçuştu.", "Time clause; prepositional phrase 'through the air at him'."),
            ("'Sorcerer! Wolf-demon!' screamed the superstitious villagers in fear.", "'Büyücü! Kurt-iblis!' diye haykırdı batıl inançlı köylüler korku içinde.", "Vocative epithets; adjective 'superstitious'."),
            ("Only Messua wept and cried, 'My son! My son! Forgive their foolishness!'", "Yalnızca Messua ağlayarak seslendi: 'Oğlum! Oğlum! Onların aptallığını bağışla!'", "Adverb 'only'; imperative 'forgive their foolishness'."),
            ("Mowgli turned his back on the village without throwing a single stone.", "Mowgli tek bir taş bile atmadan köye sırtını döndü.", "Idiom 'turned his back on'; preposition 'without' + gerund."),
            ("'Men are as fickle and ungrateful as the monkeys,' thought the boy.", "'İnsanlar da maymunlar kadar dönek ve nankör,' diye düşündü çocuk.", "Comparative equality 'as fickle and ungrateful as'."),
            ("He carried the heavy tiger hide up the mountain into the deep jungle.", "Ağır kaplan postunu dağın yukarısına, ormanın derinliklerine doğru taşıdı.", "Directional phrases 'up the mountain into'."),
            ("Night had fallen when he finally reached the high Council Rock.", "Yüksek Konsey Kayası'na nihayet ulaştığında gece çökmüştü.", "Past perfect 'had fallen'; time clause with 'reached'."),
            ("Akela, Bagheera, and Baloo were waiting among the silent wolves.", "Akela, Bagheera ve Baloo sessiz kurtların arasında bekliyorlardı.", "Past continuous 'were waiting'; preposition 'among'."),
            ("Mowgli pegged the enormous striped hide across the flat council boulder.", "Mowgli devasa çizgili postu düz konsey kayasının üzerine kazıklarla gerdi.", "Transitive past verb 'pegged'; preposition 'across'."),
            ("Akela climbed up and lay across the dead tiger's head.", "Akela yukarı tırmandı ve ölü kaplanın kafasının üzerine uzandı.", "Coordinate past verbs 'climbed and lay'."),
            ("The old wolf lifted his muzzle to the stars and let out the hunting howl.", "Yaşlı kurt burnunu yıldızlara doğru kaldırdı ve av ulumasını koyuverdi.", "Coordinate clauses; noun phrase 'hunting howl'."),
            ("Wolf after wolf joined the chorus until the hills shook with music.", "Tepeler bu müzikle sarsılana kadar kurt üstüne kurt koroya katıldı.", "Repetitive subject 'wolf after wolf'; time clause with 'until'."),
            ("The pack begged Mowgli and Akela to lead them once again.", "Sürü, Mowgli ve Akela'ya kendilerini bir kez daha yönetmeleri için yalvardı.", "Verb + object + infinitive 'begged them to lead'."),
            ("'No,' answered Mowgli softly, 'I have been hunted by men and by wolves.'", "'Hayır,' diye yanıtladı Mowgli usulca, 'ben hem insanlar hem de kurtlar tarafından avlandım.'", "Present perfect passive 'have been hunted by'."),
            ("'From now on, I will hunt alone in the jungle with my four wolf brothers.'", "'Bundan böyle, ormanda dört kurt kardeşimle birlikte tek başıma avlanacağım.'", "Time phrase 'from now on'; modal 'will hunt alone'."),
            ("Bagheera stepped forward and rubbed his glossy cheek against Mowgli's leg.", "Bagheera öne adım attı ve parlak yanağını Mowgli'nin bacağına sürttü.", "Coordinate past verbs; adjective 'glossy'."),
            ("The boy had proven himself master of the jungle and lord of the beasts.", "Çocuk kendisinin ormanın efendisi ve canavarların hükümdarı olduğunu kanıtlamıştı.", "Past perfect 'had proven'; titles in apposition."),
        ]
    },
    # Page 14: The Spring Running (The Jungle Calls Mowgli to Grow)
    {
        "page_number": 14,
        "title": "The Time of New Leaves",
        "vocab": [
            ("spring", "ilkbahar"),
            ("blossom", "çiçek açmak / çiçek"),
            ("restless", "huzursuz, yerinde duramayan"),
            ("yearn", "hasret çekmek, arzulamak"),
            ("scent", "koku"),
            ("whisper", "fısıltı"),
            ("breeze", "tatlı rüzgar, esinti"),
            ("change", "değişim, değişmek")
        ],
        "sentences": [
            ("Years drifted by, and Mowgli grew into a tall, broad-shouldered young man.", "Yıllar akıp geçti ve Mowgli uzun boylu, geniş omuzlu genç bir adama dönüştü.", "Phrasal verb 'drifted by'; compound adjective 'broad-shouldered'."),
            ("He was swifter than any deer and stronger than any beast save the elephant.", "Filden başka her canavardan daha güçlü ve her geyikten daha hızlıydı.", "Comparative adjectives; archaic preposition 'save' meaning except."),
            ("Then came the season of the Spring Running, when all the jungle woke.", "Sonra bütün ormanın uyandığı Bahar Koşusu mevsimi geldi çattı.", "Inverted structure; relative time clause 'when all the jungle woke'."),
            ("The red flowers of the dhak tree blossomed like sparks in the green sea.", "Dhak ağacının kırmızı çiçekleri yeşil denizde birer kıvılcım gibi açtı.", "Simile 'like sparks in the green sea'; past verb 'blossomed'."),
            ("The smell of damp earth and new grass filled the warm night breeze.", "Nemli toprağın ve taze çimenin kokusu ılık gece esintisini doldurdu.", "Compound subject; past verb 'filled'."),
            ("All the animals were singing, calling to their mates in the shadows.", "Bütün hayvanlar şarkı söylüyor, gölgelerin içindeki eşlerine sesleniyordu.", "Past continuous; participle phrase 'calling to their mates'."),
            ("Mowgli felt a strange, restless sorrow inside his young heart.", "Mowgli genç yüreğinin içinde garip, huzursuz bir keder hissetti.", "Copular verb 'felt'; coordinate adjectives 'strange, restless'."),
            ("He had no desire to hunt, and the meat tasted tasteless to him.", "İçinde avlanmaya dair hiçbir istek yoktu ve et ona tatsız geliyordu.", "Noun phrase 'no desire to hunt'; copular verb 'tasted'."),
            ("He ran through the jungle all night, but he could not run away from his mood.", "Bütün gece ormanın içinde koştu ama ruh halinden bir türlü kaçamadı.", "Phrasal verb 'run away from'; noun 'mood'."),
            ("He found Baloo resting under a flowering vine, looking old and frail.", "Baloo'yu çiçekli bir sarmaşığın altında dinlenirken, yaşlı ve bitkin halde buldu.", "Perception verb + participle; coordinate adjectives 'old and frail'."),
            ("'What is the matter with me, Baloo?' cried Mowgli in deep distress.", "'Bana ne oluyor Baloo?' diye haykırdı Mowgli derin bir sıkıntı içinde.", "Idiomatic question 'what is the matter with me'; prepositional phrase 'in deep distress'."),
            ("'The Time of New Leaves has arrived, Little Brother,' said the old bear.", "'Taze Yapraklar Mevsimi geldi çattı Küçük Kardeş,' dedi yaşlı ayı.", "Present perfect 'has arrived'; title 'Time of New Leaves'."),
            ("'The jungle is changing, and you are no longer a boy.'", "'Orman değişiyor ve sen artık bir çocuk değilsin.'", "Present continuous coordinate with negative adverb 'no longer'."),
            ("Bagheera bounded silently out of the ferns and sat beside the youth.", "Bagheera eğrelti otlarının arasından sessizce sıçrayıp gencin yanına oturdu.", "Adverb 'silently'; noun 'youth' meaning young man."),
            ("'A man goes to man at the last,' purred the black panther tenderly.", "'İnsan sonunda yine insana gider,' diye usulca mırıldandı kara panter şefkatle.", "Idiomatic expression 'at the last'; adverb 'tenderly'."),
            ("'Though we love you more than our own kin, your place is among men.'", "'Seni kendi soyumuzdan daha çok sevsek de, senin yerin insanların arasıdır.'", "Concession clause with 'though'; comparative 'more than'."),
            ("Mowgli looked down at his brown human hands and sighed deeply.", "Mowgli esmer insan ellerine baktı ve derin bir iç çekti.", "Directional phrase 'looked down at'; adverb 'deeply'."),
            ("He remembered Messua's gentle voice and her warm mud hut in the valley.", "Messua'nın nazik sesini ve vadideki sıcak çamur kulübesini hatırladı.", "Coordinated objects with adjectives; noun 'valley'."),
            ("The wild green forest was his home, but a new world was calling him.", "Vahşi yeşil orman onun eviydi ama yeni bir dünya ona sesleniyordu.", "Coordinate clauses with 'but'; past continuous 'was calling'."),
            ("Tears fell once more, not from weakness, but from the pain of parting.", "Gözyaşları bir kez daha döküldü; güçsüzlükten değil, ayrılığın acısından.", "Negative contrast 'not from... but from'; noun 'parting'."),
        ]
    },
    # Page 15: Farewell to the Free People (Returning to the World of Men)
    {
        "page_number": 15,
        "title": "The Master's Farewell",
        "vocab": [
            ("farewell", "veda, elveda"),
            ("boundary", "sınır"),
            ("embrace", "kucaklamak, sarılmak"),
            ("unbroken", "bozulmamış, kırılmamış"),
            ("gratitude", "şükran, minnet"),
            ("honor", "onur, şeref"),
            ("threshold", "eşik"),
            ("brotherhood", "kardeşlik")
        ],
        "sentences": [
            ("At sunrise, Mowgli climbed the Council Rock for the very last time.", "Gün doğumunda Mowgli, Konsey Kayası'na son kez tırmandı.", "Time phrase 'at sunrise'; emphatic modifier 'for the very last time'."),
            ("The Free Pack gathered below in silent ranks, heads held low.", "Özgür Sürü, başları eğik halde aşağıda sessiz saflar halinde toplandı.", "Absolute participle construction 'heads held low'; noun 'ranks'."),
            ("Father Wolf, Mother Wolf, Baloo, and Bagheera stood close around him.", "Baba Kurt, Anne Kurt, Baloo ve Bagheera etrafında dimdik durdular.", "Multiple subjects; adverbial modifier 'close around him'."),
            ("'Listen, O Free People!' spoke Mowgli with clear and steady dignity.", "'Dinleyin, ey Özgür Halk!' diye konuştu Mowgli berrak ve vakur bir asaletle.", "Archaic vocative 'O Free People!'; coordinate adjectives 'clear and steady'."),
            ("'I return to my own people, but my heart remains in this green realm.'", "'Kendi halkıma dönüyorum ama kalbim bu yeşil diyarda kalıyor.'", "Present simple coordinate clauses; noun 'realm'."),
            ("'May the jungle ever give you good hunting and cool waters.'", "'Orman size daima bereketli avlar ve serin sular bahşetsin.'", "Optative modal 'may the jungle ever give'."),
            ("Mother Wolf laid her gray muzzle against Mowgli's bare feet.", "Anne Kurt gri burnunu Mowgli'nin çıplak ayaklarına dayadı.", "Past verb 'laid'; preposition 'against'."),
            ("'My little frog, you have paid every debt to the pack ten times over,' she whispered.", "'Benim minik kurbağam, sürüye olan her borcunu katbekat ödedin,' diye fısıldadı.", "Vocative nickname 'my little frog'; present perfect 'have paid'."),
            ("Baloo embraced him with his great furry arms, unable to hold back his sorrow.", "Baloo kederini tutamayarak devasa tüylü kollarıyla ona sarıldı.", "Participial clause of result 'unable to hold back'."),
            ("'Remember the Law, Little Brother, and walk always with honor,' said the bear.", "'Kanun'u hatırla Küçük Kardeş ve daima onurunla yürü,' dedi ayı.", "Imperative coordinates 'remember' and 'walk'; prepositional phrase 'with honor'."),
            ("Bagheera bounded to a high rock and raised his deep voice to the sky.", "Bagheera yüksek bir kayaya sıçradı ve gür sesini gökyüzüne doğru yükseltti.", "Coordinate past verbs 'bounded and raised'."),
            ("'The jungle is free to thee whenever thou returnest!' cried the panther.", "'Ne zaman dönersen dön, bu orman sana ardına kadar açıktır!' diye haykırdı panter.", "Poetic/archaic grammar 'to thee whenever thou returnest'."),
            ("The four young wolves stepped to Mowgli's side with bright, faithful eyes.", "Dört genç kurt parlak ve sadık gözlerle Mowgli'nin yanı başına geçti.", "Prepositional phrase 'to Mowgli's side'; coordinate adjectives 'bright, faithful'."),
            ("'We will walk with you to the edge of the cultivated fields,' said Gray Brother.", "'Ekili tarlaların sınırına kadar seninle birlikte yürüyeceğiz,' dedi Gri Kardeş.", "Future modal 'will walk'; noun phrase 'edge of the cultivated fields'."),
            ("Together the five brothers walked down the long, sun-drenched jungle trail.", "Beş kardeş birlikte güneşle yıkanmış uzun orman patikasından aşağı yürüdüler.", "Adjective 'sun-drenched'; compound noun 'jungle trail'."),
            ("The morning wind carried the sweet scents of wild jasmine and damp pine.", "Sabah rüzgarı yaban yasemini ve nemli çamın tatlı kokularını taşıyordu.", "Compound subjects and objects; adjective 'sweet'."),
            ("At the fence of the village, Mowgli stopped and turned for one final look.", "Köyün çitinde Mowgli durdu ve son bir kez bakmak için geriye döndü.", "Prepositional phrase 'at the fence'; infinitive of purpose 'for one final look'."),
            ("The four wolves sat in a row upon the green ridge, watching him proudly.", "Dört kurt yeşil sırtın üzerinde yan yana oturmuş, onu gururla izliyordu.", "Participial phrase 'watching him proudly'; preposition 'upon'."),
            ("Mowgli stepped across the threshold into the village toward Messua's open door.", "Mowgli eşikten geçerek Messua'nın açık kapısına doğru köye adım attı.", "Prepositional phrases 'across the threshold' and 'toward open door'."),
            ("He was a man among men now, but forever Mowgli, child of the Free People.", "Artık insanlar arasında bir insandı ama ebediyen Özgür Halk'ın çocuğu Mowgli olarak kalacaktı.", "Contrasting coordinate clause; eternal epithet 'child of the Free People'.")
        ]
    }
]

TR_TITLES = [
    "Kurt Mağarasında Bir İnsan Yavrusu",
    "Kaplan ve Anne Kurt",
    "Özgür Sürünün Hükmü",
    "Yeşil Yabanın Dersleri",
    "Kanunsuz Maymun Halkı",
    "Gökyüzündeki Mesaj",
    "Soğuk İnler Harabeleri",
    "Korkunç Kırmızı Çiçek",
    "Konsey Kayası'nın Efendisi",
    "İnsan Kabilesinin Köyü",
    "Kamışlıktaki Ulak",
    "Sürünün Gürültüsü",
    "Konsey Kayası'ndaki Post",
    "Taze Yapraklar Mevsimi",
    "Efendinin Vedası"
]

def generate_data_file():
    data_path = os.path.join(os.path.dirname(__file__), "book_14_data.py")
    
    # Verification
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
        f.write('"""\nBook 14: The Jungle Book: Mowgli of the Free People (Rudyard Kipling)\n')
        f.write('Level 1 Graded Reader — 15 Pages x 20 Sentences = 300 Sentences.\n"""\n\n')
        f.write('BOOK_TITLE = "The Jungle Book: Mowgli of the Free People (15 Sayfa / 300 Cümle / Graded Reader)"\n')
        f.write('AUTHOR = "Rudyard Kipling"\n\n')
        f.write(f"PAGES_DATA = {pprint.pformat(pages_data, indent=4, width=120)}\n")
        
    print(f"Successfully wrote {data_path}")

if __name__ == "__main__":
    generate_data_file()

