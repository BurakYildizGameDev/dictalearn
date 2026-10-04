// Offline OCR with Tesseract.js. Runtime and English model are served from public/ocr
// (copied by scripts/copy-ocr-assets.mjs), so no CDN or network is needed.
import type { Worker } from 'tesseract.js'
import { orderOcrLines, type OcrLine } from '../domain/pdf-lesson/ocr-layout'

let workerPromise: Promise<Worker> | null = null

function ocrDir(): string {
  const base = import.meta.env.BASE_URL
  return new URL(`${base.endsWith('/') ? base : `${base}/`}ocr/`, window.location.href).href
}

function getWorker(): Promise<Worker> {
  if (!workerPromise) {
    workerPromise = import('tesseract.js')
      .then(({ createWorker, OEM }) =>
        createWorker('eng', OEM.LSTM_ONLY, {
          workerPath: `${ocrDir()}worker.min.js`,
          corePath: ocrDir(),
          langPath: ocrDir(),
          gzip: true,
        })
      )
      .catch((err) => {
        workerPromise = null
        throw err
      })
  }
  return workerPromise
}

/** OCR one rendered page; two-column layouts are re-ordered column by column. */
export async function recognizeCanvas(canvas: HTMLCanvasElement): Promise<string> {
  const worker = await getWorker()
  const { data } = await worker.recognize(canvas, {}, { text: true, blocks: true })
  const lines: OcrLine[] = []
  for (const block of data.blocks ?? []) {
    for (const paragraph of block.paragraphs) {
      for (const line of paragraph.lines) {
        lines.push({ words: line.words.map((w) => ({ text: w.text, x0: w.bbox.x0, x1: w.bbox.x1 })) })
      }
    }
  }
  return lines.length ? orderOcrLines(lines, canvas.width) : data.text
}

export async function terminateOcr(): Promise<void> {
  if (!workerPromise) return
  const worker = await workerPromise.catch(() => null)
  workerPromise = null
  await worker?.terminate()
}
