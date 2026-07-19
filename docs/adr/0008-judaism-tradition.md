# ADR-0008: A `judaism` tradition, the third Abrahamic tradition

- **Status:** Accepted
- **Date:** 2026-07-19

## Context

The dataset reaches Judaism from several directions at once. The origins of
Christianity are inseparable from it: Jesus and Paul were Jews, the earliest church
was a movement within Second Temple Judaism, and "the parting of the ways" is a
parting from Judaism. On the Islamic side, entries already lean on Judaism as the
tradition they describe or contest: `tahrif` (the doctrine that earlier
scripture-communities altered their scriptures), `ahl-al-kitab` (the People of the
Book), `millat-ibrahim` (the religion of Abraham), and `isa`/`maryam` all point at a
Jewish counterpart that does not yet exist as a first-class node. Without a Judaism
tradition, those cross-tradition claims have no partner to compare against and must be
carried in prose.

Judaism is the natural third religious tradition (the roadmap already anticipated a
third), and unlike the `philosophy` namespace of ADR-0007 (a substrate, not a
religion) it is a religious tradition modeled exactly like Islam and Christianity.

## Decision

1. **A new `tradition` value is added: `judaism`.** It hosts Jewish figures, concepts,
   schools, events, and works, modeled identically to the existing religious
   traditions and living at `data/{type}/judaism/<id>.json`.

2. **It joins the one global id namespace and the same graph** (ADR-0001, ADR-0006).
   A `judaism` entity and a `christianity` entity never share an id; any entity may
   reference any other; forward references remain allowed.

3. **The same neutrality rules apply unchanged.** Judaism is described on its own
   terms (#7), and every cross-tradition link (a Christian or Islamic entry about a
   Jewish figure, scripture, or claim, or the reverse) obeys #10 and #11: it compares
   a shared question without ranking answers, and it never uses one tradition's polemic
   about another as a description of it. The Christian and Islamic readings of Jewish
   scripture and of figures like Abraham, Moses, and Jesus are attributed to those
   traditions, not fused into the Jewish entries.

4. **Schema change is additive, so MINOR.** Each schema's `tradition` enum gains
   `judaism`. Existing entities are untouched and remain valid. New entities in the
   batch that ships this change are authored against `schema_version` 0.5.0 (the enum
   addition is a contract change, as with ADR-0007's move to 0.4.0). No new entity
   type, no new relation type.

## Consequences

- The origins of Christianity can rest on real Jewish nodes (Second Temple Judaism,
  the Pharisees, the Tanakh) rather than on prose context, and `jesus-of-nazareth`,
  `paul-of-tarsus`, and `parting-of-the-ways` link to them directly.
- The Islamic entries that describe or contest Jewish scripture and figures (`tahrif`,
  `ahl-al-kitab`, `millat-ibrahim`, `isa`) gain a tradition to compare with, so those
  relationships become explicit graph edges under #10/#11 instead of prose.
- The comparative core widens from a two-religion axis to the three Abrahamic
  traditions plus the philosophical substrate, consistent with the mission.
- The demo's tradition grouping and styling pick up `judaism` from the data.
- The enum edit and the first `judaism` entities ship together in this batch, so no
  empty enum value sits in the contract ahead of its use.
