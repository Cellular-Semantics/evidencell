# KB index: an in-memory knowledge graph over `kb/graphs`

Status: **proposed**. Branch `kb-index-phase1` implements Phase 1 only.
Baseline: `9bcad1a` (main after #164, #165). Figures in "Scale" and Phases 0–4
re-measured there; the "What `strip-stubs-1-2` already did" section records
the state at `3014944` and is left as written.
Related: **#125** (one file per lit type — this plan builds its required
infrastructure), #158 (fat-stub plan), #161, #162, #163.

---

## Why

The Phase 3 graph split (`732d298` → `85f128c`) replaced one-document-per-region
with one-document-per-component. The split unit is the connected component, not
the classical type, because `validate.structural_checks` requires both endpoints
of every edge to resolve **within the same document**. Hippocampus went from 4
files to 33.

A post-split review found no breakage — 873 tests pass, all KB files validate,
QC reports 0 new findings, and the split was provably edge- and hash-neutral
(421 edges / 142 stale, identical either side of `85f128c`). But it found a
consistent shape across six separate problems:

| Symptom | Root |
|---|---|
| `at_coverage` reads one file, reports as if it read the region (#162) | file-awareness in region-scope logic |
| `pool_candidates` needed a bespoke `load_region_graph` to survive | same |
| 75 atlas stub ids duplicated across files, agreement unchecked | no cross-file view |
| Callers hand-type a path that no longer matches the node name | no node→file resolution in write paths |
| QC baseline keys findings on paths; a rename re-keys the backlog | path as identity |
| ASTA ingest writes monolithic files; nothing owns the layout invariant | no layout check |

None are split bugs. They are the cost of **file-awareness leaking into logic
that should not have it**. The fix is to query a unified graph built from the
source files, leaving the files as the edit surface.

This is not a new direction. **#125** already tracks the one-file-per-lit-type
target layout, and its "Consequences / required infrastructure" section asks for
exactly three things:

> - Repo-level consistency + id-uniqueness CI check … nothing today prevents
>   two files defining the same id, a stub drifting from its canonical node, or
>   a node_id diverging from its filename.
> - Cross-file convergence detection … `pool-candidates` is single-`GRAPH_FILE`
>   today.
> - `find_node_file()` lookup utility.

Those are Phase 2, Phase 2, and Phase 1 below. **This plan is the
infrastructure half of #125**, generalised so each consumer stops solving it
privately.

Most of the machinery already exists under other names. `paths._node_index()`
is already a whole-KB, mtime-invalidated index — it rglobs every YAML under
`kb/graphs`, builds `node_id → [(file, is_stub)]`, and rebuilds when any file's
mtime changes. `find_node_file` is one query against it. The question is not
whether to adopt the pattern but whether to generalise it.

---

## Scale, and why the taxonomy DB stays

|  | `kb/graphs` | `kb/taxonomy/CCN20230722` |
|---|---|---|
| Size | 2.9 MB | 57 MB |
| Content | 92 files, 669 nodes (96 canonical + 573 stub instances), 567 edges | 6,523 nodes over 5 levels |
| Full parse | **1.73 s** | **135 s+** (supertype 31.5 s, cluster 103.8 s) |
| Changes | every curation session | on taxonomy re-ingest |
| Viable per-invocation | yes | no |

`cluster.yaml.gz` is gzipped to stay under GitHub's 100 MB file limit. The
in-memory approach does not transfer; parsing taxonomy per CLI call would turn
a 2-second command into a 2-minute one.

**The taxonomy SQLite DB is not replaced.** Two tiers, same policy, different
mechanism:

| | Edit surface | Query surface | Build | Staleness |
|---|---|---|---|---|
| Mapping graphs | YAML | in-memory index | implicit, on read | impossible — mtime stamp |
| Taxonomy | YAML | SQLite | explicit (`just build-taxonomy-db`) | real — needs freshness checks |

This is existing policy, already stated in CLAUDE.md for taxonomy ("the DB is
the query interface; YAML is the edit interface"). The plan applies the same
discipline to `kb/graphs`, choosing the implementation by scale.

**What changes is the façade.** Callers should not know which tier a node lives
in. The index exposes one `get_node(id_or_accession)` resolving lit nodes from
memory and atlas nodes through the taxonomy DB — which `render._node_b_info`
already does by hand with a per-process `db_cache`.

Note `CS202106160` has complete YAML but **no DB built**. The index must handle
a taxonomy with no DB, falling back to YAML or failing explicitly — never
silently returning empty.

---

## What `strip-stubs-1-2` already did (#158 steps 3–6)

Commit `3014944` landed before this plan was written and changes its shape.

Stripped 329 fields from 153 stubs across 34 files; fat-stub excess 234K → 0.8K.
**477 stub instances remain across 290 distinct ids, 75 of those ids in more
than one file.** Two stubs stay deliberately fat. A new `stub_shape` WARN check
(`qc_content.py:517`) fires corpus-wide on anything beyond `THIN_STUB_FIELDS`,
matching exactly those two, both baselined.

Three consequences this plan must absorb:

**1. Stub divergence is gone; duplication is not.** Divergent-content stub ids
went 5 → **0**. `stub_shape` enforces *shape*, not *agreement between copies*.
The 75-way duplication surface persists, but with thin uniform stubs the
realistic drift risk is much lower, which demotes the proposed agreement check
from "needed" to "cheap insurance, or skip if Phase 4 lands".

**2. The hash-invalidation risk is now demonstrated, not theoretical.**
`rationale_stale` moved 84 → 117 purely from thinning, because
`_rationale_hash.canonical_payload` hashes the **whole** `taxonomy_node` dict.
No fact changed; `gen-facts` was byte-identical apart from an improvement. The
commit notes this "will not recur now that stubs are thin and stable" — true
only while stubs *exist*. Removing them in Phase 4 changes `taxonomy_node`
again and would invalidate every edge a second time unless the hash is first
redefined over a canonical projection. **This is now the single highest-risk
item in the plan.**

**3. The taxonomy DB dependency deepened.** `render._node_b_info` gained a DB
fallback for `taxonomy_level`, improving 392 edges — but that field now has no
stub to fall back on. Measured on this branch with no DB present:

```
edges: 16   supertype EMPTY: 16   n_cells EMPTY: 16   taxonomy_level EMPTY: 16
```

Before the strip, `taxonomy_level` survived DB loss wherever a stub happened to
be fat. The strip replaced a silent *inconsistency* with a uniform silent
*dependency*. That makes the fail-closed DB work more urgent, not less.

---

## Design

Representation is **parsed dicts** — what every writer already manipulates —
plus derived maps. LinkML stays the validation gate, not the runtime object
model. This routes around #161 rather than blocking on it.

```
src/evidencell/kb_index.py

  nodes:              id        -> (doc, source_file, is_stub)
  edges:              id        -> (doc, source_file)
  by_lit:             node_id   -> [edge_id]
  by_region:          region    -> [node_id]
  stubs_by_accession: accession -> [(file, stub)]
  _stamp:             tuple of (path, mtime_ns) over kb/graphs/**/*.yaml
```

Built by the loop `paths._node_index()` already runs, keeping parsed content
instead of discarding it and stamping provenance on the way through. ~200 lines.

Three invariants:

1. **Read-only.** Writes go to files; the index is rebuilt, never written through.
2. **Fail closed.** If currency cannot be verified, raise. Never return a best
   guess. `kb_io.validate_kb_doc` already models the instinct — "an unavailable
   validator must not read as valid".
3. **Provenance on nodes *and* edges.** All 567 edges currently sit in their lit
   node's home file, but that is *enforced* by `structural_checks`, not chosen —
   and Phase 4 removes the constraint. Capturing edge provenance is free now and
   a painful retrofit later.

---

## Phases

### Phase 0 — prerequisites (independent; do regardless)

| Item | Why it blocks |
|---|---|
| ~~**#163** ASTA ingest → component layout~~ | **Done in code** (#164, merged): ingest now writes one node file per type directly into `kb/graphs/{region}/`, under the pre-edit hook. Issue still open |
| **#162** `at-coverage` region scope | producing wrong answers today |
| **Taxonomy DB fail-closed** | 6 bare `sqlite3.connect` in `taxonomy_db.py`. `render` guards but silently. No `.db` is committed (gitignored), so a fresh worktree degrades on every edge until `just build-taxonomy-db` runs. Now costs 3 fields on every edge, not 2 |
| **Single validated writer** | a derived index is only as good as its sources; `kb_io.write_kb_yaml` still has zero callers. #163 does **not** cover this: it moved ingest onto the hook-covered `Write` path. This item is the programmatic writers in `src/` the hook never sees (`stage_b_emit`, `rationale_writeback`, `refresh_*`, `discovery_score_backfill`, `taxonomy_ops`, `at_metrics`). Needs one validation gate with two serialisers — PyYAML for generated docs, ruamel for in-place edits. Required before Phase 3, not Phases 1–2 |
| Doc rot | dead graph paths in `justfile` + CLAUDE.md |

**#161 is deliberately excluded** — the dict-based index does not need it. It is
required only for Phase 5.

### Phase 1 — the index (additive, reversible) ← this branch

Build `kb_index.py`. Reimplement `find_node_file` on it, preserving its
signature and `AmbiguousNodeError` behaviour. No other caller changes.
Behaviour delta: zero. Risk: one module to revert.

*Done when:* full suite passes unchanged and `test_find_node_file.py` passes
against the new backend.

### Phase 2 — port the region-scope consumers

- `at_coverage` → index query, replacing the Phase 0 minimal fix
- `pool_candidates.load_region_graph` → index query, deleting the bespoke merge
- `qc_content` cross-file checks → index queries
- **New:** one-component-per-file check — gives the layout invariant an owner so
  ASTA drift surfaces immediately
- **Optional:** stub-agreement check. Lower value than when first proposed
  (divergence is 0 and `stub_shape` covers shape); skip if Phase 4 is near

*Done when:* no module under `src/` globs `kb/graphs` directly.

### Phase 3 — provenance-driven write targeting

Recipes take node ids, not paths:

```
just rationale-writeback <report> chrna2_olm_subfamily_chamberland
```

Both demonstrated failure modes — `FileNotFoundError` on a guessed path, and
ten "no such edge" errors on a wrong-but-existing one — become unreachable.

Add a placement policy for *new* content, the one thing provenance cannot
supply: a new edge goes in its lit endpoint's file; a new lit node starts its
own file. That is the splitter's component rule stated forward.

Writes stay file-based and ruamel round-tripped. Comment preservation is
non-negotiable.

### Phase 4 — remove stubs (content change, separately gated)

Relax `structural_checks` from "endpoints resolve in-document" to "endpoints
resolve in the index", then delete the stub instances (573 at `9bcad1a`). Finding #3 stops
being expressible rather than getting a new check.

> **This reverses a recorded design decision and must be argued, not assumed.**
> #125's core decision of 2026-07-09 was the opposite: keep `validate.py`'s
> in-document rule and satisfy it with thin stubs for both atlas and
> counterpart-lit targets — "Net: no `validate.py` change and no schema change
> are required to start." That was the right call for starting, and the stubs
> it chose are now thin and uniform (#158). Phase 4 claims the index makes the
> in-document rule unnecessary; #125's author may reasonably disagree. Settle
> it on #125 before writing code, and note the decision there either way.

Three hard preconditions, all new since `3014944`:

> **(a) Redefine the rationale hash first.** Demonstrated, not hypothetical:
> thinning stubs moved `rationale_stale` 84 → 117 with no fact change. Removing
> them changes `taxonomy_node` again. Define `canonical_payload` over a fixed
> projection matching `THIN_STUB_FIELDS` and the change stays neutral — the same
> discipline that made the file split neutral. Skip this and all 567 edges need
> re-synthesis.
>
> **(b) Prove the taxonomy store can supply every stripped field.** It currently
> cannot. `CS20230722_SUPT_1145` keeps `n_cells=254` because the taxonomy lacks it
> — and it is not a one-off: **18 of 1201 supertypes, 10 of 338 subclasses, 3 of
> 34 classes** have no `n_cells`. `CS20250428_GROUP_0016` (HMBA BG,
> `CCN20250428`) has no store at all until that taxonomy is ingested. Phase 4 needs a preflight that every stub field is
> recoverable, and a decision for those that are not.
>
> **(c) Taxonomy DB fail-closed (Phase 0).** Once atlas nodes resolve only
> through the store, an unusable store means edges with no resolvable target.
> That must fail loudly.

*Exit criterion:* promote `stub_shape` from WARN to ERROR — or delete it, since
with no stubs it has nothing to check.

### Phase 5 — export (optional, downstream)

Project to `brain_cell_KG`, the external neo4j `kg_query.py` already talks to.
One-directional, regenerated from source, never read back as truth. RDF via
`gen-owl` is better supported in the LinkML toolchain than Cypher and fits a
schema that is already CURIE-heavy. **Requires #161** — an evidence item cannot
be typed without a discriminator.

---

## Why not Cypher / a graph database

1. **Scale.** 669 nodes, 567 edges, 2.9 MB. Neo4j is a daemon, a connection, an
   auth story, a second copy of truth, and a new failure class — for data that
   parses in under 2 s. The bolt handshake would cost more than a full rebuild.
2. **Document model vs property graph.** 59 classes; `CellTypeNode` has 38
   attributes, `MappingEdge` 23, with `PropertySource` nested on individual
   properties. Projecting that means a node/relationship/blob decision for 59
   classes — a second schema, hand-written and hand-maintained in lockstep,
   with no well-maintained `gen-cypher` to carry it.
3. **The graph is two classes.** Everything else is payload hanging off
   `CellTypeNode` and `MappingEdge`. Real queries are dict lookups and
   comprehensions; nothing here is a variable-length path query.

**Fit with mtime invalidation.** Because the representation is the parsed files
plus maps derived in the same pass, exactly one thing can invalidate it: a file
changing. The mtime stamp captures that completely. A projected store breaks the
property — its staleness is independent of file mtimes, so it needs its own
freshness tracking, which is the machinery `taxonomy_db_freshness` provides and
which we already caught degrading silently. Choosing in-memory *is* choosing
trivially-correct invalidation.

If the ~1.7 s cold build hurts CLI ergonomics, the answer is a msgpack cache
keyed on the same mtime stamp — still derived, still fail-closed, still not a
database. Measure real usage first.

---

## Risks

| Risk | Mitigation |
|---|---|
| Phase 4 invalidates all 567 verdicts | precondition (a) — canonical projection decided up front |
| Phase 4 blocked by taxonomy gaps | precondition (b) — preflight recoverability; 31 known missing `n_cells` |
| Index silently stale → writer targets wrong file | never persist provenance; mtime stamp + raise-on-unverifiable |
| Cold build cost | measure; msgpack cache only if justified |
| Scope creep into a graph database | the graph is two classes and 567 edges |
| Phases 1–3 become a reason to defer Phase 0 | Phase 0 items are independent; #162 is live |

---

## Recommendation

Phase 0 now, in parallel with the ASTA work. Phase 1 is a contained ~200-line
addition evaluable on its own merits. Phases 2–3 deliver most of the value and
are fully reversible. Phase 4 carries the real content risk and should be its
own decision, taken after 1–3 have been in the repo long enough to trust — and
not before preconditions (a) and (b) are resolved.
