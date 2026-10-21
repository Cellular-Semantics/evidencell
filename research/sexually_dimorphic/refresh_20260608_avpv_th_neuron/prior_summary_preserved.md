# AVPV tyrosine hydroxylase (TH) neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | anteroventral periventricular nucleus (AVPV) [MBA:272] | [1] [2] [3] |
| NT | dopaminergic | [3] |
| Markers | Th+, Kiss1+ | [1] [4] [2] [3] [5] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] |  | 178 |  |  |
| — | 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 | 5 |  |  |

All edges: `evidencell:PartialOverlapMatch`

---

## 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 · 

*`CS20230722_SUPT_0486` · 178 cells (10x)*

**Supporting evidence:**

- SUPT_0486 is the top-ranked rank-1 candidate for avpv_th_neuron. Child cluster CLUS_1915 (nt_type=Dopa, male_female_ratio=0.02) is the most extremely female-biased cluster in the candidate set, directly concordant with the female-biased AVPV TH population (2-4x more TH+ neurons in females). Th=2.72, Esr1=7.72, Kiss1=0.62 at supertype level. Three independent signals (Th expression, AVPV location, female sex ratio in child cluster) converge on SUPT_0486/CLUS_1915. [Atlas metadata]

**Concerns:**

- **nt_type** (APPROXIMATE): A=dopaminergic (A14 group) / B=GABAergic (Gaba_5 label); child CLUS_1915 nt_type=Dopa. Dopaminergic identity resolved at cluster level; supertype label reflects majority.
- **location_MBA272** (APPROXIMATE): A=MBA:272 (AVPV) / B=MBA:272 (AVPV) n=16; MBA:133 PVpo n=64; MBA:515 MPN n=37. Direct AVPV cells present (n=16); supertype also spans broader preoptic zone.
- **marker_Th** (APPROXIMATE): A=POSITIVE (protein, primary defining marker) / B=precomputed mean_expression=2.72. 
- **marker_Kiss1** (APPROXIMATE): A=POSITIVE (transcript, co-expressed with Th in AVPV) / B=precomputed mean_expression=0.62. 
- SUPT_0486 carries a Gaba_5 label at supertype level while the classical AVPV TH neuron is dopaminergic. Dopaminergic identity is resolved only at cluster level (CLUS_1915, Dopa designation).
- avpv_th_neuron and avpv_kiss1_neuron both map to SUPT_0486 — these two classical types substantially overlap (most AVPV/PeN Kiss1 cells co-express Th). Cluster-level resolution needed to determine whether they are separable within SUPT_0486.

**What would upgrade confidence:**

- *Unresolved:* Does CLUS_1915 specifically correspond to AVPV A14 TH neurons? Confirm by cluster-level Kiss1/Th/Esr1 co-expression profiling.

- *Proposed:* MapMyCells annotation transfer of AVPV TH-lineage (Th-Cre or Kiss1-Cre) scRNA-seq data to WMBv1 for F1-based confirmation.


---

## 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 · 

*`CS20230722_CLUS_1915` · 5 cells (10x) · supertype: 0486 PVpo-VMPO-MPN Hmx2 Gaba_5*

**Supporting evidence:**

- CLUS_1915 is the top-ranked rank-0 candidate (DB score=6) for avpv_th_neuron. Th=6.6 (highest in the SUPT_0486 lineage), Kiss1=2.51 (only cluster with Kiss1 substantially above background), MFR=0.02 (extreme female bias), nt_type=Dopa confirmed, MBA:272 (AVPV) cells present. Slc18a2 (VMAT2, vesicular monoamine transporter) is a DEFINING cluster marker, providing independent dopaminergic identity support. Three convergent signals: Th expression, female sex ratio, and dopaminergic NT type. [Atlas metadata]

**Concerns:**

- **location_MBA272** (APPROXIMATE): A=MBA:272 (AVPV) / B=MBA:272 (AVPV) n=1; MBA:133 PVpo n=1; MBA:1097 Hypothalamus n=3. AVPV cells present; cluster too small to resolve sub-regional anatomy precisely.
- CLUS_1915 has only n=3–5 total cells. All metrics are directionally correct but have limited statistical power. Confidence capped at MODERATE.
- avpv_th_neuron and avpv_kiss1_neuron both map to CLUS_1915 — the two classical types are substantially overlapping (most AVPV Kiss1 cells co-express Th). These may be the same cell population described from different entry points in the classical literature.

**What would upgrade confidence:**

- *Unresolved:* Is CLUS_1915 specifically the A14 TH/Kiss1 cluster, or does it also include TH+ AVPV neurons that are Kiss1-negative?

- *Proposed:* MapMyCells annotation transfer of Th-Cre AVPV scRNA-seq data for F1-based confirmation at cluster level.


---

## Proposed experiments

### 1 — MapMyCells / annotation transfer

- MapMyCells annotation transfer of AVPV TH-lineage (Th-Cre or Kiss1-Cre) scRNA-seq data to WMBv1 for F1-based confirmation.
- MapMyCells annotation transfer of Th-Cre AVPV scRNA-seq data for F1-based confirmation at cluster level.
*Resolves: edge_avpv_th_neuron_to_cs20230722_supt_0486, edge_avpv_th_neuron_to_cs20230722_clus_1915*

---

## Open questions

1. Does CLUS_1915 specifically correspond to AVPV A14 TH neurons? Confirm by cluster-level Kiss1/Th/Esr1 co-expression profiling.
2. Is CLUS_1915 specifically the A14 TH/Kiss1 cluster, or does it also include TH+ AVPV neurons that are Kiss1-negative?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_avpv_th_neuron_to_cs20230722_supt_0486 | Atlas metadata | SUPPORT |
| edge_avpv_th_neuron_to_cs20230722_clus_1915 | Atlas metadata | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | https://doi.org/10.1007/s12031-012-9923-1 | — | soma location |
| [2] | He et al. 2013 · PMID:25206587 | [25206587](https://pubmed.ncbi.nlm.nih.gov/25206587/) | soma location |
| [3] | Stephens et al. 2017 · PMID:28660243 | [28660243](https://pubmed.ncbi.nlm.nih.gov/28660243/) | soma location |
| [4] | Zilkha et al. 2021 · PMID:33910083 | [33910083](https://pubmed.ncbi.nlm.nih.gov/33910083/) | Th marker |
| [5] | Kauffman et al. 2007 · PMID:17699664 | [17699664](https://pubmed.ncbi.nlm.nih.gov/17699664/) | Kiss1 marker |
