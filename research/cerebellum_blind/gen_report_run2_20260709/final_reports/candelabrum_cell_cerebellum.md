# Cerebellar candelabrum cell (Purkinje-layer interneuron) — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml`*

---

## Introduction

The cerebellar candelabrum cell (CC) is a molecularly and anatomically distinct inhibitory interneuron of the cerebellar cortex whose soma resides in or near the Purkinje cell layer (PCL) [1][2]. First recognised by light-level morphology in 1994, CCs were long enigmatic — no electrophysiological recordings or molecular markers had been identified until snRNA-seq analysis independently resolved them as a transcriptomically discrete type, separate from both molecular-layer interneurons (MLIs) and Golgi cells [1]. The mapping of CCs to a WMBv1 transcriptomic cluster is therefore a direct test of whether the transcriptomic atlas resolved this previously cryptic population.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Purkinje cell layer of cerebellar cortex [UBERON:0002979]; cerebellar cortex [UBERON:0002129] | [1][2] |
| Neurotransmitter | GABAergic | [1][3] |
| Defining markers | None documented in ingested evidence (see node notes) | — |
| Negative markers | None | — |
| Neuropeptides | None | — |
| Cell Ontology | candelabrum cell [CL:4042030] (EXACT) | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** Literature evidence · cerebellar cortex, Purkinje cell layer · [1][2]

  > CCs were identified in 1994 based on their distinctive light-level morphology (Lainé et al., 1994). CCs have a small cell body near the Purkinje cell layer (PCL), dendrites that extend to the surface of the molecular layer, and beaded axons that make numerous local synapses within the molecular layer. Nothing else was known about CCs because there had been no electrophysiological recordings, and no molecular markers had been identified. In our recent snRNAseq study we identified three types of molecularly distinct inhibitory interneurons in the cerebellar cortex that are neither MLIs or GoCs (Kozareva et al., 2020)
  > — Osorno et al. 2022, Anatomical organization and core cell types · [1] <!-- quote_key: 233245440_70215095 -->

- **Neurotransmitter:** Literature evidence · GABAergic · [1][3]

  > .We find that CCs are the most abundant PC layer interneuron. They are GABAergic, molecularly distinct, and present in all cerebellar lobules. Their high resistance renders CC firing highly sensitive to synaptic inputs. CCs are excited by MFs and granule cells, and strongly inhibited by PCs. CCs in turn inhibit molecular layer interneurons, which leads to PC disinhibition. Thus, inputs, outputs and local signals all converge onto CCs to allow them to assume a unique role in controlling cerebellar output.
  > — Osorno et al. 2022, Anatomical organization and core cell types · [1] <!-- quote_key: 233245440_edf83720 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: candelabrum cell [[CL:4042030](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4042030)] (EXACT).

---

## Results

Annotation-transfer evidence from the Kozareva et al. 2021 mouse cerebellar snRNA-seq dataset (PLI_1 source group, n=1,176 cells; GEO:GSE165371; MapMyCells against WMBv1 CCN20230722) places the candelabrum cell unambiguously on cluster 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] (F1=0.94, Purity=0.95, Coverage=0.94; `at_run_20260709_kozareva_cerebellum_mmc_wmbv1`), with concordant support from the parent supertype 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] (F1=0.72 at supertype level; see property comparison tables). Stage A discovery dominated a 50-member GABAergic-cerebellar cohort (score 6 vs next-best 3), confirming there is no viable competing cluster.

*(Note: the AT run figure (`figures/f1_for_candelabrum_cell_cerebellum.png`) was not generated at report time — run `just gen-at-figure at_run_20260709_kozareva_cerebellum_mmc_wmbv1 --source PLI_1 --output reports/cerebellum_blind/figures/f1_for_candelabrum_cell_cerebellum.png --emit-metrics reports/cerebellum_blind/figures/f1_for_candelabrum_cell_cerebellum_metrics.json` to produce it.)*

---

### 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] · 🟢 HIGH

**Table 1 — Property comparison**

| Property | Classical | Atlas cluster | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT |
| Soma location | Purkinje cell layer of cerebellar cortex [UBERON:0002979]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] `region_fraction_100um`=0.768 (lower_bound rollup) | CONSISTENT |

*(Child-cluster breakdown not assessed — CLUS_5178 is a rank-0 leaf; SUPT_1144 parent context is the relevant supertype breakdown, addressed in the paired supertype paragraph.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | ATLAS_METADATA | PARTIAL | region_fraction_100um=0.768; strict region_fraction=0.680 | atlas-internal |
| Kozareva 2021 PLI_1 MapMyCells | ANNOTATION_TRANSFER | SUPPORT | F1=0.94 at cluster level | atlas-internal |

Annotation-transfer evidence from transcriptomically validated PLI_1 cells (Kozareva et al. 2021; Osorno et al. 2022 [1]) yields an F1=0.94 at cluster resolution onto 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] with purity 0.95 and coverage 0.94 (`at_run_20260709_kozareva_cerebellum_mmc_wmbv1`). The PLI_1 source label in the Kozareva/Osorno atlas corresponds specifically to candelabrum cells per Osorno et al. 2022 [1], giving this AT result the status of direct evidence anchored to a morphologically and transcriptomically characterised source population. Neurotransmitter type is CONSISTENT: both the classical definition (GABAergic [1][3]) and the atlas cluster (annotated GABA) agree. Region location is CONSISTENT: `region_fraction_100um`=0.768 at a lower_bound rollup — the fraction is a floor, with the true cerebellar fraction potentially higher.

**Marker evidence provenance:**
- No positive defining markers are documented for the candelabrum cell in the ingested evidence. The node notes a known gap ("No positive molecular markers reported in the ingested quotes (GAP)"). This does not impair the AT call — the mapping rests on whole-transcriptome AT from a PLI_1 cluster whose CC identity was established by snRNA-seq by the source authors — but it means no independent marker cross-check against the atlas cluster is currently possible.

**Concerns:**
- Region signal is driven by a lower_bound rollup: `region_fraction_100um`=0.768 is a floor; non-painted CCF2020 descendants are uncounted. The true fraction is likely higher (weak caveat — direction of uncertainty supports rather than undermines the call).
- No positive molecular markers are available on the classical node to cross-validate atlas-side marker annotations. A literature search for candelabrum cell-specific transcripts beyond the Kozareva/Osorno panels would strengthen the evidence base.

**What would upgrade confidence:**
- Identification and curation of one or more defining molecular markers for candelabrum cells from primary literature (e.g. targeted literature search for CC-specific transcripts in the Kozareva 2021 supplementary or Osorno 2022 data). This would enable a marker-level cross-check against CLUS_5178 precomputed expression.
- An independent AT run from a second cerebellar dataset targeting the Purkinje cell layer population would add replication of the F1=0.94 result.

---

### 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] · 🟢 HIGH

**Table 1 — Property comparison**

| Property | Classical | Supertype | Alignment |
|---|---|---|---|
| NT type | GABAergic | not asserted at supertype level | NOT_ASSESSED |
| Soma location | Purkinje cell layer of cerebellar cortex [UBERON:0002979]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] `region_fraction_100um`=0.699 (lower_bound rollup) | CONSISTENT |

*(Best child within supertype: CLUS_5178, F1=0.94 — full breakdown in paired cluster paragraph above.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | ATLAS_METADATA | PARTIAL | region_fraction_100um=0.699; strict region_fraction=0.610 | atlas-internal |
| Kozareva 2021 PLI_1 MapMyCells | ANNOTATION_TRANSFER | SUPPORT | F1=0.72 at supertype level | atlas-internal |

The parent supertype 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] captures PLI_1 cells at F1=0.72 at supertype resolution (coverage=0.953, purity=0.576; `at_run_20260709_kozareva_cerebellum_mmc_wmbv1`). The reduced purity compared to the cluster (0.58 vs 0.95) reflects that the supertype pools CLUS_5178 together with sibling clusters; the high coverage (0.953) shows nearly all PLI_1 cells land within this supertype's lineage. Region location is CONSISTENT at `region_fraction_100um`=0.699 (lower_bound floor; direction of uncertainty supports the call). This supertype edge is supported as a broadMatch pairing to the cluster edge: both map the same biological population, with CLUS_5178 being the best-resolution target and SUPT_1144 confirming the lineage context.

**Concerns:**
- NT type NOT_ASSESSED at supertype level (supertype-level NT not asserted in atlas metadata). The cluster-level GABA annotation on CLUS_5178 provides the NT anchor; this is an atlas metadata gap at supertype resolution, not a contradiction.
- Region signal is lower_bound rollup (`region_fraction_100um`=0.699 vs cluster `region_fraction_100um`=0.768) — same data governance caveat applies.

**What would upgrade confidence:**
- This edge is already HIGH given the cluster-level AT anchor. No additional experiments specifically needed for the supertype edge beyond those listed for CLUS_5178.

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---:|---|---|---|---|
| 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] | 1144 CB PLI Gly-Gaba_1 | 3,066 | 🟢 HIGH | PLI_1 AT F1=0.94 clean 1:1 cluster | Primary |
| 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] | — | 3,646 | 🟢 HIGH | PLI_1 AT F1=0.72 at supertype; best child CLUS_5178 | Supports broader mapping |
| 4707 LDT Fgf7 Gaba_1 [CS20230722_CLUS_4707] | 1049 LDT Fgf7 Gaba_1 | 202 | 🔴 LOW | PLI_1 does not transfer (no AT metrics) | Eliminated (AT no transfer; brainstem LDT lineage) |
| 4705 LDT Fgf7 Gaba_1 [CS20230722_CLUS_4705] | 1049 LDT Fgf7 Gaba_1 | 120 | 🔴 LOW | PLI_1 does not transfer; midbrain/pons location | Eliminated (AT no transfer; off-region) |
| 5079 NTS-PARN Neurod2 Gly-Gaba_1 [CS20230722_CLUS_5079] | 1130 NTS-PARN Neurod2 Gly-Gaba_1 | 212 | 🔴 LOW | PLI_1 does not transfer; medulla location | Eliminated (AT no transfer; medulla lineage) |
| 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] | 1149 CBX MLI Megf11 Gaba_1 | 31,095 | 🔴 LOW | PLI_1 AT F1=0.05 at class only (CB GABA) | Eliminated (MLI cluster; AT class-only F1=0.05) |
| 1150 CBX MLI Megf11 Gaba_2 [CS20230722_SUPT_1150] | — | 370 | 🔴 LOW | PLI_1 AT F1=0.05 at class only | Eliminated (MLI supertype; AT class-only) |
| 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] | — | 13,098 | 🔴 LOW | PLI_1 AT F1=0.05 at class only | Eliminated (MLI supertype; AT class-only) |
| 1157 Bergmann NN_1 [CS20230722_SUPT_1157] | — | 3,321 | 🔴 LOW | PLI_1 no AT transfer; Bergmann glia lineage | Eliminated (non-neuronal Bergmann glia type) |
| 1147 CB PLI Gly-Gaba_4 [CS20230722_SUPT_1147] | — | 442 | 🔴 LOW | PLI_1 best AT at subclass level only (F1=0.63) | Eliminated (subclass-level only; SUPT_1144 supertype preferred) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The candelabrum cell is defined as a `CLASSICAL_MULTIMODAL` node based on morphological, anatomical, and transcriptomic evidence. Soma location is in the Purkinje cell layer of the cerebellar cortex [UBERON:0002979] and cerebellar cortex [UBERON:0002129] [1][2]. Neurotransmitter type is GABAergic [1][3]. No positive defining molecular markers have been curated — this is a recognised gap in the current KB node, flagged in node notes.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE165371 (PLI_1 — candelabrum) |
| Source species | NCBITaxon:10090 (mouse) |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper 1.7.1, default parameters, 100 bootstrap iterations) |
| Tool version | cell_type_mapper 1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 45,555 total (interneuron subset; filtered to 45,555) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md ([f4ce9b9](https://github.com/Cellular-Semantics/evidencell/blob/f4ce9b99657bf2be34f6a3f236ba9c45b0d22cce/README.md)) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/f1_scores_best.csv) |
| Caveats | Same-species (mouse) snRNA-seq → WMBv1. Source cluster labels are transcriptomic (Kozareva/Osorno) with high marker validation — treat cluster-level F1 as informative (pure-source expectation). PLI clusters are rare (candelabrum 1,176; globular 735; Lugaro 531 cells). MLI1_1 (basket) and MLI1_2 (stellate) both map to CLUS_5188 with high coverage but MLI1_1 purity is low (0.34) — the two morphological types share the MLI1 transcriptomic cluster (cross-cutting). MLI2 maps cleanly to CLUS_5192 (F1=0.996). Blind-run note: this reproduces the curator ground-truth AT anchors (candelabrum 5178 F1=0.94, globular 5177 F1=0.88, Lugaro SUPT_1145 F1=0.96) without those targets ever being supplied to the pipeline. Gene symbols remapped to Ensembl IDs via conf/gene_mapping_CCN20230722.tsv (20,390/23,203 genes mapped). BKP web backend was unavailable (HTTP 400) at run time; local backend used. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `f4ce9b9` at 2026-07-09T18:53:52+00:00 from [kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml](kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml).*

**Evidence base table**

<details>
<summary>Evidence items per edge</summary>

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5178 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | atlas-internal; at_run_20260709_kozareva_cerebellum_mmc_wmbv1 |
| edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1144 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | atlas-internal; at_run_20260709_kozareva_cerebellum_mmc_wmbv1 |
| edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_4707 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal; at_run_20260709_kozareva_cerebellum_mmc_wmbv1 |
| edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_4705 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal; at_run_20260709_kozareva_cerebellum_mmc_wmbv1 |
| edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5079 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal; at_run_20260709_kozareva_cerebellum_mmc_wmbv1 |
| edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5188 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal; at_run_20260709_kozareva_cerebellum_mmc_wmbv1 |
| edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1150 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal; at_run_20260709_kozareva_cerebellum_mmc_wmbv1 |
| edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1151 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal; at_run_20260709_kozareva_cerebellum_mmc_wmbv1 |
| edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1157 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal; at_run_20260709_kozareva_cerebellum_mmc_wmbv1 |
| edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1147 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal; at_run_20260709_kozareva_cerebellum_mmc_wmbv1 |

</details>

</details>

---

## Discussion

### Best candidate and caveats

**Primary mapping:** Cerebellar candelabrum cell (Purkinje-layer interneuron) → 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] at HIGH confidence. Key support: annotation-transfer (F1=0.94 at cluster level; PLI_1 source label validated as candelabrum-specific by Osorno et al. 2022 [1]) and atlas metadata (region consistent; GABAergic NT consistent). Key caveats: region_fraction_100um is a lower-bound rollup floor; no positive defining molecular markers available on the classical node for independent cross-check.

This classical type maps directly to the Cell Ontology term candelabrum cell [[CL:4042030](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4042030)].

The supertype 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] is the natural parent container: AT lands on this supertype at F1=0.72 with coverage 0.953, confirming that nearly all PLI_1 source cells fall within this lineage. The primary resolution is the cluster-level mapping to CLUS_5178; the supertype edge documents the broader lineage context.

### Proposed experiments and follow-ups

**1. Molecular marker identification for candelabrum cells.**
- **What:** Targeted literature search for CC-specific transcripts, particularly in Kozareva et al. 2021 supplementary data and Osorno et al. 2022 [1] cluster marker tables.
- **Target:** At least one defining marker with transcript-level evidence, detectable in WMBv1 precomputed expression on CLUS_5178.
- **Expected output:** `defining_markers` added to the classical node; cross-check against `property_comparisons` for CLUS_5178 and SUPT_1144.
- **Resolves:** Marker gap (currently no positive defining markers on node); would enable independent validation of the AT mapping beyond PLI_1 source label identity.

**2. Independent annotation-transfer replication.**
- **What:** If a second mouse cerebellar cortex snRNA-seq dataset with PLI/candelabrum annotations becomes available, run MapMyCells against WMBv1 CCN20230722.
- **Target:** F1 ≥ 0.80 at cluster level on CLUS_5178.
- **Expected output:** Second `AnnotationTransferEvidence` item on `edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5178`.
- **Resolves:** Replication of the F1=0.94 result from a single source dataset; would further consolidate HIGH confidence.

### Open questions

1. What positive molecular markers distinguish candelabrum cells from other Purkinje-layer inhabitants (including Bergmann glia and Purkinje cells themselves)? The current node carries no defining markers — a gap noted by Osorno et al. 2022 [1] who also found CCs transcriptomically distinct but did not report individual discriminating genes in the ingested evidence.

2. Does the 309 CB PLI Gly-Gaba subclass contain additional sibling supertypes with biological relevance to candelabrum cell heterogeneity? SUPT_1147 (1147 CB PLI Gly-Gaba_4) and other PLI siblings within this subclass show lower AT support from PLI_1 but share a common PLI transcriptomic lineage.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Osorno et al. 2022 | [35578131](https://pubmed.ncbi.nlm.nih.gov/35578131/) | soma location, neurotransmitter type, candelabrum cell characterisation |
| [2] | https://doi.org/10.7554/eLife.55569 | — | soma location |
| [3] | https://doi.org/10.1101/2022.03.03.482855 | — | neurotransmitter type |

---

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5178 -->
```yaml
verdict:
  confidence: HIGH
  confidence_score: 0.92
  relationship: skos:exactMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] AT transfer of PLI_1 (candelabrum source label per Osorno et al. 2022;
    PMID:35578131) to CS20230722_CLUS_5178 yields F1=0.94 (coverage=0.94, purity=0.95)
    at cluster level in at_run_20260709_kozareva_cerebellum_mmc_wmbv1. Stage A discovery
    dominated a 50-member GABAergic-cerebellar cohort (score 6, next-best 3). NT type
    CONSISTENT (GABAergic / GABA). Region CONSISTENT (region_fraction_100um=0.768,
    lower_bound floor — true value may be higher). No positive defining markers available
    for cross-check (known gap). Clean 1:1 mapping with no viable competing cluster.
  reconciliation_note: >
    Paired with edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1144 (parent supertype;
    AT F1=0.72 at supertype level in same run). Cluster edge is the primary resolution;
    supertype edge documents the lineage context. Both survivors represent the same
    biological call at two resolutions.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        region_fraction_100um=0.768 is a lower_bound rollup — non-painted CCF2020
        descendants are uncounted; the true cerebellar fraction is at least this value
        and likely higher. This is a weak caveat whose direction supports rather than
        undermines the call.
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        No positive defining molecular markers are documented for the candelabrum cell
        in the ingested evidence. The mapping rests entirely on whole-transcriptome AT
        from a source label whose CC identity was established by the source authors;
        no independent marker cross-check against CLUS_5178 precomputed expression
        is currently possible.
  proposed_experiments:
    - >
      Identify at least one defining molecular marker for candelabrum cells via targeted
      literature search (Kozareva 2021 supplementary, Osorno 2022 [1] cluster tables);
      curate onto classical node and cross-check against CLUS_5178 precomputed expression.
    - >
      If a second mouse cerebellar snRNA-seq dataset with PLI/candelabrum annotations
      is available, run MapMyCells against WMBv1 CCN20230722; target F1 ≥ 0.80 at
      cluster level; attach result as AnnotationTransferEvidence to this edge.
  unresolved_questions:
    - >
      What positive molecular markers distinguish candelabrum cells from other
      Purkinje-layer inhabitants? Current node carries no defining markers — gap
      noted in node notes and literature.
    - >
      Do other PLI subtype siblings within subclass 309 CB PLI Gly-Gaba show biological
      relevance to candelabrum cell heterogeneity (SUPT_1147 and other CB PLI Gly-Gaba
      supertypes)?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1144 -->
```yaml
verdict:
  confidence: HIGH
  confidence_score: 0.85
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] AT transfer of PLI_1 to CS20230722_SUPT_1144 yields F1=0.72
    (coverage=0.953, purity=0.576) at supertype level in
    at_run_20260709_kozareva_cerebellum_mmc_wmbv1. Nearly all PLI_1 cells land within
    this supertype lineage; reduced purity reflects pooling of CLUS_5178 with sibling
    clusters at supertype resolution. Region CONSISTENT (region_fraction_100um=0.699,
    lower_bound floor). NT NOT_ASSESSED at supertype level (atlas metadata gap).
    Supertype edge documents lineage context; primary resolution is the paired cluster
    edge to CS20230722_CLUS_5178 (skos:exactMatch).
  reconciliation_note: >
    Paired with edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5178 (best child
    cluster; exactMatch at cluster level). This supertype edge is a broadMatch pairing:
    it captures the full PLI lineage context while CLUS_5178 is the best-resolution
    1:1 target. Readers should consult both edges together.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        region_fraction_100um=0.699 is a lower_bound rollup at supertype level.
        Same data governance caveat as cluster edge; true fraction likely higher.
    - caveat_type: NT_PREDICTION_UNCERTAIN
      description: >
        NT type NOT_ASSESSED at supertype level (atlas metadata gap for SUPT_1144);
        cluster-level GABA annotation on CLUS_5178 provides the NT anchor.
  proposed_experiments:
    - >
      No additional experiments specifically targeting the supertype edge beyond those
      listed for the paired CLUS_5178 cluster edge; marker identification and AT
      replication address both edges simultaneously.
  unresolved_questions:
    - >
      NT type annotation at supertype level is missing for CS20230722_SUPT_1144
      in atlas metadata — this is an atlas-side gap, not a biological uncertainty.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_4707 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] AT transfer of PLI_1 does not reach CS20230722_CLUS_4707 lineage
    in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 (NO_EVIDENCE; no metrics rows).
    Cluster is annotated as a brainstem LDT (laterodorsal tegmentum) Fgf7 type —
    anatomically inconsistent with a cerebellar Purkinje-layer interneuron.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_4705 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.04
  rationale: >
    [tier:CUT] AT transfer of PLI_1 does not reach CS20230722_CLUS_4705 lineage
    in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 (NO_EVIDENCE; no metrics rows).
    Cluster primary soma location is midbrain/pons — anatomically distant from the
    cerebellar Purkinje cell layer. Region signal (region_fraction_100um=0.500, lower_bound)
    driven by Midbrain [MBA:313] and Periaqueductal gray [MBA:795], not cerebellum.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5079 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.04
  rationale: >
    [tier:CUT] AT transfer of PLI_1 does not reach CS20230722_CLUS_5079 lineage
    in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 (NO_EVIDENCE; no metrics rows).
    Cluster primary soma location is medulla/area postrema — anatomically distant
    from the cerebellar cortex.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_CLUS_5188 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.03
  rationale: >
    [tier:CUT] AT transfer of PLI_1 to CS20230722_CLUS_5188 (CBX MLI Megf11 Gaba_1)
    achieves F1=0.05 at class level only (28 CB GABA) in
    at_run_20260709_kozareva_cerebellum_mmc_wmbv1 — class-level F1 reflects shared
    CB GABA lineage, not a specific mapping. This is the canonical MLI1 cluster
    (basket + stellate cells); candelabrum cells are transcriptomically distinct
    from MLIs per Kozareva/Osorno.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1150 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.03
  rationale: >
    [tier:CUT] AT transfer of PLI_1 to CS20230722_SUPT_1150 (CBX MLI Megf11 Gaba_2)
    achieves F1=0.05 at class level only in at_run_20260709_kozareva_cerebellum_mmc_wmbv1.
    MLI supertype; candelabrum cells are transcriptomically distinct from MLIs.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1151 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.03
  rationale: >
    [tier:CUT] AT transfer of PLI_1 to CS20230722_SUPT_1151 (CBX MLI Cdh22 Gaba_1)
    achieves F1=0.05 at class level only in at_run_20260709_kozareva_cerebellum_mmc_wmbv1.
    MLI supertype; candelabrum cells are transcriptomically distinct from MLIs.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1157 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.02
  rationale: >
    [tier:CUT] AT transfer of PLI_1 does not reach CS20230722_SUPT_1157 lineage
    in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 (NO_EVIDENCE; no metrics rows).
    SUPT_1157 is annotated as a Bergmann glia (non-neuronal) type — biologically
    inconsistent with a GABAergic interneuron.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_candelabrum_cell_cerebellum_to_CS20230722_SUPT_1147 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] AT transfer of PLI_1 reaches CS20230722_SUPT_1147 (CB PLI Gly-Gaba_4)
    at best F1=0.63 at subclass level (309 CB PLI Gly-Gaba) in
    at_run_20260709_kozareva_cerebellum_mmc_wmbv1. The best mapping rank is 2
    (subclass), not supertype or cluster — PLI_1 does not specifically resolve
    to SUPT_1147 vs other PLI siblings. The canonical PLI supertype target is
    SUPT_1144, which captures the lineage at supertype resolution; SUPT_1147 is a sibling
    within the same CB PLI Gly-Gaba subclass lineage but without supertype-specific
    AT evidence. Region_fraction_100um=0.525 (lower_bound) is lower than SUPT_1144 (0.699).
```
<!-- verdict-block-end -->
