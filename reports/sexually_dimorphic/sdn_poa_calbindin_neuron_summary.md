# Sexually dimorphic nucleus of the preoptic area (SDN-POA) calbindin neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

The sexually dimorphic nucleus of the preoptic area (SDN-POA) is a cytoarchitectonically defined cluster of cells in the medial preoptic area of the rodent hypothalamus, larger in males than in females and implicated in the control of male sex behaviour [1][2]. It is delineated histologically by Nissl staining or, more selectively, by calbindin-D28K immunoreactivity, and contains no tyrosine hydroxylase (TH)-positive somata although TH-positive axons and synaptic profiles traverse it [2]. The nucleus is regarded as the rodent homolog of the third interstitial nucleus of the anterior hypothalamus (INAH3) in humans and has counterparts in sheep, rhesus macaque, and quail [2]. Mapping the SDN-POA calbindin neuron onto the WMBv1 taxonomy is of interest because, despite a well-established histological identity, this population has no dedicated single-cell transcriptomic identity in current whole-mouse-brain atlases.

### 3. Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:515] (named in source as SDN-POA) | [1][2] |
| Defining markers | Calb1 | [2] |
| Negative markers | Th (somatic; axonal TH present) | [2] |
| Definition basis | CLASSICAL_NEUROCHEMICAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical histology · rodent (rat/mouse) · [1][2]
  > The 2 best known dimorphic brain structures are the sexual dimorphic nucleus of the medial preoptic hypothalamic area (SDN-POA) in rodents, which correspond to the interstitial nucleus of the anterior hypothalamus (INAH) in humans, and the anteroventral periventricular (AVPV) nucleus. The first one controls male sex behavior and is larger in males than in females; the second one is critical for the cyclic control of ovulation and is larger in females than in males.
  > — Negri-Cesi 2015, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 14863067_fa51fcf7 -->

  > One of the well-defined sexually dimorphic structures in the brain is the sexually dimorphic nucleus, a cluster of cells located in the preoptic area of the hypothalamus. The rodent sexually dimorphic nucleus of the preoptic area can be delineated histologically using conventional Nissl staining or immunohistochemically using calbindin D28K immunoreactivity
  > — He et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_d6c3a647 -->

- **Defining marker (Calb1):** calbindin-D28K immunohistochemistry · rodent · [2]
  > The sexually dimorphic nucleus of the preoptic area is highlighted by calbindin-D28K immunoreactivity: no TH-positive cells were found, but fine axon-like projections/synaptic structures were seen
  > — He et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_17d4bd9d -->

- **Cross-species homology context:** [2]
  > The sexually dimorphic nucleus has been specifically defined in the brains of human and other mammalian and non-mammalian and includes the third interstitial nucleus of the anterior hypothalamus in humans (Allen et al., 1989)(Allen et al., 1990) , the ovine sexually dimorphic nucleus in the medial preoptic area (Roselli et al., 2004) , the medial preoptic and anterior hypothalamic regions in rhesus monkeys (Byne, 1998) , a specific area in the medial preoptic nucleus in quail (Viglietti‐Panzica et al., 1986) , and the sexually dimorphic nucleus of the preoptic area in rats (Gorski et al., 1978)(Gorski et al., 1980) . The human sexually dimorphic nucleus of the preoptic area is located in the medial part of the preoptic area, between the dorsolateral supraoptic nucleus and the rostral pole of the paraventricular nucleus (Hofman et al., 1989)
  > — He et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_1098a86b -->

</details>

### 4. Cell Ontology mapping

**No Cell Ontology term currently covers this type — candidate for a new CL term.**

The classical node notes flag this as a candidate for a new CL term covering the rodent SDN-POA calbindin population and its cross-species homologs.

---

## Results

Calbindin (Calb1)-expressing, male-biased candidate clusters in the medial preoptic nucleus [MBA:515] anchor a plausible but unconfirmed mapping to the BST-MPN Six3 Nrgn Gaba supertype family, with 0423 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_SUPT_0423] and its child 1550 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_CLUS_1550] offering the only MPN-primary supertype/cluster pair (see candidates table and property comparisons below). However, the SDN-POA is a histologically defined subnucleus within the broader medial preoptic nucleus and cannot be resolved as a distinct spatial domain in WMBv1 MERFISH data, so none of the candidate atlas clusters can be specifically equated with the SDN-POA itself.

### 4. Property alignment + Evidence support — Primary candidate pair (SUPT_0423 / CLUS_1550)

**Table 1 — Property comparison (0423 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_SUPT_0423] · supertype, and best child 1550 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_CLUS_1550]).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:515] | MPN n=113 / Hypothalamus [MBA:1097] n=295 / AHN [MBA:88] n=86 (region_fraction_100um=0.336; strict=0.140) | MPN n=39 / Hypothalamus [MBA:1097] n=46 / PVH [MBA:38] n=25 (region_fraction_100um=0.812; strict=0.458) | SUPT: APPROXIMATE; CLUS: CONSISTENT |
| NT type | not asserted | not asserted | GABA | NOT_ASSESSED |
| Calb1 expression | defining marker | 6.42 (cohort pct 0.771; DEFINING_SCOPED; child-coverage 1.000) | 6.66 (cohort pct 0.704) | CONSISTENT (both) |
| Th (negative) | absent in somata; axonal only | no atlas expression data | no atlas expression data | NOT_ASSESSED |
| Sex ratio | male-biased | not available | MFR=3.35 (male-biased) | CONSISTENT |

*(1 of 5 child clusters of SUPT_0423 — CLUS_1550 — shows MPN-primary location combined with male-biased MFR and high Calb1; the remaining children are not MPN-primary or were not surfaced in the candidates audit. Best match: CLUS_1550.)*

**Table 2 — Evidence support (SUPT_0423 + CLUS_1550).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + MERFISH location (SUPT_0423) | Atlas metadata | WEAK | Calb1=6.42 (DEFINING_SCOPED); MPN n=113 of 336 cells | atlas-internal |
| Atlas precomputed expression + MERFISH location (CLUS_1550) | Atlas metadata | WEAK | Calb1=6.66; MPN-primary (39/85 in MBA:515); MFR=3.35 male-biased | atlas-internal |

### 4. Property alignment + Evidence support — Secondary candidate (SUPT_0420)

**Table 1 — Property comparison (0420 BST-MPN Six3 Nrgn Gaba_1 [CS20230722_SUPT_0420]).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:515] | MPN n=289 / Hypothalamus [MBA:1097] n=315 / MPO [MBA:523] n=78 (region_fraction_100um=0.903; strict=0.759) | not assessed | CONSISTENT |
| NT type | not asserted | not asserted | not assessed | NOT_ASSESSED |
| Calb1 expression | defining marker | 6.53 (cohort pct 0.790; child-coverage 1.000) | not assessed | CONSISTENT |
| Th (negative) | absent in somata; axonal only | no atlas expression data | not assessed | NOT_ASSESSED |
| Sex ratio | male-biased | not available | not assessed | NOT_ASSESSED |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Table 2 — Evidence support (SUPT_0420).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + MERFISH location | Atlas metadata | PARTIAL | Calb1=6.53; MPN-primary (289/702; region_fraction_100um=0.903) | atlas-internal |

### 5. Candidate paragraphs

### 0423 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_SUPT_0423] · 🔴 LOW / ⚪ UNCERTAIN

Atlas precomputed expression data and MERFISH spatial registration place this supertype in a constellation of preoptic-region GABAergic populations with calbindin expression at supertype level (Calb1=6.42; DEFINING_SCOPED; cohort percentile 0.771), making it the only rank-1 candidate in which the medial preoptic nucleus contributes a non-trivial fraction of soma counts. This is the closest supertype-level match to the classical SDN-POA description (Calb1+ neurons in the medial preoptic nucleus) that the WMBv1 atlas offers, but the mapping is at best a broader correspondence — see property comparison table.

**Supporting evidence**
- Calbindin (Calb1) is the primary classical defining marker for SDN-POA neurons in rodent IHC studies [2]; its expression at supertype level on SUPT_0423 is in the upper third of the survival cohort (cohort percentile 0.771) and the marker is flagged DEFINING_SCOPED in atlas curation, meaning it discriminates within the parent subclass.
- The supertype's soma counts include 113 cells in the medial preoptic nucleus [MBA:515], consistent with the classical soma location for SDN-POA cells.
- All 5 of SUPT_0423's child clusters carry Calb1 expression (child-cluster coverage 1.000).

**Concerns**
- Location alignment is only APPROXIMATE at supertype level — strict `region_fraction: 0.140` against a `region_fraction_100um: 0.336` indicates that the bulk of SUPT_0423 soma sit outside the medial preoptic nucleus (the supertype also occupies hypothalamus [MBA:1097] and anterior hypothalamic nucleus [MBA:88]). The SUPT_0423 cohort cannot, on this evidence, be equated with SDN-POA neurons specifically.
- Calb1 is broadly expressed across hypothalamic and limbic GABAergic populations; its DEFINING_SCOPED tag means it discriminates within-subclass but is not a specific SDN-POA marker. Calb1 alone is insufficient to identify SDN-POA neurons (MARKER_NOT_SPECIFIC caveat).
- The SDN-POA is a histologically defined subnucleus within the broader medial preoptic nucleus; WMBv1 MERFISH cannot resolve it as a distinct spatial domain, so even an MPN-localised match could not be confirmed as SDN-POA-specific (MERFISH_REGISTRATION_UNCERTAINTY caveat).
- Th (a classical somatic-negative marker for SDN-POA [2]) is absent from atlas precomputed expression for this supertype, so the negative-marker constraint cannot be cross-checked at supertype level.

**Marker evidence provenance**
- **Calb1.** Established in the gathered literature by calbindin-D28K immunohistochemistry on the rodent SDN-POA, with the histological identification of the nucleus carried by the IHC stain itself [2]. There is no transcript-level primary citation in the present references for Calb1 in morphologically/cytoarchitectonically confirmed SDN-POA cells; the marker is protein-level only in the gathered evidence.
- **Th (negative).** The classical negative call is somatic: He et al. [2] explicitly report no TH-positive cells in the SDN-POA but describe TH-positive axon-like projections and synaptic structures within it. The atlas-side precomputed expression does not carry Th for this supertype, so the negative call cannot be cross-checked here.
- Calb1 is listed as DEFINING_SCOPED for SUPT_0423 with a supertype mean of 6.42 (above MIN_DETECTABLE), so there is no atlas annotation/expression discrepancy at supertype level. The discrepancy that matters lies one level up: a histologically defined SDN-POA subnucleus is collapsed into a broader BST-MPN supertype that also spans non-SDN regions.

**What would upgrade confidence**
- Spatial inspection of SUPT_0423 MERFISH cells inside [MBA:515] for sub-regional clustering consistent with the SDN-POA dorsomedial position, to determine whether any subset of SUPT_0423 cells co-localises with the histologically defined SDN-POA cytoarchitectonic zone.
- A focused transcriptomic dataset of calbindin-labelled or SDN-POA-microdissected cells, transferred by cluster annotation transfer to the WMBv1 taxonomy, would convert the supertype-level alignment into a defensible mapping (target: F1 ≥ 0.70 against SUPT_0423 or one of its children).
- Targeted literature search for transcript-level (e.g. ISH, transcriptomic) confirmation of Calb1 specifically in cytoarchitectonically confirmed SDN-POA cells, anchoring the marker beyond the IHC literature.

### 1550 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_CLUS_1550] · 🔴 LOW / ⚪ UNCERTAIN

Among the children of SUPT_0423, CLUS_1550 is the only cluster whose primary soma location is the medial preoptic nucleus [MBA:515] (39 of 85 cells; region_fraction_100um=0.812), and its male-biased sex ratio (MFR=3.35) aligns with the male-biased dimorphism of the classical SDN-POA. Calb1 is expressed at 6.66 (cohort percentile 0.704). This makes CLUS_1550 the best available cluster-level approximation to the SDN-POA calbindin population in the WMBv1 atlas, but the cluster also spans paraventricular hypothalamic nucleus [MBA:38] and is not MPN-restricted, and the negative-marker (Th) constraint cannot be confirmed.

**Supporting evidence**
- MERFISH spatial counts place CLUS_1550's largest soma cohort in the medial preoptic nucleus [MBA:515] (39 cells; region_fraction_100um=0.812; strict region_fraction=0.458), matching the classical SDN-POA soma location [1][2].
- Calb1 expression at 6.66 (cohort percentile 0.704) is consistent with the classical defining marker [2].
- The cluster's male-biased MFR (3.35) matches the male-biased dimorphism of the classical SDN-POA (larger in males [1]).
- The cluster is annotated as GABAergic by atlas curation.

**Concerns**
- Th (a classical somatic-negative marker [2]) shows precomputed mean expression 2.75 in CLUS_1550, in apparent conflict with the classical assertion. The classical negative call is restricted to somata in the SDN-POA itself, and CLUS_1550 includes cells in PVH/PVHap (where Th-expressing populations are well documented), so the Th signal may originate from the non-MPN component of the cluster rather than from MPN cells. Spatial inspection of the Th channel for CLUS_1550 cells assigned to MBA:515 would be needed to resolve this.
- Location is CONSISTENT but not MPN-restricted: 25 of 110 CLUS_1550 soma sit in paraventricular hypothalamic nucleus [MBA:38] and a further 11 in unspecified hypothalamus [MBA:1097], so the cluster spans more than the medial preoptic nucleus.
- The SDN-POA is a subnucleus within MPN that cannot be resolved as a distinct MERFISH spatial domain in WMBv1; CLUS_1550 is the best available MPN-primary Calb1+ male-biased cluster but cannot be confirmed to occupy the SDN-POA cytoarchitectonic zone specifically (MERFISH_REGISTRATION_UNCERTAINTY caveat).
- Calb1 is broadly expressed; its presence on CLUS_1550 is consistent with but not specific for SDN-POA identity (MARKER_NOT_SPECIFIC caveat).
- An auto-repredication note flags CLUS_1550 as previously carrying the deprecated `evidencell:PartialOverlapMatch` predicate (auto-migrated to `skos:closeMatch` 2026-05-26); curator review recommended.

**Marker evidence provenance**
- **Calb1.** Protein-level histology (calbindin-D28K IHC) is the primary evidence in the gathered literature [2]; no transcript-level primary citation for Calb1 in cytoarchitectonically confirmed SDN-POA cells is present. Marker is consistent with cluster-level mean expression but not specific.
- **Th (negative).** Classical assertion is somatic-absent in SDN-POA but axonal-present [2]. CLUS_1550 spans multiple anatomical regions and the precomputed mean (2.75) cannot be apportioned across components without spatial channel inspection. Discrepancy is real and surfaces in the Concerns list above.

**What would upgrade confidence**
- MERFISH spatial channel inspection of the Th signal for CLUS_1550 cells assigned to MBA:515 to determine whether Th expression co-occurs with MPN soma or originates from the PVH/PVHap component of this cluster.
- Sub-regional MERFISH spatial analysis within [MBA:515] to test whether a subset of CLUS_1550 cells form a dorsomedial cluster consistent with the histologically defined SDN-POA position.
- A targeted transcriptomic dataset of SDN-POA Calb1+ neurons (e.g. microdissection or Calb1-driver-targeted cells from the medial preoptic area) transferred by cluster annotation transfer to the WMBv1 taxonomy, with F1 ≥ 0.70 against CLUS_1550 or its supertype as the target.

### 0420 BST-MPN Six3 Nrgn Gaba_1 [CS20230722_SUPT_0420] · 🔴 LOW / ⚪ UNCERTAIN

This supertype carries the highest medial-preoptic concentration of any candidate in the audited set (region_fraction_100um=0.903; strict region_fraction=0.759; 289 of 702 soma counted at MBA:515) with Calb1 expressed at 6.53 (cohort percentile 0.790; child-cluster coverage 1.000). It is a credible MPN-anchored alternative to SUPT_0423 for a broader SDN-POA-containing population, but no child-cluster breakdown was carried into this audit, no sex-ratio assessment is available at supertype level, and the same MERFISH-resolution limitation prevents specific equation with the SDN-POA subnucleus.

**Supporting evidence**
- MERFISH spatial counts place the bulk of SUPT_0420 soma in the medial preoptic nucleus [MBA:515] (289 cells out of 526 total; region_fraction_100um=0.903), the strongest MPN concentration of any audited candidate.
- Calb1 expression at 6.53 (cohort percentile 0.790) is consistent with the classical defining marker [2], with all child clusters expressing Calb1 (child-cluster coverage 1.000).

**Concerns**
- Sex ratio is not assessed at supertype level; without a male-biased MFR signal on at least one child cluster, the male-biased dimorphism of the classical SDN-POA cannot be confirmed for this supertype.
- No child-cluster breakdown is in scope for this audit; the supertype-level signal does not localise to a specific child.
- The MERFISH-resolution limitation applies: SDN-POA cannot be resolved as a distinct spatial domain within MPN, so even the strongest MPN-concentration signal does not specifically identify SDN-POA cells (MERFISH_REGISTRATION_UNCERTAINTY).
- Th is absent from atlas precomputed expression for this supertype, so the negative-marker constraint cannot be cross-checked.

**Marker evidence provenance**
- **Calb1.** As for the other candidates, protein-level IHC is the primary classical evidence [2]; no transcript-level primary citation in morphologically confirmed SDN-POA cells is present. Supertype-level mean expression is above MIN_DETECTABLE and there is no atlas annotation/expression discrepancy at supertype level.

**What would upgrade confidence**
- Identification and audit of SUPT_0420 child clusters in [MBA:515] with explicit male-biased MFR — currently the strongest gap is that the supertype-level MPN concentration is not yet matched to a specific male-biased child cluster.
- A focused transcriptomic dataset of SDN-POA Calb1+ neurons transferred by cluster annotation transfer to the WMBv1 taxonomy, to test whether the source cells land on SUPT_0420 or SUPT_0423.

### 4c. Candidates audited (full top-K)

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0423 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_SUPT_0423] | — | 1215 | ⚪ UNCERTAIN | Only MPN-bearing rank-1 candidate; Calb1=6.42 DEFINING_SCOPED | Primary (supertype) |
| 1550 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_CLUS_1550] | 0423 BST-MPN Six3 Nrgn Gaba_4 | 215 | ⚪ UNCERTAIN | MPN-primary child of SUPT_0423; MFR=3.35; Calb1=6.66 | Primary (best child) |
| 0420 BST-MPN Six3 Nrgn Gaba_1 [CS20230722_SUPT_0420] | — | 526 | ⚪ UNCERTAIN | Highest MPN concentration (region_fraction_100um=0.903); Calb1=6.53 | Secondary (broader MPN match) |
| 0422 BST-MPN Six3 Nrgn Gaba_3 [CS20230722_SUPT_0422] | — | 1836 | 🔴 LOW | MPN-primary supertype but Calb1=5.49 lower; no sex-ratio audit | Eliminated (lower Calb1; no sex-ratio confirmation) |
| 0421 BST-MPN Six3 Nrgn Gaba_2 [CS20230722_SUPT_0421] | — | 293 | 🔴 LOW | MPN-primary supertype; Calb1=4.86 modest | Eliminated (lower Calb1; no sex-ratio confirmation) |
| 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] | — | 933 | 🔴 LOW | Periventricular preoptic; Calb1=4.16 only APPROXIMATE | Eliminated (PVpo-dominant; Calb1 modest) |
| 1542 BST-MPN Six3 Nrgn Gaba_3 [CS20230722_CLUS_1542] | 0422 BST-MPN Six3 Nrgn Gaba_3 | 109 | 🔴 LOW | Calb1=3.26 APPROXIMATE; MPN tertiary | Eliminated (Calb1 below cohort median) |
| 0360 MEA-BST Lhx6 Nfib Gaba_4 [CS20230722_SUPT_0360] | — | 339 | 🔴 LOW | High Calb1 (8.68) but MEA-BST origin; MPN secondary | Eliminated (wrong subclass — MEA-BST lineage) |
| 1304 MEA-BST Lhx6 Nfib Gaba_5 [CS20230722_CLUS_1304] | 0361 MEA-BST Lhx6 Nfib Gaba_5 | 57 | 🔴 LOW | Calb1=10.28 but MEA-BST lineage | Eliminated (wrong subclass — MEA-BST lineage) |
| 1305 MEA-BST Lhx6 Nfib Gaba_5 [CS20230722_CLUS_1305] | 0361 MEA-BST Lhx6 Nfib Gaba_5 | 92 | 🔴 LOW | Calb1=8.89 but MEA-BST lineage; AVPV secondary | Eliminated (wrong subclass — MEA-BST lineage) |
| 1303 MEA-BST Lhx6 Nfib Gaba_4 [CS20230722_CLUS_1303] | 0360 MEA-BST Lhx6 Nfib Gaba_4 | 41 | 🔴 LOW | Calb1=8.52 but MEA-BST lineage; PD secondary | Eliminated (wrong subclass — MEA-BST lineage) |
| 1310 MEA-BST Lhx6 Nfib Gaba_5 [CS20230722_CLUS_1310] | 0361 MEA-BST Lhx6 Nfib Gaba_5 | 232 | 🔴 LOW | Calb1=7.37 but MEA-BST lineage; pallidum secondary | Eliminated (wrong subclass — MEA-BST lineage) |

12 edges audited; the eight `evidencell:UncertainRelationship` cuts are listed for audit only.

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The SDN-POA calbindin neuron is defined here on a CLASSICAL_NEUROCHEMICAL basis: calbindin-D28K immunoreactivity on cytoarchitectonically delineated SDN-POA neurons in rodent medial preoptic nucleus, with somatic Th absent and a male-biased dimorphism in nucleus size [1][2]. The node has no transcript-level primary citation for either Calb1 or Th in the gathered evidence; both are protein-level histological assertions in rodent material.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match against MBA:515, sex bias = male, defining marker = Calb1). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:14:04+00:00 from [kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_sdn_poa_calbindin_neuron_to_cs20230722_supt_0423 | ATLAS_METADATA | WEAK | atlas-internal |
| edge_sdn_poa_calbindin_neuron_to_cs20230722_clus_1550 | ATLAS_METADATA | WEAK | atlas-internal |
| edge_sdn_poa_calbindin_neuron_to_CS20230722_CLUS_1304 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sdn_poa_calbindin_neuron_to_CS20230722_CLUS_1305 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sdn_poa_calbindin_neuron_to_CS20230722_CLUS_1303 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sdn_poa_calbindin_neuron_to_CS20230722_CLUS_1310 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sdn_poa_calbindin_neuron_to_CS20230722_CLUS_1542 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sdn_poa_calbindin_neuron_to_CS20230722_SUPT_0360 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sdn_poa_calbindin_neuron_to_CS20230722_SUPT_0420 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sdn_poa_calbindin_neuron_to_CS20230722_SUPT_0422 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sdn_poa_calbindin_neuron_to_CS20230722_SUPT_0421 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sdn_poa_calbindin_neuron_to_CS20230722_SUPT_0486 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

### 6. Best candidate + caveats summary

**Primary mapping:** Sexually dimorphic nucleus of the preoptic area (SDN-POA) calbindin neuron → 0423 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_SUPT_0423] (supertype) with best child 1550 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_CLUS_1550] at UNCERTAIN confidence. Key support: medial-preoptic primary soma location with Calb1 expression at supertype level and a male-biased sex ratio on the best child cluster. Key caveats: MERFISH_REGISTRATION_UNCERTAINTY (SDN-POA cannot be resolved as a distinct spatial domain within MPN in WMBv1) and MARKER_NOT_SPECIFIC (Calb1 alone does not discriminate SDN-POA cells from other MPN Calb1+ populations); the Th somatic-negative call cannot be confirmed at atlas resolution.

No Cell Ontology term currently covers this type. The classical node carries a note flagging this as a candidate for a new CL term that would cover the rodent SDN-POA calbindin population together with its cross-species homologs (INAH3 in humans, ovine SDN, rhesus medial preoptic area, quail SDN [2]).

### 7. Proposed experiments and follow-ups

- **What:** spatial inspection of MERFISH cells (any SUPT_0423 / CLUS_1550 child cluster) inside [MBA:515] for sub-regional clustering consistent with the dorsomedial position of the histologically defined SDN-POA.
  - **Target:** identification of a contiguous Calb1+ Th-negative dorsomedial sub-cluster of CLUS_1550 / SUPT_0423 within MBA:515.
  - **Expected output:** spatial annotation that could be added as additional `property_comparisons` entries on the edges, or as new spatially refined edges if a sub-cluster is identified.
  - **Resolves:** the SDN-POA-vs-MPN-Calb1+ identity question for both SUPT_0423 and CLUS_1550 (open question 1 and 2).

- **What:** MERFISH Th-channel inspection of CLUS_1550 cells assigned to MBA:515.
  - **Target:** determination of whether the cluster-level mean Th=2.75 originates from MPN soma or from the PVH/PVHap components of this multi-region cluster.
  - **Expected output:** updated `property_comparisons` row for `negative_marker_Th` on CLUS_1550 with spatially apportioned values.
  - **Resolves:** open question 2.

- **What:** cluster annotation transfer of an MPN/SDN-POA Calb1+ transcriptomic dataset (e.g. Calb1-Cre-targeted or SDN-POA-microdissected cells) to the WMBv1 taxonomy.
  - **Target:** F1 ≥ 0.70 against SUPT_0423 (or SUPT_0420), with a child-cluster-level F1 ≥ 0.50 against CLUS_1550 (or an SUPT_0420 child) and a clean Purity / Coverage signal.
  - **Expected output:** `AnnotationTransferEvidence` items added to the relevant edges.
  - **Resolves:** the central uncertainty across all surviving candidates — would convert supertype-level alignment into a defensible cluster-level mapping.

- **What:** targeted literature search for transcript-level (ISH, transcriptomic) confirmation of Calb1 in cytoarchitectonically confirmed SDN-POA cells.
  - **Target:** primary-source transcript-level citation for Calb1 on SDN-POA neurons.
  - **Expected output:** `LiteratureEvidence` (transcript-level) added to the classical node.
  - **Resolves:** the marker-provenance gap (Calb1 is currently protein-level only).

### 8. Open questions

1. Do any clusters within SUPT_0423 show peak Calb1 co-located with MBA:515 (medial preoptic nucleus) and male-biased sex ratio consistent with SDN-POA identity?
2. Do CLUS_1550 cells at MBA:515 express Th, or does Th signal originate from PVH/PVHap components of this cluster?
3. Can sub-regional MERFISH spatial data distinguish SDN-POA dorsomedial cells from other MPN Calb1+ neurons within CLUS_1550?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Negri-Cesi 2015 — *Bisphenol A Interaction With Brain Development and Functions* | [26672480](https://pubmed.ncbi.nlm.nih.gov/26672480) | soma location |
| [2] | He et al. 2013 — *Development of the sexually dimorphic nucleus of the preoptic area and the influence of estrogen-like compounds* | [25206587](https://pubmed.ncbi.nlm.nih.gov/25206587) | soma location, defining marker (Calb1), negative marker (Th), cross-species homology |

---

<!-- verdict-block-start: edge_sdn_poa_calbindin_neuron_to_cs20230722_supt_0423 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.25
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:STRONGEST] CS20230722_SUPT_0423 is the only rank-1 candidate
    where the medial preoptic nucleus [MBA:515] contributes a non-trivial
    fraction of soma (region_fraction_100um: 0.336; strict region_fraction:
    0.140) and Calb1=6.42 (DEFINING_SCOPED; cohort percentile 0.771;
    child-coverage 1.000) matches the primary classical defining marker.
    The SDN-POA is a histologically defined subnucleus within MPN and
    cannot be resolved as a distinct spatial domain in WMBv1 MERFISH data;
    Calb1 alone is not specific for SDN-POA identity.
  reconciliation_note: >
    Paired with best-child edge to CS20230722_CLUS_1550 (the only
    MPN-primary child of this supertype with male-biased MFR); see report.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        The SDN-POA is a histologically defined subnucleus within MPN, not
        resolvable as a distinct spatial domain in WMBv1 MERFISH data.
        Matching is possible only at MPN level (SUPT_0423 MBA:515, n=113);
        SDN-POA cells cannot be distinguished from other MPN Calb1
        neurons.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Calb1 is expressed across many brain regions and is DEFINING_SCOPED
        (not DEFINING) on CS20230722_SUPT_0423. Calb1 alone is insufficient
        to identify SDN-POA neurons specifically; the supertype spans BST,
        MPN, AHN, and PVN.
  proposed_experiments:
    - >
      Spatial inspection of CS20230722_SUPT_0423 MERFISH cells inside
      MBA:515 for sub-regional clustering consistent with the dorsomedial
      SDN-POA position.
    - >
      Cluster annotation transfer of an MPN/SDN-POA Calb1+ transcriptomic
      dataset to the WMBv1 taxonomy, targeting F1 >= 0.70 against
      CS20230722_SUPT_0423.
  unresolved_questions:
    - >
      Do any clusters within CS20230722_SUPT_0423 show peak Calb1
      co-located with MBA:515 and male-biased sex ratio consistent with
      SDN-POA identity?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sdn_poa_calbindin_neuron_to_cs20230722_clus_1550 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.3
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:NEXT] CS20230722_CLUS_1550 is the only child of CS20230722_SUPT_0423
    whose primary soma location is MBA:515 (region_fraction_100um: 0.812;
    strict region_fraction: 0.458), and its MFR=3.35 male-biased sex
    ratio aligns with the male-biased SDN-POA dimorphism. Calb1=6.66
    (cohort percentile 0.704) matches the classical defining marker.
    Concerns: Th=2.75 is discordant with the classical somatic-negative
    Th assertion, but the cluster spans MBA:515, MBA:1097, and MBA:38, so
    the Th signal may originate from non-MPN cells; SDN-POA cannot be
    resolved as a distinct MERFISH spatial domain within MPN.
  reconciliation_note: >
    Paired with parent supertype edge to CS20230722_SUPT_0423; see report.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        SDN-POA is a histologically defined subnucleus within MPN; WMBv1
        MERFISH cannot resolve it as a distinct spatial domain.
        CS20230722_CLUS_1550 is the best available MPN-primary Calb1+
        male-biased cluster but cannot be confirmed to occupy the SDN-POA
        cytoarchitectonic zone specifically.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Th=2.75 in CS20230722_CLUS_1550 is discordant with the classical
        somatic-Th-negative assertion. The cluster spans MBA:515,
        MBA:1097, and MBA:38; the Th signal may originate from the PVH /
        PVHap component rather than from MPN cells, but the apportionment
        cannot be made without spatial channel inspection.
    - caveat_type: OTHER
      description: >
        [AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated from
        deprecated evidencell:PartialOverlapMatch to skos:closeMatch by
        refresh_predicates.py. Curator review recommended; this verdict
        leaves the predicate as evidencell:UncertainRelationship pending
        the spatial inspection above.
  proposed_experiments:
    - >
      MERFISH Th-channel spatial inspection of CS20230722_CLUS_1550 cells
      assigned to MBA:515, to determine whether Th expression co-occurs
      with MPN cells or originates from the PVH / PVHap component.
    - >
      Sub-regional MERFISH spatial analysis within MBA:515 to test whether
      a subset of CS20230722_CLUS_1550 cells form a dorsomedial sub-cluster
      consistent with the histologically defined SDN-POA position.
    - >
      Cluster annotation transfer of MPN Calb1+ transcriptomic data
      (Calb1-driver-targeted or SDN-POA-focused dataset) to assess F1
      against CS20230722_CLUS_1550 (target F1 >= 0.50 at cluster level).
  unresolved_questions:
    - >
      Do CS20230722_CLUS_1550 cells at MBA:515 express Th, or does Th
      signal originate from PVH / PVHap components of this cluster?
    - >
      Can sub-regional MERFISH spatial data distinguish SDN-POA dorsomedial
      cells from other MPN Calb1+ neurons within CS20230722_CLUS_1550?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sdn_poa_calbindin_neuron_to_CS20230722_SUPT_0420 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.25
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:WEAKEST] CS20230722_SUPT_0420 has the highest MPN concentration
    of any audited candidate (region_fraction_100um: 0.903; strict
    region_fraction: 0.759) with Calb1=6.53 (cohort percentile 0.790;
    child-coverage 1.000). No child-cluster breakdown was carried into
    this audit and no sex-ratio assessment is available at supertype
    level, so the male-biased dimorphism of the classical SDN-POA cannot
    be confirmed; SDN-POA cannot be resolved as a distinct MERFISH
    spatial domain within MPN.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        SDN-POA is a histologically defined subnucleus within MPN that
        cannot be resolved as a distinct spatial domain in WMBv1 MERFISH
        data. The strong MPN concentration of CS20230722_SUPT_0420 does
        not specifically identify SDN-POA cells.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Calb1 is broadly expressed across hypothalamic and limbic
        GABAergic populations; its presence on CS20230722_SUPT_0420 is
        consistent with but not specific for SDN-POA identity.
  proposed_experiments:
    - >
      Audit of CS20230722_SUPT_0420 child clusters at MBA:515 for
      male-biased MFR, to test whether a specific child cluster matches
      the male-biased SDN-POA dimorphism.
    - >
      Cluster annotation transfer of an MPN / SDN-POA Calb1+ transcriptomic
      dataset to the WMBv1 taxonomy to test whether source cells land on
      CS20230722_SUPT_0420 vs CS20230722_SUPT_0423.
  unresolved_questions:
    - >
      Which children of CS20230722_SUPT_0420 in MBA:515 show male-biased
      sex ratio consistent with the SDN-POA dimorphism?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sdn_poa_calbindin_neuron_to_CS20230722_CLUS_1304 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] CS20230722_CLUS_1304 belongs to the MEA-BST Lhx6 Nfib Gaba
    lineage rather than the BST-MPN Six3 Nrgn Gaba lineage that anchors
    the MPN-primary candidates; although Calb1=10.28 is high and
    region_fraction_100um: 0.605 includes MBA:515, the dominant
    anatomical assignment is non-MPN and the subclass is inconsistent
    with the classical SDN-POA's medial preoptic identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sdn_poa_calbindin_neuron_to_CS20230722_CLUS_1305 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] CS20230722_CLUS_1305 belongs to the MEA-BST Lhx6 Nfib Gaba
    lineage and its secondary soma cohort is in MBA:272 (anteroventral
    periventricular nucleus), a female-biased structure distinct from
    the male-biased SDN-POA; Calb1=8.89 alone does not rescue the
    subclass mismatch.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sdn_poa_calbindin_neuron_to_CS20230722_CLUS_1303 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] CS20230722_CLUS_1303 belongs to the MEA-BST Lhx6 Nfib Gaba
    lineage with a secondary soma cohort in MBA:914 (posterodorsal
    preoptic nucleus); the lineage and dominant anatomical signal are
    inconsistent with the classical SDN-POA's medial preoptic identity
    despite Calb1=8.52.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sdn_poa_calbindin_neuron_to_CS20230722_CLUS_1310 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] CS20230722_CLUS_1310 belongs to the MEA-BST Lhx6 Nfib Gaba
    lineage with a secondary soma cohort in MBA:803 (pallidum), distant
    from the classical SDN-POA in the medial preoptic nucleus; subclass
    mismatch not rescued by Calb1=7.37.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sdn_poa_calbindin_neuron_to_CS20230722_CLUS_1542 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] CS20230722_CLUS_1542 sits in the correct BST-MPN Six3 Nrgn
    Gaba lineage but Calb1=3.26 (cohort percentile 0.408) is below the
    cohort median, and the tertiary anatomical assignment to MBA:515
    (after MBA:1097 and MBA:88) is weaker than its siblings.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sdn_poa_calbindin_neuron_to_CS20230722_SUPT_0360 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] CS20230722_SUPT_0360 carries high Calb1=8.68 (cohort
    percentile 0.971; child-coverage 1.000) but belongs to the
    MEA-BST Lhx6 Nfib Gaba lineage rather than the MPN-primary BST-MPN
    Six3 Nrgn Gaba lineage; the dominant soma cohort sits outside the
    medial preoptic nucleus.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sdn_poa_calbindin_neuron_to_CS20230722_SUPT_0422 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] CS20230722_SUPT_0422 sits in the BST-MPN Six3 Nrgn Gaba
    lineage with MPN-primary location (region_fraction_100um: 0.768) but
    Calb1=5.49 (cohort percentile 0.686) is lower than its sibling
    supertypes CS20230722_SUPT_0420 and CS20230722_SUPT_0423, and no
    sex-ratio audit was carried at supertype level.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sdn_poa_calbindin_neuron_to_CS20230722_SUPT_0421 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] CS20230722_SUPT_0421 sits in the BST-MPN Six3 Nrgn Gaba
    lineage with MPN-primary location (region_fraction_100um: 0.671) but
    Calb1=4.86 (cohort percentile 0.590) is modest, and the supertype is
    less anatomically concentrated in MBA:515 than CS20230722_SUPT_0420
    or CS20230722_SUPT_0423.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sdn_poa_calbindin_neuron_to_CS20230722_SUPT_0486 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] CS20230722_SUPT_0486 (PVpo-VMPO-MPN Hmx2 Gaba_5) is
    primarily a periventricular preoptic supertype with its largest soma
    cohort outside MBA:515 (strict region_fraction: 0.197); Calb1=4.16
    (cohort percentile 0.486; APPROXIMATE alignment) is below the
    cohort median.
```
<!-- verdict-block-end -->
