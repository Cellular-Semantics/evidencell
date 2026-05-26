# Hippocampo-septal (HS) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Hippocampo-septal (HS) cells are Somatostatin-positive GABAergic interneurons
of the CA1 hippocampus whose principal distinguishing feature is a long-range
axonal projection to the medial septum, with somata located predominantly in
stratum oriens close to the alveus [1][2][3][4]. Together with OLM cells they
constitute the two main Sst-expressing interneuron classes of CA1 stratum
oriens, but the two types differ fundamentally in axon target: OLM cells project
locally to stratum lacunosum-moleculare whereas HS cells project subcortically,
making the HS cell one of the few interneuron types to exert transregional
inhibitory influence beyond the hippocampus itself [2][4].

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | [1][2][3][4] |
| NT | GABAergic | — |
| Markers | Sst | [1][5][6] |
| Neuropeptides | Sst | — |
| CL term | sst chodl GABAergic interneuron [CL:4023121] (RELATED) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** stratum oriens of CA1, close to the alveus · [1][2][3][4]
  > "SST+ cells were mainly found close to the alveus in the stratum-oriens of CA1 of both SAMR1 and SAMP8"
  > — Perez et al. 2020, Molecular Markers and Gene Expression · [3] <!-- quote_key: 132515344_fb36f967 -->

  > "horizontal interneurons in stratum oriens of the hippocampal CA1 area are often studied as a single group of interneurons, they include several cell types in addition to O-LM cells"
  > — Oren et al. 2009, Conclusions · [4] <!-- quote_key: 1015389_2738d858 -->

- **Sst defining marker:** IHC evidence in mouse hippocampus · [1][5][6]

</details>

Cell Ontology mapping: sst chodl GABAergic interneuron [[CL:4023121](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023121)] (RELATED). CL:4023121 partially overlaps (long-range projecting SST+ interneurons) but HS cells are hippocampus-specific and may not express Chodl.

---

## Results

One candidate mapping was assessed: supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216]
at LOW confidence. Atlas metadata supports the Sst+ identity and CA1 stratum
oriens soma position, and Yao 2021 annotation transfer places a fraction of Sst
cells at this supertype. However, the supertype's Reln defining marker is an OLM
marker rather than an HS marker, and the overall supertype is OLM-enriched by
prior annotation-transfer evidence. The HS-defining long-range projection to the
medial septum is unresolvable from atlas metadata.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|-:|----|---|---|
| 1 | — | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | 2,712 | 🔴 LOW | Sst CONSISTENT · CA1 SO CONSISTENT · Reln DISCORDANT | Speculative |

Total: 1 edge (LOW); relationship type: PARTIAL_OVERLAP.

### Primary candidate property alignment — 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🔴 LOW

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | — | CONSISTENT |
| Soma location | CA1 stratum oriens [UBERON:0014552] | CA1 SO: 818 cells (largest single location) | — | CONSISTENT |
| Sst expression | defining marker [1][5][6] | Sst subclass; precomputed mean 11.44 | — | CONSISTENT |
| Sst neuropeptide | present | precomputed mean 11.44 | — | CONSISTENT |
| Reln expression | not listed; not an HS marker | DEFINING marker of SUPT_0216; precomputed mean 7.9 | — | DISCORDANT |
| Rbp4 expression | not listed | DEFINING marker of SUPT_0216 | — | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata: Sst+ GABA, CA1 SO anatomy | ATLAS_METADATA | PARTIAL | CA1 SO 818 cells; Sst consistent; Reln defining marker is OLM marker | atlas-internal |
| Yao 2021 SSv4 Sst → WMBv1 AT | ANNOTATION_TRANSFER | PARTIAL | SUPT_0216 F1=0.488 (83/273 cells); 053 Sst Gaba subclass F1=0.983 | GEO:GSE185862 |

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🔴 LOW

**Supporting evidence**

- Atlas metadata places 0216 Sst Gaba_3 [CS20230722_SUPT_0216] in the Sst GABAergic subclass with its largest hippocampal cell concentration in CA1 stratum oriens (818 cells). Both the Sst+ identity and the CA1 stratum oriens soma position are consistent with the HS cell classical definition [1][2][3][4].
- Yao 2021 (GEO:GSE185862) SSv4 Sst hippocampal cells (n=273) map to 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at supertype level (F1=0.488, 83 cells, target_purity=1.0), placing HS cells among the plausible Sst supertype targets. At subclass level, the Sst subclass mapping (053 Sst Gaba) is extremely clean (F1=0.983, 265/273 cells).

**Concerns and caveats**

- **Reln discordance.** Reln is listed as a DEFINING marker of 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (precomputed mean 7.9) and is a canonical OLM cell marker (Chrna2/Reln co-expression confirmed for OLM cells). Its presence as the supertype's primary defining marker indicates SUPT_0216 predominantly captures OLM-like cells rather than HS cells.
- **Shared, OLM-enriched supertype.** Prior annotation-transfer evidence (MapMyCells run on OLM interneurons from GEO:GSE124847) maps 43/46 OLM cells to 0216 Sst Gaba_3 [CS20230722_SUPT_0216] with F1=0.67, confirming this is an OLM-enriched supertype. Bistratified cells (Pvalb/Sst/Tac1+) may also contribute. HS-specific long-range projection identity cannot be verified from atlas metadata alone.
- **SUPT_0219 dominance.** At supertype level, 0219 Sst Gaba_6 [CS20230722_SUPT_0219] is the dominant recipient of Sst cells in the annotation transfer (161/273 cells, F1=0.759), making it the primary Sst supertype target overall; 0216 Sst Gaba_3 [CS20230722_SUPT_0216] captures a smaller fraction.
- **No HS-defining projecting feature assessable.** The long-range axonal projection to the medial septum that defines HS cells is not encoded in atlas metadata and cannot be evaluated with current evidence.
- **Yao 2021 AT is non-discriminative.** The Sst SSv4 source label (n=273 HIP cells) pools OLM, bistratified, hippocampo-septal, oriens-oriens, and other Sst interneuron types without morphological labels; subtype resolution requires a dedicated dataset.

**What would upgrade confidence**

- Patch-seq or single-cell RNA-seq of morphologically or physiologically confirmed HS cells (identified by antidromic stimulation from the medial septum or by Sst-Cre × retrograde-tracer approach) mapped onto WMBv1. Target: F1 ≥ 0.70 at CLUSTER level within the Sst Gaba subclass or an alternative Sst supertype.
- Query of WMBv1 Sst Gaba_3 child clusters for Chodl expression — if any child cluster is Chodl+, it would be a priority HS candidate distinct from the Reln+ OLM-like clusters.
- IHC co-staining of Chodl and Reln in CA1 stratum oriens Sst+ cells to test whether HS cells are Reln-negative at protein level, which would sharpen the search within SUPT_0216 child clusters.

## Eliminated candidates

No additional edges assessed. 0219 Sst Gaba_6 [CS20230722_SUPT_0219], the dominant Sst AT target (F1=0.759), was noted as an alternative candidate requiring further investigation and is not formally eliminated — it may be a better primary candidate than 0216 Sst Gaba_3 [CS20230722_SUPT_0216] for some Sst interneuron types.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The hippocampo-septal cell is defined on a
CLASSICAL_MULTIMODAL basis: soma in CA1 stratum oriens close to the alveus [1][2][3][4];
GABAergic; Sst as defining marker [1][5][6]; Sst as neuropeptide. The HS-specific
feature (long-range projection to medial septum) is not encodable from atlas metadata
alone. Reference coverage is sparse (one direct quote in the corpus).

**Atlas mapping query.**

Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at
rank 1 (supertype) using metadata-based scoring (region match, NT type, defining
markers). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.**

Each defining property of the classical type was compared to the corresponding
atlas-side value via the `property_comparisons` schema, with alignments graded
CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values
came from precomputed expression on the supertype.

**Annotation transfer.**

Run — Yao 2021 SSv4 hippocampal formation → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4; Allen Institute taxonomy labels) |
| Source cluster label | Sst (n=273 HIP cells) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells total | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | `f1_scores_best.csv` |
| Caveats | Yao 2021 SSv4 Sst label is morphologically heterogeneous; subtype resolution requires morphologically identified Sst-IN labels. |

**Atlas data sources.** WMBv1 (CCN20230722); precomputed stats HDF5 at
`annotation_transfer/conf/mapmycells/CCN20230722/precomputed_stats.h5`.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and
verbatim literature quotes in this report are validated against the evidencell
knowledge base at write time. The pre-write hook rejects any unresolvable identifier
or unattributed blockquote.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:24+00:00 from
[kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0216 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal; GEO:GSE185862 |

</details>

---

## Discussion

**Primary mapping:** Hippocampo-septal cell → 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at LOW confidence. Key support: Sst+ identity and CA1 stratum oriens soma position are both CONSISTENT with 0216 Sst Gaba_3 [CS20230722_SUPT_0216]; Yao 2021 annotation transfer places 83/273 Sst cells at this supertype (F1=0.488, target_purity=1.0). Key caveats: the Reln defining marker of the supertype is an OLM marker, suggesting SUPT_0216 predominantly captures OLM rather than HS cells; the Yao 2021 Sst label is morphologically unresolved and cannot discriminate HS from OLM; the HS-specific long-range projection to the medial septum is not detectable from current atlas metadata; and 0219 Sst Gaba_6 [CS20230722_SUPT_0219] (the dominant Sst AT target, F1=0.759) may be an equally or more plausible candidate.

The Cell Ontology RELATED mapping to CL:4023121 (sst chodl GABAergic interneuron) is a placeholder: the HS cell is a long-range projecting Sst+ interneuron, but hippocampal specificity and possible absence of Chodl expression distinguish HS cells from the neocortical/subcortical Sst-Chodl population for which CL:4023121 was described. The HS cell is a candidate for a dedicated CL term.

### Proposed experiments

**Transcriptomics / patch-seq**

- Antidromic stimulation from the medial septum to identify HS cells in acute slices, followed by patch-seq, to obtain morphologically confirmed HS cell transcriptomes for MapMyCells mapping onto WMBv1. Target: F1 ≥ 0.70 at CLUSTER level within the Sst Gaba subclass.
- Single-cell RNA-seq of Sst-Cre × retrograde-tracer-labelled cells from CA1 stratum oriens (tracer injected into medial septum) to establish whether HS cells form a coherent transcriptomic cluster distinct from OLM cells.

**Marker / IHC validation**

- IHC co-staining of Chodl and Reln in CA1 stratum oriens Sst+ cells to determine whether HS cells are Reln-negative and/or Chodl-positive, distinguishing them from OLM-like cells at the protein level and guiding the WMBv1 cluster search.
- Targeted IHC for potential HS-specific distinguishing markers (e.g. Chodl, absence of Chrna2) in morphologically confirmed long-range projecting cells.

**Atlas resolution**

- Query child clusters within WMBv1 Sst Gaba_3 [CS20230722_SUPT_0216] and Sst Gaba_6 [CS20230722_SUPT_0219] for Reln-low/Reln-negative child clusters and for any Chodl+ population to identify priority HS-cell candidate clusters.

### Open questions

1. Does 0216 Sst Gaba_3 [CS20230722_SUPT_0216] contain any long-range projecting Sst+ neurons, or is it exclusively a local-circuit (OLM-dominant) supertype?
2. Is there a more appropriate WMBv1 supertype for HS cells outside the Sst Gaba_3 supertype — for example within Sst Gaba_6 [CS20230722_SUPT_0219] or a Chodl+ supertype?
3. Do hippocampo-septal cells express Chodl, and if so, are they captured by the Sst Chodl class in WMBv1?
4. Can HS and OLM cells be reliably separated by single-cell transcriptomics given their shared Sst+ identity and CA1 stratum oriens soma position?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | https://doi.org/10.1101/598599 | — | soma location; Sst marker |
| [2] | Müller & Remy 2017 | [29250747](https://pubmed.ncbi.nlm.nih.gov/29250747) | soma location |
| [3] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500) | soma location |
| [4] | Oren et al. 2009 | [19176803](https://pubmed.ncbi.nlm.nih.gov/19176803) | soma location |
| [5] | Takács et al. 2024 | [38470935](https://pubmed.ncbi.nlm.nih.gov/38470935) | Sst marker |
| [6] | Katona et al. 2017 | [27997999](https://pubmed.ncbi.nlm.nih.gov/27997999) | Sst marker |
