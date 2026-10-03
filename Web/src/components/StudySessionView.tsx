import React, { useRef, useEffect, useState } from 'react'
import type { Lesson } from '../domain/lessons/types'
import type { AudioEngine } from '../domain/audio/audio-engine'
import { useStudySession } from '../state/use-study-session'
import { useShortcuts } from '../hooks/use-shortcuts'
import { DiffView } from './DiffView'
import {
  Volume2,
  ArrowRight,
  HelpCircle,
  Trophy,
  Check,
  Keyboard,
} from 'lucide-react'

interface StudySessionViewProps {
  lesson: Lesson
  audioEngine: AudioEngine
  onBackToLessons?: () => void
}

export const StudySessionView: React.FC<StudySessionViewProps> = ({
  lesson,
  audioEngine,
  onBackToLessons,
}) => {
  const session = useStudySession({ lesson, audioEngine, autoPlay: true })
  const textareaRef = useRef<HTMLTextAreaElement>(null)
  const [speed, setSpeed] = useState(1.0)
  const [showShortcutsModal, setShowShortcutsModal] = useState(false)

  // Focus textarea upon entering dictating
  useEffect(() => {
    if (session.state === 'dictating') {
      setTimeout(() => {
        textareaRef.current?.focus()
      }, 50)
    }
  }, [session.state, session.currentSegmentIndex])

  const handleSpeedChange = (newSpeed: number) => {
    setSpeed(newSpeed)
    audioEngine.setSpeed(newSpeed)
  }

  // Keyboard shortcuts integration
  useShortcuts({
    onCtrlEnter: () => {
      if (session.state === 'dictating') {
        session.giveUp()
      } else if (session.state === 'reviewing') {
        session.nextSegment()
      }
    },
    onCtrlSpace: () => {
      audioEngine.pause()
    },
    onCtrlR: () => {
      session.replaySegment()
    },
    onSpeed1: () => handleSpeedChange(0.75),
    onSpeed2: () => handleSpeedChange(1.0),
    onSpeed3: () => handleSpeedChange(1.25),
  })

  // Enter inside textarea submits answer without adding a newline
  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey && !e.ctrlKey) {
      e.preventDefault()
      session.submitAnswer()
    }
  }

  const progressPercent = Math.round(
    ((session.currentSegmentIndex + (session.state === 'completed' ? 1 : 0)) /
      session.totalSegments) *
      100
  )

  // Completed State View
  if (session.state === 'completed') {
    const totalRecords = session.sessionRecords.length
    const perfectCount = session.sessionRecords.filter((r) => r.isPerfect).length
    const avgAccuracy =
      totalRecords > 0
        ? Math.round(
            (session.sessionRecords.reduce((acc, r) => acc + r.accuracy, 0) / totalRecords) * 100
          )
        : 100
    const totalReplays = session.sessionRecords.reduce((acc, r) => acc + r.replayCount, 0)

    return (
      <div className="max-w-2xl mx-auto w-full p-6 text-center space-y-6">
        <div className="w-16 h-16 bg-amber-500/20 text-amber-400 rounded-full flex items-center justify-center mx-auto border border-amber-500/40">
          <Trophy className="w-8 h-8" />
        </div>
        <h2 className="text-3xl font-bold text-slate-100">Ders Tamamlandı!</h2>
        <p className="text-slate-400">{lesson.title}</p>

        <div className="grid grid-cols-3 gap-4 my-8">
          <div className="bg-slate-800/60 p-4 rounded-xl border border-slate-700">
            <span className="text-xs text-slate-400 uppercase tracking-wider block">Ortalama Doğruluk</span>
            <span className="text-2xl font-bold text-emerald-400 mt-1 block">%{avgAccuracy}</span>
          </div>
          <div className="bg-slate-800/60 p-4 rounded-xl border border-slate-700">
            <span className="text-xs text-slate-400 uppercase tracking-wider block">Kusursuz Cümle</span>
            <span className="text-2xl font-bold text-cyan-400 mt-1 block">
              {perfectCount} / {session.totalSegments}
            </span>
          </div>
          <div className="bg-slate-800/60 p-4 rounded-xl border border-slate-700">
            <span className="text-xs text-slate-400 uppercase tracking-wider block">Tekrar Dinleme</span>
            <span className="text-2xl font-bold text-amber-400 mt-1 block">{totalReplays} kez</span>
          </div>
        </div>

        <div className="flex justify-center gap-4">
          <button
            onClick={() => window.location.reload()}
            className="px-6 py-2.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-medium transition"
          >
            Dersi Tekrar Başlat
          </button>
          {onBackToLessons && (
            <button
              onClick={onBackToLessons}
              className="px-6 py-2.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium transition"
            >
              Dersler Listesi
            </button>
          )}
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-3xl mx-auto w-full px-4 py-6 space-y-6">
      {/* Top Header & Navigation */}
      <header className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-800">
        <div>
          <h1 className="text-xl font-bold text-slate-100">{lesson.title}</h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Cümle {session.currentSegmentIndex + 1} / {session.totalSegments}
          </p>
        </div>

        <div className="flex items-center gap-2">
          {/* Audio Speed Controls */}
          <div className="flex items-center bg-slate-800/80 p-1 rounded-lg border border-slate-700 text-xs">
            {[0.75, 1.0, 1.25].map((s) => (
              <button
                key={s}
                onClick={() => handleSpeedChange(s)}
                className={`px-2 py-1 rounded transition ${
                  speed === s
                    ? 'bg-indigo-600 text-white font-semibold'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
                title={`Hız: ${s}x (Ctrl+${s === 0.75 ? 1 : s === 1.0 ? 2 : 3})`}
              >
                {s}x
              </button>
            ))}
          </div>

          {/* Shortcuts Help Button */}
          <button
            onClick={() => setShowShortcutsModal(!showShortcutsModal)}
            className="p-2 text-slate-400 hover:text-slate-200 bg-slate-800/80 hover:bg-slate-700 border border-slate-700 rounded-lg transition"
            title="Klavye Kısayolları (F1)"
          >
            <Keyboard className="w-4 h-4" />
          </button>
        </div>
      </header>

      {/* Progress Bar */}
      <div className="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
        <div
          className="bg-indigo-500 h-full transition-all duration-300"
          style={{ width: `${progressPercent}%` }}
        />
      </div>

      {/* Audio Playback Controls Bar */}
      <div className="flex items-center justify-between bg-slate-900/60 border border-slate-800 p-3 rounded-xl">
        <div className="flex items-center gap-3">
          <button
            onClick={session.replaySegment}
            className="flex items-center gap-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg font-medium text-sm transition shadow-sm"
            title="Cümleyi Dinle / Baştan Çal (Ctrl+R)"
          >
            <Volume2 className="w-4 h-4" />
            <span>Tekrar Dinle</span>
          </button>
          {session.replayCount > 0 && (
            <span className="text-xs text-slate-400">
              ({session.replayCount} kez dinlendi)
            </span>
          )}
        </div>

        <div className="text-xs text-slate-400 flex items-center gap-1.5">
          <span className="w-2 h-2 rounded-full bg-emerald-500 inline-block animate-pulse" />
          <span>{session.state === 'dictating' ? 'Dikte Modu' : 'İnceleme Modu'}</span>
        </div>
      </div>

      {/* MAIN STUDY AREA */}
      <div className="space-y-4">
        {/* DICTATING STATE: Textarea only, zero original text in DOM */}
        {session.state === 'dictating' && (
          <div className="space-y-3">
            <label htmlFor="dictation-input" className="block text-sm font-medium text-slate-300">
              Duyduğunuz cümleyi yazın:
            </label>
            <textarea
              id="dictation-input"
              ref={textareaRef}
              value={session.typedText}
              onChange={(e) => session.setTypedText(e.target.value)}
              onKeyDown={handleKeyDown}
              autoComplete="off"
              autoCorrect="off"
              autoCapitalize="off"
              spellCheck={false}
              rows={3}
              placeholder="Duyduğunuz cümleyi buraya yazın ve Enter'a basın..."
              className="w-full bg-slate-900 border border-slate-700 rounded-xl p-4 text-lg text-slate-100 placeholder-slate-500 focus:outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/30 transition resize-none font-sans"
            />

            <div className="flex items-center justify-between pt-2">
              <button
                type="button"
                onClick={session.giveUp}
                className="flex items-center gap-1.5 text-xs text-slate-400 hover:text-amber-400 transition py-1.5 px-3 rounded hover:bg-slate-800"
                title="Bilmiyorum, cevabı göster (Ctrl+Enter)"
              >
                <HelpCircle className="w-3.5 h-3.5" />
                <span>Bilmiyorum / Göster (Ctrl+Enter)</span>
              </button>

              <button
                type="button"
                onClick={() => session.submitAnswer()}
                disabled={!session.typedText.trim()}
                className="flex items-center gap-2 px-5 py-2.5 bg-emerald-600 hover:bg-emerald-500 disabled:opacity-40 disabled:hover:bg-emerald-600 text-white rounded-lg font-medium text-sm transition shadow-sm"
              >
                <Check className="w-4 h-4" />
                <span>Kontrol Et (Enter)</span>
              </button>
            </div>
          </div>
        )}

        {/* REVIEWING STATE: Diff View, Original Text & Translation */}
        {session.state === 'reviewing' && session.diffResult && (
          <div className="space-y-4 animate-in fade-in duration-200">
            {/* Diff Result */}
            <DiffView diff={session.diffResult} />

            {/* Original Sentence & Translation Card */}
            <div className="bg-slate-900/90 border border-slate-700/70 rounded-xl p-5 space-y-3">
              <div className="space-y-1">
                <span className="text-xs uppercase font-semibold text-slate-400 tracking-wider">
                  Orijinal Metin:
                </span>
                <p className="text-lg font-semibold text-slate-100 select-text">
                  {session.currentSegment.text}
                </p>
              </div>

              {session.currentSegment.translation && (
                <div className="pt-2 border-t border-slate-800 space-y-1">
                  <span className="text-xs uppercase font-semibold text-slate-400 tracking-wider">
                    Çeviri:
                  </span>
                  <p className="text-base text-slate-300">
                    {session.currentSegment.translation}
                  </p>
                </div>
              )}

              {session.currentSegment.notes && (
                <div className="pt-2 border-t border-slate-800 text-xs text-amber-300/90 bg-amber-950/30 p-2.5 rounded-lg border border-amber-900/40">
                  <span className="font-semibold block">Not:</span>
                  {session.currentSegment.notes}
                </div>
              )}
            </div>

            {/* Next Segment Button */}
            <div className="flex justify-end pt-2">
              <button
                onClick={session.nextSegment}
                className="flex items-center gap-2 px-6 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg font-medium text-sm transition shadow-sm"
                autoFocus
              >
                <span>
                  {session.currentSegmentIndex >= session.totalSegments - 1
                    ? 'Dersi Bitir'
                    : 'Sonraki Cümle'}
                </span>
                <ArrowRight className="w-4 h-4" />
                <kbd className="ml-1 text-xs bg-indigo-800/80 px-1.5 py-0.5 rounded border border-indigo-700">
                  Enter
                </kbd>
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Keyboard Shortcuts Cheatsheet Modal */}
      {showShortcutsModal && (
        <div className="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 z-50">
          <div className="bg-slate-900 border border-slate-700 rounded-2xl max-w-md w-full p-6 space-y-4 shadow-2xl">
            <div className="flex items-center justify-between pb-3 border-b border-slate-800">
              <h3 className="font-semibold text-lg text-slate-100 flex items-center gap-2">
                <Keyboard className="w-5 h-5 text-indigo-400" />
                <span>Klavye Kısayolları</span>
              </h3>
              <button
                onClick={() => setShowShortcutsModal(false)}
                className="text-slate-400 hover:text-slate-200"
              >
                ✕
              </button>
            </div>

            <div className="space-y-2 text-sm">
              <div className="flex justify-between py-1.5 border-b border-slate-800/60">
                <span className="text-slate-400">Kontrol Et / Sonraki Segment</span>
                <kbd className="px-2 py-0.5 bg-slate-800 rounded border border-slate-700 text-slate-200 font-mono text-xs">
                  Enter
                </kbd>
              </div>
              <div className="flex justify-between py-1.5 border-b border-slate-800/60">
                <span className="text-slate-400">Pes Et / Cevabı Göster</span>
                <kbd className="px-2 py-0.5 bg-slate-800 rounded border border-slate-700 text-slate-200 font-mono text-xs">
                  Ctrl + Enter
                </kbd>
              </div>
              <div className="flex justify-between py-1.5 border-b border-slate-800/60">
                <span className="text-slate-400">Segmenti Baştan Dinle</span>
                <kbd className="px-2 py-0.5 bg-slate-800 rounded border border-slate-700 text-slate-200 font-mono text-xs">
                  Ctrl + R
                </kbd>
              </div>
              <div className="flex justify-between py-1.5 border-b border-slate-800/60">
                <span className="text-slate-400">Hız Değiştir (0.75x / 1.0x / 1.25x)</span>
                <kbd className="px-2 py-0.5 bg-slate-800 rounded border border-slate-700 text-slate-200 font-mono text-xs">
                  Ctrl + 1 / 2 / 3
                </kbd>
              </div>
            </div>

            <button
              onClick={() => setShowShortcutsModal(false)}
              className="w-full mt-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-sm font-medium transition"
            >
              Kapat
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
