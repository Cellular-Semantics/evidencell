# Arcuate aromatase neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

The arcuate aromatase neuron is a sexually dimorphic, male-biased neuronal
population of the arcuate hypothalamic nucleus that expresses aromatase
(Cyp19a1) and locally converts testosterone to estrogen adjacent to
kisspeptin neurons [1]. It forms part of a broader aromatase neuronal
network spanning hypothalamus and amygdala and is implicated in
estrogen-dependent regulation of kisspeptin neuron activity [1]. Mapping
this neurochemically defined classical type to a WMBv1 atlas cluster
matters both for placing male-biased reproductive-axis circuitry into the
current mouse-brain transcriptomic taxonomy and for evaluating whether
ARH aromatase neurons form a distinct transcriptomic identity or share
identity with periventricular aromatase populations.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Arcuate hypothalamic nucleus [MBA:223] (adjacent to kisspeptin neurons) | [1] |
| Defining markers | Cyp19a1 (aromatase) | [1] |
| Definition basis | CLASSICAL_NEUROCHEMICAL | — |
| Sex bias | Male-biased dimorphism | [1] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location & defining marker (Cyp19a1):** Wartenberg et al. 2021, Neuronal Markers and Molecular Characteristics · [1]
  > We identified an aromatase neuronal network comprising ~6000 neurons in the hypothalamus and amygdala. By birth, this network has become sexually dimorphic in a cluster of aromatase neurons in the arcuate nucleus adjacent to kisspeptin neurons. We demonstrate that male arcuate aromatase neurons convert testosterone to estrogen to regulate kisspeptin neuron activity.
  > — Wartenberg et al. 2021, Neuronal Markers and Molecular Characteristics · [1] <!-- quote_key: 237626479_5aec04ab -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

A single candidate atlas supertype was assessed and eliminated as
UNCERTAIN: SUPT_0486 (0486 PVpo-VMPO-MPN Hmx2 Gaba_5) is the best
Cyp19a1-expressing supertype identifiable in WMBv1 but lies in the
periventricular preoptic zone, not the arcuate nucleus.

A complete scan of CCN20230722 confirmed that no WMBv1 supertype in
MBA:223 (Arcuate hypothalamic nucleus) carries Cyp19a1 as a defining
marker. The best Cyp19a1-positive supertype (SUPT_0486; precomputed
mean expression 1.15, child cluster CLUS_1907 carries Cyp19a1 as a
defining marker) is located in PVpo-VMPO-MPN, with no MBA:223 cells.
Result: no acceptable mapping in WMBv1 at the supertype level pending
assessment of remaining ARH-region candidates (SUPT_0427, SUPT_0428).

### Mapping candidates table

| Rank | WMBv1 supertype | Supertype accession | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---:|---|---|---|
| — | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 | CS20230722_SUPT_0486 | 178 | ⚪ UNCERTAIN | Cyp19a1 APPROXIMATE · Location DISCORDANT | Eliminated |

Total edges: 1 (UNCERTAIN; relationship UNCERTAIN).

## Eliminated candidates

**Shared disqualifying signal:** the single candidate is in the
periventricular preoptic zone, not the arcuate nucleus — the defining
anatomical property of the classical type.

### 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] · ⚪ UNCERTAIN (n=178)

**Property alignment**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Arcuate hypothalamic nucleus [MBA:223] | MBA:133 PVpo n=64; MBA:515 MPN n=37; MBA:272 AVPV n=16 — no MBA:223 cells | not assessed | DISCORDANT |
| Cyp19a1 expression | POSITIVE (transcript, primary defining marker) | precomputed mean_expression=1.15; child CLUS_1907 has Cyp19a1 as defining marker | CLUS_1907 (defining) | APPROXIMATE |
| Sex ratio | Male-biased (documented) | not available | not assessed | NOT_ASSESSED |

*(Child-cluster breakdown not assessed beyond CLUS_1907 — see proposed experiments.)*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas DB scan for Cyp19a1 in ARH | Atlas metadata | WEAK | No ARH supertype carries Cyp19a1 as defining marker; best Cyp19a1+ supertype (SUPT_0486) in PVpo-VMPO-MPN | atlas-internal |

**Disqualifying evidence**

- **Anatomical discordance (strong counter-evidence):** SUPT_0486 has zero cells in MBA:223; its 117 located cells distribute across PVpo (MBA:133, n=64), MPN (MBA:515, n=37) and AVPV (MBA:272, n=16). *(note: PVpo, MPN and AVPV are periventricular preoptic structures, anatomically distinct from the tuberal arcuate nucleus — this is a distant-region discordance, not a registration-boundary artefact between immediately adjacent subfields.)*
- **No ARH alternative identified:** a full DB scan of CCN20230722 found that all Cyp19a1-expressing supertypes are in POA and periventricular zones. No MBA:223 supertype carries Cyp19a1 as a defining marker.
- **Cyp19a1 evidence is partial, not refuting:** SUPT_0486 supertype-level Cyp19a1 mean expression = 1.15 and its child CLUS_1907 lists Cyp19a1 as a defining marker — the cluster is genuinely Cyp19a1+, just in the wrong anatomical zone.

**Concerns**

- **MERFISH registration uncertainty:** the mapping is proposed in the absence of any ARH-specific Cyp19a1-positive atlas cluster. *(note: while registration artefacts at periventricular boundaries can occur in MERFISH atlases, ARH and PVpo/AVPV/MPN are not adjacent subfields — the discordance is unlikely to be explained by boundary registration error alone. A pan-hypothalamic aromatase transcriptomic identity remains a plausible alternative explanation.)*
- **Single-source dependence:** the classical node's ARH location and Cyp19a1 assignment derive from a single primary publication (Wartenberg et al. 2021, PMID:34561233 [1]).
- **Untested ARH candidates:** SUPT_0427 and SUPT_0428 (ARH-PVi Six6 Dopa-Gaba supertypes) have not had Cyp19a1 expression confirmed against the precomputed HDF5 stats and may yet harbour the ARH aromatase population.

**Marker evidence provenance**

- **Cyp19a1 (defining):** transcript-level / immunohistochemical aromatase evidence in Wartenberg et al. 2021 [1]; cell-type specificity established by anatomical localisation adjacent to kisspeptin neurons in ARH. Atlas precomputed expression at SUPT_0486 (1.15) and the defining-marker annotation on child CLUS_1907 are concordant with the *molecular* identity but discordant with the *anatomical* identity of the classical type.

**What would upgrade confidence**

- **Targeted atlas query:** assess Cyp19a1 precomputed expression in SUPT_0427, SUPT_0428 and other ARH-region supertypes (HDF5 lookup; expected output: ATLAS_QUERY evidence). Resolves Q1.
- **MERFISH cell-distribution check for CLUS_1907:** confirm whether CLUS_1907 cells appear exclusively in POA/periventricular zones or also distribute into MBA:223. Resolves Q2.
- **Targeted literature search:** confirm whether ARH aromatase neurons have been transcriptomically profiled beyond Wartenberg 2021 — would address single-source dependence and refine the molecular signature beyond Cyp19a1 alone.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The arcuate aromatase neuron is defined
on neurochemical grounds (CLASSICAL_NEUROCHEMICAL) by Cyp19a1 (aromatase)
expression in ARH neurons adjacent to kisspeptin neurons, with male-biased
sexual dimorphism, from Wartenberg et al. 2021 [1].

**Atlas mapping query.** Candidate atlas supertypes were retrieved from
WMBv1 (CCN20230722) at the supertype rank using metadata-based scoring
(region match, Cyp19a1 defining-marker annotation, precomputed expression
mean). The DB scan covered all Cyp19a1-positive supertypes and confirmed
none lie in MBA:223. Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was
compared to the corresponding atlas-side value via the
`property_comparisons` schema, with alignments graded CONSISTENT /
APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side values came from
precomputed expression on the cluster/supertype and from MERFISH spatial
registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs,
and verbatim literature quotes in this report are validated against the
evidencell knowledge base at write time. Authored-prose evidence
narratives are validated against their source `evidence_items[*].explanation`
fields. The pre-write hook rejects any unresolvable identifier or
unattributed blockquote. Specific mapping limitations and caveats are
documented per-candidate in the Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:17+00:00 from [kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_arc_aromatase_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA | WEAK | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Arcuate aromatase neuron → 0486 PVpo-VMPO-MPN Hmx2
Gaba_5 [CS20230722_SUPT_0486] at UNCERTAIN confidence (eliminated). Key
support: atlas precomputed Cyp19a1 expression (mean 1.15) and the
defining-marker annotation on child CLUS_1907. Key caveats:
MERFISH_REGISTRATION_UNCERTAINTY (more plausibly, anatomical mismatch)
and SINGLE_DATASET dependence on Wartenberg 2021 [1]. No Cell Ontology
term currently assigned — candidate for CL contribution.

### Proposed experiments and follow-ups

- **What:** Targeted ARH-supertype Cyp19a1 query in the precomputed HDF5 stats.
  **Target:** Cyp19a1 mean expression and defining-marker status at SUPT_0427, SUPT_0428 and other ARH-region supertypes.
  **Expected output:** ATLAS_QUERY evidence item appended to the edge / new edges if any ARH supertype shows Cyp19a1 expression.
  **Resolves:** Q1; if positive, supplants the current UNCERTAIN SUPT_0486 mapping.

- **What:** MERFISH cell-distribution check for CLUS_1907.
  **Target:** per-region cell counts to confirm whether CLUS_1907 has any MBA:223 cells.
  **Expected output:** ATLAS_QUERY evidence on the location property.
  **Resolves:** Q2 — distinguishes pan-hypothalamic-identity from registration-artefact explanations of the ARH/POA discordance.

### Open questions

1. Do SUPT_0427 or SUPT_0428 (ARH Dopa-Gaba supertypes) show Cyp19a1 expression in the precomputed HDF5 stats?
2. Is CLUS_1907 located exclusively in POA/periventricular zones in MERFISH data, or does it also distribute into MBA:223?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Wartenberg et al. 2021 | [34561233](https://pubmed.ncbi.nlm.nih.gov/34561233/) | soma location; Cyp19a1 defining marker; sexual dimorphism |
