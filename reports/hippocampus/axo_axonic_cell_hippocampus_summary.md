# Axo-axonic (chandelier) cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | pvalb chandelier GABAergic interneuron (CL:4023036) — EXACT mapping | — |
| Soma location | Stratum pyramidale [UBERON:0005401] (CA1) | [1] |
| Neurotransmitter | GABAergic | [2] |
| Defining markers | Pvalb | [1] [3] |
| Negative markers | — | — |
| Neuropeptides | None listed | — |

> "Parvalbumin + cells were specifically localized in the granular and polymorphic cell layers of the dentate gyrus and the strata oriens and pyramidale in CA1/3 fields of the rat hippocampus (Kosaka et al., 1987). They have been considered a subpopulation of GABAergic interneurons, including basket and axo-axonic cell types, which innervate the somata and proximal axons of pyramidal cells, respectively (Soriano et al., 1990)"
> — Rivera et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 10540334_bdfa426a -->

> "Interneurons expressing the calcium binding protein parvalbumin (PV) make up approximately 40% of all GABAergic interneurons. However, this is a heterogeneous group of functionally distinct interneuron subtypes. For example, in the hippocampus alone, there are at least three functionally and morphologically distinct populations of PV + expressing interneurons, namely basket, axo-axonic and bistratified cells. Fast spiking interneurons in the hippocampus and neocortex are often PV + positive and target the soma of pyramidal cells."
> — Dannenberg et al. 2017, Classification Schemes and Methodological Approaches · [2] <!-- quote_key: 38778375_462ec931 -->

**Notes.** One of three canonical PV+ interneuron subtypes alongside basket and bistratified cells. Limited hippocampus-specific electrophysiology data in this reference set.

---

## Mapping candidates

| Rank | WMBv1 cluster / supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| 1 | 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] (supertype) | — | 🔴 LOW | Pvalb CONSISTENT · type_identity CONSISTENT · location DISCORDANT | Speculative |
| 2 | 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] (cluster) | — | 🔴 LOW | Pvalb CONSISTENT · type_identity CONSISTENT · location APPROXIMATE | Speculative |

2 edges total · all EQUIVALENT.

---

## 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] · 🔴 LOW

**Supporting evidence**

- Supertype name "Pvalb chandelier Gaba_1" directly identifies the chandelier (= axo-axonic) cell type. Pvalb subclass and GABA NT type are fully consistent. The CL mapping (CL:4023036 pvalb chandelier GABAergic interneuron) is EXACT and the atlas supertype name makes the chandelier identity explicit. EQUIVALENT relationship declared because the supertype is named for and defined by the chandelier/axo-axonic cell type.
- Pvalb is present in DEFINING_SCOPED markers; precomputed stats mean = 7.47, confirming PV+ identity. CONSISTENT.
- Annotation transfer (MapMyCells, Yao 2021 GEO:GSE185862, n=66 HIP Pvalb cells): SUPT_0204 is the top supertype hit for Pvalb cells (F1=0.612, 26/66 cells, purity=1.0). The chandelier label in WMBv1 corresponds directly to axo-axonic cells. PARTIAL because the SSv4 Pvalb subclass label is a mixed population (PV basket + axo-axonic + bistratified cells); the strength of the chandelier supertype signal is nonetheless consistent with the axo-axonic cell correspondence.

**Marker evidence provenance**

- **Pvalb**: Rivera et al. 2014 [1] provides IHC-based localisation of Pvalb+ cells in rat hippocampus noting that PV+ cells include basket and axo-axonic subtypes in strata oriens and pyramidale; classical type specificity relies on the cited morphological classification. Que et al. 2021 [3] provides scRNA-seq-level evidence. The Pvalb chandelier subclass in WMBv1 is explicitly annotated; precomputed mean expression (7.47) is consistent with PV+ identity. One citation entry appears duplicated in the facts file for [3] — the underlying data source is a single paper and this does not affect evidence weight.

**Concerns**

- **location_CA1_stratum_pyramidale (DISCORDANT)**: Classical soma location is CA1 stratum pyramidale [UBERON:0005401]; atlas supertype anatomy is dominated by piriform area (194 cells) with no hippocampal pyramidal layer listed at supertype level. *(note: piriform area is anatomically distant from hippocampal CA1 — this is stronger counter-evidence. The supertype likely spans all brain regions where axo-axonic cells occur; hippocampal chandelier cells should be resolvable at cluster level — see CLUS_0732 edge.)*
- DISTRIBUTED_ACROSS_CLUSTERS: supertype anatomy is piriform-dominated at top level; hippocampal chandelier cells should be resolvable at cluster level.
- High transcriptomic similarity between PV+ morphological subtypes [3] means chandelier-specific markers are not fully resolved at supertype level from basket/bistratified cells in atlas metadata.

**What would upgrade confidence**

- **Annotation transfer with a morphologically confirmed chandelier cell dataset**: MapMyCells (local, WMBv1/CCN20230722) using a morphologically identified axo-axonic cell dataset (e.g. Cre-driver + AIS-targeting confirmation). Target: F1 ≥ 0.70 at SUPERTYPE level for SUPT_0204 [CS20230722_SUPT_0204]. Output: `AnnotationTransferEvidence`.
- **Targeted literature search**: Cite-traverse for "chandelier cell axo-axonic hippocampus parvalbumin transcriptomics" to identify primary studies with morphologically confirmed chandelier cells and transcriptomic profiling.
- **Hippocampal location confirmation at cluster level**: CLUS_0732 (child of this supertype) shows hippocampal enrichment — strong cluster-level evidence would contextualise the supertype edge.

---

## 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] · 🔴 LOW

**Supporting evidence**

- Child of SUPT_0204 (Pvalb chandelier Gaba_1). Hippocampal locations: CA1 SO (38 cells), CA1 SR (23 cells), CA3 SO (33 cells), CA3 pyramidal layer (23 cells), CA3 SR (15 cells), dentate gyrus granule cell layer (15 cells). Pvalb in MERFISH markers confirms PV+ identity (precomputed stats mean: 8.56). Cluster name "0732 Pvalb chandelier Gaba_1" explicitly identifies it as a hippocampal chandelier cell cluster. GABA NT type consistent.
- Annotation transfer (MapMyCells, Yao 2021 GEO:GSE185862, n=66 HIP Pvalb cells): CLUS_0732 is the top cluster hit for Pvalb cells (F1=0.622, 23/66 cells, purity=1.0) — the strongest cluster-level hit among all Pvalb targets, consistent with the axo-axonic → chandelier correspondence. PARTIAL because the source label is a mixed Pvalb population.

**Marker evidence provenance**

- **Pvalb**: As for SUPT_0204 above. At cluster level, MERFISH marker data provides an independent spatial confirmation of Pvalb expression (mean: 8.56, higher than parent supertype 7.47), strengthening the Pvalb marker alignment for this cluster specifically.
- **Cck (neuropeptide — unexpected)**: Cck neuropeptide score (8.4; precomputed stats mean not specified at cluster level) is unexpectedly high for a chandelier cell. Chandelier cells are classically PV+/CCK−. May indicate minor cluster contamination by CCK+ interneurons or genuine low-level peptide co-expression. Requires primary source validation.

**Concerns**

- **location_CA1_stratum_pyramidale (APPROXIMATE)**: Classical soma location is CA1 stratum pyramidale [UBERON:0005401]; cluster shows CA1 SO (38 cells) as the dominant CA1 hippocampal location, with CA3 pyramidal layer (23 cells) present. CA1 pyramidal layer is not explicitly listed. *(note: CA1 stratum oriens is directly adjacent to stratum pyramidale — this is weak counter-evidence consistent with border-zone soma placement.)*
- Cck neuropeptide score (8.4) is unexpectedly high for a chandelier cell. Chandelier cells are classically PV+/CCK− and do not characteristically express CCK. May indicate minor cluster contamination or genuine low-level peptide co-expression. Requires primary source validation before this cluster can be confidently assigned to a pure axo-axonic population.
- Dentate gyrus granule cell layer (15 cells) — chandelier cells in DG are less well characterised. *(note: axo-axonic cells targeting granule cells in the DG have been described, but their abundance and transcriptomic profile relative to CA1 chandelier cells is not established in this reference set.)*
- Annotation transfer is PARTIAL: source label is a mixed Pvalb population; subtype resolution requires a morphologically confirmed source.

**What would upgrade confidence**

- **Morphologically confirmed annotation transfer**: A morphologically identified axo-axonic cell dataset mapped to WMBv1 with F1 ≥ 0.70 at CLUSTER level against CLUS_0732 [CS20230722_CLUS_0732]. Output: `AnnotationTransferEvidence`.
- **Cck expression resolution**: Cite-traverse for "chandelier cell CCK neuropeptide hippocampus" to resolve the Cck neuropeptide caveat. Output: `LiteratureEvidence`.
- **DG chandelier cell characterisation**: Targeted search for "dentate gyrus axo-axonic cell" or "granule cell chandelier" to clarify whether the 15 DG-located cells represent a known DG chandelier population.

---

## Proposed experiments

### Annotation transfer — morphologically confirmed PV axo-axonic cell dataset

MapMyCells annotation transfer with Yao 2021 SSv4 Pvalb subclass (GEO:GSE185862, n=66 HIP cells) has been completed. SUPT_0204 is the strongest supertype hit (F1=0.612, 26 cells); CLUS_0732 is the strongest cluster hit (F1=0.622, 23 cells). The source label is a mixed Pvalb population and is insufficient for subtype-level confidence. A refined experiment is warranted.

- **What**: MapMyCells default parameters, WMBv1 (CCN20230722) as target atlas; source: morphologically confirmed PV axo-axonic cell dataset (post-hoc AIS-targeting morphology or patch-seq)
- **Target**: F1 ≥ 0.70 at SUPERTYPE level (SUPT_0204 [CS20230722_SUPT_0204]) and F1 ≥ 0.70 at CLUSTER level (CLUS_0732 [CS20230722_CLUS_0732])
- **Expected output**: `AnnotationTransferEvidence` entries on both edges; confidence upgrade to MODERATE if threshold met
- **Resolves**: Both edges; core limitation that the Yao 2021 SSv4 source is a mixed Pvalb population

### Targeted literature search — chandelier cell transcriptomics

- **What**: Cite-traverse for "chandelier cell axo-axonic hippocampus parvalbumin transcriptomics" and "chandelier cell CCK neuropeptide hippocampus"
- **Expected output**: `LiteratureEvidence` items on both edges; resolution of the Cck neuropeptide discrepancy on CLUS_0732 and the DG cell caveat
- **Resolves**: Marker evidence provenance weakness; Cck discrepancy on CLUS_0732 edge

---

## Open questions

1. Does CLUS_0732 [CS20230722_CLUS_0732] represent a hippocampus-enriched subpopulation of the broader chandelier supertype (SUPT_0204 [CS20230722_SUPT_0204]), consistent with what is known about chandelier cell distribution?
2. What is the source of the high Cck neuropeptide score (8.4) in CLUS_0732? Is this genuine chandelier-cell co-expression, minor contamination by CCK+ basket cells, or a cluster boundary artefact?
3. Do the 15 dentate-gyrus-granule-cell-layer cells in CLUS_0732 represent a distinct DG chandelier population, or do they reflect soma placement near the granule/molecular layer border?

---

## Evidence base table

| Edge ID | Evidence type | Supports | Notes |
|---|---|---|---|
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0204 | ATLAS_METADATA (Pvalb chandelier name, GABA NT, Pvalb DEFINING_SCOPED) | SUPPORT | Supertype anatomy piriform-dominated; no hippocampal SP at supertype level |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0204 | ANNOTATION_TRANSFER (MapMyCells, GEO:GSE185862, n=66) | PARTIAL | F1=0.612 at SUPT level; top Pvalb supertype hit; mixed source population |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0732 | ATLAS_METADATA (Pvalb chandelier name, hippocampal locations, Cck caveat) | SUPPORT | CA1 SP absent; CA1 SO dominant; Cck neuropeptide 8.4 unexpected |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0732 | ANNOTATION_TRANSFER (MapMyCells, GEO:GSE185862, n=66) | PARTIAL | F1=0.622 at CLUS level; top Pvalb cluster hit; mixed source population |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 | [25018703](https://pubmed.ncbi.nlm.nih.gov/25018703/) | Soma location; Pvalb marker |
| [2] | Dannenberg et al. 2017 | [29321728](https://pubmed.ncbi.nlm.nih.gov/29321728/) | Neurotransmitter type; PV+ interneuron heterogeneity |
| [3] | Que et al. 2021 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060/) | Pvalb marker; transcriptomic landscape of PV interneurons |
