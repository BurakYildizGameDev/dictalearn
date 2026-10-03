import type { AudioEngine, AudioStatus } from '../domain/audio/audio-engine'

export class WebAudioEngine implements AudioEngine {
  private ctx: AudioContext | null = null
  private audioBuffer: AudioBuffer | null = null
  private currentSource: AudioBufferSourceNode | null = null
  private status: AudioStatus = 'idle'
  private speed = 1.0
  private rangeCompleteListeners: Array<() => void> = []
  private statusListeners: Array<(status: AudioStatus) => void> = []
  private rangeTimeoutId: ReturnType<typeof setTimeout> | null = null

  private getAudioContext(): AudioContext {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext
      this.ctx = new AudioCtx()
    }
    if (this.ctx.state === 'suspended') {
      this.ctx.resume()
    }
    return this.ctx
  }

  async load(url: string): Promise<void> {
    this.setStatus('loading')
    try {
      const response = await fetch(url)
      if (!response.ok) {
        throw new Error(`Failed to load audio: ${response.statusText}`)
      }
      const arrayBuffer = await response.arrayBuffer()
      const ctx = this.getAudioContext()
      this.audioBuffer = await new Promise<AudioBuffer>((resolve, reject) => {
        try {
          const res = ctx.decodeAudioData(
            arrayBuffer,
            (buf) => resolve(buf),
            (err) => reject(err)
          )
          if (res && typeof (res as Promise<AudioBuffer>).then === 'function') {
            (res as Promise<AudioBuffer>).then(resolve).catch(reject)
          }
        } catch (e) {
          reject(e)
        }
      })
      this.setStatus('idle')
    } catch (err) {
      this.setStatus('error')
      const details = err instanceof Error ? err.message : String(err)
      throw new Error(`Audio load error for ${url}: ${details}`)
    }
  }

  // Exposed for tests or direct buffer injection
  setBuffer(buffer: AudioBuffer): void {
    this.audioBuffer = buffer
    this.setStatus('idle')
  }

  async playRange(startMs: number, endMs: number): Promise<void> {
    if (!this.audioBuffer) {
      throw new Error('Audio not loaded. Call load() before playRange().')
    }

    this.stopCurrent()

    const ctx = this.getAudioContext()
    const offset = Math.max(0, startMs / 1000)
    const duration = Math.max(0, (endMs - startMs) / 1000)

    if (duration <= 0) return

    const source = ctx.createBufferSource()
    source.buffer = this.audioBuffer
    source.playbackRate.value = this.speed
    source.connect(ctx.destination)

    this.currentSource = source
    this.setStatus('playing')

    // Start playback at hardware audio clock precision
    source.start(0, offset, duration)

    // Calculate actual elapsed wall time taking speed into account
    const actualDurationMs = (duration / this.speed) * 1000

    this.rangeTimeoutId = setTimeout(() => {
      this.stopCurrent()
      this.setStatus('rangeCompleted')
      for (const listener of this.rangeCompleteListeners) {
        listener()
      }
    }, actualDurationMs)
  }

  pause(): void {
    if (this.status === 'playing') {
      this.stopCurrent()
      this.setStatus('paused')
    }
  }

  resume(): void {
    // Range playback uses playRange; resume can be handled via playRange
    if (this.ctx?.state === 'suspended') {
      this.ctx.resume()
    }
  }

  setSpeed(speed: number): void {
    this.speed = Math.max(0.25, Math.min(speed, 2.5))
    if (this.currentSource) {
      this.currentSource.playbackRate.value = this.speed
    }
  }

  getSpeed(): number {
    return this.speed
  }

  getStatus(): AudioStatus {
    return this.status
  }

  onRangeComplete(callback: () => void): () => void {
    this.rangeCompleteListeners.push(callback)
    return () => {
      this.rangeCompleteListeners = this.rangeCompleteListeners.filter((l) => l !== callback)
    }
  }

  onStatusChange(callback: (status: AudioStatus) => void): () => void {
    this.statusListeners.push(callback)
    return () => {
      this.statusListeners = this.statusListeners.filter((l) => l !== callback)
    }
  }

  private stopCurrent(): void {
    if (this.rangeTimeoutId) {
      clearTimeout(this.rangeTimeoutId)
      this.rangeTimeoutId = null
    }
    if (this.currentSource) {
      try {
        this.currentSource.stop()
        this.currentSource.disconnect()
      } catch {
        // Source might have already stopped
      }
      this.currentSource = null
    }
  }

  private setStatus(status: AudioStatus): void {
    this.status = status
    for (const listener of this.statusListeners) {
      listener(status)
    }
  }

  dispose(): void {
    this.stopCurrent()
    this.rangeCompleteListeners = []
    this.statusListeners = []
    if (this.ctx && this.ctx.state !== 'closed') {
      this.ctx.close()
      this.ctx = null
    }
  }
}
