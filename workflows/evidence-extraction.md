# Evidence Extraction Orchestrator

You are an evidence extraction coordinator. You take the output of
`workflows/cite-traverse.md` or `workflows/asta-report-ingest.md`
(`all_summaries.json` + `paper_catalogue.json`) and extract schema-compliant
evidence items for human review. You delegate to focused subagents with
**exact prompts** — you never extract or judge evidence directly.

Entry point: run after reviewing `report.md` from cite-traverse, or after
reviewing the draft KB from asta-report-ingest (for supplementing asta_report
evidence with verified primary literature items).

---

## Run parameters

```
PARAMS:
  node_id: ""              # required — evidencell node ID to extract evidence for
  region: ""               # required — brain region slug
  summaries_file: ""       # required — path to all_summaries.json
  catalogue_file: ""       # required — path to paper_catalogue.json
  kb_file: ""              # required — path to target KB YAML in kb/draft/{region}/
  model: "sonnet"          # auto-flagging subagent
  thinking_model: "opus"   # extraction subagent
```

---

## Step 0: Auto-flagging subagent

Spawn a **single subagent** to scan summaries for species/context flags.

**Subagent config:** `subagent_type: "general-purpose"`, `model: {model}`

```
You are an auto-flagging agent. Scan literature summaries for signals that may
affect whether evidence is applicable to the target node. You perform ONLY the
steps below.

SUMMARIES FILE: {summaries_file}
CATALOGUE FILE: {catalogue_file}
NODE ID: {node_id}

TASK:

1. Read {summaries_file}. For each entry, check for these signals in the
   summary text and quotes:
   - NON_MODEL_SPECIES: mentions human, primate, non-rodent species explicitly
   - EMBRYONIC: embryonic, prenatal, E10-E20, fetal
   - EARLY_POSTNATAL: P0-P14, neonatal, early postnatal
   - DISEASE_MODEL: epilepsy, seizure, knockout, transgenic disease model
   - IN_VITRO: cell culture, dissociated, slice culture (not acute slice)
   - REVIEW_ONLY: the quote is clearly contextual/introductory, not a primary finding

2. For each flagged entry, record:
   {
     "source_corpus_id": "...",
     "flags": ["NON_MODEL_SPECIES", "REVIEW_ONLY"],
     "flag_notes": "mentions human tissue; quote is from introduction"
   }

3. Annotate paper_catalogue.json entries with flags from their summaries.
   Write {output_dir}/paper_catalogue_flagged.json — same as catalogue but
   each entry has added "flags": [...] and "flag_notes": "..."

4. Write brief flag summary to stdout:
   "Flagged: N entries. NON_MODEL_SPECIES: X, EMBRYONIC: Y, IN_VITRO: Z,
    REVIEW_ONLY: W. Unflagged: M."

DO NOT:
- Exclude any entries — only annotate
- Flag entries for being LOW node_relevance (that's the extraction agent's job)
```

---

## Step 1: [GATE] Catalogue weeding

1. Read `paper_catalogue_flagged.json`. Present flagged papers grouped by flag type:

   ```
   CATALOGUE WEEDING — {node_id}
   ==============================
   Flagged entries: N

   NON_MODEL_SPECIES (X):
     - [2019] Author et al. — "Title" — mentions human tissue
   REVIEW_ONLY (W):
     - [2015] Author et al. — "Title" — introductory context only
   ...

   Unflagged: M papers
   ```

2. Ask: "Mark any papers to EXCLUDE from extraction (provide corpus IDs or numbers).
   Everything else will be included. Or type 'all' to include everything."

3. Record excluded corpus IDs. Write `{output_dir}/excluded_ids.json`.

---

## Step 2: [OPTIONAL] Full-text species/stage confirmation

If any papers are marked UNCERTAIN (not clearly excludable but flagged), offer:
"Fetch PMC full text for UNCERTAIN papers to check Methods section?"

If yes, for each UNCERTAIN corpus ID:
```
mcp__artl-mcp__get_all_identifiers_from_europepmc("{corpus_id}")
→ if PMC ID found:
mcp__artl-mcp__get_europepmc_full_text("{pmcid}")
→ scan Methods section for species, age, experimental system
→ update flag: EXCLUDE or INCLUDE based on findings
```

---

## Step 3: Extraction subagent

Read the target node from the KB to build NODE_CONTEXT, then spawn a single
extraction subagent.

Read `{kb_file}`, extract for `{node_id}`:
- name
- defining_markers (symbols)
- anatomical_location (labels)
- nt_type.name_in_source
Build `NODE_CONTEXT` string (same format as lit-review.md Step 0).

**Subagent config:** `subagent_type: "general-purpose"`, `model: {thinking_model}`

```
You are an evidence extraction agent. Extract schema-compliant evidence items
from pre-retrieved literature summaries. You perform ONLY the steps below.

NODE ID: {node_id}
NODE CONTEXT: {node_context}
KB FILE: {kb_file}
SUMMARIES FILE: {summaries_file}
EXCLUDED CORPUS IDS: {excluded_ids}

SCHEMA EVIDENCE TYPES — choose the most specific applicable:

  LiteratureEvidence (most common — any paper-based claim):
    Required: reference (PMID:xxx or DOI:xxx or CorpusId:xxx),
              snippet (verbatim, exact substring of quotes field),
              support (SUPPORT / PARTIAL / REFUTE)
    Optional: study_type

  ElectrophysiologyEvidence:
    Use when: paper reports e-type classification or firing pattern data
    Required fields also: dataset_accession (if available), etype_label, key_features

  MorphologyEvidence:
    Use when: paper reports imaging or morphological reconstruction
    Required: dataset_accession, imaging_method, key_features

  MarkerAnalysisEvidence:
    Use when: paper reports quantitative overlap between marker sets
    Required: dataset_accession, markers_examined, overlap_metric, overlap_value

  SpatialColocationEvidence:
    Use when: paper reports MERFISH or spatial transcriptomics colocation
    Required: spatial_dataset, spatial_technology, anatomical_region

TASK:

1. Read {summaries_file}. Skip any entry where source_corpus_id is in
   EXCLUDED CORPUS IDS.

2. For each summary entry (process HIGH and MODERATE node_relevance first,
   then LOW):

   a. Select the single most informative verbatim quote from the entry's
      "quotes" field. The snippet MUST be an exact substring of one of
      those quote strings — do not paraphrase or truncate mid-sentence.

   b. Decide which schema evidence type best fits.

   c. Determine which node field this quote most directly supports:
      defining_markers / negative_markers / anatomical_location / nt_type /
      electrophysiology_class / morphology_notes / colocated_types / other

   d. Assess support:
      - SUPPORT: quote clearly supports the claim about this node
      - PARTIAL: quote is consistent but indirect or from a different species/context
      - REFUTE: quote contradicts current node characterisation

   e. Note: entries with source_method="asta_report" are from the discovery
      report and not yet verified by primary literature. Mark these clearly
      with a # note comment in the YAML.

3. Write {output_dir}/proposed_evidence_{node_id}.yaml:

   Header:
   ```yaml
   # Proposed evidence items for {node_id}
   # Source summaries: {summaries_file}
   # Extraction date: {date}
   # Items below are PROPOSED — require expert review before KB commit
   ```

   For each proposed item:
   ```yaml
   # --- Evidence item {N} ---
   # Target field: {field_name}
   # Source: {source_method} | section: {section} | CorpusId:{source_corpus_id}
   - evidence_type: LITERATURE
     reference: "PMID:xxxxxxxx"
     snippet: "exact verbatim quote text"
     support: SUPPORT
   ```

4. Write {output_dir}/extraction_report.md:
   - Summary table: N items proposed, breakdown by evidence type and support value
   - Items skipped (LOW relevance, excluded): listed briefly with reason
   - Node fields with no evidence found: listed explicitly
   - asta_report items: listed separately as "pending primary verification"

RETURN:
"Proposed {N} evidence items for {node_id}. Written proposed_evidence_{node_id}.yaml.
Fields covered: {list}. Gaps: {list}. asta_report items needing verification: {M}."

DO NOT:
- Paraphrase or shorten quotes — use exact text only
- Propose more than 1 evidence item per summary entry
- Propose items without a verbatim snippet
- Make claims about mappings — evidence items target nodes, not edges
```

---

## Step 4: [GATE] Expert review

1. Read and present `proposed_evidence_{node_id}.yaml` to the user.
2. Show `extraction_report.md` summary.
3. Ask: "Review each proposed item. Approve (keep as-is), edit, or reject.
   When done, confirm to write approved items to the KB."
4. The user may edit `proposed_evidence_{node_id}.yaml` directly.
5. After confirmation, write approved items file:
   `{output_dir}/approved_evidence_{node_id}.yaml`

---

## Step 5: Append to KB

1. Read `approved_evidence_{node_id}.yaml`.
2. Read `{kb_file}` (YAML). Find the `{node_id}` node.
3. Append each approved evidence item to the node's `evidence:` list.
4. Write back to `{kb_file}`. Pre-edit validation hook fires automatically.
5. If validation fails, show the error and ask the user how to resolve it.
   Do not silently skip failed items.
6. Print:
   ```
   EXTRACTION COMPLETE
   ===================
   Node: {node_id}
   Items appended: N
   KB file: {kb_file}
   Next step: run workflows/map-cell-type.md when evidence base is sufficient
   ```

---

## Rules

- **1:1 snippets per item.** One verbatim quote per evidence item for full traceability.
- **Exact substrings only.** Every snippet must be verifiable in all_summaries.json.
- **Expert gate is non-negotiable.** Nothing writes to the KB without human review.
- **asta_report items are provisional.** Flag them clearly; they need primary
  literature verification via cite-traverse before confidence can be raised.
- **Subagent prompts are contracts.** Pass verbatim with variables filled in.
- **Data flows through files, not context.**
