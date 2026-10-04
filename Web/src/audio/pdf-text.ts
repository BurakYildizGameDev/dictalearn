// pdf.js helpers (loaded on demand to keep the main bundle small): text layer per page and page
// rendering for OCR.
import type { PDFDocumentProxy } from 'pdfjs-dist'

export async function openPdf(data: Blob): Promise<PDFDocumentProxy> {
  const pdfjs = await import('pdfjs-dist')
  const worker = await import('pdfjs-dist/build/pdf.worker.min.mjs?url')
  pdfjs.GlobalWorkerOptions.workerSrc = worker.default
  return pdfjs.getDocument({ data: new Uint8Array(await data.arrayBuffer()) }).promise
}

/**
 * Text layer of one page. Items on one baseline are joined; a big horizontal gap (table column,
 * e.g. English | Turkish parallel text) or a new baseline starts a new line.
 */
export async function pageTextLayer(doc: PDFDocumentProxy, pageNumber: number): Promise<string> {
  const content = await (await doc.getPage(pageNumber)).getTextContent()
  const lines: string[] = []
  let line = ''
  let prevY: number | null = null
  let prevEnd = 0
  for (const item of content.items) {
    if (!('str' in item) || !item.str) {
      if ('hasEOL' in item && item.hasEOL && line) {
        lines.push(line)
        line = ''
      }
      continue
    }
    const [, , , , x, y] = item.transform as number[]
    const newColumn = prevY !== null && Math.abs(y - prevY) < 2 && x - prevEnd > 12
    const newLine = prevY !== null && Math.abs(y - prevY) >= 2
    if ((newColumn || newLine) && line) {
      lines.push(line)
      line = ''
    }
    line += line && !line.endsWith(' ') && !item.str.startsWith(' ') ? ` ${item.str}` : item.str
    prevY = y
    prevEnd = x + (item.width ?? 0)
    if (item.hasEOL) {
      lines.push(line)
      line = ''
    }
  }
  if (line.trim()) lines.push(line)
  return lines.map((l) => l.replace(/\s+/g, ' ').trim()).join('\n')
}

/** Renders a page to a canvas ~targetWidth px wide (OCR works best around 300 dpi). */
export async function renderPage(doc: PDFDocumentProxy, pageNumber: number, targetWidth = 1800): Promise<HTMLCanvasElement> {
  const page = await doc.getPage(pageNumber)
  const base = page.getViewport({ scale: 1 })
  const viewport = page.getViewport({ scale: Math.min(4, targetWidth / base.width) })
  const canvas = document.createElement('canvas')
  canvas.width = Math.ceil(viewport.width)
  canvas.height = Math.ceil(viewport.height)
  const context = canvas.getContext('2d')
  if (!context) throw new Error('Canvas desteklenmiyor.')
  context.fillStyle = '#ffffff'
  context.fillRect(0, 0, canvas.width, canvas.height)
  await page.render({ canvasContext: context, viewport, canvas }).promise
  page.cleanup()
  return canvas
}
