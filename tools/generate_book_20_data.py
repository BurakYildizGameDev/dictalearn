# -*- coding: utf-8 -*-
"""
Generator script for Book 20: "Treasure Island" by Robert Louis Stevenson.
15 Pages x 20 Sentences = Exactly 300 Sentences (Continuous IDs 1 to 300).
8 Vocabulary Focus items per page = Exactly 120 Target Vocabulary Items.
CEFR Level: A2-B1 Graded Reader Edition.
"""

import os

pages_data = [
    # Page 1 (Sentences 1-20)
    {
        "page_no": 1,
        "title": "The Old Sea-dog at the Admiral Benbow",
        "tr_title": "Amiral Benbow Hanındaki Yaşlı Deniz Kurdu",
        "vocab_focus": [
            ("innkeeper", "han işletmecisi, hancı"),
            ("sabre cut", "kılıç yarası / izi"),
            ("brass telescope", "pirinç dürbün"),
            ("chest", "sandık, büyük tahta kutu"),
            ("cliff", "uçurum, sarp kayalık"),
            ("seafaring", "denizci, deniz yolculuğu yapan"),
            ("dreadful", "korkunç, ürkütücü"),
            ("rum", "rom (sert denizci içkisi)")
        ],
        "sentences": [
            {
                "id": 1,
                "text": "Squire Trelawney and Dr. Livesey asked me to write down the whole story of Treasure Island.",
                "translation": "Lord Trelawney ve Doktor Livesey, Define Adası'nın tüm hikayesini baştan sona yazmamı istediler.",
                "notes": "ask someone to do something: birinden bir şey yapmasını rica etmek / istemek"
            },
            {
                "id": 2,
                "text": "My name is Jim Hawkins, and I will keep nothing back except the exact location of the island.",
                "translation": "Benim adım Jim Hawkins ve adanın tam konumu dışında hiçbir şeyi gizlemeden anlatacağım.",
                "notes": "keep back: saklamak, gizli tutmak; except: ... haricinde, dışında"
            },
            {
                "id": 3,
                "text": "The adventure began when an old seaman took up lodging at my father's inn, the Admiral Benbow.",
                "translation": "Macera, yaşlı bir denizcinin babamın işlettiği Amiral Benbow Hanı'nda konaklamaya başlamasıyla açıldı.",
                "notes": "take up lodging: konaklamak, yerleşmek; inn: han, küçük konukevi"
            },
            {
                "id": 4,
                "text": "He was a tall, heavy man with sunburnt skin and a brown pigtail hanging down his back.",
                "translation": "Güneşten yanmış teni ve sırtından aşağı sarkan kahverengi örgülü saçıyla uzun boylu, iri yapılı bir adamdı.",
                "notes": "sunburnt: güneşten yanmış; pigtail: örgü saç"
            },
            {
                "id": 5,
                "text": "A white, dirty sabre cut ran across one cheek, giving his face an angry look.",
                "translation": "Yanağını boydan boya kesen kirli beyaz bir kılıç izi, yüzüne öfkeli bir ifade veriyordu.",
                "notes": "sabre cut: kılıç yarası; cheek: yanak"
            },
            {
                "id": 6,
                "text": "Behind him, a man carried a heavy sea-chest on a wooden handbarrow.",
                "translation": "Arkasında bir adam, tahta bir el arabası üzerinde ağır bir denizci sandığı taşıyordu.",
                "notes": "sea-chest: denizci sandığı; handbarrow: el arabası"
            },
            {
                "id": 7,
                "text": "The old seaman called for a glass of rum and drank it slowly at the door.",
                "translation": "Yaşlı denizci bir kadeh rom istedi ve onu kapının önünde yavaşça yudumladı.",
                "notes": "call for: talep etmek, istemek"
            },
            {
                "id": 8,
                "text": "He looked out over the stormy sea and the lonely cliffs surrounding our cove.",
                "translation": "Fırtınalı denize ve koyumuzu çevreleyen ıssız sarp kayalıklara doğru baktı.",
                "notes": "cliffs: sarp kayalıklar, uçurumlar; cove: küçük koy, körfez"
            },
            {
                "id": 9,
                "text": "\"This is a pleasant cove,\" he said gruffly, \"and the tavern is well situated.\"",
                "translation": "\"Burası güzel bir koy,\" dedi boğuk bir sesle, \"ve meyhanenin konumu oldukça elverişli.\"",
                "notes": "gruffly: boğuk ve sert bir sesle; well situated: konumu güzel, iyi yerde"
            },
            {
                "id": 10,
                "text": "He threw down three gold pieces and told my father to call him simply Captain.",
                "translation": "Yere üç altın sikke attı ve babama kendisine yalnızca Kaptan diye hitap etmesini söyledi.",
                "notes": "throw down: fırlatıp atmak; gold piece: altın para / sikke"
            },
            {
                "id": 11,
                "text": "Every morning, he took his brass telescope and walked along the windy cliffs.",
                "translation": "Her sabah pirinç dürbününü alır ve rüzgarlı kayalıklar boyunca yürüyüşe çıkardı.",
                "notes": "brass telescope: pirinç el dürbünü; windy: rüzgarlı"
            },
            {
                "id": 12,
                "text": "All day long, he watched the horizon for passing sailing ships.",
                "translation": "Bütün gün boyunca ufukta geçen yelkenli gemileri dikkatle gözlerdi.",
                "notes": "horizon: ufuk çizgisi; sailing ship: yelkenli gemi"
            },
            {
                "id": 13,
                "text": "One evening, he promised me a silver fourpenny coin each month if I kept watch.",
                "translation": "Bir akşam, eğer etrafı gözetlersem bana her ay gümüş bir peni madeni para vereceğini vadetti.",
                "notes": "keep watch: nöbet tutmak, göz kulak olmak"
            },
            {
                "id": 14,
                "text": "\"Keep your eyes open for a seafaring man with one leg,\" he whispered darkly.",
                "translation": "\"Gözlerini dört aç ve tek bacaklı bir denizci görürsen hemen haber ver,\" diye fısıldadı karanlıkça.",
                "notes": "keep eyes open: gözünü açık tutmak; seafaring man: denizci"
            },
            {
                "id": 15,
                "text": "That one-legged sailor haunted my dreams for many terrible nights.",
                "translation": "O tek bacaklı denizci, birçok korkunç gece boyunca rüyalarıma kabus gibi girdi.",
                "notes": "haunt dreams: rüyalarına musallat olmak, kabus olmak"
            },
            {
                "id": 16,
                "text": "At night, the captain drank too much rum and sang loud sea songs.",
                "translation": "Geceleri kaptan haddinden fazla rom içer ve yüksek sesle deniz türküleri söylerdi.",
                "notes": "drink too much: aşırı içmek; sea song: gemici şarkısı"
            },
            {
                "id": 17,
                "text": "\"Fifteen men on the dead man's chest, yo-ho-ho, and a bottle of rum!\" he shouted.",
                "translation": "\"Ölü adamın sandığında on beş kişi, yo-ho-ho ve bir şişe rom!\" diye bağırırdı.",
                "notes": "dead man's chest: ölü adamın sandığı (ünlü korsan nakaratı)"
            },
            {
                "id": 18,
                "text": "The neighbors feared him, for he slammed the table and commanded silence.",
                "translation": "Komşular ondan çok korkardı çünkü masaya yumruk vurur ve herkesin susmasını emrederdi.",
                "notes": "slam the table: masaya sertçe vurmak; command: emretmek"
            },
            {
                "id": 19,
                "text": "He spoke of hanging pirates, walking the plank, and wild storms on the Spanish Main.",
                "translation": "Asılan korsanlardan, kalas üzerinde yürütülüp denize atılanlardan ve İspanyol Denizleri'ndeki vahşi fırtınalardan bahsederdi.",
                "notes": "walk the plank: korsanların esirleri denize atma cezası; Spanish Main: Karayip Denizi kıyıları"
            },
            {
                "id": 20,
                "text": "Our quiet country inn seemed turned into a dangerous pirate hideout.",
                "translation": "Bizim sakin kır hanımız adeta tehlikeli bir korsan sığınağına dönüşmüş gibiydi.",
                "notes": "turn into: ...e dönüşmek; hideout: sığınak, gizlenme yeri"
            }
        ]
    },

    # Page 2 (Sentences 21-40)
    {
        "page_no": 2,
        "title": "Black Dog and the Blind Pew",
        "tr_title": "Kara Köpek ve Kör Pew'ün Ziyareti",
        "vocab_focus": [
            ("tallowy", "solgun, donuk yağ renginde"),
            ("cutlass", "pala, kısa korsan kılıcı"),
            ("stroke", "felç, inme"),
            ("beggar", "dilenci"),
            ("stick", "baston, değnek"),
            ("creature", "yaratık, kişi"),
            ("grip", "sıkıca tutuş, kavrama"),
            ("summons", "çağrı, celp, bildiri")
        ],
        "sentences": [
            {
                "id": 21,
                "text": "One bitter winter morning, a pale stranger appeared at the door of the inn.",
                "translation": "Dondurucu bir kış sabahı, hanın kapısında solgun yüzlü bir yabancı belirdi.",
                "notes": "bitter winter: dondurucu kış; pale stranger: solgun yabancı"
            },
            {
                "id": 22,
                "text": "He had two fingers missing from his left hand and wore a heavy cutlass.",
                "translation": "Sol elinde iki parmağı eksikti ve belinde ağır bir pala taşıyordu.",
                "notes": "missing fingers: eksik parmaklar; cutlass: kısa eğri korsan kılıcı"
            },
            {
                "id": 23,
                "text": "\"Is this here table for my mate Bill?\" the stranger asked with an unpleasant grin.",
                "translation": "\"Şu masa benim eski dostum Bill için mi ayrıldı?\" diye sordu yabancı tekinsiz bir sırıtışla.",
                "notes": "mate: arkadaş, denizci yoldaşı; unpleasant grin: nahoş sırıtış"
            },
            {
                "id": 24,
                "text": "When the captain returned from his cliff walk, his face turned completely white.",
                "translation": "Kaptan kayalıklardaki yürüyüşünden döndüğünde yüzü bembeyaz kesildi.",
                "notes": "turn white: bembeyaz olmak, rengi atmak"
            },
            {
                "id": 25,
                "text": "\"Black Dog!\" cried the captain, staring in disbelief at the unwanted visitor.",
                "translation": "\"Kara Köpek!\" diye haykırdı kaptan, istenmeyen misafire şaşkınlıkla bakarak.",
                "notes": "stare in disbelief: inanamayarak dik dik bakmak"
            },
            {
                "id": 26,
                "text": "They sat down together to talk, but their voices quickly rose in furious anger.",
                "translation": "Konuşmak için birlikte oturdular ama sesleri çok geçmeden öfkeyle yükseldi.",
                "notes": "rise in anger: öfkeyle yükselmek"
            },
            {
                "id": 27,
                "text": "Suddenly, chairs crashed, steel clashed, and Black Dog ran out bleeding from his shoulder.",
                "translation": "Birdenbire sandalyeler devrildi, kılıç sesleri çınladı ve Kara Köpek omzundan kanlar akarak dışarı kaçtı.",
                "notes": "clash: çarpışmak, kılıç şakırtısı çıkarmak; bleed: kanamak"
            },
            {
                "id": 28,
                "text": "The captain stood gasping for breath, then collapsed heavily onto the wooden floor.",
                "translation": "Kaptan nefes nefese öylece kaldı, ardından tahta zemine boylu boyunca yığıldı.",
                "notes": "gasp for breath: nefes nefese kalmak; collapse: bayılmak, yığılmak"
            },
            {
                "id": 29,
                "text": "Dr. Livesey arrived just in time and warned the captain that rum was killing him.",
                "translation": "Doktor Livesey tam zamanında yetişti ve kaptanı fazla romun onu öldürmekte olduğu konusunda uyardı.",
                "notes": "in time: tam vaktinde; warn: uyarmak"
            },
            {
                "id": 30,
                "text": "\"You have suffered a stroke, Billy Bones,\" the doctor said sternly, \"and another drink will finish you.\"",
                "translation": "\"Bir felç geçirdin Billy Bones,\" dedi doktor sertçe, \"ve bir yudum daha içki senin sonun olur.\"",
                "notes": "suffer a stroke: inme / felç geçirmek; sternly: sert bir şekilde"
            },
            {
                "id": 31,
                "text": "A few days later, my poor father passed away, leaving our family in deep grief.",
                "translation": "Birkaç gün sonra zavallı babam vefat etti ve ailemizi derin bir keder içinde bıraktı.",
                "notes": "pass away: vefat etmek; deep grief: derin keder / yas"
            },
            {
                "id": 32,
                "text": "On the afternoon of the funeral, a blind man came tapping his stick up the frozen road.",
                "translation": "Cenazenin olduğu günün öğleden sonrasında, kör bir adam donmuş yolda bastonunu tıkırdatarak çıkageldi.",
                "notes": "tap a stick: bastonu yere vurmak; funeral: cenaze töreni"
            },
            {
                "id": 33,
                "text": "He wore a tattered sea-cloak and had a cloth bound over his sightless eyes.",
                "translation": "Eski püskü bir denizci pelerini giymişti ve görmeyen gözlerinin üzerine bir bez sarılmıştı.",
                "notes": "tattered: yırtık pırtık; sightless: kör, görmeyen"
            },
            {
                "id": 34,
                "text": "\"Will any kind friend tell a poor blind man where he has arrived?\" he begged.",
                "translation": "\"Yardımsever bir dost, zavallı bir kör adama nereye vardığını söyler mi acaba?\" diye yalvardı.",
                "notes": "kind friend: iyi kalpli dost; beg: yalvarmak, dilenmek"
            },
            {
                "id": 35,
                "text": "I offered him my hand, but his cold fingers closed around my wrist like iron pincers.",
                "translation": "Ona elimi uzattım fakat soğuk parmakları bileğimi demir bir kıskaç gibi kavradı.",
                "notes": "iron pincers: demir kıskaç; wrist: el bileği"
            },
            {
                "id": 36,
                "text": "\"Lead me straight to the captain, boy, or I will break your arm!\" he hissed.",
                "translation": "\"Beni doğrudan kaptana götür çocuk, yoksa kolunu kırarım!\" diye tısladı.",
                "notes": "lead: yol göstermek, götürmek; hiss: tıslamak, fısıldamak"
            },
            {
                "id": 37,
                "text": "Terrified, I obeyed and led the blind monster into the room where Bones lay weak.",
                "translation": "Dehşete kapılmış halde boyun eğdim ve kör canavarı Bones'un bitkin yattığı odaya soktum.",
                "notes": "terrified: dehşete düşmüş; obey: itaat etmek"
            },
            {
                "id": 38,
                "text": "The blind beggar pressed a small piece of dark paper into the captain's trembling palm.",
                "translation": "Kör dilenci, kaptanın titreyen avucuna küçük koyu renkli bir kağıt parçası sıkıştırdı.",
                "notes": "trembling palm: titreyen avuç içi; press into: eline tutuşturmak"
            },
            {
                "id": 39,
                "text": "\"Now that is done!\" the blind creature cried, turning and vanishing into the foggy mist.",
                "translation": "\"İşte bu iş tamam!\" diye bağırdı kör mahluk ve dönüp sislerin arasında kayboldu.",
                "notes": "vanish: gözden kaybolmak; foggy mist: sisli pus"
            },
            {
                "id": 40,
                "text": "The captain looked at the paper, whispered 'The Black Spot!', and fell dead upon the floor.",
                "translation": "Kaptan kağıda baktı, 'Kara Leke!' diye fısıldadı ve zemine cansız bir şekilde yığıldı.",
                "notes": "The Black Spot: Kara Leke (korsanların ölüm fermanı işareti); fall dead: cansız yere düşmek"
            }
        ]
    },

    # Page 3 (Sentences 41-60)
    {
        "page_no": 3,
        "title": "The Sea-chest and the Map",
        "tr_title": "Kaptanın Sandığı ve Gizemli Harita",
        "vocab_focus": [
            ("key", "anahtar"),
            ("oilcloth", "muşamba, su geçirmez kumaş"),
            ("packet", "paket, deste"),
            ("bullion", "külçe altın"),
            ("haste", "acele, telaş"),
            ("footsteps", "ayak sesleri"),
            ("culvert", "menfez, köprü altı su yolu"),
            ("pistol", "tabanca")
        ],
        "sentences": [
            {
                "id": 41,
                "text": "My mother and I knew that the dead pirate's crew would come back to search the inn.",
                "translation": "Annem ve ben, ölü korsanın tayfasının hanı aramak için geri döneceğini biliyorduk.",
                "notes": "crew: mürettebat, çete; search: aramak, didik didik etmek"
            },
            {
                "id": 42,
                "text": "We ran through the cold fog to the nearby hamlet to ask the villagers for help.",
                "translation": "Köylülerden yardım istemek için soğuk sisin içinden yakındaki mezraya koştuk.",
                "notes": "hamlet: küçük köy, mezra; villager: köylü"
            },
            {
                "id": 43,
                "text": "Nobody had the courage to return with us, for the terrifying name of Captain Flint ruled the coast.",
                "translation": "Kimse bizimle geri dönecek cesarete sahip değildi çünkü Kaptan Flint'in ürkütücü adı tüm kıyıya korku salıyordu.",
                "notes": "courage: cesaret; rule the coast: kıyıya hükmetmek"
            },
            {
                "id": 44,
                "text": "However, one brave boy agreed to ride to Dr. Livesey's house to bring armed soldiers.",
                "translation": "Yine de cesur bir genç, silahlı askerleri çağırmak üzere Doktor Livesey'in evine at sürmeyi kabul etti.",
                "notes": "armed soldiers: silahlı askerler; ride: at sürmek"
            },
            {
                "id": 45,
                "text": "My mother insisted on taking only the exact tavern money that Billy Bones owed us.",
                "translation": "Annem sadece Billy Bones'un bize borçlu olduğu tam han parasını almakta ısrar etti.",
                "notes": "insist on: ...de ısrar etmek; owe: borçlu olmak"
            },
            {
                "id": 46,
                "text": "We returned alone to the silent inn and locked the front door behind us.",
                "translation": "Sessiz hana tek başımıza geri döndük ve arkamızdan ön kapıyı sürgüledik.",
                "notes": "lock the door: kapıyı kilitlemek / sürgülemek"
            },
            {
                "id": 47,
                "text": "I searched the dead captain's coat and found a small iron key hanging on a piece of string.",
                "translation": "Ölü kaptanın ceketini aradım ve bir ipe asılı küçük bir demir anahtar buldum.",
                "notes": "iron key: demir anahtar; string: ip, sicim"
            },
            {
                "id": 48,
                "text": "Upstairs, we unlocked the heavy sea-chest and lifted its lid with trembling fingers.",
                "translation": "Üst katta, ağır denizci sandığının kilidini açtık ve kapağını titreyen parmaklarla kaldırdık.",
                "notes": "unlock: kilidini açmak; lift lid: kapağını kaldırmak"
            },
            {
                "id": 49,
                "text": "Inside lay a clean suit of clothes, compasses, tobacco, and two fine silver-mounted pistols.",
                "translation": "İçinde temiz bir takım elbise, pusulalar, tütün ve gümüş işlemeli iki güzel tabanca vardı.",
                "notes": "compass: pusula; silver-mounted: gümüş kaplamalı / işlemeli"
            },
            {
                "id": 50,
                "text": "Beneath a bundle of old foreign coins, I noticed a bundle wrapped tightly in waterproof oilcloth.",
                "translation": "Eski yabancı sikkelerden oluşan bir çıkının altında, su geçirmez muşambaya sıkıca sarılmış bir paket fark ettim.",
                "notes": "oilcloth: muşamba, su geçirmez kumaş; bundle: deste, paket"
            },
            {
                "id": 51,
                "text": "As my mother slowly counted out our rent, a low whistle echoed along the road outside.",
                "translation": "Annem yavaşça kira alacağımızı sayarken, dışarıdaki yol boyunca alçak bir ıslık sesi yankılandı.",
                "notes": "count out: sayarak ayırmak; whistle: ıslık sesi"
            },
            {
                "id": 52,
                "text": "It was the pirate signal warning that danger was approaching fast.",
                "translation": "Bu, tehlikenin hızla yaklaşmakta olduğunu bildiren bir korsan işaretiydi.",
                "notes": "signal: işaret, parola; approach: yaklaşmak"
            },
            {
                "id": 53,
                "text": "I seized the oilcloth packet and pushed my mother out into the dark night.",
                "translation": "Muşamba paketi kaptım ve annemi aceleyle karanlık geceye doğru dışarı çıkardım.",
                "notes": "seize: kapmak, yakalamak; dark night: karanlık gece"
            },
            {
                "id": 54,
                "text": "We hid beneath a small stone bridge in the darkness, trembling in terror.",
                "translation": "Karanlıkta küçük taş bir köprünün altına saklandık, dehşet içinde titriyorduk.",
                "notes": "hide beneath: altında saklanmak; tremble: titremek"
            },
            {
                "id": 55,
                "text": "Seven or eight rough men rushed up with lanterns, smashing into the empty inn.",
                "translation": "Fenerli yedi sekiz kaba adam hana daldı ve boş binayı yerle bir etmeye başladı.",
                "notes": "rough men: kaba / tekinsiz adamlar; smash into: zorla / kırarak içeri girmek"
            },
            {
                "id": 56,
                "text": "\"Bill is dead!\" a voice shouted from upstairs, \"and someone has turned the chest inside out!\"",
                "translation": "\"Bill ölmüş!\" diye bağırdı üst kattan bir ses, \"ve birisi sandığı altüst etmiş!\"",
                "notes": "turn inside out: altını üstüne getirmek, didik didik etmek"
            },
            {
                "id": 57,
                "text": "\"Find the boy and the packet, you fools!\" screamed the blind man Pew in fury.",
                "translation": "\"Çocuğu ve paketi bulun aptallar!\" diye öfkeyle haykırdı kör adam Pew.",
                "notes": "fool: aptal; in fury: büyük bir öfke içinde"
            },
            {
                "id": 58,
                "text": "At that moment, the galloping sound of horses signaled the arrival of the revenue officers.",
                "translation": "Tam o anda, atların dörtnala gelen sesleri sahil muhafaza süvarilerinin gelişini müjdeledi.",
                "notes": "galloping sound: dörtnal sesleri; revenue officers: gümrük / sahil muhafaza subayları"
            },
            {
                "id": 59,
                "text": "The pirates scattered into the darkness, leaving blind Pew behind to be trampled under horses' hooves.",
                "translation": "Korsanlar karanlığa dağılıp kaçtılar ve kör Pew'ü atların nalları altında ezilmek üzere geride bıraktılar.",
                "notes": "scatter: dağılmak, kaçışmak; trample: ayaklar altında ezmek"
            },
            {
                "id": 60,
                "text": "I was safe, and in my pocket I still held the mysterious oilcloth packet.",
                "translation": "Artık güvendeydim ve cebimde hala o gizemli muşamba paketi tutuyordum.",
                "notes": "mysterious: gizemli; safe: güvende"
            }
        ]
    },

    # Page 4 (Sentences 61-80)
    {
        "page_no": 4,
        "title": "The Journey to Bristol and Squire Trelawney",
        "tr_title": "Bristol Yolculuğu ve Hazırlıklar",
        "vocab_focus": [
            ("squire", "bey, soylu toprak sahibi"),
            ("estate", "malikane, mülk"),
            ("parchment", "parşömen kağıdı"),
            ("latitude", "enlem"),
            ("longitude", "boylam"),
            ("clerk", "katip, memur"),
            ("schooner", "uskuna (iki direkli hızlı yelkenli)"),
            ("treasure", "hazine")
        ],
        "sentences": [
            {
                "id": 61,
                "text": "The revenue officers escorted me to Dr. Livesey's handsome country house.",
                "translation": "Gümrük muhafızları bana Doktor Livesey'in görkemli kır evine kadar eşlik ettiler.",
                "notes": "escort: refakat etmek, eşlik etmek; handsome house: gösterişli / güzel ev"
            },
            {
                "id": 62,
                "text": "Squire Trelawney was dining with the doctor when I entered the warm library.",
                "translation": "Sıcak kütüphaneye girdiğimde Lord Trelawney doktorla birlikte akşam yemeği yiyordu.",
                "notes": "dine: akşam yemeği yemek; library: kütüphane, çalışma odası"
            },
            {
                "id": 63,
                "text": "The squire was a tall, handsome gentleman over six feet with a fiery red face.",
                "translation": "Lord, ateş kırmızısı yüzüyle boyu bir seksenin üzerinde olan uzun boylu, yakışıklı bir beyefendiydi.",
                "notes": "fiery: ateş gibi; gentleman: beyefendi"
            },
            {
                "id": 64,
                "text": "I laid the oilcloth packet upon the mahogany table before them.",
                "translation": "Muşamba paketi önlerindeki maun masanın üzerine bıraktım.",
                "notes": "lay upon: üzerine koymak; mahogany: maun ağacı"
            },
            {
                "id": 65,
                "text": "Dr. Livesey carefully cut the stitches with his medical scissors.",
                "translation": "Doktor Livesey cerrahi makasıyla dikişleri dikkatlice kesti.",
                "notes": "stitches: dikişler; medical scissors: tıbbi makas"
            },
            {
                "id": 66,
                "text": "Inside, we discovered an old logbook and a folded sheet of yellowed parchment.",
                "translation": "İçinde eski bir seyir defteri ve katlanmış bir sararmış parşömen tabakası bulduk.",
                "notes": "logbook: seyir defteri; yellowed parchment: sararmış parşömen kağıdı"
            },
            {
                "id": 67,
                "text": "The doctor spread the parchment under the bright candlelight.",
                "translation": "Doktor parşömeni parlak mum ışığının altına serdi.",
                "notes": "spread: sermek, yaymak; candlelight: mum ışığı"
            },
            {
                "id": 68,
                "text": "It was an accurate map of an unknown island, complete with latitude and longitude.",
                "translation": "Bu, enlem ve boylamı eksiksiz belirtilmiş, bilinmeyen bir adanın kusursuz bir haritasıydı.",
                "notes": "accurate map: hatasız harita; latitude: enlem; longitude: boylam"
            },
            {
                "id": 69,
                "text": "Three red ink crosses marked anchorages, hills, and hidden caves.",
                "translation": "Kırmızı mürekkeple çizilmiş üç haç; demirleme yerlerini, tepeleri ve gizli mağaraları işaretliyordu.",
                "notes": "anchorage: demirleme yeri; ink cross: mürekkep haç işareti"
            },
            {
                "id": 70,
                "text": "Beside one cross were the words: 'Bulk of treasure here, buried by J. Flint.'",
                "translation": "Haçlardan birinin yanında şu sözler yazılıydı: 'Hazinenin büyük kısmı burada, J. Flint tarafından gömüldü.'",
                "notes": "bulk of: ...in büyük kısmı; bury: gömmek"
            },
            {
                "id": 71,
                "text": "\"Livesey!\" cried the squire, springing from his chair, \"we will sail to Bristol tomorrow!\"",
                "translation": "\"Livesey!\" diye bağırdı lord sandalyesinden fırlayarak, \"yarın hemen Bristol'e yelken açıyoruz!\"",
                "notes": "spring from: ...den fırlamak; sail: denize açılmak"
            },
            {
                "id": 72,
                "text": "\"I will buy the finest ship in dock and hire the bravest crew in England!\"",
                "translation": "\"Limandaki en mükemmel gemiyi satın alacak ve İngiltere'nin en cesur mürettebatını kiralayacağım!\"",
                "notes": "dock: tersane, rıhtım; hire: kiralamak, işe almak"
            },
            {
                "id": 73,
                "text": "\"Jim Hawkins shall come as our cabin boy, and you shall be the ship's doctor.\"",
                "translation": "\"Jim Hawkins kamarotumuz olarak gelecek, siz de gemi hekimi olacaksınız.\"",
                "notes": "cabin boy: gemi miçosu / kamarotu; ship's doctor: gemi doktoru"
            },
            {
                "id": 74,
                "text": "The doctor agreed, but gave one stern warning to the excited nobleman.",
                "translation": "Doktor kabul etti ancak heyecanlı soyluya çok sert bir uyarıda bulundu.",
                "notes": "stern warning: ciddi / sert uyarı; nobleman: soylu adam"
            },
            {
                "id": 75,
                "text": "\"You have only one weakness, Trelawney: you cannot hold your tongue.\"",
                "translation": "\"Tek bir zayıflığın var Trelawney: dilini tutmayı hiç beceremiyorsun.\"",
                "notes": "hold one's tongue: dilini tutmak, sır saklamak"
            },
            {
                "id": 76,
                "text": "\"Those pirates want this map, and we must not let a soul know our destination.\"",
                "translation": "\"O korsanlar bu haritanın peşinde, bu yüzden varış noktamızı tek bir ruha bile sezdirmemeliyiz.\"",
                "notes": "destination: varış yeri; not let a soul know: kimseye hissettirmemek"
            },
            {
                "id": 77,
                "text": "The squire swore he would be as silent as the grave.",
                "translation": "Lord mezar kadar sessiz olacağına dair yeminler etti.",
                "notes": "swear: yemin etmek; silent as the grave: mezar gibi sessiz"
            },
            {
                "id": 78,
                "text": "Weeks passed while Trelawney went ahead to Bristol to prepare our expedition.",
                "translation": "Trelawney keşif gezimizi hazırlamak için önden Bristol'e giderken aradan haftalar geçti.",
                "notes": "expedition: keşif seferi; go ahead: önden gitmek"
            },
            {
                "id": 79,
                "text": "Finally, a letter arrived saying he had purchased a splendid schooner called the Hispaniola.",
                "translation": "Sonunda, Hispaniola adında muazzam bir uskuna satın aldığını bildiren bir mektup ulaştı.",
                "notes": "splendid schooner: harika iki direkli yelkenli gemi; purchase: satın almak"
            },
            {
                "id": 80,
                "text": "I said goodbye to my dear mother and set out eagerly for the bustling port of Bristol.",
                "translation": "Sevgili anneme veda ettim ve heyecanla Bristol'ün hareketli limanına doğru yola çıktım.",
                "notes": "bustling port: işlek / hareketli liman; set out: yola koyulmak"
            }
        ]
    },

    # Page 5 (Sentences 81-100)
    {
        "page_no": 5,
        "title": "The Hispaniola and Long John Silver",
        "tr_title": "Hispaniola Gemisi ve Uzun John Silver",
        "vocab_focus": [
            ("crutch", "koltuk değneği"),
            ("parrot", "papağan"),
            ("tavern", "meyhane"),
            ("cook", "aşçı"),
            ("wharf", "rıhtım, iskele"),
            ("rigging", "donanım, gemi halatları"),
            ("clever", "zeki, kurnaz"),
            ("shrewd", "açıkgöz, kurnaz")
        ],
        "sentences": [
            {
                "id": 81,
                "text": "Bristol harbor was filled with great sailing vessels, tall masts, and smelling of tar and salt.",
                "translation": "Bristol limanı ulu yelkenli teknelerle, yüksek direklerle doluydu; katran ve tuz kokuyordu.",
                "notes": "vessel: gemi, tekne; tar: katran; mast: gemi direği"
            },
            {
                "id": 82,
                "text": "Squire Trelawney sent me with a note to the Spy-glass tavern near the docks.",
                "translation": "Lord Trelawney, rıhtımın yanındaki Dürbün Meyhanesi'ne bir not iletmem için beni gönderdi.",
                "notes": "Spy-glass: el dürbünü; dock: rıhtım"
            },
            {
                "id": 83,
                "text": "He told me the tavern was kept by Long John Silver, whom he had hired as ship's cook.",
                "translation": "Bana meyhanenin, gemiye aşçı olarak tuttuğu Uzun John Silver tarafından işletildiğini söyledi.",
                "notes": "hire as: ... olarak işe almak; ship's cook: gemi aşçısı"
            },
            {
                "id": 84,
                "text": "I remembered the one-legged pirate Billy Bones had warned me about and felt nervous.",
                "translation": "Billy Bones'un beni uyardığı tek bacaklı korsanı hatırladım ve tedirgin oldum.",
                "notes": "feel nervous: tedirgin / endişeli hissetmek"
            },
            {
                "id": 85,
                "text": "When I entered, a tall man hopped briskly across the floor on a crutch.",
                "translation": "İçeri girdiğimde, uzun boylu bir adam koltuk değneği üzerinde zeminde çevikçe sekiyordu.",
                "notes": "hop briskly: çevikçe sekmek; crutch: koltuk değneği"
            },
            {
                "id": 86,
                "text": "His left leg was cut off close by the hip, but he moved with astonishing agility.",
                "translation": "Sol bacağı kalçaya yakın yerden kesilmişti fakat şaşırtıcı bir çeviklikle hareket ediyordu.",
                "notes": "cut off: kesilmiş; agility: çeviklik, kıvraklık"
            },
            {
                "id": 87,
                "text": "His face was large, intelligent, and smiling warmly at every customer.",
                "translation": "Geniş, zeki bir yüzü vardı ve her müşteriye sıcacık gülümsüyordu.",
                "notes": "smile warmly: içtenlikle gülümsemek"
            },
            {
                "id": 88,
                "text": "He read the squire's letter, shook my hand warmly, and praised my courage.",
                "translation": "Lordun mektubunu okudu, elimi samimiyetle sıktı ve cesaretimi övdü.",
                "notes": "shake hand: el sıkışmak; praise: övmek"
            },
            {
                "id": 89,
                "text": "Just then, a customer in the corner jumped up and bolted out the back door.",
                "translation": "Tam o sırada köşedeki bir müşteri fırlayıp arka kapıdan dışarı kaçtı.",
                "notes": "bolt out: fırlayıp kaçmak; corner: köşe"
            },
            {
                "id": 90,
                "text": "\"Stop him!\" I shouted, \"that is Black Dog, the man who attacked Captain Bones!\"",
                "translation": "\"Durdurun onu!\" diye bağırdım, \"bu Kaptan Bones'a saldıran Kara Köpek'in ta kendisi!\"",
                "notes": "attack: saldırmak; stop someone: birini durdurmak"
            },
            {
                "id": 91,
                "text": "Silver seemed deeply shocked and sent two men running down the street to catch the thief.",
                "translation": "Silver derinden sarsılmış göründü ve hırsızı yakalamak için sokağa koşan iki adam gönderdi.",
                "notes": "shocked: sarsılmış, şoke olmuş; catch: yakalamak"
            },
            {
                "id": 92,
                "text": "The men returned empty-handed, claiming Black Dog had vanished into the maze of alleys.",
                "translation": "Adamlar elleri boş döndüler ve Kara Köpek'in ara sokakların labirentinde kaybolduğunu iddia ettiler.",
                "notes": "empty-handed: eli boş; maze of alleys: ara sokaklar labirenti"
            },
            {
                "id": 93,
                "text": "Silver walked with me to the quay, laughing and telling pleasant sea stories.",
                "translation": "Silver rıhtıma kadar benimle yürüdü, gülüyor ve neşeli deniz hikayeleri anlatıyordu.",
                "notes": "quay: rıhtım, iskele; pleasant: hoş, neşeli"
            },
            {
                "id": 94,
                "text": "He seemed so cheerful and honest that all my suspicions melted away.",
                "translation": "O kadar neşeli ve dürüst görünüyordu ki bütün şüphelerim tamamen eriyip gitti.",
                "notes": "suspicion: şüphe; melt away: eriyip yok olmak"
            },
            {
                "id": 95,
                "text": "At the wharf, we rowed out to inspect the beautiful Hispaniola.",
                "translation": "Rıhtımda, güzel Hispaniola'yı denetlemek için kürek çekerek açıldık.",
                "notes": "row out: kürekle açılmak; inspect: denetlemek, incelemek"
            },
            {
                "id": 96,
                "text": "Captain Smollett, our ship's captain, was standing by the helm with a gloomy expression.",
                "translation": "Gemi kaptanımız Kaptan Smollett, dümende asık bir yüz ifadesiyle bekliyordu.",
                "notes": "helm: dümen; gloomy expression: kasvetli / asık surat"
            },
            {
                "id": 97,
                "text": "\"I do not like this cruise, sir,\" Captain Smollett told Trelawney plainly.",
                "translation": "\"Ben bu seferi hiç beğenmedim efendim,\" dedi Kaptan Smollett açık sözlülükle.",
                "notes": "plainly: açıkça; cruise: deniz seferi, yolculuk"
            },
            {
                "id": 98,
                "text": "\"I do not like the men, and I do not like treasure voyages where secrets leak.\"",
                "translation": "\"Mürettebatı tutmadım ve sırların etrafa saçıldığı hazine yolculuklarından hiç hoşlanmam.\"",
                "notes": "leak: sızmak, yayılmak; treasure voyage: hazine seferi"
            },
            {
                "id": 99,
                "text": "Trelawney was furious with the honest captain, but Dr. Livesey urged caution.",
                "translation": "Trelawney dürüst kaptana çok öfkelendi fakat Doktor Livesey temkinli davranılmasını istedi.",
                "notes": "furious: çok öfkeli; urge caution: temkinli olmayı öğütlemek"
            },
            {
                "id": 100,
                "text": "We weighed anchor that very night, beginning our perilous voyage across the Atlantic.",
                "translation": "Tam o gece demir aldık ve Atlantik boyunca uzanacak tehlikeli yolculuğumuza başladık.",
                "notes": "weigh anchor: demir almak; perilous voyage: tehlikeli yolculuk"
            }
        ]
    },

    # Page 6 (Sentences 101-120)
    {
        "page_no": 6,
        "title": "The Voyage Across the Ocean",
        "tr_title": "Okyanus Boyunca Tehlikeli Sefer",
        "vocab_focus": [
            ("galley", "gemi mutfağı"),
            ("lanyard", "askı ipi, bağlama kordonu"),
            ("cask", "fıçı"),
            ("barrel", "namlu / ahşap fıçı"),
            ("quartermaster", "levazım reisi, dümenci subayı"),
            ("grog", "suyla seyreltilmiş rom"),
            ("buoyant", "su üstünde durabilen, batmaz"),
            ("mate", "ikinci kaptan, gemi zabiti")
        ],
        "sentences": [
            {
                "id": 101,
                "text": "The Hispaniola proved to be a fast and seaworthy vessel in heavy weather.",
                "translation": "Hispaniola, sert havalarda hızlı ve denize son derece elverişli bir tekne olduğunu kanıtladı.",
                "notes": "seaworthy: denize dayanıklı; heavy weather: fırtınalı hava"
            },
            {
                "id": 102,
                "text": "The crew worked well, and nobody worked harder or more cheerfully than Long John Silver.",
                "translation": "Mürettebat gayet iyi çalışıyordu ve hiç kimse Uzun John Silver'dan daha sıkı veya neşeli çalışmıyordu.",
                "notes": "cheerfully: neşeyle; work hard: sıkı çalışmak"
            },
            {
                "id": 103,
                "text": "He kept his galley spotless and had a lanyard tied around his neck to secure his crutch.",
                "translation": "Gemi mutfağını tertemiz tutuyor ve koltuk değneğini sabitlemek için boynuna bir kordon bağlıyordu.",
                "notes": "galley: gemi mutfağı; spotless: lekesiz, tertemiz"
            },
            {
                "id": 104,
                "text": "A large green parrot sat on his shoulder, shouting: \"Pieces of eight! Pieces of eight!\"",
                "translation": "Omzunda oturan iri yeşil bir papağan: \"Sekiz parçalık altınlar! Sekiz parçalıklar!\" diye bağırıyordu.",
                "notes": "pieces of eight: İspanyol gümüş riyali / korsan parası; parrot: papağan"
            },
            {
                "id": 105,
                "text": "\"This bird is two hundred years old, Jim,\" Silver told me with a wink.",
                "translation": "\"Bu kuş iki yüz yaşında Jim,\" dedi Silver bana göz kırparak.",
                "notes": "wink: göz kırpmak"
            },
            {
                "id": 106,
                "text": "\"She sailed with the famous Captain Flint and knows all the pirate secrets.\"",
                "translation": "\"Ünlü Kaptan Flint'le yelken açtı ve bütün korsan sırlarını bilir.\"",
                "notes": "sail with: birlikte yelken açmak; pirate secrets: korsan sırları"
            },
            {
                "id": 107,
                "text": "Silver always had a kind word and a sweet pastry for me whenever I visited the galley.",
                "translation": "Mutfak bölümüne ne zaman uğrasam Silver bana daima tatlı bir söz söyler ve lezzetli bir çörek verirdi.",
                "notes": "kind word: tatlı / nazik söz; pastry: hamur işi, çörek"
            },
            {
                "id": 108,
                "text": "All the sailors respected him, calling him 'Barbecue' in affectionate sailor slang.",
                "translation": "Tüm denizciler ona saygı duyar, sevecen denizci argosuyla 'Barbekü' diye seslenirlerdi.",
                "notes": "affectionate: sevecen; slang: argo"
            },
            {
                "id": 109,
                "text": "Our first mate, Mr. Arrow, was quite useless and drank constantly from a private bottle.",
                "translation": "İkinci kaptanımız Bay Arrow ise tamamen işe yaramazdı ve gizli şişesinden durmadan içki içerdi.",
                "notes": "first mate: süvari / ikinci kaptan; useless: işe yaramaz"
            },
            {
                "id": 110,
                "text": "One dark and stormy night, Mr. Arrow mysteriously vanished overboard into the churning sea.",
                "translation": "Karanlık ve fırtınalı bir gece, Bay Arrow esrarengiz bir şekilde güverteden azgın denize düşüp kayboldu.",
                "notes": "vanish overboard: güverteden denize düşüp kaybolmak; churning: çalkantılı, azgın"
            },
            {
                "id": 111,
                "text": "Job Anderson, the boatswain, took his place and proved to be much more capable.",
                "translation": "Lostromo Job Anderson onun yerini aldı ve çok daha yetenekli olduğunu gösterdi.",
                "notes": "boatswain: lostromo (güverte reisi); capable: yetenekli, becerikli"
            },
            {
                "id": 112,
                "text": "Squire Trelawney was delighted with the voyage and provided a barrel of fresh apples on deck.",
                "translation": "Lord Trelawney yolculuktan son derece memnundu ve güverteye taze elmalarla dolu bir fıçı koydurdu.",
                "notes": "delighted: çok memnun; barrel: ahşap fıçı"
            },
            {
                "id": 113,
                "text": "Any sailor could help himself to an apple whenever he pleased.",
                "translation": "Her denizci dilediği zaman oradan bir elma alıp yiyebiliyordu.",
                "notes": "help oneself: çekinmeden almak; pleased: arzu etmek"
            },
            {
                "id": 114,
                "text": "This apple barrel proved to be the salvation of all our lives.",
                "translation": "İşte bu elma fıçısı, ileride hepimizin hayatının kurtuluşu olacaktı.",
                "notes": "salvation: kurtuluş, kurtarma"
            },
            {
                "id": 115,
                "text": "The trade winds carried us smoothly south towards our hidden island.",
                "translation": "Alize rüzgarları bizi güneye, gizli adamıza doğru pürüzsüzce taşıdı.",
                "notes": "trade winds: alize rüzgarları; smoothly: sarsıntısız, rahatça"
            },
            {
                "id": 116,
                "text": "The moon shone brightly upon the rolling waves each clear tropical night.",
                "translation": "Her açık tropikal gecede ay, kabaran dalgaların üzerine pırıl pırıl vuruyordu.",
                "notes": "shine brightly: parlak ışıldamak; rolling waves: dalgalı deniz"
            },
            {
                "id": 117,
                "text": "Yet Captain Smollett remained watchful, trusting neither the weather nor his crew.",
                "translation": "Yine de Kaptan Smollett tetikte kalmayı sürdürdü; ne havaya ne de mürettebatına güveniyordu.",
                "notes": "watchful: tetikte; trust: güvenmek"
            },
            {
                "id": 118,
                "text": "\"A voyage is not finished until the anchor drops in home port,\" he told the doctor.",
                "translation": "\"Bir sefer, demir ana limana atılana kadar asla bitmiş sayılmaz,\" dedi doktora.",
                "notes": "home port: ana liman; drop anchor: demir atmak"
            },
            {
                "id": 119,
                "text": "We calculated that land would be sighted within the next twenty-four hours.",
                "translation": "Önümüzdeki yirmi dört saat içinde karanın görüleceğini hesaplamıştık.",
                "notes": "sight land: karayı görmek; calculate: hesaplamak"
            },
            {
                "id": 120,
                "text": "Everyone on board was eager and excited for the grand adventure to begin.",
                "translation": "Gemideki herkes büyük maceranın başlaması için son derece sabırsız ve heyecanlıydı.",
                "notes": "on board: gemide; eager: hevesli, sabırsız"
            }
        ]
    },

    # Page 7 (Sentences 121-140)
    {
        "page_no": 7,
        "title": "The Secret in the Apple Barrel",
        "tr_title": "Elma Fıçısındaki İhanet İtirafı",
        "vocab_focus": [
            ("barrel", "fıçı"),
            ("overhear", "kulak misafiri olmak"),
            ("mutiny", "gemide isyan"),
            ("plot", "komplo, tuzak"),
            ("traitor", "hain"),
            ("gentlemen of fortune", "talih şövalyeleri (korsanlar)"),
            ("whisper", "fısıltı"),
            ("throat", "boğaz")
        ],
        "sentences": [
            {
                "id": 121,
                "text": "Just after sunset on the last day of the voyage, I wanted an apple to eat.",
                "translation": "Yolculuğun son gününde gün batımından hemen sonra yemek için bir elma canım çekti.",
                "notes": "sunset: gün batımı; want to eat: yemek istemek"
            },
            {
                "id": 122,
                "text": "The barrel on the waist was nearly empty, so I climbed right inside it.",
                "translation": "Güvertedeki fıçı neredeyse boştu, bu yüzden içine kadar tırmandım.",
                "notes": "climb inside: içine tırmanıp girmek; empty: boş"
            },
            {
                "id": 123,
                "text": "I sat in the dark wood bottom, eating my apple and rocking with the ship.",
                "translation": "Karanlık tahta dipte oturdum, elmamı yiyerek geminin sallantısıyla beşik gibi sallandım.",
                "notes": "rock with: ...ile sallanmak; dark bottom: karanlık dip"
            },
            {
                "id": 124,
                "text": "Before I could climb out, a heavy man sat down against the barrel.",
                "translation": "Dışarı çıkamadan önce ağır bir adam fıçının kenarına yaslanıp oturdu.",
                "notes": "climb out: tırmanarak çıkmak; sit against: dayanıp oturmak"
            },
            {
                "id": 125,
                "text": "The barrel shook, and I heard Long John Silver begin speaking in a low voice.",
                "translation": "Fıçı sarsıldı ve Uzun John Silver'ın alçak bir sesle konuşmaya başladığını duydum.",
                "notes": "shake: sarsılmak; low voice: alçak ses"
            },
            {
                "id": 126,
                "text": "\"Flint was captain, and I was quartermaster along of my timber leg,\" Silver said.",
                "translation": "\"Kaptan Flint'ti, tahta bacağıma rağmen ben de onun levazım reisiydim,\" dedi Silver.",
                "notes": "timber leg: tahta bacak; quartermaster: dümenci reisi / serdümen"
            },
            {
                "id": 127,
                "text": "He was persuading young Dick, our youngest sailor, to join a mutiny.",
                "translation": "En genç denizcimiz olan delikanlı Dick'i isyana katılmaya ikna etmeye çalışıyordu.",
                "notes": "persuade: ikna etmek; join a mutiny: isyana katılmak"
            },
            {
                "id": 128,
                "text": "\"You will get your share of the gold and live like a lord,\" the cook promised.",
                "translation": "\"Altından payını alacak ve bir lord gibi krallar gibi yaşayacaksın,\" diye söz verdi aşçı.",
                "notes": "share: hisse, pay; live like a lord: bey gibi yaşamak"
            },
            {
                "id": 129,
                "text": "\"What do we do with Captain Smollett and the squire?\" asked another sailor named Hands.",
                "translation": "\"Peki Kaptan Smollett ile lordu ne yapacağız?\" diye sordu Hands adındaki diğer bir gemici.",
                "notes": "what do we do with: ...i ne yapacağız?"
            },
            {
                "id": 130,
                "text": "\"Dead men don't bite,\" Silver answered coldly with a terrifying chuckle.",
                "translation": "\"Ölü adamlar ısırmaz,\" diye yanıtladı Silver buz gibi, korkunç bir kıkırdamayla.",
                "notes": "dead men don't bite: ölü adam ısırmaz (korsan atasözü); chuckle: bıyık altından gülme"
            },
            {
                "id": 131,
                "text": "\"We let them guide the ship to the island and find the treasure first.\"",
                "translation": "\"Önce onların gemiyi adaya yönlendirmesine ve hazineyi bulmasına izin vereceğiz.\"",
                "notes": "guide the ship: gemiyi yönlendirmek; find treasure: hazineyi bulmak"
            },
            {
                "id": 132,
                "text": "\"Then we slit their throats like chickens and take the ship home ourselves!\"",
                "translation": "\"Ardından tavuk gibi boğazlarını keseceğiz ve gemiyi memlekete kendimiz götüreceğiz!\"",
                "notes": "slit throat: boğaz kesmek; like chickens: tavuk gibi"
            },
            {
                "id": 133,
                "text": "Inside the dark barrel, I shivered in utter terror, holding my breath.",
                "translation": "Karanlık fıçının içinde, nefesimi tutarak tarifsiz bir dehşet içinde titredim.",
                "notes": "shiver: titremek; utter terror: mutlak dehşet"
            },
            {
                "id": 134,
                "text": "Every kind word Silver had ever spoken to me was a wicked, murderous lie.",
                "translation": "Silver'ın bana şimdiye dek söylediği her tatlı kelime sinsi ve kanlı bir yalandan ibaretti.",
                "notes": "murderous lie: kanlı / ölümcül yalan; wicked: hain, kötü niyetli"
            },
            {
                "id": 135,
                "text": "Hands then said: \"Dick, jump into the barrel and fetch me an apple to moisten my throat.\"",
                "translation": "Hands ardından dedi ki: \"Dick, fıçıya uzan da boğazımı ıslatmak için bana bir elma çıkar.\"",
                "notes": "fetch: gidip getirmek; moisten throat: boğazını ıslatmak"
            },
            {
                "id": 136,
                "text": "My heart stopped beating; I knew that discovery meant instant murder.",
                "translation": "Yüreğim duracak gibi oldu; yakalanmanın anında katledilmek anlamına geldiğini biliyordum.",
                "notes": "stop beating: duracak gibi olmak; instant murder: anında cinayet"
            },
            {
                "id": 137,
                "text": "\"Don't touch that dirty barrel,\" Silver interrupted, \"go down and fetch a keg of rum!\"",
                "translation": "\"O kirli fıçıya dokunma,\" diyerek araya girdi Silver, \"aşağı in de bir fıçı rom kap gel!\"",
                "notes": "interrupt: sözünü kesmek, araya girmek; keg of rum: küçük rom fıçısı"
            },
            {
                "id": 138,
                "text": "Just as they walked away, a lookout's shout broke the quiet evening air.",
                "translation": "Tam onlar uzaklaşırken gözcünün haykırışı akşamın sessiz havasını yardı.",
                "notes": "lookout: gözcü; quiet evening: sessiz akşam"
            },
            {
                "id": 139,
                "text": "\"Land ho!\" cried the man from the topmast rigging.",
                "translation": "\"Kara göründü!\" diye bağırdı gabya çarmıklarındaki nöbetçi.",
                "notes": "land ho: kara göründü (denizci nidası); topmast: gabya çubuğu"
            },
            {
                "id": 140,
                "text": "Everyone rushed forward to see, and I slipped out of the barrel unnoticed.",
                "translation": "Herkes görmek için öne hücum etti ve ben kimseye fark ettirmeden fıçıdan dışarı süzüldüm.",
                "notes": "rush forward: öne atılmak; slip out unnoticed: fark edilmeden süzülüp çıkmak"
            }
        ]
    },

    # Page 8 (Sentences 141-160)
    {
        "page_no": 8,
        "title": "Arrival at the Skeleton Island",
        "tr_title": "Korsanlar Adası Göründü",
        "vocab_focus": [
            ("anchorage", "demirleme yeri"),
            ("swamp", "bataklık"),
            ("fever", "sıtma, ateş"),
            ("jungle", "balta girmemiş orman"),
            ("spyglass", "dürbün / adanın en yüksek tepesi"),
            ("skeleton", "iskelet"),
            ("treachery", "ihanet, kalleşlik"),
            ("loyal", "sadık")
        ],
        "sentences": [
            {
                "id": 141,
                "text": "Two low hills and a tall peak shaped like a spyglass rose above the ocean fog.",
                "translation": "Okyanus sisinin üzerinden iki alçak tepe ile el dürbününe benzeyen sivri bir doruk yükseliyordu.",
                "notes": "tall peak: yüksek doruk; spyglass: dürbün (tepenin adı)"
            },
            {
                "id": 142,
                "text": "I whispered in Dr. Livesey's ear, asking him to gather the squire and captain below.",
                "translation": "Doktor Livesey'in kulağına fısıldayarak lordu ve kaptanı hemen aşağıda toplamasını istedim.",
                "notes": "whisper in ear: kulağa fısıldamak; gather: toplamak"
            },
            {
                "id": 143,
                "text": "In the cabin, with locked doors, I told them every word I had overheard in the apple barrel.",
                "translation": "Kilitli kapılar ardındaki kamarada, elma fıçısında kulak misafiri olduğum her bir kelimeyi onlara anlattım.",
                "notes": "cabin: kamara; overheard: kulak misafiri olunan"
            },
            {
                "id": 144,
                "text": "Squire Trelawney took Captain Smollett's hand and confessed his great mistake.",
                "translation": "Lord Trelawney Kaptan Smollett'in elini tuttu ve büyük hatasını itiraf etti.",
                "notes": "confess mistake: hatasını itiraf etmek; take hand: elini tutmak"
            },
            {
                "id": 145,
                "text": "\"Captain, you were right, and I was an arrogant fool,\" the squire said humbly.",
                "translation": "\"Kaptan, siz haklıydınız, bense kibirli bir ahmakmışım,\" dedi lord mahcup bir tavırla.",
                "notes": "arrogant fool: kibirli ahmak; humbly: alçakgönüllülükle"
            },
            {
                "id": 146,
                "text": "We counted our loyal men: only seven out of twenty-six were faithful to us.",
                "translation": "Bize sadık olan adamları saydık: yirmi altı kişiden sadece yedisi yanımızdaydı.",
                "notes": "faithful: sadık, vefalı; out of: ... arasından"
            },
            {
                "id": 147,
                "text": "\"We must wait for our chance and let Jim Hawkins watch for openings,\" the doctor advised.",
                "translation": "\"Fırsatımızı kollamalı ve Jim Hawkins'in açık aramasını beklemeliyiz,\" diye tavsiyede bulundu doktor.",
                "notes": "wait for chance: fırsat beklemek; watch for openings: fırsat kollamak"
            },
            {
                "id": 148,
                "text": "The Hispaniola dropped anchor in a calm, landlocked basin surrounded by dense woods.",
                "translation": "Hispaniola, sık ormanlarla çevrili sakin ve karayla çevrili bir koya demir attı.",
                "notes": "landlocked basin: karayla çevrili koy / havza; dense woods: sık ormanlar"
            },
            {
                "id": 149,
                "text": "A poisonous smell of rotting leaves and stagnant swamp water hung over the coast.",
                "translation": "Kıyıya çürüyen yaprakların ve durgun bataklık suyunun zehirli kokusu sinmişti.",
                "notes": "poisonous smell: zehirli koku; stagnant swamp: durgun bataklık"
            },
            {
                "id": 150,
                "text": "\"There is fever in that foul mud,\" Dr. Livesey observed, looking grimly at the shore.",
                "translation": "\"O pis çamurun içinde sıtma mikrobu yatıyor,\" dedi Doktor Livesey sahile kaygıyla bakarak.",
                "notes": "fever: sıtma, yüksek ateş; foul mud: pis çamur"
            },
            {
                "id": 151,
                "text": "The sailors were growing restless and muttered threats under their breath.",
                "translation": "Denizciler huzursuzlanıyor ve dişlerinin arasından tehditler homurdanıyorlardı.",
                "notes": "restless: huzursuz, sabırsız; mutter: homurdanmak"
            },
            {
                "id": 152,
                "text": "Captain Smollett made a bold decision to let the crew go ashore for the afternoon.",
                "translation": "Kaptan Smollett cesur bir kararla mürettebatın öğleden sonra karaya çıkmasına izin verdi.",
                "notes": "bold decision: cesur karar; go ashore: karaya çıkmak"
            },
            {
                "id": 153,
                "text": "Silver eagerly organized two boats, taking thirteen suspected mutineers with him.",
                "translation": "Silver hevesle iki sandal organize etti ve şüpheli on üç isyancıyı yanına aldı.",
                "notes": "mutineer: isyancı gemici; organize: düzenlemek"
            },
            {
                "id": 154,
                "text": "Six pirates remained behind on the Hispaniola under the watchful eyes of the captain.",
                "translation": "Kaptanın tetikteki bakışları altında altı korsan Hispaniola'da nöbette kaldı.",
                "notes": "remain behind: geride kalmak; watchful eyes: dikkatli bakışlar"
            },
            {
                "id": 155,
                "text": "A sudden impulse seized me, and I slipped silently into one of the landing boats.",
                "translation": "Ani bir dürtüye kapıldım ve sessizce karaya çıkan sandallardan birine süzüldüm.",
                "notes": "sudden impulse: ani bir dürtü / istek; seize: kapılmak"
            },
            {
                "id": 156,
                "text": "The boat reached the sand, and I leaped out, running headlong into the jungle.",
                "translation": "Sandal kuma yanaşır yanaşmaz dışarı fırladım ve var gücümle balta girmemiş ormana doğru koştum.",
                "notes": "run headlong: var gücüyle / körü körüne koşmak; jungle: sık orman"
            },
            {
                "id": 157,
                "text": "\"Jim! Jim!\" called Silver behind me, but I ran faster than ever before.",
                "translation": "\"Jim! Jim!\" diye seslendi arkamdan Silver ama ben daha önce hiç koşmadığım kadar hızlı koştum.",
                "notes": "run faster: daha hızlı koşmak"
            },
            {
                "id": 158,
                "text": "I scrambled through thorny thickets and beneath giant pine trees with sweet resin.",
                "translation": "Dikenli çalılıkların arasından ve tatlı reçineli devasa çam ağaçlarının altından tırmanarak geçtim.",
                "notes": "thorny thickets: dikenli çalılıklar; pine tree: çam ağacı"
            },
            {
                "id": 159,
                "text": "Suddenly, a terrible scream of agony rang across the quiet swamp.",
                "translation": "Birden sessiz bataklık boyunca yürek parçalayıcı korkunç bir acı çığlığı yankılandı.",
                "notes": "scream of agony: can çekişme / acı çığlığı; ring across: yankılanmak"
            },
            {
                "id": 160,
                "text": "I knew then that Silver was murdering the honest men who refused to join the pirates.",
                "translation": "O an anladım ki Silver, korsanlara katılmayı reddeden dürüst adamları acımasızca katlediyordu.",
                "notes": "honest men: dürüst adamlar; refuse to join: katılmayı reddetmek"
            }
        ]
    },

    # Page 9 (Sentences 161-180)
    {
        "page_no": 9,
        "title": "The First Strike and Ben Gunn",
        "tr_title": "İlk Saldırı ve Adadaki Sürgün Ben Gunn",
        "vocab_focus": [
            ("marooned", "ıssız adaya terk edilmiş"),
            ("goatskin", "keçi derisi"),
            ("berries", "orman meyveleri, böğürtlen"),
            ("exile", "sürgün"),
            ("cheese", "peynir"),
            ("parched", "kurumuş, kavrulmuş"),
            ("chuckle", "kıkırdamak"),
            ("salvation", "kurtarıcı, selamet")
        ],
        "sentences": [
            {
                "id": 161,
                "text": "Heart pounding with fear, I crept deeper into the wild woods to hide.",
                "translation": "Yüreğim korkuyla güm güm atarak saklanmak için vahşi koruluğun daha derinlerine sindim.",
                "notes": "heart pounding: yüreği küt küt atarak; creep: sessizce sürünmek / sokulmak"
            },
            {
                "id": 162,
                "text": "A gravel stone rolled down a sandy hill, making me freeze in place.",
                "translation": "Kumlu bir yamaçtan aşağı yuvarlanan bir çakıl taşı beni olduğum yere çiviledi.",
                "notes": "gravel stone: çakıl taşı; freeze in place: donakalmak"
            },
            {
                "id": 163,
                "text": "From trunk to trunk, a creature leaped with unnatural speed and ragged movements.",
                "translation": "Ağaç gövdesinden ağaç gövdesine, doğadışı bir hız ve hırpani hareketlerle bir yaratık sıçradı.",
                "notes": "trunk: ağaç gövdesi; ragged: pejmürde, dağınık"
            },
            {
                "id": 164,
                "text": "At first, I thought it was a bear or a wild monkey of the island.",
                "translation": "İlk başta onun bir ayı ya da adaya özgü vahşi bir maymun olduğunu sandım.",
                "notes": "wild monkey: vahşi maymun; at first: ilk başta"
            },
            {
                "id": 165,
                "text": "Then I saw that he was an English human being clothed in tatters of old ship canvas.",
                "translation": "Sonra onun eski gemi brandası paçavralarına bürünmüş İngiliz bir insan olduğunu gördüm.",
                "notes": "human being: insanoğlu; tatters: paçavralar, yırtık pırtık kumaş"
            },
            {
                "id": 166,
                "text": "His skin was burnt as dark as mahogany, and his bright blue eyes looked wild.",
                "translation": "Teni maun ağacı gibi kapkara yanmıştı ve parlak mavi gözleri çılgınca bakıyordu.",
                "notes": "skin burnt: teni yanmış; look wild: vahşi / çılgın görünmek"
            },
            {
                "id": 167,
                "text": "\"Who are you?\" I asked, drawing Billy Bones's pistol from my pocket.",
                "translation": "\"Kimsin sen?\" diye sordum, Billy Bones'un tabancasını cebimden çekerek.",
                "notes": "draw pistol: tabancayı çekmek"
            },
            {
                "id": 168,
                "text": "\"I am poor Ben Gunn,\" he answered, his voice sounding rusty like an unused lock.",
                "translation": "\"Ben zavallı Ben Gunn'ım,\" diye cevap verdi; sesi paslı, kullanılmamış bir kilit gibi çıkıyordu.",
                "notes": "rusty voice: paslı / pürüzlü ses; unused lock: kullanılmamış kilit"
            },
            {
                "id": 169,
                "text": "\"I haven't spoken with a Christian soul for three long years!\"",
                "translation": "\"Tam üç uzun yıldır tek bir insanoğluyla bile konuşmadım!\"",
                "notes": "Christian soul: Hristiyan kul, insanoğlu"
            },
            {
                "id": 170,
                "text": "\"Were you shipwrecked here?\" I asked, lowering my weapon in pity.",
                "translation": "\"Geminiz mi battı buraya düşerken?\" diye sordum acıyarak silahımı indirirken.",
                "notes": "shipwrecked: gemisi batmış; in pity: acıyarak"
            },
            {
                "id": 171,
                "text": "\"Nay, mate,\" he whispered, \"I was marooned by Flint's wicked crew three years back.\"",
                "translation": "\"Yok dostum,\" diye fısıldadı, \"üç yıl önce Flint'in hain tayfası beni buraya terk edip gitti.\"",
                "notes": "maroon: ıssız adada bırakıp kaçmak; three years back: üç yıl önce"
            },
            {
                "id": 172,
                "text": "\"I have lived on wild goats, berries, and oysters, but my heart yearns for cheese!\"",
                "translation": "\"Vahşi keçilerle, böğürtlenlerle ve istiridyeyle yaşadım ama yüreğim peynir diye yanıp tutuşuyor!\"",
                "notes": "yearn for: ...in hasretiyle yanmak; oyster: istiridye"
            },
            {
                "id": 173,
                "text": "\"Have you got a morsel of cheese about you, lad? Just a crust?\"",
                "translation": "\"Yanında bir lokmacık peynir var mı evlat? Sadece küçük bir kabuk bile olsa?\"",
                "notes": "morsel: lokma; crust: ekmek / peynir kabuğu"
            },
            {
                "id": 174,
                "text": "I promised him that Dr. Livesey had fine Parmesan cheese locked in his cabin.",
                "translation": "Ona Doktor Livesey'in kamarasında kilitli harika bir Parmesan peyniri bulunduğuna dair söz verdim.",
                "notes": "Parmesan cheese: Parmesan peyniri; locked: kilitli"
            },
            {
                "id": 175,
                "text": "Ben Gunn rejoiced, dancing on his bare feet like an excited child.",
                "translation": "Ben Gunn sevinçten havalara uçtu, çıplak ayakları üzerinde heyecanlı bir çocuk gibi dans etti.",
                "notes": "rejoice: çok sevinmek; bare feet: çıplak ayaklar"
            },
            {
                "id": 176,
                "text": "I told him about our predicament with Silver and the dangerous mutiny.",
                "translation": "Ona Silver'la yaşadığımız çıkmazı ve tehlikeli gemi isyanını anlattım.",
                "notes": "predicament: zor durum, çıkmaz; mutiny: isyan"
            },
            {
                "id": 177,
                "text": "\"Is Flint's ship back?\" he asked anxiously, clutching my sleeve.",
                "translation": "\"Flint'in gemisi mi geri geldi yoksa?\" diye sordu endişeyle koluma yapışarak.",
                "notes": "clutch sleeve: koluna yapışmak; anxiously: endişeyle"
            },
            {
                "id": 178,
                "text": "\"Flint is dead,\" I replied, \"but most of his old crew are on board under Silver.\"",
                "translation": "\"Flint öldü,\" dedim, \"ama eski mürettebatının çoğu Silver'ın emrinde gemide bulunuyor.\"",
                "notes": "on board: gemide; reply: cevap vermek"
            },
            {
                "id": 179,
                "text": "\"Ben Gunn can help your friends,\" he grinned cunningly, \"for I know this island well.\"",
                "translation": "\"Ben Gunn dostlarına yardım edebilir,\" diye sinsice sırıttı, \"çünkü ben bu adayı avucumun içi gibi bilirim.\"",
                "notes": "grin cunningly: kurnazca sırıtmak"
            },
            {
                "id": 180,
                "text": "Just then, the thunderous boom of a cannon echoed from the sea: the battle had begun!",
                "translation": "Tam o anda denizden bir topun gök gürültüsünü andıran patlaması yankılandı: savaş resmen başlamıştı!",
                "notes": "thunderous boom: gök gürültüsü gibi patlama; cannon: top güllesi"
            }
        ]
    },

    # Page 10 (Sentences 181-200)
    {
        "page_no": 10,
        "title": "The Stockade on the Hill",
        "tr_title": "Tepedeki Ahşap Siper ve Kuşatma",
        "vocab_focus": [
            ("stockade", "ahşap istihkam, siper"),
            ("palisade", "kazıklı çit, savunma duvarı"),
            ("log house", "kütük ev"),
            ("provisions", "erzak, yiyecek stoğu"),
            ("powder", "barut"),
            ("musket", "tüfek"),
            ("colors", "sancak, bayrak"),
            ("cannonball", "top güllesi")
        ],
        "sentences": [
            {
                "id": 181,
                "text": "While I was ashore, Dr. Livesey and Hunter had quietly slipped away in the small boat.",
                "translation": "Ben karadayken Doktor Livesey ve Hunter küçük sandalla sessizce gemiden ayrılmışlardı.",
                "notes": "slip away: sıvışmak, sessizce ayrılmak; ashore: karada"
            },
            {
                "id": 182,
                "text": "They had discovered an old wooden stockade built on a knoll by Captain Flint years ago.",
                "translation": "Kaptan Flint'in yıllar önce bir tepecik üzerine inşa ettiği eski bir ahşap hisarı keşfetmişlerdi.",
                "notes": "stockade: ahşap hisar / istihkam; knoll: küçük tepe"
            },
            {
                "id": 183,
                "text": "It was a stout log house surrounded by a six-foot palisade with loopholes for muskets.",
                "translation": "Tüfek delikleriyle donatılmış iki metrelik kazıklı çitle çevrili, sağlam bir kütük evdi.",
                "notes": "log house: kütük ev; palisade: kazıklı çit; loophole: mazgal, tüfek deliği"
            },
            {
                "id": 184,
                "text": "Best of all, a spring of delicious fresh water bubbled up right inside the enclosure.",
                "translation": "En güzeli de, istihkamın tam içinde leziz bir tatlı su pınarı kaynıyordu.",
                "notes": "spring: pınar, su kaynağı; enclosure: etrafı çevrili alan"
            },
            {
                "id": 185,
                "text": "Captain Smollett and the loyal men decided to abandon the Hispaniola and fortify the stockade.",
                "translation": "Kaptan Smollett ve sadık adamlar, Hispaniola'yı terk edip ahşap hisarı tahkim etmeye karar verdiler.",
                "notes": "abandon: terk etmek; fortify: güçlendirmek, tahkim etmek"
            },
            {
                "id": 186,
                "text": "They made several trips in the small boat, transporting barrels of powder, muskets, and pork.",
                "translation": "Küçük sandalla birkaç sefer yaparak barut fıçılarını, tüfekleri ve tuzlu domuz etini taşıdılar.",
                "notes": "transport: nakletmek; pork: domuz eti (gemici kumanyası)"
            },
            {
                "id": 187,
                "text": "On their last trip, the pirates on the ship opened fire with the great swivel cannon.",
                "translation": "Son seferlerinde gemideki korsanlar büyük döner topla ateşe başladılar.",
                "notes": "open fire: ateş açmak; swivel cannon: döner top"
            },
            {
                "id": 188,
                "text": "A cannonball swamped their overloaded boat, sending most of their precious food into the bay.",
                "translation": "Bir gülle aşırı yüklü sandallarını alabora etti ve değerli yiyeceklerinin çoğunu koya döktü.",
                "notes": "swamp a boat: sandalı suyla doldurup batırmak; cannonball: top güllesi"
            },
            {
                "id": 189,
                "text": "The loyal party waded ashore under heavy fire and scrambled safely inside the palisade.",
                "translation": "Sadık kafile yoğun ateş altında sudan geçerek karaya çıktı ve kazıklı çitin içine sağ salim sığındı.",
                "notes": "wade: suda yürümek; heavy fire: yoğun yaylım ateşi"
            },
            {
                "id": 190,
                "text": "Captain Smollett proudly hoisted the British Union Jack over the log roof.",
                "translation": "Kaptan Smollett İngiliz Kraliyet Bayrağı'nı kütük çatının üzerine gururla çekti.",
                "notes": "hoist the flag: bayrağı göndere çekmek; Union Jack: Birleşik Krallık bayrağı"
            },
            {
                "id": 191,
                "text": "When I arrived outside the stockade, I heard my friends' voices calling my name in joy.",
                "translation": "Ahşap siperin dışına vardığımda, dostlarımın sevinçle adımı haykıran seslerini duydum.",
                "notes": "in joy: sevinç içinde; voice: ses"
            },
            {
                "id": 192,
                "text": "I scrambled over the wooden fence and fell breathless into the arms of Dr. Livesey.",
                "translation": "Tahta çitin üzerinden aştım ve soluk soluğa Doktor Livesey'in kollarına düştüm.",
                "notes": "scramble over: üzerinden tırmanıp aşmak; breathless: nefes nefese"
            },
            {
                "id": 193,
                "text": "They were overjoyed to see me alive, for they had feared I had been murdered by Silver.",
                "translation": "Beni canlı gördüklerine çok sevindiler çünkü Silver tarafından öldürüldüğümden korkuyorlardı.",
                "notes": "overjoyed: son derece sevinçli; fear: korkmak"
            },
            {
                "id": 194,
                "text": "I reported my meeting with Ben Gunn, and the doctor nodded thoughtfully.",
                "translation": "Ben Gunn ile buluşmamı anlattım ve doktor düşünceli bir tavırla başını salladı.",
                "notes": "nod thoughtfully: düşünceli bir şekilde başını sallamak; report: bildirmek"
            },
            {
                "id": 195,
                "text": "Cannonballs from the Hispaniola crashed through the treetops above our heads all afternoon.",
                "translation": "Hispaniola'dan atılan gülleler bütün öğleden sonra başımızın üstündeki ağaç tepelerini parçaladı.",
                "notes": "treetops: ağaç tepeleri; crash through: gürültüyle parçalamak"
            },
            {
                "id": 196,
                "text": "However, the thick logs of our stockade protected us from every pirate shot.",
                "translation": "Bununla birlikte hisarımızın kalın kütükleri bizi her korsan atışından başarıyla korudu.",
                "notes": "thick logs: kalın kütükler; protect: korumak"
            },
            {
                "id": 197,
                "text": "Tom Redruth, the faithful old gamekeeper, was shot by a sniper and died with a prayer.",
                "translation": "Sadık yaşlı korucu Tom Redruth bir keskin nişancı tarafından vuruldu ve bir duayla can verdi.",
                "notes": "gamekeeper: korucu; sniper: keskin nişancı"
            },
            {
                "id": 198,
                "text": "Squire Trelawney wept like a child and laid the British flag over his faithful servant.",
                "translation": "Lord Trelawney bir çocuk gibi ağladı ve sadık uşağının üzerine İngiliz bayrağını örttü.",
                "notes": "weep: ağlamak; faithful servant: sadık hizmetkar"
            },
            {
                "id": 199,
                "text": "We were now only six well men inside the fort, surrounded by fifteen ruthless pirates.",
                "translation": "Artık kalede on beş acımasız korsanla çevrili yalnızca altı sağlam adam kalmıştık.",
                "notes": "ruthless: acımasız, merhametsiz; surrounded: kuşatılmış"
            },
            {
                "id": 200,
                "text": "As darkness fell, we prepared our muskets, knowing an assault would come with dawn.",
                "translation": "Karanlık çökerken, şafakla birlikte bir hücumun geleceğini bilerek tüfeklerimizi hazırladık.",
                "notes": "assault: hücum, saldırı; dawn: şafak vakti"
            }
        ]
    },

    # Page 11 (Sentences 201-220)
    {
        "page_no": 11,
        "title": "The Jolly Roger and the Truce",
        "tr_title": "Korsan Bayrağı ve Silver'ın Barış Teklifi",
        "vocab_focus": [
            ("truce", "ateşkes, mütareke"),
            ("embassy", "elçilik heyeti"),
            ("Jolly Roger", "korsan bayrağı (kurukafa-kemik)"),
            ("flag of truce", "beyaz bayrak, mütareke bayrağı"),
            ("surrender", "teslim olmak"),
            ("charter", "sözleşme, şart"),
            ("parley", "görüşme, müzakere"),
            ("scoundrel", "alçak, namussuz")
        ],
        "sentences": [
            {
                "id": 201,
                "text": "Early the next morning, a lookout shouted: \"Flag of truce! Flag of truce!\"",
                "translation": "Ertesi sabah erkenden nöbetçi bağırdı: \"Ateşkes bayrağı! Ateşkes bayrağı!\"",
                "notes": "flag of truce: beyaz teslim / ateşkes bayrağı"
            },
            {
                "id": 202,
                "text": "Outside the palisade stood Long John Silver, waving a white cloth upon a staff.",
                "translation": "Kazıklı çitin dışında bir sopaya takılı beyaz bezi sallayan Uzun John Silver duruyordu.",
                "notes": "staff: sopa, asa; wave a cloth: bez sallamak"
            },
            {
                "id": 203,
                "text": "He wore a grand blue coat with brass buttons and his finest cocked hat.",
                "translation": "Pirinç düğmeli görkemli mavi bir ceket ve en şık üç köşeli şapkasını giymişti.",
                "notes": "brass buttons: pirinç düğmeler; cocked hat: üç köşeli şapka"
            },
            {
                "id": 204,
                "text": "\"Cap'n Silver, sir, come on board to make terms!\" he called out grandly.",
                "translation": "\"Kaptan Silver efendim, şartları konuşmak üzere müzakereye geldi!\" diye azametle seslendi.",
                "notes": "make terms: şartlarda anlaşmak, pazarlık yapmak"
            },
            {
                "id": 205,
                "text": "Captain Smollett stood at the doorway with a pipe between his teeth.",
                "translation": "Kaptan Smollett dişlerinin arasında piposuyla kapı eşiğinde dikildi.",
                "notes": "doorway: kapı aralığı / eşiği; pipe: pipo"
            },
            {
                "id": 206,
                "text": "\"I don't know any Captain Silver,\" Smollett retorted, \"you are just a mutinous cook.\"",
                "translation": "\"Ben Kaptan Silver diye birini tanımıyorum,\" dedi Smollett sertçe, \"sen sadece isyankar bir aşçısın.\"",
                "notes": "retort: sert karşılık vermek; mutinous cook: isyankar aşçı"
            },
            {
                "id": 207,
                "text": "\"However, if you wish to talk under a flag of truce, climb over the stockade.\"",
                "translation": "\"Yine de eğer beyaz bayrak altında konuşmak istiyorsan hisarın üzerinden atla gel.\"",
                "notes": "climb over: üzerinden aşmak / atlamak"
            },
            {
                "id": 208,
                "text": "Silver hopped over the logs with great difficulty and advanced toward the cabin.",
                "translation": "Silver büyük bir güçlükle kütüklerin üzerinden sekti ve kulübeye doğru ilerledi.",
                "notes": "advance toward: ...e doğru ilerlemek; great difficulty: büyük zorluk"
            },
            {
                "id": 209,
                "text": "He sat down in the sand, wiping sweat from his brow with a silk handkerchief.",
                "translation": "Kuma oturdu, ipek bir mendille alnındaki teri sildi.",
                "notes": "wipe sweat: teri silmek; handkerchief: mendil"
            },
            {
                "id": 210,
                "text": "\"Here is our offer,\" Silver began, fixing his cold grey eyes upon the captain.",
                "translation": "\"İşte teklifimiz,\" diye başladı Silver, soğuk gri gözlerini kaptana dikerek.",
                "notes": "fix eyes upon: gözlerini dikmek; offer: teklif"
            },
            {
                "id": 211,
                "text": "\"Give us the treasure chart, and we will spare your lives without a scratch.\"",
                "translation": "\"Bize hazine haritasını verin, burnunuz bile kanamadan canınızı bağışlayalım.\"",
                "notes": "treasure chart: hazine haritası; without a scratch: burnu bile kanamadan"
            },
            {
                "id": 212,
                "text": "\"We will set you ashore on some peaceful coast or let you sail home safely.\"",
                "translation": "\"Sizi huzurlu bir kıyıda karaya bırakır ya da eve güvenle yelken açmanıza izin veririz.\"",
                "notes": "peaceful coast: huzurlu kıyı; sail home: eve yelken açmak"
            },
            {
                "id": 213,
                "text": "Captain Smollett knocked the ashes from his pipe and looked scornfully at the pirate.",
                "translation": "Kaptan Smollett piposunun külünü silkti ve korsana hor gören gözlerle baktı.",
                "notes": "look scornfully: küçümseyerek / hor görerek bakmak; ashes: küller"
            },
            {
                "id": 214,
                "text": "\"Now you hear me, Silver,\" the captain replied with steely calm.",
                "translation": "\"Şimdi sen beni dinle Silver,\" dedi kaptan çelik gibi bir sakinlikle.",
                "notes": "steely calm: çelik gibi sakinlik; hear someone: birini dinlemek"
            },
            {
                "id": 215,
                "text": "\"You can't find the treasure without the chart, and you can't sail the ship without me.\"",
                "translation": "\"Harita olmadan hazineyi bulamazsın ve ben olmadan gemiyi asla yüzdüremezsin.\"",
                "notes": "sail the ship: gemiyi yürütmek / idare etmek"
            },
            {
                "id": 216,
                "text": "\"You are on a lee shore and all of you will end your days in irons in an English prison.\"",
                "translation": "\"Kayalıklara sürüklenen bir tekne gibisiniz ve hepiniz günlerinizi İngiliz hapishanesinde zincire vurulmuş bitireceksiniz.\"",
                "notes": "in irons: prangaya vurulmuş; lee shore: tehlikeli rüzgar altı kıyısı"
            },
            {
                "id": 217,
                "text": "\"My only offer is this: come unarmed, and I will clap you in irons for a fair trial in England.\"",
                "translation": "\"Benim tek teklifim şudur: silahsız gelin, sizi İngiltere'de adil bir yargılama için prangaya vurayım.\"",
                "notes": "fair trial: adil yargılama; unarmed: silahsız"
            },
            {
                "id": 218,
                "text": "Silver's face turned purple with uncontrolled fury.",
                "translation": "Silver'ın yüzü zapt edilemez bir öfkeyle morardı.",
                "notes": "turn purple: morarmak; uncontrolled fury: kontrolsüz öfke"
            },
            {
                "id": 219,
                "text": "\"Before this hour is out, I'll smash your log house like a rum puncheon!\" he roared.",
                "translation": "\"Bu saat dolmadan kütük evinizi bir rom fıçısı gibi paramparça edeceğim!\" diye kükredi.",
                "notes": "smash: parçalamak; puncheon: büyük ahşap fıçı"
            },
            {
                "id": 220,
                "text": "He spat upon the sand, scrambled cursing over the palisade, and vanished into the jungle.",
                "translation": "Kuma tükürdü, küfürler savurarak kazıklı çiti aştı ve ormanın içinde gözden kayboldu.",
                "notes": "spit upon: üzerine tükürmek; curse: lanet okumak, küfretmek"
            }
        ]
    },

    # Page 12 (Sentences 221-240)
    {
        "page_no": 12,
        "title": "The Battle of the Stockade",
        "tr_title": "Sipere Hücum ve Şiddetli Çarpışma",
        "vocab_focus": [
            ("assault", "saldırı, taarruz"),
            ("smoke", "duman"),
            ("blade", "kılıç namlusu"),
            ("cutlass", "kısa korsan palası"),
            ("loophole", "mazgal deliği"),
            ("furious", "öfkeli, şiddetli"),
            ("volley", "yaylım ateşi"),
            ("victory", "zafer")
        ],
        "sentences": [
            {
                "id": 221,
                "text": "\"To your posts, lads!\" Captain Smollett ordered as soon as Silver disappeared.",
                "translation": "\"Mevzilere çocuklar!\" diye emretti Kaptan Smollett, Silver gözden kaybolur kaybolmaz.",
                "notes": "to your posts: mevzilere, görev yerlerine; order: emretmek"
            },
            {
                "id": 222,
                "text": "We loaded every musket and placed spare powder horns on the bench.",
                "translation": "Her tüfeği doldurduk ve yedek barut boynuzlarını sıranın üzerine dizdik.",
                "notes": "powder horn: barut boynuzu; bench: tahta sıra"
            },
            {
                "id": 223,
                "text": "A deadly silence fell over the woods, broken only by chirping crickets.",
                "translation": "Ormanın üzerine yalnızca cırcır böceklerinin cıvıltısıyla bölünen ölümcül bir sessizlik çöktü.",
                "notes": "deadly silence: ölümcül sessizlik; cricket: cırcır böceği"
            },
            {
                "id": 224,
                "text": "Suddenly, a burst of gunfire shattered the stillness from the north side of the fence.",
                "translation": "Aniden, çitin kuzey tarafından gelen bir silah patlaması sessizliği paramparça etti.",
                "notes": "shatter the stillness: sessizliği yırtmak / bozmak; burst of gunfire: yaylım ateşi"
            },
            {
                "id": 225,
                "text": "Balls whistled through the loopholes, filling our log house with pungent smoke.",
                "translation": "Kurşunlar mazgal deliklerinden ıslık çalarak geçti ve kütük evimizi geniz yakan dumanla doldurdu.",
                "notes": "pungent smoke: keskin / geniz yakan duman; whistle: vızıldamak"
            },
            {
                "id": 226,
                "text": "A score of pirates leaped from the woods, swarming over the stockade like monkeys.",
                "translation": "Yirmiye yakın korsan ormandan fırladı ve maymunlar gibi hisarın üzerine üşüştü.",
                "notes": "a score of: yirmi kadar; swarm over: üzerine üşüşmek / akın etmek"
            },
            {
                "id": 227,
                "text": "Hunter and Joyce fired through the openings, bringing down two attackers immediately.",
                "translation": "Hunter ve Joyce deliklerden ateş açarak iki saldırganı hemen yere serdiler.",
                "notes": "bring down: yere sermek; immediately: derhal"
            },
            {
                "id": 228,
                "text": "However, seven pirates scrambled inside the enclosure, cutlasses flashing in the sun.",
                "translation": "Fakat yedi korsan güneşin altında parıldayan palalarıyla avlunun içine girmeyi başardı.",
                "notes": "flash in the sun: güneşte parıldamak; cutlass: pala"
            },
            {
                "id": 229,
                "text": "\"Out, lads, and fight them in the open!\" shouted the captain, seizing a cutlass.",
                "translation": "\"Dışarı çocuklar, onlarla açık alanda dövüşeceğiz!\" diye haykırdı kaptan, bir palaya sarılarak.",
                "notes": "in the open: açık alanda; seize: kavramak"
            },
            {
                "id": 230,
                "text": "We dashed into the sunlight, where swords clashed and pistols roared at point-blank range.",
                "translation": "Kılıçların çarpıştığı ve tabancaların sıfır mesafeden kükrediği gün ışığına fırladık.",
                "notes": "point-blank range: sıfır mesafe, namlu mesafesi; clash: çarpışmak"
            },
            {
                "id": 231,
                "text": "Dr. Livesey ran his rapier through a pirate who fell screaming into the sand.",
                "translation": "Doktor Livesey meçini bir korsana sapladı; adam çığlıklar atarak kuma yığıldı.",
                "notes": "rapier: ince uzun kılıç, meç; run through: kılıcı saplamak"
            },
            {
                "id": 232,
                "text": "A pirate named Anderson raised his heavy blade above my head with an evil grin.",
                "translation": "Anderson adında bir korsan, şeytani bir sırıtışla ağır kılıcını başımın üzerine kaldırdı.",
                "notes": "evil grin: hain sırıtış; blade: kılıç namlusu"
            },
            {
                "id": 233,
                "text": "I rolled to one side as the blade struck deep into the log wall.",
                "translation": "Kılıç kütük duvara derince saplanırken ben bir yana doğru yuvarlandım.",
                "notes": "roll to one side: bir yana yuvarlanmak; strike deep: derine saplanmak"
            },
            {
                "id": 234,
                "text": "Before he could pull it free, the doctor struck him down with his sword.",
                "translation": "Adam kılıcı kurtaramadan önce doktor kılıcıyla onu yere serdi.",
                "notes": "strike down: yere sermek; pull free: çekip kurtarmak"
            },
            {
                "id": 235,
                "text": "The surviving pirates lost heart, turned around, and fled over the fence.",
                "translation": "Hayatta kalan korsanların cesareti kırıldı, geriye dönüp çitin üzerinden kaçtılar.",
                "notes": "lose heart: cesaretini yitirmek; flee: kaçmak"
            },
            {
                "id": 236,
                "text": "Within three furious minutes, the brutal attack was completely repelled.",
                "translation": "Üç şiddetli dakika içinde bu acımasız saldırı tamamen püskürtüldü.",
                "notes": "repel: püskürtmek; brutal attack: vahşi saldırı"
            },
            {
                "id": 237,
                "text": "Five pirates lay dead on the sand, while the others had escaped back into the swamp.",
                "translation": "Beş korsan kumların üzerinde cansız yatıyordu, diğerleri ise bataklığa doğru kaçmıştı.",
                "notes": "lay dead: ölü yatmak; escape back: gerisin geri kaçmak"
            },
            {
                "id": 238,
                "text": "Yet our victory had come at a heavy cost to our little garrison.",
                "translation": "Fakat bu zafer küçük garnizonumuza çok ağır bir bedele mal olmuştu.",
                "notes": "heavy cost: ağır bedel; garrison: garnizon, savunma birliği"
            },
            {
                "id": 239,
                "text": "Joyce was dead, Hunter was gravely wounded, and Captain Smollett had been shot twice.",
                "translation": "Joyce ölmüştü, Hunter ağır yaralıydı ve Kaptan Smollett iki yerinden vurulmuştu.",
                "notes": "gravely wounded: ağır yaralı; shot twice: iki kez vurulmuş"
            },
            {
                "id": 240,
                "text": "The doctor bandaged the captain's bleeding wounds while we guarded the barricade.",
                "translation": "Biz barikatı beklerken doktor kaptanın kanayan yaralarını sardı.",
                "notes": "bandage wounds: yaraları sarmak; guard: korumak, nöbet tutmak"
            }
        ]
    },

    # Page 13 (Sentences 241-260)
    {
        "page_no": 13,
        "title": "Jim's Sea Adventure and the Coracle",
        "tr_title": "Jim'in Sandalla Cesur Gece Akını",
        "vocab_focus": [
            ("coracle", "deri kaplı yuvarlak ilkel sandal"),
            ("hawser", "palamar halatı, bağlama ipi"),
            ("drift", "akıntıya kapılmak, sürüklenmek"),
            ("undertow", "dip akıntısı"),
            ("paddle", "kürek çekmek / tek pala kürek"),
            ("knife", "bıçak"),
            ("ebb tide", "cezir, suların çekilmesi"),
            ("anchor", "çapa, gemi demiri")
        ],
        "sentences": [
            {
                "id": 241,
                "text": "After dinner, Dr. Livesey took his hat and pistols and walked boldly off into the woods.",
                "translation": "Yemekten sonra Doktor Livesey şapkasını ve tabancalarını alıp cesurca ormana doğru yürüdü.",
                "notes": "boldly: cesurca; pistols: tabancalar"
            },
            {
                "id": 242,
                "text": "I knew he was going to find Ben Gunn, and a reckless plan entered my own head.",
                "translation": "Ben Gunn'ı bulmaya gittiğini biliyordum ve kendi aklıma da cüretkar bir plan girdi.",
                "notes": "reckless plan: pervasız / cüretkar plan; enter head: aklına gelmek"
            },
            {
                "id": 243,
                "text": "I hated sitting idle in the heat, watching our wounded companions groan in pain.",
                "translation": "Sıcakta boş oturmaktan ve yaralı arkadaşlarımızın acı içinde inlemesini izlemekten nefret ediyordum.",
                "notes": "idle: boş, tembel; groan in pain: acıdan inlemek"
            },
            {
                "id": 244,
                "text": "Ben Gunn had told me he had built a small boat hidden beneath a white rock.",
                "translation": "Ben Gunn bana beyaz bir kayanın altında sakladığı küçük bir kayık yaptığını söylemişti.",
                "notes": "hidden beneath: altında gizlenmiş; boat: sandal"
            },
            {
                "id": 245,
                "text": "Without asking permission, I filled my pockets with biscuits and slipped out into the bushes.",
                "translation": "İzin istemeden ceplerimi bisküviyle doldurdum ve çalılıkların arasına süzüldüm.",
                "notes": "without permission: izinsiz; slip out: sıvışmak"
            },
            {
                "id": 246,
                "text": "I ran along the coastline until I found the hollow white rock Ben had described.",
                "translation": "Ben'in tarif ettiği oyuk beyaz kayayı bulana kadar kıyı şeridi boyunca koştum.",
                "notes": "coastline: kıyı şeridi; hollow rock: oyuk kaya"
            },
            {
                "id": 247,
                "text": "Under a tent of goatskins lay a little coracle: a tiny wicker boat covered in stretched hide.",
                "translation": "Keçi derisinden bir çadırın altında küçük bir ilkel sandal duruyordu: gerilmiş deriyle kaplı minicik hasır bir kayık.",
                "notes": "coracle: deri kaplı hafif ilkel kayık; wicker: hasır, sepet örgüsü"
            },
            {
                "id": 248,
                "text": "It was very light, completely round, and exceedingly difficult to steer.",
                "translation": "Çok hafifti, tamamen yuvarlaktı ve yönlendirmesi son derece zordu.",
                "notes": "exceedingly difficult: fevkalade zor; steer: dümen tutmak, yönlendirmek"
            },
            {
                "id": 249,
                "text": "I waited until darkness covered the bay before dragging the little vessel into the surf.",
                "translation": "Karanlık koyu tamamen örtünceye kadar bekledim, sonra minik tekneyi dalgaların içine çektim.",
                "notes": "surf: kıyıya vuran dalgalar; drag: sürüklemek"
            },
            {
                "id": 250,
                "text": "My bold plan was to paddle out to the Hispaniola and cut her anchor cable.",
                "translation": "Cesur planım, kürek çekerek Hispaniola'ya ulaşmak ve demir halatını kesmekti.",
                "notes": "paddle out: kürekle açılmak; cable: palamar halatı"
            },
            {
                "id": 251,
                "text": "If the ship drifted ashore, the pirates could never use her to escape.",
                "translation": "Eğer gemi karaya sürüklenirse, korsanlar onu kaçmak için asla kullanamazlardı.",
                "notes": "drift ashore: karaya sürüklenmek; escape: kaçmak"
            },
            {
                "id": 252,
                "text": "The ebb tide carried my coracle swiftly toward the great black silhouette of the ship.",
                "translation": "Çekilen deniz akıntısı minik sandalımı geminin devasa siyah silüetine doğru hızla taşıdı.",
                "notes": "ebb tide: cezir akıntısı; silhouette: silüet"
            },
            {
                "id": 253,
                "text": "From the cabin window came loud drunken shouts and singing from the pirate watchmen.",
                "translation": "Kamaranın penceresinden sarhoşça naralar ve korsan nöbetçilerin söylediği şarkılar geliyordu.",
                "notes": "drunken shouts: sarhoşça naralar; watchmen: nöbetçiler"
            },
            {
                "id": 254,
                "text": "I drifted silently under the bowsprit, grasping the thick hawser with both hands.",
                "translation": "Civadranın altına sessizce yanaştım ve kalın palamar halatını iki elimle kavradım.",
                "notes": "bowsprit: civadra (baş bodoslama direği); hawser: kalın bağlama halatı"
            },
            {
                "id": 255,
                "text": "The hawser was taut as a bowstring under the strong ocean current.",
                "translation": "Halat güçlü okyanus akıntısının altında bir yay kirişi gibi gerilmişti.",
                "notes": "taut: gergin; bowstring: yay kirişi"
            },
            {
                "id": 256,
                "text": "I pulled out my clasp-knife and began sawing patiently strand after strand.",
                "translation": "Çakımı çıkardım ve sabırla lif lif kesmeye başladım.",
                "notes": "clasp-knife: çakı; strand: tel, lif; saw: testereyle keser gibi kesmek"
            },
            {
                "id": 257,
                "text": "A sudden gust of wind eased the strain, and my sharp knife severed the final fibers.",
                "translation": "Ani bir rüzgar esintisi gerginliği hafifletti ve keskin bıçağım son lifleri de kopardı.",
                "notes": "sever: koparmak, kesmek; gust of wind: ani rüzgar esintisi"
            },
            {
                "id": 258,
                "text": "The Hispaniola swung round in the current, beginning to drift freely out toward sea.",
                "translation": "Hispaniola akıntıyla birlikte kendi etrafında döndü ve denize doğru serbestçe sürüklenmeye başladı.",
                "notes": "swing round: dönmek, savrulmak; drift freely: serbestçe sürüklenmek"
            },
            {
                "id": 259,
                "text": "The drunken singing stopped abruptly, replaced by furious cries of alarm on deck.",
                "translation": "Sarhoş şarkıları aniden kesildi, yerini güvertedeki öfkeli alarm çığlıkları aldı.",
                "notes": "abruptly: ansızın, birdenbire; cries of alarm: panik / alarm çığlıkları"
            },
            {
                "id": 260,
                "text": "Tossed helplessly by big waves, my little boat was swept into the pitch-black night.",
                "translation": "Büyük dalgalar tarafından çaresizce savrulan küçük kayığım zifiri karanlık gecenin içine sürüklendi.",
                "notes": "toss: dalgalarda savrulmak; pitch-black: zifiri karanlık"
            }
        ]
    },

    # Page 14 (Sentences 261-280)
    {
        "page_no": 14,
        "title": "Recapturing the Hispaniola",
        "tr_title": "Hispaniola'nın Geri Alınışı",
        "vocab_focus": [
            ("helm", "dümen"),
            ("derelict", "terk edilmiş, başıboş"),
            ("coxswain", "dümenci, filika reisi"),
            ("dirk", "kama, uzun hançer"),
            ("shrouds", "çarmıklar (direk gergi ipleri)"),
            ("spar", "seren direği"),
            ("shoal", "sığlık, kum tepesi"),
            ("blood", "kan")
        ],
        "sentences": [
            {
                "id": 261,
                "text": "At sunrise, I found myself drifting near the southern cliffs of the island.",
                "translation": "Güneş doğduğunda kendimi adanın güney kayalıklarının yakınında sürüklenirken buldum.",
                "notes": "at sunrise: gün doğumunda; drift: sürüklenmek"
            },
            {
                "id": 262,
                "text": "To my utter amazement, the great schooner Hispaniola was sailing wild just a mile away.",
                "translation": "Şaşkınlıktan donakaldım; koca uskuna Hispaniola sadece bir mil ötede başıboş bir şekilde yüzüyordu.",
                "notes": "utter amazement: büyük şaşkınlık; sail wild: başıboş yelken açmak"
            },
            {
                "id": 263,
                "text": "Her mainsail flapped in the breeze, and no hand appeared to be guiding the helm.",
                "translation": "Büyük ana yelkeni rüzgarda çırpınıyordu ve dümende ona yön veren tek bir el bile görünmüyordu.",
                "notes": "mainsail: ana yelken; flap: kanat / yelken çırpmak"
            },
            {
                "id": 264,
                "text": "I paddled desperately toward her and managed to catch a dangling rope from the bowsprit.",
                "translation": "Çaresizce ona doğru kürek çektim ve civadradan sarkan bir halatı yakalamayı başardım.",
                "notes": "dangling rope: sarkan halat; catch: yakalamak"
            },
            {
                "id": 265,
                "text": "My light coracle was crushed under the schooner's hull, leaving me clinging for my life.",
                "translation": "Hafif kayığım uskunanın gövdesi altında ezildi ve beni can havliyle halata tutunur halde bıraktı.",
                "notes": "cling for life: can havliyle tutunmak; hull: gemi teknesi / gövdesi"
            },
            {
                "id": 266,
                "text": "I scrambled onto the deck and beheld a gruesome scene of pirate drunken violence.",
                "translation": "Güverteye tırmandım ve korsanların sarhoşça şiddetine ait korkunç bir manzarayla karşılaştım.",
                "notes": "gruesome scene: dehşet verici manzara; violence: şiddet"
            },
            {
                "id": 267,
                "text": "One pirate lay dead by the mast, his red cap soaked in dark blood.",
                "translation": "Bir korsan direğin dibinde ölü yatıyordu; kırmızı takkesi koyu kana bulanmıştı.",
                "notes": "soaked in blood: kana bulanmış; mast: gemi direği"
            },
            {
                "id": 268,
                "text": "Israel Hands, the ship's coxswain, sat propped against the bulwarks, groaning with a wounded thigh.",
                "translation": "Geminin serdümeni Israel Hands, küpeşteye yaslanmış oturuyor, yaralı uyluğunun acısıyla inliyordu.",
                "notes": "coxswain: serdümen, dümenci; bulwarks: küpeşte"
            },
            {
                "id": 269,
                "text": "\"Give me some brandy, Jim,\" Hands whispered hoarsely, \"I am wounded to death.\"",
                "translation": "\"Bana biraz konyak ver Jim,\" diye hırıltıyla fısıldadı Hands, \"ölümcül şekilde yaralandım.\"",
                "notes": "hoarsely: boğuk / hırıltılı sesle; brandy: konyak"
            },
            {
                "id": 270,
                "text": "I brought him a bottle of wine, food, and water from the officers' pantry.",
                "translation": "Ona subay kilerinden bir şişe şarap, yiyecek ve su getirdim.",
                "notes": "pantry: kiler; officers: subaylar"
            },
            {
                "id": 271,
                "text": "\"I have taken possession of this ship, Mr. Hands,\" I announced firmly.",
                "translation": "\"Bu geminin kontrolünü ben devraldım Bay Hands,\" diye ilan ettim kararlılıkla.",
                "notes": "take possession: sahiplenmek, kontrolünü almak; firmly: kararlılıkla"
            },
            {
                "id": 272,
                "text": "I climbed the rigging, tore down the pirate Jolly Roger flag, and tossed it into the sea.",
                "translation": "Direk donanımına tırmandım, korsanların Jolly Roger bayrağını yırttım ve denize fırlattım.",
                "notes": "tear down: yırtıp indirmek; toss into the sea: denize atmak"
            },
            {
                "id": 273,
                "text": "Hands agreed to help me steer the ship into the safe North Inlet in exchange for his life.",
                "translation": "Hands, canının bağışlanması karşılığında gemiyi güvenli Kuzey Koyu'na yanaştırmama yardım etmeyi kabul etti.",
                "notes": "in exchange for: ...in karşılığında; safe inlet: güvenli koy"
            },
            {
                "id": 274,
                "text": "However, his sly eyes constantly followed my movements with murderous intent.",
                "translation": "Ancak sinsi gözleri ölümcül bir niyetle durmadan hareketlerimi takip ediyordu.",
                "notes": "sly eyes: sinsi bakışlar; murderous intent: ölümcül niyet"
            },
            {
                "id": 275,
                "text": "As the ship ran gently onto a sandy beach, I turned around just in time.",
                "translation": "Gemi usulca kumsal bir sığlığa otururken tam vaktinde arkama döndüm.",
                "notes": "just in time: tam vaktinde; sandy beach: kumluk sahil"
            },
            {
                "id": 276,
                "text": "Hands was limping toward me with a gleaming bloody dirk in his right hand!",
                "translation": "Hands, sağ elinde pırıl pırıl parlayan kanlı bir kamayla bana doğru topallayarak geliyordu!",
                "notes": "gleaming dirk: parıldayan kama; limp: topallamak"
            },
            {
                "id": 277,
                "text": "I sprang into the mast rigging, scrambling up to the crosstrees out of his reach.",
                "translation": "Direk çarmıklarına atladım ve onun erişemeyeceği seren çarmıklarına kadar yukarı tırmandım.",
                "notes": "crosstrees: gabya çarmıkları, seren çarmığı; out of reach: erişilemez yerde"
            },
            {
                "id": 278,
                "text": "Hands hurled his knife through the air; it pinned my shoulder to the wooden mast!",
                "translation": "Hands bıçağını havadan fırlattı; bıçak omzumu tahta direğe çiviledi!",
                "notes": "hurl knife: bıçak fırlatmak; pin: çivilemek, sabitlemek"
            },
            {
                "id": 279,
                "text": "In severe pain, my pistols discharged both together; Hands gave a choked cry and plunged into the sea.",
                "translation": "Şiddetli bir acı içinde iki tabancam birden ateş aldı; Hands boğuk bir çığlık attı ve denize gömüldü.",
                "notes": "choked cry: boğuk çığlık; plunge into: içine dalmak / gömülmek"
            },
            {
                "id": 280,
                "text": "The traitor was dead, and the Hispaniola was safely beached in our hands.",
                "translation": "Hain ölmüştü ve Hispaniola güvenli bir şekilde karaya oturtulmuş olarak bizim elimizdeydi.",
                "notes": "traitor: hain; safely beached: güvenle karaya oturtulmuş"
            }
        ]
    },

    # Page 15 (Sentences 281-300)
    {
        "page_no": 15,
        "title": "The Treasure Cave and Safe Return Home",
        "tr_title": "Hazine Mağarası ve Eve Güvenli Dönüş",
        "vocab_focus": [
            ("ingot", "külçe (altın/gümüş)"),
            ("doubloon", "dublon (eski İspanyol altın sikkesi)"),
            ("guinea", "gine (İngiliz altın parası)"),
            ("moidore", "Portekiz altın sikkesi"),
            ("cave", "mağara"),
            ("treasure", "hazine"),
            ("voyage", "deniz yolculuğu"),
            ("rich", "zengin")
        ],
        "sentences": [
            {
                "id": 281,
                "text": "I freed my shoulder, bound my wound with a kerchief, and hurried through the dark woods.",
                "translation": "Omzumu kurtardım, yaramı bir mendille sardım ve karanlık ormanın içinden aceleyle ilerledim.",
                "notes": "free: kurtarmak; bind wound: yarayı sarmak"
            },
            {
                "id": 282,
                "text": "When I crept into the silent stockade, a screeching voice pierced the darkness: \"Pieces of eight!\"",
                "translation": "Sessiz hisara usulca girdiğimde, cırtlak bir ses karanlığı deldi: \"Sekiz parçalık altınlar!\"",
                "notes": "screeching voice: cırtlak ses; pierce darkness: karanlığı delip geçmek"
            },
            {
                "id": 283,
                "text": "It was Silver's green parrot; the pirates had captured the fort while I was away!",
                "translation": "Bu Silver'ın yeşil papağanıydı; ben yokken korsanlar kaleyi ele geçirmişti!",
                "notes": "capture the fort: kaleyi zapt etmek / ele geçirmek"
            },
            {
                "id": 284,
                "text": "The pirates surrounded me, but Long John Silver surprisingly stepped in to protect my life.",
                "translation": "Korsanlar etrafımı sardı fakat Uzun John Silver şaşırtıcı bir şekilde hayatımı korumak için araya girdi.",
                "notes": "step in to protect: korumak için araya girmek; surprisingly: şaşırtıcı şekilde"
            },
            {
                "id": 285,
                "text": "\"The boy has spirit, and I will not let you murder him,\" Silver growled at his disgruntled men.",
                "translation": "\"Çocukta yürek var ve onu öldürmenize izin vermeyeceğim,\" diye homurdandı Silver hoşnutsuz adamlarına.",
                "notes": "have spirit: cesur / yürekli olmak; disgruntled: hoşnutsuz"
            },
            {
                "id": 286,
                "text": "The next morning, Dr. Livesey arrived under a flag of truce to tend to the wounded pirates.",
                "translation": "Ertesi sabah Doktor Livesey, yaralı korsanları tedavi etmek için beyaz bayrak altında geldi.",
                "notes": "tend to: bakmak, tedavi etmek; flag of truce: ateşkes bayrağı"
            },
            {
                "id": 287,
                "text": "He whispered to me that Ben Gunn had already dug up the treasure months ago!",
                "translation": "Kulağıma fısıldayarak, Ben Gunn'ın hazineyi aylar önce kazıp çıkardığını söyledi!",
                "notes": "dig up: kazıp çıkarmak; whisper: fısıldamak"
            },
            {
                "id": 288,
                "text": "That was why the doctor had willingly handed the useless map over to Silver.",
                "translation": "İşte doktorun işe yaramaz haritayı Silver'a gönüllü olarak vermesinin sebebi buydu.",
                "notes": "willingly: isteyerek, gönüllüce; hand over: teslim etmek"
            },
            {
                "id": 289,
                "text": "Silver led his eager pirates across the island following Flint's map to the marked cross.",
                "translation": "Silver hevesli korsanlarını adanın üzerinden geçirerek Flint'in haritasındaki işaretli haça götürdü.",
                "notes": "lead across: üzerinden geçirerek götürmek; marked cross: işaretli haç"
            },
            {
                "id": 290,
                "text": "When they reached the spot, they found only a huge empty hole in the ground.",
                "translation": "Noktaya vardıklarında toprakta yalnızca devasa bomboş bir çukur buldular.",
                "notes": "empty hole: boş çukur; reach spot: noktaya varmak"
            },
            {
                "id": 291,
                "text": "The pirates screamed that Silver had betrayed them and drew their weapons to butcher us.",
                "translation": "Korsanlar Silver'ın kendilerine ihanet ettiğini haykırdılar ve bizi katletmek için silahlarını çektiler.",
                "notes": "betray: ihanet etmek; butcher: kasap gibi doğramak, katletmek"
            },
            {
                "id": 292,
                "text": "At that moment, three rifle shots blasted from the bushes, dropping two mutineers instantly.",
                "translation": "Tam o anda çalılıklardan üç tüfek sesi patladı ve iki isyancıyı anında yere serdi.",
                "notes": "rifle shot: tüfek atışı; blast: patlamak"
            },
            {
                "id": 293,
                "text": "Dr. Livesey, Gray, and Ben Gunn stepped forth with smoking barrels, scattering the remaining pirates.",
                "translation": "Doktor Livesey, Gray ve Ben Gunn namlularından dumanlar tüterek öne çıktılar ve kalan korsanları darmadağın ettiler.",
                "notes": "smoking barrels: dumanı tüten namlular; scatter: püskürtmek, dağıtmak"
            },
            {
                "id": 294,
                "text": "Silver surrendered instantly, humbly begging the doctor for mercy and protection.",
                "translation": "Silver derhal teslim oldu, alçakgönüllülükle doktordan merhamet ve koruma diledi.",
                "notes": "surrender instantly: anında teslim olmak; beg for mercy: merhamet dilemek"
            },
            {
                "id": 295,
                "text": "We marched across the island to Ben Gunn's secret cavern high in the granite hill.",
                "translation": "Granit tepenin doruklarındaki Ben Gunn'ın gizli mağarasına doğru adayı boydan boya yürüdük.",
                "notes": "granite hill: granit tepe; secret cavern: gizli mağara"
            },
            {
                "id": 296,
                "text": "There, stacked in golden heaps, lay the seven hundred thousand pounds of Captain Flint's fortune!",
                "translation": "Orada, altın yığınları halinde dizilmiş, Kaptan Flint'in yedi yüz bin sterlinlik serveti yatıyordu!",
                "notes": "golden heaps: altın yığınları; fortune: servet"
            },
            {
                "id": 297,
                "text": "Doubloons, guineas, gold bars, and jewels of all nations glittered in the firelight.",
                "translation": "Tüm ulusların dublonları, gineleri, altın külçeleri ve mücevherleri ateş ışığında pırıl pırıl parlıyordu.",
                "notes": "gold bars: altın külçeleri; glitter in firelight: ateş ışığında parıldamak"
            },
            {
                "id": 298,
                "text": "For days, we carried the heavy gold down to the Hispaniola and stowed it deep in the hold.",
                "translation": "Günlerce ağır altını Hispaniola'ya taşıdık ve ambarın derinliklerine istifledik.",
                "notes": "stow deep: derine istiflemek; ship's hold: gemi ambarı"
            },
            {
                "id": 299,
                "text": "We marooned the remaining three wicked pirates on the island and set sail for England with rich hearts.",
                "translation": "Kalan üç hain korsanı adada bıraktık ve zenginleşmiş yüreklerle İngiltere'ye doğru yelken açtık.",
                "notes": "set sail: yelken açmak; rich hearts: zengin / sevinçli yürekler"
            },
            {
                "id": 300,
                "text": "Long John Silver escaped at a Spanish port with a sack of gold, but none of us ever regretted his loss.",
                "translation": "Uzun John Silver bir İspanyol limanında bir çuval altınla kaçtı ama hiçbirimiz onun kaybına asla üzülmedik.",
                "notes": "sack of gold: bir çuval altın; regret loss: kaybına üzülmek / pişman olmak"
            }
        ]
    }
]

def main():
    total_pages = len(pages_data)
    total_sentences = sum(len(p["sentences"]) for p in pages_data)
    total_vocab = sum(len(p.get("vocab_focus", [])) for p in pages_data)

    print(f"Book 20 Data Verification:")
    print(f"Total Pages: {total_pages} (Target: 15)")
    print(f"Total Sentences: {total_sentences} (Target: 300)")
    print(f"Total Vocab Items: {total_vocab} (Target: 120)")

    assert total_pages == 15, f"Expected 15 pages, got {total_pages}"
    assert total_sentences == 300, f"Expected 300 sentences, got {total_sentences}"
    assert total_vocab == 120, f"Expected 120 vocab items, got {total_vocab}"

    # Verify sentence IDs are continuous 1..300
    ids = []
    for p in pages_data:
        for s in p["sentences"]:
            ids.append(s["id"])
    assert ids == list(range(1, 301)), "Sentence IDs are not continuous 1..300!"

    out_file = os.path.join(os.path.dirname(__file__), "book_20_data.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('BOOK_TITLE = "Treasure Island"\n')
        f.write('AUTHOR = "Robert Louis Stevenson"\n')
        f.write("PAGES_DATA = ")
        import pprint
        f.write(pprint.pformat(pages_data, indent=4, width=120))
        f.write("\n")

    print(f"Successfully wrote {out_file}")

if __name__ == "__main__":
    main()
