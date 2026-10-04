package com.dictalearn.app.domain.words

data class WordToken(
    val raw: String,
    val clean: String,
    val punctuation: String? = null
)

enum class WordFeedback {
    IDLE,
    INCORRECT
}

object WordModeEngine {
    private val PUNCT_REGEX = Regex("^[\\p{P}\\p{S}]+|[\\p{P}\\p{S}]+$")

    fun cleanWord(word: String): String {
        return word.trim()
            .replace(PUNCT_REGEX, "")
            .replace("’", "'")
            .replace("`", "'")
            .lowercase()
    }

    fun tokenizeSentence(text: String): List<WordToken> {
        val parts = text.trim().split(Regex("\\s+")).filter { it.isNotBlank() }
        return parts.map { raw ->
            val match = Regex("""^(.*?)([.,!?;:…"“”]+)?$""").find(raw)
            val base = match?.groups?.get(1)?.value ?: raw
            val punctuation = match?.groups?.get(2)?.value
            val clean = cleanWord(base)
            WordToken(raw = raw, clean = clean, punctuation = punctuation)
        }
    }

    fun checkWord(expectedClean: String, typed: String): Boolean {
        return cleanWord(typed) == cleanWord(expectedClean)
    }
}
