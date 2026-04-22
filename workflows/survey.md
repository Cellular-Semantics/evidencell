# Survey Orchestrator

You are a literature survey coordinator. You run a single-pass snippet search across
all ASTA corpus papers for a region and produce `all_summaries.json` — the input for
`evidence-extraction.md`. No synthesis. No KB writes. This is a fetch-and-assess step.

Called before: `workflows/evidence-extraction.md` (per node)

---

## Run parameters

```
PARAMS:
  region:           ""    # required — e.g. "hippocampus"
  node_ids:         []    # required — list of node IDs in scope
  corpus_ids_file:  ""    # required — path to pdf_corpus_ids.json (asta-report-ingest output)
                          #   OR pass corpus_ids directly as a list
  output_dir:       ""    # required — where to write outputs
  model:            "sonnet"   # fetch subagent is mechanical; sonnet is sufficient
  snippet_limit:    20    # max snippets per paper per API call
```

---

## Step 0: Build region context

1. For each `node_id` in `{node_ids}`, locate its KB file:
   ```
   uv run python -c "from evidencell.paths import find_node_file; print(find_node_file('{node_id}'))"
   ```

2. Read each KB file. For each node, extract:
   - `name`
   - `defining_markers` (gene symbols from GeneDescriptor entries)
   - `anatomical_location` (labels)
   - `nt_type.name_in_source` (if present)

3. Read `{corpus_ids_file}` (a JSON array of Semantic Scholar corpus ID strings).
   Store as `CORPUS_IDS`.

4. Build `REGION_CONTEXT` — one line per node:
   ```
   Nodes in scope: {N}
   {node_id}: {name} | markers: {symbols} | location: {locations} | NT: {nt_type or "unknown"}
   ...
   ```

5. Build `QUERY` — a string joining all node names and key marker symbols:
   ```
   {name1}, {name2}, ..., {marker1}, {marker2}, ...
   ```
   Keep it under ~200 characters; drop the least specific terms if needed.

---

## Step 1: Fetch subagent

Spawn a **single fetch subagent** with this exact prompt. Fill in all variables
before spawning.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {model}`

```
You are a literature fetch agent. Your job is to retrieve snippets for a set of
ASTA corpus papers and produce all_summaries.json.

REGION:          {region}
QUERY:           {query}
CORPUS IDS:      {corpus_ids}   (JSON array)
REGION CONTEXT:  {region_context}
OUTPUT DIR:      {output_dir}
SNIPPET LIMIT:   {snippet_limit}

## Task

1. Call mcp__Asta_semanticscholar__snippet_search with QUERY and all CORPUS IDS.
   If there are more than 50 corpus IDs, split into two parallel calls.
   Use snippet_limit: {snippet_limit}.

2. Filter snippets:
   - Discard any snippet where kind == "title"
   - Discard snippets from sections matching: "peer review", "reviewer", "references"

3. For each remaining snippet, group by source_corpus_id. For papers with >1 snippet,
   keep the highest-scored snippet as primary (or the body snippet over abstract if
   scores are equal). Retain up to 3 snippets per paper.

4. For each paper (corpus_id), produce a LiteratureSummary entry:
   {
     "source_corpus_id": "{corpus_id}",
     "source_title": "{paper title from snippet metadata}",
     "source_method": "ASTA_SNIPPET",
     "snippet_kind": "{kind}",
     "section": "{section or 'unknown'}",
     "snippet_score": {score or null},
     "node_relevance": "{HIGH|MODERATE|LOW}",
     "node_relevance_reason": "{one sentence citing specific markers/anatomy/NT type}",
     "summary": "{1-3 sentences: key findings relevant to region nodes}",
     "quotes": ["{verbatim substring 1}", "{verbatim substring 2}"],
     "depth": 0,
     "synonyms_found": [
       {
         "term": "{alternate name or abbreviation}",
         "source_corpus_id": "{corpus_id}",
         "quote": "{verbatim passage where defined}",
         "section": "{section}"
       }
     ]
   }

   node_relevance assignment:
   - HIGH: directly characterises a node in REGION CONTEXT (mentions its name,
     markers, or anatomical location with specific evidence)
   - MODERATE: consistent with a node but indirect or in a related context
   - LOW: tangentially relevant; mentions region-level terms without node specificity

   synonyms_found rules:
   - Scan the snippet text for alternate names or abbreviations for nodes in
     REGION CONTEXT. Look for patterns:
     "hereafter X", "referred to as X", "also known as X", "(X)", or a
     parenthetical abbreviation immediately after a full cell-type name.
   - Record only terms that appear to define or introduce an alternate name for a
     node — do not record every abbreviation in the text.
   - Leave synonyms_found as [] if none are found.

   quotes rules:
   - Select 1–3 verbatim substrings from the snippet text that best support the
     node_relevance assessment. Must be exact substrings — no paraphrase, no merging.
   - Prefer quotes that mention specific markers, anatomy, or functional properties.

5. Gap papers: corpus_ids that returned 0 snippets after filtering.
   For each gap paper, attempt PMC full-text fallback:
   - Call mcp__artl-mcp__get_europepmc_paper_by_id with the corpus_id
     (or PMID/DOI if known) to get the PMCID.
   - If PMCID available, call mcp__artl-mcp__get_europepmc_full_text.
   - Extract the most relevant passage (up to ~500 words) from the Methods,
     Results, or Abstract section. Produce a LiteratureSummary entry with
     source_method: "EUROPEPMC_FULLTEXT" and snippet_score: null.
   - If PMC full-text is unavailable, record the corpus_id in gap_papers but
     do not fabricate content. Leave it out of all_summaries.json.

6. Write {output_dir}/all_summaries.json — a JSON array of all LiteratureSummary
   entries, ordered by node_relevance (HIGH first, then MODERATE, then LOW).

7. Report back:
   "Fetch complete. {N} papers queried. {M} summaries produced. {G} gap papers
   ({P} via PMC fallback). Synonyms found: {K} candidates."

DO NOT:
- Paraphrase or merge quotes — exact verbatim substrings only
- Fabricate snippets for gap papers — if no text available, skip
- Write to KB YAML or references.json — this step is fetch only
- Call snippet_search more than twice (batch all IDs into ≤2 calls)
```

---

## Step 2: Collect synonyms + write outputs

After the fetch subagent returns:

1. Read `{output_dir}/all_summaries.json`.

2. Collect all `synonyms_found` entries across all summaries into a flat list.

3. Deduplicate by `(term.lower(), source_corpus_id)` — keep first occurrence.

4. Write `{output_dir}/synonyms_candidates.json`:
   ```json
   [
     {
       "term": "OLM",
       "source_corpus_id": "201041756",
       "quote": "we refer to oriens-lacunosum moleculare cells, hereafter OLM",
       "section": "Introduction"
     }
   ]
   ```
   Write an empty array `[]` if no synonyms were found.

5. Write `{output_dir}/run_config.json`:
   ```json
   {
     "region": "{region}",
     "node_ids": [...],
     "corpus_ids_file": "{corpus_ids_file}",
     "model": "{model}",
     "started_at": "{ISO timestamp}"
   }
   ```

6. Write `{output_dir}/run_manifest.json`:
   ```json
   {
     "region": "{region}",
     "node_ids": [...],
     "corpus_ids_queried": N,
     "summaries_produced": N,
     "gap_papers": N,
     "pmc_fallback_success": N,
     "synonym_candidates": N,
     "output_dir": "{output_dir}"
   }
   ```

7. Print:
   ```
   SURVEY COMPLETE
   ===============
   Region:     {region}
   Papers:     {N} queried, {M} summaries produced, {G} gap papers ({P} via PMC)
   Synonyms:   {K} candidates found

   Outputs:
     {output_dir}/all_summaries.json
     {output_dir}/synonyms_candidates.json

   Next steps:
     1. Review synonyms_candidates.json — confirm any to add as TypeSynonym entries
     2. Run workflows/evidence-extraction.md for each node:
        node_ids: {node_ids}
        summaries_file: {output_dir}/all_summaries.json
   ```

---

## Rules

- **survey.md stops at all_summaries.json.** No synthesis. No KB writes.
- **Region-level, not per-node.** Per-node filtering is evidence-extraction's job.
- **No human gate.** ASTA corpus is pre-curated. Agents handle relevance assessment.
- **Synonym extraction is best-effort.** Heuristic pattern matching, not exhaustive.
  Missed synonyms are not a correctness failure.
- **Subagent prompts are contracts.** Pass verbatim with variables filled in.
- **Data flows through files, not context.**
- **find_node_file() for all KB access.** Never hardcode KB file paths.
