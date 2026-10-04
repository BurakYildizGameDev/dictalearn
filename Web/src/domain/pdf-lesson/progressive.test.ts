import { describe, it, expect } from 'vitest'
import { mergeSentences, pageNeedsOcr, firstBatchSize, FIRST_BATCH_PAGES } from './progressive'

describe('mergeSentences', () => {
  it('keeps existing sentences in place and appends only new ones', () => {
    const existing = ['One two three.', 'Four five six.']
    const incoming = ['One two three.', 'four five six.', 'Seven eight nine.', 'Ten eleven twelve.']
    expect(mergeSentences(existing, incoming)).toEqual([
      'One two three.',
      'Four five six.',
      'Seven eight nine.',
      'Ten eleven twelve.',
    ])
  })

  it('does not reorder when a page boundary completes a sentence differently', () => {
    const existing = ['Alpha beta gamma.']
    // after more pages the extractor may produce a sentence that spans the old boundary
    const incoming = ['Alpha beta gamma.', 'Delta epsilon zeta eta.', 'Theta iota kappa.']
    expect(mergeSentences(existing, incoming)).toEqual(['Alpha beta gamma.', 'Delta epsilon zeta eta.', 'Theta iota kappa.'])
  })
})

describe('pageNeedsOcr', () => {
  it('treats pages without a usable text layer as images', () => {
    expect(pageNeedsOcr('')).toBe(true)
    expect(pageNeedsOcr('  12  ')).toBe(true)
    expect(pageNeedsOcr('Chapter 1')).toBe(true)
    expect(pageNeedsOcr('The prince stood on a tall column above the city and everyone admired him.')).toBe(false)
  })
})

describe('firstBatchSize', () => {
  it('is the first 25 pages, or the whole PDF when shorter', () => {
    expect(FIRST_BATCH_PAGES).toBe(25)
    expect(firstBatchSize(120)).toBe(25)
    expect(firstBatchSize(7)).toBe(7)
    expect(firstBatchSize(0)).toBe(0)
  })
})
