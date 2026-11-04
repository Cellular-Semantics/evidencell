# ASTA Report Ingest Orchestrator

You are an ASTA deep research report ingestion coordinator. You parse a pre-generated
ASTA AI2 deep research PDF, propose classical CellTypeNode stubs with property metadata,
and resolve all references. Quotes are stored in a shared per-region reference store
with content-hashed keys — they are **not** promoted to KB evidence items. Each proposed
node is written as its own file under `kb/graphs/{region}/`, matching the
one-component-per-file layout the KB uses.

Entry point: user asks Claude to run `just ingest-report {region} {pdf_file}`.
Claude runs the recipe (validates inputs, shows existing nodes), then reads and
follows this orchestrator.

Classical cell type nodes **emerge from this workflow** — they are not required to
exist beforehand. The PDF is the discovery mechanism for the classical side;
`ingest-taxonomy.md` handles the transcriptomic atlas side.

---

## Run parameters

```
PARAMS:
  region: ""             # required — brain region slug (e.g. "hippocampus")
  pdf_file: ""           # required — path from repo root (inputs/deepsearch/...)
  model: "sonnet"        # mechanical subagents
  thinking_model: "opus" # parsing + KB proposal subagent
  gate: false            # optional — pause for sign-off before writing nodes
```

**Branch handling is the operator's.** This orchestrator writes files; it does
not create branches, commit, or open pull requests. Whether the run happens on
a branch and whether review is a PR is the runner's call — see
"Review" below for the recommended default.

Output directory: `research/{region}/{YYYYMMDD}_{region}_report_ingest/`

---

## Data flow overview

```
PDF
 ├─ Step 1:   parse → extracted_quotes.json  (temp, keyed by author_key)
 │                   → reference_list.json    (author_keys + titles)
 │                   → pdf_corpus_ids.json    (S2 corpus IDs from PDF links)
 │
 ├─ Step 1b:  LLM read → proposed_types.json  (proposed node summaries)
 │
 ├─ Step 2:   batch resolve + merge quotes
 │            → references/{region}/  (shared, keyed by corpus_id)
 │               quotes stored with content-hashed keys: {corpus_id}_{hash8}
 │
 ├─ Step 3:   CL lookup → cl_mappings.json
 │
 ├─ Step 3b:  quote → property matching, one file per node
 │            → kb/graphs/{region}/{node_id}.yaml
 │
 ├─ Step 4:   review (PR by default; in-session gate if gate: true)
 │
 └─ Step 5:   handoff to survey
```

Quotes live in the region's reference store, never in the KB YAML. The KB references
quotes by key. Reports dereference keys to include snippets when needed.

---

## The reference store — shared, per region

`references/{region}/` is the single source of truth for all
references and their associated quotes in a region. Multiple workflows
(asta-report-ingest, cite-traverse, evidence-extraction) read and append to it.

**Structure:**

```json
{
  "_meta": {
    "region": "hippocampus",
    "last_updated": "2026-03-24T...",
    "last_updated_by": "20260324_hippocampus_report_ingest"
  },
  "12345678": {
    "corpus_id": "12345678",
    "pmid": "10862698",
    "doi": "10.1523/JNEUROSCI.20-04-01386.2000",
    "title": "Differential Expression of Group I Metabotropic...",
    "authors": "van Hooft et al.",
    "year": 2000,
    "author_keys": ["Hooft et al., 2000"],
    "quotes": {
      "12345678_a3f2c1d0": {
        "text": "Type I interneurons are located at the oriens-alveus border...",
        "section": "Anatomical Location and Morphology",
        "claims": ["soma_location_so", "sst_positive"],
        "source_method": "asta_report",
        "status": "pending",
        "added_by": "20260324_hippocampus_report_ingest"
      },
      "12345678_b7e4f912": {
        "text": "...",
        "source_method": "primary",
        "status": "verified",
        "added_by": "20260325_hippocampus_cite_traverse"
      }
    }
  }
}
```

**Quote key scheme:** `{corpus_id}_{sha256(normalised text)[:8]}`, where
normalisation is lowercase plus whitespace collapse.

Never reimplement this. `write_quote_to_refs()` derives the key for you, and
`references.compute_quote_key()` is the single definition if you need it
directly. The pre-edit hook recomputes the hash on every write and rejects a
key that does not match its own text, so a hand-computed key that drifts from
the canonical implementation is a blocked write, not a silent inconsistency.

- Deterministic: same quote from two ASTA reports → same key, deduped
- New quotes append: cite-traverse adds a quote, gets a new hash
- Slightly different extractions (whitespace, trailing period) → normalization handles it
- ASTA paraphrase vs actual paper text → different hashes, both kept

**Quote status values:**

| Status | Meaning |
|--------|---------|
| `pending` | Extracted from ASTA report, not yet verified against primary text |
| `verified` | Confirmed verbatim against primary source by cite-traverse |
| `superseded` | An ASTA quote that was found to be paraphrased; a `verified` quote exists |
| `primary` | Quote extracted directly from primary literature (not via ASTA) |

**Merge protocol:** when appending to an existing store:
1. Read existing file (or start with empty `{}` if first ingest for this region)
2. For each new reference: if corpus_id already exists, merge quotes (dedup by key)
3. For new references: add full entry
4. Update `_meta.last_updated` and `_meta.last_updated_by`
5. Write back atomically

---

## ASTA report format (reference)

ASTA deep research PDFs follow a consistent structure:
- **Section headers** (e.g. "Anatomical Location and Morphology")
- **Italic synthesis paragraph** at top of each section (ASTA-generated; labelled
  "(N sources)" or "(LLM Memory)" or "(Model-Generated)")
- **Regular synthesis paragraphs** with inline `(Author et al., Year)` hyperlink citations
- **"Evidence" subsection** listing papers, each formatted as:
  ```
  (Author et al., Year)
  Paper title as hyperlink
  "Verbatim quote from the paper..."
  "Another verbatim quote..."
  ```
- **Reference list** at end of document
- **Hyperlinked citations** — every `(Author et al., Year)` citation in the PDF is a
  hyperlink to `https://www.semanticscholar.org/p/{corpus_id}`. These embedded corpus
  IDs are the primary mechanism for reference resolution (see Step 1b).

Key extraction rule: **verbatim quotes are delimited by `"..."` quotation marks** and
appear as standalone blocks under a paper attribution — NOT inline within synthesis
sentences. Inline quoted fragments in synthesis text are ASTA paraphrase, not verbatim.

---

## Step 0: Setup

1. Confirm `{pdf_file}` exists at the given path (relative to repo root).
2. Create output directory:
   ```bash
   mkdir -p research/{region}/{YYYYMMDD}_{region}_report_ingest
   ```
3. Write `{output_dir}/run_config.json`:
   ```json
   {
     "region": "...",
     "pdf_file": "...",
     "model": "sonnet",
     "thinking_model": "opus",
     "started_at": "..."
   }
   ```

---

## Step 1: Deterministic PDF extraction

Run the pymupdf-based parser to extract quotes, references, and corpus IDs.
This is fast (seconds), deterministic, and avoids content-filter issues.

```bash
uv run python -m evidencell.extract_asta_report {pdf_file} \
    --output-dir {output_dir}
```

This writes three files:
- `{output_dir}/extracted_quotes.json` — all verbatim quotes keyed by author_key
- `{output_dir}/reference_list.json` — author_key, title, year for each paper
- `{output_dir}/pdf_corpus_ids.json` — Semantic Scholar corpus IDs from hyperlinks

**Quality check:** Verify the output line reports reasonable numbers. If
`total_quotes == 0` or `total_papers < 3`, the PDF layout may differ from the
expected ASTA format. In that case, **fall back** to the LLM subagent approach:
read the PDF with the Read tool and extract quotes manually. The expected
output file format is identical — downstream steps are agnostic to the method.

**Note:** The parser handles only mechanical extraction (quotes, refs, links).
It does NOT identify proposed classical cell types — that requires LLM judgement
and is handled in Step 1b below.

---

## Step 1b: Proposed types identification (LLM subagent)

Spawn a **single subagent** that reads the PDF and the already-extracted quotes
to identify the classical cell types the report describes.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {thinking_model}`

```
You are a cell type identification agent. Read an ASTA deep research PDF and
identify the classical cell types it describes. You have access to the
already-extracted quotes in {output_dir}/extracted_quotes.json for reference.
You perform ONLY the steps listed below.

PDF FILE: {pdf_file}
OUTPUT DIRECTORY: {output_dir}
REGION: {region}

TASK:

1. Read the PDF at {pdf_file}. Focus on the overall taxonomy framing:
   - What cell type(s) does the report treat as its subject?
   - Are there subtypes or heterogeneity discussed?

2. Read {output_dir}/extracted_quotes.json for context on what evidence exists.

3. For each proposed classical cell type, note:
   - A proposed_id (snake_case, region-scoped)
   - The full name
   - Markers mentioned (positive, negative, neuropeptides)
   - Anatomy, NT type
   - Morphology and ephys summaries (concise, from synthesis context)
   - Subtypes or heterogeneity noted
   - Quote count (from extracted_quotes.json)

4. Write {output_dir}/proposed_types.json:
   [{
     "proposed_id": "olm_ca1",
     "name": "Oriens-Lacunosum Moleculare (O-LM) interneuron",
     "markers_mentioned": ["Sst", "Chrna2", "Npy"],
     "negative_markers_mentioned": [],
     "neuropeptides_mentioned": ["Sst", "Npy", "Pnoc"],
     "anatomy_mentioned": ["CA1 stratum oriens"],
     "nt_type": "GABAergic",
     "morphology_summary": "Horizontal soma in SO, spiny dendrites in SO, axon to SLM",
     "ephys_summary": "Regular-to-fast spiking, prominent Ih sag, theta resonance",
     "subtypes_noted": "SST+ vs PV+ subpopulation (Fernández et al., 2024)",
     "quote_count": N
   }]

RETURN:
"Proposed {Q} classical type(s). Written proposed_types.json."

DO NOT:
- Re-extract quotes (already done in Step 1)
- Write a KB YAML file (that happens in Step 3b)
- Call any MCP search tools
```

---

## Step 2: Reference resolution and quote store merge

Resolve author_key references using the corpus IDs extracted in Step 1b,
then merge extracted quotes into the shared reference store with
content-hashed keys.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {model}`

```
You are a reference resolution agent. Resolve author_key references to real
corpus IDs, then merge quotes into the shared reference store.
You perform ONLY the steps listed below.

OUTPUT DIRECTORY: {output_dir}
REGION: {region}
REFERENCE STORE: references/{region}/

TASK:

1. Read {output_dir}/pdf_corpus_ids.json (Semantic Scholar corpus IDs from
   PDF hyperlinks), {output_dir}/reference_list.json, and
   {output_dir}/extracted_quotes.json.

2. Batch-resolve all corpus IDs in a single call:
   mcp__Asta_semanticscholar__get_paper_batch(
       ids=["{corpus_id}", ...],
       fields="title,authors,year,externalIds"
   )
   This returns title, authors, year, PMID, and DOI for every paper.

3. Match each batch result to an author_key in reference_list.json:
   - Match on year + first author surname.
   - Set resolution_confidence: HIGH for matches.
   - Any corpus IDs that don't match an author_key: note as "extra_references"
     (these are inline citations in synthesis text, not evidence-section papers).

4. For any author_keys still unmatched after the batch (should be rare):
   a. Search ASTA by title fragment + author:
      mcp__Asta_semanticscholar__search_papers_by_relevance(
          keyword="{title_fragment} {author_key}",
          fields="title,authors,year,externalIds",
          limit=3
      )
      Set resolution_confidence: MODERATE if matched.

   b. If still unresolved, mark resolution_confidence: UNRESOLVED.
      Do not guess.

5. Merge into the region's reference store:

   **Do not read, hand-merge, or write the store directly.** It is split into
   write-once `papers/{corpus_id}.json` and append-only
   `quotes/{corpus_id}.json`, and the pre-edit hook rejects writes that drop a
   paper, drop a quote, edit a paper's identity, or carry a quote key that is
   not the hash of its own text. Go through `write_quote_to_refs()`, which
   derives the key, is idempotent, and routes to the right files:

   ```python
   from pathlib import Path
   from evidencell.references import write_quote_to_refs

   quote_key = write_quote_to_refs(
       Path("references/{region}"),
       corpus_id="<digits-only>",
       quote_text="<exact verbatim quote>",
       section="Anatomical Location and Morphology",
       source_method="ASTA_REPORT",      # SourceMethod enum, not free text
       added_by="{run_id}",
       paper_meta=meta,                  # used only when the paper is new
   )
   ```

   Call it once per quote. Re-adding an identical quote is a no-op and returns
   the same key, so reruns are safe. Never compute a quote key by hand — it is
   `{corpus_id}_{sha256(normalised text)[:8]}` and the hook recomputes it; a
   key that does not match its text is rejected.

   a. `paper_meta` field shape — this is what becomes the `papers/` record:
       {
         "corpus_id": "<digits-only>",
         "author_keys": ["Last et al., YYYY"],          // list[str]
         "title": "<paper title>",
         "year": <int>,
         "authors": ["First Author", "Second Author"],   // list[str], full
                                                         // names. NOT a single
                                                         // comma-joined string;
                                                         // NOT 'et al.' suffix
                                                         // appended.
         "pmid": "<digits-only>",                        // NO 'PMID:' prefix
         "doi": "<bare path, e.g. 10.1111/ejn.14606>",   // NO 'DOI:' prefix,
                                                         // NO 'https://' URL
         "resolution_confidence": "HIGH" | "MODERATE" | "UNRESOLVED"
       }
       Semantic Scholar `get_paper_batch` returns authors as
       `[{"authorId": "...", "name": "..."}, ...]`. Extract `name` from each
       dict; do not flatten to a string. Three prior pilots have shipped
       wrong field shapes here (see
       planning/asta_ingest_lessons_sexually_dimorphic.md §1–2 and
       planning/minirefs_author_rendering_fix.md) — every one was caught
       only after KB writes started failing.

       Identity is write-once. If the paper already exists, `paper_meta` is
       ignored rather than overwriting it; correcting a stored identity is a
       deliberate, reviewed change, not a side effect of adding a quote.

   b. Resolve corpus IDs with `just fetch-reference CorpusId:NNN` rather than
      reading a catalogue by hand. It resolves offline-first and reports an
      unresolvable ID instead of guessing. A PMID typed from memory is how a
      bacteriophage genomics paper came to sit on a hippocampal interneuron
      node for six months.

6. Write {output_dir}/resolution_report.md — summary:
   - Total references, HIGH/MODERATE/UNRESOLVED counts
   - Quotes merged: N new, M deduplicated
   - Any extra_references (inline citations without evidence-section quotes)

RETURN:
"Resolved {N}/{total} references. HIGH: X, MODERATE: Y, UNRESOLVED: Z.
Merged {Q} quotes into the reference store ({D} deduplicated).
See resolution_report.md."

DO NOT:
- Guess corpus IDs
- Skip the batch step and go straight to search
- Run more than 2 search attempts per fallback reference
- Overwrite existing quotes in the reference store (append only)
```

---

## Step 3: CL lookup subagent

Spawn a **single subagent** to anchor proposed nodes to Cell Ontology terms.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {model}`

```
You are a Cell Ontology lookup agent. Match proposed classical cell types to
existing CL terms and collect CL definition references as additional seed papers.

OUTPUT DIRECTORY: {output_dir}
REGION: {region}

TASK:

1. Read {output_dir}/proposed_types.json for the list of proposed classical types.

2. For each proposed type, search OLS4 by name and synonyms:
   mcp__ols4__search(query="{type_name}", ontology="cl", rows=5)
   Also try key synonym searches if the primary name returns no match
   (e.g. "O-LM neuron", "oriens lacunosum moleculare", "OLM interneuron").

3. For each match found:
   - Record: cl_term_id, label, mapping_type (EXACT/BROAD/RELATED)
   - Fetch the term detail to get definition references:
     mcp__ols4__get_term(iri="{term_iri}")
   - Extract any PMID or DOI references from the definition or xrefs.

4. Write {output_dir}/cl_mappings.json:
   {
     "olm_ca1": {
       "cl_term_id": "CL:0000000",
       "label": "oriens-lacunosum moleculare neuron",
       "mapping_type": "EXACT",
       "mapping_confidence": "HIGH",
       "definition_references": ["PMID:10000001", "PMID:10000002"]
     },
     "no_match_node": {
       "cl_term_id": null,
       "mapping_type": null,
       "mapping_confidence": "CANDIDATE",
       "definition_references": [],
       "note": "No CL term found — potential CL contribution"
     }
   }

RETURN:
"CL lookup complete. Matched: N nodes. Unmatched (CANDIDATE): M nodes.
CL definition references: P additional seed papers. See cl_mappings.json."

DO NOT:
- Auto-assign EXACT mapping if only a synonym matches — use BROAD or RELATED
- Invent CL term IDs
```

---
## Step 3b: Quote matching and node authoring

Spawn a **single subagent** that matches quotes from the reference store to node
property fields and writes **one KB file per proposed node**, directly into
`kb/graphs/{region}/`.

This is the key filtering step: quotes are evaluated for relevance to specific
properties, not dumped in bulk.

**Why direct writes.** The pre-edit validation hook is a PreToolUse hook on
`Write`/`Edit`. A draft written to `research/` is not covered by it, so the
former flow was *write unvalidated → review → validate on promotion*, and the
promotion step was a `cp` away from writing wholly unvalidated YAML into the KB
(that is how an unresolvable `taxonomy_id` once reached 44 nodes across six
files). Writing each node straight to its destination inverts the order: the
hook fires on every write, and a malformed node fails at the point of
authorship, where the subagent still has the context to fix it.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {thinking_model}`

```
You are a quote matching and node authoring agent. You match quotes from the
shared reference store to node property fields and write one KB file per node.
You perform ONLY the steps listed below.

OUTPUT DIRECTORY: {output_dir}
REGION: {region}

INPUT FILES:
- {output_dir}/proposed_types.json                (node summaries from Step 1b)
- references/{region}/                            (shared quote store)
- {output_dir}/cl_mappings.json                   (CL term matches)

PROPERTY CATEGORIES:
Quotes can validate these node property fields:
- morphology (description + sources)
- electrophysiology (description + sources)
- defining_markers (positive markers)
- negative_markers
- neuropeptides
- nt_type
- anatomical_location (with nested sources per location entry)
- colocated_types

## Part A: Match quotes to properties

1. Read all input files.

2. For each proposed node in proposed_types.json, scan quotes in the reference
   store for claims about specific properties. For each quote, decide:
   a. Which property category it addresses (a quote may address several).
   b. Whether it is relevant enough to cite for that property. Keep quotes that
      characterise this specific cell type or its immediate broader class;
      discard tangential mentions and generic statements.

3. For each kept quote, update its "claims" list with the property categories
   it addresses (e.g. ["soma_location_so", "sst_positive"]). Quotes live in
   `references/{region}/quotes/{corpus_id}.json`, keyed by quote_key.

   Editing `claims` on an existing quote is allowed — it is curation metadata,
   not provenance. Do not touch `text`: the quote key is a hash of it, so any
   edit invalidates the key and the write is rejected. If the recorded text is
   genuinely wrong, add the correct quote as a new entry rather than editing
   the existing one.

4. For each property category on each node, select the best supporting
   references and their quote keys:
   - Pick the 1-3 most informative quote_keys per property
   - Prefer: direct characterisation > review > tangential mention
   - Prefer: resolved references (with PMID/DOI) > UNRESOLVED

## Part B: Write one file per node

5. For each proposed node, write `kb/graphs/{region}/{node_id}.yaml` with the
   **Write** tool. One node per file — this is the KB's one-component-per-file
   layout, and it is what makes each node independently reviewable in a diff.

   `{node_id}` is the node's `id`. Filename and id must match.

   Each file is a `CellTypeMappingGraph` containing exactly one CellTypeNode
   and no edges:
   - id, name, definition_basis
   - species: null (to be confirmed from primary literature)
   - anatomical_location: from synthesis context if unambiguous
   - nt_type.name_in_source — always attempt to resolve NT type, inferring from
     well-established facts where the report does not state it (BNST CRF
     neurons are GABAergic, for example). If it is genuinely unresolvable, say
     so in `notes`: find-candidates scores on NT type, and a silently missing
     value weakens candidate retrieval with no signal to the mapper.
   - defining_markers: symbol only; ncbi_gene_id: null
   - negative_markers, neuropeptides: as identified
   - morphology: {description: "...", sources: [...]}
   - electrophysiology: {description: "...", sources: [...]}
   - anatomical_location: [{..., sources: [...]}]  (sources nested per location)
   - cl_mapping: from cl_mappings.json (if matched)
   - definition_references: the top 3-5 most informative resolved refs
   - is_terminal: false
   - notes: caveats worth carrying — contradictions between sources,
     species-dependent claims, suspected heterogeneity that may warrant
     splitting the node later, or a provisional MBA term where no child term
     exists for the subnucleus.

   Edges: leave empty — mapping relationships require primary literature.

   For nested sources entries, use this pattern:
   ```yaml
   morphology:
     description: "Large soma with horizontal dendrites in stratum oriens..."
     sources:
       - ref: "PMID:20421280"
         method: "biocytin fill"
         scope: "adult rat CA1"
         quote_key: "12345678_a3f2c1d0"  # → lookup in the reference store
   ```

   Do NOT inline quote text in the KB YAML. Use quote_keys only.

   Header comment block:
   ```yaml
   # {node_name} — {region}
   # Source: ASTA deep research report — {pdf_file}
   # Ingestion date: {date}
   # Status: DRAFT — node metadata from ASTA report, pending primary verification
   # Property assertions reference quotes in references/{region}/
   # Proposed by: asta-report-ingest
   ```

6. If the pre-edit hook blocks a write, fix the reported problem and retry.
   Never work around a block by writing through a shell command — `cp`, `cat >`
   and `sed -i` are not intercepted by the hook, and a write that bypasses it
   is unvalidated KB content.

RETURN:
"Wrote {N} node file(s) to kb/graphs/{region}/: {filenames}.
Properties cited: {P}. Quotes used: {Q}.
Nodes with no quote support for any property: {G}."

DO NOT:
- Put quote text in the KB YAML (use quote_keys only)
- Invent property values not supported by quotes or synthesis context
- Write more than one node per file
- Write a combined/draft KB file anywhere
```

---

## Step 4: Review

Two paths. The default is a pull request; `gate: true` adds an in-session
sign-off before the run finishes.

### Default — review as a pull request

The node files are already written and hook-validated. Summarise the run and
hand review to the operator:

```
Wrote {N} node(s) to kb/graphs/{region}/:
  {node_id}.yaml — {name} — CL: {term or "none"} — {P} properties cited
  ...

References: {R} papers, {Q} quotes ({U} UNRESOLVED)
Run artifacts: {output_dir}/

Review these as a diff. Each node is its own file, so a node you do not want
is a file you delete.
```

Then run the structural check and show the result:

```bash
just validate-all
```

Branch, commit and PR are the operator's to run. A PR gives line-level comment
on each node, and CI runs the same validation on every push.

**Reviewer note:** KB YAML carries `quote_key` values, not quote text. To read
the evidence behind an assertion, dereference the key against
`references/{region}/quotes/{corpus_id}.json`.

### `gate: true` — in-session sign-off

Use when a reviewer should sign off on new KB content before the session ends.

1. Show the same summary as above.
2. Show per-node detail — name, CL mapping, properties cited, and any node
   with no quote support.
3. Ask:
   > "Wrote {N} node(s): {names}. CL mapped: {X}. {U} references UNRESOLVED.
   >
   > Review the files in kb/graphs/{region}/. Edit directly if needed
   > (correct names, adjust markers, add refs), or tell me which nodes to
   > delete."
4. Apply any requested deletions or edits, then re-run `just validate-all`.

The gate changes *when* a human looks, not *what* was written — the files and
their validation are identical either way.

---

## Step 5: Handoff

```
INGEST COMPLETE
===============
Region: {region}
Nodes written: {N} files in kb/graphs/{region}/
References: references/{region}/ ({R} papers, {Q} quotes)
Run artifacts: {output_dir}/

NEXT STEP — primary literature retrieval:
  Hand workflows/survey.md to Claude Code with:
    region: {region}
    corpus_ids_file: {output_dir}/pdf_corpus_ids.json
    output_dir: research/{region}/survey_{date}/

  Then workflows/evidence-extraction.md per node, which writes
  PropertySource entries with quote_key into the node files.

Taxonomy ingestion (workflows/ingest-taxonomy.md) is independent and can run
concurrently in a separate session.
```

---
## Rules

- **Classical nodes emerge here.** Do not require pre-existing KB nodes.
- **One node per file.** `kb/graphs/{region}/{node_id}.yaml`, filename matching
  the node id. Never write a combined draft.
- **Write with the Write tool, always.** The pre-edit hook is a PreToolUse hook
  on `Write`/`Edit`; `cp`, `cat >` and `sed -i` bypass it silently. A write
  that bypasses the hook is unvalidated KB content.
- **Quotes live in the reference store.** Content-hashed keys
  (`{corpus_id}_{hash8}`) ensure dedup across ingests. The KB YAML references
  quotes by key only — never inline text.
- **The reference store is shared.** Multiple workflows append to it per
  region. Go through `write_quote_to_refs()`; never hand-merge.
- **No evidence items at ingest.** Nodes carry property fields with `sources`
  entries pointing at quote_keys. `LiteratureEvidence` items are created by
  `evidence-extraction` after primary verification.
- **Nodes are DRAFT until verified.** Property assertions come from ASTA report
  quotes, which are paraphrase until `survey` / `evidence-extraction` confirms
  them against primary text. Say so in the node header comment.
- **The gate is optional; the validation is not.** `gate: true` changes when a
  human looks, not what was written. Every node passes the hook on write and
  `just validate-all` before the run reports complete.
- **Branches and PRs belong to the operator.** This orchestrator writes files
  and stops.
- **Subagent prompts are contracts.** Pass verbatim with variables filled in.

## Known gap: cross-report node identity

Step 1b mints `proposed_id` from the PDF in isolation and is never shown the
existing KB, so two reports describing the same cell type will propose two
nodes under different ids. The only existing-node signal is the id list printed
by `just ingest-report`, before this orchestrator is read.

Until index-backed reconciliation lands (#163 "Not in scope", depends on the
KB index), **review is the net**: check proposed ids against the list the
recipe printed, and against `kb/graphs/{region}/` filenames, before accepting.
See #116 for what this has already cost — 7 stranded ingest stubs in
hippocampus, 4 duplicating a mapping node under a different id.
