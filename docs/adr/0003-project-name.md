# ADR-0003: Project name — Hierologia

- **Status:** Accepted
- **Date:** 2026-07-18

## Context

An early working name was rejected on two grounds:

1. **Generic and pre-owned in the field.** It was a term already heavily used
   within theology itself (classic works and an academic journal carry it), and
   its bare GitHub handle was taken. A project meant to be found and cited would
   be lost among the existing uses.
2. **Too narrow for the mission.** It was built on *theos* ("God") and so was
   theistic by construction, whereas the project aims to preserve traditions
   across the world, including non-theistic ones.

Candidate names were checked for meaning and availability (GitHub / domain /
PyPI / npm). Several were live brands or had muddled or off-topic meanings
(customer loyalty, a psychology app, a finance brand, a trademarked bodywork
term) or carried a single-tradition connotation.

## Decision

The project is named **Hierologia** (Greek *hieros*, "sacred" + *logos*).

- **Meaning fits the mission.** *Hierologia* is the study of the sacred and
  religious traditions of any people, time, or place, reconciling faith with
  reason — and, unlike theology, does not require a god as its focus. It is
  inherently comparative and cross-tradition. The name is close to a mission
  statement.
- **Available everywhere checked.** GitHub, the `.com` domain, PyPI, and npm were
  all free at decision time.
- **Neutral.** It privileges no single tradition, consistent with the neutrality
  policy.

## Consequences

- Schema `$id`s use `hierologia.dev`.
- Public repository: `nurwandi/hierologia` (personal).
- The word "theologian(s)/theology" in entry content is descriptive and
  unaffected; only the project brand is Hierologia.
