# Axo-axonic (chandelier) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Axo-axonic cells, also known as chandelier cells, are PV+ fast-spiking GABAergic interneurons whose axonal output is directed exclusively onto the axon initial segment (AIS) of pyramidal neurons [1]. This unique targeting geometry — with cartridge-like bouton arrangements along the AIS — places axo-axonic cells in direct control of action potential initiation in their target cells. They are one of three canonical PV+ hippocampal interneuron subtypes alongside basket and bistratified cells, and have been noted to have high transcriptomic overlap with the other PV+ subtypes [3].

> Parvalbumin + cells were specifically localized in the granular and polymorphic cell layers of the dentate gyrus and the strata oriens and pyramidale in CA1/3 fields of the rat hippocampus (Kosaka et al., 1987). They have been considered a subpopulation of GABAergic interneurons, including basket and axo-axonic cell types, which innervate the somata and proximal axons of pyramidal cells, respectively (Soriano et al., 1990)
> — Rivera et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 10540334_bdfa426a -->

> Interneurons expressing the calcium binding protein parvalbumin (PV) make up approximately 40% of all GABAergic interneurons. However, this is a heterogeneous group of functionally distinct interneuron subtypes. For example, in the hippocampus alone, there are at least three functionally and morphologically distinct populations of PV + expressing interneurons, namely basket, axo-axonic and bistratified cells. Fast spiking interneurons in the hippocampus and neocortex are often PV + positive and target the soma of pyramidal cells.
> — Dannenberg et al. 2017, Classification Schemes and Methodological Approaches · [2] <!-- quote_key: 38778375_462ec931 -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | [1] |
| NT | GABAergic | [2] |
| Markers | Pvalb (defining) | [1][3] |
| CL term | pvalb chandelier GABAergic interneuron [CL:4023036] (EXACT) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / Pvalb marker:** rat hippocampus immunolocalisation, PV+ basket and axo-axonic cell types described together · [1]
  > Parvalbumin + cells were specifically localized in the granular and polymorphic cell layers of the dentate gyrus and the strata oriens and pyramidale in CA1/3 fields of the rat hippocampus (Kosaka et al., 1987). They have been considered a subpopulation of GABAergic interneurons, including basket and axo-axonic cell types, which innervate the somata and proximal axons of pyramidal cells, respectively (Soriano et al., 1990)
  > — Rivera et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 10540334_bdfa426a -->

- **PV-IN heterogeneity including axo-axonic cells:** [2]
  > Interneurons expressing the calcium binding protein parvalbumin (PV) make up approximately 40% of all GABAergic interneurons. However, this is a heterogeneous group of functionally distinct interneuron subtypes. For example, in the hippocampus alone, there are at least three functionally and morphologically distinct populations of PV + expressing interneurons, namely basket, axo-axonic and bistratified cells. Fast spiking interneurons in the hippocampus and neocortex are often PV + positive and target the soma of pyramidal cells.
  > — Dannenberg et al. 2017, Classification Schemes and Methodological Approaches · [2] <!-- quote_key: 38778375_462ec931 -->

</details>

Cell Ontology mapping: pvalb chandelier GABAergic interneuron [[CL:4023036](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023036)] (EXACT). CL:4023036 definition matches precisely: cartridge boutons targeting exclusively the AIS of pyramidal cells, fast-spiking PV+ interneuron.

---

## Results

Two candidate atlas entries were assessed — supertype 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] and its child cluster 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] — both at LOW confidence. The atlas supertype name explicitly identifies the chandelier (= axo-axonic) cell type, providing metadata-level EQUIVALENT support. However, the Que 2021 morphologically identified AAC cells (n=6) produce an uninformative AT result due to small n, preventing confidence upgrade above LOW.

**Annotation-transfer overview figure (run-level, filtered)**

![Filtered AT figure for Axo-axonic (chandelier) cell — Yao 2021 Pvalb SSv4 source group](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_axo_axonic_cell_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 SSv4 Pvalb subclass source group (n=66 hippocampal Pvalb cells from GEO:GSE185862). The SSv4 Pvalb label aggregates basket, axo-axonic, and bistratified PV cells; the dominant SUPERTYPE hit is 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] (F1=0.612, 26/66 cells) and the dominant CLUSTER hit is 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] (F1=0.622, 23/66 cells), consistent with the axo-axonic → chandelier supertype correspondence. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.*

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---:|---|---|---|
| 1 | 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] | — (supertype) | 2014 | 🔴 LOW | NT CONSISTENT · type_identity CONSISTENT · location DISCORDANT | Speculative |
| 2 | 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] | 0204 Pvalb chandelier Gaba_1 | 242 | 🔴 LOW | NT CONSISTENT · Pvalb CONSISTENT · type_identity CONSISTENT · location APPROXIMATE | Speculative |

Total: 2 edges; both LOW; relationship EQUIVALENT on both.

### Property alignment — 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] · 🔴 LOW

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | GABA (CLUS_0732) | CONSISTENT |
| Soma location | CA1 stratum pyramidale [UBERON:0014548] | Piriform area dominant (194 cells); no hippocampal pyramidal layer at supertype level | CA1 SO (38 cells); CA3 pyramidal layer (23 cells) (CLUS_0732) | DISCORDANT |
| Pvalb expression | defining marker | Pvalb in DEFINING_SCOPED markers; precomputed mean 7.47 | Pvalb in MERFISH markers; precomputed mean 8.56 (CLUS_0732) | CONSISTENT |
| Type identity | axo-axonic (chandelier) morphology | supertype named "Pvalb chandelier Gaba_1" | cluster named "Pvalb chandelier Gaba_1" | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas supertype metadata (SUPT_0204) | Atlas metadata | SUPPORT | Named "Pvalb chandelier Gaba_1"; Pvalb DEFINING_SCOPED; piriform-dominated anatomy | atlas-internal |
| Yao 2021 SSv4 Pvalb → WMBv1 (GEO:GSE185862) | Annotation transfer | PARTIAL | SUPT_0204 F1=0.612 (26/66 cells, target_purity=1.0); strongest Pvalb supertype hit | atlas-internal |
| Que 2021 patch-seq AAC → WMBv1 (GEO:GSE142546) | Annotation transfer | PARTIAL | n=6 AAC cells; 1/6 map to SUPT_0204; result uninformative due to small n | atlas-internal |

### Property alignment — 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] · 🔴 LOW

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | GABA | CONSISTENT |
| Soma location | CA1 stratum pyramidale [UBERON:0014548] | — | CA1 SO (38 cells); CA3 pyramidal layer (23 cells) | APPROXIMATE |
| Pvalb expression | defining marker | Pvalb chandelier subclass | Pvalb in MERFISH markers; precomputed mean 8.56 | CONSISTENT |
| Type identity | axo-axonic (chandelier) morphology | — | cluster named "Pvalb chandelier Gaba_1" | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas cluster metadata (CLUS_0732) | Atlas metadata | SUPPORT | Named "Pvalb chandelier Gaba_1"; CA1 SO (38), CA3 pyramidal layer (23); Pvalb MERFISH | atlas-internal |
| Yao 2021 SSv4 Pvalb → WMBv1 (GEO:GSE185862) | Annotation transfer | PARTIAL | CLUS_0732 F1=0.622 (23/66 cells, target_purity=1.0); top cluster hit for Pvalb | atlas-internal |
| Que 2021 patch-seq AAC → WMBv1 (GEO:GSE142546) | Annotation transfer | PARTIAL | n=6 AAC cells; 0/6 map to CLUS_0732; 5/6 map to CLUS_0739; result uninformative | atlas-internal |

### 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] · 🔴 LOW

**Supporting evidence**
- Supertype name "Pvalb chandelier Gaba_1" directly identifies the chandelier (= axo-axonic) cell type; Pvalb subclass and GABA NT type are fully consistent. The CL mapping for the classical node (CL:4023036 pvalb chandelier GABAergic interneuron) is EXACT, and the atlas supertype name makes the identity explicit.
- Pvalb present in DEFINING_SCOPED markers confirming PV+ identity; precomputed mean 7.47.
- Yao 2021 SSv4 Pvalb subclass (n=66 HIP cells): SUPT_0204 is the strongest supertype hit (F1=0.612, 26/66 cells, target_purity=1.0). The chandelier-subtype dominance in the Yao mapping is consistent with the axo-axonic → SUPT_0204 correspondence, noting that the SSv4 Pvalb label is morphologically mixed.

**Concerns**
- Soma location DISCORDANT at supertype level: piriform area dominates (194 cells); no hippocampal pyramidal layer listed. Child cluster CLUS_0732 has CA1 SO and CA3 pyramidal layer entries, indicating hippocampal chandelier cells exist within this supertype at cluster level. *(note: supertype location dominated by piriform may reflect the distribution of chandelier cells in this species, but the hippocampal classical type description is specifically in hippocampus — meaningful discordance.)*
- High transcriptomic similarity between PV+ morphological subtypes [3] means chandelier-specific markers are not fully resolved from basket/bistratified cells at supertype level in the atlas metadata.
- DISTRIBUTED_ACROSS_CLUSTERS: supertype likely spans multiple regions (hippocampus + piriform) where axo-axonic cells occur.
- Que 2021 AAC n=6 is insufficient for reliable F1 scoring; AAC AT results are treated as uninformative.

**What would upgrade confidence**
- A dedicated morphologically confirmed AAC patch-seq or targeted dataset (e.g., Ank-GFP × Pvalb-Cre labelled axo-axonic cells) mapped to WMBv1 with F1 ≥ 0.70 at supertype level.
- Cluster-level evidence from CLUS_0732 confirming hippocampal CA1 pyramidal layer soma placement alongside the chandelier-type markers.

### 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] · 🔴 LOW

**Supporting evidence**
- Child of SUPT_0204 (Pvalb chandelier Gaba_1). Cluster name explicitly identifies the hippocampal chandelier cell type. Hippocampal locations: CA1 SO (38 cells), CA1 SR (23 cells), CA3 SO (33 cells), CA3 pyramidal layer (23 cells), CA3 SR (15 cells), dentate gyrus granule cell layer (15 cells). Pvalb in MERFISH markers; precomputed mean 8.56.
- Yao 2021 SSv4 Pvalb (n=66 HIP cells) — CLUS_0732 is the top cluster hit: F1=0.622, 23/66 cells, target_purity=1.0. This is the strongest cluster-level Pvalb hit, consistent with axo-axonic → chandelier correspondence.
- Both cluster and supertype names independently identify the chandelier/axo-axonic cell type; this nomenclature convergence is atlas-internal supporting evidence for the identity claim.

**Concerns**
- CA1 pyramidal layer not listed in cluster cell counts; dominant hippocampal CA1 signal is in CA1 SO (38 cells). *(note: axo-axonic cell somata in classical literature are placed in/near the pyramidal layer of CA1 [UBERON:0014548]; the SO-dominant atlas placement may reflect adjacent-region registration or true SO-border soma placement — mild discordance.)*
- Cck neuropeptide score 8.4 at this cluster is unexpectedly high for a chandelier cell. *(note: may indicate minor contamination or genuine peptide co-expression; requires primary source validation.)*
- Dentate gyrus granule cell layer (15 cells) — chandelier cells in DG are less well characterised; may reflect axo-axonic cells contacting granule cells or a distinct population.
- Que 2021 AAC cells: 0/6 map to CLUS_0732 (5/6 map to CLUS_0739 instead). This failure to detect AAC → CLUS_0732 is uninformative due to n=6 but is technically a null result.

**What would upgrade confidence**
- Morphologically confirmed AAC dataset (n ≥ 20) with F1 ≥ 0.70 at CLUSTER level on CLUS_0732.
- Resolution of the Cck neuropeptide discordance by precomputed stats or primary source re-analysis.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The axo-axonic (chandelier) cell is defined here on a CLASSICAL_MULTIMODAL basis. Defining marker Pvalb [1][3]; soma in CA1 stratum pyramidale [UBERON:0014548] [1]; GABAergic neurotransmission [2]. CL mapping is EXACT to CL:4023036 (pvalb chandelier GABAergic interneuron).

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, type name). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to atlas-side values via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED.

**Annotation transfer.**

Run 1 — Yao 2021 SSv4 hippocampal formation → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4; Pvalb subclass, n=66 HIP cells) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |

Run 2 — Que 2021 patch-seq PV interneurons → WMBv1 (AAC cells only; result uninformative):

| Field | Value |
|---|---|
| Source dataset | GEO:GSE142546 (Que 2021 patch-seq; AAC aggregate n=6; morphologically confirmed axo-axonic cells) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations). Gene symbols remapped to Ensembl IDs. TPM as pseudo-counts. |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 88 (6 AAC cells used for this node) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_scores_aggregated_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/f1_scores_aggregated_best.csv) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | AAC n=6 is insufficient for reliable F1 scoring. Results should be treated as uninformative. 5/6 AAC cells map to CLUS_0739 (basket-type), not CLUS_0732 (chandelier-type), consistent with possible genuine transcriptomic similarity between hippocampal AAC and basket cells (PMID:33398060), or noise from n=6. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:10+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0204 | ATLAS_METADATA; ANNOTATION_TRANSFER ×2 | SUPPORT; PARTIAL; PARTIAL | atlas-internal |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0732 | ATLAS_METADATA; ANNOTATION_TRANSFER ×2 | SUPPORT; PARTIAL; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Axo-axonic (chandelier) cell → 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] at LOW confidence, with child cluster 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] also at LOW confidence. Key support: atlas supertype and cluster names explicitly identify the chandelier cell type; Pvalb expression confirmed in both; Yao 2021 SSv4 Pvalb label maps most strongly to SUPT_0204 (F1=0.612) and CLUS_0732 (F1=0.622) among all Pvalb targets; CL mapping is EXACT to CL:4023036. Key caveats: soma location DISCORDANT at supertype level (piriform-dominated anatomy); Que 2021 AAC cells n=6 insufficient for reliable F1 (uninformative); high transcriptomic similarity between PV+ subtypes prevents confident resolution from atlas metadata alone.

The EXACT Cell Ontology mapping (pvalb chandelier GABAergic interneuron [[CL:4023036](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023036)]) is a strong conceptual anchor for this type. Unlike the other PV+ subtypes in this graph (PV basket cell: BROAD; bistratified: BROAD), the axo-axonic cell has a specific CL term that fully captures its identity. The atlas naming ("chandelier") explicitly mirrors this CL term, making the identity claim strong at the nomenclature level; the evidence gap is the AT confirmation with adequate cell numbers.

### Proposed experiments and follow-ups

1. **Morphologically confirmed AAC annotation transfer.** New patch-seq or Ank-GFP × Pvalb-Cre labelled axo-axonic cell dataset (n ≥ 20, adult mice) mapped to WMBv1. Target: F1 ≥ 0.70 at supertype and cluster level on SUPT_0204 and CLUS_0732. Expected output: AnnotationTransferEvidence upgrading confidence from LOW to MODERATE or HIGH. Resolves: uninformative AAC Que 2021 result (n=6 insufficient).

2. **Cck discordance investigation at CLUS_0732.** Confirm or refute the Cck neuropeptide score 8.4 in the cluster underlying data. Expected output: MarkerAnalysisEvidence resolving the unexpected CCK expression signal.

3. **Hippocampal pyramidal layer soma count verification.** Check whether CLUS_0732 cells in CA1 pyramidal layer exist but are below the reporting threshold, or whether the soma placement is genuinely SO-dominant. *(note: this is an atlas metadata query, not a new experiment.)*

### Open questions

1. Are hippocampal axo-axonic cells transcriptomically separable from PV basket cells in the WMBv1 data? Que 2021 AAC n=6 is uninformative; this is the central unresolved question.

2. Does the piriform-dominated anatomy of SUPT_0204 mean that hippocampal AAC cells are a minor subpopulation within this supertype, or that the atlas over-represents piriform chandelier cells relative to hippocampal?

3. What is the biological basis for the Cck neuropeptide expression score 8.4 at CLUS_0732, given that axo-axonic cells are PV+ and not classically CCK-expressing?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 | [25018703](https://pubmed.ncbi.nlm.nih.gov/25018703) | soma location; Pvalb marker |
| [2] | Dannenberg et al. 2017 | [29321728](https://pubmed.ncbi.nlm.nih.gov/29321728) | neurotransmitter type; PV-IN subtypes |
| [3] | Que et al. 2021 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060) | Pvalb marker; PV subtype transcriptomic similarity |
