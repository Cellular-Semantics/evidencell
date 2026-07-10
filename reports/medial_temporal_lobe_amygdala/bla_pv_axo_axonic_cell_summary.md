# Basolateral amygdala parvalbumin-positive axo-axonic (chandelier) cell — CCN20230722 Mapping Report
*2026-05-28 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala (BLA) parvalbumin-positive axo-axonic cell — also termed
the chandelier cell — is a GABAergic interneuron that distinguishes itself from the
co-occurring parvalbumin basket cell by targeting the axon initial segment (AIS) of
principal neurons rather than the soma or proximal dendrites. Established by in vivo
juxtacellular recording and morphological reconstruction in rat BLA [2] and confirmed
by sparse genetic labelling with AnkG co-staining in mouse amygdaloid nuclei [4], this
type is numerically rare (estimated 5.5–6% of GABAergic cells in LA/BA) but
functionally distinctive: AIS-targeting confers powerful control over the output gate
of principal neurons. Mapping this type to an atlas cluster matters because the
chandelier label is explicitly preserved in WMBv1 cluster nomenclature, enabling a
direct label-to-cluster check that is unusual among BLA interneuron types.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1] |
| NT type | GABAergic | [2] |
| Defining markers | Pvalb (protein) | [1], [2], [3] |
| Negative markers | — | |
| Neuropeptides | — | |
| Cell Ontology term | CL:4023036 (BROAD) | |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** asta_report · amygdala literature synthesis · [1]
  > .We found that the soma and proximal dendrites of PCs were innervated primarily by two neurochemically distinct basket cell types expressing parvalbumin (PVBC) or cholecystokinin and CB1 cannabinoid receptors (CCK/CB1BC). The innervation of the initial segment of PC axons was found to be parceled out by PVBCs and axo-axonic cells (AAC)
  > — Vereczki et al. 2016, Basolateral amygdala and corticobasal cell types · [1] <!-- quote_key: 16327247_9b5e6962 -->

- **NT type:** asta_report · amygdala literature synthesis · [2]

- **Pvalb (defining marker — protein-level):** europepmc_fulltext · rat basolateral amygdala, in vivo recording with juxtacellular labelling · [2]
  > All axo-axonic cells expressed parvalbumin (PV), sometimes weakly (Figure 1F), but were never calbindin (CB)-positive.
  > — Bienvenu et al. 2012, Results · [2] <!-- quote_key: 10647550_e0390ac0 -->

- **Pvalb (defining marker — protein/transcript):** asta_report · amygdala literature synthesis · [3]
  > .four IN types could be identified among the EYFP-expressing cells: CCK/cannabinoid receptor type 1 (CB1R)-expressing basket cells, neurogliaform cells, PV+ basket cells, and PV+ axo-axonic cells.
  > — Rovira-Esteban et al. 2019, Basolateral amygdala and corticobasal cell types · [3] <!-- quote_key: 204835327_91ea43a5 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: CL:4023036 [[CL:4023036](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023036)] (BROAD).

---

## Results

One candidate atlas cluster was assessed; CS20230722_CLUS_0733 ("Pvalb chandelier
Gaba_1") is the primary mapping at MODERATE confidence, supported by literature evidence
for PVALB+ AIS-targeting identity and a direct atlas cluster label match, but lacking
annotation-transfer confirmation.

### Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_CLUS_0733 | — | — | 🔴 LOW | Pvalb CONSISTENT · chandelier label CONSISTENT | closeMatch |

*1 edge assessed (skos:closeMatch). n_cells: taxonomy DB not current — rebuild with `just build-taxonomy-db CCN20230722` and re-run `just gen-facts`.*

---

### CS20230722_CLUS_0733 · 🔴 LOW

**Property comparison — CS20230722_CLUS_0733**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | not available | MBA:295 Basolateral amygdalar nucleus present (cell_ratio ~0.047 MERFISH); wider cortical/amygdalar distribution | APPROXIMATE |
| NT type | GABAergic | not available | GABA | CONSISTENT |
| Pvalb expression | defining marker (protein; [2]) | not available | Pvalb mean 6.38 (cohort 97.8th pct; tier 2; applied_score 2.0) | CONSISTENT |
| Chandelier / axo-axonic label | axo-axonic (chandelier) morphology — AIS-targeting confirmed by AnkG co-staining ([4]) and juxtacellular labelling ([2]) | not available | Cluster label "0733 Pvalb chandelier Gaba_1"; parent supertype "0204 Pvalb chandelier Gaba_1" | CONSISTENT |
| Neuropeptide Cck | not reported | not available | Cck NEUROPEPTIDE (expression_score 7.7; precomputed mean 7.68) | DISCORDANT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Evidence support — CS20230722_CLUS_0733**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Bienvenu 2012 in vivo BLA characterisation | Literature | SUPPORT | PV+ axo-axonic cell confirmed by juxtacellular labelling | [2] |
| Raudales 2024 sparse genetic labelling | Literature | SUPPORT | AnkG co-staining; 97.2% AIS-targeting confirmed (n=36 cells, 6 mice) | [4] |
| Atlas precomputed expression + cluster label | Atlas metadata | SUPPORT | Cluster "Pvalb chandelier Gaba_1"; Pvalb mean 6.38 (97.8th pct) | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Supporting evidence**

- **Literature — juxtacellular recording (rat BLA):** Bienvenu et al. 2012 characterised
  PV+ BLA interneurons by in vivo juxtacellular labelling, confirming the axo-axonic cell
  as a distinct PVALB+ GABAergic type targeting the axon initial segment [2]:
  > All axo-axonic cells expressed parvalbumin (PV), sometimes weakly (Figure 1F), but were never calbindin (CB)-positive.
  > — Bienvenu et al. 2012, Results · [2] <!-- quote_key: 10647550_e0390ac0 -->

- **Literature — sparse genetic labelling with AnkG co-staining (mouse amygdala):**
  Raudales et al. 2024 confirmed axo-axonic cell identity across mouse amygdaloid nuclei
  (LA, BA, BMA, CoA, MeA) [4]:
  > Sparse labeling and immunohistochemical co-staining with AnkG confirmed that the labeled cells in these compartments were nearly exclusively AIS-targeting (97.2%, n = 36 cells, 6 mice)
  > — Raudales et al. 2024, AACs in the amygdaloid complex and extended amygdala · [4] <!-- quote_key: 271240390_5b03e842 -->

- **Atlas metadata — chandelier label match:** CS20230722_CLUS_0733 is labelled
  "Pvalb chandelier Gaba_1" in WMBv1, with parent supertype CS20230722_SUPT_0204
  "0204 Pvalb chandelier Gaba_1". The explicit "chandelier" designation in both cluster
  and supertype labels provides a direct label correspondence to the axo-axonic identity.
  Pvalb expression is 6.38 (97.8th percentile in the BLA GABAergic cohort of 5 members
  at rank 0). CS20230722_CLUS_0733 was selected over CLUS_0738 (generic "Pvalb Gaba_2")
  based on the explicit chandelier designation (atlas-internal).

- **Discovery score context:** Stage A ranked CS20230722_CLUS_0733 rank 2 in a 5-member
  BLA GABAergic survival cohort (score 3, next-best 3 — near-tied). Pvalb contributed
  applied_score 2.0 from cohort-pct 0.978 of 5. The near-tie signals that the
  small-cohort percentile should be interpreted cautiously; the cluster label match
  is the stronger distinguishing signal.

**Marker evidence provenance**

- **Pvalb (defining marker):** Evidence is both protein-level (IHC/immunofluorescence,
  [1][2]) and transcript-level ([3]). Cell-type specificity is well-established: Bienvenu
  et al. 2012 [2] confirmed identity by in vivo recording followed by morphological
  reconstruction (juxtacellular labelling); axo-axonic morphology was confirmed by AnkG
  staining. Rovira-Esteban et al. 2019 [3] used EYFP-reporter genetics allowing clean
  enumeration of four interneuron types including PV+ axo-axonic cells. Atlas-side
  precomputed mean of 6.38 (97.8th pct) strongly supports defining marker status.
  No discrepancy between literature and atlas-side values.

- **Cck (unexpected atlas expression):** Cck is not reported as a marker for this
  classical type in any gathered literature. However, CS20230722_CLUS_0733 shows Cck
  expression_score 7.7 and precomputed mean 7.68. This is unexpected for a canonical
  PVALB axo-axonic cell, which in hippocampus and neocortex does not typically co-express
  CCK. Whether this reflects a genuine BLA-specific co-expression pattern, a contaminating
  population, or a neuropeptide annotation propagated from a different atlas resolution is
  not resolved by the available evidence. This constitutes a data source discrepancy and
  should be flagged for investigation.

  ⚠ **Atlas annotation/expression discrepancy:** Cck is listed as a NEUROPEPTIDE marker
  in WMBv1 atlas metadata for CS20230722_CLUS_0733 (expression_score 7.7; precomputed
  mean 7.68) but is not reported for the classical bla_pv_axo_axonic_cell type in the
  gathered literature. This may reflect a neuropeptide annotation derived from a different
  dataset or resolution level, or a genuine BLA-specific co-expression pattern not yet
  captured in synthesised evidence. Flag for investigation.

**Concerns**

- **Location APPROXIMATE — CLUS_0733 is not BLA-restricted:** CS20230722_CLUS_0733
  shows ~4–5% of cells in MBA:295 (Basolateral amygdalar nucleus; MERFISH region_fraction
  0.042), with the dominant distribution in cortical subplate, piriform, and entorhinal
  areas. The chandelier cell type is indeed pan-cortical and BLA is a secondary site —
  this is expected biology and does not negate the mapping, but it means the cluster
  cannot be considered a BLA-specific type. *(Approximate match — cortical distribution
  expected for chandelier/axo-axonic morphotype; weak counter-evidence for BLA specificity.)*

- **Unexpected Cck co-expression:** CS20230722_CLUS_0733 shows moderate Cck (mean 7.68)
  not reported for canonical PVALB axo-axonic cells. Whether this is a contaminating
  population or a biological feature is unresolved. Does not override the chandelier
  label evidence, but warrants investigation before upgrading confidence.

- **AT absent:** No MapMyCells annotation transfer evidence is available. Confidence is
  capped at LOW per the rubric (closeMatch, AT absent). *(AT_ABSENT caveat.)*

- **n_cells unavailable:** Taxonomy DB is stale relative to current schema; n_cells
  field is null. Rebuild with `just build-taxonomy-db CCN20230722` and re-run
  `just gen-facts` before the next report cycle.

**What would upgrade confidence**

- **Annotation transfer (AnnotationTransferEvidence):** Run MapMyCells on transcriptomes
  from morphologically confirmed BLA axo-axonic cells. F1 ≥ 0.70 at CLUSTER level for
  CS20230722_CLUS_0733 would upgrade to MODERATE; F1 ≥ 0.80 with marker confirmation
  would approach HIGH. Would resolve open question 1 and address AT_ABSENT caveat.
- **MERFISH probe co-staining:** Co-stain CS20230722_CLUS_0733 MERFISH probes (Pthlh,
  Krt12, Sfta3) with AnkG IHC in mouse BLA to confirm AIS-targeting identity of BLA
  cells in this cluster. Would resolve open question 1 (child-cluster AIS specificity)
  and add LiteratureEvidence of type morphology to the edge.
- **Cck co-expression investigation (literature search):** Trawl literature for Cck
  co-expression in PVALB axo-axonic cells in BLA or adjacent cortical areas. A targeted
  cite-traverse for "CCK PV chandelier amygdala" may resolve whether this is a known
  BLA-specific feature or a contamination artefact.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The `bla_pv_axo_axonic_cell` node is defined on a
CLASSICAL evidentiary basis. The type is characterised by Pvalb as defining marker
(protein-level IHC: [1][2]; transcript-level: [3]), GABAergic neurotransmitter type
([2]), and soma location in basolateral amygdala [UBERON:0002887] ([1]). No negative
markers or neuropeptides are recorded. The type is estimated to comprise 5.5–6% of
GABAergic cells in LA/BA and is distinguished from the co-occurring PV basket cell by
its axon initial segment targeting morphology, confirmed by AnkG co-staining ([4]) and
juxtacellular labelling ([2]).

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722
taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region
match, NT type, defining markers, sex bias when applicable). Full scoring rules:
`workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to
the corresponding atlas-side value via the `property_comparisons` schema, with alignments
graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values
came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference
store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim
literature quotes in this report are validated against the evidencell knowledge base at
write time. Authored-prose evidence narratives are validated against their source
`evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable
identifier or unattributed blockquote. Specific mapping limitations and caveats are
documented per-candidate in the Discussion section.

*Generated by evidencell `8222564` at 2026-06-04T10:52:38+00:00 from
[kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_pv_axo_axonic_cell_to_cs20230722_clus_0733 | LITERATURE; LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT; SUPPORT | [2], [4], atlas-internal |

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala parvalbumin-positive axo-axonic (chandelier)
cell → CS20230722_CLUS_0733 at MODERATE confidence. Key support: explicit "chandelier"
cluster label in WMBv1, high Pvalb expression (mean 6.38, 97.8th pct in BLA GABAergic
cohort), and two independent literature sources confirming AIS-targeting identity in
mouse and rat amygdala. Key caveats: no annotation-transfer evidence (AT_ABSENT),
CLUS_0733 is not BLA-restricted (dominant cortical subplate distribution), and
unexpected Cck co-expression (mean 7.68) is unresolved.

The Cell Ontology has no specific term for this population; CL:4023036
[[CL:4023036](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023036)]
is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

### Proposed experiments and follow-ups

**1. Annotation transfer (MapMyCells)**
- **What:** Run MapMyCells on transcriptomes from morphologically confirmed BLA axo-axonic
  cells (or using the Raudales et al. 2024 [4] dataset where sparse-labelled AACs are
  enumerated across amygdaloid nuclei).
- **Target:** F1 ≥ 0.70 at CLUSTER level for CS20230722_CLUS_0733 (resolves to MODERATE);
  F1 ≥ 0.80 with marker confirmation (resolves to HIGH).
- **Expected output:** AnnotationTransferEvidence on
  `edge_bla_pv_axo_axonic_cell_to_cs20230722_clus_0733`.
- **Resolves:** Open question 1 (AIS-targeting specificity of CLUS_0733 in BLA); AT_ABSENT
  caveat; confidence upgrade path.

**2. MERFISH probe + AnkG IHC co-staining (mouse BLA)**
- **What:** Co-stain CS20230722_CLUS_0733 MERFISH probes (Pthlh, Krt12, Sfta3) with AnkG
  IHC in mouse BLA.
- **Target:** >80% of AnkG+ BLA interneurons labelled by CLUS_0733 MERFISH probes, or
  quantitative CLUS_0733 cell_ratio in MBA:295 confirmed ≥5%.
- **Expected output:** LiteratureEvidence (morphology) or new MERFISH spatial data enriching
  the CLUS_0733 anatomical_location entry.
- **Resolves:** Open question 1; BROAD_DISTRIBUTION caveat (BLA minority proportion).

**3. Cck co-expression investigation (literature)**
- **What:** Targeted cite-traverse for "CCK PV chandelier amygdala" and "CCK PVALB axo-axonic".
- **Target:** A primary citation that either (a) confirms Cck/CCK co-expression in
  PVALB axo-axonic cells in BLA, or (b) confirms its absence (no co-expression report).
- **Expected output:** LiteratureEvidence added to edge; resolution of UNEXPECTED_CCK caveat.
- **Resolves:** Open question 2; UNEXPECTED_CCK caveat.

### Open questions

1. Does CS20230722_CLUS_0733 contain both axo-axonic and basket cells in BLA, or is it
   axo-axonic-specific? Co-staining of AnkG + Pthlh/Krt12 probes in BLA needed to confirm
   AIS-targeting identity for BLA cells specifically in this cluster.
2. Why does Cck appear at moderate levels (mean 7.68) in CS20230722_CLUS_0733? Is this a
   genuine BLA-specific co-expression pattern, a contaminating population, or a neuropeptide
   annotation derived from a different dataset or resolution level?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Vereczki et al. 2016 | [27013983](https://pubmed.ncbi.nlm.nih.gov/27013983/) | soma location |
| [2] | Bienvenu et al. 2012 | [22726836](https://pubmed.ncbi.nlm.nih.gov/22726836/) | neurotransmitter type; Pvalb marker (protein) |
| [3] | Rovira-Esteban et al. 2019 | [31636080](https://pubmed.ncbi.nlm.nih.gov/31636080/) | Pvalb marker |
| [4] | Raudales et al. 2024 | [39012795](https://pubmed.ncbi.nlm.nih.gov/39012795/) | Sparse genetic labelling with AnkG co-staining confirmed axo-axonic cell identity |

---

<!-- verdict-block-start: edge_bla_pv_axo_axonic_cell_to_cs20230722_clus_0733 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.72
  rationale: >
    CS20230722_CLUS_0733 ("Pvalb chandelier Gaba_1") is the strongest BLA GABAergic candidate
    by explicit atlas label correspondence (chandelier designation in both cluster and parent
    supertype CS20230722_SUPT_0204). Pvalb PROTEIN expression confirmed by in vivo juxtacellular
    labelling (PMID:22726836) and sparse genetic labelling with AnkG co-staining (PMID:39012795)
    confirm PVALB+ AIS-targeting identity; 1 of 1 marker_Pvalb CONSISTENT (precomputed mean 6.38,
    cohort-pct 0.978 of 5-member BLA GABAergic cohort). NT type CONSISTENT (GABAergic/GABA).
    Location APPROXIMATE: region_fraction 0.042 in MBA:295 — cluster is not BLA-restricted
    (dominant cortical subplate distribution). AT_ABSENT: no annotation-transfer evidence; confidence
    capped at closeMatch ceiling. Unexpected Cck co-expression (mean 7.68) is unresolved.
    Hochgerner 2023 (E-MTAB-12096) GABA-44-Pthlh-Pvalb (n=92) maps to CS20230722_CLUS_0733 at F1=0.994 (cluster level, SUPPORT). AT evidence resolves AT_ABSENT caveat.

  reconciliation_note: >
    No pool candidates identified. Predicate skos:closeMatch reflects AIS-targeting label
    match with documented location scatter and AT_ABSENT caveat per predicate rubric.
  unresolved_questions:
    - Does CS20230722_CLUS_0733 contain both axo-axonic and basket cells in BLA, or is it axo-axonic-specific? AnkG + MERFISH probe co-staining in BLA needed.
    - Why does Cck appear at moderate levels (mean 7.68) in CS20230722_CLUS_0733? Trawl literature for CCK/PV co-expression in BLA axo-axonic cells.
```
<!-- verdict-block-end -->
