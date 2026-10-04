package com.dictalearn.app.domain

import com.dictalearn.app.domain.progress.DailyStats
import com.dictalearn.app.domain.progress.KeyValueStore
import org.junit.Assert.*
import org.junit.Test
import java.time.LocalDate

class DailyStatsTest {

    private class MemoryStore : KeyValueStore {
        val data = mutableMapOf<String, String>()
        override fun getString(key: String): String? = data[key]
        override fun putString(key: String, value: String) {
            data[key] = value
        }
    }

    @Test
    fun countsPerDay_streak_andGoal() {
        var today = LocalDate.of(2026, 10, 1)
        val kv = MemoryStore()
        val stats = DailyStats(kv) { today }
        assertEquals(20, stats.goal())
        stats.setGoal(10)
        stats.setGoal(7) // ignored
        assertEquals(10, stats.goal())

        repeat(3) { day ->
            today = LocalDate.of(2026, 10, 1 + day)
            repeat(10) { stats.addSentence() }
        }
        today = LocalDate.of(2026, 10, 4)
        stats.addSentence()
        assertEquals(1, stats.todayCount())
        assertEquals(3, stats.streak()) // unfinished today does not break it
        repeat(9) { stats.addSentence() }
        assertEquals(4, stats.streak())

        val week = stats.lastDays(7)
        assertEquals(7, week.size)
        assertEquals(LocalDate.of(2026, 10, 4) to 10, week.last())

        today = LocalDate.of(2026, 10, 6)
        assertEquals(0, stats.streak())
        assertEquals(10, DailyStats(kv) { today }.goal())
    }
}
