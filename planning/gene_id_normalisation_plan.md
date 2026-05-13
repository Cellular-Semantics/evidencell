# Gene symbol & ID normalisation for taxonomy nodes

## Context

Taxonomy YAML under `kb/taxonomy/{id}/*.yaml` currently stores markers as bare
gene symbol strings (`{symbol: Apod, category: DEFINING}`) — see
`src/evidencell/taxonomy_db.py:677-682`. The schema's `GeneDescriptor`
(`schema/celltype_mapping.yaml:646-701`) already defines an optional
`ncbi_gene_id` (CURIE) slot for species-stable IDs, and a comment in that block
points to NCATS Translator NodeNormalization as the intended resolver. None of
this is wired up at ingest time.

Goals:

1. Normalise raw symbols (handle case, "PV Neuropeptide" → `Pvalb`, etc.).
2. Populate `ncbi_gene_id` on every marker GeneDescriptor in taxonomy YAML.
3. Plumb into the standard taxonomy ingest path so it runs by default when a
   gene reference is configured, but **skips cleanly** when none is available.
4. Be flexible about reference source: prefer MapMyCells-derived
   Ensembl↔symbol files when present, but allow other sources (and no source).

A related (still-open) dev request,
`planning/dev_requests/2026-04-28_taxonomy-ensembl-mapping-fetch.md`, already
proposes the `external_resources.ensembl_gene_mapping` slot on
`TaxonomyMeta`. This plan extends/consumes that.

## Approach

### 1. Gene reference abstraction

Introduce `src/evidencell/gene_reference.py` with a small interface:

```python
class GeneReference:
    def lookup(self, symbol: str) -> GeneRecord | None: ...
    def fuzzy_lookup(self, symbol: str) -> list[GeneRecord]: ...
    @property
    def species(self) -> str: ...
```

`GeneRecord` carries `symbol_canonical`, `ensembl_id`, `synonyms`, and
optionally `ncbi_gene_id` (when it can be resolved without a network call).

Loaders:

- `EnsemblTsvReference.from_taxonomy(meta)` — reads the Ensembl↔symbol TSV
  pointed to by `external_resources.ensembl_gene_mapping.local_cache` (existing
  `conf/gene_mapping_{taxonomy}.tsv`, currently consumed by
  `taxonomy_ops.load_gene_mapping` at `src/evidencell/taxonomy_ops.py:117-131`).
  Builds case-insensitive symbol index + reverse synonym index by also pulling
  MyGene synonyms when refreshing.
- `NullGeneReference` — used when no source is configured; `lookup` always
  returns `None` so callers degrade gracefully.

Selection rule (in one helper, `load_gene_reference(taxonomy_meta)`):
- If `external_resources.ensembl_gene_mapping.local_cache` resolves and the
  file exists → `EnsemblTsvReference`.
- Else if a MapMyCells `marker_genes.json` is configured but no symbol mapping
  → log "Ensembl IDs available but no symbol bridge; skipping gene
  normalisation" and return `NullGeneReference` (don't guess).
- Else → `NullGeneReference`.

### 2. NCBI ID resolution via Translator NodeNormalization

Add `src/evidencell/gene_id_resolver.py`:

- `resolve_ncbi_ids(ensembl_ids: list[str], species: str) -> dict[str, str]`
  — POSTs to `https://nodenormalization-sri.renci.org/get_normalized_nodes`
  with `curie=ENSEMBL:ENSMUSG…` batches; parses out `NCBIGene:…` from the
  equivalent_identifiers list. Cached on disk per-taxonomy under
  `conf/gene_id_cache_{taxonomy}.tsv` (gitignored).
- One-shot: run once per taxonomy at fetch time; results merged into the
  GeneReference index. Falls back gracefully if endpoint is unreachable
  (warning, leaves `ncbi_gene_id` empty rather than failing ingest).

This sits behind the same "skip if no reference" gate.

### 3. Symbol normalisation step

Add `normalise_markers(markers, gene_ref)` in `gene_reference.py`. For each
`{symbol, category}` entry:

1. Direct lookup (case-insensitive, ignore trailing whitespace, strip
   `(Mmus)` suffix and `ensembl:` prefix if present).
2. Fuzzy match (Jaro–Winkler against canonical symbols + synonyms;
   accept ≥0.95).
3. On match → replace `symbol` with canonical symbol, set `ensembl_id` and
   `ncbi_gene_id` if known; original goes into `synonyms` if it differs.
4. On no match → leave symbol untouched, append to a per-taxonomy
   `gene_normalisation_log.tsv` (raw symbol, category, source node, reason).

**No LLM API calls are made from inside the ingest code.** The unresolved
log is the handoff surface: a curating agent (e.g. invoked through a
workflow/skill) can read the log, propose canonical mappings using its own
latent knowledge — e.g. "PV Neuropeptide" → `Pvalb` — validate each proposal
against the gene reference, and then either:

- write the resolved mappings back to a per-taxonomy
  `gene_normalisation_overrides.tsv` (consulted as a first pass on subsequent
  ingest/reingest runs), or
- directly correct the offending source field before reingest.

This keeps `src/` free of LLM-provider dependencies and gives the orchestrator
agent full control over fallback semantics, prompts, and review.

### 4. Plumbing into ingest

Two integration points, in
`src/evidencell/taxonomy_db.py` and `src/evidencell/taxonomy_ops.py`:

- In the YAML-emit path (`taxonomy_db.py` around line 677 where the unified
  `markers` list is built), call `normalise_markers(markers, gene_ref)` if
  `gene_ref` is non-null. Wire `gene_ref` through from a single load at the
  top of `ingest_taxonomy_db`.
- In `taxonomy_ops.reingest` (preserves enrichments): after re-ingest, run
  the same normalisation pass on each node's markers. Idempotent.
- The normalisation step consults `gene_normalisation_overrides.tsv` (if
  present) before the direct/fuzzy lookups, so curator-supplied mappings
  from the agent-driven fallback persist across reingest.
- New justfile recipe `just normalise-genes {taxonomy_id}` for one-off use
  on existing taxonomies (also used as a sub-step internally).

When `gene_ref` is `NullGeneReference`, the ingest path logs once
("no gene reference configured for taxonomy X; markers stored as raw
symbols") and proceeds unchanged — preserves current behaviour for
taxonomies without a MapMyCells/Ensembl mapping.

### 5. Schema

`GeneDescriptor.ncbi_gene_id` already exists. Two small additions:

- Add `synonyms: list[str]` slot to `GeneDescriptor` for the original
  symbol(s) when normalisation rewrites the canonical form.
- Add `external_resources.ensembl_gene_mapping` to `TaxonomyMeta` per the
  open dev request (treat that as a prerequisite).

## Files touched

| File | Change |
|---|---|
| `src/evidencell/gene_reference.py` | NEW — `GeneReference`, `EnsemblTsvReference`, `NullGeneReference`, `normalise_markers` |
| `src/evidencell/gene_id_resolver.py` | NEW — Translator NodeNormalization client + on-disk cache |
| `src/evidencell/taxonomy_db.py` | Call `normalise_markers` in YAML emit path (~L677) |
| `src/evidencell/taxonomy_ops.py` | Reuse in `reingest`; share `load_gene_reference` helper |
| `schema/celltype_mapping.yaml` | Add `synonyms` to `GeneDescriptor` |
| `schema/taxonomy_meta.yaml` (or wherever `TaxonomyMeta` lives) | Add `external_resources.ensembl_gene_mapping` (per existing dev request) |
| `justfile` | `just normalise-genes {taxonomy_id}`; assumes `fetch-gene-mapping` from the dev request has landed |
| `kb/taxonomy/CCN20230722/taxonomy_meta.yaml` | Backfill `external_resources` block |
| `workflows/ingest-taxonomy.md` | Add a post-ingest step pointing the orchestrating agent at `gene_normalisation_log.tsv` for review + override curation |

## Out of scope

- Fetching the ROBOT template / building the canonical Ensembl↔symbol TSV
  (covered by `planning/dev_requests/2026-04-28_taxonomy-ensembl-mapping-fetch.md`
  — this plan **consumes** it).
- Changes to KB graph YAML (`kb/graphs/**`) marker entries — this plan only
  normalises taxonomy nodes. Graph normalisation can reuse the same module
  later.
- Cross-species ortholog mapping. Translator can do it, but we restrict
  to species-of-the-taxonomy resolution here.
- In-code LLM provider calls. Natural-language → canonical-symbol resolution
  is delegated to the orchestrating agent via the unresolved log.

## Verification

1. `uv run pytest tests/test_gene_reference.py` — unit tests for direct and
   fuzzy normalisation; null-reference passthrough; override-TSV
   precedence; Translator client with VCR-recorded fixtures.
2. End-to-end on CCN20230722:
   - `just fetch-gene-mapping CCN20230722` (after dev request lands)
   - `just reingest CCN20230722` and diff a few nodes in
     `kb/taxonomy/CCN20230722/cluster.yaml` to confirm `ncbi_gene_id`
     populated and canonical symbols applied.
   - Inspect `gene_normalisation_log.tsv`; expect zero unresolved DEFINING
     markers and a small set of NEUROPEPTIDE/natural-language entries for
     agent-driven review.
3. Override round-trip: hand-write an entry in
   `gene_normalisation_overrides.tsv` (e.g. `PV Neuropeptide → Pvalb`),
   reingest, and confirm the override is applied and the entry no longer
   appears in the unresolved log.
4. Negative test: a taxonomy with no `external_resources` block ingests
   unchanged; warning is logged once; markers remain raw symbols.
5. CL/anti-hallucination hook still passes on the resulting YAML.

## Open questions

- Where to write the unresolved log + overrides TSV — `conf/`, `research/`,
  or alongside the taxonomy under `kb/taxonomy/{id}/`? Leaning toward
  `kb/taxonomy/{id}/` so the override file travels with the taxonomy in
  git, while the log file is gitignored.
