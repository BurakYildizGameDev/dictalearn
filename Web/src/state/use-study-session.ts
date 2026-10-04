import { useState, useCallback, useEffect, useMemo, useRef } from 'react'
import type { Lesson, Segment } from '../domain/lessons/types'
import type { AudioEngine } from '../domain/audio/audio-engine'
import type { DiffOptions, DiffResult } from '../domain/diff/types'
import type { MistakeRepository, MistakeRecord } from '../domain/mistakes/types'
import { computeWordDiff } from '../domain/diff/diff-engine'
import { tokenizeSentenceToWords, checkWordMatch, type WordToken } from '../domain/words/word-mode'
import { pronounce } from '../audio/word-audio'

export type SessionState = 'dictating' | 'reviewing' | 'shadowing' | 'completed'
export type StudyMode = 'sentence' | 'word'

export interface SegmentRecord {
  segmentId: number
  accuracy: number
  replayCount: number
  isPerfect: boolean
}

export interface UseStudySessionProps {
  lesson: Lesson
  audioEngine: AudioEngine
  autoPlay?: boolean
  options?: DiffOptions
  mistakeRepository?: MistakeRepository
  initialStudyMode?: StudyMode
  /** Segment to start from, e.g. restored progress. Clamped to the lesson. */
  initialSegmentIndex?: number
  /** Called whenever the current segment changes (including on mount). */
  onProgress?: (segmentIndex: number) => void
  /** Called once when the last segment is finished. */
  onComplete?: () => void
}

function clampIndex(index: number, total: number): number {
  return Math.min(Math.max(0, Math.floor(index)), Math.max(0, total - 1))
}

export function useStudySession({
  lesson,
  audioEngine,
  autoPlay = true,
  options,
  mistakeRepository,
  initialStudyMode,
  initialSegmentIndex = 0,
  onProgress,
  onComplete,
}: UseStudySessionProps) {
  const [state, setState] = useState<SessionState>('dictating')
  const [currentSegmentIndex, setCurrentSegmentIndex] = useState(() =>
    clampIndex(initialSegmentIndex, lesson.segments.length)
  )
  // Bumped on every fresh attempt so effects (autoplay) re-run even for the same segment.
  const [attemptKey, setAttemptKey] = useState(0)
  const [typedText, setTypedText] = useState('')
  const [correctionText, setCorrectionText] = useState('')
  const [diffResult, setDiffResult] = useState<DiffResult | null>(null)
  const [correctionDiff, setCorrectionDiff] = useState<DiffResult | null>(null)
  const [replayCount, setReplayCount] = useState(0)
  const [sessionRecords, setSessionRecords] = useState<SegmentRecord[]>([])
  const [showTranslation, setShowTranslation] = useState(false)

  const [studyMode, setStudyModeState] = useState<StudyMode>(() => {
    if (initialStudyMode) return initialStudyMode
    try {
      const saved = localStorage.getItem('dictalearn_study_mode')
      if (saved === 'sentence' || saved === 'word') {
        return saved
      }
    } catch {
      // ignore
    }
    return 'sentence'
  })

  const currentSegment: Segment = lesson.segments[currentSegmentIndex] || lesson.segments[0]

  const targetWords: WordToken[] = useMemo(() => {
    return tokenizeSentenceToWords(currentSegment?.text || '')
  }, [currentSegment?.text])

  const [currentWordIndex, setCurrentWordIndex] = useState(0)
  const [typedWord, setTypedWord] = useState('')
  const [wordFeedback, setWordFeedback] = useState<'idle' | 'correct' | 'incorrect'>('idle')
  // Indexes of words missed (wrong at least once, or skipped) in the current sentence.
  const [missedWords, setMissedWords] = useState<ReadonlySet<number>>(() => new Set())
  const wordMistakeCount = missedWords.size

  const onProgressRef = useRef(onProgress)
  const onCompleteRef = useRef(onComplete)
  useEffect(() => {
    onProgressRef.current = onProgress
    onCompleteRef.current = onComplete
  })

  useEffect(() => {
    onProgressRef.current?.(currentSegmentIndex)
  }, [currentSegmentIndex])

  const [autoSpeakWord, setAutoSpeakWordState] = useState<boolean>(() => {
    try {
      const saved = localStorage.getItem('dictalearn_auto_speak_word')
      return saved !== 'false'
    } catch {
      return true
    }
  })

  const setAutoSpeakWord = useCallback((val: boolean) => {
    setAutoSpeakWordState(val)
    try {
      localStorage.setItem('dictalearn_auto_speak_word', String(val))
    } catch {
      // ignore
    }
  }, [])

  const toggleAutoSpeakWord = useCallback(() => {
    setAutoSpeakWord(!autoSpeakWord)
  }, [autoSpeakWord, setAutoSpeakWord])

  const speakCurrentWord = useCallback(() => {
    const target = targetWords[currentWordIndex]
    if (target?.clean) {
      void pronounce(target.clean)
    }
  }, [targetWords, currentWordIndex])

  const speakWord = useCallback((word: string) => {
    void pronounce(word)
  }, [])

  const giveLetterHint = useCallback(() => {
    const target = targetWords[currentWordIndex]
    if (!target?.clean) return

    const clean = target.clean
    const currentLen = typedWord.length
    if (currentLen < clean.length) {
      const nextSlice = clean.slice(0, currentLen + 1)
      setTypedWord(nextSlice)
      setWordFeedback('idle')
    }
  }, [targetWords, currentWordIndex, typedWord])

  const setStudyMode = useCallback((mode: StudyMode) => {
    setStudyModeState(mode)
    try {
      localStorage.setItem('dictalearn_study_mode', mode)
    } catch {
      // ignore
    }
    setCurrentWordIndex(0)
    setTypedWord('')
    setWordFeedback('idle')
    setMissedWords(new Set())
  }, [])

  const toggleStudyMode = useCallback(() => {
    setStudyMode(studyMode === 'sentence' ? 'word' : 'sentence')
  }, [studyMode, setStudyMode])

  useEffect(() => {
    if (state !== 'dictating' || studyMode !== 'word' || !autoSpeakWord) return
    // The first word would talk over the sentence audio that autoplay just started.
    if (currentWordIndex === 0 && autoPlay) return
    speakCurrentWord()
  }, [state, studyMode, currentWordIndex, autoSpeakWord, autoPlay, speakCurrentWord])

  const playCurrentSegment = useCallback(() => {
    if (currentSegment) {
      audioEngine.playRange(currentSegment.start_ms, currentSegment.end_ms).catch(() => {})
    }
  }, [audioEngine, currentSegment])

  useEffect(() => {
    if (state === 'dictating' && autoPlay) {
      playCurrentSegment()
    }
  }, [state, currentSegmentIndex, attemptKey, autoPlay, playCurrentSegment])

  const replaySegment = useCallback(() => {
    setReplayCount((prev) => prev + 1)
    playCurrentSegment()
  }, [playCurrentSegment])

  // Log mistakes to repository on initial attempt only
  const logMistakes = useCallback(
    (diff: DiffResult) => {
      if (!mistakeRepository || diff.isPerfect) return

      const mistakesToLog: MistakeRecord[] = []
      const timestamp = new Date().toISOString()

      for (const word of diff.words) {
        if (word.kind === 'substitute' && word.expected) {
          mistakesToLog.push({
            word: word.expected.replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}]+$/gu, ''),
            kind: 'substitute',
            typed: word.typed,
            lesson_id: lesson.lesson_id,
            segment_id: currentSegment.id,
            at: timestamp,
          })
        } else if (word.kind === 'missing' && word.expected) {
          mistakesToLog.push({
            word: word.expected.replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}]+$/gu, ''),
            kind: 'missing',
            lesson_id: lesson.lesson_id,
            segment_id: currentSegment.id,
            at: timestamp,
          })
        }
      }

      mistakeRepository.addMistakes(mistakesToLog)
    },
    [mistakeRepository, lesson.lesson_id, currentSegment.id]
  )

  const submitAnswer = useCallback(
    (overrideText?: string) => {
      if (state !== 'dictating') return

      const textToSubmit = overrideText !== undefined ? overrideText : typedText
      const trimmed = textToSubmit.trim()
      if (!trimmed) return

      const diff = computeWordDiff(currentSegment.text, trimmed, options)
      setDiffResult(diff)
      logMistakes(diff)

      setSessionRecords((prev) => [
        ...prev,
        {
          segmentId: currentSegment.id,
          accuracy: diff.accuracy,
          replayCount,
          isPerfect: diff.isPerfect,
        },
      ])

      if (diff.isPerfect) {
        // Perfect sentence goes straight to shadowing
        setState('shadowing')
      } else {
        // Has mistakes: goes to reviewing for correction
        setCorrectionText('')
        setCorrectionDiff(null)
        setState('reviewing')
      }
    },
    [state, typedText, currentSegment, options, replayCount, logMistakes]
  )

  const giveUp = useCallback(() => {
    if (state !== 'dictating') return

    // In word mode the words already solved count as typed.
    const typedSoFar =
      studyMode === 'word'
        ? targetWords
            .slice(0, currentWordIndex)
            .map((w) => w.raw)
            .join(' ')
        : ''
    const diff = computeWordDiff(currentSegment.text, typedSoFar, options)
    setDiffResult(diff)
    logMistakes(diff)

    setSessionRecords((prev) => [
      ...prev,
      {
        segmentId: currentSegment.id,
        accuracy: diff.accuracy,
        replayCount,
        isPerfect: false,
      },
    ])

    setCorrectionText('')
    setCorrectionDiff(null)
    setState('reviewing')
  }, [state, studyMode, targetWords, currentWordIndex, currentSegment, options, replayCount, logMistakes])

  // Submit correction attempt in reviewing state
  const submitCorrection = useCallback(
    (overrideText?: string) => {
      if (state !== 'reviewing') return

      const text = overrideText !== undefined ? overrideText : correctionText
      const trimmed = text.trim()
      if (!trimmed) return

      const diff = computeWordDiff(currentSegment.text, trimmed, options)
      setCorrectionDiff(diff)

      if (diff.isPerfect) {
        // Successfully corrected: advance to shadowing
        setState('shadowing')
      }
    },
    [state, correctionText, currentSegment.text, options]
  )

  // Skip correction (Ctrl+Enter during reviewing)
  const skipCorrection = useCallback(() => {
    if (state === 'reviewing') {
      setState('shadowing')
    }
  }, [state])

  const toggleTranslation = useCallback(() => {
    setShowTranslation((prev) => !prev)
  }, [])

  // Word-by-Word Mode Actions (Faz 6)

  // Marks a word as missed once; later wrong attempts on the same word are not re-counted.
  const markWordMissed = useCallback(
    (index: number, kind: 'substitute' | 'missing', typed: string) => {
      if (missedWords.has(index)) return missedWords
      const next = new Set(missedWords).add(index)
      setMissedWords(next)
      const target = targetWords[index]
      if (mistakeRepository && target) {
        mistakeRepository.addMistakes([
          {
            word: target.clean,
            kind,
            typed: typed || undefined,
            lesson_id: lesson.lesson_id,
            segment_id: currentSegment.id,
            at: new Date().toISOString(),
          },
        ])
      }
      return next
    },
    [missedWords, targetWords, mistakeRepository, lesson.lesson_id, currentSegment.id]
  )

  // Advances to the next word or, after the last one, finishes the sentence.
  const advanceWord = useCallback(
    (missed: ReadonlySet<number>) => {
      setTypedWord('')
      const nextIdx = currentWordIndex + 1
      if (nextIdx < targetWords.length) {
        setCurrentWordIndex(nextIdx)
        return
      }
      const total = targetWords.length || 1
      setDiffResult(computeWordDiff(currentSegment.text, currentSegment.text, options))
      setSessionRecords((prev) => [
        ...prev,
        {
          segmentId: currentSegment.id,
          accuracy: Math.max(0, (total - missed.size) / total),
          replayCount,
          isPerfect: missed.size === 0,
        },
      ])
      setState('shadowing')
    },
    [currentWordIndex, targetWords.length, currentSegment, options, replayCount]
  )

  const submitWord = useCallback(
    (overrideWord?: string): boolean => {
      if (state !== 'dictating' || studyMode !== 'word') return false

      const wordToTest = overrideWord !== undefined ? overrideWord : typedWord
      const target = targetWords[currentWordIndex]
      if (!target || !wordToTest.trim()) return false

      if (checkWordMatch(wordToTest, target.clean)) {
        setWordFeedback('correct')
        advanceWord(missedWords)
        return true
      }
      setWordFeedback('incorrect')
      markWordMissed(currentWordIndex, 'substitute', wordToTest.trim())
      return false
    },
    [state, studyMode, typedWord, targetWords, currentWordIndex, missedWords, advanceWord, markWordMissed]
  )

  const skipWord = useCallback(() => {
    if (state !== 'dictating' || studyMode !== 'word') return
    if (!targetWords[currentWordIndex]) return

    const missed = markWordMissed(currentWordIndex, 'missing', typedWord.trim())
    setWordFeedback('idle')
    advanceWord(missed)
  }, [state, studyMode, targetWords, currentWordIndex, typedWord, markWordMissed, advanceWord])

  // Resets everything that belongs to a single attempt and lands in dictating.
  const goToSegment = useCallback(
    (index: number) => {
      setCurrentSegmentIndex(clampIndex(index, lesson.segments.length))
      setTypedText('')
      setCorrectionText('')
      setDiffResult(null)
      setCorrectionDiff(null)
      setReplayCount(0)
      setShowTranslation(false)
      setCurrentWordIndex(0)
      setTypedWord('')
      setWordFeedback('idle')
      setMissedWords(new Set())
      setAttemptKey((k) => k + 1)
      setState('dictating')
    },
    [lesson.segments.length]
  )

  const nextSegment = useCallback(() => {
    const isLast = currentSegmentIndex >= lesson.segments.length - 1
    if (isLast) {
      audioEngine.pause()
      setState('completed')
      onCompleteRef.current?.()
    } else {
      goToSegment(currentSegmentIndex + 1)
    }
  }, [currentSegmentIndex, lesson.segments.length, goToSegment, audioEngine])

  /** PageDown: jump forward without finishing the lesson. */
  const skipSegment = useCallback(() => {
    if (currentSegmentIndex < lesson.segments.length - 1) {
      goToSegment(currentSegmentIndex + 1)
    }
  }, [currentSegmentIndex, lesson.segments.length, goToSegment])

  /** PageUp: go back one segment. */
  const previousSegment = useCallback(() => {
    if (currentSegmentIndex > 0) {
      goToSegment(currentSegmentIndex - 1)
    }
  }, [currentSegmentIndex, goToSegment])

  const restart = useCallback(() => {
    setSessionRecords([])
    goToSegment(0)
  }, [goToSegment])

  return {
    state,
    currentSegmentIndex,
    currentSegment,
    totalSegments: lesson.segments.length,
    typedText,
    setTypedText,
    correctionText,
    setCorrectionText,
    diffResult,
    correctionDiff,
    replayCount,
    sessionRecords,
    showTranslation,
    toggleTranslation,
    submitAnswer,
    giveUp,
    submitCorrection,
    skipCorrection,
    nextSegment,
    skipSegment,
    previousSegment,
    goToSegment,
    restart,
    replaySegment,
    playCurrentSegment,
    // Word-by-Word Mode additions
    studyMode,
    setStudyMode,
    toggleStudyMode,
    targetWords,
    currentWordIndex,
    currentWord: targetWords[currentWordIndex],
    typedWord,
    setTypedWord,
    wordFeedback,
    wordMistakeCount,
    submitWord,
    skipWord,
    autoSpeakWord,
    setAutoSpeakWord,
    toggleAutoSpeakWord,
    speakCurrentWord,
    speakWord,
    giveLetterHint,
  }
}
