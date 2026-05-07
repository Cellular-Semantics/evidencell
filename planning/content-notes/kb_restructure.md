# KB file structure — pending curation changes

---

## Rename and consolidate graphs

Current graph files use ad-hoc names. Target names:

| Current | Target |
|---|---|
| (hippocampus graph) | `hippocampus_WMBv1.yaml` |
| (cerebellum graph) | `cerebellum_WMBv1.yaml` |
| (basal ganglia HMBA graph) | `BG_HMBA.yaml` |
| (basal ganglia WMBv1 graph) | `BG_WMBv1.yaml` |

Note: update any orchestrator or skill that hardcodes current filenames after rename.

---

## Flatten kb/ directory

Remove the `draft/` / `mappings/` split. Single `kb/` directory; `just qc` + human
sign-off as the quality gate. See ROADMAP.md `#kb` section for the infrastructure
side of this task.
