package com.dictalearn.app.domain.progress

import org.json.JSONObject
import java.time.LocalDate

/** Daily goal and streak (sentences per local day). Mirrors Web/src/domain/progress/daily-stats.ts. */
class DailyStats(
    private val store: KeyValueStore,
    private val today: () -> LocalDate = { LocalDate.now() }
) {
    companion object {
        val GOAL_OPTIONS = listOf(10, 20, 40)
        private const val DEFAULT_GOAL = 20
        private const val KEY = "dictalearn_daily_v1"
        private const val KEEP_DAYS = 400L
    }

    private data class Data(val goal: Int, val days: MutableMap<LocalDate, Int>)

    private fun read(): Data = runCatching {
        val o = JSONObject(store.getString(KEY) ?: return Data(DEFAULT_GOAL, mutableMapOf()))
        val daysObj = o.optJSONObject("days") ?: JSONObject()
        val days = daysObj.keys().asSequence().associate { LocalDate.parse(it) to daysObj.getInt(it) }.toMutableMap()
        Data(o.optInt("goal", DEFAULT_GOAL), days)
    }.getOrDefault(Data(DEFAULT_GOAL, mutableMapOf()))

    private fun write(data: Data) {
        val cutoff = today().minusDays(KEEP_DAYS)
        val days = JSONObject()
        data.days.filterKeys { !it.isBefore(cutoff) }.forEach { (d, n) -> days.put(d.toString(), n) }
        store.putString(KEY, JSONObject().put("goal", data.goal).put("days", days).toString())
    }

    fun goal(): Int = read().goal

    fun setGoal(goal: Int) {
        if (goal !in GOAL_OPTIONS) return
        write(read().copy(goal = goal))
    }

    fun addSentence() {
        val data = read()
        val d = today()
        data.days[d] = (data.days[d] ?: 0) + 1
        write(data)
    }

    fun todayCount(): Int = read().days[today()] ?: 0

    /** Consecutive days that reached the goal; today only counts once reached. */
    fun streak(): Int {
        val data = read()
        var day = today()
        if ((data.days[day] ?: 0) < data.goal) day = day.minusDays(1)
        var streak = 0
        while ((data.days[day] ?: 0) >= data.goal) {
            streak++
            day = day.minusDays(1)
        }
        return streak
    }

    fun lastDays(n: Int): List<Pair<LocalDate, Int>> {
        val days = read().days
        val now = today()
        return (n - 1 downTo 0).map { back -> now.minusDays(back.toLong()).let { it to (days[it] ?: 0) } }
    }
}
