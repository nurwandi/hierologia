# ADR-0001: Data model and file format

- **Status:** Accepted
- **Date:** 2026-07-18

## Context

Hierologia is a public academic API preserving theological, historical, and
sociological knowledge across religious traditions. Before building any
infrastructure, we need a data model whose credibility can be trusted by
scholars and whose shape is proven on real entries.

The hardest problem is not infrastructure, it is data: sourcing, provenance,
neutrality, and scope control. The first scope is **Islamic theology (kalam)**,
with **concepts/doctrines** as the core entity.

## Decision

1. **Core entity is `Concept`.** One JSON file per concept under
   `data/concepts/<tradition>/<id>.json`. The file is both the source of truth
   and the API payload.
2. **File format is JSON, not YAML.** JSON is the native API payload and needs
   no conversion step; its type handling is strict and unambiguous. The known
   cost, no inline comments, and ugly multi-line strings, is accepted and
   bounded: editorial commentary lives in a dedicated `editorial_notes` field,
   and long-form essays are deferred to a future `article` entity rather than
   stuffed into `description`.
3. **Provenance is mandatory.** Every concept requires at least one `sources`
   entry with a confidence rating. Credibility rests on traceability, not on
   the appearance of authority.
4. **Editorial lifecycle** via a `status` field: `draft → reviewed → verified`.
   Only `reviewed`/`verified` entries are meant to be relied upon.
5. **Neutrality** is a first-class constraint (see governance policy). Entries
   name interpretive schools without adjudicating between them.
6. **Data before infrastructure.** Prove the model on ~10–20 concepts before
   writing API code or Terraform.

## Consequences

- Consumers get a stable, self-describing payload validated by JSON Schema.
- Authoring long prose in JSON is mildly awkward; if it becomes painful, a
  conversion step (author in YAML, serve JSON) is a reversible future change.
- The `tradition` enum and `category` field will need to grow as scope widens;
  schema changes will follow SemVer.
