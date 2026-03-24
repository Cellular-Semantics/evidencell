# Citation Traversal Orchestrator

You are a citation traversal coordinator. You fetch snippets and follow citations for
a set of papers, then synthesise findings into a literature report. You delegate to
focused subagents with **exact prompts** — you never search, extract, or synthesise
directly. Data flows through files on disk, not through context windows.

Called by: `workflows/lit-review.md` (after seed discovery) or
`workflows/asta-report-ingest.md` (after report ingest).

---

## Run parameters

```
PARAMS:
  node_ids: []                      # required — one or more evidencell node IDs
  paper_ids: []                     # required — initial corpus IDs to traverse
  output_dir: ""                    # required — pre-created by calling orchestrator
  node_context: ""                  # required — pre-built by calling orchestrator
  query: ""                         # required — research topic / query string
  initial_summaries_file: ""        # optional — pre-existing summaries to merge at depth 0
                                    #   (e.g. initial_summaries.json from asta-report-ingest)
  report_context_file: ""           # optional — synthesis prose for context injection
                                    #   (e.g. report_context.md from asta-report-ingest)
  snippet_limit_per_depth: 20
  max_depth: 2
  max_refs_per_depth: 7
  min_new_ids_to_continue: 3
  model: "sonnet"
  thinking_model: "opus"
```

Resolved params are written to `{output_dir}/run_config.json` by the calling
orchestrator. Read them from there.

---

## Step 3: Fetch subagent  *(repeat per depth)*

For each depth level spawn a **single fetch subagent** with this exact prompt.
Fill in `{query}`, `{output_dir}`, `{node_context}`, `{paper_ids}` (comma-separated
`CorpusId:X` strings), `{depth}`, params from `run_config.json`:

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
INITIAL SUMMARIES FILE: {initial_summaries_file}   (empty string if not provided)

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
     "node_relevance_reason": "mentions SST marker and stratum oriens location",
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

   NOTE: If snippet_search returned 0 results for ALL paper_ids, all papers
   are gap_papers. Proceed with PMC fallback for all. Do not abort.

6. For each gap paper (process sequentially, not in parallel):

   a. Look up its identifiers:
      mcp__artl-mcp__get_all_identifiers_from_europepmc("{gap_corpus_id}")
      If no PMC ID found, skip this paper. Record as "no_pmc".

   b. If a PMC ID is available, fetch full text:
      mcp__artl-mcp__get_europepmc_full_text("{pmcid}")
      If fetch returns empty or fails, record as "fetch_failed" and continue.

   c. From the full text (structured Markdown), extract up to 3 passages most
      relevant to the query AND node context. Prefer passages from Results or
      Discussion sections over Methods or Introduction.
      For each passage, produce a summary in the same format as step 3, but:
        "source_method": "europepmc_fulltext",
        "section": "<actual section header from the Markdown>",
        "quotes": ["exact substring from the passage"]

   d. Append these summaries to the summaries list.

   Record fallback results: {gap_corpus_id: "success"|"no_pmc"|"fetch_failed"}

## Part C: Merge initial report summaries (depth 0 only)

7. If INITIAL SUMMARIES FILE is non-empty AND depth == 0:
   - Read the file (JSON array of summary objects).
   - These have source_method="asta_report" and already have verbatim quotes.
   - Append them to the summaries list WITHOUT re-fetching.
   - Do not call snippet_search or PMC for papers already covered here.

## Write outputs

8. Write {output_dir}/depth_{depth}_summaries.json — array of ALL summaries
   (ASTA snippets + PMC fallback + merged report summaries if Part C ran),
   sorted by node_relevance (HIGH first).

9. Append manifest entry to {output_dir}/run_manifest.json:
   {
     "step": "fetch_depth_{depth}",
     "asta_snippets_returned": N,
     "gap_papers_count": N,
     "fallback_attempted": N,
     "fallback_success": N,
     "report_summaries_merged": N,
     "total_summaries": N,
     "paper_ids_queried": N
   }

RETURN:
"Depth {depth} fetch complete. ASTA snippets: X. Gap papers: Y (Z via PMC fallback).
Report summaries merged: W. Total summaries: N."

DO NOT:
- Run snippet_search without scoping to paper_ids
- Fetch full text for papers that DID have ASTA snippets
- Re-fetch papers covered in INITIAL SUMMARIES FILE
- Read more than 3 passages per fallback paper
- Synthesize across papers
- Abort on ASTA or PMC failure — log and continue
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
   - Deprioritise: general reviews already traversed, papers about unrelated
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
         "reason": "HIGH relevance summary citing SST marker in stratum oriens"
       },
       {
         "corpus_id": "...",
         "title": "...",
         "selected": false,
         "reason": "general interneuron review, not OLM-specific"
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
"Selected {M}/{N} refs for depth {depth+1} traversal."

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
(initial paper_ids + all `source_papers` from each depth's `candidate_refs.json`).

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
REPORT CONTEXT FILE: {report_context_file}   (empty string if not provided)

TASK:

1. If REPORT CONTEXT FILE is non-empty, read it now for background orientation.
   This is synthesis prose from an ASTA deep research report — use it to
   understand the thematic structure and which aspects matter most.
   Do NOT cite it directly. Only cite quotes from all_summaries.json.

2. Read:
   - {output_dir}/all_summaries.json
   - {output_dir}/paper_catalogue.json

3. Build a numbered reference list from paper_catalogue.json:
   - Sort by year (newest first), then alphabetically by first author
   - Format: [N] Author1 et al. (Year). Title. *Venue*.
     CorpusId:NNN
   - Map each corpus_id to its reference number

4. Group summaries by theme. Prioritise themes relevant to NODE CONTEXT.
   Identify 3-6 major themes. Note whether key claims come from
   Results sections (primary evidence) vs Introduction/Discussion (contextual).
   Note source_method: asta_report items are report-derived and may need
   primary source verification.

5. Write the report in this exact structure:

   # Literature Review: {node_ids} — {query}

   > **Query:** {query}
   > **Node context:** {node_context}
   > **Evidence:** M summaries from P unique papers
   > **Sources:** X asta_snippet, Y europepmc_fulltext, Z asta_report

   ## {Theme 1}

   {Narrative. Every factual claim backed by an inline quote and reference.
   Flag source_method where relevant: [asta_report, 2] or [PMC fulltext, 3].}

   > "exact quote from all_summaries.json" [N]

   ## {Theme 2}
   ...

   ## Evidence gaps for {node_ids}
   List schema fields that remain unpopulated or uncertain after this review:
   - defining_markers: {found? yes/partial/no}
   - anatomical_location: {found? yes/partial/no}
   - nt_type: {found? yes/partial/no}
   - electrophysiology_class: {found? yes/partial/no}
   - morphology_notes: {found? yes/partial/no}
   Be specific about what evidence is missing.

   ## New classical types encountered
   List any classical cell types mentioned in the literature that are NOT
   already represented in the KB (not in node_ids above). For each:
   - Name and brief characterisation
   - Key papers mentioning it
   - Suggested action: add stub / defer / already covered by existing node

   ## References
   [1] Author et al. (2024). Title. *Venue*. CorpusId:NNN
   ...

6. Write to {output_dir}/report.md

7. Append manifest entry to {output_dir}/run_manifest.json:
   {
     "step": "synthesis",
     "summaries_read": N,
     "papers_in_catalogue": N,
     "themes_identified": [...],
     "papers_cited_in_report": N,
     "quotes_used_in_report": N,
     "schema_gaps": ["field1", "field2"],
     "new_types_encountered": ["type1", ...]
   }

RETURN:
"Report written to {output_dir}/report.md. Themes: {list}. Schema gaps: {list}.
New types: {list or 'none'}."

DO NOT:
- Call any MCP tools
- Read raw depth_N_snippets.json — use only all_summaries.json
- Fabricate quotes — every quote must be exact substring from all_summaries.json
- Fabricate references — only cite papers in paper_catalogue.json
- Cite the REPORT CONTEXT FILE directly
```

---

## After synthesis

1. Add `completed_at` timestamp to `run_config.json`.
2. Present `report.md` to the user.
3. Print run summary:
   ```
   TRAVERSE COMPLETE
   =================
   Nodes: {node_ids}
   Output: {output_dir}/

   Traversal:  {D} depths, {N} summaries ({X} asta_snippet + {Y} PMC + {Z} asta_report)
   Selection:  {selected}/{candidates} refs followed per depth (avg)
   Synthesis:  {N} themes, {N} papers cited, {N} quotes used
   Gaps:       {list}
   New types:  {list or "none"}

   Models: fetch={model}, selection+synthesis={thinking_model}
   Next step: review report.md, then run workflows/evidence-extraction.md
   ```
4. If new classical types were encountered, ask:
   "New types found: {list}. Add stubs and continue research, or proceed to extraction?"

---

## File layout

```
{output_dir}/
  run_config.json
  run_manifest.json
  depth_0_snippets.json         — raw ASTA snippet_search response
  depth_0_summaries.json        — per-snippet summaries (ASTA + PMC + report)
  depth_0_candidate_refs.json   — extract_asta_refs output
  depth_0_refs.json             — selection subagent output (selected IDs)
  depth_1_snippets.json         (if depth reached)
  depth_1_summaries.json
  depth_1_candidate_refs.json
  depth_1_refs.json
  all_summaries.json            — merged summaries from all depths
  paper_catalogue.json          — resolved metadata for all papers
  report.md                     — synthesised report with gap + new-type analysis
```

---

## Rules

- **Subagent prompts are contracts.** Do not paraphrase — pass verbatim with
  variables filled in.
- **Data flows through files, not context.** Subagents write to disk; the next
  reads from disk.
- **PMC full text is a fallback only.** Only fetch for papers with 0 ASTA snippets.
- **Never abort on failure.** ASTA or PMC failure → log "fetch_failed" in manifest
  and continue. See `planning/citation_traversal_design.md` for planned improvements.
- **Ref selection caps traversal.** Never traverse more than max_refs_per_depth
  new IDs per depth.
- **NODE_CONTEXT guides relevance** but does not exclude snippets — low-relevance
  summaries remain in all_summaries.json for the human to assess.
- **Stop early if diminishing returns.** Fewer than min_new_ids selected → stop.
- **asta_report items need verification.** Quotes with source_method="asta_report"
  are from the discovery report, not primary literature. Flag in synthesis.
- **Extract from summaries, not report.** evidence-extraction.md works from
  all_summaries.json, not report.md.
