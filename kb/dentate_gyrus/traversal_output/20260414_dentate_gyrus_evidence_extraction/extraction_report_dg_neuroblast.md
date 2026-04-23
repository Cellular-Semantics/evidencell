# Extraction report: dg_neuroblast

- Node: **dg_neuroblast**
- Node context: proliferating DCX+/Ki67+/PSA-NCAM+ neuroblast in SGZ of dentate gyrus; NeuN−, calbindin−; Tbr2+ at type-2b → type-3; glutamatergic fate, pre-synaptic. Key gaps: **electrophysiology_class**, **neuropeptides**.
- Summaries source: `/Users/ar38/Documents/GitHub/evidencell/kb/dentate_gyrus/traversal_output/20260414_dentate_gyrus_cite_traverse/all_summaries.json`
- Extraction date: 2026-04-23

## Summary

| Metric | Count |
|---|---|
| Summaries in source file | 26 |
| Excluded by corpus-ID filter | 5 |
| Processed entries | 21 |
| Entries skipped (not relevant to dg_neuroblast) | 10 |
| Evidence items proposed | 11 |

### Breakdown by evidence type

| Evidence type | Count |
|---|---|
| LiteratureEvidence (LITERATURE) | 11 |
| ElectrophysiologyEvidence | 0 |
| MorphologyEvidence | 0 |
| MarkerAnalysisEvidence | 0 |
| SpatialColocationEvidence | 0 |

### Breakdown by support value

| Support | Count |
|---|---|
| SUPPORT | 7 |
| PARTIAL | 4 |
| REFUTE | 0 |

### Target-field coverage

| Field | # items |
|---|---|
| defining_markers | 6 |
| electrophysiology_class | 3 |
| anatomical_location | 1 |
| nt_type | 1 |
| negative_markers | 0 |
| morphology_notes | 0 |
| colocated_types | 0 |
| neuropeptides (gap) | 0 |

## Proposed evidence items

| # | Target field | Reference | Source method | Support | Notes |
|---|---|---|---|---|---|
| 1 | defining_markers | CorpusId:279046466 | asta_report | SUPPORT | type-2a/2b/type-3 neuroblast marker cascade; pending primary verification |
| 2 | defining_markers | CorpusId:7393550 | asta_report | PARTIAL | Tis21+/DCX co-expression in neuroblasts; pending primary verification |
| 3 | defining_markers | CorpusId:15727849 | asta_report | SUPPORT | Tbr2+/DCX-low type-2 IPCs in SGZ; pending primary verification |
| 4 | defining_markers | CorpusId:245432259 | asta_report | SUPPORT | neuroblast DCX+/Ki67+ definition; pending primary verification |
| 5 | electrophysiology_class | CorpusId:258927570 | asta_report | PARTIAL | states intrinsic electrical properties develop alongside morphology; indirect; pending primary verification |
| 6 | defining_markers | CorpusId:14598082 | asta_report | SUPPORT | DCX almost exclusively on immature newborn DG/SVZ neurons; pending primary verification |
| 7 | defining_markers | CorpusId:8479504 | asta_report | PARTIAL | GFAP-/Nestin+/DCX+ (C-type) progenitor description; SVZ-framed but relevant; pending primary verification |
| 8 | electrophysiology_class | PMID:16341203 | europepmc_fulltext | SUPPORT | newborn DG DCX+ cells express high NKCC1, little KCC2 (Ge 2006) |
| 9 | electrophysiology_class | PMID:16157276 | abstract_only | SUPPORT | type-2 progenitors receive direct GABAergic neural inputs (Tozuka 2005) |
| 10 | anatomical_location | CorpusId:14221248 | asta_report | SUPPORT | SGZ neurogenesis stage description; pending primary verification |
| 11 | nt_type | CorpusId:252063749 | asta_report | PARTIAL | DG granule-cell lineage migration context (nt_type inferred); pending primary verification |

## asta_report items pending primary verification

The following 9 items are derived from ASTA discovery-report summaries (not yet verified against primary fulltext). They are marked in the proposed YAML with `# asta_report -- pending primary verification`.

- Evidence 1 — CorpusId:279046466 (defining_markers)
- Evidence 2 — CorpusId:7393550 (defining_markers)
- Evidence 3 — CorpusId:15727849 (defining_markers)
- Evidence 4 — CorpusId:245432259 (defining_markers)
- Evidence 5 — CorpusId:258927570 (electrophysiology_class)
- Evidence 6 — CorpusId:14598082 (defining_markers)
- Evidence 7 — CorpusId:8479504 (defining_markers)
- Evidence 10 — CorpusId:14221248 (anatomical_location)
- Evidence 11 — CorpusId:252063749 (nt_type)

## Summaries excluded by corpus-ID filter

| CorpusId | Title | Reason |
|---|---|---|
| 13752593 | Protective Effect of Antioxidants on Neuronal Dysfunction and Plasticity in Huntington's Disease | excluded (EXCLUDED CORPUS IDS) |
| 148569364 | Ameliorating effect of postweaning exposure to antioxidant on disruption of hippocampal neurogenesis induced by developmental hypothyroidism in rats. | excluded (EXCLUDED CORPUS IDS) |
| 7440369 | Prenatal genesis of layer II doublecortin expressing neurons in neonatal and young adult guinea pig cerebral cortex | excluded (EXCLUDED CORPUS IDS) |
| 625292 | Commentary: Posttraining ablation of adult-generated olfactory granule cells degrades odor-reward memories | excluded (EXCLUDED CORPUS IDS) |
| 233432690 | Widespread Doublecortin Expression in the Cerebral Cortex of the Octodon degus | excluded (EXCLUDED CORPUS IDS) |

## Summaries skipped (not relevant to dg_neuroblast)

These entries were relevant to other DG nodes (dg_immature_granule_neuron, dg_mature_granule_neuron) but not to dg_neuroblast (which is pre-synaptic, NeuN-negative, and proliferative). The per-summary "single most informative quote" for dg_neuroblast would not apply, so no item is proposed from these:

| CorpusId | Section | Relevance | Reason skipped for dg_neuroblast |
|---|---|---|---|
| 18166210 | Results (Zhao 2006) | HIGH | Morphological stages A–D of post-mitotic granule neuron maturation; targets dg_immature_granule_neuron morphology, not neuroblast. |
| 18166210 | Results — dendritic arborization | HIGH | Dendritic timeline of post-mitotic adult-born GCs; targets dg_immature_granule_neuron. |
| 4332735 | Abstract (Schmidt-Hieber 2004) | HIGH | Young *granule cells* ephys (T-type Ca2+, LTP threshold); post-mitotic dg_immature_granule_neuron, not neuroblast. |
| 38501311 | Results (Espósito 2005) | HIGH | Patch-clamp of post-mitotic newborn DGCs (silent → GABA → glu); targets dg_immature_granule_neuron ephys. |
| 38501311 | Results — GABA synaptic properties | HIGH | Synaptic GABA component dissection in post-mitotic newborn DGCs. |
| 4403779 | Results (van Praag 2002) | HIGH | Action potentials & synaptic inputs in 4–8-week-old newborn GCs; post-mitotic. |
| 18166210 | Discussion | MODERATE | Functional context for morphological stages in post-mitotic GCs. |
| 235300723 | Discussion (PSA depletion / piriform) | MODERATE | Piriform cortex immature neurons, not DG neuroblast. |
| 13799502 | Results (piriform plasticity) | MODERATE | Piriform cortex immature neurons; CaMKII glutamatergic switch not directly applicable to DG neuroblast. |
| 15994456 | Results (neocortex/striatum interneurons) | MODERATE | CR→CB switch is specifically described for post-mitotic DG granule neurons (not neuroblast). |

## Node fields with no evidence proposed (gaps)

- **neuropeptides** — no summary contained any neuropeptide data for the neuroblast stage (explicit gap, consistent with node context).
- **negative_markers** — no verbatim quote in the retrieved summaries explicitly attributes NeuN−/calbindin− status to the *neuroblast* (type-3/DCX+/Ki67+) stage; the clearest NeuN− DCX+ quote in the corpus (CorpusId:233432690, Groen 2021) is in the EXCLUDED set.
- **morphology_notes** — the morphology-focused summaries in this corpus (Zhao 2006) address post-mitotic granule neurons, not the pre-synaptic neuroblast stage.
- **colocated_types** — no spatial/MERFISH data in this corpus.
- **electrophysiology_class (primary, neuroblast-specific)** — only Tozuka 2005 (PMID:16157276) provides direct ephys data on *type-2 neuronal progenitor cells* (closest to neuroblast stage); Ge 2006 (PMID:16341203) characterises NKCC1/KCC2 in DCX+ newborn DGCs which spans the neuroblast → immature-neuron transition. Gap is partially addressed but remains an area where more specifically type-3/DCX+/Ki67+ recordings would be useful.

## Return statement source

Proposed 11 evidence items for dg_neuroblast. Fields covered: defining_markers, electrophysiology_class, anatomical_location, nt_type. Gaps: neuropeptides, negative_markers, morphology_notes, colocated_types. asta_report items needing verification: 9.
