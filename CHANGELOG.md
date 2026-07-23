# Changelog

All notable changes to Hierologia are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the data schema follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.13.0] - 2026-07-23

Judaism Batch 2, the medieval Sephardic golden age and its great texts, the second step of the
Judaism-to-parity campaign. All eight rest on open Sefaria primary texts read line-by-line and
enter directly as `verified`.

### Added
- **Five figures**: `saadia-gaon` (the Gaon of Sura, the first systematic Jewish philosophy),
  `judah-halevi` (the Andalusian poet and the Kuzari), `ibn-ezra` (the peshat exegete and
  grammarian), `nachmanides` (the Ramban, Talmudist and early kabbalist; the forced Disputation
  of Barcelona attributed on both sides, not adjudicated), and `david` (King David, on Judaism's
  own terms, a shared figure compared with the Christian and Islamic readings, not harmonized).
- **Three works**: `mishneh-torah` and `guide-for-the-perplexed` (Maimonides' code and his
  philosophy) and `kuzari` (Judah Halevi's dialogue).

### Changed
- All eight enter as `verified` (open Sefaria primaries read line-by-line: Yesodei ha-Torah, the
  Guide I.1/I.58, the Kuzari, Ibn Ezra on Deuteronomy 1:2, Ramban's foreword and on Genesis,
  Beliefs and Opinions, 2 Samuel 7). The verified tier is now 63.
- Corrected a stale "halakha is a dangling reference" note in `mishneh-torah` and `maimonides`
  (halakha and mashiach now exist).

### Notes
- Judaism grows from 19 to 27 entities. The dataset is now 215: 115 Islamic, 68 Christian, 27
  Jewish, 5 philosophy; 152 `reviewed` and 63 `verified`.
- MINOR release: adds entities, no schema change. `schema_version` stays 0.5.0.

## [0.12.0] - 2026-07-23

The Judaism section, which had no concept entities at all, gains its conceptual and medieval
spine. This begins a campaign to bring Judaism toward parity with the Christian and Islamic
coverage. Because the Jewish canon is open on Sefaria, all eight new entities rest on open
primary texts read line-by-line and enter directly as `verified`.

### Added
- **Six core concepts** (Judaism's first): `halakha` (Jewish law), `mitzvot` (the commandments,
  the 613), `oral-torah` (the Oral Torah), `brit` (the covenant), `shema` (the declaration of
  God's oneness), and `mashiach` (the Jewish messianic hope, a human Davidic king and a
  this-worldly age, the Christian identification attributed as a cross-tradition difference, not
  adjudicated).
- **Two medieval figures**: `maimonides` (the Rambam, the Mishneh Torah and the Guide for the
  Perplexed) and `rashi` (the preeminent commentator on the Tanakh and the Talmud).

### Changed
- All eight enter as `verified`: their load-bearing open Sefaria primaries (Makkot 23b for the
  613, the Mishneh Torah and Sefer HaMitzvot, the Shulchan Aruch, Pirkei Avot 1:1, Genesis 17
  and Exodus 24, Deuteronomy 6:4-9, Hilchot Melachim 11-12, and Rashi on Genesis 1:1) were read
  line-by-line and independently confirmed. The verified tier is now 55.
- Cross-tradition `compares_with` links added: brit <-> mithaq, shema <-> tawhid, mashiach <->
  jesus-of-nazareth, each comparing the shared question and stating the difference without ranking.

### Notes
- Judaism grows from 11 to 19 entities (its first six concepts). The dataset is now 207: 115
  Islamic, 68 Christian, 19 Jewish, 5 philosophy; 152 `reviewed` and 55 `verified`.
- MINOR release: adds entities, no schema change. `schema_version` stays 0.5.0.

## [0.11.0] - 2026-07-23

The four forward references the dataset had left open are now authored, and each rests on an
open primary read line-by-line, so all four enter directly as `verified`.

### Added
- **`council-of-florence`** (event): the Ferrara-Florence council (1438-1445) and its union
  decree Laetentur Caeli, defining the Filioque, purgatory, papal primacy, and the Eucharistic
  bread; the Eastern rejection of the union recorded as historical fact, the disputes not
  adjudicated.
- **`transubstantiation`** (concept): the Catholic doctrine (Lateran IV 1215, Aquinas, Trent
  1551), with the Lutheran, Reformed, and Eastern Orthodox accounts attributed as alternatives.
- **`montanism`** (school): the second-century New Prophecy, presented through the hostile
  heresiologists (Eusebius, attributed) balanced by Tertullian's sympathetic testimony.
- **`plotinus`** (figure, philosophy): the founder of Neoplatonism and the Enneads, on his own
  terms, his Christian, Islamic, and Jewish receptions attributed.

### Changed
- All four new entities enter as `verified` (their load-bearing open primaries, the Florence and
  Trent decrees, Aquinas's Summa, Eusebius, and the MacKenna Enneads, were read line-by-line and
  independently confirmed). The verified tier is now 47.

### Notes
- The dataset is now 199 entities: 115 Islamic, 68 Christian, 11 Jewish, and 5 philosophy, 152
  `reviewed` and 47 `verified`. The four targeted dangling references are closed; authoring
  opened eight smaller new ones (filioque, papal-primacy, great-schism, eucharist, real-presence,
  montanus, ammonius-saccas, porphyry), so dangling goes 4 -> 8.
- MINOR release: it adds entities, no schema change. `schema_version` stays 0.5.0.

## [0.10.4] - 2026-07-23

### Changed
- Promoted two entries `reviewed` -> `verified` after their load-bearing open primary sources
  were read line-by-line: `gnosticism` (Irenaeus, Against Heresies I.1-I.5, as an attributed
  hostile report, cross-checked against the open Nag Hammadi primaries, the Apocryphon of John
  and the Gospel of Truth) and `talmud` (the open Sefaria text: Bavli Berakhot 2a showing a
  Mishnah followed by its Gemara, and the Jerusalem Talmud, confirming the two Talmuds and the
  six-order structure). The verified tier is now 43.
- Sourcing improvements: raised the Irenaeus Against Heresies source to `high` in `gnosticism`
  and broadened its cited chapters to I.1-I.5; added the open Sefaria Talmud text at `high` to
  `talmud`, giving it its first openly-auditable primary source.

### Notes
- PATCH: status and sourcing fixes, no new entities and no schema change. Still 195 entities;
  152 `reviewed` + 43 `verified`. `schema_version` unchanged. This closes the readily
  open-primary-verifiable pool; the remaining `reviewed` entries rest on classical/paywalled
  scholarship or are broad topics no single passage carries.

## [0.10.3] - 2026-07-22

### Changed
- Promoted four entries `reviewed` -> `verified` after their load-bearing open primary sources
  were read line-by-line: `irenaeus` (Against Heresies: the rule of faith I.10, the fourfold
  Gospel III.11.8, apostolic succession III.3, recapitulation III.18), `tertullian` (Against
  Praxeas, added as a source, for the Latin trinitas/persona/substantia vocabulary), `marcion`
  (Irenaeus Against Heresies I.27 and Tertullian Against Marcion I, as attributed hostile
  witnesses to his two-god teaching), and `mishnah` (the open Sefaria text: the six orders and
  the Pirkei Avot 1:1 chain of transmission). The verified tier is now 41.
- Sourcing improvements from the reads: added Tertullian's Against Praxeas at `high` to
  `tertullian`; added the open Sefaria Mishnah text at `high` to `mishnah`; raised the Irenaeus
  Against Heresies source to `high` in both `irenaeus` and `marcion` and broadened its cited
  chapters; re-anchored the `marcion` Tertullian URL to Against Marcion Book I; and refreshed a
  few stale "dangling" notes in `marcion` (tertullian and gnosticism now exist).

### Notes
- PATCH: status and sourcing fixes, no new entities and no schema change. Still 195 entities;
  154 `reviewed` + 41 `verified`. `schema_version` unchanged.

## [0.10.2] - 2026-07-20

### Changed
- Promoted two entries `reviewed` -> `verified` after their load-bearing open primary sources
  were read line-by-line: `arianism` (Athanasius, Four Discourses against the Arians, Book I,
  which extracts and opposes Arius's Thalia) and `ebionites` (Irenaeus, Against Heresies I.26,
  the earliest attributed report). The verified tier is now 37.
- A verification sweep of nine candidates kept seven `reviewed`, honestly: their open primary
  texts carry only a definitional or scriptural anchor, while each entry's distinctive claim
  rests on secondary or paywalled scholarship (`tertullian`, `monasticism`, `indulgences`,
  `predestination`, `iman`, `khatam-al-nabiyyin`, `maad`).
- Accuracy fixes surfaced by the reads: the `arianism` Athanasius source URL now points to the
  discourse text (was the volume index); the `ebionites` Irenaeus translator corrected (Roberts
  and Rambaut); a Calvin misquotation in `predestination` corrected to "adopts some to the hope
  of life, and adjudges others to eternal death" (Institutes III.21.5); and `iman` now notes
  that Q 2:285 names four of the six objects of faith.

### Notes
- PATCH: status and content fixes, no new entities and no schema change. Still 195 entities;
  158 `reviewed` + 37 `verified`. `schema_version` unchanged.

## [0.10.1] - 2026-07-20

### Changed
- Promoted four entries `reviewed` -> `verified` after their load-bearing open primary
  sources were read line-by-line and independently confirmed: `council-of-trent` and
  `purgatory` (the Trent decrees at papalencyclicals.net, the cited sessions read verbatim),
  `adoptionism` (Eusebius, Ecclesiastical History 5.28, the "Little Labyrinth"), and
  `socrates` (Plato's Apology, verified against an open Stephanus-numbered text). The verified
  tier is now 35 entries.
- Accuracy fixes surfaced by the verification reads: `adoptionism` now attributes the "Spirit
  descended at baptism" characterization to the secondary scholarship rather than to the
  Eusebius passage (which says only "a mere man"); `socrates` now cites an openly-checkable
  Apology text so the rating is reader-auditable, and separates the Apology's "unexamined life"
  maxim from the broader-Plato doctrines ("virtue is knowledge", "no one does wrong willingly").

### Notes
- PATCH: status and content fixes, no new entities and no schema change. Still 195 entities;
  160 `reviewed` + 35 `verified`. `schema_version` stays 0.5.0.

## [0.10.0] - 2026-07-20

The remaining clear-cut forward references are closed: nine more figures, texts, and
movements the dataset had pointed at now exist, and its dangling references fall to four.

### Added
- **The Reformation cluster**: `purgatory` (the Catholic doctrine, with the Protestant
  rejection and the Orthodox difference attributed), the reformer `huldrych-zwingli`
  (Zurich, the memorialist Eucharist, the 1529 Marburg break with Luther), and the
  `council-of-trent` (1545-1563, the Counter-Reformation's doctrinal core), on a clean id.
- **The early and medieval church**: `tertullian` (the Latin apologist, later Montanist),
  `bernard-of-clairvaux` (the Cistercian abbot who opposed Abelard at Sens), and
  `gnosticism` (the second-century currents, presented through both the hostile
  heresiologists, attributed, and the primary Nag Hammadi texts, with the scholarly debate
  over the category itself flagged, not resolved).
- **Philosophy and Judaism**: `socrates` (the second philosopher-figure, on his own terms,
  the Socratic problem noted) and `neoplatonism` (the movement of Plotinus, its Christian,
  Islamic, and Jewish receptions attributed); and `judah-ha-nasi`, the traditional redactor
  of the Mishnah.

### Changed
- `reformation` now points to the clean `council-of-trent` id (was `council-of-trent-1545`),
  and its vague `late-medieval-reform` forward reference is dropped (the precursor context
  survives in prose) rather than forced into an entity.

### Notes
- The dataset is now 195 entities: 115 Islamic, 65 Christian, 11 Jewish, and 4 in the
  philosophy namespace, 164 `reviewed` and 31 `verified`. Dangling forward references drop
  from 10 to 4, all four newly opened by this batch (council-of-florence, montanism,
  plotinus, transubstantiation).
- MINOR release: it adds entities, no schema change. `schema_version` stays 0.5.0.

## [0.9.0] - 2026-07-19

The clear-cut forward references are closed: twelve figures and texts the dataset had
pointed at now exist.

### Added
- **The first three Rashidun caliphs** as figures: `abu-bakr`, `umar`, and `uthman`, with
  the Sunni/Shi'i divide over their legitimacy attributed on both sides, adjudicated on
  neither.
- **Isaac and Ishmael as a cross-tradition pair**: `isaac` (judaism) and `isma-il`
  (islam), two distinct sons of Abraham joined by `compares_with`, with the disputed
  Akedah/dhabih son attributed to each tradition (Isaac per Genesis 22, Ishmael in the
  widely held Islamic exegesis, which the Qur'an does not name).
- **The early church**: `peter` (the Petrine primacy given as the Catholic reading,
  attributed), `james-brother-of-jesus`, and the second-century `marcion` (whose teaching
  is recorded through his hostile opponents, attributed) and `irenaeus`.
- **`plato`**, the second philosopher (pupil of Socrates, teacher of Aristotle), on his
  own terms.
- **The rabbinic corpus**: the `mishnah` and the `talmud` as Jewish works.

### Notes
- The dataset is now 186 entities: 115 Islamic, 59 Christian, 10 Jewish, and 2 in the
  philosophy namespace, 155 `reviewed` and 31 `verified`. Dangling forward references drop
  from 17 to 10.
- MINOR release: it adds entities, no schema change. `schema_version` stays 0.5.0.

## [0.8.5] - 2026-07-19

The four ecumenical councils and two more Islamic concepts reach `verified`.

### Changed
- **`verified` grows from 25 to 31.** The four ecumenical councils as Events,
  `council-of-nicaea`, `council-of-constantinople`, `council-of-ephesus`, and
  `council-of-chalcedon`, verified against the promulgated conciliar acts read in the
  open NPNF2-14 edition (the homoousios creed and the anathema against Arius; the
  enlarged Holy Spirit article and Canon 1 against the Pneumatomachi; the deposition of
  Nestorius and the Theotokos; the Chalcedonian Definition and the Tome of Leo). And two
  Islamic concepts, `mithaq` (Q 7:172, the covenant of Alast) and `dhikr` (Q 13:28,
  33:41), against directly read scripture. Each gains an open primary-source object at
  `high`.

### Notes
- PATCH release: status promotions and sourcing only, no new entities and no schema
  change. `schema_version` stays 0.5.0.

## [0.8.4] - 2026-07-19

Five more entries reach `verified`; `maad` gains its Qur'anic source while honestly
staying `reviewed`.

### Changed
- **`verified` grows from 20 to 25.** `tanakh` (its tripartite structure read on Sefaria,
  the tripartite attestation in the Prologue to Ben Sira), `torah` (the five books on
  Sefaria and Mishnah Avot 1:1), `justification` (Romans 3:28 / Galatians 2:16 / James
  2:24 and the Council of Trent Decree on Justification), `apostles` (the New Testament
  lists of the Twelve and the reconstitution in Acts 1), and `hawariyyun` (Q 3:52,
  5:111-112, 61:14) were verified against directly read primary texts, with the sources
  that carry their claims raised or added at `high`.
- **`maad`** gains a Qur'an source (Q 17:51, 75:3-4, 36:78-79, 22:5-7) at `high` for the
  resurrection core, and an internal confidence contradiction in its notes is fixed, but
  it stays `reviewed`: its distinctive content, the philosophers-versus-kalam dispute over
  bodily return, rests on sources not yet read.

### Notes
- PATCH release: status promotions and sourcing only, no new entities and no schema
  change. `schema_version` stays 0.5.0.

## [0.8.3] - 2026-07-19

Five more entries reach `verified`, and `iman` gains its primary sources while honestly
staying `reviewed`.

### Changed
- **`verified` grows from 15 to 20.** `trinity` (the Niceno-Constantinopolitan Creed and
  Matthew 28:19 / 2 Corinthians 13:14), `incarnation` (John 1:1-14 and the Chalcedonian
  Definition), `original-sin` (Romans 5:12-21 and the canons of the Second Council of
  Orange, 529), `qiyama` (Q 75:1-6, 22:7, 36:78-79), and `nubuwwa` (Q 16:36, 4:163-165,
  21:25, 2:285, 33:40) were verified against their load-bearing primary texts, read
  directly. Each gains the primary-source objects that carry the claims, rated `high` on
  the passages read.
- **`iman`** gains its two primary sources (the Hadith of Gabriel, Sahih Muslim 8, and
  Q 2:285) at `high` for the articles of faith, but stays `reviewed`: its distinctive
  content, the definitional dispute and the grave-sinner taxonomy, rests on
  heresiographical sources not yet read.

### Notes
- PATCH release: status promotions and sourcing only, no new entities and no schema
  change. `schema_version` stays 0.5.0.

## [0.8.2] - 2026-07-19

Six more entries reach `verified` after their load-bearing primary texts were read
directly.

### Changed
- **`verified` grows from 9 to 15.** `isa` and `maryam` (their Qur'anic portraits,
  including the crucifixion verse Q 4:157-158), `shirk` (Q 4:48 and 4:116), and `fitra`
  (Q 30:30 and the fitra hadith in al-Bukhari and Muslim) were verified against directly
  read scripture; `homoousios` (the Nicene Creed of 325) and `chalcedonian-definition`
  (the Definition of 451, its four adverbs and double homoousios) against the promulgated
  conciliar texts read in the open NPNF2-14 editions.
- `shirk` gains a Qur'an source (Q 4:48/4:116, previously cited only inline), and
  `homoousios` and `chalcedonian-definition` each gain a reader-open conciliar-text
  source, all rated `high` on the passages actually read.

### Notes
- PATCH release: status promotions and sourcing only, no new entities and no schema
  change. `schema_version` stays 0.5.0.

## [0.8.1] - 2026-07-19

Seven entries are promoted from `reviewed` to `verified` after their load-bearing
primary sources were read directly, line by line, and confirmed.

### Changed
- **The first `verified` promotions beyond the original two.** The cited primary
  sources of `tawrat`, `injil`, `ahl-al-kitab`, and `hanif` (their Qur'anic verses,
  read at quran.com), `new-testament-canon` (Athanasius's 39th Festal Letter listing
  the twenty-seven books), `nicene-creed` (the 381 creed text), and `theosis` (2 Peter
  1:4 and Athanasius, On the Incarnation 54) were read directly and confirmed by an
  independent second check. These move to `verified`, and their read sources carry
  honest `high` confidence. The dataset now has 9 `verified` entries, up from 2.
- `theosis` splits its bundled patristic and scriptural source into two separate,
  directly-read `high` sources. `khatam-al-nabiyyin` gains its previously missing
  Qur'anic source (Q 33:40, read directly) but stays `reviewed`, because its
  distinctive historical claim still rests on a paywalled study not yet read.

### Notes
- PATCH release: status promotions and sourcing only, no new entities and no schema
  change. `schema_version` stays 0.5.0.

## [0.8.0] - 2026-07-19

The Abrahamic scriptures and patriarchs are added and the Judaism tradition deepens,
closing the forward references the three traditions had opened onto one another.

### Added
- **The Abrahamic scriptures**: `tawrat` and `injil` (the Islamic conceptions of the
  scriptures given to Moses and Jesus) and `ahl-al-kitab` (the People of the Book),
  each framed strictly as the attributed Islamic category, and the Jewish `torah` (the
  Pentateuch), with `tawrat compares_with torah` and `injil compares_with
  new-testament-canon`.
- **The patriarchs and prophets as cross-tradition pairs**, following the
  jesus-of-nazareth/isa model (one entity per tradition, joined by compares_with):
  `abraham` (judaism) and `ibrahim` (islam), `moses` (judaism) and `musa` (islam). The
  disputed son of the binding (Isaac in Judaism, widely Ishmael in Islam) and the
  historicity debates are attributed, never adjudicated.
- **`rabbinic-judaism`**: the post-70 rabbinic movement, heir of the Pharisees and,
  alongside Christianity, one of the two heirs of Second Temple Judaism, the sibling
  side of the parting of the ways.

### Notes
- The dataset is now 174 entities: 111 Islamic, 55 Christian, 7 Jewish, and 1 in the
  philosophy namespace, 172 `reviewed` and 2 `verified`. The Judaism tradition grows
  from 3 to 7.
- MINOR release: it adds entities and closes forward references. No schema change, so
  `schema_version` stays 0.5.0.

## [0.7.0] - 2026-07-19

The origins of Christianity open in a neutral historian's register, resting on a new
Judaism tradition, the third Abrahamic tradition.

### Added
- **A `judaism` tradition** (ADR-0008), modeled like Islam and Christianity:
  `second-temple-judaism` and `pharisees` (schools) and the `tanakh` (the Hebrew Bible,
  a work). The `tradition` enum gains `judaism` in all five schemas, carrying
  `schema_version` from 0.4.0 to 0.5.0. It anchors Christian origins and gives the
  Islamic entries about Jewish scripture and figures a tradition to compare with.
- **The origins of Christianity** in a historian's register: `jesus-of-nazareth` (the
  historical Jesus, a first-century Galilean Jew), `paul-of-tarsus`, the
  `council-of-jerusalem` (c. 50 CE, an Event), the `parting-of-the-ways` (the gradual
  separation from Judaism), and the `new-testament-canon`. Historical-critical claims are
  attributed to scholarship and each faith's confessional claims to that faith, with
  neither adjudicated.
- **`jesus-of-nazareth compares_with isa`** (#10): the same figure read across
  Christianity, Judaism, and Islam (who he is and what happened to him, including the
  crucifixion, historically secure to most scholars but denied on the mainstream Islamic
  reading of Q 4:157-158), ranking no answer. Also `tanakh compares_with tawrat`.

### Notes
- The dataset is now 165 entities: 106 Islamic, 55 Christian, 3 Jewish, and 1 in the
  philosophy namespace, 163 `reviewed` and 2 `verified`.
- MINOR release. The enum gains `judaism` (additive, backward compatible), so
  `schema_version` moves 0.4.0 to 0.5.0 while existing entities remain valid.
- The historical-Jesus entry passed a strict sentence-by-sentence neutrality audit: it
  records the resurrection, divinity, and messiahship only as attributed confessions and
  takes no editorial position on them.

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
