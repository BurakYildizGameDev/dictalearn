import { describe, it, expect } from 'vitest'
import { isPdfFile, asPdfBlob } from './pdf-storage'

describe('pdf file helpers', () => {
  it('accepts files reported as application/pdf', () => {
    expect(isPdfFile({ name: 'book.pdf', type: 'application/pdf' })).toBe(true)
  })

  it('accepts .pdf files with an empty or generic MIME type (Windows without a PDF reader)', () => {
    expect(isPdfFile({ name: 'Kitap.PDF', type: '' })).toBe(true)
    expect(isPdfFile({ name: 'kitap.pdf', type: 'application/octet-stream' })).toBe(true)
  })

  it('rejects non-pdf files', () => {
    expect(isPdfFile({ name: 'notes.txt', type: 'text/plain' })).toBe(false)
    expect(isPdfFile({ name: 'fake.pdf', type: 'image/png' })).toBe(false)
    expect(isPdfFile({ name: 'noext', type: '' })).toBe(false)
  })

  it('gives untyped blobs the pdf MIME type so browsers render instead of downloading', () => {
    const untyped = new Blob(['%PDF-1.4'])
    expect(asPdfBlob(untyped).type).toBe('application/pdf')
    const typed = new Blob(['%PDF-1.4'], { type: 'application/pdf' })
    expect(asPdfBlob(typed)).toBe(typed)
  })
})
