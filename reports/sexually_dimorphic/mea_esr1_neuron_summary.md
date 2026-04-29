# Medial amygdala estrogen-receptor alpha neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

**Medial amygdala estrogen-receptor alpha neuron** is a **CANDIDATE classical-node
stub** proposed on the back of bulk-correlation evidence from Knoedler 2022
(PMID:35143761) [1]. The sexually dimorphic Esr1+ population of the medial
amygdalar nucleus is well-described in the classical literature as a key node of
the male-typical reproductive behaviour circuit (mating, aggression), but this
classical type was not included in the original sexually-dimorphic
asta-report-ingest cycle. It is recorded here so that the bulk-correlation
evidence can land as an edge. Full classical literature ingest (e.g. Choi 2005,
Unger 2015, Yamaguchi 2020) is **pending** — until that ingest is complete the
single mapping edge is held at LOW confidence, reflecting single-dataset support.

| Property | Value | References |
|---|---|---|
| Soma location | Medial amygdalar nucleus [MBA:403] | — |
| Defining markers | Esr1 (transcript / receptor) | — |

*(Stub status: NT type, neuropeptides, negative markers, CL term, and per-marker
literature citations are not yet populated. They will be filled in by the
pending classical literature ingest.)*

---

## 4. Mapping candidates

### 4a. Candidate overview

A single mapping edge is recorded for mea_esr1_neuron: a supertype-level edge to
SUPT_0055 (0055 MEA Slc17a7 Glut_1) at LOW confidence. The edge is supported by
a single piece of evidence — the Knoedler 2022 Esr1+ TRAP-seq bulk correlation [1]
— and by node-level metadata alignment. LOW confidence reflects the
single-dataset support and the stub status of the classical node.

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0055 MEA Slc17a7 Glut_1 [CS20230722_SUPT_0055] | (self) | not assessed | 🔴 LOW | Location CONSISTENT; NT CONSISTENT; Esr1 CONSISTENT; sex ratio CONSISTENT (CLUS_0197 MFR=10.11) | Speculative |

1 edge total. Relationship type: PARTIAL_OVERLAP.

### 4b. Property alignment — primary candidate (SUPT_0055)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Medial amygdalar nucleus [MBA:403] | Medial amygdalar nucleus (primary soma across child clusters) | not assessed (best child cluster CLUS_0197 lies within MEA-Slc17a7 Glut_1 supertype) | CONSISTENT |
| NT type | Glutamatergic (MeA principal neurons predominantly glutamatergic) | Glutamatergic (Slc17a7 Glut_1) | not assessed | CONSISTENT |
| Esr1 expression | POSITIVE (primary defining marker) | Esr1+ by experimental design (TRAP-Cre line) | not assessed | CONSISTENT |
| Sex ratio | male-biased (MeA Esr1+ population larger in males) | not available at supertype level | MFR=10.11 (CLUS_0197) — extreme male bias | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Knoedler 2022 Esr1+ TRAP-seq MeA-FR vs VMH-FR | Bulk transcriptomic correlation | SUPPORT | δ=0.0519 (rank 3/5322; highest absolute δ in entire run); CLUS_0197 MFR=10.11 | [1] |

> Knoedler 2022 (PMID:35143761) Esr1+ TRAP-seq pooled MeA female-receptive vs VMH female-receptive identifies SUPT_0055 (MEA Slc17a7 Glut_1) as the dominant MeA-specific signal. Child cluster CLUS_0197 ranks #3 of 5,322 by δ = ρ(MeA_FR) − ρ(VMH_FR), with δ=0.0519 (the highest absolute δ value in the entire run) and MFR=10.11 (strongly male-biased — consistent with the well-known sexually dimorphic male-typical MeA Esr1+ population). Multiple sister clusters from SUPT_0055 (CLUS_0194, CLUS_0198) and the related SUPT_0057 also rank in the top 6. Anatomically clean signal. Confidence held at LOW because mea_esr1_neuron is a candidate classical node — full literature ingest has not yet been performed.
> — Knoedler et al. 2022 · [1]

*(Child-cluster breakdown not assessed — see proposed experiments. Knoedler 2022
[1] reports CLUS_0197 (rank 3, δ=0.0519, MFR=10.11), CLUS_0194 (rank 6, δ=0.0508,
MFR=2.70), and CLUS_0198 (rank 4, δ=0.0515) as the top SUPT_0055 child-cluster
hits, with sister supertype SUPT_0057 also placing in the top 6.)*

---

## 5. Candidate paragraphs

## 0055 MEA Slc17a7 Glut_1 [CS20230722_SUPT_0055] · 🔴 LOW

### Supporting evidence

- **Anatomical concordance.** SUPT_0055 (MEA Slc17a7 Glut_1) has primary soma in
  Medial amygdalar nucleus across child clusters, directly matching the classical
  soma location MBA:403 (Medial amygdalar nucleus).
- **NT type concordance.** The supertype label encodes Slc17a7-positive
  glutamatergic identity, consistent with the predominantly glutamatergic
  identity of MeA principal neurons.
- **Esr1 marker concordance by experimental design.** The Knoedler 2022 [1]
  source dataset is by construction Esr1+ (TRAP-Cre line), and the supertype is
  identified as the dominant MeA-specific signal in that pool, confirming Esr1
  expression at the population the supertype represents.
- **Sex ratio concordance at child-cluster level.** CLUS_0197 (a child cluster
  of SUPT_0055) shows MFR=10.11 — extreme male bias — directly matching the
  well-known male-biased sexually dimorphic MeA Esr1+ population.
- **Bulk-correlation evidence is anatomically clean and rank-leading [1].**
  > Knoedler 2022 (PMID:35143761) Esr1+ TRAP-seq pooled MeA female-receptive vs VMH female-receptive identifies SUPT_0055 (MEA Slc17a7 Glut_1) as the dominant MeA-specific signal. Child cluster CLUS_0197 ranks #3 of 5,322 by δ = ρ(MeA_FR) − ρ(VMH_FR), with δ=0.0519 (the highest absolute δ value in the entire run) and MFR=10.11 (strongly male-biased — consistent with the well-known sexually dimorphic male-typical MeA Esr1+ population). Multiple sister clusters from SUPT_0055 (CLUS_0194, CLUS_0198) and the related SUPT_0057 also rank in the top 6. Anatomically clean signal. Confidence held at LOW because mea_esr1_neuron is a candidate classical node — full literature ingest has not yet been performed.
  > — Knoedler et al. 2022 · [1]

### Marker evidence provenance

- **Esr1** — listed as the primary defining marker on the classical stub but
  with no per-marker literature citation populated yet (the stub awaits classical
  literature ingest). Source-side evidence is by experimental design (TRAP-Cre on
  Esr1) [1]; target-side per-cluster Esr1 expression has not been pulled into
  this edge as a quantitative comparison. *(note: the classical stub's Esr1
  attribution will be cite-supported once asta-report-ingest or cite-traverse is
  run on Choi 2005, Unger 2015, Yamaguchi 2020 — see Proposed experiments.)*

### Concerns

- **Single-dataset support.** All supporting evidence on this edge is from
  Knoedler 2022 [1]. There is no independent literature replication, no
  annotation transfer, and no atlas-metadata cross-check yet recorded.
- **Classical node is a stub (PRIOR_MAPPING_ASSUMED caveat).** mea_esr1_neuron
  was not part of the original asta-report-ingest cycle. The biological
  identity of the population is well-established in the classical literature,
  but no curated literature has yet been ingested to support the per-marker /
  per-property assertions on this node. Confidence is therefore capped at LOW
  until ingest is complete.
- **Internal heterogeneity not yet resolved.** CLUS_0197 (MFR=10.11) and
  CLUS_0194 (MFR=2.70) within SUPT_0055 differ substantially in male bias,
  raising the open question of whether they represent functionally distinct
  male-biased subpopulations (e.g. aggression-active vs neutral) or a graded
  signal across one population.

### What would upgrade confidence

- **Run asta-report-ingest or cite-traverse on MeA Esr1+ classical literature**
  (Choi 2005 PMID:16267094, Unger 2015 PMID:26119027, Yamaguchi 2020 PMID:31831664)
  to upgrade mea_esr1_neuron from stub to fully ingested classical node, populating
  per-marker, NT, and neuropeptide citations. Expected output: additional
  `LiteratureEvidence` items and a populated classical-node property set.
- **MapMyCells annotation transfer** of published MeA Esr1+ scRNA-seq data to
  WMBv1, providing direct cell-level AT evidence alongside the existing bulk
  correlation. Target: F1 ≥ 0.50 at SUPT_0055 level. Expected output:
  `AnnotationTransferEvidence`.
- **Independent bulk-correlation replication** using a second Esr1+ MeA pool
  (different lab / different sex-behavioural contrast) to confirm the rank-3 /
  δ=0.0519 placement of SUPT_0055/CLUS_0197 is not dataset-specific. Expected
  output: an additional `BulkCorrelationEvidence` entry.

---

## 6. Proposed experiments

### 1. Classical literature ingest for mea_esr1_neuron

**What:** Run asta-report-ingest or cite-traverse on the canonical MeA Esr1+
literature (Choi 2005 PMID:16267094, Unger 2015 PMID:26119027, Yamaguchi 2020
PMID:31831664) to convert the stub to a fully ingested classical node with
per-marker citations, NT-type citation, and neuropeptide list.

**Target:** Populated `defining_markers[*].refs`, `nt`/`nt_refs`, `neuropeptides`,
and `location_refs` on the mea_esr1_neuron node.

**Expected output:** `LiteratureEvidence` items on the edge; populated
classical-node property set.

**Resolves:** Open question 1; lifts the LOW-confidence ceiling imposed by
PRIOR_MAPPING_ASSUMED.

### 2. MapMyCells annotation transfer of published MeA Esr1+ scRNA-seq against WMBv1

**What:** Retrieve a published MeA Esr1+ scRNA-seq dataset (e.g. Esr1-Cre or
Esr1-TRAP sorted preparations) and run MapMyCells against WMBv1 at supertype
and cluster resolution.

**Target:** F1 ≥ 0.50 at SUPT_0055 level; child-cluster F1 distribution
to test whether CLUS_0197 vs CLUS_0194 are functionally separable.

**Expected output:** `AnnotationTransferEvidence` on this edge. Atlas: WMBv1.
Tool: MapMyCells. Output format: F1 matrix per cluster.

**Resolves:** Open question 2; addresses the AT NOT_ASSESSED gap.

### 3. Independent bulk-correlation replication

**What:** Repeat the δ = ρ(MeA_FR) − ρ(VMH_FR) (or analogous MeA-vs-VMH
contrast) computation against WMBv1 using a second Esr1+ MeA pool from an
independent dataset.

**Target:** SUPT_0055 / CLUS_0197 retains a top-3 ranking of 5,322 clusters
by δ.

**Expected output:** An additional `BulkCorrelationEvidence` entry on the edge.

**Resolves:** Robustness check on the primary external evidence [1].

---

## 7. Open questions

1. Does the existing classical literature support a single MeA Esr1+ classical
   type, or multiple subpopulations (e.g. male-typical aggression vs neutral)?
2. Are CLUS_0197 (MFR=10.11) and CLUS_0194 (MFR=2.70) functionally distinct
   male-biased subpopulations of SUPT_0055, or a graded signal across one
   population?

---

## 8. Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_mea_esr1_neuron_to_cs20230722_supt_0055 | BULK_CORRELATION ([1] Knoedler 2022) | SUPPORT — δ=0.0519 (rank 3/5322; highest absolute δ in run); CLUS_0197 MFR=10.11; SUPT_0055 identified as dominant MeA-specific signal |

---

## 9. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Knoedler et al. 2022 | [PMID:35143761](https://pubmed.ncbi.nlm.nih.gov/35143761/) | Esr1+ TRAP-seq pooled MeA female-receptive vs VMH female-receptive bulk correlation against WMBv1 — ranks SUPT_0055 / CLUS_0197 in top 6 of 5,322 by δ |
