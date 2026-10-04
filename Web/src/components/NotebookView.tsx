import React, { useMemo, useState } from 'react'
import { BookMarked, Trash2, Volume2 } from 'lucide-react'
import type { MistakeRepository } from '../domain/mistakes/types'
import { groupNotebook } from '../domain/mistakes/notebook'
import { findBook } from '../domain/library/catalog'
import { useDictionary } from '../hooks/use-dictionary'
import { pronounce } from '../audio/word-audio'
import { Button, Segmented } from './ui'

type Filter = 'all' | 'mistakes' | 'unknown'

/** The mistake notebook (F3.3): words missed in dictation plus words marked as unknown. */
export const NotebookView: React.FC<{ mistakeRepository: MistakeRepository }> = ({ mistakeRepository }) => {
  const dictionary = useDictionary()
  const [version, setVersion] = useState(0)
  const [filter, setFilter] = useState<Filter>('all')

  const rows = useMemo(() => {
    void version // bumped after clearing to re-read the repository
    return groupNotebook(mistakeRepository.getMistakes())
  }, [mistakeRepository, version])
  const visible = rows.filter((r) => filter === 'all' || (filter === 'unknown' ? r.unknown : !r.unknown))

  const clearAll = () => {
    if (!window.confirm('Defterdeki tüm kelimeler silinsin mi?')) return
    mistakeRepository.clearMistakes()
    setVersion((v) => v + 1)
  }

  return (
    <div className="mx-auto w-full max-w-3xl px-4 pb-16 pt-8 sm:pt-12">
      <p className="text-[11px] font-semibold uppercase tracking-[0.18em] text-indigo-300/80">Defterim</p>
      <h1 className="mt-2 font-serif text-3xl text-zinc-50 sm:text-4xl">Tekrar edilecek kelimeler</h1>
      <p className="mt-2 text-sm text-zinc-400">
        Dikte sırasında kaçırdığın kelimeler ve kelime kartından “bilmiyorum” diye eklediklerin.
      </p>

      <div className="mt-6 flex flex-wrap items-center justify-between gap-3">
        <Segmented<Filter>
          ariaLabel="Defter filtresi"
          value={filter}
          onChange={setFilter}
          options={[
            { value: 'all', label: `Tümü (${rows.length})` },
            { value: 'mistakes', label: 'Hatalar' },
            { value: 'unknown', label: 'Bilmediklerim' },
          ]}
        />
        {rows.length > 0 && (
          <Button size="sm" variant="ghost" onClick={clearAll}>
            <Trash2 className="h-4 w-4" />
            Defteri temizle
          </Button>
        )}
      </div>

      {visible.length === 0 ? (
        <div className="mt-16 text-center text-sm text-zinc-500">
          <BookMarked className="mx-auto mb-3 h-8 w-8 text-zinc-700" />
          Henüz kelime yok. Dikte yaptıkça yanlış yazdığın kelimeler burada birikecek.
        </div>
      ) : (
        <ul className="mt-6 divide-y divide-white/[0.06] rounded-2xl border border-white/[0.08] bg-zinc-900/60">
          {visible.map((row) => {
            const entry = dictionary?.lookup(row.word)
            const book = findBook(row.lessons[0])
            return (
              <li key={row.word} className="flex items-center gap-3 px-4 py-3">
                <button
                  type="button"
                  onClick={() => void pronounce(row.word)}
                  aria-label={`${row.word} kelimesini dinle`}
                  className="rounded-lg p-1.5 text-zinc-500 hover:bg-white/5 hover:text-zinc-200 cursor-pointer"
                >
                  <Volume2 className="h-4 w-4" />
                </button>
                <div className="min-w-0 flex-1">
                  <p className="font-serif text-lg text-zinc-100">{row.word}</p>
                  <p className="truncate text-xs text-zinc-500">
                    {entry ? entry.meaning : dictionary ? 'Sözlükte yok' : '…'}
                    {book ? ` · ${book.title}` : ''}
                  </p>
                </div>
                {row.unknown && (
                  <span className="rounded-md bg-indigo-400/10 px-2 py-0.5 text-[10px] text-indigo-200">bilmiyorum</span>
                )}
                <span className="w-10 text-right text-xs tabular-nums text-rose-300/80">×{row.count}</span>
              </li>
            )
          })}
        </ul>
      )}
    </div>
  )
}
