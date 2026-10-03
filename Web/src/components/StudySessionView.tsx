import React, { useRef, useEffect, useState, useMemo } from 'react'
import type { Lesson } from '../domain/lessons/types'
import type { AudioEngine } from '../domain/audio/audio-engine'
import type { MistakeRepository } from '../domain/mistakes/types'
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
  RotateCcw,
  Sparkles,
  Eye,
  EyeOff,
  AlertCircle,
} from 'lucide-react'

export interface StudySessionViewProps {
  lesson: Lesson
  audioEngine: AudioEngine
  mistakeRepository?: MistakeRepository
  onBackToLessons?: () => void
}

export const StudySessionView: React.FC<StudySessionViewProps> = ({
  lesson,
  audioEngine,
  mistakeRepository,
  onBackToLessons,
}) => {
  const session = useStudySession({
    lesson,
    audioEngine,
    autoPlay: true,
    mistakeRepository,
  })

  const textareaRef = useRef<HTMLTextAreaElement>(null)
  const correctionInputRef = useRef<HTMLInputElement>(null)
  const nextButtonRef = useRef<HTMLButtonElement>(null)

  const [speed, setSpeed] = useState<number>(() => {
    try {
      const saved = localStorage.getItem('dictalearn_audio_speed')
      if (saved) {
        const num = parseFloat(saved)
        if (!isNaN(num) && [0.75, 1.0, 1.25].includes(num)) {
          return num
        }
      }
    } catch {
      // localStorage unavailable in some test or strict contexts
    }
    return 1.0
  })

  const [showShortcutsModal, setShowShortcutsModal] = useState(false)

  // Sync audio speed
  useEffect(() => {
    audioEngine.setSpeed(speed)
  }, [speed, audioEngine])

  const handleSpeedChange = (newSpeed: number) => {
    setSpeed(newSpeed)
    try {
      localStorage.setItem('dictalearn_audio_speed', String(newSpeed))
    } catch {
      // Ignore storage errors
    }
    audioEngine.setSpeed(newSpeed)
  }

  // Auto-focus management depending on state
  useEffect(() => {
    if (session.state === 'dictating') {
      const t = setTimeout(() => {
        textareaRef.current?.focus()
      }, 50)
      return () => clearTimeout(t)
    } else if (session.state === 'reviewing') {
      const t = setTimeout(() => {
        correctionInputRef.current?.focus()
      }, 50)
      return () => clearTimeout(t)
    } else if (session.state === 'shadowing') {
      const t = setTimeout(() => {
        nextButtonRef.current?.focus()
      }, 50)
      return () => clearTimeout(t)
    }
  }, [session.state, session.currentSegmentIndex])

  // Keyboard shortcuts integration (F1.6, F3.1, F3.2)
  useShortcuts({
    onCtrlEnter: () => {
      if (session.state === 'dictating') {
        session.giveUp()
      } else if (session.state === 'reviewing') {
        session.skipCorrection()
      } else if (session.state === 'shadowing') {
        session.nextSegment()
      }
    },
    onCtrlSpace: () => {
      audioEngine.pause()
    },
    onCtrlR: () => {
      session.replaySegment()
    },
    onCtrlT: () => {
      if (session.state === 'shadowing' || session.state === 'reviewing') {
        session.toggleTranslation()
      }
    },
    onSpeed1: () => handleSpeedChange(0.75),
    onSpeed2: () => handleSpeedChange(1.0),
    onSpeed3: () => handleSpeedChange(1.25),
  })

  // Enter inside dictation textarea submits answer
  const handleDictationKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey && !e.ctrlKey) {
      e.preventDefault()
      session.submitAnswer()
    }
  }

  // Enter inside correction input submits correction
  const handleCorrectionKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !e.ctrlKey) {
      e.preventDefault()
      session.submitCorrection()
    }
  }

  const progressPercent = Math.round(
    ((session.currentSegmentIndex + (session.state === 'completed' ? 1 : 0)) /
      session.totalSegments) *
      100
  )

  // Top mistakes list for completed screen (F3.4)
  const topMistakes = useMemo(() => {
    if (!mistakeRepository) return []
    const frequencies = mistakeRepository.getWordFrequencies()
    return Object.entries(frequencies)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10)
  }, [mistakeRepository])

  // Completed State View (F3.4)
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
      <div className="max-w-2xl mx-auto w-full p-6 text-center space-y-6 animate-in fade-in duration-300">
        <div className="w-16 h-16 bg-amber-500/20 text-amber-400 rounded-full flex items-center justify-center mx-auto border border-amber-500/40">
          <Trophy className="w-8 h-8" />
        </div>
        <h2 className="text-3xl font-bold text-slate-100">Ders Tamamlandı!</h2>
        <p className="text-slate-400">{lesson.title}</p>

        <div className="grid grid-cols-3 gap-4 my-8">
          <div className="bg-slate-800/60 p-4 rounded-xl border border-slate-700">
            <span className="text-xs text-slate-400 uppercase tracking-wider block">
              Ortalama Doğruluk
            </span>
            <span className="text-2xl font-bold text-emerald-400 mt-1 block">%{avgAccuracy}</span>
          </div>
          <div className="bg-slate-800/60 p-4 rounded-xl border border-slate-700">
            <span className="text-xs text-slate-400 uppercase tracking-wider block">
              Kusursuz Cümle
            </span>
            <span className="text-2xl font-bold text-cyan-400 mt-1 block">
              {perfectCount} / {session.totalSegments}
            </span>
          </div>
          <div className="bg-slate-800/60 p-4 rounded-xl border border-slate-700">
            <span className="text-xs text-slate-400 uppercase tracking-wider block">
              Tekrar Dinleme
            </span>
            <span className="text-2xl font-bold text-amber-400 mt-1 block">{totalReplays} kez</span>
          </div>
        </div>

        {/* Hata Defteri Özeti (F3.4) */}
        {topMistakes.length > 0 && (
          <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 text-left space-y-3">
            <h3 className="text-sm font-semibold text-slate-200 flex items-center gap-2">
              <AlertCircle className="w-4 h-4 text-amber-400" />
              <span>Hata Defteri: Tekrar Edilmesi Önerilen Kelimeler</span>
            </h3>
            <div className="flex flex-wrap gap-2">
              {topMistakes.map(([word, count]) => (
                <span
                  key={word}
                  className="px-2.5 py-1 bg-rose-950/40 border border-rose-800/50 rounded-lg text-xs text-rose-300 flex items-center gap-1.5"
                >
                  <span className="font-medium">{word}</span>
                  <span className="bg-rose-900/60 px-1.5 py-0.2 rounded-full text-[10px] text-rose-200">
                    {count}x
                  </span>
                </span>
              ))}
            </div>
          </div>
        )}

        <div className="flex justify-center gap-4 pt-4">
          <button
            onClick={() => window.location.reload()}
            className="px-6 py-2.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-medium transition cursor-pointer"
          >
            Dersi Tekrar Başlat
          </button>
          {onBackToLessons && (
            <button
              onClick={onBackToLessons}
              className="px-6 py-2.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium transition cursor-pointer"
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
          {/* Audio Speed Controls (F3.5) */}
          <div className="flex items-center bg-slate-800/80 p-1 rounded-lg border border-slate-700 text-xs">
            {[0.75, 1.0, 1.25].map((s) => (
              <button
                key={s}
                onClick={() => handleSpeedChange(s)}
                className={`px-2 py-1 rounded transition cursor-pointer ${
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
            className="p-2 text-slate-400 hover:text-slate-200 bg-slate-800/80 hover:bg-slate-700 border border-slate-700 rounded-lg transition cursor-pointer"
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
            className="flex items-center gap-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg font-medium text-sm transition shadow-sm cursor-pointer"
            title="Cümleyi Dinle / Baştan Çal (Ctrl+R)"
          >
            <Volume2 className="w-4 h-4" />
            <span>Tekrar Dinle</span>
          </button>
          {session.replayCount > 0 && (
            <span className="text-xs text-slate-400">({session.replayCount} kez dinlendi)</span>
          )}
        </div>

        <div className="text-xs text-slate-400 flex items-center gap-1.5">
          <span
            className={`w-2 h-2 rounded-full inline-block animate-pulse ${
              session.state === 'dictating'
                ? 'bg-emerald-500'
                : session.state === 'reviewing'
                ? 'bg-amber-500'
                : 'bg-indigo-500'
            }`}
          />
          <span>
            {session.state === 'dictating'
              ? 'Dikte Modu'
              : session.state === 'reviewing'
              ? 'Düzeltme Modu'
              : 'Shadowing Modu'}
          </span>
        </div>
      </div>

      {/* MAIN STUDY AREA */}
      <div className="space-y-4">
        {/* 1. DICTATING STATE: Textarea only, zero original text in DOM */}
        {session.state === 'dictating' && (
          <div className="space-y-3 animate-in fade-in duration-150">
            <label htmlFor="dictation-input" className="block text-sm font-medium text-slate-300">
              Duyduğunuz cümleyi yazın:
            </label>
            <textarea
              id="dictation-input"
              ref={textareaRef}
              value={session.typedText}
              onChange={(e) => session.setTypedText(e.target.value)}
              onKeyDown={handleDictationKeyDown}
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
                className="flex items-center gap-1.5 text-xs text-slate-400 hover:text-amber-400 transition py-1.5 px-3 rounded hover:bg-slate-800 cursor-pointer"
                title="Bilmiyorum, cevabı göster (Ctrl+Enter)"
              >
                <HelpCircle className="w-3.5 h-3.5" />
                <span>Bilmiyorum / Göster (Ctrl+Enter)</span>
              </button>

              <button
                type="button"
                onClick={() => session.submitAnswer()}
                disabled={!session.typedText.trim()}
                className="flex items-center gap-2 px-5 py-2.5 bg-emerald-600 hover:bg-emerald-500 disabled:opacity-40 disabled:hover:bg-emerald-600 text-white rounded-lg font-medium text-sm transition shadow-sm cursor-pointer"
              >
                <Check className="w-4 h-4" />
                <span>Kontrol Et (Enter)</span>
              </button>
            </div>
          </div>
        )}

        {/* 2. REVIEWING STATE: Diff View, Original Text, Translation & Correction Input (F3.1) */}
        {session.state === 'reviewing' && session.diffResult && (
          <div className="space-y-5 animate-in fade-in duration-200">
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

            {/* Correction Form (F3.1) */}
            <div className="bg-slate-900/80 border border-amber-500/30 rounded-xl p-5 space-y-3 shadow-sm">
              <div className="flex items-center justify-between">
                <label
                  htmlFor="correction-input"
                  className="text-sm font-semibold text-amber-300 flex items-center gap-2"
                >
                  <RotateCcw className="w-4 h-4 text-amber-400" />
                  <span>Cümleyi düzelterek yeniden yazın:</span>
                </label>
                <span className="text-xs text-slate-400">Atlamak için: Ctrl+Enter</span>
              </div>

              <input
                id="correction-input"
                ref={correctionInputRef}
                type="text"
                value={session.correctionText}
                onChange={(e) => session.setCorrectionText(e.target.value)}
                onKeyDown={handleCorrectionKeyDown}
                autoComplete="off"
                autoCorrect="off"
                spellCheck={false}
                placeholder="Doğru cümleyi buraya yazın ve Enter'a basın..."
                className="w-full bg-slate-950 border border-slate-700 rounded-lg p-3 text-slate-100 placeholder-slate-500 focus:outline-none focus:border-amber-500 focus:ring-2 focus:ring-amber-500/30 transition text-base"
              />

              {/* Real-time correction diff feedback if attempted */}
              {session.correctionDiff && !session.correctionDiff.isPerfect && (
                <div className="pt-2 space-y-1.5">
                  <p className="text-xs text-rose-400 font-medium">
                    Düzeltmenizde hala eksik veya yanlış kelimeler var:
                  </p>
                  <DiffView diff={session.correctionDiff} />
                </div>
              )}

              <div className="flex items-center justify-between pt-2">
                <button
                  type="button"
                  onClick={session.skipCorrection}
                  className="text-xs text-slate-400 hover:text-slate-200 py-1.5 px-3 rounded hover:bg-slate-800 transition cursor-pointer"
                  title="Düzeltmeyi geçip doğrudan Shadowing'e ilerle (Ctrl+Enter)"
                >
                  Düzeltmeyi Atla (Ctrl+Enter)
                </button>

                <button
                  type="button"
                  onClick={() => session.submitCorrection()}
                  disabled={!session.correctionText.trim()}
                  className="flex items-center gap-2 px-4 py-2 bg-amber-600 hover:bg-amber-500 disabled:opacity-40 disabled:hover:bg-amber-600 text-white rounded-lg font-medium text-xs transition shadow-sm cursor-pointer"
                >
                  <Check className="w-3.5 h-3.5" />
                  <span>Düzeltmeyi Kontrol Et (Enter)</span>
                </button>
              </div>
            </div>
          </div>
        )}

        {/* 3. SHADOWING STATE: Audio Replay, Original Text, Translation Toggle & Next Segment (F3.2) */}
        {session.state === 'shadowing' && (
          <div className="space-y-5 animate-in fade-in duration-200">
            {/* Diff Result (Shows 100% or user's score) */}
            {session.diffResult && <DiffView diff={session.diffResult} />}

            {/* Shadowing Card */}
            <div className="bg-slate-900 border border-indigo-500/40 rounded-xl p-6 space-y-4 shadow-lg shadow-indigo-950/20">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <div className="flex items-center gap-2 text-indigo-400 font-semibold text-sm">
                  <Sparkles className="w-4 h-4" />
                  <span>Shadowing / Sesli Tekrar Modu</span>
                </div>

                {/* Translation Toggle Button (F3.2) */}
                <button
                  type="button"
                  onClick={session.toggleTranslation}
                  className="flex items-center gap-1.5 text-xs text-slate-300 hover:text-white px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 transition cursor-pointer"
                  title="Çeviriyi Aç / Kapat (Ctrl+T)"
                >
                  {session.showTranslation ? (
                    <EyeOff className="w-3.5 h-3.5 text-slate-400" />
                  ) : (
                    <Eye className="w-3.5 h-3.5 text-indigo-400" />
                  )}
                  <span>{session.showTranslation ? 'Çeviriyi Gizle' : 'Çeviriyi Göster'}</span>
                  <kbd className="ml-1 text-[10px] bg-slate-900 px-1 py-0.5 rounded border border-slate-700 text-slate-400 font-mono">
                    Ctrl+T
                  </kbd>
                </button>
              </div>

              {/* Original Sentence Display */}
              <div className="space-y-1.5">
                <span className="text-xs uppercase font-semibold text-slate-400 tracking-wider">
                  Orijinal Cümle:
                </span>
                <p className="text-xl sm:text-2xl font-bold text-slate-100 tracking-wide select-text leading-relaxed">
                  {session.currentSegment.text}
                </p>
              </div>

              {/* Audio Listen & Shadow Callout */}
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-2 bg-slate-950/60 p-3 rounded-lg border border-slate-800">
                <div className="text-xs text-slate-300">
                  <span className="font-semibold text-indigo-300 block">Nasıl Çalışmalı?</span>
                  Cümleyi dinleyin, konuşmacının telaffuz ve tonlamasını taklit ederek sesli tekrar
                  edin.
                </div>
                <button
                  type="button"
                  onClick={session.replaySegment}
                  className="flex items-center justify-center gap-2 px-3.5 py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-xs font-medium transition cursor-pointer shrink-0"
                  title="Sesli tekrar için cümleyi dinle (Ctrl+R)"
                >
                  <Volume2 className="w-4 h-4" />
                  <span>Dinle (Ctrl+R)</span>
                </button>
              </div>

              {/* Translation Display (Toggleable via Ctrl+T) */}
              {session.showTranslation && session.currentSegment.translation && (
                <div className="pt-3 border-t border-slate-800 space-y-1 animate-in fade-in duration-150">
                  <span className="text-xs uppercase font-semibold text-indigo-300 tracking-wider">
                    Türkçe Çeviri:
                  </span>
                  <p className="text-base text-slate-200">{session.currentSegment.translation}</p>
                </div>
              )}

              {/* Segment Notes */}
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
                ref={nextButtonRef}
                onClick={session.nextSegment}
                className="flex items-center gap-2 px-6 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg font-medium text-sm transition shadow-sm cursor-pointer"
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
                className="text-slate-400 hover:text-slate-200 cursor-pointer"
              >
                ✕
              </button>
            </div>

            <div className="space-y-2 text-sm">
              <div className="flex justify-between py-1.5 border-b border-slate-800/60">
                <span className="text-slate-400">Kontrol Et / Düzelt / Sonraki Cümle</span>
                <kbd className="px-2 py-0.5 bg-slate-800 rounded border border-slate-700 text-slate-200 font-mono text-xs">
                  Enter
                </kbd>
              </div>
              <div className="flex justify-between py-1.5 border-b border-slate-800/60">
                <span className="text-slate-400">Pes Et / Düzeltmeyi Atla</span>
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
                <span className="text-slate-400">Çeviriyi Aç / Kapat</span>
                <kbd className="px-2 py-0.5 bg-slate-800 rounded border border-slate-700 text-slate-200 font-mono text-xs">
                  Ctrl + T
                </kbd>
              </div>
              <div className="flex justify-between py-1.5 border-b border-slate-800/60">
                <span className="text-slate-400">Sesi Duraklat / Devam Et</span>
                <kbd className="px-2 py-0.5 bg-slate-800 rounded border border-slate-700 text-slate-200 font-mono text-xs">
                  Ctrl + Space
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
              className="w-full mt-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-sm font-medium transition cursor-pointer"
            >
              Kapat
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
