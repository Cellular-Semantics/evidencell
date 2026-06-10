# BLA GABAergic projection neuron — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala GABAergic projection neuron (BLA-GP) is a long-range inhibitory projection neuron expressing somatostatin (Sst) and neuronal nitric oxide synthase (Nos1), distinguished from local interneurons by its axonal projections outside the BLA. Vereczki et al. 2021 estimated this type constitutes 5.5–8% of GABAergic cells in the LA/BA. The BLA-GP is notable for its co-expression of Sst and Nos1 with absence of Pvalb, distinguishing it from PV+ basket cells and interneurons.

---

## Results

One candidate atlas cluster was assessed: CS20230722_CLUS_0850, carrying a `skos:broadMatch` at LOW confidence. MapMyCells annotation transfer (Hochgerner et al. 2023; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) maps GABA-37-Sst-Npy to CS20230722_CLUS_0850 with F1=0.92 at SUBCLASS and F1=0.22 at CLUSTER level. All three markers are CONSISTENT, providing strong marker-level support despite weak cluster-level AT.

### Mapping candidates table

| Rank | WMBv1 target | Confidence | Key alignment | Verdict |
|---|---|---|---|---|
| 1 | CS20230722_CLUS_0850 | 🔴 LOW | Sst CONSISTENT · Nos1 CONSISTENT · neg-Pvalb CONSISTENT · AT F1=0.92 (SUBCLASS) | `skos:broadMatch` |

#### Property alignment — CS20230722_CLUS_0850 · 🔴 LOW

| Property | Classical | Atlas | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT |
| Sst expression | Sst — positive | Sst CONSISTENT | CONSISTENT |
| Nos1 expression | Nos1 — positive | Nos1 CONSISTENT | CONSISTENT |
| Pvalb (negative) | absent | absent | CONSISTENT |

**Evidence support**

| Evidence | Type | Supports |
|---|---|---|
| WMBv1 atlas metadata | ATLAS_METADATA | SUPPORT |
| Hochgerner 2023 MapMyCells AT (GABA-37-Sst-Npy, n=22) | ANNOTATION_TRANSFER | SUPPORT |

---

## Discussion

All three markers are CONSISTENT, providing strong molecular support. However, cluster-level AT F1=0.22 is weak, with the mapping primarily resolved at SUBCLASS (F1=0.92). This suggests the classical BLA-GP is a heterogeneous population broadly corresponding to the "Sst Chodl" subclass rather than specifically to CLUS_0850. The broadMatch predicate is appropriate; upgrading to MODERATE would require literature evidence identifying specific cluster-level features distinguishing BLA-GPs from other Sst/Nos1+ cells.

---

<!-- verdict-block-start: edge_bla_gabaergic_projection_neuron_to_cs20230722_clus_0850 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.45
  rationale: >
    GABA-37-Sst-Npy maps with F1=0.92 (SUBCLASS) and F1=0.22 (CLUSTER)
    in `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` to
    CS20230722_CLUS_0850; 3 of 3 markers CONSISTENT (marker_Sst,
    marker_Nos1, negative_marker_Pvalb). Cluster-level AT weak (F1=0.22);
    broadMatch retained: classical type likely broader than this specific cluster.
  unresolved_questions:
    - "Is CS20230722_CLUS_0850 specifically the long-range projection subtype, or does GABA-37-Sst-Npy include multiple functional subtypes?"
    - "Can Nos1 expression be confirmed at protein level in the target cluster from atlas precomputed data?"
```
<!-- verdict-block-end -->
