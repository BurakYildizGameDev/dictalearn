import type { AudioEngine, AudioStatus } from '../domain/audio/audio-engine'

const END_POLL_MS = 15
// Safety net in case the element stalls (buffering) and never reaches the end.
const SAFETY_MARGIN_MS = 1500

/**
 * Plays millisecond ranges of a lesson audio file.
 *
 * Primary path: HTMLAudioElement (streams compressed audio, pitch-preserving speed change).
 * Fallback path: Web Audio BufferSource, used only when no media element exists
 * (headless/test environments or a buffer injected via setBuffer). Long lesson files are
 * never decoded to PCM in the browser: an hour of audio would need ~700 MB of memory.
 */
export class WebAudioEngine implements AudioEngine {
  private ctx: AudioContext | null = null
  private audioBuffer: AudioBuffer | null = null
  private currentSource: AudioBufferSourceNode | null = null
  private audioElement: HTMLAudioElement | null = null
  private blobUrl: string | null = null
  private status: AudioStatus = 'idle'
  private speed = 1.0
  private rangeCompleteListeners: Array<() => void> = []
  private statusListeners: Array<(status: AudioStatus) => void> = []
  private rangeTimeoutId: ReturnType<typeof setTimeout> | null = null
  private rangeEndCheckInterval: ReturnType<typeof setInterval> | null = null
  private loadToken = 0
  private playToken = 0
  private rangeEndSec = 0
  private pausedAtSec: number | null = null

  private getAudioContext(): AudioContext {
    if (!this.ctx) {
      const AudioCtx =
        window.AudioContext ||
        (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext
      this.ctx = new AudioCtx()
    }
    if (this.ctx.state === 'suspended') {
      this.ctx.resume()
    }
    return this.ctx
  }

  async load(url: string): Promise<void> {
    const token = ++this.loadToken
    this.stopCurrent()
    this.pausedAtSec = null
    this.setStatus('loading')

    try {
      const response = await fetch(url)
      if (!response.ok) {
        throw new Error(`Failed to load audio: ${response.status} ${response.statusText}`)
      }
      const arrayBuffer = await response.arrayBuffer()
      // A newer load() started while we were downloading: drop this result.
      if (token !== this.loadToken) return

      this.releaseMedia()
      this.audioBuffer = null

      if (typeof window !== 'undefined' && typeof window.Audio !== 'undefined') {
        // Blob URL keeps the whole file in memory so seeking is instant and exact.
        const blob = new Blob([arrayBuffer], { type: 'audio/mpeg' })
        this.blobUrl = URL.createObjectURL(blob)
        const audio = new Audio(this.blobUrl)
        audio.preload = 'auto'
        this.applyPitchPreservation(audio)
        audio.playbackRate = this.speed
        this.audioElement = audio
      } else {
        this.audioBuffer = await this.decode(arrayBuffer)
        if (token !== this.loadToken) return
      }

      this.setStatus('idle')
    } catch (err) {
      if (token !== this.loadToken) return
      this.setStatus('error')
      const details = err instanceof Error ? err.message : String(err)
      throw new Error(`Audio load error for ${url}: ${details}`)
    }
  }

  private decode(arrayBuffer: ArrayBuffer): Promise<AudioBuffer> {
    const ctx = this.getAudioContext()
    return new Promise<AudioBuffer>((resolve, reject) => {
      const res = ctx.decodeAudioData(arrayBuffer, resolve, reject)
      if (res && typeof (res as Promise<AudioBuffer>).then === 'function') {
        ;(res as Promise<AudioBuffer>).then(resolve).catch(reject)
      }
    })
  }

  private applyPitchPreservation(audio: HTMLAudioElement): void {
    audio.preservesPitch = true
    const legacy = audio as unknown as { mozPreservesPitch?: boolean; webkitPreservesPitch?: boolean }
    if ('mozPreservesPitch' in audio) legacy.mozPreservesPitch = true
    if ('webkitPreservesPitch' in audio) legacy.webkitPreservesPitch = true
  }

  // Exposed for tests or direct buffer injection
  setBuffer(buffer: AudioBuffer): void {
    this.releaseMedia()
    this.audioBuffer = buffer
    this.setStatus('idle')
  }

  async playRange(startMs: number, endMs: number): Promise<void> {
    if (!this.audioElement && !this.audioBuffer) {
      throw new Error('Audio not loaded. Call load() before playRange().')
    }

    const startSec = Math.max(0, startMs / 1000)
    const endSec = Math.max(startSec, endMs / 1000)
    if (endSec - startSec <= 0) return

    this.stopCurrent()
    this.pausedAtSec = null
    this.rangeEndSec = endSec

    if (this.audioElement) {
      await this.playElementFrom(startSec)
      return
    }
    this.playBufferRange(startSec, endSec)
  }

  private async playElementFrom(startSec: number): Promise<void> {
    const audio = this.audioElement
    if (!audio) return
    const token = ++this.playToken

    this.applyPitchPreservation(audio)
    audio.playbackRate = this.speed
    audio.currentTime = startSec
    this.setStatus('playing')

    try {
      await audio.play()
    } catch (err) {
      // A newer range or a pause interrupted this play() call (AbortError): not a failure.
      if (token !== this.playToken) return
      const blocked = err instanceof DOMException && err.name === 'NotAllowedError'
      this.setStatus(blocked ? 'blocked' : 'error')
      return
    }

    if (token !== this.playToken) return

    this.rangeEndCheckInterval = setInterval(() => {
      if (audio.currentTime >= this.rangeEndSec || audio.ended) {
        this.finishRange()
      }
    }, END_POLL_MS)
    this.scheduleSafetyTimeout()
  }

  private scheduleSafetyTimeout(): void {
    if (this.rangeTimeoutId) clearTimeout(this.rangeTimeoutId)
    const audio = this.audioElement
    if (!audio) return
    const remainingSec = Math.max(0, this.rangeEndSec - audio.currentTime)
    const wallMs = (remainingSec / this.speed) * 1000
    this.rangeTimeoutId = setTimeout(() => this.finishRange(), wallMs + SAFETY_MARGIN_MS)
  }

  private playBufferRange(startSec: number, endSec: number): void {
    if (!this.audioBuffer) return
    const ctx = this.getAudioContext()
    const source = ctx.createBufferSource()
    source.buffer = this.audioBuffer
    source.playbackRate.value = this.speed
    source.connect(ctx.destination)

    const durationSec = endSec - startSec
    this.currentSource = source
    this.setStatus('playing')
    source.start(0, startSec, durationSec)

    const wallMs = (durationSec / this.speed) * 1000
    this.rangeTimeoutId = setTimeout(() => this.finishRange(), Number.isFinite(wallMs) ? wallMs : 0)
  }

  private finishRange(): void {
    if (this.status !== 'playing') return
    this.stopCurrent()
    this.setStatus('rangeCompleted')
    for (const listener of this.rangeCompleteListeners) {
      listener()
    }
  }

  pause(): void {
    if (this.status !== 'playing') return
    if (this.audioElement) {
      this.pausedAtSec = this.audioElement.currentTime
    }
    this.stopCurrent()
    this.setStatus('paused')
  }

  resume(): void {
    if (this.ctx?.state === 'suspended') {
      this.ctx.resume()
    }
    if (this.status === 'paused' && this.audioElement && this.pausedAtSec !== null) {
      const from = this.pausedAtSec
      this.pausedAtSec = null
      void this.playElementFrom(from)
    }
  }

  setSpeed(speed: number): void {
    this.speed = Math.max(0.25, Math.min(speed, 2.5))
    if (this.audioElement) {
      this.applyPitchPreservation(this.audioElement)
      this.audioElement.playbackRate = this.speed
      // Remaining wall-clock time changed: move the safety net accordingly.
      if (this.status === 'playing') this.scheduleSafetyTimeout()
    }
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
    this.playToken++
    if (this.rangeTimeoutId) {
      clearTimeout(this.rangeTimeoutId)
      this.rangeTimeoutId = null
    }
    if (this.rangeEndCheckInterval) {
      clearInterval(this.rangeEndCheckInterval)
      this.rangeEndCheckInterval = null
    }
    if (this.audioElement) {
      try {
        this.audioElement.pause()
      } catch {
        // jsdom does not implement media playback
      }
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

  private releaseMedia(): void {
    this.stopCurrent()
    if (this.audioElement) {
      this.audioElement.removeAttribute('src')
      this.audioElement = null
    }
    if (this.blobUrl) {
      URL.revokeObjectURL(this.blobUrl)
      this.blobUrl = null
    }
  }

  private setStatus(status: AudioStatus): void {
    if (this.status === status) return
    this.status = status
    for (const listener of this.statusListeners) {
      listener(status)
    }
  }

  dispose(): void {
    this.loadToken++
    this.releaseMedia()
    this.audioBuffer = null
    this.status = 'idle'
    this.rangeCompleteListeners = []
    this.statusListeners = []
    if (this.ctx && this.ctx.state !== 'closed') {
      this.ctx.close()
    }
    this.ctx = null
  }
}
