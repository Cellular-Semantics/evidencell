# Basolateral amygdala calbindin-positive dendrite-targeting interneuron — CCN20230722 Mapping Report
*Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala (BLA) calbindin-positive dendrite-targeting interneuron is a classically defined GABAergic cell type characterised by expression of the calcium-binding protein calbindin-1 (Calb1) and a dendritic targeting axon arborisation. Bienvenu et al. 2012 identified this as one of four distinct interneuron classes in the BLA — alongside PV+ basket cells, axo-axonic cells, and AStria-projecting cells — based on in-vivo juxtacellular labelling combined with post-hoc immunohistochemistry [1]. Mapping this type to the WMBv1 transcriptomic atlas is important for linking classical physiology-based classification to molecular cluster identity, but is currently blocked by the non-specificity of the sole available positive marker (Calb1) in the absence of negative-marker data.

**Primary null-result finding:** A complete scan of CCN20230722 BLA GABAergic clusters (rank 0; n=5 cohort members) confirmed that Calb1 alone cannot resolve this cell type to a single atlas cluster. Five rank-0 candidates score identically (score 3), spanning both Sncg Gaba (CLUS_0666, CLUS_0668) and Pvalb Gaba (CLUS_0738, CLUS_0745, CLUS_0748) lineages. Without negative-marker data for Pvalb and Sst, the mapping remains UNCERTAIN.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1] |
| NT type | GABAergic | [1] |
| Defining marker | Calb1 (calbindin-1; protein-level) | [1], [2] |
| Neuropeptides | None documented | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / GABAergic NT / Calb1 defining marker / dendrite-targeting morphology:** in-vivo juxtacellular labelling and post-hoc immunohistochemistry · BLA · [1]
  > calbindin-positive interneurons targeting dendrites
  > — Bienvenu et al. 2012, Basolateral amygdala and corticobasal cell types · [1] <!-- quote_key: 10647550_48ea3c0f -->

- **Calb1 marker / SOM co-expression context:** review · mouse lateral amygdala · [2]
  > SOM positive interneurons constitute the other common interneuron population and they co-express markers such as neuropeptide Y (NPY) and calbindin
  > — Ünal et al. 2020, Introduction · [2] <!-- quote_key: 212579559_81debee5 -->

  *(note: This quote establishes that calbindin co-expression occurs in SOM+ interneurons — a key biological context explaining why Calb1 alone cannot discriminate the classical Calb1+/SST- dendrite-targeting type from SOM+/Calb1+ populations or their transcriptomic correlates.)*

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed: 0666 Sncg Gaba_1 [CS20230722_CLUS_0666]. The edge carries `evidencell:UncertainRelationship` at UNCERTAIN confidence because Calb1 expression is not lineage-specific in the BLA GABAergic cohort — three of five equal-scoring rank-0 candidates are Pvalb Gaba clusters, and the essential negative markers (Pvalb, Sst) are unassessed at the cluster level.

### Mapping candidates overview

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | 0666 Sncg Gaba_1 [CS20230722_CLUS_0666] | 0185 Sncg Gaba_1 | 694 | ⚪ UNCERTAIN | Calb1 CONSISTENT; Pvalb/Sst NOT_ASSESSED | Eliminated |

*1 edge assessed; relationship: `evidencell:UncertainRelationship`.*

## Eliminated candidates

All edges for this node carry UNCERTAIN confidence. The shared disqualifying signal is **non-specificity of Calb1 as the sole discriminating marker**: Calb1 is expressed at high levels in both Sncg-lineage and Pvalb-lineage GABAergic clusters in the BLA. Without negative-marker confirmation (Pvalb, Sst), the classical Calb1+/PV-/SST- definition cannot be enforced against the transcriptomic atlas.

### 0666 Sncg Gaba_1 [CS20230722_CLUS_0666] — ⚪ UNCERTAIN

**Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | GABA | CONSISTENT |
| Soma location | Basolateral amygdala [UBERON:0002887] | not available | MBA:295 present; region_fraction 0.10 (cohort rank 1 of 5 BLA GABAergic) | CONSISTENT |
| Calb1 expression | Calb1 — defining marker (protein; [1], [2]) | not available | mean_expression 10.37; 98.9th pct of BLA GABAergic cohort (applied_score 2.0) | CONSISTENT |
| Pvalb (implicit negative) | Pvalb-negative (non-PV dendrite-targeting cell) | not available | NOT_ASSESSED — Sncg Gaba_1 lineage label circumstantially consistent but unconfirmed; three rank-0 tied candidates are Pvalb Gaba clusters | NOT_ASSESSED |
| Sst (implicit negative) | Sst-negative per node notes | not available | NOT_ASSESSED — Sst not in precomputed expression data for CLUS_0666 | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Bienvenu 2012 BLA interneuron characterisation | Literature | SUPPORT | IHC + in-vivo ephys; confirms Calb1+ dendrite-targeting class in BLA | [1] |
| Ünal 2020 LA interneuron review | Literature | SUPPORT | Calb1 protein confirmed in mouse lateral amygdala; SOM co-expression noted | [2] |
| WMBv1 atlas precomputed expression — CLUS_0666 | Atlas metadata | SUPPORT | Calb1 mean 10.37; BLA cohort 98.9th pct; five rank-0 candidates score equally | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Disqualifying evidence**

- Calb1 mean_expression 10.37 (BLA GABAergic cohort 98.9th pct) is CONSISTENT with the defining marker but not discriminating: three of five rank-0 BLA GABAergic candidates (CLUS_0738, CLUS_0745, CLUS_0748) are Pvalb Gaba clusters scoring identically (discovery score 3, cohort_size 5).
- Pvalb (negative marker) is NOT_ASSESSED: Pvalb expression data absent from precomputed stats for CLUS_0666; the Sncg lineage label is circumstantially consistent with Pvalb-negativity but is not a direct measurement. *(note: In WMBv1, Sncg and Pvalb lineages are largely non-overlapping at the supertype level, so CLUS_0666's Sncg lineage membership reduces the prior probability of PV+ identity — but this is an atlas taxonomy inference, not direct expression data.)*
- Sst (negative marker) is NOT_ASSESSED: Sst not in precomputed expression data for CLUS_0666.
- CCK co-expression caveat: the parent supertype SUPT_0185 expresses Cck at high levels (precomputed mean 10.12), creating potential overlap with the bla_cck_cb1_basket_cell (sibling cluster CLUS_0664 under SUPT_0185). Whether CLUS_0666 specifically drives this CCK signal is unresolved.
- region_fraction = 0.10: only 10% of CLUS_0666 cells are in MBA:295 (BLA). This value is below the boundary band (0.3–0.7) and does not by itself disqualify the match given the small cohort of five BLA GABAergic clusters, but it indicates CLUS_0666 is not a BLA-restricted population.

**What would upgrade confidence**

1. **Acquire CCN20230722 HDF5 and query Pvalb/Sst expression in CLUS_0666** — if Pvalb ≤ MIN_DETECTABLE and Sst ≤ MIN_DETECTABLE, negative-marker comparisons would flip from NOT_ASSESSED to CONSISTENT, enabling a confidence upgrade to LOW and elimination of CLUS_0738/0745/0748 from the candidate pool.
2. **Annotation transfer (MapMyCells)** using a Calb1+/Pvalb-/Sst- BLA source population against CCN20230722; target F1 ≥ 0.70 at CLUSTER level; expected output: AnnotationTransferEvidence.
3. **Multiplexed smFISH in mouse BLA** with Calb1 + Pvalb + Sst + Sncg probes to directly identify the Calb1+/Pvalb-/Sst- cell population and correlate with Sncg expression.
4. **Targeted cite-traverse** for "calbindin Sst BLA interneuron" to find primary data confirming Calb1+/Sst- co-expression — the Ünal et al. [2] context introduces SOM/Calb1 marker overlap ambiguity that a primary study should resolve.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The BLA calbindin dendrite-targeting interneuron is defined on a CLASSICAL basis (`definition_basis: CLASSICAL`), drawing on in-vivo juxtacellular labelling and post-hoc immunohistochemistry from Bienvenu et al. 2012 [1] and a review by Ünal et al. 2020 [2]. The defining marker is Calb1 (protein level; [1], [2]). NT type is GABAergic [1]. Soma location is basolateral amygdala [UBERON:0002887] [1]. Negative markers (Pvalb, Sst) are implicit in the classical type's definition and are not positively sourced to individual publications in the current KB entry.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 0 (cluster) using metadata-based scoring (region match MBA:295, NT type GABAergic, defining marker Calb1). Full scoring rules: `workflows/map-cell-type.md`. Five BLA GABAergic clusters scored equally (score 3); CLUS_0666 was selected as the representative candidate.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values for Calb1 came from precomputed expression in the CCN20230722 taxonomy reference store. Negative markers (Pvalb, Sst) could not be assessed because precomputed expression data for these genes in CLUS_0666 was not available (HDF5 stats file not accessible at gen-facts time).

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_calbindin_dendrite_targeting_interneuron_to_cs20230722_clus_0666 | LITERATURE; LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT; SUPPORT | [1]; [2]; atlas-internal |

*Generated by evidencell `8d79cdb` at 2026-06-11T09:44:17+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala calbindin-positive dendrite-targeting interneuron → 0666 Sncg Gaba_1 [CS20230722_CLUS_0666] at UNCERTAIN confidence. Key support: Calb1 precomputed expression at BLA GABAergic cohort 98.9th percentile (applied_score 2.0; CONSISTENT); GABAergic NT type (CONSISTENT); BLA soma location (CONSISTENT). Key caveats: NO_DISCRIMINATING_MARKER (Calb1 is expressed in both Sncg and Pvalb lineages; three of five equally scoring rank-0 candidates are Pvalb Gaba clusters); DISTRIBUTED_ACROSS_CLUSTERS (five rank-0 candidates score identically; no single cluster is preferred); Pvalb and Sst negative-marker assessments are NOT_ASSESSED due to absent precomputed expression data.

No Cell Ontology term currently assigned. The node notes indicate overlap with SOM/CB+ interneurons in older marker schemes; a CL term request is warranted once transcriptomic identity is resolved.

### Proposed experiments and follow-ups

#### 1. CCN20230722 HDF5 — negative-marker scoring for Pvalb and Sst

- **What:** Query CCN20230722 HDF5 for Pvalb and Sst expression in all rank-0 BLA GABAergic candidates; re-run `just find-candidates` with negative-marker scoring enabled.
- **Target:** Pvalb ≤ MIN_DETECTABLE in CLUS_0666; Sst ≤ MIN_DETECTABLE in CLUS_0666; Pvalb Gaba clusters (CLUS_0738, CLUS_0745, CLUS_0748) demoted by negative-marker penalty.
- **Expected output:** Revised `property_comparisons` with `negative_marker_Pvalb` and `negative_marker_Sst` CONSISTENT; confidence upgrade to LOW if Sncg lineage confirmed Pvalb-negative.
- **Resolves:** Open questions 1 and 2; caveat NO_DISCRIMINATING_MARKER.

#### 2. Annotation transfer (MapMyCells)

- **What:** Run MapMyCells against CCN20230722 using a published BLA interneuron scRNA-seq or Patch-seq dataset with Calb1+/Pvalb-/Sst- source cells.
- **Target:** F1 ≥ 0.70 at CLUSTER level for a single Sncg Gaba cluster.
- **Expected output:** AnnotationTransferEvidence on `edge_bla_calbindin_dendrite_targeting_interneuron_to_cs20230722_clus_0666`; confidence upgrade from UNCERTAIN to LOW (AT alone) or MODERATE (AT + negative-marker confirmation).
- **Resolves:** Open questions 1 and 2; predicate potentially upgradeable to `skos:closeMatch`.

#### 3. Multiplexed smFISH in mouse BLA

- **What:** RNAscope or MERFISH in mouse BLA with Calb1 + Pvalb + Sst + Sncg probes.
- **Target:** Identify Calb1+/Pvalb-/Sst- cells and their Sncg status; quantify fraction of BLA GABAergic population.
- **Expected output:** LiteratureEvidence or MarkerAnalysisEvidence confirming the Calb1+/PV-/SST- phenotype; cross-reference to transcriptomic cluster via Sncg expression.
- **Resolves:** Open questions 1–3; caveats NO_DISCRIMINATING_MARKER and DISTRIBUTED_ACROSS_CLUSTERS.

#### 4. Targeted cite-traverse for Calb1/Sst co-expression in BLA

- **What:** Literature search for "calbindin BLA interneuron Sst" or "calbindin dendrite-targeting amygdala SST".
- **Target:** A primary study confirming Calb1+/Sst- as a distinct BLA population, independent of the SOM+/Calb1+ co-expression context cited in Ünal et al. [2].
- **Expected output:** LiteratureEvidence supporting the Sst-negativity criterion.
- **Resolves:** Marker evidence provenance gap — Sst-negativity currently lacks a primary citation.

### Open questions

1. Is CS20230722_CLUS_0666 Pvalb-negative? Requires precomputed expression query for Pvalb from CCN20230722 HDF5, or a targeted literature search. This is the single most important question.

2. Which BLA Sncg Gaba cluster(s) express Calb1 without high Cck and without Pvalb co-expression? CLUS_0666 (n=694 cells) co-occurs with a high-CCK parent supertype (SUPT_0185), and sibling CLUS_0664 may drive the CCK signal. CLUS_0666 and CLUS_0668 are candidates but cannot be ranked without HDF5 data.

3. Does Sst-negativity of the classical type have independent primary-literature support? Ünal et al. [2] situates Calb1 within a broader SOM+/Calb1+ context, which creates marker overlap ambiguity. A targeted cite-traverse would clarify whether a Calb1+/Sst- population has been directly documented in BLA.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Bienvenu et al. 2012 · Cell-Type-Specific Recruitment of Amygdala Interneurons to Hippocampal Theta Rhythm and Noxious Stimuli In Vivo | [22726836](https://pubmed.ncbi.nlm.nih.gov/22726836/) | Soma location; GABAergic NT; Calb1 defining marker; dendrite-targeting morphology |
| [2] | Ünal et al. 2020 · Low-threshold spiking interneurons perform feedback inhibition in the lateral amygdala | [32144495](https://pubmed.ncbi.nlm.nih.gov/32144495/) | Calb1 marker corroboration; SOM co-expression context (mouse lateral amygdala review) |

---

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_cs20230722_clus_0666 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    Calb1 (marker_Calb1 CONSISTENT; precomputed mean_expression 10.37, BLA GABAergic
    cohort 98.9th pct, applied_score 2.0) and GABAergic NT type support
    CS20230722_CLUS_0666 as a candidate, but 1 of 1 marker assessed (Calb1) is
    insufficient to discriminate the Sncg Gaba lineage from Pvalb Gaba clusters:
    three of five rank-0 BLA GABAergic candidates score identically (discovery score 3,
    cohort_size 5), and negative markers Pvalb and Sst are NOT_ASSESSED due to absent
    precomputed expression data, preventing enforcement of the defining
    non-PV, non-SST criterion for this cell type.
  reconciliation_note: >
    Calb1 is co-expressed in SOM+/Calb1+ BLA interneurons (Ünal et al. 2020,
    PMID:32144495); the classical type requires Pvalb-negativity and Sst-negativity
    to be distinguished from Pvalb Gaba and Sst Gaba clusters that also score high
    on Calb1. Until negative-marker expression is confirmed from CCN20230722 HDF5,
    no narrower predicate than evidencell:UncertainRelationship is supportable.
  lit_to_lit_edges: []
  unresolved_questions:
    - "Is CS20230722_CLUS_0666 Pvalb-negative? Requires precomputed expression query for Pvalb from CCN20230722 HDF5."
    - "Which BLA Sncg Gaba cluster(s) express Calb1 without high Cck and without Pvalb co-expression? CLUS_0666 and CLUS_0668 are candidates but cannot be ranked without HDF5 data."
    - "Does Sst-negativity of the classical type have independent primary-literature support? Ünal et al. 2020 situates Calb1 within SOM+ interneurons, creating marker overlap ambiguity."
```
<!-- verdict-block-end -->
