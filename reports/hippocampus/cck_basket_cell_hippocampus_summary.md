# Cholecystokinin-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Cholecystokinin-positive (CCK+) basket cells are CGE-derived GABAergic interneurons of the hippocampal formation whose axons, like those of PV basket cells, target the perisomatic region of pyramidal cells [1][2][3][4]. They are defined by co-expression of Cck and the CB1 cannabinoid receptor (Cnr1/CB1R), which makes them cannabinoid-sensitive — a distinguishing feature from the CB1R-negative PV basket cells [5]. Together with PV basket cells they form the two major perisomatic inhibitory populations of the hippocampus and cortex, yet they differ substantially in firing pattern, plasticity, and network engagement [4].

> We focused on cholecystokinin (CCK)-containing(+) GABAergic interneurons because their morphological and molecular features are thought to form a quasi-continuum from axon- to dendrite-targeting interneurons
> — Fuzik et al. 2015, Results · [7] <!-- quote_key: 7738817_f3d2a066 -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | [1][2][3][4] |
| NT | GABAergic | [3] |
| Markers | Cck (defining); Cnr1 (CB1R, defining); Vglut3 | Cck [5][2][4][6][7]; Cnr1 [5] |
| Negative markers | Pvalb (absent) | — |
| Neuropeptides | Cck | [5] |
| CL term | basket cell [CL:0000118] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / CB1R identity:** rat hippocampus immunolocalisation of CB1R on basket cell perisomatic boutons · [5]
  > To understand the functional significance and mechanisms of action in the CNS of endogenous and exogenous cannabinoids, it is crucial to identify the neural elements that serve as the structural substrate of these actions. We used a recently developed antibody against the CB1 cannabinoid receptor to study this question in hippocampal networks. Interneurons with features typical of basket cells showed a selective, intense staining for CB1 in all hippocampal subfields and layers. Most of them (85.6%) contained cholecystokinin (CCK), which corresponded to 96.9% of all CCK-positive interneurons, whereas only 4.6% of the parvalbumin (PV)- containing basket cells expressed CB1. Accordingly, electron microscopy revealed that CB1-immunoreactive axon terminals of CCK- containing basket cells surrounded the somata and proximal dendrites of pyramidal neurons, whereas PV-positive basket cell terminals in similar locations were negative for CB1. The synthetic cannabinoid agonist WIN 55,212-2 (0.01–3 μm) reduced dose- dependently the electrical field stimulation-induced [3H]GABA release from superfused hippocampal slices, with an EC50 value of 0.041 μm. Inhibition of GABA release by WIN 55,212-2 was not mediated by inhibition of glutamatergic transmission because the WIN 55,212-2 effect was not reduced by the glutamate blockers AP5 and CNQX. In contrast, the CB1 cannabinoid receptor antagonist SR 141716A (1 μm) prevented this effect, whereas by itself it did not change the outflow of [3H]GABA. These results suggest that cannabinoid-mediated modulation of hippocampal interneuron networks operate largely via presynaptic receptors on CCK-immunoreactive basket cell terminals. Reduction of GABA release from these terminals is the likely mechanism by which both endogenous and exogenous CB1 ligands interfere with hippocampal network oscillations and associated cognitive functions.
  > — Katona et al. 1999, Classical Functional and Morphological Interneuron Types · [5] <!-- quote_key: 480205_62cd73ae -->

- **CCK marker / CB1R positive vs PV basket cells:** rat hippocampus IHC distinguishing CCK and PV perisomatic populations · [1]
  > Most CB + 1 terminals surrounding the somata and proximal dendrites of pyramidal neurons were cholecystokinin + (CCK) GABAergic interneurons (basket cells) and, to a lower extent, calbindin D-28k + GABAergic interneurons (Katona et al., 1999) (Marsicano et al., 1999)(Tsou et al., 1999). However, parvalbumin + GABAergic interneuron terminals localized in pyramidal cell layers were negative for CB 1 (Katona et al., 1999)(Marsicano et al., 1999)
  > — Rivera et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 10540334_418c51dd -->

- **CCK and PV as the two major perisomatic populations:** intersectional genetic mapping across forebrain · [4]
  > Cholecystokinin (CCK)- and parvalbumin (PV)-expressing neurons constitute the two major populations of perisomatic GABAergic neurons in the cortex and the hippocampus. As CCK- and PV-GABA neurons differ in an array of morphological, biochemical and electrophysiological features, it has been proposed that they form distinct inhibitory ensembles which differentially contribute to network oscillations and behavior. However, the relationship and balance between CCK- and PV-GABA neurons in the inhibitory networks of the brain is currently unclear as the distribution of these cells has never been compared on a large scale. Here, we systemically investigated the distribution of CCK- and PV-GABA cells across a wide number of discrete forebrain regions using an intersectional genetic approach. Our analysis revealed several novel trends in the distribution of these cells. While PV-GABA cells were more abundant overall, CCK-GABA cells outnumbered PV-GABA cells in several subregions of the hippocampus, medial prefrontal cortex and ventrolateral temporal cortex. Interestingly, CCK-GABA cells were relatively more abundant in secondary/ association areas of the cortex (V2, S2, M2, and AudD/AudV) than they were in corresponding primary areas (V1, S1, M1, and Aud1). The reverse trend was observed for PV-GABA cells. Our findings suggest that the balance between CCK- and PV-GABA cells in a given cortical region is related to the type of processing that area performs; inhibitory networks in the secondary cortex tend to favor the inclusion of CCK-GABA cells more than networks in the primary cortex. The intersectional genetic labeling approach employed in the current study expands upon the ability to study molecularly defined subsets of GABAergic neurons. This technique can be applied to the investigation of neuropathologies which involve disruptions to the GABAergic system, including schizophrenia, stress, maternal immune activation and autism.
  > — Whissell et al. 2015, Classification Schemes and Methodological Approaches · [4] <!-- quote_key: 16859318_009e9f36 -->

</details>

Cell Ontology mapping: basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] (BROAD). CL:0000118 covers perisomatic morphology but does not capture CCK/CB1R marker identity or regular-spiking firing pattern; no CCK-specific basket cell term exists in CL.

---

## Results

Two candidate atlas entries were assessed. The AT-supported candidate is the Sncg-subclass supertype 0187 Sncg Gaba_3 [CS20230722_SUPT_0187] (LOW confidence) identified via Harris 2018 CA1 inhibitory transcriptomics. A second candidate 0179 Vip Gaba_7 [CS20230722_SUPT_0179] (UNCERTAIN, eliminated) is retained for record; it received no AT support and is based solely on atlas metadata.

**Annotation-transfer overview figure (run-level, filtered)**

![Filtered AT figure for Cholecystokinin-positive basket cell — Harris 2018 Cck.Cxcl14.Vip source group](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/figures/f1_for_cck_basket_cell_hippocampus.png)

*F1 across taxonomy levels for the Cck.Cxcl14.Vip source group from Harris 2018 CA1 inhibitory transcriptomics (GEO:GSE99888). This is the Harris CCK-expressing cluster with the strongest Sncg mapping signal (n=72 cells, group_purity=0.951 at SUPT_0187, F1=0.768). F1 ≥ 0.5 at a level indicates a clean mapping at that resolution; SUPT_0187 Sncg Gaba_3 clears this threshold.*

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---:|---|---|---|
| 1 | 0187 Sncg Gaba_3 [CS20230722_SUPT_0187] | — (supertype) | 1723 | 🔴 LOW | NT CONSISTENT · CGE origin CONSISTENT | Speculative |
| — | 0179 Vip Gaba_7 [CS20230722_SUPT_0179] | — (supertype) | 215 | ⚪ UNCERTAIN | NT CONSISTENT · location APPROXIMATE · Cck NOT_ASSESSED | Eliminated |

Total: 2 edges; 1 LOW, 1 UNCERTAIN.

### Property alignment — 0187 Sncg Gaba_3 [CS20230722_SUPT_0187] · 🔴 LOW

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | GABA (Sncg Gaba_3) | CONSISTENT |
| CGE developmental origin | CGE-derived (CCK+, Cnr1+) | Sncg subclass (CGE-derived) | Sncg subclass | CONSISTENT |
| Pvalb (negative) | absent | not Pvalb subclass | Sncg subclass | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Harris 2018 Cck.Cxcl14.Vip → WMBv1 (GEO:GSE99888) | Annotation transfer | PARTIAL | SUPT_0187 F1=0.768 (58/72 cells, group_purity=0.951, target_purity=0.644) at SUPERTYPE | atlas-internal |

### 0187 Sncg Gaba_3 [CS20230722_SUPT_0187] · 🔴 LOW

**Supporting evidence**
- Harris 2018 CA1 inhibitory cluster Cck.Cxcl14.Vip (CCK+/Cxcl14+/Vip+ hippocampal inhibitory cluster, n=72 cells) maps to SUPT_0187 Sncg Gaba_3 with F1=0.768 and group_purity=0.951. The high group_purity (95.1%) means 95% of this Harris CCK-expressing cluster maps to a single atlas supertype, providing directional evidence for Sncg Gaba_3 as the primary CCK basket cell supertype.
- CCK basket cells are CGE-derived; the Sncg subclass is well established as CGE-derived, consistent with CCK interneuron lineage. Pvalb is absent in the Sncg subclass, consistent with Pvalb-negative CCK basket cell identity.
- Harris AT provides stronger transcriptomic evidence for SUPT_0187 than the SUPT_0179 (Vip Gaba_7) edge, which has no AT support.

**Concerns**
- Cck.Cxcl14.Vip is a Harris 2018 Class label, not morphologically confirmed CCK basket cells. The Harris transcriptomic class is the best available proxy for CCK-expressing hippocampal CA1 interneurons, but basket cell morphology has not been confirmed for these cells.
- Cck, Cnr1, and Vglut3 — the three canonical CCK basket cell markers — are not documented in atlas supertype metadata; the assignment rests on CGE origin inference and transcriptomic class rather than direct marker confirmation.
- Low confidence (not MODERATE) because: (a) source label not morphologically confirmed; (b) target_purity = 0.644 indicates 36% of cells mapped to SUPT_0187 are not from the Cck.Cxcl14.Vip cluster; (c) no atlas metadata evidence on this edge.

**What would upgrade confidence**
- Morphologically confirmed CCK basket cell patch-seq dataset (Cnr1-Cre+ cells with confirmed perisomatic axon morphology) mapped to WMBv1 with F1 ≥ 0.75 at supertype level, group_purity ≥ 0.80.
- Confirmation that Cck, Cnr1, or Vglut3 are expressed in SUPT_0187 from WMBv1 precomputed stats.

## Eliminated candidates

The atlas-metadata-only edge to 0179 Vip Gaba_7 [CS20230722_SUPT_0179] (UNCERTAIN, no AT evidence) is eliminated. Harris AT does not support SUPT_0179 for CCK basket cells: the Cck.Cxcl14.Vip Harris cluster maps to SUPT_0187 with group_purity=0.951, with no significant signal to SUPT_0179.

### 0179 Vip Gaba_7 [CS20230722_SUPT_0179] · ⚪ UNCERTAIN

**Disqualifying signal:** (a) Vip Gaba subclass identity is unexpected for CCK basket cells whose primary identity is perisomatic CCK+/CB1R+, not Vip-defined; (b) Cck, Cnr1, and Vglut3 absent from supertype defining markers; (c) Harris AT data places the strongest CCK-expressing CA1 cluster at SUPT_0187, not SUPT_0179; (d) Cck precomputed mean for SUPT_0179 is 1.36, far below the expected expression level for a CCK-defining cell type. Vip-subclass CGE-derived CCK interneurons that co-express Vip cannot be formally excluded, but SUPT_0179 is not the AT-supported primary candidate.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The CCK basket cell is defined here on a CLASSICAL_MULTIMODAL basis: classical morphology + immunohistochemistry + cannabinoid pharmacology. Defining markers Cck [5][2][4][6][7], Cnr1 [5], Vglut3; negative marker Pvalb; neuropeptide Cck [5]; soma in CA1 stratum pyramidale [UBERON:0014548] [1][2][3][4]; GABAergic neurotransmission [3].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at rank 1 (supertype) using metadata-based scoring. Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to atlas-side values via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED.

**Annotation transfer.**

Run — Harris 2018 CA1 inhibitory neurons → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Harris 2018 published Class labels for 3663 mouse CA1 inhibitory neurons; source DOI: 10.1371/journal.pbio.2006387) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100). Run locally against precomputed_stats_ABC_revision_230821.h5. |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_matrix_harris_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/f1_matrix_harris_class.csv) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | This run scores Harris 2018 published Class labels against WMBv1. The companion run at_run_20260512_chamberland_subfamily_mmc_wmbv1 scores the same MMC output under Chamberland 2024 in-silico subfamily labels. Cck.Cxcl14.Vip is a transcriptomic class label, not morphologically confirmed CCK basket cells. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:09+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0187 | ANNOTATION_TRANSFER | PARTIAL | atlas-internal |
| edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Cholecystokinin-positive basket cell → 0187 Sncg Gaba_3 [CS20230722_SUPT_0187] at LOW confidence. Key support: Harris 2018 CA1 inhibitory transcriptomic cluster Cck.Cxcl14.Vip maps to SUPT_0187 with group_purity=0.951 and F1=0.768, providing the only available AT-level signal for a CCK basket cell atlas match. The Sncg subclass is CGE-derived and Pvalb-negative, consistent with CCK basket cell lineage. Key caveats: source label not morphologically confirmed basket cells; canonical CCK basket markers (Cck, Cnr1, Vglut3) absent from atlas supertype metadata; confidence held at LOW pending morphologically labelled CCK basket cell annotation transfer.

The 0179 Vip Gaba_7 [CS20230722_SUPT_0179] candidate is eliminated as UNCERTAIN — it lacks AT support and the Vip subclass identity is not expected for the canonical perisomatic CCK+/CB1R+ basket identity.

The Cell Ontology has no specific CCK basket cell term; basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] is a BROAD ancestor. A hippocampus-specific CCK basket cell CL term is a candidate new-term request.

### Proposed experiments and follow-ups

1. **Morphologically confirmed CCK basket cell annotation transfer.** MapMyCells of a source dataset containing morphologically identified CCK basket cells (Cnr1-Cre or Cck-Cre × morphological confirmation by patch-clamp + biocytin fill) onto WMBv1. Target: F1 ≥ 0.75 at supertype level with group_purity ≥ 0.80. Expected output: AnnotationTransferEvidence upgrading SUPT_0187 confidence from LOW to MODERATE. Resolves: source-label ambiguity caveat and Cck/Cnr1 marker confirmation gap.

2. **Precomputed marker check for Cck/Cnr1/Vglut3 in SUPT_0187.** Confirm or refute whether the canonical CCK basket cell markers are expressed in the Sncg Gaba_3 supertype from the WMBv1 precomputed stats. Expected output: new CONSISTENT or DISCORDANT property comparison entries on the SUPT_0187 edge.

3. **CL new term request.** Draft a CL term for "hippocampal CCK basket interneuron" via `workflows/cl-term-request.md`. Expected output: CL term issue; subsequent EXACT cl_mapping replacing the current BROAD.

### Open questions

1. Do CCK basket cells in hippocampus preferentially occupy SUPT_0187 (Sncg Gaba_3) or another CGE-derived supertype? The Harris AT provides directional evidence for SUPT_0187 but the low confidence and unconfirmed source label leave room for alternative assignments.

2. Are Cck, Cnr1, and Vglut3 detectable in SUPT_0187 at transcript level from WMBv1 precomputed stats or cluster-level expression matrices?

3. CCK basket cells are noted as "remarkably diverse, extending beyond Sncg transcriptomic class." Does this diversity mean a single supertype mapping is appropriate, or should multiple edges be expected across Sncg and Vip supertypes?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 | [25018703](https://pubmed.ncbi.nlm.nih.gov/25018703) | soma location |
| [2] | Fasano et al. 2017 | [28559797](https://pubmed.ncbi.nlm.nih.gov/28559797) | soma location; Cck marker |
| [3] | Whissell et al. 2015 | [26441554](https://pubmed.ncbi.nlm.nih.gov/26441554) | soma location; neurotransmitter type |
| [4] | Contreras et al. 2019 | [31297048](https://pubmed.ncbi.nlm.nih.gov/31297048) | soma location; CCK/PV perisomatic framing |
| [5] | Katona et al. 1999 | [10341254](https://pubmed.ncbi.nlm.nih.gov/10341254) | Cck marker; Cnr1 marker; neuropeptide; CB1R morphology |
| [6] | Huang et al. 2014 | [24533597](https://pubmed.ncbi.nlm.nih.gov/24533597) | Cck marker |
| [7] | Fuzik et al. 2015 | [26689544](https://pubmed.ncbi.nlm.nih.gov/26689544) | Cck marker; CCK IN diversity |
