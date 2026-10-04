// DictaLearn service worker: lets the installed web app open and study offline.
//  - App shell (navigation): network first, cached copy when offline.
//  - Hashed build assets and the OCR runtime: cache first (immutable).
//  - Lesson files (lesson.json, audio, PDFs, word audio, dictionary): cached the first time they are
//    downloaded, so every book you have opened once works without a connection.
const VERSION = 'v1'
const SHELL = `dictalearn-shell-${VERSION}`
const MEDIA = 'dictalearn-media-v1' // kept across app updates (large files)
const SCOPE = new URL(self.registration.scope).pathname

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches
      .open(SHELL)
      .then((cache) => cache.addAll(['./', './manifest.webmanifest', './icon-192.png', './favicon.svg']))
      .then(() => self.skipWaiting())
  )
})

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('dictalearn-shell-') && k !== SHELL).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  )
})

async function cacheFirst(request, cacheName) {
  const cache = await caches.open(cacheName)
  const hit = await cache.match(request)
  if (hit) return hit
  const response = await fetch(request)
  // Range responses (206, e.g. PDF viewers) cannot be cached as a whole file.
  if (response.status === 200) cache.put(request, response.clone())
  return response
}

async function networkFirstShell(request) {
  const cache = await caches.open(SHELL)
  try {
    const response = await fetch(request)
    if (response.ok) cache.put('./', response.clone())
    return response
  } catch {
    return (await cache.match('./')) || Response.error()
  }
}

self.addEventListener('fetch', (event) => {
  const { request } = event
  if (request.method !== 'GET') return
  const url = new URL(request.url)
  if (url.origin !== self.location.origin) return
  const path = url.pathname.slice(SCOPE.length - 1)

  if (request.mode === 'navigate') {
    event.respondWith(networkFirstShell(request))
  } else if (path.startsWith('/lessons/')) {
    if (request.headers.has('range')) return // let the browser stream PDFs normally
    event.respondWith(cacheFirst(request, MEDIA))
  } else if (path.startsWith('/assets/') || path.startsWith('/ocr/')) {
    event.respondWith(cacheFirst(request, SHELL))
  } else {
    event.respondWith(cacheFirst(request, SHELL))
  }
})
