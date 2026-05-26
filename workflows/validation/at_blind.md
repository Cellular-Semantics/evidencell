# Workflow: AT-blind audit

Method-validation audit measuring whether evidencell's `find_candidates`,
run with markers + region + NT alone (AT signal disabled), surfaces
the same candidates that annotation transfer has already identified.

- **Driver:** `src/evidencell/validation/at_blind.py` (`ATBlindAudit`)
- **Recipe:** `just validate-at-blind`
- **Findings:** [`research/validation/methods_audits/at_blind/README.md`](../../research/validation/methods_audits/at_blind/README.md)

## When to run

Run after any of:

- Material change to Stage A scoring in `find_candidates` (positive/
  negative marker tiers, cohort-percentile thresholds, coverage
  dampening, region filter semantics, AT bypass behaviour).
- Change to `find_candidates`' default config (e.g. `top_k`,
  `region_expand_levels`).
- Curated AT evidence is added or substantially edited in
  `kb/graphs/**/*.yaml`.
- Before a milestone freeze that touches map-cell-type.

Don't run as a unit test — it depends on the taxonomy DB, the MBA
ontology closure, and the AT-evidenced edges in the KB. The
`tests/test_validation/test_at_blind_audit.py` synthetic test
exercises the audit pipeline against a tiny fixture for CI; the
full audit runs against the live corpus.

## Prerequisites

- Taxonomy DB built and fresh: `just build-taxonomy-db CCN20230722`
- Anat closure built: `just fetch-mba-ontology && just build-anat-closure CCN20230722`
- KB-wide marker enrichment current:
  `just enrich-marker-union CCN20230722 <stats.h5> <gene_mapping.tsv>`

The audit's preflight will check these and abort with a specific
error if any are missing.

## Run

```bash
just validate-at-blind
```

Defaults: `top_k=10`, `f1_floor=0.5`, `taxonomy=CCN20230722`.

Options:

| Flag | Meaning |
|---|---|
| `--top-k N` | Pass threshold (default 10) |
| `--f1-floor X` | Minimum AT F1 *per `metrics_by_level` entry* to include in ground truth (default 0.5 — "candidates worth investigating") |
| `--taxonomy ID` | Target taxonomy (default CCN20230722) |
| `--limit N` | Run only the first N cases (debugging) |
| `--force-preflight` | Skip past a failed invariant. Use only with documented reason. |

## Output

```
research/validation/methods_audits/at_blind/runs/
  <ISO-timestamp>.json    # this run's full record
  latest.json             # pointer copy (overwritten each run)
```

The run artifact contains:

- `audit_id`, `commit`, `started_at`, `finished_at`, `config`
- `preflight_assertions`: list of invariant outcomes
- `outcomes`: per-case dicts with `test_id`, `expected`, `actual`,
  `passed`, `reason`, `notes`, `metadata`. ``test_id`` is
  `{classical}|{level}|{target_accession}` — **one case per AT
  metrics_by_level entry**, not per edge.
- `summary_stats`: aggregated `pass_count`, `pass_rate`,
  `by_reason`, plus:
  - `by_level` — pass rates split by AT level
    (`cluster`/`supertype`/`subclass`/`class`). Cluster vs subclass
    pass rates diagnose whether the audit is finding fine vs coarse
    matches.
  - `by_monotonicity` — pass rates split by F1 monotonicity tag
    (`rises_with_resolution`, `falls_with_resolution`, `flat`,
    `mixed`, `insufficient`). `falls_with_resolution` means the
    source label is biologically mixed (Yao Sst case): prefer
    precision (`purity`) over F1 when interpreting weakening
    cluster-level hits. `rises_with_resolution` means the source is
    morphologically/biologically pure (Que 2021 patch-seq case);
    cluster-level F1 is the right summary.
  - `region_descendant_fallback_hits` — count of candidates rescued
    from `region_drop` by the rank-0-descendant anat fallback in
    `find_candidates` (workaround for the upstream BCKG anat
    over-strip; see [the findings doc](../../planning/at_blind_region_drop_findings_2026-05-12.md) § a).

## After the run

1. Inspect `summary_stats.pass_rate` and the by-reason breakdown
   printed to stdout.
2. For any *new* misses (not present in the previous `latest.json`):
   open the per-case `actual` block, read the raw data, write the
   explanation into the audit's README "Findings" section. Do not
   summarise without consulting the data — see "Discipline" below.
3. If the audit informed a code change, update the "Decisions
   informed" section of the README with the commit hash and rationale.
4. Commit both the run artifact and the README updates.

## Discipline

The audit framework deliberately preserves raw evidence in `actual`
so that interpretive claims in writeups can be ground-checked. When
reporting on a miss, the supporting data must be quoted from the
`actual` block, not paraphrased from memory. Examples:

- ✓ "CLUS_0769 has `expression_detail.Chrna2.val = 0.0` (absence
  penalty fires)."
- ✗ "CLUS_0769 is below_topk because of weak AT signal." (Not
  supported by the audit's data; this is an inference.)

If a claim in the README cannot be backed by a value in the
`actual` block, the claim either needs a follow-up data extraction
or removal.

## Known limitations

See the [audit README](../../research/validation/methods_audits/at_blind/README.md)
section "Limitations" for the current list.
