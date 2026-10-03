import { describe, it, expect } from 'vitest'
import { validateLesson } from './lesson-validator'
import type { Lesson } from './types'

describe('Lesson Validator', () => {
  const validLesson: Lesson = {
    schema_version: 1,
    lesson_id: 'sample_ch01',
    title: 'Chapter 1: The Departure',
    source_lang: 'en',
    target_lang: 'tr',
    audio_file: 'audio.wav',
    attribution: {
      source: 'LibriVox',
      license: 'Public Domain',
    },
    segments: [
      {
        id: 1,
        start_ms: 0,
        end_ms: 4000,
        text: 'He packed his small brown suitcase.',
        translation: 'Küçük kahverengi bavulunu topladı.',
        notes: 'packed: past tense',
      },
      {
        id: 2,
        start_ms: 4800,
        end_ms: 7600,
        text: 'The morning cold hit him immediately.',
        translation: 'Sabahın soğuğu anında yüzüne çarptı.',
      },
    ],
  }

  it('validates a correct lesson structure successfully', () => {
    const result = validateLesson(validLesson)
    expect(result.isValid).toBe(true)
    expect(result.errors).toHaveLength(0)
    expect(result.lesson).toEqual(validLesson)
  })

  it('fails when schema_version is unsupported', () => {
    const invalid = { ...validLesson, schema_version: 2 }
    const result = validateLesson(invalid)
    expect(result.isValid).toBe(false)
    expect(result.errors).toContain('Unsupported schema_version: 2. Expected: 1')
  })

  it('fails when required fields are missing', () => {
    const invalid = { ...validLesson, lesson_id: '', title: '' }
    const result = validateLesson(invalid)
    expect(result.isValid).toBe(false)
    expect(result.errors.some((e) => e.includes('lesson_id'))).toBe(true)
    expect(result.errors.some((e) => e.includes('title'))).toBe(true)
  })

  it('fails when segments array is empty', () => {
    const invalid = { ...validLesson, segments: [] }
    const result = validateLesson(invalid)
    expect(result.isValid).toBe(false)
    expect(result.errors.some((e) => e.includes('segments'))).toBe(true)
  })

  it('fails when segment IDs are not strictly ascending', () => {
    const invalid: Lesson = {
      ...validLesson,
      segments: [
        { id: 2, start_ms: 0, end_ms: 1000, text: 'First' },
        { id: 1, start_ms: 1200, end_ms: 2000, text: 'Second' },
      ],
    }
    const result = validateLesson(invalid)
    expect(result.isValid).toBe(false)
    expect(result.errors.some((e) => e.includes('strictly ascending'))).toBe(true)
  })

  it('fails when segment start_ms is greater than or equal to end_ms', () => {
    const invalid: Lesson = {
      ...validLesson,
      segments: [
        { id: 1, start_ms: 3000, end_ms: 2000, text: 'Invalid time' },
      ],
    }
    const result = validateLesson(invalid)
    expect(result.isValid).toBe(false)
    expect(result.errors.some((e) => e.includes('start_ms must be less than end_ms'))).toBe(true)
  })

  it('fails when segments overlap in time', () => {
    const invalid: Lesson = {
      ...validLesson,
      segments: [
        { id: 1, start_ms: 0, end_ms: 5000, text: 'Segment 1' },
        { id: 2, start_ms: 4500, end_ms: 8000, text: 'Segment 2 overlaps' },
      ],
    }
    const result = validateLesson(invalid)
    expect(result.isValid).toBe(false)
    expect(result.errors.some((e) => e.includes('overlap'))).toBe(true)
  })

  it('fails when segment text is empty', () => {
    const invalid: Lesson = {
      ...validLesson,
      segments: [
        { id: 1, start_ms: 0, end_ms: 2000, text: '   ' },
      ],
    }
    const result = validateLesson(invalid)
    expect(result.isValid).toBe(false)
    expect(result.errors.some((e) => e.includes('text is empty'))).toBe(true)
  })
})
