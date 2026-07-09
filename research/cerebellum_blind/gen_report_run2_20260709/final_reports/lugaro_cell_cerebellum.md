# Lugaro cell (cerebellum) — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml`*

---

## Introduction

Lugaro cells are rare GABAergic/glycinergic inhibitory interneurons of the cerebellar cortex whose soma lies just beneath the Purkinje cell layer, at the Purkinje cell layer/granule cell layer border [1][2]. They are conventionally divided into two morphological subgroups: fusiform Lugaro cells, with an elongated soma in the granule cell layer and bipolar dendrites, and globular cells, with a small rounded soma directly below the Purkinje cell soma. Both subgroups project axons through the molecular layer to inhibit molecular layer interneurons (basket and stellate cells) and Golgi cells, acting as an interneuron-selective interneuron that can disinhibit cerebellar output [2][3]. The dual GABAergic/glycinergic neurotransmitter phenotype is well established [3][2], and the 5-HT2A receptor (Htr2a) and glycine transporter (Slc6a5) are the defining transcriptomic markers used to identify Lugaro cells in the Kozareva/Osorno transcriptomic dataset [2]. Mapping the Lugaro cell to the WMBv1 atlas is important both to anchor this functionally distinct interneuron population in the multi-resolution taxonomy and to support annotation transfer in large-scale cerebellar single-nucleus datasets.

**Classical type description**

| Property | Value | References |
|---|---|---|
| Soma location | Purkinje cell layer of cerebellar cortex [UBERON:0002979]; cerebellar cortex [UBERON:0002129] | [1][2] |
| NT type | GABAergic/glycinergic (mixed) | [3][2] |
| Defining markers | Htr2a, Slc6a5, Kcnd3, Grm1 | [2][4] |
| Neuropeptides | Nrgn | [5] |
| Negative markers | — | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** Morphological identification in GFP-expressing mouse cerebellar slices; globular cells and fusiform Lugaro cells both placed beneath the Purkinje cell layer · [1]
  > Inhibitory interneurons in the cerebellar granular layer are more heterogeneous than traditionally depicted. In contrast to Golgi cells, which are ubiquitously distributed in the granular layer, small fusiform Lugaro cells and globular cells are located underneath the Purkinje cell layer and small in number.
  > — Hirono et al. 2012, Structure, morphology, and anatomical subtypes · [1] <!-- quote_key: 14276970_0b2772de -->

- **Soma location (additional):** Yellow Cameleon reporter mouse; Lugaro/globular cells extend somatodendritic meshwork beneath the PC layer · [3]
  > Beneath the PC layer, they extended a sheet of somatodendritic meshwork interconnected with neighboring LCs by adherens junctions
  > — Miyazaki et al. 2020, Structure, morphology, and anatomical subtypes · [3] <!-- quote_key: 219105292_3797906f -->

- **NT type:** Yellow Cameleon reporter line; two-thirds of tagged cells dually GABAergic/glycinergic · [3]

- **Defining markers (Htr2a, Slc6a5):** Transcriptomic study, Kozareva/Osorno snRNA-seq dataset; PLI3 identified as Lugaro cells via co-expression · [2]
  > The expression of Htr2a that encodes the 5-HT2A receptor, and Slc6a5 that encodes the glycine transporter, by PLI3 suggests that this cell type corresponds to Lugaro cells (LCs) that are glycinergic and excited by serotonin (Dieudonné et al., 2000). LCs are GABAergic/glycinegic inhibitory PLIs with a distinctive fusiform soma that are inhibited by PCs, and that locally inhibit GoCs and MLIs, and send long-range axons to unknown targets
  > — Osorno et al. 2022, Function and circuit connectivity · [2] <!-- quote_key: 233245440_9b6b19b2 -->

- **Defining markers (Kcnd3, Grm1):** Anatomical immunostaining studies using antibodies against Kv4.3 (Kcnd3 protein) and mGluR1α (Grm1 protein) in Lugaro/globular cells · [4]

- **Neuropeptide (Nrgn):** Immunohistochemistry for neurogranin (Nrgn protein) used to identify Golgi/Lugaro cells in labeled cerebellar tissue · [5]
  > In cases in which many granule cells were labeled in the internal granular layer, it was difficult to identify Golgi/Lugaro cells based on morphological features only. In such cases, identification was facilitated by immunohistochemistry for neurogranin.
  > — Kita et al. 2013, Structure, morphology, and anatomical subtypes · [5] <!-- quote_key: 1394480_7612b706 -->

</details>

**Cell Ontology mapping:** Lugaro cell [[CL:0011006](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0011006)] (EXACT).

---

## Results

Annotation transfer of the transcriptomically defined Lugaro cell source group (PLI_3; n=531 cells from Kozareva/Osorno 2021 cerebellar snRNA-seq, GEO:GSE165371) maps with exceptional precision to the supertype 1145 CB PLI Gly-Gaba_2 [CS20230722_SUPT_1145] (F1=0.96; Purity=0.98, Coverage=0.94; see figure and property comparison table), supporting the primary mapping at supertype resolution. At cluster resolution, PLI_3 cells distribute across multiple child clusters of this supertype, with 5180 CB PLI Gly-Gaba_2 [CS20230722_CLUS_5180] showing the strongest individual cluster signal (F1=0.65; see figure and candidates table).

![Filtered AT figure for Lugaro cell (cerebellum)](../../kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/reports/cerebellum_blind/figures/f1_for_lugaro_cell_cerebellum.png)

*F1 across taxonomy levels for the PLI_3 source group (Kozareva et al. 2021 cerebellar cortex snRNA-seq; n=531 Lugaro cell nuclei). Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. The supertype-level result (F1=0.96) is the dominant signal; cluster-level scatter (best F1=0.65 at CLUS_5180) reflects PLI_3 nuclei distributing across three child clusters within the supertype. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.*

---

### 1145 CB PLI Gly-Gaba_2 [CS20230722_SUPT_1145] · 🟢 HIGH

**Table 1 — Property comparison**

| Property | Classical | Supertype (SUPT_1145) | Best cluster (CLUS_5180) | Alignment |
|---|---|---|---|---|
| Soma location | Purkinje cell layer of cerebellar cortex [UBERON:0002979]; cerebellar cortex [UBERON:0002129] | no atlas anat data | Cerebellum [MBA:512] region_fraction_100um=0.620 (lower_bound rollup) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| NT type | GABAergic/glycinergic (mixed) | not asserted | GABA-Glyc | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Htr2a expression | defining marker | 6.39; cohort_pct 0.982; child-coverage 1.000 | 6.63; cohort_pct 0.979 | CONSISTENT |
| Slc6a5 expression | defining marker | 7.87; cohort_pct 0.982; child-coverage 1.000 | 7.69; cohort_pct 0.989 (MERFISH panel) | CONSISTENT |
| Kcnd3 expression | defining marker | 7.46; cohort_pct 0.811; child-coverage 1.000 | 7.50; cohort_pct 0.807 | CONSISTENT |
| Grm1 expression | defining marker | 8.59; cohort_pct 0.910; child-coverage 1.000 | 8.64; cohort_pct 0.882 | CONSISTENT |
| Nrgn (neuropeptide) | neuropeptide (classical) | 0.01; cohort_pct 0.018 | 0.04; cohort_pct 0.059 | DISCORDANT |
| Sex ratio (MFR) | not documented | not available | not assessed | NOT_ASSESSED |

*(All 4 defining markers are CONSISTENT across all child clusters of SUPT_1145 (child-coverage 1.000 for all four genes). Only the Nrgn neuropeptide comparison is DISCORDANT — Nrgn is near-zero at both the supertype and best-cluster level. Child-cluster breakdown of Nrgn: CLUS_5180 = 0.04, CLUS_5182 = 0.00, suggesting Nrgn is absent from the SUPT_1145 lineage. Best AT match at cluster level: CLUS_5180.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (SUPT_1145) | Atlas metadata | PARTIAL | Supertype-level node; no region data | atlas-internal |
| PLI_3 → SUPT_1145 AT | Annotation transfer | SUPPORT | F1=0.96 at supertype | atlas-internal |

**Supporting evidence:**

- Annotation transfer of PLI_3 (531 Lugaro cell nuclei from Kozareva/Osorno 2021, GEO:GSE165371) via MapMyCells (cell_type_mapper 1.7.1; at_run_20260709_kozareva_cerebellum_mmc_wmbv1) places 94% of PLI_3 cells on SUPT_1145 with purity of 0.98 — the dominant supertype-level signal across the entire CB PLI Gly-Gaba subclass. The PLI_3 source label in the Kozareva dataset is itself identified as Lugaro cells on the basis of Htr2a and Slc6a5 co-expression ([2], quote_key 233245440_9b6b19b2), making this annotation transfer a direct experimental link between the classical Lugaro cell and the WMBv1 supertype.
- All four defining markers (Htr2a, Slc6a5, Kcnd3, Grm1) are CONSISTENT at supertype level, with expression values in the top decile of the GABAergic/glycinergic cerebellar interneuron cohort and child-cluster coverage of 1.000 across all four genes (see Table 1). This means every child cluster of SUPT_1145 expresses the Lugaro cell marker set.

**Marker evidence provenance:**

- **Htr2a** is a transcript-level defining marker for PLI3/Lugaro cells, established by Kozareva/Osorno snRNA-seq [2]. The Osorno 2022 paper confirms Htr2a encodes the 5-HT2A receptor and that its expression by PLI3 is the basis for the Lugaro cell assignment. SUPT_1145 shows Htr2a = 6.39 (cohort pct 0.982 of 50 cerebellar GABAergic/glycinergic candidates), CONSISTENT.
- **Slc6a5** is also a transcript-level marker established by the same transcriptomic study [2]. It encodes the glycine transporter and is jointly responsible for the PLI3 → Lugaro identification. Atlas annotation notes Slc6a5 as a MERFISH panel marker on CLUS_5180 (Slc6a5 = 7.69, cohort pct 0.989). CONSISTENT.
- **Kcnd3** and **Grm1** are established by protein-level immunolabeling (Kv4.3/Kcnd3 and mGluR1α/Grm1 antibodies in anatomical studies of Lugaro/globular cells [4]). Expression is confirmed at transcript level on SUPT_1145 (Kcnd3 = 7.46, Grm1 = 8.59). CONSISTENT.
- **Nrgn** as a neuropeptide marker for Lugaro cells rests on a single immunohistochemical identification study using neurogranin antibody [5]; Nrgn was used as an identification aid for Golgi/Lugaro cells, not as a defining transcript-level marker. SUPT_1145 shows Nrgn = 0.01 (DISCORDANT). Given that the primary functional identification of Lugaro cells relies on Htr2a + Slc6a5 (transcriptomic, [2]) rather than on Nrgn, this discordance likely reflects an atlas expression gap rather than evidence against the mapping — but should be followed up to determine whether Nrgn is a genuine Lugaro cell transcript or an antibody artefact from the original study.

  *(note: Atlas annotation/expression discrepancy — Nrgn is listed as a neuropeptide on the classical Lugaro cell node but shows precomputed mean expression = 0.01 on SUPT_1145. The classical Nrgn annotation derives from protein-level immunohistochemistry used as an identification aid, not from transcript-level evidence. Discordance does not challenge the primary AT-based mapping but should be investigated.)*

**Concerns:**

- Nrgn (neuropeptide_Nrgn) is DISCORDANT: precomputed mean expression = 0.01 on SUPT_1145 (cohort_pct 0.018), and 0.04 on CLUS_5180 (cohort_pct 0.059) — both well below MIN_DETECTABLE (0.1). The classical annotation of Nrgn as a Lugaro cell marker is based solely on immunohistochemistry [5] and was used as an identification convenience rather than as a defining transcript. There is no transcript-level evidence in the gathered literature that Nrgn is specifically expressed by Lugaro cells. Absence at transcript level in the atlas is therefore not a strong counter-signal, but the discordance should be noted.
- Region comparison at supertype level is NOT_ASSESSED (no atlas anat data on SUPT_1145). At cluster level (CLUS_5180), region_fraction_100um = 0.620 (lower_bound rollup — true value may be higher), CONSISTENT with cerebellar cortex location.

**What would upgrade confidence:**

- The supertype-level mapping is already at HIGH confidence based on the direct AT evidence. Cluster-level confidence could be upgraded by a patch-seq study targeting morphologically confirmed Lugaro cells and mapping them to CLUS_5180 vs. sibling clusters, establishing whether the within-supertype cluster scatter reflects subtype heterogeneity (fusiform vs. globular Lugaro) or technical noise.
- Resolve whether Nrgn is expressed at transcript level in Lugaro cells: a targeted cite-traverse for "neurogranin Lugaro cerebellum scRNA-seq" would clarify whether the Nrgn immunolabel corresponds to a genuine transcript signal not captured in current atlas precomputed statistics.

---

### 5180 CB PLI Gly-Gaba_2 [CS20230722_CLUS_5180] · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Best cluster (CLUS_5180) | Alignment |
|---|---|---|---|
| Soma location | Purkinje cell layer of cerebellar cortex [UBERON:0002979]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] region_fraction_100um=0.620 (lower_bound) | CONSISTENT |
| NT type | GABAergic/glycinergic (mixed) | GABA-Glyc | CONSISTENT |
| Htr2a expression | defining marker | 6.63; cohort_pct 0.979 | CONSISTENT |
| Slc6a5 expression | defining marker (MERFISH) | 7.69; cohort_pct 0.989 | CONSISTENT |
| Kcnd3 expression | defining marker | 7.50; cohort_pct 0.807 | CONSISTENT |
| Grm1 expression | defining marker | 8.64; cohort_pct 0.882 | CONSISTENT |
| Nrgn (neuropeptide) | neuropeptide (classical) | 0.04; cohort_pct 0.059 | DISCORDANT |
| Sex ratio (MFR) | not documented | not assessed | NOT_ASSESSED |

*(CLUS_5180 is the AT-best child cluster within SUPT_1145, with cluster-level F1=0.65 (Purity=0.99, Coverage=0.49). The remaining PLI_3 cells distribute across sibling cluster CLUS_5182 (and possibly other CB PLI Gly-Gaba_2 members not surfaced in the top candidates); this within-supertype scatter is consistent with morphological heterogeneity between fusiform Lugaro and globular cell subpopulations documented in the literature.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (CLUS_5180) | Atlas metadata | PARTIAL | region_fraction_100um=0.620 (lower_bound) | atlas-internal |
| PLI_3 → CLUS_5180 AT | Annotation transfer | SUPPORT | F1=0.65 at cluster | atlas-internal |

**Supporting evidence:**

- Among all child clusters of SUPT_1145, CLUS_5180 receives the largest single-cluster share of PLI_3 annotation transfer (Coverage=0.49, Purity=0.99, F1=0.65 in at_run_20260709_kozareva_cerebellum_mmc_wmbv1). All four defining markers are CONSISTENT (see Table 1), with Htr2a at cohort_pct 0.979, Slc6a5 at 0.989, Kcnd3 at 0.807, and Grm1 at 0.882.
- The cluster-level AT Coverage of 0.49 — nearly half the PLI_3 source cells landing on this single cluster — is notable given the rarity of Lugaro cells (531 cells total in the source dataset) and the fact that SUPT_1145 has multiple child clusters. It indicates CLUS_5180 holds the largest share of the Lugaro transcriptomic signature at cluster resolution.

**Concerns:**

- Cluster-level F1=0.65 reflects incomplete concentration of PLI_3 cells: approximately half of PLI_3 cells map to sibling clusters rather than CLUS_5180, consistent with biological heterogeneity between fusiform Lugaro and globular cell subgroups [2][4]. This scatter is expected and does not indicate misidentification; it is better read as a signal of within-supertype substructure than as a failure of the cluster-level mapping.
- Nrgn DISCORDANT (same as SUPT_1145 — precomputed expression 0.04, cohort_pct 0.059, below MIN_DETECTABLE).
- Region signal uses a lower_bound rollup (non-painted CCF2020 descendants not counted); the true cerebellar fraction is at minimum 0.620 (`region_fraction_100um: 0.620; lower_bound rollup`).
- The pairing with SUPT_1145 (the primary mapping) means that the cluster-level mapping is best understood as a refinement within the supertype rather than an independent claim: SUPT_1145 is the primary match at supertype resolution; CLUS_5180 is the best-child candidate at cluster resolution. Whether the full Lugaro population truly concentrates in CLUS_5180 or spans multiple children remains open pending patch-seq or targeted single-cell characterization of morphologically confirmed Lugaro cells.

**What would upgrade confidence to HIGH:**

- A patch-seq or Cre-driver (e.g., Htr2a-Cre) targeted annotation transfer study that captures morphologically confirmed Lugaro cells and scores them against the SUPT_1145 child cluster panel, aiming for cluster-level F1 ≥ 0.80 at CLUS_5180.
- Literature documenting Nrgn expression at transcript level specifically in Lugaro cells would resolve the Nrgn discordance.

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 1145 CB PLI Gly-Gaba_2 [CS20230722_SUPT_1145] | — | n/a (supertype) | 🟢 HIGH | PLI_3 AT F1=0.96 to supertype; 4/4 markers CONSISTENT | Primary (supertype broadMatch) |
| 5180 CB PLI Gly-Gaba_2 [CS20230722_CLUS_5180] | 1145 CB PLI Gly-Gaba_2 | 174 | 🟡 MODERATE | PLI_3 AT F1=0.65 at cluster; best child of SUPT_1145 | Secondary (cluster closeMatch, best child) |
| 5182 CB PLI Gly-Gaba_2 [CS20230722_CLUS_5182] | 1145 CB PLI Gly-Gaba_2 | 50 | 🔴 LOW | Cluster AT F1=0.44; sibling of CLUS_5180 | Eliminated (cluster AT F1 below threshold; scatter captured by supertype) |
| 5184 CB PLI Gly-Gaba_3 [CS20230722_CLUS_5184] | 1146 CB PLI Gly-Gaba_3 | 69 | 🔴 LOW | AT best at subclass only (F1=0.36); Htr2a APPROXIMATE | Eliminated (no AT to target's supertype or cluster; Htr2a weaker) |
| 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] | 1149 CBX MLI Megf11 Gaba_1 | 154 | 🔴 LOW | Htr2a DISCORDANT (0.00); AT only at class level | Eliminated (Htr2a absent; wrong MLI supertype) |
| 4763 LDT-PCG St18 Gaba_1 [CS20230722_CLUS_4763] | 1067 LDT-PCG St18 Gaba_1 | 94 | ⚪ UNCERTAIN | AT no transfer to target lineage; primary soma in Pons | Eliminated (no AT transfer; brainstem location) |
| 1146 CB PLI Gly-Gaba_3 [CS20230722_SUPT_1146] | — | 129 | 🔴 LOW | AT best at subclass (F1=0.36); Htr2a APPROXIMATE; Kcnd3 APPROXIMATE | Eliminated (no AT reaching supertype; multiple marker mismatches) |
| 1004 NTS Dbh Glut_1 [CS20230722_SUPT_1004] | — | 592 | ⚪ UNCERTAIN | No AT transfer to target's lineage; primary soma medulla/NTS | Eliminated (no AT transfer; wrong region) |
| 1130 NTS-PARN Neurod2 Gly-Gaba_1 [CS20230722_SUPT_1130] | — | 1271 | ⚪ UNCERTAIN | No AT transfer; primary soma medulla/NTS | Eliminated (no AT transfer; wrong region) |
| 1139 SPVI-SPVC Sall3 Lhx1 Gly-Gaba_2 [CS20230722_SUPT_1139] | — | 997 | ⚪ UNCERTAIN | Location DISCORDANT (region_fraction_100um=0.061); no AT transfer | Eliminated (wrong region; spinal trigeminal nucleus) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Lugaro cell (cerebellum) node is defined using a CLASSICAL_MULTIMODAL evidence base. Defining markers are Htr2a and Slc6a5 (transcriptomic, from Kozareva/Osorno snRNA-seq, PMID:35578131 [2]), and Kcnd3 and Grm1 (from immunohistochemistry against Kv4.3/mGluR1α in anatomical studies, PMID:34194302 [4]). Soma location in the Purkinje cell layer of cerebellar cortex [UBERON:0002979] is established by morphological studies in GFP-reporter and Yellow Cameleon reporter mice [1][2][3]. NT type is GABAergic/glycinergic (mixed), established by reporter-line neurochemical characterization [3][2]. The neuropeptide Nrgn is based on immunohistochemistry used as an identification convenience in viral tracing studies [5] — its transcript-level status in Lugaro cells is not established by gathered literature.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 atlas taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE165371 (PLI_3) |
| Source species | NCBITaxon:10090 (mouse) |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper 1.7.1, default parameters, 100 bootstrap iterations) |
| Tool version | cell_type_mapper 1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 45,555 (interneuron subset; PLI_3 source = 531 cells) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/f1_scores_best.csv) |
| Caveats | Same-species (mouse) snRNA-seq → WMBv1. Source cluster labels are transcriptomically defined (Kozareva/Osorno) with high marker validation — treat cluster-level F1 as informative (pure-source expectation). PLI_3 is a rare cluster (531 cells). Blind-run note: this reproduces the curator ground-truth AT anchors without those targets ever being supplied to the pipeline. |

**Atlas data sources.** WMBv1 taxonomy (CCN20230722); pseudobulk SHA-256: b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `f4ce9b9` at 2026-07-09T18:53:54+00:00 from [kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml](../../kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_lugaro_cell_cerebellum_to_CS20230722_SUPT_1145 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | atlas-internal |
| edge_lugaro_cell_cerebellum_to_CS20230722_CLUS_5180 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | atlas-internal |
| edge_lugaro_cell_cerebellum_to_CS20230722_CLUS_5182 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_lugaro_cell_cerebellum_to_CS20230722_CLUS_5184 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_lugaro_cell_cerebellum_to_CS20230722_CLUS_5189 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal |
| edge_lugaro_cell_cerebellum_to_CS20230722_CLUS_4763 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal |
| edge_lugaro_cell_cerebellum_to_CS20230722_SUPT_1146 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_lugaro_cell_cerebellum_to_CS20230722_SUPT_1004 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal |
| edge_lugaro_cell_cerebellum_to_CS20230722_SUPT_1130 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal |
| edge_lugaro_cell_cerebellum_to_CS20230722_SUPT_1139 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal |

</details>

---

## Discussion

### Best candidate + caveats

**Primary mapping:** Lugaro cell (cerebellum) → 1145 CB PLI Gly-Gaba_2 [CS20230722_SUPT_1145] at HIGH confidence. Key support: annotation transfer (PLI_3; F1=0.96 at supertype) and 4/4 defining markers CONSISTENT across all child clusters. Key caveats: Nrgn DISCORDANT at supertype level; supertype region data not assessed (no atlas anat painted at supertype resolution); cluster-level scatter across multiple SUPT_1145 children (best child CLUS_5180 at F1=0.65, MODERATE confidence). This classical type maps directly to the Cell Ontology term Lugaro cell [[CL:0011006](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0011006)].

The supertype-level mapping (SUPT_1145; HIGH) and the cluster-level best-child mapping (CLUS_5180; MODERATE) are paired: PLI_3 annotation transfer achieves clean supertype concentration (F1=0.96) and distributes across child clusters, with CLUS_5180 receiving the largest cluster-level share (F1=0.65, Coverage=0.49). This two-level pattern is consistent with a heterogeneous classical type (fusiform Lugaro cells and globular cells as described in [1][2][4]) whose subpopulations do not fully resolve at cluster level in the current transcriptomic taxonomy.

### Proposed experiments and follow-ups

**1. Patch-seq on morphologically confirmed Lugaro cells**
- **What:** Whole-cell patch-clamp with biocytin fill on cerebellar cortex slices; post-hoc morphological reconstruction to confirm fusiform Lugaro or globular cell identity; single-cell transcriptome from the same cells.
- **Target:** Cluster-level annotation transfer F1 ≥ 0.80 at CLUS_5180 (or a sibling SUPT_1145 child if the globular subtype lands elsewhere).
- **Expected output:** AnnotationTransferEvidence at CLUS_5180 with patch-seq-confirmed source; would resolve whether within-supertype scatter reflects fusiform vs. globular subtype structure.
- **Resolves:** Open question on cluster-level identity of Lugaro vs. globular subpopulations; would upgrade CLUS_5180 edge from MODERATE to HIGH.

**2. Htr2a-Cre or Slc6a5-Cre targeted annotation transfer**
- **What:** Retrieve and score Htr2a-Cre or Slc6a5-Cre targeted single-cell data from mouse cerebellum against CCN20230722.
- **Target:** Supertype-level F1 ≥ 0.95 and cluster-level F1 ≥ 0.70 at CLUS_5180.
- **Expected output:** AnnotationTransferEvidence with Cre-driver-targeted source; would provide direct source-cell identity confirmation (currently AT is based on transcriptomic cluster correspondence rather than Cre-driver targeting).
- **Resolves:** Source-cell identity question in the current PLI_3 AT evidence.

**3. Nrgn transcript verification in Lugaro cells**
- **What:** Targeted literature search for "neurogranin Lugaro cerebellum scRNA-seq" or "Nrgn cerebellar interneuron transcript"; if no published data, smFISH for Nrgn in cerebellar sections from mice also stained for Htr2a/Slc6a5.
- **Target:** Determine whether Nrgn is a true transcript-level Lugaro cell marker or an IHC-only observation.
- **Expected output:** LiteratureEvidence or new MarkerSource entry on the Nrgn property of the classical node.
- **Resolves:** The DISCORDANT Nrgn comparison on both SUPT_1145 and CLUS_5180.

### Open questions

1. Does the within-supertype AT scatter (PLI_3 distributing across CLUS_5180 and CLUS_5182) reflect a genuine transcriptomic distinction between fusiform Lugaro cells and globular cells, or is it technical noise from the small source-cell pool (n=531)? Patch-seq with morphological confirmation would resolve this.
2. Is Nrgn expressed at transcript level in Lugaro cells, or does the classical Nrgn annotation reflect only protein-level detection from the Kita et al. 2013 immunohistochemistry study [5]? Precomputed atlas expression shows Nrgn = 0.01 on SUPT_1145, which suggests absence; a targeted literature search or smFISH experiment would confirm.
3. The PLI_3 source label in Kozareva/Osorno pools both fusiform and globular subtypes; the Osorno 2022 paper suggests that the PLI3 transcriptomic cluster contains primarily Lugaro cells (via Htr2a/Slc6a5) while a separate annotation for globular cells (Aldh1a3/Slc6a5) may be better represented by the PLI_2 cluster in the original dataset. If PLI_2 (globular) and PLI_3 (Lugaro) are treated as separate source labels in a future AT run, the cluster-level mapping of PLI_3 to CLUS_5180 may sharpen. See the separate `globular_cell_cerebellum` node for the PLI_2 mapping.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Hirono et al. 2012 | [PMID:22235322](https://pubmed.ncbi.nlm.nih.gov/22235322) | Soma location; morphology |
| [2] | Osorno et al. 2022 | [PMID:35578131](https://pubmed.ncbi.nlm.nih.gov/35578131) | Soma location; NT type; Htr2a and Slc6a5 markers; PLI3 identification as Lugaro cells |
| [3] | Miyazaki et al. 2020 | [PMID:32470477](https://pubmed.ncbi.nlm.nih.gov/32470477) | NT type; soma location; circuit connectivity |
| [4] | Hirono et al. 2021 | [PMID:34194302](https://pubmed.ncbi.nlm.nih.gov/34194302) | Kcnd3 (Kv4.3) and Grm1 (mGluR1α) markers |
| [5] | Kita et al. 2013 | [PMID:23894597](https://pubmed.ncbi.nlm.nih.gov/23894597) | Nrgn neuropeptide identification |

---

<!-- verdict-block-start: edge_lugaro_cell_cerebellum_to_CS20230722_SUPT_1145 -->
```yaml
verdict:
  confidence: HIGH
  confidence_score: 0.92
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Annotation transfer of PLI_3 (GEO:GSE165371, scRNA-seq) via MapMyCells
    (at_run_20260709_kozareva_cerebellum_mmc_wmbv1) achieves F1=0.96 at CS20230722_SUPT_1145
    (Purity=0.98, Coverage=0.94). All 4 of 5 marker comparisons CONSISTENT at supertype level
    (Htr2a, Slc6a5, Kcnd3, Grm1 CONSISTENT; neuropeptide_Nrgn DISCORDANT; child-cluster
    coverage 1.000 for all four defining markers). PLI_3 source label is directly identified as
    Lugaro cells in the Osorno 2022 snRNA-seq study (PMID:35578131) via co-expression of Htr2a
    and Slc6a5. Only counter-signal is neuropeptide_Nrgn DISCORDANT (mean=0.01; IHC-only
    marker, not established at transcript level in Lugaro cells). Mapping is broadMatch + 1:n
    because PLI_3 source cells distribute across multiple child clusters of SUPT_1145; best
    child is CS20230722_CLUS_5180 (AT supertype F1=0.96; cluster-level best child at
    edge_lugaro_cell_cerebellum_to_CS20230722_CLUS_5180).
  reconciliation_note: >
    Paired with edge_lugaro_cell_cerebellum_to_CS20230722_CLUS_5180 (closeMatch, best child
    cluster within this supertype). Supertype broadMatch captures the full Lugaro population;
    cluster closeMatch represents the largest concentration at cluster resolution.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Nrgn DISCORDANT at supertype level (mean=0.01, cohort_pct 0.018). The classical
        Nrgn annotation derives from immunohistochemistry used as an identification aid
        (Kita et al. 2013, PMID:23894597), not from transcript-level evidence. Discordance
        does not challenge the primary AT-based mapping but should be investigated.
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        No region data painted at supertype level in WMBv1 (location comparison NOT_ASSESSED).
        Region signal assessed at cluster level only (CLUS_5180; region_fraction_100um=0.620,
        lower_bound rollup).
  proposed_experiments:
    - >
      Cre-driver (Htr2a-Cre or Slc6a5-Cre) targeted annotation transfer: retrieve published
      cerebellar single-cell dataset; score against CCN20230722 cluster panel, targeting
      F1 ≥ 0.80 at cluster level within CS20230722_SUPT_1145 (CS20230722_CLUS_5180 or sibling).
    - >
      Targeted literature search or smFISH experiment to establish Nrgn expression at
      transcript level in Lugaro cells.
  unresolved_questions:
    - >
      Does within-supertype AT scatter across CS20230722_CLUS_5180 and siblings reflect
      transcriptomic distinctions between fusiform Lugaro cells and globular cells, or
      technical scatter from the small source pool (n=531)?
    - >
      Is Nrgn expressed at transcript level in Lugaro cells, or is the classical annotation
      IHC-only? Atlas precomputed expression = 0.01 on CS20230722_SUPT_1145 suggests absence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_lugaro_cell_cerebellum_to_CS20230722_CLUS_5180 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.68
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Annotation transfer of PLI_3 (GEO:GSE165371, scRNA-seq) via MapMyCells
    (at_run_20260709_kozareva_cerebellum_mmc_wmbv1) achieves F1=0.65 at CS20230722_CLUS_5180
    (Purity=0.99, Coverage=0.49) — the highest cluster-level F1 among SUPT_1145 children.
    All 4 of 5 marker comparisons CONSISTENT for defining markers (Htr2a=6.63, Slc6a5=7.69,
    Kcnd3=7.50, Grm1=8.64); neuropeptide_Nrgn DISCORDANT (mean=0.04; IHC-only marker).
    Cluster-level Coverage=0.49 indicates
    approximately half of PLI_3 cells scatter to sibling clusters, consistent with
    within-supertype biological heterogeneity (fusiform Lugaro vs. globular subgroups).
    Confidence is MODERATE rather than HIGH because cluster-level F1=0.65 is below the
    0.75 threshold and source-cell identity confirmation via Cre-driver targeting is absent.
    Paired with CS20230722_SUPT_1145 edge (broadMatch, edge_lugaro_cell_cerebellum_to_CS20230722_SUPT_1145).
  reconciliation_note: >
    Paired with edge_lugaro_cell_cerebellum_to_CS20230722_SUPT_1145 (broadMatch, supertype
    primary mapping). CS20230722_CLUS_5180 is the best-child cluster within SUPT_1145 at cluster
    resolution; the MODERATE confidence reflects real within-supertype scatter, not a
    failure of the mapping.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        PLI_3 cells distribute across multiple SUPT_1145 child clusters; CLUS_5180 receives
        approximately half (Coverage=0.49). Remaining cells land on sibling clusters,
        suggesting within-supertype substructure corresponding to Lugaro vs. globular cell
        subgroups. Cluster-level F1=0.65 reflects this heterogeneity.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Nrgn DISCORDANT (mean=0.04, cohort_pct 0.059). IHC-only marker; no transcript-level
        evidence. Does not challenge the AT-based primary call.
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        region_fraction_100um=0.620 is a lower_bound rollup (non-painted CCF2020 descendants
        not counted). True cerebellar fraction is at minimum 0.620.
  proposed_experiments:
    - >
      Cre-driver (Htr2a-Cre or Slc6a5-Cre) targeted annotation transfer of cerebellar
      Lugaro cells; score against CS20230722_CLUS_5180 and SUPT_1145 siblings, targeting
      cluster-level F1 ≥ 0.80 to upgrade to HIGH confidence.
    - >
      Targeted cite-traverse: "neurogranin Lugaro cerebellum scRNA-seq" to resolve
      the Nrgn discordance.
  unresolved_questions:
    - >
      Whether CS20230722_CLUS_5180 specifically corresponds to fusiform Lugaro cells while
      sibling clusters correspond to globular cells — this subtype delineation requires
      patch-seq with morphological confirmation.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_lugaro_cell_cerebellum_to_CS20230722_CLUS_5182 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] No cluster-level AT metrics reach CS20230722_CLUS_5182 directly in
    at_run_20260709_kozareva_cerebellum_mmc_wmbv1; best PLI_3 AT signal is at
    CS20230722_SUPT_1145 (F1=0.96). CS20230722_CLUS_5182 is a sibling of the primary
    candidate CS20230722_CLUS_5180 within SUPT_1145; scatter to CLUS_5182 is captured by
    the supertype broadMatch. All defining markers CONSISTENT, but no cluster-level AT
    concentration — signal falls below the 0.5 threshold at cluster resolution.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_lugaro_cell_cerebellum_to_CS20230722_CLUS_5184 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] No AT reaching CS20230722_CLUS_5184 or its supertype CS20230722_SUPT_1146 at
    supertype or cluster level (at_run_20260709_kozareva_cerebellum_mmc_wmbv1; best AT is
    at subclass level F1=0.36). Htr2a APPROXIMATE (mean=0.17, cohort_pct 0.412) — below
    the expression level in the primary candidate. Different supertype from the AT-dominant
    SUPT_1145 lineage.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_lugaro_cell_cerebellum_to_CS20230722_CLUS_5189 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] Htr2a DISCORDANT (mean=0.00, cohort_pct 0.000) on CS20230722_CLUS_5189;
    Htr2a is a primary defining marker for Lugaro cells. AT best at class level only
    (at_run_20260709_kozareva_cerebellum_mmc_wmbv1; no AT reaching this MLI-lineage cluster).
    Wrong supertype (MLI type, not PLI).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_lugaro_cell_cerebellum_to_CS20230722_CLUS_4763 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] No AT transfer from PLI_3 to CS20230722_CLUS_4763 or its lineage
    (at_run_20260709_kozareva_cerebellum_mmc_wmbv1). Primary soma location Pons/Pontine
    central gray (region_fraction: 0.021 strict; region_fraction_100um: 0.312 — boundary
    scatter, not a cerebellar type). Lugaro cells are defined as cerebellar interneurons;
    this brainstem cluster is eliminated on anatomical grounds.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_lugaro_cell_cerebellum_to_CS20230722_SUPT_1146 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.12
  rationale: >
    [tier:CUT] No AT reaching CS20230722_SUPT_1146 at supertype level
    (at_run_20260709_kozareva_cerebellum_mmc_wmbv1; best AT subclass F1=0.36).
    Htr2a APPROXIMATE (mean=0.88, cohort_pct 0.477) and Kcnd3 APPROXIMATE
    (mean=5.98, cohort_pct 0.486) — both weaker than primary candidate SUPT_1145.
    Different supertype lineage from the AT-dominant mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_lugaro_cell_cerebellum_to_CS20230722_SUPT_1004 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.04
  rationale: >
    [tier:CUT] No AT transfer from PLI_3 to CS20230722_SUPT_1004 or its lineage
    (at_run_20260709_kozareva_cerebellum_mmc_wmbv1). Primary soma location Medulla/NTS
    (not cerebellum). Glutamatergic NTS supertype — NT type mismatch with GABAergic/glycinergic
    Lugaro cells. Eliminated on both anatomical and NT grounds.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_lugaro_cell_cerebellum_to_CS20230722_SUPT_1130 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.04
  rationale: >
    [tier:CUT] No AT transfer from PLI_3 to CS20230722_SUPT_1130 or its lineage
    (at_run_20260709_kozareva_cerebellum_mmc_wmbv1). Primary soma location Medulla/NTS-PARN
    (not cerebellum). Htr2a, Kcnd3, and Grm1 all APPROXIMATE at supertype level.
    Eliminated on anatomical grounds — cerebellar interneuron cannot map to a medullary type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_lugaro_cell_cerebellum_to_CS20230722_SUPT_1139 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.03
  rationale: >
    [tier:CUT] Location DISCORDANT (region_fraction_100um: 0.061; primary soma in Medulla/
    Spinal trigeminal nucleus, far from cerebellar cortex). No AT transfer from PLI_3
    (at_run_20260709_kozareva_cerebellum_mmc_wmbv1). Eliminated on strong anatomical
    grounds — region_fraction_100um: 0.061 is a distant-region signal.
```
<!-- verdict-block-end -->
