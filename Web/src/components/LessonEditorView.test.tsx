import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import { LessonEditorView } from './LessonEditorView'
import type { AudioEngine } from '../domain/audio/audio-engine'

describe('LessonEditorView Component (F4.3)', () => {
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

  it('renders editor with default initial fields', () => {
    render(
      <LessonEditorView
        audioEngine={mockAudioEngine}
        onStartLesson={vi.fn()}
        onCancel={vi.fn()}
      />
    )

    expect(screen.getByText(/Ders Oluşturucu & Düzenleyici/i)).toBeInTheDocument()
    expect(screen.getByDisplayValue('Yeni Ders')).toBeInTheDocument()
    expect(screen.getByDisplayValue('custom_lesson_01')).toBeInTheDocument()
    expect(screen.getByText('Cümle #1')).toBeInTheDocument()
  })

  it('allows adding and removing segments', () => {
    render(
      <LessonEditorView
        audioEngine={mockAudioEngine}
        onStartLesson={vi.fn()}
        onCancel={vi.fn()}
      />
    )

    const addBtn = screen.getByRole('button', { name: /Yeni Cümle Ekle/i })
    fireEvent.click(addBtn)

    expect(screen.getByText('Cümle #2')).toBeInTheDocument()

    const deleteBtns = screen.getAllByTitle('Cümleyi Sil')
    expect(deleteBtns).toHaveLength(2)
    fireEvent.click(deleteBtns[1])

    expect(screen.queryByText('Cümle #2')).toBeNull()
  })

  it('shows validation error if starting without an audio file', () => {
    render(
      <LessonEditorView
        audioEngine={mockAudioEngine}
        onStartLesson={vi.fn()}
        onCancel={vi.fn()}
      />
    )

    const startBtn = screen.getByRole('button', { name: /Dersi Başlat/i })
    fireEvent.click(startBtn)

    expect(screen.getByText(/bir ses dosyası seçmelisiniz/i)).toBeInTheDocument()
  })

  it('calls onCancel when cancel button is clicked', () => {
    const handleCancel = vi.fn()
    render(
      <LessonEditorView
        audioEngine={mockAudioEngine}
        onStartLesson={vi.fn()}
        onCancel={handleCancel}
      />
    )

    const cancelBtn = screen.getByRole('button', { name: /İptal/i })
    fireEvent.click(cancelBtn)

    expect(handleCancel).toHaveBeenCalled()
  })
})
