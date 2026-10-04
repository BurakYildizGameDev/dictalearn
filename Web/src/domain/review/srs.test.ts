import { describe, it, expect, beforeEach } from 'vitest'
import { SrsStore, INTERVAL_DAYS, addDays, type KeyValueStorage } from './srs'
import type { MistakeRecord } from '../mistakes/types'

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

const mistake = (word: string, at: string): MistakeRecord => ({
  word,
  kind: 'substitute',
  at,
  lesson_id: 'book_01',
  segment_id: 1,
})

describe('SrsStore', () => {
  let storage: MemoryStorage
  let today = '2026-10-04'
  let store: SrsStore

  beforeEach(() => {
    storage = new MemoryStorage()
    today = '2026-10-04'
    store = new SrsStore(storage, () => today)
  })

  it('creates a due card for every word in the mistake notebook', () => {
    store.sync([mistake('Small', '2026-10-01T10:00:00Z'), mistake('small', '2026-10-02T10:00:00Z'), mistake('cold', '2026-10-03T10:00:00Z')])
    expect(store.dueCards().map((c) => c.word).sort()).toEqual(['cold', 'small'])
    expect(store.dueCards()[0].box).toBe(0)
  })

  it('moves a card up one box per correct answer with growing intervals', () => {
    store.sync([mistake('cold', '2026-10-03T10:00:00Z')])
    store.answer('cold', true)
    let card = store.get('cold')!
    expect(card.box).toBe(1)
    expect(card.due).toBe(addDays(today, INTERVAL_DAYS[1]))
    expect(store.dueCards()).toHaveLength(0)

    today = card.due
    store.answer('cold', true)
    card = store.get('cold')!
    expect(card.box).toBe(2)
    expect(card.due).toBe(addDays(today, INTERVAL_DAYS[2]))
  })

  it('caps at the last box', () => {
    store.sync([mistake('cold', '2026-10-03T10:00:00Z')])
    for (let i = 0; i < 10; i++) store.answer('cold', true)
    expect(store.get('cold')!.box).toBe(INTERVAL_DAYS.length - 1)
  })

  it('sends a wrong answer back to box 0, due tomorrow (it was just practised)', () => {
    store.sync([mistake('cold', '2026-10-03T10:00:00Z')])
    store.answer('cold', true)
    store.answer('cold', true)
    store.answer('cold', false)
    const card = store.get('cold')!
    expect(card.box).toBe(0)
    expect(card.due).toBe(addDays(today, 1))
    expect(card.lapses).toBe(1)
    expect(store.dueCards()).toHaveLength(0)
  })

  it('resets a learned card when the word is missed again in dictation', () => {
    store.sync([mistake('cold', '2026-10-03T10:00:00Z')])
    store.answer('cold', true) // reviewed on 2026-10-04
    store.sync([mistake('cold', '2026-10-03T10:00:00Z'), mistake('cold', '2026-10-05T09:00:00Z')])
    expect(store.get('cold')!.box).toBe(0)
    // an old mistake (before the review) does not reset it
    store.answer('cold', true)
    store.sync([mistake('cold', '2026-10-03T10:00:00Z')])
    expect(store.get('cold')!.box).toBe(1)
  })

  it('reports counts per state and persists across instances', () => {
    store.sync([mistake('cold', '2026-10-03T10:00:00Z'), mistake('hit', '2026-10-03T10:00:00Z')])
    store.answer('hit', true)
    expect(store.stats()).toEqual({ total: 2, due: 1, learned: 0 })
    expect(new SrsStore(storage, () => today).get('hit')!.box).toBe(1)
  })

  it('removes cards whose words left the notebook', () => {
    store.sync([mistake('cold', '2026-10-03T10:00:00Z')])
    store.sync([])
    expect(store.get('cold')).toBeNull()
  })
})

describe('addDays', () => {
  it('handles month boundaries', () => {
    expect(addDays('2026-10-30', 3)).toBe('2026-11-02')
  })
})
