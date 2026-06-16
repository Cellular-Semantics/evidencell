# Basolateral amygdala calbindin-positive dendrite-targeting interneuron — CCN20230722 Mapping Report
*2026-06-16 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Calbindin-positive (CALB1+), parvalbumin-negative GABAergic interneurons in the basolateral amygdala (BLA) constitute a functionally specialised class of dendrite-targeting inhibitory cells that preferentially innervate the distal dendrites of principal neurons, thereby shaping synaptic integration rather than output gain control [1][3]. Bienvenu et al. 2012 characterised these cells as a distinct GABAergic type within the BLA, separable from parvalbumin-expressing basket and axo-axonic cells by their CALB1 immunoreactivity, dendritic targeting morphology, and the absence of SST co-expression in strictly defined populations [1].

---

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala complex [UBERON:0002887] | [1] |
| Neurotransmitter | GABAergic | [1][2][3] |
| Defining markers | Calb1 | [1][2][4][5] |
| Negative markers | Pvalb | [2] |
| Neuropeptides | — | — |

<details>
<summary>Per-property literature support</summary>

**Soma location.** Bienvenu et al. 2012 characterised calbindin-positive dendrite-targeting interneurons in the BLA proper, placing these cells within the basolateral amygdala complex [UBERON:0002887] [1].

**Neurotransmitter (GABAergic).** Inhibitory identity is supported by three independent lines of evidence. Bienvenu et al. 2012 used immunocytochemistry for GABA and CALB1 to identify these cells as GABAergic [1]. Flores et al. 2017 documented activation of calbindin-expressing GABAergic interneurons in the BLA following orexin-1 receptor antagonism [2]. Vereczki et al. 2021 used transgenic mice and viral strategies to enumerate GABAergic cell types in the lateral and basal amygdalar nuclei, reporting that dendrite-targeting inhibitory cells together compose a major fraction of total GABAergic cells [3].

**Calb1 (defining marker).** Bienvenu et al. 2012 reported:

> "calbindin-positive interneurons targeting dendrites"
> — Bienvenu et al. 2012, Basolateral amygdala and corticobasal cell types · [1] <!-- quote_key: 10647550_48ea3c0f -->

Ünal et al. 2020 noted co-expression of calbindin with somatostatin and NPY in the BLA interneuron population [4]. Cardenas et al. 2019 confirmed CALB1 immunoreactivity in amygdala interneurons and its co-occurrence with parvalbumin in some cells [5].

**Pvalb (negative marker).** Flores et al. 2017 explicitly distinguished calbindin-expressing from parvalbumin-expressing interneurons in the BLA:

> "GABAergic interneurons expressing calbindin, but not parvalbumin, were also activated by orexin-1 receptor antagonism in the basolateral amygdala."
> — Flores et al. 2017, dendrite-targeting interneurons · [2] <!-- quote_key: 17860491_f1ffddb9 -->

**Notes.** The classical node carries the qualifier that it overlaps partially with SOM/CB+ interneurons in older marker schemes; CALB1 positivity without SST co-expression is the defining criterion.

</details>

---

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

**No atlas cluster or supertype in CCN20230722 achieves a confident match to the basolateral amygdala calbindin-positive dendrite-targeting interneuron.** All ten candidates assessed via atlas metadata show either low Calb1 expression inconsistent with the strong CALB1-defining character of the classical type, or high Calb1 expression concentrated in striatal and pallidal regions rather than the basolateral amygdala. The absence of annotation transfer data and the unresolved soma location on the classical node mean that the mapping remains UNCERTAIN across the full candidate set.

The three most informative candidates are examined below to characterise the nature and limits of the available evidence.

---

### Table 1 — Property comparison: 0657 Vip Gaba_9 [CS20230722_CLUS_0657]

| Property | Classical | Atlas cluster | Alignment |
|---|---|---|---|
| Neurotransmitter | GABAergic | GABA | CONSISTENT |
| Soma location | Basolateral amygdala complex [UBERON:0002887] | Cortical subplate [MBA:703] (82 cells/100µm), Hippocampal formation [MBA:1089] (52/100µm), Olfactory areas [MBA:698] (42/100µm); region_fraction_100um=0.172 | APPROXIMATE |
| Calb1 | Defining marker | Mean expression 1.42; cohort percentile 0.404 | APPROXIMATE |
| Pvalb | Absent | 0.07 (below MIN_DETECTABLE); cohort percentile 0.563 | CONSISTENT |

### Table 2 — Evidence support: 0657 Vip Gaba_9 [CS20230722_CLUS_0657]

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | ATLAS_METADATA | PARTIAL | region_fraction_100um=0.172; Calb1=1.42 | CCN20230722 |

---

### ### 0657 Vip Gaba_9 · ⚪ UNCERTAIN

Atlas metadata provides the primary evidence for this candidate. The cluster [CS20230722_CLUS_0657] contains 310 cells and belongs to supertype 0181 Vip Gaba_9. The neurotransmitter annotation (GABA) is consistent with the classical GABAergic identity. The most supportive expression signal is Calb1 at a mean of 1.42 (cohort percentile 0.404), the highest Calb1 value among all cluster-level candidates in this cohort. Parvalbumin expression is near-zero (0.07), confirming consistency with the Pvalb-negative requirement. However, the anatomical distribution is approximate rather than specific: 17.2% of nearby cells (within 100 µm) are within basolateral-adjacent regions — predominantly Cortical subplate [MBA:703] and Hippocampal formation [MBA:1089] rather than the basolateral nucleus proper. A strict region fraction of only 8.9% indicates that the majority of this cluster's cells lie outside the BLA. The Calb1 expression level, while the highest among cluster candidates, falls substantially below the strong CALB1 positivity that defines the classical type by immunohistochemistry, placing this candidate in an ambiguous zone.

**Supporting evidence:**
- GABAergic neurotransmitter annotation consistent with classical type [ATLAS_METADATA]
- Calb1 mean expression 1.42 (cohort percentile 0.404) — highest Calb1 among cluster-level candidates in this GABAergic BLA cohort
- Pvalb expression 0.07, below the minimal detectable threshold, consistent with Pvalb-negative classical definition

**Marker evidence provenance:**
- Calb1 and Pvalb values derive from precomputed expression in the CCN20230722 atlas (WMBv1); data source is single-nucleus RNA-seq (10x Genomics)
- No patch-seq, immunostaining, or transgenic driver confirmation is available for this specific cluster in the current evidence base
- ⚠ Calb1 expression at 1.42 is in the low-to-moderate range by atlas cohort standards (cohort percentile 0.404); for a classically CALB1-defining type this is below what immunohistochemical positivity implies

**Concerns:**
- Strict region fraction 8.9% indicates most cells in this cluster do not co-localise spatially with the BLA, undermining anatomical specificity
- The soma location field on the classical node is unresolved ("?"), making it impossible to confirm that UBERON:0002887 maps to the atlas regions where this cluster is enriched
- No annotation transfer data are available to assess transcriptomic classification fidelity

**What would upgrade confidence:**
- Annotation transfer from a CALB1-reporter or immunostained BLA dataset would directly test whether CALB1+ dendrite-targeting interneurons transcriptomically sort into this cluster
- Patch-seq or post-hoc immunostaining of 0657 Vip Gaba_9 cells to confirm CALB1 protein positivity and dendritic targeting morphology
- Resolution of the soma location field to a specific atlas region code would allow a strict rather than approximate location comparison

---

### Table 1 — Property comparison: 0289 STR-PAL Chst9 Gaba_5 [CS20230722_SUPT_0289]

| Property | Classical | Atlas supertype | Alignment |
|---|---|---|---|
| Neurotransmitter | GABAergic | Not asserted | NOT_ASSESSED |
| Soma location | Basolateral amygdala complex [UBERON:0002887] | Striatum [MBA:477] (612/100µm), Cortical subplate [MBA:703] (515/100µm), Basomedial amygdalar nucleus ant. [MBA:327] (315/100µm); region_fraction_100um=0.262 | APPROXIMATE |
| Calb1 | Defining marker | Mean 6.13; cohort percentile 0.768; child-cluster coverage 1.000 | CONSISTENT |
| Pvalb | Absent | 0.03 (below MIN_DETECTABLE); cohort percentile 0.280 | CONSISTENT |

### Table 2 — Evidence support: 0289 STR-PAL Chst9 Gaba_5 [CS20230722_SUPT_0289]

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | ATLAS_METADATA | PARTIAL | region_fraction_100um=0.262; Calb1=6.13 (cohort pct 0.768) | CCN20230722 |

---

### 0289 STR-PAL Chst9 Gaba_5 · ⚪ UNCERTAIN

Atlas metadata is the sole evidence type for this supertype-level candidate. The supertype [CS20230722_SUPT_0289] comprises 1,533 cells and has a strong Calb1 expression signal — mean 6.13, cohort percentile 0.768, with complete child-cluster coverage (1.000), indicating that all constituent clusters within this supertype express Calb1 at elevated levels. Pvalb expression is near-absent (0.03). These two marker properties align well with the classical definition. However, the anatomical distribution is the central obstacle: the leading enrichment region is the Striatum [MBA:477], followed by Cortical subplate [MBA:703] and Basomedial amygdalar nucleus, anterior part [MBA:327]. The STR-PAL (striatum–pallidum) nomenclature of this supertype's subclass directly reflects its primary identity as a striatal-pallidal cell population. While the Basomedial amygdalar nucleus [MBA:327] is included in the top three regions, the overall distribution is dominated by striatal tissue, which is outside the basolateral amygdala complex. The NT type is not asserted in atlas metadata for this supertype, precluding a direct comparison with the GABAergic classical type.

**Supporting evidence:**
- Calb1 mean expression 6.13 (cohort percentile 0.768, child-cluster coverage 1.000) — consistent with a CALB1-enriched population
- Pvalb 0.03 — Pvalb-negative profile matches the classical exclusion criterion
- Partial amygdala-adjacent location (Basomedial amygdalar nucleus, anterior part [MBA:327]) among top enriched regions

**Marker evidence provenance:**
- Calb1 and Pvalb from precomputed single-nucleus RNA-seq expression (CCN20230722); child-cluster coverage of 1.000 indicates the Calb1 signal is uniformly distributed across all child clusters of this supertype, not driven by a single outlier cluster
- NT type not asserted at the supertype level; cannot confirm GABAergic identity from atlas metadata alone
- ⚠ STR-PAL class assignment indicates this supertype's primary biological identity is striatal-pallidal, not amygdaloid — atlas annotation supports a different regional origin

**Concerns:**
- Predominant striatal distribution (Striatum [MBA:477] leads enrichment) is inconsistent with a BLA interneuron identity
- NT type not asserted — cannot confirm GABAergic identity from atlas metadata for this candidate
- No annotation transfer data available

**What would upgrade confidence:**
- Demonstration via in situ hybridisation or immunohistochemistry that CALB1+ GABAergic cells in the BLA cluster with this STR-PAL supertype rather than with VIP-class supertypes
- Single-cell transcriptomic profiling of immunohistochemically confirmed BLA CALB1+ interneurons to determine which WMBv1 class they transcriptomically resemble

---

### Table 1 — Property comparison: 0288 STR-PAL Chst9 Gaba_4 [CS20230722_SUPT_0288]

| Property | Classical | Atlas supertype | Alignment |
|---|---|---|---|
| Neurotransmitter | GABAergic | Not asserted | NOT_ASSESSED |
| Soma location | Basolateral amygdala complex [UBERON:0002887] | Striatum [MBA:477] (4,354/100µm), Cortical subplate [MBA:703] (2,393/100µm), Central amygdalar nucleus [MBA:536] (2,052/100µm); region_fraction_100um=0.117 | APPROXIMATE |
| Calb1 | Defining marker | Mean 3.39; cohort percentile 0.549; child-coverage 1.000; atlas category: DEFINING | CONSISTENT |
| Pvalb | Absent | 0.01 (below MIN_DETECTABLE); cohort percentile 0.110 | CONSISTENT |

### Table 2 — Evidence support: 0288 STR-PAL Chst9 Gaba_4 [CS20230722_SUPT_0288]

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | ATLAS_METADATA | PARTIAL | region_fraction_100um=0.117; Calb1=3.39 (DEFINING); Pvalb=0.01 | CCN20230722 |

---

### 0288 STR-PAL Chst9 Gaba_4 · ⚪ UNCERTAIN

This supertype [CS20230722_SUPT_0288] is notable for carrying an explicit atlas annotation of Calb1 as a DEFINING marker — the only candidate in this cohort where the atlas itself designates Calb1 as a defining feature at the supertype level. The 4,588-cell supertype shows Calb1 mean expression of 3.39 (cohort percentile 0.549), with complete child-cluster coverage (1.000) and near-absent Pvalb (0.01). These properties are consistent with a CALB1+/PVALB− profile. The atlas-annotated DEFINING status for Calb1 provides additional support that this supertype is biologically characterised by Calb1 expression. However, the anatomical distribution presents a major obstacle identical to that seen for 0289: this is a STR-PAL class supertype whose primary enrichment is strongly in the Striatum [MBA:477] (4,354 cells within 100 µm), with Cortical subplate [MBA:703] and Central amygdalar nucleus [MBA:536] as secondary regions. The Central amygdalar nucleus is not part of the basolateral amygdala. The region_fraction_100um of 0.117 and strict region_fraction of 0.065 indicate only modest spatial overlap with the BLA region queried.

**Supporting evidence:**
- Calb1 atlas annotation category: DEFINING — the CCN20230722 atlas independently designated Calb1 as a defining feature of this supertype
- Calb1 mean expression 3.39 (cohort percentile 0.549, child-cluster coverage 1.000)
- Pvalb 0.01 — lowest Pvalb expression of all supertype candidates; strongly consistent with the Pvalb-negative classical definition

**Marker evidence provenance:**
- Atlas DEFINING annotation for Calb1 derives from the CCN20230722 annotation pipeline (WMBv1 Allen Brain Cell Atlas)
- NT type not asserted for this supertype in atlas metadata
- ⚠ STR-PAL class assignment indicates primary striatal-pallidal identity; the atlas DEFINING Calb1 annotation likely reflects a shared striatal interneuron property rather than amygdaloid identity
- ⚠ Central amygdalar nucleus [MBA:536] is in the third enrichment position but is anatomically distinct from the basolateral amygdala complex [UBERON:0002887]

**Concerns:**
- Striatum [MBA:477] leads the anatomical distribution overwhelmingly (4,354 cells/100µm versus 2,393 in Cortical subplate)
- NT type not asserted — cannot directly confirm GABAergic identity
- No annotation transfer data available

**What would upgrade confidence:**
- Annotation transfer from a validated BLA CALB1+ interneuron dataset would test whether this STR-PAL supertype captures any BLA CALB1+ cells
- Marker panel comparing Calb1, Chst9 (the supertype-naming gene), and BLA-specific markers in the same cells would clarify whether BLA and striatal CALB1+ cells co-cluster here

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster / supertype | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---|---|---|---|
| 0657 Vip Gaba_9 [CS20230722_CLUS_0657] | 0181 Vip Gaba_9 | 310 | ⚪ UNCERTAIN | Calb1=1.42 (cohort pct 0.404); region_fraction_100um=0.172; Pvalb=0.07 | Highest cluster-level Calb1; anatomically approximate; no AT data |
| 0289 STR-PAL Chst9 Gaba_5 [CS20230722_SUPT_0289] | — (supertype) | 1,533 | ⚪ UNCERTAIN | Calb1=6.13 (pct 0.768); child-coverage=1.0; partial amygdala; striatal predominance | Strong Calb1 signal; wrong primary region |
| 0288 STR-PAL Chst9 Gaba_4 [CS20230722_SUPT_0288] | — (supertype) | 4,588 | ⚪ UNCERTAIN | Calb1=3.39 (DEFINING); Pvalb=0.01; striatum-led distribution | Atlas-annotated DEFINING for Calb1; striatal primary identity |
| 0625 Vip Gaba_1 [CS20230722_CLUS_0625] | 0173 Vip Gaba_1 | 1,307 | ⚪ UNCERTAIN | Calb1=0.44 (pct 0.113); region_fraction_100um=0.158 | Eliminated: Calb1 expression below cohort median; inadequate marker support |
| 0634 Vip Gaba_3 [CS20230722_CLUS_0634] | 0175 Vip Gaba_3 | 1,780 | ⚪ UNCERTAIN | Calb1=0.42 (pct 0.093); region_fraction_100um=0.109 | Eliminated: lowest Calb1 among cluster candidates; olfactory area leading enrichment |
| 0636 Vip Gaba_4 [CS20230722_CLUS_0636] | 0176 Vip Gaba_4 | 750 | ⚪ UNCERTAIN | Calb1=0.41 (pct 0.086); region_fraction_100um=0.142 | Eliminated: lowest Calb1 cohort percentile in cluster set |
| 0656 Vip Gaba_9 [CS20230722_CLUS_0656] | 0181 Vip Gaba_9 | 192 | ⚪ UNCERTAIN | Calb1=0.74 (pct 0.238); region_fraction_100um=0.119 | Eliminated: smaller cluster than 0657 with lower Calb1; both share supertype 0181 |
| 0233 STR Prox1 Lhx6 Gaba_1 [CS20230722_SUPT_0233] | — (supertype) | 630 | ⚪ UNCERTAIN | Calb1=9.20 (pct 0.963); DISCORDANT location (Striatum + Medial amygdala) | Eliminated: highest Calb1 expression but DISCORDANT anatomical location (Striatum [MBA:477] + Medial amygdalar nucleus [MBA:403]) |
| 0292 IA Mgp Gaba_3 [CS20230722_SUPT_0292] | — (supertype) | 443 | ⚪ UNCERTAIN | Calb1=0.75 (pct 0.207); region_fraction_100um=0.152 | Eliminated: low Calb1 cohort percentile; Intercalated amygdala / Endopiriform distribution |
| 0291 IA Mgp Gaba_2 [CS20230722_SUPT_0291] | — (supertype) | 462 | ⚪ UNCERTAIN | Calb1=0.63 (pct 0.183); strict region_fraction=0.023 | Eliminated: lowest strict region fraction of all candidates; low Calb1 |

</details>

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Basolateral amygdala calbindin-positive dendrite-targeting interneuron is defined as a GABAergic interneuron characterised by Calb1 (CALB1) immunoreactivity, absence of parvalbumin co-expression, and dendritic targeting morphology in the basolateral amygdala complex [UBERON:0002887]. The node ID is `bla_calbindin_dendrite_targeting_interneuron` and the definition basis is CLASSICAL.

**Atlas mapping query.** Candidates were retrieved from the Allen Brain Cell Atlas CCN20230722 (WMBv1) by querying at ranks 0 (cluster level) and 1 (supertype level) for GABAergic nodes with soma enrichment in the BLA (region query: MBA:295, neurotransmitter type: GABAergic). Each candidate was scored against Calb1 expression and Pvalb negativity.

**Property alignment.** Calb1 and Pvalb expression values are precomputed means from the CCN20230722 atlas. Cohort percentile rankings are computed within the survival cohort (GABAergic nodes with region filter MBA:295). Location comparisons use MERFISH-painted cell counts within 100 µm (region_fraction_100um) and strict co-location fractions.

**Annotation transfer.** No annotation transfer runs were performed for this node. The pool candidates file is empty.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Reproducibility footer.**
*Generated by evidencell `a4a555f` at 2026-06-16T11:53:32+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

**Evidence base table:**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_CLUS_0657 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_SUPT_0289 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_SUPT_0288 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_CLUS_0625 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_CLUS_0634 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_CLUS_0636 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_CLUS_0656 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_SUPT_0233 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_SUPT_0292 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_SUPT_0291 | ATLAS_METADATA | PARTIAL | CCN20230722 |

</details>

---

## Discussion

### Best candidate and caveats summary

**Primary mapping:** Basolateral amygdala calbindin-positive dendrite-targeting interneuron → no confident atlas match identified. The closest available candidate by combined Calb1 expression and partial amygdala location is 0657 Vip Gaba_9 [CS20230722_CLUS_0657] (UNCERTAIN confidence), but this assignment cannot be made with confidence given the low Calb1 expression relative to the classical defining criterion, the limited spatial overlap with the BLA, and the absence of annotation transfer data. Supertypes 0289 and 0288 in the STR-PAL Chst9 class have stronger Calb1 expression (up to 6.13 and 3.39 respectively, with atlas-annotated DEFINING status for 0288) but their primary anatomical identity is striatal-pallidal, not amygdaloid.

The fundamental obstacle to this mapping is a class-level discordance: classical CALB1+ interneurons defined by immunohistochemistry in the BLA do not obviously correspond to any single transcriptomic cluster or supertype in the WMBv1 atlas. This is consistent with the known heterogeneity of CALB1+ interneurons across cortical and pallidal structures — CALB1 is expressed in multiple molecularly distinct interneuron classes, and the classical phenotypic definition may cross-cut transcriptomic taxonomy boundaries.

### Proposed experiments

- **Annotation transfer from a BLA single-cell dataset.** A published or in-house snRNA-seq or scRNA-seq dataset from the BLA with CALB1+ interneurons identified by transgene driver or immunostaining would enable direct transcriptomic assignment of the classical type to WMBv1 clusters. This is the highest-priority experiment for resolving the mapping.
- **Patch-seq of BLA CALB1+ interneurons.** Combining whole-cell patch-clamp recording (to confirm dendrite-targeting inhibitory physiology) with single-cell RNA-seq would allow unambiguous assignment of physiologically characterised cells to atlas clusters.
- **In situ hybridisation panel for Vip/Calb1/Chst9 in the BLA.** Multiplexed FISH with probes for Calb1, Vip, Chst9, and Pvalb would clarify whether BLA CALB1+ interneurons are transcriptomically VIP-class (consistent with cluster-level candidates) or STR-PAL class (consistent with high-Calb1 supertype candidates).
- **Resolution of the classical node soma location.** Updating the `anatomical_location` field to a specific WMBv1 region code (beyond the broad UBERON:0002887) would allow strict rather than approximate location comparisons in the atlas.

### Open questions

1. Do BLA CALB1+ dendrite-targeting interneurons transcriptomically resemble VIP-class (Vip Gaba) or STR-PAL-class (Chst9 Gaba) cells, or do they occupy a distinct transcriptomic space not well captured by either?
2. Is the classical CALB1+ dendrite-targeting BLA interneuron a single transcriptomic type or a heterogeneous grouping? Older marker schemes conflate CALB1+/SST− interneurons with CALB1+/SST+ interneurons; this ambiguity propagates into the atlas mapping.
3. Does the high Calb1 expression in STR-PAL supertypes (e.g., 0233 STR Prox1 Lhx6 Gaba_1 at 9.20) reflect a biologically distinct Calb1-high population that extends into the amygdala, or is it a striatal-specific property?

---

## References

[1] Bienvenu et al. 2012 · PMID:22726836 · DOI:10.1016/j.neuron.2012.04.022
[2] Flores et al. 2017 · PMID:28453642 · DOI:10.1093/ijnp/pyx029
[3] Vereczki et al. 2021 · PMID:33837051 · DOI:10.1101/2021.03.15.435365
[4] Ünal et al. 2020 · PMID:32144495 · DOI:10.1007/s00429-020-02051-4
[5] Cardenas et al. 2019 · PMID:31193505 · DOI:10.1016/j.ynstr.2019.100163

---

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_CLUS_0657 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.20
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] 0657 Vip Gaba_9 [CS20230722_CLUS_0657] is the strongest cluster-level
    candidate by Calb1 expression (mean=1.42, cohort percentile 0.404) and region_fraction_100um=0.172,
    but Calb1 expression is well below the level expected for a classically CALB1-defining interneuron,
    the strict region fraction is 0.089, and no annotation transfer data exist; confidence is UNCERTAIN.
  reconciliation_note: >
    The classical type's soma location field is unresolved (UBERON:0002887 without atlas region
    specificity), making it impossible to compute a strict anatomical match score. Resolving the
    location to an MBA region code and performing annotation transfer would be required to upgrade
    this to even MODERATE confidence.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Calb1 expression (1.42, cohort pct 0.404) is in the moderate range by atlas cohort
        standards; the classical CALB1-defining criterion based on antibody-based protein detection implies
        a higher expression level than is observed here.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Strict region fraction of 0.089 indicates most cells in this cluster do not spatially
        co-localise with the BLA region queried (MBA:295).
  proposed_experiments:
    - >
      Annotation transfer from a CALB1-reporter or immunostained BLA single-cell dataset to
      determine whether CALB1+ dendrite-targeting interneurons sort into this cluster or an
      alternative transcriptomic group.
    - >
      Paired single-cell sequencing and post-hoc CALB1 antibody staining of BLA CALB1+ interneurons to
      identify their WMBv1 cluster assignment.
  unresolved_questions:
    - >
      Do BLA CALB1+ dendrite-targeting interneurons transcriptomically resemble VIP-class
      (Vip Gaba supertype) cells or STR-PAL class cells?
    - >
      What is the specific atlas region (MBA code) of the soma of this classical type?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_SUPT_0289 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.18
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] 0289 STR-PAL Chst9 Gaba_5 [CS20230722_SUPT_0289] has strong Calb1 expression
    (mean=6.13, cohort pct 0.768, child-coverage=1.000) and Pvalb near-absent (0.03), but its
    primary anatomical distribution is striatal (Striatum [MBA:477]) rather than basolateral
    amygdalar; NT type is not asserted; confidence is UNCERTAIN.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        STR-PAL class identity indicates primary striatal-pallidal origin; Basomedial amygdalar
        nucleus [MBA:327] is present but not the leading enrichment region.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Neurotransmitter type not asserted in atlas metadata for this supertype; cannot directly
        confirm GABAergic identity.
  proposed_experiments:
    - >
      Annotation transfer from a validated BLA CALB1+ interneuron dataset to test whether
      BLA CALB1+ cells transcriptomically cluster with STR-PAL supertypes.
    - >
      In situ hybridisation panel combining Calb1, Chst9, and BLA-specific markers to
      determine the regional boundaries of the Chst9+/Calb1+ population.
  unresolved_questions:
    - >
      Is the high Calb1 expression in STR-PAL supertypes a shared property extending into
      the BLA, or a striatal-specific phenomenon?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_SUPT_0288 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:WEAKEST] 0288 STR-PAL Chst9 Gaba_4 [CS20230722_SUPT_0288] carries an atlas
    DEFINING annotation for Calb1 (mean=3.39, child-coverage=1.000) and near-absent Pvalb (0.01),
    but its distribution is overwhelmingly striatal (Striatum [MBA:477] leads with 4,354 cells/100µm),
    the NT type is not asserted, and region_fraction_100um=0.117 at this BLA query is low;
    confidence is UNCERTAIN.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Overwhelmingly striatal primary distribution; Central amygdalar nucleus [MBA:536]
        (not basolateral amygdala) is the third enriched region.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        NT type not asserted in atlas metadata; GABAergic identity cannot be confirmed
        from available evidence.
  proposed_experiments:
    - >
      Multiplexed FISH with Calb1, Chst9, and BLA principal cell markers to determine
      the extent of Chst9+/Calb1+ cells in the BLA versus striatum.
  unresolved_questions:
    - >
      Does the atlas DEFINING Calb1 annotation for this STR-PAL supertype reflect
      convergent evolution of Calb1 expression in striatal and amygdaloid interneurons
      or a shared transcriptomic ancestry?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_CLUS_0625 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.08
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] 0625 Vip Gaba_1 [CS20230722_CLUS_0625] has Calb1=0.44 (cohort pct 0.113),
    below the cohort median for a classically CALB1-defining type; region_fraction_100um=0.158
    but Cortical subplate leads over amygdala-specific regions; no AT data; UNCERTAIN.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_CLUS_0634 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.07
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] 0634 Vip Gaba_3 [CS20230722_CLUS_0634] has Calb1=0.42 (cohort pct 0.093),
    the lowest among Calb1-scoring cluster candidates; Olfactory areas [MBA:698] leads
    its distribution; region_fraction_100um=0.109; UNCERTAIN.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_CLUS_0636 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.07
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] 0636 Vip Gaba_4 [CS20230722_CLUS_0636] has the lowest Calb1 cohort percentile
    among cluster candidates (val=0.41, pct 0.086); Cortical subplate leads over BLA regions;
    region_fraction_100um=0.142; UNCERTAIN.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_CLUS_0656 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] 0656 Vip Gaba_9 [CS20230722_CLUS_0656] shares supertype 0181 with the stronger
    sibling 0657 but is smaller (192 cells) with lower Calb1 expression (val=0.74, pct 0.238)
    and lower region_fraction_100um (0.119); dominated by 0657 on all relevant metrics; UNCERTAIN.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_SUPT_0233 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.12
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] 0233 STR Prox1 Lhx6 Gaba_1 [CS20230722_SUPT_0233] has the highest Calb1
    expression in the cohort (mean=9.20, pct 0.963, child-coverage=1.000) but its location
    is DISCORDANT — primary enrichment in Striatum [MBA:477] and Medial amygdalar nucleus
    [MBA:403], not basolateral amygdala; strict region_fraction=0.039; UNCERTAIN.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        DISCORDANT location comparison: Striatum and Medial amygdalar nucleus are the leading
        enriched regions; these are anatomically distinct from the basolateral amygdala complex.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_SUPT_0292 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.08
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] 0292 IA Mgp Gaba_3 [CS20230722_SUPT_0292] has Calb1=0.75 (cohort pct 0.207)
    and a distribution centred on Cortical subplate and Endopiriform nucleus; IA (intercalated
    amygdala) identity is inconsistent with basolateral amygdala; strict region_fraction=0.056;
    UNCERTAIN.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_calbindin_dendrite_targeting_interneuron_to_CS20230722_SUPT_0291 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.07
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] 0291 IA Mgp Gaba_2 [CS20230722_SUPT_0291] has the lowest strict region
    fraction of all candidates (0.023), Calb1=0.63 (cohort pct 0.183), and a distribution
    centred on Cortical subplate and Endopiriform nucleus; dominated by 0292 on all metrics
    and has weaker amygdala relevance; UNCERTAIN.
```
<!-- verdict-block-end -->
