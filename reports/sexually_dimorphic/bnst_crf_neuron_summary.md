# BNST (anterolateral) corticotropin-releasing factor (CRF) neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

**BNST (anterolateral) corticotropin-releasing factor (CRF) neuron** is defined by
neurochemical criteria: Crh expression as both a defining marker and the released
neuropeptide; Calb1 absence (distinguishing dlBNST CRF neurons from the Calb1+
principal nucleus of BNST); and a female-biased sexual dimorphism — anterolateral
BST CRF+ neurons are larger and more numerous in females. Somas concentrate in
three sub-nuclei of the bed nucleus of the stria terminalis: dlBNST, ovBNST, and
alBNST. Functional electrophysiology classifies these as Type II dlBNST neurons.

CL term: **corticotropin-releasing neuron (CL:4072021)** — mapping is BROAD; a
BNST-specific child term is a candidate for new CL contribution.

| Property | Value | References |
|---|---|---|
| Soma location | Bed nuclei of the stria terminalis [MBA:174] (dorsolateral / oval / anterolateral subnuclei) | [1], [2] |
| Defining markers | Crh | — |
| Negative markers | Calb1 | — |
| Neuropeptides | Crh (corticotropin-releasing factor) | [1], [2] |
| CL term | CL:4072021 (corticotropin-releasing neuron) — BROAD | |

<details>
<summary>Literature support — expand for verbatim quotes</summary>

**[1] Frontiers in Neural Circuits 2025 — Sexually Dimorphic Brain Regions and Structures**

> The BNST modulates pain sensitivity by releasing corticotropin-releasing factor (CRF) from neurons in the anterolateral subdivision (Ide et al., 2013). Female mice have larger CRF neurons in the anterolateral BNST than male mice (Uchida et al., 2019). Dopaminergic projection from the periaqueductal gray (PAG) to the BNST, which preferentially targets the dorsal part, including the anterolateral subdivision (Gungor et al., 2016), drives pain-related behaviors differently between male and female mice (Yu et al., 2021b).
> — Frontiers in Neural Circuits 2025, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 279874350_b2b4adba -->

**[2] Ide et al. 2013 · PMID:23554470 — Sexually Dimorphic Brain Regions and Structures**

> Pain is a complex experience composed of sensory and affective components. Although the neural systems of the sensory component of pain have been studied extensively, those of its affective component remain to be determined. In the present study, we examined the effects of corticotropin-releasing factor (CRF) and neuropeptide Y (NPY) injected into the dorsolateral bed nucleus of the stria terminalis (dlBNST) on pain-induced aversion and nociceptive behaviors in rats to examine the roles of these peptides in affective and sensory components of pain, respectively. In vivo microdialysis showed that formalin-evoked pain enhanced the release of CRF in this brain region. Using a conditioned place aversion (CPA) test, we found that intra-dlBNST injection of a CRF1 or CRF2 receptor antagonist suppressed pain-induced aversion. Intra-dlBNST CRF injection induced CPA even in the absence of pain stimulation. On the other hand, intra-dlBNST NPY injection suppressed pain-induced aversion. Coadministration of NPY inhibited CRF-induced CPA. This inhibitory effect of NPY was blocked by coadministration of a Y1 or Y5 receptor antagonist. Furthermore, whole-cell patch-clamp electrophysiology in dlBNST slices revealed that CRF increased neuronal excitability specifically in type II dlBNST neurons, whereas NPY decreased it in these neurons. Excitatory effects of CRF on type II dlBNST neurons were suppressed by NPY. These results have uncovered some of the neuronal mechanisms underlying the affective component of pain by showing opposing roles of intra-dlBNST CRF and NPY in pain-induced aversion and opposing actions of these peptides on neuronal excitability converging on the same target, type II neurons, within the dlBNST.
> — Ide et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 14550592_292dccea -->

</details>

---

## 4. Mapping candidates

### 4a. Candidate overview

Two mapping edges are recorded for bnst_crf_neuron: an alternative supertype-level
edge to SUPT_0358 supported by Knoedler 2022 Esr1+ TRAP-seq bulk-correlation
evidence (LOW confidence — Esr1+ is a proxy, not a direct Crh signal), and the
existing supertype-level edge to SUPT_0393 (the sole rank-1 candidate carrying
Crh as a DEFINING_SCOPED atlas marker, eliminated at supertype resolution by
Calb1 discordance). Both are speculative or eliminated at supertype resolution
and require child-cluster analysis.

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0358 MEA-BST Lhx6 Nfib Gaba_2 [CS20230722_SUPT_0358] | (self) | not assessed | 🔴 LOW | NT CONSISTENT; Crh NOT_ASSESSED (Esr1+ proxy); location APPROXIMATE | Speculative |
| — | 0393 CEA-BST Rai14 Pdyn Crh Gaba_2 [CS20230722_SUPT_0393] | (self) | not assessed | ⚪ UNCERTAIN | Crh CONSISTENT; Calb1 DISCORDANT | Eliminated (negative_Calb1) |

2 edges total. Relationship type: PARTIAL_OVERLAP (both edges).

### 4b. Property alignment — primary candidate (SUPT_0358)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Bed nuclei of the stria terminalis [MBA:174] (dlBNST / ovBNST / alBNST) | Multiple child clusters; spans BST and MEA | CLUS_1290 primary soma = BST proper | APPROXIMATE |
| NT type | GABAergic (CRF+ BST neurons predominantly GABAergic) | GABAergic (Lhx6 Nfib Gaba_2) | not assessed | CONSISTENT |
| Crh expression | POSITIVE (defining marker) | NOT_ASSESSED — Knoedler sorted on Esr1, not Crh | not assessed | NOT_ASSESSED |
| Sex ratio | sexually dimorphic (anterolateral BST CRF+ neurons larger in females) | not available | child cluster MFRs span 0.82 to 99.0; CLUS_1293 MFR=99 (male-biased) | APPROXIMATE |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Knoedler 2022 Esr1+ TRAP-seq BNST-FR vs VMH-FR | Bulk transcriptomic correlation | PARTIAL | best_child_cluster=CLUS_1295 (rank 4, δ=0.0161); 4 SUPT_0358 child clusters in top 10 | [3] |

*(Of the 4 SUPT_0358 child clusters in the Knoedler top-10 BNST-specific signal,
CLUS_1290 maps to BST proper while CLUS_1293 carries an extreme male-biased
MFR=99 — divergent from the female-biased classical type. Best match by BNST
specificity: CLUS_1295. Direct Crh expression at child-cluster level has not
been assessed.)*

---

## 5. Candidate paragraphs

## 0358 MEA-BST Lhx6 Nfib Gaba_2 [CS20230722_SUPT_0358] · 🔴 LOW

### Supporting evidence

- **GABAergic identity is concordant.** Supertype label Lhx6 Nfib Gaba_2 directly
  aligns with the GABAergic phenotype expected for BST CRF+ neurons (CONSISTENT).
- **BST anatomical signal is captured at child-cluster level.** Property
  comparison records CLUS_1290 with primary soma in BST proper, providing direct
  anatomical anchoring within an otherwise mixed BST/MEA supertype (APPROXIMATE
  at supertype level due to MEA contribution).
- **Knoedler 2022 Esr1+ TRAP-seq bulk-correlation signal [3].**
  > Knoedler 2022 (PMID:35143761) Esr1+ TRAP-seq pooled BNST female-receptive vs VMH female-receptive identifies SUPT_0358 (MEA-BST Lhx6 Nfib Gaba_2) as a top BNST-specific signal. Multiple child clusters appear in top 10 by δ(BNST_FR − VMH_FR): CLUS_1295 (rank 4), CLUS_1291 (rank 5), CLUS_1290 (rank 9, primary soma BST proper), CLUS_1293 (rank 10, MFR=99 — extreme male bias). CRITICAL CAVEAT: Knoedler sorted on Esr1+, not Crh+. This evidence supports SUPT_0358 as the BST-localised Esr1+ supertype; CRF+/Crh+ co-localisation within this supertype must be confirmed by direct evidence (ISH, scRNA-seq for Crh) before accepting SUPT_0358 as a bnst_crf_neuron mapping target. Confidence held at LOW pending that confirmation.
  > — Knoedler et al. 2022 · [3]

### Marker evidence provenance

- **Crh** — classical node carries Crh as a defining marker without a primary
  citation on the marker entry itself; literature support comes via the
  neuropeptide field [1], [2], both of which establish Crh release and peptide
  function in dlBNST. At target side, SUPT_0358 has no DEFINING marker for Crh
  in atlas metadata, and the Knoedler sort was on Esr1+ rather than Crh+. The
  mapping therefore relies on an Esr1+ proxy with no direct Crh quantification
  at supertype or child-cluster level — a substantial provenance gap. *(note:
  targeted ISH or scRNA-seq for Crh+/Esr1+ overlap in BST would resolve whether
  the BNST-Esr1+ transcriptomic signature is a valid proxy for the CRF+
  population.)*
- **Calb1 (negative marker)** — classical node lists Calb1 as a negative marker
  without a primary citation on the marker entry. Calb1 expression at SUPT_0358
  has not been quantified in this edge's property_comparisons; this remains an
  assessment gap that should be checked against precomputed expression to rule
  out a Calb1+ contamination similar to that seen in SUPT_0393.

### Concerns

- **Crh expression is NOT_ASSESSED at supertype/cluster level.** The Knoedler
  evidence is pooled Esr1+ TRAP-seq — Crh+/Esr1+ co-localisation in BST is not
  established by this run. Without direct Crh quantification, SUPT_0358 cannot
  be confirmed as the CRF+ correlate.
- **Location APPROXIMATE — supertype spans BST and MEA.** SUPT_0358 includes
  medial amygdala (MEA) cells alongside BST. *(adjacent region — MEA and BST
  are part of the extended amygdala continuum, so this is weak counter-evidence
  at supertype resolution; cluster-level resolution shows CLUS_1290 is in BST
  proper.)*
- **Sex ratio APPROXIMATE with conflicting child-cluster signal.** Child cluster
  MFRs span 0.82 to 99.0; CLUS_1293 (rank 10 in the Knoedler signal) carries
  MFR = 99 — extreme male bias, opposite the female-biased dimorphism that
  defines bnst_crf_neuron. This indicates SUPT_0358 aggregates sex-divergent
  subpopulations and the CRF+ female-biased subset is unlikely to encompass
  the entire supertype.
- **No DEFINING Crh marker in atlas metadata (NO_DISCRIMINATING_MARKER caveat).**
  The mapping rests entirely on bulk-correlation co-localisation evidence
  (Esr1+ proxy). Direct Crh expression measurement at cluster level is the
  prerequisite for any confidence upgrade.
- **Ambiguous mapping vs SUPT_0393 (AMBIGUOUS_MAPPING caveat).** SUPT_0358 and
  SUPT_0393 may both capture parts of the heterogeneous BNST-CRF population —
  SUPT_0393 via direct Crh expression (Calb1-confounded), SUPT_0358 via Esr1+
  proxy (Crh-unverified). Curator review is required to determine which (or
  both) should be retained.

### What would upgrade confidence

- **ISH or MERFISH co-staining for Crh, Esr1, Calb1 in BST** to identify the
  cluster boundary between SUPT_0358 (Esr1+) and SUPT_0393 (Crh+). Expected
  output: `MarkerAnalysisEvidence` resolving the Crh+/Esr1+/Calb1− triple-
  overlap fraction within SUPT_0358 child clusters.
- **MapMyCells annotation transfer of published BNST scRNA-seq with Crh+ subset
  annotations** to WMBv1 at cluster resolution. Target: F1 ≥ 0.50 for Crh+
  subset cells against either SUPT_0358 or SUPT_0393 (split expected).
  Expected output: `AnnotationTransferEvidence` on both edges.
- **Targeted child-cluster query for Crh and Calb1 precomputed expression**
  across SUPT_0358 child clusters (CLUS_1290, CLUS_1291, CLUS_1293, CLUS_1295)
  to identify any Crh-high, Calb1-low, female-biased child cluster as a more
  specific candidate.
- **Targeted literature search** for primary citations supporting Calb1
  negativity in dlBNST CRF neurons (currently unsourced on the classical node)
  would strengthen the negative-marker assertion that is currently driving the
  SUPT_0393 elimination.

---

## Eliminated candidates

### 0393 CEA-BST Rai14 Pdyn Crh Gaba_2 [CS20230722_SUPT_0393] · ⚪ UNCERTAIN

The single shared disqualifying signal is **Calb1 DISCORDANT** at supertype
level (precomputed mean = 5.57 despite Calb1 being a NEGATIVE marker for the
classical type).

**Disqualifying evidence:**

- **Calb1 = 5.57 at supertype level (DISCORDANT, primary driver of UNCERTAIN
  confidence).** Calb1 is explicitly absent in dlBNST CRF neurons but shows
  substantial supertype-level expression. SUPT_0393 likely aggregates both
  Calb1− CRF neurons and Calb1+ BNST neurons. *(strong counter-evidence in a
  marker sense — the negative-marker discordance disqualifies the supertype
  as a whole; a child cluster with low Calb1 and high Crh would be a more
  specific mapping candidate and may support upgrade to LOW or MODERATE.)*
- **Sub-nucleus identity unresolvable (MERFISH_REGISTRATION_UNCERTAINTY
  caveat).** The classical type is defined at sub-nucleus resolution (dlBNST,
  ovBNST, alBNST). WMBv1 MERFISH annotation uses the parent BNST term
  [MBA:351] without sub-nucleus assignment. This caveat applies to any BST
  candidate, not only SUPT_0393.

**Otherwise-supportive properties (PARTIAL atlas-metadata evidence, all
overruled by the Calb1 discordance):**

- Crh = 7.96 (DEFINING_SCOPED, CONSISTENT) — SUPT_0393 is the only rank-1
  candidate with BST location, Crh marker, and GABAergic NT.
- Location = BNST [MBA:351] n = 140 (CONSISTENT).
- NT = GABAergic, Gad2 DEFINING (CONSISTENT).

A Calb1-low child cluster of SUPT_0393 may rescue this candidate.

---

## 6. Proposed experiments

### 1. ISH or MERFISH co-staining for Crh, Esr1, Calb1 in BST

**What:** Triple-stain ISH or MERFISH of BST in male and female mice for Crh,
Esr1, and Calb1 to define the cluster boundary between SUPT_0358 (Esr1+) and
SUPT_0393 (Crh+ with Calb1+ admixture) and to identify the Crh+ Calb1−
anterolateral BST subset.

**Target:** Quantify Crh+/Esr1+ overlap fraction in BST; identify a Crh+
Calb1− Esr1+ female-biased subset.

**Expected output:** `MarkerAnalysisEvidence` on both edges.

**Resolves:** Open questions 1 and 2 (which supertype is the better mapping
target).

### 2. Annotation transfer of BNST scRNA-seq with Crh+ subset annotations

**What:** MapMyCells annotation transfer of published BNST scRNA-seq with Crh+
subset annotations against WMBv1 at cluster resolution.

**Target:** F1 split between SUPT_0358 and SUPT_0393 — diagnostic for which
supertype carries the Crh+ female-biased dimorphic population.

**Expected output:** `AnnotationTransferEvidence` on both edges. Atlas: WMBv1.
Tool: MapMyCells. Output format: per-cluster F1 matrix, fed back as
`AnnotationTransferEvidence` YAML.

**Resolves:** Open questions 1 and 2; addresses the Crh NOT_ASSESSED gap on
SUPT_0358.

### 3. Child-cluster precomputed expression query for SUPT_0393 and SUPT_0358

**What:** Query precomputed Calb1 and Crh expression across child clusters of
SUPT_0393 to identify any Calb1-low, Crh-high cluster as a more specific
mapping candidate. Apply the same query to SUPT_0358 child clusters
(CLUS_1290, CLUS_1291, CLUS_1293, CLUS_1295) for direct Crh assessment.

**Target:** Identify a Crh-high, Calb1-low child cluster (in either supertype)
that could be promoted to a primary cluster-level mapping.

**Expected output:** Per-child-cluster Crh and Calb1 means recorded on the
edges; potentially a new cluster-level `MappingEdge` if a clean child cluster
is identified.

**Resolves:** SUPT_0393 Calb1 DISCORDANT rescue path; SUPT_0358 Crh
NOT_ASSESSED gap; refinement of female-biased vs male-biased child-cluster
heterogeneity within SUPT_0358.

---

## 7. Open questions

1. What fraction of SUPT_0358 cells co-express Esr1 and Crh? ISH or scRNA-seq
   for Crh+/Esr1+ overlap in BST would resolve this. *(Appears on the SUPT_0358
   edge.)*
2. Is SUPT_0393 (high Crh, Calb1-confounded) or SUPT_0358 (Esr1+ proxy,
   Crh-unverified) the better mapping for the sexually dimorphic anterolateral
   BST CRF+ population — or do they capture distinct subsets? *(Appears on the
   SUPT_0358 edge as the AMBIGUOUS_MAPPING caveat.)*
3. Do individual clusters under SUPT_0393 segregate into Calb1-high and
   Calb1-low populations? A Calb1-low, Crh-high child cluster would support
   confidence upgrade. *(Appears on the SUPT_0393 edge.)*
4. Does SUPT_0393 show a female-biased sex ratio consistent with
   bnst_crf_neuron? *(Appears on the SUPT_0393 edge.)*

---

## 8. Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_bnst_crf_neuron_to_cs20230722_supt_0358 | BULK_CORRELATION ([3] Knoedler 2022) | PARTIAL — best_child_cluster=CLUS_1295 (rank 4, δ=0.0161); 4 SUPT_0358 child clusters in top 10 of BNST-FR vs VMH-FR; Esr1+ proxy, Crh unverified |
| edge_bnst_crf_neuron_to_cs20230722_supt_0393 | ATLAS_METADATA | PARTIAL — Crh=7.96 (DEFINING_SCOPED), BST [MBA:351] n=140, Gad2 DEFINING; Calb1=5.57 DISCORDANT vs negative-marker requirement |

---

## 9. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Frontiers in Neural Circuits 2025 | [DOI:10.3389/fncir.2025.1593443](https://doi.org/10.3389/fncir.2025.1593443) | Soma location; CRF neuropeptide; female-biased dimorphism in anterolateral BNST |
| [2] | Ide et al. 2013 | [PMID:23554470](https://pubmed.ncbi.nlm.nih.gov/23554470/) | Soma location (dlBNST); CRF neuropeptide; Type II ephys classification within dlBNST |
| [3] | Knoedler et al. 2022 | [PMID:35143761](https://pubmed.ncbi.nlm.nih.gov/35143761/) | Knoedler 2022 Esr1+ TRAP-seq pooled BNST female-receptive vs VMH female-receptive — bulk-correlation BNST-specific signal identifying SUPT_0358 |
