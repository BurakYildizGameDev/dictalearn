// Copies the Tesseract.js runtime (worker, WASM cores) and the English model into public/ocr so OCR
// works offline and from the GitHub Pages sub-path. Runs before `dev` and `build`.
import { copyFileSync, existsSync, mkdirSync, readdirSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = join(dirname(fileURLToPath(import.meta.url)), '..')
const out = join(root, 'public', 'ocr')
const modules = join(root, 'node_modules')
mkdirSync(out, { recursive: true })

const copies = [[join(modules, 'tesseract.js', 'dist', 'worker.min.js'), 'worker.min.js']]
const coreDir = join(modules, 'tesseract.js-core')
for (const name of readdirSync(coreDir)) {
  if (/^tesseract-core.*\.wasm(\.js)?$/.test(name)) copies.push([join(coreDir, name), name])
}
// LSTM "best_int" model: 2.9 MB, good accuracy/size balance for printed English.
copies.push([join(modules, '@tesseract.js-data', 'eng', '4.0.0_best_int', 'eng.traineddata.gz'), 'eng.traineddata.gz'])

for (const [from, name] of copies) {
  if (!existsSync(from)) throw new Error(`OCR asset missing: ${from} (run npm install)`)
  copyFileSync(from, join(out, name))
}
console.log(`copy-ocr-assets: ${copies.length} files -> public/ocr`)
