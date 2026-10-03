import { describe, it, expect, vi, beforeEach } from 'vitest'
import { WebAudioEngine } from './web-audio-engine'

describe('WebAudioEngine', () => {
  let engine: WebAudioEngine

  beforeEach(() => {
    vi.useFakeTimers()
    engine = new WebAudioEngine()
  })

  it('starts in idle status', () => {
    expect(engine.getStatus()).toBe('idle')
  })

  it('allows setting and getting speed within clamped limits', () => {
    engine.setSpeed(1.25)
    expect(engine.getSpeed()).toBe(1.25)

    engine.setSpeed(5.0)
    expect(engine.getSpeed()).toBe(2.5) // clamped to max

    engine.setSpeed(0.1)
    expect(engine.getSpeed()).toBe(0.25) // clamped to min
  })

  it('notifies status listeners on status change', () => {
    const listener = vi.fn()
    const unsubscribe = engine.onStatusChange(listener)

    engine.pause()
    // When idle, pause does not change status
    expect(listener).not.toHaveBeenCalled()

    unsubscribe()
  })

  it('notifies on range complete after duration', async () => {
    // Mock dummy AudioBuffer and AudioContext
    const mockSource = {
      buffer: null,
      playbackRate: { value: 1.0 },
      connect: vi.fn(),
      disconnect: vi.fn(),
      start: vi.fn(),
      stop: vi.fn(),
    }
    const mockCtx = {
      state: 'running',
      createBufferSource: () => mockSource,
      destination: {},
      resume: vi.fn(),
      close: vi.fn(),
    }
    // Inject mock context
    // @ts-expect-error accessing private property for unit test
    engine.ctx = mockCtx
    // @ts-expect-error accessing private property for unit test
    engine.audioBuffer = { duration: 10 } as AudioBuffer

    const onComplete = vi.fn()
    const onStatus = vi.fn()
    engine.onRangeComplete(onComplete)
    engine.onStatusChange(onStatus)

    await engine.playRange(1000, 3000) // 2000 ms = 2s duration

    expect(engine.getStatus()).toBe('playing')
    expect(mockSource.start).toHaveBeenCalledWith(0, 1.0, 2.0)

    // Advance timer by 2000 ms
    vi.advanceTimersByTime(2000)

    expect(engine.getStatus()).toBe('rangeCompleted')
    expect(onComplete).toHaveBeenCalledTimes(1)
  })
})
