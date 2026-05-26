# Oriens-oriens (O-O) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The oriens-oriens (O-O) cell is a recently described GABAergic interneuron
of the CA1 hippocampus characterised by confinement of both soma and axon
to stratum oriens. It expresses Sst and Nos1, identified in a single study
by Chamberland et al. 2024 [1] using intersectional Sst-Cre;;Nos1-Flp
genetics. Of 15 cells obtained with the Sst;;Nos1 intersectional label,
12 (80%) were consistent with the O-O morphological description — soma
and axon restricted to stratum oriens without the lacunosum-moleculare
projection of OLM cells. The O-O cell is morphologically distinct from
other Sst+ stratum oriens types (OLM: projects to SLM; HS cell: long-range
projection to medial septum), though independent replication of O-O cell
identity as a discrete classical type is still needed.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | — |
| NT | GABAergic | — |
| Markers | Sst, Nos1 | [1] |
| CL term | No Cell Ontology term currently covers this type — candidate for a new CL term. | — |

Cell Ontology mapping: No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate mapping was assessed: 0219 Sst Gaba_6 [CS20230722_SUPT_0219]
at UNCERTAIN confidence (verdict: Eliminated). Evidence for the O-O cell as a
discrete classical type is thin (single study, n=12–15 cells), and the proposed
atlas correspondence cannot be confirmed because Nos1 expression is not confirmed
at atlas level (precomputed mean 1.81) and a CA3 versus CA1 subregional mismatch
persists. No MODERATE or LOW mapping edge was established.

## Eliminated candidates

### 0219 Sst Gaba_6 [CS20230722_SUPT_0219] · ⚪ UNCERTAIN

The primary shared disqualifying signal is the absence of Nos1 confirmation at
atlas level combined with a CA3 versus CA1 subregional mismatch.

**Supporting evidence**

- Sst expression strongly consistent: precomputed stats mean=10.17 for 0219 Sst Gaba_6 [CS20230722_SUPT_0219], matching the Sst-positive identity of O-O cells [1].
- 0219 Sst Gaba_6 [CS20230722_SUPT_0219] belongs to the Sst Gaba subclass (053 Sst Gaba), consistent with the GABAergic/Sst interneuron classification of O-O cells. NT type: CONSISTENT.
- Annotation transfer (MapMyCells; Yao 2021 Sst SSv4, GEO:GSE185862, n=273 HIP cells): Sst subclass maps to WMBv1 at subclass level (F1=0.983, 265 cells to 053 Sst Gaba). At supertype level, 0219 Sst Gaba_6 [CS20230722_SUPT_0219] is the dominant AT target within this subclass (F1=0.759, 161/273 cells, target_purity=0.964), indicating it captures the largest fraction of hippocampal Sst interneurons in the Yao 2021 dataset.

**Marker evidence provenance**

- **Sst:** Defined via Sst-Cre intersectional genetics by Chamberland et al. 2024 [1]. Precomputed stats (mean=10.17) confirm strong atlas-side Sst expression. Strongest molecular anchor for the proposed correspondence.
- **Nos1:** The second arm of the Sst;;Nos1 intersectional label used to isolate O-O cells [1], and the key feature distinguishing them from OLM and other Sst+ CA1 types. 0219 Sst Gaba_6 [CS20230722_SUPT_0219] does not list Nos1 among its defining markers; precomputed stats show a low mean=1.81 (alignment: APPROXIMATE). Whether this reflects genuine absence, heterogeneous expression within the supertype, or sub-threshold detection at supertype resolution is unknown.
- **Id3, Sp9 (atlas-defined markers of SUPT_0219):** No correspondence established in O-O cell classical literature — both are NOT_ASSESSED.
- **Annotation transfer caveat:** The AT source (Yao 2021 SSv4 Sst subclass) pools OLM, bistratified, hippocampo-septal, oriens-oriens, and other Sst interneuron types. Supertype-level resolution cannot discriminate O-O cells from co-resident Sst+ types.

**Concerns**

- **Subregional mismatch (APPROXIMATE):** O-O cells were characterised in CA1 stratum oriens [UBERON:0014552] [1]. 0219 Sst Gaba_6 [CS20230722_SUPT_0219] is CA3-enriched: the top location is CA3 stratum oriens (305 cells), with no prominent CA1 SO entry in the metadata. *(note: CA3 and CA1 are adjacent hippocampal subfields, but the CA3 versus CA1 distinction is a real anatomical difference — this is a meaningful subregional discrepancy, not a registration boundary error.)*
- **Nos1 not confirmed at atlas level:** The low Nos1 precomputed mean (1.81) is concerning given that Sst+/Nos1+ co-expression is the defining intersectional signature used to isolate O-O cells [1]. A different supertype or cluster with higher Nos1 and CA1 SO enrichment may be a better candidate.
- **Single-study evidence base:** O-O cell as a classically distinct type is supported by one study [1] with a small cell sample (n=12–15 cells). Robustness of the Sst+/Nos1+ definition and its distinctness from other CA1 Sst+ interneurons awaits independent replication.
- **Supertype resolution insufficient (MARKER_NOT_SPECIFIC):** Without Nos1 verification at atlas level, which supertype within the Sst Gaba subclass — if any — specifically captures the O-O cell population remains unclear.

**What would upgrade confidence**

- Demonstration of Nos1 expression in 0219 Sst Gaba_6 [CS20230722_SUPT_0219] at cluster level (cluster-level precomputed stats or scRNA-seq re-analysis of a Sst;;Nos1 intersectional dataset mapped to WMBv1) would be required to move to LOW confidence.
- Identification of a CA1 stratum oriens-enriched Sst+/Nos1+ supertype or cluster within the Sst Gaba subclass could shift the primary mapping candidate and raise confidence to LOW or MODERATE.
- Independent replication of the O-O cell morphological and molecular phenotype — ideally from a publicly available single-cell dataset with morphologically identified neurons — would strengthen the classical-side evidence sufficiently to attempt a more definitive mapping.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The oriens-oriens cell is defined on a
CLASSICAL_MULTIMODAL basis: soma in CA1 stratum oriens [UBERON:0014552]; GABAergic;
Sst and Nos1 as defining markers [1], identified by Sst-Cre;;Nos1-Flp intersectional
genetics. Evidence is from a single study (Chamberland et al. 2024 [1], n=12–15
cells). Ephys not characterised.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1
taxonomy (CCN20230722) at rank 1 (supertype) using metadata-based scoring. Full
scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property was compared to atlas values with
alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED.

**Annotation transfer.**

Run — Yao 2021 SSv4 hippocampal formation → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Sst; n=273 HIP cells) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells total | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | `f1_scores_best.csv` |
| Caveats | Yao 2021 SSv4 Sst label pools OLM, bistratified, HS, O-O, and other Sst interneurons; O-O-specific resolution unavailable. SUPT_0219 is the dominant Sst AT target; this does not confirm O-O identity. |

**Atlas data sources.** WMBv1 (CCN20230722); precomputed stats HDF5 at
`annotation_transfer/conf/mapmycells/CCN20230722/precomputed_stats.h5`.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and
verbatim literature quotes in this report are validated against the evidencell
knowledge base at write time. The pre-write hook rejects any unresolvable identifier
or unattributed blockquote.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:25+00:00 from
[kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER | PARTIAL; PARTIAL; PARTIAL | atlas-internal; GEO:GSE185862 |

</details>

---

## Discussion

**Primary mapping:** Oriens-oriens cell → 0219 Sst Gaba_6 [CS20230722_SUPT_0219] — UNCERTAIN (Eliminated). The proposed correspondence is plausible based on shared Sst+ identity, but cannot be confirmed: Nos1 is the defining discriminating feature of O-O cells (Sst;;Nos1 intersection) and the supertype's precomputed Nos1 mean (1.81) is low; the subregion is CA3-enriched rather than CA1-enriched; and the Yao 2021 AT is non-discriminative. No mapping edge at LOW or higher confidence can be established from current evidence.

Key caveats beyond the Nos1 and anatomical discordances: (1) the O-O cell itself is supported by a single study with n=12–15 cells — independent replication of the classical-side definition is needed before confident atlas mapping can be expected; (2) the Sst Gaba subclass contains multiple supertypes and no Sst+/Nos1+ supertype enriched in CA1 SO has been identified; (3) the Yao 2021 SSv4 Sst label is morphologically unresolved and SUPT_0219 being the dominant Sst supertype target does not specifically support O-O cell identity.

No Cell Ontology term is assigned to the O-O cell. It is a candidate for a new CL term once the classical definition is independently replicated.

### Proposed experiments

**Intersectional genetics + transcriptomics**

- scRNA-seq or snRNA-seq from Sst-Cre;;Nos1-Flp intersectional mouse hippocampus (CA1-enriched dissection); map to WMBv1 using MapMyCells. This is the most direct route to identifying the supertype(s) capturing the O-O population. Target: identification of a supertype with Nos1 penetrance substantially above the current 1.81 mean and CA1 SO enrichment. Expected output: AnnotationTransferEvidence on this edge, or identification of a better-fitting supertype at LOW or MODERATE confidence. Resolves: Q1, Q3.

**Atlas cluster re-analysis**

- Inspect cluster-level (not supertype-level) Nos1 expression within the Sst Gaba subclass (053 Sst Gaba). Target: identify any cluster with Nos1 mean substantially above 1.81 and hippocampal CA1 SO cell enrichment. Expected output: candidate replacement cluster for 0219 Sst Gaba_6 [CS20230722_SUPT_0219] as primary O-O mapping target. Resolves: Q1, Q3.

**Multiplex FISH**

- HiPlex RNAscope co-staining of CA1 and CA3 stratum oriens for Sst + Nos1 + Id3 + Sp9. Target: confirm whether Nos1-co-expressing Sst cells occur within Id3/Sp9-expressing clusters, providing spatial validation that 0219 Sst Gaba_6 [CS20230722_SUPT_0219] contains a Nos1+ subpopulation in CA1 SO — or identifying a different supertype or cluster. Resolves: Q1, Q2.

**Independent morphological replication**

- Independent replication of the O-O cell morphological phenotype (soma and axon confined to stratum oriens; absence of SLM projection) in mouse CA1, from a publicly available dataset or new electrophysiological/morphological study. This is a prerequisite for confident atlas mapping — the single-study, n=12–15 evidence base is insufficient to assess ambiguous atlas results.

### Open questions

1. Does 0219 Sst Gaba_6 [CS20230722_SUPT_0219] express Nos1 at meaningful penetrance? If so, is this confined to a specific cluster within the supertype?
2. Are the CA3 stratum oriens cells in 0219 Sst Gaba_6 [CS20230722_SUPT_0219] analogous to the CA1 O-O cells described by Chamberland et al. 2024 [1], or does the CA3 enrichment reflect a functionally distinct population?
3. Is there a CA1 stratum oriens-enriched Sst+/Nos1+ supertype in WMBv1 that better matches O-O cell identity than 0219 Sst Gaba_6 [CS20230722_SUPT_0219]?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347) | Sst marker; Nos1 marker; O-O cell identification via Sst;;Nos1 intersectional genetics |
