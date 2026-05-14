# Methods audits index

This directory holds **method-validation audits** of evidencell
workflows: runnable comparisons of pipeline behaviour against an oracle
ground truth, producing structured run artifacts and prose findings.

## Layout

```
research/validation/methods_audits/
  README.md                    ← this index
  <audit_id>/
    README.md                  ← methodology + run history + decisions informed
    runs/                      ← timestamped JSON artifacts; `latest.json` symlink
      <YYYY-MM-DDTHHMMSS>.json
      latest.json
```

## Where the code lives

| Layer | Location | Purpose |
|---|---|---|
| Code | `src/evidencell/validation/` | Audit driver classes (`AuditDriver`, concrete subclasses) + CLI dispatch |
| Workflow doc | `workflows/validation/<audit_id>.md` | When to run, gates, expected outputs |
| Recipe | `justfile` → `just validate-<audit_id>` | One-line invocation |
| Run history + findings | `research/validation/methods_audits/<audit_id>/` | What we ran, what we learned, what it informed |
| Tests | `tests/test_validation/` | Synthetic end-to-end exercises of the audit pipeline |

## Audit framework principles

These patterns exist to minimise the "agent inference substitutes for
data lookup" failure mode that bit us in early at-blind runs (e.g.
claiming a target was in the wrong region without checking the data,
or running the audit with the region filter silently disabled).

1. **Preflight invariants fail loud.** Each `AuditDriver` declares a
   list of `(name, callable)` checks that run before the audit body.
   Examples: taxonomy DB exists, DB is fresh, anat_closure is built,
   every classical node's UBERON IDs resolve to ≥1 MBA term. A failure
   aborts the run with a specific error; the run artifact records the
   failed assertion. Use `--force-preflight` only when you have a
   documented reason and the audit doc records it.

2. **Outcomes carry raw evidence.** Each `AuditOutcome` has `expected`
   and `actual` dicts containing the data that backed the verdict —
   not just `passed: bool`. A reviewer reading the JSON can audit the
   audit without re-running it.

3. **Claims are data extractions.** When a writeup says "this candidate
   was dropped because of X", the supporting `actual` dict must contain
   X. Avoid prose that summarises away the underlying value.

4. **Runs are reproducible.** Each `AuditRun` records the git commit,
   the config, the timestamps, every preflight outcome. Re-running on
   the same commit with the same config should reproduce.

5. **Known limitations are surfaced in the README.** When an audit
   miss-classifies a case or silently skips work, the audit-specific
   README gains a "Known limitations" entry. Future runs that hit the
   same case know to check.

## Index of audits

| Audit | Status | When to run | Key decision informed |
|---|---|---|---|
| [at_blind](at_blind/) | active | After scoring changes (map-cell-type Stage A) | region expansion default; cohort-relative scoring sanity |

## Adding a new audit

1. Implement an `AuditDriver` subclass in `src/evidencell/validation/`.
2. Wire a CLI subcommand in `src/evidencell/validation/__main__.py`.
3. Add `just validate-<audit-id>` recipe.
4. Add `workflows/validation/<audit_id>.md` orchestrator doc.
5. Add `research/validation/methods_audits/<audit_id>/README.md` with
   the methodology writeup.
6. Add a synthetic end-to-end test in `tests/test_validation/`.
7. Update this index.
