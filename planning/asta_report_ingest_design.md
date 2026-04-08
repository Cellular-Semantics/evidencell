# ASTA Report Ingest Pipeline — Design Draft

> **Status**: DRAFT — under review. Not approved for implementation.
> **Date**: 2026-03-23

---

## Core insight

An ASTA deep research report = **synthesis prose** + **verbatim quotes**.

- Synthesis prose → informs which fields to populate and where gaps are; never KB evidence
- Verbatim quotes → usable directly as KB evidence with `source_method: "asta_report"`

The report enables **direct KB population**: parse PDF → propose node stubs + evidence
items → human reviews → write to `kb/draft/`. Targeted citation traversal then fills
gaps and verifies uncertain items, rather than being required before any KB entries exist.

This is faster to something useful. The trade-off is that `asta_report`-sourced evidence
items carry lower default confidence than `asta_snippet` or `europepmc_fulltext` items —
they should be flagged for verification when the field is important.

---

## Provenance model for `asta_report` evidence

Each evidence item derived from the report has:

```yaml
reference: "PMID:xxxxxxxx"           # primary paper — the authoritative source
snippet: "exact verbatim quote..."   # must be exact text from the report's quote block
source_method: "asta_report"         # distinguishes from asta_snippet / europepmc_fulltext
# discovery_source: inputs/deepsearch/OLM_Neurons_asta_report.pdf
```

- `reference` always points to the **primary paper**, not the report itself
- The PDF filename (stored locally in `inputs/deepsearch/`) is the stability anchor;
  noting it as a YAML comment is sufficient — no need for a formal schema field
- A PDF hash could be added for integrity but is probably overkill at this stage
- The report is the discovery mechanism, not the evidence source

**Confidence implication**: evidence items with `source_method: "asta_report"` should
default to `MODERATE` or `LOW` confidence pending primary literature verification.
The synthesis + quotes together provide good signal, but the ASTA report is not
peer-reviewed and synthesis may occasionally misrepresent the primary finding.

---

## Where cell types come from

Classical cell type nodes **emerge from research** — they are not pre-created.

```
Brain region / field of interest
         │
         ├─ ingest-taxonomy.md ─────► atlas cluster CellTypeNodes (transcriptomic side)
         │
         └─ asta-report-ingest.md ──► proposes classical CellTypeNodes + initial evidence
                    │                 from the report's taxonomy framing + verbatim quotes
                    │
                    ▼
           [GATE] Human approves proposed nodes + evidence items
                    │
                    ▼
           kb/draft/{region}/ populated with stubs + asta_report evidence items
                    │
                    ▼
           cite-traverse.md ─────────► fills gaps, verifies uncertain items,
                    │                  may surface additional classical types
                    ▼
           synthesis subagent ─────────► "Evidence gaps" + "New types encountered"
                    │
                    ▼
           [GATE] Human decides: extend scope / run further retrieval / proceed to mapping
```

Classical type discovery is **iterative** — citation traversal may reveal types not in
the original report. The synthesis subagent flags these; the human decides whether to
add stubs and follow up.

---

## Simplified workflow: `asta-report-ingest.md`

**Entry point**: `just ingest-report {region} {pdf_file}`
(No `node_id` required — nodes are created by this workflow.)

**Output directory**: `kb/{region}/traversal_output/{YYYYMMDD}_{region}_report_ingest/`

### Step 0: Setup
- Confirm PDF exists in `inputs/deepsearch/`
- Create output dir, write `run_config.json` (includes PDF filename)

### Step 1: Parsing + proposal subagent (opus — judgment-heavy)
Reads the PDF natively. In a single pass, produces a draft KB file:

**Extracts**:
- Proposed classical CellTypeNodes from the report's taxonomy framing:
  name, defining markers, anatomy, NT type, definition references where explicit
- For each verbatim quote: target node, target field, verbatim text, `author_key`
  (e.g. "Maccaferri & McBain 1995"), section_label
- Reference list: `{author_key, title_fragment, year}`

**Outputs**: `proposed_kb_{region}.yaml` — a draft KB file with:
- CellTypeNode stubs (markers, anatomy, NT type populated from synthesis context)
- Evidence items with `snippet: "<verbatim quote>"`, `reference: "UNRESOLVED:{author_key}"`,
  `source_method: "asta_report"`, `# discovery_source: {pdf_file}`

### Step 2: Reference resolution subagent (sonnet — mechanical)
For each `UNRESOLVED:{author_key}` in `proposed_kb_{region}.yaml`:
- Search ASTA + EuropePMC to resolve to corpus_id / PMID / DOI
- Update references in the proposed KB file
- Flag unresolved as `reference: "UNRESOLVED:{author_key}"` with `resolution_confidence: LOW`
→ writes `proposed_kb_{region}_resolved.yaml` + `resolution_report.md`
   (summary: N resolved HIGH/MODERATE, M unresolved)

### Step 3: CL lookup subagent (sonnet, via OLS4 MCP)
For each proposed CellTypeNode:
- Search OLS4 for matching CL term by name + synonyms
- If found: add `cl_mapping` to the node stub; note any CL definition references
  (these become additional seed papers for cite-traverse)
- If not found: add `proposed_cl_term` with status CANDIDATE
→ updates `proposed_kb_{region}_resolved.yaml` with CL fields

### Step 4: [GATE] Human reviews
Orchestrator presents:
- `proposed_kb_{region}_resolved.yaml` in readable form
- `resolution_report.md` (which refs are unresolved)
- Any UNRESOLVED references for manual corpus ID entry or drop decision

Human can edit the YAML directly. Confirmed file written to `kb/draft/{region}/`.
Pre-edit validation hook fires on write.

### Step 5: Handoff
```
Nodes now in kb/draft/{region}/

For targeted retrieval + gap filling:
  Hand workflows/cite-traverse.md to Claude Code with:
    node_ids: [list of approved node IDs]
    paper_ids: [corpus IDs resolved from report references + CL definition refs]
    output_dir: {output_dir}
    report_context_file: {output_dir}/report_context.md

For mapping (if evidence base is sufficient):
  Hand workflows/map-cell-type.md to Claude Code
```

---

## What `cite-traverse.md` adds

After asta-report-ingest, citation traversal:
- Fetches ASTA snippets for the resolved papers (verifying / extending report quotes)
- Follows citations to find additional evidence not in the report
- Upgrades `source_method` on confirmed items from `asta_report` → `asta_snippet`
  (or leaves as-is if the snippet exactly matches the report quote)
- Flags any new classical types encountered → human decides whether to add stubs

The synthesis subagent output gains a **"New classical types encountered"** section
alongside "Evidence gaps".

---

## Orchestrator split (unchanged from previous)

| Orchestrator | Responsibility |
|---|---|
| `asta-report-ingest.md` | PDF → draft KB (nodes + asta_report evidence items) |
| `cite-traverse.md` | Targeted retrieval + synthesis for gap filling |
| `lit-review.md` | Seed discovery → cite-traverse (for when no report exists) |
| `evidence-extraction.md` | Summaries → proposed evidence items (for cite-traverse output) |

---

## Python module: `parse_asta_report.py`

Much thinner than originally planned. Main job: support the subagents with
deterministic transformations, not drive the workflow.

```python
resolve_references(yaml_str, resolution_map) → str
    # Replace UNRESOLVED:{key} tokens with resolved PMID/DOI/corpus_id

build_resolution_report(resolution_map) → str
    # Markdown summary of resolved / unresolved refs

extract_cl_seeds(cl_mappings) → list
    # Pull CL definition reference PMIDs/DOIs for use as cite-traverse seeds
```

The parsing and KB proposal steps are done by the subagent (Claude reads PDFs natively,
produces YAML directly). Python handles the mechanical token replacement and reporting.

---

## Implementation order

```
1. parse_asta_report.py + tests          (thin; token replacement + reporting)
2. cite-traverse.md                      (extract Steps 3–6 from lit-review;
                                          add "new types encountered" to synthesis)
3. lit-review.md refactor               (trim to Steps 0–2 + handoff)
4. asta-report-ingest.md                (new simplified orchestrator)
5. evidence-extraction.md               (complete stub — needed after cite-traverse)
6. justfile: ingest-report recipe       (no node_id arg)
7. WORKFLOW.md update
```

---

## Open questions

1. **Single subagent for parse + propose (Step 1)**: Using opus for the parsing +
   KB proposal step is expensive but appropriate — it requires judgment about which
   field each quote supports, which types to propose, and what the synthesis implies.
   Could split into: parse subagent (sonnet, mechanical) → propose subagent (opus).
   Depends on how reliably sonnet can extract the PDF structure.

2. **Quote boundary detection**: ASTA report uses italic text for quotes. Claude's
   native PDF reading should handle this; verify against the OLM PDF before writing
   the subagent prompt.

3. **CL as independent discovery**: For well-studied regions, CL may list types
   the report misses. Defer — use CL for anchoring only in this implementation.

4. **evidence-extraction.md gate count**: Two gates (weeding + expert review).
   Weeding gate may be skippable for OLM pilot (single well-studied type, known species).

5. **Multi-node cite-traverse**: Can one run cover multiple node_ids?
   Start with one node per run; extend if needed.
