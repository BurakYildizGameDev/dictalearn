import type { Lesson, ValidationResult } from './types'

export function validateLesson(data: unknown): ValidationResult {
  const errors: string[] = []

  if (!data || typeof data !== 'object') {
    return { isValid: false, errors: ['Lesson data must be a valid JSON object.'] }
  }

  const raw = data as Record<string, unknown>

  // Check schema_version
  if (raw.schema_version !== 1) {
    errors.push(`Unsupported schema_version: ${String(raw.schema_version)}. Expected: 1`)
  }

  // Check mandatory string fields
  if (!raw.lesson_id || typeof raw.lesson_id !== 'string' || !raw.lesson_id.trim()) {
    errors.push('Missing or invalid lesson_id. Must be a non-empty string.')
  }

  if (!raw.title || typeof raw.title !== 'string' || !raw.title.trim()) {
    errors.push('Missing or invalid title. Must be a non-empty string.')
  }

  if (!raw.audio_file || typeof raw.audio_file !== 'string' || !raw.audio_file.trim()) {
    errors.push('Missing or invalid audio_file. Must be a non-empty string.')
  }

  // Check segments
  if (!Array.isArray(raw.segments) || raw.segments.length === 0) {
    errors.push('Lesson must contain a non-empty array of segments.')
  } else {
    let lastId = 0
    let lastEndMs = -1

    for (let i = 0; i < raw.segments.length; i++) {
      const seg = raw.segments[i] as Record<string, unknown>

      if (typeof seg.id !== 'number' || seg.id <= lastId) {
        errors.push(`Segment at index ${i} has invalid id: ${String(seg.id)}. Segment IDs must be strictly ascending integers.`)
      } else {
        lastId = seg.id
      }

      if (typeof seg.start_ms !== 'number' || typeof seg.end_ms !== 'number') {
        errors.push(`Segment ${String(seg.id)} must have numeric start_ms and end_ms.`)
      } else {
        if (seg.start_ms >= seg.end_ms) {
          errors.push(`Segment ${String(seg.id)}: start_ms must be less than end_ms (${String(seg.start_ms)} >= ${String(seg.end_ms)}).`)
        }

        if (seg.start_ms < lastEndMs) {
          errors.push(`Segment ${String(seg.id)} overlaps with preceding segment (${String(seg.start_ms)} < ${String(lastEndMs)}).`)
        }
        lastEndMs = seg.end_ms
      }

      if (typeof seg.text !== 'string' || !seg.text.trim()) {
        errors.push(`Segment ${String(seg.id)}: text is empty.`)
      }
    }
  }

  if (errors.length > 0) {
    return { isValid: false, errors }
  }

  return {
    isValid: true,
    errors: [],
    lesson: data as Lesson,
  }
}
