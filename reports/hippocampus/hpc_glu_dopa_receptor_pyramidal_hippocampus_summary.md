# ventral hippocampal dopamine receptor-expressing glutamatergic pyramidal neuron — WMBv1 (CCN20230722) Mapping Report

## Introduction

Dopamine receptor-expressing pyramidal neurons in the ventral hippocampus are a transcriptionally distinct, topographically restricted population that co-express D1 (Drd1) and/or D2 (Drd2) receptors alongside a glutamatergic pyramidal identity. These cells are enriched specifically in ventral CA1 (vCA1) and ventral subiculum (vSub), with a gradual increase in D1/D2 cell density in the caudal-most parts of the vCA1/vSub transition zone, a distribution that contrasts sharply with dorsal hippocampus where dopamine receptor expression is largely confined to GABAergic interneurons [1].

> We here study dopaminoceptive neurons in mouse ventral hippocampus (vHipp), molecularly distinguished by their expression of dopamine D1 or D2 receptors
> — Godino et al. 2023, abstract · [1] <!-- quote_key: 260336826_f0ffda84 -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Neurotransmitter | Glutamatergic | [1] |
| Defining markers | Drd1 (D1 dopamine receptor), Drd2 (D2 dopamine receptor) | [1], [2] |
| Soma location | Hippocampal formation [UBERON:0002421]; ventral CA1 / ventral subiculum | [1] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

> In the vCA1 pyramidal cell layer, gradual enrichment of both D1 and D2 cells emerges ventral to the rhinal fissure, along with the diffuse 21 transition from vCA1 to vSub. Together, these semiquantitative observations indicate a precise topographical organization of D1 and D2 cells across vHipp subfields and layers, most notably in the DG and in the caudal-most parts of vCA1/vSub.
> — Godino et al. 2023, D1-and D2-expressing cells are topographically organized in vHipp · [1] <!-- quote_key: 260336826_acc436ad -->

> Using BAC transgenic mice expressing enhanced green fluorescent protein under the control of D1R promoter, we examined the molecular identity of D1R-containing neurons within the CA1 subfield of the dorsal hippocampus
> — Puighermanal et al. 2016, abstract · [2] <!-- quote_key: 1711204_2c89b7e1 -->

</details>

### Cell Ontology mapping

| Field | Value |
|---|---|
| CL term | pyramidal neuron (CL:0000598) |
| Mapping type | BROAD |
| Mapping notes | Ventral hippocampal D1R/D2R-expressing glutamatergic pyramidal neurons likely correspond to projection-specific ventral CA1/vSubiculum populations. CL:0000598 is the best available mapping. |

---

## Results

A single WMBv1 candidate was identified: supertype 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069]. Annotation transfer from Yao 2021 hippocampus SSv4 scRNA-seq supports the CA1-ProS Glut supertype alignment at PARTIAL confidence. However, neither defining marker (Drd1 or Drd2) is detectable at the atlas supertype level, and the edge is provisional pending Drd1/Drd2-specific evidence.

![Annotation transfer F1 heatmap (GEO:GSE185862 → WMBv1)](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_tree.png)

### Candidate overview table

| WMBv1 target | Accession | Confidence | Relationship | Verdict |
|---|---|---|---|---|
| 0069 CA1-ProS Glut_1 | CS20230722_SUPT_0069 | 🔴 LOW | PARTIAL_OVERLAP | Speculative |

### Property alignment — 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069]

**Table 1: Property comparison**

| Property | Classical type | WMBv1 SUPT_0069 | Alignment |
|---|---|---|---|
| Neurotransmitter | Glutamatergic | Glutamatergic (CA1-ProS Glut subclass) | CONSISTENT |
| Soma location | Ventral CA1 / ventral subiculum (UBERON:0002421) | CA1-ProS Glut subclass (dorsal + ventral CA1); no dorsal/ventral separation at supertype | APPROXIMATE |
| Marker — Drd1 | Defining | Mean 0.09 UMIs in SUPT_0069 — effectively absent | DISCORDANT |
| Marker — Drd2 | Defining | Mean 0.02 UMIs in SUPT_0069 — effectively absent | DISCORDANT |

**Table 2: Evidence support**

| Evidence type | Supports | Summary |
|---|---|---|
| ANNOTATION_TRANSFER | PARTIAL | Yao 2021 CA1-ProS cells (n=1704; GEO:GSE185862) map to SUPT_0069 with F1=0.744; supports CA1-ProS supertype identity but not Drd1/Drd2 subpopulation specifically |

**MapMyCells F1 — CA1-ProS source group (n=1704 cells, GEO:GSE185862)**

| Level | Best target | F1 | Group purity | Target purity | n cells mapped |
|---|---|---|---|---|---|
| SUPERTYPE | 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] | 0.744 | 0.593 | 0.999 | 1011 |

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Ventral hippocampal dopamine receptor-expressing glutamatergic pyramidal neurons defined as CLASSICAL_MULTIMODAL. Key references: Godino et al. 2023 (PMID:37546856); Puighermanal et al. 2016 (PMID:27678395). Note: an unresolved curation decision exists — whether this node represents a distinct cell type or a property annotation (Drd1/Drd2 expression) to be added to CA1 and subicular pyramidal cell nodes.

**Atlas mapping query.** Candidate search in WMBv1 (CCN20230722) at supertype rank, querying CA1-ProS Glut supertypes. SUPT_0069 identified as the highest-scoring CA1 candidate by annotation transfer.

**Property alignment.** Drd1 (mean 0.09 UMIs) and Drd2 (mean 0.02 UMIs) expression retrieved from precomputed_stats.h5 (CCN20230722) at the SUPT_0069 supertype level — both effectively absent. Low supertype-level Drd1/Drd2 is most likely due to dilution across dorsal + ventral CA1 cells in this supertype; the Drd1/Drd2-expressing subpopulation is a ventral-specific minority.

**Annotation transfer.**

| Run | Dataset | Source label | n cells | Method | Tool |
|---|---|---|---|---|---|
| at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1 | GEO:GSE185862 (Yao 2021, mouse HPF SSv4) | CA1-ProS | 1704 | MapMyCells local, raw normalization, 100 bootstrap iterations | cell_type_mapper |

Code: https://github.com/AllenInstitute/cell_type_mapper

**Anti-hallucination.** All accessions, quote keys, and PMIDs validated against the KB reference store at write time.

*Report generated 2026-05-19. Framework commit: 07c6dbd. KB graph: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`.*

**Evidence base**

| Evidence type | Count |
|---|---|
| ANNOTATION_TRANSFER | 1 |

</details>

---

## Discussion

**The provisional best candidate is 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069]**, supported by the glutamatergic CA1-ProS identity and annotation transfer from a CA1-enriched source dataset. The key weakness is the DISCORDANT alignment for both defining markers: Drd1 and Drd2 are essentially absent from SUPT_0069 at the supertype level, most plausibly because this supertype pools dorsal and ventral CA1 cells and the dopamine receptor-expressing cells are a ventral minority too small to elevate the supertype mean. An additional fundamental uncertainty concerns whether this node represents a genuinely distinct cell type or whether Drd1/Drd2 expression is better treated as a property annotation on existing CA1 and subicular pyramidal cell nodes — this curation decision should be resolved before further evidence investment. The ventral-specificity claim makes an independent second AT run from a D1R- or D2R-labelled ventral hippocampus dataset the most informative next experiment.

> these neurons are transcriptionally distinct and topographically organized across vHipp subfields and cell types.
> — Godino et al. 2023, abstract · [1] <!-- quote_key: 260336826_67252bb8 -->

### Proposed experiments

1. Run `just add-expression` for Drd1 and Drd2 across all CA1-ProS supertypes (SUPT_0069–0074) in CCN20230722 to identify whether any supertype shows elevated dopamine receptor expression, suggesting ventral CA1 enrichment.
2. If the node is retained as a distinct type, run MapMyCells annotation transfer from a Drd1-EGFP or Drd2-EGFP ventral hippocampal dataset onto WMBv1 to identify the specific supertype(s) capturing dopamine receptor-expressing vCA1 pyramidal cells.
3. Resolve the curation decision (distinct type vs. property annotation) documented in the planning notes before committing additional evidence-gathering resources.

### Open questions

1. Is this node a distinct cell type or a property annotation (Drd1/Drd2 expression) that belongs on existing CA1 and subicular pyramidal cell nodes?
2. Does any CA1-ProS supertype (SUPT_0069–0074) specifically enrich for ventral CA1 neurons, which would provide a stronger candidate for the Drd1/Drd2-expressing population?

---

## References

[1] Godino et al. 2023 · PMID:37546856 · DOI:10.1101/2023.07.25.550554

[2] Puighermanal et al. 2016 · PMID:27678395 · DOI:10.1007/s00429-016-1314-x
