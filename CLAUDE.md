# CLAUDE.md — evidencell curation guide

This is the **default** guidance loaded by Claude Code in this repository. It
describes the curation workflow: which orchestrator to run, when, and with what
inputs. Curation work — KB YAML, references, reports, research artifacts, and
dev-request reports — is in scope here.

Dev work on `src/`, `schema/`, or the `justfile` is out of scope by default; see
**Curation mode** below and `CLAUDE_dev.md` for the dev-mode companion.

---

## Curation mode

Writable zones in this session:

- `kb/graphs/**`, `kb/taxonomy/**` — KB YAML under pre-edit validation
- `references/**` — reference stores under ingest-path governance
- `reports/**` — generated reports under pre-edit validation
- `research/**` — research artifacts (field mappings, summaries, traversals)
- `planning/dev_requests/**` — historical dev-request reports (new requests go to GitHub issues; see "Hitting a wall" below)
- `planning/content-notes/**` — KB YAML curation task notes (file-rename tasks, AT import checklists, etc.)

Out of scope: `src/`, `schema/`, `justfile`, `.claude/`, and `workflows/`.
The pre-edit hook rejects writes to these paths in curation mode. This is a deliberate barrier against
accidental code/schema edits during curation sessions — schema fixes as a
response to a validation error are a common and dangerous anti-pattern. Code
and schema changes land through normal dev-mode sessions and PR review
against `main`, not through curation workflows.

Before starting curation work, check `planning/content-notes/` for any pending notes
about the target region or workflow — these track KB file rename tasks, AT import
checklists, and other curation-side TODOs that don't belong on the main ROADMAP.

### Hitting a wall

When a workflow step needs functionality that doesn't yet exist in `src/`, or
when a validation error reveals a real schema gap, do **not** attempt to fix
code or schema directly. Instead:

1. **File a dev-request GitHub issue** on `Cellular-Semantics/evidencell`
   describing: what orchestrator step is blocked, what's missing, a
   proposed surface (what would need to be added or changed and where),
   and what was tried. Use the `$CELLSEM_GH_TOKEN` PAT pattern documented
   in `CLAUDE_dev.md` § Dev request workflow. Legacy markdown reports
   under `planning/dev_requests/` remain as historical record but are no
   longer the filing path.
2. **Or load `CLAUDE_dev.md`** explicitly when you're authorised to do dev
   work this session. Schema changes in particular MUST be discussed and
   reviewed before implementation — they are occasionally legitimate (new
   taxonomy import, a novel mapping scenario) but almost never the right
   response to a validation error.

---

## Milestone status

| Milestone | Description | Status |
|---|---|---|
| M1 | Taxonomy ingest → atlas cluster stubs | **Complete** |
| M2 | Literature retrieval pipeline (ASTA ingest, cite-traverse, evidence extraction) | **Complete** |
| M3 | Mapping (property comparison, edge YAML, confidence assessment) | **Complete** |
| M4 | Report generation (summary + drill-down, LLM synthesis, anti-hallucination hooks) | **Complete** |
| M5 | Annotation transfer evidence | **In progress** — pipeline implemented, orchestrator pending |
| M7 | KB structure cleanup (Phase 1: directory restructure) | **Complete** |
| M8 | Taxonomy reference DB — compact YAML + SQLite query index | **In progress** — Phase 1 complete; Phase 2–3: KB graphs use minimal taxonomy ref stubs |
| S1 | Taxonomy rank encoding — integer ranks replace hardcoded level names | **Complete** — schema, ingest, DB, find-candidates, map-cell-type all use integer ranks |

---

## How to run a workflow

When asked to run a workflow, open the referenced orchestrator in `workflows/` and execute
its steps in order. The orchestrator is the authority — do not plan independently or
research prerequisites that the orchestrator already addresses. Use the skills and tools
it references. Stop at steps marked `[GATE]` and present results for human review before
proceeding.

**Subagent steps MUST be dispatched, not run inline.** When a workflow step says "spawn
a subagent" (synthesis subagent, validation subagent, drill-down subagent, etc.), it MUST
be dispatched via the Agent tool with an explicit `subagent_type`. Executing the prompt
inline in the orchestrator's own context window:

- defeats the context isolation the workflow is testing — the subagent prompt is the
  product, and it must be validated under the conditions it will actually run in
  production (fresh context, no parent history);
- silently incorporates prior conversation context, prior drafts, and parent-session
  hand-holding into the result, producing output that won't reproduce when a fresh
  production session is invoked;
- masks prompt deficiencies (ambiguities, missing instructions, friction points) that
  would surface immediately in a context-isolated dispatch.

The only exception is when the user has explicitly asked for an inline iteration to
debug the prompt itself. Default behaviour is always dispatch via Agent. If you find
yourself reading the subagent's input files in the parent context to "help" the
subagent reason, you are skipping the isolation — stop, dispatch, and let the
subagent read on its own.

**"Orchestrator" = the Claude session that opened the workflow.** In production this is
normally the top-level user-facing Claude Code session. If you yourself were dispatched
as a subagent by a harness (test runs, multi-node batching, etc.) and Agent-tool
dispatch is not available in your environment, **abort with a clear diagnostic — do not
inline.** The dispatch rule exists to keep subagent contexts clean, and silent
inline fallback produces results that won't reproduce when the workflow runs from
a top-level session. Diagnostic template: *"workflow Step N requires Agent-tool
dispatch; this environment does not expose it. Re-invoke from a Claude session with
Agent-tool access, or pass an explicit `allow_inline=true` parameter (debug-only
override)."*

---

## KB data management principles

### Properties live on nodes; edges compare

All biological properties (markers, NT type, anatomy, sex ratio, expression
profiles) are stored on `CellTypeNode` entries. Mapping edges document how
properties on two nodes compare — they never introduce new property assertions.
This means the mapper always sees a node's full property set regardless of which
mapping graph references it.

### Taxonomy reference YAML is canonical for atlas properties

Atlas node properties belong in `kb/taxonomy/{id}/*.yaml`, not on stub nodes
inside mapping graphs. Mapping graphs reference taxonomy nodes by accession;
stubs carry only: `id`, `name`, `definition_basis`, `taxonomy_id`,
`cell_set_accession`.

**Atlas expression is not stored in YAML** (#189). Mean expression per atlas
node is read on demand from the MapMyCells precomputed-stats HDF5 and cached
in the taxonomy SQLite DB (see "Atlas expression" below). Leftover
`precomputed_expression` blocks on stub nodes in a few `kb/graphs/` files are
dead data — nothing reads them — and can be dropped in a content PR.

### Taxonomy update operations

- **`just reingest`** — re-ingest from source JSON while preserving enrichment
  fields (`electrophysiology`, `morphology`, curated markers, etc.).
  Nodes removed in the new source are flagged for review, not silently dropped.
  Use `just reingest-dry` to preview changes. Re-ingest cannot lose
  expression: none is stored in YAML.

Field ownership is explicit: `INGEST_FIELDS` are replaced from the new source,
`ENRICHMENT_FIELDS` are preserved from old data. Both sets are declared in
`src/evidencell/taxonomy_ops.py`.

The old flush-and-replace ingest (`just ingest-taxonomy-db`) still works but
does NOT preserve enrichments. Use `just reingest` when taxonomy nodes have
post-ingest enrichments.

### Atlas expression (on-demand cache)

`TaxonomyDB.expression(symbols, accessions=…, ranks=…)` in
`src/evidencell/taxonomy_db.py` is the one accessor for atlas expression;
`find-candidates`, `emit-stage-b`, `refresh-expression`,
`refresh-property-comparisons` and the `at_blind` audit all go through it.
A gene not yet cached is read (one column, all clusters) from the stats HDF5
and written to the DB's `node_expression` / `expression_genes` tables;
non-leaf values are means of their rank-0 descendants, weighted by the stats
file's `n_cells`. In the WMBv1 stats file `n_cells` is 1 for every cluster, so
WMB supertype/subclass values are **plain (unweighted) averages of cluster
means** — the same as the former YAML values, but not cell-weighted. Details
in `src/evidencell/expression_cache.py`.

- `just build-taxonomy-db` creates the cache tables **empty**; they refill on
  use. The cache is keyed by Ensembl ID. A new stats release (different
  sha256) drops it, and is refused until `gene_ids.tsv.gz` is refreshed for
  that file (its column indices would otherwise be untrusted).
- **Gene identity (#216).** Marker names resolve to the stats file's genes
  through the `genes` / `gene_synonyms` tables, loaded by `build-taxonomy-db`
  from the committed `kb/taxonomy/{taxonomy_id}/gene_ids.tsv.gz` (Translator
  NodeNormalization + Name Resolver; refresh with `just build-gene-ids`).
  A classical marker's `ncbi_gene_id` pins its gene (a gene of another
  species reaches the taxonomy through its official symbol only); one
  without an ID is `NO_GENE_ID` and not resolved by name. A pin is one
  marker's gene, never applied to another marker by shared wording. Atlas
  metadata names resolve by exact symbol, case-insensitive symbol, or a
  synonym exactly one gene claims. See `src/evidencell/gene_identity.py`.
- **Fails closed**: an uncached gene with no stats file stops the run with
  `just fetch-mapmycells {taxonomy_id}`. There is no metadata-only fallback.
- Names that can't be measured are recorded and reported — never a silent
  `{}`: `NO_ENSEMBL_MAPPING` (no gene of the taxonomy has that name),
  `AMBIGUOUS_SYMBOL` (several do), `NO_GENE_ID` (a classical marker with
  no `ncbi_gene_id`), `PIN_NOT_IN_TAXONOMY` (its gene isn't in the
  taxonomy, nor its official symbol) or `CONFLICTING_PINS` (markers of one
  node share a name but not a gene). Set the marker's gene per
  `docs/marker_gene_ids.md`.
- Marker scoring in `find-candidates` uses expression only. The atlas
  node's metadata marker lists are cross-checked and disagreements reported
  as `marker_discrepancies` (carried into Stage B property-comparison notes).
- `just warm-expression-cache {taxonomy_id}` optionally pre-loads every
  marker named on a KB classical node.

**Keep `WORKFLOW.md` current.**

### Skills reference

| Skill | When to invoke |
|---|---|
| `query-taxonomy-db` | Any taxonomy candidate search, field coverage check, or DB exploration. **Do not read taxonomy YAML files directly for query purposes** — the DB is the query interface; YAML is the edit interface. Atlas expression is not in YAML: read it through `TaxonomyDB.expression()`, which loads uncached genes from the MapMyCells stats file into the DB's `node_expression` table on demand (#189). Querying `node_expression` directly only sees genes already cached. |
| `gene-id-curation` | Gene or protein name as a source writes it + taxon → NCBI Gene ID and official symbol (or why it names no single gene). Generic; how its result goes into the KB is `docs/marker_gene_ids.md`. |
| `cl-mapping` | Setting, checking or acting on a node's `cl_mapping` (`.claude/skills/cl-mapping.md`): CL term search, EXACT / BROAD / RELATED, what each means for `cl-term-request`. |
| `term-grounding` | Writing any other ontology term into KB YAML (`.claude/skills/term-grounding.md`): which ontology each field takes, which tool finds it, how to pass the hook. |
| `retrieve-dataset` | Downloading and inspecting an expression dataset (h5ad, RDS, loom, mtx). | Any time an orchestrator is added, removed, renamed, or its status changes, update `WORKFLOW.md` in the same commit. The overview table, inputs table, and typical workflow diagram must all reflect the current state. Never leave a stale status entry or a duplicate section.
### Provenance

The schema provides `PropertySource` as a general provenance record: `ref`
(PMID or DOI), `method`, `scope`, `snippet`/`quote_key`, `notes`.

As of v0.8.0, provenance is nested on property objects rather than in
separate per-property source fields. Each property carries its own `sources`
list:

- `electrophysiology.sources` — on `ElectrophysiologyProfile`
- `morphology.sources` — on `MorphologyProfile`
- `anatomical_location[].sources` — on each `AnatomicalLocation` entry
- `nt_type.sources` — on `NeurotransmitterType`
- `GeneDescriptor.sources` — as `MarkerSource` (adds `marker_type`)

This gives natural scoping (each source is attached to the assertion it
supports), clean RDF mapping (blank nodes, no reification needed), and
eliminates the former per-property field proliferation (`ephys_sources`,
`morphology_sources`, `location_sources` — all removed in v0.8.0).

`definition_references` (list of PMID/DOI strings) is retained as a
flat field — these are general node-level citations, not property-scoped.

Atlas node provenance follows a different convention: properties from
taxonomy ingest have implicit provenance from `taxonomy_meta.yaml`
(`source_file`, `ingest_date`). No per-field `PropertySource` entries are
needed on `ATLAS_TRANSCRIPTOMIC` nodes — the atlas and `cell_set_accession`
are the citation.

### Use `notes` fields, not YAML comments

YAML comments (`# ...`) are not preserved by programmatic round-trips
(e.g. `yaml.safe_load()` → `yaml.dump()`). Any annotation that must
survive automated processing — caveats, heterogeneity observations,
cross-references to other nodes — belongs in a `notes` field on the
relevant object, not in a YAML comment. Reserve comments for transient
developer-facing hints that are acceptable to lose.

### MapMyCells reference files — where they come from

`annotation_transfer/src/annotation_transfer/taxonomies.py` is the **single
authority** for where a taxonomy's MapMyCells files live. It holds a
`TaxonomySpec` per taxonomy id with `stats_s3_url` and `markers_s3_url`
pointing at the public Allen Brain Cell Atlas S3 bucket. Do not hardcode these
URLs anywhere else, and do not go looking for a local copy before checking the
registry — the files are re-downloadable on demand and are gitignored.

```
just fetch-mapmycells CCN20230722          # → conf/mapmycells/{taxonomy_id}/
just fetch-mapmycells CCN20250428 --force  # re-download
```

Registered taxonomies:

| id | taxonomy | species |
|---|---|---|
| `CCN20230722` | Whole Mouse Brain (Yao 2023) — WMBv1 | mouse |
| `CCN20250428` | Consensus Basal Ganglia (HMBA) | primate |
| `CCN202210140` | Whole Human Brain (Siletti) | human |
| `CCN20230505` | Human MTG SEA-AD | human |

**The stats file is a runtime dependency for mapping.** Atlas expression is
read from it on demand (see "Atlas expression" above), at
`conf/mapmycells/{taxonomy_id}/{basename of stats_s3_url}` — exactly where
`fetch-mapmycells` writes it. Stage B stamps the filename (e.g.
`precomputed_stats_ABC_revision_230821.h5`) into the notes of every marker
comparison with a measured value (`atlas expression from …`), and gen-facts
collects those stamps into `methods_summary.expression_sources`, so report
provenance resolves to a public URL without keeping the 1.4 GB artefact in the
repo. Edges emitted before the stamp existed report `stats_file: null` with a
warning; re-running `refresh-property-comparisons` stamps them.

Two things to know before using them:

- **They are large.** WMBv1 stats 1.4 GB, HMBA BG 1.1 GB. `fetch-mapmycells`
  prints the size before downloading and skips files already present.
- **HMBA BG ships two releases.** The registry points at the `20250630`
  combined consensus build, which is the right default for a consensus
  taxonomy. The earlier `20250531` release ships per-species files
  (`Human.` / `Macaque.` / `Marmoset.precomputed_stats.20250507.h5`) — use
  those directly if you need a single-species reference.

The accessor also needs the taxonomy's gene identity table,
`kb/taxonomy/{taxonomy_id}/gene_ids.tsv.gz` (committed for CCN20230722;
otherwise `just build-gene-ids {taxonomy_id}`, which needs the stats file and
network). `build-taxonomy-db` loads it offline.

### Gene IDs on classical markers

Every marker records `name_in_source` (the source's wording). A classical
marker (`defining_markers`, `negative_markers`, `neuropeptides`) that names
one gene also carries that gene's `ncbi_gene_id`, in the node's species, and
its official `symbol` — both or neither. Before adding or editing one, or
when a marker is reported `NOT MEASURED`: Follow `docs/marker_gene_ids.md` (it calls the `gene-id-curation` skill).

---

## Overview

The human is the top-level coordinator. Run each orchestrator when ready, review the output at each gate, and proceed at your own pace. There is no meta-orchestrator.

| Orchestrator | Location | Phase | Status | When to run |
|---|---|---|---|---|
| `ingest-taxonomy` | `workflows/ingest-taxonomy.md` | Discovery | **Ready** | Ingest a taxonomy table → atlas cluster CellTypeNode stubs |
| `asta-report-ingest` | `workflows/asta-report-ingest.md` | Literature | **Ready** | Start here when you have an ASTA deep research PDF — reconciles each proposed type against the region's existing nodes (NEW / ENRICH / DUPLICATE), then writes a new node file or adds to the existing one in `kb/graphs/{region}/`. Field guidance comes from the schema (`just schema-subset`); CL anchors and ontology terms via the `cl-mapping` and `term-grounding` skills. Review by PR; `gate: true` adds in-session sign-off. Hands off to `survey` |
| `survey` | `workflows/survey.md` | Literature | **Ready** | Broad snippet scan of ASTA corpus for a region → all_summaries.json; no synthesis, no KB write |
| `lit-review` | `workflows/lit-review.md` | Literature | **Experimental stub** | Seed discovery when starting without a report; may be revived; do not use in regular workflows |
| `cite-traverse` | `workflows/cite-traverse.md` | Literature | **Needs re-engineering** | Citation traversal + synthesis. Removed from the `asta-report-ingest` handoff (2026-10-27) — it is not in the regular path. May be folded back in later; do not wire new workflows to it |
| `evidence-extraction` | `workflows/evidence-extraction.md` | Literature | **Ready** | After survey or asta-report-ingest — writes PropertySource entries with quote_key to KB YAML |
| `map-cell-type` | `workflows/map-cell-type.md` | Mapping | **Ready** | Discovery mode: queries taxonomy DB at multiple ranks (0=leaf, 1, 2…) for candidate atlas matches; hypothesis mode: tests curator's proposed mapping. Uses `just find-candidates` with rank parameter. Produces MappingEdge YAML with property comparisons. Can run on stubs (LOW confidence) or after lit review. |
| `gen-report` | `workflows/gen-report.md` | Reporting | **Ready** | Single agentic session does filter (top-K → ≤ 3 survivors via evidence-hierarchy rubric) + AT-pooling decisions + paper-style report on survivors. Writes verdicts back for ALL top-K edges (survivors get SSSOM trio + caveats + proposed_experiments; cuts get confidence + tier:CUT rationale). LLM synthesis with hallucination guard (ID/quote/PMID/accession validation via pre-write hook + post-write structured-claims check). Reports open with an Introduction section surfacing `cl_mapping` + `proposed_cl_term`. |
| `cl-term-request` | `workflows/cl-term-request.md` | Reporting | **Ready** | Draft a CL new term request for a node with BROAD/RELATED/null `cl_mapping`. Reads facts via `just gen-facts`, applies CL definition + relations guidelines (`docs/LLM_prompt_guidelines_for_CL_definitions.md`, `docs/relations_guide.md`), emits issue-ready markdown. Posting is gated: `just preview-cl-ntr` then `just post-cl-ntr`. |
| `annotation-transfer` | `workflows/annotation-transfer.md` | Evidence transfer | **Pipeline ready** | Dataset retrieval → MapMyCells → F1 matrix → AnnotationTransferEvidence; marker assessment moved to `map-cell-type` |

### Validation / methods audits

Method-validation audits compare pipeline behaviour against oracle
ground truth (curator-supplied AT evidence, prior published mappings,
etc.). Each audit is a runnable driver with preflight invariants,
raw-evidence preservation, and reproducibility metadata.

| Layer | Location |
|---|---|
| Workflow docs | `workflows/validation/<audit_id>.md` (and `workflows/validation/README.md` index) |
| Driver code | `src/evidencell/validation/` |
| Run artifacts + findings | `research/validation/methods_audits/<audit_id>/` |
| Recipes | `just validate-<audit_id>` |

Current audits:

| Audit | Purpose |
|---|---|
| [`at_blind`](workflows/validation/at_blind.md) | Measure marker+region+NT coverage against curated AT evidence; informed region-expansion default and cohort-relative scoring sanity. |

When adding a new audit follow the checklist in
[`research/validation/methods_audits/README.md`](research/validation/methods_audits/README.md).

---

## Anti-hallucination infrastructure

A pre-write hook (`.claude/hooks/validate_mapping_hook.py`) runs automatically before
every `Write` or `Edit` to KB files. It is **not** an orchestrator step — it fires on all
KB writes regardless of which workflow is running.

**KB YAML** (`kb/**/*.yaml`) — blocks writes with: YAML parse errors, structural
integrity failures (dangling edges, duplicate IDs, placeholder snippets), `quote_key`
values absent from `references.json`, `PMID:`/`DOI:` citations absent from
`references.json`, LinkML schema non-conformance, and ontology-term references
(CL/UBERON/NCBITaxon CURIEs) that don't resolve via the OAK semsql DBs. The
term check is soft-skipped on fresh clones where OAK DBs aren't cached yet
(run `just fetch-oak-dbs`); `EVIDENCELL_SKIP_TERM_CHECK=1` provides an
explicit emergency bypass. CI runs the same check on every push/PR.

**Markdown reports** (`reports/{region}/*.md`) — blocks writes with: blockquote blocks
missing a `<!-- quote_key: X -->` attribution annotation, quote keys or PMIDs absent
from `references/{region}/references.json`.

See [`.claude/anti-hallucination-hooks.md`](.claude/anti-hallucination-hooks.md) for
the full specification and correction loop protocol.

---

## Inputs

| Input type | Location | Used by |
|---|---|---|
| ASTA deep research PDFs | `inputs/deepsearch/` | `asta-report-ingest.md` |
| ASTA corpus IDs | `research/{region}/{run}/pdf_corpus_ids.json` (asta-report-ingest output) | `survey.md` |
| Taxonomy tables (JSON/CSV/TSV) | `inputs/taxonomies/` | `ingest-taxonomy.md` |
| Taxonomy reference YAML | `kb/taxonomy/{taxonomy_id}/` | `map-cell-type.md`, `ingest-taxonomy.md` (M8) |
| Taxonomy SQLite index | `kb/taxonomy/{taxonomy_id}/{taxonomy_id}.db` (gitignored; build per worktree with `just build-taxonomy-db {taxonomy_id}`) | `map-cell-type.md` (candidate queries), `gen-report.md` (atlas-side facts). **Required** — a missing DB raises. Read-only previews (render, gen-facts) may set `EVIDENCELL_ALLOW_MISSING_TAXONOMY_DB=1` to proceed without atlas fields; anything that writes KB content (emit-stage-b, refresh-*, AT metrics) ignores it |
| Taxonomy field mapping | `kb/taxonomy/{taxonomy_id}/field_mapping.json` | `ingest-taxonomy.md` (fast-path detection) |
| MBA ontology JSON | `conf/mba/mbao-full.json` (gitignored; fetch with `just fetch-mba-ontology`) | `ingest-taxonomy.md` Step 4 (anat closure build); shared across all taxonomies |
| Precomputed stats HDF5 | `conf/mapmycells/{taxonomy_id}/` (gitignored; fetch with `just fetch-mapmycells {taxonomy_id}` — URLs come from `annotation_transfer/.../taxonomies.py`, see "MapMyCells reference files" above) | `map-cell-type.md` — **required**: atlas expression is read from it on demand (#189); `annotation-transfer.md` (local MapMyCells) |

Place input files in the appropriate subdirectory before running the relevant orchestrator.

---

## Typical workflow for a new mapping

Classical nodes emerge from research — they are not pre-created. Run these in
parallel where possible (taxonomy ingest + report ingest are independent).

```
── Discovery ──────────────────────────────────────────────────────────────────

1a. just ingest-report {region} {pdf_file}      # ASTA report → reconcile against the
    → workflows/asta-report-ingest.md            # region's nodes; new node files or
                                                 # additions to existing ones in kb/graphs/{region}/
    review as a PR (default), or pass gate: true for in-session sign-off

1b. just ingest-taxonomy-db {taxonomy_file} {taxonomy_id}  # full taxonomy → YAML + SQLite
    → workflows/ingest-taxonomy.md                         # (run in parallel with 1a)
    [GATE] approve field mapping + generated stubs

── Primary literature retrieval ───────────────────────────────────────────────

2.  workflows/survey.md                          # ASTA corpus → all_summaries.json
    region: {region}                             # one pass, all ASTA papers, all nodes
    corpus_ids_file: research/{region}/.../pdf_corpus_ids.json
    output_dir: research/{region}/survey_{date}/

── Evidence extraction ─────────────────────────────────────────────────────────

3.  workflows/evidence-extraction.md             # per-node: all_summaries.json → KB YAML
    summaries_file: research/{region}/survey_{date}/all_summaries.json
    # no paper selection gate for ASTA survey runs
    # run once per node_id

── AT coverage (before mapping) ────────────────────────────────────────────────

3.5 just at-coverage {taxonomy_id} {node_id}...  # declared at_source_sets → AT run?
    # (or --region {region}; with neither, the whole KB)
    # Report-only. Lists each classical node's at_source_sets correspondence
    # (dataset_accession + source_label, authored in evidence-extraction) and
    # whether an AT run already exists for it. For each UNRESOLVED row, run
    # workflows/annotation-transfer.md (Step 0 consumes the same
    # dataset_accession/source_label) BEFORE mapping — otherwise emit-stage-b
    # emits NO_EVIDENCE and you re-map after. No new gate: the retrieve_dataset
    # preflight is the single resource checkpoint. Nodes with no at_source_sets
    # are listed separately (proceed; AT simply absent) — the header states how
    # many nodes were checked, so a narrow run cannot pass for a region sweep.
    # Rows are checked against the one taxonomy given: a source whose run
    # targets another taxonomy shows as "NO RUN ON {taxonomy_id}" (still
    # non-zero exit) — check whether the node is meant to map to it.

── Mapping ────────────────────────────────────────────────────────────────────

4.  workflows/map-cell-type.md                   # evidence + atlas metadata → MappingEdge top-K
    # Stage B emits the top-K candidate edges mechanically; no curator
    # pre-filter gate. Filtering happens inside gen-report (next step).

── Reports + community ────────────────────────────────────────────────────────

5.  just gen-facts {graph_file} {node_id}        # extract structured facts
    just pool-candidates --node {node_id} > ...
    → workflows/gen-report.md                    # single session: filter (top-K → ≤3) +
                                                 # AT-pooling + synth + verdict write-back
    [GATE] biologist reviews, executes proposed experiments

6.  workflows/annotation-transfer.md             # AT results → AnnotationTransferEvidence
```

