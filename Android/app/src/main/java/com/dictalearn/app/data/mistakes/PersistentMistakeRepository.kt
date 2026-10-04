package com.dictalearn.app.data.mistakes

import com.dictalearn.app.domain.mistakes.MistakeKind
import com.dictalearn.app.domain.mistakes.MistakeRecord
import com.dictalearn.app.domain.mistakes.MistakeRepository
import com.dictalearn.app.domain.progress.KeyValueStore
import org.json.JSONArray
import org.json.JSONObject

/** Mistake notebook that survives app restarts (the in-memory one lost everything). */
class PersistentMistakeRepository(private val store: KeyValueStore) : MistakeRepository {
    private companion object {
        const val KEY = "dictalearn_mistakes_v1"
        const val MAX_RECORDS = 5000
    }

    private val cache: MutableList<MistakeRecord> by lazy { read().toMutableList() }

    private fun read(): List<MistakeRecord> {
        val raw = store.getString(KEY) ?: return emptyList()
        return try {
            val arr = JSONArray(raw)
            (0 until arr.length()).map { i ->
                val o = arr.getJSONObject(i)
                MistakeRecord(
                    word = o.getString("word"),
                    kind = runCatching { MistakeKind.valueOf(o.getString("kind")) }.getOrDefault(MistakeKind.UNKNOWN),
                    typed = if (o.has("typed")) o.getString("typed") else null,
                    lessonId = o.getString("lessonId"),
                    segmentId = o.getInt("segmentId"),
                    timestamp = o.optLong("timestamp")
                )
            }
        } catch (_: Exception) {
            emptyList()
        }
    }

    private fun persist() {
        val arr = JSONArray()
        cache.takeLast(MAX_RECORDS).forEach { m ->
            arr.put(
                JSONObject()
                    .put("word", m.word)
                    .put("kind", m.kind.name)
                    .apply { m.typed?.let { put("typed", it) } }
                    .put("lessonId", m.lessonId)
                    .put("segmentId", m.segmentId)
                    .put("timestamp", m.timestamp)
            )
        }
        store.putString(KEY, arr.toString())
    }

    override fun getMistakes(): List<MistakeRecord> = synchronized(this) { cache.toList() }

    override fun addMistakes(mistakes: List<MistakeRecord>) {
        if (mistakes.isEmpty()) return
        synchronized(this) {
            cache.addAll(mistakes)
            persist()
        }
    }

    override fun clearMistakes() {
        synchronized(this) {
            cache.clear()
            persist()
        }
    }

    override fun getWordFrequencies(): Map<String, Int> = synchronized(this) {
        cache.groupingBy { it.word.lowercase() }.eachCount()
    }
}
