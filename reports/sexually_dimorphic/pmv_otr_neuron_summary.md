# Ventral premammillary nucleus (PMv) oxytocin receptor neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type definition

The **PMv oxytocin receptor (OTR) neuron** is a sexually dimorphic hypothalamic neuron defined by expression of the oxytocin receptor (*Oxtr*) in the ventral premammillary nucleus (PMv) [MBA:1004]. OTR expression in this region is markedly male-biased across postnatal development (P14–P56) [2]. The same nucleus houses at least two additional molecularly distinct subpopulations — PMv-DAT neurons (*Slc6a3*+, dopaminergic-lineage) [1] and PMv-PACAP neurons (*Adcyap1*+) [1] — that are co-listed as defining markers because the three populations may partially overlap or have been studied together. This heterogeneity means the current node may need to be split into separate sub-nodes before a fully resolved mapping can be achieved.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Ventral premammillary nucleus [MBA:1004] | [1], [2] |
| NT type | Not specified; DAT+ subpopulation implies dopaminergic co-release; OTR+ and PACAP+ subpopulations likely glutamatergic *(note: inferred from atlas NT annotation of candidate supertype; not directly stated in classical literature)* | — |
| Defining markers | *Oxtr*, *Slc6a3*, *Adcyap1* | [2], [1], — |
| Negative markers | None documented | — |
| Neuropeptides | None documented | — |
| Sex bias | Male-biased (males > females, PMv OTR expression P14–P56) | [2] |

<details>
<summary>Literature support — expand for verbatim quotes</summary>

**[2] K et al. 2019 · PMID:32313029 — Neuronal Markers and Molecular Characteristics**

> "The ventral premammillary nucleus (PMv) showed significantly higher OTR expression in males compared to females between P14 and P56 (Fig. 7a-d)."
> — K et al. 2019, Neuronal Markers and Molecular Characteristics · [2] <!-- quote_key: 201207691_ff444c30 -->

**[1] Z et al. 2024 · PMID:39416191 — Sexually Dimorphic Brain Regions and Structures**

> "Previous studies identified sexually dimorphic neuron populations within the PMv (e.g., PMv-DAT, PMv-PACAP), complementing our systematic identification of subclass-level abundance changes."
> — Z et al. 2024, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 273240437_af6642f9 -->

> "We identified two adjacent regions within the hypothalamus that exhibited significant sexual dimorphism. Region 1 overlaps with the anterior hypothalamic nucleus (AHN), while Region 2 primarily overlaps with the ventral premammillary nucleus (PMv)."
> — Z et al. 2024, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 273240437_ed3a4faa -->

</details>

---

## WMBv1 mapping candidates

**Key finding:** pmv_otr_neuron is defined as MALE_BIASED, but sex bias cannot be confirmed at cluster level. MFR data is absent from the DB for CLUS_2470 [CS20230722_CLUS_2470] — the best child cluster with n=192 PMv cells and the highest expression of all three defining markers. This is the primary confidence gap, and it caps all edges at LOW pending resolution.

**4a. Candidate overview table**

| Rank | WMBv1 node | Taxonomy level | Cells (MERFISH) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0607 PMv-TMv Pitx2 Glut_3 [CS20230722_SUPT_0607] | SUPERTYPE | n=347 at MBA:1004 (PMv) | 🔴 LOW · CROSS_CUTTING | *Oxtr*, *Slc6a3*, *Adcyap1* all CONSISTENT; NT APPROXIMATE; sex bias NOT_ASSESSED | Speculative |
| 2 | 2470 PMv-TMv Pitx2 Glut_3 [CS20230722_CLUS_2470] | CLUSTER | n=192 at MBA:1004 (PMv) | 🔴 LOW · PARTIAL_OVERLAP | All 3 markers substantially above supertype mean; sex bias NOT_ASSESSED (MFR absent) | Speculative |

Total: 2 edges — 2 LOW, 0 MODERATE, 0 UNCERTAIN. Both are atlas-metadata only.

**4b. Property alignment table — primary candidates**

| Property | Classical | SUPT_0607 (supertype, LOW/CROSS_CUTTING) | CLUS_2470 (best cluster, LOW) | Alignment |
|---|---|---|---|---|
| Soma location | Ventral premammillary nucleus [MBA:1004] | MBA:1004 (PMv) n=347 (dominant location) | MBA:1004 (PMv) n=192 (dominant location) | CONSISTENT |
| NT type | Not specified; DAT+ subset implies dopaminergic co-release | Glutamatergic (PMv-TMv Pitx2 Glut) | Glutamatergic (PMv-TMv Pitx2 Glut) | APPROXIMATE |
| *Oxtr* expression | defining marker (transcript) | mean expression = 2.0 (DEFINING_SCOPED atlas marker) | mean expression = 4.45 (vs supertype mean 2.0) | CONSISTENT |
| *Slc6a3* expression | defining marker (transcript) | mean expression = 3.07 (DEFINING atlas marker) | mean expression = 6.02 (vs supertype mean 3.07) | CONSISTENT |
| *Adcyap1* expression | defining marker | mean expression = 4.8 | mean expression = 8.13 (vs supertype mean 4.8) | CONSISTENT |
| Sex ratio | male-biased (PMv OTR expression higher in males, P14–P56) | not available (MFR computed at rank 0 only) | NOT_ASSESSED — MFR absent from DB for CLUS_2470 (n=192 PMv cells) | NOT_ASSESSED |
| Annotation transfer | — | NOT_ASSESSED | NOT_ASSESSED | — |

*(CLUS_2470 [PMv n=192, Oxtr=4.45, Slc6a3=6.02, Adcyap1=8.13 — all above supertype mean] is the best identified child cluster of SUPT_0607; MFR data absent for CLUS_2470 — male-bias alignment pending, see proposed experiments.)*

**Note on SUPT_0607 as CROSS_CUTTING:** SUPT_0607 simultaneously expresses all three defining markers (*Oxtr*, *Slc6a3*, *Adcyap1*) at levels corresponding to the three putative PMv subpopulations (PMv-OTR, PMv-DAT, PMv-PACAP). The supertype aggregates what the classical taxonomy may treat as distinct subtypes. CLUS_2470 shows the same co-expression pattern at higher intensities (all three markers substantially above supertype means), confirming that multi-marker co-expression is a cluster-level feature, not merely a supertype-averaging artefact.

---

## 0607 PMv-TMv Pitx2 Glut_3 · 🔴 LOW

**Accession:** CS20230722_SUPT_0607 · **Taxonomy level:** SUPERTYPE · **Relationship:** CROSS_CUTTING

### Supporting evidence

- SUPT_0607 received the highest DB score (4) of any candidate at any rank for pmv_otr_neuron. Its dominant soma location is MBA:1004 (PMv; n=347 cells), directly matching the classical type definition.
- All three defining markers are detected at the supertype level: *Oxtr* (mean = 2.0, DEFINING_SCOPED), *Slc6a3* (mean = 3.07, DEFINING), and *Adcyap1* (mean = 4.8). All alignments are CONSISTENT.
- The atlas NT annotation — glutamatergic ("PMv-TMv Pitx2 Glut") — is consistent with the expected neurotransmitter identity of the OTR+ and PACAP+ subpopulations *(note: glutamatergic identity inferred from atlas cluster name; the DAT+ fraction may represent a functionally distinct, dopamine-co-releasing minority)*.

### Marker evidence provenance

- **Oxtr:** Evidence is atlas precomputed mean expression only (DEFINING_SCOPED flag indicates detectable but not pan-supertype expression). The DEFINING_SCOPED designation is consistent with the known heterogeneity of OTR+ cells in the PMv. The original classical citation [2] used OTR-Venus reporter mice, providing protein-level evidence for the classical node but no direct cross-mapping to WMBv1.
- **Slc6a3:** Atlas metadata assigns this as a DEFINING marker (mean = 3.07), consistent with the PMv-DAT subpopulation literature [1]. No direct scRNA-seq cross-validation to WMBv1 is available.
- **Adcyap1:** Listed as a defining marker with no citation on the classical node. The atlas shows mean = 4.8 for SUPT_0607, providing supporting but uncorroborated evidence. A targeted literature search for "*Adcyap1* / PACAP PMv hypothalamus" would help establish independent provenance for this marker on the classical node.

### Concerns

1. **CROSS_CUTTING relationship.** SUPT_0607 simultaneously expresses the marker signatures of all three putative PMv subpopulations (PMv-OTR, PMv-DAT, PMv-PACAP). The supertype likely aggregates neurons the classical taxonomy would treat as distinct subtypes — a structural mismatch limiting the interpretive value of a one-to-one edge.
2. ***Tac1* dominance.** *Tac1* is the highest-expressing DEFINING atlas marker in SUPT_0607 (mean = 8.95) yet is entirely absent from the classical pmv_otr_neuron definition. SUPT_0607 may be better characterised as a *Tac1*+ PMv supertype for which *Oxtr*, *Slc6a3*, and *Adcyap1* are co-expressed subtype markers rather than type-defining ones.
3. **Sister supertype SUPT_0605** (PMv-TMv Pitx2 Glut_1, DB score = 2) may capture a further fraction of the male-biased OTR+ population; the two supertypes together could span the classical node.
4. **Sex bias NOT_ASSESSED.** MFR is only computed at rank 0 (cluster level) and is absent for the best child cluster CLUS_2470. Male-biased dimorphism — the defining property of this classical node — cannot be confirmed in the atlas data at this stage.
5. **Cell count unavailable.** The n_cells field for SUPT_0607 was not retrieved.

### What would upgrade confidence

- **Resolve the MFR gap (highest priority):** Query the precomputed HDF5 directly for CLUS_2470 male_female_ratio. If MFR > 1, this removes the primary confidence barrier for both edges.
- **Sub-cluster analysis of SUPT_0607:** Query *Oxtr*, *Slc6a3*, *Adcyap1*, and *Tac1* in child clusters to determine whether marker-high cells segregate into distinct leaves. If so, a cluster-level edge to the appropriate child would replace this speculative supertype edge.
- **Resolve the *Tac1* discrepancy:** If *Tac1* is confirmed as a PMv OTR-neuron co-marker, incorporate it into the classical node definition or document as co-expressed but non-defining.
- **MapMyCells annotation transfer** of published PMv scRNA-seq or Oxtr-Cre / Slc6a3-Cre lineage data against WMBv1; target F1 ≥ 0.80 at CLUSTER level (AnnotationTransferEvidence on CS20230722_CLUS_2470).
- **Targeted literature search** for *Adcyap1* / PACAP in PMv to provide independent provenance for this marker on the classical node.
- **Node splitting decision:** Re-run candidate search on pmv_otr, pmv_dat, and pmv_pacap sub-nodes if the classical node is split; individual sub-nodes may map cleanly to separate child clusters.

---

## 2470 PMv-TMv Pitx2 Glut_3 · 🔴 LOW

**Accession:** CS20230722_CLUS_2470 · **Taxonomy level:** CLUSTER · **Relationship:** PARTIAL_OVERLAP

### Supporting evidence

- CLUS_2470 is the child cluster of SUPT_0607 with MBA:1004 (PMv) as primary soma (n=192 cells — the largest PMv cluster in the supertype). Location is CONSISTENT with the classical node.
- All three defining markers are expressed at levels substantially above the supertype mean: *Oxtr* = 4.45 (vs supertype 2.0), *Slc6a3* = 6.02 (vs supertype 3.07), *Adcyap1* = 8.13 (vs supertype 4.8). Expression concentrates all three marker-expressing PMv cells into this cluster, making it the most specific single atlas entry for pmv_otr_neuron currently available.
- The enrichment pattern — all three markers rising markedly from supertype mean to cluster level — is consistent with CLUS_2470 capturing the co-expressing PMv subpopulation rather than representing a single-marker subtype.

### Marker evidence provenance

All marker values are atlas precomputed mean expression from the Allen Brain Cell Atlas (WMBv1). No independent scRNA-seq, ISH, or IHC cross-validation against this specific cluster has been performed.

### Concerns

1. **Sex bias NOT_ASSESSED — primary confidence gap.** pmv_otr_neuron is defined as MALE_BIASED, but MFR is absent from the DB for CLUS_2470 (n=192 cells). CLUS_2473 (PMv, n=86, MFR=2.23) shows mild male bias but very low marker expression — it is a distinct PMv subtype, not a surrogate for CLUS_2470. Until sex bias is confirmed at cluster level, confidence cannot rise above LOW.
2. **Possible DB ingest gap.** The absent MFR for CLUS_2470 may reflect a gap in the DB ingest pipeline rather than a genuine absence in the precomputed stats HDF5. This should be checked before concluding that sex bias data do not exist for this cluster.
3. **Multi-marker co-expression ambiguity.** CLUS_2470 co-expresses *Oxtr*, *Slc6a3*, and *Adcyap1* at high levels simultaneously. If these mark functionally distinct cell types, a single cluster-level edge conflates them. Node splitting may be required before a higher-confidence assignment can be made.
4. **No annotation transfer evidence.** AT pipeline has not been run for pmv_otr_neuron; F1-based confirmation is unavailable.

### What would upgrade confidence

- **Resolve MFR gap (highest priority):** Query precomputed HDF5 directly for CLUS_2470 male_female_ratio. If MFR > 1, the primary confidence barrier is removed (would be added as a new property_comparison on this edge).
- **MapMyCells annotation transfer:** Run AT on published PMv scRNA-seq or Oxtr-Cre / Slc6a3-Cre data against WMBv1; target F1 ≥ 0.80 at CLUSTER level. Expected output: AnnotationTransferEvidence on CS20230722_CLUS_2470. Sex-stratified AT results would simultaneously address the sex bias question.
- **Node splitting decision** (see above — prerequisite to a definitive, non-CROSS_CUTTING cluster assignment).

---

## Proposed experiments

### 1. Precomputed stats HDF5 query — MFR for CLUS_2470

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Query precomputed HDF5 directly for CLUS_2470 male_female_ratio | CS20230722_CLUS_2470 | MFR value or confirmed absence | Whether sex bias (the primary classical property) can be confirmed at cluster level; if MFR > 1, primary confidence barrier for both edges is removed |

### 2. Atlas sub-cluster expression query — SUPT_0607 child clusters

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Query *Oxtr*, *Slc6a3*, *Adcyap1*, *Tac1* in child clusters of SUPT_0607 | All rank-0 children of CS20230722_SUPT_0607 | Per-cluster expression table | Whether PMv subpopulations segregate at cluster level; enables cluster-level edge(s) to replace speculative supertype edge; clarifies *Tac1* role (open question 5) |

### 3. MapMyCells annotation transfer

| What | Target | Expected output | Resolves |
|---|---|---|---|
| MapMyCells AT of published PMv scRNA-seq or Oxtr-Cre / Slc6a3-Cre lineage data against WMBv1 | CS20230722_CLUS_2470 (primary); CS20230722_SUPT_0607 (secondary); target F1 ≥ 0.80 at CLUSTER level | AnnotationTransferEvidence on both edges; sex-stratified F1 if data permit | Open questions 1 and 2; removes uncertainty on co-expression and sex bias alignment |

### 4. Classical node curation (prerequisite)

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Decide whether pmv_otr_neuron should be split into pmv_otr, pmv_dat, pmv_pacap sub-nodes | Classical KB node definition | Revised node YAML with single-marker-defined sub-nodes, or explicit decision to retain a heterogeneous node | Eliminates CROSS_CUTTING ambiguity in all downstream mapping edges; enables clean re-run of candidate search (open question 4) |

---

## Open questions

1. Why is MFR absent for CLUS_2470 (n=192 cells)? Is this a DB ingest gap or a genuine absence in the precomputed stats? (edge_pmv_otr_neuron_to_cs20230722_clus_2470)
2. Do *Oxtr*, *Slc6a3*, and *Adcyap1* co-localise within individual CLUS_2470 cells, or do they mark distinct subpopulations within the cluster? (edge_pmv_otr_neuron_to_cs20230722_clus_2470)
3. Do individual clusters within SUPT_0607 segregate by marker (*Oxtr*-high, *Slc6a3*-high, *Adcyap1*-high), allowing sub-resolution mapping? (edge_pmv_otr_neuron_to_cs20230722_supt_0607)
4. Should pmv_otr_neuron be split into separate pmv_otr, pmv_dat, pmv_pacap sub-nodes prior to final mapping? (both edges)
5. What is the role of *Tac1* (mean = 8.95, highest DEFINING atlas marker in SUPT_0607) relative to the classical pmv_otr_neuron definition? Should it be added as a co-expressed marker or treated as a distinguishing feature of a related but distinct supertype? (edge_pmv_otr_neuron_to_cs20230722_supt_0607)

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_pmv_otr_neuron_to_cs20230722_supt_0607 | ATLAS_METADATA | SUPPORT |
| edge_pmv_otr_neuron_to_cs20230722_clus_2470 | ATLAS_METADATA | SUPPORT |

All evidence is atlas-metadata only. No literature, annotation transfer, or direct experimental evidence has been incorporated at this stage.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Z et al. 2024 | [PMID:39416191](https://pubmed.ncbi.nlm.nih.gov/39416191/) | Soma location; *Slc6a3* marker (PMv-DAT); *Adcyap1* marker (PMv-PACAP); sexually dimorphic regions; subpopulation heterogeneity |
| [2] | K et al. 2019 | [PMID:32313029](https://pubmed.ncbi.nlm.nih.gov/32313029/) | Soma location; *Oxtr* marker; male-biased sexual dimorphism in PMv (P14–P56) |
