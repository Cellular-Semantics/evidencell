# BNST anterolateral group Type III CRF neuron — WMBv1 Mapping Report
*2026-09-11 · Source: `/Users/do12/Documents/GitHub/evidencell_content/evidencell_1/kb/graphs/sexually_dimorphic/bnstalg_type_iii_crf_neuron.yaml`*

---

## Introduction

Type III neurons of the anterolateral cell group of the bed nucleus of the stria terminalis (BNSTALG) are GABAergic, putative corticotropin-releasing factor (CRF) neurons: about 95% of them express Crh transcripts and they carry a distinctive ion-channel profile that correlates with their electrophysiological behaviour [2]. They are distinguished from parvocellular CRF neurons of the paraventricular nucleus by Oxtr expression and the absence of Oxt transcripts [2], which makes them a distinct extra-hypothalamic CRF class and a useful test of whether an atlas cluster can resolve a physiologically defined BNST type.

**Location note.** WMBv1 location data derives from MERFISH spatial registration and records **soma position** only. Axonal and dendritic projection targets are not reflected in atlas cluster location fields and are not used in mapping assessments. This matters here because the classical evidence concerns recorded somata in the BNST (mostly the oval nucleus, with some cells in the juxtacapsular and anterolateral nuclei [1]), and the BNST sits against the pallidum and striatum, so soma-position scatter across those neighbouring painted regions is expected at cluster level.

| Property | Value | References |
|---|---|---|
| Soma location | bed nucleus of stria terminalis [UBERON:0001880] (anterolateral cell group, BNSTALG) | [1], [2] |
| NT | GABAergic | [2] |
| Markers | Crh, Oxtr, Gad1, Cacna1i (Cav3.3), Hcn4, Kcnd2 (Kv4.2), Kcnj12 (Kir2.2), Kcnj4 (Kir2.3) | Crh [2], [3]; Oxtr [2]; Gad1 [2]; Cacna1i, Hcn4, Kcnd2, Kcnj12, Kcnj4 [1] |
| Negative markers | Oxt, Cacna1g (Cav3.1), Kcna4 (Kv1.4), Htr7, Slc17a7, Slc17a6, Slc17a8 | — |
| Neuropeptides | Crh | [2] |
| CL term | corticotropin-releasing neuron [CL:4072021] (BROAD) | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** recording-site report · rat BNST · [1]
  > the majority of neurons recorded were located within the boundaries of the oval nucleus (BNSTov) of the BNST, however, several cells were recorded that were located in the juxtacapsular (BNSTju) and anterolateral nuclei (BNSTal).
  > — Hazra et al. 2011, recording_location · [1] <!-- quote_key: 8615463_e974a9fd -->
- **NT type and Crh / Gad1 / Oxtr markers:** transcript-level screening of Type I-III neurons · rat BNST · [2]
  > Previously, we have shown that three physiologically and genetically distinct subclasses of neurons are present in the BNST ALG , Type I-III (Hammack et al., 2007;(Hazra et al., 2011). Type III BNST ALG neurons are putative CRF neurons, since the majority (95%) of these neurons express mRNA transcripts for CRF, and display a unique ion channel expression pattern that correlates with their electrophysiological features (Hazra et al., 2011). To determine if CRF neurons of the BNST ALG share a phenotype with parvocellular CRF neurons of the PVN we screened Type I-III BNST neurons for the presence of GAD67 and VGLUT1-3 transcripts. Significantly, all BNST ALG neurons tested, irrespective of cell type, expressed GAD67 mRNA transcripts, but none of these neurons expressed transcripts for VGLUT1-3. These findings confirmed our immunohistochemical observations that CRF neurons in the BNST ALG have a predominantly GABAergic phenotype
  > — Dabrowska et al. 2013, Molecular identity and markers · [2] <!-- quote_key: 4940077_5b783374 -->
- **Oxtr marker and Oxt negative marker:** transcript-level screening, contrast with PVN parvocellular CRF neurons · rat · [2]
  > . Significantly, unlike parvocellular CRF neurons that showed 83% co-expression with OT mRNA transcripts, none of the Type III CRF neurons tested co-expressed OT. Conversely, whereas 95% of Type III neurons expressed transcripts for OTR (18/19), no parvocellular CRF neurons expressed OTR transcripts.
  > — Dabrowska et al. 2013, Molecular identity and markers · [2] <!-- quote_key: 4940077_383bf7ef -->
- **Cacna1i (Cav3.3) marker and Cacna1g (Cav3.1) negative marker:** channel-subunit transcript profiling · rat BNST · [1]
  > Type I-III neurons also showed distinct distribution patterns for the I T channel subunits. Hence, Ca v 3.3 mRNA was expressed in 100% of Type III neurons, and 47% of Type II neurons, whereas only 17% of Type I neurons expressed this subunit. Transcripts for Ca v 3.1 were expressed in 91% of Type II neurons, but were not expressed in either Type I or III neurons.
  > — Hazra et al. 2011, cav3_distribution · [1] <!-- quote_key: 8615463_a14b307e -->
- **Hcn4, Cacna1i, Kcnd2 and Kir2 channel markers:** single-cell channel-subunit cluster profile · rat BNST · [1]
  > Similarly, another subgroup of neurons (n = 9) was characterized by their expression of transcripts for only the HCN4 subunit, together with Ca v 3.3, K v 4.2, and Kir2.1, 2.2 and 2.3 subunits, and these neurons corresponded to 9/11 of the Type III neurons recorded.
  > — Hazra et al. 2011, type3_cluster_profile · [1] <!-- quote_key: 8615463_6a67aab1 -->
- **Kcnj12 (Kir2.2) and Kcnj4 (Kir2.3) markers:** channel-subunit transcript profiling · rat BNST · [1]
  > Hence, Kir2.1 expression was highest (83%) in Type I neurons compared to other two subtypes (29% in Type II, and 45% in Type III). Conversely, the expression of Kir2.2 and Kir2.3 was highest in Type III neurons (64% and 72%) compared to Type II (20%, and 62%) and Type I neurons (0%, and 17%), respectively.
  > — Hazra et al. 2011, kir2_distribution · [1] <!-- quote_key: 8615463_bc844471 -->
- **Crh as a Type III-selective marker:** stress-response comparison across Type I-III neurons · rat BNST · [3]
  > Additionally, only the Type III neurons exhibited an increase in Crf mRNA and a decrease in striatal-enriched protein tyrosine phosphatase (Ptpn5) mRNA after CSS.
  > — Daniel et al. 2019, type3_stress_selective · [3] <!-- quote_key: 76666373_ccffc91d -->

</details>

Cell Ontology mapping: corticotropin-releasing neuron [[CL:4072021](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4072021)] (BROAD).

---

## Results

No atlas cluster in WMBv1 reproduces the Type III channel signature, but atlas metadata (region match, GABAergic neurotransmitter type and Crh expression) points to the CEA-BST Rai14 Pdyn Crh Gaba_2 supertype [CS20230722_SUPT_0393] as the closest available match, with its child cluster 1409 CEA-BST Rai14 Pdyn Crh Gaba_2 [CS20230722_CLUS_1409] as the leading cluster (see property comparison tables and evidence support tables). Both calls rest on atlas-internal metadata alone, with no annotation transfer or other experimental anchor, and both express Cacna1g, Kcna4 and Htr7, which the Type III literature reports as absent, so confidence is low.

No annotation transfer run is attached to this node, so there is no transfer figure.

### CEA-BST Rai14 Pdyn Crh Gaba_2 [CS20230722_SUPT_0393] · 🔴 LOW

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | bed nucleus of stria terminalis [UBERON:0001880] | Pallidum [MBA:803] count_100um=222; Bed nuclei of the stria terminalis [MBA:351] count_100um=215; Striatum [MBA:477] count_100um=1 | Pallidum [MBA:803] count_100um=129; Bed nuclei of the stria terminalis [MBA:351] count_100um=123; Striatum [MBA:477] count_100um=7 (CS20230722_CLUS_1409) | CONSISTENT (SUPT and CLUS) |
| NT type | GABAergic | not asserted | GABA | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Crh expression | defining marker | 7.96 | 6.30 (CS20230722_CLUS_1409) | CONSISTENT |
| Oxtr expression | defining marker | 0.57 | 0.74 (CS20230722_CLUS_1409) | CONSISTENT |
| Gad1 expression | defining marker | 9.27 | 8.83 (CS20230722_CLUS_1409) | CONSISTENT |
| Cacna1i expression | defining marker | 2.98 | 4.49 (CS20230722_CLUS_1409) | SUPT: APPROXIMATE; CLUS: CONSISTENT |
| Hcn4 expression | defining marker | 0.39 | 0.54 (CS20230722_CLUS_1409) | APPROXIMATE |
| Kcnd2 expression | defining marker | 10.39 | 11.10 (CS20230722_CLUS_1409) | CONSISTENT |
| Kcnj12 expression | defining marker | 0.47 | 0.57 (CS20230722_CLUS_1409) | APPROXIMATE |
| Kcnj4 expression | defining marker | 0.81 | 0.13 (CS20230722_CLUS_1409) | SUPT: CONSISTENT; CLUS: APPROXIMATE |
| Oxt expression | negative marker | 0.05 | 0.04 (CS20230722_CLUS_1409) | CONSISTENT |
| Cacna1g expression | negative marker | 2.32 | 3.14 (CS20230722_CLUS_1409) | DISCORDANT |
| Kcna4 expression | negative marker | 2.58 | 2.55 (CS20230722_CLUS_1409) | DISCORDANT |
| Htr7 expression | negative marker | 2.84 | 1.70 (CS20230722_CLUS_1409) | DISCORDANT |
| Slc17a7 / Slc17a6 / Slc17a8 expression | negative markers | 0.00 / 0.08 / 0.03 | 0.00 / 0.04 / 0.07 (CS20230722_CLUS_1409) | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node 0393 CEA-BST Rai14 Pdyn Crh Gaba_2 region and marker match | Atlas metadata | PARTIAL | region_fraction_100um=0.846; strict region_fraction=0.628 | atlas-internal |

**Supporting evidence:**

- Location: region_fraction_100um=0.846 with strict region_fraction=0.628; painted counts fall in the pallidum (222) and the bed nuclei of the stria terminalis (215); CONSISTENT.
- Crh is a defining marker for this supertype at mean expression 7.96 (cohort percentile 0.995, child coverage 1.000); Gad1 (9.27) and Kcnd2 (10.39) are CONSISTENT, and the glutamatergic markers Slc17a7, Slc17a6 and Slc17a8 are near zero, as expected for a GABAergic type [2].

**Marker evidence provenance:**

- **Crh:** the classical Crh assignment is transcript-level (mRNA screening of recorded Type III neurons, 95% positive) [2], and Type III selectivity is supported by a Crh transcript response seen only in Type III neurons after stress [3]; both studies sorted cells by electrophysiological type before assaying, so the marker is anchored to the right cells. Supertype-name circularity does not apply, because Crh has primary citations on the classical node.
- **Oxtr / Oxt:** transcript-level and tested on Type III cells specifically, but scoped to the contrast with paraventricular parvocellular CRF neurons [2]; it does not discriminate among BNST populations. Atlas Oxtr is low (0.57) and Oxt is near zero (0.05).
- **Channel markers (Cacna1i, Hcn4, Kcnd2, Kcnj12, Kcnj4) and negative markers (Cacna1g, Kcna4, Htr7):** established in a single laboratory's transcript profiling of identified rat neurons [1]; not replicated in the corpus and not in mouse. These properties distinguish Type III from Type I and II neurons, and the atlas does not reproduce them cleanly (see Concerns). Per-negative-marker citations are not recorded on the classical node, so Cacna1g (Cav3.1) absence rests on the Cav3.3/Cav3.1 profiling in [1], while Kcna4 and Htr7 are unsourced on the node; a targeted literature search for primary citations would close this gap.
- No atlas annotation/expression discrepancy was found: no marker flagged as defining in atlas metadata is near zero on this supertype.

**Concerns:**

- Cacna1g (2.32), Kcna4 (2.58) and Htr7 (2.84) are DISCORDANT negative markers; the Type III channel signature is not matched at supertype level.
- Cacna1i, Hcn4 and Kcnj12 are only APPROXIMATE (Hcn4 at 0.39 and Kcnj12 at 0.47 are low against a classical profile in which Hcn4 and Kir2.2 mark Type III neurons).
- Location is CONSISTENT, with most cells in or within 100 µm of the BNST, but the largest painted count is in the pallidum (222 versus 215 for the BNST), reflecting the supertype's position at the pallidal edge of the BNST.
- The evidence is a single atlas-metadata item; no experimental anchor (annotation transfer, direct measurement on Type III cells) is attached.
- All Type III evidence is from rat, and the atlas is mouse.

**What would upgrade confidence:** annotation transfer evidence from a Type III-annotated BNST dataset (none identified in the corpus yet) with F1 at or above 0.75 on this supertype or one of its child clusters; a literature search for mouse BNST CRF subtype transcriptomes to test whether Cav3.1, Kv1.4 and 5-HT7 absence holds in mouse; and primary citations for the Kcna4 and Htr7 negative markers.

### 1409 CEA-BST Rai14 Pdyn Crh Gaba_2 [CS20230722_CLUS_1409] · 🔴 LOW

The best child cluster within this supertype, 1409 CEA-BST Rai14 Pdyn Crh Gaba_2 [CS20230722_CLUS_1409], is a low-confidence candidate on the same basis as its parent: atlas metadata alone matches the BNST location, GABAergic type and Crh expression (see Table 1 above and the evidence support table below). Cluster-level facts are given per property in Table 1 rather than as an inventory across child clusters.

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node 1409 CEA-BST Rai14 Pdyn Crh Gaba_2 region and marker match | Atlas metadata | PARTIAL | region_fraction_100um=0.794; strict region_fraction=0.506 | atlas-internal |

**Supporting evidence:**

- Location: region_fraction_100um=0.794 and strict region_fraction=0.506, with painted counts in the pallidum (129) and the bed nuclei of the stria terminalis (123); CONSISTENT.
- Crh is a defining marker for the cluster at mean expression 6.30 (cohort percentile 0.979); Gad1 (8.83) and Kcnd2 (11.10) are CONSISTENT; Slc17a7, Slc17a6 and Slc17a8 are near zero, as expected for a GABAergic type [2].
- Cacna1i (Cav3.3), the classical Type III channel marker [1], is present at 4.49 (CONSISTENT).

**Marker evidence provenance:** as for the parent supertype above. Atlas Crh is a defining marker with a primary-cited classical counterpart, so no circularity flag arises. Cacna1i is present (4.49) while Hcn4 (0.54), Kcnj12 (0.57) and Kcnj4 (0.13) are low, so the HCN4 and Kir2 components of the classical profile are only approximately matched. Atlas Cacna1g is expressed on this cluster (3.14) whereas the Type III literature reports it absent [1].

**Concerns:**

- Cacna1g (3.14), Kcna4 (2.55) and Htr7 (1.70) are DISCORDANT negative markers, so the cluster carries Cav3.1, Kv1.4 and 5-HT7 expression that the Type III class lacks; this could reflect a mixed population within the cluster, but no data in hand tests that.
- Hcn4, Kcnj12 and Kcnj4 are APPROXIMATE.
- Location is CONSISTENT with region_fraction_100um=0.794 and strict region_fraction=0.506; the cluster sits at the BNST-pallidum boundary, where boundary scatter is plausible and at most weak counter-evidence.
- Single atlas-metadata evidence item; no experimental anchor.
- All Type III evidence is from rat; the atlas is mouse.

**What would upgrade confidence:** annotation transfer evidence from Type III cells onto this cluster, with Cacna1g, Kcna4 and Htr7 detection rates measured directly in the atlas cells; and multiplexed transcript co-detection of Crh with these channel genes in the oval and anterolateral BNST to determine whether a Cav3.3+/Cav3.1- subset exists within the cluster.

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| — | `0393 CEA-BST Rai14 Pdyn Crh Gaba_2 [CS20230722_SUPT_0393]` | 278 | 🔴 LOW | Crh defining; BNST/pallidum location | Primary |
| `1409 CEA-BST Rai14 Pdyn Crh Gaba_2 [CS20230722_CLUS_1409]` | `0393 CEA-BST Rai14 Pdyn Crh Gaba_2 [CS20230722_SUPT_0393]` | 191 | 🔴 LOW | Crh 6.30; location CONSISTENT | Secondary |
| `0962 STR D1 Gaba_8 [CS20230722_CLUS_0962]` | `0272 STR D1 Gaba_8 [CS20230722_SUPT_0272]` | 429 | ⚪ UNCERTAIN | Striatal; Hcn4 absent, Kcna4 high | Eliminated (striatal D1 neurons; Hcn4 absent) |
| `0961 STR D1 Gaba_8 [CS20230722_CLUS_0961]` | `0272 STR D1 Gaba_8 [CS20230722_SUPT_0272]` | 960 | 🔴 REFUTED | Striatal location; Crh 0.22 | Eliminated (striatal, not BNST) |
| `1360 CEA-AAA-BST Six3 Sp9 Gaba_3 [CS20230722_CLUS_1360]` | 0375 CEA-AAA-BST Six3 Sp9 Gaba_3 | 202 | ⚪ UNCERTAIN | Crh 0.12; Cav3.1, Kv1.4, 5-HT7 present | Eliminated (Crh near absent) |
| `1375 ACB-BST-FS D1 Gaba_1 [CS20230722_CLUS_1375]` | 0381 ACB-BST-FS D1 Gaba_1 | 139 | ⚪ UNCERTAIN | Crh 0.18; Oxt, Cacna1g, Kcna4 present | Eliminated (Crh low; accumbens-fundus type) |
| — | `0272 STR D1 Gaba_8 [CS20230722_SUPT_0272]` | 1918 | 🔴 REFUTED | Striatal; Hcn4 absent, Kcna4 high | Eliminated (striatal, not BNST) |
| — | `0265 STR D1 Gaba_1 [CS20230722_SUPT_0265]` | 2291 | 🔴 REFUTED | Striatal; Hcn4 absent | Eliminated (striatal, not BNST) |
| — | `0278 STR D2 Gaba_5 [CS20230722_SUPT_0278]` | 1182 | 🔴 REFUTED | Striatal D2 type; Hcn4 absent | Eliminated (striatal D2 neurons) |
| — | `0266 STR D1 Gaba_2 [CS20230722_SUPT_0266]` | 434 | 🔴 REFUTED | Striatal; Oxtr near absent | Eliminated (striatal, Oxtr absent) |

</details>

---

## Methods

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The BNST anterolateral group Type III CRF neuron is a CLASSICAL_ELECTROPHYSIOLOGICAL node: GABAergic [2], with Crh [2], [3], Oxtr [2], Gad1 [2], Cacna1i, Hcn4, Kcnd2, Kcnj12 and Kcnj4 [1] as defining markers; Oxt, Cacna1g, Kcna4, Htr7, Slc17a7, Slc17a6 and Slc17a8 as negative markers; and soma location in the bed nucleus of stria terminalis [UBERON:0001880] [1], [2]. The curated node records that this is a subset of the broader BNST CRF neuron population (not synonymous with it), that all Type I-III evidence is from rat, and that no morphology is reported.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

No annotation transfer or bulk transcriptomic correlation runs are attached to this node.

**Atlas data sources.** WMBv1 (CCN20230722); no pseudobulk source path or SHA-256 is recorded in the methods summary for this graph.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table:**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_bnstalg_type_iii_crf_neuron_to_CS20230722_CLUS_0962 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bnstalg_type_iii_crf_neuron_to_CS20230722_CLUS_1409 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bnstalg_type_iii_crf_neuron_to_CS20230722_CLUS_0961 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bnstalg_type_iii_crf_neuron_to_CS20230722_CLUS_1360 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bnstalg_type_iii_crf_neuron_to_CS20230722_CLUS_1375 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bnstalg_type_iii_crf_neuron_to_CS20230722_SUPT_0393 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bnstalg_type_iii_crf_neuron_to_CS20230722_SUPT_0272 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bnstalg_type_iii_crf_neuron_to_CS20230722_SUPT_0265 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bnstalg_type_iii_crf_neuron_to_CS20230722_SUPT_0278 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bnstalg_type_iii_crf_neuron_to_CS20230722_SUPT_0266 | ATLAS_METADATA | PARTIAL | atlas-internal |

*Generated by evidencell `464c7dd` at 2026-11-13T13:27:09+00:00 from [kb/graphs/sexually_dimorphic/bnstalg_type_iii_crf_neuron.yaml](kb/graphs/sexually_dimorphic/bnstalg_type_iii_crf_neuron.yaml).*

</details>

---

## Discussion

**Primary mapping:** BNST anterolateral group Type III CRF neuron → 0393 CEA-BST Rai14 Pdyn Crh Gaba_2 [CS20230722_SUPT_0393] at LOW confidence. Key support: atlas metadata for BNST/pallidum location and defining Crh expression, with a paired best child cluster 1409 CEA-BST Rai14 Pdyn Crh Gaba_2 [CS20230722_CLUS_1409]. Key caveats: ambiguous mapping through DISCORDANT negative channel and receptor markers (Cacna1g, Kcna4, Htr7), and the absence of any experimental anchor.

The Cell Ontology has no specific term for this population; corticotropin-releasing neuron [[CL:4072021](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4072021)] is the closest ancestor. No CL term exists for an electrophysiologically defined BNSTALG Type III class, nor for any BNSTALG-specific cell class. BROAD parent mapping to CL:4072021 only. Candidate for a new CL term capturing the BNSTALG Type III CRF class, distinguished from PVN parvocellular CRF neurons by an OTR+/Oxt- profile and from sibling BNSTALG types by the Cav3.3+/Cav3.1-/Kv1.4-/5-HT7- channel and receptor signature.

The practical reading is that the Crh-defined CEA-BST supertype is where a BNST CRF neuron class would be expected to fall in WMBv1, but the channel signature that defines Type III is not reproduced at either supertype or best-cluster level. Because Type III is a physiologically defined subset of BNST CRF neurons, and the supertype contains Crh-expressing neurons with a different channel profile, the correspondence may be partial (Type III cells forming a subset of the cluster) or absent. The data in hand cannot separate these.

### Proposed experiments and follow-ups

No annotation transfer has been run for this node and no external dataset with a declared Type III source correspondence has been identified, so the honest follow-up is an evidence-extraction gap: no external dataset identified for this type.

1. **Annotation transfer from Type III-matched cells.** Identify a rodent single-cell transcriptomic dataset of BNST CRF neurons that carries electrophysiological or channel-profile labels, run annotation transfer onto WMBv1 (CCN20230722) at supertype and cluster ranks, and attach the result as AnnotationTransferEvidence. Target: F1 of 0.75 or higher at CS20230722_SUPT_0393 or CS20230722_CLUS_1409. Resolves open questions 1 and 2 for both candidates.
2. **Channel-gene co-detection.** Multiplexed transcript co-detection of Crh with Cacna1i, Cacna1g, Kcna4 and Htr7 in the oval and anterolateral BNST of mouse, to test whether a Cav3.3+/Cav3.1-/Kv1.4-/5-HT7- subset exists within the CEA-BST Rai14 Pdyn Crh Gaba_2 cells. Expected output: a quantitative co-expression record for the node's evidence. Resolves open questions 2 and 3.
3. **Targeted literature search.** Search for mouse BNST CRF subtype transcriptomes and for primary citations for the Kcna4 and Htr7 negative markers on the classical node; expected output: LiteratureEvidence entries with quote_keys. Resolves open questions 3 and 4.

### Open questions

1. Is there an annotation transfer dataset for Type III neurons, and where do these cells land in WMBv1 (children of the CEA-BST Rai14 Pdyn Crh Gaba_2 supertype versus other CEA-BST or ACB-BST types)? (both candidates)
2. Is the classical Cav3.3+/Cav3.1-/Kv1.4-/5-HT7- signature present in any WMBv1 cluster, or does it fail to transfer from rat to mouse? (both candidates)
3. Do the Cacna1g, Kcna4 and Htr7 signals on these Crh clusters come from a subpopulation that is distinct from a putative Type III subset? (both candidates)
4. Are the Kcna4 and Htr7 negative markers and the Hcn4 marker primary-cited on the classical node? (both candidates)
5. Consider curator review of whether the striatal D1/D2 supertypes surfaced by the Stage A cohort should remain in the candidate set; they show no Hcn4 expression and only distant location overlap.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Hazra et al. 2011 | [21310239](https://pubmed.ncbi.nlm.nih.gov/21310239/) | soma location |
| [2] | Dabrowska et al. 2013 | [24009552](https://pubmed.ncbi.nlm.nih.gov/24009552/) | soma location |
| [3] | Daniel et al. 2019 | [30878403](https://pubmed.ncbi.nlm.nih.gov/30878403/) | Crh marker |

<!-- verdict-block-start: edge_bnstalg_type_iii_crf_neuron_to_CS20230722_SUPT_0393 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  relationship: evidencell:UncertainRelationship
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] CS20230722_SUPT_0393 is the closest available supertype: Crh is a defining
    marker with child coverage 1.0 and region_fraction_100um 0.846, but the only evidence is
    atlas metadata and Cacna1g, Kcna4 and Htr7 are DISCORDANT negative markers.
  reconciliation_note: >
    Paired with edge_bnstalg_type_iii_crf_neuron_to_CS20230722_CLUS_1409 (best child cluster
    of this supertype). Predicate left uncertain between broadMatch (Type III as a subset of the
    Crh-defined CEA-BST group) and no correspondence; no experimental anchor to decide.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: Cacna1g, Kcna4 and Htr7 are DISCORDANT negative markers at supertype level; the Type III channel signature is not matched.
    - caveat_type: AMBIGUOUS_MAPPING
      description: The only evidence is a single atlas-metadata item; no annotation transfer or direct measurement on Type III cells is attached. Child-cluster breakdown not assessed.
  proposed_experiments:
    - Run annotation transfer from a Type III-matched BNST single-cell dataset onto CS20230722_SUPT_0393 and its child clusters (target F1 of 0.75 or higher).
    - Multiplexed transcript co-detection of Crh with Cacna1i, Cacna1g, Kcna4 and Htr7 in mouse oval and anterolateral BNST.
  unresolved_questions:
    - No external dataset identified for the BNST anterolateral group Type III CRF neuron; annotation transfer cannot yet be run.
    - Is the Cav3.3+/Cav3.1-/Kv1.4-/5-HT7- signature present in any WMBv1 cluster, or does it fail to transfer from rat to mouse?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bnstalg_type_iii_crf_neuron_to_CS20230722_CLUS_1409 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  relationship: evidencell:UncertainRelationship
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CS20230722_CLUS_1409 is the leading child cluster of the CEA-BST Rai14 Pdyn Crh Gaba_2
    supertype: Crh is a defining marker (cohort percentile 0.979) and region_fraction_100um is 0.794,
    but the only evidence is atlas metadata and Cacna1g, Kcna4 and Htr7 are DISCORDANT negative markers.
  reconciliation_note: >
    Paired with edge_bnstalg_type_iii_crf_neuron_to_CS20230722_SUPT_0393 (parent supertype).
    Close versus broad is undecided because no experimental evidence shows whether Type III cells
    form a subset of this cluster or map elsewhere.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: Cacna1g, Kcna4 and Htr7 are DISCORDANT negative markers on this cluster; Hcn4, Kcnj12 and Kcnj4 are APPROXIMATE.
    - caveat_type: AMBIGUOUS_MAPPING
      description: The only evidence is a single atlas-metadata item, with no annotation transfer or direct measurement on Type III cells.
  proposed_experiments:
    - Run annotation transfer from a Type III-matched BNST single-cell dataset onto CS20230722_CLUS_1409 (target F1 of 0.75 or higher).
    - Multiplexed transcript co-detection of Crh with Cacna1i, Cacna1g, Kcna4 and Htr7 in mouse oval and anterolateral BNST.
  unresolved_questions:
    - Do the Cacna1g, Kcna4 and Htr7 signals on this cluster arise from a subpopulation distinct from any Type III subset?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bnstalg_type_iii_crf_neuron_to_CS20230722_CLUS_0962 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Striatal D1 cluster: Hcn4 is DISCORDANT (absent) and Kcna4 is expressed, against a classical Type III profile.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bnstalg_type_iii_crf_neuron_to_CS20230722_CLUS_0961 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Striatal location is DISCORDANT with the BNST (region_fraction_100um 0.039) and Hcn4 is absent.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bnstalg_type_iii_crf_neuron_to_CS20230722_CLUS_1360 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Crh is near absent on this cluster and Cacna1g, Kcna4 and Htr7 are all DISCORDANT negative markers.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bnstalg_type_iii_crf_neuron_to_CS20230722_CLUS_1375 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Crh is low on this accumbens-fundus-type cluster and Oxt, Cacna1g and Kcna4 are DISCORDANT negative markers.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bnstalg_type_iii_crf_neuron_to_CS20230722_SUPT_0272 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Striatal supertype with DISCORDANT location (region_fraction_100um 0.061), absent Hcn4 and high Kcna4.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bnstalg_type_iii_crf_neuron_to_CS20230722_SUPT_0265 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Striatal supertype with DISCORDANT location (region_fraction_100um 0.024) and absent Hcn4.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bnstalg_type_iii_crf_neuron_to_CS20230722_SUPT_0278 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Striatal D2-type supertype with DISCORDANT location (region_fraction_100um 0.048) and absent Hcn4.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bnstalg_type_iii_crf_neuron_to_CS20230722_SUPT_0266 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Striatal supertype with DISCORDANT location (region_fraction_100um 0.016), near-absent Oxtr and absent Hcn4.
```
<!-- verdict-block-end -->
