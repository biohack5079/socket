// sw.js
self.addEventListener('install', (e) => {
    console.log("Service Worker installed");
    e.waitUntil(
      caches.open('pwa-cache').then(cache => {
        return cache.addAll([
          '/index.html',
          '/manifest.json',
          '/icon.png'
        ]);
      })
    );
  });
  
  self.addEventListener('fetch', (e) => {
    e.respondWith(
      caches.match(e.request).then(response => response || fetch(e.request))
    );
  });
  