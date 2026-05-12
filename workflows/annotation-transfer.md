# Annotation Transfer Feedback Orchestrator

> **STATUS: Pipeline implemented; KB import orchestrator pending**
> The `annotation_transfer/` proto-repo provides dataset retrieval, MapMyCells
> mapping, and F1 scoring. The orchestrator steps below for importing results
> into the KB are not yet automated.

---

## Purpose

Closes the experimental feedback loop. Annotation transfer experiments proposed
in gen-report output (MapMyCells, Seurat label transfer, scANVI) return results that
are imported as `AnnotationTransferEvidence` items, potentially upgrading mapping
confidence from MODERATE to HIGH.

---

## Pipeline tools (`annotation_transfer/`)

The annotation transfer proto-repo provides three stages:

| Stage | Tool | Description |
|-------|------|-------------|
| **Preflight** | `just at-preflight FILE` | Estimate memory, gate large datasets |
| **Convert** | `just at-convert INPUT OUTPUT [--cluster-col COL]` | Sanitise h5ad for MapMyCells (raw counts, sparse CSR, minimal obs/var) |
| **Map** | `just at-map INPUT TAXONOMY OUTPUT_DIR` | Run MapMyCells via web API or local (auto-resolved) |
| **Map (local)** | `just at-map-local INPUT STATS MARKERS OUTPUT_JSON` | Run MapMyCells locally (requires `cell_type_mapper`) |
| **Subsample** | `just at-subsample INPUT OUTPUT [--stratify-col COL]` | Stratified subsample for web API limits (150K cells / 2GB) |
| **Score** | `just at-score MMC_CSV LABELS OUTPUT` | Compute F1 matrix from MapMyCells CSV + source labels |
| **Taxonomy setup** | `just at-taxonomy-setup TAXONOMY_ID` | Configure backend preference for a taxonomy |

For dataset retrieval from heterogeneous sources, use the **retrieve_dataset** skill
(`.claude/skills/retrieve_dataset.md`), which handles format detection, R conversion,
annotation inspection, and the preflight gate.

MapMyCells mapping uses the BKP GraphQL API by default (no local install needed).
For local execution, install `cell_type_mapper` and download taxonomy files:

```
just at-download-taxonomy CCN20230722
```

This downloads stats + marker files to `conf/mapmycells/{taxonomy_id}/` (gitignored,
re-fetchable), updates the AT taxonomy spec with absolute local paths, and syncs
relative paths into `kb/taxonomy/{taxonomy_id}/taxonomy_meta.yaml`.

---

## Steps

```
Step 0  Dataset retrieval
        Use .claude/skills/retrieve_dataset.md to obtain and convert the source
        dataset to MapMyCells-ready h5ad + source labels JSON.
        [GATE] Human confirms annotation column and any cell subset filters.

Step 0.5 Backend resolution + subsample
        Load taxonomy spec; check preferred backend.
        If web backend and dataset >150K cells:
          annotation-transfer subsample <input.h5ad> <subsampled.h5ad> --stratify-col <label_col>
        [GATE] Human confirms subsampling strategy or switches to local.

Step 1  Run MapMyCells
        annotation-transfer map <input.h5ad> CCN20230722 <output_dir/> --backend auto
        Uses taxonomy's preferred backend. Override with --backend web|local.
        For explicit local: annotation-transfer map-local <input.h5ad> <stats> <markers> <output.json>

Step 2  Score
        annotation-transfer score <mmc_output.csv> <labels.json> <f1_matrix.csv>
        Produces: F1 matrix CSV + best-mappings summary.
        [GATE] Human reviews F1 matrix, confirms results are sensible.

Step 3  Parse results (PENDING — not yet automated)
        Extracts per-taxonomy-level F1, purity, n_cells from the scoring output.
        Maps results to KB node IDs.
        Produces: proposed AnnotationTransferEvidence YAML block.

Step 4  Append to KB
        AnnotationTransferEvidence appended to relevant MappingEdge.

Step 5  Confidence re-assessment
        Re-evaluate MappingConfidence per decision guide given new experimental
        evidence. Flag edges where confidence may upgrade.

Step 6  Report regeneration
        Run `just gen-report` on the updated graph file. Biologist reviews
        updated confidence levels and evidence chain.
```

---

## Source-label purity

When registering an `AnnotationTransferRun`, **document whether the
source cluster label is morphologically/biologically pure or known to
be mixed**. The distinction shapes how the resulting F1 metrics should
be interpreted in mapping edges and reports.

- **Pure source labels** (patch-seq with morphological confirmation,
  cluster labels from datasets with deep marker validation): expect
  F1 to *rise* with finer atlas resolution. Cluster-level F1 is the
  most informative summary. Example: Que 2021 PV patch-seq
  (`at_run_20260508_que2021_pvin_mmc_wmbv1`) — BIC's F1 rises from
  0.38 at subclass → 0.80 at cluster (`CLUS_0737`).
- **Mixed source labels** (coarse scRNA-seq subclass labels covering
  multiple biological types): expect F1 to *fall* with finer
  resolution. Precision (`target_purity`) at deep levels is the
  honest summary; F1 understates the cells' specificity. Example:
  Yao 2021 SSv4 `Sst` subclass (272 hippocampal cells containing
  OLM, bistratified, HS, oriens-oriens, …) — F1 falls from 0.98 at
  subclass → 0.23 at cluster. The audit tags such cases with
  `at_f1_monotonicity: falls_with_resolution` — read precision over
  F1 when consuming.

**Anti-pattern — do not bundle AT + relabel in one run.** When you
want to score the same MapMyCells output under two label schemes (raw
published labels vs derived/relabel scheme like Chamberland 2024
gene-pair subfamilies on top of Harris 2018 Classes), create **two
separate `AnnotationTransferRun` records** that reference the same
`mmc_results.csv` via `output.relpath`. The schema allows shared
outputs (no uniqueness constraint on `relpath`). Bundling makes the
"drop unassigned" decision ambiguous and prevents downstream KB edges
from citing the relevant scoring slice unambiguously. See
[`planning/at_blind_region_drop_findings_2026-05-12.md`](../planning/at_blind_region_drop_findings_2026-05-12.md)
§ h for the worked example.

---

## Key design decisions (from ROADMAP)

- **Source and target species are explicit**: `source_species` and
  `target_species` fields on `AnnotationTransferEvidence` (cross-species by
  design — typically primate → mouse WMBv1).
- **Discordance handling**: if annotation transfer reports LOW confidence but
  literature strongly supports the mapping, experimental evidence takes
  precedence, but the conflict must be documented as a caveat.
- **Confidence upgrade path**: HIGH requires ≥2 independent evidence types
  including ≥1 experimental. Annotation transfer is the primary route to
  HIGH confidence for atlas mappings.
- **Preflight gate**: Large datasets (>available RAM) require explicit human
  confirmation before loading. The preflight module estimates memory from
  HDF5 metadata without loading the matrix.
- **Run records are self-contained**: every AT run record under
  `kb/annotation_transfer_runs/{run_id}/` must reproduce its outputs from
  inputs and tool versions captured in the manifest, **plus any bespoke
  scripts retained in a `scripts/` subdirectory of the run record**. If
  the recipe in the README references a script (label derivation,
  preprocessing, custom figure rendering, ad-hoc analysis), the script
  must live in `scripts/` not in `/tmp` or another transient location.
  The principle generalises: any committed run record whose reproduction
  recipe references custom scripts must vendor those scripts into the
  run record, so that a future reader can reproduce the run from the
  record alone without depending on session-local state.

---

## Marker expression assessment

Source-side marker assessment (expression of classical markers in the mapped
dataset) and target-side marker cross-checking (expression in candidate atlas
clusters via precomputed stats or class-level h5ad files) are **mapping
concerns**, not annotation transfer concerns. They are handled by
`map-cell-type.md` Step 3, which populates `node_a_value` and `node_b_value`
on property comparisons using available expression data.

The precomputed stats HDF5 downloaded during taxonomy setup (see
ROADMAP.md § Taxonomy Reference DB) provides full-transcriptome cluster means for quantitative
target-side marker assessment without downloading per-class expression
matrices.
