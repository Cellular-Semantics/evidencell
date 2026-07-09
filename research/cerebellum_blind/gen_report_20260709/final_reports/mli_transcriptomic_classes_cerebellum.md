# Molecular layer interneuron transcriptomic classes MLI1 / MLI2 (class I / class II) — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml`*

---

## Introduction

Molecular layer interneurons (MLIs) of the cerebellar cortex comprise GABAergic cells that reside throughout the thickness of the molecular layer of cerebellar cortex [UBERON:0002974] and have historically been classified by morphology as basket cells (inner layer) and stellate cells (outer layer). Single-nucleus RNA sequencing revealed that this morphological distinction incompletely captures the underlying transcriptomic organisation: MLIs are instead organised into two molecularly and functionally discrete classes — MLI1 (class I) and MLI2 (class II) — distinguished by differential expression of Sorcs3 and Nxph1, respectively [1][2][3]. This classical node, grounded in prior transcriptomic evidence, represents both classes jointly, given the historical tendency to study them together and the absence of a Cell Ontology term covering the class split.

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] | [1] |
| NT type | GABAergic | [1] |
| Defining markers | Sorcs3 (MLI1 / class I), Nxph1 (both classes; enriched in MLI2), Pvalb (MLI2 / class II) | [2][3][4] |
| Neuropeptides | Nxph1 | [4] |
| CL term | molecular layer interneuron (CL:4042035) — BROAD | |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** single-nucleus RNA-seq, mouse cerebellar cortex · [1]

  > For multiple types of cerebellar interneurons, the molecular variation within each type was more continuous, rather than discrete. For the unipolar brush cells (UBCs)—an interneuron population previously subdivided into two discrete populations—the continuous variation in gene expression was associated with a graded continuum of electrophysiological properties. Most surprisingly, we found that molecular layer interneurons (MLIs) were composed of two molecularly and functionally distinct types. Both show a continuum of morphological variation through the thickness of the molecular layer, but electrophysiological recordings revealed marked differences between the two types in spontaneous firing, excitability, and electrical coupling.
  > — Kozareva et al. 2020, Anatomical organization and core cell types · [1] <!-- quote_key: 214725795_3d3df51c -->

- **Defining markers (Sorcs3, Nxph1):** review/commentary on MLI class characterisation · [2]

  > 2021) also examined the development of molecular layer inhibitory interneurons, which have been historically separated into stellate and basket cells based on their morphology (Leto et al., 2015)(2020)(Leto et al., 2009). This distinction is a little unclear however as many of these interneurons display mixed morphologies, leading to the conclusion that these cells may represent a morphological contiuum. Surprisingly, their adult snRNAseq data revealed two classes of molecular layer interneurons, which they termed as class I (MLI1 and Sorcs3+) and class II (MLI2 and Nxph1+). In an effort to examine the development of these interneurons, the authors expanded their analysis to 5500 GABAergic progenitors across four stages of development and could distinguish between the distinct developmental trajectories of class I and class II interneurons. Although these cells develop from common progenitors, class II differentially expressed immediate early genes such as Fos during their development, which the authors concluded might indicate a higher cellular activity during their specification. Both classes of interneurons differ in their electrophysiological properties, and many class I, but not class II, are coupled to one another via gap junctions, demonstrating that the transcriptomic differences between these two classes of interneurons are also functionally relevant.
  > — Lowenstein et al. 2022, Anatomical organization and core cell types · [2] <!-- quote_key: 247317953_380921bf -->

- **Defining markers (Sorcs3, Nxph1):** scRNA-seq differential gene expression · [3]

  > Differential gene expression analyses confirmed that MLI t-types were distinguished by Sorcs3 or Nxph1 expression51.
  > — Wang & Lefebvre 2022, Results · [3] <!-- quote_key: 213840122_4cb91d31 -->

- **Defining markers (Pvalb, Nxph1), neuropeptides (Nxph1):** developmental transcriptomic analysis, mouse cerebellum · [4]

  > Whereas granule cells form a homogeneous differentiating population (Fig. 4B), interneurons are stratified into distinct temporally specified subtypes (fig. S13, E and F): early-born interneurons (Zfhx4, Slit2) detected at E13 to E15, mid-born Golgi cells (Chrm2), Purkinje layer interneurons (Nxph1, Klhl1) prevalent at E17 to P7, and late-born molecular layer interneurons of type 1 (Sorcs3, Grm8) and 2 (MLI2; Nxph1, Pvalb), which are abundant at P14 to P63 (Leto et al., 2015)37).
  > — Sarropoulos et al. 2021, Anatomical organization and core cell types · [4] <!-- quote_key: 237308705_5cd4bd6a -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: molecular layer interneuron [[CL:4042035](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4042035)] (BROAD).

The Cell Ontology has no specific term for the MLI1/MLI2 class split; CL:4042035 is the closest ancestor. Both classes are candidates for new CL subtypes.

---

## Results

Atlas metadata evidence supports placement of the MLI1/MLI2 transcriptomic classes within the WMBv1 cerebellar cortex GABAergic interneuron set, with two CBX MLI supertypes emerging as the primary candidates — one capturing the Sorcs3-dominant profile associated with MLI1, and the other the Nxph1/Pvalb-dominant profile associated with MLI2 (see property comparison tables below). Because the classical node spans both transcriptomic classes, no single atlas cluster is expected to fully capture the joint MLI1+MLI2 population; atlas-level scatter across the two CBX MLI lineages is a biological prediction of the dual-class structure rather than a mapping ambiguity.

### 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] · 🟡 MODERATE

Atlas marker metadata and cerebellar cortex location support placement of the MLI1 (class I) component of this joint classical node onto cluster 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] (n=31,095 cells; `region_fraction_100um`: 0.841, lower_bound rollup). The CBX (cerebellar cortex) designation and the high Sorcs3 expression (Sorcs3 mean 10.35; cohort percentile 0.995) anchor this to the MLI1/class I arm of the split described by Kozareva et al. [1] and Sarropoulos et al. [4]. Pvalb is also strongly expressed (mean 11.12; cohort percentile 0.995), consistent with its role as a general MLI marker [4]; Nxph1 is moderate (mean 2.09; cohort percentile 0.364), which aligns with the lower Nxph1 expectation for MLI1 relative to MLI2.

**Supporting evidence:**

- Atlas metadata: cluster 5188 CBX MLI Megf11 Gaba_1 is annotated as a cerebellar cortex (CBX) molecular layer interneuron. Region fraction `region_fraction_100um`: 0.841 (lower_bound rollup — true value may be higher). GABA NT annotation is CONSISTENT with classical GABAergic identity.
- Sorcs3 expression (mean 10.35; cohort percentile 0.995): CONSISTENT with classical Sorcs3-defining marker for MLI1 [2][3].
- Pvalb expression (mean 11.12; cohort percentile 0.995): CONSISTENT with Pvalb as MLI2/general MLI marker [4]; in the atlas this cluster is in the MERFISH panel.
- Nxph1 expression (mean 2.09; cohort percentile 0.364): APPROXIMATE — lower than the strong Nxph1 expected for MLI2, consistent with MLI1 identity.

**Marker evidence provenance:**

- **Sorcs3**: established as a class I (MLI1) marker by Lowenstein et al. [2] and confirmed by differential expression analysis (Wang & Lefebvre [3]). Evidence is transcript-level (scRNA-seq / snRNA-seq). The high Sorcs3 expression on this cluster (pct 0.995) is strongly concordant. No discrepancy between atlas annotation and precomputed expression.
- **Nxph1**: expressed by both classes but at higher levels in MLI2 [2][4]. Precomputed mean 2.09 on this cluster is below the cohort median, consistent with MLI1 identity. No annotation/expression discrepancy per se, but the expected lower level is observed.
- **Pvalb**: established as an MLI2 / late-born MLI marker by Sarropoulos et al. [4] using developmental transcriptomics. Pvalb is tagged as a MERFISH panel gene on this cluster (atlas category: MERFISH); the MERFISH tag indicates panel inclusion for spatial profiling and is not in itself a discriminatory signal. The high precomputed expression (mean 11.12) is consistent with Pvalb being broadly expressed across MLIs in the atlas regardless of class.

**Concerns:**

- The classical node spans both MLI1 and MLI2, and cluster 5188 CBX MLI Megf11 Gaba_1 has a Sorcs3-high / Nxph1-moderate profile, most consistent with MLI1. The MLI2 population is better represented by a separate CBX MLI lineage (see 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] below). No single cluster is expected to fully represent the joint classical node; this mapping is understood as partial coverage.
- `region_fraction_100um`: 0.841 is a lower_bound rollup — non-painted CCF2020 descendants are present and uncounted. The true cerebellar fraction may be higher.
- *(note: Purkinje collaterals are reported to preferentially target one class of MLI over the other in recent literature — this functional asymmetry is not yet reflected in atlas metadata and cannot be assessed from available evidence.)*
- No annotation transfer data are available; confidence is capped at MODERATE in the absence of direct cell-level experimental mapping.

**What would upgrade confidence:**

- MapMyCells annotation transfer using a source dataset with cell-type labels distinguishing MLI1 from MLI2 (e.g. a cerebellar scRNA-seq dataset with Sorcs3/Nxph1-resolved labels). Target: F1 ≥ 0.70 at cluster level for the MLI1-labelled source group. Would add AnnotationTransferEvidence.
- Literature-based confirmation that the Megf11-expressing CBX MLI cluster corresponds specifically to the Sorcs3+ (class I) lineage.

**Table 1 — Property comparison: 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188]**

| Property | Classical | Atlas cluster | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] | Cerebellum [MBA:512]; `region_fraction_100um`: 0.841 (lower_bound) | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Sorcs3 expression | Defining marker (MLI1) | Mean 10.35; cohort pct 0.995 | CONSISTENT |
| Nxph1 expression | Defining marker (both classes; MLI2-enriched) | Mean 2.09; cohort pct 0.364 | APPROXIMATE |
| Pvalb expression | Defining marker (MLI2) | Mean 11.12; cohort pct 0.995 (MERFISH) | CONSISTENT |
| Nxph1 neuropeptide | Nxph1 | Mean 2.09; cohort pct 0.364 | APPROXIMATE |

**Table 2 — Evidence support: 5188 CBX MLI Megf11 Gaba_1**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | Atlas metadata | PARTIAL | `region_fraction_100um`=0.841; strict=0.720; lower_bound | atlas-internal |

*(Child-cluster breakdown not assessed — cluster 5188 CBX MLI Megf11 Gaba_1 is itself a rank-0 cluster; its sibling 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] shares the same supertype 1149 CBX MLI Megf11 Gaba_1 and shows all three markers CONSISTENT at smaller cell count n=154.)*

---

### 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] · 🟡 MODERATE

Atlas metadata evidence supports the MLI2 (class II) component of the joint classical node onto supertype 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] (n=13,098 cells; `region_fraction_100um`: 0.851, lower_bound rollup). The Nxph1-dominant and Pvalb-dominant expression profile on this supertype — Nxph1 mean 11.40 (cohort pct 0.982), Pvalb mean 11.33 (cohort pct 0.991), Sorcs3 mean 0.81 (cohort pct 0.236) — is the inverse of the 5188 pattern and aligns with the MLI2 (class II) arm of the transcriptomic split [2][4]. All child clusters of this supertype express Nxph1 and Pvalb consistently (child-coverage 1.000).

**Supporting evidence:**

- Atlas metadata: supertype 1151 CBX MLI Cdh22 Gaba_1 is annotated as a cerebellar cortex (CBX) molecular layer interneuron. `region_fraction_100um`: 0.851 (lower_bound rollup). NT annotation is absent at supertype level (NOT_ASSESSED), which is a data gap rather than a disagreement.
- Nxph1 expression (mean 11.40; cohort pct 0.982; child-coverage 1.000): CONSISTENT across all child clusters. Nxph1 is the defining marker for MLI2 (class II) [2][4].
- Pvalb expression (mean 11.33; cohort pct 0.991; child-coverage 1.000): CONSISTENT. Pvalb marks the late-born MLI2 lineage [4].
- Sorcs3 expression (mean 0.81; cohort pct 0.236; child-coverage 1.000): APPROXIMATE. Low Sorcs3 is expected for MLI2 (Sorcs3 defines MLI1, not MLI2) [2][3]; the low value is therefore biologically coherent.

**Marker evidence provenance:**

- **Nxph1**: expressed by both MLI classes at the transcript level but enriched in MLI2 [2]. Here precomputed mean 11.40 is in the 98th cohort percentile, consistent with this supertype representing the Nxph1-high (MLI2) arm. No discrepancy between atlas and precomputed expression.
- **Pvalb**: developmental transcriptomics (Sarropoulos et al. [4]) establishes Pvalb as a marker of late-born MLI2. Transcript-level evidence. The high expression here (mean 11.33, pct 0.991) supports MLI2 placement.
- **Sorcs3**: low expression (mean 0.81, pct 0.236) is consistent with MLI2 not being the Sorcs3-defining class. This is not a discordance — it is a biologically predicted absence.
- NT type is NOT_ASSESSED at the supertype level — atlas NT annotation is missing on this node. Classical type is GABAergic. The CLUS_5188 sibling group is annotated GABA in the atlas; the NT gap here is likely a metadata completeness issue.

**Concerns:**

- NT type is NOT_ASSESSED: the atlas supertype lacks NT annotation. This is a data gap and cannot be resolved from available evidence without consulting atlas provenance.
- Sorcs3 at pct 0.236 is only APPROXIMATE. While biologically expected for MLI2, this could also reflect a heterogeneous population spanning both classes. A targeted lit-review or annotation transfer with class-resolved labels is needed to confirm.
- As with CLUS_5188: the classical node spans both classes, and this supertype is proposed as the MLI2 complement. The two candidates together are expected to cover the joint node, but this remains speculative without direct annotation transfer evidence.
- `region_fraction_100um`: 0.851 is a lower_bound rollup — true cerebellar fraction may be higher.

**What would upgrade confidence:**

- MapMyCells annotation transfer with Nxph1-high (MLI2) source cells. Target: F1 ≥ 0.70 at supertype level. Would add AnnotationTransferEvidence and confirm MLI2 placement.
- Atlas NT annotation completion at the supertype level.
- Targeted literature search linking the Cdh22-expressing CBX MLI cluster to the Nxph1+ (class II) lineage.

**Table 1 — Property comparison: 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151]**

| Property | Classical | Atlas supertype | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] | Cerebellum [MBA:512]; `region_fraction_100um`: 0.851 (lower_bound) | CONSISTENT |
| NT type | GABAergic | not asserted | NOT_ASSESSED |
| Sorcs3 expression | Defining marker (MLI1) | Mean 0.81; cohort pct 0.236; child-coverage 1.000 | APPROXIMATE |
| Nxph1 expression | Defining marker (both classes; MLI2-enriched) | Mean 11.40; cohort pct 0.982; child-coverage 1.000 | CONSISTENT |
| Pvalb expression | Defining marker (MLI2) | Mean 11.33; cohort pct 0.991; child-coverage 1.000 | CONSISTENT |
| Nxph1 neuropeptide | Nxph1 | Mean 11.40; cohort pct 0.982; child-coverage 1.000 | CONSISTENT |

**Table 2 — Evidence support: 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151]**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | Atlas metadata | PARTIAL | `region_fraction_100um`=0.851; strict=0.723; lower_bound | atlas-internal |

*(All child clusters of 1151 CBX MLI Cdh22 Gaba_1 show Nxph1 and Pvalb consistently (child-coverage 1.000 for both); Sorcs3 child-coverage 1.000 at a low mean consistent with MLI2 identity. Child-cluster count within this supertype not available from current facts — child-cluster breakdown proposed as a follow-up.)*

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] | 1149 CBX MLI Megf11 Gaba_1 | 31,095 | 🟡 MODERATE | Sorcs3+Pvalb CONSISTENT; CBX MLI; n=31,095 | Primary (MLI1 arm) |
| 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] | — | 13,098 | 🟡 MODERATE | Nxph1+Pvalb CONSISTENT; Sorcs3 low (MLI2) | Secondary (MLI2 arm) |
| 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] | 1149 CBX MLI Megf11 Gaba_1 | 154 | 🔴 LOW | All 3 markers CONSISTENT; small cell count | Eliminated (low cell count; sibling of primary) |
| 1150 CBX MLI Megf11 Gaba_2 [CS20230722_SUPT_1150] | — | 370 | 🔴 LOW | Pvalb CONSISTENT (DEFINING); Nxph1 APPROXIMATE | Eliminated (Nxph1 APPROXIMATE; small n) |
| 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] | 1144 CB PLI Gly-Gaba_1 | 3,066 | 🔴 LOW | NT CONSISTENT; Sorcs3 APPROXIMATE; PLI not CBX MLI | Eliminated (Purkinje layer, not molecular layer) |
| 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] | — | 3,646 | 🔴 LOW | NT missing; Sorcs3 APPROXIMATE; PLI not CBX MLI | Eliminated (Purkinje layer, not molecular layer) |
| 5185 CB PLI Gly-Gaba_4 [CS20230722_CLUS_5185] | 1147 CB PLI Gly-Gaba_4 | 442 | 🔴 LOW | Sorcs3 near-zero (0.065 pct); PLI designation | Eliminated (Purkinje layer; Sorcs3 absent) |
| 1147 CB PLI Gly-Gaba_4 [CS20230722_SUPT_1147] | — | 442 | 🔴 LOW | Sorcs3 near-zero; NT missing; PLI | Eliminated (Purkinje layer; Sorcs3 absent) |
| 4707 LDT Fgf7 Gaba_1 [CS20230722_CLUS_4707] | 1049 LDT Fgf7 Gaba_1 | 202 | 🔴 LOW | LDT (lateral dorsal tegmentum); Pvalb APPROXIMATE | Eliminated (wrong region — lateral dorsal tegmentum) |
| 1157 Bergmann NN_1 [CS20230722_SUPT_1157] | — | 3,321 | 🔴 LOW | "Bergmann" = Bergmann glia; Nxph1 APPROXIMATE; Pvalb low | Eliminated (Bergmann glia — wrong cell class) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical node `mli_transcriptomic_classes_cerebellum` is defined on a PRIOR_TRANSCRIPTOMIC basis, representing molecular layer interneurons of the cerebellar cortex characterised by single-nucleus RNA sequencing (Kozareva et al. 2020 [1]). The two transcriptomic classes — MLI1 (Sorcs3+) and MLI2 (Nxph1+, Pvalb+) — were identified by differential gene expression; their correspondence to basket and stellate cell morphological categories is partial and non-exclusive. Markers: Sorcs3 [2][3], Nxph1 [2], Pvalb [4]; neuropeptide: Nxph1 [4]. NT type: GABAergic [1]. Soma location: molecular layer of cerebellar cortex [UBERON:0002974] [1].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table:**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5188 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1151 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5189 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1150 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5178 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1144 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5185 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1147 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_4707 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1157 | ATLAS_METADATA | PARTIAL | atlas-internal |

*Generated by evidencell `8e05bb5` at 2026-07-09T13:25:36+00:00 from [kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml](../../kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Molecular layer interneuron transcriptomic classes MLI1 / MLI2 (class I / class II) → 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] at MODERATE confidence. Key support: atlas metadata with strong Sorcs3 and Pvalb expression; CBX MLI designation and high cerebellar location fraction. Key caveats: classical node spans two transcriptomic classes and no single atlas cluster covers both; no annotation transfer evidence available; region fraction is a lower_bound rollup.

**Secondary mapping:** → 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] at MODERATE confidence as the proposed MLI2-arm complement. Key support: Nxph1 and Pvalb strongly CONSISTENT; CBX MLI designation. Key caveats: NT annotation missing at supertype level; Sorcs3 APPROXIMATE (biologically expected for MLI2 but requires confirmation).

The Cell Ontology has no specific term for the MLI1/MLI2 class split; molecular layer interneuron [[CL:4042035](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4042035)] is the closest ancestor. Both classes are candidates for new CL subtypes.

### Proposed experiments and follow-ups

**Annotation transfer (MapMyCells)**
- **What:** Run MapMyCells on a source dataset with class-resolved MLI labels (MLI1 / MLI2 defined by Sorcs3 / Nxph1 differential expression), mapping to WMBv1 at cluster and supertype level separately for each class.
- **Target:** F1 ≥ 0.70 at cluster level for each source class.
- **Expected output:** AnnotationTransferEvidence items linking MLI1 cells to CBX MLI Megf11 Gaba_1 clusters and MLI2 cells to CBX MLI Cdh22 Gaba_1 supertype or equivalent.
- **Resolves:** Both primary and secondary mappings; would upgrade confidence from MODERATE to HIGH if F1 threshold met.

**Atlas NT annotation**
- **What:** Confirm NT annotation at supertype level for 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151]. Current atlas metadata lacks NT assertion at this node.
- **Expected output:** CONSISTENT or NOT_ASSESSED confirmation; would resolve one current data gap.

**Literature: Megf11 and Cdh22 as MLI class markers**
- **What:** Targeted literature search for Megf11 and Cdh22 as discriminators of MLI transcriptomic classes in cerebellar cortex; cross-reference with Kozareva 2020 [1] cluster definitions.
- **Expected output:** LiteratureEvidence linking atlas cluster names to the MLI1/MLI2 class split.

### Open questions

1. Does the atlas supertype 1149 CBX MLI Megf11 Gaba_1 (parent of clusters 5188 and 5189 CBX MLI Megf11 Gaba_1) specifically capture the MLI1 (Sorcs3+) population, or does it span both classes? A supertype-level edge is not present in the current candidate set and would help clarify the breadth of the mapping.
2. Is the NT annotation gap at 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] a database completeness issue or does the supertype genuinely lack atlas-side GABAergic annotation?
3. Nxph1 is annotated as a neuropeptide on the classical node but is also a defining marker. The precomputed expression values are the same field; no discrepancy to report, but the dual annotation (marker and neuropeptide) should be reviewed against the primary source to confirm whether Nxph1 functions primarily as a transcript-level marker or also as a secreted peptide in the MLI context.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Kozareva et al. 2020 — https://doi.org/10.1101/2020.03.04.976407 | — | Soma location, GABAergic NT, MLI1/MLI2 discovery |
| [2] | Lowenstein et al. 2022 · PMID:35262281 | [35262281](https://pubmed.ncbi.nlm.nih.gov/35262281/) | Sorcs3 marker (MLI1), Nxph1 marker (MLI2), class electrophysiology |
| [3] | Wang & Lefebvre 2022 · PMID:35701402 | [35701402](https://pubmed.ncbi.nlm.nih.gov/35701402/) | Sorcs3/Nxph1 differential expression confirmation |
| [4] | Sarropoulos et al. 2021 · PMID:34446581 | [34446581](https://pubmed.ncbi.nlm.nih.gov/34446581/) | Pvalb marker (MLI2), Nxph1 neuropeptide, developmental timing |

---

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5188 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.52
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Atlas metadata CONSISTENT for Sorcs3 (mean 10.35; cohort pct 0.995;
    EXPRESSION source) and Pvalb (mean 11.12; cohort pct 0.995); Nxph1 APPROXIMATE
    (mean 2.09; cohort pct 0.364) consistent with MLI1/class I identity based on
    precomputed expression cohort percentiles
    (marker_Sorcs3 CONSISTENT; marker_Pvalb CONSISTENT; marker_Nxph1 APPROXIMATE —
    2 of 4 markers CONSISTENT). CBX MLI designation; region_fraction_100um: 0.841
    (lower_bound rollup). No annotation-transfer evidence available; confidence capped
    at MODERATE. Classical node spans both MLI1 and MLI2; this cluster is proposed
    as the MLI1-arm mapping.
  reconciliation_note: >
    This edge covers the MLI1 (Sorcs3-high) arm of the joint MLI1/MLI2 classical node.
    The MLI2 arm is mapped separately to CS20230722_SUPT_1151 (1151 CBX MLI Cdh22 Gaba_1).
    The two edges together are proposed to cover the joint classical node. The supertype
    1149 CBX MLI Megf11 Gaba_1 (parent of CS20230722_CLUS_5188 and CS20230722_CLUS_5189)
    is not a current graph edge; adding a supertype-level edge at rank 1 is a proposed
    follow-up.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal is driven by a lower_bound rollup row — non-painted CCF2020
        descendants are present and uncounted. region_fraction_100um value of 0.841 is
        a floor; true cerebellar fraction may be higher.
    - caveat_type: SINGLE_DATASET
      description: >
        No annotation transfer evidence is available. Confidence is capped at MODERATE
        in the absence of direct cell-level experimental mapping.
  proposed_experiments:
    - >
      Run annotation transfer on a source cerebellar dataset with class-resolved
      MLI1 / MLI2 labels (distinguished by Sorcs3 vs. Nxph1 expression). Map to
      WMBv1 (CCN20230722) at cluster and supertype level. Target F1 ≥ 0.70 at cluster
      level for the MLI1 source group. Add result as AnnotationTransferEvidence.
    - >
      Literature search linking the Megf11-expressing CBX MLI cluster lineage to
      the Sorcs3+ (class I / MLI1) transcriptomic class. Add result as LiteratureEvidence.
  unresolved_questions:
    - >
      Does the supertype 1149 CBX MLI Megf11 Gaba_1 (parent of CS20230722_CLUS_5188
      and CS20230722_CLUS_5189) specifically capture the MLI1 population? A supertype-level
      edge (rank 1) is absent from the current graph and should be emitted.
    - >
      The classical node spans both MLI1 and MLI2; confirm whether the Megf11
      designation in the atlas cluster name is a known discriminator between the two
      classes before elevating confidence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1151 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.48
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Atlas metadata CONSISTENT for Nxph1 (mean 11.40; cohort pct 0.982;
    child-coverage 1.000; EXPRESSION source) and Pvalb (mean 11.33; cohort pct 0.991;
    child-coverage 1.000; atlas category DEFINING on sibling SUPT_1150); Sorcs3
    APPROXIMATE (mean 0.81; cohort pct 0.236) — expected low for MLI2/class II.
    3 of 4 markers CONSISTENT. CBX MLI designation; region_fraction_100um: 0.851
    (lower_bound). NT annotation absent at supertype level (NOT_ASSESSED). No
    annotation-transfer evidence available; confidence capped at MODERATE.
  reconciliation_note: >
    This edge covers the MLI2 (Nxph1-high, Pvalb-high) arm of the joint MLI1/MLI2
    classical node. The MLI1 arm is mapped separately to CS20230722_CLUS_5188.
    Together these two candidates are proposed to partition the joint classical node
    across the two transcriptomic classes. NT gap at this supertype should be
    resolved against atlas provenance.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal is driven by a lower_bound rollup row — non-painted CCF2020
        descendants are present and uncounted. region_fraction_100um value of 0.851 is
        a floor.
    - caveat_type: SINGLE_DATASET
      description: >
        No annotation transfer evidence is available. NT annotation is absent at
        this supertype level. Confidence is capped at MODERATE.
  proposed_experiments:
    - >
      Run annotation transfer on a source dataset with Nxph1-high (MLI2 / class II) cells
      from cerebellar cortex. Map to WMBv1 (CCN20230722) at supertype level.
      Target F1 ≥ 0.70. Add result as AnnotationTransferEvidence.
    - >
      Confirm GABAergic NT annotation at supertype CS20230722_SUPT_1151 via atlas
      provenance query. Add result as atlas metadata note.
  unresolved_questions:
    - >
      NT annotation is absent at 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151].
      Is this a database completeness gap or does the atlas genuinely lack NT assertion
      at this node?
    - >
      Is the Cdh22 marker in the supertype name a confirmed discriminator between
      the MLI1 and MLI2 classes? Literature search needed to anchor this.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5189 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.28
  rationale: >
    [tier:CUT] All 3 markers CONSISTENT on cluster 5189 CBX MLI Megf11 Gaba_1
    (Sorcs3 CONSISTENT, Nxph1 CONSISTENT, Pvalb CONSISTENT) but n_cells=154 is very small
    relative to sibling CS20230722_CLUS_5188 (n=31,095) in the same supertype 1149
    CBX MLI Megf11 Gaba_1. Evidence base is identical in type (ATLAS_METADATA only)
    and the larger sibling cluster is the preferred primary candidate.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1150 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] Pvalb CONSISTENT (mean 10.71; DEFINING atlas category); Sorcs3
    CONSISTENT (mean 4.58; pct 0.509); Nxph1 APPROXIMATE (mean 5.66; pct 0.482;
    child-coverage 1.000). Region CONSISTENT (region_fraction_100um: 0.865). CBX MLI
    designation. However Nxph1 APPROXIMATE and the small cell count (n=370) compared
    to primary candidate; NT annotation missing. Eliminated in favour of SUPT_1151
    which has stronger Nxph1 and larger n_cells for the MLI2-arm placement.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5178 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.20
  rationale: >
    [tier:CUT] CB PLI (Purkinje layer interneuron) designation — not a molecular layer
    interneuron cluster. Sorcs3 APPROXIMATE (mean 0.64; pct 0.326). NT CONSISTENT (GABA).
    Region CONSISTENT (region_fraction_100um: 0.768) but PLI designation places this
    cluster in the Purkinje cell layer, not the molecular layer. Eliminated (wrong layer).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1144 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.18
  rationale: >
    [tier:CUT] CB PLI supertype designation — Purkinje layer, not molecular layer.
    Sorcs3 APPROXIMATE (mean 0.57; pct 0.209); NT NOT_ASSESSED. Eliminated (Purkinje
    layer interneuron supertype; wrong laminar position).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5185 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CB PLI designation — Purkinje layer. Sorcs3 mean 0.18 (cohort pct 0.065)
    — essentially absent. Although Nxph1 and Pvalb are CONSISTENT, the Sorcs3 absence
    and PLI designation make this an unlikely MLI mapping. Eliminated (Purkinje layer;
    Sorcs3 absent).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1147 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.13
  rationale: >
    [tier:CUT] CB PLI supertype. Sorcs3 mean 0.18 (pct 0.027) — absent. NT NOT_ASSESSED.
    Same reasoning as cluster 5185 CB PLI Gly-Gaba_4 [CS20230722_CLUS_5185].
    Eliminated (Purkinje layer; Sorcs3 absent).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_4707 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] LDT (lateral dorsal tegmentum) designation — not a cerebellar interneuron.
    Top anatomical label in atlas: Pons [MBA:771] (count_100um=39); Cerebellum
    [MBA:512] (count_100um=38). Region signal is split between brainstem and
    cerebellum. Pvalb APPROXIMATE (mean 0.11; pct 0.255). Eliminated (wrong region —
    lateral dorsal tegmentum).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1157 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] "Bergmann NN_1" — Bergmann glia, not a GABAergic interneuron. Nxph1
    APPROXIMATE (mean 0.59; pct 0.218); Pvalb mean 1.44 only pct 0.700; Sorcs3
    APPROXIMATE (mean 0.53; pct 0.200). NT NOT_ASSESSED (glia, not neuron). Eliminated
    (Bergmann glia — wrong cell class).
```
<!-- verdict-block-end -->
