export type AudioStatus =
  | 'idle'
  | 'loading'
  | 'playing'
  | 'paused'
  | 'rangeCompleted'
  | 'blocked' // browser autoplay policy rejected playback; needs a user gesture
  | 'error'

export interface AudioEngine {
  load(url: string): Promise<void>
  playRange(startMs: number, endMs: number): Promise<void>
  pause(): void
  /** Continues a paused range from where it stopped. */
  resume(): void
  setSpeed(speed: number): void
  getSpeed(): number
  getStatus(): AudioStatus
  onRangeComplete(callback: () => void): () => void
  onStatusChange(callback: (status: AudioStatus) => void): () => void
  dispose(): void
}
