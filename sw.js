const CACHE = "appian-handbook-v1";
const SHELL = ["./", "index.html", "styles.css", "app.js", "manifest.json", "icons/icon-192.png", "icons/icon-512.png"];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(SHELL)));
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
  );
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);
  const isContent = url.pathname.endsWith("handbook.md") || url.pathname.endsWith("reference-index.md");

  if (isContent) {
    // Network-first so a fresh sync shows up immediately; fall back to cache offline.
    event.respondWith(
      fetch(event.request)
        .then((res) => {
          const clone = res.clone();
          caches.open(CACHE).then((cache) => cache.put(event.request, clone));
          return res;
        })
        .catch(() => caches.match(event.request))
    );
    return;
  }

  // Cache-first for the app shell.
  event.respondWith(
    caches.match(event.request).then((cached) => cached || fetch(event.request))
  );
});
