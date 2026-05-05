# entorhinal cortex layer III PCP4-positive pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

| Property | Value | References |
|---|---|---|
| CL term | pyramidal neuron (CL:0000598) | |
| Soma location | entorhinal cortex layer III [UBERON:0001905] | |
| NT | glutamatergic | [1] |
| Defining markers | Pcp4 (PCP4/Purkinje cell protein 4) | [2][1] |
| Negative markers | — | |
| Neuropeptides | — | |

*Note: no soma location references are recorded in the facts file; the layer III location is supported by the NT and marker citations.*

---

## 2. Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0036 L2/3 IT ENT Glut_4 [CS20230722_SUPT_0036] | L2/3 IT ENT Glut | — | 🟡 MODERATE | Location CONSISTENT · F1=0.937 | Best candidate |

Total: 1 edge. Relationship type: PARTIAL_OVERLAP (SUPT_0036 is the dominant target, with SUPT_0037 accounting for a further 10.2% of L3 IT ENT cells; together 99.0%).

---

## 3. Candidate paragraphs

## 0036 L2/3 IT ENT Glut_4 [CS20230722_SUPT_0036] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0036 belongs to subclass SUBC_008 L2/3 IT ENT Glut, a glutamatergic layer II/III entorhinal cortex intratelencephalic subclass. The classical EC layer III PCP4-positive pyramidal cell is glutamatergic [1], consistent with this subclass.

- **Soma location — CONSISTENT.** The Yao 2021 'L3 IT ENT' subclass explicitly labels layer III cells of the entorhinal cortex. SUPT_0036 is the dominant target for this subclass (88.8% group purity), confirming strong layer correspondence. The WMBv1 'L2/3 IT ENT' designation groups layers II and III EC IT neurons, but the Yao 2021 L3 IT ENT annotation is layer-specific and maps predominantly to SUPT_0036, supporting the layer III assignment for this supertype. The near-perfect target purity (0.992) confirms that SUPT_0036 is essentially exclusively populated by EC layer III cells in the Yao 2021 dataset.

- **Annotation transfer — SUPPORT.** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) mouse hippocampus SSv4 scRNA-seq data onto WMBv1 (CCN20230722): of 588 Yao 2021 'L3 IT ENT' subclass cells, 522 (88.8%) map to SUPT_0036 at the supertype level. F1 = 0.937, group_purity = 0.888, target_purity = 0.992. This is a strong, high-purity mapping. SUPT_0037 (L2/3 IT ENT Glut_5) accounts for a further 10.2% of L3 IT ENT cells. Together SUPT_0036 and SUPT_0037 cover 99.0% of L3 IT ENT cells, consistent with a TYPE_A_SPLITS relationship between these two supertypes.

- **Marker Pcp4 — CONSISTENT.** Pcp4 is listed as the defining identity marker of EC layer III pyramidal cells, distinguishing them from layer II populations [2][1]. Precomputed expression stats (precomputed_stats.h5, supertype level) confirm Pcp4 mean expression = 10.57 in SUPT_0036 — among the highest Pcp4 values across HPF supertypes. Although Pcp4 does not appear among the WMBv1 defining discriminating markers for SUPT_0036 (Fermt1, Cxcl14), the high quantitative expression value is consistent with EC layer III pyramidal cell identity.

**Marker evidence provenance**

- **Pcp4** [2][1]: Pcp4 (PCP4, Purkinje cell protein 4) is described as an immunohistochemical marker identifying EC layer III pyramidal cells in mice, with a key study reporting that EC layer III neurons express PCP4 and project to CA1 and the subiculum via the temporoammonic pathway [1]. A second study reports Pcp4 immunostaining for CA2 region delineation in mouse [2], confirming that Pcp4 is broadly expressed in specific hippocampal populations. An important cross-marker consideration: Pcp4 marks both EC layer III pyramidal cells and CA2 pyramidal cells — these are distinct populations separated by anatomy (entorhinal cortex vs. CA2 field). In the atlas, CA2-relevant supertypes (SUPT_0100, SUPT_0101) also express Pcp4; Open question 1 addresses whether Pcp4 expression can distinguish EC layer III (SUPT_0036) from CA2 (SUPT_0100/0101) at the supertype level. The primary cellular identity evidence is based on anatomical location and projection pattern (not on Pcp4 alone), which is appropriate for a well-defined anatomical type. *(Recommendation: Running add-expression for Pcp4 across SUBC_008 L2/3 IT ENT Glut supertypes and comparing with SUBC_019 CA2-FC-IG supertypes would clarify whether Pcp4 mean expression level can discriminate EC layer III vs. CA2 supertypes.)*

**Concerns**

- **PARTIAL_OVERLAP — secondary edge to SUPT_0037 not yet added.** SUPT_0037 (L2/3 IT ENT Glut_5) captures 10.2% of L3 IT ENT cells. The classical EC layer III pyramidal cell population may TYPE_A_SPLITS across SUPT_0036 and SUPT_0037. A secondary edge to SUPT_0037 would complete the mapping. SUPT_0037 group_purity and F1 scores are lower (F1=0.177 due to lower group purity), suggesting it captures a minor subpopulation.

- **Pcp4 marker cross-reactivity with CA2.** Pcp4 is expressed in both EC layer III pyramidal cells and CA2 pyramidal cells in the mouse. This shared marker does not affect the quality of this mapping (the annotation transfer provides a direct L3 IT ENT cell label), but it means Pcp4 alone cannot serve as a discriminating atlas marker between EC layer III and CA2 populations.

**What would upgrade confidence**

- **Secondary edge to SUPT_0037:** Adding a MappingEdge to SUPT_0037 (L2/3 IT ENT Glut_5) would complete the EC layer III pyramidal cell coverage across the atlas. This requires curation effort but no new experiments.

- **Pcp4 atlas expression comparison:** Running add-expression for Pcp4 in SUBC_008 (L2/3 IT ENT Glut) and SUBC_019 (CA2-FC-IG Glut) supertypes in the atlas would confirm whether Pcp4 expression level can distinguish EC layer III supertypes from CA2 supertypes (Open question 1), and add quantitative marker evidence to the node without new experiments.

---

## 4. Proposed experiments

### 1 — Curation (complete TYPE_A_SPLITS edge to SUPT_0037)

**What:** Add a secondary MappingEdge to SUPT_0037 (L2/3 IT ENT Glut_5) for the EC layer III pyramidal cell.

**Target:** F1=0.177 from existing Yao 2021 transfer (lower group purity); no new experiment required.

**Expected output:** Additional MappingEdge YAML entry completing the TYPE_A_SPLITS coverage of EC layer III pyramidal cells.

**Resolves:** Incomplete TYPE_A_SPLITS representation; provides full coverage of EC layer III IT neuron supertypes.

### 2 — Atlas expression query (add-expression)

**What:** Run add-expression for Pcp4 on CCN20230722 precomputed stats across SUBC_008 (L2/3 IT ENT Glut) supertypes and SUBC_019 (CA2-FC-IG Glut) supertypes.

**Target:** Determine whether Pcp4 mean expression level distinguishes EC layer III supertypes (SUPT_0036, 0037) from CA2 supertypes (SUPT_0100, 0101).

**Expected output:** PrecomputedExpression entries confirming or disconfirming Pcp4 as a discriminating marker at the atlas supertype level.

**Resolves:** Open question 1 (Pcp4 specificity for EC layer III vs. CA2 atlas populations).

---

## 5. Open questions

1. Does Pcp4 expression level in WMBv1 distinguish SUPT_0036 (EC layer III) from SUPT_0100/0101 (CA2-FC-IG) supertypes? Running add-expression for Pcp4 across SUBC_008 and SUBC_019 supertypes would resolve this and confirm whether Pcp4 is a useful discriminating marker at the atlas supertype level.

---

## 6. Evidence base table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_ec_layer3_pyramidal_cell_hippocampus_to_supt_0036 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862) | SUPPORT — F1=0.937; group_purity=0.888; target_purity=0.992; 88.8% of L3 IT ENT cells map to SUPT_0036 |

---

## 7. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2021 · PMID:34949991 | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991/) | NT type; Pcp4 marker |
| [2] | Unknown 2014 · PMID:24166578 | [24166578](https://pubmed.ncbi.nlm.nih.gov/24166578/) | Pcp4 marker |
