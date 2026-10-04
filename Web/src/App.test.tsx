import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import App from './App'

describe('App Integration Smoke Test', () => {
  beforeEach(() => {
    window.location.hash = ''
    localStorage.clear()
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

  it('opens on the library with level sections and book cards', () => {
    render(<App />)
    expect(screen.getByRole('button', { name: /DictaLearn ana sayfa/i })).toBeInTheDocument()
    expect(screen.getByRole('heading', { name: /Seviye 1/i })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /The Happy Prince/i })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /PDF Ekle/i })).toBeInTheDocument()
  })

  it('shows the daily goal card and lets the user change the goal', () => {
    render(<App />)
    const card = screen.getByRole('region', { name: 'Bugünkü hedef' })
    expect(card).toHaveTextContent('0 / 20 cümle')
    fireEvent.click(screen.getByTitle('Günde 10 cümle'))
    expect(screen.getByRole('region', { name: 'Bugünkü hedef' })).toHaveTextContent('0 / 10 cümle')
  })

  it('filters books with the search box', () => {
    render(<App />)
    fireEvent.change(screen.getByPlaceholderText(/Kitap, yazar ara/i), { target: { value: 'dracula' } })
    expect(screen.getByRole('button', { name: /Dracula/i })).toBeInTheDocument()
    expect(screen.queryByRole('button', { name: /The Happy Prince/i })).toBeNull()
  })

  it('loads a book from the library into the study screen via the hash route', async () => {
    render(<App />)
    fireEvent.click(screen.getByRole('button', { name: /The Happy Prince/i }))

    expect(await screen.findByRole('heading', { level: 1, name: 'The Happy Prince' })).toBeInTheDocument()
    expect(screen.getByRole('textbox')).toBeInTheDocument()
    expect(window.location.hash).toBe('#/study/book_01_the_happy_prince')
    expect(globalThis.fetch).toHaveBeenCalledWith('/lessons/book_01_the_happy_prince/lesson.json')
    expect(localStorage.getItem('dictalearn_last_book')).toBe('book_01_the_happy_prince')
  })

  it('shows an error with retry instead of a blank page when a lesson fails to load', async () => {
    vi.mocked(globalThis.fetch).mockResolvedValue({ ok: false, status: 404, statusText: 'Not Found' } as Response)
    window.location.hash = '#/study/book_02_the_selfish_giant'
    render(<App />)
    expect(await screen.findByText(/Ders yüklenemedi/i)).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /Yeniden Dene/i })).toBeInTheDocument()
  })
})
