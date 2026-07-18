#!/usr/bin/env python3
"""Cross-check each entry's sources against Crossref to surface real DOIs and
flag citations with no plausible external match for human review.

This is an AID, not a gate. Reference works (encyclopedias like EI2, SEP) often
have no DOI / no Crossref record, so a NONE result there is expected, not a
defect. Strong matches hand you a real DOI to attach to the source.

Usage:
    python3 scripts/verify_sources.py            # all entries
    python3 scripts/verify_sources.py tawhid     # only ids containing "tawhid"

# ponytail: Crossref bibliographic search + title similarity. Good enough to spot
# fabricated/mismatched refs and harvest DOIs. Swap in OpenAlex/a real matcher if
# hit-rate on reference works matters.
"""
import json
import ssl
import sys
import time
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

# macOS system Python often lacks a root cert bundle; use certifi's if present.
try:
    import certifi

    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
MAILTO = "hierologia@nurwandi.dev"  # polite-pool contact, adjust to a real inbox
UA = f"Hierologia-source-verifier (mailto:{MAILTO})"
STRONG, WEAK = 0.60, 0.35


def crossref_search(citation, rows=3):
    q = urllib.parse.urlencode(
        {"query.bibliographic": citation, "rows": rows, "mailto": MAILTO}
    )
    req = urllib.request.Request(
        f"https://api.crossref.org/works?{q}", headers={"User-Agent": UA}
    )
    with urllib.request.urlopen(req, timeout=25, context=SSL_CTX) as r:
        return json.load(r).get("message", {}).get("items", [])


def best_match(citation, items):
    best = (0.0, "", "")
    cl = citation.lower()
    for it in items:
        title = " ".join(it.get("title") or [])
        if not title:
            continue
        s = SequenceMatcher(None, cl, title.lower()).ratio()
        if s > best[0]:
            best = (s, title, it.get("DOI", ""))
    return best


def main():
    needle = sys.argv[1] if len(sys.argv) > 1 else ""
    files = [f for f in sorted(DATA.rglob("*.json")) if needle in f.stem]
    if not files:
        print("No matching entry files.", file=sys.stderr)
        return 1

    total = flagged = 0
    for f in files:
        doc = json.loads(f.read_text())
        for src in doc.get("sources", []):
            total += 1
            cite = src["citation"]
            try:
                items = crossref_search(cite)
            except Exception as e:
                print(f"?? [ERR ] {doc['id']}: {e}  ({cite[:50]})")
                flagged += 1
                continue
            score, title, doi = best_match(cite, items)
            verdict = "MATCH" if score >= STRONG else "WEAK" if score >= WEAK else "NONE"
            mark = {"MATCH": "ok  ", "WEAK": "~   ", "NONE": "??  "}[verdict]
            print(f"{mark}[{score:.2f}] {doc['id']}: {cite[:58]}")
            if verdict != "NONE":
                print(f"          crossref: {title[:64]}  {('doi:' + doi) if doi else ''}")
            if verdict != "MATCH":
                flagged += 1
            time.sleep(0.3)  # be polite to the API

    print(f"\n{total} sources checked; {flagged} without a strong match (review / expected for reference works).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
