const CACHE_NAME = 'Diabetese-app-v1';
const FILES_TO_CACHE = [
  '/',
  '/static/manifest.json',
  '/static/icon/icons8-diabetes-192.png',
  '/static/icon/diabetes-512.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(FILES_TO_CACHE))
      .catch(err => console.warn('Cache failed:', err))
  );
  self.skipWaiting();
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(resp => resp || fetch(event.request))
  );
});
