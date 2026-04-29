# VMHvl estrogen-receptor alpha / progesterone receptor neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

**VMHvl estrogen-receptor alpha / progesterone receptor neuron** is a molecularly heterogeneous
population of glutamatergic neurons in the ventrolateral subdivision of the ventromedial
hypothalamus, defined by neurochemical criteria including ERα (Esr1), progesterone receptor
(Pgr), Nkx2-1, and Tac1 expression. Multiple defined subpopulations have been reported: a Pgr+
subset required for mating in both sexes and fighting in males; an ERα+/Nkx2-1+/Tac1+ subset
that drives female-specific locomotion; and additional ERα-expressing subtypes with different
projections and sex-related functions. Single-nucleus RNA-seq has identified 17 transcriptomic
types within this anatomical population (Kim 2019), and the classical node is acknowledged as
heterogeneous and a candidate for splitting into multiple sub-nodes in future iterations.

No CL term — candidate for new term(s).

| Property | Value | References |
|---|---|---|
| Soma location | Ventromedial hypothalamic nucleus [MBA:693] (ventrolateral subdivision, VMHvl) | [1] |
| Defining markers | Esr1, Nkx2-1, Tac1 (transcript) [1]; Pgr (transcript) [2] | [1], [2] |
| Neuropeptides | Tac1 | [1] |
| CL term | — (none assigned; candidate for new term) | |

<details>
<summary>Details — source evidence for classical type properties</summary>

**[1] Correa et al. 2015 · PMID:25543145 — Developmental and Hormonal Regulation**

> Estrogen-receptor alpha (ERα) neurons in the ventrolateral region of the ventromedial hypothalamus (VMHVL) control an array of sex-specific responses to maximize reproductive success. In females, these VMHVL neurons are believed to coordinate metabolism and reproduction. However, it remains unknown whether specific neuronal populations control distinct components of this physiological repertoire. Here, we identify a subset of ERα VMHVL neurons that promotes hormone-dependent female locomotion. Activating Nkx2-1-expressing VMHVL neurons via pharmacogenetics elicits a female-specific burst of spontaneous movement, which requires ERα and Tac1 signaling. Disrupting the development of Nkx2-1(+) VMHVL neurons results in female-specific obesity, inactivity, and loss of VMHVL neurons coexpressing ERα and Tac1. Unexpectedly, two responses controlled by ERα(+) neurons, fertility and brown adipose tissue thermogenesis, are unaffected. We conclude that a dedicated subset of VMHVL neurons marked by ERα, NKX2-1, and Tac1 regulates estrogen-dependent fluctuations in physical activity and constitutes one of several neuroendocrine modules that drive sex-specific responses.
> — Correa et al. 2015, Developmental and Hormonal Regulation · [1] <!-- quote_key: 27794167_af52b501 -->

**[2] Zilkha et al. 2021 · PMID:33910083 — Sexually Dimorphic Brain Regions and Structures**

> Another molecularly defined sexually dimorphic VMHvl subpopulation that controls sex-typical behaviors in both sexes is the progesterone receptor (PR)-expressing neurons. This subpopulation is required for the normal display of mating in both sexes and for fighting in males [76].
> — Zilkha et al. 2021, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 233446934_8cb6b0bc -->

</details>

---

## 4. Mapping candidates

### 4a. Candidate overview

Two co-primary mapping edges are recorded for vmhvl_esr1_pr_neuron, both at supertype
resolution and both classified `CROSS_CUTTING` because the classical node is a heterogeneous
population that maps onto distinct VMH Fezf1 Glut transcriptomic supertypes. SUPT_0564
captures the broader Pgr+/Nkx2-1+/Tac1+ VMH ERα subpopulation; SUPT_0563 captures the
female-biased lordosis-circuit subpopulation. Both should be retained until the classical
node is split.

| Rank | WMBv1 cluster | Supertype | Cells (MERFISH) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0564 VMH Fezf1 Glut_2 [CS20230722_SUPT_0564] | (self) | n=360 (MBA:693 VMH) | 🟡 MODERATE | Nkx2-1 CONSISTENT; Pgr APPROXIMATE; Esr1 APPROXIMATE; loc CONSISTENT | Best candidate (broad Pgr+ subpopulation) |
| 1 | 0563 VMH Fezf1 Glut_1 [CS20230722_SUPT_0563] | (self) | not assessed | 🟡 MODERATE | Sex ratio CONSISTENT (child clusters MFR=0.08, 0.12); loc CONSISTENT | Best candidate (female-biased lordosis subpopulation) |

2 edges total. Relationship type: CROSS_CUTTING (both edges, co-primary).

### 4b. Property alignment — primary candidate (SUPT_0564)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Ventromedial hypothalamic nucleus [MBA:693] (VMHvl) | MBA:693 (VMH) n=360 (dominant location) | not assessed | CONSISTENT |
| NT type | not stated; VMHvl neurons predominantly glutamatergic | Glutamatergic (VMH Fezf1 Glut label) | not assessed | CONSISTENT |
| Nkx2-1 expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=5.34 | not assessed | CONSISTENT |
| Pgr expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=4.54 | not assessed | APPROXIMATE |
| Esr1 expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=2.35 | not assessed | APPROXIMATE |
| Tac1 expression | POSITIVE (transcript, defining marker and neuropeptide) | precomputed mean_expression=1.39 | not assessed | APPROXIMATE |
| Sex ratio | not documented at this level | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| SUPT_0564 atlas precomputed expression + MBA:693 location | Atlas metadata | PARTIAL | MBA:693 n=360; Nkx2-1=5.34, Pgr=4.54, Esr1=2.35, Tac1=1.39 | atlas-internal |
| Knoedler 2022 Esr1+ TRAP-seq VMH-FR vs BNST-FR | Bulk transcriptomic correlation | PARTIAL | SUPT_0564 not in top-20 by δ; SUPT_0563 takes ranks 1, 2, 4 instead | [3] |

*(SUPT_0564 child-cluster breakdown not assessed at this stage — child clusters were not enumerated in the rank-1 DB query and cluster-level expression / MFR were not pulled. The bulk-correlation analysis [3] indicates that SUPT_0564 child clusters are not the female-biased subset; that signal is concentrated in SUPT_0563.)*

### 4b. Property alignment — primary candidate (SUPT_0563)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Ventromedial hypothalamic nucleus [MBA:693] (VMHvl) | MBA:693 (VMH) primary location across child clusters | CLUS_2293 (top by δ); CLUS_2290, CLUS_2292 (female-biased) | CONSISTENT |
| NT type | not stated; VMHvl predominantly glutamatergic | Glutamatergic (VMH Fezf1 Glut label) | Glutamatergic | CONSISTENT |
| Sex ratio | female-biased lordosis subpopulation expected | not available at supertype level | CLUS_2290 MFR=0.08; CLUS_2292 MFR=0.12 (both strongly female-biased) | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Knoedler 2022 Esr1+ TRAP-seq VMH-FR vs BNST-FR | Bulk transcriptomic correlation | SUPPORT | best child CLUS_2293 rank 1/5322 (δ=0.0180); CLUS_2290 rank 2 (δ=0.0159, MFR=0.08); CLUS_2292 rank 4 (δ=0.0145, MFR=0.12); 3 child clusters in top 20 | [3] |

*(2 of the SUPT_0563 child clusters surfaced by the bulk correlation — CLUS_2290 (MFR=0.08) and CLUS_2292 (MFR=0.12) — are strongly female-biased, directly matching the lordosis-circuit subpopulation expectation. CLUS_2293 (top by δ) does not have an MFR value reported here. Sex ratio is NULL at supertype level; the female-biased signal is concentrated in these child clusters. Best match: CLUS_2293.)*

---

## 5. Candidate paragraphs

## 0564 VMH Fezf1 Glut_2 [CS20230722_SUPT_0564] · 🟡 MODERATE

### Supporting evidence

- **Direct location match.** SUPT_0564 has Ventromedial hypothalamic nucleus [MBA:693] as primary location with n=360 cells, directly matching the VMHvl soma location of the classical node.
- **Glutamatergic identity is CONSISTENT.** The VMH Fezf1 Glut_2 label is glutamatergic, consistent with the predominantly glutamatergic VMHvl Esr1/Pgr neuron population.
- **Nkx2-1 expression is strongly consistent (mean = 5.34).** This is a strong quantitative agreement with the defining Nkx2-1+ marker for the classical type, and matches the Nkx2-1+/ERα+/Tac1+ female-locomotion subpopulation reported in [1].
- **Pgr expression is moderately strong (mean = 4.54).** Approximate agreement with the Pgr+ defining marker [2]; consistent with subset expression within a heterogeneous supertype.
- **Esr1 (mean = 2.35) and Tac1 (mean = 1.39) are present at moderate-to-low levels.** Both are defining markers of the classical type; the moderate atlas values indicate subset expression rather than uniform population-level positivity, consistent with the Nkx2-1/ERα/Tac1 functional subpopulation [1] occupying a fraction of SUPT_0564.

### Marker evidence provenance

- **Esr1** — classical evidence is transcript-based (ISH/scRNA-seq) [1]. Atlas precomputed value (mean = 2.35) is transcript-based (10x Chromium). The moderate atlas value is consistent with subset expression: Esr1 marks a fraction of SUPT_0564 cells rather than the whole supertype. Specificity at cluster level was not assessed at this stage.
- **Pgr** — classical evidence is transcript-based [2] (Pgr+ neurons in VMHvl mediating mating/fighting). Atlas precomputed Pgr = 4.54 is a moderately strong agreement, consistent with Pgr+ neurons being a substantial subset of SUPT_0564.
- **Nkx2-1** — classical evidence is transcript-based [1] (Nkx2-1-expressing VMHVL neurons). Atlas precomputed Nkx2-1 = 5.34 is the strongest single marker agreement on this edge. No data-source discrepancy.
- **Tac1** — listed as both a defining marker and a neuropeptide on the classical node, with transcript-level evidence [1]. Atlas precomputed Tac1 = 1.39 is low-but-present, consistent with the small Nkx2-1+/ERα+/Tac1+ functional subpopulation that drives female locomotion. Peptidergic identity is inferred from gene transcript; not directly confirmed by atlas data.
- *(note: Calb1 has the highest mean expression in SUPT_0564 (mean = 8.0) but is not a defining marker of vmhvl_esr1_pr_neuron — Calb1 is a canonical marker of the distinct SDN-POA calbindin neuron. High Calb1 in SUPT_0564 warrants primary literature verification of whether Calb1 co-localises with Esr1/Pgr in VMHvl, or marks a distinct subpopulation within this supertype.)*

### Concerns

- **Heterogeneity caveat.** VMHvl contains 17 transcriptomic types (Kim 2019). The classical vmhvl_esr1_pr_neuron is acknowledged as spanning multiple functional subtypes — Pgr+ (mating/fighting), ERα+/Nkx2-1+/Tac1+ (female locomotion), and additional ERα subtypes — and SUPT_0564 captures only the broader Pgr+/Nkx2-1+/Tac1+ subset, not the female-biased lordosis subpopulation. This is the primary justification for the CROSS_CUTTING relationship and for retaining SUPT_0563 as a co-primary edge.
- **Bulk-correlation evidence does not single out SUPT_0564 as the female-receptive Esr1+ pool [3].**
  > Knoedler 2022 (PMID:35143761) Esr1+ TRAP-seq pooled VMH female-receptive vs BNST female-receptive. SUPT_0564 itself does not appear in the top 20 by δ — instead, SUPT_0563 takes 3 of the top 4 (CLUS_2293, 2290, 2292). This is independent quantitative support for the open question already raised on this edge: SUPT_0563 should be added as a co-primary CROSS_CUTTING target. SUPT_0564 retains its existing ATLAS_METADATA support but should not be the sole mapping target.
  > — Knoedler et al. 2022 · [3]
- **Calb1 specificity unresolved.** Calb1 mean = 8.0 is the highest expression in SUPT_0564 but is not a defining marker of vmhvl_esr1_pr_neuron; it is a canonical marker of the distinct SDN-POA calbindin neuron. Whether Calb1 co-localises with Esr1/Pgr in VMHvl SUPT_0564 cells, or marks a distinct subpopulation, is unresolved.
- **Child-cluster breakdown not assessed.** SUPT_0564 child clusters and their per-cluster MFR / marker means were not enumerated, so the cluster-level concordance question (which child clusters carry the Pgr+/Nkx2-1+/Tac1+ profile) remains open.

### What would upgrade confidence

- **Primary literature search** for whether Calb1 co-localises with Esr1/Pgr in VMHvl neurons or marks a distinct subpopulation — addressing the Calb1 unresolved question without new experiments.
- **SUPT_0564 child-cluster expression + MFR enumeration** — needed to identify which child cluster(s) of SUPT_0564 carry the Pgr+/Nkx2-1+/Tac1+ functional subpopulation, parallel to the SUPT_0563 cluster-level analysis [3] already on file.
- **MapMyCells annotation transfer** of published VMHvl ERα-Cre or Pgr-Cre scRNA-seq data to WMBv1; expected: F1 split between SUPT_0563 (female-biased lordosis subset) and SUPT_0564 (broader Pgr+ subset). Expected output: `AnnotationTransferEvidence` on both edges.

---

## 0563 VMH Fezf1 Glut_1 [CS20230722_SUPT_0563] · 🟡 MODERATE

### Supporting evidence

- **Direct location match.** SUPT_0563 has Ventromedial hypothalamic nucleus [MBA:693] as primary location across child clusters, consistent with the VMHvl soma location of the classical node.
- **Glutamatergic identity is CONSISTENT.** The VMH Fezf1 Glut_1 label is glutamatergic.
- **Sex ratio strongly concordant at cluster level.** Child clusters CLUS_2290 (MFR=0.08) and CLUS_2292 (MFR=0.12) are both strongly female-biased, directly matching the female-biased lordosis subpopulation expected within vmhvl_esr1_pr_neuron. Sex ratio at supertype level is NULL; this signal is only visible at cluster resolution.
- **Independent quantitative bulk-transcriptomic confirmation [3].**
  > Knoedler 2022 (PMID:35143761) Esr1+ TRAP-seq pooled VMH female-receptive vs BNST female-receptive. SUPT_0563 takes three of the top four child-cluster positions by δ = ρ(VMH_FR) − ρ(BNST_FR): CLUS_2293 (rank 1, δ=0.0180), CLUS_2290 (rank 2, δ=0.0159, MFR=0.08), CLUS_2292 (rank 4, δ=0.0145, MFR=0.12). The female-biased CLUS_2290 and CLUS_2292 directly correspond to the lordosis-circuit subpopulation flagged in vmhvl_esr1_pr_neuron's classical definition. SUPT_0563 was missed by the rank-1 DB query (no DEFINING_SCOPED markers in atlas metadata for this supertype) and is added here as a co-primary CROSS_CUTTING target alongside SUPT_0564 based on the bulk-correlation evidence.
  > — Knoedler et al. 2022 · [3]
- **Discovery provenance.** SUPT_0563 was missed by the rank-1 DB query (no DEFINING_SCOPED markers in atlas metadata for this supertype) and was added here as a co-primary CROSS_CUTTING target on the basis of the bulk-correlation ranks alone — a clean example of bulk correlation surfacing a target that atlas-metadata discovery missed.

### Marker evidence provenance

- **Per-marker atlas precomputed expression at supertype level (Esr1, Pgr, Nkx2-1, Tac1) was not assessed for SUPT_0563** at this stage. The supporting evidence for SUPT_0563 is primarily bulk-correlation rank and child-cluster MFR, not per-marker mean expression. This is a gap relative to SUPT_0564 and should be addressed by pulling cluster-level expression for CLUS_2290, 2292, 2293.

### Concerns

- **No per-marker atlas expression evidence.** Unlike SUPT_0564, SUPT_0563 does not have ATLAS_METADATA evidence on file showing Esr1/Pgr/Nkx2-1/Tac1 mean expression values; it relies on bulk correlation alone for quantitative support. Cluster-level Esr1/Pgr/Nkx2-1/Tac1 in CLUS_2290, 2292, 2293 should be enumerated.
- **Co-primary ambiguity.** SUPT_0563 is co-primary with SUPT_0564. The classical node is heterogeneous; SUPT_0563 captures the female-biased lordosis subpopulation, SUPT_0564 captures the broader Pgr+/Nkx2-1+/Tac1+ subpopulation. Whether this is a clean two-way split or whether both supertypes contain heterogeneous sub-populations cross-cutting the classical definition is open.
- **CLUS_2290 vs CLUS_2292 internal structure.** Whether these two female-biased child clusters are distinct functional subtypes within SUPT_0563 or replicates of the same lordosis subpopulation is unresolved.

### What would upgrade confidence

- **Cluster-level Esr1, Pgr, Nkx2-1, Tac1 co-expression in CLUS_2290, 2292, 2293** vs the female-biased clusters of SUPT_0564 — would distinguish the two SUPT mappings and provide direct per-marker concordance evidence parallel to the SUPT_0564 ATLAS_METADATA support.
- **MapMyCells annotation transfer** of published VMHvl ERα-Cre or Pgr-Cre scRNA-seq data to WMBv1; expected: F1 split between SUPT_0563 (female-biased) and SUPT_0564 (broader). Expected output: `AnnotationTransferEvidence` on both edges; F1 ≥ 0.50 at SUPT_0563 would substantially strengthen this edge.

---

## 6. Proposed experiments

### 1. Cluster-level Esr1, Pgr, Nkx2-1, Tac1 co-expression in CLUS_2290, 2292, 2293 (and SUPT_0564 child clusters)

**What:** Pull per-cluster precomputed expression for Esr1, Pgr, Nkx2-1, Tac1 across the
SUPT_0563 child clusters identified by the bulk-correlation analysis (CLUS_2290, CLUS_2292,
CLUS_2293) and across SUPT_0564 child clusters; compare per-cluster MFR and marker means.

**Target:** Identify the SUPT_0563 cluster(s) with peak Esr1/Pgr/Nkx2-1/Tac1 co-expression
and confirm whether the female-bias signal (CLUS_2290 MFR=0.08, CLUS_2292 MFR=0.12) is
co-extensive with peak marker expression.

**Expected output:** Cluster-level `property_comparisons` with per-marker means and MFR for
each SUPT_0563 / SUPT_0564 child cluster; potential addition of cluster-level edges if
specific child clusters emerge as the cleanest atlas correlate of the lordosis subpopulation
or the broader Pgr+ subpopulation.

**Resolves:** Open questions 1 and 2; addresses the SUPT_0563 per-marker atlas evidence gap.

### 2. MapMyCells annotation transfer of published VMHvl ERα-Cre or Pgr-Cre scRNA-seq data against WMBv1

**What:** Retrieve published VMHvl ERα-Cre or PR-Cre sorted scRNA-seq datasets and run
MapMyCells against WMBv1 at supertype and cluster resolution.

**Target:** F1 split between SUPT_0563 (female-biased lordosis subset) and SUPT_0564 (broader
Pgr+/Nkx2-1+/Tac1+ subset). F1 ≥ 0.50 at either supertype substantially strengthens the
corresponding edge; F1 ≥ 0.80 at cluster level would support upgrading either edge to HIGH.

**Expected output:** `AnnotationTransferEvidence` entries on both edges. Atlas: WMBv1. Tool:
MapMyCells. Output format: F1 matrix per supertype/cluster, fed back as `AnnotationTransferEvidence` YAML.

**Resolves:** Open question 1 (SUPT_0563 vs SUPT_0564 split); the `annotation_transfer_f1`
NOT_ASSESSED gap on both edges.

### 3. Targeted literature search — Calb1 co-localisation with Esr1/Pgr in VMHvl

**What:** Cite-traverse for primary studies testing whether Calb1 co-localises with Esr1
and/or Pgr in VMHvl neurons, vs marking a distinct subpopulation (e.g. SDN-POA calbindin
neurons).

**Target:** Resolve whether high SUPT_0564 Calb1 = 8.0 reflects the classical
Esr1/Pgr-defined population or a distinct co-resident subpopulation within the same
supertype.

**Expected output:** Evidence on the classical node (additional defining or negative marker)
or a caveat update on the SUPT_0564 edge.

**Resolves:** SUPT_0564 unresolved question on Calb1 specificity.

---

## 7. Open questions

1. Is SUPT_0563 vs SUPT_0564 a clean female-vs-broader split, or do both supertypes contain
   heterogeneous sub-populations that cross-cut the classical definition? *(Appears on the
   SUPT_0563 edge; bears on the CROSS_CUTTING relationship for both edges.)*
2. Are CLUS_2290 and CLUS_2292 distinct functional subtypes within SUPT_0563, or replicates
   of the same lordosis subpopulation? *(Appears on the SUPT_0563 edge.)*
3. Does Calb1 co-localise with Esr1/Pgr in VMHvl neurons, or does it mark a distinct
   subpopulation within SUPT_0564? *(Appears on the SUPT_0564 edge.)*

---

## 8. Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0564 | ATLAS_METADATA | PARTIAL — MBA:693 n=360; Nkx2-1=5.34, Pgr=4.54, Esr1=2.35, Tac1=1.39 |
| edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0564 | BULK_CORRELATION ([3] Knoedler 2022) | PARTIAL — SUPT_0564 not in top-20 by δ; supports adding SUPT_0563 as co-primary |
| edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0563 | BULK_CORRELATION ([3] Knoedler 2022) | SUPPORT — CLUS_2293 rank 1/5322 (δ=0.0180); CLUS_2290 rank 2 (MFR=0.08); CLUS_2292 rank 4 (MFR=0.12); 3 child clusters in top 20 |

---

## 9. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Correa et al. 2015 | [PMID:25543145](https://pubmed.ncbi.nlm.nih.gov/25543145/) | Soma location (VMHvl); Esr1, Nkx2-1, Tac1 markers; Tac1 neuropeptide; Nkx2-1+/ERα+/Tac1+ female-locomotion subpopulation |
| [2] | Zilkha et al. 2021 | [PMID:33910083](https://pubmed.ncbi.nlm.nih.gov/33910083/) | Pgr marker; Pgr+ VMHvl subpopulation in mating / fighting |
| [3] | Knoedler et al. 2022 | [PMID:35143761](https://pubmed.ncbi.nlm.nih.gov/35143761/) | Esr1+ TRAP-seq pooled VMH female-receptive vs BNST female-receptive bulk correlation against WMBv1 — supports SUPT_0563 as co-primary; SUPT_0564 not in top-20 by δ |
