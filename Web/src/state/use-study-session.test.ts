import { describe, it, expect, vi, beforeEach } from 'vitest'
import { renderHook, act } from '@testing-library/react'
import { useStudySession } from './use-study-session'
import type { Lesson } from '../domain/lessons/types'
import type { AudioEngine } from '../domain/audio/audio-engine'
import type { MistakeRepository, MistakeRecord } from '../domain/mistakes/types'

describe('useStudySession Hook (Phase 3 Full 4-Step Cycle)', () => {
  const dummyLesson: Lesson = {
    schema_version: 1,
    lesson_id: 'test_ch01',
    title: 'Test Lesson',
    source_lang: 'en',
    target_lang: 'tr',
    audio_file: 'audio.wav',
    segments: [
      {
        id: 1,
        start_ms: 0,
        end_ms: 3000,
        text: 'He packed his small brown suitcase.',
        translation: 'Küçük bavulunu topladı.',
      },
      {
        id: 2,
        start_ms: 3500,
        end_ms: 6000,
        text: 'The morning cold hit him.',
        translation: 'Sabah soğuğu yüzüne çarptı.',
      },
    ],
  }

  let mockAudioEngine: AudioEngine
  let mockMistakeRepo: MistakeRepository
  let loggedMistakes: MistakeRecord[]

  beforeEach(() => {
    loggedMistakes = []
    mockMistakeRepo = {
      getMistakes: () => loggedMistakes,
      addMistakes: (m) => loggedMistakes.push(...m),
      clearMistakes: () => { loggedMistakes = [] },
      getWordFrequencies: () => ({}),
    }

    mockAudioEngine = {
      load: vi.fn().mockResolvedValue(undefined),
      playRange: vi.fn().mockResolvedValue(undefined),
      pause: vi.fn(),
      resume: vi.fn(),
      setSpeed: vi.fn(),
      getSpeed: vi.fn().mockReturnValue(1.0),
      getStatus: vi.fn().mockReturnValue('idle'),
      onRangeComplete: vi.fn().mockReturnValue(() => {}),
      onStatusChange: vi.fn().mockReturnValue(() => {}),
      dispose: vi.fn(),
    }
  })

  it('starts in dictating state on the first segment', () => {
    const { result } = renderHook(() =>
      useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
    )

    expect(result.current.state).toBe('dictating')
    expect(result.current.currentSegmentIndex).toBe(0)
    expect(result.current.currentSegment.id).toBe(1)
  })

  it('transitions directly to shadowing when answer is perfect', () => {
    const { result } = renderHook(() =>
      useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
    )

    act(() => {
      result.current.setTypedText('He packed his small brown suitcase.')
    })
    act(() => {
      result.current.submitAnswer()
    })

    expect(result.current.state).toBe('shadowing')
    expect(result.current.diffResult?.isPerfect).toBe(true)
  })

  it('transitions to reviewing when answer has mistakes, and logs mistakes to repo', () => {
    const { result } = renderHook(() =>
      useStudySession({
        lesson: dummyLesson,
        audioEngine: mockAudioEngine,
        autoPlay: false,
        mistakeRepository: mockMistakeRepo,
      })
    )

    act(() => {
      result.current.setTypedText('He packed his brown suitcase.') // missing "small"
    })
    act(() => {
      result.current.submitAnswer()
    })

    expect(result.current.state).toBe('reviewing')
    expect(result.current.diffResult?.isPerfect).toBe(false)
    expect(loggedMistakes.length).toBeGreaterThan(0)
    expect(loggedMistakes[0].word).toBe('small')
  })

  it('correction flow: user retries in reviewing, succeeds, and enters shadowing (F3.1)', () => {
    const { result } = renderHook(() =>
      useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
    )

    act(() => {
      result.current.setTypedText('He packed his brown suitcase')
    })
    act(() => {
      result.current.submitAnswer()
    })
    expect(result.current.state).toBe('reviewing')

    // Wrong correction attempt
    act(() => {
      result.current.setCorrectionText('He packed suitcase')
    })
    act(() => {
      result.current.submitCorrection()
    })
    expect(result.current.state).toBe('reviewing')

    // Correct correction attempt
    act(() => {
      result.current.setCorrectionText('He packed his small brown suitcase.')
    })
    act(() => {
      result.current.submitCorrection()
    })
    expect(result.current.state).toBe('shadowing')
  })

  it('skipping correction transitions from reviewing to shadowing', () => {
    const { result } = renderHook(() =>
      useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
    )

    act(() => {
      result.current.giveUp()
    })
    expect(result.current.state).toBe('reviewing')

    act(() => {
      result.current.skipCorrection()
    })
    expect(result.current.state).toBe('shadowing')
  })

  it('toggles translation in shadowing state (F3.2)', () => {
    const { result } = renderHook(() =>
      useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
    )

    expect(result.current.showTranslation).toBe(false)
    act(() => {
      result.current.toggleTranslation()
    })
    expect(result.current.showTranslation).toBe(true)
  })

  it('advances through segments to completed', () => {
    const { result } = renderHook(() =>
      useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
    )

    // Segment 1
    act(() => {
      result.current.setTypedText('He packed his small brown suitcase.')
    })
    act(() => {
      result.current.submitAnswer()
    })
    expect(result.current.state).toBe('shadowing')

    act(() => {
      result.current.nextSegment()
    })
    expect(result.current.state).toBe('dictating')
    expect(result.current.currentSegmentIndex).toBe(1)

    // Segment 2
    act(() => {
      result.current.setTypedText('The morning cold hit him.')
    })
    act(() => {
      result.current.submitAnswer()
    })
    expect(result.current.state).toBe('shadowing')

    act(() => {
      result.current.nextSegment()
    })
    expect(result.current.state).toBe('completed')
  })

  it('handles word-by-word mode: step-by-step word checking and completion', () => {
    const { result } = renderHook(() =>
      useStudySession({
        lesson: dummyLesson,
        audioEngine: mockAudioEngine,
        autoPlay: false,
        initialStudyMode: 'word',
      })
    )

    expect(result.current.studyMode).toBe('word')
    expect(result.current.targetWords).toHaveLength(6) // "He packed his small brown suitcase."
    expect(result.current.currentWordIndex).toBe(0)
    expect(result.current.currentWord?.clean).toBe('he')

    // 1. Wrong word attempt
    act(() => {
      result.current.setTypedWord('she')
    })
    let success = false
    act(() => {
      success = result.current.submitWord()
    })
    expect(success).toBe(false)
    expect(result.current.wordFeedback).toBe('incorrect')
    expect(result.current.currentWordIndex).toBe(0)

    // 2. Correct word 1: "he"
    act(() => {
      result.current.setTypedWord('He')
    })
    act(() => {
      success = result.current.submitWord()
    })
    expect(success).toBe(true)
    expect(result.current.wordFeedback).toBe('correct')
    expect(result.current.currentWordIndex).toBe(1)
    expect(result.current.currentWord?.clean).toBe('packed')

    // 3. Skip word 2: "packed"
    act(() => {
      result.current.skipWord()
    })
    expect(result.current.currentWordIndex).toBe(2)
    expect(result.current.currentWord?.clean).toBe('his')

    // 4. Complete remaining words: "his", "small", "brown", "suitcase"
    act(() => { result.current.submitWord('his') })
    act(() => { result.current.submitWord('small') })
    act(() => { result.current.submitWord('brown') })
    act(() => { result.current.submitWord('suitcase') })

    // When the last word is submitted, transitions to shadowing!
    expect(result.current.state).toBe('shadowing')
    expect(result.current.sessionRecords).toHaveLength(1)
  })

  describe('bug fixes & navigation', () => {
    it('giveUp is ignored outside dictating so records are not duplicated', () => {
      const { result } = renderHook(() =>
        useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
      )
      act(() => result.current.giveUp())
      act(() => result.current.giveUp())
      expect(result.current.state).toBe('reviewing')
      expect(result.current.sessionRecords).toHaveLength(1)
    })

    it('word mode: repeated wrong attempts on one word count as a single mistake', () => {
      const { result } = renderHook(() =>
        useStudySession({
          lesson: dummyLesson,
          audioEngine: mockAudioEngine,
          autoPlay: false,
          initialStudyMode: 'word',
          mistakeRepository: mockMistakeRepo,
        })
      )
      act(() => { result.current.submitWord('she') })
      act(() => { result.current.submitWord('the') })
      act(() => { result.current.submitWord('we') })
      expect(result.current.wordMistakeCount).toBe(1)
      expect(loggedMistakes).toHaveLength(1)

      for (const w of ['he', 'packed', 'his', 'small', 'brown', 'suitcase']) {
        act(() => { result.current.submitWord(w) })
      }
      expect(result.current.state).toBe('shadowing')
      const record = result.current.sessionRecords[0]
      expect(record.isPerfect).toBe(false)
      expect(record.accuracy).toBeCloseTo(5 / 6)
    })

    it('word mode: giving up keeps the words already typed correctly', () => {
      const { result } = renderHook(() =>
        useStudySession({
          lesson: dummyLesson,
          audioEngine: mockAudioEngine,
          autoPlay: false,
          initialStudyMode: 'word',
        })
      )
      act(() => { result.current.submitWord('he') })
      act(() => { result.current.submitWord('packed') })
      act(() => result.current.giveUp())

      expect(result.current.state).toBe('reviewing')
      expect(result.current.diffResult?.correctCount).toBe(2)
      expect(result.current.sessionRecords[0].accuracy).toBeCloseTo(2 / 6)
    })

    it('starts from initialSegmentIndex (resume progress)', () => {
      const { result } = renderHook(() =>
        useStudySession({
          lesson: dummyLesson,
          audioEngine: mockAudioEngine,
          autoPlay: false,
          initialSegmentIndex: 1,
        })
      )
      expect(result.current.currentSegmentIndex).toBe(1)
      expect(result.current.currentSegment.id).toBe(2)
    })

    it('clamps an out-of-range initialSegmentIndex', () => {
      const { result } = renderHook(() =>
        useStudySession({
          lesson: dummyLesson,
          audioEngine: mockAudioEngine,
          autoPlay: false,
          initialSegmentIndex: 99,
        })
      )
      expect(result.current.currentSegmentIndex).toBe(1)
    })

    it('goToSegment jumps from any state and resets the attempt', () => {
      const { result } = renderHook(() =>
        useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
      )
      act(() => result.current.setTypedText('He packed'))
      act(() => result.current.submitAnswer())
      expect(result.current.state).toBe('reviewing')

      act(() => result.current.goToSegment(1))
      expect(result.current.state).toBe('dictating')
      expect(result.current.currentSegmentIndex).toBe(1)
      expect(result.current.typedText).toBe('')
      expect(result.current.diffResult).toBeNull()

      act(() => result.current.goToSegment(-5))
      expect(result.current.currentSegmentIndex).toBe(0)
    })

    it('previousSegment / skipSegment navigate without completing the lesson', () => {
      const { result } = renderHook(() =>
        useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
      )
      act(() => result.current.skipSegment())
      expect(result.current.currentSegmentIndex).toBe(1)
      act(() => result.current.skipSegment()) // already last: stays
      expect(result.current.currentSegmentIndex).toBe(1)
      expect(result.current.state).toBe('dictating')
      act(() => result.current.previousSegment())
      expect(result.current.currentSegmentIndex).toBe(0)
    })

    it('reports progress changes and completion', () => {
      const onProgress = vi.fn()
      const onComplete = vi.fn()
      const { result } = renderHook(() =>
        useStudySession({
          lesson: dummyLesson,
          audioEngine: mockAudioEngine,
          autoPlay: false,
          onProgress,
          onComplete,
        })
      )
      act(() => result.current.giveUp())
      act(() => result.current.skipCorrection())
      act(() => result.current.nextSegment())
      expect(onProgress).toHaveBeenLastCalledWith(1)

      act(() => result.current.giveUp())
      act(() => result.current.skipCorrection())
      act(() => result.current.nextSegment())
      expect(result.current.state).toBe('completed')
      expect(onComplete).toHaveBeenCalledTimes(1)
    })

    it('restart returns to the first segment with a clean session', () => {
      const { result } = renderHook(() =>
        useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
      )
      act(() => result.current.giveUp())
      act(() => result.current.skipCorrection())
      act(() => result.current.nextSegment())
      act(() => result.current.restart())
      expect(result.current.currentSegmentIndex).toBe(0)
      expect(result.current.state).toBe('dictating')
      expect(result.current.sessionRecords).toHaveLength(0)
    })
  })

  it('reports every first-attempt result through onRecord', () => {
    const onRecord = vi.fn()
    const { result } = renderHook(() =>
      useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false, onRecord })
    )
    act(() => result.current.setTypedText('He packed his'))
    act(() => result.current.submitAnswer())
    // the correction attempt is not a new record
    act(() => result.current.setCorrectionText('He packed his small brown suitcase.'))
    act(() => result.current.submitCorrection())
    expect(onRecord).toHaveBeenCalledTimes(1)
    expect(onRecord.mock.calls[0][0]).toMatchObject({ segmentId: 1, isPerfect: false })
    expect(onRecord.mock.calls[0][0].accuracy).toBeLessThan(0.7)
  })
})
