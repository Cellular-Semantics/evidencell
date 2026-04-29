# ventral hippocampal dopamine receptor-expressing glutamatergic pyramidal neuron — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type definition

| Property | Value | References |
|---|---|---|
| Soma location | Hippocampal formation [UBERON:0002421] (*ventral CA1 / ventral subiculum*) | [1] |
| Neurotransmitter | Glutamatergic | [1] |
| Defining markers | *Drd1*, *Drd2* | [1][2] |
| CL term | pyramidal neuron [CL:0000598] (BROAD) | — |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_SUPT_0069 | 0069 CA1-ProS Glut_1 | — | ⚪ LOW | NT consistent; location approximate; Drd1/Drd2 not assessed | Speculative |

**Total edges: 1 · Relationship type: PARTIAL_OVERLAP.** *(note: Drd1/Drd2-expressing cells are described as a ventral-restricted subpopulation within CA1/subiculum; WMBv1 does not resolve a dedicated dopamine receptor-expressing supertype at the current atlas resolution)*

---

## 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] · ⚪ LOW

### Supporting evidence

- **Atlas metadata — subclass assignment:** SUPT_0069 [CS20230722_SUPT_0069] belongs to subclass CS20230722_SUBC_016 (016 CA1-ProS Glut), the dedicated CA1/prosubiculum glutamatergic subclass in WMBv1. It is the highest-scoring candidate for ventral CA1 pyramidal cells in the atlas and is shared as the primary candidate with the CA1 pyramidal cell node (ca1_pc_hippocampus).
- **Atlas metadata — NT type:** The parent subclass SUBC_016 is named "CA1-ProS Glut", confirming glutamatergic identity consistent with the classical node.
- **Annotation transfer — GSE185862 (Yao 2021 SSv4):** Of 1704 CA1-ProS cells from this dataset, 1011 (59.3%) mapped to SUPT_0069 [CS20230722_SUPT_0069] at the supertype level; F1 = 0.744, target_purity = 1.0. This demonstrates SUPT_0069 [CS20230722_SUPT_0069] exclusively receives CA1-ProS cells in this dataset, supporting it as the primary CA1-ProS representative. The dopamine receptor-expressing subpopulation described in [1] is expected to fall within this broader CA1-ProS correspondence, but cannot be resolved to a specific supertype from current evidence.

### Marker evidence provenance

- **Drd1 — dopamine D1 receptor, defining marker, not assessed in atlas:** *Drd1* is listed as a defining marker supported by two sources: Godino et al. 2023 [1] and Puighermanal et al. 2016 [2]. Godino et al. 2023 [1] characterised dopaminoceptive neurons in mouse ventral hippocampus by their expression of D1 or D2 receptors using BAC transgenic and immunofluorescence approaches. Puighermanal et al. 2016 [2] examined D1R-containing neurons by BAC transgenic reporter (eGFP under D1R promoter) in dorsal CA1 *(note: the Puighermanal 2016 study is explicitly described in dorsal hippocampus, while the classical node targets ventral hippocampus — a geographical discordance that cannot be resolved from current atlas metadata)*. Neither *Drd1* nor *Drd2* appears in the SUPT_0069 [CS20230722_SUPT_0069] defining marker list; both comparisons are flagged NOT_ASSESSED.
- **Drd2 — dopamine D2 receptor, defining marker, not assessed in atlas:** *Drd2* is supported by Godino et al. 2023 [1] alone. It is co-expressed with *Drd1* in a subset of ventral hippocampal neurons, with topographic organisation across vCA1/vSubiculum. The D2-expressing population has not been characterised at the single-cell transcriptomic level in the WMBv1 atlas based on current metadata.
- **No dopamine receptor expression data available from atlas:** The atlas metadata for SUPT_0069 [CS20230722_SUPT_0069] and its sibling CA1-ProS supertypes does not include *Drd1* or *Drd2* among defining markers. The precomputed expression statistics for these receptors across CA1-ProS supertypes (SUPT_0069–0074) have not been queried; their absence from the defining marker list does not exclude detectable expression.

### Concerns

- **Ambiguous mapping — type vs. property annotation:** The most fundamental uncertainty for this node is whether Drd1/Drd2-expressing hippocampal pyramidal neurons constitute a distinct transcriptomic cell type or are a functional/molecular property annotation on CA1 pyramidal cells. Godino et al. 2023 [1] describes these as transcriptionally distinct and topographically organised, supporting a type-level distinction. However, if the Drd1/Drd2 signature does not produce a separable cluster in WMBv1, the appropriate representation may be a marker annotation on the CA1 pyramidal cell node rather than a separate mapping edge. This curation decision is unresolved.
- **Location alignment is APPROXIMATE:** The dopamine receptor-expressing cells are specifically described in ventral hippocampus — ventral CA1 and ventral subiculum [1] — while SUPT_0069 [CS20230722_SUPT_0069] captures the full CA1-ProS range (dorsal + ventral). WMBv1 does not clearly separate dorsal and ventral CA1 at the supertype level without MERFISH spatial breakdown. The ventral restriction is a defining feature of this classical node that is not reproduced in the atlas candidate.
- **Dorsal/ventral discordance in marker evidence:** The Puighermanal 2016 [2] evidence for *Drd1* is explicitly from dorsal CA1, while the Godino 2023 [1] characterisation of the classical node is in ventral hippocampus. It is possible that Drd1-expressing CA1 pyramidal cells in dorsal and ventral hippocampus belong to different transcriptomic supertypes.

### What would upgrade confidence

- Run add-expression for *Drd1* and *Drd2* across CA1-ProS supertypes SUPT_0069–0074 to identify any ventral-enriched supertype with dopamine receptor expression.
- Perform annotation transfer using a ventral hippocampus dataset with D1R/D2R cell labelling (e.g. Drd1-Cre × reporter or FISH-validated single-cell data); F1 ≥ 0.7 in a specific CA1-ProS supertype would support a MODERATE confidence edge.
- Resolve the type-vs-property curation decision: if Godino 2023 [1] transcriptomic data support a separable cluster, a distinct node is justified; if not, the node should be retired and Drd1/Drd2 annotations added to ca1_pc_hippocampus.

---

## Proposed experiments

### Atlas precomputed expression query — Drd1, Drd2

| Attribute | Detail |
|---|---|
| **What** | Run `just add-expression` for *Drd1* and *Drd2* across all CA1-ProS supertypes in WMBv1 (SUPT_0069–0074) |
| **Target** | Mean expression and fraction expressing per supertype; identify any supertype with enriched dopamine receptor expression |
| **Expected output** | PropertySource marker evidence entries for *Drd1* / *Drd2* on the appropriate CA1-ProS supertype node(s) |
| **Resolves** | Drd1/Drd2 NOT_ASSESSED comparisons on SUPT_0069 [CS20230722_SUPT_0069]; may identify a ventral-enriched supertype as a more specific mapping target |

### Annotation transfer — ventral hippocampus D1R/D2R dataset

| Attribute | Detail |
|---|---|
| **What** | MapMyCells annotation transfer using a ventral hippocampus scRNA-seq dataset with Drd1/Drd2 cell identity labels onto WMBv1 |
| **Target** | F1 ≥ 0.7 for Drd1/Drd2-expressing cell labels mapped to a specific CA1-ProS supertype |
| **Expected output** | AnnotationTransferEvidence entries per supertype, enabling upgrade from LOW to MODERATE confidence |
| **Resolves** | Which CA1-ProS supertype(s) within CS20230722_SUBC_016 contain the ventral-hippocampal dopamine receptor-expressing pyramidal cell population |

---

## Open questions

1. Are Drd1/Drd2-expressing ventral hippocampal pyramidal neurons a transcriptomically distinct cell type (warranting a dedicated node and mapping edge) or a functional property annotation on CA1/subicular pyramidal cells? The Godino et al. 2023 [1] claim of transcriptional distinctness must be evaluated against WMBv1 cluster resolution to resolve this.
2. Does any CA1-ProS supertype within CS20230722_SUBC_016 specifically enrich for ventral CA1 identity, which would provide a candidate to test for Drd1/Drd2 expression?
3. Is the dorsal CA1 D1R population characterised by Puighermanal et al. 2016 [2] the same transcriptomic type as the ventral D1R population in Godino et al. 2023 [1], or does dorsal/ventral hippocampus segregate into different supertypes in WMBv1?

---

## Evidence base

| Edge ID | Evidence type | Details | Supports |
|---|---|---|---|
| edge_hpc_glu_dopa_receptor_pyramidal_hippocampus_to_supt_0069 | ATLAS_METADATA | SUPT_0069 [CS20230722_SUPT_0069] in subclass 016 CA1-ProS Glut; highest-scoring CA1-ProS candidate; Drd1/Drd2 not in defining markers | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Godino et al. 2023 | [37546856](https://pubmed.ncbi.nlm.nih.gov/37546856/) | Soma location; NT type; Drd1 marker; Drd2 marker |
| [2] | Puighermanal et al. 2016 | [27678395](https://pubmed.ncbi.nlm.nih.gov/27678395/) | Drd1 marker |
