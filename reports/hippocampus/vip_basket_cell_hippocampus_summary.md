# VIP-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | stratum pyramidale [UBERON:0005401] | — |
| NT | GABAergic | — |
| Markers | Vip+ | — |

**Node notes:** Stub from cite-traverse (2026-04-10). Described by Tyan et al. (2014, PMID:24671999). Unlike interneuron-selective (IS) cells — which target other interneurons — VIP basket cells provide perisomatic inhibition to CA1 pyramidal neurons with asynchronous GABA release and are not connected with O/A interneurons. Evidence derives from a single primary characterisation. No primary citations are indexed in this facts file for the Vip marker or soma location.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | — | 0179 Vip Gaba_7 [CS20230722_SUPT_0179] | — | ⚪ UNCERTAIN | Vip CONSISTENT · location APPROXIMATE · basket vs IS ambiguous | Eliminated |

1 edge total · relationship type: UNCERTAIN. No MODERATE or LOW edges were resolved.

---

## Eliminated candidates

### 0179 Vip Gaba_7 [CS20230722_SUPT_0179] — ⚪ UNCERTAIN

The primary disqualifying signal is the inability to discriminate VIP basket cells from IS interneurons using available atlas metadata: both types share VIP expression and the same supertype candidate, and the functional distinction (perisomatic vs. interneuron-selective targeting) is not resolvable from transcriptomic data alone.

**Supporting evidence**

- NT type: GABAergic (Vip Gaba subclass in atlas): CONSISTENT.
- Vip is a DEFINING marker of SUPT_0179 [CS20230722_SUPT_0179] (precomputed stats mean 6.82), matching the sole defining marker of the classical type: CONSISTENT.
- Atlas metadata records 11 cells in the CA1 pyramidal layer and 24 cells in CA1 stratum oriens for SUPT_0179 [CS20230722_SUPT_0179], providing partial anatomical overlap with the stratum pyramidale [UBERON:0005401] soma location of the classical type (alignment: APPROXIMATE).
- Annotation transfer (MapMyCells; Yao 2021 SSv4 Vip subclass, GEO:GSE185862, n=476 HIP cells): 046 Vip Gaba subclass receives 463/476 cells (F1=0.969, purity=0.953), confirming robust hippocampal representation in the Vip Gaba clade. At supertype level, SUPT_0179 [CS20230722_SUPT_0179] is the second-strongest target (F1=0.379, 96 cells, purity=0.970), alongside 0177 Vip Gaba_5 (F1=0.397, 101 cells).

**Marker evidence provenance**

- **Vip:** Single primary study (Tyan et al. 2014, PMID:24671999); IHC in fixed CA1 tissue. No primary citations are formally indexed in this facts file. No quantitative single-cell expression profiling specific to morphologically identified VIP basket cells has been curated. Precomputed expression for SUPT_0179 (Vip mean=6.82) confirms robust Vip expression at supertype level but does not discriminate perisomatic-targeting basket cells from interneuron-selective VIP cells.
- **Annotation transfer source:** Yao 2021 SSv4 encompass the full transcriptomic Vip subclass from hippocampus — basket cells, IS cells, and other VIP subtypes — with no morphological or projection-target annotation. Basket-specific signals cannot be extracted without additional labels.

**Concerns**

- **AMBIGUOUS_MAPPING.** SUPT_0179 [CS20230722_SUPT_0179] is also the candidate supertype for IS interneurons (VIP+/calretinin+ interneuron-selective cells). VIP basket cells and IS cells are functionally distinct but share Vip expression. Without discriminating markers (e.g., Cnr1 for basket identity; Calb2 for IS identity), this mapping cannot be resolved from atlas metadata.
- **SINGLE_STUDY.** The VIP basket cell phenotype rests entirely on Tyan et al. (2014, PMID:24671999); independent morphological and transcriptomic replication has not been curated.
- **LOW_CELL_COUNT.** CA1 pyramidal layer representation in SUPT_0179 [CS20230722_SUPT_0179] is very low (11 cells). The supertype is primarily CA3-enriched (CA3 pyramidal layer 23, CA3 stratum oriens 25, CA3 stratum radiatum 17, CA3 stratum lucidum 11), making location alignment APPROXIMATE rather than CONSISTENT.
- **Annotation transfer F1 scores at supertype level are low** (<0.40) and spread across multiple supertypes, reflecting biological heterogeneity of the Vip population.

**What would upgrade confidence**

- A Patch-seq or morphologically verified single-cell dataset from CA1 VIP+ interneurons, annotated as basket vs. IS, mapped onto WMBv1 would resolve the basket-vs-IS ambiguity and potentially elevate one WMBv1 supertype to MODERATE or higher.
- Discriminating marker genes (Cnr1 for basket; Calb2 for IS) in the property comparison against WMBv1 supertype expression profiles would constrain the mapping.
- Subcluster-level inspection of WMBv1 clusters within the Vip Gaba clade may reveal one cluster with a CA1-pyramidal-layer-dominant distribution consistent with basket morphology.

---

## Proposed experiments

### Multiplexed FISH / smFISH
- **What:** Co-detect Vip, Cnr1, and Calb2 in CA1 sections to count perisomatic VIP+/Cnr1+/Calb2− cells (basket candidates) versus VIP+/Calb2+/Cnr1− cells (IS candidates) and characterise their laminar distribution
- **Target:** Proportion estimate for each population; laminar enrichment comparison
- **Expected output:** LiteratureEvidence supporting or refuting basket identity for SUPT_0179 [CS20230722_SUPT_0179]; informs whether a different Vip Gaba cluster has a CA1 SP-dominant distribution
- **Resolves:** Open question 1

### Patch-seq (morphology-targeted)
- **What:** Record and fill CA1 VIP+ interneurons to confirm perisomatic axon collateral patterns; map to WMBv1
- **Target:** Determine which WMBv1 supertype(s) encompass morphologically verified VIP basket cells
- **Expected output:** AnnotationTransferEvidence on this edge; or identification of a more specific Vip Gaba cluster
- **Resolves:** Open questions 1, 3, 4

---

## Open questions

1. Can Cnr1 and Calb2 expression across WMBv1 clusters within the 046 Vip Gaba subclass discriminate basket from IS cell identity at the supertype or cluster level?
2. Is the low CA1 pyramidal layer cell count in SUPT_0179 [CS20230722_SUPT_0179] (11 cells) genuine biological sparsity or a sampling artefact of the WMBv1 dissection protocol?
3. Does any WMBv1 supertype or cluster within the 046 Vip Gaba subclass show a CA1-pyramidal-layer-dominant distribution consistent with perisomatic basket morphology?
4. What is the transcriptomic relationship between VIP basket cells and VIP IS interneurons — are they separable clusters at any WMBv1 taxonomy level, or a functionally defined subpopulation within a molecularly heterogeneous supertype?

---

## Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_vip_basket_cell_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA — Vip Gaba_7 supertype marker and anatomy comparison | PARTIAL |
| edge_vip_basket_cell_hippocampus_to_CS20230722_SUPT_0179 | ANNOTATION_TRANSFER — MapMyCells · GEO:GSE185862 · Vip subclass n=476 HIP cells | PARTIAL |

---

## References

No literature references are formally indexed in this facts file (reference_index is empty). The primary characterisation study (Tyan et al. 2014, PMID:24671999) is cited in the node notes but has not yet been ingested into the reference store for this mapping graph.
