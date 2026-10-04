import { describe, it, expect } from 'vitest'
import { parseHash, routeToHash } from './route'

describe('hash routes', () => {
  it('parses the library for empty or unknown hashes', () => {
    expect(parseHash('')).toEqual({ name: 'library' })
    expect(parseHash('#/')).toEqual({ name: 'library' })
    expect(parseHash('#/nope/x')).toEqual({ name: 'library' })
  })

  it('parses study routes with a book id', () => {
    expect(parseHash('#/study/book_32_dracula')).toEqual({ name: 'study', bookId: 'book_32_dracula' })
    expect(parseHash('#/study/')).toEqual({ name: 'library' })
  })

  it('parses editor and custom lesson routes', () => {
    expect(parseHash('#/editor')).toEqual({ name: 'editor' })
    expect(parseHash('#/custom')).toEqual({ name: 'custom' })
  })

  it('round-trips every route', () => {
    for (const hash of ['#/', '#/study/book_01_the_happy_prince', '#/editor', '#/custom', '#/notebook', '#/review', '#/pdf-lesson/custom_user_1']) {
      expect(routeToHash(parseHash(hash))).toBe(hash)
    }
  })

  it('decodes and encodes ids safely', () => {
    expect(routeToHash({ name: 'study', bookId: 'a b' })).toBe('#/study/a%20b')
    expect(parseHash('#/study/a%20b')).toEqual({ name: 'study', bookId: 'a b' })
    expect(parseHash('#/study/%E0%A4%A')).toEqual({ name: 'library' })
  })
})
