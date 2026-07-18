<p align="center">
  <img src="web/hierologia.svg" alt="Hierologia logo" width="96" height="96">
</p>

<h1 align="center">Hierologia</h1>

<p align="center"><strong>An open, neutral, well-sourced academic API for the comparative study of sacred traditions.</strong></p>

<p align="center">
  <a href="https://nurwandi.github.io/hierologia/"><img src="https://img.shields.io/badge/demo-live-2ea44f" alt="Live demo"></a>
  <a href="https://github.com/nurwandi/hierologia/actions/workflows/pages.yml"><img src="https://github.com/nurwandi/hierologia/actions/workflows/pages.yml/badge.svg" alt="Deploy"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-yellow" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/status-early%20draft-orange" alt="Status: early draft">
</p>

*Hierologia*, from Greek *hierós* (“sacred”) and *lógos*, is the study of the
sacred and religious traditions of any people, time, or place. This project
preserves theological, historical, and sociological knowledge as structured,
citable data. Every entry is neutral, attributed to its sources, and versioned.

**Live demo & API:** https://nurwandi.github.io/hierologia/

> ⚠️ **Early stage.** The dataset is small and every entry is currently a
> `draft`. Coverage is deliberately partial and growing; the project says what
> it does not yet cover rather than pretending to be complete.

## Scope

The first tradition is **Islamic theology (*kalam*)**. The dataset models three
kinds of entity, linked into a graph:

- **Concepts**, doctrines and ideas (e.g. *tawḥīd*, *qadar*, *ʿadl*)
- **Figures**, theologians and scholars (e.g. al-Ashʿarī, Ibn Ḥanbal)
- **Schools**, movements and schools of thought (e.g. Muʿtazila, Ashʿariyya, Atharis)

Further traditions will follow the same model.

## The data is the API

Each entity is a single JSON file under `data/`, validated against a schema in
`schema/`. The same files are served statically as a read-only API, no backend
required:

```
GET https://nurwandi.github.io/hierologia/api/index.json      # catalog of all entities
GET https://nurwandi.github.io/hierologia/api/tawhid.json     # one entity
```

```js
fetch("https://nurwandi.github.io/hierologia/api/tawhid.json")
  .then(r => r.json())
  .then(entry => console.log(entry.names.primary, entry.summary));
```

## Principles

- **Provenance is mandatory.** Every entry carries its `sources` with an honest
  confidence rating. No claim without traceability.
- **Neutrality.** Entries describe traditions and schools on their own terms and
  attribute contested claims; they never adjudicate which belief is correct.
  See [`docs/governance/neutrality.md`](docs/governance/neutrality.md).
- **Source diversity.** Sources triangulate across scholarly traditions -
  Western academic Islamic studies *and* Muslim/Islamic scholarship (classical
  primary texts, heresiographers, and reputable Muslim scholars alike).
- **Editorial lifecycle.** Entries move `draft → reviewed → verified`; only
  `reviewed`/`verified` entries are meant to be relied upon.

## Repository layout

```
data/       one JSON file per entity (concepts, figures, schools), the source of truth
schema/     JSON Schemas: the contract for every entity and the API payload
scripts/    validate.py (schema + relation checks), build_api.py, verify_sources.py
web/        the static single-page demo
docs/       decision records (docs/adr) and the neutrality policy
```

Design decisions and their rationale are recorded as ADRs in
[`docs/adr/`](docs/adr/).

## Validating

```
python3 scripts/validate.py     # 0 errors required (also the CI gate)
```

## License

Code is released under the [MIT License](LICENSE). The dataset is intended for
open scholarly reuse with attribution; a formal data license (e.g. CC BY 4.0) is
being finalized.
