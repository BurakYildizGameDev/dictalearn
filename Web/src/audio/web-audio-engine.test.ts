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

  describe('HTMLAudioElement path', () => {
    function fakeAudio() {
      const audio = {
        currentTime: 0,
        playbackRate: 1,
        preservesPitch: false,
        ended: false,
        play: vi.fn().mockResolvedValue(undefined),
        pause: vi.fn(),
        removeAttribute: vi.fn(),
      }
      // @ts-expect-error inject fake element into private field
      engine.audioElement = audio
      return audio
    }

    it('stops exactly when currentTime passes the range end', async () => {
      const audio = fakeAudio()
      const onComplete = vi.fn()
      engine.onRangeComplete(onComplete)

      await engine.playRange(1000, 3000)
      expect(audio.currentTime).toBe(1)
      expect(engine.getStatus()).toBe('playing')

      audio.currentTime = 2.5
      vi.advanceTimersByTime(30)
      expect(onComplete).not.toHaveBeenCalled()

      audio.currentTime = 3.0
      vi.advanceTimersByTime(30)
      expect(onComplete).toHaveBeenCalledTimes(1)
      expect(engine.getStatus()).toBe('rangeCompleted')
      expect(audio.pause).toHaveBeenCalled()
    })

    it('does not cut the range early when speed is lowered during playback', async () => {
      const audio = fakeAudio()
      const onComplete = vi.fn()
      engine.onRangeComplete(onComplete)

      await engine.playRange(0, 2000) // 2 s at 1.0x
      engine.setSpeed(0.5) // now needs 4 s wall time
      expect(audio.playbackRate).toBe(0.5)

      audio.currentTime = 1.2
      vi.advanceTimersByTime(3000) // old 1.0x schedule would have fired by now
      expect(onComplete).not.toHaveBeenCalled()

      audio.currentTime = 2.0
      vi.advanceTimersByTime(30)
      expect(onComplete).toHaveBeenCalledTimes(1)
    })

    it('pauses and resumes from the paused position within the same range', async () => {
      const audio = fakeAudio()
      await engine.playRange(1000, 5000)

      audio.currentTime = 2.2
      engine.pause()
      expect(engine.getStatus()).toBe('paused')

      audio.currentTime = 0 // something else moved the head
      engine.resume()
      await Promise.resolve()
      expect(audio.currentTime).toBe(2.2)
      expect(engine.getStatus()).toBe('playing')
    })

    it('reports blocked status when the browser rejects autoplay', async () => {
      const audio = fakeAudio()
      audio.play.mockRejectedValueOnce(new DOMException('no gesture', 'NotAllowedError'))
      await engine.playRange(0, 1000)
      expect(engine.getStatus()).toBe('blocked')
    })

    it('ignores the AbortError of a play() interrupted by a newer range', async () => {
      const audio = fakeAudio()
      let rejectFirst: (e: unknown) => void = () => {}
      audio.play.mockImplementationOnce(() => new Promise((_, reject) => (rejectFirst = reject)))

      const first = engine.playRange(0, 1000)
      await engine.playRange(2000, 3000)
      rejectFirst(new DOMException('interrupted', 'AbortError'))
      await first

      expect(engine.getStatus()).toBe('playing')
      expect(audio.currentTime).toBe(2)
    })
  })

  it('ignores a stale load that finishes after a newer one started', async () => {
    let resolveFirst: (r: Response) => void = () => {}
    const fetchMock = vi
      .spyOn(globalThis, 'fetch')
      .mockImplementationOnce(() => new Promise((resolve) => (resolveFirst = resolve)))
      .mockResolvedValueOnce({ ok: true, arrayBuffer: async () => new ArrayBuffer(8) } as Response)

    const first = engine.load('/a.mp3')
    await engine.load('/b.mp3')
    const statuses: string[] = []
    engine.onStatusChange((s) => statuses.push(s))

    resolveFirst({ ok: true, arrayBuffer: async () => new ArrayBuffer(8) } as Response)
    await first
    expect(statuses).toEqual([])
    expect(engine.getStatus()).toBe('idle')
    fetchMock.mockRestore()
  })
})
