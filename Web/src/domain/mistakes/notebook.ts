import type { MistakeRecord } from './types'

export interface NotebookRow {
  word: string
  count: number
  unknown: boolean
  lastAt: string
  lessons: string[]
}

/** Groups mistake records per word, most frequent first. */
export function groupNotebook(records: MistakeRecord[]): NotebookRow[] {
  const map = new Map<string, NotebookRow>()
  for (const r of records) {
    const word = r.word.trim().toLowerCase()
    if (!word) continue
    const row = map.get(word) ?? { word, count: 0, unknown: false, lastAt: '', lessons: [] }
    row.count += 1
    row.unknown ||= r.kind === 'unknown'
    if (r.at > row.lastAt) row.lastAt = r.at
    if (!row.lessons.includes(r.lesson_id)) row.lessons.push(r.lesson_id)
    map.set(word, row)
  }
  return [...map.values()].sort((a, b) => b.count - a.count || b.lastAt.localeCompare(a.lastAt))
}
