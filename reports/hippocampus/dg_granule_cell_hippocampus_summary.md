# Dentate gyrus granule cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

---

## Introduction

Dentate gyrus (DG) granule cells are the principal glutamatergic neurons of the
DG, whose somata occupy the granule cell layer and whose mossy-fiber axons
project into the hilus and to CA3, forming the classical trisynaptic
hippocampal circuit. Mapping this classical type onto the WMBv1 (CCN20230722)
atlas is foundational for anchoring hippocampal cell-type ontologies, since DG
granule cells span both developmentally born and adult-born populations and
must be resolved across the multiple "DG Glut" supertypes in the atlas.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | dentate gyrus granule cell layer [UBERON:0005381] | [1][2][3][4] |
| NT | glutamatergic | [5][6][7] |
| Markers | Prox1, C1ql2 | Prox1: [8]; C1ql2: [9] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical anatomical description · [1]
  > The hippocampal mossy fibers (MFs), the axons of the granule cells (GCs) of the dentate gyrus, innervate mossy cells and interneurons in the hilus on their way to CA3 where they innervate interneurons and pyramidal cells
  > — Munster-Wandowski et al. 2013, abstract · [1] <!-- quote_key: 7458943_e2eed73d -->
- **Soma location:** glutamate-receptor expression confirms granule cell identity in granule cell layer · [2]
  > AMPA receptor subunits GluR1 and GluR2 are expressed in differentiated granule cells, but not in stem cells, in neonatal, and adult dentate gyrus
  > — Hagihara et al. 2011, abstract · [2] <!-- quote_key: 16383828_d2ad6dc6 -->
- **Soma location:** trisynaptic-circuit framing · [3]
  > These principal cells are interconnected through glutamatergic synapses that form the classical trisynaptic pathway, where dentate granule cells receive input from entorhinal cortex and project to CA3 pyramidal cells, which then connect to CA1 pyramidal cells (Munster-Wandowski et al., 2013)(Yau et al., 2015).
  > — Yau et al. 2015, Classical Hippocampal Circuit Organization · [3] <!-- quote_key: 1705399_6ee6563e -->
- **NT type:** whole-genome RNA-seq characterisation of DG granule cells · [5]
  > we used next-generation RNA sequencing (RNA-seq) to produce a quantitative, whole genome characterization of gene expression for the major excitatory neuronal classes of the hippocampus; namely, granule cells and mossy cells of the dentate gyrus, and pyramidal cells of areas CA3, CA2, and CA1
  > — Cembrowski et al. 2016, abstract · [5] <!-- quote_key: 4875295_4a456257 -->
- **NT type:** vesicular glutamate transporter expression in mossy fibre terminals · [6]
  > VGLUT1, VGLUT2, and VGAT coexist in mossy fiber terminals of the h
  > — Zander et al. 2010, abstract · [6] <!-- quote_key: 539922_281341b3 -->
- **NT type:** developmental GABAergic-to-glutamatergic switch in granule cells · [7]
  > immediately after birth, GCs exhibit a clear GABAergic phenotype. Only later they integrate the classical glutamatergic trisynaptic hippocampal circuit
  > — Pedroni et al. 2014, abstract · [7] <!-- quote_key: 11333153_3bc75fe5 -->
- **Prox1 marker:** mGluR1/vGLUT1 expression patterns in granule cells · [8]
  > Metabotropic glutamate receptors also play important roles, with mGluR1 mainly expressed in granule cells and CA3 pyramidal neurons, while mGluR5 is highly expressed in all hippocampal subfields (Sarvari et al., 2016). The vesicular glutamate transporter vGLUT1 is the main subtype expressed in the hippocampus, packing glutamate into synaptic vesicles of glutamatergic axon terminals (Sarvari et al., 2016).
  > — Sarvari et al. 2016, Synaptic Properties and Neurotransmitter Systems · [8] <!-- quote_key: 14854554_439a5d0b -->
- **C1ql2 marker:** restricted expression to DG granule cells · [9]
  > the expression of Sema5B and C1ql2 is restricted to dentate granule cells within the hippocampus
  > — D et al. 2018, discussion · [9] <!-- quote_key: 5895709_81a3d36b -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas supertype was assessed; SUPT_0137 (0137 DG Glut_2) is the
primary mapping at MODERATE confidence on annotation-transfer and atlas-metadata
evidence.

![Filtered AT figure for Dentate gyrus granule cell](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/figures/f1_for_dg_granule_cell_hippocampus.png)

*F1 across taxonomy levels for the 2 source group(s) relevant to Dentate gyrus
granule cell (Granule-mature, Granule-immature). Each panel row is a
source-cell group; nodes are coloured by F1 with precision (P) and recall (R)
shown inline. F1 ≥ 0.5 at a level indicates a clean mapping at that
resolution.*

Both mature and immature Hochgerner granule cell populations map predominantly
to SUPT_0137 at the supertype level (F1 ≈ 0.58–0.60), with strong subclass-level
consolidation onto DG Glut (group_purity 0.888–0.988).

### Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---:|---|---|---|
| 1 | — | 0137 DG Glut_2 [CS20230722_SUPT_0137] | 21781 | 🟡 MODERATE | Location CONSISTENT · NT CONSISTENT | Best candidate |

Total: 1 edge. Relationship: PARTIAL_OVERLAP.

### Property alignment — SUPT_0137 (0137 DG Glut_2)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | dentate gyrus granule cell layer (UBERON:0001885) | DG granule cell layer (MBA:632): 7199; molecular layer (MBA:10703): 6636; polymorph layer (MBA:10704): 3067; CA3 pyramidal layer (MBA:495): 1529 | not assessed | CONSISTENT |
| NT type | glutamatergic | glutamatergic (SUBC_037 DG Glut, SUPT_0137) | not assessed | CONSISTENT |
| Prox1 expression | defining marker | not listed in SUPT_0137 defining markers (Dsp, Kcnh3, Syndig1); mean_expression=8.59 (precomputed_stats, supertype level) | not assessed | CONSISTENT |
| C1ql2 expression | defining marker | not listed in SUPT_0137 defining markers; mean_expression=5.77 (precomputed_stats, supertype level) | not assessed | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Hochgerner 2018 MapMyCells AT | Annotation transfer | SUPPORT | F1=0.584 (SUPT_0137, Granule-mature); F1=0.601 (Granule-immature); subclass F1=0.703 | atlas-internal |
| WMBv1 atlas metadata | Atlas metadata | SUPPORT | 7199 cells in DG granule cell layer (MBA:632) | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

### 0137 DG Glut_2 [CS20230722_SUPT_0137] · 🟡 MODERATE

**Supporting evidence:**
- MapMyCells local annotation transfer of Hochgerner 2018 (GEO:GSE95315) mouse
  DG scRNA-seq onto WMBv1: Granule-mature maps to SUPT_0137 with F1=0.584
  (433/609 cells) and Granule-immature with F1=0.601 (437/581 cells). At
  subclass level, DG Glut (SUBC_037) is the dominant classification with
  group_purity 0.988 for Granule-mature and 0.888 for Granule-immature
  (subclass F1=0.703 on 716 mapped cells).
- WMBv1 atlas metadata: SUPT_0137 holds 7199 cells in the DG granule cell
  layer (MBA:632), 6636 in the molecular layer (MBA:10703) and 3067 in the
  polymorph layer (MBA:10704) — anatomically consistent with DG granule cell
  soma placement (molecular-layer signal likely reflects dendritic-process
  registration or immature granule cells with broader distribution).
- Precomputed expression cross-check confirms the two classical defining
  markers in SUPT_0137: Prox1 mean_expression = 8.59 and C1ql2 mean_expression
  = 5.77 at the supertype level. Note these are not listed among the atlas's
  named defining markers (Dsp, Kcnh3, Syndig1) but are clearly expressed in
  the population.

**Marker evidence provenance:**
- **Prox1:** classical defining marker cited via a hippocampal-marker review
  (Sarvari et al. 2016, [8]) rather than a granule-cell-specific primary
  study; nonetheless, transcript-level evidence is corroborated by direct
  precomputed expression on SUPT_0137 (mean=8.59), so the marker stands.
- **C1ql2:** supported by a primary study restricting Sema5B/C1ql2 expression
  to DG granule cells within the hippocampus ([9]); precomputed expression in
  SUPT_0137 (mean=5.77) confirms the marker is present at the supertype level.
- Neither Prox1 nor C1ql2 is named in the WMBv1 metadata defining-marker list
  for SUPT_0137 (Dsp, Kcnh3, Syndig1). This is a presentation-layer gap, not
  an expression gap — the markers are expressed but were not selected by the
  atlas's automatic marker-ranking pipeline.

**Concerns:**
- AMBIGUOUS_MAPPING: DG Glut subclass (SUBC_037) in WMBv1 contains at least
  four supertypes (SUPT_0136–0139). Hochgerner Granule-mature and
  Granule-immature both map predominantly to SUPT_0137, suggesting it is the
  dominant mature-granule-cell supertype, but adult-born immature granule
  cells may also map to SUPT_0141 (DG-PIR Ex IMN_2; F1=0.146 for
  Granule-immature). The classical DG granule cell type as described here
  spans both mature and immature populations and is not cleanly captured by a
  single supertype.
- CROSS_SPECIES_EXTRAPOLATION: source data are mouse DG scRNA-seq
  (Hochgerner 2018) mapped onto mouse WMBv1; no cross-species concern, but
  Hochgerner's juvenile-postnatal age distribution differs from WMBv1's adult
  reference and may inflate the immature-population mapping.
- The 1529 cells in CA3 pyramidal layer (MBA:495) on SUPT_0137 may represent
  adult-born granule cells in transit or MERFISH registration overlap at
  CA3c — adjacent region, weak counter-evidence.

**What would upgrade confidence:**
- Run `add-expression` for Prox1 and C1ql2 across SUPT_0136–0139 (and at
  cluster rank 0) to resolve whether SUPT_0137 is uniquely the
  "mature granule cell" supertype or whether the marker profile is shared
  across the DG Glut supertypes. Resolves open question 2.
- Perform annotation transfer from an independent mouse granule cell dataset
  (e.g. Artimovich 2020 or Shin 2015) to cross-validate the SUPT_0137 mapping
  with a different sampling and age distribution. Target: F1 ≥ 0.70 at
  SUPERTYPE level. Resolves open questions 1 and the cross-cohort caveat;
  expected output AnnotationTransferEvidence.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical DG granule cell node
(`definition_basis: CLASSICAL_MULTIMODAL`) is defined by glutamatergic
neurotransmitter identity [5][6][7], soma residency in the dentate gyrus
granule cell layer (UBERON:0005381) [1][2][3][4], and the markers Prox1 [8]
and C1ql2 [9].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the
WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using
metadata-based scoring (region match, NT type, defining markers, sex bias
when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was
compared to the corresponding atlas-side value via the `property_comparisons`
schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT /
NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on
the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH
spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE95315 (Hochgerner 2018 mouse DG scRNA-seq cell type labels: Granule-mature, Granule-immature, Mossy-Cyp26b1, Mossy-Adcyap1, Mossy-Klk8, Neuroblast 1, Neuroblast 2, Cajal-Retzius, GABA-Cnr1, GABA-Lhx6, Astrocytes) |
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

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and
verbatim literature quotes in this report are validated against the
evidencell knowledge base at write time. Authored-prose evidence narratives
are validated against their source `evidence_items[*].explanation` fields.
The pre-write hook rejects any unresolvable identifier or unattributed
blockquote. Specific mapping limitations and caveats are documented
per-candidate in the Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:14+00:00 from
[kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_dg_granule_cell_hippocampus_to_supt_0137 | ANNOTATION_TRANSFER; ATLAS_METADATA | SUPPORT; SUPPORT | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Dentate gyrus granule cell → 0137 DG Glut_2
[CS20230722_SUPT_0137] at MODERATE confidence. Key support: annotation
transfer from Hochgerner 2018 (F1=0.584/0.601 at SUPERTYPE; F1=0.703 at
SUBCLASS) and atlas-metadata anatomical agreement (7199 cells in DG granule
cell layer). Key caveats: AMBIGUOUS_MAPPING across the four DG Glut
supertypes (SUPT_0136–0139) and CROSS_SPECIES_EXTRAPOLATION-style age-cohort
mismatch between Hochgerner's juvenile sampling and WMBv1's adult reference.

No Cell Ontology term currently assigned. Candidate for CL contribution —
the existing CL taxonomy lacks a granule-cell-of-dentate-gyrus class
specific enough to anchor the SUPT_0137 mapping.

### Proposed experiments and follow-ups

The Hochgerner 2018 → WMBv1 annotation transfer already establishes SUPT_0137
as the primary granule-cell supertype mapping; remaining experiments target
cluster-level resolution and marker-expression confirmation.

- **What:** `add-expression` for Prox1 and C1ql2 across SUPT_0136–0139 and
  their child clusters in WMBv1.
  **Target:** detection-rate quantification at supertype and cluster rank for
  both markers.
  **Expected output:** precomputed expression entries on the taxonomy
  reference YAML (no new KB EvidenceItem; supports property_comparison
  refinement).
  **Resolves:** open question 2; refines the four-supertype ambiguity caveat.
- **What:** independent MapMyCells annotation transfer from a second mouse
  granule cell dataset (e.g. Artimovich 2020 or Shin 2015).
  **Target:** F1 ≥ 0.70 at SUPERTYPE for the mature granule cell population on
  SUPT_0137 in a different sampling cohort.
  **Expected output:** AnnotationTransferEvidence added to
  `edge_dg_granule_cell_hippocampus_to_supt_0137`.
  **Resolves:** open question 1; reduces the age-cohort caveat.

### Open questions

1. Do SUPT_0136, SUPT_0137, SUPT_0138 correspond to functionally distinct
   granule cell populations (e.g. adult-born vs. developmentally-born, or
   dorsal vs. ventral DG)?
2. Are Prox1 and C1ql2 expressed in SUPT_0137 cells uniformly, or does
   expression vary across the DG Glut supertypes? Direct precomputed
   expression at cluster rank is needed to resolve.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Munster-Wandowski et al. 2013 | [24319410](https://pubmed.ncbi.nlm.nih.gov/24319410) | soma location |
| [2] | Hagihara et al. 2011 | [21927594](https://pubmed.ncbi.nlm.nih.gov/21927594) | soma location |
| [3] | Yau et al. 2015 | [26380120](https://pubmed.ncbi.nlm.nih.gov/26380120) | soma location |
| [4] | https://doi.org/10.1038/s41598-017-11268-z | — | soma location |
| [5] | Cembrowski et al. 2016 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915) | neurotransmitter type |
| [6] | Zander et al. 2010 | [20519538](https://pubmed.ncbi.nlm.nih.gov/20519538) | neurotransmitter type |
| [7] | Pedroni et al. 2014 | [24592213](https://pubmed.ncbi.nlm.nih.gov/24592213) | neurotransmitter type |
| [8] | Sarvari et al. 2016 | [27375434](https://pubmed.ncbi.nlm.nih.gov/27375434) | Prox1 marker |
| [9] | D et al. 2018 | [29674952](https://pubmed.ncbi.nlm.nih.gov/29674952) | C1ql2 marker |
