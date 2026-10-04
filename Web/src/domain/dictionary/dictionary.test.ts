import { describe, it, expect } from 'vitest'
import { Dictionary, lemmaCandidates, normalizeLookupWord } from './dictionary'

const dict = new Dictionary({
  pack: 'toplamak',
  story: 'hikâye',
  stand: 'ayakta durmak',
  stop: 'durmak',
  make: 'yapmak',
  happy: 'mutlu',
  'drift apart': 'birbirinden uzaklaşmak',
  'high above': 'çok yukarısında',
  "o'clock": 'saat',
  box: 'kutu',
  run: 'koşmak',
})

describe('normalizeLookupWord', () => {
  it('lowercases, unifies apostrophes and strips boundary punctuation', () => {
    expect(normalizeLookupWord('“Happy,”')).toBe('happy')
    expect(normalizeLookupWord("O’clock.")).toBe("o'clock")
    expect(normalizeLookupWord('...')).toBe('')
  })
})

describe('lemmaCandidates', () => {
  it('covers regular inflections', () => {
    expect(lemmaCandidates('packed')).toContain('pack')
    expect(lemmaCandidates('stories')).toContain('story')
    expect(lemmaCandidates('stopped')).toContain('stop')
    expect(lemmaCandidates('making')).toContain('make')
    expect(lemmaCandidates('boxes')).toContain('box')
    expect(lemmaCandidates('running')).toContain('run')
    expect(lemmaCandidates("prince's")).toContain('prince')
  })

  it('maps common irregular forms', () => {
    expect(lemmaCandidates('stood')).toContain('stand')
    expect(lemmaCandidates('made')).toContain('make')
  })
})

describe('Dictionary.lookup', () => {
  it('finds exact and inflected words, reporting the matched headword', () => {
    expect(dict.lookup('Happy!')).toEqual({ headword: 'happy', meaning: 'mutlu' })
    expect(dict.lookup('packed')).toEqual({ headword: 'pack', meaning: 'toplamak' })
    expect(dict.lookup('stood')).toEqual({ headword: 'stand', meaning: 'ayakta durmak' })
  })

  it('returns null for unknown words', () => {
    expect(dict.lookup('zyzzyva')).toBeNull()
    expect(dict.lookup('')).toBeNull()
  })

  it('prefers the longest phrase in the sentence that contains the clicked word', () => {
    const words = ['They', 'began', 'to', 'drift', 'apart.']
    expect(dict.lookupInSentence(words, 4)).toEqual({ headword: 'drift apart', meaning: 'birbirinden uzaklaşmak' })
    expect(dict.lookupInSentence(['High', 'above', 'the', 'city'], 0)?.headword).toBe('high above')
    expect(dict.lookupInSentence(['He', 'packed', 'it'], 1)?.headword).toBe('pack')
  })

  it('reports its size', () => {
    expect(dict.size).toBe(11)
  })
})
