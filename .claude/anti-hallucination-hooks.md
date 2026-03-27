# Anti-hallucination hooks — implementation notes

*Current implementation. Updated as hooks are added or extended.*

This document is the reference for anyone modifying hook logic, validation sources, or
the `references.json` ingest path. Orchestrators should link to relevant sections when
giving correction-loop instructions to subagents.

---

## Architecture

```
Agent attempts Edit/Write
        │
        ▼
.claude/hooks/validate_mapping_hook.py   ← PreToolUse hook
        │
        ├─ KB YAML files (kb/**/*.yaml)
        │     → YAML parse validity
        │     → structural integrity (duplicate IDs, dangling edges, placeholder snippets)
        │     → quote_key existence in references.json
        │     → PMID/DOI existence in references.json
        │     → LinkML schema conformance (subprocess; skipped if schema absent)
        │
        └─ Report files (kb/**/reports/*.md)
              → unannotated blockquote detection
              → quote_key existence in references.json
              → PMID existence in references.json
              → ontology CURIE existence in term_index.json (if present)
              → atlas accession existence in sibling KB nodes (if discoverable)
        │
        ▼
Write proceeds if all checks pass; blocked with structured error if any fail.
```

Validation subagents in orchestrators (e.g. `gen-report.md` Step 4) provide a second
layer for LLM-synthesised content: they cross-check [n]/[A] labels, blockquotes, and
accessions against the facts file before the report is accepted.

---

## Validated content types

### Ontology terms (CL, UBERON, NCBITaxon, MBA, …)

**Storage format**
```yaml
name: "CA1 stratum oriens"
id: "UBERON:0014548"
name_in_source: "oriens layer of hippocampus CA1"   # verbatim from source document
```

**Check**
- `name` and `id` are consistent: OAK local DB lookup (`runoak info {id}`) confirms the
  label for `id` matches or is a synonym of `name`.
- `name_in_source` is a known label or synonym for `id` — catches substitution of a
  plausible-sounding name for a different concept.

**Verification source:** OAK local DB snapshots (`~/.data/oaklib/`).

**Status:** `name_in_source` storage is implemented in schema. OAK lookup in hook —
*not yet implemented*; currently checked interactively via `just qc` (linkml-term-validator).

---

### Gene symbols and IDs

**Storage format**
```yaml
symbol: "Chrna2"
ncbi_gene_id: 11440           # MGI or NCBI, species-specific
```

**Check**
- `symbol` resolves to `ncbi_gene_id` in the reference gene database.
- Gene symbols alone are not sufficient — the same symbol can refer to different genes
  across species (e.g. human CHRNA2 vs mouse Chrna2 have different NCBITaxon-scoped IDs).

**Verification source:** NCBI Gene (via API) or OAK HGNC/MGI adapter.

**Status:** Schema has `ncbi_gene_id` field. Hook check — *not yet implemented*.

---

### Publication IDs (PMID, DOI, corpus_id)

**Storage format (references.json)**
```json
{
  "corpus_id": "201041756",
  "pmid": "31420995",
  "doi": "10.1111/ejn.14606",
  "authors": ["Winterer J", "…"],
  "year": 2019,
  "title": "Single-cell RNA-Seq characterization of anatomically identified OLM interneurons…",
  "journal": "Eur J Neurosci"
}
```

**Check**
- Stored metadata (author, year, title) is consistent with the PMID/DOI.
- A PMID that resolves to a different paper than the stored author/year is a hallucinated
  citation.

**Verification source:** Local `references.json` for cross-field consistency; Europe PMC
API for initial ingest validation.

**Status:** Metadata storage implemented. Hook consistency check — *not yet implemented*.
Initial ingest validation done manually or via `just add-ref` (planned).

---

### Verbatim quotes

**Storage format**
```yaml
# In KB YAML (marker source or edge evidence):
quote_key: 201041756_bd56f851

# In references.json:
{
  "corpus_id": "201041756",
  "quotes": {
    "201041756_bd56f851": {
      "text": "as well as expression of Chrna2, which has been used as a marker for hippocampal OLM interneurons",
      "section": "Results 3.3",
      "claims": ["chrna2_positive"]
    }
  }
}
```

The key format is `{corpus_id}_{hash8}` where `hash8` is the first 8 hex characters of
the SHA-256 of the normalised quote text. This makes keys content-addressed: a modified
quote produces a different key and fails the lookup.

**Check**
- `quote_key` exists in `references.json[corpus_id].quotes`.
- The referenced `text` field is present (non-empty).
- For report synthesis: `render.py` raises `KeyError` on a missing key, preventing the
  report from being written with a fabricated quote.

**Verification source:** Local `references.json` — sufficient because the provenance chain
is YAML → `references.json` → report with no LLM in the loop at render time.

**Status:** Implemented. Hook checks key existence before write; `render.py` raises on
missing key at render time.

---

## Markdown report annotation standard

Reports in `kb/**/reports/*.md` embed machine-readable annotations so the hook can
validate identifiers without parsing prose. The principle: IDs that are reader-relevant
appear as visible bracket notation; content-addressed hashes that carry no meaning
to a reader appear as hidden HTML comments.

### Summary

| Content | Visible in report | Hidden | Hook parses |
|---|---|---|---|
| Blockquote source | `> — Author et al. Year, §section · [n]` attribution line | `<!-- quote_key: X -->` | HTML comment regex |
| Ontology terms | `Name [PREFIX:ID]` | — | `\[[A-Z]+:\d+\]` |
| Atlas accessions | `Name [CS…ID]` | — | `\[CS[A-Z0-9_]+\]` |
| PMIDs | reference table rows with PubMed links | — | pubmed URL regex |
| Gene symbols | symbol in text/table | — | (future: gene_index.json lookup) |

### Blockquote pattern

Every blockquote block must contain an attribution line with a `quote_key` comment:

```markdown
> verbatim quote text
> — Winterer et al. 2019, Results §3.3 <!-- quote_key: 201041756_aabb1234 -->
```

- The attribution line (`> — ...`) is for readers: miniref and numbered citation
- `<!-- quote_key: X -->` is for the hook: `parse_md_annotations()` extracts it with
  `<!--\s*quote_key:\s*(\S+)\s*-->`
- A blockquote block (consecutive `>` lines) with no `quote_key` comment in any line
  is flagged as unannotated and blocks the write

`render.py` emits this pattern automatically for programmatic drill-down output.
For synthesis-agent-authored summaries, rules 6–8 in `gen-report.md` enforce it.

### Ontology and accession brackets

`render.py` automatically appends brackets where IDs are available:
- Anatomical location: `CA1 stratum oriens [UBERON:0014548]`
- Atlas cluster: `0769 Sst Gaba_3 [CS20230722_CLUS_0769]`

The hook extracts these with `parse_md_annotations()` and checks:
- CURIEs against `term_index.json` (silently skipped if absent)
- Accessions against sibling KB YAML nodes (silently skipped if not discoverable)

---

## Contamination rules for validated stores

These rules apply during any agentic curation or synthesis session:

**`references.json`**
- READ freely from any agent or tool.
- WRITE only through the validated ingest path. Direct edits to `references.json` are
  prohibited — the ingest path enforces content-hash keying and metadata consistency.
- During report synthesis (`render.py`, `gen-report.md` orchestrator), `references.json`
  must not be modified. If a quote key is missing, the correct fix is to add the quote
  through ingest, then re-run `just gen-facts`.

**OAK local DB snapshots**
- READ freely.
- Do not update the local ontology DB in the same session as KB writes. A mid-session
  update could change term labels and invalidate checks already performed.

**`kb/mappings/` (canonical KB)**
- Never write directly. Graduate from `kb/draft/` via `just qc` then curator approval.

---

## Adding new validation checks

When adding a new validated content type:

1. Define the storage format in `schema/evidencell.yaml`
2. Implement the check function in `src/evidencell/validate.py`
3. Register the check in `.claude/hooks/validate_mapping_hook.py`
4. Add a test to `tests/test_hook_integration.py`:
   - valid input → hook exits 0
   - invalid input (bad ID, missing quote key, etc.) → hook exits 2 with structured error
5. Add the content type to the table in CLAUDE.md § Anti-hallucination mechanisms
6. Update the Status line in this document

---

## Correction loop protocol (for curation orchestrators)

When a hook rejects a write, the correction loop is:

1. Read the structured error output from the hook (JSON on stderr).
2. Identify the failing field and the check that failed.
3. Fix the source content (YAML field, quote key, ID) — do not edit the validated store.
4. Re-attempt the write. The hook will re-run automatically.
5. If the fix requires adding a new entry to `references.json` (missing quote key),
   add it through the validated ingest path and re-run `just gen-facts` to update the
   facts file before retrying synthesis.

Limit correction attempts to 2 before escalating to the curator. Repeated failures
usually indicate a data quality issue upstream, not a transient error.
