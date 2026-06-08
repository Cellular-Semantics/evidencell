# hippocampal calretinin-positive glutamatergic neuron — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

## Introduction

Calretinin (Calb2) labels a small population of glutamatergic neurons in the rodent hippocampal formation [UBERON:0002421] whose somata sit in stratum lacunosum-moleculare and the outer molecular layer of the dentate gyrus. These cells are distinct from the much larger calretinin-positive GABAergic interneuron population and are notable as the first reported source of intrinsic glutamatergic connections that run counter to the classical trisynaptic loop [2]. Resolving their transcriptomic identity in WMBv1 is complicated by their rarity in adult mouse and by overlap with developmentally derived Cajal-Retzius cells in the same laminar zone.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | hippocampal formation [UBERON:0002421] (stratum lacunosum-moleculare / outer molecular layer) | [1], [2] |
| NT | glutamatergic | — |
| Markers | Calb2 (calretinin) | — |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical anatomy · rodent hippocampal formation · [1], [2]
  > Hippocampome.org is a comprehensive knowledge base of neuron types in the rodent hippocampal formation (dentate gyrus, CA3, CA2, CA1, subiculum, and entorhinal cortex)
  > — Wheeler et al. 2015, abstract · [1] <!-- quote_key: 631148_edb9eac6 -->

  > Notably, CR cells provide the first evidence of intrinsic glutamatergic hippocampal connections that flow against the classical trisynaptic circuit direction (Anstotz et al., 2015)(Ceranik et al., 1997).
  > — Ceranik et al. 1997, Specialized Glutamatergic Populations · [2] <!-- quote_key: 393787_0325d3d4 -->

</details>

Cell Ontology mapping: glutamatergic neuron [[CL:0000679](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000679)] (BROAD).

---

## Results

Annotation transfer of an independent mouse hippocampal scRNA-seq dataset places the classical calretinin-positive glutamatergic population onto the WMBv1 supertype 0135 HPF CR Glut_1 [CS20230722_SUPT_0135] (F1=0.99 at supertype), with the source paper's "Cajal-Retzius" cluster mapping cleanly within the HPF CR Glut lineage (see figure and property comparison table below). Confidence in the mapping is LOW because the supertype contains only n=5 reference cells in WMBv1, the source cluster is annotated as Cajal-Retzius rather than as the proposed adult SLM/OML Calb2+ population, and other high-Calb2 candidates in the candidate cohort sit in off-target laminae (CA3, entorhinal, presubiculum) and therefore do not relieve the ambiguity.

![Annotation transfer F1 heatmap (GEO:GSE95315 → WMBv1)](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/figures/f1_tree.png)

*F1 across taxonomy levels for the Hochgerner 2018 (GEO:GSE95315) hippocampal scRNA-seq source groups mapped onto WMBv1. Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. The Cajal-Retzius source row converges on the HPF CR Glut lineage at every taxonomy level.*

### 0135 HPF CR Glut_1 · 🔴 LOW

**Property comparison (Table 1).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | hippocampal formation [UBERON:0002421] | Hippocampal formation [MBA:1089] count_100um=2967; Dentate gyrus [MBA:726] count_100um=2414; Dentate gyrus, molecular layer [MBA:10703] count_100um=2410 | not assessed | CONSISTENT |
| NT type | glutamatergic | not asserted | not assessed | NOT_ASSESSED |
| Calb2 expression | defining marker | Calb2: 4.86; cohort_pct 0.848; child-coverage 1.000 | not assessed | CONSISTENT |

*(Subcluster-level breakdown not collected for SUPT_0135; child-cluster coverage of 1.000 indicates all 5 child clusters contribute to the supertype-level Calb2 mean, but per-child expression values were not extracted into the edge YAML — see proposed experiments.)*

**Evidence support (Table 2).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| WMBv1 precomputed stats — Calb2, Reln, Trp73 | Atlas metadata | SUPPORT | Calb2 mean 4.86 on supertype; Reln 12–13, Trp73 8.8–9.7 UMIs/cell on 5 reference cells | atlas-internal |
| Hochgerner 2018 → WMBv1 MapMyCells | Annotation transfer | SUPPORT | F1=0.99 at SUBC_036/SUPT_0135; F1=1.00 at CLUS_0497 | atlas-internal |

**Supporting evidence**

- The MapMyCells transfer of Hochgerner 2018 (GEO:GSE95315) mouse dentate gyrus scRNA-seq onto WMBv1 maps the source dataset's Cajal-Retzius cluster (n=33 cells) exclusively into the HPF CR Glut lineage — F1=0.99 at both subclass 036 HPF CR Glut and supertype 0135 HPF CR Glut_1 [CS20230722_SUPT_0135], and F1=1.00 at the cluster level. Group purity of 1.0 across levels means every Cajal-Retzius source cell stays within this subtree.
- Atlas-side precomputed stats place SUPT_0135 as the only WMBv1 glutamatergic supertype in the stratum lacunosum-moleculare / outer molecular layer of the hippocampal formation, with high Calb2 (mean 4.86 across the supertype) co-expressed with Reln (12–13 UMIs/cell) and Trp73 (8.8–9.7 UMIs/cell) on the supertype's 5 reference cells.
- The atlas-internal evidence narrative summarising the SUPT_0135 case (paraphrased): SUPT_0135 is the only WMBv1 glutamatergic supertype located in the SLM / outer molecular layer of the HPF and the only HPF Glut supertype not assigned to a DG/CA/SUB subclass; WMBv1 precomputed stats show high Calb2 in SUPT_0135 reference cells (mean 4.5–8.2 UMIs/cell across 5 clusters; n=1 each) versus near-absent Calb2 in DG Glut supertypes (0.08–0.16 UMIs); the same reference cells co-express high Reln (12–13 UMIs/cell) and Trp73 (8.8–9.7 UMIs/cell), consistent with Cajal-Retzius cell identity in the SLM/OML; confidence is held at LOW because Slc17a8 (VGluT3) is essentially absent from SUPT_0135 (0–0.3 UMIs in 2 of 5 clusters), the reference population is extremely small (n=5 cells total), and the 'HPF CR' designation may specifically capture developmentally transient Cajal-Retzius cells rather than the proposed VGluT3+/Calb2+ glutamatergic population described in the literature.

**Marker evidence provenance**

- **Calb2** is the only defining marker carried on the classical node and has no primary citation attached. The atlas-side evidence is at transcript level via WMBv1 precomputed stats; calretinin protein expression in SLM/OML glutamatergic cells is the classical anatomical claim *(note: not directly cited in the facts file beyond the general Hippocampome.org overview [1])*. A targeted literature trawl for "calretinin SLM glutamatergic mouse" would anchor this marker to a primary study and clarify whether Slc17a8 (VGluT3) co-expression is expected on the proposed population — the edge narrative references VGluT3 as a "second defining marker" but no such marker is recorded on the classical node, so the assertion is currently unanchored on the KB side.

**Concerns**

- The transcriptomic source mapped by AT is annotated as **Cajal-Retzius**, a developmentally transient population that is largely lost from adult rodent hippocampus, whereas the classical type described in [2] is an adult intrinsic glutamatergic neuron. The two may share laminar position, calretinin expression, and Reln co-expression yet not be the same cell type. The AMBIGUOUS_MAPPING caveat on the edge surfaces this directly.
- SUPT_0135 has only **n=5 WMBv1 reference cells** (1 per child cluster), the smallest representation of any HPF Glut supertype. This is consistent with either extreme rarity or undersampling; statistical inferences from this reference set carry low weight regardless of how strong the AT F1 looks.
- The atlas-internal narrative flags **Slc17a8 (VGluT3) absent** from SUPT_0135 (0–0.3 UMIs in 2 of 5 clusters). If VGluT3 is a true marker of the adult SLM/OML calretinin-positive glutamatergic cells described in the literature, its absence in SUPT_0135 argues against this being the proposed population *(note: VGluT3 is not encoded as a marker on the current classical node — this is an external claim from the atlas narrative)*.
- A migration caveat notes that the edge's predicate was automatically rewritten from the deprecated `evidencell:PartialOverlapMatch` to `skos:closeMatch` and flags curator review.

**What would upgrade confidence**

- Run annotation transfer from a dataset of validated Calb2+/Slc17a8+ SLM cells against WMBv1 and check whether the resulting source group maps to SUPT_0135 or to a different supertype — this is the experiment that directly distinguishes the Cajal-Retzius interpretation from the adult SLM/OML interpretation.
- Inspect MERFISH soma locations for the cells contributing to SUPT_0135 in WMBv1 (atlas browser / MERFISH cell-type distribution) to confirm SLM/OML placement rather than displaced or developmental positioning.
- Targeted literature search for primary work establishing Calb2 (and any VGluT3 co-expression) in adult mouse SLM/OML glutamatergic neurons, to anchor the classical marker definition before treating the AT signal as a 1:1 call.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0135 HPF CR Glut_1 [CS20230722_SUPT_0135]` | — | 3116 | 🔴 LOW | Cajal-Retzius AT F1=0.99 to supertype; SLM/OML location | Primary |
| `0316 CA3 Glut_5 [CS20230722_CLUS_0316]` | 0079 CA3 Glut_5 | 202 | ⚪ UNCERTAIN | High Calb2 (9.60) but CA3 stratum radiatum | Eliminated (wrong laminar zone — CA3) |
| `0317 CA3 Glut_5 [CS20230722_CLUS_0317]` | 0079 CA3 Glut_5 | 116 | ⚪ UNCERTAIN | High Calb2 (9.58) but DG polymorph layer | Eliminated (wrong laminar zone — DG hilus) |
| `2659 TH Prkcd Grin2c Glut_6 [CS20230722_CLUS_2659]` | 0659 TH Prkcd Grin2c Glut_6 | 728 | ⚪ UNCERTAIN | High Calb2 (9.24) but thalamic | Eliminated (thalamic — off-target) |
| `0014 IT EP-CLA Glut_2 [CS20230722_CLUS_0014]` | 0004 IT EP-CLA Glut_2 | 849 | ⚪ UNCERTAIN | Modest Calb2 (0.67); lateral entorhinal | Eliminated (entorhinal layer 6a) |
| `0015 IT EP-CLA Glut_2 [CS20230722_CLUS_0015]` | 0004 IT EP-CLA Glut_2 | 304 | ⚪ UNCERTAIN | Modest Calb2 (1.61); lateral entorhinal | Eliminated (entorhinal layer 6a) |
| `0079 CA3 Glut_5 [CS20230722_SUPT_0079]` | — | 318 | ⚪ UNCERTAIN | Supertype of 0316/0317; CA3/DG hilus | Eliminated (wrong laminar zone — CA3/hilus) |
| `0010 L5/6 IT TPE-ENT Glut_4 [CS20230722_SUPT_0010]` | — | 1791 | ⚪ UNCERTAIN | Calb2 0.59; lateral entorhinal L5 | Eliminated (entorhinal pyramidal — off-target) |
| `0066 ENTmv-PA-COAp Glut_1 [CS20230722_SUPT_0066]` | — | 1528 | ⚪ UNCERTAIN | Calb2 0.36; cortical subplate / posterior amygdala | Eliminated (cortical subplate — off-target) |
| `0099 L5 PPP Glut_1 [CS20230722_SUPT_0099]` | — | 1428 | ⚪ UNCERTAIN | Calb2 0.14; postsubiculum/presubiculum | Eliminated (parahippocampal — off-target) |
| `0085 L2/3 IT PPP Glut_2 [CS20230722_SUPT_0085]` | — | 20603 | ⚪ UNCERTAIN | Calb2 0.47; presubiculum/postsubiculum L2/3 | Eliminated (parahippocampal — off-target) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical node `hpc_calretinin_glu_neuron_hippocampus` carries `definition_basis: CLASSICAL_MULTIMODAL` and defines a glutamatergic neuron whose soma sits in the stratum lacunosum-moleculare / outer molecular layer of the hippocampal formation [UBERON:0002421] [1], [2]. Calb2 (calretinin) is recorded as the defining marker; no negative markers or neuropeptides are encoded.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE95315 (Hochgerner 2018 mouse DG scRNA-seq cell type labels: Granule-mature, Granule-immature, Mossy-Cyp26b1, Mossy-Adcyap1, Mossy-Klk8, Neuroblast 1, Neuroblast 2, Cajal-Retzius, GABA-Cnr1, GABA-Lhx6, Astrocytes) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations). 2 genes unmapped. Per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 2934 (filtered to 2934) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_hpc_calretinin_glu_neuron_hippocampus_to_supt_0135 | ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT | atlas-internal |
| edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_CLUS_0316 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_CLUS_0317 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_CLUS_2659 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_CLUS_0014 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_CLUS_0015 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_SUPT_0079 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_SUPT_0010 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_SUPT_0066 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_SUPT_0099 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_SUPT_0085 | ATLAS_METADATA | PARTIAL | atlas-internal |

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:57+00:00 from [kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

</details>

---

## Discussion

**Primary mapping:** hippocampal calretinin-positive glutamatergic neuron → 0135 HPF CR Glut_1 [CS20230722_SUPT_0135] at LOW confidence. Key support: annotation transfer of an independent mouse hippocampal scRNA-seq dataset (Hochgerner 2018) routes the Cajal-Retzius source cluster cleanly onto SUPT_0135 (F1=0.99 at supertype), and SUPT_0135 is the only WMBv1 glutamatergic supertype whose reference cells co-express Calb2, Reln, and Trp73 in the SLM/OML laminar zone. Key caveats: AMBIGUOUS_MAPPING — the AT source label is "Cajal-Retzius", a developmentally transient population, so SUPT_0135 may not correspond to the adult intrinsic SLM/OML calretinin-positive glutamatergic neurons of the classical description; the supertype carries only n=5 reference cells, limiting confidence regardless of F1.

The Cell Ontology has no specific term for this population; glutamatergic neuron [[CL:0000679](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000679)] is the closest ancestor. Calretinin-positive hippocampal glutamatergic neurons are distinct from calretinin-positive GABAergic interneurons. They span SLM, outer molecular layer, and subicular complex, with local-projecting and long-range subpopulations. CL:0000679 is the broadest accurate mapping; no calretinin-positive glutamatergic-specific CL term exists.

### Proposed experiments and follow-ups

- **Annotation transfer from a Calb2+ adult SLM/OML source dataset** — *Target:* F1 ≥ 0.80 at SUPERTYPE level on WMBv1. *Expected output:* AnnotationTransferEvidence on the SUPT_0135 edge (or on a different supertype if the adult cells do not co-cluster with the Cajal-Retzius cells already mapped). *Resolves:* whether SUPT_0135 is the Cajal-Retzius remnant population or the adult intrinsic glutamatergic neurons of [2] (open question 1). The Hochgerner 2018 (GEO:GSE95315) round mapped a Cajal-Retzius-labelled cluster; this refined round needs a source population validated as adult Calb2+ SLM/OML cells, which the Hochgerner data do not provide.
- **MERFISH soma-position check for SUPT_0135 cells** — *Target:* confirm SLM/OML placement at the laminar resolution available in WMBv1's MERFISH layer. *Expected output:* atlas-query evidence on the SUPT_0135 edge, supporting or refuting the SLM/OML location at single-cell resolution beyond the painted-region rollup already on the edge.
- **Targeted literature trawl for Calb2 (and possible Slc17a8 co-expression) in adult mouse SLM/OML** — *Expected output:* MarkerSource entries anchoring Calb2 (and clarifying whether VGluT3 belongs on the classical node) to primary studies on morphology- or laminar-position-confirmed cells. *Resolves:* the unanchored marker definition flagged in the Concerns section.

### Open questions

1. Is SUPT_0135 a Cajal-Retzius remnant population or does it represent the adult SLM/OML Calb2+/Slc17a8+ glutamatergic neurons described in the literature? ISH validation of Trp73 and Calb2 co-expression in adult SLM/OML would resolve this.
2. Why is Slc17a8 (VGluT3) absent from SUPT_0135 given that SLM glutamatergic neurons are described as VGluT3+? Is VGluT3 expression limited to a subset of Calb2+ SLM cells, or is the classical node definition too broad?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Wheeler et al. 2015, *Hippocampome.org: a knowledge base of neuron types in the rodent hippocampus* | [26402459](https://pubmed.ncbi.nlm.nih.gov/26402459/) | soma location |
| [2] | Ceranik et al. 1997, *A Novel Type of GABAergic Interneuron Connecting the Input and the Output Regions of the Hippocampus* | [9204922](https://pubmed.ncbi.nlm.nih.gov/9204922/) | soma location |

---

<!-- verdict-block-start: edge_hpc_calretinin_glu_neuron_hippocampus_to_supt_0135 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.45
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] MapMyCells annotation transfer of Hochgerner 2018
    (run_ref at_run_20260427_hochgerner2018_dg_mmc_wmbv1) routes the
    Cajal-Retzius source cluster onto CS20230722_SUPT_0135 with F1=0.99
    at supertype and F1=1.00 at cluster CS20230722_CLUS_0497;
    CS20230722_SUPT_0135 is the only WMBv1 HPF Glut supertype localised
    to SLM/OML (region_fraction_100um 0.823) with Calb2 marker_Calb2
    CONSISTENT (1 of 1 markers CONSISTENT). Confidence held at LOW
    because the supertype carries only 5 reference cells and the
    source label is a developmentally transient Cajal-Retzius
    population rather than the adult SLM/OML cells of the classical
    description.
  reconciliation_note: >
    Migration note: this edge previously carried the deprecated
    evidencell:PartialOverlapMatch predicate (auto-rewritten by
    refresh_predicates.py on 2026-05-26). Under the 2026-06 rubric the
    edge fits skos:closeMatch — 1:1 shape with strong AT support and
    documented Cajal-Retzius / adult-population ambiguity rather than
    a cardinality or cross-cutting issue.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        CS20230722_SUPT_0135 reference cells strongly express Reln and
        Trp73 alongside Calb2, consistent with Cajal-Retzius identity.
        Classical Cajal-Retzius cells are developmentally transient
        and may not correspond to the adult SLM/OML
        calretinin-positive glutamatergic neurons of the classical
        literature; the WMBv1 "HPF CR" designation may specifically
        label Cajal-Retzius remnants captured during adult brain
        profiling.
    - caveat_type: OTHER
      description: >
        CS20230722_SUPT_0135 has n=5 WMBv1 reference cells total (1
        per child cluster) — the smallest representation of any HPF
        Glut supertype. Atlas-side expression means (Calb2 marker_Calb2
        CONSISTENT, val 4.86, cohort percentile 0.848) and marker
        comparisons rest on a statistically thin reference set
        regardless of how cleanly the annotation transfer F1 lands.
    - caveat_type: OTHER
      description: >
        Calb2 on the classical node has no primary citation
        (defining_markers entry carries an empty refs list). The
        marker concordance with WMBv1 atlas precomputed expression is
        therefore unanchored on the literature side; curator review
        recommended before treating Calb2 alignment as supporting
        evidence in further mappings.
  proposed_experiments:
    - Annotation transfer from a dataset of validated adult Calb2+
      SLM/OML glutamatergic neurons (i.e. not Cajal-Retzius-labelled)
      against WMBv1 with MapMyCells; target F1 >= 0.80 at SUPERTYPE
      level. Output AnnotationTransferEvidence on this edge; resolves
      open question 1 by distinguishing the Cajal-Retzius and adult
      interpretations of CS20230722_SUPT_0135.
    - Inspect MERFISH soma positions for CS20230722_SUPT_0135 cells
      in WMBv1 to confirm stratum lacunosum-moleculare / outer
      molecular layer placement at single-cell resolution beyond the
      painted-region rollup (region_fraction_100um 0.823 currently on
      the edge).
    - Targeted literature search ("calretinin SLM glutamatergic
      mouse" and "VGluT3 SLM hippocampus") to anchor Calb2 (and
      clarify Slc17a8 status) to a primary study on morphology- or
      laminar-position-confirmed adult cells.
  unresolved_questions:
    - Is CS20230722_SUPT_0135 a Cajal-Retzius remnant population or
      does it represent the adult SLM/OML Calb2+/Slc17a8+
      glutamatergic neurons described in the literature?
    - Why is Slc17a8 (VGluT3) absent from CS20230722_SUPT_0135 given
      that SLM glutamatergic neurons are described as VGluT3+? Is
      VGluT3 expression limited to a subset of Calb2+ SLM cells, or
      is the classical node definition too broad?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_CLUS_0316 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_CLUS_0316 is a CA3 Glut_5 cluster (supertype
    CS20230722_SUPT_0079) whose soma sits in field CA3 / CA3 stratum
    radiatum (region_fraction_100um 1.00 within HPF) but the laminar
    zone is wrong; high Calb2 (val 9.60, cohort percentile 0.978)
    reflects CA3 pyramidal expression and not the SLM/OML
    calretinin-positive glutamatergic population described by the
    classical node.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_CLUS_0317 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_CLUS_0317 (supertype CS20230722_SUPT_0079)
    localises to Dentate gyrus polymorph layer (hilus;
    region_fraction_100um 1.00) — the wrong laminar zone for the
    classical SLM/OML population — despite high Calb2 (val 9.58,
    cohort percentile 0.976). Likely a hilar mossy / CA3-related
    glutamatergic cell rather than the SLM calretinin type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_CLUS_2659 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_2659 (TH Prkcd Grin2c Glut_6) is a
    thalamic cluster (Thalamus / Lateral posterior nucleus dominant;
    region_fraction_100um 0.655 but strict region_fraction only
    0.118, region_evidence SELF) — high Calb2 (val 9.24, cohort
    percentile 0.968) reflects thalamic calretinin expression, not a
    hippocampal cell.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_CLUS_0014 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_CLUS_0014 (supertype CS20230722_SUPT_0004,
    IT EP-CLA Glut_2) localises to lateral entorhinal area, layer 6a
    (region_fraction_100um 0.770) with only modest Calb2 (val 0.67,
    cohort percentile 0.673) — an entorhinal projection cluster
    rather than an SLM/OML hippocampal cell.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_CLUS_0015 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_CLUS_0015 (supertype CS20230722_SUPT_0004,
    IT EP-CLA Glut_2) sits in lateral entorhinal area layer 6a
    (region_fraction_100um 0.698) with modest Calb2 (val 1.61, cohort
    percentile 0.765) — sibling of CS20230722_CLUS_0014 and similarly
    off-target for the SLM/OML hippocampal population.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_SUPT_0079 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0079 (0079 CA3 Glut_5) is the parent
    supertype of CS20230722_CLUS_0316 and CS20230722_CLUS_0317; soma
    in CA3 / DG polymorph layer (region_fraction_100um 0.994). High
    Calb2 (val 9.59, cohort percentile 0.986) reflects CA3-lineage
    expression rather than the classical SLM/OML calretinin
    glutamatergic type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_SUPT_0010 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0010 (0010 L5/6 IT TPE-ENT Glut_4) is
    a lateral entorhinal layer 5 IT supertype (region_fraction_100um
    0.867) with low Calb2 (val 0.59, cohort percentile 0.629) — an
    entorhinal pyramidal population rather than an SLM/OML
    hippocampal cell.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_SUPT_0066 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0066 (0066 ENTmv-PA-COAp Glut_1) sits
    in cortical subplate / posterior amygdalar nucleus
    (region_fraction_100um 0.572, strict region_fraction 0.438,
    region_evidence SELF) with very low Calb2 (val 0.36, cohort
    percentile 0.538) — off-target relative to the hippocampal
    formation.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_SUPT_0099 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0099 (0099 L5 PPP Glut_1) is a
    postsubiculum / presubiculum L5 supertype
    (region_fraction_100um 0.978) with Calb2 essentially absent (val
    0.14, cohort percentile 0.281; marker_Calb2 APPROXIMATE only by
    virtue of cohort ranking) — parahippocampal projection neuron,
    not the SLM/OML calretinin type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_calretinin_glu_neuron_hippocampus_to_CS20230722_SUPT_0085 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0085 (0085 L2/3 IT PPP Glut_2) is a
    large presubiculum/postsubiculum L2/3 IT supertype
    (region_fraction_100um 0.991; 20603 cells) with low Calb2 (val
    0.47, cohort percentile 0.581) — a parahippocampal cortical
    population rather than the SLM/OML calretinin glutamatergic
    neuron.
```
<!-- verdict-block-end -->
