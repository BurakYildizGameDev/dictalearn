import { describe, it, expect } from 'vitest'
import { orderOcrLines, englishWordRatio, isProbablyEnglish, type OcrLine } from './ocr-layout'

const w = (text: string, x0: number, x1: number) => ({ text, x0, x1 })

describe('orderOcrLines', () => {
  it('splits two-column lines at the gutter and reads the left column first', () => {
    const lines: OcrLine[] = [
      { words: [w('[1]', 10, 40), w('She', 45, 80), w('said', 85, 130), w('[1]', 520, 550), w('Genç', 555, 600), w('kız', 605, 640)] },
      { words: [w('young', 10, 70), w('Student.', 75, 150), w('diye', 520, 560), w('yakındı.', 565, 640)] },
    ]
    expect(orderOcrLines(lines, 1000)).toBe('[1] She said\nyoung Student.\n[1] Genç kız\ndiye yakındı.')
  })

  it('keeps single-column text in order', () => {
    const lines: OcrLine[] = [
      { words: [w('The', 50, 90), w('prince', 95, 160), w('was', 165, 200), w('happy.', 205, 270)] },
      { words: [w('Everyone', 50, 150), w('loved', 155, 210), w('him.', 215, 260)] },
    ]
    expect(orderOcrLines(lines, 1000)).toBe('The prince was happy.\nEveryone loved him.')
  })

  it('splits at the learned column start even when the gutter is as small as a word gap', () => {
    const lines: OcrLine[] = [
      { words: [w('short', 10, 60), w('line.', 65, 110), w('Kısa', 520, 560)] },
      { words: [w('another', 10, 80), w('one.', 85, 120), w('Diğer', 520, 570)] },
      { words: [w('third', 10, 60), w('row.', 65, 100), w('Üçüncü', 521, 580)] },
      // full left column: the gap before the right column is only 12px
      { words: [w('[1]', 10, 40), w('A', 45, 55), w('very', 60, 100), w('long', 105, 470), w('cried', 475, 508), w('[1]', 520, 545), w('Genç', 550, 600)] },
    ]
    expect(orderOcrLines(lines, 1000)).toBe(
      'short line.\nanother one.\nthird row.\n[1] A very long cried\nKısa\nDiğer\nÜçüncü\n[1] Genç'
    )
  })

  it('does not split single-column pages with an occasional wide gap', () => {
    const lines: OcrLine[] = [{ words: [w('Chapter', 10, 120), w('One', 600, 680)] }]
    expect(orderOcrLines(lines, 1000)).toBe('Chapter One')
  })
})

describe('English detection by function words', () => {
  it('recognises English even without punctuation', () => {
    expect(englishWordRatio('She said that she would dance with me if I brought her red roses')).toBeGreaterThan(0.3)
  })

  it('rejects Turkish whose letters were flattened by OCR', () => {
    expect(isProbablyEnglish('Fakat bitin bahgemde higbir yerde tek bir kirmizi gll dahi bulunmuyor.')).toBe(false)
    expect(isProbablyEnglish('Geng Ogrenci Ona kirmizi guller gotururSem benimle dans edecegini soyledi')).toBe(false)
  })

  it('accepts typical English sentences and short phrases', () => {
    expect(isProbablyEnglish('From her high nest in the holm-oak tree, the gentle Nightingale heard his words.')).toBe(true)
    expect(isProbablyEnglish('a tall giraffe')).toBe(true) // too short to judge: allowed
  })
})
