# Validation workflows

Orchestrator docs for evidencell's validation/audit framework. Each
audit has its own workflow doc describing when to run, prerequisites,
expected outputs, and post-run discipline.

## Architecture

| Layer | Location |
|---|---|
| Driver code | `src/evidencell/validation/` |
| CLI dispatch | `python -m evidencell.validation <audit-id>` |
| `just` recipe | `just validate-<audit-id>` |
| Workflow doc | `workflows/validation/<audit-id>.md`  ← you are here |
| Run artifacts | `research/validation/methods_audits/<audit-id>/runs/` |
| Findings + decisions | `research/validation/methods_audits/<audit-id>/README.md` |
| End-to-end test | `tests/test_validation/test_<audit-id>.py` |

See [`research/validation/methods_audits/README.md`](../../research/validation/methods_audits/README.md)
for the audit framework principles (preflight invariants, raw evidence
preservation, claims must be data extractions, reproducibility).

## Audits

| Audit | Doc | Driver | Purpose |
|---|---|---|---|
| `at_blind` | [at_blind.md](at_blind.md) | `evidencell.validation.at_blind` | Measure marker+region+NT coverage against curated AT evidence |
