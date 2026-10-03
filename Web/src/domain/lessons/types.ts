export interface Segment {
  id: number
  start_ms: number
  end_ms: number
  text: string
  translation?: string
  notes?: string
}

export interface Attribution {
  source: string
  license: string
}

export interface Lesson {
  schema_version: number
  lesson_id: string
  title: string
  source_lang: string
  target_lang: string
  audio_file: string
  attribution?: Attribution
  segments: Segment[]
}

export interface ValidationResult {
  isValid: boolean
  errors: string[]
  lesson?: Lesson
}
