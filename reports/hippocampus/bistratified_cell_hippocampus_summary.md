# Bistratified cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | bistratified cell (CL:0004247) | |
| Soma location | CA1 stratum pyramidale [UBERON:0014548]; CA1 stratum oriens [UBERON:0014552]; CA1 stratum radiatum [UBERON:0014554] | [1] [2] [3] [1] [2] [3] [1] [2] [3] |
| NT | GABAergic | [4] |
| Markers | Pvalb+, Sst+, Tac1+ | [5] [6] [7] [8] [9] |
| Neuropeptides | Sst | [9] |

---

## Cell Ontology mapping

Bistratified cell is a **broad match** to **bistratified cell (CL:0004247)** in the Cell Ontology — i.e. **bistratified cell (CL:0004247)** is the closest existing CL term (an ancestor) but does not fully cover this type. A new child term is a candidate for submission to CL.

*Mapping notes:* CL:0004247 is retinal-focused. The hippocampal bistratified interneuron (Pvalb/Sst/Tac1+, axon in SO and SR) has no dedicated CL term.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] |  | 2,860 | 🟡 MODERATE | Best candidate |
| 2 | 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] | 0206 Pvalb Gaba_2 | 1,312 | 🟡 MODERATE | Best candidate |
| 3 | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] |  | 2,712 | 🔴 LOW | Speculative |

All edges: `evidencell:PartialOverlapMatch`

---

## 0206 Pvalb Gaba_2 · 🟡 MODERATE

*`CS20230722_SUPT_0206` · 2,860 cells (10x)*

**Supporting evidence:**

- SUPT_0206 (Pvalb Gaba_2) is the dominant hippocampal Pvalb supertype and primary atlas target for canonical PV bistratified cells. Pvalb is the defining marker of bistratified cells; this supertype is Pvalb subclass. Child cluster CLUS_0737 shows bilaminar anatomy (CA1 SO: 361 cells, CA1 SR: 72 cells) directly consistent with bistratified axon targets (stratum oriens + radiatum). CLUS_0737 NP markers include Sst:4.4 and Tac1:7.3, both consistent with bistratified identity (PMID:38640347). PARTIAL: supertype also contains PV basket cells (CLUS_0739); CLUS_0737 provides cluster-level resolution. [Atlas metadata]
- MapMyCells local (cell_type_mapper v1.7.1, Que 2021, GSE142546) PV bistratified cells (20 cells: hBIC + vBIC). 18/20 cells map to SUPT_0206 (coverage=0.900, F1=0.375). Best cluster hit: CLUS_0737 (F1=0.800, coverage=0.941, purity=0.696). BC cells preferentially map to CLUS_0739; BIC cells to CLUS_0737 — this BC/BIC cluster separation is a genuine transcriptomic signal from morphologically labelled cells. Gene symbols remapped to Ensembl IDs; 19788/35825 genes mapped. [Annotation transfer]

**Concerns:**

- SUPT_0206 contains both PV basket cells (CLUS_0739) and PV bistratified cells (CLUS_0737). Not separable at supertype level; see CLUS_0737 edge for cluster-level mapping.

**What would upgrade confidence:**

- *Unresolved:* Whether SUPT_0206 provides morphologically informative substructure beyond the CLUS_0737 / CLUS_0739 BIC/BC cluster-level split.

---

## 0737 Pvalb Gaba_2 · 🟡 MODERATE

*`CS20230722_CLUS_0737` · 1,312 cells (10x) · supertype: 0206 Pvalb Gaba_2*

**Supporting evidence:**

- CLUS_0737 (Pvalb Gaba_2, child of SUPT_0206). Top anatomy: CA1 SO (361), CA1 SR (72), CA3 SO (72). The bilaminar CA1 SO + CA1 SR distribution directly matches the bistratified cell axon territory. MERFISH markers: Moxd1, Grpr, Syt2, Nxph2, Prkg2. NP markers: Cort:8.0, Tac1:7.3, Npy:5.5, Cck:5.2, Sst:4.4 — Sst and Tac1 are directly consistent with bistratified identity (PMID:38640347). Scoped marker: Ednra. SUPPORT: anatomy + marker profile converge on bistratified identity. [Atlas metadata]
- MapMyCells local (Que 2021, GSE142546) PV bistratified cells (20 cells). CLUS_0737 is the primary cluster hit: F1=0.800, coverage=0.941, purity=0.696. BC cells (basket) preferentially map to sibling CLUS_0739 (F1=0.827) — BC/BIC cluster separation within SUPT_0206 distinguishes basket from bistratified cells at cluster level. Strongest AT signal for bistratified cell identity in WMBv1. [Annotation transfer]
- Harris 2018 cells labelled Sst_Tac1 by Chamberland per-cluster rules (bistratified proxy, n=168 total) map to Pvalb Gaba subclass (F1=0.578, recall=0.783) and specifically to CLUS_0737 Pvalb Gaba_2 (purity=0.939 at cluster level). High purity confirms CLUS_0737 as the specific landing site within the Pvalb tree. Consistent with Chamberland 2024 (PMID:38640347) Fig 6 Sst-Pvalb transcriptomic continuum for bistratified cells. PARTIAL — Sst_Tac1 label is in-silico derived from Harris cluster-mean expression, not morphologically confirmed. See at_run_20260506_harris_chamberland_mmc_wmbv1 README Caveats. [Annotation transfer]

**Concerns:**

- Sst-expressing bistratified subpopulation may distribute toward SUPT_0216 (see edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216). CLUS_0737 captures the PV-primary bistratified population.

**What would upgrade confidence:**

- *Unresolved:* Replication of Que 2021 BIC → CLUS_0737 F1=0.80 with an independent morphologically confirmed PV bistratified scRNA-seq dataset.
- *Unresolved:* Robustness of CLUS_0737 assignment to raw-counts vs TPM-pseudo-counts normalization in GEO:GSE142546.

---

## 0216 Sst Gaba_3 · 🔴 LOW

*`CS20230722_SUPT_0216` · 2,712 cells (10x)*

**Supporting evidence:**

- REFRAMED (Que 2021): this edge now represents the Sst-expressing bistratified subpopulation specifically, not the full bistratified cell population. The canonical PV bistratified cell maps to SUPT_0206/CLUS_0737 (see separate edge). SUPT_0216 assignment is supported by Sst/Tac1 component only: Chamberland et al. 2024 (PMID:38640347) used Sst;;Tac1 intersection to target bistratified cells, and SUPT_0216 carries Tac1 in DEFINING_SCOPED markers. Sst and Reln are expressed in bistratified cells and consistent with SUPT_0216. PARTIAL: supertype also contains OLM and HS cells. Que 2021 patch-seq BIC cells (20 cells) show zero mapping to any Sst supertype, mapping entirely to SUPT_0206 (Pvalb Gaba_2). This edge therefore represents a potential Sst-dominant bistratified subpopulation, not the primary atlas target. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Pvalb subclass (n=66 HIP cells) onto WMBv1. SUPT_0216 (Sst Gaba_3) receives only 6/66 Pvalb cells (F1=0.053, purity=0.036). The Pvalb population maps predominantly to Pvalb chandelier (SUPT_0204, F1=0.612) and Pvalb Gaba_2 (SUPT_0206, F1=0.324) supertypes. SUPT_0216 is a Sst supertype; Sst SSv4 cells map to SUPT_0216 with F1=0.488 (83/273 cells). PARTIAL: the weak Pvalb→SUPT_0216 signal reflects possible Sst co-expression in a bistratified cell subpopulation, consistent with the known transcriptomic plasticity of bistratified cells (some express both Pvalb and Sst). The Sst SSv4 Gaba population partially supports this target, but SUPT_0219 (Sst Gaba_6, F1=0.759) is the dominant Sst target. This edge should be interpreted with LOW confidence. Yao 2021 SSv4 'Pvalb' subclass label (n=66 HIP cells) encompasses PV basket, axo-axonic, and bistratified cells; subtype resolution requires a morphologically identified PV-IN dataset. [Annotation transfer]
- MapMyCells local (Que 2021, GSE142546) morphologically identified PV bistratified cells (20 cells: hBIC + vBIC). BIC cells show NO mapping to any Sst supertype: 18/20 map to SUPT_0206 (F1=0.375) and 16/20 concentrate at CLUS_0737 (F1=0.800). SUPT_0216 (Sst Gaba_3) F1 is absent from BIC top results. This AT does not support SUPT_0216 as the primary target for canonical PV bistratified cells. The evidence for this edge rests on Sst marker co-expression and Chamberland 2024 Sst;;Tac1 genetics, which capture a Sst-dominant bistratified subpopulation. See edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206 and edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 for the primary mapping. [Annotation transfer]

**Concerns:**

- **location_CA1_stratum_pyramidale** (APPROXIMATE): A=CA1 stratum pyramidale (UBERON:0014548) — soma / B=CA1 stratum oriens (MBA:399, 818 cells) — no pyramidal layer listed. Dominant hippocampal signal in CA1 SO, not pyramidale. Bistratified cell soma classically in/near stratum pyramidale.
- **marker_Pvalb** (DISCORDANT): A=Pvalb — defining marker (co-expressed with Sst) / B=Sst subclass, not Pvalb; Pvalb not in supertype markers; precomputed stats mean: 1.48. Bistratified cells co-express Pvalb and Sst (PMID:37467748). The Sst subclass placement is consistent with the Sst component but the Pvalb component is not captured. High transcriptomic similarity within Sst subclass may place bistratified closer to OLM cells than PV basket cells at transcriptomic level.

- Sst Gaba_3 supertype contains at least three classical hippocampal types: OLM cells (Sst+/Chrna2+), bistratified cells (Sst+/Pvalb+/Tac1+), and HS cells (Sst+, long-range projecting). These are not separable at supertype level. This edge and the olm_cell_ca1 edge to the same supertype reflect this overlap explicitly.
- Pvalb co-expression (defining for bistratified) is not captured at the supertype level — Sst subclass placement may under-represent the PV component of bistratified cell identity.

**What would upgrade confidence:**

- *Unresolved:* Does a Sst-dominant Pvalb-low bistratified subpopulation exist, and if so does it map to CS20230722_SUPT_0216 specifically? Requires a Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq + morphology dataset.

---

## Open questions

1. Whether SUPT_0206 provides morphologically informative substructure beyond the CLUS_0737 / CLUS_0739 BIC/BC cluster-level split.
2. Replication of Que 2021 BIC → CLUS_0737 F1=0.80 with an independent morphologically confirmed PV bistratified scRNA-seq dataset.
3. Robustness of CLUS_0737 assignment to raw-counts vs TPM-pseudo-counts normalization in GEO:GSE142546.
4. Does a Sst-dominant Pvalb-low bistratified subpopulation exist, and if so does it map to CS20230722_SUPT_0216 specifically? Requires a Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq + morphology dataset.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206 | Atlas metadata | PARTIAL |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206 | Annotation transfer | SUPPORT |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 | Atlas metadata | SUPPORT |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 | Annotation transfer | SUPPORT |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 | Annotation transfer | PARTIAL |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | Atlas metadata | PARTIAL |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | Annotation transfer | PARTIAL |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland & Topolnik 2012 · PMID:23162426 | [23162426](https://pubmed.ncbi.nlm.nih.gov/23162426/) | soma location |
| [2] | Bocchio et al. 2024 · PMID:39401246 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | soma location |
| [3] | Perez et al. 2020 · PMID:33404500 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | soma location |
| [4] | Dannenberg et al. 2017 · PMID:29321728 | [29321728](https://pubmed.ncbi.nlm.nih.gov/29321728/) | neurotransmitter type |
| [5] | Ekins et al. 2020 · PMID:33150866 | [33150866](https://pubmed.ncbi.nlm.nih.gov/33150866/) | Pvalb marker |
| [6] | Chamberland et al. 2023 · PMID:37162922 | [37162922](https://pubmed.ncbi.nlm.nih.gov/37162922/) | Pvalb marker |
| [7] | Tzilivaki et al. 2023 · PMID:37467748 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Pvalb marker |
| [8] | Que et al. 2021 · PMID:33398060 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060/) | Pvalb marker |
| [9] | Chamberland et al. 2024 · PMID:38640347 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | Sst marker |

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.78
  rationale: >
    Morphologically confirmed PV bistratified patch-seq cells from Que 2021
    (`at_run_20260508_que2021_pvin_mmc_wmbv1`) map to
    CS20230722_CLUS_0737 at F1=0.80 (coverage 0.941, purity
    0.696), with the sibling BC group separating to CLUS_0739. Atlas
    precomputed expression on CS20230722_CLUS_0737 confirms the
    bistratified-specific bilaminar CA1 SO + CA1 SR MERFISH anatomy with
    NP Sst:4.4 and Tac1:7.3 matching Chamberland 2024 Sst;;Tac1
    intersectional Cre-line targeting; the Chamberland-on-Harris in-silico
    Sst_Tac1 subfamily AT (`at_run_20260512_chamberland_subfamily_mmc_wmbv1`)
    independently concentrates at CS20230722_CLUS_0737 (purity
    0.939), demonstrating Sst-Pvalb transcriptomic continuity from a
    Sst-side label; 3 of 3 marker_-prefixed PCs CONSISTENT across
    patch-seq and scRNA-seq modalities.
  unresolved_questions:
    - Replication of Que 2021 BIC → CLUS_0737 F1=0.80 with an independent
      morphologically confirmed PV bistratified scRNA-seq dataset.
    - Robustness of CLUS_0737 assignment to raw-counts vs TPM-pseudo-counts
      normalization in GEO:GSE142546.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.65
  rationale: >
    Que 2021 morphologically confirmed BIC patch-seq cells map 18/20 to
    CS20230722_SUPT_0206 at F1=0.38 (coverage 0.900) in
    `at_run_20260508_que2021_pvin_mmc_wmbv1`, with cluster-level resolution
    at CS20230722_CLUS_0737 reaching F1=0.80 — the supertype F1 is bounded
    by sibling-cluster confusion with the PV basket child CLUS_0739, not
    by source-target mismatch. Atlas Pvalb subclass placement (scRNA-seq +
    MERFISH) supports the Pvalb defining marker; 3 of 3 marker_-prefixed PCs CONSISTENT
    (Pvalb via subclass, Sst/Tac1/GABA via CLUS_0737).
  unresolved_questions:
    - Whether SUPT_0206 provides morphologically informative substructure
      beyond the CLUS_0737 / CLUS_0739 BIC/BC cluster-level split.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.22
  rationale: >
    CS20230722_SUPT_0216 carries Sst (precomputed mean 11.44) and Tac1
    DEFINING_SCOPED, both consistent with Chamberland 2024 Sst;;Tac1
    intersectional Cre-line targeting of bistratified cells, but Pvalb is
    DISCORDANT at the supertype (Sst-subclass placement); 3 of 4 marker_-prefixed
    PCs CONSISTENT. Yao 2021 SSv4 'Pvalb' scRNA-seq cells map only weakly
    (F1=0.05 in `at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1`), and
    morphologically confirmed Que 2021 BIC patch-seq cells
    (`at_run_20260508_que2021_pvin_mmc_wmbv1`) show zero mapping to
    CS20230722_SUPT_0216 — they map entirely to the Pvalb side at
    CS20230722_SUPT_0206 / CS20230722_CLUS_0737. The edge is retained
    speculatively for a possible Sst-dominant Pvalb-low bistratified
    subpopulation; supertype also pools OLM (Sst+/Chrna2+) and HS
    (long-range projecting Sst+) cells (DISTRIBUTED_ACROSS_CLUSTERS).
  unresolved_questions:
    - Does a Sst-dominant Pvalb-low bistratified subpopulation exist, and
      if so does it map to CS20230722_SUPT_0216 specifically? Requires a
      Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq +
      morphology dataset.
```
<!-- verdict-block-end -->
