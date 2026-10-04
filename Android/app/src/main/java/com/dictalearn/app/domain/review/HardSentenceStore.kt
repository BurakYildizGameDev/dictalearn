package com.dictalearn.app.domain.review

import com.dictalearn.app.domain.model.Lesson
import com.dictalearn.app.domain.progress.KeyValueStore
import org.json.JSONArray
import org.json.JSONObject

/**
 * Segments answered below 70% accuracy, kept per lesson for a short review round.
 * Mirrors Web/src/domain/review/hard-sentences.ts.
 */
class HardSentenceStore(private val store: KeyValueStore) {
    companion object {
        const val THRESHOLD = 0.7
        const val SUFFIX = "::hard"
        private const val KEY = "dictalearn_hard_sentences_v1"

        /** The same lesson restricted to the hard segments (audio ranges unchanged). */
        fun subLesson(lesson: Lesson, segmentIds: List<Int>): Lesson {
            val wanted = segmentIds.toSet()
            return lesson.copy(lessonId = lesson.lessonId + SUFFIX, segments = lesson.segments.filter { it.id in wanted })
        }
    }

    private fun read(): MutableMap<String, List<Int>> = runCatching {
        val root = JSONObject(store.getString(KEY) ?: return mutableMapOf())
        root.keys().asSequence().associateWith { key ->
            val arr = root.getJSONArray(key)
            (0 until arr.length()).map { arr.getInt(it) }
        }.toMutableMap()
    }.getOrDefault(mutableMapOf())

    private fun write(all: Map<String, List<Int>>) {
        val root = JSONObject()
        all.forEach { (k, v) -> root.put(k, JSONArray(v)) }
        store.putString(KEY, root.toString())
    }

    /** Below the threshold the segment becomes hard; a good later result removes it. */
    fun record(lessonId: String, segmentId: Int, accuracy: Double) {
        val all = read()
        val ids = all[lessonId].orEmpty().toMutableSet()
        if (accuracy < THRESHOLD) ids.add(segmentId) else ids.remove(segmentId)
        if (ids.isEmpty()) all.remove(lessonId) else all[lessonId] = ids.sorted()
        write(all)
    }

    fun list(lessonId: String): List<Int> = read()[lessonId].orEmpty()

    fun count(lessonId: String): Int = list(lessonId).size
}
