# CLAUDE_dev.md — dev-mode companion

This is the **dev-mode** companion to `CLAUDE.md` (the default curation guide).
Load this file explicitly when the session involves changes to `src/`,
`schema/`, `.claude/hooks/`, or `justfile`. Write access to those paths is
gated by the pre-edit hook; if you hit a block, contact the repo maintainer
or file a dev-request report under `planning/dev_requests/`. Dev work lands
through PR review against `main`.

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

## Project

evidencell is a LinkML-based knowledge base for cell type mapping evidence — linking classical cell types to modern transcriptomic atlas clusters. It combines a structured schema, a curated KB of mapping YAML files, Python tooling, and an ASTA-powered literature review workflow.

## Repo structure

```
schema/                  # LinkML schema (source of truth for KB structure)
kb/mappings/{region}/    # canonical, validated mapping graphs (YAML only)
kb/draft/{region}/       # work-in-progress graphs (YAML only); graduate via just qc
references/{region}/     # references.json — shared quote store per region
research/{region}/       # research artifacts: field_mapping, cite_traverse, evidence_extraction
reports/{region}/        # human-readable summary + drill-down reports
inputs/deepsearch/       # ASTA deep research PDFs used as literature discovery input
inputs/taxonomies/       # taxonomy table slices (CSV/TSV) used for ingest-taxonomy
src/evidencell/          # all Python logic (validation, rendering, compliance, fetching)
workflows/               # multi-step curation orchestrators (see below)
.claude/hooks/           # pre-edit validation hook (runs before KB writes)
.claude/skills/          # bounded single-focus tasks, called interactively
.claude/agents/          # shared subagent personas (reserved; populate if needed)
references_cache/        # cached ASTA reference text for snippet provenance
justfile                 # thin task runner — all logic lives in src/evidencell/
CLAUDE.md                # curation-mode default guide: which orchestrator to run, when, and with what inputs
CLAUDE_dev.md            # this file — dev-mode companion guide
```

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
- **New KB schema class or required field** → graduated files in `kb/mappings/` are the strict schema fixtures; `test_kb_examples.py` validates them on every `just test` run. Draft files in `kb/draft/` are only checked for YAML parseability — schema conformance for drafts is the job of `just qc-draft` and the pre-edit hook.

**What NOT to write tests for:**

- OAK DB term lookups — too heavy; validate terms interactively with `runoak` before committing.
- Workflow orchestrators (`workflows/*.md`) — these are prose + control flow, not Python code; test them by running them, not by unit-testing them.
- Stub modules (`fetch.py`, `render.py`, `compliance.py`) — add tests when the implementation lands.
- Just recipe shell glue — trivial file-existence / grep logic; not worth mocking.

**Regression rule:** if a bug slips through `just qc` or `just test` once, add a targeted test before fixing it so it cannot regress silently.

## Anti-hallucination mechanisms

Anti-hallucination is a **central design principle** of all evidencell workflows. The system
enforces correctness structurally rather than relying on self-correction.

Two complementary mechanisms:

1. **Pre-write hooks** (`.claude/hooks/`) — triggered automatically before any `Edit` or
   `Write` to KB YAML or reports. If the hook rejects, fix the underlying content — do not
   attempt to bypass the hook.

2. **Validation subagents** (within orchestrators) — spawned after LLM synthesis steps to
   cross-check generated content against a provenance-labelled facts file. See
   `workflows/gen-report.md` Step 4 for the pattern.

Each validated content type (ontology terms, gene IDs, publication IDs, verbatim quotes)
has a defined storage syntax and a defined verification source. All checks rely on this
consistency: a name:ID pair can be verified against an ontology endpoint; a quote can be
verified as verbatim against its content-hashed entry in `references.json`.

For current implementation details, validation sources, and the rules governing agentic
writes to validated stores, read:
**[`.claude/anti-hallucination-hooks.md`](.claude/anti-hallucination-hooks.md)** *(compulsory read before modifying hooks, validation logic, or `references.json` ingest)*

## Working with YAML and LinkML

- Always parse YAML with `yaml.safe_load()`. Never use shell `grep`, `sed`, or `awk` on YAML files.
- The pre-edit hook validates KB YAML before it reaches disk. If it rejects, fix the underlying issue — do not attempt to bypass the hook.
- When the hook reports an error, read the structured output, correct the YAML, and retry. The correction loop typically resolves in 1–2 iterations.
- Ontology terms (CL, UBERON, NCBITaxon) must exist in the OAK local databases. Look up terms with `runoak` before using them — do not invent IDs.

## Claude bug fix

You *must* validate *all* image files before reading them.