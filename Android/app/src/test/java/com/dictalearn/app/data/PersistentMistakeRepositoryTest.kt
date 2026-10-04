package com.dictalearn.app.data

import com.dictalearn.app.data.mistakes.PersistentMistakeRepository
import com.dictalearn.app.domain.mistakes.MistakeKind
import com.dictalearn.app.domain.mistakes.MistakeRecord
import com.dictalearn.app.domain.progress.KeyValueStore
import org.junit.Assert.*
import org.junit.Test

class PersistentMistakeRepositoryTest {

    private class MemoryStore : KeyValueStore {
        val data = mutableMapOf<String, String>()
        override fun getString(key: String): String? = data[key]
        override fun putString(key: String, value: String) {
            data[key] = value
        }
    }

    @Test
    fun mistakes_surviveANewRepositoryInstance() {
        val store = MemoryStore()
        PersistentMistakeRepository(store).addMistakes(
            listOf(
                MistakeRecord("Small", MistakeKind.SUBSTITUTE, "smal", "book_01", 3, 42L),
                MistakeRecord("small", MistakeKind.MISSING, null, "book_01", 4, 43L)
            )
        )

        val reloaded = PersistentMistakeRepository(store)
        assertEquals(2, reloaded.getMistakes().size)
        assertEquals("smal", reloaded.getMistakes()[0].typed)
        assertNull(reloaded.getMistakes()[1].typed)
        assertEquals(mapOf("small" to 2), reloaded.getWordFrequencies())
    }

    @Test
    fun corruptData_isIgnored_andClearPersists() {
        val store = MemoryStore()
        store.data["dictalearn_mistakes_v1"] = "[{broken"
        val repo = PersistentMistakeRepository(store)
        assertTrue(repo.getMistakes().isEmpty())

        repo.addMistakes(listOf(MistakeRecord("x", MistakeKind.MISSING, null, "l", 1)))
        repo.clearMistakes()
        assertTrue(PersistentMistakeRepository(store).getMistakes().isEmpty())
    }
}
