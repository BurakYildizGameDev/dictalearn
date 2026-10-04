// Per-lesson study progress, persisted in a key-value store (localStorage in the browser).

export interface KeyValueStorage {
  getItem(key: string): string | null
  setItem(key: string, value: string): void
  removeItem(key: string): void
}

export interface LessonProgress {
  lessonId: string
  /** Segment the user was last working on (0-based). */
  segmentIndex: number
  /** Highest segment index ever reached; equals totalSegments once completed. */
  furthestIndex: number
  totalSegments: number
  completed: boolean
  updatedAt: string
}

const STORAGE_KEY = 'dictalearn_progress_v1'

export class ProgressStore {
  private readonly storage: KeyValueStorage | null
  private readonly now: () => string

  constructor(storage: KeyValueStorage | null, now: () => string = () => new Date().toISOString()) {
    this.storage = storage
    this.now = now
  }

  all(): Record<string, LessonProgress> {
    if (!this.storage) return {}
    try {
      const raw = this.storage.getItem(STORAGE_KEY)
      if (!raw) return {}
      const parsed: unknown = JSON.parse(raw)
      return parsed && typeof parsed === 'object' ? (parsed as Record<string, LessonProgress>) : {}
    } catch {
      return {}
    }
  }

  get(lessonId: string): LessonProgress | null {
    return this.all()[lessonId] ?? null
  }

  record(lessonId: string, segmentIndex: number, totalSegments: number): void {
    const index = Math.min(Math.max(0, Math.floor(segmentIndex)), Math.max(0, totalSegments - 1))
    const prev = this.get(lessonId)
    this.write(lessonId, {
      lessonId,
      segmentIndex: index,
      furthestIndex: Math.max(index, prev?.furthestIndex ?? 0),
      totalSegments,
      completed: prev?.completed ?? false,
      updatedAt: this.now(),
    })
  }

  markCompleted(lessonId: string, totalSegments: number): void {
    this.write(lessonId, {
      lessonId,
      segmentIndex: 0,
      furthestIndex: totalSegments,
      totalSegments,
      completed: true,
      updatedAt: this.now(),
    })
  }

  reset(lessonId: string): void {
    const all = this.all()
    delete all[lessonId]
    this.persist(all)
  }

  private write(lessonId: string, progress: LessonProgress): void {
    const all = this.all()
    all[lessonId] = progress
    this.persist(all)
  }

  private persist(all: Record<string, LessonProgress>): void {
    if (!this.storage) return
    try {
      this.storage.setItem(STORAGE_KEY, JSON.stringify(all))
    } catch {
      // Quota exceeded or storage disabled: progress is best-effort.
    }
  }
}

export function progressPercent(progress: LessonProgress | null): number {
  if (!progress || progress.totalSegments <= 0) return 0
  if (progress.completed) return 100
  return Math.min(100, Math.round((progress.furthestIndex / progress.totalSegments) * 100))
}
