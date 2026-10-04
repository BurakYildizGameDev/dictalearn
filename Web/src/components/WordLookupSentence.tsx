import React, { useEffect, useState } from 'react'
import { useDictionary, googleTranslateUrl } from '../hooks/use-dictionary'
import { BookmarkPlus, Check, ExternalLink, Volume2, X } from 'lucide-react'
import type { DictionaryEntry } from '../domain/dictionary/dictionary'
import { normalizeLookupWord } from '../domain/dictionary/dictionary'
import type { MistakeRepository } from '../domain/mistakes/types'
import { pronounce } from '../audio/word-audio'
import { cx } from './cx'


const nowIso = () => new Date().toISOString()

export interface WordLookupSentenceProps {
  text: string
  className?: string
  lessonId: string
  segmentId: number
  mistakeRepository?: MistakeRepository
  /** Accessible label for the sentence region. */
  label?: string
}

/**
 * Renders a revealed sentence with every word clickable. Clicking opens a word card with the
 * Turkish meaning (offline dictionary), pronunciation and "add to notebook" (Faz 7.2 / 7.4).
 * Only used after the answer was submitted, so the copy-protection rule still holds.
 */
export const WordLookupSentence: React.FC<WordLookupSentenceProps> = ({
  text,
  className,
  lessonId,
  segmentId,
  mistakeRepository,
  label = 'Orijinal cümle',
}) => {
  const dictionary = useDictionary()
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null)
  const [saved, setSaved] = useState<Set<string>>(() => new Set())
  const words = text.split(/\s+/).filter(Boolean)
  // Computed on render so the card fills in once the dictionary finishes loading.
  const selection =
    selectedIndex === null
      ? null
      : {
          index: selectedIndex,
          word: words[selectedIndex],
          entry: (dictionary?.lookupInSentence(words, selectedIndex) ?? null) as DictionaryEntry | null,
        }

  const isOpen = selectedIndex !== null
  useEffect(() => {
    if (!isOpen) return
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setSelectedIndex(null)
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [isOpen])

  const open = (index: number) => {
    if (!normalizeLookupWord(words[index])) return
    setSelectedIndex((current) => (current === index ? null : index))
  }

  const headword = selection ? (selection.entry?.headword ?? normalizeLookupWord(selection.word)) : ''

  const addToNotebook = () => {
    if (!selection || !mistakeRepository || saved.has(headword)) return
    mistakeRepository.addMistakes([
      { word: headword, kind: 'unknown', lesson_id: lessonId, segment_id: segmentId, at: nowIso() },
    ])
    setSaved((prev) => new Set(prev).add(headword))
  }

  return (
    <div>
      <p aria-label={label} className={cx('select-text', className)}>
        {words.map((w, i) => (
          <React.Fragment key={i}>
            {i > 0 && ' '}
            <button
              type="button"
              onClick={() => open(i)}
              aria-expanded={selection?.index === i}
              className={cx(
                'cursor-pointer rounded decoration-dotted underline-offset-[6px] transition-colors hover:text-indigo-200 hover:underline',
                selection?.index === i && 'bg-indigo-400/15 text-indigo-100 underline'
              )}
            >
              {w}
            </button>
          </React.Fragment>
        ))}
      </p>

      {selection && (
        <div
          role="dialog"
          aria-label={`Kelime kartı: ${headword}`}
          className="mt-4 rounded-xl border border-white/10 bg-zinc-950/80 p-4 animate-fade-up"
        >
          <div className="flex items-start justify-between gap-3">
            <div className="min-w-0">
              <p className="font-serif text-xl text-zinc-50">{headword}</p>
              {selection.entry ? (
                <p className="mt-1 text-sm text-zinc-300">{selection.entry.meaning}</p>
              ) : (
                <p className="mt-1 text-sm text-zinc-500">
                  {dictionary ? 'Çevrimdışı sözlükte bulunamadı.' : 'Sözlük yükleniyor…'}
                </p>
              )}
            </div>
            <button
              type="button"
              onClick={() => setSelectedIndex(null)}
              aria-label="Kelime kartını kapat"
              className="rounded-md p-1 text-zinc-500 hover:bg-white/5 hover:text-zinc-200 cursor-pointer"
            >
              <X className="h-4 w-4" />
            </button>
          </div>
          <div className="mt-3 flex flex-wrap gap-2">
            <button
              type="button"
              onClick={() => void pronounce(headword)}
              className="inline-flex h-8 items-center gap-1.5 rounded-lg bg-white/5 px-3 text-xs text-zinc-200 hover:bg-white/10 cursor-pointer"
            >
              <Volume2 className="h-3.5 w-3.5" /> Telaffuz
            </button>
            {mistakeRepository && (
              <button
                type="button"
                onClick={addToNotebook}
                disabled={saved.has(headword)}
                className="inline-flex h-8 items-center gap-1.5 rounded-lg bg-white/5 px-3 text-xs text-zinc-200 hover:bg-white/10 disabled:text-emerald-300 cursor-pointer"
              >
                {saved.has(headword) ? (
                  <>
                    <Check className="h-3.5 w-3.5" /> Defterde
                  </>
                ) : (
                  <>
                    <BookmarkPlus className="h-3.5 w-3.5" /> Bilmiyorum, deftere ekle
                  </>
                )}
              </button>
            )}
            <a
              href={googleTranslateUrl(selection.entry ? headword : text)}
              target="_blank"
              rel="noreferrer"
              className="inline-flex h-8 items-center gap-1.5 rounded-lg px-3 text-xs text-zinc-400 hover:bg-white/5 hover:text-zinc-200"
              title="Çevrimiçi çeviri (yeni sekme)"
            >
              <ExternalLink className="h-3.5 w-3.5" /> {selection.entry ? 'Daha fazla anlam' : 'Cümleyi çevir'}
            </a>
          </div>
        </div>
      )}
    </div>
  )
}
