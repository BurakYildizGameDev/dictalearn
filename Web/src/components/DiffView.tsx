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

      {/* Word-by-word diff output (shape + color distinction, horizontal inline flow) */}
      <div className="flex flex-wrap items-center gap-x-2 gap-y-2 text-base md:text-lg leading-relaxed font-sans">
        {diff.words.map((word: DiffWord, idx: number) => {
          if (word.kind === 'equal') {
            return (
              <span
                key={idx}
                className="text-emerald-400 font-medium px-1"
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
                className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-lg bg-rose-950/40 border border-rose-700/60 text-sm md:text-base"
                title={`Hata: "${word.typed}" yazdın, doğrusu "${word.expected}"`}
              >
                <span className="line-through text-rose-400/80 font-normal">
                  {word.typed}
                </span>
                <span className="text-emerald-400 font-semibold">
                  {word.expected}
                </span>
              </span>
            )
          }

          if (word.kind === 'missing') {
            return (
              <span
                key={idx}
                className="inline-flex items-center gap-1 px-2 py-0.5 rounded-lg bg-amber-950/40 border border-dashed border-amber-600/70 text-amber-300 italic text-sm md:text-base"
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
                className="inline-flex items-center gap-1 px-2 py-0.5 rounded-lg bg-rose-950/40 border border-rose-800/60 text-rose-400 line-through text-sm md:text-base"
                title={`Fazladan yazılan: "${word.typed}"`}
              >
                <XCircle className="w-3.5 h-3.5 text-rose-500 inline shrink-0" />
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
