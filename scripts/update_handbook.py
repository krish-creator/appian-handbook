#!/usr/bin/env python3
"""
Appian Handbook auto-updater.

What it does, every scheduled run:

1. RELEASE NOTES (handbook.md)
   Discovers every Appian version listed in the docs version selector,
   compares that list against what's already recorded in handbook.md, and
   backfills any missing versions -- not just the newest one. This means a
   missed run (or the very first run) catches up on everything, in order,
   instead of silently skipping releases.

2. PER-RELEASE REFERENCE LINKS (reference-index.md)
   For each newly-added release, extracts every function/smart-service/
   component/record-type/process-model/log/admin link mentioned in that
   release's notes -- title + link only, filed by category.

3. FULL CATALOG (catalog.md)
   Separately, rebuilt fresh every run (not appended): a complete index of
   every Appian function and every smart service, pulled from Appian's own
   master reference pages (Appian_Functions.html, Smart_Services.html).
   Again, title + link only -- no reference documentation content is
   copied, so this stays a navigation index rather than a mirror of
   Appian's docs.

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


def already_recorded_versions() -> set:
    if not HANDBOOK_PATH.exists():
        return set()
    text = HANDBOOK_PATH.read_text(encoding="utf-8")
    return set(re.findall(r"## Appian ([\d.]+) — synced", text))


def html_to_markdown_and_links(main):
    lines = []
    for el in main.find_all(["h1", "h2", "h3", "h4", "p", "li"]):
        text = el.get_text(" ", strip=True)
        if not text:
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
        if not title or not href:
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


def append_handbook_entry(version: str, url: str, body: str):
    today = date.today().isoformat()
    section = f"\n\n---\n\n## Appian {version} — synced {today}\n\nSource: {url}\n\n{body}\n"

    if not HANDBOOK_PATH.exists():
        HANDBOOK_PATH.write_text(
            "# Appian Handbook\n\n"
            "Auto-updated from public Appian release notes. "
            "Not affiliated with or endorsed by Appian Corporation.\n"
        )
    with HANDBOOK_PATH.open("a", encoding="utf-8") as f:
        f.write(section)


def append_reference_index(version: str, links: dict):
    if not links:
        return
    by_category = {}
    for url, (title, category) in links.items():
        by_category.setdefault(category, []).append((title, url))

    today = date.today().isoformat()
    lines = [f"\n\n---\n\n## Appian {version} — indexed {today}\n"]
    for category in sorted(by_category):
        lines.append(f"\n### {category}\n")
        for title, url in sorted(set(by_category[category])):
            lines.append(f"- [{title}]({url})")
    section = "\n".join(lines) + "\n"

    if not INDEX_PATH.exists():
        INDEX_PATH.write_text(
            "# Appian Reference Index\n\n"
            "Links only -- titles and URLs pointing to Appian's own official "
            "documentation for functions, smart services, components, objects, "
            "and logs mentioned in each release. No reference content is "
            "copied here; click through to docs.appian.com for the real thing.\n"
        )
    with INDEX_PATH.open("a", encoding="utf-8") as f:
        f.write(section)


# ---------------------------------------------------------------------------
# Full catalog: complete function + smart service index, rebuilt each run.
# ---------------------------------------------------------------------------

def fetch_full_function_catalog(version: str) -> dict:
    """Appian_Functions.html lists every function, grouped by category,
    each function name linking to its own reference page."""
    url = f"https://docs.appian.com/suite/help/{version}/Appian_Functions.html"
    try:
        soup = get_soup(url)
    except requests.RequestException:
        return {}

    main = soup.find("main") or soup.find("article") or soup.body
    catalog = {}
    for a in main.find_all("a", href=True):
        title = a.get_text(" ", strip=True)
        href = a["href"]
        if not title or "(" not in title:
            continue  # function links render as e.g. "flatten()" / "a!flatten()"
        full_url = href if href.startswith("http") else f"https://docs.appian.com{href}"
        if "docs.appian.com" not in full_url or "/fnc_" not in full_url and "Function" not in full_url:
            continue
        catalog.setdefault("Functions", []).append((title, full_url))
    return catalog


def fetch_full_smart_service_catalog(version: str) -> dict:
    """Smart service master index -- URL name has varied across doc
    versions, so try the known variants."""
    candidates = [
        f"https://docs.appian.com/suite/help/{version}/Smart_Services.html",
        f"https://docs.appian.com/suite/help/{version}/Process_Nodes_and_Smart_Services.html",
    ]
    for url in candidates:
        try:
            soup = get_soup(url)
        except requests.RequestException:
            continue
        main = soup.find("main") or soup.find("article") or soup.body
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
    latest = all_versions[0]
    print(f"Detected versions (newest first): {all_versions}")

    recorded = already_recorded_versions()
    missing = [v for v in all_versions if v not in recorded]
    missing.sort(key=lambda v: tuple(int(p) for p in v.split(".")))  # oldest first

    if not missing:
        print("Handbook already has every listed version.")
    else:
        print(f"Backfilling missing versions: {missing}")
        for version in missing:
            url, body, links = fetch_release_notes(version)
            append_handbook_entry(version, url, body)
            append_reference_index(version, links)
            print(f"  added {version}")

    rebuild_catalog(latest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
