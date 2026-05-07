# Dev request: KB draft-tier removal — cleanup checklist

**Date:** 2026-04-29
**Status:** Planning — flagged in advance of the draft-tier removal so the cleanup is scoped.
**Severity:** Medium — touches several places that currently key on `kb/draft/` vs `kb/mappings/` or on `graph_meta.status == "draft"`.

---

## Context

The plan is to drop the `kb/draft/` vs `kb/mappings/` two-tier KB layout and write directly to a single canonical location (e.g. `kb/{region}/...yaml` or similar flat layout). The "draft → graduate" pipeline disappears.

This affects validation logic, workflow rules, and report rendering that currently distinguish the two states.

## Places that need updating when the transition happens

### Code

- **`src/evidencell/render.py`** — `extract_node_facts()` derives `status = "draft" if "draft" in str(graph_file) else "canonical"`. With no draft tier this becomes always-canonical. Either drop the field or hardcode "canonical".
- **`src/evidencell/validate.py:_target_class_for_kb_path`** — currently maps `kb/draft/{region}/*.yaml` → `CellTypeMappingGraph`. Adjust to whatever the new layout is.
- **`src/evidencell/paths.py`** — review for any `kb/draft` or `kb/mappings` references.
- **`.claude/hooks/validate_mapping_hook.py`** — region-detection logic walks back to `kb/draft/{region}` or `kb/mappings/{region}`. Update to new layout.

### Workflows

- **`workflows/gen-report.md`** — Section 1 (Report header) currently has:

  > If `graph_meta.status` is "draft", add the warning banner as bold inline
  > text (...): `**⚠ Draft mappings...**`

  Drop the conditional and the banner entirely. (Or keep a confidence-based banner — e.g. for any report whose primary candidate is below MODERATE — but that's a separate decision.)

- **`workflows/asta-report-ingest.md`** — writes new graphs to `kb/draft/{region}/`. Update target path.
- **`workflows/map-cell-type.md`** — references `kb/draft/{region}/` in PARAMS examples. Update.
- **`workflows/cite-traverse.md`**, **`workflows/evidence-extraction.md`** — likewise scan for path assumptions.

### Justfile

- `validate-draft`, `qc-draft`, `gen-report-draft` — these target `kb/draft/` directly. Either remove them or repoint at the new layout.

### CLAUDE.md / CLAUDE_dev.md

- Both currently document the two-tier layout (`kb/draft/{region}/` vs `kb/mappings/{region}/`). Update repo-structure section, writable-zones list, and any orchestrator descriptions that reference the draft tier.
- The "graduate via `just qc`" line in CLAUDE_dev.md becomes obsolete.

### Tests

- `tests/test_render.py` has `test_render_summary_draft_banner` and `test_render_summary_no_draft_banner_for_canonical`. Either remove or repurpose if the banner is repurposed (e.g. confidence-based).
- `tests/test_kb_examples.py` — strict-schema fixtures live in `kb/mappings/`. Repoint at the new canonical location.

### Existing content

- `kb/draft/{region}/*.yaml` — move to the new layout. One-shot migration script or `git mv`.
- `references/{region}/references.json` — the references store hangs off region; check it survives any region-layout change.

## Recommended sequencing

1. Decide and document the new canonical layout (single PR, no code changes).
2. Update schema/code (validate dispatch, render.py, hook) to support both old and new layouts during the transition.
3. Move content; remove old paths from code.
4. Update workflows + CLAUDE.md + CLAUDE_dev.md.
5. Drop the dual-layout support code.

This staged approach lets KB content move without breaking writers mid-flight.
