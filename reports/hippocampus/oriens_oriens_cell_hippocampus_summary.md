# Oriens-oriens (O-O) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The oriens-oriens (O-O) cell is a CA1 stratum oriens GABAergic interneuron whose axon is confined to the same stratum oriens (UBERON:0014552) layer where its soma resides, distinguishing it from oriens-lacunosum-moleculare (OLM) cells whose axons project away to stratum lacunosum-moleculare. The type was defined in a single study using Sst;;Nos1 intersectional Cre/Flp genetics to label cells expressing both Sst and Nos1, and Nos1 is therefore not an incidental marker but the defining co-receptor of the lineage-style intersection used to isolate the population [1]. The evidentiary base is thin (one paper, n = 12/15 Sst;;Nos1 intersectional cells in the reported sample), and the mapping question is whether any WMBv1 supertype or cluster captures the Sst+/Nos1+ CA1 stratum oriens fraction with axon-confinement-compatible properties.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | — |
| Neurotransmitter | GABAergic | — |
| Defining markers | Sst, Nos1 | Sst [1] |
| Negative markers | — | — |
| Neuropeptides | — | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Sst (defining marker):** literature source on the classical node · [1]

(No other property carries a literature source on the classical node; the type is supported by a single intersectional-genetics study and the remainder of the property table is inherited from that work as cited in the node `notes`.)
</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Annotation transfer evidence from the Yao 2021 (GEO:GSE185862) hippocampal SMART-Seq v4 dataset places the broad Sst-expressing interneuron pool of mouse hippocampus onto WMBv1 supertype 0219 Sst Gaba_6 [CS20230722_SUPT_0219] at the supertype level (F1=0.76, n=161 of 273 Sst cells; see figure and Table 2), but the Yao SSv4 "Sst" label is a coarse subclass pool that does not distinguish O-O from other Sst-IN morphological types (OLM, bistratified, hippocampo-septal, P-LM, R-LM, L-th), so the AT signal supports placement somewhere within the Sst Gaba subclass without identifying the O-O-specific subset. The Sst+/Nos1+ co-expression that intersectionally defines the type is not uniquely satisfied by any single WMBv1 supertype or cluster in the surveyed cohort: candidates that best satisfy Nos1 (0850 Sst Chodl Gaba_2 [CS20230722_CLUS_0850], Nos1=12.14) sit in distant non-hippocampal regions, while candidates with the cleanest CA1 stratum oriens location (0768 Sst Gaba_3 [CS20230722_CLUS_0768], 0772 Sst Gaba_3 [CS20230722_CLUS_0772], 0216 Sst Gaba_3 [CS20230722_SUPT_0216]) carry only weak-to-moderate Nos1 expression.

![Filtered AT figure for oriens-oriens cell](figures/f1_for_oriens_oriens_cell_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 SSv4 "Sst" source group (n=273 hippocampal cells; the source label pools all Sst-expressing hippocampal interneuron morphological types). Each node is coloured by F1 with **Purity** (Pur, fraction of target cells from the source group) and **Coverage** (Cov, fraction of source cells on this target) shown inline. With a single pooled source, Purity is high at every level the source matches and Coverage discriminates the target's specificity. The supertype 0219 Sst Gaba_6 [CS20230722_SUPT_0219] is the best target at supertype level but cannot resolve O-O from the other Sst-IN morphological types collapsed into the SSv4 "Sst" pool; see Discussion and pool-candidates.*

### 0219 Sst Gaba_6 [CS20230722_SUPT_0219] · 🔴 LOW

#### Property alignment

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | not asserted | not assessed | NOT_ASSESSED |
| Soma location | CA1 stratum oriens [UBERON:0014552] | Hippocampal formation [MBA:1089] count_100um=1350; Field CA3 [MBA:463] count_100um=1068; Field CA3, pyramidal layer [MBA:495] count_100um=799 | not assessed | APPROXIMATE |
| Sst expression | defining marker | Sst: 10.17 (cohort_pct 0.778; child-coverage 1.000); atlas category DEFINING | not assessed | CONSISTENT |
| Nos1 expression | defining marker | Nos1: 1.81 (cohort_pct 0.508; child-coverage 1.000) | not assessed | CONSISTENT |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

#### Evidence support

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression (Sst) | Atlas metadata | PARTIAL | Sst=10.17, Nos1=1.81 | atlas-internal |
| Atlas precomputed expression (Nos1 cross-check) | Atlas metadata | PARTIAL | Nos1=1.81 modest | atlas-internal |
| MapMyCells AT (Yao 2021 Sst → WMBv1) | Annotation transfer | PARTIAL | F1=0.76 at supertype | atlas-internal |

**Supporting evidence**
- Annotation transfer of the Yao 2021 SSv4 Sst pool onto WMBv1 [run_ref `at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1`] reaches F1=0.76, Coverage=0.63, Purity=0.96 at supertype 0219 Sst Gaba_6, the dominant supertype target for Sst-expressing hippocampal interneurons in this dataset.
- The supertype carries Sst expression at cohort percentile 0.778 (atlas DEFINING category), consistent with Sst as a defining marker of the classical type.
- Nos1 is present (1.81; cohort percentile 0.508), low in absolute terms but non-zero, leaving the Sst+/Nos1+ intersectional pattern at least nominally permitted at supertype-level mean.

**Marker evidence provenance**
- **Sst:** confirmed at transcript level on the atlas supertype (precomputed mean 10.17, cohort percentile 0.778, DEFINING category). The classical-node Sst citation [1] is the same study that defines the type intersectionally with Nos1; the marker assertion rests on Sst::Nos1 transgene targeting in that paper rather than on an independent Sst study.
- **Nos1:** classical-node Nos1 has no primary citation on the node (its role is established by the intersectional definition in [1]). Atlas-side Nos1=1.81 is modest and may reflect a mixture of Nos1-positive and Nos1-negative cells within the supertype — recommend a targeted re-analysis of Sst::Nos1 intersectional or single-cell co-expression data resolved to WMBv1 supertypes.

**Concerns**
- Location alignment is APPROXIMATE with strong CA3 bias on the atlas side (top counts in CA3, CA3 pyramidal layer; `region_fraction_100um: 0.132` for the queried CA1 stratum oriens). The classical definition places the O-O soma in CA1 stratum oriens, so the CA3 enrichment of SUPT_0219 is a substantive mismatch with the queried region. The mapping may still hold if O-O cells exist in CA3 as well, but Chamberland 2024 reports them in CA1.
- The supertype-level AT F1=0.76 derives from a coarse Yao SSv4 "Sst" pool that collapses OLM, bistratified, hippocampo-septal, O-O, P-LM, R-LM, and L-th cells into a single source label; the AT signal cannot identify the O-O subset specifically.
- AMBIGUOUS_MAPPING caveat on the edge: Sst Gaba_6 subclass contains multiple supertypes, and without Nos1 verification at finer resolution it is unclear which (if any) supertype within Sst Gaba subclass captures the O-O population.

**What would upgrade confidence**
- A single-cell dataset with morphologically-confirmed or Sst::Nos1 intersectionally-labeled O-O cells mapped to WMBv1 via MapMyCells at F1 ≥ 0.80 at SUPERTYPE or CLUSTER would resolve the AT pooling problem.
- Per-cell Nos1 co-expression statistics within SUPT_0219 (rather than only the supertype mean) would test whether the supertype contains a Nos1+ subpopulation matching the intersectional definition.

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · ⚪ UNCERTAIN

#### Property alignment

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | not asserted | not assessed | NOT_ASSESSED |
| Soma location | CA1 stratum oriens [UBERON:0014552] | Hippocampal formation [MBA:1089] count_100um=2145; Field CA1 [MBA:382] count_100um=1559; Field CA1, stratum oriens [MBA:399] count_100um=1463 | 0768 Sst Gaba_3: CA1 stratum oriens count_100um=261 | CONSISTENT |
| Sst expression | defining marker | Sst: 11.44 (cohort_pct 0.905; child-coverage 1.000) | 0768: Sst=12.70 (cohort_pct 0.992) | CONSISTENT |
| Nos1 expression | defining marker | Nos1: 2.94 (cohort_pct 0.667; child-coverage 1.000) | 0768: Nos1=0.76 (cohort_pct 0.378) | CONSISTENT (SUPT); APPROXIMATE (CLUS) |

*(Child-cluster breakdown: 0768 Sst Gaba_3 [CS20230722_CLUS_0768] is the supertype's best CA1 stratum oriens child, but its Nos1 (0.76) is lower than the parent supertype mean (2.94), suggesting Nos1+ cells may be concentrated in other child clusters of the supertype or be cell-sparse within children.)*

#### Evidence support

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression | Atlas metadata | PARTIAL | Sst=11.44, Nos1=2.94 | atlas-internal |

**Supporting evidence**
- Location alignment is CONSISTENT: Sst Gaba_3 supertype's top three painted regions are Hippocampal formation, Field CA1, and Field CA1 stratum oriens, the exact location of the O-O soma. `region_fraction_100um: 0.539` for CA1 stratum oriens.
- Sst is high (11.44, cohort percentile 0.905), supporting Sst as a defining marker.
- Nos1 is detectable (2.94, cohort percentile 0.667), the highest among the CA1 stratum oriens Sst supertype candidates in this cohort.

**Marker evidence provenance**
- **Sst:** transcript-level confirmation on the supertype (cohort percentile 0.905). Concordance not nominal.
- **Nos1:** present at modest level on the supertype mean (2.94); the best CA1 SO child cluster (0768 Sst Gaba_3) has lower Nos1 (0.76), so the supertype-level Nos1 signal is not uniformly distributed across children — flag for child-resolved investigation.

**Concerns**
- Although location is CONSISTENT, this supertype is also the canonical OLM mapping target (a separate classical type in this graph). Without Nos1-resolving data, the O-O fraction cannot be separated from the OLM fraction within Sst Gaba_3.
- No AT evidence on this edge: the Yao SSv4 Sst pool's best supertype is SUPT_0219, not SUPT_0216 — meaning the broader Sst-IN population mapped preferentially elsewhere, weakening the case that O-O cells specifically land here.

**What would upgrade confidence**
- Per-child-cluster Nos1 statistics within SUPT_0216 to identify any Nos1-enriched child consistent with the Sst::Nos1 intersectional definition.
- AT from a Sst::Nos1 intersectional dataset (if available) targeted at SUPT_0216 child clusters.

### 0768 Sst Gaba_3 [CS20230722_CLUS_0768] · ⚪ UNCERTAIN

#### Property alignment

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | GABA | CONSISTENT |
| Soma location | CA1 stratum oriens [UBERON:0014552] | (parent SUPT_0216 above) | Hippocampal formation [MBA:1089] count_100um=296; Field CA1 [MBA:382] count_100um=273; Field CA1, stratum oriens [MBA:399] count_100um=261 | CONSISTENT |
| Sst expression | defining marker | (parent above) | Sst: 12.70 (cohort_pct 0.992); atlas category NEUROPEPTIDE | CONSISTENT |
| Nos1 expression | defining marker | (parent above) | Nos1: 0.76 (cohort_pct 0.378) | APPROXIMATE |

*(This cluster sits inside the SUPT_0216 paragraph above as the best CA1 stratum oriens child of the supertype; it is surfaced separately because the curator's cohort scoring placed it at rank 1 on score 6.)*

#### Evidence support

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression | Atlas metadata | PARTIAL | Sst=12.70, Nos1=0.76 | atlas-internal |

**Supporting evidence**
- Strongest individual CA1 stratum oriens location signal in the cohort: `region_fraction_100um: 0.818`, with 261 of 296 painted hippocampal cells in CA1 stratum oriens.
- Sst is at the top of the cohort (cohort percentile 0.992) at val 12.70.

**Marker evidence provenance**
- **Sst:** the atlas category at cluster level is NEUROPEPTIDE rather than DEFINING — Sst is annotated as a neuropeptide on the atlas team's panel for this cluster, which is informational support for presence but does not necessarily designate Sst as a cluster-discriminating marker.
- **Nos1:** very low (0.76, cohort percentile 0.378); the Sst+/Nos1+ intersectional definition of O-O is not met at cluster level on CLUS_0768. If O-O cells are a Nos1-positive subset of this cluster, the cluster-level mean would still be modest if O-O cells are a minority within the cluster.

**Concerns**
- Nos1 is APPROXIMATE: this is the decisive mismatch. The O-O type is defined by the Sst::Nos1 intersection [1], and CLUS_0768 carries weak Nos1.
- No AT support: the AT-best cluster for the Yao Sst pool is 0786 Sst Gaba_6 (F1=0.23 only; Coverage=0.13), and CLUS_0768 is not the AT-best target.

**What would upgrade confidence**
- Single-cell co-expression resolution showing whether a Nos1-positive subset of CLUS_0768 exists and matches the morphological O-O profile would convert this from APPROXIMATE to CONSISTENT.

### Candidates audited (full top-K)

<details>
<summary>Audit table (11 edges)</summary>

| WMBv1 target | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | — | 725 | 🔴 LOW | AT F1=0.76 for Sst pool at supertype | Primary |
| 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — | 2004 | ⚪ UNCERTAIN | CA1 SO location CONSISTENT; Nos1 modest | Secondary |
| 0768 Sst Gaba_3 [CS20230722_CLUS_0768] | 0216 Sst Gaba_3 | 66 | ⚪ UNCERTAIN | Best CA1 SO location; Nos1 APPROXIMATE | Supports broader mapping |
| 0772 Sst Gaba_3 [CS20230722_CLUS_0772] | 0216 Sst Gaba_3 | 190 | 🔴 LOW | CA1 SO CONSISTENT but Nos1 APPROXIMATE | Eliminated (Nos1 weak) |
| 0850 Sst Chodl Gaba_2 [CS20230722_CLUS_0850] | 0239 Sst Chodl Gaba_2 | 407 | 🔴 REFUTED | Sst+Nos1 high but striatum/NAc | Eliminated (wrong region — striatum) |
| 0651 Vip Gaba_7 [CS20230722_CLUS_0651] | 0179 Vip Gaba_7 | 170 | 🔴 REFUTED | Sst APPROXIMATE (val 0.70); wrong subclass | Eliminated (Sst absent; Vip subclass) |
| 0724 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0724] | 0203 Lamp5 Lhx6 Gaba_1 | 2443 | 🔴 REFUTED | Sst APPROXIMATE (val 1.18); Lamp5 subclass | Eliminated (wrong subclass) |
| 0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241] | — | 2905 | 🔴 REFUTED | Sst Chodl, isocortex/forebrain bundle | Eliminated (wrong region — cortex) |
| 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] | — | 8913 | 🔴 REFUTED | Sst CONSISTENT but val 1.52; Lamp5 subclass | Eliminated (wrong subclass) |
| 0226 Sst Gaba_13 [CS20230722_SUPT_0226] | — | 4064 | 🔴 REFUTED | Sst high but isocortex/subplate | Eliminated (wrong region — cortex) |
| 1164 Astro-TE NN_4 [CS20230722_SUPT_1164] | — | 982 | 🔴 REFUTED | Astrocyte supertype | Eliminated (astrocyte; not a neuron) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The oriens-oriens cell was defined in Chamberland et al. 2024 [1] as a CA1 stratum oriens Sst-expressing GABAergic interneuron labelled by Sst::Nos1 intersectional Cre/Flp genetics (n = 12/15 intersectional cells in the source sample), with axon confined to the same stratum oriens layer that hosts the soma — anatomically distinct from OLM cells whose axon projects to stratum lacunosum-moleculare. `definition_basis: CLASSICAL_MULTIMODAL`.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match against MBA:399 Field CA1 stratum oriens, NT type GABAergic, defining markers Sst + Nos1). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Sst) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells (default parameters) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398; Sst source-label cells n=273) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |
| Caveats | Yao 2021 SSv4 "Sst" source label is a subclass-level pool collapsing OLM, bistratified, hippocampo-septal, oriens-oriens, P-LM, R-LM, L-th, and other Sst-IN morphological types into a single label; subtype resolution requires a dataset with morphologically-identified Sst-IN labels. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:37+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA; ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL; PARTIAL | [1] + atlas-internal |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_CLUS_0768 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_CLUS_0772 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_CLUS_0850 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_CLUS_0651 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_CLUS_0724 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0241 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0203 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0226 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_1164 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Oriens-oriens (O-O) cell → 0219 Sst Gaba_6 [CS20230722_SUPT_0219] at LOW confidence. Key support: annotation transfer of the Yao 2021 Sst pool (F1=0.76 at supertype) and atlas precomputed Sst expression at cohort percentile 0.778. Key caveats: OTHER (single-study definition with thin evidence and unresolved CA1-vs-CA3 location mismatch on the atlas supertype) and MARKER_NOT_SPECIFIC (Sst Gaba_6 subclass contains multiple supertypes and Nos1 is not verified as a discriminating feature of SUPT_0219 specifically).

The O-O type is indistinguishable from several other CA1 Sst-IN classical types (bistratified, hippocampo-septal, OLM, P-LM, R-LM, L-th cells) at the AT levels reachable in this run — the Yao 2021 SSv4 "Sst" label pools all of them. Resolving the O-O-specific mapping requires either (a) a single-cell dataset with morphologically-confirmed or Sst::Nos1 intersectionally-labeled O-O cells, or (b) per-cell Nos1 co-expression statistics at WMBv1 cluster resolution to identify a Sst+/Nos1+ subset within a CA1 stratum oriens cluster.

No Cell Ontology term currently assigned. Candidate for CL contribution — the Sst+/Nos1+ CA1 stratum oriens interneuron with axon confined to stratum oriens has no existing CL counterpart distinct from broader Sst+ hippocampal interneuron terms.

### Proposed experiments and follow-ups

- **MapMyCells on a Sst::Nos1-intersectional or morphologically-confirmed O-O dataset.**
  - Target: F1 ≥ 0.80 at CLUSTER level within Sst Gaba_3 or Sst Gaba_6 supertype.
  - Expected output: AnnotationTransferEvidence resolving whether O-O cells land on a specific child cluster (most likely a Nos1-enriched child of 0216 Sst Gaba_3 or 0219 Sst Gaba_6).
  - Resolves: open questions 1, 2, 3.
- **Per-child-cluster Nos1 expression resolution within SUPT_0216 and SUPT_0219.**
  - Target: identify a child cluster with Nos1 ≥ tier 2 within the queried CA1 SO region.
  - Expected output: refined property comparisons + potential 1:1 candidate.
  - Resolves: open questions 1, 3.
- **Targeted literature search for Nos1 heterogeneity within CA1 Sst-IN populations.**
  - Expected output: LiteratureEvidence on whether Nos1 distinguishes a specific Sst-IN morphological type beyond the Sst::Nos1 intersection used by Chamberland 2024.

The existing AT run on Yao 2021 SSv4 partially addresses experiment (1) but cannot resolve O-O specifically because the source label is a subclass-level Sst pool; a refined version using a finer source label (intersectionally-targeted O-O cells, or morphologically-reconstructed Sst-INs) would be required.

### Open questions

1. Does SUPT_0219 express Nos1? If so, at what penetrance?
2. Are the CA3 SO cells in SUPT_0219 analogous to the CA1 O-O cells described by Chamberland 2024?
3. Is there a CA1 SO Sst+/Nos1+ supertype better matching O-O cell identity?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | Sst marker; Sst::Nos1 intersectional definition of O-O cell |

---

<!-- verdict-block-start: edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0219 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:STRONGEST] Annotation transfer of the Yao 2021 hippocampal Sst pool
    (run_ref at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1) lands on
    CS20230722_SUPT_0219 at F1=0.76 at supertype (n=161/273), and Sst is
    present on the supertype (cohort percentile 0.778, atlas DEFINING);
    however the Yao SSv4 Sst label is a coarse subclass pool that does not
    distinguish O-O from OLM, bistratified, hippocampo-septal, P-LM, R-LM
    or L-th cells, so the call cannot identify the O-O subset specifically.
    Atlas-side location is CA3-enriched rather than CA1 stratum oriens
    (region_fraction_100um: 0.132 for the queried region), a substantive
    location mismatch with the Chamberland 2024 CA1 description.
  reconciliation_note: >
    Indistinguishable from bistratified_cell_hippocampus,
    hippocampo_septal_cell_ca1, lth_cell_hippocampus, p_lm_cell_hippocampus
    and r_lm_cell_hippocampus at the AT levels reachable in this run
    (panels: AT only; markers, anat, NT not jointly discriminating at the
    pooled-source resolution). CASE B AT-only indistinguishability; no
    lit_to_lit edge emitted.
  caveats:
    - caveat_type: OTHER
      description: >
        O-O cell evidence is thin — defined in a single intersectional-genetics
        study (Chamberland et al. 2024, PMID:38640347). Atlas-side Nos1=1.81
        is modest and not independently verified as a discriminator of
        CS20230722_SUPT_0219 within the Sst Gaba_6 subclass.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Sst Gaba_6 subclass contains multiple supertypes and the AT signal
        rests on a Yao SSv4 Sst subclass pool that does not separate O-O
        from other Sst-IN classical types.
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        CS20230722_SUPT_0219 painted-region top counts are dominated by
        Field CA3 and CA3 pyramidal layer rather than CA1 stratum oriens;
        region_fraction_100um: 0.132 for the queried region.
  proposed_experiments:
    - >
      MapMyCells on a Sst::Nos1 intersectional or classical-type-confirmed
      O-O single-cell dataset onto WMBv1, target F1 >= 0.80 at CLUSTER level
      within Sst Gaba_3 or Sst Gaba_6, to produce AnnotationTransferEvidence
      resolving O-O-specific placement.
    - >
      Per-child-cluster Nos1 expression resolution within CS20230722_SUPT_0219
      to test whether a Nos1-enriched child consistent with the Sst::Nos1
      intersectional definition exists.
  unresolved_questions:
    - Does CS20230722_SUPT_0219 express Nos1 at penetrance compatible with the Sst::Nos1 intersectional definition of O-O?
    - Are the CA3 stratum oriens cells in CS20230722_SUPT_0219 analogous to the CA1 O-O cells described by Chamberland 2024?
    - Is there a CA1 stratum oriens Sst+/Nos1+ supertype that better matches O-O identity than CS20230722_SUPT_0219?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.30
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:NEXT] CS20230722_SUPT_0216 has the cleanest CA1 stratum oriens
    location among Sst supertype candidates (region_fraction_100um: 0.539,
    top painted regions Field CA1 and CA1 stratum oriens) and high Sst
    (cohort percentile 0.905), but Nos1 is modest at supertype mean (2.94,
    cohort percentile 0.667) and the AT-best supertype for the Yao 2021 Sst
    pool was CS20230722_SUPT_0219 rather than CS20230722_SUPT_0216, so
    direct AT support for placement here is absent. SUPT_0216 is also the
    canonical OLM mapping target and cannot be separated from OLM without
    Nos1-resolving data.
  reconciliation_note: >
    Predicate uncertain between closeMatch and broadMatch; depends on
    whether a Nos1-enriched child cluster of SUPT_0216 exists. Without
    AT or per-cell Nos1 resolution, the call cannot separate O-O from
    OLM within Sst Gaba_3 subclass.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Nos1 is present at modest supertype-mean expression (2.94) but the
        best CA1 SO child cluster CS20230722_CLUS_0768 carries lower Nos1
        (0.76), suggesting Nos1-positive cells are not uniformly distributed
        across children of CS20230722_SUPT_0216.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        CS20230722_SUPT_0216 is the canonical mapping target for OLM cells
        and cannot be separated from O-O cells without Nos1-resolving
        single-cell data.
  proposed_experiments:
    - >
      Per-child-cluster Nos1 expression resolution within CS20230722_SUPT_0216
      to identify any Nos1-enriched child consistent with the Sst::Nos1
      intersectional definition.
  unresolved_questions:
    - Does any child cluster of CS20230722_SUPT_0216 carry Nos1 expression compatible with the Sst::Nos1 intersectional definition of O-O?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_oriens_oriens_cell_hippocampus_to_CS20230722_CLUS_0768 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.28
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:WEAKEST] CS20230722_CLUS_0768 has the strongest individual CA1
    stratum oriens location signal in the cohort (region_fraction_100um:
    0.818) and very high Sst (12.70, cohort percentile 0.992), but Nos1 is
    weak (0.76, cohort percentile 0.378) and APPROXIMATE rather than
    CONSISTENT — the Sst::Nos1 intersectional definition of O-O is not met
    at cluster-mean level. The cluster is the AT-best CA1 SO child of
    CS20230722_SUPT_0216 but no AT evidence directly supports placement
    here for the O-O label specifically.
  reconciliation_note: >
    Surfaced separately from the parent CS20230722_SUPT_0216 paragraph;
    treat as the CA1 stratum oriens reference cluster for testing whether
    a Sst+/Nos1+ subset exists within the SUPT_0216 supertype.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Nos1 is weak at cluster level (0.76, cohort percentile 0.378);
        Sst::Nos1 intersectional cells from Chamberland 2024 may be a
        minority within CS20230722_CLUS_0768, depressing the cluster-mean
        Nos1 signal.
  proposed_experiments:
    - >
      Per-cell Nos1 co-expression statistics within CS20230722_CLUS_0768
      to test whether a Nos1-positive subset matching the classical O-O
      profile exists.
  unresolved_questions:
    - Does CS20230722_CLUS_0768 contain a Sst+/Nos1+ subset matching the classical O-O profile, or are O-O cells concentrated in a different child cluster of CS20230722_SUPT_0216?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_oriens_oriens_cell_hippocampus_to_CS20230722_CLUS_0772 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.20
  rationale: >
    [tier:CUT] CS20230722_CLUS_0772 has CONSISTENT CA1 stratum oriens
    location (region_fraction_100um: 0.706) and high Sst (11.92, cohort
    percentile 0.958), but Nos1 is APPROXIMATE (1.09, cohort percentile
    0.454), and no AT or literature evidence specifically supports placement
    of the O-O type on this cluster over its supertype siblings.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_oriens_oriens_cell_hippocampus_to_CS20230722_CLUS_0850 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0850 satisfies the Sst+/Nos1+ marker pair
    strongly (Sst=12.23, Nos1=12.14) but its painted regions are Striatum,
    Nucleus accumbens and Caudoputamen with region_fraction_100um: 0.030
    for the queried CA1 stratum oriens — the cluster sits in a distant
    non-hippocampal region inconsistent with the O-O type's CA1 location.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_oriens_oriens_cell_hippocampus_to_CS20230722_CLUS_0651 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0651 is a Vip Gaba_7 cluster with Sst
    APPROXIMATE at val 0.70 (cohort percentile 0.269); the wrong subclass
    for a Sst-defined classical type, and the high Nos1 (9.01) does not
    rescue subclass mismatch.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_oriens_oriens_cell_hippocampus_to_CS20230722_CLUS_0724 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0724 is a Lamp5 Lhx6 Gaba_1 cluster with
    Sst APPROXIMATE at val 1.18 (cohort percentile 0.479); wrong subclass
    for a Sst-defined classical type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0241 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0241 is a Sst Chodl Gaba_4 supertype with
    Sst=12.33 and Nos1=11.26 but painted regions Isocortex, lateral
    forebrain bundle system and corpus callosum; region_fraction_100um:
    0.021 for CA1 stratum oriens — distant cortical/white-matter location
    incompatible with O-O identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0203 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0203 is a Lamp5 Lhx6 Gaba_1 supertype with
    Sst=1.52 (cohort percentile 0.603) and high Nos1; wrong subclass for a
    Sst-defined classical type, and location is APPROXIMATE
    (region_fraction_100um: 0.114) with hippocampal cells biased to
    Dentate gyrus and CA3 rather than CA1 stratum oriens.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0226 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0226 is a Sst Gaba_13 supertype with high
    Sst (12.08) and modest Nos1 (1.92) but painted regions Isocortex and
    Cortical subplate; region_fraction_100um: 0.016 for CA1 stratum oriens —
    distant cortical location incompatible with O-O identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_1164 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.02
  rationale: >
    [tier:CUT] CS20230722_SUPT_1164 is an astrocyte supertype (Astro-TE
    NN_4), not a GABAergic neuron — incompatible cell class for the O-O
    type regardless of region or marker signal.
```
<!-- verdict-block-end -->
