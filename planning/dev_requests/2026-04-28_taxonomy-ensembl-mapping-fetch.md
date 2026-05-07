# Dev request: Track Ensembl ↔ symbol mapping as a taxonomy artefact with provenance

**Date:** 2026-04-28
**Blocked step:** none currently — this is infrastructure work
**Severity:** Low — affects reproducibility and future use cases (bulk dataset alignment, gene-symbol normalisation in reports)

---

## What is missing

`conf/gene_mapping_CCN20230722.tsv` exists (31,714 rows, ensembl_id↔symbol) and is consumed by `just add-expression`, but it has no provenance:

- The source URL is not recorded anywhere
- `kb/taxonomy/CCN20230722/taxonomy_meta.yaml` has a `mapmycells` block with the precomputed stats and markers S3 URLs, but no analogue for the gene mapping
- There's no `just fetch-` or `just refresh-` target for it
- Row count differs from the canonical source (32,284 — see below), so the local file may be stale

**Canonical source:** `https://raw.githubusercontent.com/Cellular-Semantics/whole_mouse_brain_ontology/refs/heads/main/src/templates/CCN_ensmusg.tsv` — ROBOT template format with 32,286 rows (2 header rows + 32,284 data rows).

This is a generic taxonomy artefact: every taxonomy ingest will eventually need an Ensembl↔symbol mapping for bulk dataset alignment, supplementary-table integration, and cross-taxonomy gene normalisation.

## What needs to change

### Schema

Add an `external_resources` block to `TaxonomyMeta` (mirrors the existing `mapmycells` block):

```yaml
# kb/taxonomy/CCN20230722/taxonomy_meta.yaml
external_resources:
  ensembl_gene_mapping:
    url: https://raw.githubusercontent.com/Cellular-Semantics/whole_mouse_brain_ontology/refs/heads/main/src/templates/CCN_ensmusg.tsv
    local_cache: conf/gene_mapping_CCN20230722.tsv
    format: robot_template  # 2 header rows; ID/TYPE/NAME columns; "ensembl:" prefix on IDs; " (Mmus)" suffix on symbols
    fetched_date: 2026-04-28  # set by fetch command
```

### Justfile target

```
just fetch-gene-mapping {taxonomy_id}
```

- Reads `external_resources.ensembl_gene_mapping.url` from `taxonomy_meta.yaml`
- Downloads to `external_resources.ensembl_gene_mapping.local_cache`
- Parses ROBOT template (drop first 2 header rows; strip `ensembl:` prefix; strip ` (Mmus)` suffix)
- Writes a clean `ensembl_id<TAB>symbol` TSV (matches current `gene_mapping_CCN20230722.tsv` format)
- Updates `fetched_date` in `taxonomy_meta.yaml`
- Gitignored at the cache path (verify `.gitignore` already excludes `conf/gene_mapping_*.tsv`)

### Backfill

Set `external_resources.ensembl_gene_mapping` on:
- `kb/taxonomy/CCN20230722/taxonomy_meta.yaml`
- `kb/taxonomy/CS202106160/taxonomy_meta.yaml` (if a parallel HMBA gene mapping exists)

Run `just fetch-gene-mapping CCN20230722` to confirm the URL produces a file matching the existing `conf/gene_mapping_CCN20230722.tsv` after parsing — investigate the 570-row difference (32,284 canonical vs 31,714 local).

## What was tried

- Verified URL fetches cleanly: 32,286 rows of `ensembl:ENSMUSGxxx<TAB>SO:0000704<TAB>Symbol (Mmus)`
- Confirmed atlas HDF5 (`precomputed_stats.h5`) uses bare Ensembl IDs in `col_names`, so this mapping is the canonical bridge between bulk-RNA datasets (Ensembl-keyed) and the atlas (also Ensembl-keyed for column indexing) and the human-readable symbols used in reports/literature.

## Proposed surface

| File | Change |
|---|---|
| `schema/taxonomy_meta.yaml` (or wherever TaxonomyMeta lives) | Add `external_resources.ensembl_gene_mapping` block with `url`, `local_cache`, `format`, `fetched_date` |
| `justfile` | Add `fetch-gene-mapping` recipe |
| `src/evidencell/taxonomy_ops.py` (or new `taxonomy_fetch.py`) | Implement parser for ROBOT template → clean TSV |
| `kb/taxonomy/CCN20230722/taxonomy_meta.yaml` | Backfill the `external_resources` block |
| `.gitignore` | Verify `conf/gene_mapping_*.tsv` is excluded |
