import { describe, it, expect } from 'vitest'
import { tokenizeSentenceToWords, checkWordMatch, normalizeWord } from './word-mode'

describe('word-mode domain logic', () => {
  it('tokenizes sentence text into WordToken objects', () => {
    const text = 'Every morning, the Time Traveller arrived.'
    const tokens = tokenizeSentenceToWords(text)

    expect(tokens).toHaveLength(6)
    expect(tokens[0]).toEqual({
      index: 0,
      raw: 'Every',
      clean: 'every',
      punctuation: '',
      isRevealed: false,
    })
    expect(tokens[1]).toEqual({
      index: 1,
      raw: 'morning,',
      clean: 'morning',
      punctuation: ',',
      isRevealed: false,
    })
    expect(tokens[5]).toEqual({
      index: 5,
      raw: 'arrived.',
      clean: 'arrived',
      punctuation: '.',
      isRevealed: false,
    })
  })

  it('normalizes words removing leading and trailing punctuation', () => {
    expect(normalizeWord('"Hello!"')).toBe('hello')
    expect(normalizeWord('...world...')).toBe('world')
    expect(normalizeWord("didn't")).toBe("didn't")
  })

  it('checks word match correctly with case insensitivity and punctuation tolerance', () => {
    expect(checkWordMatch('every', 'every')).toBe(true)
    expect(checkWordMatch('Every', 'every')).toBe(true)
    expect(checkWordMatch('EVERY!', 'every')).toBe(true)
    expect(checkWordMatch('didnt', "didn't")).toBe(true)
    expect(checkWordMatch("didn't", "didn't")).toBe(true)
    expect(checkWordMatch('different', 'every')).toBe(false)
    expect(checkWordMatch('', 'every')).toBe(false)
  })
})
