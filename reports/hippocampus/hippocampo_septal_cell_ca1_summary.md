# Hippocampo-septal (HS) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

## Introduction

Hippocampo-septal (HS) cells are CA1 GABAergic interneurons whose somata lie
in stratum oriens and that send long-range projecting axons from the hippocampus
to the medial septum [1][2][3][4]. They co-express somatostatin (Sst), which is
both a defining marker and a neuropeptide of the type [1][5][6]. HS cells are one
of two principal Sst+ interneuron classes of CA1 — alongside oriens-lacunosum
moleculare (OLM) cells — but they are defined by their long-range septal
projection rather than by a local lacunosum-moleculare axonal arbor.
Mapping HS cells to the WMBv1 single-cell transcriptomic atlas is non-trivial:
the long-range projection identity is not captured in any precomputed atlas
property, and Sst+ CA1 stratum-oriens interneurons of multiple morphologies
share the same Sst transcriptomic neighbourhood.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | [1][2][3][4] |
| NT | GABAergic | — |
| Markers | Sst (defining) | [1][5][6] |
| Neuropeptides | Sst | — |
| CL term | sst chodl GABAergic interneuron [CL:4023121] (RELATED) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical morphology · CA1 stratum oriens with long-range axon to medial septum · [1][2][3][4]
  > SST+ cells were mainly found close to the alveus in the stratum-oriens of CA1 of both SAMR1 and SAMP8
  > — Takács et al. 2024, Molecular Markers and Gene Expression · [5] <!-- quote_key: 132515344_fb36f967 -->

  > horizontal interneurons in stratum oriens of the hippocampal CA1 area are often studied as a single group of interneurons, they include several cell types in addition to O-LM cells
  > — Oren et al. 2009, Conclusions · [4] <!-- quote_key: 1015389_2738d858 -->

</details>

Cell Ontology mapping: sst chodl GABAergic interneuron [[CL:4023121](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023121)] (RELATED).

---

## Results

One candidate atlas mapping was assessed; the primary (and only) candidate is
the supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at LOW confidence — a
shared Sst supertype that captures HS, OLM, and other CA1 stratum-oriens
Sst+ interneurons and is not separable for HS-specific identity from atlas
metadata or current annotation-transfer evidence.

![Filtered AT figure for Hippocampo-septal cell — Yao 2021 Sst SSv4 group](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_hippocampo_septal_cell_ca1.png)

*F1 across taxonomy levels for the Sst SSv4 source group (n=273 HIP cells)
from Yao 2021 GSE185862 hippocampal formation. The Sst label is
morphologically unresolved — encompassing OLM, bistratified, hippocampo-septal,
oriens-oriens and other Sst+ interneurons — and maps cleanly to the 053
Sst Gaba subclass at subclass level (F1 = 0.983) but distributes across
two supertypes at supertype level: 0219 Sst Gaba_6 [CS20230722_SUPT_0219]
(F1 = 0.759, dominant) and 0216 Sst Gaba_3 [CS20230722_SUPT_0216]
(F1 = 0.488). HS-specific cluster resolution is not achievable from this
source labelling.*

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---:|---|---|---|
| 1 | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — (supertype) | 2712 | 🔴 LOW | Sst CONSISTENT · CA1 SO CONSISTENT · Reln DISCORDANT | Speculative (shared Sst supertype) |

Total edges: 1 (LOW); relationship PARTIAL_OVERLAP.

### Primary candidate property alignment — 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🔴 LOW

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | not assessed | CONSISTENT |
| Soma location | CA1 stratum oriens [UBERON:0014552] — SOMA | Field CA1, stratum oriens (MBA:399, 818 cells) | not assessed | CONSISTENT |
| Sst expression | defining marker (IHC, mouse hippocampus) | Sst Gaba subclass — Sst is subclass-level marker; precomputed stats mean: 11.44 | not assessed | CONSISTENT |
| Sst neuropeptide | present | not in supertype neuropeptide list; precomputed stats mean: 11.44 | not assessed | CONSISTENT |
| Reln (target-side) | not a HS defining marker | Reln DEFINING marker of SUPT_0216; precomputed stats mean: 7.9 | not assessed | DISCORDANT |
| Rbp4 (target-side) | not listed | Rbp4 DEFINING marker of SUPT_0216 | not assessed | NOT_ASSESSED |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + MERFISH (SUPT_0216) | Atlas metadata | PARTIAL | CA1 SO 818 cells (largest single location) · Sst mean 11.44 · Reln mean 7.9 | atlas-internal |
| Yao 2021 SSv4 'Sst' MapMyCells (n=273 HIP cells) | Annotation transfer | PARTIAL | F1 = 0.488 at SUPT_0216 (target_purity 1.0, group_purity 0.323; SUPT_0219 dominant at F1 = 0.759) | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🔴 LOW

**Supporting evidence**
- SUPT_0216 is an MGE-derived Sst+ GABAergic supertype with its largest single MERFISH location in CA1 stratum oriens (818 cells). Both the Sst+ GABAergic identity and the CA1 stratum oriens soma location of HS cells [1][2][3][4][5] are consistent with this supertype.
- Sst (defining marker and neuropeptide of HS cells) is supported by the supertype's subclass placement (053 Sst Gaba) and a precomputed expression mean of 11.44 — among the highest in the atlas. This corroborates Sst as the principal classical marker via direct atlas evidence rather than literature alone.
- Yao 2021 (GEO:GSE185862) SSv4 'Sst'-labelled hippocampal cells (n=273) map onto SUPT_0216 with F1 = 0.488, target_purity = 1.0 (every cell delivered to SUPT_0216 came from the Sst SSv4 group), group_purity = 0.323 (83/273 cells land here). At subclass level the Sst group reaches F1 = 0.983 at the 053 Sst Gaba subclass; the supertype split between SUPT_0219 (F1 = 0.759, dominant) and SUPT_0216 (F1 = 0.488) reflects that the Sst SSv4 label is morphologically unresolved and encompasses multiple Sst+ CA1 interneuron types (OLM, bistratified, HS, oriens-oriens). The presence of *any* Sst-labelled signal in SUPT_0216 with perfect target purity is consistent with — but does not specifically identify — an HS subpopulation in this supertype.

**Marker evidence provenance**
- **Sst (defining and neuropeptide):** transcript-level confirmation via SUPT_0216 precomputed stats (Sst:11.44, among the highest in WMBv1); protein-level evidence from immunohistochemistry of Sst+ cells in CA1 stratum oriens [5]. Cell-type specificity for HS identity in the literature is weak: the classical node carries only one anchoring quote and the Sst antibody work [5] does not distinguish HS from OLM, bistratified, or other Sst+ stratum-oriens types. The defining-marker evidence supports the Sst+ identity component of the mapping but not the long-range-projection HS identity itself.

**Concerns**
- MARKER_NOT_SPECIFIC: Reln is listed as a DEFINING marker of SUPT_0216 (precomputed mean 7.9). Reln is a well-established OLM marker (Chrna2::Reln coexpression confirmed) and is not expected on HS cells. The presence of Reln as a supertype defining marker suggests SUPT_0216 predominantly captures OLM-like cells rather than HS cells.
- DISTRIBUTED_ACROSS_CLUSTERS: SUPT_0216 (Sst Gaba_3) is a shared supertype of at least three classical hippocampal Sst types — OLM cells (Sst+/Chrna2+/Reln+), bistratified cells (Sst+/Pvalb+/Tac1+), and HS cells (Sst+, long-range projecting). Independent MapMyCells AT of OLM interneurons (GSE124847) places 43/46 OLM cells onto SUPT_0216 (F1 = 0.67). The supertype is therefore not separable for HS-specific identity at supertype resolution, and the long-range septal projection — the defining HS feature — is not resolvable from atlas metadata.
- At supertype level the Yao 2021 Sst SSv4 cells preferentially land on SUPT_0219 Sst Gaba_6 (F1 = 0.759) rather than SUPT_0216 — i.e. the dominant transcriptomic correspondent of the broader Sst class is a *different* supertype, and SUPT_0216 receives a smaller, target-pure but morphologically unresolved subset.
- Very limited classical reference coverage for HS-specific evidence (one verbatim soma-location quote on the classical node). Ephys is uncharacterised at the classical-type level.

**What would upgrade confidence**
- Does SUPT_0216 contain any long-range projecting Sst+ neurons, or is it exclusively local-circuit (OLM, bistratified)? Requires a retrograde-traced (medial-septum-projecting) hippocampal scRNA-seq dataset → MapMyCells onto WMBv1; AnnotationTransferEvidence reaching F1 ≥ 0.5 at SUPT_0216 specifically for the projecting Sst+ subset.
- Is there a more appropriate HS candidate outside the Sst Gaba_3 supertype (e.g. Chodl+ class)? Requires a candidate sweep at supertype and class rank for Chodl-expressing Sst clusters, with property comparison against the HS classical profile.
- Targeted literature search for primary studies on HS-cell molecular profile beyond Sst (e.g. retrograde-traced HS-cell scRNA-seq, intersectional genetics for septal-projecting Sst+ INs). Current node coverage is weak (1 quote) and a focused cite-traverse may surface additional defining or negative markers (e.g. Chrna2 absence; Calb1, Npy, Chodl status).

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The hippocampo-septal (HS) cell is defined here on
a CLASSICAL_MULTIMODAL basis: the soma lies in CA1 stratum oriens [UBERON:0014552]
with a long-range axonal projection to the medial septum [1][2][3][4]; the type
is GABAergic; the defining marker and neuropeptide is Sst [1][5][6]. The classical
node carries very limited reference coverage (one anchoring verbatim quote) and
ephys characterisation is not recorded at the type level — both of which weaken
the literature side of the mapping evidence chain.

**Atlas mapping query.**

Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy
at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region
match, NT type, defining markers, sex bias when applicable). Full scoring
rules: `workflows/map-cell-type.md`.

**Property alignment.**

Each defining property of the classical type was compared to the corresponding
atlas-side value via the `property_comparisons` schema, with alignments graded
CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical
values came from precomputed expression on the cluster (cluster.yaml in the
taxonomy reference store) and from MERFISH spatial registration for soma
location.

**Annotation transfer.**

Yao 2021 SSv4 hippocampal formation → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4 Allen Institute taxonomy labels; Sst subclass label used here) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations). Per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.**

All citations, atlas accessions, ontology CURIEs, and verbatim literature
quotes in this report are validated against the evidencell knowledge base
at write time. Authored-prose evidence narratives are validated against
their source `evidence_items[*].explanation` fields. The pre-write hook
rejects any unresolvable identifier or unattributed blockquote. Specific
mapping limitations and caveats are documented per-candidate in the
Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:14+00:00 from
[kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0216 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Hippocampo-septal (HS) cell → 0216 Sst Gaba_3
[CS20230722_SUPT_0216] at LOW confidence. Key support: atlas metadata
(MGE-derived Sst+ supertype with largest MERFISH presence in CA1 stratum
oriens; Sst precomputed mean 11.44) and Yao 2021 SSv4 Sst-subclass
MapMyCells (F1 = 0.488 at supertype level, target_purity 1.0). Key caveats:
DISTRIBUTED_ACROSS_CLUSTERS (the supertype is shared between HS, OLM and
bistratified cells with no atlas-resolvable HS-specific feature) and
MARKER_NOT_SPECIFIC (Reln is a DEFINING marker of SUPT_0216 but is an OLM
rather than HS marker, suggesting the supertype predominantly captures
OLM-like cells).

The Cell Ontology term sst chodl GABAergic interneuron
[[CL:4023121](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023121)]
is a related but non-identical term. CL:4023121 partially overlaps (long-range
projecting SST+ INs) but HS cells are hippocampus-specific and may not express
Chodl. A dedicated CL term for the hippocampal HS cell may be warranted once
HS-specific molecular evidence is consolidated.

### Proposed experiments and follow-ups

**Cross-check with existing AT evidence.** The single AT run for this edge
(Yao 2021 SSv4 Sst subclass) is morphologically unresolved and cannot
distinguish HS from OLM or bistratified Sst+ types — F1 = 0.488 at
SUPT_0216 is the headline but every cell in the SUPT_0216 hit is from a
mixed Sst label, so the AT evidence is PARTIAL only. A refined AT run on a
morphologically or projection-resolved HS-cell source is needed.

1. **Retrograde-traced medial-septum-projecting Sst+ hippocampal scRNA-seq → MapMyCells.**
   - What: Retrograde tracer injection in medial septum followed by FACS or sorting of labelled hippocampal Sst+ cells, then scRNA-seq, then MapMyCells onto WMBv1.
   - Target: F1 ≥ 0.5 at SUPT_0216 specifically for the septal-projecting Sst+ subset (test whether the supertype contains any long-range projecting Sst+ neurons).
   - Expected output: AnnotationTransferEvidence on the SUPT_0216 edge; either lifts confidence (LOW → MODERATE) or refutes the supertype assignment.
   - Resolves: open question (1) below; the long-range-projection identity gap that is the principal LOW-confidence driver.

2. **Candidate sweep for HS-cell alternatives outside SUPT_0216.**
   - What: Re-run `map-cell-type` discovery at higher ranks (subclass, class) targeted at Chodl-expressing Sst clusters; compare against the HS property profile.
   - Target: identify any candidate atlas cluster or supertype with a CA1 stratum oriens + Sst+ + Chodl+ signature distinct from SUPT_0216.
   - Expected output: additional MappingEdge(s) — either confirming SUPT_0216 as the only available candidate or surfacing a better-aligned alternative.
   - Resolves: open question (2) below.

3. **Targeted literature search for primary HS-cell molecular characterisation.**
   - What: cite-traverse for "hippocampo-septal projection Sst hippocampus" and intersectional-genetic targeting studies of septal-projecting Sst+ INs.
   - Target: surface additional defining or negative markers (e.g. Chrna2 absence, Calb1, Npy, Chodl status) to strengthen the classical node beyond the current single anchoring quote.
   - Expected output: PropertySource entries added to the classical node; corresponding refinements to the property_comparisons.
   - Resolves: weak literature-side evidence chain.

### Open questions

1. Does SUPT_0216 contain any long-range projecting Sst+ neurons, or is it exclusively local-circuit (OLM, bistratified)?
2. Is there a more appropriate HS candidate outside the Sst Gaba_3 supertype (e.g. a Chodl+ class)?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | https://doi.org/10.1101/598599 | — | soma location |
| [2] | Müller & Remy 2017 | [29250747](https://pubmed.ncbi.nlm.nih.gov/29250747) | soma location |
| [3] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500) | soma location |
| [4] | Oren et al. 2009 | [19176803](https://pubmed.ncbi.nlm.nih.gov/19176803) | soma location |
| [5] | Takács et al. 2024 | [38470935](https://pubmed.ncbi.nlm.nih.gov/38470935) | Sst marker |
| [6] | Katona et al. 2017 | [27997999](https://pubmed.ncbi.nlm.nih.gov/27997999) | Sst marker |
