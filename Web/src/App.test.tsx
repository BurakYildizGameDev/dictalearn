import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen } from '@testing-library/react'
import App from './App'

describe('App Integration Smoke Test', () => {
  beforeEach(() => {
    vi.spyOn(globalThis, 'fetch').mockImplementation(async (input) => {
      const url = String(input)
      if (url.includes('.json')) {
        return {
          ok: true,
          json: async () => ({
            schema_version: 1,
            lesson_id: 'test_ch01',
            title: 'Chapter 1: The Departure',
            source_lang: 'en',
            target_lang: 'tr',
            audio_file: 'audio.wav',
            segments: [
              {
                id: 1,
                start_ms: 0,
                end_ms: 3000,
                text: 'He packed his small brown suitcase.',
                translation: 'Küçük kahverengi bavulunu topladı.',
              },
            ],
          }),
        } as Response
      }
      // audio mock
      return {
        ok: true,
        arrayBuffer: async () => new ArrayBuffer(8),
      } as Response
    })

    class MockAudioContext {
      state = 'running'
      resume = vi.fn()
      close = vi.fn()
      destination = {}
      createBufferSource() {
        return {
          buffer: null,
          playbackRate: { value: 1.0 },
          connect: vi.fn(),
          disconnect: vi.fn(),
          start: vi.fn(),
          stop: vi.fn(),
        }
      }
      decodeAudioData(_data: ArrayBuffer, success?: (buf: AudioBuffer) => void) {
        const buf = { duration: 3 } as AudioBuffer
        if (success) success(buf)
        return Promise.resolve(buf)
      }
    }

    // @ts-expect-error mock AudioContext class
    window.AudioContext = MockAudioContext
  })

  it('renders application header and title', async () => {
    render(<App />)
    expect(screen.getByText('DictaLearn')).toBeInTheDocument()
    expect(await screen.findByText(/Chapter 1: The Departure/i)).toBeInTheDocument()
  })
})
