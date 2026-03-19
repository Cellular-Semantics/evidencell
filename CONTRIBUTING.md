# Contributing to evidencell

evidencell is a community-curated knowledge base. Contributions take two forms:
new mapping graphs (a brain region not yet in the KB) and additions or
corrections to existing graphs.

Curation in evidencell is a **guided agentic workflow**. You work with
[Claude Code](https://claude.ai/claude-code) as a co-curator: the agent handles
literature search, evidence extraction, and schema-compliant YAML drafting; you
provide the biological expertise and hold the review gates. Support for other AI
coding assistants may be added in future.

---

## Prerequisites

```bash
# Install Claude Code
# https://claude.ai/claude-code

# Install just (task runner)
brew install just           # macOS
# or: https://just.systems/man/en/chapter_4.html

# Install uv (Python package manager)
brew install uv
# or: https://docs.astral.sh/uv/getting-started/installation/

# Clone and install
git clone https://github.com/your-org/evidencell
cd evidencell
just install

# Prime OAK ontology databases (one-time, large download)
just fetch-oak-dbs
```

Open the repo as a Claude Code project. The pre-edit validation hook activates
automatically for any edits to `kb/`.

---

## Adding a new mapping entry

See `WORKFLOW.md` for the complete pipeline. Each step is an orchestrator you
run in Claude Code — tell Claude which workflow to follow, provide the inputs,
and review the output at each gate before proceeding.

```
workflows/ingest-taxonomy.md             # parse atlas data → CellTypeNode stubs
# [GATE] review + correct field mapping; review generated stubs

workflows/lit-review.md                  # build literature evidence corpus
# [GATE] review paper list, prune catalogue

workflows/evidence-extraction.md         # extract LiteratureEvidence items
# [GATE] review proposed evidence items

workflows/map-cell-type.md               # propose MappingEdge + confidence
# [GATE] review proposed edges
```

Nothing is written to `kb/mappings/` without passing validation and your
sign-off. Claude does not proceed past a gate autonomously.

---

## Graduating a draft entry to canonical

An entry in `kb/draft/` graduates to `kb/mappings/` when:

1. Schema validation and OAK term checks pass
2. Every `MappingEdge` has ≥1 `EvidenceItem`
3. Every node has a `cell_ontology_term` (at minimum a broad CL mapping)
4. Confidence assessments have been reviewed by a domain expert

Ask Claude to graduate the entry: it will run the validators, fix any remaining
issues, and move the file when all checks pass.

---

## Opening a PR

```bash
git checkout -b add-{region}-{type}
git add kb/mappings/{region}/{file}.yaml
git commit -m "Add {cell type} mapping for {region}"
git push origin add-{region}-{type}
# open PR on GitHub
```

PR checklist (automated review checks these):
- [ ] Schema validation passes
- [ ] Every `MappingEdge` has ≥1 `EvidenceItem` with a verbatim snippet
- [ ] Every node has a CL term
- [ ] Confidence rationale documented for HIGH-confidence edges
- [ ] No invented ontology IDs

---

## Schema questions and novel fields

If you have data that doesn't fit the current schema — an extra column from your
atlas, a field type we haven't anticipated — open an issue rather than inventing
a workaround. The `ingest-taxonomy` workflow preserves unrecognised fields as
YAML comments and flags potential schema candidates; these are the signal for
schema evolution discussions. The schema is actively developed.
