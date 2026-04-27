# AVPV tyrosine hydroxylase (TH) neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Anteroventral periventricular nucleus [MBA:272] | [1][2][3] |
| Neurotransmitter | Dopaminergic | [3] |
| Defining markers | Th (protein, primary defining marker) | [1][2][4] |
| Defining markers | Kiss1 (transcript, co-expressed with Th in AVPV/PeN) | [3][5] |
| Negative markers | — | |
| Neuropeptides | — | |

**Notes.** AVPV TH neurons are a sexually dimorphic population with 2–4× more TH-immunoreactive neurons in females than in males [4]. In mice, the AVPV/periventricular nucleus (PeN) Kiss1 population substantially overlaps with TH neurons: most AVPV/PeN Kiss1-expressing cells co-express TH [3]. These neurons are distinct from the sexually dimorphic nucleus of the preoptic area (SDN-POA), which contains TH-positive axons and synapses but not TH-positive cell bodies. No CL term currently exists for this population; it is a candidate for a new term as a sibling of CL:4072009 ("A12 dopaminergic neuron"), representing AVPV/RP3V A14 dopaminergic neurons.

> "In mice, most AVPV/PeN Kiss1 cells coexpress tyrosine hydroxylase (TH), the rate-limiting enzyme in catecholamine synthesis (in this case, dopamine)."
> — S et al. 2017, Neuronal Markers and Molecular Characteristics · [3] <!-- quote_key: 4702847_ebd225e6 -->

> "A notable exception is the AVPV of the hypothalamus, which is larger in volume, contains more cells, and sends more projections to multiple reproduction-related brain regions in females compared to males [25,34,71,72,76e[79]. Importantly, it also expresses several sexually dimorphic molecularly defined neuronal populations, including the tyrosine hydroxylase (TH)-expressing population, which contains 3e4 times more neurons in females than in males [34,72]"
> — N et al. 2021, Sexually Dimorphic Brain Regions and Structures · [4] <!-- quote_key: 233446934_e19240c2 -->

---

## 2. Mapping candidates

### 4a. Candidate overview

| Rank | WMBv1 node | Taxonomy level | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| 1 | 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] | CLUSTER | 🟡 MODERATE | Th CONSISTENT (mean 6.6) · Kiss1 CONSISTENT (mean 2.51, defining marker) · MFR=0.02 CONSISTENT · NT Dopa CONSISTENT | Best candidate (cluster) |
| 2 | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] | SUPERTYPE | 🟡 MODERATE | Th APPROXIMATE (mean 2.72) · Kiss1 APPROXIMATE (mean 0.62) · female bias in child CLUS_1915 | Best candidate (supertype) |

*2 edges total; relationship type: PARTIAL_OVERLAP. Both edges are MODERATE — no UNCERTAIN edges.*

### 4b. Property alignment table

| Property | Classical | SUPT_0486 (supertype) | CLUS_1915 (best cluster) | Alignment |
|---|---|---|---|---|
| Soma location | MBA:272 (AVPV) | MBA:272 n=16; MBA:133 PVpo n=64; MBA:515 MPN n=37 | MBA:272 n=1; MBA:133 PVpo n=1; MBA:1097 Hypothalamus n=3 | APPROXIMATE (AVPV cells present in both; supertype and cluster span broader preoptic zone) |
| NT type | Dopaminergic (A14 group) | GABAergic (Gaba_5 label); child CLUS_1915 nt_type=Dopa | Dopa (confirmed, cluster name_in_source='Dopa') | SUPT: APPROXIMATE; CLUS: CONSISTENT |
| Th expression | POSITIVE (protein, primary defining marker) | Precomputed mean_expression=2.72 | Precomputed mean_expression=6.6; VMAT2 (Slc18a2) is a DEFINING cluster marker | SUPT: APPROXIMATE; CLUS: CONSISTENT |
| Kiss1 expression | POSITIVE (transcript, co-expressed with Th) | Precomputed mean_expression=0.62 | Precomputed mean_expression=2.51; Kiss1 is a cluster-level DEFINING marker | SUPT: APPROXIMATE; CLUS: CONSISTENT |
| Sex ratio | Female-biased (2–4× more TH+ neurons in females) | not available at supertype level | male_female_ratio=0.02 (extreme female bias, ~50:1 F:M) [CS20230722_CLUS_1915] | CONSISTENT |
| Annotation transfer | — | NOT_ASSESSED | NOT_ASSESSED | — |

---

## 5. Candidate paragraphs

## 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] · 🟡 MODERATE

### Supporting evidence

- CLUS_1915 is the top-ranked rank-0 (cluster-level) candidate for avpv_th_neuron based on atlas metadata queries (DB score=6).
- Th mean expression = 6.6 — the highest in the SUPT_0486 lineage — and VMAT2 (Slc18a2), the vesicular monoamine transporter, is a DEFINING cluster marker, providing independent dopaminergic identity support beyond the Th transcript alone.
- Kiss1 mean expression = 2.51 at cluster level, and Kiss1 is listed as a cluster-level DEFINING marker for CLUS_1915 — consistent with the near-complete Kiss1/TH co-expression documented classically in the AVPV/PeN [3][5].
- The cluster carries nt_type=Dopa (confirmed at cluster level), fully resolving the GABAergic supertype label seen at the SUPT_0486 level.
- male_female_ratio=0.02 in CLUS_1915 represents extreme female bias (~50:1 F:M), directly concordant with the 2–4× female excess of AVPV TH neurons documented in [4]. This is the most female-biased cluster in the candidate set.
- MBA:272 (AVPV) cells are present in CLUS_1915. Although cell counts are low (n=1), this is consistent with the very small absolute number of AVPV TH cells expected from atlas sampling.
- Three independent convergent signals — Th expression (highest in lineage), dopaminergic NT type (Dopa confirmed), and extreme female sex ratio — all support CLUS_1915 as the best cluster-level match.

### Marker evidence provenance

- **Th:** Defined by immunoreactivity (protein-level) across multiple independent classical studies [1][2][4]. At cluster level, Th transcript mean = 6.6 and Slc18a2 (VMAT2) is a DEFINING marker, providing transcript- and transporter-level corroboration. The protein/transcript cross-modality approximation is a standard limitation, but the convergence of Th, Slc18a2, and Dopa NT type at cluster level strengthens this alignment beyond a single-marker comparison.
- **Kiss1:** Defined by mRNA co-expression with TH in AVPV/PeN [3][5]. At cluster level Kiss1 = 2.51 and Kiss1 is a DEFINING marker for CLUS_1915, suggesting this cluster captures the Kiss1/TH co-expressing subset identified classically. This is a marked improvement over the supertype-level signal (0.62), consistent with Kiss1 being diluted across the broader preoptic territory at supertype level.
- No negative markers are defined for this classical type.

### Concerns

- **LOW_CELL_COUNT:** CLUS_1915 has only n=3–5 total cells in the atlas. All directional metrics (Th, Kiss1, MFR, Dopa NT) are concordant, but statistical power is limited. Confidence is capped at MODERATE.
- **Ambiguous mapping with avpv_kiss1_neuron (AMBIGUOUS_MAPPING):** avpv_th_neuron and avpv_kiss1_neuron both map to CLUS_1915. The two classical types are substantially overlapping — most AVPV Kiss1 cells co-express TH [3] — and may represent the same cell population described from different entry points in the classical literature. Whether they are biologically separable within CLUS_1915 cannot be resolved from atlas metadata alone.
- **Spatial breadth at cluster level:** CLUS_1915 cells are distributed across MBA:272 (AVPV, n=1), MBA:133 (PVpo, n=1), and MBA:1097 (Hypothalamus, n=3). The small cell count prevents sub-regional resolution; AVPV representation is present but not dominant.

### What would upgrade confidence

- Run MapMyCells annotation transfer of Th-Cre AVPV scRNA-seq data to WMBv1 and compute F1 scores at cluster level for CLUS_1915. An F1 ≥ 0.80 at CLUSTER level would upgrade confidence to HIGH.
- Targeted literature search for datasets from Th-Cre or Kiss1-Cre AVPV cell isolation that could serve as input for annotation transfer.
- Cluster-level Kiss1/Th/Esr1 co-expression profiling within SUPT_0486 to confirm that CLUS_1915 specifically corresponds to the A14 TH/Kiss1 cluster and to determine whether avpv_th_neuron and avpv_kiss1_neuron can be distinguished at cluster resolution.

---

## 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] · 🟡 MODERATE

### Supporting evidence

- SUPT_0486 is the top-ranked rank-1 (supertype-level) candidate for avpv_th_neuron based on atlas metadata queries.
- Th mean expression = 2.72 at supertype level, consistent with TH-expressing identity of the classical AVPV TH neuron.
- Esr1 mean expression = 7.72 at supertype level, corroborating the estrogen responsiveness of AVPV Kiss1/TH neurons — consistent with the positive estradiol-feedback role documented classically [3].
- Kiss1 mean expression = 0.62 at supertype level. *(note: this is lower than expected given near-complete Kiss1/TH co-expression classically; likely reflects dilution across the broader preoptic territory before cluster-level resolution — cluster-level Kiss1 = 2.51 in CLUS_1915.)*
- Direct AVPV [MBA:272] cell representation within SUPT_0486: n=16 cells, supporting anatomical concordance.
- Child cluster CLUS_1915 carries nt_type=Dopa and male_female_ratio=0.02, providing cluster-level evidence anchored under this supertype.
- Three independent signals converge at supertype level: Th expression, AVPV anatomical representation, and extreme female sex bias in child cluster CLUS_1915.

### Marker evidence provenance

- **Th:** Same protein-level definition as for CLUS_1915 above. At supertype level Th = 2.72 (lower than cluster-level 6.6), which is expected given averaging across the broader preoptic population including non-TH cells.
- **Kiss1:** At supertype level Kiss1 = 0.62. *(note: dilution across PVpo, MPN, and AVPV contributions is the most likely explanation, given that cluster-level Kiss1 = 2.51 in CLUS_1915.)* The low supertype signal should not be interpreted as Kiss1 absence.
- **Esr1:** High mean expression (7.72) is consistent with estrogen responsiveness of this population but Esr1 is not a primary classical defining marker; treat as corroborating.

### Concerns

- **NT label mismatch (NT_PREDICTION_UNCERTAIN):** SUPT_0486 carries a "Gaba_5" label at supertype level, implying majority GABAergic identity. The dopaminergic designation is resolved only at child cluster level (CLUS_1915). *(note: supertype NT labels in WMBv1 reflect the dominant NT category within the supertype; a minority dopaminergic cluster nested within a GABAergic supertype is plausible but should be verified at cluster level before asserting dopaminergic identity for the supertype as a whole.)*
- **Ambiguous mapping with avpv_kiss1_neuron (AMBIGUOUS_MAPPING):** avpv_th_neuron and avpv_kiss1_neuron both map to SUPT_0486, reflecting the substantial classical overlap between these populations. Whether they resolve to separable clusters within SUPT_0486 cannot be determined from supertype-level data.
- **Spatial breadth of supertype:** SUPT_0486 spans PVpo (n=64), MPN (n=37), and AVPV (n=16). The majority of cells are from preoptic regions outside AVPV. The avpv_th_neuron likely corresponds to the AVPV-localised subset captured at cluster level by CLUS_1915 rather than the full supertype.
- **Kiss1 signal lower than expected at supertype level:** Supertype-level Kiss1 = 0.62 vs. near-complete Kiss1/TH co-expression described classically [3]. Cluster-level analysis (CLUS_1915 Kiss1 = 2.51) resolves this concern; the supertype signal reflects dilution.

### What would upgrade confidence

- As for CLUS_1915: annotation transfer (MapMyCells, Th-Cre or Kiss1-Cre AVPV data) with F1 ≥ 0.80 at cluster level is the primary upgrade pathway.
- Confirm cluster-level Th/Kiss1/Esr1 co-expression in CLUS_1915 as the AVPV-specific subpopulation anchored under SUPT_0486.

---

## 6. Proposed experiments

### Cross-check against existing evidence

No AnnotationTransferEvidence items exist on any edge for avpv_th_neuron. The annotation transfer experiment is outstanding.

### Annotation transfer (MapMyCells)

| Item | Detail |
|---|---|
| **What** | MapMyCells annotation transfer of AVPV TH-lineage single-cell RNA-seq data to WMBv1 |
| **Target source data** | Th-Cre or Kiss1-Cre FACS-sorted or spatially captured AVPV neurons |
| **Atlas target** | WMBv1 (CCN20230722) |
| **Quantitative threshold** | F1 ≥ 0.80 at CLUSTER level for CLUS_1915 [CS20230722_CLUS_1915] |
| **Expected output** | AnnotationTransferEvidence entries on both edges (SUPT_0486 and CLUS_1915) |
| **Resolves** | Whether CLUS_1915 specifically corresponds to classical AVPV A14 TH neurons; whether avpv_th_neuron and avpv_kiss1_neuron resolve to the same or different clusters within SUPT_0486 (open questions 1, 2, 4) |

### Cluster-level co-expression profiling

| Item | Detail |
|---|---|
| **What** | Targeted query of CLUS_1915 Th/Kiss1/Esr1 co-expression in atlas data |
| **Target** | CLUS_1915 [CS20230722_CLUS_1915] within SUPT_0486 [CS20230722_SUPT_0486] |
| **Expected output** | LiteratureEvidence or ATLAS_METADATA evidence item confirming or refuting Kiss1/TH co-expression at cluster level |
| **Resolves** | Open questions 1 and 3 |

---

## 7. Open questions

1. Does CLUS_1915 specifically correspond to AVPV A14 TH neurons? Confirm by cluster-level Kiss1/Th/Esr1 co-expression profiling within SUPT_0486. *(Applies to both edges.)*
2. Are avpv_th_neuron and avpv_kiss1_neuron separable at the cluster level within SUPT_0486, or do they both map to CLUS_1915 as a single overlapping population? *(Applies to both edges.)*
3. What is the Kiss1 mean expression specifically within CLUS_1915 (as opposed to supertype level), and does it approach the near-complete Kiss1/TH co-expression described classically [3]? *(Partial resolution: cluster-level Kiss1 = 2.51 and Kiss1 is a DEFINING marker for CLUS_1915; full co-expression profiling needed.)*
4. Does the "Gaba_5" supertype NT label for SUPT_0486 reflect a genuine biological heterogeneity (GABAergic + dopaminergic co-population) or a classification artefact? Resolved at cluster level for CLUS_1915 (Dopa confirmed) but not for the supertype as a whole.

---

## 8. Evidence base table

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_avpv_th_neuron_to_cs20230722_clus_1915 | ATLAS_METADATA — Th mean=6.6 (highest in SUPT_0486 lineage), Kiss1 mean=2.51 (DEFINING), Slc18a2/VMAT2 DEFINING marker | SUPPORT |
| edge_avpv_th_neuron_to_cs20230722_clus_1915 | ATLAS_METADATA — nt_type=Dopa (confirmed at cluster level) | SUPPORT |
| edge_avpv_th_neuron_to_cs20230722_clus_1915 | ATLAS_METADATA — male_female_ratio=0.02 (extreme female bias ~50:1 F:M) | SUPPORT |
| edge_avpv_th_neuron_to_cs20230722_clus_1915 | ATLAS_METADATA — MBA:272 (AVPV) cells present; n=3–5 total cells (low count) | SUPPORT (limited statistical power) |
| edge_avpv_th_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA — Th mean=2.72, Esr1 mean=7.72, Kiss1 mean=0.62 at supertype level | SUPPORT |
| edge_avpv_th_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA — AVPV [MBA:272] n=16 cells within SUPT_0486 | SUPPORT |
| edge_avpv_th_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA — child cluster CLUS_1915 nt_type=Dopa, male_female_ratio=0.02 | SUPPORT |
| edge_avpv_th_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA — SUPT_0486 NT supertype label = Gaba_5; dopaminergic identity unresolved at supertype level | CONCERN (NT_PREDICTION_UNCERTAIN) |
| edge_avpv_th_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA — SUPT_0486 spans PVpo (n=64), MPN (n=37), AVPV (n=16); AVPV-localised cells are a minority | CONCERN (spatial breadth) |
| Both edges | ATLAS_METADATA — avpv_th_neuron and avpv_kiss1_neuron both map to CLUS_1915/SUPT_0486 | CONCERN (AMBIGUOUS_MAPPING) |

---

## 9. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | https://doi.org/10.1007/s12031-012-9923-1 | — | Soma location, Th marker |
| [2] | Z et al. 2013 · PMID:25206587 | 25206587 | Soma location, Th marker |
| [3] | S et al. 2017 · PMID:28660243 | 28660243 | Soma location, NT (dopaminergic), Kiss1 marker, Kiss1/TH co-expression in AVPV/PeN |
| [4] | N et al. 2021 · PMID:33910083 | 33910083 | Th marker, sex ratio (female-biased, 3–4×) |
| [5] | A et al. 2007 · PMID:17699664 | 17699664 | Kiss1 marker |
