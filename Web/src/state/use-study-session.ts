import { useState, useCallback, useEffect } from 'react'
import type { Lesson, Segment } from '../domain/lessons/types'
import type { AudioEngine } from '../domain/audio/audio-engine'
import type { DiffOptions, DiffResult } from '../domain/diff/types'
import { computeWordDiff } from '../domain/diff/diff-engine'

export type SessionState = 'dictating' | 'reviewing' | 'shadowing' | 'completed'

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
}

export function useStudySession({
  lesson,
  audioEngine,
  autoPlay = true,
  options,
}: UseStudySessionProps) {
  const [state, setState] = useState<SessionState>('dictating')
  const [currentSegmentIndex, setCurrentSegmentIndex] = useState(0)
  const [typedText, setTypedText] = useState('')
  const [diffResult, setDiffResult] = useState<DiffResult | null>(null)
  const [replayCount, setReplayCount] = useState(0)
  const [sessionRecords, setSessionRecords] = useState<SegmentRecord[]>([])

  const currentSegment: Segment = lesson.segments[currentSegmentIndex] || lesson.segments[0]

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

  const submitAnswer = useCallback((overrideText?: string) => {
    if (state !== 'dictating') return

    const textToSubmit = overrideText !== undefined ? overrideText : typedText
    const trimmed = textToSubmit.trim()
    if (!trimmed) {
      // Empty enter does nothing according to PLAN §4.1
      return
    }

    const diff = computeWordDiff(currentSegment.text, trimmed, options)
    setDiffResult(diff)
    setState('reviewing')

    setSessionRecords((prev) => [
      ...prev,
      {
        segmentId: currentSegment.id,
        accuracy: diff.accuracy,
        replayCount,
        isPerfect: diff.isPerfect,
      },
    ])
  }, [state, typedText, currentSegment, options, replayCount])

  const giveUp = useCallback(() => {
    if (state !== 'dictating' && state !== 'reviewing') return

    // All words marked missing
    const diff = computeWordDiff(currentSegment.text, '', options)
    setDiffResult(diff)
    setState('reviewing')

    setSessionRecords((prev) => [
      ...prev,
      {
        segmentId: currentSegment.id,
        accuracy: 0,
        replayCount,
        isPerfect: false,
      },
    ])
  }, [state, currentSegment, options, replayCount])

  const nextSegment = useCallback(() => {
    if (state !== 'reviewing' && state !== 'shadowing') return

    const isLast = currentSegmentIndex >= lesson.segments.length - 1
    if (isLast) {
      setState('completed')
    } else {
      setCurrentSegmentIndex((prev) => prev + 1)
      setTypedText('')
      setDiffResult(null)
      setReplayCount(0)
      setState('dictating')
    }
  }, [state, currentSegmentIndex, lesson.segments.length])

  return {
    state,
    currentSegmentIndex,
    currentSegment,
    totalSegments: lesson.segments.length,
    typedText,
    setTypedText,
    diffResult,
    replayCount,
    sessionRecords,
    submitAnswer,
    giveUp,
    nextSegment,
    replaySegment,
  }
}
