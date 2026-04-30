# Arcuate aromatase neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Introduction

### Classical type

**Arcuate aromatase neuron** is defined by neurochemical criteria: Cyp19a1 (aromatase)
expression in a sexually dimorphic, male-biased cluster located in the arcuate hypothalamic
nucleus, adjacent to kisspeptin neurons. The population is part of a broader aromatase
neuronal network spanning hypothalamus and amygdala (~6,000 neurons at birth). Functionally,
male arcuate aromatase neurons convert testosterone to estrogen and regulate kisspeptin
neuron activity. Evidence derives from a single primary source (Wartenberg et al. 2021 [1]);
no CL term is currently assigned and the type is a candidate for a new term. NT type and
negative markers are not reported.

| Property | Value | References |
|---|---|---|
| Soma location | Arcuate hypothalamic nucleus [MBA:223] (adjacent to kisspeptin neurons, per source) | [1] |
| Defining markers | Cyp19a1 (aromatase, transcript) | [1] |

<details>
<summary>Literature support — expand for verbatim quotes</summary>

**[1] Wartenberg et al. 2021 · PMID:34561233 — Neuronal Markers and Molecular Characteristics**

> We identified an aromatase neuronal network comprising ~6000 neurons in the hypothalamus and amygdala. By birth, this network has become sexually dimorphic in a cluster of aromatase neurons in the arcuate nucleus adjacent to kisspeptin neurons. We demonstrate that male arcuate aromatase neurons convert testosterone to estrogen to regulate kisspeptin neuron activity.
> — Wartenberg et al. 2021, Neuronal Markers and Molecular Characteristics · [1] <!-- quote_key: 237626479_5aec04ab -->

</details>

---

## Results

**Primary finding (null result).** A complete scan of WMBv1 (CCN20230722) confirmed that
no supertype or cluster located in Arcuate hypothalamic nucleus [MBA:223] carries Cyp19a1
as a defining marker. All Cyp19a1-expressing clusters identified by the DB scan reside in
preoptic area (POA) and periventricular zones, not in MBA:223. The best available atlas
match — 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] — is in the periventricular
preoptic zone (PVpo n=64; MPN n=37; AVPV n=16) with **no MBA:223 cells**, and is proposed
only because its child cluster CLUS_1907 carries Cyp19a1 as a defining marker (supertype
mean Cyp19a1=1.15). The arc_aromatase_neuron edge is therefore classified UNCERTAIN, and
the apparent transcriptomic signal is anatomically discordant with the classical type's
defining ARH location.

### Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (MERFISH) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] | (self) | n=117 (PVpo 64 / MPN 37 / AVPV 16; **0 in MBA:223**) | ⚪ UNCERTAIN | Cyp19a1 APPROXIMATE; location DISCORDANT | Eliminated |

1 edge total. Relationship type: UNCERTAIN.

### Property alignment — primary candidate (SUPT_0486)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Arcuate hypothalamic nucleus [MBA:223] | MBA:133 PVpo n=64; MBA:515 MPN n=37; MBA:272 AVPV n=16 — no MBA:223 cells | not assessed | DISCORDANT |
| Cyp19a1 expression | POSITIVE (transcript, primary defining marker) | precomputed mean_expression=1.15; child CLUS_1907 has Cyp19a1 as defining marker | not assessed | APPROXIMATE |
| Sex ratio | Male-biased (not quantitatively documented in classical source) | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas DB scan for Cyp19a1 in ARH (MBA:223) | Atlas metadata | WEAK | No MBA:223 supertype carries Cyp19a1 as defining marker; SUPT_0486 best available (mean=1.15) but in PVpo-VMPO-MPN | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments. CLUS_1907 is flagged
in atlas metadata as carrying Cyp19a1 as a defining marker, but its MERFISH spatial
distribution within SUPT_0486's preoptic/periventricular footprint has not been verified
against MBA:223.)*

---



### Eliminated candidates

**Shared disqualifying signal:** the only edge on this classical node is UNCERTAIN, and
the disqualifying property is **anatomical location**. Cyp19a1 expression is detectable
at supertype level in SUPT_0486 (mean=1.15) and at child-cluster level in CLUS_1907
(defining marker), but the supertype's MERFISH soma distribution places its cells in
MBA:133 (PVpo, n=64), MBA:515 (MPN, n=37), and MBA:272 (AVPV, n=16) with **zero cells in
MBA:223 (ARH)**. The defining ARH location of arc_aromatase_neuron is therefore not
recovered by any Cyp19a1-positive WMBv1 supertype.

### 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] · ⚪ UNCERTAIN

**Disqualifying evidence**

- **Location DISCORDANT — distant region.** Classical type is in Arcuate hypothalamic
  nucleus [MBA:223]; SUPT_0486 cells are distributed across the periventricular preoptic
  zone (MBA:133 PVpo, MBA:515 MPN, MBA:272 AVPV) with no cells recorded in MBA:223. POA
  and ARH are anatomically distinct hypothalamic nuclei separated by intervening
  periventricular and tuberal zones. *(distant region — stronger counter-evidence;
  classical type may still be a member of this T-type's broader aromatase network but
  not the ARH population specifically)*
- **Cyp19a1 alignment is APPROXIMATE only.** SUPT_0486 supertype mean Cyp19a1 = 1.15 is
  the best Cyp19a1 signal available, and CLUS_1907 carries Cyp19a1 as a defining marker;
  but a full DB scan confirmed **no ARH supertype expresses Cyp19a1 as a defining
  marker**. The match is therefore the least-bad transcriptomic candidate rather than a
  positive identification of the ARH aromatase population.
- **MERFISH registration uncertainty.** The classical type is defined in MBA:223 but the
  best transcriptomic match sits in periventricular preoptic territory. Possible
  explanations include MERFISH registration artefacts at the ARH/periventricular boundary
  or a pan-hypothalamic aromatase transcriptomic identity that is not segregated by
  anatomical zone in WMBv1 — neither is established by current evidence.
- **Single-source classical definition.** The ARH location assignment for
  arc_aromatase_neuron rests entirely on Wartenberg et al. 2021 [1]. ARH-region
  alternative supertypes SUPT_0427 and SUPT_0428 (ARH-PVi Six6 Dopa-Gaba) have not had
  Cyp19a1 expression assessed and remain possible — though unconfirmed — candidates.

**Marker evidence provenance**

- **Cyp19a1** — classical evidence is transcript-level (Wartenberg 2021 reports an
  aromatase neuronal network in hypothalamus and amygdala, sexually dimorphic in ARH
  adjacent to kisspeptin neurons) [1]. Atlas signal is also transcript-level (10x
  Chromium precomputed mean = 1.15 at SUPT_0486; CLUS_1907 carries Cyp19a1 as a defining
  marker). The atlas captures Cyp19a1+ cells, but they are spatially located in the
  preoptic / periventricular zone — not the arcuate nucleus. There is no atlas
  annotation/expression discrepancy in the usual sense (the gene is detected and the
  metadata flags it as defining for CLUS_1907) — the discrepancy is between the
  classical type's ARH location and the atlas Cyp19a1+ cells' POA/periventricular
  location.
- **Single-citation marker provenance.** Cyp19a1 as a defining marker for
  arc_aromatase_neuron rests on Wartenberg 2021 [1] alone. A targeted literature search
  for additional primary studies of arcuate Cyp19a1+ neurons (e.g. Cyp19a1-Cre lineage
  tracing, ISH co-localisation with kisspeptin) would strengthen the classical
  definition independently of the atlas mapping problem.

**What would upgrade — or definitively eliminate — confidence**

- **Query Cyp19a1 expression in ARH-located supertypes** (SUPT_0427, SUPT_0428, and
  neighbouring ARH supertypes) from the precomputed HDF5 stats. If any ARH supertype
  carries non-zero Cyp19a1, it becomes a stronger candidate than SUPT_0486 despite a
  weaker marker signal, because it would resolve the location DISCORDANT verdict. If all
  ARH supertypes are confirmed Cyp19a1-negative, SUPT_0486 remains the only available
  match and the UNCERTAIN classification is locked in by atlas-level absence of ARH
  Cyp19a1+ cells.
- **CLUS_1907 spatial localisation.** Confirm whether CLUS_1907 cells are exclusively
  POA/periventricular or include any MBA:223 representation. If exclusively POA, this
  strengthens the location DISCORDANT verdict.
- **Targeted cite-traverse** for "arcuate aromatase Cyp19a1 mouse" beyond Wartenberg 2021
  to confirm the ARH location of the classical type with independent primary evidence.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** See classical type table in Introduction; defining_basis on the classical node and per-property literature support are listed there. The KB-side definition lives at the source graph file linked in the reproducibility footer.

**Atlas mapping query.** Candidate atlas clusters were retrieved from CCN20230722 at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property was compared to the corresponding atlas-side value via the `property_comparisons` schema; alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.



**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote.

*Generated by evidencell `0c97cfa` from [`kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`](../../kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

</details>

---

## Discussion

**Primary mapping:** → SUPT_0486 (preoptic — wrong region; null result) at UNCERTAIN confidence. Key support: no support — ATLAS_METADATA confirms Cyp19a1 = 0.0 across all ARH supertypes (SUPT_0427 Cyp19a1=0.0; child clusters CLUS_1569, 1570, 1571 all = 0.0). Key caveats: `MARKER_NOT_SPECIFIC` (Cyp19a1 absent from atlas at the expected location); the arcuate aromatase population is not resolvable from WMBv1 metadata.

No Cell Ontology term currently assigned for this classical type.

### Proposed experiments and follow-ups

### 1. Targeted Cyp19a1 expression query in ARH-located WMBv1 supertypes

**What:** Query the precomputed HDF5 expression stats for Cyp19a1 across all WMBv1
supertypes whose MERFISH soma distribution includes Arcuate hypothalamic nucleus
[MBA:223] — including SUPT_0427 and SUPT_0428 (ARH-PVi Six6 Dopa-Gaba supertypes) and
neighbouring ARH supertypes.

**Target:** Identify any ARH supertype with Cyp19a1 mean expression ≥ 0.5 (consistent
with detectable subset expression).

**Expected output:** `MarkerAnalysisEvidence` for any ARH supertype with non-zero
Cyp19a1; or, if all ARH supertypes return Cyp19a1 ≈ 0, a negative `MarkerAnalysisEvidence`
that locks in the UNCERTAIN classification by establishing atlas-level absence of ARH
Cyp19a1+ cells.

**Resolves:** Open question 1.

### 2. Spatial localisation of CLUS_1907

**What:** Inspect the MERFISH spatial distribution of CLUS_1907 (the SUPT_0486 child
cluster carrying Cyp19a1 as a defining marker) and determine whether any cells are
located in MBA:223 (ARH) or whether the cluster is exclusively in POA/periventricular
zones.

**Target:** A definitive MBA-region breakdown of CLUS_1907 cells.

**Expected output:** Updated location field on the SUPT_0486 / CLUS_1907 edge, supporting
either retention of the DISCORDANT verdict (CLUS_1907 entirely outside MBA:223) or
re-assessment if any MBA:223 cells are present.

**Resolves:** Open question 2.

---

### Open questions

1. Do SUPT_0427 or SUPT_0428 (ARH Dopa-Gaba supertypes), or any other ARH-located
   supertype, show Cyp19a1 expression in the precomputed HDF5 stats?
2. Is CLUS_1907 located exclusively in POA/periventricular zones in MERFISH data, or
   are any cells assigned to MBA:223?

---

### Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_arc_aromatase_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA | WEAK — SUPT_0486 best available Cyp19a1 signal (mean=1.15; CLUS_1907 defining) but anatomically in PVpo-VMPO-MPN with 0 cells in MBA:223; full DB scan confirms no ARH supertype carries Cyp19a1 as a defining marker |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Wartenberg et al. 2021 | [PMID:34561233](https://pubmed.ncbi.nlm.nih.gov/34561233/) | Soma location (ARH adjacent to kisspeptin neurons), Cyp19a1 / aromatase as defining marker, sexually dimorphic male-biased ARH aromatase cluster, testosterone-to-estrogen conversion |
