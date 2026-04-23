# Extraction Report: dg_mature_granule_neuron

**Extraction date:** 2026-04-23
**Source summaries:** `/Users/ar38/Documents/GitHub/evidencell/kb/dentate_gyrus/traversal_output/20260414_dentate_gyrus_cite_traverse/all_summaries.json`
**Output YAML:** `proposed_evidence_dg_mature_granule_neuron.yaml`
**Node context:** Terminally differentiated calbindin+/NeuN+/Tbr1+ glutamatergic granule neuron in the dentate gyrus granule cell layer. DCX-, PSA-NCAM-, nestin-. Key gaps: electrophysiology_class (no primary data in original KB), neuropeptides (no data).

---

## Summary

**Total proposed items:** 15

### Breakdown by evidence type

| Evidence type | Count |
|---|---|
| LiteratureEvidence (LITERATURE) | 15 |
| ElectrophysiologyEvidence | 0 |
| MorphologyEvidence | 0 |
| MarkerAnalysisEvidence | 0 |
| SpatialColocationEvidence | 0 |

All items were coded as generic LITERATURE. No papers in the summary set report dataset-level ephys/morphology/marker-overlap with accessions appropriate to the dedicated evidence subclasses.

### Breakdown by support

| Support | Count |
|---|---|
| SUPPORT | 9 |
| PARTIAL | 6 |
| REFUTE | 0 |

### Breakdown by target field

| Target field | Count |
|---|---|
| defining_markers | 6 |
| electrophysiology_class | 5 |
| negative_markers | 1 |
| morphology_notes | 2 |
| nt_type | 1 |

---

## Items skipped

### Excluded by corpus-ID list (per `excluded_ids.json`)

| CorpusId | Reason |
|---|---|
| 13752593 | DISEASE_MODEL — Huntington's Disease antioxidants review; DG neurogenesis only background context |
| 148569364 | DISEASE_MODEL + EARLY_POSTNATAL — developmental hypothyroidism model; no full text; zero quotes |
| 7440369 | NON_MODEL_SPECIES + EARLY_POSTNATAL — neonatal guinea pig neocortex; not adult DG |
| 625292 | UNRELATED_REGION — olfactory bulb GABAergic granule cells; wrong region and NT type |
| 233432690 | NON_MODEL_SPECIES — Octodon degus; no mechanistic data |

### Low-relevance summaries processed but not used for this node

| CorpusId | Node_relevance | Reason not used for dg_mature_granule_neuron |
|---|---|---|
| 3154810 (Tozuka 2005, PMID:16157276) | HIGH | Focus is on type-2 progenitor GABAergic depolarisation; nothing directly about mature granule neurons. |
| 4378008 (Ge 2006, PMID:16341203) | HIGH | Entirely about newborn DGC integration (tonic GABA, NKCC1); no mature-stage claim suitable for this node. |
| 38501311 second entry (Esposito 2005, GABA synaptic properties) | HIGH | Already represented by item 9 (main Esposito entry) — rule: max 1 evidence item per summary entry, and the same paper covered by one. Skipped to avoid double-counting the source (different summary entry was considered but the first-quote snippet was more mature-stage relevant). |
| 235300723 (Coviello 2021) | MODERATE | PSA-NCAM depletion in piriform cortex; not DG. AIS/firing quote applies to piriform mature neurons, only PARTIAL applicability. Skipped to keep emphasis on DG-specific evidence. |
| 13799502 (Rotheneichner 2018) | MODERATE | CaMKII/glutamatergic maturation in piriform cortex, not DG; cross-region only, weaker than the DG-specific items kept. |

---

## Node fields with no evidence found

| Field | Status |
|---|---|
| neuropeptides | No evidence in summary set — persistent gap. No paper in the corpus reports neuropeptide expression in DG mature granule neurons. |
| colocated_types | No evidence in summary set — node characterisation does not require spatial colocation data; not addressed in any summary. |

## Node fields with only PARTIAL-quality evidence

| Field | Notes |
|---|---|
| electrophysiology_class | Best direct evidence is item 10 (van Praag 2002, PMID:11875571) and item 8 (Schmidt-Hieber 2004, PMID:15107864) — both SUPPORT, providing primary patch-clamp data contrasting newborn vs mature granule cells. Items 6, 9, 11 are PARTIAL (review or immature-stage focus). |
| morphology_notes | Items 12 and 15 are the only hits; both PARTIAL/SUPPORT and review-level. Dedicated MorphologyEvidence would require a paper reporting a reconstructed mature granule cell with explicit dataset accession — not present in the summary set. |

---

## asta_report items pending primary verification

These items are marked `asta_report — pending primary verification` in the YAML source comment and require cross-checking against the primary source before KB commit:

| Item # | CorpusId | Target field |
|---|---|---|
| 2 | 279046466 | defining_markers |
| 3 | 7393550 | defining_markers |
| 4 | 15727849 | defining_markers |
| 5 | 245432259 | defining_markers |
| 6 | 258927570 | electrophysiology_class |
| 7 | 14598082 | negative_markers |
| 11 | 8479504 | electrophysiology_class |
| 13 | 15994456 | defining_markers |
| 14 | 252063749 | nt_type |
| 15 | 14221248 | morphology_notes |

**Total asta_report items needing verification: 10**

Non-asta_report items (items 1, 8, 9, 10, 12) are from europepmc_fulltext or abstract_only sources and are considered primary-verified at the quote level.

---

## Coverage notes

- The dg_mature_granule_neuron node's electrophysiology_class gap is **partially filled** by items 8, 9, 10 (Schmidt-Hieber 2004, Esposito 2005, van Praag 2002). These provide primary patch-clamp evidence characterising mature DG granule cells as the reference state against which immature cells are compared (e.g. Cm ~99 pF, Vrest ~−74 mV, firing plateau ~140 Hz; membrane properties distinct from young cells). Recommend expert-curator review to confirm whether these comparative statements satisfy the node's ephys gap or whether a dedicated mature-GC-only primary paper is still needed.
- The neuropeptides field remains a **hard gap** — no evidence was located in this corpus. A targeted second-pass literature search would be needed.
- defining_markers has strong redundant support (6 items) for Calbindin, NeuN, Tbr1 from multiple independent sources — sufficient for KB commit once asta_report items are primary-verified.
