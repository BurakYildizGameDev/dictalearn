package com.dictalearn.app.domain

import com.dictalearn.app.domain.mistakes.MistakeKind
import com.dictalearn.app.domain.mistakes.MistakeRecord
import com.dictalearn.app.domain.progress.KeyValueStore
import com.dictalearn.app.domain.review.SrsStore
import org.junit.Assert.*
import org.junit.Before
import org.junit.Test
import java.time.LocalDate
import java.time.ZoneId

class SrsStoreTest {

    private class MemoryStore : KeyValueStore {
        val data = mutableMapOf<String, String>()
        override fun getString(key: String): String? = data[key]
        override fun putString(key: String, value: String) {
            data[key] = value
        }
    }

    private lateinit var kv: MemoryStore
    private var today: LocalDate = LocalDate.of(2026, 10, 4)
    private lateinit var store: SrsStore

    private fun missed(word: String, day: LocalDate) = MistakeRecord(
        word = word, kind = MistakeKind.MISSING, lessonId = "b", segmentId = 1,
        timestamp = day.atTime(12, 0).atZone(ZoneId.systemDefault()).toInstant().toEpochMilli()
    )

    @Before
    fun setUp() {
        kv = MemoryStore()
        today = LocalDate.of(2026, 10, 4)
        store = SrsStore(kv) { today }
    }

    @Test
    fun sync_createsOneDueCardPerWord() {
        store.sync(listOf(missed("Small", today.minusDays(3)), missed("small", today.minusDays(2)), missed("cold", today.minusDays(1))))
        assertEquals(listOf("cold", "small"), store.dueCards().map { it.word }.sorted())
        assertEquals(0, store.dueCards().first().box)
    }

    @Test
    fun correctAnswers_climbBoxesWithGrowingIntervals() {
        store.sync(listOf(missed("cold", today.minusDays(1))))
        store.answer("cold", true)
        var card = store.get("cold")!!
        assertEquals(1, card.box)
        assertEquals(today.plusDays(SrsStore.INTERVAL_DAYS[1].toLong()), card.due)
        assertTrue(store.dueCards().isEmpty())

        today = card.due
        store.answer("cold", true)
        card = store.get("cold")!!
        assertEquals(2, card.box)
        assertEquals(today.plusDays(SrsStore.INTERVAL_DAYS[2].toLong()), card.due)

        repeat(10) { store.answer("cold", true) }
        assertEquals(SrsStore.INTERVAL_DAYS.size - 1, store.get("cold")!!.box)
    }

    @Test
    fun wrongAnswer_andNewDictationMistake_resetTheCard() {
        store.sync(listOf(missed("cold", today.minusDays(1))))
        store.answer("cold", true)
        store.answer("cold", false)
        assertEquals(0, store.get("cold")!!.box)
        assertEquals(today.plusDays(1), store.get("cold")!!.due)
        assertEquals(1, store.get("cold")!!.lapses)
        assertTrue(store.dueCards().isEmpty())

        store.answer("cold", true) // reviewed today
        store.sync(listOf(missed("cold", today.plusDays(1))))
        assertEquals(0, store.get("cold")!!.box)
    }

    @Test
    fun stats_persistence_andRemoval() {
        store.sync(listOf(missed("cold", today), missed("hit", today)))
        store.answer("hit", true)
        assertEquals(SrsStore.Stats(total = 2, due = 1, learned = 0), store.stats())
        assertEquals(1, SrsStore(kv) { today }.get("hit")!!.box)
        store.sync(emptyList())
        assertNull(store.get("cold"))
    }
}
