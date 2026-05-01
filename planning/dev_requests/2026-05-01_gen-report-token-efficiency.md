# Dev request: gen-report token efficiency review

**Date:** 2026-05-01
**Status:** Discussion / planning — no implementation yet
**Trigger:** Pending regen pass for moderate-to-high confidence nodes; previous
parallel subagent runs burned tokens faster than expected.

---

## Context

`workflows/gen-report.md` was recently overhauled to produce paper-style
reports (Header → Introduction → Results → Methods → Discussion → References).
The overhaul was deliberately more agentic — the synthesis subagent now owns
substantially more structural responsibility (long Methods subsections,
Evidence support tables, per-candidate paragraphs with bespoke
property-by-property interpretation). Token cost rose accordingly. This
document audits where cost is being spent and what is worth changing **before**
a moderate-to-high regen pass.

This is not a critique of the paper-style design. The Results / Discussion
prose and per-candidate interpretation genuinely need an LLM. The question is
whether everything *currently* routed through an LLM also needs one.

---

## Cost shape — per node, today

| Stage | Mechanism | Input | Output | Notes |
|---|---|---|---|---|
| `gen-facts` | Python | YAML | `{node}_facts.json` | Free; deterministic. |
| Synthesis subagent | LLM (Sonnet default) | facts.json (50–200 KB) + ~700-line workflow prompt | 10–30 KB Markdown | Owns *both* mechanical templating (Header, Classical-type table, Methods tables, References, reproducibility footer, Evidence-base audit) and interpretive prose (Introduction framing, per-candidate Supporting/Concerns/What-would-upgrade, Best-candidate). |
| Validation subagent | LLM (Sonnet default) | facts.json + generated report + ~150-line prompt | Short verdict | Pure enumeration/lookup — does each `[n]`, accession, blockquote resolve. |
| Drill-down scaffold (per PMID) | Python | references.json + edge YAML | scaffold Markdown | Free. |
| Drill-down synthesis (per PMID) | LLM (Sonnet) | scaffold + facts.json + drill-down prompt | enriched Markdown | Low-creativity templating around verbatim quotes. |
| Drill-down validation (per PMID) | LLM (Sonnet) | scaffold + facts + report | verdict | Same enumeration work as summary validation. |

**Dominant multiplier:** drill-down mode, where N papers × M nodes × 2 subagents
fans out fast (a region with 6 nodes and 15 papers per node is ~180 subagent
spawns). Each spawn re-loads the same facts.json and a near-identical workflow
prompt — that redundant context is a large fraction of the bill.

**Secondary multiplier:** the synthesis subagent renders deterministic tables
(Methods, References, Evidence base) that don't need a model at all, but doing
so requires it to consume the entire workflow prompt and produce long output.
Programmatic templating of these would shrink both the prompt the LLM sees and
the tokens it has to emit.

---

## Levers, ranked by saving ÷ risk

## Note on drill-downs

Drill-downs are opt-in via the orchestrator's `mode` parameter
(`summary | drilldowns | all`, default `summary`). They are **out of scope for
the upcoming moderate-confidence regen** unless explicitly invoked. Drill-down
specific levers (caching, model downgrade) are deferred to the larger review
section and should not be acted on for this regen campaign.

---

## Quick fixes (this regen pass)

Each lever below is small, low-risk, and independently shippable. Land them
together and re-measure.

### QF1. Node-selection filter on confidence

Filter classical nodes upstream of the per-node loop: include a node iff at
least one of its edges has confidence ∈ {HIGH, MODERATE}. Apply when the
orchestrator expands `node_id: null` (or a region-scoped request) into the
working set.

Note this is *not* "skip nodes whose best edge is UNCERTAIN" — a node with
one MODERATE survivor and several eliminated UNCERTAIN candidates is exactly
where the report's eliminated-candidate logic adds value. The filter only
excludes nodes where *every* edge is UNCERTAIN/LOW, since those have no
positive signal worth synthesising.

Skipped nodes appear as a one-line index entry
("skipped: no MODERATE/HIGH candidates").

**Effort:** trivial. **Saving:** depends on region — typically 30–50% of
classical nodes in a region.

### QF2. Replace LLM validation subagent with a Python `validate-report` step

The validation subagent does enumeration work — extract every `[n]` and
accession, confirm it resolves in `facts.reference_index` or `facts.edges`,
verify blockquote bodies match `facts.quotes[key].text` verbatim. All
deterministic. Replace the subagent with a Python checker covering the four
checks the pre-write hook can't do (the hook already covers blockquote
attribution form, `quote_key` resolution, and PMID resolution against
`references.json` — the validator runs on writes the hook accepted).

**Failure handling — three classes, with retry-once correction loop:**

| Class | Example | Response |
|---|---|---|
| Hallucinated identifier | `[3]` cited in body, not in `facts.reference_index`; or accession `CS20230722_CLUS_9999` not in `facts.edges` | Re-run synthesis once with the failure list appended as a targeted correction prompt ("remove or replace [3]; not in references"). Stop and ask curator if still failing. |
| Verbatim mismatch on blockquote body | Synthesis paraphrased a quote whose `quote_key` is valid (so the hook passed) but body text doesn't match `facts.quotes[key].text` | Same retry-once correction loop, with the diff in the prompt. Usually fixed in one retry. |
| Missing interpretation marker | Sentence makes a neuroanatomical claim without `*(note: ...)*` | Advisory, not blocking — flag inline with a comment for curator review. The fuzzy check shouldn't gate acceptance because false positives are likely. |

Same correction-loop shape as the current LLM-validator pipeline; the input
to the correction prompt is now a deterministic failure list with line
numbers and expected-vs-found, rather than an LLM-summarised verdict.

**Effort:** small — the checks are set membership and substring matching
against the facts file. **Saving:** eliminates one subagent per node, so
roughly half the per-node LLM cost.

### QF3. No extended thinking on synthesis

`gen-report` synthesis prompts are extremely prescriptive — little ambiguity
for thinking budget to chew on. Default thinking budget mostly retraces the
spec. Disable on synthesis. Re-enable selectively if a specific synthesis
section turns out to need it (e.g. complex multi-edge Discussion).

**Effort:** trivial. **Saving:** small but free.

### QF4. Parallel-by-default for batch, sequential for single-node

Parallel spawn helps wall-clock, not tokens. The right default is mode-
dependent:

- **Multi-node batch run** (e.g. "regen all moderate-confidence nodes for
  this region") — parallel by default. Wall-clock matters; without it a
  region pass can be very slow.
- **Single-node run** (`node_id` specified, interactive iteration) —
  sequential is fine; the loop is length-1 anyway, and the curator wants
  to inspect the result before kicking off more.

Expose a `parallel: true|false` flag with the default keyed on whether a
single `node_id` was specified.

**Effort:** trivial — orchestrator already sequences per node; this just
makes the loop's mode explicit.

---

## Larger review (post-regen, separate effort)

Defer until quick-fix savings are measured. Both items below are bigger
structural changes whose value should be evaluated against a clean
post-quick-fix baseline.

### LR1. Jinja-style slot architecture

Today the synthesis prompt embeds the entire paper-style report structure
as natural-language instructions; the LLM has to *interpret a spec and emit
structure* when the structure is fixed and only certain slots are creative.
A Jinja template makes the contract explicit:

- **Deterministic slots — filled in Python from `facts.json`, no LLM:**
  Header, draft warning banner, Location note (conditional), Classical type
  table, Methods section (all tables: AT runs, bulk correlation runs, atlas
  data sources, Evidence base audit, anti-hallucination boilerplate,
  reproducibility footer), References table.
- **Authored-prose slots — small targeted LLM calls, each with only the
  slot's local context:** Introduction framing paragraph, Cell Ontology
  mapping interpretation line, Results opening sentence, per-candidate
  paragraphs (Supporting evidence, Concerns, What would upgrade, Marker
  evidence provenance), Best candidate + caveats summary, Proposed
  experiments synthesis, Open questions list.

Each authored-prose call sees only the data its slot needs (e.g. one edge
plus its property comparisons), not the full facts.json. The model never
sees or rewrites the structural skeleton.

This subsumes a previously-considered "summary scaffold" idea — the
scaffold becomes the rendered template with empty slots, and the LLM fills
slots rather than writing a delta on top of a partial document.

**Considerations to flag now:**
- Real refactor: `evidencell.render` currently produces `facts.json`, not
  Markdown templates. A Jinja layer is a new responsibility for the renderer
  (or a new sibling module).
- Slot prompts proliferate — needs a small library of slot-filler prompts
  rather than one monolithic orchestrator prompt. Easier to maintain
  (each slot's contract is local), but more files.
- Parallel becomes more attractive *within* a single node: per-candidate
  slots can be filled concurrently with small prompts each, recovering any
  wall-clock loss from QF4's sequential single-node default.
- Open: how much of the deterministic-table logic already exists in
  `evidencell.render` to extend vs. how much is currently happening
  implicitly inside the synthesis LLM. Affects effort estimate.

### LR2. Drill-down conditional improvements (only when drill-down regen is in scope)

Two levers, both deferred until drill-down mode is reactivated for a
campaign:

- **Caching by content hash.** Drill-downs are stable per-paper: a drill-
  down only changes when its source quotes (`references.json`) or its
  supporting edge changes. Cache key:
  `hash(corpus_id, edge_node_b_accession, edge_confidence, references.json[corpus_id].text)`.
  Skip regen if cached drill-down has matching key. Manifest at
  `drilldown_manifest.json` per region.
- **Drill-down synthesis → Haiku.** Low-creativity templating around
  verbatim quotes pre-extracted in the scaffold. Pilot on 2–3
  representative drill-downs first — APPROXIMATE/DISCORDANT alignment
  interpretation does benefit from a capable model.

Both should be revisited if and when a campaign requires drill-down regen.

---

## Recommended starting point

Land QF1–QF4 together, then run a moderate-confidence regen on one region
to establish a clean baseline. Decide on LR1 (Jinja split) based on
measured residual cost. Don't touch LR2 until drill-downs are explicitly
in scope.

---

## Open questions

- Should QF1 be the default behaviour with `--include-uncertain` to opt back
  in, or a flag (`confidence_min: MODERATE`) that has to be set explicitly?
- For LR1 effort estimate: how much of the deterministic-table logic
  already exists in `evidencell.render` to extend? (Material to whether
  LR1 is a moderate or large refactor.)
