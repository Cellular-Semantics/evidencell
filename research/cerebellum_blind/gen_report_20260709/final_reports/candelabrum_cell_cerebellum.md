# Cerebellar candelabrum cell (Purkinje-layer interneuron) — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml`*

---

## Introduction

Candelabrum cells (CCs) are molecularly distinct GABAergic interneurons of the cerebellar cortex whose soma reside in the Purkinje cell layer (PCL), a position that sets them apart from the molecular layer interneurons (basket and stellate cells) and from granule-layer Golgi cells. They were originally identified in 1994 on the basis of their distinctive light-level morphology — small PCL soma, dendrites extending to the molecular layer surface, and beaded axons making numerous local synapses within the molecular layer — and subsequently confirmed as a separate transcriptomic class by snRNAseq (Kozareva et al. 2020; Osorno et al. 2021/2022). Recent functional work establishes that CCs preferentially receive Purkinje-collateral input and in turn inhibit molecular layer interneurons, producing a PC disinhibition circuit [1]. The mapping matters because no positive molecular markers have yet been formally reported for this type, leaving soma location and GABAergic identity as the principal available features for atlas alignment at present.

| Property | Value | References |
|---|---|---|
| Soma location | Purkinje cell layer of cerebellar cortex [UBERON:0002979]; cerebellar cortex [UBERON:0002129] | [1], [2] |
| Neurotransmitter | GABAergic | [1], [3] |
| Defining markers | None ingested (molecular marker gap — see notes) | — |
| Negative markers | None | — |
| Neuropeptides | None | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** literature (Osorno et al. 2022; Lainé et al. 1994 cited therein) · PCL confirmed by morphology and snRNAseq · [1], [2]

  > CCs were identified in 1994 based on their distinctive light-level morphology (Lainé et al., 1994). CCs have a small cell body near the Purkinje cell layer (PCL), dendrites that extend to the surface of the molecular layer, and beaded axons that make numerous local synapses within the molecular layer. Nothing else was known about CCs because there had been no electrophysiological recordings, and no molecular markers had been identified. In our recent snRNAseq study we identified three types of molecularly distinct inhibitory interneurons in the cerebellar cortex that are neither MLIs or GoCs (Kozareva et al., 2020)
  > — Osorno et al. 2022, Anatomical organization and core cell types · [1] <!-- quote_key: 233245440_70215095 -->

- **Neurotransmitter:** GABAergic confirmed by snRNAseq and functional experiments · [1], [3]

  > .We find that CCs are the most abundant PC layer interneuron. They are GABAergic, molecularly distinct, and present in all cerebellar lobules. Their high resistance renders CC firing highly sensitive to synaptic inputs. CCs are excited by MFs and granule cells, and strongly inhibited by PCs. CCs in turn inhibit molecular layer interneurons, which leads to PC disinhibition. Thus, inputs, outputs and local signals all converge onto CCs to allow them to assume a unique role in controlling cerebellar output.
  > — Osorno et al. 2022, Anatomical organization and core cell types · [1] <!-- quote_key: 233245440_edf83720 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: candelabrum cell [[CL:4042030](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4042030)] (EXACT).

---

## Results

Atlas metadata alignment supports a tentative mapping of the cerebellar candelabrum cell to the "CB PLI" (Purkinje layer interneuron) cluster-supertype family in WMBv1, based on consistent GABAergic identity and cerebellar regional proximity; no annotation-transfer or molecular marker evidence is available to anchor the call further. The region fractions for all candidates are lower-bound estimates due to unpainted CCF2020 descendants, and the absent molecular marker profile means the mapping rests entirely on naming and regional signal (see property comparison tables).

### 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] · 🔴 LOW

GABAergic identity and cerebellar region proximity support a broad alignment of candelabrum cells to the supertype 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] as the most plausible atlas placement available from current evidence. The supertype label — "CB PLI" (cerebellar Purkinje layer interneuron) — directly reflects the soma position that defines candelabrum cells, and its child cluster 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] confirms the GABAergic annotation consistent with the classical type. However, no molecular markers, patch-seq data, or annotation-transfer experiments constrain this to a single cluster or confirm transcriptomic identity; the call is held at LOW confidence pending experimental anchor.

**Table 1 — Property comparison (supertype 1144)**

| Property | Classical | Supertype 1144 | Best cluster (5178) | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | not asserted at supertype | GABA (cluster-level) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Soma location | Purkinje cell layer of cerebellar cortex [UBERON:0002979]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512], fiber tracts, arbor vitae (region_fraction_100um: 0.699; lower_bound) | Cerebellum [MBA:512] (region_fraction_100um: 0.768; lower_bound) | CONSISTENT (lower_bound caveat) |

**Table 2 — Evidence support (supertype 1144)**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas region + NT metadata | Atlas metadata | PARTIAL | region_fraction_100um=0.699 (lower_bound); NT not asserted at supertype level | atlas-internal |

*(Child-cluster breakdown not assessed — no per-cluster marker or expression data was collected. See proposed experiments.)*

**Supporting evidence:**
- Region fraction for 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] is `region_fraction_100um: 0.699` with strict `region_fraction: 0.610`, both lower-bound estimates. The dominant soma signal is in Cerebellum [MBA:512]. The cerebellar majority placement is consistent with candelabrum cell location in the Purkinje cell layer.
- The supertype name "CB PLI Gly-Gaba_1" encodes a cerebellar Purkinje layer interneuron identity, directly consistent with the classical anatomical definition of candelabrum cells.
- Child cluster 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] (the best child by region fraction) confirms GABAergic identity (CONSISTENT), reinforcing the broader supertype placement.

**Marker evidence provenance:**
- ⚠ **Molecular marker gap**: The classical node carries no defining_markers, negative_markers, or neuropeptides in the knowledge base. Candelabrum cells were identified as a transcriptomically distinct type (Kozareva et al. 2020; Osorno et al. 2021/2022), but no specific positive molecular markers were ingested. This is the single largest gap in the mapping evidence portfolio. Without markers, concordance between the classical type's transcriptomic signature and the atlas cluster's expression profile cannot be assessed.

**Concerns:**
- NT type is NOT_ASSESSED at supertype level — the atlas supertype node does not carry a GABA annotation, though the child cluster (5178) does.
- All region fractions are `lower_bound` estimates (non-painted CCF2020 descendants present and uncounted). The true cerebellar fraction may be higher but cannot be confirmed from current atlas paint.
- Candelabrum cells are defined by PCL soma position, but WMBv1 MERFISH data registers soma position at broad cerebellar/lobular resolution, not at laminar (Purkinje layer vs. molecular layer) resolution. The atlas cannot distinguish PCL from molecular layer interneurons on location alone.
- No molecular markers are available to exclude contamination of this cluster by other PCL-resident cells.

**What would upgrade confidence:**
- Annotation transfer from a candelabrum-cell-specific source dataset (e.g. snRNAseq from PCL-enriched fractions or Cre-driver-targeted CCs if a Cre line is developed) to WMBv1, targeting F1 ≥ 0.60 at cluster level.
- Identification and validation of at least one positive molecular marker for CCs, followed by marker comparison to atlas cluster 5178 and its siblings within supertype 1144.
- Targeted literature search: "candelabrum cell markers cerebellum snRNAseq" to recover any markers reported since Osorno 2022 that have not yet been ingested.

---

### 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] · 🔴 LOW

Within supertype 1144, cluster 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] is the best single-cluster candidate for candelabrum cell identity, supported by the highest cerebellar region fraction among the "CB PLI" members (region_fraction_100um: 0.768, lower_bound) and confirmed GABAergic annotation. With n=3,066 cells, 5178 is the largest cluster within the CB PLI supertype, potentially reflecting the numerical abundance of CCs among PCL interneurons noted by Osorno et al. [1]. However, this mapping is inferential rather than experimental: no marker concordance, patch-seq, or direct annotation-transfer evidence is available to confirm that 5178 corresponds to CCs rather than to other PCL-resident cells.

**Table 1 — Property comparison (cluster 5178)**

| Property | Classical | Supertype 1144 | Cluster 5178 | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | not asserted | GABA | CLUS: CONSISTENT |
| Soma location | Purkinje cell layer of cerebellar cortex [UBERON:0002979]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] (region_fraction_100um: 0.699; lower_bound) | Cerebellum [MBA:512] (region_fraction_100um: 0.768; lower_bound) | CONSISTENT (lower_bound caveat) |

**Table 2 — Evidence support (cluster 5178)**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas region + NT metadata | Atlas metadata | PARTIAL | region_fraction_100um=0.768 (lower_bound); GABAergic CONSISTENT | atlas-internal |

*(Child-cluster breakdown not assessed — 5178 is a rank-0 cluster; sibling comparison within supertype 1144 would require surveying all CB PLI cluster members.)*

**Supporting evidence:**
- 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] carries the highest cerebellar region fraction among rank-0 candidates with confirmed GABAergic identity (`region_fraction_100um: 0.768`, strict `region_fraction: 0.680`), both lower-bound.
- Consistent GABAergic annotation (nt_type CONSISTENT) aligns with the established inhibitory identity of CCs [1].
- n=3,066 cells is the largest CB PLI cluster, potentially reflecting the numerical abundance of CCs among PCL interneurons noted by Osorno et al. [1]. *(note: cell count abundance inference is consistent with the literature description but cannot confirm type identity without molecular markers.)*

**Marker evidence provenance:**
- ⚠ **Molecular marker gap (same as for supertype 1144)**: No defining markers on the classical node; no marker comparison possible. See supertype paragraph above for full discussion.

**Concerns:**
- Same lower_bound and laminar-resolution caveats as for supertype 1144.
- Cluster 5178 may represent a heterogeneous population of PCL-resident cells, not exclusively candelabrum cells, if other PCL interneuron types have not been split out in the atlas at this resolution.
- The supertype-to-cluster relationship and sibling cluster profiles (i.e., whether other CB PLI clusters within 1144 are equally plausible) have not been evaluated — this comparison would require surveying all children of 1144.

**What would upgrade confidence:**
- Same marker identification and annotation-transfer experiments as noted for the supertype.
- Patch-seq experiments on morphologically confirmed CCs (biocytin fill confirming small PCL soma + molecular layer axonal arbor), with the resulting transcriptomic profiles mapped to WMBv1 to confirm assignment to 5178 vs. its siblings.

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] | — | 3,646 | 🔴 LOW | CB PLI supertype, cerebellar region (region_fraction_100um: 0.699) | Primary |
| 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] | 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] | 3,066 | 🔴 LOW | CB PLI name + cerebellar region (region_fraction_100um: 0.768) + GABAergic consistent | Secondary (best child within CB PLI supertype) |
| 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] | 1149 CBX MLI Megf11 Gaba_1 | 31,095 | — | MLI cluster (molecular layer, not Purkinje layer) | Eliminated (wrong cortical layer — MLI, not PLI) |
| 1150 CBX MLI Megf11 Gaba_2 [CS20230722_SUPT_1150] | — | 370 | — | MLI supertype (molecular layer) | Eliminated (wrong cortical layer — MLI supertype) |
| 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] | — | 13,098 | — | MLI supertype (molecular layer) | Eliminated (wrong cortical layer — MLI supertype) |
| 1157 Bergmann NN_1 [CS20230722_SUPT_1157] | — | 3,321 | — | Non-neuronal (Bergmann glia) | Eliminated (non-neuronal cell type) |
| 1147 CB PLI Gly-Gaba_4 [CS20230722_SUPT_1147] | — | 442 | — | CB PLI but lower region fraction (0.525) and NT not asserted | Eliminated (weaker regional signal than 1144; NT not assessed) |
| 5079 NTS-PARN Neurod2 Gly-Gaba_1 [CS20230722_CLUS_5079] | 1130 NTS-PARN Neurod2 Gly-Gaba_1 | 212 | — | Primary anatomy Medulla, not cerebellum | Eliminated (brainstem, not cerebellar) |
| 4705 LDT Fgf7 Gaba_1 [CS20230722_CLUS_4705] | 1049 LDT Fgf7 Gaba_1 | 120 | — | Primary anatomy Midbrain/PAG, not cerebellum | Eliminated (midbrain, not cerebellar) |
| 4707 LDT Fgf7 Gaba_1 [CS20230722_CLUS_4707] | 1049 LDT Fgf7 Gaba_1 | 202 | — | Primary anatomy Pons/LDT with boundary cerebellum overlap | Eliminated (lateral dorsal tegmentum, not cerebellar) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The cerebellar candelabrum cell (CC) is defined by CLASSICAL_MULTIMODAL criteria: GABAergic identity ([1], [3]), soma position in the Purkinje cell layer of the cerebellar cortex [UBERON:0002979] ([1], [2]), and a molecularly distinct transcriptomic signature established by snRNAseq (Kozareva et al. 2020 and Osorno et al. 2021/2022 [1]). No positive molecular markers have been formally established in the ingested evidence base, making this a definition grounded primarily on location, neurotransmitter type, and negative distinction from MLIs and Golgi cells.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table:**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1144 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5178 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5188 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1150 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1151 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1157 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1147 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5079 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_4705 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_4707 | ATLAS_METADATA | PARTIAL | atlas-internal |

*Generated by evidencell `8e05bb5` at 2026-07-09T13:25:35+00:00 from [kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml](../../kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Cerebellar candelabrum cell (Purkinje-layer interneuron) → 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] at LOW confidence. Key support: cerebellar regional proximity (region_fraction_100um: 0.699, lower_bound) and atlas cluster nomenclature consistent with Purkinje layer interneuron identity. Key caveats: no molecular markers on classical node; all region fractions are lower-bound estimates; atlas MERFISH cannot resolve Purkinje-layer vs. molecular-layer position at laminar resolution.

This classical type maps directly to the Cell Ontology term candelabrum cell [[CL:4042030](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4042030)] (EXACT mapping).

### Proposed experiments and follow-ups

**Annotation transfer from a CC-enriched source:**
- **What:** Run MapMyCells on a snRNAseq dataset enriched for PCL cells (e.g. Kozareva et al. 2020 or Osorno et al. 2022 data if available), restricting source labels to confirmed CC transcriptomic clusters.
- **Target:** F1 ≥ 0.60 at CLUSTER level (lower threshold given expected biological rarity and small n_cells in CC-specific clusters).
- **Expected output:** AnnotationTransferEvidence on edges to 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] and its CB PLI siblings within supertype 1144.
- **Resolves:** Whether 5178 or a sibling cluster is the true transcriptomic correspondent of CCs.

**Positive marker identification and validation:**
- **What:** Targeted literature review ("candelabrum cell markers cerebellum snRNAseq") and/or fresh snRNAseq marker analysis to extract genes differentially expressed in CC clusters relative to MLIs and GoCs.
- **Expected output:** LiteratureEvidence or MarkerAnalysisEvidence on classical node + marker PropertyComparisons on surviving edges.
- **Resolves:** Whether CB PLI clusters (5178 and siblings) express the CC-defining transcriptomic signature; eliminates the molecular marker gap.

**Patch-seq on morphologically confirmed CCs:**
- **What:** Electrophysiological recording + biocytin fill confirming small PCL soma and characteristic molecular-layer axonal arbor, followed by single-cell sequencing and MapMyCells alignment to WMBv1.
- **Expected output:** AnnotationTransferEvidence with ground-truth source identity, potentially raising confidence to MODERATE or HIGH.
- **Resolves:** Direct confirmation of cluster identity; the only approach that anchors the mapping to morphologically verified CCs.

### Open questions

1. Do any existing published snRNAseq datasets (Kozareva et al. 2020 preprint; Osorno et al. 2021/2022) contain CC-labelled clusters with extractable barcodes that can be mapped to WMBv1 via MapMyCells?
2. Are the "CB PLI" clusters within WMBv1 supertype 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] exhaustive of PCL interneurons, or do additional PLI-type clusters exist at higher resolution that would better isolate CCs from other PCL-resident types?
3. Can supertype 1147 CB PLI Gly-Gaba_4 [CS20230722_SUPT_1147] (eliminated on weaker regional signal) be excluded biologically, or does it represent a distinct PLI population whose relationship to CCs remains open?
4. The classical node notes that CCs preferentially receive Purkinje-collateral input (Lackey et al. 2025) — does any connectivity or synaptic metadata in the atlas allow this circuit property to further constrain the mapping?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Osorno et al. 2022 | [35578131](https://pubmed.ncbi.nlm.nih.gov/35578131/) | Soma location, NT type, CC description |
| [2] | https://doi.org/10.7554/eLife.55569 | — | Soma location |
| [3] | https://doi.org/10.1101/2022.03.03.482855 | — | Neurotransmitter type |

---

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1144 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Atlas supertype 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144]
    is the strongest available atlas placement for the cerebellar candelabrum cell,
    supported by cerebellar regional proximity (region_fraction_100um: 0.699,
    lower_bound rollup) and a supertype name consistent with Purkinje layer
    interneuron soma position. GABAergic identity is confirmed at child-cluster
    level (cluster 5178 nt_type CONSISTENT) but not asserted at supertype level
    (NOT_ASSESSED). No annotation-transfer or molecular marker evidence exists;
    all region fractions are lower_bound estimates due to unpainted CCF2020
    descendants. Confidence is LOW: naming + regional proximity only, no
    experimental anchor. BroadMatch is assigned because multiple CB PLI cluster
    children exist within the supertype and the transcriptomic correspondent has
    not been isolated to a single cluster.
  reconciliation_note: >
    Paired with edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5178 (best
    child cluster within supertype 1144 by cerebellar region fraction and GABAergic
    confirmation). Both verdicts hold at LOW confidence; the supertype-level
    broadMatch + 1:n is the primary call; the cluster-level closeMatch is the
    best-child refinement.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        All region fractions for this candidate are lower_bound estimates — the
        winning rollup row includes non-painted CCF2020 descendants whose cells
        are not counted. The true cerebellar fraction may be higher.
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        No positive molecular markers are recorded on the classical node.
        The mapping rests entirely on regional proximity and atlas cluster
        nomenclature; marker concordance cannot be assessed.
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        WMBv1 MERFISH spatial registration does not resolve Purkinje cell layer
        vs. molecular layer position. The atlas cannot distinguish PCL from MLI
        residence on location alone, so the "CB PLI" cluster label is the
        primary but unverified basis for preferring this supertype over
        MLI supertypes.
  proposed_experiments:
    - >
      Run annotation transfer from a CC-enriched or PCL-enriched snRNAseq source
      (Kozareva et al. 2020 / Osorno et al. 2022 data) onto WMBv1 targeting
      supertype 1144 and its children; aim for F1 ≥ 0.60 at cluster level.
      Expected output: AnnotationTransferEvidence on
      edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1144 and sibling
      cluster edges.
    - >
      Identify at least one positive molecular marker for candelabrum cells via
      targeted literature review or fresh differential expression analysis; add
      as defining_marker to the classical node and compare to atlas cluster
      expression for 5178 and CB PLI siblings.
    - >
      Electrophysiological recording and single-cell sequencing on CCs confirmed
      by light microscopy (PCL soma + molecular-layer beaded axon) to obtain
      ground-truth transcriptomic profiles for direct WMBv1 alignment.
  unresolved_questions:
    - >
      Do published snRNAseq datasets (Kozareva et al. 2020; Osorno et al.
      2021/2022) contain extractable CC-labelled barcodes suitable for
      annotation-transfer alignment to WMBv1?
    - >
      Are CB PLI clusters within supertype 1144 exhaustive of PCL interneurons
      in WMBv1, or do additional PLI-type clusters exist at higher resolution?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5178 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.22
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Cluster 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] is the
    best single cluster within supertype 1144 for candelabrum cell identity:
    highest cerebellar region_fraction_100um: 0.768 (lower_bound) among rank-0
    CB PLI candidates, and nt_type CONSISTENT (GABA confirmed). The cluster
    is the largest in the CB PLI supertype (n=3,066 cells), consistent with
    CCs being described as the most abundant PCL interneuron. No annotation-
    transfer or molecular marker evidence is available. CloseMatch is assigned
    over broadMatch because this is a single cluster candidate; confidence
    remains LOW because the assignment rests on naming and regional proximity
    only.
  reconciliation_note: >
    Paired with edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1144 (parent
    supertype; primary broadMatch + 1:n call). Cluster 5178 is the best child
    within that supertype. See parent verdict block for full evidence discussion.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        region_fraction_100um: 0.768 is a lower_bound estimate; true cerebellar
        fraction may be higher but cannot be confirmed from current atlas paint.
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        No molecular markers available for comparison. Cluster-versus-sibling
        discrimination within supertype 1144 cannot be made on marker grounds.
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Atlas spatial registration cannot distinguish PCL from molecular layer.
        Cluster 5178 may be heterogeneous for PCL vs. adjacent-layer cells.
  proposed_experiments:
    - >
      Annotation transfer from CC-enriched source to WMBv1, targeting cluster
      5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178]; F1 ≥ 0.60 at cluster level
      would support upgrading to MODERATE confidence.
    - >
      Compare sibling clusters within supertype 1144 to determine whether 5178
      or another CB PLI cluster better captures the CC transcriptomic signature
      once markers are established.
  unresolved_questions:
    - >
      Is cluster 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] specifically
      enriched for candelabrum cells, or does it represent a mixed population
      of Purkinje-layer interneurons including other rare PCL-resident types?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5188 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Cluster 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] is
    an MLI (molecular layer interneuron) cluster, not a Purkinje layer
    interneuron. Candelabrum cells reside in the PCL, not the molecular layer;
    the atlas naming is a strong indicator of wrong cortical-layer assignment.
    Eliminated on layer mismatch.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1150 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Supertype 1150 CBX MLI Megf11 Gaba_2 [CS20230722_SUPT_1150] is
    an MLI supertype (molecular layer interneuron). Candelabrum cells are
    Purkinje-layer resident. Eliminated on layer mismatch; NT not asserted
    at supertype level.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1151 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Supertype 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] is
    an MLI supertype (molecular layer interneuron). Candelabrum cells are
    Purkinje-layer resident. Eliminated on layer mismatch; NT not asserted
    at supertype level.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1157 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.02
  rationale: >
    [tier:CUT] Supertype 1157 Bergmann NN_1 [CS20230722_SUPT_1157] is a
    non-neuronal (Bergmann glia) supertype. Candelabrum cells are GABAergic
    neurons. Eliminated — non-neuronal cell type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1147 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] Supertype 1147 CB PLI Gly-Gaba_4 [CS20230722_SUPT_1147] is a
    cerebellar Purkinje layer interneuron supertype, but carries a lower
    cerebellar region_fraction_100um: 0.525 than the primary candidate
    supertype 1144 (region_fraction_100um: 0.699), and NT is not asserted at
    supertype level. With n=442 cells and weaker regional signal, this supertype
    is subordinate to 1144 as a CC candidate. Eliminated on weaker regional
    signal relative to primary survivor.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5079 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.03
  rationale: >
    [tier:CUT] Cluster 5079 NTS-PARN Neurod2 Gly-Gaba_1
    [CS20230722_CLUS_5079] has primary anatomy in the medulla (NTS-PARN:
    nucleus of the solitary tract / parabrachial area region). Although
    Cerebellum [MBA:512] appears in the proximity count, the dominant
    anatomical signal is brainstem medulla. Eliminated — brainstem, not
    cerebellar primary location.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_4705 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.03
  rationale: >
    [tier:CUT] Cluster 4705 LDT Fgf7 Gaba_1 [CS20230722_CLUS_4705] has
    primary anatomy in the midbrain (Periaqueductal gray [MBA:795];
    Midbrain [MBA:313]) and pons. Region_fraction_100um: 0.500 is
    lower-bound; cerebellar cells are a minority of this cluster.
    Eliminated — midbrain/pontine, not cerebellar primary location.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_4707 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.04
  rationale: >
    [tier:CUT] Cluster 4707 LDT Fgf7 Gaba_1 [CS20230722_CLUS_4707] has
    dominant soma signal in Pons [MBA:771] (LDT: lateral dorsal tegmentum),
    with cerebellar boundary overlap (region_fraction_100um: 0.607,
    lower_bound). The LDT is anatomically adjacent to the cerebellum at
    the pontocerebellar border, explaining the proximity signal, but the
    primary type identity is pontine GABAergic. Eliminated — lateral dorsal
    tegmentum primary location, not cerebellar.
```
<!-- verdict-block-end -->
