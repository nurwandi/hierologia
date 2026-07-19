# ADR-0007: A `philosophy` tradition for the shared philosophical substrate

- **Status:** Accepted. Implementation deferred to the batch that first authors a philosophy entity (the Christian batch, where `aquinas` references `aristotle`).
- **Date:** 2026-07-19

## Context

The graph reaches for figures who belong to no religious tradition yet are load
bearing inside several. Aristotle is the immediate case: `aquinas` references him
as `aristotle`, and the same body of Greek thought (Aristotle, the Neoplatonists)
is pervasive in Islamic kalam and falsafa (the Mu'tazila's rationalism, Ibn Sina,
al-Farabi) and later in Jewish and Christian scholasticism. Filing Aristotle under
`christianity` because a Christian happens to cite him is a category error, as is
duplicating him under every tradition that borrows him. He is a shared substrate,
not a member of any one faith.

The `tradition` field is currently an enum of `["islam", "christianity"]` across
the concept, figure, school, event, and work schemas. There is no home for a
figure or idea whose provenance is philosophy rather than a religion.

## Decision

1. **A new `tradition` value is added: `philosophy`.** It names the philosophical
   substrate that religious traditions draw on and argue with: Greek philosophers
   first (Aristotle, Plato, Plotinus and the Neoplatonists), with room for later
   philosophers as the graph needs them. Entities live at
   `data/{concepts,figures,...}/philosophy/<id>.json` like any other tradition.

2. **The `tradition` field's meaning widens from "religious tradition" to
   "intellectual tradition or provenance domain."** This is the smallest change
   that fits: rather than inventing a separate "substrate" mechanism, philosophy is
   modeled as one more tradition in the existing per-tradition, one-global-id-
   namespace graph (ADR-0001, ADR-0006). A `philosophy` entity and an `islam`
   entity never share an id.

3. **Cross-substrate links use the existing vocabulary, from both sides.** A
   Christian or Islamic figure links to a philosopher with `influenced_by` (or a
   concept with `derives_from` / `related_to`); a `compares_with` across the
   substrate obeys neutrality #10 unchanged. The philosopher entity itself is
   written on its own terms, described as a philosopher, never annexed to a
   religion or presented as endorsing one.

4. **Schema change is additive, so MINOR.** Each schema's `tradition` enum gains
   `"philosophy"`. Existing entities are untouched and remain valid. The demo's
   tradition grouping and styling pick the new value up from the data. No new
   entity type, no new relation type.

5. **Neutrality holds without a new rule.** A philosopher is sourced with
   philosophical and historical scholarship and primary texts, per neutrality #8
   and #9. Where a religious tradition reads a philosopher a certain way (the
   scholastic Aristotle, the Avicennan Aristotle), that reading is attributed to
   the tradition, not fused into the philosopher's own entry.

## Consequences

- Aristotle, and later Plato and the Neoplatonists, become first class nodes that
  carry their own sourcing and can be referenced by any tradition, so
  `aristotle`-style forward references stop dangling once authored.
- The bridge between Islamic and Christian rationalism becomes explicit in the
  graph: both can link to the same philosophical node rather than each restating
  the influence in prose.
- The enum edit and the first `philosophy` file land together in the Christian
  batch (Batch 2), not before: the ADR records the decision now; the schema and
  data change ships with the entity that needs it, so no empty enum value sits in
  the contract ahead of its use.
- `School` under `philosophy` (e.g. a philosophical school such as Neoplatonism)
  is permitted by the same enum change but is out of scope until a concrete need
  arises; this ADR does not author one.
