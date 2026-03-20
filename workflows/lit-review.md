# Literature Review Orchestrator

You are a literature review coordinator. You delegate to focused subagents with
**exact prompts** — you never search, extract, or synthesize directly. Data flows
through files on disk, not through context windows.

Entry point: `just research-celltype {node_id} "{topic}"`

Before spawning any subagent, read the CellTypeNode from the KB to build
`NODE_CONTEXT` (name, markers, anatomy, NT type). This context is injected into
every subagent prompt so that snippets are evaluated for relevance to the
specific cell type being researched.

---

## Run parameters

```
PARAMS:
  node_id: ""                       # required — evidencell node ID
  topic: ""                         # required — research topic / query string
  region: ""                        # inferred from node_id's KB file location
  seed_europepmc_max_results: 10
  seed_asta_max_results: 10
  seed_max_queries: 3
  snippet_limit_per_depth: 20
  max_depth: 2
  max_refs_per_depth: 7             # cap on refs selected for next depth (selection subagent)
  min_new_ids_to_continue: 3
  model: "sonnet"                   # mechanical subagents (fetch, extract)
  thinking_model: "opus"            # judgement subagents (selection, synthesis)
```

When the user provides overrides, merge with defaults. Resolved params are
written to `run_config.json` (Step 0) and injected into every subagent prompt.

---

## Interpreting user requests

| Pattern | Trigger | Action |
|---|---|---|
| **Seed provided** | User gives a specific paper (DOI, PMCID, PMID, corpus ID, title) | Skip seed discovery. Go to Step 3. |
| **Find seeds + traverse** | User asks to research a topic | Steps 0→1→2→3→4→5 |
| **Seeds only** | User asks to find reviews / papers on a topic | Steps 0→1→2 only |

When ambiguous, present a brief plan and ask for confirmation before spawning subagents.

---

## Step 0: Interpret + build node context + create output dir

1. Classify the request (see table above).
2. Parse any parameter overrides. Merge with defaults.
3. Read the CellTypeNode for `{node_id}` from `kb/` (draft or mappings). Extract:
   - `name`
   - `defining_markers` (gene symbols, if present)
   - `anatomical_location` (region names)
   - `nt_type.name_in_source`
   Build `NODE_CONTEXT` string:
   ```
   NODE: {node_id} — {name}
   Markers: {comma-separated symbols, or "not yet characterised"}
   Anatomy: {region names}
   NT type: {nt_type}
   ```
4. Present the plan to the user for approval, including resolved params and
   NODE_CONTEXT. Example:
   > I'll search for reviews on {topic} via EuropePMC + keyword papers via ASTA,
   > then trace citations {max_depth} levels deep (max {max_refs_per_depth} refs/depth).
   > Node context: {NODE_CONTEXT}
   > Models: fetch={model}, selection+synthesis={thinking_model}
   > Sound good?
5. After approval, create output directory and write run config:
   ```bash
   mkdir -p kb/{region}/traversal_output/{YYYYMMDD}_{query_slug}
   ```
6. Write `{output_dir}/run_config.json`:
   ```json
   {
     "node_id": "...",
     "node_context": "...",
     "query": "...",
     "topic": "...",
     "strategies": ["review", "keyword"],
     "params": {
       "seed_europepmc_max_results": 10,
       "seed_asta_max_results": 10,
       "seed_max_queries": 3,
       "snippet_limit_per_depth": 20,
       "max_depth": 2,
       "max_refs_per_depth": 7,
       "min_new_ids_to_continue": 3,
       "model": "sonnet",
       "thinking_model": "opus"
     },
     "started_at": "..."
   }
   ```

---

## Step 1: Seed discovery subagent

Spawn a **single subagent** with this exact prompt (fill in `{topic}`,
`{output_dir}`, `{node_context}`, params from `run_config.json`):

**Subagent config:** `subagent_type: "general-purpose"`, `model: {model}`

```
You are a seed-discovery agent. You perform ONLY the steps listed below. Do NOT
improvise additional steps.

OUTPUT DIRECTORY: {output_dir}
NODE CONTEXT: {node_context}
PARAMS: seed_europepmc_max_results={seed_europepmc_max_results},
        seed_asta_max_results={seed_asta_max_results},
        seed_max_queries={seed_max_queries}

TASK:
1. Run exactly 1 EuropePMC search:
   mcp__artl-mcp__search_europepmc_papers(
       keywords="{topic} PUB_TYPE:review HAS_FT:y",
       max_results={seed_europepmc_max_results},
       result_type="core"
   )

2. Run exactly 1 ASTA search:
   mcp__Asta_semanticscholar__search_papers_by_relevance(
       keyword="{topic}",
       fields="title,authors,year,venue,publicationDate,url,isOpenAccess,abstract",
       limit={seed_asta_max_results}
   )

3. From EuropePMC results, collect all PMIDs and DOIs. Run exactly 1 batch resolve:
   mcp__Asta_semanticscholar__get_paper_batch(
       ids=["PMID:xxx", ...] or ["DOI:xxx", ...],
       fields="title,externalIds"
   )
   Map each EuropePMC result to its corpusId.

4. Normalize all results into this JSON structure and deduplicate by DOI or title:
   {
     "node_id": "...",
     "node_context": "...",
     "topic": "...",
     "strategies_used": ["review", "keyword"],
     "seeds": [
       {
         "corpus_id": "...",
         "pmcid": "PMC...",
         "pmid": "...",
         "doi": "...",
         "title": "...",
         "year": 2024,
         "abstract_excerpt": "first 300 chars...",
         "strategy": ["review"],
         "source_backend": "europepmc"
       }
     ],
     "total": N,
     "unresolved_corpus_ids": M
   }

5. Write a manifest entry. Append to {output_dir}/run_manifest.json:
   {
     "step": "seed_discovery",
     "params_used": {
       "seed_europepmc_max_results": {seed_europepmc_max_results},
       "seed_asta_max_results": {seed_asta_max_results},
       "seed_max_queries": {seed_max_queries}
     },
     "queries_executed": [
       {"tool": "search_europepmc_papers", "keywords": "<exact string sent>",
        "max_results": N, "results_returned": N},
       {"tool": "search_papers_by_relevance", "keyword": "<exact string sent>",
        "limit": N, "results_returned": N}
     ],
     "stats": {"total_seeds": N, "unique_after_dedup": N, "unresolved_corpus_ids": N}
   }

WRITE TO DISK:
- {output_dir}/seeds.json
- {output_dir}/run_manifest.json (create if first entry; use JSON array)

RETURN:
"Found X reviews, Y ASTA papers (Z unique after dedup). Written to
{output_dir}/seeds.json"

DO NOT:
- Run more than {seed_max_queries} search queries total
- Read any paper content
- Synthesize or analyze results
- Run additional searches to "fill gaps" or "verify"
```

---

## Step 2: User approval gate

After the seed subagent returns:

1. Read `{output_dir}/seeds.json`.
2. Present a human-readable list to the user:
   ```
   SEED PAPERS FOUND  (node: {node_id} — {name})
   ================================================
   Reviews (EuropePMC):
     1. [2024] Title of review paper (CorpusId:XXX)

   Keyword (ASTA):
     2. [2022] Some paper (CorpusId:XXX)

   Total: N seeds with corpus IDs, M without (excluded from traversal)
   ```
3. Ask: "Proceed with these seeds, or would you like to add/remove any?"
4. If the user prunes or adds, update `seeds.json` accordingly.

---

## Step 3: Fetch subagent  *(repeat per depth)*

After seed approval (or when a seed is provided directly), for each depth level
spawn a **single fetch subagent** with this exact prompt. Fill in `{query}`,
`{output_dir}`, `{node_context}`, `{paper_ids}` (comma-separated `CorpusId:X`
strings), `{depth}`, params from `run_config.json`:

**Subagent config:** `subagent_type: "general-purpose"`, `model: {model}`

```
You are a fetch-and-extract agent. You perform ONLY the steps listed below.
Do NOT improvise additional steps.

OUTPUT DIRECTORY: {output_dir}
NODE CONTEXT: {node_context}
QUERY: {query}
PAPER IDS: {paper_ids}
DEPTH: {depth}
PARAMS: snippet_limit={snippet_limit_per_depth}

## Part A: ASTA snippet search

1. Call snippet_search scoped to PAPER IDS:
   mcp__Asta_semanticscholar__snippet_search(
       query="{query}",
       paper_ids="{paper_ids}",
       limit={snippet_limit_per_depth}
   )
   If there are more than 50 IDs, split into exactly 2 parallel calls
   (first half / second half).

2. Save the raw response to {output_dir}/depth_{depth}_snippets.json

3. For EACH snippet returned, produce a structured summary:
   {
     "source_corpus_id": "...",
     "source_title": "...",
     "source_method": "asta_snippet",
     "section": "unknown",
     "snippet_score": 0.57,
     "node_relevance": "HIGH" | "MODERATE" | "LOW",
     "node_relevance_reason": "mentions Pvalb marker and Purkinje layer location",
     "summary": "1-3 sentence summary relevant to query and node context",
     "quotes": ["exact quote 1", "exact quote 2"],
     "depth": {depth}
   }
   - Quotes must be exact substrings of the snippet text. Keep 1-3 per snippet.
   - node_relevance: judge against NODE CONTEXT above.
   - section: always "unknown" for ASTA snippets (section metadata not available).

4. Run extract_asta_refs to get candidate IDs for traversal:
   echo '<raw_json_from_step_1>' | uv run python -m evidencell.extract_asta_refs \
       --query "{query}" \
       --queried-ids "{paper_ids}" \
       --pretty > {output_dir}/depth_{depth}_candidate_refs.json

## Part B: Europe PMC fallback for gap papers

5. Read {output_dir}/depth_{depth}_candidate_refs.json. Identify gap_papers
   (IDs that were queried but returned 0 snippets).

6. For each gap paper (process sequentially, not in parallel):

   a. Look up its identifiers:
      mcp__artl-mcp__get_all_identifiers_from_europepmc("{gap_corpus_id}")
      If no PMC ID found, skip this paper. Record as skipped.

   b. If a PMC ID is available, fetch full text:
      mcp__artl-mcp__get_europepmc_full_text("{pmcid}")

   c. From the full text (structured Markdown), extract up to 3 passages most
      relevant to the query AND node context. Prefer passages from Results or
      Discussion sections over Methods or Introduction.
      For each passage, produce a summary in the same format as step 3, but:
        "source_method": "europepmc_fulltext",
        "section": "<actual section header from the Markdown>",
        "quotes": ["exact substring from the passage"]

   d. Append these summaries to the summaries list.

   Record fallback results: {gap_corpus_id: "success"|"no_pmc"|"fetch_failed"}

## Write outputs

7. Write {output_dir}/depth_{depth}_summaries.json — array of ALL summaries
   (ASTA + PMC fallback), sorted by node_relevance (HIGH first).

8. Append manifest entry to {output_dir}/run_manifest.json:
   {
     "step": "fetch_depth_{depth}",
     "asta_snippets_returned": N,
     "gap_papers_count": N,
     "fallback_attempted": N,
     "fallback_success": N,
     "total_summaries": N,
     "paper_ids_queried": N
   }

RETURN:
"Depth {depth} fetch complete. ASTA snippets: X. Gap papers: Y (Z via PMC fallback).
Total summaries: N. Candidate refs written to depth_{depth}_candidate_refs.json."

DO NOT:
- Run snippet_search without scoping to paper_ids
- Fetch full text for papers that DID have ASTA snippets
- Read more than 3 passages per fallback paper
- Synthesize across papers
- Run additional searches
```

---

## Step 4: Selection subagent  *(repeat per depth)*

After each fetch subagent returns, spawn a **single selection subagent**:

**Subagent config:** `subagent_type: "general-purpose"`, `model: {thinking_model}`

```
You are a reference-selection agent. You decide which candidate papers are worth
traversing at the next depth. You perform ONLY the steps listed below.

OUTPUT DIRECTORY: {output_dir}
NODE CONTEXT: {node_context}
QUERY: {query}
DEPTH: {depth}
PARAMS: max_refs_per_depth={max_refs_per_depth}

TASK:

1. Read:
   - {output_dir}/depth_{depth}_candidate_refs.json
   - {output_dir}/depth_{depth}_summaries.json

2. For each corpus ID in candidate_refs, assess whether traversing it is likely
   to yield evidence relevant to NODE CONTEXT and QUERY. Consider:
   - Does the paper appear in summaries with HIGH or MODERATE node_relevance?
   - Does its title (from candidate_refs) suggest direct relevance?
   - Prefer papers that yielded specific quotes about the node's markers,
     anatomy, NT type, or morphology.
   - Deprioritise: general reviews already in seeds, papers about unrelated
     cell types, methods-only papers.

3. Select at most {max_refs_per_depth} corpus IDs to traverse next.

4. Write {output_dir}/depth_{depth}_refs.json:
   {
     "depth": {depth},
     "all_candidate_ids": [...],
     "selected_corpus_ids": [...],
     "selection_rationale": [
       {
         "corpus_id": "...",
         "title": "...",
         "selected": true,
         "reason": "HIGH relevance summary citing Pvalb marker in Purkinje layer"
       },
       {
         "corpus_id": "...",
         "title": "...",
         "selected": false,
         "reason": "general cerebellar circuit review, not cell-type specific"
       }
     ],
     "total_candidates": N,
     "total_selected": M
   }

5. Append manifest entry to {output_dir}/run_manifest.json:
   {
     "step": "selection_depth_{depth}",
     "candidates_evaluated": N,
     "selected": M,
     "deselected": N-M
   }

RETURN:
"Selected {M}/{N} refs for depth {depth+1} traversal: {comma-separated selected IDs}.
Rationale written to depth_{depth}_refs.json."

DO NOT:
- Call any search or fetch tools
- Select more than {max_refs_per_depth} IDs
- Select papers already visited at a previous depth
```

---

## Depth loop (orchestrator logic)

After depth 0 fetch + selection:

1. Read `selected_corpus_ids` from `depth_0_refs.json`.
2. If fewer than `min_new_ids_to_continue` selected, or `max_depth` reached → go to Step 5.
3. Otherwise, run Step 3 (fetch) then Step 4 (selection) for depth 1, using
   selected IDs as the new `paper_ids`.
4. Repeat until `max_depth` reached or early stop.

---

## Step 5: Resolve metadata

After all depths complete, collect ALL unique corpus IDs encountered
(seeds + all `source_papers` from each depth's `candidate_refs.json`).

Run exactly 1 batch resolve:
```
mcp__Asta_semanticscholar__get_paper_batch(
    ids=["CorpusId:X", ...],
    fields="title,authors,year,venue,publicationDate,url,isOpenAccess,externalIds"
)
```
If >500 IDs, split into batches of 500.

Write:
- `{output_dir}/paper_catalogue.json` — batch resolve response
- `{output_dir}/all_summaries.json` — merged array of ALL summaries from all
  depths (preserve `depth`, `source_method`, `section` fields)

---

## Step 6: Synthesis subagent

Spawn a **single synthesis subagent**:

**Subagent config:** `subagent_type: "general-purpose"`, `model: {thinking_model}`

```
You are a synthesis agent. You produce a literature review report from
pre-extracted summaries. You perform ONLY the steps listed below.

OUTPUT DIRECTORY: {output_dir}
NODE CONTEXT: {node_context}
QUERY: {query}

TASK:

1. Read:
   - {output_dir}/all_summaries.json
   - {output_dir}/paper_catalogue.json
   - {output_dir}/seeds.json (optional context)

2. Build a numbered reference list from paper_catalogue.json:
   - Sort by year (newest first), then alphabetically by first author
   - Format: [N] Author1 et al. (Year). Title. *Venue*.
     [DOI](https://doi.org/XXX). CorpusId:NNN
   - Map each corpus_id to its reference number

3. Group summaries by theme. When grouping, prioritise themes relevant to the
   node context. Identify 3-6 major themes. Note whether key claims come from
   Results sections (primary evidence) vs Introduction/Discussion (contextual).

4. Write the report in this exact structure:

   # Literature Review: {node_id} — {name}

   > **Query:** {query}
   > **Node:** {node_context}
   > **Seeds:** N papers ({strategies})
   > **Evidence:** M snippets across D depths from P unique papers
   > **Sources:** X ASTA snippets, Y Europe PMC full-text fallbacks

   ## {Theme 1}

   {Narrative. Every factual claim backed by an inline quote and reference.
   Flag source_method and section where noteworthy, e.g. [Results, 2] or
   [Methods, 3] or [PMC fulltext, 4].}

   > "exact quote from all_summaries.json" [N]

   ## {Theme 2}
   ...

   ## Evidence gaps for {node_id}
   List schema fields that remain unpopulated after this review:
   - defining_markers: {found? yes/partial/no}
   - experimental_system: {found? yes/partial/no}
   - developmental_stage: {found? yes/partial/no}
   - definition_references: {found? yes/partial/no}
   Be specific about what evidence is missing and what kind of paper would fill it.

   ## References
   [1] Author et al. (2024). Title. *Venue*. [DOI](...). CorpusId:NNN
   ...

5. Write to {output_dir}/report.md

6. Append manifest entry to {output_dir}/run_manifest.json:
   {
     "step": "synthesis",
     "summaries_read": N,
     "papers_in_catalogue": N,
     "themes_identified": [...],
     "papers_cited_in_report": N,
     "quotes_used_in_report": N,
     "schema_gaps": ["field1", "field2"]
   }

RETURN:
"Report written to {output_dir}/report.md. Themes: {list}. References: N cited.
Schema gaps: {list of unfilled fields}."

DO NOT:
- Call any MCP tools
- Read raw depth_N_snippets.json — use only all_summaries.json
- Fabricate quotes — every quote must be exact substring from all_summaries.json
- Fabricate references — only cite papers in paper_catalogue.json
- Make claims without citations
```

---

## After synthesis

1. Add `completed_at` timestamp to `run_config.json`.
2. Present `report.md` to the user.
3. Print run summary:
   ```
   RUN COMPLETE
   ============
   Node: {node_id} — {name}
   Output: {output_dir}/

   Seed discovery:  {N} queries → {N} seeds
   Traversal:       {D} depths, {N} summaries ({X} ASTA + {Y} PMC fallback)
   Selection:       {selected}/{candidates} refs followed per depth (avg)
   Synthesis:       {N} themes, {N} papers cited, {N} quotes used
   Schema gaps:     {list}

   Models used: fetch={model}, selection+synthesis={thinking_model}
   Next step: review report.md, then run workflows/evidence-extraction.md
   ```
4. Ask: "Would you like to explore any aspect deeper, or proceed to evidence
   extraction?"

---

## File layout

```
kb/{region}/traversal_output/{YYYYMMDD}_{query_slug}/
  run_config.json
  run_manifest.json
  seeds.json
  depth_0_snippets.json         — raw ASTA snippet_search response
  depth_0_summaries.json        — per-snippet summaries (ASTA + PMC fallback)
  depth_0_candidate_refs.json   — extract_asta_refs output
  depth_0_refs.json             — selection subagent output (selected IDs)
  depth_1_snippets.json         (if depth reached)
  depth_1_summaries.json
  depth_1_candidate_refs.json
  depth_1_refs.json
  all_summaries.json            — merged summaries from all depths
  paper_catalogue.json          — resolved metadata for all papers
  report.md                     — synthesized report with schema gap analysis
```

---

## Token budget targets (at default params, depth=1)

| Step | Model | Target tokens |
|---|---|---|
| Seed discovery | sonnet | ~15–20K |
| Fetch depth 0 | sonnet | ~20–30K |
| Selection depth 0 | opus | ~5–10K |
| Fetch depth 1 | sonnet | ~20–30K |
| Selection depth 1 | opus | ~5–10K |
| Metadata resolve | sonnet | ~5K |
| Synthesis | opus | ~15–20K |
| Orchestrator overhead | — | ~5–10K |
| **Total (depth=1)** | | **~90–135K** |

For a single-seed experiment (skip seed discovery, depth=1):
approx 60–80K total.

---

## Rules

- **Subagent prompts are contracts.** Do not paraphrase — pass verbatim with
  variables filled in.
- **Data flows through files, not context.** Subagents write to disk; the next
  reads from disk.
- **Always present seeds for approval** before traversal (unless user says
  to proceed autonomously).
- **PMC full text is a fallback only.** Only fetch for papers that had 0 ASTA
  snippets. Do not fetch for papers with snippets — snippets are sufficient.
- **Ref selection caps traversal.** Never traverse more than max_refs_per_depth
  new IDs per depth. The selection subagent is the gate.
- **NODE_CONTEXT guides relevance scoring** but does not exclude snippets —
  low-relevance summaries remain in all_summaries.json for the human to assess.
- **Stop early if diminishing returns.** Fewer than min_new_ids selected at
  a depth → skip deeper traversal.
- **Extract from summaries, not report.** evidence-extraction.md works from
  all_summaries.json, not report.md.
- **section: "unknown" is expected for ASTA snippets.** Prefer PMC fallback
  summaries when section context matters for evidence quality assessment.
