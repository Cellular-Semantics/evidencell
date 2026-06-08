# Basolateral amygdala calbindin-positive dendrite-targeting interneuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala (BLA) calbindin-positive dendrite-targeting interneuron is a classically defined GABAergic cell type of the BLA characterised by expression of the calcium-binding protein calbindin-1 (Calb1) and a dendritic targeting morphology. Bienvenu et al. 2012 identified this as one of four distinct interneuron classes in the BLA — alongside PV+ basket cells, axo-axonic cells, and AStria-projecting cells — based on in-vivo electrophysiology combined with post-hoc immunohistochemistry [1]. The cell type is further distinguished from the related SOM+ dendrite-targeting population by the absence of SST co-expression [classical node notes]. Mapping this type to the WMBv1 transcriptomic atlas is important for linking classical physiology-based classification to molecular cluster identity, but is currently blocked by the non-specificity of the sole available marker.

**Primary null-result finding:** A complete scan of CCN20230722 BLA GABAergic clusters (rank 0) confirmed that Calb1 alone cannot resolve this cell type to a single atlas cluster. Five rank-0 candidates from the BLA GABAergic cohort score identically (score 3), spanning both Sncg Gaba (CLUS_0666, CLUS_0668) and Pvalb Gaba (CLUS_0738, CLUS_0745, CLUS_0748) lineages. Without negative-marker confirmation for Pvalb and Sst, the mapping remains UNCERTAIN.

### Classical type description

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1] |
| NT type | GABAergic | [1] |
| Defining marker | Calb1 (calbindin-1; protein-level) | [1], [2] |
| Negative markers | Pvalb (implicit — non-PV by definition), Sst (no SST co-expression) | [1] (implicit) |
| Neuropeptides | None documented | — |
| Morphology | Dendrite-targeting | [1] |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location / GABAergic NT / Dendrite-targeting morphology / Calb1 defining marker:** electrophysiology + post-hoc immunohistochemistry · in-vivo rat BLA · [1]
  > calbindin-positive interneurons targeting dendrites
  > — Bienvenu et al. 2012, Basolateral amygdala and corticobasal cell types · [1] <!-- quote_key: 10647550_48ea3c0f -->

  Additional characterisation context:
  > We characterized GABAergic interneuron types of the BLA
  > — Bienvenu et al. 2012, Basolateral amygdala and corticobasal cell types · [1] <!-- quote_key: 10647550_0e5ce349 -->

- **Calb1 marker / SOM co-expression context:** review + immunofluorescence · mouse lateral amygdala · [2]
  > SOM positive interneurons constitute the other common interneuron population and they co-express markers such as neuropeptide Y (NPY) and calbindin
  > — Ünal et al. 2020, Introduction · [2] <!-- quote_key: 212579559_81debee5 -->

  *(note: This quote establishes that calbindin co-expression occurs in SOM+ interneurons — a key biological context explaining why Calb1 alone cannot discriminate the classical Calb1+/SST- dendrite-targeting type from SOM+ populations or their transcriptomic correlates.)*

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed (CS20230722_CLUS_0666 "Sncg Gaba_1"). The edge carries `evidencell:UncertainRelationship` at UNCERTAIN confidence because Calb1 expression does not discriminate the Sncg Gaba lineage from Pvalb Gaba lineages in the BLA GABAergic cohort.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | CS20230722_CLUS_0666 ("Sncg Gaba_1") | — | n/a | ⚪ UNCERTAIN | Calb1 CONSISTENT; Pvalb NOT_ASSESSED | `evidencell:UncertainRelationship` |

*1 edge assessed; all UNCERTAIN. No MODERATE or LOW edges.*

#### Property alignment — CS20230722_CLUS_0666 [⚪ UNCERTAIN]

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA (atlas label) | GABA | CONSISTENT |
| Soma location | BLA [UBERON:0002887] | not available | MBA:295 present; region_fraction = 0.10 (cohort rank 1 of 5 BLA GABAergic) | CONSISTENT |
| Calb1 expression | Calb1 — defining marker (protein; [1], [2]) | not available | mean_expression 10.37; 98.9th pct of BLA GABAergic cohort | CONSISTENT |
| Pvalb (negative) | Pvalb — implicitly negative (non-PV cell) | not available | NOT_ASSESSED — Sncg Gaba_1 lineage label suggestive but unconfirmed | NOT_ASSESSED |
| Sst (negative) | Sst — implicitly negative (no SST co-expression; node notes) | not available | NOT_ASSESSED — Sst not in precomputed expression for CLUS_0666 | NOT_ASSESSED |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Bienvenu 2012 BLA interneuron characterisation | Literature | SUPPORT | IHC + in-vivo ephys; confirms Calb1+ dendrite-targeting class in BLA | [1] |
| Ünal 2020 LA interneuron review | Literature | SUPPORT | Calb1 protein confirmed in mouse lateral amygdala; SOM co-expression noted | [2] |
| WMBv1 atlas metadata — CLUS_0666 | Atlas metadata | SUPPORT | Calb1 98.9th pct of BLA GABAergic cohort; but 5 rank-0 clusters score equally; non-specific | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

## Eliminated candidates

All edges for this node carry UNCERTAIN confidence. The shared disqualifying signal is **non-specificity of Calb1 as the sole discriminating marker**: Calb1 is expressed in both Sncg-lineage and Pvalb-lineage GABAergic clusters in the BLA. Without negative-marker confirmation (Pvalb, Sst), the classical Calb1+/PV-/SST- definition cannot be enforced against the transcriptomic atlas.

### CS20230722_CLUS_0666 "Sncg Gaba_1" — ⚪ UNCERTAIN

- Calb1 mean_expression 10.37 (BLA GABAergic cohort 98.9th pct) — CONSISTENT with defining marker, but not discriminating.
- Three of five rank-0 BLA GABAergic candidates (CLUS_0738, CLUS_0745, CLUS_0748) are Pvalb Gaba clusters scoring equally (score 3, same as CLUS_0666); this demonstrates that single-marker Calb1 scoring does not exclude PV+ cells.
- Pvalb (negative marker) is NOT_ASSESSED: Pvalb expression not available from precomputed data for CLUS_0666; the Sncg lineage label is circumstantially consistent with Pvalb-negativity but is not sufficient confirmation.
- Sst (negative marker) is NOT_ASSESSED: Sst not in precomputed expression data for CLUS_0666.
- Additional caveat: the parent supertype of CLUS_0666 expresses CCK at high levels (precomputed mean 10.12), creating potential overlap with the bla_cck_cb1_basket_cell node (sibling cluster CLUS_0664 under the same supertype). This is a weak counter-signal — it does not refute the location or NT match — but it complicates cluster-level specificity.
- region_fraction = 0.10: only 10% of this cluster's cells are in MBA:295 (BLA). This is below the boundary band of 0.3–0.7 and is consistent with a broad amygdala-wide or cortex-wide cluster, not a BLA-specific population. Given the very small BLA-GABAergic cohort of only 5 clusters, this value alone is not a strong disqualifier.
- *(note: The Sncg Gaba lineage label is a useful prior against Pvalb identity, but is not a direct negative-marker measurement. Sncg and Pvalb lineages are largely non-overlapping in WMBv1, so CLUS_0666 being in the Sncg family somewhat reduces the probability that it is a PV+ basket cell — but this reasoning is based on atlas taxonomy conventions, not direct expression data.)*

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The BLA calbindin dendrite-targeting interneuron is defined on a CLASSICAL basis: the node's `definition_basis` is `CLASSICAL`, drawing on in-vivo electrophysiology combined with post-hoc immunohistochemistry from Bienvenu et al. 2012 [1] and immunofluorescence from Ünal et al. 2020 [2]. The defining marker is Calb1 (protein level; [1], [2]). NT type is GABAergic [1]. Soma location is basolateral amygdala [UBERON:0002887] [1]. The negative markers (Pvalb, Sst) are implicit in the classical type's definition ("non-PV, non-SST" criterion) and are not positively sourced to individual publications in the current KB entry.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 0 (cluster) using metadata-based scoring (region match MBA:295, NT type GABAergic, defining marker Calb1). Full scoring rules: `workflows/map-cell-type.md`. Only rank 0 was assessed; the facts file contains no rank-1 (supertype-level) edges.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values for Calb1 came from precomputed expression on the cluster in the taxonomy reference store. Negative markers (Pvalb, Sst) could not be assessed because precomputed expression data for these genes in CLUS_0666 was not available.

**Atlas data sources.** CCN20230722 · taxonomy YAML under `kb/taxonomy/CCN20230722/`. No pseudobulk SHA-256 was emitted for this run (atlas_data_sources list empty in facts file — indicates the HDF5 precomputed stats file was not accessible at gen-facts time; this is the root cause of the NOT_ASSESSED Pvalb/Sst alignments).

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_calbindin_dendrite_targeting_interneuron_to_cs20230722_clus_0666 | LITERATURE; LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT; SUPPORT | [1]; [2]; atlas-internal |

*Generated by evidencell `8222564` at 2026-06-04T10:52:48+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala calbindin-positive dendrite-targeting interneuron → CS20230722_CLUS_0666 ("Sncg Gaba_1") at UNCERTAIN confidence. Key support: Calb1 is consistently expressed at the 98.9th percentile of the BLA GABAergic cohort (EXPRESSION source); GABAergic NT and BLA soma location are CONSISTENT. Key caveats: NO_DISCRIMINATING_MARKER (Calb1 alone cannot exclude Pvalb Gaba clusters); DISTRIBUTED_ACROSS_CLUSTERS (5 rank-0 candidates score identically, including 3 Pvalb Gaba clusters); Pvalb and Sst negative-marker assessments are NOT_ASSESSED due to absent HDF5 data.

No Cell Ontology term currently assigned. The node notes indicate overlap with SOM/CB+ interneurons in older marker schemes; a targeted CL term request may be warranted once transcriptomic identity is resolved.

### Proposed experiments and follow-ups

#### 1. Acquire CCN20230722 HDF5 and re-run discovery with negative-marker scoring

- **What:** Re-run `just find-candidates` for `bla_calbindin_dendrite_targeting_interneuron` after making the CCN20230722 HDF5 precomputed stats accessible, adding Pvalb and Sst as negative markers in the scoring configuration.
- **Target:** Elimination of CLUS_0738, CLUS_0745, CLUS_0748 (Pvalb Gaba) from the candidate set; narrowing to Sncg Gaba candidates that are Pvalb-low and Sst-low.
- **Expected output:** Updated `property_comparisons` with `negative_marker_Pvalb` = CONSISTENT (absent in CLUS_0666) and `negative_marker_Sst` = CONSISTENT; confidence upgrade to LOW if Sncg Gaba lineage is confirmed Pvalb-negative.
- **Resolves:** Unresolved question 1 ("Is CLUS_0666 Pvalb-negative?"); caveat NO_DISCRIMINATING_MARKER.

#### 2. Multiplexed smFISH in mouse BLA

- **What:** Multiplexed smFISH (e.g. RNAscope or MERFISH) in mouse BLA with probes for Calb1, Pvalb, Sst, and Sncg.
- **Target:** Identify cells that are Calb1+/Pvalb-/Sst- and determine their Sncg expression status; quantify as fraction of BLA GABAergic population.
- **Expected output:** LiteratureEvidence or direct MarkerAnalysisEvidence on the classical node confirming the Calb1+/PV-/SST- phenotype in mouse; cross-reference to transcriptomic cluster via Sncg.
- **Resolves:** Unresolved question 2 ("Which Sncg Gaba cluster(s) in BLA express Calb1 without high Cck, excluding PV lineage?"); caveats NO_DISCRIMINATING_MARKER and DISTRIBUTED_ACROSS_CLUSTERS.

#### 3. Annotation transfer (MapMyCells)

- **What:** Run MapMyCells annotation transfer against CCN20230722 using a published BLA interneuron transcriptomic dataset (if available) that includes Calb1+/PV-/SST- cells.
- **Target:** F1 >= 0.70 at CLUSTER level for a single Sncg Gaba cluster (preferably CLUS_0666 or CLUS_0668).
- **Expected output:** AnnotationTransferEvidence item on the edge; confidence upgrade from UNCERTAIN to LOW (single AT run) or MODERATE (AT + marker confirmation).
- **Resolves:** Both unresolved questions; predicate may be upgradeable from `evidencell:UncertainRelationship` to `skos:closeMatch` or `skos:exactMatch` pending AT result and marker cross-check.

#### 4. Targeted literature search for Calb1 specificity in BLA

- **What:** Targeted cite-traverse for "calbindin BLA interneuron PV SST" and "calbindin dendrite targeting amygdala transcriptomics" to find studies that have co-stained or co-sequenced Calb1+ BLA interneurons with Pvalb/Sst.
- **Target:** A primary study confirming Calb1+/PV-/SST- as a distinct BLA population at protein or transcript level.
- **Expected output:** LiteratureEvidence item supporting the negative-marker criterion; would allow moving the Pvalb/Sst alignments from NOT_ASSESSED to CONSISTENT or DISCORDANT.
- **Resolves:** Weak-provenance flag on implicit negative markers; may partially substitute for experiment 2 if a relevant ISH or scRNA-seq dataset already exists in the literature.

### Open questions

1. Is CS20230722_CLUS_0666 Pvalb-negative? This is the single most important question. Requires expression query for Pvalb in CLUS_0666 from the CCN20230722 HDF5, or a targeted literature search. (Edge: `edge_bla_calbindin_dendrite_targeting_interneuron_to_cs20230722_clus_0666`)

2. Which Sncg Gaba cluster(s) in BLA express Calb1 without high Cck and while excluding PV lineage? CLUS_0666 co-occurs with a high-CCK supertype (SUPT_0185), creating potential confusion with the bla_cck_cb1_basket_cell node. Identifying whether the Calb1+ dendrite-targeting population maps to CLUS_0666, CLUS_0668, or a combination would narrow the classical-to-atlas correspondence. (Edge: `edge_bla_calbindin_dendrite_targeting_interneuron_to_cs20230722_clus_0666`)

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Bienvenu et al. 2012 · Cell-Type-Specific Recruitment of Amygdala Interneurons to Hippocampal Theta Rhythm and Noxious Stimuli In Vivo | [22726836](https://pubmed.ncbi.nlm.nih.gov/22726836/) | Soma location; GABAergic NT; Calb1 defining marker; dendrite-targeting morphology; negative marker (Pvalb, implicit) |
| [2] | Ünal et al. 2020 · Low-threshold spiking interneurons perform feedback inhibition in the lateral amygdala | [32144495](https://pubmed.ncbi.nlm.nih.gov/32144495/) | Calb1 protein confirmation in mouse lateral amygdala interneurons |

---

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_cs20230722_clus_0666 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    Calb1 is CONSISTENT at the 98.9th percentile of the BLA GABAergic cohort
    (EXPRESSION source; mean_expression 10.37) and NT/location are CONSISTENT,
    but Calb1 alone cannot discriminate Sncg Gaba from Pvalb Gaba lineages:
    3 of 5 rank-0 BLA GABAergic candidates are Pvalb Gaba clusters (CLUS_0738,
    CLUS_0745, CLUS_0748) scoring identically (score 3, cohort_size 5).
    Negative markers Pvalb and Sst are NOT_ASSESSED (HDF5 unavailable).
    No annotation-transfer evidence. Relationship is evidencell:UncertainRelationship.
  reconciliation_note: >
    Calb1 is co-expressed in SOM+/Calb1+ interneurons (Ünal et al. 2020 [PMID:32144495]);
    the classical type requires Pvalb-negativity and Sst-negativity to be distinguished
    from the Pvalb Gaba and Sst Gaba clusters that also show high Calb1. Until
    negative-marker expression is confirmed from HDF5, no narrower predicate is
    supportable. HDF5 acquisition (proposed experiment 1) is the blocker.
  unresolved_questions:
    - "Is CS20230722_CLUS_0666 Pvalb-negative? Requires precomputed expression query for Pvalb from CCN20230722 HDF5."
    - "Which BLA Sncg Gaba cluster(s) express Calb1 without high Cck and without Pvalb co-expression? CLUS_0666 and CLUS_0668 are candidates but cannot be ranked without HDF5 data."
```
<!-- verdict-block-end -->
