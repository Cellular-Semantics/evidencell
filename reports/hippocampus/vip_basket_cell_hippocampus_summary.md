# VIP-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | stratum pyramidale [UBERON:0005401] | — |
| Neurotransmitter | GABAergic | — |
| Defining markers | Vip | — |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | — | — |

**Node notes:** Stub from cite-traverse (2026-04-10). Described by Tyan et al. (2014, PMID:24671999). Unlike interneuron-selective (IS) cells — which target other interneurons — VIP basket cells provide perisomatic inhibition to CA1 pyramidal neurons and release GABA asynchronously. Evidence derives from a single primary characterisation. VIP basket cells are not connected with O/A interneurons, distinguishing them from IS subtypes that share VIP expression.

---

## Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells (atlas) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | 0179 Vip Gaba_7 [CS20230722_SUPT_0179] | 0179 Vip Gaba_7 | — | ⚪ UNCERTAIN | Vip CONSISTENT; location APPROXIMATE; basket vs. IS ambiguous | Eliminated |

**Total edges: 1.** Relationship type: UNCERTAIN. No MODERATE or LOW edges were resolved.

---

## Eliminated candidates

### 0179 Vip Gaba_7 [CS20230722_SUPT_0179] · ⚪ UNCERTAIN

**Supporting evidence**

- NT type is GABAergic in both the classical node and in the atlas (046 Vip Gaba subclass): CONSISTENT.
- *Vip* is a defining marker in SUPT_0179 (precomputed stats mean: 6.82), matching the classical type's sole defining marker: CONSISTENT.
- Atlas metadata records 11 cells in the CA1 pyramidal layer and 24 cells in CA1 stratum oriens for SUPT_0179, providing partial anatomical overlap with the stratum pyramidale soma location of the classical type.
- Annotation transfer (MapMyCells; Yao 2021 SSv4 Vip subclass, GEO:GSE185862, n=476 HIP cells) maps strongly to the 046 Vip Gaba subclass (F1=0.969, 463/476 cells, target_purity=0.953), confirming robust hippocampal representation in the Vip Gaba subclass. At supertype level, SUPT_0179 is the second-strongest target (F1=0.379, 96 cells, target_purity=0.970), alongside 0177 Vip Gaba_5 (F1=0.397, 101 cells).

**Marker evidence provenance**

- Primary *Vip* marker evidence: single study (Tyan et al. 2014, PMID:24671999); method is immunohistochemistry in fixed CA1 tissue. No quantitative single-cell expression profiling specific to morphologically identified VIP basket cells has been curated.
- Precomputed expression for SUPT_0179 (Vip mean=6.82) is derived from WMBv1 atlas bulk-supertype statistics and confirms robust *Vip* expression. It does not discriminate perisomatic-targeting basket cells from interneuron-selective VIP cells within the supertype.
- The annotation-transfer source (Yao 2021 SSv4) encompasses the full transcriptomic Vip subclass from hippocampus — including basket cells, IS cells, and other VIP interneuron subtypes — and carries no morphological or projection-target annotation; basket-specific signals cannot be extracted from this dataset without additional labels.

**Concerns**

- AMBIGUOUS MAPPING: SUPT_0179 (Vip Gaba_7) is also the candidate supertype for hippocampal interneuron-selective (IS) interneurons — VIP+/calretinin+ cells that gate other interneurons rather than pyramidal cells. VIP basket cells and IS cells are functionally distinct but share *Vip* expression. Without discriminating markers (e.g., *Cnr1* for basket identity; *Calb2* for IS identity), this mapping cannot be resolved from atlas metadata.
- SINGLE STUDY: The VIP basket cell phenotype rests entirely on Tyan et al. (2014, PMID:24671999); independent morphological and transcriptomic replication has not been curated.
- LOW CELL COUNT: CA1 pyramidal layer representation in SUPT_0179 is very low (11 cells). The supertype is primarily CA3-enriched (CA3 pyramidal layer 23, CA3 stratum oriens 25, CA3 stratum radiatum 17, CA3 stratum lucidum 11), making location alignment APPROXIMATE rather than CONSISTENT for a CA1-characterised cell type.
- CA1 stratum oriens cells (24 cells) in SUPT_0179 likely represent a different VIP interneuron type — perisomatic basket cell identity requires a pyramidal-layer-dominant soma distribution, which is not the dominant pattern here.
- Annotation-transfer F1 scores at supertype level are low (<0.4) and spread across multiple supertypes, indicating that the Yao 2021 Vip subclass maps heterogeneously with no clean single supertype target; this reflects biological heterogeneity, not a mapping failure per se.

**What would upgrade confidence**

- A Patch-seq or morphologically verified single-cell dataset from CA1 VIP+ interneurons, annotated as basket vs. IS, mapped onto WMBv1 would resolve the basket-vs-IS ambiguity and potentially elevate one WMBv1 supertype to MODERATE or higher confidence.
- Inclusion of discriminating marker genes (*Cnr1* for basket; *Calb2* for IS) in the property comparison against WMBv1 supertype expression profiles would constrain the mapping.
- Independent studies characterising VIP+ perisomatic interneurons in CA1 would strengthen the classical node definition and provide additional marker anchors to distinguish this type.
- Subcluster-level inspection of WMBv1 clusters within the Vip Gaba subclass may reveal one cluster with a CA1-pyramidal-layer-dominant distribution consistent with basket morphology.

---

## Proposed experiments

No proposed experiments are formally recorded on this edge. The following approaches follow directly from the identified ambiguities:

**Multiplexed fluorescence in situ hybridisation (FISH) / smFISH**
- Co-detect *Vip*, *Cnr1*, and *Calb2* in CA1 sections to count perisomatic VIP+/Cnr1+/Calb2- cells (basket candidates) versus VIP+/Calb2+/Cnr1- cells (IS candidates), and to characterise their laminar distribution.

**Morphology-targeted single-cell transcriptomics (Patch-seq)**
- Record and fill CA1 VIP+ interneurons to confirm perisomatic axon collateral patterns, then sequence and map to WMBv1 to determine which supertype(s) encompass morphologically verified basket cells.

**Re-analysis of existing Patch-seq datasets**
- Query publicly available hippocampal Patch-seq data for VIP+ cells with perisomatic morphology; map onto WMBv1 to test whether SUPT_0179 or 0177 Vip Gaba_5 better captures VIP basket identity.

---

## Open questions

1. Can *Cnr1* and *Calb2* expression across WMBv1 clusters within the 046 Vip Gaba subclass discriminate basket from IS cell identity at the supertype or cluster level?
2. Is the low CA1 pyramidal layer cell count in SUPT_0179 (11 cells) genuine biological sparsity or a sampling artefact of the WMBv1 dissection protocol?
3. Does any WMBv1 supertype or cluster within the 046 Vip Gaba subclass show a CA1-pyramidal-layer-dominant distribution consistent with perisomatic basket morphology?
4. What is the transcriptomic relationship between VIP basket cells described by Tyan et al. (2014) and VIP IS interneurons — are they separable clusters at any WMBv1 taxonomy level, or a functionally defined subpopulation within a molecularly heterogeneous supertype?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_vip_basket_cell_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA, ANNOTATION_TRANSFER | PARTIAL |

---

## References

No literature references are formally indexed in this facts file. The node notes cite PMID:24671999 (Tyan et al. 2014) as the primary characterisation study; this reference has not yet been ingested into the reference store for this mapping graph.

| # | Citation | PMID | Used for |
|---|---|---|---|
| — | Tyan et al. (2014) — VIP-positive basket cells provide perisomatic inhibition to CA1 pyramidal neurons with asynchronous GABA release. *(not yet ingested into reference store)* | [24671999](https://pubmed.ncbi.nlm.nih.gov/24671999/) | Primary characterisation; classical node definition; perisomatic inhibition phenotype |
