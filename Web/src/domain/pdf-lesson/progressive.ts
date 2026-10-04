// Progressive PDF lessons: the first pages become a lesson right away, later pages are processed in
// the background and only ever appended, so saved progress (segment index) stays valid.

/** Pages processed before the lesson opens; the rest continue in the background. */
export const FIRST_BATCH_PAGES = 25

export function firstBatchSize(totalPages: number): number {
  return Math.max(0, Math.min(FIRST_BATCH_PAGES, totalPages))
}

/** A page whose text layer has fewer than ~40 letters is treated as a scanned image. */
export function pageNeedsOcr(textLayer: string): boolean {
  return textLayer.replace(/[^A-Za-zÀ-ÿ]/g, '').length < 40
}

/** Existing sentences keep their order and position; unseen incoming sentences are appended. */
export function mergeSentences(existing: string[], incoming: string[]): string[] {
  const seen = new Set(existing.map((s) => s.toLowerCase()))
  const merged = [...existing]
  for (const s of incoming) {
    const key = s.toLowerCase()
    if (seen.has(key)) continue
    seen.add(key)
    merged.push(s)
  }
  return merged
}
