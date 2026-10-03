package com.dictalearn.app.domain.mistakes

enum class MistakeKind {
    SUBSTITUTE,
    MISSING,
    UNKNOWN
}

data class MistakeRecord(
    val word: String,
    val kind: MistakeKind,
    val typed: String? = null,
    val lessonId: String,
    val segmentId: Int,
    val timestamp: Long = System.currentTimeMillis()
)

interface MistakeRepository {
    fun getMistakes(): List<MistakeRecord>
    fun addMistakes(mistakes: List<MistakeRecord>)
    fun clearMistakes()
    fun getWordFrequencies(): Map<String, Int>
}
