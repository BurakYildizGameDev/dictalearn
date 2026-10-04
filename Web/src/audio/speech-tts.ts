// Browser Web Speech API helper for zero-latency English word pronunciation

export class WordSpeechEngine {
  /**
   * Pronounces a word using the device's native SpeechSynthesis engine.
   * Works 100% offline in modern mobile and desktop browsers.
   */
  static speak(word: string, rate = 0.88, pitch = 1.0) {
    if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
      return
    }

    try {
      window.speechSynthesis.cancel() // Stop previous speech immediately
      const clean = word.replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}]+$/gu, '').trim()
      if (!clean) return

      const utterance = new SpeechSynthesisUtterance(clean)
      utterance.lang = 'en-US'
      utterance.rate = rate
      utterance.pitch = pitch

      // Pick an English voice if available
      const voices = window.speechSynthesis.getVoices()
      const enVoice = voices.find(
        (v) =>
          v.lang.startsWith('en') &&
          (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('English') || v.lang === 'en-US')
      )
      if (enVoice) {
        utterance.voice = enVoice
      }

      window.speechSynthesis.speak(utterance)
    } catch {
      // Ignore synthesis errors in non-browser / strict sandbox environments
    }
  }

  static stop() {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      window.speechSynthesis.cancel()
    }
  }
}
