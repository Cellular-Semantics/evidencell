# Molecular layer interneuron transcriptomic classes MLI1 / MLI2 (class I / class II) — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml`*

---

## Introduction

Molecular layer interneurons (MLIs) of the cerebellar cortex are GABAergic inhibitory cells residing in the molecular layer [UBERON:0002974] that provide feedforward and lateral inhibition onto Purkinje cells and onto one another. Their classical morphological subdivision into basket and stellate cells, long treated as two discrete populations, has been complicated by intermediate forms and a continuous gradient of positional and axonal characters across the molecular layer. Transcriptomic profiling of the adult mouse cerebellar cortex (Kozareva et al. 2020 [1]) revealed that the MLI population actually resolves into two molecularly and functionally distinct classes — MLI1 and MLI2 — that do not map cleanly onto the basket/stellate morphological boundary. Both classes span the full thickness of the molecular layer, but they differ in spontaneous firing rate, excitability, and electrical coupling via gap junctions. Lowenstein et al. 2022 [2] renamed these class I (MLI1; Sorcs3+) and class II (MLI2; Nxph1+/Pvalb-enriched) and showed that the two classes follow distinct developmental trajectories from common progenitors. The mapping of these transcriptomic classes to WMBv1 atlas clusters provides the molecular anchor for their eventual integration into the Cell Ontology and cross-species comparative analysis.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974]; cerebellar cortex [UBERON:0002129] (both classes span full thickness) | [1] |
| NT type | GABAergic | [1] |
| Defining markers | Sorcs3 (MLI1/class I), Nxph1 (both classes; higher in MLI2), Pvalb (both classes; higher in MLI2) | [2], [3] |
| Neuropeptides | Nxph1 | [4] |
| Notes | MLI1 and MLI2 correspond to class I and class II respectively; Purkinje collaterals preferentially target MLI2 over MLI1 |  |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** preprint observation (snRNA-seq) · mouse cerebellar cortex · [1]

- **Sorcs3 (defining marker, MLI1/class I):** scRNA-seq, FEBS Lett 2022 · [2]
  > 2021) also examined the development of molecular layer inhibitory interneurons, which have been historically separated into stellate and basket cells based on their morphology (Leto et al., 2015)(2020)(Leto et al., 2009). This distinction is a little unclear however as many of these interneurons display mixed morphologies, leading to the conclusion that these cells may represent a morphological contiuum. Surprisingly, their adult snRNAseq data revealed two classes of molecular layer interneurons, which they termed as class I (MLI1 and Sorcs3+) and class II (MLI2 and Nxph1+). In an effort to examine the development of these interneurons, the authors expanded their analysis to 5500 GABAergic progenitors across four stages of development and could distinguish between the distinct developmental trajectories of class I and class II interneurons. Although these cells develop from common progenitors, class II differentially expressed immediate early genes such as Fos during their development, which the authors concluded might indicate a higher cellular activity during their specification. Both classes of interneurons differ in their electrophysiological properties, and many class I, but not class II, are coupled to one another via gap junctions, demonstrating that the transcriptomic differences between these two classes of interneurons are also functionally relevant.
  > — Lowenstein et al. 2022, Anatomical organization and core cell types · [2] <!-- quote_key: 247317953_380921bf -->

- **Sorcs3 / Nxph1 (differential marker assignment):** scRNA-seq, Nat Commun 2022 · [3]
  > Differential gene expression analyses confirmed that MLI t-types were distinguished by Sorcs3 or Nxph1 expression51.
  > — Wang & Lefebvre 2022, Results · [3] <!-- quote_key: 213840122_4cb91d31 -->

- **Nxph1 and Pvalb (MLI2/class II markers):** developmental scRNA-seq · [4]
  > Whereas granule cells form a homogeneous differentiating population (Fig. 4B), interneurons are stratified into distinct temporally specified subtypes (fig. S13, E and F): early-born interneurons (Zfhx4, Slit2) detected at E13 to E15, mid-born Golgi cells (Chrm2), Purkinje layer interneurons (Nxph1, Klhl1) prevalent at E17 to P7, and late-born molecular layer interneurons of type 1 (Sorcs3, Grm8) and 2 (MLI2; Nxph1, Pvalb), which are abundant at P14 to P63 (Leto et al., 2015)37).
  > — Sarropoulos et al. 2021, Anatomical organization and core cell types · [4] <!-- quote_key: 237308705_5cd4bd6a -->

- **Two molecularly and functionally distinct types (Kozareva 2020):** snRNA-seq, bioRxiv · [1]
  > For multiple types of cerebellar interneurons, the molecular variation within each type was more continuous, rather than discrete. For the unipolar brush cells (UBCs)—an interneuron population previously subdivided into two discrete populations—the continuous variation in gene expression was associated with a graded continuum of electrophysiological properties. Most surprisingly, we found that molecular layer interneurons (MLIs) were composed of two molecularly and functionally distinct types. Both show a continuum of morphological variation through the thickness of the molecular layer, but electrophysiological recordings revealed marked differences between the two types in spontaneous firing, excitability, and electrical coupling.
  > — Kozareva et al. 2020, Anatomical organization and core cell types · [1] <!-- quote_key: 214725795_3d3df51c -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: molecular layer interneuron [[CL:4042035](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4042035)] (BROAD).

No Cell Ontology term currently exists for the MLI1/MLI2 class split; CL:4042035 (molecular layer interneuron) is the closest parent. Both MLI1 and MLI2 are candidates for new CL term contributions as distinct subtypes.

---

## Results

Annotation transfer from the Kozareva et al. 2021 mouse cerebellar snRNA-seq dataset (GEO:GSE165371; `at_run_20260709_kozareva_cerebellum_mmc_wmbv1`) reveals a clean two-way split: the MLI2 transcriptomic cluster (n=10,544 source cells) maps with extraordinary precision to 5192 CBX MLI Cdh22 Gaba_1 [CS20230722_CLUS_5192] (F1=1.00 at cluster level; see property comparison table), while the MLI1 cluster (represented by both morphological subforms MLI1_1 and MLI1_2) maps to 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] with high specificity for the MLI1_2 source cells (F1=0.79 at cluster level). The two transcriptomic classes thus resolve cleanly onto two distinct WMBv1 clusters distinguished by their defining atlas markers — Cdh22 for MLI2 and Megf11 for MLI1.

### 5192 CBX MLI Cdh22 Gaba_1 · 🟢 HIGH

**Table 1 — Property comparison (MLI2 → CLUS_5192)**

| Property | Classical | Atlas cluster (CLUS_5192) | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] | no atlas anat data | NOT_ASSESSED |
| NT type | GABAergic | GABA | CONSISTENT |
| Sorcs3 expression | defining marker (MLI1 primary; lower in MLI2) | Sorcs3: 0.81 (cohort_pct 0.341) | APPROXIMATE |
| Nxph1 expression | defining marker (both; higher in MLI2) | Nxph1: 11.40 (cohort_pct 0.978) | CONSISTENT |
| Pvalb expression | defining marker | Pvalb: 11.33 (cohort_pct 0.995) | CONSISTENT |
| Nxph1 neuropeptide | Nxph1 | Nxph1: 11.40 (cohort_pct 0.978) | CONSISTENT |

*(Child-cluster breakdown not assessed — CLUS_5192 is a single-cluster mapping; no child substructure surveyed.)*

**Table 2 — Evidence support (MLI2 → CLUS_5192)**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node metadata | Atlas metadata | PARTIAL | no anat data on CLUS_5192 directly | atlas-internal |
| Kozareva 2021 AT (MLI1_1) | Annotation transfer | PARTIAL | F1=0.39 at class level (no sub-class transfer to this lineage) | — |
| Kozareva 2021 AT (MLI1_2) | Annotation transfer | PARTIAL | F1=0.64 at class level (no sub-class transfer to this lineage) | — |
| Kozareva 2021 AT (MLI2) | Annotation transfer | SUPPORT | F1=1.00 at cluster level | — |

The MLI2 → 5192 CBX MLI Cdh22 Gaba_1 [CS20230722_CLUS_5192] mapping is supported by exceptionally clean annotation transfer from the Kozareva/Osorno snRNA-seq dataset (`at_run_20260709_kozareva_cerebellum_mmc_wmbv1`). The MLI2 source cluster (n=10,544 interneuron nuclei) transfers almost entirely to CLUS_5192, achieving F1=1.00, Purity=1.00, and Coverage=0.99 at cluster level. The same source cells reach F1=0.99 at supertype level (1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151]) and F1=0.99 at subclass level, confirming that the mapping is not an artefact of a broad classifier: MLI2 lands specifically on the Cdh22-marked lineage and nowhere else.

**Marker provenance notes:**

- **Sorcs3:** The APPROXIMATE alignment (atlas val=0.81, cohort_pct 0.341) is expected — Sorcs3 is the primary discriminating marker for MLI1 (class I), not MLI2. Lower Sorcs3 on CLUS_5192 is biologically consistent with the MLI2 identity and is not a concern.
- **Nxph1:** CONSISTENT at cohort_pct 0.978 — Nxph1 is cited as the class II (MLI2) discriminating marker by Lowenstein et al. 2022 [2] and Sarropoulos et al. 2021 [4]. High atlas expression is exactly expected for MLI2.
- **Pvalb:** CONSISTENT at cohort_pct 0.995 — Pvalb is described as enriched in the MLI2 cluster per Sarropoulos 2021 [4] ("MLI2; Nxph1, Pvalb"). The high atlas expression at cohort_pct 0.995 is consistent with this description.
- **Atlas anat data absent:** CLUS_5192 lacks spatial registration data in this atlas version — the location comparison is NOT_ASSESSED. This is a data-coverage gap, not a biological concern, since the atlas SUPT_1151 parent carries region_fraction_100um=0.851 (cerebellar, as expected).

**Concerns:**

- No spatial data on CLUS_5192 itself; location assessment relies on parent supertype 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] (region_fraction_100um=0.851, lower_bound completeness). *(note: this is an atlas-coverage limitation, not a biological mismatch; the Cdh22 supertype is cerebellar-specific.)*
- The MLI1_1 and MLI1_2 source labels transfer to CLUS_5192 only at class level (F1=0.39 and 0.64 respectively), confirming they do not share the Cdh22 identity. This is a positive specificity signal for the MLI2 mapping.

**What would upgrade confidence:**

- Spatial registration data for CLUS_5192 directly (atlas update or MERFISH re-registration) would complete the location comparison.
- Literature directly testing Cdh22 protein expression in morphologically confirmed MLI2 cells would provide an independent marker anchor.

---

### 5188 CBX MLI Megf11 Gaba_1 · 🟡 MODERATE

**Table 1 — Property comparison (MLI1 → CLUS_5188)**

| Property | Classical | Atlas cluster (CLUS_5188) | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] | Cerebellum [MBA:512] (region_fraction_100um=0.841; lower_bound) | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Sorcs3 expression | defining marker (MLI1 primary) | Sorcs3: 10.35 (cohort_pct 0.995) | CONSISTENT |
| Nxph1 expression | defining marker (both; higher in MLI2) | Nxph1: 2.09 (cohort_pct 0.362) | APPROXIMATE |
| Pvalb expression | defining marker | Pvalb: 11.12 (cohort_pct 0.989) | CONSISTENT |
| Nxph1 neuropeptide | Nxph1 | Nxph1: 2.09 (cohort_pct 0.362) | APPROXIMATE |

*(Child-cluster breakdown not assessed — single Megf11 cluster as primary candidate; sibling CLUS_5189 [CS20230722_CLUS_5189] is present in the atlas but extremely rare, n=154.)*

**Table 2 — Evidence support (MLI1 → CLUS_5188)**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node metadata | Atlas metadata | PARTIAL | region_fraction_100um=0.841 (lower_bound); strict 0.720 | atlas-internal |
| Kozareva 2021 AT (MLI1_1/basket) | Annotation transfer | PARTIAL | F1=0.51 at cluster level; Purity=0.34 (cross-cutting with MLI1_2) | — |
| Kozareva 2021 AT (MLI1_2/stellate) | Annotation transfer | SUPPORT | F1=0.79 at cluster level; Purity=0.66; Coverage=1.00 | — |
| Kozareva 2021 AT (MLI2) | Annotation transfer | PARTIAL | F1=0.38 at class level (does not reach Megf11 lineage at sub-class) | — |

Annotation transfer from the Kozareva/Osorno dataset supports mapping of the MLI1 transcriptomic class to 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188]. The MLI1_2 (stellate-enriched) source cells transfer cleanly at F1=0.79, Coverage=1.00, Purity=0.66 at cluster level in `at_run_20260709_kozareva_cerebellum_mmc_wmbv1`. The MLI1_1 (basket-enriched) source cells transfer to the same target but with lower purity (F1=0.51, Purity=0.34), consistent with the Kozareva 2020 observation that both basket and stellate morphological forms share the MLI1 transcriptomic identity: the Megf11 atlas cluster captures both morphological subtypes within a single transcriptomic unit. Sorcs3 expression at CLUS_5188 is the highest in the GABAergic cerebellar cohort (val=10.35, cohort_pct 0.995), directly matching the literature description of class I as Sorcs3+ [2],[3].

The moderate purity of MLI1_1 transfer (0.34) reflects a genuine biological feature: basket and stellate morphological forms are transcriptomically unified in MLI1 but produce distinct morphological outputs. This does not indicate a wrong mapping; rather, it explains why neither morphological subform produces a perfect 1:1 AT signal when evaluated independently — both converge on the same Megf11 cluster.

**Marker provenance notes:**

- **Sorcs3 (CONSISTENT, cohort_pct 0.995):** The defining discriminator for class I (MLI1) per Lowenstein 2022 [2] and Wang & Lefebvre 2022 [3]. Atlas expression is at the very top of the cerebellar GABAergic cohort — strong concordance.
- **Nxph1 (APPROXIMATE, cohort_pct 0.362):** Nxph1 is expressed by both MLI1 and MLI2, but at higher levels in MLI2. Lower Nxph1 on CLUS_5188 relative to CLUS_5192 is therefore expected and consistent with the class-I identity. The APPROXIMATE alignment reflects a real but expected quantitative difference, not a mismatch.
- **Pvalb (CONSISTENT, cohort_pct 0.989):** High Pvalb is shared across both MLI classes and consistent with the broad MLI marker profile.
- **Supertype-name circularity check:** The atlas node name "5188 CBX MLI Megf11 Gaba_1" contains "Megf11" — a gene not among the classical defining markers for this node. No circularity issue with the classical marker set (Sorcs3, Nxph1, Pvalb).

**Concerns:**

- Location: region_fraction_100um=0.841 (lower_bound rollup) — a floor value, since non-painted CCF2020 descendants are uncounted. True cerebellar fraction is at least 84.1%, likely higher.
- The MLI1_1 source cells show purity of only 0.34 at cluster level against CLUS_5188. This reflects the cross-cutting nature of the basket/stellate morphological distinction within the MLI1 transcriptomic class — not a concern for the mapping, but a reminder that CLUS_5188 captures the shared transcriptomic identity regardless of axonal morphology.
- The pool_candidates file identifies that `stellate_cell_cerebellum` (a sibling classical node in this KB) shares identical AT metrics to `mli_transcriptomic_classes_cerebellum` at the MLI1_2→CLUS_5188 level (F1=0.794, same coverage and purity). Anat, markers, and NT panels are also non-distinguishing between the two classical nodes at this AT level. This reflects the fact that both classical node definitions draw on the MLI1_2 source label; the extent to which `stellate_cell_cerebellum` and MLI1 (class I) are independently resolvable as distinct classical entities is an open question requiring cross-panel assessment beyond AT alone (ephys, morphology, connectivity).

**What would upgrade confidence:**

- Patch-seq data directly labelling MLI1 (class I) cells and running MapMyCells would provide a source-cell-confirmed AT result, bypassing the basket/stellate ambiguity. Target: F1 ≥ 0.80 at CLUSTER level against CLUS_5188.
- Literature confirming Megf11 protein expression specifically in morphologically confirmed MLI1 (class I) cells would anchor the Megf11 atlas marker to the classical type.
- Resolution of the `stellate_cell_cerebellum` / MLI1 class-I overlap across ephys and morphology panels would clarify whether these are truly one or two classical types.

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 5192 CBX MLI Cdh22 Gaba_1 [CS20230722_CLUS_5192] | 1151 CBX MLI Cdh22 Gaba_1 | null (stale) | 🟢 HIGH | MLI2 AT F1=1.00 to cluster | Primary (MLI2 class) |
| 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] | 1149 CBX MLI Megf11 Gaba_1 | 31,095 | 🟡 MODERATE | MLI1_2 AT F1=0.79; Sorcs3 top-cohort | Secondary (MLI1 class) |
| 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] | — | 13,098 | 🟢 HIGH | MLI2 AT F1=0.99 at supertype; parent of CLUS_5192 | Supports MLI2 mapping (supertype of primary) |
| 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] | 1144 CB PLI Gly-Gaba_1 | 3,066 | 🔴 LOW | AT best F1=0.39 at class only; PLI lineage | Eliminated (PLI lineage, no sub-class transfer) |
| 5185 CB PLI Gly-Gaba_4 [CS20230722_CLUS_5185] | 1147 CB PLI Gly-Gaba_4 | 442 | 🔴 LOW | AT best F1=0.39 at class only; PLI lineage | Eliminated (PLI lineage, no sub-class transfer) |
| 5189 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5189] | 1149 CBX MLI Megf11 Gaba_1 | 154 | 🔴 LOW | AT subclass-level only; very rare sibling | Eliminated (subsumed by CLUS_5188; too rare) |
| 1147 CB PLI Gly-Gaba_4 [CS20230722_SUPT_1147] | — | 442 | 🔴 LOW | AT class-level only; PLI lineage | Eliminated (PLI lineage) |
| 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] | — | 3,646 | 🔴 LOW | AT class-level only; PLI lineage | Eliminated (PLI lineage) |
| 1150 CBX MLI Megf11 Gaba_2 [CS20230722_SUPT_1150] | — | 370 | 🔴 LOW | AT subclass-level F1=0.80; Nxph1 APPROXIMATE | Eliminated (subclass only; small n) |
| 1157 Bergmann NN_1 [CS20230722_SUPT_1157] | — | 3,321 | ⚪ UNCERTAIN | No AT transfer; glia | Eliminated (no AT signal; wrong cell type) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical node `mli_transcriptomic_classes_cerebellum` is defined on a PRIOR_TRANSCRIPTOMIC basis: it represents the MLI1 and MLI2 transcriptomic classes identified by Kozareva et al. 2020 (bioRxiv [1]) and confirmed by Lowenstein et al. 2022 [2], Wang & Lefebvre 2022 [3], and Sarropoulos et al. 2021 [4]. Defining markers are Sorcs3 (class I/MLI1 primary), Nxph1 (both classes; higher in MLI2), and Pvalb (both classes). Soma location is the molecular layer of cerebellar cortex [UBERON:0002974]; both classes span the full thickness of the molecular layer. NT type is GABAergic.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match: cerebellum [MBA:1144, MBA:528], NT type: GABAergic, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE165371 (MLI1_1 basket n=10,998; MLI1_2 stellate n=21,571; MLI2 n=10,544; PLI_1 candelabrum n=1,176; PLI_2 globular n=735; PLI_3 Lugaro n=531) |
| Source species | NCBITaxon:10090 (mouse) |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper 1.7.1, default parameters, 100 bootstrap iterations). Gene symbols remapped to Ensembl IDs via conf/gene_mapping_CCN20230722.tsv (20,390/23,203 genes mapped). Interneuron subset (45,555 of 60,526 joint-archive nuclei). BKP web backend unavailable (HTTP 400) at run time; local backend used. |
| Tool version | cell_type_mapper 1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 45,555 (filtered to 45,555) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/f1_scores_best.csv) |
| Caveats | Same-species (mouse) snRNA-seq → WMBv1. MLI1_1 (basket) and MLI1_2 (stellate) both map to CLUS_5188; MLI1_1 purity is low (0.34) — the two morphological types share the MLI1 transcriptomic cluster (cross-cutting). MLI2 maps cleanly to CLUS_5192 (F1=1.00). Blind-run note: this reproduces the curator ground-truth AT anchors without those targets being supplied to the pipeline. |

**Atlas data sources.** WMBv1 (CCN20230722); pseudobulk SHA-256: b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source evidence_items fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `f4ce9b9` at 2026-07-09T18:53:55+00:00 from [kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml](kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5192 | ATLAS_METADATA; ANNOTATION_TRANSFER (MLI1_1); ANNOTATION_TRANSFER (MLI1_2); ANNOTATION_TRANSFER (MLI2) | PARTIAL; PARTIAL; PARTIAL; SUPPORT | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5188 | ATLAS_METADATA; ANNOTATION_TRANSFER (MLI1_1); ANNOTATION_TRANSFER (MLI1_2); ANNOTATION_TRANSFER (MLI2) | PARTIAL; PARTIAL; SUPPORT; PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5178 | ATLAS_METADATA; ANNOTATION_TRANSFER (MLI1_1); ANNOTATION_TRANSFER (MLI1_2); ANNOTATION_TRANSFER (MLI2) | PARTIAL; PARTIAL; PARTIAL; PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5185 | ATLAS_METADATA; ANNOTATION_TRANSFER (MLI1_1); ANNOTATION_TRANSFER (MLI1_2); ANNOTATION_TRANSFER (MLI2) | PARTIAL; PARTIAL; PARTIAL; PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5189 | ATLAS_METADATA; ANNOTATION_TRANSFER (MLI1_1); ANNOTATION_TRANSFER (MLI1_2); ANNOTATION_TRANSFER (MLI2) | PARTIAL; PARTIAL; PARTIAL; PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1151 | ATLAS_METADATA; ANNOTATION_TRANSFER (MLI1_1); ANNOTATION_TRANSFER (MLI1_2); ANNOTATION_TRANSFER (MLI2) | PARTIAL; PARTIAL; PARTIAL; SUPPORT | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1147 | ATLAS_METADATA; ANNOTATION_TRANSFER (MLI1_1); ANNOTATION_TRANSFER (MLI1_2); ANNOTATION_TRANSFER (MLI2) | PARTIAL; PARTIAL; PARTIAL; PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1144 | ATLAS_METADATA; ANNOTATION_TRANSFER (MLI1_1); ANNOTATION_TRANSFER (MLI1_2); ANNOTATION_TRANSFER (MLI2) | PARTIAL; PARTIAL; PARTIAL; PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1150 | ATLAS_METADATA; ANNOTATION_TRANSFER (MLI1_1); ANNOTATION_TRANSFER (MLI1_2); ANNOTATION_TRANSFER (MLI2) | PARTIAL; PARTIAL; PARTIAL; PARTIAL | atlas-internal |
| edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1157 | ATLAS_METADATA; ANNOTATION_TRANSFER (MLI1_1 NO_EVIDENCE); ANNOTATION_TRANSFER (MLI1_2 NO_EVIDENCE); ANNOTATION_TRANSFER (MLI2 NO_EVIDENCE) | PARTIAL; NO_EVIDENCE; NO_EVIDENCE; NO_EVIDENCE | atlas-internal |

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping (MLI2):** Molecular layer interneuron transcriptomic classes MLI1 / MLI2 (MLI2 subtype) → 5192 CBX MLI Cdh22 Gaba_1 [CS20230722_CLUS_5192] at HIGH confidence. Key support: MapMyCells annotation transfer (F1=1.00 at cluster level; `at_run_20260709_kozareva_cerebellum_mmc_wmbv1`); Nxph1 and Pvalb marker expression CONSISTENT. Key caveat: no spatial registration data for CLUS_5192 directly (location NOT_ASSESSED at cluster level); Sorcs3 APPROXIMATE (expected for class II).

**Secondary mapping (MLI1):** Molecular layer interneuron transcriptomic classes MLI1 / MLI2 (MLI1 subtype) → 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] at MODERATE confidence. Key support: MapMyCells AT (MLI1_2 F1=0.79 at cluster; Sorcs3 top-cohort). Key caveats: MLI1_1 (basket) purity=0.34 (expected cross-cutting of morphological forms sharing one transcriptomic cluster); Nxph1 APPROXIMATE; relationship to sibling `stellate_cell_cerebellum` classical node requires cross-panel resolution.

The Cell Ontology has no specific term for either the MLI1 or MLI2 transcriptomic class; CL:4042035 (molecular layer interneuron) is the closest BROAD ancestor. Both classes are strong candidates for new CL term contributions — two distinct GABAergic subtypes with established transcriptomic, electrophysiological, and developmental support.

### Proposed experiments and follow-ups

AT has already been run (Kozareva/Osorno GEO:GSE165371 → WMBv1; `at_run_20260709_kozareva_cerebellum_mmc_wmbv1`). This provides strong AT evidence for both mappings. Refined experiments below address remaining gaps.

1. **Patch-seq AT for MLI1 confirmation.** Method: patch-seq targeting MLI1/class I cells (e.g. using a Sorcs3-Cre driver or equivalent), followed by MapMyCells against WMBv1. Target: F1 ≥ 0.80 at CLUSTER level against CS20230722_CLUS_5188. Expected output: AnnotationTransferEvidence on the CLUS_5188 edge. Resolves: the basket/stellate purity ambiguity in the current MLI1_1 source label.

2. **Cdh22 and Megf11 protein validation.** Method: immunohistochemistry or smFISH for Cdh22 and Megf11 in cerebellar molecular layer sections. Target: confirm Cdh22 protein on MLI2 cells and Megf11 on MLI1 cells. Expected output: LiteratureEvidence on the respective edges. Resolves: the atlas-name marker concordance question for both primary clusters.

3. **Atlas spatial registration for CLUS_5192.** Required for the location comparison to move from NOT_ASSESSED to CONSISTENT. Resolves: the location caveat on the MLI2 edge.

4. **Cross-panel assessment of `stellate_cell_cerebellum` / MLI1 class-I overlap.** Method: compare ephys, morphology, and connectivity properties of morphologically confirmed stellate cells versus MLI1 (class I) transcriptomic-cluster cells. Expected output: either confirmation that `stellate_cell_cerebellum` is a subset of MLI1 (class I), or evidence of independent classical-type identity. Resolves: the pool_candidates CASE B flag on the CLUS_5188 edge.

5. **New CL term request for MLI1 and MLI2.** Both transcriptomic classes meet CL contribution criteria. Proposed path: run `workflows/cl-term-request.md` for each class once the CLUS_5188 and CLUS_5192 mappings are accepted.

### Open questions

1. Is `stellate_cell_cerebellum` a morphological synonym for MLI1 (class I), or does it represent an independently defined classical type that partially overlaps the MLI1 transcriptomic class? The pool_candidates flag (identical AT metrics at MLI1_2→CLUS_5188) indicates AT-level indistinguishability; ephys and morphology panels not yet assessed.

2. Does the low purity of MLI1_1 (basket) AT transfer to CLUS_5188 (Purity=0.34) reflect genuine scatter across multiple Megf11-lineage clusters, or is it entirely explained by the basket/stellate cross-cutting within the single MLI1 transcriptomic unit? A sibling cluster CLUS_5189 [CS20230722_CLUS_5189] (n=154) exists in the Megf11 lineage — basket cells may be enriched there, though the extremely low cell count makes this unlikely to be the primary explanation.

3. What is the spatial distribution of CLUS_5192 (Cdh22 cluster) in the cerebellar molecular layer? The lack of MERFISH registration data for this cluster prevents assessment of whether MLI2 cells occupy a distinct sub-laminar position.

4. Nxph1 is listed as a defining marker for the overall MLI node and as a neuropeptide. A primary-literature trawl specifically anchoring Nxph1 peptide function in MLI cells (as opposed to transcript-level detection) would clarify whether the neuropeptide annotation is supported by protein-level data.

5. Why did CS20230722_SUPT_1157 (Bergmann NN_1) survive Stage A scoring for an MLI node? The Pvalb-driven composite score (val=1.44) and location proximity may be the cause. Stage A cohort filters (region=MBA:1144,MBA:528; nt=GABAergic) should exclude non-neuronal types — worth investigating whether Bergmann glia carry a GABAergic NT annotation in the taxonomy.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Kozareva et al. 2020 — https://doi.org/10.1101/2020.03.04.976407 | — | Soma location, GABAergic NT, MLI1/MLI2 two-class discovery |
| [2] | Lowenstein et al. 2022 · PMID:[35262281](https://pubmed.ncbi.nlm.nih.gov/35262281/) | 35262281 | Sorcs3 marker (class I), Nxph1 marker (class II), developmental trajectories |
| [3] | Wang & Lefebvre 2022 · PMID:[35701402](https://pubmed.ncbi.nlm.nih.gov/35701402/) | 35701402 | Sorcs3/Nxph1 differential expression confirmation |
| [4] | Sarropoulos et al. 2021 · PMID:[34446581](https://pubmed.ncbi.nlm.nih.gov/34446581/) | 34446581 | Pvalb (MLI2), Nxph1, developmental marker assignment |

---

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5192 -->
```yaml
verdict:
  confidence: HIGH
  confidence_score: 0.92
  relationship: skos:exactMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] MLI2 source cluster (GEO:GSE165371) transfers to CS20230722_CLUS_5192
    with F1=1.00 at cluster level in at_run_20260709_kozareva_cerebellum_mmc_wmbv1
    (Purity=1.00, Coverage=0.99). 3 of 4 markers CONSISTENT (Nxph1 cohort_pct 0.978,
    Pvalb cohort_pct 0.995, neuropeptide_Nxph1 cohort_pct 0.978); Sorcs3 APPROXIMATE
    (expected for class II / MLI2 identity).
    NT CONSISTENT (GABAergic/GABA). Location NOT_ASSESSED (no region data on CLUS_5192
    directly; parent SUPT_1151 region_fraction_100um: 0.851, lower_bound).
  reconciliation_note: >
    MLI2 maps 1:1 to CS20230722_CLUS_5192 (Cdh22 cluster). Paired with
    edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5188 (MLI1 → Megf11
    cluster); together the two edges document the two-class split of the MLI population.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        No MERFISH spatial registration data exists for CS20230722_CLUS_5192 directly;
        location comparison is NOT_ASSESSED at cluster level. Parent supertype
        CS20230722_SUPT_1151 has region_fraction_100um=0.851 (lower_bound rollup)
        confirming cerebellar identity, but sub-laminar position of Cdh22 cells
        within the molecular layer is not resolved from atlas metadata.
  proposed_experiments:
    - >
      Annotation transfer from a pure MLI2/class II source dataset to WMBv1;
      target F1 ≥ 0.80 at cluster level against CS20230722_CLUS_5192.
    - >
      Atlas spatial registration update for CS20230722_CLUS_5192.
    - >
      Expression validation of Cdh22 in cerebellar molecular layer to confirm
      expression in MLI2 (class II) cells.
  unresolved_questions:
    - >
      What is the sub-laminar position of CS20230722_CLUS_5192 (Cdh22) cells within the
      cerebellar molecular layer?
    - >
      Does the Purkinje collateral preference for MLI2 over MLI1 correlate with the
      Cdh22/Megf11 atlas cluster split?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5188 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.72
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] MLI1 source (GEO:GSE165371) transfers to CS20230722_CLUS_5188 with
    F1=0.79 at cluster level (MLI1_2 stellate source; at_run_20260709_kozareva_cerebellum_mmc_wmbv1).
    Sorcs3 CONSISTENT (cohort_pct 0.995 — highest in cerebellar GABAergic cohort).
    2 of 4 markers CONSISTENT (Sorcs3, Pvalb); Nxph1 APPROXIMATE (cohort_pct 0.362 —
    expected, as Nxph1 enriched in MLI2); neuropeptide_Nxph1 APPROXIMATE. NT CONSISTENT.
    Location CONSISTENT (region_fraction_100um: 0.841, lower_bound). Downgrade from HIGH:
    MLI1_1 purity=0.34 (cross-cutting of basket and stellate forms within the MLI1
    transcriptomic class); Nxph1 APPROXIMATE; relationship with
    stellate_cell_cerebellum classical node requires resolution (pool_candidates
    AT-level indistinguishability — CASE B).
  reconciliation_note: >
    MLI1 (class I) maps to CS20230722_CLUS_5188 (Megf11 cluster); paired with
    edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5192 (MLI2 → Cdh22).
    Pool_candidates identifies AT-level indistinguishability between this node and
    stellate_cell_cerebellum at MLI1_2→CS20230722_CLUS_5188 (F1=0.79, identical
    coverage/purity); anat, markers, NT panels also non-distinguishing in this run.
    Ephys, cell-shape, connectivity panels NOT assessed — CASE B call. No lit_to_lit
    edge emitted pending cross-panel assessment.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal driven by lower_bound rollup row; region_fraction_100um=0.841
        is a floor — true cerebellar fraction is at least 84.1%.
    - caveat_type: OTHER
      description: >
        MLI1_1 (basket) source cells transfer to CS20230722_CLUS_5188 with Purity=0.34,
        reflecting cross-cutting of basket and stellate forms within
        the single MLI1 transcriptomic class. MLI1_2 (stellate) drives the primary
        support (F1=0.79). The mapping captures the transcriptomic class identity;
        axonal projection pattern is not a discriminator at this atlas resolution.
  proposed_experiments:
    - >
      Annotation transfer from a pure MLI1/class I source dataset (e.g. an MLI1-enriched
      source) to WMBv1; target F1 ≥ 0.80 at cluster level
      against CS20230722_CLUS_5188.
    - >
      Cross-panel comparison (electrophysiology, connectivity) of stellate_cell_cerebellum
      vs MLI1 (class I) to determine whether they are independently resolvable.
    - >
      Expression validation of Megf11 in cerebellar molecular layer to confirm
      expression in MLI1 (class I) cells.
  unresolved_questions:
    - >
      Are stellate_cell_cerebellum and MLI1 (class I) independently resolvable classical
      types across ephys, cell-shape, and connectivity panels, or are they AT-level
      synonyms? See pool_candidates CASE B flag.
    - >
      Does CLUS_5189 (CS20230722_CLUS_5189; n=154) preferentially capture basket-cell
      axonal projection form within the MLI1 transcriptomic class?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5178 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] All three MLI source labels transfer to CS20230722_CLUS_5178 only at
    class level (best F1=0.39 from MLI1_2 in at_run_20260709_kozareva_cerebellum_mmc_wmbv1);
    no sub-class or cluster-level transfer to this lineage. CLUS_5178 is a PLI
    (Purkinje layer interneuron) cluster. The class-level signal reflects shared
    CB GABA class identity, not a genuine MLI mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5185 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] All three MLI source labels transfer to CS20230722_CLUS_5185 only at
    class level (best F1=0.39 in at_run_20260709_kozareva_cerebellum_mmc_wmbv1);
    no sub-class transfer to this PLI lineage. CB GABA class signal only.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_CLUS_5189 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.20
  rationale: >
    [tier:CUT] MLI1 source cells reach CS20230722_CLUS_5189 at subclass level only
    (subclass 311 CBX MLI Megf11 Gaba); no cluster-level metrics row for CLUS_5189
    in at_run_20260709_kozareva_cerebellum_mmc_wmbv1. Extremely rare cluster (n=154);
    mapping subsumed by the primary CLUS_5188 evidence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1151 -->
```yaml
verdict:
  confidence: HIGH
  confidence_score: 0.88
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] MLI2 source (GEO:GSE165371) transfers to CS20230722_SUPT_1151 with
    F1=0.99 at supertype level in at_run_20260709_kozareva_cerebellum_mmc_wmbv1.
    3 of 4 markers CONSISTENT (Nxph1 cohort_pct 0.982, Pvalb cohort_pct 0.991, neuropeptide_Nxph1 cohort_pct 0.982);
    Sorcs3 APPROXIMATE (expected for MLI2). Location CONSISTENT
    (region_fraction_100um: 0.851, lower_bound). CS20230722_SUPT_1151 is the parent
    supertype of the primary mapping target CS20230722_CLUS_5192 (F1=1.00 at cluster).
    Supertype edge retained as supporting context; primary verdict on CLUS_5192 edge.
  reconciliation_note: >
    CS20230722_SUPT_1151 is the parent of CS20230722_CLUS_5192 (primary MLI2 mapping).
    The supertype edge confirms the lineage identity; the cluster-level edge is the
    primary evidence record.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal driven by lower_bound rollup; region_fraction_100um=0.851 is a floor.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1147 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] All three MLI source labels reach CS20230722_SUPT_1147 only at class
    level (best F1=0.39 in at_run_20260709_kozareva_cerebellum_mmc_wmbv1). PLI
    lineage; no MLI-specific transfer.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1144 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] All three MLI source labels reach CS20230722_SUPT_1144 only at class
    level (best F1=0.39 from MLI1_2 in at_run_20260709_kozareva_cerebellum_mmc_wmbv1).
    PLI lineage; no MLI-specific transfer.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1150 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.22
  rationale: >
    [tier:CUT] MLI1 source cells reach CS20230722_SUPT_1150 at subclass level only
    (best F1=0.80 from MLI1_2 at subclass 311 CBX MLI Megf11 Gaba in
    at_run_20260709_kozareva_cerebellum_mmc_wmbv1). SUPT_1150 is a small supertype
    (n=370) within the Megf11 lineage. Nxph1 APPROXIMATE (cohort_pct 0.482).
    Subsumed by the CLUS_5188 evidence; no independent sub-class-level signal
    distinguishing this supertype as a better match.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_mli_transcriptomic_classes_cerebellum_to_CS20230722_SUPT_1157 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.02
  rationale: >
    [tier:CUT] NO_EVIDENCE from all three MLI source labels in
    at_run_20260709_kozareva_cerebellum_mmc_wmbv1 — MLI1_1, MLI1_2, and MLI2 all
    fail to transfer to the CS20230722_SUPT_1157 (Bergmann NN_1) lineage. Bergmann
    glia are a non-neuronal glial type; no biological basis for an MLI mapping.
    Candidate likely survived Stage A due to Pvalb val=1.44 and location proximity.
  unresolved_questions:
    - >
      Why did CS20230722_SUPT_1157 (Bergmann NN_1) survive Stage A scoring for an MLI
      node? Investigate whether Bergmann glia carry a GABAergic NT annotation in the
      taxonomy — if so, the cohort filter (nt=GABAergic) is incorrectly passing them.
```
<!-- verdict-block-end -->
