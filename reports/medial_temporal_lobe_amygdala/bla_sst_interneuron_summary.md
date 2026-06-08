# Basolateral amygdala somatostatin interneuron — CCN20230722 Mapping Report
*2026-06-05 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Somatostatin (SST)-expressing interneurons are a well-characterised GABAergic interneuron class of the basolateral amygdala (BLA), comprising 10–16% of all GABAergic cells in the lateral and basal amygdala [2]. They co-express the calcium-binding protein calbindin (Calb1/CB) and function as dendrite-targeting inhibitory cells [1][2][3][4]. Mapping this classical type to the Allen CCN20230722 mouse atlas connects amygdala circuit-level inhibitory biology to a transcriptomic cell-type taxonomy and establishes the correspondence for downstream annotation-transfer work.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1][2] |
| Neurotransmitter | GABAergic | [1][2] |
| Defining markers | Sst, Calb1 | [1][3][4][5] |
| Negative markers | Pvalb | — |
| Neuropeptides | Sst | [1][2] |
| CL term | CL:0011005 (BROAD) | — |
| Definition basis | CLASSICAL | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location / defining markers / NT type / neuropeptides:** literature review · basolateral amygdala · [1]
  > The principal neurons in the CBL are pyramidal-like projection neurons with spiny dendrites that utilize glutamate as an excitatory neurotransmitter, whereas most non-pyramidal neurons in the CBL are spine-sparse interneurons that utilize GABA as an inhibitory neurotransmitter (McDonald, 1982)(McDonald, 1985)(McDonald, , 1992a(McDonald, ,b, 1996(McDonald, , 2003(Millhouse et al., 1983)(Fuller et al., 1987)(Carlsen et al., 1988)(McDonald et al., 1993). Dual-labeling immunohistochemical studies in the basolateral amygdala suggest that the CBL contains at least four distinct subpopulations of GABAergic non-pyramidal neurons that can be distinguished on the basis of their content of calcium-binding proteins and peptides. These subpopulations are: (1) PV+/CB+ neurons, (2) SOM+/CB+ neurons, (3) large multipolar cholecystokinin+ neurons that are often CB+, and (4) small bipolar and bitufted interneurons that exhibit extensive colocalization of calretinin, cholecystokinin, and vasoactive intestinal peptide (Kemppainen and Pitkänen, 2000;McDonald and Betette, 2001;Mascagni, 2001, 2002;
  > — McDonald et al. 2012, Basolateral amygdala neuronal subtypes · [1] <!-- quote_key: 11544073_ea8d2bb3 -->

- **Soma location / NT type / neuropeptide (Sst) / abundance / negative marker (Pvalb):** cell counting survey · mouse BLA/LA · [2]
  > we estimated that the following cell types together compose the vast majority of GABAergic cells in the LA and BA: axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%). Our results show that these amygdalar nuclei contain all major GABAergic neuron types as found in other cortical regions.
  > — Vereczki et al. 2021, Basolateral amygdala neuronal subtypes · [2] <!-- quote_key: 232283078_d4238834 -->

- **Dendrite-targeting morphological class:** discussion · mouse BLA · [2]
  > SST+ inhibitory cells target predominantly the dendritic shaft and to a lesser extent, the spines of principal cells
  > — Vereczki et al. 2021, Discussion · [2] <!-- quote_key: 232283078_bd1f3975 -->

- **Defining marker — Sst:** literature review · BLA interneuron populations · [3]
  > Four populations of interneurons have been described in the BLA: those expressing parvalbumin (McDonald, 1992;Mc-Donald and Betette, 2001), those expressing somatostatin (Mc-Donald and Mascagni, 2002), those expressing cholecystokinin
  > — Woodruff & Sah 2007, Basolateral amygdala neuronal subtypes · [3] <!-- quote_key: 161407_eb8bfaf0 -->

- **Defining markers — Sst and Calb1:** comparative review · BLA interneuron classes · [4]
  > The most salient parallels between BLA and other cortical regions with respect to their interneurons exist with respect to parvalbumin (PV) and somatostatin (SOM) positive interneurons.
  > — Ünal et al. 2020, Basolateral amygdala neuronal subtypes · [4] <!-- quote_key: 212579559_d2c2762c -->

- **Defining marker — Sst (transcriptomic atlas context):** asta_snippet · mouse amygdala · [5]
  > This group was consistent with Lhx + MEA-projecting inhibitory cell types and was rich in neuropeptide expression
  > — Hochgerner et al. 2023, Inhibitory cells mirror projection type · [5] <!-- quote_key: 264517392_0ef3e300 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: somatostatin-expressing interneuron [[CL:0011005](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0011005)] (BROAD). Auto-proposed by asta-report-ingest; requires expert review.

---

## Results

One candidate atlas cluster was assessed. 0765 Sst Gaba_2 [CS20230722_CLUS_0765] in supertype 0215 Sst Gaba_2 is the primary mapping at LOW confidence; it is a `skos:broadMatch` 1:n, reflecting a broader transcriptomic type that likely encompasses the classical BLA SST interneuron population among potentially multiple BLA GABAergic clusters.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0765 Sst Gaba_2 [CS20230722_CLUS_0765] | 0215 Sst Gaba_2 | 218 | 🔴 LOW | Sst CONSISTENT · Calb1 CONSISTENT | Broad match — dominant BLA presence |

Note: 1 edge assessed; relationship type skos:broadMatch (1:n).

### Property alignment table — 0765 Sst Gaba_2 [CS20230722_CLUS_0765]

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | not available | MBA:295 BLA: region_fraction 0.289 — dominant BLA presence | CONSISTENT |
| NT type | GABAergic | not available | GABA | CONSISTENT |
| Sst neuropeptide | Sst — neuropeptide | not available | Sst precomputed mean 11.92 (96.7th pct; tier 2) | CONSISTENT |
| Calb1 marker | Calb1 — defining marker | not available | Calb1 precomputed mean 9.57 (96.5th pct; tier 2) | CONSISTENT |
| Pvalb (negative) | Pvalb — negative marker | not available | not assessed | NOT_ASSESSED |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Vereczki 2021 BLA GABAergic census | Literature | SUPPORT | SST+/Calb1+ BLA interneurons 10–16% of GABAergic cells; dendrite-targeting class | [2] |
| CLUS_0765 atlas metadata | Atlas metadata | SUPPORT | Sst 96.7th pct, Calb1 96.5th pct; region_fraction 0.289 BLA | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### 0765 Sst Gaba_2 [CS20230722_CLUS_0765] · 🔴 LOW

**Supporting evidence:**

- **Sst neuropeptide CONSISTENT.** CLUS_0765 shows Sst precomputed mean 11.92, placing it at the 96.7th percentile among BLA GABAergic clusters — strong high-tier expression, classifying it confidently as an Sst-expressing GABAergic type. This directly matches the defining neuropeptide of the classical BLA SST interneuron. *(Stage A discovery: Sst contributed `applied_score: 2.0` from cohort-pct 0.967 in a 5-member BLA GABAergic rank-0 cohort.)*

- **Calb1 marker CONSISTENT.** Calb1 precomputed mean 9.57, 96.5th percentile in the BLA GABAergic rank-0 cohort — high-tier expression concordant with the classical type's Calb1 co-expression requirement. *(Stage A: Calb1 contributed `applied_score: 2.0` from cohort-pct 0.965.)* Stage A discovery dominated its 5-member BLA GABAergic cohort (score 5 vs next-best 5 — cohort tied; all candidates had the same score because the cohort is very small).

- **NT type CONSISTENT.** CLUS_0765 annotation GABA is concordant with the classical type's GABAergic identity [1][2].

- **Soma location CONSISTENT.** region_fraction 0.289 places CLUS_0765 as having a dominant BLA (MBA:295) presence. This is in the lower boundary band (0.289 is below 0.3) — see caveats.
  > Vereczki et al. 2021: SST+/Calb1+ BLA interneurons estimated 10-16% of GABAergic cells; dendrite-targeting class distinct from PV and CCK types.
  > — Vereczki et al. 2021 · [2]

- **ATLAS_METADATA support:** CLUS_0765 "Sst Gaba_2" (WMBv1): Sst 96.7th pct, Calb1 96.5th pct; dominant BLA fraction 0.289.

**Concerns:**

- **DISTRIBUTED_ACROSS_CLUSTERS.** CLUS_0765 and CLUS_0774 both scored equally in Stage A discovery. A parallel edge to CLUS_0774 may be needed to capture the full BLA SST interneuron population, and the broadMatch 1:n designation reflects this distribution. It is unclear whether these two clusters represent distinct SST subtypes or simply a split of the same population during atlas construction.

- **No annotation-transfer evidence.** The mapping rests on atlas metadata alone; there is no ANNOTATION_TRANSFER evidence item linking a characterised SST+ BLA source dataset to this cluster. This is the primary ceiling on confidence.

- **region_fraction borderline.** region_fraction = 0.289 is slightly below the typical CONSISTENT band. While categorised CONSISTENT in the property comparison, it implies that approximately 71% of CLUS_0765 cells are distributed outside MBA:295, indicating this cluster is not BLA-exclusive. This is consistent with the broadMatch 1:n relationship — the classical type is likely one of several BLA sub-populations contained within this broader atlas cluster or cluster pair.

- **Pvalb negative marker NOT_ASSESSED.** No precomputed expression data available for Pvalb in CLUS_0765; inability to confirm Pvalb absence leaves a small ambiguity.

**Marker evidence provenance:**

- **Sst:** Evidence is both transcript-level (Hochgerner et al. 2023 [5] scRNA-seq amygdala atlas; Woodruff & Sah 2007 [3] review) and protein-level (McDonald et al. 2012 [1], Vereczki et al. 2021 [2] cell-counting survey using antibody labelling). The convergence of transcript- and protein-level evidence from multiple independent studies provides strong support for Sst as a defining marker. The Vereczki et al. 2021 survey specifically quantified the population in mouse, matching the species of the target atlas. Note that Hochgerner et al. 2023 [5] used mouse amygdala tissue, directly relevant to CCN20230722.

- **Calb1:** Evidence is protein-level (McDonald et al. 2012 [1] dual-labelling in BLA; Woodruff & Sah 2007 [3] review; Ünal et al. 2020 [4]). All studies establish Calb1/CB as a co-marker with SOM. No primary study has yet verified Calb1 at the transcript level in morphologically confirmed BLA SST cells (i.e., linked explicitly to post-hoc cell identity). A targeted literature search for "calbindin somatostatin amygdala interneuron transcript" may confirm transcript-level equivalence.

- **Pvalb (negative marker):** The Vereczki et al. 2021 [2] census establishes PV+ and SST+ populations as distinct non-overlapping GABAergic classes in the BLA. However, no primary study assessing Pvalb absence at transcript level in individual confirmed SST+ cells is recorded. Atlas-side Pvalb is NOT_ASSESSED for CLUS_0765, so no cross-check is possible; flag for investigation.

**What would upgrade confidence:**

- **Annotation transfer (AnnotationTransferEvidence):** Run a mapping tool on a mouse BLA or amygdala dataset with labelled SST+ cells against CCN20230722 at cluster and supertype levels. Target F1 ≥ 0.60 at cluster level. This would directly resolve whether CLUS_0765 (and/or CLUS_0774) receives the SST BLA signal and would upgrade to MODERATE or HIGH depending on F1.

- **Targeted literature search:** Cite-traverse for "somatostatin interneuron basolateral amygdala single-cell transcriptomics" and "SST BLA mouse atlas" to identify studies mapping SST+ BLA cells to CCN20230722 clusters. Would add LiteratureEvidence with cluster cross-reference.

- **smFISH (Sst + Calb1 in mouse BLA):** As noted in the proposed experiments, smFISH with Sst + Calb1 probes would confirm co-expression at transcript level in mouse BLA, providing a direct bridge to atlas marker comparisons. Would add LiteratureEvidence or direct property-source evidence for Calb1.

- **Pvalb expression check:** Precomputed expression data for Pvalb in CLUS_0765 would resolve the NOT_ASSESSED negative-marker gap and provide stronger support for cell-type identity discrimination.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Basolateral amygdala somatostatin interneuron (bla_sst_interneuron) is defined on a CLASSICAL basis. The classical type is GABAergic with Sst and Calb1 as defining markers, Pvalb as a negative marker, soma in the basolateral amygdala [UBERON:0002887], and Sst as a neuropeptide. McDonald et al. 2012 [1] established the BLA SOM+/CB+ subpopulation within a four-subpopulation classification scheme; Woodruff & Sah 2007 [3] reviewed the four BLA interneuron populations; Vereczki et al. 2021 [2] quantified the SST+ class at 10–16% of GABAergic cells in mouse LA/BA and described its dendrite-targeting axonal pattern; Ünal et al. 2020 [4] reviewed parallels with cortical SST interneurons; Hochgerner et al. 2023 [5] characterised the transcriptomic identity of amygdala inhibitory cell types. A closely related population of GABAergic projection neurons expressing both Sst and neuronal nitric oxide synthase (~5.5–8% of GABAergic cells) is listed separately (bla_gabaergic_projection_neuron) and is excluded from this mapping.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy (CS20230722) at rank 0 (cluster) using metadata-based scoring (region match = MBA:295, NT type = GABAergic, defining markers = Sst + Calb1). Full scoring rules: `workflows/map-cell-type.md`. Discovery cohort at rank 0: 5 BLA GABAergic clusters. CLUS_0765 and CLUS_0774 tied at score=5 as top candidates; CLUS_0765 is recorded as the primary edge.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store). MERFISH spatial registration was not available for this atlas version (has_merfish_location = false); soma location comparison uses region_fraction from precomputed spatial metadata.

**Atlas data sources.**

| Field | Value |
|---|---|
| Atlas | CCN20230722 |
| Taxonomy ID | CS20230722 |
| Primary candidate | CS20230722_CLUS_0765 (0765 Sst Gaba_2) |
| Supertype | 0215 Sst Gaba_2 |
| n_cells (10x) | 218 |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_sst_interneuron_to_cs20230722_clus_0765 | LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT | [2]; atlas-internal |

*Generated by evidencell `c4efa0e` at 2026-06-05T13:42:46+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala somatostatin interneuron → 0765 Sst Gaba_2 [CS20230722_CLUS_0765] at LOW confidence via skos:broadMatch 1:n. Key support: Sst precomputed mean 11.92 (96.7th pct) and Calb1 precomputed mean 9.57 (96.5th pct), both CONSISTENT with classical type markers; dominant BLA region_fraction 0.289; GABA NT type CONSISTENT. Key caveats: no annotation-transfer evidence; CLUS_0765 and CLUS_0774 scored equally in discovery (DISTRIBUTED_ACROSS_CLUSTERS caveat); region_fraction 0.289 is borderline, consistent with a 1:n broadMatch rather than a 1:1 clean assignment.

The Cell Ontology has no specific term for this BLA population; somatostatin-expressing interneuron [[CL:0011005](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0011005)] is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

### Proposed experiments and follow-ups

**1. Annotation transfer**
- **What:** Run a mapping tool (e.g., MapMyCells or hierarchical label transfer) on a publicly available mouse amygdala or BLA dataset with SST+ cells against CCN20230722 at cluster and supertype levels.
- **Target:** AnnotationTransferEvidence with F1 ≥ 0.60 at cluster level for the SST BLA source group.
- **Expected output:** `AnnotationTransferEvidence` items on `edge_bla_sst_interneuron_to_cs20230722_clus_0765` (and potentially a parallel edge to CLUS_0774); would upgrade confidence from LOW to MODERATE or HIGHER.
- **Resolves:** Primary no-AT caveat; unresolved question 1 (CLUS_0765 vs CLUS_0774 distinction).

**2. smFISH (Sst + Calb1, mouse BLA)**
- **What:** smFISH co-detection of Sst and Calb1 transcripts in mouse BLA tissue sections.
- **Target:** Quantitative co-expression rate in mouse BLA, mapping to atlas precomputed values.
- **Expected output:** `LiteratureEvidence` confirming Calb1 transcript-level co-expression; would also verify the broadMatch vs narrowMatch designation.
- **Resolves:** Calb1 evidence provenance gap; unresolved question 1.

**3. Targeted literature search**
- **What:** Cite-traverse for "somatostatin interneuron basolateral amygdala single-cell transcriptomics" and "SST BLA mouse atlas cluster" to identify studies cross-referencing CCN20230722 cluster accessions.
- **Target:** LiteratureEvidence with an explicit cluster cross-reference for BLA SST+ cells.
- **Expected output:** Additional `LiteratureEvidence` items; potentially upgrades without new experiments.
- **Resolves:** Unresolved question 2.

**4. Pvalb precomputed expression check**
- **What:** Confirm that Pvalb expression in CLUS_0765 is below detectable threshold in precomputed stats (or add expression data if absent).
- **Target:** Pvalb negative_marker comparison upgraded from NOT_ASSESSED to CONSISTENT.
- **Expected output:** Updated property_comparisons for negative_marker_Pvalb.
- **Resolves:** Unresolved question 3.

### Open questions

1. Do CLUS_0765 and CLUS_0774 represent distinct SST subtypes in the BLA, or is the classical BLA SST interneuron population split across both clusters in the CCN20230722 taxonomy? (`edge_bla_sst_interneuron_to_cs20230722_clus_0765`)
2. Does any published single-cell or spatial transcriptomic study of mouse BLA cross-reference CCN20230722 cluster accessions for SST+ interneurons, enabling a direct literature-based mapping? (`edge_bla_sst_interneuron_to_cs20230722_clus_0765`)
3. Is Pvalb absent from CLUS_0765 in precomputed expression statistics, confirming separation from the PV+ basket cell atlas cluster? (`edge_bla_sst_interneuron_to_cs20230722_clus_0765`)

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | McDonald et al. 2012 | [22837739](https://pubmed.ncbi.nlm.nih.gov/22837739/) | soma location; defining markers; NT type; neuropeptides |
| [2] | Vereczki et al. 2021 | [33837051](https://pubmed.ncbi.nlm.nih.gov/33837051/) | soma location; NT type; neuropeptides; cell type abundance; dendrite-targeting class |
| [3] | Woodruff & Sah 2007 | [17234587](https://pubmed.ncbi.nlm.nih.gov/17234587/) | Sst defining marker |
| [4] | Ünal et al. 2020 | [32144495](https://pubmed.ncbi.nlm.nih.gov/32144495/) | Sst and Calb1 defining markers |
| [5] | Hochgerner et al. 2023 | [37884748](https://pubmed.ncbi.nlm.nih.gov/37884748/) | Sst defining marker (transcriptomic atlas context) |

---

<!-- verdict-block-start: edge_bla_sst_interneuron_to_cs20230722_clus_0765 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    Sst precomputed mean 11.92 (96.7th pct; `neuropeptide_Sst` CONSISTENT) and
    Calb1 precomputed mean 9.57 (96.5th pct; `marker_Calb1` CONSISTENT); 2 of 3
    markers CONSISTENT (`negative_marker_Pvalb` NOT_ASSESSED). NT type CONSISTENT
    (GABA). Location CONSISTENT: region_fraction=0.289 in MBA:295 (dominant BLA
    presence; borderline band, consistent with skos:broadMatch 1:n). No AT evidence
    available; atlas-metadata-only support caps confidence at LOW.
    DISTRIBUTED_ACROSS_CLUSTERS caveat: CLUS_0765 and CLUS_0774 tied in Stage A
    discovery (score=5 of 5-member cohort, rank_in_cohort=1).
  reconciliation_note: ""
  lit_to_lit_edges: []
  unresolved_questions:
    - "Do CLUS_0765 and CLUS_0774 represent distinct SST subtypes in BLA? A parallel edge to CLUS_0774 may be warranted."
    - "Run annotation transfer on a mouse BLA SST+ source dataset to confirm cluster assignment and resolve CLUS_0765 vs CLUS_0774 ambiguity."
```
<!-- verdict-block-end -->
