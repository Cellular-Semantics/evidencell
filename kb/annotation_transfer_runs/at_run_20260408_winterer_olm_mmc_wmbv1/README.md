# Winterer 2019 OLM → WMBv1 annotation transfer

Run id: `at_run_20260408_winterer_olm_mmc_wmbv1` ([manifest.yaml](manifest.yaml))
Source dataset: [GEO:GSE124847](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE124847) (Winterer et al. 2019, *Eur J Neurosci*; 46 OLM patch-seq cells, two Cre-driver subgroups).
Target atlas: WMBv1 (CCN20230722) — `precomputed_stats.h5`.

## Headline

OLM cells map cleanly at **subclass / supertype** resolution (Sst Gaba / Sst Gaba_3, F1 ≈ 0.65) but scatter across sibling clusters at **cluster** (rank 0) resolution (max F1 = 0.26 to CLUS_0768).

This is the expected pattern for a classical type that is real at one taxonomy level but not yet resolved at the leaf rank — the report's Methods section frames it as such, and the figure makes the spread visible.

## Files

| File | Purpose |
|---|---|
| `manifest.yaml` | `AnnotationTransferRun` record (provenance + run params) |
| `f1_matrix.csv` | F1 / group_purity / target_purity per (source_label × level × target_name); 25 rows |
| `mmc_results.csv` | Raw MapMyCells per-cell mapping output |
| `source_cell_labels.json` | 46 cell barcodes → source_label (Sst-OLM, Htr3a-OLM) |
| `GSE124847_OLM_mmc.h5ad` | Input AnnData (3.7 MB) — converted from GSE124847 raw counts via the MapMyCells2CL preprocessing pipeline |
| `figures/f1_heatmap.png` | Faceted F1 heatmap (2 source rows × 4 taxonomy-level columns × top targets per level). Reused unchanged in the OLM mapping report. |
| `figures/f1_compact.png` | Compact variant for smaller layouts |

## Reproduce

```bash
# 1. Activate the annotation_transfer venv (separate package)
cd /path/to/evidencell/annotation_transfer
uv venv && source .venv/bin/activate
uv pip install -e .

# 2. Run MapMyCells against the input h5ad
python -m annotation_transfer.cli run \
    --input GSE124847_OLM_mmc.h5ad \
    --labels source_cell_labels.json \
    --target precomputed_stats.h5 \
    --output mmc_results.csv

# 3. Compute F1 matrix
python -m annotation_transfer.cli score \
    --mmc mmc_results.csv \
    --labels source_cell_labels.json \
    --output f1_matrix.csv
```

The figure was rendered externally from `f1_matrix.csv` via a matplotlib script (preserved in the older `evidencell` checkout's `scratch/olm-at/`; will be ported to `src/evidencell/figures.py` as `render_at_f1_heatmap` in a follow-up branch). The pre-rendered PNG is committed here as the canonical run output for the OLM mapping report.

## Caveats

- Source N is small (46 cells); F1 stability at cluster rank is limited.
- The cluster-level scatter (CLUS_0768 / 0769 / 0773 / 0774 within SUPT_0204 Sst Gaba_3) reflects real biological structure: WMBv1's leaf clusters split Sst Gaba_3 finer than the OLM transcriptomic identity warrants. The supertype-level mapping is the appropriate resolution.
- No species mapping: source and target are both *Mus musculus*.
- See `manifest.yaml` for full provenance fields and SHAs.
