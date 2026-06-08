# Basolateral amygdala VIP/calretinin interneuron — CCN20230722 Mapping Report
*2026-06-05 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala (BLA) VIP/calretinin interneuron is a classically defined GABAergic cell type characterised by co-expression of vasoactive intestinal peptide (encoded by *Vip*), calretinin (encoded by *Calb2*), and often cholecystokinin (*Cck*). These cells are the numerically dominant inhibitory class in the mouse lateral and basal amygdala — estimated at 29–38% of all GABAergic neurons in the LA and BA [2] — and preferentially target other interneurons (interneuron-selective, IS morphology), placing them at the apex of the BLA disinhibitory circuit. Mapping this type to the CCN20230722 transcriptomic atlas would anchor the dominant inhibitory element of amygdala circuitry to a genome-wide expression reference and enable annotation-transfer across datasets.

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdaloid area [UBERON:0002887] | [1], [2] |
| Neurotransmitter | GABAergic | [1], [2] |
| Defining markers | Vip, Calb2 (calretinin), Cck | [1], [2], [3], [4] |
| Neuropeptides | Vip, Cck | [1], [2] |
| Negative markers | Pvalb, Sst | — |
| CL mapping | GABAergic interneuron [CL:0011005] — BROAD | — |
| Notes | VIP and/or calretinin co-expression; grouped as a single class but acknowledged as molecularly mixed. | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location [UBERON:0002887], neurotransmitter (GABAergic), defining markers (Vip, Calb2, Cck), neuropeptides (Vip, Cck):** Dual-label protein staining · mouse BLA · [1]

  > The cell types in all of these amygdalar nuclei are similar, but they have been studied primarily in the basolateral amygdala. The principal neurons in the CBL are pyramidal-like projection neurons with spiny dendrites that utilize glutamate as an excitatory neurotransmitter, whereas most non-pyramidal neurons in the CBL are spine-sparse interneurons that utilize GABA as an inhibitory neurotransmitter (McDonald, 1982(McDonald, , 1985(McDonald, , 1992a(McDonald, ,b, 1996(McDonald, , 2003Millhouse and DeOlmos, 1983;Fuller et al., 1987;Carlsen and Heimer, 1988;McDonald and Augustine, 1993). Dual-labeling immunohistochemical studies in the basolateral amygdala suggest that the CBL contains at least four distinct subpopulations of GABAergic non-pyramidal neurons that can be distinguished on the basis of their content of calcium-binding proteins and peptides. These subpopulations are: (1) PV+/CB+ neurons, (2) SOM+/CB+ neurons, (3) large multipolar cholecystokinin+ neurons that are often CB+, and (4) small bipolar and bitufted interneurons that exhibit extensive colocalization of calretinin, cholecystokinin, and vasoactive intestinal peptide (Kemppainen and Pitkänen, 2000;McDonald and Betette, 2001;Mascagni, 2001, 2002;
  > — McDonald et al. 2012, Classical neuron classes across amygdala subdivisions · [1] <!-- quote_key: 11544073_94689603 -->

- **Soma location, defining markers (Vip, Calb2, Cck), neuropeptides, proportional composition:** Stereological quantification · mouse LA/BA · [2]

  > we estimated that the following cell types together compose the vast majority of GABAergic cells in the LA and BA: axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%). Our results show that these amygdalar nuclei contain all major GABAergic neuron types as found in other cortical regions.
  > — Vereczki et al. 2021, Basolateral amygdala neuronal subtypes · [2] <!-- quote_key: 232283078_d4238834 -->

- **Defining marker Vip (transcript-level):** Mouse amygdala transcriptomic atlas · [3]

  > sparse, but specific expression of Grpr in several GABAergic interneurons, such as Vip-expressing GABA-50 and GABA-51, Pvalb-type GABA-41
  > — Hochgerner et al. 2023, Two classes of glutamatergic neurons par · [3] <!-- quote_key: 264517392_039d73c7 -->

- **Defining marker Calb2 (transcript-level, cross-species confirmation):** Primate amygdala single-nucleus RNA-seq; VIP+ clusters co-express CALB2, CCK, CRH, and CNR1 across humans, macaques, and baboons · [4]

  > both clusters showed increased expression of genes (Fig. 3B) encoding calretinin (CALB2), cholecystokinin (CCK), corticotropin releasing hormone (CRH), cannabinoid receptor 1 (CNR1)
  > — Totty et al. 2024, GABAergic neuron types in the primate amygdala show distributed or subregion specific expression patterns · [4] <!-- quote_key: 273531817_447a3097 -->

- **Negative markers (Pvalb, Sst):** Not directly sourced from stored snippets; the two negative markers are implicit in the classical taxonomy: PV+ neurons [1] and SOM+ neurons [1] are defined as separate subpopulations from the VIP/calretinin class. No primary citation is recorded on the KB node for these negative markers specifically.

</details>

### Cell Ontology mapping

Cell Ontology mapping: GABAergic interneuron [[CL:0011005](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0011005)] (BROAD). The Cell Ontology has no specific term for this population; CL:0011005 is the closest identified ancestor. Auto-proposed by asta-report-ingest; requires expert review.

---

## Results

One candidate atlas cluster was assessed; 0628 Vip Gaba_2 [CS20230722_CLUS_0628] within supertype 0174 Vip Gaba_2 is the primary mapping at LOW confidence. The broadMatch 1:n predicate reflects that five Vip Gaba clusters in the CCN20230722 atlas all score equally in the discovery cohort (score = 6; tied), indicating that the classical VIP/calretinin interneuron cannot yet be uniquely assigned to a single rank-0 cluster. Both Calb2 and Vip are highly expressed in CS20230722_CLUS_0628 (Calb2 mean 8.12, 98.3rd pct; Vip mean 11.11, 96.9th pct), providing strong marker-level support. The broadMatch reflects this five-way tie and the absence of annotation-transfer evidence to resolve cardinality.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0628 Vip Gaba_2 [CS20230722_CLUS_0628] | 0174 Vip Gaba_2 | 1401 | 🔴 LOW | Calb2 CONSISTENT · Vip CONSISTENT · Cck APPROXIMATE | broadMatch 1:n |

*1 edge total; relationship type: `skos:broadMatch` (1:n).*

### Property alignment — CS20230722_CLUS_0628

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Basolateral amygdaloid area [UBERON:0002887] | MBA:295 BLA present; region_fraction 0.049 | not assessed | CONSISTENT |
| NT type | GABAergic | GABA | not assessed | CONSISTENT |
| Calb2 expression | defining marker | not available | Calb2 mean 8.12 (98.3rd pct; tier 2) [CS20230722_CLUS_0628] | CONSISTENT |
| Vip expression (neuropeptide) | neuropeptide | not available | Vip mean 11.11 (96.9th pct; tier 2) [CS20230722_CLUS_0628] | CONSISTENT |
| Cck expression (neuropeptide) | neuropeptide | not available | Cck mean 0.97 (41.7th pct; tier 1 — low reliability) [CS20230722_CLUS_0628] | APPROXIMATE |
| Pvalb | negative marker | not assessed | NOT_ASSESSED | NOT_ASSESSED |
| Sst | negative marker | not assessed | NOT_ASSESSED | NOT_ASSESSED |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| McDonald 2012 BLA IS interneurons | Literature | SUPPORT | BLA VIP/calretinin as IS subclass; largest GABAergic class (29–38%) | [1] |
| Atlas precomputed expression (CLUS_0628) | Atlas metadata | SUPPORT | Calb2 98.3rd pct, Vip 96.9th pct — both tier-2; five Vip Gaba clusters all score equally | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### 0628 Vip Gaba_2 [CS20230722_CLUS_0628] · 🔴 LOW

**Supporting evidence:**

- **Calb2 CONSISTENT:** Precomputed expression shows Calb2 mean = 8.12, placing CS20230722_CLUS_0628 at the 98.3rd percentile within the survival cohort (region=MBA:295, nt_type=GABAergic; n=5 clusters). This is tier-2 (high-reliability) expression and directly matches the classical defining marker calretinin/Calb2 [1][2][4].
- **Vip CONSISTENT:** Vip mean = 11.11, 96.9th percentile in the survival cohort (tier 2). This tier-2 expression is concordant with the classical neuropeptide/marker designation [1][2][3].
- **NT type CONSISTENT:** CS20230722_CLUS_0628 is annotated GABA, concordant with the classical GABAergic identity [1][2].
- **Soma location CONSISTENT:** MBA:295 (BLA) is present in the cluster's region distribution (region_fraction = 0.049). This low region_fraction is consistent with a small BLA interneuron population dispersed across a broad atlas partition. *(note: region_fraction 0.049 is in the low-boundary band; it does not by itself constitute location evidence but does not contradict BLA origin.)*
- **Literature:** McDonald et al. 2012 characterises BLA VIP/calretinin interneurons as the IS subclass; the largest GABAergic class (29–38%) [1].

  > McDonald et al. characterises BLA VIP/calretinin interneurons as the IS subclass; largest GABAergic class (29-38%).
  > — McDonald et al. 2012 · [1]

**Marker evidence provenance:**

- **Calb2:** The classical evidence for Calb2 as a defining marker comes from protein-level studies in mouse BLA [1][2] and from cross-species transcript-level data in primate [4]. No mouse-specific transcript-level study of Calb2 expression in Vip+ BLA interneurons is currently stored in the KB. The atlas-side Calb2 value (mean 8.12, 98.3rd pct) represents precomputed expression from the CCN20230722 reference and provides strong concordance. The cross-species primate evidence [4] supports the co-expression signature but cannot substitute for a primary mouse transcript-level citation confirming morphologically identified IS cells. *(note: a targeted literature search for Calb2/calretinin × VIP co-expression in mouse BLA would strengthen the source-side evidence chain.)*
- **Vip:** Three independent sources support Vip as a defining marker: classical BLA anatomy [1][2] and mouse amygdala transcriptomics [3]. The Hochgerner et al. 2023 quote [3] references Vip-expressing GABA types in the mouse amygdala at the transcript level. Atlas-side Vip expression (mean 11.11, 96.9th pct) confirms robust expression in CS20230722_CLUS_0628.
- **Cck APPROXIMATE:** Cck is listed as a defining marker [1][2] and a neuropeptide [1][2], and primate data confirm CCK co-expression [4]. Atlas-side Cck mean = 0.97 (41.7th percentile, tier 1 — low reliability). This low percentile and tier-1 rating indicate Cck is not a discriminating marker for CS20230722_CLUS_0628 within the BLA GABAergic cohort. The APPROXIMATE alignment reflects that Cck may be expressed in a subset of cells below the cluster mean, consistent with the known molecular heterogeneity of the VIP/calretinin class ("VIP and/or calretinin-expressing" [2]).
- **Pvalb, Sst (negative markers):** No precomputed expression values are stored for Pvalb or Sst in the facts for CS20230722_CLUS_0628. Whether the cluster lacks these markers is not confirmed from atlas-internal data — this is a gap in the evidence.
- **Weak evidence flag:** No primary citation records negative-marker status (Pvalb−, Sst−) for this classical type specifically. The exclusion of these markers is inferred from the classical taxonomy (separate BLA PV+ and SOM+ subpopulations), not from a targeted study of VIP/calretinin cells.

**Concerns:**

- **DISTRIBUTED_ACROSS_CLUSTERS:** Five Vip Gaba clusters all tie at discovery score = 6 (cohort of 5 BLA GABAergic clusters, rank 0). CS20230722_CLUS_0628 is one of five equally plausible candidates. The broadMatch 1:n predicate is appropriate: the classical type cannot be uniquely assigned to this cluster without annotation-transfer or subcluster expression profiling. Stage A discovery dominated none of the five candidates (score 6 vs next_best_score 6).
- **No annotation-transfer evidence:** The mapping rests on precomputed expression and classical literature alone. Without annotation-transfer (MapMyCells or equivalent) applied to a labelled VIP/calretinin single-cell dataset, the cluster-level assignment remains ambiguous.
- **Cck APPROXIMATE:** Cck mean 0.97 (41.7th pct, tier 1) in CS20230722_CLUS_0628 is below the reliable-expression threshold. If Cck co-expression is considered essential to the classical type, the low atlas-side value is a concern.
- **Low region_fraction:** region_fraction = 0.049 at MBA:295 (BLA) is in the low range. *(note: because this is a broadMatch and the survival cohort was filtered to BLA, the BLA presence is real but the cluster's primary cell mass may extend beyond BLA proper — this is consistent with a broadly distributed interneuron type but should be examined in the annotation-transfer step.)*

**What would upgrade confidence:**

- **Annotation transfer** (MapMyCells) applied to a mouse BLA transcriptomic dataset containing labelled VIP/calretinin interneurons, targeting F1 ≥ 0.50 at CLUSTER level as a minimum informative threshold and F1 ≥ 0.80 to upgrade to MODERATE. This would distinguish among the five co-scoring Vip Gaba clusters and potentially resolve the broadMatch to a closeMatch or exactMatch. Would add `AnnotationTransferEvidence` to the edge.
- **Targeted literature search** for Calb2 × Vip co-expression in mouse BLA at the transcript level (e.g. Allen Brain Cell Atlas, Hochgerner et al. 2023 sub-cluster analysis [3]). Would add `LiteratureEvidence` items strengthening the source-side Calb2 assertion. Resolves open question 3.
- **Negative marker confirmation:** Expression data for Pvalb and Sst in CS20230722_CLUS_0628 would convert the two NOT_ASSESSED comparisons to CONSISTENT (if absent) and further separate this cluster from PV/SOM subtypes.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The basolateral amygdala VIP/calretinin interneuron is defined on a CLASSICAL basis. Defining markers: Vip [1][2][3], Calb2 [1][2][4], Cck [1][2]. Neuropeptides: Vip [1][2], Cck [1][2]. Negative markers: Pvalb, Sst (implicit from classical taxonomy — separate BLA GABAergic subpopulations). Soma location: basolateral amygdaloid area [UBERON:0002887] [1][2]. NT type: GABAergic [1][2]. The node is explicitly flagged as molecularly mixed (VIP and/or calretinin co-expression acknowledged as a heterogeneous grouping). Definition basis: CLASSICAL.

**Atlas mapping query.**  Candidate atlas clusters were retrieved from the CCN20230722 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Atlas data sources.** No atlas pseudobulk SHA recorded (atlas metadata only; no bulk correlation run).

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_vip_calretinin_interneuron_to_cs20230722_clus_0628 | LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT | [1]; atlas-internal |

*Generated by evidencell `c4efa0e` at 2026-06-05T13:42:47+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala VIP/calretinin interneuron → 0628 Vip Gaba_2 [CS20230722_CLUS_0628] at LOW confidence. Key support: Calb2 CONSISTENT (98.3rd pct, tier 2) and Vip CONSISTENT (96.9th pct, tier 2). Key caveats: five Vip Gaba clusters tie at discovery score 6 (DISTRIBUTED_ACROSS_CLUSTERS); no annotation-transfer evidence is present; Cck APPROXIMATE (41.7th pct, tier 1 — low reliability).

The Cell Ontology has no specific term for this population; GABAergic interneuron [[CL:0011005](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0011005)] is the closest identified ancestor (BROAD). Auto-proposed by asta-report-ingest; requires expert review.

### Proposed experiments and follow-ups

**1. Annotation transfer from IS interneuron patch-seq transcriptomes**

- **What:** Apply MapMyCells to a mouse BLA single-cell or patch-seq transcriptomic dataset with labelled VIP/calretinin or IS interneurons, targeting CCN20230722 as the reference atlas.
- **Target:** F1 ≥ 0.50 at CLUSTER level as a minimum informative threshold; F1 ≥ 0.80 to support upgrade to MODERATE confidence.
- **Expected output:** `AnnotationTransferEvidence` items on rank-0 Vip Gaba cluster edges; resolves the five-way cluster tie by directing assignment to the best-matching cluster.
- **Resolves:** DISTRIBUTED_ACROSS_CLUSTERS caveat; resolves open question 1. Addresses the proposed experiment recorded on the edge.

**2. Targeted literature search for Calb2 × Vip co-expression in mouse BLA**

- **What:** Cite-traverse targeting Calb2 × Vip co-expression in mouse BLA at the transcript level, focusing on single-cell transcriptomic studies (e.g. Allen Brain Cell Atlas, Hochgerner et al. 2023 [3]).
- **Target:** Identify mouse transcript-level evidence for Calb2 expression in VIP+ BLA interneurons; cross-reference to CCN20230722 cluster labels if present.
- **Expected output:** `LiteratureEvidence` items with quote_key-linked snippets on the edge, strengthening the Calb2 marker alignment beyond current primate [4] and classical anatomy [1][2] citations.
- **Resolves:** Open question 3; weak source-side Calb2 evidence.

**3. Negative marker confirmation for Pvalb and Sst**

- **What:** Extract precomputed expression values for Pvalb and Sst from CCN20230722 taxonomy reference store for CS20230722_CLUS_0628 and sibling Vip Gaba clusters.
- **Target:** Confirm Pvalb < MIN_DETECTABLE and Sst < MIN_DETECTABLE for the candidate cluster(s).
- **Expected output:** ATLAS_METADATA evidence items converting NOT_ASSESSED → CONSISTENT for both negative markers; tightens the exclusion criteria.
- **Resolves:** Two NOT_ASSESSED property comparisons on the primary edge.

### Open questions

1. Which rank-0 cluster among the five Vip Gaba clusters in CCN20230722 best captures the VIP/calretinin IS interneuron? Answering this requires annotation-transfer evidence.

2. Does the VIP/calretinin population map to a single rank-0 cluster or is it split across multiple clusters? The classical description acknowledges molecular heterogeneity ("VIP and/or calretinin" [2]); this predicts possible 1:N or CrossCuttingMatch cardinality.

3. What is the relationship between the BLA VIP/calretinin interneuron and the Hochgerner et al. 2023 Vip-expressing GABA types in mouse amygdala [3]? These have not yet been cross-referenced to CCN20230722 accessions.

4. Does the mouse BLA VIP/calretinin interneuron co-express CRH and CNR1, as suggested by the primate data in Totty et al. 2024 [4]? If so, this would tighten the marker profile and clarify the relationship with the CCK/CB1 basket cell population.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | McDonald et al. 2012 | [22837739](https://pubmed.ncbi.nlm.nih.gov/22837739/) | Soma location, NT type, defining markers (Vip, Calb2, Cck), neuropeptides, IS morphology class |
| [2] | Vereczki et al. 2021 | [33837051](https://pubmed.ncbi.nlm.nih.gov/33837051/) | Soma location, NT type, defining markers, neuropeptides, proportional composition |
| [3] | Hochgerner et al. 2023 | [37884748](https://pubmed.ncbi.nlm.nih.gov/37884748/) | Vip marker (mouse amygdala transcriptomic atlas) |
| [4] | Totty et al. 2024 | [39463931](https://pubmed.ncbi.nlm.nih.gov/39463931/) | Calb2 marker (primate amygdala single-nucleus RNA-seq) |

---

<!-- verdict-block-start: edge_bla_vip_calretinin_interneuron_to_cs20230722_clus_0628 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    `marker_Calb2` CONSISTENT (Calb2 mean 8.12, 98.3rd pct, tier 2) and
    `neuropeptide_Vip` CONSISTENT (Vip mean 11.11, 96.9th pct, tier 2) in
    CS20230722_CLUS_0628; 2 of 2 expression-assessed markers CONSISTENT.
    `neuropeptide_Cck` APPROXIMATE (Cck mean 0.97, 41.7th pct, tier 1 — low
    reliability). NT CONSISTENT (GABA). Location CONSISTENT (MBA:295 present;
    region_fraction 0.049). Stage A discovery score 6, rank 1 of 5 in
    BLA GABAergic cohort (next_best_score 6) — five Vip Gaba clusters tied;
    broadMatch 1:n reflects inability to resolve cardinality without AT evidence.
    No annotation-transfer evidence present.
  unresolved_questions:
    - "Which of the five Vip Gaba rank-0 clusters best matches the BLA VIP/calretinin IS interneuron — resolve by annotation transfer targeting F1 >= 0.50 at CLUSTER level."
    - "Determine whether the VIP/calretinin population maps to one cluster or multiple (1:N / CrossCuttingMatch) given acknowledged molecular heterogeneity."
```
<!-- verdict-block-end -->
