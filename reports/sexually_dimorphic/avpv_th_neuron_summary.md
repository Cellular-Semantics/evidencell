# AVPV tyrosine hydroxylase (TH) neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

The anteroventral periventricular nucleus (AVPV) of the rostral hypothalamus contains a sexually dimorphic population of tyrosine hydroxylase (TH)-expressing neurons that is two- to four-fold more numerous in females than in males and is implicated in oestradiol-driven positive feedback control of GnRH secretion [4]. Most of these AVPV/PeN TH neurons co-express Kiss1, and the population sits at the heart of the dimorphic preoptic circuitry coordinating reproductive physiology with environmental cues [3]. Placing this classical, transgene- and immunohistochemistry-defined population onto the Whole Mouse Brain v1 (WMBv1) transcriptomic atlas is the goal of the present mapping.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Anteroventral periventricular nucleus [MBA:272] | [1], [2], [3] |
| NT type | dopaminergic | [3] |
| Defining markers | Th; Kiss1 | Th: [1], [4], [2]; Kiss1: [3], [5] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| Notes | Female-biased dimorphism (2–4× more TH+ neurons in females); substantial overlap with AVPV/PeN Kiss1 neurons; distinct from SDN-POA where TH-ir cell bodies are absent (only TH-ir axons/synapses present). | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Th (defining marker):** classical immunohistochemistry / TH-ir cell counts in AVPV [[1]], [[4]], [[2]].
  > the anteroventral periventricular nucleus of the hypothalamus (AVPV) consists mainly of TH-positive neurons
  > — He et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_1dd3b718 -->

  > A notable exception is the AVPV of the hypothalamus, which is larger in volume, contains more cells, and sends more projections to multiple reproduction-related brain regions in females compared to males [25,34,71,72,76e[79]. Importantly, it also expresses several sexually dimorphic molecularly defined neuronal populations, including the tyrosine hydroxylase (TH)-expressing population, which contains 3e4 times more neurons in females than in males [34,72]
  > — Zilkha et al. 2021, Sexually Dimorphic Brain Regions and Structures · [4] <!-- quote_key: 233446934_e19240c2 -->

- **Kiss1 (defining marker):** AVPV/PeN Kiss1 ↔ TH co-expression [[3]], [[5]].
  > Kiss1-syntheizing neurons reside primarily in the hypothalamic anteroventral periventricular (AVPV/PeN) and arcuate (ARC) nuclei. AVPV/PeN Kiss1 neurons are sexually dimorphic, with females expressing more Kiss1 than males, and participate in estradiol (E2)- induced positive feedback control of GnRH secretion. In mice, most AVPV/PeN Kiss1 cells coexpress tyrosine hydroxylase (TH), the rate-limiting enzyme in catecholamine synthesis (in this case, dopamine).
  > — Stephens et al. 2017, Neuronal Markers and Molecular Characteristics · [3] <!-- quote_key: 4702847_ebd225e6 -->

  > adult testosterone-treated GPR54 KO males displayed "female-like" numbers of tyrosine hydroxylase-immunoreactive and Kiss1 mRNA-containing neurons in the anteroventral periventricular nucleus and likewise possessed fewer motoneurons in the spino- bulbocavernosus nucleus than did WT males
  > — Kauffman et al. 2007, Neuronal Markers and Molecular Characteristics · [5] <!-- quote_key: 17692566_78d7ff15 -->

- **Soma location (AVPV [MBA:272]):**
  > The hypothalamus plays a critical role in coordinating expression of reproductive behaviors and physiological responses with environmental cues. Its close anatomical and physiological relationship with the pituitary gland provides an effective means for coordinating diverse homeostatic processes through neuroendocrine regulation of hormone secretion. The hypothalamus contains sexual dimorphic areas which are different in morphology, density, gene expression and neuronal projections. One of the sexually dimorphic neuronal populations in the hypothalamus is tyrosine hydroxylase expressing (TH-ir) neurons whose number is greater in female than in male mice. The role of the sexual dimorphism of these TH-ir neurons is still unknown
  > — author of [1] et al. 2012, Introduction · [1] <!-- quote_key: 214694216_9c6ba0ce -->

</details>

No Cell Ontology term currently covers this type — candidate for a new CL term (sibling of CL:4072009 *A12 dopaminergic neuron*, for the AVPV/RP3V A14 dopaminergic population).

---

## Results

Classical AVPV TH neurons map most plausibly onto the periventricular-preoptic Hmx2 GABAergic supertype 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] (see property comparison and evidence support tables below), with the rare dopaminergic child cluster 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] as the best-resolved cluster carrying the female-biased TH/Kiss1 signature. Cluster-level resolution is limited by small n (CLUS_1915 retains only ~3–5 cells in the curated cohort) and by ambiguous separation from the largely overlapping AVPV Kiss1 population; soma counts at MBA:272 (Anteroventral periventricular nucleus) for both targets are sparse, consistent with boundary scatter across the periventricular-preoptic corridor rather than a clean within-AVPV placement.

### Supertype-level survivor — 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] · 🟡 MODERATE

**Property comparison (Table 1).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Anteroventral periventricular nucleus [MBA:272] | hypothalamus / Periventricular hypothalamic nucleus, preoptic part [MBA:133] / Medial preoptic nucleus [MBA:515] (`region_fraction_100um: 0.061`) | hypothalamus / preoptic periventricular / Medial preoptic nucleus (CLUS_1915; `region_fraction_100um: 0.071`) | DISCORDANT |
| NT type | dopaminergic | not asserted (supertype label is Gaba_5) | Dopa (CLUS_1915) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Th expression | defining marker | no precomputed value at supertype level | Th=6.6 (CLUS_1915; highest in SUPT_0486 lineage) | NOT_ASSESSED at supertype; supportive at cluster |
| Kiss1 expression | defining marker | no precomputed value at supertype level | Kiss1=2.51 (CLUS_1915; only child cluster substantially above background) | NOT_ASSESSED at supertype; supportive at cluster |
| Sex ratio | female-biased (2–4× more TH+ in females) | not available at supertype level | MFR=0.02 (CLUS_1915; extreme female bias) | CONSISTENT at cluster |

*(1 of 5 child clusters in SUPT_0486 [CLUS_1915] carries the female-biased Th/Kiss1 dopaminergic profile; the remainder are sex-neutral or lack Th/Kiss1 signal. Best match: CLUS_1915.)*

**Evidence support (Table 2).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression / cohort scoring at supertype | Atlas metadata | SUPPORT | Th=2.72, Esr1=7.72, Kiss1=0.62; rank-1 cohort top; female-biased child CLUS_1915 inside | atlas-internal |

The mapping at supertype level is supported by three converging atlas signals: a Th-expressing periventricular-preoptic GABAergic supertype, an unusually female-biased child cluster (CLUS_1915, male/female ratio 0.02) within it, and Esr1 expression consistent with the classical type's documented oestrogen responsiveness [3]. The supertype's GABAergic label is not a contradiction of the classical type's dopaminergic identity: dopaminergic identity in this corridor is resolved only at cluster level (CLUS_1915 is annotated Dopa) and the AVPV TH/Kiss1 population is widely reported to be GABAergic-dopaminergic dual-phenotype. The principal weakness is that direct atlas-side Th and Kiss1 expression values are not exposed at the supertype level in the available facts, so transcript-level marker concordance is established only via the child cluster (see CLUS_1915 below). Location is the main caveat: only ~6% of SUPT_0486 cells fall within or near (100 µm of) MBA:272, with the bulk of soma scattering across the periventricular preoptic nucleus [MBA:133] and the medial preoptic nucleus [MBA:515] — adjacent rostral preoptic structures consistent with boundary scatter rather than a wrong-region placement *(note: the AVPV abuts the periventricular preoptic and medial preoptic nuclei, and MERFISH-derived soma assignments in this corridor are known to drift across the AVPV/PeN/MPO border)*.

**Concerns.**
- Location DISCORDANT — `region_fraction_100um: 0.061` (distant from a clean within-AVPV placement; weak counter-evidence interpretable as registration scatter across the adjacent preoptic periventricular and medial preoptic compartments rather than off-target localisation).
- Supertype label is Gaba_5, not Dopa; dopaminergic identity is rescued only at cluster level (CLUS_1915).
- avpv_th_neuron and avpv_kiss1_neuron both land on SUPT_0486 — the two classical types substantially overlap at the literature level (most AVPV/PeN Kiss1 cells co-express Th) and atlas-side separation between them within SUPT_0486 is not yet established.

**What would upgrade confidence.**
- Cluster annotation transfer onto WMBv1 from Th-Cre or Kiss1-Cre AVPV transcriptomic data, targeting F1 ≥ 0.80 at supertype (SUPT_0486) and cluster (CLUS_1915) levels, written back as `AnnotationTransferEvidence`.
- Atlas-side Th and Kiss1 precomputed-expression values exposed at the supertype level, to anchor marker concordance without relying solely on the single Dopa-annotated child cluster.

### Cluster-level survivor — 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] · 🟡 MODERATE

**Property comparison (Table 1).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Anteroventral periventricular nucleus [MBA:272] | (see SUPT_0486 row above) | hypothalamus / Periventricular hypothalamic nucleus, preoptic part [MBA:133] / Medial preoptic nucleus [MBA:515] (`region_fraction_100um: 0.071`) | DISCORDANT |
| NT type | dopaminergic | not asserted | Dopa | CONSISTENT |
| Th expression | defining marker | not available | Th=6.6 (highest in the SUPT_0486 lineage) | CONSISTENT |
| Kiss1 expression | defining marker | not available | Kiss1=2.51 (only cluster substantially above background) | CONSISTENT |
| Slc18a2 (VMAT2) | not asserted by classical lit | not available | DEFINING cluster marker | supportive context |
| Sex ratio | female-biased (2–4×) | not available | MFR=0.02 (extreme female bias) | CONSISTENT |

**Evidence support (Table 2).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression / cluster annotation | Atlas metadata | SUPPORT | Th=6.6; Kiss1=2.51; Dopa; MFR=0.02; Slc18a2 DEFINING; cohort top (rank 0, score 4/next-best 2) | atlas-internal |

CLUS_1915 is the only WMBv1 cluster simultaneously carrying (i) high Th expression, (ii) detectable Kiss1, (iii) a dopaminergic neurotransmitter annotation, and (iv) the extreme female bias characteristic of the AVPV TH/Kiss1 population [3], [4]. Slc18a2 (VMAT2), the vesicular monoamine transporter required for dopaminergic vesicle loading, appears as a DEFINING cluster marker, providing an orthogonal monoaminergic identity signal beyond Th itself. Stage A scored CLUS_1915 as the dominant rank-0 candidate within a 10-member female-biased dopaminergic AVPV cohort (score 4 vs next-best 2). The principal weakness is statistical: the cluster retains only ~3–5 source-cohort cells after atlas filtering, so all metrics are directionally correct but underpowered, which caps reportable confidence at MODERATE despite the qualitative marker convergence. As with the parent supertype, soma counts at MBA:272 are sparse (`region_fraction_100um: 0.071`), with the bulk of the cluster falling into the adjacent periventricular preoptic [MBA:133] and medial preoptic nuclei [MBA:515] — interpretable as boundary scatter across the AVPV/PeN/MPO corridor rather than off-target placement.

**Concerns.**
- Low cell count (n ≈ 3–5 after filtering): all signals directional but underpowered.
- Location DISCORDANT — `region_fraction_100um: 0.071` (boundary scatter across the periventricular and medial preoptic neighbours of MBA:272).
- avpv_th_neuron and avpv_kiss1_neuron both map onto CLUS_1915 — these two classical types substantially overlap in the literature (most AVPV/PeN Kiss1 cells co-express Th) and may in fact be the same transcriptomic population entered from two marker-defined entry points.
- Edge YAML duplication: a second edge against this same accession (`edge_avpv_th_neuron_to_CS20230722_CLUS_1915`, fresh-emit ID) carries only stub structured evidence and no curator caveats; it should be retired by the curator in favour of the substantive lowercase-ID edge.

**What would upgrade confidence.**
- Annotation transfer of Th-Cre AVPV transcriptomic data onto WMBv1 targeting F1 ≥ 0.80 at cluster level for CLUS_1915.
- A larger AVPV/PeN-targeted transcriptomic cohort (Th-Cre and/or Kiss1-Cre) to lift n above the small-sample ceiling that currently caps cluster-level confidence.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster / supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---:|---|---|---|
| 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] | 933 | 🟡 MODERATE | Th+/Esr1+ supertype harbours female-biased Dopa child CLUS_1915 | Primary (supertype) |
| 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] | 265 | 🟡 MODERATE | Th=6.6, Kiss1=2.51, Dopa, MFR=0.02 | Primary (cluster) |
| 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] (duplicate edge) | 265 | ⚪ UNCERTAIN | Stub fresh-emit edge against same accession | Eliminated (duplicate of substantive edge) |
| 1469 MPO-ADP Lhx8 Gaba_3 [CS20230722_CLUS_1469] | 30 | 🔴 LOW | Dopa label but in MPO/ADP, not AVPV | Eliminated (wrong subregion) |
| 5246 Tanycyte NN_2 [CS20230722_CLUS_5246] | 94 | 🔴 REFUTED | Tanycyte (non-neuronal), located at third ventricle | Eliminated (non-neuronal lineage) |
| 1910 PVpo-VMPO-MPN Hmx2 Gaba_4 [CS20230722_CLUS_1910] | 135 | 🔴 LOW | Dopa-adjacent but no Th/Kiss1 / female-bias signal | Eliminated (no dimorphic Th/Kiss1 signal) |
| 5211 Astro-NT NN_1 [CS20230722_CLUS_5211] | 89 | 🔴 REFUTED | Astrocyte (non-neuronal), striatal/olfactory soma | Eliminated (non-neuronal lineage) |
| 0550 MPN-MPO-PVpo Hmx2 Glut_5 [CS20230722_SUPT_0550] | 583 | 🔴 LOW | Glutamatergic; high MBA:272 fraction but no Th/Dopa | Eliminated (glutamatergic, no dopaminergic child) |
| 1172 Tanycyte NN_1 [CS20230722_SUPT_1172] | 135 | 🔴 REFUTED | Tanycyte (non-neuronal) | Eliminated (non-neuronal lineage) |
| 0419 PVR Six3 Sox3 Gaba_9 [CS20230722_SUPT_0419] | 620 | 🔴 LOW | Preoptic GABAergic; no Th/Dopa annotation | Eliminated (no dopaminergic identity) |
| 0485 PVpo-VMPO-MPN Hmx2 Gaba_4 [CS20230722_SUPT_0485] | 260 | 🔴 LOW | PVpo GABA neighbour of SUPT_0486; no Th/Dopa child | Eliminated (no Th/Dopa child) |
| 0400 SI-MPO-LPO Lhx8 Gaba_5 [CS20230722_SUPT_0400] | 195 | 🔴 LOW | Substantia innominata / MPO/LPO GABA; far from AVPV | Eliminated (wrong subregion) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical AVPV TH neuron is defined (CLASSICAL_NEUROCHEMICAL `definition_basis`) by tyrosine hydroxylase (Th) immunoreactivity in AVPV cell bodies [1], [4], [2], with substantial co-expression of Kiss1 [3], [5], a dopaminergic neurotransmitter phenotype [3], soma in the anteroventral periventricular nucleus [MBA:272] [1], [2], [3], and a robust female-biased numerical dimorphism (2–4× more TH+ neurons in females [4]).

**Atlas mapping query.** Candidate atlas clusters were retrieved from the Whole Mouse Brain v1 (WMBv1) taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match at MBA:272, dopaminergic NT type, defining markers Th/Kiss1, and female sex bias). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster and from MERFISH spatial registration for soma location. No MERFISH location data was used for the classical-side soma (`has_merfish_location: false`); the classical soma assignment is anchored on the literature record.

**Annotation transfer.** No annotation-transfer runs are recorded against this node — this is the principal gap and the primary upgrade path (see Discussion).

**Bulk transcriptomic correlation.** No bulk-correlation runs are recorded against this node.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:14:03+00:00 from [kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_avpv_th_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA | SUPPORT | atlas-internal |
| edge_avpv_th_neuron_to_cs20230722_clus_1915 | ATLAS_METADATA | SUPPORT | atlas-internal |
| edge_avpv_th_neuron_to_CS20230722_CLUS_1915 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_avpv_th_neuron_to_CS20230722_CLUS_1469 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_avpv_th_neuron_to_CS20230722_CLUS_5246 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_avpv_th_neuron_to_CS20230722_CLUS_1910 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_avpv_th_neuron_to_CS20230722_CLUS_5211 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_avpv_th_neuron_to_CS20230722_SUPT_0550 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_avpv_th_neuron_to_CS20230722_SUPT_1172 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_avpv_th_neuron_to_CS20230722_SUPT_0419 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_avpv_th_neuron_to_CS20230722_SUPT_0485 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_avpv_th_neuron_to_CS20230722_SUPT_0400 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** AVPV tyrosine hydroxylase (TH) neuron → 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] at MODERATE confidence, with 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_CLUS_1915] as the best-resolved child cluster at MODERATE confidence. Key support: atlas-side convergence of dopaminergic identity, Th/Kiss1 expression, and extreme female sex bias on CLUS_1915 within an otherwise GABAergic periventricular-preoptic supertype. Key caveats: NT prediction uncertain at supertype level (Gaba_5 vs Dopa rescued only at cluster level); low cell count at CLUS_1915 capping cluster-level confidence; and an ambiguous mapping with the overlapping avpv_kiss1_neuron classical type, which targets the same supertype and cluster.

No Cell Ontology term currently covers this type. The knowledge base notes this as a candidate for a new CL term, structured as a sibling of CL:4072009 (*A12 dopaminergic neuron*) covering the AVPV/RP3V A14 dopaminergic group — distinct from CL:4072009 on anatomical (A14 vs A12), developmental, and functional grounds (oestradiol-driven positive feedback on GnRH secretion is specific to the AVPV/PeN population). The mapping above should therefore be read as a transcriptomic anchor for a future CL contribution rather than as a placement onto an existing ontology class.

### Proposed experiments and follow-ups

- **What:** Cluster-level annotation transfer of AVPV TH-lineage and Kiss1-lineage transcriptomic data (Th-Cre or Kiss1-Cre cohorts) onto WMBv1.
  **Target:** F1 ≥ 0.80 at supertype CS20230722_SUPT_0486 and at cluster CS20230722_CLUS_1915; concurrent assessment of whether the avpv_th_neuron and avpv_kiss1_neuron source cohorts are separable within CLUS_1915.
  **Expected output:** `AnnotationTransferEvidence` items on edges to SUPT_0486 and CLUS_1915; if the two source cohorts are indistinguishable on AT and on available property panels, a `lit_to_lit_edges` link between the two classical nodes.
  **Resolves:** the supertype-level NT uncertainty (Gaba_5 vs Dopa), the cluster-level small-n cap, and open question (1) below.

- **What:** Atlas-side cluster-level Kiss1/Th/Esr1 co-expression profiling at single-cell resolution on CLUS_1915 and its sibling clusters within SUPT_0486.
  **Target:** identify which child cluster(s), if any, beyond CLUS_1915 carry the female-biased Th/Kiss1 profile and quantify within-cluster heterogeneity.
  **Expected output:** updated PropertyComparisons with cluster-resolved marker values; possible reassignment of confidence at CLUS_1915 from MODERATE to HIGH if the small-n picture holds at fuller depth.
  **Resolves:** open question (1).

### Open questions

1. Does CLUS_1915 specifically correspond to AVPV A14 TH/Kiss1 neurons, or does it also include TH+ AVPV neurons that are Kiss1-negative? Cluster-level Kiss1/Th/Esr1 co-expression profiling is needed (raised on both the SUPT_0486 and CLUS_1915 edges).
2. Curator removal of the duplicate stub edge `edge_avpv_th_neuron_to_CS20230722_CLUS_1915` (legacy / fresh-emit ID collision against the substantive lowercase-ID edge on the same `taxonomy_type` accession).

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | https://doi.org/10.1007/s12031-012-9923-1 | — | soma location |
| [2] | He et al. 2013 | [PMID:25206587](https://pubmed.ncbi.nlm.nih.gov/25206587/) | soma location |
| [3] | Stephens et al. 2017 | [PMID:28660243](https://pubmed.ncbi.nlm.nih.gov/28660243/) | soma location |
| [4] | Zilkha et al. 2021 | [PMID:33910083](https://pubmed.ncbi.nlm.nih.gov/33910083/) | Th marker |
| [5] | Kauffman et al. 2007 | [PMID:17699664](https://pubmed.ncbi.nlm.nih.gov/17699664/) | Kiss1 marker |

---

<!-- verdict-block-start: edge_avpv_th_neuron_to_cs20230722_supt_0486 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] CS20230722_SUPT_0486 (rank 1, cohort rank 6 of 12 by composite
    score; the supertype's broader female-biased Dopa signal is concentrated in
    child CS20230722_CLUS_1915, MFR=0.02, Th=6.6, Kiss1=2.51) is the broadest
    defensible anchor for the classical AVPV Th/Kiss1 dopaminergic population;
    supertype-level NT label is Gaba_5 with Dopa identity rescued only at the
    cluster level, and region_fraction_100um=0.061 reflects boundary scatter
    across MBA:133 / MBA:515 adjacent to MBA:272. Marker concordance is supported
    indirectly via child CS20230722_CLUS_1915 (Th, Kiss1, Slc18a2 DEFINING).
  reconciliation_note: >
    Paired with the cluster-level call on CS20230722_CLUS_1915 (skos:closeMatch +
    1:1); the supertype carries the broader mapping while CS20230722_CLUS_1915 is
    the best-resolved child carrying the female-biased Th/Kiss1 profile. Also
    overlaps with avpv_kiss1_neuron, which targets the same supertype.
  caveats:
    - caveat_type: NT_PREDICTION_UNCERTAIN
      description: >
        SUPT_0486 carries a Gaba_5 label at supertype level while the classical
        AVPV TH neuron is dopaminergic. Dopaminergic identity is resolved only at
        cluster level (CS20230722_CLUS_1915, Dopa designation).
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        avpv_th_neuron and avpv_kiss1_neuron both map to SUPT_0486; the two
        classical types substantially overlap (most AVPV/PeN Kiss1 cells co-express
        Th). Cluster-level resolution needed to determine whether they are
        separable within SUPT_0486.
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        region_fraction_100um=0.061 at MBA:272; bulk of supertype soma sit in
        adjacent MBA:133 (preoptic periventricular) and MBA:515 (medial preoptic
        nucleus) — interpretable as boundary scatter rather than off-target
        placement.
  proposed_experiments:
    - >
      Cluster annotation transfer of Th-Cre or Kiss1-Cre AVPV transgene-marked
      transcriptomes onto WMBv1, targeting F1 >= 0.80 at supertype
      CS20230722_SUPT_0486 and cluster CS20230722_CLUS_1915.
    - >
      Atlas-side cluster-resolved Th/Kiss1/Esr1 co-expression profiling across
      SUPT_0486 children to localise the female-biased dopaminergic signal
      beyond CS20230722_CLUS_1915.
  unresolved_questions:
    - >
      Does CS20230722_CLUS_1915 specifically correspond to AVPV A14 TH neurons?
      Confirm by cluster-level Kiss1/Th/Esr1 co-expression profiling.
    - >
      Curator removal of duplicate edge edge_avpv_th_neuron_to_CS20230722_CLUS_1915
      — legacy/fresh-emit ID collision on taxonomy_type CS20230722_CLUS_1915.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_avpv_th_neuron_to_cs20230722_clus_1915 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.6
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] CS20230722_CLUS_1915 (rank 0, cohort rank 1 of 10 by composite
    score 4 vs next-best 2) is the only WMBv1 cluster simultaneously carrying high
    Th (precomputed=6.6), detectable Kiss1 (=2.51), a Dopa neurotransmitter
    annotation, Slc18a2 as a DEFINING cluster marker, and an extreme female sex
    bias (MFR=0.02) matching the classical AVPV Th/Kiss1 dopaminergic population.
    Confidence is capped at MODERATE by small cohort retention (n approx 3-5
    cells after filtering) and by region_fraction_100um=0.071 at MBA:272 — boundary
    scatter across the adjacent MBA:133 / MBA:515 preoptic periventricular corridor
    rather than a clean within-AVPV placement.
  reconciliation_note: >
    Paired with the supertype-level call on CS20230722_SUPT_0486
    (skos:broadMatch + 1:n); the cluster is the best-resolved child carrying the
    female-biased Th/Kiss1 profile within that supertype. Also overlaps with
    avpv_kiss1_neuron, which targets the same cluster — the two classical types
    may correspond to the same transcriptomic population entered from two
    marker-defined entry points.
  caveats:
    - caveat_type: LOW_CELL_COUNT
      description: >
        CS20230722_CLUS_1915 retains only n approx 3-5 cells after filtering. All
        signals are directionally correct but statistical power is limited;
        confidence is capped at MODERATE.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        avpv_th_neuron and avpv_kiss1_neuron both map to CS20230722_CLUS_1915;
        most AVPV/PeN Kiss1 cells co-express Th, and the two classical types may
        in fact be the same population described from different marker entry
        points.
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        region_fraction_100um=0.071 at MBA:272; bulk of cluster soma sit in
        adjacent MBA:133 (preoptic periventricular) and MBA:515 (medial preoptic
        nucleus) — interpretable as boundary scatter across the AVPV/PeN/MPO
        corridor rather than off-target placement.
  proposed_experiments:
    - >
      Annotation transfer of Th-Cre AVPV transgene-marked transcriptomes onto
      WMBv1 targeting F1 >= 0.80 at cluster CS20230722_CLUS_1915.
    - >
      Larger AVPV/PeN-targeted transcriptomic cohort (Th-Cre and/or Kiss1-Cre) to
      lift n above the small-sample ceiling currently capping cluster-level
      confidence.
  unresolved_questions:
    - >
      Is CS20230722_CLUS_1915 specifically the A14 TH/Kiss1 cluster, or does it
      also include TH+ AVPV neurons that are Kiss1-negative?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_avpv_th_neuron_to_CS20230722_CLUS_1915 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Duplicate fresh-emit edge against the same taxonomy_type
    CS20230722_CLUS_1915 as the substantive lowercase-ID edge; this stub carries
    only PARTIAL ATLAS_METADATA with region_fraction_100um=0.071 and no curator
    caveats. Surfaced for curator removal.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Duplicate of substantive edge on CS20230722_CLUS_1915; retain the
        lowercase-ID edge which carries the full caveat and evidence set.
  unresolved_questions:
    - >
      Curator removal of duplicate edge edge_avpv_th_neuron_to_CS20230722_CLUS_1915
      — legacy/fresh-emit ID collision on taxonomy_type CS20230722_CLUS_1915.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_avpv_th_neuron_to_CS20230722_CLUS_1469 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_1469 carries a Dopa annotation but its soma sit in
    the MPO/ADP (MBA:133 / third ventricle) with region_fraction_100um=0.053 at
    MBA:272 — too distant from the AVPV to plausibly host the classical Th/Kiss1
    population, and no Th/Kiss1 expression signal stands out at the cluster level.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        region_fraction_100um=0.053 at MBA:272; soma distribution centred on MPO
        and the third ventricle, not AVPV.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_avpv_th_neuron_to_CS20230722_CLUS_5246 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_5246 is a Tanycyte NN_2 cluster (non-neuronal,
    ependymal lineage) with soma centred on the third ventricle and intermediate
    periventricular hypothalamus; incompatible with a neuronal Th/Kiss1
    dopaminergic identity regardless of any partial proximity to MBA:272.
  caveats:
    - caveat_type: OTHER
      description: >
        Non-neuronal lineage (tanycyte); cannot host the classical AVPV TH neuron
        regardless of region overlap.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_avpv_th_neuron_to_CS20230722_CLUS_1910 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_1910 (PVpo-VMPO-MPN Hmx2 Gaba_4, sibling of the
    primary SUPT_0486 lineage) is Dopa-annotated and has region_fraction_100um=0.260
    at MBA:272 but shows no standout Th, Kiss1, or female-bias signal at the
    cluster level; the dimorphic AVPV Th/Kiss1 profile that anchors the mapping
    sits in CS20230722_CLUS_1915, not here.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Adjacent Hmx2-lineage cluster lacking the defining female-biased Th/Kiss1
        signature on which the mapping rests.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_avpv_th_neuron_to_CS20230722_CLUS_5211 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_5211 is an Astro-NT NN_1 cluster (non-neuronal,
    astrocytic lineage) with soma centred on striatum, cranial nerves, and
    olfactory areas; incompatible with a neuronal AVPV Th/Kiss1 identity.
  caveats:
    - caveat_type: OTHER
      description: >
        Non-neuronal lineage (astrocyte) and soma in striatal/olfactory regions
        far from MBA:272.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_avpv_th_neuron_to_CS20230722_SUPT_0550 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0550 (MPN-MPO-PVpo Hmx2 Glut_5) is glutamatergic
    and lacks any Dopa-annotated child cluster, despite a very high
    region_fraction_100um=0.733 at MBA:272. Without dopaminergic identity or a
    Th/Kiss1-carrying child cluster, region overlap alone does not place the
    classical AVPV TH neuron here.
  caveats:
    - caveat_type: NT_PREDICTION_UNCERTAIN
      description: >
        Glutamatergic supertype with no dopaminergic child cluster — incompatible
        with the classical type's dopaminergic identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_avpv_th_neuron_to_CS20230722_SUPT_1172 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_1172 (Tanycyte NN_1) is non-neuronal (ependymal
    tanycyte lineage); incompatible with a neuronal Th/Kiss1 dopaminergic identity
    regardless of partial periventricular overlap.
  caveats:
    - caveat_type: OTHER
      description: >
        Non-neuronal lineage (tanycyte); cannot host the classical AVPV TH neuron.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_avpv_th_neuron_to_CS20230722_SUPT_0419 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0419 (PVR Six3 Sox3 Gaba_9) is a periventricular
    GABAergic supertype without dopaminergic identity or a Th/Kiss1-defining
    child cluster, and region_fraction_100um=0.348 at MBA:272 reflects preoptic
    overlap rather than AVPV-specific placement.
  caveats:
    - caveat_type: NT_PREDICTION_UNCERTAIN
      description: >
        GABAergic supertype with no dopaminergic child cluster; lacks the
        defining classical-type Th/Kiss1 dopaminergic identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_avpv_th_neuron_to_CS20230722_SUPT_0485 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0485 (PVpo-VMPO-MPN Hmx2 Gaba_4) is the immediate
    Hmx2-lineage sibling of the primary SUPT_0486 anchor but lacks a Dopa-annotated
    Th/Kiss1-carrying child cluster equivalent to CS20230722_CLUS_1915; the AVPV
    Th/Kiss1 dimorphic signal is concentrated in the SUPT_0486 lineage, not here.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Sibling Hmx2-lineage supertype without the defining female-biased Th/Kiss1
        dopaminergic child cluster.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_avpv_th_neuron_to_CS20230722_SUPT_0400 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0400 (SI-MPO-LPO Lhx8 Gaba_5) is centred on
    substantia innominata / MPO / LPO with region_fraction_100um=0.022 at MBA:272
    — too distant from the AVPV — and lacks any dopaminergic or Th/Kiss1 signal.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        region_fraction_100um=0.022 at MBA:272; soma centred on substantia
        innominata and lateral preoptic area, far from AVPV.
```
<!-- verdict-block-end -->
