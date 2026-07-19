# ADR-0006: Event and Work entities

- **Status:** Accepted
- **Date:** 2026-07-19

## Context

The comparative graph reaches for entities that are neither a doctrine
(`Concept`), a person (`Figure`), nor a movement (`School`). An ecumenical council
is a datable historical happening; a creed is a text. Modeling either as a
`School` is a category error, and Christian entities already carry forward
references to `council-of-nicaea`, `council-of-chalcedon`, `council-of-ephesus`,
and `nicene-creed` that resolve to nothing.

This is the long-planned history and sociology module. The same two shapes,
an event and a text, also cover Islamic material (the Mihna over the createdness
of the Qur'an; the canonical hadith collections) and the later social history the
project intends to reach (the Mudejar and Morisco communities, Aljamiado
literature). Introducing them once, generically, avoids a Christianity-only patch.

## Decision

1. **Two new entity types are added: `Event` and `Work`.**
   - `Event` is a datable historical happening (council, synod, inquisition,
     expulsion). It carries `category`, `location`, and a `date` of `year`,
     optional `end_year`, and a `note`.
   - `Work` is a text or document (creed, conciliar definition, treatise, canon,
     authoritative collection). It carries `category` and a `date` of `year` and
     `note`.
   - Both share the provenance and lifecycle model of the existing types:
     `sources` with honest `confidence`, `status` (`draft -> reviewed ->
     verified`), neutral voice, and the same `tradition` enum.

2. **They join the one global id namespace and the same graph.** An `Event` and a
   `Concept` never share an id. Any entity may reference any other by id,
   including the new types, and forward references remain allowed.

3. **Each type gets its own relation vocabulary, plus the shared
   `related_to` and `compares_with`.**
   - `Event`: `convened_by`, `participant`, `condemned`, `affirmed`, `produced`
     (e.g. a council produced a creed), `preceded_by`, `followed_by`.
   - `Work`: `authored_by`, `adopted_at` (e.g. a creed adopted at a council),
     `affirms`, `condemns`, `part_of`, `responds_to`.

4. **Schema change is additive, so MINOR.** New schemas `schema/event.schema.json`
   and `schema/work.schema.json`; `validate.py` and `build_api.py` gain the
   `events/` and `works/` directories. Existing entities are untouched and remain
   valid. New entities are authored against `schema_version` 0.3.0; the next
   dataset release is a MINOR bump (0.3.0).

## Consequences

- The demo's Type filter gains `event` and `work` groups automatically (it is
  built from the data). The detail view should show an event's date and location
  and a work's date; this is a small, additive frontend change.
- Councils and creeds stop being dangling forward references and become first
  class nodes that carry their own sourcing and comparisons.
- The same types host Islamic events and texts and the future social-history
  layer, so the module is cross-tradition from the start, consistent with the
  mission and with ADR-0005.
- Neutrality principles #10 and #11 apply unchanged: a `compares_with` on an
  `Event` or `Work` compares a question, not an answer, and rests on scholarship
  rather than one tradition's polemic about another.
