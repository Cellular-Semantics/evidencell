# Radiatum-lacunosum moleculare (R-LM) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

## Introduction

The radiatum-lacunosum moleculare (R-LM) cell is a sparsely described GABAergic interneuron of the hippocampal formation (UBERON:0002421). It was originally identified by Oliva et al. 2000 [2] in GIN transgenic mice as a somatostatin-positive cell with soma at or near the stratum radiatum / stratum lacunosum-moleculare boundary, and was tentatively given a CA1 stratum oriens [UBERON:0014552] soma location on the classical node based on the GIN labelling pattern. The mapping matters because R-LM identity overlaps anatomically and molecularly with several better-characterised CA1 SST+ types (OLM, P-LM, hippocampo-septal, oriens-oriens, LTH), and resolving which transcriptomic supertype — if any — corresponds to R-LM is needed before the classical node can be retained as a distinct type or collapsed into a sibling.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | [1] |
| NT | GABAergic | — |
| Defining markers | Sst | [2] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical literature citation · [1]
  > their transcriptomes were closest to RLMb and Neuroglialform interneurons whose somata are located at the border between the stratum radiatum (sr) and the slm and exhibit short dendrites
  > — Perez et al. 2020, Identification of cell types based on the somatic transcriptome · [1] <!-- quote_key: 224817966_e829ad95 -->
- **Sst marker:** classical literature citation, GIN transgenic labelling in mouse hippocampus · [2]

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

No candidate WMBv1 supertype or cluster is supported as an R-LM mapping by the evidence on the graph; all top-K edges resolve to LOW or UNCERTAIN confidence. Annotation transfer of the Yao 2021 (GSE185862) SMART-Seq v4 *Sst* subclass label onto WMBv1 lands cleanly at the Sst Gaba subclass (F1=0.98; see filtered figure below) but the source label pools every CA1 SST+ interneuron type and cannot resolve to a specific supertype — at the supertype level the same Yao Sst pseudo-source spreads with 0216 Sst Gaba_3 [CS20230722_SUPT_0216] receiving F1=0.49 and 0219 Sst Gaba_6 (n_cells 161, F1=0.76) becoming the dominant single target *(note: SUPT_0219 is not an edge on this graph)*. The strongest classical-literature quote available [1] places the somatically defined RLM-like population at the stratum radiatum / stratum lacunosum-moleculare boundary with transcriptomic proximity to neurogliaform cells, which is inconsistent with both the Sst-defined soma-oriens framing on the classical node and with mapping to a Sst Gaba_3 cluster; this report flags the classical node itself as in need of curator review before any mapping can be committed.

![Filtered AT figure for R-LM cell](figures/f1_for_r_lm_cell_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 (GSE185862) SMART-Seq v4 'Sst' source group (n=273 HIP cells; the only AT label available for an R-LM mapping attempt). Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. With a single source in the figure, Purity is 1.0 at every target by construction at SUBCLASS and below; at SUPERTYPE Purity = 0.96, Coverage = 0.63 to 0219 Sst Gaba_6. F1 at or above 0.5 at a level indicates a clean mapping at that resolution. The Yao 'Sst' label pools morphologically distinct SST+ interneuron types — pooling assessment from `r_lm_cell_hippocampus_pool_candidates.json` finds R-LM indistinguishable on AT from OLM, P-LM, bistratified, hippocampo-septal, oriens-oriens, and LTH at CLASS and SUBCLASS, with markers and NT also non-distinguishing across these labels.*

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · LOW

**Supporting evidence:**
- Sst is consistent on this supertype (mean expression 11.44, cohort percentile 0.905, child-coverage 1.000); the Sst Gaba_3 supertype carries 818 CA1 stratum oriens cells in atlas metadata, matching the classical-node soma location field by the strict count rule (region_fraction_100um: 0.539; strict region_fraction: 0.305).
- Annotation transfer of Yao 2021 (GSE185862) Sst subclass cells onto WMBv1 places 83/273 cells on SUPT_0216 (F1=0.49, purity=1.00) — partial support; the dominant Sst supertype target in the same run is SUPT_0219 Sst Gaba_6 (F1=0.76) *(note: SUPT_0219 is a separate edge in this graph, scored UNCERTAIN due to APPROXIMATE/Field-CA3 location).*

**Marker evidence provenance:**
- *Sst* on the classical node is sourced to Oliva et al. 2000 [2] (GIN transgenic mice). GIN labels a subset of SST+ CA1 INs by GFP expression; the original study did not perform morphological reconstruction of every labelled cell, so the classical-side marker is presence-only and does not by itself identify a single transcriptomic supertype.

**Concerns:**
- AMBIGUOUS_MAPPING: SUPT_0216 is also the primary OLM-cell candidate supertype (annotation transfer of Chrna2-Cre data; see OLM report on this graph). R-LM and OLM cells share SST+ identity and putative stratum oriens soma location and cannot be distinguished at this supertype level from atlas metadata alone.
- SINGLE_STUDY: the R-LM type is described only by Oliva et al. 2000 [2] using GIN transgenic labelling. No subsequent transcriptomic or patch-seq characterisation places R-LM cells on the WMBv1 taxonomy.
- NO_DISCRIMINATING_MARKER: no axon-projection or laminar markers distinguishing R-LM from OLM, P-LM, or bistratified cells are available in the atlas supertype metadata.
- Classical-soma-location vs. literature contradiction: the most specific available literature quote [1] places RLMb-like cells at the stratum radiatum / stratum lacunosum-moleculare boundary, not at stratum oriens; this contradicts the soma-oriens basis for matching SUPT_0216 *(note: requires curator review of the classical node's location field — see Open questions)*.

**What would upgrade confidence:**
- A targeted literature search for "R-LM cell hippocampus" and "radiatum-lacunosum moleculare interneuron transcriptomics" to determine whether (a) any subsequent study has placed R-LM on a transcriptomic taxonomy, or (b) R-LM should be merged with a better-characterised sibling (P-LM, neurogliaform, or LTH).
- A patch-seq dataset with morphologically reconstructed R-LM cells (dendrites at sr/slm border, axon in stratum lacunosum-moleculare) mapped to WMBv1 via cell_type_mapper, expected output AnnotationTransferEvidence reaching F1 at or above 0.80 at CLUSTER level.
- Curator decision on whether to retain R-LM as a distinct classical node or collapse it into an existing sibling on this graph.

### 0768 Sst Gaba_3 [CS20230722_CLUS_0768] · LOW

**Supporting evidence:**
- This cluster is the strongest single-cluster anatomical match within the Sst Gaba_3 supertype to the curator-supplied CA1 stratum oriens [UBERON:0014552] field: region_fraction_100um=0.818, strict region_fraction=0.458 (atlas count 261/319 cells in Field CA1, stratum oriens [MBA:399]).
- Sst is highly expressed (12.70, cohort percentile 0.992; atlas category: NEUROPEPTIDE), consistent with the classical Sst+ definition.

**Marker evidence provenance:**
- *Sst* atlas category is NEUROPEPTIDE on this cluster (an atlas-side neuropeptide annotation; treat presence as informational rather than as a primary discriminator on its own). The high precomputed mean is independent evidence of expression.

**Concerns:**
- This cluster is also the leading R-LM candidate for the OLM mapping on this graph (see OLM report) and for several other CA1 SST+ classical nodes; the pooling analysis confirms R-LM cannot be distinguished from OLM, P-LM, bistratified, hippocampo-septal, oriens-oriens, or LTH at this cluster's level using available source labels.
- The Yao 2021 (GSE185862) Sst subclass annotation transfer does NOT specifically support CLUS_0768 — at supertype level the dominant target is SUPT_0219, and no cluster-level F1 row in the rendered figure metrics highlights CLUS_0768 as a top match for the Sst source label. The cluster's selection here is driven by region overlap and Sst expression, not by AT.
- The classical-side soma location may be wrong (see Concerns in §0216 above and the Perez quote [1]): if R-LM cells actually sit at the sr/slm boundary, a stratum-oriens-dominated cluster like CLUS_0768 is unlikely to be the right target.

**What would upgrade confidence:**
- Resolve the classical-node soma location: re-read Oliva et al. 2000 [2] for soma laminar position, and reconcile with Perez et al. 2020 [1] which places RLMb at the sr/slm border.
- A morphologically targeted patch-seq dataset for sr/slm-border SST+ interneurons mapped to WMBv1 (expected AnnotationTransferEvidence reaching F1 at or above 0.80, CLUSTER level).

### 0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241] · UNCERTAIN

**Supporting evidence:**
- Sst is highly expressed (12.33, cohort percentile 0.984, child-coverage 1.000), consistent with the SST+ classical definition.

**Concerns:**
- AMBIGUOUS_MAPPING (location DISCORDANT): the supertype's painted-anat distribution is dominated by Isocortex [MBA:315] (1377 cells in 100µm window) and lateral/medial forebrain bundle systems; region_fraction_100um=0.021 and strict region_fraction=0.008 at CA1 stratum oriens [MBA:399]. The Sst Chodl long-range projection identity (Chodl+) does not match any reported R-LM feature.
- Location is distant from the classical-type field — `region_fraction_100um: 0.021` is well below the boundary band; stronger counter-evidence than a registration scatter case; the classical type is unlikely to be a CA1 representative of this T-type.

**What would upgrade confidence:**
- This candidate is unlikely to recover R-LM identity; no specific experiment is proposed.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — | 2004 | 🔴 LOW | Region 0.539; Yao Sst F1=0.49 to supertype | Primary (uncertain) |
| 0768 Sst Gaba_3 [CS20230722_CLUS_0768] | 0216 Sst Gaba_3 | 66 | 🔴 LOW | Region 0.818; Sst 12.70 | Secondary (uncertain) |
| 0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241] | — | 2905 | ⚪ UNCERTAIN | Location DISCORDANT (Isocortex) | Eliminated (wrong region) |
| 0772 Sst Gaba_3 [CS20230722_CLUS_0772] | 0216 Sst Gaba_3 | 190 | 🔴 LOW | Region 0.706; Sst 11.92 | Eliminated (no R-LM-specific signal) |
| 0767 Sst Gaba_3 [CS20230722_CLUS_0767] | 0216 Sst Gaba_3 | 104 | 🔴 LOW | Region 0.578; Sst 10.78 | Eliminated (no R-LM-specific signal) |
| 0770 Sst Gaba_3 [CS20230722_CLUS_0770] | 0216 Sst Gaba_3 | 404 | 🔴 LOW | Region 0.506; Sst 10.54 | Eliminated (no R-LM-specific signal) |
| 0773 Sst Gaba_3 [CS20230722_CLUS_0773] | 0216 Sst Gaba_3 | 156 | 🔴 LOW | Region 0.648; Sst 11.43 | Eliminated (no R-LM-specific signal) |
| 0226 Sst Gaba_13 [CS20230722_SUPT_0226] | — | 4064 | ⚪ UNCERTAIN | Location DISCORDANT (Isocortex) | Eliminated (wrong region) |
| 1164 Astro-TE NN_4 [CS20230722_SUPT_1164] | — | 982 | 🔴 REFUTED | Sst 0.80 (not a neuron) | Eliminated (non-neuronal supertype) |
| 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | — | 725 | ⚪ UNCERTAIN | Region APPROXIMATE (CA3); Sst 10.17 | Eliminated (CA3-dominant; off-target) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The R-LM (radiatum-lacunosum moleculare) cell on this graph is a CLASSICAL_MULTIMODAL stub described originally by Oliva et al. 2000 [2] using GIN transgenic mice. Defining marker: Sst (single defining marker, no negative markers, no neuropeptide list). NT type: GABAergic (no primary citation on the node). Soma location: CA1 stratum oriens [UBERON:0014552] (location ref [1]). The classical node carries an explicit THIN EVIDENCE note flagging that this type may not be transcriptomically separable from OLM or P-LM cells.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match against CA1 stratum oriens [MBA:399], NT type=GABAergic, defining marker Sst). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Sst — Yao 2021 SMART-Seq v4 hippocampal formation, n=273 HIP cells under the Sst subclass label) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |
| Caveats | The Yao 'Sst' label pools every CA1 SST+ interneuron type (OLM, bistratified, hippocampo-septal, oriens-oriens, R-LM, P-LM, LTH) and does NOT resolve to any specific classical type at supertype or cluster level. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:41+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_r_lm_cell_hippocampus_to_CS20230722_CLUS_0768 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_r_lm_cell_hippocampus_to_CS20230722_CLUS_0772 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_r_lm_cell_hippocampus_to_CS20230722_CLUS_0767 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_r_lm_cell_hippocampus_to_CS20230722_CLUS_0770 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_r_lm_cell_hippocampus_to_CS20230722_CLUS_0773 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0241 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0226 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_1164 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** R-LM cell → 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at LOW confidence. Key support: Sst expression CONSISTENT (mean 11.44, cohort percentile 0.905) and CA1 stratum oriens overlap (region_fraction_100um: 0.539); partial annotation transfer of the Yao 2021 Sst subclass label (F1=0.49 to the supertype). Key caveats: AMBIGUOUS_MAPPING (same supertype is the primary OLM candidate; pooling assessment shows R-LM is not distinguished from OLM, P-LM, bistratified, hippocampo-septal, oriens-oriens, or LTH on the available data) and SINGLE_STUDY (R-LM is described only by Oliva et al. 2000 [2], without transcriptomic characterisation).

The strongest available literature quote [1] additionally argues that an RLMb-like population's transcriptome is closest to neurogliaform interneurons rather than to a canonical SST+ supertype, and places the soma at the sr/slm border rather than in stratum oriens — directly conflicting with the basis for matching any Sst Gaba_3 cluster. The honest reading is therefore that no transcriptomic distinction between R-LM and the better-characterised CA1 SST+ siblings is achievable on this graph's evidence, and the curator should consider whether to (a) retain R-LM as a distinct classical node pending targeted literature work, (b) collapse it into a sibling (OLM, P-LM, neurogliaform, or LTH), or (c) revise its soma location field to the sr/slm boundary and re-run map-cell-type.

No Cell Ontology term currently assigned. Candidate for CL contribution only after the classical-node identity is resolved.

### Proposed experiments and follow-ups

- **Targeted literature trawl** — search PubMed and primary sources for "radiatum-lacunosum moleculare cell", "R-LM interneuron hippocampus", and the Oliva 2000 GIN line follow-ups, to determine whether R-LM has been re-examined with morphological reconstruction + scRNA-seq or patch-seq since the original description. **Expected output:** LiteratureEvidence updates on the classical node, possibly a node-merge proposal. **Resolves:** open questions 1 and 2.
- **Patch-seq mapping** of morphologically reconstructed R-LM cells (sr/slm-border SST+ interneurons with axon in stratum lacunosum-moleculare) onto WMBv1 via cell_type_mapper. **Target:** F1 at or above 0.80 at CLUSTER level. **Expected output:** AnnotationTransferEvidence specific to R-LM (not via the Yao Sst pool). **Resolves:** open question 1 (assigns R-LM to a single cluster) and open question 2 (distinguishes R-LM from OLM/P-LM).
- **Curator review of classical-node soma location** — reconcile the current `CA1 stratum oriens [UBERON:0014552]` field with Perez et al. 2020 [1] sr/slm-border placement and Oliva et al. 2000 [2] original GIN description; revise the classical node if appropriate and re-run map-cell-type.

### Open questions

1. Is R-LM a transcriptomically separable type within the Sst Gaba_3 supertype, or should it be collapsed into OLM, P-LM, or a neurogliaform sibling?
2. Does R-LM cell soma sit in stratum oriens (per current classical-node assertion) or at the stratum radiatum / stratum lacunosum-moleculare boundary (per Perez et al. 2020 [1])?
3. Is the Yao 2021 'Sst' SMART-Seq v4 subclass label the only AT source available for an R-LM mapping? A morphologically targeted source (e.g. GIN-line patch-seq) would resolve the pooling problem.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500) | soma location |
| [2] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798) | Sst marker |

---

<!-- verdict-block-start: edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  relationship: evidencell:UncertainRelationship
  rationale: "[tier:STRONGEST] Sst CONSISTENT on CS20230722_SUPT_0216 (mean 11.44, cohort percentile 0.905) and CA1 stratum oriens proximity (region_fraction_100um: 0.539; strict region_fraction: 0.305) align with the classical-node fields, and transcriptomic annotation transfer of the Yao 2021 Sst subclass label onto WMBv1 places 83/273 source cells on this supertype as a partial match (parent-subclass Sst Gaba alignment is clean, with subclass-level F1=0.98 in at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1). However, the Yao Sst label pools every CA1 SST+ interneuron type and cannot resolve R-LM specifically; the same supertype is the primary OLM candidate on this graph; and the strongest classical-literature quote available (Perez et al. 2020 PMID:33404500) places an RLMb-like population at the stratum radiatum / stratum lacunosum-moleculare boundary with transcriptomic proximity to neurogliaform cells, not to a Sst Gaba_3 supertype. 1 of 1 markers CONSISTENT but R-LM-specific support is absent."
  reconciliation_note: "R-LM cannot be distinguished from OLM, P-LM, bistratified, hippocampo-septal, oriens-oriens, or LTH on transcriptomic annotation transfer at CLASS or SUBCLASS using the Yao 2021 Sst source label (pool_candidates report). Panels markers and nt are also non-distinguishing across these sibling classical nodes; CASE B (transcriptomic-only indistinguishability — other panels not assessed in available evidence)."
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: "CS20230722_SUPT_0216 is also the primary OLM-cell candidate supertype on this graph; R-LM and OLM share SST+ identity and putative stratum oriens soma location and cannot be distinguished at this supertype level from atlas metadata alone."
    - caveat_type: SINGLE_STUDY
      description: "R-LM type is described only by Oliva et al. 2000 (PMID:10777798) using GIN transgenic mice, without subsequent transcriptomic characterisation placing R-LM cells on the WMBv1 taxonomy."
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: "No axon-projection or laminar markers distinguishing R-LM from OLM, P-LM, or bistratified cells are available in the atlas supertype metadata for CS20230722_SUPT_0216."
    - caveat_type: OTHER
      description: "Perez et al. 2020 (PMID:33404500) places an RLMb-like population at the stratum radiatum / stratum lacunosum-moleculare boundary with transcriptomic proximity to neurogliaform cells, contradicting the basis for matching CS20230722_SUPT_0216 via stratum-oriens soma and Sst Gaba_3 identity."
  proposed_experiments:
    - "Single-cell transcriptomic profiling paired with anatomical reconstruction of R-LM cells (sr/slm-border SST+ interneurons with axon in stratum lacunosum-moleculare), mapped to WMBv1 via cell_type_mapper; target F1 at or above 0.80 at CLUSTER level; expected output AnnotationTransferEvidence specific to R-LM."
    - "Targeted literature search for R-LM transcriptomic characterisation since Oliva et al. 2000 to determine whether R-LM should be retained, merged with a sibling (OLM, P-LM, neurogliaform, LTH), or revised in its soma location field."
  unresolved_questions:
    - "Is R-LM transcriptomically separable from OLM, P-LM, bistratified, hippocampo-septal, oriens-oriens, or LTH on WMBv1, or should it be collapsed into one of these siblings?"
    - "Does R-LM soma sit in stratum oriens (current classical-node field) or at the stratum radiatum / stratum lacunosum-moleculare boundary (Perez et al. 2020 PMID:33404500)?"
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_r_lm_cell_hippocampus_to_CS20230722_CLUS_0768 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  relationship: evidencell:UncertainRelationship
  rationale: "[tier:NEXT] CS20230722_CLUS_0768 is the strongest single-cluster anatomical match within the Sst Gaba_3 supertype to CA1 stratum oriens (region_fraction_100um: 0.818; strict region_fraction: 0.458) and shows high Sst (mean 12.70, cohort percentile 0.992). However, no R-LM-specific evidence selects this cluster over its Sst Gaba_3 siblings, and the same cluster is the leading candidate for the OLM mapping on this graph; R-LM cannot be distinguished from OLM at this cluster level. 1 of 1 markers CONSISTENT."
  reconciliation_note: "Paired with CS20230722_SUPT_0216 in this report; R-LM is indistinguishable from OLM at CS20230722_CLUS_0768 on available evidence."
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: "CS20230722_CLUS_0768 is the leading R-LM candidate for the OLM mapping on this graph and for several other CA1 SST+ classical nodes; no atlas-metadata feature distinguishes R-LM from these siblings at cluster level."
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: "No R-LM-specific marker (laminar position, axon target, transcript signature) is available to select CS20230722_CLUS_0768 over its Sst Gaba_3 siblings (CS20230722_CLUS_0767, CS20230722_CLUS_0770, CS20230722_CLUS_0772, CS20230722_CLUS_0773)."
    - caveat_type: OTHER
      description: "Perez et al. 2020 (PMID:33404500) places an RLMb-like population at the stratum radiatum / stratum lacunosum-moleculare boundary with transcriptomic proximity to neurogliaform cells, which is inconsistent with selecting a stratum-oriens-dominated Sst Gaba_3 cluster."
  proposed_experiments:
    - "Single-cell transcriptomic profiling paired with anatomical reconstruction of R-LM cells mapped to WMBv1 via cell_type_mapper; target F1 at or above 0.80 at CLUSTER level on CS20230722_CLUS_0768 or a sibling."
  unresolved_questions:
    - "Is R-LM identifiable at cluster level on WMBv1, or only at subclass (Sst Gaba) and not below?"
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_r_lm_cell_hippocampus_to_CS20230722_CLUS_0772 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.20
  relationship: evidencell:UncertainRelationship
  rationale: "[tier:CUT] CS20230722_CLUS_0772 has CA1 stratum oriens overlap (region_fraction_100um: 0.706) and high Sst (mean 11.92, cohort percentile 0.958) but no R-LM-specific signal selects it over its Sst Gaba_3 siblings; eliminated as no R-LM-specific evidence is available at cluster level."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_r_lm_cell_hippocampus_to_CS20230722_CLUS_0767 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.20
  relationship: evidencell:UncertainRelationship
  rationale: "[tier:CUT] CS20230722_CLUS_0767 has CA1 stratum oriens overlap (region_fraction_100um: 0.578) and Sst expression (mean 10.78, cohort percentile 0.832) but no R-LM-specific evidence selects it over sibling Sst Gaba_3 clusters; eliminated."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_r_lm_cell_hippocampus_to_CS20230722_CLUS_0770 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.20
  relationship: evidencell:UncertainRelationship
  rationale: "[tier:CUT] CS20230722_CLUS_0770 has CA1 stratum oriens overlap (region_fraction_100um: 0.506) and Sst expression (mean 10.54, cohort percentile 0.807) but no R-LM-specific evidence selects it over sibling Sst Gaba_3 clusters; eliminated."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_r_lm_cell_hippocampus_to_CS20230722_CLUS_0773 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.20
  relationship: evidencell:UncertainRelationship
  rationale: "[tier:CUT] CS20230722_CLUS_0773 has CA1 stratum oriens overlap (region_fraction_100um: 0.648) and Sst expression (mean 11.43, cohort percentile 0.908) but no R-LM-specific evidence selects it over sibling Sst Gaba_3 clusters; eliminated."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0241 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  relationship: evidencell:UncertainRelationship
  rationale: "[tier:CUT] CS20230722_SUPT_0241 (Sst Chodl Gaba_4) shows location DISCORDANT (region_fraction_100um: 0.021; strict region_fraction: 0.008; Isocortex- and forebrain-bundle-dominant distribution) and a Sst Chodl long-range projection identity incompatible with reported R-LM features; eliminated as wrong region and wrong functional class."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0226 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  relationship: evidencell:UncertainRelationship
  rationale: "[tier:CUT] CS20230722_SUPT_0226 (Sst Gaba_13) shows location DISCORDANT (region_fraction_100um: 0.016; strict region_fraction: 0.008; Isocortex- and cortical-subplate-dominant); eliminated as wrong region."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_1164 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.02
  relationship: evidencell:NoCorrespondence
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: "[tier:CUT] CS20230722_SUPT_1164 (Astro-TE NN_4) is a non-neuronal supertype with Sst at mean 0.80 (cohort percentile 0.333); eliminated as non-neuronal and Sst-non-expressing relative to the SST+ classical R-LM definition."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0219 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.20
  relationship: evidencell:UncertainRelationship
  rationale: "[tier:CUT] CS20230722_SUPT_0219 (Sst Gaba_6) painted-anat distribution is Field CA3-dominant (region_fraction_100um: 0.132; strict region_fraction: 0.061 at CA1 stratum oriens); Sst is present (mean 10.17). Not selectable as an R-LM target given the off-target CA3-dominance and the absence of any R-LM-specific source label."
```
<!-- verdict-block-end -->
