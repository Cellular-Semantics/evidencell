# medial septal / diagonal band of Broca glutamatergic neuron — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml`*

---

## Introduction

Medial septal / diagonal band of Broca (MS-DBB) glutamatergic neurons are VGluT2-expressing (with some VGluT1) projection neurons whose somata sit in the medial septum and the diagonal band of Broca — i.e. *outside* the hippocampal formation — and whose axons project to hippocampal interneurons in stratum oriens near the alveus [1]. They are thought to participate in pacing hippocampal theta and discharge preferentially during locomotion [1, 2]. Electrophysiologically they form a heterogeneous population of fast-spiking, cluster-firing, burst-firing and slow-firing subgroups, with the cluster-firing phenotype reported as unique among MS-DBB cell classes and a candidate substrate for theta pacing [1, 2]. The cell type is retained in this hippocampus-centric graph because its synaptic targets lie in the hippocampal formation, even though its soma does not — the UBERON soma assignment (`UBERON:0002421` hippocampal formation) is used here as the nearest available umbrella term and is approximate.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | medial septum / diagonal band of Broca (extrahippocampal; UBERON:0002421 hippocampal formation used as nearest umbrella term); axonal target in hippocampus stratum oriens [UBERON:0005371] | [1] |
| Neurotransmitter | glutamatergic | [1] |
| Defining markers | Slc17a7 (VGluT1), Slc17a6 (VGluT2) | [1], [2] |
| Negative markers | Chat, Gad1 (i.e. neither cholinergic nor GABAergic) | [1] |
| Electrophysiology | Four VGluT2+ subgroups: fast-spiking, cluster-firing, burst-firing, slow-firing; cluster firing is unique to the glutamatergic population | [1], [2] |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Defining markers / negative markers / electrophysiology:** review of MS-DBB cellular composition · mouse · [1]
  > Glutamatergic neurons account for approximately 23% of the projections from the medial septum to the hippocampus (Colom et al. 2005). They are characterized by the expression of VGluT1 and/or VGluT2 and by the lack of expression of either ChAT or GAD (Sotty et al. 2003). Electrophysiologically, medial septal glutamatergic neurons form a highly diverse group (Huh et al. 2010; Sotty et al. 2003). The VGluT2 expressing medial septal neurons can be separated into four groups. The first and largest group is formed by the fast spiking neurons, showing only little action potential accommodation and sometimes spontaneous action potential firing (Huh et al. 2010). Remarkably, some of the fast-spiking glutamatergic neurons show a pronounced sag in response to a hyperpolarizing current injection. Similar intrinsic properties can be observed in GABAergic medial septal neurons (Huh et al. 2010). The second group of VGluT2-positive medial septal neurons exhibit a quite specific firing pattern. These neurons fire clusters of action potentials, which cannot be observed in other cell types of the medial septum. In these neurons, subthreshold intrinsic membrane oscillations, only a small or no sag and strong action potential accommodation is seen. The third group is formed by burst firing glutamatergic neurons, exhibiting a small or no sag (Huh et al. 2010). The neurons of the fourth group are slow firing. Following somatic current injection, they discharge at low rates with accommodating action potentials
  > — Müller & Remy 2017, Electrophysiological Properties and Firing Patterns · [1] <!-- quote_key: 21358766_0c242fdc -->

- **Axonal target / behavioural correlate:** review of MS-DBB cellular composition · mouse · [1]
  > Glutamatergic medial septal neurons mainly project to hippocampal interneurons (see Fig. 1) with their somata located in stratum oriens near the alveus. In vivo, the activity of glutamatergic medial septal neurons increases before the mouse initiates locomotion and is higher during running, when compared to resting phases.
  > — Müller & Remy 2017, Electrophysiological Properties and Firing Patterns · [1] <!-- quote_key: 21358766_01840c4a -->

- **Slc17a6 marker / firing properties:** review of medial septum in theta generation · [2]
  > Medial septal glutamatergic neurons expressing type 2 vesicular glutamate transporters (VGluT2) are likely involved in hippocampal theta generation. 132,135,140 They display a heterogeneous firing pattern, including fast, slow, burs, and clusterfiring (8-14 Hz, half of glutamatergic neurons) properties in slice. 135,137 Glutamatergic neurons also have intrinsic firing properties that may play an important role in pacing the hippocampus in vivo: they can discharge in recurrent clusters of action potentials, interspersed with intrinsically generated subthreshold membrane potential oscillations. 135
  > — Senova et al. 2020, Electrophysiological Properties and Firing Patterns · [2] <!-- quote_key: 212418354_02349d4e -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term. CL:0000679 (glutamatergic neuron) is too broad; no extant CL term names the medial septal / diagonal band of Broca glutamatergic projection neuron specifically.

---

## Results

A scan of WMBv1 (CCN20230722) at ranks 0 and 1, restricted to glutamatergic clusters with cells in hippocampal formation (MBA:1089), yielded no atlas cluster whose soma distribution falls within the medial septum or diagonal band of Broca. The ten candidates emitted by the discovery cohort are all hippocampal / entorhinal pyramidal populations or off-target thalamic / non-neuronal clusters whose somata sit *inside* the hippocampal formation or in neighbouring regions; none of them are extrahippocampal septal projection neurons of the kind defined by the classical literature. The atlas's MS-DBB glutamatergic population, if present, would be expected outside this region-filtered cohort, and no current evidence in this graph supports promotion of any candidate above UNCERTAIN.

Defining-marker evidence cannot be evaluated at this resolution: neither Slc17a7 (VGluT1) nor Slc17a6 (VGluT2) appears in the precomputed expression matrix or in Stage A's expression detail for any of the ten candidates, so the canonical VGluT1/VGluT2 signature cannot be tested. The only marker-based discriminator available is the classical *negative* marker Gad1, which serves as a coarse Glut-vs-GABA filter rather than as a positive identifier of MS-DBB cells. Several rank-0 entorhinal clusters (CLUS_0122, CLUS_0132, CLUS_0133) and rank-1 entorhinal supertypes (SUPT_0010, SUPT_0012, SUPT_0068) carry detectable Gad1 (0.59–0.92), which is inconsistent with a strictly non-GABAergic projection class and pushes them further from the classical type.

No candidates rise above UNCERTAIN. There are no survivor paragraphs — the cohort does not contain a credible MS-DBB representative. The full audit set is listed below.

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster / supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---:|---|---|---|
| `0332 L2/3 IT PPP Glut_1 [CS20230722_CLUS_0332]` | 82 | ⚪ UNCERTAIN | Hippocampal-formation L2/3 IT pyramidal cell; Gad1 = 0.00 | Eliminated (wrong cell class — local pyramidal, not septal projection) |
| `2689 TH Prkcd Grin2c Glut_14 [CS20230722_CLUS_2689]` | 942 | 🔴 LOW | Thalamic submedial / rhomboid nucleus; almost no hippocampal cells | Eliminated (extrahippocampal but wrong region — thalamus) |
| `0122 L2/3 IT ENT Glut_1 [CS20230722_CLUS_0122]` | 579 | 🔴 LOW | Entorhinal L2/3 IT pyramidal; Gad1 = 0.59 (cohort 30th pct) | Eliminated (wrong cell class; Gad1 detected) |
| `0132 L2/3 IT ENT Glut_4 [CS20230722_CLUS_0132]` | 5159 | 🔴 LOW | Entorhinal L2/3 IT pyramidal; Gad1 = 0.77 (cohort 55th pct) | Eliminated (wrong cell class; Gad1 detected) |
| `0133 L2/3 IT ENT Glut_5 [CS20230722_CLUS_0133]` | 903 | 🔴 LOW | Entorhinal L2/3 IT pyramidal; Gad1 = 0.71 (cohort 48th pct) | Eliminated (wrong cell class; Gad1 detected) |
| `0673 MG-POL-SGN Nts Glut_2 [CS20230722_SUPT_0673]` | 593 | 🔴 LOW | Thalamic / midbrain (suprageniculate); very few hippocampal cells | Eliminated (wrong region — thalamus/midbrain) |
| `1170 Astroependymal NN_2 [CS20230722_SUPT_1170]` | 66 | 🔴 REFUTED | Non-neuronal astroependymal supertype; cerebellum/medulla | Eliminated (non-neuronal; wrong region) |
| `0012 L5/6 IT TPE-ENT Glut_6 [CS20230722_SUPT_0012]` | 193 | 🔴 LOW | Presubiculum / parasubiculum L5/6 IT pyramidal; Gad1 = 0.23 | Eliminated (wrong cell class — local pyramidal) |
| `0010 L5/6 IT TPE-ENT Glut_4 [CS20230722_SUPT_0010]` | 1791 | 🔴 LOW | Entorhinal L5/6 IT pyramidal; Gad1 = 0.92 (cohort 71st pct) | Eliminated (wrong cell class; Gad1 detected) |
| `0068 ENTmv-PA-COAp Glut_3 [CS20230722_SUPT_0068]` | 963 | 🔴 LOW | Entorhinal medial / piriform-amygdalar Glut supertype; Gad1 = 0.60 | Eliminated (wrong cell class; Gad1 detected) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** MS-DBB glutamatergic neurons are defined here as VGluT1+ and/or VGluT2+ (Slc17a7, Slc17a6) projection neurons that lack Chat and Gad1, with somata in the medial septum and diagonal band of Broca and axonal targets on hippocampal interneurons in stratum oriens near the alveus [1, 2]. The `definition_basis` is `CLASSICAL_MULTIMODAL`: marker, neurotransmitter, electrophysiological, and connectivity criteria all draw on classical anatomy and slice-physiology literature. Cluster-firing in the 8–14 Hz range is reported as a discriminating intrinsic property of the glutamatergic subgroup [1, 2].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match against MBA:1089 hippocampal formation, glutamatergic NT type, and defining-marker presence where available). Full scoring rules: `workflows/map-cell-type.md`. Note that the region filter is anchored to the hippocampal formation (the axonal target), not to the medial septum (the somatic location), because MBA does not register septal nuclei into the hippocampal-formation hierarchy.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Slc17a7 and Slc17a6 were NOT_ASSESSED at all candidates because they are absent from the precomputed expression matrix and Stage A expression detail. Gad1 was the only marker with usable atlas-side numerics.

**Evidence base.** Ten candidates were assessed (5 rank-0 clusters + 5 rank-1 supertypes). All carry a single PARTIAL `ATLAS_METADATA` evidence item recording the candidate's hippocampal-formation `region_fraction_100um`. No annotation-transfer, bulk-correlation, patch-seq, or targeted-transcriptomic evidence is available for this node.

</details>

---

## Discussion

**Best candidate.** None. No candidate in the current cohort represents the medial septal / diagonal band of Broca glutamatergic projection neuron defined by the classical literature. The strongest *structural* match (CLUS_0332, hippocampal-formation L2/3 IT PPP with Gad1 = 0.00) is wrong on cell class — it is a local pyramidal cell, not a septal projection neuron — and the other candidates are either intrahippocampal/entorhinal pyramidal populations, off-target thalamic/midbrain clusters, or non-neuronal supertypes.

**Why the cohort lacks a credible candidate.** The discovery query is anchored on the *target* region of the classical type (hippocampal formation, MBA:1089) because that is where the cell's axons synapse, but the somata sit outside this region in medial septum / diagonal band of Broca. WMBv1 candidates are scored on soma location (the MERFISH spatial signal records soma position only — axonal projection targets are not represented), so the query as constructed cannot surface MS-DBB cells. The mapping is fundamentally limited by this query/biology mismatch, not by absence of an MS-DBB cluster in WMBv1 per se.

**What would change the picture.** A targeted re-query against the medial septum and diagonal band of Broca (MBA ancestors of the septal nuclear group) at ranks 0 and 1, restricted to glutamatergic NT type and screened for Slc17a6 expression where available, would surface the appropriate cohort. Patch-seq evidence linking electrophysiology (the cluster-firing / fast-spiking / burst-firing / slow-firing subgroup structure reported by Huh et al. 2010 and reviewed in [1, 2]) to transcriptomic identity would then be the most direct evidence to anchor the mapping. Cre-driver targeting of VGluT2+ septal projection neurons followed by transcriptomic profiling and cluster annotation transfer (e.g. against WMBv1) would provide the canonical direct-evidence path.

---

## References

[1] Müller & Remy 2017 · PMID:29250747 · doi:10.1007/s00441-017-2745-2
[2] Senova et al. 2020 · PMID:32132227 · doi:10.1136/jnnp-2019-322375

---

<!-- verdict-block-start: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_CLUS_0332 -->
```yaml
verdict:
  edge_id: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_CLUS_0332
  confidence: UNCERTAIN
  confidence_score: 0.15
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  rationale: |
    [tier:CUT] CLUS_0332 (0332 L2/3 IT PPP Glut_1) is a hippocampal-formation L2/3 intratelencephalic pyramidal cluster with soma fully inside the hippocampal formation; the classical MS-DBB glutamatergic projection neuron has its soma in the medial septum / diagonal band of Broca, projecting *to* hippocampal interneurons in stratum oriens. The classical cell class is therefore wrong, despite Gad1 being correctly near-zero and region_fraction_100um = 1.0 (the latter is misleading because the discovery query anchors on the axonal target rather than the soma).
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Atlas cluster soma is intrahippocampal (L2/3 IT PPP); classical type soma is in medial septum / diagonal band of Broca."
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: "Defining markers Slc17a7 and Slc17a6 are not available in precomputed expression; Gad1 is the only marker checked and only weakly discriminates."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_CLUS_2689 -->
```yaml
verdict:
  edge_id: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_CLUS_2689
  confidence: LOW
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  rationale: |
    [tier:CUT] CLUS_2689 (2689 TH Prkcd Grin2c Glut_14) is a thalamic submedial / rhomboid nucleus cluster (region_fraction_100um = 0.011); essentially no cells sit in hippocampal formation and none in medial septum. Wrong region and wrong cell class for an MS-DBB projection neuron.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Cluster soma in thalamus (submedial / rhomboid nucleus); classical type soma in medial septum / diagonal band of Broca."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_CLUS_0122 -->
```yaml
verdict:
  edge_id: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_CLUS_0122
  confidence: LOW
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  rationale: |
    [tier:CUT] CLUS_0122 (0122 L2/3 IT ENT Glut_1) is an entorhinal lateral L2/3 IT pyramidal cluster. Gad1 = 0.59 (cohort 30th percentile) is inconsistent with the classical non-GABAergic negative marker. Soma is intrahippocampal/entorhinal, not in medial septum.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Cluster soma in entorhinal cortex; classical type soma in medial septum / diagonal band of Broca."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Gad1 detected at 0.59 contradicts the classical negative-marker assertion."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_CLUS_0132 -->
```yaml
verdict:
  edge_id: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_CLUS_0132
  confidence: LOW
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  rationale: |
    [tier:CUT] CLUS_0132 (0132 L2/3 IT ENT Glut_4) is an entorhinal medial-dorsal L2/3 IT pyramidal cluster. Gad1 = 0.77 (cohort 55th percentile) contradicts the classical Gad1-negative criterion. Soma is intrahippocampal/entorhinal.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Cluster soma in entorhinal cortex; classical type soma in medial septum / diagonal band of Broca."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Gad1 detected at 0.77 contradicts the classical negative-marker assertion."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_CLUS_0133 -->
```yaml
verdict:
  edge_id: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_CLUS_0133
  confidence: LOW
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  rationale: |
    [tier:CUT] CLUS_0133 (0133 L2/3 IT ENT Glut_5) is an entorhinal lateral L2/3 IT pyramidal cluster. Gad1 = 0.71 (cohort 48th percentile) contradicts the Gad1-negative criterion. Soma is intrahippocampal/entorhinal, not septal.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Cluster soma in entorhinal cortex; classical type soma in medial septum / diagonal band of Broca."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Gad1 detected at 0.71 contradicts the classical negative-marker assertion."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_SUPT_0673 -->
```yaml
verdict:
  edge_id: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_SUPT_0673
  confidence: LOW
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  rationale: |
    [tier:CUT] SUPT_0673 (0673 MG-POL-SGN Nts Glut_2) is a thalamic / midbrain (suprageniculate / posterior medial) supertype with very few cells in hippocampal formation (region_fraction_100um = 0.12). NT type was not asserted on the atlas side, so glutamatergic alignment could not be checked at supertype level. Wrong region for an MS-DBB neuron.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Supertype soma in thalamus / midbrain; classical type soma in medial septum / diagonal band of Broca."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_SUPT_1170 -->
```yaml
verdict:
  edge_id: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_SUPT_1170
  confidence: REFUTED
  confidence_score: 0.01
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  rationale: |
    [tier:CUT] SUPT_1170 (1170 Astroependymal NN_2) is a non-neuronal astroependymal supertype concentrated in cerebellum, medulla, and area postrema (region_fraction_100um = 0.02). Wrong cell class (non-neuronal) and wrong region; cannot represent an MS-DBB glutamatergic projection neuron under any reading.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Non-neuronal supertype localised to cerebellum/medulla/area postrema; classical type is a neuron in medial septum / diagonal band of Broca."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_SUPT_0012 -->
```yaml
verdict:
  edge_id: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_SUPT_0012
  confidence: LOW
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  rationale: |
    [tier:CUT] SUPT_0012 (0012 L5/6 IT TPE-ENT Glut_6) is a presubiculum / parasubiculum L5/6 IT pyramidal supertype. Gad1 = 0.23 is in the discordant tier on the Gad1-negative criterion. Soma is intrahippocampal (parahippocampal subdivisions), not septal.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Supertype soma in presubiculum / parasubiculum; classical type soma in medial septum / diagonal band of Broca."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Gad1 = 0.23 weakly contradicts the classical Gad1-negative criterion."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_SUPT_0010 -->
```yaml
verdict:
  edge_id: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_SUPT_0010
  confidence: LOW
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  rationale: |
    [tier:CUT] SUPT_0010 (0010 L5/6 IT TPE-ENT Glut_4) is an entorhinal lateral L5/6 IT pyramidal supertype. Gad1 = 0.92 (cohort 71st percentile) strongly contradicts the Gad1-negative criterion. Soma is in entorhinal cortex, not medial septum.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Supertype soma in entorhinal cortex; classical type soma in medial septum / diagonal band of Broca."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Gad1 = 0.92 contradicts the classical Gad1-negative criterion."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_SUPT_0068 -->
```yaml
verdict:
  edge_id: edge_ms_dbb_glutamatergic_neuron_to_CS20230722_SUPT_0068
  confidence: LOW
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  rationale: |
    [tier:CUT] SUPT_0068 (0068 ENTmv-PA-COAp Glut_3) is an entorhinal medial / piriform-amygdalar / cortical-amygdalar Glut supertype. Gad1 = 0.60 (cohort 24th percentile) contradicts the Gad1-negative criterion. Soma is in entorhinal / piriform-amygdalar cortex, not medial septum.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Supertype soma in entorhinal medial / piriform-amygdalar / cortical-amygdalar cortex; classical type soma in medial septum / diagonal band of Broca."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Gad1 = 0.60 contradicts the classical Gad1-negative criterion."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->
