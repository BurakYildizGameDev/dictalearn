// Browser Web Speech API helper. Only ever uses an English voice: on a Turkish OS the default voice
// is often Turkish ("Microsoft Tolga"), which made English words unintelligible.

export interface VoiceLike {
  name: string
  lang: string
  localService?: boolean
}

/** Best English voice: natural/neural voices first, then US English, then any English. */
export function pickEnglishVoice<T extends VoiceLike>(voices: T[]): T | null {
  const english = voices.filter((v) => v.lang.toLowerCase().replace('_', '-').startsWith('en'))
  if (english.length === 0) return null
  const score = (v: T) => {
    const name = v.name.toLowerCase()
    let s = 0
    if (/natural|neural|online/.test(name)) s += 8
    if (/google/.test(name)) s += 6
    if (/aria|jenny|guy|christopher|samantha|daniel|karen/.test(name)) s += 3
    if (v.lang.toLowerCase().replace('_', '-') === 'en-us') s += 2
    return s
  }
  return [...english].sort((a, b) => score(b) - score(a))[0]
}

let voicesPromise: Promise<SpeechSynthesisVoice[]> | null = null

/** getVoices() is empty until the browser fires "voiceschanged"; wait for it (max 2 s). */
function loadVoices(): Promise<SpeechSynthesisVoice[]> {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) return Promise.resolve([])
  if (!voicesPromise) {
    voicesPromise = new Promise((resolve) => {
      const synth = window.speechSynthesis
      const now = synth.getVoices()
      if (now.length) return resolve(now)
      const done = () => resolve(synth.getVoices())
      synth.addEventListener?.('voiceschanged', done, { once: true })
      setTimeout(done, 2000)
    })
    void voicesPromise.then((v) => {
      if (v.length === 0) voicesPromise = null // try again next time
    })
  }
  return voicesPromise
}

const wait = (ms: number) => new Promise((r) => setTimeout(r, ms))

export class WordSpeechEngine {
  static async englishVoice(): Promise<SpeechSynthesisVoice | null> {
    return pickEnglishVoice(await loadVoices())
  }

  static async hasEnglishVoice(): Promise<boolean> {
    return (await WordSpeechEngine.englishVoice()) !== null
  }

  /**
   * Speaks English text. Resolves false (and stays silent) when no English voice exists.
   * `onEnd` fires when speech finishes or is interrupted.
   */
  static async speak(text: string, rate = 0.9, onEnd?: () => void): Promise<boolean> {
    if (typeof window === 'undefined' || !('speechSynthesis' in window)) return false
    const clean = text.replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}]+$/gu, '').trim()
    if (!clean) return false
    const voice = await WordSpeechEngine.englishVoice()
    if (!voice) return false
    try {
      window.speechSynthesis.cancel()
      await wait(60) // Chrome drops or garbles an utterance queued right after cancel()
      const utterance = new SpeechSynthesisUtterance(clean)
      utterance.voice = voice
      utterance.lang = voice.lang
      utterance.rate = rate
      if (onEnd) {
        utterance.onend = () => onEnd()
        utterance.onerror = () => onEnd()
      }
      window.speechSynthesis.speak(utterance)
      return true
    } catch {
      return false
    }
  }

  static stop() {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      window.speechSynthesis.cancel()
    }
  }
}
