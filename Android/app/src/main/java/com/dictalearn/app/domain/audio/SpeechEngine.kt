package com.dictalearn.app.domain.audio

interface SpeechEngine {
    fun speak(text: String)
    fun stop()
    fun dispose()
}

class FakeSpeechEngine : SpeechEngine {
    val spokenWords = mutableListOf<String>()

    override fun speak(text: String) {
        spokenWords.add(text)
    }

    override fun stop() {}

    override fun dispose() {}
}
