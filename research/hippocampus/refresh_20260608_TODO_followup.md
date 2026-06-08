# Hippocampus refresh 20260608 — follow-up TODO

PR head: `refresh_reports_20260608_hippocampus`

## Status at session limit (2026-06-08)

### Done
- **Refresh**: Stage A + Stage B emit + refresh-property-comparisons at ranks 0 and 1 for all 41 (graph, node) classical pairs.
- **Stale-location audit**: 6 stale entries — `olm_hippocampus` (4 legacy CLUS_0727/0785/0788/0789), `sst_nos1_subfamily_chamberland` (CLUS_0859), `hpc_glu_dopa_receptor_pyramidal_hippocampus` (SUPT_0069). See `research/hippocampus/refresh_20260608_stale_audit.md`.
- **Synth**: 41 reports regenerated end-to-end via gen-report Step 3 subagents (3 waves).
- **Step 4b corrections — wave 1 (16 of 31 originally failing nodes)**: applied; resulting in 14 of those nodes now Step 4b-clean and **already written back** to the KB graph (137 verdict blocks total).
- **Hit Anthropic session limit during Step 4b corrections — wave 2 (15 nodes)**; only 1 of 15 wave-2 dispatches returned (and it described rather than edited).

### Still failing Step 4b (need follow-up corrections in next session)
| Node | Errors | Notes |
|---|---|---|
| `trilaminar_cell_hippocampus` | 3 | residual patch-seq/morphology modality literals |
| `lth_cell_hippocampus` | 6 | residual patch-seq/morphology modality literals |
| `olm_hippocampus` | 6 | accessions-not-on-edge + patch-seq/immunohistochemistry modality |
| `ndnf_nkx2_1_olm_subfamily_chamberland` | 12 | F1 / modality / accession |
| `sst_nos1_subfamily_chamberland` | 8 | marker count, modality |
| `sst_tac1_subfamily_chamberland` | 17 | F1 mismatch (none on edge), modality |
| `ca1_pc_hippocampus` | 4 | F1 mismatches |
| `ca2_pc_hippocampus` | 4 | F1 mismatches |
| `ca3_pc_hippocampus` | 5 | F1 / run_ref mismatches |
| `dg_granule_cell_hippocampus` | 5 | F1 + accession |
| `hilar_mossy_cell_hippocampus` | 5 | F1 mismatches |
| `dg_semilunar_granule_cell_hippocampus` | 4 | run_ref not on edge |
| `subicular_pyramidal_cell_hippocampus` | 3 | modality patch-seq |
| `ec_layer2_stellate_cell_hippocampus` | 2 | F1=0.96 mismatch |
| `ec_layer2_pyramidal_cell_hippocampus` | 6 | marker count + modality |
| `ec_layer3_pyramidal_cell_hippocampus` | 4 | F1=0.18 mismatch |
| `hpc_calretinin_glu_neuron_hippocampus` | 2 | CLUS_0497 not on edge + morphology |
| `hpc_glu_dopa_receptor_pyramidal_hippocampus` | 1 | modality 'cre line' |

Each node has a stamped `reports/hippocampus/<stem>_summary.md.corrections.json` from `just rationale-writeback --correction-mode` ready for a focused-correction subagent.

### Zero-edges stubs (no verdict blocks; safe — nothing to write back)
- `dg_granule_cell`, `dg_mossy_cell`, `ca3_pyramidal_cell`, `ca1_pyramidal_cell`, `ms_dbb_glutamatergic_neuron`, `hpc_cajal_retzius_cell`, `ca1_radiatum_giant_cell` (from `20260427_hippocampus_glutamatergic_report_ingest.yaml`; no edges in graph)
- `_demo_ec_l3_20260607` (demo graph)
- `bistratified_cell_hippocampus` — flagged as 0-parsed by Step 4b despite synth claiming verdict blocks were written; verdict-YAML parser may be choking on a fenced-block format issue. Worth re-inspecting the report file for malformed YAML fences.

## Follow-up checklist for next session

1. Re-dispatch correction subagents for the 18 failing nodes above. Each has its corrections.json ready.
2. After each corrects, real-writeback (no `--dry-run`).
3. Investigate `bistratified_cell_hippocampus` verdict-block-not-parsed issue.
4. Run LLM-validation (Step 4) on all 41 hippocampus reports. The current PR commits only Step 4b-clean nodes; Step 4 (LLM) hasn't been run yet for hippocampus.
5. Update this PR with the residual writebacks; or open a follow-up PR `refresh_reports_20260608_hippocampus_residual`.

## Known data issues surfaced

- Anthropic Cellular-Semantics/evidencell#112: `taxonomy_id: CCN202307220` typo blocking dentate_gyrus / cerebellum / BG / immature_neurons refresh.
- Cellular-Semantics/evidencell#111: score-specific-cluster mode for stale-edge curator review (legacy edges that fell outside current Stage A top-50).
