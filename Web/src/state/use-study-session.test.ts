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
})
