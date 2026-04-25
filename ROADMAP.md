# evidencell Roadmap

**Format**: GFM task lists. `- [ ]` pending · `- [x]` done · `- [~]` in progress.
Priority: items are listed highest-priority-first within each section; **bold** = blocks other work.

Archive of prior roadmap with full milestone write-ups: [planning/ROADMAP_archive_2026-04.md](planning/ROADMAP_archive_2026-04.md)

---

## Tag glossary

| Tag | Scope |
|---|---|
| `#schema` | LinkML schema, enum values, semantic lint rules |
| `#kb` | KB file structure, naming conventions |
| `#content` | KB YAML content — updates needed when schema or file structure changes |
| `#lit` | Literature curation workflows generally |
| `#at` | Annotation transfer pipeline and report improvements |
| `#workflow-design` | Orchestrator architecture, data contracts |
| `#qc` | Validation hooks, compliance scoring, test coverage |
| `#community` | Biologist review tooling, compliance scoring, public access |
| `#infrastructure` | Packaging, CI, Docker, code/content separation |
| `#map-cell-type` | `workflows/map-cell-type.md` orchestrator |
| `#asta-ingest` | `workflows/asta-report-ingest.md` orchestrator |
| `#cite-traverse` | `.claude/skills/cite-traverse.md` (or current orchestrator) |
| `#evidence-extraction` | `workflows/evidence-extraction.md` orchestrator |
| `#survey` | `survey.md` orchestrator (not yet built) |
| `#targeted-search` | `targeted-search.md` orchestrator (not yet built) |
| `#gen-report` | `workflows/gen-report.md` + `render.py` |
| `#ingest-taxonomy` | `workflows/ingest-taxonomy.md` + `taxonomy_db.py` |
| `#annotation-transfer` | `workflows/annotation-transfer.md` orchestrator |

Milestones: `@Allen` (Allen Institute deliverable, date TBC) · `@BICAN` (BICAN deliverable, date TBC)

---

## Schema `#schema`

- [~] **Taxonomy rank encoding** — `taxonomy_rank: int` on `CellTypeNode` + `TaxonomyNodeList` `#ingest-taxonomy` `#map-cell-type`
  - [x] Schema fields + WMB YAML rank assignments (v0.7.1)
  - [x] `find_candidates()` accepts rank or level
- [ ] Review v0.8.0 schema additions — `PropertySource.source` rename candidate, WEAK vs PARTIAL, OVERLAPS vs PARTIAL_OVERLAP, CAS-specific fields on core `CellTypeNode`
- [ ] Marker/assay consistency — split `detected_molecule` + `assay_method`, or add SC1 lint check `#qc`
- [ ] Dual MBA + UBERON anatomy at ingest — annotate classical nodes with both IDs; shared `annotate-anatomy` skill `#asta-ingest` `#survey`
- [ ] Iterative mapping infrastructure — liberal initial writes, confidence upgrade, pruning with provenance trail, batch region-level review `#map-cell-type`
- [ ] Lint: marker type vs assay method in pre-edit hook (SC1) `#qc`
- [ ] Lint: flag mapping info in classical node notes (SC2) `#qc`
- [ ] Convention: no data in YAML comments (SC3) — add to CLAUDE.md

---

## KB structure `#kb`

- [ ] **Flatten kb/ — remove draft/mappings split**: single `kb/` directory; `just qc` + human sign-off as the quality gate `#content`
- [ ] **Rename and consolidate graphs**: `hippocampus_WMBv1.yaml`, `cerebellum_WMBv1.yaml`, `BG_HMBA.yaml`, `BG_WMBv1.yaml` `#content`
- [ ] Wire remaining orchestrators to `references/`, `research/`, `reports/` at repo root `#asta-ingest` `#gen-report` `#evidence-extraction`
- [ ] Orchestrators write directly into region graph (read-merge-write); ephemera to `research/` `#asta-ingest` `#evidence-extraction` `#content`
- [ ] Self-contained KB graphs — inline snippets, `PublicationReference` metadata, ingest provenance (see [planning/schema_self_contained_references.md](planning/schema_self_contained_references.md)) `#content`

---

## Taxonomy DB queries `#ingest-taxonomy` `#map-cell-type`

- [ ] Update `query_by_region`, `query_by_nt`, `query_by_nt_propagated` to accept `taxonomy_rank`
- [ ] QC smoke tests: `--help` probes for new `taxonomy_ops` CLI subcommands `#qc`
- [ ] Verify supertype-level expression weighted mean logic in `test_taxonomy_ops.py` `#qc`

---

## Multi-taxonomy DB `#ingest-taxonomy` `#schema` `#map-cell-type`

Currently one taxonomy per DB file (`{taxonomy_id}.db`). With multiple atlases (WMBv1,
HMBA, future species), cross-taxonomy queries — especially for annotation transfer edges —
require either joining across DBs or consolidating into one.

**Core tension**: a single DB supports cross-taxonomy joins and keeps annotation transfer
edges queryable; separate DBs are simpler to ingest, version, and swap out independently.
Lean toward **single DB, partitioned by taxonomy_id** — the `taxonomy_id` column already
exists on every node row, so queries within a single atlas work unchanged.

- [ ] **Decide: single shared DB vs per-taxonomy DBs** — document the chosen model and its
  implications for `taxonomy_db_path()`, `build_from_yaml()`, and the skill `#workflow-design`
- [ ] If single DB: update `taxonomy_db_path()` to return a shared path (e.g.
  `kb/taxonomy/taxonomy.db`); `build_from_yaml()` upserts by taxonomy_id rather than
  dropping all nodes
- [ ] Cross-taxonomy candidate queries — `find_candidates()` needs a `taxonomy_ids` filter
  so callers can scope to one atlas or query across several `#map-cell-type`
- [ ] Cross-taxonomy annotation transfer edges in `MappingEdge` must explicitly record
  `source_taxonomy_id` and `target_taxonomy_id`; update schema + query skill `#schema`
- [ ] `reingest()` in `taxonomy_ops.py` must not clobber nodes from other taxonomies when
  updating a single atlas `#ingest-taxonomy`
- [ ] Update `_meta` table to track build timestamps per taxonomy_id (key:
  `taxonomy_built_at:{taxonomy_id}`) `#ingest-taxonomy`

---

## Literature curation `#lit`

- [ ] **Survey/targeted workflow split** — `survey.md` + `targeted-search.md` orchestrators; cite-traverse → skill; KB gap flags on nodes `#survey` `#targeted-search` `#cite-traverse` `#workflow-design` (see [planning/workflow_architecture_design.md](planning/workflow_architecture_design.md))
- [ ] Lit pipeline file schemas — Pydantic models for summary/refs/manifest; validated handovers between steps `#cite-traverse` `#evidence-extraction` `#workflow-design`
- [ ] Workflow handover contracts — handover inventory, schema coverage map, user-facing gate terminology `#workflow-design`
- [ ] Lit quality improvements — contextual retrieval for Round 2 papers, venue/citation quality signals, domain relevance pre-filters `#cite-traverse`

---

## Annotation transfer `#at`

- [ ] **OLM hippocampus**: KB import orchestrator for GSE124847 → WMBv1 AT results (branch `at/olm-hippocampus`) `#annotation-transfer` `#content`
- [ ] **PV hippocampus**: GSE142546 Que 2021 PV patch-seq AT (branch `at/pv-hippocampus`; awaiting SRA reprocessing) `#annotation-transfer` `#content`
- [ ] AT orchestrator: use `best_mapping_rank` throughout `#annotation-transfer` `#map-cell-type`
- [ ] AT-before-edges mapping loop — triage-first ordering, compute preflight gate, sub-node creation rule `#map-cell-type` `#annotation-transfer` (see [planning/adaptive_mapping_loop_design.md](planning/adaptive_mapping_loop_design.md))
- [ ] Report: assess all rank-0 nodes collectively when AT resolves above rank 0 `#gen-report`
- [ ] Workflow: agent-driven sub-node creation when source evidence separates subtypes `#map-cell-type`
- [ ] F1 heatmap visualisation in AT output / gen-report `#gen-report` `#annotation-transfer`
- [ ] Report: make classical-type provenance explicit for genetically/morphologically defined source data `#gen-report`

---

## Workflow design `#workflow-design`

- [ ] **`map-cell-type.md` progressive rewrite** — direct KB writes; biologist report review is the main gate; remove per-edge curator gates except reference weeding `#map-cell-type`
- [ ] Curation mode vs dev mode — review workflow mode split (WORKFLOW.md / CLAUDE.md routing)

---

## Community feedback `#community`

- [ ] Biologist report review workflow — structured path from feedback → KB change with provenance `#gen-report`
- [ ] Compliance scoring in `src/evidencell/compliance.py`
- [ ] `celltype-mapping-pr-review` skill — rubric-based KB PR review
- [ ] GitHub Actions feasibility spike — hosted orchestrator execution on PR trigger `#infrastructure`

---

## Infrastructure `#infrastructure`

- [ ] Code/content separation — `content/hmba-mouse` branch; `main` fixture-only KB; `just test` green on main `#content`
- [ ] Docker setup — `docs/SETUP.md`, `just docker-setup`, `.env.example`

---

## Recently completed

Brief log — see [planning/ROADMAP_archive_2026-04.md](planning/ROADMAP_archive_2026-04.md) for full write-ups.

- [x] M0–M4: schema hardening, repo bootstrap, lit pipeline, mapping hypotheses, report generation
- [x] AT: OLM hippocampus end-to-end (GSE124847 → WMBv1); schema v0.6.0 (AnatomicalLocation + CellCompartment)
- [x] M8 Ph1: taxonomy SQLite DB + YAML ingest (CCN20230722); `taxonomy_db.py` `#ingest-taxonomy`
- [x] S1 (partial): `taxonomy_rank` schema + WMB rank assignments + `find_candidates` rank support
- [x] Taxonomy update ops: `add-expression`, `reingest` with field ownership (`taxonomy_ops.py`); `map-cell-type.md` Step 2b expression enrichment `#ingest-taxonomy` `#map-cell-type`
- [x] CAS taxonomy ingest: CTX-HPF CS202106160 + cross-taxonomy AT edges `#ingest-taxonomy` `#annotation-transfer`
- [x] Pre-commit hook: strict schema validation on all staged KB YAML `#qc`
- [x] Provenance schema unification (v0.8.0): `ElectrophysiologyProfile` + `MorphologyProfile` classes; `AnatomicalLocation.sources`; removed flat `ephys_sources`/`morphology_sources`/`location_sources` `#schema` `#content`
