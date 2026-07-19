# Changelog

All notable changes to Hierologia are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the data schema follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0] - 2026-07-19

First public release: the Islamic theology (kalam) dataset, fully reviewed.

### Added
- Three entity types (`Concept`, `Figure`, `School`) with JSON Schemas and a
  unified id namespace.
- 75 Islamic (kalam) entities, all `reviewed`: 36 concepts, 21 figures, and 18
  schools covering the kalam schools (Mu'tazila, Ash'ari, Maturidi, Athari,
  Hanbali, Hanafi, and the early groups), the branches (Sunni, Shi'i/Twelver,
  Ibadi), and the movements (Sufism, Salafism), down to the Sufi doctrines and
  the Salafi tawhid cluster.
- Sourcing standard: scholarship only (journal articles, academic books, primary
  texts; no encyclopedias or tertiary sources), triangulated across three lenses
  (Western academic, classical Muslim, modern Muslim), with honest confidence.
- Governance: neutrality policy with nine principles, including balanced coverage
  of the traditionist position (#7), source diversity (#8), and source quality (#9).
- `scripts/validate.py` (multi-schema validation + relation integrity, the CI
  gate), `scripts/build_api.py` (static read-only API), and
  `scripts/verify_sources.py` (Crossref cross-check).
- `web/` static single-page demo: responsive master-detail layout, a grouped and
  filterable entry list (religion, type, status), sourced entries with confidence
  ratings, and per-entry API examples. Deployed to GitHub Pages via GitHub Actions.
- README with banner and badges, and `CITATION.cff` for citation.
- ADR-0001 (data model), ADR-0002 (Figure/School entities), ADR-0003 (project
  name), ADR-0004 (versioning and release), plus a tag-triggered release workflow.

### Notes
- Inception was data-first: prove the model on Islamic theology (kalam) before
  building dynamic infrastructure. All entries were promoted from `draft` to
  `reviewed` after a peer-review audit and the fixes it surfaced. Writing style:
  no em dashes.
