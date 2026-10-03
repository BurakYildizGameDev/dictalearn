export type AudioStatus = 'idle' | 'loading' | 'playing' | 'paused' | 'rangeCompleted' | 'error'

export interface AudioEngine {
  load(url: string): Promise<void>
  playRange(startMs: number, endMs: number): Promise<void>
  pause(): void
  resume(): void
  setSpeed(speed: number): void
  getSpeed(): number
  getStatus(): AudioStatus
  onRangeComplete(callback: () => void): () => void
  onStatusChange(callback: (status: AudioStatus) => void): () => void
  dispose(): void
}
