import { useState, useCallback, useEffect, useMemo } from 'react'
import type { Lesson, Segment } from '../domain/lessons/types'
import type { AudioEngine } from '../domain/audio/audio-engine'
import type { DiffOptions, DiffResult } from '../domain/diff/types'
import type { MistakeRepository, MistakeRecord } from '../domain/mistakes/types'
import { computeWordDiff } from '../domain/diff/diff-engine'
import { tokenizeSentenceToWords, checkWordMatch, type WordToken } from '../domain/words/word-mode'

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
}

export function useStudySession({
  lesson,
  audioEngine,
  autoPlay = true,
  options,
  mistakeRepository,
  initialStudyMode,
}: UseStudySessionProps) {
  const [state, setState] = useState<SessionState>('dictating')
  const [currentSegmentIndex, setCurrentSegmentIndex] = useState(0)
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
  const [wordMistakeCount, setWordMistakeCount] = useState(0)

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
    setWordMistakeCount(0)
  }, [])

  const toggleStudyMode = useCallback(() => {
    setStudyMode(studyMode === 'sentence' ? 'word' : 'sentence')
  }, [studyMode, setStudyMode])

  const playCurrentSegment = useCallback(() => {
    if (currentSegment) {
      audioEngine.playRange(currentSegment.start_ms, currentSegment.end_ms).catch(() => {})
    }
  }, [audioEngine, currentSegment])

  useEffect(() => {
    if (state === 'dictating' && autoPlay) {
      playCurrentSegment()
    }
  }, [state, currentSegmentIndex, autoPlay, playCurrentSegment])

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
    if (state !== 'dictating' && state !== 'reviewing') return

    const diff = computeWordDiff(currentSegment.text, '', options)
    setDiffResult(diff)
    logMistakes(diff)

    setSessionRecords((prev) => [
      ...prev,
      {
        segmentId: currentSegment.id,
        accuracy: 0,
        replayCount,
        isPerfect: false,
      },
    ])

    setCorrectionText('')
    setCorrectionDiff(null)
    setState('reviewing')
  }, [state, currentSegment, options, replayCount, logMistakes])

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
  const submitWord = useCallback(
    (overrideWord?: string): boolean => {
      if (state !== 'dictating' || studyMode !== 'word') return false

      const wordToTest = overrideWord !== undefined ? overrideWord : typedWord
      const target = targetWords[currentWordIndex]
      if (!target) return false

      const isMatch = checkWordMatch(wordToTest, target.clean)
      if (isMatch) {
        setWordFeedback('correct')
        setTypedWord('')

        const nextIdx = currentWordIndex + 1
        if (nextIdx >= targetWords.length) {
          // Entire sentence completed via word-by-word!
          const isPerfect = wordMistakeCount === 0
          const accuracy = isPerfect
            ? 1
            : Math.max(0, (targetWords.length - wordMistakeCount) / targetWords.length)
          const diff = computeWordDiff(currentSegment.text, currentSegment.text, options)
          setDiffResult(diff)
          setSessionRecords((prev) => [
            ...prev,
            {
              segmentId: currentSegment.id,
              accuracy,
              replayCount,
              isPerfect,
            },
          ])
          setState('shadowing')
        } else {
          setCurrentWordIndex(nextIdx)
        }
        return true
      } else {
        setWordFeedback('incorrect')
        setWordMistakeCount((prev) => prev + 1)
        if (mistakeRepository) {
          mistakeRepository.addMistakes([
            {
              word: target.clean,
              kind: 'substitute',
              typed: wordToTest,
              lesson_id: lesson.lesson_id,
              segment_id: currentSegment.id,
              at: new Date().toISOString(),
            },
          ])
        }
        return false
      }
    },
    [
      state,
      studyMode,
      typedWord,
      targetWords,
      currentWordIndex,
      wordMistakeCount,
      currentSegment,
      options,
      replayCount,
      mistakeRepository,
      lesson.lesson_id,
    ]
  )

  const skipWord = useCallback(() => {
    if (state !== 'dictating' || studyMode !== 'word') return

    const target = targetWords[currentWordIndex]
    if (!target) return

    const newMistakes = wordMistakeCount + 1
    setWordMistakeCount(newMistakes)
    if (mistakeRepository) {
      mistakeRepository.addMistakes([
        {
          word: target.clean,
          kind: 'missing',
          typed: typedWord,
          lesson_id: lesson.lesson_id,
          segment_id: currentSegment.id,
          at: new Date().toISOString(),
        },
      ])
    }

    setTypedWord('')
    setWordFeedback('idle')
    const nextIdx = currentWordIndex + 1
    if (nextIdx >= targetWords.length) {
      const accuracy = Math.max(0, (targetWords.length - newMistakes) / targetWords.length)
      const diff = computeWordDiff(currentSegment.text, currentSegment.text, options)
      setDiffResult(diff)
      setSessionRecords((prev) => [
        ...prev,
        {
          segmentId: currentSegment.id,
          accuracy,
          replayCount,
          isPerfect: false,
        },
      ])
      setState('shadowing')
    } else {
      setCurrentWordIndex(nextIdx)
    }
  }, [
    state,
    studyMode,
    targetWords,
    currentWordIndex,
    wordMistakeCount,
    typedWord,
    mistakeRepository,
    lesson.lesson_id,
    currentSegment,
    options,
    replayCount,
  ])

  const nextSegment = useCallback(() => {
    // Can advance from reviewing or shadowing
    const isLast = currentSegmentIndex >= lesson.segments.length - 1
    if (isLast) {
      setState('completed')
    } else {
      setCurrentSegmentIndex((prev) => prev + 1)
      setTypedText('')
      setCorrectionText('')
      setDiffResult(null)
      setCorrectionDiff(null)
      setReplayCount(0)
      setShowTranslation(false)
      setCurrentWordIndex(0)
      setTypedWord('')
      setWordFeedback('idle')
      setWordMistakeCount(0)
      setState('dictating')
    }
  }, [currentSegmentIndex, lesson.segments.length])

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
    replaySegment,
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
  }
}
