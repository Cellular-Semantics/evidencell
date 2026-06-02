# Central amygdala GABAergic projection neuron — CCN20230722 Mapping Report

## Introduction

The central amygdala (CeA) is the principal output nucleus of the amygdaloid complex, composed almost exclusively of GABAergic spiny projection neurons analogous to striatal medium spiny neurons. As the major source of amygdala-mediated behavioural outputs — projecting to brainstem, hypothalamus, and bed nucleus of the stria terminalis — CeA GABAergic projection neurons occupy a central position in fear, pain, and autonomic control circuits.

---

## Classical node properties

| Property | Value | Source(s) |
|---|---|---|
| Cell type name | Central amygdala GABAergic projection neuron | — |
| Definition basis | CLASSICAL | — |
| CL mapping | CL:0011005 (BROAD; auto-proposed, requires expert review) | — |
| Neurotransmitter | GABAergic | [1] [3] [4] |
| Soma location | UBERON:0002883 — central amygdaloid nucleus | [1] [2] [3] |
| Defining markers | None recorded | — |
| Negative markers | None recorded | — |
| Neuropeptides | None recorded | — |
| Morphology | Spiny projection neuron (extended amygdala type) | [4] |
| Electrophysiology | Not recorded | — |
| Notes | CeA further divides into medial (CeM), lateral (CeL), and central (CeC) sections | — |

**References used above:**
- [1] Raudales et al. 2024 · PMID:39012795
- [2] Nolan et al. 2020 · PMID:33015518
- [3] Ignacio et al. 2014 · PMID:25309888
- [4] Loonen & Ivanova 2016 · PMID:27920666

> "Both the cortical amygdalar nuclei and the basolateral amygdalar nuclear complex…have cortex-like cell types…In contrast, the so called 'extended amygdalar nuclei' contain predominantly GABAergic spiny projection neurons, like the striatum." <!-- quote_key: 18703800_715e9b7d -->

> "Within the amygdala nuclei, PNs are exclusively glutamatergic in BLA, CoA, BMA, exclusively GABAergic in CeA, and predominantly GABAergic in MeA and BST." <!-- quote_key: 271240390_b54d0b91 -->

---

## Mapping edge: edge_central_amygdala_gabaergic_projection_neuron_to_cs20230722_supt_0249

**Atlas target:** CS20230722_SUPT_0249 — "0249 NDB-SI-MA-STRv Lhx8 Gaba_6"
**Relationship:** skos:broadMatch
**Atlas cell count:** 423 cells

### Property comparisons

| Property | Classical node (A) | Atlas supertype (B) | Alignment |
|---|---|---|---|
| Neurotransmitter type | GABAergic | GABA (inferred from label "NDB-SI-MA-STRv Lhx8 Gaba_6"; nt_type field null) | CONSISTENT |
| Soma location | UBERON:0002883 central amygdala | MBA:536 Central amygdalar nucleus — 85 cells / 0.150 (Zhuang 2023 MERFISH); 33 cells / 0.073 (Yao 2024); dominant locations NDB, SI, Striatum, Pallidum (CeA region_fraction 0.14) | APPROXIMATE |
| Marker — Gbx1 | Not assessed (no defining markers on classical node) | Gbx1: DEFINING marker on SUPT_0249 | NOT_ASSESSED |
| Marker — Th | Not assessed | Th (tyrosine hydroxylase): DEFINING marker on SUPT_0249 | NOT_ASSESSED |
| Marker — Nr4a2 | Not assessed | Nr4a2: DEFINING and DEFINING_SCOPED on SUPT_0249 | NOT_ASSESSED |

### Key issue: Th as a defining marker

Tyrosine hydroxylase (Th) is a DEFINING marker for SUPT_0249. This is conspicuous for a putative CeA GABAergic projection neuron: Th marks catecholaminergic neurons and is not a canonical CeA marker. CeA neurons are GABAergic but not dopaminergic or noradrenergic. This discordance most likely reflects the non-CeA majority of the supertype — cells in the NDB, SI, STRv, and Pallidum that co-define this atlas cluster and may drive the Th signature. Spatial filtering restricted to MBA:536 cells would clarify whether the CeA minority of SUPT_0249 is also Th-positive.

### Discovery context

Five CeA GABAergic supertypes (SUPT_0249, SUPT_0255, SUPT_0252, SUPT_0238, SUPT_0235) all scored equally (score = 1) in discovery mode at MBA:536 with a GABAergic filter. SUPT_0249 is ranked first by cohort order only. All five remain equally viable candidates. This tie underscores the provisional character of the present mapping.

---

## Verdict

| Field | Value |
|---|---|
| Confidence | LOW |
| Confidence score | 0.30 |
| Relationship | skos:broadMatch |
| Atlas target | CS20230722_SUPT_0249 |

**Rationale.** Neurotransmitter type is consistent: the classical node is GABAergic and the atlas label designates GABA. Soma location is APPROXIMATE — CeA cells are present in SUPT_0249 (85 cells, 15% by MERFISH; 33 cells, 7% by Yao 2024), but the supertype's primary distribution spans the nucleus of the diagonal band (NDB), substantia innominata (SI), ventral striatum (STRv), and Pallidum, with CeA accounting for only ~14% of total cells. No defining markers are recorded on the classical node, leaving all three marker comparisons NOT_ASSESSED and providing no positive evidence of molecular identity. The Th defining marker on SUPT_0249 is potentially discordant with classical CeA GABAergic identity and requires scrutiny. Finally, five equally-scored CeA GABAergic supertypes exist at discovery; this assignment is provisional until canonical CeA markers are assessed across all candidates.

### Caveats

1. **BROAD_ATLAS_TYPE** — SUPT_0249 (NDB-SI-MA-STRv Lhx8 Gaba_6) spans NDB, SI, STRv, Pallidum, and Hypothalamus. CeA constitutes only ~14% of cells; the supertype label does not designate CeA as primary.
2. **ATLAS_MARKER_MISMATCH_RISK** — Th (tyrosine hydroxylase) is a defining marker of SUPT_0249, which is unusual for CeA GABAergic projection neurons. Enrichment may be driven by the non-CeA cell fraction; spatial filtering is required.
3. **MULTIPLE_CANDIDATES** — Five GABAergic supertypes at MBA:536 scored equally in discovery. SUPT_0249 is ranked first by cohort order only; SUPT_0255, SUPT_0252, SUPT_0238, and SUPT_0235 remain equally viable.

---

## Discussion

The present mapping highlights a fundamental gap in the classical node: no defining molecular markers are recorded for the central amygdala GABAergic projection neuron, even though the literature provides a rich set of canonical CeA markers (Prkcd, Sst, Crh, Calcrl, Htr2a, Tac2, Isl1). Critically, none of these canonical markers appear among the defining markers of any of the five equally-scored CeA GABAergic supertype candidates in CCN20230722. This absence does not imply the markers are absent from these atlas types — the current pipeline queries defining markers only. A follow-up targeted query for Prkcd, Sst, Crh, and Isl1 expression across all five MBA:536 GABAergic supertype candidates would likely resolve the tie and identify which supertype(s) carry the molecular signature of classical CeA subtypes. Adding these markers to the classical node definition would simultaneously strengthen or rule out the current broadMatch assignment.

The broadMatch to SUPT_0249 should therefore be treated as a discovery-mode placeholder rather than a biologically validated mapping. Two experiments are proposed: (1) query CCN20230722 for supertype-level expression of Prkcd, Sst, Crh, and Isl1 across all five MBA:536 GABAergic candidates to identify the best molecular match; (2) apply MERFISH spatial filtering to restrict SUPT_0249 to MBA:536 cells and compare the resulting marker profile — particularly Th expression — to the full supertype profile. If Th enrichment disappears after spatial restriction, the Th discordance is an artefact of the cross-regional supertype and the mapping confidence would improve; if it persists, SUPT_0249 may not represent canonical CeA neurons at all.

---

## References

| Label | Citation | PMID | DOI |
|---|---|---|---|
| [1] | Raudales et al. 2024 | PMID:39012795 | 10.7554/eLife.93481 |
| [2] | Nolan et al. 2020 | PMID:33015518 | 10.1177/2470547020944553 |
| [3] | Ignacio et al. 2014 | PMID:25309888 | 10.3389/fped.2014.00103 |
| [4] | Loonen & Ivanova 2016 | PMID:27920666 | 10.3389/fnins.2016.00539 |
| — | Zhuang 2023 (MERFISH atlas) | PMID:37915112 | — |
