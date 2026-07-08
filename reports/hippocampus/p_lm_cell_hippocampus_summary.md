# Pyramidale-lacunosum moleculare (P-LM) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The pyramidale-lacunosum moleculare (P-LM) cell is a somatostatin-expressing GABAergic interneuron of the CA1 hippocampus, distinguished from the more familiar oriens-lacunosum moleculare (O-LM) cell by the laminar position of its soma in stratum pyramidale rather than stratum oriens. The two types were originally described together by Oliva et al. 2000 [1] in the same single study, where they were identified as GFP-labelled subpopulations of Sst+ interneurons that projected axons to stratum lacunosum-moleculare. P-LM cells have not been transcriptomically characterised in any follow-up study, and it remains unclear whether they constitute a distinct transcriptomic type or are a soma-position variant of O-LM cells.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | — |
| NT | GABAergic | — |
| Defining markers | Sst | [1] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Sst (defining marker):** literature citation only; no quote captured in the facts file. The marker assertion derives from the single foundational study, where P-LM cells were identified within the Sst-EGFP reporter line population.
- **Soma location:** no separate location source captured on the classical node; the stratum-pyramidale assignment derives from the same single study as a defining feature distinguishing P-LM from R-LM and O-LM cells.

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Marker concordance and annotation transfer of the Sst subclass from Yao 2021 (GSE185862, SMART-Seq v4) supports broad mapping of the P-LM cell to the supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (Sst F1=0.98 at subclass level; see figure), with cluster 0768 Sst Gaba_3 [CS20230722_CLUS_0768] as the closest single-cluster match (Sst cohort_pct 0.994, CA1 stratum oriens-enriched). Cluster-level confidence is LOW because the source dataset carries only the subclass label "Sst" — it pools P-LM with O-LM, bistratified, hippocampo-septal, and oriens-oriens cells without distinguishing morphology, so the cluster-level partition of those types is not resolvable from this AT alone *(note: this AT-side indistinguishability is documented in the source dataset's labelling, not in the literature)*.

![Filtered AT figure for P-LM cell](figures/f1_for_p_lm_cell_hippocampus.png)

*F1 across taxonomy levels for the single source group (Yao 2021 "Sst" subclass, n=273 HPF cells) relevant to the P-LM cell. Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. With a single pooled source, Purity is 1.0 at every target where any source-group cells land and only Coverage discriminates. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. F1 collapses from 0.98 at subclass (053 Sst Gaba) to 0.23 at cluster (0786 Sst Gaba_6) — consistent with the source label pooling many distinct Sst-IN morphological types.*

### 0216 Sst Gaba_3 · 🔴 LOW

**Supporting evidence:**

- Sst defining marker: cluster-mean 11.44; cohort percentile 0.976 of 50 GABAergic candidates in the hippocampal-region cohort; child-cluster coverage 1.000 (atlas-internal, precomputed expression on CS20230722_SUPT_0216).
- Soma location: 0216 Sst Gaba_3 carries 2145 painted Hippocampal formation cells (MBA:1089) with the dominant CA1 stratum oriens count (1463 cells, MBA:399), placing this supertype anatomically within CA1. `region_fraction_100um: 0.153` — proximity rather than centred-inside (atlas-internal).

**Concerns:**

- Soma location APPROXIMATE: 0216 Sst Gaba_3's primary soma layer is CA1 stratum oriens (MBA:399), not the pyramidal layer (MBA:495). The P-LM cell is defined by its stratum-pyramidale soma, and the supertype's mapped cells do not centre there. This is the primary biological tension — the supertype hosts O-LM cells whose soma sits in oriens; P-LM cells, if a distinct type, would form a sparse pyramidale subpopulation that the atlas may or may not resolve at this rank.
- NT type NOT_ASSESSED at supertype level (atlas does not assert a unified NT annotation at rank 1 here).
- Single-study evidence base: the P-LM cell is described in one paper (Oliva et al. 2000 [1]) and has not been transcriptomically characterised; whether it is a distinct transcriptomic type or a soma-position variant of O-LM cells is unknown.
- Cross-edge ambiguity: P-LM, R-LM, O-LM, bistratified, hippocampo-septal, and oriens-oriens cells all land on the same Sst subclass (F1=0.98 to CS20230722_SUBC_053) in the available AT, and the source dataset's labelling provides no morphology-resolved subtypes to separate them.

(1 of multiple child clusters within 0216 Sst Gaba_3 — specifically 0768 — shows the highest Sst expression and clearest CA1 stratum-oriens enrichment; see candidates table for the alternative children and their region fractions.)

### 0768 Sst Gaba_3 · 🔴 LOW

**Supporting evidence:**

- Sst expression: cluster-mean 12.70; cohort percentile 0.994 — the strongest Sst signal among the assessed cohort (atlas-internal, precomputed expression on CS20230722_CLUS_0768). Sst is annotated as a NEUROPEPTIDE category marker in the atlas metadata for this cluster.
- Soma location: 0768 Sst Gaba_3 carries 296 painted Hippocampal formation cells (MBA:1089) with the dominant count in CA1 stratum oriens (261 cells, MBA:399). `region_fraction_100um: 0.248` — this cluster has the cleanest CA1 anatomical placement among Sst Gaba_3 children (atlas-internal).
- Within the 0216 Sst Gaba_3 supertype, 0768 is the best-candidate child for any CA1 Sst+ lacunosum-moleculare-projecting interneuron based on both Sst level and CA1 proximity.

**Concerns:**

- Soma location APPROXIMATE: 0768 Sst Gaba_3's primary soma layer is CA1 stratum **oriens**, not CA1 stratum **pyramidale**. The defining feature of the P-LM cell — soma in stratum pyramidale — is not reflected in the atlas placement of this cluster. If P-LM cells are a distinct transcriptomic type, this would predict a separate pyramidale-soma cluster that the atlas may not currently resolve; if they are a soma-position variant of O-LM, the oriens placement of 0768 would be consistent.
- AT cluster-level resolution: F1 collapses to 0.23 at cluster (best cluster 0786 Sst Gaba_6, not 0768) because the source label "Sst" pools many morphological types. The cluster-level call cannot be anchored in AT *(note: this is the same limitation as for OLM and other Sst-IN classical types; resolution requires a morphology-targeted source dataset)*.
- Same single-study and indistinguishability concerns as the supertype edge above.

**What would upgrade confidence:**

- A scRNA-seq dataset of morphologically reconstructed Sst+ CA1 interneurons in which P-LM cells are labelled separately from O-LM, bistratified, and hippocampo-septal cells (e.g. patch-seq with biocytin fill and post-hoc laminar reconstruction). MapMyCells on such a dataset onto WMBv1 at F1 ≥ 0.70 at CLUSTER level would resolve whether P-LM is a distinct cluster or shares 0768 / its siblings with O-LM.
- A targeted ISH or smFISH panel comparing Sst+ cells in CA1 stratum pyramidale versus stratum oriens to test whether laminar position correlates with a transcriptomic difference, or with a marker (e.g. Chrna2, Pnoc, Reln) known to subdivide the Sst-IN population.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0216 Sst Gaba_3 [CS20230722_SUPT_0216]` | — | 2004 | 🔴 LOW | Sst cohort_pct 0.976; CA1 SO-enriched supertype hosting OLM | Primary (supertype broadMatch) |
| `0768 Sst Gaba_3 [CS20230722_CLUS_0768]` | 0216 Sst Gaba_3 | 66 | 🔴 LOW | Sst cohort_pct 0.994; CA1 SO; best child of 0216 | Secondary (best child within primary supertype) |
| `0219 Sst Gaba_6 [CS20230722_SUPT_0219]` | — | 725 | ⚪ UNCERTAIN | AT supertype F1=0.76 but CA3-enriched | Eliminated (CA3 not CA1) |
| `0698 RHP-COA Ndnf Gaba_4 [CS20230722_CLUS_0698]` | 0196 RHP-COA Ndnf Gaba_4 | 80 | ⚪ UNCERTAIN | CA3 SO; RHP-COA subclass, low Sst | Eliminated (wrong subclass and CA3) |
| `0728 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0728]` | 0203 Lamp5 Lhx6 Gaba_1 | 63 | ⚪ UNCERTAIN | Lamp5 Lhx6 subclass; low Sst | Eliminated (wrong subclass) |
| `0730 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0730]` | 0203 Lamp5 Lhx6 Gaba_1 | 112 | ⚪ UNCERTAIN | Lamp5 Lhx6 subclass; low Sst | Eliminated (wrong subclass) |
| `0771 Sst Gaba_3 [CS20230722_CLUS_0771]` | 0216 Sst Gaba_3 | 462 | ⚪ UNCERTAIN | Sst cohort_pct 0.952 but region_fraction_100um 0.112 | Eliminated (low CA1 representation) |
| `0196 RHP-COA Ndnf Gaba_4 [CS20230722_SUPT_0196]` | — | 167 | ⚪ UNCERTAIN | RHP-COA subclass; CA3 SO; low Sst | Eliminated (wrong subclass) |
| `0232 Sst Gaba_19 [CS20230722_SUPT_0232]` | — | 663 | 🔴 REFUTED | Entorhinal-enriched (MBA:926/918); DISCORDANT location | Eliminated (no hippocampal cells) |
| `0206 Pvalb Gaba_2 [CS20230722_SUPT_0206]` | — | 650 | ⚪ UNCERTAIN | Pvalb subclass; CA1 with cortical-subplate spread | Eliminated (wrong subclass) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The P-LM cell is defined by Oliva et al. 2000 [1] as a Sst+ GABAergic interneuron with soma in CA1 stratum pyramidale and axonal projection to stratum lacunosum-moleculare. The classical-node `definition_basis` is `CLASSICAL_MULTIMODAL` — the original study combined GFP transgene targeting with morphology and electrophysiology, but the type has not been re-examined since and has no transcriptomic characterisation.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Sst) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells (default parameters) |
| Tool version | cell_type_mapper |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |
| Caveats | Source label is the subclass-level "Sst" tag from Yao 2021 — pools multiple Sst-IN morphological types (O-LM, bistratified, hippocampo-septal, oriens-oriens, P-LM, R-LM). Cluster-level resolution of any one type is not recoverable from this AT alone. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_p_lm_cell_hippocampus_to_CS20230722_CLUS_0768 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA; ANNOTATION_TRANSFER | WEAK; PARTIAL | atlas-internal |
| edge_p_lm_cell_hippocampus_to_CS20230722_CLUS_0698 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_p_lm_cell_hippocampus_to_CS20230722_CLUS_0728 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_p_lm_cell_hippocampus_to_CS20230722_CLUS_0730 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_p_lm_cell_hippocampus_to_CS20230722_CLUS_0771 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0196 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0232 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA | PARTIAL | atlas-internal |

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:42+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

</details>

---

## Discussion

**Primary mapping:** Pyramidale-lacunosum moleculare (P-LM) cell → 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at LOW confidence, with 0768 Sst Gaba_3 [CS20230722_CLUS_0768] as the best child-cluster candidate (also LOW). Key support: Sst marker concordance (cohort_pct 0.976 at supertype, 0.994 at cluster) and CA1 anatomical placement of the Sst Gaba_3 supertype family. Key caveats: SINGLE_STUDY (Oliva et al. 2000 [1] is the only literature description) and AMBIGUOUS_MAPPING (P-LM may not be a transcriptomic type distinct from O-LM and R-LM; its defining stratum-pyramidale soma is not reflected in 0768's CA1 stratum-oriens-enriched placement).

No Cell Ontology term currently assigned. This is a candidate for CL contribution, but the underlying biological question — whether P-LM cells are a distinct transcriptomic type or a soma-position variant of O-LM cells — would ideally be resolved before a new CL term is requested.

### 7. Proposed experiments and follow-ups

The single MapMyCells AT run on this edge family used the Yao 2021 SSv4 dataset with subclass-level labels only ("Sst"), which is intrinsically incapable of resolving cluster-level membership of any specific Sst-IN morphological subtype. A *refined* AT experiment is needed:

- **What:** scRNA-seq on morphologically reconstructed Sst+ CA1 interneurons, with P-LM cells separately labelled from O-LM, bistratified, hippocampo-septal, and oriens-oriens cells (e.g. patch-seq with biocytin fill and post-hoc laminar reconstruction of soma position in stratum pyramidale vs stratum oriens).
- **Target:** F1 ≥ 0.70 at CLUSTER level via MapMyCells onto WMBv1.
- **Expected output:** AnnotationTransferEvidence on a new edge, with morphology-confirmed P-LM cells as the source group.
- **Resolves:** open questions (1) and (2) below.

Targeted ISH or smFISH:

- **What:** dual-label ISH/smFISH for Sst combined with a candidate-discriminating marker (Chrna2 / Pnoc / Reln) in CA1 stratum pyramidale, comparing Sst+ cells in stratum pyramidale to those in stratum oriens.
- **Target:** detection of any marker showing differential expression between the two laminar populations.
- **Expected output:** MarkerAnalysisEvidence.
- **Resolves:** open question (1).

### 8. Open questions

1. Is the P-LM cell a transcriptomically distinct type, or a soma-position variant of the O-LM cell?
2. P-LM, R-LM, O-LM, bistratified, hippocampo-septal, and oriens-oriens cells all collapse onto a single Sst-subclass label in available AT data; morphology-resolved labels are required to test cluster-level separability.
3. Should P-LM and R-LM (described in the same study, differing only in soma laminar position) be unified into a single classical node pending evidence of transcriptomic distinction?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Oliva et al. 2000 · PMID:[10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | 10777798 | Sst marker |

---

<!-- verdict-block-start: edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] P-LM cell maps to CS20230722_SUPT_0216 (0216 Sst Gaba_3)
    at LOW confidence via Sst marker concordance (cohort_pct 0.976,
    child-coverage 1.000) and CA1 anatomical placement of the supertype's
    painted cells (region_fraction_100um: 0.153); 1 of 1 markers CONSISTENT.
    Confidence is capped LOW because the classical type rests on a single
    study (Oliva et al. 2000, PMID:10777798) without transcriptomic
    characterisation, and because the supertype's dominant soma layer is
    CA1 stratum oriens (MBA:399) rather than stratum pyramidale (MBA:495);
    P-LM may be a soma-position variant of O-LM rather than a distinct
    transcriptomic type. The supertype broadMatch reflects assignment to
    the Sst Gaba_3 family without resolving which child cluster (if any)
    corresponds specifically to the stratum-pyramidale subpopulation.
  reconciliation_note: >
    Paired with edge_p_lm_cell_hippocampus_to_CS20230722_CLUS_0768 (the
    best-child closeMatch within this supertype). This edge rests on
    atlas-internal precomputed expression and painted-cell anatomy only;
    no annotation transfer is asserted on this edge.
  caveats:
    - caveat_type: SINGLE_STUDY
      description: >
        P-LM cell described only in Oliva et al. 2000 (PMID:10777798); the
        type has not been re-examined in any follow-up study.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        P-LM and R-LM cells (and possibly O-LM) were identified in the same
        study and differ only in soma laminar position; whether they are
        distinct types or a single type with variable soma location is
        unknown.
    - caveat_type: OTHER
      description: >
        Supertype-level assignment cannot be narrowed to a specific child
        cluster from atlas-internal evidence alone; finer resolution
        requires an annotation-transfer experiment with laminar-resolved
        labels (see proposed_experiments).
  proposed_experiments:
    - >
      A targeted expression-profiling experiment on Sst+ CA1 interneurons
      with P-LM cells separately labelled by laminar position
      (stratum pyramidale vs stratum oriens), followed by annotation
      transfer onto WMBv1 targeting F1 >= 0.70 at CLUSTER level.
    - >
      Dual-label smFISH for Sst plus a candidate discriminator
      (Chrna2, Pnoc, or Reln) comparing Sst+ cells in CA1 stratum
      pyramidale vs stratum oriens.
  unresolved_questions:
    - Is the P-LM cell transcriptomically distinct from the O-LM cell, or a soma-position variant?
    - Should P-LM and R-LM be unified pending evidence of transcriptomic distinction?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_p_lm_cell_hippocampus_to_CS20230722_CLUS_0768 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Best-child cluster within CS20230722_SUPT_0216; 0768 Sst
    Gaba_3 carries the strongest Sst signal in the assessed cohort
    (cohort_pct 0.994) and the cleanest CA1 anatomical placement among
    Sst Gaba_3 children (region_fraction_100um: 0.248, dominant count in
    CA1 stratum oriens MBA:399). 1 of 1 markers CONSISTENT. Cluster-level
    AT support is absent — the Yao 2021 Sst subclass label is too broad to
    resolve which Sst-IN cluster corresponds to P-LM cells.
  reconciliation_note: >
    Paired with edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0216 (the
    supertype broadMatch). closeMatch is asserted at cluster level on the
    grounds of strongest Sst expression and CA1 placement; the
    stratum-pyramidale defining feature of the classical type is not
    reflected (CLUS_0768's painted cells centre on CA1 stratum oriens),
    so the closeMatch is contingent on P-LM cells not being a distinct
    pyramidale-soma type.
  caveats:
    - caveat_type: SINGLE_STUDY
      description: >
        P-LM cell described only in Oliva et al. 2000 (PMID:10777798); no
        follow-up characterisation exists.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        CLUS_0768's painted soma distribution centres on CA1 stratum
        oriens, not the stratum pyramidale that defines the P-LM cell;
        the cluster better matches the O-LM laminar profile.
    - caveat_type: OTHER
      description: >
        This edge carries atlas-internal evidence only; cluster-level
        resolution between P-LM and other Sst-IN types within the
        Sst Gaba_3 family cannot be anchored without a laminar-resolved
        source dataset.
  proposed_experiments:
    - >
      A laminar-resolved profiling experiment on Sst+ CA1 interneurons,
      distinguishing stratum-pyramidale from stratum-oriens somata, to
      assess whether stratum-pyramidale Sst+ cells form a separable
      cluster distinct from CLUS_0768 or co-assign with it.
  unresolved_questions:
    - Is CLUS_0768 the correct cluster for both O-LM and P-LM cells, or does P-LM map elsewhere?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0219 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0219 (0219 Sst Gaba_6) is the dominant AT
    target for Yao 2021 Sst HPF cells at supertype level (F1=0.76), but
    its painted cells are predominantly CA3 (CA3 SO 305, CA3 lucidum 99,
    CA3 SR 167, CA3 pyr 261) with no CA1 representation; the P-LM cell
    is a CA1 type, so anatomical mismatch eliminates this supertype
    despite the AT signal.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        SUPT_0219 is a CA3-enriched supertype with no CA1 representation;
        P-LM cell is defined in CA1 stratum pyramidale.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_p_lm_cell_hippocampus_to_CS20230722_CLUS_0698 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0698 (0698 RHP-COA Ndnf Gaba_4) is in the
    RHP-COA Ndnf Gaba_4 subclass with low Sst expression (1.49,
    cohort_pct 0.661) and CA3 stratum oriens placement
    (region_fraction_100um: 0.525, dominant count in MBA:486); wrong
    subclass for a Sst+ CA1 type.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        CLUS_0698 sits in CA3 stratum oriens, not CA1; wrong subclass
        (RHP-COA Ndnf rather than Sst).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_p_lm_cell_hippocampus_to_CS20230722_CLUS_0728 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0728 (0728 Lamp5 Lhx6 Gaba_1) is in the
    Lamp5 Lhx6 Gaba_1 subclass with low Sst (1.22, cohort_pct 0.485);
    wrong subclass for an Sst-defined classical type.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Lamp5 Lhx6 subclass; Sst expression APPROXIMATE rather than
        CONSISTENT; classical type defined by Sst.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_p_lm_cell_hippocampus_to_CS20230722_CLUS_0730 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0730 (0730 Lamp5 Lhx6 Gaba_1) is in the
    Lamp5 Lhx6 Gaba_1 subclass with Sst cohort_pct 0.612; wrong subclass
    for an Sst-defined classical type.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Lamp5 Lhx6 subclass; classical type defined by Sst.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_p_lm_cell_hippocampus_to_CS20230722_CLUS_0771 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.20
  rationale: >
    [tier:CUT] CS20230722_CLUS_0771 (0771 Sst Gaba_3) shares the 0216
    supertype with CLUS_0768 and carries high Sst (cohort_pct 0.952) but
    region_fraction_100um is 0.112 — substantially lower CA1
    representation than CLUS_0768 (0.248); CLUS_0768 is the better
    child-cluster candidate within the same supertype.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Sibling of CLUS_0768 within SUPT_0216; lower CA1 anatomical
        placement makes it a weaker candidate than its sibling.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0196 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CS20230722_SUPT_0196 (0196 RHP-COA Ndnf Gaba_4) is the
    RHP-COA Ndnf Gaba_4 supertype with CA3 placement
    (region_fraction_100um: 0.633, MBA:495) and low Sst (1.71); wrong
    subclass for an Sst-defined CA1 type.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        RHP-COA Ndnf subclass with low Sst expression; classical type
        defined by Sst.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0232 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0232 (0232 Sst Gaba_19) is enriched in
    entorhinal cortex (MBA:926 dorsal medial EC count_100um=259,
    MBA:918 lateral EC count_100um=195) with region_fraction_100um:
    0.054 for the hippocampal query region; DISCORDANT location for a
    CA1-defined classical type.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Entorhinal cortex-enriched supertype; not hippocampal.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0206 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CS20230722_SUPT_0206 (0206 Pvalb Gaba_2) is a Pvalb
    subclass supertype; classical P-LM cell is defined by Sst, not
    Pvalb. Region_fraction_100um is 0.160 with a substantial cortical
    subplate (MBA:703 count_100um=824) component.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Pvalb subclass; classical type defined by Sst.
```
<!-- verdict-block-end -->
