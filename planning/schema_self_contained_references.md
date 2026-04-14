# Proposal: Self-contained KB graphs with inline references

## Problem

KB YAML files depend on an external `references/{region}/references.json` sidecar for
quote text and publication metadata. This creates:
- Path coupling (hooks, renderer, orchestrators all need to resolve the sidecar)
- Confusion about what's infrastructure vs research artifact
- Files that can't be read standalone

## Design principles

1. **KB YAML is self-contained** — every quote cited as evidence is inline; every cited
   paper has metadata in the file. Reading one YAML gives the full picture.
2. **The bulk quote store is a research artifact** — ASTA report ingest extracts hundreds
   of quotes before KB nodes exist. This store lives in `research/` as a mineable pool,
   not as KB infrastructure.
3. **Full text stays in `references_cache/`** — one markdown file per paper (like dismech),
   used for post-hoc snippet verification.

## Proposed schema additions

### On `CellTypeMappingGraph`

```yaml
references:
  multivalued: true
  inlined_as_list: true
  range: PublicationReference
  description: >
    Metadata for every publication cited in this graph's evidence items.
    Populated during evidence-extraction; verified against Europe PMC at ingest.
```

### New class: `PublicationReference`

```yaml
PublicationReference:
  description: >
    Metadata for a cited publication. Keyed by PMID or DOI.
    Inspired by dismech PublicationReference but without findings
    (findings are the evidence items themselves).
  attributes:
    reference:
      required: true
      identifier: true
      pattern: "^(PMID:[0-9]+|DOI:.+)$"
    title: {}
    authors:
      multivalued: true
    year:
      range: integer
    journal: {}
    doi: {}
    pmid: {}
    corpus_id:
      description: Semantic Scholar corpus ID (links back to ASTA/research quote store)
```

### Changes to evidence items

No schema changes needed — `snippet` already exists on `PropertySource` and
`LiteratureEvidence` and is the right place for inline quotes.

`quote_key` is **retained but optional** — it becomes an annotation linking back to
the research quote store for provenance, not the primary mechanism for quote lookup.
The hook and renderer read `snippet` directly; `quote_key` is informational.

## Migration path

### Phase A: Add `PublicationReference` to schema

- Add the class and `references` slot to `CellTypeMappingGraph`
- Populate from existing `references.json` metadata for papers actually cited
  in evidence items (not the full bulk store)
- No breaking change — new optional field

### Phase B: Ensure all cited evidence has inline `snippet`

- For evidence items that only have `quote_key` (no `snippet`), dereference the
  quote from `references.json` and inline it
- After this, every evidence item has its snippet inline

### Phase C: Shift hook and renderer to read inline

- Hook validates `snippet` text directly (not via quote_key → references.json lookup)
- Renderer reads `snippet` from evidence items and `references` from the graph
- `references.json` is no longer required infrastructure

### Phase D: Move `references.json` to `research/`

- `references/{region}/references.json` → `research/{region}/references.json`
- It's now purely a mineable research artifact for future evidence-extraction
- ASTA report ingest continues to write here; evidence-extraction reads from here
  and inlines into KB YAML

### Phase E: Add `references_cache/` verification (like dismech)

- One markdown file per paper with frontmatter metadata + full text
- Post-hoc validator checks `snippet` is a literal substring of cached text
- Replaces content-hash verification with direct substring matching

## What stays, what goes

| Component | Current role | Future role |
|---|---|---|
| `references.json` | Required KB infrastructure | Research artifact in `research/` — ASTA quote mine |
| `quote_key` | Primary quote lookup mechanism | Optional provenance annotation |
| `snippet` (inline) | Optional if quote_key set | Required on all evidence items |
| `references_cache/` | Exists but underused | Full-text store for snippet verification |
| `PublicationReference` | Does not exist | Schema-specified metadata on graph |

## ASTA ingest compatibility

ASTA report ingest extracts quotes in bulk before KB nodes exist. This workflow
is preserved:

1. ASTA ingest → writes `research/{region}/references.json` (bulk quote store)
2. Evidence-extraction reads from quote store, selects relevant quotes
3. Evidence items get inline `snippet` + optional `quote_key` back-reference
4. `PublicationReference` entries added to graph for cited papers

The bulk store remains available for future mining passes — new evidence-extraction
runs can pull additional quotes without re-running ASTA ingest.

## Ingest provenance on the quote store

Currently `references.json` merges quotes from multiple ASTA reports (e.g. OLM
report + broader GABAergic report) into one file with only `_meta.last_updated_by`
recording the most recent write. This loses the provenance chain — you can't tell
which report contributed which quotes without forensics.

### Fix: per-quote `ingested_by` + per-file `ingest_log`

Each quote entry gains an `ingested_by` field recording which workflow run added it:

```json
{
  "201041756": {
    "corpus_id": "201041756",
    "pmid": "31420995",
    "quotes": {
      "201041756_bd56f851": {
        "text": "as well as expression of Chrna2...",
        "section": "Results 3.3",
        "claims": ["chrna2_positive"],
        "ingested_by": "OLM_Neurons_asta_report/step2"
      }
    }
  }
}
```

The `_meta` block gains an `ingest_log` recording every write:

```json
{
  "_meta": {
    "region": "hippocampus",
    "ingest_log": [
      {"run": "OLM_Neurons_asta_report/step2", "date": "2026-04-08T...", "quotes_added": 120},
      {"run": "hippocampus_GABAergic_neurons/step2", "date": "2026-04-09T...", "quotes_added": 80}
    ]
  }
}
```

This is cheap to implement (one field per quote, one list in `_meta`) and makes
the merge history transparent. The `asta-report-ingest.md` Step 2 merge protocol
just needs to stamp `ingested_by` on new quotes and append to `ingest_log`.

When quotes are later inlined into KB evidence items, `ingested_by` traces back
to the source report — closing the provenance loop from ASTA PDF → quote store →
KB evidence → rendered report.

## Relationship to dismech

Converges with dismech pattern: inline snippets, top-level `references:` list,
`references_cache/` for verification. Key differences: we retain the bulk quote
store as a research artifact because our ASTA ingest pipeline produces it and
it has ongoing value; we add ingest provenance tracking that dismech doesn't need
(dismech writes evidence items one-at-a-time, not via bulk ingest).
