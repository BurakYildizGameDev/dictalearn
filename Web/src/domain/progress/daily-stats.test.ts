import { describe, it, expect, beforeEach } from 'vitest'
import { DailyStats, GOAL_OPTIONS } from './daily-stats'
import type { KeyValueStorage } from './progress-store'

class MemoryStorage implements KeyValueStorage {
  data = new Map<string, string>()
  getItem(k: string) {
    return this.data.get(k) ?? null
  }
  setItem(k: string, v: string) {
    this.data.set(k, v)
  }
  removeItem(k: string) {
    this.data.delete(k)
  }
}

describe('DailyStats', () => {
  let storage: MemoryStorage
  let today: string
  let stats: DailyStats

  beforeEach(() => {
    storage = new MemoryStorage()
    today = '2026-10-04'
    stats = new DailyStats(storage, () => today)
  })

  it('counts sentences per day against a goal (default 20)', () => {
    expect(stats.goal()).toBe(20)
    expect(GOAL_OPTIONS).toEqual([10, 20, 40])
    stats.addSentence()
    stats.addSentence()
    expect(stats.todayCount()).toBe(2)
    today = '2026-10-05'
    expect(stats.todayCount()).toBe(0)
  })

  it('streak counts consecutive days that reached the goal; an unfinished today does not break it', () => {
    stats.setGoal(10)
    for (const day of ['2026-10-01', '2026-10-02', '2026-10-03']) {
      today = day
      for (let i = 0; i < 10; i++) stats.addSentence()
    }
    today = '2026-10-04'
    stats.addSentence() // 1 / 10 today
    expect(stats.streak()).toBe(3)
    for (let i = 0; i < 9; i++) stats.addSentence()
    expect(stats.streak()).toBe(4)
    today = '2026-10-06' // a whole day skipped
    expect(stats.streak()).toBe(0)
  })

  it('persists goal and counts, and ignores invalid goals', () => {
    stats.setGoal(40)
    stats.addSentence()
    stats.setGoal(7)
    const again = new DailyStats(storage, () => today)
    expect(again.goal()).toBe(40)
    expect(again.todayCount()).toBe(1)
  })

  it('reports the last 7 days for a small chart', () => {
    today = '2026-10-03'
    stats.addSentence()
    today = '2026-10-04'
    stats.addSentence()
    stats.addSentence()
    const week = stats.lastDays(7)
    expect(week).toHaveLength(7)
    expect(week[6]).toEqual({ date: '2026-10-04', count: 2 })
    expect(week[5]).toEqual({ date: '2026-10-03', count: 1 })
    expect(week[0].date).toBe('2026-09-28')
  })
})
