# Cerebellar stellate cell (molecular layer interneuron) — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml`*

---

## Introduction

Cerebellar stellate cells are GABAergic interneurons residing in the outer (upper) molecular layer of the cerebellar cortex [UBERON:0002974]. Together with basket cells, they constitute the two classes of molecular layer interneurons (MLIs) that provide feedforward and lateral inhibition to Purkinje cells, controlling their firing rate and the precise timing of action potential discharge. Stellate cells are distinguished from basket cells primarily by their position in the upper molecular layer and by targeting the distal dendritic shafts of Purkinje cells rather than the soma or axon initial segment, though the two populations form a morphological continuum. Mapping this classical type to WMBv1 atlas clusters is complicated by the fact that the transcriptomic taxonomy does not draw a clean boundary between stellate and basket cells — both share Pvalb and RORa, and no stellate-specific marker has been reported.

| Property | Value | References |
|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] (outer/upper third); cerebellar cortex [UBERON:0002129] (coarse query term) | [1], [2], [3] |
| NT type | GABAergic | [4] |
| Defining markers | Pvalb, RORa, Grid1 | [1], [5] |
| Negative markers | — | |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** literature · Brown et al. 2018 [1], Jahncke & Wright 2024 [2], Miyazaki et al. 2021 [3]
  > Stellate cells terminate on the shaft of the Purkinje cell dendritic tree 34
  > — Brown et al. 2018, Anatomical organization and core cell types · [1] <!-- quote_key: 59945454_5ca8f6ac -->

  > Upper MLIs corresponding to stellate cells innervate dendritic shafts of PCs.
  > — Miyazaki et al. 2021, Results · [3] <!-- quote_key: 239017682_4f0c2aa3 -->

  > The simple, well-defined, and stereotyped circuitry of the cerebellum makes it an ideal model system for studying synapse development and maintenance (Figure 1). At the center of the circuit are Purkinje cells (PCs), which are the primary output neurons of the cerebellum and project their axons to the deep cerebellar nuclei (DCN) and the vestibular nuclei in the brainstem. Purkinje cells receive excitatory inputs from two different sources. Parallel fibers originate from cerebellar granule cells, the most numerous neuron type in the brain, and provide a large number of weak excitatory inputs to the dendrites of Purkinje cells (Itō, 1984;Palay & Chan-Palay, 2012). Climbing fibers originate from excitatory neurons in the inferior olive, and their axons wrap around the primary dendritic branches of Purkinje cells, forming strong excitatory contacts (Itō, 1984;Palay & Chan-Palay, 2012). In mouse, Purkinje cells initially receive inputs from multiple climbing fibers, which undergo activity-dependent pruning during the first 3 weeks of postnatal development until a 1:1 ratio is achieved (Bosman et al., 2008)(Bosman et al., 2009)(Crépel et al., 1976), but see (Busch et al., 2023). These inputs represent one of the best-studied examples of synaptic competition in the central nervous system (CNS). Purkinje cells receive the majority of their inhibitory inputs from two types of Molecular Layer Interneurons (MLIs): Basket Cells (BCs) and Stellate Cells (SCs) (Itō, 1984;Palay & Chan-Palay, 2012). BCs form inhibitory contacts on the soma and proximal dendrites of Purkinje cells, whereas SCs innervate the distal dendrites. Each BC/SC contacts multiple Purkinje cells in the same sagittal plane. There are also recurrent inhibitory connections between Purkinje cells (Altman, 1972;Bernard & Axelrad, 1993;Witter et al., 2016)
  > — Jahncke & Wright 2024, Anatomical organization and core cell types · [2] <!-- quote_key: 268857461_d94370f3 -->

- **NT type:** Briatore et al. 2010 [4]
  > . Stellate and basket cells are the only ML interneurons (MLIs) known to use GABA as a neurotransmitter (Shepherd, 1974). They are distinguished by their position in the upper and lower ML and by their axonal distribution [1,3], although intermediate forms have been described, raising the possibility that MLIs represent a continuum that varies gradually (Sultan et al., 1998)(Schilling et al., 2008). Basket cell axons, in particular, surround the cell bodies of Purkinje cells and also form a characteristic plexus around the axon initial segment, whereas stellate cells make synapses exclusively on the dendritic arbor. Collectively, MLIs provide feed-forward and lateral inhibition to Purkinje cells, thus controlling their firing rate, the precise timing of action potential firing and the spread of activity [4,(Mittmann et al., 2005)[17]. In addition to targeting Purkinje cells, MLIs make synapses with each other, and likely with Golgi cell dendrites. The existence of such synapses is supported by both electron microscopic analyses [3] and electrophysiological recordings (Mittmann et al., 2005)(Llano et al., 1993)(Kondo et al., 1998)(Chavas et al., 2003)
  > — Briatore et al. 2010, Anatomical organization and core cell types · [4] <!-- quote_key: 1460508_88d765d5 -->

- **Pvalb (defining marker):** immunofluorescence colocalization · Brown et al. 2018 [1]
  > The reporter expressing cells colocalized with the expression of parvalbumin, which is a well-known marker for Purkinje cells and molecular layer interneurons (Figs 1f,g and 2d) (Stichel et al., 1986)
  > — Brown et al. 2018, Anatomical organization and core cell types · [1] <!-- quote_key: 59945454_1c861584 -->

- **RORa (defining marker):** immunofluorescence · Brown et al. 2018 [1]
  > The distribution of reporter expression in stellate versus basket cells was validated by RAR-related orphan receptor alpha (RORα) expression (Fig. 2c, per condition: N = 3, n = 9), which also marks molecular layer interneurons and Purkinje cells (Maricich et al., 1999)(Hamilton et al., 1996)(Ino, 2004)(Sillitoe et al., 2008)
  > — Brown et al. 2018, Anatomical organization and core cell types · [1] <!-- quote_key: 59945454_b21703e0 -->

- **Grid1 (defining marker):** mRNA expression + immunoreactivity · Konno et al. 2014 [5]
  > In the cerebellar cortex, GluD1 mRNA was expressed at the highest level in molecular layer interneurons and its immunoreactivity was concentrated at PF synapses on interneuron somata. In GluD1-knock-out mice, the density of PF synapses on interneuron somata was significantly reduced and the size and number of interneurons were significantly diminished. Therefore, GluD1 is common to GluD2 in expression at PF synapses, but distinct from GluD2 in neuronal expression in the cerebellar cortex; that is, GluD1 in interneurons and GluD2 in PCs. Furthermore, GluD1 regulates the connectivity of PF–interneuron synapses and promotes the differentiation and/or survival of molecular layer interneurons.
  > — Konno et al. 2014, Functional roles and physiology · [5] <!-- quote_key: 8585958_c30f821f -->

</details>

Cell Ontology mapping: cerebellar stellate cell [[CL:0010010](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0010010)] (EXACT).

---

## Results

Atlas metadata alignment places 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] as the primary candidate for the cerebellar stellate cell, leading a 50-member GABAergic cerebellar cohort (discovery score 7 vs. next-best 6) with Pvalb and Grid1 both CONSISTENT at high cerebellar cohort percentiles (see property comparison table below). A second CBX MLI cluster, 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189], carries the same supertype label and shows concordant Pvalb and Grid1 expression but represents a much smaller population (154 cells vs. 31,095); both clusters warrant recording, though the transcriptomic basis for separating stellate from basket cells within the CBX MLI population remains unresolved.

---

### 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Atlas cluster (5188) | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] (primary, region_fraction_100um: 0.841 lower_bound) | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Pvalb expression | Defining marker | Pvalb: 11.12; cohort_pct 0.995 | CONSISTENT |
| RORa expression | Defining marker | No atlas expression data | NOT_ASSESSED |
| Grid1 expression | Defining marker | Grid1: 9.85; cohort_pct 0.989 | CONSISTENT |

*(Child-cluster breakdown not assessed — no supertype edge for the parent supertype 1149 CBX MLI Megf11 Gaba_1 appears in the current graph; per-lobule information (ansiform, simple lobule) is visible in the atlas location field.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node 5188 metadata | ATLAS_METADATA | PARTIAL | region_fraction_100um=0.841; strict=0.720; lower_bound | atlas-internal |

**Supporting evidence:**
- Pvalb expression is CONSISTENT, at the 99.5th percentile of the 50-member GABAergic cerebellar cohort (mean 11.12). Parvalbumin is a well-established marker for MLIs including stellate cells, confirmed by immunofluorescence in morphologically identified cells [1].
- Grid1 (GluD1) expression is CONSISTENT, at the 98.9th percentile of the same cohort (mean 9.85). Grid1 was established as a defining marker of cerebellar molecular layer interneurons at both mRNA and protein level [5].
- The cluster name "CBX MLI Megf11 Gaba_1" directly encodes cerebellar cortex (CBX) and molecular layer interneuron (MLI) identity, consistent with the classical soma location (molecular layer of cerebellar cortex [UBERON:0002974]).
- Region signal: region_fraction_100um = 0.841 (lower_bound rollup — true value may be higher); strict region_fraction = 0.720. The dominant painted region is Cerebellum [MBA:512], with ansiform and simple lobules as top sub-regions. This is a strong cerebellar location match.
- Discovery score of 7 dominated the 50-member cerebellar GABAergic cohort at rank 0 (next-best 6 across 4 competitors), driven by Pvalb contributing applied_score 2.0 (pct 0.995 of 50) and Grid1 contributing applied_score 2.0 (pct 0.989 of 50).

**Marker evidence provenance:**

- **Pvalb**: Protein-level (immunofluorescence) in Brown et al. 2018 [1], validated in cells containing a stellate-basket cell reporter. The study confirmed colocalization with parvalbumin in MLI populations, though morphological confirmation of stellate identity was at the population level rather than single-cell reconstruction. Pvalb is shared with basket cells and Purkinje cells; it is a shared-MLI marker rather than stellate-specific.
- **RORa**: Protein-level (immunofluorescence) in Brown et al. 2018 [1]. RORa is also shared with basket cells and Purkinje cells. No atlas expression data are available for RORa on this cluster — NOT_ASSESSED.
- **Grid1**: mRNA (ISH) and protein (immunoreactivity) in Konno et al. 2014 [5], confirmed specific to MLI (GluD1) vs. Purkinje cell (GluD2) compartments. This is the most MLI-specific marker in the panel, establishing Grid1 at transcript level in interneurons. Grid1 on 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] is at the 98.9th cohort percentile — strongly supportive.
- **Supertype-name circularity:** None of the three classical markers match the supertype name "Megf11" — no circularity concern.
- **No stellate-specific marker exists** in the currently gathered literature; Pvalb and RORa are shared across the MLI-Purkinje continuum. This is a fundamental gap that prevents distinguishing stellate from basket at the classical-evidence level (see classical node notes). A novel stellate-specific marker, if identified, would resolve ambiguity.

**Concerns:**
- Region fraction is reported as a lower_bound rollup — non-painted CCF2020 descendants are uncounted. The floor value (region_fraction_100um ≥ 0.841) is strongly supportive, but the true value could be higher.
- RORa is not assessable from atlas precomputed expression; one of three defining markers remains NOT_ASSESSED.
- No annotation transfer evidence is available. The mapping rests entirely on atlas metadata and marker expression; direct transcriptomic bridging from a classical stellate cohort (e.g. patch-seq cells with morphological reconstruction) is absent.
- The transcriptomic MLI classification in WMBv1 (CBX MLI subtypes) does not directly correspond to the morphological stellate/basket divide. 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] may contain both stellate and basket cells, or may selectively capture one population — this is currently unresolved.

**What would upgrade confidence:**
- Annotation transfer from a patch-seq dataset targeting morphologically confirmed stellate cells (upper ML position, dendritic targeting), with F1 ≥ 0.70 at CLUSTER level, would establish a direct transcriptomic bridge.
- Atlas expression data for RORa would resolve the NOT_ASSESSED property comparison.
- A targeted literature search for single-cell transcriptomic papers distinguishing MLI subtypes in the mouse cerebellum (e.g. distinguishing Megf11-expressing clusters from other MLI classes) would clarify whether 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] maps preferentially to stellate morphology.

---

### 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Atlas cluster (5189) | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] (primary, region_fraction_100um: 0.861 lower_bound) | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Pvalb expression | Defining marker | Pvalb: 9.90; cohort_pct 0.962 | CONSISTENT |
| RORa expression | Defining marker | No atlas expression data | NOT_ASSESSED |
| Grid1 expression | Defining marker | Grid1: 8.06; cohort_pct 0.598 | CONSISTENT |

*(Child-cluster breakdown not assessed — 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] is itself a rank-0 cluster under supertype 1149 CBX MLI Megf11 Gaba_1, which is also the parent of 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188].)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node 5189 metadata | ATLAS_METADATA | PARTIAL | region_fraction_100um=0.861; strict=0.764; lower_bound | atlas-internal |

**Supporting evidence:**
- Pvalb is CONSISTENT at the 96.2nd cohort percentile (mean 9.90); Grid1 is CONSISTENT at the 59.8th percentile (mean 8.06) — both above the CONSISTENT threshold, though Grid1 is notably weaker here than on the primary candidate. The same MLI marker profile applies; see marker provenance under the primary candidate above.
- Region signal: region_fraction_100um = 0.861 (lower_bound); strict = 0.764. The dominant painted region is Cerebellum [MBA:512], consistent with cerebellar identity.
- 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] shares the supertype 1149 CBX MLI Megf11 Gaba_1 with the primary candidate, placing it in the same broader transcriptomic grouping.
- n_cells = 154 — a small cluster relative to the primary candidate (31,095 cells). Whether this represents a distinct stellate subpopulation, a technical artifact, or lobule-specific enrichment is not resolvable from current evidence.

**Concerns:**
- Grid1 at cohort_pct 0.598 is weaker than on the primary candidate (0.989), though the absolute expression value (8.06) is still in the moderate-high range. The lower cohort percentile reduces the discriminatory strength of this marker here.
- The very small n_cells (154) limits confidence; this may be a satellite cluster or a subpopulation of the main CBX MLI Megf11 class.
- Same region lower_bound caveat as the primary candidate applies.
- RORa remains NOT_ASSESSED.
- No annotation transfer evidence.

**What would upgrade confidence:**
- Same experiments as for the primary candidate (patch-seq AT, RORa atlas expression) would also help resolve whether 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] represents a distinct stellate subpopulation or is biologically redundant with the primary candidate.
- Inspection of which lobules preferentially contribute to the primary vs. secondary candidate (ansiform/simple lobule breakdown) may shed light on whether the cluster separation is anatomical.

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] | 1149 CBX MLI Megf11 Gaba_1 | 31,095 | 🟡 MODERATE | Pvalb CONSISTENT pct 0.995; Grid1 CONSISTENT pct 0.989 | Primary |
| 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] | 1149 CBX MLI Megf11 Gaba_1 | 154 | 🟡 MODERATE | Pvalb CONSISTENT pct 0.962; Grid1 CONSISTENT pct 0.598 | Secondary (same supertype as primary) |
| 5079 NTS-PARN Neurod2 Gly-Gaba_1 [CS20230722_CLUS_5079] | 1130 NTS-PARN Neurod2 Gly-Gaba_1 | 212 | 🔴 LOW | Pvalb APPROXIMATE; dominant region Medulla/Area postrema | Eliminated (brainstem cluster, not cerebellar) |
| 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] | 1144 CB PLI Gly-Gaba_1 | 3,066 | 🔴 LOW | Grid1 APPROXIMATE pct 0.408; Purkinje cell layer identity | Eliminated (PLI identity, Grid1 weak) |
| 5185 CB PLI Gly-Gaba_4 [CS20230722_CLUS_5185] | 1147 CB PLI Gly-Gaba_4 | 442 | 🔴 LOW | Grid1 APPROXIMATE pct 0.332; PLI identity | Eliminated (PLI identity, Grid1 weak) |
| 1150 CBX MLI Megf11 Gaba_2 [CS20230722_SUPT_1150] | — | 370 | 🔴 LOW | NT not asserted; Grid1 APPROXIMATE pct 0.236 | Eliminated (missing NT assertion; Grid1 weak) |
| 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] | — | 13,098 | 🔴 LOW | Grid1 APPROXIMATE pct 0.191; Cdh22 subtype | Eliminated (Grid1 very weak; different subtype) |
| 1147 CB PLI Gly-Gaba_4 [CS20230722_SUPT_1147] | — | 442 | 🔴 LOW | Grid1 APPROXIMATE pct 0.282; PLI identity | Eliminated (PLI identity, Grid1 weak) |
| 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] | — | 3,646 | 🔴 LOW | Grid1 APPROXIMATE pct 0.400; PLI identity | Eliminated (PLI identity, moderate-weak Grid1) |
| 1004 NTS Dbh Glut_1 [CS20230722_SUPT_1004] | — | 592 | 🔴 LOW | Pvalb APPROXIMATE pct 0.418; dominant region Medulla | Eliminated (brainstem, not cerebellar) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical stellate cell node (`stellate_cell_cerebellum`) is defined on a CLASSICAL_MULTIMODAL basis: GABAergic NT type [4]; soma in the molecular layer of cerebellar cortex [UBERON:0002974] (outer/upper third) [1][2][3]; defining markers Pvalb [1], RORa [1], and Grid1 [5]. The node notes that Pvalb and RORa are shared with basket cells and Purkinje cells, and that no stellate-specific marker has been identified — the morphological stellate/basket distinction does not translate cleanly onto transcriptomic MLI classes.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table:**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5188 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5079 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5178 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5189 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5185 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1150 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1151 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1147 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1144 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1004 | ATLAS_METADATA | PARTIAL | atlas-internal |

*Generated by evidencell `8e05bb5` at 2026-07-09T13:25:35+00:00 from [kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml](../../kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Cerebellar stellate cell (molecular layer interneuron) → 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] at MODERATE confidence. Key support: atlas metadata (Pvalb CONSISTENT at cohort_pct 0.995; Grid1 CONSISTENT at cohort_pct 0.989; location cerebellar, region_fraction_100um ≥ 0.841). Key caveats: evidence rests entirely on atlas metadata with no annotation-transfer anchor; RORa is NOT_ASSESSED; the transcriptomic MLI classification does not cleanly separate stellate from basket cells.

This classical type maps directly to the Cell Ontology term cerebellar stellate cell [[CL:0010010](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0010010)].

A secondary CBX MLI cluster, 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189], shares the same supertype (1149 CBX MLI Megf11 Gaba_1) and shows similar Pvalb and Grid1 profiles. It is assigned MODERATE confidence as a secondary candidate; its small size (154 cells) and weaker Grid1 cohort percentile (0.598 vs. 0.989 on the primary) place it below the primary candidate. Whether the two clusters represent distinct stellate subpopulations or a lobule-specific partition of the same population cannot be resolved from current atlas metadata alone.

### Proposed experiments and follow-ups

**Annotation transfer (MapMyCells)**
- **What:** Run MapMyCells on a published patch-seq dataset containing morphologically confirmed stellate cells (upper molecular layer position, dendritic arbor innervation of Purkinje cells).
- **Target:** F1 ≥ 0.70 at CLUSTER level against WMBv1 CCN20230722.
- **Expected output:** AnnotationTransferEvidence items on the primary and secondary edges.
- **Resolves:** Which CBX MLI cluster(s) receive stellate-specific patch-seq transfer; whether the two candidates are distinguishable at this resolution.

**Atlas expression for RORa**
- **What:** Retrieve or compute RORa precomputed expression statistics for the two primary candidates from WMBv1 source data.
- **Target:** Alignment assessment (CONSISTENT / DISCORDANT).
- **Expected output:** Updated property_comparisons for marker_RORa.
- **Resolves:** The NOT_ASSESSED gap on all candidate edges.

**Targeted literature search: MLI transcriptomic subtypes**
- **What:** Search for single-cell RNA-seq studies of cerebellar cortex distinguishing MLI1 (putative stellate) from MLI2 (putative basket) populations; assess whether Megf11-expressing clusters preferentially map to stellate vs. basket morphological class.
- **Expected output:** LiteratureEvidence items clarifying which WMBv1 CBX MLI subtype corresponds to stellate morphology.
- **Resolves:** The fundamental ambiguity in mapping a morphologically defined classical type to a transcriptomically defined cluster.

### Open questions

1. Does the transcriptomic boundary between 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] (n=31,095) and 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] (n=154) correspond to a biologically meaningful distinction within the stellate cell population, or is the secondary cluster a satellite/lobule-specific sub-cluster?
2. Is the CBX MLI Megf11 Gaba_1 supertype purely stellate, purely basket, or a mixed population? Single-cell transcriptomic studies that include morphological ground truth are needed to resolve this.
3. What is the RORa expression level across CBX MLI clusters in WMBv1? Its absence from precomputed atlas expression data is an informational gap.
4. Do any CBX MLI clusters in WMBv1 show differential enrichment for known stellate vs. basket cell functional markers (e.g. position-associated genes from spatial datasets)?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Brown et al. 2018 · PMID:30742002 | [30742002](https://pubmed.ncbi.nlm.nih.gov/30742002/) | Soma location, Pvalb, RORa markers |
| [2] | Jahncke & Wright 2024 · PMID:38585758 | [38585758](https://pubmed.ncbi.nlm.nih.gov/38585758/) | Soma location, circuit context |
| [3] | Miyazaki et al. 2021 · PMID:34658339 | [34658339](https://pubmed.ncbi.nlm.nih.gov/34658339/) | Soma location |
| [4] | Briatore et al. 2010 · PMID:20711348 | [20711348](https://pubmed.ncbi.nlm.nih.gov/20711348/) | NT type (GABAergic) |
| [5] | Konno et al. 2014 · PMID:24872547 | [24872547](https://pubmed.ncbi.nlm.nih.gov/24872547/) | Grid1 marker |

---

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5188 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.52
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Atlas metadata supports close match to CS20230722_CLUS_5188 (5188 CBX
    MLI Megf11 Gaba_1): marker_Pvalb CONSISTENT (cohort_pct 0.995 of 50);
    marker_Grid1 CONSISTENT (cohort_pct 0.989 of 50); 2 of 2 assessed markers
    CONSISTENT; location CONSISTENT (region_fraction_100um: 0.841, lower_bound rollup).
    MODERATE not HIGH: no annotation-transfer evidence; marker_RORa NOT_ASSESSED;
    no modality beyond atlas metadata; transcriptomic MLI classification does not
    cleanly separate stellate from basket cells.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal is driven by a lower_bound rollup row — non-painted CCF2020
        descendants are present and uncounted. region_fraction_100um value (0.841) is
        a floor; true value may be higher.
    - caveat_type: SINGLE_DATASET
      description: >
        No annotation-transfer evidence from an independently verified stellate cell
        dataset. Mapping rests entirely on atlas metadata (precomputed marker expression
        and MERFISH spatial registration). RORa (one of three defining markers) has no
        precomputed atlas expression data and is NOT_ASSESSED.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Pvalb and RORa are shared with basket cells and Purkinje cells; Grid1 is the
        most MLI-specific marker. No stellate-specific marker has been identified in
        the gathered literature, preventing transcriptomic separation of stellate from
        basket cells at this cluster level.
  proposed_experiments:
    - >
      Run annotation transfer from a published upper-molecular-layer interneuron
      dataset (cells with confirmed dendritic innervation of Purkinje cells, upper
      ML position), targeting WMBv1 CCN20230722 at ranks 0 and 1. Threshold: F1 ≥
      0.70 at CLUSTER level. Would add AnnotationTransferEvidence and resolve whether
      CS20230722_CLUS_5188 selectively captures stellate identity among CBX MLI
      clusters.
    - >
      Retrieve or compute RORa precomputed expression statistics for CS20230722_CLUS_5188
      from WMBv1 source data. Would convert marker_RORa from NOT_ASSESSED to a graded
      alignment.
    - >
      Targeted literature search for transcriptomic studies distinguishing MLI1
      (putative stellate) from MLI2 (putative basket) subtypes in mouse cerebellar
      cortex (e.g. studies using in situ spatial transcriptomics or laminar
      dissection with single-nucleus sequencing). Would add LiteratureEvidence
      clarifying whether Megf11-expressing clusters map to stellate identity.
  unresolved_questions:
    - >
      Does the CBX MLI Megf11 Gaba_1 supertype contain only stellate cells,
      only basket cells, or both? Transcriptomic studies with laminar ground
      truth are needed.
    - >
      What is the RORa expression level in CBX MLI clusters in WMBv1? Its absence
      from precomputed atlas expression is an informational gap.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5189 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.42
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Atlas metadata supports close match to CS20230722_CLUS_5189 (5189 CBX
    MLI Megf11 Gaba_1): marker_Pvalb CONSISTENT (cohort_pct 0.962 of 50);
    marker_Grid1 CONSISTENT (cohort_pct 0.598 of 50); 2 of 2 assessed markers
    CONSISTENT; location CONSISTENT (region_fraction_100um: 0.861, lower_bound rollup).
    Ranked secondary to CS20230722_CLUS_5188 due to smaller population (n_cells=154)
    and weaker Grid1 cohort percentile. Same supertype (1149 CBX MLI Megf11 Gaba_1)
    as primary. MODERATE ceiling applies for same reasons as primary edge.
  reconciliation_note: >
    Paired with edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5188 — both
    CS20230722_CLUS_5188 and CS20230722_CLUS_5189 carry supertype 1149 CBX MLI
    Megf11 Gaba_1. Whether the two clusters represent biologically distinct stellate
    subpopulations or a lobule/size-based partition is unresolved. The primary edge
    (CS20230722_CLUS_5188, n=31095) is preferred on cohort-rank and marker-percentile
    grounds.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal is driven by a lower_bound rollup row. region_fraction_100um
        value (0.861) is a floor.
    - caveat_type: SINGLE_DATASET
      description: >
        No annotation-transfer evidence. RORa NOT_ASSESSED. Small n_cells (154)
        limits confidence in biological distinctiveness from CS20230722_CLUS_5188.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Same shared-marker concern as CS20230722_CLUS_5188: Pvalb and RORa are not
        stellate-specific. Grid1 is lower percentile here (0.598 vs. 0.989 on
        primary).
  proposed_experiments:
    - >
      Same annotation transfer experiment as proposed for CS20230722_CLUS_5188 —
      inspect whether cells from an upper-ML interneuron dataset distribute across
      both clusters or preferentially to one.
    - >
      Lobule-level spatial analysis to determine whether CS20230722_CLUS_5189
      enrichment in specific cerebellar lobules explains its separation from
      CS20230722_CLUS_5188.
  unresolved_questions:
    - >
      Does CS20230722_CLUS_5189 represent a biologically distinct stellate
      subpopulation, a lobule-enriched variant, or a technical artifact of
      clustering?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5079 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] Dominant soma location is Medulla [MBA:354] / Area postrema [MBA:207]
    with only 19 cells in Cerebellum [MBA:512]; marker_Pvalb APPROXIMATE
    (cohort_pct 0.429); brainstem NTS-PARN identity. Not consistent with cerebellar
    MLI.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5178 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.12
  rationale: >
    [tier:CUT] Purkinje cell layer (PLI) cluster; Grid1 APPROXIMATE (cohort_pct 0.408).
    PLI identity is inconsistent with stellate cell molecular layer location.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5185 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] PLI cluster; Grid1 APPROXIMATE (cohort_pct 0.332, weakest Grid1
    signal among cluster-level candidates). PLI identity inconsistent with stellate
    cell.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1150 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.18
  rationale: >
    [tier:CUT] NT type not asserted at supertype level; Grid1 APPROXIMATE
    (cohort_pct 0.236). CBX MLI Megf11 Gaba_2 secondary supertype; Grid1 signal
    substantially weaker than primary candidates. Insufficient evidence to prefer
    over CS20230722_CLUS_5188.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1151 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CBX MLI Cdh22 subtype; Grid1 APPROXIMATE (cohort_pct 0.191, lowest
    Grid1 signal in the candidate set). Cdh22-dominated subtype is a different
    transcriptomic MLI class from the Megf11 supertypes containing the primary
    candidates.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1147 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] PLI supertype (1147 CB PLI Gly-Gaba_4); Grid1 APPROXIMATE
    (cohort_pct 0.282); NT not asserted. PLI identity inconsistent with stellate
    cell.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1144 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.12
  rationale: >
    [tier:CUT] PLI supertype (1144 CB PLI Gly-Gaba_1); Grid1 APPROXIMATE
    (cohort_pct 0.400); NT not asserted. PLI identity inconsistent with stellate
    cell.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1004 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Brainstem NTS Dbh Glut_1 supertype; dominant location Medulla [MBA:354]
    / Area postrema [MBA:207]; marker_Pvalb APPROXIMATE (cohort_pct 0.418);
    NT not asserted. Not consistent with cerebellar MLI identity.
```
<!-- verdict-block-end -->
