// "Hard sentences": segments answered below 70% accuracy, kept per lesson for a short review round.
import type { KeyValueStorage } from '../progress/progress-store'
import type { Lesson } from '../lessons/types'

export const HARD_THRESHOLD = 0.7
const STORAGE_KEY = 'dictalearn_hard_sentences_v1'
export const HARD_SUFFIX = '::hard'

export class HardSentenceStore {
  private readonly storage: KeyValueStorage | null

  constructor(storage: KeyValueStorage | null) {
    this.storage = storage
  }

  private read(): Record<string, number[]> {
    if (!this.storage) return {}
    try {
      const raw = this.storage.getItem(STORAGE_KEY)
      const parsed: unknown = raw ? JSON.parse(raw) : {}
      return parsed && typeof parsed === 'object' ? (parsed as Record<string, number[]>) : {}
    } catch {
      return {}
    }
  }

  private write(all: Record<string, number[]>): void {
    try {
      this.storage?.setItem(STORAGE_KEY, JSON.stringify(all))
    } catch {
      // best-effort
    }
  }

  /** Below the threshold the segment becomes hard; a good later result removes it. */
  record(lessonId: string, segmentId: number, accuracy: number): void {
    const all = this.read()
    const ids = new Set(all[lessonId] ?? [])
    if (accuracy < HARD_THRESHOLD) ids.add(segmentId)
    else ids.delete(segmentId)
    if (ids.size) all[lessonId] = [...ids].sort((a, b) => a - b)
    else delete all[lessonId]
    this.write(all)
  }

  list(lessonId: string): number[] {
    return this.read()[lessonId] ?? []
  }

  count(lessonId: string): number {
    return this.list(lessonId).length
  }
}

/** The same lesson restricted to the hard segments (audio ranges unchanged). */
export function hardSubLesson(lesson: Lesson, segmentIds: number[]): Lesson {
  const wanted = new Set(segmentIds)
  return {
    ...lesson,
    lesson_id: `${lesson.lesson_id}${HARD_SUFFIX}`,
    segments: lesson.segments.filter((s) => wanted.has(s.id)),
  }
}
