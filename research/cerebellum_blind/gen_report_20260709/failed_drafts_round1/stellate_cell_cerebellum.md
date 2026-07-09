# Cerebellar stellate cell (molecular layer interneuron) — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml`*

---

## Introduction

Cerebellar stellate cells are GABAergic interneurons residing in the upper third of the molecular layer of the cerebellar cortex [UBERON:0002974], where they innervate the distal dendritic shafts of Purkinje cells. Classically they are distinguished from basket cells by their position in the upper molecular layer and by their exclusively dendritic — not somatic — synaptic targeting [1][2][3][4]. Together with basket cells they form the two known molecular layer interneuron (MLI) populations of the cerebellar cortex; they share the GABAergic phenotype and most transcriptomic markers with basket cells, and there is no confirmed stellate-specific transcript marker in the current literature. Mapping to a single WMBv1 cluster is therefore inherently constrained by the breadth of the marker panel: Pvalb and RORa are shared with basket cells and Purkinje cells, and Grid1 (GluD1) labels MLIs broadly.

**Classical type table**

| Property | Value | References |
|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] (outer/upper third) | [1][2][3] |
| Neurotransmitter | GABAergic | [4] |
| Defining markers | Pvalb, RORa, Grid1 | [1][5] |
| Negative markers | — | |
| Neuropeptides | — | |
| Cell Ontology | cerebellar stellate cell [CL:0010010] (EXACT) | |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** Anatomical + morphological study · Brown et al. 2018 · [1]
  > Stellate cells terminate on the shaft of the Purkinje cell dendritic tree
  > — Brown et al. 2018, Anatomical organization and core cell types · [1] <!-- quote_key: 59945454_5ca8f6ac -->

- **Soma location (circuit context):** Jahncke & Wright 2024 · [2]
  > Purkinje cells receive the majority of their inhibitory inputs from two types of Molecular Layer Interneurons (MLIs): Basket Cells (BCs) and Stellate Cells (SCs) (Itō, 1984;Palay & Chan-Palay, 2012). BCs form inhibitory contacts on the soma and proximal dendrites of Purkinje cells, whereas SCs innervate the distal dendrites.
  > — Jahncke & Wright 2024, Anatomical organization and core cell types · [2] <!-- quote_key: 268857461_d94370f3 -->

- **Soma location (upper MLI):** Miyazaki et al. 2021 · [3]
  > Upper MLIs corresponding to stellate cells innervate dendritic shafts of PCs.
  > — Miyazaki et al. 2021, Results · [3] <!-- quote_key: 239017682_4f0c2aa3 -->

- **Neurotransmitter / axonal morphology:** Briatore et al. 2010 · [4]
  > . Stellate and basket cells are the only ML interneurons (MLIs) known to use GABA as a neurotransmitter (Shepherd, 1974). They are distinguished by their position in the upper and lower ML and by their axonal distribution [1,3], although intermediate forms have been described, raising the possibility that MLIs represent a continuum that varies gradually (Sultan et al., 1998)(Schilling et al., 2008). Basket cell axons, in particular, surround the cell bodies of Purkinje cells and also form a characteristic plexus around the axon initial segment, whereas stellate cells make synapses exclusively on the dendritic arbor.
  > — Briatore et al. 2010, Anatomical organization and core cell types · [4] <!-- quote_key: 1460508_88d765d5 -->

- **Defining marker — Pvalb:** Protein-level (colocalization with reporter line) · Brown et al. 2018 · [1]
  > The reporter expressing cells colocalized with the expression of parvalbumin, which is a well-known marker for Purkinje cells and molecular layer interneurons (Figs 1f,g and 2d) (Stichel et al., 1986)
  > — Brown et al. 2018, Anatomical organization and core cell types · [1] <!-- quote_key: 59945454_1c861584 -->

- **Defining marker — RORa:** Protein-level (immunostaining) · Brown et al. 2018 · [1]
  > The distribution of reporter expression in stellate versus basket cells was validated by RAR-related orphan receptor alpha (RORα) expression (Fig. 2c, per condition: N = 3, n = 9), which also marks molecular layer interneurons and Purkinje cells (Maricich et al., 1999)(Hamilton et al., 1996)(Ino, 2004)(Sillitoe et al., 2008)
  > — Brown et al. 2018, Anatomical organization and core cell types · [1] <!-- quote_key: 59945454_b21703e0 -->

- **Defining marker — Grid1 (GluD1):** Transcript (in situ / immunohistochemistry) + functional data · Konno et al. 2014 · [5]
  > In the cerebellar cortex, GluD1 mRNA was expressed at the highest level in molecular layer interneurons and its immunoreactivity was concentrated at PF synapses on interneuron somata. In GluD1-knock-out mice, the density of PF synapses on interneuron somata was significantly reduced and the size and number of interneurons were significantly diminished. Therefore, GluD1 is common to GluD2 in expression at PF synapses, but distinct from GluD2 in neuronal expression in the cerebellar cortex; that is, GluD1 in interneurons and GluD2 in PCs. Furthermore, GluD1 regulates the connectivity of PF–interneuron synapses and promotes the differentiation and/or survival of molecular layer interneurons.
  > — Konno et al. 2014, Functional roles and physiology · [5] <!-- quote_key: 8585958_c30f821f -->

</details>

**Cell Ontology mapping:** cerebellar stellate cell [[CL:0010010](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0010010)] (EXACT).

---

## Results

Atlas metadata evidence supports mapping the cerebellar stellate cell primarily to cluster 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188], which leads the 50-member GABAergic cerebellar cohort on composite score and shows both Pvalb and Grid1 at very high cohort percentiles (see property comparison table below). A second candidate at supertype level — 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] — represents a distinct MLI transcriptomic class and is worth noting given the documented absence of a stellate-specific transcriptomic marker; however, its lower Grid1 expression weakens the case relative to the Megf11 cluster.

---

### 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Cluster (5188) | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] | Cerebellum [MBA:512] (dominant; region_fraction_100um=0.841, lower_bound) | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Pvalb expression | Defining marker | Mean=11.12; cohort percentile=0.995 | CONSISTENT |
| RORa expression | Defining marker | No atlas expression data | NOT_ASSESSED |
| Grid1 expression | Defining marker | Mean=9.85; cohort percentile=0.989 | CONSISTENT |
| Sex ratio | Not documented in classical literature | Not available at cluster level | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node 5188 CBX MLI Megf11 Gaba_1 | ATLAS_METADATA | PARTIAL | region_fraction_100um=0.841; strict region_fraction=0.720; completeness=lower_bound | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Marker evidence provenance**

- **Pvalb:** Evidence for Pvalb as an MLI marker comes from protein-level data (parvalbumin immunostaining co-registered with a reporter line) in Brown et al. 2018 [1]. The study labels both stellate and basket cells, as well as Purkinje cells — Pvalb is not stellate-specific. On the atlas side, cluster 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] shows Pvalb mean expression of 11.12 at cohort percentile 0.995, confirming it as a high-Pvalb cerebellar interneuron cluster consistent with the MLI identity.

- **RORa:** Evidence comes from protein-level immunostaining (Brown et al. 2018 [1]); like Pvalb, RORa marks both MLI subtypes and Purkinje cells. RORa is absent from the WMBv1 precomputed expression data for this cluster — it cannot be assessed from atlas metadata. This is a gap in the property alignment.

  ⚠ **Atlas annotation/expression gap**: RORa is listed as a defining marker of the classical stellate cell node but has no precomputed expression data in the WMBv1 atlas for any candidate cluster. This may reflect probe panel coverage, low detection rate at atlas pseudobulk level, or a gene annotation not yet integrated into the atlas. Flag for investigation.

- **Grid1 (GluD1):** Evidence comes from transcript-level ISH and immunostaining combined with functional knockout data (Konno et al. 2014 [5]). GluD1 is expressed at highest levels in cerebellar MLIs and is functionally required for PF–interneuron synapse density and MLI differentiation. On the atlas side, cluster 5188 shows Grid1 mean expression of 9.85 at cohort percentile 0.989 — among the highest in the cerebellar GABAergic cohort. This strongly supports the MLI identity of 5188.

  *(Note: Grid1/GluD1 marks cerebellar MLIs broadly — both stellate and basket cell populations. No literature source establishes Grid1 as a stellate-specific discriminator at the transcriptomic level.)*

- **Supertype-name note:** The cluster name "5188 CBX MLI Megf11 Gaba_1" contains "Megf11" as a likely discriminating atlas marker. Megf11 is not listed as a defining marker of the classical stellate cell node in the KB, and its presence in the cluster name may reflect a transcriptomic division of cerebellar MLIs that has no direct counterpart in the classical literature. This warrants investigation (see Open questions).

**Supporting evidence**

- Atlas cluster name "CBX MLI" aligns precisely with the expected soma location — cerebellar cortex molecular layer interneuron. This is the largest cerebellar MLI cluster in the cohort (n=31,095 cells), consistent with the stellate cell being the numerically dominant upper-ML population.
- Both Pvalb (pct 0.995) and Grid1 (pct 0.989) are at very high percentiles within the 50-member GABAergic cerebellar cohort, confirming this cluster as the best-matched by marker expression among all surveyed candidates.
- The cerebellar location signal is strong: region_fraction_100um=0.841 (lower_bound rollup — actual value may be higher), with the primary painted region Cerebellum [MBA:512].

**Concerns**

- No annotation transfer evidence is available. The confidence ceiling here is MODERATE because the mapping rests on atlas metadata alone — no experimental anchor (patch-seq AT, driver-line AT, bulk correlation) directly links stellate cell physiology or morphology to this specific cluster's transcriptome.
- RORa cannot be assessed from atlas metadata (see above).
- The Megf11 transcriptomic label in the cluster name is not represented in the classical node's marker panel. If Megf11 defines a subset of MLIs that specifically corresponds to basket cells (or to a transcriptomic class distinct from classical stellate cells), the mapping could be misplaced. *(Note: this is an interpretation; Megf11's biological role in cerebellar interneuron taxonomy is not confirmed in the facts file.)*
- Region fraction is a lower_bound estimate (non-painted CCF2020 descendants uncounted); actual cerebellar fraction is ≥0.841.
- No stellate-specific marker is available to distinguish this cluster from basket cell candidates at the transcript level.

**What would upgrade confidence**

- Annotation transfer using a source dataset with cell-type identity confirmed by morphology (upper-ML position + dendritic targeting) would directly test whether stellate cell transcriptomes land on cluster 5188 or distribute across the CBX MLI supertypes. Target: F1 ≥ 0.70 at cluster level.
- Literature retrieval for Megf11 expression in cerebellar interneurons would clarify whether the Megf11 label marks a stellate-specific or a broader MLI population.
- Targeted search for scRNA-seq data distinguishing cerebellar stellate from basket cells (e.g. Kozareva et al. 2021 cerebellar atlas, Cadwell et al. — *(note: cited from neuroanatomical training knowledge, not from the facts file)*) would establish whether the WMBv1 MLI transcriptomic classes correspond to the classical stellate/basket distinction.

---

### 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] · 🔴 LOW

**Table 1 — Property comparison**

| Property | Classical | Supertype (1151) | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] | Cerebellum [MBA:512] (dominant; region_fraction_100um=0.851, lower_bound) | CONSISTENT |
| NT type | GABAergic | Not asserted | NOT_ASSESSED |
| Pvalb expression | Defining marker | Mean=11.33; cohort percentile=0.991; child-coverage=1.000 | CONSISTENT |
| RORa expression | Defining marker | No atlas expression data | NOT_ASSESSED |
| Grid1 expression | Defining marker | Mean=1.39; cohort percentile=0.191; child-coverage=1.000 | APPROXIMATE |
| Sex ratio | Not documented | Not available | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node 1151 CBX MLI Cdh22 Gaba_1 | ATLAS_METADATA | PARTIAL | region_fraction_100um=0.851; strict region_fraction=0.723; completeness=lower_bound | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Supporting evidence**

- Cerebellar location is strong (region_fraction_100um=0.851, lower_bound), comparable to cluster 5188.
- Pvalb expression is very high (mean=11.33, cohort pct=0.991, child-coverage=1.000), consistent with cerebellar MLI identity.
- This is a large supertype (n=13,098 cells), consistent with the expectation that an MLI-class supertype would encompass substantial numbers of cells.

**Concerns**

- Grid1 expression is low (mean=1.39, cohort pct=0.191) — APPROXIMATE. The classical node lists Grid1 as a defining marker based on MLI-specific expression (Konno et al. 2014 [5]); its low value on this supertype is a substantive concern. The Cdh22 supertype may represent an MLI transcriptomic class in which Grid1 is less defining, or may overlap more with a non-stellate MLI population.
- NT type is not asserted in the atlas for this supertype — cannot confirm GABAergic identity from the KB data.
- No annotation transfer evidence.
- The Cdh22 label (Cadherin 22) in the supertype name is not a classical stellate cell marker; its discriminating role in cerebellar MLI taxonomy is unclear.
- Choosing this supertype as the mapping target would imply that the classical stellate cell is part of a transcriptomic class that differs from the best Pvalb+Grid1 cluster (5188 / Megf11 class), which is biologically possible but presently unsupported.

**What would upgrade confidence**

- Annotation transfer with morphologically confirmed stellate cells would directly test whether they land on the Cdh22 or Megf11 transcriptomic class.
- Literature retrieval for the transcriptomic identity of cerebellar MLI subtypes would clarify the Megf11/Cdh22 distinction and its relationship to the classical stellate/basket cell distinction.

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] | 1149 CBX MLI Megf11 Gaba_1 | 31,095 | 🟡 MODERATE | Pvalb+Grid1 CONSISTENT; CBX MLI; top cohort rank | Primary |
| 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] | — | 13,098 | 🔴 LOW | Pvalb CONSISTENT; Grid1 low (pct 0.191) | Secondary |
| 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] | 1144 CB PLI Gly-Gaba_1 | 3,066 | — | Eliminated (Grid1 borderline; PLI not ML) |
| 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] | 1149 CBX MLI Megf11 Gaba_1 | 154 | — | Eliminated (minor cluster under 5188 supertype; duplicate of 5188 at cluster level) |
| 5185 CB PLI Gly-Gaba_4 [CS20230722_CLUS_5185] | 1147 CB PLI Gly-Gaba_4 | 442 | — | Eliminated (Grid1 low-cohort; PLI location) |
| 1150 CBX MLI Megf11 Gaba_2 [CS20230722_SUPT_1150] | — | 370 | — | Eliminated (Grid1 low cohort pct 0.236; NT not asserted) |
| 1147 CB PLI Gly-Gaba_4 [CS20230722_SUPT_1147] | — | 442 | — | Eliminated (Grid1 borderline; PLI not molecular layer) |
| 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] | — | 3,646 | — | Eliminated (Grid1 borderline; PLI location) |
| 5079 NTS-PARN Neurod2 Gly-Gaba_1 [CS20230722_CLUS_5079] | 1130 NTS-PARN Neurod2 Gly-Gaba_1 | 212 | — | Eliminated (dominant anatomy brainstem; Pvalb low) |
| 1004 NTS Dbh Glut_1 [CS20230722_SUPT_1004] | — | 592 | — | Eliminated (brainstem nucleus tractus solitarius; wrong region) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The cerebellar stellate cell (molecular layer interneuron) is defined on a CLASSICAL_MULTIMODAL basis: GABAergic neurotransmitter type [4], soma in the molecular layer of the cerebellar cortex (upper/outer third) [1][2][3], defining markers Pvalb [1], RORa [1], and Grid1 [5]. No stellate-specific transcriptomic marker is established; Pvalb and RORa are shared with basket cells and Purkinje cells. The classical node notes explicitly record that the type "does not map cleanly onto transcriptomic MLI1/MLI2 classes."

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

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

**Primary mapping:** Cerebellar stellate cell (molecular layer interneuron) → 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] at MODERATE confidence. Key support: Pvalb and Grid1 both CONSISTENT at very high cohort percentile; cerebellar MLI annotation and location match. Key caveats: atlas metadata only (no annotation transfer anchor); no stellate-specific discriminating marker available; RORa not assessable from atlas metadata; Megf11 discriminating label not represented in classical panel.

This classical type maps directly to the Cell Ontology term cerebellar stellate cell [[CL:0010010](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0010010)].

### Proposed experiments and follow-ups

**1. Annotation transfer from morphologically confirmed stellate cell datasets**
- **What:** MapMyCells annotation transfer to WMBv1 (CCN20230722) using a source dataset that identifies stellate cells by morphology (upper-ML soma position + dendritic-only targeting confirmed by biocytin fill or post-hoc reconstruction).
- **Target:** F1 ≥ 0.70 at cluster level.
- **Expected output:** AnnotationTransferEvidence on edges for CLUS_5188 and SUPT_1151, clarifying which MLI transcriptomic class the classical stellate cell lands on.
- **Resolves:** The central question of whether stellate cells correspond to the Megf11 or Cdh22 WMBv1 transcriptomic class, and whether CLUS_5188 is the correct primary mapping or whether the stellate cell distributes across multiple clusters.

**2. Literature retrieval for Megf11 and Cdh22 in cerebellar interneurons**
- **What:** Targeted cite-traverse / literature search for "Megf11 cerebellum interneuron" and "Cdh22 cerebellum stellate basket."
- **Target:** Establish which transcriptomic class (Megf11 vs. Cdh22) corresponds to the classical stellate vs. basket distinction.
- **Expected output:** LiteratureEvidence entries anchoring the Megf11/Cdh22 atlas label to a known morphological or physiological property.
- **Resolves:** Whether CLUS_5188 (Megf11) or SUPT_1151 (Cdh22) is the better primary mapping.

**3. RORa atlas coverage**
- **What:** Check whether RORa (Rora) is present in the WMBv1 precomputed expression data for the CBX MLI clusters (possible data ingestion or gene-alias issue).
- **Target:** Confirm CONSISTENT or DISCORDANT alignment for this defining marker.
- **Expected output:** Updated property comparison entry for marker_RORa.
- **Resolves:** The NOT_ASSESSED gap on RORa for all 10 candidate edges.

### Open questions

1. Does the Megf11 transcriptomic label (as in "CBX MLI Megf11 Gaba_1") correspond to a stellate-cell-enriched or basket-cell-enriched population in the WMBv1 taxonomy? No literature source in the facts file establishes this.

2. Does WMBv1 distinguish stellate cells from basket cells at the cluster or supertype level? The classical node notes record that the type "does not map cleanly onto transcriptomic MLI1/MLI2 classes" — this question would be resolved by annotation transfer with morphologically confirmed source cells.

3. Is RORa absent from the WMBv1 atlas precomputed expression due to probe panel coverage, gene aliasing (RORA vs. RORa), or genuinely low expression in cerebellar MLIs? This should be confirmed before treating the NOT_ASSESSED alignment as uninformative.

4. Should the cerebellar stellate cell KB node be linked to a "basket_cell_cerebellum" sibling node via a `skos:closeMatch` or `evidencell:CrossCuttingMatch` edge reflecting the documented morphological continuum (Briatore et al. 2010 [4])? This is a KB topology question for curator review.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Brown et al. 2018 | [30742002](https://pubmed.ncbi.nlm.nih.gov/30742002/) | Soma location, Pvalb marker, RORa marker |
| [2] | Jahncke & Wright 2024 | [38585758](https://pubmed.ncbi.nlm.nih.gov/38585758/) | Soma location, circuit context |
| [3] | Miyazaki et al. 2021 | [34658339](https://pubmed.ncbi.nlm.nih.gov/34658339/) | Soma location (upper MLI) |
| [4] | Briatore et al. 2010 | [20711348](https://pubmed.ncbi.nlm.nih.gov/20711348/) | Neurotransmitter type, morphology |
| [5] | Konno et al. 2014 | [24872547](https://pubmed.ncbi.nlm.nih.gov/24872547/) | Grid1 marker |

---

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5188 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.45
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Pvalb (mean=11.12, cohort_pct 0.995) and Grid1 (mean=9.85,
    cohort_pct 0.989) both CONSISTENT on CS20230722_CLUS_5188; 2 of 2 assayed
    markers CONSISTENT (RORa NOT_ASSESSED — absent from atlas precomputed
    expression). Cerebellar location confirmed (region_fraction_100um: 0.841,
    lower_bound). Atlas cluster label "CBX MLI" matches expected cerebellar
    cortex molecular layer interneuron soma position. No annotation transfer
    evidence available; confidence ceiling is MODERATE on atlas metadata alone.
    Megf11 discriminating label in cluster name not present in classical marker
    panel — warrants lit follow-up.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal is driven by a lower_bound rollup — non-painted CCF2020
        descendants uncounted; region_fraction_100um=0.841 is a floor (true
        value may be higher).
    - caveat_type: MISSING_EVIDENCE_TYPE
      description: >
        No annotation transfer evidence. Confidence cannot exceed MODERATE without
        an experimental anchor (patch-seq AT or driver-line AT) confirming that
        morphologically identified stellate cells map to CS20230722_CLUS_5188.
    - caveat_type: MARKER_HETEROGENEITY
      description: >
        No stellate-specific transcriptomic marker is established. Pvalb and RORa
        are shared with basket cells and Purkinje cells; Grid1 labels cerebellar
        MLIs broadly. The Megf11 discriminating label in the cluster name may
        reflect a transcriptomic class that partially overlaps with the classical
        stellate vs. basket distinction.
  proposed_experiments:
    - >
      Annotation transfer using morphologically confirmed stellate cells (upper-ML
      soma, dendritic targeting confirmed by biocytin fill or reconstruction) as
      source; MapMyCells to WMBv1 CCN20230722; target F1 ≥ 0.70 at cluster level.
      Would add AnnotationTransferEvidence and test whether stellate cells land on
      CS20230722_CLUS_5188 or distribute across MLI supertypes.
    - >
      Literature retrieval for Megf11 expression in cerebellar interneurons to
      establish whether the Megf11 cluster label marks a stellate- or basket-cell-
      enriched population. Would add LiteratureEvidence anchoring the atlas label.
    - >
      Confirm RORa (Rora) atlas coverage for CBX MLI clusters — check gene aliasing
      and probe panel. Would resolve the NOT_ASSESSED gap on marker_RORa.
  unresolved_questions:
    - >
      Does the Megf11 label in CS20230722_CLUS_5188 correspond to stellate-enriched
      or basket-enriched cerebellar MLIs?
    - >
      Does WMBv1 distinguish stellate cells from basket cells at cluster or supertype
      level, or do classical morphological subtypes distribute across multiple
      transcriptomic clusters?
    - >
      Is RORa absent from WMBv1 precomputed expression due to probe panel coverage,
      gene aliasing, or genuinely low expression in cerebellar MLIs?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5079 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Dominant anatomy is brainstem (Medulla [MBA:354], Area postrema
    [MBA:207]); Cerebellum [MBA:512] is the third-ranked region. Pvalb mean=0.21
    (APPROXIMATE, cohort_pct 0.429) — well below the expected high-Pvalb MLI
    signature. NTS-PARN identity is inconsistent with cerebellar stellate cell
    biology.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5178 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.12
  rationale: >
    [tier:CUT] CB PLI (Purkinje layer interneuron) location label is inconsistent
    with molecular layer soma position; dominant anatomy includes cerebellum related
    fiber tracts [MBA:960] and arbor vitae [MBA:728]. Pvalb CONSISTENT (mean=10.41,
    cohort_pct 0.984) but Grid1 APPROXIMATE (mean=6.98, cohort_pct 0.408) — lower
    than the top cerebellar MLI candidates. No atlas metadata support for molecular
    layer placement.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5189 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] Same supertype as CS20230722_CLUS_5188 (1149 CBX MLI Megf11
    Gaba_1) but much smaller cluster (n=154 vs. 31,095). Pvalb CONSISTENT
    (mean=9.90, cohort_pct 0.962) and Grid1 CONSISTENT (mean=8.06, cohort_pct
    0.598) — both lower than CLUS_5188. Evidence portfolio is weaker on all
    signals; CLUS_5188 is the preferred representative of this supertype.
    Duplicate representation of the same supertype in the candidate set.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_CLUS_5185 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CB PLI location label inconsistent with molecular layer; fiber tract
    and arbor vitae anatomy signal. Pvalb CONSISTENT (mean=10.40, cohort_pct 0.978)
    but Grid1 APPROXIMATE (mean=5.49, cohort_pct 0.332) — weak by cohort standards.
    region_fraction_100um=0.525 is in the boundary band but PLI identity and lower
    Grid1 argue against stellate cell placement.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1150 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.18
  rationale: >
    [tier:CUT] CBX MLI Megf11 Gaba_2 supertype; cerebellar location confirmed
    (region_fraction_100um=0.865). Pvalb CONSISTENT (mean=10.71, cohort_pct
    0.982, child-coverage 1.000). Grid1 APPROXIMATE (mean=4.18, cohort_pct
    0.236, child-coverage 1.000) — substantially weaker than CLUS_5188.
    NT not asserted. As a smaller supertype (n=370) with lower Grid1 than
    SUPT_1151 (n=13,098) and markedly lower Grid1 than CLUS_5188, this is
    the weakest of the CBX MLI supertype candidates.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1151 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.28
  relationship: evidencell:UncertainRelationship
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CBX MLI Cdh22 Gaba_1 supertype; cerebellar location confirmed
    (region_fraction_100um=0.851). Pvalb CONSISTENT (mean=11.33, cohort_pct
    0.991, child-coverage 1.000). Grid1 APPROXIMATE (mean=1.39, cohort_pct
    0.191, child-coverage 1.000) — weak Grid1 is the primary concern. Large
    cluster (n=13,098). NT not asserted from atlas metadata. Represents a
    distinct MLI transcriptomic class (Cdh22 vs. Megf11); its relationship to
    the classical stellate/basket distinction is unknown. Uncertainty about
    which MLI transcriptomic class the stellate cell falls into warrants
    keeping this as a named alternative pending annotation transfer evidence.
  reconciliation_note: >
    Uncertain alternative to CS20230722_CLUS_5188: the WMBv1 MLI classes
    (Megf11 vs. Cdh22) may or may not correspond to the classical stellate
    vs. basket distinction. Annotation transfer with morphologically confirmed
    stellate cells would resolve which class to prefer.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal lower_bound rollup; region_fraction_100um=0.851 is a floor.
    - caveat_type: MISSING_EVIDENCE_TYPE
      description: >
        No annotation transfer evidence. Grid1 low at supertype level
        (cohort_pct 0.191) despite child-coverage 1.0 — likely a within-supertype
        averaging effect; child-cluster breakdown would clarify.
    - caveat_type: MARKER_HETEROGENEITY
      description: >
        Grid1 APPROXIMATE at supertype level; NT not asserted. Cdh22 label not
        represented in classical stellate cell marker panel.
  proposed_experiments:
    - >
      Annotation transfer using morphologically confirmed stellate cells to
      WMBv1 CCN20230722; compare F1 landing on SUPT_1151 vs. CS20230722_CLUS_5188.
    - >
      Literature retrieval for Cdh22 expression in cerebellar interneurons;
      establish whether Cdh22 marks stellate-enriched or basket-enriched population.
  unresolved_questions:
    - >
      Does the WMBv1 Megf11/Cdh22 transcriptomic division of cerebellar MLIs
      correspond to the classical stellate/basket morphological distinction?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1147 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] CB PLI Gly-Gaba_4 supertype; location includes fiber tracts and
    arbor vitae — inconsistent with molecular layer soma. Pvalb CONSISTENT
    (mean=10.40, cohort_pct 0.964, child-coverage 1.000) but Grid1 APPROXIMATE
    (mean=5.49, cohort_pct 0.282, child-coverage 1.000). PLI location and
    lower Grid1 argue against stellate cell placement; NT not asserted.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1144 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CB PLI Gly-Gaba_1 supertype; location includes fiber tracts and
    arbor vitae. Pvalb CONSISTENT (mean=10.03, cohort_pct 0.955, child-coverage
    1.000) and Grid1 APPROXIMATE (mean=7.44, cohort_pct 0.400, child-coverage
    1.000) — Grid1 higher than SUPT_1147 but still APPROXIMATE, and PLI location
    inconsistent with molecular layer soma position. NT not asserted.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_stellate_cell_cerebellum_to_CS20230722_SUPT_1004 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.03
  rationale: >
    [tier:CUT] NTS Dbh Glut_1 — nucleus tractus solitarius with Dbh
    (dopamine-beta-hydroxylase) label; dominant anatomy is Medulla [MBA:354]
    and Area postrema [MBA:207]. Pvalb APPROXIMATE (mean=0.30, cohort_pct
    0.418, child-coverage 0.875). Wrong region and wrong NT profile for
    cerebellar stellate cell.
```
<!-- verdict-block-end -->
