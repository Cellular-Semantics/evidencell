# Axo-axonic (chandelier) cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | pvalb chandelier GABAergic interneuron (CL:4023036) | |
| Soma location | CA1 stratum pyramidale [UBERON:0005401] | [1] |
| NT | GABAergic | [2] |
| Markers | Pvalb+ | [1] [3] |

*Notes: One of three canonical PV+ interneuron subtypes alongside basket and bistratified cells. Limited hippocampus-specific electrophysiology data in this reference set.*

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] | — | — | 🔴 LOW | Pvalb CONSISTENT · location DISCORDANT | Speculative |
| 2 | 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] | — | — | 🔴 LOW | Pvalb CONSISTENT · location APPROXIMATE | Speculative |

2 edges total · all `EQUIVALENT`

---

## 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] · 🔴 LOW

**Supporting evidence:**

- **Atlas metadata (SUPPORT):** Supertype name "Pvalb chandelier Gaba_1" directly identifies the chandelier (= axo-axonic) cell type. Pvalb is present in DEFINING_SCOPED markers (precomputed stats mean: 7.47), confirming PV+ identity. GABA neurotransmitter type is fully consistent with GABAergic. The CL mapping for the classical node (CL:4023036 pvalb chandelier GABAergic interneuron) is EXACT, and the atlas supertype name makes the chandelier identity explicit. EQUIVALENT declared because the supertype is named for and defined by the chandelier/axo-axonic cell type.
- **Annotation transfer (PARTIAL):** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 Pvalb subclass (n=66 HIP cells) onto WMBv1. SUPT_0204 [CS20230722_SUPT_0204] is the top supertype hit for Pvalb cells (F1=0.612, 26/66 cells, target_purity=1.0). The chandelier label in WMBv1 corresponds to axo-axonic cells. PARTIAL because the SSv4 Pvalb subclass label is a mixed population encompassing PV basket, axo-axonic, and bistratified cells; nevertheless, SUPT_0204 being the single strongest Pvalb supertype target is consistent with the axo-axonic cell correspondence. Subtype resolution requires a morphologically identified PV-IN dataset.

**Marker evidence provenance:**

- **Pvalb (defining marker):** Evidence is multi-modal. [1] provides immunofluorescence-based localization of Pvalb+ cells in the rat hippocampus, noting that PV+ cells include basket and axo-axonic subtypes in strata oriens and pyramidale; classical type specificity relies on the cited morphological classification rather than a directly reconstructed chandelier cell. [3] provides scRNA-seq-level evidence (precomputed expression stats); while not morphologically confirmed for axo-axonic cells specifically, the Pvalb chandelier subclass in WMBv1 is annotated and the mean expression (7.47 at supertype level) is consistent. One citation entry appears duplicated in the facts file for [3] — the underlying data source is a single paper and this does not affect the evidence weight. Primary evidence for Pvalb as a chandelier-cell marker in morphologically confirmed material would strengthen the provenance chain.

**Concerns:**

- **location_CA1_stratum_pyramidale (DISCORDANT):** Classical soma location is CA1 stratum pyramidale [UBERON:0005401]; atlas supertype anatomy is dominated by piriform area with no hippocampal pyramidal layer listed at supertype level. *(note: piriform area is anatomically distant from hippocampal CA1 — this is stronger counter-evidence. The classical type is expected in hippocampal CA1, not piriform cortex. The supertype is likely distributed across all brain regions where axo-axonic cells occur, and hippocampal chandelier cells may be resolvable only at cluster level — see CLUS_0732 edge.)*
- **DISTRIBUTED_ACROSS_CLUSTERS caveat:** Supertype anatomy is piriform-dominated at top level; hippocampal chandelier cells should be resolvable at cluster level (see 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732]). Supertype likely spans multiple regions.
- **MARKER_NOT_SPECIFIC caveat:** High transcriptomic similarity between PV+ morphological subtypes [3] means chandelier-specific markers are not fully resolved at supertype level from basket/bistratified cells in the atlas metadata.

**What would upgrade confidence:**

- **Annotation transfer with a morphologically confirmed chandelier cell dataset:** A morphologically identified PV axo-axonic cell scRNA-seq dataset mapped to WMBv1 using MapMyCells targeting SUPT_0204 [CS20230722_SUPT_0204] at F1 ≥ 0.70 at SUPERTYPE level would provide AnnotationTransferEvidence sufficient to upgrade to MODERATE. Dataset GEO:GSE185862 (Yao 2021 SSv4) is available but does not resolve PV subtypes; a subtype-resolved source is needed.
- **Targeted literature search:** A cite-traverse for "chandelier cell axo-axonic hippocampus parvalbumin transcriptomics" may identify primary studies with morphologically confirmed chandelier cells and transcriptomic profiling that could be cross-checked against SUPT_0204 metadata.
- **Hippocampal location confirmation at cluster level:** If CLUS_0732 (child of this supertype) shows strong hippocampal enrichment with MODERATE confidence, the supertype edge confidence may be reviewed in context.

---

## 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] · 🔴 LOW

**Supporting evidence:**

- **Atlas metadata (SUPPORT):** Child of SUPT_0204 (Pvalb chandelier Gaba_1). Hippocampal locations: CA1 SO (38 cells), CA1 SR (23 cells), CA3 SO (33 cells), CA3 pyramidal layer (23 cells), CA3 SR (15 cells), dentate gyrus granule cell layer (15 cells). Pvalb in MERFISH markers confirms PV+ identity (precomputed stats mean: 8.56). Cluster name "0732 Pvalb chandelier Gaba_1" explicitly identifies it as a hippocampal chandelier cell cluster. GABA NT type consistent. Neuropeptides Cck (8.4), Pthlh, and Npy are present; Cck at a high score is unexpected for chandelier cells and warrants noting.
- **Annotation transfer (PARTIAL):** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 Pvalb subclass (n=66 HIP cells) onto WMBv1. CLUS_0732 [CS20230722_CLUS_0732] is the top cluster hit for Pvalb cells (F1=0.622, 23/66 cells, target_purity=1.0) — the strongest cluster-level hit among all Pvalb targets, consistent with the axo-axonic → chandelier supertype correspondence. PARTIAL because the source label is a mixed Pvalb population. Subtype resolution requires a morphologically identified PV-IN dataset.

**Marker evidence provenance:**

- **Pvalb (defining marker):** As for SUPT_0204 above. At cluster level, MERFISH marker data provides an independent spatial confirmation of Pvalb expression (mean: 8.56, higher than parent supertype 7.47), strengthening the Pvalb marker alignment for this cluster specifically. The slight increase in mean expression at cluster vs supertype level is consistent with CLUS_0732 being a more homogeneous PV+ population than its parent.

**Concerns:**

- **location_CA1_stratum_pyramidale (APPROXIMATE):** Classical soma location is CA1 stratum pyramidale [UBERON:0005401]; cluster shows CA1 SO (38 cells) as the dominant CA1 hippocampal location, with CA3 pyramidal layer (23 cells) also present. CA1 pyramidal layer is not explicitly listed. *(note: CA1 stratum oriens is directly adjacent to stratum pyramidale — this is weak counter-evidence consistent with border-zone registration or soma placement near the SO/SP boundary. The discrepancy does not strongly argue against chandelier cell identity.)*
- **MARKER_NOT_SPECIFIC caveat:** Cck neuropeptide score (8.4) is unexpectedly high for a chandelier cell. Chandelier cells are classically PV+/CCK− and do not characteristically express CCK. May indicate minor cluster contamination by CCK+ interneurons or genuine low-level peptide co-expression. Requires primary source validation before this cluster can be confidently assigned to a pure axo-axonic population.
- **OTHER caveat:** Dentate gyrus granule cell layer (15 cells) — chandelier cells in DG are less well characterised. *(note: axo-axonic cells targeting granule cells in the DG molecular layer or hilus have been described, but their abundance and transcriptomic profile relative to CA1 chandelier cells is not established in this reference set. These cells may constitute a distinct population.)* Requires primary source confirmation.

**What would upgrade confidence:**

- **Morphologically confirmed annotation transfer:** Same requirement as SUPT_0204. A morphologically identified axo-axonic cell dataset mapped to WMBv1 with F1 ≥ 0.70 at CLUSTER level against CLUS_0732 [CS20230722_CLUS_0732] would provide AnnotationTransferEvidence sufficient to upgrade to MODERATE.
- **Cck expression resolution:** Primary literature confirming (or refuting) Cck co-expression in chandelier cells would resolve the Cck neuropeptide caveat. A targeted cite-traverse for "chandelier cell CCK neuropeptide hippocampus" is recommended.
- **DG chandelier cell characterisation:** A targeted search for "dentate gyrus axo-axonic cell" or "granule cell chandelier" would clarify whether the 15 DG-located cells in CLUS_0732 represent a known DG chandelier population.

---

## Proposed experiments

MapMyCells annotation transfer with morphologically resolved source data has partially been completed (Yao 2021 SSv4 Pvalb subclass; see evidence items above). The current round used a mixed Pvalb population and is insufficient for subtype-level confidence. A refined experiment is warranted.

**Annotation transfer — morphologically confirmed PV axo-axonic cell dataset**

- **What:** MapMyCells default parameters, WMBv1 (CCN20230722) as target atlas
- **Target:** F1 ≥ 0.70 at SUPERTYPE level (SUPT_0204 [CS20230722_SUPT_0204]) and F1 ≥ 0.70 at CLUSTER level (CLUS_0732 [CS20230722_CLUS_0732])
- **Expected output:** AnnotationTransferEvidence entries on both edges; if F1 threshold met, upgrade edge confidence to MODERATE
- **Resolves:** Both edges; the core limitation that the Yao 2021 SSv4 source label is a mixed Pvalb population

**Targeted literature search — chandelier cell transcriptomics**

- **What:** cite-traverse or manual search for primary studies with morphologically confirmed chandelier cells + transcriptomic profiling (patch-seq, Cre-driver single-cell, or scRNA-seq with morphological reconstruction)
- **Target:** At least one study confirming Pvalb expression in morphologically identified chandelier cells in mouse hippocampus
- **Expected output:** LiteratureEvidence item on one or both edges; may also resolve the Cck neuropeptide discrepancy and the DG cell caveat
- **Resolves:** Marker evidence provenance weakness on both edges; Cck discrepancy on CLUS_0732 edge

---

## Open questions

1. Does CLUS_0732 [CS20230722_CLUS_0732] represent a hippocampus-enriched subpopulation of the broader chandelier supertype (SUPT_0204 [CS20230722_SUPT_0204]), consistent with what is known about chandelier cell distribution? *(appears on both edges)*
2. What is the source of the high Cck neuropeptide score (8.4) in CLUS_0732? Is this genuine chandelier-cell co-expression, minor contamination by CCK+ basket cells, or a cluster boundary artefact?
3. Do the 15 dentate-gyrus-granule-cell-layer cells in CLUS_0732 represent a distinct DG chandelier population, or do they reflect soma placement near the granule/molecular layer border?

---

## Evidence base

| Edge | Evidence type | Supports |
|---|---|---|
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0204 | Atlas metadata | SUPPORT |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0204 | Annotation transfer (MapMyCells) | PARTIAL |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0732 | Atlas metadata | SUPPORT |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0732 | Annotation transfer (MapMyCells) | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 · PMID:25018703 | [25018703](https://pubmed.ncbi.nlm.nih.gov/25018703/) | soma location |
| [2] | Dannenberg et al. 2017 · PMID:29321728 | [29321728](https://pubmed.ncbi.nlm.nih.gov/29321728/) | neurotransmitter type |
| [3] | Que et al. 2021 · PMID:33398060 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060/) | Pvalb marker |
