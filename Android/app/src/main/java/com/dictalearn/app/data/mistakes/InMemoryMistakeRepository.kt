package com.dictalearn.app.data.mistakes

import com.dictalearn.app.domain.mistakes.MistakeRecord
import com.dictalearn.app.domain.mistakes.MistakeRepository

class InMemoryMistakeRepository : MistakeRepository {
    private val mistakes = mutableListOf<MistakeRecord>()

    override fun getMistakes(): List<MistakeRecord> = synchronized(this) {
        mistakes.toList()
    }

    override fun addMistakes(mistakes: List<MistakeRecord>) {
        synchronized(this) {
            this.mistakes.addAll(mistakes)
        }
    }

    override fun clearMistakes() {
        synchronized(this) {
            mistakes.clear()
        }
    }

    override fun getWordFrequencies(): Map<String, Int> = synchronized(this) {
        mistakes.groupingBy { it.word.lowercase() }.eachCount()
    }
}
