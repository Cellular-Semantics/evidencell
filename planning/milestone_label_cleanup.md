# Cleanup: remove milestone labels from user-facing docs

## Problem

Internal milestone labels (M1, M2, M3, ...) from `ROADMAP.md` have bled into
workflow orchestrators and `WORKFLOW.md`. These labels are meaningless to users
and agents running the workflows — they're dev planning shorthand, not
user-facing concepts.

An agent executing `map-cell-type.md` that reads "paper catalogue from M2" has
to guess what M2 means. It should say "paper catalogue from cite-traverse".

## Where milestone labels belong

- `ROADMAP.md` — yes, this is the milestone tracker
- `planning/` docs — yes, internal planning context

## Where they don't belong

### Workflow orchestrators (`workflows/*.md`)

| File | Line | Current | Replace with |
|---|---|---|---|
| `ingest-taxonomy.md` | 113 | "potentially useful for M3" | "potentially useful for map-cell-type" |
| `map-cell-type.md` | 12 | "from M1 ingestion or..." | "from ingest-taxonomy or..." |
| `map-cell-type.md` | 180 | "paper catalogue from M2" | "paper catalogue from cite-traverse" |
| `annotation-transfer.md` | 13 | "in M4 reports" | "in gen-report output" |
| `annotation-transfer.md` | 112 | "see M8 in..." | "see ROADMAP.md M8 for..." (or describe the actual dependency) |

### `WORKFLOW.md`

The milestone status table (lines 7-16) is fine — it's a status tracker.

The overview table (line 34) has a "Milestone" column. Options:
1. **Remove the column** — orchestrators are mature enough that grouping by
   milestone adds no clarity. The "When to run" column already explains purpose.
2. **Replace with a "Phase" or "Stage" column** using plain labels like
   "Discovery", "Literature", "Mapping", "Reporting", "Evidence transfer" —
   meaningful without consulting the roadmap.

The inputs table (line 73) says "see M8" — replace with "see ROADMAP.md § M8"
or describe the dependency inline.

The workflow diagram (line 118) says "extract structured facts (M4)" — replace
with "extract structured facts (gen-report)".

## Principle

Orchestrators and WORKFLOW.md are **user-facing operational docs**. They should
be self-contained — readable without consulting the roadmap. Milestone labels
are cross-references that force the reader to look up context elsewhere.

Rule: if a milestone label appears outside `ROADMAP.md` or `planning/`, replace
it with the plain-language concept it refers to (usually the orchestrator name
or the workflow phase).
