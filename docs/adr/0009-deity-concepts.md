# ADR-0009: Deity concepts, one per tradition

- **Status:** Accepted
- **Date:** 2026-09-15

## Context

The dataset maps doctrines about God (`tawhid`, `al-asma-wa-l-sifat`, `trinity`,
`divine-simplicity`, `ein-sof`, `tzimtzum`) but has no node for the God those
doctrines are about. The center of gravity of every covered tradition, the One
who is worshiped and obeyed, exists only as prose inside other entries. This is
a gap, not a feature: a theological dataset whose graph cannot answer "whom does
this tradition worship, and why" describes the periphery and omits the point.

The questions such a node must carry are the classic theological ones, recorded
as each tradition's attributed answers: which God does this tradition command
worship of, what is this God like, why worship this God, why is there a God at
all. The dataset records the questions and each tradition's answers; the reader
draws conclusions.

The reason the node has been avoided is neutrality: a single universal "God"
entity would force the editor to adjudicate whether the traditions worship the
same referent, a question the traditions themselves dispute in both directions.

## Decision

1. **God is modeled as a `concept`, one per tradition, never as a `figure` and
   never as a single cross-tradition node.** Each entry describes the tradition's
   own understanding of the God it worships, fully and on its own terms
   (neutrality principle #6, and the same self-understanding rule the manual
   applies to schools). Whether two traditions' God-concepts share a referent is
   never asserted or denied by the editor; where a tradition itself takes a
   position on that question (as Islam does regarding the God of Abraham, and
   Christianity does regarding the God of Israel), that position is recorded as
   the tradition's attributed claim.

2. **Ids follow each tradition's own dominant self-designation**, like every
   other slug in the dataset: `allah` (Islam), `hashem` (Judaism), and
   `god-in-christianity` (Christianity, since the bare slug `god` would read as
   a universal node, which point 1 rules out). The `hashem` entry covers the
   naming practice itself: the Tetragrammaton, the non-pronunciation tradition,
   and the Adonai and HaShem substitutions, since in Judaism the handling of the
   Name is inseparable from the concept of the Named.

3. **Scope of each entry.** The entry answers, as attributed positions with
   sources: (a) what kind of God this is (attributes, unity, relation to
   creation); (b) what worship and obedience this God commands and why the
   tradition holds worship to be owed; (c) how the tradition grounds the
   existence of this God (revelation, argument, or both, e.g. kalam cosmological
   arguments, the five ways, creation theology). Internal disputes about the
   God-concept (anthropomorphism debates, essence and attributes, palamite
   distinctions) belong to the doctrine entries, which link here rather than
   being absorbed.

4. **Graph wiring.** Doctrine entries about God link to their tradition's deity
   concept with `elaborates` or `related_to` (e.g. `tawhid` elaborates `allah`,
   `trinity` elaborates `god-in-christianity`, `ein-sof` related_to `hashem`).
   The three deity concepts link to each other pairwise with `compares_with`
   under the ADR-0005 rules: the note states the shared question and names the
   difference, and never equates, ranks, or harmonizes.

5. **No schema change.** `concept` already exists, the traditions already exist
   in the enum, and the relation types suffice. Entries are authored at the
   current `schema_version` (0.5.0).

## Consequences

- The graph gains its center: every tradition's doctrines about God now point at
  an explicit node for the God they are about, and the comparative axis of the
  dataset (ADR-0005) runs through the deity concepts themselves.
- These three entries carry the highest neutrality burden in the dataset. They
  receive the strictest review: every sentence must be attributable to the
  tradition or to scholarship about it, and the three-lens sourcing rule
  (academic, classical primary, contemporary insider) applies in full.
- The editor's line is drawn explicitly: the dataset describes whom each
  tradition worships and why; it does not itself worship, and it does not rule
  on the identity of referents across traditions.
- Later traditions added to the dataset ship a deity concept (or, for
  non-theistic traditions, the entry that occupies the corresponding place in
  that tradition's own self-understanding) as part of their first batch.
