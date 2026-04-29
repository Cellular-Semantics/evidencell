# entorhinal cortex layer III PCP4-positive pyramidal cell — WMBv1 (CCN20230722) Mapping Report

*draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type definition

| Property | Value | References |
|---|---|---|
| Soma location | Entorhinal cortex [UBERON:0001905] (*entorhinal cortex layer III*) | — |
| Neurotransmitter | Glutamatergic | [1] |
| Defining markers | *Pcp4* | [2][1] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | pyramidal neuron [CL:0000598] (BROAD) | — |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells mapped | Confidence | Key alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_SUPT_0036 | 0036 L2/3 IT ENT Glut_4 | 522 (GSE185862) | 🟡 MODERATE | NT consistent; layer III location consistent; *Pcp4* not assessed in atlas markers | Best candidate |

**Total edges: 1 · Relationship type: PARTIAL_OVERLAP.** *(note: a secondary edge to SUPT_0037 (L2/3 IT ENT Glut_5) is proposed — this supertype captures the remaining ~10% of L3 IT ENT cells not mapping to SUPT_0036)*

---

## 0036 L2/3 IT ENT Glut_4 [CS20230722_SUPT_0036] · 🟡 MODERATE

### Supporting evidence

**Annotation transfer — GSE185862 (Yao 2021 SSv4).** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 hippocampal cells onto WMBv1 (CCN20230722). Yao 2021 'L3 IT ENT' subclass cells (n=588), representing entorhinal cortex layer III IT projection neurons (including PCP4+ pyramidal cells projecting to CA1 and the subiculum via the temporoammonic pathway), map to SUPT_0036 [CS20230722_SUPT_0036] (L2/3 IT ENT Glut_4) with group_purity=0.888 and F1=0.937, and target_purity=0.992. This is a strong, high-purity mapping. A further 10.2% of L3 IT ENT cells map to SUPT_0037 (L2/3 IT ENT Glut_5), giving combined coverage of 99.0% of L3 IT ENT cells across the two supertypes.

The WMBv1 'L2/3 IT ENT' subclass nomenclature groups layer 2-3 EC IT neurons, and is consistent with the Yao 2021 'L3 IT ENT' labelling. SUPT_0036 is the dominant correspondence for the layer III EC PCP4+ population.

### Marker evidence provenance

- ***Pcp4*** — defining marker for EC layer III pyramidal cells [2][1]. Principal neurons in EC layer III express Purkinje cell protein 4 (PCP4) and project to CA1 and the subiculum [1]. However, *Pcp4* is **not listed** in the SUPT_0036 [CS20230722_SUPT_0036] defining atlas markers (listed as *Fermt1*, *Cxcl14*). The marker comparison is flagged NOT_ASSESSED: expression of *Pcp4* in SUPT_0036 has not been directly interrogated from the atlas precomputed statistics.
- ***Pcp4* shared with CA2 pyramidal cells:** *Pcp4* is also a marker of CA2 pyramidal cells in the mouse hippocampus [2], where immunostaining delineates the CA3/CA2 and CA2/CA1 borders. The annotation transfer evidence clearly separates EC layer III (SUPT_0036) from CA2-FC-IG supertypes in the atlas, so cross-contamination is not expected. Nevertheless, running `add-expression` for *Pcp4* across L2/3 IT ENT supertypes (SUBC_008) would confirm which atlas supertype carries the highest *Pcp4* expression and resolve the NOT_ASSESSED status.
- **SUPT_0036 atlas markers** (*Fermt1*, *Cxcl14*) are not classical EC layer III markers. These defining markers have not been validated against primary literature for this node — **recommend cite-traverse on *Fermt1* / *Cxcl14* and EC layer III to identify peer-reviewed primary sources**.

### Concerns

- **Ambiguous mapping — secondary supertype SUPT_0037:** SUPT_0036 and SUPT_0037 together capture 99.0% of Yao 2021 L3 IT ENT cells. The classical EC layer III PCP4+ pyramidal cell population may split across these two supertypes. SUPT_0036 is the dominant target (F1=0.937); a secondary edge to SUPT_0037 (L2/3 IT ENT Glut_5) would complete the mapping but is not yet recorded.
- ***Pcp4* absent from SUPT_0036 defining markers:** The canonical EC layer III marker *Pcp4* does not appear in the SUPT_0036 [CS20230722_SUPT_0036] metadata marker list. This is not a refutation — *Pcp4* may be expressed at detectable levels without reaching the threshold for inclusion as a defining marker — but the NOT_ASSESSED status should be resolved with an atlas expression query.
- **No soma location references:** No location references are recorded in the classical node reference_index. The soma location assignment (EC layer III) relies on the Yao 2021 'L3 IT ENT' label rather than an independent anatomical source.

### What would upgrade confidence

- Add a secondary edge to SUPT_0037 (L2/3 IT ENT Glut_5) to complete the mapping of EC layer III PCP4+ pyramidal cells across both dominant supertypes.
- Query WMBv1 precomputed expression statistics for *Pcp4* across SUBC_008 (L2/3 IT ENT) supertypes using `just add-expression` to identify which supertype carries the *Pcp4*-high signature and resolve the NOT_ASSESSED comparison.
- Add primary literature references for the EC layer III soma location to the classical node.

---

## Eliminated candidates

No edges have been eliminated as UNCERTAIN. The remaining <1% of Yao 2021 L3 IT ENT cells not captured by SUPT_0036+SUPT_0037 are distributed across minor off-target mappings; these are not biologically informative.

---

## Proposed experiments

### Secondary edge — SUPT_0037

| Attribute | Detail |
|---|---|
| **What** | Add mapping edge to SUPT_0037 (L2/3 IT ENT Glut_5) as secondary EC layer III correspondence |
| **Target** | Document that SUPT_0036+SUPT_0037 together capture ≥ 99% of L3 IT ENT cells from Yao 2021 |
| **Expected output** | Low-confidence PARTIAL_OVERLAP edge to SUPT_0037 [CS20230722_SUPT_0037] |
| **Resolves** | Incomplete mapping: ~10% of L3 IT ENT cells are not accounted for by the current single edge |

### Atlas expression query — Pcp4

| Attribute | Detail |
|---|---|
| **What** | Query WMBv1 precomputed expression statistics for *Pcp4* across all L2/3 IT ENT supertypes within SUBC_008 using `just add-expression` or direct HDF5 query |
| **Target** | Mean expression and fraction expressing *Pcp4* per supertype; identify whether SUPT_0036 or SUPT_0037 carries the higher *Pcp4* signal |
| **Expected output** | MarkerSource entry for *Pcp4* on the appropriate SUPT node; resolution of NOT_ASSESSED comparison |
| **Resolves** | *Pcp4* NOT_ASSESSED comparison on SUPT_0036 [CS20230722_SUPT_0036]; establishes which L2/3 IT ENT supertype best matches the *Pcp4*-defined classical EC layer III PCP4+ pyramidal cell |

---

## Open questions

1. Does PCP4 expression in WMBv1 distinguish SUPT_0036 (EC layer III) from SUPT_0100/0101 (CA2-FC-IG) supertypes? This would confirm the *Pcp4* marker is not confounded across atlas types.

---

## Evidence base

| Edge ID | Evidence type | Details | Supports |
|---|---|---|---|
| edge_ec_layer3_pyramidal_cell_hippocampus_to_supt_0036 | ANNOTATION_TRANSFER | GSE185862 (Yao 2021 SSv4); 522/588 L3 IT ENT cells → SUPT_0036 [CS20230722_SUPT_0036]; group_purity=0.888, target_purity=0.992, F1=0.937 | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2021 | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991/) | Neurotransmitter type; *Pcp4* marker |
| [2] | Unknown 2014 | [24166578](https://pubmed.ncbi.nlm.nih.gov/24166578/) | *Pcp4* marker |
