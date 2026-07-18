# Changelog

All notable changes to Hierologia are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the data schema follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Initial `Concept` data model and JSON Schema (`schema/concept.schema.json`).
- 13 kalam concepts (all `draft`): tawhid, shirk, al-asma-wa-l-sifat, tanzih,
  tashbih, iman, kufr, qadar, nubuwwa, akhira, adl, khalq-al-quran, ruyat-allah.
- `Figure` and `School` entity types + schemas; 4 figures (al-ashari,
  ahmad-ibn-hanbal, al-maturidi, wasil-ibn-ata) and 6 schools (mutazila,
  ashariyya, maturidiyya, murjia, kharijites, qadariyya), all `draft`.
- `scripts/validate.py` — multi-schema validation + relation integrity (CI gate).
- Governance: neutrality policy (draft), incl. balanced-coverage principle for
  the Athari/traditionist position.
- ADR-0001 (data model), ADR-0002 (Figure/School entities).

## [0.1.0] - 2026-07-18

- Project inception. Scope: Islamic theology (kalam), concepts/doctrines as the core entity.
- Data-first approach: prove the model on ~10–20 concepts before building API or infrastructure.
