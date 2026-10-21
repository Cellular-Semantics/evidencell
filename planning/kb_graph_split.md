# Splitting the KB graph files — draft plan for #125

> **Status:** draft for discussion.
> **Tracks:** [#125](https://github.com/Cellular-Semantics/evidencell/issues/125)
> **Measured on** `main` @ `4fde53a`.

---

## 1. The problem

A round of curation on one cell type currently rewrites a file shared with
eighteen others.

`kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml` is **1.0 MB
holding 19 literature types**; `hippocampus_glutamatergic.yaml` is **0.5 MB
holding 12**. Between them, 70% of all KB graph content sits in two files.

Three consequences:

- **Every edit is a whole-file rewrite.** Diffs are unreviewable, and two
  curators working on different cell types collide in the same file.
- **Blast radius has no relationship to intent.** Correcting one marker on one
  type touches a file eighteen other types depend on.
- **Agents read far more than they need.** A workflow targeting one type loads
  the entire region.

The aim is to **limit the size of the files updated during each round of
work** — taxonomies excepted.

---

## 2. Current state

14 files, 2.17 MB, 415 nodes, 472 edges.

### 2.1 There are three kinds of node, not two

This is the fact that reshapes the plan. `definition_basis` across all 415
nodes:

| Kind | Count | What it is |
|---|---:|---|
| `CLASSICAL_*` (MULTIMODAL 35, NEUROCHEMICAL 21, MORPHOLOGICAL 5, ANATOMICAL 2, ELECTROPHYSIOLOGICAL 1) | **64** | Literature types defined by morphology, markers, physiology |
| **`PRIOR_TRANSCRIPTOMIC`** | **6** | **Literature types that are T-types from a *non-reference* taxonomy** — carry `prior_cluster_label`, `prior_dataset_accession`, `prior_reference` |
| `ATLAS_TRANSCRIPTOMIC` | **345** | Stubs pointing into a reference taxonomy |

`PRIOR_TRANSCRIPTOMIC` nodes are first-class literature types, not anomalies.
In cerebellum they form the middle of a three-step chain:

```
classical_candelabrum  ──exactMatch──▶  pli1_osorno  ──exactMatch──▶  wmb_cluster_5178
 CLASSICAL_MORPHOLOGICAL                PRIOR_TRANSCRIPTOMIC           ATLAS_TRANSCRIPTOMIC
 (Osorno et al. T-type, not in a reference taxonomy)
```

**Therefore the split unit is not "one classical type" — it is the connected
component of non-atlas nodes joined by lit→lit edges.**

### 2.2 That gives 64 split units, not 70

| | |
|---|---:|
| Connected components of non-atlas nodes | **64** |
| …of which multi-node | **4** (all cerebellar) |

The four multi-node components:

| Component | File |
|---|---|
| `classical_basket`, `classical_stellate`, `mli1_kozareva`, `mli2_kozareva` | `CB_MLI_types.yaml` |
| `classical_candelabrum`, `pli1_osorno` | `CB_PLI_types.yaml` |
| `classical_globular`, `pli2_osorno` | `CB_PLI_types.yaml` |
| `classical_lugaro`, `pli3_osorno` | `CB_PLI_types.yaml` |

Note `CB_MLI_types.yaml` is **one** component — it cannot split into four
files. `CB_PLI_types.yaml` splits into three.

### 2.3 File inventory

| Region | File | KB | non-atlas | atlas | edges |
|---|---|---:|---:|---:|---:|
| hippocampus | `hippocampus_GABAergic_interneurons.yaml` | **1022** | 19 | 82 | 205 |
| hippocampus | `hippocampus_glutamatergic.yaml` | **499** | 12 | 88 | 135 |
| sexually_dimorphic | `20260425_…_report_ingest.yaml` | 149 | 10 | 22 | 27 |
| hippocampus | `20260427_…_glutamatergic_report_ingest.yaml` | 112 | 3 | 30 | 30 |
| dentate_gyrus | `20260414_…_report_ingest.yaml` | 104 | 5 | 12 | 13 |
| hippocampus | `wmb_to_ctx_annotation_transfer.yaml` | 79 | **0** | 78 | 49 |
| dentate_gyrus | `dg_glut.yaml` | 45 | **0** | 15 | **0** |
| cerebellum | `CB_PLI_types.yaml` | 32 | 6 | 3 | 6 |
| dentate_gyrus | `dg_pir_ex_imn.yaml` | 31 | **0** | 11 | **0** |
| immature_neurons | `20260422_…_report_ingest.yaml` | 29 | 7 | 0 | **0** |
| cerebellum | `CB_MLI_types.yaml` | 19 | 4 | 2 | 5 |
| sexually_dimorphic | `dlbnst_crf.yaml` | 19 | 2 | 0 | **0** |
| BG | `GPi_shell_neuron_Mmus.yaml` | 14 | 1 | 1 | 1 |
| BG | `GPi_shell_neuron.yaml` | 12 | 1 | 1 | 1 |

### 2.4 Five files do not fit the model

| File | Why | Likely disposition |
|---|---|---|
| `wmb_to_ctx_annotation_transfer.yaml` | 0 non-atlas nodes, 49 atlas→atlas edges. A **taxonomy↔taxonomy crosswalk** (WMBv1 CCN20230722 → CTX-HPF CS202106160) derived from vendor CTX_* fields, abusing `lit_type`/`taxonomy_type` to hold two atlas endpoints | Reference data — move beside the taxonomies, not a graph |
| `dg_glut.yaml` | 0 non-atlas, 0 edges, 15 stubs — **all orphan** | Stub dump; `kb/taxonomy/` or delete |
| `dg_pir_ex_imn.yaml` | 0 non-atlas, 0 edges, 11 stubs — **all orphan** | Stub dump; `kb/taxonomy/` or delete |
| `20260422_immature_neurons_report_ingest.yaml` | 7 non-atlas nodes, **0 edges** | Unmapped lit types — valid content, but 7 single-node components |
| `dlbnst_crf.yaml` | 2 non-atlas nodes, **0 edges** | Same |

**Not** an AT-results problem: `kb/annotation_transfer_runs/` separately holds
**8 genuine AT run records** (`at_run_20260408_winterer_olm_mmc_wmbv1` ←
`GEO:GSE124847`, etc.), cited from edges via `run_ref` /
`AnnotationTransferEvidence`. The name collision with
`wmb_to_ctx_annotation_transfer.yaml` is misleading; the two are unrelated.

### 2.5 Duplication is mechanical, not curatorial — good news

345 atlas stub instances resolve to 270 distinct accessions. **65 accessions
appear in ≥2 files.** Classified by cause:

| Cause | Count | Fix |
|---|---:|---|
| Identical spelling, same fields, >1 file | **52** | Pure dedup — mechanical |
| `taxonomy_id` disagreement | **13** | All the same typo (below) |
| **Genuine curatorial conflict** | **0** | — |

This is materially cheaper than feared. There are **no merge decisions to
make** on shared stub fields.

### 2.6 Three latent defects the split would otherwise inherit

**(a) `taxonomy_id: CCN202307220` — a trailing zero on 44 nodes.**

| File | nodes |
|---|---:|
| `dentate_gyrus/dg_glut.yaml` | 15 |
| `dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml` | 12 |
| `dentate_gyrus/dg_pir_ex_imn.yaml` | 11 |
| `cerebellum/CB_PLI_types.yaml` | 3 |
| `cerebellum/CB_MLI_types.yaml` | 2 |
| `BG/GPi_shell_neuron_Mmus.yaml` | 1 |

`kb/taxonomy/` holds only `CCN20230722` and `CS202106160`. These 44 nodes
resolve to no taxonomy, so `render._node_b_info` DB lookups **fail silently
today**. Not caused by the split — but the split multiplies it.

**(b) 39 nodes are referenced by no edge.** Orphans by file: `dg_glut` 15,
`dg_pir_ex_imn` 11, `immature_neurons` 7, `dlbnst_crf` 2, plus 4 scattered
across the three largest files. **A component-based splitter would drop every
one of these silently** — they belong to no component. They need an explicit
disposition, not a default.

**(c) `workflows/asta-report-ingest.md:680` bypasses the pre-edit hook.** It
writes region-wide dated dumps with `cp`:

```bash
cp {output_dir}/proposed_kb_{region}.yaml \
   kb/graphs/{region}/{YYYYMMDD}_{region}_report_ingest.yaml
```

The adjacent comment claims "Pre-edit validation hook fires automatically on
write" — **it does not.** The hook is PreToolUse on Edit/Write; `cp` runs
through Bash and is not intercepted. This is the producer that introduced both
the cross-region duplicates and the `CCN202307220` typo. Splitting without
fixing it means the next ingest round re-creates region-wide files.

### 2.7 Edge endpoint reality

| Combination | count |
|---|---:|
| lit → atlas (the normal case) | **417** |
| atlas → atlas (all in `wmb_to_ctx_…`) | 49 |
| lit → lit | **6** |

All 6 lit→lit edges are cerebellar, and all 6 connect a `CLASSICAL_*` node to a
`PRIOR_TRANSCRIPTOMIC` node. They are the reason components, not types, are the
split unit.

### 2.8 The rule that constrains the layout

`src/evidencell/validate.py` `structural_checks()` **lines 65–72**: both
`lit_type` and `taxonomy_type` of every edge must string-match the `id` of a
node in the **same YAML document**. No cross-file or cross-store resolution
exists.

This single rule is why atlas stubs exist at all. Stubs are projections of the
taxonomy DB — generated by `taxonomy_db.py:836`, written by
`stage_b_emit.py:951`. They carry no literature justification and need none;
atlas provenance is implicit from `atlas` + `cell_set_accession`
(`_models.py:939`).

### 2.9 What stubs cost

Stubs are **345 of 415 nodes (83%)** and are the dominant driver of projected
per-component file size. `olm_cell_ca1` projects to 114 KB because of 16 edges
and their 16 stubs — not because the type itself is large.

Retiring stubs entirely (resolving atlas endpoints against
`kb/taxonomy/CCN20230722.db` instead) is therefore the single highest-leverage
change available. It is a **validator change, not a content decision**, and it
is deliberately *not* in this plan's scope — but the pilot is designed to
measure whether it should be.

---

## 3. Consumer surface

Measured against every module reading `kb/graphs`.

| Consumer | Effect of the split |
|---|---|
| `toc.py` `load_mappings()` | **unchanged** — walks the directory, reads only `edges[]` |
| `render.extract_node_facts()` | **unchanged in substance** — needs the node, its edges, its stubs |
| `stage_b_emit._write_back()` | **unchanged** — already *creates* the stubs the design relies on |
| `refresh_property_comparisons`, `refresh_predicates`, `refresh_expression_pcs` | **unchanged** |
| `qc_content` | **unchanged** |

Four things need handling:

**`paths.find_node_file()` — highest unaccounted risk.** It is
first-match-wins over `sorted(kb_dir.rglob("*.yaml"))` (`paths.py:35`). Today a
node id appears in one file. Post-split, if any stub or duplicate shares an id
with a canonical file, `find_node_file` can return the **wrong** file, and
`render.extract_node_facts` will happily render a full report from a stub. This
must be made unambiguous — or made to raise on multiple matches — **before**
the split, not after.

**`pool_candidates.find_pool_candidates()` fails silently.** It does an
all-pairs comparison over distinct `edge.lit_type` values *within one
document*. One component per file means one key, zero pairs, and it returns
`[]` with no error. Callers: `just pool-candidates GRAPH_FILE`,
`workflows/gen-report.md`. Fix is ~20 lines: scope to a region directory. A
silent loss of convergence detection is the worst available failure mode.

**Per-file validation gets ~4.5× slower.** `tests/test_kb_examples.py`, `just
validate-all` and `just validate-terms` spawn one `linkml-validate` subprocess
per file; 14 → ~64 files at ~1.5 s per spawn. Batch the invocation, or accept
the regression knowingly.

**`render.has_merfish` is a trap that bites before any split.**
`render.py:1311` scans terminal nodes for `anatomical_location` and sets
`graph_meta.has_merfish_location` (`:1543`). `workflows/gen-report.md:517`
uses it to gate a **correctness caveat** — "WMBv1 location data derives from
MERFISH spatial registration and records soma position only; axonal and
dendritic projection targets are not reflected." It is true in exactly three
files (`GPi_shell_neuron.yaml`, `GPi_shell_neuron_Mmus.yaml`,
`CB_PLI_types.yaml`), and in every case **because atlas stubs carry
`anatomical_location`** — one of the stub-convention violations. Stripping
stubs to the documented five fields silently removes a caveat from three
reports. The fix is to derive it from the taxonomy store, where atlas anatomy
canonically lives.

### Conflict surface

Only **3 open PRs touch `kb/graphs/`** — #117 (3 files), #74 (3), #113 (1).
Seven files between them, all 3–5 months stale.

---

## 4. Functional spec

Stated without reference to implementation, so success is checkable.

**For a curator.** Opening a cell type means opening one file of roughly
20–60 KB containing that type (and, where a lit→lit edge binds them, its
tightly-coupled siblings) and nothing else. A round of work produces a diff
confined to that file. Two curators working on different types in the same
region never touch the same file.

**For an agent.** Locating a type's file is a function call — `find_node_file(node_id)` —
not a convention the agent has to know, and it either returns the one canonical
file or raises.

**For review.** Merging two types becomes a file deletion plus an edit: atomic
and legible in git. Today it is an invisible edit inside a 1 MB file.

**For CI.** Four guarantees that cannot exist today, because no per-file check
sees across files:

1. No node id is canonically defined in more than one file.
2. Every edge endpoint resolves to exactly one canonical definition.
3. Every file's name agrees with the component it defines.
4. Every `taxonomy_id` resolves to a directory under `kb/taxonomy/`.

**What does not change.** Taxonomy files. Quote and reference provenance. The
schema. The pre-edit hook keeps blocking invalid writes.

**Projected sizes** (each component assembled with its edges and their stubs):

| | size |
|---|---|
| median | **30 KB** |
| p90 | 60 KB |
| largest (`olm_cell_ca1`, 16 edges + 16 stubs) | **114 KB** |
| smallest | 2 KB |

A typical curation round moves from a 1.0 MB file to a **30 KB** one — ~34×.
Worst case 114 KB, still ~9×.

---

## 5. Technical endpoint

### Layout

```
kb/graphs/{region}/{component_id}.yaml
```

where `component_id` is the id of the component's single non-atlas node, or —
for the four multi-node components — a stable chosen representative. Each file
is a self-contained `CellTypeMappingGraph`.

### Contents

- **The component's non-atlas nodes** in full (`CLASSICAL_*` and/or
  `PRIOR_TRANSCRIPTOMIC`), with markers, `sources`, `definition_references`.
  Exactly one file canonically defines any given node id.
- **Thin stubs** for atlas edge targets.
- **Edges** owned by the component, carrying their evidence.

### Endpoint resolution

Satisfy `validate.py:65–72` with thin stubs rather than changing the rule —
**provisionally**. §2.9 argues stubs are the dominant cost; the pilot measures
that cost, and the evidence decides whether to keep them or open the
retire-stubs follow-on. Committing either way on prediction is what made this
ticket hard to finish.

### New `qc_content` checks

New *checks in an existing sweep* — `qc_content.py` already has severity tiers,
subject-based fingerprints, a baseline with pruning, and `_coverage_gaps()`.

| Check | Severity | Catches |
|---|---|---|
| `duplicate_node_id` | ERROR | a node id canonically defined twice |
| `filename_component` | ERROR | filename disagreeing with the component |
| `dangling_endpoint` | ERROR | an endpoint resolving to no canonical file |
| `unknown_taxonomy_id` | ERROR | the `CCN202307220` class of defect |
| `orphan_node` | WARN | a node referenced by no edge |
| `stub_drift` | WARN | a stub disagreeing with the taxonomy DB |

**These must run corpus-wide, not per-region.** The `dg_*` duplicates span
`dentate_gyrus/` and `immature_neurons/`, so `qc_content._kb_nodes_for_region`
— which is region-scoped — would never see them.

### Explicitly not in the endpoint

No build artifact. No region flattening. No `node_id`-as-global-key change. No
stub retirement. All remain live follow-ons; the layout above is compatible
with each.

---

## 6. Sequencing

### Rationale

1. **A split multiplies whatever it starts from.** 44 bad `taxonomy_id`s and 65
   duplicated accessions become ~64 files' worth of the same. *Reconcile before
   relayout.*
2. **Two consumers fail silently.** `find_node_file` can return a stub;
   `pool_candidates` returns `[]`. Silence is worse than a crash. *Fix before
   the split.*
3. **One producer bypasses the hook.** `asta-report-ingest.md:680`'s `cp` will
   re-create region-wide files after the split. *Fix it, or the split does not
   hold.*
4. **`src/`-only work has no curation conflict.** Front-load it.
5. **We are uncertain about one thing: whether stubs are worth their cost.**
   Reach a measurement of that as early as possible, on the smallest content
   that exercises it. *The pilot is an experiment, not a first instalment.*

### Phase 0 — enablers (`src/` and `workflows/` only)

| Step | Why here |
|---|---|
| **`find_node_file()` raises on multiple matches** | Rationale 2. The highest unaccounted risk: today it silently returns the first `sorted(rglob)` hit |
| **`pool_candidates` → region-scoped** | Rationale 2. ~20 lines; update `just pool-candidates` and `workflows/gen-report.md` |
| **`asta-report-ingest.md:680` writes via the hook-covered path** | Rationale 3. Also correct the false comment claiming the hook fires on `cp` |
| **`has_merfish` derives from the taxonomy store** | Unblocks any stub normalisation; otherwise 3 reports silently lose a caveat |
| **Corpus-wide cross-file checks in `qc_content`** | They immediately report Phase 1's work-list, and are in place when the split lands. Baseline the backlog |
| **Batch `linkml-validate`** | 14 → ~64 files at ~1.5 s/spawn |
| **#86 — one pinned serialiser** | Scoped down: pin canonical YAML output in *one* helper rather than converting all 8 writers. Converting all 8 is a separate ticket and not a prerequisite |

*Verified by:* `just test`; `just qc-content` reporting the known violations as
new findings; the baseline absorbing them.

### Phase 1 — reconciliation (content, no layout change)

| Step | Detail |
|---|---|
| **Fix `taxonomy_id: CCN202307220` → `CCN20230722`** | 44 nodes, 6 files. Mechanical. Also repairs today's silent `_node_b_info` failures |
| **Dedup 52 identical-spelling repeated accessions** | Mechanical — §2.5 established there are no curatorial conflicts |
| **Disposition for 39 orphan nodes** | Curator decision per file. `dg_glut` / `dg_pir_ex_imn` (26 orphans) are pure stub dumps; the 9 in `immature_neurons` / `dlbnst_crf` are unmapped lit types and must be *kept* as single-node components |
| **Disposition for the 5 non-conforming files** | Per §2.4. `wmb_to_ctx_annotation_transfer.yaml` is reference data and should leave `kb/graphs/` whole |

**Deliberately excluded:** normalising the 133 fat stubs. Stripping
`anatomical_location` is a report-content regression (§3), and the fields are
redundant with the taxonomy DB regardless. If stubs are retired later, the
whole question dissolves. Fold it into the stub-retirement follow-on instead of
paying for it twice.

*Verified by:* Phase 0 checks going quiet; baseline shrinking rather than being
re-accepted.

### Phase 2 — pilot: cerebellum

**`CB_MLI_types.yaml` + `CB_PLI_types.yaml` — 51 KB → 4 component files.**

Chosen because it is simultaneously the smallest useful case and the hardest:

- **Zero stubs shared with any other file** — no dedup entangled in the
  experiment.
- **All 6 lit→lit edges in the repo** are here, so it is the only content that
  exercises multi-node components and the `PRIOR_TRANSCRIPTOMIC` chain.
- `CB_MLI_types.yaml` is a **single 4-node component** — it directly tests that
  the splitter refuses to break a component rather than producing 4 broken
  files.
- Small enough to `git revert`.

**Decision gate.** The pilot answers: how much duplicated state do stubs
introduce, does `stub_drift` fire in practice, is the diff legible, and does
component-naming survive the multi-node case? That evidence — not prediction —
decides whether to continue with stubs or open the stub-retirement follow-on.

### Phase 3 — roll out, smallest first

`BG` (already compliant — rename only) → `sexually_dimorphic` →
`dentate_gyrus` → `immature_neurons` → **the two hippocampus monoliths last**
(31 components, 70% of all bytes).

Hippocampus is last for a reason beyond size: its merge decisions are entangled
in #116, and resolving those under a split is strictly easier than resolving
them *and* splitting at once.

---

## 7. Verification

- `just test` green at each phase; `just qc-content --baseline` reporting
  **0 new** after each.
- `find_node_file()` resolves all 64 components and **raises** on any ambiguity.
- `just gen-facts` and `just gen-report-node` produce **byte-identical** output
  for a pilot type before and after its split — the strongest single check that
  the split is content-preserving.
- `just pool-candidates` still surfaces convergence post-split.
- Every `taxonomy_id` in the corpus resolves to a `kb/taxonomy/` directory.
- Node count conserved across the split: 415 in, 415 + (duplicated stubs) out,
  with **0 nodes dropped** — specifically the 39 orphans accounted for
  explicitly rather than by omission.
- `graph_meta.has_merfish_location` unchanged for `GPi_shell_neuron*` and the
  cerebellar components.
- Per-component sizes near projection (median ~30 KB, max ~114 KB).

---

## 8. Follow-ons, explicitly deferred

| | |
|---|---|
| **Retire atlas stubs** | Resolve atlas endpoints against `kb/taxonomy/*.db` by relaxing `validate.py:65–72`. Highest leverage available (§2.9); the Phase 2 gate is designed to inform it |
| **Normalise the 133 fat stubs** | Subsumed by the above if it proceeds |
| **Convert all 8 KB writers** to the pinned serialiser (#86 in full) | |
| Build/query layer over components | |
| Region flattening; `node_id` as global primary key | |
| #101 / #31 convergence as queries | |

### Issues that need filing

- Disposition of `wmb_to_ctx_annotation_transfer.yaml` (reference data filed as
  a graph).
- The `CCN202307220` typo and its silent `_node_b_info` failures — a live bug
  independent of this work.
- `asta-report-ingest.md:680` hook bypass — also live and independent.

---

## 9. Implementation log — Phase 0, Phase 1 (partial), Phase 2 pilot

Completed on branch `kb-graph-split`. Measurements and corrections below
supersede the estimates above where they disagree.

### 9.1 Corrections to this plan found during implementation

**`refresh_predicates` is not defective.** §"consumer surface" implied its
`yaml.dump(data, fh)` alphabetised keys. It does not — that module uses a
configured `ruamel.yaml` round-trip dumper (`preserve_quotes`, explicit indent,
width 4096), which preserves key order *and* comments. The real writer gap is
narrower and different: **no writer validates before writing**, and none passes
through the PreToolUse hook (it intercepts the Write/Edit tools only).

**A `dangling_endpoint` check cannot fire today.** It was specified in §5 but is
unimplementable: while `validate.structural_checks` requires both endpoints to
resolve *within the same document*, every endpoint is resolvable by
construction. The check becomes meaningful only if that rule is relaxed to
cross-file resolution — i.e. with stub retirement. Shipping it now would add a
check that silently never runs, which is the defect class this work exists to
remove. Deferred, with the reason recorded in `qc_content.sweep_cross_file`.

**A `filename_component` check would fire on correct content.** `CB_MLI_types.yaml`
is one whole component under a descriptive name, which is right, not wrong. The
check only makes sense once the rollout is complete. Deferred.

**`orphan_node` must be scoped per file, not corpus-wide.** Pooling edge
endpoints across the corpus reports 18 orphans; scoping per file reports 39.
The per-file number is the correct one, because that is what a component split
acts on — a node unreferenced in its own document belongs to no component and
is dropped, whether or not another file's edge names it.

**The split unit count stands at 64**, and the pilot confirmed the component
rule empirically: `CB_PLI_types.yaml` split into 3, `CB_MLI_types.yaml` refused
to split at all.

### 9.2 Two fails-open defects found and fixed

Both are instances of the pattern this work targets — a check that passes
because it could not run.

**LinkML's `Validator` validates nothing unless plugins are passed explicitly.**
`Validator.iter_results_from_source` opens with
`if not self._validation_plugins: return []`, so a `Validator(schema)` built
without a plugin list reports **every** instance as valid. The first cut of the
batch validator hit this and cheerfully reported "All 14 KB files valid" while
checking nothing. Both `validate_batch` and `kb_io` now pass
`[JsonschemaValidationPlugin(closed=True)]` explicitly, matching the
`linkml-validate` CLI, and `tests/test_kb_io.py::test_validator_actually_validates`
fails if that is ever dropped.

**`sqlite3.connect()` creates an empty database, poisoning `exists()` guards.**
Every taxonomy-DB lookup guards with `db_path.exists()` / `is_file()` and then
connects. On the first miss, connect leaves a 0-byte file — after which the
guard passes forever and the next query raises `no such table: nodes` instead
of degrading gracefully. Observed live: running `render facts` in a fresh
worktree created `kb/taxonomy/CCN20230722/CCN20230722.db` (0 bytes) and broke
three previously-passing `at_metrics` tests. Fixed with
`kb_io.usable_sqlite` / `kb_io.connect_readonly` (read-only URI mode, so a
missing file raises rather than being created) at the two graceful-degradation
sites: `at_metrics.ancestor_accession_by_level`, `render._open_taxonomy_db`.
Other `sqlite3.connect` call sites are not graceful-degradation paths and were
left alone.

### 9.3 A live report defect fixed

`GPi_shell_neuron.yaml` targets **`HMBA_BG_Consensus`**, which is
dissection-based, yet it emitted the location caveat whose text reads *"WMBv1
location data derives from MERFISH spatial registration"*. Wrong atlas, in a
generated report.

Cause: the caveat was gated on "any terminal node carries
`anatomical_location`", which is a stub-convention violation rather than a fact
about the atlas. The gate is now keyed on `taxonomy_id` against
`MERFISH_REGISTERED_TAXONOMIES`:

- keyed on `taxonomy_id`, not the atlas name, because the atlas name is free
  text and WMBv1 alone is spelled four ways across the corpus — `WMBv1`,
  `WMBv1 (CCN20230722)`, `Allen Brain Cell Atlas`, `Allen Brain Cell Atlas
  CCN202307220`;
- the note text is now parameterised by atlas rather than hardcoding "WMBv1".

**This changes report content.** `has_merfish_location` was true for 3 files on
stub contents; it is now true for the 6 files that actually map into
CCN20230722 and false for `GPi_shell_neuron.yaml`. Net effect: one incorrect
caveat removed, and the caveat added to WMBv1-mapping reports that previously
omitted it because their stubs happened to be thin. The facts output for the
three pilot types is byte-identical across the change.

### 9.4 Phase 1 — the `CCN202307220` typo, fixed

44 nodes across 6 files. Confirmed a typo rather than a distinct identifier:
both spellings carry the identical `CS20230722` accession prefix (44 vs 271
nodes). The token also appeared in `atlas`, `target_atlas`, node names and
prose, all referring to the same wrong id — replaced globally in those six
files. `taxonomy_id` counts are now `CCN20230722: 315` (271 + 44),
`CS202106160: 29`, and the new `unknown_taxonomy_id` check reports zero.

Not yet done from Phase 1, both needing curator decisions: deduping the 52
identical-spelling repeated accessions, the disposition of the 39 orphan nodes,
and the disposition of the 5 non-conforming files.

### 9.5 Phase 2 pilot — results

`CB_PLI_types.yaml` (32.6 KB, 6 non-atlas nodes, 3 components) → three files:

| File | Size | Nodes | Edges |
|---|---:|---|---:|
| `classical_candelabrum.yaml` | 14.6 KB | `classical_candelabrum`, `pli1_osorno` + 1 stub | 2 |
| `classical_lugaro.yaml` | 11.3 KB | `classical_lugaro`, `pli3_osorno` + 1 stub | 2 |
| `classical_globular.yaml` | 10.1 KB | `classical_globular`, `pli2_osorno` + 1 stub | 2 |

`CB_MLI_types.yaml` is one whole component and was **left untouched** — the
splitter now treats "already a single component" as a no-op rather than a
rename, because renaming a curated file costs its header provenance for nothing.

Total bytes grew 32.6 KB → 36.0 KB (+10%), entirely from duplicating the
curatorial header comment into each file. Largest file fell 32.6 KB → 14.6 KB.

**Verification, all passing:**

- `just validate-all` — 16 files valid.
- `structural_checks` — 0 issues on each of the 4 cerebellum files.
- `find_node_file` resolves all 9 cerebellum node ids to the right file.
- **`just gen-facts` output is byte-identical** for all three pilot types
  except `graph_file`, `kb_graph_file` (correctly updated — the file moved) and
  `gen_timestamp`. Normalising those three keys, content compares equal.
- `just test` — 751 passed, 11 skipped.
- `just qc-content --baseline` — 0 stale, 5 new (below).

**Comment preservation.** The splitter serialises through ruamel round-trip, not
`kb_io.write_kb_yaml`, because the two CB files carry 87 curatorial comment
lines — curator, date, source-analysis URL, an ASCII evidence-graph diagram.
A PyYAML re-serialise would drop all of them. CLAUDE.md permits losing comments,
but losing 87 in a pilot is avoidable. The file header is shared provenance and
is copied into each component file.

### 9.6 Open items surfaced for review

`just qc-content --baseline` reports **5 new findings, deliberately not
baselined** — baselining them here would accept content problems as a side
effect of a layout change:

- **3 × `duplicate_node_id`** (ERROR) — `dg_neuroblast`,
  `dg_immature_granule_neuron`, `dg_mature_granule_neuron`, each defined in both
  `dentate_gyrus/20260414_…` and `immature_neurons/20260422_…`. These are
  cross-region, which is why no region-scoped check ever saw them. **Needs a
  curator decision on which copy is canonical, and its own issue.**
- **2 × `no_refs_store`** (ERROR) — mechanical propagation of an existing
  cerebellum finding across the split (the pre-existing
  `CB_PLI_types.yaml` entry was pruned as genuinely fixed). Cerebellum has no
  reference store, so every provenance check for the region is vacuous.
  Pre-existing, now attributed to two files instead of one.

`orphan_node` (39) and `rationale_stale` (41) are WARN and do not gate.

### 9.7 Also landed

- `just validate-all` batches into one process: **16.2 s → 2.5 s** for 14
  files, and the cost now scales with file count rather than per-spawn schema
  compilation. New module `src/evidencell/validate_batch.py`.
- `workflows/asta-report-ingest.md:680` no longer writes via `cp`. The step now
  requires the Write tool and explains why, and the false claim that "pre-edit
  validation hook fires automatically on write" is gone — `cp` runs through Bash
  and is not intercepted. No other `cp` into `kb/` remains in `workflows/`.
- `pool_candidates` is region-scoped by default (`load_region_graph`), with
  `--this-file-only` to opt out. On cerebellum the region view sees 11 edges
  where the per-file view sees 2.
- `find_node_file` prefers the canonical definition over a stub and raises
  `AmbiguousNodeError` on a genuine duplicate, with a cached index invalidated
  on mtime change. It raises on the three `dg_*` duplicates today, which is the
  intended behaviour.
