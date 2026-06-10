# Basolateral amygdala NPY neurogliaform cell — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala (BLA) NPY neurogliaform cell is a GABAergic interneuron subtype distinguished by neuropeptide Y (NPY) expression and neurogliaform morphology. Vereczki et al. 2021 [1] estimated this population at 14–15% of all GABAergic cells in the lateral and basal amygdala, placing it among the major inhibitory classes alongside parvalbumin basket cells, CCK basket cells, SST dendrite-targeting interneurons, and VIP/calretinin interneuron-selective interneurons. Accurate atlas mapping is important for interpreting BLA circuit models and for linking the classical neuromodulatory roles of NPY to transcriptomic cell-type resolution.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1] |
| NT type | GABAergic | [1] |
| Defining marker | Npy | [1] |
| Negative markers | Pvalb, Sst | — |
| Neuropeptides | Npy | [1], [2] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / NT type / Defining marker (Npy) / Neuropeptide (Npy):** literature census · Vereczki et al. 2021 · [1]
  > we estimated that the following cell types together compose the vast majority of GABAergic cells in the LA and BA: axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%). Our results show that these amygdalar nuclei contain all major GABAergic neuron types as found in other cortical regions.
  > — Vereczki et al. 2021, Basolateral amygdala neuronal subtypes · [1] <!-- quote_key: 232283078_d4238834 -->

- **Neuropeptide (Npy):** neurochemical classification · Rovira-Esteban et al. 2019 · [2]
  > One commonly adopted method segregates IN subpopulations based on neurochemical content, including expression of Ca 2  - binding proteins [e.g., parvalbumin (PV); (McDonald et al., 2001)(McDonald et al., 2001)] and neuropeptides such as somatostatin (SOM), neuropeptide Y (NPY), and cholecystokinin (CCK; Mascagni and Mc-Donald, 2003;(Kepecs et al., 2014)
  > — Rovira-Esteban et al. 2019, Basolateral amygdala and corticobasal cell types · [2] <!-- quote_key: 204835327_bf931431 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: neurogliaform cell [[CL:0000693](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000693)] (BROAD).

The Cell Ontology has no specific term for this population; CL:0000693 (neurogliaform cell) is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review. This classical type is a candidate for a new CL term specifically covering the NPY-expressing neurogliaform class in the BLA.

---

## Results

One candidate atlas cluster was assessed; 0710 Lamp5 Gaba_1 [CS20230722_CLUS_0710] in supertype 0199 Lamp5 Gaba_1 (CS20230722_SUPT_0199) is the primary candidate at UNCERTAIN confidence, constrained by a Sst DISCORDANT marker signal and low BLA region fraction.

### Annotation-transfer overview figure

The Hochgerner 2023 MapMyCells run (`at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) assessed correspondence between the Hochgerner 2023 GABA-46-Lamp5-Kit source group (ArrayExpress:E-MTAB-12096; n=167 naive cells after filtering) and the CCN20230722 taxonomy. The figure below shows F1 scores across taxonomy levels for this source group.

![Filtered AT figure for Basolateral amygdala NPY neurogliaform cell](figures/f1_for_bla_npy_neurogliaform_cell.png)

*F1 across taxonomy levels for the source group GABA-46-Lamp5-Kit relevant to the Basolateral amygdala NPY neurogliaform cell. Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. With a single source group in the figure, Purity differentiates targets; Coverage discriminates how cleanly the source group resolves to each target node. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.*

At subclass level, F1=0.95 (Pur=0.92, Cov=0.99) to 049 Lamp5 Gaba (CS20230722_SUBC_049). At supertype level, F1=0.98 (Pur=0.98, Cov=0.98) to 0199 Lamp5 Gaba_1 (CS20230722_SUPT_0199). At cluster level, F1=0.57 (Pur=1.00, Cov=0.40) to 0710 Lamp5 Gaba_1 [CS20230722_CLUS_0710], indicating the source group distributes across several sibling clusters at rank 0 without clean single-cluster resolution.

The source labels used in this run are Zeisel-style transcriptomically defined types, not classical morpho-electrophysiological types; the correspondence to the BLA NPY neurogliaform classical node requires the additional inference that GABA-46-Lamp5-Kit is the Hochgerner 2023 type most consistent with Lamp5+/Npy+ BLA interneurons.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | 0710 Lamp5 Gaba_1 [CS20230722_CLUS_0710] | 0199 Lamp5 Gaba_1 (CS20230722_SUPT_0199) | 5,178 | ⚪ UNCERTAIN | Npy CONSISTENT · Sst DISCORDANT | Eliminated (negative_Sst) |

1 edge total; relationship type: evidencell:UncertainRelationship.

#### Property comparison — 0710 Lamp5 Gaba_1 [CS20230722_CLUS_0710]

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | not available | MBA:295 BLA present; region_fraction 0.02 | APPROXIMATE |
| NT type | GABAergic | not available | GABA | CONSISTENT |
| Npy expression | defining marker / neuropeptide | not available | Npy precomputed mean 10.5 (tier 2) | CONSISTENT |
| Pvalb (negative) | negative marker | not available | Pvalb val 0.1 (low; consistent with Pvalb-negativity) | CONSISTENT |
| Sst (negative) | negative marker | not available | Sst val 1.0 (above MIN_DETECTABLE) | DISCORDANT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Vereczki et al. 2021 BLA census | Literature | SUPPORT | NPY neurogliaform cells 14–15% of BLA GABAergic cells; separate from Pvalb/Sst populations | [1] |
| CLUS_0710 atlas metadata | Atlas metadata | PARTIAL | Npy tier-2 (10.5), Pvalb absent — but Sst=1.0 DISCORDANT | — |
| MapMyCells AT (Hochgerner 2023) | Annotation transfer | SUPPORT | F1=0.57 at CLUSTER; F1=0.98 at SUPERTYPE (`at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) | — |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### 0710 Lamp5 Gaba_1 [CS20230722_CLUS_0710] · ⚪ UNCERTAIN

**Supporting evidence**

- **Npy expression** (CONSISTENT): CLUS_0710 carries Npy precomputed mean 10.5 (tier 2; applied_score 2.0), placing it at the 98th percentile of the 5-member BLA GABAergic survival cohort (region=MBA:295, nt_type=GABAergic; cohort_size=5). This is the highest Npy-expressing cluster in the cohort and the best available candidate for the Npy-positive defining marker.
- **Pvalb-negativity** (CONSISTENT): Pvalb val 0.1 (unreliable; below MIN_DETECTABLE), consistent with the Pvalb-negative classification of BLA NPY neurogliaform cells.
- **NT type** (CONSISTENT): CLUS_0710 annotation is GABA, matching the GABAergic identity of the classical type [1].
- **Literature** (SUPPORT): Vereczki et al. 2021 [1] establish this population as a distinct BLA interneuron class, estimating 14–15% of GABAergic neurons:
  > we estimated that the following cell types together compose the vast majority of GABAergic cells in the LA and BA: axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%). Our results show that these amygdalar nuclei contain all major GABAergic neuron types as found in other cortical regions.
  > — Vereczki et al. 2021, Basolateral amygdala neuronal subtypes · [1] <!-- quote_key: 232283078_d4238834 -->

- **Annotation transfer** (SUPPORT): MapMyCells run `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` maps Hochgerner 2023 GABA-46-Lamp5-Kit (n=167 naive cells) to supertype 0199 Lamp5 Gaba_1 (CS20230722_SUPT_0199) at F1=0.98 (Pur=0.98, Cov=0.98) and to 0710 Lamp5 Gaba_1 [CS20230722_CLUS_0710] at F1=0.57 (Pur=1.00, Cov=0.40). The supertype-level mapping is highly specific; cluster-level coverage drops to 0.40, with residual cells distributing across sibling clusters within 0199 Lamp5 Gaba_1 (CS20230722_SUPT_0199).

**Marker evidence provenance**

- **Npy (defining marker / neuropeptide):** Evidence is both protein-level (immunohistochemistry) and transcript-level (atlas precomputed expression). Vereczki et al. 2021 [1] established NPY-containing neurogliaform cells as a distinct BLA interneuron class using immunohistochemistry in mouse; Rovira-Esteban et al. 2019 [2] cites NPY as one of the established BLA neuropeptide markers. The atlas-side value (Npy mean 10.5 at CLUS_0710) derives from CCN20230722 precomputed expression. Cell-type specificity in Vereczki et al. 2021 [1] is established by the census design — counts were made against morphologically and neurochemically identified interneuron types in adult mouse.

- **Pvalb (negative marker):** No primary citation is recorded for the Pvalb-negativity assertion on this node; the designation appears to derive from the established segregation logic in BLA (Pvalb-basket cells are a distinct class [1]). Atlas-side Pvalb val=0.1 is below MIN_DETECTABLE and consistent with Pvalb-negativity. A targeted literature check for Pvalb expression specifically in NPY neurogliaform cells would strengthen this negative-marker assertion.

- **Sst (negative marker):** The Sst-negativity expectation has no explicit primary citation on this node. Atlas-side Sst val=1.0 is above MIN_DETECTABLE for CLUS_0710 [CS20230722_CLUS_0710], generating a DISCORDANT flag. This could reflect: (1) genuine Sst co-expression in a subset of Lamp5/Npy cells; (2) cell-level averaging across heterogeneous cells within the cluster; or (3) a Lamp5+/Npy+ cluster that carries low-level Sst expression not captured in classical single-marker literature. **Warning — marker expression concern**: Sst is listed as a negative marker for the classical type but shows val=1.0 (above MIN_DETECTABLE) in CLUS_0710 [CS20230722_CLUS_0710]. This is the primary disqualifying signal for this edge. Whether this reflects genuine co-expression or cluster heterogeneity is unresolved. The Sst-negative designation for NPY neurogliaform cells in BLA should be confirmed with a primary citation and targeted multiplexed expression data.

**Concerns**

- **Sst DISCORDANT** (primary disqualifying signal): CLUS_0710 [CS20230722_CLUS_0710] shows Sst val=1.0 above MIN_DETECTABLE; applied_score -1.0. NPY neurogliaform cells are expected Sst-negative. This marker contradiction is the basis for the UNCERTAIN/eliminated classification. The Sst signal may be a low-level admixture within the cluster rather than true co-expression in Npy+ cells, but this cannot be resolved from atlas precomputed means alone.
- **Low BLA region fraction**: region_fraction 0.02 for CLUS_0710 [CS20230722_CLUS_0710] in MBA:295 (BLA). Lamp5 interneurons are sparse in mouse BLA in the WMBv1 atlas. *(note: the low region fraction is consistent with Lamp5-lineage interneurons being relatively underrepresented in amygdala compared with cortical regions in mouse atlas data.)*
- **Discovery cohort tie**: Stage A discovery score for CLUS_0710 [CS20230722_CLUS_0710] is 3, equal to the next-best candidate in a 5-member BLA GABAergic survival cohort (cohort_size=5, rank_in_cohort=1, next_best_score=3). Npy applied_score=2.0 is the key positive contribution; Sst applied_score=-1.0 offsets this. The tie indicates low selectivity at Stage A.
- **Indirect AT source**: The AT source (GABA-46-Lamp5-Kit from Hochgerner 2023) is a transcriptomically defined label, not a morphologically confirmed NPY neurogliaform population. The link to the classical node is inferred from marker overlap, not from direct cell-type identity matching.
- **Overlap with bla_lamp5_interneuron**: CLUS_0710 [CS20230722_CLUS_0710] is also mapped to `bla_lamp5_interneuron` in this graph, indicating that the Lamp5 Gaba_1 cluster likely represents a broader Lamp5-positive population encompassing multiple classical types. The NPY neurogliaform cell may be a subset of this transcriptomic cluster.

**What would upgrade confidence**

- **Multiplexed smFISH** (Npy + Lamp5 + Sst probes) in mouse BLA: would resolve whether Npy+ neurogliaform cells in the BLA co-express Sst. A clean Sst-negative result in Npy+/Lamp5+ BLA cells would remove the DISCORDANT flag; confirmed Sst co-expression would eliminate this candidate and motivate discovery of an alternative cluster. Expected output: MarkerAnalysisEvidence on `edge_bla_npy_neurogliaform_cell_to_cs20230722_clus_0710`.
- **Direct annotation transfer from morphologically confirmed NPY neurogliaform cells**: patch-seq or single-cell profiling of BLA NPY neurogliaform cells with post-hoc morphological reconstruction, followed by MapMyCells against CCN20230722. Target: F1 ≥ 0.75 at CLUSTER level to upgrade to MODERATE. Expected output: AnnotationTransferEvidence with a classical-type-specific source cluster.
- **CCN20230722 HDF5 rediscovery with Npy+/Sst- compound scoring**: re-running Stage A with explicit Npy+/Sst- scoring on the full atlas may identify a better-fitting cluster outside the current 5-member cohort.
- **Primary citations for negative-marker assertions**: targeted literature search for Sst and Pvalb expression in BLA NPY neurogliaform cells. Expected output: LiteratureEvidence entries anchoring the negative-marker designations.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Basolateral amygdala NPY neurogliaform cell (id: `bla_npy_neurogliaform_cell`) is defined on a CLASSICAL basis — evidence is drawn from primary literature using morphological and neurochemical criteria. Defining marker: Npy [1]. NT type: GABAergic [1]. Soma location: basolateral amygdala [UBERON:0002887] [1]. Negative markers: Pvalb, Sst (citations not recorded on node). Neuropeptide: Npy [1],[2]. Node notes: "No further subtypes noted within BLA neurogliaform class. Directly identified among BLA interneurons in CCK-Cre targeting studies."

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 0 (cluster) using metadata-based scoring (region match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`. Survival cohort filtered to region=MBA:295 (BLA), nt_type=GABAergic; cohort_size=5.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store).

**Annotation transfer.** MapMyCells run: `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`.

| Field | Value |
|---|---|
| Source dataset | ArrayExpress:E-MTAB-12096 (GABA-46-Lamp5-Kit) |
| Source species | NCBITaxon:10090 (mouse) |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.7 |
| n cells | 55,514 total (filtered to 7,777 naive neuronal cells) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`../../../../research/medial_temporal_lobe_amygdala/annotation_transfer/hochgerner2023_amygdala/mapping_result.csv`](../../../../research/medial_temporal_lobe_amygdala/annotation_transfer/hochgerner2023_amygdala/mapping_result.csv) |
| Caveats | Source labels are transcriptomically-defined types, not classical morpho-electrophysiological types. Matching to KB classical nodes requires a mapping step (Hochgerner type → classical node) based on shared molecular markers. Fear-conditioned cells excluded to avoid transcriptional-state confounds. Non-neuronal cells excluded. Gene symbols used (not Ensembl IDs); matched against WMBv1 marker genes. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `9d82411` at 2026-06-10T12:49:03+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_npy_neurogliaform_cell_to_cs20230722_clus_0710 | LITERATURE; ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT; PARTIAL; SUPPORT | [1]; —; — |

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala NPY neurogliaform cell → 0710 Lamp5 Gaba_1 [CS20230722_CLUS_0710] at UNCERTAIN confidence. Key support: annotation transfer (F1=0.98 at supertype in `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`; F1=0.57 at cluster) and Npy expression CONSISTENT (precomputed mean 10.5). Key caveats: Sst DISCORDANT (val=1.0 above MIN_DETECTABLE); low region fraction in BLA (region_fraction=0.02).

The Cell Ontology has no specific term for this population; neurogliaform cell [[CL:0000693](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000693)] is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

### Proposed experiments and follow-ups

The annotation transfer experiment has been partially addressed: MapMyCells was run with Hochgerner 2023 GABA-46-Lamp5-Kit cells (n=167 naive, ArrayExpress:E-MTAB-12096), establishing a strong supertype-level mapping to 0199 Lamp5 Gaba_1 (CS20230722_SUPT_0199) (F1=0.98) but incomplete cluster-level resolution (F1=0.57 at CLUS_0710 [CS20230722_CLUS_0710], with multiple sibling clusters receiving residual cells). Remaining experiments:

1. **Multiplexed smFISH — Npy/Lamp5/Sst co-expression in mouse BLA**
   - What: fluorescent ISH with Npy, Lamp5, and Sst probes in coronal BLA sections
   - Target: quantify Sst co-expression rate in Npy+/Lamp5+ cells; threshold Sst < MIN_DETECTABLE in ≥ 90% of Npy+ cells to call Sst-negative
   - Expected output: MarkerAnalysisEvidence on `edge_bla_npy_neurogliaform_cell_to_cs20230722_clus_0710`; if Sst-negative confirmed: remove DISCORDANT flag; if co-expression confirmed: search for a Sst-negative Lamp5+/Npy+ cluster
   - Resolves: DISCORDANT `negative_marker_Sst`; open questions 1 and 2

2. **Direct annotation transfer from morphologically confirmed NPY neurogliaform cell dataset**
   - What: MapMyCells on a patch-seq or single-cell dataset of morphologically reconstructed BLA NPY neurogliaform cells against CCN20230722
   - Target: F1 ≥ 0.75 at CLUSTER level
   - Expected output: AnnotationTransferEvidence with classical-type-specific source cluster; would upgrade edge to MODERATE or higher with predicate revision
   - Resolves: indirect AT anchor; open question 1

3. **CCN20230722 HDF5 rediscovery with Npy+/Sst- compound scoring**
   - What: acquire CCN20230722 HDF5 and re-run Stage A discovery with explicit Npy+/Sst- scoring
   - Target: identify any cluster with Npy expression above tier-1 and Sst val below MIN_DETECTABLE
   - Expected output: revised candidate set; potentially new edge at MODERATE
   - Resolves: open question 4

4. **Targeted literature search for negative-marker provenance**
   - What: cite-traverse for "NPY neurogliaform Sst BLA mouse" and "NPY neurogliaform Pvalb BLA mouse"
   - Expected output: LiteratureEvidence entries anchoring Sst-negative and Pvalb-negative assertions on the classical node
   - Resolves: missing primary citations for negative-marker designations

### Open questions

1. Do BLA NPY neurogliaform cells overlap with the Lamp5 Gaba family in WMBv1?
2. Is the Sst signal in CLUS_0710 [CS20230722_CLUS_0710] genuine co-expression or averaging artifact?
3. Run multiplexed smFISH (Npy+Lamp5+Sst) in mouse BLA to resolve whether Sst co-expression occurs in NPY neurogliaform cells.
4. Acquire CCN20230722 HDF5 and re-run Stage A discovery with explicit Npy+/Sst- scoring to test for a better-fitting BLA cluster.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Vereczki et al. 2021 · Total Number and Ratio of GABAergic Neuron Types in the Mouse Lateral and Basal Amygdala | [33837051](https://pubmed.ncbi.nlm.nih.gov/33837051/) | soma location; defining marker; NT type; neuropeptide |
| [2] | Rovira-Esteban et al. 2019 · Excitation of Diverse Classes of Cholecystokinin Interneurons in the Basal Amygdala Facilitates Fear Extinction | [31636080](https://pubmed.ncbi.nlm.nih.gov/31636080/) | Npy neuropeptide |

---

<!-- verdict-block-start: edge_bla_npy_neurogliaform_cell_to_cs20230722_clus_0710 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    MapMyCells (`at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) maps
    GABA-46-Lamp5-Kit to CS20230722_SUPT_0199 at F1=0.98 and to
    CS20230722_CLUS_0710 at F1=0.57; 2 of 3 markers CONSISTENT
    (neuropeptide_Npy CONSISTENT; negative_marker_Pvalb CONSISTENT);
    negative_marker_Sst DISCORDANT (Sst val=1.0 above MIN_DETECTABLE) is
    the primary disqualifying signal. Region fraction 0.02 in MBA:295 is
    low. Predicate evidencell:UncertainRelationship retained pending Sst
    co-expression resolution.
  reconciliation_note: >
    The inherited predicate evidencell:UncertainRelationship may be
    inconsistent with the AT evidence strength: F1=0.98 at supertype
    CS20230722_SUPT_0199 and F1=0.57 at cluster CS20230722_CLUS_0710 in
    `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` are stronger than
    UNCERTAIN typically implies. However, the Sst DISCORDANT negative-marker
    flag (val=1.0) and the indirect nature of the AT source (transcriptomically
    defined GABA-46-Lamp5-Kit, not morphologically confirmed NPY neurogliaform
    cells) together justify retaining UNCERTAIN until Sst co-expression is
    resolved. If multiplexed smFISH confirms Sst-negativity in Npy+/Lamp5+ BLA
    cells, the predicate should be upgraded to skos:closeMatch or skos:exactMatch
    at MODERATE confidence — curator review required.
  unresolved_questions:
    - "Trawl literature for Sst expression in BLA NPY neurogliaform cells — the CS20230722_CLUS_0710 Sst val=1.0 may reflect cluster heterogeneity not captured in classical single-marker studies."
    - "Confirm Pvalb-negativity assertion for BLA NPY neurogliaform cells with a primary citation."
```
<!-- verdict-block-end -->
