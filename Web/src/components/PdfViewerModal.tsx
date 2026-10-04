import React, { useRef, useEffect, useState } from 'react'
import { BookOpen, ExternalLink, Download, Upload, X, FileText } from 'lucide-react'
import { cx } from './cx'
import { isPdfFile } from '../domain/storage/pdf-storage'

/**
 * Android Chrome (and some older mobile browsers) have no inline PDF viewer: an iframe stays blank.
 * `navigator.pdfViewerEnabled` reports this where supported; otherwise fall back to a UA check.
 */
function canShowPdfInline(): boolean {
  if (typeof navigator === 'undefined') return true
  const reported = (navigator as Navigator & { pdfViewerEnabled?: boolean }).pdfViewerEnabled
  if (typeof reported === 'boolean') return reported
  return !/Android/i.test(navigator.userAgent)
}

export interface PdfViewerModalProps {
  isOpen: boolean
  onClose: () => void
  defaultPdfUrl?: string
  bookTitle?: string
  /** Called with a PDF the user picked; the caller decides how to persist it. */
  onPdfUploaded?: (fileName: string, file: Blob) => void
  /** `docked` renders as a side panel next to the study screen (split view). */
  variant?: 'modal' | 'docked'
}

export const PdfViewerModal: React.FC<PdfViewerModalProps> = ({
  isOpen,
  onClose,
  defaultPdfUrl,
  bookTitle = 'Kitap PDF',
  onPdfUploaded,
  variant = 'modal',
}) => {
  const fileInputRef = useRef<HTMLInputElement>(null)
  const [uploadError, setUploadError] = useState<string | null>(null)
  const inline = canShowPdfInline()

  useEffect(() => {
    if (!isOpen || variant !== 'modal') return
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose()
    }
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [isOpen, onClose, variant])

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    e.target.value = ''
    if (!file) return
    if (isPdfFile(file)) {
      setUploadError(null)
      onPdfUploaded?.(file.name, file)
    } else {
      setUploadError('Sadece .pdf dosyaları eklenebilir.')
    }
  }

  if (!isOpen) return null

  const iconBtn =
    'flex h-8 items-center gap-1.5 rounded-lg px-2.5 text-xs text-zinc-400 transition-colors hover:bg-white/5 hover:text-zinc-100 cursor-pointer'

  const panel = (
    <div
      className={cx(
        'flex h-full w-full flex-col overflow-hidden border-white/10 bg-zinc-900',
        variant === 'modal' ? 'max-w-6xl rounded-2xl border shadow-2xl' : 'border-l'
      )}
    >
      <div className="flex items-center justify-between gap-3 border-b border-white/[0.08] px-3 py-2">
        <div className="flex min-w-0 items-center gap-2">
          <BookOpen className="h-4 w-4 shrink-0 text-zinc-500" />
          <h2 className="truncate text-sm font-medium text-zinc-100">{bookTitle}</h2>
        </div>
        <div className="flex shrink-0 items-center gap-0.5">
          {onPdfUploaded && (
            <>
              <input type="file" ref={fileInputRef} accept=".pdf,application/pdf" onChange={handleFileChange} className="hidden" />
              <button type="button" onClick={() => fileInputRef.current?.click()} className={iconBtn} title="Kendi PDF'ini kütüphaneye ekle">
                <Upload className="h-3.5 w-3.5" />
                <span className="hidden sm:inline">PDF ekle</span>
              </button>
            </>
          )}
          {defaultPdfUrl && (
            <>
              <a href={defaultPdfUrl} target="_blank" rel="noreferrer" className={iconBtn} title="Yeni sekmede aç">
                <ExternalLink className="h-3.5 w-3.5" />
              </a>
              <a href={defaultPdfUrl} download className={iconBtn} title="PDF'i indir">
                <Download className="h-3.5 w-3.5" />
              </a>
            </>
          )}
          <button type="button" onClick={onClose} className={iconBtn} title={variant === 'modal' ? 'Kapat (Esc)' : 'Kapat'}>
            <X className="h-4 w-4" />
          </button>
        </div>
      </div>

      {uploadError && (
        <p role="alert" className="border-b border-rose-400/20 bg-rose-400/[0.06] px-3 py-2 text-xs text-rose-200">
          {uploadError}
        </p>
      )}

      <div className="relative flex flex-1 items-center justify-center bg-zinc-950">
        {defaultPdfUrl && inline ? (
          <iframe src={defaultPdfUrl} title={bookTitle} className="h-full w-full border-none" />
        ) : defaultPdfUrl ? (
          <div className="max-w-sm space-y-4 p-8 text-center">
            <FileText className="mx-auto h-8 w-8 text-zinc-500" />
            <p className="text-sm text-zinc-300">Bu tarayıcı PDF'i sayfa içinde gösteremiyor.</p>
            <div className="flex justify-center gap-2">
              <a
                href={defaultPdfUrl}
                target="_blank"
                rel="noreferrer"
                className="inline-flex h-10 items-center gap-2 rounded-xl bg-indigo-500 px-4 text-sm font-medium text-white hover:bg-indigo-400"
              >
                <ExternalLink className="h-4 w-4" />
                PDF'i aç
              </a>
              <a
                href={defaultPdfUrl}
                download
                className="inline-flex h-10 items-center gap-2 rounded-xl border border-white/10 bg-white/5 px-4 text-sm font-medium text-zinc-200 hover:bg-white/10"
              >
                <Download className="h-4 w-4" />
                İndir
              </a>
            </div>
          </div>
        ) : (
          <div className="max-w-sm space-y-3 p-8 text-center">
            <FileText className="mx-auto h-8 w-8 text-zinc-600" />
            <h3 className="text-sm font-medium text-zinc-200">Bu ders için PDF yok</h3>
            <p className="text-xs text-zinc-500">Kendi PDF dosyanı ekleyerek kütüphanede okuyabilirsin.</p>
          </div>
        )}
      </div>
    </div>
  )

  if (variant === 'docked') {
    return (
      <aside aria-label="PDF Görüntüleyici" className="h-full">
        {panel}
      </aside>
    )
  }

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-label="PDF Görüntüleyici"
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 p-2 backdrop-blur-sm sm:p-4"
      onClick={onClose}
    >
      <div className="flex h-[94dvh] w-full justify-center" onClick={(e) => e.stopPropagation()}>
        {panel}
      </div>
    </div>
  )
}
