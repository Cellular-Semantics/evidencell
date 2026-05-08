# Dev request: scaffold AT manifests from operator run directories

**Date:** 2026-05-08
**Status:** Filed — ready for implementation when scheduled
**Trigger:** Audit of `kb/annotation_transfer_runs/index.yaml` post-merge
revealed 10 distinct (KB-file × source-dataset) groups of AT evidence with
no `run_ref` and no manifest. Several of these correspond to runs the
hippocampal-glut authors performed externally before the AT registry
landed (commit `c9da825`, 2026-05-06). Authoring those manifests by hand
across ~10 runs is the wrong cost profile.

---

## Goal

Add a `just scaffold-at-manifest` recipe that takes an operator's working
directory of MapMyCells outputs and emits a populated `manifest.yaml`
stub at `kb/annotation_transfer_runs/{run_id}/manifest.yaml`, with all
mechanically derivable fields filled in. The operator drops in their
files, fills the few qualitative `TODO:` markers (primarily `caveats`),
and `just register-at-run` indexes it.

---

## What's predictable from a working directory

The scratch/olm-at directory and the two registered run records
(`20260408_winterer_olm_mmc_wmbv1`, `at_run_20260506_harris_chamberland_mmc_wmbv1`)
all share the same canonical artefact set, which is what
`just at-map-local` + `just at-score` produce. That gives us a stable
file layout to scaffold from:

| Canonical filename | Purpose | Fields derivable |
|---|---|---|
| `*.h5ad` (input) | MMC-ready AnnData | `n_cells_total`, `source_file_sha256`, `metadata.source_format=h5ad` |
| `*.labels.json` or `source_cell_labels.json` | per-cell label map | `source_cluster_label` (group names + per-group counts) |
| `mmc_results.csv` | MapMyCells per-cell output | row count → `n_cells_after_filter`, sha256 |
| `mmc_extended.json` | MMC extended metadata | `tool_version`, `bootstrap_threshold`, mapping parameters |
| `f1_matrix.csv` | F1 scoring output | sha256, present-flag for `output.relpath` |
| `figures/*.png` | F1 heatmap | `figure.relpath`, sha256 |
| `mouse_markers_*.json` | marker reference (incidental) | not on manifest |
| precomputed_stats h5 (referenced) | atlas pseudobulk | `atlas.pseudobulk_source`, sha256 |

Plus environment-derived fields:
- `script.git_commit` ← `git rev-parse HEAD`
- `script.git_repo_url` ← `git remote get-url origin`
- `script.python_version` ← from current uv lockfile or running interpreter
- Convention-based fields (`target_atlas: WMBv1`, `target_species:
  NCBITaxon:10090` for mouse data; configurable via flags)

**Residual fields needing operator input** (small):
- `caveats` — qualitative; emit `TODO:` placeholder
- `code_version` — emit `(external; precomputed)` default; operator
  overrides if internally produced
- `code_reference` — default to AllenInstitute MMC repo URL; override flag
- `metadata` — multi-line free-form; emit a structured stub from what we
  know (source dataset, sha256s, levels scored, source groups + counts)

---

## Proposed surface

```
just scaffold-at-manifest RUN_ID RUN_DIR [SOURCE_DATASET] [TARGET_TAXONOMY] [*OPTS]

Examples:
  just scaffold-at-manifest at_run_20260427_yao2021_hpf_pvalb_wmbv1 \
       /path/to/operator/yao2021_hpf_pvalb GEO:GSE185862 CCN20230722

  # auto-infer source dataset from h5ad filename / parent dir naming convention
  just scaffold-at-manifest at_run_20260427_yao2021_hpf_pvalb_wmbv1 \
       scratch/yao2021/
```

Behaviour:
1. Walk `RUN_DIR` for the canonical artefacts above.
2. Hash each file (sha256), populate manifest with relative paths.
3. Read mmc_extended.json for tool_version / bootstrap_threshold.
4. Read labels.json for source_cluster_label group structure.
5. Read f1_matrix.csv to populate richest fields possible (best_f1_score,
   best_mapping_level summary in `metadata`).
6. Resolve atlas pseudobulk path/hash from taxonomy_meta.yaml +
   `local_stats_path`.
7. Capture git_commit / git_remote / python_version from the env.
8. Render manifest.yaml from a Jinja template with `TODO:` markers for
   `caveats` and any field that couldn't be resolved.
9. **Copy** (don't move) the canonical artefacts into
   `kb/annotation_transfer_runs/{RUN_ID}/`. Skip if files already there
   (idempotent re-runs).
10. Print a checklist of remaining TODOs before recommending
    `just register-at-run`.

Optional flags:
- `--target-atlas WMBv1` (default)
- `--target-species NCBITaxon:10090` (default)
- `--copy-input` to vendor the input h5ad into the run record (large, but
  matches the Winterer-OLM precedent for full reproducibility)
- `--dry-run` to preview without writing
- `--from-evidence kb/path/to/file.yaml --dataset GEO:...` — pull
  inline AT evidence blocks for that dataset and use their fields
  (best_f1_score, n_cells_total, source_cluster_label, method) as a
  cross-check against the directory contents; warn on mismatch.

---

## Backfill use case

For each of the 10 unindexed groups identified in the merge audit, the
operator (whoever ran the external mapping) supplies their working
directory; we run the scaffolder with the appropriate `--from-evidence`
flag pointing at the KB file that already cites the run, and the output
manifest both validates against `AnnotationTransferRun` and matches the
inline evidence blocks. After registration, a follow-up curator pass adds
`run_ref:` to the inline evidence blocks (or a small companion command
`just backfill-run-ref RUN_ID KB_FILE DATASET` does it programmatically).

---

## Out of scope (file as separate work)

- Auto-adding `run_ref:` to existing AT evidence blocks. That's a separate
  KB-edit step. Could be a `--patch-evidence` flag here, but cleaner as
  its own command so the manifest scaffolding stays read-only on the KB.
- Standardising the `just at-map-local` / `just at-score` output layout
  itself. Today the canonical filenames are conventional, not enforced.
  Worth tightening once the scaffolder has revealed the contract it
  depends on.
- Extending the same pattern to `CorrelationRun` records. Probably a
  parallel scaffolder, not a shared one — different artefact set.

---

## Acceptance criteria

1. Running the scaffolder against `scratch/olm-at/` (with
   `at_run_20260408_winterer_olm_mmc_wmbv1` as RUN_ID) reproduces a
   manifest within whitespace/`caveats` of the existing
   `kb/annotation_transfer_runs/20260408_winterer_olm_mmc_wmbv1/manifest.yaml`.
2. Running it against a synthetic minimal run dir (just the canonical
   files) emits a valid manifest with `TODO:` placeholders only for
   genuinely qualitative fields.
3. `just register-at-run` accepts the scaffolded manifest without
   modification (modulo TODO resolution).
4. Test added under `tests/test_scaffold_at_manifest.py` exercising both
   golden-path and missing-files cases.

---

## Risks

- File-naming conventions in operator working directories drift. The
  scaffolder should be permissive (accept `*.csv` matching a glob) and
  loud about what it found vs expected.
- `mmc_extended.json` schema is upstream-controlled (Allen MMC). If the
  scaffolder relies on a specific key path, document the version
  baseline (cell_type_mapper v1.7.1 per the existing manifests).
