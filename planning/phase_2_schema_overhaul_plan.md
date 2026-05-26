# Phase 2 plan — mapping schema overhaul (issue #30)

**Status:** plan; not yet started.
**Tracks:** [#30](https://github.com/Cellular-Semantics/evidencell/issues/30).
**Roadmap context:** [planning/map_cell_type_redesign_roadmap.md](./map_cell_type_redesign_roadmap.md) § 4.
**Created:** 2026-05-12.

## Context

Phase 1 (find_candidates Stage A redesign + AT-blind audit refactor)
landed via PR #49. Phase 2 restructures `MappingEdge` and related
enums for SSSOM alignment so curators can express finer mapping
semantics and downstream consumers can interoperate with the broader
mapping-tooling ecosystem.

The schema deltas were largely agreed in issue #30 + three amendment
comments. This plan resolves the small remaining open questions,
prescribes a two-PR migration (transient back-compat shim in PR1,
hard cutover in PR2), and lists exact edit points.

**Not in scope here:** `sssom_export.py` and SSSOM TSV emission — kept
as a follow-up (file separately as a content task or issue).

## Phase 0 — record decisions

Create `planning/phase_2_decisions_2026-05-12.md` capturing:

1. **Splits as N edges.** Existing KB already uses N edges per split
   (36 `TYPE_A_SPLITS` rows across `kb/graphs/**`). Stay with N edges
   per split; each carries `mapping_cardinality: 1:n`.
2. **`reconciliation_note` name retained.** Issue #30 listed
   alternatives (`confidence_basis`, `reviewer_synthesis`,
   `judgement_note`) but no strong preference; keep the proposed
   name as the conservative call.
3. **`confidence_score` is agent-emitted only.** No
   ordinal→numeric fallback when curator doesn't supply one (since
   no edge is "manually curated" in the strict sense; everything
   passes through an agent path). The Phase 3 report-time agent may
   eventually write `confidence_score` back alongside
   `rationale_source_hash`; that hand-off is flagged here, not
   implemented in Phase 2.
4. **Enum cleanup.** Final `MappingRelationship` set:
   `skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`,
   `skos:narrowMatch`, `evidencell:PartialOverlapMatch`,
   `evidencell:CrossCuttingMatch`, `evidencell:NoCorrespondence`.
   Drop `TYPE_A_SPLITS`, `TYPE_A_MERGES`, `CANDIDATE_SYNONYM`,
   `SUBSET`, `SUPERSET`, `OVERLAPS`, `UNCERTAIN` (relationship value;
   the `UNCERTAIN` value on `MappingConfidence` is a separate slot
   and stays).
5. **Enum values are CURIEs, not ALL_CAPS slugs.** Each
   permissible-value identifier IS its IRI binding —
   `skos:exactMatch` rather than `EXACT_MATCH` + `meaning:`. Same
   pattern applies to `MappingJustification` (semapv: prefix).
   `MappingCardinality` is the exception: its values are literal
   `1:1`/`1:n`/`n:1` strings (matches SSSOM's column convention; no
   upstream ontology to bind).
6. **`ADJACENT`/`DISTAL`/`PROXIMAL` are not Phase 2 concerns.** They
   appear on `CellTypeColocation.spatial_relationship` (a free-text
   string slot, range = no enum), not on `MappingEdge.relationship`.
   The original scoping survey grep folded them in. No action needed.
7. **`evidencell:` prefix URL.** Recommendation:
   `https://w3id.org/evidencell/` (PURL convention; matches OBO /
   SSSOM ecosystem practice). Flag for user ratification before PR1.

## PR1 — schema + src/ + hooks + tests (transient back-compat)

Goal: schema and code on the new shape; KB graphs still on the old
shape, kept valid by a small back-compat shim. CI green at the end of
PR1; KB sweep follows in PR2.

### Schema — `schema/celltype_mapping.yaml`

Header — add prefix block:

```yaml
prefixes:
  skos:       http://www.w3.org/2004/02/skos/core#
  semapv:     https://w3id.org/semapv/vocab/
  evidencell: https://w3id.org/evidencell/   # ratify in Phase 0
```

`MappingEdge` attributes (lines 1796–1850):

- Rename `type_a` → `lit_type`; `type_b` → `taxonomy_type`. Mark old
  slots `deprecated: true` so the schema still validates KB YAML that
  uses the old names during the PR1 → PR2 window.
- Add fields:
  - `mapping_cardinality` (range `MappingCardinality`)
  - `mapping_justification` (range `MappingJustification`)
  - `reconciliation_note` (string)
  - `reviewed_by` (string)
  - `confidence_score` (float, min 0.0, max 1.0)

`MappingRelationship` enum (lines 252–318):

- Permissible-value identifiers become CURIEs:
  - `skos:exactMatch` — direct one-to-one identity (high precision +
    high recall AT, convergent multi-source evidence).
  - `skos:closeMatch` — same-cell-type judgement under partial
    information (F1 ≈ 0.65–0.8); the conservative default for
    candidate-synonym-style cases per #30 amendment 1.
  - `skos:broadMatch` — lit_type is **narrower** than taxonomy_type.
    Self-disambiguating description per #30 cmt 3:
    > Read `lit_OLM --skos:broadMatch--> Sst_Gaba_3_supertype` as
    > "OLM has a broad match — the supertype is the broader thing".
    > Pair with `mapping_cardinality: 1:1` when a specific cluster
    > is suspected to equal the lit_type but cannot yet be
    > identified; with `1:n` when the lit_type genuinely subsumes
    > multiple taxonomy_types within the broader node.
  - `skos:narrowMatch` — lit_type is **broader** than taxonomy_type.
    Symmetric description.
  - `evidencell:PartialOverlapMatch` — genuinely incomplete overlap;
    precision OR recall below ~0.65, partial-set semantics.
  - `evidencell:CrossCuttingMatch` — orthogonal partition (no SKOS
    equivalent).
  - `evidencell:NoCorrespondence` — explicitly does not map (no SKOS
    equivalent).
- Drop: `TYPE_A_SPLITS`, `TYPE_A_MERGES`, `CANDIDATE_SYNONYM`,
  `SUBSET`, `SUPERSET`, `OVERLAPS`, `UNCERTAIN`.

New enum `MappingCardinality`:

```yaml
MappingCardinality:
  permissible_values:
    "1:1":  {description: One source maps to one target.}
    "1:n":  {description: One source splits across multiple targets.}
    "n:1":  {description: Multiple sources collapse onto one target.}
```

New enum `MappingJustification` (semapv subset):

```yaml
MappingJustification:
  permissible_values:
    semapv:ManualMappingCuration:        {description: Reviewed by a curator.}
    semapv:UnreviewedManualMapping:      {description: Agent-emitted, not yet curator-reviewed.}
    semapv:LexicalMatching:              {description: Name-based match.}
    semapv:CompositeMatching:            {description: Multi-source evidence-driven match.}
    semapv:LogicalReasoning:             {description: Match derived by logical reasoning.}
    semapv:UnspecifiedMatching:          {description: Provenance not recorded.}
```

### src/ — back-compat shim

New `src/evidencell/_mapping_compat.py`:

- `read_edge_endpoint(edge: dict, end: Literal["lit", "tax"]) -> str` —
  returns `edge["lit_type"]` or `edge["type_a"]`; emits a single
  DeprecationWarning per process if old name found.
- `read_edge_relationship(edge: dict) -> str | None` — passes through.
- Used by the five src modules that touch these fields.

Modules touched (all read via the shim):

| Module | refs |
|---|---|
| `src/evidencell/render.py` | 28 (incl. 2 enum display strings) |
| `src/evidencell/validation/at_blind.py` | 12 |
| `src/evidencell/at_f1_attribution.py` | 9 |
| `src/evidencell/toc.py` | 4 |
| `src/evidencell/validate.py` | 2 |

`render.py` also remaps the legacy display strings:
`TYPE_A_SPLITS · MODERATE` → `skos:broadMatch (1:n) · MODERATE` (or a
glossier short form if curator-facing prose matters more than the
direct CURIE; decide alongside the docs glossary).

### Hook — `.claude/hooks/validate_mapping_hook.py`

Dangling-edge resolver accepts both `type_a`/`type_b` and
`lit_type`/`taxonomy_type` for the PR1 → PR2 window. PR2 drops the
old branch.

### Tests

- Update fixtures in `tests/test_validate.py`, `tests/test_toc.py`,
  `tests/test_render.py`, `tests/test_at_f1_attribution.py`,
  `tests/test_validation/test_at_blind_audit.py` to use new field
  names and new CURIE relationship values.
- New `tests/test_mapping_compat.py`: one fixture uses old field
  names + old enum values; assert shim normalises correctly. PR2
  inverts these assertions.

### Docs

- `workflows/map-cell-type.md` (lines 325, 375) — update field /
  enum references.
- New `docs/mapping_schema_2026-05-12.md` — glossary preamble
  covering the SKOS direction convention (per #30 cmt 3), the
  CURIE-as-value convention, a worked `skos:broadMatch + 1:1` vs
  `skos:broadMatch + 1:n` example, and a cardinality interaction
  table. Datestamped so future refreshes can co-exist.

## PR2 — KB sweep + back-compat removal

Goal: rewrite every KB edge into the new shape; remove the shim.

### KB sweep — `kb/graphs/**` (11 files, 137 edges)

Single ruamel.yaml round-trip script (analogous to Phase 1's
`/tmp/sweep_best_at_fields.py`). Remap rules:

| Old field / value | New |
|---|---|
| `type_a` | `lit_type` |
| `type_b` | `taxonomy_type` |
| `relationship: EQUIVALENT` | `relationship: skos:exactMatch` |
| `relationship: TYPE_A_SPLITS` (36 edges) | `relationship: skos:broadMatch` + `mapping_cardinality: 1:n` |
| `relationship: OVERLAPS` | `relationship: skos:closeMatch` |
| `relationship: SUBSET` | `relationship: skos:broadMatch` + `mapping_cardinality: 1:1` |
| `relationship: SUPERSET` | `relationship: skos:narrowMatch` + `mapping_cardinality: n:1` |
| `relationship: UNCERTAIN` | drop relationship; set `mapping_justification: semapv:UnspecifiedMatching` |
| `relationship: CROSS_CUTTING` | `relationship: evidencell:CrossCuttingMatch` |
| `relationship: PARTIAL_OVERLAP` | `relationship: evidencell:PartialOverlapMatch` |
| `relationship: NO_CORRESPONDENCE` | `relationship: evidencell:NoCorrespondence` |

Default `mapping_justification: semapv:ManualMappingCuration` on
edges without an explicit value (curator-touched by definition).

### Back-compat removal

- Delete `src/evidencell/_mapping_compat.py`.
- Strip fallback branches from the 5 src modules.
- Drop deprecated aliases from `MappingEdge` in the schema.
- Hook drops the old-name branch.
- Invert `tests/test_mapping_compat.py`: old field names + old enum
  values now must error against the schema.

## Critical files to modify

| Path | PR1 | PR2 |
|---|---|---|
| `schema/celltype_mapping.yaml` | prefix block; CURIE enum values; deprecated `type_a`/`type_b` aliases; new slots + enums | drop deprecated aliases |
| `src/evidencell/_mapping_compat.py` | **new** | **delete** |
| `src/evidencell/render.py` | route reads through shim; remap display strings | strip shim |
| `src/evidencell/{toc,validate,validation/at_blind,at_f1_attribution}.py` | shim reads | strip shim |
| `.claude/hooks/validate_mapping_hook.py` | dual-name accept | single-name |
| `kb/graphs/**` (11 files) | — | sweep |
| `tests/test_{validate,toc,render,at_f1_attribution,kb_examples}.py` | fixture renames + CURIE values | — |
| `tests/test_mapping_compat.py` | **new**; assert shim works | invert assertions |
| `workflows/map-cell-type.md` | field/enum names | — |
| `docs/mapping_schema_2026-05-12.md` | **new** glossary | — |
| `planning/phase_2_decisions_2026-05-12.md` | **new** decision log | — |

## Verification

**PR1.**

1. `uv run pytest tests/ --no-cov` — green, including new
   `test_mapping_compat`.
2. `just validate-all` — current KB still passes (shim plus
   deprecated aliases accept old names against new schema).
3. `just validate-at-blind` — pass rate unchanged from current
   baseline (renames are read-side only).
4. Spot-render a report; `skos:broadMatch (1:n) · MODERATE` (or
   chosen glossier form) renders correctly.

**PR2.**

1. `uv run pytest tests/` — green; `test_mapping_compat` now asserts
   old field names + old enum values are rejected.
2. `just validate-all` — every KB graph passes LinkML under the
   post-sweep schema.
3. `just validate-at-blind` — pass rate doesn't regress (renames +
   enum remaps preserve audit semantics).
4. `git grep -E '\btype_a\b|\btype_b\b|TYPE_A_SPLITS|TYPE_A_MERGES|CANDIDATE_SYNONYM|\bSUBSET\b|\bSUPERSET\b|relationship:\s*OVERLAPS\b'` — zero hits.

## Out of scope / deferred

- `sssom_export.py` and SSSOM TSV emission — file separately.
- HIGH/MODERATE/LOW/UNCERTAIN binning thresholds for `confidence`
  (separate decision per #30; data-driven).
- TOC glossary integration of `lit_type` / `taxonomy_type` — trivial
  follow-up after the rename lands.
- Phase 3 fields (`rationale`, `report_path`, `rationale_generated_at`,
  `rationale_source_hash`). Phase 3 may also extend who writes
  `confidence_score`; flagged here as the Phase 3 hand-off.
- Phase 4 (joint heterogeneity → splitting). Phase 4 depends on the
  `skos:broadMatch + 1:n` predicate landing here; otherwise no Phase
  2 impact.
