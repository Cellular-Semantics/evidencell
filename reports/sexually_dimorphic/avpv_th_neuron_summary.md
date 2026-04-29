# AVPV tyrosine hydroxylase (TH) neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

**AVPV tyrosine hydroxylase (TH) neuron** is defined by neurochemical criteria:
TH (tyrosine hydroxylase) expression marking a dopaminergic phenotype within the
anteroventral periventricular nucleus (AVPV), with substantial Kiss1
co-expression. The population is strongly female-biased (2–4× more TH+ neurons
in females than males) and overlaps extensively with the AVPV/PeN Kiss1 neuron
population — most AVPV/PeN Kiss1 cells co-express TH. The classical type is
distinct from the SDN-POA, where TH-positive cell bodies are absent (only
TH-immunoreactive axons/synapses are observed). No exact CL term currently
exists; a candidate sibling of CL:4072009 ('A12 dopaminergic neuron') for
AVPV/RP3V A14 dopaminergic neurons may be warranted.

| Property | Value | References |
|---|---|---|
| Soma location | Anteroventral periventricular nucleus [MBA:272] | [1], [2], [3] |
| NT | dopaminergic | [3] |
| Defining markers | Th (protein, primary defining marker), Kiss1 (transcript, co-expressed with Th in AVPV) | [1], [2], [3], [4], [5] |
| Negative markers | — | |
| Neuropeptides | — | |

<details>
<summary>Literature support — expand for verbatim quotes</summary>

**[3] Stephens et al. 2017 · PMID:28660243 — Neuronal Markers and Molecular Characteristics**

> Kiss1-syntheizing neurons reside primarily in the hypothalamic anteroventral periventricular (AVPV/PeN) and arcuate (ARC) nuclei. AVPV/PeN Kiss1 neurons are sexually dimorphic, with females expressing more Kiss1 than males, and participate in estradiol (E2)- induced positive feedback control of GnRH secretion. In mice, most AVPV/PeN Kiss1 cells coexpress tyrosine hydroxylase (TH), the rate-limiting enzyme in catecholamine synthesis (in this case, dopamine).
> — Stephens et al. 2017, Neuronal Markers and Molecular Characteristics · [3] <!-- quote_key: 4702847_ebd225e6 -->

**[4] Zilkha et al. 2021 · PMID:33910083 — Sexually Dimorphic Brain Regions and Structures**

> A notable exception is the AVPV of the hypothalamus, which is larger in volume, contains more cells, and sends more projections to multiple reproduction-related brain regions in females compared to males [25,34,71,72,76e[79]. Importantly, it also expresses several sexually dimorphic molecularly defined neuronal populations, including the tyrosine hydroxylase (TH)-expressing population, which contains 3e4 times more neurons in females than in males [34,72]
> — Zilkha et al. 2021, Sexually Dimorphic Brain Regions and Structures · [4] <!-- quote_key: 233446934_e19240c2 -->

**[1] Mughal et al. 2012 — Introduction (TH-ir hypothalamic dimorphism)**

> The hypothalamus plays a critical role in coordinating expression of reproductive behaviors and physiological responses with environmental cues. Its close anatomical and physiological relationship with the pituitary gland provides an effective means for coordinating diverse homeostatic processes through neuroendocrine regulation of hormone secretion. The hypothalamus contains sexual dimorphic areas which are different in morphology, density, gene expression and neuronal projections. One of the sexually dimorphic neuronal populations in the hypothalamus is tyrosine hydroxylase expressing (TH-ir) neurons whose number is greater in female than in male mice. The role of the sexual dimorphism of these TH-ir neurons is still unknown
> — Mughal et al. 2012, Introduction · [1] <!-- quote_key: 214694216_9c6ba0ce -->

**[2] He et al. 2013 · PMID:25206587 — Sexually Dimorphic Brain Regions and Structures**

> the anteroventral periventricular nucleus of the hypothalamus (AVPV) consists mainly of TH-positive neurons
> — He et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_1dd3b718 -->

**[5] Kauffman et al. 2007 · PMID:17699664 — Neuronal Markers and Molecular Characteristics**

> adult testosterone-treated GPR54 KO males displayed "female-like" numbers of tyrosine hydroxylase-immunoreactive and Kiss1 mRNA-containing neurons in the anteroventral periventricular nucleus and likewise possessed fewer motoneurons in the spino- bulbocavernosus nucleus than did WT males
> — Kauffman et al. 2007, Neuronal Markers and Molecular Characteristics · [5] <!-- quote_key: 17692566_78d7ff15 -->

</details>

---

## 4. Mapping candidates

### 4a. Candidate overview

Two mapping edges are recorded for avpv_th_neuron: a supertype-level edge to
SUPT_0486 and a cluster-level edge to CLUS_1915, the child cluster carrying the
strongest Th+Kiss1 co-expression signal, dopaminergic NT annotation, and the
most extreme female bias (male_female_ratio = 0.02).

| Rank | WMBv1 cluster | Supertype | Cells (MERFISH) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 | n=3–5 ^ | 🟡 MODERATE | Th CONSISTENT; Kiss1 CONSISTENT; nt_type=Dopa; MFR=0.02 CONSISTENT | Best cluster candidate |
| 2 | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] | (self) | n=117 (16 AVPV / 64 PVpo / 37 MPN) | 🟡 MODERATE | Th APPROXIMATE; Kiss1 APPROXIMATE; child CLUS_1915 MFR=0.02 | Best supertype candidate |

2 edges total. Relationship type: PARTIAL_OVERLAP (both edges).

^MERFISH n=3–5; 10x cluster size not yet shown — see ROADMAP.

### 4b. Property alignment — primary candidate (CLUS_1915)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | dopaminergic (A14 group) | GABAergic (Gaba_5 label); Th=2.72 present but diluted | Dopa (confirmed, cluster.yaml name_in_source='Dopa') | SUPT: APPROXIMATE; CLUS: CONSISTENT |
| Soma location | Anteroventral periventricular nucleus [MBA:272] | n=16 cells in MBA:272; also MBA:133 PVpo (n=64), MBA:515 MPN (n=37) | n=1 AVPV (MBA:272), n=1 PVpo (MBA:133), n=3 MBA:1097 Hypothalamus (broad catchall) | APPROXIMATE (both levels) |
| Th expression | POSITIVE (protein, primary defining marker) | precomputed mean_expression=2.72 | precomputed mean_expression=6.6; VMAT2 (Slc18a2) is a DEFINING marker | SUPT: APPROXIMATE; CLUS: CONSISTENT |
| Kiss1 expression | POSITIVE (transcript, co-expressed with Th in AVPV) | precomputed mean_expression=0.62 | precomputed mean_expression=2.51; Kiss1 is a cluster-level DEFINING marker | SUPT: APPROXIMATE; CLUS: CONSISTENT |
| Sex ratio | female-biased (2–4× more TH+ neurons in females) | not available at supertype level | MFR=0.02 (CLUS_1915) — extreme female bias, ~50:1 F:M | CONSISTENT |
| Annotation transfer F1 | not applicable | NOT_ASSESSED | NOT_ASSESSED | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression (CLUS_1915 Th/Kiss1, MFR, nt_type) | Atlas metadata | SUPPORT | Th=6.6, Kiss1=2.51, MFR=0.02, nt_type=Dopa; Slc18a2 DEFINING | atlas-internal |

*(1 of 5 child clusters of SUPT_0486 — CLUS_1915 — shows the female-biased
Th+Kiss1+ profile (Th=6.6, Kiss1=2.51, MFR=0.02, nt_type=Dopa) concordant with
avpv_th_neuron; supertype-level dopaminergic identity and sex ratio are not
resolvable. Best match: CLUS_1915.)*

---

## 5. Candidate paragraphs

## 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] · 🟡 MODERATE

### Supporting evidence

- **Th expression is CONSISTENT at cluster level.** CLUS_1915 shows precomputed mean Th = 6.6 — the highest of any child cluster within SUPT_0486. Slc18a2 (VMAT2, the vesicular monoamine transporter) is also a DEFINING cluster marker, providing independent dopaminergic vesicular-packaging support beyond Th transcript abundance alone.
- **Dopaminergic NT type is confirmed.** cluster.yaml annotates nt_type = Dopa (name_in_source = 'Dopa'), resolving the APPROXIMATE supertype Gaba_5 label and providing CONSISTENT alignment with the classical node's A14 dopaminergic phenotype.
- **Kiss1 co-expression is concordant.** CLUS_1915 Kiss1 = 2.51, with Kiss1 listed as a cluster-level DEFINING marker. This directly matches the classical observation that most AVPV TH+ neurons co-express Kiss1 [3], [5].
- **Sex ratio is strongly concordant.** male_female_ratio = 0.02 (~50:1 female-to-male) is the most extreme female bias in SUPT_0486 and matches the FEMALE_BIASED dimorphism that defines avpv_th_neuron (2–4× more TH+ neurons in females) [1], [4].
- **AVPV cells are explicitly present.** n=1 cell at MBA:272 (AVPV), n=1 at MBA:133 (PVpo); the remainder fall under the broad MBA:1097 (Hypothalamus) catchall.
- **Three convergent independent signals.** Th expression, female sex ratio, and dopaminergic NT type all converge on CLUS_1915 — directly addressing the three principal classical criteria.

### Marker evidence provenance

- **Th** — classical evidence is mixed protein (IHC for TH-immunoreactive neurons) [1], [2], [4] and transcript [3], [5]. Atlas precomputed value at CLUS_1915 (mean = 6.6) is transcript-based (10x Chromium). Direct concordance with the cluster's Slc18a2 (VMAT2) DEFINING-marker annotation provides additional support that this is a bona fide dopaminergic cluster, not a transcriptionally TH+ but functionally non-catecholaminergic population *(note: VMAT2 is required for vesicular packaging of dopamine in catecholaminergic neurons)*.
- **Kiss1** — atlas value at CLUS_1915 (mean = 2.51, DEFINING) is transcript-based and consistent with literature transcript-based ISH detection in AVPV [3], [5]. The cluster-level signal is substantially stronger than the supertype mean (0.62), as expected for a marker concentrated in a specific child cluster rather than diluted across the broader SUPT_0486 population.
- **Slc18a2 (VMAT2)** — listed as a cluster-level DEFINING marker but not present on the classical node. *(note: VMAT2 is consistent with dopaminergic vesicular packaging in AVPV TH neurons but represents a testable additional prediction from atlas data — could be verified by ISH or scRNA-seq re-analysis.)*

### Concerns

- **Very low cell count (n = 3–5 total cells in WMBv1).** All metrics (MFR = 0.02, expression values) are directionally reliable but have limited statistical power. Confidence is capped at MODERATE pending annotation transfer or replication in a larger dataset.
- **MERFISH spatial resolution is insufficient to discriminate AVPV from adjacent PVpo/MPN.** Most CLUS_1915 cells localise to the broad Hypothalamus catchall [MBA:1097] (n=3) rather than to the precise AVPV [MBA:272] (n=1). This does not refute AVPV identity — the cluster is too small to resolve sub-regional anatomy — but prevents location from contributing CONSISTENT evidence at cluster level. *(adjacent region — could reflect registration boundary error or low-cell-count anatomical noise; weak counter-evidence.)*
- **avpv_th_neuron and avpv_kiss1_neuron both map to CLUS_1915.** Because most AVPV Kiss1 cells co-express TH, the two classical types substantially overlap. CLUS_1915 may represent the shared atlas correlate of both populations rather than a distinct transcriptomic split between TH-only and Kiss1-only AVPV neurons.
- **Annotation transfer not yet performed.** No independent, data-driven cell-level mapping of published AVPV TH+ scRNA-seq cells to WMBv1 has been run; this is the most important remaining gap in the evidence base for this edge.

### What would upgrade confidence

- **MapMyCells annotation transfer of AVPV TH-lineage scRNA-seq data** (Th-Cre or Kiss1-Cre sorted preparations) against WMBv1; F1 ≥ 0.80 against CLUS_1915 at cluster level would substantially support upgrading to HIGH confidence and would add `AnnotationTransferEvidence`.
- **Cluster-level co-expression profiling** of CLUS_1915 cells stratified by Kiss1+/Th+ vs Kiss1−/Th+ profiles would address whether avpv_th_neuron and avpv_kiss1_neuron are separable within CLUS_1915 or represent the same atlas population from two classical entry points.

---

## 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] · 🟡 MODERATE

### Supporting evidence

- **TH expression is detected at supertype level.** Precomputed mean Th = 2.72, reflecting the dopaminergic component of AVPV TH neurons, though diluted across a broader supertype.
- **Kiss1 co-expression is detected.** Precomputed mean Kiss1 = 0.62, consistent with subset expression within a heterogeneous supertype spanning multiple preoptic subregions.
- **Direct AVPV location match.** n = 16 cells within SUPT_0486 are labelled to Anteroventral periventricular nucleus [MBA:272], providing a direct anatomical anchor.
- **Esr1 high at supertype level.** Esr1 mean expression = 7.72 at supertype level, consistent with the obligate ERalpha-expressing identity of AVPV reproductive-axis neurons (although Esr1 is not on the classical node for avpv_th_neuron).
- **Child cluster CLUS_1915 concentrates the dopaminergic / female-biased signal.** Child cluster 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] shows Th = 6.6, Kiss1 = 2.51, nt_type = Dopa, and male_female_ratio = 0.02 — the most extreme female bias in SUPT_0486. This cluster-level evidence substantially strengthens the supertype assignment.

### Marker evidence provenance

- **Th** — classical evidence mixes protein (IHC for TH-IR neurons) [1], [2], [4] and transcript [3], [5]. Atlas precomputed Th at supertype (mean = 2.72) is transcript-based (10x Chromium); the moderate value reflects dilution across PVpo/MPN/VMPO cells that do not co-express TH. Cluster-level Th = 6.6 at CLUS_1915 provides much stronger agreement and resolves the supertype-level dilution.
- **Kiss1** — classical evidence is transcript-based (KiSS-1 ISH) [3], [5]. Atlas precomputed value at supertype (mean = 0.62) is also transcript-based. The low supertype mean is expected for a subset marker; cluster-level value (2.51, DEFINING) confirms specificity at CLUS_1915.
- **Atlas annotation/expression check (NT label):** SUPT_0486 carries a Gaba_5 label, but the classical node is dopaminergic. Th = 2.72 is non-zero but the dopaminergic identity is concentrated in CLUS_1915 (nt_type = Dopa). This is a known caveat (NT_PREDICTION_UNCERTAIN) — the supertype label reflects the GABAergic majority rather than the dopaminergic minority.

### Concerns

- **Supertype label (Gaba_5) is not dopaminergic.** SUPT_0486 is annotated as a Gaba_5 supertype while the classical AVPV TH neuron is dopaminergic. The dopaminergic identity is resolved only at cluster level (CLUS_1915, nt_type = Dopa). Mapping to SUPT_0486 as a whole leaves the dopaminergic phenotype only partially captured (APPROXIMATE).
- **Supertype spans a broader preoptic territory than AVPV.** SUPT_0486 covers PVpo [MBA:133] (n=64 cells) and MPN [MBA:515] (n=37 cells) in addition to AVPV [MBA:272] (n=16 cells). The TH+ AVPV population is a minority of the supertype. *(adjacent region — weak counter-evidence at supertype level; the extra cells are within the same broad preoptic/periventricular zone.)*
- **Sex ratio data not available at supertype level.** Female-biased dimorphism (2–4× more TH+ neurons in females) — a defining feature of avpv_th_neuron [1], [4] — cannot be assessed from supertype-level metadata. The signal is visible only in CLUS_1915 (male_female_ratio = 0.02).
- **avpv_th_neuron and avpv_kiss1_neuron both map to SUPT_0486.** These two classical types substantially overlap (most AVPV/PeN Kiss1 cells co-express Th); cluster-level resolution is needed to determine whether they are separable within SUPT_0486.
- **Annotation transfer NOT_ASSESSED.**

### What would upgrade confidence

- The child-cluster inspection has already been carried out and is captured in the CLUS_1915 edge above.
- **MapMyCells annotation transfer of Th-Cre or Kiss1-Cre AVPV scRNA-seq data** to WMBv1; F1 ≥ 0.50 at SUPT_0486 would upgrade this edge; F1 ≥ 0.80 at CLUS_1915 level would support HIGH confidence. Expected output: `AnnotationTransferEvidence`.
- **Targeted cite-traverse for AVPV TH+ scRNA-seq** would provide an independent evidence trail beyond atlas metadata alone and could clarify the avpv_th_neuron / avpv_kiss1_neuron separability question.

---

## 6. Proposed experiments

### 1. MapMyCells annotation transfer of AVPV TH-lineage scRNA-seq data against WMBv1

**What:** Retrieve a published scRNA-seq dataset enriched for AVPV TH+ neurons (e.g., Th-Cre or Kiss1-Cre sorted preparations, or sex-stratified hypothalamic atlases). Run MapMyCells against WMBv1 at cluster resolution.

**Target:** F1 ≥ 0.50 at SUPT_0486 level; F1 ≥ 0.80 at CLUS_1915 level for Th+ cells.

**Expected output:** `AnnotationTransferEvidence` entries on both edges (edge_avpv_th_neuron_to_cs20230722_supt_0486 and edge_avpv_th_neuron_to_cs20230722_clus_1915). Atlas: WMBv1. Tool: MapMyCells. Output format: F1 matrix per cluster, fed back as `AnnotationTransferEvidence` YAML.

**Resolves:** Open questions 1 and 2. Confirms or refutes CLUS_1915 as the correct cluster assignment and addresses the `annotation_transfer_f1` NOT_ASSESSED gap on both edges.

### 2. Cluster-level co-expression profiling to separate avpv_th_neuron and avpv_kiss1_neuron

**What:** Within-cluster re-analysis of CLUS_1915 cells, stratified by Kiss1+/Th+ vs Kiss1−/Th+ profiles; or AT of a Kiss1-Cre-only dataset and a TH-Cre-only dataset against the same target.

**Target:** Detection of two separable sub-populations within CLUS_1915, or formal demonstration that they are co-extensive at this resolution.

**Expected output:** Additional `AnnotationTransferEvidence` and/or `MarkerAnalysisEvidence` records.

**Resolves:** Open question 1 (cluster edge) — whether CLUS_1915 specifically corresponds to the A14 TH/Kiss1 cluster or also includes Kiss1-negative TH+ AVPV neurons.

---

## 7. Open questions

1. Does CLUS_1915 [CS20230722_CLUS_1915] specifically correspond to AVPV A14 TH neurons? Confirmation by cluster-level Kiss1/Th/Esr1 co-expression profiling is needed; does CLUS_1915 also include TH+ AVPV neurons that are Kiss1-negative? *(Appears on the cluster edge.)*
2. Does CLUS_1915 specifically correspond to the AVPV TH neuron population, given that avpv_th_neuron and avpv_kiss1_neuron both map to it and most AVPV Kiss1 cells co-express TH? *(Appears on the supertype edge.)*

---

## 8. Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_avpv_th_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA | SUPPORT — Th=2.72, Kiss1=0.62, Esr1=7.72 at supertype; n=16 AVPV cells; child CLUS_1915 (nt_type=Dopa, MFR=0.02) noted as cluster-level support |
| edge_avpv_th_neuron_to_cs20230722_clus_1915 | ATLAS_METADATA | SUPPORT — Th=6.6 (highest in SUPT_0486), Kiss1=2.51 (DEFINING), nt_type=Dopa confirmed, MFR=0.02 (extreme female bias), Slc18a2 (VMAT2) DEFINING |

---

## 9. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Mughal et al. 2012 | — | Soma location; sexually dimorphic TH-ir neuron population in hypothalamus |
| [2] | He et al. 2013 | [PMID:25206587](https://pubmed.ncbi.nlm.nih.gov/25206587/) | Soma location (AVPV consists mainly of TH-positive neurons) |
| [3] | Stephens et al. 2017 | [PMID:28660243](https://pubmed.ncbi.nlm.nih.gov/28660243/) | Soma location, NT type (dopaminergic), Th/Kiss1 co-expression, sex dimorphism |
| [4] | Zilkha et al. 2021 | [PMID:33910083](https://pubmed.ncbi.nlm.nih.gov/33910083/) | Th marker; AVPV TH+ population 3–4× more neurons in females |
| [5] | Kauffman et al. 2007 | [PMID:17699664](https://pubmed.ncbi.nlm.nih.gov/17699664/) | Kiss1 marker; TH-IR and Kiss1 mRNA co-labelling in AVPV |
