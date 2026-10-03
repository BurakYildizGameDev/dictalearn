import { useEffect } from 'react'

export interface ShortcutHandlers {
  onEnter?: () => void
  onCtrlEnter?: () => void
  onCtrlSpace?: () => void
  onCtrlR?: () => void
  onSpeed1?: () => void
  onSpeed2?: () => void
  onSpeed3?: () => void
}

export function useShortcuts(handlers: ShortcutHandlers, enabled = true) {
  useEffect(() => {
    if (!enabled) return

    const handleKeyDown = (e: KeyboardEvent) => {
      const isCtrl = e.ctrlKey || e.metaKey

      // Ctrl + Enter
      if (isCtrl && e.key === 'Enter') {
        e.preventDefault()
        handlers.onCtrlEnter?.()
        return
      }

      // Ctrl + Space
      if (isCtrl && (e.key === ' ' || e.code === 'Space')) {
        e.preventDefault()
        handlers.onCtrlSpace?.()
        return
      }

      // Ctrl + R
      if (isCtrl && (e.key === 'r' || e.key === 'R')) {
        e.preventDefault()
        handlers.onCtrlR?.()
        return
      }

      // Ctrl + 1 (0.75x)
      if (isCtrl && e.key === '1') {
        e.preventDefault()
        handlers.onSpeed1?.()
        return
      }

      // Ctrl + 2 (1.0x)
      if (isCtrl && e.key === '2') {
        e.preventDefault()
        handlers.onSpeed2?.()
        return
      }

      // Ctrl + 3 (1.25x)
      if (isCtrl && e.key === '3') {
        e.preventDefault()
        handlers.onSpeed3?.()
        return
      }
    }

    window.addEventListener('keydown', handleKeyDown)
    return () => {
      window.removeEventListener('keydown', handleKeyDown)
    }
  }, [handlers, enabled])
}
