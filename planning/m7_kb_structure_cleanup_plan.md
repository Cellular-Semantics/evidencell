# M7: KB Structure Cleanup — Implementation Plan

> Detailed plan generated from [Claude Code session plan](./../.claude/plans/composed-prancing-hare.md).

## Context

`kb/` currently mixes graph YAML (the actual knowledge base) with research artifacts (cite-traverse outputs, evidence extraction intermediates), references infrastructure (`references.json`), and reports. This makes the KB confusing to navigate and blocks clean onboarding. The ROADMAP M7 proposal (lines 675-753) describes the target state. This plan turns that proposal into a safe, lossless execution sequence.

**Branch**: `hippocampus_gaba` has uncommitted untracked files that must be accounted for:
- `annotation_transfer/data/GSE124847/` — 2 data files (gitignore; large GEO downloads, re-fetchable)
- `kb/hippocampus/traversal_output/` — 13 files from earlier pipeline runs (MUST be moved to `research/`)

**Two PRs, not one**: Phase 1 (directory restructure + code updates) is one PR. Phase 2 (graph renaming/merging) is a separate future PR requiring curator content review.

---

## Target directory layout

```
kb/
  draft/{region}/*.yaml          # work-in-progress graph YAML only
  mappings/{region}/*.yaml       # graduated graph YAML only
references/{region}/
  references.json                # shared quote store (was sibling of graph YAML)
research/{region}/
  field_mapping.json             # taxonomy ingest config
  discovery_candidates.json      # map-cell-type output
  evidence_gaps.md               # working artifact
  cite_traverse/                 # cite-traverse run outputs
  evidence_extraction/           # evidence-extraction run outputs
  {run_id}/                      # dated traversal outputs
reports/{region}/
  *.md                           # human-readable reports
```

---

## Step 1: Commit uncommitted work on current branch

Before restructuring, commit the untracked files so nothing is lost.

- `annotation_transfer/data/GSE124847/` — add `annotation_transfer/data/` to `.gitignore`
- `kb/hippocampus/traversal_output/` — these move to `research/` in Step 2, so commit them first as-is, then `git mv` in the restructure commit

---

## Step 2: Move files with `git mv` (single commit)

All moves in one atomic commit. No content changes.

### Hippocampus — from `kb/draft/hippocampus/`

| Source | Destination |
|--------|-------------|
| `kb/draft/hippocampus/references.json` | `references/hippocampus/references.json` |
| `kb/draft/hippocampus/field_mapping.json` | `research/hippocampus/field_mapping.json` |
| `kb/draft/hippocampus/discovery_candidates.json` | `research/hippocampus/discovery_candidates.json` |
| `kb/draft/hippocampus/evidence_gaps.md` | `research/hippocampus/evidence_gaps.md` |
| `kb/draft/hippocampus/cite_traverse/*` (11 files) | `research/hippocampus/cite_traverse/*` |
| `kb/draft/hippocampus/evidence_extraction/*` (5 files) | `research/hippocampus/evidence_extraction/*` |
| `kb/draft/hippocampus/reports/olm_hippocampus_summary.md` | `reports/hippocampus/olm_hippocampus_summary.md` |
| `kb/draft/hippocampus/20260409_hippocampus_report_ingest.yaml` | `research/hippocampus/20260409_hippocampus_report_ingest.yaml` |

### Hippocampus — from `kb/hippocampus/` (untracked traversal outputs)

| Source | Destination |
|--------|-------------|
| `kb/hippocampus/traversal_output/20260409_hippocampus_cite_traverse/*` | `research/hippocampus/20260409_hippocampus_cite_traverse/*` |
| `kb/hippocampus/traversal_output/20260409_hippocampus_report_ingest/*` | `research/hippocampus/20260409_hippocampus_report_ingest/*` |

### Files that STAY in `kb/`

- `kb/draft/hippocampus/hippocampus_GABA_stratum_oriens_stubs.yaml`
- `kb/draft/BG/GPi_shell_neuron.yaml`
- `kb/draft/BG/GPi_shell_neuron_Mmus.yaml`
- `kb/draft/cerebellum/CB_MLI_types.yaml`
- `kb/draft/cerebellum/CB_PLI_types.yaml`
- `kb/mappings/` (empty, placeholder)

### Verification after move

- `find kb/ -type f` → only `.yaml` files
- `find references/ research/ reports/ -type f` → all moved files present
- `git diff --stat` → only renames, no content changes

---

## Step 3: Create `src/evidencell/paths.py`

New module — single source of truth for path conventions:

```python
def repo_root() -> Path              # walk up from __file__ looking for schema/
def region_from_graph(graph_file) -> str   # kb/draft/{region}/foo.yaml → region
def refs_path_for_graph(graph_file) -> Path  # → references/{region}/references.json
def refs_path_for_region(region) -> Path
def reports_dir_for_region(region) -> Path
def research_dir_for_region(region) -> Path
```

### Critical files to modify

**`src/evidencell/render.py`** — 3 changes:
- Line 1203: `graph_file.parent / "references.json"` → `refs_path_for_graph(graph_file)`
- Line 1274: same pattern → same fix
- Report output default dir: use `reports_dir_for_region()`

**`.claude/hooks/validate_mapping_hook.py`** — 4 changes:
- Lines 58-62: `is_report` check — remove `"/kb/" in str(file_path)` requirement; reports now at `/reports/{region}/*.md`
- Line 79: `refs_path` derivation — use `refs_path_for_region(file_path.parent.name)` for reports, `refs_path_for_graph(file_path)` for YAML
- Lines 86-101: KB node discovery for report validation — scan `kb/draft/{region}/` and `kb/mappings/{region}/` instead of navigating up from report dir
- Line 57: `is_yaml` check `"/kb/" in str(file_path)` — unchanged (correct)

**`src/evidencell/validate.py`** — line 431: `term_index_path = refs_path.parent / "term_index.json"` — will resolve correctly since `refs_path` is now `references/{region}/references.json` and `term_index.json` should live alongside it. No change needed.

---

## Step 4: Update `.gitignore`

Remove:
```
kb/mappings/**/traversal_output/
kb/**/reports/*_facts.json
```

Add:
```
reports/**/*_facts.json
annotation_transfer/data/
```

---

## Step 5: Update workflow orchestrators

All `.md` files in `workflows/` that reference `kb/draft/{region}/references.json`:

| Orchestrator | Key changes |
|---|---|
| `asta-report-ingest.md` | ~20 refs to `kb/draft/{region}/references.json` → `references/{region}/references.json`; output_dir patterns → `research/{region}/` |
| `cite-traverse.md` | Default output_dir examples → `research/{region}/cite_traverse/` |
| `evidence-extraction.md` | output_dir examples → `research/{region}/evidence_extraction/` |
| `gen-report.md` | references.json location; output_dir default → `reports/{region}/` |
| `ingest-taxonomy.md` | field_mapping.json → `research/{region}/field_mapping.json`; stubs still → `kb/draft/` |
| `map-cell-type.md` | discovery_candidates.json → `research/{region}/` |
| `lit-review.md` | output_dir patterns |

---

## Step 6: Update documentation

- **`CLAUDE.md`** — repo structure diagram (lines 12-24): add `references/`, `research/`, `reports/`
- **`.claude/anti-hallucination-hooks.md`** — path references in architecture diagram and validation source descriptions
- **`WORKFLOW.md`** — inputs table, anti-hallucination section paths
- **`ROADMAP.md`** — mark M7 Phase 1 as complete
- **`README.md`** — update any repo structure references

---

## Step 7: Update tests

**`tests/test_hook_integration.py`**:
- `_make_refs_and_yaml()` (line 160): currently creates `tmp_path/kb/draft/` with `references.json` as sibling. Must create `tmp_path/references/{region}/references.json` and mock or configure `paths.repo_root()` to return `tmp_path`
- `_make_refs_and_md()` (line 236): same — set up `tmp_path/reports/{region}/` and `tmp_path/references/{region}/`

**`tests/test_render.py`**:
- Line 778 (`kb_dir = tmp_path / "kb" / "draft" / "myregion"`): must also create `tmp_path/references/myregion/references.json` and ensure render.py finds it

**`tests/test_validate.py`**: No changes — `check_quote_keys` and `check_ref_pmids` receive `refs_path` as explicit parameter.

**New: `tests/test_paths.py`**: Test `region_from_graph()`, `refs_path_for_graph()` with various inputs including edge cases (BG, cerebellum, nested paths).

---

## Step 8: Verification

1. `just test` — all tests pass
2. `just qc-draft hippocampus` — draft KB validates
3. `uv run python -m evidencell.render summary kb/draft/hippocampus/hippocampus_GABA_stratum_oriens_stubs.yaml` — renders successfully, finds references.json at new location
4. `find kb/ -type f | grep -v '.yaml'` — empty (only YAML in kb/)
5. Manually trigger the hook by editing a draft YAML — hook finds references.json

---

## Flagged for future review (NOT in this PR)

- **`research/hippocampus/20260409_hippocampus_report_ingest.yaml`** vs `research/hippocampus/20260409_hippocampus_report_ingest/proposed_kb_hippocampus.yaml` — likely duplicates; check and deduplicate
- **Graph renaming** (Phase 2): `hippocampus_GABA_stratum_oriens_stubs.yaml` → `hippocampus_WMBv1.yaml`, cerebellum merge, BG renames — separate PR with curator review
- **Graduation criteria + `just graduate` recipe** — Phase 3 of M7, separate PR
