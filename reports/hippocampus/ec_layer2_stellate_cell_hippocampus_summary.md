# entorhinal cortex layer II stellate cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

---

## Introduction

Entorhinal cortex layer II principal neurons comprise two distinct excitatory populations distinguished by morphology, marker expression, and projection target. Reelin-positive stellate cells project to the dentate gyrus and CA3/CA2, while calbindin-positive pyramidal cells project to CA1 [1][3][7]. These cells provide the principal cortical input to the hippocampus and are central to spatial memory and grid-cell function [4][5].

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | entorhinal cortex [UBERON:0002728] (layer II) | [1][2][3][4][5][6][7] |
| NT | glutamatergic | [4] |
| Defining markers | Reln | [1] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** asta_report · [1]
  > Principal neurons in layer 2 are divided into two distinct cell types, pyramidal and stellate, based on morphology, immunoreactivity, and functional properties
  > — Naumann et al. 2015, abstract · [1] <!-- quote_key: 10060696_40a9cee6 -->
- **Soma location:** asta_report · [2]
  > we identified essential components of LII networks in the MEC. We distinguished four types of excitatory neurons that exhibit cell-type-specific local excitatory and inhibitory
  > — Unknown et al. 2016, abstract · [2] <!-- quote_key: 16218278_b1f423dd -->
- **Soma location:** asta_report · [3]
  > cannabinoid type 1 receptor–expressing GABAergic basket cells selectively innervated principal cells in layer II of the rat MEC that projected outside the hippocampus but avoided neighboring cells that give rise to the perforant pathway to the dentate gyrus
  > — Unknown et al. 2010, abstract · [3] <!-- quote_key: 10189534_bd3e2e57 -->
- **Soma location:** asta_report · [4]
  > The entorhinal cortex (EC) is a major gateway between the hippocampus and telencephalic structures, and plays a critical role in memory and navigation
  > — Unknown et al. 2021, abstract · [4] <!-- quote_key: 244909998_0364a3fb -->
- **Soma location:** asta_report · [5]
  > The entorhinal cortex contains specialized glutamatergic pyramidal neurons and is part of the medial temporal lobe, lying between the transentorhinal area and hippocampal formation (Strell et al., 2023).
  > — Unknown et al. 2023, Entorhinal Cortex Glutamatergic Populations · [5] <!-- quote_key: 258843956_9ed20870 -->
- **Soma location:** asta_report · [6]
  > The entorhinal cortex acts as the main interface between the hippocampus and neocortex and is divided into two subdivisions-lateral and medial-that exhibit distinct anatomical features and input-output connectivity (Park et al., 2018).
  > — Unknown et al. 2018, Entorhinal Cortex Glutamatergic Populations · [6] <!-- quote_key: 4935821_0f0827e4 -->
- **Soma location:** asta_report · [7]
  > Principal neurons in entorhinal cortex layer II are of two types, stellate-like neurons and pyramidal neurons, the former of which express reelin, whereas the latter include a large population of calbindin-expressing neurons (Ohara et al., 2021)(Varga et al., 2010)(Fuchs et al., 2016)(Ohara et al., 2019)(Zutshi et al., 2018).
  > — Unknown et al. 2018, Entorhinal Cortex Glutamatergic Populations · [7] <!-- quote_key: 52194250_9b25e78b -->
- **Defining marker (Reln):** asta_report · [1]
  > Reelin-positive cells project to the dentate gyrus and show electrophysiological parameters of stellate cells (Varga et al., 2010), whereas calbindin-positive cells project to CA1 (Kitamura et al., 2014) and have electrophysiological properties described previously for pyramidal cells (Klink and Alonso, 1997).
  > — Naumann et al. 2015, layer 2 medial entorhinal cortex · [1] <!-- quote_key: 10060696_46dbde68 -->

</details>

Cell Ontology mapping: glutamatergic neuron [[CL:0000679](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000679)] (BROAD).

---

## Results

Annotation transfer of the Yao 2021 lateral entorhinal cortex layer II IT subclass onto WMBv1 supports mapping to supertype 0042 L2/3 IT PIR-ENTl Glut_4 [CS20230722_SUPT_0042] (F1=0.96), with cluster 0155 L2/3 IT PIR-ENTl Glut_4 [CS20230722_CLUS_0155] standing out as the EC-layer-II resident child cluster (region_fraction_100um=0.918; Reln cohort percentile 0.97; see property comparison table). Several medial-EC layer II supertypes (SUPT_0051, SUPT_0052, SUPT_0053) carry consistent Reln expression and EC localisation as alternative candidates, raising the possibility that the classical reelin-positive stellate population is distributed across both lateral and medial EC layer II transcriptomic types *(note: classical literature describes stellate cells in both MEC and LEC layer II; the AT evidence in hand interrogates only the Yao 2021 lateral-EC subclass)*.

### 0042 L2/3 IT PIR-ENTl Glut_4 [CS20230722_SUPT_0042] · 🟡 MODERATE

**Property alignment**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | glutamatergic | not asserted | Glut (CLUS_0155) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Soma location | entorhinal cortex [UBERON:0002728] | region_fraction_100um=0.232; dominant soma in Olfactory areas [MBA:698] / Piriform area [MBA:961] | region_fraction_100um=0.918 in Hippocampal formation [MBA:1089] / Entorhinal area, lateral part, layer 2 [MBA:20] (CLUS_0155) | SUPT: APPROXIMATE; CLUS: CONSISTENT |
| Reln expression | defining marker | Reln=8.17 (cohort_pct 0.92; child-coverage 1.00) | Reln=10.31 (cohort_pct 0.97) (CLUS_0155) | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

*(2 of the supertype's child clusters [CLUS_0155, CLUS_0158] are in EC layer II by region_fraction_100um and carry Reln at high cohort percentile; the supertype-level location signal is diluted because other child clusters sit in piriform/olfactory areas. Best child cluster within SUPT_0042 for EC residency: CLUS_0155.)*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Yao 2021 SSv4 → WMBv1 (L2 IT ENTl subclass) | Annotation transfer | SUPPORT | F1=0.96 at supertype | atlas-internal |

**Supporting evidence**

- Annotation transfer from the Yao 2021 lateral entorhinal cortex layer II IT subclass (n=180 source cells) onto WMBv1 places these cells on supertype 0042 L2/3 IT PIR-ENTl Glut_4 [CS20230722_SUPT_0042] with F1=0.96, coverage=0.96, purity=0.97 — a near-perfect supertype-level mapping for cells representing the reelin-positive stellate population of lateral EC layer II.
- Reln is expressed at cohort percentile 0.92 across the supertype (mean 8.17) with child-cluster coverage 1.00, consistent with reelin's role as the defining stellate-cell marker [1].

**Marker evidence provenance**

- **Reln:** the asta_report citation [1] (Naumann et al. 2015) establishes Reln as the discriminator between EC layer II stellate (Reln+) and pyramidal (Calb1+) populations on the basis of morphological reconstruction and projection-target tracing. The atlas-side precomputed expression (cohort_pct 0.92 across SUPT_0042; 0.97 on CLUS_0155) gives strong transcript-level confirmation. Calb1 was not assayed on the atlas side in this edge — a follow-up `add-expression` run for Calb1 would let the report distinguish SUPT_0042 (expected Reln+ Calb1-) from neighbouring pyramidal-bearing supertypes.

**Concerns**

- Supertype-level location is APPROXIMATE: `region_fraction_100um: 0.232` reflects soma counts dominated by Olfactory areas [MBA:698] and Piriform area [MBA:961] rather than entorhinal cortex (boundary scatter — `region_fraction_100um: 0.232`; the PIR-ENTl transcriptomic signature is shared between piriform cortex and lateral entorhinal layer II, so the supertype catchment extends into piriform; weak counter-evidence at supertype level, resolved at cluster level — see CLUS_0155).
- The Yao 2021 "L2 IT ENTl" subclass is defined in the Allen taxonomy by transcriptomic signature; it may contain a minor non-stellate fraction in lateral EC layer II beyond the canonical Reln+ stellate cells.

**What would upgrade confidence**

- Run `add-expression` for Reln and Calb1 on CCN20230722 across all candidate supertypes to distinguish stellate (Reln+ Calb1-) from pyramidal (Reln- Calb1+) populations at atlas level (would add atlas-internal marker evidence).
- Resolve whether the PIR-ENTl supertype signature reflects shared piriform/lateral-EC transcriptomics or atlas-side spatial inclusion of piriform cells — MERFISH spatial inspection on this supertype's painted clusters.

### 0155 L2/3 IT PIR-ENTl Glut_4 [CS20230722_CLUS_0155] · 🟡 MODERATE

**Property alignment**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | glutamatergic | not assessed at supertype on this edge | Glut | CONSISTENT |
| Soma location | entorhinal cortex [UBERON:0002728] | not assessed at supertype on this edge | region_fraction_100um=0.918; Hippocampal formation [MBA:1089] / Entorhinal area, lateral part, layer 2 [MBA:20] | CONSISTENT |
| Reln expression | defining marker | not assessed at supertype on this edge | Reln=10.31; cohort_pct 0.97; atlas category DEFINING | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

*(Within parent SUPT_0042, CLUS_0155 is the lateral-EC layer-II-resident child cluster: 86% of cells lie strictly in EC by `region_fraction`, 92% by proximity, and Reln is flagged DEFINING on the atlas side. The other layer-II child cluster CLUS_0158 carries a very similar profile and is named in the candidates audit table below.)*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (region + Reln) | Atlas metadata | PARTIAL | region_fraction_100um=0.918; Reln=10.31 (DEFINING) | atlas-internal |

**Supporting evidence**

- Of cluster 0155's painted cells, 92% lie within or near (≤100µm) the hippocampal formation / lateral EC layer II [MBA:20]; strict region_fraction is 0.86.
- Reln=10.31 (cohort_pct 0.97) with Reln flagged as DEFINING in the WMBv1 atlas metadata for CLUS_0155 — both literature [1] and atlas curation converge on Reln as the cluster's primary discriminator.

**Marker evidence provenance**

- **Reln:** primary citation [1] (Naumann et al. 2015) ties Reln to morphology-confirmed stellate cells; atlas-side Reln=10.31 with DEFINING category gives transcript-level confirmation. No circularity concern — the atlas supertype name (PIR-ENTl Glut_4) does not contain "Reln".

**Concerns**

- The cluster's painted-cell counts in Hippocampal formation [MBA:1089] and lateral entorhinal layer 2 [MBA:20] are nearly equal, reflecting MBA's hierarchical assignment of EC under the HPF parent rather than physical hippocampal residency — the cluster is in EC, not hippocampus proper.
- No direct annotation transfer at the cluster level is available for this edge (the supporting AT lives on the SUPT_0042 edge); cluster-level call rests on atlas metadata alone.

**What would upgrade confidence**

- Cluster-level AT bootstrap from a source dataset that explicitly distinguishes lateral-EC layer II stellate cells (e.g. Reln-Cre or morphologically reconstructed source cohort) — would add AnnotationTransferEvidence with F1 at CLUSTER level.
- `add-expression` for Calb1 to confirm CLUS_0155 is Calb1-low relative to neighbouring pyramidal-enriched clusters.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 target | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0042 L2/3 IT PIR-ENTl Glut_4 [CS20230722_SUPT_0042] | — | 16330 | 🟡 MODERATE | AT F1=0.96 from Yao 2021 LEC L2 IT subclass | Primary (supertype) |
| 0155 L2/3 IT PIR-ENTl Glut_4 [CS20230722_CLUS_0155] | 0042 L2/3 IT PIR-ENTl Glut_4 | 1859 | 🟡 MODERATE | region_fraction_100um=0.918; Reln DEFINING; cohort_pct 0.97 | Primary (best EC L2 child within SUPT_0042) |
| 0158 L2/3 IT PIR-ENTl Glut_4 [CS20230722_CLUS_0158] | 0042 L2/3 IT PIR-ENTl Glut_4 | 2043 | ⚪ UNCERTAIN | region_fraction_100um=0.879; Reln=10.28 | Supports broader mapping (sibling EC L2 child) |
| 0186 L2 IT ENT-po Glut_1 [CS20230722_CLUS_0186] | 0051 L2 IT ENT-po Glut_1 | 172 | ⚪ UNCERTAIN | MEC L2 cluster; Reln=9.69 | Eliminated (no AT support; alternative MEC L2 cluster) |
| 0190 L2 IT ENT-po Glut_3 [CS20230722_CLUS_0190] | 0053 L2 IT ENT-po Glut_3 | 495 | ⚪ UNCERTAIN | MEC L2 cluster; Reln=9.80 | Eliminated (no AT support; alternative MEC L2 cluster) |
| 0014 IT EP-CLA Glut_2 [CS20230722_CLUS_0014] | 0004 IT EP-CLA Glut_2 | 849 | 🔴 LOW | EC layer 6 cluster; Reln=1.81 (low) | Eliminated (wrong layer / weak Reln) |
| 0053 L2 IT ENT-po Glut_3 [CS20230722_SUPT_0053] | — | 495 | ⚪ UNCERTAIN | MEC L2 supertype; Reln cohort_pct 0.98 | Eliminated (no AT bridge from Yao 2021; alternative MEC candidate) |
| 0052 L2 IT ENT-po Glut_2 [CS20230722_SUPT_0052] | — | 992 | ⚪ UNCERTAIN | MEC L2/L3 supertype; Reln cohort_pct 0.96 | Eliminated (no AT bridge; alternative MEC candidate) |
| 0051 L2 IT ENT-po Glut_1 [CS20230722_SUPT_0051] | — | 350 | ⚪ UNCERTAIN | MEC L2 supertype; Reln cohort_pct 0.97 | Eliminated (no AT bridge; alternative MEC candidate) |
| 0010 L5/6 IT TPE-ENT Glut_4 [CS20230722_SUPT_0010] | — | 1791 | 🔴 LOW | EC layer 5 supertype; Reln=1.54 | Eliminated (wrong layer; weak Reln) |
| 0068 ENTmv-PA-COAp Glut_3 [CS20230722_SUPT_0068] | — | 963 | 🔴 LOW | MEC L5 supertype; Reln=8.50 | Eliminated (wrong layer) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Entorhinal cortex layer II stellate cell — definition_basis CLASSICAL_MULTIMODAL. Glutamatergic [4] excitatory neuron of entorhinal cortex layer II [UBERON:0002728], defined by Reln expression [1] and reelin-positive (vs. calbindin-positive pyramidal) morphology and projection pattern [1][2][3][7].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (L2 IT ENTl, Yao 2021 subclass) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:54+00:00 from [kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_ec_layer2_stellate_cell_hippocampus_to_supt_0042 | ANNOTATION_TRANSFER | SUPPORT | atlas-internal |
| edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_CLUS_0155 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_CLUS_0158 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_CLUS_0186 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_CLUS_0190 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_CLUS_0014 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_SUPT_0053 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_SUPT_0052 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_SUPT_0051 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_SUPT_0010 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_SUPT_0068 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** entorhinal cortex layer II stellate cell → 0042 L2/3 IT PIR-ENTl Glut_4 [CS20230722_SUPT_0042] at MODERATE confidence (supertype) with 0155 L2/3 IT PIR-ENTl Glut_4 [CS20230722_CLUS_0155] as the best-child resolution within it (MODERATE). Key support: annotation transfer from the Yao 2021 lateral EC L2 IT subclass (F1=0.96 at supertype) and Reln cohort percentiles above 0.92, with Reln flagged DEFINING by atlas curation on CLUS_0155. Key caveats: AMBIGUOUS_MAPPING (supertype catchment includes piriform-cortex cells alongside lateral EC layer II); DISCORDANT_ANATOMY at supertype level resolved at the cluster level.

The Cell Ontology has no specific term for EC layer II stellate cells; glutamatergic neuron [[CL:0000679](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000679)] is the closest ancestor. EC layer II stellate cells have stellate morphology and express reelin but not calbindin, distinguishing them from layer II pyramidal cells. No EC layer II stellate-specific CL term exists; CL:0000679 is used as the broadest accurate mapping.

### Proposed experiments and follow-ups

- **add-expression for Reln and Calb1 on CCN20230722.** Confirms (and contrasts) Reln+ stellate vs Calb1+ pyramidal populations across all EC layer II candidate supertypes. Expected output: extends `precomputed_expression` blocks on taxonomy nodes; resolves whether SUPT_0042 is Calb1-low and whether the medial-EC supertypes (SUPT_0051/52/53) are equally Reln+ Calb1- (which would expand the mapping cardinality).
- **Cluster-level AT with a Reln-Cre or morphologically reconstructed source cohort.** Resolves whether the AT signal can resolve EC L2 stellate identity at cluster (vs. supertype) level. Target: F1 ≥ 0.80 at CLUSTER level. Expected output: AnnotationTransferEvidence on the cluster edges.

### Open questions

1. Does SUPT_0042 expression include a significant piriform cortex component in the WMBv1 MERFISH data, or is the PIR-ENTl designation primarily driven by transcriptomic similarity rather than spatial overlap?
2. Is Reln expressed in SUPT_0042 at the level expected for stellate cells? Running add-expression for Reln on CCN20230722 precomputed stats would confirm.
3. Does the classical Reln+ stellate population distribute across both lateral EC supertypes (SUPT_0042 family) and medial EC supertypes (SUPT_0051/0052/0053 families), or is the lateral-EC mapping primary?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Naumann et al. 2015 | [26223342](https://pubmed.ncbi.nlm.nih.gov/26223342) | soma location |
| [2] | Unknown 2016 | [26711115](https://pubmed.ncbi.nlm.nih.gov/26711115) | soma location |
| [3] | Unknown 2010 | [20512133](https://pubmed.ncbi.nlm.nih.gov/20512133) | soma location |
| [4] | Unknown 2021 | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991) | soma location |
| [5] | Unknown 2023 | [37219048](https://pubmed.ncbi.nlm.nih.gov/37219048) | soma location |
| [6] | Unknown 2018 | [29665671](https://pubmed.ncbi.nlm.nih.gov/29665671) | soma location |
| [7] | Unknown 2018 | [30209250](https://pubmed.ncbi.nlm.nih.gov/30209250) | soma location |

<!-- verdict-block-start: edge_ec_layer2_stellate_cell_hippocampus_to_supt_0042 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.7
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Annotation transfer from the Yao 2021 lateral EC layer II IT
    subclass (run_ref at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1) lands on
    CS20230722_SUPT_0042 with F1=0.96; Reln (cohort_pct 0.92, child-coverage 1.00)
    matches the classical defining marker. region_fraction_100um=0.23 at supertype
    is APPROXIMATE because the PIR-ENTl signature extends into piriform/olfactory
    areas; resolved at child-cluster level on CS20230722_CLUS_0155
    (region_fraction_100um=0.918, Reln DEFINING) — paired best-child verdict.
  reconciliation_note: >
    Paired with best-child CS20230722_CLUS_0155 verdict (skos:closeMatch).
    Supertype catchment includes piriform-cortex children; cluster-level
    mapping concentrates the EC L2 stellate signal on CLUS_0155 and CLUS_0158.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        The Yao 2021 L2 IT ENTl subclass may include both Reln+ stellate cells
        and minor non-stellate populations in lateral EC layer II; the PIR
        component of SUPT_0042's name reflects a shared transcriptomic
        signature with piriform cortex and the supertype catchment extends
        into piriform/olfactory areas (region_fraction_100um=0.23).
    - caveat_type: SINGLE_DATASET
      description: >
        Annotation transfer evidence comes from a single Yao 2021 SSv4 dataset
        (GEO:GSE185862); independent replication with a stellate-specific
        source cohort would strengthen the call.
  proposed_experiments:
    - >
      Run add-expression for Reln and Calb1 on CCN20230722 to distinguish
      SUPT_0042 (Reln+, stellate) from neighbouring pyramidal-enriched
      supertypes at the atlas level.
    - >
      Cluster-level AT with a Reln-Cre or morphology-confirmed stellate source
      cohort; target F1 >= 0.80 at CLUSTER level.
  unresolved_questions:
    - >
      Does the classical Reln+ stellate population distribute across both
      lateral EC supertypes (SUPT_0042 family) and medial EC supertypes
      (SUPT_0051/0052/0053 families)?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_CLUS_0155 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.65
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CS20230722_CLUS_0155 is the EC-layer-II-resident child of
    CS20230722_SUPT_0042: region_fraction_100um=0.92 in Entorhinal area lateral
    part layer 2 (MBA:20), and Reln is flagged DEFINING by atlas curation
    (cohort_pct 0.97). Supertype-level AT (F1=0.96) on the parent SUPT_0042
    transfers to this cluster as best EC L2 child; sibling CLUS_0158 shares
    a closely matching profile. No cluster-level AT bootstrap is available
    on this edge.
  reconciliation_note: >
    Paired with parent CS20230722_SUPT_0042 verdict (skos:broadMatch 1:n).
    Best EC L2 child within SUPT_0042; sibling CLUS_0158 is a near-equivalent
    candidate.
  caveats:
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        Supporting annotation transfer evidence is at supertype level
        (CS20230722_SUPT_0042, F1=0.96) rather than the cluster level;
        cluster-level mapping here rests on atlas metadata (region and
        Reln expression) without a cluster-level AT bootstrap.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Sibling cluster CS20230722_CLUS_0158 (region_fraction_100um=0.88,
        Reln cohort_pct 0.96) within the same SUPT_0042 supertype carries
        a closely matching profile; the choice of CLUS_0155 as primary best
        child is marginal.
  proposed_experiments:
    - >
      Run add-expression for Calb1 on CCN20230722 to confirm CLUS_0155 is
      Calb1-low relative to neighbouring pyramidal-enriched clusters.
    - >
      Cluster-level AT with a stellate-specific source cohort; target
      F1 >= 0.80 at CLUSTER level on CS20230722_CLUS_0155.
  unresolved_questions:
    - >
      Is CS20230722_CLUS_0155 distinguishable from sibling CS20230722_CLUS_0158
      by classical-type-relevant features (e.g. projection target, Calb1 status)?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_CLUS_0158 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.4
  rationale: >
    [tier:WEAKEST] CS20230722_CLUS_0158 is a near-equivalent sibling of
    CS20230722_CLUS_0155 within SUPT_0042: region_fraction_100um=0.88 in
    Entorhinal area lateral part layer 2 (MBA:20), Reln cohort_pct 0.97.
    Supports the broader mapping to SUPT_0042 but does not lead the
    cluster-level candidate set on the available signals.
  caveats:
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        No cluster-level annotation transfer is available; selection between
        CS20230722_CLUS_0155 and CS20230722_CLUS_0158 cannot be made from the
        current evidence portfolio.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_CLUS_0186 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.3
  rationale: >
    [tier:CUT] CS20230722_CLUS_0186 is an MEC layer II cluster within the
    SUPT_0051 medial-EC family (region_fraction_100um=0.94, Reln=9.69) with
    no annotation transfer bridge from the Yao 2021 lateral-EC source. Plausible
    alternative MEC candidate; without an MEC-targeted AT cohort the call
    cannot be made.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_CLUS_0190 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.3
  rationale: >
    [tier:CUT] CS20230722_CLUS_0190 is an MEC layer II cluster within the
    SUPT_0053 medial-EC family (region_fraction_100um=0.99, Reln=9.80). No
    AT bridge from the Yao 2021 lateral-EC subclass; alternative MEC candidate
    pending MEC-targeted evidence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_CLUS_0014 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0014 sits in lateral EC layer 6a
    (region_fraction_100um=0.75) — wrong cortical layer for layer II stellate
    cells — and Reln expression is weak (Reln=1.81, cohort_pct 0.60) relative
    to the layer II candidates.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_SUPT_0053 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.35
  rationale: >
    [tier:CUT] CS20230722_SUPT_0053 (MEC layer II, Reln cohort_pct 0.98,
    region_fraction_100um=0.99) is a strong alternative MEC L2 candidate but
    lacks an annotation transfer bridge from the Yao 2021 lateral-EC source.
    Pending MEC-targeted AT or a Reln-Cre source cohort.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_SUPT_0052 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.35
  rationale: >
    [tier:CUT] CS20230722_SUPT_0052 (MEC L2/L3, region_fraction_100um=1.00,
    Reln cohort_pct 0.96) is a plausible MEC alternative candidate but has no
    AT bridge from the Yao 2021 lateral-EC subclass; pending MEC-targeted evidence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_SUPT_0051 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.35
  rationale: >
    [tier:CUT] CS20230722_SUPT_0051 (MEC L2, region_fraction_100um=0.91,
    Reln cohort_pct 0.97) is a plausible MEC alternative; no AT bridge from
    Yao 2021 lateral-EC source.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_SUPT_0010 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0010 sits in lateral EC layer 5
    (region_fraction_100um=0.86) — wrong cortical layer — with weak Reln
    (Reln=1.54, cohort_pct 0.62).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_stellate_cell_hippocampus_to_CS20230722_SUPT_0068 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0068 sits in MEC layer 5 (medial EC dorsal
    zone L5; region_fraction_100um=0.71) — wrong cortical layer for layer II
    stellate cells — despite moderate Reln (Reln=8.50).
```
<!-- verdict-block-end -->
