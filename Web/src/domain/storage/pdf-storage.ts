/**
 * Browsers report an empty (or generic) MIME type for .pdf files when no PDF handler is
 * registered on the OS, so the extension is accepted as well.
 */
export function isPdfFile(file: { name: string; type: string }): boolean {
  if (file.type === 'application/pdf') return true
  const genericType = file.type === '' || file.type === 'application/octet-stream'
  return genericType && /\.pdf$/i.test(file.name)
}

/** Without the right MIME type a blob: URL is downloaded instead of shown in the viewer. */
export function asPdfBlob(blob: Blob): Blob {
  return blob.type === 'application/pdf' ? blob : new Blob([blob], { type: 'application/pdf' })
}

const DB_NAME = 'DictaLearnPDFDB'
const STORE_NAME = 'custom_pdfs'
const DB_VERSION = 1

function openDB(): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    if (typeof indexedDB === 'undefined') {
      return reject(new Error('IndexedDB not supported'))
    }
    const request = indexedDB.open(DB_NAME, DB_VERSION)
    request.onupgradeneeded = () => {
      const db = request.result
      if (!db.objectStoreNames.contains(STORE_NAME)) {
        db.createObjectStore(STORE_NAME)
      }
    }
    request.onsuccess = () => resolve(request.result)
    request.onerror = () => reject(request.error)
  })
}

export interface StoredPdf {
  blob: Blob
  name: string
  updatedAt: number
}

export async function saveCustomPdf(key: string, file: Blob, fileName: string): Promise<void> {
  try {
    const db = await openDB()
    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_NAME, 'readwrite')
      const store = tx.objectStore(STORE_NAME)
      store.put({ blob: file, name: fileName, updatedAt: Date.now() }, key)
      tx.oncomplete = () => resolve()
      tx.onerror = () => reject(tx.error)
    })
  } catch (err) {
    console.warn('Failed to save PDF to IndexedDB:', err)
  }
}

export async function getCustomPdf(key: string): Promise<StoredPdf | null> {
  try {
    const db = await openDB()
    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_NAME, 'readonly')
      const store = tx.objectStore(STORE_NAME)
      const request = store.get(key)
      request.onsuccess = () => resolve(request.result || null)
      request.onerror = () => reject(request.error)
    })
  } catch {
    return null
  }
}

export async function removeCustomPdf(key: string): Promise<void> {
  try {
    const db = await openDB()
    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_NAME, 'readwrite')
      const store = tx.objectStore(STORE_NAME)
      store.delete(key)
      tx.oncomplete = () => resolve()
      tx.onerror = () => reject(tx.error)
    })
  } catch (err) {
    console.warn('Failed to remove PDF from IndexedDB:', err)
  }
}

export interface StoredPdfRecord {
  id: string
  blob: Blob
  name: string
  updatedAt: number
}

export async function listAllCustomPdfs(): Promise<StoredPdfRecord[]> {
  try {
    const db = await openDB()
    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_NAME, 'readonly')
      const store = tx.objectStore(STORE_NAME)
      const request = store.openCursor()
      const results: StoredPdfRecord[] = []
      request.onsuccess = () => {
        const cursor = request.result
        if (cursor) {
          const val = cursor.value as { blob: Blob; name: string; updatedAt?: number }
          results.push({
            id: String(cursor.key),
            blob: val.blob,
            name: val.name,
            updatedAt: val.updatedAt || Date.now(),
          })
          cursor.continue()
        } else {
          resolve(results)
        }
      }
      request.onerror = () => reject(request.error)
    })
  } catch {
    return []
  }
}
