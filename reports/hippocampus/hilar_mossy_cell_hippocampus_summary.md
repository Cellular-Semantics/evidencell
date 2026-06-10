# Hilar mossy cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

## Introduction

Hilar mossy cells are large glutamatergic projection neurons resident in the dentate gyrus polymorph layer, with proximal dendrites bearing the thorny excrescences that gave them their name and axons projecting widely within the inner molecular layer of the ipsi- and contralateral dentate gyrus [1][3][5]. They constitute the major non-granule excitatory population of the dentate hilus and provide feedback excitation onto granule cells, so their atlas correspondence anchors hilar-circuit interpretation of dentate transcriptomic data.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | dentate gyrus polymorphic layer [UBERON:0002928]; dentate gyrus of hippocampal formation [UBERON:0001885]; inner molecular layer [UBERON:0022347]; middle molecular layer [UBERON:0022346] (dorsal mossy cells only) | [1][2][3][4] |
| NT | glutamatergic | [3][4][5][1] |
| Defining markers | Gria4, Dkk3, Slc17a7, Drd2, Calcrl, Reln | [6][1][7][8] |
| Negative markers | Gad1 | — |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location & morphology:** Scharfman & Myers 2013 · practical definition · [3]
  > A cell body in the hilus, defined as zone 4 of Amaral (1978). Glutamate as the primary transmitter (other markers are less valuable, as discussed below). An axon that innervates the inner molecular layer.
  > — Scharfman & Myers 2013, WHAT IS A MOSSY CELL? A PRACTICAL DEFINITION · [3] <!-- quote_key: 11290620_d7c0cc69 -->
- **Soma location & morphology:** Botterill et al. 2021 · viral axon labelling · [1]
  > Hilar mossy cells (MCs) are large glutamatergic neurons that innervate both GCs and inhibitory GABAergic neurons within the DG (Scharfman, 2016)(Scharfman et al., 2013). MCs make up the majority of hilar neurons, and are known for their complex spines called thorny excrescences (Scharfman, 2016)(Scharfman et al., 2013). They have dendrites mainly in the hilus and their axon projects to locations within the DG. Near the cell body the axon makes collaterals that terminate mainly in the hilus. Distal to the cell body the axon terminates at many septotemporal levels. There is also a commissural projection that terminates in the contralateral DG (Scharfman et al., 2013)
  > — Botterill et al. 2021, Mossy Cells: Specialized Glutamatergic Neurons · [1] <!-- quote_key: 231953329_132cf2e1 -->
- **Dorsal/ventral axon target heterogeneity:** Botterill et al. 2021 · [1]
  > dorsal MC axons are an exception to this rule. We used two mouse lines that allow for Cre‐dependent viral labeling of MCs and their axons: dopamine receptor D2 (Drd2‐Cre) and calcitonin receptor‐like receptor (Crlr‐Cre). A single viral injection into the dorsal DG to label dorsal MCs resulted in labeling of MC axons in both the IML and middle molecular layer (MML)
  > — Botterill et al. 2021, Mossy Cells: Specialized Glutamatergic Neurons · [1] <!-- quote_key: 231953329_ceaf8acb -->
- **Glutamatergic identity:** Sun et al. 2017 · [4]
  > Hilar mossy cells are the prominent glutamatergic cell type in the dentate hilus of the dentate gyrus (DG)
  > — Sun et al. 2017, Mossy Cells: Specialized Glutamatergic Neurons · [4] <!-- quote_key: 3583187_ea3794f5 -->
- **Glutamatergic identity (anatomical + physiological convergence):** Scharfman & Myers 2013 · [3]
  > Two studies provided evidence that mossy cells were glutamatergic, one anatomical and the second physiological. The first anatomical demonstration of glutamate immunoreactivity was made in Golgi-impregnated mossy cells (Soriano et al., 1994). The physiological study used hippocampal slices to impale mossy cells-which were confirmed to be regular-spiking, hilar, and had thorny excrescences-and simultaneously recorded from neurons in the granule cell layer until a monosynaptic connection was identified. That study showed for the first time that mossy cells produced unitary EPSPs in granule cells, supporting the hypothesis that mossy cells were glutamatergic (Scharfman, 1995).
  > — Scharfman & Myers 2013, Mossy Cells: Specialized Glutamatergic Neurons · [3] <!-- quote_key: 11290620_a475a601 -->
- **Slc17a7 (Vglut1) marker:** Sarvari et al. 2016 · [6]
  > From the three known vesicular glutamate transporters (vGLUT1-3), vGLUT1 is the main subtype expressed in the hippocampus (Fremeau et al., 2004). It packs glutamate into synaptic vesicles of the glutamatergic axon terminals.
  > — Sarvari et al. 2016, Synaptic Properties and Neurotransmitter Systems · [6] <!-- quote_key: 14854554_ed1bdc00 -->
- **Drd2 marker:** Godino et al. 2023 · [7]
  > glutamatergic neurons represented 45.1% of all D1 or D2 cells in vHipp, in stark contrast to more dorsal parts of hippocampus where -barring D2-positive hilar mossy cells -D1 or D2 cells are almost exclusively interneurons (Gangarossa et al., 2012) (Puighermanal et al., 2015)(Puighermanal et al., 2016) . While GABAergic clusters readily mapped to canonical neuropeptide-defined interneuron cell types 40 , glutamatergic pyramidal neuron classification was not as clear-cut: we hypothesize that pyramidal neuron clusters might generally correspond to projection-specific vCA1/vSub populations.
  > — Godino et al. 2023, Specialized Glutamatergic Populations · [7] <!-- quote_key: 260336826_494cac70 -->
- **Reln marker (hilar mossy cells predominantly glutamatergic):** Yu et al. 2014 · [8]
  > Results of the present study showed that reelin-positive cells that were GABAergic or glutamatergic increased in density with increasing age. Moreover, these cells were both GABAergic and glutamatergic. Reelin-positive mossy cells in the dentate hilus were predominantly glutamatergic, but in the molecular layer of the dentate gyrus, reelin-positive cells that were GABAergic and glutamatergic showed a spatiotemporal pattern.
  > — Yu et al. 2014, Specialized Glutamatergic Populations · [8] <!-- quote_key: 7981953_7f1ea74e -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: dentate gyrus neuron [[CL:4023062](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023062)] (BROAD).

**Proposed CL term:** *hilar mossy cell* (SUBMITTED)
> A dentate gyrus neuron with soma in the polymorphic layer (UBERON:0002928) (Scharfman & Myers, 2012), capable of glutamate secretion as a neurotransmitter (Scharfman & Bernstein, 2015). Distinguished by a large multipolar soma, thorny excrescences on proximal dendrites, and commissural/associational axon projections terminating in the inner molecular layer of the dentate gyrus (Scharfman & Myers, 2012). Electrophysiologically characterised by a depolarised resting membrane potential, prominent hyperpolarisation-activated cation current (Ih), and firing accommodation (Scharfman & Myers, 2012). In rodents, serves as a major excitatory neuron of the dentate hilus providing feedback excitation to granule cells (Sun et al., 2017).
> — Proposed CL term draft (curator-authored) · [3][5][4]

---

## Results

Annotation transfer of two distinct Hochgerner 2018 hilar source labels onto WMBv1 — Mossy-Adcyap1 and Mossy-Cyp26b1 — converges on a paired-supertype mapping for the classical hilar mossy cell: 0079 CA3 Glut_5 [CS20230722_SUPT_0079] captures the Adcyap1+ subtype with hilar-dominant atlas anatomy, and 0078 CA3 Glut_4 [CS20230722_SUPT_0078] captures the Cyp26b1+ subtype but with atlas anatomy that registers to the CA3 pyramidal layer rather than the hilus (see filtered AT figure and property comparison tables). The Adcyap1+ side resolves to a single best cluster, 0317 CA3 Glut_5 [CS20230722_CLUS_0317], whose hilar location is unambiguous; the Cyp26b1+ side has the strongest transcriptomic signal of the run but its anatomy is the principal unresolved point.

![Filtered AT figure for hilar mossy cell](figures/f1_for_hilar_mossy_cell_hippocampus.png)

*F1 across taxonomy levels for the two hilar mossy-cell source groups from Hochgerner 2018 (Mossy-Adcyap1, n=28; Mossy-Cyp26b1, n=34). Each row is one source label; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. F1 >= 0.5 indicates a clean mapping at that resolution. Both supertypes lie inside the 017 CA3 Glut subclass at supertype rank, but split cleanly into two non-overlapping supertypes — SUPT_0079 (F1=0.83 for Mossy-Adcyap1) and SUPT_0078 (F1=0.94 for Mossy-Cyp26b1) — consistent with the Hochgerner 2018 report of three molecularly distinct hilar mossy-cell subtypes.*

### 0079 CA3 Glut_5 [CS20230722_SUPT_0079] · 🟢 HIGH

#### Property comparison

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | dentate gyrus polymorphic layer [UBERON:0002928] | Dentate gyrus, polymorph layer [MBA:10704] count_100um=1524; region_fraction_100um=0.94 | Dentate gyrus, polymorph layer [MBA:10704] count_100um=1222; region_fraction_100um=0.99 (CLUS_0317) | CONSISTENT |
| NT type | glutamatergic | not asserted | Glut (CLUS_0317) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Gria4 expression | defining marker | 8.05; cohort_pct 0.667; child-coverage 1.000 | 8.03; cohort_pct 0.778 (CLUS_0317) | CONSISTENT |
| Dkk3 expression | defining marker | 5.32; cohort_pct 0.733; child-coverage 1.000 | 7.34; cohort_pct 0.852 (CLUS_0317) | CONSISTENT |

*(2 of 2 child clusters of SUPT_0079 (CLUS_0316, CLUS_0317) show concordant Gria4 and Dkk3 expression at child-coverage 1.000; the AT-best child is CLUS_0317.)*

#### Evidence support

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Hochgerner 2018 AT (Mossy-Adcyap1) | Annotation transfer | SUPPORT | F1=0.83 at SUPERTYPE (20/27 cells); purity=0.95 | atlas-internal |

#### Supporting evidence

- Annotation transfer from the Hochgerner 2018 mouse dentate gyrus single-cell dataset, run locally against the WMBv1 precomputed-stats reference, lands 20 of 27 Mossy-Adcyap1 cells on SUPT_0079 at F1=0.83, with purity 0.95 — i.e. SUPT_0079 cells captured by the transfer come almost exclusively from this source label.
- Atlas anatomy is decisively hilar: of 1619 SUPT_0079 cells painted within the 100µm neighbourhood, 1524 sit in the dentate polymorph layer (MBA:10704), the canonical mossy-cell soma compartment, with `region_fraction_100um: 0.936` and strict in-region `region_fraction: 0.668`.
- Defining markers Gria4 and Dkk3 are both expressed at supertype level with cohort percentiles 0.67 and 0.73 respectively, and child-cluster coverage of 1.000 across the two SUPT_0079 children (CLUS_0316, CLUS_0317).

#### Concerns

- Atlas-side NT type is not asserted at supertype level (`NT_PREDICTION_UNCERTAIN`); cluster-level Glut annotation is consistent.
- AT evidence derives from a single source dataset (`SINGLE_DATASET`); independent dentate-gyrus replication has not been performed.
- Hochgerner 2018 identifies three molecular mossy-cell subtypes (Cyp26b1, Adcyap1, Klk8); SUPT_0079 captures only the Adcyap1+ subtype (`AMBIGUOUS_MAPPING`). Mossy-Klk8 (n=6) maps ambiguously across CA3 supertypes with insufficient evidence for a dedicated edge.

#### What would upgrade confidence

- Independent mouse dentate gyrus annotation transfer targeting F1 >= 0.80 at SUPERTYPE level on CS20230722_SUPT_0079, ideally from a separately collected and dissected hilar dataset.
- ISH co-labelling of Cyp26b1 and Adcyap1 in dentate hilus to confirm non-overlapping expression and validate the two-supertype split between SUPT_0078 and SUPT_0079.

### 0317 CA3 Glut_5 [CS20230722_CLUS_0317] · 🟢 HIGH

#### Property comparison

| Property | Classical | Supertype (SUPT_0079) | Best cluster (CLUS_0317) | Alignment |
|---|---|---|---|---|
| Soma location | dentate gyrus polymorphic layer [UBERON:0002928] | count_100um=1524 in MBA:10704; region_fraction_100um=0.94 | count_100um=1222 in MBA:10704; region_fraction_100um=0.99 | CONSISTENT |
| NT type | glutamatergic | not asserted | Glut | CONSISTENT |
| Gria4 expression | defining marker | 8.05; cohort_pct 0.667 | 8.03; cohort_pct 0.778 | CONSISTENT |
| Dkk3 expression | defining marker | 5.32; cohort_pct 0.733 | 7.34; cohort_pct 0.852 | CONSISTENT |

*Within SUPT_0079, CLUS_0317 leads on hilar fraction (`region_fraction_100um: 0.991` vs CLUS_0316's 0.604) and on Dkk3 (cohort percentile 0.852 vs 0.630); the supertype-level AT signal scatters across both children, with CLUS_0317 carrying the larger share at cluster rank.*

#### Evidence support

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| WMBv1 atlas metadata | Atlas metadata | PARTIAL | region_fraction_100um=0.991; strict region_fraction=0.835 | atlas-internal |

#### Supporting evidence

- The cluster's 1222 of 1231 painted cells in the 100µm neighbourhood lie in the dentate polymorph layer (MBA:10704), a tighter localisation to the hilus than the parent supertype: strict `region_fraction: 0.835` and proximity `region_fraction_100um: 0.991`.
- Gria4 expression at 8.03 (cohort percentile 0.778) and Dkk3 at 7.34 (cohort percentile 0.852) place CLUS_0317 in the top quartile of the survival cohort for both markers and well above its sibling cluster CLUS_0316 for Dkk3 (3.30).
- AT support is inherited from the parent supertype SUPT_0079 edge; the Mossy-Adcyap1 cells that landed at supertype level distribute across SUPT_0079's two children, with CLUS_0317 leading the cluster-rank distribution.

#### Concerns

- Cluster-level AT n is small (n=15 Mossy-Adcyap1 cells; `LOW_CELL_COUNT`); independent replication is needed before treating CLUS_0317 as a 1:1 atlas correspondent rather than the strongest child within SUPT_0079.
- Adcyap1+ cells scatter to the sibling CLUS_0316 as well as CLUS_0317 (`DISTRIBUTED_ACROSS_CLUSTERS`); the supertype-level mapping is the primary call, the cluster-level call is the best-child refinement.
- AT evidence is from a single source dataset (`SINGLE_DATASET`).

#### What would upgrade confidence

- Independent mouse dentate gyrus annotation transfer targeting F1 >= 0.80 at CLUSTER level on CS20230722_CLUS_0317, ideally with hilar-enriched dissection to increase the Adcyap1+ source cell count.

### 0078 CA3 Glut_4 [CS20230722_SUPT_0078] · 🟡 MODERATE

#### Property comparison

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | dentate gyrus polymorphic layer [UBERON:0002928] | Field CA3, pyramidal layer [MBA:495] count_100um=8918; region_fraction_100um=0.20 | not assessed (CLUS_0315 also CA3-pyramidal-dominant) | APPROXIMATE |
| NT type | glutamatergic | not asserted | Glut (CLUS_0315) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Gria4 expression | defining marker | 5.37; cohort_pct 0.267; child-coverage 1.000 | 5.12; cohort_pct 0.407 (CLUS_0315) | APPROXIMATE |
| Dkk3 expression | defining marker | 8.71; cohort_pct 0.933; child-coverage 1.000 | 8.94; cohort_pct 0.963 (CLUS_0315) | CONSISTENT |

*Child-cluster breakdown: both SUPT_0078 children show child-coverage 1.000 for Gria4 and Dkk3; Dkk3 is the stronger discriminator on the Cyp26b1+ side (supertype value 8.71 in the 93rd cohort percentile). Best AT child is CLUS_0315 (20 of 34 cells; F1=0.83 at cluster level).*

#### Evidence support

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Hochgerner 2018 AT (Mossy-Cyp26b1) | Annotation transfer | SUPPORT | F1=0.94 at SUPERTYPE (33/34 cells); purity=0.92 | atlas-internal |

#### Supporting evidence

- The Mossy-Cyp26b1 source label maps with the strongest signal in the run: 33 of 34 cells land on SUPT_0078 at F1=0.94, coverage 0.97, purity 0.92 — a near-complete subset relationship at supertype rank.
- Dkk3 is highly expressed at supertype level (8.71, cohort percentile 0.93) and on the AT-best child CLUS_0315 (8.94, cohort percentile 0.96), and child-coverage of 1.000 indicates that Dkk3 expression is uniform across the supertype's clusters.
- Gria4 is present but at lower cohort percentile (0.267 supertype, 0.407 best child), consistent with Hochgerner 2018's reading that the Cyp26b1+ mossy-cell subtype has a distinct transcriptomic profile from the Adcyap1+ subtype.

#### Concerns

- `DISCORDANT_ANATOMY`: SUPT_0078 atlas anatomy registers to Field CA3 pyramidal layer (MBA:495; `region_fraction_100um: 0.195`, strict `region_fraction: 0.040`) rather than the dentate polymorph layer. Two interpretations are open and not resolvable from atlas data alone: (i) the Cyp26b1+ mossy cells sit at the CA3c/hilus border and the spatial-registration step paints them onto CA3; (ii) SUPT_0078 also contains CA3 pyramidal cells sharing the Cyp26b1 transcriptomic profile, so the supertype is a composite. *(note: CA3c is adjacent to the dentate hilus and partial misregistration of CA3c cells into pyramidal-layer spatial paints is a known interpretive caveat; this does not resolve the question.)*
- Atlas-side NT type is not asserted at supertype level (`NT_PREDICTION_UNCERTAIN`); cluster-level Glut annotation is consistent.
- `SINGLE_DATASET`: AT evidence is from one source dataset; independent replication has not been performed.

#### What would upgrade confidence

- Spatial-transcriptomic validation of SUPT_0078 defining markers (Homer3, Cldn22) within the dentate hilus and at the CA3c boundary to test whether the supertype's soma positions span the CA3c/hilus border, which would explain the AT anatomy.
- Independent mouse dentate gyrus annotation transfer to confirm the Mossy-Cyp26b1 → SUPT_0078 assignment is reproducible across labs.

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0079 CA3 Glut_5 [CS20230722_SUPT_0079]` | — | 318 | 🟢 HIGH | Mossy-Adcyap1 AT F1=0.83; hilar anatomy | Primary |
| `0317 CA3 Glut_5 [CS20230722_CLUS_0317]` | `0079 CA3 Glut_5` | 116 | 🟢 HIGH | Hilar-dominant child of SUPT_0079; Dkk3 top quartile | Secondary (best child) |
| `0078 CA3 Glut_4 [CS20230722_SUPT_0078]` | — | 2147 | 🟡 MODERATE | Mossy-Cyp26b1 AT F1=0.94; anatomy on CA3 pyramidal | Secondary (paired subtype, anatomy caveat) |
| `0315 CA3 Glut_4 [CS20230722_CLUS_0315]` | `0078 CA3 Glut_4` | 1219 | 🔴 LOW | AT-best child of SUPT_0078 but CA3 pyramidal | Eliminated (CA3 pyramidal anatomy) |
| `0316 CA3 Glut_5 [CS20230722_CLUS_0316]` | `0079 CA3 Glut_5` | 202 | 🔴 LOW | Stratum-radiatum-dominant sibling within SUPT_0079 | Eliminated (off-hilus radiatum sibling) |
| `0507 DG Glut_2 [CS20230722_CLUS_0507]` | `0137 DG Glut_2` | 42250 | 🔴 LOW | Dentate granule cell layer anatomy | Eliminated (granule cell layer, not hilus) |
| `0508 DG Glut_3 [CS20230722_CLUS_0508]` | `0138 DG Glut_3` | 165 | 🔴 LOW | Dentate granule cell layer anatomy | Eliminated (granule cell layer, not hilus) |
| `0079 CA3 Glut_5 [CS20230722_SUPT_0079]` (legacy duplicate) | — | 318 | 🔴 LOW | Same accession as primary row; legacy edge ID | Eliminated (legacy/fresh-emit ID collision) |
| `0139 DG Glut_4 [CS20230722_SUPT_0139]` | — | 5166 | 🔴 LOW | DG granule cell layer; low Gria4/Dkk3 | Eliminated (granule cell layer, not hilus) |
| `0138 DG Glut_3 [CS20230722_SUPT_0138]` | — | 964 | 🔴 LOW | DG granule cell layer; low markers | Eliminated (granule cell layer, not hilus) |
| `0141 DG-PIR Ex IMN_2 [CS20230722_SUPT_0141]` | — | 1200 | 🔴 LOW | DG granule cell layer; immature-neuron supertype | Eliminated (immature neuron, granule layer) |
| `0137 DG Glut_2 [CS20230722_SUPT_0137]` | — | 74950 | 🔴 LOW | DG granule cell layer; low Gria4 (cohort percentile 0.067) | Eliminated (granule cell layer, not hilus) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Hilar mossy cell is defined here on the CLASSICAL_MULTIMODAL basis: soma in the dentate gyrus polymorph layer [UBERON:0002928] [1][2][3][4], glutamatergic neurotransmitter identity [3][4][5][1], defining transcript/protein markers Gria4, Dkk3, Slc17a7 [6], Drd2 [1][7], Calcrl [1], and Reln [8], and negative marker Gad1. The mossy-cell axon projects predominantly to the dentate inner molecular layer with a commissural component to the contralateral DG [1][3]; dorsal mossy cells additionally innervate the middle molecular layer [1].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE95315 (Hochgerner 2018 (GSE95315) mouse DG single-cell cell type labels: Granule-mature, Granule-immature, Mossy-Cyp26b1, Mossy-Adcyap1, Mossy-Klk8, Neuroblast 1, Neuroblast 2, Cajal-Retzius, GABA-Cnr1, GABA-Lhx6, Astrocytes.) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations). 2 genes unmapped. Per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 2934 (filtered to 2934) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `b95d284` at 2026-06-10T13:04:44+00:00 from [kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_hilar_mossy_cell_hippocampus_to_supt_0079 | ANNOTATION_TRANSFER | SUPPORT | atlas-internal |
| edge_hilar_mossy_cell_hippocampus_to_CS20230722_CLUS_0317 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hilar_mossy_cell_hippocampus_to_supt_0078 | ANNOTATION_TRANSFER | SUPPORT | atlas-internal |
| edge_hilar_mossy_cell_hippocampus_to_CS20230722_CLUS_0315 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hilar_mossy_cell_hippocampus_to_CS20230722_CLUS_0316 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hilar_mossy_cell_hippocampus_to_CS20230722_CLUS_0507 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hilar_mossy_cell_hippocampus_to_CS20230722_CLUS_0508 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hilar_mossy_cell_hippocampus_to_CS20230722_SUPT_0079 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hilar_mossy_cell_hippocampus_to_CS20230722_SUPT_0139 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hilar_mossy_cell_hippocampus_to_CS20230722_SUPT_0138 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hilar_mossy_cell_hippocampus_to_CS20230722_SUPT_0141 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hilar_mossy_cell_hippocampus_to_CS20230722_SUPT_0137 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Hilar mossy cell → 0079 CA3 Glut_5 [CS20230722_SUPT_0079] at HIGH confidence, with 0317 CA3 Glut_5 [CS20230722_CLUS_0317] as the best child cluster within the supertype. Key support: AT from Hochgerner 2018 Mossy-Adcyap1 (F1=0.83 at supertype rank, purity 0.95), with hilar atlas anatomy (`region_fraction_100um: 0.936` for the supertype, 0.991 for CLUS_0317). Key caveats: `SINGLE_DATASET` and `AMBIGUOUS_MAPPING` — the same AT run also identifies a parallel Cyp26b1+ mossy-cell subtype mapping to 0078 CA3 Glut_4 [CS20230722_SUPT_0078] (F1=0.94, MODERATE), with `DISCORDANT_ANATOMY` because the SUPT_0078 atlas anatomy registers to the CA3 pyramidal layer rather than the dentate hilus. The Cyp26b1 → SUPT_0078 and Adcyap1 → SUPT_0079 pair are presented as a two-supertype mossy-cell mapping rather than competing alternatives. The Cell Ontology has no specific term for this population; dentate gyrus neuron [[CL:4023062](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023062)] is the closest ancestor. Hilar mossy cells are glutamatergic neurons with soma restricted to the dentate gyrus polymorphic layer; CL:4023062 covers all dentate gyrus neurons and is therefore a BROAD match. No mossy cell-specific CL term currently exists.

### Proposed experiments and follow-ups

**Already completed.** Hochgerner 2018 mouse dentate gyrus annotation transfer to WMBv1 (run `at_run_20260427_hochgerner2018_dg_mmc_wmbv1`, F1=0.83 at SUPT_0079 for Mossy-Adcyap1; F1=0.94 at SUPT_0078 for Mossy-Cyp26b1) resolves the primary supertype mapping for both molecular mossy-cell subtypes. What remains unresolved: independent replication, the anatomical interpretation of the SUPT_0078 anatomy mismatch, and the Mossy-Klk8 third-subtype assignment.

- **Independent dentate-gyrus annotation transfer.** Run MapMyCells or equivalent against WMBv1 using a separately-collected mouse hilar single-cell dataset; target F1 >= 0.80 at SUPERTYPE level on CS20230722_SUPT_0078 and CS20230722_SUPT_0079, and F1 >= 0.80 at CLUSTER level on CS20230722_CLUS_0317. Expected output: AnnotationTransferEvidence on edges 0078, 0079, 0317. Resolves: `SINGLE_DATASET` caveat on all three survivors.
- **Spatial validation of the Cyp26b1+ subtype anatomy.** Targeted FISH/ISH of SUPT_0078 defining markers (Homer3, Cldn22) and Cyp26b1 in the dentate hilus and at the CA3c boundary in mouse dorsal and ventral hippocampus; expected output: LiteratureEvidence or AnnotationTransferEvidence on edge to SUPT_0078 resolving whether the supertype's soma positions span the CA3c/hilus boundary. Resolves: `DISCORDANT_ANATOMY` caveat on SUPT_0078 and open question 1.
- **Cyp26b1/Adcyap1 co-labelling in the hilus.** ISH co-labelling of Cyp26b1 and Adcyap1 in dentate hilus to confirm non-overlapping expression and validate the two-supertype mossy-cell split. Expected output: LiteratureEvidence; resolves open question 1.
- **Mossy-Klk8 subtype assignment.** Targeted analysis of the Hochgerner 2018 Mossy-Klk8 cells (n=6 in the existing AT run, best F1=0.56) against WMBv1 supertype-rank candidates, or a higher-n hilar dataset focused on Klk8+ cells; expected output: AT evidence and potentially a third mossy-cell edge.

### Open questions

1. What is the functional and anatomical distinction between the SUPT_0078 (Cyp26b1+) and SUPT_0079 (Adcyap1+) mossy-cell subtypes? Do they correspond to dorsal vs. ventral mossy cells, or to distinct projection patterns (IML-only vs. IML+MML in dorsal mossy cells)? *(Appears on both supertype-survivor edges.)*
2. Are SUPT_0078 cells that map to CA3 pyramidal layer in spatial registration actually at the CA3c/hilar boundary? High-resolution FISH of Homer3 or Cldn22 in hilus/CA3c would resolve this.
3. Does the ~32% of Mossy-Adcyap1 cells scattering to sibling clusters within SUPT_0079 reflect a real molecular subdivision of the Adcyap1+ mossy cells, or AT noise at small n?
4. Curator follow-up: removal of the legacy/fresh-emit duplicate edge `edge_hilar_mossy_cell_hippocampus_to_CS20230722_SUPT_0079` (same `taxonomy_type` as the canonical AT-supported edge `edge_hilar_mossy_cell_hippocampus_to_supt_0079`).

---

## References

| # | Citation | PMID | Used for |
|---:|---|---|---|
| [1] | Botterill et al. 2021 | [33600026](https://pubmed.ncbi.nlm.nih.gov/33600026) | soma location |
| [2] | Fredes & Shigemoto 2021 | [34214666](https://pubmed.ncbi.nlm.nih.gov/34214666) | soma location |
| [3] | Scharfman & Myers 2013 | [23420672](https://pubmed.ncbi.nlm.nih.gov/23420672) | soma location |
| [4] | Sun et al. 2017 | [28451637](https://pubmed.ncbi.nlm.nih.gov/28451637) | soma location |
| [5] | Scharfman & Bernstein 2015 | [26347618](https://pubmed.ncbi.nlm.nih.gov/26347618) | neurotransmitter type |
| [6] | Sarvari et al. 2016 | [27375434](https://pubmed.ncbi.nlm.nih.gov/27375434) | Slc17a7 marker |
| [7] | Godino et al. 2023 | [37546856](https://pubmed.ncbi.nlm.nih.gov/37546856) | Drd2 marker |
| [8] | Yu et al. 2014 | [25206826](https://pubmed.ncbi.nlm.nih.gov/25206826) | Reln marker |

---

<!-- verdict-block-start: edge_hilar_mossy_cell_hippocampus_to_supt_0079 -->
```yaml
verdict:
  confidence: HIGH
  confidence_score: 0.85
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Hochgerner 2018 Mossy-Adcyap1 annotation transfer
    (run at_run_20260427_hochgerner2018_dg_mmc_wmbv1) lands 20 of 27
    cells on CS20230722_SUPT_0079 at on the paired edge), and the
    supertype's atlas anatomy is dentate polymorph layer (MBA:10704)
    dominant with region_fraction_100um: 0.94. Gria4 and Dkk3 are
    expressed at supertype rank with child-coverage 1.000 across
    CS20230722_CLUS_0316 and CS20230722_CLUS_0317; the best AT child
    is CS20230722_CLUS_0317 (paired skos:closeMatch edge).
  reconciliation_note: >
    Paired with cluster-level edge_hilar_mossy_cell_hippocampus_to_CS20230722_CLUS_0317
    (best-child within SUPT_0079; skos:closeMatch + 1:1) and with the
    Cyp26b1+ mossy-cell supertype edge to CS20230722_SUPT_0078; the
    classical hilar mossy cell maps to a two-supertype pair rather
    than a single 1:1.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: Hochgerner 2018 identifies three molecular mossy-cell
        subtypes (Cyp26b1, Adcyap1, Klk8); CS20230722_SUPT_0079
        captures the Adcyap1+ subtype while CS20230722_SUPT_0078
        captures the Cyp26b1+ subtype. Mossy-Klk8 (n=6) maps
        ambiguously across CA3 supertypes (best F1=0.56) — insufficient
        evidence for a separate edge.
    - caveat_type: SINGLE_DATASET
      description: Annotation transfer evidence comes from a single
        source dataset (GEO:GSE95315); independent replication of the
        Mossy-Adcyap1 to CS20230722_SUPT_0079 assignment is not yet
        available.
    - caveat_type: NT_PREDICTION_UNCERTAIN
      description: Atlas-side NT type is not asserted on the supertype;
        the cluster-level Glut annotation on CS20230722_CLUS_0317 is
        consistent with the glutamatergic classical type but
        supertype-level NT is NOT_ASSESSED.
  proposed_experiments:
    - Independent mouse dentate gyrus annotation transfer
      (Hochgerner-style replication) targeting F1 >= 0.80 at
      SUPERTYPE level for CS20230722_SUPT_0079.
    - ISH co-labelling of Cyp26b1 and Adcyap1 in dentate hilus to
      confirm non-overlapping expression and validate the
      two-supertype mossy-cell split between CS20230722_SUPT_0078
      and CS20230722_SUPT_0079.
  unresolved_questions:
    - What is the functional and anatomical distinction between the
      CS20230722_SUPT_0078 (Cyp26b1+) and CS20230722_SUPT_0079
      (Adcyap1+) mossy-cell subtypes — dorsal vs. ventral, or
      distinct projection patterns?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hilar_mossy_cell_hippocampus_to_CS20230722_CLUS_0317 -->
```yaml
verdict:
  confidence: HIGH
  confidence_score: 0.78
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Best-child within CS20230722_SUPT_0079 for the
    Mossy-Adcyap1 source label (Hochgerner 2018,:
    CS20230722_CLUS_0317 has the tightest hilar localisation
    (region_fraction_100um: 0.99 in MBA:10704) and the highest cohort
    percentiles for Gria4 (0.778) and Dkk3 (0.852) among the
    supertype's two children. Annotation transfer support is
    inherited from the parent supertype edge (on the paired edge
    CS20230722_SUPT_0079); cluster-level AT n is small (15 cells).
  reconciliation_note: >
    Paired with the parent supertype edge
    edge_hilar_mossy_cell_hippocampus_to_supt_0079 (skos:broadMatch
    + 1:n); this 1:1 records the best-child refinement.
  caveats:
    - caveat_type: LOW_CELL_COUNT
      description: Cluster-level annotation transfer n=15 cells from
        the Mossy-Adcyap1 source label; independent replication
        recommended to confirm cluster-level assignment.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: Cluster-level annotation transfer support is
        inherited from the supertype-level edge
        edge_hilar_mossy_cell_hippocampus_to_supt_0079; the
        Mossy-Adcyap1 label is distributed across sibling clusters
        within CS20230722_SUPT_0079. Supertype-level mapping is the
        primary call.
    - caveat_type: SINGLE_DATASET
      description: Annotation transfer evidence comes from a single
        source dataset (GEO:GSE95315).
  proposed_experiments:
    - Independent mouse dentate gyrus annotation transfer targeting
      the Adcyap1+ mossy-cell subtype, with F1 >= 0.80 at CLUSTER
      level on CS20230722_CLUS_0317.
  unresolved_questions:
    - Does the ~32% of Mossy-Adcyap1 cells scattering to sibling
      clusters within CS20230722_SUPT_0079 reflect a real molecular
      subdivision of the Adcyap1+ mossy cells, or annotation
      transfer noise at small n?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hilar_mossy_cell_hippocampus_to_supt_0078 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.6
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Hochgerner 2018 Mossy-Cyp26b1 annotation transfer
    (run at_run_20260427_hochgerner2018_dg_mmc_wmbv1) lands 33 of 34
    cells on CS20230722_SUPT_0078 at F1=0.94 (purity 0.92), the
    strongest signal in the run. Confidence is held at MODERATE
    because the supertype's atlas anatomy registers to Field CA3
    pyramidal layer (region_fraction_100um: 0.20, strict
    region_fraction: 0.04) rather than the dentate polymorph layer
    expected for hilar mossy cells. Dkk3 expression is high
    (cohort percentile 0.93 at supertype; 0.96 at the AT-best child
    CS20230722_CLUS_0315) with child-coverage 1.000.
  reconciliation_note: >
    Paired with edge_hilar_mossy_cell_hippocampus_to_supt_0079 as
    the Cyp26b1+ side of a two-supertype mossy-cell mapping; the
    anatomy mismatch (CS20230722_SUPT_0078 painting onto CA3 vs.
    expected hilus) is the principal open question and may reflect
    CA3c/hilus boundary registration or a composite supertype.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: CS20230722_SUPT_0078 atlas cells are distributed
        across CA3 strata (Field CA3 pyramidal layer dominant;
        region_fraction_100um: 0.20) rather than the dentate hilus,
        while classical hilar mossy cells have soma restricted to
        the dentate polymorph layer. The transcriptomic signal is
        strong (F1=0.94) but the anatomy is unresolved — Cyp26b1+
        cells may be CA3c/hilus-border mossy cells registering as
        CA3, or CS20230722_SUPT_0078 may include CA3 pyramidal cells
        sharing the Cyp26b1 signature.
    - caveat_type: SINGLE_DATASET
      description: Annotation transfer evidence comes from a single
        source dataset (GEO:GSE95315); independent replication of
        the Mossy-Cyp26b1 to CS20230722_SUPT_0078 assignment is not
        yet available.
    - caveat_type: NT_PREDICTION_UNCERTAIN
      description: Atlas-side NT type is NOT_ASSESSED at supertype
        level; cluster-level Glut annotation on CS20230722_CLUS_0315
        is consistent with the glutamatergic classical type.
  proposed_experiments:
    - Spatial-transcriptomic spot validation of CS20230722_SUPT_0078
      defining markers (Homer3, Cldn22) in dentate hilus and at the
      CA3c boundary to test whether soma positions span the
      CA3c/hilus boundary.
    - Independent mouse dentate gyrus annotation transfer to confirm
      species- and lab-generality of the Mossy-Cyp26b1 to
      CS20230722_SUPT_0078 assignment.
  unresolved_questions:
    - Are CS20230722_SUPT_0078 cells that map to Field CA3 pyramidal
      layer in spatial registration actually at the CA3c/hilar
      boundary? High-resolution FISH of Homer3 or Cldn22 in
      hilus/CA3c would resolve this.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hilar_mossy_cell_hippocampus_to_CS20230722_CLUS_0315 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  rationale: >
    [tier:CUT] AT-best child within CS20230722_SUPT_0078 for
    Mossy-Cyp26b1 but inherits the supertype's CA3 pyramidal layer
    anatomy (region_fraction_100um: 0.28, strict region_fraction:
    0.07); not in the dentate hilus. Eliminated in favour of the
    parent supertype edge, which carries the annotation transfer
    signal and the same anatomy caveat.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hilar_mossy_cell_hippocampus_to_CS20230722_CLUS_0316 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  rationale: >
    [tier:CUT] Sibling cluster of CS20230722_CLUS_0317 within
    CS20230722_SUPT_0079; atlas anatomy is Field CA3 stratum
    radiatum dominant (region_fraction_100um: 0.60, strict
    region_fraction: 0.11), not the dentate hilus.
    CS20230722_CLUS_0317 is the AT-best and hilus-dominant child of
    CS20230722_SUPT_0079.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hilar_mossy_cell_hippocampus_to_CS20230722_CLUS_0507 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0507 atlas anatomy is dentate granule
    cell layer (MBA:632) dominant (region_fraction_100um: 0.81), not
    the dentate polymorph layer; cohort percentiles for Gria4
    (0.370) and Dkk3 (0.259) are well below the hilar candidates.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hilar_mossy_cell_hippocampus_to_CS20230722_CLUS_0508 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0508 atlas anatomy is dentate granule
    cell layer (MBA:632) dominant (region_fraction_100um: 0.84), not
    the dentate polymorph layer; cohort percentiles for Gria4
    (0.296) and Dkk3 (0.222) are well below the hilar candidates.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hilar_mossy_cell_hippocampus_to_CS20230722_SUPT_0079 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] Duplicate edge targeting CS20230722_SUPT_0079 alongside
    the canonical annotation-transfer-supported edge
    edge_hilar_mossy_cell_hippocampus_to_supt_0079; this is a
    legacy/fresh-emit ID collision. The canonical edge carries the
    Mossy-Adcyap1 annotation transfer evidence (on the paired edge) and the
    substantive property comparisons.
  unresolved_questions:
    - Curator removal of duplicate edge
      edge_hilar_mossy_cell_hippocampus_to_CS20230722_SUPT_0079 —
      legacy/fresh-emit ID collision on taxonomy_type
      CS20230722_SUPT_0079; canonical AT-supported edge is
      edge_hilar_mossy_cell_hippocampus_to_supt_0079.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hilar_mossy_cell_hippocampus_to_CS20230722_SUPT_0139 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0139 atlas anatomy is dentate granule
    cell layer (MBA:632) dominant (region_fraction_100um: 0.69,
    strict region_fraction: 0.26), not the dentate polymorph layer.
    Cohort percentiles for Gria4 (0.333) and Dkk3 (0.267) are well
    below the two annotation-transfer-supported mossy-cell
    supertypes.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hilar_mossy_cell_hippocampus_to_CS20230722_SUPT_0138 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.18
  rationale: >
    [tier:CUT] CS20230722_SUPT_0138 atlas anatomy is dentate granule
    cell layer dominant (region_fraction_100um: 0.77), not the
    dentate polymorph layer. Cohort percentiles for Gria4 (0.133)
    and Dkk3 (0.200) are very low.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hilar_mossy_cell_hippocampus_to_CS20230722_SUPT_0141 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0141 (DG-PIR Ex IMN_2) is an
    immature-neuron supertype with dentate granule cell layer
    anatomy (region_fraction_100um: 0.92, strict region_fraction:
    0.44); soma not in the dentate polymorph layer and developmental
    profile inconsistent with mature hilar mossy cells. Cohort
    percentiles for Gria4 (0.200) and Dkk3 (0.400) are low.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hilar_mossy_cell_hippocampus_to_CS20230722_SUPT_0137 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.18
  rationale: >
    [tier:CUT] CS20230722_SUPT_0137 atlas anatomy is dentate granule
    cell layer dominant (region_fraction_100um: 0.81); cohort
    percentiles for Gria4 (0.067) and Dkk3 (0.067) place it in the
    bottom decile of the hilar-glutamatergic survival cohort.
```
<!-- verdict-block-end -->
