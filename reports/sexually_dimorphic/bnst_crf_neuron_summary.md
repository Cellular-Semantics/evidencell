# BNST (anterolateral) corticotropin-releasing factor (CRF) neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Bed nuclei of the stria terminalis [MBA:174] — dlBNST, ovBNST, alBNST subnuclei | [1][2] |
| Neurotransmitter | GABAergic (inferred from literature context; not formally curated) | — |
| Defining markers | Crh | — |
| Negative markers | Calb1 | — |
| Neuropeptides | Crh | [1][2] |
| CL term | corticotropin-releasing neuron (CL:4072021) — BROAD match | — |

**Notes.** The classical type is defined by CRF/Crh expression in the anterolateral subdivision of the BNST (dlBNST, ovBNST, alBNST), with explicit Calb1 negativity distinguishing it from the Calb1+ calbindin-immunoreactive principal nucleus population. It carries a female-biased sexual dimorphism: CRF neurons in the anterolateral BNST are larger and more numerous in females. CL:4072021 is a broad parent term; a BNST-specific child term is a candidate for future CL contribution.

<details>
<summary>Literature support — expand for verbatim quotes</summary>

**[1] Kanaya et al. 2025, Frontiers in Neural Circuits — Sexually Dimorphic Brain Regions and Structures**

> "The BNST modulates pain sensitivity by releasing corticotropin-releasing factor (CRF) from neurons in the anterolateral subdivision (Ide et al., 2013). Female mice have larger CRF neurons in the anterolateral BNST than male mice (Uchida et al., 2019). Dopaminergic projection from the periaqueductal gray (PAG) to the BNST, which preferentially targets the dorsal part, including the anterolateral subdivision (Gungor et al., 2016), drives pain-related behaviors differently between male and female mice (Yu et al., 2021b)."
> — Kanaya et al. 2025, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 279874350_b2b4adba -->

**[2] S et al. 2013 · PMID:23554470 — Sexually Dimorphic Brain Regions and Structures**

> "Pain is a complex experience composed of sensory and affective components. Although the neural systems of the sensory component of pain have been studied extensively, those of its affective component remain to be determined. In the present study, we examined the effects of corticotropin-releasing factor (CRF) and neuropeptide Y (NPY) injected into the dorsolateral bed nucleus of the stria terminalis (dlBNST) on pain-induced aversion and nociceptive behaviors in rats to examine the roles of these peptides in affective and sensory components of pain, respectively. In vivo microdialysis showed that formalin-evoked pain enhanced the release of CRF in this brain region. Using a conditioned place aversion (CPA) test, we found that intra-dlBNST injection of a CRF1 or CRF2 receptor antagonist suppressed pain-induced aversion. Intra-dlBNST CRF injection induced CPA even in the absence of pain stimulation. On the other hand, intra-dlBNST NPY injection suppressed pain-induced aversion. Coadministration of NPY inhibited CRF-induced CPA. This inhibitory effect of NPY was blocked by coadministration of a Y1 or Y5 receptor antagonist. Furthermore, whole-cell patch-clamp electrophysiology in dlBNST slices revealed that CRF increased neuronal excitability specifically in type II dlBNST neurons, whereas NPY decreased it in these neurons. Excitatory effects of CRF on type II dlBNST neurons were suppressed by NPY. These results have uncovered some of the neuronal mechanisms underlying the affective component of pain by showing opposing roles of intra-dlBNST CRF and NPY in pain-induced aversion and opposing actions of these peptides on neuronal excitability converging on the same target, type II neurons, within the dlBNST."
> — S et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 14550592_292dccea -->

</details>

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (MERFISH) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| SUPERTYPE | 0393 CEA-BST Rai14 Pdyn Crh Gaba_2 [CS20230722_SUPT_0393] | — | not available | ⚪ UNCERTAIN | BNST location ✓, Crh ✓, GABAergic ✓; Calb1 discordant ✗ | Eliminated (Calb1+) |

---

## Eliminated candidates

### SUPT_0393 — 0393 CEA-BST Rai14 Pdyn Crh Gaba_2

**Accession:** CS20230722_SUPT_0393 · **Taxonomy level:** SUPERTYPE · **Relationship:** PARTIAL_OVERLAP

**Supporting evidence**

SUPT_0393 is the sole rank-1 WMBv1 candidate combining a BNST primary location (MBA:351, n = 140 cells), Crh as a defining-scoped atlas marker (precomputed mean expression = 7.96), and GABAergic neurotransmitter identity (Gad2 DEFINING marker, "Gaba" label). All three of these properties are consistent with the bnst_crf_neuron classical type, placing this supertype in the correct broad neighbourhood.

**Marker evidence provenance**

All marker comparisons are derived from WMBv1 atlas metadata (precomputed expression statistics and atlas-assigned marker flags). No literature-sourced marker evidence is available at this stage. The classical node's Crh positivity is supported by [1] and [2]; its Calb1 negativity is asserted from the literature (no direct PMID on file for the negative assertion) and cross-referenced against [2] (type II dlBNST neuron physiology context).

Atlas annotation/expression discrepancy check: Crh is a DEFINING_SCOPED marker and also the node neuropeptide; precomputed mean_expression = 7.96 (above 0.5 threshold — no discrepancy flagged). Calb1 is a NEGATIVE marker on the classical node, not a DEFINING or NEUROPEPTIDE marker — atlas expression discrepancy check does not apply.

**Concerns**

The critical discordance is Calb1 expression. Calb1 is an explicit negative marker for bnst_crf_neuron — it distinguishes dlBNST CRF neurons from the Calb1+ principal nucleus population. SUPT_0393 shows a precomputed mean Calb1 expression of 5.57, a substantial value indicating that a meaningful proportion of cells within this supertype express Calb1. This strongly suggests that SUPT_0393 is a heterogeneous aggregation of at least two biologically distinct BNST GABAergic populations: Calb1- Crh-high CRF neurons (the target classical type) and Calb1+ neurons of the BNST principal nucleus.

A secondary concern is spatial resolution. The classical type is defined at sub-nucleus resolution (dlBNST, ovBNST, alBNST). WMBv1 MERFISH annotation assigns these cells to the parent BNST term (MBA:351) without sub-nucleus assignment, so sub-nuclear identity of any matched cells cannot be confirmed from atlas metadata alone.

**What would upgrade confidence**

Identifying a child cluster of SUPT_0393 with low Calb1 and high Crh expression would provide a more specific atlas target and could support confidence upgrade to LOW or MODERATE for that cluster. Additionally, confirming a female-biased sex ratio in that child cluster would provide independent corroboration of the sexual dimorphism reported in the literature.

---

## Proposed experiments

### Bioinformatic / in silico

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Query precomputed expression for Calb1 and Crh across all child clusters of SUPT_0393 | Child clusters of CS20230722_SUPT_0393 in WMBv1 | Identification of any Calb1-low, Crh-high child cluster as a more specific mapping candidate | Whether a finer-grained atlas unit matches the classical type; potential confidence upgrade |

---

## Open questions

1. Do individual clusters under SUPT_0393 segregate into Calb1-high and Calb1-low populations? A Calb1-low, Crh-high child cluster would support confidence upgrade for that unit.
2. Does SUPT_0393 (or a child cluster) show a female-biased sex ratio consistent with the reported sexual dimorphism of bnst_crf_neuron?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_bnst_crf_neuron_to_cs20230722_supt_0393 | ATLAS_METADATA | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | https://doi.org/10.3389/fncir.2025.1593443 | — | soma location, neuropeptide (Crh), sex dimorphism |
| [2] | S et al. 2013 · PMID:23554470 | 23554470 | soma location, neuropeptide (Crh), dlBNST type II neurons |
