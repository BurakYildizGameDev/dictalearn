package com.dictalearn.app.domain

import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.model.Segment
import com.dictalearn.app.domain.progress.KeyValueStore
import com.dictalearn.app.domain.review.HardSentenceStore
import org.junit.Assert.*
import org.junit.Test

class HardSentenceStoreTest {

    private class MemoryStore : KeyValueStore {
        val data = mutableMapOf<String, String>()
        override fun getString(key: String): String? = data[key]
        override fun putString(key: String, value: String) {
            data[key] = value
        }
    }

    @Test
    fun marksBelowThreshold_andUnmarksGoodResults() {
        val kv = MemoryStore()
        val store = HardSentenceStore(kv)
        store.record("book_01", 3, 0.4)
        store.record("book_01", 1, 0.69)
        store.record("book_01", 2, 0.9)
        assertEquals(listOf(1, 3), store.list("book_01"))
        store.record("book_01", 3, 1.0)
        assertEquals(listOf(1), store.list("book_01"))
        assertEquals(0, store.count("other"))
        assertEquals(listOf(1), HardSentenceStore(kv).list("book_01"))
    }

    @Test
    fun subLesson_keepsOriginalAudioRanges() {
        val lesson = Lesson(1, "book_01", "Book", "en", "tr", "audio.mp3", null,
            (1..4).map { Segment(it, it * 1000, it * 1000 + 900, "Sentence $it.") })
        val sub = HardSentenceStore.subLesson(lesson, listOf(2, 4, 99))
        assertEquals("book_01::hard", sub.lessonId)
        assertEquals(listOf(2000 to 2900, 4000 to 4900), sub.segments.map { it.startMs to it.endMs })
    }
}
