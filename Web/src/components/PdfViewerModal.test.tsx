import { describe, it, expect, vi } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import { PdfViewerModal } from './PdfViewerModal'

describe('PdfViewerModal', () => {
  it('does not render when isOpen is false', () => {
    const { container } = render(
      <PdfViewerModal
        isOpen={false}
        onClose={vi.fn()}
        defaultPdfUrl="/lessons/book_01/book.pdf"
      />
    )
    expect(container.firstChild).toBeNull()
  })

  it('renders modal with book title and iframe when open', () => {
    render(
      <PdfViewerModal
        isOpen={true}
        onClose={vi.fn()}
        defaultPdfUrl="/lessons/book_01/book.pdf"
        bookTitle="1. The Happy Prince"
      />
    )

    expect(screen.getByRole('dialog')).toBeInTheDocument()
    expect(screen.getByText('1. The Happy Prince')).toBeInTheDocument()
    const iframe = screen.getByTitle('1. The Happy Prince')
    expect(iframe).toHaveAttribute('src', '/lessons/book_01/book.pdf')
  })

  it('calls onClose when close button is clicked', () => {
    const onClose = vi.fn()
    render(
      <PdfViewerModal
        isOpen={true}
        onClose={onClose}
        defaultPdfUrl="/lessons/book_01/book.pdf"
      />
    )

    const closeBtn = screen.getByTitle(/Kapat/i)
    fireEvent.click(closeBtn)
    expect(onClose).toHaveBeenCalledTimes(1)
  })

  it('closes on Escape key press', () => {
    const onClose = vi.fn()
    render(
      <PdfViewerModal
        isOpen={true}
        onClose={onClose}
        defaultPdfUrl="/lessons/book_01/book.pdf"
      />
    )

    fireEvent.keyDown(window, { key: 'Escape' })
    expect(onClose).toHaveBeenCalledTimes(1)
  })
})

describe('PdfViewerModal on browsers without an inline PDF viewer', () => {
  it('shows open/download links instead of a blank iframe', () => {
    Object.defineProperty(navigator, 'pdfViewerEnabled', { value: false, configurable: true })
    try {
      render(<PdfViewerModal isOpen onClose={vi.fn()} defaultPdfUrl="/lessons/book_01/book.pdf" bookTitle="Book" />)
      expect(screen.queryByTitle('Book')).toBeNull()
      expect(screen.getByRole('link', { name: /PDF'i aç/i })).toHaveAttribute('href', '/lessons/book_01/book.pdf')
      expect(screen.getByRole('link', { name: /İndir/i })).toBeInTheDocument()
    } finally {
      Object.defineProperty(navigator, 'pdfViewerEnabled', { value: undefined, configurable: true })
    }
  })

  it('accepts a .pdf with an empty MIME type and rejects other files with a message', () => {
    const onUploaded = vi.fn()
    const { container } = render(
      <PdfViewerModal isOpen onClose={vi.fn()} defaultPdfUrl="/x.pdf" onPdfUploaded={onUploaded} />
    )
    const input = container.querySelector('input[type="file"]') as HTMLInputElement

    fireEvent.change(input, { target: { files: [new File(['%PDF'], 'kitap.pdf', { type: '' })] } })
    expect(onUploaded).toHaveBeenCalledWith('kitap.pdf', expect.any(File))

    fireEvent.change(input, { target: { files: [new File(['x'], 'resim.png', { type: 'image/png' })] } })
    expect(onUploaded).toHaveBeenCalledTimes(1)
    expect(screen.getByRole('alert')).toHaveTextContent(/Sadece .pdf/i)
  })
})
