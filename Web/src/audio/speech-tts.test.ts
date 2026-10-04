import { describe, it, expect } from 'vitest'
import { pickEnglishVoice } from './speech-tts'

const v = (name: string, lang: string) => ({ name, lang })

describe('pickEnglishVoice', () => {
  it('never returns a non-English voice (Turkish OS default)', () => {
    expect(pickEnglishVoice([v('Microsoft Tolga - Turkish (Turkey)', 'tr-TR')])).toBeNull()
    expect(pickEnglishVoice([])).toBeNull()
  })

  it('prefers natural/online voices, then Google, then US English', () => {
    const voices = [
      v('Microsoft Tolga - Turkish (Turkey)', 'tr-TR'),
      v('Microsoft Zira - English (United States)', 'en-US'),
      v('Google UK English Female', 'en-GB'),
      v('Microsoft Aria Online (Natural) - English (United States)', 'en-US'),
    ]
    expect(pickEnglishVoice(voices)?.name).toContain('Aria Online (Natural)')
    expect(pickEnglishVoice(voices.slice(0, 3))?.name).toBe('Google UK English Female')
    expect(pickEnglishVoice(voices.slice(0, 2))?.name).toContain('Zira')
  })

  it('accepts underscore locale formats used by some Android browsers', () => {
    expect(pickEnglishVoice([v('English', 'en_US')])?.name).toBe('English')
  })
})
