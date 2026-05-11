# Interneuron-specific (IS) interneuron — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | VIP GABAergic interneuron (CL:4023016) — BROAD | — |
| Soma location | stratum oriens [UBERON:0005383] (CA1); stratum radiatum [UBERON:0005402] (CA1); stratum lacunosum-moleculare [UBERON:0005403] (CA1) | [1] |
| NT | GABAergic | — |
| Markers | Calb2 (calretinin)+, Vip+ | [1][2][3][4] |
| Neuropeptides | Vip | [2] |

**Node notes:** Three classical subtypes are recognised: IS-1 (CR+/VIP−), IS-2 (VIP+), IS-3 (CR+/VIP+). The CL mapping to VIP GABAergic interneuron (CL:4023016) covers only VIP+ subtypes (IS-2 and IS-3); IS-1 (CR+/VIP−) falls outside this mapping.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | — | 0179 Vip Gaba_7 [CS20230722_SUPT_0179] | — | 🟡 MODERATE | Vip CONSISTENT · Calb2 CONSISTENT | Best candidate |

1 edge total · relationship type: PARTIAL_OVERLAP.

---

## 0179 Vip Gaba_7 [CS20230722_SUPT_0179] · 🟡 MODERATE

### Supporting evidence

- **VIP-family identity confirmed at SUBCLASS level (annotation transfer, GEO:GSE185862).** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 Vip subclass (n=476 HIP cells) onto WMBv1 mapped 463/476 cells to subclass 046 Vip Gaba (F1=0.969, group_purity=0.985, target_purity=0.953), confirming the Vip SSv4 population sits squarely within the WMBv1 Vip Gaba clade. At SUPERTYPE level, 0179 Vip Gaba_7 [CS20230722_SUPT_0179] received 96/476 cells (F1=0.379, target_purity=0.970), ranking second to 0177 Vip Gaba_5 (101 cells, F1=0.397). Vip cells distribute broadly across 10+ Vip supertypes, consistent with IS population heterogeneity. PARTIAL: the SSv4 'Vip' label cannot discriminate IS cells from VIP basket or other VIP interneuron subtypes; IS-specific resolution requires a dataset with morphologically identified VIP-IN labels.
- **Annotation transfer (GEO:GSE99888) — partial corroboration from Harris 2018.** Harris 2018 Class Calb2.Vip.Igfbp4 (Calb2+/Vip+/Igfbp4+ CA1 interneurons, n=98 cells in the 3,663-cell dataset) maps entirely to Vip Gaba subclass (group_purity=1.0, 98/98 cells) and 57.8% to [CS20230722_SUPT_0179] Vip Gaba_7 (F1=0.612, group_purity=0.578, 26 cells). The complete recall at SUBCLASS (100%) confirms Vip family assignment. The modest SUPERTYPE F1 (0.612) and dispersal across Vip supertypes reflects IS subtype heterogeneity — IS-1 is VIP−, while IS-2 and IS-3 are VIP+. The Calb2.Vip.Igfbp4 Harris cluster is not specifically IS-labelled; this evidence provides additional PARTIAL corroboration that Calb2+/Vip+ cells from an unbiased CA1 dataset preferentially map to SUPT_0179.
- **Multi-laminar CA1 anatomy is consistent.** Atlas metadata records SUPT_0179 [CS20230722_SUPT_0179] cells in CA1 stratum oriens (24 cells; CONSISTENT with location_stratum_oriens) and CA1 stratum radiatum (26 cells; CONSISTENT with location_stratum_radiatum). Additional CA3 representation (CA3 SO 25, CA3 SR 17) and CA1/CA3 pyramidal layer cells (11 and 23 respectively) are present. The multi-laminar CA1 distribution matches the classical IS soma locations cited by Tyan et al. 2014 [1].
- **Both defining markers confirmed by precomputed stats.** Precomputed statistics for SUPT_0179 [CS20230722_SUPT_0179] show Vip mean=6.82 (DEFINING marker, CONSISTENT) and Calb2 mean=6.78 (CONSISTENT). NT type: GABAergic (CONSISTENT with GABA atlas). Vip neuropeptide confirmed (precomputed mean=6.82, CONSISTENT).
- Tyan et al. 2014 [1] characterised IS cells using direct ultrastructural evidence in CA1, confirming selective interneuron targeting:

> The so-called interneuron-specific (IS) cells were identified based on direct ultrastructural evidence that some calretinin (CR)- expressing or vasoactive intestinal polypeptide (VIP)-expressing GABAergic cells in the CA1 area of the hippocampus contact interneurons selectively. IS cells were further subdivided into three subtypes with distinct anatomical and neurochemical features.
> — Tyan et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 23480858_1f4801fb -->

- Tzilivaki et al. 2023 [2] further confirm the IS-1/2/3 subtype scheme:

> Freund and colleagues first characterized IS interneurons and showed that these cells express calretinin (CR) (IS-1), VIP (IS-2), or both (IS-3)
> — Tzilivaki et al. 2023, Transcriptomic Interneuron Classifications · [2] <!-- quote_key: 259953057_10f139f9 -->

### Marker evidence provenance

- **Calb2 (calretinin):** Evidence is protein-level (IHC). Tyan et al. 2014 [1] used direct ultrastructural evidence in CA1 — cells were included based on selective interneuron targeting confirmed by electron microscopy, providing morphologically grounded cell-type specificity. Chamberland & Topolnik 2012 [3] provides review-level confirmation. Tzilivaki et al. 2023 [2] provides transcriptomic context. Data source discrepancy: Calb2 is **not listed as a defining marker of SUPT_0179** in atlas metadata, yet precomputed stats return a mean of 6.78. Both values are recorded; the discrepancy warrants investigation. Calb2 may be expressed at variable levels across multiple Vip supertypes rather than being specific to SUPT_0179 [CS20230722_SUPT_0179].
- **Vip:** Evidence is IHC and transgenic reporter-level from Tzilivaki et al. 2023 [2] and Bocchio et al. 2024 [4]. Bocchio et al. 2024 [4] used a Vip-IRES-Cre driver in CA1, providing direct targeting of VIP-expressing cells in the appropriate anatomical context. Vip is a DEFINING marker of SUPT_0179 with precomputed stats mean=6.82. No discrepancy between literature and atlas metadata.

### Concerns

- **IS-1 subtype not captured.** IS-1 cells are VIP−/CR+ and would not map to a Vip supertype. This edge represents only IS-2 (VIP+) and IS-3 (VIP+/CR+). A Calb2-expressing but Vip-negative supertype may be a better candidate for IS-1; none has been identified in this graph.
- **VIP basket cells co-occur in this supertype (MARKER_NOT_SPECIFIC).** VIP interneurons in hippocampus include VIP basket cells (vip_basket_cell_hippocampus) in addition to IS cells. SUPT_0179 [CS20230722_SUPT_0179] may encompass both perisomatic VIP basket cells and disinhibitory IS cells. The interneuron-specific targeting feature of IS cells is not resolvable from transcriptomic metadata alone.
- **Stratum lacunosum-moleculare location: NOT_ASSESSED.** SLM [UBERON:0005403] (CA1) is listed as a classical IS soma location [1] but is not recorded among the top-count anatomical locations for SUPT_0179 [CS20230722_SUPT_0179].
- **Additional atlas defining markers without classical correspondence.** Qrfpr, Stk32a, and Igfbp4 are additional defining markers of SUPT_0179; none appears in the classical IS literature surveyed.
- **Annotation transfer is not IS-cell-specific.** The Yao 2021 SSv4 source dataset labels cells as 'Vip subclass' without discriminating IS cells from VIP basket or other VIP interneuron types. F1=0.969 at SUBCLASS confirms VIP family membership but does not provide IS-specific evidence.

### What would upgrade confidence

- **IS-cell-specific annotation transfer.** A dataset with morphologically identified IS cells (IS-1, IS-2, IS-3 individually) mapped via MapMyCells onto WMBv1; target: F1 ≥ 0.80 at SUPERTYPE level. Expected output: AnnotationTransferEvidence discriminating IS cells from VIP basket cells within the Vip Gaba clade.
- **Resolve the IS-1 / CR-only gap.** Identify a Calb2+/Vip− supertype candidate from WMBv1 and initiate a parallel mapping edge for IS-1. A `just find-candidates` query filtering on Calb2 expression, hippocampal anatomy, and GABAergic NT excluding Vip-defining supertypes would generate candidates.
- **Targeted literature search for Calb2 as IS marker.** Cite-traverse for "calretinin interneuron-specific hippocampus" to confirm cell-type specificity of the original IHC studies [1][3]. Weak marker evidence for Calb2 specificity to IS cells (rather than CR+ interneurons broadly) is a gap addressable without new experiments.

---

## Proposed experiments

### 1. IS-cell-specific annotation transfer
- **What:** MapMyCells annotation transfer using a source dataset with morphologically or physiologically confirmed IS cell labels
- **Target:** F1 ≥ 0.80 at SUPERTYPE level against WMBv1
- **Expected output:** AnnotationTransferEvidence entries on this edge and any IS-1 candidate edge
- **Resolves:** Whether SUPT_0179 [CS20230722_SUPT_0179] (vs. 0177 Vip Gaba_5 or other Vip supertypes) is the primary IS-2/3 recipient; whether an IS-1 candidate exists in WMBv1

### 2. IS-1 candidate identification
- **What:** `just find-candidates` query on WMBv1 filtered for Calb2 expression + hippocampal anatomy + GABAergic NT, excluding Vip-defining supertypes
- **Target:** Identify ≥1 candidate supertype with Calb2 as defining or high-expression marker and no Vip
- **Expected output:** A new LOW or MODERATE edge for IS-1 (CR+/VIP−) in this graph
- **Resolves:** Open question 2

### 3. Targeted cite-traverse for Calb2 / IS marker specificity
- **What:** Cite-traverse for "calretinin interneuron-specific hippocampus" and "IS-1 interneuron calretinin CA1"
- **Target:** Primary study confirming Calb2/calretinin as a marker specifically on morphology-confirmed IS cells
- **Expected output:** LiteratureEvidence entries strengthening the Calb2 marker attribution; or revised marker confidence
- **Resolves:** Open question 1

---

## Open questions

1. Can WMBv1 supertypes discriminate IS cells from VIP basket cells based on transcriptomic signature alone? The disinhibitory connectivity motif of IS cells may not have a distinctive transcriptomic correlate at supertype resolution.
2. Which WMBv1 supertype(s) contain IS-1 (CR+/VIP−) cells? A Calb2+/Vip− supertype with hippocampal anatomy has not yet been identified in this mapping.
3. Does the Calb2 atlas-detected expression (precomputed mean=6.78 at SUPT_0179 [CS20230722_SUPT_0179]) reflect IS-1/3 cells specifically, or is it broadly expressed across the Vip Gaba clade?
4. What are the functional roles of Qrfpr, Stk32a, and Igfbp4 — the additional atlas-defining markers of SUPT_0179 [CS20230722_SUPT_0179] — in IS cell identity?
5. Does stratum lacunosum-moleculare represent a genuine IS soma location, or is it sparse/transient? Not among top anatomical counts in SUPT_0179 [CS20230722_SUPT_0179].

---

## Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_is_interneuron_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA — Vip Gaba_7 supertype marker + anatomy review | PARTIAL |
| edge_is_interneuron_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA — precomputed stats cross-check (Calb2=6.78, Vip=6.82) | SUPPORT |
| edge_is_interneuron_hippocampus_to_CS20230722_SUPT_0179 | ANNOTATION_TRANSFER — MapMyCells · GEO:GSE185862 · Vip subclass n=476 HIP cells | PARTIAL |
| edge_is_interneuron_hippocampus_to_CS20230722_SUPT_0179 | ANNOTATION_TRANSFER — MapMyCells local · GEO:GSE99888 · Calb2.Vip.Igfbp4 · SUPT_0179 F1=0.612 (SUPERTYPE) | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Tyan et al. 2014 | [24671999](https://pubmed.ncbi.nlm.nih.gov/24671999/) | soma location; IS cell definition |
| [2] | Tzilivaki et al. 2023 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Calb2 marker; Vip marker; IS subtype scheme |
| [3] | Chamberland & Topolnik 2012 | [23162426](https://pubmed.ncbi.nlm.nih.gov/23162426/) | Calb2 marker |
| [4] | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | Vip marker |
