// Reads every page of an uploaded PDF in order: the text layer when there is one, OCR otherwise.
// Jobs live at module level so they keep running when the user leaves the lesson, and every page
// is cached in IndexedDB so a PDF is scanned only once.
import { getPdfPages, savePdfPages, type StoredPdfPages } from '../domain/storage/pdf-storage'
import { pageNeedsOcr } from '../domain/pdf-lesson/progressive'
import { openPdf, pageTextLayer, renderPage } from '../audio/pdf-text'
import { recognizeCanvas } from './ocr-engine'

export interface PdfPagesState {
  pdfId: string
  totalPages: number
  texts: Array<string | null>
  ocr: boolean[]
  running: boolean
  error: string | null
}

type Listener = (state: PdfPagesState) => void

/** Version of the page text extraction (column-aware OCR layout = 2). */
const PAGES_VERSION = 2

/** Number of pages processed from page 1 without a gap. */
export function contiguousDone(state: PdfPagesState): number {
  let n = 0
  while (n < state.texts.length && state.texts[n] !== null) n++
  return n
}

class PdfPagesJob {
  state: PdfPagesState
  private listeners = new Set<Listener>()
  private cancelled = false
  private readonly blob: Blob

  constructor(pdfId: string, blob: Blob) {
    this.blob = blob
    this.state = { pdfId, totalPages: 0, texts: [], ocr: [], running: true, error: null }
    void this.run()
  }

  subscribe(listener: Listener): () => void {
    this.listeners.add(listener)
    listener(this.state)
    return () => this.listeners.delete(listener)
  }

  cancel(): void {
    this.cancelled = true
  }

  private emit(patch: Partial<PdfPagesState>): void {
    this.state = { ...this.state, ...patch }
    for (const l of this.listeners) l(this.state)
  }

  private async run(): Promise<void> {
    try {
      const doc = await openPdf(this.blob)
      const total = doc.numPages
      const cached = await getPdfPages(this.state.pdfId)
      const fresh: StoredPdfPages = {
        version: PAGES_VERSION,
        totalPages: total,
        texts: Array(total).fill(null),
        ocr: Array(total).fill(false),
      }
      const pages = cached && cached.totalPages === total && cached.version === PAGES_VERSION ? cached : fresh
      this.emit({ totalPages: total, texts: [...pages.texts], ocr: [...pages.ocr] })

      for (let i = 0; i < total; i++) {
        if (this.cancelled) break
        if (pages.texts[i] !== null) continue
        let text = await pageTextLayer(doc, i + 1)
        let viaOcr = false
        if (pageNeedsOcr(text)) {
          const canvas = await renderPage(doc, i + 1)
          if (this.cancelled) break
          text = await recognizeCanvas(canvas)
          canvas.width = canvas.height = 0 // free the bitmap early
          viaOcr = true
        }
        pages.texts[i] = text
        pages.ocr[i] = viaOcr
        await savePdfPages(this.state.pdfId, pages)
        this.emit({ texts: [...pages.texts], ocr: [...pages.ocr] })
      }
      void doc.destroy()
      this.emit({ running: false })
    } catch (err) {
      this.emit({ running: false, error: err instanceof Error ? err.message : 'PDF okunamadı.' })
    } finally {
      if (this.cancelled || !this.state.error) jobs.delete(this.state.pdfId)
    }
  }
}

const jobs = new Map<string, PdfPagesJob>()

/** Returns the running job for this PDF or starts one (resuming from the cache). */
export function getPdfPagesJob(pdfId: string, blob: Blob): PdfPagesJob {
  let job = jobs.get(pdfId)
  if (!job) {
    job = new PdfPagesJob(pdfId, blob)
    jobs.set(pdfId, job)
  }
  return job
}

export function cancelPdfPagesJob(pdfId: string): void {
  jobs.get(pdfId)?.cancel()
  jobs.delete(pdfId)
}
