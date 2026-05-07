# Validation hook + LinkML target_class dispatch — tidy-ups

**Date:** 2026-04-28
**Severity:** Low — current state works for the new bulk-correlation content; these are quality follow-ups.

---

## Context

Adding `BulkDataset` and `CorrelationRun` as new top-level KB document types required the validation hook to dispatch `target_class` by file path rather than hard-coding `CellTypeMappingGraph`. That landed in commit 15b8e5b (`validate: dispatch linkml target_class by KB file path`).

The minimal dispatch table in `src/evidencell/validate.py:_target_class_for_kb_path` now covers:

| Path pattern | target_class |
|---|---|
| `kb/datasets/*.yaml` | `BulkDataset` |
| `kb/correlation_runs/*/manifest.yaml` | `CorrelationRun` |
| `kb/correlation_runs/*/<other>.yaml` | None (skipped) |
| `kb/taxonomy/*/cluster.yaml`, `supertype.yaml`, `subclass.yaml`, `class.yaml`, `neurotransmitter.yaml` | `TaxonomyNodeList` |
| `kb/taxonomy/*/taxonomy_meta.yaml` | None (skipped — no schema class) |
| `kb/draft/{region}/*.yaml`, `kb/mappings/{region}/*.yaml`, anything else under `kb/` | `CellTypeMappingGraph` (default) |

This works but exposes three rough edges worth tidying.

---

## File-location reference (current state)

For ease of reference, here is where each kind of validated file lives, what schema class it maps to, and what hook checks apply:

### KB YAML — `kb/**/*.yaml`

| Location | Class | Reference / quote_key check | Notes |
|---|---|:---:|---|
| `kb/draft/{region}/*.yaml` | `CellTypeMappingGraph` | yes (`references/{region}/references.json`) | classical + atlas nodes + mapping edges |
| `kb/mappings/{region}/*.yaml` | `CellTypeMappingGraph` | yes (`references/{region}/references.json`) | graduated mapping graphs |
| `kb/taxonomy/{taxonomy_id}/cluster.yaml` | `TaxonomyNodeList` | n/a | atlas leaf nodes |
| `kb/taxonomy/{taxonomy_id}/supertype.yaml` | `TaxonomyNodeList` | n/a | |
| `kb/taxonomy/{taxonomy_id}/subclass.yaml` | `TaxonomyNodeList` | n/a | |
| `kb/taxonomy/{taxonomy_id}/class.yaml` | `TaxonomyNodeList` | n/a | |
| `kb/taxonomy/{taxonomy_id}/neurotransmitter.yaml` | `TaxonomyNodeList` | n/a | orthogonal annotation level |
| `kb/taxonomy/{taxonomy_id}/taxonomy_meta.yaml` | **none — skipped** | n/a | level_hierarchy, mapmycells block, ingest metadata |
| `kb/datasets/*.yaml` | `BulkDataset` | n/a | one YAML per published bulk dataset |
| `kb/correlation_runs/{run_id}/manifest.yaml` | `CorrelationRun` | n/a | one manifest per correlation analysis |
| `kb/correlation_runs/{run_id}/<other>.yaml` | **none — skipped** | n/a | reserved for future structured outputs |

### Reports — `reports/**/*.md`

| Location | Checks |
|---|---|
| `reports/{region}/*.md` | blockquote attribution annotation, quote_key existence in `references/{region}/references.json`, ontology CURIEs, atlas accessions, PMIDs |

### Out-of-scope-in-curation-mode

These paths are blocked by the curation-mode hook (writes rejected unless dev-mode is loaded):

- `src/`, `schema/`, `.claude/`, `workflows/`, `justfile`

### Inputs not validated

- `inputs/deepsearch/*.pdf` — ASTA reports
- `inputs/taxonomies/*.{json,csv,tsv,cypher}` — taxonomy ingest sources
- `references/{region}/references.json` — reference store (validated separately by ingest path; not by the hook)
- `references_cache/**` — cached snippets
- `research/{region}/**` — research artefacts (will be promoted to `kb/correlation_runs/` for bulk-correlation runs as part of this work)
- `conf/**` — runtime configuration (gitignored caches, MBA ontology, gene mappings)
- `planning/**` — planning notes, dev requests, content notes

---

## Tidy-ups to implement

### 1. Add `TaxonomyMeta` LinkML class

`kb/taxonomy/{id}/taxonomy_meta.yaml` is real structured KB content but currently has no schema class — validation is silently skipped. Define `TaxonomyMeta` with the existing fields: `taxonomy_id`, `taxonomy_name`, `species_id`, `species_label`, `tissue_id`, `tissue_label`, `anatomy_ontology`, `source_query`, `source_file`, `ingest_date`, `level_hierarchy[*]`, `level_counts`, `mapmycells` (sub-object with stats_s3_url, markers_s3_url, at_taxonomy_id), and a future `external_resources` block (see the separate Ensembl-mapping dev-request for the latter).

Add `(name="taxonomy_meta.yaml") → "TaxonomyMeta"` to the dispatch table. Backfill the existing two `taxonomy_meta.yaml` files to confirm they pass.

### 2. Dispatch table → declarative registry

Currently the dispatch is a 5-line if/elif in `_target_class_for_kb_path`. As content types accumulate (`BulkDataset`, `CorrelationRun`, `TaxonomyMeta`, future skill-specific record types) this will balloon. Cleaner: store the table as a side-config (e.g. `schema/file_routing.yaml`) keyed by glob pattern → target_class, and load it once at hook start.

Example surface:
```yaml
# schema/file_routing.yaml
routes:
  - pattern: kb/datasets/*.yaml
    target_class: BulkDataset
  - pattern: kb/correlation_runs/*/manifest.yaml
    target_class: CorrelationRun
  - pattern: kb/taxonomy/*/cluster.yaml
    target_class: TaxonomyNodeList
  # ...
  - pattern: kb/**
    target_class: CellTypeMappingGraph     # fallback
```

Adding a new content type then becomes a single-line config change rather than a code change.

### 3. Path-aware reference checks

The hook's `references.json` check assumes the file is `kb/draft/{region}/*.yaml` and reads `references/{region}/references.json`. For `kb/datasets/*.yaml` and `kb/correlation_runs/*/manifest.yaml` this assumption doesn't hold — but the check is currently still fired. Either:

- Make the check path-aware (match only the existing kb/draft and kb/mappings patterns), OR
- Treat datasets and correlation runs as "no region" content and skip the check explicitly.

A clean implementation gates the check the same way as schema dispatch: the dispatch table can carry a `requires_region_refs: bool` flag. If false, skip the references.json lookup.

### 4. (Optional) consolidate `_CURATION_BLOCKED_ZONES` with the dispatch table

The curation-mode block list (`src`, `schema`, `.claude`, `workflows`, `justfile`) lives in the hook; the dispatch table lives in `validate.py`. Both are answers to the same question — *what does the hook do for files at this path?* — and would be cleaner as one declarative spec.

---

## Verification

For each tidy-up:
- Round-trip the existing taxonomy_meta files; confirm they validate against the new `TaxonomyMeta` class
- Test a path-mismatch in the registry (e.g. a `kb/datasets/foo.yaml` where the YAML has `record_type: CorrelationRun`) — should fail with a clear error
- Confirm `references.json` check is not fired for `kb/datasets/` or `kb/correlation_runs/` writes
