# CLAUDE_dev.md — dev-mode companion

This is the **dev-mode** companion to `CLAUDE.md` (the default curation guide).
Load this file explicitly when the session involves changes to `src/`,
`schema/`, `.claude/`, `workflows/`, or `justfile`. Write access to those paths is
gated by the pre-edit hook; if you hit a block, contact the repo maintainer
or file a dev-request **GitHub issue** (see "Dev request workflow" below).
Dev work lands through PR review against `main`, with PRs closing the
originating issue via `Closes #N`.

## Dev request workflow

Dev requests are tracked as **GitHub issues** on
`Cellular-Semantics/evidencell`, not as markdown files. Each issue captures
one blocker or feature ask; a PR resolves it with `Closes #N` in the body.

### Filing an issue

Use the project PAT exposed via `$CELLSEM_GH_TOKEN` (set in
`.claude/settings.local.json`, gitignored). Pattern:

```bash
GH_TOKEN="$CELLSEM_GH_TOKEN" gh issue create --repo Cellular-Semantics/evidencell \
  --title "{short description}" \
  --body "$(cat <<'EOF'
## Goal
...

## Scope
...

## Proposed surface
...

## Open questions
...
EOF
)"
```

If `$CELLSEM_GH_TOKEN` is unset (e.g. in a CI or fresh-clone environment),
`gh` falls back to the system keychain — the wrapper degrades gracefully.

Required body sections: **Goal**, **Scope**, **Proposed surface**. Add
**Open questions** and **Out of scope** when relevant. Keep the issue
self-contained — it should be readable without the originating chat
transcript.

### Linking from ROADMAP

When a roadmap item maps to a tracked issue, link it inline:

```markdown
- [ ] Taxonomy-indexed report TOC ([#26](https://github.com/Cellular-Semantics/evidencell/issues/26)) `#gen-report`
```

Roadmap entries without a corresponding issue are fine — issues are for
items that need a dedicated PR.

### Closing via PR

End the PR body with `Closes #N` (one line per issue) so merge auto-closes
the issue. Do not delete the issue; the closed thread is the historical
record.

### Migration note

The legacy markdown reports under `planning/dev_requests/*.md` are the
historical record up to 2026-04-30. New dev requests go to GitHub issues.
The directory's `README.md` redirects to this workflow.

This file provides guidance to Claude Code when working on the code, schema,
and tooling in the **evidencell** repository.

## Schema changes

Schema edits MUST be discussed and reviewed before implementation. They are
occasionally legitimate — when importing a new kind of data (e.g. a new
taxonomy with fields not yet represented) or handling a novel mapping
scenario — but are almost never the right response to a LinkML validation
error. The default response to a validation error is to fix the data, not the
schema. If discussion concludes that a schema change is warranted, it lands in
its own PR with an explicit rationale; it does not ride along in a
content-focused commit.

## Consistency over scope economy

When proposing a fix or refactor that touches naming, conventions, or
data shapes, default to **end-to-end consistency** — even when the small
scope feels tempting. Any lack of consistency between adjacent surfaces
(schema / code / data / docs / reports) is a real source of confusion
that will bite a later session. The maintainer's standing preference is
"the bigger PR with full alignment, not the smaller one with a known
mismatch left behind."

Practical implications when scoping:

- **Do** propose the smaller and larger versions side by side with
  honest time + risk estimates. Don't slip into recommending the
  smaller one to save effort.
- **Do** push the rename / convention change through every surface
  it touches in one commit / PR: schema, generated Pydantic, every
  consumer in `src/`, every KB YAML file, every test fixture, every
  doc, every report, every sidecar / artefact file.
- **Do** add a back-compat *read* path for legacy on-disk artefacts
  (e.g. `at_metrics.migrate_csv` accepts both old and new CSV column
  names) — that's how a hard cutover stays robust against pre-cutover
  data still being out in the wild.
- **Don't** keep aliases in the schema. The Phase 2 precedent is hard
  cutover (e.g. `type_a` → `lit_type` removed the old name entirely);
  follow it.
- **Don't** invent a third name to bridge old + new. Pick one
  canonical name, document the rename, move on.

Worked example: the 2026-05-25 purity/coverage standardisation
(commit `fcdf68d`) renamed `group_purity` → `coverage` and
`target_purity` → `purity` across 70 files in one commit — schema,
Pydantic models, scoring CSV emitter, all consumers, all KB YAMLs,
all `at_results*.yaml`, all sidecars, every test, every report. The
smaller alternative ("rename everything except the schema field
identifiers, since those are in hundreds of YAML files") was rejected
on this principle: leaving the slot names mismatched with sidecars +
figures + reports would have preserved exactly the confusion we were
fixing.

## AT metric nomenclature (canonical)

The two annotation-transfer per-(source, target) quantities have a
single canonical name across every surface of the codebase. Standard
ML terms are retained in parens for cross-reference only. Use the
canonical names in all new code, docs, and reports.

| Canonical | Definition | Schema field | CSV column | Sidecar JSON | Figure |
|---|---|---|---|---|---|
| **Coverage** (= recall) | Fraction of source cells on this target | `coverage` | `coverage` | `coverage` | `Cov` |
| **Purity** (= precision) | Fraction of target cells from this source | `purity` | `purity` | `purity` | `Pur` |

F1 is the harmonic mean of coverage and purity. See
[`docs/at_data_flow.md`](docs/at_data_flow.md) § "Purity and coverage —
naming reference" for full provenance.

Legacy CSVs produced before the 2026-05-25 standardisation used
`group_purity` / `target_purity`; the read path in
`src/evidencell/at_metrics.py::migrate_csv` and
`src/evidencell/at_figures.py::load_f1_matrix` accepts both and
normalises on load. Do not emit the old names in new code.

## Project

evidencell is a LinkML-based knowledge base for cell type mapping evidence — linking classical cell types to modern transcriptomic atlas clusters. It combines a structured schema, a curated KB of mapping YAML files, Python tooling, and an ASTA-powered literature review workflow.

## Repo structure

```
schema/                                       # LinkML schema (source of truth for KB structure)
kb/graphs/{region}/                           # cell-type mapping graphs (YAML only); just qc + PR review as quality gate
references/{region}/                          # references.json — shared quote store per region
research/{region}/                            # research artifacts: field_mapping, cite_traverse, evidence_extraction
research/validation/methods_audits/{audit}/   # validation/audit run artifacts + per-audit findings READMEs
reports/{region}/                             # human-readable summary + drill-down reports
inputs/deepsearch/                            # ASTA deep research PDFs used as literature discovery input
inputs/taxonomies/                            # taxonomy table slices (CSV/TSV) used for ingest-taxonomy
src/evidencell/                               # all Python logic (validation, rendering, compliance, fetching)
src/evidencell/validation/                    # audit/validation drivers (AuditDriver + concrete subclasses)
workflows/                                    # multi-step curation orchestrators (see below)
workflows/validation/                         # validation/audit orchestrator docs
.claude/hooks/                                # pre-edit validation hook (runs before KB writes)
.claude/skills/                               # bounded single-focus tasks, called interactively
.claude/agents/                               # shared subagent personas (reserved; populate if needed)
references_cache/                             # cached ASTA reference text for snippet provenance
justfile                                      # thin task runner — all logic lives in src/evidencell/
CLAUDE.md                                     # curation-mode default guide: which orchestrator to run, when, and with what inputs
CLAUDE_dev.md                                 # this file — dev-mode companion guide
```

## Validation / methods audits

Method-validation audits are runnable drivers that compare evidencell's
current behaviour against an oracle ground truth (e.g. curated AT
evidence). They live alongside the workflow code and follow a
deliberate four-piece layout (code, recipe, orchestrator doc, findings
doc) intended to combat the "agent inference replaces data lookup"
failure mode.

| Layer | Location |
|---|---|
| Driver code | `src/evidencell/validation/` (concrete subclasses of `AuditDriver`) |
| CLI dispatch | `python -m evidencell.validation <audit-id>` |
| `just` recipe | `just validate-<audit-id>` |
| Workflow doc | `workflows/validation/<audit-id>.md` |
| Run artifacts + findings | `research/validation/methods_audits/<audit-id>/` |
| End-to-end tests | `tests/test_validation/` |

The framework enforces:
- Preflight invariants (fail loud rather than silently skip).
- Raw `expected` / `actual` dicts on every outcome (claims must be
  data extractions, not summaries).
- Reproducibility metadata on every run (git commit, config, timestamps).

Add an audit by following the checklist in
[`research/validation/methods_audits/README.md`](research/validation/methods_audits/README.md).

## Orchestrators vs skills

**Multi-step curation workflows live in `workflows/` as orchestrators.** An orchestrator holds the control flow explicitly, spawns subagents with verbatim prompts, and stores state in files on disk. This is the pattern from `lit-review.md` — reliable because the orchestrator enforces sequencing and gates; subagents cannot skip steps they don't know exist.

**Single-focus bounded tasks live in `.claude/skills/`.** A skill is a prompt library for a constrained, well-defined action (review a PR, present a catalogue for weeding). Skills give Claude discretion over execution and are appropriate when the task is simple enough that that discretion does not matter.

**Do not implement a multi-step workflow as a skill.** Skills give Claude room to approximate the workflow, taking shortcuts and collapsing validation gates. For anything with sequential steps, conditional logic, or human review gates, write an orchestrator in `workflows/`.

There is no meta-orchestrator driving the whole pipeline. The human is the top-level coordinator: they run each phase orchestrator when ready, review the output at each gate, and proceed at their own pace. `CLAUDE.md` (the default curation guide) documents what to run when.

**Keep `CLAUDE.md` current.** Any time an orchestrator is added, removed, renamed, or its status changes, update `CLAUDE.md` in the same commit. The overview table, inputs table, and typical workflow diagram must all reflect the current state. Never leave a stale status entry or a duplicate section.

## Code quality

- Run `just qc` before committing. This covers schema validation, ontology term checking, and snippet provenance.
- All Python logic longer than ~10 lines belongs in `src/evidencell/`, not in justfile shell blocks. `justfile` recipes are thin dispatchers.
- `ruff` for linting, `mypy` for type checking. Both must pass cleanly.
- `pytest` for unit tests. The ported KB examples are the test fixtures — if a schema or rendering change breaks them, CI catches it.

## Testing

Three test tiers keep runs cheap:

| Tier | Command | When to run |
|------|---------|-------------|
| Smoke | `just smoke` | After any dependency update — verifies external CLI interfaces haven't changed |
| Fast | `just test-fast` | Normal dev loop — all unit tests, no OAK DB or network |
| Full | `just test` | Pre-commit and CI — includes integration tests |

**What to write as you develop:**

- **New `src/evidencell/` module** → unit tests in `tests/test_<module>.py`. Test pure logic with in-process data; mock `subprocess.run` for any CLI calls.
- **New external CLI invocation** (new tool added to justfile or `validate.py`) → add a `--help` probe to `tests/test_tool_interfaces.py` asserting the subcommand and key flags exist. This is what catches "wrong subcommand" bugs like the `linkml-term-validator` regression.
- **New hook behaviour** → add a case to `tests/test_hook_integration.py` (valid YAML → exits 0, bad YAML → exits 2).
- **New KB schema class or required field** → files in `kb/graphs/` are the schema fixtures; `test_kb_examples.py` runs strict linkml + structural checks on every `just test` run. Pre-edit hook also validates writes interactively.

**What NOT to write tests for:**

- Workflow orchestrators (`workflows/*.md`) — these are prose + control flow, not Python code; test them by running them, not by unit-testing them.
- Stub modules (`fetch.py`, `render.py`, `compliance.py`) — add tests when the implementation lands.
- Just recipe shell glue — trivial file-existence / grep logic; not worth mocking.

**OAK DB term-lookup tests ARE required (NOT the previous "too heavy" exception).**
End-to-end hook tests that exercise the term-validation path against real OAK
adapters must exist and run in CI. Mark them `@pytest.mark.integration` (so
`just test-fast` skips them) and gate each test on the relevant DB being cached
locally — CI fetches the DBs via `just fetch-oak-dbs` before running the
integration suite. Mocking the validator inside `tests/test_validate.py` is
fine for testing the wiring (e.g. soft-skip behaviour) but does **not**
substitute for an integration test that runs the real validator against the
real schema with a deliberately-hallucinated CURIE.

**Regression rule:** if a bug slips through `just qc` or `just test` once, add a targeted test before fixing it so it cannot regress silently.

## Anti-hallucination mechanisms

Anti-hallucination is the **primary correctness mechanism** for evidencell — it is not
a nice-to-have, it is the load-bearing safeguard that lets us trust LLM-authored
curation. Every category of identifier present in the KB — ontology CURIEs (CL,
UBERON, NCBITaxon, MBA, DHBA, HOMBA, …), publication IDs (PMID, DOI), gene IDs (NCBI
Gene, HGNC), verbatim quote keys, atlas accessions — **must have a working, tested
check** that catches a hallucinated value before it lands on disk. If any check is
absent, soft-skipped, or silently bypassed, hallucinated content can reach `kb/` and
downstream reports without trace.

Two complementary mechanisms:

1. **Pre-write hooks** (`.claude/hooks/`) — triggered automatically before any `Edit` or
   `Write` to KB YAML or reports. If the hook rejects, fix the underlying content — do not
   attempt to bypass the hook.

2. **Validation subagents** (within orchestrators) — spawned after LLM synthesis steps to
   cross-check generated content against a provenance-labelled facts file. See
   `workflows/gen-report.md` Step 4 for the pattern.

Each validated content type has a defined storage syntax and a defined verification
source. A name:ID pair can be verified against an ontology endpoint; a quote against
its content-hashed entry in `references.json`; a PMID against the metadata in the
same store.

### Discipline for hallucination checks (NON-NEGOTIABLE)

**Every identifier category present in the KB must have a check that is wired in
end-to-end and tested in CI.** Concretely:

- **Coverage**: When a new identifier category is introduced (e.g. a new ontology
  prefix, a new ID-like field), the same PR that introduces the storage must wire
  up the check, the soft-skip mechanism (with a clear missing-resource message),
  and the integration test. Do not land "we'll add validation later" — later
  reliably becomes never, and the gap is invisible until something hallucinates.
- **End-to-end test required**: Each check must have a test in
  `tests/test_hook_integration.py` of the form "valid YAML → exit 0, deliberately
  hallucinated value → exit 2 with the bad identifier mentioned in stderr."
  Marked `@pytest.mark.integration` when it requires external resources (OAK DBs,
  network); CI must run integration tests after fetching those resources via
  `just fetch-oak-dbs`. **A unit test that mocks the validator is not sufficient
  — the check must be exercised end-to-end through the actual hook.**
- **Soft-skip is dangerous**: A soft-skip path (e.g. "resource not available →
  allow the write with an info message") is necessary for fresh clones but is
  also the most common silent-failure mode. Any soft-skip MUST:
  - Print a clearly visible message to stderr with the actionable fix
    (`run `just fetch-oak-dbs``).
  - Be tested: a test must confirm the soft-skip message appears when the
    resource is removed.
  - Be exercised in CI: CI must fetch the resources so the real (non-skip)
    path runs against every PR. Never run CI in skip mode.
  - Be reviewed for path-sync drift on every dependency upgrade. The
    `_semsql_db_path` regression (the function checked `~/.data/semsql/sqlite/`
    while oaklib started caching under `~/.data/oaklib/`) silently disabled
    term validation for an unknown period before the term-validation-bindings
    PR caught it. Path conventions of vendored caches are external state — pin
    them in a test that asserts the resource exists where we expect.
- **No new check without a regression-locking test**: If a hallucination slips
  past CI once, the test that would have caught it MUST be added before the
  data is repaired. This is the same regression rule as elsewhere in the
  codebase, but it applies with extra force here.

### What is and isn't currently checked

A live status of which checks fire end-to-end on which content types lives in
[`.claude/anti-hallucination-hooks.md`](.claude/anti-hallucination-hooks.md).
**Read it before modifying hooks, validation logic, the schema's ontology
bindings, or `references.json` ingest.** When a check moves from
"intended/documented" to "actually wired", update the Status line in the same
PR — stale status claims are the antecedent of silent failures.

## Working with YAML and LinkML

- Always parse YAML with `yaml.safe_load()`. Never use shell `grep`, `sed`, or `awk` on YAML files.
- The pre-edit hook validates KB YAML before it reaches disk. If it rejects, fix the underlying issue — do not attempt to bypass the hook.
- When the hook reports an error, read the structured output, correct the YAML, and retry. The correction loop typically resolves in 1–2 iterations.
- Ontology terms (CL, UBERON, NCBITaxon) must exist in the OAK local databases. Look up terms with `runoak` before using them — do not invent IDs.

## Claude bug fix

You *must* validate *all* image files before reading them.