# Evidence Extraction Report — dg_immature_granule_neuron

**Extraction date:** 2026-04-23
**Source summaries:** `/Users/ar38/Documents/GitHub/evidencell/kb/dentate_gyrus/traversal_output/20260414_dentate_gyrus_cite_traverse/all_summaries.json`
**Output file:** `proposed_evidence_dg_immature_granule_neuron.yaml`
**Excluded corpus IDs:** 13752593, 148569364, 7440369, 625292, 233432690

---

## Summary

**Total proposed items:** 21

### Breakdown by evidence type

| Evidence type | Count |
|---|---|
| LITERATURE | 21 |

### Breakdown by support value

| Support | Count |
|---|---|
| SUPPORT | 13 |
| PARTIAL | 8 |
| REFUTE | 0 |

### Breakdown by target node field

| Field | Count |
|---|---|
| defining_markers | 6 |
| electrophysiology_class | 10 |
| morphology_notes | 2 |
| nt_type | 1 |
| anatomical_location | 1 |
| other | 2 |

---

## Items proposed (by source)

| # | CorpusId | PMID | node_relevance | source_method | Target field | Support |
|---|---|---|---|---|---|---|
| 1 | 18166210 | — | HIGH | europepmc_fulltext | morphology_notes | SUPPORT |
| 2 | 18166210 | — | HIGH | europepmc_fulltext | morphology_notes | SUPPORT |
| 3 | 279046466 | — | HIGH | asta_report | defining_markers | SUPPORT |
| 4 | 7393550 | — | HIGH | asta_report | defining_markers | PARTIAL |
| 5 | 15727849 | — | HIGH | asta_report | other | PARTIAL |
| 6 | 245432259 | — | HIGH | asta_report | defining_markers | SUPPORT |
| 7 | 258927570 | — | HIGH | asta_report | electrophysiology_class | PARTIAL |
| 8 | 14598082 | — | HIGH | asta_report | defining_markers | SUPPORT |
| 9 | 8479504 | — | HIGH | asta_report | electrophysiology_class | PARTIAL |
| 10 | 4332735 | 15107864 | HIGH | abstract_only | electrophysiology_class | SUPPORT |
| 11 | 38501311 | 16267214 | HIGH | europepmc_fulltext | electrophysiology_class | SUPPORT |
| 12 | 38501311 | 16267214 | HIGH | europepmc_fulltext | electrophysiology_class | SUPPORT |
| 13 | 4378008 | 16341203 | HIGH | europepmc_fulltext | electrophysiology_class | SUPPORT |
| 14 | 3154810 | 16157276 | HIGH | abstract_only | electrophysiology_class | PARTIAL |
| 15 | 4403779 | 11875571 | HIGH | europepmc_fulltext | electrophysiology_class | SUPPORT |
| 16 | 18166210 | — | MODERATE | europepmc_fulltext | electrophysiology_class | SUPPORT |
| 17 | 235300723 | — | MODERATE | asta_report | electrophysiology_class | PARTIAL |
| 18 | 13799502 | — | MODERATE | asta_report | other | PARTIAL |
| 19 | 15994456 | — | MODERATE | asta_report | defining_markers | SUPPORT |
| 20 | 252063749 | — | MODERATE | asta_report | nt_type | SUPPORT |
| 21 | 14221248 | — | MODERATE | asta_report | anatomical_location | SUPPORT |

---

## asta_report items — PENDING PRIMARY VERIFICATION

The following proposed items are sourced from the discovery report (ASTA) and have not yet been verified against primary-literature fulltext. An expert / downstream orchestrator must verify these quotes against the original paper before KB commit.

| # | CorpusId | Title (truncated) | Target field |
|---|---|---|---|
| 3 | 279046466 | Survey of transcriptome analyses of hippocampal neurogenesis... | defining_markers |
| 4 | 7393550 | Tis21 Expression Marks Not Only Populations of Neurogenic Precursor Cells... | defining_markers |
| 5 | 15727849 | Intermediate Progenitors in Adult Hippocampal Neurogenesis: Tbr2... | other |
| 6 | 245432259 | Neurogenesis in neurodegenerative diseases in the adult human brain | defining_markers |
| 7 | 258927570 | Adult neurogenesis: a real hope or a delusion? | electrophysiology_class |
| 8 | 14598082 | Evidence that Doublecortin Is Dispensable... | defining_markers |
| 9 | 8479504 | Advances toward regenerative medicine in the central nervous system | electrophysiology_class |
| 17 | 235300723 | PSA Depletion Induces the Differentiation of Immature Neurons in the Piriform Cortex... | electrophysiology_class |
| 18 | 13799502 | Cellular Plasticity in the Adult Murine Piriform Cortex... | other |
| 19 | 15994456 | New GABAergic interneurons in the adult neocortex and striatum... | defining_markers |
| 20 | 252063749 | Postnatal and Adult Neurogenesis in Mammals, Including Marsupials | nt_type |
| 21 | 14221248 | Mimicking Neural Stem Cell Niche by Biocompatible Substrates | anatomical_location |

**Total asta_report items pending verification: 12**

---

## Items skipped

### Excluded corpus IDs (pre-specified exclusion list)

| CorpusId | Title (truncated) | Reason |
|---|---|---|
| 13752593 | Protective Effect of Antioxidants on Neuronal Dysfunction... (Huntington's) | On exclusion list |
| 148569364 | Ameliorating effect of postweaning exposure to antioxidant on disruption of hippocampal neurogenesis... | On exclusion list (and no fulltext retrievable) |
| 7440369 | Prenatal genesis of layer II doublecortin expressing neurons... guinea pig | On exclusion list |
| 625292 | Commentary: Posttraining ablation of adult-generated olfactory granule cells... | On exclusion list |
| 233432690 | Widespread Doublecortin Expression in the Cerebral Cortex of the Octodon degus | On exclusion list |

### Not skipped — LOW relevance but not excluded

None remaining. All LOW-relevance entries in the summaries file were on the exclusion list.

---

## Node fields with no evidence found

The following node context fields have **no proposed evidence items** from the current summaries set:

- **negative_markers** — no quote in the summaries directly addresses Calbindin-negative or other negative markers for the immature stage (closest indirect: item #3 contrasts stage 5 DCX+/NeuN+ with stage 6 Calbindin+/NeuN+, but this is inferred rather than an explicit negative-marker statement).
- **colocated_types** — no spatial colocation data in the summaries.
- **neuropeptides** — GAP confirmed. No summary quote mentions neuropeptide expression in immature granule neurons.

---

## Notes on evidence-type selection

All 21 items are typed as `LITERATURE` (LiteratureEvidence). None of the summaries provided the structured-field requirements (dataset_accession, etype_label, imaging_method, markers_examined, spatial_technology) that would justify the more-specific ElectrophysiologyEvidence, MorphologyEvidence, MarkerAnalysisEvidence, or SpatialColocationEvidence types. Several electrophysiology items (e.g. items 11, 12, 13, 15) contain rich quantitative ephys content and could be promoted to ElectrophysiologyEvidence during expert review if a dataset_accession and etype_label are assigned.
