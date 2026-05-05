# entorhinal cortex layer II calbindin-positive pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

| Property | Value | References |
|---|---|---|
| CL term | pyramidal neuron (CL:0000598) | |
| Soma location | entorhinal cortex layer II [UBERON:0002728] | [1][2][3] |
| NT | glutamatergic | [4] |
| Defining markers | Calb1 (calbindin) | [4][5] |
| Negative markers | — | |
| Neuropeptides | — | |

---

## 2. Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0052 L2 IT ENT-po Glut_2 [CS20230722_SUPT_0052] | L2 IT ENT-po Glut | — | 🟡 MODERATE | Calb1 CONSISTENT · F1=0.694 | Best candidate |

Total: 1 edge. Relationship type: PARTIAL_OVERLAP (the classical EC layer II calbindin-positive pyramidal cell maps primarily to SUPT_0052, with a secondary split to SUPT_0054; the 'ENT-po' subclass also spans postrhinal cortex).

---

## 3. Candidate paragraphs

## 0052 L2 IT ENT-po Glut_2 [CS20230722_SUPT_0052] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0052 belongs to subclass SUBC_011 L2 IT ENT-po Glut, a glutamatergic layer II intratelencephalic subclass grouping medial entorhinal cortex and postrhinal cortex neurons. The classical EC layer II calbindin-positive pyramidal cell is glutamatergic [4], consistent with this subclass.

- **Annotation transfer — SUPPORT.** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) mouse hippocampus SSv4 scRNA-seq data onto WMBv1 (CCN20230722): of 42 Yao 2021 'L2 IT ENTm' subclass cells (representing medial entorhinal cortex layer II IT neurons, principally calbindin-positive pyramidal cells), 25 (59.5%) map to SUPT_0052 at the supertype level. F1 = 0.694, group_purity = 0.595, target_purity = 0.833. SUPT_0054 (L2 IT ENT-po Glut_4) accounts for a further 33.3% of L2 IT ENTm cells. Together SUPT_0052 and SUPT_0054 cover 92.8% of L2 IT ENTm cells. Note: n=42 is a small sample; results should be interpreted with appropriate caution.

- **Marker Calb1 — CONSISTENT.** Calb1 is listed as the defining identity marker of EC layer II calbindin-positive pyramidal cells [4][5]. Precomputed expression stats (precomputed_stats.h5, supertype level) confirm Calb1 mean expression = 7.14 in SUPT_0052. Although Calb1 does not appear among the defining discriminating markers for SUPT_0052 in the atlas (Ush2a, Dcn), the quantitative expression value is consistent with calbindin expression in this population.

- **Location — APPROXIMATE.** The 'ENT-po' (entorhinal postrhinal) subclass designation reflects a shared transcriptomic signature between medial entorhinal cortex and postrhinal cortex. Classical EC layer II calbindin-positive pyramidal cells are restricted to medial entorhinal cortex [UBERON:0002728] [1][2][3]; postrhinal cortex is a distinct but adjacent area. *(note: medial entorhinal cortex and postrhinal cortex are anatomically adjacent posterior cortical regions — the ENT-po grouping likely reflects transcriptomic similarity rather than equal spatial representation, consistent with an adjacent-region boundary effect rather than a strong counter-evidence signal.)*

**Marker evidence provenance**

- **Calb1** [4][5]: Two independent citations support Calb1 as the pyramidal cell identity marker in EC layer II. Naumann et al. 2015 [4] report immunofluorescence evidence in rodents confirming that ~88% of calbindin-positive cells are glutamatergic in entorhinal cortex, and confirm the existence of periodically arranged calbindin-positive pyramidal cell patches across species; cell-type identity was established by electrophysiological properties and projection tracing (CA1-projecting), providing strong specificity for the pyramidal cell identity as distinct from stellate cells. The second citation [5] provides transcript-level evidence. No discrepancy exists between the literature markers and the atlas precomputed value (Calb1 mean = 7.14 in SUPT_0052). The absence of Calb1 from the atlas defining-marker list reflects cluster-discriminating rather than exhaustive expression reporting. *(Recommendation: Running add-expression for Calb1 and Reln across SUBC_011 supertypes would directly confirm the pyramidal/stellate distinction within the ENT-po subclass and resolve Open question 1.)*

**Concerns**

- **Small sample size (n=42).** The L2 IT ENTm subclass in Yao 2021 (GEO:GSE185862) contains only 42 cells, limiting the statistical reliability of the F1 = 0.694 estimate. The moderate F1 and lower group_purity (0.595) are consistent with either biological heterogeneity within medial EC layer II or sampling noise from the small n. Additional medial EC layer II cells from a larger HPF dataset would improve confidence.

- **Location APPROXIMATE — postrhinal cortex component.** The 'ENT-po' subclass spans medial EC and postrhinal cortex; classical EC layer II pyramidal cells are restricted to medial EC. Any postrhinal component in SUPT_0052 would represent a different population sharing a transcriptomic signature. *(note: medial EC and postrhinal cortex are adjacent — this is weak rather than strong counter-evidence.)*

- **TYPE_A_SPLITS — secondary edge to SUPT_0054 not yet added.** SUPT_0054 captures an additional 33.3% of L2 IT ENTm cells; a second edge (F1=0.500) would complete the mapping when more data are available.

**What would upgrade confidence**

- **Larger medial EC layer II dataset:** Obtaining a dataset with more L2 IT ENTm cells (n > 100 target) and re-running annotation transfer would substantially improve F1 confidence and distinguish whether the 40% of L2 IT ENTm cells mapping to SUPT_0054 represent a distinct subpopulation (LiteratureEvidence or AnnotationTransferEvidence). This addresses the core statistical limitation.

- **Calb1 and Reln expression atlas check:** Running add-expression for Calb1 and Reln across SUBC_011 (ENT-po) and SUBC_009 (PIR-ENTl) supertypes would directly confirm that SUPT_0052 is Calb1-high/Reln-low (pyramidal) while SUPT_0042 is Reln-high/Calb1-low (stellate), resolving Open question 1 without new experiments.

---

## 4. Proposed experiments

### 1 — Atlas expression query (add-expression)

**What:** Run add-expression for Calb1 and Reln on CCN20230722 precomputed stats across all SUBC_011 (L2 IT ENT-po Glut) and SUBC_009 (L2/3 IT PIR-ENTl Glut) supertypes.

**Target:** Confirm Calb1 mean expression significantly higher in SUPT_0052 than in SUPT_0042; Reln mean expression significantly higher in SUPT_0042 than in SUPT_0052.

**Expected output:** PrecomputedExpression entries on atlas nodes confirming the molecular distinction between pyramidal and stellate EC layer II supertypes.

**Resolves:** Open question 1 (Calb1 as atlas-level distinguisher of pyramidal vs. stellate supertypes).

### 2 — Larger dataset annotation transfer

**What:** Obtain a larger HPF scRNA-seq or snRNA-seq dataset with sufficient medial EC layer II coverage (target n > 100 L2 IT ENTm-equivalent cells) and re-run MapMyCells annotation transfer onto WMBv1 (CCN20230722).

**Target:** F1 ≥ 0.80 at SUPERTYPE level for SUPT_0052.

**Expected output:** AnnotationTransferEvidence entry upgrading confidence from MODERATE to HIGH if threshold is met; also enables secondary edge to SUPT_0054.

**Resolves:** Open question 2 (whether F1=0.694 reflects biological heterogeneity or sampling noise); incomplete TYPE_A_SPLITS mapping to SUPT_0054.

---

## 5. Open questions

1. Does Calb1 expression distinguish SUPT_0052 (pyramidal, Calb1+) from SUPT_0042 (stellate, Reln+) at the atlas level? Running add-expression for Calb1 and Reln across SUBC_011 (ENT-po) and SUBC_009 (PIR-ENTl) supertypes would resolve this without new experiments.

2. Is the moderate F1 = 0.694 a reflection of genuine biological heterogeneity within medial EC layer II pyramidal cells (consistent with a TYPE_A_SPLITS to SUPT_0052 and SUPT_0054), or does it primarily reflect statistical noise from the small sample (n=42)?

---

## 6. Evidence base table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_ec_layer2_pyramidal_cell_hippocampus_to_supt_0052 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862) | SUPPORT — F1=0.694; group_purity=0.595; target_purity=0.833; 59.5% of L2 IT ENTm cells map to SUPT_0052; n=42 (small sample) |

---

## 7. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2019 · PMID:31680885 | [31680885](https://pubmed.ncbi.nlm.nih.gov/31680885/) | Soma location |
| [2] | Unknown 2018 · PMID:30209250 | [30209250](https://pubmed.ncbi.nlm.nih.gov/30209250/) | Soma location |
| [3] | Unknown 2021 · PMID:34949991 | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991/) | Soma location |
| [4] | Naumann et al. 2015 · PMID:26223342 | [26223342](https://pubmed.ncbi.nlm.nih.gov/26223342/) | NT type; Calb1 marker |
| [5] | Unknown 2010 · PMID:20512133 | [20512133](https://pubmed.ncbi.nlm.nih.gov/20512133/) | Calb1 marker |
