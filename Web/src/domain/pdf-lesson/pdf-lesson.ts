// Turns the text of a user's PDF into a dictation lesson (no audio file: sentences are spoken by
// the speech engine, so segment timings are synthetic placeholders).

import type { Lesson } from '../lessons/types'
import { isProbablyEnglish } from './ocr-layout'

/** Synthetic slot per segment; the speech engine maps start_ms back to the sentence. */
export const SYNTHETIC_SEGMENT_MS = 10_000

const ABBREVIATIONS = ['Mr', 'Mrs', 'Ms', 'Dr', 'St', 'Mt', 'Jr', 'Sr', 'Prof', 'Capt', 'Col', 'Gen', 'vs', 'etc', 'e.g', 'i.e', 'No']
// Stands in for the dot of an abbreviation while splitting (private-use code point).
const DOT = '\uE000'
const TURKISH_CHARS = /[çğışöüÇĞİŞÖÜ]/
const MIN_WORDS = 3
const MAX_WORDS = 40

function wordCount(s: string): number {
  return s.split(/\s+/).filter(Boolean).length
}

/** English-looking text with lowercase letters, not Turkish, not a number/header. */
function looksLikeEnglish(s: string): boolean {
  if (TURKISH_CHARS.test(s)) return false
  if (!/[a-z]/.test(s)) return false // all-caps headers, numbers
  const letters = s.replace(/[^A-Za-z]/g, '').length
  if (letters / s.replace(/\s/g, '').length <= 0.6) return false
  // Catches Turkish without its special letters (e.g. after OCR with an English model).
  return isProbablyEnglish(s)
}

function normalizeText(text: string): string {
  return text
    .replace(/\r/g, '')
    .replace(/(\w)-\n(\w)/g, '$1$2') // hyphenated line breaks
    // OCR reads "[5]" as "[s]", "(2]", "[8j", "[10)"…: normalize line-leading markers to "[0]"
    .replace(/^[[(][0-9A-Za-z]{1,3}[\])jJ]\s*/gm, '[0] ')
    .replace(/[ \t]+/g, ' ')
}

function splitSentences(paragraph: string): string[] {
  const protectedText = ABBREVIATIONS.reduce(
    (acc, abbr) => acc.replace(new RegExp(`\\b${abbr.replace('.', '\\.')}\\.`, 'g'), `${abbr}${DOT}`),
    paragraph
  )
  return protectedText
    .split(/(?<=[.!?]["”’)]?)\s+(?=["“‘(]?[A-Z0-9])/)
    .map((s) => s.replaceAll(DOT, '.').trim())
    .filter(Boolean)
}

function validSentence(s: string): boolean {
  const n = wordCount(s)
  return n >= MIN_WORDS && n <= MAX_WORDS && looksLikeEnglish(s)
}

/**
 * Parallel-text PDFs number every sentence ("[12] English…" then "[12] Türkçe…"). Splitting on the
 * markers and judging each whole block is far more reliable than judging single lines, because a
 * wrapped Turkish line can contain no Turkish-specific letters at all ("oldu.").
 */
function numberedBlocks(normalized: string): string[] | null {
  const parts = normalized.split(/\[\d{1,4}\]/)
  if (parts.length < 6) return null
  return parts
    .slice(1)
    .map((block) => block.replace(/\s+/g, ' ').trim())
    .filter((block) => block && !TURKISH_CHARS.test(block))
    .flatMap((block) => splitSentences(block))
    .filter(validSentence)
}

export function extractSentences(text: string): string[] {
  const normalized = normalizeText(text)
  const numbered = numberedBlocks(normalized)
  if (numbered && numbered.length >= 5) return dedupe(numbered)
  // Keep only English lines first so Turkish parallel columns don't merge into sentences.
  const englishLines = normalized
    .split('\n')
    .map((l) => l.trim())
    .filter((l) => l && looksLikeEnglish(l))

  const sentences = toParagraphs(englishLines)
    .flatMap((p) => splitSentences(p))
    .filter((s) => /[.!?]["”’)]?$/.test(s))
    .filter(validSentence)

  if (sentences.length >= 5 || (sentences.length > 0 && englishLines.length < 10)) {
    return dedupe(sentences)
  }

  // Word lists / picture books: use meaningful lines instead.
  const lines = englishLines.filter((l) => {
    const n = wordCount(l)
    return n >= 2 && n <= 20
  })
  return dedupe(lines.length > 0 ? lines : sentences)
}

const ENDS_SENTENCE = /[.!?:;]["”’)]?$/
const STARTS_UPPER = /^["“‘(]?[A-Z]/

/**
 * Joins wrapped lines into paragraphs. A short capitalised line without end punctuation that is
 * followed by another capitalised line is a heading ("Contents", "About this book"): it closes the
 * paragraph instead of being glued to the next sentence.
 */
function toParagraphs(lines: string[]): string[] {
  const paragraphs: string[] = []
  let current: string[] = []
  lines.forEach((line, i) => {
    const next = lines[i + 1] ?? ''
    const heading =
      wordCount(line) <= 8 && !ENDS_SENTENCE.test(line) && STARTS_UPPER.test(line) && STARTS_UPPER.test(next)
    if (heading) {
      if (current.length) paragraphs.push(current.join(' '))
      current = []
      return
    }
    current.push(line)
  })
  if (current.length) paragraphs.push(current.join(' '))
  return paragraphs
}

function dedupe(items: string[]): string[] {
  const seen = new Set<string>()
  return items.filter((s) => {
    const key = s.toLowerCase()
    if (seen.has(key)) return false
    seen.add(key)
    return true
  })
}

export function buildPdfLesson(lessonId: string, fileName: string, sentences: string[]): Lesson {
  return {
    schema_version: 1,
    lesson_id: lessonId,
    title: fileName.replace(/\.pdf$/i, ''),
    source_lang: 'en',
    target_lang: 'tr',
    audio_file: 'speech-synthesis',
    attribution: { source: `Kullanıcının PDF dosyası: ${fileName}`, license: 'Personal' },
    segments: sentences.map((text, i) => ({
      id: i + 1,
      start_ms: i * SYNTHETIC_SEGMENT_MS,
      end_ms: (i + 1) * SYNTHETIC_SEGMENT_MS - 1,
      text,
    })),
  }
}
