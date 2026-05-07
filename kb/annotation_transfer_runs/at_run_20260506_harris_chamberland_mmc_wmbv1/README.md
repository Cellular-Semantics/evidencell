# Harris 2018 + Chamberland 2024 → WMBv1 annotation transfer

Run id: `at_run_20260506_harris_chamberland_mmc_wmbv1` ([manifest.yaml](manifest.yaml))

Source dataset: Harris et al. 2018 (PLoS Biology, [PMID 29912866](https://pubmed.ncbi.nlm.nih.gov/29912866/), [GEO:GSE99888](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99888); [Figshare 6198656](https://figshare.com/articles/dataset/Transcriptomic_analysis_of_CA1_inhibitory_interneurons/6198656); n=3663 cells, mouse CA1 inhibitory neurons, 10x scRNA-seq).

Source labels: three label sets scored against the same MapMyCells output, in increasing dropout-robustness:

1. **Harris 2018 Class** (50 published subtype labels). Reference / sanity check; widest resolution.
2. **Chamberland subfamily, per-cell** — gene-pair rules applied directly to per-cell Harris expression. Suffers from scRNA-seq dropout: a real Chrna2-OLM cell with zero detected Chrna2 UMIs falls into "unassigned".
3. **Chamberland subfamily, per-cluster** (primary result) — gene-pair rules applied to *Harris-cluster-mean* expression, then propagated to all cells in that Class. Dropout-robust: cluster means average over hundreds of cells per Harris Class, so single-cell dropout does not flip the cluster-level call.

The per-cluster labels are the primary result reported here. Per-cell labels are retained for transparency and for the cross-comparison documented in **Methods note** below.

Target atlas: WMBv1 (CCN20230722) — same `precomputed_stats.h5` (SHA `b21ca985…`) used by [`at_run_20260408_winterer_olm_mmc_wmbv1`](../20260408_winterer_olm_mmc_wmbv1/manifest.yaml).

## Headline — per-cluster Chamberland labels (primary result)

| Subfamily | Best cluster | Recall | Precision | F1 | n cells |
|---|---|---:|---:|---:|---:|
| **Chrna2** | **CLUS_0771** Sst Gaba_3 | 0.81 | 0.54 | **0.65** | 74 |
| **Sst_Nos1** | **CLUS_0859** Sst Chodl Gaba_4 | 0.94 | 1.00 | **0.97** | 31 |
| **Sst_Tac1** | CLUS_0737 Pvalb Gaba_2 | 0.31 | 0.94 | 0.47 | 31 |
| Ndnf | (unresolved) | — | — | — | 27 source |

Three of four Chamberland subfamilies map to specific WMBv1 clusters with strong-to-moderate F1. The **Ndnf** subfamily is the weakest signal in this run: only one Harris Class (`Sst.Cryab`, n=27) had a cluster-mean Ndnf>1.0 within the Sst+ population, and those cells do not concentrate at a single WMBv1 cluster. This is reported as an honest negative result and discussed under **Caveats** below.

The Chamberland subfamily / WMBv1 cluster correspondence at cluster level:

- **Chrna2-OLM (Chamberland) → CLUS_0771** (WMBv1, Sst Gaba_3 supertype)
- **Sst::Nos1-IN (Chamberland) → CLUS_0859** (WMBv1, Sst Chodl Gaba_4 — long-range-projecting Sst subclass, *not* Sst Gaba_3)
- **Sst::Tac1-IN (Chamberland) → CLUS_0737** (WMBv1, Pvalb Gaba_2 — Pvalb subclass, surfacing the transcriptomic Sst↔Pvalb continuity for bistratified cells noted in Chamberland Fig 6)
- **Ndnf::Nkx2-1-OLM (Chamberland) → not cleanly resolved** in this analysis. The cluster-level Ndnf rule selected only `Sst.Cryab` from the Harris Classes, and the cells do not concentrate at a Sst Gaba_3 child cluster. Possible reasons discussed in Caveats.

This re-frames the OLM mapping question: the Sst Gaba_3 supertype encodes biologically meaningful sub-OLM substructure (the Chrna2-OLM subfamily concentrates at CLUS_0771 with cluster-level F1=0.65), but at least one Chamberland subfamily (Ndnf::Nkx2-1-OLM) is not cleanly recoverable from this combination of source dataset, labelling rule, and target taxonomy.

## Methods note — why per-cluster labels are the primary signal

Per-cell labelling using Chamberland's gene-pair rules suffers from a structural artefact specific to droplet scRNA-seq. The 10x Chromium platform has gene-detection dropout rates of 30%–80% per cell for moderate-expression transcripts, including Chrna2 in OLM cells (35% per-cell detection in the Winterer 2019 dataset, which used Sst-Cre and Htr3a-Cre to enrich for OLMs; per-cell detection in the Harris dataset, which is unbiased CA1 inhibitory, will be lower still). Applying a per-cell rule like "Sst > 0 AND Chrna2 > 0" therefore systematically misses real Chrna2-OLM cells in which Chrna2 was not detected at sequencing depth, throwing them into the `unassigned` source bucket. When those cells subsequently map (correctly) to CLUS_0771 in MapMyCells, they dilute the precision of the Chrna2-source → CLUS_0771 assignment, and lower the F1.

Restricting per-cell labelling to "Sst > 0" cells (a narrower subset more enriched for OLM types) does not solve the problem because Sst itself has dropout in heterogeneous datasets — a fraction of real Sst-INs have zero detected Sst UMIs and would be excluded from labelling entirely.

The dropout-robust translation of Chamberland's framework is to apply the gene-pair rules at the **Harris-cluster-mean** level. Harris's published clustering uses several hundred genes jointly across thousands of cells; cluster identity is established with high confidence regardless of individual gene dropout. A cluster mean of Sst expression averaging over 100 cells is essentially noise-free relative to per-cell Sst counts. The per-cluster labels we report propagate the cluster-level subfamily call to each cell in that Harris Class, which sidesteps per-cell dropout entirely. The trade-off is that within-cluster heterogeneity (a Harris Class containing a mix of subfamilies) is hidden — but Harris's clusters are themselves the result of joint clustering and are biologically tighter than per-cell expression products. This trade-off is appropriate for the question we are asking (do Chamberland subfamilies map to distinct WMBv1 clusters?).

The per-cluster F1 figures reported above should still not be over-interpreted in isolation. Specifically:

- **Recall (group_purity)** is the more interpretable single metric: of the cells assigned to a Chamberland subfamily, where do they go? Chrna2 → 81% to CLUS_0771 is a strong same-direction signal even allowing for label-set noise. Recall is robust to dropout in the *target* (atlas) side because MapMyCells uses the full transcriptome for assignment, not single-marker tests.
- **Precision (target_purity)** is a relative measure dependent on how many *other* labelled cells land at the target cluster. With multiple source labels in play, precision values cannot be compared directly across runs with different label sets.
- **Per-cluster cell counts (n)** are small for some subfamilies (Ndnf=27 source cells, Sst_Tac1=31 mapped). Small-n F1s carry wide confidence intervals; a difference of 5–10 cells in destination would change F1 substantially.
- **Within-supertype preference ratios** (e.g. of all Chrna2-source cells landing in Sst Gaba_3 child clusters, what fraction goes to CLUS_0771 vs CLUS_0768?) are the most robust comparisons because dropout in source labelling tends to distribute approximately uniformly across destination clusters when destinations are siblings of similar size.

## Files

| File | Purpose |
|---|---|
| `manifest.yaml` | `AnnotationTransferRun` record (provenance + run params) |
| `class_to_subfamily.tsv` | Per-Harris-Class subfamily assignment table from cluster-mean rules (50 rows) |
| `f1_matrix_chamberland_by_class.csv` | **Primary result.** F1 / group_purity / target_purity per (Chamberland_subfamily × level × target), labels propagated from Harris Class assignments |
| `f1_matrix_chamberland.csv` | Per-cell-rule version (subject to dropout, retained for transparency) |
| `f1_matrix_harris_class.csv` | F1 matrix for Harris's own published Class labels (50 source labels) |
| `labels_chamberland_by_class.json` | 3663 cell barcodes → Chamberland subfamily, derived per-Class |
| `labels_chamberland_subfamily.json` | 3663 cell barcodes → Chamberland subfamily, derived per-cell |
| `labels_harris_class.json` | 3663 cell barcodes → Harris's published Class label |
| `mmc_results.csv` | Raw MapMyCells per-cell hierarchical mapping output |
| `figures/f1_heatmap_by_class.png` | **Primary figure.** Faceted F1 heatmap from per-cluster labels (4 source subfamilies × 4 taxonomy levels × top-6 targets per panel) |
| `figures/f1_heatmap.png` | Same layout from per-cell labels |

## Reproduce

```bash
# 1. Build h5ad + per-cell labels
uv run python scripts/build_harris_h5ad.py

# 2. Derive per-cluster Chamberland labels
uv run python scripts/relabel_by_harris_cluster.py

# 3. Run MapMyCells locally (Python 3.12 required for cell_type_mapper v1.7.1)
uv run --python 3.12 \
  --with "cell_type_mapper @ git+https://github.com/AllenInstitute/cell_type_mapper@v1.7.1" \
  --with anndata --with pandas \
  python -m cell_type_mapper.cli.from_specified_markers \
  --query_path annotation_transfer/data/harris2018/harris_mmc_ready.h5ad \
  --precomputed_stats.path conf/mapmycells/CCN20230722/precomputed_stats.h5 \
  --query_markers.serialized_lookup conf/mapmycells/CCN20230722/mouse_markers.json \
  --extended_result_path .../mmc_local_out/result.json \
  --csv_result_path .../mmc_local_out/result.csv \
  --type_assignment.normalization raw

# 4. Score
grep -v '^#' .../mmc_local_out/result.csv > .../mmc_local_out/result_clean.csv
just at-score .../result_clean.csv .../labels_chamberland_by_class.json .../f1_chamberland_by_class.csv
just at-score .../result_clean.csv .../labels_chamberland_subfamily.json .../f1_chamberland.csv
just at-score .../result_clean.csv .../labels_harris_class.json .../f1_harris_class.csv

# 5. Heatmap
uv run --with matplotlib --with pandas python scripts/render_f1_heatmap.py
```

## Caveats

**Chamberland subfamily labels are derived in-silico**, not Chamberland's own per-cell labels (those were never published; only the rules and code on Zenodo at [10.5281/zenodo.10815380](https://doi.org/10.5281/zenodo.10815380)). Two derivation methods are reported here, with the per-cluster method (primary) being more dropout-robust as documented in **Methods note**.

**Ndnf::Nkx2-1-OLM is not cleanly recovered.** The Ndnf::Nkx2-1 transgenic intersection from Chamberland's lines cannot be replicated exactly because Nkx2-1 is a developmental MGE transcription factor that is silent in adult expression; the operational adult-transcriptomic equivalent is Sst+/Ndnf+. Only one Harris Class (`Sst.Cryab`, n=27) has a cluster-mean Ndnf > 1.0 within the Sst+ population, and the cells in this Class do not concentrate at a Sst Gaba_3 child cluster on MapMyCells transfer. Three plausible reasons:

1. The Ndnf::Nkx2-1-OLM subfamily is genuinely captured in Harris's clustering but not by a cluster whose Ndnf cluster-mean exceeds our threshold (i.e. our threshold is too strict, or Ndnf signal is distributed across multiple Harris Classes that each fall below threshold individually).
2. The subfamily is *not* a coherent transcriptomic group in Harris's clustering — Harris's clusters were not designed to recover Chamberland's subfamilies, and the joint-genome clustering may have placed Ndnf::Nkx2-1-OLM cells in an Ndnf-low cluster that other markers dominated.
3. The subfamily is small enough in the Harris dataset that it falls below Harris's clustering resolution — Chamberland describe Ndnf::Nkx2-1-INs as a minority population.

These cannot be distinguished from this analysis alone. Targeted Ndnf-Cre + scRNA-seq (the wet-lab proposal already on the OLM mapping report) would resolve. Reporting Ndnf as unresolved is the appropriate honest outcome.

**Sst::Nos1 maps cross-supertype** to Sst Chodl Gaba_4 (CLUS_0859), not to a child of Sst Gaba_3 (CS20230722_SUPT_0216). This is consistent with Chamberland's observation that Sst::Nos1 cells are alveus-localised with diffuse axons (the long-range-projecting Sst Chodl identity in WMBv1). Their inclusion in this analysis was intended as a sanity-check positive control for the labelling pipeline; the F1=0.97 confirms the pipeline works.

**Sst::Tac1 maps to Pvalb subclass** (subclass-level recall = 0.78). Real biological signal: Chamberland identify Sst::Tac1-INs as bistratified cells with somata closest to the pyramidal layer; the transcriptomic Sst↔Pvalb continuity for bistratified types is consistent with their report.
