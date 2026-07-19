# Changelog

All notable changes to Hierologia are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the data schema follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.3.0] - 2026-07-19

The history layer opens and the Christian tradition deepens toward parity: two new
entity types, the ecumenical councils and creeds, the Islamic account of Jesus,
and an early Jewish-Christian sect that raises the comparison directly.

### Added
- **Two entity types, `Event` and `Work`** (ADR-0006). An `Event` is a datable
  happening (a council, synod, inquisition); a `Work` is a text (a creed,
  conciliar definition, treatise, canon). Both share the provenance, lifecycle,
  and neutrality model of the existing types. This is the foundation of the
  planned history and sociology module, and it is cross-tradition from the start.
- **The first four ecumenical councils** as Events (Nicaea 325, Constantinople
  381, Ephesus 431, Chalcedon 451) and **two creeds** as Works (the
  Niceno-Constantinopolitan Creed and the Definition of Chalcedon). These were
  dangling forward references and are now sourced, first-class nodes.
- **The Islamic account of Jesus**, anchoring new cross-tradition comparisons:
  `isa` (Jesus in Islam), `maryam` (Mary), and `hawariyyun` (the disciples in the
  Qur'an), with `isa compares_with incarnation` and `hawariyyun compares_with
  apostles`.
- **Early Christianity and the direct comparison**: `ebionites`, an early
  Jewish-Christian movement whose low Christology is compared with `tawhid` and
  `isa` as a shared question and explicitly never as a claim that Islam derives
  from it (#10, #11); plus `adoptionism` and the Christian `apostles`.
- **The Christian tradition deepened toward parity** (now 40 entities): the
  figures Origen, Cyril of Alexandria, Gregory of Nazianzus, Anselm, Calvin, and
  Barth; the branches and movements Roman Catholicism, Eastern Orthodoxy, the
  Reformed tradition, and monasticism; and the concepts homoousios, Eutychianism,
  sola fide, sola scriptura, the sacraments, and ecclesiology.
- `docs/governance/build-process.md`, the six-step batch lifecycle (scope, author,
  validate, review, promote, release) written down as a public methodology.
- Demo: the detail view now shows an event's date and location, a work's date, and
  a figure's dates.

### Notes
- The dataset is now 121 entities: 81 Islamic and 40 Christian, all `reviewed`
  (2 `verified`). Every new entity passed an independent peer-review audit that
  verified each citation. With councils and creeds now first-class, the social
  history layer (the Mihna, the Mudejar and Morisco communities) can follow using
  the same Event and Work types.

## [0.2.0] - 2026-07-19

The second tradition and the first cross-tradition comparisons: Hierologia
becomes a comparative dataset rather than a single-tradition one.

### Added
- **Christianity, the second tradition:** 15 entities, all `reviewed`. Six
  concepts (Trinity, Incarnation, atonement, grace, justification, original sin),
  four figures (Athanasius, Augustine, Aquinas, Luther), and five schools or
  movements (patristics, scholasticism, Protestantism, Arianism, Nestorianism).
- **Cross-tradition links (`compares_with`)**, the project's distinctive value:
  they assert that two traditions address a comparable question without equating,
  ranking, or harmonizing their answers. Examples: the Arian created Son and the
  createdness of the Qur'an; Aquinas and al-Ghazali on reason and revelation;
  original sin and *fitra* on the human condition at birth. See ADR-0005.
- Three Islamic entities anchoring the comparisons: `fitra` (the innate sound
  disposition, the counterpart to original sin) and the falsafa philosophers
  `ibn-sina` (Avicenna) and `ibn-rushd` (Averroes).
- Neutrality policy gains two principles: #10 (cross-tradition comparison compares
  questions, not answers) and #11 (cross-tradition sourcing is triangulated and
  non-polemical; a polemical account of another religion, such as John of Damascus
  on Islam, is never used as a neutral description of that religion).
- ADR-0005 (cross-tradition modeling): the `tradition` and relation `type` enums
  gain `christianity` and `compares_with`. The change is additive, so this is a
  MINOR bump; new entities are authored against `schema_version` 0.2.0.
- Demo: cross-tradition relations are shown distinctly (a cross-tradition marker
  and the other tradition's tag), and relation targets not yet documented render
  as plain "not yet documented" labels instead of dead links.

### Notes
- The dataset is now 93 entities: 78 Islamic and 15 Christian, all `reviewed`
  (2 `verified`). Councils and creeds (Nicaea, Chalcedon, the Nicene Creed) are
  referenced as forward references and await a later history module with its own
  entity types.

## [0.1.1] - 2026-07-19

### Added
- `.zenodo.json` archival metadata. This release is archived to Zenodo and
  minted a DOI, so the dataset is formally citable.

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
