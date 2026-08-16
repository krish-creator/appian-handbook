# Appian Handbook

Auto-updated from public Appian release notes (docs.appian.com). Not affiliated with or endorsed by Appian Corporation. Content is sourced from Appian's own public documentation; see each section's source link for the original.

---

## Appian 25.3 — synced 2026-08-14

Source: https://docs.appian.com/suite/help/25.3/Appian_Release_Notes.html

Highlights from this release, summarized:

- **Process HQ on your Site** — the Reports and Dashboards Library can now be embedded as a page inside an Appian Site, with light/dark theming and custom branding.
- **Appian Composer (preview)** — an AI-assisted planning tool that turns a plain-language description into a working app scaffold (groups, interfaces, record types, landing page).
- **Async interface loading** — the new `a!asyncVariable()` function lets slow-loading data load independently of the rest of the UI, improving perceived performance.
- **Self-managed AI** — AI Copilot and AI skills are now available for self-managed (Kubernetes) environments, not just Appian Cloud.
- **Smart search GA** — semantic search now returns more matches, supports larger datasets, and includes better error/indexing diagnostics.
- **AI skills** — Advanced IDP Tools now supports query-based extraction ("what is the patient's name?") and image file inputs (JPEG/PNG/TIFF).
- **Data fabric** — scheduled incremental syncs now extend to database-backed record types; new document monitoring/cleanup tools; expanded related-record query limits (up to 250 for `queryByIdentifier`).
- **Interfaces** — new sidebar template for forms/wizards, accessible message banner component, transparent hex color support, and a faster, more responsive design-mode experience.
- **Admin** — trusted server certificates now work automatically with OpenID Connect; the `configure.sh` script has moved to a standalone download on Forum.
- **Deprecations** — legacy RPA Queues/Scheduling are deprecated (full removal in 26.1); report objects can no longer be added directly as Site pages.

*(Once you run the automated workflow, newer releases — 25.4, 26.1, 26.3, 26.6, 26.7, etc. — will be appended below this section automatically.)*
