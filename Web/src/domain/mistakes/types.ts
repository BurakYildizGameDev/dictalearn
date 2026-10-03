export type MistakeKind = 'substitute' | 'missing' | 'unknown'

export interface MistakeRecord {
  word: string
  kind: MistakeKind
  typed?: string
  lesson_id: string
  segment_id: number
  at: string
}

export interface MistakeRepository {
  getMistakes(): MistakeRecord[]
  addMistakes(mistakes: MistakeRecord[]): void
  clearMistakes(): void
  getWordFrequencies(): Record<string, number>
}
