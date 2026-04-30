# MPOA estrogen receptor 1 (Esr1) neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Introduction

### Classical type

**MPOA estrogen receptor 1 (Esr1) neuron** is defined by neurochemical criteria —
Esr1, Ar, and Pgr expression — in the medial preoptic area (MPOA). The
population is functionally heterogeneous: MPOA Esr1 neurons (alongside galanin
neurons) are required for pup-directed/parental behavior, Esr1 governs male-type
mating behavior, and an overlapping Nts (neurotensin)+ subtype governs female
socio-sexual behaviors. The MPOA contains both GABAergic and glutamatergic
neurons, and the Esr1+ population spans both NT subtypes — the classical node
may be better represented as multiple cell-type terms. No CL term has been
assigned and one is a candidate for new term(s).

| Property | Value | References |
|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:464] | [1] |
| Defining markers | Esr1 (transcript), Ar (transcript), Pgr (transcript) | [1], [2] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location (MPOA):** review · mouse · [1]
  > A large hypothalamic structure, the MPOA sends projections to multiple downstream brain regions and is both larger and contains more neurons in males than in females [35]. Notably, the MPOA is home to various heterogeneous, molecularly defined, neuronal clusters, including many sexually dimorphic populations, such as androgen receptor (AR)-expressing population and estrogen receptor alpha (ESR1)expressing population [80]
  > — Zilkha et al. 2021, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 233446934_5d0fb07e -->

- **Esr1 / parental behavior context:** review · mouse · [1]
  > At least two different subpopulations within the MPOA were shown to be required for the regulation of pupdirected behavior. The first is the ESR1 þ population, which is highly sexually dimorphic in its distribution and projection patterns [85]
  > — Zilkha et al. 2021, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 233446934_9f0f55ea -->

</details>

---

## Results

### Mapping candidates

Two co-primary mapping edges are recorded for mpoa_esr1_neuron, reflecting that
the classical population is heterogeneous in NT type. SUPT_0486 (GABAergic,
PVpo-VMPO-MPN) captures the GABAergic Esr1+ fraction with direct atlas-marker
support; SUPT_0521 (glutamatergic, AVPV-MEPO-SFO Tbr1 Glut_3) is independently
identified as the dominant POA-Esr1+ supertype by Knoedler 2022 bulk
correlation [3]. Both are CROSS_CUTTING relationships and the classical node
likely requires a glut/GABA split.

| Rank | WMBv1 cluster | Supertype | Cells (MERFISH) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] | (self) | n=117 (16 AVPV / 64 PVpo / 37 MPN) | 🟡 MODERATE | Esr1/Ar/Pgr CONSISTENT; NT APPROXIMATE (GABA only) | Best candidate (GABAergic fraction) |
| 2 | 0521 AVPV-MEPO-SFO Tbr1 Glut_3 [CS20230722_SUPT_0521] | (self) | not reported | 🟡 MODERATE | Esr1 CONSISTENT; NT APPROXIMATE (Glut only); location APPROXIMATE | Best candidate (glutamatergic fraction) |

2 edges total. Relationship type: CROSS_CUTTING (both edges).

### Property alignment — primary candidate (SUPT_0486)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:464] | MBA:515 (MPN) n=37; MBA:133 (PVpo) n=64; MBA:272 (AVPV) n=16 | not assessed | CONSISTENT |
| NT type | mixed (GABAergic and glutamatergic, both documented in MPOA) | GABAergic (PVpo-VMPO-MPN Hmx2 Gaba subclass) | not assessed | APPROXIMATE |
| Esr1 expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=7.72 (DEFINING atlas marker) | not assessed | CONSISTENT |
| Ar expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=8.15 | not assessed | CONSISTENT |
| Pgr expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=6.80 | not assessed | CONSISTENT |
| Sex ratio | not documented on classical node | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| SUPT_0486 atlas metadata (Esr1/Ar/Pgr, MPN n=37) | Atlas metadata | SUPPORT | Esr1=7.72 (DEFINING), Ar=8.15, Pgr=6.80; MBA:515 MPN n=37 | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

### Property alignment — co-primary candidate (SUPT_0521)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:464] | Anteroventral periventricular nucleus, Median preoptic nucleus | CLUS_2085 primary soma in Anteroventral periventricular nucleus | APPROXIMATE |
| NT type | mixed (GABAergic and glutamatergic, both documented in MPOA) | Glutamatergic (Tbr1 Glut_3 label) | not assessed | APPROXIMATE |
| Esr1 expression | POSITIVE (transcript, primary defining marker) | Esr1+ by experimental design (TRAP-Cre line) | not assessed | CONSISTENT |
| Sex ratio | not documented on classical node | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Knoedler 2022 TRAP-seq POA_FR vs VMH_FR | Bulk transcriptomic correlation | SUPPORT | best child CLUS_2085 (rank 1 of 5322, δ=0.0151); 4 SUPT_0521 children in top 10 | [3] |

*(4 of SUPT_0521's child clusters — CLUS_2085, CLUS_2087, CLUS_2082, CLUS_2079 — appear in the top 10 atlas clusters by POA_FR vs VMH_FR Esr1+ TRAP differential; CLUS_2085 ranks first overall. Best match: CLUS_2085.)*

---



### 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] · 🟡 MODERATE

### Supporting evidence

- **All three classical defining markers reach CONSISTENT alignment at supertype level.** Precomputed mean expression Esr1 = 7.72 (DEFINING atlas marker), Ar = 8.15, and Pgr = 6.80 — directly matching the steroid hormone receptor profile that defines mpoa_esr1_neuron [1], [2].
- **Direct anatomical anchor in MPN.** SUPT_0486 carries n = 37 cells in Medial preoptic nucleus [MBA:515], which is the same structure as the classical node's soma assignment Medial preoptic nucleus [MBA:464] *(note: MBA:515 and MBA:464 both label MPN — the location is concordant)*.
- **GABAergic component matches.** The supertype label PVpo-VMPO-MPN Hmx2 Gaba_5 is concordant with the GABAergic fraction of the mixed-NT classical population.
- **Adjacent preoptic territory captured.** Additional cells in Periventricular preoptic nucleus [MBA:133] (n=64) and Anteroventral periventricular nucleus [MBA:272] (n=16) are within the broader medial preoptic zone.

### Marker evidence provenance

- **Esr1** — classical evidence is transcript-based (review citations) [1], [2]. Atlas precomputed Esr1 = 7.72 is transcript-based (10x Chromium) and Esr1 is a DEFINING atlas marker for SUPT_0486. Strong cross-platform agreement.
- **Ar** — classical evidence is transcript-based [1], [2]. Atlas precomputed Ar = 8.15 (transcript). Highest of the three steroid receptors at supertype level. Consistent.
- **Pgr** — classical evidence is from a single preprint citation [2]. Atlas precomputed Pgr = 6.80 (transcript). Supports the classical assertion; *(note: a single primary citation underlies the classical Pgr claim and a targeted cite-traverse for "MPOA progesterone receptor Esr1 co-expression" could strengthen this provenance)*.

### Concerns

- **NT-type alignment is APPROXIMATE — supertype captures only the GABAergic fraction.** SUPT_0486 is GABAergic; the classical mpoa_esr1_neuron population includes glutamatergic Esr1+ neurons that map elsewhere (specifically to SUPT_0521 — see co-primary candidate below). The supertype assignment alone does not represent the full classical population.
- **Functional heterogeneity is unresolved.** The classical node spans multiple functional subtypes — parental (alongside galanin), male-type mating, and Nts+ female socio-sexual — that likely distribute across multiple clusters within SUPT_0486 *(distributed across clusters caveat from edge YAML)*.
- **Child-cluster breakdown not assessed.** No specific child cluster of SUPT_0486 has been identified as carrying peak Esr1/Ar/Pgr or strongest MPN anatomical signal.
- **Sex ratio not assessed.** Sex dimorphism is documented for MPOA generally [1] but is not in the classical node's properties or the supertype atlas metadata; child-cluster MFR data have not been collected for this edge.

### What would upgrade confidence

- **Child-cluster expression analysis** within SUPT_0486 to identify the cluster(s) with peak Esr1/Ar/Pgr and strongest MPN signal (resolves open question 1). Expected output: cluster-level edge with `ATLAS_METADATA` evidence and potential CONSISTENT location alignment at MPN.
- **MapMyCells annotation transfer** of a published MPOA Esr1+ scRNA-seq dataset (e.g. Moffitt 2018) against WMBv1 at cluster resolution; F1 ≥ 0.50 at SUPT_0486 would support the supertype assignment, with the F1 split between SUPT_0486 and SUPT_0521 directly testing the NT heterogeneity. Expected output: `AnnotationTransferEvidence`.
- **Targeted literature search** for the Nts+ MPOA Esr1+ subpopulation to determine whether it co-maps to SUPT_0486 (resolves open question 2).

---

### 0521 AVPV-MEPO-SFO Tbr1 Glut_3 [CS20230722_SUPT_0521] · 🟡 MODERATE

### Supporting evidence

- **Independent quantitative bulk-correlation evidence ranks SUPT_0521 first across the atlas [3].**
  > Knoedler 2022 (PMID:35143761) Esr1+ TRAP-seq pooled POA female-receptive vs VMH female-receptive. SUPT_0521 (AVPV-MEPO-SFO Tbr1 Glut_3, glutamatergic) child cluster CLUS_2085 ranks #1 of 5,322 atlas clusters by δ = ρ(POA_FR) − ρ(VMH_FR), with δ=0.0151 and primary soma in the Anteroventral periventricular nucleus. Three additional SUPT_0521 child clusters (2087, 2082, 2079) appear in the top 10. This is the dominant POA-Esr1+ supertype by bulk correlation — but is glutamatergic, not GABAergic like the existing SUPT_0486 mapping. Suggests the classical mpoa_esr1_neuron node may be heterogeneous and need a glut/GABA split, or that SUPT_0486 captures only a subset of the classical population.
  > — Knoedler et al. 2022 · [3]
- **Esr1 identity is CONSISTENT by experimental design.** SUPT_0521 cells were captured in a Esr1+ TRAP-Cre line — Esr1 expression is established by the input contrast itself, independent of atlas precomputed values [3].
- **Glutamatergic NT identity is captured.** The Tbr1 Glut_3 label resolves the glutamatergic fraction of the classical mixed-NT MPOA Esr1+ population that SUPT_0486 (GABAergic) does not represent.
- **Multiple SUPT_0521 child clusters cluster together at the top of the differential.** Four child clusters in the top 10 of 5,322 indicates the differential signal is supertype-coherent rather than driven by a single cluster.

### Marker evidence provenance

- **Esr1** — classical evidence is transcript-based (ISH and review citations) [1], [2]. SUPT_0521 Esr1 status is inferred from TRAP-Cre transgenic capture rather than from atlas precomputed expression alone — this is a stronger experimental confirmation of Esr1 expression than precomputed mean values *(note: precomputed Esr1 expression for SUPT_0521 is not surfaced in this facts file and would strengthen the cross-platform comparison)*.
- **Ar / Pgr** — not assessed for SUPT_0521 in this edge. The classical node's defining marker set (Esr1, Ar, Pgr) is only partially evaluated against SUPT_0521; Ar and Pgr expression at this supertype/its child clusters has not yet been compared.

### Concerns

- **Location is APPROXIMATE — SUPT_0521 spans AVPV/MePO, not MPN proper.** The classical mpoa_esr1_neuron is anchored at Medial preoptic nucleus [MBA:464]; SUPT_0521's primary somas are in Anteroventral periventricular nucleus and Median preoptic nucleus. AVPV/MePO is part of the broader medial preoptic area but is anatomically distinct from MPN proper *(adjacent region — could reflect the classical node's "MPOA" being broader than MPN, or could indicate the classical node should be narrowed to MPN-specific Esr1+ neurons; weak counter-evidence)*.
- **Atlas dissection overlap caveat.** Knoedler's "POA" dissection captures a broader preoptic zone than MPN proper; AVPV and MePO Esr1+ neurons (anatomically anterior to MPN) are likely included in the bulk pool and contribute to the SUPT_0521 signal. The bulk-correlation evidence cannot distinguish MPN-Esr1+ from AVPV/MePO-Esr1+ contributions [3].
- **NT-type alignment is APPROXIMATE — supertype captures only the glutamatergic fraction.** Mirror-image of the SUPT_0486 concern: SUPT_0521 represents the glutamatergic Esr1+ POA cells while SUPT_0486 represents the GABAergic fraction. Neither alone covers the full classical population.
- **Co-primary mapping ambiguity.** This edge is co-primary alongside SUPT_0486; the two supertypes capture different NT-typed Esr1+ preoptic populations. The classical node likely needs to be split (mpoa_esr1_neuron_GABAergic vs mpoa_esr1_neuron_glutamatergic) or narrowed to MPN proper.
- **Ar / Pgr not assessed at this supertype.** Two of the three classical defining markers have not been quantified for SUPT_0521.

### What would upgrade confidence

- **ISH or MERFISH co-staining for Esr1, Slc17a6 (vGlut2), Slc32a1 (vGAT) in MPOA** to quantify the GABAergic vs glutamatergic fractions of Esr1+ cells (proposed experiment 1). Expected output: `MarkerAnalysisEvidence` documenting the empirical NT split.
- **MapMyCells annotation transfer of published MPOA Esr1+ scRNA-seq data (e.g. Moffitt 2018) to SUPT_0521 vs SUPT_0486** (proposed experiment 2); expect F1 to split between the two supertypes, directly testing the glut/GABA hypothesis. Expected output: `AnnotationTransferEvidence` on both edges. Target: F1 ≥ 0.50 at supertype level for the matched NT fraction in each case.
- **Quantification of Ar and Pgr precomputed expression for SUPT_0521 and its top-ranked child clusters** to complete the defining-marker comparison.
- **Anatomical / functional literature search** to determine whether the AVPV/MePO Esr1+ population (SUPT_0521) is functionally distinct from MPN Esr1+ (SUPT_0486) in the parental/mating circuit literature (resolves open question 4).

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** See classical type table in Introduction; defining_basis on the classical node and per-property literature support are listed there. The KB-side definition lives at the source graph file linked in the reproducibility footer.

**Atlas mapping query.** Candidate atlas clusters were retrieved from CCN20230722 at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property was compared to the corresponding atlas-side value via the `property_comparisons` schema; alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Bulk transcriptomic correlation.** Knoedler 2022 (PMID:35143761) Esr1+ TRAP-seq pooled POA female-receptive vs VMH female-receptive. SUPT_0521 child cluster CLUS_2085 ranks #1 of 5,322 atlas clusters by δ. Run record: [`kb/correlation_runs/20260428_knoedler_esr1_wmbv1/manifest.yaml`](../../kb/correlation_runs/20260428_knoedler_esr1_wmbv1/manifest.yaml). Script: [`correlate.py`](https://github.com/Cellular-Semantics/evidencell/blob/4e67d6b/kb/correlation_runs/20260428_knoedler_esr1_wmbv1/correlate.py)

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote.

*Generated by evidencell `0c97cfa` from [`kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`](../../kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

</details>

---

## Discussion

**Primary mapping:** → SUPT_0486 (GABAergic) and SUPT_0521 (glutamatergic) at MODERATE (co-primary) confidence. Key support: ATLAS_METADATA (Esr1=7.72 DEFINING at SUPT_0486) and BULK_CORRELATION (Knoedler 2022 [3]) for SUPT_0521. Key caveats: `AMBIGUOUS_MAPPING` (glut/GABA split — classical node may need to be split into GABAergic/glutamatergic subnodes).

No Cell Ontology term currently assigned for this classical type.

### Proposed experiments and follow-ups

### 1. ISH / MERFISH co-staining for Esr1 with Slc17a6 (vGlut2) and Slc32a1 (vGAT) in MPOA

**What:** Multiplexed in situ co-staining of Esr1 with Slc17a6 and Slc32a1 across MPOA subregions (MPN, PVpo, AVPV, MePO).

**Target:** Quantitative GABAergic vs glutamatergic fractions of Esr1+ cells per subregion.

**Expected output:** `MarkerAnalysisEvidence` documenting the empirical NT split, supporting the proposed glut/GABA decomposition of mpoa_esr1_neuron.

**Resolves:** Open questions 3 and 4. Directly tests whether mpoa_esr1_neuron should be split into GABAergic and glutamatergic subnodes.

### 2. MapMyCells annotation transfer of an MPOA Esr1+ scRNA-seq dataset against WMBv1

**What:** Retrieve a published MPOA Esr1+ scRNA-seq dataset (e.g. Moffitt 2018) and run MapMyCells against WMBv1 at cluster resolution.

**Target:** F1 ≥ 0.50 at supertype level on whichever NT fraction is matched (GABAergic cells → SUPT_0486; glutamatergic cells → SUPT_0521); F1 split between SUPT_0486 and SUPT_0521 expected.

**Expected output:** `AnnotationTransferEvidence` entries on both edges (edge_mpoa_esr1_neuron_to_cs20230722_supt_0486 and edge_mpoa_esr1_neuron_to_cs20230722_supt_0521). Atlas: WMBv1. Tool: MapMyCells. Output: F1 matrix per cluster.

**Resolves:** Open questions 1, 3, and 4. Confirms or refutes the co-primary glut/GABA mapping; identifies best child clusters within each supertype.

### 3. Targeted child-cluster expression analysis within SUPT_0486 and SUPT_0521

**What:** Inspect precomputed expression for Esr1, Ar, Pgr, Nts, and Gal across all child clusters of SUPT_0486 and SUPT_0521; identify clusters with peak co-expression and strongest MPN/AVPV anatomical signal.

**Target:** Identification of best child cluster(s) for each supertype edge with quantitative thresholds (e.g. Esr1 mean ≥ 5.0 and MPN cell count ≥ 10).

**Expected output:** Cluster-level mapping edges with `ATLAS_METADATA` evidence; potential resolution of the Nts+ female socio-sexual subpopulation.

**Resolves:** Open questions 1 and 2.

---

### Open questions

1. Which clusters within SUPT_0486 [CS20230722_SUPT_0486] have highest Esr1/Ar/Pgr and strongest MPN anatomical signal? *(SUPT_0486 edge.)*
2. Does the Nts+ female socio-sexual subpopulation map to SUPT_0486 or to a separate preoptic supertype? *(SUPT_0486 edge.)*
3. Should mpoa_esr1_neuron be split into GABAergic (SUPT_0486) and glutamatergic (SUPT_0521) subnodes, or narrowed to MPN-proper Esr1+ neurons? *(SUPT_0521 edge; central organising question across both edges.)*
4. Is the AVPV/MePO Esr1+ population (SUPT_0521) functionally distinct from MPN Esr1+ (SUPT_0486) in the parental/mating circuit literature? *(SUPT_0521 edge.)*

---

### Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_mpoa_esr1_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA | SUPPORT — Esr1=7.72 (DEFINING), Ar=8.15, Pgr=6.80; MBA:515 MPN n=37; GABAergic fraction |
| edge_mpoa_esr1_neuron_to_cs20230722_supt_0521 | BULK_CORRELATION ([3] Knoedler 2022) | SUPPORT — POA_FR vs VMH_FR; CLUS_2085 rank 1/5322 (δ=0.0151); 4 child clusters in top 10; glutamatergic fraction |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Zilkha et al. 2021 | [PMID:33910083](https://pubmed.ncbi.nlm.nih.gov/33910083/) | Soma location (MPOA); Esr1 / Ar marker context; sexually dimorphic MPOA |
| [2] | bioRxiv 2021.09.02.458782 | — | Esr1, Ar, Pgr marker evidence (steroid hormone receptors in MPOA) |
| [3] | Knoedler et al. 2022 | [PMID:35143761](https://pubmed.ncbi.nlm.nih.gov/35143761/) | Esr1+ TRAP-seq POA female-receptive vs VMH female-receptive bulk correlation against WMBv1 |
