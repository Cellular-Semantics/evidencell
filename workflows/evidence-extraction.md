# Evidence Extraction Orchestrator

> **STATUS: PENDING — M2 work**
> This orchestrator is not yet implemented. See `planning/ROADMAP.md §M2` for
> the full design. The stub below documents the intended structure.

---

## Purpose

Takes the output of `workflows/lit-review.md` (specifically `all_summaries.json`
and `paper_catalogue.json`) and extracts schema-compliant `LiteratureEvidence`
items for human review. This is the first end-to-end pipeline step from
"literature corpus" to "proposed KB YAML".

Entry point: run after completing `workflows/lit-review.md` and reviewing
`report.md`. The human has already pruned the paper catalogue at the gate in
lit-review Step 2.

---

## Intended steps

```
Step 0  Auto-flagging
        src/evidencell/flag_papers.py
        Scans paper_catalogue.json for species, developmental stage, disease
        context, and experimental system signals → paper_catalogue_flagged.json

Step 1  [GATE] Catalogue weeding
        Human reviews flagged catalogue (title, year, venue, auto-flags)
        Prunes irrelevant papers before extraction runs

Step 2  [OPTIONAL] Full-text sweep
        For flagged papers that are KEPT, call get_europepmc_full_text (EuropePMC,
        ~35-40% coverage) to confirm species/stage from Methods section.
        Updates evidence_scope fields on linked snippets.

Step 3  Extraction subagent
        all_summaries.json (filtered) + paper_catalogue_flagged.json +
        CellTypeNode context → proposed LiteratureEvidence YAML blocks
        Output: proposed_evidence_{node_id}.yaml

Step 4  [GATE] Expert review
        Expert reviews proposed LiteratureEvidence items.
        Approves, edits, or rejects each item.

Step 5  Append to KB
        Validated evidence items appended to kb/mappings/{region}/{graph}.yaml
```

---

## Key design decisions (from ROADMAP)

- **1:1 snippets per EvidenceItem** for traceability. Multiple snippets
  supporting the same claim = separate EvidenceItems on the same edge.
- **Extract from all_summaries.json, not report.md.** The report is synthesised
  prose; quotes from it are not verbatim from papers.
- **Snippet provenance check**: every proposed `LiteratureEvidence.snippet` must
  be a substring of the corresponding entry in `all_summaries.json`.
- **support judgment** (SUPPORT / PARTIAL / REFUTE) requires explicit node
  context in the prompt — the agent assesses whether the snippet supports the
  *specific mapping claim*, not the topic in general.
- **Expert review gate is non-negotiable** before KB commit.

---

## File layout (when implemented)

```
kb/{region}/traversal_output/{date}_{slug}/
  paper_catalogue_flagged.json
  proposed_evidence_{node_id}.yaml
```
