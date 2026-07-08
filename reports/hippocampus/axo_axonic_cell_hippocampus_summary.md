# Axo-axonic (chandelier) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Axo-axonic (chandelier) cells are one of three canonical parvalbumin-expressing
(Pvalb+) GABAergic interneuron subtypes of the hippocampus — alongside basket
and bistratified cells — distinguished by cartridge-like axonal boutons that
contact exclusively the axon initial segment (AIS) of pyramidal neurons. Their
defining transcriptomic signature is Pvalb expression, with somata classically
localised to the CA1 pyramidal layer (UBERON:0014548) of the hippocampal
formation. Resolving the chandelier subtype within the broader Pvalb cohort is
a long-standing challenge because the three morphological PV+ subtypes share
substantial transcriptomic overlap (PMID:33398060).

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | [1] |
| NT | GABAergic | [2] |
| Markers | Pvalb (defining) | [1], [3] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Pvalb marker:** Rivera et al. 2014 establishes Pvalb+ identity and CA1
  pyramidal-layer localisation for hippocampal axo-axonic cells · [1]
  > Parvalbumin + cells were specifically localized in the granular and polymorphic cell layers of the dentate gyrus and the strata oriens and pyramidale in CA1/3 fields of the rat hippocampus (Kosaka et al., 1987). They have been considered a subpopulation of GABAergic interneurons, including basket and axo-axonic cell types, which innervate the somata and proximal axons of pyramidal cells, respectively (Soriano et al., 1990)
  > — Rivera et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 10540334_bdfa426a -->
- **NT type / functional class:** Dannenberg et al. 2017 — three functionally and
  morphologically distinct Pvalb+ hippocampal subtypes including axo-axonic · [2]
  > Interneurons expressing the calcium binding protein parvalbumin (PV) make up approximately 40% of all GABAergic interneurons. However, this is a heterogeneous group of functionally distinct interneuron subtypes. For example, in the hippocampus alone, there are at least three functionally and morphologically distinct populations of PV + expressing interneurons, namely basket, axo-axonic and bistratified cells. Fast spiking interneurons in the hippocampus and neocortex are often PV + positive and target the soma of pyramidal cells.
  > — Dannenberg et al. 2017, Classification Schemes and Methodological Approaches · [2] <!-- quote_key: 38778375_462ec931 -->
- **Pvalb (Que 2021 patch-seq):** patch-seq dataset providing morphological
  identification of axo-axonic cells alongside Pvalb expression · [3]

</details>

### Cell Ontology mapping

Cell Ontology mapping: pvalb chandelier GABAergic interneuron [[CL:4023036](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023036)] (EXACT).

---

## Results

The hippocampal chandelier cell maps to the WMBv1 supertype 0204 Pvalb
chandelier Gaba_1 [CS20230722_SUPT_0204] (skos:exactMatch by name and
defining-marker concordance), with the cluster 0732 Pvalb chandelier Gaba_1
[CS20230722_CLUS_0732] as the hippocampal child target (F1=0.62 on a mixed
Pvalb source; see figure and property comparison table). Annotation-transfer
evidence on a morphologically confirmed axo-axonic cohort (Que 2021 patch-seq,
n=6) is uninformative at the chandelier supertype: only 1 of 6 AAC cells lands
on SUPT_0204 with the remainder scattering to the Pvalb Gaba_2 basket
supertype, consistent with the documented high transcriptomic similarity
across Pvalb+ morphological subtypes (PMID:33398060) but also limited by the
very small n.

![Filtered AT figure for axo-axonic cell (Yao 2021 SSv4 Pvalb)](figures/f1_for_axo_axonic_yao_pvalb.png)

*F1 across taxonomy levels for the single Pvalb source group in the Yao 2021
SSv4 → WMBv1 transfer (n=66 hippocampal Pvalb cells). Each panel row is a
source-cell group; nodes are coloured by F1 with **Purity** (Pur) and
**Coverage** (Cov) shown inline. Coverage = fraction of source-group cells
landing on this target; Purity = fraction of this target's cells coming from
the source group. With a single source group in the figure, Purity is 1.0 at
every retained target and only Coverage discriminates. F1 ≥ 0.5 at a level
indicates a clean mapping at that resolution. The Pvalb source label
encompasses basket, axo-axonic and bistratified cells, so subtype resolution
below subclass is limited.*

![Filtered AT figure for axo-axonic cell (Que 2021 AAC)](figures/f1_for_axo_axonic_que_aac.png)

*As before, Pur = Purity (fraction of target cells from this source); Cov =
Coverage (fraction of source cells on this target). Que 2021 patch-seq axo-axonic
cells (n=6) — F1 is uninformative across all levels (best=0.24 at cluster on
CLUS_0739, a Pvalb Gaba_2 basket cluster). The small n and high transcriptomic
similarity between Pvalb+ morphological subtypes prevent a clean AT-based call
on this source.*

### 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] · 🟡 MODERATE

**Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | Isocortex [MBA:315], Hippocampal formation [MBA:1089], Olfactory areas [MBA:698] | hippocampal CA1/CA3 layers (CLUS_0732) | DISCORDANT at supertype; APPROXIMATE at best cluster |
| NT type | GABAergic | not asserted | GABA | NOT_ASSESSED at supertype; CONSISTENT at cluster |
| Pvalb expression | defining marker | 7.47 (cohort percentile 0.903; child-coverage 1.00; DEFINING_SCOPED) | 8.56 (cohort percentile 0.971) | CONSISTENT |

*(1 of 1 child clusters with hippocampal coverage (CLUS_0732) is concordant
for Pvalb and partially concordant for CA1 pyramidal-layer location; the
remainder of the supertype's children sit in cortical / olfactory territory
where chandelier cells also occur but outside the hippocampus.)*

**Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| WMBv1 supertype name "Pvalb chandelier Gaba_1" | Atlas metadata | SUPPORT | name + DEFINING_SCOPED Pvalb | atlas-internal |
| Yao 2021 SSv4 Pvalb → WMBv1 AT | Annotation transfer | PARTIAL | F1=0.61 at supertype (n=26/66) | atlas-internal |
| Que 2021 patch-seq AAC → WMBv1 AT | Annotation transfer | PARTIAL | 1/6 to SUPT_0204; F1 uninformative | atlas-internal |

**Supporting evidence.**

- The WMBv1 supertype name "0204 Pvalb chandelier Gaba_1" directly identifies
  this supertype as the chandelier (= axo-axonic) population; the EXACT CL
  mapping CL:4023036 *(pvalb chandelier GABAergic interneuron)* on the
  classical node and the atlas-side label converge on the same biological
  identity.
- DEFINING_SCOPED Pvalb in atlas metadata, with measured mean expression 7.47
  on the supertype (cohort percentile 0.903; child-cluster coverage 1.000),
  confirms uniform Pvalb expression across the supertype's children.
- Yao 2021 (GSE185862) SSv4 transcriptomic transfer of the Pvalb subclass label
  onto WMBv1 places SUPT_0204 as the single strongest Pvalb supertype target
  (F1=0.61, 26/66 cells, Purity=1.0). PARTIAL because the SSv4 "Pvalb" label
  is a mixed population of basket, axo-axonic and bistratified cells —
  morphologically resolved subtype data is required to confirm the
  chandelier-specific correspondence.

**Marker evidence provenance.**

- *Pvalb (defining)*: established at transcript and protein level for
  hippocampal axo-axonic cells in classical IHC (Rivera et al. 2014 [1])
  and confirmed by morphology-targeted patch-seq (Que et al. 2021 [3]).
  Atlas-side DEFINING_SCOPED Pvalb plus precomputed mean 7.47 on the
  supertype (cohort percentile 0.903; child-coverage 1.000) is fully
  concordant. ⚠ **Marker concordance circularity**: the atlas supertype's
  name contains "Pvalb chandelier" — the marker concordance is in part
  nominal at the supertype level. Resolution at the child-cluster level
  (CLUS_0732, see below) is the substantive concordance.

**Concerns.**

- Supertype-level soma location is DISCORDANT with the CA1 pyramidal-layer
  expectation: top counts sit in Isocortex (1159) and Olfactory areas (796),
  with Hippocampal formation third (805); region_fraction_100um is 0.067 —
  the supertype spans cortical and hippocampal chandelier populations
  rather than being hippocampus-specific *(distant region in aggregate —
  `region_fraction_100um: 0.067`; stronger counter-evidence at supertype
  level; the supertype is not the CA1 chandelier population specifically
  but spans multiple regions where axo-axonic cells occur)*.
- Caveat `DISTRIBUTED_ACROSS_CLUSTERS`: supertype anatomy is
  piriform-dominated at top level; hippocampal chandelier cells are
  resolvable only at the child-cluster level (see CLUS_0732 below).
- Caveat `MARKER_NOT_SPECIFIC`: high transcriptomic similarity between
  PV+ morphological subtypes (PMID:33398060) means chandelier-specific
  markers are not fully resolved at supertype level from basket and
  bistratified cells in metadata alone.
- The morphology-confirmed AAC AT (Que 2021, n=6) lands only 1/6 cells on
  SUPT_0204 with 5/6 scattering to the basket supertype SUPT_0206.
  This may reflect either the small-n noise floor or genuine transcriptomic
  similarity between hippocampal AAC and basket cells (PMID:33398060) —
  with n=6 the result is uninformative either way.

**What would upgrade confidence.**

- A morphologically resolved axo-axonic dataset with n ≥ 30 mapped to WMBv1
  (Cre-driver targeting + patch-seq); target F1 ≥ 0.75 at supertype level
  to confirm SUPT_0204 specifically as the chandelier population rather
  than a mixed PV+ supertype.
- Targeted re-mapping of the morphology-confirmed AAC cells in Que 2021
  with a larger cohort (their dataset is publicly available;
  GEO:GSE142546 currently has n=6 AAC).

### 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] · 🟡 MODERATE

**Property comparison.**

| Property | Classical | Cluster (CLUS_0732) | Alignment |
|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | Hippocampal formation [MBA:1089] (305 cells); Field CA1 [MBA:382] (159); Field CA3 [MBA:463] (156) | APPROXIMATE |
| NT type | GABAergic | GABA | CONSISTENT |
| Pvalb expression | defining marker | 8.56 (cohort percentile 0.971) | CONSISTENT |

**Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| WMBv1 cluster name "Pvalb chandelier Gaba_1" + hippocampal counts | Atlas metadata | SUPPORT | CA1/CA3 SO/SP/SR cells | atlas-internal |
| Yao 2021 SSv4 Pvalb → WMBv1 AT | Annotation transfer | PARTIAL | F1=0.62 at cluster (n=23/66) | atlas-internal |
| Que 2021 patch-seq AAC → WMBv1 AT | Annotation transfer | PARTIAL | 0/6 to CLUS_0732 | atlas-internal |

**Supporting evidence.**

- CLUS_0732 is the hippocampal child of SUPT_0204. Atlas anatomy shows it
  carries cells in CA1 stratum oriens (38), CA1 stratum radiatum (23), CA3
  stratum oriens (33), CA3 pyramidal layer (23), CA3 stratum radiatum (15)
  and dentate gyrus granule cell layer (15) — i.e. it is the hippocampus-
  resident chandelier-cell cluster within the supertype.
- Yao 2021 SSv4 Pvalb transcriptomic transfer places CLUS_0732 as the
  single strongest cluster-level hit (F1=0.62, 23/66 cells, Purity=1.0).
- Pvalb on CLUS_0732 is at cohort percentile 0.971 (precomputed mean
  8.56) — uniformly high, consistent with chandelier identity.

**Marker evidence provenance.**

- *Pvalb (defining)*: as above — classical IHC plus patch-seq confirmation;
  atlas-side measured mean 8.56 on the cluster is concordant.
- *Cck (atlas-side neuropeptide, score 8.4)*: unexpectedly high for a
  chandelier cell. Cck is canonically a marker of a separate non-PV
  basket-cell population; presence here may reflect minor contamination
  or genuine low-level peptide co-expression on a subset of cells. Treat
  as flagged pending primary-literature confirmation.

**Concerns.**

- Soma location is APPROXIMATE rather than CONSISTENT: hippocampal
  formation is the top region in painted counts but the cluster also
  carries scatter to other regions; `region_fraction_100um: 0.431` is
  in the boundary band *(boundary scatter — `region_fraction_100um:
  0.431`; could reflect registration error at the CA1 pyramidal-layer
  boundary or genuine spread across hippocampal subfields; weak
  counter-evidence)*.
- Caveat `MARKER_NOT_SPECIFIC`: Cck neuropeptide (atlas score 8.4) is
  unexpectedly high — requires primary-source validation.
- Caveat `OTHER`: dentate gyrus granule cell layer (15 cells) — DG
  chandelier cells are less well characterised in the classical literature.

**What would upgrade confidence.**

- Morphology-confirmed axo-axonic cells (Cre-driver targeting + patch-seq)
  mapped to WMBv1 with F1 ≥ 0.75 at cluster level on CLUS_0732
  specifically. The Que 2021 cohort exists (GEO:GSE142546) but n=6 is too
  small; a targeted re-collection at n ≥ 30 would resolve.
- Primary-literature confirmation or refutation of Cck transcript
  expression on hippocampal axo-axonic cells — currently flagged as a
  potential discrepancy.

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732]` | `0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204]` | 309 | 🟡 MODERATE | hippocampal CA1/CA3 PV+ chandelier-named cluster; Yao Pvalb F1=0.62 | Primary (cluster) |
| `0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204]` | — | 3470 | 🟡 MODERATE | Pvalb DEFINING_SCOPED + chandelier-named supertype; Yao Pvalb F1=0.61 | Primary (supertype) |
| `0739 Pvalb Gaba_2 [CS20230722_CLUS_0739]` | `0206 Pvalb Gaba_2` | 55 | 🔴 LOW | Pvalb+ but basket cluster (Que 2021 maps BC here at F1=0.83) | Eliminated (basket cluster, not chandelier) |
| `0737 Pvalb Gaba_2 [CS20230722_CLUS_0737]` | `0206 Pvalb Gaba_2` | 170 | 🔴 LOW | Pvalb+ stratum-oriens cluster (Que 2021 maps BIC here at F1=0.80) | Eliminated (bistratified-cell cluster) |
| `0206 Pvalb Gaba_2 [CS20230722_SUPT_0206]` | — | 650 | 🔴 LOW | Pvalb+ basket-cell supertype | Eliminated (basket supertype, not chandelier) |
| `0644 Vip Gaba_5 [CS20230722_CLUS_0644]` | `0177 Vip Gaba_5` | 1039 | ⚪ UNCERTAIN | Pvalb 0.32 (cohort pct 0.500); Vip subclass | Eliminated (wrong subclass, Vip) |
| `0649 Vip Gaba_7 [CS20230722_CLUS_0649]` | `0179 Vip Gaba_7` | 409 | ⚪ UNCERTAIN | Pvalb 0.12 (cohort pct 0.265); Vip subclass | Eliminated (wrong subclass, Vip) |
| `0219 Sst Gaba_6 [CS20230722_SUPT_0219]` | — | 725 | ⚪ UNCERTAIN | Pvalb 1.68 cohort pct 0.839; Sst subclass | Eliminated (Sst subclass) |
| `0189 Sncg Gaba_5 [CS20230722_SUPT_0189]` | — | 1065 | ⚪ UNCERTAIN | Pvalb 0.61 cohort pct 0.677; Sncg subclass | Eliminated (Sncg subclass) |
| `0196 RHP-COA Ndnf Gaba_4 [CS20230722_SUPT_0196]` | — | 167 | ⚪ UNCERTAIN | Pvalb 0.48 cohort pct 0.548; Ndnf subclass | Eliminated (Ndnf subclass) |
| `0216 Sst Gaba_3 [CS20230722_SUPT_0216]` | — | 2004 | ⚪ UNCERTAIN | Pvalb 1.48 cohort pct 0.806; Sst subclass | Eliminated (Sst subclass, OLM-type) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical hippocampal axo-axonic
(chandelier) cell is defined here on a CLASSICAL_MULTIMODAL basis as a
GABAergic interneuron with Pvalb as the defining marker [1][3], soma
localised to the CA1 pyramidal layer (UBERON:0014548) [1], and a NT-type
assignment of GABAergic [2]. It is one of three canonical PV+ subtypes
(basket, axo-axonic, bistratified) in the hippocampus.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the
WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using
metadata-based scoring (region match, NT type, defining markers). Full
scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was
compared to the corresponding atlas-side value via the `property_comparisons`
schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT /
NOT_ASSESSED. Atlas-side numerical values came from precomputed expression
on the cluster and from MERFISH spatial registration for soma location.

**Annotation transfer (run 1 — Yao 2021 SSv4 Pvalb).**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Pvalb subclass label, hippocampal cells n=66) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | SSv4 "Pvalb" label is a mixed population (basket + chandelier + bistratified); subtype resolution requires morphology-confirmed source data. |

**Annotation transfer (run 2 — Que 2021 patch-seq AAC).**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE142546 (AAC label, n=6 from 88 QC-passed cells) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper v1.7.1 |
| n cells | 88 (filtered to 88) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_scores_aggregated_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/f1_scores_aggregated_best.csv) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | Patch-seq dataset with morphologically confirmed PV subtypes. TPM input used as pseudo-counts. Age range P10-P77; most cells juvenile (mean P30) vs adult WMBv1. AAC n=6 is insufficient for reliable F1 scoring; treat AAC results as uninformative. BC and BIC cells separate cleanly within SUPT_0206 at cluster level — BC to CLUS_0739 (F1=0.83), BIC to CLUS_0737 (F1=0.80). |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and
verbatim literature quotes in this report are validated against the evidencell
knowledge base at write time. Authored-prose evidence narratives are validated
against their source `evidence_items[*].explanation` fields. The pre-write hook
rejects any unresolvable identifier or unattributed blockquote. Specific
mapping limitations and caveats are documented per-candidate in the
Discussion section.

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0204 | ATLAS_METADATA; ANNOTATION_TRANSFER (×2) | SUPPORT; PARTIAL; PARTIAL | atlas-internal |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0732 | ATLAS_METADATA; ANNOTATION_TRANSFER (×2) | SUPPORT; PARTIAL; PARTIAL | atlas-internal |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0739 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0737 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0644 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0649 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0189 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0196 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA | PARTIAL | atlas-internal |

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:28+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

</details>

---

## Discussion

**Primary mapping:** Axo-axonic (chandelier) cell → 0732 Pvalb chandelier
Gaba_1 [CS20230722_CLUS_0732] at MODERATE confidence (with parent supertype
0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] also MODERATE as a
broader-resolution sibling call). Key support: atlas-side chandelier-cell
naming with DEFINING_SCOPED Pvalb at cluster mean 8.56 (cohort percentile
0.971) plus the highest cluster-level Pvalb-subclass annotation-transfer hit
in Yao 2021 SSv4 (F1=0.62). Key caveats: `MARKER_NOT_SPECIFIC` (high
transcriptomic similarity across PV+ morphological subtypes per
PMID:33398060) and `DISTRIBUTED_ACROSS_CLUSTERS` at supertype level
(cortical / olfactory scatter dilutes the hippocampal signal).
This classical type maps directly to the Cell Ontology term
*pvalb chandelier GABAergic interneuron* [[CL:4023036](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023036)].

### Proposed experiments and follow-ups

- **Morphology-confirmed axo-axonic cell transcriptomic transfer (refined).**
  *What:* targeted patch-seq or Cre-driver-targeted single-cell RNA-seq of
  morphologically reconstructed AIS-targeting cells (cartridge bouton
  morphology) mapped to WMBv1. *Target:* F1 ≥ 0.75 at cluster level on
  CS20230722_CLUS_0732 with n ≥ 30. *Expected output:*
  `AnnotationTransferEvidence` on the CLUS_0732 and SUPT_0204 edges.
  *Resolves:* the chandelier-vs-basket discrimination within Pvalb+; the
  small-n limitation of the Que 2021 AAC cohort (n=6) currently leaves
  this open. *Note*: Que 2021 SSv4 patch-seq (GEO:GSE142546) data are
  publicly available; a re-collection at higher n in the same paradigm
  would directly resolve this without new infrastructure.
- **Cck transcript validation on hippocampal chandelier cells.** *What:*
  targeted literature trawl + smFISH on Pvalb+ AIS-targeting cells for
  Cck expression. *Expected output:* `MarkerAnalysisEvidence` or
  `LiteratureEvidence` resolving the elevated Cck score (8.4) on
  CLUS_0732. *Resolves:* potential `MARKER_NOT_SPECIFIC` caveat on the
  cluster.

### Open questions

1. Does the Que 2021 small-n result (1/6 AAC to chandelier supertype,
   5/6 to basket supertype) reflect genuine cross-subtype transcriptomic
   similarity (PMID:33398060) or under-sampling noise? Resolves with a
   higher-n morphology-confirmed AAC dataset.
2. Why is Cck transcript expression elevated (score 8.4) on the
   hippocampal chandelier cluster CLUS_0732? Is this minor contamination,
   genuine peptide co-expression, or a cell-subset signal?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 · PMID:[25018703](https://pubmed.ncbi.nlm.nih.gov/25018703/) | 25018703 | soma location, Pvalb marker |
| [2] | Dannenberg et al. 2017 · PMID:[29321728](https://pubmed.ncbi.nlm.nih.gov/29321728/) | 29321728 | neurotransmitter type, functional class |
| [3] | Que et al. 2021 · PMID:[33398060](https://pubmed.ncbi.nlm.nih.gov/33398060/) | 33398060 | Pvalb marker, PV+ subtype transcriptomic similarity, AAC patch-seq |

<!-- verdict-block-start: edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0204 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.6
  relationship: skos:exactMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Atlas supertype named "Pvalb chandelier Gaba_1"
    directly identifies the chandelier (axo-axonic) population with
    DEFINING_SCOPED Pvalb (cohort percentile 0.903, child-coverage 1.000);
    cluster annotation transfer (Yao 2021 SSv4 Pvalb subclass label;
    at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1) places SUPT_0204 as the
    single strongest Pvalb supertype hit (F1=0.61, n=26/66, Purity=1.0).
    Supertype-level soma scatter (Isocortex, Olfactory areas) is expected
    because chandelier cells occur in many regions; the hippocampal
    chandelier population is resolved at child cluster
    CS20230722_CLUS_0732 (paired survivor edge).
  reconciliation_note: >
    Paired with edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0732
    (best-child cluster for the hippocampal axo-axonic population within
    this supertype).
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Supertype anatomy is multi-regional (Isocortex 1159, Hippocampal
        formation 805, Olfactory areas 796 painted counts;
        region_fraction_100um=0.067 against MBA:407); hippocampal
        chandelier cells are resolvable at the child cluster
        CS20230722_CLUS_0732.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        High transcriptomic similarity between PV+ morphological subtypes
        (PMID:33398060) means chandelier-specific markers are not fully
        resolved at supertype level from basket and bistratified cells.
    - caveat_type: LOW_CELL_COUNT
      description: >
        Morphology-confirmed AAC AT (Que 2021,
        at_run_20260508_que2021_pvin_mmc_wmbv1) is n=6 and lands only 1/6
        cells on SUPT_0204; the source dataset is too small for an
        informative direct chandelier-cell F1 call.
  proposed_experiments:
    - >
      Morphology-confirmed axo-axonic patch-seq or Cre-driver scRNA-seq
      cohort (n>=30) mapped to WMBv1 via cluster annotation transfer;
      target F1>=0.75 at SUPT_0204 to confirm chandelier-specific
      correspondence at supertype level.
  unresolved_questions:
    - >
      Trawl literature for hippocampal axo-axonic vs basket cell
      transcriptomic divergence beyond PMID:33398060 — atlas-side
      indistinguishability at supertype level may reflect genuine
      biology or current dataset limits.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0732 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.6
  relationship: skos:exactMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Hippocampal child of CS20230722_SUPT_0204 within the
    "Pvalb chandelier Gaba_1" supertype. Atlas anatomy carries cells across
    CA1 SO, CA1 SR, CA3 SO, CA3 pyramidal layer, CA3 SR and DG granule
    layer (region_fraction_100um=0.431 against MBA:407, boundary scatter);
    Pvalb cluster mean 8.56 at cohort percentile 0.971 (CONSISTENT with
    defining-marker classical assertion). Yao 2021 SSv4 Pvalb subclass
    cluster annotation transfer (at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1)
    places CS20230722_CLUS_0732 as the single strongest cluster-level
    Pvalb hit (F1=0.62, n=23/66, Purity=1.0). 2 of 3 markers/properties
    CONSISTENT (NT, Pvalb), 1 APPROXIMATE (location, boundary scatter).
  reconciliation_note: >
    Paired with edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0204
    (parent supertype survivor); CLUS_0732 is the hippocampus-specific
    child within that supertype.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Cck atlas-side neuropeptide score 8.4 unexpectedly high for a
        chandelier cell; potential discrepancy with classical chandelier
        marker profile requires primary-source validation.
    - caveat_type: LOW_CELL_COUNT
      description: >
        Morphology-confirmed AAC AT
        (at_run_20260508_que2021_pvin_mmc_wmbv1) is n=6 and lands 0/6
        cells on CS20230722_CLUS_0732 (5/6 to CS20230722_CLUS_0739 in the
        basket supertype); uninformative at this n.
  proposed_experiments:
    - >
      Higher-n morphology-confirmed axo-axonic cluster annotation transfer
      (patch-seq or Cre-driver scRNA-seq, n>=30) targeting F1>=0.75 at
      CS20230722_CLUS_0732 specifically.
    - >
      Targeted smFISH validation of Cck transcript on Pvalb+ AIS-targeting
      hippocampal cells to resolve the atlas-side Cck score 8.4 anomaly.
  unresolved_questions:
    - >
      Is the elevated Cck atlas-side score on CS20230722_CLUS_0732 a real
      peptide co-expression signal in chandelier cells, minor
      contamination, or a cell-subset feature?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0739 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0739 sits in the Pvalb Gaba_2 (basket)
    supertype, not the chandelier supertype; morphologically identified
    PV basket cells map preferentially to this cluster in independent
    patch-seq evidence — wrong PV+ subtype for the axo-axonic
    classical type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0737 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0737 sits in the Pvalb Gaba_2 supertype
    and is the preferred bistratified-cell target in independent
    morphology-labelled patch-seq evidence — wrong PV+ subtype for the
    axo-axonic classical type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0644 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_CLUS_0644 is in the Vip Gaba_5 supertype with
    Pvalb mean 0.32 (cohort percentile 0.500) — wrong subclass for a
    Pvalb-defined axo-axonic cell.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_axo_axonic_cell_hippocampus_to_CS20230722_CLUS_0649 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_CLUS_0649 is in the Vip Gaba_7 supertype with
    Pvalb mean 0.12 (cohort percentile 0.265, APPROXIMATE) — wrong
    subclass for a Pvalb-defined axo-axonic cell.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0206 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0206 (Pvalb Gaba_2) is the basket-cell
    supertype within the Pvalb subclass — morphologically confirmed
    basket cells map here in independent patch-seq evidence. Wrong
    PV+ subtype for the axo-axonic classical type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0219 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0219 is in the Sst subclass with
    Pvalb 1.68 (cohort percentile 0.839) — wrong subclass for a
    Pvalb-defined axo-axonic cell.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0189 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0189 is in the Sncg subclass with
    Pvalb 0.61 (cohort percentile 0.677) — wrong subclass for a
    Pvalb-defined axo-axonic cell.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0196 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0196 is the RHP-COA Ndnf Gaba_4 supertype
    with Pvalb 0.48 (cohort percentile 0.548) — wrong subclass and
    region (retrohippocampal / cortical amygdala) for a CA1-pyramidal
    layer Pvalb-defined axo-axonic cell.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_axo_axonic_cell_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0216 is the Sst Gaba_3 supertype (the
    OLM-type Sst supertype) with Pvalb 1.48 (cohort percentile 0.806) —
    wrong subclass for a Pvalb-defined axo-axonic cell.
```
<!-- verdict-block-end -->
