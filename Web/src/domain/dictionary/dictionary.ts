// Offline English -> Turkish dictionary lookup with light-weight lemmatization (Faz 7).

export interface DictionaryEntry {
  /** The dictionary key that matched (may be a lemma or a multi-word phrase). */
  headword: string
  meaning: string
}

export interface DictionaryFile {
  version: number
  entries: Record<string, string>
}

const IRREGULAR: Record<string, string> = {
  was: 'be', were: 'be', been: 'be', is: 'be', am: 'be', are: 'be',
  had: 'have', has: 'have', did: 'do', done: 'do', does: 'do',
  went: 'go', gone: 'go', came: 'come', saw: 'see', seen: 'see',
  took: 'take', taken: 'take', gave: 'give', given: 'give', made: 'make',
  said: 'say', told: 'tell', knew: 'know', known: 'know', thought: 'think',
  found: 'find', felt: 'feel', left: 'leave', kept: 'keep', held: 'hold',
  stood: 'stand', sat: 'sit', ran: 'run', began: 'begin', begun: 'begin',
  brought: 'bring', bought: 'buy', caught: 'catch', taught: 'teach', fought: 'fight',
  heard: 'hear', met: 'meet', lost: 'lose', sent: 'send', spent: 'spend',
  spoke: 'speak', spoken: 'speak', wrote: 'write', written: 'write', ate: 'eat', eaten: 'eat',
  fell: 'fall', fallen: 'fall', flew: 'fly', flown: 'fly', grew: 'grow', grown: 'grow',
  drew: 'draw', drawn: 'draw', threw: 'throw', thrown: 'throw', broke: 'break', broken: 'break',
  chose: 'choose', chosen: 'choose', rose: 'rise', risen: 'rise', woke: 'wake', woken: 'wake',
  wore: 'wear', worn: 'wear', drove: 'drive', driven: 'drive', rode: 'ride', ridden: 'ride',
  sang: 'sing', sung: 'sing', swam: 'swim', drank: 'drink', drunk: 'drink', became: 'become',
  slept: 'sleep', swept: 'sweep', wept: 'weep', crept: 'creep', built: 'build', meant: 'mean',
  led: 'lead', fed: 'feed', fled: 'flee', hid: 'hide', hidden: 'hide', bit: 'bite', shook: 'shake',
  struck: 'strike', stole: 'steal', stolen: 'steal', forgot: 'forget', forgotten: 'forget',
  understood: 'understand', lay: 'lie', lain: 'lie', men: 'man', women: 'woman',
  children: 'child', feet: 'foot', teeth: 'tooth', mice: 'mouse', geese: 'goose',
  better: 'good', best: 'good', worse: 'bad', worst: 'bad',
}

const BOUNDARY = /^[^\p{L}\p{N}']+|[^\p{L}\p{N}']+$/gu

export function normalizeLookupWord(word: string): string {
  return word
    .toLowerCase()
    .replace(/[’‘`]/g, "'")
    .replace(BOUNDARY, '')
    .replace(/^'+|'+$/g, '')
}

const isConsonant = (ch: string) => /[bcdfghjklmnpqrstvwxz]/.test(ch)

/** Possible dictionary forms for an inflected word, most likely first. */
export function lemmaCandidates(word: string): string[] {
  const w = normalizeLookupWord(word)
  const out: string[] = []
  const add = (c: string) => {
    if (c.length >= 2 && !out.includes(c)) out.push(c)
  }
  if (IRREGULAR[w]) add(IRREGULAR[w])
  if (w.endsWith("'s")) add(w.slice(0, -2))
  if (w.endsWith("s'")) add(w.slice(0, -1))

  const undouble = (stem: string) => {
    const n = stem.length
    if (n >= 3 && stem[n - 1] === stem[n - 2] && isConsonant(stem[n - 1])) add(stem.slice(0, -1))
  }

  if (w.endsWith('ies') && w.length > 4) add(`${w.slice(0, -3)}y`)
  if (w.endsWith('ied') && w.length > 4) add(`${w.slice(0, -3)}y`)
  if (w.endsWith('es') && w.length > 3) add(w.slice(0, -2))
  if (w.endsWith('s') && !w.endsWith('ss') && w.length > 3) add(w.slice(0, -1))
  if (w.endsWith('ed') && w.length > 3) {
    const stem = w.slice(0, -2)
    add(stem)
    add(`${stem}e`)
    undouble(stem)
  }
  if (w.endsWith('ing') && w.length > 4) {
    const stem = w.slice(0, -3)
    add(stem)
    add(`${stem}e`)
    undouble(stem)
  }
  if (w.endsWith('ly') && w.length > 4) add(w.slice(0, -2))
  if (w.endsWith('er') && w.length > 4) add(w.slice(0, -2))
  if (w.endsWith('est') && w.length > 5) add(w.slice(0, -3))
  return out
}

export class Dictionary {
  private readonly entries: Map<string, string>

  constructor(entries: Record<string, string>) {
    this.entries = new Map(Object.entries(entries))
  }

  get size(): number {
    return this.entries.size
  }

  lookup(word: string): DictionaryEntry | null {
    const w = normalizeLookupWord(word)
    if (!w) return null
    for (const key of [w, ...lemmaCandidates(w)]) {
      const meaning = this.entries.get(key)
      if (meaning) return { headword: key, meaning }
    }
    return null
  }

  /**
   * Looks the clicked word up in its sentence context: phrases of up to 4 words that
   * include the clicked word win over the single word ("drift apart" vs "apart").
   */
  lookupInSentence(words: string[], index: number): DictionaryEntry | null {
    const norm = words.map(normalizeLookupWord)
    for (let len = Math.min(4, norm.length); len >= 2; len--) {
      for (let start = Math.max(0, index - len + 1); start <= index && start + len <= norm.length; start++) {
        const phrase = norm.slice(start, start + len).join(' ')
        const meaning = this.entries.get(phrase)
        if (meaning) return { headword: phrase, meaning }
      }
    }
    return this.lookup(words[index] ?? '')
  }
}
