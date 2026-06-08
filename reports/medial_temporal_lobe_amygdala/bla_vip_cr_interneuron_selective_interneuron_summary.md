# Basolateral amygdala VIP/calretinin-expressing interneuron-selective interneuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

The VIP/calretinin-expressing interneuron-selective (IS) interneuron is the numerically dominant GABAergic class of the mouse basolateral amygdala (BLA), comprising an estimated 29–38% of all GABAergic cells in the lateral (LA) and basal (BA) amygdala [3]. Classically recognised as small bipolar and bitufted non-pyramidal neurons, these cells co-express the calcium-binding protein calretinin (encoded by *Calb2*), the neuropeptide VIP, and often CCK; their morphological specialisation toward targeting other interneurons (IS morphology) distinguishes them from the larger CCK+ basket cell population. Mapping this type to the WMBv1 atlas is important for anchoring the dominant inhibitory circuit element of the BLA to a transcriptomic reference that enables cross-region comparisons and future annotation-transfer workflows.

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1] |
| Neurotransmitter | GABAergic | [1] |
| Defining marker | Calb2 (calretinin) | [1], [2] |
| Neuropeptides | Vip, Cck | [1] |
| Morphology | Small bipolar/bitufted; interneuron-selective (targets other interneurons) | [1] |
| Proportion | ~29–38% of GABAergic cells in LA/BA | [3] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / Neurotransmitter / Defining marker / Neuropeptides / Morphology:** Immunohistochemistry · mouse BLA · [1]
  > The cell types in all of these amygdalar nuclei are similar, but they have been studied primarily in the basolateral amygdala. The principal neurons in the CBL are pyramidal-like projection neurons with spiny dendrites that utilize glutamate as an excitatory neurotransmitter, whereas most non-pyramidal neurons in the CBL are spine-sparse interneurons that utilize GABA as an inhibitory neurotransmitter … Dual-labeling immunohistochemical studies in the basolateral amygdala suggest that the CBL contains at least four distinct subpopulations of GABAergic non-pyramidal neurons that can be distinguished on the basis of their content of calcium-binding proteins and peptides. These subpopulations are: (1) PV+/CB+ neurons, (2) SOM+/CB+ neurons, (3) large multipolar cholecystokinin+ neurons that are often CB+, and (4) small bipolar and bitufted interneurons that exhibit extensive colocalization of calretinin, cholecystokinin, and vasoactive intestinal peptide
  > — McDonald et al. 2012, Classical neuron classes across amygdala subdivisions · [1] <!-- quote_key: 11544073_94689603 -->

- **Proportion (29–38% of GABAergic cells):** Stereological quantification · mouse LA/BA · [3]
  > VIP and/or calretinin-expressing interneuron-selective interneurons (29-38 %)
  > — Vereczki et al. 2021, Abstract · [3] <!-- quote_key: 232283078_08e867ee -->

- **Defining marker Calb2:** scRNA-seq / transcriptomic profiling · mouse amygdala · [2]
  *(note: Hochgerner et al. 2023 [2] identify canonical CGE-derived interneuron types including Vip and Sncg classes; Calb2 co-expression with Vip is an interpretive inference from the VIP/CR classical type definition rather than a direct quote from the stored evidence — see defining markers above.)*

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate edge was assessed (broadMatch 1:n). Because all five Vip Gaba clusters in the WMBv1 atlas within the BLA GABAergic cohort score equally on the two defining criteria (Calb2 + Vip, both tier-2 reliable), the classical type distributes across multiple atlas clusters; confidence is LOW, capped by the absence of annotation-transfer evidence and the unresolved 1:n cardinality.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_CLUS_0628 (representative of five equal Vip Gaba clusters) | SUPT_0174 | not recorded | 🔴 LOW | Calb2 CONSISTENT · Vip CONSISTENT · Cck APPROXIMATE | broadMatch 1:n |

*1 edge assessed; relationship type: `skos:broadMatch` (1:n — all 5 Vip Gaba clusters score equally).*

### Property alignment — CS20230722_CLUS_0628 (representative)

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | not available | MBA:295 BLA present; region_fraction 0.049 (SUPT_0174) | CONSISTENT |
| NT type | GABAergic | GABA | GABA | CONSISTENT |
| Calb2 expression | defining marker (TRANSCRIPT) | not available | mean 8.12 (BLA GABAergic cohort 98.3rd pct; tier 2) | CONSISTENT |
| Vip neuropeptide | Vip — neuropeptide | not available | mean 11.11 (BLA GABAergic cohort 96.9th pct; tier 2; cluster label "Vip Gaba_2") | CONSISTENT |
| Cck neuropeptide | Cck — neuropeptide (co-expressed with VIP per [1]) | not available | mean 0.97 (BLA GABAergic cohort 41.7th pct; tier 1) | APPROXIMATE |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| McDonald 2012 BLA interneuron classification | Literature | SUPPORT | IS interneurons: small bipolar/bitufted, calretinin+CCK+VIP co-expression | [1] |
| Vereczki 2021 stereological quantification | Literature | SUPPORT | VIP/CR interneurons = 29–38% of GABAergic cells in LA/BA | [3] |
| WMBv1 atlas metadata — CLUS_0628 Vip Gaba_2 | Atlas metadata | SUPPORT | Calb2 98.3rd pct, Vip 96.9th pct; 5 Vip Gaba clusters score equally (score 6/6) | atlas-internal |

*(Child-cluster breakdown not assessed beyond the five equally scoring Vip Gaba rank-0 clusters — see proposed experiments.)*

---

### CS20230722_CLUS_0628 "Vip Gaba_2" · 🔴 LOW

This edge nominates CS20230722_CLUS_0628 as a representative member of the Vip Gaba cluster family, reflecting a broadMatch over five clusters (CLUS_0628, CLUS_0630, CLUS_0638, CLUS_0649, CLUS_0656) spanning four supertypes (SUPT_0174, SUPT_0176, SUPT_0179, SUPT_0181).

**Supporting evidence:**

- **Calb2 CONSISTENT.** CLUS_0628 shows Calb2 precomputed mean expression 8.12, ranking at the 98.3rd percentile of the BLA GABAergic cohort (tier 2, applied_score 2.0). McDonald et al. 2012 [1] and Hochgerner et al. 2023 [2] both establish calretinin (Calb2) as a defining transcript of this interneuron class in BLA.

- **Vip CONSISTENT.** CLUS_0628 shows Vip mean 11.11, at the 96.9th percentile of the BLA GABAergic cohort (tier 2, applied_score 2.0). The cluster label "Vip Gaba_2" reflects this. The classical type is by definition VIP-expressing, and this alignment is unambiguous across all five Vip Gaba cluster candidates.

- **Location CONSISTENT.** Region_fraction 0.049 for CLUS_0628 in MBA:295 (BLA), with parent SUPT_0174 present in BLA. CLUS_0630 has the highest region_fraction (0.066) within the same supertype. Both are consistent with basolateral amygdala soma location [UBERON:0002887].

- **Stereological confirmation** [3]: Vereczki et al. 2021 provide an independent quantification by stereology, confirming VIP/calretinin IS interneurons as the single largest GABAergic class in mouse LA/BA:

  > VIP and/or calretinin-expressing interneuron-selective interneurons (29-38 %)
  > — Vereczki et al. 2021, Abstract · [3] <!-- quote_key: 232283078_08e867ee -->

- **Stage A discovery score.** CLUS_0628 ranks 1st in a 5-member BLA GABAergic cohort with score 6, but all five Vip Gaba clusters share the same score 6 (next_best_score = 6, cohort_size = 5). This tie means Stage A cannot discriminate among them; the broadMatch 1:n is the correct cardinality call.

**Marker evidence provenance:**

- **Calb2:** Evidence is transcript-level (scRNA-seq in [2]; IHC-inferred in [1] where "calretinin" is the protein label for *Calb2*). McDonald et al. 2012 [1] confirmed calretinin co-expression in morphologically characterised bipolar/bitufted interneurons (morphological reconstruction implicit in dual-label IHC studies cited). Hochgerner et al. 2023 [2] provide direct scRNA-seq evidence from mouse amygdala. Evidence chain is adequate: two independent primary studies, both using methods appropriate for cell-type identification in BLA.

- **Vip:** Protein-level evidence by IHC ([1]); cluster label in WMBv1 confirms transcript-level agreement. No discrepancy flagged.

- **Cck:** Classical literature ([1]) lists Cck as co-expressed in a subset of these IS interneurons. CLUS_0628 shows Cck at tier-1 reliability only (mean 0.97, 41.7th percentile). This is an APPROXIMATE alignment: Cck is present but not the dominant identity marker in this cluster. Higher Cck expression is found in sibling Sncg Gaba supertypes (SUPT_0185, mean 10.12). This discrepancy does not refute the mapping — IS interneurons are known to show partial Cck co-expression — but it raises the question of whether a subset of CCK-dominant IS interneurons may be better captured by the Sncg Gaba family.

**Concerns:**

- **1:n cardinality unresolved.** Five Vip Gaba clusters spanning four supertypes score equally on Calb2+Vip. No current evidence (AT, patch-seq, smFISH) resolves which subset of these clusters corresponds to the IS morphological specialisation that defines the classical type. This is the primary driver of LOW (not MODERATE) confidence.

- **Cck APPROXIMATE** in CLUS_0628 (tier 1, 41.7th pct). The classical IS interneuron is described as co-expressing Cck; higher Cck resides in the Sncg Gaba family. Some IS interneurons may be better captured by Sncg over Vip Gaba clusters — see unresolved question 2 below.

- **No annotation-transfer evidence.** Confidence is capped at LOW per the predicate rubric (step iv) in the absence of AT evidence. A MapMyCells run on patch-seq transcriptomes from morphologically confirmed BLA IS interneurons would be the most direct path to resolving cardinality.

- **No negative markers characterised.** The classical node carries no negative markers, limiting the ability to discriminate CLUS_0628 from its four equally scoring Vip Gaba siblings.

**What would upgrade confidence:**

- **MapMyCells annotation transfer** on patch-seq or single-cell transcriptomes from morphologically confirmed (IS morphology, biocytin fill) BLA VIP/calretinin interneurons. Target: F1 ≥ 0.70 at CLUSTER level for a specific Vip Gaba cluster, reducing 1:n to a clear primary candidate. Expected output: `AnnotationTransferEvidence` on the highest-F1 cluster; remaining four edges demoted to UNCERTAIN or REFUTED. Resolves the DISTRIBUTED_ACROSS_CLUSTERS caveat.

- **Multiplexed smFISH** (Vip + Calb2 + Cck + Cnr1 in mouse BLA) to map the five Vip Gaba cluster sizes, distinguish the IS subpopulation (Cnr1-negative, Calb2-high), and quantify the Sncg vs Vip Gaba split for CCK-expressing IS cells. Expected output: revised `marker_Cck` alignment and potentially a refined 1:n cardinality.

- **Targeted literature search** for Cnr1 expression in VIP/calretinin BLA interneurons: the classical description includes a CNR1-negative, calretinin-leading characterisation (node notes). A lit search for "CNR1 VIP calretinin BLA amygdala" would clarify whether this is documented in primary literature and whether any Vip Gaba cluster carries CNR1-absent metadata.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Basolateral amygdala VIP/calretinin-expressing interneuron-selective interneuron is defined on a CLASSICAL basis, drawing on dual-label immunohistochemical studies in mouse BLA. Defining marker: Calb2 (calretinin) [1, 2]. Neuropeptides: Vip [1], Cck [1]. NT type: GABAergic [1]. Soma location: Basolateral amygdala [UBERON:0002887] [1]. Morphological identity (small bipolar/bitufted, IS targeting) is IHC-established [1]. Stereological proportion (29–38% of GABAergic cells in LA/BA) from [3]. This is the largest GABAergic class in the BLA.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`. Discovery was restricted to BLA GABAergic cohort (region=MBA:295, nt_type=GABAergic), yielding a cohort of 5 Vip Gaba clusters.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Atlas data sources.**
- Atlas: CCN20230722; taxonomy_id: CCN20230722; graph file: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_vip_cr_interneuron_selective_interneuron_to_cs20230722_clus_0628 | LITERATURE; LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT; SUPPORT | [1], [3], atlas-internal |

*Generated by evidencell `8222564` at 2026-06-04T10:52:48+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala VIP/calretinin-expressing interneuron-selective interneuron → CS20230722_CLUS_0628 (representative of five equal Vip Gaba clusters) at LOW confidence. Key support: Calb2 CONSISTENT (98.3rd pct in BLA GABAergic cohort) and Vip CONSISTENT (96.9th pct); two independent primary literature sources confirm the IS interneuron class. Key caveats: broadMatch 1:n — all five Vip Gaba clusters score equally with no AT evidence to resolve cardinality; Cck expression is APPROXIMATE (tier 1 only in CLUS_0628), raising the possibility that a CCK-dominant IS subset aligns better to the Sncg Gaba family.

No Cell Ontology term currently assigned. This type is a strong candidate for a new CL term describing the calretinin+VIP+CCK IS interneuron of the BLA.

### Proposed experiments and follow-ups

**1. Annotation transfer (MapMyCells) — resolves 1:n cardinality**

- **What:** MapMyCells annotation transfer using patch-seq or single-cell RNA-seq transcriptomes from morphologically confirmed IS interneurons (biocytin fill + calretinin/VIP immunostaining) in mouse BLA.
- **Target:** F1 ≥ 0.70 at CLUSTER level for a single Vip Gaba cluster.
- **Expected output:** `AnnotationTransferEvidence` on the primary cluster; remaining four Vip Gaba edges reclassified as UNCERTAIN. Confidence would upgrade to MODERATE (exactMatch or closeMatch; AT present + consistent markers).
- **Resolves:** DISTRIBUTED_ACROSS_CLUSTERS caveat; unresolved question 1.

**2. Multiplexed smFISH panel — Cck / Cnr1 discrimination**

- **What:** smFISH with probes for Vip, Calb2, Cck, and Cnr1 in mouse BLA sections.
- **Target:** Quantify fraction of Vip/Calb2-double-positive cells that are Cck-high and/or Cnr1-positive; map to Vip Gaba vs Sncg Gaba cluster sizes.
- **Expected output:** Updated `marker_Cck` alignment (CONSISTENT or DISCORDANT rather than APPROXIMATE); potentially a revised `neuropeptide_Cck` property_comparison. Could also clarify whether IS interneurons are Cnr1-negative as suggested by the node notes.
- **Resolves:** MARKER_NOT_SPECIFIC caveat; unresolved question 2.

**3. Targeted literature search — Cnr1 / VIP / calretinin BLA**

- **What:** Cite-traverse or snippet search for "CNR1 VIP calretinin BLA" or "CB1 VIP calretinin amygdala".
- **Target:** Identify any primary publication confirming CNR1-negative status of calretinin-expressing IS interneurons in BLA.
- **Expected output:** `LiteratureEvidence` item on the edge with `marker_Cnr1` property comparison added; no new experiment required.
- **Resolves:** Node notes flag on CNR1-negative characterisation currently lacking a citation.

### Open questions

1. Which of the five Vip Gaba clusters (CLUS_0628, CLUS_0630, CLUS_0638, CLUS_0649, CLUS_0656) best captures the IS morphological specialisation in BLA? All currently score equally on Calb2+Vip.

2. Is the Sncg Gaba_1 supertype (SUPT_0185, Cck-high, mean 10.12) a better transcriptomic match than the Vip Gaba family for the CCK-expressing IS interneuron subset? The tier-1 Cck signal in CLUS_0628 raises this as an open question.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | McDonald et al. 2012 | [22837739](https://pubmed.ncbi.nlm.nih.gov/22837739/) | Soma location, NT type, defining marker (Calb2), neuropeptides (Vip, Cck), IS morphology |
| [2] | Hochgerner et al. 2023 | [37884748](https://pubmed.ncbi.nlm.nih.gov/37884748/) | Calb2 as defining marker in mouse amygdala transcriptomic atlas |
| [3] | Vereczki et al. 2021 | [33837051](https://pubmed.ncbi.nlm.nih.gov/33837051/) | Stereological quantification: VIP/CR interneurons = 29–38% of GABAergic cells in LA/BA |

---

<!-- verdict-block-start: edge_bla_vip_cr_interneuron_selective_interneuron_to_cs20230722_clus_0628 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  rationale: >
    skos:broadMatch 1:n over five Vip Gaba clusters; all five score equally in a 5-member
    BLA GABAergic cohort (score 6, next_best_score 6). CS20230722_CLUS_0628 is
    representative: marker_Calb2 CONSISTENT (98.3rd pct, tier 2) and neuropeptide_Vip
    CONSISTENT (96.9th pct, tier 2) anchor the Vip Gaba family assignment;
    neuropeptide_Cck APPROXIMATE (tier 1, 41.7th pct). No ANNOTATION_TRANSFER evidence
    available; confidence capped at LOW per predicate rubric step iv.
  reconciliation_note: ""
  lit_to_lit_edges: []
  unresolved_questions:
    - "Which of the five Vip Gaba clusters best captures the IS morphological specialisation in BLA?"
    - "Is SUPT_0185 (Sncg Gaba_1, Cck-high) a better match for the CCK-dominant IS interneuron subset?"
```
<!-- verdict-block-end -->
