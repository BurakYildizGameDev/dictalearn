import { useState, useEffect, useMemo } from 'react'
import type { Lesson } from './domain/lessons/types'
import { loadLessonFromUrl } from './domain/lessons/lesson-loader'
import { WebAudioEngine } from './audio/web-audio-engine'
import { LocalMistakeRepository } from './domain/mistakes/local-mistake-repository'
import { StudySessionView } from './components/StudySessionView'
import { LessonEditorView } from './components/LessonEditorView'
import { Headphones, AlertTriangle, Edit3, ArrowLeft, FileText, BookOpen } from 'lucide-react'

interface PresetLesson {
  id: string
  name: string
  jsonUrl: string
  audioUrl: string
  pdfUrl?: string
}

const PRESET_LESSONS: PresetLesson[] = [
  {
    id: 'book_01_the_happy_prince',
    name: '1. The Happy Prince (15 Sayfa / 300 Cümle)',
    jsonUrl: '/lessons/book_01_the_happy_prince/lesson.json',
    audioUrl: '/lessons/book_01_the_happy_prince/audio.mp3',
    pdfUrl: '/lessons/book_01_the_happy_prince/book_01_the_happy_prince.pdf',
  },
  {
    id: 'book_02_the_selfish_giant',
    name: '2. The Selfish Giant (15 Sayfa / 300 Cümle)',
    jsonUrl: '/lessons/book_02_the_selfish_giant/lesson.json',
    audioUrl: '/lessons/book_02_the_selfish_giant/audio.mp3',
    pdfUrl: '/lessons/book_02_the_selfish_giant/book_02_the_selfish_giant.pdf',
  },
  {
    id: 'book_03_the_nightingale_and_the_rose',
    name: '3. The Nightingale and the Rose (15 Sayfa / 300 Cümle)',
    jsonUrl: '/lessons/book_03_the_nightingale_and_the_rose/lesson.json',
    audioUrl: '/lessons/book_03_the_nightingale_and_the_rose/audio.mp3',
    pdfUrl: '/lessons/book_03_the_nightingale_and_the_rose/book_03_the_nightingale_and_the_rose.pdf',
  },
  {
    id: 'book_04_the_devoted_friend',
    name: '4. The Devoted Friend (15 Sayfa / 300 Cümle)',
    jsonUrl: '/lessons/book_04_the_devoted_friend/lesson.json',
    audioUrl: '/lessons/book_04_the_devoted_friend/audio.mp3',
    pdfUrl: '/lessons/book_04_the_devoted_friend/book_04_the_devoted_friend.pdf',
  },
  {
    id: 'book_05_the_remarkable_rocket',
    name: '5. The Remarkable Rocket (15 Sayfa / 300 Cümle)',
    jsonUrl: '/lessons/book_05_the_remarkable_rocket/lesson.json',
    audioUrl: '/lessons/book_05_the_remarkable_rocket/audio.mp3',
    pdfUrl: '/lessons/book_05_the_remarkable_rocket/book_05_the_remarkable_rocket.pdf',
  },
  {
    id: 'book_06_aesops_fables_part1',
    name: "6. Aesop's Fables (Part 1) (15 Sayfa / 300 Cümle)",
    jsonUrl: '/lessons/book_06_aesops_fables_part1/lesson.json',
    audioUrl: '/lessons/book_06_aesops_fables_part1/audio.mp3',
    pdfUrl: '/lessons/book_06_aesops_fables_part1/book_06_aesops_fables_part1.pdf',
  },
  {
    id: 'book_07_aesops_fables_part2',
    name: "7. Aesop's Fables (Part 2) (15 Sayfa / 300 Cümle)",
    jsonUrl: '/lessons/book_07_aesops_fables_part2/lesson.json',
    audioUrl: '/lessons/book_07_aesops_fables_part2/audio.mp3',
    pdfUrl: '/lessons/book_07_aesops_fables_part2/book_07_aesops_fables_part2.pdf',
  },
  {
    id: 'book_08_the_little_prince',
    name: '8. The Little Prince (15 Sayfa / 300 Cümle)',
    jsonUrl: '/lessons/book_08_the_little_prince/lesson.json',
    audioUrl: '/lessons/book_08_the_little_prince/audio.mp3',
    pdfUrl: '/lessons/book_08_the_little_prince/book_08_the_little_prince.pdf',
  },
  {
    id: 'book_09_grimms_fairy_tales',
    name: "9. Grimm's Fairy Tales (15 Sayfa / 300 Cümle)",
    jsonUrl: '/lessons/book_09_grimms_fairy_tales/lesson.json',
    audioUrl: '/lessons/book_09_grimms_fairy_tales/audio.mp3',
    pdfUrl: '/lessons/book_09_grimms_fairy_tales/book_09_grimms_fairy_tales.pdf',
  },
  {
    id: 'book_10_hans_christian_andersen',
    name: "10. Hans Christian Andersen (15 Sayfa / 300 Cümle)",
    jsonUrl: '/lessons/book_10_hans_christian_andersen/lesson.json',
    audioUrl: '/lessons/book_10_hans_christian_andersen/audio.mp3',
    pdfUrl: '/lessons/book_10_hans_christian_andersen/book_10_hans_christian_andersen.pdf',
  },
  {
    id: 'book_11_alices_adventures_in_wonderland',
    name: "11. Alice in Wonderland (15 Sayfa / 300 Cümle)",
    jsonUrl: '/lessons/book_11_alices_adventures_in_wonderland/lesson.json',
    audioUrl: '/lessons/book_11_alices_adventures_in_wonderland/audio.mp3',
    pdfUrl: '/lessons/book_11_alices_adventures_in_wonderland/book_11_alices_adventures_in_wonderland.pdf',
  },
  {
    id: 'book_12_the_adventures_of_pinocchio',
    name: "12. The Adventures of Pinocchio (15 Sayfa / 300 Cümle)",
    jsonUrl: '/lessons/book_12_the_adventures_of_pinocchio/lesson.json',
    audioUrl: '/lessons/book_12_the_adventures_of_pinocchio/audio.mp3',
    pdfUrl: '/lessons/book_12_the_adventures_of_pinocchio/book_12_the_adventures_of_pinocchio.pdf',
  },
  {
    id: 'book_13_the_wonderful_wizard_of_oz',
    name: "13. The Wonderful Wizard of Oz (15 Sayfa / 300 Cümle)",
    jsonUrl: '/lessons/book_13_the_wonderful_wizard_of_oz/lesson.json',
    audioUrl: '/lessons/book_13_the_wonderful_wizard_of_oz/audio.mp3',
    pdfUrl: '/lessons/book_13_the_wonderful_wizard_of_oz/book_13_the_wonderful_wizard_of_oz.pdf',
  },
  {
    id: 'book_14_the_jungle_book',
    name: "14. The Jungle Book (15 Sayfa / 300 Cümle)",
    jsonUrl: '/lessons/book_14_the_jungle_book/lesson.json',
    audioUrl: '/lessons/book_14_the_jungle_book/audio.mp3',
    pdfUrl: '/lessons/book_14_the_jungle_book/book_14_the_jungle_book.pdf',
  },
  {
    id: 'sample_ch01',
    name: 'Demo: The Departure (6 Cümle)',
    jsonUrl: '/lessons/sample_ch01/lesson.json',
    audioUrl: '/lessons/sample_ch01/audio.mp3',
  },
]

export function App() {
  const [selectedPresetId, setSelectedPresetId] = useState<string>('book_01_the_happy_prince')
  const [lesson, setLesson] = useState<Lesson | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [viewMode, setViewMode] = useState<'study' | 'editor'>('study')

  const audioEngine = useMemo(() => new WebAudioEngine(), [])
  const mistakeRepository = useMemo(() => new LocalMistakeRepository(), [])

  const loadPreset = async (preset: PresetLesson) => {
    try {
      setLoading(true)
      setError(null)
      const loadedLesson = await loadLessonFromUrl(preset.jsonUrl)
      await audioEngine.load(preset.audioUrl)
      setLesson(loadedLesson)
      setSelectedPresetId(preset.id)
      setViewMode('study')
    } catch (err: unknown) {
      const msg = err instanceof Error ? err.message : 'Ders yüklenirken beklenmeyen bir hata oluştu.'
      setError(msg)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    let mounted = true

    async function init() {
      try {
        setLoading(true)
        setError(null)
        const preset = PRESET_LESSONS[0]
        const loadedLesson = await loadLessonFromUrl(preset.jsonUrl)
        await audioEngine.load(preset.audioUrl)

        if (mounted) {
          setLesson(loadedLesson)
        }
      } catch (err: unknown) {
        if (mounted) {
          const msg =
            err instanceof Error ? err.message : 'Ders yüklenirken beklenmeyen bir hata oluştu.'
          setError(msg)
        }
      } finally {
        if (mounted) {
          setLoading(false)
        }
      }
    }

    init()

    return () => {
      mounted = false
      audioEngine.dispose()
    }
  }, [audioEngine])

  const handleStartCustomLesson = async (customLesson: Lesson, customAudioUrl: string) => {
    try {
      setLoading(true)
      await audioEngine.load(customAudioUrl)
      setLesson(customLesson)
      setSelectedPresetId('custom')
      setViewMode('study')
    } catch (err: unknown) {
      const msg = err instanceof Error ? err.message : 'Özel ders sesi yüklenemedi.'
      setError(msg)
    } finally {
      setLoading(false)
    }
  }

  const currentPreset = PRESET_LESSONS.find((p) => p.id === selectedPresetId)

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans selection:bg-indigo-500/30 selection:text-indigo-200">
      {/* Global Navigation Header */}
      <nav className="border-b border-slate-800 bg-slate-900/50 backdrop-blur sticky top-0 z-40">
        <div className="max-w-5xl mx-auto px-4 h-16 flex items-center justify-between gap-4">
          <div className="flex items-center gap-2.5 shrink-0">
            <div className="w-9 h-9 rounded-xl bg-indigo-600/20 text-indigo-400 border border-indigo-500/30 flex items-center justify-center font-bold">
              <Headphones className="w-5 h-5" />
            </div>
            <div>
              <span className="font-bold text-lg text-slate-100 tracking-tight">DictaLearn</span>
              <span className="ml-2 text-[10px] font-semibold uppercase tracking-wider px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800">
                Faz 5 • Studio Audio
              </span>
            </div>
          </div>

          <div className="flex items-center gap-2.5">
            {/* Preset Selector */}
            <div className="flex items-center gap-1.5">
              <label className="text-xs text-slate-400 hidden md:flex items-center gap-1">
                <BookOpen className="w-3.5 h-3.5 text-indigo-400" /> Kitap:
              </label>
              <select
                aria-label="Kitap Seçimi"
                value={selectedPresetId}
                onChange={(e) => {
                  const target = PRESET_LESSONS.find((p) => p.id === e.target.value)
                  if (target) loadPreset(target)
                }}
                className="bg-slate-900 border border-slate-700 text-slate-200 text-xs rounded-lg px-2.5 py-1.5 focus:outline-none focus:border-indigo-500 cursor-pointer max-w-[200px] sm:max-w-none truncate"
              >
                {PRESET_LESSONS.map((p) => (
                  <option key={p.id} value={p.id}>
                    {p.name}
                  </option>
                ))}
                {selectedPresetId === 'custom' && (
                  <option value="custom">Özel Yüklenen Ders</option>
                )}
              </select>
            </div>

            {currentPreset?.pdfUrl && (
              <a
                href={currentPreset.pdfUrl}
                target="_blank"
                rel="noreferrer"
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/30 text-xs font-medium transition cursor-pointer"
                title="15 Sayfalık PDF Kitabı Aç"
              >
                <FileText className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">15 Sayfa PDF</span>
                <span className="sm:hidden">PDF</span>
              </a>
            )}

            {/* View Mode Switcher Button */}
            <button
              onClick={() => setViewMode(viewMode === 'study' ? 'editor' : 'study')}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-300 border border-indigo-500/30 text-xs font-medium transition cursor-pointer"
            >
              {viewMode === 'study' ? (
                <>
                  <Edit3 className="w-3.5 h-3.5" />
                  <span className="hidden sm:inline">Ders Düzenleyici</span>
                  <span className="sm:hidden">Düzenleyici</span>
                </>
              ) : (
                <>
                  <ArrowLeft className="w-3.5 h-3.5" />
                  <span>Ders Ekranına Dön</span>
                </>
              )}
            </button>
          </div>
        </div>
      </nav>

      {/* Main Content Area */}
      <main className="flex-1 flex flex-col justify-center py-8">
        {loading && (
          <div className="max-w-md mx-auto text-center space-y-4 py-16">
            <div className="w-10 h-10 border-2 border-indigo-500 border-t-transparent rounded-full animate-spin mx-auto" />
            <p className="text-slate-400 text-sm">Ders ve ses dosyası yükleniyor...</p>
          </div>
        )}

        {error && (
          <div className="max-w-md mx-auto p-6 bg-rose-950/40 border border-rose-800/60 rounded-xl text-center space-y-3">
            <AlertTriangle className="w-8 h-8 text-rose-400 mx-auto" />
            <h3 className="font-semibold text-rose-200">Ders Yüklenemedi</h3>
            <p className="text-xs text-rose-300/80">{error}</p>
            <button
              onClick={() => window.location.reload()}
              className="mt-3 px-4 py-2 bg-rose-600 hover:bg-rose-500 text-white rounded-lg text-xs font-medium transition cursor-pointer"
            >
              Yeniden Dene
            </button>
          </div>
        )}

        {!loading && !error && viewMode === 'editor' && (
          <LessonEditorView
            audioEngine={audioEngine}
            initialLesson={lesson}
            onStartLesson={handleStartCustomLesson}
            onCancel={() => setViewMode('study')}
          />
        )}

        {!loading && !error && viewMode === 'study' && lesson && (
          <StudySessionView
            key={lesson.lesson_id}
            lesson={lesson}
            audioEngine={audioEngine}
            mistakeRepository={mistakeRepository}
            onBackToLessons={() => setViewMode('editor')}
          />
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-900 py-4 text-center text-xs text-slate-600">
        DictaLearn &bull; Açık Kaynak İngilizce Dikte ve Çeviri Aracı
      </footer>
    </div>
  )
}

export default App
