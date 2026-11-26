## vLGN / LGv GABAergic nodes: survey + evidence-extraction trial (follow-up to #235)

This is a trial of `survey` → `evidence-extraction` on the 10 nodes from the vLGN ASTA report ingest (#235, merged). The Asta MCP server was unavailable, so snippets came from an interim direct-API script (see #250). The aim is to judge whether this enrichment path is worth running on other regions.

**Status: draft for review.** It deviates from the workflows (listed below), and several conflicts are left for a curator to settle.

### Method
- **Corpus:** the 26 papers cited by the ASTA report (`research/thalamus/20261125_thalamus_lgv_report_ingest/pdf_corpus_ids.json`).
- **Fetch:** `research/thalamus/survey_20261125/fetch_snippets.py` runs one Semantic Scholar `snippet/search` query per node, with `limit=1000` (`queries.json`). The API key is passed to curl on stdin, never in argv. All 719 snippets came back for every query, from 22 of the 26 papers, but in a different order per query. The script keeps the top 8 per paper (about 155 snippets per node) and writes them to `trimmed/`. The raw dumps (20 MB) are not committed and can be re-fetched.
- **Survey:** one sonnet subagent per node read only its trimmed file and wrote `summaries/{node}.json` in the survey.md LiteratureSummary shape. `prepare_extraction.py` then merged these to one entry per paper (`summaries_merged/`) and built `paper_catalogue.json` from the reference store.
- **Extraction:** one opus subagent per node, run sequentially because they share the quote store, using the evidence-extraction.md Step 2 contract plus the deviations below. Per-node manifests are in `extraction_manifest_*.json`.

### Deviations from the workflows
- **Fetch:** an interim script instead of `mcp__Asta_semanticscholar__snippet_search` (#250); per-node queries instead of one combined query; a per-paper cap of 8 instead of `limit=20` total.
- **D1:** summaries were *not* skipped when their paper was already cited on the node. Without this, most HIGH-relevance papers would have been dropped (see `skip_analysis.py`).
- **D2:** up to 3 sources per summary entry, each from a different quote and each adding a new fact.
- **D3:** additions only. Conflicts were recorded in the manifests, not edited.
- **D5:** synaptic-input data may go in `electrophysiology` only when labelled as synaptic.
- **D6:** the reuniens-projecting node could reuse the sibling nodes' Salay 2021 transmitter quotes.

### Results (`node_metrics.py`, before → after)
| node | sources | distinct refs | quote keys | markers w/ gene |
|---|---|---|---|---|
| lgv_igl_gabaergic_neuron | 31→47 | 10→16 | 15→31 | 2→2 |
| vlgn_gabaergic_neuron | 21→27 | 11→15 | 13→19 | 1→1 |
| vlgne_gabaergic_neuron | 12→16 | 6→6 | 9→13 | 0→0 |
| vlgni_gabaergic_neuron | 7→18 | 5→8 | 5→15 | 1→1 |
| vlgn_local_gabaergic_interneuron | 4→16 | 2→6 | 2→9 | 0→1 |
| vlgn_sc_projecting_gabaergic_neuron | 11→19 | 4→6 | 4→12 | 0→2 |
| lgv_igl_sox14_gabaergic_neuron | 21→24 | 1→1 | 7→10 | 2→2 |
| lgv_igl_lhb_projecting_gabaergic_neuron | 14→16 | 3→5 | 3→5 | 0→0 |
| lgv_igl_lpbn_projecting_gabaergic_neuron | 5→6 | 1→1 | 1→2 | 0→0 |
| lgv_igl_reuniens_projecting_neuron | 12→17 | 3→5 | 3→8 | 1→1 |
| **Total** | **138→206** | **46→69** | **62→124** | **7→10** |

Filled property fields went from 40 to 43.

**Substantive gains**
- **Reuniens-projecting transmitter:** Salay 2021 retrograde tracing found all vLGN→Re neurons Vgat+, and Gad2-Cre GABA axons in Re. GABAergic now has direct support.
- **`vlgn_local_gabaergic_interneuron`:**
  - New marker Gad1 (GAD67), with the caveat that it is not specific to interneurons.
  - New location, vLGNe only (the cells are absent from vLGNi).
  - Recruitment depends on retinal input.
  - It is no longer an obvious merge candidate.
- **`vlgn_sc_projecting_gabaergic_neuron`:**
  - Markers Slc32a1 (Vgat, ~90% of cells) and Gad2 (~65%).
  - Superficial superior colliculus as a target layer.
  - A population distinct from the Re-projecting one.
- **`vlgni_gabaergic_neuron`:** corticothalamic EPSCs in 10 of 21 neurons (synaptic, under D5); no retinal input; Re and SC targets marked WEAK.
- **`lgv_igl_gabaergic_neuron`:** new target, periaqueductal grey; tracing support added for its existing SC, pretectal and Re targets.

**Little gain**
- **LHb-, LPBN- and Sox14 nodes:** each rests on 1–2 papers. Huang 2019, Huang 2020, Ciftcioglu 2020 and Guido 2018 have **no snippets** in the API.

### For the reviewer (conflicts recorded, not edited)
1. **`lgv_igl_reuniens_projecting_neuron`:** the TRANSMITTER CAVEAT note and the Huang 2020 REFUTE source now sit beside direct GABAergic tracing support. Consider revising the caveat, and the generic CL:0000540 cl_mapping.
2. **`vlgn_gabaergic_neuron` / `lgv_igl_gabaergic_neuron`:** the same caveat makes the Re target WEAK, which now conflicts with the Vgat+ retrograde tracing.
3. **`lgv_igl_sox14_gabaergic_neuron`:**
   - SCN innervation: "few" fibres in one quote vs "dense" in another.
   - Sox14+ cells "also contribute to the prethalamic LGv", which conflicts with the node's pTH-R-only definition.
4. **`vlgne_gabaergic_neuron`:** the sublaminar markers (Pvalb, Penk, Ecel1, Spp1; Nxph1 possible) were left off the pooled node. They argue for vLGNe child nodes.
5. **`vlgni_gabaergic_neuron`:** synaptic EPSC data is in `electrophysiology`, which the ingest agents had deliberately avoided. Confirm the schema intent.
6. The stale notes on `lgv_igl_gabaergic_neuron` (from #235) are still there.

### Lessons for running elsewhere
- The skip-already-cited rule in evidence-extraction.md needs revisiting for post-ingest runs. About 40% of the new sources came from already-cited papers.
- Each node's trimmed file should be about 30k tokens. One survey agent could not read its 64k file in full.
- Survey agents often broke the one-entry-per-paper rule, so keep the merge step in code.
- Papers with no snippets (here 4 of 26) need a full-text fallback (Europe PMC) to be checked at all.

### Validation
- The pre-edit hook accepted every KB and reference-store write.
- `just validate-all`: **All 118 KB files valid.**

Related: #235 (ingest, merged), #250 (MCP config + direct-API snippet CLI).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
