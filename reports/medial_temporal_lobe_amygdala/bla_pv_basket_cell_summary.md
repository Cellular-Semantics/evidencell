# BLA PV basket cell — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala parvalbumin (PV) basket cell is a perisomatic-targeting GABAergic interneuron defined by strong Pvalb expression and absence of Sst. Vereczki et al. 2021 estimated PV basket cells constitute 17–20% of GABAergic cells in the LA/BA. These fast-spiking cells provide powerful perisomatic inhibition onto principal neuron soma and proximal dendrites. Their Pvalb+ / Sst- profile distinguishes them from the closely related axo-axonic cell (also Pvalb+) and from Sst+ dendrite-targeting interneurons.

---

## Results

One candidate atlas cluster was assessed: CS20230722_CLUS_0738, carrying a `skos:broadMatch` at LOW confidence. MapMyCells annotation transfer (Hochgerner et al. 2023; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) maps GABA-41-Moxd1-Pvalb to CS20230722_CLUS_0738 with F1=0.74 at CLUSTER level. The defining marker Pvalb is CONSISTENT.

### Mapping candidates table

| Rank | WMBv1 target | Confidence | Key alignment | Verdict |
|---|---|---|---|---|
| 1 | CS20230722_CLUS_0738 | 🔴 LOW | Pvalb CONSISTENT · AT F1=0.74 (CLUSTER) | `skos:broadMatch` |

#### Property alignment — CS20230722_CLUS_0738 · 🔴 LOW

| Property | Classical | Atlas | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT |
| Pvalb expression | Pvalb — defining | Pvalb CONSISTENT | CONSISTENT |
| Sst (negative) | absent | not in precomputed data | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports |
|---|---|---|
| WMBv1 atlas metadata | ATLAS_METADATA | SUPPORT |
| Hochgerner 2023 MapMyCells AT (GABA-41-Moxd1-Pvalb, n=58) | ANNOTATION_TRANSFER | SUPPORT |

---

## Discussion

Cluster-level AT F1=0.74 is near but below the 0.75 threshold for strong support. Pvalb is CONSISTENT. The broadMatch predicate reflects that BLA PV basket cells likely correspond to a subset of CS20230722_CLUS_0738, which is a pan-cortical Pvalb+ cluster (similar to the chandelier CLUS_0733 situation). The F1=0.74 provides near-threshold evidence; upgrading to MODERATE would require either reaching F1=0.75 with additional AT data or literature evidence specifically linking GABA-41-Moxd1-Pvalb to BLA basket morphology.

---

<!-- verdict-block-start: edge_bla_pv_basket_cell_to_cs20230722_clus_0738 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.45
  rationale: >
    GABA-41-Moxd1-Pvalb maps with F1=0.74 (CLUSTER) in
    `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` to
    CS20230722_CLUS_0738; 1 of 2 markers CONSISTENT (marker_Pvalb
    CONSISTENT; negative_marker_Sst NOT_ASSESSED). Cluster-level AT
    near threshold (F1=0.74); broadMatch retained pending pan-cortical
    cluster specificity review.
  unresolved_questions:
    - "Can Sst absence be confirmed in CS20230722_CLUS_0738 from precomputed stats, distinguishing PV basket from PV+ chandelier cells in BLA?"
    - "Is the BLA component (~4%?) of CS20230722_CLUS_0738 specifically perisomatic-targeting basket cells or does it include chandelier cells?"
```
<!-- verdict-block-end -->
