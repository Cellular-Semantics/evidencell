# Sexually dimorphic nucleus of the preoptic area (SDN-POA) calbindin neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

The sexually dimorphic nucleus of the preoptic area (SDN-POA) is one of the
best-characterised sexually dimorphic brain structures in the rodent. It is a
histologically defined cluster of calbindin-D28K immunoreactive neurons in the
medial preoptic area, larger in males than in females, and considered the
rodent homolog of the third interstitial nucleus of the anterior hypothalamus
(INAH3) in humans [1] [2]. Mapping this classical, male-biased neurochemical
type to the WMBv1 atlas tests whether a histological subnucleus can be
recovered from molecular taxonomy alone.

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:515]; SDN-POA is a histological subnucleus within MPN | [1] [2] |
| Defining markers | Calb1 (calbindin-D28K) | [2] |
| Negative markers | Th | [2] |
| Sex bias | MALE_BIASED (SDN-POA larger in males than females; classical IHC) | [1] [2] |
| Cell Ontology term | (none assigned) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical histology/IHC · rodent SDN-POA · [1] [2]
  > The 2 best known dimorphic brain structures are the sexual dimorphic nucleus of the medial preoptic hypothalamic area (SDN-POA) in rodents, which correspond to the interstitial nucleus of the anterior hypothalamus (INAH) in humans, and the anteroventral periventricular (AVPV) nucleus. The first one controls male sex behavior and is larger in males than in females; the second one is critical for the cyclic control of ovulation and is larger in females than in males.
  > — Negri-Cesi 2015, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 14863067_fa51fcf7 -->

  > One of the well-defined sexually dimorphic structures in the brain is the sexually dimorphic nucleus, a cluster of cells located in the preoptic area of the hypothalamus. The rodent sexually dimorphic nucleus of the preoptic area can be delineated histologically using conventional Nissl staining or immunohistochemically using calbindin D28K immunoreactivity
  > — He et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_d6c3a647 -->

  > The sexually dimorphic nucleus has been specifically defined in the brains of human and other mammalian and non-mammalian and includes the third interstitial nucleus of the anterior hypothalamus in humans (Allen et al., 1989)(Allen et al., 1990) , the ovine sexually dimorphic nucleus in the medial preoptic area (Roselli et al., 2004) , the medial preoptic and anterior hypothalamic regions in rhesus monkeys (Byne, 1998) , a specific area in the medial preoptic nucleus in quail (Viglietti‐Panzica et al., 1986) , and the sexually dimorphic nucleus of the preoptic area in rats (Gorski et al., 1978)(Gorski et al., 1980) . The human sexually dimorphic nucleus of the preoptic area is located in the medial part of the preoptic area, between the dorsolateral supraoptic nucleus and the rostral pole of the paraventricular nucleus (Hofman et al., 1989)
  > — He et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_1098a86b -->

- **Calb1 / negative marker Th:** classical IHC · rodent SDN-POA · [2]
  > The sexually dimorphic nucleus of the preoptic area is highlighted by calbindin-D28K immunoreactivity: no TH-positive cells were found, but fine axon-like projections/synaptic structures were seen
  > — He et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_17d4bd9d -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Two candidate atlas nodes were assessed for `sdn_poa_calbindin_neuron`: the
supertype SUPT_0423 (BST-MPN Six3 Nrgn Gaba_4) and its child cluster CLUS_1550.
Both are LOW confidence / Speculative — the SDN-POA cannot be resolved as a
distinct spatial domain in WMBv1 MERFISH data, and the only MPN-primary
Calb1+ male-biased child cluster also shows non-zero Th expression discordant
with the classical Th-negative assertion.

### Mapping candidates

| Rank | WMBv1 node | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | SUPT_0423 (0423 BST-MPN Six3 Nrgn Gaba_4) | — (supertype) | 336 | 🔴 LOW | Calb1 CONSISTENT · Th DISCORDANT | Speculative |
| 2 | CLUS_1550 (1550 BST-MPN Six3 Nrgn Gaba_4) | 0423 BST-MPN Six3 Nrgn Gaba_4 | 48 | 🔴 LOW | Calb1 CONSISTENT · sex_ratio CONSISTENT · Th DISCORDANT | Speculative |

Total: 2 edges; both UNCERTAIN/PARTIAL_OVERLAP at LOW confidence.

#### Property alignment — SUPT_0423 (primary supertype candidate)

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | MBA:515 (Medial preoptic nucleus; SDN-POA is a histological subnucleus within MPN) | MBA:515 (MPN) n=47; also BNST n=18, AHN n=46, PVN n=31 | MBA:515 (MPN) n=22 primary soma (CLUS_1550); also PVH n=9, PVHap n=4, Hypothalamus n=9 | APPROXIMATE |
| Calb1 | POSITIVE (protein, primary defining marker) | mean_expression=6.42 (DEFINING_SCOPED atlas marker) | mean_expression=6.66 (CLUS_1550) | CONSISTENT |
| Th (negative) | ABSENT (no TH cell bodies in SDN-POA) | mean_expression=0.99 | mean_expression=2.75 (CLUS_1550) | DISCORDANT |
| Sex ratio | male-biased (SDN-POA larger in males) | not available | MFR=3.35 (CLUS_1550, male-biased) | CONSISTENT |
| Annotation transfer F1 | not applicable | NOT_ASSESSED | NOT_ASSESSED | NOT_ASSESSED |

*(1 of an unspecified number of child clusters of SUPT_0423, CLUS_1550, has
MPN as its primary soma and a male-biased MFR consistent with SDN-POA
identity; the remaining children of this BST-MPN supertype have different
primary soma assignments or do not show an unambiguous male bias. Best match:
CLUS_1550.)*

##### Evidence support — SUPT_0423

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (SUPT_0423 marker + region) | Atlas metadata | WEAK | Calb1=6.42 (DEFINING_SCOPED); MBA:515 n=47; Th=0.99 conflicts negative-marker assertion | atlas-internal |

#### Property alignment — CLUS_1550 (best child cluster)

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | MBA:515 (Medial preoptic nucleus; SDN-POA histological subnucleus) | not available | MBA:515 (MPN) n=22 primary soma; also PVH n=9, PVHap n=4, Hypothalamus n=9 | APPROXIMATE |
| Calb1 | POSITIVE (protein, primary defining marker) | not available | mean_expression=6.66 | CONSISTENT |
| Th (negative) | ABSENT (no TH cell bodies in SDN-POA) | not available | mean_expression=2.75 | DISCORDANT |
| Sex ratio | male-biased | not available | MFR=3.35 (male-biased) | CONSISTENT |
| Annotation transfer F1 | not applicable | not available | NOT_ASSESSED | NOT_ASSESSED |

##### Evidence support — CLUS_1550

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (CLUS_1550 marker + region + MFR) | Atlas metadata | WEAK | Calb1=6.66; MBA:515 primary soma n=22; MFR=3.35; Th=2.75 discordant | atlas-internal |

### 0423 BST-MPN Six3 Nrgn Gaba_4 · 🔴 LOW

**Supporting evidence**

- SUPT_0423 is the only anatomically plausible rank-1 candidate from
  metadata-based scoring; Calb1 mean_expression = 6.42 is high and the gene
  is annotated as a `DEFINING_SCOPED` marker for this supertype, matching
  the classical primary defining marker.
- MBA:515 (MPN) appears among the supertype's region distribution with n=47
  cells, consistent with the classical SDN-POA soma assignment (MPN).

**Marker evidence provenance**

- **Calb1 (defining):** classical evidence is protein-level (calbindin-D28K
  immunoreactivity from Nissl/IHC delineation of the SDN-POA) [2]. Atlas
  precomputed mean = 6.42 at supertype level (6.66 at CLUS_1550) is fully
  consistent. Calb1 is broadly expressed across the brain, so it is not
  region-specific — adequate as a co-defining feature but not sufficient
  alone (`MARKER_NOT_SPECIFIC` caveat).
- **Th (negative):** the classical Th-negative assertion derives from the
  same calbindin IHC study [2], which reported "no TH-positive cells" within
  the SDN-POA. Atlas mean_expression = 0.99 (SUPT_0423) and 2.75 (CLUS_1550)
  are low but non-zero. ⚠ This is a DISCORDANT alignment at cluster level.
  Because CLUS_1550 spans MPN, PVH, PVHap and additional hypothalamic
  regions, the non-zero Th signal may originate from non-MPN cells in the
  cluster rather than from MPN-resident Calb1+ neurons.

**Concerns**

- Location APPROXIMATE — the supertype is multi-regional (BNST, MPN, AHN,
  PVN). SDN-POA is a histological subnucleus *within* MPN, and WMBv1 MERFISH
  cannot resolve sub-MPN cytoarchitectonic zones (`MERFISH_REGISTRATION_UNCERTAINTY` caveat).
- Th DISCORDANT (mean=0.99 at supertype; 2.75 at cluster) — directly conflicts
  with the classical Th-negative defining property.
- Calb1 is `DEFINING_SCOPED` rather than `DEFINING` for SUPT_0423, and is
  expressed across many brain regions — insufficient alone to pick out
  SDN-POA (`MARKER_NOT_SPECIFIC` caveat).
- No annotation-transfer evidence has been computed for this node.

**What would upgrade confidence**

- MapMyCells annotation transfer of an MPN Calb1+ or SDN-POA-targeted
  scRNA-seq dataset against WMBv1 to produce `AnnotationTransferEvidence`
  (target F1 ≥ 0.80 at cluster level). Would resolve the supertype/cluster
  mapping question.
- Spatial inspection of SUPT_0423 MERFISH cells within MBA:515 for
  sub-regional clustering consistent with the dorsomedial SDN-POA position
  *(note: SDN-POA sits dorsomedially within MPN in classical histology —
  this is interpretation beyond the facts).*

### 1550 BST-MPN Six3 Nrgn Gaba_4 · 🔴 LOW

**Supporting evidence**

- CLUS_1550 is the only child cluster of SUPT_0423 whose **primary** soma
  assignment is MBA:515 (MPN), with n=22 MERFISH cells.
- Calb1 mean_expression = 6.66 at cluster level — high and consistent with
  the classical primary defining marker.
- Male-female ratio = 3.35 (male-biased), the strongest available
  transcriptomic signature concordant with the MALE_BIASED classical
  sex_bias. CLUS_1550 is the only cluster in SUPT_0423 combining MPN primary
  soma with an unambiguous male bias.

**Marker evidence provenance**

- **Calb1 (defining):** protein-level IHC from [2] is the basis. Atlas
  precomputed mean = 6.66 is fully consistent at cluster level.
- **Th (negative):** classical defines Th as ABSENT (IHC, [2]); atlas
  precomputed mean = 2.75 in CLUS_1550. Because CLUS_1550 spans MPN (n=22),
  PVH (n=9), PVHap (n=4), and other hypothalamic regions (n=9), the Th
  signal may originate from the PVH/PVHap components rather than MPN-proper
  cells. MERFISH spatial inspection of the Th channel within MBA:515-assigned
  cells of CLUS_1550 is required to distinguish these possibilities.

**Concerns**

- Location APPROXIMATE — although MPN is the primary soma, CLUS_1550 is
  spatially heterogeneous (also PVH/PVHap and broader hypothalamus). SDN-POA
  cannot be resolved within MPN at MERFISH resolution
  (`MERFISH_REGISTRATION_UNCERTAINTY`).
- Th DISCORDANT at cluster level (mean=2.75) — the strongest single
  counter-signal in the mapping.
- Cluster is small (n=48 total 10x cells) — limits statistical resolution of
  any cluster-restricted property.

**What would upgrade confidence**

- MapMyCells annotation transfer of MPN Calb1+ scRNA-seq data (Calb1-Cre or
  SDN-POA-focused dataset) to CLUS_1550 → AnnotationTransferEvidence
  (target F1 ≥ 0.80 at cluster level).
- MERFISH spatial channel inspection of Th in CLUS_1550 cells assigned to
  MBA:515 to determine whether non-zero Th signal originates from MPN cells
  or from the PVH/PVHap components of this multi-region cluster.
- Sub-regional spatial analysis to test whether CLUS_1550 MERFISH cells in
  MBA:515 occupy the dorsomedial SDN-POA cytoarchitectonic zone *(note:
  interpretive — based on classical SDN-POA position within MPN).*

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** `sdn_poa_calbindin_neuron` has
`definition_basis = CLASSICAL_NEUROCHEMICAL`. The classical description rests
on Nissl histology plus calbindin-D28K immunoreactivity delineating a
male-larger cluster of neurons in the medial preoptic area, with no TH-positive
cell bodies [1] [2]. Defining marker: Calb1. Negative marker: Th. Soma
location: MBA:515 (Medial preoptic nucleus). Sex bias: MALE_BIASED.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the
WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using
metadata-based scoring (region match, NT type, defining markers, sex bias
when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was
compared to the corresponding atlas-side value via the `property_comparisons`
schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT /
NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on
the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH
spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and
verbatim literature quotes in this report are validated against the evidencell
knowledge base at write time. Authored-prose evidence narratives are validated
against their source `evidence_items[*].explanation` fields. The pre-write
hook rejects any unresolvable identifier or unattributed blockquote. Specific
mapping limitations and caveats are documented per-candidate in the Discussion
section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:19+00:00 from
[kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_sdn_poa_calbindin_neuron_to_cs20230722_supt_0423 | ATLAS_METADATA | WEAK | atlas-internal |
| edge_sdn_poa_calbindin_neuron_to_cs20230722_clus_1550 | ATLAS_METADATA | WEAK | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Sexually dimorphic nucleus of the preoptic area (SDN-POA)
calbindin neuron → 1550 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_CLUS_1550] at LOW
confidence. Key support: ATLAS_METADATA (high Calb1, MPN primary soma,
male-biased MFR=3.35). Key caveats: MERFISH_REGISTRATION_UNCERTAINTY (SDN-POA
is a histological subnucleus within MPN, not separately resolvable in WMBv1)
and MARKER_NOT_SPECIFIC (Th=2.75 discordant with the classical Th-negative
defining property; Calb1 alone is not region-specific). SUPT_0423 is recorded
as a LOW-confidence supertype-level alternative covering the same cells, but
without the cluster-level sex_ratio and MPN-primary discrimination.

No Cell Ontology term currently assigned. The classical SDN-POA calbindin
neuron is a candidate for a new CL term capturing a male-biased Calb1+
Th-negative MPN neuron population homologous to human INAH3.

### Proposed experiments and follow-ups

**MapMyCells annotation transfer of an MPN Calb1+ scRNA-seq dataset against WMBv1.**
- **What:** MapMyCells annotation transfer using a Calb1-Cre / SDN-POA-focused
  MPN scRNA-seq dataset against CCN20230722.
- **Target:** F1 ≥ 0.80 at CLUSTER level for CLUS_1550 (and F1 against
  SUPT_0423 at supertype level).
- **Expected output:** `AnnotationTransferEvidence` items on both edges.
- **Resolves:** Q1 (do any clusters within SUPT_0423 show peak Calb1
  co-located with MBA:515 and male-biased sex ratio consistent with SDN-POA
  identity?); contributes to Q3.

**MERFISH spatial channel inspection of Th in CLUS_1550 cells assigned to MBA:515.**
- **What:** Inspect Th MERFISH counts in CLUS_1550 cells whose
  `parcellation_substructure` is MBA:515, separately from cells assigned to
  PVH / PVHap / other hypothalamic regions.
- **Target:** Determine whether Th expression in CLUS_1550 originates from
  MPN-resident cells (which would persist as a real discordance with the
  classical Th-negative assertion) or from the PVH/PVHap components of this
  multi-region cluster.
- **Expected output:** Atlas-internal property-comparison note refining the
  Th alignment, possibly upgrading from DISCORDANT to APPROXIMATE if Th
  signal is confined to non-MPN cells.
- **Resolves:** Q2.

**Sub-regional MERFISH spatial analysis within MBA:515 for SDN-POA dorsomedial position.**
- **What:** Inspect MERFISH cell coordinates within MBA:515 for SUPT_0423 /
  CLUS_1550 cells to test for sub-regional clustering consistent with the
  histologically defined dorsomedial SDN-POA position.
- **Target:** Identify a spatial subset of MPN-assigned CLUS_1550 cells that
  occupy the SDN-POA cytoarchitectonic zone, if such resolution is achievable.
- **Expected output:** Spatial inspection note; possibly a refined edge if
  SDN-POA can be sub-cluster-resolved.
- **Resolves:** Q3.

### Open questions

1. Do any clusters within SUPT_0423 show peak Calb1 co-located with MBA:515 (MPN) and male-biased sex ratio consistent with SDN-POA identity? *(currently answered partially by CLUS_1550, pending AT confirmation)*
2. Do CLUS_1550 cells at MBA:515 express Th, or does Th signal originate from PVH/PVHap components of this multi-region cluster?
3. Can sub-regional MERFISH spatial data distinguish SDN-POA dorsomedial cells from other MPN Calb1+ neurons within CLUS_1550?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Negri-Cesi 2015 | [26672480](https://pubmed.ncbi.nlm.nih.gov/26672480) | soma location |
| [2] | He et al. 2013 | [25206587](https://pubmed.ncbi.nlm.nih.gov/25206587) | soma location, Calb1 marker, Th-negative marker |
