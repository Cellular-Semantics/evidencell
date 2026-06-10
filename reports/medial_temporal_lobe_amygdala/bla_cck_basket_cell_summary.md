# BLA CCK basket cell — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala CCK basket cell is a perisomatic-targeting GABAergic interneuron defined by cholecystokinin (CCK) expression, with absence of Pvalb. Vereczki et al. 2021 estimated CCK basket cells constitute 7–9% of GABAergic cells in the LA/BA. These cells modulate principal neuron activity through perisomatic inhibition and are distinguished from PV basket cells by their CCK+ / Pvalb- profile.

---

## Results

One candidate atlas cluster was assessed: CS20230722_CLUS_0664, carrying a `skos:closeMatch` at LOW confidence. MapMyCells annotation transfer (Hochgerner et al. 2023; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) maps GABA-54-Scng-Kcnc2 to CS20230722_CLUS_0664 with F1=0.59 at SUBCLASS and F1=0.06 at CLUSTER level (PARTIAL support). CCK is CONSISTENT but Pvalb-negative is NOT_ASSESSED.

### Mapping candidates table

| Rank | WMBv1 target | Confidence | Key alignment | Verdict |
|---|---|---|---|---|
| 1 | CS20230722_CLUS_0664 | 🔴 LOW | CCK CONSISTENT · neg-Pvalb NOT_ASSESSED · AT F1=0.06 (CLUSTER; PARTIAL) | `skos:closeMatch` |

#### Property alignment — CS20230722_CLUS_0664 · 🔴 LOW

| Property | Classical | Atlas | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT |
| CCK expression | CCK — defining | CCK CONSISTENT | CONSISTENT |
| Pvalb (negative) | absent | not in precomputed data | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports |
|---|---|---|
| WMBv1 atlas metadata | ATLAS_METADATA | SUPPORT |
| Hochgerner 2023 MapMyCells AT (GABA-54-Scng-Kcnc2, n=70) | ANNOTATION_TRANSFER | PARTIAL |

---

## Discussion

Cluster-level AT F1=0.06 is very weak (PARTIAL support), and subclass AT F1=0.59 is moderate. The weak cluster-level mapping suggests GABA-54-Scng-Kcnc2 does not specifically map to CS20230722_CLUS_0664. CCK is CONSISTENT, providing some marker support. The closeMatch predicate may require downgrading to broadMatch pending review of whether the classical CCK basket cell corresponds to CLUS_0664 specifically or to a broader clade. A second dataset with a more specific CCK basket cell capture would be required to strengthen this mapping.

---

<!-- verdict-block-start: edge_bla_cck_basket_cell_to_cs20230722_clus_0664 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.32
  rationale: >
    GABA-54-Scng-Kcnc2 maps with F1=0.59 (SUBCLASS) and F1=0.06 (CLUSTER)
    in `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` to
    CS20230722_CLUS_0664 (PARTIAL); 1 of 2 markers CONSISTENT
    (neuropeptide_Cck CONSISTENT; negative_marker_Pvalb NOT_ASSESSED).
    Cluster-level AT very weak (F1=0.06); closeMatch predicate requires
    review given weak cluster specificity.
  unresolved_questions:
    - "Is CS20230722_CLUS_0664 the correct cluster target, or does the CCK basket cell correspond to a broader subclass/supertype in CCN20230722?"
    - "Can Pvalb absence be confirmed in CS20230722_CLUS_0664 from precomputed stats?"
```
<!-- verdict-block-end -->
