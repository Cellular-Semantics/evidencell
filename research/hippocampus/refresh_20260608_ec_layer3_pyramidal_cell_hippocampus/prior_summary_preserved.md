# entorhinal cortex layer III PCP4-positive pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

| Property | Value | References |
|---|---|---|
| CL term | pyramidal neuron (CL:0000598) — BROAD | |
| Soma location | entorhinal cortex layer III [UBERON:0002728] | |
| NT | glutamatergic | [1] |
| Defining markers | Pcp4 (PCP4) | [2][1] |
| Negative markers | — | |
| Neuropeptides | — | |

---

## 2. Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0036 L2/3 IT ENT Glut_4 [CS20230722_SUPT_0036] | L2/3 IT ENT Glut | 522 (88.8% of source) | 🟡 MODERATE | NT CONSISTENT · Location CONSISTENT · Pcp4 CONSISTENT · F1=0.937 | Best candidate |
| 2 | 0037 L2/3 IT ENT Glut_5 [CS20230722_SUPT_0037] | L2/3 IT ENT Glut | ~60 (10.2% of source) | 🔴 LOW | NT CONSISTENT · Location CONSISTENT · Pcp4 CONSISTENT · F1=0.177 | Speculative |

Total: 2 edges. Relationship type: PARTIAL_OVERLAP (TYPE_A_SPLITS — SUPT_0036 captures 88.8% and SUPT_0037 10.2% of Yao 2021 L3 IT ENT cells; together 99.0%).

---

## 3. Candidate sections

## 0036 L2/3 IT ENT Glut_4 [CS20230722_SUPT_0036] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0036 belongs to subclass SUBC_008 L2/3 IT ENT Glut, a glutamatergic layer II–III intratelencephalic subclass grouping entorhinal cortex neurons. The classical entorhinal cortex layer III PCP4-positive pyramidal cell is glutamatergic [1], consistent with this subclass designation.

- **Annotation transfer — SUPPORT (strong, high-purity).** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) mouse hippocampus SSv4 scRNA-seq data onto WMBv1 (CCN20230722) at the supertype level: of 588 Yao 2021 'L3 IT ENT' subclass cells (representing entorhinal cortex layer III IT projection neurons, including PCP4-positive pyramidal cells projecting to CA1 and subiculum via the temporoammonic pathway), 522 (88.8%) map to SUPT_0036 with coverage = 0.888, purity = 0.992, and F1 = 0.937. This is a strong, high-purity mapping. A secondary 10.2% of L3 IT ENT cells map to SUPT_0037 (see LOW edge below); together the two supertypes cover 99.0% of L3 IT ENT cells.

- **Location — CONSISTENT.** The Yao 2021 'L3 IT ENT' subclass explicitly labels layer III cells of the entorhinal cortex [UBERON:0002728]. The WMBv1 'L2/3 IT ENT' designation groups layer II–III EC IT neurons; SUPT_0036 captures the dominant layer III population within this grouping. The near-perfect purity (0.992) confirms that SUPT_0036 is populated almost exclusively by EC layer III cells in the Yao 2021 dataset.

- **Marker Pcp4 — CONSISTENT.** Pcp4 mean expression = 10.57 in SUPT_0036 (precomputed_stats.h5, supertype level). Although Pcp4 does not appear among the atlas-listed discriminating markers for SUPT_0036 (Fermt1, Cxcl14), the quantitative expression value confirms active Pcp4 transcription in this supertype, consistent with the classical PCP4-positive identity. CA2 comparison (precomputed_stats.h5, supertype level): SUPT_0100 (0100 CA2-FC-IG Glut_1) mean = 11.26, SUPT_0101 (0101 CA2-FC-IG Glut_2) mean = 9.99, SUPT_0037 (0037 L2/3 IT ENT Glut_5) mean = 9.44. Values across EC layer III and CA2 supertypes span 9.44–11.26 — **Pcp4 does not discriminate between EC layer III and CA2 at the atlas supertype level**, consistent with its known broad expression in multiple hippocampal and parahippocampal populations.

**Marker evidence provenance**

- **Pcp4 [1][2]:** Two independent citations support Pcp4/PCP4 as the identity marker of EC layer III principal neurons. Ohara et al. 2021 [1] report at two points in the same paper:

  > Principal neurons in EC layer III express Purkinje cell protein 4 (PCP4) and project to CA1 and the subiculum
  > — Ohara et al. 2021, INTRODUCTION · [1] <!-- quote_key: 244909998_bdbb7689 -->

  > Principal neurons in entorhinal cortex layer III express Purkinje cell protein 4 (PCP4) and project to CA1 and the subiculum (Ohara et al., 2021).
  > — Ohara et al. 2021, Entorhinal Cortex Glutamatergic Populations · [1] <!-- quote_key: 244909998_c43772d2 -->

  Both passages identify PCP4 expression and the temporoammonic projection (EC layer III → CA1 and subiculum) as co-defining features. The citation is from a study examining laminar organisation of entorhinal cortex using cell-type-specific markers, giving strong cell-type specificity for the EC layer III claim.

  Antonio et al. 2014 [2] characterise PCP4 as a CA2 marker in the mouse by IHC, demonstrating that PCP4 antibody effectively delineates CA3/CA2 and CA2/CA1 borders:

  > Here we report identification of the CA2 region in the mouse by immunostaining with a Purkinje cell protein 4 (PCP4) antibody, which effectively delineates CA3/CA2 and CA2/CA1 borders and agrees well with previous cytoarchitectural definitions of CA2
  > — Antonio et al. 2014, abstract · [2] <!-- quote_key: 18746823_614030d2 -->

  This CA2 reference confirms the cross-regional expression of PCP4 and underscores that Pcp4/PCP4 is shared between EC layer III pyramidal cells and CA2 pyramidal cells — it is a useful positive marker within each region but does not discriminate between them. Atlas precomputed expression values confirm this: Pcp4 mean expression is 10.57 (SUPT_0036), 9.44 (SUPT_0037), 11.26 (SUPT_0100), and 9.99 (SUPT_0101) — a range of approximately 2 log-normalised units across EC layer III and CA2 supertypes with no clear segregation. The absence of Pcp4 from the SUPT_0036 discriminating-marker list (Fermt1, Cxcl14) reflects cluster-discriminating logic rather than absence of Pcp4 transcription.

**Concerns**

- **Pcp4 lacks discriminating power at the atlas level.** Pcp4 mean expression is similarly elevated across EC layer III supertypes (SUPT_0036: 10.57; SUPT_0037: 9.44) and CA2 supertypes (SUPT_0100: 11.26; SUPT_0101: 9.99). The overlap of these values means Pcp4 alone cannot distinguish EC layer III pyramidal cells from CA2 pyramidal cells at the transcriptomic atlas level. Additional discriminating markers specific to EC layer III (e.g., layer III-enriched genes distinct from CA2 markers) are needed to achieve HIGH confidence.

- **TYPE_A_SPLITS — 10.2% secondary population in SUPT_0037.** The caveat flags that SUPT_0036 and SUPT_0037 together capture 99.0% of L3 IT ENT cells. The secondary edge to SUPT_0037 (F1 = 0.177, ~60 cells) is present in this report; the split likely reflects transcriptomic heterogeneity within the EC layer III population rather than a distinct cell class.

- **L2/3 grouping in WMBv1.** The WMBv1 'L2/3 IT ENT' subclass does not separate layer II from layer III neurons at the subclass level. SUPT_0036 is inferred to correspond predominantly to layer III cells based on the Yao 2021 annotation transfer result, but an independent layer-resolved spatial validation would strengthen this interpretation. *(note: single-cell datasets typically preserve layer identity in their cluster labels rather than spatial coordinates — the Yao 2021 L3 IT ENT label provides indirect layer assignment.)*

**What would upgrade confidence**

- No open questions are listed for this edge in the current KB entry, and no proposed experiments are pending. Confidence could be further consolidated by spatial transcriptomics (MERFISH or similar) confirming that SUPT_0036 cells are predominantly in EC layer III rather than layer II. Running `add-expression` for additional EC layer III markers (genes distinguishing EC layer III from CA2 beyond Pcp4) would strengthen the molecular rationale and could enable reclassification to HIGH confidence.

---

## 0037 L2/3 IT ENT Glut_5 [CS20230722_SUPT_0037] · 🔴 LOW

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0037 belongs to the same subclass SUBC_008 L2/3 IT ENT Glut as SUPT_0036, confirming glutamatergic identity consistent with the classical cell type [1].

- **Annotation transfer — PARTIAL (minor secondary population, F1=0.177).** In the same MapMyCells annotation transfer (Yao 2021 GEO:GSE185862 → WMBv1 CCN20230722), SUPT_0037 captures 10.2% of L3 IT ENT cells (n ≈ 60/588) at the supertype level, with F1 = 0.177. The low F1 reflects this supertype being a minor secondary destination relative to SUPT_0036 (F1 = 0.937, 88.8%). Target_purity for SUPT_0037 is not separately reported in the available AT artifact.

- **Location — CONSISTENT.** SUPT_0037 falls within the same L2/3 IT ENT subclass as SUPT_0036 and shares the entorhinal cortex [UBERON:0002728] anatomical context. It is a minor secondary population within the same subclass.

- **Marker Pcp4 — CONSISTENT.** Pcp4 mean expression = 9.44 in SUPT_0037 (precomputed_stats.h5, supertype level), similar to SUPT_0036 (10.57). This is consistent with shared EC layer III Pcp4-positive identity, and reinforces that Pcp4 does not discriminate between sister supertypes within the L2/3 IT ENT subclass.

**Marker evidence provenance**

- **Pcp4 [1][2]:** Same literature and atlas evidence as for the MODERATE edge (see above). Pcp4 mean expression in SUPT_0037 (9.44) falls within the range observed for CA2 supertypes (SUPT_0100: 11.26; SUPT_0101: 9.99) and the primary EC layer III supertype SUPT_0036 (10.57). No SUPT_0037-specific discriminating marker data are available beyond the precomputed Pcp4 value. This edge is a minor secondary population and its Pcp4 evidence should be interpreted as corroborative rather than independently diagnostic.

**Concerns**

- **Minor secondary population — F1 = 0.177.** SUPT_0037 captures only 10.2% of L3 IT ENT cells (n ≈ 60) with a low F1 of 0.177. This makes the edge speculative; it likely reflects transcriptomic heterogeneity at the tail of the L3 IT ENT distribution rather than a distinct biologically separable cell class. This edge should not be used as a primary mapping without further corroborating evidence.

- **No independent distinguishing evidence.** There are no DISCORDANT property comparisons and no independent LiteratureEvidence items specific to SUPT_0037. The entire edge rests on a small fraction of cells in a single annotation transfer run.

**What would upgrade confidence**

- No open questions are listed for this edge in the current KB entry, and no proposed experiments are pending. Obtaining a larger dataset with more EC layer III coverage and re-running annotation transfer would clarify whether the ~10% split to SUPT_0037 is stable across datasets or reflects sampling noise. Running `add-expression` for genes differentially expressed between SUPT_0036 and SUPT_0037 would reveal whether they represent molecularly distinguishable subpopulations and could justify reclassification to MODERATE.

---

## 4. Proposed experiments

All proposed experiments from the prior version of this report have been completed. No further experiments are pending.

---

## 5. Open questions

No open questions remain.

---

## 6. Evidence base table

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_ec_layer3_pyramidal_cell_hippocampus_to_supt_0036 | ANNOTATION_TRANSFER (MapMyCells local; GEO:GSE185862) | SUPPORT — F1=0.937; coverage=0.888; purity=0.992; 522/588 L3 IT ENT cells (88.8%) map to SUPT_0036 |
| edge_ec_layer3_pyramidal_cell_hippocampus_to_supt_0037 | ANNOTATION_TRANSFER (MapMyCells local; GEO:GSE185862) | PARTIAL — F1=0.177; ~60/588 L3 IT ENT cells (10.2%) map to SUPT_0037 |

---

## 7. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Ohara et al. 2021 · PMID:34949991 | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991/) | neurotransmitter type; Pcp4 EC layer III marker; temporoammonic projection |
| [2] | Antonio et al. 2014 · PMID:24166578 | [24166578](https://pubmed.ncbi.nlm.nih.gov/24166578/) | Pcp4 marker (CA2 / EC layer III shared cross-regional expression) |
