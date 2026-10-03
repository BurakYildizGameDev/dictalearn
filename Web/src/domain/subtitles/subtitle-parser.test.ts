import { describe, it, expect } from 'vitest'
import {
  parseTimestampToMs,
  formatMsToTimestamp,
  cleanSubtitleText,
  parseSrt,
  parseVtt,
  parseSubtitles,
} from './subtitle-parser'

describe('Subtitle Parser (F4.1)', () => {
  describe('parseTimestampToMs', () => {
    it('parses standard hh:mm:ss,mmm (SRT)', () => {
      expect(parseTimestampToMs('00:00:01,000')).toBe(1000)
      expect(parseTimestampToMs('00:01:23,456')).toBe(83456)
      expect(parseTimestampToMs('01:00:00,000')).toBe(3600000)
    })

    it('parses standard hh:mm:ss.mmm (VTT)', () => {
      expect(parseTimestampToMs('00:00:01.500')).toBe(1500)
      expect(parseTimestampToMs('00:02:10.050')).toBe(130050)
    })

    it('parses short mm:ss.mmm (VTT)', () => {
      expect(parseTimestampToMs('01:23.456')).toBe(83456)
      expect(parseTimestampToMs('00:05.100')).toBe(5100)
    })

    it('handles padding of incomplete milliseconds', () => {
      expect(parseTimestampToMs('00:00:01,5')).toBe(1500)
      expect(parseTimestampToMs('00:00:01,50')).toBe(1500)
    })
  })

  describe('formatMsToTimestamp', () => {
    it('formats ms to SRT timestamp string', () => {
      expect(formatMsToTimestamp(83456, 'srt')).toBe('00:01:23,456')
      expect(formatMsToTimestamp(0, 'srt')).toBe('00:00:00,000')
    })

    it('formats ms to VTT timestamp string', () => {
      expect(formatMsToTimestamp(83456, 'vtt')).toBe('00:01:23.456')
    })
  })

  describe('cleanSubtitleText', () => {
    it('strips formatting tags and HTML entities', () => {
      const raw = '<i>Hello</i>, <b>world</b>! &amp; welcome &lt;here&gt;'
      expect(cleanSubtitleText(raw)).toBe('Hello, world! & welcome <here>')
    })

    it('normalizes multi-line and whitespace text', () => {
      const raw = 'This is a\nline with   extra\r\nspaces.'
      expect(cleanSubtitleText(raw)).toBe('This is a line with extra spaces.')
    })
  })

  describe('parseSrt', () => {
    it('parses standard SRT content into segments', () => {
      const srt = `
1
00:00:00,500 --> 00:00:04,200
He packed his small brown suitcase.

2
00:00:04,500 --> 00:00:08,100
The morning cold hit him immediately.
`
      const segments = parseSrt(srt)
      expect(segments).toHaveLength(2)
      expect(segments[0]).toEqual({
        id: 1,
        start_ms: 500,
        end_ms: 4200,
        text: 'He packed his small brown suitcase.',
      })
      expect(segments[1]).toEqual({
        id: 2,
        start_ms: 4500,
        end_ms: 8100,
        text: 'The morning cold hit him immediately.',
      })
    })

    it('handles multi-line text and tags inside SRT cues', () => {
      const srt = `
1
00:00:01,000 --> 00:00:03,000
<i>She looked around</i>
and <b>whispered</b>.
`
      const segments = parseSrt(srt)
      expect(segments).toHaveLength(1)
      expect(segments[0].text).toBe('She looked around and whispered.')
    })

    it('skips invalid blocks where end_ms <= start_ms or empty text', () => {
      const srt = `
1
00:00:05,000 --> 00:00:02,000
Invalid backwards time

2
00:00:03,000 --> 00:00:06,000
Valid sentence.
`
      const segments = parseSrt(srt)
      expect(segments).toHaveLength(1)
      expect(segments[0].text).toBe('Valid sentence.')
    })
  })

  describe('parseVtt', () => {
    it('parses standard WebVTT with header and cue ids', () => {
      const vtt = `WEBVTT - Chapter 1

cue-1
00:00:01.000 --> 00:00:04.000
He packed his small brown suitcase.

NOTE This is a comment

cue-2
00:04.500 --> 00:08.000
<v Speaker1>The morning cold hit him.</v>
`
      const segments = parseVtt(vtt)
      expect(segments).toHaveLength(2)
      expect(segments[0]).toEqual({
        id: 1,
        start_ms: 1000,
        end_ms: 4000,
        text: 'He packed his small brown suitcase.',
      })
      expect(segments[1]).toEqual({
        id: 2,
        start_ms: 4500,
        end_ms: 8000,
        text: 'The morning cold hit him.',
      })
    })
  })

  describe('parseSubtitles auto-detection', () => {
    it('detects WEBVTT header and parses with parseVtt', () => {
      const vtt = `WEBVTT\n\n00:00:01.000 --> 00:00:03.000\nHello from VTT!`
      const res = parseSubtitles(vtt)
      expect(res).toHaveLength(1)
      expect(res[0].text).toBe('Hello from VTT!')
    })

    it('detects SRT and parses with parseSrt', () => {
      const srt = `1\n00:00:01,000 --> 00:00:03,000\nHello from SRT!`
      const res = parseSubtitles(srt)
      expect(res).toHaveLength(1)
      expect(res[0].text).toBe('Hello from SRT!')
    })
  })
})
