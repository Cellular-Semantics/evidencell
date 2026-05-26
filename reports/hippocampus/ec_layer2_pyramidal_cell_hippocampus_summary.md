# Entorhinal cortex layer II calbindin-positive pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-05-19 · Source: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

## Introduction

The entorhinal cortex layer II calbindin-positive pyramidal cell (EC layer II pyramidal cell) is the complementary principal neuron type to the reelin-positive stellate cell in EC layer II. Unlike stellate cells, EC layer II pyramidal cells express calbindin (Calb1) and project primarily to CA1 rather than to the dentate gyrus [4]. They are arranged in a characteristic hexagonal patch grid in medial EC [4], show strong theta modulation, and give rise to widespread telencephalic and intrinsic projections [1]. At least half originate local intrinsic and commissural projections distributing mainly to layers I and II [1]. Mapping this population to WMBv1 is supported by annotation transfer evidence, though the small sample of medial EC cells in the Yao 2021 SSv4 dataset (n=42 L2 IT ENTm cells) limits statistical confidence.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Entorhinal cortex [UBERON:0002728] layer II | [1][2][3] |
| NT | Glutamatergic | [4] |
| Defining markers | Calb1 (calbindin) | [4][5] |
| Negative markers | — | |
| Neuropeptides | — | |
| CL term | pyramidal neuron [CL:0000598] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **CB+ layer II pyramidal cells: diverse excitatory projections, local intrinsic and commissural projections** [1]
  > the layer II CB+ population comprises neurons with diverse, mainly excitatory projections. At least half of them originate local intrinsic and commissural projections which distribute mainly to layer I and II
  > — Unknown 2019 · [1] <!-- quote_key: 204538361_555db016 -->

- **Calb1 as pyramidal cell marker: ~88% of calbindin-positive cells are glutamatergic; periodic patch arrangement** [4]
  > In the rodent entorhinal cortex, $88% of calbindin-positive cells are glutamatergic
  > — Naumann et al. 2015 · [4] <!-- quote_key: 10060696_f4cc1f5f -->

  > We confirm the existence of patches of calbindin‐positive pyramidal cells across these species, arranged periodically
  > — Naumann et al. 2015 · [4] <!-- quote_key: 10060696_93c3874e -->

- **Two EC layer II types: Reln+ stellate (→DG/CA3) and Calb1+ pyramidal (→CA1)** [5][2]
  > Principal neurons in entorhinal cortex layer II are of two types, stellate-like neurons and pyramidal neurons, the former of which express reelin, whereas the latter include a large population of calbindin-expressing neurons (Ohara et al., 2021)(Varga et al., 2010)(Fuchs et al., 2016)(Ohara et al., 2019)(Zutshi et al., 2018).
  > — Unknown 2018 · [5] <!-- quote_key: 10189534_9b25e78b -->

- **Grid and head-direction cells in medial EC layer II: role of locally projecting pyramidal cells** [2]
  > optogenetically perturb locally projecting layer II pyramidal cells. We find that sharply tuned HD cells are only weakly responsive while speed, broadly tuned HD cells, and grid cells show pronounced transient excitatory and inhibitory responses
  > — Unknown 2018 · [2] <!-- quote_key: 52194250_dabdef57 -->

</details>

Cell Ontology mapping: pyramidal neuron [[CL:0000598](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000598)] (BROAD). No EC layer II pyramidal-specific CL term exists; CL:0000598 is the best available match.

---

## Results

One annotation-transfer run informs this node. Yao 2021 (GSE185862) 'L2 IT ENTm' subclass cells (medial EC layer II IT neurons, principally Calb1+ pyramidal cells) map primarily to WMBv1 supertype 0052 L2 IT ENT-po Glut_2 [CS20230722_SUPT_0052] (F1=0.694, group_purity=0.595, target_purity=0.833). The sample is small (n=42) and results should be interpreted with appropriate caution.

**Note on filtered AT figure:** A filtered AT figure could not be generated for this node. The source label "L2 IT ENTm" is not present in the SSv4 CSV used for filtered figure generation — the SSv4 dataset (GEO:GSE185862) has very few medial EC cells. No figure is embedded here.

### Mapping candidates table

| Rank | WMBv1 supertype | Cells (WMBv1) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| 1 | 0052 L2 IT ENT-po Glut_2 [CS20230722_SUPT_0052] | 857 | 🟡 MODERATE | NT CONSISTENT · Calb1 mean=7.14 · F1=0.694 · location APPROXIMATE | Best candidate |

Total: 1 edge; relationship PARTIAL_OVERLAP. *(note: SUPT_0054 captures a further 33.3% of L2 IT ENTm cells, suggesting a TYPE_A_SPLITS relationship; a secondary edge to SUPT_0054 is pending.)*

### Primary candidate property alignment — 0052 L2 IT ENT-po Glut_2 [CS20230722_SUPT_0052] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Atlas supertype | Alignment |
|---|---|---|---|
| NT type | Glutamatergic | Glutamatergic (SUBC_011 L2 IT ENT-po Glut) | CONSISTENT |
| Soma location | Entorhinal cortex [UBERON:0002728] layer II | SUPT_0052 in L2 IT ENT-po (entorhinal postrhinal) subclass | APPROXIMATE |
| Calb1 (defining marker) | Pyramidal cell identity; ~88% of Calb1+ EC cells are glutamatergic [4] | Not in atlas discriminating markers (Ush2a, Dcn); mean_expression=7.14 (precomputed_stats.h5) | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Yao 2021 (GSE185862) MapMyCells, L2 IT ENTm (n=42) | Annotation transfer | SUPPORT | F1=0.694, group_purity=0.595, target_purity=0.833; 59.5% of L2 IT ENTm cells | at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1 |

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0052 belongs to subclass SUBC_011 L2 IT ENT-po Glut, a glutamatergic layer II IT subclass grouping medial EC and postrhinal cortex neurons. The classical EC layer II Calb1+ pyramidal cell is glutamatergic [4].

- **Annotation transfer — SUPPORT.** MapMyCells local AT of Yao 2021 (GEO:GSE185862) 'L2 IT ENTm' cells (n=42, medial EC layer II IT neurons, principally Calb1+ pyramidal cells) onto WMBv1: 25 (59.5%) map to SUPT_0052, F1=0.694, group_purity=0.595, target_purity=0.833. SUPT_0054 accounts for a further 33.3%; together SUPT_0052 and SUPT_0054 cover 92.8% of L2 IT ENTm cells. *Note: n=42 is a small sample; the moderate F1 may reflect biological heterogeneity or sampling noise.*

- **Marker Calb1 — CONSISTENT.** Calb1 is the defining pyramidal cell identity marker [4][5]. Precomputed expression stats confirm Calb1 mean=7.14 in SUPT_0052. Calb1 is not among the atlas discriminating markers for SUPT_0052 (Ush2a, Dcn), but the quantitative value is consistent with calbindin expression in this population.

- **Location — APPROXIMATE.** The 'ENT-po' (entorhinal postrhinal) subclass spans medial EC and postrhinal cortex. Classical EC layer II pyramidal cells are restricted to medial EC [UBERON:0002728]; postrhinal cortex is a distinct but adjacent area. The ENT-po grouping likely reflects transcriptomic similarity between adjacent posterior cortical regions.

**Concerns**

- **Small sample size (n=42).** Only 42 L2 IT ENTm cells in Yao 2021 (GEO:GSE185862). The moderate F1=0.694 and lower group_purity=0.595 could reflect biological heterogeneity or sampling noise. Additional medial EC cells from a larger HPF dataset would substantially improve confidence.

- **TYPE_A_SPLITS — secondary edge to SUPT_0054 pending.** SUPT_0054 captures 33.3% of L2 IT ENTm cells (F1=0.500); a secondary edge is appropriate when more data become available.

- **Location APPROXIMATE — postrhinal component.** The ENT-po subclass spans medial EC and postrhinal cortex. Any postrhinal component in SUPT_0052 would represent a different population.

**What would upgrade confidence**

- Obtain a larger HPF dataset with sufficient medial EC layer II coverage (target n > 100 L2 IT ENTm-equivalent cells) and re-run MapMyCells AT to WMBv1. Target: F1 ≥ 0.80 at SUPERTYPE level.
- Run add-expression for Calb1 and Reln across SUBC_011 (ENT-po) and SUBC_009 (PIR-ENTl) supertypes to confirm the pyramidal/stellate molecular distinction at the atlas level. No new experiments required.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The EC layer II calbindin-positive pyramidal cell is defined on a CLASSICAL_MULTIMODAL basis: soma in entorhinal cortex [UBERON:0002728] layer II [1][2][3]; glutamatergic [4]; defining marker Calb1 (calbindin; pyramidal cell identity, CA1 projection) [4][5]; characteristic periodic patch arrangement in medial EC [4].

**Atlas mapping query.** Candidate atlas clusters retrieved from WMBv1 (CCN20230722) at rank 1 (supertype) using NT type (glutamatergic) and region (entorhinal cortex) as primary filters.

**Property alignment.** Alignments graded CONSISTENT / APPROXIMATE. Calb1 atlas value from precomputed_stats.h5 (supertype level).

**Annotation transfer.**

Run 1 — Yao 2021 SSv4 hippocampal formation → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse HPF SMART-Seq v4) |
| Source group | L2 IT ENTm subclass (Yao 2021 Allen Institute taxonomy) |
| n cells (L2 IT ENTm) | 42 |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default params, raw norm, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| n cells total | 6,398 |
| Run record | `kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/` |
| F1 matrix | `f1_scores_best.csv` |
| Caveats | Small sample (n=42). No filtered AT figure available: source label "L2 IT ENTm" not present in SSv4 CSV — SSv4 dataset has very few medial EC cells. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes are validated against the evidencell knowledge base at write time.

*Generated by evidencell `07c6dbd` at 2026-05-19 from `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`.*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_ec_layer2_pyramidal_cell_hippocampus_to_supt_0052 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862) | SUPPORT — F1=0.694; group_purity=0.595; target_purity=0.833; 59.5% of L2 IT ENTm cells; n=42 (small sample) | at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1 |

</details>

---

## Discussion

**Primary mapping: EC layer II calbindin-positive pyramidal cell → 0052 L2 IT ENT-po Glut_2 [CS20230722_SUPT_0052] · MODERATE.** The Yao 2021 (GEO:GSE185862) annotation transfer of 42 'L2 IT ENTm' cells maps 59.5% to SUPT_0052 (F1=0.694, group_purity=0.595, target_purity=0.833), with SUPT_0054 capturing a further 33.3%. Together these two supertypes cover 92.8% of L2 IT ENTm cells, suggesting a TYPE_A_SPLITS relationship. Calb1 mean=7.14 in SUPT_0052 (precomputed_stats.h5) is consistent with calbindin expression in this population.

The core limitation is sample size: only 42 medial EC layer II cells in the Yao 2021 SSv4 dataset. The moderate F1 and lower group_purity may reflect genuine biological heterogeneity (consistent with a TYPE_A_SPLITS to SUPT_0052 and SUPT_0054) or sampling noise. The 'ENT-po' subclass designation spans medial EC and postrhinal cortex, introducing an APPROXIMATE location caveat. A filtered AT figure could not be generated for this node — the SSv4 dataset lacks sufficient medial EC cells to populate the source label in the SSv4 CSV.

The Cell Ontology has no EC layer II pyramidal-specific CL term; pyramidal neuron [CL:0000598] is used as BROAD mapping.

### Proposed experiments

1. **Obtain a larger HPF dataset with medial EC layer II coverage** (target n > 100 L2 IT ENTm-equivalent cells) and re-run MapMyCells AT to WMBv1. Target: F1 ≥ 0.80. This is the highest-priority step for upgrading confidence.

2. **Add-expression for Calb1 and Reln across SUBC_011 (ENT-po) and SUBC_009 (PIR-ENTl) supertypes** to confirm the Calb1-high/Reln-low (pyramidal) vs. Reln-high/Calb1-low (stellate) distinction at the atlas level. No new experiments required.

3. **Add secondary edge to SUPT_0054** (F1=0.500, 33.3% of L2 IT ENTm cells) to complete the TYPE_A_SPLITS representation; requires only curation effort.

### Open questions

1. Does Calb1 expression distinguish SUPT_0052 (pyramidal, Calb1+) from SUPT_0042 (stellate, Reln+) at the atlas level? Running add-expression for Calb1 and Reln across SUBC_011 (ENT-po) and SUBC_009 (PIR-ENTl) supertypes would resolve this without new experiments.
2. Is the moderate F1=0.694 a reflection of genuine biological heterogeneity within medial EC layer II pyramidal cells (TYPE_A_SPLITS to SUPT_0052 and SUPT_0054), or primarily sampling noise from the small n=42?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2019 · PMID:31680885 | [31680885](https://pubmed.ncbi.nlm.nih.gov/31680885/) | soma location; CB+ pyramidal cell projections |
| [2] | Unknown 2018 · PMID:30209250 | [30209250](https://pubmed.ncbi.nlm.nih.gov/30209250/) | soma location; locally projecting pyramidal cells in MEC |
| [3] | Unknown 2021 · PMID:34949991 | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991/) | soma location |
| [4] | Naumann et al. 2015 · PMID:26223342 | [26223342](https://pubmed.ncbi.nlm.nih.gov/26223342/) | NT type; Calb1 marker; periodic patch arrangement |
| [5] | Unknown 2010 · PMID:20512133 | [20512133](https://pubmed.ncbi.nlm.nih.gov/20512133/) | Calb1 marker; Reln+/Calb1+ two-cell-type distinction |
