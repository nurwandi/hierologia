# ADR-0010: Home tradition for shared history

- **Status:** Accepted
- **Date:** 2026-10-18

## Context

The history layer is reaching the meeting points between traditions: the
Crusades and the Rhineland massacres of 1096, the sack of Constantinople in
1204, its fall in 1453, al-Andalus, Granada 1492, and the Moriscos. These
events belong to the histories of two or three traditions at once, but the
`tradition` field holds a single value and decides the storage path
(`data/<type>/<tradition>/`). Choosing a tradition for such an entry can read
as a claim that the event "belongs" to one side, which is a neutrality risk on
exactly the entries where the narratives are most contested.

Alternatives considered:

- A new `interreligious` tradition value. Neutral on its face, but it mixes a
  category of relationship into a field that otherwise names a tradition, and
  it would make the Religion filter less meaningful.
- Making `tradition` an array. The most faithful model, but a breaking change
  to the schema, the storage layout, and every API client.

## Decision

1. **Every entity keeps exactly one home tradition.** No schema change.

2. **The home is the tradition whose community or institution the entity
   chiefly concerns.** A polity's fall is filed with that polity's tradition
   (`fall-of-baghdad-1258` under `islam`, `fall-of-constantinople-1453` under
   `christianity`, `fall-of-granada-1492` under `islam`). An institution of one
   tradition is filed with that tradition (`first-crusade` under
   `christianity`). Violence against a community is filed with that community
   (`rhineland-massacres-1096` under `judaism`).

3. **The home is a storage convention, not a claim of ownership.** Each such
   entry says so in `editorial_notes` and links to the other traditions'
   entries through relations, so the event is reachable from every side.

4. **The other traditions' perspectives are sourced from those traditions'
   own records and scholarship** (neutrality principles #10 and #11), not from
   the home tradition's account of them.

## Consequences

- No migration, no MAJOR or MINOR schema bump.
- The rule is mechanical enough to apply without debate in most cases; where
  it is genuinely unclear, the editor picks one, and the entry's
  `editorial_notes` gives the reason.
- Filtering by tradition returns an event under one tradition only; clients
  that want every tradition's view of an event follow its relations.
