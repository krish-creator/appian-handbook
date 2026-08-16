#!/usr/bin/env python3
"""
Appian Handbook auto-updater.

What it does:
1. Visits a known Appian docs release-notes page to discover the version selector,
   which lists all available releases (newest first).
2. Fetches the release notes page for the newest version.
3. Converts the main content to clean Markdown.
4. Compares it to what's already saved in handbook.md for that version.
5. If new/changed, appends a dated, versioned section to handbook.md.
6. Separately, extracts every function/smart-service/object/component link
   mentioned in that release's notes and files it into reference-index.md
   as a categorized list of titles + links back to the official Appian
   docs page. No reference documentation content is copied -- only the
   name and a link, same as any changelog or blog post would do.

Designed to run for free on a schedule via GitHub Actions (see
.github/workflows/update.yml). It only touches PUBLIC Appian documentation
pages (docs.appian.com) -- NOT Appian Academy, which requires a login and
is intentionally out of scope (scraping authenticated training content
would violate Appian's terms of service).
"""

import re
import sys
import hashlib
from datetime import date, datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

HANDBOOK_PATH = Path(__file__).resolve().parent.parent / "handbook.md"
INDEX_PATH = Path(__file__).resolve().parent.parent / "reference-index.md"
STATE_PATH = Path(__file__).resolve().parent.parent / ".last_version"

# URL-pattern -> category, used to file each linked doc page into a bucket.
# Order matters: more specific patterns first.
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

# A stable, known-good release-notes URL used just to read the version
# selector (the dropdown/list of versions shown on every release-notes page).
SEED_URL = "https://docs.appian.com/suite/help/25.3/Appian_Release_Notes.html"

HEADERS = {
    "User-Agent": "AppianHandbookBot/1.0 (personal, non-commercial, respectful polling; "
                  "contact: set-your-email-here)"
}


def get_soup(url: str) -> BeautifulSoup:
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def discover_latest_version() -> str:
    """The release-notes page includes a version list (e.g. 26.7, 26.6, ...).
    The first entry is the newest release."""
    soup = get_soup(SEED_URL)
    text = soup.get_text("\n")
    versions = re.findall(r"\b(2\d\.\d)\b", text)
    if not versions:
        raise RuntimeError("Could not detect any version numbers on the seed page.")
    # First occurrence in the version selector is newest.
    seen = []
    for v in versions:
        if v not in seen:
            seen.append(v)
    return seen[0]


def fetch_release_notes_markdown(version: str) -> str:
    url = f"https://docs.appian.com/suite/help/{version}/Appian_Release_Notes.html"
    soup = get_soup(url)

    main = soup.find("main") or soup.find("article") or soup.body
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

    # Collect reference links (functions, smart services, components, etc.)
    # mentioned anywhere in the release notes -- title + URL only.
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

    return url, body, links


def categorize(url: str):
    for pattern, category in CATEGORY_PATTERNS:
        if pattern.search(url):
            return category
    return None


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def update_reference_index(version: str, links: dict):
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


def main():
    version = discover_latest_version()
    print(f"Latest detected Appian version: {version}")

    last_version = STATE_PATH.read_text().strip() if STATE_PATH.exists() else ""

    url, body, links = fetch_release_notes_markdown(version)
    new_hash = content_hash(body)

    last_hash = ""
    if STATE_PATH.exists():
        parts = STATE_PATH.read_text().strip().split("|")
        if len(parts) == 2:
            last_version, last_hash = parts

    if version == last_version and new_hash == last_hash:
        print("No changes detected. Handbook is already up to date.")
        return 0

    today = date.today().isoformat()
    section = (
        f"\n\n---\n\n"
        f"## Appian {version} — synced {today}\n\n"
        f"Source: {url}\n\n"
        f"{body}\n"
    )

    if not HANDBOOK_PATH.exists():
        HANDBOOK_PATH.write_text(
            "# Appian Handbook\n\n"
            "Auto-updated from public Appian release notes. "
            "Not affiliated with or endorsed by Appian Corporation.\n"
        )

    with HANDBOOK_PATH.open("a", encoding="utf-8") as f:
        f.write(section)

    update_reference_index(version, links)

    STATE_PATH.write_text(f"{version}|{new_hash}")
    print(f"Handbook updated with Appian {version}. Indexed {len(links)} reference links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
