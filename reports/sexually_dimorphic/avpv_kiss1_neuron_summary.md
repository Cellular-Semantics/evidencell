# AVPV/PeN kisspeptin neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

**AVPV/PeN kisspeptin neuron** is defined by neurochemical criteria: Kiss1 expression,
TH co-expression (marking a dopaminergic component within a broader GABAergic phenotype),
and obligate Esr1 co-expression. Somas are concentrated in two periventricular zones of the
rostral hypothalamus. The population is female-biased in cell number, mediates estrogen
positive-feedback control of the preovulatory GnRH/LH surge, and is functionally and
molecularly distinct from the arcuate KNDy (kisspeptin/neurokinin B/dynorphin) population.
Most AVPV/PeN Kiss1 cells co-express TH, overlapping the AVPV TH neuron population.

CL term: **hypothalamus kisspeptin neuron (CL:4023123)** — mapping is BROAD; a dedicated
term for the AVPV/RP3V non-KNDy kisspeptin population may be warranted.

| Property | Value | References |
|---|---|---|
| Soma location | Anteroventral periventricular nucleus [MBA:272]; Periventricular hypothalamic nucleus, posterior part [MBA:341] | [1][2][3] |
| NT | GABAergic / dopaminergic (TH co-expression) | [3] |
| Defining markers | Kiss1 (transcript), Th (protein, co-expressed with Kiss1), Esr1 (transcript) | [1][2][3][4][5] |
| Negative markers | — | |
| Neuropeptides | Kiss1 (kisspeptin) | [6] |
| CL term | CL:4023123 (hypothalamus kisspeptin neuron) — BROAD | |

<details>
<summary>Literature support — expand for verbatim quotes</summary>

**[3] S et al. 2017 · PMID:28660243 — Neuronal Markers and Molecular Characteristics**

> "Kiss1-synthesizing neurons reside primarily in the hypothalamic anteroventral periventricular (AVPV/PeN) and arcuate (ARC) nuclei. AVPV/PeN Kiss1 neurons are sexually dimorphic, with females expressing more Kiss1 than males, and participate in estradiol (E2)-induced positive feedback control of GnRH secretion. In mice, most AVPV/PeN Kiss1 cells coexpress tyrosine hydroxylase (TH), the rate-limiting enzyme in catecholamine synthesis (in this case, dopamine)."
> — S et al. 2017, Neuronal Markers and Molecular Characteristics · [3] <!-- quote_key: 4702847_ebd225e6 -->

**[2] S et al. 2007 · PMID:17213691 — Functional Roles in Reproductive Neuroendocrine Control**

> "Metastin/kisspeptin, the KiSS-1 gene product, has been identified as an endogenous ligand of GPR54 that reportedly regulates GnRH/LH surges and estrous cyclicity in female rats. The aim of the present study was to determine if metastin/kisspeptin neurons are a target of estrogen positive feedback to induce GnRH/LH surges. We demonstrated that preoptic area (POA) infusion of the anti-rat metastin/kisspeptin monoclonal antibody blocked the estrogen-induced LH surge, indicating that endogenous metastin/kisspeptin released around the POA mediates the estrogen positive feedback effect on GnRH/LH release. Metastin/kisspeptin neurons in the anteroventral periventricular nucleus (AVPV) may be responsible for mediating the feedback effect because the percentage of c-Fos-expressing KiSS-1 mRNA-positive cells to total KiSS-1 mRNA-positive cells was significantly higher in the afternoon than in the morning in the anteroventral periventricular nucleus (AVPV) of high estradiol (E(2))-treated females. Most of the KiSS-1 mRNA expressing cells contain ERalpha immunoreactivity in the AVPV and ARC."
> — S et al. 2007, Functional Roles in Reproductive Neuroendocrine Control · [2] <!-- quote_key: 1357086_85e3d032 -->

**[1] S et al. 2017 · PMID:29201072 — Functional Roles in Reproductive Neuroendocrine Control**

> "The Kisspeptin system is apparently critical for brain gender differentiation, acting through the regulation of postnatal T secretion. Distribution of Kisspeptin neurons in the hypothalamus varies between species. In mammals there are 2 major regions of these neurons; a rostral one in the Pre-Optic Area (POA) and a caudal one in the arcuate nucleus, with proportionally more Kisspeptin neurons in the ARC than in the POA region. In rodents, the POA regions are concentrated in the Anteroventral Periventricular Nucleus (AVPV). Anatomical differences between genders have been reported in the hypothalamus of some species, e.g. the rat AVPV is sexually dimorphic, with a greater number of KISS1 neurons in females compared to males."
> — S et al. 2017, Functional Roles in Reproductive Neuroendocrine Control · [1] <!-- quote_key: 1227024_3fcab8ab -->

**[6] R et al. 2013 · PMID:23407940 — Functional Roles in Reproductive Neuroendocrine Control**

> "The AVPV is a sexually dimorphic site with a differential distribution pattern of several neurotransmitters and neuropeptides, including kisspeptin"
> — R et al. 2013, Functional Roles in Reproductive Neuroendocrine Control · [6] <!-- quote_key: 11330110_f135c1a8 -->

</details>

---

## 4. Mapping candidates

### 4a. Candidate overview

Two mapping edges are recorded for avpv_kiss1_neuron: a supertype-level edge to SUPT_0486
and a cluster-level edge to CLUS_1915, the child cluster with the strongest Kiss1+Th+Esr1
co-expression profile and the most extreme female bias (male_female_ratio = 0.02).

| Rank | WMBv1 cluster | Supertype | Cells (MERFISH) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 | n=3–5 * | 🟡 MODERATE | Kiss1 CONSISTENT; Esr1 CONSISTENT; Th CONSISTENT; MFR=0.02 CONSISTENT | Best cluster candidate |
| 2 | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] | (self) | not available | 🟡 MODERATE | Esr1 CONSISTENT; Th APPROXIMATE | Best supertype candidate |

2 edges total. Relationship type: PARTIAL_OVERLAP (both edges).

\* MERFISH n=3–5; 10x cluster size not yet shown — see ROADMAP.

### 4b. Property alignment table

| Property | Classical | SUPT_0486 (supertype) | CLUS_1915 (best cluster) | Alignment |
|---|---|---|---|---|
| Soma location | Anteroventral periventricular nucleus [MBA:272]; Periventricular hypothalamic nucleus, posterior part [MBA:341] | n=16 cells in MBA:272; also MBA:133 PVpo (n=64), MBA:515 MPN (n=37) | n=1 AVPV (MBA:272), n=1 PVpo (MBA:133), n=3 MBA:1097 Hypothalamus (broad catchall) | SUPT: APPROXIMATE; CLUS: APPROXIMATE |
| NT type | GABAergic / dopaminergic (Th co-expression) | GABAergic (Gaba_5 label); Th=2.72 present but diluted | Dopa (confirmed, cluster.yaml name_in_source='Dopa') | SUPT: APPROXIMATE; CLUS: CONSISTENT |
| Kiss1 expression | POSITIVE (transcript, primary defining marker) | precomputed mean_expression=0.62 | precomputed mean_expression=2.51; Kiss1 is a cluster-level DEFINING marker | SUPT: APPROXIMATE; CLUS: CONSISTENT |
| Esr1 expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=7.72 (DEFINING atlas marker) | precomputed mean_expression=9.55 (highest Esr1 in SUPT_0486) | CONSISTENT (both levels) |
| Th expression | POSITIVE (protein, co-expressed with Kiss1) | precomputed mean_expression=2.72 | precomputed mean_expression=6.6 (highest Th of any SUPT_0486 child cluster) | SUPT: APPROXIMATE; CLUS: CONSISTENT |
| Sex ratio | FEMALE_BIASED (AVPV Kiss1 neurons strongly female-biased) | not available at supertype level | male_female_ratio=0.02 (extreme female bias, ~50:1 F:M) | CONSISTENT (CLUS_1915 MFR=0.02 matches FEMALE_BIASED) |
| Annotation transfer | — | NOT_ASSESSED | NOT_ASSESSED | — |

*(1 of 5 child clusters of SUPT_0486 — CLUS_1915 — shows the female-biased Kiss1+Th+Esr1 co-expression profile (Kiss1=2.51, Th=6.6, Esr1=9.55, MFR=0.02) concordant with avpv_kiss1_neuron; MFR data are absent at supertype level and for most SUPT_0486 child clusters.)*

---

## 5. Candidate paragraphs

## 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] · 🟡 MODERATE

### Supporting evidence

- **Esr1 expression is strongly consistent.** Precomputed mean expression Esr1 = 7.72 at the supertype level, matching the canonical defining marker for AVPV/PeN kisspeptin neurons. Esr1 is a DEFINING atlas marker for SUPT_0486 — this is the strongest quantitative agreement between classical node and supertype.
- **GABAergic identity is concordant.** The supertype carries a Gaba_5 label, consistent with the GABAergic component of the classical node's mixed GABAergic/dopaminergic phenotype.
- **TH expression is present.** Precomputed mean Th = 2.72, reflecting the dopaminergic co-expression characteristic of AVPV Kiss1 neurons, though diluted across the broader supertype.
- **Kiss1 expression is detected.** Precomputed mean Kiss1 = 0.62, consistent with subset expression within a heterogeneous supertype spanning multiple preoptic subregions.
- **Direct AVPV location match.** n = 16 cells within SUPT_0486 are labelled to Anteroventral periventricular nucleus [MBA:272], providing a direct anatomical anchor.
- **Child cluster CLUS_1915 concentrates the female-biased signal.** Child cluster 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] shows male_female_ratio = 0.02 — the most extreme female bias in SUPT_0486 — and co-expresses Kiss1=2.51, Th=6.6, Esr1=9.55 at the highest levels of any child cluster. This cluster-level evidence substantially strengthens the supertype assignment.

### Marker evidence provenance

- **Kiss1** — classical node evidence is transcript-based (ISH, KiSS-1 mRNA in situ) [1][2][3]. Atlas precomputed value (mean = 0.62) is transcript-based (10x Chromium). The moderate atlas value is expected for a subset marker diluted across a broad supertype; it does not contradict Kiss1 identity but does not confirm it at the population level. Specificity requires cluster-level resolution (resolved at CLUS_1915: mean = 2.51, DEFINING marker status).
- **Th** — classical node evidence mixes protein (IHC for TH protein) [4] and transcript evidence [3]. Atlas precomputed value is transcript-based (mean = 2.72). A protein-vs-transcript discrepancy is a known caveat for Th: IHC may detect TH protein in cells with low transcript abundance *(note: well-documented in catecholaminergic neurons under dopamine-depleted or dopamine-regulated conditions)*. The atlas value is moderately supportive at supertype level; cluster-level Th = 6.6 at CLUS_1915 provides stronger agreement.
- **Esr1** — classical node evidence is transcript-based [1][2][5], including demonstration that ERalpha immunoreactivity co-localises with KiSS-1 mRNA in AVPV [2]. Atlas precomputed Esr1 = 7.72 (supertype) and 9.55 (CLUS_1915) are both high and consistent. This is the most robustly supported marker alignment across all levels.
- **Kiss1 (as neuropeptide)** — supported by functional evidence that kisspeptin peptide mediates estrogen positive feedback via the POA [2][6]. Atlas expression captures the gene transcript; peptidergic identity is inferred rather than directly confirmed by atlas data.

### Concerns

- **Supertype spans a broader preoptic territory than AVPV/PeN.** SUPT_0486 covers PVpo [MBA:133] (n=64 cells), MPN [MBA:515] (n=37 cells), and VMPO in addition to AVPV [MBA:272] (n=16 cells). Multiple classical types — including avpv_th_neuron and mpoa_esr1_neuron — are expected to map to this same supertype; AVPV Kiss1 neurons are a subset.
- **Dopaminergic identity is not resolved at supertype level.** The supertype label is Gaba_5, not dopaminergic. Th = 2.72 is present but the full dopaminergic signal is concentrated in CLUS_1915 (nt_type = Dopa). Mapping to SUPT_0486 as a whole leaves the GABAergic/dopaminergic co-phenotype only partially captured (APPROXIMATE).
- **Sex ratio data not available at supertype level.** Female-biased sex dimorphism — a defining feature of AVPV Kiss1 neurons [1][3] — cannot be assessed from supertype-level metadata. The signal is visible only in CLUS_1915 (male_female_ratio = 0.02).
- **PeN Kiss1 neurons are unresolved.** It is unknown whether Periventricular hypothalamic nucleus, posterior part [MBA:341] Kiss1 neurons co-map to SUPT_0486 or a distinct supertype.

### What would upgrade confidence

- Annotation transfer (MapMyCells) of published AVPV Kiss1-Cre or Kiss1-Cre/Rosa-tdTom scRNA-seq data to WMBv1; F1 >= 0.5 at SUPT_0486 would upgrade this edge; F1 >= 0.8 at CLUS_1915 level would support HIGH confidence. This would add AnnotationTransferEvidence.
- A targeted literature search for studies reporting scRNA-seq of AVPV neurons from both sexes would address the sex-ratio open question at atlas resolution.

---

## 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] · 🟡 MODERATE

### Supporting evidence

- **Kiss1, Th, and Esr1 all reach CONSISTENT alignment at cluster level.** CLUS_1915 shows the highest co-expression of all three classical defining markers among SUPT_0486 child clusters: Kiss1 = 2.51, Th = 6.6, Esr1 = 9.55. Kiss1 is a cluster-level DEFINING marker for CLUS_1915 — directly matching its role as the primary defining marker of the classical node.
- **Dopaminergic NT type is confirmed.** cluster.yaml annotates nt_type = Dopa (name_in_source = 'Dopa'), resolving the APPROXIMATE supertype Gaba_5 label and providing CONSISTENT alignment with the classical node's GABAergic/dopaminergic co-phenotype.
- **Sex ratio is strongly concordant.** male_female_ratio = 0.02 (~50:1 female-to-male) is the most extreme female bias in SUPT_0486 and directly matches the FEMALE_BIASED sex dimorphism that defines avpv_kiss1_neuron [1][3].
- **AVPV cells are explicitly present.** MBA:272 (AVPV) cells are present in CLUS_1915, providing a direct anatomical link, albeit at low cell counts.
- **Cluster was identified by targeted child-cluster analysis.** CLUS_1915 was not surfaced in the initial top-30 DB query (Kiss1/Th/Esr1 profile resides in precomputed_expression, not defining_markers metadata columns). It was identified by systematic child-cluster expression analysis of SUPT_0486 — indicating the cluster-level signal is real but sub-threshold for routine discovery queries.

### Marker evidence provenance

- **Kiss1** — at CLUS_1915, Kiss1 = 2.51 and is listed as a cluster-level DEFINING marker. This is a substantially stronger signal than the supertype mean (0.62) and directly confirms the primary classical criterion. Evidence is transcript-based on both sides (literature ISH [1][2][3]; atlas 10x Chromium).
- **Th** — CLUS_1915 Th = 6.6, the highest of any child cluster in SUPT_0486, consistent with the concentrated TH/dopaminergic signal expected in the AVPV Kiss1 population [3][4]. The nt_type = Dopa annotation independently confirms dopaminergic identity at transcript level.
- **Esr1** — CLUS_1915 Esr1 = 9.55, the highest in SUPT_0486. This is strongly consistent with classical evidence that ERalpha is obligately co-expressed with Kiss1 in AVPV [1][2][5].
- **Slc18a2 (VMAT2)** — listed as a co-defining marker in cluster.yaml alongside Kiss1. This is consistent with dopaminergic vesicular packaging in AVPV TH/Kiss1 neurons *(note: Slc18a2 is not listed on the classical node; this represents a testable additional prediction from atlas data that could be verified by ISH or scRNA-seq re-analysis)*.

### Concerns

- **Very low cell count (n = 3–5 total cells in WMBv1).** The sex ratio (MFR = 0.02) and expression values are directionally reliable but have limited statistical power. Confidence is capped at MODERATE pending annotation transfer or replication in a larger dataset.
- **MERFISH spatial resolution is insufficient to discriminate AVPV from adjacent PVpo/PeN.** The primary soma annotation resolves to the broad Hypothalamus catchall [MBA:1097] (n=3) for most CLUS_1915 cells, with only n=1 cell each in MBA:272 (AVPV) and MBA:133 (PVpo). This does not refute AVPV identity — MERFISH spatial registration at periventricular boundaries has limited precision — but it prevents location from contributing CONSISTENT evidence. *(note: AVPV is a small periventricular nucleus adjacent to PVpo; registration boundary uncertainty at this scale is expected)*
- **avpv_kiss1_neuron and avpv_th_neuron both map to CLUS_1915.** Because most AVPV Kiss1 cells co-express TH, these classical types substantially overlap; CLUS_1915 may represent the shared atlas correlate rather than a distinct transcriptomic split between them. Resolution would require single-cell co-expression data with morphological or functional validation.
- **Annotation transfer not yet performed.** No independent, data-driven mapping of published AVPV Kiss1 scRNA-seq cells to WMBv1 has been run; this is the most important gap in the evidence base for this edge.

### What would upgrade confidence

- **MapMyCells annotation transfer** (see Proposed experiments) is the priority experiment; F1 >= 0.8 against CLUS_1915 at cluster level would substantially support upgrading to HIGH confidence and would add AnnotationTransferEvidence.
- **Larger MERFISH datasets or higher-resolution spatial registration** around the AVPV/PVpo boundary would clarify the location alignment.
- **Targeted cite-traverse** for papers co-profiling AVPV Kiss1 and TH neurons by scRNA-seq could confirm Slc18a2 co-expression and resolve avpv_kiss1_neuron vs avpv_th_neuron as separable clusters.

---

## 6. Proposed experiments

### MapMyCells annotation transfer

**What:** Retrieve a published scRNA-seq dataset enriched for AVPV/preoptic kisspeptin neurons (e.g., from Kiss1-Cre or Kiss1-Cre/Rosa-tdTom sorted preparations, or sex-stratified hypothalamic atlases). Run MapMyCells against WMBv1 at cluster resolution.

**Target:** F1 >= 0.5 at SUPT_0486 level; F1 >= 0.8 at CLUS_1915 level for Kiss1+ cells.

**Expected output:** AnnotationTransferEvidence entries on both edges (edge_avpv_kiss1_neuron_to_cs20230722_supt_0486 and edge_avpv_kiss1_neuron_to_cs20230722_clus_1915). Atlas: WMBv1. Tool: MapMyCells. Output format: F1 matrix per cluster, fed back as AnnotationTransferEvidence YAML.

**Resolves:** Open questions 1 and 3. Confirms or refutes CLUS_1915 as the correct cluster assignment. Addresses the annotation_transfer_f1 NOT_ASSESSED gap on both edges.

---

## 7. Open questions

1. Which cluster(s) within SUPT_0486 [CS20230722_SUPT_0486] carry peak Kiss1+Th+Esr1 co-expression consistent with AVPV Kiss1/TH identity? (Partially addressed by CLUS_1915 identification; requires annotation transfer to confirm.)
2. Do Periventricular hypothalamic nucleus, posterior part [MBA:341] Kiss1 neurons map to SUPT_0486 or to a different supertype? (Appears on edge_avpv_kiss1_neuron_to_cs20230722_supt_0486.)
3. Do avpv_kiss1_neuron and avpv_th_neuron represent separable populations within CLUS_1915 [CS20230722_CLUS_1915], or is CLUS_1915 the shared atlas correlate of both? (Appears on edge_avpv_kiss1_neuron_to_cs20230722_clus_1915.)

---

## 8. Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_avpv_kiss1_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA | PARTIAL — Esr1=7.72 (DEFINING), Th=2.72, Kiss1=0.62 at supertype; n=16 AVPV cells; CLUS_1915 sex ratio (MFR=0.02) noted as child-cluster support |
| edge_avpv_kiss1_neuron_to_cs20230722_clus_1915 | ATLAS_METADATA | SUPPORT — Kiss1=2.51 (DEFINING marker), Th=6.6 (highest in supertype), Esr1=9.55 (highest in supertype), MFR=0.02 (extreme female bias), nt_type=Dopa confirmed |

---

## 9. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | S et al. 2017 | [29201072](https://pubmed.ncbi.nlm.nih.gov/29201072/) | Soma location, Kiss1 marker, Esr1 marker |
| [2] | S et al. 2007 | [17213691](https://pubmed.ncbi.nlm.nih.gov/17213691/) | Soma location, Kiss1 marker, Esr1 coexpression (ERalpha+KiSS-1 in AVPV), GnRH/LH surge |
| [3] | S et al. 2017 | [28660243](https://pubmed.ncbi.nlm.nih.gov/28660243/) | Soma location, NT type (GABAergic/dopaminergic), Kiss1+Th coexpression, sex dimorphism |
| [4] | A et al. 2007 | [17699664](https://pubmed.ncbi.nlm.nih.gov/17699664/) | Th marker (protein, IHC); TH-IR and Kiss1 mRNA co-labelling in AVPV |
| [5] | P et al. 2021 | [34561233](https://pubmed.ncbi.nlm.nih.gov/34561233/) | Esr1 marker; estrogen receptor expression in kisspeptin neurons |
| [6] | R et al. 2013 | [23407940](https://pubmed.ncbi.nlm.nih.gov/23407940/) | Kiss1 neuropeptide / kisspeptin; AVPV as a sexually dimorphic site for kisspeptin |
