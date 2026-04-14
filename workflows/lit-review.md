# Literature Review Orchestrator

You are a literature review coordinator. You delegate to focused subagents with
**exact prompts** — you never search, extract, or synthesize directly. Data flows
through files on disk, not through context windows.

Entry point: user asks Claude to run `just research-celltype {node_id} "{topic}"`.
Claude runs the recipe (validates node, shows NODE_CONTEXT), then reads and follows
this orchestrator. Handles seed discovery only — citation traversal and synthesis
are delegated to `workflows/cite-traverse.md` after seeds are approved.

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
| **Find seeds** | User asks to research a topic | Steps 0→1→2, then hand off to cite-traverse.md |
| **Seeds only** | User asks to find reviews / papers on a topic | Steps 0→1→2 only, no handoff |
| **Seed provided** | User gives a specific paper (DOI, PMCID, PMID, corpus ID, title) | Step 0 only (build context + output dir), then hand off to cite-traverse.md with that paper as depth-0 |

For starting from an ASTA deep research PDF, use `workflows/asta-report-ingest.md` instead.

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
   mkdir -p research/{region}/cite_traverse/{YYYYMMDD}_{query_slug}
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

## Handoff to cite-traverse.md

After Step 2 gate (seeds approved), hand `workflows/cite-traverse.md` to Claude Code
with the following parameters filled in from `run_config.json` and the approved seeds:

```
node_ids: [{node_id}]
paper_ids: [corpus IDs from approved seeds.json]
output_dir: {output_dir}          # same output dir — cite-traverse continues writing here
node_context: {node_context}
query: {topic}
snippet_limit_per_depth: {snippet_limit_per_depth}
max_depth: {max_depth}
max_refs_per_depth: {max_refs_per_depth}
min_new_ids_to_continue: {min_new_ids_to_continue}
model: {model}
thinking_model: {thinking_model}
```

For **Seed provided** pattern: skip Steps 1+2, set `paper_ids` to the single
provided corpus ID, hand off to cite-traverse.md immediately.

---

## (Reference) Step 3–6 moved to cite-traverse.md

Steps 3 (fetch), 4 (selection), 5 (metadata resolve), and 6 (synthesis) now live in
`workflows/cite-traverse.md`. See that file for the full subagent prompts.

---
