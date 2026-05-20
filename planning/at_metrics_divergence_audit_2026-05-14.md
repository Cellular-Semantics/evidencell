# AT `metrics_by_level` vs `f1_matrix.csv` audit — 2026-05-14

Survey script: `/tmp/at_survey.py` (one-off; not committed).

## Methodology

For every `ANNOTATION_TRANSFER` evidence item in `kb/graphs/**/*.yaml`,
recompute the F1 value that *should* live in `metrics_by_level[*].f1_score`
by reading the run's `f1_matrix.csv`, filtering to the row whose
`source_label` matches the evidence's `source_cluster_label`, and looking
up the `target_name` declared in the metrics row.

Tolerance: ±0.05 absolute on F1.

## Headline numbers

| Category | Count |
|---|---|
| Total AT metric rows across KB | 196 |
| Within tolerance (stored ≈ CSV row for declared `source_cluster_label`) | 132 |
| Diverged by > 0.05 from declared-label CSV row | 26 |
| `source_cluster_label` is a pool (`" + "`, `"combined"`, `"aggregated"`) and no exact CSV row exists | 24 |
| No CSV available (no `run_ref` or run dir missing) | 38 (mostly cerebellum) |

So **64 of 196 AT metric rows (33%) are either divergent or unverifiable**
against the canonical `f1_matrix.csv`.

## Divergence buckets

### Bucket A — Hand-entered numbers that don't match any obvious aggregation

- `hippocampus_OLM.yaml` edge_olm_to_wmb_clus_0769 (4 rows) — fixed
  in this session. Stored 0.68 / 0.68 / 0.67 / 0.47 was neither
  per-source nor pooled. Replaced with pooled values from
  `at_figures --pool --emit-metrics` (0.99 / 0.99 / 0.97 / 0.65).

### Bucket B — Pooled labels that read as single source

Edges declare `source_cluster_label: "BIC (hBIC n=11 + vBIC n=9 aggregated)"`
or `"Sst-OLM + Htr3a-OLM (combined)"`, but the CSV uses the bare label
`BIC` / has separate `Sst-OLM` + `Htr3a-OLM` rows. The stored F1 may have
been computed under one grouping while the figure used another.

Affected:

- `hippocampus_GABAergic_interneurons.yaml`: BIC bistratified (9 rows),
  PV basket pool (also flagged as unauditable, 6 rows).
- `hippocampus_OLM.yaml`: combined OLM (fixed).

### Bucket C — Stored < CSV row by 0.4–0.6 absolute

The Que 2021 PV-IN AAC edges in `hippocampus_GABAergic_interneurons.yaml`:
stored ≈ 0.12–0.24 vs CSV ≈ 0.78–0.83 at all levels. AAC IS a single
source label in the CSV. Stored values look like they were computed
against the WRONG target (cross-contamination row e.g. CLUS_0739 instead
of an AAC-best target), or filtered to a non-best target on the edge.

Affected:
- `edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0204` (4 levels)
- `edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0732` (4 levels)

These are large divergences and likely indicate a curation bug, not just
a sync drift.

### Bucket D — DG immature/neuroblast/granule run

`20260414_dentate_gyrus_report_ingest.yaml` has 9 rows diverging by
−0.07 to −0.64. Pattern looks like the values were taken from a
non-best target at each level (e.g. `dg_neuroblast → 04 DG-IMN Glut`
stored F1=0.10 but Neuroblast_1 at CLASS level has F1=0.57). Either the
"best" claim is wrong or a different metric (filtered to a specific
target subset) was used.

### Bucket E — Chamberland subfamily

`hippocampus_chamberland_subfamilies.yaml` Chrna2/Ndnf rows: stored
0.33 / 0.04 / 0.05 vs CSV 0.74 / 0.23 / 0.20. Same pattern as Bucket C.

## Unverifiable rows

### Cerebellum (`CB_MLI_types.yaml`, `CB_PLI_types.yaml`)
No `run_ref` on the evidence items — they predate the
`annotation_transfer_runs/` directory convention. 5 evidence items
across both files. Cannot audit without finding the source matrix.

### Yao 2021 SSv4 subclass-level groupings
A handful of edges have `source_cluster_label` = `'Pvalb'` or `'Sst'`
(subclass-level groupings of the Yao 2021 SSv4 data). These labels
don't exist in `f1_matrix.csv` (which is keyed on cluster-level Yao
labels). Either the original ingest aggregated to subclass before
writing the F1, or the wrong label was recorded.

## What this confirms

The OLM-edge divergence is **not** an isolated case. The KB has a
systematic problem:

1. AT metrics are stored as a one-shot snapshot when the evidence is
   first written; no script keeps them in sync with the canonical
   `f1_matrix.csv`.
2. `source_cluster_label` is free-text — pools, aliases, and aggregation
   notes are all stuffed into the same string, defeating programmatic
   joins back to the CSV.
3. There is no recorded provenance for *how* a stored F1 was computed
   (best-target per source? pooled? best of any source at this target?
   a manual filter applied at ingest?). When stored ≠ CSV, we cannot
   even tell which side is wrong.

## Recommendations (for the broader persistence-audit project)

1. **Add a refresh tool** analogous to `refresh_expression_pcs.py`:
   `refresh_at_metrics.py` that, for every AT evidence item with a
   resolvable `run_ref`, recomputes `metrics_by_level` from the CSV
   (per-source or pooled per declared rule) and rewrites it. Conservative
   default = dry-run + diff report.

2. **Schema move**: make `source_cluster_label` a structured slot:
   ```yaml
   source_groups:
     - label: "Sst-OLM"        # CSV-matching key
       n_cells: 23
     - label: "Htr3a-OLM"
       n_cells: 23
   aggregation: POOLED         # POOLED | PER_SOURCE | BEST_OF_ANY
   ```
   `metrics_by_level` then carries `aggregation` too, so the recompute
   is unambiguous.

3. **Make `metrics_by_level` derived, not stored**: at report time the
   gen-report agent reads the CSV + the structured `source_groups` /
   `aggregation` and computes the figure, the caption, and the inline
   stats from one source. The edge YAML stores only the *interpretation*
   (which target was called, why) — not the raw numbers.

4. **`at_figures.py --emit-metrics`** (landed this session) makes (3)
   feasible: the same code that draws the figure emits the sidecar JSON
   the report grounds against. Extending it to also dump pooled values
   for declared pools would close the audit loop.

## Action proposed for this session

- ✅ OLM edge fixed.
- ✅ `--emit-metrics` landed.
- ✅ Survey done (this doc).
- ⏭ Broader fix-up (Buckets C / D / E and the cerebellum NO-CSV rows)
  deferred to a follow-up — each will need its CSV interpreted carefully,
  some will require re-running the AT pipeline against the original
  source data, and the schema move is a substantial design change.

File the architecture issue ("Property persistence audit") and attach
this doc as the AT-specific evidence.
