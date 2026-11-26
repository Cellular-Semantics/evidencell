# AT Run: Gao 2023 PVT snRNA-seq, pooled "PVT" label → WMBv1 (CCN20230722)

Status: scored, manifests written, runs registered. **F1 gate review
pending.** No `at_source_sets` declared yet. The labels are re-derived, so
declarations wait for curator approval.

## Purpose

Gao et al. 2023 (*eLife* 12:e81818, PMID:36867023, doi:10.7554/eLife.81818)
report five PVT neuronal subtypes (PVT1–5) from snRNA-seq of mouse PVT
punches, with ISH markers Esr1 / Col12a1 / Npffr1 / Hcrtr1 / Drd3 and an
antero-posterior bias: PVT1/2 posterior, PVT3/4 anterior, PVT5 pan-PVT.
This run maps the dataset onto WMBv1 for the KB's PVT nodes.

## Data source and what is missing

- GEO:GSE208707 `GSE208707_allnuclei_{matrix.mtx,genes.tsv,barcodes.tsv,metadata.csv}.gz`:
  - integer UMI counts for 20,503 nuclei: 13,002 male, plus 7,501 female
    nuclei added in revision;
  - gene symbols only.
- The only cell-type column is `cluster.ids`, the **phase-1** clusters
  (Astrocytes, …, "Neurons (1)" … "Neurons (8)").
- **The phase-2 neuron clusters (PVT vs MD/IMD/BSTpr/Hb) and the phase-3
  PVT1–5 labels are not deposited.** The `SCT_snn_res.*` columns are
  phase-1 resolutions.
- eLife Supplementary file 1 (Europe PMC, PMC10014079) has the authors'
  DEG tables:
  - 1b: phase-2 neuron clusters 0–9;
  - 1c: PVT1–5, with pct.1 / pct.2 / pct_ratio.
  These tables are used **only to name** the re-derived labels.

## Three label schemes, one mapping

| Run | Labels | Node use (proposed, pending gate) |
|---|---|---|
| this run | `PVT` (5,373) + neighbours | `pvt_glutamatergic_neuron` |
| `at_run_20261126_gao2023_pvt_cluster_mmc_wmbv1` | `PVT1`…`PVT5` + neighbours | new PVT1–4 nodes (EXACT) |
| `at_run_20261126_gao2023_pvt_ap_mmc_wmbv1` | `pPVT-biased (PVT1+PVT2)`, `aPVT-biased (PVT3+PVT4)`, `pan-PVT (PVT5)` + neighbours | `apvt_glutamatergic_neuron`, `ppvt_glutamatergic_neuron` |

Neighbour labels: MD 2,334; BSTpr 852; Hb 821; IMD 805; unassigned 122.
All carry "(derived)".

## Label derivation (summary; full report in `research/thalamus/annotation_transfer/gao2023_pvt/derived/derivation_report.md`)

1. **PVT vs neighbours** (paper phase 2):
   - Input: the 10,307 phase-1 neurons with > 1000 genes.
   - Pearson-residual normalisation, Harmony on `sample`, 6 PCs, Leiden.
     The graph is over-clustered to 14 clusters.
   - Each cluster is named by the paper's identity markers: PVT
     Gck/C1ql3/Hcn1; Hb Tac2; MD Adarb2; IMD Cdh24; BSTpr Gpr101.
   - Result: PVT 5,373. The paper reports 5,737, before the female
     samples were added.
2. **PVT1–5** (paper phase 3):
   - Unsupervised re-clustering with 18 PCs does not give five discrete
     clusters matching the paper. Silhouette is 0.13; the result is
     reported as a diagnostic.
   - Instead, each nucleus is assigned by arg-max of z-scored module
     scores over the published Supp. 1c marker sets (top 30 DEGs with
     pct.1 ≥ 0.3 and pct_ratio ≥ 1.5).
   - Validated on held-out published DEGs (log pct-ratio r 0.77–0.95) and
     on held-out ISH markers (Esr1, Npffr1, Hcrtr1 within 0.04 of the
     published pct.1).
3. Nothing in the derivation reads WMBv1 output. Labels were frozen
   before the MapMyCells output was inspected.

## Reproduction (from the clone root)

```bash
# 1. inputs (GEO + eLife Supplementary file 1)
D=annotation_transfer/inputs/datasets/gao2023_pvt
R=kb/annotation_transfer_runs/at_run_20261126_gao2023_pvt_pooled_mmc_wmbv1
bash $R/scripts/fetch_inputs.sh $D

# 2. neuron h5ads: symbols (for label derivation) + WMBv1-Ensembl counts (for MapMyCells)
annotation_transfer/.venv/bin/python -I $R/scripts/build_gao2023_h5ad.py $D kb/taxonomy/CCN20230722/CCN20230722.db

# 3. preflight + local MapMyCells (cell_type_mapper 1.7.5)
just at-preflight ../$D/gao2023_pvt_mmc.h5ad
cd annotation_transfer && uv run --no-sync annotation-transfer map-local \
  inputs/datasets/gao2023_pvt/gao2023_pvt_mmc.h5ad \
  ../conf/mapmycells/CCN20230722/precomputed_stats_ABC_revision_230821.h5 \
  ../conf/mapmycells/CCN20230722/mouse_markers_230821.json \
  inputs/datasets/gao2023_pvt/mmc/mmc_extended.json \
  --csv inputs/datasets/gao2023_pvt/mmc/mmc_results.csv && cd ..
cp $D/mmc/mmc_results.csv $R/

# 4. derived labels (separate env: scanpy 1.13.0, leidenalg 0.12.0, scikit-learn, openpyxl, tabulate)
uv venv /tmp/gao_env && VIRTUAL_ENV=/tmp/gao_env uv pip install scanpy==1.13.0 leidenalg igraph scikit-learn openpyxl tabulate
O=research/thalamus/annotation_transfer/gao2023_pvt/derived
/tmp/gao_env/bin/python -I $R/scripts/derive_gao2023_labels.py $D/gao2023_neurons_symbols.h5ad $D/elife-81818-supp1.xlsx $O
C=kb/annotation_transfer_runs/at_run_20261126_gao2023_pvt_cluster_mmc_wmbv1
A=kb/annotation_transfer_runs/at_run_20261126_gao2023_pvt_ap_mmc_wmbv1
mv $O/labels_pvt_pooled.json $R/; mv $O/labels_pvt_clusters.json $C/; mv $O/labels_pvt_ap.json $A/

# 5. score (bootstrap 0.8), three schemes, shared mmc_results.csv
just at-score ../$R/mmc_results.csv ../$R/labels_pvt_pooled.json ../$R/f1_matrix.csv
just at-score ../$R/mmc_results.csv ../$C/labels_pvt_clusters.json ../$C/f1_matrix.csv
just at-score ../$R/mmc_results.csv ../$A/labels_pvt_ap.json ../$A/f1_matrix.csv

# 6. per-label distribution with WMBv1 MERFISH nucleus annotation
for d in $R:labels_pvt_pooled.json $C:labels_pvt_clusters.json $A:labels_pvt_ap.json; do
  .venv/bin/python -I $R/scripts/summarise_label_distribution.py $R/mmc_results.csv \
    "${d%%:*}/${d##*:}" "${d%%:*}/label_distribution.tsv" --top 6; done

# 7. at_results YAML + index
just migrate-at-metrics && just register-at-run && just validate-at-results-all
```

## Results (bootstrap ≥ 0.8)

| Label (n) | Level | Best WMBv1 target | Coverage | Purity | F1 |
|---|---|---|---|---|---|
| PVT (5,373) | subclass | 149 PVT-PT Ntrk1 Glut | 0.79 | 0.86 | 0.83 |
| PVT1 (1,373) | cluster | 2621 PVT-PT Ntrk1 Glut_2 | 0.64 | 0.64 | 0.64 |
| PVT2 (952) | cluster | 2639 CM-IAD-CL-PCN Sema5b Glut_2 | 0.63 | 0.80 | 0.71 |
| PVT3 (1,013) | cluster | 2624 PVT-PT Ntrk1 Glut_3 | 0.60 | 0.94 | 0.73 |
| PVT4 (953) | cluster | 2626 PVT-PT Ntrk1 Glut_3 | 0.55 | 0.87 | 0.67 |
| PVT5 (1,082) | cluster | 2637 CM-IAD-CL-PCN Sema5b Glut_2 | 0.28 | 0.83 | 0.42 |
| aPVT-biased (PVT3+4) | supertype | 0645 PVT-PT Ntrk1 Glut_3 | 0.61 | 0.97 | 0.75 |
| pPVT-biased (PVT1+2) | supertype | 0644 PVT-PT Ntrk1 Glut_2 | 0.57 | 0.57 | 0.57 |
| pan-PVT (PVT5) | supertype | 0650 CM-IAD-CL-PCN Sema5b Glut_2 | 0.34 | 0.31 | 0.33 |

Of PVT, 18% maps to supertype 0650 (CM-IAD-CL-PCN Sema5b Glut_2), which is
PVT-dominant in WMBv1 MERFISH (PVT 0.34, MD 0.31). The PVT2 (Col12a1,
ventral-edge pPVT, PFC-projecting) population is the main contributor.
Full distributions are in each run's `label_distribution.tsv`.

## Independence from WMBv1

GSE208707 is NIMH data (Penzo lab; 10x Chromium 3′ snRNA-seq, Cell Ranger
3.0.0) and is not part of the WMBv1 training data (Yao et al. 2023, Allen
Institute). The mapping is not circular.
