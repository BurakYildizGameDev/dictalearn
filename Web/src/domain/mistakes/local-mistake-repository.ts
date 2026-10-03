import type { MistakeRecord, MistakeRepository } from './types'

const STORAGE_KEY = 'dictalearn_mistakes_v1'

export class LocalMistakeRepository implements MistakeRepository {
  getMistakes(): MistakeRecord[] {
    try {
      const raw = localStorage.getItem(STORAGE_KEY)
      if (!raw) return []
      const parsed = JSON.parse(raw)
      if (Array.isArray(parsed)) {
        return parsed
      }
      return []
    } catch {
      // Safe recovery on corrupt storage
      return []
    }
  }

  addMistakes(newMistakes: MistakeRecord[]): void {
    if (newMistakes.length === 0) return
    const current = this.getMistakes()
    const updated = [...current, ...newMistakes]
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(updated))
    } catch {
      // Storage quota or privacy mode error
    }
  }

  clearMistakes(): void {
    try {
      localStorage.removeItem(STORAGE_KEY)
    } catch {
      // Ignore
    }
  }

  getWordFrequencies(): Record<string, number> {
    const mistakes = this.getMistakes()
    const freqs: Record<string, number> = {}
    for (const m of mistakes) {
      const lower = m.word.toLowerCase()
      freqs[lower] = (freqs[lower] || 0) + 1
    }
    return freqs
  }
}
