import JSZip from 'jszip'
import type { Lesson } from '../lessons/types'
import { validateLesson } from '../lessons/lesson-validator'

export interface ImportedLessonPackage {
  lesson: Lesson
  audioBlob: Blob
  audioUrl: string
}

/**
 * Packs a Lesson and its audio into a portable .zip Blob.
 */
export async function exportLessonZip(
  lesson: Lesson,
  audioBlob: Blob | File
): Promise<Blob> {
  const validation = validateLesson(lesson)
  if (!validation.isValid) {
    throw new Error(`Geçersiz ders verisi: ${validation.errors.join(', ')}`)
  }

  const zip = new JSZip()
  const lessonJsonStr = JSON.stringify(lesson, null, 2)
  zip.file('lesson.json', lessonJsonStr)

  const audioFileName = lesson.audio_file || 'audio.wav'
  zip.file(audioFileName, audioBlob)

  return await zip.generateAsync({ type: 'blob' })
}

/**
 * Triggers a browser download of the exported lesson zip.
 */
export async function downloadLessonZip(
  lesson: Lesson,
  audioBlob: Blob | File
): Promise<void> {
  const blob = await exportLessonZip(lesson, audioBlob)
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `${lesson.lesson_id || 'lesson'}.zip`
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  setTimeout(() => URL.revokeObjectURL(url), 1000)
}

/**
 * Unpacks an imported .zip file, validates lesson.json, and extracts the audio Blob and URL.
 */
export async function importLessonZip(
  zipData: Blob | File | ArrayBuffer
): Promise<ImportedLessonPackage> {
  const zip = await JSZip.loadAsync(zipData)

  // Find lesson.json (search root or subdirectories)
  let lessonFile = zip.file('lesson.json')
  if (!lessonFile) {
    const candidates = zip.file(/lesson\.json$/i)
    if (candidates.length > 0) {
      lessonFile = candidates[0]
    }
  }

  if (!lessonFile) {
    throw new Error('Zip paketi içinde "lesson.json" dosyası bulunamadı.')
  }

  const jsonText = await lessonFile.async('text')
  let parsed: unknown
  try {
    parsed = JSON.parse(jsonText)
  } catch {
    throw new Error('"lesson.json" geçerli bir JSON dosyası değil.')
  }

  const validation = validateLesson(parsed)
  if (!validation.isValid || !validation.lesson) {
    throw new Error(`Ders doğrulanamadı:\n- ${validation.errors.join('\n- ')}`)
  }

  const lesson = validation.lesson

  // Find audio file: first check lesson.audio_file, then any audio extension
  let audioZipFile = zip.file(lesson.audio_file)
  if (!audioZipFile) {
    // Check if path has subdir
    const baseName = lesson.audio_file.split('/').pop() || lesson.audio_file
    const candidates = zip.file(new RegExp(`${baseName.replace('.', '\\.')}$`, 'i'))
    if (candidates.length > 0) {
      audioZipFile = candidates[0]
    }
  }

  if (!audioZipFile) {
    // Fallback: look for any .wav, .mp3, .m4a, .ogg file
    const audioCandidates = zip.file(/\.(wav|mp3|m4a|ogg|aac)$/i)
    if (audioCandidates.length > 0) {
      audioZipFile = audioCandidates[0]
    }
  }

  if (!audioZipFile) {
    throw new Error(
      `Zip paketi içinde "${lesson.audio_file}" veya geçerli bir ses dosyası (.wav, .mp3) bulunamadı.`
    )
  }

  const audioBlob = await audioZipFile.async('blob')
  const audioUrl = URL.createObjectURL(audioBlob)

  return {
    lesson,
    audioBlob,
    audioUrl,
  }
}
