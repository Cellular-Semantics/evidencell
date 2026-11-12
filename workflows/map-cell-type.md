# Mapping Orchestrator

You are a mapping coordinator. You discover candidate atlas matches for classical
(or prior transcriptomic) cell types, substantiate mappings against evidence and
atlas metadata, and produce MappingEdge YAML with structured property comparisons.

The curator may arrive with a hypothesis or with a discovery question. Both modes
use the same pipeline — discovery simply means Step 0 generates the candidates
rather than receiving them.

**Prerequisites**:
- Classical `CellTypeNode` in a KB YAML graph with at minimum: defining markers,
  NT type, and anatomical location. Literature evidence items improve confidence
  but are not required to begin — edges can start at LOW/UNCERTAIN and be upgraded
  after lit review.
- Taxonomy reference DB ready for the target atlas. The `query-taxonomy-db` skill
  (Step 0) checks freshness automatically and rebuilds if needed. Anatomy closure
  must be built once per taxonomy: `just fetch-mba-ontology` then
  `just build-anat-closure {taxonomy_id}`. The skill will warn if a newer MBA
  ontology release is available.

---

## Run parameters

```
PARAMS:
  classical_node_file: ""       # path to KB YAML containing the classical node(s)
  classical_node_id: ""         # id of the classical node to map (required)
  taxonomy_id: "CCN20230722"    # taxonomy DB to query for atlas candidates
  curator_hypothesis: null      # optional: {cell_set_accession, relationship} or list thereof
                                # if null → discovery mode (Step 0 queries taxonomy DB)
  ranks: [0, 1]                 # taxonomy ranks to query (0=leaf, 1=supertype, 2=subclass, …)
                                # check taxonomy_meta.yaml level_hierarchy for available ranks
  model: "sonnet"
```

**Setup, once per checkout per taxonomy** — atlas expression is read on
demand from the MapMyCells precomputed-stats HDF5 and cached in the
taxonomy DB (#189), so the stats file is a runtime dependency:

```bash
just fetch-mapmycells {taxonomy_id}    # → conf/mapmycells/{taxonomy_id}/ (1–1.5 GB)
just build-taxonomy-db {taxonomy_id}   # expression cache tables start empty
```

The gene mapping TSV is `conf/gene_mapping_{taxonomy_id}.tsv` (committed for
CCN20230722; otherwise `just generate-gene-mapping {stats_h5} {tsv}`). Both
paths come from the registry in
`annotation_transfer/src/annotation_transfer/taxonomies.py` — there is no
path parameter to set. `just warm-expression-cache {taxonomy_id}` optionally
pre-loads every KB marker gene and lists any that can't be measured.

---

## Step 0: Candidate discovery

If `curator_hypothesis` is provided, skip to Step 1 using those candidates.

Otherwise, query the taxonomy DB for candidates at each rank.

### Step 0a: DB query

Run the taxonomy DB candidate search at each requested rank. Ranks are integers
(0 = most granular/leaf, incrementing toward root). The mapping between rank and
level name is taxonomy-specific — check `taxonomy_meta.yaml` `level_hierarchy`
for the target taxonomy.

```bash
# For each rank in {ranks}, run:
just find-candidates {classical_node_file} {classical_node_id} {taxonomy_id} {rank} {top_k} \
  > {output_dir}/discovery_candidates_rank{rank}.json
```

Default: `top_k=5` per rank. Adjust ranks based on the taxonomy's
level_hierarchy — some taxonomies have more or fewer levels.

**AT signal comes from the node's `at_source_sets`.** `find-candidates` reads the
classical node's curated `at_source_sets` (the `(dataset_accession,
source_label)` correspondences authored in evidence-extraction), resolves each to
its AT run (`at_metrics.resolve_run_for_source`), and surfaces the atlas clusters
that source maps to as candidates — they get the F1 score bonus and bypass the
region/NT filters. There is no hand-made `research/{region}/at/*_f1.json` file
anymore. Run `just at-coverage {taxonomy_id} {classical_node_id}` first: any
`UNRESOLVED` row means a declared source has no AT run yet — run
`workflows/annotation-transfer.md` for it before mapping, or discovery gets no AT
signal for that node.

Stage A scoring (see [planning/map_cell_type_redesign_roadmap.md](../planning/map_cell_type_redesign_roadmap.md) §3 for the full
specification):

- **Hard prerequisite filters** (drop, not penalise):
  - **Region match (permissive)** — a candidate survives if any of
    its anat rows on a curator-queried term has `cell_count > 0`
    (strict in-region) OR `count_in_or_near_100um > 0` (soma
    within 100µm of the queried region). The 100µm-proximity
    signal handles registration-edge cases (CA1 ↔ subiculum,
    stratum-oriens ↔ pyramidale boundary, etc.) without LLM
    adjacency judgement. brain_cell_KG materialises closure
    aggregates upstream, so the query inspects the candidate's
    edge to the curator's literal terms directly — no
    `get_descendants()` expansion on our side.
  - **NT match** — only when both classical and candidate carry NT.
  - Annotation-transfer-matched candidates bypass both filters.
  - **Rank ≥ 1 descendant-anat fallback** (BCKG workaround): when a
    rank ≥ 1 candidate's own anat fails to qualify under the
    permissive rule, find_candidates retries against the union of
    its rank-0 descendants' anat with the same rule. If that
    qualifies, the candidate survives with
    `region_evidence: descendant_only`. Rationale: upstream Brain
    Cell KG strips non-dominant regions from non-leaf taxonomy
    nodes via a percent-of-cells cutoff, so the subclass /
    supertype `anat` row is unreliable; rank-0 (cluster) anat
    comes from the source cluster-cell-anat table and is intact.
    **Remove once BCKG ships an upstream anat-rollup fix.** See
    [planning/at_blind_region_drop_findings_2026-05-12.md](../planning/at_blind_region_drop_findings_2026-05-12.md)
    § a, § B2.
- **Expression** for the node's `defining_markers + neuropeptides +
  negative_markers` comes from `TaxonomyDB.expression()`. Genes not yet
  cached load from the stats HDF5 on first use (one-off per gene per
  checkout). If the HDF5 is missing and any queried gene is uncached,
  `find-candidates` **stops** with `just fetch-mapmycells {taxonomy_id}` —
  there is no metadata-only mode. Genes that can't be measured (no Ensembl
  mapping, or absent from the stats file) are listed as `NOT MEASURED` on
  stderr and under `not_measured_genes` in the discovery JSON; they score 0.
  Protein-name markers that only resolve to a gene through the
  `marker_aliases` stopgap (`PV`, `CB`, `CR`, `NOS`, `mGluR1` …) are not
  scored in Stage A — listed as `NOT SCORED` on stderr and under
  `unscored_protein_alias_markers` — until gene identity is resolved
  properly (#216). Use canonical gene symbols on classical nodes to have a
  marker scored.
- **Soft scoring** within the surviving pool:
  - **Graded region score** from `region_fraction_100um`:
    +2 if ≥ 0.5, +1 if ≥ 0.1, +0.5 if > 0, else 0.
    `region_fraction_100um` = candidate's
    `count_in_or_near_100um` at the highest matching queried
    term ÷ candidate's `n_cells`. Strict in-region cells also
    push this up (a soma inside the region is by definition
    within 100µm of it), so this signal subsumes "is the
    candidate located here?" generally.
  - **Region exact-match bonus** (+1): when the candidate has
    `cell_count > 0` strictly in any curator-queried term.
    Preserves discrimination between candidates centred in the
    region and those rescued by 100µm scatter alone.
  - Per-marker presence/absence credit and percentile-based
    discrimination (defining markers + neuropeptides + negative
    markers, equal-weight), **from expression only** — a gene listed
    in the atlas node's metadata marker columns gets no credit for
    being listed; annotation-transfer F1 buckets (+3/+2/+1); sex-bias
    bonus at rank 0.
- **Metadata cross-check (not scored)**: per candidate × queried gene,
  the atlas metadata marker lists (`defining_markers_scoped`,
  `defining_markers`, `tf_markers`, `merfish_markers`, `np_markers`)
  are compared with measured expression and disagreements reported as
  `marker_discrepancies` in the discovery JSON, plus a one-line summary
  per candidate on stderr:
  - `LISTED_NOT_EXPRESSED` — listed, but below `MIN_DETECTABLE`, or in
    the bottom 10% of siblings (same parent) *and* under half the top
    sibling's value. The important case: metadata error, gene-version
    difference, or scope mismatch.
  - `EXPRESSED_NOT_LISTED` — top 10% of siblings but not listed.
    Informational; metadata lists are short.
  - `LISTED_NO_EXPRESSION_DATA` — listed, but can't be measured.
- **Heterogeneity coverage** at rank ≥ 1: positive-marker scores are
  soft-dampened by `coverage^0.5` where coverage is the fraction of
  rank-(N−1) children with detectable expression. Tempers over-confidence
  on heterogeneous supertypes.
- **Output**: `expression_detail` (per-gene val/percentile/score),
  `region_fraction` (strict), `region_fraction_100um` (proximity),
  `region_count_completeness` (provenance of the winning anat row —
  null/`exact`/`lower_bound`; see schema), `region_evidence`,
  `at_hit`, `coverage` are emitted alongside the score for
  downstream consumption; `marker_discrepancies` per candidate and
  per-candidate `expression_source`, and top-level `not_measured_genes` /
  `unscored_protein_alias_markers` / `expression_source` sit outside
  `discovery_score`.

---

## Step 1: Cutoff (no curator gate)

The Stage A→B curator gate has been removed (Phase 1). Top-K candidates
from Step 0 — default `K=5`, configurable via the `top_k` arg to
`just find-candidates` — feed Stage B mechanical-emitter spawning directly.
Every above-cutoff candidate gets a `MappingEdge` written; the report
(generated downstream) is the human review point.

If discovery ran, read `discovery_candidates.json` for context but do not
present a gate. Proceed directly to Step 2.

If `curator_hypothesis` was provided in PARAMS, use those candidates as
the input set instead of discovery output.

---

## Step 2: (removed)

The former pre-flight enrichment step (`just enrich-marker-union` + DB
rebuild) is gone (#189). Expression is no longer stored in taxonomy YAML;
`find-candidates`, `emit-stage-b` and the `refresh-*` commands load any
uncached gene from the stats HDF5 themselves. There is no degraded mode:
a missing stats file stops the run with the fetch command.

---

## Step 3: Stage B emit (mechanical)

Stage B is fully programmatic as of issue #96. The per-candidate
mapping subagent that used to live here has been replaced by
`just emit-stage-b`, which constructs a `MappingEdge` skeleton per
top-K candidate from the Stage A discovery JSON + classical node YAML
+ taxonomy DB (atlas expression through the same on-demand accessor as
Stage A) + AT artifact. No LLM call. Run it once per rank:

```bash
just emit-stage-b {classical_node_file} {classical_node_id} {taxonomy_id} {rank} {top_k}
```

The emitter writes edges directly to `{classical_node_file}`'s `edges:`
section (auto-write per the Phase 1 design) and adds taxonomy-ref stub
nodes when missing. Idempotent: existing edge ids are skipped with a
warning.

### What the emitter produces per candidate

- `id`, `lit_type`, `taxonomy_type`, `mapping_justification:
  semapv:UnreviewedManualMapping`.
- `relationship: evidencell:UncertainRelationship` (default;
  gen-report's verdict block overrides at write-back with the
  predicate the report-time agent picks).
- `discovery_score` — verbatim copy from the discovery JSON entry
  (score, region_fraction_100um, region_count_completeness,
  expression_detail with per-gene cohort percentiles + coverage
  dampening, at_signal).
- `property_comparisons[]` — one row per:
  - `nt_type`: CONSISTENT when the candidate survived Stage A's NT
    prefix-match filter; NOT_ASSESSED if either side null.
  - `location`: alignment from the proximity-aware tier rule —
    `region_fraction_100um >= 0.5` → CONSISTENT;
    `0.1 <= region_fraction_100um < 0.5` → APPROXIMATE;
    `< 0.1` → DISCORDANT; null → NOT_ASSESSED;
    `region_evidence == DESCENDANT_ONLY` → DISCORDANT (the
    rank ≥ 1 BCKG-rescue path; the candidate's own anat missed,
    only its rank-0 descendants surfaced). The `node_b_value`
    string summarises the candidate's top painted (CCF2020)
    anat rows, falling through to `exact` then `lower_bound`
    rollups only when no painted leaves are available.
  - One row per defining_marker, negative_marker, neuropeptide on
    the classical node. Alignment from
    `expression_detail.val` vs `MIN_DETECTABLE` (0.1):
    - positive marker, `val >= MIN_DETECTABLE` and not boundary-
      cohort → CONSISTENT;
    - positive marker, `val >= MIN_DETECTABLE` with
      `cohort_pct in [0.1, 0.5)` → APPROXIMATE;
    - positive marker, `val < MIN_DETECTABLE` → DISCORDANT;
    - negative marker inverts: `val < MIN_DETECTABLE` →
      CONSISTENT, otherwise DISCORDANT;
    - `NOT_ASSESSED` (`node_b_value: not measured`) only for a gene
      recorded as not measured — the notes give the reason
      (`NO_ENSEMBL_MAPPING` / `NOT_IN_STATS`) and the stats file.
    The candidate's Stage A `marker_discrepancies` entry for the gene,
    if any, is appended to the notes (`METADATA DISCREPANCY …`) so
    gen-facts and report synthesis can see it. It does not change
    the alignment.
    Every comparison with a measured value records its stats file in
    the notes (`atlas expression from {file}`); gen-facts collects
    these for the report's Methods section.
    Symbol resolution: classical-node marker abbreviations
    (PV → Pvalb, CB → Calb1, CR → Calb2, NOS → Nos1, VIP → Vip,
    etc.) are mapped to canonical gene symbols via
    `PROTEIN_TO_GENE_ALIASES` in `src/evidencell/marker_aliases.py`
    (Stage B only; Stage A does not score them). This table is a
    stopgap — see #216; preferred is canonical gene symbols in
    classical-node YAML.
- `evidence[]` — emit deterministically:
  - `ATLAS_METADATA` (always; `supports: PARTIAL`): explanation
    auto-built from candidate atlas-side properties (n_cells,
    neighborhood, dominant anat term with completeness flag, key
    expression values).
  - `ANNOTATION_TRANSFER` (one item per entry in the classical
    node's `at_source_sets`, per candidate — issue #126): the node
    declares which external `(dataset_accession, source_label)`
    corresponds to this classical type (an agentic judgement made in
    evidence-extraction, quote-backed via `sources[]`). Stage B
    resolves the AT run operationally with
    [`at_metrics.resolve_run_for_source`](../src/evidencell/at_metrics.py)
    (matching `(dataset_accession, target_taxonomy, source_label)`),
    then [`compute_edge_metrics`](../src/evidencell/at_metrics.py)
    populates `run_ref`, `source_dataset_accession`,
    `source_cluster_label`, `correspondence`, `target_atlas`,
    `method`, `metrics_by_level`. `supports` defaults from
    `supports_default`, which is **level-aware**: SUPPORT only when an
    F1 ≥ 0.6 exists at the edge target's own rank or finer (a
    coarse-only match → PARTIAL), else PARTIAL ≥ noise floor, else
    NO_EVIDENCE. A declared source that does **not** transfer to a
    candidate (or whose run can't be resolved) still emits a
    `NO_EVIDENCE` item — negative signal, not a silent drop. Nodes
    without `at_source_sets` emit no AT evidence.
  - **LITERATURE evidence is NOT emitted by the mechanical
    Stage B** — verbatim `snippet:` matching against
    the reference store belongs in gen-report's synthesis pass,
    which sees the full literature context.
- `caveats[]` — emit typed by rule:
  - `MERFISH_REGISTRATION_UNCERTAINTY` when the winning anat row
    is `lower_bound` (the rollup includes non-painted CCF2020
    descendants whose cells aren't counted; value is a floor).
  - `AMBIGUOUS_MAPPING` when ANY property comparison is DISCORDANT
    (lists the discordant property names in the description).
  - `DISTRIBUTED_ACROSS_CLUSTERS` when AT F1 < 0.5 at cluster
    level (source cells are scattered across atlas clusters rather
    than concentrated; cleaner AT signal often lives at a coarser
    taxonomy level).
- **No `unresolved_questions`, `proposed_experiments`,
  `confidence`, `confidence_score`, or `rationale`** — these are
  gen-report's territory (written via the verdict block at
  writeback time; see Phase 3 design and `workflows/gen-report.md`).

The emitter's structural rules are unit-tested in
[`tests/test_stage_b_emit.py`](../tests/test_stage_b_emit.py).
Any rule change should land in both the module and the tests; the
workflow doc should be updated in the same PR.

### Curator hypothesis mode

When the curator supplies an explicit hypothesis (`PARAMS:
curator_hypothesis: [{cell_set_accession, relationship}, ...]`),
the emitter takes that list in place of the Stage A discovery
output. Stage A is still useful for the discovery_score block —
running `just find-candidates` first and then `just emit-stage-b`
populates the structured signals on the hypothesis edge.

## Step 4: Write to KB (no curator gate)

Edges produced by the Stage B mechanical emitter are written directly to
the target graph — there is no blocking curator review at this step.
Verdict authority lives in `gen-report` (Phase 3 design); the
curator reviews the synthesised report + PR diff downstream.
The pre-edit hook (`.claude/hooks/validate_mapping_hook.py`) still
validates structural integrity on every write.

For each edge emitted by Step 3:

1. For each atlas node referenced by the edge, ensure a minimal
   taxonomy ref stub exists in the graph's `nodes:` list. A stub
   needs only: `id` (= cell_set_accession), `name`,
   `definition_basis: ATLAS_TRANSCRIPTOMIC`, `taxonomy_id`,
   `cell_set_accession`. Full node data lives in the taxonomy
   reference store at `kb/taxonomy/{taxonomy_id}/`.

2. Append the edge to the `edges:` section of the target file.
   Edge `taxonomy_type` should use the `cell_set_accession`
   (e.g. `CS20230722_CLUS_0769`).

3. Update `target_atlas` on the graph if it was null (as for ASTA
   report ingests that started without an atlas target).

**Deferred edges** — curators may mark a candidate as deferred via
`PARAMS.deferred: [accession, ...]` (out of scope of the mechanical
emitter; see future tooling).
Route those to `{output_dir}/proposed_edges_{classical_node_id}.yaml`
as a standalone fragment instead of appending to the graph file;
they are picked up after lit review and re-evaluated. Default
behaviour is to write to the graph; only deferred items go to the
fragment.

---

## Rules

- **Discovery is the default.** Curator hypotheses are welcome but not required.
  The orchestrator surfaces candidates from the data; the curator adjudicates.
- **Ranks are taxonomy-agnostic.** Always use integer ranks (0=leaf, incrementing),
  never hardcoded level names like "cluster" or "supertype". Check the target
  taxonomy's `taxonomy_meta.yaml` `level_hierarchy` for available ranks.
- **No HIGH confidence from literature alone.** The agent must check the decision
  guide. Annotation transfer or experimental data (ephys/morphology) required.
- **No literature found → UNCERTAIN.** Document the evidence gap explicitly.
  Do not guess. Propose experiments that would resolve it.
- **Stubs are valid starting points.** Atlas metadata (markers, NT, location) is
  real evidence — it supports LOW-confidence edges. Confidence upgrades come from
  lit review and experimental evidence.
- **Stage B is mechanical (issue #96).** No per-candidate LLM call. The
  emitter's rules are versioned with the code and tested in
  `tests/test_stage_b_emit.py` — change rules there, not at use sites.
- **Predicate + confidence belong to gen-report.** The Stage B emitter
  defaults `relationship: evidencell:UncertainRelationship`; the
  report-time agent (`workflows/gen-report.md` Step 3) writes the final
  predicate, cardinality, and confidence/rationale via the verdict
  block at writeback time (Phase 3 design).
- **No curator pre-filter between Stage B and report-time.** Stage B
  unconditionally emits the top-K candidate edges; gen-report's
  synthesis session performs filter + AT-pooling + synth as one
  agentic pass (Acts 1–3, see `workflows/gen-report.md` Step 3),
  whittles down to ≤ 3 survivors using the evidence-hierarchy
  rubric, and writes back verdicts for both survivors and cuts.
