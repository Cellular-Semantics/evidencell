# ASTA Report Ingest Orchestrator

You are an ASTA deep research report ingestion coordinator. You parse a pre-generated
ASTA AI2 deep research PDF, propose classical CellTypeNode stubs, and build an initial
KB file populated with verbatim-quote evidence items. You then hand off to
`workflows/cite-traverse.md` for targeted primary literature retrieval.

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

## Step 1: Parsing and KB proposal subagent

Spawn a **single subagent** that reads the PDF and proposes a complete draft KB file.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {thinking_model}`

```
You are a PDF parsing and KB proposal agent. Read an ASTA deep research PDF and
produce a draft KB YAML file. You perform ONLY the steps listed below.

OUTPUT DIRECTORY: {output_dir}
PDF FILE: {pdf_file}
REGION: {region}

## Part A: Read and parse the PDF

1. Read the PDF at {pdf_file} in full.

2. Extract the document structure. For each section:
   a. Record the section title.
   b. Identify synthesis paragraphs (do NOT extract as evidence — context only).
   c. Find all "Evidence" subsections. Each evidence subsection contains:
      - Paper attribution: (Author et al., Year) — the author_key
      - Paper title (as hyperlink text)
      - One or more verbatim quotes delimited by "..." quotation marks
   d. For each verbatim quote block:
      - Record: text (exact), author_key, section_title
      - The quote is what appears between the outer " " marks as a standalone
        block beneath the paper attribution. Do NOT include synthesis sentences
        that happen to contain short quoted fragments.

3. Extract the reference list at the end of the document:
   - For each entry: author_key (e.g. "Hooft et al., 2000"),
     title (full title if available), year

4. Identify proposed classical cell types from the report's taxonomy framing:
   - Look for explicit cell type names the report uses as subjects
   - For each: note the name, any markers mentioned (e.g. SST+, Chrna2+),
     anatomy (e.g. CA1 stratum oriens), NT type (e.g. GABAergic)
   - Note any heterogeneity or subtypes discussed (e.g. SST+ vs PV+ subpopulations)

## Part B: Propose KB YAML

5. Write a draft KB YAML file to {output_dir}/proposed_kb_{region}.yaml.

   Structure (CellTypeMappingGraph):
   - One CellTypeNode per proposed classical type
   - For each node:
     - id: {region}_slug (e.g. "olm_ca1")
     - name: full classical name
     - node_type: CLASSICAL_MORPHOLOGICAL or appropriate DefinitionBasis
     - species: leave null (to be filled from primary literature)
     - anatomical_location: populate from synthesis context if clear
     - nt_type.name_in_source: from synthesis context
     - defining_markers: from synthesis context (symbol only; ncbi_gene_id: null)
     - evidence: list of proposed LiteratureEvidence items (see below)

   For each verbatim quote extracted in Part A, propose ONE LiteratureEvidence item:
   - evidence_type: LITERATURE
   - reference: "UNRESOLVED:{author_key}"    ← placeholder; resolved in Step 2
   - snippet: "<exact verbatim quote text>"  ← must be exact text from the PDF
   - source_method: "asta_report"
   - support: SUPPORT (default; adjust to PARTIAL or REFUTE if clearly warranted)
   - # discovery_source: {pdf_file}          ← YAML comment, not a schema field

   Place each evidence item under the node it most directly characterises.
   If a quote spans multiple nodes or characterises a relationship, place it
   under the most specific node and add a # note comment.

   Edges: leave empty for now — mapping relationships require primary literature.

   Header comment block:
   ```yaml
   # Draft KB — {region}
   # Source: ASTA deep research report — {pdf_file}
   # Ingestion date: {date}
   # Status: DRAFT — evidence items are asta_report source, pending primary verification
   # Classical nodes proposed by: asta-report-ingest Step 1
   ```

6. Write {output_dir}/proposed_types.json — summary of proposed classical types:
   [{
     "proposed_id": "olm_ca1",
     "name": "...",
     "markers_mentioned": [...],
     "anatomy_mentioned": [...],
     "nt_type": "...",
     "quote_count": N,
     "subtypes_noted": "SST+ vs PV+ subpopulation noted in Zhang et al., 2025"
   }]

7. Write {output_dir}/reference_list.json — raw reference list from PDF:
   [{"author_key": "Hooft et al., 2000", "title": "...", "year": 2000}]

RETURN:
"Parsed {N} sections, {M} evidence quotes across {P} papers. Proposed {Q} classical
node(s). Written proposed_kb_{region}.yaml, proposed_types.json, reference_list.json."

DO NOT:
- Include synthesis prose as evidence items
- Include ASTA-generated summary paragraphs as snippets
- Invent information not in the PDF
- Call any MCP search tools
- Create mapping edges (leave edges: [])
```

---

## Step 2: Reference resolution subagent

Spawn a **single subagent** to resolve `UNRESOLVED:{author_key}` tokens to real IDs.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {model}`

```
You are a reference resolution agent. Resolve author_key references to real
corpus IDs, PMIDs, or DOIs. You perform ONLY the steps listed below.

OUTPUT DIRECTORY: {output_dir}

TASK:

1. Read {output_dir}/reference_list.json.

2. For each entry, attempt resolution in order:
   a. Search ASTA by title fragment + author:
      mcp__Asta_semanticscholar__search_papers_by_relevance(
          keyword="{title_fragment} {author_key}",
          fields="title,authors,year,externalIds",
          limit=3
      )
      If the top result matches year and author, record corpus_id + pmid + doi.
      Set resolution_confidence: HIGH.

   b. If ASTA returns no match, search EuropePMC:
      mcp__artl-mcp__search_europepmc_papers(
          keywords="{title_fragment} {first_author} {year}",
          max_results=3,
          result_type="core"
      )
      If a result matches year and author, record pmid + doi.
      Batch-resolve pmids to corpus_ids:
      mcp__Asta_semanticscholar__get_paper_batch(
          ids=["PMID:xxx", ...], fields="title,externalIds"
      )
      Set resolution_confidence: MODERATE.

   c. If neither resolves, mark resolution_confidence: UNRESOLVED.
      Do not guess.

3. Write {output_dir}/resolution_map.json:
   {
     "Hooft et al., 2000": {
       "corpus_id": "12345678",
       "pmid": "10862698",
       "doi": "10.1523/JNEUROSCI.20-04-01386.2000",
       "title": "Differential Expression of Group I Metabotropic...",
       "year": 2000,
       "resolution_confidence": "HIGH",
       "quote_count": 2
     },
     "Ghost 1999": {
       "resolution_confidence": "UNRESOLVED",
       "title_fragment": "...",
       "year": 1999,
       "quote_count": 1
     }
   }

   Include quote_count for each key (count occurrences in proposed_kb_{region}.yaml).

4. Apply resolution: run the Python CLI to replace UNRESOLVED tokens:
   uv run python -m evidencell.parse_asta_report resolve \
     {output_dir}/proposed_kb_{region}.yaml \
     {output_dir}/resolution_map.json \
     > {output_dir}/proposed_kb_{region}_resolved.yaml

5. Generate the resolution report:
   uv run python -m evidencell.parse_asta_report report \
     {output_dir}/resolution_map.json \
     > {output_dir}/resolution_report.md

RETURN:
"Resolved {N}/{total} references. HIGH: X, MODERATE: Y, UNRESOLVED: Z.
See resolution_report.md."

DO NOT:
- Guess corpus IDs
- Use title fragments shorter than 5 words for matching
- Run more than 2 search attempts per reference
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

5. Update {output_dir}/proposed_kb_{region}_resolved.yaml:
   - For nodes with a CL match: add cl_mapping block
   - For nodes without: add proposed_cl_term block with status CANDIDATE

6. Extract CL definition reference seeds:
   uv run python -m evidencell.parse_asta_report cl-seeds \
     {output_dir}/cl_mappings.json \
     > {output_dir}/cl_seeds.json

RETURN:
"CL lookup complete. Matched: N nodes. Unmatched (CANDIDATE): M nodes.
CL definition references: P additional seed papers. See cl_mappings.json."

DO NOT:
- Auto-assign EXACT mapping if only a synonym matches — use BROAD or RELATED
- Invent CL term IDs
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

3. Show the draft KB file (abbreviated — node names, evidence count per node,
   unresolved refs remaining):
   - Count nodes, evidence items, UNRESOLVED references remaining
   - List any unresolved references so the human can add them manually

4. Ask:
   > "Proposed {N} node(s): {names}. CL mapped: {X}. Evidence items: {E}
   > ({U} references still UNRESOLVED).
   >
   > Please review {output_dir}/proposed_kb_{region}_resolved.yaml.
   > Edit directly if needed (correct node names, add missing corpus IDs,
   > adjust evidence placement). Then confirm to write to kb/draft/{region}/."

5. After confirmation, write the approved file:
   ```bash
   mkdir -p kb/draft/{region}
   cp {output_dir}/proposed_kb_{region}_resolved.yaml \
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
Evidence items: {E} (all source_method: "asta_report" — pending primary verification)
Output dir: {output_dir}/

CL seeds available: {P} papers from CL definition references
Report refs resolved: {R} papers

NEXT STEPS
==========

Option A — Targeted primary literature retrieval (recommended):
  Hand workflows/cite-traverse.md to Claude Code with:
    node_ids: {list of node IDs}
    paper_ids: {resolved corpus IDs from resolution_map.json} + {CL seeds from cl_seeds.json}
    output_dir: {output_dir}
    node_context: {built from first approved node — or repeat per node}
    query: "{region} {first_node_name} characterisation"
    report_context_file: (optional — write synthesis prose from PDF to report_context.md first)

Option B — Proceed directly to evidence extraction:
  The draft KB already has asta_report evidence items.
  Hand workflows/evidence-extraction.md to Claude Code.
  Note: evidence items will remain source_method "asta_report" until Option A is run.

Option C — Run taxonomy ingestion in parallel:
  Place taxonomy table in inputs/taxonomies/
  Hand workflows/ingest-taxonomy.md to Claude Code
  (can run concurrently with Option A in a separate session)
```

Ask: "Which option would you like to proceed with?"

---

## Rules

- **Classical nodes emerge here.** Do not require pre-existing KB nodes.
- **Verbatim only.** Evidence items must use exact PDF quote text. The parsing
  subagent must not paraphrase.
- **source_method: "asta_report"** is the correct tag for all evidence items
  from this workflow. They require primary literature verification.
- **One gate.** Review ref resolution quality + proposed nodes together.
  Do not proceed to kb/draft/ without human confirmation.
- **Validation hook fires on write.** Fix any validation errors before confirming
  to the user that the file was written successfully.
- **Subagent prompts are contracts.** Pass verbatim with variables filled in.
