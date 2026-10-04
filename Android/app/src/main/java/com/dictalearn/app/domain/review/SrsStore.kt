package com.dictalearn.app.domain.review

import com.dictalearn.app.domain.mistakes.MistakeRecord
import com.dictalearn.app.domain.progress.KeyValueStore
import org.json.JSONObject
import java.time.Instant
import java.time.LocalDate
import java.time.ZoneId

data class SrsCard(
    val word: String,
    val box: Int,
    val due: LocalDate,
    /** Null when never reviewed. */
    val lastReviewed: LocalDate?,
    val lapses: Int
)

/** Spaced repetition (Leitner boxes) for the mistake notebook. Mirrors Web/src/domain/review/srs.ts. */
class SrsStore(
    private val store: KeyValueStore,
    private val today: () -> LocalDate = { LocalDate.now() }
) {
    data class Stats(val total: Int, val due: Int, val learned: Int)

    companion object {
        /** Days until the next review per box: today, 1, 3, 7, 14, 30. */
        val INTERVAL_DAYS = listOf(0, 1, 3, 7, 14, 30)
        private const val LEARNED_BOX = 4
        private const val KEY = "dictalearn_srs_v1"
    }

    private fun read(): MutableMap<String, SrsCard> = runCatching {
        val root = JSONObject(store.getString(KEY) ?: return mutableMapOf())
        root.keys().asSequence().associateWith { key ->
            val o = root.getJSONObject(key)
            SrsCard(
                word = key,
                box = o.getInt("box"),
                due = LocalDate.parse(o.getString("due")),
                lastReviewed = o.optString("lastReviewed").takeIf { it.isNotEmpty() }?.let(LocalDate::parse),
                lapses = o.optInt("lapses")
            )
        }.toMutableMap()
    }.getOrDefault(mutableMapOf())

    private fun write(cards: Map<String, SrsCard>) {
        val root = JSONObject()
        for ((key, c) in cards) {
            root.put(
                key,
                JSONObject()
                    .put("box", c.box)
                    .put("due", c.due.toString())
                    .put("lastReviewed", c.lastReviewed?.toString() ?: "")
                    .put("lapses", c.lapses)
            )
        }
        store.putString(KEY, root.toString())
    }

    fun get(word: String): SrsCard? = read()[word.lowercase()]

    /** One card per notebook word; a word missed again after its last review returns to box 0. */
    fun sync(mistakes: List<MistakeRecord>) {
        val cards = read()
        val latest = mutableMapOf<String, LocalDate>()
        for (m in mistakes) {
            val word = m.word.trim().lowercase()
            if (word.isEmpty()) continue
            val day = Instant.ofEpochMilli(m.timestamp).atZone(ZoneId.systemDefault()).toLocalDate()
            if (latest[word]?.isBefore(day) != false) latest[word] = day
        }
        val next = latest.mapValues { (word, lastMissed) ->
            val card = cards[word]
            when {
                card == null -> SrsCard(word, 0, today(), null, 0)
                card.lastReviewed != null && lastMissed.isAfter(card.lastReviewed) ->
                    card.copy(box = 0, due = today(), lapses = card.lapses + 1)
                else -> card
            }
        }
        write(next)
    }

    fun dueCards(): List<SrsCard> {
        val now = today()
        return read().values.filter { !it.due.isAfter(now) }.sortedWith(compareBy({ it.due }, { it.box }, { it.word }))
    }

    fun answer(word: String, correct: Boolean) {
        val cards = read()
        val card = cards[word.lowercase()] ?: return
        val now = today()
        val box = if (correct) minOf(card.box + 1, INTERVAL_DAYS.size - 1) else 0
        cards[card.word] = card.copy(
            box = box,
            // A missed word is practised again at the end of the session, then asked tomorrow.
            due = now.plusDays(if (correct) INTERVAL_DAYS[box].toLong() else 1L),
            lastReviewed = now,
            lapses = if (correct) card.lapses else card.lapses + 1
        )
        write(cards)
    }

    fun stats(): Stats {
        val all = read().values
        return Stats(total = all.size, due = dueCards().size, learned = all.count { it.box >= LEARNED_BOX })
    }
}
