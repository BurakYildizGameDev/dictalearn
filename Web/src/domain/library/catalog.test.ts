import { describe, it, expect } from 'vitest'
import { CATALOG, filterCatalog, lessonAssetUrls, findBook, LEVEL_LABELS } from './catalog'

describe('Library catalog', () => {
  it('has unique ids', () => {
    const ids = CATALOG.map((b) => b.id)
    expect(new Set(ids).size).toBe(ids.length)
  })

  it('contains all 36 graded books with consistent level and page metadata', () => {
    const books = CATALOG.filter((b) => b.kind === 'book')
    expect(books).toHaveLength(36)
    for (const book of books) {
      expect(LEVEL_LABELS[book.level]).toBeDefined()
      expect(book.sentences).toBe(book.pages * 20)
    }
  })

  it('builds asset urls relative to the deployment base url', () => {
    const book = findBook('book_01_the_happy_prince')!
    const urls = lessonAssetUrls(book, '/dictalearn/')
    expect(urls.jsonUrl).toBe('/dictalearn/lessons/book_01_the_happy_prince/lesson.json')
    expect(urls.audioUrl).toBe('/dictalearn/lessons/book_01_the_happy_prince/audio.mp3')
    expect(urls.pdfUrl).toBe('/dictalearn/lessons/book_01_the_happy_prince/book_01_the_happy_prince.pdf')
  })

  it('tolerates a base url without trailing slash and books without pdf', () => {
    const demo = findBook('sample_ch01')!
    const urls = lessonAssetUrls(demo, '/app')
    expect(urls.jsonUrl).toBe('/app/lessons/sample_ch01/lesson.json')
    expect(urls.pdfUrl).toBeUndefined()
  })

  it('filters by level', () => {
    const level2 = filterCatalog(CATALOG, { level: 2 })
    expect(level2.length).toBeGreaterThan(0)
    expect(level2.every((b) => b.level === 2)).toBe(true)
  })

  it('searches title, turkish title and author case-insensitively', () => {
    expect(filterCatalog(CATALOG, { query: 'DRACULA' }).map((b) => b.id)).toContain('book_32_dracula')
    expect(filterCatalog(CATALOG, { query: 'hayalet' }).map((b) => b.id)).toContain(
      'book_35_the_canterville_ghost'
    )
    expect(filterCatalog(CATALOG, { query: 'wilde' }).length).toBeGreaterThanOrEqual(5)
  })

  it('returns everything for an empty filter', () => {
    expect(filterCatalog(CATALOG, {})).toHaveLength(CATALOG.length)
  })
})
