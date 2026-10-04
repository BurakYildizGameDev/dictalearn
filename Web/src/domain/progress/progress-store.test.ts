import { describe, it, expect, beforeEach } from 'vitest'
import { ProgressStore, progressPercent, type KeyValueStorage } from './progress-store'

class MemoryStorage implements KeyValueStorage {
  data = new Map<string, string>()
  getItem(key: string) {
    return this.data.has(key) ? this.data.get(key)! : null
  }
  setItem(key: string, value: string) {
    this.data.set(key, value)
  }
  removeItem(key: string) {
    this.data.delete(key)
  }
}

describe('ProgressStore', () => {
  let storage: MemoryStorage
  let store: ProgressStore

  beforeEach(() => {
    storage = new MemoryStorage()
    store = new ProgressStore(storage, () => '2026-10-04T10:00:00.000Z')
  })

  it('returns null for an unknown lesson', () => {
    expect(store.get('book_01')).toBeNull()
  })

  it('records the current segment and keeps the furthest segment reached', () => {
    store.record('book_01', 5, 300)
    store.record('book_01', 2, 300) // user went back with PageUp
    const p = store.get('book_01')!
    expect(p.segmentIndex).toBe(2)
    expect(p.furthestIndex).toBe(5)
    expect(p.totalSegments).toBe(300)
    expect(p.completed).toBe(false)
    expect(p.updatedAt).toBe('2026-10-04T10:00:00.000Z')
  })

  it('marks a lesson as completed and keeps that flag', () => {
    store.markCompleted('book_01', 300)
    store.record('book_01', 0, 300)
    expect(store.get('book_01')!.completed).toBe(true)
    expect(store.get('book_01')!.furthestIndex).toBe(300)
  })

  it('clamps out-of-range indexes', () => {
    store.record('book_01', 999, 10)
    expect(store.get('book_01')!.segmentIndex).toBe(9)
    store.record('book_02', -4, 10)
    expect(store.get('book_02')!.segmentIndex).toBe(0)
  })

  it('persists across instances and survives corrupt data', () => {
    store.record('book_01', 3, 10)
    expect(new ProgressStore(storage).get('book_01')!.segmentIndex).toBe(3)

    storage.setItem('dictalearn_progress_v1', '{not json')
    expect(new ProgressStore(storage).get('book_01')).toBeNull()
  })

  it('reset removes one lesson only', () => {
    store.record('book_01', 3, 10)
    store.record('book_02', 4, 10)
    store.reset('book_01')
    expect(store.get('book_01')).toBeNull()
    expect(store.get('book_02')).not.toBeNull()
  })

  it('works without storage (private mode)', () => {
    const memoryless = new ProgressStore(null)
    memoryless.record('x', 1, 5)
    expect(memoryless.get('x')).toBeNull()
  })

  it('computes progress percent', () => {
    expect(progressPercent(null)).toBe(0)
    store.record('book_01', 149, 300)
    expect(progressPercent(store.get('book_01'))).toBe(50)
    store.markCompleted('book_01', 300)
    expect(progressPercent(store.get('book_01'))).toBe(100)
  })
})
