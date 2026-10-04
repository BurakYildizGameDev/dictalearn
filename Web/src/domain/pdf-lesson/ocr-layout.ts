// Layout and language helpers for OCR output of scanned pages.

export interface OcrWord {
  text: string
  x0: number
  x1: number
}

export interface OcrLine {
  words: OcrWord[]
}

/** A gap this wide (fraction of page width) clearly separates two columns. */
const WIDE_GAP = 0.06
/** Tolerance around the detected right-column start. */
const COLUMN_TOLERANCE = 0.025

function median(values: number[]): number {
  const sorted = [...values].sort((a, b) => a - b)
  return sorted[Math.floor(sorted.length / 2)]
}

/**
 * Where the right column starts, learned from lines whose columns are clearly apart. When the left
 * column is full, the gutter can shrink to a normal word gap, so the position is what matters.
 */
function rightColumnStart(lines: OcrWord[][], pageWidth: number): number | null {
  const starts: number[] = []
  for (const words of lines) {
    for (let i = 1; i < words.length; i++) {
      if (words[i].x0 - words[i - 1].x1 > pageWidth * WIDE_GAP && words[i].x0 >= pageWidth * 0.35) {
        starts.push(words[i].x0)
        break
      }
    }
  }
  return starts.length >= 2 ? median(starts) : null
}

/**
 * Tesseract reads straight across two-column pages ("…cried the [1] Genç Öğrenci…"). Lines are split
 * where a word starts at the right column, and the right column is read after the left one.
 * Single-column pages come out unchanged.
 */
export function orderOcrLines(lines: OcrLine[], pageWidth: number): string {
  const wordLines = lines.map((l) => l.words.filter((wd) => wd.text.trim())).filter((ws) => ws.length > 0)
  const column = rightColumnStart(wordLines, pageWidth)
  const left: string[] = []
  const right: string[] = []
  for (const words of wordLines) {
    let split = -1
    if (column !== null) {
      split = words.findIndex(
        (wd, i) => i > 0 && Math.abs(wd.x0 - column) <= pageWidth * COLUMN_TOLERANCE && wd.x0 > words[i - 1].x1
      )
      if (split === -1 && words[0].x0 >= column - pageWidth * COLUMN_TOLERANCE) split = 0
    }
    const leftPart = split === -1 ? words : words.slice(0, split)
    const rightPart = split === -1 ? [] : words.slice(split)
    if (leftPart.length) left.push(leftPart.map((wd) => wd.text).join(' '))
    if (rightPart.length) right.push(rightPart.map((wd) => wd.text).join(' '))
  }
  return [...left, ...right].join('\n')
}

// Frequent English function words; Turkish text (even with its letters flattened by an English
// OCR model) contains almost none of them.
const ENGLISH_FUNCTION_WORDS = new Set(
  (
    'the a an and or but of to in on at for with from by as is are was were be been it its he she ' +
    'his her him they them their we our you your i me my this that these those there here not no ' +
    'so if then than when what which who how all had has have do did would could should will can ' +
    'into over up out about after before again very just only one'
  ).split(' ')
)

export function englishWordRatio(text: string): number {
  const words = text.toLowerCase().match(/[a-z']+/g) ?? []
  if (words.length === 0) return 0
  return words.filter((wd) => ENGLISH_FUNCTION_WORDS.has(wd)).length / words.length
}

/** Short fragments (< 4 words) cannot be judged and are allowed. */
export function isProbablyEnglish(text: string): boolean {
  const words = text.match(/[A-Za-z']+/g) ?? []
  if (words.length < 4) return true
  return englishWordRatio(text) >= 0.12
}
