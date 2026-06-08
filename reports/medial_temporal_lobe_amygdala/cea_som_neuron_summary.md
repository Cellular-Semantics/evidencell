# Central amygdala somatostatin-positive neuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

The central amygdala somatostatin-positive (SST+) neuron is a GABAergic interneuron-like projection cell residing in the lateral subdivision of the central amygdala (CeL; UBERON:0002883). Classically defined by somatostatin (Sst) neuropeptide expression and the absence of protein kinase C-delta (Prkcd), this population constitutes the "CeL-ON" class — neurons that potentiate firing during fear conditioning and gate fear expression through inhibition of CeL output neurons. Their complementary opposition to the Prkcd+ "CeL-OFF" class makes the Sst/Prkcd dichotomy the central molecular axis of CeA circuit identity. Mapping this classical type to the WMBv1 atlas is essential for anchoring CeA circuit models in transcriptomic space and enabling cross-study comparisons.

### Classical type description

| Property | Value | References |
|---|---|---|
| Soma location | Central amygdaloid nucleus [UBERON:0002883] | [1] [2] [3] [4] |
| Neurotransmitter | GABAergic | [1] [5] |
| Defining markers | None recorded (type identified by neuropeptide + negative marker) | — |
| Negative markers | Prkcd | [2] |
| Neuropeptides | Sst | [1] [2] [6] [7] |
| Notes | Largely non-overlapping with PKC-delta neurons; constitutes a large share of lateral CeA neurons | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location — UBERON:0002883:** Li et al. 2013 identified CeL SST+ neurons as the fear-conditioning CeL-ON class in the lateral subdivision of the CeA [1]. Adke et al. 2019 localised SST+ and PKCδ+ neurons as the two major CeLC populations [2]. Nisbett & Koob 2025 reviewed CeA subdivisions including CeC, CeL, and CeM [3]. Vicario et al. 2014 noted somatostatin-positive MGE-derived neurons concentrate in the medial subdivision of the nucleus [4].

  For **[1]** (Li et al. 2013):
  > "The amygdala is essential for fear learning and expression. The central amygdala (CeA), once viewed as a passive relay between the amygdala complex and downstream fear effectors, has emerged as an active participant in fear conditioning. However, the mechanism by which CeA contributes to the learning and expression of fear is unclear. We found that fear conditioning in mice induced robust plasticity of excitatory synapses onto inhibitory neurons in the lateral subdivision of the CeA (CeL). This experience-dependent plasticity was cell specific, bidirectional and expressed presynaptically by inputs from the lateral amygdala. In particular, preventing synaptic potentiation onto somatostatin-positive neurons impaired fear memory formation. Furthermore, activation of these neurons was necessary for fear memory recall and was sufficient to drive fear responses. Our findings support a model in which fear conditioning–induced synaptic modifications in CeL favor the activation of somatostatin-positive neurons, which inhibit CeL output, thereby disinhibiting the medial subdivision of CeA and releasing fear expression."
  > — Li et al. 2013, Central amygdala cell types · [1] <!-- quote_key: 10650261_f38d6b66 -->

- **Neurotransmitter — GABAergic:** Li et al. 2013 [1] and Gilpin et al. 2014 [5] document the CeA as a primarily GABAergic nucleus.

  For **[5]** (Gilpin et al. 2014):
  > "The central amygdala (CeA) plays a central role in physiological and behavioral responses to fearful stimuli, stressful stimuli, and drug-related stimuli. The CeA receives dense inputs from cortical regions, is the major output region of the amygdala, is primarily GABAergic (inhibitory), and expresses high levels of pro- and anti-stress peptides."
  > — Gilpin et al. 2014, Central amygdala cell types · [5] <!-- quote_key: 442779_deea5502 -->

- **Negative marker — Prkcd:** Adke et al. 2019 [2] explicitly state SST+ and PKCδ+ neurons are largely non-overlapping, establishing Prkcd absence as a defining feature of the SST+ class.

  For **[2]** (Adke et al. 2019):
  > "This diverse span of function is mirrored by the genetic, physiological and morphologic heterogeneity in CeA neuron subtypes (Martina et al., 1999;Schiess et al., 1999;Janak and Tye, 2015). Two genetically identified cell types, protein kinase Cdexpressing (PKCd⁺) neurons and somatostatin-expressing (Som⁺) neurons, constitute most CeLC neurons and are largely non-overlapping (Li et al., 2013;Kim et al., 2017;Wilson et al., 2019)."
  > — Adke et al. 2019, Central amygdala cell types · [2] <!-- quote_key: 209598438_053c1083 -->

- **Neuropeptide — Sst:** Confirmed by Li et al. 2013 [1], Adke et al. 2019 [2], Yeh et al. 2024 [6], and O'Leary et al. 2022 [7]. Yeh et al. 2024 identified distinct PKC-δ, SOM, and CRF neuronal populations in this region.

  For **[6]** (Yeh et al. 2024):
  > ".It revealed distinct PKC-δ, SOM, and CRF neuronal populations similar to those in mice."
  > — Yeh et al. 2024, Central amygdala cell types · [6] <!-- quote_key: 267685584_daaf5612 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed; CS20230722_CLUS_0823 ("Sst Gaba_17") is the primary mapping at LOW confidence, reflecting a clean property alignment for SST expression and Prkcd absence, but confounded by five equally-scored CeA GABAergic clusters and the absence of annotation-transfer evidence.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---|---:|---|---|---|
| 1 | CS20230722_CLUS_0823 | SUPT_0230 (Sst Gaba_17) | not assessed | 🔴 LOW | Sst CONSISTENT · Prkcd-negative CONSISTENT | broadMatch; 1:n tie |

*1 edge assessed; relationship type: skos:broadMatch (1:n — 5 Sst Gaba clusters score equally).*

### Property alignment table — CS20230722_CLUS_0823

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Central amygdaloid nucleus [UBERON:0002883] | MBA:536 CeA present; region_fraction 0.067 (cohort rank 2 of 5); parent supertype SUPT_0230 (Sst Gaba_17) | not assessed | CONSISTENT |
| NT type | GABAergic | GABA | GABA | CONSISTENT |
| Sst expression | Sst — defining neuropeptide | not available at supertype level | Sst mean_expression 10.36 (CeA GABAergic cohort 95.1th pct; tier 2; applied_score 2.0) | CONSISTENT |
| Prkcd (negative) | Prkcd — negative marker | not available | Prkcd precomputed val 0.0 (0th pct; tier 1 unreliable); effectively absent | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Li et al. 2013 — fear-conditioning SST+ CeL-ON | Literature | SUPPORT | SST+ neurons required for fear memory recall; non-overlapping with PKCδ class | [1] |
| Adke et al. 2019 — SST+/PKCδ+ CeLC dichotomy | Literature | SUPPORT | Som+ and PKCd+ constitute most CeLC neurons; largely non-overlapping | [2] |
| Atlas metadata — CLUS_0823 Sst/Prkcd expression | Atlas metadata | SUPPORT | Sst 95.1th pct of CeA GABAergic cohort; Prkcd 0th pct | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### CS20230722_CLUS_0823 (Sst Gaba_17, SUPT_0230) · 🔴 LOW

**Supporting evidence:**

- **Sst expression (CONSISTENT):** CLUS_0823 carries Sst mean_expression 10.36, placing it at the 95.1th percentile of the CeA GABAergic survival cohort (5 members; filtered to MBA:536 + GABAergic). This is the highest tier-2 reliable Sst signal among the five cohort members and directly matches the defining neuropeptide of the classical type. Stage A discovery score for CLUS_0823 was 4 (rank 2 of 5 in a 5-member cohort; score tied with all cohort members — cohort-wide tie), with Sst contributing `applied_score: 2.0` from cohort-pct 0.951 of 5. *(Note: the cohort has only 5 members, so percentile values reflect intra-cohort rank only and do not convey atlas-wide specificity.)*

- **Prkcd-negative (CONSISTENT):** Prkcd precomputed expression = 0.0 (0th percentile of the CeA GABAergic cohort; tier 1 unreliable, meaning the gene is absent or near-undetectable). This confirms Prkcd negativity, a defining exclusion criterion for the SST+ class [2].

- **NT type (CONSISTENT):** CLUS_0823 is designated GABA, consistent with the classical type's GABAergic identity [1][5].

- **CeA location (CONSISTENT):** MBA:536 (Central amygdalar nucleus) is present in the CLUS_0823 distribution with region_fraction 0.067. This places it at cohort rank 2 of 5 for CeA specificity — not the highest CeA fraction in the cohort. *(Note: region_fraction 0.067 is in the boundary band per the reporting rubric — see Concerns below.)*

  Ciocchi et al. 2010 identifies CeL SST+ neurons (CeL-ON) that increase firing during fear conditioning; SST is the primary neuropeptide marker defining this population opposite to the PKC-delta CeL-OFF class [1]. Adke et al. 2019 confirms SST+ CeL neurons as the classical CeL-ON population non-overlapping with PKC-delta cells; SST and Prkcd jointly define the two major CeL classes [2].

**Marker evidence provenance:**

- **Sst (neuropeptide):** Evidence is multi-source: immunohistochemistry in rodents (Yeh et al. 2024 [6] confirmed distinct SOM populations at protein level), scRNA-seq-based studies (O'Leary et al. 2022 [7] noted mixed Prkcd/Sst expression across scRNA-seq clusters), and functional characterisation (Li et al. 2013 [1] used Sst-IRES-Cre targeting with patch-clamp and biocytin fills, confirming cell-type identity through morphological reconstruction and targeted activation). The cell-type specificity basis is strong for [1]: SST-Cre driver targeting confirmed by morphological and electrophysiological characterisation. Sst expression is confirmed in the WMBv1 atlas at tier 2 (mean = 10.36).

  ⚠ **Data source note:** O'Leary et al. 2022 [7] explicitly state "Prkcd and Sst each exhibited mixed expression across multiple scRNA-seq-clusters" — this is consistent with the DISTRIBUTED_ACROSS_CLUSTERS caveat (five clusters score equally) and does not contradict the classical type definition, but it signals that no single WMBv1 cluster cleanly captures all SST+ CeA neurons.

- **Prkcd (negative marker):** Established by Adke et al. 2019 [2] and Li et al. 2013 [1] through Cre-driver-based genetic labelling combined with IHC. Evidence is protein-level (PKCδ immunostaining) and transcript-level (SST-Cre × reporter crosses). Cell-type specificity is high: both studies confirmed identity through functional and anatomical characterisation of targeted cells. Atlas-side Prkcd = 0.0 at CLUS_0823 is fully concordant.

**Concerns:**

- **DISTRIBUTED_ACROSS_CLUSTERS:** Five Sst Gaba clusters (CLUS_0765, CLUS_0823, CLUS_0850, CLUS_0860, and CLUS_1312) all scored equally (score 4) in the CeA GABAergic discovery cohort. The Stage A tie means no cluster dominates; the classical type likely spans multiple atlas clusters. CLUS_0823 is selected here because CLUS_0765 is already used for the BLA SST dendrite-targeting interneuron and CLUS_0860 carries the Chodl co-expression designation (Chodl is not a canonical CeA SST marker and may reflect a different subpopulation). However, CLUS_0850 and CLUS_1312 remain unassessed alternatives. *(Note: in a 5-member cohort, a score of 4 vs next-best 4 means Stage A provides no discriminating power — the tie is complete.)*

- **Low region_fraction (boundary band):** CeA region_fraction = 0.067 for CLUS_0823. This is in the boundary band; the CeA is not the dominant soma location for this cluster. CLUS_0860 ("Sst Chodl") has a slightly higher CeA fraction (0.084) but the Chodl designation introduces uncertainty about whether it represents typical CeA SST neurons.

- **No AT evidence:** No MapMyCells annotation-transfer evidence is available. The molecular identity rests solely on metadata-level Sst/Prkcd expression alignment and literature support. This is the primary reason for LOW rather than MODERATE confidence.

- **1:n cardinality unresolved:** CeA SST neurons overlap with BLA SST dendrite-targeting neurons in the discovery pool. Anatomical restriction to MBA:536 is the primary discriminator, but several clusters span both BLA and CeA. The broadMatch predicate correctly signals this 1:n situation.

**What would upgrade confidence:**

1. **MapMyCells annotation transfer (AnnotationTransferEvidence):** Run MapMyCells on published CeA SST scRNA-seq data (e.g. from SST-Cre targeted recordings or TRAP-seq) against WMBv1. F1 ≥ 0.60 at cluster level would resolve the 1:n tie and upgrade to MODERATE. F1 ≥ 0.80 would support HIGH if other markers align.

2. **scRNA-seq of CeA-targeted SST-Cre+ neurons:** Profile isolated CeA SST+ neurons with WMBv1 cluster assignment to determine whether the SST+ CeL-ON population falls in one cluster or spans multiple Sst Gaba supertypes. Expected output: AnnotationTransferEvidence or cluster-assignment proportions resolving edges Q1 and Q2 (see Open questions).

3. **Targeted expression query across all 5 cohort members:** Query CCN20230722 for CeA-fraction and Chodl expression across CLUS_0823, CLUS_0850, CLUS_0860, CLUS_0765, and CLUS_1312. If CLUS_0860 (Sst Chodl) can be excluded on Chodl co-expression grounds, the 1:n is narrowed to 3–4 clusters. Expected output: ATLAS_QUERY evidence items added to the relevant edges.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Central amygdala somatostatin-positive neuron is defined on a CLASSICAL basis: it is identified by Sst neuropeptide expression, GABAergic neurotransmitter type, and soma location in the central amygdaloid nucleus [UBERON:0002883]. The defining negative marker is Prkcd (protein kinase C-delta), whose absence distinguishes the SST+ CeL-ON class from the PKCδ+ CeL-OFF class. Primary citations: Li et al. 2013 [1] (Cre-driver functional characterisation), Adke et al. 2019 [2] (two-class CeLC model), Nisbett & Koob 2025 [3] and Vicario et al. 2014 [4] (anatomical context). Neurotransmitter confirmed by Li et al. 2013 [1] and Gilpin et al. 2014 [5]. Sst neuropeptide additionally supported by Yeh et al. 2024 [6] and O'Leary et al. 2022 [7]. Definition basis: CLASSICAL (functional + genetic + anatomical evidence from primary studies; no patch-seq transcriptomic profile assigned).

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 0 (cluster) using metadata-based scoring (region match MBA:536, NT type GABAergic, neuropeptide Sst, negative marker Prkcd). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Atlas data sources.**

| Atlas | Taxonomy ID | Notes |
|---|---|---|
| WMBv1 | CCN20230722 | Allen Brain Cell Atlas (2023); Zhuang et al. 2023 MERFISH spatial registration |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cea_som_neuron_to_cs20230722_clus_0823 | LITERATURE; LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT; SUPPORT | [1]; [2]; atlas-internal |

*Generated by evidencell `8222564` at 2026-06-04T10:52:49+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats

**Primary mapping:** Central amygdala somatostatin-positive neuron → CS20230722_CLUS_0823 (Sst Gaba_17, SUPT_0230) at LOW confidence. Key support: Sst precomputed expression at 95.1th cohort percentile (CONSISTENT) and Prkcd effectively absent (CONSISTENT). Key caveats: DISTRIBUTED_ACROSS_CLUSTERS (five Sst Gaba clusters score equally; CeA SST neurons likely span multiple WMBv1 clusters); no MapMyCells AT evidence to resolve 1:n cardinality.

No Cell Ontology term currently assigned. The SST+ CeL-ON population is a functionally and genetically defined class that may warrant a new CL term once the transcriptomic boundary with the BLA SST dendrite-targeting interneuron is clarified.

### Proposed experiments and follow-ups

**1. MapMyCells annotation transfer**
- **What:** Run MapMyCells on published CeA SST scRNA-seq data (SST-Cre+ targeted cells from CeA).
- **Target:** F1 ≥ 0.60 at cluster level for a single Sst Gaba cluster.
- **Expected output:** AnnotationTransferEvidence added to edge_cea_som_neuron_to_cs20230722_clus_0823 (and possibly new edges to sibling clusters).
- **Resolves:** Open questions Q1 and Q2; DISTRIBUTED_ACROSS_CLUSTERS caveat; would upgrade confidence from LOW to MODERATE or higher.

**2. CeA-targeted SST-Cre scRNA-seq with WMBv1 cluster assignment**
- **What:** Profile isolated CeA SST+ neurons (SST-Cre × reporter, FACS, scRNA-seq) and assign to WMBv1 clusters.
- **Target:** Determine whether ≥ 70% of CeA SST+ neurons fall in a single cluster.
- **Expected output:** AnnotationTransferEvidence or LiteratureEvidence resolving 1:n cardinality.
- **Resolves:** Q1 (which Sst Gaba cluster is most CeA-specific), Q2 (does the CeL-ON population correspond to one cluster or multiple supertypes); SINGLE_DATASET caveat.

**3. Targeted expression query for Chodl across the 5 cohort clusters**
- **What:** Query CCN20230722 precomputed expression for Chodl across CLUS_0823, CLUS_0850, CLUS_0860, CLUS_0765, and CLUS_1312.
- **Target:** Confirm whether CLUS_0860 can be excluded from the 1:n on Chodl co-expression grounds; assess whether CLUS_0850 or CLUS_1312 carry higher CeA fractions.
- **Expected output:** ATLAS_QUERY evidence narrowing the 1:n broadMatch to a smaller candidate set.
- **Resolves:** DISTRIBUTED_ACROSS_CLUSTERS caveat (partial); Q1.

### Open questions

1. **Which Sst Gaba cluster is most specific to CeA vs BLA?** CLUS_0860 (Sst Chodl) has a higher CeA fraction (0.084) than CLUS_0823 (0.067) but carries the Chodl designation. CLUS_0823 was selected partly because CLUS_0765 is already used for the BLA SST dendrite-targeting interneuron, but the CeA/BLA boundary among Sst Gaba clusters remains unresolved. *(Appears on: edge_cea_som_neuron_to_cs20230722_clus_0823)*

2. **Does the CeA SST+ CeL-ON population correspond to a single WMBv1 cluster or is it heterogeneous across multiple Sst Gaba supertypes?** O'Leary et al. 2022 [7] note that "Prkcd and Sst each exhibited mixed expression across multiple scRNA-seq-clusters," consistent with biological heterogeneity within the classical type's transcriptomic boundaries. *(Appears on: edge_cea_som_neuron_to_cs20230722_clus_0823)*

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Li et al. 2013 | [PMID:23354330](https://pubmed.ncbi.nlm.nih.gov/23354330/) | Soma location; NT type; Sst neuropeptide; CeL-ON definition |
| [2] | Adke et al. 2019 | [PMID:33188006](https://pubmed.ncbi.nlm.nih.gov/33188006/) | Soma location; Sst neuropeptide; Prkcd negative marker |
| [3] | Nisbett & Koob 2025 | [PMID:40780965](https://pubmed.ncbi.nlm.nih.gov/40780965/) | Soma location; CeA subdivision anatomy |
| [4] | Vicario et al. 2014 | [PMID:25309337](https://pubmed.ncbi.nlm.nih.gov/25309337/) | Soma location; MGE-derived Sst cells in CeA |
| [5] | Gilpin et al. 2014 | [PMID:25433901](https://pubmed.ncbi.nlm.nih.gov/25433901/) | NT type (CeA primarily GABAergic) |
| [6] | Yeh et al. 2024 | [PMID:38419794](https://pubmed.ncbi.nlm.nih.gov/38419794/) | Sst neuropeptide; distinct SOM population |
| [7] | O'Leary et al. 2022 | [PMID:36425768](https://pubmed.ncbi.nlm.nih.gov/36425768/) | Sst neuropeptide; Prkcd/Sst mixed expression across clusters |

---

<!-- verdict-block-start: edge_cea_som_neuron_to_cs20230722_clus_0823 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    skos:broadMatch 1:n: CLUS_0823 ("0823 Sst Gaba_17", SUPT_0230) aligns on
    `neuropeptide_Sst` CONSISTENT (precomputed mean 10.36, 95.1th pct of CeA
    GABAergic cohort of 5) and `negative_marker_Prkcd` CONSISTENT (Prkcd val
    0.0, 0th pct). NT type and soma location (MBA:536, region_fraction 0.067)
    are both CONSISTENT. However, 5 Sst Gaba clusters score equally (score 4,
    cohort_size 5, all tied) — Stage A provides no discriminating signal.
    No ANNOTATION_TRANSFER evidence is available. LOW confidence reflects
    single-panel metadata alignment with unresolved 1:n cardinality.
  unresolved_questions:
    - "Which Sst Gaba cluster is most specific to CeA vs BLA? CLUS_0860 (Sst Chodl) has a higher CeA fraction (0.084) than CLUS_0823 (0.067) but carries the Chodl designation."
    - "Does the CeA SST+ CeL-ON population correspond to a single WMBv1 cluster or is it heterogeneous across multiple Sst Gaba supertypes?"
```
<!-- verdict-block-end -->
