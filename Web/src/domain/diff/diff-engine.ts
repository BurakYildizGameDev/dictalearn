import type { DiffOptions, DiffResult, DiffWord } from './types'

export function normalizeWord(word: string, options: DiffOptions): string {
  let w = word.replace(/[’‘]/g, "'").replace(/[“”]/g, '"')

  if (options.ignorePunctuation ?? true) {
    // Strip leading and trailing punctuation, keeping internal apostrophes/hyphens (e.g. don't, well-known)
    w = w.replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}]+$/gu, '')
  }

  if (options.ignoreCase ?? true) {
    w = w.toLowerCase()
  }

  return w
}

function splitWords(text: string): string[] {
  const clean = text.trim().replace(/[’‘]/g, "'").replace(/[“”]/g, '"')
  if (!clean) return []
  return clean.split(/\s+/).filter(Boolean)
}

export function computeWordDiff(
  expectedText: string,
  typedText: string,
  options: DiffOptions = {}
): DiffResult {
  const opts: DiffOptions = {
    ignoreCase: options.ignoreCase ?? true,
    ignorePunctuation: options.ignorePunctuation ?? true,
  }

  const expectedWords = splitWords(expectedText)
  const typedWords = splitWords(typedText)

  const n = expectedWords.length
  const m = typedWords.length

  if (n === 0 && m === 0) {
    return {
      words: [],
      correctCount: 0,
      expectedCount: 0,
      accuracy: 1,
      isPerfect: true,
    }
  }

  if (n === 0) {
    const words: DiffWord[] = typedWords.map((t) => ({ kind: 'extra', typed: t }))
    return {
      words,
      correctCount: 0,
      expectedCount: 0,
      accuracy: 0,
      isPerfect: false,
    }
  }

  if (m === 0) {
    const words: DiffWord[] = expectedWords.map((e) => ({ kind: 'missing', expected: e }))
    return {
      words,
      correctCount: 0,
      expectedCount: n,
      accuracy: 0,
      isPerfect: false,
    }
  }

  const normExpected = expectedWords.map((w) => normalizeWord(w, opts))
  const normTyped = typedWords.map((w) => normalizeWord(w, opts))

  // DP table for Levenshtein alignment
  // dp[i][j]: minimum cost to align expected[0..i-1] with typed[0..j-1]
  const dp: number[][] = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0))

  for (let i = 0; i <= n; i++) dp[i][0] = i
  for (let j = 0; j <= m; j++) dp[0][j] = j

  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      if (normExpected[i - 1] === normTyped[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1]
      } else {
        const subCost = dp[i - 1][j - 1] + 1.2 // substitute cost < insert + delete
        const delCost = dp[i - 1][j] + 1 // missing (expected deleted)
        const insCost = dp[i][j - 1] + 1 // extra (typed inserted)
        dp[i][j] = Math.min(subCost, delCost, insCost)
      }
    }
  }

  // Backtracking to find aligned words
  const resultWords: DiffWord[] = []
  let i = n
  let j = m

  while (i > 0 || j > 0) {
    if (i > 0 && j > 0) {
      if (normExpected[i - 1] === normTyped[j - 1]) {
        resultWords.push({
          kind: 'equal',
          expected: expectedWords[i - 1],
          typed: typedWords[j - 1],
        })
        i--
        j--
        continue
      }

      const subCost = dp[i - 1][j - 1] + 1.2
      const delCost = dp[i - 1][j] + 1
      const insCost = dp[i][j - 1] + 1
      const minCost = dp[i][j]

      if (Math.abs(minCost - subCost) < 1e-6) {
        resultWords.push({
          kind: 'substitute',
          expected: expectedWords[i - 1],
          typed: typedWords[j - 1],
        })
        i--
        j--
        continue
      }

      if (Math.abs(minCost - delCost) < 1e-6) {
        resultWords.push({
          kind: 'missing',
          expected: expectedWords[i - 1],
        })
        i--
        continue
      }

      if (Math.abs(minCost - insCost) < 1e-6) {
        resultWords.push({
          kind: 'extra',
          typed: typedWords[j - 1],
        })
        j--
        continue
      }
    }

    if (i > 0) {
      resultWords.push({
        kind: 'missing',
        expected: expectedWords[i - 1],
      })
      i--
    } else if (j > 0) {
      resultWords.push({
        kind: 'extra',
        typed: typedWords[j - 1],
      })
      j--
    }
  }

  resultWords.reverse()

  const correctCount = resultWords.filter((w) => w.kind === 'equal').length
  const accuracy = n > 0 ? correctCount / n : 0
  const isPerfect =
    accuracy === 1 &&
    !resultWords.some((w) => w.kind === 'substitute' || w.kind === 'missing' || w.kind === 'extra')

  return {
    words: resultWords,
    correctCount,
    expectedCount: n,
    accuracy,
    isPerfect,
  }
}
