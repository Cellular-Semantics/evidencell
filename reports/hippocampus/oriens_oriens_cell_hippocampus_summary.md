# Oriens-oriens (O-O) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The oriens-oriens (O-O) cell is a recently described GABAergic interneuron of
the hippocampal CA1 stratum oriens, identified by Chamberland et al. 2024
[1] using a Sst;;Nos1 intersectional Cre/Flp genetic strategy. The defining
feature is co-expression of *Sst* and *Nos1* with an axonal arbor confined to
stratum oriens — distinguishing O-O cells from the more widely characterised
OLM (oriens lacunosum-moleculare) cell, whose axon targets stratum
lacunosum-moleculare. The classical description rests on a single primary
study (n = 12/15 Sst;;Nos1-INs in CA1 stratum oriens [1]), and mapping this
nascent type to the WMBv1 mouse-brain transcriptomic taxonomy is a test of
whether the population is resolvable at current atlas resolution.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | — |
| NT | GABAergic | — |
| Markers | Sst, Nos1 | Sst: [1]; Nos1: — |
| Definition basis | CLASSICAL_MULTIMODAL (Sst;;Nos1 intersectional Cre/Flp + axonal-arbor reconstruction) | [1] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Markers — Sst:** classical marker citation · [1]

No verbatim quotes were captured in the facts file for the Sst marker
assertion; no per-source evidence exists for Nos1, soma location, or NT
type on the classical node.
</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

A single supertype-level candidate atlas cluster was assessed for the
oriens-oriens cell; the resulting mapping is UNCERTAIN (eliminated), with the
best available WMBv1 supertype (0219 Sst Gaba_6 [CS20230722_SUPT_0219]) showing
Sst concordance but weak Nos1 expression and CA3-rather-than-CA1 enrichment.

![Filtered AT figure for Oriens-oriens (O-O) cell](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_oriens_oriens_cell_hippocampus.png)

*F1 across taxonomy levels for the 1 source group (Yao 2021 SSv4 "Sst"
subclass) relevant to the oriens-oriens cell. Each panel row is a
source-cell group; nodes are coloured by F1 with precision (P) and recall
(R) shown inline. F1 ≥ 0.5 at a level indicates a clean mapping at that
resolution.*

The Yao 2021 "Sst" SSv4 label maps cleanly at SUBCLASS level (053 Sst Gaba,
F1 = 0.983) and resolves to 0219 Sst Gaba_6 [CS20230722_SUPT_0219] at
SUPERTYPE level (F1 = 0.759), but the source label aggregates multiple Sst
interneuron types so this is not O-O-specific.

### Mapping candidates table

| Rank | WMBv1 supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---:|:---:|---|---|
| — | 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | 1495 | ⚪ UNCERTAIN | Sst CONSISTENT · Nos1 APPROXIMATE · location APPROXIMATE | Eliminated |

Total: 1 edge (UNCERTAIN). All candidates eliminated; see *Eliminated
candidates* below.

### Null result headline

The single supertype-level candidate scanned (0219 Sst Gaba_6
[CS20230722_SUPT_0219]) confirms Sst expression (precomputed stats mean
10.17) but Nos1 expression is weak (mean 1.81), and the supertype is
CA3-enriched (305 cells in field CA3 stratum oriens [MBA:486]) rather than
the CA1 stratum oriens where O-O cells are defined [1]. No CA1 stratum
oriens Sst+/Nos1+ supertype emerged from this assessment.

---

## Eliminated candidates

Shared disqualifying signal: across the assessed Sst Gaba supertypes, none
shows co-expression of *Sst* and *Nos1* combined with CA1 stratum oriens
enrichment as required by the Chamberland 2024 intersectional definition [1].

### 0219 Sst Gaba_6 [CS20230722_SUPT_0219] · ⚪ UNCERTAIN

*1495 cells (10x).*

**Disqualifying evidence:**

- *Nos1 expression weak.* SUPT_0219 precomputed-stats mean for Nos1 = 1.81
  versus Sst = 10.17. O-O cells are defined by Sst+Nos1 co-expression via
  intersectional genetics [1]; weak Nos1 at supertype level argues SUPT_0219
  is not predominantly composed of O-O cells.
- *CA3 rather than CA1 enrichment.* SUPT_0219 anatomical distribution is
  CA3-enriched (305 cells in field CA3 stratum oriens [MBA:486], plus SR 167,
  SP 261, lucidum 99). O-O cells are described in CA1 stratum oriens
  [UBERON:0014552] [1]. *(note: CA3 and CA1 are adjacent hippocampal
  subfields, so this is a moderate — not extreme — anatomical mismatch, but
  it nonetheless places the bulk of SUPT_0219 outside the defined O-O
  location.)*
- *Atlas defining markers (Id3, Adamtsl1, Sp9) have no correspondence in the
  O-O classical literature.* These are NOT_ASSESSED at the classical-node
  side (none listed on the O-O classical node) and so cannot be confirmed
  or refuted from existing evidence.
- *Annotation-transfer evidence is not O-O-specific.* The dominant target
  of the Yao 2021 SSv4 "Sst" subclass at SUPERTYPE level is SUPT_0219
  (F1 = 0.759, 161/273 cells, target_purity = 0.964), but the source label
  aggregates OLM, bistratified, hippocampo-septal, oriens-oriens and other
  Sst interneurons; the mapping is supportive of "SUPT_0219 is a Sst-IN
  supertype" but not of "SUPT_0219 is the O-O supertype".

**Marker evidence provenance:**

- **Sst (defining).** Cited from Chamberland 2024 [1] in the context of a
  Sst;;Nos1 intersectional Cre/Flp targeting morphologically reconstructed
  O-O cells (n = 12/15 in CA1 stratum oriens). Cell-type specificity for
  this study is strong — the cited paper *is* the type definition. Atlas
  cross-check confirms Sst at SUPT_0219 (mean 10.17), CONSISTENT.
- **Nos1 (defining).** Listed without a primary citation on the classical
  node. The intersectional Sst;;Nos1 logic in Chamberland 2024 [1] is the
  implicit source, but no quote_key was captured for Nos1 specifically. A
  targeted cite-traverse to confirm Nos1 protein/transcript evidence in
  morphologically identified O-O cells would strengthen the classical
  description. Atlas cross-check: Nos1 = 1.81 at SUPT_0219 — well below the
  *Sst* defining-marker signal. *Nos1* is not listed as a defining marker
  of SUPT_0219 in atlas metadata, so no atlas-annotation/expression
  discrepancy is formally flagged, but the low atlas mean is itself a
  concern for the O-O assignment.
- *No negative markers or neuropeptides are listed on the classical node;
  none assessed.*

**Concerns:**

- Single-study evidence base — the classical type rests on Chamberland et al.
  2024 [1] alone (caveat type: OTHER).
- *Sst Gaba_6 subclass contains multiple supertypes; without Nos1
  verification at the atlas level, the correct (if any) Sst Gaba_6
  supertype for the O-O cell cannot be determined (caveat type:
  MARKER_NOT_SPECIFIC).*
- Location APPROXIMATE: CA3 stratum oriens [MBA:486] is *(note: an
  adjacent hippocampal subfield to CA1, so this is a registration-boundary
  / proximal-region mismatch rather than a distant-region mismatch — weak-
  to-moderate counter-evidence on its own, but combined with weak Nos1 it
  is sufficient to leave the mapping UNCERTAIN.)*
- Nos1 APPROXIMATE: low mean expression (1.81) does not exclude penetrant
  expression in a sparse subset — the atlas mean alone cannot resolve this.

**What would upgrade confidence:**

1. **Per-cluster Nos1 expression breakdown for child clusters of SUPT_0219.**
   Method: query precomputed expression at cluster (rank 0) level across
   all SUPT_0219 children for *Nos1*. Expected output: ATLAS_METADATA /
   MarkerAnalysisEvidence; threshold: at least one child cluster with
   Nos1 mean ≥ 5 *and* CA1 stratum oriens MERFISH enrichment would be
   a strong O-O candidate. Resolves: unresolved question 1 ("Does
   SUPT_0219 express Nos1? If so, at what penetrance?").
2. **Locate any CA1 SO Sst+/Nos1+ supertype.** Method: cluster-level scan
   across child supertypes of the Sst Gaba subclass (053 Sst Gaba) for
   combined Sst+Nos1 co-expression and CA1 stratum oriens MERFISH
   enrichment. Resolves: unresolved question 3 ("Is there a CA1 SO
   Sst+/Nos1+ supertype better matching O-O cell identity?").
3. **CA3 vs CA1 SO comparison of Sst+/Nos1+ cells.** Method: targeted
   re-analysis or new patch-seq on CA3 stratum oriens Sst;;Nos1 cells to
   ask whether they are transcriptomically equivalent to the CA1 O-O
   population (resolves unresolved question 2).
4. **Higher-resolution annotation transfer with morphologically identified
   Sst-IN labels.** The Yao 2021 SSv4 "Sst" label is a heterogeneous
   subclass-level aggregate. Target: F1 ≥ 0.80 at SUPERTYPE for an O-O-
   specific source label. Expected output: AnnotationTransferEvidence.
   Resolves: AT-side support for O-O ↔ SUPT_0219 (or alternative) at
   cell-type-specific resolution.
5. **Primary-source verification of *Nos1* as an O-O defining marker.**
   Targeted cite-traverse for Nos1 protein/transcript in morphologically
   confirmed CA1 SO Sst+ interneurons — addresses the weak provenance
   noted above.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The oriens-oriens cell is defined by
co-expression of *Sst* and *Nos1* in CA1 stratum oriens [UBERON:0014552]
with axonal arbor confined to stratum oriens, established by Sst;;Nos1
intersectional Cre/Flp genetics in Chamberland et al. 2024 (n = 12/15
intersectional cells) [1]. `definition_basis: CLASSICAL_MULTIMODAL` — the
classical node combines genetic-intersection markers with morphological
axon-target criteria.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the
WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using
metadata-based scoring (region match, NT type, defining markers, sex bias
when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was
compared to the corresponding atlas-side value via the
`property_comparisons` schema, with alignments graded CONSISTENT /
APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came
from precomputed expression on the cluster (cluster.yaml in the taxonomy
reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 (GSE185862) mouse hippocampal formation SMART-Seq v4 cell type labels) |
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

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs,
and verbatim literature quotes in this report are validated against the
evidencell knowledge base at write time. Authored-prose evidence narratives
are validated against their source `evidence_items[*].explanation` fields.
The pre-write hook rejects any unresolvable identifier or unattributed
blockquote. Specific mapping limitations and caveats are documented
per-candidate in the Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:16+00:00 from
[kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER | PARTIAL ×3 | atlas-internal; [1] (classical-side marker) |

</details>

---

## Discussion

**Primary mapping:** Oriens-oriens (O-O) cell → 0219 Sst Gaba_6
[CS20230722_SUPT_0219] at UNCERTAIN confidence (eliminated). Key support:
Sst CONSISTENT (atlas precomputed stats mean 10.17) and dominant target of
the Yao 2021 SSv4 "Sst" subclass at SUPERTYPE level (F1 = 0.759). Key
caveats: weak Nos1 at the atlas supertype (mean 1.81) and CA3-rather-than-
CA1 enrichment; the underlying classical evidence is also thin (single
primary study).

No Cell Ontology term currently assigned. The O-O cell is a candidate for
a new CL term (Sst+/Nos1+ GABAergic interneuron of CA1 stratum oriens with
axon confined to stratum oriens).

### Proposed experiments and follow-ups

*Cross-check against existing evidence:* an ANNOTATION_TRANSFER evidence
item already exists on this edge (Yao 2021 GSE185862 SSv4 → WMBv1,
SUPERTYPE F1 = 0.759 at SUPT_0219). That run resolves the *Sst-subclass-
level* mapping but does NOT resolve O-O specificity, because the Yao 2021
SSv4 "Sst" label aggregates OLM, bistratified, hippocampo-septal, oriens-
oriens and others. A refined AT run with O-O-specific source labels (e.g.
a morphology-confirmed Sst;;Nos1 patch-seq or single-nucleus dataset that
labels O-O cells distinctly) is therefore still needed.

Remaining experiments by method:

- **Atlas precomputed-expression query (rank 0).**
  - *Target:* per-cluster Nos1 expression for all SUPT_0219 child clusters;
    flag any child with Nos1 mean ≥ 5 *and* CA1 stratum oriens MERFISH
    enrichment.
  - *Expected output:* ATLAS_METADATA / MarkerAnalysisEvidence on the
    candidate child cluster(s).
  - *Resolves:* unresolved questions 1, 2, 3.

- **Higher-resolution annotation transfer (refined AT).**
  - *Target:* F1 ≥ 0.80 at SUPERTYPE for an O-O-specific source label
    (e.g. patch-seq with morphology-confirmed O-O calls).
  - *Expected output:* AnnotationTransferEvidence with a non-aggregated
    source_cluster_label.
  - *Resolves:* whether SUPT_0219 (or an alternative Sst Gaba subclass
    child supertype) is the O-O correspondent at cell-type resolution.

- **Targeted cite-traverse / literature search.**
  - *Target:* primary-source citations for *Nos1* as an O-O-defining
    transcript/protein, and any CA3 vs CA1 SO Sst;;Nos1 comparative
    data.
  - *Expected output:* LITERATURE evidence (with quotes captured for
    `facts.quotes`) on the classical node.
  - *Resolves:* weak marker provenance for Nos1 (Methods → Marker
    evidence provenance); informs unresolved question 2.

### Open questions

1. Does SUPT_0219 express *Nos1*? If so, at what penetrance?
2. Are the CA3 stratum oriens cells in SUPT_0219 analogous to the CA1
   O-O cells described by Chamberland 2024 [1]?
3. Is there a CA1 stratum oriens Sst+/Nos1+ supertype better matching
   O-O cell identity than SUPT_0219?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | Sst marker; O-O classical type definition (Sst;;Nos1 intersectional Cre/Flp identification) |
