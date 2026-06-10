# Basolateral amygdala axo-axonic (chandelier) cell — CCN20230722 Mapping Report
*2026-06-05 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala (BLA) axo-axonic cell, also known as the chandelier cell, is a classically defined GABAergic interneuron that selectively targets the axon initial segment (AIS) of excitatory principal neurons. Bienvenu et al. 2012 established this cell type in the mouse BLA using in-vivo juxtacellular labeling, showing that all axo-axonic cells express parvalbumin (PV) and are never calbindin-positive [4]. Vereczki et al. 2021 estimated that axo-axonic cells constitute approximately 5.5–6% of all GABAergic cells in the lateral and basal amygdala [1], and Raudales et al. 2024 demonstrated using genetic targeting and AnkyrinG co-staining that axo-axonic cells are present across all amygdala nuclei containing glutamatergic principal neurons — including the lateral, basal, basomedial, cortical, and medial amygdala — but are absent from the central amygdala [2]. Mapping this type to the WMBv1 transcriptomic atlas provides a molecular anchor for the classical PV-expressing, AIS-targeting interneuron identity.

### Classical type description

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1], [2] |
| NT type | GABAergic | [1] |
| Defining marker | Pvalb (PV protein; expressed in all axo-axonic cells, sometimes weakly; never calbindin-positive) | [1], [3], [4] |
| Negative markers | Sst | — |
| Neuropeptides | None documented | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / GABAergic NT / Pvalb defining marker (population estimate):** ASTA report synthesis · amygdala/hippocampus literature · [1]
  > we estimated that the following cell types together compose the vast majority of GABAergic cells in the LA and BA: axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%). Our results show that these amygdalar nuclei contain all major GABAergic neuron types as found in other cortical regions.
  > — Vereczki et al. 2021, Basolateral amygdala neuronal subtypes · [1] <!-- quote_key: 232283078_d4238834 -->

- **Soma location (nuclear distribution, genetic targeting):** genetic targeting + AnkG co-staining · mouse brain-wide AAC targeting · [2]
  > we found AACs or pAACs in all the amygdala nuclei containing GLU PNs, that is except CeA
  > — Raudales et al. 2024, AACs in the amygdaloid complex and exten · [2] <!-- quote_key: 271240390_c5dcc7db -->

- **Pvalb defining marker (PV+ interneuron populations in BLA context):** review · rat BLA · [3]
  > Four populations of interneurons have been described in the BLA: those expressing parvalbumin (McDonald, 1992;Mc-Donald and Betette, 2001), those expressing somatostatin (Mc-Donald and Mascagni, 2002), those expressing cholecystokinin and either cal
  > — Woodruff & Sah 2007, Introduction · [3] <!-- quote_key: 161407_e34026c5 -->

- **Pvalb defining marker (all axo-axonic cells PV+, never calbindin-positive):** in-vivo juxtacellular labeling · mouse BLA · [4]
  > All axo-axonic cells expressed parvalbumin (PV), sometimes weakly (Figure 1F), but were never calbindin (CB)-positive.
  > — Bienvenu et al. 2012, Results · [4] <!-- quote_key: 10647550_e0390ac0 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: pvalb chandelier GABAergic interneuron [[CL:4023036](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023036)] (BROAD).

The Cell Ontology has no current term specific to the BLA axo-axonic population; CL:4023036 (pvalb chandelier GABAergic interneuron) is the closest ancestor. The auto-proposed BROAD mapping requires expert review to determine whether CL:4023036 is appropriate as a broadMatch or whether a BLA-specific new term is warranted.

---

## Results

One candidate atlas cluster was assessed: CS20230722_CLUS_0733 "0733 Pvalb chandelier Gaba_1" [CS20230722_CLUS_0733], carrying a `skos:closeMatch` 1:1 relationship at MODERATE confidence. The explicit "chandelier" label in both the cluster and its parent supertype provides direct nomenclature correspondence to axo-axonic cell identity, and MapMyCells annotation transfer (Hochgerner et al. 2023; F1=0.99 at CLUSTER level) provides an experimental anchor anchoring the closeMatch.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0733 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0733] | 0204 Pvalb chandelier Gaba_1 | 3,161 | 🟡 MODERATE | Pvalb CONSISTENT · chandelier label CONSISTENT · AT F1=0.99 | `skos:closeMatch` |

*1 edge assessed; 1 MODERATE. Relationship type: `skos:closeMatch` (1:1).*

#### Property alignment — 0733 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0733] · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | GABA | CONSISTENT |
| Soma location | Basolateral amygdala [UBERON:0002887] | MBA:295 BLA ~4% of cluster; wider cortical/subplate distribution | MBA:295 BLA ~4% of cluster | APPROXIMATE |
| Pvalb expression | Pvalb — defining marker | Pvalb precomputed mean 6.38 (97.8th pct in BLA GABAergic cohort; tier 2) | Pvalb precomputed mean 6.38 [CS20230722_CLUS_0733] | CONSISTENT |
| Chandelier / AIS-targeting identity | axo-axonic (chandelier) — AIS-targeting | "Pvalb chandelier Gaba_1" (SUPT_0204) | "0733 Pvalb chandelier Gaba_1" [CS20230722_CLUS_0733] | CONSISTENT |
| Sst expression (negative) | Sst — negative marker | not in precomputed data for CS20230722_CLUS_0733 | not in precomputed data for CS20230722_CLUS_0733 | NOT_ASSESSED |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Bienvenu et al. 2012 BLA interneuron classification | Literature | SUPPORT | PV+ AIS-targeting identity confirmed | [4] |
| WMBv1 atlas label — "Pvalb chandelier Gaba_1" | Atlas metadata | SUPPORT | Direct chandelier label correspondence at cluster and supertype level | atlas-internal |
| Hochgerner 2023 MapMyCells AT | Annotation transfer | SUPPORT | F1=0.99 (CLUSTER level, GABA-44-Pthlh-Pvalb→CS20230722_CLUS_0733; n=88 cells) | atlas-internal |

*(Child-cluster breakdown not assessed — CS20230722_CLUS_0733 is a rank-0 cluster with no further subdivision in CCN20230722.)*

### 0733 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0733] · 🟡 MODERATE

**Supporting evidence:**

- **Atlas label correspondence (CONSISTENT):** The WMBv1 cluster CS20230722_CLUS_0733 is explicitly labeled "0733 Pvalb chandelier Gaba_1", and its parent supertype CS20230722_SUPT_0204 is labeled "0204 Pvalb chandelier Gaba_1". The term "chandelier" in the CCN20230722 taxonomy nomenclature is synonymous with axo-axonic cell identity, providing direct label-based evidence for this mapping. Both cluster and supertype carry the chandelier designation, making this a label-explicit closeMatch.

- **Pvalb expression (CONSISTENT):** Pvalb precomputed mean expression = 6.38 in CS20230722_CLUS_0733, placing it at the 97.8th percentile of the BLA GABAergic survival cohort (rank 1 of 5 at rank 0, n=5 members). The atlas-side Pvalb value is fully consistent with the classical type's defining marker requirement. Bienvenu et al. 2012 [4] confirmed with in-vivo juxtacellular labeling that all BLA axo-axonic cells express PV (sometimes weakly):

  > All axo-axonic cells expressed parvalbumin (PV), sometimes weakly (Figure 1F), but were never calbindin (CB)-positive.
  > — Bienvenu et al. 2012, Results · [4] <!-- quote_key: 10647550_e0390ac0 -->

- **NT type (CONSISTENT):** Both classical type (GABAergic) and CS20230722_CLUS_0733 (GABA) are consistent.

- **MapMyCells annotation transfer (SUPPORT):** The Hochgerner 2023 deep amygdala scRNA-seq dataset (ArrayExpress:E-MTAB-12096; n=88 fear-naive GABAergic cells in source cluster GABA-44-Pthlh-Pvalb) mapped to CS20230722_CLUS_0733 with F1=0.99 at CLUSTER level and F1=0.98 at both SUPERTYPE and SUBCLASS levels (run `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`). Purity = 1.0 at CLUSTER level (all cells assigned to CS20230722_CLUS_0733 come from this source group). This is an extremely clean single-cluster mapping providing strong experimental support for the nomenclature-based closeMatch.

- **Stage A discovery:** CS20230722_CLUS_0733 ranked 1st in the 5-member BLA GABAergic cohort (score = 3; next-best = 3, tied cohort at rank 0). The score reflects NT match and Pvalb tier-2 expression (applied_score = 2.0 from EXPRESSION source, not METADATA). *(note: The tied next-best score means Stage A alone does not discriminate this candidate from others in the cohort; the chandelier atlas label and Bienvenu 2012 literature are the primary differentiators for axo-axonic cell identity specifically.)*

**Marker evidence provenance:**

- **Pvalb:** Evidence is from in-vivo juxtacellular labeling of cells confirmed to have axo-axonic morphology (Bienvenu et al. 2012 [4], mouse BLA). Cells were included only after confirming the AIS-targeting axon morphology post-hoc, providing strong cell-type specificity. The ASTA synthesis [1] and Woodruff & Sah 2007 review [3] (rat BLA) provide corroborating context across species. Atlas-side Pvalb value (mean 6.38) is derived from precomputed expression data (source: EXPRESSION), making this a well-grounded two-sided CONSISTENT alignment.

- **Sst (negative marker):** Sst is listed as a negative marker to distinguish axo-axonic cells from somatostatin-expressing dendrite-targeting interneurons. Sst in CS20230722_CLUS_0733 is NOT_ASSESSED because Sst precomputed expression data is unavailable for this cluster. Confirmation of Sst absence would strengthen the marker profile and convert this alignment from NOT_ASSESSED to CONSISTENT.

**Concerns:**

- **Soma location APPROXIMATE — pan-cortical chandelier type:** The `location_soma` comparison is APPROXIMATE. CS20230722_CLUS_0733 has only approximately 4% of its 3,161 cells in MBA:295 (basolateral amygdala; region_fraction = 0.042), well below the boundary band of 0.3–0.7. The cluster is broadly distributed across cortical and subplate regions. This reflects the known pan-cortical biology of chandelier cells: the WMBv1 atlas groups all Pvalb chandelier cells into a single cluster regardless of specific brain region. *(note: chandelier cells are a functionally specialised type that spans neocortex, hippocampus, and amygdala — the low BLA region_fraction reflects atlas grouping structure rather than a biological mismatch, and the APPROXIMATE alignment is a known caveat rather than counter-evidence against identity.)* The mapped cluster represents the full chandelier cell class, not a BLA-specific population.

- **Sst NOT_ASSESSED:** The classical type's negative marker (Sst) cannot be confirmed absent in CS20230722_CLUS_0733 from available data.

**What would upgrade confidence:**

- **Annotation transfer already completed** (F1=0.99 CLUSTER level; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`). Confidence is currently MODERATE. To reach HIGH, patch-seq mapping of morphologically confirmed BLA axo-axonic cells would be required (exactMatch + patch-seq AT F1>0.75).
- **Sst expression quantification** in CS20230722_CLUS_0733 from precomputed stats would resolve the NOT_ASSESSED negative-marker alignment.
- **Targeted literature search** for "axo-axonic chandelier cell amygdala transcriptomics" may identify additional markers distinguishing axo-axonic from PV+ basket cells at transcript level.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The BLA axo-axonic (chandelier) cell is defined on a CLASSICAL basis (`definition_basis: CLASSICAL`). The defining marker is Pvalb (protein level; [3], [4]), supported by the ASTA synthesis report [1] and confirmed by in-vivo juxtacellular labeling in mouse BLA (Bienvenu et al. 2012 [4]: all axo-axonic cells PV+, never calbindin-positive). Sst is recorded as a negative marker, distinguishing axo-axonic cells from somatostatin-expressing dendrite-targeting interneurons in the BLA. NT type is GABAergic [1]. Soma location is basolateral amygdala [UBERON:0002887] [1], [2], with genetic-targeting evidence extending presence to all amygdala nuclei containing glutamatergic principal neurons except the central amygdala [2].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.** MapMyCells annotation transfer using the Hochgerner 2023 fear-naive amygdala scRNA-seq dataset.

| Field | Value |
|---|---|
| Source dataset | ArrayExpress:E-MTAB-12096 (GABA-44-Pthlh-Pvalb, n=88 fear-naive cells) |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization) |
| Run record | `kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml` |
| F1 matrix | `kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/f1_matrix.csv` |
| Caveats | Fear-conditioned cells excluded; n=88 is fear-naive subset only |

**Atlas data sources.** CCN20230722 · taxonomy YAML under `kb/taxonomy/CCN20230722/`. No pseudobulk SHA-256 emitted (atlas_data_sources list empty in facts file).

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_axo_axonic_cell_to_cs20230722_clus_0733 | LITERATURE; ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT; SUPPORT; SUPPORT | [4], atlas-internal, at_run_20260609 |

*Generated by evidencell `c4efa0e` at 2026-06-05T13:42:46+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala axo-axonic (chandelier) cell → 0733 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0733] at MODERATE confidence. Key support: explicit "chandelier" label in WMBv1 atlas at cluster and supertype level; MapMyCells AT F1=0.99 (CLUSTER level, Hochgerner 2023, `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`); Pvalb CONSISTENT [4]. Key caveats: DISTRIBUTED_ACROSS_CLUSTERS (pan-cortical type, region_fraction=0.042 in BLA); scRNA-seq AT, not patch-seq.

The Cell Ontology has no BLA-specific axo-axonic cell term; CL:4023036 (pvalb chandelier GABAergic interneuron) is the closest ancestor. The BROAD mapping type indicates that CL:4023036 does not specifically cover the BLA population. A BLA-specific new CL term contribution may be appropriate once transcriptomic identity is confirmed by annotation transfer.

### Proposed experiments and follow-ups

MapMyCells annotation transfer has been completed using Hochgerner 2023 data (F1=0.99 at CLUSTER level). Confidence is now MODERATE. The following experiments would further strengthen the mapping:

#### 1. Patch-seq mapping of morphologically confirmed BLA axo-axonic cells

- **What:** Patch-seq of morphologically confirmed (AnkG co-staining or post-hoc fill + AIS reconstruction) BLA axo-axonic cells, then MapMyCells mapping against CCN20230722.
- **Target:** F1 > 0.75 at CLUSTER level (patch-seq anchor for exactMatch upgrade).
- **Expected output:** HIGH confidence if target met; would confirm that the ~4% of CS20230722_CLUS_0733 cells in BLA specifically represent axo-axonic cells.
- **Resolves:** Open question 1 (whether the BLA component of CLUS_0733 is axo-axonic).

#### 2. Sst expression quantification in CS20230722_CLUS_0733

- **What:** Retrieve or compute Sst expression value for CS20230722_CLUS_0733 from precomputed stats or atlas metadata to confirm the NOT_ASSESSED negative-marker alignment.
- **Target:** Sst mean expression < 0.5 (absence confirmed) to convert NOT_ASSESSED to CONSISTENT for the negative marker.
- **Expected output:** Updated `negative_marker_Sst` property_comparison.
- **Resolves:** Open question 2; Sst NOT_ASSESSED gap.

#### 3. Targeted literature search for BLA axo-axonic cell transcriptomics

- **What:** Targeted cite-traverse for "axo-axonic chandelier cell amygdala transcriptomics" and "PV chandelier BLA scRNA-seq".
- **Target:** LiteratureEvidence item identifying a distinguishing marker (beyond Pvalb) separating axo-axonic from PV+ basket cells in BLA.
- **Expected output:** Additional defining or negative markers on the classical node; potential CONSISTENT alignment for a second marker.
- **Resolves:** Open question 3; reliance on Pvalb alone for axo-axonic vs. basket cell specificity.

### Open questions

1. Does CS20230722_CLUS_0733 resolve cleanly to axo-axonic cells in MBA:295 by AnkG co-staining, i.e. do the ~4% of CS20230722_CLUS_0733 cells in the BLA specifically target the AIS? (Edge: `edge_bla_axo_axonic_cell_to_cs20230722_clus_0733`)

2. Can Sst absence be confirmed in CS20230722_CLUS_0733 from precomputed stats? (Edge: `edge_bla_axo_axonic_cell_to_cs20230722_clus_0733`)

3. Are there additional markers beyond Pvalb that distinguish BLA axo-axonic cells from BLA PV+ basket cells at transcript level in CCN20230722? Both cell types are Pvalb+ and would map to CS20230722_CLUS_0733 without further discrimination. (Edge: `edge_bla_axo_axonic_cell_to_cs20230722_clus_0733`)

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Vereczki et al. 2021 | [33837051](https://pubmed.ncbi.nlm.nih.gov/33837051/) | Soma location; GABAergic NT; Pvalb defining marker; population proportion estimate |
| [2] | Raudales et al. 2024 | [39012795](https://pubmed.ncbi.nlm.nih.gov/39012795/) | Soma location; nuclear distribution of AACs across amygdala (GLU PN-containing nuclei only) |
| [3] | Woodruff & Sah 2007 | [17234587](https://pubmed.ncbi.nlm.nih.gov/17234587/) | Pvalb as a defining marker of BLA interneuron populations |
| [4] | Bienvenu et al. 2012 | [22726836](https://pubmed.ncbi.nlm.nih.gov/22726836/) | Pvalb protein expression in all axo-axonic cells (sometimes weakly); never calbindin-positive; literature support for CS20230722_CLUS_0733 edge |

---

<!-- verdict-block-start: edge_bla_axo_axonic_cell_to_cs20230722_clus_0733 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.72
  rationale: >
    GABA-44-Pthlh-Pvalb maps with F1=0.99 (CLUSTER level) in
    `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` to CS20230722_CLUS_0733;
    atlas label "Pvalb chandelier Gaba_1" provides direct nomenclature
    correspondence. 1 of 2 markers CONSISTENT (marker_Pvalb;
    negative_marker_Sst NOT_ASSESSED). `skos:closeMatch` retained:
    location_soma APPROXIMATE (region_fraction=0.042 in BLA;
    pan-cortical chandelier type).
  unresolved_questions:
    - "Does the ~4% BLA component of CS20230722_CLUS_0733 specifically correspond to axo-axonic cells confirmed by AnkG co-staining?"
    - "Can Sst absence be confirmed in CS20230722_CLUS_0733 from precomputed stats?"
```
<!-- verdict-block-end -->
