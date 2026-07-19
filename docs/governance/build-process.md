# Build Process

How every tradition and every batch of entities is built, so the dataset grows
the same disciplined way regardless of who or what is drafting it. This is the
process the Islamic and Christian datasets were built with, written down.

## Lifecycle of an entity

`draft -> reviewed -> verified`

- **draft**: authored and schema-valid, but not yet audited. Not to be relied on.
- **reviewed**: a peer-review audit has checked accuracy, neutrality, and that
  every source genuinely exists and supports its claim.
- **verified**: the cited passages have actually been read line by line. `high`
  confidence is honest only here.

## The six steps for a batch

1. **Scope.** List the target entities by type (`concept`, `figure`, `school`,
   `event`, `work`) and the cross-tradition `compares_with` edges the batch should
   create. Name the dangling references the batch is meant to close.

2. **Author.** Draft each entity to its schema. Sourcing is the hard part and is
   governed by [`neutrality.md`](neutrality.md):
   - three lenses (#8): outside academic scholarship, the tradition's own
     classical and primary texts, and its modern scholars;
   - scholarship only (#9): journal articles, academic monographs, primary texts.
     No encyclopedias or tertiary or popular sources;
   - cross-tradition sourcing is non-polemical (#11): an account of one tradition
     by another is used only where it is scholarship, never polemic.
   Confidence is honest (`high` only if the passage was read). No em dashes.
   New entities carry the current `schema_version`. Status starts at `draft`.

3. **Validate.** `python3 scripts/validate.py` must report 0 errors. This checks
   every file against its schema, unique ids, filename/id match, and relation
   integrity. It is also the CI gate. Dangling targets are allowed and reported.

4. **Peer-review audit.** An independent reviewer verifies each citation by
   searching for it, checks theological accuracy and neutrality (especially every
   `compares_with` note against #10), and flags any dishonest `high` confidence.
   The reviewer reports a per-entity verdict: pass, minor fixes, or needs-work.

5. **Apply fixes and promote.** Apply the reviewer's fixes, re-validate, then
   promote the batch from `draft` to `reviewed`.

6. **Release.** Rebuild the API (`scripts/build_api.py`), update `CHANGELOG.md`,
   and cut a versioned release. A new tradition, entity type, or batch of entities
   is a MINOR bump; a content fix or status promotion alone is a PATCH. When scope
   changes (a new tradition or type), refresh `CITATION.cff`, `.zenodo.json`, and
   the README before tagging. The tag triggers the GitHub Release and the Zenodo
   archive and DOI.

## Coverage is honest

The dataset is explicitly partial and growing. It says what it does not yet cover
rather than implying completeness: entities reference not-yet-written targets as
forward references, and the demo shows those as "not yet documented" rather than
as broken links.
