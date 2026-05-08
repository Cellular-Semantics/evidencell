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

## ~~Flatten kb/ directory~~ — DONE

Implemented on branch `reorg`: cell-type graphs live in `kb/graphs/{region}/`;
`just qc` + human PR review is the quality gate. ROADMAP `#kb` ticked.
