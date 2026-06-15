# Paralaminar/ventral amygdala immature excitatory neuron — CCN20230722 Mapping Report
* · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Paralaminar/ventral amygdala immature excitatory neurons are a primate-enriched population occupying the paralaminar nucleus [UBERON:0002887] and adjacent ventral amygdala territory. They are defined by a suite of immaturity and progenitor-state markers — DCX, BCL2, NES, VIM, MKI67, SP8, NR2F2, PROX1, NCAM1, RBFOX3, and TUBB3 — and are negative for NKX2-1, which excludes a medial ganglionic eminence origin [1, 2]. The population spans a developmental continuum from actively dividing progenitors (Ki-67+ vimentin+ nestin+) through postmitotic immature neurons (DCX+ BCL2+ NeuN+), and persists into childhood and adolescence on a protracted developmental timeline [4]. Characterising their atlas correspondence is important for contextualising adult-atlas transcriptomic data in the amygdala and for understanding the extent of primate-specific neurogenesis.

### Classical type description

| Property | Value | References |
|---|---|---|
| Soma location | Paralaminar nucleus [UBERON:0002887]; also present in ventral amygdala, anterior entorhinal cortex, layer II perirhinal cortex | [1], [2], [3], [4] |
| NT type | Glutamatergic (inferred from lineage context; no explicit NT recording) | — |
| Defining markers | DCX, BCL2, NCAM1, RBFOX3, TUBB3, VIM, NES, MKI67, SP8, NR2F2, PROX1 | [1], [2] |
| Negative markers | NKX2-1 (excludes MGE origin) | [1] |
| Neuropeptides | None documented | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location and defining markers:** immunohistochemistry on human temporal lobe · Sorrells et al. 2019 [1]
  > The PL develops next to the CGE which is highly proliferative in humans (Hansen et al., 2013) . To determine whether the PL forms from progenitors in the CGE we immunostained the human temporal lobe for Ki-67 to label dividing cells, and for transcription factors expressed in the CGE (SP8, COUP-TFII, and PROX1) (Ma et al., 2013)(Hansen et al., 2013)(Miyoshi et al., 2015)(Rubin et al., 2013)
  > — Sorrells et al. 2019, Non-neuronal and immature neuron populations · [1] <!-- quote_key: 195246702_dd079f9e -->

- **Negative markers (NKX2-1):** immunohistochemistry on human temporal lobe · Sorrells et al. 2019 [1]
  > Regions with high Ki-67 + cell density contained many SP8 + COUP-TFII + cells, few NKX2.1 + cells that would be likely be medial ganglionic eminence-derived, and a dense field of vimentin + nestin + cells and DCX + PSA-NCAM + cells (Fig. 1f, g)
  > — Sorrells et al. 2019, Non-neuronal and immature neuron populations · [1] <!-- quote_key: 195246702_302eefd5 -->

- **Soma location and defining markers (DCX, BCL2):** immunohistochemistry on human and non-human primate temporal lobe · Chareyron et al. 2021 [2]
  > Our current findings demonstrate that the population of immature neurons found in the ventral amygdala is not an isolated population but may be part of a larger group of Bcl-2-positive and NeuN-positive cells that extends from the SVZ of the lateral ventricle to the paralaminar nucleus and some cortical areas within the medial temporal lobe. The presence of these immature neurons in the ventral amygdala, anterior entorhinal cortex and layer II of the perirhinal cortex can be observed on coronal or sagittal sections of the temporal lobe labeled with DCX or Bcl-2 markers (Bernier et al., 2002)(Fudge, 2004)(0).
  > — Chareyron et al. 2021, Non-neuronal and immature neuron populations · [2] <!-- quote_key: 235715856_1045f5c1 -->

- **Soma location (ventral amygdala; primate distribution):** review / histology · Villard et al. 2023 [3]
  > populations of immature neurons expressing the anti-apoptosis Bcl2 protein have been observed in several regions of the adult mammalian brain, including the ventromedial amygdala and the temporal cortex in humans and non-human primates (Bernier et al., 2002)(Bernier et al., 1998)(Fudge, 2004)(Yachnis et al., 2000)
  > — Villard et al. 2023, Non-neuronal and immature neuron populations · [3] <!-- quote_key: 259201574_70036ef8 -->

- **Developmental timeline and progenitor dynamics:** Page et al. 2022 [4]
  > The PL contains a large population of immature excitatory neurons at birth, some of which may continue to be born from local progenitors. These progenitors disappear rapidly in infancy, but the immature neurons persist throughout childhood and adolescent ages, indicating that they develop on a protracted timeline.
  > — Page et al. 2022, Paralaminar nucleus immature excitatory neurons · [4] <!-- quote_key: 250411527_03961399 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: immature neuron [[CL:4042028](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4042028)] (BROAD).

*(note: The CL:4042028 mapping was auto-proposed during report ingest and requires expert review. A dedicated CL term for this primate-specific population does not currently exist; this type is a strong candidate for a new CL contribution.)*

---

## Results

No atlas cluster in CCN20230722 (WMBv1) constitutes a biologically meaningful correspondent for the paralaminar/ventral amygdala immature excitatory neuron. This population is primate-enriched, defined by neuroblast immaturity markers (DCX, BCL2, VIM, NES, MKI67) that are absent from adult mouse transcriptomes, and it occupies an anatomical zone — the paralaminar nucleus [UBERON:0002887] — with no direct CCF20 equivalent in the mouse brain atlas. Cross-species snRNA-seq evidence (cited in the ATLAS_METADATA evidence item on the single assessed candidate) explicitly identifies these neurons as absent from mouse datasets. The single candidate assessed here, 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005], was retrieved by a regional/NT filter in the absence of a true homolog and is not a supported biological equivalence.

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] | — | 798 | ⚪ UNCERTAIN | Primate-enriched; DCX/BCL2/VIM absent from adult mouse | Eliminated (species barrier; no adult mouse homolog) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The paralaminar/ventral amygdala immature excitatory neuron is defined on a CLASSICAL basis — primary immunohistochemistry studies on human and non-human primate temporal lobe tissue. Defining markers are DCX, BCL2, NCAM1, RBFOX3, TUBB3, VIM, NES, MKI67, SP8, NR2F2, and PROX1; the population is negative for NKX2-1, consistent with a CGE rather than MGE origin. Soma location is the paralaminar nucleus [UBERON:0002887] and adjacent ventral amygdala, anterior entorhinal cortex, and perirhinal cortex layer II [1–4].

**Atlas mapping query.**
> Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.**
> Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.**
> All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

<details>
<summary>Full evidence base</summary>

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_paralaminar_immature_neuron_to_cs20230722_supt_0005 | ATLAS_METADATA | AGAINST | atlas-internal |

</details>

*Generated by evidencell `bfdb7f1` at 2026-06-15T10:49:37+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** No biologically supported correspondence exists between the paralaminar/ventral amygdala immature excitatory neuron and any CCN20230722 cluster. The single candidate assessed, 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005], was recovered by regional and NT proximity filter and carries UNCERTAIN confidence with evidence against biological equivalence. Key caveats: (1) species barrier — paralaminar immature neurons are a primate-enriched population explicitly absent from adult mouse transcriptomic datasets; (2) marker incompatibility — the defining immaturity markers (DCX, VIM, NES, MKI67, BCL2) are not expressed in adult mouse transcriptomic types.

The Cell Ontology has no specific term for this primate-specific population; CL:4042028 (immature neuron) is the closest available ancestor. This mapping was auto-proposed during report ingest and requires expert review. Given the distinctive biology of these cells — primate-specific, protracted developmental timeline, CGE lineage, DCX+/BCL2+ immaturity state — this population is a strong candidate for a new, more specific CL term capturing paralaminar/ventral amygdala immature excitatory neurons as a primate class.

### Proposed experiments and follow-ups

**1. MapMyCells annotation transfer from human paralaminar snRNA-seq data**
- **What:** Run MapMyCells on publicly available human amygdala snRNA-seq datasets (e.g. Sorrells et al. 2019 or Caglayan et al. 2023, if accessible in h5ad format) using WMBv1 as the reference atlas.
- **Target:** Identify any mouse atlas cluster that receives partial transfer signal from DCX+/BCL2+/PROX1+ cells.
- **Expected output:** AnnotationTransferEvidence items showing partial F1 transfer (likely low, reflecting the species gap rather than a clean match).
- **Resolves:** Open question 1 (Does any cross-species dataset reveal a mouse cluster partially matching the paralaminar population?); would also determine whether the IT EP-CLA Glut_3 [CS20230722_SUPT_0005] candidate is the true closest type or whether a different cluster (e.g. in endopiriform nucleus) is closer.

**2. Targeted re-analysis of WMBv1 in endopiriform nucleus**
- **What:** Run `just find-candidates` restricted to MBA:942 (endopiriform nucleus) to assess whether this territory yields a closer candidate than the current EP-CLA Glut_3 supertype.
- **Target:** Identification of a candidate with lower discordance on location and/or markers.
- **Expected output:** Revised MappingEdge set; may upgrade to LOW confidence if a closer regional match exists.
- **Resolves:** Open question 2.

**3. IHC confirmation of paralaminar marker absence in adult mouse amygdala**
- **What:** Immunohistochemistry for DCX, BCL2, and NES in adult mouse amygdala sections.
- **Target:** Formal confirmation that no DCX+/BCL2+ population is present in the adult mouse paralaminar or periamygdaloid territory.
- **Expected output:** LiteratureEvidence item documenting species barrier empirically (REFUTE signal for any proposed mouse-side correspondence).
- **Resolves:** Establishes the definitive ground truth for the species barrier caveat.

### Open questions

1. Does any cross-species snRNA-seq dataset contain a mouse cluster partially matching the DCX+/BCL2+/PROX1+ paralaminar population?
2. Would targeted re-analysis of WMBv1 in endopiriform nucleus [MBA:942] reveal a closer candidate than the IT EP-CLA Glut_3 supertype?
3. Should this population be submitted as a new CL term? The combination of primate-specificity, CGE lineage, and protracted postnatal developmental trajectory is biologically well-described and would benefit from a dedicated ontology node distinct from the generic CL:4042028 (immature neuron).

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Sorrells et al. 2019 | [31227709](https://pubmed.ncbi.nlm.nih.gov/31227709/) | Soma location, defining markers, negative markers |
| [2] | Chareyron et al. 2021 | [34206571](https://pubmed.ncbi.nlm.nih.gov/34206571/) | Soma location, defining markers |
| [3] | Villard et al. 2023 | [37337377](https://pubmed.ncbi.nlm.nih.gov/37337377/) | Soma location |
| [4] | Page et al. 2022 | [35841648](https://pubmed.ncbi.nlm.nih.gov/35841648/) | Soma location, developmental timeline |

---

<!-- verdict-block-start: edge_paralaminar_immature_neuron_to_cs20230722_supt_0005 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Paralaminar/ventral amygdala immature excitatory neurons are a primate-enriched population with defining immaturity markers (DCX, BCL2, VIM, NES, MKI67) absent from adult mouse transcriptomic types; ATLAS_METADATA evidence explicitly argues against biological equivalence to any WMBv1 type. CS20230722_SUPT_0005 was the only candidate retrieved from MBA:295 proximity filter (score 1, cohort_size 5, rank 1 in a tie) and carries DISCORDANT location_soma (cortical subplate / EP-CLA territory) and DISCORDANT marker_DCX alignment. No annotation transfer evidence exists. This is a species-barrier null result, not a mapping failure.
  reconciliation_note: >
    No WMBv1 cluster constitutes a biologically supported homolog. The UNCERTAIN verdict reflects a species-barrier gap rather than insufficient evidence about the candidate itself. A future annotation transfer from human paralaminar snRNA-seq data may reveal a partial transcriptomic signature landing on CS20230722_SUPT_0005 or a related EP-CLA type, which could upgrade to LOW confidence with a closeMatch predicate.
  caveats:
    - caveat_type: CROSS_SPECIES_EXTRAPOLATION
      description: Paralaminar immature neurons are a primate-enriched type with no established mouse homolog. WMBv1 is derived from adult mouse brain. This mapping has no biological support and records only the closest type by regional/NT filter in the absence of a true homolog.
    - caveat_type: OTHER
      description: Classical defining markers (DCX, VIM, NES, MKI67, BCL2) are immaturity/progenitor-state markers absent from adult mouse transcriptomic atlases. No precomputed expression comparison is possible against WMBv1 cluster data.
  proposed_experiments:
    - Map human paralaminar nucleus snRNA-seq data (Sorrells et al. 2019 or Caglayan et al. 2023) to WMBv1 using cell type assignment tools to determine whether any mouse atlas type captures a partial transcriptomic signature; would add AnnotationTransferEvidence to this edge.
    - Perform targeted fluorescence labeling for DCX, BCL2, and NES in adult mouse amygdala to formally confirm absence of a paralaminar-equivalent population in rodent; would add LiteratureEvidence with REFUTE support formalising the species barrier.
    - Re-run find-candidates restricted to MBA:942 (endopiriform nucleus) to assess whether a closer WMBv1 candidate exists at either rank 0 or rank 1.
  unresolved_questions:
    - Does any cross-species scRNA-seq dataset contain a mouse cluster partially matching the DCX+/BCL2+/PROX1+ paralaminar population?
    - Would targeted re-analysis of WMBv1 in endopiriform nucleus (MBA:942) reveal a closer candidate?
    - Should this population be submitted as a new CL term distinct from CL:4042028 (immature neuron)?
```
<!-- verdict-block-end -->
