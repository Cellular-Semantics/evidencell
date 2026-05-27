# ventral hippocampal dopamine receptor-expressing glutamatergic pyramidal neuron — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | pyramidal neuron (CL:0000598) | |
| Soma location | ventral CA1 / ventral subiculum [UBERON:0002421] | [1] [1] |
| NT | glutamatergic | [1] |
| Markers | Drd1+, Drd2+ | [1] [2] |

---

## Cell Ontology mapping

ventral hippocampal dopamine receptor-expressing glutamatergic pyramidal neuron is a **broad match** to **pyramidal neuron (CL:0000598)** in the Cell Ontology — i.e. **pyramidal neuron (CL:0000598)** is the closest existing CL term (an ancestor) but does not fully cover this type. A new child term is a candidate for submission to CL.

*Mapping notes:* Ventral hippocampal D1R/D2R-expressing glutamatergic pyramidal neurons represent ~45% of all dopamine receptor-positive cells in ventral hippocampus (Godino et al., 2023), contrasting with dorsal hippocampus where D1/D2 are interneuron-restricted. Likely correspond to projection-specific ventral CA1/vSubiculum populations. CL:0000598 is the best available mapping.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] |  | 13,245 |  |  |

All edges: `skos:closeMatch`

---

## 0069 CA1-ProS Glut_1 · 

*`CS20230722_SUPT_0069` · 13,245 cells (10x)*

**Supporting evidence:**

- SUPT_0069 (0069 CA1-ProS Glut_1) is the highest-scoring candidate for ventral CA1 pyramidal cells in WMBv1 (shared target with ca1_pc_hippocampus). Yao 2021 CA1-ProS cells (n=1704) map to SUPT_0069 with 59.3% purity and F1=0.744. The ventral CA1 / ventral subiculum location of hpc_glu_dopa_receptor_pyramidal cells suggests they are a subpopulation within CA1-ProS or SUB-ProS supertypes. Without Drd1/Drd2-specific expression data in the atlas, it is not possible to determine which specific supertype(s) capture the dopamine receptor-expressing subset. This edge is provisional and should be upgraded once AT evidence from a ventral hippocampus dataset with D1R/D2R labelling is available. [Annotation transfer]

**Concerns:**

- **location** (APPROXIMATE): A=ventral CA1 / ventral subiculum (UBERON:0002421) / B=SUPT_0069 in CA1-ProS Glut subclass (dorsal + ventral CA1). The dopamine receptor-expressing cells are specifically described in ventral hippocampus (Godino et al., 2023), while SUPT_0069 captures the full CA1-ProS range (dorsal + ventral). WMBv1 does not clearly separate dorsal/ventral CA1 at the supertype level without MERFISH SOMA location breakdown.

- **marker_Drd1** (DISCORDANT): A=defining marker Drd1 (D1 dopamine receptor) / B=not listed in SUPT_0069 defining markers. Drd1 mean_expression=0.09 in SUPT_0069 — effectively absent (precomputed_stats.h5, supertype level)
- **marker_Drd2** (DISCORDANT): A=defining marker Drd2 (D2 dopamine receptor) / B=not listed in SUPT_0069 defining markers. Drd2 mean_expression=0.02 in SUPT_0069 — effectively absent (precomputed_stats.h5, supertype level)
- The dopamine receptor-expressing glutamatergic pyramidal cells are described as a ventral-specific subpopulation (Godino et al., 2023) within vCA1/vSubiculum. The curation decision in validation_notes.json (whether this is a distinct type or a property annotation) is unresolved. If resolved as a property annotation, this edge should be replaced by Drd1/Drd2 expression annotations on the CA1 and subicular pyramidal cell nodes.
- [AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated from deprecated evidencell:PartialOverlapMatch to skos:closeMatch by `refresh_predicates.py`. Rule: rule-3b: F1=0.744 ≤ 0.75, DISCORDANT comparison(s), existing caveats → closeMatch. Curator review recommended.

**What would upgrade confidence:**

- *Unresolved:* Is hpc_glu_dopa_receptor_pyramidal_hippocampus a distinct cell type or a property of vCA1/vSubiculum pyramidal cells? See curation_decisions_needed in validation_notes.json.

- *Unresolved:* Does any CA1-ProS supertype specifically enrich for ventral CA1 (which would provide a candidate for Drd1/Drd2-expressing cells)?

- *Proposed:* Run add-expression for Drd1 and Drd2 in SUPT_0069-0074 (CA1-ProS supertypes) to identify any ventral-enriched supertype.


---

## Proposed experiments

### 1 — Other

- Run add-expression for Drd1 and Drd2 in SUPT_0069-0074 (CA1-ProS supertypes) to identify any ventral-enriched supertype.
*Resolves: edge_hpc_glu_dopa_receptor_pyramidal_hippocampus_to_supt_0069*

---

## Open questions

1. Is hpc_glu_dopa_receptor_pyramidal_hippocampus a distinct cell type or a property of vCA1/vSubiculum pyramidal cells? See curation_decisions_needed in validation_notes.json.
2. Does any CA1-ProS supertype specifically enrich for ventral CA1 (which would provide a candidate for Drd1/Drd2-expressing cells)?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_hpc_glu_dopa_receptor_pyramidal_hippocampus_to_supt_0069 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Godino et al. 2023 · PMID:37546856 | [37546856](https://pubmed.ncbi.nlm.nih.gov/37546856/) | soma location |
| [2] | Puighermanal et al. 2016 · PMID:27678395 | [27678395](https://pubmed.ncbi.nlm.nih.gov/27678395/) | Drd1 marker |
