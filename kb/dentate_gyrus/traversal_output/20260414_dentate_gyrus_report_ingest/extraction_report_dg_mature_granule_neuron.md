# Evidence Extraction Report — dg_mature_granule_neuron

**Extraction date:** 2026-04-22
**Node:** dg_mature_granule_neuron (Dentate Gyrus Mature Granule Neuron, stage-6)
**CL mapping:** CL:2000089 (EXACT)
**Source summaries:** `kb/dentate_gyrus/traversal_output/20260414_dentate_gyrus_report_ingest/all_summaries.json`
**Output file:** `proposed_evidence_dg_mature_granule_neuron.yaml`

## Node context recap

- Markers: Calbindin+, NeuN+, Tbr1+
- Negative markers: DCX−, Nestin−, PSA-NCAM−
- Location: granule cell layer (GCL) of the dentate gyrus
- NT type: glutamatergic
- Morphology: terminally differentiated; fully elaborated dendritic arbor; mossy fiber projections to CA3

## Exclusions

Excluded corpus IDs (from task directive):
- `14221248` — Mimicking Neural Stem Cell Niche by Biocompatible Substrates
- `252063749` — Postnatal and Adult Neurogenesis in Mammals, Including Marsupials
- `7440369` — Prenatal genesis of layer II DCX neurons in guinea pig cortex
- `13752593` — Protective Effect of Antioxidants on Neuronal Dysfunction in HD

The `148569364` entry (Tanaka 2019 — no PMC fulltext, empty quotes) was not extracted because it contains no retrievable quotes.

## Summary of proposed evidence

**12 evidence items proposed** (one per eligible summary, max 1 per entry as specified).

| # | CorpusId | Reference | Target field | Support | Relevance |
|---|---|---|---|---|---|
| 1 | 279046466 | PMID:40519263 | defining_markers | SUPPORT | HIGH |
| 2 | 7393550  | PMID:19482889 | defining_markers | SUPPORT | HIGH |
| 3 | 15727849 | PMID:18385329 | defining_markers (Tbr1) | SUPPORT | HIGH |
| 4 | 245432259 | PMID:37082558 | defining_markers (NeuN) | PARTIAL | HIGH |
| 5 | 258927570 | PMID:37488837 | electrophysiology_class | SUPPORT | HIGH |
| 6 | 14598082 | PMID:23667508 | negative_markers (DCX) | SUPPORT | HIGH |
| 7 | 8479504 | PMID:26056581 | electrophysiology_class | PARTIAL | HIGH |
| 8 | 235300723 | PMID:34072166 | electrophysiology_class (AIS firing) | PARTIAL | MODERATE |
| 9 | 13799502 | PMID:29688272 | nt_type (CaMKII glutamatergic) | PARTIAL | MODERATE |
| 10 | 233432690 | PMID:33994960 | negative_markers (DCX neg → mature = NeuN+) | SUPPORT | MODERATE |
| 11 | 15994456 | PMID:15684031 | defining_markers (CR→CB switch) | SUPPORT | MODERATE |
| 12 | 625292 | DOI:10.3389/fnins.2015.00110 | electrophysiology_class (integration at 21d) | PARTIAL | LOW |

## Fields covered

- `defining_markers` — 5 items (Calbindin, NeuN, Tbr1 coverage)
- `negative_markers` — 2 items (DCX − confirmation)
- `electrophysiology_class` — 4 items (concurrent maturation, excitability contrast, AIS+repetitive firing, integration timing)
- `nt_type` — 1 item (CaMKII glutamatergic, piriform analogue)

## Gaps

- **anatomical_location (GCL):** no summary quote explicitly anchors a mature GCL statement beyond excluded reviews (14221248, 13752593) — gap remains.
- **morphology_notes (mossy fiber projections to CA3):** no non-excluded quote explicitly describes mature GCN mossy fiber projection to CA3. The excluded reviews contained this content.
- **colocated_types:** no direct evidence extracted.
- **Glutamatergic (DG-specific):** excluded corpus 252063749 was the only source asserting "Granule cells in the DG are glutaminergic"; non-DG CaMKII data (Rotheneichner) is only partial support. nt_type for mature DG granule cell remains weakly supported from this summary set.
- **Species specificity:** most quotes are from mouse or rodent/review context; primate/human mature GCN evidence not represented in this set.
- **Dedicated DG mature-neuron electrophysiology:** quotes 5, 7, 8, 12 address maturation trajectory and AIS-dependent firing but no quote presents intrinsic parameters of fully mature DG GCs directly.

## Notes

- Item 4 (Stepien 2021) is marked PARTIAL because the quote describes NeuN in immature neurons (DCX+/PSA-NCAM+/NeuN+), but NeuN is also a defining marker for mature (Calbindin+/NeuN+) stage-6; the quote indirectly supports NeuN presence but not Calbindin.
- Items 8, 9 (Coviello 2021, Rotheneichner 2018) are piriform-cortex data; included as supportive cross-regional analogues to fill electrophysiology_class and nt_type gaps.
- Item 11 (Dayer 2005) explicitly references the DG calretinin→calbindin developmental switch, directly supporting the DG mature-neuron Calbindin+ defining marker in a cross-regional comparison.
- Item 12 (Vangeneugden 2015) is from olfactory bulb (GABAergic, not DG); included with LOW relevance and PARTIAL support for the general principle that adult-born neurons require ~21 days for synaptic integration.
