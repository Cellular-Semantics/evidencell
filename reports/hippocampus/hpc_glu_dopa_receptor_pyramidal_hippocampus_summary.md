# ventral hippocampal dopamine receptor-expressing glutamatergic pyramidal neuron — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

| Property | Value | References |
|---|---|---|
| CL term | pyramidal neuron (CL:0000598) | |
| Soma location | ventral CA1 / ventral subiculum [UBERON:0002421] | [1] |
| NT | glutamatergic | [1] |
| Defining markers | Drd1 (D1 dopamine receptor), Drd2 (D2 dopamine receptor) | [1][2] |
| Negative markers | — | |
| Neuropeptides | — | |

---

## 2. Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] | CA1-ProS Glut | — | 🔴 LOW | NT CONSISTENT · Drd1/Drd2 DISCORDANT | Speculative |

Total: 1 edge. Relationship type: PARTIAL_OVERLAP (provisional; Drd1/Drd2-expressing cells are a ventral-specific subpopulation within CA1/SUB; SUPT_0069 captures the full CA1-ProS range without ventral enrichment).

---

## 3. Candidate paragraphs

## 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] · 🔴 LOW

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0069 belongs to subclass SUBC_016 CA1-ProS Glut, the dedicated CA1/ProSubiculum glutamatergic subclass in WMBv1. The classical ventral hippocampal dopamine receptor-expressing pyramidal neuron is glutamatergic [1]; this identity is consistent at both the supertype and subclass level.

- **Annotation transfer — PARTIAL.** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) mouse hippocampus SSv4 scRNA-seq CA1-ProS subclass labels onto WMBv1 (CCN20230722): of 1704 CA1-ProS cells, 1011 (59.3%) map to SUPT_0069. F1 = 0.744, coverage = 0.593, purity = 0.999. Target_purity = 0.999 confirms SUPT_0069 is exclusively populated by CA1-ProS cells, but the Yao 2021 CA1-ProS subclass is not annotated for Drd1/Drd2 expression. This annotation transfer reflects the correspondence between Yao 2021 CA1-ProS labels and SUPT_0069, not a confirmation that dopamine receptor-expressing cells specifically map here. The support is therefore PARTIAL — it establishes the ventral CA1 subfield correspondence at a supertype level but does not resolve the Drd1/Drd2 subpopulation identity.

- **Location — APPROXIMATE.** The dopamine receptor-expressing pyramidal cells are described as specifically enriched in ventral hippocampus (vCA1 and ventral subiculum) [1]. SUPT_0069 captures the full CA1-ProS range (dorsal + ventral CA1); WMBv1 does not clearly separate dorsal and ventral CA1 at the supertype level from atlas metadata alone. The ventral-specific enrichment of the classical node within the broader CA1 supertype means the location alignment is APPROXIMATE rather than CONSISTENT.

**Marker evidence provenance**

- **Drd1** [1][2]: Godino et al. 2023 [1] characterises dopamine D1 and D2 receptor-expressing neurons in mouse ventral hippocampus using BAC transgenic Drd1-EGFP and Drd2-EGFP mice combined with single-cell transcriptomics. Cell identity is established by the Drd1/Drd2 transgenic labelling combined with pyramidal layer location in vCA1. Puighermanal et al. 2016 [2] uses BAC transgenic mice expressing EGFP under D1R promoter to characterise D1R-containing neurons in CA1 of dorsal hippocampus. Together these citations provide transcript- and protein-level evidence at the BAC transgenic level — strong specificity for dopamine receptor-expressing cells. However, the precomputed expression stats for SUPT_0069 reveal Drd1 mean expression = 0.09 and Drd2 mean expression = 0.02, both effectively absent at the supertype level. This is a direct discrepancy between the classical node marker definition and the atlas supertype profile: if SUPT_0069 captures the classical type's cells, dopamine receptor expression should be detectable above background.

- **Discrepancy explanation — ventral subpopulation dilution.** The near-zero Drd1/Drd2 expression in SUPT_0069 is most likely explained by the fact that SUPT_0069 captures the entire CA1-ProS Glut population (dorsal + ventral), of which the Drd1/Drd2-expressing cells represent only a small ventral subset. Averaging expression across all cells in the supertype would dilute the signal from this minority subpopulation to near-zero. This interpretation is consistent with the Godino et al. description of gradual ventral enrichment [1]. However, this dilution hypothesis remains unverified without Drd1/Drd2 expression data at the CLUSTER level (sub-supertype level) for ventral CA1-enriched clusters. *(note: this is an interpretation beyond stated facts.)*

**Concerns**

- **Marker Drd1 — DISCORDANT.** Drd1 mean expression = 0.09 in SUPT_0069, effectively absent from the supertype-level precomputed stats. This is the primary counter-evidence to the mapping. The classical node is defined by Drd1 expression, which is not detectable at the supertype level in SUPT_0069.

- **Marker Drd2 — DISCORDANT.** Drd2 mean expression = 0.02 in SUPT_0069, also effectively absent. Both defining markers fail the atlas-level cross-check.

- **Curation decision unresolved: distinct type vs. property annotation.** The facts file records an unresolved curation decision: whether hpc_glu_dopa_receptor_pyramidal_hippocampus is best treated as a distinct cell type or as a property annotation (Drd1/Drd2 expression) to be added to the existing CA1 and subicular pyramidal cell nodes. If resolved as a property annotation, this edge should be replaced by Drd1/Drd2 expression entries on the CA1 and subicular pyramidal cell nodes rather than a separate mapping edge.

- **Location APPROXIMATE — no dorsal/ventral CA1 separation in atlas.** WMBv1 does not explicitly resolve dorsal vs. ventral CA1 at the supertype level in the available metadata. If a ventral-enriched supertype exists within SUBC_016, it would be a stronger candidate than SUPT_0069 for this classical type.

**What would upgrade confidence**

- **Resolve the type vs. property curation decision:** The first step is to determine whether this node is a distinct cell type or a property annotation. If it is a property, the appropriate action is to annotate Drd1/Drd2 expression on the CA1 and subicular pyramidal cell KB nodes and retire this mapping edge, rather than invest in annotation transfer evidence. This curation decision should precede any experimental follow-up.

- **Drd1 and Drd2 expression at CLUSTER level in CA1-ProS supertypes:** Running add-expression for Drd1 and Drd2 across all CA1-ProS supertypes (SUPT_0069–0074) at the atlas level would identify whether any specific supertype shows elevated dopamine receptor expression, suggesting ventral CA1 enrichment. This can be done without new experiments and directly addresses the marker DISCORDANT issue.

- **Annotation transfer from ventral hippocampus D1R/D2R-labelled dataset:** If the node is retained as a distinct type, running annotation transfer from a Drd1-EGFP or Drd2-EGFP ventral hippocampus dataset onto WMBv1 (CCN20230722) would provide direct AnnotationTransferEvidence. Target: F1 ≥ 0.70 at SUPERTYPE level for Drd1+ or Drd2+ cells. Expected output: AnnotationTransferEvidence entries resolving both marker DISCORDANT alignments and potentially identifying a ventral-specific CA1 supertype.

---

## 4. Proposed experiments

### 1 — Curation decision (type vs. property annotation)

**What:** Review the unresolved curation decision (validation_notes.json) on whether this node is a distinct cell type or a Drd1/Drd2 property annotation for CA1/subicular pyramidal cells.

**Target:** Curation decision documented and acted upon.

**Expected output:** Either (a) node retained with updated evidence; or (b) node deprecated and Drd1/Drd2 expression added to CA1 and subicular pyramidal cell nodes.

**Resolves:** Open question 1 (fundamental identity of this node).

### 2 — Atlas expression query (add-expression)

**What:** Run add-expression for Drd1 and Drd2 on CCN20230722 precomputed stats across all SUBC_016 CA1-ProS supertypes (SUPT_0069–0074).

**Target:** Identify any supertype with Drd1 or Drd2 mean expression above background (> 1 UMI), suggesting ventral CA1 enrichment.

**Expected output:** PrecomputedExpression entries for Drd1/Drd2 across CA1-ProS supertypes; identification of ventral-enriched candidate supertype if present.

**Resolves:** Open question 2 (whether any CA1-ProS supertype enriches for ventral CA1); potentially resolves marker DISCORDANT alignments if a ventral-specific supertype is identified.

### 3 — MapMyCells / Annotation transfer (D1R/D2R-labelled ventral hippocampus cells)

**What:** Run annotation transfer from a dataset containing Drd1-EGFP or Drd2-EGFP ventral hippocampal cells (e.g. from Godino et al. 2023 data if available, or from a similar BAC transgenic dataset) onto WMBv1 (CCN20230722).

**Target:** F1 ≥ 0.70 at SUPERTYPE level for Drd1+ or Drd2+ cells.

**Expected output:** AnnotationTransferEvidence entries; identification of the specific supertype(s) that capture dopamine receptor-expressing ventral CA1 pyramidal cells.

**Resolves:** Open question 2; marker DISCORDANT alignments for Drd1 and Drd2; would enable confidence upgrade to MODERATE.

---

## 5. Open questions

1. Is hpc_glu_dopa_receptor_pyramidal_hippocampus a distinct cell type or a property annotation (Drd1/Drd2 expression) for vCA1/vSubiculum pyramidal cells? The curation decision referenced in validation_notes.json must be resolved before further evidence investment is appropriate.

2. Does any CA1-ProS supertype (SUPT_0069–0074) specifically enrich for ventral CA1 neurons, which would provide a stronger candidate for the Drd1/Drd2-expressing population? Running add-expression for Drd1 and Drd2 across CA1-ProS supertypes would resolve this.

---

## 6. Evidence base table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_hpc_glu_dopa_receptor_pyramidal_hippocampus_to_supt_0069 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862) | PARTIAL — F1=0.744; purity=0.999; maps CA1-ProS (not Drd1/Drd2-specific) cells to SUPT_0069; Drd1 mean=0.09 and Drd2 mean=0.02 in SUPT_0069 (DISCORDANT) |

---

## 7. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Godino et al. 2023 · PMID:37546856 | [37546856](https://pubmed.ncbi.nlm.nih.gov/37546856/) | Soma location; NT type; Drd1/Drd2 markers |
| [2] | Puighermanal et al. 2016 · PMID:27678395 | [27678395](https://pubmed.ncbi.nlm.nih.gov/27678395/) | Drd1 marker |
