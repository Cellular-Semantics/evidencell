# Interneuron-specific (IS) interneuron — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | VIP GABAergic interneuron (CL:4023016) | |
| Soma location | stratum oriens [UBERON:0005383] (CA1); stratum radiatum [UBERON:0005402] (CA1); stratum lacunosum moleculare [UBERON:0005403] (CA1) | [1] |
| NT | GABAergic | |
| Markers | Calb2 (calretinin), Vip | [2] [1] [3] [2] [4] |
| Neuropeptides | Vip | [2] |

**Node notes:** Three classical subtypes are recognised: IS-1 (CR+/VIP−), IS-2 (VIP+), IS-3 (CR+/VIP+). The CL mapping to VIP GABAergic interneuron (CL:4023016) covers only VIP+ subtypes (IS-2 and IS-3); IS-1 falls outside this mapping.

---

## Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0179 Vip Gaba_7 [CS20230722_SUPT_0179] | — | — | 🟡 MODERATE | Vip CONSISTENT · Calb2 CONSISTENT | Best candidate |

1 edge total · relationship type: `PARTIAL_OVERLAP`

---

## 0179 Vip Gaba_7 · 🟡 MODERATE

### Supporting evidence

- **VIP-family identity confirmed at SUBCLASS level (annotation transfer).** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 Vip subclass (n = 476 HIP cells) onto WMBv1 mapped 463/476 cells to subclass 046 Vip Gaba (F1 = 0.969, group_purity = 0.985, target_purity = 0.953), confirming that the Vip SSv4 population sits squarely within the WMBv1 Vip Gaba clade. At SUPERTYPE level, 0179 Vip Gaba_7 [CS20230722_SUPT_0179] received 96/476 cells (F1 = 0.379, target_purity = 0.970), ranking second to 0177 Vip Gaba_5 (101 cells, F1 = 0.397). Vip cells distribute broadly across 10+ Vip supertypes, consistent with the heterogeneity of the classical IS population. PARTIAL: the SSv4 'Vip' label cannot discriminate IS cells from VIP basket or other VIP interneuron subtypes; IS-specific resolution requires a dataset with morphologically identified VIP-IN labels.

- **Multi-laminar CA1 anatomy is consistent.** Atlas metadata records 0179 Vip Gaba_7 [CS20230722_SUPT_0179] cells across CA1 stratum oriens (MBA:399, 24 cells), CA1 stratum radiatum (MBA:415, 26 cells), CA3 stratum oriens (25 cells), and CA3 stratum radiatum (17 cells), as well as CA1 stratum pyramidale (11 cells) and CA3 stratum pyramidale (23 cells). The CA1 SO and SR distributions match the classical IS soma locations at stratum oriens [UBERON:0005383] and stratum radiatum [UBERON:0005402] cited by Tyan et al. 2014 [1]. Property comparisons: location_stratum_oriens = CONSISTENT; location_stratum_radiatum = CONSISTENT.

- **Both defining markers confirmed by precomputed stats.** Precomputed statistics for 0179 Vip Gaba_7 [CS20230722_SUPT_0179] show Vip mean = 6.82 (DEFINING marker) and Calb2 mean = 6.78. NT type: GABAergic (CONSISTENT with GABA in atlas). Vip neuropeptide confirmed (precomputed stats mean = 6.82). Property comparisons: marker_Vip = CONSISTENT; marker_Calb2 = CONSISTENT; neuropeptide_Vip = CONSISTENT; nt_type = CONSISTENT.

### Marker evidence provenance

**Calb2 (calretinin):**

- **Method type:** IHC (protein-level). Evidence derives primarily from Tyan et al. 2014 [1] (ultrastructural characterisation in CA1) and Chamberland & Topolnik 2012 [3] (review of IS cell neurochemistry), with Tzilivaki et al. 2023 [2] providing confirmatory transcriptomic context.
- **Cell-type specificity:** Tyan et al. 2014 [1] used direct ultrastructural evidence in CA1 to confirm IS cell identity — cells were included based on selective interneuron targeting confirmed by electron microscopy. This provides a morphologically grounded basis for the calretinin attribution.
- **Data source discrepancy:** Calb2 is **not listed as a defining marker of 0179 Vip Gaba_7** in atlas metadata, yet precomputed stats return a mean of 6.78 for this supertype. Both values are recorded; the discrepancy warrants investigation. The precomputed value is consistent with IS cell expression, but absence from defining marker lists means the atlas does not treat Calb2 as a discriminating feature at supertype resolution. This may reflect that Calb2 is expressed at variable levels across multiple Vip supertypes rather than being specific to 0179 Vip Gaba_7 [CS20230722_SUPT_0179].

**Vip:**

- **Method type:** IHC and transgenic reporter (protein/reporter-level). Evidence from Tzilivaki et al. 2023 [2] and Bocchio et al. 2024 [4].
- **Cell-type specificity:** Bocchio et al. 2024 [4] used a Vip-IRES-Cre driver line in CA1, providing direct targeting of VIP-expressing cells in the appropriate anatomical context. This is a standard approach and provides adequate specificity for VIP-family assignment.
- **Quantitative cross-check:** Vip is a DEFINING marker of 0179 Vip Gaba_7 [CS20230722_SUPT_0179] with precomputed stats mean = 6.82. No discrepancy between literature and atlas metadata.

### Concerns

- **IS-1 subtype is outside this mapping.** IS-1 cells are VIP−/CR+ and would not map to a Vip supertype. This edge represents only IS-2 (VIP+) and IS-3 (VIP+/CR+). A Calb2-expressing but Vip-negative supertype may be a better candidate for IS-1; no such candidate has been proposed in this graph.

- **VIP basket cells co-occur in this supertype.** VIP GABAergic interneurons in hippocampus include VIP basket cells (vip_basket_cell_hippocampus) in addition to IS cells. The 0179 Vip Gaba_7 [CS20230722_SUPT_0179] supertype may encompass both perisomatic VIP basket cells and disinhibitory IS cells. The interneuron-specific targeting feature of IS cells — that they innervate exclusively other GABAergic cells — is not resolvable from transcriptomic metadata alone.

- **Stratum lacunosum-moleculare location: NOT_ASSESSED.** The classical IS node includes stratum lacunosum moleculare [UBERON:0005403] (CA1) as a soma location, but SLM is not recorded among the top-count anatomical locations for 0179 Vip Gaba_7 [CS20230722_SUPT_0179]. This is a metadata resolution gap, not a contradiction.

- **Additional atlas defining markers without classical correspondence.** The atlas defines this supertype partly by Qrfpr, Stk32a, and Igfbp4 — none of these genes appear in the classical IS literature surveyed. Their significance for IS cell identity is unknown.

- **Annotation transfer is not IS-cell-specific.** The Yao 2021 SSv4 source dataset labels cells as 'Vip subclass' without discriminating IS cells from VIP basket or other VIP interneuron types. The F1 = 0.969 at SUBCLASS level confirms VIP family membership but does not provide IS-specific evidence.

### What would upgrade confidence

- **IS-cell-specific annotation transfer.** A dataset with morphologically identified IS cells (IS-1, IS-2, IS-3 individually) mapped via MapMyCells onto WMBv1, targeting F1 ≥ 0.80 at SUPERTYPE level, would add `AnnotationTransferEvidence` that could discriminate IS cells from VIP basket cells within the Vip Gaba clade.

- **Resolve the IS-1 / CR-only gap.** Identify a Calb2+/Vip− supertype candidate from WMBv1 and initiate a parallel mapping edge for IS-1. A targeted `find-candidates` query filtering on Calb2 expression and hippocampal anatomy would generate candidates.

- **Targeted literature search for Calb2 as IS marker.** The Calb2 evidence linking it specifically to IS cells (rather than CR+ interneurons broadly) would benefit from a cite-traverse for "calretinin interneuron-specific hippocampus" to confirm cell-type specificity of the original IHC studies cited in [1] and [3].

- **Patch-seq / MERSCOPE data linking IS morphology to transcriptome.** A PATCH_SEQ dataset in which IS cells are identified morphologically (post-hoc reconstruction confirming interneuron-only axonal targets) and then transcriptomically profiled would provide a direct bridge from classical morpho-functional identity to a WMBv1 cluster assignment.

---

## Eliminated candidates

No UNCERTAIN edges in this graph. The only candidate evaluated is 0179 Vip Gaba_7 [CS20230722_SUPT_0179] at MODERATE confidence.

---

## Proposed experiments

No formal experiments are recorded in this edge's `proposed_experiments` field. Based on the analysis above, the following are recommended:

### 1. IS-cell-specific annotation transfer
- **What:** MapMyCells annotation transfer using a source dataset with morphologically or physiologically confirmed IS cell labels
- **Target:** F1 ≥ 0.80 at SUPERTYPE level against WMBv1
- **Expected output:** `AnnotationTransferEvidence` entries on this edge and any IS-1 candidate edge
- **Resolves:** Whether 0179 Vip Gaba_7 [CS20230722_SUPT_0179] (vs. 0177 Vip Gaba_5 or other Vip supertypes) is the primary IS-2/3 recipient; whether an IS-1 candidate exists in WMBv1

### 2. IS-1 candidate identification
- **What:** `just find-candidates` query on WMBv1 filtered for Calb2 expression + hippocampal anatomy + GABAergic NT, excluding Vip-defining supertypes
- **Target:** Identify ≥1 candidate supertype with Calb2 as defining or high-expression marker and no Vip
- **Expected output:** A new LOW or MODERATE edge for IS-1 (CR+/VIP−) in this graph
- **Resolves:** Open question 2 (which WMBv1 supertypes contain IS-1 cells)

### 3. Targeted cite-traverse for Calb2 / IS marker specificity
- **What:** cite-traverse or survey search for "calretinin interneuron-specific hippocampus" and "IS-1 interneuron calretinin CA1"
- **Target:** Primary study confirming Calb2/calretinin as a marker specifically on morphology-confirmed IS cells
- **Expected output:** `LiteratureEvidence` entries strengthening the Calb2 marker attribution; or revised marker confidence if specificity is lower than assumed
- **Resolves:** Open question 1 (weak marker evidence provenance for Calb2)

---

## Open questions

1. Can WMBv1 supertypes discriminate IS cells from VIP basket cells based on transcriptomic signature alone? The disinhibitory connectivity motif of IS cells may not have a distinctive transcriptomic correlate at supertype resolution.

2. Which WMBv1 supertype(s) contain IS-1 (CR+/VIP−) cells? A Calb2+/Vip− supertype with hippocampal anatomy has not yet been identified in this mapping.

3. Does the Calb2 atlas-detected expression (precomputed mean = 6.78) at 0179 Vip Gaba_7 [CS20230722_SUPT_0179] reflect IS-1/3 cells specifically, or is it broadly expressed across the Vip Gaba clade? Absent from atlas defining marker lists, its discriminating value is unclear.

4. What are the functional roles of Qrfpr, Stk32a, and Igfbp4 — the atlas-defining markers of 0179 Vip Gaba_7 [CS20230722_SUPT_0179] — in IS cell identity or circuit function? These are not documented in the classical IS literature.

5. Does stratum lacunosum-moleculare represent a genuine IS soma location, or does it reflect transient or sparse SLM presence? The SLM location is not among top anatomical counts in 0179 Vip Gaba_7 [CS20230722_SUPT_0179] and has not been assessed.

---

## Evidence base

| Edge ID | Evidence type | Method / Source | Supports |
|---|---|---|---|
| edge_is_interneuron_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA | Vip Gaba_7 supertype marker + anatomy review | PARTIAL |
| edge_is_interneuron_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA | Precomputed stats cross-check (Calb2, Vip) | SUPPORT |
| edge_is_interneuron_hippocampus_to_CS20230722_SUPT_0179 | ANNOTATION_TRANSFER | MapMyCells · Yao 2021 SSv4 Vip HIP cells (GEO:GSE185862) | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Tyan et al. 2014 · PMID:24671999 | [24671999](https://pubmed.ncbi.nlm.nih.gov/24671999/) | soma location |
| [2] | Tzilivaki et al. 2023 · PMID:37467748 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Calb2 marker |
| [3] | Chamberland & Topolnik 2012 · PMID:23162426 | [23162426](https://pubmed.ncbi.nlm.nih.gov/23162426/) | Calb2 marker |
| [4] | Bocchio et al. 2024 · PMID:39401246 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | Vip marker |
