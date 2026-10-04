// Daily goal and streak: sentences practised per local day.
import type { KeyValueStorage } from './progress-store'
import { addDays, localDate } from '../review/srs'

export const GOAL_OPTIONS = [10, 20, 40] as const
const DEFAULT_GOAL = 20
const STORAGE_KEY = 'dictalearn_daily_v1'
const KEEP_DAYS = 400

interface DailyData {
  goal: number
  days: Record<string, number>
}

export class DailyStats {
  private readonly storage: KeyValueStorage | null
  private readonly today: () => string

  constructor(storage: KeyValueStorage | null, today: () => string = () => localDate()) {
    this.storage = storage
    this.today = today
  }

  private read(): DailyData {
    try {
      const raw = this.storage?.getItem(STORAGE_KEY)
      const parsed = raw ? (JSON.parse(raw) as Partial<DailyData>) : {}
      return { goal: parsed.goal ?? DEFAULT_GOAL, days: parsed.days ?? {} }
    } catch {
      return { goal: DEFAULT_GOAL, days: {} }
    }
  }

  private write(data: DailyData): void {
    // Keep the file small: drop days older than ~a year.
    const cutoff = addDays(this.today(), -KEEP_DAYS)
    const days = Object.fromEntries(Object.entries(data.days).filter(([d]) => d >= cutoff))
    try {
      this.storage?.setItem(STORAGE_KEY, JSON.stringify({ goal: data.goal, days }))
    } catch {
      // best-effort
    }
  }

  goal(): number {
    return this.read().goal
  }

  setGoal(goal: number): void {
    if (!(GOAL_OPTIONS as readonly number[]).includes(goal)) return
    this.write({ ...this.read(), goal })
  }

  addSentence(): void {
    const data = this.read()
    const day = this.today()
    data.days[day] = (data.days[day] ?? 0) + 1
    this.write(data)
  }

  todayCount(): number {
    return this.read().days[this.today()] ?? 0
  }

  /** Consecutive days that reached the goal; today only counts once reached (it never breaks the streak). */
  streak(): number {
    const { goal, days } = this.read()
    let day = this.today()
    if ((days[day] ?? 0) < goal) day = addDays(day, -1)
    let streak = 0
    while ((days[day] ?? 0) >= goal) {
      streak++
      day = addDays(day, -1)
    }
    return streak
  }

  lastDays(n: number): Array<{ date: string; count: number }> {
    const { days } = this.read()
    const today = this.today()
    return Array.from({ length: n }, (_, i) => {
      const date = addDays(today, i - (n - 1))
      return { date, count: days[date] ?? 0 }
    })
  }
}
