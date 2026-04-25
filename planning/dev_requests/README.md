# planning/dev_requests/

Dev-request reports filed from curation-mode sessions when a workflow hits a
wall that requires dev work (new functionality in `src/`, a schema change, or
a tooling fix).

Filing a report here is the curation-mode escape hatch: it captures the
problem without making code or schema edits in a content-focused session.
Reports are reviewed later in a dedicated dev-mode session.

## When to file

File a dev-request report when any of the following is true during curation:

- A workflow step calls a function or recipe that does not exist, or that
  exists but does not accept the needed arguments.
- A KB validation error reveals a real gap in the schema (not a data-level
  fix). Schema edits must never be attempted directly in a curation session.
- A planned ingest, mapping, or reporting step is impossible given current
  tooling and would require new code to proceed.
- An orchestrator's instructions conflict with the state of the code or repo.

Do **not** file a report for data-level fixes, normal validation failures that
a content correction resolves, or ambiguity that human review can answer in
the current session.

## File name

```
planning/dev_requests/{YYYY-MM-DD}_{short-slug}.md
```

Use the current date (absolute, not relative) and a slug that names the
blocker — e.g. `2026-04-23_taxonomy_enrichment_merge.md`.

## Template

```markdown
# Dev request: {short description}

**Date filed**: {YYYY-MM-DD}
**Reporter**: {git user.email or name}
**Orchestrator / session context**: {which workflow, which step, what region / taxonomy / KB file}

## What is blocked

{One or two paragraphs describing the step that cannot proceed.}

## What is missing

{What functionality, schema element, or tooling does not exist and is required.}

## Proposed surface

{Where in the codebase the change likely belongs — module, function name,
schema class — and a sketch of the minimum viable change. A proposal, not a
final design; dev-mode review refines it.}

## What was tried

{The immediate workaround attempts, if any, and why they didn't work.
Relevant error messages, file paths, and commands.}

## References

{Links to relevant orchestrator steps, KB files, prior dev-requests, or
planning documents.}
```

## Lifecycle

1. **Filed** — report lands here in a curation-mode commit.
2. **Triaged** — reviewed in a later dev-mode session; accepted, declined, or
   deferred with a note.
3. **Resolved** — when the referenced dev work lands, the commit message
   should reference the dev-request filename. The report itself stays as the
   historical record; do not delete resolved reports.
