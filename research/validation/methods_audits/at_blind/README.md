# AT-blind audit

**Audit ID:** `at_blind`  •  **Status:** active  •  **First run:** 2026-05-10
•  **Driver:** [`src/evidencell/validation/at_blind.py`](../../../../src/evidencell/validation/at_blind.py)
•  **Orchestrator:** [`workflows/validation/at_blind.md`](../../../../workflows/validation/at_blind.md)

## Question

When annotation transfer (MapMyCells) has already identified an atlas
target for a classical cell type, does evidencell's `find_candidates`
— run on markers + region + NT alone, with the AT signal disabled —
surface that same target in its top-K?

Equivalently: *how much of the AT signal does the marker pipeline
already cover, and where are the gaps?* The audit treats curated AT
evidence as oracle and measures the marker pipeline against it.

The audit is **blind**: `find_candidates` runs with `at_hits=None` and
`at_bypass=None`, so the AT signal it's being audited against is
denied to it. AT artifact loading is suppressed.

## Method

### Ground truth

For each `kb/graphs/**/*.yaml`, walk the `edges` list and pick every
edge carrying `AnnotationTransferEvidence` with
`best_f1_score ≥ f1_floor` (default 0.2). The edge's `type_a`
classical node and `type_b` atlas-stub node together with the F1
score form one test case.

Cases are restricted to atlas targets in the audited taxonomy
(`taxonomy_id` config). PRIOR_TRANSCRIPTOMIC targets (e.g. Kozareva)
are excluded because we don't have a corresponding taxonomy DB to
query.

### Per-case execution

1. Resolve the classical node's UBERON soma locations to MBA IDs.
   Primary: `anat_terms.uberon_id` lookup. Fallback: label-based
   matching via `_resolve_mba_by_name` (Latin↔English synonyms,
   hippocampal field prefix normalisation).
2. Extract positive markers (defining + neuropeptide, deduplicated),
   negative markers, NT type, sex_bias.
3. Load `precomputed_expression` for the queried rank AND rank 0
   (needed for coverage descent).
4. Call `find_candidates` with the above + `at_hits=None`,
   `at_bypass=None`. Region filter uses the permissive rule
   (strict `cell_count > 0` OR proximity `count_in_or_near_100um > 0`
   in the curator-literal anat terms; no MBA-tree expansion).
5. Look up the AT target accession in the returned candidates list.

### Outcome categorisation

| `reason` | meaning |
|---|---|
| `found` | Target is in top-K (passes the audit). |
| `below_topk` | Target appears in the survivor pool but ranks outside top-K. |
| `region_drop` | Target dropped by the region filter — no annotated cells in queried or expanded closure. |
| `nt_drop` | Target dropped by the NT filter — neurotransmitter mismatch. |
| `negative_score_or_other` | Target survived filters but failed `score >= 0` (or some categoriser didn't catch it). |

Misses include the full `expected` and `actual` dicts so a reviewer
can re-derive the verdict.

### Preflight invariants (fail loud)

| Check | Rationale |
|---|---|
| `taxonomy_db_exists` | Audit can't query without the DB. |
| `taxonomy_db_fresh` | Stale DB → mismatched anat/expression vs YAML. |
| `anat_closure_built` | Without closure, region filter silently does nothing. |
| `uberon_resolution_coverage` | Catches the OLM-style silent skip where UBERON IDs without xref + no name-fallback produced empty MBA list and effectively disabled the region filter. |

## Run history

Every run is archived at `runs/<timestamp>.json`. `latest.json`
points to the most recent. Each artifact carries config, commit,
preflight outcomes, and per-case raw data.

| Date | Commit | Config | Pass rate | Key change since previous |
|---|---|---|---|---|
| 2026-05-10 | `db4d2e1` (pre-expansion) | top-K 10, F1 floor 0.2 | 12/19 (63%) | First run on cohort-relative scoring; strict region match only. |
| 2026-05-10 | `5bb6c3d` (post-expansion) | top-K 10, F1 floor 0.2 | 16/19 (84%) | Region expansion + exact-match bonus (commit E). |
| 2026-05-11 | `5bb6c3d` (audit script fixed) | top-K 10, F1 floor 0.2 | 16/19 (84%) | Same code; audit-driver gained UBERON name-fallback so the OLM case is region-filtered properly. Headline rate unchanged but per-case rank diagnoses are now accurate. |
| 2026-05-31 | `main` (pre-#95) | top-K 10, F1 floor 0.2 | 50/77 (64.9%) | KB grew (77 AT cases vs 19); legacy `expanded_anat` walk + flat region-survival bonus. Baseline for #95. **filter_loss=2.6%, topk_loss=32.5%.** Sole filter losses are `negative_score_or_other`; 0 `region_drop` because `expanded_anat` rescues everything. |
| 2026-05-31 | issue #95 (literal anat, no KG closure update) | top-K 10, F1 floor 0.2 | 54/77 (70.1%) | Permissive filter (strict ‖ 100µm proximity), graded region score, `expanded_anat` walk removed. **filter_loss=7.8%, topk_loss=22.1%** — graded score helps real candidates rise; +5pp filter_loss reflects 3 EC supertype cases the old expansion was rescuing via taxonomic adjacency. |
| 2026-06-02 | issue #95 + KG update (`cellCountCompleteness` tags + materialised rollups) | top-K 10, F1 floor 0.2 | 54/77 (70.1%) | brain_cell_KG now materialises `exact` rollup edges at non-painted parent terms (e.g. SUPT_0042 → MBA:909 *Entorhinal area* now present). **filter_loss=3.9%, topk_loss=26.0%.** The 3 EC supertypes moved from `region_drop` → `below_topk` (now in the candidate pool but below top-10). Net survival unchanged because they don't score high enough to overtake other candidates; visible to a curator who increases top-K. Pipeline now diagnoses these as ranking-stage losses (curator-actionable) rather than filter losses (silent drops). 402K anat rows (was 247K) reflecting new rollup edges. |

## Findings

### Region expansion to 1 parent level is decisive

The headline rate jump from 63% → 84% comes from rescuing 4 high-F1
targets whose MBA annotations sit in *sibling* sublayers of the
queried region rather than as exact matches. The MBA hierarchy is
flat enough that one level up — `MBA:382 Field CA1` for any CA1
sublayer — captures all the relevant sibling layers in one step.

Rescued at commit E (post-expansion):

| Classical | Target | F1 | Why strict match dropped it |
|---|---|---|---|
| neurogliaform → SUPT_0203 | 0.90 | Target has cells in CA1 stratum radiatum; queried CA1 stratum lacunosum-moleculare. |
| ivy → SUPT_0203 | 0.90 | Same target as neurogliaform; queried CA1 pyramidal layer. |
| p_lm → SUPT_0219 | 0.98 | Target predominantly CA3; queried CA1 pyramidal. Has minor CA1 stratum oriens cells (n=89) which the expansion catches. |
| bistratified → SUPT_0216 | 0.49 | Target's 818-cell major region is CA1 stratum oriens; queried CA1 pyramidal layer. |

The single remaining region_drop (axo_axonic → SUPT_0204, F1=0.61)
is a genuine biological mismatch: target is in Piriform area
(olfactory), LCA with CA1 pyramidal sits at `MBA:8 "Basic cell groups
and regions"` (depth 2 from root). Expansion to 1 level up correctly
does not rescue it.

### Below-top-K cases

Both remaining misses have honest mechanistic explanations from the
audit's raw `actual` data:

1. **p_lm → SUPT_0219** (F1=0.98, rank 15, score 1.0): Target's
   predominant cells are in CA3, not CA1; region expansion lets it
   pass the filter, but its cohort-percentile scoring doesn't favour
   it among CA1 candidates. The F1=0.98 is itself suspect at this
   level of regional mismatch — likely reflects MapMyCells assigning
   p_lm cells broadly across the Sst supertype family.

2. **olm_hippocampus → CLUS_0769** (F1=0.67, rank 38, score 3.0):
   `expression_detail` shows `Chrna2` at value 0.0 on this cluster
   while sibling Sst Gaba_3 clusters (0768, 0770, 0772, 0773) all
   express it (~0.5–0.8). The absence penalty fires (−1) and
   distinguishes CLUS_0769 from its Chrna2-positive siblings. The
   F1=0.67 on this edge is actually the parent supertype SUPT_0216's
   F1 — verified by looking up the AT artifact for the same run,
   where CLUS_0769 is not among hits with F1 ≥ 0.2 (the
   cluster-level hits are CLUS_0767 F1=0.29, CLUS_0768 F1=0.44,
   CLUS_0772 F1=0.27). The miss is partly a data-attribution
   imprecision; biologically, the marker pipeline is correctly
   distinguishing a Chrna2-negative sub-cluster within the OLM-
   adjacent supertype family.

### Stratified by F1 (run with F1 floor 0.0 for fuller picture)

| F1 bucket | n | Found in top-10 | Hit rate |
|---|---|---|---|
| F1 ≥ 0.5 | 18 | 15 | 83% |
| 0.3 ≤ F1 < 0.5 | 1 | 1 | 100% |
| 0.1 ≤ F1 < 0.3 | 0 | — | — |
| F1 < 0.1 | 17 | 6 | 35% |

At F1 ≥ 0.5 — the regime where AT itself is informative — marker
filtering recovers ~83% of cases. Below F1 0.3 the AT signal becomes
noisy; the 35% pickup of F1<0.1 cases is a coincidence floor, not
evidence the marker pipeline is doing real work there.

## Decisions informed

- **`region_expand_levels=1` default in `find_candidates`** (commit
  E on the Phase 1 branch). The 63%→84% jump in this audit was the
  primary evidence at the time; without taxonomic expansion the audit
  was losing high-F1 cases. **Superseded (issue #95):** the parameter
  and the `expanded_anat` walk were removed when find_candidates
  switched to a permissive `cell_count > 0` OR
  `count_in_or_near_100um > 0` filter against curator-literal anat
  terms. The 100µm proximity data captures the boundary / sibling-
  sublayer cases the MBA-tree walk was rescuing; the brain_cell_KG
  update on 2026-06-02 materialised `exact` rollup edges at
  non-painted parent terms (e.g. SUPT_0042 → MBA:909 *Entorhinal
  area*) so curator queries at any MBA level hit the right edge
  directly. **`cell_count_completeness`** flags rollups that
  include non-painted descendants as `lower_bound` so Stage B and
  report-time agents can caveat citations.
- **Validation metric exposed** — `summary_stats.at_target_survival`
  now reports `filter_loss_rate` + `topk_loss_rate` + `survival_rate`
  alongside the existing `pass_rate`. The split lets the write-up
  distinguish "found vs missed" from "filter-stage loss vs ranking-
  stage loss" — the actionable diagnosis is different for each.
- **LLM adjacency wiring reverted** (commit A on the Phase 1 branch).
  Originally region-pending candidates went through a batched LLM
  call. Audit-driven cost/benefit (~500 candidates per query at
  rank 1; few interesting cases) plus the v1 audit showing
  programmatic-only expansion already rescued the high-F1 misses,
  led to the revert. The `llm_adjacency` module was finally
  deleted in issue #95 alongside the region-filter overhaul —
  proximity-based filtering subsumes its intended use case.
- **Top-K default 10 (rather than 5)** (commit D). The audit
  measured rank distribution of valid AT hits to set a sensible K;
  at 10 we capture meaningful below-the-top cases without diluting
  the Stage B mapping-subagent workload.

## Limitations

- **Hippocampus bias.** All 19 cases in the F1≥0.2 set are hippocampal
  interneurons. Broader regional coverage requires more curated AT
  evidence (or auto-mining `kb/annotation_transfer_runs/*/f1_matrix.csv`
  with a curator-supplied `source_label → classical_id` map, which
  doesn't currently exist in the schema).
- **F1 attribution.** A small number of edges carry the parent
  supertype's F1 on a cluster-level edge (the CLUS_0769 case). The
  audit takes the edge's `best_f1_score` at face value; this can
  produce misleading "below_topk at high F1" diagnoses.
- **Synonym fallback coverage.** `_resolve_mba_by_name` covers
  hippocampal nomenclature well. A new region (e.g. specific
  hypothalamic subnuclei) without xref AND without a synonym entry
  would re-introduce the silent-skip failure mode — caught by the
  preflight `uberon_resolution_coverage` check, but the operator
  needs to either extend the synonym table or accept the skip
  explicitly via `--force-preflight`.

  Two upstream options worth considering rather than maintaining the
  synonym table indefinitely in `_resolve_mba_by_name`:

  1. **Agentic mapping at taxonomy-ingest time.** When a taxonomy
     ingest encounters an MBA term whose UBERON xref is missing,
     run an agentic step that combines OLS lookup with context +
     latent knowledge to propose a UBERON ID, write it back to the
     taxonomy reference store flagged as agentic so a curator can
     review. Scope: inside evidencell, in the ingest workflow.
  2. **Agentic extension of the MBA itself.** Build (probably
     outside evidencell) an agentic pipeline that proposes MBA →
     UBERON xref additions, contributes them upstream to the MBA
     release or maintains them as an importable supplement. Higher
     leverage; benefits any consumer of MBA, not just evidencell.

  Tracked as [issue #50](https://github.com/Cellular-Semantics/evidencell/issues/50).
- **Single-target lookup.** The audit asks "is this exact accession
  in top-K?" If the marker pipeline ranks a *sibling* cluster of the
  AT target highly, we currently call that a miss even when the
  biology is equivalent. A "supertype family overlap" relaxation is a
  reasonable extension (TODO).

## How to run

```
just validate-at-blind                            # top_k=10, f1_floor=0.2
just validate-at-blind --top-k 20 --f1-floor 0.3
just validate-at-blind --force-preflight          # skip past assertion failure (records skip)
```

Run artifact lands in `runs/<timestamp>.json`. `latest.json` is
overwritten on each run.
