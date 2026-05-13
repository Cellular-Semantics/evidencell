# MPOA estrogen receptor 1 (Esr1) neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

The medial preoptic area (MPOA) is a sexually dimorphic hypothalamic structure that contains heterogeneous, molecularly defined neuronal populations, including a prominent estrogen receptor 1 (Esr1)-expressing population required for sex-typical reproductive and parental behaviors [1]. MPOA Esr1+ neurons are required (alongside galanin neurons) for pup-directed/parental behavior, while Esr1 signalling in the MPOA governs male-type mating behavior; an overlapping neurotensin (Nts)+ subset governs female socio-sexual behaviors [1]. Because the MPOA contains both GABAergic and glutamatergic Esr1+ neurons, this classical type is expected to span more than one transcriptomic supertype, and the mapping matters for assigning the correct atlas substrate(s) to each behavioral subcircuit.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:464] (name in source: medial preoptic area, MPOA) | [1] |
| Markers | Esr1, Ar, Pgr | [1], [2] |
| CL term | none assigned | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical literature review · MPOA · [1]
  > A large hypothalamic structure, the MPOA sends projections to multiple downstream brain regions and is both larger and contains more neurons in males than in females [35]. Notably, the MPOA is home to various heterogeneous, molecularly defined, neuronal clusters, including many sexually dimorphic populations, such as androgen receptor (AR)-expressing population and estrogen receptor alpha (ESR1)expressing population [80]
  > — Zilkha et al. 2021, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 233446934_5d0fb07e -->
- **Esr1 marker:** classical review · MPOA Esr1+ population · [1]
  > At least two different subpopulations within the MPOA were shown to be required for the regulation of pupdirected behavior. The first is the ESR1 þ population, which is highly sexually dimorphic in its distribution and projection patterns [85]
  > — Zilkha et al. 2021, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 233446934_9f0f55ea -->
- **Esr1 / Ar / Pgr markers:** transcriptomic + classical review · MPOA steroid receptor expression · [2]
  > Since the MPOA is enriched in the expression of steroid hormone receptors genes (e.g., Esr1, androgen receptor (Ar), progesterone receptor (Pgr))
  > — preprint 2021, Neuronal Markers and Molecular Characteristics · [2] <!-- quote_key: 237425192_b8087ed0 -->
- **Behavioral subdivision (Esr1 vs Nts vs Gal):** classical review · MPOA functional subtypes · [2]
  > Molecularly defined subpopulations of neurons expressing a variety of neuropeptides and/or hormonal receptors in the MPOA are tightly associated with reproductive behaviors. MPOA neurons expressing Gal (galanin) or Esr1 (estrogen receptor 1) are essential for parental behaviors, while MPOA neurons expressing Esr1 or Nts (neurotensin) govern male-type mating behaviors and female socio-sexual behaviors, respectively
  > — preprint 2021, Neuronal Markers and Molecular Characteristics · [2] <!-- quote_key: 237425192_c17e0213 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

The classical node carries no `proposed_cl_term`; the curator notes that the MPOA Esr1 population is heterogeneous (GABAergic and glutamatergic subtypes with distinct behavioral roles) and may be better represented as multiple new CL terms.

---

## Results

Two MODERATE-confidence candidate supertypes were assessed; together they appear to capture distinct NT-typed fractions of the heterogeneous MPOA Esr1+ population — SUPT_0486 (GABAergic, MPN-proper) and SUPT_0521 (glutamatergic, AVPV/MePO/SFO) — rather than a single primary mapping.

### Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---|---:|---|---|---|
| 1 | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] | SUPT_0486 | 178 | 🟡 MODERATE | Esr1/Ar/Pgr CONSISTENT · MPN location CONSISTENT · GABAergic | Best candidate (GABAergic fraction) |
| 2 | 0521 AVPV-MEPO-SFO Tbr1 Glut_3 [CS20230722_SUPT_0521] | SUPT_0521 | 391 | 🟡 MODERATE | Esr1 CONSISTENT · location APPROXIMATE · Glutamatergic | Best candidate (glutamatergic fraction) |

Two candidate edges (`CROSS_CUTTING` relationship for both); no UNCERTAIN or eliminated candidates were emitted at this stage.

### 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 · 🟡 MODERATE

**Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:464] | MBA:515 (MPN) n=37; MBA:133 (PVpo) n=64; MBA:272 (AVPV) n=16 | not assessed | CONSISTENT |
| Esr1 expression | POSITIVE (transcript, defining marker) | mean_expression=7.72 (DEFINING atlas marker) | not assessed | CONSISTENT |
| Ar expression | POSITIVE (transcript, defining marker) | mean_expression=8.15 | not assessed | CONSISTENT |
| Pgr expression | POSITIVE (transcript, defining marker) | mean_expression=6.80 | not assessed | CONSISTENT |
| NT type | mixed (GABAergic and glutamatergic, both documented in MPOA) | GABAergic (PVpo-VMPO-MPN Hmx2 Gaba subclass) | not assessed | APPROXIMATE |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| WMBv1 atlas metadata (SUPT_0486) | Atlas metadata | SUPPORT | Esr1=7.72 (DEFINING), Ar=8.15, Pgr=6.80; MPN n=37 cells | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Supporting evidence**

- SUPT_0486 (PVpo-VMPO-MPN Hmx2 Gaba_5) directly encodes MPN in its label and has Medial preoptic nucleus [MBA:515] (n=37) cells, with additional cells in Periventricular preoptic nucleus [MBA:133] (n=64) and Anteroventral periventricular nucleus [MBA:272] (n=16) — anatomically concordant with the classical MPOA soma assignment [MBA:464].
- All three defining markers of the classical type show high precomputed expression on the supertype: Esr1=7.72 (DEFINING atlas marker), Ar=8.15, Pgr=6.80 — i.e. the supertype is independently flagged Esr1-defining in atlas metadata.

**Marker evidence provenance**

- **Esr1:** transcript-level evidence on the classical side (Zilkha review citing primary work [1]; preprint [2]); CONSISTENT with atlas DEFINING flag at mean=7.72. No atlas annotation/expression discrepancy.
- **Ar:** classical literature (review [1]; preprint [2]). Atlas mean=8.15 — concordant; no discrepancy flag.
- **Pgr:** classical literature (preprint [2] only). Atlas mean=6.80 — concordant. The primary-literature base for Pgr as a *defining* (rather than enriched) MPOA Esr1+ marker is thinner than for Esr1/Ar; a targeted cite-traverse for "progesterone receptor MPOA Esr1 co-expression" would strengthen the evidence chain.

**Concerns**

- NT type APPROXIMATE: the classical population includes both GABAergic and glutamatergic Esr1+ neurons; SUPT_0486 captures only the GABAergic fraction (`caveat_type: AMBIGUOUS_MAPPING`).
- Functional subtypes within MPOA Esr1+ (parental, male mating, female socio-sexual via Nts+ subset) likely distribute across multiple child clusters of SUPT_0486 (`caveat_type: DISTRIBUTED_ACROSS_CLUSTERS`).

**What would upgrade confidence**

- Resolve which SUPT_0486 child clusters carry the highest Esr1/Ar/Pgr means together with the strongest MPN [MBA:515] anatomical signal (open question 1) — adds a cluster-level `ATLAS_METADATA` / `MarkerAnalysisEvidence` row at rank 0.
- Determine whether the Nts+ female socio-sexual subpopulation maps to SUPT_0486 or to a distinct preoptic supertype (open question 2) — addressable by MapMyCells annotation transfer of a published MPOA Esr1+ scRNA-seq dataset, expected output `AnnotationTransferEvidence` with F1 ≥ 0.5 at SUPERTYPE level.

### 0521 AVPV-MEPO-SFO Tbr1 Glut_3 · 🟡 MODERATE

**Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:464] / broader medial preoptic | Anteroventral periventricular nucleus, Median preoptic nucleus | CLUS_2085 top anat: Anteroventral periventricular nucleus (n=29) | APPROXIMATE |
| NT type | mixed (GABAergic and glutamatergic) | Glutamatergic (Tbr1 Glut_3) | not assessed | APPROXIMATE |
| Esr1 expression | POSITIVE (transcript, primary defining marker) | Esr1+ by experimental design (TRAP-Cre line) | not assessed | CONSISTENT |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Knoedler 2022 TRAP-seq (POA_FR vs VMH_FR) | Bulk transcriptomic correlation | SUPPORT | best child CLUS_2085, rank 1/5322, δ=0.0151 | [3] |

*(1 SUPT_0521 child cluster (CLUS_2085) ranks #1 by δ; 3 SUPT_0521 child clusters appear in the top 10 (CLUS_2085, CLUS_2087, CLUS_2086). Best match: CLUS_2085.)*

> Knoedler 2022 (PMID:35143761) Esr1+ TRAP-seq pooled POA female-receptive vs VMH female-receptive. SUPT_0521 (AVPV-MEPO-SFO Tbr1 Glut_3, glutamatergic) child cluster CLUS_2085 ranks #1 of 5,322 atlas clusters by δ = ρ(POA_FR) − ρ(VMH_FR), with δ=0.0151 and primary soma in the Anteroventral periventricular nucleus. Three additional SUPT_0521 child clusters (2087, 2082, 2079) appear in the top 10. This is the dominant POA-Esr1+ supertype by bulk correlation — but is glutamatergic, not GABAergic like the existing SUPT_0486 mapping. Suggests the classical mpoa_esr1_neuron node may be heterogeneous and need a glut/GABA split, or that SUPT_0486 captures only a subset of the classical population.
> — Knoedler et al. 2022 · [3]

![Top 10 clusters by δ for POA_FR_vs_VMH_FR (CS20230722_SUPT_0521)](figures/mpoa_esr1_neuron_POA_FR_vs_VMH_FR_838adb5f.png)

| Rank | Cluster | Supertype | δ | MFR | Top anatomy |
|---:|---|---|---:|---:|---|
| **1** | **CS20230722_CLUS_2085** | **CS20230722_SUPT_0521** | **0.0151** | **1.5** | **Anteroventral periventricular nucleus** |
| 2 | CS20230722_CLUS_1528 | CS20230722_SUPT_0418 | 0.0149 | 1.04 | choroid plexus |
| **3** | **CS20230722_CLUS_2087** | **CS20230722_SUPT_0521** | **0.0141** | **1.33** | **Anteroventral periventricular nucleus** |
| 4 | CS20230722_CLUS_2082 | CS20230722_SUPT_0520 | 0.0140 | 1.86 | Median preoptic nucleus |
| 5 | CS20230722_CLUS_1877 | CS20230722_SUPT_0482 | 0.0140 | 2.57 | optic chiasm |
| 6 | CS20230722_CLUS_1507 | CS20230722_SUPT_0411 | 0.0137 | 1.04 | Anteroventral periventricular nucleus |
| 7 | CS20230722_CLUS_1509 | CS20230722_SUPT_0412 | 0.0136 | 1.7 | Retrochiasmatic area |
| 8 | CS20230722_CLUS_1527 | CS20230722_SUPT_0418 | 0.0132 | 1.56 | Median preoptic nucleus |
| **9** | **CS20230722_CLUS_2086** | **CS20230722_SUPT_0521** | **0.0131** | **1.08** | **Median preoptic nucleus** |
| 10 | CS20230722_CLUS_2079 | CS20230722_SUPT_0520 | 0.0131 | 0.96 | Anteroventral periventricular nucleus |

**Supporting evidence**

- Bulk transcriptomic correlation against Knoedler 2022 Esr1+ TRAP-seq pseudobulks ranks SUPT_0521 child clusters at positions #1 (CLUS_2085), #3 (CLUS_2087), #9 (CLUS_2086) of 5,322 atlas clusters on the POA_FR vs VMH_FR contrast — i.e. SUPT_0521 is the dominant supertype enriched in POA over VMH among Esr1+ pools [3].
- The top-ranked cluster (CLUS_2085) has primary MERFISH soma in Anteroventral periventricular nucleus (n=29), and rank-9 CLUS_2086 sits in Median preoptic nucleus, both anatomically within the broader preoptic zone sampled by Knoedler's "POA" dissection.

**Marker evidence provenance**

- **Esr1:** evidence here is experimental design — the Knoedler TRAP-seq pools are Esr1-Cre-defined by construction [3]; this is a strong inclusion criterion rather than a measured marker call. The atlas side does not provide a SUPT_0521 precomputed Esr1 value in this facts file (gap: target-side Esr1 mean is not in `property_comparisons` for SUPT_0521). Source-side confirmed by TRAP-Cre targeting; target-side Esr1 quantification still unresolvable from this facts extract — a follow-up `gen-facts` with marker comparisons populated would close this.

**Concerns**

- Location APPROXIMATE: SUPT_0521 child clusters localise to Anteroventral periventricular nucleus and Median preoptic nucleus, which are part of the broader medial preoptic region but anatomically anterior to the medial preoptic nucleus proper [MBA:464] *(note: AVPV and MePO are adjacent preoptic subnuclei to MPN — weak/moderate counter-evidence; the classical node may legitimately encompass these subfields or may need narrowing to MPN-proper)*.
- NT type APPROXIMATE: SUPT_0521 is glutamatergic (Tbr1 Glut_3), whereas the classical type spans both GABAergic and glutamatergic Esr1+ MPOA neurons (`caveat_type: AMBIGUOUS_MAPPING`). Co-primary mapping alongside SUPT_0486 (GABAergic) — the classical node likely needs to be split.
- Atlas dissection overlap: Knoedler's "POA" dissection captures a broader preoptic zone than MPN proper; AVPV and MePO Esr1+ neurons anterior to MPN are likely included in the bulk pool and contribute to the SUPT_0521 signal (`caveat_type: OTHER · ATLAS_DISSECTION_OVERLAP`).

**What would upgrade confidence**

- ISH or MERFISH co-staining for Esr1, Slc17a6 (vGlut2), and Slc32a1 (vGAT) in MPOA to quantify the GABAergic vs glutamatergic fractions of Esr1+ cells — would adjudicate the SUPT_0486 vs SUPT_0521 NT split.
- MapMyCells annotation transfer of published MPOA Esr1+ scRNA-seq data (e.g. Moffitt 2018) onto WMBv1 with the expectation of an F1 split between SUPT_0521 and SUPT_0486; expected output `AnnotationTransferEvidence` with per-supertype F1 at SUPERTYPE level.
- Targeted classical-literature follow-up (open question 4) on whether AVPV/MePO Esr1+ neurons are functionally distinct from MPN Esr1+ in the parental/mating circuit literature would help decide between *narrowing* the classical node to MPN proper vs *splitting* by NT type.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** `mpoa_esr1_neuron` is a `CLASSICAL_NEUROCHEMICAL` node defined by Esr1, Ar, and Pgr expression with soma in the Medial preoptic nucleus [MBA:464] (name in source: medial preoptic area, MPOA). Defining-marker citations: Esr1 [1], [2]; Ar [1], [2]; Pgr [2]. Soma location: [1]. NT type is left mixed on the classical side because both GABAergic and glutamatergic Esr1+ MPOA populations are documented; no defining NT call is made on the classical node.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Bulk transcriptomic correlation.**

| Field | Value |
|---|---|
| Source publication | Knoedler et al. 2022 · PMID:35143761 · [3] |
| GEO accession | GSE183092 |
| Technique | TRAP-seq |
| n pools | 12 |
| Atlas | CCN20230722 (SHA-256: b21ca985) |
| Statistic | spearman_rho |
| Parameters | pseudobulk_transform=log1p(sum/n_cells); pool_transform=log1p(replicate_mean(DESeq2_normalised_counts)); gene_id_space=ensembl_mouse_via_symbol_lookup (conf/gene_mapping_CCN20230722.tsv); gene_intersection=intersection_across_4_regions∩atlas_col_names; n_replicates_per_pool=3. |
| Script | [correlate.py](https://github.com/Cellular-Semantics/evidencell/blob/4e67d6b/kb/correlation_runs/corr_run_20260428_knoedler_esr1_wmbv1/correlate.py) |
| Code version | 4e67d6b |
| Caveats | Cross-sex within-region δ contrasts (Male vs FR or Male vs FNR) are artefactual: across all three regions tested (POA, VMH, BNST) the top hits are hindbrain Calcb cholinergic motor neurons — a global male-vs-female expression bias that swamps region-specific signals. Suspected causes: Y-linked/X-inactivation gene dosage, batch effects, sex-specific TRAP-seq pulldown efficiency. METHODOLOGICAL RULE: paired-bulk δ requires the two pools to differ in cell population (region/marker/state) holding sex constant. Cross-sex δ within a single population is not a valid use of this method. TRAP-seq vs scRNA-seq pseudobulk: polysome-bound mRNA shifts absolute ρ values lower than for FACS-bulk inputs (Stephens-style), but Spearman rank-based statistics handle the magnitude offset; δ rankings are comparable across the two run types. |

**Atlas data sources.**

- WMBv1 · CCN20230722 · `conf/mapmycells/CCN20230722/precomputed_stats.h5` · SHA-256 `b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b`.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:19+00:00 from [kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

<details>
<summary>Evidence base table</summary>

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_mpoa_esr1_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA | SUPPORT | atlas-internal |
| edge_mpoa_esr1_neuron_to_cs20230722_supt_0521 | BULK_CORRELATION | SUPPORT | [3] |

</details>

</details>

---

## Discussion

**Primary mapping:** MPOA estrogen receptor 1 (Esr1) neuron → co-primary 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] and 0521 AVPV-MEPO-SFO Tbr1 Glut_3 [CS20230722_SUPT_0521], both at MODERATE confidence. Key support: atlas precomputed Esr1/Ar/Pgr expression on SUPT_0486 plus MPN [MBA:515] cells in its MERFISH distribution; Knoedler 2022 TRAP-seq bulk-correlation δ ranks SUPT_0521 child clusters at #1/3/9 of 5,322 on POA_FR vs VMH_FR. Key caveats: AMBIGUOUS_MAPPING (classical node spans GABAergic and glutamatergic Esr1+ subpopulations) and ATLAS_DISSECTION_OVERLAP (Knoedler POA dissection includes AVPV/MePO anterior to MPN proper). No Cell Ontology term is currently assigned; this classical type is a candidate for new CL term(s), most likely as separate GABAergic and glutamatergic preoptic Esr1+ classes.

### Proposed experiments and follow-ups

**1. NT-typed quantification of MPOA Esr1+ cells in situ**
- **What:** ISH or MERFISH co-staining for Esr1 with Slc17a6 (vGlut2) and Slc32a1 (vGAT) in MPOA.
- **Target:** Per-cell NT classification of Esr1+ MPOA cells; report GABAergic vs glutamatergic fractions per MBA subregion (MBA:464 / MBA:515 / MBA:272 / MBA:133).
- **Expected output:** Updates `mpoa_esr1_neuron` notes / triggers split into GABAergic vs glutamatergic subnodes; informs CL term proposal.
- **Resolves:** open question 3 (NT-split vs MPN-narrowing decision).

**2. Annotation transfer of published MPOA Esr1+ scRNA-seq onto WMBv1**
- **What:** MapMyCells annotation transfer of a published MPOA Esr1+ scRNA-seq dataset (e.g. Moffitt 2018) to CCN20230722.
- **Target:** F1 ≥ 0.5 at SUPERTYPE level; expect F1 to split between SUPT_0486 and SUPT_0521.
- **Expected output:** `AnnotationTransferEvidence` on both edges, plus on any newly implicated supertype harbouring the Nts+ female socio-sexual subset.
- **Resolves:** open question 2 (Nts+ subset destination).

**3. Atlas-side cluster-resolution marker check for SUPT_0486**
- **What:** Re-run `gen-facts` (or a targeted marker query) at rank 0 within SUPT_0486 to report per-cluster Esr1/Ar/Pgr precomputed means alongside per-cluster MBA:515 cell counts.
- **Target:** Identify the SUPT_0486 child cluster(s) with both highest steroid-receptor expression and strongest MPN [MBA:515] anatomical signal.
- **Expected output:** Cluster-level `ATLAS_METADATA` evidence row(s) on the SUPT_0486 edge.
- **Resolves:** open question 1.

**4. Targeted literature follow-up on AVPV/MePO vs MPN Esr1+ functional roles**
- **What:** Targeted cite-traverse for AVPV/MePO Esr1+ vs MPN Esr1+ in parental and mating circuit literature.
- **Target:** Identify whether published functional studies treat AVPV/MePO Esr1+ as a distinct cell type from MPN Esr1+.
- **Expected output:** `LiteratureEvidence` entries informing whether to narrow `mpoa_esr1_neuron` to MPN proper or to keep the broader preoptic scope.
- **Resolves:** open question 4.

### Open questions

1. Which clusters within SUPT_0486 have highest Esr1/Ar/Pgr and strongest MPN anatomical signal? *(edge SUPT_0486)*
2. Does the Nts+ female socio-sexual subpopulation map to SUPT_0486 or to a separate preoptic supertype? *(edge SUPT_0486)*
3. Should `mpoa_esr1_neuron` be split into GABAergic (SUPT_0486) and glutamatergic (SUPT_0521) subnodes, or narrowed to MPN-proper Esr1+ neurons? *(edge SUPT_0521)*
4. Is the AVPV/MePO Esr1+ population (SUPT_0521) functionally distinct from MPN Esr1+ (SUPT_0486) in the parental/mating circuit literature? *(edge SUPT_0521)*

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Zilkha et al. 2021 · PMID:33910083 | [33910083](https://pubmed.ncbi.nlm.nih.gov/33910083/) | soma location |
| [2] | https://doi.org/10.1101/2021.09.02.458782 | — | Esr1 marker |
| [3] | Knoedler et al. 2022 · PMID:35143761 | [35143761](https://pubmed.ncbi.nlm.nih.gov/35143761/) | Knoedler 2022 (PMID:35143761) Esr1+ TRAP-seq pooled POA female-receptive vs VMH |
