import React, { useEffect, useMemo, useRef, useState } from 'react'
import { ArrowLeft, Check, HelpCircle, RotateCcw, Trophy, Volume2, X } from 'lucide-react'
import type { SrsCard, SrsStore } from '../domain/review/srs'
import { checkWordMatch } from '../domain/words/word-mode'
import { useDictionary } from '../hooks/use-dictionary'
import { pronounce } from '../audio/word-audio'
import { Button, Kbd, ProgressBar } from './ui'
import { cx } from './cx'

interface ReviewViewProps {
  srs: SrsStore
  onDone: () => void
}

type Feedback = null | { correct: boolean }

/**
 * Spaced-repetition review of the mistake notebook: hear the word (studio voice), see its Turkish
 * meaning, type it. The first answer of each card moves it between Leitner boxes; missed cards come
 * back once more at the end of the session for practice.
 */
export const ReviewView: React.FC<ReviewViewProps> = ({ srs, onDone }) => {
  const dictionary = useDictionary()
  const [queue, setQueue] = useState<SrsCard[]>(() => srs.dueCards())
  const [total] = useState(() => queue.length)
  const [position, setPosition] = useState(0)
  const [typed, setTyped] = useState('')
  const [feedback, setFeedback] = useState<Feedback>(null)
  const [results, setResults] = useState<Record<string, boolean>>({})
  const inputRef = useRef<HTMLInputElement>(null)
  const nextRef = useRef<HTMLButtonElement>(null)

  const card = queue[position]
  const meaning = useMemo(() => (card ? dictionary?.lookup(card.word)?.meaning ?? null : null), [card, dictionary])

  useEffect(() => {
    if (!card) return
    void pronounce(card.word)
    const t = setTimeout(() => inputRef.current?.focus(), 30)
    return () => clearTimeout(t)
  }, [card])

  useEffect(() => {
    if (feedback) nextRef.current?.focus()
  }, [feedback])

  const submit = (gaveUp = false) => {
    if (!card || feedback) return
    if (!gaveUp && !typed.trim()) return
    const correct = !gaveUp && checkWordMatch(typed, card.word)
    setFeedback({ correct })
    if (!(card.word in results)) {
      srs.answer(card.word, correct) // only the first answer in a session counts
      setResults((r) => ({ ...r, [card.word]: correct }))
      if (!correct) setQueue((q) => [...q, card]) // practise once more at the end
    }
    if (!correct) void pronounce(card.word)
  }

  const next = () => {
    setFeedback(null)
    setTyped('')
    setPosition((p) => p + 1)
  }

  if (total === 0) {
    return (
      <div className="mx-auto max-w-md px-4 py-20 text-center">
        <Check className="mx-auto mb-3 h-8 w-8 text-emerald-300" />
        <h1 className="font-serif text-2xl text-zinc-50">Bugün tekrar edilecek kelime yok</h1>
        <p className="mt-2 text-sm text-zinc-400">Yeni kelimeler dikte yaptıkça defterine eklenir.</p>
        <Button className="mt-6" onClick={onDone}>
          <ArrowLeft className="h-4 w-4" /> Defterime dön
        </Button>
      </div>
    )
  }

  if (!card) {
    const correct = Object.values(results).filter(Boolean).length
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center animate-fade-up">
        <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-amber-400/10 text-amber-300">
          <Trophy className="h-7 w-7" />
        </div>
        <h1 className="font-serif text-3xl text-zinc-50">Tekrar tamamlandı</h1>
        <p className="mt-2 text-sm text-zinc-400">
          {total} kelimenin {correct} tanesini ilk denemede bildin. Bildiklerin daha seyrek, bilemediklerin yarın tekrar sorulacak.
        </p>
        <Button variant="primary" size="lg" className="mt-8" onClick={onDone}>
          <ArrowLeft className="h-4 w-4" /> Defterime dön
        </Button>
      </div>
    )
  }

  const answered = Object.keys(results).length
  return (
    <div className="mx-auto w-full max-w-xl px-4 pb-16 pt-8 sm:pt-12">
      <div className="mb-3 flex items-center justify-between text-xs text-zinc-500">
        <span>Kelime tekrarı</span>
        <span className="tabular-nums">
          {Math.min(answered + (feedback ? 0 : 1), total)} / {total}
          {position >= total && ' · ek tekrar'}
        </span>
      </div>
      <ProgressBar value={(answered / total) * 100} label="Tekrar ilerlemesi" />

      <div className="mt-6 rounded-2xl border border-white/[0.08] bg-zinc-900/60 p-6 animate-fade-up" key={`${card.word}-${position}`}>
        <div className="flex items-center justify-between gap-3">
          <Button variant="secondary" onClick={() => void pronounce(card.word)} title="Kelimeyi tekrar dinle">
            <Volume2 className="h-4 w-4" /> Dinle
          </Button>
          <span className="text-[11px] text-zinc-500">Kutu {card.box + 1} / 6</span>
        </div>

        <p className="mt-5 text-sm text-zinc-400">Türkçesi:</p>
        <p className="font-serif text-2xl text-zinc-100">
          {meaning ?? `${card.word.charAt(0).toUpperCase()}${'·'.repeat(Math.max(0, card.word.length - 1))}`}
        </p>

        <label htmlFor="review-input" className="mt-5 block text-xs text-zinc-500">
          Duyduğun İngilizce kelimeyi yaz
        </label>
        <input
          id="review-input"
          ref={inputRef}
          value={typed}
          onChange={(e) => setTyped(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter') {
              e.preventDefault()
              if (feedback) next()
              else submit()
            }
          }}
          readOnly={!!feedback}
          autoComplete="off"
          autoCorrect="off"
          autoCapitalize="none"
          spellCheck={false}
          placeholder="Kelimeyi yaz…"
          className={cx(
            'mt-1.5 h-14 w-full rounded-xl border bg-black/30 px-4 font-serif text-2xl text-zinc-50 placeholder:font-sans placeholder:text-base placeholder:text-zinc-600 focus:outline-none',
            feedback?.correct === true && 'border-emerald-400/60',
            feedback?.correct === false && 'border-rose-400/60',
            !feedback && 'border-white/10 focus:border-indigo-400/60'
          )}
        />

        {feedback && (
          <div
            role="status"
            className={cx(
              'mt-4 flex items-center gap-2 rounded-xl px-4 py-3 text-sm',
              feedback.correct ? 'bg-emerald-500/10 text-emerald-200' : 'bg-rose-500/10 text-rose-200'
            )}
          >
            {feedback.correct ? <Check className="h-4 w-4" /> : <X className="h-4 w-4" />}
            {feedback.correct ? 'Doğru!' : 'Doğrusu:'}
            <strong className="font-serif text-lg">{card.word}</strong>
          </div>
        )}

        <div className="mt-5 flex items-center justify-between gap-2">
          {!feedback ? (
            <>
              <Button variant="ghost" onClick={() => submit(true)}>
                <HelpCircle className="h-4 w-4" /> Bilmiyorum
              </Button>
              <Button variant="primary" onClick={() => submit()} disabled={!typed.trim()}>
                <Check className="h-4 w-4" /> Kontrol Et <Kbd className="border-white/20 bg-white/10 text-indigo-100">Enter</Kbd>
              </Button>
            </>
          ) : (
            <>
              <span className="text-xs text-zinc-500">
                {feedback.correct ? 'Bir sonraki tekrar daha ileri bir tarihte.' : 'Bu kelime yarın tekrar gelecek.'}
              </span>
              <Button ref={nextRef} variant="primary" onClick={next}>
                <RotateCcw className="h-4 w-4 rotate-180" /> Devam <Kbd className="border-white/20 bg-white/10 text-indigo-100">Enter</Kbd>
              </Button>
            </>
          )}
        </div>
      </div>
    </div>
  )
}
