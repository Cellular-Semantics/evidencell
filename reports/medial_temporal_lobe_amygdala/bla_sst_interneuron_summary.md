# BLA SST interneuron — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala somatostatin (SST) interneuron is a dendrite-targeting GABAergic interneuron defined by somatostatin (Sst) expression and co-expression of calbindin (Calb1). Vereczki et al. 2021 estimated Sst-expressing interneurons constitute 10–16% of GABAergic cells in the LA/BA. These cells predominantly target dendrites of principal neurons and play key roles in gating plasticity and fear memory. The absence of Pvalb distinguishes them from axo-axonic and basket cells.

---

## Results

One candidate atlas cluster was assessed: CS20230722_CLUS_0765, carrying a `skos:broadMatch` at LOW confidence. MapMyCells annotation transfer (Hochgerner et al. 2023; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) maps GABA-38-Sst-Tmtc4 to CS20230722_CLUS_0765 with F1=0.76 at SUPERTYPE and F1=0.30 at CLUSTER level. Two of three markers are CONSISTENT.

### Mapping candidates table

| Rank | WMBv1 target | Confidence | Key alignment | Verdict |
|---|---|---|---|---|
| 1 | CS20230722_CLUS_0765 | 🔴 LOW | Sst CONSISTENT · Calb1 CONSISTENT · AT F1=0.76 (SUPERTYPE) | `skos:broadMatch` |

#### Property alignment — CS20230722_CLUS_0765 · 🔴 LOW

| Property | Classical | Atlas | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT |
| Sst expression | Sst — positive | Sst CONSISTENT | CONSISTENT |
| Calb1 expression | Calb1 — positive | Calb1 CONSISTENT | CONSISTENT |
| Pvalb (negative) | absent | not in precomputed data | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports |
|---|---|---|
| WMBv1 atlas metadata | ATLAS_METADATA | SUPPORT |
| Hochgerner 2023 MapMyCells AT (GABA-38-Sst-Tmtc4, n=59) | ANNOTATION_TRANSFER | SUPPORT |

---

## Discussion

Supertype AT F1=0.76 meets the 0.75 threshold, and both Sst and Calb1 are CONSISTENT. However, cluster-level AT F1=0.30 is weak, indicating the classical SST interneuron population distributes across multiple clusters within the supertype. The broadMatch predicate is appropriate. To upgrade to MODERATE, either a closeMatch predicate revision or strong literature linking GABA-38-Sst-Tmtc4 specifically to BLA Sst interneurons would be required.

---

<!-- verdict-block-start: edge_bla_sst_interneuron_to_cs20230722_clus_0765 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.45
  rationale: >
    GABA-38-Sst-Tmtc4 maps with F1=0.76 (SUPERTYPE) and F1=0.30 (CLUSTER)
    in `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` to
    CS20230722_CLUS_0765; 2 of 3 markers CONSISTENT (neuropeptide_Sst,
    marker_Calb1 CONSISTENT; negative_marker_Pvalb NOT_ASSESSED).
    Supertype AT meets threshold but cluster-level AT is weak; broadMatch
    retained.
  unresolved_questions:
    - "Is CS20230722_CLUS_0765 specifically the dendrite-targeting SST subtype, or does GABA-38-Sst-Tmtc4 span multiple Sst+ subtypes in the BLA?"
    - "Can Pvalb absence be confirmed in CS20230722_CLUS_0765 from precomputed stats?"
```
<!-- verdict-block-end -->
