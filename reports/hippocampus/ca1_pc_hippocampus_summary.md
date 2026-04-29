# CA1 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**STATUS: DRAFT.** Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.

---

## Classical type definition

| Property | Value | References |
|---|---|---|
| Soma location | Pyramidal layer of CA1 [UBERON:0014548] (*CA1 stratum pyramidale*) | [1][2][3][4][5] |
| Neurotransmitter | Glutamatergic | [4] |
| Defining markers | *Wfs1* | [6][7][8][9][10] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (CA1 pyr. layer) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_SUPT_0069 | 0069 CA1-ProS Glut_1 | 2553 | 🟡 MODERATE | NT consistent; location consistent; Wfs1 not assessed | Best candidate |

**Total edges: 1 · Relationship type: TYPE_A_SPLITS.** *(note: the classical CA1 pyramidal cell population encompasses at least four WMBv1 supertypes within subclass CS20230722_SUBC_016; this edge captures the primary correspondence only)*

---

## 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] · 🟡 MODERATE

### Supporting evidence

- **Atlas metadata — subclass assignment:** SUPT_0069 [CS20230722_SUPT_0069] belongs to subclass CS20230722_SUBC_016 (016 CA1-ProS Glut), the dedicated CA1/prosubiculum glutamatergic subclass in WMBv1. This is the highest-scoring candidate for CA1 pyramidal cells (discovery score 5).
- **Atlas metadata — soma location:** SUPT_0069 [CS20230722_SUPT_0069] has 2553 cells assigned to Field CA1, pyramidal layer (MBA:407), directly consistent with the classical CA1 stratum pyramidale soma location [UBERON:0014548].
- **Atlas metadata — NT type:** The parent subclass SUBC_016 is named "CA1-ProS Glut", confirming glutamatergic identity consistent with the classical node.
- **Annotation transfer — GSE185862 (Yao 2021 SSv4):** MapMyCells local annotation transfer of CA1-ProS subclass labels from Yao 2021 mouse hippocampus SSv4 scRNA-seq dataset (GEO:GSE185862) onto WMBv1 (CCN20230722). Of 1704 CA1-ProS cells, 1011 (59.3%) mapped to SUPT_0069 [CS20230722_SUPT_0069] at the supertype level. F1 score = 0.745 (group_purity = 0.593, target_purity = 1.0). Target purity of 1.0 confirms SUPT_0069 is exclusively populated by CA1-ProS cells in this dataset, with no contamination from other subclasses.

### Marker evidence provenance

- **Wfs1 — canonical CA1 marker, not assessed in SUPT_0069 metadata:** *Wfs1* is listed as the sole defining marker for the classical CA1 pyramidal cell node [6][7][8][9][10]. However, SUPT_0069 [CS20230722_SUPT_0069] lists defining markers as *Lefty1*, *Fibcd1*, and *Pcp4l1* — none of which are *Wfs1*. This comparison is flagged NOT_ASSESSED: expression of *Wfs1* in SUPT_0069 has not been directly interrogated from the atlas precomputed statistics.
- **Wfs1 is a well-established CA1 marker** supported by immunohistochemistry [6][8][9][10] and transcript-level data [7], but these studies characterise *Wfs1* as enriched in CA1 pyramidal cells broadly rather than as specific to a particular CA1 supertype. It is possible that *Wfs1* is enriched in one sibling CA1-ProS supertype relative to SUPT_0069 [CS20230722_SUPT_0069], which would have bearing on the sublayer correspondence (see Open questions below).
- **No protein-level marker comparison is possible** from current atlas metadata: WMBv1 cluster markers are transcript-based (scRNA-seq/MERFISH), while several *Wfs1* references use immunohistochemistry [8][9][10]. Method-level discordance cannot be excluded.

### Concerns

- **Ambiguous mapping — TYPE_A_SPLITS:** WMBv1 resolves at least four supertypes within CS20230722_SUBC_016. The annotation transfer result (GSE185862) shows the remaining 40.7% of CA1-ProS cells distribute across sibling supertypes within the same subclass. The full classical CA1 pyramidal cell population is not captured by this single edge; additional edges within CS20230722_SUBC_016 are needed.
- **Wfs1 absent from SUPT_0069 defining markers:** The canonical CA1 pyramidal marker *Wfs1* does not appear in the SUPT_0069 [CS20230722_SUPT_0069] metadata marker list. This is not a refutation — *Wfs1* may be expressed at detectable levels without reaching the threshold for inclusion as a defining marker — but it introduces uncertainty about which CA1-ProS supertype best corresponds to the Wfs1-high (deep-layer) pyramidal cell population described in the classical literature.
- **ProS admixture:** The subclass name "CA1-ProS Glut" indicates joint CA1/prosubiculum representation. SUPT_0069 [CS20230722_SUPT_0069]'s cell counts in MERFISH data include pyramidal layer cells in Field CA1 (MBA:407), which is consistent with CA1 identity, but the extent of prosubiculum admixture at the supertype level is not assessed. *(note: the pyramidal layer of the prosubiculum is anatomically adjacent to CA1 and partial admixture in transcriptomic clusters is expected.)*
- **Location alignment uses MERFISH compartment data:** CA1-ProS cells in MERFISH distribute across pyramidal layer, stratum oriens, and stratum radiatum. The pyramidal layer assignment (2553 cells in MBA:407) is consistent with classical soma location, but dendritic compartments (oriens and radiatum) inflate the total cell count in adjacent layers. This is a normal feature of MERFISH spatial assignment and is not a true discordance.

### What would upgrade confidence

- Run MapMyCells annotation transfer of Cembrowski 2016 [1] or Zeisel 2018 dorsal CA1 pyramidal cell labels onto WMBv1 to resolve sublayer correspondence across SUPT_0069 and its sibling supertypes within CS20230722_SUBC_016.
- Query WMBv1 precomputed expression statistics for *Wfs1* across all CA1-ProS supertypes within CS20230722_SUBC_016 to directly assess which supertype carries the deep-layer *Wfs1*-high signature. A clear *Wfs1* enrichment in one supertype would allow confident sublayer assignment.
- Add mapping edges to the remaining CA1-ProS supertypes within CS20230722_SUBC_016 to complete the TYPE_A_SPLITS set and document how the classical CA1 PC population partitions across the atlas.

---

## Proposed experiments

### Annotation transfer — targeted sublayer labels

| Attribute | Detail |
|---|---|
| **What** | MapMyCells annotation transfer of labelled CA1 sublayer datasets (Cembrowski 2016 [1]) |
| **Target** | F1 ≥ 0.7 per supertype; distinct primary mapping for deep vs. superficial CA1 PC labels |
| **Expected output** | AnnotationTransferEvidence entries for each CA1-ProS supertype within CS20230722_SUBC_016, with per-supertype F1 scores |
| **Resolves** | Which CA1-ProS supertype within CS20230722_SUBC_016 corresponds to the Wfs1-high deep-layer population; sublayer partitioning across supertypes |

### Atlas precomputed expression query — Wfs1

| Attribute | Detail |
|---|---|
| **What** | Query WMBv1 precomputed expression statistics for *Wfs1* across all CA1-ProS supertypes within CS20230722_SUBC_016 using `just add-expression` or direct HDF5 query |
| **Target** | Mean expression and fraction expressing *Wfs1* per supertype; identify highest-expressing supertype |
| **Expected output** | PropertySource marker evidence entry for *Wfs1* on the appropriate CA1-ProS supertype node |
| **Resolves** | Wfs1 NOT_ASSESSED comparison on SUPT_0069 [CS20230722_SUPT_0069]; establishes which supertype best matches the *Wfs1*-defined classical CA1 PC |

---

## Open questions

1. Which CA1-ProS supertypes within CS20230722_SUBC_016 correspond to deep vs. superficial CA1 pyramidal cell sublayers? *Wfs1* marks deep-layer CA1 PCs in the literature; querying which supertype carries *Wfs1* in the atlas would resolve the sublayer correspondence.

---

## Evidence base

| Edge ID | Evidence type | Details | Supports |
|---|---|---|---|
| edge_ca1_pc_hippocampus_to_supt_0069 | ATLAS_METADATA | SUPT_0069 [CS20230722_SUPT_0069] in subclass 016 CA1-ProS Glut; 2553 cells in CA1 pyramidal layer; discovery score 5 | SUPPORT |
| edge_ca1_pc_hippocampus_to_supt_0069 | ANNOTATION_TRANSFER | GSE185862 (Yao 2021 SSv4); 1011/1704 CA1-ProS cells → SUPT_0069 [CS20230722_SUPT_0069]; F1 = 0.745; target_purity = 1.0 | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | Soma location |
| [2] | Müller & Remy 2017 | [29250747](https://pubmed.ncbi.nlm.nih.gov/29250747/) | Soma location |
| [3] | https://doi.org/10.1038/s41598-017-11268-z | — | Soma location |
| [4] | Dale et al. 2015 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | Soma location; NT type |
| [5] | Mancini et al. 2022 | [37011759](https://pubmed.ncbi.nlm.nih.gov/37011759/) | Soma location |
| [6] | Siegel et al. 1995 | [7722624](https://pubmed.ncbi.nlm.nih.gov/7722624/) | Wfs1 marker |
| [7] | Yeung et al. 2020 | [32009891](https://pubmed.ncbi.nlm.nih.gov/32009891/) | Wfs1 marker |
| [8] | Herrera-Molina et al. 2017 | [28779130](https://pubmed.ncbi.nlm.nih.gov/28779130/) | Wfs1 marker |
| [9] | Langnaese et al. 1997 | [8995369](https://pubmed.ncbi.nlm.nih.gov/8995369/) | Wfs1 marker |
| [10] | Herrera-Molina et al. 2014 | [24554721](https://pubmed.ncbi.nlm.nih.gov/24554721/) | Wfs1 marker |
