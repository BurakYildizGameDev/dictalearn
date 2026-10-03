export type DiffKind = 'equal' | 'substitute' | 'missing' | 'extra'

export interface DiffWord {
  kind: DiffKind
  expected?: string
  typed?: string
}

export interface DiffOptions {
  ignoreCase?: boolean
  ignorePunctuation?: boolean
}

export interface DiffResult {
  words: DiffWord[]
  correctCount: number
  expectedCount: number
  accuracy: number
  isPerfect: boolean
}
