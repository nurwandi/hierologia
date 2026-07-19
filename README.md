<p align="center">
  <img src="web/hierologia.svg" alt="Hierologia logo" width="88" height="88">
</p>

<h1 align="center">Hierologia</h1>

<p align="center"><strong>An open, neutral, well-sourced academic API for the comparative study of sacred traditions.</strong></p>

<p align="center">
  <a href="https://nurwandi.github.io/hierologia/"><img src="https://img.shields.io/badge/demo-live-2ea44f" alt="Live demo"></a>
  <a href="https://github.com/nurwandi/hierologia/actions/workflows/pages.yml"><img src="https://github.com/nurwandi/hierologia/actions/workflows/pages.yml/badge.svg" alt="Deploy"></a>
  <a href="https://doi.org/10.5281/zenodo.21436391"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.21436391.svg" alt="DOI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-yellow" alt="License: MIT"></a>
</p>

*Hierologia*, from Greek *hierós* (“sacred”) and *lógos*, is the study of the
sacred and religious traditions of any people, time, or place. This project
preserves theological, historical, and sociological knowledge as structured,
citable data. Every entry is neutral, attributed to its sources, and versioned.

<p align="center">
  <img src="assets/hierologia-banner.jpg" alt="Hierologia" width="100%">
</p>

**Live demo & API:** https://nurwandi.github.io/hierologia/

> **Status.** Two traditions are covered: Islamic theology (*kalam*) with 91
> entities and Christian theology with 40, all peer-`reviewed`, linked by
> cross-tradition comparisons. Coverage is deliberately partial and growing; the
> project says what it does not yet cover rather than pretending to be complete.

## Scope

Two traditions are covered: **Islamic theology (*kalam*)** and **Christian
theology**, linked by cross-tradition comparisons. The dataset models five kinds
of entity, linked into a graph:

- **Concepts**, doctrines and ideas (e.g. *tawḥīd*, *qadar*, the Trinity, grace)
- **Figures**, theologians and scholars (e.g. al-Ashʿarī, Ibn Ḥanbal, Augustine, Aquinas)
- **Schools**, movements and schools of thought (e.g. Muʿtazila, Ashʿariyya, patristics, scholasticism)
- **Events**, datable happenings (e.g. the councils of Nicaea and Chalcedon, the Abbasid Mihna)
- **Works**, texts and documents (e.g. the Nicene Creed, Ṣaḥīḥ al-Bukhārī)

Cross-tradition `compares_with` links compare a shared question across traditions
without equating the answers. Further traditions will follow the same model.

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
- **Source diversity.** Sources triangulate across scholarly vantages: outside
  academic scholarship, each tradition's own classical and primary texts, and its
  modern scholars. An account of one tradition by another is used only where it is
  scholarship, never polemic.
- **Editorial lifecycle.** Entries move `draft → reviewed → verified`; only
  `reviewed`/`verified` entries are meant to be relied upon.

## Repository layout

```
data/       one JSON file per entity (concepts, figures, schools, events, works), the source of truth
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

The code (`scripts/`, `schema/`, `web/`) is released under the
[MIT License](LICENSE). The dataset (`data/` and the API payloads built from it) is
released under the
[Creative Commons Attribution 4.0 International License (CC BY 4.0)](LICENSE-DATA):
you may share and adapt it, including commercially, provided you give appropriate
credit and indicate changes. Please attribute via the dataset DOI
([10.5281/zenodo.21436391](https://doi.org/10.5281/zenodo.21436391)) and
[`CITATION.cff`](CITATION.cff).
