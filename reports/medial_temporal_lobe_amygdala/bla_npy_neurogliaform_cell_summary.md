# BLA NPY neurogliaform cell — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala NPY neurogliaform cell is a GABAergic interneuron characterised by NPY expression and a neurogliaform morphology with dense local axonal arborisation. Vereczki et al. 2021 estimated this type constitutes 14–15% of GABAergic cells in the LA/BA, where it forms a major interneuron class alongside basket and somatostatin-positive cells. The classical definition relies on NPY as a positive marker with absence of Pvalb and Sst as negative markers. These cells are known for volume transmission and neuromodulatory roles through NPY release.

---

## Results

One candidate atlas cluster was assessed: CS20230722_CLUS_0710, carrying an `evidencell:UncertainRelationship` at LOW confidence. MapMyCells annotation transfer (Hochgerner et al. 2023; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) maps GABA-46-Lamp5-Kit to CS20230722_CLUS_0710 with F1=0.98 at SUPERTYPE and F1=0.57 at CLUSTER level, suggesting the classical type maps broadly to the parent supertype rather than specifically to this cluster.

### Mapping candidates table

| Rank | WMBv1 target | Confidence | Key alignment | Verdict |
|---|---|---|---|---|
| 1 | CS20230722_CLUS_0710 | 🔴 LOW | NPY CONSISTENT · neg-Pvalb CONSISTENT · neg-Sst DISCORDANT · AT F1=0.98 (SUPERTYPE) | `evidencell:UncertainRelationship` |

#### Property alignment — CS20230722_CLUS_0710 · 🔴 LOW

| Property | Classical | Atlas | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT |
| NPY expression | Npy — positive | Npy CONSISTENT in cluster | CONSISTENT |
| Pvalb (negative) | absent | absent | CONSISTENT |
| Sst (negative) | absent | present in atlas cluster | DISCORDANT |

**Evidence support**

| Evidence | Type | Supports |
|---|---|---|
| WMBv1 atlas metadata | ATLAS_METADATA | SUPPORT |
| Hochgerner 2023 MapMyCells AT (GABA-46-Lamp5-Kit, n=167) | ANNOTATION_TRANSFER | SUPPORT |

---

## Discussion

AT F1=0.98 at SUPERTYPE level is strong but F1=0.57 at CLUSTER level is moderate, indicating the source cluster GABA-46-Lamp5-Kit distributes across multiple clusters within the supertype. The negative_marker_Sst DISCORDANT alignment is a concern. The `evidencell:UncertainRelationship` predicate reflects unresolved taxonomy-level uncertainty; the evidence supports at least a broadMatch to the parent supertype if the Sst discordancy can be explained. Upgrading to broadMatch at SUPERTYPE would require literature confirmation that NPY neurogliaform cells specifically populate the BLA in the Lamp5-Kit clade.

---

<!-- verdict-block-start: edge_bla_npy_neurogliaform_cell_to_cs20230722_clus_0710 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.40
  rationale: >
    GABA-46-Lamp5-Kit maps with F1=0.98 (SUPERTYPE) and F1=0.57 (CLUSTER)
    in `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` to
    CS20230722_CLUS_0710; 2 of 3 markers CONSISTENT (neuropeptide_Npy,
    negative_marker_Pvalb CONSISTENT; negative_marker_Sst DISCORDANT).
    Predicate `evidencell:UncertainRelationship` retained pending review;
    cluster-level AT moderate (F1=0.57).
  unresolved_questions:
    - "Does the BLA component of CS20230722_CLUS_0710 correspond to NPY neurogliaform cells? Predicate should be upgraded to broadMatch if confirmed."
    - "Why is negative_marker_Sst DISCORDANT? Is there Sst co-expression in the Lamp5-Kit cluster?"
```
<!-- verdict-block-end -->
