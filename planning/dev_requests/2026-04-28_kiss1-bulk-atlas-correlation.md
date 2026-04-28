# Dev request: Bulk RNA-seq → atlas cluster correlation analysis (Kiss1 case)

**Date:** 2026-04-28
**Blocked step:** none yet — this is a one-off analysis, requested by curator
**Severity:** Low — exploratory; outcome decides whether to promote to a generic skill

---

## What this is

A one-off analysis correlating bulk RNA-seq expression vectors from
[Stephens et al. 2024 (PMID 37934722)](https://pubmed.ncbi.nlm.nih.gov/37934722/)
against WMBv1 cluster pseudobulks, to refine the
`avpv_kiss1_neuron` and (eventually) ARC Kiss1 mapping edges.

Input data: `Reproduction` 167(1) supplementary table 3 — a 4,724-gene normalised
log2 expression matrix with two columns (RP3V, ARC) representing pools of 10–15
FACS-sorted Kiss1 neurons from each region. Ensembl-keyed, directly
compatible with WMBv1's `precomputed_stats.h5` `col_names`.

## Why it matters

The current `avpv_kiss1_neuron → CS20230722_CLUS_1915` edge sits at MODERATE
confidence on `ATLAS_METADATA` evidence only (Kiss1 mean=2.51, Th=6.6,
MFR=0.02 — strong qualitative match, no quantitative cross-dataset signal).
A high Spearman ρ between the bulk RP3V profile and the CLUS_1915 pseudobulk
would be direct quantitative evidence, eligible to upgrade confidence
toward HIGH or document a discrepancy if the top hit is elsewhere.

## What the analysis does

1. Load supp table 3 → (RP3V, ARC) log2 vectors per Ensembl ID
2. Load `precomputed_stats.h5` (`sum`, `n_cells`, `col_names`, `cluster_to_row`)
3. Compute per-cluster mean log-expression: `log1p(sum / n_cells)` (or
   appropriate normalisation — see "open questions")
4. Restrict to genes present in both: bulk supp ∩ atlas `col_names`
5. For each of 5,322 clusters: compute Spearman ρ (a) vs RP3V vector,
   (b) vs ARC vector
6. Output ranked tables — top 20 clusters per bulk sample, with
   metadata (supertype, primary soma region, MFR)
7. Specifically report rank of CLUS_1915 (predicted AVPV match) and
   ARC-region clusters (predicted ARC Kiss1 match)

## Where it lives

`research/sexually_dimorphic/20260428_kiss1_bulk_correlation/`:
- `README.md` — analysis summary, top hits, interpretation
- `correlate.py` — script (one-off; not promoted to `src/`)
- `bulk_supp_table.csv` — copy of the supp table for reproducibility
- `correlations_rp3v.tsv`, `correlations_arc.tsv` — full ranked output
- `top_hits.md` — human-readable summary

## Open questions

1. **Normalisation alignment.** Bulk supp values are log2-scale, range ~0–14;
   atlas `sum` is raw counts. Should we use log1p(CPM) for the atlas, log1p(raw),
   or simply rank-transform both before correlation (Spearman handles this
   naturally — likely the safest default).
2. **Gene set restriction.** Should we restrict to highly variable genes across
   the atlas to avoid correlation being dominated by housekeeping? Initial pass:
   no restriction. Sensitivity analysis if results are flat.
3. **MERFISH vs 10x reference.** WMBv1 has both. Precomputed stats file is
   the 10x reference (per filename `precomputed_stats_ABC_revision_230821.h5`).
   This is the right substrate for bulk correlation — MERFISH only profiles
   ~500 genes.

## Promotion to skill (decision after this run)

If results clearly identify CLUS_1915 (or its supertype SUPT_0486) as a top-3
hit for RP3V, the bulk-correlation pattern is worth promoting to a generic
skill `bulk-atlas-correlate` with a `BulkCorrelationEvidence` evidence type.
If results are noisy or top hits don't align with prior expectations, the
method needs refinement before generalisation.

## Surface (if promoted)

| Component | Form |
|---|---|
| Skill | `.claude/skills/bulk-atlas-correlate/SKILL.md` |
| Schema | `BulkCorrelationEvidence(target_node_id, source_dataset_id, spearman_rho, n_genes_overlapping, normalisation, sample_label)` on MappingEdge |
| `map-cell-type.md` | Step that surfaces existing BulkCorrelationEvidence in refinement subagent |
| Justfile | `just bulk-correlate {bulk_csv} {taxonomy_id}` |

This is intentionally **deferred** — do not implement until the Kiss1 run validates the approach.
