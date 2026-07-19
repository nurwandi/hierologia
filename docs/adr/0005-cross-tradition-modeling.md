# ADR-0005: Cross-tradition modeling

- **Status:** Accepted
- **Date:** 2026-07-19

## Context

The mission is the comparative study of sacred traditions, but the dataset has so
far covered only Islamic theology (kalam). Adding a second tradition
(Christianity) turns the project from a single-tradition dataset into a
comparative graph. The comparison is the point, and it is also the most dangerous
place to breach neutrality: a careless link can equate, rank, or subordinate one
tradition to another.

## Decision

1. **Traditions are added to the `tradition` enum as they are covered.**
   `christianity` is added now. Entities live under `data/<type>/<tradition>/`.
   Entity `id`s are globally unique across all traditions (a Christian and an
   Islamic concept never share an id, e.g. `trinity` vs `tawhid`).

2. **Each tradition is described on its own terms first** (neutrality principle
   #6). No tradition is the baseline, the norm, or the measure of another.
   Comparison is additive, never reductive: describing X in tradition A does not
   require translating it into tradition B's categories.

3. **Cross-tradition links use a new relation type, `compares_with`.** It means:
   *the target addresses a comparable theme or question in another tradition.* It
   asserts the comparability of a QUESTION, never the equivalence of an ANSWER.
   The relation `note` is mandatory here and must (a) state the shared theme and
   (b) name the difference. Example: `tawhid compares_with trinity` with the note
   "both address the oneness and nature of God; tawhid affirms an absolute
   oneness admitting no persons, the Trinity affirms one God in three persons."
   Never write a `compares_with` note that equates, ranks, or harmonizes the two.

4. **Schema change (additive, so MINOR).** The `tradition` enum and the relation
   `type` enums gain the values `christianity` and `compares_with`. Existing Islam
   entities remain valid (they use none of the new values). New entities are
   authored against `schema_version` 0.2.0; existing entities keep 0.1.0 until
   touched. The next dataset release is a MINOR bump (0.2.0).

## Consequences

- The demo's Religion filter becomes meaningful (more than one tradition).
- The graph gains genuinely comparative edges, the project's distinctive value.
- The neutrality burden rises. `compares_with` notes receive extra scrutiny in
  review: they are the entries most tempting to editorialize, harmonize, or rank.
- Sourcing for a comparison should ideally rest on scholarship that actually makes
  the comparison, not on the editor's own synthesis; where it is the editor's
  framing, the note says so.
