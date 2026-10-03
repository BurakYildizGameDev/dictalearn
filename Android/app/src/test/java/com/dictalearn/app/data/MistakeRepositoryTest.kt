package com.dictalearn.app.data

import com.dictalearn.app.data.mistakes.InMemoryMistakeRepository
import com.dictalearn.app.domain.mistakes.MistakeKind
import com.dictalearn.app.domain.mistakes.MistakeRecord
import org.junit.Assert.*
import org.junit.Before
import org.junit.Test

class MistakeRepositoryTest {

    private lateinit var repo: InMemoryMistakeRepository

    @Before
    fun setUp() {
        repo = InMemoryMistakeRepository()
    }

    @Test
    fun startsEmpty_andAddsMistakes() {
        assertTrue(repo.getMistakes().isEmpty())

        repo.addMistakes(
            listOf(
                MistakeRecord(word = "suitcase", kind = MistakeKind.SUBSTITUTE, typed = "bag", lessonId = "l1", segmentId = 1),
                MistakeRecord(word = "brown", kind = MistakeKind.MISSING, lessonId = "l1", segmentId = 1)
            )
        )

        val mistakes = repo.getMistakes()
        assertEquals(2, mistakes.size)
        assertEquals("suitcase", mistakes[0].word)
        assertEquals(MistakeKind.SUBSTITUTE, mistakes[0].kind)
        assertEquals("brown", mistakes[1].word)
    }

    @Test
    fun computesWordFrequencies() {
        repo.addMistakes(
            listOf(
                MistakeRecord(word = "suitcase", kind = MistakeKind.SUBSTITUTE, lessonId = "l1", segmentId = 1),
                MistakeRecord(word = "Suitcase", kind = MistakeKind.MISSING, lessonId = "l1", segmentId = 2),
                MistakeRecord(word = "door", kind = MistakeKind.MISSING, lessonId = "l1", segmentId = 1)
            )
        )

        val freqs = repo.getWordFrequencies()
        assertEquals(2, freqs["suitcase"])
        assertEquals(1, freqs["door"])
    }

    @Test
    fun clearMistakes_resetsRepository() {
        repo.addMistakes(
            listOf(
                MistakeRecord(word = "suitcase", kind = MistakeKind.SUBSTITUTE, lessonId = "l1", segmentId = 1)
            )
        )
        assertFalse(repo.getMistakes().isEmpty())

        repo.clearMistakes()
        assertTrue(repo.getMistakes().isEmpty())
        assertTrue(repo.getWordFrequencies().isEmpty())
    }
}
