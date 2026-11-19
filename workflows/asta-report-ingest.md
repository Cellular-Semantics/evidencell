# ASTA Report Ingest Orchestrator

You are an ASTA deep research report ingestion coordinator. You parse a pre-generated
ASTA AI2 deep research PDF, resolve its references into the shared per-region reference
store, identify the cell types it describes, reconcile each one against the nodes
already in the KB, and write or enrich one node file per type under
`kb/graphs/{region}/`. Quotes are stored with content-hashed keys and cited by key —
they are **not** promoted to KB evidence items.

Entry point: user asks Claude to run `just ingest-report {region} {pdf_file}`.
Claude runs the recipe (validates inputs, lists the region's existing nodes), then
reads and follows this orchestrator.

A report may describe types that are new to the KB, types that already have a node,
or subtypes of existing nodes. The workflow decides which before it writes anything,
and adds to existing nodes rather than rewriting them. `ingest-taxonomy.md` handles
the transcriptomic atlas side.

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

## Tools and skills

Subagents get these by name in their prompts. Which tool to use is decided
here and in the skills, never in the schema.

| Need | Use |
|---|---|
| Field meanings, shapes, allowed values, fill order | `{output_dir}/schema_subset.yaml` (Step 0, `just schema-subset`) |
| The node's Cell Ontology anchor (`cl_mapping`) | `.claude/skills/cl-mapping.md` |
| Any other ontology term: species, anatomy, transmitter CL terms | `.claude/skills/term-grounding.md` |
| Paper metadata for corpus IDs | `mcp__Asta_semanticscholar__get_paper_batch`, `just fetch-reference` |
| Adding quotes to the reference store | `evidencell.references.write_quote_to_refs()` |
| The region's existing nodes | `uv run python -m evidencell.kb_index region {region}` |
| Checking written files | the pre-edit hook (automatic), `just validate-terms-file`, `just validate-all` |

---

## Data flow overview

```
PDF
 ├─ Step 0:  setup → existing_nodes.yaml   (region's canonical nodes, from the KB index)
 │                 → schema_subset.yaml     (the schema needed to write a node file)
 │
 ├─ Step 1:  parse → extracted_quotes.json, reference_list.json, pdf_corpus_ids.json
 │
 ├─ Step 2:  resolve refs + merge quotes → references/{region}/
 │                                        → run_quotes.json   (this run's quote pool)
 │
 ├─ Step 3:  identify + reconcile       (identity fields)
 │           → kb/graphs/{region}/{node_id}.yaml   identity fields: new files,
 │                                                  or additions to existing ones
 │           → ingest_plan.yaml                     action per type, subtype
 │                                                  hypotheses, unplaced findings
 │
 ├─ Step 4:  CL mapping → cl_mapping on each node file; cl_mappings.json
 │
 ├─ Step 5:  characterise, one subagent per node   (property fields)
 │           → property fields on each node file; unplaced/{node_id}.yaml
 │
 ├─ Step 6:  review (PR by default; in-session gate if gate: true)
 │
 └─ Step 7:  handoff to survey
```

**The node file is the handoff between Steps 3, 4 and 5.** Whatever a step decides
about a node is written to the node file, in schema fields, under hook validation.
A finding that fits no field goes to `ingest_plan.yaml` or `unplaced/` — never to
free text passed between steps, and never to `notes` unless it is a caveat.

**Field guidance comes from the schema.** Step 0 writes `schema_subset.yaml`: the
graph header, `CellTypeNode`, and every class and enum they use, copied from the
schema. The `CellTypeNode` slots this workflow writes carry an `ingest_phase`
annotation, filled in order: `identity` in Step 3, `classification`
(`cl_mapping`) in Step 4, `properties` in Step 5. Never add a hand-written field
list to a step prompt: if a field's guidance is wrong, fix its description in
the schema. What stays in the prompts is workflow policy — what to write when,
what never to write, how to treat existing nodes.

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
4. Write back atomically

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
  IDs are the primary mechanism for reference resolution (see Step 2).

Key extraction rule: **verbatim quotes are delimited by `"..."` quotation marks** and
appear as standalone blocks under a paper attribution — NOT inline within synthesis
sentences. Inline quoted fragments in synthesis text are ASTA paraphrase, not verbatim.

---

## Step 0: Setup

1. Confirm `{pdf_file}` exists at the given path (relative to repo root).
2. Create output directory; `{run_id}` is its basename:
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
4. Snapshot the region's existing nodes and write the schema subset:
   ```bash
   uv run python -m evidencell.kb_index region {region} > {output_dir}/existing_nodes.yaml
   just schema-subset -o {output_dir}/schema_subset.yaml
   ```
   `existing_nodes.yaml` lists every canonical node in `kb/graphs/{region}/` with
   its identity fields (name, synonyms, definition basis, species, CL term) and
   file. It is taken before anything is written, so Step 3 reconciles against the
   KB as it was when the run started. The schema subset is the field guidance
   Steps 3 to 5 read; pass it to subagents as a file, not paraphrased.

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
and is handled in Step 3.

---

## Step 2: Reference resolution and quote store merge

Resolve author_key references using the corpus IDs extracted in Step 1,
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

6. Write {output_dir}/run_quotes.json — one entry for every quote this run
   passed to write_quote_to_refs, including ones that were already in the
   store (the call returns the key either way). This is the quote pool Steps 3
   and 5 cite from:
       [{
         "quote_key": "<returned key>",
         "corpus_id": "<digits-only>",
         "ref": "PMID:<digits>" | "https://doi.org/<doi>" | null,
         "author_key": "Last et al., YYYY",
         "section": "<report section header>",
         "text": "<the quote>"
       }]
   `ref` is the PMID form when the paper has a PMID, otherwise the DOI URL,
   otherwise null (UNRESOLVED). A quote with a null ref cannot be cited in KB
   YAML.

7. Write {output_dir}/resolution_report.md — summary:
   - Total references, HIGH/MODERATE/UNRESOLVED counts
   - Quotes merged: N new, M deduplicated
   - Any extra_references (inline citations without evidence-section quotes)

RETURN:
"Resolved {N}/{total} references. HIGH: X, MODERATE: Y, UNRESOLVED: Z.
Merged {Q} quotes into the reference store ({D} deduplicated).
See resolution_report.md and run_quotes.json."

DO NOT:
- Guess corpus IDs
- Skip the batch step and go straight to search
- Run more than 2 search attempts per fallback reference
- Overwrite existing quotes in the reference store (append only)
```

---

## Step 3: Identify and reconcile (LLM subagent)

Spawn a **single subagent** that reads the report, decides which cell types it
describes and how each relates to the region's existing nodes, and writes each
type's identity fields to its node file.

This is where the structural decisions are made: which types exist, whether each
is new, and how types relate to one another. Making them here, against the KB and
in schema fields, is what stops them being lost before Step 5.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {thinking_model}`

```
You are a cell type identification and reconciliation agent. You read an ASTA
deep research report, decide which cell types it describes, decide how each one
relates to the nodes already in the KB, and write each type's identity fields to
its KB node file. You perform ONLY the steps listed below.

PDF FILE: {pdf_file}
OUTPUT DIRECTORY: {output_dir}
REGION: {region}
RUN ID: {run_id}
DATE: {date}

INPUT FILES:
- {pdf_file}                          the report
- {output_dir}/existing_nodes.yaml    canonical nodes already in this region
- {output_dir}/run_quotes.json        this run's quotes, each with quote_key and ref
- {output_dir}/schema_subset.yaml     the schema for a node file: each field's
                                      description, shape, allowed values and
                                      ingest_phase
- schema/workflow_schema.yaml         IngestPlan: the schema for ingest_plan.yaml
- .claude/skills/term-grounding.md    how to find and write species terms

## Part A: Identify

1. Read the report. Which cell type(s) does it treat as its subject? Which
   subtypes or subpopulations does it characterise? Propose a type only where
   the report characterises it (a name plus at least one defining property). A
   type mentioned in passing is not proposed.

## Part B: Reconcile against the KB

2. For each proposed type, compare it with existing_nodes.yaml (names, synonyms,
   definition basis, the anatomy its name implies) and choose ONE action:
   - NEW — no existing node describes this population.
   - ENRICH <node_id> — an existing node describes the same population, and the
     report adds names or evidence for it.
   - DUPLICATE <node_id> — an existing node describes the same population and
     the report adds nothing new. Nothing is written for it.
   Two nodes describe the same population when the sources would let you swap
   one name for the other. A narrower population inside an existing node is NEW,
   not ENRICH; record the relation as a subtype hypothesis (step 5).
   Never choose ENRICH on name similarity alone. If unsure between NEW and
   ENRICH, choose NEW and say why in reconciliation_note; review merges.

3. Mint an id for each NEW type: lowercase_underscored, describing the
   population (not the report), and unique across the KB — check
   existing_nodes.yaml and `ls kb/graphs/*/`.

## Part C: Fill the identity fields

4. For each NEW or ENRICH type, fill every CellTypeNode field tagged
   `ingest_phase: identity` in schema_subset.yaml, following each field's
   description and allowed values. Ground species terms as term-grounding.md
   says. Cite sources by quote_key from run_quotes.json, with ref copied from
   the same entry. Use only entries whose ref is not null.

5. Subtype relations. If the report describes a type as part of another type —
   one proposed in this run or one in existing_nodes.yaml — record it in
   ingest_plan.yaml under subtype_hypotheses. The schema has no field for it yet
   (#183), so it goes nowhere else: not in notes, not as an edge. For each, give
   the kind, DEFINITIONAL or EMPIRICAL, as SubtypeHypothesisKind in
   workflow_schema.yaml defines them.

## Part D: Write

6. NEW: write kb/graphs/{region}/{node_id}.yaml with the Write tool. One node
   per file; filename and id must match. The file is a CellTypeMappingGraph with
   exactly one CellTypeNode carrying identity fields only, and no edges:

   # {node name} — {region}
   # Source: ASTA deep research report — {pdf_file}
   # Ingestion date: {date}
   # Status: DRAFT — node metadata from ASTA report, pending primary verification
   # Property assertions reference quotes in references/{region}/
   # Proposed by: asta-report-ingest

   name: "{short name}"
   description: >
     Evidence graph component for {node name}, proposed from the ASTA deep
     research report {pdf file name}.
   brain_region: {copy the brain_region block from an existing file in
                  kb/graphs/{region}/; if there is none, the region's
                  top-level structure as id, label, name_in_source}
   target_atlas: "NOT_APPLICABLE_CLASSICAL_ONLY"
   species: {the node's species, or omit}
   creation_date: "{date}"
   nodes:
     - id: ...
       name: ...
       definition_basis: ...
       species: ...
       synonyms: [...]
   edges: []

   Property fields (markers, location, NT type, morphology, electrophysiology,
   neuropeptides, notes, definition_references) are written in Step 5, and
   cl_mapping in Step 4. Do not add them here.

7. ENRICH: edit the existing node file with the Edit tool. You may ADD a synonym
   not already present, and species if absent. Never change or remove an existing
   value. If the report contradicts an existing identity value, leave the file
   unchanged and record the conflict in identity_conflicts.

8. Write {output_dir}/ingest_plan.yaml with the Write tool, one entry per
   proposed type. Its shape and field meanings are the IngestPlan class in
   workflow_schema.yaml; the pre-edit hook validates the file against it and
   checks every quote key against the reference store. Outline:

   run_id: {run_id}
   types:
     - node_id: ...
       action: ...
       file: ...
       report_sections: [...]
       reconciliation_note: ...
       subtype_hypotheses: [{parent: ..., kind: ..., quote_keys: [...], note: ...}]
       identity_conflicts: [...]
       unplaced: [{finding: ..., quote_keys: [...], closest_field: ...}]

9. If the pre-edit hook blocks a write, fix the reported problem and retry.
   Never write through a shell command — `cp`, `cat >` and `sed -i` are not
   intercepted by the hook, and a write that bypasses it is unvalidated KB content.

RETURN:
"Proposed {T} type(s): NEW {n}, ENRICH {e}, DUPLICATE {d}. Subtype hypotheses: {s}.
Wrote {w} new node file(s), edited {x}. See ingest_plan.yaml."

DO NOT:
- Write property fields (Step 5) or cl_mapping (Step 4)
- Write edges or LIT_TYPE stubs
- Record a subtype relation in notes or as an edge
- Change or remove any existing value in an ENRICH node
- Cite a quote that is not in run_quotes.json, or whose ref is null
- Put quote text in the KB YAML
```

---

## Step 4: CL mapping (LLM subagent)

Spawn a **single subagent** to anchor the run's nodes to Cell Ontology terms. It
fills the `classification` field (`cl_mapping`) in each node file, following the
`cl-mapping` skill.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {model}`

```
You are a Cell Ontology mapping agent. You set cl_mapping on the run's nodes.
You perform ONLY the steps listed below.

OUTPUT DIRECTORY: {output_dir}
REGION: {region}

INPUT FILES:
- .claude/skills/cl-mapping.md        how to choose the CL term and mapping type;
                                      read it first and follow it
- {output_dir}/ingest_plan.yaml       the run's types, with action and file
- {output_dir}/schema_subset.yaml     the CLMapping shape and CLMappingType values
- the node files named in ingest_plan.yaml

TASK:

1. Read ingest_plan.yaml. Work on every NEW type, and every ENRICH type whose
   node file has no cl_mapping. Skip DUPLICATE types.

2. For each, choose the CL term and mapping type as cl-mapping.md says, and
   write cl_mapping into the node file with the Edit tool.

3. Write {output_dir}/cl_mappings.json, one entry per node worked on:
   {
     "<node_id>": {
       "cl_term_id": "CL:...",
       "label": "...",
       "mapping_type": "EXACT | BROAD | RELATED",
       "definition_references": ["PMID:...", "https://doi.org/..."],
       "disagreement": "<only for an ENRICH node whose existing cl_mapping you
                        would have set differently; the file is left unchanged>"
     }
   }
   definition_references are the PMIDs and DOIs from an EXACT term's definition
   and xrefs; they are seed papers for later retrieval.

4. If the pre-edit hook blocks a write, fix the reported problem and retry.
   Never write through a shell command.

RETURN:
"CL mapping complete. EXACT: X, BROAD: Y, RELATED: Z. Disagreements: D.
See cl_mappings.json."

DO NOT:
- Edit any field other than cl_mapping
- Change an existing cl_mapping
- Invent CL term IDs or labels
```

---

## Step 5: Characterise, one node at a time (LLM subagents)

For each type in `ingest_plan.yaml` with action NEW or ENRICH, spawn **one
subagent** that fills the property fields in that node's file. Dispatch them **one after another**, not in parallel: each
appends `claims` to quotes in the shared store, and concurrent writes to the same
quote file would race.

One node per subagent keeps each context to one type's quotes plus the schema
subset, and a failure costs one node, not the run.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {thinking_model}`

```
You are a node characterisation agent for ONE cell type. You match quotes to the
property fields of one KB node and write them into its file. You perform ONLY the
steps listed below.

NODE: {node_id}
ACTION: {NEW | ENRICH}
NODE FILE: {file}
OUTPUT DIRECTORY: {output_dir}
REGION: {region}

INPUT FILES:
- {file}                              the node as Steps 3 and 4 left it; read it first
- {output_dir}/ingest_plan.yaml       this node's entry: report_sections,
                                      subtype_hypotheses, reconciliation_note
- {output_dir}/run_quotes.json        this run's quotes (the main pool)
- references/{region}/quotes/         the region's full quote store (an ENRICH node
                                      may already cite earlier quotes)
- {output_dir}/schema_subset.yaml     the schema for a node file: each field's
                                      description, shape, allowed values and
                                      ingest_phase
- schema/workflow_schema.yaml         UnplacedFindings: the schema for unplaced files
- .claude/skills/term-grounding.md    how to find and write anatomy and
                                      transmitter terms
- {pdf_file}                          the report, for the sections in report_sections

## Part A: Match quotes to fields

1. For each CellTypeNode field tagged `ingest_phase: properties` in
   schema_subset.yaml, find quotes that bear on it for THIS cell type or its
   immediate broader class. Discard tangential mentions and generic statements.

2. For each kept quote, add the fields it answers to its "claims" list (e.g.
   ["defining_markers", "anatomical_location"]). Quotes live in
   `references/{region}/quotes/{corpus_id}.json`, keyed by quote_key. Editing
   `claims` is allowed — it is curation metadata, not provenance. Do not touch
   `text`: the quote key is a hash of it, so any edit invalidates the key and the
   write is rejected. Make these edits with the Edit tool, never a script: the
   pre-edit hook guards the reference store too.

3. Per field, pick the 1-3 most informative quote_keys. Prefer direct
   characterisation over review, and resolved references over unresolved. Cite
   only quotes with a PMID or DOI.

## Part B: Write

4. Write the property fields into the node file with the Edit tool. Meanings,
   shapes, required sub-fields and allowed values are in schema_subset.yaml.
   - NEW: add the property fields. Leave identity fields and cl_mapping as they are.
   - ENRICH: add new entries and new sources. Never remove or rewrite an existing
     entry, source or description. A description may be extended with a sentence
     tied to a new source.

   Workflow policy (applies on top of the schema):
   - Sources carry quote_key, ref, and method/scope where known. Never put quote
     text in the YAML: no snippet fields.
   - nt_type: always attempt it. Where the sources do not state it, infer from
     well-established facts (e.g. BNST CRF neurons are GABAergic) and say it is
     inferred. find-candidates scores on NT type, so a silently missing value
     weakens retrieval.
   - defining_markers / negative_markers / neuropeptides: ncbi_gene_id: null.
   - anatomical_location and nt_type.cl_terms: ground terms as
     term-grounding.md says; every CURIE must resolve (the hook checks).
   - definition_references: the 3-5 most informative resolved refs.

5. notes: caveats only, as the notes description says. A finding that fits no
   field goes to {output_dir}/unplaced/{node_id}.yaml, written with the Write
   tool. Its shape is the UnplacedFindings class in workflow_schema.yaml, and
   the pre-edit hook validates it:

   node_id: {node_id}
   findings:
     - finding: ...
       quote_keys: [...]
       closest_field: ...

6. If the pre-edit hook blocks a write, fix the reported problem and retry.
   Never write through a shell command — `cp`, `cat >` and `sed -i` are not
   intercepted by the hook.

RETURN:
"{node_id} ({action}): {F} property fields written, {Q} quotes cited,
{U} unplaced findings."

DO NOT:
- Edit any other node's file
- Change identity fields or cl_mapping
- Write edges, or record a subtype relation anywhere
- Put quote text in the KB YAML
- Invent property values not supported by the quotes or the report's text
```

---

## Step 6: Review

Two paths. The default is a pull request; `gate: true` adds an in-session
sign-off before the run finishes.

### Default — review as a pull request

The node files are already written and hook-validated. Summarise the run and
hand review to the operator:

```
Types: NEW {n}, ENRICH {e}, DUPLICATE {d}
  {node_id}.yaml — {action} — {name} — CL: {term or "none"} — {P} properties cited
  ...
Subtype hypotheses: {s} (in ingest_plan.yaml; not yet KB content, see #183)
Unplaced findings: {u} (in unplaced/)

References: {R} papers, {Q} quotes ({U} UNRESOLVED)
Run artifacts: {output_dir}/

Review these as a diff. A NEW node is its own file, so a node you do not want
is a file you delete. ENRICH changes are additions to existing files.
```

Then run the structural check and show the result:

```bash
just validate-all
```

Branch, commit and PR are the operator's to run. A PR gives line-level comment
on each node, and CI runs the same validation on every push.

Points for the reviewer beyond the diff:
- **Reconciliation.** Check each NEW / ENRICH / DUPLICATE decision and its
  `reconciliation_note` in `ingest_plan.yaml`. A wrong NEW is a duplicate node; a
  wrong ENRICH merges two populations.
- **Subtype hypotheses and unplaced findings** are the run's record of what the
  schema could not hold. They are inputs to schema decisions (#183, #202), so
  keep them with the run artifacts.

**Reviewer note:** KB YAML carries `quote_key` values, not quote text. To read
the evidence behind an assertion, dereference the key against
`references/{region}/quotes/{corpus_id}.json`.

### `gate: true` — in-session sign-off

Use when a reviewer should sign off on new KB content before the session ends.

1. Show the same summary as above.
2. Show per-node detail — action, name, CL mapping, properties cited, and any
   node with no quote support.
3. Ask:
   > "Types: NEW {n}, ENRICH {e}, DUPLICATE {d}. CL mapped: {X}. {U} references
   > UNRESOLVED.
   >
   > Review the files in kb/graphs/{region}/ and ingest_plan.yaml. Edit directly
   > if needed, or tell me which nodes to delete or which decisions to change."
4. Apply any requested deletions or edits, then re-run `just validate-all`.

The gate changes *when* a human looks, not *what* was written — the files and
their validation are identical either way.

---

## Step 7: Handoff

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

- **Reconcile before writing.** Every proposed type is NEW, ENRICH or DUPLICATE
  against `existing_nodes.yaml`. Existing nodes are added to, never rewritten.
- **The node file is the handoff.** Steps 3, 4 and 5 pass decisions to each
  other through schema fields in the node file, not through free text.
- **Field guidance comes from the schema.** Prompts carry workflow policy; what
  a field means lives in its schema description, and when it is filled in its
  `ingest_phase`. Fix a field's guidance there, not here.
- **Tools live in the workflow and skills, never the schema.** `cl-mapping.md`
  for CL anchors, `term-grounding.md` for every other ontology term.
- **One node per file.** `kb/graphs/{region}/{node_id}.yaml`, filename matching
  the node id. Never write a combined draft.
- **Write and Edit tools only.** The pre-edit hook is a PreToolUse hook on
  `Write`/`Edit`; `cp`, `cat >` and `sed -i` bypass it silently. A write that
  bypasses it is unvalidated KB content.
- **Quotes live in the reference store.** Content-hashed keys
  (`{corpus_id}_{hash8}`) ensure dedup across ingests. The KB YAML references
  quotes by key only — never inline text.
- **The reference store is shared.** Multiple workflows append to it per
  region. Go through `write_quote_to_refs()`; never hand-merge.
- **No evidence items at ingest.** Nodes carry property fields with `sources`
  entries pointing at quote_keys. `LiteratureEvidence` items are created by
  `evidence-extraction` after primary verification.
- **No edges at ingest.** Subtype relations go to `ingest_plan.yaml` until the
  schema has a field for them (#183).
- **Run files that hold KB-pending content are validated too.**
  `ingest_plan.yaml` and `unplaced/*.yaml` have schema classes in
  `schema/workflow_schema.yaml` (`IngestPlan`, `UnplacedFindings`), and the
  pre-edit hook checks them and their quote keys like a KB file (#236).
- **Nodes are DRAFT until verified.** Property assertions come from ASTA report
  quotes, which are paraphrase until `survey` / `evidence-extraction` confirms
  them against primary text. Say so in the node header comment.
- **The gate is optional; the validation is not.** `gate: true` changes when a
  human looks, not what was written. Every node passes the hook on write and
  `just validate-all` before the run reports complete.
- **Branches and PRs belong to the operator.** This orchestrator writes files
  and stops.
- **Subagent prompts are contracts.** Pass verbatim with variables filled in.

## Known gap: reconciliation sees one region

Step 3 reconciles against `existing_nodes.yaml`, which lists the canonical nodes
in `kb/graphs/{region}/` only. A type whose node lives in another region's
directory — a type spanning two regions, or one filed under a neighbouring
region — is not seen, and may be proposed again as NEW. Review is the net for
these: check NEW ids against `kb/graphs/*/` before accepting. See #116 for what
duplicate nodes have cost.
