# entorhinal cortex layer II calbindin-positive pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

---

## Introduction

Entorhinal cortex (EC) layer II is organised into two principal-cell populations: calbindin-positive pyramidal cells, arranged as a hexagonal grid of patches in medial EC, and reelin-positive stellate cells. The calbindin pyramidal cells originate widespread telencephalic and intrinsic projections, are strongly theta-modulated, and form the substrate for one of the EC's two parallel output streams to the hippocampus.

> Principal neurons in entorhinal cortex layer II are of two types, stellate-like neurons and pyramidal neurons, the former of which express reelin, whereas the latter include a large population of calbindin-expressing neurons (Ohara et al., 2021)(Varga et al., 2010)(Fuchs et al., 2016)(Ohara et al., 2019)(Zutshi et al., 2018).
> — Varga et al. 2010, Entorhinal Cortex Glutamatergic Populations · [5] <!-- quote_key: 10189534_9b25e78b -->

> We confirm the existence of patches of calbindin‐positive pyramidal cells across these species, arranged periodically
> — Naumann et al. 2015, abstract · [4] <!-- quote_key: 10060696_93c3874e -->

> the layer II CB+ population comprises neurons with diverse, mainly excitatory projections. At least half of them originate local intrinsic and commissural projections which distribute mainly to layer I and II
> — Ohara et al. 2019, abstract · [1] <!-- quote_key: 204538361_555db016 -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | entorhinal cortex [UBERON:0002728] (layer II) | [1], [2], [3] |
| NT | glutamatergic | [4] |
| Markers | Calb1 (defining) | [4], [5] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** entorhinal cortex layer II · [1], [2], [3]
  > the layer II CB+ population comprises neurons with diverse, mainly excitatory projections. At least half of them originate local intrinsic and commissural projections which distribute mainly to layer I and II
  > — Ohara et al. 2019, abstract · [1] <!-- quote_key: 204538361_555db016 -->

  > optogenetically perturb locally projecting layer II pyramidal cells. We find that sharply tuned HD cells are only weakly responsive while speed, broadly tuned HD cells, and grid cells show pronounced transient excitatory and inhibitory responses
  > — Zutshi et al. 2018, abstract · [2] <!-- quote_key: 52194250_dabdef57 -->

  > here we provide the first cell-type-based global map of EC in macaque monkeys
  > — Ohara et al. 2021, abstract · [3] <!-- quote_key: 244909998_3c05e0b2 -->

- **NT type:** glutamatergic · [4]
  > In the rodent entorhinal cortex, $88% of calbindin-positive cells are glutamatergic
  > — Naumann et al. 2015, body · [4] <!-- quote_key: 10060696_f4cc1f5f -->

- **Calb1 marker:** defining · [4], [5]
  > We confirm the existence of patches of calbindin‐positive pyramidal cells across these species, arranged periodically
  > — Naumann et al. 2015, abstract · [4] <!-- quote_key: 10060696_93c3874e -->

  > Principal neurons in entorhinal cortex layer II are of two types, stellate-like neurons and pyramidal neurons, the former of which express reelin, whereas the latter include a large population of calbindin-expressing neurons (Ohara et al., 2021)(Varga et al., 2010)(Fuchs et al., 2016)(Ohara et al., 2019)(Zutshi et al., 2018).
  > — Varga et al. 2010, Entorhinal Cortex Glutamatergic Populations · [5] <!-- quote_key: 10189534_9b25e78b -->

</details>

Cell Ontology mapping: pyramidal neuron [[CL:0000598](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000598)] (BROAD).

---

## Results

Annotation-transfer evidence from Yao 2021 medial EC layer II IT cells (n=42) supports a primary mapping to the supertype 0052 L2 IT ENT-po Glut_2 [CS20230722_SUPT_0052] (F1=0.69; see figure and property comparison table), with 33% of the same source cells landing on the sibling supertype 0054 L2 IT ENT-po Glut_4 [CS20230722_SUPT_0054]; the two ENT-po supertypes together absorb 92.8% of the source population, consistent with the calbindin patches partitioning across two closely related medial-EC L2 transcriptomic populations rather than mapping cleanly to a single one. A third high-Calb1 candidate at the lateral-EC supertype 0035 L2/3 IT ENT Glut_3 [CS20230722_SUPT_0035] is structurally plausible on Calb1 expression and EC location but lacks direct AT support in this dataset.

![Annotation transfer F1 tree — Yao 2021 SSv4 HPF → WMBv1](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_tree.png)

*F1 across taxonomy levels for the Yao 2021 (GEO:GSE185862) SSv4 hippocampal-formation source labels mapped onto WMBv1 (CCN20230722) by local MapMyCells. Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. The L2 IT ENTm subclass (n=42) is the relevant row for the calbindin pyramidal type; its dominant supertype-level assignment is 0052 L2 IT ENT-po Glut_2 with secondary scatter onto 0054 L2 IT ENT-po Glut_4. The figure is rendered run-level without source filtering because the canonical "L2 IT ENTm" source label (a subclass aggregation upstream of the figure's per-source rows) is not surfaced as a separate panel; readers should locate the ENT-po Glut rows for the relevant signal.*

### 0052 L2 IT ENT-po Glut_2 [CS20230722_SUPT_0052] · 🟡 MODERATE

**Supporting evidence:**
- Annotation transfer of Yao 2021 SSv4 medial EC layer II IT cells (L2 IT ENTm subclass, n=42) onto WMBv1 maps 59.5% of source cells to this supertype, with F1=0.694 (Purity=0.833, Coverage=0.595) at supertype level — direct transcriptomic evidence linking the medial-EC L2 IT population (dominated by calbindin-positive pyramidal cells) to ENT-po Glut_2. The "ENT-po" (entorhinal postrhinal) designation in the WMBv1 taxonomy encompasses medial EC and postrhinal cortex layer II populations.
- Location alignment is excellent: `region_fraction_100um: 1.000`, strict `region_fraction: 0.933`; the supertype's painted soma counts concentrate in entorhinal area medial part dorsal zone [MBA:926] and layer 3 thereof [MBA:664], within the hippocampal formation [MBA:1089].
- Calb1 mean expression on the supertype is 7.14 (cohort percentile 0.913, child-coverage 1.000) — concordant with the defining marker and present across all child clusters.

**Property alignment**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | entorhinal cortex [UBERON:0002728] | hippocampal formation [MBA:1089] / entorhinal area medial part dorsal zone [MBA:926]; region_fraction_100um=1.000 | not assessed | CONSISTENT |
| NT type | glutamatergic | not asserted | not assessed | NOT_ASSESSED |
| Calb1 expression | defining marker | 7.14 (cohort_pct 0.913; child-coverage 1.000) | not assessed | CONSISTENT |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Yao 2021 L2 IT ENTm AT | Annotation transfer | SUPPORT | F1=0.69 | — |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Concerns:**
- The AT source has n=42 cells, limiting statistical confidence; the supertype-level Coverage of 0.595 means roughly 41% of L2 IT ENTm cells map elsewhere, predominantly to SUPT_0054 (33%) — see paired survivor below.
- NT alignment is structurally unassessable because the supertype does not assert an NT label in the taxonomy metadata; the assignment is inferred from the Glut subclass naming and from the source-side glutamatergic assertion in Naumann 2015 [4].
- The "ENT-po" (entorhinal postrhinal) supertype name encompasses both medial EC and postrhinal cortex layer II populations, so a fraction of supertype cells may originate from postrhinal cortex rather than medial EC proper.

**What would upgrade confidence:**
- A larger medial-EC layer II patch-seq or scRNA-seq cohort (Cre-driver targeting of calbindin-positive pyramidal cells, e.g. Wfs1-Cre or anatomically restricted dissection) mapped via MapMyCells at F1 ≥ 0.80 at SUPERTYPE level, with explicit reporting of how the source cells distribute across SUPT_0052 and SUPT_0054.
- A precomputed-expression check of Calb1 and Reln on the SUPT_0052 / SUPT_0054 cohort vs. the stellate-associated supertype to resolve the calbindin/reln pyramidal/stellate axis at atlas level.

### 0054 L2 IT ENT-po Glut_4 [CS20230722_SUPT_0054] · 🟡 MODERATE

**Supporting evidence:**
- The same Yao 2021 L2 IT ENTm cohort scatters a further 33.3% of cells onto this supertype; together with SUPT_0052 it covers 92.8% of the source population. This is the AT scatter partner to the primary mapping, not an independent line of evidence.
- Location is excellent: `region_fraction_100um: 0.979`, strict `region_fraction: 0.954`, with painted soma counts heavily concentrated in entorhinal area medial part dorsal zone layer 2 [MBA:543]. This is the strongest location score among all candidates and the only one whose dominant painted layer is explicitly layer 2.
- Belongs to the same ENT-po subclass as SUPT_0052; co-membership of the AT pair is consistent with the calbindin pyramidal patches having transcriptomic structure that splits across two closely related medial-EC L2 supertypes.

**Property alignment**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | entorhinal cortex [UBERON:0002728] | hippocampal formation [MBA:1089] / entorhinal area medial part dorsal zone layer 2 [MBA:543]; region_fraction_100um=0.979 | not assessed | CONSISTENT |
| NT type | glutamatergic | not asserted | not assessed | NOT_ASSESSED |
| Calb1 expression | defining marker | 0.66 (cohort_pct 0.489; child-coverage 1.000) | not assessed | APPROXIMATE |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (location) | Atlas metadata | PARTIAL | region_fraction_100um=0.979 | — |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Concerns:**
- Calb1 mean expression on this supertype is 0.66 (cohort percentile 0.489) — substantially lower than on SUPT_0052 (7.14). This is the central inconsistency: SUPT_0054 receives a third of L2 IT ENTm AT scatter and has the best location score of any candidate, but its atlas-side Calb1 expression is approximate at best. Possible readings include (a) Calb1 expression within the ENT-po L2 calbindin patch population is bimodal across SUPT_0052 / SUPT_0054, with only one of the two carrying high Calb1 mean expression, or (b) the AT scatter onto SUPT_0054 reflects medial-EC L2 cells that are not the calbindin pyramidal type proper.
- Same n=42 small-sample limitation as the primary candidate.
- NT alignment unassessable (supertype does not assert an NT label).

**What would upgrade confidence:**
- Per-child-cluster Calb1 measurement across the SUPT_0054 child clusters to test whether a subset carries Calb1 at the expected level — current child-cluster breakdown is not assessed.
- Larger medial-EC L2 source cohort to determine whether the SUPT_0052 / SUPT_0054 split is stable and biologically meaningful, or noise at n=42.

### 0035 L2/3 IT ENT Glut_3 [CS20230722_SUPT_0035] · 🔴 LOW

**Supporting evidence:**
- Calb1 mean expression on this supertype is 7.78 (cohort percentile 0.967, child-coverage 1.000) — the highest Calb1 signal among the ENT supertypes assessed.
- Location: `region_fraction_100um: 0.786`, strict `region_fraction: 0.709`; painted soma counts concentrate in entorhinal area lateral part [MBA:918] layer 3 [MBA:52]. This is the lateral-EC counterpart to the medial-EC ENT-po supertypes — anatomically EC but a different EC subdivision and a deeper layer than the classical type's layer II soma.

**Property alignment**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | entorhinal cortex [UBERON:0002728] | hippocampal formation [MBA:1089] / entorhinal area lateral part layer 3 [MBA:52]; region_fraction_100um=0.786 | not assessed | CONSISTENT |
| NT type | glutamatergic | not asserted | not assessed | NOT_ASSESSED |
| Calb1 expression | defining marker | 7.78 (cohort_pct 0.967; child-coverage 1.000) | not assessed | CONSISTENT |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (location) | Atlas metadata | PARTIAL | region_fraction_100um=0.786 | — |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Concerns:**
- No annotation-transfer evidence supports this supertype: in the Yao 2021 SSv4 run, the available lateral-EC source label "L2/3 IT ENTl" maps not onto SUPT_0035 but onto a dentate gyrus supertype at n=2 cells, suggesting that the lateral-EC L2/3 source population is either too sparse in this dataset to evaluate the mapping or that the lateral-EC pyramidal cells are not well represented as a coherent transcriptomic group at this resolution. *(note: the lateral-EC L2/3 IT ENTl source label dropping out at n=2 is consistent with the Yao 2021 hippocampal-formation dataset under-sampling pure lateral-EC populations, not with refutation of SUPT_0035 itself.)*
- The classical calbindin patches are canonically a medial-EC layer II phenomenon; SUPT_0035 is lateral-EC layer 3. While Calb1 is highly expressed here, this likely represents a separate Calb1+ EC population (lateral L2/3 IT) rather than the medial-EC layer II calbindin pyramidal cells the classical type names.

**What would upgrade confidence:**
- A medial-EC-restricted scRNA-seq or patch-seq cohort that cleanly excludes lateral-EC and postrhinal cells, mapped to WMBv1 — would clarify whether any medial-EC L2 calbindin cells map to SUPT_0035 or whether SUPT_0035 is the lateral-EC homologue.
- Targeted literature search for Calb1+ pyramidal cells specifically in lateral EC layer 3 versus medial EC layer II, to assess whether SUPT_0035 represents a distinct anatomical / functional population.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0052 L2 IT ENT-po Glut_2 [CS20230722_SUPT_0052] | — | 992 | 🟡 MODERATE | AT F1=0.69 from L2 IT ENTm; Calb1=7.14 | Primary |
| 0054 L2 IT ENT-po Glut_4 [CS20230722_SUPT_0054] | — | 1867 | 🟡 MODERATE | AT scatter partner (33% of L2 IT ENTm); best location | Secondary (paired) |
| 0035 L2/3 IT ENT Glut_3 [CS20230722_SUPT_0035] | — | 2527 | 🔴 LOW | Calb1=7.78; lateral-EC L3 | Supports broader mapping |
| 0129 L2/3 IT ENT Glut_3 [CS20230722_CLUS_0129] | 0035 L2/3 IT ENT Glut_3 | 909 | ⚪ UNCERTAIN | Calb1=8.15; lateral-EC L3 child of SUPT_0035 | Eliminated (lateral-EC; no AT) |
| 0259 ENTmv-PA-COAp Glut_3 [CS20230722_CLUS_0259] | 0068 ENTmv-PA-COAp Glut_3 | 673 | ⚪ UNCERTAIN | Calb1=8.30; medial-EC ventral L5 | Eliminated (wrong layer; PA-COAp admixture) |
| 0260 ENTmv-PA-COAp Glut_3 [CS20230722_CLUS_0260] | 0068 ENTmv-PA-COAp Glut_3 | 290 | ⚪ UNCERTAIN | Calb1=8.46; medial-EC ventral L3 | Eliminated (wrong layer; PA-COAp admixture) |
| 0068 ENTmv-PA-COAp Glut_3 [CS20230722_SUPT_0068] | — | 963 | ⚪ UNCERTAIN | Calb1=8.38; ENTmv with PA/COAp admixture | Eliminated (cross-region supertype) |
| 0329 L2/3 IT PPP Glut_1 [CS20230722_CLUS_0329] | 0084 L2/3 IT PPP Glut_1 | 505 | ⚪ UNCERTAIN | Calb1=8.07; parahippocampal | Eliminated (PPP, not EC proper) |
| 0014 IT EP-CLA Glut_2 [CS20230722_CLUS_0014] | 0004 IT EP-CLA Glut_2 | 849 | ⚪ UNCERTAIN | Calb1=1.76; endopiriform/claustrum | Eliminated (wrong region) |
| 0010 L5/6 IT TPE-ENT Glut_4 [CS20230722_SUPT_0010] | — | 1791 | ⚪ UNCERTAIN | Calb1=0.47; lateral-EC L5/6 | Eliminated (wrong layer; Calb1 low) |
| 0067 ENTmv-PA-COAp Glut_2 [CS20230722_SUPT_0067] | — | 943 | ⚪ UNCERTAIN | Calb1=4.99; ENTmv with PA/COAp admixture | Eliminated (cross-region supertype) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The entorhinal cortex layer II calbindin-positive pyramidal cell is defined as a glutamatergic [4] principal neuron of EC layer II [1][2][3], identified by Calb1 expression [4][5], arranged in a hexagonal patch grid in medial EC, with widespread telencephalic and intrinsic projections and strong theta modulation. `definition_basis: CLASSICAL_MULTIMODAL`.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4 cell type labels) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:55+00:00 from [kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_ec_layer2_pyramidal_cell_hippocampus_to_supt_0052 | ANNOTATION_TRANSFER | SUPPORT | — |
| edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0054 | ATLAS_METADATA | PARTIAL | — |
| edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0035 | ATLAS_METADATA | PARTIAL | — |
| edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0129 | ATLAS_METADATA | PARTIAL | — |
| edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0259 | ATLAS_METADATA | PARTIAL | — |
| edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0260 | ATLAS_METADATA | PARTIAL | — |
| edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0068 | ATLAS_METADATA | PARTIAL | — |
| edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0329 | ATLAS_METADATA | PARTIAL | — |
| edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0014 | ATLAS_METADATA | PARTIAL | — |
| edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0010 | ATLAS_METADATA | PARTIAL | — |
| edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0067 | ATLAS_METADATA | PARTIAL | — |

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** entorhinal cortex layer II calbindin-positive pyramidal cell → 0052 L2 IT ENT-po Glut_2 [CS20230722_SUPT_0052] at MODERATE confidence. Key support: annotation transfer from Yao 2021 medial-EC L2 IT cells (F1=0.69 at SUPERTYPE level); concordant location (region_fraction_100um=1.000) and Calb1 expression (cohort_pct 0.913). Key caveats: AMBIGUOUS_MAPPING — 33% of source cells scatter to the sibling supertype SUPT_0054, suggesting the calbindin pyramidal patches partition across two closely related ENT-po Glut supertypes rather than mapping cleanly to one; small source sample (n=42) limits statistical confidence.

The Cell Ontology has no specific term for EC layer II calbindin-positive pyramidal cells; pyramidal neuron [[CL:0000598](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000598)] is the closest ancestor. EC layer II calbindin-positive pyramidal cells originate widespread telencephalic and intrinsic projections and show strong theta modulation. Arranged in a hexagonal patch grid in medial EC. CL:0000598 (pyramidal neuron) is the best available match; no EC layer II pyramidal-specific CL term exists.

### Proposed experiments and follow-ups

- **What:** Larger medial-EC layer II patch-seq or scRNA-seq cohort with Cre-driver targeting (e.g. Wfs1-Cre, calbindin-specific drivers) or anatomically restricted medial-EC dissection, mapped to WMBv1 via MapMyCells.
  **Target:** F1 ≥ 0.80 at SUPERTYPE level; explicit reporting of how source cells distribute between SUPT_0052 and SUPT_0054.
  **Expected output:** A higher-confidence AnnotationTransferEvidence record replacing the present n=42 evidence, with a defensible SUPT_0052-vs-SUPT_0054 partition.
  **Resolves:** The AMBIGUOUS_MAPPING caveat on the primary edge; open questions 1 and 2.
  **Note on completed work:** The present ANNOTATION_TRANSFER evidence already uses MapMyCells on Yao 2021 SSv4 cells (n=42). A refined run is needed because the source sample is small and the source labels are subclass-level aggregations rather than calbindin-targeted populations.
- **What:** Precomputed-expression cross-check of Calb1 and Reln across the relevant ENT-po Glut and stellate-associated supertypes at child-cluster resolution.
  **Target:** Identify which SUPT_0052 / SUPT_0054 child clusters carry Calb1 at the high-expression tier (≥ 4.0 mean) versus reln-dominant signatures.
  **Expected output:** A property-level discrimination between the calbindin pyramidal and reln stellate atlas populations, written back as MarkerAnalysisEvidence on the relevant edges.
  **Resolves:** Open question 1; clarifies the SUPT_0054 Calb1=0.66 anomaly.

### Open questions

1. Does Calb1 expression distinguish SUPT_0052 from SUPT_0042 (stellate)? Precomputed expression check for Calb1 and Reln in SUBT_011 (ENT-po) vs SUBC_009 (PIR-ENTl) supertypes would resolve the stellate/pyramidal distinction at the atlas level.
2. Within SUPT_0054, which child cluster(s) carry Calb1 at the high-expression tier consistent with the calbindin pyramidal type, and which carry the L2 IT ENTm AT scatter? Current child-cluster breakdown is not assessed.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Ohara et al. 2019 | [31680885](https://pubmed.ncbi.nlm.nih.gov/31680885) | soma location |
| [2] | Zutshi et al. 2018 | [30209250](https://pubmed.ncbi.nlm.nih.gov/30209250) | soma location |
| [3] | Ohara et al. 2021 | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991) | soma location |
| [4] | Naumann et al. 2015 | [26223342](https://pubmed.ncbi.nlm.nih.gov/26223342) | neurotransmitter type; Calb1 marker |
| [5] | Varga et al. 2010 | [20512133](https://pubmed.ncbi.nlm.nih.gov/20512133) | Calb1 marker |

---

<!-- verdict-block-start: edge_ec_layer2_pyramidal_cell_hippocampus_to_supt_0052 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.65
  relationship: skos:closeMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Annotation transfer from Yao 2021 medial-EC L2 IT cells
    (n=42) places 59.5% of source cells on CS20230722_SUPT_0052 with F1=0.69
    at supertype level (run_ref: at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1);
    location region_fraction_100um=1.000 and Calb1=7.14 (cohort_pct 0.913)
    are both CONSISTENT. 2 of 3 markers CONSISTENT (Calb1, location); NT
    NOT_ASSESSED on the supertype side. 33% AT scatter onto sibling
    CS20230722_SUPT_0054 motivates 1:n cardinality.
  reconciliation_note: >
    Paired with CS20230722_SUPT_0054 as scatter partner; together the two
    ENT-po Glut supertypes absorb 92.8% of L2 IT ENTm AT source cells. The
    calbindin pyramidal patches likely partition across both supertypes
    rather than mapping cleanly to one.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Small AT sample (n=42) limits statistical confidence;
        CS20230722_SUPT_0052 and CS20230722_SUPT_0054 together cover 92.8%
        of L2 IT ENTm cells (59.5% + 33.3%), so the classical EC layer II
        calbindin pyramidal cell splits across these two supertypes rather
        than mapping cleanly to either alone.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Supertype NT label is not asserted in WMBv1 metadata; NT alignment
        is inferred from the Glut subclass naming and from the source-side
        glutamatergic assertion in Naumann 2015.
  proposed_experiments:
    - >
      Larger medial-EC layer II scRNA-seq or patch-seq cohort with
      Cre-driver targeting (e.g. Wfs1-Cre) or anatomically restricted
      medial-EC dissection, mapped via MapMyCells; target F1 >= 0.80 at
      supertype level with explicit SUPT_0052/SUPT_0054 partition reporting.
    - >
      Precomputed expression check of Calb1 and Reln across the SUPT_0052,
      SUPT_0054, and stellate-associated supertype child clusters to
      anchor the pyramidal/stellate distinction at atlas resolution.
  unresolved_questions:
    - >
      Within the L2 IT ENTm AT cohort, which source-cell subpopulation
      drives the SUPT_0054 scatter versus the SUPT_0052 majority?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0054 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:closeMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] AT scatter partner of CS20230722_SUPT_0052: 33% of the Yao
    2021 L2 IT ENTm cohort (n=42) lands here (run_ref:
    at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1); together with SUPT_0052
    the pair covers 92.8% of source cells. Location is the strongest of
    all candidates (region_fraction_100um=0.979, strict region_fraction=0.954,
    painted soma concentrated in entorhinal area medial part dorsal zone
    layer 2). Calb1=0.66 (cohort_pct 0.489) is APPROXIMATE — the central
    inconsistency: best location among candidates but supertype-level mean
    Calb1 below the high-expression tier. 1 of 3 markers CONSISTENT
    (location); Calb1 APPROXIMATE; NT NOT_ASSESSED.
  reconciliation_note: >
    Paired with CS20230722_SUPT_0052 as primary; the calbindin pyramidal
    population partitions across both ENT-po Glut supertypes. The
    SUPT_0054 Calb1 mean being approximate while location and AT support
    are strong suggests either bimodal Calb1 distribution within the
    supertype's children or non-calbindin medial-EC L2 cells contaminating
    the AT scatter.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Supertype-level Calb1 mean=0.66 (cohort_pct 0.489) is approximate
        relative to the high-expression tier expected for a calbindin-
        defined classical type; child-cluster breakdown not assessed.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Small AT sample (n=42); scatter partner to CS20230722_SUPT_0052
        rather than independent line of evidence.
  proposed_experiments:
    - >
      Per-child-cluster Calb1 measurement across CS20230722_SUPT_0054
      children to test for a high-Calb1 subset consistent with the
      calbindin pyramidal type.
  unresolved_questions:
    - >
      Is the SUPT_0054 Calb1=0.66 mean driven by a low-Calb1 majority
      with a high-Calb1 subset, or by uniformly approximate Calb1 across
      all child clusters?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0035 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:WEAKEST] Lateral-EC layer 3 supertype with high Calb1=7.78
    (cohort_pct 0.967) and CONSISTENT location (region_fraction_100um=0.786,
    painted soma in entorhinal area lateral part layer 3). No annotation-
    transfer evidence supports this supertype: the analogous Yao 2021
    source label "L2/3 IT ENTl" maps onto a dentate gyrus supertype at n=2
    (likely source-side under-sampling, not refutation). 2 of 3 markers
    CONSISTENT (Calb1, location); NT NOT_ASSESSED. The classical calbindin
    patches are canonically medial-EC layer II; SUPT_0035 is lateral-EC
    layer 3 and likely represents a separate Calb1+ EC population rather
    than the canonical type.
  reconciliation_note: >
    Lateral-EC counterpart; unresolved between a true second-population
    inclusion and a wrong-subdivision call without a medial-EC-restricted
    source cohort.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Lateral-EC layer 3 placement differs from the classical medial-EC
        layer II location; mapping treats the supertype as a related but
        distinct Calb1+ EC population.
    - caveat_type: OTHER
      description: >
        No annotation-transfer evidence supports CS20230722_SUPT_0035;
        the source-side "L2/3 IT ENTl" label has only n=2 cells in the
        available run.
  proposed_experiments:
    - >
      Medial-EC-restricted scRNA-seq cohort mapped to WMBv1 to determine
      whether any medial-EC L2 calbindin cells land on CS20230722_SUPT_0035
      versus exclusively on the ENT-po supertypes.
  unresolved_questions:
    - >
      Is CS20230722_SUPT_0035 the lateral-EC homologue of the medial-EC
      calbindin pyramidal type, or a distinct lateral-EC L2/3 IT
      population?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0129 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Lateral-EC layer 3 cluster (child of CS20230722_SUPT_0035);
    Calb1=8.15 and location CONSISTENT but no AT evidence and lateral-EC
    placement is inconsistent with the classical medial-EC layer II patch
    population.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0259 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0259 sits in ENTmv with cortical amygdala
    (PA-COAp) admixture and a dominant layer 5 painted soma; the classical
    type is medial-EC layer II, so cross-region supertype membership and
    wrong-layer placement eliminate this candidate despite high Calb1=8.30.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0260 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Sibling of CS20230722_CLUS_0259 in the ENTmv-PA-COAp
    supertype; layer 3 painted soma rather than layer II and PA-COAp
    cross-region admixture eliminate the candidate despite Calb1=8.46.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0068 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Cross-region supertype mixing ENTmv with posterior amygdala
    and cortical amygdala (PA-COAp); the classical type is restricted to
    medial-EC layer II, so the cross-region admixture eliminates this
    candidate despite Calb1=8.38.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0329 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Parahippocampal (PPP) L2/3 IT cluster; the classical type
    is entorhinal cortex proper, not parahippocampal, and no AT evidence
    supports the mapping despite Calb1=8.07.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0014 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Endopiriform / claustrum (EP-CLA) cluster; wrong region and
    Calb1=1.76 (cohort_pct 0.573) is well below the high-expression tier
    expected for a calbindin-defined classical type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0010 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Lateral-EC layer 5/6 IT supertype; wrong layer (classical
    type is layer II) and Calb1=0.47 (cohort_pct 0.337) is below the
    detectable expression tier.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer2_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0067 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Sibling of CS20230722_SUPT_0068 in the ENTmv-PA-COAp
    cross-region supertype family; PA-COAp admixture eliminates the
    candidate despite Calb1=4.99 and CONSISTENT location.
```
<!-- verdict-block-end -->
