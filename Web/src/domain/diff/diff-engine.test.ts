import { describe, it, expect } from 'vitest'
import { computeWordDiff } from './diff-engine'

describe('Diff Engine (§4.3 Mandatory Cases)', () => {
  it('1. Perfect match ignoring case and trailing period', () => {
    const expected = 'He packed his small brown suitcase.'
    const typed = 'he packed his small brown suitcase'
    const result = computeWordDiff(expected, typed)

    expect(result.isPerfect).toBe(true)
    expect(result.accuracy).toBe(1)
    expect(result.expectedCount).toBe(6)
    expect(result.correctCount).toBe(6)
    expect(result.words.every((w) => w.kind === 'equal')).toBe(true)
  })

  it('2. Single typo results in 1 substitute, accuracy 5/6', () => {
    const expected = 'The morning cold hit him immediately.'
    const typed = 'The morning cold hit him imediately'
    const result = computeWordDiff(expected, typed)

    expect(result.isPerfect).toBe(false)
    expect(result.correctCount).toBe(5)
    expect(result.expectedCount).toBe(6)
    expect(result.accuracy).toBeCloseTo(5 / 6)

    const sub = result.words.find((w) => w.kind === 'substitute')
    expect(sub).toBeDefined()
    expect(sub?.expected).toBe('immediately.')
    expect(sub?.typed).toBe('imediately')
  })

  it('3. Omitted word results in 1 missing', () => {
    const expected = 'He packed his small brown suitcase.'
    const typed = 'He packed his brown suitcase'
    const result = computeWordDiff(expected, typed)

    expect(result.isPerfect).toBe(false)
    expect(result.correctCount).toBe(5)
    expect(result.expectedCount).toBe(6)

    const missing = result.words.find((w) => w.kind === 'missing')
    expect(missing).toBeDefined()
    expect(missing?.expected).toBe('small')
  })

  it('4. Repeated word results in 1 extra', () => {
    const expected = 'He opened the door.'
    const typed = 'He opened the the door'
    const result = computeWordDiff(expected, typed)

    expect(result.isPerfect).toBe(false)
    expect(result.correctCount).toBe(4)
    expect(result.expectedCount).toBe(4)

    const extra = result.words.find((w) => w.kind === 'extra')
    expect(extra).toBeDefined()
    expect(extra?.typed).toBe('the')
  })

  it('5. Normalizes curly apostrophes to straight apostrophes', () => {
    const expected = 'I don’t know.'
    const typed = "I don't know"
    const result = computeWordDiff(expected, typed)

    expect(result.isPerfect).toBe(true)
    expect(result.accuracy).toBe(1)
  })

  it('6. Empty typed input results in all missing words and 0 accuracy', () => {
    const expected = 'He opened the door.'
    const typed = ''
    const result = computeWordDiff(expected, typed)

    expect(result.isPerfect).toBe(false)
    expect(result.correctCount).toBe(0)
    expect(result.expectedCount).toBe(4)
    expect(result.accuracy).toBe(0)
    expect(result.words.every((w) => w.kind === 'missing')).toBe(true)
  })

  it('7. Handles ignorePunctuation flag', () => {
    const expected = 'Hello, world!'
    const typed = 'hello world'

    // Default: ignorePunctuation = true
    const withPunctuationIgnored = computeWordDiff(expected, typed, { ignorePunctuation: true })
    expect(withPunctuationIgnored.isPerfect).toBe(true)

    // With ignorePunctuation = false
    const withPunctuationStrict = computeWordDiff(expected, typed, { ignorePunctuation: false })
    expect(withPunctuationStrict.isPerfect).toBe(false)
    expect(withPunctuationStrict.words.filter((w) => w.kind === 'substitute')).toHaveLength(2)
  })

  it('8. Handles ignoreCase flag', () => {
    const expected = 'He Opened'
    const typed = 'he opened'

    // Default: ignoreCase = true
    const withCaseIgnored = computeWordDiff(expected, typed, { ignoreCase: true })
    expect(withCaseIgnored.isPerfect).toBe(true)

    // With ignoreCase = false
    const withCaseStrict = computeWordDiff(expected, typed, { ignoreCase: false })
    expect(withCaseStrict.isPerfect).toBe(false)
    expect(withCaseStrict.words.filter((w) => w.kind === 'substitute')).toHaveLength(2)
  })
})
