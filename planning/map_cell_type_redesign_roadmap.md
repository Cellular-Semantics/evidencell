# map-cell-type redesign — mini-roadmap

Working roadmap for overhauling marker/expression scoring, candidate
finding, mapping-edge schema, and verdict assignment across
`workflows/map-cell-type.md`, `src/evidencell/taxonomy_db.py`, and
`schema/celltype_mapping.yaml`. Recorded 2026-05-08, expanded into a
phased roadmap on 2026-05-09 to integrate with the SSSOM/SKOS schema
discussion in [issue #30](https://github.com/Cellular-Semantics/evidencell/issues/30)
and the OLM-driven splitting question in
[`adaptive_mapping_loop_design.md`](adaptive_mapping_loop_design.md).

**Status:** best plan so far, not yet filed as PR-scoped GitHub issues.
Phase 1 is independent and ready to scope first. Phases 2–4 have open
prerequisites flagged below.

---

## 0. Roadmap overview

Four phased PRs with explicit dependencies. Each phase is a separately
scopeable issue / PR; later phases benefit from the schema migration
done in phase 2.

| Phase | Scope | Schema impact | Depends on |
|---|---|---|---|
| **1** — Marker scoring core | Stage A scoring overhaul: presence/absence credit, neuropeptides into Stage A, hard prerequisite filters, top-K cutoff, drop A→B gating, AT artifact persistence + scoring, proactive enrichment, heterogeneity coverage at rank ≥ 1 | None | — |
| **2** — Mapping schema overhaul ([#30](https://github.com/Cellular-Semantics/evidencell/issues/30)) | SSSOM-aligned predicates; predicate / cardinality split; `lit_type` / `taxonomy_type` rename; `mapping_justification`; `reconciliation_note` + `reviewed_by`; numeric `confidence_score`; SSSOM TSV export | Heavy: schema + KB-wide YAML rewrite | #30 discussion converging |
| **3** — Verdict at report time | Move `confidence` (ordinal) and `confidence_score` (numeric) assignment from Stage B → report time; add `rationale` + `report_path` + currency hash; gen-report write-back; Stage B becomes pure structured data | Schema additions (small if landed alongside phase 2) | Phase 2 |
| **4** — Joint heterogeneity → splitting | Atlas-side coverage (phase 1) + classical-side lit subtypes (`adaptive_mapping_loop_design.md` OQ 2) → splitting recommendation in reports; KB write-back of split classical nodes | Uses phase-2 `BROADER` + `mapping_cardinality: 1:n`. No further schema changes likely. | Phases 1 + 2; coordinates with `adaptive_mapping_loop_design.md` |

The §§ 1–2 sections below give shared foundation (current state +
bigger picture). Then §§ 3–6 are one section per phase. § 7 lists
cross-cutting open questions; § 8 lists why-better per-phase; § 9
lists files touched per-phase.

---

## 1. The bigger picture: what scoring is used for

Two distinct scoring activities happen during a mapping. They use different
inputs, produce different outputs, and are run by different parts of the
system. Conflating them obscures what each change actually affects.

### 1.1 Stage A — candidate-finding score

**Where:** `find_candidates` in `src/evidencell/taxonomy_db.py`, invoked via
`just find-candidates` from `workflows/map-cell-type.md` Step 0a.

**Inputs:** classical node's property signature (markers, NT type, soma
locations, sex_bias) + taxonomy DB of candidate atlas nodes (with optional
`precomputed_expression`).

**Output:** an integer score per candidate atlas node, used to rank-and-cut
the candidate set the rest of the pipeline operates on.

**Consumers today:**
- The Step 0b refinement subagent reads the JSON candidate list and adds
  qualitative assessments (STRONG / PLAUSIBLE / WEAK / EXCLUDE) for the
  curator gate.
- The curator at the Step 1 gate reviews the ranked list and confirms which
  candidates to pursue.
- Implicitly, by determining what makes the shortlist, this score gates which
  candidates ever get a `MappingEdge` written.

**Consumers under the proposal:**
- No curator gate after Stage A. The cutoff (score threshold or top-K)
  directly determines which candidates the Stage B mapping subagent is
  spawned for.
- Refinement subagent shrinks; its remaining role is enrichment of the
  candidate record fed into Stage B (e.g. child-cluster context for
  supertypes), not decision-support for a now-removed gate.

### 1.2 Stage B — mapping-edge confidence

**Where:** the Step 3 mapping subagent in `workflows/map-cell-type.md`.

**Inputs:** classical node + chosen atlas node's full property record (incl.
`precomputed_expression`) + any literature evidence + any AT evidence.

**Output:** a `MappingEdge` YAML with:
- `property_comparisons[*]` — per-property alignment
  (CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED) with verbatim values
  on both sides.
- `evidence_items[*]` — typed, citable evidence
  (LITERATURE / ATLAS_METADATA / ANNOTATION_TRANSFER / …) each labelled
  SUPPORT / REFUTE / PARTIAL / NO_EVIDENCE.
- `confidence` — HIGH / MODERATE / LOW / UNCERTAIN, set by an LLM applying
  the decision guide:
  - HIGH: ≥2 independent convergent evidence types, ≥1 experimental
    (annotation transfer, electrophysiology, morphology). Not achievable
    from literature alone.
  - MODERATE: ≥2 independent evidence items with consistent support.
  - LOW: single item, or consistent but weak/indirect evidence.
  - UNCERTAIN: contradictory, ambiguous, or minimal.

**This score is qualitative.** It does not consume the Stage A integer; it is
re-derived per edge from the structured evidence written into the
`MappingEdge`.

### 1.3 Relationship between the two

Today: Stage A determines *who gets a Stage B*. Stage B determines
*confidence in the resulting edge*. The link is set-membership, not numeric.

Under the proposal: same logical relationship, but the Stage A cutoff
becomes the only filter (no curator gate in between), so Stage A's recall
matters more — anything wrongly excluded never reaches the report. This
argues for a generous cutoff and for ensuring scoring captures all signals
that meaningfully separate plausible from implausible candidates (hence
including neuropeptides and AT, and giving expression-above-noise its own
credit).

---

## 2. Current scoring system (Stage A)

### 2.1 Inputs extracted from the classical node

`_cmd_find_candidates` ([`src/evidencell/taxonomy_db.py`](../src/evidencell/taxonomy_db.py)):

| Classical-side field | Used as | Notes |
|---|---|---|
| `defining_markers[*].symbol` | `markers` (positive) | Scored at Stage A |
| `negative_markers[*].symbol` | `negative_markers` | Scored at Stage A |
| `neuropeptides[*].symbol` | — not extracted — | **Silent at Stage A** |
| `nt_type.name_in_source` | `nt_type` | Prefix match, +2 if matched |
| `anatomical_location[*]` (SOMA only) | `anat_root_ids` | UBERON→MBA resolution, +2 if matched |
| `sex_bias` (`MALE_BIASED` / `FEMALE_BIASED`) | optional criterion | +1 at rank 0 if matched |

### 2.2 Candidate-side data sources for a queried gene

| Source | Type | Coverage |
|---|---|---|
| `precomputed_expression.genes` | Quantitative mean expression (HDF5 → YAML) | Sparse: only genes added via `just add-expression` |
| `defining_markers_scoped` | JSON-array metadata flag (within-subclass discriminator) | Set at taxonomy ingest |
| `defining_markers` | JSON-array metadata flag (looser) | Set at taxonomy ingest |
| `tf_markers` | JSON-array metadata flag (TF subset) | Set at taxonomy ingest |
| `merfish_markers` | JSON-array metadata flag (MERFISH panel subset) | Set at taxonomy ingest |
| `np_markers` | Packed string `"Sst:9.2,Crh:4.4"` (symbols + ingest scores) | Set at taxonomy ingest |

`node_markers` = union of symbols from the four JSON arrays + parsed
`np_markers` symbols (scores discarded).

### 2.3 Per-criterion scoring

**Region** (anat closure transitive match): +2 if any classical soma
location resolves to an MBA ID present on the candidate.

**NT type** (prefix match, propagated to non-leaf ranks via cluster
aggregation): +2 if matched.

**Positive markers** (per gene `m`):
```
if m in node.precomputed_expression:
    if val ≥ MIN_DETECTABLE:
        sibling_pct ≥ 0.80 → +2
        sibling_pct ≥ 0.50 → +1
        sibling_pct < 0.50 → 0
        global_pct  ≥ 0.90 → +1 additional (only on top of a sibling-pass)
    else:                # below detection
        0
elif m in node_markers:  # metadata fallback
    +1                   # binary; ignored entirely if m is in precomputed_expression
else:
    0
```

**Negative markers** (per gene `m`):
```
if m in node.precomputed_expression:
    if val ≥ MIN_DETECTABLE:
        sibling_pct ≥ 0.80 → −2
        sibling_pct ≥ 0.50 → −1
        sibling_pct < 0.50 → +1   # absence confirms expectation
    else:                # below detection
        0
else:
    0                    # no metadata fallback for negative markers
```

**Optional criteria** (registry in `_OPTIONAL_CRITERIA_REGISTRY`):
- `sex_bias`: at rank 0, +1 if `male_female_ratio` matches the classical
  node's expected direction (< 0.3 for female-biased, > 3.0 for
  male-biased).

### 2.4 Reference distributions for percentiles

For a queried gene G:
- **Global** reference: every value of G in `precomputed_expression`
  across all nodes at the queried rank that have G enriched.
- **Sibling** reference: same, restricted to nodes sharing the candidate's
  `parent_id`.

Because `precomputed_expression` is enriched per-classical-type on demand
(Step 2b), the reference for G is "nodes that happen to have been enriched
for G" — a curation-history-shaped subset, not the full atlas.

### 2.5 Aggregation

Score is the sum across all criteria. Candidates with score > 0 are kept,
sorted descending. The `find-candidates` CLI emits the top N (default 20 at
rank 1, 30 at rank 0).

A per-candidate `_expression_detail` (val, reliability, sibling/global pcts,
per-gene contribution) is computed but **not emitted** in the JSON output.

### 2.6 Identified gaps

| # | Gap | Affects |
|---|---|---|
| 1 | "Expressed above noise" earns 0 (sibling-non-discriminating, on-but-low-rank) | defining_markers via precomputed_expression |
| 2 | Defining marker absent (val < MIN_DETECTABLE) earns 0 — no penalty | defining_markers via precomputed_expression |
| 3 | Neuropeptides not extracted from classical node | all sources |
| 4 | Negative markers have no metadata fallback (only scored via precomputed) | negative_markers via DB metadata cols |
| 5 | `np_markers` ingest-time expression scores dropped at query time | np_markers packed col |
| 6 | DB metadata flag is silent when `precomputed_expression` covers the gene (else-branch only) | defining_markers via DB metadata cols |
| 7 | `_expression_detail` computed but not emitted | all (downstream visibility) |
| 8 | Percentile reference is curation-history biased (sparse enrichment) | all percentile-scored genes |
| 9 | AT evidence not consumed by Stage A scoring | annotation_transfer |

---

## 3. Phase 1 — Marker scoring core (proposed Stage A)

*No schema impact. Independent of other phases. Ready to scope as the
first issue / PR.*

### 3.0 Phase scope summary

This phase delivers the marker/expression scoring fixes (gaps 1–9 from
§ 2.6), restructures Stage A as a hard-prerequisite-filter +
soft-scoring system, drops the Stage A→B curator gate, persists
annotation-transfer F1 hits as a Stage A signal, and adds
heterogeneity-aware scoring at non-leaf ranks. Stage B confidence
assignment stays where it is (until phase 3). The schema is not
touched.



### 3.1 Inputs extracted from the classical node

Add neuropeptides as a third positive-marker channel (gap 3):

| Classical-side field | Used as |
|---|---|
| `defining_markers[*].symbol` | positive markers (defining) |
| `neuropeptides[*].symbol` | positive markers (neuropeptide) |
| `negative_markers[*].symbol` | negative markers |
| `nt_type` | unchanged |
| `anatomical_location` (SOMA) | unchanged |
| `sex_bias` | unchanged |

Treating defining markers and neuropeptides as a unified positive-marker
channel is the simplest first cut. Whether they should be weighted
differently (e.g. neuropeptide hits at half weight) is open.

### 3.2 Data layer: proactive enrichment (option A)

Drop the per-mapping `Step 2b` enrichment. Instead, batch-enrich every
taxonomy node at every relevant rank with `precomputed_expression` for the
union of all KB-mentioned marker genes
(`defining_markers ∪ neuropeptides ∪ negative_markers` across every
classical node in the KB).

Trigger: on classical-node ingest, or as a periodic batch over the KB.

Consequence: any gene that's a marker for any classical type has full
quantitative data on every taxonomy node. The percentile reference for G
becomes "every node in the taxonomy" — unbiased and complete (gap 8).

Option B (full HDF5 matrix in DB) considered and rejected; its only
advantage is querying genes that have never appeared on a classical node,
which the current pipeline never does.

### 3.3 Hard prerequisite filters (new)

Region and NT change role: they stop being additive scoring contributions
and become hard filters applied before scoring. Candidates that fail are
dropped from the pool, not penalised. Markers and AT then determine the
ranking of the surviving pool. Rationale: a Pvalb interneuron in cortex
should not compete against thalamic candidates regardless of marker
overlap; absolute marker scores are not comparable across classical types
of differing marker-list size, so additive bonuses for region/NT distort
top-K ranking.

**Region filter — programmatic + LLM-adjudicated.**

1. Programmatic check: does the candidate have any cells annotated as
   being in the queried soma region? (Use the existing anat closure /
   anat-table lookup; do not require the candidate's *primary* region to
   match — any presence in the region passes.) Whether the match is
   exclusive is a Stage B / mapping-type concern, not a Stage A
   eligibility one.
2. If the candidate has zero cells in the queried region but does have
   annotated regions elsewhere, fall back to an LLM adjacency check:
   ask whether any of the candidate's annotated regions are adjacent
   or closely associated with the queried region. LLM latent knowledge
   handles this better than MBA hierarchy alone (e.g. CA1 ↔ subiculum
   is closer than MBA siblings would suggest). Pass if yes, drop if no.
3. If the candidate has no anatomical annotations at all, treat region
   as unknown for that candidate and pass the filter (don't disqualify
   on missing data).

The adjacency check should be batched (one LLM call per find-candidates
invocation, listing all candidates that need adjudication and their
annotated regions) and the verdicts cached against (region, candidate
region set) to avoid redundant calls.

**Note — "in region + distant" cases.** A candidate that has cells in
the queried region *and* substantial cells in anatomically distant /
unrelated regions passes the binary filter above (any presence is
enough), but the distant-cell fraction is a weakening signal: the
cluster's identity may not be coherent with the classical type, or the
match may be partial rather than equivalent. **Phase 1 should record
the region fraction** (cells-in-queried-region / total-cells) and
**emit it in the candidate JSON output** (alongside `_expression_detail`)
without using it for filtering or scoring. The fraction is then
available downstream:

- The mapping subagent (Phase 1 Stage B, or Phase 3 reformulation) can
  cite it in property comparisons.
- It feeds naturally into Phase 2 predicate selection — a low region
  fraction supports `BROADER` or `PARTIAL_OVERLAP` rather than
  `EQUIVALENT`/`CLOSE`.
- Future tightening could weight scoring by region fraction if curator
  feedback shows the binary pass-through is too generous.

Treating distant-cell penalisation as a Phase 2/3 concern rather than
Phase 1 scoring keeps the scoring rules simple and avoids double-
penalising (once via score, once via predicate). Open question deferred
to Phase 2/3.

**NT filter — applies only when both sides are assessed.**

1. If the classical node has no `nt_type` → drop the filter (do not
   disqualify on absence of classical-side data).
2. If the candidate has no NT call (some taxonomies don't carry one)
   → drop the filter for that candidate (do not disqualify on absence
   of atlas-side data).
3. Otherwise: prefix-match (current behaviour, propagated to non-leaf
   ranks via cluster aggregation). Mismatch → drop.

**AT bypass.** Candidates with an AT F1 hit above the persistence floor
are exempt from both region and NT filters. Direct cell-assignment
evidence is allowed to overrule priors; the resulting edge may end up
refuted at Stage B / report time, but it deserves to enter the pool. AT
match without supporting region/NT becomes part of what makes the
mapping interesting.

### 3.4 Soft scoring — REVISED (Phase 1 follow-up commit B)

**Two-pass loop with cohort-relative scoring.** Pass 1 applies hard
prerequisite filters (region, NT, AT bypass) and collects survivors.
Pass 2 builds cohort percentile distributions from survivors, then
scores each survivor.

Cohort distribution for gene `g` = list of values across all survivors
(candidates without a value contribute 0.0). `cohort_pct(val, g)` =
fraction of cohort strictly less than `val`.

**Positive markers (defining + neuropeptide):** three tiers, anchored on
the absolute MIN_DETECTABLE noise floor and the cohort percentile:

| Condition | Tier |
|---|---|
| `val < MIN_DETECTABLE` | **−1**  (absent / noise floor) |
| `val ≥ MIN_DETECTABLE` AND `cohort_pct < 0.95` | **+1**  (present) |
| `val ≥ MIN_DETECTABLE` AND `cohort_pct ≥ 0.95` | **+2**  (cohort-specific) |

Coverage dampening at rank ≥ 1: positive tiers multiplied by
`sqrt(coverage)` where coverage = fraction of rank-0 (leaf) descendants
with detectable expression. Negative tiers (absence) propagate
undampened.

**Negative markers** (option A, symmetric to positives):

| Condition | Tier |
|---|---|
| `val < MIN_DETECTABLE` | **+1**  (absence confirms expectation) |
| `val ≥ MIN_DETECTABLE` AND `cohort_pct < 0.95` | **−1**  (present — contradicts) |
| `val ≥ MIN_DETECTABLE` AND `cohort_pct ≥ 0.95` | **−2**  (aberrantly high) |

**Metadata fallback** (existing gap-4 behaviour): when a gene is absent
from `precomputed_expression` but flagged in the candidate's DB metadata
marker columns (defining/MERFISH/TF/np), score `+1` for positive markers
and `−1` for negatives.

**LLM adjacency** (formerly part of region filter): reverted in
Phase 1 follow-up A. Region mismatches now hard-drop programmatically.
The `llm_adjacency` module is retained as dormant infrastructure for a
future "characterise off-target expression" use case feeding Phase 2
predicate selection.

The previous atlas-global / sibling-pct scheme is documented below for
historical reference but is no longer in use.

### 3.4-legacy Soft scoring (per-criterion, original)

Sex bias remains a soft additive bonus (rank-0 only, +1 for matching
direction).

**Positive markers** (per gene `m`, defining or neuropeptide):

| Case (post-enrichment, expression_data present) | Score |
|---|---|
| `val ≥ MIN_DETECTABLE`, sibling ≥ 0.80 | +2 (+1 if global ≥ 0.90) |
| `val ≥ MIN_DETECTABLE`, sibling ≥ 0.50 | +1 (+1 if global ≥ 0.90) |
| `val ≥ MIN_DETECTABLE`, sibling < 0.50 | **+1** ← new (presence credit, gap 1) |
| `val < MIN_DETECTABLE` | **−1** ← new (absence penalty, gap 2) |
| Gene absent from precomputed_expression | binary metadata fallback: +1 if in `node_markers`, else 0 |

Per-gene range expands from `0..+3` to `−1..+3`. Defining markers gain a
negative branch symmetric to (but milder than) negative markers' positive
branch.

**Negative markers** (per gene `m`):

| Case | Score |
|---|---|
| `val ≥ MIN_DETECTABLE`, sibling ≥ 0.80 | −2 |
| `val ≥ MIN_DETECTABLE`, sibling ≥ 0.50 | −1 |
| `val ≥ MIN_DETECTABLE`, sibling < 0.50 | +1 |
| `val < MIN_DETECTABLE` | +1 (absence confirms expectation) |
| Gene absent from precomputed_expression | **0 today; under proposal, also has a metadata fallback** (gap 4) — if `m` is flagged as defining/MERFISH/TF marker on the candidate, score −1 (contradicts the negative expectation) |

**Annotation transfer** (gap 9, new criterion):

When MapMyCells has been run for the classical type against the target
taxonomy, persist all atlas-node hits above an F1 floor (~0.2–0.3) as an
artifact, e.g. `research/{region}/at/{classical_id}_{taxonomy_id}_f1.json`.
find-candidates reads this when present.

| F1 bucket | Score |
|---|---|
| F1 ≥ 0.5 | +3 (strong direct evidence) |
| 0.3 ≤ F1 < 0.5 | +2 |
| F1 floor ≤ F1 < 0.3 | +1 |
| Below floor / absent | 0 |

Rationale: AT is direct cell-assignment evidence on the exact
(classical, atlas) pair, independent of marker overlap. A high-F1 candidate
should rank above marker-only candidates even with mediocre marker scores.
Specific weights TBD.

### 3.5 Aggregation and cutoff

Score is the sum across the soft-scoring criteria (markers + AT +
sex_bias) for candidates that passed the hard filters or qualified via
AT bypass.

**Top-K only**, no absolute threshold. Absolute scores are not
comparable across classical types — a 12-marker type can hit much
higher totals than a 3-marker type. Top-K within the qualifying pool
normalises across types and bounds Stage B subagent spawn count.
Default K = 10 (Phase 1 follow-up D bump from initial 5; with cohort-
relative scoring producing simpler tier values and limited
differentiation among presence-tier candidates, more headroom for
Stage B is reasonable).

If the qualifying pool is smaller than K, take the whole pool — under-K
is honest signal that few atlas candidates exist for this classical
type. Every selected candidate gets a Stage B mapping subagent run.

### 3.6 Output

Emit `_expression_detail` in the JSON output (gap 7) so downstream
consumers can see per-gene contributions, percentiles, and reliability
flags without re-deriving them.

### 3.7 Level-dependent scoring and heterogeneity

The data sources we have are asymmetric across ranks:

| Rank | Available signal |
|---|---|
| 0 (leaf cluster) | Pseudo-bulk mean only. Within-cluster heterogeneity not recoverable from precomputed stats; would require cell-level data — out of scope here. |
| 1+ (supertype / subclass) | Pseudo-bulk mean **plus** observable heterogeneity across rank-(N−1) children, accessible via `child_cluster_expression` on the parent YAML. |

At rank ≥ 1, the supertype mean can hide structure: a supertype with mean
Sst = 5.0 looks like a Sst+ marker, but if its child clusters are
[12.0, 8.0, 0.1, 0.0], two children don't express it at all. Currently the
Step 0b refinement subagent reads this qualitatively; the scoring function
ignores it. Under this proposal, heterogeneity becomes a structural input.

**Detection coverage** is the primary heterogeneity metric:

```
coverage(m, S) = (# children of S with val_m ≥ MIN_DETECTABLE)
                 / (# children of S)
```

It directly answers "is M a property of S, or just of one child?" — more
interpretable than CV or max/mean.

**Soft dampening, not hard.** Per-gene marker score at rank ≥ 1 is
multiplied by `coverage^0.5`:

| Coverage | Multiplier |
|---|---|
| 1.00 (uniform) | 1.00 |
| 0.75 | 0.87 |
| 0.50 | 0.71 |
| 0.25 | 0.50 |
| 0.10 | 0.32 |

Rationale: hard dampening (linear scaling) is over-confident — a
heterogeneous supertype isn't *wrong*, it's just *not uniform*. Some
classical types legitimately map to heterogeneous supertypes when only a
subset of markers is the discriminator. Soft dampening preserves the
signal without over-correcting.

**Metrics emitted alongside the score.** The `_expression_detail` block
(§3.6) gains a `coverage` field at rank ≥ 1, plus the per-child values
that drove it, so downstream consumers (Stage B mapping subagent,
report-time rationale, anyone reading candidate JSON) can see the
structure without re-deriving.

**Rank handling: query both, let scoring sort it out.** The orchestrator
already queries rank 0 and rank 1 by default. Coverage-weighted scoring
naturally selects the right level: a heterogeneous supertype loses score
relative to its actually-expressing child cluster, and the child cluster
wins its rank-0 top-K slot. No adaptive descent is needed. Adaptive
descent (automatically replacing a low-coverage rank-1 candidate with its
top-coverage child) is a more invasive future refinement and not part of
this proposal.

**Stage B alignment rules.** Coverage propagates into the property
comparisons the mapping subagent writes — a marker with coverage 0.25 on
a supertype candidate should be `APPROXIMATE` with notes citing the
coverage, not `CONSISTENT`, even if the supertype mean clears the
percentile thresholds. Step 3 prompt update needed.

**Cross-reference to subpopulation splitting.** Atlas-side heterogeneity
(this section) is one of the inputs the classical-side splitting
decision rule needs. See
[`adaptive_mapping_loop_design.md`](adaptive_mapping_loop_design.md)
open question 2 ("Subpopulation splitting: when does the agent judge
that evidence warrants creating sub-nodes vs. flagging heterogeneity in
caveats?") — the OLM-driven case study. This proposal does not resolve
that question; it provides the atlas-side metrics that the splitting
rule will need to consume. Joint handling (atlas-side heterogeneity +
classical-side lit evidence of subtypes converging on a splitting
recommendation) is explicitly out of scope here — see §6.

---

### 3.8 Interim consequences for Stage B confidence (Phase 1 only)

*This subsection is Phase-1-scoped. Stage B confidence assignment
stays where it is in Phase 1; Phase 3 moves it to report time.*

The Stage B mapping subagent's confidence rubric is currently qualitative
and evidence-type-driven, not numeric. The proposed Stage A changes
affect Stage B in three ways:

### 3.9 More candidates reach Stage B

With no curator gate, every above-cutoff candidate gets a `MappingEdge`.
Most edges will be LOW or UNCERTAIN. The report is where these get
filtered for human attention.

### 3.10 Richer property_comparisons inputs

After universal enrichment (§3.2), every defining marker / neuropeptide /
negative marker on the classical node has quantitative data on every
candidate. Consequences:

- The `NOT_ASSESSED` alignment value becomes rare (only when a gene is
  genuinely missing from the HDF5).
- Defining markers absent from the candidate (`val < MIN_DETECTABLE`)
  should produce `DISCORDANT`, not `NOT_ASSESSED` — currently no rule
  covers this. The mapping-subagent prompt
  (`workflows/map-cell-type.md` Step 3) needs updating.
- Presence-only matches (sibling-non-discriminating) should produce
  `APPROXIMATE` rather than `CONSISTENT` — the gene is on but doesn't
  distinguish the candidate from siblings.

### 3.11 AT evidence is more uniformly present

If AT artifacts are persisted at threshold (§3.3), the mapping subagent
will more often see an `AnnotationTransferEvidence` entry on candidates
beyond the originally-motivating one. This makes HIGH confidence reachable
for more edges (the rubric requires ≥1 experimental evidence type).
Whether the rubric needs to change to handle the broader availability of
AT — e.g. require a higher F1 threshold for HIGH — is open.

### 3.12 What does NOT change in Phase 1

The confidence rubric itself (HIGH / MODERATE / LOW / UNCERTAIN, evidence
counting, experimental-evidence requirement) is unchanged by this
proposal. Stage A score is still not consumed by Stage B; the link
remains set-membership.

---

## 4. Phase 2 — Mapping schema overhaul

*Tracks [issue #30](https://github.com/Cellular-Semantics/evidencell/issues/30).
Heavy schema + KB-wide YAML rewrite; ships once #30 discussion has
converged. Phases 3 and 4 depend on the field set this phase
introduces.*

This phase is summarised here for roadmap context; full content lives
in issue #30 and should not be duplicated. Read #30 for the working
proposal text and discussion.

### 4.1 What this phase delivers (summary of #30)

1. **SSSOM-aligned predicates.** Three-tier equivalence
   (`EQUIVALENT` ≈ skos:exactMatch; `CLOSE` ≈ skos:closeMatch, *new*;
   `PARTIAL_OVERLAP` for genuinely incomplete) plus
   `BROADER` / `NARROWER` aligned to skos:broadMatch / skos:narrowMatch.
   Drop `TYPE_A_SPLITS` / `TYPE_A_MERGES`.
2. **Predicate / cardinality split.** New `mapping_cardinality` enum
   (`1:1`, `1:n`, `n:1`); splits/merges are expressed as
   `BROADER + 1:n` or `NARROWER + n:1`.
3. **Field renames.** `type_a` → `lit_type`, `type_b` → `taxonomy_type`
   throughout schema, code, KB YAML, and docs.
4. **`mapping_justification`** (semapv subset:
   `ManualMappingCuration`, `UnreviewedManualMapping`,
   `LexicalMatching`, `CompositeMatching`, `LogicalReasoning`,
   `UnspecifiedMatching`).
5. **Reviewer fields.** `reconciliation_note` (curator synthesis when
   parallel evidence sources disagree) + `reviewed_by` (human
   reviewer, distinct from `curator`).
6. **`confidence_score`** optional numeric field (0–1, SSSOM-compatible)
   alongside the ordinal `confidence`.
7. **Drop `CANDIDATE_SYNONYM`.**
8. **Self-disambiguating schema descriptions** for SKOS directional
   predicates (`BROADER` / `NARROWER`) — TOC glossary preamble
   explaining the directional rule, schema enum descriptions with
   worked examples and cardinality interaction notes.
9. **`src/evidencell/sssom_export.py`** — TSV emission for
   interoperability.

### 4.2 Why this phase has to land before Phase 3

Phase 3 (verdict at report time) adds further fields to `MappingEdge`
(`rationale`, `report_path`, `rationale_generated_at`,
`rationale_source_hash`) and changes who writes `confidence` /
`confidence_score`. Doing those additions before the Phase 2 rename
would mean migrating KB YAML twice. Order: #30 → Phase 3.

### 4.3 Why this phase has to land before Phase 4

Phase 4 (joint heterogeneity → splitting) needs `BROADER` +
`mapping_cardinality: 1:n` to express "OLM splits into Sst-OLM +
Htr3a-OLM, each mapping to a different sub-cluster of Sst Gaba_3."
Without the predicate/cardinality split, the splitting workflow has
nowhere clean to write the resulting edges.

### 4.4 What this phase does *not* address

- Does not move confidence assignment to report time — that's Phase 3.
- Does not add `rationale` or `report_path` — Phase 3.
- Does not resolve splitting decision rules — Phase 4.
- Does not change Stage A scoring — Phase 1.

---

## 5. Phase 3 — Verdict at report time

*Depends on Phase 2 schema migration. Materially changes Stage B's
output spec; coordinates with the new Phase-2 fields
(`reconciliation_note`, `confidence_score`).*

> **⚠ Status — needs further design work before scoping.**
>
> The Phase-3 sketch below covers field additions, currency
> mechanism, and the migration story, but the operational details of
> how Stage B and report generation should divide labour are not yet
> settled. Specifically:
>
> - What exactly does a Phase-3 Stage B emit? Pure structured data
>   (no `confidence`, no caveats), or does it still produce a
>   provisional verdict to be superseded? § 5.3 sketches the former
>   but the trade-offs aren't fully worked through.
> - What does the report-generation step need to do that it doesn't
>   already? The rationale write-back and currency hash are new, but
>   the underlying synthesis logic largely already exists in
>   `gen-report`. Need a precise inventory of new vs. existing work.
> - How does this interact with the §3.3 "in region + distant"
>   note — does the report-time verdict cite region fraction
>   directly, or does Phase-2's predicate selection capture it?
>
> Treat §§ 5.1–5.5 as the working sketch, not a scoping spec. A
> dedicated Phase-3 design pass should happen before this phase is
> filed as an issue.

### 5.1 Motivation

Under §4, the holistic verdict on a mapping (cross-modal triangulation,
literature synthesis, judgement over the full evidence picture) doesn't
have a clean home. Stage B is being asked to compress it into a
`confidence` enum with reasoning scattered across per-property `notes`
and per-evidence `explanation` fields; the report stage then redoes the
same synthesis from the structured residue plus literature quotes.
Two layers of LLM reasoning over largely the same inputs.

But pushing the synthesis entirely to report time leaves the graph YAML
without a headline rationale, which breaks downstream consumers that
predate this project (spreadsheet review of taxonomy annotations, the
Cell Annotation Platform, anyone scanning a graph file). A `rationale`
field is established practice in those workflows.

### 5.2 Proposal

The report generation step writes back a short rationale to the
`MappingEdge` it just synthesised, alongside currency metadata.

**New `MappingEdge` fields, set at report time:**

| Field | Type | Source |
|---|---|---|
| `rationale` | string (short prose) | Report-gen LLM, distilled from the report it just produced |
| `confidence` | enum (HIGH / MODERATE / LOW / UNCERTAIN) | Moved from Stage B → report time; same rubric, applied with full literature in scope |
| `report_path` | string | Relative path / URL to the full report |
| `rationale_generated_at` | datetime | Timestamp |
| `rationale_source_hash` | string | Hash over the gen-facts output that fed this report |

**Currency mechanism.** On every read or `just qc` pass, recompute the
gen-facts hash from current node + edge state and compare against
`rationale_source_hash`. Mismatch → mark stale. Stale rationales are
still shown but flagged (`(rationale stale — regenerate report)` in
renderings; similar warning surfaced in spreadsheet/CAP exports).
The hash beats a plain timestamp because YAML files get touched for
unrelated edits constantly; we want to detect *meaningful* drift only.

### 5.3 What Stage B looks like under this extension

Stage B becomes pure structured data work:

- `relationship` enum — still genuine typology (EQUIVALENT /
  PARTIAL_OVERLAP / CROSS_CUTTING / SUBSET / TYPE_A_SPLITS / UNCERTAIN);
  retained as an edge-level field.
- `property_comparisons[*]` — verbatim values, alignment enum, per-
  property notes for APPROXIMATE / DISCORDANT cases.
- `evidence_items[*]` — typed, provenance-bearing.
- `caveats[]`, `unresolved_questions[]`, `proposed_experiments[]` —
  retained for now (could later move to report-time too if synthesis
  rather than data).

**`confidence` is no longer a Stage B output.** Edges that have not yet
been through report generation carry no headline verdict — honest
state, not a regression. Spreadsheet exports of pre-report edges can
fall back to a templated summary derived from alignment enums
(e.g. "5/7 markers CONSISTENT, 1 DISCORDANT, location CONSISTENT").

### 5.4 What this could break / things to watch

This section names knock-ons, not blockers — but they need attention if
we adopt.

- **Schema change.** `MappingEdge` gains five fields and loses Stage B
  authority over `confidence`. Schema PR with explicit rationale per
  `CLAUDE_dev.md` § Schema changes.
- **Existing edges in `kb/graphs/`.** All currently
  carry a Stage-B-assigned `confidence`. Migration choice: leave them
  as-is and treat the existing value as the rationale-time verdict
  (with `rationale_source_hash` null = "untracked legacy"), or
  invalidate and require report re-runs to populate the new fields.
  Leave-as-is is safer; the staleness check naturally tags them as
  needing regeneration on next QC.
- **Stage B prompt and orchestrator.** Step 3 prompt
  ([map-cell-type.md:316-426](../workflows/map-cell-type.md#L316-L426))
  needs the confidence-determination instruction removed; the
  decision-guide block becomes report-time material. Step 4 gate text
  ("Confidence: {CONFIDENCE} — {rationale summary}") needs rewording.
- **Report orchestrator.** `gen-report` needs a write-back step:
  produce report + extract short rationale + compute hash + edit the
  MappingEdge YAML. The pre-edit hook must accept these writes.
- **Pre-edit hook.** Validation rules around `confidence` need to allow
  null / unset (for pre-report edges) where they may currently require
  it.
- **Consumers reading `confidence`.** Any code or view that assumes
  every edge has a `confidence` value needs to handle the unset case.
  Likely audit targets: report renderers, TOC generation, any
  spreadsheet/CAP export.
- **Stage A → Stage B integration.** Independent of this section's
  changes — but if §1–4 ship first with Stage B still owning
  confidence, that's fine; this extension lands separately and
  inverts that ownership cleanly.
- **What rationale is allowed to claim.** The rationale lives in YAML
  but is generated from a report. Anti-hallucination guarantees on
  the report (quote_key validation, ID/PMID checks) don't transitively
  apply to a distilled prose summary. Either re-run validation on the
  rationale text, or keep the rationale strictly to claims already
  validated in the structured fields ("MODERATE confidence; 5 of 7
  markers CONSISTENT, AT F1 = 0.62").

### 5.5 Why this fits the broader direction

- Reports already are the review gate (KB curation principle); putting
  the verdict at report time aligns *where the verdict is written*
  with *where it gets reviewed*.
- Compounds with the §1–4 gating drop: Stage A→B becomes a cutoff
  filter, Stage B becomes mechanical structured-data extraction,
  Stage C (report) is where holistic judgement and rationale
  consolidate. Three stages, three distinct jobs, no redundant
  reasoning.
- Preserves the human-readable surface that spreadsheet / CAP
  workflows depend on, with a currency-tagging mechanism that lets
  consumers know when a verdict is stale.

---

## 6. Phase 4 — Joint heterogeneity → splitting

*Depends on Phases 1 and 2. Coordinates with
[`adaptive_mapping_loop_design.md`](adaptive_mapping_loop_design.md)
open question 2. OLM is the canonical worked example.*

This phase is summarised here for roadmap context; the splitting
decision rule belongs in the adaptive-mapping-loop workstream, not in
this redesign. Read `adaptive_mapping_loop_design.md` § "OLM-specific
observations" and § Open questions item 2 for the originating
discussion.

### 6.1 What this phase delivers

1. **Joint heterogeneity surfacing.** When atlas-side coverage
   (Phase 1, § 3.7) and classical-side lit evidence of subtypes
   (already captured on the classical node, e.g. Winterer 2019 splits
   OLM into Sst-OLM + Htr3a-OLM) both fire on the same mapping, the
   report flags this as a candidate for classical-node splitting.
2. **Splitting decision rule.** Threshold on convergence:
   - Atlas-side: marker coverage at the supertype < some threshold
     (e.g. < 50%) for the classical type's defining markers.
   - Classical-side: lit evidence of ≥ 2 distinct subtypes with
     differential expression / morphology / electrophysiology.
   - AT-side (when available): F1 distribution across child clusters
     showing scatter consistent with subtype heterogeneity.
   Specific thresholds TBD — see `adaptive_mapping_loop_design.md`
   OQ 2.
3. **KB write-back.** When the curator approves a splitting
   recommendation, the workflow:
   - Creates new sub-nodes on the classical side (e.g. `lit_OLM_Sst`,
     `lit_OLM_Htr3a`).
   - Migrates evidence items from the parent node to the appropriate
     sub-node where source evidence is subtype-specific.
   - Writes new MappingEdges using Phase-2 `BROADER` +
     `mapping_cardinality: 1:n` predicates targeting the appropriate
     child clusters.
   - Optionally retains the parent classical node with edges marking
     it as the union (subject to the splitting decision rule).

### 6.2 What this phase does *not* address

- Does not change Stage A scoring — that's Phase 1.
- Does not change the schema — that's Phase 2.
- Does not resolve metadata-vs-precomputed disagreement (§ 7).
- Heterogeneity within rank-0 clusters (would need cell-level data,
  out of scope across all phases).

### 6.3 Cross-references

- [`adaptive_mapping_loop_design.md`](adaptive_mapping_loop_design.md)
  § "OLM-specific observations", § Open questions item 2.
- Memory: `project_olm_annotation_transfer.md`.
- Issue #30 § cardinality: provides the `BROADER + 1:n` predicate.

---

## 7. Open questions

**Metadata vs precomputed disagreement.** When a gene is flagged in the
taxonomy metadata marker columns but `precomputed_expression` shows it
absent (or vice versa), default behaviour: record both, flag as a
discrepancy in `property_comparisons` and surface in the report. Whether
scoring should use one, the other, or neither when they conflict is
undecided. Plausible cases drove this — bimodal expression (high in a
subset, low mean) is a real biological pattern where metadata may
legitimately flag a marker the cluster mean understates. Detection rate
(fraction of cells with non-zero counts) from the precomputed stats HDF5,
if accessible, would resolve many of these cases as a third evidence
stream.

**AT scoring weight at Stage A.** Specific bucket boundaries and points
TBD. Resolved: AT is additive with marker scores (not dominant), and
candidates with AT above the persistence floor bypass region/NT hard
filters (§3.3). The bypass means an AT-matched candidate in the "wrong"
region still enters the pool; whether the resulting edge stands or gets
refuted is a Stage B / report concern.

**AT artifact freshness.** If AT artifacts are read at find-candidates
time, the taxonomy-DB freshness check needs to either incorporate them or
the artifacts need their own staleness check.

**Cutoff: K value.** Resolved: top-K only, no absolute threshold (§3.5).
Default likely conservative (~5), possibly rank-dependent. Open: exact
default and whether it should be configurable per find-candidates run.

**LLM adjacency calls in Stage A.** Region filter falls back to LLM
latent knowledge when the candidate has zero cells in the queried
region. Open questions: how to surface the verdicts (cache against
(region, candidate region set) tuples?), where in the find-candidates
pipeline the call lives, what model to use, what to do on LLM-call
failure (default permissive — pass — to avoid silently dropping
candidates).

**Anatomical-region propagation at higher ranks.** Resolved (Phase 1
implementation): on inspection, every rank in WMBv1 source taxonomy
YAML already carries `anatomical_location` entries
(class 31/34, subclass 326/338, supertype 1180/1201, plus all clusters),
and `_insert_node` populates the `anat` SQLite table uniformly across
ranks. `_get_anat` therefore returns rows at every rank without
requiring programmatic propagation. If a future taxonomy ingest produces
sparse parent-rank anat coverage, build-time aggregation from
descendants is the natural fallback.

**Defining vs neuropeptide weighting.** Should neuropeptides count
identically to defining markers in positive-marker scoring, or be
weighted lower? Argument for equal: they're equally diagnostic for many
classical types. Argument for lower: defining markers are the curated
discriminators, neuropeptides are more often co-expressed across
related types.

**Confidence rubric and AT.** Does broader AT availability need stricter
F1 thresholds in the HIGH-confidence rule?

**Property-comparison alignment rules.** Update Step 3 prompt for
`val < MIN_DETECTABLE` → `DISCORDANT`, presence-only → `APPROXIMATE`,
and low-coverage at rank ≥ 1 → `APPROXIMATE` with coverage cited
(§3.7).

**Heterogeneity metric choice.** Detection coverage is the
proposed primary metric (§3.7). Whether to also emit CV or
max/mean ratio for downstream interpretation, or whether
coverage alone is sufficient, is open. Probably defer until we
see what Stage B / report rationale ends up wanting to say.

**Joint heterogeneity → splitting workflow.** When atlas-side
heterogeneity (this proposal §3.7) and classical-side
heterogeneity (lit evidence of subtypes, per
[`adaptive_mapping_loop_design.md`](adaptive_mapping_loop_design.md)
OQ 2) both fire on the same mapping, how should the system surface
this as a candidate for classical-node splitting? Out of scope for
this PR — the marker-scoring redesign produces the atlas-side
inputs; the splitting decision rule and any KB write-back is a
separate workstream. OLM is the canonical worked example
(adaptive-loop doc §"OLM-specific observations").

---

## 8. Why the full roadmap is better than the current design

**From Phase 1:**

- Eliminates per-mapping enrichment as a manual orchestrator step.
- Percentile references become unbiased.
- Neuropeptides become first-class at Stage A.
- Defining-marker presence/absence enters scoring symmetrically with
  negative markers.
- Negative markers gain a metadata fallback (gap 4).
- AT evidence becomes a deterministic Stage A signal, not a textual
  refinement-subagent lookup.
- `_expression_detail` becomes visible to downstream consumers.
- Curator labour shifts from per-shortlist gating to report review,
  consistent with the project's broader direction ("reports are the
  review gate").
- Heterogeneity-aware scoring at non-leaf ranks; right level wins on
  score without adaptive descent.
- Hard region/NT prerequisites stop letting unrelated candidates
  compete on marker overlap alone.

**From Phase 2 (#30):**

- Mapping relationships align with SSSOM/SKOS — interoperable export,
  unambiguous predicate semantics, predicate/cardinality split removes
  jargon (`TYPE_A_SPLITS` etc.).
- Three-tier equivalence (`EQUIVALENT` / `CLOSE` / `PARTIAL_OVERLAP`)
  fixes the over-strict-equivalence problem.
- Curator-side reviewer fields (`reconciliation_note`, `reviewed_by`)
  give human synthesis a clean home.
- Numeric `confidence_score` removes ordinal binning ambiguity for
  SSSOM export.

**From Phase 3:**

- Holistic verdict synthesis happens once, at report time, with
  literature in scope — not redundantly recomputed.
- Stage B becomes mechanical (cheap, fast, no subagent budget
  pressure); LLM reasoning consolidates at report stage.
- Currency-tagged rationale + report link preserves graph legibility
  for spreadsheet / CAP workflows.

**From Phase 4:**

- Joint heterogeneity surfacing turns OLM-style ambiguity (atlas-side
  scatter + lit-side subtype evidence) into an explicit splitting
  recommendation, rather than a curator-noticed caveat.
- Phase-2 `BROADER + 1:n` predicates give splits a clean schema home.

---

## 9. Files this would touch

### Phase 1 — Marker scoring core

- `src/evidencell/taxonomy_db.py` — `find_candidates` signature, scoring
  logic, percentile references, AT artifact reading, JSON output
  including `_expression_detail`, negative-marker metadata fallback,
  hard prerequisite filters with LLM adjacency fallback, heterogeneity
  coverage at rank ≥ 1.
- `src/evidencell/taxonomy_ops.py` — proactive batch enrichment driver
  (gene-union over all KB classical nodes).
- `workflows/map-cell-type.md` — drop Stage A gate, restructure Step 0b,
  remove Step 2b, add AT artifact handling, update Step 3 prompt for
  new alignment rules.
- `justfile` — new recipe(s) for KB-wide marker-union enrichment;
  possibly a recipe for AT artifact ingestion.
- Tests — new percentile cases (presence/absence), AT scoring,
  unbiased reference verification, negative-marker metadata fallback,
  coverage scoring, hard-filter behaviour.

### Phase 2 — Mapping schema overhaul ([#30](https://github.com/Cellular-Semantics/evidencell/issues/30))

- `schema/celltype_mapping.yaml` — predicate enum restructure, field
  renames, `mapping_cardinality`, `mapping_justification`,
  `reconciliation_note`, `reviewed_by`, `confidence_score`,
  self-disambiguating descriptions.
- `kb/graphs/**` — every `edges:` block: rename
  fields (`type_a` → `lit_type`, `type_b` → `taxonomy_type`), remap
  relationship values, add `mapping_cardinality` where derivable from
  existing splits/merges.
- `src/evidencell/toc.py`, `validate.py`, `render.py`, `taxonomy_db.py`,
  `taxonomy_ops.py` — ~20 call sites for field renames and enum
  remapping.
- `src/evidencell/sssom_export.py` — *new*; TSV export.
- `.claude/hooks/` — pre-edit hook updates for new field set.
- Tests — schema round-trip, SSSOM export round-trip.
- Docs — `CLAUDE.md`, workflow docs, glossary preamble.

### Phase 3 — Verdict at report time

- `schema/celltype_mapping.yaml` — add `rationale`, `report_path`,
  `rationale_generated_at`, `rationale_source_hash`. Move `confidence`
  / `confidence_score` writes from Stage B → report time (no schema
  change here, but provenance shifts).
- `workflows/gen-report.md` — write-back step: produce report, distil
  rationale, compute hash, edit MappingEdge YAML.
- `workflows/map-cell-type.md` Step 3 prompt — remove
  confidence-determination instruction; Stage B emits structured data
  only.
- `.claude/hooks/` — accept rationale/hash writes; staleness check on
  read / `just qc`.
- `src/evidencell/render.py` — render `(rationale stale)` flag when
  hash mismatches; spreadsheet/CAP exports surface the same.
- Tests — hash currency, write-back idempotency, legacy edge migration
  (`rationale_source_hash: null` accepted).

### Phase 4 — Joint heterogeneity → splitting

- `workflows/adaptive-mapping-loop.md` (or wherever the splitting
  workflow lands) — splitting decision rule using Phase-1 coverage
  metrics + classical-side lit evidence.
- `workflows/gen-report.md` — surface joint-heterogeneity flags as
  splitting candidates in reports.
- KB write-back tooling — sub-node creation, evidence migration to
  sub-nodes, edge rewriting using Phase-2 `BROADER + 1:n` predicates.
- Tests — splitting rule unit tests, integration test on OLM example.
- Docs — splitting decision rule documented in `CLAUDE.md` and the
  splitting workflow.
