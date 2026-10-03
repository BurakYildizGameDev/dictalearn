import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import { StudySessionView } from './StudySessionView'
import type { Lesson } from '../domain/lessons/types'
import type { AudioEngine } from '../domain/audio/audio-engine'

describe('StudySessionView Component (F1.5 & F1.6)', () => {
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

    // The secret sentence must not be anywhere in document
    expect(screen.queryByText(/He packed his small brown suitcase/i)).toBeNull()
    expect(screen.queryByText(/Küçük kahverengi bavulunu topladı/i)).toBeNull()

    // Textarea must have spellcheck and autocomplete disabled
    const textarea = screen.getByRole('textbox') as HTMLTextAreaElement
    expect(textarea.getAttribute('spellcheck')).toBe('false')
    expect(textarea.getAttribute('autocomplete')).toBe('off')
    expect(textarea.getAttribute('autocorrect')).toBe('off')
  })

  it('reveals diff and original text only after user submits answer', () => {
    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)

    const textarea = screen.getByRole('textbox')
    fireEvent.change(textarea, { target: { value: 'he packed his small brown suitcase' } })

    const submitBtn = screen.getByRole('button', { name: /Kontrol Et/i })
    fireEvent.click(submitBtn)

    // Now in reviewing state: original text is visible
    expect(screen.getByText('He packed his small brown suitcase.')).toBeInTheDocument()
    expect(screen.getByText('Küçük kahverengi bavulunu topladı.')).toBeInTheDocument()
    expect(screen.getByText(/Kusursuz/i)).toBeInTheDocument()
  })

  it('giving up via Bilmiyorum / Göster reveals answer with 0 accuracy', () => {
    render(<StudySessionView lesson={dummyLesson} audioEngine={mockAudioEngine} />)

    const giveUpBtn = screen.getByRole('button', { name: /Bilmiyorum \/ Göster/i })
    fireEvent.click(giveUpBtn)

    // Now in reviewing state
    expect(screen.getByText('He packed his small brown suitcase.')).toBeInTheDocument()
    expect(screen.getByText(/0%/i)).toBeInTheDocument()
  })
})
