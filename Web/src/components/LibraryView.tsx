import React, { useMemo, useRef, useState } from 'react'
import { Search, Upload, FileText, Trash2, PenLine, Play, CheckCircle2, BookOpen, Headphones, Flame, Target } from 'lucide-react'
import {
  filterCatalog,
  LEVEL_LABELS,
  type BookLevel,
  type CatalogBook,
} from '../domain/library/catalog'
import { progressPercent, type LessonProgress } from '../domain/progress/progress-store'
import { isPdfFile } from '../domain/storage/pdf-storage'
import { Button, ProgressBar, Segmented } from './ui'
import { cx } from './cx'

export interface UploadedPdf {
  id: string
  name: string
  pdfUrl: string
}

export interface DailySnapshot {
  count: number
  goal: number
  streak: number
  week: Array<{ date: string; count: number }>
}

export interface LibraryViewProps {
  daily?: DailySnapshot
  onGoalChange?: (goal: number) => void
  books: CatalogBook[]
  progress: Record<string, LessonProgress>
  lastBookId?: string | null
  uploadedPdfs: UploadedPdf[]
  onOpenBook: (bookId: string) => void
  onOpenUploadedPdf: (pdf: UploadedPdf) => void
  onRemoveUploadedPdf: (pdf: UploadedPdf) => void
  onStudyUploadedPdf: (pdf: UploadedPdf) => void
  onUploadPdf: (file: File) => void
  onOpenEditor: () => void
}

// Hand-picked cover gradients; a book always maps to the same one.
const COVERS = [
  'from-rose-500/80 to-orange-400/70',
  'from-indigo-500/80 to-sky-400/70',
  'from-emerald-500/80 to-teal-300/70',
  'from-amber-500/80 to-yellow-300/70',
  'from-fuchsia-500/80 to-pink-400/70',
  'from-cyan-500/80 to-blue-400/70',
  'from-violet-500/80 to-purple-400/70',
  'from-lime-500/80 to-green-400/70',
]

function coverFor(id: string): string {
  let hash = 0
  for (const ch of id) hash = (hash * 31 + ch.charCodeAt(0)) | 0
  return COVERS[Math.abs(hash) % COVERS.length]
}

const BookCover: React.FC<{ book: CatalogBook; className?: string; mini?: boolean }> = ({
  book,
  className,
  mini = false,
}) => (
  <div
    aria-hidden="true"
    className={cx(
      'relative flex aspect-[3/4] flex-col justify-between overflow-hidden rounded-xl bg-gradient-to-br p-3 shadow-lg shadow-black/30',
      coverFor(book.id),
      className
    )}
  >
    <div className="absolute inset-y-0 left-0 w-2 bg-black/15" />
    <span className="self-end rounded-md bg-black/25 px-1.5 py-0.5 text-[10px] font-semibold text-white/90">
      {LEVEL_LABELS[book.level].short}
    </span>
    <div className={mini ? 'hidden' : undefined}>
      <p className="line-clamp-4 font-serif text-[15px] leading-tight text-white drop-shadow">{book.title}</p>
      <p className="mt-1 truncate text-[10px] uppercase tracking-wider text-white/70">{book.author}</p>
    </div>
  </div>
)

type LevelFilter = BookLevel | 'all'

export const LibraryView: React.FC<LibraryViewProps> = ({
  daily,
  onGoalChange,
  books,
  progress,
  lastBookId,
  uploadedPdfs,
  onOpenBook,
  onOpenUploadedPdf,
  onRemoveUploadedPdf,
  onStudyUploadedPdf,
  onUploadPdf,
  onOpenEditor,
}) => {
  const [query, setQuery] = useState('')
  const [level, setLevel] = useState<LevelFilter>('all')
  const fileInputRef = useRef<HTMLInputElement>(null)
  const [uploadError, setUploadError] = useState<string | null>(null)

  const visible = useMemo(() => filterCatalog(books, { query, level }), [books, query, level])
  const levelsPresent = useMemo(
    () => (Object.keys(LEVEL_LABELS).map(Number) as BookLevel[]).filter((l) => books.some((b) => b.level === l)),
    [books]
  )

  const lastBook = lastBookId ? books.find((b) => b.id === lastBookId) : undefined
  const lastProgress = lastBook ? progress[lastBook.id] ?? null : null
  const showContinue = lastBook && lastProgress && !lastProgress.completed

  const grouped = useMemo(() => {
    const map = new Map<BookLevel, CatalogBook[]>()
    for (const b of visible) {
      if (!map.has(b.level)) map.set(b.level, [])
      map.get(b.level)!.push(b)
    }
    // Real books first, demo/personal lessons last.
    return [...map.entries()].sort(([a], [b]) => (a === 0 ? 99 : a) - (b === 0 ? 99 : b))
  }, [visible])

  const totalSentences = books.filter((b) => b.kind === 'book').reduce((acc, b) => acc + b.sentences, 0)

  return (
    <div className="mx-auto w-full max-w-6xl px-4 pb-16 pt-8 sm:pt-12">
      {/* Hero */}
      <section className="mb-10 grid gap-6 lg:grid-cols-[1fr_minmax(0,420px)] lg:items-end">
        <div>
          <p className="text-[11px] font-semibold uppercase tracking-[0.18em] text-indigo-300/80">Kütüphane</p>
          <h1 className="mt-2 font-serif text-4xl leading-tight text-zinc-50 sm:text-5xl">
            Dinle. Yaz. Düzelt. <span className="text-zinc-500">Tekrar et.</span>
          </h1>
          <p className="mt-3 max-w-xl text-sm leading-relaxed text-zinc-400">
            {books.filter((b) => b.kind === 'book').length} kademeli klasik,{' '}
            {totalSentences.toLocaleString('tr-TR')} seslendirilmiş cümle. Her cümleyi önce kulağınla duy,
            sonra yaz ve farkları gör.
          </p>
        </div>

        <div className="flex flex-col gap-3">
        {daily && <DailyGoalCard daily={daily} onGoalChange={onGoalChange} />}
        {showContinue && lastBook && (
          <button
            type="button"
            onClick={() => onOpenBook(lastBook.id)}
            className="group flex items-center gap-4 rounded-2xl border border-white/[0.08] bg-zinc-900/70 p-3 text-left transition-colors hover:border-indigo-400/30 hover:bg-zinc-900 cursor-pointer"
          >
            <BookCover book={lastBook} mini className="w-14 shrink-0 p-2" />
            <div className="min-w-0 flex-1">
              <p className="text-[11px] font-semibold uppercase tracking-wider text-indigo-300/80">Kaldığın yerden devam et</p>
              <p className="mt-0.5 truncate font-serif text-lg text-zinc-50">{lastBook.title}</p>
              <p className="text-xs text-zinc-500">
                Cümle {lastProgress.segmentIndex + 1} / {lastProgress.totalSegments}
              </p>
              <ProgressBar value={progressPercent(lastProgress)} className="mt-2" />
            </div>
            <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-indigo-500 text-white transition-transform group-hover:scale-105">
              <Play className="ml-0.5 h-4 w-4" />
            </span>
          </button>
        )}
        </div>
      </section>

      {/* Toolbar */}
      <div className="sticky top-14 z-20 -mx-4 mb-6 flex flex-col gap-3 border-b border-white/[0.06] bg-zinc-950/85 px-4 py-3 backdrop-blur-xl sm:flex-row sm:items-center sm:justify-between">
        <Segmented<LevelFilter>
          ariaLabel="Seviye filtresi"
          value={level}
          onChange={setLevel}
          className="self-start overflow-x-auto"
          options={[
            { value: 'all', label: 'Tümü' },
            ...levelsPresent.map((l) => ({ value: l, label: LEVEL_LABELS[l].short, title: LEVEL_LABELS[l].long })),
          ]}
        />
        <div className="flex items-center gap-2">
          <label className="relative flex-1 sm:w-64">
            <span className="sr-only">Kitap ara</span>
            <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-zinc-500" />
            <input
              type="search"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Kitap, yazar ara…"
              className="h-10 w-full rounded-xl border border-white/10 bg-white/[0.03] pl-9 pr-3 text-sm text-zinc-100 placeholder:text-zinc-500 focus:border-indigo-400/50 focus:outline-none"
            />
          </label>
          <input
            ref={fileInputRef}
            type="file"
            accept=".pdf,application/pdf"
            className="hidden"
            onChange={(e) => {
              const file = e.target.files?.[0]
              e.target.value = ''
              if (!file) return
              if (isPdfFile(file)) {
                setUploadError(null)
                onUploadPdf(file)
              } else {
                setUploadError(`“${file.name}” bir PDF dosyası değil. Sadece .pdf dosyaları eklenebilir.`)
              }
            }}
          />
          <Button onClick={() => fileInputRef.current?.click()} title="Bilgisayarından bir PDF kitap ekle">
            <Upload className="h-4 w-4" />
            <span className="hidden sm:inline">PDF Ekle</span>
          </Button>
          <Button variant="ghost" onClick={onOpenEditor} title="Kendi ses ve altyazı dosyalarından ders oluştur">
            <PenLine className="h-4 w-4" />
            <span className="hidden md:inline">Ders Oluştur</span>
          </Button>
        </div>
      </div>

      {uploadError && (
        <p role="alert" className="mb-6 rounded-xl border border-rose-400/20 bg-rose-400/[0.06] px-4 py-2.5 text-sm text-rose-200">
          {uploadError}
        </p>
      )}

      {visible.length === 0 && (
        <p className="py-16 text-center text-sm text-zinc-500">“{query}” için sonuç bulunamadı.</p>
      )}

      {grouped.map(([lvl, list]) => (
        <section key={lvl} className="mb-12" aria-labelledby={`level-${lvl}`}>
          <h2 id={`level-${lvl}`} className="mb-4 flex items-baseline gap-3">
            <span className="font-serif text-xl text-zinc-100">{LEVEL_LABELS[lvl].long}</span>
            <span className="text-xs text-zinc-500">{list.length} ders</span>
          </h2>
          <ul className="grid grid-cols-2 gap-x-4 gap-y-7 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6">
            {list.map((book) => {
              const p = progress[book.id] ?? null
              const pct = progressPercent(p)
              return (
                <li key={book.id}>
                  <button
                    type="button"
                    onClick={() => onOpenBook(book.id)}
                    className="group w-full text-left cursor-pointer"
                    aria-label={`${book.title} — ${book.author}${pct > 0 ? `, %${pct} tamamlandı` : ''}`}
                  >
                    <BookCover book={book} className="transition-transform duration-200 group-hover:-translate-y-1" />
                    <div className="mt-2.5 space-y-1">
                      <p className="line-clamp-1 text-sm font-medium text-zinc-100 group-hover:text-white">{book.title}</p>
                      {book.titleTr && <p className="line-clamp-1 text-xs text-zinc-500">{book.titleTr}</p>}
                      <p className="flex items-center gap-1.5 text-[11px] text-zinc-500">
                        {p?.completed ? (
                          <span className="inline-flex items-center gap-1 text-emerald-300">
                            <CheckCircle2 className="h-3 w-3" /> Tamamlandı
                          </span>
                        ) : (
                          <span>
                            {book.kind === 'book' ? `${book.pages} sayfa · ` : ''}
                            {book.sentences} cümle
                          </span>
                        )}
                      </p>
                      {pct > 0 && !p?.completed && <ProgressBar value={pct} className="mt-1" />}
                    </div>
                  </button>
                </li>
              )
            })}
          </ul>
        </section>
      ))}

      {uploadedPdfs.length > 0 && (
        <section className="mb-12" aria-labelledby="uploaded-pdfs">
          <h2 id="uploaded-pdfs" className="mb-4 flex items-baseline gap-3">
            <span className="font-serif text-xl text-zinc-100">Yüklediğin PDF'ler</span>
            <span className="text-xs text-zinc-500">bu tarayıcıda saklanır · “Dikte” ile PDF'ten ders oluştur</span>
          </h2>
          <ul className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
            {uploadedPdfs.map((pdf) => (
              <li
                key={pdf.id}
                className="flex items-center gap-3 rounded-xl border border-white/[0.08] bg-zinc-900/60 p-3"
              >
                <FileText className="h-5 w-5 shrink-0 text-zinc-500" />
                <button
                  type="button"
                  onClick={() => onOpenUploadedPdf(pdf)}
                  className="min-w-0 flex-1 truncate text-left text-sm text-zinc-200 hover:text-white cursor-pointer"
                  title="Oku"
                >
                  {pdf.name}
                </button>
                <button
                  type="button"
                  onClick={() => onStudyUploadedPdf(pdf)}
                  className="inline-flex h-8 items-center gap-1.5 rounded-lg bg-indigo-500/15 px-2.5 text-xs font-medium text-indigo-200 hover:bg-indigo-500/25 cursor-pointer"
                  title="PDF'teki İngilizce cümlelerden dikte dersi oluştur"
                >
                  <Headphones className="h-3.5 w-3.5" />
                  Dikte
                </button>
                <button
                  type="button"
                  onClick={() => onOpenUploadedPdf(pdf)}
                  aria-label={`${pdf.name} dosyasını aç`}
                  className="rounded-lg p-1.5 text-zinc-500 hover:bg-white/5 hover:text-zinc-200 cursor-pointer"
                >
                  <BookOpen className="h-4 w-4" />
                </button>
                <button
                  type="button"
                  onClick={() => onRemoveUploadedPdf(pdf)}
                  aria-label={`${pdf.name} dosyasını sil`}
                  className="rounded-lg p-1.5 text-zinc-500 hover:bg-rose-500/10 hover:text-rose-300 cursor-pointer"
                >
                  <Trash2 className="h-4 w-4" />
                </button>
              </li>
            ))}
          </ul>
        </section>
      )}
    </div>
  )
}

const DAY_LETTERS = ['Pz', 'Pt', 'Sa', 'Ça', 'Pe', 'Cu', 'Ct']

/** Today's goal, streak and the last 7 days. */
const DailyGoalCard: React.FC<{ daily: DailySnapshot; onGoalChange?: (goal: number) => void }> = ({ daily, onGoalChange }) => {
  const done = daily.count >= daily.goal
  const max = Math.max(daily.goal, ...daily.week.map((d) => d.count))
  return (
    <section aria-label="Bugünkü hedef" className="rounded-2xl border border-white/[0.08] bg-zinc-900/70 p-4">
      <div className="flex items-start justify-between gap-3">
        <div>
          <p className="flex items-center gap-1.5 text-[11px] font-semibold uppercase tracking-wider text-zinc-500">
            <Target className="h-3.5 w-3.5" /> Bugünkü hedef
          </p>
          <p className="mt-1 text-lg text-zinc-100">
            <span className={done ? 'text-emerald-300' : ''}>{daily.count}</span>
            <span className="text-zinc-500"> / {daily.goal} cümle</span>
            {done && <span className="ml-2 text-xs text-emerald-300">tamamlandı</span>}
          </p>
        </div>
        <p
          className="flex items-center gap-1 rounded-lg bg-amber-400/10 px-2.5 py-1 text-sm font-medium text-amber-200"
          title="Hedefin tutturulduğu ardışık gün sayısı"
        >
          <Flame className="h-4 w-4" /> {daily.streak} gün
        </p>
      </div>
      <ProgressBar value={(daily.count / daily.goal) * 100} className="mt-3" label="Bugünkü hedef ilerlemesi" />
      <div className="mt-3 flex items-end justify-between gap-3">
        <div className="flex h-10 items-end gap-1.5" aria-label="Son 7 gün">
          {daily.week.map((d) => {
            const [y, m, dd] = d.date.split('-').map(Number)
            const weekday = DAY_LETTERS[new Date(y, m - 1, dd).getDay()]
            return (
              <div key={d.date} className="flex flex-col items-center gap-1" title={`${d.date}: ${d.count} cümle`}>
                <div
                  className={cx('w-3 rounded-sm', d.count >= daily.goal ? 'bg-emerald-400/80' : d.count > 0 ? 'bg-indigo-400/60' : 'bg-white/[0.06]')}
                  style={{ height: `${Math.max(3, (d.count / max) * 28)}px` }}
                />
                <span className="text-[9px] text-zinc-600">{weekday}</span>
              </div>
            )
          })}
        </div>
        {onGoalChange && (
          <Segmented<number>
            ariaLabel="Günlük hedef"
            value={daily.goal}
            onChange={onGoalChange}
            options={[10, 20, 40].map((g) => ({ value: g, label: String(g), title: `Günde ${g} cümle` }))}
          />
        )}
      </div>
    </section>
  )
}
