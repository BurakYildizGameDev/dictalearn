package com.dictalearn.app.domain.translation

/** Translates free English text to Turkish (on-device ML Kit in production). */
interface SentenceTranslator {
    suspend fun translate(text: String): Result<String>
    fun close()
}
