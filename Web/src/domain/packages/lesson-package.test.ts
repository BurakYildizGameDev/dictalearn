import { describe, it, expect, vi, beforeEach } from 'vitest'
import { exportLessonZip, importLessonZip } from './lesson-package'
import type { Lesson } from '../lessons/types'
import JSZip from 'jszip'

describe('Lesson Package Manager (F4.2 Zip Export/Import)', () => {
  const dummyLesson: Lesson = {
    schema_version: 1,
    lesson_id: 'sample_pack',
    title: 'Sample Package Lesson',
    source_lang: 'en',
    target_lang: 'tr',
    audio_file: 'audio.wav',
    segments: [
      {
        id: 1,
        start_ms: 0,
        end_ms: 4000,
        text: 'He packed his small brown suitcase.',
        translation: 'Küçük bavulunu topladı.',
      },
    ],
  }

  beforeEach(() => {
    globalThis.URL.createObjectURL = vi.fn().mockReturnValue('blob:mock-url')
    globalThis.URL.revokeObjectURL = vi.fn()
  })

  it('exports a lesson and audio blob into a valid zip archive', async () => {
    const fakeAudioBlob = new Blob(['fake audio content'], { type: 'audio/wav' })
    const zipBlob = await exportLessonZip(dummyLesson, fakeAudioBlob)

    expect(zipBlob).toBeInstanceOf(Blob)
    expect(zipBlob.size).toBeGreaterThan(0)

    // Verify zip contains lesson.json and audio.wav
    const unzipped = await JSZip.loadAsync(zipBlob)
    expect(unzipped.file('lesson.json')).not.toBeNull()
    expect(unzipped.file('audio.wav')).not.toBeNull()

    const jsonText = await unzipped.file('lesson.json')!.async('text')
    const parsed = JSON.parse(jsonText)
    expect(parsed.lesson_id).toBe('sample_pack')
    expect(parsed.segments).toHaveLength(1)
  })

  it('imports an exported lesson zip and reconstructs valid Lesson & audioUrl', async () => {
    const fakeAudioBlob = new Blob(['riff wave sample bytes'], { type: 'audio/wav' })
    const zipBlob = await exportLessonZip(dummyLesson, fakeAudioBlob)

    const result = await importLessonZip(zipBlob)

    expect(result.lesson.lesson_id).toBe('sample_pack')
    expect(result.lesson.title).toBe('Sample Package Lesson')
    expect(result.lesson.segments[0].text).toBe('He packed his small brown suitcase.')
    expect(result.audioUrl).toBe('blob:mock-url')
    expect(result.audioBlob).toBeInstanceOf(Blob)
  })

  it('fails with clear error if zip does not contain lesson.json', async () => {
    const zip = new JSZip()
    zip.file('random.txt', 'hello')
    const badZipBlob = await zip.generateAsync({ type: 'blob' })

    await expect(importLessonZip(badZipBlob)).rejects.toThrow(
      'Zip paketi içinde "lesson.json" dosyası bulunamadı.'
    )
  })

  it('fails with clear error if zip does not contain audio file', async () => {
    const zip = new JSZip()
    zip.file('lesson.json', JSON.stringify(dummyLesson))
    const noAudioZipBlob = await zip.generateAsync({ type: 'blob' })

    await expect(importLessonZip(noAudioZipBlob)).rejects.toThrow(
      'ses dosyası (.wav, .mp3) bulunamadı.'
    )
  })
})
