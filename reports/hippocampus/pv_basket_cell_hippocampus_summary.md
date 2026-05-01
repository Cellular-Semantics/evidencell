# Parvalbumin-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | basket cell (CL:0000118) | |
| Soma location | CA1 stratum pyramidale [UBERON:0005401]; CA3 stratum pyramidale [UBERON:0005401]; dentate gyrus granule cell layer [UBERON:0001885] | [1] [2] [3] [4] [1] [2] [3] [4] [1] [2] [3] [4] |
| NT | GABAergic | [5] |
| Markers | Pvalb+, Gad1+, Gad2+ | [1] [6] [7] [8] |
| Negative | Cnr1− | |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] |  | — | 🟡 MODERATE | Best candidate |
| 2 | 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] |  | — | 🟡 MODERATE | Best candidate |

All edges: `PARTIAL_OVERLAP`

---

## 0206 Pvalb Gaba_2 · 🟡 MODERATE

**Supporting evidence:**

- Pvalb subclass and GABA neurotransmitter type are fully consistent with PV basket cell identity. CA1 stratum oriens (818 cells) and CA3 stratum oriens (152 cells) include appropriate perisomatic interneuron locations; however, the supertype also spans piriform area (959 cells), indicating it is not hippocampus-specific. Defining markers (Cort, Adamts15, Vwc2l, Ets1) do not include Pvalb directly but Pvalb is prominent in child cluster MERFISH data. The supertype name "Pvalb Gaba_2" is consistent with PV+ identity. Partial overlap declared because (a) the supertype spans multiple regions beyond hippocampus and (b) the PV basket cell is one of several PV+ morphological subtypes (basket, axo-axonic, bistratified) that share high transcriptomic similarity and may not be separable at supertype level. [Atlas metadata]
- Precomputed stats cross-check: all 3 defining markers confirmed (Pvalb=8.74, Gad1=10.34, Gad2=9.28) and negative marker Cnr1 absent (1.93). Strong quantitative support for PV basket identity in this supertype. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) mouse hippocampus SSv4 Pvalb subclass label (n=66 HIP cells) onto WMBv1 (CCN20230722). At SUBCLASS level, Pvalb cells split equally between SUBC_051 (Pvalb chandelier, F1=0.588, 25 cells) and SUBC_052 (Pvalb Gaba, F1=0.588, 25 cells). At SUPERTYPE level, SUPT_0204 chandelier (F1=0.612, 26 cells) is stronger than SUPT_0206 Pvalb Gaba_2 (F1=0.324, 12 cells). SUPT_0206 receives 12/66 Pvalb cells, with target_purity=0.800 (80% of mapped SUPT_0206 cells are Pvalb). PARTIAL because the SSv4 Pvalb label is a mixed population; chandelier/AAC cells likely dominate the mapping, reflecting enrichment in the Yao dataset. Yao 2021 SSv4 'Pvalb' subclass label (n=66 HIP cells) encompasses PV basket, axo-axonic, and bistratified cells; subtype resolution requires a morphologically identified PV-IN dataset. [Annotation transfer]

**Concerns:**

- **location_CA1_stratum_pyramidale** (APPROXIMATE): A=CA1 stratum pyramidale (UBERON:0005401) — soma / B=CA1 stratum oriens (MBA:399, 818 cells); CA1 pyramidal layer not listed. Classical soma location is stratum pyramidale; atlas shows CA1 SO as dominant hippocampal location. Both are perisomatic layers; some soma placement discrepancy may reflect soma-in-SO border cells or atlas resolution limits.

- **marker_Gad1** (APPROXIMATE): A=Gad1 — defining marker / B=not present in supertype defining_markers; GABA nt_type consistent; precomputed stats mean: 10.34. 
- **marker_Gad2** (APPROXIMATE): A=Gad2 — defining marker / B=not present in supertype defining_markers; GABA nt_type consistent; precomputed stats mean: 9.28. 
- Supertype spans hippocampus (CA1 SO, CA3 SO) and piriform area; not hippocampus-specific. Multiple PV+ morphological subtypes (basket, axo-axonic, bistratified) co-populate the Pvalb Gaba subclass with high transcriptomic similarity (Bomkamp et al. 2019 PMID:33398060) and may not be separable at supertype level.
- Cnr1 negative marker status unverifiable from atlas supertype metadata.

---

## 0739 Pvalb Gaba_2 · 🟡 MODERATE

**Supporting evidence:**

- Child of SUPT_0206 (Pvalb Gaba_2). Hippocampal enrichment: CA1 SO (124 cells), CA3 SO (80 cells), CA1 pyramidal layer (26 cells), CA1 SR (45 cells). GABA consistent. Pvalb in MERFISH markers confirms PV identity. Neuropeptides include Cck (score 7.6), Pthlh, Cort, Tac1 — no Cck association expected for PV basket cells; Cck is a defining marker of CCK basket cells. This neuropeptide profile is discordant and suggests the cluster may contain mixed PV+/CCK+ identities, or that Cck peptide co-expression occurs at low level in some PV neurons. Partial overlap declared for same reasons as parent supertype. [Atlas metadata]
- Precomputed stats cross-check: Pvalb=10.63, Gad1=10.52, Gad2=8.43, Cnr1=1.68 (absent). Strongest Pvalb expression among SUPT_0206 child clusters. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Pvalb subclass (n=66 HIP cells) onto WMBv1. At CLUSTER level, CLUS_0739 (Pvalb Gaba_2) receives 5/66 Pvalb cells (F1=0.179, target_purity=1.0), with CLUS_0732 (chandelier) as the dominant cluster hit (F1=0.622, 23 cells). PARTIAL because the SSv4 Pvalb label is a mixed population; chandelier/AAC cells are the dominant contributor. Yao 2021 SSv4 'Pvalb' subclass label (n=66 HIP cells) encompasses PV basket, axo-axonic, and bistratified cells; subtype resolution requires a morphologically identified PV-IN dataset. [Annotation transfer]

**Concerns:**

- **location_CA1_stratum_pyramidale** (APPROXIMATE): A=CA1 stratum pyramidale (UBERON:0005401) — soma / B=CA1 pyramidal layer (MBA:407, 26 cells); CA1 SO (MBA:399, 124 cells). Small CA1 pyramidal layer count; main hippocampal signal in SO.
- **marker_Gad1** (APPROXIMATE): A=Gad1 — defining marker / B=not in cluster defining_markers; GABA NT consistent; precomputed stats mean: 10.52. 
- **marker_Gad2** (APPROXIMATE): A=Gad2 — defining marker / B=not in cluster defining_markers; GABA NT consistent; precomputed stats mean: 8.43. 
- **neuropeptide_Cck** (DISCORDANT): A=Cck not expected (Cnr1-negative PV cells) / B=Cck present (expression score 7.6); precomputed stats mean: 7.56. High Cck neuropeptide score is unexpected for a PV basket cell, which should be Cnr1/CB1R-negative. Could indicate cluster contains CCK-co-expressing PV cells, or that cluster boundaries do not align cleanly to classical types.

- Cck neuropeptide at high expression score in this cluster is discordant with expected PV basket cell identity (Cnr1-negative). May indicate mixed cluster content or non-specific peptide expression.
- PV+ hippocampal interneurons (basket, axo-axonic, bistratified) have high transcriptomic similarity and are not cleanly separated at cluster level (PMID:33398060). This cluster likely contains multiple classical PV subtypes.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206 | Atlas metadata | PARTIAL |
| edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206 | Atlas metadata | SUPPORT |
| edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206 | Annotation transfer | PARTIAL |
| edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739 | Atlas metadata | PARTIAL |
| edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739 | Atlas metadata | SUPPORT |
| edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 · PMID:25018703 | [25018703](https://pubmed.ncbi.nlm.nih.gov/25018703/) | soma location |
| [2] | Sik et al. 1995 · PMID:7472426 | [7472426](https://pubmed.ncbi.nlm.nih.gov/7472426/) | soma location |
| [3] | Müller & Remy 2014 · PMID:25324774 | [25324774](https://pubmed.ncbi.nlm.nih.gov/25324774/) | soma location |
| [4] | Bocchio et al. 2024 · PMID:39401246 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | soma location |
| [5] | Whissell et al. 2015 · PMID:26441554 | [26441554](https://pubmed.ncbi.nlm.nih.gov/26441554/) | neurotransmitter type |
| [6] | Que et al. 2021 · PMID:33398060 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060/) | Pvalb marker |
| [7] | Perrenoud et al. 2022 · PMID:35802727 | [35802727](https://pubmed.ncbi.nlm.nih.gov/35802727/) | Pvalb marker |
| [8] | Contreras et al. 2019 · PMID:31297048 | [31297048](https://pubmed.ncbi.nlm.nih.gov/31297048/) | Pvalb marker |
