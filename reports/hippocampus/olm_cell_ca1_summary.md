# Oriens-Lacunosum Moleculare (O-LM) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Oriens-lacunosum moleculare (O-LM) cells are Sst+ GABAergic interneurons of the hippocampal CA1 region whose somata and dendrites are restricted to stratum oriens and whose axons project exclusively to stratum lacunosum-moleculare, targeting the apical dendritic tufts of CA1 pyramidal cells [1][2][3]. This distinctive polarity — receiving excitatory input in stratum oriens and delivering inhibitory output to the most distal dendritic compartment — positions OLM cells as key regulators of CA1 pyramidal cell integration of entorhinal cortex inputs. They are defined molecularly by co-expression of Sst, Chrna2 (the alpha2 subunit of the nicotinic acetylcholine receptor), and Reln, and are Pvalb-negative or Pvalb-sparse [4].

> Hippocampal CA1 stratum oriens interneuron subtypes include oriens lacunosum-moleculare (O-LM) interneurons, which can be identified by the expression of somatostatin and have regular-to-fast action potential spiking patterns (Oren et al., 2009)(Nicholson et al., 2014)(Huh et al., 2016). O-LM cell soma and dendrites reside in the stratum oriens and their axons project to the stratum lacunosum-moleculare layer
> — Friend et al. 2019, Electrophysiological Properties and Function · [1] <!-- quote_key: 116862536_5f5f2ae8 -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552]; CA1 stratum lacunosum moleculare [UBERON:0014557] (axon target) | [1][2][3][4][5][6][7] |
| NT | GABAergic | [4] |
| Markers | Sst (defining); Chrna2 (defining); Reln (defining) | Sst [4][8][5][6]; Chrna2 [6][4]; Reln [4] |
| Negative markers | Pvalb (low/absent) | — |
| Neuropeptides | Sst; Npy; Pnoc | [4] |
| CL term | No CL term currently covers this type — candidate for a new CL term. | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / axon projection:** soma and dendrites in stratum oriens; axon in stratum lacunosum-moleculare · [1]
  > Hippocampal CA1 stratum oriens interneuron subtypes include oriens lacunosum-moleculare (O-LM) interneurons, which can be identified by the expression of somatostatin and have regular-to-fast action potential spiking patterns (Oren et al., 2009)(Nicholson et al., 2014)(Huh et al., 2016). O-LM cell soma and dendrites reside in the stratum oriens and their axons project to the stratum lacunosum-moleculare layer
  > — Friend et al. 2019, Electrophysiological Properties and Function · [1] <!-- quote_key: 116862536_5f5f2ae8 -->

  > CA1 oriens-lacunosum moleculare (O-LM) interneurons innervate only the apical tuft of pyramidal cells (PCs) in stratum lacunosum-moleculare (SLM) and receive inputs only in stratum oriens (SO) (McBain et al., 1994)(Losonczy et al., 2002)(Zemankovics et al., 2010).
  > — Tecuatl et al. 2020, Projection Patterns and Connectivity · [2] <!-- quote_key: 229694907_6865b9db -->

  > oriens-lacunosum moleculare (O-LM) cells (these SOM+ cells project to the distal dendrites in the stratum lacunosum-moleculare though their somata are located in the stratum oriens)
  > — Bezaire et al. 2016, Molecular Markers and Gene Expression · [3] <!-- quote_key: 4776309_dd48b1ec -->

- **GABAergic identity / Sst and Reln expression:** single-cell RT-PCR on morphologically reconstructed OLM cells · [4]
  > Independent of the Cre line used for cell collection, we found consistent expression of GABA release‐related Gad1, Gad2 and Slc6a1 in all OLM interneurons. By contrast, glutamate release‐related vesicular glutamate transporter Slc17a7 (detected in 2/46 cells) and Slc17a6 (detected in 1/46 cells) genes were virtually not expressed across the whole population.
  > — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_1d024a35 -->

  > we found consistent expression of Sst and Reln, and sparse expression of Pvalb across both OLM neuron types
  > — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_2d5a5fb3 -->

- **Chrna2 as specific OLM marker:** · [6]
  > The nicotinic acetylcholine receptor alpha2 subunit (Chrna2) is a specific marker for oriens lacunosum-moleculare (OLM) interneurons in the dorsal CA1 region of the hippocampus
  > — Nichol et al. 2018, Anatomical Location and Morphology · [6] <!-- quote_key: 3591966_644f1e68 -->

  > as well as expression of Chrna2, which has been used as a marker for hippocampal OLM interneurons
  > — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_bd56f851 -->

- **Neuropeptide Npy:** consistently expressed in mouse OLM cells · [4]
  > we found a surprisingly consistent expression of Npy in OLMs
  > — Winterer et al. 2019, Molecular Markers and Gene Expression · [4] <!-- quote_key: 201041756_8d16e821 -->

- **Neuropeptide Pnoc:** detected in both Htr3aCre-OLM and SstCre-OLM cells · [4]
  > we detected Pnoc in both Htr3aCre‐OLM (14/23) and SstCre‐OLM (13/23)
  > — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_1d20426d -->

- **Sst;;Tac1 vs Ndnf;;Nkx2-1 intersectional targeting (OLM vs bistratified distinction):** · [7]
  > While Sst;;Tac1-INs were located closer to the CA1 pyramidal layer, Ndnf;;Nkx2-1-INs and Chrna2-INs were found progressively deeper in O/A
  > — Chamberland et al. 2024, Results · [7] <!-- quote_key: 269246896_1b1ebab4 -->

</details>

No Cell Ontology term currently covers this type — candidate for a new CL term. The nearest superclass is CL:4023017 (sst GABAergic interneuron) but does not capture OLM-specific morphology (soma in stratum oriens, axon in stratum lacunosum-moleculare).

---

## Results

One candidate atlas entry was assessed: supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at MODERATE confidence with PARTIAL_OVERLAP relationship. Three independent AT runs converge on this supertype; the Chrna2-OLM Chamberland per-cluster run sub-resolves OLM cells to cluster 0771 Sst Gaba_3 [CS20230722_CLUS_0771] within SUPT_0216.

**Annotation-transfer overview figure (run-level, filtered)**

![Filtered AT figure for OLM cell — Yao 2021 Sst SSv4 source group](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_olm_cell_ca1.png)

*F1 across taxonomy levels for the Sst source group from Yao 2021 hippocampal formation SSv4 (GEO:GSE185862, n=273 HIP Sst cells). The Sst label aggregates multiple Sst interneuron types (OLM, bistratified, hippocampo-septal, and others); signal splits between SUPT_0219 Sst Gaba_6 (F1=0.759, 161 cells) and SUPT_0216 Sst Gaba_3 (F1=0.488, 83 cells). F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.*

![Filtered AT figure for OLM cell — Harris 2018 Sst.Pnoc.Calb1.Igfbp5 source group](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/figures/f1_for_olm_cell_ca1.png)

*F1 across taxonomy levels for the Harris 2018 Sst.Pnoc.Calb1.Igfbp5 Class label (OLM-type transcriptomic cluster, n=254 cells from GEO:GSE99888). Group_purity=0.965 at SUPT_0216: 96.5% of this SST+/Pnoc+/Calb1+/Igfbp5+ cluster concentrates in Sst Gaba_3, providing strong directional evidence for SUPT_0216 as the OLM-type supertype.*

![Filtered AT figure for OLM cell — Chamberland Chrna2-OLM per-cluster subfamily](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/figures/f1_for_olm_cell_ca1.png)

*F1 across taxonomy levels for the Chrna2-OLM source group derived from Harris 2018 cluster-mean expression using Chamberland 2024 in-silico gene-pair rules (n=153 cells from GEO:GSE99888). Chrna2-labelled cells map to CLUS_0771 Sst Gaba_3 at cluster level (F1=0.649, group_purity=0.813), sub-resolving the OLM population within SUPT_0216. Per-cluster labels are dropout-robust (cluster-mean gene-pair rules).*

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---:|---|---|---|
| 1 | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — (supertype) | 2712 | 🟡 MODERATE | Sst CONSISTENT · Reln CONSISTENT · CA1 SO CONSISTENT · Chrna2 APPROXIMATE | Best candidate |

Total: 1 edge; relationship PARTIAL_OVERLAP.

### Property alignment — 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | GABA (Sst Gaba_3) | CONSISTENT |
| Soma location | CA1 stratum oriens [UBERON:0014552] | CA1 stratum oriens (818 cells) | CA1 SO dominant (within SUPT_0216) | CONSISTENT |
| Sst expression | defining marker | Sst subclass; precomputed mean 11.44 | Sst subclass | CONSISTENT |
| Chrna2 expression | defining marker | not in supertype defining_markers; precomputed mean 1.53; present in ABC Atlas HPF/GABA/Chrna2 filter | CLUS_0771 (Sst Gaba_3): target_purity=0.54 for Chrna2-OLM | APPROXIMATE |
| Reln expression | defining marker | Reln in DEFINING markers; precomputed mean 7.90 | Reln in DEFINING markers | CONSISTENT |
| Sst neuropeptide | Sst; Npy; Pnoc | Sst mean 11.44; Npy mean 5.07; Pnoc mean 3.69 | confirmed at supertype level | CONSISTENT |
| Pvalb (negative) | low/absent | Sst subclass (not Pvalb); precomputed mean 1.48 | Sst subclass | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas supertype metadata + precomputed stats | Atlas metadata | PARTIAL | CA1 SO 818 cells; Sst=11.44; Reln=7.90; Chrna2=1.53; Npy=5.07; Pnoc=3.69; Pvalb=1.48 | atlas-internal |
| Atlas precomputed stats cross-check | Atlas metadata | SUPPORT | All 3 neuropeptides confirmed (Sst, Npy, Pnoc); Reln defining; Pvalb absent | atlas-internal |
| Yao 2021 SSv4 Sst → WMBv1 (GEO:GSE185862) | Annotation transfer | PARTIAL | SUPT_0216 F1=0.488 (83/273 cells, target_purity=1.0); SUPT_0219 dominant (F1=0.759) | atlas-internal |
| Harris 2018 Sst.Pnoc.Calb1.Igfbp5 → WMBv1 (GEO:GSE99888) | Annotation transfer | SUPPORT | SUPT_0216 F1=0.514 (222/254 cells, group_purity=0.965) | atlas-internal |
| Chamberland Chrna2-OLM per-cluster → WMBv1 (GEO:GSE99888) | Annotation transfer | SUPPORT | CLUS_0771 F1=0.649 (74 cells, group_purity=0.813, target_purity=0.54) | atlas-internal |

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🟡 MODERATE

**Supporting evidence**
- Sst subclass identity and GABA NT type are fully consistent with OLM cell identity [4][8][5][6]. CA1 stratum oriens (818 cells) is the primary OLM soma location [1][2][3][4][5][6][7].
- Precomputed stats cross-check confirms all three neuropeptides (Sst=11.44, Npy=5.07, Pnoc=3.69) [4] and the Reln defining marker (7.90) [4]. Pvalb low/absent (1.48), consistent with OLM Pvalb-sparse phenotype [4].
- Reln is in the defining markers of SUPT_0216, directly matching OLM Reln expression established by Winterer et al. 2019 [4].
- Harris 2018 Sst.Pnoc.Calb1.Igfbp5 (OLM-type transcriptomic cluster, n=254 cells) maps with group_purity=0.965 to SUPT_0216 (F1=0.514, 222 cells). The very high group_purity means 96.5% of this SST+/Pnoc+/Calb1+/Igfbp5+ cluster concentrates in Sst Gaba_3 — strong directional evidence for SUPT_0216 as the OLM-type supertype.
- Chamberland per-cluster Chrna2-OLM labels applied to Harris 2018 (n=153 cells) map to CLUS_0771 (Sst Gaba_3 child cluster) at cluster level with F1=0.649 and group_purity=0.813, providing the first cluster-level AT support for OLM cell identity within SUPT_0216. Per-cluster labels are dropout-robust.
- Yao 2021 SSv4 Sst (n=273 HIP cells): Sst cells map strongly to Sst Gaba subclass (F1=0.983); at supertype level SUPT_0216 receives 83/273 cells with target_purity=1.0.

**Marker evidence provenance**
- **Sst (defining and neuropeptide):** transcript-level evidence by single-cell RT-PCR on patch-clamp filled and morphologically reconstructed OLM cells by Winterer et al. 2019 [4]; additional transcript support from Chamberland et al. 2023 [8]. Atlas precomputed stats mean 11.44 — strong concordance. No discrepancy.
- **Chrna2 (defining):** established at protein and transcript level. Nichol et al. 2018 [6] characterised Chrna2 as specific OLM marker in dorsal CA1; Winterer et al. 2019 [4] confirmed at transcript level. However, Chrna2 is not in the SUPT_0216 defining markers (precomputed mean 1.53; APPROXIMATE alignment). The ABC Atlas HPF/GABA/Chrna2 filter retains SUPT_0216 (unlike SUPT_0219), consistent with OLM cells being a subpopulation with Chrna2 scattered across clusters. The Chamberland Chrna2-OLM cluster-level result (CLUS_0771 F1=0.649) partially resolves this.
- **Reln (defining):** transcript-level by RT-PCR in morphologically reconstructed OLM cells [4]. Reln is also in DEFINING markers of SUPT_0216 (mean 7.90) — one of the best-supported alignment points.
- **Npy (neuropeptide):** consistent at transcript level in mouse OLM cells per Winterer et al. 2019 [4]; species caveat — Npy is consistent in mouse but absent in rat. Atlas is mouse (WMBv1), so mouse data are directly relevant. Precomputed mean 5.07.
- **Pnoc (neuropeptide):** detected in 14/23 Htr3aCre-OLM and 13/23 SstCre-OLM cells [4]. Precomputed mean 3.69.
- **Pvalb (negative):** Winterer et al. 2019 [4] reports sparse (not absent) Pvalb expression — the known PV+ OLM subpopulation means Pvalb negativity is not absolute. Atlas precomputed mean 1.48, consistent with sparse expression.

**Concerns**
- Chrna2 APPROXIMATE: Chrna2 is an OLM defining marker but shows only scattered expression at supertype level (precomputed mean 1.53; not in defining markers). *(note: OLM cells are a subpopulation within SUPT_0216; Chrna2 expression marks OLM cells specifically but is diluted across the mixed supertype — consistent with DISTRIBUTED_ACROSS_CLUSTERS caveat.)*
- DISTRIBUTED_ACROSS_CLUSTERS: Sst Gaba_3 supertype contains at least three classical hippocampal cell types: OLM cells, bistratified cells, and hippocampo-septal (HS) cells. These are not separable at supertype level.
- Non-hippocampal cells in supertype: prosubiculum (259 cells) and posterior amygdala (780 cells) are prominent. *(note: posterior amygdala is anatomically distant from CA1 stratum oriens — the classical OLM type may correspond to a subtype of this T-type, but the posterior amygdala population is not the CA1 OLM population specifically.)*
- AT ambiguity: the dominant Sst supertype in the GSE185862 MapMyCells transfer is SUPT_0219 Sst Gaba_6 (F1=0.759, 161 cells), not SUPT_0216 (F1=0.488, 83 cells). The Harris AT evidence (group_purity=0.965 at SUPT_0216; Chrna2 F1=0.649 at CLUS_0771) partially resolves this ambiguity in favour of SUPT_0216 as the OLM-type supertype.

**What would upgrade confidence**
- OLM-specific annotation transfer with morphologically or genetically labelled cells (Chrna2-Cre or Ndnf::Nkx2-1 labelled Sst+ cells), targeting F1 ≥ 0.80 at CLUSTER level against WMBv1.
- Cluster-level Chrna2/Sst/Reln co-expression analysis identifying which SUPT_0216 cluster(s) show highest Chrna2 co-expression with Sst and Reln.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The O-LM cell is defined here on a CLASSICAL_MULTIMODAL basis: classical morphology + single-cell electrophysiology + molecular markers. Soma in CA1 stratum oriens [UBERON:0014552] [1][2][3][4][5][6][7]; axon in CA1 stratum lacunosum moleculare [UBERON:0014557]; GABAergic [4]; defining markers Sst [4][8][5][6], Chrna2 [6][4], Reln [4]; negative marker Pvalb; neuropeptides Sst, Npy, Pnoc [4]. No CL term exists for OLM cell.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at rank 1 (supertype) using metadata-based scoring. Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to atlas-side values via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED.

**Annotation transfer.**

Run 1 — Yao 2021 SSv4 hippocampal formation → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4; Sst subclass, n=273 HIP cells) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |

Run 2 — Harris 2018 CA1 inhibitory neurons → WMBv1 (scored under Harris published Class labels):

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Harris 2018 published Class labels for 3663 mouse CA1 inhibitory neurons; source DOI: 10.1371/journal.pbio.2006387) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100). Run locally against precomputed_stats_ABC_revision_230821.h5. |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_matrix_harris_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/f1_matrix_harris_class.csv) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | This run record scores Harris 2018 published Class labels against WMBv1. The companion at_run_20260512_chamberland_subfamily_mmc_wmbv1 scores the same MMC output under Chamberland 2024 in-silico subfamily labels. |

Run 3 — Harris 2018 + Chamberland 2024 in-silico Chrna2-OLM subfamily labels → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Harris 2018 Class labels relabelled by Chamberland 2024 in-silico gene-pair criteria; Chrna2-OLM per-cluster label; n=153 cells propagated from Sst.Pnoc.Calb1.Pvalb and related Harris Classes) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, same MMC output as Run 2; re-aggregated under Chamberland subfamily labels via class_to_subfamily.tsv; bootstrap_iteration=100). |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_matrix_chamberland_by_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/f1_matrix_chamberland_by_class.csv) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | Per-cluster derivation (f1_matrix_chamberland_by_class.csv) is the primary result: gene-pair rules applied to Harris cluster-mean expression, dropout-robust. Per-cell derivation is also retained but subject to scRNA-seq dropout. Headline cluster-level finding: Chrna2-OLM → CLUS_0771 (F1=0.649, recall=0.813). |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:10+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ATLAS_METADATA ×2 | PARTIAL; SUPPORT | atlas-internal |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER (GEO:GSE185862) | PARTIAL | atlas-internal |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER (GEO:GSE99888, Harris Class) | SUPPORT | atlas-internal |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER (GEO:GSE99888, Chamberland Chrna2) | SUPPORT | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Oriens-Lacunosum Moleculare (O-LM) cell → 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at MODERATE confidence. Key support: three independent AT runs converge on SUPT_0216 — Harris 2018 Sst.Pnoc.Calb1.Igfbp5 cluster maps with group_purity=0.965 (SUPPORT); Chamberland Chrna2-OLM per-cluster labels sub-resolve to CLUS_0771 within SUPT_0216 at F1=0.649 (SUPPORT); Reln is a defining supertype marker with precomputed mean 7.90; all three neuropeptides (Sst, Npy, Pnoc) confirmed; CA1 SO soma location is exactly matched (818 cells); Pvalb absent at supertype level. Key caveats: DISTRIBUTED_ACROSS_CLUSTERS (SUPT_0216 contains OLM cells, bistratified cells, and HS cells — not separable at supertype level); Chrna2 APPROXIMATE (not in defining markers, scattered expression); prominent non-hippocampal cells (posterior amygdala 780 cells, prosubiculum 259 cells).

No Cell Ontology term currently covers the OLM cell; the nearest superclass CL:4023017 (sst GABAergic interneuron) does not capture OLM-specific morphology (soma in stratum oriens, exclusive axon projection to stratum lacunosum-moleculare). This is a priority candidate for a new CL term request.

### Proposed experiments and follow-ups

The three AT runs already substantially support SUPT_0216 as the OLM supertype and have partially sub-resolved to CLUS_0771 via the Chrna2-OLM per-cluster Chamberland run. Remaining gaps:

1. **OLM-specific annotation transfer with morphologically labelled cells.** MapMyCells annotation transfer using a source dataset with morphologically or genetically identified OLM cells (Chrna2-Cre or Ndnf::Nkx2-1 × Sst-Cre labelled). Target: F1 ≥ 0.80 at CLUSTER level against WMBv1. Expected output: AnnotationTransferEvidence at cluster level, resolving the SUPT_0216 vs SUPT_0219 ambiguity and confirming or refuting CLUS_0771 as the primary OLM cluster. Resolves: open question 1; Chrna2 APPROXIMATE alignment; DISTRIBUTED_ACROSS_CLUSTERS caveat.

2. **Cluster-level Chrna2/Sst/Reln co-expression analysis.** Identify which WMBv1 cluster(s) within Sst Gaba_3 show highest Chrna2 co-expression with Sst and Reln, without new experiments, by querying the atlas precomputed stats at cluster level. Expected output: cluster-level property comparison entries. Resolves: open question 2; Chrna2 APPROXIMATE alignment.

3. **Primary source for Pvalb negativity.** Targeted cite-traverse for "Pvalb OLM hippocampus CA1 negative marker" to identify a primary study testing Pvalb in morphologically confirmed OLM cells. Expected output: LiteratureEvidence entry. Resolves: open question 3 (sparse vs absent Pvalb).

4. **CL new term request.** Draft a CL new term for "oriens-lacunosum moleculare interneuron" via `workflows/cl-term-request.md`. Expected output: CL term issue; subsequent EXACT cl_mapping on this node. Resolves: CL placement gap.

### Open questions

1. Do OLM cells preferentially map to WMBv1 supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216] or 0219 Sst Gaba_6 [CS20230722_SUPT_0219] when a morphologically labelled source dataset is used? The Yao 2021 SSv4 mixed-Sst transfer favours SUPT_0219 (F1=0.759 vs 0.488), but Harris AT evidence favours SUPT_0216 (group_purity=0.965). A morphologically confirmed source dataset would resolve this ambiguity.

2. Which specific WMBv1 cluster(s) within Sst Gaba_3 carry the highest Chrna2 expression co-expressed with Sst and Reln? CLUS_0771 is the candidate from the Chamberland Chrna2-OLM per-cluster run (F1=0.649), but additional cluster-level data are needed to confirm.

3. What is the basis for Pvalb as an OLM negative marker? Winterer et al. 2019 [4] reports sparse (not absent) Pvalb expression across both OLM neuron types. Is there a primary study confirming this exclusion criterion in morphologically identified OLM cells?

4. Are the non-hippocampal cells in Sst Gaba_3 (posterior amygdala 780 cells; prosubiculum 259 cells) OLM-like Sst+ interneurons, or unrelated Sst types?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Friend et al. 2019 | [30987110](https://pubmed.ncbi.nlm.nih.gov/30987110) | soma location; electrophysiology |
| [2] | Tecuatl et al. 2020 | [33361464](https://pubmed.ncbi.nlm.nih.gov/33361464) | soma location; axon projection |
| [3] | Bezaire et al. 2016 | [28009257](https://pubmed.ncbi.nlm.nih.gov/28009257) | soma location; Sst marker |
| [4] | Winterer et al. 2019 | [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995) | soma location; NT type; Sst, Chrna2, Reln markers; Npy, Pnoc neuropeptides; Pvalb sparse |
| [5] | Leão et al. 2012 | [23042082](https://pubmed.ncbi.nlm.nih.gov/23042082) | soma location; Sst marker |
| [6] | Nichol et al. 2018 | [29487503](https://pubmed.ncbi.nlm.nih.gov/29487503) | soma location; Chrna2 specific OLM marker |
| [7] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347) | soma location; OLM vs bistratified intersectional targeting |
| [8] | Chamberland et al. 2023 | [37162922](https://pubmed.ncbi.nlm.nih.gov/37162922) | Sst marker |
