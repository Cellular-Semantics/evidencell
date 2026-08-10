# Arcuate aromatase neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

The arcuate aromatase neuron is a sexually dimorphic, male-biased neurochemical population defined by expression of *Cyp19a1* (aromatase) within the arcuate hypothalamic nucleus, located adjacent to kisspeptin neurons. Wartenberg and colleagues identified this population as part of a broader aromatase neuronal network of roughly 6000 neurons spanning the hypothalamus and amygdala, with the arcuate cluster becoming sexually dimorphic by birth and contributing to local estrogenic regulation of kisspeptin neuron activity [1].

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Arcuate hypothalamic nucleus [MBA:223] | [1] |
| Defining markers | Cyp19a1 | [1] |
| NT type | not asserted | — |
| Negative markers | none documented | — |
| Neuropeptides | none documented | — |
| Sex bias | male-biased dimorphism | [1] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** asta_report · *Mus musculus* · [1]
  > We identified an aromatase neuronal network comprising 6000 neurons in the hypothalamus and amygdala. By birth, this network has become sexually dimorphic in a cluster of aromatase neurons in the arcuate nucleus adjacent to kisspeptin neurons. We demonstrate that male arcuate aromatase neurons convert testosterone to estrogen to regulate kisspeptin neuron activity.
  > — Wartenberg et al. 2021, Neuronal Markers and Molecular Characteristics · [1] <!-- quote_key: 237626479_5aec04ab -->
- **Defining marker Cyp19a1:** asta_report · *Mus musculus* · [1] (same quote as above)

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

A complete scan of CCN20230722 candidates at supertype (rank 1) and cluster (rank 0) ranks within MBA:223 (arcuate hypothalamic nucleus) found no atlas node carrying *Cyp19a1* as a defining marker or with atlas-side expression evidence at this resolution. The previously proposed best Cyp19a1-expressing candidate at the supertype level, 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486], is located in periventricular preoptic zones (PVpo, MPN, AVPV) rather than the arcuate nucleus and is no longer in the current Stage A top-50 at rank 1 (see candidates table). All remaining candidates for the arcuate aromatase neuron are anatomically plausible ARH or peri-ARH residents but lack atlas-side *Cyp19a1* expression data, so the mapping is currently UNCERTAIN across the cohort.

### 0427 ARH-PVi Six6 Dopa-Gaba_1 [CS20230722_SUPT_0427] · ⚪ UNCERTAIN

The canonical ARH-PVi GABAergic supertype with dopamine cotransmission. It is one of the few survey-cohort supertypes whose painted soma distribution centres on the arcuate nucleus (region_fraction_100um: 0.741; strict region_fraction: 0.427), making it the strongest anatomical candidate among ARH residents. However, *Cyp19a1* is absent from Stage A expression detail and from the precomputed expression panel on this supertype, so the defining marker cannot be checked.

**Table 1 — Property comparison (CS20230722_SUPT_0427).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Arcuate hypothalamic nucleus [MBA:223] | MBA:223 cells present (region_fraction_100um=0.741) | best child CLUS_1571 region_fraction_100um=0.690 | CONSISTENT |
| NT type | not asserted | not asserted | Dopa (child CLUS_1569/1570/1571) | NOT_ASSESSED |
| Cyp19a1 expression | defining marker | no atlas expression data | no atlas expression data | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas region match | Atlas metadata | PARTIAL | region_fraction_100um=0.741 | atlas-internal |

*(3 of the supertype's child clusters in this cohort — CLUS_1569, CLUS_1570, CLUS_1571 — show MBA:223 cells in their painted distributions; none have Cyp19a1 atlas expression data. Best child by strict region_fraction: CLUS_1569, region_fraction=0.526.)*

**Supporting evidence**
- Atlas metadata locates a substantial fraction of this supertype's soma in or near MBA:223 (region_fraction_100um=0.741; strict region_fraction=0.427); region_evidence: SELF.

**Marker evidence provenance**
- *Cyp19a1* on the classical node is anchored to a single primary citation [1]. Aromatase is documented at the level of immunohistochemistry and reporter mouse work in that paper; the transcript-level signal for the arcuate cluster has not been quantified in WMBv1 at this resolution. The atlas precomputed expression panel does not carry *Cyp19a1* for this supertype, so the property cannot be cross-checked here. Targeted query of the precomputed expression HDF5 for *Cyp19a1* across ARH supertypes is the natural next step.

**Concerns**
- *Cyp19a1* expression on this supertype is unknown (NOT_ASSESSED). Without atlas-side aromatase data, anatomical concordance is necessary but not sufficient.
- The supertype's transmitter annotation (Dopa) is consistent with the well-described ARH-PVi dopaminergic population; the classical aromatase node has no NT assertion, so this is an open property rather than a contradiction.

**What would upgrade confidence**
- Query *Cyp19a1* expression in the precomputed HDF5 stats for SUPT_0427, neighbouring ARH supertypes (SUPT_0428, SUPT_0495), and their child clusters. If *Cyp19a1* is detectable in any ARH supertype, that supertype should be tested as the primary candidate.

### 0495 ARH-PVp Tbx3 Gaba_3 [CS20230722_SUPT_0495] · ⚪ UNCERTAIN

A large arcuate-and-periventricular-posterior GABAergic supertype (n_cells = 1460) with the highest arcuate proximity in the survival cohort (region_fraction_100um: 0.917; strict region_fraction: 0.665). The Tbx3 lineage is well-documented in the posterior arcuate, and the soma distribution centres tightly on MBA:223. As with the other candidates, the atlas precomputed expression panel does not record *Cyp19a1*, so the defining marker is unassessed.

**Table 1 — Property comparison (CS20230722_SUPT_0495).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Arcuate hypothalamic nucleus [MBA:223] | MBA:223 cells present (region_fraction_100um=0.917; n_arc≈472) | not assessed | CONSISTENT |
| NT type | not asserted | not asserted | not assessed | NOT_ASSESSED |
| Cyp19a1 expression | defining marker | no atlas expression data | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas region match | Atlas metadata | PARTIAL | region_fraction_100um=0.917 | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Supporting evidence**
- The painted soma distribution is dominated by MBA:223 and immediately adjacent hypothalamic / VMH cells; this is the tightest arcuate-proximity candidate in the survival cohort.

**Concerns**
- *Cyp19a1* expression on this supertype is unknown; the candidate's biological plausibility rests on anatomy alone.
- Tbx3-defined posterior arcuate populations are typically associated with feeding-related circuitry (POMC / AgRP neighbourhoods) rather than with neurosteroid biosynthesis in the published literature available here. Anatomical proximity does not by itself imply a Cyp19a1-positive identity.

**What would upgrade confidence**
- Query *Cyp19a1* expression in the precomputed HDF5 stats for SUPT_0495 and its child clusters. A non-trivial expression value would substantially strengthen the case; near-zero would effectively refute it.

### 1569 ARH-PVi Six6 Dopa-Gaba_1 [CS20230722_CLUS_1569] · ⚪ UNCERTAIN

The leading child cluster of SUPT_0427 by strict arcuate-region fraction (region_fraction_100um: 0.789; strict region_fraction: 0.526), with Dopa as the assigned transmitter. Of all the candidates in the current top-K, this is the cluster-rank node whose painted distribution is most concentrated in MBA:223. Like the parent supertype, it carries no atlas-side *Cyp19a1* expression, so the call remains UNCERTAIN.

**Table 1 — Property comparison (CS20230722_CLUS_1569).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Arcuate hypothalamic nucleus [MBA:223] | SUPT_0427 region_fraction_100um=0.741 | region_fraction_100um=0.789 | CONSISTENT |
| NT type | not asserted | not asserted | Dopa | NOT_ASSESSED |
| Cyp19a1 expression | defining marker | no atlas expression data | no atlas expression data | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas region match | Atlas metadata | PARTIAL | region_fraction_100um=0.789 | atlas-internal |

**Supporting evidence**
- Cluster-level painted distribution centres on MBA:223 (region_fraction_100um=0.789; strict region_fraction=0.526), the highest strict arcuate fraction among the top-K cluster-rank candidates.
- Sibling clusters in the same supertype (CLUS_1570, CLUS_1571) show similar but less concentrated arcuate occupancy, consistent with a coherent ARH-PVi Dopa-Gaba child set whose best ARH representative is CLUS_1569.

**Concerns**
- *Cyp19a1* not represented in atlas expression data at cluster level.
- The Six6-Dopa-Gaba transcriptomic identity is canonical for the ARH-PVi dopaminergic population (the tubero-infundibular dopamine neurons that regulate prolactin), which is biologically distinct from the aromatase neurons reported by Wartenberg et al. as adjacent to kisspeptin neurons. Cluster-level anatomical proximity therefore does not imply identity with the classical aromatase population.

**What would upgrade confidence**
- Cross-check *Cyp19a1* in the precomputed HDF5 for CLUS_1569 and its siblings.
- Examine whether any ARH cluster outside the current top-K (notably any Kiss1-adjacent cluster) carries *Cyp19a1*; the classical type is reported as adjacent to kisspeptin neurons, so a Kiss1-neighbouring cluster is a higher-priority candidate than the ARH-PVi Dopa-Gaba set if such a cluster exists.

---

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0427 ARH-PVi Six6 Dopa-Gaba_1 [CS20230722_SUPT_0427] | — | 659 | ⚪ UNCERTAIN | ARH proximity, no Cyp19a1 data | Primary |
| 0495 ARH-PVp Tbx3 Gaba_3 [CS20230722_SUPT_0495] | — | 1460 | ⚪ UNCERTAIN | Highest ARH proximity, no Cyp19a1 data | Secondary |
| 1569 ARH-PVi Six6 Dopa-Gaba_1 [CS20230722_CLUS_1569] | 0427 ARH-PVi Six6 Dopa-Gaba_1 | 176 | ⚪ UNCERTAIN | Best ARH cluster fraction, no Cyp19a1 data | Secondary |
| 1570 ARH-PVi Six6 Dopa-Gaba_1 [CS20230722_CLUS_1570] | 0427 ARH-PVi Six6 Dopa-Gaba_1 | 204 | ⚪ UNCERTAIN | ARH sibling cluster, no Cyp19a1 data | Eliminated (sibling of CLUS_1569, lower ARH fraction) |
| 1571 ARH-PVi Six6 Dopa-Gaba_1 [CS20230722_CLUS_1571] | 0427 ARH-PVi Six6 Dopa-Gaba_1 | 279 | ⚪ UNCERTAIN | ARH sibling cluster, no Cyp19a1 data | Eliminated (sibling of CLUS_1569, lower ARH fraction) |
| 1683 SBPV-PVa Six6 Satb2 Gaba_1 [CS20230722_CLUS_1683] | 0453 SBPV-PVa Six6 Satb2 Gaba_1 | 268 | ⚪ UNCERTAIN | SBPV/PVa, not ARH-centred | Eliminated (off-region, SBPV-PVa) |
| 5303 VLMC NN_4 [CS20230722_CLUS_5303] | 1190 VLMC NN_4 | 76 | ⚪ UNCERTAIN | Vascular leptomeningeal, not neuronal | Eliminated (non-neuronal) |
| 1190 VLMC NN_4 [CS20230722_SUPT_1190] | — | 76 | ⚪ UNCERTAIN | Vascular leptomeningeal supertype | Eliminated (non-neuronal) |
| 1173 Tanycyte NN_2 [CS20230722_SUPT_1173] | — | 896 | ⚪ UNCERTAIN | Tanycyte, not neuronal | Eliminated (non-neuronal) |
| 1174 Tanycyte NN_3 [CS20230722_SUPT_1174] | — | 41 | ⚪ UNCERTAIN | Tanycyte, not neuronal | Eliminated (non-neuronal) |
| 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] | — | 933 | ⚪ UNCERTAIN | CLUS_1907 child carries Cyp19a1 (defining), but soma in periventricular preoptic | Eliminated (off-region; outside current Stage A top-50) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The arcuate aromatase neuron is a CLASSICAL_NEUROCHEMICAL node defined by *Cyp19a1* (aromatase) expression in the arcuate hypothalamic nucleus [MBA:223], with male-biased sexual dimorphism. The single primary citation is Wartenberg et al. 2021 [1], which characterised the aromatase network across hypothalamus and amygdala using reporter mouse and immunohistochemistry, and identified the arcuate aromatase cluster as adjacent to kisspeptin neurons. No NT type, negative markers, or neuropeptides are asserted on the classical node.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match within MBA:223, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:14:09+00:00 from [kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_arc_aromatase_neuron_to_CS20230722_SUPT_0427 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_arc_aromatase_neuron_to_CS20230722_SUPT_0495 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_arc_aromatase_neuron_to_CS20230722_CLUS_1569 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_arc_aromatase_neuron_to_CS20230722_CLUS_1570 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_arc_aromatase_neuron_to_CS20230722_CLUS_1571 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_arc_aromatase_neuron_to_CS20230722_CLUS_1683 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_arc_aromatase_neuron_to_CS20230722_CLUS_5303 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_arc_aromatase_neuron_to_CS20230722_SUPT_1190 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_arc_aromatase_neuron_to_CS20230722_SUPT_1173 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_arc_aromatase_neuron_to_CS20230722_SUPT_1174 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_arc_aromatase_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA | WEAK | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Arcuate aromatase neuron → 0427 ARH-PVi Six6 Dopa-Gaba_1 [CS20230722_SUPT_0427] at UNCERTAIN confidence. Key support: arcuate region match in atlas metadata (region_fraction_100um=0.741). Key caveats: *Cyp19a1* is the defining marker for the classical type but is absent from the WMBv1 precomputed expression panel at supertype and cluster level for every ARH candidate in the current top-K, so the diagnostic marker cannot be checked. The Six6-Dopa-Gaba transcriptomic identity is canonical for the tubero-infundibular dopaminergic neurons of the ARH-PVi rather than for an aromatase population, so anatomy alone is not enough to commit to this mapping.

No Cell Ontology term currently assigned. This type is a candidate for CL contribution: a sexually dimorphic, *Cyp19a1*-positive arcuate neuron with documented neurosteroidogenic function (testosterone → estrogen) and a male-biased cell count.

### Proposed experiments and follow-ups

- **What:** Query *Cyp19a1* expression in the WMBv1 precomputed expression HDF5 for all ARH-region (MBA:223) supertypes and their child clusters, including SUPT_0427, SUPT_0428, SUPT_0495 and any Kiss1-neighbouring ARH cluster.
  **Target:** identify any ARH cluster with non-trivial *Cyp19a1* mean expression.
  **Expected output:** atlas-internal expression record on candidate clusters; potential reassignment of primary candidate.
  **Resolves:** open question 1; underpins all UNCERTAIN→stronger confidence transitions in this report.

- **What:** Re-assess the legacy edge to SUPT_0486 (PVpo-VMPO-MPN Hmx2 Gaba_5), whose child CLUS_1907 carries *Cyp19a1* as a defining marker. The supertype is in periventricular preoptic zones, not ARH, but the *Cyp19a1*-positive child is the only direct atlas marker signal for aromatase in this graph.
  **Target:** decide whether CLUS_1907 represents (a) the same pan-hypothalamic aromatase network described in the source paper [1] but lying outside the strict ARH boundary, or (b) a distinct preoptic aromatase population.
  **Expected output:** curator decision on whether SUPT_0486 belongs in a separate classical preoptic-aromatase node; refreshed property comparisons against the current Stage A top-K.
  **Resolves:** open questions 2 and 3.

- **What:** Targeted literature search for atlas-side transcriptomic studies of arcuate aromatase neurons (Wartenberg follow-ups, Mouse Whole Brain papers describing aromatase clusters, MERFISH-based ARH studies that quantify *Cyp19a1*).
  **Target:** find any independent transcriptomic confirmation of an ARH *Cyp19a1*-positive cluster.
  **Expected output:** additional LiteratureEvidence on the classical node and potentially new candidate edges.
  **Resolves:** open question 4.

### Open questions

1. Does *Cyp19a1* show detectable expression in any ARH supertype (SUPT_0427, SUPT_0428, SUPT_0495, or others) in the WMBv1 precomputed expression panel?
2. Is CLUS_1907 (the *Cyp19a1*-positive child of SUPT_0486) located exclusively in periventricular preoptic zones in MERFISH spatial data, or does it have any arcuate-region representation?
3. The legacy edge `edge_arc_aromatase_neuron_to_cs20230722_supt_0486` fell outside the current Stage A top-50 and warrants curator review — should this candidate be reinstated, retired, or migrated to a separate preoptic-aromatase classical node?
4. Does any Kiss1-neighbouring ARH cluster carry *Cyp19a1*? Wartenberg et al. [1] specify that the arcuate aromatase neurons are adjacent to kisspeptin neurons; spatial co-localisation with a Kiss1+ cluster is a strong prior for the true target.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Wartenberg et al. 2021 | [34561233](https://pubmed.ncbi.nlm.nih.gov/34561233) | soma location, defining marker, sexual dimorphism |

---

<!-- verdict-block-start: edge_arc_aromatase_neuron_to_CS20230722_SUPT_0427 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.30
  rationale: >
    [tier:STRONGEST] CS20230722_SUPT_0427 painted soma distribution centres on
    MBA:223 (region_fraction_100um: 0.741; strict region_fraction: 0.427), the
    strongest ARH-resident candidate among neuronal supertypes in the current
    top-K. The defining marker Cyp19a1 is not represented in the atlas
    precomputed expression panel for this supertype, so the diagnostic marker
    cannot be cross-checked; mapping is left as evidencell:UncertainRelationship.
  reconciliation_note: >
    Cyp19a1 absent from atlas expression panel across all ARH candidates in
    current top-K; predicate cannot be committed until atlas-side aromatase
    expression is queried (see proposed_experiments).
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        Cyp19a1 defining marker has no atlas-side expression data on
        CS20230722_SUPT_0427 or any of its child clusters in the current
        property_comparisons. The mapping rests on anatomy alone.
    - caveat_type: SINGLE_DATASET
      description: >
        Classical node arc_aromatase_neuron is supported by a single primary
        source (Wartenberg 2021, PMID:34561233); marker, location, and sex-bias
        assertions all depend on this paper.
  proposed_experiments:
    - >
      Query Cyp19a1 expression in the precomputed expression HDF5 for
      CS20230722_SUPT_0427 and its child clusters (CLUS_1569, CLUS_1570,
      CLUS_1571).
    - >
      Extend the Cyp19a1 query to all ARH-region (MBA:223) supertypes
      including the sister TIDA supertype and CS20230722_SUPT_0495 to identify any
      ARH-resident cluster with non-trivial aromatase expression.
  unresolved_questions:
    - >
      Does Cyp19a1 show detectable expression in any ARH supertype in the
      WMBv1 precomputed expression panel?
    - >
      Is there a Kiss1-neighbouring ARH cluster carrying Cyp19a1, matching
      the Wartenberg 2021 description of arcuate aromatase neurons adjacent
      to kisspeptin neurons?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_arc_aromatase_neuron_to_CS20230722_SUPT_0495 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.25
  rationale: >
    [tier:NEXT] CS20230722_SUPT_0495 has the highest arcuate proximity in the
    survival cohort (region_fraction_100um: 0.917; strict region_fraction:
    0.665), but Cyp19a1 is absent from the atlas precomputed expression
    panel for this supertype, so the defining marker is unassessed and the
    relationship cannot be committed.
  reconciliation_note: >
    Strongest pure anatomical match for MBA:223 in the cohort; lineage
    (Tbx3-defined posterior arcuate) does not by itself predict an
    aromatase-positive identity.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        Cyp19a1 has no atlas-side expression record on CS20230722_SUPT_0495;
        candidate retained on anatomical proximity alone.
    - caveat_type: OTHER
      description: >
        Tbx3-defined posterior arcuate populations are most often associated
        with feeding-circuit neurons (POMC/AgRP neighbourhood) rather than
        with neurosteroid biosynthesis; identity with Wartenberg 2021's
        Cyp19a1-positive arcuate cluster is not implied by anatomy alone.
  proposed_experiments:
    - >
      Query Cyp19a1 expression in the precomputed expression HDF5 for
      CS20230722_SUPT_0495 and its child clusters.
  unresolved_questions:
    - >
      Is the Tbx3-defined posterior arcuate population aromatase-expressing
      at any of its child clusters?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_arc_aromatase_neuron_to_CS20230722_CLUS_1569 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.25
  rationale: >
    [tier:WEAKEST] CS20230722_CLUS_1569 is the leading ARH child of
    CS20230722_SUPT_0427 by strict region_fraction (0.526;
    region_fraction_100um: 0.789) with Dopa as the assigned transmitter.
    Cyp19a1 is absent from the atlas expression panel at cluster level, and
    the Six6-Dopa-Gaba identity is canonical for the tubero-infundibular
    dopaminergic neurons rather than for an aromatase population;
    relationship remains evidencell:UncertainRelationship.
  reconciliation_note: >
    Sibling clusters CLUS_1570 and CLUS_1571 share the same supertype with
    weaker ARH fractions; CLUS_1569 is the best ARH representative of the
    set. Identity with the classical aromatase node is not supported by
    transcriptomic evidence currently available.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        Cyp19a1 has no atlas-side cluster-level expression record on
        CS20230722_CLUS_1569.
    - caveat_type: OTHER
      description: >
        Six6-Dopa-Gaba is the canonical transcriptomic identity for the
        ARH-PVi tubero-infundibular dopamine neurons; Wartenberg 2021's
        arcuate aromatase neurons are described as a distinct,
        Kiss1-adjacent population.
  proposed_experiments:
    - >
      Query Cyp19a1 expression in the precomputed expression HDF5 for
      CS20230722_CLUS_1569 and sibling clusters CS20230722_CLUS_1570 and
      CS20230722_CLUS_1571.
  unresolved_questions:
    - >
      Does CS20230722_CLUS_1569 (or any sibling in
      CS20230722_SUPT_0427) carry Cyp19a1 at detectable levels?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_arc_aromatase_neuron_to_CS20230722_CLUS_1570 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_1570 is a sibling of CS20230722_CLUS_1569 in
    the same supertype with a lower strict region_fraction (0.545 with
    region_fraction_100um: 0.779) and no Cyp19a1 atlas expression data;
    superseded by CS20230722_CLUS_1569 as the best ARH-resident child.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        Cyp19a1 not represented in atlas expression panel for
        CS20230722_CLUS_1570.
  proposed_experiments: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_arc_aromatase_neuron_to_CS20230722_CLUS_1571 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_1571 is a sibling of CS20230722_CLUS_1569 in
    the same supertype with a lower strict region_fraction (0.338) and no
    Cyp19a1 atlas expression data; superseded by CS20230722_CLUS_1569 as
    the best ARH-resident child.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        Cyp19a1 not represented in atlas expression panel for
        CS20230722_CLUS_1571.
  proposed_experiments: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_arc_aromatase_neuron_to_CS20230722_CLUS_1683 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CS20230722_CLUS_1683 (SBPV-PVa Six6 Satb2 Gaba_1) is centred
    on the suprachiasmatic preoptic and periventricular anterior zones
    rather than the arcuate (region_fraction_100um: 0.506; strict
    region_fraction: 0.346, with substantial Medial preoptic nucleus
    occupancy), and carries no Cyp19a1 atlas expression data.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        SBPV-PVa Six6 Satb2 Gaba_1 occupancy of MBA:223 is partial; primary
        soma distribution is in preoptic/periventricular zones.
  proposed_experiments: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_arc_aromatase_neuron_to_CS20230722_CLUS_5303 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_5303 (5303 VLMC NN_4) is a vascular
    leptomeningeal cluster, not a neuronal population; identity with a
    Cyp19a1-positive neurochemical arcuate neuron is excluded by cell
    class.
  caveats:
    - caveat_type: OTHER
      description: >
        VLMC NN_4 is a non-neuronal vascular leptomeningeal cluster.
  proposed_experiments: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_arc_aromatase_neuron_to_CS20230722_SUPT_1190 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_1190 (1190 VLMC NN_4) is a vascular
    leptomeningeal supertype, not a neuronal population; excluded by cell
    class.
  caveats:
    - caveat_type: OTHER
      description: >
        VLMC NN_4 supertype is non-neuronal.
  proposed_experiments: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_arc_aromatase_neuron_to_CS20230722_SUPT_1173 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_1173 (1173 Tanycyte NN_2) is a tanycyte
    supertype, not a neuronal population; identity with the arcuate
    aromatase neuron is excluded by cell class even though tanycytes
    populate MBA:223 abundantly.
  caveats:
    - caveat_type: OTHER
      description: >
        Tanycyte NN_2 is non-neuronal.
  proposed_experiments: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_arc_aromatase_neuron_to_CS20230722_SUPT_1174 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_1174 (1174 Tanycyte NN_3) is a tanycyte
    supertype, not a neuronal population; excluded by cell class.
  caveats:
    - caveat_type: OTHER
      description: >
        Tanycyte NN_3 is non-neuronal.
  proposed_experiments: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_arc_aromatase_neuron_to_cs20230722_supt_0486 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.20
  rationale: >
    [tier:CUT] CS20230722_SUPT_0486 (PVpo-VMPO-MPN Hmx2 Gaba_5) was
    previously proposed because its periventricular preoptic child cluster
    carries Cyp19a1 as a defining marker, but the supertype's painted soma
    distribution sits in PVpo/MPN/AVPV (no MBA:223 cells), and the legacy
    edge fell outside the current Stage A top-50; flagged for curator
    review.
  reconciliation_note: >
    Legacy edge from pre-emitter pass; property_comparisons not refreshed
    in current run. The Cyp19a1-positive periventricular preoptic child cluster
    may represent a separate preoptic-aromatase population rather than the
    arcuate aromatase neuron of Wartenberg 2021; curator decision needed.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        CS20230722_SUPT_0486 is in PVpo-VMPO-MPN with no MBA:223 cells in
        its painted distribution; classical type is in MBA:223.
    - caveat_type: OTHER
      description: >
        Edge fell outside current Stage A top-50 at rank 1;
        property_comparisons not refreshed in this run. Curator review
        warranted (cf. evidencell #111).
  proposed_experiments:
    - >
      Confirm whether the periventricular preoptic child cluster has any
      MBA:223 representation in MERFISH spatial data, or is exclusively in
      periventricular preoptic zones.
  unresolved_questions:
    - >
      Should CS20230722_SUPT_0486 and its periventricular preoptic child
      cluster be re-mapped to a separate preoptic-aromatase classical node
      distinct from arc_aromatase_neuron?
    - >
      Curator review of legacy edge edge_arc_aromatase_neuron_to_cs20230722_supt_0486 — fell outside current Stage A top-50 (cf. #111).
```
<!-- verdict-block-end -->
