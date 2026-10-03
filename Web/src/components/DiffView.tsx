import React from 'react'
import type { DiffResult, DiffWord } from '../domain/diff/types'
import { CheckCircle2, AlertCircle, XCircle } from 'lucide-react'

interface DiffViewProps {
  diff: DiffResult
}

export const DiffView: React.FC<DiffViewProps> = ({ diff }) => {
  return (
    <div className="w-full bg-slate-900 border border-slate-700/80 rounded-xl p-5 shadow-lg space-y-4">
      <div className="flex items-center justify-between pb-3 border-b border-slate-800">
        <span className="text-sm font-medium text-slate-400">Karşılaştırma Sonucu:</span>
        <div className="flex items-center gap-3">
          <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-800 text-slate-300">
            Doğruluk: {Math.round(diff.accuracy * 100)}% ({diff.correctCount}/{diff.expectedCount})
          </span>
          {diff.isPerfect ? (
            <span className="inline-flex items-center gap-1 text-xs font-semibold text-emerald-400 bg-emerald-950/60 px-2.5 py-1 rounded-full border border-emerald-800/60">
              <CheckCircle2 className="w-3.5 h-3.5" /> Kusursuz
            </span>
          ) : (
            <span className="inline-flex items-center gap-1 text-xs font-semibold text-amber-400 bg-amber-950/60 px-2.5 py-1 rounded-full border border-amber-800/60">
              <AlertCircle className="w-3.5 h-3.5" /> Hatalar Var
            </span>
          )}
        </div>
      </div>

      {/* Word-by-word diff output (shape + color distinction) */}
      <div className="flex flex-wrap items-baseline gap-x-2 gap-y-3 text-lg leading-relaxed font-sans">
        {diff.words.map((word: DiffWord, idx: number) => {
          if (word.kind === 'equal') {
            return (
              <span
                key={idx}
                className="text-emerald-400 font-medium"
                title="Doğru"
              >
                {word.expected || word.typed}
              </span>
            )
          }

          if (word.kind === 'substitute') {
            return (
              <span
                key={idx}
                className="inline-flex flex-col items-center px-1 py-0.5 rounded bg-rose-950/40 border border-rose-800/50"
                title={`Yanlış: "${word.typed}" yerine "${word.expected}"`}
              >
                <span className="text-xs line-through text-rose-400/80 decoration-2">
                  {word.typed}
                </span>
                <span className="text-emerald-400 font-semibold underline decoration-emerald-500 decoration-2 underline-offset-2">
                  {word.expected}
                </span>
              </span>
            )
          }

          if (word.kind === 'missing') {
            return (
              <span
                key={idx}
                className="inline-flex items-center gap-1 px-1.5 py-0.5 rounded bg-amber-950/40 border border-dashed border-amber-600/70 text-amber-300 italic underline decoration-amber-500 underline-offset-2"
                title={`Eksik kelime: "${word.expected}"`}
              >
                <span>+{word.expected}</span>
              </span>
            )
          }

          if (word.kind === 'extra') {
            return (
              <span
                key={idx}
                className="inline-flex items-center gap-1 px-1.5 py-0.5 rounded bg-rose-950/40 border border-rose-800/60 text-rose-400 line-through decoration-rose-500 decoration-2"
                title={`Fazladan yazılan: "${word.typed}"`}
              >
                <XCircle className="w-3 h-3 text-rose-500 inline" />
                <span>{word.typed}</span>
              </span>
            )
          }

          return null
        })}
      </div>
    </div>
  )
}
