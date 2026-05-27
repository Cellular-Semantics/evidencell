# AVPV/PeN kisspeptin neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | hypothalamus kisspeptin neuron (CL:4023123) | |
| Soma location | anteroventral periventricular nucleus (AVPV) [MBA:272]; periventricular nucleus (PeN) [MBA:341] | [1] [2] [3] [1] [2] [3] |
| NT | GABAergic / dopaminergic (TH co-expression) | [3] |
| Markers | Kiss1+, Th+, Esr1+ | [1] [2] [3] [4] [5] |
| Neuropeptides | Kiss1 | [6] |

---

## Cell Ontology mapping

AVPV/PeN kisspeptin neuron is a **broad match** to **hypothalamus kisspeptin neuron (CL:4023123)** in the Cell Ontology — i.e. **hypothalamus kisspeptin neuron (CL:4023123)** is the closest existing CL term (an ancestor) but does not fully cover this type. A new child term is a candidate for submission to CL.

*Mapping notes:* CL:4023123 covers all hypothalamic kisspeptin neurons. The AVPV/PeN (RP3V) population is Kiss1-only (not obligately KNDy), so the more specific CL:4023128 (RP3V KNDy neuron) is inappropriate as it requires NKB and dynorphin co-expression. A dedicated CL term for the AVPV/RP3V Kiss1 non-KNDy subpopulation does not yet exist — potential CL contribution.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] |  | 178 |  |  |
| — | 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 | 5 |  |  |

All edges: `skos:closeMatch`

---

## 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 · 

*`CS20230722_SUPT_0486` · 178 cells (10x)*

**Supporting evidence:**

- SUPT_0486 (PVpo-VMPO-MPN Hmx2 Gaba_5) is the highest-scoring supertype for AVPV-region preoptic GABAergic neurons. Precomputed expression confirms Esr1=7.72 (defining marker for both classical node and supertype), Th=2.72, and Kiss1=0.62. The supertype contains n=16 cells labeled AVPV (MBA:272). Child cluster CLUS_1915 (dopaminergic designation, male_female_ratio=0.02) is the strongest sub-resolution candidate for the female-biased AVPV Kiss1/TH population. PARTIAL_OVERLAP because SUPT_0486 spans a broader preoptic zone than the AVPV/PeN. [Atlas metadata]

**Concerns:**

- **nt_type** (APPROXIMATE): A=GABAergic / dopaminergic (Th co-expression) / B=GABAergic (Gaba_5 label). GABAergic concordant; dopaminergic component present at supertype level (Th=2.72) but diluted. Resolved at cluster level by CLUS_1915 (nt_type=Dopa).

- **location_MBA272** (APPROXIMATE): A=MBA:272 (AVPV) / B=MBA:272 (AVPV) n=16; MBA:133 PVpo n=64; MBA:515 MPN n=37. Direct AVPV location match (n=16); supertype spans broader preoptic zone.
- **marker_Kiss1** (APPROXIMATE): A=POSITIVE (transcript, defining marker) / B=precomputed mean_expression=0.62. Present but low-moderate at supertype level; consistent with subset expression.
- **marker_Th** (APPROXIMATE): A=POSITIVE (protein, co-expressed with Kiss1) / B=precomputed mean_expression=2.72. 
- SUPT_0486 spans PVpo-VMPO-MPN and contains multiple preoptic cell types. avpv_kiss1_neuron, avpv_th_neuron, and mpoa_esr1_neuron all map to SUPT_0486, reflecting the heterogeneity of this preoptic GABAergic supertype. AVPV Kiss1 neurons are a subset.
- Supertype-level sex ratio not directly available. Female-biased sex ratio signal is concentrated in child cluster CLUS_1915 (male_female_ratio=0.02). A cluster-level edge to CLUS_1915 would provide more specific mapping.
- [AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated from deprecated evidencell:PartialOverlapMatch to skos:closeMatch by `refresh_predicates.py`. Rule: rule-3b: no AT F1, existing caveats → closeMatch. Curator review recommended.

**What would upgrade confidence:**

- *Unresolved:* Which cluster(s) within SUPT_0486 carry peak Kiss1+Th+Esr1 co-expression consistent with AVPV Kiss1/TH identity?

- *Unresolved:* Do PeN (MBA:341) Kiss1 neurons map to SUPT_0486 or a different supertype?

- *Proposed:* Inspect child clusters of SUPT_0486 for Kiss1, Th, Esr1 co-expression at cluster level to identify the AVPV Kiss1/TH candidate cluster.

- *Proposed:* MapMyCells annotation transfer of published AVPV Kiss1 scRNA-seq data to WMBv1.


---

## 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 · 

*`CS20230722_CLUS_1915` · 5 cells (10x) · supertype: 0486 PVpo-VMPO-MPN Hmx2 Gaba_5*

**Supporting evidence:**

- CLUS_1915 (1915 PVpo-VMPO-MPN Hmx2 Gaba_5) is the child cluster of SUPT_0486 with the highest co-expression of Kiss1 (2.51), Th (6.6), and Esr1 (9.55) — all three classical defining markers. It is the most strongly female-biased cluster in the supertype (male_female_ratio=0.02), directly concordant with the FEMALE_BIASED sex_bias of avpv_kiss1_neuron. Kiss1 and Slc18a2 are cluster-level DEFINING markers. nt_type=Dopa confirmed in cluster.yaml. MBA:272 (AVPV) cells explicitly present. CLUS_1915 was not ranked in the top-30 DB results because its Kiss1/Th/Esr1 profile appears only in precomputed_expression, not in the defining_markers metadata columns. It was identified through child_cluster_expression analysis of the SUPT_0486 parent. [Atlas metadata]
- Stephens 2024 (PMID:37934722) bulk Kiss1+ neurons sorted from RP3V vs ARC. Differential δ = ρ_RP3V − ρ_ARC ranks CLUS_1915 first of 5,322 atlas clusters, with δ=0.090 (ρ_RP3V=0.388, ρ_ARC=0.298). All other top-20 hits are also preoptic/periventricular hypothalamic GABAergic clusters — the differential signal is strongly anatomically clean. Independent quantitative confirmation of the existing ATLAS_METADATA-based mapping; the Kiss1+ pool transcriptomic profile tracks CLUS_1915 specifically more than any other cluster in the atlas. [Bulk correlation] [7]

**Concerns:**

- **location_MBA272** (APPROXIMATE): A=MBA:272 (AVPV) / B=MBA:272 (AVPV) n=1; MBA:133 PVpo n=1; MBA:1097 Hypothalamus n=3. AVPV cells present but cluster is very small (n=5 total) and primary soma annotation resolves to the broad Hypothalamus catchall (MBA:1097). MERFISH spatial resolution insufficient to resolve AVPV vs adjacent PVpo/PeN at this cell count.

- CLUS_1915 contains only n=3–5 total cells in the WMBv1 atlas. The sex ratio (MFR=0.02) and expression values are reliable in direction but have limited statistical power. Confidence is capped at MODERATE pending annotation transfer evidence or larger-dataset replication.
- CLUS_1915 is a sub-resolution split of SUPT_0486. The cluster-level Kiss1+Th+Dopa phenotype is the most specific available match for avpv_kiss1_neuron; however, avpv_th_neuron maps to the same cluster (both types substantially overlap in the classical literature — most AVPV Kiss1 cells co-express Th).
- [AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated from deprecated evidencell:PartialOverlapMatch to skos:closeMatch by `refresh_predicates.py`. Rule: rule-3b: no AT F1, existing caveats → closeMatch. Curator review recommended.

**What would upgrade confidence:**

- *Unresolved:* Do avpv_kiss1_neuron and avpv_th_neuron represent separable populations within CLUS_1915, or is CLUS_1915 the atlas correlate of both?

- *Proposed:* MapMyCells annotation transfer of published AVPV Kiss1-Cre or Kiss1-Cre/Rosa-tdTom scRNA-seq data to WMBv1; confirm F1 score against CLUS_1915.


---

## Proposed experiments

### 1 — Other

- Inspect child clusters of SUPT_0486 for Kiss1, Th, Esr1 co-expression at cluster level to identify the AVPV Kiss1/TH candidate cluster.
*Resolves: edge_avpv_kiss1_neuron_to_cs20230722_supt_0486*

### 2 — MapMyCells / annotation transfer

- MapMyCells annotation transfer of published AVPV Kiss1 scRNA-seq data to WMBv1.
- MapMyCells annotation transfer of published AVPV Kiss1-Cre or Kiss1-Cre/Rosa-tdTom scRNA-seq data to WMBv1; confirm F1 score against CLUS_1915.
*Resolves: edge_avpv_kiss1_neuron_to_cs20230722_supt_0486, edge_avpv_kiss1_neuron_to_cs20230722_clus_1915*

---

## Open questions

1. Which cluster(s) within SUPT_0486 carry peak Kiss1+Th+Esr1 co-expression consistent with AVPV Kiss1/TH identity?
2. Do PeN (MBA:341) Kiss1 neurons map to SUPT_0486 or a different supertype?
3. Do avpv_kiss1_neuron and avpv_th_neuron represent separable populations within CLUS_1915, or is CLUS_1915 the atlas correlate of both?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_avpv_kiss1_neuron_to_cs20230722_supt_0486 | Atlas metadata | PARTIAL |
| edge_avpv_kiss1_neuron_to_cs20230722_clus_1915 | Atlas metadata | SUPPORT |
| edge_avpv_kiss1_neuron_to_cs20230722_clus_1915 | Bulk correlation [7] | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Nejad et al. 2017 · PMID:29201072 | [29201072](https://pubmed.ncbi.nlm.nih.gov/29201072/) | soma location |
| [2] | Adachi et al. 2007 · PMID:17213691 | [17213691](https://pubmed.ncbi.nlm.nih.gov/17213691/) | soma location |
| [3] | Stephens et al. 2017 · PMID:28660243 | [28660243](https://pubmed.ncbi.nlm.nih.gov/28660243/) | soma location |
| [4] | Kauffman et al. 2007 · PMID:17699664 | [17699664](https://pubmed.ncbi.nlm.nih.gov/17699664/) | Th marker |
| [5] | Wartenberg et al. 2021 · PMID:34561233 | [34561233](https://pubmed.ncbi.nlm.nih.gov/34561233/) | Esr1 marker |
| [6] | Frazão et al. 2013 · PMID:23407940 | [23407940](https://pubmed.ncbi.nlm.nih.gov/23407940/) | Kiss1 neuropeptide |
| [7] | Stephens et al. 2024 · PMID:37934722 | [37934722](https://pubmed.ncbi.nlm.nih.gov/37934722/) | Stephens 2024 (PMID:37934722) bulk Kiss1+ neurons sorted from RP3V vs ARC. Diffe |
