package com.dictalearn.app.data.audio

import android.content.Context
import com.dictalearn.app.domain.audio.SpeechEngine
import com.dictalearn.app.domain.dictionary.Dictionary
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.SupervisorJob
import kotlinx.coroutines.cancel
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import org.json.JSONObject

/**
 * Pronounces words with the studio-voice sprites in assets/lessons/word_audio (built by
 * tools/build_word_audio.py), the same narrator as the books. Words missing from the pack fall
 * back to the system TextToSpeech engine.
 */
class WordAudioSpeechEngine(
    private val context: Context,
    private val fallback: SpeechEngine
) : SpeechEngine {
    private val scope = CoroutineScope(Dispatchers.Main + SupervisorJob())
    private val player = MediaPlayerAudioEngine(context)
    private var loadedLetter: Char? = null

    @Volatile
    private var index: Map<String, IntArray>? = null

    init {
        scope.launch {
            index = withContext(Dispatchers.IO) {
                runCatching {
                    val json = context.assets.open("lessons/word_audio/index.json").bufferedReader().use { it.readText() }
                    val words = JSONObject(json).getJSONObject("words")
                    val map = HashMap<String, IntArray>(words.length() * 2)
                    for (key in words.keys()) {
                        val range = words.getJSONArray(key)
                        map[key] = intArrayOf(range.getInt(0), range.getInt(1))
                    }
                    map
                }.getOrNull()
            }
        }
    }

    override fun speak(text: String) {
        val word = Dictionary.normalize(text)
        val range = index?.get(word)
        if (range == null) {
            fallback.speak(text)
            return
        }
        fallback.stop()
        val letter = word.first()
        if (loadedLetter != letter) {
            player.load("assets/lessons/word_audio/$letter.mp3") // async; the range plays once prepared
            loadedLetter = letter
        }
        player.playRange(range[0], range[1])
    }

    override fun stop() {
        player.pause()
        fallback.stop()
    }

    override fun dispose() {
        scope.cancel()
        player.dispose()
        fallback.dispose()
    }
}
