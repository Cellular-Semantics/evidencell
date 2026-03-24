# CLAUDE.md

This file provides guidance to Claude Code when working in the **evidencell** repository.

## Project

evidencell is a LinkML-based knowledge base for cell type mapping evidence — linking classical cell types to modern transcriptomic atlas clusters. It combines a structured schema, a curated KB of mapping YAML files, Python tooling, and an ASTA-powered literature review workflow.

## Repo structure

```
schema/                  # LinkML schema (source of truth for KB structure)
kb/mappings/{region}/    # canonical, validated mapping graphs
kb/draft/{region}/       # work-in-progress; graduate to kb/mappings/ after just qc
inputs/deepsearch/       # ASTA deep research PDFs used as literature discovery input
inputs/taxonomies/       # taxonomy table slices (CSV/TSV) used for ingest-taxonomy
src/evidencell/          # all Python logic (validation, rendering, compliance, fetching)
workflows/               # multi-step curation orchestrators (see below)
.claude/hooks/           # pre-edit validation hook (runs before KB writes)
.claude/skills/          # bounded single-focus tasks, called interactively
.claude/agents/          # shared subagent personas (reserved; populate if needed)
references_cache/        # cached ASTA reference text for snippet provenance
justfile                 # thin task runner — all logic lives in src/evidencell/
WORKFLOW.md              # guide: which orchestrator to run, when, and with what inputs
```

## Orchestrators vs skills

**Multi-step curation workflows live in `workflows/` as orchestrators.** An orchestrator holds the control flow explicitly, spawns subagents with verbatim prompts, and stores state in files on disk. This is the pattern from `lit-review.md` — reliable because the orchestrator enforces sequencing and gates; subagents cannot skip steps they don't know exist.

**Single-focus bounded tasks live in `.claude/skills/`.** A skill is a prompt library for a constrained, well-defined action (review a PR, present a catalogue for weeding). Skills give Claude discretion over execution and are appropriate when the task is simple enough that that discretion does not matter.

**Do not implement a multi-step workflow as a skill.** Skills give Claude room to approximate the workflow, taking shortcuts and collapsing validation gates. For anything with sequential steps, conditional logic, or human review gates, write an orchestrator in `workflows/`.

There is no meta-orchestrator driving the whole pipeline. The human is the top-level coordinator: they run each phase orchestrator when ready, review the output at each gate, and proceed at their own pace. `WORKFLOW.md` documents what to run when.

## Code quality

- Run `just qc` before committing. This covers schema validation, ontology term checking, and snippet provenance.
- All Python logic longer than ~10 lines belongs in `src/evidencell/`, not in justfile shell blocks. `justfile` recipes are thin dispatchers.
- `ruff` for linting, `mypy` for type checking. Both must pass cleanly.
- `pytest` for unit tests. The ported KB examples are the test fixtures — if a schema or rendering change breaks them, CI catches it.

## Working with YAML and LinkML

- Always parse YAML with `yaml.safe_load()`. Never use shell `grep`, `sed`, or `awk` on YAML files.
- The pre-edit hook validates KB YAML before it reaches disk. If it rejects, fix the underlying issue — do not attempt to bypass the hook.
- When the hook reports an error, read the structured output, correct the YAML, and retry. The correction loop typically resolves in 1–2 iterations.
- Ontology terms (CL, UBERON, NCBITaxon) must exist in the OAK local databases. Look up terms with `runoak` before using them — do not invent IDs.
