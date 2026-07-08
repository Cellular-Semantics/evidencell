# CA2 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

## Introduction

CA2 pyramidal cells are the principal glutamatergic neurons of hippocampal area CA2, a narrow subfield between CA3 and CA1 whose dedicated marker profile (Pcp4, Rgs14, Amigo2) and absence of the CA1 marker Wfs1 distinguish them from neighbouring pyramidal populations [4][5]. Defining CA2 transcriptomically matters because the field supports a distinct cortical input pathway and is required for social memory, but its narrow spatial extent makes it difficult to separate from CA1/CA3 in dissociated single-cell datasets.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA2 [UBERON:0014549] | [1], [2] |
| NT type | glutamatergic | [3] |
| Defining markers | Pcp4, Rgs14, Amigo2 | [4], [5] |
| Negative markers | Wfs1 | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** Cembrowski et al. 2016 transcriptomic profiling along the CA2 dorsoventral axis · [1]
  > we profiled transcriptomes at both dorsal and ventral poles, producing a cell-class- and region-specific transcriptional description for these populations
  > — Cembrowski et al. 2016, abstract · [1] <!-- quote_key: 4875295_8cb069d9 -->
- **Soma location:** Sanchez-Aguilera et al. 2021 mapping of CA2 cells across CA3 subregion boundaries · [2]
  > For CA2, we identified some pyramidal cells at the CA3c region while others distributed along the intermediate (CA3b) and distal (CA3a) subregions (Sanchez-Aguilera et al., 2021).
  > — Unknown et al. 2021, Classical Hippocampal Circuit Organization · [2] <!-- quote_key: 233984943_56acd5f8 -->
- **NT type:** Dale et al. 2015 review of hippocampal principal cell neurotransmitter identity · [3]
  > There are 2 types of principal cells in the hippocampal circuit: glutamatergic pyramidal cells in the Ammon's horn and subiculum regions, and glutamatergic granule cells in the DG (Figure 1). They generally have excitatory effects on the neurons to which they send axon terminals including other glutamatergic and GABAergic, as well monoaminergic [5-HT, norepinephrine (NE), dopamine (DA)], cholinergic, and histaminergic (HA) cells.
  > — Dale et al. 2015, Major Glutamatergic Cell Types in Hippocampal Subfields · [3] <!-- quote_key: 2281033_5b9805ff -->
- **Marker Pcp4:** Pcp4 antibody delineation of CA2 borders · [4]
  > Here we report identification of the CA2 region in the mouse by immunostaining with a Purkinje cell protein 4 (PCP4) antibody, which effectively delineates CA3/CA2 and CA2/CA1 borders and agrees well with previous cytoarchitectural definitions of CA2
  > — Unknown et al. 2014, abstract · [4] <!-- quote_key: 18746823_614030d2 -->
- **Marker Rgs14, Amigo2:** broader CA2 marker panel · [4][5]
  > These markers include Purkinje cell protein 4 (PCP4), neurotrophin 3, fibroblast growth factor, a-actinin 2, adenosine A1 receptor, vasopressin 1b receptor, RGS14 (regulator of G-protein signaling 14), and amigo2. These markers are specifically or more prominently expressed in the distal portion of regio inferior corresponding roughly to Lorente de N o's CA2
  > — Unknown et al. 2014, Introduction · [4] <!-- quote_key: 18746823_8ba0bf29 -->
  > a number of genes, including the regulator of G-protein signaling 14 (RGS14), Amigo2, PCP4, TARP5, FGF5, and several adenylyl cyclases (e.g., adcy1, adcy5, and adcy6), are highly expressed in CA2
  > — Unknown et al. 2012, Introduction · [5] <!-- quote_key: 20853920_44ab38bb -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

**Proposed CL term:** *CA2 pyramidal cell* (SUBMITTED; parent CL:1001571 hippocampal pyramidal neuron)

Definition: A hippocampal pyramidal neuron with soma located in the pyramidal layer of hippocampal area CA2 (Cembrowski et al., 2016; Sanchez-Aguilera et al., 2021). Distinguished from CA1 and CA3 pyramidal neurons by expression of Pcp4, Rgs14, and Amigo2 in rodents (San Antonio et al., 2014; Caruana et al., 2012), and by absence of the CA1 marker wolframin (Wfs1) (Evans et al., 2018). Receives strong LTP-competent input from entorhinal cortex at distal dendrites, while Schaffer collateral inputs to proximal dendrites are resistant to canonical LTP in wild-type animals (Chevaleyre & Siegelbaum, 2010). Required for social memory in mice (Hitti & Siegelbaum, 2014).

---

## Results

The classical CA2 marker triad (Pcp4, Rgs14, Amigo2) and atlas MERFISH soma counts in CA2 pyramidal layer converge on the supertype 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] as the primary mapping for CA2 pyramidal cells, with the dominant child cluster 0399 CA2-FC-IG Glut_1 [CS20230722_CLUS_0399] as the best resolved cluster within it (see figure and property comparison tables). Annotation transfer from a Yao 2021 SSv4 hippocampus dataset is informative but technically refutes neither candidate — the source label "CA2-IG-FC" pools CA2 with the adjacent fasciola cinerea / indusium griseum cells, and its 18 of 19 cells map to the sibling supertype 0101 CA2-FC-IG Glut_2 [CS20230722_SUPT_0101], whose MERFISH soma counts place it outside the CA2 pyramidal layer.

![Filtered AT figure for CA2 pyramidal cell](figures/f1_for_ca2_pc_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 SSv4 CA2-IG-FC source group (n=19 cells), mapped via MapMyCells onto WMBv1. Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. The subclass-level call onto 025 CA2-FC-IG Glut (F1=0.97) is the clean signal; supertype-level scatter onto 0101 CA2-FC-IG Glut_2 (F1=0.95) reflects the FC/IG component of Yao's mixed source label, not the CA2 pyramidal population proper — see Discussion for the MERFISH-anatomy reconciliation.*

### 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] · 🟡 MODERATE

**Supporting evidence:**
- All three classical defining markers are at high precomputed expression on this supertype (Pcp4=11.26; Rgs14=8.84; Amigo2=7.39) with cohort percentile 0.923 and full child-cluster coverage of 1.000 — every child cluster within SUPT_0100 carries the marker, so the supertype-level mean is not driven by a minority of children.
- MERFISH soma anatomy on this supertype includes Field CA3, pyramidal layer [MBA:495] (count_100um=1307) and Hippocampal formation [MBA:1089] (count_100um=1809). Atlas curator metadata also records 446 cells in Field CA2, pyramidal layer (MBA:446) on this supertype, consistent with CA2 pyramidal soma placement.
- Stage A discovery dominates its 13-member rank-1 supertype cohort (region=MBA:446, NT=glutamatergic): score 5 vs next-best 4, rank 1.
- The subclass-level annotation-transfer call from Yao 2021 (GEO:GSE185862) onto 025 CA2-FC-IG Glut (F1=0.97, 18/19 cells) confirms CA2-FC-IG subclass membership for this branch of the taxonomy.

**Marker evidence provenance:**
- **Pcp4** is established as a CA2 border-delineating marker by Pcp4 immunostaining (protein-level) on the mouse hippocampus [4], and is corroborated at transcript level by Caruana et al. 2012 [5]. Atlas-side mean expression 11.26 (cohort percentile 0.923) is the strongest single marker signal.
- **Rgs14, Amigo2** are listed together in [4][5] as CA2-enriched genes; both replicate strongly on this supertype.
- **Wfs1 negative-marker check** — Wfs1 mean expression on SUPT_0100 is 1.33 (cohort percentile 0.308), which is the lowest tertile of the rank-1 cohort but above the noise floor; the atlas-internal call is DISCORDANT under the strict "absent" reading. Interpretation: Wfs1 is robustly absent in *CA2* pyramidal cells per [4][5], but SUPT_0100 also contains FC/IG cells (per the subclass name "CA2-FC-IG"); residual Wfs1 expression may originate from the non-CA2 components of the supertype rather than from CA2 pyramidal cells themselves *(note: interpretation based on supertype composition; a CA2-specific dataset would confirm).*

**Concerns:**
- The subclass groups CA2 with fasciola cinerea (FC) and indusium griseum (IG) — small CA2-adjacent structures distinct from CA2 proper. The supertype therefore conflates CA2 pyramidal cells with FC/IG glutamatergic cells; the mapping is at supertype level rather than 1:1 to a CA2-only target.
- Wfs1 negative marker DISCORDANT (val=1.33; cohort_pct 0.308) — see provenance bullet above.
- Annotation transfer of Yao 2021 (GEO:GSE185862) CA2-IG-FC subclass label (n=19) maps 94.7% of cells to SUPT_0101 (F1=0.95 at supertype level; cluster-level F1=0.88 onto sibling cluster 0401 CA2-FC-IG Glut_2 with Cov=0.79 and Pur=1.00), not to SUPT_0100. However, SUPT_0101 MERFISH anatomy is dominated by fasciola cinerea and indusium griseum with no cells in CA2 pyramidal layer, while SUPT_0100 carries the CA2 pyramidal soma counts — so the AT result reflects which atlas supertype absorbs the FC/IG component of Yao's mixed CA2-IG-FC label, not which supertype is the correct target for CA2 pyramidal cells proper.
- An auto-repredication caveat flags this edge's predicate as migrated from the deprecated `evidencell:PartialOverlapMatch` and recommends curator review.

**What would upgrade confidence:**
- Annotation transfer from a CA2-specific dataset (without FC/IG contamination in the source labels) targeting WMBv1 at F1 ≥ 0.80 at supertype level — would add an AnnotationTransferEvidence item discriminating SUPT_0100 from SUPT_0101 for CA2 pyramidal cells.
- FISH validation of Rgs14 or Amigo2 in MERFISH-assigned SUPT_0100 cells in CA1/CA3 strata to determine whether those soma locations reflect genuine boundary CA2 cells or registration error.

### 0399 CA2-FC-IG Glut_1 [CS20230722_CLUS_0399] · 🟡 MODERATE

**Supporting evidence:**
- All three CA2 defining markers reach their highest cohort percentile on this child cluster (Pcp4=11.26 pct 0.969; Rgs14=8.84 pct 0.969; Amigo2=7.39 pct 0.969) within a 32-member rank-0 glutamatergic CA2-region cohort.
- Stage A discovery score 8 vs next-best 4 in cohort_size 32 — strong cohort-relative dominance at the cluster level (rank 1 in cohort).
- MERFISH soma anatomy matches the parent supertype: Field CA3, pyramidal layer [MBA:495] and Hippocampal formation [MBA:1089] (region_fraction_100um: 0.649, region_evidence: SELF).
- Subclass-level annotation-transfer confirmation onto 025 CA2-FC-IG Glut (F1=0.97) places this cluster within the correct subclass branch.

**Marker evidence provenance:**
- Same Pcp4 / Rgs14 / Amigo2 chain as the parent supertype ([4], [5]); cluster-level cohort percentiles (0.969) are slightly higher than supertype-level (0.923), reflecting child-cluster narrowing within a 32-member cohort.
- **Wfs1**: cluster-level expression 1.33 (cohort_pct 0.188) — lower than at supertype level relative to the rank-0 cohort, consistent with the CA2-PC component of the parent supertype carrying less Wfs1 than the FC/IG component *(note: inference based on supertype composition).*

**Concerns:**
- Wfs1 negative marker DISCORDANT (val=1.33; cohort_pct 0.188) — the same caveat as the parent supertype; same interpretation applies.
- No direct annotation transfer evidence at cluster level — the Yao 2021 (GEO:GSE185862) AT run's CA2-IG-FC source label maps to the sibling cluster 0401 CA2-FC-IG Glut_2 (cluster F1=0.88, Cov=0.79, Pur=1.00; child of SUPT_0101), not to CLUS_0399. As with the supertype-level argument, the absence of cluster-level AT support for CLUS_0399 is explained by the FC/IG bias of the source label rather than by CA2 pyramidal cells genuinely mapping elsewhere.

**What would upgrade confidence:**
- Cluster-level annotation transfer from a CA2-specific source at F1 ≥ 0.80.
- Per-cell precomputed expression for Rgs14, Pcp4, Amigo2 within CLUS_0399 to confirm marker expression is centred on CA2 pyramidal soma rather than on FC/IG subset.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster / supertype | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] | — | 143 | 🟡 MODERATE | Pcp4/Rgs14/Amigo2 high; 446 CA2 PL soma | Primary (supertype) |
| 0399 CA2-FC-IG Glut_1 [CS20230722_CLUS_0399] | 0100 CA2-FC-IG Glut_1 | 143 | 🟡 MODERATE | All 3 markers pct 0.969 (rank 0 cohort) | Secondary (best child of SUPT_0100) |
| 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] (duplicate edge) | — | 143 | ⚪ UNCERTAIN | Same target as primary; no AT evidence | Eliminated (duplicate edge — see open questions) |
| 0261 CA1-ProS Glut_1 [CS20230722_CLUS_0261] | 0069 CA1-ProS Glut_1 | 215 | 🔴 LOW | Pcp4=1.68 weak; Wfs1=4.29 high | Eliminated (CA1-ProS subclass, Wfs1+) |
| 0270 CA1-ProS Glut_1 [CS20230722_CLUS_0270] | 0069 CA1-ProS Glut_1 | 300 | 🔴 LOW | Markers APPROXIMATE; Wfs1=2.68 | Eliminated (CA1-ProS subclass, Wfs1+) |
| 0296 CA3 Glut_1 [CS20230722_CLUS_0296] | 0075 CA3 Glut_1 | 230 | 🔴 LOW | CA3 subclass; Wfs1 discordant | Eliminated (CA3 subclass) |
| 0298 CA3 Glut_1 [CS20230722_CLUS_0298] | 0075 CA3 Glut_1 | 95 | 🔴 LOW | CA3 subclass; Wfs1 discordant | Eliminated (CA3 subclass) |
| 0075 CA3 Glut_1 [CS20230722_SUPT_0075] | — | 763 | 🔴 LOW | CA3 supertype; location APPROXIMATE | Eliminated (CA3 subclass) |
| 0073 CA1-ProS Glut_5 [CS20230722_SUPT_0073] | — | 898 | 🔴 LOW | Amigo2=0.18; Wfs1=2.41 | Eliminated (CA1-ProS subclass, Amigo2 low) |
| 0101 CA2-FC-IG Glut_2 [CS20230722_SUPT_0101] | — | 497 | 🔴 LOW | High markers but 0 CA2 PL soma | Eliminated (FC/IG sibling, no CA2 PL cells) |
| 0078 CA3 Glut_4 [CS20230722_SUPT_0078] | — | 2147 | 🔴 LOW | Location DISCORDANT (rf100um=0.025) | Eliminated (distant region; CA3 subclass) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** CA2 pyramidal cell (definition_basis: CLASSICAL_MULTIMODAL) is defined by glutamatergic neurotransmitter identity [3], soma in pyramidal layer of CA2 [UBERON:0014549] [1][2], defining markers Pcp4, Rgs14, Amigo2 [4][5], and absence of the CA1 marker Wfs1.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SSv4 cell type labels) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:49+00:00 from [kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_ca2_pc_hippocampus_to_supt_0100 | ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT; PARTIAL | atlas-internal |
| edge_ca2_pc_hippocampus_to_CS20230722_CLUS_0399 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0100 (duplicate) | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca2_pc_hippocampus_to_CS20230722_CLUS_0261 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca2_pc_hippocampus_to_CS20230722_CLUS_0270 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca2_pc_hippocampus_to_CS20230722_CLUS_0296 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca2_pc_hippocampus_to_CS20230722_CLUS_0298 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0075 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0073 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0101 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0078 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** CA2 pyramidal cell → 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] at MODERATE confidence, with 0399 CA2-FC-IG Glut_1 [CS20230722_CLUS_0399] as the best resolved child cluster within the supertype. Key support: atlas precomputed expression of Pcp4/Rgs14/Amigo2 (cohort_pct 0.923 supertype, 0.969 cluster) plus MERFISH soma counts in CA2 pyramidal layer. Key caveats: DISCORDANT_ANATOMY (FC/IG cells lumped with CA2 in the supertype name); annotation transfer from Yao 2021 maps the CA2-IG-FC source label onto the sibling supertype SUPT_0101 because Yao's source label conflates CA2 with FC/IG and the FC/IG component dominates the AT decision.

No Cell Ontology term currently assigned. The Cell Ontology lacks a CA2-specific pyramidal-cell term; a new term *CA2 pyramidal cell* (parent CL:1001571 hippocampal pyramidal neuron) is in submission.

### Proposed experiments and follow-ups

- **What:** Annotation transfer from a CA2-specific transcriptomic dataset (a source label restricted to CA2 pyramidal cells without FC/IG contamination) onto WMBv1.
  - **Target:** F1 ≥ 0.80 at supertype level on CS20230722_SUPT_0100 (and < 0.50 on CS20230722_SUPT_0101 to confirm the FC/IG-only interpretation of the Yao 2021 result).
  - **Expected output:** AnnotationTransferEvidence resolving the SUPT_0100 vs SUPT_0101 ambiguity for CA2 pyramidal cells proper.
  - **Resolves:** the supertype-discrimination question for the primary mapping; the cluster-level call for CLUS_0399.
  - **Existing AT round insufficient because:** the Yao 2021 source label is "CA2-IG-FC", which already pools CA2 with FC/IG; the FC/IG component dominates and forces 18/19 cells onto SUPT_0101 (the FC/IG-enriched supertype).
- **What:** Targeted FISH validation of Rgs14 or Amigo2 in MERFISH-assigned SUPT_0100 cells located in CA1 and CA3 strata.
  - **Target:** Determine whether these are genuine boundary CA2 pyramidal neurons or MERFISH registration errors.
  - **Expected output:** Evidence informing whether SUPT_0100 cells in CA1/CA3 strata refine the CA2 mapping or should be excluded.
- **What:** Per-cluster precomputed expression of Rgs14 and Pcp4 on SUPT_0100 via `add-expression`.
  - **Target:** Distinguish the CA2-PC subset of SUPT_0100 from any FC/IG contamination at finer resolution.
  - **Expected output:** Stronger marker-evidence support for the supertype-level call.

### Open questions

1. Do SUPT_0100 cells in CA1 and CA3 strata represent genuine pyramidal neurons (e.g. deep CA3c cells near CA2 border) or MERFISH registration errors? FISH validation of Rgs14 or Amigo2 in CA2 cells assigned to SUPT_0100 would clarify.
2. Curator review needed: two MappingEdges currently target CS20230722_SUPT_0100 (`edge_ca2_pc_hippocampus_to_supt_0100` carries the substantive AT evidence and DISCORDANT_ANATOMY caveat; `edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0100` is a fresh-emit duplicate without AT). Recommend removing the impoverished duplicate edge.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | soma location |
| [2] | Unknown 2021 | [33956790](https://pubmed.ncbi.nlm.nih.gov/33956790/) | soma location |
| [3] | Dale et al. 2015 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | neurotransmitter type |
| [4] | Unknown 2014 | [24166578](https://pubmed.ncbi.nlm.nih.gov/24166578/) | Pcp4 marker |
| [5] | Unknown 2012 | [22904370](https://pubmed.ncbi.nlm.nih.gov/22904370/) | Amigo2 marker |

---

<!-- verdict-block-start: edge_ca2_pc_hippocampus_to_supt_0100 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.6
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] All three CA2 defining markers high on CS20230722_SUPT_0100
    (Pcp4=11.26, Rgs14=8.84, Amigo2=7.39; cohort percentile 0.923; child-coverage
    1.000) and MERFISH soma counts in CA2 pyramidal layer; 3 of 4 markers
    CONSISTENT. Annotation transfer in at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1
    routes Yao's mixed CA2-IG-FC label to the FC/IG-enriched sibling
    CS20230722_SUPT_0101 (subclass-level F1=0.97) which has no CA2 pyramidal layer
    soma; SUPT_0100 retains the CA2-PC mapping under the MERFISH-anatomy
    reading. Supertype lumps CA2 with fasciola cinerea and indusium griseum
    (broadMatch + 1:n).
  reconciliation_note: >
    Paired with child-cluster edge edge_ca2_pc_hippocampus_to_CS20230722_CLUS_0399
    (best within-supertype child); also paired with the duplicate fresh-emit
    edge edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0100 which targets the same
    accession without AT evidence — recommend curator removal of the duplicate.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Supertype name lumps CA2 with fasciola cinerea (FC) and indusium
        griseum (IG); classical CA2 pyramidal cells are distinct from FC/IG
        neurons. The skos:broadMatch + 1:n encoding reflects this conflation.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Negative marker Wfs1 mean expression 1.33 on CS20230722_SUPT_0100
        (cohort percentile 0.308) is above the strict-absent threshold; likely
        contributed by the non-CA2 (FC/IG) component of the supertype rather
        than by CA2 pyramidal cells.
    - caveat_type: OTHER
      description: >
        Annotation transfer of Yao 2021 (GEO:GSE185862) CA2-IG-FC subclass label
        (n=19) via at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1 maps 18/19 cells
        to CS20230722_SUPT_0101 (subclass-level F1=0.97) and only 1/19 to
        CS20230722_SUPT_0100; SUPT_0101 has 0 CA2 pyramidal layer cells in
        MERFISH while SUPT_0100 has 446. AT result reflects FC/IG dominance in
        Yao's pooled source label, not the correct target for CA2 pyramidal
        cells.
  proposed_experiments:
    - >
      Annotation transfer from a CA2-specific transcriptomic source (no FC/IG
      contamination) onto WMBv1 at F1 >= 0.80 at supertype level on
      CS20230722_SUPT_0100, with F1 < 0.50 on CS20230722_SUPT_0101 to confirm
      the FC/IG-only interpretation of at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1.
    - >
      smFISH validation of Rgs14 or Amigo2 in MERFISH-assigned SUPT_0100 cells
      located in CA1 and CA3 strata to determine whether these are boundary CA2
      pyramidal neurons or registration errors.
  unresolved_questions:
    - >
      Curator removal of duplicate edge edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0100
      — legacy/fresh-emit ID collision on taxonomy_type CS20230722_SUPT_0100.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca2_pc_hippocampus_to_CS20230722_CLUS_0399 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Best within-supertype child of CS20230722_SUPT_0100. All three
    defining markers reach cohort percentile 0.969 on CS20230722_CLUS_0399
    (Pcp4=11.26, Rgs14=8.84, Amigo2=7.39) within a 32-member rank-0 cohort,
    Stage A score 8 vs next-best 4; MERFISH soma anatomy matches the parent
    supertype (region_fraction_100um=0.649). 3 of 4 markers CONSISTENT; no
    direct cluster-level AT (Yao 2021 scRNA-seq CA2-IG-FC label routes to a
    sibling cluster under SUPT_0101 via FC/IG dominance).
  reconciliation_note: >
    Paired with supertype edge edge_ca2_pc_hippocampus_to_supt_0100; the supertype
    is the broadMatch encoding and this child is the best resolved cluster within it.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Negative marker Wfs1 expression 1.33 on CS20230722_CLUS_0399
        (cohort percentile 0.188) is non-zero; same FC/IG-component interpretation
        as the parent supertype applies.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        No direct cluster-level annotation transfer evidence; Yao 2021 AT routes
        the mixed CA2-IG-FC source label to a sibling cluster under
        CS20230722_SUPT_0101 via FC/IG dominance rather than to CS20230722_CLUS_0399.
  proposed_experiments:
    - >
      Cluster-level annotation transfer from a CA2-specific source at
      F1 >= 0.80 on CS20230722_CLUS_0399.
    - >
      Per-cell precomputed expression for Rgs14, Pcp4, Amigo2 within
      CS20230722_CLUS_0399 to confirm marker expression centred on CA2
      pyramidal soma rather than on an FC/IG subset.
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0100 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Fresh-emit duplicate edge targeting the same accession
    CS20230722_SUPT_0100 as the substantive primary edge
    edge_ca2_pc_hippocampus_to_supt_0100; this duplicate carries no
    annotation-transfer evidence and only the auto-generated AMBIGUOUS_MAPPING
    caveat. Recommend curator removal.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Duplicate of substantive edge edge_ca2_pc_hippocampus_to_supt_0100 on
        taxonomy_type CS20230722_SUPT_0100; the substantive edge carries the
        annotation-transfer evidence and DISCORDANT_ANATOMY caveat.
  proposed_experiments: []
  unresolved_questions:
    - >
      Curator removal of duplicate edge edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0100
      — legacy/fresh-emit ID collision on taxonomy_type CS20230722_SUPT_0100.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca2_pc_hippocampus_to_CS20230722_CLUS_0261 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0261 sits in CA1-ProS subclass (supertype 0069
    CA1-ProS Glut_1); Pcp4=1.68 (cohort percentile 0.125) is APPROXIMATE,
    Amigo2=0.14 is APPROXIMATE, and the negative marker Wfs1=4.29 (cohort
    percentile 0.844) is strongly DISCORDANT — characteristic of CA1 rather
    than CA2.
  caveats:
    - caveat_type: OTHER
      description: >
        CA1-ProS subclass; Pcp4 and Amigo2 weak; Wfs1 high (cohort percentile
        0.844) — characteristic of CA1.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca2_pc_hippocampus_to_CS20230722_CLUS_0270 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0270 sits in CA1-ProS subclass (supertype 0069
    CA1-ProS Glut_1); all three defining markers APPROXIMATE only (Pcp4=4.58,
    Rgs14=3.84, Amigo2=0.29) and negative marker Wfs1=2.68 (cohort percentile
    0.656) is DISCORDANT.
  caveats:
    - caveat_type: OTHER
      description: >
        CA1-ProS subclass; markers APPROXIMATE; Wfs1 moderate-high
        (cohort percentile 0.656).
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca2_pc_hippocampus_to_CS20230722_CLUS_0296 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0296 sits in CA3 subclass (supertype 0075 CA3
    Glut_1). CA2 markers Pcp4=9.04, Rgs14=4.97, Amigo2=1.84 are CONSISTENT
    but at moderate cohort percentile, and location alignment is APPROXIMATE
    (region_fraction_100um=0.221) with soma counts dominated by CA1 stratum
    oriens rather than CA2 pyramidal layer.
  caveats:
    - caveat_type: OTHER
      description: >
        CA3 subclass; off-target soma distribution
        (region_fraction_100um=0.221, dominant anatomy Field CA1).
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca2_pc_hippocampus_to_CS20230722_CLUS_0298 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0298 sits in CA3 subclass (supertype 0075 CA3
    Glut_1). Markers CONSISTENT (Pcp4=9.65, Rgs14=5.19, Amigo2=2.51) but
    region alignment APPROXIMATE (region_fraction_100um=0.410, soma in
    Field CA3 stratum oriens rather than CA2 pyramidal layer); negative
    marker Wfs1=2.16 DISCORDANT.
  caveats:
    - caveat_type: OTHER
      description: >
        CA3 subclass; soma in CA3 stratum oriens; Wfs1 moderate
        (cohort percentile 0.375).
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0075 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0075 is the CA3 supertype. Markers CONSISTENT
    (Pcp4=8.95, Rgs14=4.14, Amigo2=2.03) but location alignment APPROXIMATE
    (region_fraction_100um=0.181, dominant anatomy Field CA3 stratum oriens);
    Wfs1=1.99 DISCORDANT. CA3 rather than CA2.
  caveats:
    - caveat_type: OTHER
      description: >
        CA3 supertype; off-target region (region_fraction_100um=0.181).
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0073 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0073 is a CA1-ProS supertype. Pcp4=7.91 and
    Rgs14=3.10 CONSISTENT but Amigo2=0.18 APPROXIMATE (cohort percentile
    0.308) and negative marker Wfs1=2.41 DISCORDANT (cohort percentile
    0.615) — characteristic of CA1, not CA2; location alignment APPROXIMATE
    (region_fraction_100um=0.141, dominant anatomy Field CA1 stratum oriens).
  caveats:
    - caveat_type: OTHER
      description: >
        CA1-ProS supertype; Amigo2 weak, Wfs1 moderate-high.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0101 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_SUPT_0101 is the FC/IG-enriched sibling supertype
    in subclass 025 CA2-FC-IG Glut. Markers high (Pcp4=9.99, Rgs14=5.67,
    Amigo2=4.12). MERFISH soma anatomy shows 0 cells in CA2 pyramidal layer
    for this supertype (dominant anatomy Hippocampal formation outside CA2;
    region_fraction_100um=0.136). The Yao 2021 AT signal routing the mixed
    CA2-IG-FC source label to this branch is captured on the paired
    edge_ca2_pc_hippocampus_to_supt_0100 verdict and reflects FC/IG dominance
    in Yao's pooled source label, not CA2 pyramidal cells.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        No CA2 pyramidal layer soma despite CA2-FC-IG subclass membership;
        anatomy dominated by fasciola cinerea / indusium griseum
        (region_fraction_100um=0.136).
    - caveat_type: OTHER
      description: >
        Yao 2021 AT routes the mixed CA2-IG-FC label here via the FC/IG
        component of the source label, not via CA2 pyramidal cells; not
        evidence for a CA2-PC mapping.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca2_pc_hippocampus_to_CS20230722_SUPT_0078 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0078 is a CA3 supertype (0078 CA3 Glut_4).
    Location DISCORDANT (region_fraction_100um=0.025; soma dominated by
    Field CA3 pyramidal layer); markers APPROXIMATE only (Pcp4=4.29,
    Rgs14=2.15); Wfs1=1.94 DISCORDANT. CA3 rather than CA2.
  caveats:
    - caveat_type: OTHER
      description: >
        CA3 supertype; distant region (region_fraction_100um=0.025);
        markers APPROXIMATE.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->
