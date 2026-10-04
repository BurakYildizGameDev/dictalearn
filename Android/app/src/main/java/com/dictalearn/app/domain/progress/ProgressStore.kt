package com.dictalearn.app.domain.progress

import org.json.JSONObject
import kotlin.math.roundToInt

/** Minimal string storage so the store can be backed by SharedPreferences or memory (tests). */
interface KeyValueStore {
    fun getString(key: String): String?
    fun putString(key: String, value: String)
}

data class LessonProgress(
    val lessonId: String,
    /** Segment the user was last working on (0-based). */
    val segmentIndex: Int,
    /** Highest segment index reached; equals totalSegments once completed. */
    val furthestIndex: Int,
    val totalSegments: Int,
    val completed: Boolean,
    val updatedAt: Long
) {
    val percent: Int
        get() = when {
            completed -> 100
            totalSegments <= 0 -> 0
            else -> ((furthestIndex.toDouble() / totalSegments) * 100).roundToInt().coerceAtMost(100)
        }
}

/** Per-lesson study progress. Mirrors Web/src/domain/progress/progress-store.ts. */
class ProgressStore(
    private val store: KeyValueStore,
    private val now: () -> Long = { System.currentTimeMillis() }
) {
    private companion object {
        const val KEY = "dictalearn_progress_v1"
    }

    fun all(): Map<String, LessonProgress> {
        val raw = store.getString(KEY) ?: return emptyMap()
        return try {
            val root = JSONObject(raw)
            root.keys().asSequence().associateWith { id ->
                val o = root.getJSONObject(id)
                LessonProgress(
                    lessonId = id,
                    segmentIndex = o.optInt("segmentIndex"),
                    furthestIndex = o.optInt("furthestIndex"),
                    totalSegments = o.optInt("totalSegments"),
                    completed = o.optBoolean("completed"),
                    updatedAt = o.optLong("updatedAt")
                )
            }
        } catch (_: Exception) {
            emptyMap()
        }
    }

    fun get(lessonId: String): LessonProgress? = all()[lessonId]

    fun record(lessonId: String, segmentIndex: Int, totalSegments: Int) {
        val index = segmentIndex.coerceIn(0, (totalSegments - 1).coerceAtLeast(0))
        val prev = get(lessonId)
        write(
            LessonProgress(
                lessonId = lessonId,
                segmentIndex = index,
                furthestIndex = maxOf(index, prev?.furthestIndex ?: 0),
                totalSegments = totalSegments,
                completed = prev?.completed ?: false,
                updatedAt = now()
            )
        )
    }

    fun markCompleted(lessonId: String, totalSegments: Int) {
        write(LessonProgress(lessonId, 0, totalSegments, totalSegments, completed = true, updatedAt = now()))
    }

    private fun write(p: LessonProgress) {
        val all = all().toMutableMap()
        all[p.lessonId] = p
        val root = JSONObject()
        for ((id, v) in all) {
            root.put(
                id,
                JSONObject()
                    .put("segmentIndex", v.segmentIndex)
                    .put("furthestIndex", v.furthestIndex)
                    .put("totalSegments", v.totalSegments)
                    .put("completed", v.completed)
                    .put("updatedAt", v.updatedAt)
            )
        }
        store.putString(KEY, root.toString())
    }
}
