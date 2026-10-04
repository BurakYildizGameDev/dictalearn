import { useState, useEffect, useMemo, useCallback, useSyncExternalStore } from 'react'
import type { Lesson } from './domain/lessons/types'
import { loadLessonFromUrl } from './domain/lessons/lesson-loader'
import { WebAudioEngine } from './audio/web-audio-engine'
import { SpeechSegmentEngine } from './audio/speech-segment-engine'
import { wordAudio } from './audio/word-audio'
import { WordSpeechEngine } from './audio/speech-tts'
import { extractPdfText } from './audio/pdf-text'
import { extractSentences, buildPdfLesson } from './domain/pdf-lesson/pdf-lesson'
import { LocalMistakeRepository } from './domain/mistakes/local-mistake-repository'
import { CATALOG, findBook, lessonAssetUrls } from './domain/library/catalog'
import { ProgressStore, type KeyValueStorage } from './domain/progress/progress-store'
import { listAllCustomPdfs, saveCustomPdf, removeCustomPdf, asPdfBlob, getCustomPdf } from './domain/storage/pdf-storage'
import { useHashRoute } from './state/route'
import { StudySessionView } from './components/StudySessionView'
import { LessonEditorView } from './components/LessonEditorView'
import { PdfViewerModal } from './components/PdfViewerModal'
import { LibraryView, type UploadedPdf } from './components/LibraryView'
import { NotebookView } from './components/NotebookView'
import { Button } from './components/ui'
import { Headphones, AlertTriangle, ArrowLeft, Library, BookMarked } from 'lucide-react'

const BASE_URL = import.meta.env.BASE_URL
const LAST_BOOK_KEY = 'dictalearn_last_book'
const CUSTOM_LESSON_ID = '__custom__'
// Personal lessons are git-ignored (not openly licensed), so only a local dev server has them.
const VISIBLE_BOOKS = CATALOG.filter((b) => b.kind !== 'personal' || import.meta.env.DEV)

function safeStorage(): KeyValueStorage | null {
  try {
    return window.localStorage
  } catch {
    return null
  }
}

function useMediaQuery(query: string): boolean {
  const subscribe = useCallback(
    (onChange: () => void) => {
      if (typeof window.matchMedia !== 'function') return () => {}
      const mql = window.matchMedia(query)
      mql.addEventListener('change', onChange)
      return () => mql.removeEventListener('change', onChange)
    },
    [query]
  )
  const getSnapshot = () => typeof window.matchMedia === 'function' && window.matchMedia(query).matches
  return useSyncExternalStore(subscribe, getSnapshot, () => false)
}

interface LoadedLesson {
  id: string
  lesson: Lesson
  startIndex: number
  /** 'speech' lessons (from uploaded PDFs) have no audio file and are spoken instead. */
  engine: 'audio' | 'speech'
  title?: string
  pdfUrl?: string
}

const pdfLessonId = (pdfId: string) => `pdf_${pdfId}`

export function App() {
  const [route, navigate] = useHashRoute()
  const audioEngine = useMemo(() => new WebAudioEngine(), [])
  const speechEngine = useMemo(() => new SpeechSegmentEngine(wordAudio), [])
  const mistakeRepository = useMemo(() => new LocalMistakeRepository(), [])
  const progressStore = useMemo(() => new ProgressStore(safeStorage()), [])

  const [progressMap, setProgressMap] = useState(() => progressStore.all())
  const [lastBookId, setLastBookId] = useState<string | null>(() => safeStorage()?.getItem(LAST_BOOK_KEY) ?? null)
  const [loaded, setLoaded] = useState<LoadedLesson | null>(null)
  const [loadError, setLoadError] = useState<{ id: string; message: string } | null>(null)
  const [customLoading, setCustomLoading] = useState(false)
  const [retryKey, setRetryKey] = useState(0)
  // The PDF panel belongs to one lesson; switching lessons closes it implicitly.
  const [pdfOpenFor, setPdfOpenFor] = useState<string | null>(null)
  const [uploadedPdfs, setUploadedPdfs] = useState<UploadedPdf[]>([])
  const [viewerPdf, setViewerPdf] = useState<UploadedPdf | null>(null)
  const isWide = useMediaQuery('(min-width: 1024px)')
  const [hasEnglishVoice, setHasEnglishVoice] = useState(true)

  useEffect(() => {
    void WordSpeechEngine.hasEnglishVoice().then(setHasEnglishVoice)
  }, [])

  useEffect(() => () => audioEngine.dispose(), [audioEngine])

  // Restore PDFs the user uploaded in earlier visits (IndexedDB).
  useEffect(() => {
    let cancelled = false
    listAllCustomPdfs()
      .then((records) => {
        if (cancelled) return
        // Newest first; older duplicates and the legacy "active_pdf" slot are cleaned up.
        const sorted = [...records].sort((a, b) => b.updatedAt - a.updatedAt)
        const seen = new Set<string>()
        const pdfs: UploadedPdf[] = []
        for (const r of sorted) {
          if (r.id === 'active_pdf' || seen.has(r.name) || !(r.blob instanceof Blob)) {
            void removeCustomPdf(r.id)
            continue
          }
          seen.add(r.name)
          pdfs.push({ id: r.id, name: r.name, pdfUrl: URL.createObjectURL(asPdfBlob(r.blob)) })
        }
        setUploadedPdfs(pdfs)
      })
      .catch(() => {
        // IndexedDB unavailable (private mode): uploads just won't persist.
      })
    return () => {
      cancelled = true
    }
  }, [])

  // Load the requested book whenever the study route points to a different one.
  const studyBookId = route.name === 'study' ? route.bookId : null
  useEffect(() => {
    if (!studyBookId) return
    const book = findBook(studyBookId)
    if (!book) {
      navigate({ name: 'library' })
      return
    }

    let cancelled = false
    const urls = lessonAssetUrls(book, BASE_URL)
    audioEngine.pause()

    Promise.all([loadLessonFromUrl(urls.jsonUrl), audioEngine.load(urls.audioUrl)])
      .then(([lesson]) => {
        if (cancelled) return
        const saved = progressStore.get(book.id)
        const startIndex = saved && !saved.completed ? saved.segmentIndex : 0
        setLoaded({ id: book.id, lesson, startIndex, engine: 'audio' })
        setLastBookId(book.id)
        safeStorage()?.setItem(LAST_BOOK_KEY, book.id)
      })
      .catch((err: unknown) => {
        if (cancelled) return
        const message = err instanceof Error ? err.message : 'Ders yüklenirken beklenmeyen bir hata oluştu.'
        setLoadError({ id: book.id, message })
      })

    return () => {
      cancelled = true
    }
  }, [studyBookId, retryKey, audioEngine, progressStore, navigate])

  // Build a dictation lesson from an uploaded PDF: text layer -> English sentences -> spoken segments.
  const pdfId = route.name === 'pdfLesson' ? route.pdfId : null
  useEffect(() => {
    if (!pdfId) return
    let cancelled = false
    const id = pdfLessonId(pdfId)
    audioEngine.pause()
    ;(async () => {
      try {
        const stored = await getCustomPdf(pdfId)
        if (!stored) throw new Error('PDF bulunamadı. Kütüphaneden yeniden ekleyebilirsin.')
        const sentences = extractSentences(await extractPdfText(stored.blob))
        if (sentences.length === 0) {
          throw new Error('Bu PDF’te dikte için İngilizce cümle bulunamadı (taranmış görüntü ya da Türkçe metin olabilir).')
        }
        if (cancelled) return
        const lesson = buildPdfLesson(id, stored.name, sentences)
        speechEngine.setSegments(lesson.segments)
        const saved = progressStore.get(id)
        setLoaded({
          id,
          lesson,
          startIndex: saved && !saved.completed ? Math.min(saved.segmentIndex, sentences.length - 1) : 0,
          engine: 'speech',
          title: lesson.title,
          pdfUrl: URL.createObjectURL(asPdfBlob(stored.blob)),
        })
      } catch (err: unknown) {
        if (cancelled) return
        setLoadError({ id, message: err instanceof Error ? err.message : 'PDF işlenemedi.' })
      }
    })()
    return () => {
      cancelled = true
    }
  }, [pdfId, retryKey, audioEngine, speechEngine, progressStore])

  // Leaving the study screens stops the audio.
  useEffect(() => {
    if (route.name === 'library' || route.name === 'editor' || route.name === 'notebook') {
      audioEngine.pause()
      speechEngine.pause()
    }
  }, [route.name, audioEngine, speechEngine])

  // A custom lesson only lives in memory; after a reload there is nothing to show.
  useEffect(() => {
    if (route.name === 'custom' && loaded?.id !== CUSTOM_LESSON_ID) navigate({ name: 'library' })
  }, [route.name, loaded, navigate])

  const targetId = studyBookId ?? (pdfId ? pdfLessonId(pdfId) : null)
  const error = targetId && loadError?.id === targetId ? loadError.message : null
  const loadingId =
    targetId && loaded?.id !== targetId && !error
      ? targetId
      : customLoading
        ? CUSTOM_LESSON_ID
        : null
  const isPdfOpen = !!loaded && pdfOpenFor === loaded.id
  const setIsPdfOpen = (open: boolean | ((prev: boolean) => boolean)) => {
    const next = typeof open === 'function' ? open(isPdfOpen) : open
    setPdfOpenFor(next && loaded ? loaded.id : null)
  }

  const activeBook = loaded && loaded.id !== CUSTOM_LESSON_ID ? findBook(loaded.id) : undefined
  const activePdfUrl = activeBook ? lessonAssetUrls(activeBook, BASE_URL).pdfUrl : loaded?.pdfUrl
  const activeTitle = activeBook?.title ?? loaded?.title

  useEffect(() => {
    const onStudy = route.name === 'study' || route.name === 'custom' || route.name === 'pdfLesson'
    document.title = onStudy && loaded ? `${activeTitle ?? loaded.lesson.title} · DictaLearn` : 'DictaLearn'
  }, [route.name, loaded, activeTitle])

  const handleProgress = useCallback(
    (lessonId: string, index: number, total: number) => {
      if (lessonId === CUSTOM_LESSON_ID) return
      progressStore.record(lessonId, index, total)
      setProgressMap(progressStore.all())
    },
    [progressStore]
  )

  const handleComplete = useCallback(
    (lessonId: string, total: number) => {
      if (lessonId === CUSTOM_LESSON_ID) return
      progressStore.markCompleted(lessonId, total)
      setProgressMap(progressStore.all())
    },
    [progressStore]
  )

  const addUploadedPdf = async (name: string, file: Blob): Promise<UploadedPdf> => {
    const id = `custom_user_${Date.now()}`
    const blob = asPdfBlob(file)
    // Re-uploading a file with the same name replaces the old copy.
    for (const old of uploadedPdfs.filter((p) => p.name === name)) {
      URL.revokeObjectURL(old.pdfUrl)
      void removeCustomPdf(old.id)
    }
    await saveCustomPdf(id, blob, name) // never throws; logs and continues if storage is unavailable
    const pdf: UploadedPdf = { id, name, pdfUrl: URL.createObjectURL(blob) }
    setUploadedPdfs((prev) => [pdf, ...prev.filter((p) => p.name !== name)])
    return pdf
  }

  const removeUploadedPdf = async (pdf: UploadedPdf) => {
    setUploadedPdfs((prev) => prev.filter((p) => p.id !== pdf.id))
    URL.revokeObjectURL(pdf.pdfUrl)
    try {
      await removeCustomPdf(pdf.id)
    } catch {
      // ignore
    }
  }

  const handleStartCustomLesson = async (customLesson: Lesson, customAudioUrl: string) => {
    try {
      setCustomLoading(true)
      await audioEngine.load(customAudioUrl)
      setLoaded({ id: CUSTOM_LESSON_ID, lesson: customLesson, startIndex: 0, engine: 'audio' })
      navigate({ name: 'custom' })
    } catch (err: unknown) {
      window.alert(err instanceof Error ? err.message : 'Özel ders sesi yüklenemedi.')
    } finally {
      setCustomLoading(false)
    }
  }

  const onStudyScreen = route.name === 'study' || route.name === 'custom' || route.name === 'pdfLesson'
  const showStudy =
    onStudyScreen &&
    !loadingId &&
    !error &&
    loaded &&
    (route.name === 'custom' ? loaded.id === CUSTOM_LESSON_ID : loaded.id === targetId)
  const pdfDocked = showStudy && isPdfOpen && isWide && !!activePdfUrl

  return (
    <div className="flex min-h-dvh flex-col bg-zinc-950 text-zinc-100">
      <nav className="sticky top-0 z-40 h-14 border-b border-white/[0.06] bg-zinc-950/80 backdrop-blur-xl">
        <div className="mx-auto flex h-full max-w-6xl items-center justify-between gap-4 px-4">
          <button
            type="button"
            onClick={() => navigate({ name: 'library' })}
            className="flex items-center gap-2.5 cursor-pointer"
            aria-label="DictaLearn ana sayfa"
          >
            <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-indigo-500/15 text-indigo-300">
              <Headphones className="h-4 w-4" />
            </span>
            <span className="font-semibold tracking-tight text-zinc-100">DictaLearn</span>
          </button>

          <div className="flex items-center gap-1">
            {route.name !== 'library' && (
              <Button size="sm" variant="ghost" onClick={() => navigate({ name: 'library' })}>
                <Library className="h-4 w-4" />
                Kütüphane
              </Button>
            )}
            {route.name !== 'notebook' && (
              <Button size="sm" variant="ghost" onClick={() => navigate({ name: 'notebook' })} title="Hata defteri ve bilmediğin kelimeler">
                <BookMarked className="h-4 w-4" />
                Defterim
              </Button>
            )}
          </div>
        </div>
      </nav>

      <div className={pdfDocked ? 'grid flex-1 grid-cols-[minmax(0,1fr)_minmax(380px,44%)]' : 'flex flex-1 flex-col'}>
        <main className="flex min-w-0 flex-1 flex-col">
          {route.name === 'library' && (
            <LibraryView
              books={VISIBLE_BOOKS}
              progress={progressMap}
              lastBookId={lastBookId}
              uploadedPdfs={uploadedPdfs}
              onOpenBook={(id) => navigate({ name: 'study', bookId: id })}
              onOpenUploadedPdf={setViewerPdf}
              onRemoveUploadedPdf={removeUploadedPdf}
              onStudyUploadedPdf={(pdf) => navigate({ name: 'pdfLesson', pdfId: pdf.id })}
              onUploadPdf={async (file) => setViewerPdf(await addUploadedPdf(file.name, file))}
              onOpenEditor={() => navigate({ name: 'editor' })}
            />
          )}

          {route.name === 'notebook' && <NotebookView mistakeRepository={mistakeRepository} />}

          {route.name === 'editor' && (
            <LessonEditorView
              audioEngine={audioEngine}
              initialLesson={loaded?.lesson ?? null}
              onStartLesson={handleStartCustomLesson}
              onCancel={() => navigate({ name: 'library' })}
            />
          )}

          {onStudyScreen && loadingId && (
            <div className="mx-auto space-y-4 py-24 text-center" role="status">
              <div className="mx-auto h-8 w-8 animate-spin rounded-full border-2 border-indigo-400 border-t-transparent" />
              <p className="text-sm text-zinc-400">
                {route.name === 'pdfLesson' ? 'PDF okunuyor ve cümlelere ayrılıyor…' : 'Ders ve ses dosyası yükleniyor…'}
              </p>
            </div>
          )}

          {onStudyScreen && error && (
            <div className="mx-auto mt-16 max-w-md space-y-3 rounded-2xl border border-rose-400/20 bg-rose-400/[0.05] p-6 text-center">
              <AlertTriangle className="mx-auto h-7 w-7 text-rose-300" />
              <h3 className="font-medium text-rose-100">Ders yüklenemedi</h3>
              <p className="break-words text-xs text-rose-200/70">{error}</p>
              <div className="flex justify-center gap-2 pt-2">
                <Button size="sm" variant="ghost" onClick={() => navigate({ name: 'library' })}>
                  <ArrowLeft className="h-4 w-4" />
                  Kütüphane
                </Button>
                {(route.name === 'study' || route.name === 'pdfLesson') && (
                  <Button
                    size="sm"
                    variant="primary"
                    onClick={() => {
                      setLoadError(null)
                      setRetryKey((k) => k + 1)
                    }}
                  >
                    Yeniden Dene
                  </Button>
                )}
              </div>
            </div>
          )}

          {showStudy && loaded?.engine === 'speech' && !hasEnglishVoice && (
            <div className="mx-auto mt-4 w-full max-w-3xl px-4">
              <p className="rounded-xl border border-amber-400/20 bg-amber-400/[0.06] px-4 py-3 text-xs leading-relaxed text-amber-100/90">
                Bu derste ses dosyası yok; cümleler stüdyo kelime paketinden kelime kelime okunuyor. Daha akıcı bir
                okuma için Windows&apos;ta <strong>Ayarlar → Saat ve dil → Konuşma → Ses ekle → English (United States)</strong>{' '}
                paketini kur ve tarayıcıyı yeniden başlat.
              </p>
            </div>
          )}

          {showStudy && loaded && (
            <StudySessionView
              key={loaded.id}
              lesson={loaded.lesson}
              title={activeTitle}
              audioEngine={loaded.engine === 'speech' ? speechEngine : audioEngine}
              mistakeRepository={mistakeRepository}
              initialSegmentIndex={loaded.startIndex}
              onProgress={(index) => handleProgress(loaded.id, index, loaded.lesson.segments.length)}
              onComplete={() => handleComplete(loaded.id, loaded.lesson.segments.length)}
              onBackToLessons={() => navigate({ name: 'library' })}
              onOpenPdf={activePdfUrl ? () => setIsPdfOpen((v) => !v) : undefined}
              isPdfOpen={isPdfOpen}
            />
          )}
        </main>

        {pdfDocked && (
          <div className="sticky top-14 h-[calc(100dvh-3.5rem)]">
            <PdfViewerModal
              variant="docked"
              isOpen
              onClose={() => setIsPdfOpen(false)}
              defaultPdfUrl={activePdfUrl}
              bookTitle={activeTitle}
            />
          </div>
        )}
      </div>

      {/* Narrow screens: the book PDF opens as a modal instead of a side panel. */}
      <PdfViewerModal
        isOpen={!!showStudy && isPdfOpen && !isWide}
        onClose={() => setIsPdfOpen(false)}
        defaultPdfUrl={activePdfUrl}
        bookTitle={activeTitle}
      />

      <PdfViewerModal
        isOpen={!!viewerPdf}
        onClose={() => setViewerPdf(null)}
        defaultPdfUrl={viewerPdf?.pdfUrl}
        bookTitle={viewerPdf?.name}
        onPdfUploaded={async (name, file) => setViewerPdf(await addUploadedPdf(name, file))}
        onCreateLesson={
          viewerPdf
            ? () => {
                navigate({ name: 'pdfLesson', pdfId: viewerPdf.id })
                setViewerPdf(null)
              }
            : undefined
        }
      />

      {route.name === 'library' && (
        <footer className="border-t border-white/[0.06] py-6 text-center text-xs text-zinc-600">
          DictaLearn · Açık kaynak İngilizce dikte ve çeviri aracı · Kütüphanedeki klasikler kamu malı eserlerden uyarlanmıştır
        </footer>
      )}
    </div>
  )
}

export default App
