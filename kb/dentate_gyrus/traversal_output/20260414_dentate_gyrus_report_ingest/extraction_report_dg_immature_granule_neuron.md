# Extraction Report: dg_immature_granule_neuron

**Node:** dg_immature_granule_neuron (Dentate Gyrus Immature Granule Neuron)
**KB file:** `kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`
**Summaries file:** `kb/dentate_gyrus/traversal_output/20260414_dentate_gyrus_report_ingest/all_summaries.json`
**Extraction date:** 2026-04-22
**Proposed evidence file:** `proposed_evidence_dg_immature_granule_neuron.yaml`

## Node context recap

- Defining markers: DCX+, NeuN+, PSA-NCAM+, Tis21+
- Negative markers: Calbindin−
- Location: inner granule cell layer (GCL) of the dentate gyrus
- NT type: glutamatergic
- Morphology: postmitotic stage-5; axons reach CA3 by day 10–11; first spines at 15–16 days; peak spine growth 3–4 weeks
- Proposed CL: CL:9900002

## Corpus handling

**Input summaries:** 17 entries
**Excluded by caller:** 4 corpus IDs — 14221248 (Regalado-Santiago 2016), 252063749 (Bartkowska 2022), 7440369 (Yang 2015), 13752593 (Velusamy 2017)
**Skipped (no quotes):** 1 — CorpusId:148569364 (Tanaka 2019; no PMC fulltext, empty quotes list)
**Processed:** 12 entries → 12 proposed evidence items (1 per summary)

## Proposed items by target field

| # | Ref | Target field | Support | Summary |
|---|-----|--------------|---------|---------|
| 1 | PMID:40519263 (Micheli 2025) | defining_markers | SUPPORT | Stage-5 = DCX+/NeuN+ postmitotic immature granule neuron definition |
| 2 | PMID:19482889 (Attardo 2009) | defining_markers | SUPPORT | Tis21 expressed in postmitotic DG neurons (adult, unlike fetal) |
| 3 | PMID:18385329 (Hodge 2008) | defining_markers | PARTIAL | Tbr1 marks postmitotic granule cells (transcription factor, not in node context) |
| 4 | PMID:37082558 (Stepien 2021) | defining_markers | SUPPORT | Immature DG neurons express DCX + PSA-NCAM + NeuN |
| 5 | PMID:37488837 (Hussain 2023) | electrophysiology_class | PARTIAL | Intrinsic electrical properties develop concurrently with synapses & morphology |
| 6 | PMID:23667508 (Merz 2013) | defining_markers | SUPPORT | DCX almost exclusively marks immature newborn DG/SVZ neurons |
| 7 | PMID:26056581 (Stoll 2014) | electrophysiology_class | SUPPORT | Immature neurons are highly excitable, affect network dynamics |
| 8 | PMID:34072166 (Coviello 2021) | electrophysiology_class | PARTIAL | AIS presence → repetitive AP firing; absent in immature precursors (PCX data, applied cross-region) |
| 9 | PMID:29688272 (Rotheneichner 2018) | morphology_notes | PARTIAL | Low-DCX + complex morphology → electrophysiology consistent with maturing neurons (PCX data) |
| 10 | PMID:33994960 (Groen 2021) | negative_markers | PARTIAL | DCX-labeled DG neurons are NeuN-negative AND calretinin-negative (Octodon degus) |
| 11 | PMID:15684031 (Dayer 2005) | negative_markers | SUPPORT | Adult-born DG granule neurons switch CR → CB during maturation |
| 12 | DOI:10.3389/fnins.2015.00110 (Vangeneugden 2015) | morphology_notes | PARTIAL | 10 dpi "immature" vs 21 dpi "integrated" distinction (OB context) |

## Fields covered

- **defining_markers:** items 1, 2, 3, 4, 6 (strong support for DCX/NeuN/PSA-NCAM/Tis21 panel)
- **electrophysiology_class:** items 5, 7, 8 (partial support; no DG-specific patch-clamp data)
- **morphology_notes:** items 9, 12 (indirect; no direct support for 15–16 day spine onset, CA3 axon timing)
- **negative_markers:** items 10, 11 (support for Calbindin− via CR→CB switch, and NeuN−/calretinin− in DCX+ DG cells)

## Gaps

- **anatomical_location (inner GCL):** no item extracted — most explicit statements (Regalado-Santiago, Velusamy) are in the excluded corpus. Gap: inner GCL location not independently supported from the non-excluded summaries beyond the DCX+/SGZ descriptions.
- **nt_type (glutamatergic):** no item extracted — the most direct glutamatergic statement (Bartkowska 2022, "Granule cells in the DG are glutaminergic") was in the excluded corpus. Rotheneichner (item 9 candidate on CaMKII) refers to piriform cortex, not DG.
- **morphology_notes specifics:** no evidence retrieved for the specific timing claims in the node context (axons reach CA3 by day 10–11; first spines at 15–16 days; peak spine growth 3–4 weeks). Items 9 and 12 are only indirect maturation timing proxies.
- **Node 10 (PSA-NCAM+):** supported only through marker-cascade mentions (items 4, 8 indirectly via Coviello PCX context). No dedicated PSA-NCAM+ DG quote survived the HIGH-relevance filter.
- **Tis21 beyond Attardo:** only item 2 supports Tis21 expression; replication would strengthen.
- **No MarkerAnalysisEvidence items** proposed — none of the summaries report quantitative marker-overlap metrics (dataset accession + overlap_value) in the retrieved quotes.

## Reviewer notes

- Items 3 (Hodge Tbr1), 9 (Rotheneichner piriform), 12 (Vangeneugden OB) are cross-region or auxiliary-marker inferences — flag for expert decision on whether to keep, downgrade, or drop.
- Item 10 (Groen Octodon degus) is cross-species but directly targets DG; PARTIAL is appropriate.
- Item 11 (Dayer) is the strongest negative_markers evidence (CR → CB switch in adult-born DG granule neurons); recommended for inclusion.
