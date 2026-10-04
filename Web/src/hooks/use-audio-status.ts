import { useCallback, useSyncExternalStore } from 'react'
import type { AudioEngine, AudioStatus } from '../domain/audio/audio-engine'

/** Subscribes a component to the engine's playback status. */
export function useAudioStatus(engine: AudioEngine): AudioStatus {
  const subscribe = useCallback((onChange: () => void) => engine.onStatusChange(onChange), [engine])
  const getSnapshot = useCallback(() => engine.getStatus(), [engine])
  return useSyncExternalStore(subscribe, getSnapshot, getSnapshot)
}
