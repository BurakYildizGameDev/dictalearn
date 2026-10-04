import { Dictionary, type DictionaryFile } from './dictionary'

let cached: Promise<Dictionary> | null = null

/** Loads lessons/dictionary.json once per page; later calls share the same promise. */
export function loadDictionary(baseUrl: string): Promise<Dictionary> {
  if (!cached) {
    const base = baseUrl.endsWith('/') ? baseUrl : `${baseUrl}/`
    cached = fetch(`${base}lessons/dictionary.json`)
      .then((res) => {
        if (!res.ok) throw new Error(`Dictionary load failed: ${res.status}`)
        return res.json() as Promise<DictionaryFile>
      })
      .then((file) => new Dictionary(file.entries ?? {}))
      .catch((err) => {
        cached = null // allow a retry on the next request
        throw err
      })
  }
  return cached
}

/** Test helper: forget the cached dictionary. */
export function resetDictionaryCache(): void {
  cached = null
}
