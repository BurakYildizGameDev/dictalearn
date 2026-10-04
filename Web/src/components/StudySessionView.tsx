import React, { useRef, useEffect, useState, useMemo } from 'react'
import type { Lesson } from '../domain/lessons/types'
import type { AudioEngine } from '../domain/audio/audio-engine'
import type { MistakeRepository } from '../domain/mistakes/types'
import { useStudySession, type StudyMode } from '../state/use-study-session'
import { useShortcuts } from '../hooks/use-shortcuts'
import { useAudioStatus } from '../hooks/use-audio-status'
import { DiffView } from './DiffView'
import { WordLookupSentence } from './WordLookupSentence'
import { Button, Kbd, ProgressBar, Segmented } from './ui'
import { cx } from './cx'
import {
  Volume2,
  VolumeX,
  Pause,
  Play,
  ArrowRight,
  ArrowLeft,
  ChevronLeft,
  ChevronRight,
  Trophy,
  Check,
  Keyboard,
  RotateCcw,
  Eye,
  EyeOff,
  Lightbulb,
  SkipForward,
  BookOpen,
  HelpCircle,
  X,
  Mic,
  StickyNote,
  History,
} from 'lucide-react'

export interface StudySessionViewProps {
  lesson: Lesson
  audioEngine: AudioEngine
  mistakeRepository?: MistakeRepository
  initialSegmentIndex?: number
  onProgress?: (segmentIndex: number) => void
  onComplete?: () => void
  onBackToLessons?: () => void
  onOpenPdf?: () => void
  isPdfOpen?: boolean
  /** Short display title; defaults to lesson.title. */
  title?: string
}

const SPEEDS = [0.75, 1.0, 1.25] as const

function readStored<T>(key: string, parse: (raw: string) => T | undefined, fallback: T): T {
  try {
    const raw = localStorage.getItem(key)
    if (raw !== null) {
      const parsed = parse(raw)
      if (parsed !== undefined) return parsed
    }
  } catch {
    // localStorage unavailable (private mode / sandbox)
  }
  return fallback
}

function writeStored(key: string, value: string) {
  try {
    localStorage.setItem(key, value)
  } catch {
    // ignore storage errors
  }
}

/** Small equalizer shown while audio plays (F9.3). */
const PlayingBars: React.FC = () => (
  <span aria-hidden="true" className="flex h-3.5 items-end gap-[2px]">
    {[0, 150, 300, 450].map((delay) => (
      <span
        key={delay}
        className="h-full w-[3px] origin-bottom rounded-full bg-current animate-eq"
        style={{ animationDelay: `${delay}ms` }}
      />
    ))}
  </span>
)

/** Listen button that doubles as pause/resume while the segment is playing. */
const ListenButton: React.FC<{
  audioEngine: AudioEngine
  onReplay: () => void
  label?: string
  variant?: 'primary' | 'secondary'
}> = ({ audioEngine, onReplay, label = 'Dinle', variant = 'primary' }) => {
  const status = useAudioStatus(audioEngine)
  const playing = status === 'playing'
  return (
    <Button
      variant={variant}
      onClick={() => (playing ? audioEngine.pause() : onReplay())}
      title={playing ? 'Duraklat (Ctrl+Space)' : 'Cümleyi baştan dinle (Ctrl+R)'}
      className={cx(playing && 'ring-2 ring-indigo-300/40')}
    >
      {playing ? <Pause className="h-4 w-4" /> : <Volume2 className="h-4 w-4" />}
      <span>{playing ? 'Duraklat' : label}</span>
      {playing && <PlayingBars />}
    </Button>
  )
}

const Card: React.FC<{ children: React.ReactNode; className?: string; tone?: 'default' | 'amber' | 'indigo' }> = ({
  children,
  className,
  tone = 'default',
}) => (
  <div
    className={cx(
      'rounded-2xl border p-4 sm:p-6 animate-fade-up',
      tone === 'default' && 'border-white/[0.08] bg-zinc-900/60',
      tone === 'amber' && 'border-amber-400/20 bg-amber-400/[0.03]',
      tone === 'indigo' && 'border-indigo-400/20 bg-indigo-400/[0.04]',
      className
    )}
  >
    {children}
  </div>
)

const Eyebrow: React.FC<{ children: React.ReactNode; className?: string }> = ({ children, className }) => (
  <p className={cx('text-[11px] font-semibold uppercase tracking-[0.14em] text-zinc-500', className)}>
    {children}
  </p>
)

export const StudySessionView: React.FC<StudySessionViewProps> = ({
  lesson,
  audioEngine,
  mistakeRepository,
  initialSegmentIndex = 0,
  onProgress,
  onComplete,
  onBackToLessons,
  onOpenPdf,
  isPdfOpen = false,
  title,
}) => {
  const displayTitle = title ?? lesson.title
  // Default off: browsers block audio before the first user gesture anyway.
  const [autoPlay, setAutoPlay] = useState<boolean>(() =>
    readStored('dictalearn_autoplay', (raw) => raw === 'true', false)
  )
  const [speed, setSpeed] = useState<number>(() =>
    readStored(
      'dictalearn_audio_speed',
      (raw) => {
        const num = parseFloat(raw)
        return (SPEEDS as readonly number[]).includes(num) ? num : undefined
      },
      1.0
    )
  )
  const [showShortcutsModal, setShowShortcutsModal] = useState(false)
  const [resumeNoticeVisible, setResumeNoticeVisible] = useState(initialSegmentIndex > 0)

  const session = useStudySession({
    lesson,
    audioEngine,
    autoPlay,
    mistakeRepository,
    initialSegmentIndex,
    onProgress,
    onComplete,
  })
  const audioStatus = useAudioStatus(audioEngine)

  const textareaRef = useRef<HTMLTextAreaElement>(null)
  const wordInputRef = useRef<HTMLInputElement>(null)
  const correctionInputRef = useRef<HTMLInputElement>(null)
  const nextButtonRef = useRef<HTMLButtonElement>(null)

  useEffect(() => {
    audioEngine.setSpeed(speed)
  }, [speed, audioEngine])

  const handleSpeedChange = (newSpeed: number) => {
    setSpeed(newSpeed)
    writeStored('dictalearn_audio_speed', String(newSpeed))
    audioEngine.setSpeed(newSpeed)
  }

  const handleToggleAutoPlay = () => {
    const next = !autoPlay
    setAutoPlay(next)
    writeStored('dictalearn_autoplay', String(next))
  }

  const togglePlayback = () => {
    const status = audioEngine.getStatus()
    if (status === 'playing') audioEngine.pause()
    else if (status === 'paused') audioEngine.resume()
    else session.replaySegment()
  }

  // Focus follows the state machine so the whole loop works from the keyboard.
  useEffect(() => {
    const target =
      session.state === 'dictating'
        ? session.studyMode === 'word'
          ? wordInputRef.current
          : textareaRef.current
        : session.state === 'reviewing'
          ? correctionInputRef.current
          : session.state === 'shadowing'
            ? nextButtonRef.current
            : null
    if (!target) return
    const t = setTimeout(() => target.focus(), 50)
    return () => clearTimeout(t)
  }, [session.state, session.currentSegmentIndex, session.studyMode, session.currentWordIndex])

  useShortcuts({
    onCtrlEnter: () => {
      if (session.state === 'dictating') {
        if (session.studyMode === 'word') session.skipWord()
        else session.giveUp()
      } else if (session.state === 'reviewing') {
        session.skipCorrection()
      } else if (session.state === 'shadowing') {
        session.nextSegment()
      }
    },
    onCtrlSpace: togglePlayback,
    onCtrlR: () => session.replaySegment(),
    onCtrlT: () => {
      if (session.state === 'shadowing' || session.state === 'reviewing') session.toggleTranslation()
    },
    onCtrlM: () => session.toggleStudyMode(),
    onSpeed1: () => handleSpeedChange(0.75),
    onSpeed2: () => handleSpeedChange(1.0),
    onSpeed3: () => handleSpeedChange(1.25),
    onPageUp: () => session.previousSegment(),
    onPageDown: () => session.skipSegment(),
    onF1: () => setShowShortcutsModal((v) => !v),
    onEscape: showShortcutsModal ? () => setShowShortcutsModal(false) : undefined,
    onEnter: () => {
      if (session.state === 'shadowing') session.nextSegment()
    },
  })

  const handleDictationKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey && !e.ctrlKey && !e.metaKey) {
      e.preventDefault()
      session.submitAnswer()
    }
  }

  const handleWordKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.ctrlKey || e.metaKey) return
    if (e.key === 'Enter' || (e.key === ' ' && session.typedWord.trim().length > 0)) {
      e.preventDefault()
      session.submitWord()
    }
  }

  const handleCorrectionKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !e.ctrlKey && !e.metaKey) {
      e.preventDefault()
      session.submitCorrection()
    }
  }

  const isCompleted = session.state === 'completed'
  const progressPercent =
    ((session.currentSegmentIndex + (isCompleted ? 1 : 0)) / session.totalSegments) * 100

  // Mistakes of this lesson only, read when the summary is shown.
  const lessonMistakes = useMemo(() => {
    if (!isCompleted || !mistakeRepository) return []
    const counts = new Map<string, number>()
    for (const m of mistakeRepository.getMistakes()) {
      if (m.lesson_id !== lesson.lesson_id || !m.word) continue
      const w = m.word.toLowerCase()
      counts.set(w, (counts.get(w) ?? 0) + 1)
    }
    return [...counts.entries()].sort((a, b) => b[1] - a[1]).slice(0, 12)
  }, [isCompleted, mistakeRepository, lesson.lesson_id])

  // ─── Completed ────────────────────────────────────────────────────────────
  if (isCompleted) {
    const records = session.sessionRecords
    const perfectCount = records.filter((r) => r.isPerfect).length
    const avgAccuracy =
      records.length > 0
        ? Math.round((records.reduce((acc, r) => acc + r.accuracy, 0) / records.length) * 100)
        : 0
    const totalReplays = records.reduce((acc, r) => acc + r.replayCount, 0)

    return (
      <div className="mx-auto w-full max-w-2xl px-4 py-10 text-center animate-fade-up">
        <div className="mx-auto mb-5 flex h-14 w-14 items-center justify-center rounded-2xl bg-amber-400/10 text-amber-300">
          <Trophy className="h-7 w-7" />
        </div>
        <h2 className="font-serif text-3xl text-zinc-50">Ders tamamlandı</h2>
        <p className="mt-1 text-sm text-zinc-400">{displayTitle}</p>

        <dl className="my-8 grid grid-cols-3 gap-3">
          {[
            { label: 'Ortalama doğruluk', value: `%${avgAccuracy}`, color: 'text-emerald-300' },
            { label: 'Kusursuz cümle', value: `${perfectCount} / ${records.length}`, color: 'text-zinc-50' },
            { label: 'Tekrar dinleme', value: `${totalReplays}`, color: 'text-zinc-50' },
          ].map((s) => (
            <div key={s.label} className="rounded-2xl border border-white/[0.08] bg-zinc-900/60 p-4">
              <dt className="text-[11px] uppercase tracking-wider text-zinc-500">{s.label}</dt>
              <dd className={cx('mt-1 text-2xl font-semibold tabular-nums', s.color)}>{s.value}</dd>
            </div>
          ))}
        </dl>

        {lessonMistakes.length > 0 && (
          <div className="rounded-2xl border border-white/[0.08] bg-zinc-900/60 p-5 text-left">
            <Eyebrow className="mb-3">Hata defteri · tekrar et</Eyebrow>
            <div className="flex flex-wrap gap-2">
              {lessonMistakes.map(([word, count]) => (
                <span
                  key={word}
                  className="inline-flex items-center gap-1.5 rounded-lg bg-rose-500/10 px-2.5 py-1 text-sm text-rose-200"
                >
                  {word}
                  <span className="text-[10px] tabular-nums text-rose-300/70">×{count}</span>
                </span>
              ))}
            </div>
          </div>
        )}

        <div className="mt-8 flex flex-wrap justify-center gap-3">
          <Button variant="primary" size="lg" onClick={session.restart}>
            <RotateCcw className="h-4 w-4" />
            Dersi Tekrar Başlat
          </Button>
          {onBackToLessons && (
            <Button size="lg" onClick={onBackToLessons}>
              <ArrowLeft className="h-4 w-4" />
              Kütüphaneye Dön
            </Button>
          )}
        </div>
      </div>
    )
  }

  const segment = session.currentSegment
  const isLastSegment = session.currentSegmentIndex >= session.totalSegments - 1

  return (
    <div className="mx-auto flex w-full max-w-3xl flex-col gap-5 px-4 pb-6 pt-5 sm:pt-8">
      {/* ─── Header: title, segment navigation, progress ─────────────────── */}
      <header className="space-y-3">
        <div className="flex items-start justify-between gap-3">
          <div className="min-w-0">
            <h1 className="truncate font-serif text-xl text-zinc-50 sm:text-2xl">{displayTitle}</h1>
            <p className="mt-0.5 text-xs text-zinc-500">
              {session.studyMode === 'word' ? 'Kelime kelime dikte' : 'Cümle dikte'} ·{' '}
              {session.state === 'dictating'
                ? 'Dinle ve yaz'
                : session.state === 'reviewing'
                  ? 'Düzelt'
                  : 'Sesli tekrar'}
            </p>
          </div>

          <nav aria-label="Cümle gezinme" className="flex shrink-0 items-center gap-1">
            <button
              type="button"
              aria-label="Önceki cümle"
              title="Önceki cümle (PageUp)"
              onClick={session.previousSegment}
              disabled={session.currentSegmentIndex === 0}
              className="flex h-8 w-8 items-center justify-center rounded-lg text-zinc-400 hover:bg-white/5 hover:text-zinc-100 disabled:opacity-30 cursor-pointer"
            >
              <ChevronLeft className="h-4 w-4" />
            </button>
            <SegmentJump
              key={session.currentSegmentIndex}
              current={session.currentSegmentIndex}
              total={session.totalSegments}
              onJump={session.goToSegment}
            />
            <button
              type="button"
              aria-label="İleri atla"
              title="İleri atla (PageDown)"
              onClick={session.skipSegment}
              disabled={isLastSegment}
              className="flex h-8 w-8 items-center justify-center rounded-lg text-zinc-400 hover:bg-white/5 hover:text-zinc-100 disabled:opacity-30 cursor-pointer"
            >
              <ChevronRight className="h-4 w-4" />
            </button>
          </nav>
        </div>
        <ProgressBar value={progressPercent} label="Ders ilerlemesi" />
      </header>

      {resumeNoticeVisible && (
        <div className="flex items-center justify-between gap-3 rounded-xl border border-indigo-400/20 bg-indigo-400/[0.06] px-4 py-2.5 text-sm text-indigo-100 animate-fade-up">
          <span className="flex items-center gap-2">
            <History className="h-4 w-4 text-indigo-300" />
            Kaldığın yerden devam ediyorsun.
          </span>
          <span className="flex items-center gap-1">
            <Button
              size="sm"
              variant="ghost"
              onClick={() => {
                session.restart()
                setResumeNoticeVisible(false)
              }}
            >
              Baştan başla
            </Button>
            <button
              type="button"
              aria-label="Bildirimi kapat"
              onClick={() => setResumeNoticeVisible(false)}
              className="rounded-md p-1 text-indigo-200/70 hover:text-white cursor-pointer"
            >
              <X className="h-4 w-4" />
            </button>
          </span>
        </div>
      )}

      {audioStatus === 'blocked' && (
        <div className="rounded-xl border border-amber-400/20 bg-amber-400/[0.06] px-4 py-2.5 text-sm text-amber-100">
          Tarayıcı otomatik oynatmayı engelledi. Sesi başlatmak için <strong>Dinle</strong>&apos;ye bas.
        </div>
      )}

      {/* ─── Stage ───────────────────────────────────────────────────────── */}
      <main className="flex flex-col gap-4">
        {/* 1. Dictating · sentence */}
        {session.state === 'dictating' && session.studyMode === 'sentence' && (
          <Card key={`dict-${session.currentSegmentIndex}`}>
            <div className="mb-4 flex items-center justify-between gap-3">
              <ListenButton audioEngine={audioEngine} onReplay={session.replaySegment} />
              <span className="text-xs text-zinc-500">
                {session.replayCount > 0 ? `${session.replayCount} kez dinlendi` : 'Sesi dinle, duyduğunu yaz'}
              </span>
            </div>

            <label htmlFor="dictation-input" className="sr-only">
              Duyduğunuz cümleyi yazın
            </label>
            <textarea
              id="dictation-input"
              ref={textareaRef}
              value={session.typedText}
              onChange={(e) => session.setTypedText(e.target.value)}
              onKeyDown={handleDictationKeyDown}
              inputMode="text"
              autoComplete="off"
              autoCorrect="off"
              autoCapitalize="off"
              spellCheck={false}
              rows={3}
              placeholder="Duyduğun cümleyi buraya yaz…"
              className="w-full resize-none rounded-xl border border-white/10 bg-black/30 p-4 font-serif text-xl leading-relaxed text-zinc-50 placeholder:font-sans placeholder:text-base placeholder:text-zinc-600 focus:border-indigo-400/60 focus:outline-none focus:ring-4 focus:ring-indigo-400/10"
            />

            <div className="mt-4 flex flex-wrap items-center justify-between gap-3">
              <Button variant="ghost" onClick={session.giveUp} title="Bilmiyorum, cevabı göster (Ctrl+Enter)">
                <HelpCircle className="h-4 w-4" />
                Bilmiyorum / Göster
              </Button>
              <Button variant="primary" size="lg" onClick={() => session.submitAnswer()} disabled={!session.typedText.trim()}>
                <Check className="h-4 w-4" />
                Kontrol Et
                <Kbd className="border-white/20 bg-white/10 text-indigo-100">Enter</Kbd>
              </Button>
            </div>
          </Card>
        )}

        {/* 1b. Dictating · word by word */}
        {session.state === 'dictating' && session.studyMode === 'word' && (
          <Card key={`word-${session.currentSegmentIndex}`}>
            <div className="mb-4 flex flex-wrap items-center justify-between gap-2">
              <span className="text-xs text-zinc-400">
                Kelime İlerlemesi:{' '}
                <span className="tabular-nums text-zinc-200">
                  {session.currentWordIndex + 1} / {session.targetWords.length}
                </span>
              </span>
              <div className="flex flex-wrap items-center gap-2">
                <ListenButton
                  audioEngine={audioEngine}
                  onReplay={session.replaySegment}
                  label="Cümleyi Dinle"
                  variant="secondary"
                />
                <Button size="sm" variant="ghost" onClick={session.toggleAutoSpeakWord} title="Yeni kelimeye geçince otomatik seslendir">
                  {session.autoSpeakWord ? <Volume2 className="h-3.5 w-3.5" /> : <VolumeX className="h-3.5 w-3.5" />}
                  Oto-Oku: {session.autoSpeakWord ? 'Açık' : 'Kapalı'}
                </Button>
              </div>
            </div>

            {/* Future words are masked: only solved words reach the DOM. */}
            <div className="mb-5 flex min-h-[48px] flex-wrap items-center gap-2 font-serif text-lg">
              {session.targetWords.map((token, idx) => {
                if (idx < session.currentWordIndex) {
                  return (
                    <button
                      type="button"
                      key={idx}
                      onClick={() => session.speakWord(token.clean)}
                      className="rounded-lg bg-emerald-500/10 px-2.5 py-1 text-emerald-200 hover:bg-emerald-500/20 cursor-pointer"
                      title="Dinlemek için tıkla"
                    >
                      {token.raw}
                    </button>
                  )
                }
                if (idx === session.currentWordIndex) {
                  return (
                    <span
                      key={idx}
                      className={cx(
                        'rounded-lg border-2 px-2.5 py-0.5 font-sans text-sm font-semibold',
                        session.wordFeedback === 'incorrect'
                          ? 'border-rose-400/70 text-rose-200 animate-shake'
                          : 'border-indigo-400/70 text-indigo-100'
                      )}
                    >
                      [{idx + 1}. Kelime]
                      {token.punctuation && <span className="ml-0.5">{token.punctuation}</span>}
                    </span>
                  )
                }
                return (
                  <span
                    key={idx}
                    aria-hidden="true"
                    className="select-none rounded-lg bg-white/[0.04] px-2.5 py-1 font-mono text-sm tracking-widest text-zinc-700"
                  >
                    ••••
                  </span>
                )
              })}
            </div>

            <label htmlFor="word-input" className="mb-1.5 block text-xs text-zinc-400">
              {session.currentWordIndex + 1}. kelimeyi yazın
              <span className="text-zinc-600"> · Boşluk veya Enter ile kontrol</span>
            </label>
            <input
              id="word-input"
              ref={wordInputRef}
              type="text"
              inputMode="text"
              enterKeyHint="go"
              value={session.typedWord}
              onChange={(e) => session.setTypedWord(e.target.value)}
              onKeyDown={handleWordKeyDown}
              autoComplete="off"
              autoCorrect="off"
              autoCapitalize="none"
              spellCheck={false}
              placeholder="Kelimeyi buraya yazın…"
              className={cx(
                'h-14 w-full rounded-xl border bg-black/30 px-4 font-serif text-2xl text-zinc-50 placeholder:font-sans placeholder:text-base placeholder:text-zinc-600 focus:outline-none focus:ring-4',
                session.wordFeedback === 'incorrect'
                  ? 'border-rose-400/60 focus:ring-rose-400/10'
                  : 'border-white/10 focus:border-indigo-400/60 focus:ring-indigo-400/10'
              )}
            />
            {session.wordFeedback === 'incorrect' && session.currentWord && (
              <p className="mt-2 text-xs text-rose-300">
                Yanlış kelime, tekrar dene. İpucu: “{session.currentWord.clean.charAt(0).toUpperCase()}” ile
                başlıyor, {session.currentWord.clean.length} harf.
              </p>
            )}

            <div className="mt-4 grid grid-cols-2 gap-2 sm:grid-cols-4">
              <Button variant="primary" onClick={() => session.submitWord()} disabled={!session.typedWord.trim()} className="col-span-2 sm:col-span-1">
                <Check className="h-4 w-4" />
                Kontrol Et
              </Button>
              <Button onClick={session.giveLetterHint} title="Sonraki harfi yaz">
                <Lightbulb className="h-4 w-4 text-amber-300" />
                Harf İpucu Al
              </Button>
              <Button onClick={session.speakCurrentWord} title="Kelimeyi seslendir">
                <Volume2 className="h-4 w-4" />
                Kelimeyi Oku
              </Button>
              <Button variant="ghost" onClick={session.skipWord} title="Kelimeyi atla ve doğrusunu gör (Ctrl+Enter)" className="col-span-2 sm:col-span-1">
                <SkipForward className="h-4 w-4" />
                Bu Kelimeyi Atla
              </Button>
            </div>
            <div className="mt-3 text-right">
              <Button size="sm" variant="ghost" onClick={session.giveUp}>
                Tüm cümleyi göster
              </Button>
            </div>
          </Card>
        )}

        {/* 2. Reviewing: diff + original + correction */}
        {session.state === 'reviewing' && session.diffResult && (
          <>
            <DiffView diff={session.diffResult} />

            <Card>
              <div className="mb-2 flex items-center justify-between gap-3">
                <Eyebrow>Orijinal</Eyebrow>
                <ListenButton audioEngine={audioEngine} onReplay={session.replaySegment} variant="secondary" />
              </div>
              <WordLookupSentence
                text={segment.text}
                lessonId={lesson.lesson_id}
                segmentId={segment.id}
                mistakeRepository={mistakeRepository}
                className="font-serif text-xl leading-relaxed text-zinc-50 sm:text-2xl"
              />
              {segment.translation && <p className="mt-3 text-sm leading-relaxed text-zinc-400">{segment.translation}</p>}
              {segment.notes && <SegmentNote text={segment.notes} />}
            </Card>

            <Card tone="amber">
              <label htmlFor="correction-input" className="mb-2 flex items-center gap-2 text-sm font-medium text-amber-200">
                <RotateCcw className="h-4 w-4" />
                Cümleyi düzelterek yeniden yazın
              </label>
              <input
                id="correction-input"
                ref={correctionInputRef}
                type="text"
                inputMode="text"
                enterKeyHint="done"
                value={session.correctionText}
                onChange={(e) => session.setCorrectionText(e.target.value)}
                onKeyDown={handleCorrectionKeyDown}
                autoComplete="off"
                autoCorrect="off"
                autoCapitalize="off"
                spellCheck={false}
                placeholder="Doğru cümleyi buraya yazın ve Enter'a basın…"
                className="h-12 w-full rounded-xl border border-white/10 bg-black/30 px-4 font-serif text-lg text-zinc-50 placeholder:font-sans placeholder:text-sm placeholder:text-zinc-600 focus:border-amber-300/60 focus:outline-none focus:ring-4 focus:ring-amber-300/10"
              />
              {session.correctionDiff && !session.correctionDiff.isPerfect && (
                <div className="mt-3 space-y-2">
                  <p className="text-xs text-rose-300">Hâlâ eksik ya da yanlış kelimeler var:</p>
                  <DiffView diff={session.correctionDiff} compact />
                </div>
              )}
              <div className="mt-4 flex flex-wrap items-center justify-between gap-2">
                <Button variant="ghost" onClick={session.skipCorrection} title="Düzeltmeyi atla (Ctrl+Enter)">
                  Düzeltmeyi atla <Kbd>Ctrl+Enter</Kbd>
                </Button>
                <Button variant="warning" onClick={() => session.submitCorrection()} disabled={!session.correctionText.trim()}>
                  <Check className="h-4 w-4" />
                  Düzeltmeyi Kontrol Et
                </Button>
              </div>
            </Card>
          </>
        )}

        {/* 3. Shadowing */}
        {session.state === 'shadowing' && (
          <>
            {session.diffResult && <DiffView diff={session.diffResult} compact />}

            <Card tone="indigo">
              <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
                <Eyebrow className="flex items-center gap-1.5 text-indigo-300/80">
                  <Mic className="h-3.5 w-3.5" /> Shadowing / Sesli Tekrar
                </Eyebrow>
                <Button size="sm" variant="ghost" onClick={session.toggleTranslation} title="Çeviriyi aç / kapat (Ctrl+T)">
                  {session.showTranslation ? <EyeOff className="h-3.5 w-3.5" /> : <Eye className="h-3.5 w-3.5" />}
                  {session.showTranslation ? 'Çeviriyi Gizle' : 'Çeviriyi Göster'}
                </Button>
              </div>

              <WordLookupSentence
                text={segment.text}
                lessonId={lesson.lesson_id}
                segmentId={segment.id}
                mistakeRepository={mistakeRepository}
                className="font-serif text-2xl leading-relaxed text-zinc-50 sm:text-3xl"
              />
              <p className="mt-2 text-[11px] text-zinc-600">Anlamını görmek için bir kelimeye dokun.</p>

              {session.showTranslation && segment.translation && (
                <p className="mt-3 text-base leading-relaxed text-indigo-100/80 animate-fade-up">{segment.translation}</p>
              )}
              {segment.notes && <SegmentNote text={segment.notes} />}

              <div className="mt-5 flex flex-wrap items-center gap-3 border-t border-white/[0.06] pt-4">
                <ListenButton audioEngine={audioEngine} onReplay={session.replaySegment} variant="secondary" />
                <p className="text-xs text-zinc-400">Dinle, konuşmacının ritmini ve tonlamasını taklit ederek yüksek sesle tekrar et.</p>
              </div>
            </Card>

            <div className="flex justify-end">
              <Button ref={nextButtonRef} variant="primary" size="lg" onClick={session.nextSegment}>
                {isLastSegment ? 'Dersi Bitir' : 'Sonraki Cümle'}
                <ArrowRight className="h-4 w-4" />
                <Kbd className="border-white/20 bg-white/10 text-indigo-100">Enter</Kbd>
              </Button>
            </div>
          </>
        )}
      </main>

      {/* ─── Settings dock ───────────────────────────────────────────────── */}
      <div className="z-30 mt-2 sm:sticky sm:bottom-3">
        <div className="flex flex-wrap items-center justify-between gap-2 rounded-2xl border border-white/10 bg-zinc-900/85 p-2 shadow-2xl shadow-black/40 backdrop-blur-xl">
          <div className="flex flex-wrap items-center gap-2">
            <button
              type="button"
              onClick={togglePlayback}
              aria-label={audioStatus === 'playing' ? 'Duraklat' : 'Oynat'}
              title="Oynat / duraklat (Ctrl+Space)"
              className="flex h-9 w-9 items-center justify-center rounded-xl bg-white/5 text-zinc-200 hover:bg-white/10 cursor-pointer"
            >
              {audioStatus === 'playing' ? <Pause className="h-4 w-4" /> : <Play className="h-4 w-4" />}
            </button>
            <Segmented<StudyMode>
              ariaLabel="Çalışma modu"
              value={session.studyMode}
              onChange={session.setStudyMode}
              options={[
                { value: 'sentence', label: 'Cümle', title: 'Cümle cümle çalış (Ctrl+M)' },
                { value: 'word', label: 'Kelime', title: 'Kelime kelime çalış (Ctrl+M)' },
              ]}
            />
            <Segmented<number>
              ariaLabel="Oynatma hızı"
              value={speed}
              onChange={handleSpeedChange}
              options={SPEEDS.map((s, i) => ({ value: s, label: `${s}x`, title: `Hız: ${s}x (Ctrl+${i + 1})` }))}
            />
          </div>
          <div className="flex items-center gap-1">
            <button
              type="button"
              onClick={handleToggleAutoPlay}
              aria-pressed={autoPlay}
              title="Yeni cümleye geçince sesi otomatik çal"
              className={cx(
                'h-9 rounded-xl px-3 text-xs font-medium transition-colors cursor-pointer',
                autoPlay ? 'bg-indigo-500/15 text-indigo-200' : 'text-zinc-400 hover:bg-white/5 hover:text-zinc-200'
              )}
            >
              <span className="hidden sm:inline">Otomatik çal: </span>
              <span className="sm:hidden">Oto: </span>
              {autoPlay ? 'Açık' : 'Kapalı'}
            </button>
            {onOpenPdf && (
              <button
                type="button"
                onClick={onOpenPdf}
                aria-pressed={isPdfOpen}
                title="Kitabın PDF'ini aç"
                className={cx(
                  'flex h-9 items-center gap-1.5 rounded-xl px-3 text-xs font-medium transition-colors cursor-pointer',
                  isPdfOpen ? 'bg-white/10 text-white' : 'text-zinc-400 hover:bg-white/5 hover:text-zinc-200'
                )}
              >
                <BookOpen className="h-4 w-4" />
                PDF
              </button>
            )}
            <button
              type="button"
              onClick={() => setShowShortcutsModal(true)}
              aria-label="Klavye kısayolları"
              title="Klavye kısayolları (F1)"
              className="flex h-9 w-9 items-center justify-center rounded-xl text-zinc-400 hover:bg-white/5 hover:text-zinc-200 cursor-pointer"
            >
              <Keyboard className="h-4 w-4" />
            </button>
          </div>
        </div>
      </div>

      {showShortcutsModal && <ShortcutsModal onClose={() => setShowShortcutsModal(false)} />}
    </div>
  )
}

const SegmentNote: React.FC<{ text: string }> = ({ text }) => (
  <p className="mt-4 flex gap-2 rounded-xl bg-amber-400/[0.06] p-3 text-xs leading-relaxed text-amber-100/90">
    <StickyNote className="mt-0.5 h-3.5 w-3.5 shrink-0 text-amber-300" />
    <span>{text}</span>
  </p>
)

/** "12 / 300" indicator that becomes an input to jump to any sentence. */
const SegmentJump: React.FC<{ current: number; total: number; onJump: (index: number) => void }> = ({
  current,
  total,
  onJump,
}) => {
  const [value, setValue] = useState(String(current + 1))
  const commit = () => {
    const n = parseInt(value, 10)
    if (Number.isFinite(n) && n - 1 !== current) onJump(n - 1)
    else setValue(String(current + 1))
  }
  return (
    <span className="flex items-center gap-1 text-xs tabular-nums text-zinc-400">
      <input
        type="number"
        min={1}
        max={total}
        aria-label="Cümleye git"
        title="Cümle numarası yazıp Enter'a bas"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        onBlur={commit}
        onKeyDown={(e) => {
          if (e.key === 'Enter') {
            e.preventDefault()
            commit()
          }
        }}
        className="h-8 w-14 rounded-lg border border-transparent bg-transparent text-center text-zinc-100 [appearance:textfield] hover:border-white/10 focus:border-indigo-400/50 focus:bg-black/30 focus:outline-none [&::-webkit-inner-spin-button]:appearance-none"
      />
      <span>/ {total}</span>
    </span>
  )
}

const SHORTCUTS: Array<[string, string]> = [
  ['Kontrol et · düzelt · sonraki cümle', 'Enter'],
  ['Cevabı göster · düzeltmeyi atla · kelimeyi atla', 'Ctrl + Enter'],
  ['Cümleyi baştan dinle', 'Ctrl + R'],
  ['Oynat / duraklat', 'Ctrl + Space'],
  ['Çeviriyi aç / kapat', 'Ctrl + T'],
  ['Cümle / kelime modu', 'Ctrl + M'],
  ['Hız 0.75x · 1x · 1.25x', 'Ctrl + 1 / 2 / 3'],
  ['Önceki / sonraki cümle', 'PageUp / PageDown'],
  ['Kelime modunda kontrol', 'Boşluk'],
  ['Bu pencere', 'F1'],
]

const ShortcutsModal: React.FC<{ onClose: () => void }> = ({ onClose }) => (
  <div
    role="dialog"
    aria-modal="true"
    aria-label="Klavye kısayolları"
    className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4 backdrop-blur-sm"
    onClick={onClose}
  >
    <div
      className="w-full max-w-md rounded-2xl border border-white/10 bg-zinc-900 p-5 shadow-2xl animate-fade-up"
      onClick={(e) => e.stopPropagation()}
    >
      <div className="mb-3 flex items-center justify-between">
        <h3 className="flex items-center gap-2 font-medium text-zinc-100">
          <Keyboard className="h-4 w-4 text-indigo-300" />
          Klavye kısayolları
        </h3>
        <button type="button" onClick={onClose} aria-label="Kapat" className="rounded-lg p-1 text-zinc-400 hover:bg-white/5 hover:text-zinc-100 cursor-pointer">
          <X className="h-4 w-4" />
        </button>
      </div>
      <ul className="divide-y divide-white/[0.06] text-sm">
        {SHORTCUTS.map(([label, keys]) => (
          <li key={label} className="flex items-center justify-between gap-4 py-2">
            <span className="text-zinc-400">{label}</span>
            <Kbd className="shrink-0 text-[11px]">{keys}</Kbd>
          </li>
        ))}
      </ul>
      <p className="mt-3 text-[11px] text-zinc-500">
        Bir metin alanı odaktayken tek tuş kısayolları devre dışıdır; Ctrl kısayolları her zaman çalışır.
      </p>
    </div>
  </div>
)
