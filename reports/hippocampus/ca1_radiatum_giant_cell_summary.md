# CA1 radiatum giant cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA1 stratum radiatum [UBERON:0005372]; CA1 stratum lacunosum-moleculare (apical dendritic arborization) [UBERON:0014557]; subiculum (axon projection target) [UBERON:0002191] | [1] [2] [1] [1] |
| NT | glutamatergic | [1] |
| Markers |  |  |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | CS20230722_CLUS_0261 |  | — | 🔴 LOW | Speculative |
| 2 | CS20230722_SUPT_0069 |  | — | 🔴 LOW | Speculative |

All edges: `PARTIAL_OVERLAP`

---

## CS20230722_CLUS_0261 · 🔴 LOW

**Supporting evidence:**

- CLUS_0261 (0261 CA1-ProS Glut_1) has the correct NT type (Glut) and includes cells in CA1 stratum radiatum (MBA:415, n=71 across Yao 2024 and Zhuang 2023 MERFISH). However stratum radiatum is not the dominant soma location — most cells fall in CA1 stratum oriens (MBA:399, n=284) and pyramidal layer (MBA:407, n=136). The cluster spans CA1, ProS, and some CA2/CA3, indicating a broad CA1-proximal glutamatergic population rather than the radiatum-restricted RGC specifically. No marker overlap can be assessed (classical node has no defined molecular markers). [Atlas metadata]
- Kirson & Yaari (2000) define the RGC by its exclusively radiatum soma, myelinated axon, and NMDA-dependent burst firing. The MERFISH data for CLUS_0261 shows a subset of cells in stratum radiatum consistent with the classical location, but the cluster spans multiple laminae and subfields, suggesting the RGC is at most a minor component of this broad cluster. [Literature] [1]
- Nasrallah et al. (2019) confirm the mouse RGC morphology and identify CA2 pyramidal neurons as a strong presynaptic input. CLUS_0261 includes cells in CA2 subfields, which may reflect CA2-adjacent glutamatergic neurons grouped with the RGC in this broad cluster. [Literature] [2]

**Concerns:**

- **location** (APPROXIMATE): A=SOMA in CA1 stratum radiatum (UBERON:0005372 / MBA:415) / B=MBA:415 present (n=71 across Yao 2024 + Zhuang 2023 MERFISH) but minority; dominant locations are MBA:399 CA1 stratum oriens (n=284) and MBA:407 CA1 pyramidal layer (n=136). region_fraction=0.104 for MBA:415.. CA1 stratum radiatum soma is the defining RGC feature. The cluster includes radiatum cells but is not radiatum-selective — the RGC may be a minority subpopulation of this broader glutamatergic cluster.


- The classical node has no defining, negative, or neuropeptide markers. All marker property comparisons are NOT_ASSESSED. Confidence cannot exceed LOW until molecular markers are identified for the RGC.
- CLUS_0261 (n=529) spans multiple CA1 laminae and extends into CA2/CA3. The RGC is described as a rare specialised neuron; it is unlikely to constitute more than a small fraction of this cluster.
- Primary classical evidence is from rat (Kirson & Yaari 2000; Christie et al. 2000). Atlas is mouse. Cross-species extrapolation is plausible given Nasrallah et al. (2019) mouse replication but not confirmed at the molecular level.

**What would upgrade confidence:**

- *Unresolved:* What are the defining molecular markers of the CA1 radiatum giant cell? Modern single-cell transcriptomics is needed to determine whether the RGC falls within CLUS_0261 or a neighbouring cluster.


- *Unresolved:* Is the minority population of CLUS_0261 cells in CA1 stratum radiatum enriched for RGC-like morphology and electrophysiology, or do those cells represent another radiatum-soma type (e.g. displaced CA1 pyramidal cells)?


- *Unresolved:* Does CLUS_0261 show differential Grin2d or Hcn1/Hcn4 expression relative to adjacent CA1 clusters, consistent with the RGC biophysical signature?


- *Proposed:* Patch-seq on morphologically identified CA1 radiatum giant cells (DIC optics, as per Christie et al. 2000) to link the distinctive RGC electrophysiology to a transcriptomic cluster within CCN20230722 SUBC_016.


- *Proposed:* MERFISH/STARmap with probes for GRIN2D, HCN1, HCN4, and LEFTY1 in CA1 stratum radiatum to identify the molecular signature of radiatum-soma glutamatergic neurons.



---

## CS20230722_SUPT_0069 · 🔴 LOW

**Supporting evidence:**

- CS20230722_SUPT_0069 (0069 CA1-ProS Glut_1) is the highest region-fraction supertype candidate for MBA:415 (CA1 stratum radiatum, region_fraction=0.276). MERFISH confirms cells in stratum radiatum (4162 cells by Zhuang 2023; 6573 by Yao 2024), but the supertype also spans the pyramidal layer and stratum oriens broadly (13,245 cells total), indicating it captures the major CA1 principal cell population rather than the radiatum-restricted RGC specifically. [Atlas metadata]
- The classical RGC is defined by its exclusively radiatum soma and distinctive NMDA-dependent burst firing. SUPT_0069 encompasses the broad CA1-ProS Glut_1 supertype (n=13245) corresponding to the major CA1 principal cell population — the RGC is a rare subpopulation within this supertype rather than its defining member. [Literature] [1]
- Nasrallah et al. (2019) confirm the RGC in adult mouse with the same inverted triangular soma and identify CA2 as a strong presynaptic partner. The stratum radiatum component of SUPT_0069 (by MERFISH) is consistent with the Nasrallah observation, supporting this supertype as the most plausible atlas-level home for the RGC. [Literature] [2]

**Concerns:**

- **location** (APPROXIMATE): A=SOMA in CA1 stratum radiatum (UBERON:0005372 / MBA:415) / B=MBA:415 present (4162 cells Zhuang 2023; 6573 cells Yao 2024 MERFISH); also broadly in CA1 pyramidal layer MBA:407 and stratum oriens MBA:399. region_fraction=0.276 for MBA:415.. The atlas supertype has a substantial CA1 stratum radiatum component, consistent with the classical RGC soma location, but is not radiatum-selective. At 13,245 cells, the supertype corresponds to a major CA1 principal cell population of which the RGC is likely a minor sub-type.


- The classical node has no defining molecular markers. All marker property comparisons are NOT_ASSESSED. Confidence cannot exceed LOW until molecular markers are identified for the RGC. The supertype defining markers (Lefty1, Fibcd1, Pcp4l1, Onecut2, Kcnk2, Akain1, Rgs8) have not been tested on the classical type.
- The RGC is described as a rare specialised neuron. SUPT_0069 contains 13,245 cells, consistent with a major principal cell population. If the RGC is truly rare, it constitutes a minor subpopulation of this supertype, and a cluster-level node may be more appropriate once molecular markers are established.

**What would upgrade confidence:**

- *Unresolved:* Is the CA1 radiatum giant cell captured in one specific cluster within CS20230722_SUBC_016 at resolution finer than supertype 0069? Cluster-level candidates should be explored once molecular markers are available.


- *Unresolved:* Does SUPT_0069 or one of its child clusters show enrichment for GRIN2D or differential Hcn1/Hcn4 expression, consistent with the NR2D hypothesis and reversed HCN gradient described for the RGC?


- *Proposed:* Patch-seq on DIC-identified radiatum giant cells to identify their transcriptomic cluster within SUBC_016 and test whether SUPT_0069 supertype markers (Lefty1, Fibcd1) are expressed.


- *Proposed:* Grin2d immunohistochemistry on CA1 stratum radiatum sections to test the NR2D hypothesis and check co-localisation with the large-soma RGC morphology.


- *Proposed:* Re-analysis of the Yao 2021 HPF snRNA-seq dataset (GSE185862) for a rare Lefty1+/Fibcd1+ cluster with CA1 stratum radiatum localisation, to identify an RGC-compatible sub-cluster within SUPT_0069.



---

## Proposed experiments

### 1 — Patch-seq

- Patch-seq on morphologically identified CA1 radiatum giant cells (DIC optics, as per Christie et al. 2000) to link the distinctive RGC electrophysiology to a transcriptomic cluster within CCN20230722 SUBC_016.
- Patch-seq on DIC-identified radiatum giant cells to identify their transcriptomic cluster within SUBC_016 and test whether SUPT_0069 supertype markers (Lefty1, Fibcd1) are expressed.
*Resolves: edge_ca1_radiatum_giant_cell_to_clus_0261, edge_ca1_radiatum_giant_cell_to_supt_0069*

### 2 — MERFISH / spatial transcriptomics

- MERFISH/STARmap with probes for GRIN2D, HCN1, HCN4, and LEFTY1 in CA1 stratum radiatum to identify the molecular signature of radiatum-soma glutamatergic neurons.
*Resolves: edge_ca1_radiatum_giant_cell_to_clus_0261*

### 3 — Other

- Grin2d immunohistochemistry on CA1 stratum radiatum sections to test the NR2D hypothesis and check co-localisation with the large-soma RGC morphology.
*Resolves: edge_ca1_radiatum_giant_cell_to_supt_0069*

### 4 — scRNA-seq / single-cell

- Re-analysis of the Yao 2021 HPF snRNA-seq dataset (GSE185862) for a rare Lefty1+/Fibcd1+ cluster with CA1 stratum radiatum localisation, to identify an RGC-compatible sub-cluster within SUPT_0069.
*Resolves: edge_ca1_radiatum_giant_cell_to_supt_0069*

---

## Open questions

1. What are the defining molecular markers of the CA1 radiatum giant cell? Modern single-cell transcriptomics is needed to determine whether the RGC falls within CLUS_0261 or a neighbouring cluster.
2. Is the minority population of CLUS_0261 cells in CA1 stratum radiatum enriched for RGC-like morphology and electrophysiology, or do those cells represent another radiatum-soma type (e.g. displaced CA1 pyramidal cells)?
3. Does CLUS_0261 show differential Grin2d or Hcn1/Hcn4 expression relative to adjacent CA1 clusters, consistent with the RGC biophysical signature?
4. Is the CA1 radiatum giant cell captured in one specific cluster within CS20230722_SUBC_016 at resolution finer than supertype 0069? Cluster-level candidates should be explored once molecular markers are available.
5. Does SUPT_0069 or one of its child clusters show enrichment for GRIN2D or differential Hcn1/Hcn4 expression, consistent with the NR2D hypothesis and reversed HCN gradient described for the RGC?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_ca1_radiatum_giant_cell_to_clus_0261 | Atlas metadata | PARTIAL |
| edge_ca1_radiatum_giant_cell_to_clus_0261 | Literature [1] | PARTIAL |
| edge_ca1_radiatum_giant_cell_to_clus_0261 | Literature [2] | PARTIAL |
| edge_ca1_radiatum_giant_cell_to_supt_0069 | Atlas metadata | PARTIAL |
| edge_ca1_radiatum_giant_cell_to_supt_0069 | Literature [1] | PARTIAL |
| edge_ca1_radiatum_giant_cell_to_supt_0069 | Literature [2] | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Kirson & Yaari 2000 · PMID:10864941 | [10864941](https://pubmed.ncbi.nlm.nih.gov/10864941/) | soma location |
| [2] | Nasrallah et al. 2019 · PMID:30943417 | [30943417](https://pubmed.ncbi.nlm.nih.gov/30943417/) | soma location |
