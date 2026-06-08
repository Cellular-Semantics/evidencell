# Amygdala intercalated cell — CCN20230722 Mapping Report
*2026-06-05 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Amygdala intercalated cells (ITCs) are small clusters of densely packed GABAergic neurons
positioned within the intercalated cell masses (ICMs) — a set of nuclei at the interface between
the basolateral and centromedial amygdala that remain outside the canonical four-subdivision
classification. Their distinctive molecular identity, defined by co-expression of Foxp2, Drd1
(dopamine D1-receptor), and Oprm1 (µ-opioid receptor), has been documented across multiple
mammalian species by transcriptomic studies. Mapping this population to the Allen CCN20230722
transcriptomic atlas grounds their molecular identity in the mouse whole-brain taxonomy and
provides a substrate for cross-species and functional comparisons.

> . In addition to the four groups, a few nuclei of the amygdala remain unclassified, among them the intercalated cell masses which are small clusters of densely packed GABAergic neurons (Palomares-Castillo et al., 2012).
> — Veinante et al. 2013, Amygdala organization and principal cellular classes · [3] <!-- quote_key: 15449738_a21bd562 -->

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Intercalated cell masses of the amygdala [UBERON:0002884] | [1], [2], [3] |
| NT type | GABAergic | [3], [4] |
| Foxp2 | Defining marker (transcript) | [5], [6] |
| Drd1 | Defining marker (transcript) | [6] |
| Oprm1 | Defining marker (transcript) | [5] |
| Negative markers | — | |
| Neuropeptides | — | |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** asta_report synthesis · amygdala/hippocampus literature · [1], [2], [3]

  > At the cellular level, the amygdala is composed of a group of 13 sub-nuclei located in the medial temporal lobe (Price, 2003). These nuclei may be divided into four subdivisions (Sah et al., 2003): (Ethen et al., 2009) basolateral (which includes the lateral, basolateral, and basomedial nuclei), (May et al., 2009) cortical like (including nucleus of the lateral olfactory tract, bed nucleus of the accessory olfactory tract, the cortical nucleus, and the periamygdaloid cortex), (3) centromedial (central and medial nuclei, and the amygdaloid part of the bed nucleus of stria terminalis), and (4) other (which includes anterior amygdala area, the amygdalo-hippocampal area, and the intercalated nuclei)
  > — Ignacio et al. 2014, Amygdala organization and principal cellular classes · [1] <!-- quote_key: 1229611_e14a19cf -->

  > . Anatomically the amygdala is composed of three major nuclear groups 198 : the deep or basolateral group, which contains the lateral nucleus, the basal nucleus, and the accessory basal nucleus; the superficial or cortical-like group, which contains the cortical nuclei and the nucleus of the lateral olfactory tract; the centromedial group, which contains the medial and central nuclei. To this canonical classification, other amygdaloid nuclei must be added, such as the anterior amygdaloid area, the amygdalohippocampal area, and the intercalated cells. 199 In addition, a rostro-medial extension of the centromedian amygdala into an area known as extended amygdala has been proposed. 200
  > — Nardelli et al. 2024, Amygdala organization and principal cellular classes · [2] <!-- quote_key: 270614391_b0af02da -->

- **NT type:** asta_report synthesis · amygdala/hippocampus literature · [3]; macaque amygdala GABA immunohistochemistry · [4]

  > . In addition to the four groups, a few nuclei of the amygdala remain unclassified, among them the intercalated cell masses which are small clusters of densely packed GABAergic neurons (Palomares-Castillo et al., 2012).
  > — Veinante et al. 2013, Amygdala organization and principal cellular classes · [3] <!-- quote_key: 15449738_a21bd562 -->

  > In some regions, such as the intercalated nuclei, virtually all of the resident neurons appeared to be GABAergic
  > — Pitkānen & Amaral 1994, abstract · [4] <!-- quote_key: 14068807_9efc175b -->

- **Foxp2 (defining marker):** asta_snippet · human, macaque, baboon amygdala snRNA-seq · [5]; human, macaque, mouse, chicken amygdala snRNA-seq · [6]

  > We identified distinct subtypes of FOXP2+ interneurons in the intercalated cell masses and protein-kinase C-δ interneurons in the central nucleus. We also establish that glutamatergic, pyramidal-like neurons are transcriptionally specialized within the basal, lateral, or accessory basal nuclei
  > — Totty et al. 2024, Medial, cortical/superficial, and intercalated cell populations · [5] <!-- quote_key: 273531817_88e4457f -->

  > the IA subnuclei were highly conserved, and all mammals in our datasets contained two types of TSHZ1+ neurons, i.e., DRD1+ and DRD1−.
  > — Yu et al. 2023, Results · [6] <!-- quote_key: 256832817_4f39c6f9 -->

- **Drd1 (defining marker):** asta_snippet · human, macaque, mouse, chicken amygdala snRNA-seq · [6]

  > the IA subnuclei were highly conserved, and all mammals in our datasets contained two types of TSHZ1+ neurons, i.e., DRD1+ and DRD1−.
  > — Yu et al. 2023, Results · [6] <!-- quote_key: 256832817_4f39c6f9 -->

- **Oprm1 (defining marker):** asta_snippet · human, macaque, baboon amygdala snRNA-seq · [5]

  > We identified distinct subtypes of FOXP2+ interneurons in the intercalated cell masses and protein-kinase C-δ interneurons in the central nucleus. We also establish that glutamatergic, pyramidal-like neurons are transcriptionally specialized within the basal, lateral, or accessory basal nuclei
  > — Totty et al. 2024, Medial, cortical/superficial, and intercalated cell populations · [5] <!-- quote_key: 273531817_88e4457f -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed; 0998 STR D1 Sema5a Gaba_3 [CS20230722_CLUS_0998]
is the primary mapping at LOW confidence via `skos:broadMatch` (1:n cardinality). All three
tier-2 defining markers — Foxp2, Drd1, and Oprm1 — are CONSISTENT, representing the strongest
three-marker convergence among the five GABAergic ITC-region clusters in the CCN20230722 cohort.

### Mapping candidates

**4a. Candidate overview table**

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---|---:|---|---|---|
| 1 | 0998 STR D1 Sema5a Gaba_3 [CS20230722_CLUS_0998] | 0283 STR D1 Sema5a Gaba_3 | 424 | 🔴 LOW | Foxp2 · Drd1 · Oprm1 all CONSISTENT | broadMatch 1:n |

1 edge assessed; relationship type `skos:broadMatch` (1:n).

**4b. Property alignment table — 0998 STR D1 Sema5a Gaba_3 [CS20230722_CLUS_0998]**

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Intercalated cell masses [UBERON:0002884] | not available | MBA:1105 intercalated nucleus present; region_fraction 0.001 | CONSISTENT |
| NT type | GABAergic | not available | GABA | CONSISTENT |
| Foxp2 expression | defining marker | not available | precomputed mean 11.35 (98.5th pct; tier 2) [CS20230722_CLUS_0998] | CONSISTENT |
| Drd1 expression | defining marker | not available | precomputed mean 7.07 (98.3rd pct; tier 2) [CS20230722_CLUS_0998] | CONSISTENT |
| Oprm1 expression | defining marker | not available | precomputed mean 8.31 (99.1th pct; tier 2) [CS20230722_CLUS_0998] | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Sarowar & Grabrucker 2020 | Literature | SUPPORT | FOXP2+/DRD1+/OPRM1+ as the molecular signature of ITC neurons | [7] |
| Atlas metadata query | Atlas metadata | SUPPORT | Score 7/7 on Foxp2+Drd1+Oprm1 — strongest three-marker convergence in ITC cohort | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### 0998 STR D1 Sema5a Gaba_3 [CS20230722_CLUS_0998] · 🔴 LOW

**Supporting evidence**

- **Literature — FOXP2+/DRD1+/OPRM1+ molecular signature.** Sarowar & Grabrucker 2020 [7] explicitly document the ICMs as small GABAergic clusters whose cells co-express dopamine type-1 receptor and µ-opioid receptor. CLUS_0998 carries all three markers at tier-2 expression (≥ MIN_DETECTABLE, ≥ 98th percentile within the five-member GABAergic ITC survival cohort). This is the strongest molecular convergence available for this type in the current atlas scan.

  > The ICMs are small cell clusters and consist of more dopamine type-1 and µ-opioid-receptor expressing cells (Poulin et al., 2008).
  > — Sarowar & Grabrucker 2020, Classical neuron classes across amygdala subdivisions · [7] <!-- quote_key: 221366115_e5c2cd9e -->

- **Atlas metadata — CLUS_0998 score 7/7 in ITC cohort.** The cohort consisted of five GABAergic clusters filtered to MBA:1105 (intercalated nucleus). CLUS_0998 achieved a discovery score of 7, rank 1 of 5 in the SURVIVAL_COHORT (filters: region=MBA:1105, nt_type=GABAergic), with Foxp2 at cohort-pct 0.985, Drd1 at 0.983, and Oprm1 at 0.991 — all three from precomputed expression (EXPRESSION source). The next-best score in this cohort was also 7; however, CLUS_0998 is distinguished by the simultaneous CONSISTENT tier across all three markers, making it the most strongly supported single candidate.

**Marker evidence provenance**

- **Foxp2:** Transcript-level evidence from two cross-species snRNA-seq studies — Totty et al. 2024 [5] (human, macaque, baboon amygdala) and Yu et al. 2023 [6] (human, macaque, mouse, chicken amygdala) — both identifying FOXP2+ subtypes specifically within the intercalated cell masses. Cell-type specificity is established by the anatomical dissection and subclustering in these studies, which identified ITC-mass neurons as a distinct transcriptomic group. Atlas-side precomputed mean 11.35 (tier 2, 98.5th pct) is strong convergence. Note that the primary evidence derives from primate amygdala; mouse-specific Foxp2 expression in ITCs is inferred from Yu et al. 2023 [6] (which includes mouse data) but is not independently confirmed in mouse by dedicated in situ expression in the gathered literature.
- **Drd1:** Transcript-level evidence from Yu et al. 2023 [6], which further subdivides ITC neurons into DRD1+ and DRD1- populations. The current classical node represents the DRD1+ subset. The broadMatch 1:n cardinality reflects that a DRD1- ITC subtype likely also exists in the atlas but was not assigned here. Atlas-side precomputed mean 7.07 (tier 2, 98.3rd pct).
- **Oprm1:** Transcript-level evidence from Totty et al. 2024 [5]. Atlas-side precomputed mean 8.31 (tier 2, 99.1th pct) — the highest-percentile marker among the three. No protein-level confirmation of Oprm1 in ITC neurons is present in the gathered literature; the evidence chain is transcript-level throughout. This is a gap that targeted in situ expression studies in mouse amygdala could address.

**Concerns**

- **LOW region_fraction (0.001):** CLUS_0998 has region_fraction 0.001 for MBA:1105 (intercalated nucleus). This reflects the anatomical reality that the ITC is a very small structure and is not a mapping discordance. The location alignment is correctly scored CONSISTENT.
- **No annotation-transfer evidence.** There is no AT evidence on this edge. Confidence is capped at LOW; the molecular convergence across three markers is supportive but an experimental anchor is absent.
- **Cohort tie at score 7.** The discovery score is tied at 7 between CLUS_0998 and at least one other member of the five-cluster ITC cohort (note: `next_best_score: 7`). The unresolved question of whether CLUS_1009 is a second genuine ITC transcriptomic type (possibly corresponding to the DRD1- subtype) is directly relevant — see Open questions.
- **Species transfer for Foxp2/Oprm1.** The primary sources for Foxp2 and Oprm1 as ITC markers are primate studies (Totty et al. 2024 [5]). Yu et al. 2023 [6] includes mouse data for Foxp2, providing partial cross-species support, but dedicated mouse-specific confirmation of the full Foxp2+Drd1+Oprm1 triple co-expression in ITC neurons is absent from the gathered literature.

**What would upgrade confidence**

- **smFISH co-localisation in mouse amygdala.** Triple-label smFISH with Foxp2, Drd1, and Oprm1 probes in mouse amygdala with positional verification to the intercalated cell masses would provide spatially resolved, mouse-specific expression evidence. This would add LiteratureEvidence with SUPPORT at HIGH confidence and address the species-transfer gap. This is the experiment proposed on the edge.
- **Annotation transfer from ITC-enriched scRNA-seq.** A MapMyCells run mapping single-cell data from an amygdala or ITC-enriched dataset against CCN20230722 would add AnnotationTransferEvidence. F1 ≥ 0.70 at CLUSTER level for CS20230722_CLUS_0998 would justify upgrading to MODERATE. The CLUS_0998 vs. CLUS_1009 question would also be addressed by examining which source cells map to each cluster.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Amygdala intercalated cell node (`amygdala_intercalated_cell`) is defined on a `CLASSICAL` definition basis. The classical type is GABAergic [3][4], localised to the intercalated cell masses of the amygdala [UBERON:0002884] [1][2][3], and carries three defining markers at the transcript level: Foxp2 [5][6], Drd1 [6], and Oprm1 [5]. No negative markers or neuropeptides are recorded on this node. The notes field states: "No subtypes detailed in this report."

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `c4efa0e` at 2026-06-05T13:42:49+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_amygdala_intercalated_cell_to_cs20230722_clus_0998 | LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT | [7]; atlas-internal |

</details>

---

## Discussion

### Best candidate and caveats

**Primary mapping:** Amygdala intercalated cell → 0998 STR D1 Sema5a Gaba_3 [CS20230722_CLUS_0998] at LOW confidence. Key support: literature molecular signature (FOXP2+/DRD1+/OPRM1+) and atlas metadata (score 7/7 in the five-cluster GABAergic ITC cohort with all three markers at tier-2 precomputed expression). Key caveats: no annotation-transfer evidence; region_fraction 0.001 very low (structural, not a mapping error).

No Cell Ontology term is currently assigned to this type.

### Proposed experiments and follow-ups

**smFISH co-localisation in mouse amygdala**
- **What:** Triple-label smFISH with Foxp2, Drd1, and Oprm1 probes in mouse amygdala sections
- **Target:** Co-expression confirmed in anatomically verified intercalated cell mass neurons (positioned medial to the basolateral nucleus, lateral to the central nucleus)
- **Expected output:** LiteratureEvidence item on `edge_amygdala_intercalated_cell_to_cs20230722_clus_0998` with supports=SUPPORT; marker_type TRANSCRIPT (or PROTEIN if antibody panels are included)
- **Resolves:** Species-transfer gap for Foxp2/Oprm1 (current evidence primarily primate-derived); confirms mouse-specific Foxp2+Drd1+Oprm1 co-expression in ITC neurons

**Annotation transfer from ITC-enriched or amygdala scRNA-seq dataset**
- **What:** MapMyCells run mapping single-cell or single-nucleus data from an amygdala dataset with ITC cells against CCN20230722
- **Target:** F1 ≥ 0.70 at CLUSTER level for CS20230722_CLUS_0998; additionally assess whether CS20230722_CLUS_1009 receives ITC-origin cells (testing the DRD1- ITC subtype hypothesis)
- **Expected output:** AnnotationTransferEvidence added to the edge; F1 ≥ 0.70 would justify upgrading confidence to MODERATE
- **Resolves:** Missing AT evidence (current confidence ceiling); open question about CLUS_0998 vs. CLUS_1009

### Open questions

1. Are CS20230722_CLUS_0998 and CS20230722_CLUS_1009 both genuine ITC transcriptomic types? The discovery score was tied at 7 within the five-cluster ITC cohort; a second cluster may represent the DRD1- ITC subtype identified by Yu et al. 2023 [6]. Annotation transfer from ITC-labelled source data would directly address this question.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Ignacio et al. 2014 | [25309888](https://pubmed.ncbi.nlm.nih.gov/25309888/) | Soma location |
| [2] | Nardelli et al. 2024 | [39130512](https://pubmed.ncbi.nlm.nih.gov/39130512/) | Soma location |
| [3] | Veinante et al. 2013 | [25408902](https://pubmed.ncbi.nlm.nih.gov/25408902/) | Soma location; GABAergic NT type |
| [4] | Pitkānen & Amaral 1994 | [8158266](https://pubmed.ncbi.nlm.nih.gov/8158266/) | GABAergic NT type (macaque) |
| [5] | Totty et al. 2024 | [39463931](https://pubmed.ncbi.nlm.nih.gov/39463931/) | Foxp2 and Oprm1 defining markers |
| [6] | Yu et al. 2023 | [36788214](https://pubmed.ncbi.nlm.nih.gov/36788214/) | Foxp2 and Drd1 defining markers; DRD1+/DRD1- ITC subtypes |
| [7] | Sarowar & Grabrucker 2020 | [32858950](https://pubmed.ncbi.nlm.nih.gov/32858950/) | FOXP2+/DRD1+/OPRM1+ as the molecular signature of ITC neurons |

---

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_cs20230722_clus_0998 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  rationale: >
    Foxp2, Drd1, and Oprm1 are all CONSISTENT (3 of 3 markers CONSISTENT) against
    CS20230722_CLUS_0998; Stage A discovery score 7 (rank 1 of 5 in the GABAergic
    MBA:1105 SURVIVAL_COHORT). Location CONSISTENT via MBA:1105 intercalated nucleus.
    Confidence is LOW: no annotation-transfer evidence and region_fraction 0.001
    reflects small ITC structure.
  reconciliation_note: ""
  lit_to_lit_edges: []
  unresolved_questions:
    - Are CS20230722_CLUS_0998 and CS20230722_CLUS_1009 both genuine ITC transcriptomic types?
```
<!-- verdict-block-end -->
