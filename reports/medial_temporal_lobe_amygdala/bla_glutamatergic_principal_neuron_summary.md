# BLA glutamatergic principal neuron — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala glutamatergic principal neuron (BLA-PN) is the principal excitatory cell type of the BLA, expressing SLC17A7 (vGluT1) and CAMK2A. These cells receive sensory inputs, form associative memories, and project to multiple downstream regions including the nucleus accumbens, prefrontal cortex, and striatum. The classical type is defined by glutamatergic NT type with SLC17A7 and CAMK2A as defining markers, but these markers are broadly expressed across all cortical/hippocampal excitatory neurons, making specific atlas assignment challenging.

---

## Results

One candidate atlas supertype was assessed: CS20230722_SUPT_0005, carrying a `skos:broadMatch` at LOW confidence. MapMyCells annotation transfer (Hochgerner et al. 2023; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) maps VGLUT2-23-Nov_Gpr83 to CS20230722_SUPT_0005 with F1=0.30 at SUPERTYPE level (PARTIAL support; n=3 cells only). Both defining markers are NOT_ASSESSED.

### Mapping candidates table

| Rank | WMBv1 target | Confidence | Key alignment | Verdict |
|---|---|---|---|---|
| 1 | CS20230722_SUPT_0005 | 🔴 LOW | AT F1=0.30 (SUPERTYPE; PARTIAL; n=3) · SLC17A7, CAMK2A NOT_ASSESSED | `skos:broadMatch` |

#### Property alignment — CS20230722_SUPT_0005 · 🔴 LOW

| Property | Classical | Atlas | Alignment |
|---|---|---|---|
| NT type | Glutamatergic | Glutamatergic | CONSISTENT |
| SLC17A7 expression | SLC17A7 — positive | not in precomputed data | NOT_ASSESSED |
| CAMK2A expression | CAMK2A — positive | not in precomputed data | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports |
|---|---|---|
| WMBv1 atlas metadata | ATLAS_METADATA | SUPPORT |
| Hochgerner 2023 MapMyCells AT (VGLUT2-23-Nov_Gpr83, n=3) | ANNOTATION_TRANSFER | PARTIAL |

---

## Discussion

AT F1=0.30 is weak and n=3 cells is very small (PARTIAL support). Both defining markers are NOT_ASSESSED. The Hochgerner 2023 dataset is primarily a deep amygdala inhibitory neuron dataset and likely undersamples BLA principal neurons. This mapping is tenuous and requires a dedicated BLA excitatory neuron dataset for validation. The broadMatch to SUPT_0005 (IT EP-CLA Glut_3) is a working hypothesis only.

---

<!-- verdict-block-start: edge_bla_glutamatergic_principal_neuron_to_cs20230722_supt_0005 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.28
  rationale: >
    VGLUT2-23-Nov_Gpr83 maps with F1=0.30 (SUPERTYPE) in
    `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` to
    CS20230722_SUPT_0005 (PARTIAL; n=3 cells); 0 of 2 markers CONSISTENT
    (marker_SLC17A7, marker_CAMK2A both NOT_ASSESSED). Very weak AT
    from undersampled excitatory population in this dataset; mapping
    requires dedicated BLA excitatory neuron dataset.
  unresolved_questions:
    - "Does VGLUT2-23-Nov_Gpr83 specifically correspond to BLA principal neurons, or is this spurious mapping from a dataset that undersamples excitatory cells?"
    - "Is CS20230722_SUPT_0005 the correct supertype for BLA glutamatergic principal neurons, or are they distributed across multiple IT supertypes?"
```
<!-- verdict-block-end -->
