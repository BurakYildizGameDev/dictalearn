import { useCallback, useEffect, useState } from 'react'

// Hash-based routes work on static hosting (GitHub Pages) without server rewrites.
export type Route =
  | { name: 'library' }
  | { name: 'study'; bookId: string }
  | { name: 'editor' }
  | { name: 'custom' } // lesson built in the editor; lives only in memory
  | { name: 'notebook' }
  | { name: 'review' } // spaced-repetition review of the notebook
  | { name: 'pdfLesson'; pdfId: string } // dictation lesson built from an uploaded PDF

export function parseHash(hash: string): Route {
  const parts = hash.replace(/^#\/?/, '').split('/')
  switch (parts[0]) {
    case 'study': {
      if (!parts[1]) return { name: 'library' }
      try {
        return { name: 'study', bookId: decodeURIComponent(parts[1]) }
      } catch {
        return { name: 'library' }
      }
    }
    case 'editor':
      return { name: 'editor' }
    case 'custom':
      return { name: 'custom' }
    case 'notebook':
      return { name: 'notebook' }
    case 'review':
      return { name: 'review' }
    case 'pdf-lesson': {
      if (!parts[1]) return { name: 'library' }
      try {
        return { name: 'pdfLesson', pdfId: decodeURIComponent(parts[1]) }
      } catch {
        return { name: 'library' }
      }
    }
    default:
      return { name: 'library' }
  }
}

export function routeToHash(route: Route): string {
  switch (route.name) {
    case 'study':
      return `#/study/${encodeURIComponent(route.bookId)}`
    case 'editor':
      return '#/editor'
    case 'custom':
      return '#/custom'
    case 'notebook':
      return '#/notebook'
    case 'review':
      return '#/review'
    case 'pdfLesson':
      return `#/pdf-lesson/${encodeURIComponent(route.pdfId)}`
    default:
      return '#/'
  }
}

export function useHashRoute(): [Route, (route: Route) => void] {
  const [route, setRoute] = useState<Route>(() => parseHash(window.location.hash))

  useEffect(() => {
    const onChange = () => setRoute(parseHash(window.location.hash))
    window.addEventListener('hashchange', onChange)
    return () => window.removeEventListener('hashchange', onChange)
  }, [])

  const navigate = useCallback((next: Route) => {
    const hash = routeToHash(next)
    if (window.location.hash !== hash) {
      window.location.hash = hash
    }
    setRoute(next)
  }, [])

  return [route, navigate]
}
