import { useEffect, useRef } from 'react'

export interface ShortcutHandlers {
  onCtrlEnter?: () => void
  onCtrlSpace?: () => void
  onCtrlR?: () => void
  onCtrlT?: () => void
  onSpeed1?: () => void
  onSpeed2?: () => void
  onSpeed3?: () => void
  onCtrlM?: () => void
  onPageUp?: () => void
  onPageDown?: () => void
  onF1?: () => void
  onEscape?: () => void
  /** Bare Enter while nothing interactive is focused (text fields and buttons handle their own Enter). */
  onEnter?: () => void
}

/** True when the key event targets an element that handles keyboard input itself. */
export function isInteractiveTarget(target: EventTarget | null): boolean {
  if (!(target instanceof HTMLElement)) return false
  if (target.isContentEditable) return true
  return ['INPUT', 'TEXTAREA', 'SELECT', 'BUTTON', 'A'].includes(target.tagName)
}

export function useShortcuts(handlers: ShortcutHandlers, enabled = true) {
  // Keep the latest handlers without re-binding the listener on every render.
  const handlersRef = useRef(handlers)
  useEffect(() => {
    handlersRef.current = handlers
  })

  useEffect(() => {
    if (!enabled) return

    const handleKeyDown = (e: KeyboardEvent) => {
      const h = handlersRef.current
      const isCtrl = e.ctrlKey || e.metaKey
      const key = e.key.length === 1 ? e.key.toLowerCase() : e.key

      const run = (handler?: () => void) => {
        if (!handler) return false
        e.preventDefault()
        handler()
        return true
      }

      if (isCtrl) {
        if (key === 'Enter') return void run(h.onCtrlEnter)
        if (key === ' ' || e.code === 'Space') return void run(h.onCtrlSpace)
        if (key === 'r') return void run(h.onCtrlR)
        if (key === 't') return void run(h.onCtrlT)
        if (key === 'm') return void run(h.onCtrlM)
        if (key === '1') return void run(h.onSpeed1)
        if (key === '2') return void run(h.onSpeed2)
        if (key === '3') return void run(h.onSpeed3)
        return
      }

      if (e.altKey || e.shiftKey) return

      if (key === 'F1') return void run(h.onF1)
      if (key === 'Escape') return void run(h.onEscape)
      if (key === 'PageUp') return void run(h.onPageUp)
      if (key === 'PageDown') return void run(h.onPageDown)
      if (key === 'Enter' && !isInteractiveTarget(e.target)) return void run(h.onEnter)
    }

    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [enabled])
}
