# Evidence Extraction Orchestrator

You are an evidence extraction coordinator. You take `all_summaries.json` produced
by a survey or asta-report-ingest run and write `PropertySource` entries directly to
KB nodes. The extraction subagent writes quotes to `references.json` and
`PropertySource` entries (with `quote_key`) to KB YAML.

The pre-edit hook is the structural validation gate — it verifies every `quote_key`
exists in `references.json` before the KB write proceeds.

Called after: `workflows/asta-report-ingest.md` or `workflows/survey.md`

**Paper selection gate (Step 1):** Optional — only invoke for noisy corpora (cite-traverse,
lit-review). Skip for ASTA survey runs: ASTA papers are pre-curated and the extraction
subagent handles relevance filtering internally.

---

## Run parameters

```
PARAMS:
  node_id:         ""   # required — evidencell node ID
  summaries_file:  ""   # required — path to all_summaries.json
  output_dir:      ""   # required — for manifest and exclusion log
  model:           "opus"   # judgement-heavy; use thinking model
```

---

## Step 0: Build node context

1. Locate the KB file for this node:
   ```
   uv run python -c "from evidencell.paths import find_node_file; print(find_node_file('{node_id}'))"
   ```
   Store the result as `KB_FILE`.

2. Read `KB_FILE`. Extract for `{node_id}`:
   - `name`
   - `definition_basis`
   - `defining_markers` (gene symbols)
   - `anatomical_location` (labels)
   - `nt_type.name_in_source`
   - All `ref` values already present in any `PropertySource` list on this node
     (to avoid duplicating evidence already in the KB)

3. Locate `paper_catalogue.json`: check the same directory as `{summaries_file}`.
   If present, read it — it provides paper metadata (title, year, authors, PMID, DOI)
   used when writing new entries to `references.json`.

4. Locate `references.json` for this node's region:
   ```
   uv run python -c "
   from evidencell.paths import find_node_file, refs_path_for_graph
   print(refs_path_for_graph(find_node_file('{node_id}')))
   "
   ```
   Store as `REFS_FILE`.

Build `NODE_CONTEXT`:
```
Node:            {name} ({node_id})
Definition:      {definition_basis}
Markers:         {symbols or "none recorded"}
Location:        {locations or "none recorded"}
NT type:         {nt_type or "unknown"}
Existing refs:   {list of ref values already on this node, or "none"}
```

---

## Step 1: [GATE] Paper selection — optional

**Skip this step for ASTA survey runs.** Proceed directly to Step 2 and pass
`excluded_ids: "none"` to the extraction subagent.

**Invoke this step for cite-traverse or lit-review runs** where corpus quality
varies and papers from noisy citation graphs or disease/non-model-organism
contexts may need human weeding.

When invoked:

1. Read `{summaries_file}`. For each entry, auto-detect these signals from the
   `summary` and `quotes` fields:
   - `NON_MODEL_SPECIES` — human, primate, or non-rodent species explicitly mentioned
   - `EARLY_STAGE` — embryonic, prenatal, P0–P14, neonatal
   - `DISEASE_MODEL` — epilepsy, seizure, knockout, transgenic disease model
   - `IN_VITRO` — dissociated culture (not acute slice)
   - `REVIEW_ONLY` — quote is clearly contextual/introductory, not a primary finding

2. Present to user, grouped by `node_relevance`:

   ```
   PAPER SELECTION — {node_id}
   ============================
   Summaries file: {summaries_file}

   HIGH relevance ({N}):
     [CorpusId:X] Author et al. (Year) — "Title"
       Signals: NON_MODEL_SPECIES — "mentions human tissue in methods"
     [CorpusId:Y] Author et al. (Year) — "Title"
       Signals: none

   MODERATE relevance ({N}):
     ...

   LOW relevance ({N}):
     ...

   Refs already in KB (will be skipped): {existing refs list}
   ```

3. Ask: "Exclude any papers? Provide CorpusIds, or 'none' to include all."

4. Write `{output_dir}/excluded_{node_id}.json`:
   ```json
   { "node_id": "{node_id}", "excluded_corpus_ids": [...] }
   ```
   Write an empty list if the user excludes nothing.

LOW relevance summaries are included unless explicitly excluded — the extraction
subagent makes the final relevance call per field.

---

## Step 2: Extraction subagent

Spawn a **single extraction subagent** with this exact prompt. Fill in all
variables before spawning.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {model}`

```
You are an evidence extraction agent. For each included literature summary you:
(1) decide whether it contains evidence for the target node,
(2) write the chosen quote to references.json,
(3) write a PropertySource entry with quote_key to the KB YAML.
You perform ONLY the steps below.

NODE ID:              {node_id}
NODE CONTEXT:         {node_context}
KB FILE:              {kb_file}
REFS FILE:            {refs_file}
SUMMARIES FILE:       {summaries_file}
EXCLUDED CORPUS IDS:  {excluded_ids}   (comma-separated, or "none")
PAPER CATALOGUE:      {paper_catalogue_path}   (path, or "none" if absent)
ADDED_BY:             evidence_extraction_{node_id}_{date}

## KB fields that accept PropertySource lists

  anatomical_location[].sources → per-location evidence (nested on each AnatomicalLocation entry)
  electrophysiology.sources     → electrophysiology claims (nested on ElectrophysiologyProfile)
  morphology.sources            → morphology claims (nested on MorphologyProfile)
  nt_type.sources               → neurotransmitter type claims
  synonyms[N].sources           → synonym usage evidence (for a specific synonym entry)

For marker claims, use MarkerSource (extends PropertySource):
  GeneDescriptor.sources → add a MarkerSource entry on the specific gene
  marker_type: PROTEIN   → IHC, immunofluorescence, Western blot
  marker_type: TRANSCRIPT → scRNA-seq, smFISH, ISH, qPCR

PropertySource fields:
  ref:       required — "PMID:xxxxxxxx" or "https://doi.org/..."
             Resolve from paper_catalogue.json externalIds (PubMed → PMID,
             DOI field). Fallback: "CorpusId:{source_corpus_id}".
  method:    how the property was detected (free text)
             e.g. "IHC (somatostatin antibody)", "patch-clamp (acute slice)",
             "scRNA-seq (Gad2 expression)", "biocytin fill + confocal"
  scope:     species, age, preparation
             e.g. "adult mouse CA1", "P21 rat hippocampus, acute slice"
  quote_key: content-hashed key into references.json (set in step 3 below)

## Task

1. Read {summaries_file}.

2. For each entry, skip if:
   - source_corpus_id is in EXCLUDED CORPUS IDS
   - ref (PMID/DOI resolved from source_corpus_id) already in NODE CONTEXT
     "Existing refs" list

3. For each remaining entry (process HIGH node_relevance first, then MODERATE,
   then LOW):

   a. Decide if this summary contains evidence for {node_id} specifically.
      Consider NODE CONTEXT markers, location, and NT type. If node_relevance
      is LOW and neither the node's name, markers, nor location are mentioned
      in the summary or quotes — skip. Record skipped entries in the manifest.

   b. Identify the single KB field this summary most directly supports.
      Choose one: anatomical_location[].sources / electrophysiology.sources /
      morphology.sources / nt_type.sources / synonyms[N].sources /
      GeneDescriptor.sources.
      If the summary supports multiple fields, choose the field where the
      evidence is strongest. Do not split one quote across multiple fields.

   c. Select the single most informative verbatim quote from the entry's
      `quotes` list. The quote MUST be an exact substring of one of those
      strings — do not paraphrase, truncate mid-sentence, or merge quotes.

   d. Write the quote to references.json:
      ```
      uv run python -c "
      from evidencell.references import write_quote_to_refs
      from pathlib import Path
      import json

      meta = {}
      catalogue = '{paper_catalogue_path}'
      if catalogue != 'none':
          cat = json.load(open(catalogue))
          papers = cat if isinstance(cat, list) else cat.get('result', [])
          for p in papers:
              ext = p.get('externalIds', {})
              if str(ext.get('CorpusId', '')) == '{source_corpus_id}':
                  meta = p
                  break

      key = write_quote_to_refs(
          refs_path=Path('{refs_file}'),
          corpus_id='{source_corpus_id}',
          quote_text='''{quote_text}''',
          section='{section}',
          source_method='{source_method}',
          added_by='{added_by}',
          paper_meta=meta,
      )
      print(key)
      "
      ```
      Store the printed key as `QUOTE_KEY`.

   e. Resolve `ref`:
      - If paper_catalogue exists: find the entry for source_corpus_id,
        use externalIds.PubMed → "PMID:{id}" or DOI → "https://doi.org/{doi}"
      - Fallback: "CorpusId:{source_corpus_id}"

   f. Build the PropertySource / MarkerSource entry:
      ```yaml
      ref: "PMID:xxxxxxxx"
      method: "patch-clamp (acute slice)"
      scope: "adult mouse CA1"
      quote_key: "{QUOTE_KEY}"
      ```

   g. Edit {kb_file} to append this entry to the correct field list on node
      {node_id}. Edit only the relevant list — do NOT rewrite the entire file.
      The pre-edit validation hook fires automatically. If it rejects:
      - Read the error carefully
      - The most likely cause is quote_key not found in references.json —
        verify the write_quote_to_refs call succeeded
      - Fix the issue and retry the edit. Do not silently skip failed items.

4. Write {output_dir}/extraction_manifest_{node_id}.json:
   ```json
   {
     "node_id": "{node_id}",
     "summaries_read": N,
     "skipped_excluded": N,
     "skipped_duplicate_ref": N,
     "skipped_low_relevance": N,
     "entries_written": N,
     "fields_populated": ["anatomical_location.sources", "morphology.sources"],
     "fields_with_no_evidence": ["electrophysiology.sources", "nt_type.sources"],
     "synonyms_found": ["OLM", "O-LM interneuron"],
     "refs_file": "{refs_file}"
   }
   ```

RETURN:
"Extracted {N} PropertySource entries for {node_id}.
Fields: {list}. Gaps: {list}. Synonyms found: {list or 'none'}."

DO NOT:
- Paraphrase or shorten quotes — exact substring of all_summaries.json quotes field
- Write more than one PropertySource entry per summary entry
- Write PropertySource without a quote_key (inline snippet is not acceptable)
- Write EvidenceItem or LiteratureEvidence shapes to nodes — only PropertySource / MarkerSource
- Rewrite the entire KB YAML — only append to specific field lists
- Skip hook failures silently — fix and retry
```

---

## After extraction

1. Read `{output_dir}/extraction_manifest_{node_id}.json`.
2. Print summary:
   ```
   EXTRACTION COMPLETE
   ===================
   Node:     {node_id}
   Written:  {N} PropertySource entries → {kb_file}
   Refs:     {N} quotes added → {refs_file}
   Fields:   {populated list}
   Gaps:     {no-evidence list}
   Synonyms: {synonyms_found or "none"}

   Next: run evidence-extraction for other nodes, or
         run just gen-report {region} to review KB state.
   ```
3. If `synonyms_found` is non-empty, ask:
   "Add these as TypeSynonym entries on {node_id}? (yes/no)"
   If yes, spawn a subagent to write TypeSynonym entries to the node
   (one per synonym, with a PropertySource using the quote_key that first
   introduced the synonym).

---

## Rules

- **quote_key always.** Write the quote to references.json first, get the key,
  then write PropertySource.quote_key. Never use inline snippet.
- **find_node_file() for all KB access.** Never hardcode KB file paths.
- **No intermediate evidence files.** Evidence writes directly to KB YAML.
- **One gate only.** Paper selection (Step 1) is the only human checkpoint.
  The pre-edit hook is the structural validation gate.
- **One PropertySource per summary.** Choose the strongest field — do not split.
- **Exact verbatim quotes only.** Must be exact substrings of all_summaries.json
  `quotes` field entries. No paraphrase, no truncation mid-sentence.
- **Subagent prompts are contracts.** Pass verbatim with variables filled in.
- **Data flows through files, not context.**
