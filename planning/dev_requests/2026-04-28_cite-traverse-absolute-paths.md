# Dev request: cite-traverse extraction writes absolute paths

**Date:** 2026-04-28
**Severity:** Medium — committed config files contain machine-specific paths; reproducibility is broken across machines.

---

## What's wrong

Files under `research/hippocampus/cite_traverse/extraction/` contain hardcoded absolute paths in their JSON contents:

- `extraction_manifest_*.json` (~10 files) — `refs_file: /Users/do12/Documents/GitHub/evidencell/references/hippocampus/references.json`
- `node_contexts.json` — multiple `kb_file` and `refs_file` entries with the same prefix

The path prefix `/Users/do12/Documents/GitHub/evidencell/` does not even match the **current** repo location (`/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/`). It refers to a different (presumably earlier) checkout. So the paths are both absolute AND stale.

These files are tracked in git, which means anyone cloning the repo on a different machine cannot reproduce or rerun the extraction without rewriting them.

## Where the producer lives

These files are written by the cite-traverse workflow's extraction step. The producer should be in `src/evidencell/` or under a skill in `.claude/skills/cite-traverse/`. (Find via `grep -rn 'extraction_manifest' src/ .claude/`.)

## Fix

Producer should write repo-relative paths (e.g. `references/hippocampus/references.json`) instead of absolute paths. Consumers should resolve relative to the repo root using a `_repo_root()` walker (looking for `pyproject.toml`) — same pattern as the new bulk-correlation `correlate.py` scripts.

## Cleanup

After the producer is fixed, regenerate the existing files (or rewrite them in place with `sed` against the prefix). They are research artefacts so a one-time bulk rewrite is acceptable.

## Verification

- After fix: `grep -rn '/Users/' research/` returns no hits
- Cite-traverse can be re-run cleanly on a fresh clone
