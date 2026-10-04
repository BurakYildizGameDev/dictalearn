import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import { ReviewView } from './ReviewView'
import { SrsStore, type KeyValueStorage } from '../domain/review/srs'
import { resetDictionaryCache } from '../domain/dictionary/dictionary-loader'

class MemoryStorage implements KeyValueStorage {
  data = new Map<string, string>()
  getItem(k: string) {
    return this.data.get(k) ?? null
  }
  setItem(k: string, v: string) {
    this.data.set(k, v)
  }
  removeItem(k: string) {
    this.data.delete(k)
  }
}

describe('ReviewView', () => {
  beforeEach(() => {
    resetDictionaryCache()
    vi.spyOn(globalThis, 'fetch').mockImplementation(async (input) => {
      const url = String(input)
      if (url.includes('dictionary.json')) {
        return { ok: true, json: async () => ({ version: 1, entries: { cold: 'soğuk', hit: 'vurmak' } }) } as Response
      }
      return { ok: false, status: 404, json: async () => ({}) } as Response // no word audio in tests
    })
  })

  function setup() {
    const srs = new SrsStore(new MemoryStorage(), () => '2026-10-04')
    srs.sync([
      { word: 'cold', kind: 'missing', at: '2026-10-03T10:00:00Z', lesson_id: 'b', segment_id: 1 },
      { word: 'hit', kind: 'missing', at: '2026-10-03T10:00:00Z', lesson_id: 'b', segment_id: 2 },
    ])
    const onDone = vi.fn()
    render(<ReviewView srs={srs} onDone={onDone} />)
    return { srs, onDone }
  }

  it('asks each due word by meaning, moves cards between boxes and repeats missed ones', async () => {
    const { srs, onDone } = setup()
    // the card remounts per word (entry animation), so always query the current input
    const input = () => screen.getByLabelText(/Duyduğun İngilizce kelimeyi yaz/i)

    // card 1: cold (correct)
    expect(await screen.findByText('soğuk')).toBeInTheDocument()
    fireEvent.change(input(), { target: { value: 'Cold' } })
    fireEvent.keyDown(input(), { key: 'Enter' })
    expect(screen.getByRole('status')).toHaveTextContent('Doğru!')
    expect(srs.get('cold')!.box).toBe(1)
    fireEvent.keyDown(input(), { key: 'Enter' })

    // card 2: hit (wrong -> back to box 0, repeated at the end)
    expect(await screen.findByText('vurmak')).toBeInTheDocument()
    fireEvent.click(screen.getByRole('button', { name: /Bilmiyorum/i }))
    expect(screen.getByRole('status')).toHaveTextContent('Doğrusu:hit')
    expect(srs.get('hit')!.box).toBe(0)
    fireEvent.click(screen.getByRole('button', { name: /Devam/i }))

    // extra practice round for "hit" does not change its box again
    expect(screen.getByText(/ek tekrar/)).toBeInTheDocument()
    fireEvent.change(input(), { target: { value: 'hit' } })
    fireEvent.keyDown(input(), { key: 'Enter' })
    expect(srs.get('hit')!.box).toBe(0)
    fireEvent.keyDown(input(), { key: 'Enter' })

    expect(screen.getByText('Tekrar tamamlandı')).toBeInTheDocument()
    expect(screen.getByText(/2 kelimenin 1 tanesini/)).toBeInTheDocument()
    fireEvent.click(screen.getByRole('button', { name: /Defterime dön/i }))
    expect(onDone).toHaveBeenCalled()
  })

  it('shows an empty state when nothing is due', () => {
    const srs = new SrsStore(new MemoryStorage(), () => '2026-10-04')
    render(<ReviewView srs={srs} onDone={vi.fn()} />)
    expect(screen.getByText(/Bugün tekrar edilecek kelime yok/)).toBeInTheDocument()
  })
})
