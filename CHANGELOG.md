# Changelog

All notable changes to Hierologia are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the data schema follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.6.0] - 2026-07-19

A third namespace opens for the shared philosophical substrate, the Christian
dangling references are closed, and the Islamic side gains its self-understanding
layer, all linked by two new cross-tradition comparisons.

### Added
- **A `philosophy` tradition** (ADR-0007) for the Greek substrate that both kalam
  and scholasticism draw on, with `aristotle` as its first entry, written on his own
  terms and never annexed to a religion. The `tradition` enum gains `philosophy` in
  all five schemas; this is the additive schema change that carries `schema_version`
  from 0.3.0 to 0.4.0.
- **The Christian dangling references, closed**: the figures Constantine, Pelagius,
  and Peter Abelard; the concepts predestination, theosis, indulgences, and the Five
  Ways; the school Pelagianism; the Reformation as an Event; and the ecumenical
  councils as an institution.
- **Two cross-tradition comparisons** (#10): `predestination compares_with qadar`
  (divine determination and human freedom, framed as a shared question, neither
  answer ranked) and `theosis compares_with fana` (human participation in or nearness
  to a transcendent God).
- **The Islamic self-understanding layer**: `islam` (submission, in both the generic
  sense that all creation and all prophets submit and the specific sense of the final
  revelation), `hanif` (the primordial pure monotheist), `millat-ibrahim` (the
  religion of Abraham that Islam understands itself to continue and restore), and
  `tahrif` (the doctrine that earlier scripture-communities altered their scriptures).
  Each states the tradition's self-understanding fully on its own terms (#7) while
  attributing every claim that touches Abraham, Moses, Jesus, or the Jewish and
  Christian scriptures, rather than asserting it as neutral fact (#1, #11). `tahrif`
  is written strictly as the attributed Islamic doctrine and its internal debate
  (distortion of meaning versus corruption of the text), and does not adjudicate the
  actual textual history of the Bible.

### Notes
- The dataset is now 157 entities: 106 Islamic, 50 Christian, and 1 in the new
  philosophy namespace, 155 `reviewed` and 2 `verified`.
- MINOR release. The schema change (the enum gains `philosophy`) is additive and
  backward compatible, so `schema_version` moves 0.3.0 to 0.4.0 while existing
  entities remain valid (ADR-0004: dataset and schema versions are separate axes).

## [0.5.0] - 2026-07-19

Eleven Islamic entities close the Islamic dangling references, adding the political
theology of the caliphate, the Sufi vocabulary of annihilation and covenant, the
great hadith compilers, and the Salafi-Athari account of divine unity.

### Added
- **The theology of leadership**: `baya` (the pledge of allegiance) and `shura`
  (consultation) as the mechanisms Sunni thought invokes to constitute the
  caliphate, and `rashidun` as an Event (the "rightly guided" caliphate, 632-661).
  "Rightly guided" is carried only as an attributed Sunni honorific, and the Shi'i
  view is attributed and not ranked (#1, #7).
- **The hadith compilers** as Figures: al-Bukhari, Muslim ibn al-Hajjaj, and Malik
  ibn Anas, the authors behind the Work entries added in 0.4.0.
- **The Sufi path**: `baqa` (subsistence, the state paired with fana') and `mithaq`
  (the primordial covenant of the Day of Alast), plus `al-jili`, the metaphysician
  of the Perfect Human (al-insan al-kamil). Whether these amount to union with God
  is attributed to the tradition and its critics, not settled.
- **The Salafi-Athari account of divine unity**: `tawhid-al-rububiyya` (the oneness
  of lordship) and `kitab-al-tawhid` (Ibn Abd al-Wahhab's treatise), presented on
  the tradition's own terms, with critiques attributed and left unadjudicated (#7).
- **ADR-0007**: a decision to add a `philosophy` tradition for the shared
  philosophical substrate (Aristotle and the Greeks) that both kalam and
  scholasticism draw on; the schema change and first entity land in a later batch.

### Changed
- `khilafa` now resolves its reference to `baya` (the id drops the apostrophe the
  schema forbids), and `ali`'s confidence for Ayoub, The Crisis of Muslim History is
  aligned to `medium` to match that source elsewhere (same source, same rating).

### Notes
- The dataset is now 142 entities: 102 Islamic and 40 Christian, 140 `reviewed` and
  2 `verified`. The Islamic dangling references are closed; the remaining forward
  references are Christian (the Reformation, Aquinas's sources, and others), the
  first three caliphs (Abu Bakr, Umar, Uthman), and the Greek philosophers awaiting
  the `philosophy` tradition.
- MINOR release: it adds entities. `schema_version` stays 0.3.0; ADR-0007 records a
  decision but ships no contract change yet (ADR-0004: dataset and schema versions
  are separate axes).

## [0.4.0] - 2026-07-19

The Islamic history layer opens, mirroring the Christian one, and the first
Event-to-Event cross-tradition comparison links the two.

### Added
- **The Mihna** (the Abbasid inquisition of 833, which enforced the doctrine that
  the Qur'an is created) as an `Event`, with `mihna compares_with council-of-nicaea`,
  the first Event-to-Event cross-tradition link. Both are cases of political
  authority enforcing a created-or-uncreated doctrine, one on the Qur'an and one on
  the Son; the note compares the question and ranks neither (#10).
- The Abbasid figures of the Mihna: the caliphs al-Ma'mun, al-Mu'tasim, al-Wathiq,
  and al-Mutawakkil (who reversed it), and the Mu'tazili chief judge Ibn Abi Du'ad.
- Four hadith collections as `Work`s: Sahih al-Bukhari, Sahih Muslim, the Muwatta
  of Malik, and the Musnad of Ibn Hanbal, giving the Islamic side its own text
  layer alongside the Christian creeds.

### Notes
- The dataset is now 131 entities: 91 Islamic and 40 Christian, all `reviewed`
  (2 `verified`). Both traditions now carry a history layer of events and works,
  and the createdness controversy is a graph quadrangle: the doctrines Arianism and
  khalq-al-quran, and the Nicaea and Mihna that each enforced a side.
- This is a MINOR release because it adds entities; the `schema_version` stays
  0.3.0, since the Event and Work contract is unchanged since ADR-0006. Dataset
  version and schema version are separate axes (ADR-0004).

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
