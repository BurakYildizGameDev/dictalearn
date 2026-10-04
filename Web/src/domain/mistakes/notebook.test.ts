import { describe, it, expect } from 'vitest'
import { groupNotebook } from './notebook'
import type { MistakeRecord } from './types'

const rec = (word: string, kind: MistakeRecord['kind'], at: string, lesson = 'book_01'): MistakeRecord => ({
  word,
  kind,
  at,
  lesson_id: lesson,
  segment_id: 1,
})

describe('groupNotebook', () => {
  it('groups case-insensitively, counts, and sorts by frequency then recency', () => {
    const rows = groupNotebook([
      rec('Small', 'substitute', '2026-10-01'),
      rec('small', 'missing', '2026-10-03', 'book_02'),
      rec('cold', 'unknown', '2026-10-04'),
      rec('  ', 'missing', '2026-10-04'),
      rec('hit', 'missing', '2026-10-02'),
    ])
    expect(rows.map((r) => r.word)).toEqual(['small', 'cold', 'hit'])
    expect(rows[0]).toMatchObject({ count: 2, unknown: false, lastAt: '2026-10-03', lessons: ['book_01', 'book_02'] })
    expect(rows[1].unknown).toBe(true)
  })
})
