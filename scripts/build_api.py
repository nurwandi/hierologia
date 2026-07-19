#!/usr/bin/env python3
"""Generate the static read-only API + catalog for the GitHub Pages demo.

Copies every entity into web/api/<id>.json (adding an explicit `type`) and writes
web/api/index.json, a lightweight catalog the frontend loads first. ids are unique
across entity types, so a flat /api/<id>.json namespace is unambiguous.

# ponytail: static JSON *is* the read-only API, no server. Move to a real API
# (AWS) only when dynamic query / search / scale is actually needed.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "web" / "api"
TYPE = {"concepts": "concept", "figures": "figure", "schools": "school", "events": "event", "works": "work"}


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    index = []
    for f in sorted(DATA.rglob("*.json")):
        entity_type = TYPE[f.relative_to(DATA).parts[0]]
        doc = json.loads(f.read_text())
        doc["type"] = entity_type
        (OUT / f"{doc['id']}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=2)
        )
        index.append({
            "id": doc["id"],
            "type": entity_type,
            "tradition": doc["tradition"],
            "name": doc["names"]["primary"],
            "status": doc["status"],
            "summary": doc.get("summary", ""),
        })

    index.sort(key=lambda e: (e["type"], e["name"]))
    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2))
    print(f"Built {len(index)} entities -> web/api/ (index.json + per-entity)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
