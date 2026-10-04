import { WebAudioEngine } from './web-audio-engine'
import { WordSpeechEngine } from './speech-tts'
import { normalizeLookupWord } from '../domain/dictionary/dictionary'

interface WordAudioIndex {
  version: number
  words: Record<string, [number, number]>
}

/**
 * Plays single words from the studio-voice sprites in lessons/word_audio/<letter>.mp3
 * (built by tools/build_word_audio.py). Sprites are fetched lazily, one letter at a time.
 */
export class WordAudioPlayer {
  private index: Promise<Record<string, [number, number]>> | null = null
  private engines = new Map<string, Promise<WebAudioEngine>>()
  private current: WebAudioEngine | null = null
  private sequenceToken = 0
  private readonly dir: string

  constructor(baseUrl: string) {
    this.dir = `${baseUrl.endsWith('/') ? baseUrl : `${baseUrl}/`}lessons/word_audio/`
  }

  private loadIndex(): Promise<Record<string, [number, number]>> {
    if (!this.index) {
      this.index = fetch(`${this.dir}index.json`)
        .then((r) => (r.ok ? (r.json() as Promise<WordAudioIndex>) : { version: 0, words: {} }))
        .then((d) => d.words ?? {})
        .catch(() => {
          this.index = null
          return {}
        })
    }
    return this.index
  }

  private engineFor(letter: string): Promise<WebAudioEngine> {
    let engine = this.engines.get(letter)
    if (!engine) {
      const e = new WebAudioEngine()
      engine = e.load(`${this.dir}${letter}.mp3`).then(() => e)
      engine.catch(() => this.engines.delete(letter))
      this.engines.set(letter, engine)
    }
    return engine
  }

  async has(word: string): Promise<boolean> {
    return Boolean((await this.loadIndex())[normalizeLookupWord(word)])
  }

  /** Plays one word and resolves when it has finished; false if the word is not in the pack. */
  async play(word: string, rate = 1): Promise<boolean> {
    const w = normalizeLookupWord(word)
    const range = (await this.loadIndex())[w]
    if (!range) return false
    try {
      const engine = await this.engineFor(w[0])
      this.current?.pause()
      this.current = engine
      engine.setSpeed(rate)
      await new Promise<void>((resolve) => {
        const offDone = engine.onRangeComplete(() => finish())
        const offStatus = engine.onStatusChange((s) => {
          if (s === 'paused' || s === 'error' || s === 'blocked') finish()
        })
        function finish() {
          offDone()
          offStatus()
          resolve()
        }
        engine.playRange(range[0], range[1]).catch(finish)
      })
      return true
    } catch {
      return false
    }
  }

  /** Reads a sentence word by word (fallback when the OS has no English voice). */
  async playSequence(words: string[], rate = 1): Promise<void> {
    const token = ++this.sequenceToken
    for (const word of words) {
      if (token !== this.sequenceToken) return
      await this.play(word, rate)
      await new Promise((r) => setTimeout(r, 40 / rate))
    }
  }

  stop(): void {
    this.sequenceToken++
    this.current?.pause()
  }
}

export const wordAudio = new WordAudioPlayer(import.meta.env.BASE_URL)

/** Pronounces a word: studio voice pack first, then an English OS voice. Never a Turkish voice. */
export async function pronounce(word: string): Promise<boolean> {
  if (await wordAudio.play(word)) return true
  return WordSpeechEngine.speak(word, 0.9)
}
