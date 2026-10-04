import React from 'react'
import type { DiffResult, DiffWord } from '../domain/diff/types'
import { CheckCircle2, AlertCircle } from 'lucide-react'
import { cx } from './cx'

interface DiffViewProps {
  diff: DiffResult
  compact?: boolean
}

// Each kind differs by shape as well as color (strike-through, underline, dashed box)
// so the result stays readable for color-blind users.
const DiffToken: React.FC<{ word: DiffWord }> = ({ word }) => {
  switch (word.kind) {
    case 'equal':
      return <span className="text-zinc-100">{word.expected || word.typed}</span>
    case 'substitute':
      return (
        <span
          className="inline-flex items-baseline gap-1 rounded-md bg-rose-500/10 px-1.5"
          title={`"${word.typed}" yazdın, doğrusu "${word.expected}"`}
        >
          <span className="text-rose-300/80 line-through decoration-rose-400/80">{word.typed}</span>
          <span className="font-semibold text-emerald-300 underline decoration-emerald-400/70 decoration-2 underline-offset-4">
            {word.expected}
          </span>
        </span>
      )
    case 'missing':
      return (
        <span
          className="rounded-md border border-dashed border-amber-400/60 px-1.5 italic text-amber-200"
          title={`Eksik kelime: "${word.expected}"`}
        >
          {word.expected}
        </span>
      )
    case 'extra':
      return (
        <span
          className="rounded-md bg-rose-500/10 px-1.5 text-rose-300/80 line-through decoration-rose-400"
          title={`Fazladan yazılan: "${word.typed}"`}
        >
          {word.typed}
        </span>
      )
    default:
      return null
  }
}

export const DiffView: React.FC<DiffViewProps> = ({ diff, compact = false }) => {
  const percent = Math.round(diff.accuracy * 100)
  return (
    <section
      aria-label="Karşılaştırma sonucu"
      className={cx(
        'w-full rounded-2xl border border-white/[0.08] bg-white/[0.02]',
        compact ? 'p-3' : 'p-4 sm:p-5'
      )}
    >
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <span
          className={cx(
            'inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-xs font-medium',
            diff.isPerfect
              ? 'bg-emerald-500/10 text-emerald-300'
              : 'bg-amber-500/10 text-amber-300'
          )}
        >
          {diff.isPerfect ? (
            <>
              <CheckCircle2 className="h-3.5 w-3.5" /> Kusursuz
            </>
          ) : (
            <>
              <AlertCircle className="h-3.5 w-3.5" /> Hatalar var
            </>
          )}
        </span>
        <span className="text-xs tabular-nums text-zinc-400">
          Doğruluk: {percent}% ({diff.correctCount}/{diff.expectedCount})
        </span>
      </div>

      <p
        className={cx(
          'flex flex-wrap items-baseline gap-x-2 gap-y-2 font-serif leading-relaxed',
          compact ? 'text-base' : 'text-lg sm:text-xl'
        )}
      >
        {diff.words.map((word, idx) => (
          <DiffToken key={idx} word={word} />
        ))}
      </p>

      {!diff.isPerfect && !compact && (
        <div className="mt-4 flex flex-wrap gap-x-4 gap-y-1 border-t border-white/[0.06] pt-3 text-[11px] text-zinc-500">
          <span>
            <span className="text-rose-300/80 line-through">yanlış</span> →{' '}
            <span className="text-emerald-300 underline underline-offset-4">doğru</span>
          </span>
          <span>
            <span className="rounded border border-dashed border-amber-400/60 px-1 italic text-amber-200">
              eksik
            </span>
          </span>
          <span>
            <span className="text-rose-300/80 line-through">fazla</span>
          </span>
        </div>
      )}
    </section>
  )
}
