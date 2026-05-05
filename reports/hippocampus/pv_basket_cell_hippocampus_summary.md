# Parvalbumin-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | basket cell (CL:0000118) — BROAD mapping | — |
| Soma location | Stratum pyramidale [UBERON:0005401] (CA1 and CA3); dentate gyrus granule cell layer [UBERON:0001885] | [1] [2] [3] [4] |
| Neurotransmitter | GABAergic | [5] |
| Defining markers | Pvalb, Gad1, Gad2 | Pvalb: [1] [6] [7] [8] |
| Negative markers | Cnr1 | — |
| Neuropeptides | None listed | — |

> "Parvalbumin + cells were specifically localized in the granular and polymorphic cell layers of the dentate gyrus and the strata oriens and pyramidale in CA1/3 fields of the rat hippocampus (Kosaka et al., 1987). They have been considered a subpopulation of GABAergic interneurons, including basket and axo-axonic cell types, which innervate the somata and proximal axons of pyramidal cells, respectively (Soriano et al., 1990)"
> — Rivera et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 10540334_bdfa426a -->

> "Fast spiking interneurons in the CA1 area of the dorsal hippocampus were recorded from and filled with biocytin in anesthetized rats. The full extent of their dendrites and axonal arborizations as well as their calcium binding protein content were examined. Based on the spatial extent of axon collaterals, local circuit cells (basket and O- LM neurons) and long-range cells (bistratified, trilaminar, and backprojection neurons) could be distinguished. Basket cells were immunoreactive for parvalbumin and their axon collaterals were confined to the pyramidal layer. A single basket cell contacted more than 1500 pyramidal neurons and 60 other parvalbumin-positive interneurons. Commissural stimulation directly discharged basket cells, followed by an early and late IPSPs, indicating interneuronal inhibition of basket cells. The dendrites of another local circuit neuron (O-LM) were confined to stratum oriens and it had a small but high-density axonal terminal field in stratum lacunosum-moleculare. The fastest firing cell of all interneurons was a calbindin-immunoreactive bistratified neuron with axonal targets in stratum oriens and radiatum. Two neurons with their cell bodies in the alveus innervated the CA3 region (backprojection cells), in addition to rich axon collaterals in the CA1 region. The trilaminar interneuron had axon collaterals in strata radiatum, oriens and pyramidale with its dendrites confined to stratum oriens. Commissural stimulation evoked an early EPSP-IPSP-late depolarizing potential sequence in this cell. All interneurons formed symmetric synapses with their targets at the electron microscopic level. These findings indicate that interneurons with distinct axonal targets have differential functions in shaping the physiological patterns of the CA1 network."
> — Sik et al. 1995, Anatomical Location and Morphology · [2] <!-- quote_key: 10664418_9acd7ec1 -->

**Notes.** Four morphological subtypes are recognised within PV+ interneurons (basket, axo-axonic, bistratified, radiatum-targeting). Activity of PV basket cells is inversely coupled with CCK basket cell activity.

---

## Mapping candidates

| Rank | WMBv1 cluster / supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| 1 | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] (supertype) | — | 🟡 MODERATE | Pvalb CONSISTENT · Cnr1 CONSISTENT | Best candidate (supertype) |
| 2 | 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] (cluster) | — | 🟡 MODERATE | Pvalb CONSISTENT · Cck DISCORDANT | Best candidate (cluster) |

2 edges total; both PARTIAL_OVERLAP. No UNCERTAIN edges.

---

## 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] · 🟡 MODERATE

**Supporting evidence**

- Pvalb subclass and GABA neurotransmitter type are fully consistent with PV basket cell identity. The supertype name "Pvalb Gaba_2" directly reflects PV+ GABA interneuron identity. NT type: GABAergic vs GABA — CONSISTENT.
- Precomputed stats (atlas metadata) confirm all three defining markers: Pvalb (mean 8.74), Gad1 (mean 10.34), Gad2 (mean 9.28) — strong quantitative support across the supertype.
- Negative marker Cnr1 is low/absent in precomputed stats (mean 1.93), consistent with the expected Cnr1-negative profile of PV basket cells — CONSISTENT.
- CA1 stratum oriens (818 cells) and CA3 stratum oriens (152 cells) are appropriate perisomatic interneuron locations within hippocampus — APPROXIMATE (main hippocampal signal is SO, not SP directly).
- Annotation transfer (MapMyCells, Yao 2021 GEO:GSE185862, n=66 HIP Pvalb cells): SUPT_0206 receives 12/66 Pvalb cells with target_purity=0.800 (80% of mapped SUPT_0206 cells are from the Pvalb group). PARTIAL because the SSv4 Pvalb label is a mixed population (basket + axo-axonic + bistratified cells); chandelier/AAC cells dominate the mapping.

**Marker evidence provenance**

- **Pvalb**: Evidence is both protein-level (IHC — Rivera et al. 2014 [1]) and transcript-level (Que et al. 2021 [6]; Perrenoud et al. 2022 [7]; Contreras et al. 2019 [8]). Cell-type specificity is well-established — Pvalb identifies a major class of perisomatic interneurons and the basket/axo-axonic/bistratified subtypes share this marker. Precomputed stats mean of 8.74 confirms high expression in SUPT_0206. Evidence is strong across multiple methods and independent studies.
- **Gad1 / Gad2**: Listed as defining markers on the classical node but carry no specific citations. Atlas support derives from GABA NT classification (APPROXIMATE) and precomputed stats (Gad1 mean 10.34, Gad2 mean 9.28 in SUPT_0206). The lack of specific primary citations on the classical node is a minor gap — Gad1/Gad2 co-expression with Pvalb in hippocampal PV interneurons is widely established, but the KB entry should carry at least one primary citation. A targeted cite-traverse for "Pvalb Gad1 basket cell hippocampus" could resolve this.
- **Cnr1 (negative marker)**: No specific citation for Cnr1 negativity on the classical node. The distinction between CCK basket cells (Cnr1-positive) and PV basket cells (Cnr1-negative) is a canonical distinction referenced in the CCK/PV literature [5] [8], but the classical node lacks a direct primary citation confirming absence in morphology-verified PV basket cells. Precomputed stats value of 1.93 is consistent with low/absent expression. A primary citation specifically testing Cnr1 on morphology-confirmed PV basket cells would strengthen this entry.

**Concerns**

- Location APPROXIMATE: classical soma location is stratum pyramidale [UBERON:0005401]; the atlas supertype's dominant hippocampal signal is CA1 stratum oriens (818 cells) rather than CA1 pyramidal layer. *(note: stratum oriens and stratum pyramidale are adjacent layers in CA1 — SO lies directly below SP; soma placement discrepancy may reflect border cells or atlas resolution limits; this is weak counter-evidence.)*
- The supertype spans piriform area (959 cells) in addition to hippocampal subfields — it is not hippocampus-specific. Multiple PV+ morphological subtypes (basket, axo-axonic, bistratified) co-populate the Pvalb Gaba subclass with high transcriptomic similarity and may not be separable at supertype level.
- Annotation transfer is PARTIAL: the dominant mapping target is 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] (F1=0.612, 26 cells) rather than SUPT_0206 (F1=0.324, 12 cells), reflecting enrichment of axo-axonic/chandelier cells in the Yao 2021 SSv4 Pvalb dataset. Subtype resolution requires a morphologically identified PV-IN dataset.
- Gad1 and Gad2 are not present in the supertype's defining markers; their APPROXIMATE alignment is based on GABA NT type consistency and precomputed stats rather than direct marker-level confirmation in atlas metadata.

**What would upgrade confidence**

- **Annotation transfer with a morphologically identified PV basket cell dataset**: Use a dataset where PV basket cell identity is confirmed (e.g. Cre-driver + morphological reconstruction, or patch-clamp followed by biocytin fill) and re-run MapMyCells targeting WMBv1 (CCN20230722). Target: F1 ≥ 0.80 at CLUSTER level. Output would be `AnnotationTransferEvidence`. This would directly distinguish basket from axo-axonic/chandelier contributions and resolve the dominant-mapping ambiguity.
- **Targeted cite-traverse**: Search for primary literature confirming Cnr1 negativity and Gad1/Gad2 co-expression in morphology-confirmed PV basket cells (e.g. "Cnr1 PV basket cell hippocampus mouse" and "Pvalb Gad1 basket cell hippocampus"). Would add `LiteratureEvidence` to the classical node marker entries.
- **Hippocampus-specific atlas query**: Identify whether any child clusters of SUPT_0206 are more hippocampus-restricted (see cluster-level edge below for CLUS_0739).

---

## 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] · 🟡 MODERATE

**Supporting evidence**

- Child of 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206]. Inherits GABA NT and Pvalb identity support from parent supertype.
- Hippocampal enrichment at cluster level: CA1 SO (124 cells), CA3 SO (80 cells), CA1 pyramidal layer (26 cells), CA1 SR (45 cells). The 26 CA1 pyramidal layer cells are a direct match to the classical soma location in stratum pyramidale [UBERON:0005401] — APPROXIMATE overall (small count, main signal in SO).
- Precomputed stats: Pvalb=10.63 (highest Pvalb expression among SUPT_0206 child clusters), Gad1=10.52, Gad2=8.43 — all strong. Cnr1=1.68 (low/absent) — CONSISTENT with negative marker expectation.
- Annotation transfer (MapMyCells, Yao 2021 GEO:GSE185862): CLUS_0739 receives 5/66 Pvalb cells with target_purity=1.0 (all 5 are from the Pvalb group). PARTIAL because the dominant cluster hit is 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] (F1=0.622, 23 cells), not CLUS_0739 (F1=0.179, 5 cells).

**Marker evidence provenance**

- **Pvalb, Gad1, Gad2, Cnr1**: Same as SUPT_0206 edge above. Precomputed stats are stronger at cluster level: Pvalb=10.63 is the highest among SUPT_0206 children, supporting this cluster as the most Pvalb-enriched node within the supertype.
- **Cck (neuropeptide — DISCORDANT)**: Cck is present in the cluster's neuropeptide list (expression score 7.6; precomputed stats mean 7.56). No Cck expression is expected for PV basket cells, which are defined in part by their Cnr1/CB1R-negative, non-CCK profile. The CCK/PV distinction in perisomatic hippocampal interneurons is well-established [5] [8]. This is a genuine DISCORDANT signal. Two interpretations are possible: (a) the cluster contains a mixed population including PV cells that co-express low levels of Cck, or (b) the cluster boundaries do not align cleanly to classical PV basket cell identity and include CCK-co-expressing neurons. Neither interpretation is resolved by atlas metadata alone.

**Concerns**

- **Cck neuropeptide DISCORDANT** (primary concern): High Cck expression score (7.6; precomputed stats 7.56) in CLUS_0739 is the most significant counter-evidence for this edge. PV basket cells are expected to be Cck-negative [5] [8]; the Cck signal could indicate mixed cluster content or non-specific peptide expression.
- Location APPROXIMATE: 26 CA1 pyramidal layer cells vs 124 in CA1 SO — the pyramidal layer signal exists but is not dominant. *(note: CA1 stratum pyramidale and stratum oriens are adjacent layers; this is weak counter-evidence, consistent with border-zone soma placement.)*
- Annotation transfer is PARTIAL: 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] dominates the Yao 2021 mapping at cluster level, consistent with the parent supertype result. Only 5/66 Pvalb cells map to CLUS_0739.
- PV+ hippocampal interneurons (basket, axo-axonic, bistratified) have high transcriptomic similarity; this cluster likely contains multiple classical PV subtypes.

**What would upgrade confidence**

- **Resolve the Cck discordance**: A targeted cite-traverse for "Cck PV basket cell hippocampus co-expression" would clarify whether primary literature reports Cck co-expression in PV cells, or confirms it is exclusive to CCK basket cells in mouse hippocampus. If Cck positivity is confirmed to exclude PV basket identity, this edge should be downgraded to LOW or UNCERTAIN. Would add `LiteratureEvidence`.
- **Annotation transfer with a morphologically identified PV basket cell dataset** (same as parent edge): Target F1 ≥ 0.80 at CLUSTER level for CLUS_0739. If a morphologically clean PV basket dataset maps preferentially to CLUS_0739 rather than to CLUS_0732 (chandelier), confidence would upgrade toward HIGH. Output: `AnnotationTransferEvidence`.
- **Single-cell resolve of Cck/Pvalb co-expression**: A patch-seq experiment on morphology-confirmed PV basket cells would determine whether any cells express both Pvalb and Cck, and would add `LiteratureEvidence` directly relevant to the neuropeptide discordance.

---

## Proposed experiments

### 1. Annotation transfer — morphologically identified PV basket cell dataset

**Already completed (partial):** MapMyCells was run using Yao 2021 GEO:GSE185862 Pvalb subclass (n=66 HIP cells). At SUPERTYPE level, SUPT_0206 received 12/66 cells (F1=0.324, target_purity=0.800); at CLUSTER level, CLUS_0739 received 5/66 cells (F1=0.179, target_purity=1.0). The dominant target in both cases was the chandelier supertype/cluster, reflecting enrichment of axo-axonic cells in the Yao 2021 SSv4 Pvalb mixed population. This partially addresses the annotation transfer need, but the source dataset is insufficiently stratified by morphological subtype to distinguish basket from axo-axonic cells.

**Refined experiment still needed:**

- **What**: MapMyCells (local, WMBv1/CCN20230722) on a single-cell dataset from morphologically identified PV basket cells (Cre-driver targeted with post-hoc morphological verification, or patch-seq with axon reconstruction confirming perisomatic targeting)
- **Target**: F1 ≥ 0.80 at CLUSTER level for CLUS_0739 [CS20230722_CLUS_0739]; secondary target SUPT_0206 [CS20230722_SUPT_0206]
- **Expected output**: `AnnotationTransferEvidence` on both edges
- **Resolves**: Both MODERATE edges — distinguishes PV basket from axo-axonic/chandelier contribution; resolves the dominant-mapping ambiguity from the Yao 2021 mixed Pvalb dataset

### 2. Targeted literature searches

- **What**: Cite-traverse for (a) "Cnr1 PV basket cell hippocampus mouse" — to add a primary citation for Cnr1 negativity on the classical node; (b) "Cck PV basket cell hippocampus co-expression" — to resolve the Cck discordance on CLUS_0739; (c) "Pvalb Gad1 basket cell hippocampus" — to add Gad1/Gad2 citations to the classical node
- **Expected output**: `LiteratureEvidence` items on classical node marker entries and on edge CLUS_0739 for the Cck property
- **Resolves**: Cnr1 negative marker citation gap; Cck DISCORDANT flag on edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739; Gad1/Gad2 citation gap

---

## Open questions

1. Does any child cluster of SUPT_0206 show hippocampus-specific enrichment and absence of Cck expression, making it a cleaner match for PV basket cell identity than CLUS_0739?
2. Does Cck expression in CLUS_0739 reflect genuine Cck/Pvalb co-expression in a subset of PV neurons, mixed cluster content, or noise? This is the primary unresolved question for the cluster-level edge.
3. Can a morphologically identified PV basket cell dataset (clearly distinct from axo-axonic/chandelier cells) be identified for a higher-resolution annotation transfer?
4. Does the Yao 2021 SSv4 Pvalb subclass label contain PV basket cells as a majority population, or are axo-axonic/chandelier cells dominant in that dataset? The annotation transfer result (chandelier dominant) suggests the latter.

---

## Evidence base table

| Edge ID | Evidence type | Supports | Notes |
|---|---|---|---|
| edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA (Pvalb subclass, GABA NT, location) | PARTIAL | Supertype spans hippocampus + piriform area; not hippocampus-specific |
| edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA (precomputed stats: Pvalb=8.74, Gad1=10.34, Gad2=9.28, Cnr1=1.93) | SUPPORT | All defining markers confirmed; Cnr1 absent |
| edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206 | ANNOTATION_TRANSFER (MapMyCells, GEO:GSE185862, n=66) | PARTIAL | F1=0.324 at SUPT level; chandelier dominant (F1=0.612) |
| edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739 | ATLAS_METADATA (Pvalb MERFISH, hippocampal subfields, Cck discordance) | PARTIAL | CA1 SP 26 cells; Cck score 7.6 discordant |
| edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739 | ATLAS_METADATA (precomputed stats: Pvalb=10.63, Gad1=10.52, Gad2=8.43, Cnr1=1.68) | SUPPORT | Highest Pvalb in SUPT_0206 children; Cnr1 absent |
| edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739 | ANNOTATION_TRANSFER (MapMyCells, GEO:GSE185862, n=66) | PARTIAL | F1=0.179 at CLUS level; chandelier dominant (F1=0.622) |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 | [25018703](https://pubmed.ncbi.nlm.nih.gov/25018703/) | Soma location; Pvalb marker |
| [2] | Sik et al. 1995 | [7472426](https://pubmed.ncbi.nlm.nih.gov/7472426/) | Soma location; morphology |
| [3] | Müller & Remy 2014 | [25324774](https://pubmed.ncbi.nlm.nih.gov/25324774/) | Soma location |
| [4] | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | Soma location |
| [5] | Whissell et al. 2015 | [26441554](https://pubmed.ncbi.nlm.nih.gov/26441554/) | Neurotransmitter type; CCK/PV perisomatic distinction |
| [6] | Que et al. 2021 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060/) | Pvalb marker |
| [7] | Perrenoud et al. 2022 | [35802727](https://pubmed.ncbi.nlm.nih.gov/35802727/) | Pvalb marker |
| [8] | Contreras et al. 2019 | [31297048](https://pubmed.ncbi.nlm.nih.gov/31297048/) | Pvalb marker; CCK/PV systematic comparison |
