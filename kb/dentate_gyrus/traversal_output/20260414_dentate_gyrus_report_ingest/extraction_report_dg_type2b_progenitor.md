# Evidence Extraction Report — dg_type2b_progenitor

- **Node:** `dg_type2b_progenitor` (Dentate Gyrus Type-2b Neural Progenitor, CL:9900004)
- **KB file:** `kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`
- **Summaries file:** `kb/dentate_gyrus/traversal_output/20260414_dentate_gyrus_report_ingest/all_summaries.json`
- **Proposed evidence file:** `proposed_evidence_dg_type2b_progenitor.yaml`
- **Extraction date:** 2026-04-22
- **Excluded corpus IDs:** 14221248, 252063749, 7440369, 13752593

---

## Node context recap

- **Markers:** Nestin+, DCX+ (low), Eomes/Tbr2+
- **Negative markers:** NeuN-, Calbindin-
- **Location:** subgranular zone (SGZ) of the dentate gyrus (UBERON:0009952)
- **NT type:** glutamatergic (lineage-committed)
- **Morphology:** co-expresses Nestin and DCX at low levels; short tangential processes; 64% of Tbr2+ cells co-label with DCX; clusters in SGZ near type-1 radial processes
- **Atlas correlate:** cluster 0511 (Eomes+/Sox6+)
- **Primary source:** Hodge 2008 (CorpusId:15727849, PMID:18385329)

---

## Summary

**Items proposed:** 12

### Breakdown by target field

| Target field        | Count |
|---------------------|-------|
| defining_markers    | 6     |
| negative_markers    | 2     |
| nt_type             | 3     |
| morphology_notes    | 1     |

### Breakdown by support value

| Support  | Count |
|----------|-------|
| SUPPORT  | 4     |
| PARTIAL  | 8     |
| REFUTE   | 0     |

### Breakdown by evidence type

| Evidence type       | Count |
|---------------------|-------|
| LiteratureEvidence  | 12    |

All proposed items are `LiteratureEvidence`. No quantitative marker-overlap data for `MarkerAnalysisEvidence` was present in the retained summaries for this node beyond what is already captured in the Hodge 2008 text (96.76% Nestin/Tbr2 co-label; 64.4% Tbr2/DCX co-label — embedded in the literature snippet).

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

| CorpusId    | Title                                                                                                                          | Relevance | Reason                                                                 |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------|
| 625292      | Commentary: Posttraining ablation of adult-generated olfactory granule cells degrades odor-reward memories (Vangeneugden 2015) | LOW       | OB granule cells (GABAergic); no content relevant to type-2b progenitor |
| 148569364   | Ameliorating effect of postweaning exposure to antioxidant ... hypothyroidism in rats (Tanaka 2019)                            | LOW       | no quotes available (no PMC fulltext)                                  |

---

## Items proposed (mapped to source summaries)

| # | CorpusId    | Reference                          | Field              | Support | Relevance |
|---|-------------|------------------------------------|--------------------|---------|-----------|
| 1 | 15727849    | PMID:18385329 (Hodge 2008)         | defining_markers   | SUPPORT | HIGH      |
| 2 | 15727849    | PMID:18385329 (Hodge 2008)         | morphology_notes   | SUPPORT | HIGH      |
| 3 | 279046466   | PMID:40519263 (Micheli 2025)       | defining_markers   | SUPPORT | HIGH      |
| 4 | 245432259   | PMID:37082558 (Stepien 2021)       | defining_markers   | SUPPORT | HIGH      |
| 5 | 7393550     | PMID:19482889 (Attardo 2009)       | defining_markers   | PARTIAL | HIGH      |
| 6 | 8479504     | PMID:26056581 (Stoll 2014)         | defining_markers   | PARTIAL | HIGH      |
| 7 | 258927570   | PMID:37488837 (Hussain 2023)       | nt_type            | PARTIAL | HIGH      |
| 8 | 14598082    | PMID:23667508 (Merz 2013)          | negative_markers   | PARTIAL | HIGH      |
| 9 | 233432690   | PMID:33994960 (Groen 2021)         | negative_markers   | PARTIAL | MODERATE  |
| 10| 235300723   | PMID:34072166 (Coviello 2021)      | defining_markers   | PARTIAL | MODERATE  |
| 11| 13799502    | PMID:29688272 (Rotheneichner 2018) | nt_type            | PARTIAL | MODERATE  |
| 12| 15994456    | PMID:15684031 (Dayer 2005)         | nt_type            | PARTIAL | MODERATE  |

### Note on duplicate source

Hodge 2008 (CorpusId:15727849) contributes two items (items 1 and 2). This is a deliberate
exception to the one-item-per-summary guideline: Hodge is the primary Tbr2/type-2 progenitor
source and uniquely carries both (a) defining-marker content (Tbr2+/DCX-low co-labeling)
and (b) morphology_notes content (SGZ clustering in close association with Tbr2-negative
type-1 nestin+ cells). No other non-excluded summary covers morphology_notes for this node.
Reviewer may consolidate to a single item if desired.

---

## Node fields: coverage and gaps

| Node field               | Evidence proposed? | Notes                                                                                             |
|--------------------------|--------------------|---------------------------------------------------------------------------------------------------|
| defining_markers         | YES (6 items)      | Tbr2/Eomes, Nestin, DCX-low, PSA-NCAM, Tis21 covered; Hodge 2008 is the anchor                    |
| negative_markers         | YES (2 items)      | NeuN-negative (DCX-defined immature) via Merz 2013 / Groen 2021 context; Calbindin- not directly attested |
| anatomical_location      | NO                 | SGZ location embedded in multiple item snippets but no dedicated quote selected                   |
| morphology_notes         | YES (1 item)       | Hodge 2008: clusters in SGZ, close association with Tbr2-negative type-1 nestin+ cells             |
| nt_type                  | YES (3 items)      | Glutamatergic lineage commitment — indirect (CR->CB switch, CaMKII acquisition, RGL->IPC->granule trajectory); no direct type-2b glutamatergic attestation |
| electrophysiology_class  | NO                 | Not in node context; no quote selected                                                            |
| colocated_types          | NO                 | Not addressed by retained summaries                                                               |
| atlas_correlate          | NO                 | Atlas cluster 0511 (Eomes+/Sox6+) is an integration correlate; not addressed by literature summaries |

### Explicit gaps (no evidence found)

- **anatomical_location** — SGZ mentioned incidentally in marker and morphology items, but no
  dedicated evidence item proposed (best-selected quotes instead carried marker/morphology content).
- **negative_markers (Calbindin-)** — Calbindin- status is implied by type-2b being pre-granule
  but is not directly attested in any retained summary.
- **nt_type (direct attestation)** — All three nt_type items are PARTIAL/indirect:
  - Hussain 2023: generic RGL->IPC->granule trajectory
  - Rotheneichner 2018: CaMKII acquisition in piriform cortex (not DG)
  - Dayer 2005: cross-regional CR->CB switch analogy
  No retained summary directly states that type-2b progenitors in DG are glutamatergic/lineage-committed.
- **colocated_types** — not addressed by any retained summary.
- **atlas_correlate** — no literature evidence linking type-2b to the MERFISH 0511 cluster;
  this is an atlas-integration attestation out of scope for literature extraction.

### Primary source coverage

Hodge 2008 (CorpusId:15727849 / PMID:18385329) is the primary literature source for this
node. Both of its most informative quotes (Tbr2/DCX co-labeling; Tbr2/nestin SGZ clustering)
have been captured. The 96.76% Nestin-GFP/Tbr2 co-labeling statistic is embedded in the
item 2 snippet (verbatim). No Hodge quotes were discarded.

### asta_report items

No summary entries carried `source_method: "asta_report"`; all retained entries were
`europepmc_fulltext`. No items need the "asta_report — pending primary verification"
annotation.
