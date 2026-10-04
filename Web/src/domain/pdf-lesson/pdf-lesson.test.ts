import { describe, it, expect } from 'vitest'
import { extractSentences, buildPdfLesson, SYNTHETIC_SEGMENT_MS } from './pdf-lesson'

describe('extractSentences', () => {
  it('splits prose into sentences and joins hyphenated line breaks', () => {
    const text = 'Tom packed his bag. Then he left the house!\nHe walked to the sta-\ntion quickly. "Wait for me," said Ann.'
    expect(extractSentences(text)).toEqual([
      'Tom packed his bag.',
      'Then he left the house!',
      'He walked to the station quickly.',
      '"Wait for me," said Ann.',
    ])
  })

  it('does not split after common abbreviations', () => {
    expect(extractSentences('Mr. Holmes met Dr. Watson at the door. They talked for hours.')).toEqual([
      'Mr. Holmes met Dr. Watson at the door.',
      'They talked for hours.',
    ])
  })

  it('drops Turkish parallel text, all-caps headers and page numbers', () => {
    const text = [
      'DICTALEARN GRADED CLASSICS',
      'Sayfa 1 / 16',
      'The prince stood on a tall column.',
      'Prens yüksek bir sütunun üzerinde duruyordu.',
      '12',
      'Everyone admired him very much.',
    ].join('\n')
    expect(extractSentences(text)).toEqual(['The prince stood on a tall column.', 'Everyone admired him very much.'])
  })

  it('uses [n] markers of parallel-text PDFs and drops the Turkish blocks', () => {
    const text = [
      'ENGLISH STORY TEXT (ORİJİNAL İNGİLİZCE)',
      '[1] "She said that she would dance with me," cried the',
      'young Student.',
      '[1] Genç Öğrenci "Benimle dans edeceğini söyledi," diye',
      'yakındı.',
      '[2] "Yet in all my garden there is no red rose." [2] "Fakat bahçemde hiç kırmızı gül yok."',
      '[3] He was sad and his life was ruined.',
      '[3] Hayatı sefil ve harap',
      'oldu.',
      '[4] The Nightingale heard his sorrowful words.',
      '[4] Bülbül onun kederli sözlerini işitti.',
      '[5] She flew over the garden like a shadow.',
      '[5] Bahçenin üzerinden bir gölge gibi uçtu.',
    ].join('\n')
    expect(extractSentences(text)).toEqual([
      '"She said that she would dance with me," cried the young Student.',
      '"Yet in all my garden there is no red rose."',
      'He was sad and his life was ruined.',
      'The Nightingale heard his sorrowful words.',
      'She flew over the garden like a shadow.',
    ])
  })

  it('does not glue headings to the following sentence', () => {
    const text = 'Contents\nAbout this book\nYou will find each of these words in bold.\nMeet the Flyers\nThe children love going to the park.'
    expect(extractSentences(text)).toEqual([
      'You will find each of these words in bold.',
      'The children love going to the park.',
    ])
  })

  it('falls back to meaningful lines for word lists without sentence punctuation', () => {
    const text = 'Animals\nthe big brown bear\na small grey mouse\na tall giraffe\nan old horse\na fast rabbit\n7'
    expect(extractSentences(text)).toEqual([
      'the big brown bear',
      'a small grey mouse',
      'a tall giraffe',
      'an old horse',
      'a fast rabbit',
    ])
  })

  it('returns nothing for scanned PDFs without text', () => {
    expect(extractSentences('   \n  \n')).toEqual([])
  })
})

describe('buildPdfLesson', () => {
  it('creates a schema v1 lesson with synthetic, ordered millisecond timings', () => {
    const lesson = buildPdfLesson('pdf_custom_1', 'Benim Kitabım.pdf', ['One two three.', 'Four five six.'])
    expect(lesson.schema_version).toBe(1)
    expect(lesson.lesson_id).toBe('pdf_custom_1')
    expect(lesson.title).toBe('Benim Kitabım')
    expect(lesson.segments.map((s) => [s.id, s.start_ms, s.end_ms, s.text])).toEqual([
      [1, 0, SYNTHETIC_SEGMENT_MS - 1, 'One two three.'],
      [2, SYNTHETIC_SEGMENT_MS, 2 * SYNTHETIC_SEGMENT_MS - 1, 'Four five six.'],
    ])
    expect(Number.isInteger(lesson.segments[1].start_ms)).toBe(true)
  })
})
