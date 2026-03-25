# ASTA Report Ingest Orchestrator

You are an ASTA deep research report ingestion coordinator. You parse a pre-generated
ASTA AI2 deep research PDF, propose classical CellTypeNode stubs with property metadata,
and resolve all references. Quotes are stored in a shared per-region `references.json`
with content-hashed keys — they are **not** promoted to KB evidence items. A validation
round matches quotes to node properties and flags ambiguities for downstream
`cite-traverse` to resolve against primary literature.

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
```

Output directory: `kb/{region}/traversal_output/{YYYYMMDD}_{region}_report_ingest/`

---

## Data flow overview

```
PDF
 ├─ Step 1:   parse → extracted_quotes.json  (temp, keyed by author_key)
 │                   → proposed_types.json    (proposed node summaries)
 │                   → reference_list.json    (author_keys + titles)
 │
 ├─ Step 1b:  hyperlinks → pdf_corpus_ids.json (S2 corpus IDs from PDF links)
 │
 ├─ Step 2:   batch resolve + merge quotes
 │            → kb/draft/{region}/references.json  (shared, keyed by corpus_id)
 │               quotes stored with content-hashed keys: {corpus_id}_{hash8}
 │
 ├─ Step 3:   CL lookup → cl_mappings.json
 │
 ├─ Step 3b:  quote validation (Round 1)
 │            → proposed_kb_{region}.yaml     (nodes with metadata, quote_keys on assertions)
 │            → validation_notes.json         (ambiguities, contradictions, gaps)
 │
 ├─ Step 4:   [GATE] human review
 │
 └─ Step 5:   handoff to cite-traverse (Round 2 targets ambiguities + gaps)
```

Quotes live in `references.json`, never in the KB YAML. The KB references
quotes by key. Reports dereference keys to include snippets when needed.

---

## references.json — shared quote store

`kb/draft/{region}/references.json` is the single source of truth for all
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

**Quote key scheme:**

```python
import hashlib

def quote_key(corpus_id: str, text: str) -> str:
    """Content-hashed quote key. Deterministic, deduplicates across ingests."""
    normalized = " ".join(text.lower().split())
    h = hashlib.sha256(normalized.encode()).hexdigest()[:8]
    return f"{corpus_id}_{h}"
```

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

**Merge protocol:** when appending to an existing `references.json`:
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
   mkdir -p kb/{region}/traversal_output/{YYYYMMDD}_{region}_report_ingest
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
then merge extracted quotes into the shared `references.json` with
content-hashed keys.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {model}`

```
You are a reference resolution agent. Resolve author_key references to real
corpus IDs, then merge quotes into the shared references.json quote store.
You perform ONLY the steps listed below.

OUTPUT DIRECTORY: {output_dir}
REGION: {region}
REFERENCES FILE: kb/draft/{region}/references.json

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

5. Merge into kb/draft/{region}/references.json:

   a. Read existing references.json (or start with {"_meta": {...}} if first
      ingest for this region). Create kb/draft/{region}/ if needed.

   b. For each resolved reference, generate content-hashed quote keys:
      ```python
      import hashlib
      def quote_key(corpus_id, text):
          normalized = " ".join(text.lower().split())
          h = hashlib.sha256(normalized.encode()).hexdigest()[:8]
          return f"{corpus_id}_{h}"
      ```

   c. For each reference:
      - If corpus_id already exists in references.json: merge new quotes
        (skip duplicates by key), append any new author_keys to the
        author_keys list.
      - If new: add full entry with metadata + quotes.

   d. Each quote entry:
      {
        "text": "<exact quote>",
        "section": "Anatomical Location and Morphology",
        "claims": [],
        "source_method": "asta_report",
        "status": "pending",
        "added_by": "{run_id}"
      }
      (claims list is empty here — populated in Step 3b)

   e. Update _meta.last_updated and _meta.last_updated_by.
      Write back to kb/draft/{region}/references.json.

6. Write {output_dir}/resolution_report.md — summary:
   - Total references, HIGH/MODERATE/UNRESOLVED counts
   - Quotes merged: N new, M deduplicated
   - Any extra_references (inline citations without evidence-section quotes)

RETURN:
"Resolved {N}/{total} references. HIGH: X, MODERATE: Y, UNRESOLVED: Z.
Merged {Q} quotes into references.json ({D} deduplicated).
See resolution_report.md."

DO NOT:
- Guess corpus IDs
- Skip the batch step and go straight to search
- Run more than 2 search attempts per fallback reference
- Overwrite existing quotes in references.json (merge only)
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

## Step 3b: Quote validation and KB proposal (Round 1)

Spawn a **single subagent** that matches quotes from `references.json` to node
property fields, writes the draft KB YAML (nodes with metadata + quote_keys on
assertions), and flags ambiguities for Round 2.

This is the key filtering step: quotes are evaluated for relevance to specific
properties, not dumped in bulk.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {thinking_model}`

```
You are a quote validation and KB proposal agent. You match quotes from the
shared references.json to node property fields and produce a clean draft KB.
You perform ONLY the steps listed below.

OUTPUT DIRECTORY: {output_dir}
REGION: {region}

INPUT FILES:
- {output_dir}/proposed_types.json                (node summaries from Step 1)
- kb/draft/{region}/references.json               (shared quote store)
- {output_dir}/cl_mappings.json                   (CL term matches)

PROPERTY CATEGORIES:
Quotes can validate these node property fields:
- morphology_notes / morphology_sources
- electrophysiology_class / ephys_sources
- defining_markers (positive markers)
- negative_markers
- neuropeptides
- nt_type
- anatomical_location / location_sources
- colocated_types

## Part A: Match quotes to properties

1. Read all input files.

2. For each proposed node in proposed_types.json, scan quotes in
   references.json for claims about specific properties:

   For each quote, determine:
   a. Which property category does it address? (morphology, ephys, markers, etc.)
      A quote may address multiple categories.
   b. Does it SUPPORT, REFINE, or CONTRADICT the proposed node's summary
      for that property?
   c. Relevance: HIGH (directly characterises this specific cell type),
      MODERATE (characterises the broader class or a related type),
      LOW (tangential mention, generic statement, or mostly about other types)

   Keep only HIGH and MODERATE relevance quotes. Discard LOW.

3. For each kept quote, update its "claims" list in references.json with
   the property categories it addresses (e.g. ["soma_location_so", "sst_positive"]).
   Write back to references.json.

4. For each property category on each node, select the best supporting
   references and their quote keys:
   - Pick the 1-3 most informative quote_keys per property
   - Prefer: direct characterisation > review > tangential mention
   - Prefer: resolved references (with PMID/DOI) > UNRESOLVED

5. Flag validation issues in a structured list:
   - CONTRADICTION: quotes from different papers disagree on a property
     (e.g. spiny vs aspinous dendrites)
   - AMBIGUITY: a property claim is qualified or species-dependent
   - GAP: a property mentioned in proposed_types.json has no supporting quotes
   - HETEROGENEITY: quotes suggest the proposed type may contain distinct
     subtypes that need separate nodes

## Part B: Write draft KB YAML

6. Write {output_dir}/proposed_kb_{region}.yaml — the draft KB file.

   Structure (CellTypeMappingGraph):
   - One CellTypeNode per proposed classical type
   - For each node, populate property fields from proposed_types.json summaries:
     - id, name, definition_basis
     - species: null (to be confirmed from primary literature)
     - anatomical_location: from synthesis context if unambiguous
     - nt_type.name_in_source
     - defining_markers: symbol only; ncbi_gene_id: null
     - negative_markers, neuropeptides: as identified
     - morphology_notes: concise summary from synthesis context
     - electrophysiology_class: concise summary from synthesis context
     - morphology_sources: PropertySource entries with ref + quote_key
     - ephys_sources: PropertySource entries with ref + quote_key
     - location_sources: PropertySource entries with ref + quote_key
     - cl_mapping: from cl_mappings.json (if matched)
     - definition_references: the top 3-5 most informative resolved refs overall
     - is_terminal: false
     - notes: any important caveats from validation

   For *_sources entries, use this pattern:
   ```yaml
   morphology_sources:
     - ref: "PMID:20421280"
       method: "biocytin fill"
       scope: "adult rat CA1"
       quote_key: "12345678_a3f2c1d0"  # → lookup in references.json
   ```

   The quote_key references a specific quote in references.json. Reports
   can dereference to include the snippet text, or omit it for compact output.

   Do NOT inline quote text in the KB YAML. Use quote_keys only.

   Edges: leave empty — mapping relationships require primary literature.

   Header comment block:
   ```yaml
   # Draft KB — {region}
   # Source: ASTA deep research report — {pdf_file}
   # Ingestion date: {date}
   # Status: DRAFT — node metadata from ASTA report, pending primary verification
   # Property assertions reference quotes in kb/draft/{region}/references.json
   # Classical nodes proposed by: asta-report-ingest
   ```

## Part C: Write validation notes

7. Write {output_dir}/validation_notes.json:
   {
     "nodes": {
       "olm_ca1": {
         "property_support": {
           "morphology_notes": {
             "status": "SUPPORTED",
             "quote_keys": ["12345678_a3f2c1d0", "87654321_c2e1b4a5"],
             "issues": []
           },
           "defining_markers": {
             "status": "PARTIAL",
             "quote_keys": ["11111111_d4f5e6a7"],
             "issues": [
               {
                 "type": "AMBIGUITY",
                 "description": "TRPV1 reported in OLM cells by Hurtado-Zavala 2017
                   but not confirmed by other sources — may be subpopulation-specific",
                 "quote_keys": ["28722015_f8a9b0c1"]
               }
             ]
           }
         },
         "gaps": ["colocated_types — no quotes address spatial relationships"],
         "overall_confidence": "HIGH"
       }
     },
     "round2_targets": [
       {
         "node_id": "olm_ca1",
         "property": "defining_markers",
         "issue": "TRPV1 expression ambiguity",
         "quote_keys": ["28722015_f8a9b0c1"],
         "action": "Read primary source to confirm scope of TRPV1 expression"
       }
     ]
   }

   The round2_targets list feeds directly into cite-traverse as prioritised
   retrieval targets. cite-traverse reads the quote_keys, looks up the paper
   in references.json, fetches the primary text, and adds verified quotes.

RETURN:
"Validated {N} node(s). Properties supported: {S}, partial: {P}, gaps: {G}.
Issues flagged: {I} (contradictions: {C}, ambiguities: {A}).
Round 2 targets: {T}. Written proposed_kb_{region}.yaml and validation_notes.json."

DO NOT:
- Put quote text in the KB YAML (use quote_keys only)
- Invent property values not supported by quotes or synthesis context
- Mark LOW-relevance quotes as supporting refs
- Skip writing validation_notes.json even if no issues are found
```

---

## Step 4: [GATE] Human review

Present to the user for review and approval before writing to the canonical KB location.

1. Show resolution quality:
   ```
   cat {output_dir}/resolution_report.md
   ```

2. Show proposed nodes + CL mappings:
   ```
   cat {output_dir}/proposed_types.json
   cat {output_dir}/cl_mappings.json
   ```

3. Show validation summary — for each node, list:
   - Properties with support status (SUPPORTED / PARTIAL / GAP)
   - Issues flagged (contradictions, ambiguities)
   - Round 2 targets count

4. Show the draft KB file summary:
   - Node names and definition_basis
   - Supporting refs per property (count)
   - Any UNRESOLVED references remaining

5. Ask:
   > "Proposed {N} node(s): {names}. CL mapped: {X}.
   > Properties: {S} supported, {P} partial, {G} gaps.
   > Issues: {I} flagged for Round 2.
   >
   > Please review {output_dir}/proposed_kb_{region}.yaml.
   > Edit directly if needed (correct node names, adjust markers,
   > add missing refs). Then confirm to write to kb/draft/{region}/."

6. After confirmation, write the approved file:
   ```bash
   mkdir -p kb/draft/{region}
   cp {output_dir}/proposed_kb_{region}.yaml \
      kb/draft/{region}/{YYYYMMDD}_{region}_report_ingest.yaml
   ```
   Pre-edit validation hook fires automatically on write.

---

## Step 5: Handoff

After the draft KB is written, present the handoff options:

```
INGEST COMPLETE
===============
Region: {region}
Draft KB: kb/draft/{region}/{kb_file}
Nodes written: {N}
References: kb/draft/{region}/references.json ({R} papers, {Q} quotes)
Output dir: {output_dir}/

Validation: {S} properties supported, {P} partial, {G} gaps
Round 2 targets: {T} issues flagged for primary literature verification
CL seeds available: {CL} papers from CL definition references

NEXT STEPS
==========

Option A — Targeted primary literature retrieval (recommended):
  Hand workflows/cite-traverse.md to Claude Code with:
    node_ids: {list of node IDs}
    references_file: kb/draft/{region}/references.json
    round2_targets: {output_dir}/validation_notes.json  ← prioritised issues
    output_dir: {output_dir}

  cite-traverse will:
  1. Prioritise Round 2 targets (ambiguities, contradictions, gaps)
  2. Fetch primary literature for flagged papers
  3. Verify ASTA quotes (flip status: pending → verified or superseded)
  4. Add new quotes with source_method: "primary" and status: "verified"
  5. Surface new claims the ASTA report missed

Option B — Run taxonomy ingestion in parallel:
  Place taxonomy table in inputs/taxonomies/
  Hand workflows/ingest-taxonomy.md to Claude Code
  (can run concurrently with Option A in a separate session)
```

Ask: "Which option would you like to proceed with?"

---

## Rules

- **Classical nodes emerge here.** Do not require pre-existing KB nodes.
- **Quotes live in references.json.** Content-hashed keys (`{corpus_id}_{hash8}`)
  ensure dedup across ingests. The KB YAML references quotes by key only —
  never inline text.
- **references.json is shared.** Multiple workflows append to the same file
  per region. Always read-merge-write, never overwrite.
- **No evidence items at ingest.** The draft KB has nodes with property fields
  and `*_sources` entries pointing to quote_keys. Actual LiteratureEvidence
  items are created by `evidence-extraction` after primary verification.
- **Two rounds.** Round 1 (Step 3b) validates against ASTA quotes — cheap,
  no API calls. Round 2 (cite-traverse) goes to primary literature for
  ambiguities, contradictions, and gaps — expensive, targeted.
- **One gate.** Review nodes + validation notes together.
  Do not proceed to kb/draft/ without human confirmation.
- **Validation hook fires on write.** Fix any validation errors before confirming
  to the user that the file was written successfully.
- **Subagent prompts are contracts.** Pass verbatim with variables filled in.
