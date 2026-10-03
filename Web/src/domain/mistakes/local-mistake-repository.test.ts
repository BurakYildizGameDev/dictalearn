import { describe, it, expect, beforeEach } from 'vitest'
import { LocalMistakeRepository } from './local-mistake-repository'
import type { MistakeRecord } from './types'

describe('LocalMistakeRepository (F3.3)', () => {
  let repo: LocalMistakeRepository

  beforeEach(() => {
    localStorage.clear()
    repo = new LocalMistakeRepository()
  })

  it('starts with empty mistakes', () => {
    expect(repo.getMistakes()).toEqual([])
  })

  it('adds and retrieves mistakes correctly', () => {
    const mistake: MistakeRecord = {
      word: 'immediately',
      kind: 'substitute',
      typed: 'imediately',
      lesson_id: 'sample_ch01',
      segment_id: 2,
      at: '2026-10-03T10:00:00Z',
    }

    repo.addMistakes([mistake])
    expect(repo.getMistakes()).toHaveLength(1)
    expect(repo.getMistakes()[0].word).toBe('immediately')
  })

  it('calculates word frequencies across mistakes', () => {
    const m1: MistakeRecord = {
      word: 'immediately',
      kind: 'substitute',
      lesson_id: 'test',
      segment_id: 1,
      at: '',
    }
    const m2: MistakeRecord = {
      word: 'Immediately',
      kind: 'missing',
      lesson_id: 'test',
      segment_id: 2,
      at: '',
    }
    const m3: MistakeRecord = {
      word: 'suitcase',
      kind: 'substitute',
      lesson_id: 'test',
      segment_id: 3,
      at: '',
    }

    repo.addMistakes([m1, m2, m3])
    const freqs = repo.getWordFrequencies()

    expect(freqs['immediately']).toBe(2)
    expect(freqs['suitcase']).toBe(1)
  })

  it('recovers safely from corrupted localStorage JSON without crashing', () => {
    localStorage.setItem('dictalearn_mistakes_v1', 'corrupted{json[')
    expect(repo.getMistakes()).toEqual([])
  })
})
