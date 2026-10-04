import { describe, it, expect, beforeEach } from 'vitest'
import { HardSentenceStore, HARD_THRESHOLD, hardSubLesson } from './hard-sentences'
import type { KeyValueStorage } from '../progress/progress-store'
import type { Lesson } from '../lessons/types'

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

const lesson: Lesson = {
  schema_version: 1,
  lesson_id: 'book_01',
  title: 'Book',
  source_lang: 'en',
  target_lang: 'tr',
  audio_file: 'audio.mp3',
  segments: [1, 2, 3, 4].map((id) => ({ id, start_ms: id * 1000, end_ms: id * 1000 + 900, text: `Sentence ${id}.` })),
}

describe('HardSentenceStore', () => {
  let storage: MemoryStorage
  let store: HardSentenceStore

  beforeEach(() => {
    storage = new MemoryStorage()
    store = new HardSentenceStore(storage)
  })

  it('marks sentences below the threshold as hard and unmarks them once done well', () => {
    expect(HARD_THRESHOLD).toBe(0.7)
    store.record('book_01', 3, 0.4)
    store.record('book_01', 1, 0.69)
    store.record('book_01', 2, 0.9)
    expect(store.list('book_01')).toEqual([1, 3])
    store.record('book_01', 3, 1)
    expect(store.list('book_01')).toEqual([1])
    expect(store.count('book_01')).toBe(1)
    expect(store.count('other')).toBe(0)
  })

  it('persists per lesson and survives corrupt data', () => {
    store.record('book_01', 2, 0)
    store.record('book_02', 5, 0.1)
    expect(new HardSentenceStore(storage).list('book_02')).toEqual([5])
    storage.setItem('dictalearn_hard_sentences_v1', '{oops')
    expect(new HardSentenceStore(storage).list('book_01')).toEqual([])
  })
})

describe('hardSubLesson', () => {
  it('keeps only the hard segments with their original audio ranges', () => {
    const sub = hardSubLesson(lesson, [2, 4, 99])
    expect(sub.lesson_id).toBe('book_01::hard')
    expect(sub.segments.map((s) => [s.id, s.start_ms, s.end_ms])).toEqual([
      [2, 2000, 2900],
      [4, 4000, 4900],
    ])
  })
})
