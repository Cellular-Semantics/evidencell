# Workflow Architecture: Survey vs Targeted Search

**Date**: 2026-04-21
**Status**: Design discussion — informing workflow refactor
**Context**: Emerged from a broad review of the lit-review → cite-traverse → evidence-extraction
pipeline. The core insight is that the pipeline conflates two fundamentally different modes
of operation. Getting this distinction right is the key to avoiding procedural hairballs.

> **Naming note**: "Discovery" was considered for the first path but is too vague.
> Current working name: **Survey** (bounded by ASTA paper set) vs **Targeted**.
> Better names welcome.

---

## The core insight: two axes

### Axis 1 — Survey vs Targeted

| | Survey | Targeted |
|---|---|---|
| **When** | First encounter; KB sparse after ASTA ingest | KB has content; gap review reveals specific missing fields |
| **Question** | What do we know about this cell type from the ASTA corpus? | Find Chrna2 expression data for OLM in stratum oriens |
| **Scope** | Bounded by ASTA paper set (may expand in future) | Narrower; fanning out is a bug |
| **Sources** | ASTA snippets across all corpus papers; PMC full text for gaps | Targeted snippet query + optional citation follow + full text |
| **Output shape** | Unknown in advance; serendipity has value | Known (specific PropertySource field) |
| **Synthesis** | After mining — cross-paper signal matters | At mining time — per-paper agent writes KB directly |
| **Citation following** | Not the primary mode; corpus already defines scope | Yes, bounded — 1–2 hops for a specific question |

### Axis 2 — Synthesis placement

| | Per-paper agents | Post-hoc |
|---|---|---|
| **When** | Targeted mode | Survey mode |
| **What** | Agent reads one paper, writes KB entry | Cache summaries, single synthesis subagent over all |
| **Benefit** | Fast; synthesis baked in | Flexible — re-synthesise from same cache |
| **Cost** | Loses cross-paper signal | Large cache; synthesis deferred |

---

## Pipeline structure

```
[ASTA report (PDF)]
        │
        ▼
asta-report-ingest ──────────────────────────────► KB (properties + stub edges)
  [+ synonym extraction]                            │
                                                    ▼
                                            KB gap review
                                         (what's missing?)
                                            [fluid — runs
                                            as first step of
                                            any research cycle]
                                                    │
                         ┌──────────────────────────┴───────────────────────┐
                         ▼                                                  ▼
                  SURVEY path                                      TARGETED path
         (cell type poorly characterised;                     (specific KB field gap;
          KB sparse after ASTA ingest)                         KB has partial content)
                         │                                                  │
              ASTA snippet_search across                       targeted snippet query
              all corpus paper IDs (batch)                     + synonym expansion
                         │                                                  │
              PMC full text for gap papers               optionally: cite-traverse skill
              (enrich where snippets thin)                (1–2 hops, bounded question)
                         │                                                  │
              all_summaries.json                           per-query synthesis agent
              (per-snippet summaries,                      → KB write (PropertySource)
               section, quotes, relevance)                 → pre-edit hook validates
                         │
              synthesis subagent
              (cross-paper; themes;
               gap + new types analysis)
                         │
                  KB + report.md
```

---

## How all_summaries.json is produced

This is the central cache for the survey path and deserves explicit description.
The current cite-traverse fetch subagent produces it as follows:

1. **ASTA snippet_search** across all corpus paper IDs (can be batched — a single
   call handles multiple papers). Returns short snippets with section metadata.

2. **Filter** — title-kind snippets and peer-review sections excluded.

3. **Per-snippet summary** — for each retained snippet: section, relevance score,
   1–3 verbatim quotes, node relevance judgement.

4. **PMC full-text fallback** — for papers that returned 0 snippets ("gap papers"):
   fetch EuropePMC full text, extract up to 3 relevant passages. This is currently
   a fallback only, not used to enrich all papers.

5. **Merge** — depth_N_summaries from each traversal depth → all_summaries.json.

**Planned improvement (refactor aim):** Use full text more broadly — not just as
a fallback for zero-snippet papers, but to enrich thin-snippet papers (e.g. 1 snippet
from a high-relevance paper) and to extract synonyms and dataset accessions that
snippets miss. The mechanism for this is not yet specified: options include
a per-paper enrichment pass triggered by relevance score, or a post-scan full-text
fetch for papers flagged as high-priority by the synthesis subagent.

**What we must NOT lose in refactoring**: the multi-paper batch capability of
ASTA snippet_search. A single call can cover the full ASTA corpus — this is the
efficiency gain of the survey path. Refactoring to cite-traverse-as-skill for
targeted questions should not reduce this capability; it should coexist with it.

---

## Critical early step: synonym capture

**This is potentially the most important infrastructure to get right early.**

Papers, atlases, and databases use different names for the same cell type. Without
synonym mapping, both survey and targeted searches fail silently — queries miss the
cell type because the wrong term is used.

Examples:
- OLM = oriens-lacunosum moleculare = O-LM cell = OLM interneuron
- "Sst+" in atlas cluster labels vs "somatostatin-expressing" in papers
- Historical names vs current names
- Short abbreviations used in atlas annotation vs full classical names in papers

**Synonym bootstrapping mechanism:**
Look for synonyms on each paper as a first step when processing it. Use what is
found in subsequent queries — feed forward within the same mining run. Snippet
search alone may be insufficient for this (snippets may not include the passage
where the author defines their abbreviation); PMC full-text fetch is probably
required for reliable synonym extraction.

Also take advantage of existing KB content: if a node already has synonyms from
a prior run, inject them into all subsequent queries for that node.

**Split-first principle for extraction agents:**
The KB is built while being queried — extraction agents cannot always determine whether
two names refer to the same type or subtly distinct types. Collapsing two names into one
node is lossy and hard to reverse; keeping them separate and linking is not.

Default agent behavior when uncertain: **create two nodes + a `CANDIDATE_SYNONYM` edge**
(schema v0.6.2) rather than assuming synonym. This is queryable ("show all unresolved
CANDIDATE_SYNONYM edges"), does not block KB construction, and defers the decision to
curation. Merging nodes later (migrate evidence, deprecate one) is straightforward.
Splitting a merged node (reconstruct which evidence belonged to which type) is not.

Curation resolution: confirm (→ EQUIVALENT + migrate evidence) or reject (→ document
distinguishing feature in caveats; change relationship to PARTIAL_OVERLAP or UNCERTAIN).

**When to add as synonym vs create new node:**
- Source paper *explicitly* defines one term as abbreviation of another ("hereafter OLM")
  → add as `TypeSynonym` on the existing node.
- Two names appear in different papers with overlapping but not identical characterisations
  → create two nodes + `CANDIDATE_SYNONYM` edge.

**Schema design (v0.6.1):** `CellTypeNode.synonyms` is a list of `TypeSynonym` objects,
each with:
- `term` (required) — the alternate name exactly as used in source
- `synonym_type` — enum: ABBREVIATION | HISTORICAL | ATLAS_LABEL | CROSS_SPECIES | INFORMAL
- `sources` — list of `PropertySource` (ref, snippet/quote_key, method, scope)

This mirrors the `AnatomicalLocation` pattern: a wrapper class with the term + evidence list.
A single synonym can have multiple sources (same term cited in multiple papers).

**Where this fits:** ASTA ingest should extract known synonyms as the first processing
step. KB gap review should flag nodes with no synonyms. Targeted search agents should
automatically expand queries with all known synonyms. New synonyms discovered during
mining → added to node before next search cycle.

---

## KB flags as workflow memory

Rather than a separate tracking file, workflow state is encoded as flags on KB nodes.
This keeps provenance in the KB and avoids a parallel bookkeeping system.

**How it works:**
- On each research cycle run, flags are set on the node (e.g. `survey_run: 2026-04-21`,
  `gaps_flagged: [anatomical_location, defining_markers]`).
- When information is found and written as PropertySource, the corresponding gap flag
  is cleared.
- The KB gap reviewer reads current flags + KB content to decide what to do next.
- This makes cycles efficient: the reviewer doesn't re-derive gaps from scratch,
  it reads the flag state.

**Priority tags in KB:** Gap flags can carry priority scores — `AT_dataset_gap: HIGH`
because AT needs a bridging dataset accession; `marker_gap: MODERATE` because ASTA
already has partial marker information. The gap reviewer uses these to decide what
targeted question to run next.

Aim: mapping improvement. Two main triggers for targeted search:
1. **Mapping evidence review** — what evidence would strengthen or refine an edge?
2. **Gap review** — what information is most beneficial to future mapping?
   (markers and AT transfer datasets are top priority)

---

## cite-traverse: from orchestrator to skill

cite-traverse is currently a named orchestrator — implying it should be run as a
top-level step. But **following citations is a technique, not a workflow phase.**

**Proposed redesign:** cite-traverse becomes a skill (`.claude/skills/cite-traverse.md`)
invokable by a targeted research agent when it judges that following a specific paper's
references will yield the answer to a bounded question. The skill:
- Takes one or more entry-point papers + a specific question
- Traverses 1–2 citation hops (bounded)
- Writes depth_N_summaries to output_dir
- Returns a summary of what was found

**What is preserved:** The multi-paper ASTA batch capability, the snippet filtering
logic, the PMC fallback — all of this lives in the skill and can be invoked from either
the survey path or the targeted path. Renaming does not reduce capability.

The broad survey-mode scan (ASTA corpus fan-out) uses the same underlying machinery
but is framed as "snippet scan of corpus" and lives in the survey orchestrator.

---

## Implications for current workflows

| Workflow | Current status | Proposed change |
|---|---|---|
| `lit-review.md` | **EXPERIMENTAL — DO NOT USE** | Retire; fold into survey orchestrator |
| `cite-traverse.md` | Working but overscoped as orchestrator | Refactor as skill; machinery preserved |
| `evidence-extraction.md` | Overengineered (5 steps, 3 gates) | Simplify: paper selection gate → extraction → KB write |
| `asta-report-ingest.md` | Working | Keep; add synonym extraction step |
| New: `survey.md` | Not yet written | ASTA-bounded lit scan after ingest |
| New: `targeted-search.md` | Not yet written | KB-gap-driven, invokes cite-traverse skill |

---

## Open questions

1. **Gap reviewer as step vs orchestrator entry**: Fluid makes more sense — in the
   spirit of iterative improvement. Efficiency maintained via KB flags (see above):
   the reviewer reads flag state rather than re-deriving gaps from scratch each time.

2. **How many targeted questions per cycle?** Hard to specify in advance. Priority
   tags in KB (see above) determine what runs. Aim is always improved mappings:
   primary triggers are mapping evidence review and gap review (markers and AT
   dataset accessions as top priorities).

3. **When does survey terminate?** Survey is bounded by the ASTA paper set (may be
   broadened in future — e.g. to include papers from a separate lit search run).
   After survey, results write to DB / KB, and gap flags + mapping state set
   priorities for targeted runs. No explicit handoff signal needed — the gap flags
   carry forward.

4. **Synonym bootstrapping:** Look for synonyms on each paper as first processing
   step; feed forward to subsequent queries in the same run. Snippet search may be
   insufficient — PMC full text likely needed for reliable synonym extraction.
   Mechanism: enrichment pass for high-relevance papers, triggered by relevance score.
   Also: leverage existing KB synonym content to seed queries.

5. **Per-node running summary cache:** If targeted runs produce summaries for narrow
   questions, a per-node cache of all collected summaries (across runs) avoids
   re-fetching. Unclear whether this is worth the complexity vs just re-running.
   Deferred until targeted-search orchestrator design.
