/* Appian Handbook PWA — fetches handbook.md + reference-index.md from the
   same origin (this repo, served by GitHub Pages), parses them into
   entries, and renders a searchable, installable reading experience. */

const HANDBOOK_URL = "handbook.md";
const INDEX_URL = "reference-index.md";
const CACHE_KEY_HANDBOOK = "appian-hb:handbook";
const CACHE_KEY_INDEX = "appian-hb:index";
const CACHE_KEY_SYNCED = "appian-hb:synced-at";

const state = { notesEntries: [], indexEntries: [], activeTab: "notes" };

/* ---------------- fetch + cache ---------------- */

async function loadText(url, cacheKey) {
  try {
    const res = await fetch(url, { cache: "no-store" });
    if (!res.ok) throw new Error(`${url}: ${res.status}`);
    const text = await res.text();
    localStorage.setItem(cacheKey, text);
    localStorage.setItem(CACHE_KEY_SYNCED, new Date().toISOString());
    document.getElementById("offline-pill").hidden = true;
    return text;
  } catch (err) {
    const cached = localStorage.getItem(cacheKey);
    if (cached) {
      document.getElementById("offline-pill").hidden = false;
      return cached;
    }
    throw err;
  }
}

/* ---------------- parsing ---------------- */

function parseHandbook(md) {
  const re = /\n## Appian ([\d.]+) — synced (\d{4}-\d{2}-\d{2})\n/g;
  const entries = [];
  let match, lastIndex = null, lastMeta = null;
  while ((match = re.exec(md)) !== null) {
    if (lastMeta) entries.push(buildNotesEntry(lastMeta, md.slice(lastIndex, match.index)));
    lastMeta = { version: match[1], date: match[2] };
    lastIndex = re.lastIndex;
  }
  if (lastMeta) entries.push(buildNotesEntry(lastMeta, md.slice(lastIndex)));
  entries.reverse(); // newest first
  return entries;
}

function buildNotesEntry(meta, chunk) {
  const sourceMatch = chunk.match(/Source:\s*(\S+)/);
  const source = sourceMatch ? sourceMatch[1] : null;
  let body = chunk.replace(/^Source:.*\n/m, "").trim();
  body = body.replace(/^---\s*/, "").trim();
  return { ...meta, source, body };
}

function parseIndex(md) {
  const re = /\n## Appian ([\d.]+) — indexed (\d{4}-\d{2}-\d{2})\n/g;
  const entries = [];
  let match, lastIndex = null, lastMeta = null;
  while ((match = re.exec(md)) !== null) {
    if (lastMeta) entries.push(buildIndexEntry(lastMeta, md.slice(lastIndex, match.index)));
    lastMeta = { version: match[1], date: match[2] };
    lastIndex = re.lastIndex;
  }
  if (lastMeta) entries.push(buildIndexEntry(lastMeta, md.slice(lastIndex)));
  entries.reverse();
  return entries;
}

function buildIndexEntry(meta, chunk) {
  const categories = [];
  const catRe = /### (.+)\n((?:- \[.*\]\(.*\)\n?)+)/g;
  let m;
  while ((m = catRe.exec(chunk)) !== null) {
    const title = m[1].trim();
    const links = [...m[2].matchAll(/- \[(.*?)\]\((.*?)\)/g)].map(l => ({ title: l[1], url: l[2] }));
    categories.push({ title, links });
  }
  return { ...meta, categories };
}

/* ---------------- rendering ---------------- */

function renderNotes() {
  const panel = document.getElementById("panel-notes");
  if (!state.notesEntries.length) {
    panel.innerHTML = `<div class="empty-state">No release entries yet. Run the sync workflow once to populate the handbook.</div>`;
    return;
  }
  panel.innerHTML = state.notesEntries.map(e => `
    <article class="entry" id="notes-${e.version}" data-search-blob="${escapeAttr(e.version + ' ' + e.body)}">
      <div class="entry-header">
        <span class="entry-version">v${e.version}</span>
        <span class="entry-date">${e.date}</span>
      </div>
      ${e.source ? `<span class="entry-source">Source: <a href="${e.source}" target="_blank" rel="noopener">${e.source}</a></span>` : ""}
      <div class="entry-body">${marked.parse(e.body)}</div>
    </article>
  `).join("");
}

function renderIndex() {
  const panel = document.getElementById("panel-index");
  if (!state.indexEntries.length) {
    panel.innerHTML = `<div class="empty-state">No reference index yet. It builds automatically alongside the release notes.</div>`;
    return;
  }
  panel.innerHTML = state.indexEntries.map(e => `
    <article class="entry" id="index-${e.version}" data-search-blob="${escapeAttr(e.version + ' ' + e.categories.map(c => c.title + ' ' + c.links.map(l => l.title).join(' ')).join(' '))}">
      <div class="entry-header">
        <span class="entry-version">v${e.version}</span>
        <span class="entry-date">${e.date}</span>
      </div>
      ${e.categories.map(c => `
        <div class="ref-category">
          <h3>${c.title}</h3>
          <ul class="ref-link-list">
            ${c.links.map(l => `<li><a href="${l.url}" target="_blank" rel="noopener">${escapeHtml(l.title)}</a></li>`).join("")}
          </ul>
        </div>
      `).join("")}
    </article>
  `).join("");
}

function renderTicker() {
  const ticker = document.getElementById("version-ticker");
  if (!state.notesEntries.length) { ticker.innerHTML = ""; return; }
  ticker.innerHTML = state.notesEntries.map((e, i) => `
    <button class="version-dot ${i === 0 ? "latest" : ""}" data-version="${e.version}">v${e.version}</button>
  `).join("");
  ticker.querySelectorAll(".version-dot").forEach(btn => {
    btn.addEventListener("click", () => {
      const id = (state.activeTab === "notes" ? "notes-" : "index-") + btn.dataset.version;
      document.getElementById(id)?.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
}

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}
function escapeAttr(s) { return escapeHtml(s).toLowerCase(); }

/* ---------------- tabs ---------------- */

document.querySelectorAll(".tab").forEach(tab => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach(t => { t.classList.remove("active"); t.setAttribute("aria-selected", "false"); });
    tab.classList.add("active"); tab.setAttribute("aria-selected", "true");
    state.activeTab = tab.dataset.tab;
    document.getElementById("panel-notes").hidden = state.activeTab !== "notes";
    document.getElementById("panel-index").hidden = state.activeTab !== "index";
    applySearch();
  });
});

/* ---------------- search ---------------- */

const searchInput = document.getElementById("search");
searchInput.addEventListener("input", applySearch);

function applySearch() {
  const q = searchInput.value.trim().toLowerCase();
  const panelId = state.activeTab === "notes" ? "panel-notes" : "panel-index";
  const entries = document.querySelectorAll(`#${panelId} .entry`);
  let anyVisible = false;
  entries.forEach(entry => {
    const blob = entry.dataset.searchBlob || "";
    const match = !q || blob.includes(q);
    entry.style.display = match ? "" : "none";
    if (match) anyVisible = true;
  });
  let empty = document.getElementById(panelId).querySelector(".no-results");
  if (!anyVisible && q) {
    if (!empty) {
      empty = document.createElement("div");
      empty.className = "empty-state no-results";
      empty.textContent = `No matches for "${searchInput.value.trim()}".`;
      document.getElementById(panelId).appendChild(empty);
    }
  } else if (empty) {
    empty.remove();
  }
}

/* ---------------- install prompt ---------------- */

let deferredPrompt = null;
window.addEventListener("beforeinstallprompt", (e) => {
  e.preventDefault();
  deferredPrompt = e;
  if (!localStorage.getItem("appian-hb:install-dismissed")) {
    document.getElementById("install-banner").hidden = false;
  }
});

document.getElementById("install-btn").addEventListener("click", async () => {
  if (deferredPrompt) {
    deferredPrompt.prompt();
    await deferredPrompt.userChoice;
    deferredPrompt = null;
  }
  document.getElementById("install-banner").hidden = true;
});

document.getElementById("install-dismiss").addEventListener("click", () => {
  document.getElementById("install-banner").hidden = true;
  localStorage.setItem("appian-hb:install-dismissed", "1");
});

// iOS Safari has no beforeinstallprompt — show manual instructions instead.
const isIOS = /iP(hone|ad|od)/.test(navigator.userAgent);
const isStandalone = window.matchMedia("(display-mode: standalone)").matches || navigator.standalone;
if (isIOS && !isStandalone && !localStorage.getItem("appian-hb:install-dismissed")) {
  document.getElementById("install-text").textContent =
    "Save this to your home screen: tap Share, then \u201cAdd to Home Screen.\u201d";
  document.getElementById("install-btn").hidden = true;
  document.getElementById("install-banner").hidden = false;
}

/* ---------------- boot ---------------- */

async function boot() {
  document.getElementById("panel-notes").innerHTML = `<div class="loading-state">Loading handbook…</div>`;
  try {
    const [handbookMd, indexMd] = await Promise.all([
      loadText(HANDBOOK_URL, CACHE_KEY_HANDBOOK),
      loadText(INDEX_URL, CACHE_KEY_INDEX),
    ]);
    state.notesEntries = parseHandbook(handbookMd);
    state.indexEntries = parseIndex(indexMd);
    renderNotes();
    renderIndex();
    renderTicker();

    const synced = localStorage.getItem(CACHE_KEY_SYNCED);
    document.getElementById("last-synced").textContent = synced
      ? `synced ${new Date(synced).toLocaleDateString()}`
      : "sync pending";
  } catch (err) {
    document.getElementById("panel-notes").innerHTML =
      `<div class="error-state">Couldn't load the handbook (${err.message}). Check your connection and reload.</div>`;
  }
}

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
}

boot();
