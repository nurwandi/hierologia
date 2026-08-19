#!/usr/bin/env python3
"""Compact, token-frugal queries over the Hierologia dataset.

Prints only what you ask, and never dumps the heavy fields (description,
editorial_notes, sources). Use this for navigation instead of reading raw
entity files or grepping across the whole tree.

Usage:
  python3 scripts/query.py summary
      Per-tradition status (verified/reviewed/draft) and type counts.

  python3 scripts/query.py dangling
      Dangling relation targets (referenced but not present), grouped by the
      tradition(s) that reference them.

  python3 scripts/query.py refs-to <id>
      Every entity whose relations point at <id> (with the relation type).

  python3 scripts/query.py show <id> [<id> ...]
      Compact view of an entity: id, type, tradition, status, and summary only.

  python3 scripts/query.py list [--tradition T] [--type K] [--status S]
      Ids matching the filters (K is concept/figure/school/event/work).
"""
import json, glob, sys, collections

TYPE = {"concepts": "concept", "figures": "figure", "schools": "school",
        "events": "event", "works": "work"}


def load():
    ents = {}
    for f in sorted(glob.glob("data/*/*/*.json")):
        parts = f.split("/")
        d = json.load(open(f))
        d["_type"] = TYPE.get(parts[1], parts[1])
        ents[d["id"]] = d
    return ents


def cmd_summary(ents):
    trads = ["islam", "christianity", "judaism", "philosophy"]
    by = collections.defaultdict(collections.Counter)
    ty = collections.defaultdict(collections.Counter)
    for d in ents.values():
        by[d["tradition"]][d["status"]] += 1
        ty[d["tradition"]][d["_type"]] += 1
    print(f"total: {len(ents)}  verified: {sum(1 for d in ents.values() if d['status']=='verified')}"
          f"  reviewed: {sum(1 for d in ents.values() if d['status']=='reviewed')}")
    for t in trads:
        s, k = by[t], ty[t]
        tot = sum(s.values())
        if not tot:
            continue
        pct = 100 * s.get("verified", 0) // tot
        print(f"  {t:13} {tot:3}  verified {s.get('verified',0):3} ({pct}%)  reviewed {s.get('reviewed',0):3}"
              f"  draft {s.get('draft',0)}  |  c{k.get('concept',0)} f{k.get('figure',0)}"
              f" s{k.get('school',0)} e{k.get('event',0)} w{k.get('work',0)}")


def cmd_dangling(ents):
    present = set(ents)
    dang = collections.defaultdict(set)
    for d in ents.values():
        for r in d.get("relations", []):
            t = r.get("target")
            if t and t not in present:
                dang[t].add(d["tradition"])
    by = collections.defaultdict(list)
    for t, trs in dang.items():
        for tr in trs:
            by[tr].append(t)
    print(f"total dangling: {len(dang)}")
    for tr in ["judaism", "christianity", "islam", "philosophy"]:
        u = sorted(set(by[tr]))
        if u:
            print(f"  {tr} ({len(u)}): " + ", ".join(u))


def cmd_refs_to(ents, target):
    hits = []
    for d in ents.values():
        for r in d.get("relations", []):
            if r.get("target") == target:
                hits.append((d["id"], r.get("type", "?")))
    print(f"{target}  <- {len(hits)} referrer(s):")
    for i, t in sorted(hits):
        print(f"  {i}  ({t})")
    if target in ents:
        print(f"(note: {target} EXISTS in the dataset)")


def cmd_show(ents, ids):
    for i in ids:
        d = ents.get(i)
        if not d:
            print(f"{i}: NOT FOUND")
            continue
        print(f"{d['id']}  [{d['_type']}/{d['tradition']}/{d['status']}]")
        print(f"  {d.get('summary','(no summary)')}")


def cmd_list(ents, args):
    f = {"--tradition": None, "--type": None, "--status": None}
    it = iter(args)
    for a in it:
        if a in f:
            f[a] = next(it, None)
    out = [d["id"] for d in ents.values()
           if (not f["--tradition"] or d["tradition"] == f["--tradition"])
           and (not f["--type"] or d["_type"] == f["--type"])
           and (not f["--status"] or d["status"] == f["--status"])]
    print(f"{len(out)} match:")
    print("  " + ", ".join(sorted(out)))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    ents = load()
    cmd, rest = sys.argv[1], sys.argv[2:]
    if cmd == "summary":
        cmd_summary(ents)
    elif cmd == "dangling":
        cmd_dangling(ents)
    elif cmd == "refs-to" and rest:
        cmd_refs_to(ents, rest[0])
    elif cmd == "show" and rest:
        cmd_show(ents, rest)
    elif cmd == "list":
        cmd_list(ents, rest)
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
