import { describe, it, expect } from 'vitest'
import { notebookCsv, notebookAnkiTsv } from './export'
import type { NotebookRow } from './notebook'

const rows: NotebookRow[] = [
  { word: 'small', count: 3, unknown: false, lastAt: '2026-10-04', lessons: ['book_01'] },
  { word: 'drift apart', count: 1, unknown: true, lastAt: '2026-10-03', lessons: ['book_26'] },
  { word: 'quote', count: 1, unknown: false, lastAt: '2026-10-02', lessons: ['b'] },
]
const meanings: Record<string, string> = {
  small: 'küçük',
  'drift apart': 'zamanla birbirinden uzaklaşmak',
  quote: 'alıntı, "söz"; teklif',
}
const meaningOf = (w: string) => meanings[w]

describe('notebook export', () => {
  it('CSV has a BOM, a header and RFC 4180 quoting', () => {
    const csv = notebookCsv(rows, meaningOf)
    expect(csv.startsWith('﻿')).toBe(true)
    const lines = csv.slice(1).split('\r\n')
    expect(lines[0]).toBe('word,meaning,count,type')
    expect(lines[1]).toBe('small,küçük,3,hata')
    expect(lines[2]).toBe('drift apart,zamanla birbirinden uzaklaşmak,1,bilmiyorum')
    expect(lines[3]).toBe('quote,"alıntı, ""söz""; teklif",1,hata')
  })

  it('Anki TSV uses the tab-separated import header and skips words without meaning', () => {
    const tsv = notebookAnkiTsv([...rows, { word: 'zzz', count: 1, unknown: false, lastAt: '', lessons: [] }], meaningOf)
    const lines = tsv.split('\n')
    expect(lines[0]).toBe('#separator:tab')
    expect(lines[1]).toBe('#html:false')
    expect(lines[2]).toBe('small\tküçük')
    expect(lines).toHaveLength(6) // 2 header lines + 3 cards + trailing newline
    expect(tsv).not.toContain('zzz')
  })
})
