// Word-by-Word Mode Domain Logic & Tokenization (Faz 6)

export interface WordToken {
  index: number
  raw: string // Original token with punctuation, e.g. "Every,"
  clean: string // Normalized token without boundary punctuation, lowercased, e.g. "every"
  punctuation: string // Trailing punctuation for display, e.g. "," or "."
  isRevealed: boolean
}

/**
 * Normalizes a word for comparison by removing boundary punctuation
 * and converting to lower case.
 */
export function normalizeWord(word: string): string {
  return word
    .trim()
    .replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}]+$/gu, '')
    .toLowerCase()
}

/**
 * Tokenizes sentence text into word tokens for word-by-word practice.
 */
export function tokenizeSentenceToWords(text: string): WordToken[] {
  if (!text || !text.trim()) return []

  const rawTokens = text.trim().split(/\s+/).filter(Boolean)

  return rawTokens.map((raw, index) => {
    const clean = normalizeWord(raw)
    const punctMatch = raw.match(/[^\p{L}\p{N}]+$/u)
    const punctuation = punctMatch ? punctMatch[0] : ''

    return {
      index,
      raw,
      clean,
      punctuation,
      isRevealed: false,
    }
  })
}

/**
 * Checks if user typed word matches the target clean word.
 * Also tolerates missing internal apostrophes (e.g., "didnt" matching "didn't").
 */
export function checkWordMatch(typed: string, targetClean: string): boolean {
  const cleanTyped = normalizeWord(typed)
  if (!cleanTyped || !targetClean) return false

  if (cleanTyped === targetClean) return true

  // Forgiving apostrophe tolerance (e.g. didnt == didn't, travellers == traveller's)
  const stripApostrophes = (s: string) => s.replace(/['’]/g, '')
  if (stripApostrophes(cleanTyped) === stripApostrophes(targetClean)) {
    return true
  }

  return false
}
