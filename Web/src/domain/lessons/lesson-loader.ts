import { validateLesson } from './lesson-validator'
import type { Lesson } from './types'

export async function loadLessonFromUrl(url: string): Promise<Lesson> {
  const response = await fetch(url)
  if (!response.ok) {
    throw new Error(`Failed to fetch lesson from ${url}: ${response.statusText}`)
  }
  const json = await response.json()
  const result = validateLesson(json)
  if (!result.isValid || !result.lesson) {
    throw new Error(`Lesson validation failed: ${result.errors.join('; ')}`)
  }
  return result.lesson
}
