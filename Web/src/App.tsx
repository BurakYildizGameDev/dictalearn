import { useState, useEffect, useMemo } from 'react'
import type { Lesson } from './domain/lessons/types'
import { loadLessonFromUrl } from './domain/lessons/lesson-loader'
import { WebAudioEngine } from './audio/web-audio-engine'
import { LocalMistakeRepository } from './domain/mistakes/local-mistake-repository'
import { StudySessionView } from './components/StudySessionView'
import { BookOpen, Headphones, AlertTriangle } from 'lucide-react'

export function App() {
  const [lesson, setLesson] = useState<Lesson | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const audioEngine = useMemo(() => new WebAudioEngine(), [])
  const mistakeRepository = useMemo(() => new LocalMistakeRepository(), [])

  useEffect(() => {
    let mounted = true

    async function init() {
      try {
        setLoading(true)
        setError(null)
        // Load the validated sample lesson
        const loadedLesson = await loadLessonFromUrl('/lessons/sample_ch01/lesson.json')
        // Load the sample audio
        await audioEngine.load('/lessons/sample_ch01/audio.wav')

        if (mounted) {
          setLesson(loadedLesson)
        }
      } catch (err: unknown) {
        if (mounted) {
          const msg = err instanceof Error ? err.message : 'Ders yüklenirken beklenmeyen bir hata oluştu.'
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

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans selection:bg-indigo-500/30 selection:text-indigo-200">
      {/* Global Navigation Header */}
      <nav className="border-b border-slate-800 bg-slate-900/50 backdrop-blur sticky top-0 z-40">
        <div className="max-w-5xl mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded-xl bg-indigo-600/20 text-indigo-400 border border-indigo-500/30 flex items-center justify-center font-bold">
              <Headphones className="w-5 h-5" />
            </div>
            <div>
              <span className="font-bold text-lg text-slate-100 tracking-tight">DictaLearn</span>
              <span className="ml-2 text-[10px] font-semibold uppercase tracking-wider px-2 py-0.5 rounded bg-indigo-950 text-indigo-300 border border-indigo-800">
                Web MVP
              </span>
            </div>
          </div>

          <div className="flex items-center gap-4 text-xs text-slate-400">
            <span className="hidden sm:inline-flex items-center gap-1.5">
              <BookOpen className="w-3.5 h-3.5" />
              <span>İngilizce → Türkçe</span>
            </span>
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
              className="mt-3 px-4 py-2 bg-rose-600 hover:bg-rose-500 text-white rounded-lg text-xs font-medium transition"
            >
              Yeniden Dene
            </button>
          </div>
        )}

        {!loading && !error && lesson && (
          <StudySessionView
            lesson={lesson}
            audioEngine={audioEngine}
            mistakeRepository={mistakeRepository}
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
