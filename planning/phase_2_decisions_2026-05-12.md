# Phase 2 decisions — mapping schema overhaul

**Date:** 2026-05-12
**Tracks:** [#30](https://github.com/Cellular-Semantics/evidencell/issues/30)
**Plan:** [phase_2_schema_overhaul_plan.md](phase_2_schema_overhaul_plan.md)

Resolutions of the small open questions remaining after issue #30 +
its three amendment comments. Captured here so the PR1 + PR2 commits
can cite this doc.

---

## 1. Splits as N edges, not one edge with N targets

Existing KB already encodes splits as N edges per split (36
`TYPE_A_SPLITS` rows across `kb/graphs/**`). Continue with N edges.
Each carries `mapping_cardinality: 1:n` so consumers can group by
`(lit_type, mapping_cardinality=1:n)` to recover the split-as-set.

## 2. `reconciliation_note` name retained

Issue #30 listed alternatives (`confidence_basis`,
`reviewer_synthesis`, `judgement_note`). No strong preference among
them. Keeping the proposed name as the conservative call.

## 3. `confidence_score` is agent-emitted only

No edge in this KB is "manually curated" in the strict sense —
everything passes through an agent path. There is no ordinal →
numeric fallback at any point. Curator review may *change*
`confidence` (ordinal) but does not back-fill `confidence_score`
(numeric) from the ordinal.

The Phase 3 report-time agent may write `confidence_score` back to
each edge alongside `rationale_source_hash`. Flagged here as the
Phase 3 hand-off, not implemented in Phase 2. Issue
[#57](https://github.com/Cellular-Semantics/evidencell/issues/57)
tracks the ordinal ↔ numeric binding decision separately.

## 4. Final MappingRelationship value set

Permissible values after Phase 2:

| Value | SKOS / IRI | Meaning |
|---|---|---|
| `skos:exactMatch` | skos | one-to-one identity (convergent evidence) |
| `skos:closeMatch` | skos | same-type judgement under partial information (conservative default for candidate-synonym cases) |
| `skos:broadMatch` | skos | lit_type is **narrower** than taxonomy_type |
| `skos:narrowMatch` | skos | lit_type is **broader** than taxonomy_type |
| `evidencell:PartialOverlapMatch` | custom | genuinely incomplete overlap |
| `evidencell:CrossCuttingMatch` | custom | orthogonal partition |
| `evidencell:NoCorrespondence` | custom | explicitly does not map |

Dropped: `TYPE_A_SPLITS`, `TYPE_A_MERGES`, `CANDIDATE_SYNONYM`,
`SUBSET`, `SUPERSET`, `OVERLAPS`, `UNCERTAIN` (as a relationship
value; `UNCERTAIN` on `MappingConfidence` is a separate slot and
stays).

## 5. Enum values are CURIEs, not ALL_CAPS slugs

Permissible-value identifiers are the CURIE itself (e.g.
`skos:exactMatch`), not `EXACT_MATCH` + `meaning: skos:exactMatch`.
Rationale:

- KB YAML is self-disambiguating; the value tells you what the
  predicate is without consulting the schema.
- SSSOM export (deferred to #56) becomes 1:1 — the predicate column
  emits the value verbatim.
- LinkML supports CURIE-style identifiers in `permissible_values`;
  Python codegen is slightly awkward (`MappingRelationship["skos:exactMatch"]`)
  but evidencell's src/ mostly does string comparisons, not enum-
  constant access.

The same convention applies to `MappingJustification`
(`semapv:ManualMappingCuration` etc.).

**Exception: `MappingCardinality`** stays string-literal (`1:1`,
`1:n`, `n:1`). SSSOM itself stores these as strings; no upstream
ontology to bind to.

## 6. ADJACENT / DISTAL / PROXIMAL — not Phase 2 concerns

The original Phase 2 scoping survey flagged these as `relationship:`
values in KB. They are actually values of
`CellTypeColocation.spatial_relationship` (a free-text string slot —
range = description-suggested values; no enum). Schema validation
permits them because the slot accepts any string.

No action in Phase 2. Long-term: consider promoting
`spatial_relationship` to a typed enum, but that's orthogonal to
mapping semantics.

## 7. Prefix URLs

Schema header `prefixes:` block:

```yaml
prefixes:
  skos:       http://www.w3.org/2004/02/skos/core#
  semapv:     https://w3id.org/semapv/vocab/
  evidencell: https://w3id.org/evidencell/
```

The `skos:` and `semapv:` URLs are the canonical ones used across
the OBO / SSSOM ecosystem.

`evidencell:` is anchored at `https://w3id.org/evidencell/` —
PURL pattern, fits OBO / SSSOM conventions, allows future
redirection without breaking IRIs in older exports. The URL does
not have to resolve to live content immediately; we own the
namespace conceptually and can wire up a w3id redirect later.

**Pending ratification by maintainer** before the schema header
lands in PR1. If a different anchor is preferred (e.g.
`https://cellular-semantics.org/evidencell/`), substitute and
update this section.

---

## Source documents

- [Issue #30](https://github.com/Cellular-Semantics/evidencell/issues/30) — Mapping schema design discussion.
- [planning/phase_2_schema_overhaul_plan.md](phase_2_schema_overhaul_plan.md) — implementation plan.
- [planning/map_cell_type_redesign_roadmap.md](map_cell_type_redesign_roadmap.md) § 4 — roadmap entry.
