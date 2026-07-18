#!/usr/bin/env python3
"""Validate every entity file against its schema and report relation integrity.

Directory under data/ selects the schema:
    data/concepts/... -> schema/concept.schema.json
    data/figures/...  -> schema/figure.schema.json
    data/schools/...  -> schema/school.schema.json

ids share one namespace across all entity types, so any entity may reference any
other by id. Exit non-zero on invalid JSON, schema failure, duplicate id, or
filename/id mismatch — this doubles as the CI gate. Dangling relation targets
are reported but NOT fatal: forward references to not-yet-written entities are
allowed by design.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schema"
DATA = ROOT / "data"

SCHEMA_BY_TYPE = {
    "concepts": "concept.schema.json",
    "figures": "figure.schema.json",
    "schools": "school.schema.json",
}


def main() -> int:
    try:
        import jsonschema
    except ImportError:
        print("ERROR: jsonschema not installed (pip install jsonschema)", file=sys.stderr)
        return 2

    validators = {}
    for entity_type, fname in SCHEMA_BY_TYPE.items():
        path = SCHEMA_DIR / fname
        if path.exists():
            validators[entity_type] = jsonschema.Draft202012Validator(json.loads(path.read_text()))

    files = sorted(DATA.rglob("*.json"))
    if not files:
        print("No entity files found.", file=sys.stderr)
        return 1

    ids: dict[str, Path] = {}
    targets: dict[str, list[str]] = {}
    status_counts: dict[str, int] = {}
    type_counts: dict[str, int] = {}
    errors = 0

    for f in files:
        rel = f.relative_to(ROOT)
        entity_type = f.relative_to(DATA).parts[0]
        validator = validators.get(entity_type)
        if validator is None:
            print(f"UNKNOWN TYPE  {rel}: no schema for data/{entity_type}/")
            errors += 1
            continue

        try:
            doc = json.loads(f.read_text())
        except json.JSONDecodeError as e:
            print(f"INVALID JSON  {rel}: {e}")
            errors += 1
            continue

        schema_errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))
        if schema_errors:
            for e in schema_errors:
                loc = "/".join(str(p) for p in e.path) or "(root)"
                print(f"SCHEMA FAIL   {rel}  [{loc}]: {e.message}")
            errors += 1
            continue

        cid = doc["id"]
        if cid in ids:
            print(f"DUPLICATE ID  {rel}: id '{cid}' also in {ids[cid].relative_to(ROOT)}")
            errors += 1
        ids[cid] = f
        if f.stem != cid:
            print(f"NAME MISMATCH {rel}: id '{cid}' != filename '{f.stem}'")
            errors += 1

        type_counts[entity_type] = type_counts.get(entity_type, 0) + 1
        status_counts[doc["status"]] = status_counts.get(doc["status"], 0) + 1
        for r in doc.get("relations", []):
            targets.setdefault(r["target"], []).append(cid)

    print(f"\nValidated {len(files)} file(s): {errors} error(s).")
    print("By type:", ", ".join(f"{k}={v}" for k, v in sorted(type_counts.items())))
    print("Status:", ", ".join(f"{k}={v}" for k, v in sorted(status_counts.items())))

    dangling = sorted(t for t in targets if t not in ids)
    if dangling:
        print(f"\nDangling relation targets (allowed — future entities): {len(dangling)}")
        for t in dangling:
            print(f"  {t}  <- referenced by: {', '.join(sorted(set(targets[t])))}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
