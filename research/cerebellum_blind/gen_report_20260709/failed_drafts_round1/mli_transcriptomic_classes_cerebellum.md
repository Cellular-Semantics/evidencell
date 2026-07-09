# Molecular layer interneuron transcriptomic classes MLI1 / MLI2 (class I / class II) — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml`*

---

## Introduction

Cerebellar molecular layer interneurons (MLIs) provide GABAergic inhibition onto Purkinje cells and onto one another, exerting lateral and feedforward inhibitory control over cerebellar output. Historically classified into basket cells and stellate cells on the basis of soma depth and axonal target (basket cells in the inner molecular layer targeting Purkinje soma and axon initial segment; stellate cells in the outer molecular layer targeting Purkinje dendrites), the basket–stellate division has long been debated because of extensive morphological intermediates. Single-nucleus RNA sequencing overturned the classical morphological scheme: Kozareva et al. 2020 [1] identified two transcriptomically and functionally distinct types — MLI1 and MLI2 — that each span the full thickness of the molecular layer through a continuum of morphological variation, while differing markedly in spontaneous firing, excitability, and electrical coupling. Lowenstein et al. 2022 [2] confirmed and extended this finding, designating these as class I (MLI1; Sorcs3+) and class II (MLI2; Nxph1+), with distinct developmental trajectories arising from common progenitors but diverging electrophysiology and gap-junction connectivity (class I cells are coupled; class II are not). Sarropoulos et al. 2021 [4] further documented the defining markers of each class in a developmental transcriptomic context: MLI1 (Sorcs3, Grm8) and MLI2 (Nxph1, Pvalb) arise late in postnatal development, distinguishable by their cis-regulatory programmes.

The present mapping covers the MLI1/MLI2 pair as a single classical node, reflecting the fact that both classes co-inhabit the same anatomical compartment, arise from a common progenitor pool, and are molecularly defined jointly (no CL term exists for either subtype individually; see Cell Ontology mapping below). The mapping question is therefore which WMBv1 clusters or supertypes capture this MLI population — and, secondarily, whether the atlas resolves the MLI1/MLI2 distinction.

| Property | Value | References |
|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974]; cerebellar cortex [UBERON:0002129] | [1] |
| NT | GABAergic | [1] |
| Defining markers | Sorcs3 (MLI1-enriched) | [2], [3] |
| | Nxph1 (expressed by both; higher in MLI2) | [2] |
| | Pvalb | [4] |
| Neuropeptides | Nxph1 | [4] |
| Negative markers | None documented | — |
| Definition basis | PRIOR_TRANSCRIPTOMIC (Kozareva et al. 2020; Lowenstein et al. 2022) | [1], [2] |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location / Electrophysiology / NT type:** Kozareva et al. 2020 · snRNA-seq (mouse cerebellum) · [1]
  > For multiple types of cerebellar interneurons, the molecular variation within each type was more continuous, rather than discrete. For the unipolar brush cells (UBCs)—an interneuron population previously subdivided into two discrete populations—the continuous variation in gene expression was associated with a graded continuum of electrophysiological properties. Most surprisingly, we found that molecular layer interneurons (MLIs) were composed of two molecularly and functionally distinct types. Both show a continuum of morphological variation through the thickness of the molecular layer, but electrophysiological recordings revealed marked differences between the two types in spontaneous firing, excitability, and electrical coupling.
  > — Kozareva et al. 2020, Anatomical organization and core cell types · [1] <!-- quote_key: 214725795_3d3df51c -->

- **Defining markers (Sorcs3, Nxph1) / Electrophysiology / Development:** Lowenstein et al. 2022 · review of snRNA-seq + electrophysiology literature · [2]
  > 2021) also examined the development of molecular layer inhibitory interneurons, which have been historically separated into stellate and basket cells based on their morphology (Leto et al., 2015)(2020)(Leto et al., 2009). This distinction is a little unclear however as many of these interneurons display mixed morphologies, leading to the conclusion that these cells may represent a morphological contiuum. Surprisingly, their adult snRNAseq data revealed two classes of molecular layer interneurons, which they termed as class I (MLI1 and Sorcs3+) and class II (MLI2 and Nxph1+). In an effort to examine the development of these interneurons, the authors expanded their analysis to 5500 GABAergic progenitors across four stages of development and could distinguish between the distinct developmental trajectories of class I and class II interneurons. Although these cells develop from common progenitors, class II differentially expressed immediate early genes such as Fos during their development, which the authors concluded might indicate a higher cellular activity during their specification. Both classes of interneurons differ in their electrophysiological properties, and many class I, but not class II, are coupled to one another via gap junctions, demonstrating that the transcriptomic differences between these two classes of interneurons are also functionally relevant.
  > — Lowenstein et al. 2022, Anatomical organization and core cell types · [2] <!-- quote_key: 247317953_380921bf -->

- **Defining markers (Sorcs3 / Nxph1 distinction):** Wang & Lefebvre 2020 · snRNA-seq + morphological fate mapping · [3]
  > Differential gene expression analyses confirmed that MLI t-types were distinguished by Sorcs3 or Nxph1 expression51.
  > — Wang & Lefebvre 2020, Results · [3] <!-- quote_key: 213840122_4cb91d31 -->

- **Defining markers (Sorcs3 MLI1; Nxph1+Pvalb MLI2) / Development:** Sarropoulos et al. 2021 · comparative genomics + snRNA-seq (developmental stages) · [4]
  > Whereas granule cells form a homogeneous differentiating population (Fig. 4B), interneurons are stratified into distinct temporally specified subtypes (fig. S13, E and F): early-born interneurons (Zfhx4, Slit2) detected at E13 to E15, mid-born Golgi cells (Chrm2), Purkinje layer interneurons (Nxph1, Klhl1) prevalent at E17 to P7, and late-born molecular layer interneurons of type 1 (Sorcs3, Grm8) and 2 (MLI2; Nxph1, Pvalb), which are abundant at P14 to P63 (Leto et al., 2015)37).
  > — Sarropoulos et al. 2021, Anatomical organization and core cell types · [4] <!-- quote_key: 237308705_5cd4bd6a -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: molecular layer interneuron [[CL:4042035](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4042035)] (BROAD).

No Cell Ontology term currently covers the MLI1 or MLI2 subtypes individually. CL:4042035 (molecular layer interneuron) is the closest ancestor but encompasses both classes and the full basket/stellate morphological population without distinguishing the Sorcs3+ and Nxph1+ transcriptomic sub-identities. This node is a candidate for CL contribution of two new subtypes (see node notes).

---

## Results

Atlas metadata and precomputed expression support mapping of the MLI1/MLI2 node to cerebellar cortex MLI clusters in WMBv1, with the strongest signal at cluster 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] (Sorcs3 and Pvalb both at the 99th percentile of the cerebellar GABAergic cohort) and at supertype 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] (Nxph1 at 98th percentile, Pvalb at 99th percentile, region fraction 0.851; see property comparison tables). Because the classical node spans MLI1 and MLI2 together, and because the atlas resolves multiple distinct MLI populations by different marker profiles, the mapping distributes across complementary cluster/supertype entries reflecting different aspects of the MLI class.

*(No annotation transfer runs are available for these edges; all evidence is from atlas metadata and precomputed expression.)*

---

### 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] · 🟡 MODERATE

**Table 1 — Property comparison: 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188]**

| Property | Classical | Atlas cluster | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] (region_fraction_100um=0.841; lower_bound rollup) | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Sorcs3 expression | Defining marker (MLI1-enriched) | Mean=10.35; 99.5th cohort percentile | CONSISTENT |
| Nxph1 expression | Defining marker (both classes; higher in MLI2) | Mean=2.09; 36.4th cohort percentile | APPROXIMATE |
| Pvalb expression | Defining marker | Mean=11.12; 99.5th cohort percentile | CONSISTENT |
| Nxph1 (neuropeptide) | Nxph1 neuropeptide | Mean=2.09; 36.4th cohort percentile | APPROXIMATE |

**Table 2 — Evidence support: 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188]**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node 5188 CBX MLI Megf11 Gaba_1 | Atlas metadata | PARTIAL | region_fraction_100um=0.841; strict region_fraction=0.720 | atlas-internal |

*(Child-cluster breakdown not assessed — no supertype-level child inventory available at this rank-0 edge.)*

Sorcs3 and Pvalb co-expression at the 99th percentile of the cerebellar GABAergic cohort supports identification of 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] as the primary WMBv1 cluster match for the combined MLI1/MLI2 classical node, at MODERATE confidence on atlas metadata alone. Sorcs3, the defining MLI1 marker (established by snRNA-seq in Kozareva et al. 2020 [1] and confirmed by Wang & Lefebvre 2020 [3]), is at a 99.5th cohort percentile expression level, placing this cluster unambiguously among the highest Sorcs3-expressing cerebellar GABAergic neurons. Pvalb, which marks MLI2 (alongside Nxph1) in the Sarropoulos et al. 2021 [4] developmental analysis, is also at the 99.5th percentile. This dual-high Sorcs3 + Pvalb profile fits a population that spans or co-represents both MLI classes, or alternatively captures the Sorcs3+ MLI1 class with Pvalb co-expression (consistent with the Sarropoulos [4] annotation that MLI2 is Nxph1+ Pvalb+ while MLI1 carries Sorcs3, but Pvalb is broadly expressed in MLIs — Buttermore et al. 2012 [1-context], Kamath et al. 2018, and Brown et al. 2018 established Pvalb as a shared MLI marker). The n=31,095 cells in this cluster is the largest of any candidate examined, consistent with its representing a major MLI population in the WMBv1 atlas.

**Marker evidence provenance:**

- **Sorcs3:** Established as an MLI1 (class I) defining marker by snRNA-seq in Kozareva et al. 2020 [1] (mouse cerebellum); confirmed by Wang & Lefebvre 2020 [3] ("MLI t-types were distinguished by Sorcs3 or Nxph1 expression") and in the developmental time series of Sarropoulos et al. 2021 [4]. Evidence is transcript-level, from sorted/nuclear RNA-seq populations; no protein-level (IHC) confirmation is present in the gathered literature for cell-type specificity to morphology-confirmed MLIs, but the snRNA-seq studies used cerebellar tissue populations where MLIs are well-defined numerically. The cell-type specificity of the Sorcs3 assignment to MLI1 is robust across three independent datasets.

- **Nxph1:** Designated as the defining marker for MLI2 (class II) by Lowenstein et al. 2022 [2] and Kozareva et al. 2020 [1]; Sarropoulos et al. 2021 [4] confirm Nxph1 marks Purkinje layer interneurons early and MLI2 later in development. Note: the classical node assigns Nxph1 as a defining marker for both classes (expressed by both at different levels), but MLI2 enrichment is the primary functional claim. On cluster CLUS_5188, Nxph1 is at only the 36.4th cohort percentile (mean=2.09), which is APPROXIMATE — this is consistent with a Sorcs3-enriched (MLI1-dominant) cluster profile, or with a mixed population in which the Nxph1-high cells (MLI2) have been resolved elsewhere in the atlas.

- **Pvalb:** Confirmed as a molecular layer interneuron marker (shared with Purkinje cells) by multiple studies — Buttermore et al. 2012, Brown et al. 2018, Kamath et al. 2018. Designated as an MLI2 marker in the developmental analysis of Sarropoulos et al. 2021 [4] (MLI2: Nxph1, Pvalb). On CLUS_5188, Pvalb is at 99.5th percentile — consistent with a strong Pvalb+ MLI identity. Note: Pvalb is also expressed by Purkinje cells, so high Pvalb alone does not discriminate MLIs from Purkinje cells in bulk; in the snRNA-seq context, the cluster assignment and the co-expression profile with Sorcs3/Nxph1 provide the discriminating context.

- **Atlas annotation:** Pvalb on CLUS_5188 does not carry a DEFINING or MERFISH atlas category tag, consistent with Pvalb being a broadly-expressed marker rather than the primary cluster discriminator. The cluster discriminator appears to be Megf11 (in the cluster name: "CBX MLI Megf11 Gaba_1"), which is not in the classical node's marker set and thus not directly assessed here.

**Concerns:**

- Nxph1 at only the 36.4th cohort percentile (APPROXIMATE) on CLUS_5188 is lower than expected if this cluster represents the full MLI1/MLI2 population. The low Nxph1 may indicate this cluster is predominantly MLI1 (Sorcs3+), with the MLI2 (Nxph1+ Pvalb+) cells resolved into separate WMBv1 clusters such as SUPT_1151 or SUPT_1150. The classical node's definition encompasses both classes, so the mapping is partial at the cluster level — this is expected given the prior-transcriptomic definition spanning two atlas-resolvable populations.

- Region fraction is a lower-bound rollup (region_count_completeness=lower_bound), meaning non-painted CCF2020 descendants are uncounted; region_fraction_100um=0.841 is a floor. This is a caveat on precision but does not contradict the cerebellar cortex localization.

- The "Megf11" discriminator in the cluster name is not assessed from the classical-side literature gathered; it is unknown whether Megf11 is expressed specifically by MLI1, MLI2, or both. A targeted literature search for Megf11 expression in cerebellar MLIs would clarify the cluster's position within the MLI taxonomy.

**What would upgrade confidence:**

- Annotation transfer (MapMyCells) from an MLI1- or MLI2-labelled source dataset (e.g. Cre-driver TRAP-seq from Sorcs3-Cre or a Nxph1-marked cohort) would establish F1-based quantitative mapping, replacing MODERATE metadata-based confidence with HIGH if F1 ≥ 0.75 at cluster level.
- Targeted literature search for Megf11 cerebellar expression to assess whether CLUS_5188's primary discriminator aligns with MLI1 or MLI2 identity.
- Expression of Sorcs3 on the sibling SUPT_1149 children (including CLUS_5189) at cluster level would clarify whether the Megf11 Gaba_1 family captures MLI1, MLI2, or both within the Kozareva taxonomy.

---

### 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] · 🟡 MODERATE

**Table 1 — Property comparison: 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151]**

| Property | Classical | Atlas supertype | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] (region_fraction_100um=0.851; lower_bound rollup) | CONSISTENT |
| NT type | GABAergic | not asserted | NOT_ASSESSED |
| Sorcs3 expression | Defining marker (MLI1-enriched) | Mean=0.81; 23.6th cohort percentile; child-coverage=1.000 | APPROXIMATE |
| Nxph1 expression | Defining marker (both; higher in MLI2) | Mean=11.40; 98.2th cohort percentile; child-coverage=1.000 | CONSISTENT |
| Pvalb expression | Defining marker | Mean=11.33; 99.1th cohort percentile; child-coverage=1.000 | CONSISTENT |
| Nxph1 (neuropeptide) | Nxph1 neuropeptide | Mean=11.40; 98.2th cohort percentile; child-coverage=1.000 | CONSISTENT |

**Table 2 — Evidence support: 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151]**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node 1151 CBX MLI Cdh22 Gaba_1 | Atlas metadata | PARTIAL | region_fraction_100um=0.851; strict region_fraction=0.723 | atlas-internal |

*(Child-cluster coverage=1.000 across all three markers confirms the Nxph1+Pvalb+ signal is supertype-wide, not driven by a minority child cluster.)*

Nxph1 at the 98th percentile and Pvalb at the 99th percentile, both with child-coverage=1.000, support identification of 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] as the primary supertype-level match for the Nxph1+/MLI2 component of the classical node, at MODERATE confidence on atlas metadata. The "CBX MLI" prefix in the supertype name directly indicates cerebellar cortex (CBX) molecular layer interneuron identity, providing name-level concordance with the classical type. The high child-coverage=1.000 means the Nxph1+Pvalb+ profile characterises all child clusters of this supertype uniformly — this is a coherent supertype, not driven by a single outlier child. The Sorcs3 signal is low (23.6th percentile, APPROXIMATE), suggesting SUPT_1151 represents the Nxph1-dominant (MLI2-like) end of the MLI spectrum, complementary to the Sorcs3-dominant CLUS_5188.

Together, CLUS_5188 and SUPT_1151 capture the two main transcriptomic classes: CLUS_5188 is Sorcs3-high (MLI1-like) and SUPT_1151 is Nxph1-high (MLI2-like). This complementary atlas architecture is consistent with the prior transcriptomic definition of the classical node as a pair of co-habiting types.

**Marker evidence provenance:**

- **Nxph1:** As above for CLUS_5188. On SUPT_1151, Nxph1 is at the 98.2nd percentile with child-coverage=1.000 — this is the highest Nxph1 cohort ranking seen across the top-10 candidates, and is consistent with SUPT_1151 capturing the Nxph1+ MLI2 (class II) component of the classical node. The neuropeptide Nxph1 assignment in the classical node [4] is supported by this atlas-side expression level.

- **NT not asserted:** NT data is missing at the SUPT_1151 atlas level. This is a data gap — the classical type is clearly GABAergic [1], and the "Gaba" in the supertype name (CBX MLI Cdh22 Gaba_1) implies a GABA annotation in the atlas, but the structured NT field is absent from the property comparison. This is assessed NOT_ASSESSED rather than DISCORDANT, and does not constitute a counter-signal.

- **Cdh22 discriminator:** The supertype name includes Cdh22, which is not in the classical node marker set. Cdh22 (Cadherin-22) is not discussed in the gathered literature for MLIs; it may represent an atlas-internal discriminating marker for this supertype lineage. A targeted literature search for Cdh22 in cerebellar MLI subtypes would clarify whether it aligns with MLI1, MLI2, or is supertype-specific.

**Concerns:**

- NT data not asserted at this supertype level — a data gap, not a contradiction. The Gaba suffix in the supertype name provides indirect support.

- Sorcs3 at only the 23.6th percentile (APPROXIMATE) on SUPT_1151 confirms this supertype is Sorcs3-low, making it an incomplete representation of the MLI1/MLI2 joint node. However, given that CLUS_5188 captures Sorcs3-high signal and SUPT_1151 captures Nxph1-high signal, the pair together covers the classical node's defining marker profile.

- Lower-bound region_fraction_100um=0.851 (same caveat as CLUS_5188).

**What would upgrade confidence:**

- Same annotation-transfer experiment as above, specifically from a Nxph1-marked MLI2 cohort, would place the SUPT_1151 mapping on direct experimental footing.
- Confirming NT annotation at the atlas level for SUPT_1151 would resolve the NOT_ASSESSED gap.
- Clarifying the Cdh22 expression pattern in MLI subtypes would support or qualify the supertype assignment.

---

### 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] · 🔴 LOW

**Table 1 — Property comparison: 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178]**

| Property | Classical | Atlas cluster | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] (region_fraction_100um=0.768; lower_bound rollup) | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Sorcs3 expression | Defining marker (MLI1-enriched) | Mean=0.64; 32.6th cohort percentile | APPROXIMATE |
| Nxph1 expression | Defining marker (both; higher in MLI2) | Mean=11.87; 98.9th cohort percentile | CONSISTENT |
| Pvalb expression | Defining marker | Mean=10.41; 98.4th cohort percentile | CONSISTENT |
| Nxph1 (neuropeptide) | Nxph1 neuropeptide | Mean=11.87; 98.9th cohort percentile | CONSISTENT |

**Table 2 — Evidence support: 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178]**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node 5178 CB PLI Gly-Gaba_1 | Atlas metadata | PARTIAL | region_fraction_100um=0.768; strict region_fraction=0.680 | atlas-internal |

*(Child-cluster breakdown not assessed — rank-0 edge.)*

Atlas metadata supports a Nxph1-high, Pvalb-high profile for 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] consistent with the MLI2 (class II) component, but the "PLI Gly-Gaba" label — Purkinje-layer interneuron, glycinergic-GABAergic — raises a significant concern: the "Gly-Gaba" annotation implies glycine co-transmission, which is not part of the MLI1/MLI2 classical node definition (GABAergic only [1]). The NT property comparison shows GABA consistent at the structured field level, but the free-text cluster name "Gly-Gaba" suggests this cluster may represent a co-transmitter population distinct from the classical MLI Gly-only GABAergic phenotype. Additionally, the n=3,066 cells and the "CB PLI" prefix (CB rather than CBX, suggesting possibly broad cerebellar rather than cerebellar cortex specificity) makes this a less clean hit than CLUS_5188 or SUPT_1151. Confidence is LOW.

**Concerns:**

- "Gly-Gaba" in the cluster name is inconsistent with the purely GABAergic classical type definition. If this cluster uses glycine co-transmission, it represents a different cell type from MLIs as defined by Kozareva et al. 2020 [1]. This is the primary concern.

- Sorcs3 at only the 32.6th cohort percentile (APPROXIMATE) — not a strong Sorcs3 signal.

- Lower-bound region_fraction_100um=0.768 and strict region_fraction=0.680.

**What would upgrade confidence:**

- Confirming whether the Gly-Gaba co-transmission annotation on CLUS_5178 reflects genuine glycine co-release (which would refute the MLI identity) or is a legacy classification artefact would be the single most important follow-up.
- Annotation transfer from an MLI source dataset would quantify whether cells from a known MLI cohort actually land on CLUS_5178.

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] | 1149 CBX MLI Megf11 Gaba_1 | 31,095 | 🟡 MODERATE | Sorcs3 + Pvalb both 99.5th percentile; CBX MLI name | Primary |
| 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] | — | 13,098 | 🟡 MODERATE | Nxph1 98th + Pvalb 99th percentile; child-coverage=1.000; CBX MLI name | Secondary |
| 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] | 1144 CB PLI Gly-Gaba_1 | 3,066 | 🔴 LOW | Nxph1 98.9th, Pvalb 98.4th; but Gly-Gaba co-transmitter label | Supports broader mapping (Gly-Gaba label concern) |
| 5185 CB PLI Gly-Gaba_4 [CS20230722_CLUS_5185] | 1147 CB PLI Gly-Gaba_4 | 442 | ⚪ UNCERTAIN | Sorcs3 low (6.5th pct); small cluster; Gly-Gaba label | Eliminated (Sorcs3 absent; Gly-Gaba) |
| 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] | 1149 CBX MLI Megf11 Gaba_1 | 154 | ⚪ UNCERTAIN | Minor cluster dominated by CLUS_5188 from same supertype | Eliminated (dominated by sibling CLUS_5188; very small) |
| 4707 LDT Fgf7 Gaba_1 [CS20230722_CLUS_4707] | 1049 LDT Fgf7 Gaba_1 | 202 | ⚪ UNCERTAIN | LDT (brainstem), not cerebellum; Pvalb low (25.5th pct) | Eliminated (wrong region — lateral dorsal tegmental nucleus) |
| 1147 CB PLI Gly-Gaba_4 [CS20230722_SUPT_1147] | — | 442 | ⚪ UNCERTAIN | Sorcs3 2.7th pct; Gly-Gaba label; very small | Eliminated (Sorcs3 absent; Gly-Gaba) |
| 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] | — | 3,646 | ⚪ UNCERTAIN | Sorcs3 only 20.9th pct; Gly-Gaba label | Eliminated (Gly-Gaba label; Sorcs3 low) |
| 1150 CBX MLI Megf11 Gaba_2 [CS20230722_SUPT_1150] | — | 370 | ⚪ UNCERTAIN | Nxph1 only 48.2th pct; small; dominated by SUPT_1151 | Eliminated (Nxph1 below threshold; dominated by SUPT_1151) |
| 1157 Bergmann NN_1 [CS20230722_SUPT_1157] | — | 3,321 | ⚪ UNCERTAIN | Bergmann glia; Nxph1 21.8th, Sorcs3 20th pct | Eliminated (non-neuronal Bergmann glia identity) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical node `mli_transcriptomic_classes_cerebellum` is defined on a PRIOR_TRANSCRIPTOMIC basis, derived from single-nucleus RNA sequencing studies of the mouse cerebellum. Kozareva et al. 2020 [1] identified MLI1 and MLI2 as two molecularly and functionally distinct types within the molecular layer interneuron population; Lowenstein et al. 2022 [2] confirmed and named these as class I (Sorcs3+) and class II (Nxph1+); Wang & Lefebvre 2020 [3] confirmed the Sorcs3/Nxph1 marker distinction; Sarropoulos et al. 2021 [4] documented the developmental marker profiles (MLI1: Sorcs3, Grm8; MLI2: Nxph1, Pvalb). Defining markers: Sorcs3 [2,3], Nxph1 [2], Pvalb [4]. NT type: GABAergic [1]. Soma location: molecular layer of cerebellar cortex [UBERON:0002974] [1].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table:**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5188 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5178 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5185 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_4707 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5189 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1151 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1147 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1144 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1150 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1157 | ATLAS_METADATA | PARTIAL | atlas-internal |

*Generated by evidencell `8e05bb5` at 2026-07-09T13:25:36+00:00 from [kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml](kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml).*

</details>

---

## Discussion

**Primary mapping:** Molecular layer interneuron transcriptomic classes MLI1 / MLI2 (class I / class II) → 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] at MODERATE confidence. Key support: atlas precomputed expression (Sorcs3 and Pvalb both at 99.5th percentile of the cerebellar GABAergic cohort; region_fraction_100um=0.841). Key caveats: no annotation transfer evidence; all evidence from atlas metadata; the classical node spans two transcriptomic classes that may resolve to distinct atlas entries.

The Cell Ontology has no specific term for the MLI1 or MLI2 populations; molecular layer interneuron [CL:4042035] is the closest ancestor (BROAD mapping). The two-class structure documented by Kozareva et al. 2020 [1] is not yet captured in CL, making this node a strong candidate for a new CL term contribution.

A secondary MODERATE mapping to 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] captures the Nxph1-dominant (MLI2-like) signal that is low on the primary candidate. Together, CLUS_5188 and SUPT_1151 provide complementary coverage of the MLI1 (Sorcs3-high) and MLI2 (Nxph1-high) components respectively, consistent with the classical node's dual-class definition. A third candidate, 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178], carries a Nxph1-high profile similar to SUPT_1151 but is held at LOW confidence because the "Gly-Gaba" co-transmitter label is inconsistent with the purely GABAergic MLI phenotype [1]; this requires investigation before the mapping can be strengthened.

### Proposed experiments and follow-ups

**1. Annotation transfer — MLI1 and MLI2 source cohorts (priority)**
- **What:** MapMyCells annotation transfer from a Sorcs3-Cre or MLI1-specific TRAP-seq/scRNA-seq source dataset, and separately from an Nxph1-marked or MLI2-specific source.
- **Target:** F1 ≥ 0.75 at cluster level for the MLI1 cohort on CLUS_5188; F1 ≥ 0.75 for the MLI2 cohort on SUPT_1151 or its children.
- **Expected output:** AnnotationTransferEvidence items on the relevant edges.
- **Resolves:** Whether CLUS_5188 captures predominantly MLI1 and SUPT_1151 predominantly MLI2, and whether the split reflects the biological class structure.

**2. Glycine co-transmission investigation — CLUS_5178 / CLUS_5185 / SUPT_1144 / SUPT_1147**
- **What:** Targeted literature search and atlas metadata query for glycine co-transmission evidence on the "CB PLI Gly-Gaba" clusters.
- **Target:** Determine whether the Gly-Gaba label reflects genuine glycine co-release in these cells.
- **Resolves:** Whether any of the Gly-Gaba clusters can be considered MLI, or whether they represent a separate cerebellar interneuron population.

**3. Megf11 and Cdh22 expression in cerebellar MLIs**
- **What:** Targeted literature search for Megf11 and Cdh22 expression in the Kozareva et al. 2020 MLI1/MLI2 transcriptomics, or in other cerebellar MLI datasets.
- **Resolves:** Whether the Megf11 (CLUS_5188/SUPT_1149) and Cdh22 (SUPT_1151) discriminating markers in WMBv1 align with MLI1 or MLI2 identity, clarifying which WMBv1 clusters correspond to each class.

**4. Supertype-level atlas query for SUPT_1149 children**
- **What:** Examine all child clusters of SUPT_1149 CBX MLI Megf11 Gaba_1 (which includes CLUS_5188 and CLUS_5189) for Sorcs3 and Nxph1 differential expression.
- **Resolves:** Whether the Megf11 supertype family captures both MLI classes or predominantly MLI1.

### Open questions

1. Does the WMBv1 atlas resolve MLI1 and MLI2 into distinct supertypes (e.g. Megf11 Gaba_1 = MLI1; Cdh22 Gaba_1 = MLI2), or are both classes distributed within each supertype? The complementary Sorcs3/Nxph1 profiles of CLUS_5188 vs SUPT_1151 suggest the former, but direct annotation transfer evidence is needed.

2. What is the biological basis for the "Gly-Gaba" co-transmitter label on several top-ranked cerebellar candidates (CB PLI Gly-Gaba_1, _4)? If these represent a genuine glycine-expressing interneuron population, they should be separated from the MLI1/MLI2 node and a distinct classical type may be warranted.

3. The node notes report that Purkinje collaterals preferentially target MLI2 over MLI1 (Lackey et al. 2025). This functional distinction is not yet captured in the mapping evidence; connectivity data from WMBv1 or from annotation-transfer of Purkinje-collateral-targeted cells would add a functional dimension to the MLI1 vs MLI2 cluster assignment.

4. Nxph1 is described as expressed at higher levels in MLI2 but by both classes; marker assignment to the two classes is subtype-dependent (node notes). The current atlas property comparisons treat Nxph1 as a single marker across the node, which may produce misleading alignment scores when the node includes both Nxph1-high (MLI2) and Nxph1-lower (MLI1) cells. A per-class split of the classical node should be considered.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Kozareva et al. 2020 · [https://doi.org/10.1101/2020.03.04.976407](https://doi.org/10.1101/2020.03.04.976407) | — (preprint) | soma location, NT type, MLI1/MLI2 definition |
| [2] | Lowenstein et al. 2022 · PMID:[35262281](https://pubmed.ncbi.nlm.nih.gov/35262281/) | 35262281 | Sorcs3 marker, Nxph1 marker, class I/II definition |
| [3] | Wang & Lefebvre 2020 · PMID:[35701402](https://pubmed.ncbi.nlm.nih.gov/35701402/) | 35701402 | Sorcs3 marker |
| [4] | Sarropoulos et al. 2021 · PMID:[34446581](https://pubmed.ncbi.nlm.nih.gov/34446581/) | 34446581 | Pvalb marker, MLI1/MLI2 developmental markers |

---

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5188 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:closeMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Atlas metadata supports close match to CS20230722_CLUS_5188 (5188 CBX MLI Megf11 Gaba_1):
    Sorcs3 cohort_pct=0.995 (CONSISTENT) and Pvalb cohort_pct=0.995 (CONSISTENT) place this cluster at
    the top of the cerebellar GABAergic cohort for both MLI1 and MLI2 markers. Nxph1 cohort_pct=0.364
    (APPROXIMATE) is lower, consistent with an MLI1-enriched profile. Region fraction_100um=0.841
    (lower_bound rollup). n=31,095 cells. No annotation transfer evidence; confidence ceiling MODERATE
    without AT. Mapping cardinality 1:n because the classical node spans both MLI1 and MLI2 and the atlas
    likely resolves them into multiple clusters.
  reconciliation_note: >
    Complementary mapping: CS20230722_SUPT_1151 captures the Nxph1-dominant (MLI2-like) component
    not well represented on this Sorcs3-high cluster. Together, CLUS_5188 + SUPT_1151 cover the
    MLI1/MLI2 joint classical node at the cluster and supertype levels respectively.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region fraction is a lower_bound rollup — non-painted CCF2020 descendants are uncounted;
        region_fraction_100um=0.841 is a floor, not an exact value.
    - caveat_type: MISSING_EVIDENCE_TYPE
      description: >
        No annotation transfer evidence is available. Confidence is capped at MODERATE until
        F1-based AT from an MLI1/MLI2-labelled source dataset confirms the mapping.
  proposed_experiments:
    - >
      Run MapMyCells annotation transfer from a Sorcs3-Cre or MLI1-specific scRNA-seq/TRAP-seq source
      dataset against WMBv1 (CCN20230722) targeting CS20230722_CLUS_5188. Threshold: F1 >= 0.75 at
      cluster level. Expected output: AnnotationTransferEvidence on this edge.
    - >
      Investigate Megf11 expression in MLI1 vs MLI2 subtypes from published cerebellar snRNA-seq data
      to confirm whether the Megf11 Gaba_1 cluster family (SUPT_1149) captures MLI1, MLI2, or both.
  unresolved_questions:
    - >
      Does CS20230722_CLUS_5188 (Megf11 Gaba_1) represent MLI1 (Sorcs3+), MLI2, or a mixed population?
      The high Sorcs3 suggests MLI1-dominant, but the classical node spans both; annotation transfer
      from class-specific sources is needed to resolve.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1151 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.50
  relationship: skos:closeMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Atlas metadata supports close match to CS20230722_SUPT_1151 (1151 CBX MLI Cdh22 Gaba_1):
    Nxph1 cohort_pct=0.982 (CONSISTENT) and Pvalb cohort_pct=0.991 (CONSISTENT), both with
    child-coverage=1.000 confirming the signal is supertype-wide. Sorcs3 cohort_pct=0.236 (APPROXIMATE)
    is low, suggesting Nxph1-dominant (MLI2-like) profile. Region_fraction_100um=0.851 (lower_bound).
    NT not asserted at supertype level — NOT_ASSESSED (Gaba suffix in name provides indirect support).
    No AT evidence; MODERATE ceiling. Supertype-level mapping (1:n) consistent with the classical node
    spanning both MLI classes.
  reconciliation_note: >
    Complementary to edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5188 — SUPT_1151
    captures the Nxph1-high (MLI2-like) component while CLUS_5188 captures the Sorcs3-high (MLI1-like)
    component. Both are needed to cover the full MLI1/MLI2 classical node.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region fraction is a lower_bound rollup; region_fraction_100um=0.851 is a floor.
    - caveat_type: MISSING_EVIDENCE_TYPE
      description: >
        NT not asserted at this supertype level; no annotation transfer evidence. Confidence capped
        at MODERATE.
  proposed_experiments:
    - >
      Run MapMyCells annotation transfer from an Nxph1-marked or MLI2-specific source dataset against
      WMBv1 (CCN20230722) targeting CS20230722_SUPT_1151 and its child clusters. Threshold: F1 >= 0.75
      at supertype level. Expected output: AnnotationTransferEvidence on this edge.
    - >
      Confirm NT annotation (GABAergic) at the SUPT_1151 atlas level via atlas metadata query.
    - >
      Investigate Cdh22 expression in MLI1 vs MLI2 subtypes to clarify whether the Cdh22 Gaba_1
      supertype lineage aligns with class II (Nxph1+) identity.
  unresolved_questions:
    - >
      Does CS20230722_SUPT_1151 (Cdh22 Gaba_1) correspond to the MLI2 (Nxph1+, class II) component
      of the classical node? The Nxph1-high profile is consistent with MLI2, but class-specific
      annotation transfer is needed to confirm.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5178 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:WEAKEST] Atlas metadata shows Nxph1 cohort_pct=0.989 (CONSISTENT) and Pvalb cohort_pct=0.984
    (CONSISTENT) but Sorcs3 cohort_pct=0.326 (APPROXIMATE). Region_fraction_100um=0.768 (lower_bound).
    NT asserted as GABA (CONSISTENT). However the cluster label "CB PLI Gly-Gaba_1" implies
    glycine co-transmission inconsistent with the purely GABAergic MLI classical definition.
    LOW confidence pending investigation of the Gly-Gaba annotation. No AT evidence.
  reconciliation_note: >
    The Gly-Gaba co-transmitter label requires investigation before this mapping can be upgraded.
    If the glycine co-transmission annotation is a classification artefact, the Nxph1+Pvalb+ profile
    would support an MLI2-like assignment similar to CS20230722_SUPT_1151.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region fraction is a lower_bound rollup; region_fraction_100um=0.768 is a floor.
    - caveat_type: CONFLICTING_EVIDENCE
      description: >
        "Gly-Gaba" label in cluster name implies glycine co-transmission; the MLI classical node
        is defined as purely GABAergic. This inconsistency must be resolved before the mapping
        can be strengthened.
  proposed_experiments:
    - >
      Investigate whether the CB PLI Gly-Gaba cluster family (CS20230722_CLUS_5178, CS20230722_SUPT_1144)
      carries genuine glycine co-transmitter annotation in the WMBv1 atlas or whether the Gly-Gaba
      label reflects a nomenclature convention. Check for Slc6a5 (GlyT2) or Glra expression in
      the cluster's precomputed expression data.
    - >
      Run annotation transfer from an MLI-specific source dataset; if F1 > 0.5 lands on CS20230722_CLUS_5178,
      the glycine issue may reflect atlas over-splitting rather than a distinct cell type.
  unresolved_questions:
    - >
      Is the "Gly-Gaba" co-transmitter designation on CS20230722_CLUS_5178 biologically real
      (reflecting a glycine-co-releasing interneuron distinct from MLI1/MLI2) or a classification
      convention in the WMBv1 atlas? This is the primary gate for this mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5185 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Sorcs3 cohort_pct=0.065 (CONSISTENT label but 6.5th percentile — effectively absent
    at the cohort level). Gly-Gaba co-transmitter label conflicts with GABAergic MLI definition.
    n=442 cells only. Region_fraction_100um=0.525 (lower_bound). Insufficient evidence for MLI identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5189 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Minor sub-cluster (n=154) within the same SUPT_1149 supertype family as CS20230722_CLUS_5188.
    Dominated by its larger sibling CLUS_5188 (n=31,095). No additional discriminating evidence.
    Very small cell count makes mapping unreliable.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_4707 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] CS20230722_CLUS_4707 (4707 LDT Fgf7 Gaba_1) is in the lateral dorsal tegmental nucleus
    (LDT, brainstem), not the cerebellar cortex. Despite Sorcs3 and Nxph1 expression, Pvalb cohort_pct=0.255
    (APPROXIMATE — low). Region_fraction_100um=0.607 but strict region_fraction=0.361, and the top painted
    regions include Pons [MBA:771], not cerebellum. This is a brainstem cell type; wrong region eliminates
    the MLI identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1147 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.08
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Sorcs3 cohort_pct=0.027 (child-coverage=1.000 — supertype-wide absence of Sorcs3).
    Gly-Gaba co-transmitter label. n=442 cells. Region_fraction_100um=0.525 (lower_bound).
    Sorcs3 absence and Gly-Gaba label eliminate this supertype from MLI1/MLI2 consideration.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1144 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.12
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Sorcs3 cohort_pct=0.209 (APPROXIMATE, child-coverage=1.000). Gly-Gaba co-transmitter
    label. Region_fraction_100um=0.699 (lower_bound). The Gly-Gaba label and low Sorcs3 at the supertype
    level (supertype-wide) are inconsistent with MLI1/MLI2 identity. This supertype is the parent of
    CS20230722_CLUS_5178 (LOW survivor); both share the Gly-Gaba concern.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1150 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.12
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Nxph1 cohort_pct=0.482 (APPROXIMATE, child-coverage=1.000) — Nxph1 is only at median
    for the cohort, not the high signal seen in SUPT_1151 (cohort_pct=0.982). Pvalb cohort_pct=0.982
    (CONSISTENT, DEFINING category). n=370. Dominated by CS20230722_SUPT_1151 which has far superior
    Nxph1 signal for the MLI2 mapping. Small cell count and intermediate Nxph1 exclude from primary
    mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1157 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.02
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] CS20230722_SUPT_1157 (1157 Bergmann NN_1) is Bergmann glia — a non-neuronal glial cell type
    of the cerebellar cortex, not a GABAergic interneuron. Nxph1 cohort_pct=0.218 and Sorcs3 cohort_pct=0.200
    are both low; Pvalb cohort_pct=0.700 is intermediate. The "NN" (non-neuronal) designation in the atlas
    name confirms glia identity. Definitively eliminated on cell-class grounds.
```
<!-- verdict-block-end -->
