# VIP-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

## Introduction

VIP-positive basket cells are GABAergic interneurons of the CA1 stratum pyramidale that provide perisomatic inhibition to pyramidal neurons via asynchronous GABA release, distinguishing them functionally from VIP interneuron-selective (IS) interneurons, which target other interneurons rather than principal cells. First characterised electrophysiologically and morphologically in a single study (Tyan et al. 2014, PMID:24671999), the VIP basket cell shares VIP expression with IS cells but differs in its pyramidal-cell target and its lack of connectivity with oriens/alveus interneurons — a distinction that is not yet resolvable at the transcriptomic level with available atlas metadata.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | — |
| NT | GABAergic | — |
| Markers | Vip (defining) | — |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | — (no mapping) | — |

<details><summary>Details — source evidence for classical type properties</summary>

- **Soma location and functional identity:** VIP basket cell soma in stratum pyramidale and perisomatic targeting documented by Tyan et al. 2014 (PMID:24671999). This study is cited in the node notes but is not formally indexed in the facts reference store for this mapping graph; no verbatim quotes with quote keys are available.
- **Vip marker:** single study IHC; VIP positivity is the sole molecular marker entry. No discriminating co-markers (e.g., Cnr1, Calb2) are recorded in the classical node.
- **Functional distinction from IS interneurons:** the node notes document that VIP basket cells "provided perisomatic inhibition to CA1 pyramidal neurons with asynchronous GABA release and were not connected with O/A interneurons" (from cite-traverse entry citing PMID:24671999). No formal quote key is available for this assertion.

</details>

Cell Ontology mapping: no CL term is mapped for this node. A CL new term request is warranted if the VIP basket cell can be transcriptomically anchored.

---

## Results

One candidate atlas supertype was assessed and eliminated as UNCERTAIN. No MODERATE or LOW edges were resolved. The inability to discriminate VIP basket cells from IS interneurons using available atlas metadata — both types sharing Vip expression and the same supertype candidate — is the primary blocker.

![Annotation transfer F1 heatmap — Yao 2021 SSv4 Vip subclass → WMBv1](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_vip_basket_cell_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 (GEO:GSE185862) SSv4 Vip source group (n=476 HIP cells) mapped to WMBv1. Vip cells map cleanly to the Vip Gaba subclass at subclass level (F1=0.969), but diverge across multiple supertypes at supertype level; SUPT_0179 (Vip Gaba_7) receives the second-largest share (F1=0.379, 96 cells) alongside SUPT_0177 (Vip Gaba_5, F1=0.397, 101 cells). VIP basket vs. IS identity cannot be resolved from this morphologically unresolved source.*

### Candidate overview table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key alignment | Verdict |
|---|---|---|---:|---|---|---|
| — | — | 0179 Vip Gaba_7 [CS20230722_SUPT_0179] | 215 | ⚪ UNCERTAIN | Vip CONSISTENT · CA1 pyr layer APPROXIMATE (11 cells) · basket vs. IS unresolvable | Eliminated |

1 edge total · relationship type: UNCERTAIN.

## Eliminated candidates

### 0179 Vip Gaba_7 [CS20230722_SUPT_0179] — ⚪ UNCERTAIN

The primary disqualifying signal is the inability to discriminate VIP basket cells from IS interneurons using available atlas metadata: both types share Vip expression and are captured by the same supertype candidate. The functional distinction (perisomatic pyramidal-cell targeting vs. interneuron-selective targeting) is not resolvable from transcriptomic data alone.

**Supporting evidence**

- GABAergic NT type is CONSISTENT: Vip Gaba_7 belongs to the Vip Gaba subclass.
- Vip is a DEFINING marker of SUPT_0179 (precomputed mean 6.82), matching the sole defining marker of the classical type.
- Atlas metadata includes 11 cells in the CA1 pyramidal layer, providing partial anatomical overlap with the stratum pyramidale soma location of the classical type (alignment: APPROXIMATE).
- Annotation transfer: MapMyCells local, Yao 2021 (GEO:GSE185862) SSv4 Vip subclass (n=476 HIP cells). At subclass level, 046 Vip Gaba receives 463/476 cells (F1=0.969, target_purity=0.953). At supertype level, SUPT_0179 is the second-strongest target (F1=0.379, 96 cells, target_purity=0.970), alongside SUPT_0177 Vip Gaba_5 (F1=0.397, 101 cells). The Vip population is distributed across many supertypes; SUPT_0179 being a prominent target is consistent with the VIP basket correspondence but does not discriminate basket from IS cells.

**Concerns**

- AMBIGUOUS_MAPPING: SUPT_0179 (Vip Gaba_7) is simultaneously the candidate supertype for IS interneurons. VIP basket cells (perisomatic pyramidal-cell targeting) and IS cells (targeting other interneurons) share Vip expression. Without discriminating markers (Cnr1 for basket; Calb2 for IS), this mapping cannot be resolved.
- SINGLE_STUDY: the VIP basket cell phenotype rests entirely on Tyan et al. 2014 (PMID:24671999); no independent morphological or transcriptomic replication is curated.
- LOW_CELL_COUNT: CA1 pyramidal layer representation in SUPT_0179 is very low (11 cells); the supertype is primarily CA3-enriched (CA3 pyr 23, CA3 SO 25, CA3 SR 17, CA3 lucidum 11), making location alignment APPROXIMATE rather than CONSISTENT.
- Annotation transfer F1 scores at supertype level are low (below 0.40) and spread across multiple supertypes, reflecting biological heterogeneity of the Vip population rather than specific VIP basket identity.

**What would upgrade confidence**

- A patch-seq or morphologically verified single-cell dataset from CA1 VIP+ interneurons annotated as basket vs. IS cells mapped onto WMBv1 would resolve the ambiguity and potentially elevate one supertype or cluster to MODERATE or higher.
- Discriminating marker genes (Cnr1 for basket; Calb2 for IS) tested against WMBv1 Vip Gaba supertype expression profiles would constrain the mapping without requiring a new experiment.
- Subcluster-level inspection of WMBv1 clusters within the Vip Gaba clade may reveal one cluster with a CA1-pyramidal-layer-dominant distribution consistent with basket morphology.

## Methods

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The VIP-positive basket cell is defined on a CLASSICAL_MULTIMODAL basis: soma in the pyramidal layer of CA1 [UBERON:0014548]; GABAergic neurotransmitter type; defining marker Vip. Primary characterisation from Tyan et al. 2014 (PMID:24671999), cited in node notes but not formally indexed in the reference store for this mapping graph.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at rank 1 (supertype) using metadata-based scoring (region match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Numerical values from precomputed expression on the supertype in the taxonomy reference store.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4) |
| Source cluster label | Vip (n=476 HIP cells; morphologically unresolved) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells total | 6398; Vip subclass n=476 |
| Run record | `kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/` |
| Code reference | https://github.com/AllenInstitute/cell_type_mapper |
| F1 matrix | `f1_scores_best.csv` |
| Caveats | Yao 2021 SSv4 Vip label encompasses VIP basket, IS cells, and other VIP interneuron subtypes; basket-specific resolution is not achievable from this morphologically unresolved source without additional discriminating labels. |

**Atlas data sources.** WMBv1 (CCN20230722); precomputed expression from supertype YAML in the taxonomy reference store.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. The pre-write hook rejects any unresolvable identifier or unattributed blockquote.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:25+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_vip_basket_cell_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** VIP-positive basket cell → 0179 Vip Gaba_7 [CS20230722_SUPT_0179] at UNCERTAIN confidence; candidate is ELIMINATED. Key support: Vip expression is CONSISTENT (precomputed mean 6.82); SUPT_0179 carries 11 CA1 pyramidal layer cells, providing partial anatomical overlap; annotation transfer of the Yao 2021 Vip subclass (n=476) places SUPT_0179 as a prominent supertype hit (F1=0.379, 96 cells, target_purity=0.970). Key caveats: SUPT_0179 is simultaneously the candidate supertype for IS interneurons; no discriminating markers between basket and IS cells are recorded in the classical node; the supertype is primarily CA3-enriched (only 11 CA1 pyr layer cells); the evidence base rests on a single study (PMID:24671999) that is not formally indexed in the reference store for this report; the VIP basket cell does not yet have a confirmed transcriptomic identity that can be placed in the WMBv1 taxonomy.

### Proposed experiments

**Multiplexed FISH — Vip + Cnr1 + Calb2.**

- Co-detect Vip, Cnr1 (candidate basket marker), and Calb2 (candidate IS marker) in CA1 sections to count perisomatic VIP+/Cnr1+/Calb2- cells (basket candidates) versus VIP+/Calb2+ cells (IS candidates) and characterise their laminar distribution.
- Cross-check: no discriminating molecular markers are present in the classical node; this experiment would directly establish whether basket and IS cells are separable by additional markers and inform which WMBv1 cluster inherits each population.

**Patch-seq from morphologically identified VIP+ interneurons.**

- Record and fill CA1 VIP+ interneurons to confirm perisomatic axon collateral patterns onto pyramidal cells (basket) versus interneuron-targeting patterns (IS); extract cytoplasm for scRNA-seq and apply MapMyCells to WMBv1.
- Cross-check: current AT uses the bulk Yao 2021 Vip label (morphologically unresolved); basket-specific resolution requires a morphologically confirmed labelled reference. This is the primary bottleneck for confidence upgrade.

**Subcluster-level inspection of WMBv1 Vip Gaba clade.**

- Examine WMBv1 clusters within the 046 Vip Gaba subclass for CA1-pyramidal-layer-dominant cell distributions; a cluster with dominant CA1 pyr representation may be the more specific basket-cell correspondent even if not captured in the supertype-level mapping.

### Open questions

1. Can Cnr1 and Calb2 expression across WMBv1 clusters within the 046 Vip Gaba subclass discriminate basket from IS cell identity at the supertype or cluster level?
2. Does any WMBv1 supertype or cluster within the 046 Vip Gaba subclass show a CA1-pyramidal-layer-dominant distribution consistent with perisomatic basket morphology?
3. Is the low CA1 pyramidal layer cell count in SUPT_0179 (11 cells) genuine biological sparsity or a sampling artefact of the WMBv1 dissection protocol?
4. What is the transcriptomic relationship between VIP basket cells and VIP IS interneurons — are they separable clusters at any WMBv1 taxonomy level, or a functionally defined subpopulation within a molecularly heterogeneous supertype?

---

## References

No literature references are formally indexed in this facts file (reference_index is empty). The primary characterisation study (Tyan et al. 2014, PMID:24671999) is cited in the node notes but has not been ingested into the reference store for this mapping graph.
