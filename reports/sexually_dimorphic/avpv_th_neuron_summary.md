# AVPV tyrosine hydroxylase (TH) neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

The AVPV tyrosine hydroxylase (TH) neuron is a classically defined, sexually dimorphic hypothalamic population in the Anteroventral periventricular nucleus [MBA:272]. It is dopaminergic (A14 group) and shows a pronounced female bias in cell number — approximately 3–4× more TH-immunoreactive neurons in females than in males [4]. Most AVPV/PeN Kiss1 cells co-express TH [3], so the AVPV TH population substantially overlaps the AVPV Kiss1 population at the level of individual cells; anchoring this classical type onto the WMBv1 transcriptomic taxonomy is needed to identify a molecular correlate and to resolve whether the TH-defined and Kiss1-defined entry points map to one or to separable atlas clusters.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Anteroventral periventricular nucleus [MBA:272] | [1], [2], [3] |
| NT type | dopaminergic | [3] |
| Defining markers | Th; Kiss1 | [1], [4], [2], [3], [5] |
| Sex bias | Female-biased (2–4× more TH+ neurons in females) | [1], [2], [4] |
| CL term | — (candidate for a new CL term) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location (AVPV) / sexually dimorphic TH population:** literature · rodent · [1]
  > The hypothalamus plays a critical role in coordinating expression of reproductive behaviors and physiological responses with environmental cues. Its close anatomical and physiological relationship with the pituitary gland provides an effective means for coordinating diverse homeostatic processes through neuroendocrine regulation of hormone secretion. The hypothalamus contains sexual dimorphic areas which are different in morphology, density, gene expression and neuronal projections. One of the sexually dimorphic neuronal populations in the hypothalamus is tyrosine hydroxylase expressing (TH-ir) neurons whose number is greater in female than in male mice. The role of the sexual dimorphism of these TH-ir neurons is still unknown
  > — Abrahão et al. 2012, Introduction · [1] <!-- quote_key: 214694216_9c6ba0ce -->

- **Soma location (AVPV mainly TH+):** literature · rodent · [2]
  > the anteroventral periventricular nucleus of the hypothalamus (AVPV) consists mainly of TH-positive neurons
  > — He et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_1dd3b718 -->

- **NT type (dopaminergic) and Kiss1/TH co-expression:** literature · mouse · [3]
  > Kiss1-syntheizing neurons reside primarily in the hypothalamic anteroventral periventricular (AVPV/PeN) and arcuate (ARC) nuclei. AVPV/PeN Kiss1 neurons are sexually dimorphic, with females expressing more Kiss1 than males, and participate in estradiol (E2)- induced positive feedback control of GnRH secretion. In mice, most AVPV/PeN Kiss1 cells coexpress tyrosine hydroxylase (TH), the rate-limiting enzyme in catecholamine synthesis (in this case, dopamine).
  > — Stephens et al. 2017, Neuronal Markers and Molecular Characteristics · [3] <!-- quote_key: 4702847_ebd225e6 -->

- **Th marker / female bias (3–4× more TH neurons in females):** literature · mouse · [4]
  > A notable exception is the AVPV of the hypothalamus, which is larger in volume, contains more cells, and sends more projections to multiple reproduction-related brain regions in females compared to males [25,34,71,72,76e[79]. Importantly, it also expresses several sexually dimorphic molecularly defined neuronal populations, including the tyrosine hydroxylase (TH)-expressing population, which contains 3e4 times more neurons in females than in males [34,72]
  > — Zilkha et al. 2021, Sexually Dimorphic Brain Regions and Structures · [4] <!-- quote_key: 233446934_e19240c2 -->

- **Kiss1 marker / sex-reversal of TH and Kiss1 in GPR54 KO:** literature · mouse · [5]
  > adult testosterone-treated GPR54 KO males displayed "female-like" numbers of tyrosine hydroxylase-immunoreactive and Kiss1 mRNA-containing neurons in the anteroventral periventricular nucleus and likewise possessed fewer motoneurons in the spino- bulbocavernosus nucleus than did WT males
  > — Kauffman et al. 2007, Neuronal Markers and Molecular Characteristics · [5] <!-- quote_key: 17692566_78d7ff15 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term. The classical node notes a proposed sibling of CL:4072009 ("A12 dopaminergic neuron") for AVPV/RP3V A14 dopaminergic neurons.

---

## Results

Two candidate atlas entries were assessed at supertype and cluster resolution; CLUS_1915 within SUPT_0486 is the primary mapping at MODERATE confidence, with three convergent atlas signals (Th expression, AVPV location, and an extreme female sex ratio at the child-cluster level) all consistent with the classical definition.

### Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 | 5 | 🟡 MODERATE | Th/Kiss1 CONSISTENT · sex_ratio CONSISTENT | Best candidate (cluster) |
| 2 | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] | — | 178 | 🟡 MODERATE | Th APPROXIMATE · sex_ratio CONSISTENT (via child) | Best candidate (supertype) |

Total: 2 edges, both PARTIAL_OVERLAP relationships.

### 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] · 🟡 MODERATE

**Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | dopaminergic (A14 group) | GABAergic (Gaba_5 label) | Dopa (confirmed, cluster.yaml name_in_source='Dopa') | CONSISTENT |
| Soma location | Anteroventral periventricular nucleus [MBA:272] | MBA:272 (AVPV) n=16; MBA:133 PVpo n=64; MBA:515 MPN n=37 | MBA:272 (AVPV) n=1; MBA:133 PVpo n=1; MBA:1097 Hypothalamus n=3 | APPROXIMATE |
| Th expression | POSITIVE (protein, primary defining marker) | mean_expression=2.72 | mean_expression=6.6; VMAT2 (Slc18a2) is a DEFINING marker | CONSISTENT |
| Kiss1 expression | POSITIVE (transcript, co-expressed with Th) | mean_expression=0.62 | mean_expression=2.51; Kiss1 is a cluster-level DEFINING marker | CONSISTENT |
| Sex ratio | Female-biased (2–4× more TH+ neurons in females) | not available | MFR=0.02 (CS20230722_CLUS_1915; extreme female bias, ~50:1 F:M) | CONSISTENT |
| Annotation transfer F1 | not applicable | NOT_ASSESSED | NOT_ASSESSED | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression (CLUS_1915) | Atlas metadata | SUPPORT | Th=6.6, Kiss1=2.51, MFR=0.02; VMAT2 DEFINING | atlas-internal |

*(1 of 5 child clusters of SUPT_0486 (CLUS_1915) shows the female-biased dopaminergic Th+/Kiss1+ profile concordant with the classical AVPV TH neuron; the remaining 4 child clusters are sex-neutral or male-biased and either lack Kiss1 expression or are not assigned a Dopa NT type. Best match: CLUS_1915.)*

**Supporting evidence**

- Atlas metadata for CLUS_1915 records Th mean expression = 6.6 — the highest of any child cluster within SUPT_0486 — together with Kiss1 = 2.51 (above background for the supertype) and an explicit `name_in_source='Dopa'` neurotransmitter assignment at cluster level. Kiss1 and Slc18a2 (VMAT2, the vesicular monoamine transporter) are cluster-level DEFINING markers per WMBv1 metadata, providing an independent line of dopaminergic identity support beyond Th alone.
- Sex ratio: CLUS_1915 has `male_female_ratio = 0.02` (approximately 50:1 female:male), the most extreme female bias of any child cluster in SUPT_0486 — directly concordant with the classical 2–4× female bias in AVPV TH-immunoreactive cell number reported in [1], [2], [4].
- MBA:272 (AVPV) cells are explicitly present in CLUS_1915's MERFISH location distribution (n=1 cell), with the remaining cells located in adjacent periventricular/preoptic zones (MBA:133 PVpo, MBA:1097 Hypothalamus catchall).

**Marker evidence provenance**

- **Th (defining marker):** literature evidence is protein-level (tyrosine hydroxylase immunoreactivity in [1], [2], [4]) and transcript-level via [5] (Kiss1 mRNA / TH-ir co-counts in GPR54 KO). Atlas CLUS_1915 records Th mean expression = 6.6 — the highest of any SUPT_0486 child cluster — confirming the literature TH co-expression claim at transcript level. VMAT2/Slc18a2 is independently flagged as a cluster-level DEFINING marker, reinforcing the dopaminergic identity.
- **Kiss1 (defining marker, co-expressed):** literature evidence is transcript-level in [3] and mRNA-positive cell counts in [5]; atlas CLUS_1915 records Kiss1 mean expression = 2.51 and Kiss1 is a cluster-level DEFINING marker. Concordant across protein/transcript literature and atlas annotation.
- No atlas-annotation/expression discrepancies were flagged at cluster level — both defining markers show concordant high expression on CLUS_1915.

**Concerns**

- LOW_CELL_COUNT: CLUS_1915 contains only n=3–5 total cells in WMBv1. The MFR=0.02 and expression peaks are directionally consistent but underpowered statistically; this is the principal reason confidence is capped at MODERATE rather than HIGH.
- Soma location APPROXIMATE: only n=1 cell is annotated to MBA:272 (AVPV) at this cluster, with the remainder spread across adjacent PVpo and the broad Hypothalamus catchall. MERFISH spatial resolution is insufficient to resolve AVPV vs adjacent PVpo at this cell count *(adjacent region — could reflect registration boundary error; weak counter-evidence)*.
- AMBIGUOUS_MAPPING: avpv_th_neuron and avpv_kiss1_neuron both map to CLUS_1915 — the two classical types substantially overlap (most AVPV Kiss1 cells co-express Th in the classical literature [3], [5]). These may be the same underlying cell population described from different neurochemical entry points.
- Annotation transfer NOT_ASSESSED.

**What would upgrade confidence**

- Run MapMyCells annotation transfer of Th-Cre or Kiss1-Cre AVPV scRNA-seq data against WMBv1; target F1 ≥ 0.80 at CLUSTER level to resolve LOW_CELL_COUNT and emit an AnnotationTransferEvidence record on this edge.
- Cluster-level Kiss1/Th/Esr1 co-expression profiling on CLUS_1915 cells to confirm whether they correspond specifically to A14 TH/Kiss1 neurons or also include Kiss1-negative TH+ AVPV neurons (open question 1).

### 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] · 🟡 MODERATE

**Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | dopaminergic (A14 group) | GABAergic (Gaba_5 label) | CLUS_1915 nt_type=Dopa | APPROXIMATE |
| Soma location | Anteroventral periventricular nucleus [MBA:272] | MBA:272 (AVPV) n=16; MBA:133 PVpo n=64; MBA:515 MPN n=37 | not assessed at this row | APPROXIMATE |
| Th expression | POSITIVE (protein, primary defining marker) | mean_expression=2.72 | not assessed | APPROXIMATE |
| Kiss1 expression | POSITIVE (transcript, co-expressed) | mean_expression=0.62 | not assessed | APPROXIMATE |
| Sex ratio | Female-biased (2–4× more TH+ neurons in females) | not available | child CLUS_1915 MFR=0.02 | CONSISTENT |
| Annotation transfer F1 | not applicable | NOT_ASSESSED | NOT_ASSESSED | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression (SUPT_0486) | Atlas metadata | SUPPORT | Th=2.72; Esr1=7.72; Kiss1=0.62; AVPV n=16 | atlas-internal |

*(Heterogeneity caveat: SUPT_0486 spans PVpo-VMPO-MPN and contains 5 child clusters; only CLUS_1915 carries the Dopa NT assignment, peak Th/Kiss1 expression, and extreme female bias. The other 4 child clusters are sex-neutral or male-biased. Best match within supertype: CLUS_1915.)*

**Supporting evidence**

- SUPT_0486 is the top-ranked rank-1 candidate for avpv_th_neuron; n=16 of its 178 cells are annotated to MBA:272 (AVPV), providing direct AVPV anatomical overlap. Th mean expression at supertype level is 2.72 — detectable but diluted relative to CLUS_1915 (6.6), consistent with the AVPV TH/Kiss1 subset being one of several preoptic populations grouped into this supertype.
- The female-biased sex signal that defines the classical type is resolved at the child cluster CLUS_1915 (MFR=0.02), confirming that SUPT_0486 contains the AVPV TH population even though sex ratio is not separately reported at supertype level.

**Concerns**

- NT_PREDICTION_UNCERTAIN: SUPT_0486 carries a Gaba_5 label at supertype level while the classical AVPV TH neuron is dopaminergic. Dopaminergic identity is resolved only at cluster level (CLUS_1915, Dopa designation) — supertype-level NT annotation reflects the majority of its 178 cells, not the AVPV TH subset.
- AMBIGUOUS_MAPPING: avpv_th_neuron and avpv_kiss1_neuron both map to SUPT_0486, and these two classical types substantially overlap (most AVPV/PeN Kiss1 cells co-express Th); cluster-level resolution is needed to determine whether they are separable within SUPT_0486.
- Soma location APPROXIMATE: supertype spans the broader preoptic zone (PVpo, MPN, VMPO) beyond the AVPV proper *(adjacent region — could reflect registration boundary error; weak counter-evidence)*.
- Th and Kiss1 APPROXIMATE at supertype mean — consistent with subset expression diluted across heterogeneous child clusters; cluster-level resolution restores concordance at CLUS_1915.
- TAXONOMY_LEVEL_MISMATCH: the defining female-biased sex ratio is only resolvable at child cluster (CLUS_1915), not at supertype level.

**What would upgrade confidence**

- Prefer the cluster-level edge (CLUS_1915) for downstream reasoning; supertype edge is retained for taxonomic context.
- MapMyCells annotation transfer at SUBCLASS / SUPERTYPE level on a published AVPV Th-Cre scRNA-seq dataset would emit an AnnotationTransferEvidence record on this edge.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** AVPV tyrosine hydroxylase (TH) neuron is defined as a dopaminergic (A14) neuron with Th as the primary defining marker and Kiss1 as a co-expressed defining marker, soma-localised to the Anteroventral periventricular nucleus [MBA:272], with a 2–4× female-biased anatomical dimorphism; literature support from [1], [2], [3], [4], [5]. The classical type is CLASSICAL_NEUROCHEMICAL by `definition_basis` — it predates transcriptomic taxonomies and is anchored on neurochemical and anatomical evidence in rodents.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:17+00:00 from [kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_avpv_th_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA | SUPPORT | atlas-internal |
| edge_avpv_th_neuron_to_cs20230722_clus_1915 | ATLAS_METADATA | SUPPORT | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** AVPV tyrosine hydroxylase (TH) neuron → 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] at MODERATE confidence. Key support: ATLAS_METADATA — Th=6.6 (highest in SUPT_0486 lineage), Kiss1=2.51 cluster-DEFINING, `name_in_source='Dopa'` NT assignment, and MFR=0.02 extreme female bias at the child cluster all converge on a single cluster matching the classical neurochemical and anatomical definition. Key caveats: LOW_CELL_COUNT (n=3–5 cells in WMBv1) and AMBIGUOUS_MAPPING with the overlapping avpv_kiss1_neuron classical type, which maps to the same cluster.

No Cell Ontology term currently assigned. The classical node notes that no exact CL term covers AVPV A14 dopaminergic neurons — a candidate for a new CL term as a sibling of CL:4072009 ("A12 dopaminergic neuron").

### Proposed experiments and follow-ups

**Annotation transfer of published AVPV TH/Kiss1 scRNA-seq data to WMBv1.**
- What: MapMyCells annotation transfer using a published Th-Cre or Kiss1-Cre AVPV scRNA-seq dataset against WMBv1.
- Target: F1 ≥ 0.80 at CLUSTER level against CLUS_1915.
- Expected output: AnnotationTransferEvidence on both `edge_avpv_th_neuron_to_cs20230722_clus_1915` and the parent supertype edge.
- Resolves: open question 1 (whether CLUS_1915 corresponds specifically to A14 TH/Kiss1 neurons or also captures TH+ Kiss1-negative AVPV cells); upgrades cluster-level confidence beyond LOW_CELL_COUNT.

**Joint cluster-level separability assessment with avpv_kiss1_neuron.**
- What: Cluster-level Kiss1/Th co-expression profiling on CLUS_1915 cells (or higher-resolution scRNA-seq) to determine whether avpv_th_neuron and avpv_kiss1_neuron are separable populations within the same cluster or represent the same underlying cells described from different neurochemical entry points.
- Expected output: either a refined sub-cluster mapping that distinguishes Th-only, Kiss1-only, and Th+Kiss1+ subsets within CLUS_1915, or confirmation that the two classical types collapse to a single transcriptomic identity.
- Resolves: AMBIGUOUS_MAPPING caveat on both edges.

### Open questions

1. Does CLUS_1915 specifically correspond to AVPV A14 TH neurons, or does it also include TH+ AVPV neurons that are Kiss1-negative?
2. Are avpv_th_neuron and avpv_kiss1_neuron separable populations within CLUS_1915, or does CLUS_1915 represent the joint AVPV Th/Kiss1 co-expressing population described in [3]?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Abrahão et al. 2012 | — (DOI:10.1007/s12031-012-9923-1) | soma location, sexually dimorphic TH population |
| [2] | He et al. 2013 | [25206587](https://pubmed.ncbi.nlm.nih.gov/25206587) | soma location (AVPV mainly TH+) |
| [3] | Stephens et al. 2017 | [28660243](https://pubmed.ncbi.nlm.nih.gov/28660243) | NT type, Th/Kiss1 co-expression |
| [4] | Zilkha et al. 2021 | [33910083](https://pubmed.ncbi.nlm.nih.gov/33910083) | Th marker, 3–4× female bias |
| [5] | Kauffman et al. 2007 | [17699664](https://pubmed.ncbi.nlm.nih.gov/17699664) | Kiss1 marker, sex-reversal in GPR54 KO |
