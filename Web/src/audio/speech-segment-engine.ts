import type { AudioEngine, AudioStatus } from '../domain/audio/audio-engine'
import type { Segment } from '../domain/lessons/types'
import { WordSpeechEngine } from './speech-tts'
import type { WordAudioPlayer } from './word-audio'

/**
 * AudioEngine for lessons without an audio file (lessons built from the user's PDFs).
 * playRange(start_ms) looks the sentence up by its synthetic start time and speaks it with an
 * English OS voice; without one, the sentence is read word by word from the studio word pack.
 */
export class SpeechSegmentEngine implements AudioEngine {
  private byStart = new Map<number, Segment>()
  private status: AudioStatus = 'idle'
  private speed = 1
  private token = 0
  private lastStart: number | null = null
  private rangeListeners: Array<() => void> = []
  private statusListeners: Array<(s: AudioStatus) => void> = []
  private readonly words: WordAudioPlayer

  constructor(words: WordAudioPlayer) {
    this.words = words
  }

  setSegments(segments: Segment[]): void {
    this.byStart = new Map(segments.map((s) => [s.start_ms, s]))
  }

  async load(): Promise<void> {
    this.setStatus('idle')
  }

  async playRange(startMs: number): Promise<void> {
    const segment = this.byStart.get(startMs)
    if (!segment) return
    this.stopSpeaking()
    const token = ++this.token
    this.lastStart = startMs
    this.setStatus('playing')

    const finished = () => {
      if (token !== this.token || this.status !== 'playing') return
      this.setStatus('rangeCompleted')
      for (const l of this.rangeListeners) l()
    }

    const spoken = await WordSpeechEngine.speak(segment.text, 0.95 * this.speed, finished)
    if (token !== this.token) return
    if (!spoken) {
      await this.words.playSequence(segment.text.split(/\s+/), this.speed)
      finished()
    }
  }

  private stopSpeaking(): void {
    this.token++
    WordSpeechEngine.stop()
    this.words.stop()
  }

  pause(): void {
    if (this.status !== 'playing') return
    this.stopSpeaking()
    this.setStatus('paused')
  }

  /** Speech cannot continue mid-sentence reliably; the sentence starts over. */
  resume(): void {
    if (this.status === 'paused' && this.lastStart !== null) void this.playRange(this.lastStart)
  }

  setSpeed(speed: number): void {
    this.speed = Math.max(0.5, Math.min(speed, 2))
  }

  getSpeed(): number {
    return this.speed
  }

  getStatus(): AudioStatus {
    return this.status
  }

  onRangeComplete(callback: () => void): () => void {
    this.rangeListeners.push(callback)
    return () => {
      this.rangeListeners = this.rangeListeners.filter((l) => l !== callback)
    }
  }

  onStatusChange(callback: (status: AudioStatus) => void): () => void {
    this.statusListeners.push(callback)
    return () => {
      this.statusListeners = this.statusListeners.filter((l) => l !== callback)
    }
  }

  private setStatus(status: AudioStatus): void {
    if (this.status === status) return
    this.status = status
    for (const l of this.statusListeners) l(status)
  }

  dispose(): void {
    this.stopSpeaking()
    this.status = 'idle'
  }
}
