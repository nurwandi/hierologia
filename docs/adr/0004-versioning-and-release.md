# ADR-0004: Versioning and release

- **Status:** Accepted
- **Date:** 2026-07-19

## Context

Two different things need versioning and they are easy to conflate:

1. The **data contract** (the shape of each JSON entity, i.e. the API payload).
2. The **dataset content** (which entities exist and what they say), which
   scholars need to cite as a stable, dated snapshot.

We also deploy in two different senses: a live always-latest demo, and stable
citable releases.

## Decision

### Two version axes, kept separate

- **`schema_version`** (per entity, SemVer): versions the *contract*. Bump it
  when a schema changes. A breaking change (removing or renaming a field,
  tightening a constraint) is a MAJOR bump; an additive field is MINOR. A dataset
  release may keep an older `schema_version` while its content version moves on.
- **Dataset version** (the repository release, SemVer, git tag `vX.Y.Z`): versions
  the *content*.
  - **MAJOR** breaking: a schema change that breaks consumers, or the removal or
    rename of an already-published entity `id`.
  - **MINOR** additive: new entities, a new tradition, backward-compatible schema
    fields.
  - **PATCH**: content fixes, source corrections, status promotions
    (`draft -> reviewed -> verified`), typos. No structural change.

### Two deploy tracks

- **Continuous (demo / read-only API):** every push to `main` deploys the latest
  state to GitHub Pages via `.github/workflows/pages.yml`. This is the preview
  endpoint; it is not a citable version.
- **Versioned releases (dataset):** a git tag `vX.Y.Z` triggers
  `.github/workflows/release.yml`, which validates the data, packages a snapshot
  (`data/` + `schema/` + `CITATION.cff` + `LICENSE`), and creates a GitHub
  Release. A release is the stable, dated, citable snapshot. A DOI (Zenodo) is
  minted per release once that integration is set up.

### Release process

1. Work happens on `main` (which continuously deploys the demo).
2. At a milestone, cut a release:
   - if the scope changed (for example a new tradition), refresh the description
     and keywords in `.zenodo.json`, `README.md`, and `CITATION.cff` first;
     Zenodo re-reads `.zenodo.json` at each release, and the concept DOI surfaces
     the latest version's metadata (older version records stay frozen, which is
     correct: each snapshot is honest about what it contained);
   - move the `CHANGELOG.md` `[Unreleased]` section to `[X.Y.Z] - DATE`;
   - set `version` and `date-released` in `CITATION.cff`;
   - `git tag vX.Y.Z` and push the tag.
3. `release.yml` builds the artifact and publishes the GitHub Release.

A release may contain entities at any editorial status; each entity carries its
own `status`, so a snapshot is honest about what is `reviewed` versus `draft`.

## Consequences

- Citations point at a tag, never at `main`.
- `github-pages` is the current "production" environment shown in the GitHub UI;
  when a dynamic AWS API is added (via HCP Terraform), it becomes a separate
  `production` environment, and this same two-track model still applies.
- Pushing workflow files requires the `workflow` OAuth scope on the pushing
  account.
