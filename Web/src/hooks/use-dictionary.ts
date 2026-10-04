import { useEffect, useState } from 'react'
import type { Dictionary } from '../domain/dictionary/dictionary'
import { loadDictionary } from '../domain/dictionary/dictionary-loader'

const BASE_URL = import.meta.env.BASE_URL

/** Shared, lazily loaded dictionary; null until ready (or if it failed to load). */
export function useDictionary(): Dictionary | null {
  const [dict, setDict] = useState<Dictionary | null>(null)
  useEffect(() => {
    let active = true
    loadDictionary(BASE_URL)
      .then((d) => active && setDict(d))
      .catch(() => {
        // Offline without a cached dictionary: the card falls back to the translate link.
      })
    return () => {
      active = false
    }
  }, [])
  return dict
}

export function googleTranslateUrl(text: string): string {
  return `https://translate.google.com/?sl=en&tl=tr&op=translate&text=${encodeURIComponent(text)}`
}
