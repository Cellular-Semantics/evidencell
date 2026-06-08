# CA3 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

## Introduction

CA3 pyramidal cells are the principal glutamatergic neurons of hippocampal area CA3 and form the main excitatory relay of the trisynaptic circuit, receiving mossy fiber input from dentate gyrus granule cells on thorny-excrescence-bearing proximal apical dendrites and projecting via Schaffer collaterals to CA1. The dense recurrent collateral network of CA3 is the anatomical substrate for pattern-completion memory models, and no molecular marker exclusively specific to CA3 has been identified in classical literature — thorny excrescence morphology and mossy fiber innervation remain the primary defining criteria.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA3 [UBERON:0014550] | [1], [2] |
| NT | glutamatergic | [3] |
| Defining markers | none documented | — |
| Negative markers | none documented | — |
| Neuropeptides | none documented | — |
| CL term | hippocampal pyramidal neuron [[CL:1001571](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001571)] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** quantitative hippocampal pyramidal-cell RNA-seq panel · [1]
  > we used next-generation RNA sequencing (RNA-seq) to produce a quantitative, whole genome characterization of gene expression for the major excitatory neuronal classes of the hippocampus; namely, granule cells and mossy cells of the dentate gyrus, and pyramidal cells of areas CA3, CA2, and CA1
  > — Cembrowski et al. 2016, abstract · [1] <!-- quote_key: 4875295_4a456257 -->
- **Soma location:** knowledge-base enumeration of rodent hippocampal neuron types · [2]
  > Hippocampome.org is a comprehensive knowledge base of neuron types in the rodent hippocampal formation (dentate gyrus, CA3, CA2, CA1, subiculum, and entorhinal cortex)
  > — Wheeler et al. 2015, abstract · [2] <!-- quote_key: 631148_edb9eac6 -->
- **NT type:** review of hippocampal principal-cell glutamatergic identity · [3]
  > There are 2 types of principal cells in the hippocampal circuit: glutamatergic pyramidal cells in the Ammon's horn and subiculum regions, and glutamatergic granule cells in the DG (Figure 1). They generally have excitatory effects on the neurons to which they send axon terminals including other glutamatergic and GABAergic, as well monoaminergic [5-HT, norepinephrine (NE), dopamine (DA)], cholinergic, and histaminergic (HA) cells.
  > — Dale et al. 2015, Major Glutamatergic Cell Types in Hippocampal Subfields · [3] <!-- quote_key: 2281033_5b9805ff -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: hippocampal pyramidal neuron [[CL:1001571](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001571)] (BROAD).

**Proposed CL term:** *CA3 pyramidal cell* (SUBMITTED) — submitted as a child of CL:1001571 (hippocampal pyramidal neuron); tracking issue [obophenotype/cell-ontology#3653](https://github.com/obophenotype/cell-ontology/issues/3653).

---

## Results

Annotation transfer of Yao 2021 CA3 single-cell labels onto WMBv1 supports a supertype-level mapping to 0078 CA3 Glut_4 [CS20230722_SUPT_0078] within the 017 CA3 Glut subclass, with the source-side CA3 cohort partitioning across all five supertypes of that subclass (see figure and Table 1). The mapping is supertype-resolution rather than 1:1 at cluster level: the Yao CA3 cohort distributes across multiple CA3 Glut clusters, and the strict in-region soma fraction is moderate (`region_fraction: 0.539`) while the 100-µm-proximity fraction is near-saturating (`region_fraction_100um: 0.969`), consistent with CA3 PCs whose somata sit within the CA3 pyramidal layer and its immediate boundary.

![Annotation transfer F1 across taxonomy levels for the Yao 2021 CA3 source group](figures/f1_for_ca3_pc_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 (GSE185862) SSv4 CA3 source group (n=322 source cells). Coverage = fraction of source-group cells landing on the target; Purity = fraction of target cells from the source group. With a single source group in the figure, Purity is 1.0 at the supertype and cluster best targets and only Coverage discriminates. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. The subclass-level mapping is essentially complete (017 CA3 Glut subclass F1=0.99, Coverage=0.99); supertype-level resolution lands on 0078 CA3 Glut_4 with the remaining Yao CA3 cells distributing across the four sibling CA3 Glut supertypes within the same subclass.*

### 4b. Property alignment + Evidence support — 0078 CA3 Glut_4 [CS20230722_SUPT_0078]

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA3 [UBERON:0014550] | Field CA3, pyramidal layer [MBA:495] count_100um=8918; Field CA3 [MBA:463] count_100um=9164; hippocampal formation [MBA:1089] count_100um=9204 (`region_fraction_100um: 0.969`; strict `region_fraction: 0.539`) | not assessed (no child-cluster edge with property comparisons on graph) | CONSISTENT |
| NT type | glutamatergic | not asserted on supertype metadata | not assessed | NOT_ASSESSED |
| Sex ratio | not documented | not available (MFR is rank-0 only) | not assessed | NOT_ASSESSED |

*(Child-cluster breakdown not assessed in this graph — no per-cluster property comparisons are recorded against children of SUPT_0078; see proposed experiments.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (SUPT_0078) | Atlas metadata | SUPPORT | region_fraction_100um=0.97; subclass 017 CA3 Glut; defining markers Homer3, Cldn22 | atlas-internal |
| Yao 2021 SSv4 MapMyCells AT | Annotation transfer | SUPPORT | F1=0.77 at supertype (Cov=0.63, Pur=1.0); F1=0.99 at subclass | atlas-internal |

**Marker evidence provenance.** No defining markers, negative markers, or neuropeptides are recorded on the classical CA3 PC node, so no marker concordance check applies. The atlas metadata records *Homer3* and *Cldn22* as defining markers on SUPT_0078, but these are atlas-team annotations rather than classical CA3 PC markers; they support the supertype's identity within the CA3 Glut subclass but cannot be cross-checked against a classical marker list for this type. A targeted literature trawl for transcript-level CA3 PC discriminators (and any reported heterogeneity across the five CA3 Glut supertypes) would help resolve why the Yao 2021 cohort partitions across all five supertypes of the 017 CA3 Glut subclass.

### 5. Primary candidate: 0078 CA3 Glut_4 [CS20230722_SUPT_0078] · 🟡 MODERATE

**Supporting evidence**
- Annotation transfer of Yao 2021 (GSE185862) SSv4 CA3 labels onto WMBv1 lands 203 of 322 source cells (63%) on SUPT_0078 with F1=0.77 (Coverage=0.63, Purity=1.0); the dominant supertype-level correspondence among the five CA3 Glut supertypes.
- Subclass-level transfer is essentially complete: 320 of 322 Yao CA3 cells (99.4%) land on the 017 CA3 Glut subclass with F1=0.99. This confirms that the classical CA3 PC type maps to the CA3 Glut subclass at very high resolution and that the only open question is the within-subclass supertype distribution.
- Soma location is consistent with classical CA3: SUPT_0078 MERFISH counts concentrate in field CA3, pyramidal layer [MBA:495] (count_100um=8918), with negligible spread outside the hippocampal formation; `region_fraction_100um: 0.969`.
- The atlas's annotation transfer figure shows Coverage=1.0 at the class level for the 01 IT-ET Glut class, reflecting that all Yao CA3 cells land within the broad glutamatergic class (the low class-level F1=0.28 is a Purity artefact — that class contains many cortical populations unrelated to CA3 PCs).

**Concerns**
- The Yao CA3 cohort is distributed across all five CA3 Glut supertypes (SUPT_0075–0079): SUPT_0078 (63.0%), SUPT_0075 (16.8%), SUPT_0077 (11.5%), SUPT_0076 (6.5%), and SUPT_0079 (1.6%). The mapping is therefore not 1:1 at supertype level — a single classical CA3 PC label maps to several taxonomy_types within the same subclass.
- The cluster-level AT best target (0315 CA3 Glut_4) drops to F1=0.70 (Coverage=0.54, Purity=1.0) — clean for its target but capturing only just over half of the Yao CA3 cohort, with the remainder distributed across sibling clusters. This is consistent with within-CA3 sublayer or proximodistal heterogeneity that the atlas resolves at finer resolution than the classical anatomical label. *(note: no edge to that cluster is currently in the graph — see open questions.)*
- Strict in-region soma fraction is moderate (`region_fraction: 0.539`) while proximity-based fraction is high (`region_fraction_100um: 0.969`). The disagreement is the signature of boundary scatter — many SUPT_0078 cells sit within 100 µm of MBA:495 (the CA3 pyramidal layer) without being strictly inside the painted polygon — and does not constitute counter-evidence against the mapping.
- No NT annotation on the supertype metadata, so the glutamatergic NT identity of the classical type cannot be directly cross-checked at supertype level (the named 017 CA3 Glut subclass is the operative cross-check).

**What would upgrade confidence**
- Annotation transfer from a CA3-sublayer-resolved dataset (CA3a, CA3b, CA3c) onto WMBv1 to determine whether SUPT_0075, SUPT_0076, SUPT_0077, and SUPT_0079 correspond to CA3 sublayers, proximodistal positions, or other organisational axes (target F1 ≥ 0.80 at supertype across sublayer-labelled source groups). Expected output: AnnotationTransferEvidence; resolves open question 1.
- Targeted literature search for transcript-level CA3 PC discriminators and for reported heterogeneity within the CA3 PC population (sublayer, proximodistal, dorsoventral). Expected output: LiteratureEvidence + populated `defining_markers` on the classical node.
- Cluster-resolution edges for the AT-best child cluster (0315 CA3 Glut_4) and its siblings within SUPT_0078, so the within-supertype scatter can be assessed against atlas property comparisons; the current top-K does not include an edge to that cluster.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 target | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0078 CA3 Glut_4 [CS20230722_SUPT_0078]` | — | 2147 | 🟡 MODERATE | AT F1=0.77 to supertype; region 0.97 | Primary |
| `0075 CA3 Glut_1 [CS20230722_SUPT_0075]` | — | 763 | ⚪ UNCERTAIN | AT 16.8% of Yao CA3 at supertype | Eliminated (minor share of CA3 cohort) |
| `0076 CA3 Glut_2 [CS20230722_SUPT_0076]` | — | 962 | ⚪ UNCERTAIN | AT 6.5% of Yao CA3 at supertype | Eliminated (minor share of CA3 cohort) |
| `0077 CA3 Glut_3 [CS20230722_SUPT_0077]` | — | 1039 | ⚪ UNCERTAIN | AT 11.5% of Yao CA3 at supertype | Eliminated (minor share of CA3 cohort) |
| `0079 CA3 Glut_5 [CS20230722_SUPT_0079]` | — | 318 | 🔴 REFUTED | AT 1.6% Yao CA3; MERFISH soma in dentate gyrus polymorph layer | Eliminated (hilar location, not CA3) |
| `0297 CA3 Glut_1 [CS20230722_CLUS_0297]` | 0075 CA3 Glut_1 | 199 | ⚪ UNCERTAIN | Region 0.73; no AT evidence on edge | Eliminated (no cluster-level AT support) |
| `0300 CA3 Glut_1 [CS20230722_CLUS_0300]` | 0075 CA3 Glut_1 | 60 | ⚪ UNCERTAIN | Region 0.90; LOW_CELL_COUNT (n=60) | Eliminated (no cluster-level AT support) |
| `0301 CA3 Glut_1 [CS20230722_CLUS_0301]` | 0075 CA3 Glut_1 | 101 | ⚪ UNCERTAIN | Region 0.63; CA1 spread in MERFISH | Eliminated (no cluster-level AT support) |
| `0303 CA3 Glut_2 [CS20230722_CLUS_0303]` | 0076 CA3 Glut_2 | 164 | ⚪ UNCERTAIN | Region 0.81; no AT evidence on edge | Eliminated (no cluster-level AT support) |
| `0309 CA3 Glut_3 [CS20230722_CLUS_0309]` | 0077 CA3 Glut_3 | 246 | ⚪ UNCERTAIN | Region 0.73; no AT evidence on edge | Eliminated (no cluster-level AT support) |

Two graph edges target SUPT_0078: `edge_ca3_pc_hippocampus_to_supt_0078` (the substantive edge carrying ATLAS_METADATA + ANNOTATION_TRANSFER evidence and the AMBIGUOUS_MAPPING caveat) and `edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078` (a fresh-emit stub carrying only `discovery_score` and a partial property comparison). The substantive edge is the primary record; the stub is flagged for curator removal (see open questions).

</details>

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** CA3 pyramidal cell, definition basis: CLASSICAL_MULTIMODAL. Glutamatergic principal cell of hippocampal area CA3 [1, 2, 3], with soma in the pyramidal layer of CA3 [UBERON:0014550] [1, 2]. No molecular defining markers, negative markers, or neuropeptides have been entered on the classical node; the defining criteria in the classical literature are thorny-excrescence morphology and mossy fiber innervation.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 SSv4 mouse hippocampal formation; CA3 source label) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells (default parameters) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398; 322 in CA3 source group) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |
| Best per level (from figure sidecar) | CLASS 01 IT-ET Glut F1=0.28 (Cov=1.00, Pur=0.16, n=322); SUBCLASS 017 CA3 Glut F1=0.99 (Cov=0.99, Pur=0.99, n=320); SUPERTYPE 0078 CA3 Glut_4 F1=0.77 (Cov=0.63, Pur=1.00, n=198); CLUSTER 0315 CA3 Glut_4 F1=0.70 (Cov=0.54, Pur=1.00, n=157) |
| Caveats | — |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:49+00:00 from [kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_ca3_pc_hippocampus_to_supt_0078 | ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0075 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0076 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0077 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0079 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0297 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0300 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0301 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0303 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0309 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** CA3 pyramidal cell → 0078 CA3 Glut_4 [CS20230722_SUPT_0078] at MODERATE confidence. Key support: annotation transfer (Yao 2021 SSv4 CA3 → SUPT_0078 F1=0.77; 017 CA3 Glut subclass F1=0.99) and atlas MERFISH soma counts saturating the CA3 pyramidal layer. Key caveats: AMBIGUOUS_MAPPING (Yao CA3 cells distribute across all five CA3 Glut supertypes), and SINGLE_DATASET (a single MapMyCells run from Yao 2021 is the only cross-dataset anchor).

The Cell Ontology has no specific term for this population; hippocampal pyramidal neuron [[CL:1001571](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001571)] is the closest ancestor. CA3 pyramidal cells are a subpopulation of hippocampal pyramidal neurons; CL:1001571 covers all hippocampal pyramidal neurons without anatomical resolution to individual subfields. No CA3-specific CL term currently exists. A new term *CA3 pyramidal cell* has been submitted to the Cell Ontology as a child of CL:1001571.

### 7. Proposed experiments and follow-ups

- **What:** annotation transfer from a CA3-sublayer-resolved dataset (CA3a / CA3b / CA3c, or proximodistal-position-resolved labels) onto WMBv1.
  **Target:** F1 ≥ 0.80 at supertype level for at least one sublayer label per supertype within the 017 CA3 Glut subclass.
  **Expected output:** AnnotationTransferEvidence on edges between sublayer-resolved source groups and SUPT_0075 / SUPT_0076 / SUPT_0077 / SUPT_0078 / SUPT_0079.
  **Resolves:** open question 1 (sublayer correspondence among CA3 Glut supertypes) and the AMBIGUOUS_MAPPING caveat on the primary edge.

The existing Yao 2021 MapMyCells run already addresses the question "does the classical CA3 PC type map to the CA3 Glut subclass?" (yes — F1=0.99 at subclass). A second, sublayer-resolved AT run would address what the existing run cannot: the within-subclass partition.

### 8. Open questions

1. Do SUPT_0075, SUPT_0076, SUPT_0077 correspond to CA3a, CA3b, CA3c sublayers respectively, or to other organisational principles (e.g. proximal vs. distal mossy fiber input zone)? *(from primary edge)*
2. Should the duplicate fresh-emit edge `edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078` be removed in favour of the substantive `edge_ca3_pc_hippocampus_to_supt_0078`? Both target the same supertype accession; the substantive edge carries the AT evidence and the AMBIGUOUS_MAPPING caveat while the fresh-emit edge carries only `discovery_score` and a stub property comparison.
3. The cluster-resolution AT best target for the Yao CA3 cohort is 0315 CA3 Glut_4 (F1=0.70), but no edge to that cluster is present in the current top-K. Should an edge be emitted at rank 0 so the within-supertype best-cluster correspondence is recorded?

---

## References

| # | Citation | PMID | Used for |
|---:|---|---|---|
| [1] | Cembrowski et al. 2016 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915) | soma location |
| [2] | Wheeler et al. 2015 | [26402459](https://pubmed.ncbi.nlm.nih.gov/26402459) | soma location |
| [3] | Dale et al. 2015 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726) | neurotransmitter type |

---

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_supt_0078 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.65
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Annotation transfer (Yao 2021 GSE185862 SSv4 via MapMyCells in
    at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1) lands 63% of source CA3 cells on
    CS20230722_SUPT_0078 with F1=0.77 at supertype and F1=0.99 at subclass
    CS20230722_SUBC_017; MERFISH soma counts saturate Field CA3, pyramidal layer
    [MBA:495] with region_fraction_100um: 0.969. Mapping is 1:n because the Yao CA3
    cohort distributes across all five CS20230722_SUBC_017 supertypes (0075–0079).
  reconciliation_note: >
    Duplicate edge edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078 targets the same
    supertype with only a discovery_score stub; the substantive evidence (AT + caveat)
    lives on this edge — curator removal of the duplicate recommended.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Yao 2021 source CA3 cells distribute across all five CS20230722_SUBC_017
        supertypes (SUPT_0078 63.0%, SUPT_0075 16.8%, SUPT_0077 11.5%, SUPT_0076 6.5%,
        SUPT_0079 1.6%); CS20230722_SUPT_0078 is the dominant correspondence but not 1:1.
    - caveat_type: SINGLE_DATASET
      description: >
        Annotation transfer evidence comes from a single source dataset (Yao 2021
        GSE185862 SSv4); independent replication on a second CA3-resolved dataset is
        not yet available.
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        Best supportable resolution is supertype CS20230722_SUPT_0078 (F1=0.77);
        cluster-level transfer best target is CS20230722_CLUS_0315, which is not
        currently represented as an edge in this graph.
  proposed_experiments:
    - >
      Annotation transfer from a CA3-sublayer-resolved dataset (CA3a / CA3b / CA3c,
      or proximodistal labels) onto WMBv1 CCN20230722 via MapMyCells; target F1 >= 0.80
      at supertype for each sublayer source group; expected output
      AnnotationTransferEvidence on edges to CS20230722_SUPT_0075 / 0076 / 0077 /
      0078 / 0079.
  unresolved_questions:
    - >
      Do CS20230722_SUPT_0075, CS20230722_SUPT_0076, CS20230722_SUPT_0077 correspond
      to CA3a, CA3b, CA3c sublayers respectively, or to another organisational axis
      (proximal vs distal mossy fiber input zone)?
    - >
      Curator removal of duplicate edge
      edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078 — legacy/fresh-emit ID
      collision on taxonomy_type CS20230722_SUPT_0078.
    - >
      Should an edge be emitted to CS20230722_CLUS_0315 (cluster-level AT best target,
      F1=0.70) so the within-supertype best-cluster correspondence is recorded?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Duplicate fresh-emit edge targeting CS20230722_SUPT_0078; the
    substantive evidence (AT + caveat) lives on edge_ca3_pc_hippocampus_to_supt_0078.
    This edge carries only a discovery_score stub and a partial property comparison;
    flagged for curator removal.
  caveats:
    - caveat_type: OTHER
      description: >
        Duplicate edge — legacy/fresh-emit ID collision on taxonomy_type
        CS20230722_SUPT_0078; substantive record lives on
        edge_ca3_pc_hippocampus_to_supt_0078.
  proposed_experiments: []
  unresolved_questions:
    - >
      Curator removal of duplicate edge
      edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0075 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.25
  rationale: >
    [tier:CUT] Edge carries only ATLAS_METADATA; the AT cohort distribution captured
    on the SUPT_0078 edge attributes a minor share of the Yao 2021 CA3 source cells to
    this supertype. region_fraction_100um: 0.708 places somata in CA3, but the supertype's
    sublayer or proximodistal identity within CS20230722_SUBC_017 is unresolved.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Supertype captures a minor share of the Yao 2021 CA3 cohort; correspondence
        to a CA3 sublayer or proximodistal subdivision unresolved.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0076 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Edge carries only ATLAS_METADATA; the AT cohort distribution captured
    on the SUPT_0078 edge attributes a minor share of the Yao 2021 CA3 source cells to
    this supertype. region_fraction_100um: 0.842 places somata in CA3, but the supertype's
    sublayer identity within CS20230722_SUBC_017 is unresolved.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Supertype captures a minor share of the Yao 2021 CA3 cohort; correspondence
        to a CA3 sublayer or proximodistal subdivision unresolved.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0077 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.25
  rationale: >
    [tier:CUT] Edge carries only ATLAS_METADATA; the AT cohort distribution captured
    on the SUPT_0078 edge attributes a minor share of the Yao 2021 CA3 source cells to
    this supertype. region_fraction_100um: 0.713 places somata in CA3, but the supertype's
    sublayer identity within CS20230722_SUBC_017 is unresolved.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Supertype captures a minor share of the Yao 2021 CA3 cohort; correspondence
        to a CA3 sublayer or proximodistal subdivision unresolved.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0079 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Edge carries only ATLAS_METADATA; the AT cohort distribution captured
    on the SUPT_0078 edge attributes a minor share of the Yao 2021 CA3 source cells to
    this supertype. MERFISH soma counts on this supertype concentrate in Dentate gyrus,
    polymorph layer [MBA:10704] rather than the CA3 pyramidal layer — anatomically
    incompatible with CA3 pyramidal cells.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        CS20230722_SUPT_0079 MERFISH somata localise to the dentate gyrus polymorph
        layer (MBA:10704), not to the CA3 pyramidal layer; consistent with hilar
        mossy-cell rather than CA3 pyramidal-cell identity.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0297 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Cluster within CS20230722_SUPT_0075; region_fraction_100um: 0.735 puts
    somata in CA3 stratum oriens but no cluster-level annotation transfer evidence is
    recorded on this edge and the parent supertype captures only a minor share of the
    Yao 2021 CA3 cohort.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Cluster sits within a parent supertype that captures a minor share of the Yao
        2021 CA3 cohort; cluster-level AT evidence not recorded.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0300 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Cluster within CS20230722_SUPT_0075; region_fraction_100um: 0.895 puts
    somata in CA3 stratum oriens but no cluster-level annotation transfer evidence is
    recorded and the cluster has only 60 atlas cells.
  caveats:
    - caveat_type: LOW_CELL_COUNT
      description: >
        Cluster has 60 atlas cells, below the ~50-cell robustness threshold's margin;
        cluster-level AT not recorded on this edge.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0301 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] Cluster within CS20230722_SUPT_0075; region_fraction_100um: 0.628 with
    notable MERFISH spread into Field CA1 [MBA:382] (count_100um=178) — boundary
    scatter with a sibling subfield. No cluster-level AT evidence recorded.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        MERFISH counts show comparable density in Field CA3 [MBA:463] and Field CA1
        [MBA:382], suggesting a CA3/CA1 boundary population rather than a clean CA3
        pyramidal cluster.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0303 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Cluster within CS20230722_SUPT_0076; region_fraction_100um: 0.810 with
    MERFISH somata in Field CA3, pyramidal layer [MBA:495] but no cluster-level AT
    evidence recorded and the parent supertype captures only 6.5% of the Yao 2021 CA3
    cohort.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Cluster sits within a parent supertype that captures a minor share of the Yao
        2021 CA3 cohort; cluster-level AT evidence not recorded.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0309 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Cluster within CS20230722_SUPT_0077; region_fraction_100um: 0.730 puts
    somata in CA3 stratum oriens but no cluster-level annotation transfer evidence is
    recorded and the parent supertype captures only 11.5% of the Yao 2021 CA3 cohort.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Cluster sits within a parent supertype that captures a minor share of the Yao
        2021 CA3 cohort; cluster-level AT evidence not recorded.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->
