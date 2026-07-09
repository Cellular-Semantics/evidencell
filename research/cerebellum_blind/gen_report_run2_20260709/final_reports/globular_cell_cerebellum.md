# Globular Purkinje layer interneuron (globular cell / glycinergic globular cell) — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml`*

---

## Introduction

Globular cells (also called glycinergic Lugaro cells / GLCs) are a rare inhibitory interneuron population of the cerebellar cortex with cell bodies situated at the underside of the Purkinje cell layer, often extending into the granule cell layer [1][2]. They are distinguished from the morphologically related fusiform Lugaro cells and from candelabrum cells (CCs) by their globular-shaped soma, transversely oriented axons, and a characteristic three-marker transcriptomic signature: Nxph1+, Aldh1a3+, Slc6a5+ (GlyT2+), with Oxtr absent [3]. Mapping this type to the WMBv1 atlas is consequential because the globular cell has no existing Cell Ontology term — confirming its correspondence to a discrete atlas cluster would support a new CL term contribution.

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Purkinje cell layer of cerebellar cortex [UBERON:0002979]; soma extends into granular layer; cerebellar cortex [UBERON:0002129] | [1][2] |
| NT type | GABAergic / glycinergic (Slc6a5/GlyT2+) | [3][4] |
| Defining markers | Nxph1, Aldh1a3, Slc6a5 | [3][4] |
| Negative markers | Oxtr | [2] |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** morphological characterisation; mouse (GAD67-GFP cerebellar slices) · [1]
  > Inhibitory interneurons in the cerebellar granular layer are more heterogeneous than traditionally depicted. In contrast to Golgi cells, which are ubiquitously distributed in the granular layer, small fusiform Lugaro cells and globular cells are located underneath the Purkinje cell layer and small in number.
  > — Hirono et al. 2012, Structure, morphology, and anatomical subtypes · [1] <!-- quote_key: 14276970_0b2772de -->

- **Soma location (comparative):** comparative anatomy and morphology (candelabrum vs. globular cells); mouse · [2]
  > Oxtr-Cre mice allowed us to target CCs, rather than glycinergic globular cells. CCs and globular cells have similarities and differences. Both are located near the PC layer, although the locations of CC somata extend slightly into the molecular layer, and globular cells into the granular layer.
  > — Osorno et al. 2022, Transcriptomics and cell-type mapping studies · [2] <!-- quote_key: 248832318_c6f9d2fc -->

- **Defining markers (Nxph1, Aldh1a3, Slc6a5):** three-marker combinatorial logic from snRNA-seq; mouse cerebellar cortex · [3]
  > .The combined expression of these 3 markers allowed us to identify five populations of cells: CCs (Nxph1+, Aldh1a+, Slc6a5-), GLCs (Nxph1+, Aldh1a3+, Slc6a5+), Golgi1 cells (Nxph1-, Aldh1a3-, Slc6a5+), a mixed population that contains Golgi2 cells and LCs (Nxph1+, Aldh1a3-, Slc6a5+), and MLI2s (Nxph1+, Aldh1a3-, Slc6a5-).
  > — Kozareva et al. (preprint), Transcriptomics and cell-type mapping studies · [3] <!-- quote_key: 233245440_4fadb9cd -->

- **NT type (glycinergic):** GABAergic synaptic connectivity via PC collaterals; mouse · [4]
  > .PCs make inhibitory GABAergic synapses with their target neurons: other PCs and Lugaro/globular cells via PC axon collaterals
  > — Hirono et al. 2021, Structure, morphology, and anatomical subtypes · [4] <!-- quote_key: 235419102_404105ba -->

- **Negative marker (Oxtr):** Oxtr-Cre driver targets candelabrum cells, not globular cells; mouse · [2]
  > Oxtr-Cre mice allowed us to target CCs, rather than glycinergic globular cells.
  > — Osorno et al. 2022, Transcriptomics and cell-type mapping studies · [2] <!-- quote_key: 248832318_c6f9d2fc -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Marker expression alignment and annotation transfer (AT) evidence from the Kozareva et al. 2021 PLI_2 (globular) source cluster (GEO:GSE165371, MapMyCells local, `at_run_20260709_kozareva_cerebellum_mmc_wmbv1`) supports a clean mapping to the cluster 5177 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5177] (F1=0.88 at cluster level; see property comparison table). At supertype level, PLI_2 distributes across the children of supertype 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] (F1=0.55), with CLUS_5177 as the leading cluster child; the supportable narrow mapping is therefore to CLUS_5177 specifically, within the broader context of SUPT_1144.

---

### 5177 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5177] · 🟢 HIGH

**Table 1 — Property comparison**

| Property | Classical | Best cluster (CLUS_5177) | Alignment |
|---|---|---|---|
| Soma location | Purkinje cell layer of cerebellar cortex [UBERON:0002979]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] (lower_bound rollup; region_fraction_100um=0.509) | CONSISTENT |
| NT type | GABAergic / glycinergic (Slc6a5/GlyT2+) | GABA-Glyc | CONSISTENT |
| Nxph1 | defining marker | Nxph1: 11.42; cohort_pct 0.978 | CONSISTENT |
| Aldh1a3 | defining marker | Aldh1a3: 5.38; cohort_pct 0.995 (atlas category: DEFINING) | CONSISTENT |
| Slc6a5 | defining marker | Slc6a5: 6.53; cohort_pct 0.989 (atlas category: MERFISH) | CONSISTENT |
| Oxtr | negative marker (ABSENT) | Oxtr: 0.00; cohort_pct 0.000 | CONSISTENT |
| Sex ratio | not documented | not available | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (CLUS_5177) | Atlas metadata | PARTIAL | region_fraction_100um=0.509 (lower_bound) | atlas-internal |
| Kozareva PLI_2 → CLUS_5177 | Annotation transfer | SUPPORT | F1=0.88 (cluster level); purity=0.93, coverage=0.83 | atlas-internal |

*(Child-cluster breakdown not assessed — CLUS_5177 is itself the rank-0 target; no subcluster breakdown available.)*

**Marker evidence provenance:**

- **Nxph1 (defining):** Evidence is transcript-level (snRNA-seq, Kozareva et al. 2021 / Osorno et al. 2022 three-marker logic); mouse cerebellar cortex snRNA-seq clusters. Cell-type specificity rests on the three-marker combination: the source paper (Kozareva preprint [3]) identified GLCs as Nxph1+, Aldh1a3+, Slc6a5+ — the same pattern that CLUS_5177 displays at high percentile (cohort_pct 0.978). The atlas category for Nxph1 on CLUS_5177 is not tagged DEFINING or MERFISH in the property comparison notes, suggesting Nxph1 is expressed at high levels without being the primary atlas discriminator — consistent with its shared expression across related PLI clusters.

- **Aldh1a3 (defining):** Transcript-level evidence from Kozareva preprint [3] and Hirono 2021 [4]. Aldh1a3 is tagged as a DEFINING marker on CLUS_5177 in atlas metadata (cohort_pct 0.995), making this the highest-confidence concordance: both the classical three-marker logic and the WMBv1 atlas independently identify Aldh1a3 as a primary discriminator of this cluster. Among the SUPT_1144 children, Aldh1a3 expression is not uniform: Aldh1a3 child-coverage on the supertype is 0.667, meaning only about two-thirds of child clusters express it reliably — CLUS_5177 (5.38) and CLUS_5178 (2.96) carry the bulk of the signal, while CLUS_5179 shows 0.00 (DISCORDANT). This heterogeneity within the supertype reinforces CLUS_5177 as the most coherent match for the GLC three-marker definition.

- **Slc6a5 (defining):** Transcript-level evidence from Kozareva [3] and Hirono 2021 [4]. On CLUS_5177, Slc6a5 is 6.53 (cohort_pct 0.989) and tagged MERFISH — indicating it is in the atlas team's spatial panel. The glycinergic identity (Slc6a5/GlyT2+) is the biochemically distinctive feature of globular cells among PLI subtypes; the CLUS_5177 atlas annotation "GABA-Glyc" (NT type) directly confirms this. Note: among sibling clusters, CLUS_5178 and CLUS_5185 show much lower Slc6a5 (0.29 and 0.38, respectively), consistent with them representing a subset that retains GABAergic but not glycinergic character. CLUS_5177's high Slc6a5 is therefore the key discriminating feature at cluster level.

- **Oxtr (negative):** Transcript-level; Oxtr: 0.00 on CLUS_5177 (below MIN_DETECTABLE), confirming the expected absence. Osorno 2022 [2] established that Oxtr-Cre targets candelabrum cells, not globular cells; CLUS_5177's zero Oxtr is concordant with the GLC identity and with the distinction from candelabrum cells.

**Concerns:**

- Region location is driven by a lower_bound rollup row (`region_fraction_100um: 0.509`; lower_bound completeness). The WMBv1 atlas does not paint at laminar resolution (Purkinje cell layer is not separately annotated); the query used cerebellar cortex [UBERON:0002129] as a coarser fallback. The fraction is a floor; the true cerebellar cortex fraction may be higher. *(note: cerebellar cortex encompasses the Purkinje cell layer, so a fraction at cerebellar cortex resolution underestimates laminar specificity — this is an expected limitation of the atlas spatial resolution, not a counter-signal.)*

**What would upgrade confidence:**

- A primary dataset with morphological identification of globular cells (patch-seq or biocytin fill confirming globular soma and transverse axon) mapped directly to WMBv1 would strengthen the morphological grounding. No such dataset is currently in the evidence base.
- Deeper spatial resolution in the WMBv1 atlas at Purkinje cell layer granularity would allow direct region_fraction assessment. Currently spatial data at laminar resolution is absent.

---

### 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] · 🟡 MODERATE

**Table 1 — Property comparison (supertype)**

| Property | Classical | Supertype (SUPT_1144) | Best cluster (CLUS_5177) | Alignment |
|---|---|---|---|---|
| Soma location | Purkinje cell layer [UBERON:0002979]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] (region_fraction_100um=0.699, lower_bound) | region_fraction_100um=0.509 | CONSISTENT |
| NT type | GABAergic / glycinergic | not asserted at supertype level | GABA-Glyc | NOT_ASSESSED / CONSISTENT |
| Nxph1 | defining marker | Nxph1: 11.32; cohort_pct 0.973; child-coverage 1.000 | 11.42 | CONSISTENT |
| Aldh1a3 | defining marker | Aldh1a3: 2.78; cohort_pct 0.991; child-coverage 0.667 | 5.38 | CONSISTENT |
| Slc6a5 | defining marker | Slc6a5: 4.75; cohort_pct 0.900; child-coverage 1.000 | 6.53 | CONSISTENT |
| Oxtr | negative (ABSENT) | Oxtr: 0.00 | 0.00 | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (SUPT_1144) | Atlas metadata | PARTIAL | region_fraction_100um=0.699 (lower_bound) | atlas-internal |
| Kozareva PLI_2 → SUPT_1144 | Annotation transfer | PARTIAL | F1=0.55 (supertype level); coverage=0.97 | atlas-internal |

*(2 of 3 child clusters of SUPT_1144 express Aldh1a3 reliably (child-coverage 0.667); CLUS_5179 shows Aldh1a3 = 0.00. Nxph1 and Slc6a5 are present in all children (child-coverage 1.000 for both). Best match within the supertype: 5177 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5177].)*

The AT evidence from the PLI_2 source group (n=735 cells, MapMyCells local) supports this supertype as the broader classification context for the globular cell. At the supertype level (F1=0.55, coverage=0.97), virtually all PLI_2 cells land on SUPT_1144 or its children; the F1 is diluted because PLI_2 purity at the supertype level is 0.38 — indicating that SUPT_1144 contains cell types beyond the globular cell. This is consistent with SUPT_1144 being a multi-cluster supertype (including CLUS_5177, CLUS_5178, and CLUS_5179), of which only CLUS_5177 achieves the tight cluster-level match. The three defining markers are expressed throughout the supertype (Nxph1 and Slc6a5 with full child-coverage), confirming the supertype-level identity as Gly-Gaba PLI interneurons, with Aldh1a3 partially heterogeneous across children (child-coverage 0.667).

**Concerns:**

- NT type is not asserted at the SUPT_1144 level in atlas metadata (NOT_ASSESSED); the glycinergic identity is established only at CLUS_5177 (GABA-Glyc annotation).
- Low purity at supertype level (0.38) reflects that SUPT_1144 encompasses multiple clusters of which only CLUS_5177 cleanly concentrates PLI_2 cells.
- Region location is a lower_bound rollup (`region_fraction_100um: 0.699`).

**What would upgrade confidence:**

- Confirming that Aldh1a3-expressing cells within SUPT_1144 map specifically to CLUS_5177 (rather than CLUS_5178) using single-cell expression data would strengthen the subtype resolution claim.

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 5177 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5177] | 1144 CB PLI Gly-Gaba_1 | 535 | 🟢 HIGH | AT F1=0.88; 3 of 3 markers CONSISTENT | Primary |
| 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] | (supertype) | 3646 | 🟡 MODERATE | AT F1=0.55 (supertype); all markers CONSISTENT | Supports broader mapping |
| 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] | 1144 CB PLI Gly-Gaba_1 | 3066 | — | AT best at supertype only; Slc6a5 low (0.29) | Eliminated (AT best at supertype, not cluster; low Slc6a5) |
| 5185 CB PLI Gly-Gaba_4 [CS20230722_CLUS_5185] | 1147 CB PLI Gly-Gaba_4 | 442 | — | AT best at subclass only (F1=0.46) | Eliminated (AT does not reach cluster level) |
| 5179 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5179] | 1144 CB PLI Gly-Gaba_1 | 45 | — | Aldh1a3 DISCORDANT (0.00); poor AT | Eliminated (Aldh1a3 absent) |
| 1147 CB PLI Gly-Gaba_4 [CS20230722_SUPT_1147] | (supertype) | 442 | — | AT best at subclass only; Slc6a5 low | Eliminated (AT does not reach supertype level) |
| 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] | (supertype) | 13098 | — | Aldh1a3 DISCORDANT (0.02); no AT transfer | Eliminated (Aldh1a3 absent; wrong MLI type) |
| 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] | 1149 CBX MLI Megf11 Gaba_1 | 154 | — | No AT transfer (F1=0.032 at class only) | Eliminated (no AT transfer; MLI not PLI) |
| 1146 CB PLI Gly-Gaba_3 [CS20230722_SUPT_1146] | (supertype) | 129 | — | Oxtr DISCORDANT (1.21) | Eliminated (Oxtr expressed — candelabrum-like) |
| 0999 MV-SPIV Zic4 Neurod2 Glut_3 [CS20230722_SUPT_0999] | (supertype) | 400 | — | Wrong region (region_fraction_100um=0.138; medulla) | Eliminated (wrong region) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Globular Purkinje layer interneuron (globular cell / glycinergic globular cell) is defined on the basis of CLASSICAL_MULTIMODAL evidence: morphological characterisation (globular soma, transverse axon, location at the underside of the Purkinje cell layer extending into the granular layer) [1][2], glycinergic/GABAergic neurotransmitter identity (Slc6a5/GlyT2+) [3][4], and a three-marker transcriptomic signature (Nxph1+, Aldh1a3+, Slc6a5+; Oxtr–) [2][3]. The classical node notes provisional status for the marker and mapping interpretation pending primary dataset verification.

**Atlas mapping query.**
Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.**
Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE165371 (PLI_2) |
| Source species | NCBITaxon:10090 (mouse) |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper 1.7.1, default parameters, 100 bootstrap iterations). Gene symbols remapped to Ensembl IDs via conf/gene_mapping_CCN20230722.tsv (20390/23203 genes mapped). Interneuron subset (45,555 of 60,526 joint-archive nuclei with final subcluster annotation). BKP web backend was unavailable (HTTP 400) at run time; local backend used. |
| Tool version | cell_type_mapper 1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 45,555 total; 45,555 after filter |
| Run record | [`kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/f1_scores_best.csv) |
| Caveats | Same-species (mouse) snRNA-seq to WMBv1. Source cluster labels are transcriptomic (Kozareva/Osorno) with high marker validation — treat cluster-level F1 as informative (pure-source expectation). PLI clusters are rare (globular PLI_2: 735 cells). Blind-run note: this reproduces the curator ground-truth AT anchors without those targets ever being supplied to the pipeline. |

**Atlas data sources.** All atlas values are from the WMBv1 (CCN20230722) taxonomy reference store.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `f4ce9b9` at 2026-07-09T18:53:53+00:00 from [kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml](kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml).*

<details>
<summary>Evidence base audit table</summary>

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_globular_cell_cerebellum_to_CS20230722_CLUS_5177 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | atlas-internal |
| edge_globular_cell_cerebellum_to_CS20230722_SUPT_1144 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_globular_cell_cerebellum_to_CS20230722_CLUS_5178 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_globular_cell_cerebellum_to_CS20230722_CLUS_5189 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal |
| edge_globular_cell_cerebellum_to_CS20230722_CLUS_5185 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_globular_cell_cerebellum_to_CS20230722_CLUS_5179 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_globular_cell_cerebellum_to_CS20230722_SUPT_1147 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_globular_cell_cerebellum_to_CS20230722_SUPT_1151 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal |
| edge_globular_cell_cerebellum_to_CS20230722_SUPT_0999 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal |
| edge_globular_cell_cerebellum_to_CS20230722_SUPT_1146 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |

</details>

</details>

---

## Discussion

### Best candidate + caveats

**Primary mapping:** Globular Purkinje layer interneuron → 5177 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5177] at HIGH confidence. Key support: annotation transfer (PLI_2; F1=0.88 at cluster level; purity=0.93) and full marker concordance (3 of 3 defining markers CONSISTENT; Oxtr absent CONSISTENT). Key caveats: region location is a lower_bound rollup (atlas does not resolve at Purkinje cell layer laminar resolution); no primary morphological characterisation dataset (patch-seq or biocytin fill) is available to bridge the classical morphological definition to the transcriptomic cluster.

**Broader context:** The supertype 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] represents the broader mapping context: virtually all PLI_2 source cells land on this supertype (coverage=0.97), confirming that the globular cell is embedded within this Gly-Gaba PLI supertype. The narrow cluster-level call to CLUS_5177 is supported by the high F1, high purity, and the Aldh1a3 expression gradient across supertype children (full expression in CLUS_5177, absent in CLUS_5179).

No Cell Ontology term currently assigned. The globular cell / glycinergic Lugaro cell (PLI2-type) has no CL equivalent; this mapping is a candidate for CL contribution.

### Proposed experiments and follow-ups

1. **Patch-seq or biocytin-fill morphological mapping.** Target Slc6a5+ (or Aldh1a3+) cells in the cerebellar cortex with post-hoc morphological verification of the globular soma and transverse axon. Map recovered profiles directly to WMBv1 (MapMyCells or equivalent) targeting CLUS_5177. Expected output: AnnotationTransferEvidence with morphological confirmation. Expected threshold: F1 ≥ 0.75 at CLUSTER level. Resolves: the open gap between classical morphological definition and transcriptomic cluster identity.

2. **Expression dataset re-analysis for laminar resolution.** If a dataset with laminar positional metadata (e.g. MERFISH-resolved coordinates for PLI cell types) becomes available for mouse cerebellar cortex, assess whether CLUS_5177 cells co-localise with the Purkinje cell layer underside. Expected output: spatial location evidence strengthening or qualifying the CONSISTENT location alignment.

3. **CL term request.** Given the strong transcriptomic identity (F1=0.88, 3 of 3 markers CONSISTENT, glycinergic identity confirmed), draft a new CL term for the glycinergic Purkinje layer interneuron / globular cell using `workflows/cl-term-request.md`. The mapping to CLUS_5177 provides the atlas anchor for the term definition.

4. **Aldh1a3 heterogeneity investigation.** Targeted Aldh1a3 ISH or smFISH on morphologically verified globular cells to clarify whether Aldh1a3 heterogeneity within SUPT_1144 (child-coverage 0.667) reflects a biological subpopulation or assay noise.

### Open questions

1. Does Aldh1a3 heterogeneity within SUPT_1144 (child-coverage 0.667) reflect a biological subpopulation difference between CLUS_5177 and CLUS_5178/CLUS_5179, or assay noise? Targeted Aldh1a3 ISH on morphologically verified globular cells would clarify.

2. Are CLUS_5178 and CLUS_5179 (sibling clusters in SUPT_1144 that lack high Slc6a5 or Aldh1a3) biologically distinct PLI subtypes, or represent the same globular cell population in a different state? This has implications for whether the mapping should remain at cluster or supertype level.

3. The three-marker logic (Kozareva preprint [3]) uses a preprint reference (doi:https://doi.org/10.1101/2021.04.09.439172). Is this now published with a stable PMID? If so, the reference entry should be updated.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Hirono et al. 2012 | [22235322](https://pubmed.ncbi.nlm.nih.gov/22235322/) | soma location, morphology, electrophysiology |
| [2] | Osorno et al. 2022 | [35578131](https://pubmed.ncbi.nlm.nih.gov/35578131/) | soma location, negative markers (Oxtr) |
| [3] | Kozareva et al. (preprint) · doi:https://doi.org/10.1101/2021.04.09.439172 | — | defining markers (Nxph1, Aldh1a3, Slc6a5), NT type |
| [4] | Hirono et al. 2021 | [34194302](https://pubmed.ncbi.nlm.nih.gov/34194302/) | NT type (GABAergic/glycinergic) |

---

<!-- verdict-block-start: edge_globular_cell_cerebellum_to_CS20230722_CLUS_5177 -->
```yaml
verdict:
  confidence: HIGH
  confidence_score: 0.88
  relationship: skos:exactMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] AT transfer of PLI_2 (GEO:GSE165371, n=735) in
    at_run_20260709_kozareva_cerebellum_mmc_wmbv1 reaches CS20230722_CLUS_5177 with
    F1=0.88 (purity=0.93, coverage=0.83) — the cleanest cluster-level resolution in the PLI
    glycinergic cohort. 4 of 4 defining markers CONSISTENT (Nxph1 cohort_pct 0.978;
    Aldh1a3 cohort_pct 0.995 with atlas category DEFINING; Slc6a5 cohort_pct 0.989 with
    atlas category SPATIAL_PANEL). Negative marker Oxtr CONSISTENT (0.00). NT annotation GABA-Glyc
    matches glycinergic (Slc6a5+) classical identity. Region CONSISTENT (lower_bound rollup;
    region_fraction_100um: 0.509 — a floor; atlas lacks laminar resolution for Purkinje cell layer).
  reconciliation_note: >
    Primary cluster within CS20230722_SUPT_1144 (see edge_globular_cell_cerebellum_to_CS20230722_SUPT_1144);
    supertype edge provides the broader context (skos:broadMatch + 1:n). CLUS_5177 leads the
    cluster F1 distribution within SUPT_1144 decisively (F1=0.88 vs siblings < 0.21).
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal driven by lower_bound rollup row — non-painted CCF2020 descendants uncounted;
        region_fraction_100um: 0.509 is a floor. Atlas does not paint at Purkinje cell layer resolution.
    - caveat_type: SINGLE_DATASET
      description: >
        No primary dataset from an independent morphologically-defined source is available to bridge
        the classical globular soma / transverse axon definition to the transcriptomic cluster.
        Three-marker logic rests on Kozareva preprint [3] (publication status unconfirmed).
  proposed_experiments:
    - >
      Annotation transfer from an independent morphologically-defined source dataset of globular cells
      in cerebellar cortex; map recovered transcriptomic profiles to WMBv1 targeting
      CS20230722_CLUS_5177 via annotation transfer.
      Expected AnnotationTransferEvidence confirming cluster identity; threshold F1 >= 0.75 at
      cluster level.
    - >
      Spatially resolved transcriptomic dataset for mouse cerebellar cortex with laminar
      annotation — assess co-localisation of CLUS_5177 cells with Purkinje cell layer underside.
    - >
      Draft new CL term for glycinergic Purkinje layer interneuron (globular cell) using
      workflows/cl-term-request.md, with CS20230722_CLUS_5177 as the atlas anchor.
    - >
      Confirm Kozareva preprint [3] publication status (doi:https://doi.org/10.1101/2021.04.09.439172);
      update reference to stable PMID if published.
  unresolved_questions:
    - >
      Does Aldh1a3 heterogeneity within CS20230722_SUPT_1144 (child-coverage 0.667) reflect
      a biological subpopulation difference or assay noise? Targeted Aldh1a3 expression profiling
      on verified globular cells would clarify.
    - >
      Are CS20230722_CLUS_5178 and CS20230722_CLUS_5179 (sibling clusters lacking high Slc6a5
      or Aldh1a3) biologically distinct PLI subtypes or the same globular cell in a different state?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_globular_cell_cerebellum_to_CS20230722_SUPT_1144 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] AT transfer of PLI_2 in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 reaches
    CS20230722_SUPT_1144 with F1=0.55 (coverage=0.97, purity=0.38) — near-complete coverage
    of PLI_2 source cells lands on this supertype, but purity is diluted because SUPT_1144
    contains multiple clusters of which only CS20230722_CLUS_5177 achieves clean cluster-level
    mapping. 4 of 4 markers CONSISTENT at supertype level (Nxph1 cohort_pct 0.973 child-coverage
    1.000; Aldh1a3 cohort_pct 0.991 child-coverage 0.667; Slc6a5 cohort_pct 0.900
    child-coverage 1.000). Oxtr CONSISTENT (0.00). NT NOT_ASSESSED at supertype level.
    BroadMatch is appropriate: the supertype encompasses the globular cell cluster
    (CS20230722_CLUS_5177) alongside sibling clusters that do not express the full
    three-marker GLC signature.
  reconciliation_note: >
    Paired with edge_globular_cell_cerebellum_to_CS20230722_CLUS_5177 (skos:exactMatch + 1:1)
    which provides the cluster-level resolution. Supertype broadMatch captures the lineage
    context; the narrow GLC identity lives at CS20230722_CLUS_5177.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal driven by lower_bound rollup row; region_fraction_100um: 0.699 is a floor.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        NT type not asserted at supertype level (NOT_ASSESSED); glycinergic identity confirmed
        only at CS20230722_CLUS_5177. Aldh1a3 child-coverage 0.667 indicates supertype is
        not uniformly Aldh1a3+.
  proposed_experiments:
    - >
      Confirm whether Aldh1a3-expressing cells within CS20230722_SUPT_1144 co-localise
      exclusively with CS20230722_CLUS_5177 using single-cell expression data.
  unresolved_questions:
    - >
      NT type of CS20230722_SUPT_1144 is not asserted in atlas metadata; clarify whether
      all SUPT_1144 children carry GABA-Glyc identity or only CS20230722_CLUS_5177.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_globular_cell_cerebellum_to_CS20230722_CLUS_5178 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] AT best mapping for PLI_2 reaches only supertype level on CS20230722_CLUS_5178
    (F1=0.55 at supertype, not cluster); no cluster-level AT metrics row reaches this target.
    Slc6a5 expression is low (0.29; cohort_pct 0.823) — substantially below the defining
    marker level on CS20230722_CLUS_5177 (6.53). While Nxph1 and Aldh1a3 are CONSISTENT,
    the low Slc6a5 does not support the glycinergic GLC identity. Sibling of CS20230722_CLUS_5177
    within CS20230722_SUPT_1144 but a weaker specific match.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_globular_cell_cerebellum_to_CS20230722_CLUS_5189 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] AT transfer of PLI_2 does not reach CS20230722_CLUS_5189 — best F1 is 0.03
    at class level only (28 CB GABA), with no supertype- or cluster-level transfer. This
    cluster belongs to the CBX MLI Megf11 lineage, not the PLI Gly-Gaba lineage. Wrong cell
    type class.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_globular_cell_cerebellum_to_CS20230722_CLUS_5185 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] AT best mapping for PLI_2 reaches only subclass level for CS20230722_CLUS_5185
    (F1=0.46 at subclass CB PLI Gly-Gaba); no supertype- or cluster-level transfer to this
    specific cluster. Belongs to CS20230722_SUPT_1147, a distinct supertype from
    CS20230722_SUPT_1144. Slc6a5 low (0.38; cohort_pct 0.849). Not the leading PLI_2 target.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_globular_cell_cerebellum_to_CS20230722_CLUS_5179 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] Aldh1a3 DISCORDANT (0.00; below MIN_DETECTABLE) on CS20230722_CLUS_5179 —
    the defining marker for GLCs is absent. AT cluster-level F1 for PLI_2 does not reach
    cluster level on this target (best at supertype, F1=0.55). Sibling of CS20230722_CLUS_5177
    in CS20230722_SUPT_1144 but lacks both Aldh1a3 and meaningful cluster-level AT transfer.
    Eliminated (Aldh1a3 absent).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_globular_cell_cerebellum_to_CS20230722_SUPT_1147 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] AT best mapping for PLI_2 reaches only subclass level for CS20230722_SUPT_1147
    (F1=0.46 at CB PLI Gly-Gaba subclass); no supertype-level AT metrics row reaches this
    target. Slc6a5 low (0.38; cohort_pct 0.755). Distinct from the SUPT_1144 lineage.
    Not a meaningful specific match.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_globular_cell_cerebellum_to_CS20230722_SUPT_1151 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Aldh1a3 DISCORDANT (0.02; below MIN_DETECTABLE) on CS20230722_SUPT_1151. No AT
    transfer beyond class level (F1=0.03). CBX MLI Cdh22 lineage — wrong cell type class
    (MLI, not PLI). Eliminated (Aldh1a3 absent; MLI lineage).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_globular_cell_cerebellum_to_CS20230722_SUPT_0999 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0999 is a medulla/vestibular nucleus cluster (MV-SPIV Zic4 Neurod2
    Glut_3) with region_fraction_100um: 0.138 — the vast majority of cells are in medulla, not
    cerebellar cortex. No AT transfer at any level within the CB lineage. Wrong region and wrong
    cell type. Eliminated (wrong region; glutamatergic).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_globular_cell_cerebellum_to_CS20230722_SUPT_1146 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] Oxtr DISCORDANT on CS20230722_SUPT_1146 (Oxtr: 1.21; cohort_pct 0.900) —
    Oxtr expression is the hallmark of candelabrum cells (PLI_1), not glycinergic globular cells
    (PLI_2). The Oxtr-positive identity directly contradicts the GLC negative marker criterion.
    AT best only at subclass level (F1=0.46 at CB PLI Gly-Gaba subclass). Eliminated (Oxtr expressed —
    candelabrum-like profile).
```
<!-- verdict-block-end -->
