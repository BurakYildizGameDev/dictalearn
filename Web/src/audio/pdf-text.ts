// Extracts the text layer of a PDF with pdf.js (loaded on demand to keep the main bundle small).

export class PdfHasNoTextError extends Error {
  constructor() {
    super('Bu PDF’te seçilebilir metin yok (taranmış görüntü olabilir).')
  }
}

export async function extractPdfText(data: Blob, maxPages = 300): Promise<string> {
  const pdfjs = await import('pdfjs-dist')
  const worker = await import('pdfjs-dist/build/pdf.worker.min.mjs?url')
  pdfjs.GlobalWorkerOptions.workerSrc = worker.default

  const doc = await pdfjs.getDocument({ data: new Uint8Array(await data.arrayBuffer()) }).promise
  try {
    const pages: string[] = []
    for (let p = 1; p <= Math.min(doc.numPages, maxPages); p++) {
      const content = await (await doc.getPage(p)).getTextContent()
      // Items on one baseline are joined; a big horizontal gap (table column, e.g. English |
      // Turkish parallel text) or a new baseline starts a new line.
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
      pages.push(lines.map((l) => l.replace(/\s+/g, ' ').trim()).join('\n'))
    }
    const text = pages.join('\n')
    if (!text.replace(/\s/g, '')) throw new PdfHasNoTextError()
    return text
  } finally {
    void doc.destroy()
  }
}
