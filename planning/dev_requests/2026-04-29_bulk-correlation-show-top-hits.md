# Dev request: surface top-N hits in BulkCorrelationEvidence rendering

**Date:** 2026-04-29
**Severity:** Low — enhancement to BulkCorrelationEvidence reporting; current
output is correct but unverifiable from the report alone.

---

## Context

The first regenerated report under the new generic-evidence framework
(`reports/sexually_dimorphic/avpv_kiss1_neuron_summary.md`, commit `0ba481a`)
includes this BulkCorrelation evidence narrative for CLUS_1915:

> Stephens 2024 (PMID:37934722) bulk Kiss1+ neurons sorted from RP3V vs ARC.
> Differential δ = ρ_RP3V − ρ_ARC ranks CLUS_1915 first of 5,322 atlas clusters,
> with δ=0.090 (ρ_RP3V=0.388, ρ_ARC=0.298). All other top-20 hits are also
> preoptic/periventricular hypothalamic GABAergic clusters — the differential
> signal is strongly anatomically clean.
> — Stephens et al. 2024 · [7]

**The "all other top-20 hits are also preoptic/periventricular GABAergic" claim
is the most scientifically interesting line in the entire evidence narrative —
but the reader has no way to verify or explore it from the report.** They have
to dig into `kb/correlation_runs/{run_id}/delta_rp3v_specific.tsv` (or the
equivalent ranked output) to see the spread of hits.

For other classical types where the spread might be less anatomically clean,
this matters even more: a curator looking at a BulkCorrelation result wants
to see whether the top-N hits cluster anatomically (good signal) or are
scattered across unrelated regions (weak signal, possibly noisy).

## Proposal

When `gen-report` (or the synthesis subagent) renders a BulkCorrelationEvidence
item, also emit a small **top-N hits** table immediately below the evidence
blockquote. Pull from the run's ranked output (referenced via `manifest.output.relpath`).

Suggested format (top 10, one row per cluster):

| Rank | δ | Cluster | Supertype | Top anatomy | MFR |
|---:|---:|---|---|---|---:|
| 1 | 0.090 | CS20230722_CLUS_1915 | SUPT_0486 | Hypothalamus | 0.02 |
| 2 | 0.087 | CS20230722_CLUS_1527 | SUPT_0418 | Median preoptic nucleus | 1.56 |
| ... | | | | | |

The cluster being mapped (CLUS_1915) is bolded or marked. The reader can
immediately see:
- Whether the target cluster sits at the top of the ranking (rank 1 here)
- Whether the spread is anatomically coherent (all preoptic/periventricular)
  or scattered (would be a red flag)
- Whether sister clusters of the same supertype also appear high
- Whether the MFR pattern across hits matches the classical type's sex bias

## Implementation surface

The data is already present:
- `manifest.output.relpath` → `kb/correlation_runs/{run_id}/{output_file}.tsv`
  (e.g. `delta_rp3v_specific.tsv`, sorted by δ descending, with cluster + δ + label
  + parent_supertype + top_anat + MFR columns)
- `manifest.contrasts[*]` tells us which contrast id each evidence item references
- The renderer (or a new helper) reads the top N rows and emits them as a Markdown
  table with the target cluster highlighted

`render.py` extension sketch:
```python
def _read_top_n_for_contrast(run_ref: str, contrast_ref: str, n: int = 10) -> list[dict]:
    """Read top-N rows from the ranked output TSV for the named contrast."""
    # 1. Resolve run manifest
    # 2. Find contrast metadata (which TSV column / which output file)
    # 3. Read top N rows
    # 4. Return list[dict] with columns: rank, delta, cluster, supertype, top_anat, mfr
```

This reaches into `kb/correlation_runs/{run_id}/` filesystem just like the
existing `_resolve_run_ref_to_pmid` helper. Deterministic, no extra schema.

The synthesis subagent prompt in `workflows/gen-report.md` would add a rule:
> For each BULK_CORRELATION evidence item with a resolvable run_ref + contrast_ref,
> follow the attributed blockquote with a top-N hits table built from the run's
> output. Highlight the row whose cluster matches the edge target.

## Verification

- Re-run on `avpv_kiss1_neuron`: the top-10 table for the RP3V vs ARC contrast
  should put CLUS_1915 at rank 1 with surrounding rows showing the
  preoptic/periventricular GABAergic cluster set the user noted in §0.
- Re-run on a hypothetical case where the top-10 spans multiple unrelated
  regions — the table should make that anatomical incoherence visible
  without requiring trust in the prose narrative.

## Out of scope (for now)

- Configurable N (top-10 is enough; optional override later)
- Highlighting in HTML/CSS — keep to plain Markdown bolding
- Cross-contrast comparison tables (e.g. side-by-side δ_RP3V_minus_ARC and
  δ_ARC_minus_RP3V) — separate feature
- Visualisation as an image — the table is enough for review
