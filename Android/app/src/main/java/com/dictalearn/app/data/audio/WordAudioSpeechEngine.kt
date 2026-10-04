package com.dictalearn.app.data.audio

import android.content.Context
import com.dictalearn.app.data.download.DownloadItem
import com.dictalearn.app.data.download.FileDownloader
import com.dictalearn.app.domain.audio.SpeechEngine
import com.dictalearn.app.domain.dictionary.Dictionary
import com.dictalearn.app.domain.library.RemoteLessons
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.SupervisorJob
import kotlinx.coroutines.cancel
import kotlinx.coroutines.launch
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import kotlinx.coroutines.withContext
import org.json.JSONObject
import java.io.File

/**
 * Pronounces words with the studio-voice sprites of lessons/word_audio (built by
 * tools/build_word_audio.py), the same narrator as the books. The index ships in the APK; the
 * per-letter MP3s (~2 MB each) are downloaded the first time a word with that letter is spoken.
 * Words missing from the pack, or a sprite that can't be downloaded, fall back to the system
 * TextToSpeech engine.
 */
class WordAudioSpeechEngine(
    private val context: Context,
    private val fallback: SpeechEngine,
    private val downloader: FileDownloader = FileDownloader()
) : SpeechEngine {
    private val scope = CoroutineScope(Dispatchers.Main + SupervisorJob())
    private val player = MediaPlayerAudioEngine(context)
    private var loadedLetter: Char? = null
    private var request = 0
    private val downloadLock = Mutex()
    private val spriteDir = File(context.filesDir, "word_audio")
    private val bundledSprites: Boolean by lazy {
        runCatching { context.assets.list("lessons/word_audio").orEmpty().any { it.endsWith(".mp3") } }.getOrDefault(false)
    }

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
        val id = ++request
        val letter = word.first()
        scope.launch {
            if (loadedLetter != letter) {
                val source = spriteSource(letter)
                if (id != request) return@launch // a newer word was requested meanwhile
                if (source == null) {
                    fallback.speak(text)
                    return@launch
                }
                player.load(source) // async; the range plays once prepared
                loadedLetter = letter
            }
            player.playRange(range[0], range[1])
        }
    }

    private suspend fun spriteSource(letter: Char): String? {
        if (bundledSprites) return "assets/lessons/word_audio/$letter.mp3"
        val file = File(spriteDir, "$letter.mp3")
        return downloadLock.withLock {
            if (!file.exists()) {
                runCatching {
                    withContext(Dispatchers.IO) {
                        downloader.download(listOf(DownloadItem(RemoteLessons.wordAudioUrl(letter), file))) {}
                    }
                }
            }
            file.path.takeIf { file.exists() }
        }
    }

    override fun stop() {
        request++
        player.pause()
        fallback.stop()
    }

    override fun dispose() {
        scope.cancel()
        player.dispose()
        fallback.dispose()
    }
}
