# Basolateral amygdala calbindin-positive dendrite-targeting interneuron — CCN20230722 Mapping Report
* · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Calbindin-positive (Calb1+) dendrite-targeting interneurons of the basolateral amygdala (BLA) constitute a classically defined GABAergic cell class that selectively innervates the dendritic compartments of principal neurons. First systematically characterised by Bienvenu et al. 2012 [1], these cells are distinguished from other BLA interneuron populations by their expression of calbindin without parvalbumin co-expression, placing them outside both the PV+ basket-cell and the axo-axonic cell lineages. Their functional significance in amygdalar circuit gating makes them a biologically important target for atlas-level characterisation.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1] |
| Neurotransmitter | GABAergic | [1], [2], [3] |
| Defining marker | Calb1 (calbindin) | [1], [2], [4], [5] |
| Negative marker | Pvalb (parvalbumin) | [2] |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Calb1 (defining marker):** Immunohistochemistry; mouse BLA · [1]
  > calbindin-positive interneurons targeting dendrites
  > — Bienvenu et al. 2012, Basolateral amygdala and corticobasal cell types · [1] <!-- quote_key: 10647550_48ea3c0f -->

- **Calb1 (defining marker):** Immunohistochemistry; mouse BLA · [4]

- **Pvalb (negative marker) / GABAergic identity:** Pharmacological activation + immunohistochemistry · [2]
  > Treatment with the orexin-1 receptor antagonist SB334867 increased the activity of basolateral amygdala neurons projecting to infralimbic medial prefrontal cortex during fear extinction. GABAergic interneurons expressing calbindin, but not parvalbumin, were also activated by orexin-1 receptor antagonism in the basolateral amygdala.
  > — Flores et al. 2017, dendrite-targeting interneurons · [2] <!-- quote_key: 17860491_f1ffddb9 -->

- **GABAergic identity (supporting context):** Stereological cell-type census; mouse LA and BA · [3]

</details>

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

No candidate in the current top-K assessment reaches a confidence level sufficient to support a positive mapping call. The available CCN20230722 cluster-level data cannot resolve the classical type's defining negative-marker profile (Pvalb−, Sst−), and the single provisional candidate [0666 Sncg Gaba_1 [CS20230722_CLUS_0666]] scores identically with three Pvalb Gaba clusters under the current Calb1-only search strategy. The primary finding is therefore the boundary of current evidence: a BLA GABAergic cluster expressing high Calb1 exists in the atlas, but the transcriptomic identity of the Calb1+/Pvalb−/Sst− class cannot be confirmed without negative-marker expression data.

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0666 Sncg Gaba_1 [CS20230722_CLUS_0666] | 0185 Sncg Gaba_1 | 694 | ⚪ UNCERTAIN | Calb1 high; Pvalb/Sst status unconfirmed | Eliminated (negative markers not assessable) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Basolateral amygdala calbindin-positive dendrite-targeting interneuron is defined on a CLASSICAL basis, combining immunohistochemical identification from primary literature and functional characterisation. Defining properties: Calb1+ (protein, confirmed in mouse BLA by immunostaining [1][4]); GABAergic [1][2][3]; Pvalb− (pharmacological + immunohistochemical [2]); dendrite-targeting morphology [1]. The classical definition does not include SST, but the node notes record partial overlap with SOM/CB+ schemes in earlier work, and SST-negativity lacks an independent primary citation.

**Atlas mapping query.**
> Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.**
> Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.**
> All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_calbindin_dendrite_targeting_interneuron_to_cs20230722_clus_0666 | LITERATURE; LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT; SUPPORT | [1], [4], — |

*Generated by evidencell `bfdb7f1` at 2026-06-15T10:48:33+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats

**Primary mapping:** Basolateral amygdala calbindin-positive dendrite-targeting interneuron → no confident atlas match established at this time. The provisional top-ranked candidate 0666 Sncg Gaba_1 [CS20230722_CLUS_0666] (694 cells) carries high Calb1 expression consistent with the classical marker but cannot be validated as the correct mapping because precomputed expression data for Pvalb and Sst are absent for this cluster. Three of the five BLA GABAergic clusters that score equally (CLUS_0738, CLUS_0745, CLUS_0748) belong to the Pvalb Gaba lineage — the very population that the classical type definition explicitly excludes. A positive mapping cannot be supported until negative-marker expression data disambiguate the Calb1+ cluster landscape.

No Cell Ontology term is currently assigned to this type.

### Proposed experiments and follow-ups

1. **Precomputed expression query (HDF5).** Acquire the CCN20230722 HDF5 file and extract mean expression values for Pvalb and Sst in the five BLA GABAergic rank-0 clusters (CLUS_0666, CLUS_0668, CLUS_0738, CLUS_0745, CLUS_0748). Expected output: `ATLAS_METADATA` evidence items with Pvalb and Sst expression for each candidate; resolves which clusters are Pvalb− and Sst−. This experiment requires no new tissue — the data are atlas-internal.

2. **Multiplexed smFISH.** In mouse BLA, co-probe for Calb1 + Pvalb + Sst + Sncg. Target: identify the Calb1+/Pvalb−/Sst− cell population and link it to an atlas cluster via MapMyCells or direct transcript-level fingerprinting. Expected output: `AnnotationTransferEvidence` or `MarkerAnalysisEvidence` at CLUSTER level; threshold F1 ≥ 0.70. Resolves the non-PV, non-SST criterion that the current atlas metadata cannot enforce.

3. **Targeted cite-traverse.** Calb1 as a dendrite-targeting interneuron marker in BLA lacks a transcript-level primary citation — all current sources are protein-level (IHC). A targeted cite-traverse for "calbindin dendrite-targeting interneuron BLA mouse scRNA-seq" may identify a transcriptomic study that already maps this type and provides Pvalb/Sst co-expression data.

### Open questions

1. Is CS20230722_CLUS_0666 Pvalb-negative? Requires expression query for Pvalb from the CCN20230722 HDF5.
2. Which BLA Sncg Gaba cluster(s) express Calb1 without high Cck and without Pvalb co-expression? CLUS_0666 and CLUS_0668 are candidates but cannot be ranked without HDF5 data.
3. Does Sst-negativity of the classical type have independent primary-literature support? Ünal et al. 2020 [4] situates Calb1 within SOM+ interneurons, raising a marker-overlap ambiguity that the current node notes acknowledge but do not resolve. A targeted literature search is warranted.
4. Is the SUPT_0185 (parent of CLUS_0666) CCK signal a genuine overlap risk with the bla_cck_cb1_basket_cell type? Both CLUS_0664 (sibling) and CLUS_0666 sit under the same supertype; functional dissociation requires clarification.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Bienvenu et al. 2012 | [22726836](https://pubmed.ncbi.nlm.nih.gov/22726836/) | Soma location; defining marker Calb1; NT type |
| [2] | Flores et al. 2017 | [28453642](https://pubmed.ncbi.nlm.nih.gov/28453642/) | NT type; negative marker Pvalb |
| [3] | Vereczki et al. 2021 | [33837051](https://pubmed.ncbi.nlm.nih.gov/33837051/) | NT type |
| [4] | Ünal et al. 2020 | [32144495](https://pubmed.ncbi.nlm.nih.gov/32144495/) | Calb1 marker |
| [5] | Cardenas et al. 2019 | [31193505](https://pubmed.ncbi.nlm.nih.gov/31193505/) | Calb1 marker |

---

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_cs20230722_clus_0666 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Calb1 expression CONSISTENT (precomputed mean 10.37, cohort 98.9th pct) but
    Pvalb and Sst negativity NOT_ASSESSED for CS20230722_CLUS_0666; three of five equally
    scored rank-0 BLA GABAergic candidates are Pvalb Gaba lineage clusters. Negative-marker
    data from CCN20230722 HDF5 are required to enforce the classical type's non-PV, non-SST
    criterion before any positive mapping can be made.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        Calb1 is expressed in both Sncg and Pvalb lineages. Without precomputed expression
        for Pvalb and Sst as negative markers, discovery cannot enforce the classical type's
        non-PV, non-SST criterion. Mapping is uncertain.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Five rank-0 candidates score equally (score 3), spanning both Sncg Gaba
        (CLUS_0666/0668) and Pvalb Gaba (CLUS_0738/0745/0748) families. No single cluster
        is clearly preferred.
    - caveat_type: OTHER
      description: >
        SUPT_0185 (parent of CLUS_0666) expresses CCK at high levels (precomputed mean 10.12),
        creating potential overlap with bla_cck_cb1_basket_cell (CLUS_0664, sibling cluster
        under same supertype).
  proposed_experiments:
    - >
      Acquire HDF5 for CCN20230722 and extract Pvalb and Sst expression for BLA GABAergic
      rank-0 clusters (CLUS_0666, CLUS_0668, CLUS_0738, CLUS_0745, CLUS_0748); re-run
      discovery with negative marker scores to filter Pvalb Gaba clusters.
    - >
      Multiplexed smFISH in mouse BLA with Calb1 + Pvalb + Sst + Sncg probes to identify
      Calb1+/Pvalb-/Sst- cells and resolve their transcriptomic cluster identity.
  unresolved_questions:
    - >
      Is CS20230722_CLUS_0666 Pvalb-negative? Requires expression query for Pvalb from
      CCN20230722 HDF5.
    - >
      Which BLA Sncg Gaba cluster(s) express Calb1 without high Cck and without Pvalb
      co-expression? CLUS_0666 and CLUS_0668 are candidates but cannot be ranked without
      HDF5 data.
    - >
      Does Sst-negativity of the classical type have independent primary-literature support?
      Ünal et al. 2020 situates Calb1 within SOM+ interneurons, creating marker overlap
      ambiguity.
```
<!-- verdict-block-end -->
