# Axo-axonic (chandelier) cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | pvalb chandelier GABAergic interneuron (CL:4023036) | |
| Soma location | CA1 stratum pyramidale [UBERON:0005401] | [1] |
| NT | GABAergic | [2] |
| Markers | Pvalb+ | [1] [3] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] |  | — | 🔴 LOW | Speculative |
| 2 | 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] |  | — | 🔴 LOW | Speculative |

All edges: `EQUIVALENT`

---

## 0204 Pvalb chandelier Gaba_1 · 🔴 LOW

**Supporting evidence:**

- Supertype name "Pvalb chandelier Gaba_1" directly names the chandelier (= axo-axonic) cell type. Pvalb subclass, GABA NT type are fully consistent. Pvalb present in DEFINING_SCOPED markers confirming PV+ identity. The CL mapping for the classical node (CL:4023036 pvalb chandelier GABAergic interneuron) is EXACT, and the atlas supertype name makes the identity explicit. EQUIVALENT declared because the atlas supertype is named for and defined by the chandelier/axo-axonic cell type. Confidence is LOW (not MODERATE) because: (a) the supertype has only piriform area in its top anatomical locations (194 cells) with no explicit hippocampal pyramidal layer entry at supertype level; (b) this is metadata-only with no primary literature on the edge; (c) axo-axonic and basket PV cells have been reported to have high transcriptomic overlap (PMID:33398060). [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Pvalb subclass (n=66 HIP cells) onto WMBv1. SUPT_0204 (Pvalb chandelier Gaba_1) is the top supertype hit for Pvalb cells (F1=0.612, 26/66 cells, target_purity=1.0). The 'chandelier' label in WMBv1 corresponds to axo-axonic cells. PARTIAL because the SSv4 Pvalb label is a mixed population; nevertheless, SUPT_0204/chandelier being the single strongest Pvalb target is consistent with the axo-axonic cell correspondence. Yao 2021 SSv4 'Pvalb' subclass label (n=66 HIP cells) encompasses PV basket, axo-axonic, and bistratified cells; subtype resolution requires a morphologically identified PV-IN dataset. [Annotation transfer]

**Concerns:**

- **location_CA1_stratum_pyramidale** (DISCORDANT): A=CA1 stratum pyramidale (UBERON:0005401) — soma / B=Piriform area (MBA:961, 194 cells) — no hippocampal pyramidal layer listed at supertype level. Supertype anatomy dominated by piriform area. Hippocampal pyramidal layer not listed at supertype level. However, child cluster 0732 has CA1 SO, CA1 SR, CA3 SO, and CA3 pyramidal layer entries, suggesting hippocampal chandelier cells exist within this supertype at cluster level.

- Supertype anatomy is piriform-dominated at top level; hippocampal chandelier cells should be resolvable at cluster level (see CLUS_0732 edge). Supertype likely spans multiple regions where axo-axonic cells occur.
- High transcriptomic similarity between PV+ morphological subtypes (PMID:33398060) means chandelier-specific markers are not fully resolved at supertype level from basket/bistratified cells in the metadata.

---

## 0732 Pvalb chandelier Gaba_1 · 🔴 LOW

**Supporting evidence:**

- Child of SUPT_0204 (Pvalb chandelier Gaba_1). Hippocampal locations: CA1 SO (38 cells), CA1 SR (23 cells), CA3 SO (33 cells), CA3 pyramidal layer (23 cells), CA3 SR (15 cells), dentate gyrus granule cell layer (15 cells). Pvalb in MERFISH markers confirms PV+ identity. Cluster name "0732 Pvalb chandelier Gaba_1" explicitly identifies it as a hippocampal chandelier cell cluster. GABA consistent. Neuropeptides Cck (8.4), Pthlh, Npy present; Cck at high score warrants noting but chandelier cells can have low-level peptide co-expression. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Pvalb subclass (n=66 HIP cells) onto WMBv1. CLUS_0732 (Pvalb chandelier Gaba_1) is the top cluster hit for Pvalb cells (F1=0.622, 23/66 cells, target_purity=1.0). This is the strongest cluster-level hit among all Pvalb targets, consistent with the axo-axonic → chandelier supertype correspondence. PARTIAL because the source label is a mixed Pvalb population. Yao 2021 SSv4 'Pvalb' subclass label (n=66 HIP cells) encompasses PV basket, axo-axonic, and bistratified cells; subtype resolution requires a morphologically identified PV-IN dataset. [Annotation transfer]

**Concerns:**

- **location_CA1_stratum_pyramidale** (APPROXIMATE): A=CA1 stratum pyramidale (UBERON:0005401) — soma / B=CA1 SO (MBA:399, 38 cells); CA3 pyramidal layer (MBA:495, 23 cells). CA1 pyramidal layer not listed; CA1 SO is the dominant hippocampal CA1 location. CA3 pyramidal layer present. Some soma-in-SO placement may reflect atlas resolution.

- Cck neuropeptide (score 8.4) unexpectedly high for a chandelier cell. May indicate minor contamination or genuine peptide co-expression. Requires primary source validation.
- Dentate gyrus granule cell layer (15 cells) — chandelier cells in DG are less well characterized. May reflect axo-axonic cells contacting granule cells or a distinct population.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0204 | Atlas metadata | SUPPORT |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0204 | Annotation transfer | PARTIAL |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0732 | Atlas metadata | SUPPORT |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0732 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 · PMID:25018703 | [25018703](https://pubmed.ncbi.nlm.nih.gov/25018703/) | soma location |
| [2] | Dannenberg et al. 2017 · PMID:29321728 | [29321728](https://pubmed.ncbi.nlm.nih.gov/29321728/) | neurotransmitter type |
| [3] | Que et al. 2021 · PMID:33398060 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060/) | Pvalb marker |
