# -*- coding: utf-8 -*-
"""
Generator script for Book 25: "The Time Machine" by H. G. Wells.
15 Pages x 20 Sentences = Exactly 300 Sentences (Continuous IDs 1 to 300).
8 Vocabulary Focus items per page = Exactly 120 Target Vocabulary Items.
CEFR Level: A2-B1 Graded Reader Edition.
"""

import os

pages_data = [
    # Page 1 (Sentences 1-20)
    {
        "page_no": 1,
        "title": "The Fourth Dimension and the Dinner Guests",
        "tr_title": "Dördüncü Boyut ve Akşam Yemeği Konukları",
        "vocab_focus": [
            ("dimension", "boyut"),
            ("geometry", "geometri"),
            ("duration", "süre, zaman aralığı"),
            ("scientific", "bilimsel"),
            ("hearth", "şömine ocağı"),
            ("skeptical", "şüpheci, kuşkucu"),
            ("investigate", "araştırmak, incelemek"),
            ("philosophy", "felsefe")
        ],
        "sentences": [
            {
                "id": 1,
                "text": "The Time Traveller was explaining a strange and subtle matter to us in his warm sitting room.",
                "translation": "Zaman Gezgini, sıcak oturma odasında bize tuhaf ve ince bir konuyu açıklıyordu.",
                "notes": "subtle: ince, derin; sitting room: oturma odası"
            },
            {
                "id": 2,
                "text": "His pale grey eyes shone and twinkled, and his usually pale face was flushed and animated.",
                "translation": "Soluk gri gözleri parıldıyor, genellikle solgun olan yüzü heyecanla kızarmış görünüyordu.",
                "notes": "twinkle: parıldamak; animated: heyecanlı, canlı"
            },
            {
                "id": 3,
                "text": "The fire burned brightly, and the soft light of the lamps fell upon our curious faces.",
                "translation": "Ateş neşeyle yanıyor ve lambaların yumuşak ışığı meraklı yüzlerimize vuruyordu.",
                "notes": "burn brightly: ışıl ışıl yanmak; curious: meraklı"
            },
            {
                "id": 4,
                "text": "He held a slender piece of metal in his hand and pointed to a diagram on the desk.",
                "translation": "Elinde ince bir metal parçası tutuyor ve masanın üzerindeki bir şemayı işaret ediyordu.",
                "notes": "slender: ince; diagram: şema, çizim"
            },
            {
                "id": 5,
                "text": "\"You must follow me carefully,\" he said in a calm and deliberate voice.",
                "translation": "\"Beni dikkatle takip etmelisiniz,\" dedi sakin ve kendinden emin bir sesle.",
                "notes": "deliberate voice: kararlı, sakin ses"
            },
            {
                "id": 6,
                "text": "\"Any real body must have extension in four directions: Length, Breadth, Thickness, and Duration.\"",
                "translation": "\"Her gerçek cisim dört yönde uzantıya sahip olmalıdır: Boy, En, Derinlik ve Süre.\"",
                "notes": "extension: uzantı; breadth: en, genişlik; duration: süre"
            },
            {
                "id": 7,
                "text": "We sat comfortably in our armchairs and listened to his remarkable scientific theories.",
                "translation": "Koltuklarımızda rahatça oturuyor ve onun olağanüstü bilimsel teorilerini dinliyorduk.",
                "notes": "armchair: koltuk; remarkable: olağanüstü"
            },
            {
                "id": 8,
                "text": "The Medical Man and the Provincial Mayor looked at each other with quiet amusement.",
                "translation": "Hekim ile Taşra Belediye Başkanı sessiz bir tebessümle birbirlerine baktılar.",
                "notes": "amusement: tebessüm, eğlenme hali"
            },
            {
                "id": 9,
                "text": "\"There are really four dimensions, three which we call the three planes of Space, and a fourth, Time.\"",
                "translation": "\"Gerçekte dört boyut vardır; üçüne Uzay düzlemleri deriz, dördüncüsü ise Zaman'dır.\"",
                "notes": "planes of Space: uzay düzlemleri; fourth dimension: dördüncü boyut"
            },
            {
                "id": 10,
                "text": "The Time Traveller paused to observe whether we understood his fundamental proposition.",
                "translation": "Zaman Gezgini, temel tezini anlayıp anlamadığımızı gözlemlemek için durakladı.",
                "notes": "proposition: önerme, iddia; observe: gözlemlemek"
            },
            {
                "id": 11,
                "text": "\"Can a cube that does not last for any length of time have a real existence?\" he asked.",
                "translation": "\"Herhangi bir süre boyunca varlığını sürdürmeyen bir küpün gerçek bir varlığı olabilir mi?\" diye sordu.",
                "notes": "last: sürmek, devam etmek; real existence: gerçek varlık"
            },
            {
                "id": 12,
                "text": "Filby, an argumentative man with red hair, shook his head in disagreement.",
                "translation": "Kızıl saçlı, tartışmacı bir adam olan Filby, katılmadığını belirterek başını salladı.",
                "notes": "argumentative: tartışmacı; disagreement: anlaşmazlık"
            },
            {
                "id": 13,
                "text": "\"Clearly,\" the Time Traveller continued, \"any physical object must endure through time.\"",
                "translation": "\"Açıkçası,\" diye devam etti Zaman Gezgini, \"herhangi bir fiziksel nesne zaman boyunca varlığını sürdürmelidir.\"",
                "notes": "endure: devam etmek, sürmek; physical object: fiziksel nesne"
            },
            {
                "id": 14,
                "text": "He explained that human consciousness moves along Time from the cradle to the grave.",
                "translation": "İnsan bilincinin beşikten mezara kadar Zaman boyunca ilerlediğini açıkladı.",
                "notes": "consciousness: bilinç; cradle to the grave: beşikten mezara"
            },
            {
                "id": 15,
                "text": "\"We cannot move about in Time as we do in Space, or at least people think so.\"",
                "translation": "\"Uzayda hareket ettiğimiz gibi Zamanda serbestçe hareket edemeyiz ya da en azından insanlar öyle sanır.\"",
                "notes": "move about: serbestçe dolaşmak; at least: en azından"
            },
            {
                "id": 16,
                "text": "The Very Young Man smiled skeptically and puffed on his cigar.",
                "translation": "Çok Genç Adam kuşkulu bir gülümsemeyle purosunu tüttürdü.",
                "notes": "skeptically: kuşkucu şekilde; puff: duman üflemek"
            },
            {
                "id": 17,
                "text": "\"That is the germ of my great discovery,\" said our host with growing enthusiasm.",
                "translation": "\"İşte bu, büyük keşfimin tohumudur,\" dedi ev sahibimiz artan bir coşkuyla.",
                "notes": "germ: tohum, öz; enthusiasm: coşku"
            },
            {
                "id": 18,
                "text": "\"For many years, I have worked upon the geometry of Four Dimensions in secret.\"",
                "translation": "\"Uzun yıllardır gizlice Dört Boyut geometrisi üzerinde çalışıyordum.\"",
                "notes": "in secret: gizlice; geometry: geometri"
            },
            {
                "id": 19,
                "text": "\"And now, gentlemen, I have verified my theory by practical experiment.\"",
                "translation": "\"Ve şimdi baylar, teorimi pratik bir deneyle doğrulamış bulunuyorum.\"",
                "notes": "verify: doğrulamak; practical experiment: pratik deney"
            },
            {
                "id": 20,
                "text": "We stared at him in complete silence, wondering what extraordinary proof he was about to show us.",
                "translation": "Bize nasıl olağanüstü bir kanıt göstermek üzere olduğunu merak ederek derin bir sessizlik içinde ona baktık.",
                "notes": "extraordinary proof: olağanüstü kanıt; stare in silence: sessizce bakmak"
            }
        ]
    },

    # Page 2 (Sentences 21-40)
    {
        "page_no": 2,
        "title": "The Model Mechanism and the Laboratory",
        "tr_title": "Model Mekanizma ve Laboratuvar",
        "vocab_focus": [
            ("mechanism", "mekanizma, düzenek"),
            ("ivory", "fildişi"),
            ("quartz", "kuvars kristali"),
            ("lever", "kol, levyeli anahtar"),
            ("vanish", "aniden kaybolmak"),
            ("miniature", "minyatür, küçük ölçekli"),
            ("laboratory", "laboratuvar"),
            ("convince", "ikna etmek")
        ],
        "sentences": [
            {
                "id": 21,
                "text": "The Time Traveller rose from his chair and led us into his private laboratory.",
                "translation": "Zaman Gezgini sandalyesinden kalktı ve bizi özel laboratuvarına götürdü.",
                "notes": "private laboratory: özel laboratuvar; rise: kalkmak"
            },
            {
                "id": 22,
                "text": "On a large wooden table stood a delicate mechanism scarcely larger than a small clock.",
                "translation": "Büyük ahşap bir masanın üzerinde, küçük bir saatten ancak biraz daha büyük zarif bir mekanizma duruyordu.",
                "notes": "delicate mechanism: zarif mekanizma; scarcely: ancak, neredeyse"
            },
            {
                "id": 23,
                "text": "It was made of shining brass, polished nickel, white ivory, and transparent quartz crystal.",
                "translation": "Parlak pirinç, cilalı nikel, beyaz fildişi ve şeffaf kuvars kristalinden yapılmıştı.",
                "notes": "brass: pirinç metal; transparent quartz: şeffaf kuvars"
            },
            {
                "id": 24,
                "text": "\"This is the miniature model of my machine,\" he explained, touching the delicate frame.",
                "translation": "\"Bu makinemin minyatür modelidir,\" diye açıkladı zarif çerçeveye dokunarak.",
                "notes": "miniature model: minyatür maket; frame: çerçeve, gövde"
            },
            {
                "id": 25,
                "text": "The Medical Man inspected the device closely through his spectacles.",
                "translation": "Hekim gözlüklerinin ardından cihazı yakından inceledi.",
                "notes": "inspect closely: yakından incelemek; spectacles: gözlük"
            },
            {
                "id": 26,
                "text": "\"There are two levers,\" the inventor pointed out with proud satisfaction.",
                "translation": "\"İki kol var,\" diye belirtti mucit gururlu bir memnuniyetle.",
                "notes": "lever: kol, kaldıraç; satisfaction: memnuniyet"
            },
            {
                "id": 27,
                "text": "\"One sends the machine travelling into the future, and the other sends it into the past.\"",
                "translation": "\"Biri makineyi geleceğe doğru yolculuğa gönderir, diğeri ise geçmişe yollar.\"",
                "notes": "travel into the future: geleceğe seyahat etmek"
            },
            {
                "id": 28,
                "text": "He invited the Medical Man to push the forward lever with his own finger.",
                "translation": "Hekimi ileriye doğru olan kola kendi parmağıyla basması için davet etti.",
                "notes": "invite: davet etmek; push: itmek, basmak"
            },
            {
                "id": 29,
                "text": "As the lever moved, a sudden eddy of wind swept across the workshop.",
                "translation": "Kol hareket ettiği anda, atölye boyunca ani bir rüzgar girdabı esti.",
                "notes": "eddy of wind: rüzgar girdabı; sweep across: esip geçmek"
            },
            {
                "id": 30,
                "text": "The small brass machine began to spin and blur until its outline became indistinct.",
                "translation": "Küçük pirinç makine dönmeye ve silikleşmeye başladı, ta ki hatları belirsizleşene dek.",
                "notes": "blur: bulanıklaşmak; indistinct: belirsiz"
            },
            {
                "id": 31,
                "text": "In a fraction of a second, with a faint whistling sound, the model vanished completely.",
                "translation": "Saniyenin onda biri kadar bir sürede, hafif bir ıslık sesiyle model tamamen yok oldu.",
                "notes": "fraction of a second: saniyenin onda biri; vanish: yok olmak"
            },
            {
                "id": 32,
                "text": "The table was entirely empty; not a screw or wire remained upon the wood.",
                "translation": "Masa tamamen boştu; tahtanın üzerinde tek bir vida ya da tel bile kalmamıştı.",
                "notes": "entirely empty: tamamen boş; screw: vida"
            },
            {
                "id": 33,
                "text": "\"Where has it gone?\" cried the Medical Man, stepping back in astonishment.",
                "translation": "\"Nereye gitti bu?\" diye haykırdı Hekim, şaşkınlıkla geriye adım atarak.",
                "notes": "step back: geri çekilmek; astonishment: büyük şaşkınlık"
            },
            {
                "id": 34,
                "text": "\"It has gone into the future,\" the Time Traveller replied calmly.",
                "translation": "\"Geleceğe gitti,\" diye sakin bir tonla cevap verdi Zaman Gezgini.",
                "notes": "reply calmly: sakince yanıtlamak"
            },
            {
                "id": 35,
                "text": "\"It is travelling through time right now, faster than the speed of light.\"",
                "translation": "\"Şu anda zamanın içinde ışık hızından daha hızlı bir şekilde ilerliyor.\"",
                "notes": "speed of light: ışık hızı; travel through time: zamanda yolculuk etmek"
            },
            {
                "id": 36,
                "text": "Then he drew aside a heavy curtain at the end of the spacious room.",
                "translation": "Ardından geniş odanın ucundaki ağır bir perdeyi kenara çekti.",
                "notes": "draw aside: kenara çekmek; curtain: perde"
            },
            {
                "id": 37,
                "text": "There stood a full-sized machine, constructed of bronze, ebony, and gleaming nickel bars.",
                "translation": "Orada bronz, abanoz ağacı ve parıldayan nikel çubuklardan yapılmış gerçek boyutlu bir makine duruyordu.",
                "notes": "full-sized: tam boyutlu; ebony: abanoz ağacı"
            },
            {
                "id": 38,
                "text": "\"In this machine,\" he declared, \"I intend to explore the untold ages of our world.\"",
                "translation": "\"Bu makinenin içinde,\" dedi kararlılıkla, \"dünyamızın anlatılmamış çağlarını keşfetmeye niyetliyim.\"",
                "notes": "intend: niyetinde olmak; untold ages: anlatılmamış çağlar"
            },
            {
                "id": 39,
                "text": "We were stunned into silence, unable to determine whether he was mad or a brilliant visionary.",
                "translation": "Delirmiş mi yoksa dahi bir vizyoner mi olduğunu anlayamayarak şaşkınlıktan sessizliğe gömüldük.",
                "notes": "visionary: ileri görüşlü kimse; stunned: donakalmış"
            },
            {
                "id": 40,
                "text": "\"I shall start on my voyage tomorrow morning,\" he said with a serene smile.",
                "translation": "\"Yolculuğuma yarın sabah başlayacağım,\" dedi dingin bir tebessümle.",
                "notes": "voyage: seyahat, sefer; serene: huzurlu, dingin"
            }
        ]
    },

    # Page 3 (Sentences 41-60)
    {
        "page_no": 3,
        "title": "The Flight into Time: Night and Day",
        "tr_title": "Zamana Doğru Uçuş: Gece ve Gündüz",
        "vocab_focus": [
            ("sensation", "duyum, his"),
            ("whirl", "fırıl fırıl dönmek"),
            ("accelerate", "hızlanmak, ivmelenmek"),
            ("flicker", "titreşmek, yanıp sönmek"),
            ("velocity", "hız, sürat"),
            ("hazy", "puslu, dumanlı"),
            ("dizziness", "baş dönmesi"),
            ("milestone", "dönüm noktası, kilometre taşı")
        ],
        "sentences": [
            {
                "id": 41,
                "text": "The Time Traveller settled into the saddle of his full-scale machine and grasped the starting lever.",
                "translation": "Zaman Gezgini tam ölçekli makinesinin selesine yerleşti ve çalıştırma kolunu kavradı.",
                "notes": "settle into: yerleşmek; saddle: sele, oturak"
            },
            {
                "id": 42,
                "text": "He took a deep breath, checked his pocket watch, and pressed the lever forward.",
                "translation": "Derin bir nefes aldı, cep saatini kontrol etti ve kolu ileri doğru itti.",
                "notes": "deep breath: derin nefes; press forward: ileri itmek"
            },
            {
                "id": 43,
                "text": "Instantly, a strange and nauseating sensation of falling overwhelmed his senses.",
                "translation": "Anında, tuhaf ve mide bulandırıcı bir düşüş hissi duyularını altüst etti.",
                "notes": "nauseating sensation: mide bulandırıcı his; overwhelm: bastırmak, altüst etmek"
            },
            {
                "id": 44,
                "text": "The laboratory around him grew faint and hazy, like an image reflected in mist.",
                "translation": "Etrafındaki laboratuvar, siste yansıyan bir görüntü gibi silikleşti ve puslandı.",
                "notes": "hazy: puslu; reflected in mist: siste yansıyan"
            },
            {
                "id": 45,
                "text": "He pushed the lever further, accelerating his velocity through the stream of time.",
                "translation": "Kolu daha da ileri iterek zaman akışındaki hızını artırdı.",
                "notes": "accelerate: hızlandırmak; velocity: hız, sürat"
            },
            {
                "id": 46,
                "text": "Night followed day like the flapping of a black wing, fluttering faster and faster.",
                "translation": "Gece, kara bir kanadın çırpınışı gibi gündüzü izliyor, gittikçe daha hızlı kanat çırpıyordu.",
                "notes": "flapping of a wing: kanat çırpma; flutter: pırpır etmek"
            },
            {
                "id": 47,
                "text": "Soon the alternation of darkness and daylight merged into a continuous grey brightness.",
                "translation": "Çok geçmeden karanlık ve aydınlığın birbirini izlemesi kesintisiz gri bir parlaklığa dönüştü.",
                "notes": "alternation: sırayla değişme; merge: birleşmek"
            },
            {
                "id": 48,
                "text": "The sun became a streak of golden fire across the sky, tracing seasonal curves.",
                "translation": "Güneş, gökyüzünde mevsimsel kavisler çizerek altın bir ateş çizgisine dönüştü.",
                "notes": "streak of fire: ateş şeridi; trace curves: kavisler çizmek"
            },
            {
                "id": 49,
                "text": "The moon spun rapidly from new crescent to full disc, waxing and waning in seconds.",
                "translation": "Ay saniyeler içinde hilalden dolunaya geçerek büyüyüp küçülüyor, hızla dönüyordu.",
                "notes": "wax and wane: büyüyüp küçülmek (ay evreleri); crescent: hilal"
            },
            {
                "id": 50,
                "text": "He saw trees growing like puffs of green vapour, spreading their branches, and vanishing.",
                "translation": "Ağaçların yeşil buhar kümeleri gibi büyüdüğünü, dallarını açtığını ve yok olduğunu gördü.",
                "notes": "puffs of vapour: buhar bulutları; spread branches: dalları yaymak"
            },
            {
                "id": 51,
                "text": "Old buildings crumbled to dust and grand new palaces rose up in the blink of an eye.",
                "translation": "Eski binalar toza dönüşürken, göz açıp kapayıncaya kadar yeni görkemli saraylar yükseliyordu.",
                "notes": "crumble to dust: toza dönüşmek; blink of an eye: göz açıp kapayıncaya dek"
            },
            {
                "id": 52,
                "text": "A terrifying dizziness gripped him as the speedometer recorded thousands of years passing.",
                "translation": "Hız göstergesi binlerce yılın geçtiğini kaydederken korkunç bir baş dönmesi onu yakaladı.",
                "notes": "terrifying dizziness: dehşet verici baş dönmesi; speedometer: hız göstergesi"
            },
            {
                "id": 53,
                "text": "The hills changed their shapes slowly, melting and reforming under the relentless flight of centuries.",
                "translation": "Tepeler yüzyılların amansız uçuşu altında eriyip yeniden biçimlenerek yavaş yavaş şekil değiştirdi.",
                "notes": "relentless: amansız; melt and reform: eriyip yeniden şekillenmek"
            },
            {
                "id": 54,
                "text": "He wondered what kind of humanity awaited him in the distant future.",
                "translation": "Uzak gelecekte kendisini nasıl bir insanlığın beklediğini merak etti.",
                "notes": "distant future: uzak gelecek; await: beklemek"
            },
            {
                "id": 55,
                "text": "\"Have people conquered sickness, cruelty, and ignorance?\" he asked himself in awe.",
                "translation": "\"Acaba insanlar hastalığı, zalimliği ve cehaleti yenebildi mi?\" diye sordu kendi kendine hayretle.",
                "notes": "conquer: fethetmek, alt etmek; ignorance: cehalet; in awe: huşu içinde"
            },
            {
                "id": 56,
                "text": "A sudden dread seized his heart that he might crash into a solid structure when stopping.",
                "translation": "Durduğunda sert bir yapıya çarpabileceği endişesi birden yüreğini sardı.",
                "notes": "dread: derin korku, dehşet; solid structure: katı yapı"
            },
            {
                "id": 57,
                "text": "He decided that he must bring the speeding apparatus to a sudden halt.",
                "translation": "Hızla ilerleyen düzeneği ani bir şekilde durdurması gerektiğine karar verdi.",
                "notes": "apparatus: aygıt, cihaz; sudden halt: ani duruş"
            },
            {
                "id": 58,
                "text": "With nervous hands, he pulled hard upon the reverse braking lever.",
                "translation": "Gergin elleriyle ters yöndeki fren kolunu kuvvetle çekti.",
                "notes": "reverse braking lever: geri fren kolu; nervous: gergin"
            },
            {
                "id": 59,
                "text": "There was a sound of thunder, a violent jolt, and he was flung headlong through the air.",
                "translation": "Bir gök gürültüsü sesi, şiddetli bir sarsıntı duyuldu ve baş aşağı havaya savruldu.",
                "notes": "flung headlong: baş aşağı savrulmuş; violent jolt: şiddetli sarsıntı"
            },
            {
                "id": 60,
                "text": "He landed on a soft lawn in a heavy shower of warm spring rain.",
                "translation": "Ilık bir bahar yağmuru sağanağı altında yumuşak bir çimenliğe düştü.",
                "notes": "soft lawn: yumuşak çimenlik; shower of rain: yağmur sağanağı"
            }
        ]
    },

    # Page 4 (Sentences 61-80)
    {
        "page_no": 4,
        "title": "Arrival in 802,701 AD and the White Sphinx",
        "tr_title": "MS 802.701 Yılına Varış ve Beyaz Sfenks",
        "vocab_focus": [
            ("sphinx", "sfenks heykeli"),
            ("pedestal", "kaide, heykel tabanı"),
            ("marble", "mermer"),
            ("weathered", "aşınmış, yıpranmış"),
            ("foliage", "yeşillik, bitki örtüsü"),
            ("gigantic", "devasa"),
            ("hailstorm", "dolu fırtınası"),
            ("bronze", "tunç, bronz")
        ],
        "sentences": [
            {
                "id": 61,
                "text": "The Time Traveller sat up on the wet grass and wiped the raindrops from his eyes.",
                "translation": "Zaman Gezgini ıslak çimlerin üzerinde doğruldu ve gözlerindeki yağmur damlalarını sildi.",
                "notes": "sit up: doğrulmak; raindrops: yağmur damlaları"
            },
            {
                "id": 62,
                "text": "Looking at the dials of his machine, he read the unbelievable date: Eight Hundred and Two Thousand, Seven Hundred and One.",
                "translation": "Makinesinin kadranlarına baktığında inanılmaz tarihi okudu: Sekiz Yüz İki Bin Yedi Yüz Bir.",
                "notes": "dials: göstergeler, kadranlar; unbelievable date: inanılmaz tarih"
            },
            {
                "id": 63,
                "text": "He had travelled more than eight hundred millennia into the destiny of planet Earth.",
                "translation": "Dünya gezegeninin kaderinde sekiz yüz bin yıldan fazla ileriye yolculuk yapmıştı.",
                "notes": "millennia: binyıllar; destiny: kader"
            },
            {
                "id": 64,
                "text": "Towering directly above him through the mist was an enormous statue carved of white marble.",
                "translation": "Sisin içinden tam tepesinde yükselen, beyaz mermerden oyulmuş devasa bir heykel vardı.",
                "notes": "tower above: tepesinde yükselmek; carved: yontulmuş, oyulmuş"
            },
            {
                "id": 65,
                "text": "It was shaped like a winged Sphinx, resting upon a colossal pedestal of weathered bronze.",
                "translation": "Aşınmış bronzdan muazzam bir kaide üzerinde duran kanatlı bir Sfenks biçimindeydi.",
                "notes": "winged Sphinx: kanatlı Sfenks; colossal pedestal: devasa kaide"
            },
            {
                "id": 66,
                "text": "The face of the Sphinx was turned toward him, its sightless stone eyes gazing into eternity.",
                "translation": "Sfenks'in yüzü ona dönüktü, görmeyen taş gözleri sonsuzluğa dikilmişti.",
                "notes": "sightless eyes: görmeyen gözler; eternity: sonsuzluk"
            },
            {
                "id": 67,
                "text": "A faint, enigmatic smile seemed to hover on its weathered lips.",
                "translation": "Aşınmış dudaklarında hafif, gizemli bir tebessüm dolaşıyor gibiydi.",
                "notes": "enigmatic smile: gizemli tebessüm; hover: gezinmek, asılı kalmak"
            },
            {
                "id": 68,
                "text": "The hailstorm quickly passed, and warm sunshine bathed the unfamiliar landscape.",
                "translation": "Dolu fırtınası hızla geçti ve ılık güneş ışığı yabancı manzarayı yıkadı.",
                "notes": "hailstorm: dolu fırtınası; unfamiliar landscape: yabancı manzara"
            },
            {
                "id": 69,
                "text": "The air was fragrant with strange flowers, unlike any blossoms he had known in England.",
                "translation": "Hava, İngiltere'de bildiği hiçbir çiçeğe benzemeyen tuhaf çiçeklerin kokusuyla doluydu.",
                "notes": "fragrant: mis kokulu; blossoms: çiçekler"
            },
            {
                "id": 70,
                "text": "Rich, lush foliage covered the rolling hills, and grand ruined palaces dotted the horizon.",
                "translation": "Gür ve zengin bitki örtüsü engebeli tepeleri örtüyor, ufukta görkemli harabe saraylar görünüyordu.",
                "notes": "lush foliage: gür bitki örtüsü; ruined palaces: harabe saraylar"
            },
            {
                "id": 71,
                "text": "The whole world looked like an untended yet magnificent paradise garden.",
                "translation": "Tüm dünya, bakımsız ama yine de muazzam bir cennet bahçesine benziyordu.",
                "notes": "untended: bakımsız; magnificent: muazzam, görkemli"
            },
            {
                "id": 72,
                "text": "\"What has become of mankind?\" he whispered, standing cautiously beside his machine.",
                "translation": "\"İnsanlığa ne oldu acaba?\" diye fısıldadı makinesinin yanında temkinle dikilerek.",
                "notes": "what has become of: başına ne geldi; cautiously: temkinle"
            },
            {
                "id": 73,
                "text": "He checked the bronze machine and made sure that its vital levers were undamaged.",
                "translation": "Bronz makineyi kontrol etti ve hayati kollarının hasar görmediğinden emin oldu.",
                "notes": "vital levers: hayati kollar; undamaged: hasarsız"
            },
            {
                "id": 74,
                "text": "Then he unscrewed the tiny ivory levers and placed them safely into his pocket.",
                "translation": "Sonra minik fildişi kolları vidalarından söküp güvenle cebine koydu.",
                "notes": "unscrew: vidasını sökmek; safely: güvenle"
            },
            {
                "id": 75,
                "text": "Without these small levers, nobody could operate the machine in his absence.",
                "translation": "Bu küçük kollar olmadan, onun yokluğunda hiç kimse makineyi çalıştıramazdı.",
                "notes": "operate: çalıştırmak; in one's absence: birinin yokluğunda"
            },
            {
                "id": 76,
                "text": "Suddenly, he noticed a group of slender figures approaching through the bushes.",
                "translation": "Aniden, çalıların arasından yaklaşmakta olan ince yapılı bir grup figür fark etti.",
                "notes": "slender figures: ince yapılı figürler; approach: yaklaşmak"
            },
            {
                "id": 77,
                "text": "They were dressed in soft, bright tunics of purple and white silk.",
                "translation": "Mor ve beyaz ipekten yapılmış yumuşak, parlak tunikler giymişlerdi.",
                "notes": "tunics: tunikler; silk: ipek"
            },
            {
                "id": 78,
                "text": "Their sandals were made of supple leather, fastened with delicate metallic clasps.",
                "translation": "Sandaletleri yumuşak deriden yapılmıştı ve zarif metal tokalarla bağlanmıştı.",
                "notes": "supple leather: esnek, yumuşak deri; clasp: toka"
            },
            {
                "id": 79,
                "text": "They walked with light, dancing steps, smiling innocently without any sign of fear.",
                "translation": "Hafif, dans eder gibi adımlarla yürüyor, hiçbir korku belirtisi göstermeden masumca gülümsüyorlardı.",
                "notes": "dancing steps: dans eder gibi adımlar; innocently: masumca"
            },
            {
                "id": 80,
                "text": "The Time Traveller stepped forward to greet the future inhabitants of the world.",
                "translation": "Zaman Gezgini, dünyanın gelecekteki sakinlerini selamlamak için öne doğru bir adım attı.",
                "notes": "inhabitants: sakinler, yaşayanlar; step forward: öne adım atmak"
            }
        ]
    },

    # Page 5 (Sentences 81-100)
    {
        "page_no": 5,
        "title": "Meeting the Eloi: The Gentle People of the Future",
        "tr_title": "Eloi Halkıyla Karşılaşma: Geleceğin Narin İnsanları",
        "vocab_focus": [
            ("fragile", "narin, kırılgan"),
            ("graceful", "zarif, incelikli"),
            ("garland", "çiçek çelengi"),
            ("tunic", "tunik, elbise"),
            ("curiosity", "merak"),
            ("childlike", "çocuksu"),
            ("gestures", "el kol hareketleri, jestler"),
            ("innocence", "masumiyet")
        ],
        "sentences": [
            {
                "id": 81,
                "text": "The creatures who gathered around him were small, delicate beings only four feet tall.",
                "translation": "Etrafında toplanan varlıklar sadece dört fit (120 cm) boyunda küçük, narin canlılardı.",
                "notes": "delicate beings: narin varlıklar; four feet tall: dört fit boyunda"
            },
            {
                "id": 82,
                "text": "They possessed exquisite beauty, with curly hair, large liquid eyes, and thin lips.",
                "translation": "Kıvırcık saçları, iri buğulu gözleri ve ince dudaklarıyla enfes bir güzelliğe sahiptiler.",
                "notes": "exquisite beauty: enfes güzellik; liquid eyes: buğulu, parlak gözler"
            },
            {
                "id": 83,
                "text": "Their skin was remarkably soft and pale, showing no marks of hard physical labor.",
                "translation": "Tenleri son derece yumuşak ve solgundu, ağır bedensel emeğe dair hiçbir iz taşımıyordu.",
                "notes": "physical labor: bedensel çalışma; remarkably: dikkate değer derecede"
            },
            {
                "id": 84,
                "text": "They looked at him with wondering curiosity, touching his rough coat with soft fingers.",
                "translation": "Yumuşak parmaklarıyla kaba paltosuna dokunarak ona hayret dolu bir merakla baktılar.",
                "notes": "rough coat: kaba kumaş palto; wondering curiosity: hayret dolu merak"
            },
            {
                "id": 85,
                "text": "One of them placed a garland of fragrant white blossoms gently around his neck.",
                "translation": "İçlerinden biri kokulu beyaz çiçeklerden yapılmış bir çelengi nazikçe boynuna taktı.",
                "notes": "garland: çiçek çelengi; fragrant blossoms: mis kokulu çiçekler"
            },
            {
                "id": 86,
                "text": "They spoke in a sweet, musical language composed of short, melodious vowels.",
                "translation": "Kısa ve ahenkli sesli harflerden oluşan tatlı, müzikal bir dille konuşuyorlardı.",
                "notes": "melodious vowels: melodik sesli harfler; musical language: müzikal dil"
            },
            {
                "id": 87,
                "text": "The Time Traveller tried to speak English, but they only laughed with childlike delight.",
                "translation": "Zaman Gezgini İngilizce konuşmaya çalıştı ama onlar yalnızca çocuksu bir neşeyle güldüler.",
                "notes": "childlike delight: çocuksu sevinç; laugh: gülmek"
            },
            {
                "id": 88,
                "text": "He pointed up at the sun to ask if they understood where he had come from.",
                "translation": "Nereden geldiğini anlayıp anlamadıklarını sormak için gökyüzündeki güneşi işaret etti.",
                "notes": "point at: işaret etmek; come from: -den gelmek"
            },
            {
                "id": 89,
                "text": "One of the little people pointed to the sky and made a sound like a clap of thunder.",
                "translation": "Küçük insanlardan biri gökyüzünü işaret etti ve gök gürültüsüne benzer bir ses çıkardı.",
                "notes": "clap of thunder: gök gürültüsü patlaması; make a sound: ses çıkarmak"
            },
            {
                "id": 90,
                "text": "They apparently believed that he had descended directly from the sun during the storm.",
                "translation": "Anlaşılan fırtına sırasında doğrudan güneşten indiğine inanıyorlardı.",
                "notes": "apparently: anlaşılan, görünüşe göre; descend: inmek"
            },
            {
                "id": 91,
                "text": "The Time Traveller was astonished by their complete lack of intellectual depth.",
                "translation": "Zaman Gezgini onların entelektüel derinlikten tamamen yoksun oluşuna çok şaşırdı.",
                "notes": "lack of depth: derinlik eksikliği; astonished: hayrete düşmüş"
            },
            {
                "id": 92,
                "text": "\"I expected to find a race of supreme intellect,\" he thought with deep disappointment.",
                "translation": "\"Üstün zekalı bir ırk bulmayı umuyordum,\" diye düşündü derin bir hayal kırıklığıyla.",
                "notes": "supreme intellect: üstün zeka; disappointment: hayal kırıklığı"
            },
            {
                "id": 93,
                "text": "\"Instead, these future humans have the minds of five-year-old children.\"",
                "translation": "\"Oysa bu geleceğin insanları beş yaşındaki çocukların zihnine sahip.\"",
                "notes": "instead: yerine, oysa; minds: zihinler"
            },
            {
                "id": 94,
                "text": "They took him by the hand and led him toward a vast hall of decorated stone.",
                "translation": "Onu elinden tuttular ve süslü taştan yapılmış devasa bir salona doğru götürdüler.",
                "notes": "take by the hand: elinden tutmak; decorated stone: süslemeli taş"
            },
            {
                "id": 95,
                "text": "The archways of the building were crumbling, covered with creeping ivy and wild roses.",
                "translation": "Binanın kemerleri ufalanıyor, sarmaşıklar ve yaban gülleriyle kaplanıyordu.",
                "notes": "crumbling archways: ufalanan kemerler; creeping ivy: sarmaşık"
            },
            {
                "id": 96,
                "text": "Inside, dozens of the gentle creatures sat upon cushions, eating delicious fruits.",
                "translation": "İçeride düzinelerce sevecen varlık minderlerin üzerine oturmuş, leziz meyveler yiyordu.",
                "notes": "cushions: minderler; delicious fruits: lezzetli meyveler"
            },
            {
                "id": 97,
                "text": "There was no sign of meat, bread, or cooking fire anywhere in the building.",
                "translation": "Binanın hiçbir yerinde et, ekmek veya yemek ateşine dair tek bir iz yoktu.",
                "notes": "no sign of: hiçbir izi olmamak; cooking fire: yemek ateşi"
            },
            {
                "id": 98,
                "text": "The fruits were sweet, juicy, and unlike anything cultivated in modern times.",
                "translation": "Meyveler tatlı, sulu ve modern çağlarda yetiştirilen hiçbir şeye benzemiyordu.",
                "notes": "juicy: sulu; cultivate: yetiştirmek, tarımını yapmak"
            },
            {
                "id": 99,
                "text": "Being hungry after his voyage, the Time Traveller ate heartily beside his hosts.",
                "translation": "Yolculuğundan sonra karnı acıkan Zaman Gezgini, ev sahiplerinin yanında iştahla karnını doyurdu.",
                "notes": "eat heartily: iştahla yemek; hosts: ev sahipleri"
            },
            {
                "id": 100,
                "text": "He noticed that these people, whom he learned were called the Eloi, lived in complete indolence.",
                "translation": "Adlarının Eloi olduğunu öğrendiği bu insanların tam bir tembellik ve kaygısızlık içinde yaşadığını fark etti.",
                "notes": "indolence: uyuşukluk, kaygısız tembellik; notice: fark etmek"
            }
        ]
    },

    # Page 6 (Sentences 101-120)
    {
        "page_no": 6,
        "title": "The Golden Age of Decay and the Absence of Labor",
        "tr_title": "Çöküşün Altın Çağı ve Emeğin Yokluğu",
        "vocab_focus": [
            ("decay", "çürüme, çöküş"),
            ("abundance", "bolluk, bereket"),
            ("disease", "hastalık"),
            ("competition", "rekabet"),
            ("stagnation", "durgunluk"),
            ("ruins", "harabeler"),
            ("leisure", "boş vakit, rahatlık"),
            ("decline", "gerileme, zayıflama")
        ],
        "sentences": [
            {
                "id": 101,
                "text": "After the meal, the Time Traveller walked out into the warm afternoon air to explore.",
                "translation": "Yemekten sonra Zaman Gezgini etrafı keşfetmek için ılık ikindi havasına çıktı.",
                "notes": "walk out: dışarı çıkmak; explore: keşfetmek"
            },
            {
                "id": 102,
                "text": "He climbed a green hill to gain a panoramic view of the Thames Valley in the future.",
                "translation": "Gelecekteki Thames Vadisi'nin panoramik bir manzarasını görmek için yeşil bir tepeye tırmandı.",
                "notes": "panoramic view: panoramik manzara; Thames Valley: Thames Vadisi"
            },
            {
                "id": 103,
                "text": "The entire country had become one vast, neglected garden of extraordinary beauty.",
                "translation": "Bütün ülke, olağanüstü güzellikte uçsuz bucaksız, ihmal edilmiş bir bahçeye dönüşmüştü.",
                "notes": "neglected garden: bakımsız bahçe; extraordinary: olağanüstü"
            },
            {
                "id": 104,
                "text": "There were no separate houses, no fences, no factories, and no signs of agriculture.",
                "translation": "Ayrı evler, çitler, fabrikalar ve hiçbir tarım faaliyeti belirtisi yoktu.",
                "notes": "fences: çitler; agriculture: tarım"
            },
            {
                "id": 105,
                "text": "The Eloi lived collectively in huge communal palaces that were slowly decaying.",
                "translation": "Eloi halkı, yavaş yavaş çürüyen devasa ortak saraylarda hep birlikte yaşıyordu.",
                "notes": "communal palaces: ortak saraylar; slowly decaying: yavaşça çürüyen"
            },
            {
                "id": 106,
                "text": "Everywhere he looked, ancient marble structures showed signs of weather damage and neglect.",
                "translation": "Baktığı her yerde, antik mermer yapılar hava şartlarının verdiği hasarın ve ihmalin izlerini taşıyordu.",
                "notes": "weather damage: hava şartı hasarı; neglect: ihmal"
            },
            {
                "id": 107,
                "text": "He sat on the crest of the hill and reflected on the strange fate of human civilization.",
                "translation": "Tepenin doruğuna oturdu ve insan uygarlığının tuhaf yazgısı üzerine düşündü.",
                "notes": "crest of the hill: tepenin doruğu; reflect on: üzerine kafa yormak"
            },
            {
                "id": 108,
                "text": "\"In my own Victorian century,\" he mused, \"humanity fought against nature, disease, and poverty.\"",
                "translation": "\"Kendi Viktorya yüzyılımda,\" diye düşündü, \"insanlık doğaya, hastalıklara ve yoksulluğa karşı savaşıyordu.\"",
                "notes": "muse: derin düşüncelere dalmak; poverty: yoksulluk"
            },
            {
                "id": 109,
                "text": "\"Now it appears that mankind has achieved complete victory over all hardships.\"",
                "translation": "\"Şimdi ise insanoğlunun tüm zorluklara karşı kesin bir zafer kazandığı anlaşılıyor.\"",
                "notes": "achieve victory: zafer kazanmak; hardships: zorluklar, sıkıntılar"
            },
            {
                "id": 110,
                "text": "There were no dangerous wild beasts, no poisonous weeds, and no infectious epidemics.",
                "translation": "Hiçbir tehlikeli vahşi hayvan, zehirli ot ya da bulaşıcı salgın hastalık kalmamıştı.",
                "notes": "wild beasts: vahşi canavarlar; infectious epidemics: bulaşıcı salgınlar"
            },
            {
                "id": 111,
                "text": "The climate had become uniformly warm, pleasant, and mild throughout the year.",
                "translation": "İklim yıl boyunca her yerde ılık, hoş ve ılıman hale gelmişti.",
                "notes": "uniformly: tekdüze, her yerde aynı; mild: ılıman"
            },
            {
                "id": 112,
                "text": "Yet this absolute security and abundance had brought an unexpected consequence: intellectual stagnation.",
                "translation": "Fakat bu mutlak güvenlik ve bolluk, beklenmedik bir sonucu da beraberinde getirmişti: zihinsel durgunluk.",
                "notes": "absolute security: mutlak güvenlik; stagnation: durgunluk"
            },
            {
                "id": 113,
                "text": "Without hardship, struggle, and competition, human strength and intelligence had withered away.",
                "translation": "Zorluk, mücadele ve rekabet olmayınca, insanın gücü ve zekası körelip yok olmuştu.",
                "notes": "wither away: solup gitmek, körelmek; struggle: mücadele"
            },
            {
                "id": 114,
                "text": "The Eloi were as weak and helpless as butterflies, spending their days dancing and singing.",
                "translation": "Eloi halkı birer kelebek kadar zayıf ve çaresizdi; günlerini dans edip şarkı söyleyerek geçiriyorlardı.",
                "notes": "helpless as butterflies: kelebekler kadar çaresiz; spend days: günleri geçirmek"
            },
            {
                "id": 115,
                "text": "They showed no interest in books, science, art, or any serious enterprise.",
                "translation": "Kitaplara, bilime, sanata veya herhangi bir ciddi girişime hiçbir ilgi göstermiyorlardı.",
                "notes": "serious enterprise: ciddi girişim; show interest: ilgi göstermek"
            },
            {
                "id": 116,
                "text": "\"Strength is the outcome of necessity; security sets a premium upon feebleness,\" he noted.",
                "translation": "\"Kuvvet zorunluluğun sonucudur; aşırı güvenlik ise güçsüzlüğü ödüllendirir,\" diye not düştü.",
                "notes": "outcome of necessity: zorunluluğun neticesi; feebleness: zayıflık, güçsüzlük"
            },
            {
                "id": 117,
                "text": "He felt a melancholy sadness looking down upon this faded twilight of humanity.",
                "translation": "İnsanlığın bu solgun alacakaranlığına tepeden bakarken hüzünlü bir keder hissetti.",
                "notes": "melancholy sadness: melankolik hüzün; twilight of humanity: insanlığın alacakaranlığı"
            },
            {
                "id": 118,
                "text": "The sun was sinking below the western hills, painting the clouds in crimson and gold.",
                "translation": "Güneş batıdaki tepelerin ardında batıyor, bulutları kızıla ve altına boyuyordu.",
                "notes": "sink below: ardında batmak; crimson: kızıla çalan kırmızı"
            },
            {
                "id": 119,
                "text": "He realized it was time to return to the lawn where he had left his Time Machine.",
                "translation": "Zaman Makinesini bıraktığı çimenliğe dönme vaktinin geldiğini anladı.",
                "notes": "realize: farkına varmak; return to: -e dönmek"
            },
            {
                "id": 120,
                "text": "He began to walk down the hill as the shadows lengthened across the silent valley.",
                "translation": "Gölgeler sessiz vadi boyunca uzarken tepeden aşağı doğru yürümeye başladı.",
                "notes": "shadows lengthen: gölgeler uzamak; silent valley: sessiz vadi"
            }
        ]
    },

    # Page 7 (Sentences 121-140)
    {
        "page_no": 7,
        "title": "Panic: The Vanished Machine and the Bronze Pedestal",
        "tr_title": "Panik: Kaybolan Makine ve Bronz Kaide",
        "vocab_focus": [
            ("panic", "panik, dehşet"),
            ("vanish", "yok olmak, kaybolmak"),
            ("despair", "umutsuzluk, çaresizlik"),
            ("drag", "sürüklemek"),
            ("footprints", "ayak izleri"),
            ("groove", "oluk, iz"),
            ("hollow", "içi boş"),
            ("trap", "kapana kısılmak")
        ],
        "sentences": [
            {
                "id": 121,
                "text": "As the Time Traveller reached the lawn near the White Sphinx, his blood ran cold.",
                "translation": "Zaman Gezgini Beyaz Sfenks'in yanındaki çimenliğe ulaştığında kanı dondu.",
                "notes": "blood runs cold: kanı donmak; reach: ulaşmak"
            },
            {
                "id": 122,
                "text": "The lawn was completely deserted, and the Time Machine was gone.",
                "translation": "Çimenlik tamamen ıssızdı ve Zaman Makinesi ortadan kaybolmuştu.",
                "notes": "deserted: terk edilmiş, ıssız; gone: gitmiş, yok olmuş"
            },
            {
                "id": 123,
                "text": "He rubbed his eyes in disbelief, thinking that in the dusk he had mistaken the place.",
                "translation": "Alacakaranlıkta yeri karıştırdığını düşünerek inanmaz gözlerle gözlerini ovuşturdu.",
                "notes": "in disbelief: inanamayarak; dusk: alacakaranlık"
            },
            {
                "id": 124,
                "text": "He ran wildly across the grass, stumbling over roots and tearing his clothes.",
                "translation": "Köklerin üzerinden tökezleyip giysilerini yırtarak çimlerin üzerinde çılgınca koştu.",
                "notes": "run wildly: çılgınca koşmak; stumble over: tökezlemek"
            },
            {
                "id": 125,
                "text": "No, there was no mistake: the circular mark where the machine had rested was clearly visible.",
                "translation": "Hayır, hiçbir hata yoktu: makinenin durduğu yerdeki dairesel ezik iz açıkça görünüyordu.",
                "notes": "circular mark: dairesel iz; clearly visible: açıkça görünür"
            },
            {
                "id": 126,
                "text": "A sickening wave of terror and despair swept through his entire body.",
                "translation": "Bütün bedenini dehşet ve çaresizlik dolu mide bulandırıcı bir dalga sardı.",
                "notes": "sickening wave: mide bulandırıcı dalga; terror: dehşet"
            },
            {
                "id": 127,
                "text": "\"I am trapped in the year 802,701!\" he cried out in bitter agony.",
                "translation": "\"802.701 yılında kapana kısıldım!\" diye acı bir ızdırapla haykırdı.",
                "notes": "trapped: tuzağa düşmüş, mahsur; bitter agony: acı ızdırap"
            },
            {
                "id": 128,
                "text": "Without the machine, he could never return to his friends, his home, or his own century.",
                "translation": "Makine olmadan arkadaşlarına, evine ya da kendi yüzyılına asla dönemezdi.",
                "notes": "never return: asla geri dönememek"
            },
            {
                "id": 129,
                "text": "He struck matches to inspect the soft ground around the pedestal of the Sphinx.",
                "translation": "Sfenks'in kaidesinin etrafındaki yumuşak zemini incelemek için kibritler çaktı.",
                "notes": "strike matches: kibrit çakmak; inspect ground: zemini incelemek"
            },
            {
                "id": 130,
                "text": "In the damp earth, he found deep grooves where heavy wheels or metal bars had been dragged.",
                "translation": "Nemli toprakta, ağır tekerleklerin veya metal çubukların sürüklendiği derin oluklar buldu.",
                "notes": "deep grooves: derin oluklar; drag: sürüklemek"
            },
            {
                "id": 131,
                "text": "Alongside the grooves were strange narrow footprints that did not look entirely human.",
                "translation": "Olukların yanında, pek de insana benzemeyen tuhaf ve dar ayak izleri vardı.",
                "notes": "narrow footprints: dar ayak izleri; alongside: yanı sıra"
            },
            {
                "id": 132,
                "text": "The tracks led directly to the bronze doors at the base of the colossal pedestal.",
                "translation": "İzler doğrudan devasa kaidenin tabanındaki bronz kapılara çıkıyordu.",
                "notes": "tracks: izler; base of pedestal: kaidenin tabanı"
            },
            {
                "id": 133,
                "text": "He rushed to the doors and hammered on the thick bronze panels with his bare fists.",
                "translation": "Kapılara doğru koştu ve çıplak yumruklarıyla kalın bronz panelleri yumrukladı.",
                "notes": "hammer on: yumruklamak; bare fists: çıplak yumruklar"
            },
            {
                "id": 134,
                "text": "The metal rang with a hollow sound, indicating that there was a large cavernous chamber within.",
                "translation": "Metal içi boş bir sesle yankılandı, bu da içeride büyük, mağaramsı bir oda olduğunu gösteriyordu.",
                "notes": "hollow sound: içi boş yankı; cavernous chamber: mağaramsı oda"
            },
            {
                "id": 135,
                "text": "The doors were locked fast from the inside and refused to yield even an inch.",
                "translation": "Kapılar içeriden sıkıca kilitlenmişti ve tek bir santim bile oynamıyordu.",
                "notes": "locked fast: sıkıca kilitli; refuse to yield: boyun eğmemek, oynamamak"
            },
            {
                "id": 136,
                "text": "He found a heavy flint stone and battered the bronze panels until his hands bled.",
                "translation": "Ağır bir çakmaktaşı buldu ve elleri kanayana kadar bronz panellere vurdu.",
                "notes": "flint stone: çakmaktaşı; batter: dövmek, art arda vurmak"
            },
            {
                "id": 137,
                "text": "The White Sphinx seemed to smile down upon his useless fury with cold indifference.",
                "translation": "Beyaz Sfenks, onun nafile öfkesine soğuk bir kayıtsızlıkla tepeden gülümsüyor gibiydi.",
                "notes": "useless fury: nafile öfke; cold indifference: soğuk kayıtsızlık"
            },
            {
                "id": 138,
                "text": "Exhausted and breathless, he collapsed onto the grass and wept like a child.",
                "translation": "Tükenmiş ve nefessiz kalmış halde çimlerin üzerine yığıldı ve bir çocuk gibi ağladı.",
                "notes": "exhausted: bitkin; collapse: yere yığılmak; weep: ağlamak"
            },
            {
                "id": 139,
                "text": "Gradually, his scientific reason asserted itself over his hysterical panic.",
                "translation": "Zamanla, bilimsel aklı histerik paniğine baskın geldi.",
                "notes": "scientific reason: bilimsel akıl; assert itself: kendini göstermek"
            },
            {
                "id": 140,
                "text": "\"The machine is inside that pedestal,\" he told himself firmly. \"I must find a way to open it.\"",
                "translation": "\"Makine o kaidenin içinde,\" dedi kendi kendine kararlılıkla. \"Onu açmanın bir yolunu bulmalıyım.\"",
                "notes": "firmly: kararlılıkla; find a way: bir yol bulmak"
            }
        ]
    },

    # Page 8 (Sentences 141-160)
    {
        "page_no": 8,
        "title": "Saving Weena: A Pure Friendship in the Future",
        "tr_title": "Weena'yı Kurtarmak: Gelecekte Saf Bir Dostluk",
        "vocab_focus": [
            ("stream", "akarsu, dere"),
            ("drown", "boğulmak"),
            ("rescue", "kurtarmak"),
            ("affection", "şefkat, sevgi"),
            ("cramp", "kramp"),
            ("devotion", "bağlılık, sadakat"),
            ("pocket", "cep"),
            ("companion", "yoldaş, arkadaş")
        ],
        "sentences": [
            {
                "id": 141,
                "text": "The following morning, the Time Traveller decided to interrogate the Eloi about the bronze doors.",
                "translation": "Ertesi sabah Zaman Gezgini, bronz kapılar hakkında Eloi halkını sorgulamaya karar verdi.",
                "notes": "interrogate: sorgulamak; following morning: ertesi sabah"
            },
            {
                "id": 142,
                "text": "Whenever he pointed to the Sphinx and made gestures of opening, they turned away in disgust and terror.",
                "translation": "Ne zaman Sfenks'i işaret edip açma hareketleri yapsa, tiksinti ve dehşet içinde arkalarını dönüyorlardı.",
                "notes": "disgust: tiksinti; terror: dehşet; gesture: hareket, jest"
            },
            {
                "id": 143,
                "text": "It was obvious that they held the Sphinx and the underworld in absolute taboo.",
                "translation": "Sfenks'i ve yer altı dünyasını mutlak bir tabu olarak gördükleri apaçıktı.",
                "notes": "obvious: apaçık, bariz; absolute taboo: mutlak tabu"
            },
            {
                "id": 144,
                "text": "He walked toward a shallow river where several Eloi were bathing in the morning sun.",
                "translation": "Birkaç Eloi'nin sabah güneşinde yıkandığı sığ bir nehre doğru yürüdü.",
                "notes": "shallow river: sığ nehir; bathe: yıkanmak, yüzmek"
            },
            {
                "id": 145,
                "text": "Suddenly, one of the little women was seized by a violent cramp and began to sink beneath the water.",
                "translation": "Aniden, küçük kadınlardan birini şiddetli bir kramp yakaladı ve suyun altına batmaya başladı.",
                "notes": "cramp: kramp; sink beneath: dibe batmak"
            },
            {
                "id": 146,
                "text": "She was swept downstream, crying out faintly for assistance.",
                "translation": "Akıntıyla aşağı sürükleniyor, cılız bir sesle yardım için bağırıyordu.",
                "notes": "swept downstream: akıntıyla sürüklenmek; assistance: yardım"
            },
            {
                "id": 147,
                "text": "Astonishingly, none of her companions made the slightest effort to rescue her.",
                "translation": "Şaşırtıcı şekilde, arkadaşlarından hiçbiri onu kurtarmak için en ufak bir çaba göstermedi.",
                "notes": "astonishingly: şaşırtıcı şekilde; slightest effort: en ufak çaba"
            },
            {
                "id": 148,
                "text": "They simply watched her drown with placid, unconcerned curiosity from the riverbank.",
                "translation": "Nehir kıyısından kayıtsız ve umursamaz bir merakla onun boğulmasını öylece seyrettiler.",
                "notes": "placid: dingin, sakin; unconcerned: umursamaz"
            },
            {
                "id": 149,
                "text": "The Time Traveller tore off his heavy coat, plunged into the current, and swam swiftly.",
                "translation": "Zaman Gezgini ağır paltosunu fırlattı, akıntıya daldı ve hızla yüzdü.",
                "notes": "tear off: fırlatıp çıkarmak; plunge into: içine dalmak"
            },
            {
                "id": 150,
                "text": "He seized her delicate arm just as she slipped beneath the swirling foam.",
                "translation": "Köpüklerin arasına batmak üzereyken narin kolundan yakaladı.",
                "notes": "seize: kavramak, yakalamak; swirling foam: köpüren girdap"
            },
            {
                "id": 151,
                "text": "Pulling her ashore, he rubbed her cold limbs until her breathing returned to normal.",
                "translation": "Onu kıyıya çekip nefesi normale dönene kadar soğuk uzuvlarını ovuşturdu.",
                "notes": "ashore: kıyıya; cold limbs: soğuk kollar bacaklar"
            },
            {
                "id": 152,
                "text": "Her name, as he soon learned, was Weena, a tiny and gentle creature.",
                "translation": "Kısa sürede öğrendiğine göre adı Weena'ydı; minik ve nazik bir varlıktı.",
                "notes": "gentle creature: narin, nazik varlık"
            },
            {
                "id": 153,
                "text": "From that moment onward, Weena regarded him with boundless devotion and love.",
                "translation": "O andan itibaren Weena ona sonsuz bir bağlılık ve sevgiyle bağlandı.",
                "notes": "boundless devotion: sonsuz bağlılık; regard: bakmak, görmek"
            },
            {
                "id": 154,
                "text": "She followed him everywhere like a faithful puppy, refusing to leave his side.",
                "translation": "Sadık bir yavru köpek gibi onu her yerde takip etti, yanından ayrılmayı reddetti.",
                "notes": "faithful puppy: sadık yavru köpek; refuse: reddetmek"
            },
            {
                "id": 155,
                "text": "She wove wreaths of exotic blossoms and placed them upon his shoulders.",
                "translation": "Egzotik çiçeklerden taçlar ördü ve bunları onun omuzlarına yerleştirdi.",
                "notes": "wreaths: çiçek çelenkleri; exotic: egzotik, yabancı"
            },
            {
                "id": 156,
                "text": "She would run ahead, pluck rare flowers, and stuff them playfully into his jacket pockets.",
                "translation": "Önden koşar, nadide çiçekler toplar ve bunları şakacı bir tavırla ceketinin ceplerine tıkardı.",
                "notes": "pluck: koparmak; stuff playfully: şakacıktan tıkıştırmak"
            },
            {
                "id": 157,
                "text": "Her affectionate presence gave the Time Traveller immense comfort in this alien world.",
                "translation": "Onun şefkat dolu varlığı, bu yabancı dünyada Zaman Gezgini'ne muazzam bir teselli verdi.",
                "notes": "immense comfort: büyük teselli; alien world: yabancı dünya"
            },
            {
                "id": 158,
                "text": "Yet he noticed that Weena had a dreadful, overwhelming fear of the dark.",
                "translation": "Yine de Weena'nın karanlığa karşı korkunç, bastırılamaz bir korkusu olduğunu fark etti.",
                "notes": "overwhelming fear: bastırılamaz korku; dreadful: dehşet verici"
            },
            {
                "id": 159,
                "text": "Whenever sunset approached, all the Eloi would rush indoors and sleep clustered closely together.",
                "translation": "Gün batımı yaklaştığında, bütün Eloi halkı içeri koşar ve birbirine sokulup uyurdu.",
                "notes": "sunset: gün batımı; clustered together: birbirine sokulmuş"
            },
            {
                "id": 160,
                "text": "There was clearly something monstrous that stalked the night, something that terrorized their innocent lives.",
                "translation": "Geceleri kol gezen, masum hayatlarına dehşet saçan canavarımsı bir şey olduğu kesindi.",
                "notes": "stalk the night: geceleri kol gezmek; monstrous: canavarca"
            }
        ]
    },

    # Page 9 (Sentences 161-180)
    {
        "page_no": 9,
        "title": "The Deep Wells and the Subterranean Machinery",
        "tr_title": "Derin Kuyular ve Yer Altı Makineleri",
        "vocab_focus": [
            ("well", "kuyu"),
            ("ventilation", "havalandırma"),
            ("subterranean", "yer altı"),
            ("shaft", "kuyu bacası, şaft"),
            ("thud", "gümleme sesi, tok ses"),
            ("mechanism", "mekanizma"),
            ("draught", "hava akımı, cereyan"),
            ("rung", "merdiven basamağı")
        ],
        "sentences": [
            {
                "id": 161,
                "text": "During his walks across the hills, the Time Traveller noticed several deep, circular stone wells.",
                "translation": "Tepelerdeki yürüyüşleri sırasında Zaman Gezgini birkaç derin, yuvarlak taş kuyu fark etti.",
                "notes": "circular stone wells: yuvarlak taş kuyular; notice: fark etmek"
            },
            {
                "id": 162,
                "text": "These wells were carefully constructed with carved stone rims, but they contained no buckets or ropes.",
                "translation": "Bu kuyular özenle oyulmuş taş çeperlerle inşa edilmişti ancak içlerinde ne kova ne de ip vardı.",
                "notes": "carved rims: oymalı kenarlar; bucket: kova"
            },
            {
                "id": 163,
                "text": "When he leaned over the mouth of a well, he felt a steady draught of cool air sucking downward.",
                "translation": "Bir kuyunun ağzına doğru eğildiğinde, aşağıya doğru emilen düzenli bir serin hava akımı hissetti.",
                "notes": "steady draught: düzenli hava akımı; suck downward: aşağı çekilmek"
            },
            {
                "id": 164,
                "text": "From deep within the black darkness came a rhythmic thudding sound: thud-thud, thud-thud.",
                "translation": "Karanlığın derinliklerinden ritmik bir gümleme sesi geliyordu: güm-güm, güm-güm.",
                "notes": "rhythmic thudding: ritmik tok ses; deep within: derinliklerden"
            },
            {
                "id": 165,
                "text": "It sounded like the slow, steady heartbeat of some gigantic underground steam engine.",
                "translation": "Devasa bir yer altı buhar makinesinin yavaş, düzenli kalp atışına benziyordu.",
                "notes": "steam engine: buhar makinesi; heartbeat: kalp atışı"
            },
            {
                "id": 166,
                "text": "He struck a match and dropped it down into the yawning shaft.",
                "translation": "Bir kibrit çaktı ve esneyen dipsiz kuyu boşluğuna doğru bıraktı.",
                "notes": "yawning shaft: dipsiz kuyu bacası; strike a match: kibrit yakmak"
            },
            {
                "id": 167,
                "text": "Before the flame was extinguished by the wind, he caught a glimpse of metal rungs embedded in the wall.",
                "translation": "Alev rüzgardan sönmeden önce duvara çakılmış metal merdiven basamaklarına bir anlık göz attı.",
                "notes": "metal rungs: metal basamaklar; catch a glimpse: bir anlığına görmek"
            },
            {
                "id": 168,
                "text": "It was an iron ladder leading straight down into the pitch-black abyss.",
                "translation": "Zifiri karanlık uçuruma doğru dimdik inen demir bir merdivendi bu.",
                "notes": "pitch-black abyss: zifiri karanlık uçurum; lead down: aşağı inmek"
            },
            {
                "id": 169,
                "text": "\"These wells are huge ventilation shafts for a subterranean world,\" he deduced.",
                "translation": "\"Bu kuyular bir yer altı dünyası için devasa havalandırma bacalarıdır,\" çıkarımında bulundu.",
                "notes": "ventilation shafts: havalandırma bacaları; deduce: mantıksal sonuca varmak"
            },
            {
                "id": 170,
                "text": "He threw a pebble down, but it fell for a long time before striking metal far below.",
                "translation": "Aşağıya küçük bir çakıl taşı fırlattı fakat taş çok aşağılardaki bir metale çarpmadan önce uzun süre düştü.",
                "notes": "pebble: çakıl taşı; strike metal: metale çarpmak"
            },
            {
                "id": 171,
                "text": "The Eloi avoided these wells with obvious shuddering horror.",
                "translation": "Eloi halkı bariz bir ürperti ve dehşetle bu kuyulardan uzak duruyordu.",
                "notes": "shuddering horror: ürpertici dehşet; avoid: kaçınmak"
            },
            {
                "id": 172,
                "text": "If he sat near a well, Weena would tug at his hand and beg him in tears to come away.",
                "translation": "Kuyulardan birinin yanına otursa, Weena elini çekiştirir ve gözyaşları içinde oradan uzaklaşması için ona yalvarırdı.",
                "notes": "tug at: çekiştirmek; in tears: gözyaşları içinde"
            },
            {
                "id": 173,
                "text": "One morning, seeking shelter from the heat in a dark ruined hall, he saw two glowing eyes watching him.",
                "translation": "Bir sabah sıcaktan kaçıp karanlık bir harabe salona sığındığında, parıldayan iki gözün kendisini izlediğini gördü.",
                "notes": "glowing eyes: parıldayan gözler; seek shelter: sığınak aramak"
            },
            {
                "id": 174,
                "text": "A pale, ape-like creature was crouching in the shadows beside a pillar.",
                "translation": "Soluk tenli, maymuna benzer bir yaratık bir sütunun yanındaki gölgelerde çömelmiş duruyordu.",
                "notes": "ape-like creature: maymunumsu yaratık; crouch: çömelmek"
            },
            {
                "id": 175,
                "text": "Its skin was a dull bleached white, like a blind fish from a subterranean cavern.",
                "translation": "Ten rengi, bir yer altı mağarasından çıkan kör bir balık gibi donuk, solgun bir beyazlıktaydı.",
                "notes": "bleached white: kireç gibi beyaz; subterranean cavern: yer altı mağarası"
            },
            {
                "id": 176,
                "text": "It had flaxen hair upon its back, red reflective eyes, and long, claw-like fingers.",
                "translation": "Sırtında açık sarı tüyler, kırmızı yansıtıcı gözler ve uzun pençemsi parmaklar vardı.",
                "notes": "flaxen hair: keten rengi tüy/saç; claw-like: pençe benzeri"
            },
            {
                "id": 177,
                "text": "The Time Traveller stepped forward to touch it, but the creature recoiled in terror from the sunlight.",
                "translation": "Zaman Gezgini ona dokunmak için öne adım attı fakat yaratık güneş ışığından dehşetle geri kaçtı.",
                "notes": "recoil: irkilip geri sıçramak; in terror: korkuyla"
            },
            {
                "id": 178,
                "text": "It scampered across the ruin with incredible agility and plunged down the shaft of a nearby well.",
                "translation": "İnanılmaz bir çeviklikle harabeden geçti ve yakındaki bir kuyunun bacasından aşağıya daldı.",
                "notes": "scamper: hızlıca kaçmak; agility: çeviklik"
            },
            {
                "id": 179,
                "text": "He peered down and saw the creature climbing down the iron ladder like a spider.",
                "translation": "Aşağı baktı ve yaratığın demir merdivenden bir örümcek gibi aşağı indiğini gördü.",
                "notes": "peer down: aşağıya dikkatle bakmak; like a spider: örümcek gibi"
            },
            {
                "id": 180,
                "text": "\"Now I understand,\" he thought. \"Mankind has not merged into one; it has split into two distinct species!\"",
                "translation": "\"Şimdi anlıyorum,\" diye düşündü. \"İnsanlık tek bir türde birleşmemiş; iki ayrı türe ayrılmış!\"",
                "notes": "split into two: ikiye bölünmek; distinct species: farklı türler"
            }
        ]
    },

    # Page 10 (Sentences 181-200)
    {
        "page_no": 10,
        "title": "The Morlocks: The Dark Subterranean Species",
        "tr_title": "Morlocklar: Karanlık Yer Altı Türü",
        "vocab_focus": [
            ("species", "tür"),
            ("subterranean", "yer altı"),
            ("aristocracy", "aristokrasi, soylular sınıfı"),
            ("capitalist", "kapitalist"),
            ("nocturnal", "gece yaşayan"),
            ("underworld", "yer altı dünyası"),
            ("predator", "avcı, yırtıcı"),
            ("evolution", "evrim")
        ],
        "sentences": [
            {
                "id": 181,
                "text": "The Time Traveller developed a startling sociological theory to explain this terrible split.",
                "translation": "Zaman Gezgini bu korkunç bölünmeyi açıklamak için çarpıcı bir sosyolojik teori geliştirdi.",
                "notes": "startling theory: çarpıcı teori; terrible split: korkunç ayrım"
            },
            {
                "id": 182,
                "text": "He realized that the division between rich and poor had continued widen over hundreds of thousands of years.",
                "translation": "Zengin ve yoksul arasındaki ayrımın yüz binlerce yıl boyunca giderek derinleştiğini anladı.",
                "notes": "division: bölünme, ayrım; widen: genişlemek"
            },
            {
                "id": 183,
                "text": "The wealthy classes had driven the laborers underground into subterranean factories.",
                "translation": "Zengin sınıflar işçileri yer altındaki fabrikalara sürmüşlerdi.",
                "notes": "wealthy classes: varlıklı sınıflar; laborer: işçi"
            },
            {
                "id": 184,
                "text": "Generation after generation, the workers lived entirely in tunnels, deprived of sunshine.",
                "translation": "Nesiller boyunca işçiler güneş ışığından mahrum şekilde tamamen tünellerde yaşamışlardı.",
                "notes": "deprived of: -den mahrum; generation after generation: nesiller boyu"
            },
            {
                "id": 185,
                "text": "Their descendants became the Morlocks: nocturnal, pale, sensitive to light, and predatory.",
                "translation": "Onların torunları Morlocklar haline gelmişti: gece yaşayan, solgun, ışığa duyarlı ve yırtıcı.",
                "notes": "nocturnal: gececil; predatory: yırtıcı, avcı"
            },
            {
                "id": 186,
                "text": "Meanwhile, the upper classes remained on the surface in sunlit luxury, becoming the fragile Eloi.",
                "translation": "Bu sırada üst sınıflar güneşli lüks içinde yüzeyde kalmış ve narin Eloi haline gelmişti.",
                "notes": "sunlit luxury: güneşli lüks; fragile: narin, kırılgan"
            },
            {
                "id": 187,
                "text": "The Eloi possessed beauty and grace, but they had lost all courage, strength, and ingenuity.",
                "translation": "Eloi güzelliğe ve zarafete sahipti ama tüm cesaretini, gücünü ve hünerini kaybetmişti.",
                "notes": "ingenuity: ustalık, hüner; courage: cesaret"
            },
            {
                "id": 188,
                "text": "The Morlocks maintained the underground machinery that made the Eloi's clothes and cleaned the rivers.",
                "translation": "Morlocklar, Eloi'nin elbiselerini yapan ve nehirleri temizleyen yer altı makinelerinin bakımını yapıyordu.",
                "notes": "maintain machinery: makinelerin bakımını yapmak"
            },
            {
                "id": 189,
                "text": "\"At first,\" he thought, \"the relation between the two species seemed like master and servant.\"",
                "translation": "\"İlk başta,\" diye düşündü, \"iki tür arasındaki ilişki efendi ve hizmetkar gibi görünüyordu.\"",
                "notes": "relation: ilişki; master and servant: efendi ve uşak"
            },
            {
                "id": 190,
                "text": "\"The Eloi were the idle masters, and the Morlocks were the underground slaves.\"",
                "translation": "\"Eloi asalak efendilerdi, Morlocklar ise yer altındaki kölelerdi.\"",
                "notes": "idle masters: aylak efendiler; underground slaves: yer altı köleleri"
            },
            {
                "id": 191,
                "text": "Then a far darker and more horrifying truth began to dawn upon his mind.",
                "translation": "Derken zihninde çok daha karanlık ve korkunç bir gerçek belirmeye başladı.",
                "notes": "dawn upon mind: aklına dank etmek, belirmek; horrifying: dehşet verici"
            },
            {
                "id": 192,
                "text": "He remembered that the Eloi were strictly vegetarian, eating only fruit.",
                "translation": "Eloi'nin sadece meyve yiyerek katı bir vejetaryen olduğunu hatırladı.",
                "notes": "strictly vegetarian: katı vejetaryen"
            },
            {
                "id": 193,
                "text": "Yet in the underground caverns, he had smelled the distinct scent of roast meat.",
                "translation": "Oysa yer altı mağaralarında bariz bir kızarmış et kokusu duymuştu.",
                "notes": "distinct scent: belirgin koku; roast meat: kızarmış et"
            },
            {
                "id": 194,
                "text": "There were no cows, sheep, or horses anywhere on the surface of the earth.",
                "translation": "Dünya yüzeyinde hiçbir inek, koyun veya at kalmamıştı.",
                "notes": "surface of the earth: yeryüzü"
            },
            {
                "id": 195,
                "text": "Where, then, did the Morlocks obtain their supply of meat?",
                "translation": "Öyleyse Morlocklar et ihtiyaçlarını nereden temin ediyordu?",
                "notes": "obtain: elde etmek; supply: tedarik"
            },
            {
                "id": 196,
                "text": "The horrifying realization struck him with the force of a physical blow.",
                "translation": "Korkunç gerçeğin farkına varması ona fiziksel bir darbe kuvvetiyle çarptı.",
                "notes": "horrifying realization: dehşet verici farkındalık; physical blow: fiziksel darbe"
            },
            {
                "id": 197,
                "text": "The Eloi were not masters at all; they were cattle kept by the Morlocks for food!",
                "translation": "Eloi asla efendi değildi; onlar Morlocklar tarafından besin için yetiştirilen büyükbaş hayvanlardı!",
                "notes": "cattle: büyükbaş hayvan sürüsü; kept for food: yemek için beslenen"
            },
            {
                "id": 198,
                "text": "The Morlocks clothed and fed them in the sunshine until they were ready to be harvested in the dark.",
                "translation": "Morlocklar onları karanlıkta hasat edilmeye hazır olana kadar güneşte giydirip besliyordu.",
                "notes": "harvest: hasat etmek; feed: beslemek"
            },
            {
                "id": 199,
                "text": "This explained the overwhelming terror the Eloi felt whenever the moonless night approached.",
                "translation": "Bu durum, aysız gece yaklaştığında Eloi'nin hissettiği o bastırılamaz dehşeti açıklıyordu.",
                "notes": "moonless night: aysız gece; explain terror: dehşeti açıklamak"
            },
            {
                "id": 200,
                "text": "And it was the Morlocks who had dragged his precious Time Machine into the bronze pedestal!",
                "translation": "Ve onun paha biçilmez Zaman Makinesini bronz kaidenin içine sürükleyenler de Morlocklardı!",
                "notes": "precious: değerli; drag into: içine sürüklemek"
            }
        ]
    },

    # Page 11 (Sentences 201-220)
    {
        "page_no": 11,
        "title": "Descent into the Abyss: Matches in the Dark",
        "tr_title": "Uçuruma İniş: Karanlıkta Kibritler",
        "vocab_focus": [
            ("descent", "iniş, alçalma"),
            ("abyss", "uçurum, dipsiz derinlik"),
            ("ladder", "merdiven"),
            ("suffocate", "boğulmak, nefessiz kalmak"),
            ("match", "kibrit"),
            ("cavern", "mağara"),
            ("clammy", "yapış yapış, soğuk ve nemli"),
            ("escape", "kaçmak, kurtulmak")
        ],
        "sentences": [
            {
                "id": 201,
                "text": "The Time Traveller knew that to recover his machine, he had to confront the Morlocks in their lair.",
                "translation": "Zaman Gezgini makinesini geri almak için Morlocklarla kendi inlerinde yüzleşmesi gerektiğini biliyordu.",
                "notes": "recover: geri almak; confront in lair: ininde yüzleşmek"
            },
            {
                "id": 202,
                "text": "He approached one of the circular wells with grim and unyielding determination.",
                "translation": "Kararlı ve boyun eğmez bir azimle dairesel kuyulardan birine yaklaştı.",
                "notes": "unyielding determination: sarsılmaz azim; grim: ciddi, kararlı"
            },
            {
                "id": 203,
                "text": "Weena wept bitterly, clinging to his knees and begging him not to enter the well.",
                "translation": "Weena dizlerine sarılıp kuyuya girmemesi için yalvararak acı acı ağladı.",
                "notes": "cling to knees: dizlerine sarılmak; weep bitterly: acı acı ağlamak"
            },
            {
                "id": 204,
                "text": "He kissed her tenderly, placed a handful of flowers in her hair, and swung his legs over the rim.",
                "translation": "Onu şefkatle öptü, saçlarına bir avuç çiçek koydu ve bacaklarını kenardan aşağı sarkıttı.",
                "notes": "swing legs over rim: bacakları kenardan sarkıtmak; tenderly: şefkatle"
            },
            {
                "id": 205,
                "text": "He grasped the cold iron rungs and began his perilous descent into the dark shaft.",
                "translation": "Soğuk demir basamakları kavradı ve karanlık kuyu boşluğuna doğru tehlikeli inişine başladı.",
                "notes": "perilous descent: tehlikeli iniş; grasp rungs: basamakları kavramak"
            },
            {
                "id": 206,
                "text": "The air grew hotter, thicker, and smelled foully of decaying grease and stagnant damp.",
                "translation": "Hava daha sıcak, daha ağır hale geldi ve çürümüş makine yağı ile durgun rutubetin pis kokusunu yaydı.",
                "notes": "decaying grease: bozulmuş gres yağı; stagnant damp: durgun nem"
            },
            {
                "id": 207,
                "text": "His arms ached terribly after climbing down more than two hundred feet of vertical ladder.",
                "translation": "İki yüz fitten (60 metre) fazla dik merdivenden indikten sonra kolları feci şekilde ağrıyordu.",
                "notes": "vertical ladder: dik merdiven; ache terribly: feci ağrımak"
            },
            {
                "id": 208,
                "text": "At last, his boots touched solid stone in a vast subterranean corridor.",
                "translation": "Sonunda botları devasa bir yer altı koridorundaki sert taşa değdi.",
                "notes": "touch solid stone: sert taşa değmek; corridor: koridor"
            },
            {
                "id": 209,
                "text": "He heard a soft pattering of naked feet and whisperings in the pitch darkness around him.",
                "translation": "Çevresindeki zifiri karanlıkta çıplak ayakların hafif pıtırtılarını ve fısıltıları duydu.",
                "notes": "pattering of feet: ayak pıtırtısı; pitch darkness: zifiri karanlık"
            },
            {
                "id": 210,
                "text": "Cold, clammy fingers touched his face and began tugging at his clothing.",
                "translation": "Soğuk, nemli parmaklar yüzüne dokundu ve giysilerini çekiştirmeye başladı.",
                "notes": "clammy fingers: nemli parmaklar; tug at: çekiştirmek"
            },
            {
                "id": 211,
                "text": "He reached into his pocket and struck one of his precious safety matches.",
                "translation": "Cebine uzandı ve değerli emniyet kibritlerinden birini yaktı.",
                "notes": "safety match: emniyet kibriti; precious: kıymetli"
            },
            {
                "id": 212,
                "text": "The sudden flare of light illuminated a horrifying scene in the cavern.",
                "translation": "Işığın ani alevlenmesi mağaradaki dehşet verici manzarayı aydınlattı.",
                "notes": "flare of light: ışık alevlenmesi; illuminate: aydınlatmak"
            },
            {
                "id": 213,
                "text": "Dozens of Morlocks recoiled from the brightness, covering their oversized red eyes with their hands.",
                "translation": "Düzinelerce Morlock parlaklıktan irkilerek kocaman kırmızı gözlerini elleriyle kapattı.",
                "notes": "oversized: aşırı büyük; recoil: geri çekilmek"
            },
            {
                "id": 214,
                "text": "They were hideous, stunted creatures with white hair and pale, sickly skin.",
                "translation": "Beyaz saçlı, solgun ve hastalıklı tenli, biçimsiz ve çirkin yaratıklardı.",
                "notes": "stunted creatures: cılız, güdük yaratıklar; hideous: iğrenç, korkunç"
            },
            {
                "id": 215,
                "text": "On a massive iron table nearby lay a freshly butchered carcass covered with a cloth.",
                "translation": "Yakındaki masif demir bir masanın üzerinde üzeri bir bezle örtülü yeni kesilmiş bir karkas yatıyordu.",
                "notes": "butchered carcass: kesilmiş karkas et; massive: masif, koca"
            },
            {
                "id": 216,
                "text": "The match burned down to his fingers and went out, plunging him once more into darkness.",
                "translation": "Kibrit parmaklarına kadar yandı ve söndü; onu bir kez daha karanlığa gömdü.",
                "notes": "burn down: yanıp tükenmek; plunge into darkness: karanlığa gömmek"
            },
            {
                "id": 217,
                "text": "Instantly, the creatures lunged at him from every corner, hissing like venomous snakes.",
                "translation": "Anında, yaratıklar zehirli yılanlar gibi tıslayarak her köşeden onun üzerine atıldı.",
                "notes": "lunge at: üzerine atılmak; hiss: tıslamak"
            },
            {
                "id": 218,
                "text": "He struck another match, which made them scatter momentarily in blinding pain.",
                "translation": "Bir kibrit daha çaktı, bu da kör edici acıyla bir anlığına dağılmalarını sağladı.",
                "notes": "scatter momentarily: bir anlığına dağılmak; blinding pain: kör edici acı"
            },
            {
                "id": 219,
                "text": "Realizing his mortal danger, he fought his way desperately back toward the ladder shaft.",
                "translation": "Ölümcül tehlikesinin farkına vararak umutsuzca merdiven bacasına doğru yolunu açtı.",
                "notes": "mortal danger: ölümcül tehlike; fight one's way: savaşarak yol açmak"
            },
            {
                "id": 220,
                "text": "He climbed upward with superhuman effort, kicking away the clutching hands of his pursuers.",
                "translation": "Kendisini kovalayanların yakalamaya çalışan ellerini tekmeleyerek insanüstü bir gayretle yukarı tırmandı.",
                "notes": "superhuman effort: insanüstü çaba; pursuers: takip edenler"
            }
        ]
    },

    # Page 12 (Sentences 221-240)
    {
        "page_no": 12,
        "title": "The Palace of Green Porcelain: Arsenal of the Past",
        "tr_title": "Yeşil Porselen Sarayı: Geçmişin Cephaneliği",
        "vocab_focus": [
            ("porcelain", "porselen"),
            ("museum", "müze"),
            ("weapon", "silah"),
            ("crowbar", "levye, demir çubuk"),
            ("camphor", "kâfur, yanıcı reçine"),
            ("combustible", "kolay yanan, parlayıcı"),
            ("exhibit", "sergi nesnesi"),
            ("shelter", "sığınak, barınak")
        ],
        "sentences": [
            {
                "id": 221,
                "text": "The Time Traveller scrambled out of the well into the dazzling sunlight, bruised and exhausted.",
                "translation": "Zaman Gezgini morluklar içinde ve bitkin bir halde kuyudan göz kamaştırıcı güneş ışığına çıktı.",
                "notes": "scramble out: güçbela dışarı çıkmak; bruised: ezik ve morluklar içinde"
            },
            {
                "id": 222,
                "text": "Weena greeted him with joyous cries, covering his hands with tears and kisses.",
                "translation": "Weena ellerini gözyaşları ve öpücüklerle yıkayarak onu sevinç çığlıklarıyla karşıladı.",
                "notes": "joyous cries: sevinç çığlıkları; greet: karşılamak"
            },
            {
                "id": 223,
                "text": "He knew that he needed weapons and fire to break open the bronze pedestal and defend himself.",
                "translation": "Bronz kaideyi kırmak ve kendini savunmak için silahlara ve ateşe ihtiyacı olduğunu biliyordu.",
                "notes": "break open: kırarak açmak; defend oneself: kendini savunmak"
            },
            {
                "id": 224,
                "text": "Miles away to the southwest stood a gigantic structure gleaming with greenish tiles.",
                "translation": "Millerce uzakta güneybatıda yeşilimsi çinilerle parıldayan devasa bir yapı yükseliyordu.",
                "notes": "gigantic structure: devasa yapı; tiles: çiniler, karolar"
            },
            {
                "id": 225,
                "text": "Taking Weena with him, he set out on a long trek toward this mysterious Palace of Green Porcelain.",
                "translation": "Weena'yı yanına alarak bu gizemli Yeşil Porselen Sarayı'na doğru uzun bir yürüyüşe çıktı.",
                "notes": "set out on trek: zorlu yürüyüşe çıkmak; mysterious: gizemli"
            },
            {
                "id": 226,
                "text": "They walked all afternoon through fragrant meadows, while Weena gathered wild blossoms.",
                "translation": "Bütün öğleden sonrayı mis kokulu çayırlardan yürüyerek geçirdiler; Weena bu sırada kır çiçekleri topladı.",
                "notes": "fragrant meadows: mis kokulu çayırlar; gather: toplamak"
            },
            {
                "id": 227,
                "text": "When they arrived, he discovered that the palace was a vast, ruined museum of ancient human history.",
                "translation": "Vardıklarında, sarayın antik insanlık tarihine ait devasa, harabe bir müze olduğunu keşfetti.",
                "notes": "ruined museum: harabe müze; arrive: varmak"
            },
            {
                "id": 228,
                "text": "Glass cases were broken, and historical artifacts from the Victorian era and beyond lay covered in dust.",
                "translation": "Cam vitrinler kırılmıştı ve Viktorya döneminden ve sonrasından kalma tarihi eserler tozla kaplanmıştı.",
                "notes": "glass cases: cam vitrinler; artifacts: tarihi eserler"
            },
            {
                "id": 229,
                "text": "He walked through galleries of fossil skeletons, decaying machinery, and decaying books.",
                "translation": "Fosil iskeletlerin, çürüyen makinelerin ve unufak olan kitapların sergilendiği salonlardan geçti.",
                "notes": "fossil skeletons: fosil iskeletler; galleries: sergi salonları"
            },
            {
                "id": 230,
                "text": "In a mineralogy room, he found a glass jar containing a large block of dry camphor.",
                "translation": "Bir mineraloji odasında, büyük bir kalıp kuru kâfur içeren bir cam kavanoz buldu.",
                "notes": "camphor: kâfur (yanıcı organik madde); mineralogy: mineraloji"
            },
            {
                "id": 231,
                "text": "Camphor was an exceptionally combustible substance that would burn with a bright, smoky flame.",
                "translation": "Kâfur, parlak ve dumanlı bir alevle yanan son derece yanıcı bir maddeydi.",
                "notes": "combustible substance: kolay tutuşan madde; smoky flame: dumanlı alev"
            },
            {
                "id": 232,
                "text": "He slipped the camphor eagerly into his pockets, thanking fortune for this useful discovery.",
                "translation": "Bu faydalı keşif için talihe teşekkür ederek kâfuru hevesle ceplerine koydu.",
                "notes": "useful discovery: yararlı keşif; fortune: talih, şans"
            },
            {
                "id": 233,
                "text": "Further along, in a ruined military gallery, he found a display of heavy steel machinery.",
                "translation": "Daha ileride, yıkık bir askeri galeride ağır çelik makinelerin sergilendiği bir alan buldu.",
                "notes": "military gallery: askeri galeri; display: sergi"
            },
            {
                "id": 234,
                "text": "He managed to break off a stout iron lever about three feet long: a perfect crowbar.",
                "translation": "Yaklaşık üç fit (90 cm) uzunluğunda sağlam bir demir kolu kırmayı başardı: mükemmel bir levye.",
                "notes": "stout iron lever: sağlam demir kol; crowbar: levye"
            },
            {
                "id": 235,
                "text": "\"With this iron bar,\" he exclaimed, \"I can smash open the bronze doors of the Sphinx!\"",
                "translation": "\"Bu demir çubukla,\" diye haykırdı, \"Sfenks'in bronz kapılarını kırıp açabilirim!\"",
                "notes": "smash open: kırıp parçalayarak açmak; iron bar: demir çubuk"
            },
            {
                "id": 236,
                "text": "He swung the heavy weapon in his hands, feeling his confidence and courage return.",
                "translation": "Güveninin ve cesaretinin geri geldiğini hissederek ağır silahı ellerinde salladı.",
                "notes": "confidence: kendine güven; courage: cesaret"
            },
            {
                "id": 237,
                "text": "In another damaged cabinet, he found an unbroken tin box containing a box of matches.",
                "translation": "Hasarlı başka bir dolapta, bir kutu kibrit içeren sağlam bir teneke kutu buldu.",
                "notes": "tin box: teneke kutu; unbroken: hasarsız, kırılmamış"
            },
            {
                "id": 238,
                "text": "Now he possessed iron for striking, matches for lighting, and camphor for fuel.",
                "translation": "Artık vurmak için demire, yakmak için kibrite ve yakıt için kâfura sahipti.",
                "notes": "strike: vurmak; fuel: yakıt"
            },
            {
                "id": 239,
                "text": "Weena clung to his side, looking anxiously through the broken windows at the dying twilight.",
                "translation": "Weena kırık pencerelerden can çekişen alacakaranlığa endişeyle bakarak onun yanına sokuldu.",
                "notes": "dying twilight: sönen alacakaranlık; anxiously: endişeyle"
            },
            {
                "id": 240,
                "text": "A dark, dense forest lay between them and the White Sphinx, and night was falling fast.",
                "translation": "Aralarıyla Beyaz Sfenks arasında karanlık, sık bir orman uzanıyordu ve gece hızla çöküyordu.",
                "notes": "dense forest: sık orman; night falls: gece çökmek"
            }
        ]
    },

    # Page 13 (Sentences 241-260)
    {
        "page_no": 13,
        "title": "Night in the Burning Forest and the Loss of Weena",
        "tr_title": "Yanan Ormanda Gece ve Weena'nın Kaybı",
        "vocab_focus": [
            ("bonfire", "büyük ateş, şenlik ateşi"),
            ("conflagration", "büyük yangın"),
            ("embers", "közler"),
            ("screech", "tiz çığlık"),
            ("smoke", "duman"),
            ("tragedy", "trajedi, facia"),
            ("perish", "yok olmak, can vermek"),
            ("grief", "keder, derin üzüntü")
        ],
        "sentences": [
            {
                "id": 241,
                "text": "They entered the black shadow of the woods, Weena trembling with terror on his shoulder.",
                "translation": "Ormanın kara gölgesine girdiler; Weena onun omzunda dehşet içinde titriyordu.",
                "notes": "tremble with terror: korkuyla titremek; woods: orman"
            },
            {
                "id": 242,
                "text": "The darkness was so thick that the Time Traveller could hardly distinguish the tree trunks.",
                "translation": "Karanlık o kadar yoğundu ki Zaman Gezgini ağaç gövdelerini güçlükle ayırt edebiliyordu.",
                "notes": "distinguish: ayırt etmek; tree trunks: ağaç gövdeleri"
            },
            {
                "id": 243,
                "text": "He could hear soft footsteps padding behind them, and pale figures darted between the branches.",
                "translation": "Arkalarından gelen hafif adımları duyabiliyordu ve dalların arasında solgun silüetler süzülüyordu.",
                "notes": "padding footsteps: yumuşak ayak sesleri; dart: hızla süzülmek"
            },
            {
                "id": 244,
                "text": "To keep the Morlocks at bay, he built a small fire of dried twigs and ignited some camphor.",
                "translation": "Morlockları uzakta tutmak için kuru dallardan küçük bir ateş yaktı ve biraz kâfur tutuşturdu.",
                "notes": "keep at bay: uzakta tutmak; dry twigs: kuru ince dallar"
            },
            {
                "id": 245,
                "text": "The chemical burned with a brilliant white flame that pushed back the advancing shadows.",
                "translation": "Kimyasal madde, yaklaşan gölgeleri geriye iten parlak beyaz bir alevle yandı.",
                "notes": "brilliant white flame: parlak beyaz alev; advance: ilerlemek"
            },
            {
                "id": 246,
                "text": "Overcome with exhaustion, the Time Traveller sat down on the moss and closed his eyes.",
                "translation": "Yorgunluktan bitap düşen Zaman Gezgini yosunların üzerine oturdu ve gözlerini kapattı.",
                "notes": "overcome with exhaustion: yorgunluktan bitap düşmek; moss: yosun"
            },
            {
                "id": 247,
                "text": "Weena lay curled up in his lap, breathing softly like a sleeping kitten.",
                "translation": "Weena kucağında kıvrılmış, uyuyan bir kedi yavrusu gibi usulca nefes alıyordu.",
                "notes": "curled up: kıvrılmış; kitten: kedi yavrusu"
            },
            {
                "id": 248,
                "text": "He intended only to rest for a few minutes, but profound sleep overpowered him.",
                "translation": "Yalnızca birkaç dakika dinlenmeye niyetliydi fakat derin bir uyku onu ele geçirdi.",
                "notes": "profound sleep: derin uyku; overpower: alt etmek, ele geçirmek"
            },
            {
                "id": 249,
                "text": "He awoke to find fingers tugging at his throat and his iron bar being wrenched away.",
                "translation": "Boğazını çekiştiren parmaklarla ve demir çubuğunun elinden çekilip alınmasıyla uyandı.",
                "notes": "wrench away: zorla çekip almak; throat: boğaz"
            },
            {
                "id": 250,
                "text": "The small fire had spread out of control into the dry grass and dead bushes.",
                "translation": "Küçük ateş kontrolden çıkarak kuru çimlere ve ölü çalılara sıçramıştı.",
                "notes": "spread out of control: kontrolden çıkmak; dead bushes: kuru çalılar"
            },
            {
                "id": 251,
                "text": "A roaring wall of flame was sweeping through the trees, creating a raging conflagration.",
                "translation": "Kükreyen bir alev duvarı ağaçların arasından geçerek şiddetli bir yangın yaratıyordu.",
                "notes": "raging conflagration: azgın büyük yangın; roaring wall: kükreyen duvar"
            },
            {
                "id": 252,
                "text": "Blinded by the glare, the terrified Morlocks ran shrieking directly into the fire.",
                "translation": "Parlama yüzünden gözleri kör olan dehşet içindeki Morlocklar çığlıklar atarak dosdoğru ateşin içine koştular.",
                "notes": "blinded by glare: ışıktan gözü kamaşmış; shriek: çığlık atmak"
            },
            {
                "id": 253,
                "text": "The Time Traveller struck out with his fists, striking down the creatures that clawed at him.",
                "translation": "Zaman Gezgini yumruklarını savurarak kendisini pençeleyen yaratıkları yere serdi.",
                "notes": "strike out: yumruk savurmak; claw at: pençelemek"
            },
            {
                "id": 254,
                "text": "In the blinding smoke and chaos, he reached out desperately for Weena, but she was gone.",
                "translation": "Kör edici duman ve kargaşada umutsuzca Weena'ya uzandı ama o yoktu.",
                "notes": "blinding smoke: kör edici duman; reach out: elini uzatmak"
            },
            {
                "id": 255,
                "text": "He shouted her name again and again into the roar of the burning timber: \"Weena! Weena!\"",
                "translation": "Yanan kerestelerin kükremesi içinde defalarca onun adını haykırdı: \"Weena! Weena!\"",
                "notes": "burning timber: yanan keresteler/ağaçlar; roar: kükreme"
            },
            {
                "id": 256,
                "text": "No answer came through the smoke, only the crackle of burning branches and the cries of dying Morlocks.",
                "translation": "Dumanın içinden hiçbir cevap gelmedi; yalnızca yanan dalların çıtırtısı ve can veren Morlockların çığlıkları duyuldu.",
                "notes": "crackle of branches: dalların çıtırtısı; no answer: cevap yok"
            },
            {
                "id": 257,
                "text": "He searched frantically until the intense heat threatened to scorch his clothes and skin.",
                "translation": "Yoğun ısı giysilerini ve tenini yakmakla tehdit edene kadar çılgınca aradı.",
                "notes": "search frantically: çılgınca aramak; scorch: yakmak, kavurmak"
            },
            {
                "id": 258,
                "text": "Weena had perished in the fire, suffocated by the smoke or seized by the panicked subterranean creatures.",
                "translation": "Weena dumandan boğularak ya da panikleyen yer altı yaratıkları tarafından kapılarak yangında can vermişti.",
                "notes": "perish: can vermek; suffocate: havasızlıktan boğulmak"
            },
            {
                "id": 259,
                "text": "Weeping with bitter grief and remorse, he staggered out of the flaming woods into the open meadow.",
                "translation": "Acı bir keder ve vicdan azabıyla ağlayarak alevler içindeki ormandan açık çayırlığa doğru sendeledi.",
                "notes": "bitter grief: acı keder; remorse: vicdan azabı; stagger: sendeleyerek yürümek"
            },
            {
                "id": 260,
                "text": "Dawn was breaking over the eastern horizon as he stood alone, his heart broken by the tragic loss.",
                "translation": "O tek başına dururken doğu ufkunda şafak söküyordu, yüreği bu trajik kayıpla paramparça olmuştu.",
                "notes": "dawn breaks: şafak sökmek; tragic loss: trajik kayıp"
            }
        ]
    },

    # Page 14 (Sentences 261-280)
    {
        "page_no": 14,
        "title": "The Bronze Pedestal Opened: Escape into the Far Future",
        "tr_title": "Bronz Kaide Açıldı: Uzak Geleceğe Kaçış",
        "vocab_focus": [
            ("pedestal", "kaide"),
            ("ambush", "tuzak, pusu"),
            ("lubricate", "yağlamak"),
            ("lever", "kol, levyeli anahtar"),
            ("mechanism", "mekanizma"),
            ("entrap", "kapana kıstırmak"),
            ("solar", "güneşle ilgili"),
            ("twilight", "alacakaranlık")
        ],
        "sentences": [
            {
                "id": 261,
                "text": "By midday, the Time Traveller arrived once more at the colossal White Sphinx.",
                "translation": "Öğle vakti Zaman Gezgini bir kez daha devasa Beyaz Sfenks'e ulaştı.",
                "notes": "midday: öğle vakti; arrive at: -e varmak"
            },
            {
                "id": 262,
                "text": "To his utter astonishment, the bronze doors at the base of the pedestal stood wide open.",
                "translation": "Büyük bir şaşkınlıkla gördü ki, kaidenin tabanındaki bronz kapılar ardına kadar açıktı.",
                "notes": "utter astonishment: tam bir şaşkınlık; stand wide open: ardına kadar açık durmak"
            },
            {
                "id": 263,
                "text": "He looked inside and saw his Time Machine resting upon a raised platform in the chamber.",
                "translation": "İçeri baktı ve Zaman Makinesinin odadaki yükseltilmiş bir platform üzerinde durduğunu gördü.",
                "notes": "raised platform: yükseltilmiş platform; chamber: oda, bölme"
            },
            {
                "id": 264,
                "text": "The machine had been carefully cleaned and lubricated with thick oil by the Morlocks.",
                "translation": "Makine Morlocklar tarafından özenle temizlenmiş ve kalın bir yağla yağlanmıştı.",
                "notes": "lubricate: yağlamak; thick oil: kalın makine yağı"
            },
            {
                "id": 265,
                "text": "\"They think they have laid an ingenious trap for me,\" he thought with a cold smile.",
                "translation": "\"Benim için ustaca bir tuzak kurduklarını sanıyorlar,\" diye düşündü soğuk bir gülümsemeyle.",
                "notes": "ingenious trap: dahiyane tuzak; cold smile: soğuk gülümseme"
            },
            {
                "id": 266,
                "text": "He gripped his iron crowbar tightly and walked cautiously into the shadowy vault.",
                "translation": "Demir levyesini sıkıca kavradı ve temkinle gölgeli mahzene doğru yürüdü.",
                "notes": "shadowy vault: gölgeli mahzen; grip tightly: sıkıca kavramak"
            },
            {
                "id": 267,
                "text": "As soon as he stepped inside, the heavy bronze panels slammed shut with a resounding clang.",
                "translation": "İçeri adımını atar atmaz, ağır bronz paneller yankılanan bir çınlamayla kapandı.",
                "notes": "slam shut: çarparak kapanmak; resounding clang: yankılanan metalik çınlama"
            },
            {
                "id": 268,
                "text": "He was plunged into pitch darkness, and he heard the eager chuckling of Morlocks all around him.",
                "translation": "Zifiri karanlığa gömüldü ve her yanından Morlockların hevesli kıkırdamalarını duydu.",
                "notes": "pitch darkness: zifiri karanlık; eager chuckling: hevesli kıkırdama"
            },
            {
                "id": 269,
                "text": "They believed they had trapped him like an animal in a cage.",
                "translation": "Onu kafesteki bir hayvan gibi tuzağa düşürdüklerine inanıyorlardı.",
                "notes": "trap like an animal: hayvan gibi tuzağa düşürmek; cage: kafes"
            },
            {
                "id": 270,
                "text": "Unbeknownst to them, the Time Traveller had the two starting levers safe in his pocket.",
                "translation": "Onların haberi yoktu ama iki çalıştırma kolu Zaman Gezgini'nin cebinde güvendeydi.",
                "notes": "unbeknownst to: -in haberi olmadan; safe in pocket: cepte güvende"
            },
            {
                "id": 271,
                "text": "Clammy hands grabbed his ankles and tried to pull him from the saddle of the machine.",
                "translation": "Yapış yapış eller ayak bileklerini yakaladı ve onu makinenin selesinden çekmeye çalıştı.",
                "notes": "grab ankles: ayak bileklerini kavramak; saddle: sele"
            },
            {
                "id": 272,
                "text": "Fumbling in the dark, he guided the small ivory levers into their respective brass sockets.",
                "translation": "Karanlıkta el yordamıyla arayarak küçük fildişi kolları pirinç yuvalarına yerleştirdi.",
                "notes": "fumble: el yordamıyla aramak; brass sockets: pirinç yuvalar"
            },
            {
                "id": 273,
                "text": "A Morlock's hairy fingers seized his throat, choking off his breath.",
                "translation": "Bir Morlock'un kıllı parmakları boğazına sarıldı ve nefesini kesti.",
                "notes": "hairy fingers: kıllı parmaklar; choke off: boğmak"
            },
            {
                "id": 274,
                "text": "With a desperate effort, he smashed his elbow into the monster's face and wrenched the forward lever.",
                "translation": "Umutsuz bir gayretle dirseğini canavarın suratına vurdu ve ileri kolu var gücüyle çekti.",
                "notes": "smash elbow: dirsek vurmak; wrench lever: kolu hızla çekmek"
            },
            {
                "id": 275,
                "text": "Instantly, the pedestal, the chamber, and the clutching Morlocks dissolved like smoke.",
                "translation": "Anında, kaide, oda ve onu yakalamaya çalışan Morlocklar duman gibi eriyip yok oldu.",
                "notes": "dissolve like smoke: duman gibi dağılmak; clutching: yakalayan"
            },
            {
                "id": 276,
                "text": "He was flung forward once again into the rushing hurricane of temporal flight.",
                "translation": "Zaman yolculuğunun coşkun kasırgasına bir kez daha ileriye doğru fırlatıldı.",
                "notes": "temporal flight: zamansal uçuş; rushing hurricane: coşkun kasırga"
            },
            {
                "id": 277,
                "text": "In his panic and confusion, he realized that he had pushed the lever forward, toward the remote future.",
                "translation": "Panik ve kafa karışıklığı içinde, kolu ileriye, yani uzak geleceğe doğru ittiğini fark etti.",
                "notes": "confusion: kafa karışıklığı; remote future: uzak gelecek"
            },
            {
                "id": 278,
                "text": "Millions of years flew past in seconds; the sun grew larger, redder, and stopped moving across the sky.",
                "translation": "Milyonlarca yıl saniyeler içinde uçup gitti; güneş büyüdü, daha da kızıllaştı ve gökyüzünde hareket etmeyi bıraktı.",
                "notes": "grow redder: daha da kızıllaşmak; millions of years: milyonlarca yıl"
            },
            {
                "id": 279,
                "text": "The rotation of the Earth had ceased; one side faced the huge dying sun, while the other remained in eternal ice.",
                "translation": "Dünya'nın kendi etrafında dönüşü durmuştu; bir tarafı devasa can çekişen güneşe bakarken diğer tarafı ebedi buzlar içindeydi.",
                "notes": "rotation ceased: dönüşü durdu; eternal ice: sonsuz buzullar"
            },
            {
                "id": 280,
                "text": "A terrible, frozen stillness settled upon the dying world as he brought his machine to a halt.",
                "translation": "Makinesini durdurduğunda, can çekişen dünyanın üzerine korkunç, donuk bir durağanlık çöktü.",
                "notes": "frozen stillness: donuk durağanlık; bring to a halt: durdurmak"
            }
        ]
    },

    # Page 15 (Sentences 281-300)
    {
        "page_no": 15,
        "title": "The End of the World, Return to London, and the Lost Explorer",
        "tr_title": "Dünyanın Sonu, Londra'ya Dönüş ve Kayıp Kaşif",
        "vocab_focus": [
            ("desolate", "ıssız, terk edilmiş"),
            ("lichen", "liken, kaya yosunu"),
            ("monstrous", "canavarca, devasa"),
            ("eclipse", "tutulma"),
            ("reverse", "tersine çevirmek"),
            ("witness", "şahit olmak"),
            ("perpetual", "sürekli, daimi"),
            ("investigation", "araştırma, soruşturma")
        ],
        "sentences": [
            {
                "id": 281,
                "text": "The Time Traveller found himself standing upon a desolate shore thirty million years in the future.",
                "translation": "Zaman Gezgini kendisini gelecekte otuz milyon yıl sonrasının ıssız bir sahilinde dururken buldu.",
                "notes": "desolate shore: ıssız sahil; thirty million years: otuz milyon yıl"
            },
            {
                "id": 282,
                "text": "A huge, blood-red sun hung motionless in the western sky, giving off a sombre, crimson glow.",
                "translation": "Kocaman, kan kırmızısı bir güneş batı göğünde hareketsizce asılı duruyor, kasvetli, kızıl bir parıltı yayıyordu.",
                "notes": "motionless: hareketsiz; sombre crimson glow: kasvetli kızıl parıltı"
            },
            {
                "id": 283,
                "text": "The ocean was oily, lifeless, and black, barely lapping against a beach of salt and dark rock.",
                "translation": "Okyanus yağlı, cansız ve siyahtı; tuz ve koyu renkli kayalardan oluşan kumsala güçbela vuruyordu.",
                "notes": "oily and lifeless: yağlı ve cansız; lap against: kıyıya hafifçe vurmak"
            },
            {
                "id": 284,
                "text": "The only vegetation consisted of greenish lichens and giant liverworts clinging to the stones.",
                "translation": "Tek bitki örtüsü taşlara yapışmış yeşilimsi likenler ve dev ciğerotlarından ibaretti.",
                "notes": "vegetation: bitki örtüsü; lichens: likenler"
            },
            {
                "id": 285,
                "text": "Suddenly, a monstrous reddish creature like a gigantic crab with waving antennae crawled onto the shore.",
                "translation": "Aniden, antenlerini sallayan devasa bir yengece benzeyen canavarımsı kızıl bir yaratık sahile doğru süründü.",
                "notes": "gigantic crab: devasa yengeç; waving antennae: sallanan antenler"
            },
            {
                "id": 286,
                "text": "Cold flakes of snow began to drift down through the thinning, bitter atmosphere.",
                "translation": "Soğuk kar taneleri incelen, dondurucu atmosferden aşağı süzülmeye başladı.",
                "notes": "drift down: aşağı süzülmek; bitter atmosphere: dondurucu atmosfer"
            },
            {
                "id": 287,
                "text": "A dark shadow crept across the face of the dead sun: an eclipse that plunged the world into utter darkness.",
                "translation": "Ölü güneşin yüzünden karanlık bir gölge geçti: dünyayı zifiri karanlığa gömen bir tutulma.",
                "notes": "eclipse: tutulma; dead sun: sönmüş/ölü güneş"
            },
            {
                "id": 288,
                "text": "Shivering with cold and horror, he mounted his machine and pulled the lever backward toward the past.",
                "translation": "Soğuktan ve dehşetten titreyerek makinesine bindi ve kolu geçmişe doğru geriye çekti.",
                "notes": "shiver with cold: soğuktan titremek; pull lever backward: kolu geriye çekmek"
            },
            {
                "id": 289,
                "text": "The reverse flight was long and dizzying, but gradually the days and nights resumed their flickering rhythm.",
                "translation": "Geriye doğru uçuş uzun ve baş döndürücüydü fakat yavaş yavaş günler ve geceler titreşen ritimlerine yeniden kavuştu.",
                "notes": "reverse flight: geriye uçuş; resume rhythm: ritmine dönmek"
            },
            {
                "id": 290,
                "text": "Centuries and millennia unrolled backward until the walls of his familiar Richmond laboratory materialized.",
                "translation": "Yüzyıllar ve binyıllar geriye doğru açıldı, ta ki tanıdık Richmond laboratuvarının duvarları belirginleşene dek.",
                "notes": "materialize: belirmek, somutlaşmak; familiar: tanıdık"
            },
            {
                "id": 291,
                "text": "With a gentle sigh of braking metal, the Time Machine came to rest on the exact spot from which it had departed.",
                "translation": "Frenleyen metalin tatlı bir iç çekişiyle Zaman Makinesi, tam olarak ayrıldığı noktanın üzerine oturdu.",
                "notes": "come to rest: durmak; exact spot: tam nokta"
            },
            {
                "id": 292,
                "text": "He staggered out of the saddle, limped into the dining room, and found his dinner guests still waiting.",
                "translation": "Seleden sendeleyerek indi, topallayarak yemek odasına geçti ve akşam yemeği konuklarını hala beklerken buldu.",
                "notes": "limp: topallamak; dinner guests: yemek konukları"
            },
            {
                "id": 293,
                "text": "His clothes were torn and smeared with dust, and his face was drawn with unforgettable sorrow.",
                "translation": "Giysileri yırtılmış ve toza bulanmıştı, yüzü ise unutulmaz bir kederle çökmüştü.",
                "notes": "drawn with sorrow: kederle çökmüş; smeared with dust: toza bulanmış"
            },
            {
                "id": 294,
                "text": "He sat down, ate greedily, and told us the astonishing story of his voyage into the future.",
                "translation": "Masaya oturdu, açgözlülükle yemeğini yedi ve bize geleceğe yaptığı yolculuğun akıllara durgunluk veren hikayesini anlattı.",
                "notes": "eat greedily: açgözlülükle yemek; astonishing story: şaşırtıcı hikaye"
            },
            {
                "id": 295,
                "text": "Most of the guests smiled skeptically, believing it was merely an ingenious scientific romance.",
                "translation": "Konukların çoğu kuşkulu bir tebessümle gülümsedi, bunun sadece ustaca kurgulanmış bir bilim kurgu hikayesi olduğuna inandı.",
                "notes": "scientific romance: bilim kurgu öyküsü; skeptically: kuşkucu şekilde"
            },
            {
                "id": 296,
                "text": "Then the Time Traveller reached into his coat pocket and placed two strange, faded white flowers on the table.",
                "translation": "Sonra Zaman Gezgini palto cebine uzandı ve masanın üzerine iki tuhaf, solmuş beyaz çiçek bıraktı.",
                "notes": "faded flowers: solmuş çiçekler; reach into pocket: cebe uzanmak"
            },
            {
                "id": 297,
                "text": "They were the blossoms Weena had placed in his pocket: delicate flowers unknown to modern botany.",
                "translation": "Bunlar Weena'nın onun cebine koyduğu çiçeklerdi: modern botanik biliminin hiç bilmediği narin çiçekler.",
                "notes": "modern botany: çağdaş botanik bilimi; delicate blossoms: zarif çiçekler"
            },
            {
                "id": 298,
                "text": "The next afternoon, he took a knapsack and a camera, entered his laboratory, and departed once more.",
                "translation": "Ertesi öğleden sonra bir sırt çantası ve bir fotoğraf makinesi aldı, laboratuvarına girdi ve bir kez daha yola çıktı.",
                "notes": "knapsack: sırt çantası; depart once more: bir kez daha ayrılmak"
            },
            {
                "id": 299,
                "text": "Three years have passed since that day, and the Time Traveller has never returned from the mysterious currents of time.",
                "translation": "O günden bu yana üç yıl geçti ve Zaman Gezgini zamanın gizemli akıntılarından asla geri dönmedi.",
                "notes": "three years have passed: üç yıl geçti; never returned: asla dönmedi"
            },
            {
                "id": 300,
                "text": "Yet those two withered white flowers remain with me, witnessing that even when intellect fades, mutual love and gratitude endure.",
                "translation": "Yine de o iki kurumuş beyaz çiçek benimle duruyor ve zeka solup gitse bile karşılıklı sevgi ve minnettarlığın sonsuza dek yaşadığına şahitlik ediyor.",
                "notes": "withered flowers: kurumuş çiçekler; mutual love: karşılıklı sevgi; endure: sonsuza dek yaşamak"
            }
        ]
    }
]

def main():
    total_pages = len(pages_data)
    total_sentences = sum(len(p["sentences"]) for p in pages_data)
    total_vocab = sum(len(p.get("vocab_focus", [])) for p in pages_data)

    print("Book 25 Data Verification:")
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

    out_file = os.path.join(os.path.dirname(__file__), "book_25_data.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('BOOK_TITLE = "The Time Machine"\n')
        f.write('AUTHOR = "H. G. Wells"\n')
        f.write("PAGES_DATA = ")
        import pprint
        f.write(pprint.pformat(pages_data, indent=4, width=120))
        f.write("\n")

    print(f"Successfully wrote {out_file}")

if __name__ == "__main__":
    main()
