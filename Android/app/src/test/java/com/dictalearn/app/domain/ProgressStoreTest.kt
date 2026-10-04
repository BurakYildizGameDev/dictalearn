package com.dictalearn.app.domain

import com.dictalearn.app.domain.progress.KeyValueStore
import com.dictalearn.app.domain.progress.ProgressStore
import org.junit.Assert.*
import org.junit.Before
import org.junit.Test

class ProgressStoreTest {

    private class MemoryStore : KeyValueStore {
        val data = mutableMapOf<String, String>()
        override fun getString(key: String): String? = data[key]
        override fun putString(key: String, value: String) {
            data[key] = value
        }
    }

    private lateinit var kv: MemoryStore
    private lateinit var store: ProgressStore

    @Before
    fun setUp() {
        kv = MemoryStore()
        store = ProgressStore(kv) { 1000L }
    }

    @Test
    fun unknownLesson_returnsNull() {
        assertNull(store.get("book_01"))
    }

    @Test
    fun record_keepsFurthestIndex_andClamps() {
        store.record("book_01", 5, 300)
        store.record("book_01", 2, 300)
        val p = store.get("book_01")!!
        assertEquals(2, p.segmentIndex)
        assertEquals(5, p.furthestIndex)
        assertFalse(p.completed)

        store.record("book_02", 999, 10)
        assertEquals(9, store.get("book_02")!!.segmentIndex)
    }

    @Test
    fun markCompleted_isSticky_andPercentIs100() {
        store.markCompleted("book_01", 300)
        store.record("book_01", 0, 300)
        val p = store.get("book_01")!!
        assertTrue(p.completed)
        assertEquals(100, p.percent)
    }

    @Test
    fun persistsAcrossInstances_andSurvivesCorruptData() {
        store.record("book_01", 3, 10)
        assertEquals(3, ProgressStore(kv).get("book_01")!!.segmentIndex)

        kv.data["dictalearn_progress_v1"] = "{not json"
        assertNull(ProgressStore(kv).get("book_01"))
    }

    @Test
    fun percent_isBasedOnFurthestIndex() {
        store.record("book_01", 149, 300)
        assertEquals(50, store.get("book_01")!!.percent)
    }
}
