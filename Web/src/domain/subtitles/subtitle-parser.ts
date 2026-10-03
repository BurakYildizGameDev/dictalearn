import type { Segment } from '../lessons/types'

/**
 * Parses timestamp string into milliseconds.
 * Supports:
 * - SRT style: '00:01:23,456'
 * - VTT style: '00:01:23.456' or '01:23.456'
 */
export function parseTimestampToMs(timeStr: string): number {
  const trimmed = timeStr.trim()
  const [timePart, millisPart = '0'] = trimmed.split(/[,.]/)

  const timeTokens = timePart.split(':').map((t) => parseInt(t, 10))
  let hours = 0
  let minutes = 0
  let seconds = 0

  if (timeTokens.length === 3) {
    hours = isNaN(timeTokens[0]) ? 0 : timeTokens[0]
    minutes = isNaN(timeTokens[1]) ? 0 : timeTokens[1]
    seconds = isNaN(timeTokens[2]) ? 0 : timeTokens[2]
  } else if (timeTokens.length === 2) {
    minutes = isNaN(timeTokens[0]) ? 0 : timeTokens[0]
    seconds = isNaN(timeTokens[1]) ? 0 : timeTokens[1]
  } else if (timeTokens.length === 1) {
    seconds = isNaN(timeTokens[0]) ? 0 : timeTokens[0]
  }

  // Normalize milliseconds (e.g. '5' -> 500, '50' -> 500, '500' -> 500)
  const normalizedMillisStr = millisPart.padEnd(3, '0').slice(0, 3)
  const millis = parseInt(normalizedMillisStr, 10) || 0

  return hours * 3600000 + minutes * 60000 + seconds * 1000 + millis
}

/**
 * Converts milliseconds to formatted time string:
 * format 'srt': '00:01:23,456'
 * format 'vtt': '00:01:23.456'
 */
export function formatMsToTimestamp(ms: number, format: 'srt' | 'vtt' = 'srt'): string {
  const safeMs = Math.max(0, Math.floor(ms))
  const hours = Math.floor(safeMs / 3600000)
  const minutes = Math.floor((safeMs % 3600000) / 60000)
  const seconds = Math.floor((safeMs % 60000) / 1000)
  const millis = safeMs % 1000

  const hh = String(hours).padStart(2, '0')
  const mm = String(minutes).padStart(2, '0')
  const ss = String(seconds).padStart(2, '0')
  const mmm = String(millis).padStart(3, '0')

  const separator = format === 'srt' ? ',' : '.'
  return `${hh}:${mm}:${ss}${separator}${mmm}`
}

/**
 * Strips subtitle tags (like <i>, <b>, <v Speaker>, <c.color>) and unescapes entities.
 */
export function cleanSubtitleText(raw: string): string {
  return raw
    .replace(/<[^>]+>/g, '') // remove tags
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&nbsp;/g, ' ')
    .replace(/\r\n/g, ' ')
    .replace(/[\r\n]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
}

/**
 * Parses raw SRT format string into Segment array.
 */
export function parseSrt(rawSrt: string): Segment[] {
  const normalized = rawSrt.replace(/\r\n/g, '\n').replace(/\r/g, '\n')
  const blocks = normalized.split(/\n\s*\n/)
  const segments: Segment[] = []
  let nextId = 1

  const timeArrowRegex = /((?:\d{1,2}:)?\d{2}:\d{2}[,.]\d{1,3})\s*-->\s*((?:\d{1,2}:)?\d{2}:\d{2}[,.]\d{1,3})/

  for (const block of blocks) {
    const lines = block
      .split('\n')
      .map((l) => l.trim())
      .filter((l) => l.length > 0)

    if (lines.length === 0) continue

    // Find line containing '-->'
    const timeLineIndex = lines.findIndex((l) => timeArrowRegex.test(l))
    if (timeLineIndex === -1) continue

    const match = lines[timeLineIndex].match(timeArrowRegex)
    if (!match) continue

    const startMs = parseTimestampToMs(match[1])
    const endMs = parseTimestampToMs(match[2])

    if (endMs <= startMs) continue

    // Text is everything after the timestamp line
    const textLines = lines.slice(timeLineIndex + 1)
    const text = cleanSubtitleText(textLines.join(' '))

    if (text.length === 0) continue

    segments.push({
      id: nextId++,
      start_ms: startMs,
      end_ms: endMs,
      text,
    })
  }

  return segments
}

/**
 * Parses raw WebVTT format string into Segment array.
 */
export function parseVtt(rawVtt: string): Segment[] {
  const normalized = rawVtt.replace(/\r\n/g, '\n').replace(/\r/g, '\n')
  const blocks = normalized.split(/\n\s*\n/)
  const segments: Segment[] = []
  let nextId = 1

  const timeArrowRegex = /((?:\d{1,2}:)?\d{2}:\d{2}[,.]\d{1,3})\s*-->\s*((?:\d{1,2}:)?\d{2}:\d{2}[,.]\d{1,3})/

  for (const block of blocks) {
    const lines = block
      .split('\n')
      .map((l) => l.trim())
      .filter((l) => l.length > 0)

    if (lines.length === 0) continue

    // Ignore WEBVTT header and NOTE comments
    if (lines[0].startsWith('WEBVTT') || lines[0].startsWith('NOTE') || lines[0].startsWith('STYLE')) {
      continue
    }

    const timeLineIndex = lines.findIndex((l) => timeArrowRegex.test(l))
    if (timeLineIndex === -1) continue

    const match = lines[timeLineIndex].match(timeArrowRegex)
    if (!match) continue

    const startMs = parseTimestampToMs(match[1])
    const endMs = parseTimestampToMs(match[2])

    if (endMs <= startMs) continue

    const textLines = lines.slice(timeLineIndex + 1)
    const text = cleanSubtitleText(textLines.join(' '))

    if (text.length === 0) continue

    segments.push({
      id: nextId++,
      start_ms: startMs,
      end_ms: endMs,
      text,
    })
  }

  return segments
}

/**
 * Auto-detects format (SRT vs VTT) and parses into Segment array.
 */
export function parseSubtitles(content: string): Segment[] {
  if (content.trim().startsWith('WEBVTT')) {
    return parseVtt(content)
  }
  return parseSrt(content)
}
