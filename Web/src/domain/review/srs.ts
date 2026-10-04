// Spaced repetition (Leitner boxes) for the mistake notebook.
import type { MistakeRecord } from '../mistakes/types'
import type { KeyValueStorage } from '../progress/progress-store'

export type { KeyValueStorage }

/** Days until the next review for each box: today, 1, 3, 7, 14, 30. */
export const INTERVAL_DAYS = [0, 1, 3, 7, 14, 30] as const
/** Boxes from here on count as "learned". */
const LEARNED_BOX = 4
const STORAGE_KEY = 'dictalearn_srs_v1'

export interface SrsCard {
  word: string
  box: number
  /** Local date (YYYY-MM-DD) when the card is due. */
  due: string
  /** Local date of the last review, or '' if never reviewed. */
  lastReviewed: string
  lapses: number
}

export function localDate(d: Date = new Date()): string {
  const pad = (n: number) => String(n).padStart(2, '0')
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`
}

export function addDays(date: string, days: number): string {
  const [y, m, d] = date.split('-').map(Number)
  return localDate(new Date(y, m - 1, d + days))
}

export class SrsStore {
  private readonly storage: KeyValueStorage | null
  private readonly today: () => string

  constructor(storage: KeyValueStorage | null, today: () => string = () => localDate()) {
    this.storage = storage
    this.today = today
  }

  private read(): Record<string, SrsCard> {
    if (!this.storage) return {}
    try {
      const raw = this.storage.getItem(STORAGE_KEY)
      const parsed: unknown = raw ? JSON.parse(raw) : {}
      return parsed && typeof parsed === 'object' ? (parsed as Record<string, SrsCard>) : {}
    } catch {
      return {}
    }
  }

  private write(cards: Record<string, SrsCard>): void {
    try {
      this.storage?.setItem(STORAGE_KEY, JSON.stringify(cards))
    } catch {
      // storage full / unavailable: reviews are best-effort
    }
  }

  get(word: string): SrsCard | null {
    return this.read()[word.toLowerCase()] ?? null
  }

  /**
   * Keeps one card per notebook word. New words start in box 0 (due today); a word missed again
   * in dictation after its last review goes back to box 0. Words no longer in the notebook drop out.
   */
  sync(mistakes: MistakeRecord[]): void {
    const cards = this.read()
    const latest = new Map<string, string>()
    for (const m of mistakes) {
      const word = m.word.trim().toLowerCase()
      if (!word) continue
      const day = localDate(new Date(m.at))
      if ((latest.get(word) ?? '') < day) latest.set(word, day)
    }
    const next: Record<string, SrsCard> = {}
    for (const [word, lastMissed] of latest) {
      const card = cards[word]
      if (!card) {
        next[word] = { word, box: 0, due: this.today(), lastReviewed: '', lapses: 0 }
      } else if (card.lastReviewed && lastMissed > card.lastReviewed) {
        next[word] = { ...card, box: 0, due: this.today(), lapses: card.lapses + 1 }
      } else {
        next[word] = card
      }
    }
    this.write(next)
  }

  dueCards(): SrsCard[] {
    const today = this.today()
    return Object.values(this.read())
      .filter((c) => c.due <= today)
      .sort((a, b) => a.due.localeCompare(b.due) || a.box - b.box || a.word.localeCompare(b.word))
  }

  answer(word: string, correct: boolean): void {
    const cards = this.read()
    const key = word.toLowerCase()
    const card = cards[key]
    if (!card) return
    const today = this.today()
    const box = correct ? Math.min(card.box + 1, INTERVAL_DAYS.length - 1) : 0
    cards[key] = {
      ...card,
      box,
      // A missed word is practised again at the end of the session, then asked tomorrow.
      due: addDays(today, correct ? INTERVAL_DAYS[box] : 1),
      lastReviewed: today,
      lapses: correct ? card.lapses : card.lapses + 1,
    }
    this.write(cards)
  }

  stats(): { total: number; due: number; learned: number } {
    const all = Object.values(this.read())
    return {
      total: all.length,
      due: this.dueCards().length,
      learned: all.filter((c) => c.box >= LEARNED_BOX).length,
    }
  }
}
