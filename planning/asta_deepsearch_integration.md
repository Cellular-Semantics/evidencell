# Asta Deepsearch Integration Plan

> **Date**: 2026-03-08
> **Context**: Planning session discussion — how the Asta_deepsearch literature workflow integrates into the evidencell CellTypeEvidence KB as a local deepsearch component.

---

## 1. Strategic Direction

The original plan was a local [paperqa2](https://github.com/whitead/paper-qa) implementation (`Asta_deepsearch/paperqa2_cyberian/`). The preferred approach is now **ASTA-based**, taking advantage of:

- Vectorised snippet search (`snippet_search` with `paper_ids` scoping)
- Easy citation traversal via `refMentions` in snippet annotations
- Massive Semantic Scholar corpus without local PDF management

The paperqa2/Cyberian backend remains in the repo as a working prototype but is not the primary path forward.

**Alternative input modes** (not requiring the local workflow):
- Drop in pre-run deepsearch text (e.g. from a Perplexity/Falcon-style external provider)
- Call deepsearch via an upstream API

The local ASTA workflow is the preferred option when available; others are fallbacks.

---

## 2. Entry Points

Two distinct entry points into the evidence accumulation pipeline, with different purposes:

| Entry point | Trigger | Output |
|---|---|---|
| **Topic / literature review** | "What is known about [cell type]?" | Broad evidence base, report, paper catalogue |
| **Specific mapping assertion** | "Find evidence for [type A] = [type B]" | Targeted evidence items for a specific KB edge |

These are **not** the same workflow. The mapping assertion entry point is a later, more focused operation that may reuse the corpus already built by a topic review.

---

## 3. Three-Phase Workflow

For the topic entry point, evidence accumulation proceeds in three phases that share a persistent session directory.

### Phase 1 — Literature Review

Run `Asta_deepsearch/workflows/lit-review.md` as-is.

**Inputs**: topic / cell type name, optional parameter overrides
**Outputs**: `traversal_output/{date}_{slug}/` containing:
- `seeds.json`, `paper_catalogue.json`, `all_summaries.json`
- `depth_N_snippets.json`, `depth_N_summaries.json`, `depth_N_refs.json`
- `report.md`
- `run_config.json`, `run_manifest.json`

**Human gates**:
1. Seed approval (Step 2 in lit-review.md) — approve/prune the discovered seed papers before traversal begins
2. Catalogue review — after traversal, before synthesis: present `paper_catalogue.json` as a curated list (title, year, venue, abstract excerpt) for lightweight paper weeding. Pruned papers have their snippets excluded from synthesis and downstream KB extraction.

The catalogue gate is lighter than reading the full report — it's just a list of titles to approve, identical in style to the seed gate.

### Phase 2 — Mapping Hypothesis Generation

Two inputs feed this phase:
- Phase 1 output (`all_summaries.json`, `paper_catalogue.json`)
- Independent snippet searches targeting **property combinations** (marker genes, morphology, NT type, spatial location, ephys characteristics) scoped to the catalogue papers

A mapping extraction agent reads this combined evidence and proposes:
- `CellTypeNode` entries for newly identified cell types
- `MappingEdge` candidates with relationship type and confidence
- `LiteratureEvidence` items (one per supporting snippet, with verbatim quote)

**Human gate**: Expert reviews proposed mapping edges and evidence items before they are committed to the KB YAML.

### Phase 3 — Cross-Validation and Extension

For each proposed mapping node that has a counterpart in another taxonomy (e.g. a WMBv1 supertype or HMBA cluster):

1. Pull any existing annotation transfer results → `AnnotationTransferEvidence`
2. Check `paper_catalogue.json` for whether the atlas papers are already in the corpus
3. If not: run citation chains from those atlas papers (same traversal subagent, scoped to new IDs only)

The visited set from Phase 1 (`paper_catalogue.json`) prevents redundant traversal. Phase 3 only fetches what Phase 1 missed.

---

## 4. Evidence Scope Metadata

A recurring problem in real search results: evidence that is superficially relevant but comes from the wrong biological context. Known categories:

| Scope field | Values | Risk level |
|---|---|---|
| `species` | `human`, `mouse`, `rat`, `NHP`, `in_vitro`, ... | Cross-species: use with caution |
| `developmental_stage` | `adult`, `postnatal_early`, `postnatal_late`, `embryonic`, ... | Stage mismatch: likely invalid unless asserting lineage |
| `biological_context` | `normal`, `disease`, `injury`, `genetic_model` | Disease-state: needs explicit justification |
| `experimental_system` | `in_vivo`, `organoid`, `acute_slice`, `cell_line`, `dissociated_culture` | In vitro: treat with caution |

These fields should be populated on each `EvidenceItem` during the KB extraction step. ASTA snippets often carry enough context to infer them from the text, or the paper metadata (venue, title, abstract) provides signals.

Two levers for managing scope noise:

**At query time (upstream)**: Targeted ASTA queries (e.g. `"GPi shell neuron human adult"`) naturally reduce cross-species/cross-stage noise. Not perfect, but cheaply reduces review burden.

**At evidence item level (downstream)**: Structured `scope` metadata on each `EvidenceItem` lets experts make informed judgments without re-reading the source. A `flagged` boolean + `flag_reason` string allows items to be excluded from mapping confidence calculations without deleting the provenance.

---

## 5. Auto-Flagging and Full-Text Validation Sweep

### Auto-flagging agent

After `paper_catalogue.json` is built (end of Phase 1 traversal), a lightweight agent scans paper metadata for scope red-flag signals:

- Model organism venue / journal
- Organoid / in vitro keywords in title or abstract
- Developmental biology context
- Disease cohort keywords

Output: `paper_catalogue_flagged.json` — same structure as `paper_catalogue.json` with an added `scope_flags: []` field per paper, and linked `all_summaries.json` snippets updated with `auto_flagged: true`.

This happens before synthesis so flagged papers can be handled in the catalogue weeding gate.

### Full-text validation sweep (optional, targeted)

For papers flagged as potentially problematic, a targeted full-text validation sweep can resolve ambiguity that snippets alone cannot. The `get_europepmc_full_text` MCP tool is available for this purpose — it is explicitly excluded from the core traversal for cost/scale reasons, but appropriate here because:

- Scope is small (only flagged papers)
- The specific question is narrow (read methods section, confirm species/stage/preparation)
- Full text is available via EuropePMC for ~35–40% of neuroscience papers

The sweep updates `scope_fields` on affected evidence items and adds a `validation_source: "full_text"` provenance flag.

---

## 6. Session Directory Structure

Each cell type / mapping topic has a persistent session directory. Phases append to it rather than creating separate outputs.

```
kb/
  {region}_{cell_class}/
    mappings.yaml                    ← schema-compliant KB (source of truth)
    traversal_output/
      {YYYYMMDD}_{topic_slug}/       ← Phase 1 lit-review output
        run_config.json
        run_manifest.json
        seeds.json
        paper_catalogue.json
        paper_catalogue_flagged.json ← auto-flagging output
        all_summaries.json
        depth_N_*.json
        report.md
      phase2_snippets/               ← Phase 2 property-combination searches
        {property_query_slug}.json
      annotation_transfer/           ← Phase 3 annotation transfer evidence
        {dataset_id}.json
```

The `traversal_output/` directory is the deepsearch working directory; `mappings.yaml` is the KB. They are peers under the same cell type directory.

Whether a single shared corpus (e.g. all cerebellar cell types sharing one traversal run) or per-cell-type corpora are more practical depends on the breadth of the review. Reviews covering a whole region (e.g. a cerebellar atlas paper) should be shared; targeted cell-type reviews can be per-type. `paper_catalogue.json` serves as the visited-set to prevent redundant traversal across runs.

---

## 7. Relationship to dismech Patterns

Key patterns from dismech that apply directly:

| dismech pattern | Our adaptation |
|---|---|
| Pre-edit validation hook blocks invalid YAML | Same hook for `kb/*/mappings.yaml` |
| Exact-quote requirement (anti-hallucination) | ASTA snippet text as verbatim quote; full-text validated when flagged |
| Three-layer validation (schema → terms → references) | Schema + ontology terms + ASTA corpus ID provenance |
| Skills as reusable prompt libraries | Domain skills: `map-cell-type`, `fetch-literature`, `extract-evidence` |
| Human-in-loop at PR review stage | Earlier gates: seed approval, catalogue weeding, mapping review |
| `run_manifest.json` audit trail | Already present in lit-review.md; extend to mapping extraction step |

Key difference from dismech: dismech synthesis is delegated to an external provider (Falcon/Perplexity). Our ASTA-based approach keeps the full provenance chain in-house — snippet → summary → evidence item — which enables stronger validation.

---

## 8. Open Questions

1. **Weeding granularity**: Should post-traversal catalogue weeding operate at paper level only, or also at snippet level within a kept paper? Paper-level is much lighter; snippet-level gives finer control but may be too onerous in the general case. Likely: paper-level as default, snippet-level available as an expert tool for reviewing specific evidence chains.

2. **Schema extension for scope metadata**: The current `EvidenceItem` schema (v0.3) does not yet have `species`, `developmental_stage`, `biological_context`, `experimental_system`, or `flagged` fields. These need adding before the extraction agent can be built.

3. **Mapping extraction agent design**: The transition from `all_summaries.json` to proposed KB YAML is the most complex step. The agent needs to know what mapping assertion is being evidenced (requiring mapping context to be passed in), and must assign `support` judgment per snippet. This is the primary design task for Phase 2.

4. **Shared vs per-type corpora**: Decision depends on how broad the first real review will be. Deferring until the first test run.
