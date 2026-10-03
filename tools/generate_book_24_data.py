# -*- coding: utf-8 -*-
"""
Generator script for Book 24: "White Fang" by Jack London.
15 Pages x 20 Sentences = Exactly 300 Sentences (Continuous IDs 1 to 300).
8 Vocabulary Focus items per page = Exactly 120 Target Vocabulary Items.
CEFR Level: A2-B1 Graded Reader Edition.
"""

import os

pages_data = [
    # Page 1 (Sentences 1-20)
    {
        "page_no": 1,
        "title": "The Trail of the Meat in the Wild North",
        "tr_title": "Kuzeyin Vahşi Yollarında",
        "vocab_focus": [
            ("Wild", "Vahşi Doğa, ıssız kuzey"),
            ("frost", "şiddetli ayaz, don"),
            ("spruce", "ladin ağacı"),
            ("sled", "köpek kızağı"),
            ("coffin", "tabut"),
            ("pack", "kurt sürüsü"),
            ("famine", "kıtlık, açlık"),
            ("howl", "kurt uluması")
        ],
        "sentences": [
            {
                "id": 1,
                "text": "Dark spruce forest frowned on either side the frozen waterway of the Far North.",
                "translation": "Uzak Kuzey'in donmuş su yolunun iki yanında koyu renkli ladin ormanı çatık kaşlarla dikiliyordu.",
                "notes": "spruce forest: ladin ormanı; frozen waterway: donmuş su yolu"
            },
            {
                "id": 2,
                "text": "The trees had been stripped by a recent wind of their white covering of frost.",
                "translation": "Ağaçlar, son rüzgar yüzünden beyaz don ve kırağı örtülerinden tamamen sıyrılmıştı.",
                "notes": "strip: sıyırmak, soymak; covering of frost: don / kırağı örtüsü"
            },
            {
                "id": 3,
                "text": "A vast silence reigned over the desolate land: it was the Wild, the savage, frozen Northland.",
                "translation": "Issız toprakların üzerinde uçsuz bucaksız bir sessizlik hüküm sürüyordu: burası Vahşi Doğa'ydı, donmuş acımasız Kuzey diyarıydı.",
                "notes": "desolate land: ıssız topraklar; reign: hüküm sürmek"
            },
            {
                "id": 4,
                "text": "Down the frozen river toiled a team of six wolf-dogs, hauling a heavy birch-bark sled.",
                "translation": "Donmuş nehir boyunca altı kurt köpeğinden oluşan bir takım, huş kabuğundan yapılmış ağır bir kızağı çekerek güçbela ilerliyordu.",
                "notes": "haul: çekmek, sürüklemek; birch-bark sled: huş kabuğu kızak"
            },
            {
                "id": 5,
                "text": "On the sled, lashed securely with rawhide ropes, lay an oblong wooden box: a coffin.",
                "translation": "Kızağın üzerinde ham deri iplerle sıkıca bağlanmış dikdörtgen tahta bir kutu yatıyordu: bir tabut.",
                "notes": "lashed securely: sıkıca bağlanmış; coffin: tabut"
            },
            {
                "id": 6,
                "text": "Two men, Bill and Henry, walked before and behind the sled, bundled in heavy furs.",
                "translation": "Bill ve Henry adında iki adam, ağır kürkler içine sarınmış olarak kızağın önünde ve arkasında yürüyordu.",
                "notes": "bundled in furs: kürklere sarınmış; sled: kızak"
            },
            {
                "id": 7,
                "text": "Their breath came out in crystal white plumes that froze immediately upon their beards.",
                "translation": "Nefesleri, sakalları üzerinde anında donan kristal beyaz dumanlar halinde çıkıyordu.",
                "notes": "crystal plumes: kristal dumanlar; freeze upon beards: sakalında donmak"
            },
            {
                "id": 8,
                "text": "They were carrying the dead body of an adventurous young lord back to civilization.",
                "translation": "Maceraperest genç bir lordun cansız bedenini medeniyete geri taşıyorlardı.",
                "notes": "adventurous lord: maceracı lord; civilization: medeniyet"
            },
            {
                "id": 9,
                "text": "The cold was fifty degrees below zero, biting deep into their flesh and marrow.",
                "translation": "Soğuk sıfırın altında elli dereceydi; etlerine ve kemiklerinin iliğine kadar işliyordu.",
                "notes": "below zero: sıfırın altında; marrow: kemik iliği"
            },
            {
                "id": 10,
                "text": "Behind them, scarcely a hundred yards away, came the haunting, mournful cry of a hunting wolf pack.",
                "translation": "Arkalarından, henüz yüz metre bile uzakta olmayan bir mesafeden, avlanan bir kurt sürüsünün yürek parçalayıcı hazin uluması geldi.",
                "notes": "mournful cry: hazin / kederli çığlık; wolf pack: kurt sürüsü"
            },
            {
                "id": 11,
                "text": "It was a cry of hunger, fierce and desperate in the grip of the winter famine.",
                "translation": "Bu, kış kıtlığının pençesinde azgınlaşmış ve çaresiz kalmış bir açlık haykırışıydı.",
                "notes": "cry of hunger: açlık haykırışı; winter famine: kış kıtlığı"
            },
            {
                "id": 12,
                "text": "\"They're after us, Henry,\" Bill said, looking over his shoulder with fearful eyes.",
                "translation": "\"Peşimizdeler Henry,\" dedi Bill, korku dolu gözlerle omzunun üzerinden geriye bakarak.",
                "notes": "after us: peşimizde; fearful eyes: korku dolu gözler"
            },
            {
                "id": 13,
                "text": "\"Meat is scarce, and the famine is hard upon them,\" Henry answered grimly.",
                "translation": "\"Et kıt, kıtlık da tepelerine fena çökmüş durumda,\" diye yanıtladı Henry kasvetle.",
                "notes": "meat is scarce: et kıt; grimly: kasvetle"
            },
            {
                "id": 14,
                "text": "They made camp when darkness fell, tethering the sled dogs securely to prevent escape.",
                "translation": "Karanlık çöktüğünde kamp kurdular, kaçmalarını önlemek için kızak köpeklerini emniyetle bağladılar.",
                "notes": "tether: bağlamak; make camp: kamp kurmak"
            },
            {
                "id": 15,
                "text": "While feeding the dogs their frozen fish, Bill noticed an extra wolf sitting in the shadows.",
                "translation": "Köpeklere donmuş balıklarını yedirirken Bill, gölgelerin içinde oturan fazladan bir kurt fark etti.",
                "notes": "frozen fish: donmuş balık; extra wolf: fazladan bir kurt"
            },
            {
                "id": 16,
                "text": "\"I fed seven dogs tonight, Henry, but we only have six dogs in our team!\"",
                "translation": "\"Bu gece yedi köpeğe yemek verdim Henry, oysa takımımızda sadece altı köpek var!\"",
                "notes": "feed dogs: köpekleri beslemek; team: kızak takımı"
            },
            {
                "id": 17,
                "text": "A daring she-wolf had slipped into the circle of firelight to steal a fish.",
                "translation": "Cüretkar bir dişi kurt, bir balık çalmak için ateş ışığının çemberine süzülmüştü.",
                "notes": "she-wolf: dişi kurt; circle of firelight: ateş çemberi"
            },
            {
                "id": 18,
                "text": "She was reddish-gray, looking like a large sled dog, but moving with the stealth of a wild predator.",
                "translation": "Kızılımsı gri renkteydi; iri bir kızak köpeğine benziyordu fakat vahşi bir yırtıcının sinsiliğiyle hareket ediyordu.",
                "notes": "stealth: sinsi hareket; predator: yırtıcı hayvan"
            },
            {
                "id": 19,
                "text": "Next morning, their lead dog Fatty was gone, lured into the forest by the clever she-wolf.",
                "translation": "Ertesi sabah, önder köpekleri Fatty kaybolmuştu; kurnaz dişi kurt tarafından ormanın içine çekilip tuzağa düşürülmüştü.",
                "notes": "lure into: kandırıp içine çekmek; lead dog: önder köpek"
            },
            {
                "id": 20,
                "text": "Night by night, dog after dog vanished into the jaws of the starving, relentless pack.",
                "translation": "Geceler geçtikçe köpekler birbiri ardına açlıktan kırılan acımasız sürünün çeneleri arasında kayboldu.",
                "notes": "relentless pack: acımasız sürü; starving: açlıktan kırılan"
            }
        ]
    },

    # Page 2 (Sentences 21-40)
    {
        "page_no": 2,
        "title": "The She-wolf Kiche and the Pack",
        "tr_title": "Dişi Kurt Kiche ve Kurt Sürüsü",
        "vocab_focus": [
            ("she-wolf", "dişi kurt"),
            ("cartridge", "mermi, fişek"),
            ("mate", "eş (hayvanlarda)"),
            ("ambush", "pusu"),
            ("famine", "kıtlık"),
            ("wilderness", "yaban hayatı, ıssız doğa"),
            ("rescue", "kurtarma"),
            ("instinct", "içgüdü")
        ],
        "sentences": [
            {
                "id": 21,
                "text": "Bill lost his temper when a third dog was lured away and devoured by the wolves.",
                "translation": "Üçüncü bir köpek de kandırılıp kurtlar tarafından parçalanınca Bill öfkesine hakim olamadı.",
                "notes": "devour: parçalayıp yemek; lose temper: öfkelenmek"
            },
            {
                "id": 22,
                "text": "He grabbed his rifle with only three cartridges remaining and pursued the she-wolf into the trees.",
                "translation": "Yalnızca üç fişeği kalan tüfeğini kaptı ve dişi kurdu ağaçların arasına doğru kovaladı.",
                "notes": "cartridge: tüfek fişeği / mermi; pursue: kovalamak"
            },
            {
                "id": 23,
                "text": "Henry heard two rifle shots, a terrible canine snarling, and then a man's dying shriek.",
                "translation": "Henry iki el tüfek sesi, ardından korkunç köpek hırlamaları ve son olarak bir adamın can çekişen çığlığını duydu.",
                "notes": "canine snarling: köpek hırlaması; dying shriek: can çekişme çığlığı"
            },
            {
                "id": 24,
                "text": "Bill was dead, and Henry was left alone with two exhausted dogs and the coffin.",
                "translation": "Bill ölmüştü ve Henry iki bitkin köpek ve tabutla yapayalnız kalmıştı.",
                "notes": "exhausted dogs: bitkin köpekler; left alone: yalnız kaldı"
            },
            {
                "id": 25,
                "text": "That night, the wolves encircled Henry's tiny fire, their glowing amber eyes creeping within yards.",
                "translation": "O gece kurtlar Henry'nin minik ateşini çembere aldı; parıldayan kehribar gözleri birkaç metreye kadar yaklaştı.",
                "notes": "amber eyes: kehribar gözler; encircle: çembere almak"
            },
            {
                "id": 26,
                "text": "The she-wolf crept boldest of all, staring at him with strange familiarity in her gaze.",
                "translation": "Dişi kurt hepsinden daha cesurca sokuldu; bakışlarında tuhaf bir aşinalıkla ona gözlerini dikti.",
                "notes": "strange familiarity: tuhaf aşinalık; boldest: en cesur"
            },
            {
                "id": 27,
                "text": "Henry threw burning brands from the fire to keep the hungry beasts from leaping upon him.",
                "translation": "Henry, aç canavarların üzerine atlamasını engellemek için ateşten yanan odun parçaları fırlattı.",
                "notes": "burning brands: yanan odunlar; hungry beasts: aç canavarlar"
            },
            {
                "id": 28,
                "text": "Just as his wood supply ended and he prepared to die, a team of armed dog-sleds burst through the snow.",
                "translation": "Tam odun stoku bittiği ve ölüme hazırlandığı sırada, silahlı köpek kızaklarından oluşan bir kafile karları yararak çıkageldi.",
                "notes": "wood supply: odun stoku; burst through: yararak çıkagelmek"
            },
            {
                "id": 29,
                "text": "The rescue party fired their rifles, driving the wolf pack back into the shadowy wilderness.",
                "translation": "Kurtarma ekibi tüfeklerini ateşleyerek kurt sürüsünü karanlık yabanın içine geri püskürttü.",
                "notes": "rescue party: kurtarma ekibi; drive back: geri püskürtmek"
            },
            {
                "id": 30,
                "text": "The pack retreated northward, following a great herd of caribou across the Mackenzie River.",
                "translation": "Sürü kuzeye doğru çekildi, Mackenzie Nehri boyunca uzanan büyük bir rengeyiği sürüsünü takip etti.",
                "notes": "caribou: rengeyiği; retreat: geri çekilmek"
            },
            {
                "id": 31,
                "text": "They hunted successfully and the famine ended; full bellies brought playful affection among the wolves.",
                "translation": "Başarıyla avlandılar ve kıtlık son buldu; doyan karınlar kurtlar arasında neşeli bir yakınlık getirdi.",
                "notes": "full bellies: doymuş karınlar; playful affection: neşeli yakınlık"
            },
            {
                "id": 32,
                "text": "Several fierce males fought bloody battles to win the favor of the reddish she-wolf.",
                "translation": "Kızılımsı dişi kurdun sevgisini kazanmak için birkaç azılı erkek kurt kanlı kavgalara tutuştu.",
                "notes": "win favor: sevgisini kazanmak; bloody battles: kanlı savaşlar"
            },
            {
                "id": 33,
                "text": "An old, battle-scarred wolf with one eye, called One Eye, vanquished all younger rivals.",
                "translation": "Tek Göz adı verilen, yaralarla dolu tek gözlü yaşlı bir kurt, kendinden genç bütün rakiplerini yendi.",
                "notes": "One Eye: Tek Göz; battle-scarred: savaş yaralarıyla dolu; vanquish: yenmek"
            },
            {
                "id": 34,
                "text": "The she-wolf accepted the victorious veteran as her chosen mate and hunting partner.",
                "translation": "Dişi kurt, bu muzaffer emektarı seçtiği eşi ve av yoldaşı olarak kabul etti.",
                "notes": "victorious veteran: muzaffer emektar; chosen mate: seçilmiş eş"
            },
            {
                "id": 35,
                "text": "They left the main pack and traveled together as spring began melting the river ice.",
                "translation": "İlkbahar nehir buzlarını eritmeye başlarken ana sürüden ayrıldılar ve birlikte yol aldılar.",
                "notes": "main pack: ana sürü; melt river ice: nehir buzunu eritmek"
            },
            {
                "id": 36,
                "text": "The she-wolf grew heavy with young, seeking a safe, dry shelter to bear her cubs.",
                "translation": "Dişi kurt yavrularla ağırlaştı; eniklerini doğurmak için güvenli, kuru bir sığınak aramaya koyuldu.",
                "notes": "heavy with young: gebe; bear cubs: yavrular doğurmak"
            },
            {
                "id": 37,
                "text": "Along the bank of a tributary stream, she discovered a limestone cave sheltered by spruce roots.",
                "translation": "Bir yan derenin kıyısında, ladin kökleriyle korunan kireçtaşından bir mağara keşfetti.",
                "notes": "tributary stream: yan kol dere; limestone cave: kireçtaşı mağarası"
            },
            {
                "id": 38,
                "text": "It was dry, warm, and hidden from the eyes of dangerous larger predators.",
                "translation": "Burası kuru, sıcak ve tehlikeli iri yırtıcıların gözlerinden uzaktı.",
                "notes": "dry and warm: kuru ve sıcak; hidden: gizlenmiş"
            },
            {
                "id": 39,
                "text": "One Eye hunted meat tirelessly, bringing rabbits and ptarmigan birds to his mate's lair.",
                "translation": "Tek Göz yorulmak bilmeden et avladı; eşinin inine tavşanlar ve kar tavukları taşıdı.",
                "notes": "tirelessly: yorulmak bilmeden; ptarmigan: kar tavuğu; lair: hayvan ini"
            },
            {
                "id": 40,
                "text": "Inside that dark earthen den, life stirred quietly as five tiny newborn cubs entered the world.",
                "translation": "O karanlık toprak inin içinde, yeni doğan beş minik enik dünyaya adım atarken hayat usulca kıpırdandı.",
                "notes": "earthen den: toprak in; life stirred: hayat kıpırdadı"
            }
        ]
    },

    # Page 3 (Sentences 41-60)
    {
        "page_no": 3,
        "title": "The Birth of the Gray Cub in the Cave",
        "tr_title": "Mağarada Gri Yavrunun Doğuşu",
        "vocab_focus": [
            ("cub", "yırtıcı hayvan yavrusu, enik"),
            ("gray", "boz, gri"),
            ("cave", "mağara"),
            ("entrance", "giriş"),
            ("snarl", "hırlamak"),
            ("meat", "et, av"),
            ("blind", "kör"),
            ("whimper", "sızlanmak, viyaklamak")
        ],
        "sentences": [
            {
                "id": 41,
                "text": "Four of the cubs were reddish like their mother, but one was different from all the rest.",
                "translation": "Yavruların dördü anneleri gibi kızılımsı renkteydi fakat biri diğerlerinden tamamen farklıydı.",
                "notes": "reddish: kızılımsı; different from rest: diğerlerinden farklı"
            },
            {
                "id": 42,
                "text": "He was an exact copy of his father: a true gray wolf from the tip of his nose to his tail.",
                "translation": "Babasının tıpatıp aynısıydı: burnunun ucundan kuyruğuna kadar tam bir boz kurttu.",
                "notes": "exact copy: tıpatıp aynısı; gray wolf: boz kurt"
            },
            {
                "id": 43,
                "text": "He was the fiercest, strongest, and most inquisitive cub in the entire litter.",
                "translation": "Bütün batındaki en azılı, en güçlü ve en meraklı yavru oydu.",
                "notes": "inquisitive: meraklı; litter: bir doğumda doğan yavrular"
            },
            {
                "id": 44,
                "text": "At first, his eyes were closed, and his whole world consisted of warmth, milk, and his mother's tongue.",
                "translation": "İlk başta gözleri kapalıydı ve bütün dünyası sıcaklıktan, sütten ve annesinin dilinden ibaretti.",
                "notes": "at first: ilk başta; consist of: ...den oluşmak"
            },
            {
                "id": 45,
                "text": "When his eyes opened, he discovered that the cave was dark except for one luminous circle: the entrance.",
                "translation": "Gözleri açıldığında, mağaranın parıldayan tek bir daire—yani giriş—dışında karanlık olduğunu keşfetti.",
                "notes": "luminous circle: ışıklı daire; entrance: mağara girişi"
            },
            {
                "id": 46,
                "text": "To the gray cub, that glowing white circle was the wall of the world where the light lived.",
                "translation": "Gri yavru için parıldayan o beyaz daire, ışığın yaşadığı dünya duvarıydı.",
                "notes": "glowing circle: parıldayan daire; wall of the world: dünyanın duvarı"
            },
            {
                "id": 47,
                "text": "His mother, the she-wolf, guarded the entrance fiercely, forbidding the cubs to venture into the light.",
                "translation": "Anneleri olan dişi kurt, yavruların ışığa yaklaşmasını yasaklayarak girişi hırsla korudu.",
                "notes": "forbid: yasaklamak; venture into: içine adım atmak"
            },
            {
                "id": 48,
                "text": "Whenever the cub crawled toward the white doorway, a cuff from her soft paw rolled him back.",
                "translation": "Yavru o beyaz kapı aralığına doğru her emeklediğinde, annesinin yumuşak patisinden bir tokat onu geri yuvarlardı.",
                "notes": "cuff from paw: patiden bir tokat; roll back: geri yuvarlamak"
            },
            {
                "id": 49,
                "text": "He learned his first lesson of life: obedience to the mother law.",
                "translation": "Hayatının ilk dersini öğrendi: anne kanununa itaat.",
                "notes": "first lesson: ilk ders; obedience: itaat"
            },
            {
                "id": 50,
                "text": "A terrible second famine struck the northern forests in late spring.",
                "translation": "İlkbaharın sonlarında kuzey ormanlarını korkunç ikinci bir kıtlık vurdu.",
                "notes": "famine struck: kıtlık vurdu; late spring: ilkbahar sonu"
            },
            {
                "id": 51,
                "text": "Game grew so scarce that One Eye had to hunt night and day without finding a single rabbit.",
                "translation": "Av hayvanları o kadar azaldı ki Tek Göz tek bir tavşan bile bulamadan gece gündüz avlanmak zorunda kaldı.",
                "notes": "game grew scarce: av kıtlaştı; hunt night and day: gece gündüz avlanmak"
            },
            {
                "id": 52,
                "text": "One by one, the four reddish brothers and sisters whimpered, grew cold, and died of hunger.",
                "translation": "Dört kızıl kardeş birer birer inledi, soğudu ve açlıktan can verdi.",
                "notes": "whimper: inlemek; die of hunger: açlıktan ölmek"
            },
            {
                "id": 53,
                "text": "Only the sturdy gray cub survived, sucking the few drops of milk his starving mother could produce.",
                "translation": "Yalnızca sağlam yapılı gri yavru hayatta kaldı, açlıktan bitap annesinin üretebildiği birkaç damla sütü emdi.",
                "notes": "sturdy cub: sağlam yapılı yavru; survive: hayatta kalmak"
            },
            {
                "id": 54,
                "text": "Then father One Eye went out to hunt along the rocky canyon and never returned.",
                "translation": "Ardından baba Tek Göz kayalık kanyon boyunca avlanmaya çıktı ve bir daha asla geri dönmedi.",
                "notes": "rocky canyon: kayalık kanyon; never returned: asla dönmedi"
            },
            {
                "id": 55,
                "text": "Near a beaver dam, the she-wolf found his bones and the tracks of an enormous female lynx.",
                "translation": "Bir kunduz bendi yakınında dişi kurt, onun kemiklerini ve devasa bir dişi vaşağın izlerini buldu.",
                "notes": "beaver dam: kunduz bendi; female lynx: dişi vaşak"
            },
            {
                "id": 56,
                "text": "The brave she-wolf now had to leave her sole surviving cub alone in the cave to hunt for meat.",
                "translation": "Cesur dişi kurt artık et avlamak için hayatta kalan tek yavrusunu mağarada yalnız bırakmak zorundaydı.",
                "notes": "sole surviving cub: hayatta kalan tek yavru; hunt for meat: et avlamak"
            },
            {
                "id": 57,
                "text": "Left by himself, the gray cub looked longingly at the glowing circle of sunshine.",
                "translation": "Kendi başına kalan gri yavru, güneş ışığının parıldayan çemberine özlemle baktı.",
                "notes": "look longingly: özlemle bakmak; glowing circle: parıldayan çember"
            },
            {
                "id": 58,
                "text": "Fear held him back for a time, but powerful natural curiosity drew him forward.",
                "translation": "Korku onu bir süre geride tuttu fakat güçlü doğal merakı onu ileri doğru çekti.",
                "notes": "natural curiosity: doğal merak; draw forward: ileri çekmek"
            },
            {
                "id": 59,
                "text": "He crawled on trembling paws across the stone floor straight toward the light.",
                "translation": "Titreyen patileri üzerinde taş zemin boyunca dosdoğru ışığa doğru emekledi.",
                "notes": "trembling paws: titreyen patiler; straight toward: dosdoğru ...e doğru"
            },
            {
                "id": 60,
                "text": "He stepped through the luminous opening and plunged headlong into the great unknown world outside.",
                "translation": "Işıklı kapı aralığından dışarı adım attı ve dışarıdaki bilinmeyen o koca dünyanın içine baş aşağı yuvarlandı.",
                "notes": "plunge headlong: baş aşağı yuvarlanmak; unknown world: bilinmeyen dünya"
            }
        ]
    },

    # Page 4 (Sentences 61-80)
    {
        "page_no": 4,
        "title": "The Law of Meat and the World Outside",
        "tr_title": "Et Yasası ve Dış Dünyaya İlk Adım",
        "vocab_focus": [
            ("ptarmigan", "kar tavuğu"),
            ("weasel", "gelincik"),
            ("hawk", "şahin, yırtıcı kuş"),
            ("fang", "sivri köpek dişi"),
            ("flesh", "çiğ et, beden"),
            ("prey", "av"),
            ("predator", "yırtıcı hayvan"),
            ("lynx", "vaşak")
        ],
        "sentences": [
            {
                "id": 61,
                "text": "The gray cub rolled down the mossy bank, landing with a yelp of shock among pine needles.",
                "translation": "Gri yavru yosunlu bayırdan aşağı yuvarlandı, çam iğnelerinin arasına şaşkın bir ciyaklamayla düştü.",
                "notes": "mossy bank: yosunlu bayır; pine needles: çam iğneleri"
            },
            {
                "id": 62,
                "text": "He discovered that the world did not end at the cave mouth, but expanded endlessly under the sky.",
                "translation": "Dünyanın mağara ağzında bitmediğini, gökyüzünün altında sonsuzca genişlediğini keşfetti.",
                "notes": "cave mouth: mağara ağzı; expand endlessly: sonsuzca genişlemek"
            },
            {
                "id": 63,
                "text": "Everything was strange and terrifying: waving branches, buzzing insects, and the vast open air.",
                "translation": "Her şey garip ve ürkütücüydü: sallanan dallar, vızıldayan böcekler ve engin açık hava.",
                "notes": "waving branches: sallanan dallar; buzzing insects: vızıldayan böcekler"
            },
            {
                "id": 64,
                "text": "A sudden shadow fell over him as a great hawk swooped down, narrowly missing him with razor talons.",
                "translation": "Koca bir şahin tepeden süzülüp jilet gibi pençeleriyle onu kıl payı ıskalarken üzerine ani bir gölge düştü.",
                "notes": "hawk swooped down: şahin süzüldü; razor talons: jilet gibi pençeler"
            },
            {
                "id": 65,
                "text": "He scrambled under a fallen birch log, learning that danger rained down from the sky.",
                "translation": "Devrilmiş bir huş kütüğünün altına sindi; tehlikenin gökten yağabileceğini böylece öğrendi.",
                "notes": "scramble under: altına sıvışmak; danger rained down: tehlike yağdı"
            },
            {
                "id": 66,
                "text": "Under the log, he stumbled upon a nest of seven young ptarmigan chicks.",
                "translation": "Kütüğün altında yedi yavru kar tavuğu civcivinden oluşan bir yuvaya rastladı.",
                "notes": "stumble upon: tesadüfen rastlamak; ptarmigan chicks: kar tavuğu civcivleri"
            },
            {
                "id": 67,
                "text": "They were soft and fluttering; his jaw snapped shut on one, and warm meat filled his mouth.",
                "translation": "Yumuşacıktılar ve pırpır ediyorlardı; çenesi birinin üzerinde şak diye kapandı ve ağzı sıcak etle doldu.",
                "notes": "snap shut: şak diye kapanmak; warm meat: taze ılık et"
            },
            {
                "id": 68,
                "text": "He devoured all seven chicks, feeling the raw savage joy of the successful predator.",
                "translation": "Yedi civcivin hepsini yedi, başarılı bir yırtıcının o çiğ ve vahşi sevincini tattı.",
                "notes": "devour: silip süpürmek; savage joy: vahşi sevinç"
            },
            {
                "id": 69,
                "text": "Then the mother ptarmigan flew at him furiously, pecking his tender nose with her sharp beak.",
                "translation": "Ardından anne kar tavuğu hiddetle üzerine uçtu, sivri gagasıyla yavrunun narin burnunu gagaladı.",
                "notes": "sharp beak: sivri gaga; tender nose: narin burun"
            },
            {
                "id": 70,
                "text": "He fought back with ferocious snarls, tasting blood for the first time in his life.",
                "translation": "Vahşi hırlamalarla karşılık verdi, hayatında ilk defa kan tadını aldı.",
                "notes": "ferocious snarls: azgın hırlamalar; taste blood: kan tadı almak"
            },
            {
                "id": 71,
                "text": "Next, he encountered a fierce, slender weasel who leaped straight for his throat.",
                "translation": "Derken dosdoğru boğazına atılan azılı, ince uzun bir gelincikle karşılaştı.",
                "notes": "slender weasel: narin gelincik; leap for throat: boğaza atılmak"
            },
            {
                "id": 72,
                "text": "The little weasel's needle teeth bit deep, and the cub would have died had not his mother arrived.",
                "translation": "Minik gelinciğin iğne gibi dişleri derine battı; eğer annesi yetişmeseydi yavru ölmüş olacaktı.",
                "notes": "needle teeth: iğne dişler; had not mother arrived: annesi yetişmeseydi"
            },
            {
                "id": 73,
                "text": "The she-wolf crushed the weasel in one snap of her powerful jaws and licked her cub's wounds.",
                "translation": "Dişi kurt güçlü çenesinin tek bir kapanışıyla gelinciği ezdi ve yavrusunun yaralarını yaladı.",
                "notes": "crush in one snap: tek ısırıkta ezmek; lick wounds: yaraları yalamak"
            },
            {
                "id": 74,
                "text": "The gray cub learned the fundamental Law of the Wild: Eat or be eaten; kill or be killed.",
                "translation": "Boz yavru, Vahşi Doğa'nın en temel Yasasını öğrendi: Ye ya da yem ol; öldür ya da öldürül.",
                "notes": "Law of the Wild: Vahşi Doğa Kanunu; eat or be eaten: ye ya da yem ol"
            },
            {
                "id": 75,
                "text": "Life was meat, and meat was life; all living things were either predators or prey.",
                "translation": "Hayat demek etti, et demek hayattı; tüm canlılar ya avcıydı ya da av.",
                "notes": "predator or prey: avcı ya da av"
            },
            {
                "id": 76,
                "text": "A few days later, the vengeful female lynx tracked the she-wolf to her cave.",
                "translation": "Birkaç gün sonra intikam peşindeki dişi vaşak, dişi kurdun izini mağarasına kadar sürdü.",
                "notes": "vengeful: intikamcı; track to cave: izini mağaraya sürmek"
            },
            {
                "id": 77,
                "text": "A savage battle exploded in the dark den, teeth clashing and claws ripping flesh.",
                "translation": "Karanlık inde vahşi bir kavga patlak verdi; dişler çarpıştı, pençeler etleri parçaladı.",
                "notes": "savage battle: vahşi dövüş; rip flesh: eti parçalamak"
            },
            {
                "id": 78,
                "text": "The gray cub bravely attacked the lynx's hind leg, sinking his little sharp teeth into her tendon.",
                "translation": "Gri yavru cesurca vaşağın arka bacağına saldırdı, minik sivri dişlerini hayvanın kirişine geçirdi.",
                "notes": "hind leg: arka bacak; sink teeth: dişlerini geçirmek"
            },
            {
                "id": 79,
                "text": "Together, mother and son slaughtered the great cat, winning a mountain of fresh meat.",
                "translation": "Anne ve oğul birlikte o koca kediyi öldürdüler, böylece bir dağ dolusu taze et kazandılar.",
                "notes": "slaughter: öldürmek, telef etmek; fresh meat: taze et"
            },
            {
                "id": 80,
                "text": "Though torn and bleeding, the gray cub had proved his courage and inherited the killer's pride.",
                "translation": "Yaralanmış ve kanlar içinde kalmış olsa da boz yavru cesaretini kanıtlamış ve avcının gururunu devralmıştı.",
                "notes": "inherited pride: devralınan gurur; killer: avcı, öldüren"
            }
        ]
    },

    # Page 5 (Sentences 81-100)
    {
        "page_no": 5,
        "title": "The Makers of Fire at the Indian Camp",
        "tr_title": "Kızılderili Kampındaki Ateş Sahipleri",
        "vocab_focus": [
            ("tepee", "kızılderili çadırı"),
            ("gods", "tanrılar (insanlar)"),
            ("fire", "ateş"),
            ("smoke", "duman"),
            ("master", "efendi, sahip"),
            ("subjection", "boyun eğme, tabi olma"),
            ("tame", "evcil"),
            ("Indian", "Kızılderili, yerli")
        ],
        "sentences": [
            {
                "id": 81,
                "text": "One warm summer morning, the cub strolled down to the stream to drink cool water.",
                "translation": "Ilık bir yaz sabahı yavru, serin su içmek için dereye doğru yürüdü.",
                "notes": "stroll down: aşağı yürümek; cool water: serin su"
            },
            {
                "id": 82,
                "text": "He stepped through a clump of willows and froze: sitting on logs were five human beings.",
                "translation": "Bir söğüt kümesinin arasından geçti ve donakaldı: kütüklerin üzerinde oturan beş insanoğlu vardı.",
                "notes": "clump of willows: söğüt kümesi; freeze: donakalmak"
            },
            {
                "id": 83,
                "text": "He had never seen a man before; they did not run away like prey, nor crouch like predators.",
                "translation": "Daha önce hiç insan görmemişti; ne av gibi kaçıyorlar ne de yırtıcılar gibi pusuya yatıyorlardı.",
                "notes": "run away: kaçmak; crouch: çömelmek, pusuya yatmak"
            },
            {
                "id": 84,
                "text": "They sat upright in calm majesty, clothed in soft tanned deer skins.",
                "translation": "Tabaklanmış yumuşak geyik derilerine bürünmüş, sakin bir azametle dimdik oturuyorlardı.",
                "notes": "tanned skins: tabaklanmış deriler; calm majesty: sakin azamet"
            },
            {
                "id": 85,
                "text": "An instinctive feeling of awe and weakness surged through the little cub's heart.",
                "translation": "Küçük yavrunun kalbine içgüdüsel bir hayranlık ve acizlik duygusu doldu.",
                "notes": "instinctive feeling: içgüdüsel duygu; awe: hayranlık ve ürperti"
            },
            {
                "id": 86,
                "text": "One Indian rose, walked toward him, and reached out a large dark hand to seize him.",
                "translation": "Kızılderililerden biri ayağa kalktı, ona doğru yürüdü ve onu yakalamak için iri esmer elini uzattı.",
                "notes": "reach out hand: elini uzatmak; seize: yakalamak"
            },
            {
                "id": 87,
                "text": "The cub's fur bristled, his ears flattened, and his sharp milk teeth sank into the man's hand.",
                "translation": "Yavrunun tüyleri kabardı, kulakları arkaya yattı ve sivri süt dişleri adamın eline geçti.",
                "notes": "fur bristled: tüyleri kabardı; milk teeth: süt dişleri"
            },
            {
                "id": 88,
                "text": "The man shouted in anger and struck the cub a stinging blow on the side of his head.",
                "translation": "Adam öfkeyle bağırdı ve yavrunun kafasının yan tarafına can yakan sert bir tokat indirdi.",
                "notes": "stinging blow: can yakan darbe; struck: vurdu"
            },
            {
                "id": 89,
                "text": "The cub was hurled onto his back, whimpering in pain and humiliation.",
                "translation": "Yavru sırtüstü savruldu, acı ve aşağılanma içinde viyakladı.",
                "notes": "hurled: savrulmuş; humiliation: aşağılanma"
            },
            {
                "id": 90,
                "text": "He gave a loud cry for help, and through the bushes crashed the enraged she-wolf!",
                "translation": "Yüksek sesle yardım çığlığı attı ve çalılıkları yararak öfkeden kuduran dişi kurt çıkageldi!",
                "notes": "loud cry: yüksek sesli çığlık; crash through: yararak çıkagelmek"
            },
            {
                "id": 91,
                "text": "She leaped between her cub and the men, baring her deadly fangs with ferocious snarls.",
                "translation": "Yavrusuyla adamların arasına sıçradı, ölümcül sivri dişlerini vahşi hırlamalarla gösterdi.",
                "notes": "bare fangs: dişlerini göstermek; ferocious snarls: vahşi hırlamalar"
            },
            {
                "id": 92,
                "text": "Suddenly, the foremost Indian named Gray Beaver looked closely at her and called: \"Kiche!\"",
                "translation": "Birdenbire Gri Kunduz adındaki öndeki Kızılderili kadına dikkatle baktı ve seslendi: \"Kiche!\"",
                "notes": "foremost: en öndeki; Gray Beaver: Gri Kunduz (Kızılderili adı)"
            },
            {
                "id": 93,
                "text": "To the cub's utter bewilderment, the fierce she-wolf dropped her tail and lowered her ears.",
                "translation": "Yavrunun tam bir şaşkınlığı karşısında, o azılı dişi kurt kuyruğunu indirdi ve kulaklarını kıstı.",
                "notes": "utter bewilderment: tam bir şaşkınlık; drop tail: kuyruğunu indirmek"
            },
            {
                "id": 94,
                "text": "She whimpered submissively, belly to the ground, crawling toward the Indian man like a dog.",
                "translation": "Uysallıkla sızlandı, karnı yere yapışık halde tıpkı bir köpek gibi Kızılderili adama doğru süründü.",
                "notes": "submissively: boyun eğerek; crawl like a dog: köpek gibi sürünmek"
            },
            {
                "id": 95,
                "text": "\"Kiche! Kiche!\" the other men laughed. \"It is Kiche, the dog that ran away into the woods during the famine!\"",
                "translation": "\"Kiche! Kiche!\" diye güldü diğer adamlar. \"Kıtlık zamanında ormana kaçan köpek Kiche bu!\"",
                "notes": "ran away: kaçtı; during famine: kıtlık sırasında"
            },
            {
                "id": 96,
                "text": "She was half wolf and half dog, born in an Indian village and raised among domestic sleds.",
                "translation": "Yarı kurt yarı köpekti; bir Kızılderili köyünde doğmuş ve evcil kızakların arasında büyümüştü.",
                "notes": "half wolf half dog: yarı kurt yarı köpek; domestic: evcil"
            },
            {
                "id": 97,
                "text": "Gray Beaver reached down and stroked her head, claiming her and her cub as his lawful property.",
                "translation": "Gri Kunduz aşağı uzanıp başını okşadı; onu ve yavrusunu yasal mülkü olarak sahiplendi.",
                "notes": "stroke head: başını okşamak; lawful property: yasal mülk"
            },
            {
                "id": 98,
                "text": "The cub saw that men were masters: gods who ruled all beasts and controlled living fire.",
                "translation": "Yavru, insanların birer efendi olduğunu gördü: tüm hayvanlara hükmeden ve canlı ateşi kontrol eden tanrılardı onlar.",
                "notes": "masters: efendiler; rule beasts: hayvanlara hükmetmek"
            },
            {
                "id": 99,
                "text": "They walked back to the Indian village, where dozens of tepees were pitched along the riverbank.",
                "translation": "Nehir kıyısı boyunca düzinelerce konik çadırın kurulduğu Kızılderili köyüne doğru yürüdüler.",
                "notes": "tepees pitched: kurulmuş çadırlar; riverbank: nehir kıyısı"
            },
            {
                "id": 100,
                "text": "The wild free life of the woods was gone; the cub was now bound to the dominion of man.",
                "translation": "Ormanın vahşi ve özgür hayatı artık geride kalmıştı; yavru artık insanın egemenliğine bağlanmıştı.",
                "notes": "dominion of man: insanın egemenliği; bound to: ...e bağlanmış"
            }
        ]
    },

    # Page 6 (Sentences 101-120)
    {
        "page_no": 6,
        "title": "The Name White Fang and Gray Beaver",
        "tr_title": "Beyaz Diş İsmi ve Gri Kunduz",
        "vocab_focus": [
            ("fangs", "sivri köpek dişleri"),
            ("puppy", "köpek yavrusu"),
            ("hearth", "ocak, ateş başı"),
            ("leather", "deri, kösele"),
            ("thong", "deri kayış"),
            ("flesh", "et"),
            ("gods", "tanrılar (insanlar)"),
            ("master", "sahip, efendi")
        ],
        "sentences": [
            {
                "id": 101,
                "text": "Gray Beaver examined the cub's teeth and noticed his remarkably white, sharp fangs.",
                "translation": "Gri Kunduz yavrunun dişlerini muayene etti ve son derece beyaz, sivri köpek dişlerini fark etti.",
                "notes": "examine: muayene etmek; sharp fangs: sivri dişler"
            },
            {
                "id": 102,
                "text": "\"His fangs are white as the northern snow,\" the Indian said, \"his name shall be White Fang!\"",
                "translation": "\"Dişleri kuzeyin karları kadar beyaz,\" dedi Kızılderili, \"onun adı Beyaz Diş olsun!\"",
                "notes": "white as snow: kar gibi beyaz; White Fang: Beyaz Diş"
            },
            {
                "id": 103,
                "text": "White Fang learned that the camp was a noisy, bustling community of two-legged gods.",
                "translation": "Beyaz Diş, kampın iki bacaklı tanrılardan oluşan gürültülü, hareketli bir topluluk olduğunu öğrendi.",
                "notes": "bustling community: hareketli topluluk; two-legged gods: iki bacaklı tanrılar"
            },
            {
                "id": 104,
                "text": "They chopped wood with axes, threw blazing sticks of fire, and commanded dogs with whistles.",
                "translation": "Baltalarla odun kesiyor, alevli ateş çubukları fırlatıyor ve ıslıklarla köpeklere emir veriyorlardı.",
                "notes": "chop wood: odun kesmek; command with whistles: ıslıkla emretmek"
            },
            {
                "id": 105,
                "text": "Their power was absolute: a single man could kill an animal from a distance with lightning and thunder.",
                "translation": "Güçleri mutlaktı: tek bir adam şimşek ve gök gürültüsüyle uzaktan bir hayvanı öldürebilirdi.",
                "notes": "lightning and thunder: şimşek ve gök gürültüsü (tüfek patlaması); absolute power: mutlak güç"
            },
            {
                "id": 106,
                "text": "White Fang crept toward a fire in curiosity, sniffing at the dancing red flames.",
                "translation": "Beyaz Diş merakla bir ateşe doğru sokuldu, dans eden kızıl alevleri kokladı.",
                "notes": "sniff at: koklamak; dancing flames: dans eden alevler"
            },
            {
                "id": 107,
                "text": "He touched the hot embers with his tender snout, burning his nose and tongue with blistering agony.",
                "translation": "Narin burnunu sıcak közlere dokundurdu; kavurucu bir ıstırapla burnunu ve dilini yaktı.",
                "notes": "hot embers: sıcak közler; tender snout: narin burun"
            },
            {
                "id": 108,
                "text": "He leaped backward yelping, rolling in the grass while all the Indians laughed loudly at his folly.",
                "translation": "Acı içinde ciyaklayarak geriye sıçradı; tüm Kızılderililer onun bu ahmaklığına kahkahalarla gülerken çimenlerde yuvarlandı.",
                "notes": "yelp: acıyla ciyaklamak; laugh at folly: ahmaklığına gülmek"
            },
            {
                "id": 109,
                "text": "He retreated to his mother Kiche, feeling humiliated by the scornful laughter of the gods.",
                "translation": "Tanrıların alaycı kahkahaları yüzünden aşağılanmış hissederek annesi Kiche'nin yanına sığındı.",
                "notes": "scornful laughter: alaycı kahkaha; retreat: geri çekilmek, sığınmak"
            },
            {
                "id": 110,
                "text": "He never approached fire again, understanding that some powers were too dangerous to touch.",
                "translation": "Bazı güçlerin dokunulamayacak kadar tehlikeli olduğunu anlayarak bir daha asla ateşe yaklaşmadı.",
                "notes": "too dangerous: çok tehlikeli; approach: yaklaşmak"
            },
            {
                "id": 111,
                "text": "Gray Beaver tied Kiche with a strong thong of braided moose hide to a wooden stake.",
                "translation": "Gri Kunduz, Kiche'yi örgü sığın derisinden güçlü bir kayışla tahta bir kazığa bağladı.",
                "notes": "braided hide: örgülü deri; wooden stake: tahta kazık"
            },
            {
                "id": 112,
                "text": "White Fang was allowed to roam free, but he stayed close to his captive mother.",
                "translation": "Beyaz Diş'in serbestçe dolaşmasına izin verildi fakat o esir annesinin yanından ayrılmadı.",
                "notes": "roam free: serbestçe dolaşmak; captive mother: esir anne"
            },
            {
                "id": 113,
                "text": "Gray Beaver tossed him a strip of fresh fish, defending the cub when other puppies tried to steal it.",
                "translation": "Gri Kunduz ona bir parça taze balık attı, diğer köpek yavruları onu çalmaya çalıştığında yavruyu savundu.",
                "notes": "strip of fish: balık parçası; defend: savunmak"
            },
            {
                "id": 114,
                "text": "White Fang recognized Gray Beaver as his special god: stern, just, and the distributor of meat.",
                "translation": "Beyaz Diş Gri Kunduz'u kendi özel tanrısı olarak tanıdı: sert, adil ve etin dağıtıcısı.",
                "notes": "distributor of meat: et dağıtıcısı; stern and just: sert ve adil"
            },
            {
                "id": 115,
                "text": "The cub owed him allegiance, and in return received food, protection, and fire.",
                "translation": "Yavru ona sadakat borçluydu, karşılığında ise yiyecek, koruma ve ateş alıyordu.",
                "notes": "owe allegiance: sadakat borçlu olmak; protection: koruma"
            },
            {
                "id": 116,
                "text": "He began to forget the wild caves and the free hunt of the silent forest.",
                "translation": "Vahşi mağaraları ve sessiz ormanın özgür avını yavaş yavaş unutmaya başladı.",
                "notes": "forget: unutmak; free hunt: özgür av"
            },
            {
                "id": 117,
                "text": "The camp was his new territory, surrounded by the invisible fence of human will.",
                "translation": "Kamp onun yeni sahasıydı, insan iradesinin görünmez çitiyle çevrelenmişti.",
                "notes": "new territory: yeni saha / bölge; human will: insan iradesi"
            },
            {
                "id": 118,
                "text": "Yet his wild wolf blood remained pure, making him proud, fierce, and alert.",
                "translation": "Yine de vahşi kurt kanı saf kaldı; onu gururlu, hırçın ve daima tetikte kıldı.",
                "notes": "wolf blood: kurt kanı; alert: tetikte"
            },
            {
                "id": 119,
                "text": "He did not bark like a dog; he snarled, growled, or suffered in deep wolf silence.",
                "translation": "Bir köpek gibi havlamazdı; hırlar, homurdanır ya da kurtlara özgü derin bir sessizlik içinde acı çekerdi.",
                "notes": "bark: havlamak; growl: homurdanmak; silence: sessizlik"
            },
            {
                "id": 120,
                "text": "He was growing fast, with heavy bone, dense fur, and muscles like coiled steel wire.",
                "translation": "İri kemikleri, sık kürkü ve gerilmiş çelik tel gibi kaslarıyla hızla büyüyordu.",
                "notes": "dense fur: sık kürk; coiled steel wire: gerilmiş çelik tel"
            }
        ]
    },

    # Page 7 (Sentences 121-140)
    {
        "page_no": 7,
        "title": "The Persecution by Lip-lip and the Dogs",
        "tr_title": "Lip-lip ve Köpeklerin Düşmanlığı",
        "vocab_focus": [
            ("bully", "zorba, kabadayı"),
            ("puppy", "köpek yavrusu"),
            ("persecution", "eziyet, zulüm"),
            ("pack", "sürü, çete"),
            ("outcast", "dışlanmış, sürgün"),
            ("solitary", "yalnız, tek başına"),
            ("stealth", "gizlilik, kurnazlık"),
            ("slash", "kesip yırtmak (dişle)")
        ],
        "sentences": [
            {
                "id": 121,
                "text": "Life in the Indian camp was not peaceful for the solitary wolf cub.",
                "translation": "Kızılderili kampındaki hayat, yapayalnız kurt yavrusu için hiç de huzurlu değildi.",
                "notes": "solitary cub: yalnız yavru; peaceful: huzurlu"
            },
            {
                "id": 122,
                "text": "An older, heavier puppy named Lip-lip immediately made White Fang his sworn enemy.",
                "translation": "Lip-lip adında kendisinden daha büyük ve iri bir köpek yavrusu, Beyaz Diş'i derhal can düşmanı belledi.",
                "notes": "sworn enemy: can düşmanı; heavier puppy: daha iri enik"
            },
            {
                "id": 123,
                "text": "Because White Fang smelled of the wild wolf, all the village dogs despised him.",
                "translation": "Beyaz Diş vahşi kurt koktuğu için bütün köy köpekleri ondan nefret ediyordu.",
                "notes": "smell of wolf: kurt kokmak; despise: nefret etmek, hor görmek"
            },
            {
                "id": 124,
                "text": "Lip-lip organized the puppies into a merciless pack that hunted White Fang relentlessly.",
                "translation": "Lip-lip diğer enikleri, Beyaz Diş'i amansızca kovalayan acımasız bir sürü halinde örgütledi.",
                "notes": "merciless pack: acımasız sürü; relentlessly: amansızca"
            },
            {
                "id": 125,
                "text": "Whenever White Fang stepped away from his mother's stake, the pack attacked him in a swarm.",
                "translation": "Beyaz Diş annesinin bağlı olduğu kazıktan her uzaklaştığında, sürü bir arı sürüsü gibi üzerine saldırdı.",
                "notes": "in a swarm: sürü halinde, üşüşerek; stake: kazık"
            },
            {
                "id": 126,
                "text": "He was forced to flee for his life, running back to Kiche with bleeding ears and flank.",
                "translation": "Canını kurtarmak için kaçmak zorunda kaldı; kulakları ve böğrü kanlar içinde Kiche'nin yanına koştu.",
                "notes": "flee for life: canını kurtarmak için kaçmak; bleeding flank: kanayan böğür"
            },
            {
                "id": 127,
                "text": "Then a terrible day arrived: Gray Beaver sold Kiche to another Indian to pay an old debt.",
                "translation": "Derken korkunç bir gün geldi: Gri Kunduz eski bir borcunu ödemek için Kiche'yi başka bir Kızılderiliye sattı.",
                "notes": "old debt: eski borç; sell: satmak"
            },
            {
                "id": 128,
                "text": "White Fang watched in despair as his mother was loaded onto a large canoe and paddled down the river.",
                "translation": "Beyaz Diş, annesinin büyük bir kanoya bindirilip nehir aşağı kürekle götürülüşünü çaresizlik içinde izledi.",
                "notes": "canoe: kano; in despair: çaresizlik içinde"
            },
            {
                "id": 129,
                "text": "He jumped into the water and swam desperately after the boat, crying for his mother.",
                "translation": "Suya atladı ve annesi için ağlayarak çaresizce teknenin arkasından yüzdü.",
                "notes": "swim desperately: çaresizce yüzmek; jump into water: suya atlamak"
            },
            {
                "id": 130,
                "text": "Gray Beaver intercepted him in another canoe, dragged him out, and gave him a severe beating with a paddle.",
                "translation": "Gri Kunduz başka bir kanoyla önünü kesti, onu sudan çekip çıkardı ve kürekle ona fena bir dayak attı.",
                "notes": "intercept: önünü kesmek; severe beating: fena dayak"
            },
            {
                "id": 131,
                "text": "White Fang learned that the god's command was law: he must never disobey.",
                "translation": "Beyaz Diş tanrının emrinin kanun olduğunu öğrendi: asla itaatsizlik etmemeliydi.",
                "notes": "disobey: itaatsizlik etmek; command was law: emir kanundur"
            },
            {
                "id": 132,
                "text": "Deprived of his mother's protection, the young wolf cub was completely at the mercy of the dog pack.",
                "translation": "Annesinin korumasından mahrum kalan genç kurt yavrusu, tamamen köpek sürüsünün insafına kaldı.",
                "notes": "deprived of protection: korumadan mahrum; at the mercy: insafına kalmış"
            },
            {
                "id": 133,
                "text": "Lip-lip made his daily life a living nightmare of constant skirmishes and ambushes.",
                "translation": "Lip-lip onun günlük hayatını aralıksız çatışmalar ve pusulardan oluşan bir kabusa çevirdi.",
                "notes": "living nightmare: kabus dolu hayat; skirmish: çatışma, dalaşma"
            },
            {
                "id": 134,
                "text": "Persecution hardened White Fang, turning him into a solitary, cunning warrior.",
                "translation": "Gördüğü bu eziyet Beyaz Diş'i sertleştirdi, onu yapayalnız ve kurnaz bir savaşçıya dönüştürdü.",
                "notes": "persecution: eziyet, zulüm; cunning warrior: kurnaz savaşçı"
            },
            {
                "id": 135,
                "text": "He developed astonishing swiftness: he never gave warning, never barked, but struck like lightning.",
                "translation": "Şaşırtıcı bir çabukluk geliştirdi: asla uyarı vermez, asla havlamaz, yıldırım gibi saldırırdı.",
                "notes": "strike like lightning: yıldırım gibi çarpmak; swiftness: çabukluk"
            },
            {
                "id": 136,
                "text": "His tactic was to slash with his fangs and leap clear before the opponent could retaliate.",
                "translation": "Taktiği, sivri dişleriyle kesip yırtmak ve rakibi karşılık veremeden geriye sıçramaktı.",
                "notes": "slash: kesip yırtmak; retaliate: karşılık vermek, misilleme yapmak"
            },
            {
                "id": 137,
                "text": "Whenever he caught an enemy puppy alone in the woods, he attacked and shredded it without mercy.",
                "translation": "Ormanda düşman bir eniği tek başına yakaladığı her seferde, merhametsizce saldırır ve onu parçalardı.",
                "notes": "without mercy: merhametsizce; shred: paramparça etmek"
            },
            {
                "id": 138,
                "text": "The camp dogs learned to fear him when separated, hunting him only in united bands.",
                "translation": "Kamp köpekleri ayrı düştüklerinde ondan korkmayı öğrendiler, onun peşine ancak birleşmiş çeteler halinde düştüler.",
                "notes": "united bands: birleşmiş çeteler; separated: ayrı düşmüş"
            },
            {
                "id": 139,
                "text": "He became an Ishmael among dogs, his hand against everyone and everyone's hand against him.",
                "translation": "Köpekler arasında dışlanmış bir sürgün oldu; kendi eli herkese karşıydı, herkesin eli de kendisine.",
                "notes": "Ishmael: dışlanmış sürgün / toplum dışı kişi (edebi tabir)"
            },
            {
                "id": 140,
                "text": "He was dangerous, deadly, and brooding with cold, merciless ferocity.",
                "translation": "Tehlikeliydi, ölümcüldü ve soğuk, merhametsiz bir yırtıcılıkla yanıp tutuşuyordu.",
                "notes": "merciless ferocity: merhametsiz yırtıcılık; brooding: düşünceli, kinle dolu"
            }
        ]
    },

    # Page 8 (Sentences 141-160)
    {
        "page_no": 8,
        "title": "The Great Famine and Life in the Forest",
        "tr_title": "Büyük Kıtlık ve Ormandaki Yalnızlık",
        "vocab_focus": [
            ("famine", "büyük kıtlık"),
            ("leather", "deri"),
            ("moccasin", "mokasen (kızılderili ayakkabısı)"),
            ("lynx", "vaşak"),
            ("solitude", "yalnızlık"),
            ("starvation", "açlıktan ölme"),
            ("wilderness", "vahşi doğa"),
            ("allegiance", "sadakat, bağlılık")
        ],
        "sentences": [
            {
                "id": 141,
                "text": "In the third autumn of White Fang's life, a terrible winter famine settled over the Mackenzie valley.",
                "translation": "Beyaz Diş'in hayatının üçüncü sonbaharında, Mackenzie vadisine korkunç bir kış kıtlığı çöktü.",
                "notes": "winter famine: kış kıtlığı; valley: vadi"
            },
            {
                "id": 142,
                "text": "The moose did not migrate, the caribou failed to appear, and fish froze deep beneath thick ice.",
                "translation": "Sığınlar göç etmedi, rengeyikleri ortalıkta görünmedi ve balıklar kalın buzun derinliklerinde dondu.",
                "notes": "migrate: göç etmek; thick ice: kalın buz"
            },
            {
                "id": 143,
                "text": "The Indians were reduced to boiling old leather moccasins and gnawing birch bark to survive.",
                "translation": "Kızılderililer hayatta kalabilmek için eski deri mokasenleri kaynatmaya ve huş kabuklarını kemirmeye mecbur kaldı.",
                "notes": "gnaw: kemirmek; boiled moccasins: kaynatılmış mokasenler"
            },
            {
                "id": 144,
                "text": "The starving sled dogs turned into skeletons, and the weaker animals were slaughtered for human food.",
                "translation": "Açlıktan kırılan kızak köpekleri birer iskelete döndü ve daha zayıf olan hayvanlar insan gıdası için kesildi.",
                "notes": "turned into skeletons: iskelete dönmek; slaughtered: kesildi"
            },
            {
                "id": 145,
                "text": "White Fang was wise enough to know that his gods would eat him if he lingered in the camp.",
                "translation": "Beyaz Diş kampta oyalanırsa tanrılarının kendisini de yiyeceğini bilecek kadar akıllıydı.",
                "notes": "linger: oyalanmak; wise enough: yeterince akıllı"
            },
            {
                "id": 146,
                "text": "He slipped away into the frozen forest, returning to the wild solitude of his wolf ancestors.",
                "translation": "Donmuş ormanın içine süzüldü, kurt atalarının vahşi yalnızlığına geri döndü.",
                "notes": "wolf ancestors: kurt atalar; wild solitude: vahşi yalnızlık"
            },
            {
                "id": 147,
                "text": "It was a grim battle against starvation: the temperature fell to seventy degrees below zero.",
                "translation": "Açlığa karşı amansız bir mücadeleydi: sıcaklık sıfırın altında yetmiş dereceye kadar düştü.",
                "notes": "grim battle: amansız savaş; starvation: açlıktan ölme"
            },
            {
                "id": 148,
                "text": "He hunted field mice beneath deep snowdrifts, digging them out with frantic paws.",
                "translation": "Derin kar yığınlarının altındaki tarla farelerini avladı, onları hummalı patileriyle kazıp çıkardı.",
                "notes": "snowdrifts: kar yığınları; frantic paws: hummalı patiler"
            },
            {
                "id": 149,
                "text": "He stalked a starving young wolf and killed him, eating the flesh of his own kind to stay alive.",
                "translation": "Açlıktan bitkin genç bir kurdu sinsice izleyip öldürdü; hayatta kalabilmek için kendi türünün etini yedi.",
                "notes": "stalk: sinsice izlemek; own kind: kendi türü"
            },
            {
                "id": 150,
                "text": "In a narrow ravine, he crossed paths with an old mother lynx that was weak with famine.",
                "translation": "Dar bir vadide, kıtlıktan bitkin düşmüş yaşlı bir anne vaşakla karşılaştı.",
                "notes": "narrow ravine: dar vadi; weak with famine: kıtlıktan bitkin"
            },
            {
                "id": 151,
                "text": "They fought a ferocious duel in the snow until White Fang clamped his jaws onto her throat.",
                "translation": "Karların içinde vahşi bir düello yaptılar, ta ki Beyaz Diş çenesini hayvanın boğazına kenetleyene kadar.",
                "notes": "ferocious duel: vahşi düello; clamp jaws: çeneyi kenetlemek"
            },
            {
                "id": 152,
                "text": "The lynx's meat sustained him for two whole weeks, giving him renewed strength and endurance.",
                "translation": "Vaşağın eti ona tam iki hafta boyunca yetti, ona tazelenmiş bir güç ve dayanıklılık kazandırdı.",
                "notes": "sustain: beslemek, hayatta tutmak; endurance: dayanıklılık"
            },
            {
                "id": 153,
                "text": "As the warm chinook wind arrived in early spring, the rivers thawed and game returned.",
                "translation": "İlkbahar başında ılık çinuk rüzgarı gelince nehirler çözüldü ve av hayvanları geri döndü.",
                "notes": "chinook wind: ılık dağ rüzgarı; river thawed: nehir çözüldü"
            },
            {
                "id": 154,
                "text": "White Fang could have remained forever in the forest as a free wolf, wild and untamed.",
                "translation": "Beyaz Diş vahşi ve evcilleştirilmemiş özgür bir kurt olarak sonsuza dek ormanda kalabilirdi.",
                "notes": "wild and untamed: vahşi ve evcilleşmemiş; remain forever: sonsuza dek kalmak"
            },
            {
                "id": 155,
                "text": "Yet deep within his soul lived an overpowering yearning for the gods and their warm campfires.",
                "translation": "Yine de ruhunun derinliklerinde tanrılara ve onların sıcak kamp ateşlerine karşı karşı konulmaz bir özlem yaşıyordu.",
                "notes": "overpowering yearning: karşı konulmaz özlem; campfire: kamp ateşi"
            },
            {
                "id": 156,
                "text": "He followed the riverbank back toward the site of Gray Beaver's village.",
                "translation": "Gri Kunduz'un köyünün bulunduğu yere doğru nehir kıyısını takip etti.",
                "notes": "follow riverbank: nehir kıyısını takip etmek"
            },
            {
                "id": 157,
                "text": "Outside the camp, he stumbled upon his old arch-enemy, Lip-lip, who was also returning from the woods.",
                "translation": "Kampın dışında, kendisi gibi ormandan dönmekte olan eski can düşmanı Lip-lip'e rastladı.",
                "notes": "arch-enemy: can düşmanı; stumble upon: rastlamak"
            },
            {
                "id": 158,
                "text": "There was no pack to help the bully now; White Fang rushed in like a thunderbolt.",
                "translation": "Artık o zorbaya yardım edecek hiçbir sürü yoktu; Beyaz Diş bir yıldırım gibi üzerine atıldı.",
                "notes": "bully: kabadayı, zorba; rush in: üzerine atılmak"
            },
            {
                "id": 159,
                "text": "With three lightning slashes, he broke Lip-lip's forelegs and ripped out his jugular vein.",
                "translation": "Üç şimşek gibi ısırıkla Lip-lip'in ön bacaklarını kırdı ve şah damarını söküp attı.",
                "notes": "lightning slashes: şimşek gibi ısırıklar; jugular vein: şah damarı"
            },
            {
                "id": 160,
                "text": "His ancient enemy was dead; White Fang trotted into the camp and lay submissively at Gray Beaver's feet.",
                "translation": "Eski düşmanı ölmüştü; Beyaz Diş tırıs adımlarla kampa girdi ve uysallıkla Gri Kunduz'un ayaklarının dibine yattı.",
                "notes": "ancient enemy: eski düşman; lay submissively: boyun eğerek yatmak"
            }
        ]
    },

    # Page 9 (Sentences 161-180)
    {
        "page_no": 9,
        "title": "The Covenant with Man and the Sled",
        "tr_title": "İnsanla Ahit ve Kızak Köpekliği",
        "vocab_focus": [
            ("lead-dog", "önder kızak köpeği"),
            ("traces", "koşum kayışları"),
            ("sled", "kızak"),
            ("whip", "kırbaç"),
            ("master", "sahip, efendi"),
            ("team", "kızak takımı"),
            ("discipline", "disiplin"),
            ("covenant", "sözleşme, ahit")
        ],
        "sentences": [
            {
                "id": 161,
                "text": "Gray Beaver did not strike him; instead, he tossed him a great chunk of dried moose meat.",
                "translation": "Gri Kunduz ona vurmadı; aksine ona koca bir parça kurutulmuş sığın eti fırlattı.",
                "notes": "chunk of meat: et parçası; dried moose: kurutulmuş sığın eti"
            },
            {
                "id": 162,
                "text": "The covenant between man and wolf was renewed: loyalty in exchange for leadership and food.",
                "translation": "İnsanla kurt arasındaki ahit yenilenmişti: liderlik ve yiyecek karşılığında sadakat.",
                "notes": "covenant: ahit, kutsal bağ; loyalty: sadakat"
            },
            {
                "id": 163,
                "text": "That winter, Gray Beaver fitted White Fang into a rawhide harness and attached him to the heavy sled.",
                "translation": "O kış Gri Kunduz, Beyaz Diş'e ham deriden bir koşum takımı taktı ve onu ağır kızağa bağladı.",
                "notes": "rawhide harness: ham deri koşum; attach to sled: kızağa bağlamak"
            },
            {
                "id": 164,
                "text": "Because he was faster and stronger than all the other dogs, he was made the lead-dog of the team.",
                "translation": "Diğer bütün köpeklerden daha hızlı ve güçlü olduğu için takımın önder köpeği yapıldı.",
                "notes": "lead-dog: önder köpek; team: takım"
            },
            {
                "id": 165,
                "text": "His position at the head of the traces provoked the furious jealousy of the entire pack.",
                "translation": "Koşum kayışlarının başındaki konumu, bütün sürünün azgın kıskançlığını körükledi.",
                "notes": "head of traces: koşumların başı; furious jealousy: azgın kıskançlık"
            },
            {
                "id": 166,
                "text": "The other dogs ran behind him in a fan-shaped formation, constantly trying to catch and tear him down.",
                "translation": "Diğer köpekler arkasından yelpaze düzeninde koşuyor, durmadan onu yakalayıp parçalamaya çalışıyorlardı.",
                "notes": "fan-shaped formation: yelpaze düzeni; tear down: parçalamak"
            },
            {
                "id": 167,
                "text": "White Fang had to run at top speed all day long to keep ahead of their snapping jaws.",
                "translation": "Beyaz Diş, onların kapan dişlerinin önünde kalabilmek için bütün gün son sürat koşmak zorundaydı.",
                "notes": "top speed: son sürat; snapping jaws: kapan çeneler"
            },
            {
                "id": 168,
                "text": "This brutal arrangement made him the swiftest, most tireless sled dog in the entire Northland.",
                "translation": "Bu acımasız düzen onu bütün Kuzey diyarının en hızlı, en yorulmak bilmez kızak köpeği yaptı.",
                "notes": "brutal arrangement: acımasız düzen; tireless: yorulmaz"
            },
            {
                "id": 169,
                "text": "Whenever the sled stopped and a dog stepped out of line, White Fang attacked like a whirlwind.",
                "translation": "Kızak her durduğunda ve bir köpek hizayı bozduğunda Beyaz Diş bir kasırga gibi saldırdı.",
                "notes": "step out of line: hizayı bozmak; attack like whirlwind: kasırga gibi saldırmak"
            },
            {
                "id": 170,
                "text": "He enforced iron discipline among the team on behalf of his master Gray Beaver.",
                "translation": "Efendisi Gri Kunduz adına takımın içinde demir bir disiplin uyguladı.",
                "notes": "iron discipline: demir disiplin; on behalf of: ...in adına"
            },
            {
                "id": 171,
                "text": "He showed no mercy, accepted no friendship, and tolerated no defiance from any canine.",
                "translation": "Hiçbir merhamet göstermedi, hiçbir dostluğu kabul etmedi ve hiçbir köpekten en ufak bir itaatsizliğe göz yummadı.",
                "notes": "tolerate defiance: itaatsizliğe göz yummak; canine: köpek"
            },
            {
                "id": 172,
                "text": "The gods admired his savage efficiency and rewarded him with the best scraps of meat.",
                "translation": "Tanrılar onun bu vahşi verimliliğine hayran kaldılar ve onu en güzel et parçalarıyla ödüllendirdiler.",
                "notes": "savage efficiency: vahşi verimlilik; scraps of meat: et parçaları"
            },
            {
                "id": 173,
                "text": "When strange dogs in other villages challenged him, he killed them in seconds with lethal throat slashes.",
                "translation": "Diğer köylerdeki yabancı köpekler ona meydan okuduğunda, ölümcül boğaz ısırıklarıyla onları saniyeler içinde öldürdü.",
                "notes": "challenge: meydan okumak; lethal throat slash: ölümcül boğaz ısırığı"
            },
            {
                "id": 174,
                "text": "He was now fully grown, standing nearly two and a half feet at the shoulder and weighing over eighty pounds.",
                "translation": "Artık tamamen büyümüştü; omuz boyu yaklaşık yetmiş beş santimi buluyor, kırk kilonun üzerinde geliyordu.",
                "notes": "fully grown: tamamen büyümüş; weigh: ağırlığında olmak"
            },
            {
                "id": 175,
                "text": "His wolf coat was thick and silvery gray, shielding him against the bitterest Arctic blizzards.",
                "translation": "Kurt kürkü kalın ve gümüşi griydi; onu en dondurucu Kutup tipilerine karşı koruyordu.",
                "notes": "silvery gray: gümüşi gri; Arctic blizzard: Kutup kar fırtınası"
            },
            {
                "id": 176,
                "text": "His instincts were razor-sharp: he could sense danger hours before it manifested.",
                "translation": "İçgüdüleri jilet gibi keskindi: tehlikeyi ortaya çıkmadan saatler önce sezebilirdi.",
                "notes": "razor-sharp instincts: jilet gibi keskin içgüdüler; sense danger: tehlikeyi sezmek"
            },
            {
                "id": 177,
                "text": "Yet his heart was devoid of love; he knew only duty, obedience, and fierce possessiveness of his master's property.",
                "translation": "Yine de kalbi sevgiden tamamen yoksundu; yalnızca vazifeyi, itaati ve efendisinin mülkünü azgınca sahiplenmeyi bilirdi.",
                "notes": "devoid of love: sevgiden yoksun; possessiveness: sahiplenme"
            },
            {
                "id": 178,
                "text": "He protected Gray Beaver's tepee and goods with ferocious ferocity: no thief dared approach.",
                "translation": "Gri Kunduz'un çadırını ve mallarını vahşi bir hırsla korudu: hiçbir hırsız yaklaşmaya cesaret edemezdi.",
                "notes": "protect goods: malları korumak; dare approach: yaklaşmaya cesaret etmek"
            },
            {
                "id": 179,
                "text": "The Indians respected him as a superior beast, calling him the fierce fighting wolf-dog.",
                "translation": "Kızılderililer ona üstün bir hayvan olarak saygı duydular; ona azılı dövüşçü kurt köpeği adını verdiler.",
                "notes": "superior beast: üstün canavar / hayvan; fighting wolf-dog: dövüşçü kurt köpeği"
            },
            {
                "id": 180,
                "text": "In the summer of 1898, Gray Beaver decided to take his furs and White Fang on a long voyage to Fort Yukon.",
                "translation": "1898 yazında Gri Kunduz, kürklerini ve Beyaz Diş'i yanına alarak Fort Yukon'a uzun bir yolculuğa çıkmaya karar verdi.",
                "notes": "voyage to Fort Yukon: Fort Yukon yolculuğu"
            }
        ]
    },

    # Page 10 (Sentences 181-200)
    {
        "page_no": 10,
        "title": "The Enemy of His Kind at Fort Yukon",
        "tr_title": "Fort Yukon ve Türünün Düşmanı",
        "vocab_focus": [
            ("gold rush", "altına hücum dönemi"),
            ("prospector", "altın arayıcısı"),
            ("steamer", "nehir buharlısı"),
            ("monstrous", "canavarca, korkunç"),
            ("ferocity", "vahşilik, yırtıcılık"),
            ("whiskey", "viski"),
            ("scoundrel", "alçak, rezil herif"),
            ("whiskey bottle", "viski şişesi")
        ],
        "sentences": [
            {
                "id": 181,
                "text": "Fort Yukon was teeming with thousands of gold prospectors on their way to the Klondike gold fields.",
                "translation": "Fort Yukon, Klondike altın sahalarına gitmekte olan binlerce altın arayıcısıyla dolup taşıyordu.",
                "notes": "teeming with: ...ile dolup taşan; gold prospectors: altın arayıcıları"
            },
            {
                "id": 182,
                "text": "Steamers arrived daily from the south, unloading swarms of greedy men and clumsy civil dogs.",
                "translation": "Güneyden her gün nehir buharlıları geliyor; açgözlü adam sürülerini ve beceriksiz şehir köpeklerini boşaltıyordu.",
                "notes": "clumsy civil dogs: beceriksiz şehir köpekleri; greedy men: açgözlü adamlar"
            },
            {
                "id": 183,
                "text": "Gray Beaver sold his bales of fine furs for bags of golden dust and silver coins.",
                "translation": "Gri Kunduz kaliteli kürk balyalarını torbalar dolusu altın tozu ve gümüş sikkeler karşılığında sattı.",
                "notes": "bales of furs: kürk balyaları; golden dust: altın tozu"
            },
            {
                "id": 184,
                "text": "White Fang despised the white men's dogs: soft, overfed mastiffs, hounds, and pointers.",
                "translation": "Beyaz Diş beyaz adamların köpeklerinden nefret ediyordu: yumuşak, aşırı beslenmiş mastifler, tazılar ve av köpekleri.",
                "notes": "overfed mastiffs: fazla beslenmiş mastif köpekleri; despise: nefret etmek"
            },
            {
                "id": 185,
                "text": "Whenever a domestic dog stepped off the boat, White Fang lured it into an alley and destroyed it.",
                "translation": "Evcil bir köpek tekneden her indiğinde, Beyaz Diş onu bir ara sokağa çeker ve saniyeler içinde yok ederdi.",
                "notes": "lure into alley: ara sokağa çekmek; destroy: yok etmek"
            },
            {
                "id": 186,
                "text": "His ferocity became legendary among the rough miners, who called him the 'Fighting Wolf'.",
                "translation": "Vahşiliği, kendisine 'Dövüşçü Kurt' adını takan sert madenciler arasında efsane haline geldi.",
                "notes": "Fighting Wolf: Dövüşçü Kurt; rough miners: sert madenciler"
            },
            {
                "id": 187,
                "text": "Among the crowd of spectators was a cowardly, hideous man named Beauty Smith.",
                "translation": "Seyirciler kalabalığının arasında Beauty Smith adında korkak, iğrenç görünümlü bir adam vardı.",
                "notes": "hideous man: iğrenç / çirkin adam; Beauty Smith: Güzel Smith (alaycı lakap)"
            },
            {
                "id": 188,
                "text": "He was called 'Beauty' in hideous irony, for he had a misshapen head, pig eyes, and yellow tusks for teeth.",
                "translation": "Ona korkunç bir ironiyle 'Güzel' derlerdi; çünkü biçimsiz bir kafası, domuz gözleri ve diş yerine sarı azı dişleri vardı.",
                "notes": "hideous irony: korkunç ironi; misshapen head: biçimsiz kafa"
            },
            {
                "id": 189,
                "text": "He was a cook, a thief, and a promoter of illegal dog-fights in the gold rush town.",
                "translation": "Altına hücum kasabasında bir aşçı, bir hırsız ve yasadışı köpek dövüşlerinin organizatörüydü.",
                "notes": "illegal dog-fights: yasadışı köpek dövüşleri; promoter: organizatör"
            },
            {
                "id": 190,
                "text": "He saw White Fang fight and recognized him as an invincible killing machine that could make him rich.",
                "translation": "Beyaz Diş'in dövüştüğünü gördü ve onu kendisini zengin edebilecek yenilmez bir ölüm makinesi olarak tanıdı.",
                "notes": "invincible killing machine: yenilmez ölüm makinesi"
            },
            {
                "id": 191,
                "text": "Beauty Smith approached Gray Beaver and offered bags of gold to buy the wolf-dog.",
                "translation": "Beauty Smith Gri Kunduz'a yaklaştı ve kurt köpeğini satın almak için torbalar dolusu altın teklif etti.",
                "notes": "approach: yaklaşmak; offer gold: altın teklif etmek"
            },
            {
                "id": 192,
                "text": "Gray Beaver refused scornfully: \"White Fang is the finest dog on the Yukon; I will not sell him!\"",
                "translation": "Gri Kunduz küçümseyerek reddetti: \"Beyaz Diş Yukon'daki en mükemmel köpektir; onu asla satmam!\"",
                "notes": "refuse scornfully: hor görerek reddetmek; sell: satmak"
            },
            {
                "id": 193,
                "text": "Beauty Smith knew the Indian's terrible weakness: an uncontrollable thirst for whiskey.",
                "translation": "Beauty Smith Kızılderilinin o korkunç zaafını iyi biliyordu: viskiye karşı önüne geçilmez bir açlık.",
                "notes": "uncontrollable thirst: önüne geçilmez susuzluk / düşkünlük"
            },
            {
                "id": 194,
                "text": "He brought bottles of fiery liquor to Gray Beaver's camp night after night.",
                "translation": "Gece ardına gece Gri Kunduz'un kampına şişeler dolusu ateşli içki taşıdı.",
                "notes": "fiery liquor: yakıcı sert içki; night after night: her gece"
            },
            {
                "id": 195,
                "text": "Within weeks, the Indian drank away all his gold dust, his blankets, and his furs.",
                "translation": "Haftalar içinde Kızılderili bütün altın tozunu, battaniyelerini ve kürklerini içkiye yatırıp bitirdi.",
                "notes": "drink away: içkide tüketmek; within weeks: haftalar içinde"
            },
            {
                "id": 196,
                "text": "Penniless and trembling with delirium, Gray Beaver finally traded White Fang for a few bottles of cheap whiskey.",
                "translation": "Meteliksiz kalan ve hezeyan içinde titreyen Gri Kunduz, sonunda birkaç şişe ucuz viski karşılığında Beyaz Diş'i takas etti.",
                "notes": "trembling with delirium: hezeyanla titreyerek; trade: takas etmek"
            },
            {
                "id": 197,
                "text": "White Fang escaped twice, returning faithfully to his Indian master's side.",
                "translation": "Beyaz Diş iki kez kaçtı, sadakatle Kızılderili efendisinin yanına geri döndü.",
                "notes": "escape twice: iki kez kaçmak; faithfully: sadakatle"
            },
            {
                "id": 198,
                "text": "Each time, Gray Beaver tied him up and handed him back to the hideous white monster.",
                "translation": "Her seferinde Gri Kunduz onu bağladı ve o iğrenç beyaz canavara elleriyle geri teslim etti.",
                "notes": "hand back: geri teslim etmek; tie up: bağlamak"
            },
            {
                "id": 199,
                "text": "On the third day, Gray Beaver boarded a canoe and abandoned Fort Yukon forever without looking back.",
                "translation": "Üçüncü gün Gri Kunduz bir kanoya bindi ve arkasına bile bakmadan Fort Yukon'u sonsuza dek terk etti.",
                "notes": "abandon forever: sonsuza dek terk etmek; without looking back: arkasına bakmadan"
            },
            {
                "id": 200,
                "text": "White Fang was left chained in the clutches of Beauty Smith: the nightmare of madness had begun.",
                "translation": "Beyaz Diş, Beauty Smith'in pençelerinde zincirlenmiş olarak kaldı: delilik kabusu resmen başlamıştı.",
                "notes": "clutches: pençeler; nightmare of madness: delilik kabusu"
            }
        ]
    },

    # Page 11 (Sentences 201-220)
    {
        "page_no": 11,
        "title": "The Mad God Beauty Smith and the Pit",
        "tr_title": "Deli Tanrı Beauty Smith ve Dövüş Çukuru",
        "vocab_focus": [
            ("cage", "kafes"),
            ("pit", "dövüş çukuru, arena"),
            ("madness", "delilik, cinnet"),
            ("torment", "işkence, eziyet"),
            ("mastiff", "mastif cinsi iri köpek"),
            ("lynx", "vaşak"),
            ("spectators", "seyirciler"),
            ("fury", "öfke, gazap")
        ],
        "sentences": [
            {
                "id": 201,
                "text": "Beauty Smith was a coward, and like all cowards, he was unspeakably cruel.",
                "translation": "Beauty Smith bir korkaktı ve tüm korkaklar gibi tarif edilemez derecede zalimdi.",
                "notes": "coward: korkak; unspeakably cruel: tarif edilemez derecede zalim"
            },
            {
                "id": 202,
                "text": "He kept White Fang chained in an iron pen, beating him with heavy sticks to inflame his rage.",
                "translation": "Beyaz Diş'i demir bir kafeste zincirli tutuyor, öfkesini körüklemek için kalın sopalarla onu dövüyordu.",
                "notes": "iron pen: demir kafes / ağıl; inflame rage: öfkesini körüklemek"
            },
            {
                "id": 203,
                "text": "He poked him with burning sticks through the bars and incited spectators to taunt and throw stones at him.",
                "translation": "Parmaklıkların arasından yanan çubuklar batırıyor ve seyircileri onu kışkırtıp taş atmaları için kışkırtıyordu.",
                "notes": "taunt: alay edip kışkırtmak; poke: dürtmek"
            },
            {
                "id": 204,
                "text": "White Fang became a raging fiend: his fur bristled perpetually, and red hatred burned in his wild eyes.",
                "translation": "Beyaz Diş kudurmuş bir iblise dönüştü: tüyleri sürekli kabarıktı ve vahşi gözlerinde kızıl bir nefret yanıyordu.",
                "notes": "raging fiend: kudurmuş iblis; red hatred: kızıl nefret"
            },
            {
                "id": 205,
                "text": "He was known throughout the Yukon territory as 'The Fighting Wolf', the terror of all canines.",
                "translation": "Tüm Yukon bölgesinde bütün köpeklerin korkulu rüyası olan 'Dövüşçü Kurt' olarak tanındı.",
                "notes": "Yukon territory: Yukon bölgesi; terror of canines: köpeklerin korkulu rüyası"
            },
            {
                "id": 206,
                "text": "Beauty Smith charged admission to the dog pit, earning hundreds of dollars on bloody betting matches.",
                "translation": "Beauty Smith dövüş çukuruna giriş ücreti alıyor, kanlı bahis maçlarından yüzlerce dolar kazanıyordu.",
                "notes": "charge admission: giriş ücreti almak; betting match: bahisli maç"
            },
            {
                "id": 207,
                "text": "Large dogs, small dogs, and even two dogs at once were pushed into the pit to fight him.",
                "translation": "İri köpekler, küçük köpekler ve hatta aynı anda iki köpek birden onunla dövüşmesi için çukura itildi.",
                "notes": "dog pit: köpek dövüş çukuru; pushed into: içine itildi"
            },
            {
                "id": 208,
                "text": "White Fang killed them all with clinical precision, slashing jugulars without suffering a scratch.",
                "translation": "Beyaz Diş tek bir çizik bile almadan şah damarlarını keserek hepsini kusursuz bir ustalıkla öldürdü.",
                "notes": "clinical precision: kusursuz / cerrahi ustalık; without a scratch: çizik almadan"
            },
            {
                "id": 209,
                "text": "Once, Beauty Smith captured a wild female lynx and released her into the arena with White Fang.",
                "translation": "Bir defasında Beauty Smith vahşi bir dişi vaşak yakaladı ve onu arenaya Beyaz Diş'in karşısına saldı.",
                "notes": "captured: yakaladı; released into arena: arenaya saldı"
            },
            {
                "id": 210,
                "text": "It was a dreadful battle of claws against fangs, but White Fang emerged drenched in blood, triumphant.",
                "translation": "Pençelerin sivri dişlere karşı korkunç bir savaşıydı fakat Beyaz Diş kana bulanmış halde muzaffer çıktı.",
                "notes": "drenched in blood: kana bulanmış; triumphant: zafer kazanmış"
            },
            {
                "id": 211,
                "text": "Miners refused to bet against him any longer; Beauty Smith could find no more dogs willing to fight.",
                "translation": "Madenciler artık onun aleyhine bahse girmeyi reddetti; Beauty Smith dövüşecek başka hiçbir köpek bulamaz oldu.",
                "notes": "refuse to bet: bahse girmeyi reddetmek; willing to fight: dövüşmeye hevesli"
            },
            {
                "id": 212,
                "text": "In the spring, a steamboat arrived carrying a professional English fighting bulldog named Cherokee.",
                "translation": "İlkbaharda, Cherokee adında profesyonel bir İngiliz dövüş buldogunu taşıyan bir nehir vapuru ulaştı.",
                "notes": "fighting bulldog: dövüş buldogu; steamboat: nehir vapuru"
            },
            {
                "id": 213,
                "text": "Cherokee was short, squat, and weighed fifty pounds of solid, iron muscle with a massive jaw.",
                "translation": "Cherokee kısa boylu, tıknazdı ve koca bir çeneyle elli librelik som, demir gibi bir kastan ibaretti.",
                "notes": "short and squat: kısa ve tıknaz; massive jaw: devasa çene"
            },
            {
                "id": 214,
                "text": "A huge crowd gathered around the pit, wagering thousands of dollars on the unprecedented contest.",
                "translation": "Bu eşi görülmemiş kapışma üzerine binlerce dolar bahse girerek çukurun etrafında dev bir kalabalık toplandı.",
                "notes": "unprecedented contest: eşi görülmemiş mücadele; huge crowd: dev kalabalık"
            },
            {
                "id": 215,
                "text": "The gate opened, and White Fang circled the strange, low-slung beast with flashing fangs.",
                "translation": "Kapı açıldı ve Beyaz Diş parıldayan dişleriyle bu tuhaf, alçak yapılı canavarın etrafında döndü.",
                "notes": "low-slung beast: alçak boylu canavar; flashing fangs: parıldayan dişler"
            },
            {
                "id": 216,
                "text": "Cherokee did not rush; he advanced slowly, wagging his stump of a tail in good nature.",
                "translation": "Cherokee acele etmedi; uysal bir edayla güdük kuyruğunu sallayarak yavaşça ilerledi.",
                "notes": "stump of tail: güdük kuyruk; advance slowly: yavaşça ilerlemek"
            },
            {
                "id": 217,
                "text": "White Fang slashed his shoulder and ripped his ear, but the bulldog refused to be knocked off his feet.",
                "translation": "Beyaz Diş onun omzunu yardı ve kulağını kopardı fakat buldog yere devrilmeyi inatla reddetti.",
                "notes": "rip ear: kulağı koparmak; knocked off feet: yere devrilmek"
            },
            {
                "id": 218,
                "text": "Every time White Fang struck, Cherokee simply closed in closer, aiming for one specific grip.",
                "translation": "Beyaz Diş'in her vuruşunda Cherokee yalnızca daha da sokuldu, tek bir belirli kilitlenmeyi hedefledi.",
                "notes": "close in: yaklaşmak, sokulmak; specific grip: belirli kavrayış / tutuş"
            },
            {
                "id": 219,
                "text": "White Fang tripped over the sawdust and lost his footing for a split second.",
                "translation": "Beyaz Diş talaşlara takıldı ve saniyenin kesrinde dengesini kaybetti.",
                "notes": "sawdust: talaş; lost footing: ayağı kaydı, dengesini kaybetti"
            },
            {
                "id": 220,
                "text": "In that instant, Cherokee's iron jaws clamped onto the loose flesh of White Fang's throat!",
                "translation": "Tam o anda Cherokee'nin demir çenesi Beyaz Diş'in boğazındaki gevşek ete kenetlendi!",
                "notes": "clamp onto: ...e kenetlenmek; throat: boğaz"
            }
        ]
    },

    # Page 12 (Sentences 221-240)
    {
        "page_no": 12,
        "title": "The Bulldog Cherokee and the Rescue",
        "tr_title": "Bulldog Cherokee ve Weedon Scott'ın Kurtarışı",
        "vocab_focus": [
            ("strangle", "boğmak"),
            ("grip", "sıkı kavrayış, tutuş"),
            ("choke", "nefessiz kalmak"),
            ("revolver", "altıpatlar"),
            ("pity", "acıma, merhamet"),
            ("beating", "dayak"),
            ("rescuer", "kurtarıcı"),
            ("jaw", "çene")
        ],
        "sentences": [
            {
                "id": 221,
                "text": "Cherokee's teeth did not let go; his jaws locked like an iron vise upon White Fang's throat.",
                "translation": "Cherokee'nin dişleri asla bırakmadı; çenesi Beyaz Diş'in boğazına demir bir mengene gibi kilitlendi.",
                "notes": "iron vise: demir mengene; lock jaws: çeneleri kilitlemek"
            },
            {
                "id": 222,
                "text": "He began chewing steadily deeper, shifting his bite millimetre by millimetre toward the windpipe.",
                "translation": "Isırığını milim milim nefes borusuna doğru kaydırarak istikrarlı biçimde daha derini çiğnemeye başladı.",
                "notes": "windpipe: soluk borusu; chew deeper: daha derini çiğnemek"
            },
            {
                "id": 223,
                "text": "White Fang thrashed violently, tossing the heavy bulldog into the air, but the grip remained unbroken.",
                "translation": "Beyaz Diş çılgınca debelendi, ağır buldogu havaya fırlattı fakat tutuş hiç bozulmadı.",
                "notes": "thrash violently: çılgınca çırpınmak; unbroken: bozulmamış"
            },
            {
                "id": 224,
                "text": "His breath grew choked, his eyes bulged, and his hind legs weakened beneath him.",
                "translation": "Nefesi tıkandı, gözleri yuvalarından fırladı ve arka bacakları altından kayıp gevşedi.",
                "notes": "eyes bulged: gözleri pörtledi; choked breath: tıkanan nefes"
            },
            {
                "id": 225,
                "text": "For the first time in his life, the invincible fighting wolf was facing certain death.",
                "translation": "Hayatında ilk defa, o yenilmez dövüşçü kurt kesin bir ölümle yüz yüzeydi.",
                "notes": "certain death: kesin ölüm; face: yüzleşmek"
            },
            {
                "id": 226,
                "text": "Beauty Smith leaped into the pit in a fury, kicking White Fang savagely in the ribs with heavy boots.",
                "translation": "Beauty Smith öfkeyle çukura atladı, ağır çizmeleriyle Beyaz Diş'in kaburgalarına vahşice tekmeler savurdu.",
                "notes": "kick savagely: vahşice tekmelemek; heavy boots: ağır çizmeler"
            },
            {
                "id": 227,
                "text": "\"Fight, you coward! Get up and kill him!\" the cruel monster screamed, kicking him again and again.",
                "translation": "\"Dövüş seni korkak! Kalk ve öldür onu!\" diye çığlık attı zalim canavar, onu tekrar tekrar tekmeleyerek.",
                "notes": "cruel monster: zalim canavar; get up: ayağa kalk"
            },
            {
                "id": 228,
                "text": "Suddenly, a tall, clean-shaven young gentleman broke through the crowd of shouting miners.",
                "translation": "Birdenbire uzun boylu, sinekkaydı tıraşlı genç bir beyefendi bağıran madenciler kalabalığını yardı.",
                "notes": "clean-shaven: sinekkaydı tıraşlı; break through: yarıp geçmek"
            },
            {
                "id": 229,
                "text": "It was Weedon Scott, a wealthy mining engineer from California, accompanied by his companion Matt.",
                "translation": "Bu, yanında arkadaşı Matt ile birlikte Kaliforniyalı zengin bir maden mühendisi olan Weedon Scott'tı.",
                "notes": "mining engineer: maden mühendisi; companion: yol arkadaşı"
            },
            {
                "id": 230,
                "text": "\"You cowardly beast!\" Scott roared, striking Beauty Smith a crushing blow that knocked him sprawling in the dirt.",
                "translation": "\"Seni korkak canavar!\" diye gürledi Scott; Beauty Smith'e onu toz toprak içine serecek ezici bir yumruk indirdi.",
                "notes": "crushing blow: ezici darbe; sprawling: boylu boyunca serilmiş"
            },
            {
                "id": 231,
                "text": "Scott and Matt leaped into the pit to pry the locked bulldog off the suffocating wolf.",
                "translation": "Scott ve Matt, kilitlenmiş buldogu boğulmakta olan kurttan ayırmak için çukura atladılar.",
                "notes": "pry off: zorlayarak ayırmak; suffocating: boğulan"
            },
            {
                "id": 232,
                "text": "Matt inserted the steel barrel of his revolver between Cherokee's teeth, using it as a lever.",
                "translation": "Matt tabancasının çelik namlusunu bir kaldıraç gibi kullanarak Cherokee'nin dişlerinin arasına soktu.",
                "notes": "steel barrel: çelik namlu; lever: kaldıraç"
            },
            {
                "id": 233,
                "text": "Slowly, prying with all their strength, they forced the locked jaws apart and pulled Cherokee away.",
                "translation": "Bütün güçleriyle kanırtarak yavaşça o kilitli çeneleri ayırdılar ve Cherokee'yi geri çektiler.",
                "notes": "force jaws apart: çeneleri zorla ayırmak; with all strength: var gücüyle"
            },
            {
                "id": 234,
                "text": "White Fang lay limp upon the sawdust, bleeding profusely and gasping for faint breath.",
                "translation": "Beyaz Diş talaşın üzerinde gevşemiş yatıyordu; oluk oluk kan kaybediyor ve zayıf nefesler alıyordu.",
                "notes": "lay limp: gevşek yatmak; bleed profusely: oluk oluk kanamak"
            },
            {
                "id": 235,
                "text": "Beauty Smith staggered to his feet, whining: \"You can't interfere! That wolf is my property!\"",
                "translation": "Beauty Smith sendeleyerek ayağa kalktı, sızlandı: \"Karışamazsınız! O kurt benim mülküm!\"",
                "notes": "stagger to feet: sendeleyerek kalkmak; interfere: müdahale etmek"
            },
            {
                "id": 236,
                "text": "\"I'm buying him right now for one hundred and fifty dollars,\" Weedon Scott said with icy contempt.",
                "translation": "\"Onu tam şu an yüz elli dolara satın alıyorum,\" dedi Weedon Scott buz gibi bir küçümsemeyle.",
                "notes": "icy contempt: buz gibi küçümseme; buy: satın almak"
            },
            {
                "id": 237,
                "text": "\"If you open your mouth again, I'll beat you until you can't walk!\"",
                "translation": "\"Eğer bir daha ağzını açarsan, seni yürüyemez hale gelene kadar döverim!\"",
                "notes": "beat: dövmek; open mouth: ağzını açmak"
            },
            {
                "id": 238,
                "text": "The miners in the crowd cheered the brave engineer, and cowardly Beauty Smith snatched the money and fled.",
                "translation": "Kalabalıktaki madenciler cesur mühendisi alkışladılar; korkak Beauty Smith ise parayı kapıp kaçtı.",
                "notes": "cheer: alkışlamak; snatch money: parayı kapmak"
            },
            {
                "id": 239,
                "text": "Weedon Scott and Matt gently lifted the dying wolf onto their sled and carried him to their cabin.",
                "translation": "Weedon Scott ve Matt can çekişen kurdu usulca kızaklarına kaldırdılar ve onu kulübelerine taşıdılar.",
                "notes": "dying wolf: can çekişen kurt; cabin: kulübe"
            },
            {
                "id": 240,
                "text": "White Fang had been rescued from the abyss of death by a tall, kind god of a new and gentle kind.",
                "translation": "Beyaz Diş ölümün uçurumundan, yeni ve şefkatli türden uzun boylu, iyi kalpli bir tanrı tarafından kurtarılmıştı.",
                "notes": "abyss of death: ölüm uçurumu; gentle kind: şefkatli tür"
            }
        ]
    },

    # Page 13 (Sentences 241-260)
    {
        "page_no": 13,
        "title": "The Reign of Love and Taming the Wild Heart",
        "tr_title": "Sevginin Hükmü ve Vahşi Kalbin Evcilleşmesi",
        "vocab_focus": [
            ("taming", "evcilleştirme"),
            ("caress", "okşama, şefkat gösterme"),
            ("patience", "sabır"),
            ("meat", "et"),
            ("growl", "hırlama"),
            ("redemption", "kurtuluş, arınma"),
            ("devotion", "bağlılık, fedakarlık"),
            ("love", "sevgi, aşk")
        ],
        "sentences": [
            {
                "id": 241,
                "text": "At first, White Fang was convinced that his new master would beat and torture him like Beauty Smith.",
                "translation": "İlk başta Beyaz Diş, yeni efendisinin de tıpkı Beauty Smith gibi kendisini döveceğine ve eziyet edeceğine inanıyordu.",
                "notes": "convinced: ikna olmuş, emin; torture: işkence etmek"
            },
            {
                "id": 242,
                "text": "He snarled ferociously whenever anyone approached, and bit Matt deeply in the leg when untied.",
                "translation": "Biri yaklaştığında vahşice hırladı ve çözüldüğünde Matt'in bacağını derince ısırdı.",
                "notes": "bite deeply: derince ısırmak; untied: çözülmüş"
            },
            {
                "id": 243,
                "text": "\"He's a thoroughbred wolf, Mr. Scott,\" Matt said, nursing his bandaged leg. \"He cannot be tamed.\"",
                "translation": "\"Bu safkan bir kurt Bay Scott,\" dedi Matt sarılı bacağına pansuman yaparken. \"Asla evcilleştirilemez.\"",
                "notes": "thoroughbred wolf: safkan kurt; tamed: evcilleştirilmiş"
            },
            {
                "id": 244,
                "text": "\"I'll give him a chance,\" Weedon Scott replied calmly. \"He has known only cruelty all his life.\"",
                "translation": "\"Ona bir şans vereceğim,\" diye sakince yanıtladı Weedon Scott. \"Bütün hayatı boyunca yalnızca zulüm gördü.\"",
                "notes": "give a chance: şans vermek; cruelty: zalimlik, zulüm"
            },
            {
                "id": 245,
                "text": "Scott sat patiently outside the cabin every afternoon, speaking to White Fang in soft, soothing tones.",
                "translation": "Scott her öğleden sonra kulübenin dışında sabırla oturdu, Beyaz Diş ile yumuşak, yatıştırıcı tonlarla konuştu.",
                "notes": "sit patiently: sabırla oturmak; soothing tones: yatıştırıcı tonlar"
            },
            {
                "id": 246,
                "text": "He threw him juicy chunks of raw meat from his own hand, refusing to use a club or whip.",
                "translation": "Bir sopa veya kırbaç kullanmayı reddederek kendi eliyle ona sulu çiğ et parçaları attı.",
                "notes": "juicy chunks: sulu parçalar; raw meat: çiğ et"
            },
            {
                "id": 247,
                "text": "White Fang was suspicious of this strange new god who neither shouted, threw stones, nor delivered blows.",
                "translation": "Beyaz Diş ne bağıran, ne taş atan, ne de yumruk indiren bu tuhaf yeni tanrıdan şüpheleniyordu.",
                "notes": "suspicious: şüpheci; deliver blows: darbe indirmek"
            },
            {
                "id": 248,
                "text": "One afternoon, Scott took a piece of meat in his bare hand and held it out directly to the wolf.",
                "translation": "Bir öğleden sonra Scott çıplak eline bir parça et aldı ve onu dosdoğru kurda doğru uzattı.",
                "notes": "bare hand: çıplak el; hold out: uzatmak"
            },
            {
                "id": 249,
                "text": "White Fang crept forward cautiously, every muscle tensed for sudden violence.",
                "translation": "Beyaz Diş ani bir şiddet ihtimaline karşı her kası gerilmiş halde temkinle ileri doğru süründü.",
                "notes": "creep forward cautiously: temkinle öne sürünmek; tensed: gergin"
            },
            {
                "id": 250,
                "text": "He took the meat gently from Scott's fingers, without snapping or scratching.",
                "translation": "Eti kapmadan veya tırmalamadan Scott'ın parmaklarından usulca aldı.",
                "notes": "without snapping: ısırmadan, kapmadan; gently: usulca"
            },
            {
                "id": 251,
                "text": "Then Weedon Scott did something no human had ever attempted: he reached out and touched the wolf's head.",
                "translation": "Ardından Weedon Scott hiçbir insanın daha önce kalkışmadığı bir şey yaptı: elini uzattı ve kurdun başına dokundu.",
                "notes": "attempt: kalkışmak, denemek; reach out: elini uzatmak"
            },
            {
                "id": 252,
                "text": "White Fang snarled instinctively, his fur rising, but the master's hand did not strike.",
                "translation": "Beyaz Diş içgüdüsel olarak hırladı, tüyleri dikeldi fakat efendinin eli hiç vurmadı.",
                "notes": "fur rising: tüyleri dikelerek; instinctively: içgüdüselce"
            },
            {
                "id": 253,
                "text": "The hand rested firmly between his ears, stroking down his neck with deep, rhythmic affection.",
                "translation": "El iki kulağının arasına sağlamca yerleşti; derin, ritmik bir sevgiyle boynunu okşadı.",
                "notes": "rest firmly: sağlamca durmak; rhythmic affection: ritmik sevgi"
            },
            {
                "id": 254,
                "text": "A strange, pleasurable sensation swept through the wild animal's body: it was the caress of love.",
                "translation": "Vahşi hayvanın bedenini tuhaf, haz dolu bir his baştan başa sardı: bu sevginin okşamasıydı.",
                "notes": "caress of love: sevginin okşaması; pleasurable sensation: haz veren his"
            },
            {
                "id": 255,
                "text": "His snarl died away into a contented sigh; his bristling fur smoothed flat against his body.",
                "translation": "Hırlaması huzurlu bir iç çekişe dönüştü; kabaran tüyleri bedenine doğru pürüzsüzce yatıştı.",
                "notes": "contented sigh: huzurlu iç çekiş; smoothed flat: pürüzsüzce yatıştı"
            },
            {
                "id": 256,
                "text": "The wall of hatred that had encased his wild heart for years crumbled into dust.",
                "translation": "Yıllardır o vahşi kalbini çevreleyen nefret duvarı tuzla buz olup toza dönüştü.",
                "notes": "wall of hatred: nefret duvarı; crumble into dust: toza dönüşmek"
            },
            {
                "id": 257,
                "text": "A new and profound emotion blossomed inside him: absolute, worshipping devotion to this love-god.",
                "translation": "İçinde yeni ve derin bir duygu filizlendi: bu sevgi tanrısına karşı mutlak, tapınası bir bağlılık.",
                "notes": "profound emotion: derin duygu; worshipping devotion: taparcasına bağlılık"
            },
            {
                "id": 258,
                "text": "One night, Beauty Smith crept to the cabin with a club and chains to steal White Fang back.",
                "translation": "Bir gece Beauty Smith elinde bir sopa ve zincirlerle Beyaz Diş'i geri çalmak için kulübeye sokuldu.",
                "notes": "creep to cabin: kulübeye sokulmak; steal back: geri çalmak"
            },
            {
                "id": 259,
                "text": "White Fang leaped upon the cowardly tormentor in absolute silence, tearing his arms and throat.",
                "translation": "Beyaz Diş mutlak bir sessizlik içinde o korkak zalimin üzerine atıldı, kollarını ve boğazını paraladı.",
                "notes": "cowardly tormentor: korkak zalim; tear arms: kolları parçalamak"
            },
            {
                "id": 260,
                "text": "Scott pulled the wolf off, and the terrified Beauty Smith fled screaming into the darkness, never to return.",
                "translation": "Scott kurdu üzerinden çekti; dehşet içindeki Beauty Smith çığlıklar atarak bir daha dönmemek üzere karanlığa kaçtı.",
                "notes": "pull off: üzerinden çekmek; fled screaming: çığlıklarla kaçtı"
            }
        ]
    },

    # Page 14 (Sentences 261-280)
    {
        "page_no": 14,
        "title": "The Journey to the Sunland of California",
        "tr_title": "Kaliforniya Güneşine Yolculuk",
        "vocab_focus": [
            ("steamer", "nehir vapuru"),
            ("estate", "çiftlik arazisi, mülk"),
            ("sheep-dog", "çoban köpeği"),
            ("sunland", "güneş diyarı"),
            ("pasture", "otlak, çayır"),
            ("carriage", "fayton, at arabası"),
            ("civilization", "medeniyet"),
            ("guardian", "koruyucu, muhafız")
        ],
        "sentences": [
            {
                "id": 261,
                "text": "When Scott prepared to return home to California, he planned to leave White Fang behind with Matt.",
                "translation": "Scott Kaliforniya'daki evine dönmeye hazırlandığında, Beyaz Diş'i Matt'in yanında geride bırakmayı planladı.",
                "notes": "leave behind: geride bırakmak; plan: planlamak"
            },
            {
                "id": 262,
                "text": "White Fang sensed the departure, refusing to eat and howling mournfully outside the locked cabin.",
                "translation": "Beyaz Diş bu ayrılığı hissetti, yemek yemeyi reddetti ve kilitli kulübenin dışında hazin hazin uludu.",
                "notes": "sense departure: ayrılığı hissetmek; howl mournfully: hazin ulumak"
            },
            {
                "id": 263,
                "text": "As the steamboat blew its whistle at the wharf, White Fang smashed through the cabin window pane.",
                "translation": "Nehir vapuru rıhtımda düdüğünü çalarken Beyaz Diş kulübenin pencere camını kırıp geçti.",
                "notes": "smash through window: pencereyi kırıp geçmek; wharf: rıhtım"
            },
            {
                "id": 264,
                "text": "Bleeding from cuts, he ran at top speed down to the dock and leaped onto the departing deck.",
                "translation": "Kesiklerden kanlar akarak son sürat rıhtıma koştu ve hareket eden güverteye sıçradı.",
                "notes": "top speed: son sürat; departing deck: hareket eden güverte"
            },
            {
                "id": 265,
                "text": "He buried his head against Scott's knees, panting with desperate, overwhelming devotion.",
                "translation": "Çaresiz, taşkın bir bağlılıkla soluyarak başını Scott'ın dizlerine gömdü.",
                "notes": "overwhelming devotion: taşkın bağlılık; bury head: başını gömmek"
            },
            {
                "id": 266,
                "text": "\"Well, I'll be hanged!\" Scott exclaimed with tears in his eyes. \"You're coming with me, old fellow!\"",
                "translation": "\"Gözlerime inanamıyorum!\" diye haykırdı Scott gözlerinde yaşlarla. \"Benimle geliyorsun ihtiyar dostum!\"",
                "notes": "tears in eyes: gözlerinde yaşlar; old fellow: ihtiyar dostum"
            },
            {
                "id": 267,
                "text": "They traveled south across ocean waters to the sunny valleys of Santa Clara County in California.",
                "translation": "Okyanus suları üzerinden güneye, Kaliforniya'nın Santa Clara bölgesindeki güneşli vadilerine yolculuk ettiler.",
                "notes": "sunny valleys: güneşli vadiler; travel south: güneye yolculuk etmek"
            },
            {
                "id": 268,
                "text": "It was a wonderland of warmth, sprawling vineyards, orange groves, and green rolling hills.",
                "translation": "Burası sıcağın, uçsuz bucaksız üzüm bağlarının, portakal bahçelerinin ve dalgalanan yeşil tepelerin harikalar diyarıydı.",
                "notes": "sprawling vineyards: uzanan bağlar; orange groves: portakal bahçeleri"
            },
            {
                "id": 269,
                "text": "They arrived at Sierra Vista, the beautiful country estate of Judge Scott, Weedon's father.",
                "translation": "Weedon'ın babası Yargıç Scott'ın güzel kır çiftliği olan Sierra Vista'ya vardılar.",
                "notes": "country estate: kır çiftliği; Judge: Yargıç"
            },
            {
                "id": 270,
                "text": "As the carriage drove up the driveway, a graceful sheep-dog named Collie rushed out barking furiously.",
                "translation": "Fayton giriş yolundan yukarı çıkarken, Collie adında zarif bir çoban köpeği öfkeyle havlayarak dışarı fırladı.",
                "notes": "sheep-dog: çoban köpeği; bark furiously: öfkeyle havlamak"
            },
            {
                "id": 271,
                "text": "She was the guardian of the estate, and her wild wolf instinct warned her that a predator had arrived.",
                "translation": "Çiftliğin koruyucusuydu ve vahşi kurt içgüdüsü ona bir yırtıcının geldiğini fısıldıyordu.",
                "notes": "guardian of estate: çiftliğin muhafızı; wild instinct: vahşi içgüdü"
            },
            {
                "id": 272,
                "text": "Because she was a female, the code of the wolf forbade White Fang from fighting or injuring her.",
                "translation": "O bir dişi olduğu için kurt kanunu Beyaz Diş'in onunla dövüşmesini ya da onu yaralamasını yasaklıyordu.",
                "notes": "code of wolf: kurt kanunu; forbid: yasaklamak"
            },
            {
                "id": 273,
                "text": "He endured her snaps with majestic dignity, trotting proudly beside his beloved master.",
                "translation": "Sevgili efendisinin yanında gururla tırıs giderek dişi köpeğin havlamalarına asil bir vakarla katlandı.",
                "notes": "majestic dignity: asil vakar; beloved master: sevgili efendi"
            },
            {
                "id": 274,
                "text": "Judge Scott and the family were initially terrified of the gray northern wolf-dog.",
                "translation": "Yargıç Scott ve aile başlangıçta bu gri kuzey kurt köpeğinden çok korktular.",
                "notes": "initially terrified: başlangıçta dehşete düşmüş; northern: kuzeyli"
            },
            {
                "id": 275,
                "text": "\"He will kill the sheep and attack the children!\" the judge warned anxiously.",
                "translation": "\"Koyunları parçalayacak ve çocuklara saldıracak!\" diye endişeyle uyardı yargıç.",
                "notes": "kill sheep: koyunları parçalamak; warn anxiously: endişeyle uyarmak"
            },
            {
                "id": 276,
                "text": "\"Give him time, father,\" Weedon smiled, \"he understands civilization better than you think.\"",
                "translation": "\"Ona biraz zaman tanı baba,\" diye gülümsedi Weedon, \"o medeniyeti sandığından çok daha iyi anlar.\"",
                "notes": "give time: zaman tanımak; understand civilization: medeniyeti anlamak"
            },
            {
                "id": 277,
                "text": "White Fang quickly mastered the complex laws of the peaceful California estate.",
                "translation": "Beyaz Diş huzurlu Kaliforniya çiftliğinin karmaşık kurallarını hızla kavradı.",
                "notes": "master laws: kuralları kavramak; peaceful estate: huzurlu çiftlik"
            },
            {
                "id": 278,
                "text": "He learned never to chase chickens, never to harm sheep, and to protect the family's young children.",
                "translation": "Asla tavukları kovalamamayı, asla koyunlara zarar vermemeyi ve ailenin küçük çocuklarını korumayı öğrendi.",
                "notes": "chase chickens: tavukları kovalamak; harm sheep: koyunlara zarar vermek"
            },
            {
                "id": 279,
                "text": "The children rode on his back, pulled his thick fur, and hugged him without fear.",
                "translation": "Çocuklar sırtına bindiler, kalın kürkünü çekiştirdiler ve ona korkusuzca sarıldılar.",
                "notes": "ride on back: sırtına binmek; hug without fear: korkusuzca sarılmak"
            },
            {
                "id": 280,
                "text": "Collie's hostility softened into affection, and the two former enemies became devoted companions.",
                "translation": "Collie'nin düşmanlığı yerini sevgiye bıraktı ve bu iki eski düşman birbirine sadık yoldaşlar haline geldi.",
                "notes": "hostility softened: düşmanlık yumuşadı; devoted companions: sadık yoldaşlar"
            }
        ]
    },

    # Page 15 (Sentences 281-300)
    {
        "page_no": 15,
        "title": "The Blessed Wolf and the Hero's Honor",
        "tr_title": "Kutsanmış Kurt ve Ailenin Kurtarıcısı",
        "vocab_focus": [
            ("convict", "firari mahkum, kürek mahkumu"),
            ("escape", "kaçış"),
            ("hallway", "antre, koridor"),
            ("shotgun", "av tüfeği"),
            ("blessed", "kutsanmış, mübarek"),
            ("wound", "yara"),
            ("honor", "şeref, onur"),
            ("hero", "kahraman")
        ],
        "sentences": [
            {
                "id": 281,
                "text": "One summer evening, terrifying news arrived from San Quentin state prison.",
                "translation": "Bir yaz akşamı San Quentin eyalet hapishanesinden korkunç bir haber ulaştı.",
                "notes": "state prison: eyalet hapishanesi; terrifying news: korkunç haber"
            },
            {
                "id": 282,
                "text": "A monstrous murderer named Jim Hall, sentenced to prison years ago by Judge Scott, had escaped.",
                "translation": "Yıllar önce Yargıç Scott tarafından hapse mahkum edilen Jim Hall adında azılı bir katil firar etmişti.",
                "notes": "monstrous murderer: azılı katil; sentenced to prison: hapse mahkum edilmiş"
            },
            {
                "id": 283,
                "text": "Jim Hall had sworn to kill the judge and slaughter his entire family in bloody revenge.",
                "translation": "Jim Hall yargıcı öldürmeye ve kanlı bir intikamla bütün ailesini kılıçtan geçirmeye yemin etmişti.",
                "notes": "bloody revenge: kanlı intikam; swear to kill: öldürmeye yemin etmek"
            },
            {
                "id": 284,
                "text": "That midnight, a dark figure crept silently through the moonlit grounds of Sierra Vista.",
                "translation": "O gece yarısı karanlık bir silüet, ay ışığının aydınlattığı Sierra Vista arazisi boyunca sessizce süzüldü.",
                "notes": "dark figure: karanlık silüet; moonlit grounds: ay ışığıyla aydınlanan arazi"
            },
            {
                "id": 285,
                "text": "He climbed onto the porch, forced open the library window, and stepped inside with a drawn revolver.",
                "translation": "Verandaya tırmandı, kütüphane penceresini zorlayarak açtı ve çekili tabancasıyla içeri adım attı.",
                "notes": "drawn revolver: çekilmiş tabanca; force open: zorlayarak açmak"
            },
            {
                "id": 286,
                "text": "White Fang was sleeping at the foot of the stairs, on guard as always.",
                "translation": "Beyaz Diş merdivenlerin dibinde uyuyordu, her zamanki gibi nöbetteydi.",
                "notes": "foot of stairs: merdiven dibi; on guard: nöbette"
            },
            {
                "id": 287,
                "text": "He smelled the strange man's murderous scent and heard the faint creak of the floorboard.",
                "translation": "Yabancı adamın ölümcül kokusunu aldı ve döşeme tahtasının hafif gıcırtısını duydu.",
                "notes": "murderous scent: ölümcül koku; faint creak: hafif gıcırtı"
            },
            {
                "id": 288,
                "text": "He gave no bark, no warning growl; he launched himself through the air like a catapult.",
                "translation": "Hiç havlamadı, tek bir uyarıcı hırıltı bile çıkarmadı; bir mancınık gibi kendini havaya fırlattı.",
                "notes": "launch like catapult: mancınık gibi fırlatmak; no warning: uyarısız"
            },
            {
                "id": 289,
                "text": "He struck Jim Hall full in the chest, bearing him backward to the floor in a tempest of fury.",
                "translation": "Jim Hall'un tam göğsüne çarptı, onu bir öfke fırtınası içinde gerisin geri yere devirdi.",
                "notes": "bear to floor: yere devirmek; tempest of fury: öfke fırtınası"
            },
            {
                "id": 290,
                "text": "A terrible struggle erupted in the dark hallway: furniture crashed, pistols roared, and teeth tore flesh.",
                "translation": "Karanlık koridorda korkunç bir boğuşma patlak verdi: mobilyalar devrildi, tabancalar kükredi ve dişler eti parçaladı.",
                "notes": "terrible struggle: korkunç boğuşma; furniture crashed: mobilyalar devrildi"
            },
            {
                "id": 291,
                "text": "Hall fired three bullets into the wolf at point-blank range, shattering his leg and puncturing his lungs.",
                "translation": "Hall sıfır mesafeden kurda üç el ateş etti, bacağını parçaladı ve ciğerlerini deldi.",
                "notes": "point-blank range: sıfır mesafe; puncture lungs: ciğerleri delmek"
            },
            {
                "id": 292,
                "text": "Despite mortal agony, White Fang clamped his jaws onto the killer's throat and did not let go until life ceased.",
                "translation": "Ölümcül ıstıraba rağmen Beyaz Diş çenesini katilin boğazına kilitledi ve canı çıkana kadar asla bırakmadı.",
                "notes": "mortal agony: ölümcül ıstırap; life ceased: hayat son buldu"
            },
            {
                "id": 293,
                "text": "Judge Scott and Weedon rushed downstairs with lamps, discovering Jim Hall dead upon the bloodstained carpet.",
                "translation": "Yargıç Scott ve Weedon ellerinde lambalarla merdivenlerden aşağı koştular, kana bulanmış halının üzerinde Jim Hall'u ölü buldular.",
                "notes": "bloodstained carpet: kanlı halı; rush downstairs: aşağı koşmak"
            },
            {
                "id": 294,
                "text": "Beside the villain lay White Fang, riddled with bullets, broken bones, and bleeding from a dozen wounds.",
                "translation": "Hainin yanında kurşunlarla delik deşik olmuş, kemikleri kırılmış ve bir düzine yaradan kan kaybeden Beyaz Diş yatıyordu.",
                "notes": "riddled with bullets: kurşunlarla delik deşik; villain: cani, hain"
            },
            {
                "id": 295,
                "text": "The surgeon examined him and shook his head: \"There is one chance in a thousand that he can survive.\"",
                "translation": "Cerrah onu muayene etti ve başını iki yana salladı: \"Hayatta kalabilmesi için binde bir ihtimal var.\"",
                "notes": "surgeon: cerrah; one chance in a thousand: binde bir ihtimal"
            },
            {
                "id": 296,
                "text": "\"He must have that one chance!\" the weeping family insisted, sparing no expense or care.",
                "translation": "\"O tek şansı almalı!\" diye ısrar etti gözü yaşlı aile; hiçbir masraftan ve özenden kaçınmadılar.",
                "notes": "spare no expense: hiçbir masraftan kaçınmamak; weeping: ağlayan"
            },
            {
                "id": 297,
                "text": "Bound in splints and bandages, the northern wolf's incredible vitality fought back against death.",
                "translation": "Ateller ve sargılar içine sarılmış olan kuzeyli kurdun inanılmaz dirayeti ölüme karşı savaştı.",
                "notes": "splints and bandages: ateller ve sargılar; vitality: yaşama gücü, dirayet"
            },
            {
                "id": 298,
                "text": "Week after week he healed, until at last the bandages were removed and he stood upon his feet once more.",
                "translation": "Haftalar geçtikçe iyileşti; ta ki sonunda sargılar çıkarılana ve o bir kez daha ayakları üzerinde doğrulana kadar.",
                "notes": "healed: iyileşti; stood upon feet: ayakları üzerinde durdu"
            },
            {
                "id": 299,
                "text": "The family gathered around him with tears of devotion, christening him forever as 'The Blessed Wolf'.",
                "translation": "Aile sevgi ve minnet gözyaşlarıyla etrafında toplandı; ona sonsuza dek 'Kutsanmış Kurt' unvanını verdiler.",
                "notes": "The Blessed Wolf: Kutsanmış Kurt; christen: adlandırmak, unvan vermek"
            },
            {
                "id": 300,
                "text": "Outside on the sunny lawn, Collie led forth five tumbling puppies to meet their proud, loving father in the warm California sun.",
                "translation": "Dışarıda güneşli çimenlikte Collie, sıcak Kaliforniya güneşi altında gururlu ve sevgi dolu babalarıyla tanışmaları için beş yuvarlanan eniği öne çıkardı.",
                "notes": "tumbling puppies: yuvarlanan enikler; proud father: gururlu baba"
            }
        ]
    }
]

def main():
    total_pages = len(pages_data)
    total_sentences = sum(len(p["sentences"]) for p in pages_data)
    total_vocab = sum(len(p.get("vocab_focus", [])) for p in pages_data)

    print(f"Book 24 Data Verification:")
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

    out_file = os.path.join(os.path.dirname(__file__), "book_24_data.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('BOOK_TITLE = "White Fang"\n')
        f.write('AUTHOR = "Jack London"\n')
        f.write("PAGES_DATA = ")
        import pprint
        f.write(pprint.pformat(pages_data, indent=4, width=120))
        f.write("\n")

    print(f"Successfully wrote {out_file}")

if __name__ == "__main__":
    main()
