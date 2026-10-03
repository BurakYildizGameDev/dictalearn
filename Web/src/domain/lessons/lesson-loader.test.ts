import { describe, it, expect, vi } from 'vitest'
import { loadLessonFromUrl } from './lesson-loader'

describe('Lesson Loader', () => {
  it('loads and validates a valid lesson via fetch', async () => {
    const validJson = {
      schema_version: 1,
      lesson_id: 'test_ch01',
      title: 'Test',
      source_lang: 'en',
      target_lang: 'tr',
      audio_file: 'audio.wav',
      segments: [{ id: 1, start_ms: 0, end_ms: 1000, text: 'Hello' }],
    }

    vi.spyOn(globalThis, 'fetch').mockResolvedValueOnce({
      ok: true,
      json: async () => validJson,
    } as Response)

    const lesson = await loadLessonFromUrl('/lessons/test/lesson.json')
    expect(lesson.lesson_id).toBe('test_ch01')
  })

  it('throws an error when fetch fails or response is not ok', async () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValueOnce({
      ok: false,
      statusText: 'Not Found',
    } as Response)

    await expect(loadLessonFromUrl('/lessons/missing/lesson.json')).rejects.toThrow(
      'Failed to fetch lesson'
    )
  })

  it('throws an error when JSON validation fails', async () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValueOnce({
      ok: true,
      json: async () => ({ schema_version: 99 }),
    } as Response)

    await expect(loadLessonFromUrl('/lessons/bad/lesson.json')).rejects.toThrow(
      'Lesson validation failed'
    )
  })
})
