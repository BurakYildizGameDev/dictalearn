# -*- coding: utf-8 -*-
"""
Build lesson data and audio for denme.pdf (The Camping Trip)
"""

import os
import json
import asyncio
import edge_tts
import soundfile as sf
import numpy as np

SENTENCES = [
    {
        "id": 1,
        "text": "\"Don't forget your warm clothes,\" says Louisa to her children.",
        "translation": "\"Sıcak tutan kıyafetlerinizi unutmayın,\" der Louisa çocuklarına.",
        "notes": "warm clothes: sıcak tutan kalın kıyafetler"
    },
    {
        "id": 2,
        "text": "\"I'm packing mine now.\"",
        "translation": "\"Ben benimkileri şimdi topluyorum.\"",
        "notes": "packing: bavul/çanta hazırlamak"
    },
    {
        "id": 3,
        "text": "She takes her backpack upstairs and looks at her notebook.",
        "translation": "Sırt çantasını üst kata çıkarır ve defterine bakar.",
        "notes": "backpack: sırt çantası"
    },
    {
        "id": 4,
        "text": "It says \"Camping Trip\" at the top of a long list.",
        "translation": "Uzun bir listenin en başında \"Kamp Gezisi\" yazmaktadır.",
        "notes": "at the top of: ...nın en tepesinde"
    },
    {
        "id": 5,
        "text": "She packs two pairs of gloves, two scarves, two coats, five shirts and ten pairs of socks.",
        "translation": "İki çift eldiven, iki atkı, iki palto, beş gömlek ve on çift çorap koyar.",
        "notes": "two pairs of gloves: iki çift eldiven"
    },
    {
        "id": 6,
        "text": "\"It's only three days,\" says her husband. \"Just in case,\" she explains.",
        "translation": "\"Yalnızca üç gün sürecek,\" der kocası. \"Ne olur ne olmaz diye,\" diye açıklar Louisa.",
        "notes": "just in case: her ihtimale karşı, ne olur ne olmaz"
    },
    {
        "id": 7,
        "text": "They go to the kitchen. \"Don't forget to bring enough food,\" she tells her husband.",
        "translation": "Mutfağa giderler. \"Yeterli yiyecek getirmeyi unutma,\" der kocasına.",
        "notes": "enough food: yeterli yiyecek"
    },
    {
        "id": 8,
        "text": "He packs cereal bars, peanut butter sandwiches, cheese and fruit.",
        "translation": "Kocası tahıl barları, fıstık ezmeli sandviçler, peynir ve meyve paketler.",
        "notes": "cereal bars: tahıl barları"
    },
    {
        "id": 9,
        "text": "Louisa opens the cupboard and takes out four cans of beans, five cans of tuna and eight cans of tomatoes.",
        "translation": "Louisa dolabı açar; dört kutu fasulye, beş kutu ton balığı ve sekiz kutu domates konservesi çıkarır.",
        "notes": "cans of tuna: ton balığı konserveleri"
    },
    {
        "id": 10,
        "text": "Then she gets three packets of pasta and puts it all in her backpack.",
        "translation": "Ardından üç paket makarna alır ve hepsini sırt çantasına koyar.",
        "notes": "packets of pasta: makarna paketleri"
    },
    {
        "id": 11,
        "text": "Her husband looks surprised. \"We need healthy meals,\" Louisa explains.",
        "translation": "Kocası şaşkınlıkla bakar. \"Sağlıklı öğünlere ihtiyacımız var,\" diye açıklar Louisa.",
        "notes": "looks surprised: şaşırmış görünür"
    },
    {
        "id": 12,
        "text": "\"But you can't cook them?\" Louisa picks up a box and opens it. It's a new camping stove.",
        "translation": "\"Ama onları pişiremezsin ki?\" Louisa bir kutuyu alıp açar; bu yeni bir kamp ocağıdır.",
        "notes": "camping stove: portatif kamp ocağı"
    },
    {
        "id": 13,
        "text": "\"Don't forget to bring the gas,\" she tells her husband.",
        "translation": "\"Tüp gazı getirmeyi unutma,\" der kocasına.",
        "notes": "bring the gas: gazı/tüpü getirmek"
    },
    {
        "id": 14,
        "text": "Louisa puts her heavy backpack on her back. \"Maybe that's too heavy, dear?\"",
        "translation": "Louisa ağır sırt çantasını sırtına takar. \"Belki de o çok ağırdır hayatım?\"",
        "notes": "too heavy: fazlasıyla ağır"
    },
    {
        "id": 15,
        "text": "Louisa's face is red. \"It's fine,\" she says, and they put everything in the car.",
        "translation": "Louisa'nın yüzü kıpkırmızıdır. \"Gayet iyi,\" der ve her şeyi arabaya koyarlar.",
        "notes": "face is red: yüzü kızarmış"
    },
    {
        "id": 16,
        "text": "They drive for eight hours through the beautiful countryside.",
        "translation": "Güzel kırsal araziden geçerek sekiz saat boyunca araba sürerler.",
        "notes": "drive for eight hours: sekiz saat boyunca sürmek"
    },
    {
        "id": 17,
        "text": "At six o'clock they park the car in the middle of a large field as the sun is setting.",
        "translation": "Saat altıda güneş batarken arabayı geniş bir tarlanın ortasına park ederler.",
        "notes": "sun is setting: güneş batıyor"
    },
    {
        "id": 18,
        "text": "\"I'm cold,\" says their daughter, and Louisa gives her the warm coat.",
        "translation": "\"Üşüdüm,\" der kızları; Louisa ona kalın paltoyu verir.",
        "notes": "I'm cold: üşüdüm"
    },
    {
        "id": 19,
        "text": "They set up the camping table and chairs, and Louisa connects the gas canister to the stove.",
        "translation": "Kamp masasını ve sandalyelerini kurarlar; Louisa gaz tüpünü ocağa bağlar.",
        "notes": "gas canister: gaz kartuşu / tüpü"
    },
    {
        "id": 20,
        "text": "She takes a can opener out of her backpack and opens the cans to cook a delicious meal.",
        "translation": "Sırt çantasından bir konserve açacağı çıkarır ve lezzetli bir yemek pişirmek için konserveleri açar.",
        "notes": "can opener: konserve açacağı"
    },
    {
        "id": 21,
        "text": "Afterwards, they all enjoy the hot meal and thank Louisa for cooking.",
        "translation": "Sonrasında hepsi sıcak yemeğin tadını çıkarır ve pişirdiği için Louisa'ya teşekkür eder.",
        "notes": "enjoy the hot meal: sıcak yemeğin tadını çıkarmak"
    },
    {
        "id": 22,
        "text": "She says, \"It's almost dark now. Let's set up the tent.\"",
        "translation": "Louisa, \"Neredeyse hava karardı. Haydi çadırı kuralım,\" der.",
        "notes": "set up the tent: çadırı kurmak"
    },
    {
        "id": 23,
        "text": "Her husband is looking in the car. \"Where's the tent?\" he says.",
        "translation": "Kocası arabanın içine bakınır. \"Çadır nerede?\" der şaşkınlıkla.",
        "notes": "where's the tent: çadır nerede?"
    }
]

async def build():
    out_dir = os.path.join("Web", "public", "lessons", "custom_denme")
    os.makedirs(out_dir, exist_ok=True)
    
    current_ms = 300
    wav_parts = [np.zeros(int(0.3 * 24000), dtype=np.int16)]
    
    for s in SENTENCES:
        s_id = s["id"]
        temp_file = f"temp_denme_{s_id}.mp3"
        comm = edge_tts.Communicate(s["text"], "en-US-ChristopherNeural")
        await comm.save(temp_file)
        
        audio_data, sr = sf.read(temp_file, dtype="int16")
        if os.path.exists(temp_file):
            os.remove(temp_file)
            
        dur_ms = int(len(audio_data) / sr * 1000)
        s["start_ms"] = current_ms
        s["end_ms"] = current_ms + dur_ms
        wav_parts.append(audio_data)
        
        pause = int(0.4 * sr)
        wav_parts.append(np.zeros(pause, dtype=np.int16))
        current_ms = s["end_ms"] + 400
        
    full_audio = np.concatenate(wav_parts)
    wav_path = os.path.join(out_dir, "audio.wav")
    mp3_path = os.path.join(out_dir, "audio.mp3")
    sf.write(wav_path, full_audio, 24000)
    sf.write(mp3_path, full_audio, 24000)
    
    lesson_data = {
        "schema_version": 1,
        "lesson_id": "custom_denme",
        "title": "The Camping Trip (Kamp Gezisi) — denme.pdf",
        "source_lang": "en",
        "target_lang": "tr",
        "audio_file": "audio.mp3",
        "attribution": {
            "source": "Özel Yüklenen PDF (denme.pdf)",
            "license": "Custom Study"
        },
        "segments": SENTENCES
    }
    
    json_path = os.path.join(out_dir, "lesson.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(lesson_data, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully created custom_denme lesson with {len(SENTENCES)} sentences!")

if __name__ == "__main__":
    asyncio.run(build())
