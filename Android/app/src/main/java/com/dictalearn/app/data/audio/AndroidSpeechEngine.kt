package com.dictalearn.app.data.audio

import android.content.Context
import android.speech.tts.TextToSpeech
import com.dictalearn.app.domain.audio.SpeechEngine
import java.util.Locale

class AndroidSpeechEngine(context: Context) : SpeechEngine {
    private var tts: TextToSpeech? = null
    private var isReady = false

    init {
        tts = TextToSpeech(context.applicationContext) { status ->
            if (status == TextToSpeech.SUCCESS) {
                tts?.language = Locale.US
                tts?.setSpeechRate(0.95f)
                isReady = true
            }
        }
    }

    override fun speak(text: String) {
        if (isReady && text.isNotBlank()) {
            tts?.speak(text, TextToSpeech.QUEUE_FLUSH, null, "DictaLearnTTS")
        }
    }

    override fun stop() {
        tts?.stop()
    }

    override fun dispose() {
        tts?.stop()
        tts?.shutdown()
        tts = null
    }
}
