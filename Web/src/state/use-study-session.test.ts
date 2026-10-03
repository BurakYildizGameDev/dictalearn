import { describe, it, expect, vi, beforeEach } from 'vitest'
import { renderHook, act } from '@testing-library/react'
import { useStudySession } from './use-study-session'
import type { Lesson } from '../domain/lessons/types'
import type { AudioEngine } from '../domain/audio/audio-engine'

describe('useStudySession Hook (F1.4)', () => {
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

  beforeEach(() => {
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
    expect(result.current.typedText).toBe('')
  })

  it('plays segment audio when entering dictating with autoPlay true', () => {
    renderHook(() =>
      useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: true })
    )

    expect(mockAudioEngine.playRange).toHaveBeenCalledWith(0, 3000)
  })

  it('submits typed text on submitAnswer and transitions to reviewing', () => {
    const { result } = renderHook(() =>
      useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
    )

    act(() => {
      result.current.setTypedText('he packed his small brown suitcase')
    })

    act(() => {
      result.current.submitAnswer()
    })

    expect(result.current.state).toBe('reviewing')
    expect(result.current.diffResult).toBeDefined()
    expect(result.current.diffResult?.isPerfect).toBe(true)
  })

  it('does nothing on submitAnswer when typed text is empty', () => {
    const { result } = renderHook(() =>
      useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
    )

    act(() => {
      result.current.submitAnswer()
    })

    expect(result.current.state).toBe('dictating')
    expect(result.current.diffResult).toBeNull()
  })

  it('gives up on giveUp, treating all words as missing and moving to reviewing', () => {
    const { result } = renderHook(() =>
      useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
    )

    act(() => {
      result.current.giveUp()
    })

    expect(result.current.state).toBe('reviewing')
    expect(result.current.diffResult).toBeDefined()
    expect(result.current.diffResult?.correctCount).toBe(0)
    expect(result.current.diffResult?.words.every((w) => w.kind === 'missing')).toBe(true)
  })

  it('advances to next segment from reviewing, and then to completed after last segment', () => {
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
    expect(result.current.state).toBe('reviewing')

    act(() => {
      result.current.nextSegment()
    })
    expect(result.current.state).toBe('dictating')
    expect(result.current.currentSegmentIndex).toBe(1)
    expect(result.current.typedText).toBe('')

    // Segment 2 (Last)
    act(() => {
      result.current.setTypedText('The morning cold hit him.')
    })
    act(() => {
      result.current.submitAnswer()
    })
    expect(result.current.state).toBe('reviewing')

    act(() => {
      result.current.nextSegment()
    })
    expect(result.current.state).toBe('completed')
  })

  it('tracks repeat count when replayCurrentSegment is called', () => {
    const { result } = renderHook(() =>
      useStudySession({ lesson: dummyLesson, audioEngine: mockAudioEngine, autoPlay: false })
    )

    expect(result.current.replayCount).toBe(0)

    act(() => {
      result.current.replaySegment()
    })

    expect(result.current.replayCount).toBe(1)
    expect(mockAudioEngine.playRange).toHaveBeenCalledWith(0, 3000)
  })
})
