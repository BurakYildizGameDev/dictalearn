import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import { StudySessionView } from './StudySessionView'
import type { Lesson } from '../domain/lessons/types'
import type { AudioEngine } from '../domain/audio/audio-engine'

describe('StudySessionView Component (Faz 1 & Faz 3)', () => {
  const dummyLesson: Lesson = {
    schema_version: 1,
    lesson_id: 'sample_ch01',
    title: 'Chapter 1: The Departure',
    source_lang: 'en',
    target_lang: 'tr',
    audio_file: 'audio.wav',
    segments: [
      {
        id: 1,
        start_ms: 0,
        end_ms: 4000,
        text: 'He packed his small brown suitcase.',
        translation: 'Küçük kahverengi bavulunu topladı.',
      },
    ],
  }

  let mockAudioEngine: AudioEngine

  beforeEach(() => {
    localStorage.clear()
    mockAudioEngine = {
      load: vi.fn().mockResolvedValue(undefined),
      playRange: vi.fn().mockResolvedValue(undefined),
      pause: vi.fn(),
      resume: vi.fn(),
      setSpeed: vi.fn(),
      getSpeed: vi.fn().mockReturnValue(1.0),
      getStatus: vi.fn().mockReturnValue('idle'),
      onRangeComplete: vi.fn().mockReturnValue(() => {}),
      onStatusChange: vi.fn().mockReturnValue(() => {}),
      dispose: vi.fn(),
    }
  })

  it('anti-cheat rule: original text and translation are NOT in the DOM during dictating', () => {
    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)

    // The secret sentence and translation must not be anywhere in document
    expect(screen.queryByText(/He packed his small brown suitcase/i)).toBeNull()
    expect(screen.queryByText(/Küçük kahverengi bavulunu topladı/i)).toBeNull()

    // Textarea must have spellcheck and autocomplete disabled
    const textarea = screen.getByRole('textbox') as HTMLTextAreaElement
    expect(textarea.getAttribute('spellcheck')).toBe('false')
    expect(textarea.getAttribute('autocomplete')).toBe('off')
    expect(textarea.getAttribute('autocorrect')).toBe('off')
  })

  it('reveals reviewing state with diff, original text, translation, and correction input when answer has mistakes', () => {
    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)

    const textarea = screen.getByRole('textbox')
    // Missing "small brown"
    fireEvent.change(textarea, { target: { value: 'He packed his suitcase.' } })

    const submitBtn = screen.getByRole('button', { name: /Kontrol Et/i })
    fireEvent.click(submitBtn)

    // Now in reviewing state: original text, translation, and correction field are visible
    expect(screen.getByLabelText('Orijinal cümle')).toHaveTextContent('He packed his small brown suitcase.')
    expect(screen.getByText('Küçük kahverengi bavulunu topladı.')).toBeInTheDocument()
    expect(screen.getByText(/Cümleyi düzelterek yeniden yazın/i)).toBeInTheDocument()
  })

  it('correction flow: user corrects sentence in reviewing state and advances to shadowing', () => {
    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)

    const textarea = screen.getByRole('textbox')
    fireEvent.change(textarea, { target: { value: 'He packed his suitcase.' } })
    fireEvent.click(screen.getByRole('button', { name: /Kontrol Et/i }))

    // User is in reviewing state, now corrects in correction input
    const correctionInput = screen.getByPlaceholderText(/Doğru cümleyi buraya yazın/i)
    fireEvent.change(correctionInput, { target: { value: 'He packed his small brown suitcase.' } })
    fireEvent.click(screen.getByRole('button', { name: /Düzeltmeyi Kontrol Et/i }))

    // Now successfully entered shadowing mode
    expect(screen.getByText(/Shadowing \/ Sesli Tekrar/i)).toBeInTheDocument()
    expect(screen.getByText(/Dersi Bitir/i)).toBeInTheDocument()
  })

  it('perfect answer enters shadowing mode directly and toggles translation on/off (F3.2)', () => {
    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)

    const textarea = screen.getByRole('textbox')
    fireEvent.change(textarea, { target: { value: 'he packed his small brown suitcase' } })
    fireEvent.click(screen.getByRole('button', { name: /Kontrol Et/i }))

    // Enters shadowing mode directly
    expect(screen.getByText(/Shadowing \/ Sesli Tekrar/i)).toBeInTheDocument()
    expect(screen.getByText(/Kusursuz/i)).toBeInTheDocument()
    expect(screen.getByLabelText('Orijinal cümle')).toHaveTextContent('He packed his small brown suitcase.')

    // Initially translation is hidden in shadowing
    expect(screen.queryByText('Küçük kahverengi bavulunu topladı.')).toBeNull()

    // Clicking toggle button reveals translation
    const toggleBtn = screen.getByRole('button', { name: /Çeviriyi Göster/i })
    fireEvent.click(toggleBtn)
    expect(screen.getByText('Küçük kahverengi bavulunu topladı.')).toBeInTheDocument()

    // Clicking toggle button again hides translation
    const hideBtn = screen.getByRole('button', { name: /Çeviriyi Gizle/i })
    fireEvent.click(hideBtn)
    expect(screen.queryByText('Küçük kahverengi bavulunu topladı.')).toBeNull()
  })

  it('giving up via Bilmiyorum / Göster reveals answer with 0 accuracy in reviewing state', () => {
    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)

    const giveUpBtn = screen.getByRole('button', { name: /Bilmiyorum \/ Göster/i })
    fireEvent.click(giveUpBtn)

    // Now in reviewing state
    expect(screen.getByLabelText('Orijinal cümle')).toHaveTextContent('He packed his small brown suitcase.')
    expect(screen.getByText('Küçük kahverengi bavulunu topladı.')).toBeInTheDocument()
    expect(screen.getByText(/0%/i)).toBeInTheDocument()
    expect(screen.getByText(/Cümleyi düzelterek yeniden yazın/i)).toBeInTheDocument()
  })

  it('audio speed controls update audioEngine and persist to localStorage (F3.5)', () => {
    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)

    const speed075Btn = screen.getByTitle(/Hız: 0.75x/i)
    fireEvent.click(speed075Btn)

    expect(mockAudioEngine.setSpeed).toHaveBeenCalledWith(0.75)
    expect(localStorage.getItem('dictalearn_audio_speed')).toBe('0.75')
  })

  it('switches to word-by-word mode and checks words interactively (Faz 6)', () => {
    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)

    // Switch to Kelime Modu
    const wordModeBtn = screen.getByRole('button', { name: /Kelime/i })
    fireEvent.click(wordModeBtn)

    // Check that word mode indicators are visible
    expect(screen.getByText(/Kelime İlerlemesi/i)).toBeInTheDocument()
    expect(screen.getByText('[1. Kelime]')).toBeInTheDocument()
    expect(screen.getByLabelText(/1\. kelimeyi/i)).toBeInTheDocument()

    // Anti-cheat in word mode: future words are masked
    expect(screen.queryByText('packed')).toBeNull()
    expect(screen.queryByText('suitcase')).toBeNull()

    const wordInput = screen.getByPlaceholderText(/Kelimeyi buraya yazın/i)

    // Type incorrect word
    fireEvent.change(wordInput, { target: { value: 'she' } })
    fireEvent.click(screen.getByRole('button', { name: /Kontrol Et/i }))

    // Error hint appears
    expect(screen.getByText(/Yanlış kelime/i)).toBeInTheDocument()

    // Type correct word: "he"
    fireEvent.change(wordInput, { target: { value: 'He' } })
    fireEvent.click(screen.getByRole('button', { name: /Kontrol Et/i }))

    // Word 1 is now revealed and we moved to Word 2
    expect(screen.getByText('He')).toBeInTheDocument()
    expect(screen.getByText('[2. Kelime]')).toBeInTheDocument()

    // Skip word 2: "packed"
    const skipBtn = screen.getByRole('button', { name: /Bu Kelimeyi Atla/i })
    fireEvent.click(skipBtn)

    // Word 3 is now active
    expect(screen.getByText('[3. Kelime]')).toBeInTheDocument()
  })

  it('letter hint button provides incremental letters in word mode', () => {
    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)

    // Switch to Kelime Modu
    fireEvent.click(screen.getByRole('button', { name: /Kelime/i }))

    const wordInput = screen.getByPlaceholderText(/Kelimeyi buraya yazın/i) as HTMLInputElement
    expect(wordInput.value).toBe('')

    // Click "Harf İpucu Al" -> Word 1 is "He", clean is "he"
    const hintBtn = screen.getByRole('button', { name: /Harf İpucu Al/i })
    fireEvent.click(hintBtn)
    expect(wordInput.value).toBe('h')

    // Click hint again -> gets second letter "he"
    fireEvent.click(hintBtn)
    expect(wordInput.value).toBe('he')

    // Submit word
    fireEvent.click(screen.getByRole('button', { name: /Kontrol Et/i }))
    expect(screen.getByText('[2. Kelime]')).toBeInTheDocument()
  })

  it('provides on-screen audio controls (Kelimeyi Oku, Oto-Oku toggle, Cümleyi Dinle)', () => {
    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)

    // Switch to Kelime Modu
    fireEvent.click(screen.getByRole('button', { name: /Kelime/i }))

    // Kelimeyi Oku button is present
    const speakBtns = screen.getAllByRole('button', { name: /Kelimeyi Oku/i })
    expect(speakBtns.length).toBeGreaterThanOrEqual(1)
    fireEvent.click(speakBtns[0])

    // Oto-Oku toggle button is present
    const autoReadBtn = screen.getByRole('button', { name: /Oto-Oku/i })
    expect(autoReadBtn).toBeInTheDocument()
    expect(autoReadBtn.textContent).toContain('Açık')

    fireEvent.click(autoReadBtn)
    expect(autoReadBtn.textContent).toContain('Kapalı')

    // Cümleyi Dinle button calls audioEngine.playRange
    const listenSentenceBtn = screen.getByRole('button', { name: /Cümleyi Dinle/i })
    fireEvent.click(listenSentenceBtn)
    expect(mockAudioEngine.playRange).toHaveBeenCalledWith(0, 4000)
  })

  it('word mode builds the sentence with Turkish meanings under solved words only', async () => {
    const { resetDictionaryCache } = await import('../domain/dictionary/dictionary-loader')
    resetDictionaryCache()
    vi.spyOn(globalThis, 'fetch').mockResolvedValue({
      ok: true,
      json: async () => ({ version: 1, entries: { he: 'o (erkek)', pack: 'toplamak, paketlemek', his: 'onun' } }),
    } as Response)
    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)
    fireEvent.click(screen.getByRole('button', { name: /Kelime/i }))
    const input = screen.getByPlaceholderText(/Kelimeyi buraya yazın/i)

    fireEvent.change(input, { target: { value: 'he' } })
    fireEvent.click(screen.getByRole('button', { name: /Kontrol Et/i }))
    expect(await screen.findByText('o')).toBeInTheDocument() // "o (erkek)" -> "o"
    // the next word ("packed" -> toplamak) must not be hinted
    expect(screen.queryByText('toplamak')).toBeNull()

    fireEvent.change(input, { target: { value: 'packed' } })
    fireEvent.click(screen.getByRole('button', { name: /Kontrol Et/i }))
    expect(screen.getByText('toplamak')).toBeInTheDocument()
    expect(screen.getAllByTestId('word-gloss')).toHaveLength(2)

    fireEvent.click(screen.getByRole('button', { name: /Anlamlar: Açık/i }))
    expect(screen.queryAllByTestId('word-gloss')).toHaveLength(0)
    expect(localStorage.getItem('dictalearn_word_gloss')).toBe('false')
  })

  it('offers a hard-sentence round in normal mode and labels the round in hard mode', () => {
    const onReviewHard = vi.fn()
    const { unmount } = render(
      <StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} hardCount={2} onReviewHard={onReviewHard} />
    )
    fireEvent.click(screen.getByRole('button', { name: /Zor cümleler \(2\)/ }))
    expect(onReviewHard).toHaveBeenCalled()
    unmount()

    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} mode="hard" hardCount={2} onReviewHard={onReviewHard} />)
    expect(screen.getByText(/Zor cümleler turu/)).toBeInTheDocument()
    expect(screen.queryByRole('button', { name: /Zor cümleler \(/ })).toBeNull()
  })

  describe('word info card (Faz 7)', () => {
    beforeEach(async () => {
      const { resetDictionaryCache } = await import('../domain/dictionary/dictionary-loader')
      resetDictionaryCache()
      vi.spyOn(globalThis, 'fetch').mockResolvedValue({
        ok: true,
        json: async () => ({ version: 1, entries: { pack: 'toplamak', suitcase: 'bavul' } }),
      } as Response)
    })

    it('shows the Turkish meaning of a clicked word after the answer is revealed', async () => {
      const repo = {
        getMistakes: vi.fn(() => []),
        addMistakes: vi.fn(),
        clearMistakes: vi.fn(),
        getWordFrequencies: vi.fn(() => ({})),
      }
      render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} mistakeRepository={repo} />)
      fireEvent.click(screen.getByRole('button', { name: /Bilmiyorum \/ Göster/i }))

      const sentence = screen.getByLabelText('Orijinal cümle')
      const packed = Array.from(sentence.querySelectorAll('button')).find((b) => b.textContent === 'packed')!
      fireEvent.click(packed)

      // The dictionary loads asynchronously; the open card fills in when it arrives.
      expect(await screen.findByText('toplamak')).toBeInTheDocument()
      expect(screen.getByRole('dialog', { name: /Kelime kartı: pack/i })).toBeInTheDocument()

      fireEvent.click(screen.getByRole('button', { name: /deftere ekle/i }))
      expect(repo.addMistakes).toHaveBeenCalledWith([
        expect.objectContaining({ word: 'pack', kind: 'unknown', lesson_id: 'sample_ch01', segment_id: 1 }),
      ])
      expect(screen.getByRole('button', { name: /Defterde/i })).toBeDisabled()
    })

    it('never renders clickable sentence words during dictating (copy protection)', () => {
      render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)
      expect(screen.queryByLabelText('Orijinal cümle')).toBeNull()
      expect(screen.queryByRole('button', { name: 'suitcase.' })).toBeNull()
    })
  })
})
