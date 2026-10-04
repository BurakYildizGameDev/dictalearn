// Export of the mistake notebook: CSV (spreadsheets) and Anki's tab-separated import format.
import type { NotebookRow } from './notebook'

function csvField(value: string): string {
  return /[",\r\n]/.test(value) ? `"${value.replace(/"/g, '""')}"` : value
}

/** UTF-8 BOM so Excel opens Turkish characters correctly; CRLF line endings per RFC 4180. */
export function notebookCsv(rows: NotebookRow[], meaningOf: (word: string) => string | undefined): string {
  const lines = [['word', 'meaning', 'count', 'type']]
  for (const r of rows) {
    lines.push([r.word, meaningOf(r.word) ?? '', String(r.count), r.unknown ? 'bilmiyorum' : 'hata'])
  }
  return '﻿' + lines.map((l) => l.map(csvField).join(',')).join('\r\n')
}

/** Anki 2.1.54+ reads the "#separator" / "#html" headers; front = English, back = Turkish. */
export function notebookAnkiTsv(rows: NotebookRow[], meaningOf: (word: string) => string | undefined): string {
  const clean = (s: string) => s.replace(/[\t\r\n]+/g, ' ').trim()
  const cards = rows
    .map((r) => [r.word, meaningOf(r.word)] as const)
    .filter(([, meaning]) => !!meaning)
    .map(([word, meaning]) => `${clean(word)}\t${clean(meaning!)}`)
  return ['#separator:tab', '#html:false', ...cards].join('\n') + '\n'
}
