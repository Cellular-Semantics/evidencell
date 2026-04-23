# Evidence Extraction Report — dg_neuroblast

- **Node:** `dg_neuroblast` (Dentate Gyrus Neuroblast / Type-3 Progenitor)
- **KB file:** `kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`
- **Summaries file:** `kb/dentate_gyrus/traversal_output/20260414_dentate_gyrus_report_ingest/all_summaries.json`
- **Extraction date:** 2026-04-22
- **Excluded corpus IDs:** 14221248, 252063749, 7440369, 13752593

---

## Summary

**Items proposed:** 11

### Breakdown by target field

| Target field            | Count |
|-------------------------|-------|
| defining_markers        | 6     |
| electrophysiology_class | 3     |
| negative_markers        | 1     |
| nt_type                 | 1     |

### Breakdown by support value

| Support  | Count |
|----------|-------|
| SUPPORT  | 5     |
| PARTIAL  | 6     |
| REFUTE   | 0     |

### Breakdown by evidence type

| Evidence type       | Count |
|---------------------|-------|
| LiteratureEvidence  | 11    |

All proposed items are `LiteratureEvidence`. No quantitative marker-overlap data (for `MarkerAnalysisEvidence`) was present in the retained summaries for this node.

---

## Items skipped

### Excluded via EXCLUDED CORPUS IDS

| CorpusId    | Title                                                                                                      | Relevance | Reason                                      |
|-------------|------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------|
| 14221248    | Mimicking Neural Stem Cell Niche by Biocompatible Substrates (Regalado-Santiago 2016)                      | MODERATE  | on EXCLUDED list                            |
| 252063749   | Postnatal and Adult Neurogenesis in Mammals, Including Marsupials (Bartkowska 2022)                        | MODERATE  | on EXCLUDED list                            |
| 7440369     | Prenatal genesis of layer II doublecortin expressing neurons ... guinea pig cerebral cortex (Yang 2015)    | LOW       | on EXCLUDED list                            |
| 13752593    | Protective Effect of Antioxidants ... Huntington's Disease (Velusamy 2017)                                 | LOW       | on EXCLUDED list                            |

### Skipped for other reasons

| CorpusId    | Title                                                                                                                          | Relevance | Reason                                  |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------|
| 625292      | Commentary: Posttraining ablation of adult-generated olfactory granule cells degrades odor-reward memories (Vangeneugden 2015) | LOW       | OB granule cells (GABAergic), not DG    |
| 148569364   | Ameliorating effect of postweaning exposure to antioxidant ... hypothyroidism in rats. (Tanaka 2019)                           | LOW       | no quotes available (no PMC fulltext)   |

---

## Items proposed (mapped to source summaries)

| # | CorpusId    | Reference                       | Field                    | Support | Relevance |
|---|-------------|---------------------------------|--------------------------|---------|-----------|
| 1 | 279046466   | PMID:40519263 (Micheli 2025)    | defining_markers         | SUPPORT | HIGH      |
| 2 | 7393550     | PMID:19482889 (Attardo 2009)    | defining_markers         | PARTIAL | HIGH      |
| 3 | 15727849    | PMID:18385329 (Hodge 2008)      | defining_markers         | SUPPORT | HIGH      |
| 4 | 245432259   | PMID:37082558 (Stepien 2021)    | defining_markers         | SUPPORT | HIGH      |
| 5 | 258927570   | PMID:37488837 (Hussain 2023)    | electrophysiology_class  | PARTIAL | HIGH      |
| 6 | 14598082    | PMID:23667508 (Merz 2013)       | defining_markers         | SUPPORT | HIGH      |
| 7 | 8479504     | PMID:26056581 (Stoll 2014)      | electrophysiology_class  | PARTIAL | HIGH      |
| 8 | 235300723   | PMID:34072166 (Coviello 2021)   | defining_markers         | PARTIAL | MODERATE  |
| 9 | 13799502    | PMID:29688272 (Rotheneichner 2018) | electrophysiology_class | PARTIAL | MODERATE  |
| 10| 233432690   | PMID:33994960 (Groen 2021)      | negative_markers         | SUPPORT | MODERATE  |
| 11| 15994456    | PMID:15684031 (Dayer 2005)      | nt_type                  | PARTIAL | MODERATE  |

---

## Node fields: coverage and gaps

| Node field               | Evidence proposed? | Notes                                                                 |
|--------------------------|-------------------|-----------------------------------------------------------------------|
| defining_markers         | YES (6 items)     | DCX, Ki67, PSA-NCAM, Nestin (type-2b), Tbr2, Tis21 signals covered     |
| negative_markers         | YES (1 item)      | NeuN-negative status for DCX+ DG cells (Groen 2021)                    |
| anatomical_location      | NO                | SGZ location stated in multiple quotes but none selected as primary    |
| nt_type                  | YES (1 item)      | Indirect (cross-region CR→CB switch analogy, Dayer 2005)               |
| electrophysiology_class  | YES (3 items)     | All PARTIAL — general/indirect claims about immature neuron excitability and concurrent ephys maturation |
| morphology_notes         | NO                | No quote selected primarily for morphology in retained (non-excluded) summaries |
| colocated_types          | NO                | Not addressed by the retained literature summaries                     |

### Explicit gaps (no evidence found)

- **anatomical_location** — no dedicated evidence item proposed (best-selected quotes instead carried marker content)
- **morphology_notes** — no primary evidence item proposed from the retained, non-excluded summaries
- **colocated_types** — not addressed by any retained summary

### Notes on electrophysiology

All three `electrophysiology_class` items are PARTIAL:
- Hussain 2023 (review statement on concurrent ephys/morph maturation)
- Stoll 2014 (general "immature neurons are highly excitable" claim)
- Rotheneichner 2018 (piriform cortex, not DG, citing Klempin 2011)

No primary DG-specific electrophysiology quote was present among the retained summaries; the DG neuroblast ephys GAP noted in the node context remains open.

### asta_report items

No summary entries carried `source_method: "asta_report"`; all retained entries were `europepmc_fulltext`. No items need the "asta_report — pending primary verification" annotation.
