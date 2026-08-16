# Appian Handbook (auto-updating)

A free, self-updating handbook of Appian release notes, pulled from Appian's
public documentation (docs.appian.com). Runs entirely on GitHub's free tier.

## What it does
- A scheduled GitHub Actions job runs weekly (free — 2,000 min/month included
  on free GitHub accounts, this job takes seconds).
- It detects the newest Appian release, converts the release notes to
  Markdown, and appends a new dated section to `handbook.md` — only if the
  content actually changed.
- It also builds `reference-index.md`: every function, smart service,
  component, record type, process model, log, and admin doc mentioned in
  that release, filed into categories as **title + link back to Appian's
  own docs page**. This is a navigation index, not a copy — it doesn't
  reproduce any reference documentation content, so it's safe to share
  publicly (see "What's legal to share" below).
- A small installable **web app** (`index.html` + friends) reads those two
  files and renders them as a searchable, phone-friendly reading experience.
  It's a real PWA — people can add it to their home screen and it works
  offline after the first load.

## What's legal to share
- ✅ `handbook.md` — paraphrased/summarized release notes with source links
- ✅ `reference-index.md` — titles + links only, no copied reference content
- ❌ Do not extend this to mirror the full text of Appian's function,
  smart service, or object reference docs — that's copyrighted reference
  material and republishing it wholesale isn't something this project
  should do. Link to it instead, like the index already does.
- ❌ Do not point this at Appian Academy — it's authenticated training
  content; this tool intentionally never logs in or touches it.

## What it deliberately does NOT do
**It does not touch Appian Academy.** Academy is authenticated training
content (courses/videos behind a login). Automating access to it would
require storing your credentials in a bot and likely breaks Appian's terms
of service. This tool only reads Appian's public docs site, which is meant
to be read by anyone, including bots (like search engines).

## Setup (10 minutes, $0)

1. **Create a free GitHub account** if you don't have one: github.com
2. **Create a new repository**, e.g. `appian-handbook`. Upload every file in
   this folder — `index.html`, `styles.css`, `app.js`, `manifest.json`,
   `sw.js`, `icons/`, `handbook.md`, `reference-index.md`, `scripts/`,
   `.github/` — all at the repo root, keeping the folder structure as-is.
3. **Enable Actions**: go to your repo → Settings → Actions → General →
   allow "Read and write permissions" for workflows (needed so the bot can
   commit updates back to the repo).
4. **Run it once manually**: go to the "Actions" tab → "Update Appian
   Handbook" → "Run workflow". Check that `handbook.md` and
   `reference-index.md` get updated.
5. **Turn on GitHub Pages**: Settings → Pages → Source: Deploy from a
   branch → `main` / root → Save. GitHub gives you a URL like
   `https://yourname.github.io/appian-handbook/`.

From then on, it updates itself every Monday, for free, forever (or until
GitHub changes its free-tier policy).

## Installing it on a phone
Once Pages is live:
- **Android (Chrome)**: open the Pages URL → tap the menu (⋮) →
  "Add to Home screen" / "Install app". A banner in the app also offers
  this automatically.
- **iPhone (Safari)**: open the Pages URL → tap the Share icon → "Add to
  Home Screen". Safari doesn't support automatic install prompts, so the
  app shows manual instructions instead.

Once installed, it opens full-screen like a native app, and cached content
is available offline — it silently re-checks for a fresh sync whenever
there's a connection.

## Sharing with the community
Once it's live, you can share the GitHub repo link or the Pages URL. Since
the content originates from Appian's own release notes, consider keeping the
"source" links intact (already included) so readers can verify against the
original and Appian gets appropriate attribution.

## Local test (optional)
```bash
pip install -r scripts/requirements.txt
python scripts/update_handbook.py
```
