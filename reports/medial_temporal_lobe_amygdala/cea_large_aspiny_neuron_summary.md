# Central amygdala large aspiny neuron — CCN20230722 Mapping Report
* · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Central amygdala large aspiny neurons are a classical morphological class of the central nucleus of the amygdala (CeA), distinguished from the better-known medium spiny neurons by their large soma and thick aspiny primary dendrites [1]. Like all CeA neurons, they are GABAergic [2][3][4][5][6][7] — the CeA as a whole is organised along striatum-like lines with a predominance of inhibitory projection neurons. Mapping this morphological class to a transcriptomic atlas cluster matters because the CeA is the primary output station of the amygdala for fear and threat responses, and precise circuit dissection requires linking classical anatomical cell types to the molecular profiles now available in single-cell and MERFISH datasets. At present, no molecular markers have been established for the large aspiny class, which severely limits the ability to anchor it in any transcriptomic atlas.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Central nucleus of the amygdala [UBERON:0002883] | [1][2] |
| NT type | GABAergic | [2][3][4][5][6][7] |
| Morphology | Large soma, thick aspiny primary dendrites; seldom-spiny secondary processes | [1] |
| Defining molecular markers | None established | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / Morphology:** Nikolenko et al. 2020 · [1]
  > Morphologically, there are several types of neurons located in the central nucleus of the amygdala (CeA). In the lateral sector of the central nucleus, a predominant cell type with ovoid soma is located. These cells have several primary nonspiny dendrites, branching onto spiny secondary and tertiary dendrite. Their axons begin branching even before leaving the nucleus, which is why these cells are called "medium spiny neurons" (Hall, 2004)(McDonald, 1982). Another type of neurons located in the central nuclei have big soma with thick aspiny dendrites, branching on to secondary seldom spiny processes (McDonald, 1982)(Cassell et al., 1989) (Schiess et al., 1999). The third type of cells are small aspiny neurons (Cassell et al., 1989)
  > — Nikolenko et al. 2020, Central amygdala cell types · [1] <!-- quote_key: 220976356_f1fe3fe1 -->

- **NT type:** Waclaw et al. 2010 · [2]

- **NT type:** Yeh et al. 2024 · [3]

- **NT type:** Paul et al. 2025 · [4]

- **NT type:** Sarowar & Grabrucker 2020 · [5]

- **NT type:** Chung et al. 2016 · [6]

- **NT type:** Hochgerner et al. 2023 · [7]

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

The current evidence base is insufficient to support any specific atlas cluster assignment for the central amygdala large aspiny neuron. No molecular markers are defined for this morphological class, and every candidate in the GABAergic CeA cohort received an identical discovery score of 1 — the bottom of the scoring range — because region co-localisation was the only evaluable criterion. Under these conditions the candidate set is entirely uninformative: the same five clusters would be ranked identically for any of the three CeA morphological classes (large aspiny, medium spiny, small aspiny). The sole candidate carried forward by the atlas query — 0705 RHP-COA Ndnf Gaba_6 [CS20230722_CLUS_0705] — was selected by region filter only, with no supporting marker overlap, and is assigned NO_EVIDENCE support.

The null finding is the primary result. A validated mapping requires molecular data that does not yet exist for this morphological class.

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0705 RHP-COA Ndnf Gaba_6 [CS20230722_CLUS_0705] | 0198 RHP-COA Ndnf Gaba_6 | 61 | ⚪ UNCERTAIN | No markers; region filter only | Eliminated (no molecular anchor) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The central amygdala large aspiny neuron is defined on a CLASSICAL morphological basis: large soma with thick, primarily aspiny dendrites, as described by McDonald 1982, Cassell et al. 1989, and Schiess et al. 1999 (referenced in Nikolenko et al. 2020 [1]). The definition_basis is CLASSICAL and no molecular markers are currently attached to this node. Neurotransmitter identity (GABAergic) is established by multiple independent studies [2][3][4][5][6][7]; the CeA as a whole is a GABAergic structure with striatum-like projection neurons.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 0 (cluster) using metadata-based scoring (region match MBA:536, NT type GABAergic). Full scoring rules: `workflows/map-cell-type.md`. Only five candidates survived the region + NT filter (cohort size = 5). All received a discovery score of 1, indicating no marker overlap contributed any additional signal.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. NT type alignment for CLUS_0705 is CONSISTENT (GABA vs. GABAergic). Soma location alignment is CONSISTENT on the nominal criterion (CeA present) but the region_fraction for CLUS_0705 is 0.014, reflecting a very small fraction of this cluster's cells in the queried region. Morphology is NOT_ASSESSED — WMBv1 does not provide morphological descriptors at the cluster level.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cea_large_aspiny_neuron_to_cs20230722_clus_0705 | LITERATURE; ATLAS_METADATA | PARTIAL; NO_EVIDENCE | [1]; — |

*Generated by evidencell `bfdb7f1` at 2026-06-15T10:48:33+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Central amygdala large aspiny neuron → no assignable cluster at current evidence level. The single candidate assessed — 0705 RHP-COA Ndnf Gaba_6 [CS20230722_CLUS_0705] — was retrieved on region and NT criteria only; no molecular markers distinguish this morphological class from the other two CeA morphological classes (medium spiny, small aspiny), and the candidate carries NO_EVIDENCE support. The mapping is genuinely UNCERTAIN and cannot be resolved without new molecular data.

No Cell Ontology term is currently assigned. The large aspiny CeA neuron is a candidate for CL contribution once molecular markers are established.

### Proposed experiments and follow-ups

**Patch-seq of morphologically identified large aspiny CeA neurons**
- **What:** Patch-clamp recording followed by single-cell RNA sequencing (patch-seq) on neurons in the lateral CeA confirmed post-hoc as large aspiny by biocytin fill and morphological reconstruction.
- **Target:** Transcriptome sufficient for MapMyCells atlas assignment; F1 ≥ 0.60 at CLUSTER level in CCN20230722 would constitute positive evidence.
- **Expected output:** AnnotationTransferEvidence on the cluster edge, defining_markers on the classical node.
- **Resolves:** Open question 1 (electrophysiological class identity); breaks the marker-ambiguity deadlock shared with cea_medium_spiny_neuron and cea_small_aspiny_neuron.

**Targeted molecular profiling — fast-spiking interneuron marker screen**
- **What:** Literature trawl and targeted immunohistochemistry / smFISH for fast-spiking interneuron markers (Pvalb, Kcnc1, Kcnc2) on morphologically confirmed large aspiny CeA neurons. The electrophysiological heterogeneity reported for this class raises the possibility that a subset corresponds to fast-spiking internuncial neurons.
- **Target:** Establish or exclude Pvalb/Kcnc1/Kcnc2 as positive or negative markers; confirm or refute putative overlap with atlas Pvalb-class clusters.
- **Expected output:** LiteratureEvidence or MarkerAnalysisEvidence entries on the classical node; updated property_comparisons on candidate edges.
- **Resolves:** Open question 1.

### Open questions

1. Do large aspiny CeA neurons correspond to the fast-spiking internuncial class described electrophysiologically, and if so, do they share markers with Pvalb or other known fast-spiking interneuron clusters? This question appears on the sole assessed edge and is the primary blocker for atlas assignment.
2. Are the three classical CeA morphological classes (large aspiny, medium spiny, small aspiny) distinguishable at the transcriptomic level at all? If they share molecular identity (as implied by their shared striatal-like GABAergic character), they may resolve to overlapping atlas clusters — a finding with implications for how all three nodes are curated.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Nikolenko et al. 2020 | [32751957](https://pubmed.ncbi.nlm.nih.gov/32751957/) | soma location, morphology |
| [2] | Waclaw et al. 2010 | [20484636](https://pubmed.ncbi.nlm.nih.gov/20484636/) | soma location, NT type |
| [3] | Yeh et al. 2024 | [38419794](https://pubmed.ncbi.nlm.nih.gov/38419794/) | NT type |
| [4] | Paul et al. 2025 | [40686779](https://pubmed.ncbi.nlm.nih.gov/40686779/) | NT type |
| [5] | Sarowar & Grabrucker 2020 | [32858950](https://pubmed.ncbi.nlm.nih.gov/32858950/) | NT type |
| [6] | Chung et al. 2016 | [27053114](https://pubmed.ncbi.nlm.nih.gov/27053114/) | NT type |
| [7] | Hochgerner et al. 2023 | [37884748](https://pubmed.ncbi.nlm.nih.gov/37884748/) | NT type |

---

<!-- verdict-block-start: edge_cea_large_aspiny_neuron_to_cs20230722_clus_0705 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] No molecular markers are defined for the central amygdala large aspiny
    neuron; the sole candidate CS20230722_CLUS_0705 was selected by region filter
    only (region_fraction 0.014; GABAergic NT CONSISTENT) with ATLAS_METADATA
    support=NO_EVIDENCE and LITERATURE support=PARTIAL (classical soma-size
    description only, no transcriptomic data). Discovery score 1 (rank 2 of 5;
    cohort_size 5; all cohort members tied at score 1). Mapping is entirely
    uninformative without defining markers.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        No molecular markers defined for cea_large_aspiny_neuron. Discovery
        returned score 1 for all candidates. Mapping is entirely uninformative.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Identical candidate pool to cea_medium_spiny_neuron and
        cea_small_aspiny_neuron; three classical CeA soma-type classes are
        indistinguishable without markers.
  proposed_experiments:
    - >
      Single-cell transcriptomics of large aspiny CeA neurons identified
      by soma size and aspiny dendritic architecture, with post-recording
      cellular labeling for cell-type confirmation and WMBv1 cluster
      assignment. Target: F1 >= 0.60 at CLUSTER level in CCN20230722.
  unresolved_questions:
    - >
      Do large aspiny CeA neurons correspond to the fast-spiking internuncial
      class described electrophysiologically, and if so, do they share markers
      with Pvalb or other known fast-spiking interneuron clusters?
    - >
      Are the three classical CeA soma-type classes (large aspiny, medium
      spiny, small aspiny) distinguishable at the transcriptomic level? They
      may resolve to overlapping atlas clusters given their shared GABAergic
      striatal-like character.
```
<!-- verdict-block-end -->
