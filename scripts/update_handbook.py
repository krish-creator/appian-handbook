#!/usr/bin/env python3
"""
Appian Handbook auto-updater.

What it does, every scheduled run:

1. RELEASE NOTES (handbook.md)
   Discovers every Appian version listed in the docs version selector, and
   keeps a rolling window of the KEEP_LAST_N most recent releases (default:
   2). handbook.md is fully regenerated each run from that window -- not
   appended to forever -- so it stays a tight "what's current" digest
   rather than growing into a full historical archive.

2. PER-RELEASE REFERENCE LINKS (reference-index.md)
   For each release in that same window, extracts every function/smart-
   service/component/record-type/process-model/log/admin link mentioned in
   that release's notes -- title + link only, filed by category. Same
   rolling window as handbook.md.

3. FULL CATALOG (catalog.md)
   Separately, rebuilt fresh every run: a complete index of every Appian
   function and every smart service, pulled from Appian's own master
   reference pages (Appian_Functions.html, Smart_Services.html). This one
   isn't windowed -- it's always the full current catalog.

   In all three files: title + link only -- no reference documentation
   content is copied, so this stays a navigation index rather than a
   mirror of Appian's docs.

Designed to run for free on a schedule via GitHub Actions (see
.github/workflows/update.yml). It only touches PUBLIC Appian documentation
pages (docs.appian.com) -- NOT Appian Academy, which requires a login and
is intentionally out of scope (scraping authenticated training content
would violate Appian's terms of service).
"""

import re
import sys
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
HANDBOOK_PATH = ROOT / "handbook.md"
INDEX_PATH = ROOT / "reference-index.md"
CATALOG_PATH = ROOT / "catalog.md"

KEEP_LAST_N = 2  # rolling window of most recent releases to keep in handbook.md / reference-index.md

CATEGORY_PATTERNS = [
    (re.compile(r"/fnc_"), "Functions"),
    (re.compile(r"_Smart_Service"), "Smart Services"),
    (re.compile(r"_Component"), "Components"),
    (re.compile(r"record-type|Record_Type|record_type"), "Record Types / Data Fabric"),
    (re.compile(r"process-model|Process_Model|Intermediate_Event|Start_Process"), "Process Models"),
    (re.compile(r"Logging|_log|logs\.html", re.IGNORECASE), "Logs"),
    (re.compile(r"admin|Admin_Console", re.IGNORECASE), "Administration"),
    (re.compile(r"_Object|_object\.html"), "Objects"),
]

# Page-chrome text that shows up inside <main> on docs.appian.com but isn't
# actual release-notes content -- share widgets, search-tips, nav labels,
# image-pan hints, etc. Filtered out verbatim (exact match after strip).
CHROME_BLOCKLIST = {
    "Share", "Share via", "LinkedIn", "Reddit", "Email", "Copy Link", "Print",
    "Ask AI", "Feedback", "Skip to main content",
    "View this page in the latest version of Appian.",
    "Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close",
    "How search works: Capitalization, punctuation, and special characters are ignored",
    "Matches in a title, heading, or function name rank higher",
    "Synonyms are applied",
    "Wildcards are not supported",
    "On This Page",
}
LONE_VERSION_RE = re.compile(r"^2\d\.\d$")

SEED_URL = "https://docs.appian.com/suite/help/25.3/Appian_Release_Notes.html"

HEADERS = {
    "User-Agent": "AppianHandbookBot/1.0 (personal, non-commercial, respectful polling; "
                  "contact: set-your-email-here)"
}


def get_soup(url: str) -> BeautifulSoup:
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def discover_all_versions() -> list:
    """The release-notes page includes a version selector listing every
    available release, newest first."""
    soup = get_soup(SEED_URL)
    text = soup.get_text("\n")
    versions = re.findall(r"\b(2\d\.\d)\b", text)
    seen = []
    for v in versions:
        if v not in seen:
            seen.append(v)
    if not seen:
        raise RuntimeError("Could not detect any version numbers on the seed page.")
    return seen  # newest first


def clean_main(main):
    """Strip structural chrome (nav/aside/header/footer) that isn't the
    actual article content, before extracting text."""
    for tag in main.find_all(["nav", "aside", "header", "footer"]):
        tag.decompose()
    return main


def html_to_markdown_and_links(main):
    main = clean_main(main)
    lines = []
    for el in main.find_all(["h1", "h2", "h3", "h4", "p", "li"]):
        text = el.get_text(" ", strip=True)
        if not text or text in CHROME_BLOCKLIST or LONE_VERSION_RE.match(text):
            continue
        if el.name == "h1":
            lines.append(f"# {text}")
        elif el.name == "h2":
            lines.append(f"## {text}")
        elif el.name == "h3":
            lines.append(f"### {text}")
        elif el.name == "h4":
            lines.append(f"#### {text}")
        elif el.name == "li":
            lines.append(f"- {text}")
        else:
            lines.append(text)
    body = "\n\n".join(lines)

    links = {}
    for a in main.find_all("a", href=True):
        href = a["href"]
        title = a.get_text(" ", strip=True)
        if not title or not href or title in CHROME_BLOCKLIST:
            continue
        full_url = href if href.startswith("http") else f"https://docs.appian.com{href}"
        if "docs.appian.com" not in full_url:
            continue
        category = categorize(full_url)
        if category:
            links[full_url] = (title, category)

    return body, links


def fetch_release_notes(version: str):
    url = f"https://docs.appian.com/suite/help/{version}/Appian_Release_Notes.html"
    soup = get_soup(url)
    main = soup.find("main") or soup.find("article") or soup.body
    body, links = html_to_markdown_and_links(main)
    return url, body, links


def categorize(url: str):
    for pattern, category in CATEGORY_PATTERNS:
        if pattern.search(url):
            return category
    return None


def build_handbook(entries: list):
    """entries: list of (version, url, body), oldest first."""
    today = date.today().isoformat()
    parts = [
        "# Appian Handbook\n",
        "Auto-updated from public Appian release notes. Shows the most "
        f"recent {KEEP_LAST_N} releases. Not affiliated with or endorsed "
        "by Appian Corporation.\n",
    ]
    for version, url, body in entries:
        parts.append(f"\n---\n\n## Appian {version} — synced {today}\n\nSource: {url}\n\n{body}\n")
    HANDBOOK_PATH.write_text("\n".join(parts), encoding="utf-8")


def build_reference_index(entries_links: list):
    """entries_links: list of (version, links_dict), oldest first."""
    today = date.today().isoformat()
    parts = [
        "# Appian Reference Index\n",
        "Links only -- titles and URLs pointing to Appian's own official "
        "documentation for functions, smart services, components, objects, "
        f"and logs mentioned in the most recent {KEEP_LAST_N} releases. No "
        "reference content is copied here; click through to docs.appian.com "
        "for the real thing.\n",
    ]
    for version, links in entries_links:
        if not links:
            continue
        by_category = {}
        for url, (title, category) in links.items():
            by_category.setdefault(category, []).append((title, url))
        parts.append(f"\n---\n\n## Appian {version} — indexed {today}\n")
        for category in sorted(by_category):
            parts.append(f"\n### {category}\n")
            for title, url in sorted(set(by_category[category])):
                parts.append(f"- [{title}]({url})")
    INDEX_PATH.write_text("\n".join(parts) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Full catalog: complete function + smart service index, rebuilt each run.
# ---------------------------------------------------------------------------

def fetch_full_function_catalog(version: str) -> dict:
    url = f"https://docs.appian.com/suite/help/{version}/Appian_Functions.html"
    try:
        soup = get_soup(url)
    except requests.RequestException:
        return {}

    main = clean_main(soup.find("main") or soup.find("article") or soup.body)
    catalog = {}
    for a in main.find_all("a", href=True):
        title = a.get_text(" ", strip=True)
        href = a["href"]
        if not title or "(" not in title:
            continue
        full_url = href if href.startswith("http") else f"https://docs.appian.com{href}"
        if "docs.appian.com" not in full_url or ("/fnc_" not in full_url and "Function" not in full_url):
            continue
        catalog.setdefault("Functions", []).append((title, full_url))
    return catalog


def fetch_full_smart_service_catalog(version: str) -> dict:
    candidates = [
        f"https://docs.appian.com/suite/help/{version}/Smart_Services.html",
        f"https://docs.appian.com/suite/help/{version}/Process_Nodes_and_Smart_Services.html",
    ]
    for url in candidates:
        try:
            soup = get_soup(url)
        except requests.RequestException:
            continue
        main = clean_main(soup.find("main") or soup.find("article") or soup.body)
        catalog = {}
        for a in main.find_all("a", href=True):
            title = a.get_text(" ", strip=True)
            href = a["href"]
            if not title:
                continue
            full_url = href if href.startswith("http") else f"https://docs.appian.com{href}"
            if "docs.appian.com" not in full_url or "_Smart_Service" not in full_url:
                continue
            catalog.setdefault("Smart Services", []).append((title, full_url))
        if catalog:
            return catalog
    return {}


def rebuild_catalog(version: str):
    catalog = {}
    catalog.update(fetch_full_function_catalog(version))
    catalog.update(fetch_full_smart_service_catalog(version))

    if not catalog:
        print("Could not build full catalog this run (source pages unavailable).")
        return

    today = date.today().isoformat()
    lines = [
        "# Appian Full Reference Catalog\n",
        f"Rebuilt {today} from Appian {version}'s own master reference pages "
        f"(Appian_Functions.html, Smart_Services.html). Titles and links only "
        f"-- click through to docs.appian.com for full documentation on each "
        f"item. Not affiliated with or endorsed by Appian Corporation.\n",
    ]
    for category in sorted(catalog):
        entries = sorted(set(catalog[category]))
        lines.append(f"\n## {category} ({len(entries)})\n")
        for title, url in entries:
            lines.append(f"- [{title}]({url})")
    CATALOG_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Catalog rebuilt: {sum(len(v) for v in catalog.values())} entries.")


def main():
    all_versions = discover_all_versions()   # newest first
    window = all_versions[:KEEP_LAST_N]
    window_oldest_first = list(reversed(window))
    print(f"Keeping latest {KEEP_LAST_N} releases: {window}")

    handbook_entries = []
    index_entries = []
    for version in window_oldest_first:
        url, body, links = fetch_release_notes(version)
        handbook_entries.append((version, url, body))
        index_entries.append((version, links))
        print(f"  fetched {version}")

    build_handbook(handbook_entries)
    build_reference_index(index_entries)
    rebuild_catalog(all_versions[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
