# ADR-0002: Figure and School entity types

- **Status:** Accepted
- **Date:** 2026-07-18

## Context

The first 13 `Concept` entries produced 15 dangling relation targets. They split
cleanly into two kinds the `Concept` model cannot represent honestly:

- **People**, al-ashari, ahmad-ibn-hanbal, and others referenced via
  `articulated_by`.
- **Schools / movements**, mutazila, murjia, kharijites, qadariyya.

Forcing a person or a movement into the `Concept` schema would misrepresent them
(a person has a lifespan; a school has founders and a historical arc). The
data-first approach surfaced this need rather than us guessing it up front.

## Decision

1. **Add two entity types**, each with its own schema and directory:
   - `Figure` → `schema/figure.schema.json`, files under `data/figures/<tradition>/`.
   - `School` → `schema/school.schema.json`, files under `data/schools/<tradition>/`.
2. **Unified id namespace.** ids are unique across *all* entity types, so any
   entity may reference any other by id. `validate.py` enforces uniqueness and
   resolves dangling targets across the whole dataset.
3. **Directory determines schema.** `validate.py` maps the first path segment
   under `data/` (`concepts` / `figures` / `schools`) to its schema.
4. **Shared model, duplicated blocks.** All three schemas share the same
   `names`, `sources`, `status`, and versioning structure. For now this is
   **duplicated** in each schema file rather than factored into a shared
   `$defs` file referenced by `$ref`.
   - *Why:* cross-file `$ref` needs a resolver/registry in `validate.py`, added
     complexity for ~15 lines shared across 3 files that change rarely.
   - *Upgrade path:* if entity types or traditions multiply and the shared
     blocks start to drift, extract `schema/_defs.schema.json` and `$ref` it.
     This is a reversible change.

## Consequences

- The dataset becomes a genuine graph across concepts, people, and schools.
- Three schemas must be kept in sync by hand until the shared-defs extraction is
  justified. `validate.py` runs all three, so drift shows up as validation
  failures, not silent inconsistency.
- Relation vocabularies differ per entity type (a figure `founded` a school; a
  school is `founded_by` a figure), which is intentional, the direction and
  verb carry meaning.
