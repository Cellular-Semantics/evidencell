# Paper-style reports — pipeline review and POC scope

**Date:** 2026-04-29
**Branch:** `paper-style-reports`
**Goal:** restructure mapping reports into a paper-like form (Intro / Results / Methods / Discussion) suitable for screenshots in a short paper on evidencell. Demo on **OLM** and **vmhvl_esr1_pr_neuron** as worked examples.

This doc is the entry point for the POC. It maps the existing pipeline section-by-section, calls out what is deterministic vs LLM, identifies the gap (Methods) that the new structure introduces, and scopes the figure question.

---

## 1. Existing pipeline architecture

```
KB YAML (kb/draft/{region}/...yaml, kb/datasets/, kb/correlation_runs/)
        │
        │  (1) Fact extraction — DETERMINISTIC
        │      python -m evidencell.render facts {graph} --node {node_id}
        │      src/evidencell/render.py:extract_node_facts() (~600 lines)
        ▼
reports/{region}/{node_id}_facts.json     (gitignored intermediate)
        │
        │  (2) Synthesis — LLM SUBAGENT
        │      Prompt: workflows/gen-report.md Step 3 (~370 lines of prose rules)
        │      Reads facts JSON → writes Markdown
        ▼
reports/{region}/{node_id}_summary.md     (the deliverable)
        │
        │  (3) Validation — DETERMINISTIC + LLM SUBAGENT
        │      Pre-write hook: .claude/hooks/validate_mapping_hook.py
        │        (blockquote attribution, accession existence, refs.json)
        │      Validation subagent: workflows/gen-report.md Step 4
        │        (LLM cross-checks every claim against facts JSON)
        ▼
{accepted | rejected}
```

**Two-layer pattern: structural integrity is deterministic, prose is LLM.**

| Concern | Layer | File |
|---|---|---|
| Reference index, [n] labels | Deterministic | `render.py:build_reference_index()` |
| Quote collection from references.json | Deterministic | `render.py:_collect_quotes()` |
| Run_ref → publication PMID resolution | Deterministic | `render.py:_resolve_run_ref_to_pmid()` (recent) |
| Section-by-section prose | LLM | `workflows/gen-report.md` Step 3 prompt |
| Headline framing, biological interpretation | LLM | (same) |
| Anti-hallucination (CURIE/accession/quote_key) | Deterministic | `validate.py:parse_md_annotations()`, hook |
| Cross-checking text against facts | LLM | `workflows/gen-report.md` Step 4 prompt |

The synthesis prompt (Step 3) is itself ~370 lines of structured instructions — it dictates section order, table schemas, attribution rules, what to derive from which facts field. It is closer to a templating language with LLM fill-in than free-form generation.

---

## 2. Current report sections → paper sections

Existing reports already follow a recognisable scientific structure. Most of the restructuring is renaming and resequencing rather than new content.

| Paper section | Current report content | Source(s) | Mode | Gap |
|---|---|---|---|---|
| **Title + Abstract** | Title; first paragraph after Header | classical_node.name, primary mapping verdict | LLM | Add a 3-sentence abstract |
| **Introduction** | Section 3 "Classical type table" + literature `<details>` fold | classical_nodes[0], LITERATURE quotes from references.json | Mixed | Add 1-2 paragraphs of biological framing (currently only as table rows) |
| **Results** | Section 4a/4b (mapping candidates + property alignment + Evidence support) + Section 5 (Candidate paragraphs) | edges[*], property_comparisons, evidence_items | LLM with deterministic table population | Already substantial; add figures |
| **Methods** | **NOT PRESENT** | — | — | New section. Most content already exists in KB; needs a synthesis path |
| **Discussion** | Section 7 "Open questions" + Section 6 "Proposed experiments" | edges[*].unresolved_questions, proposed_experiments | LLM | Reframe; add explicit "best candidate + caveats" summary |
| **References** | Section 9 References table | reference_index | Deterministic | OK as-is |

The **Methods** section is the only genuinely new piece. The rest is reorganisation and minor expansion.

---

## 3. Methods section — what would flow in

The Methods section is the framework's audit trail made visible. It should be **mostly deterministic** — pull from already-structured KB data, with the LLM only stitching the prose connectives.

Subsections and their data sources:

### 3.1 Classical type definition
- **Source**: `classical_nodes[0]` — markers, NT type, anatomy, references
- **Mode**: Deterministic with one LLM-generated sentence summarising
- **Content**: "The classical [name] is defined by [markers] in [region], with [N] supporting publications. Definition basis: [CLASSICAL_MULTIMODAL/PRIOR_TRANSCRIPTOMIC/...]."

### 3.2 Atlas mapping query
- **Source**: graph metadata + `find-candidates` parameters (currently implicit in workflow PARAMS)
- **Mode**: Deterministic
- **Content**: "Candidate atlas clusters were retrieved from [taxonomy] at ranks [0, 1] using metadata-based scoring (region match, NT type, defining markers). Top-N candidates: [list]. Sex bias scoring applied: [yes/no]."
- **Gap**: `find-candidates` doesn't currently leave a record on the edge YAML or in the KB graph metadata; the parameters/scoring are ephemeral. Either:
  - (a) Persist the find-candidates parameters in `graph.metadata` or per-edge `discovery_params`
  - (b) Reconstruct from the find-candidates skill at render time

### 3.3 Property alignment
- **Source**: `edges[*].property_comparisons[*]` — property, classical value, atlas value, alignment
- **Mode**: Deterministic
- **Content**: Already in Results; surface here as the *method* of comparison. "Each defining property was compared between classical and atlas representations using [the property_comparisons schema]. Alignments: CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED."

### 3.4 Expression cross-check
- **Source**: `precomputed_expression` blocks on atlas nodes; child-cluster analysis
- **Mode**: Deterministic
- **Content**: "Atlas precomputed expression for defining markers retrieved from [HDF5 source]. Best child cluster identified by [scoring rule]. Sex ratio (MFR) read directly from atlas metadata for each cluster."

### 3.5 Annotation transfer (if applicable)
- **Source**: `AnnotationTransferEvidence` items + `annotation_transfer_datasets` on graph
- **Mode**: Deterministic
- **Content**: "MapMyCells annotation transfer was run with method [method], best F1 score [X] at [level]. Source dataset: [accession], target: [WMBv1]."

### 3.6 Bulk transcriptomic correlation (if applicable)
- **Source**: `BulkCorrelationEvidence` items + `kb/correlation_runs/{id}/manifest.yaml` + `kb/datasets/{ds}.yaml`
- **Mode**: Deterministic, with run details from manifest
- **Content**: "Paired-bulk correlation was run against [N] WMBv1 cluster pseudobulks. Source data: [BulkDataset citation]. Method: [statistic_kind, parameters]. Contrasts: [list]. Output: ranked TSV at [path]."
- This is the most data-rich part and benefits most from a top-N hits table or figure (see §4).

### 3.7 Anti-hallucination guarantees
- **Source**: known framework-level
- **Mode**: Static text or LLM-summarised
- **Content**: One paragraph noting that all [n] citations, accessions, and verbatim quotes are validated against KB stores; pre-write hook enforces blockquote attribution.

**Implementation cost**: most subsections are 100-200 lines of new render.py code (data extraction + Markdown emit) plus a Methods section template in the workflow. Each subsection emits a few sentences of structured text + (optional) a small table.

---

## 4. Figures — three options

### Option A: tables only (zero new dependencies)
- Top-N hits Markdown table for BulkCorrelationEvidence (already filed in `2026-04-29_bulk-correlation-show-top-hits.md`)
- Property alignment table (existing)
- Method-summary table (new — Methods section subsections as rows)
- **Cost**: half-day. Suitable for screenshots.

### Option B: programmatic Markdown + matplotlib (1 day on top of A)
- Add δ ranked-bar plot per BulkCorrelation contrast → PNG saved to `reports/{region}/figures/{node_id}_{contrast}.png`
- Add expression heatmap per atlas-metadata cross-check (defining markers × candidate clusters) → PNG
- Embed via standard Markdown `![caption](figures/...)` syntax
- **Cost**: 1 extra day. Adds a `matplotlib`/`altair` dependency. Deterministic. Anti-hallucination-safe (no LLM decides what to plot).

### Option C: atlas browser screenshots (out of scope for this POC)
- Selenium/Playwright scripted screenshots of ABC Atlas / Allen Brain Map
- Defer to future work. Manual screenshots can supplement for the paper.

**Recommendation: A first, then B as the figure scope grows.** A is enough for half the screenshots a paper needs; B is a clean upgrade path that doesn't depend on workflow restructuring.

---

## 5. POC scope

### Must have
1. **Methods section** — new section in `workflows/gen-report.md` between Results (Section 5) and Discussion (Section 7). Subsections 3.1–3.7 above (omit 3.5 / 3.6 if the demo node has no AT / bulk evidence).
2. **Renderer additions** — extract Methods data into facts JSON. Add to `extract_node_facts()`:
   - `methods.classical_definition` (auto-generated paragraph)
   - `methods.expression_crosscheck_summary` (gene list + source HDF5 if found in graph metadata)
   - `methods.annotation_transfer_summary` (if AT items present)
   - `methods.bulk_correlation_summary` (if BULK_CORRELATION items present; pulls run manifest + dataset descriptor)
3. **Section reordering** — restructure `gen-report.md` synthesis prompt to use Intro / Results / Methods / Discussion top-level headings.
4. **Top-N hits Markdown table** for BulkCorrelationEvidence (Option A figure).
5. **Demo on two nodes**: OLM (rich AT evidence) + vmhvl_esr1_pr_neuron (rich bulk-correlation evidence + co-primary edges).

### Nice to have
6. **Programmatic δ plot** for bulk-correlation contrasts (Option B, single figure type).
7. **Abstract** — 3-sentence top-of-report summary.
8. **"Best candidate + caveats" headline** in Discussion.

### Not in scope
- Atlas browser screenshots (manual)
- New evidence types
- Schema changes
- Drilldown-mode restructure (focus on summary mode for paper screenshots)

### Demo target reports
- `reports/hippocampus/olm_neuron_summary.md` — already exists; regenerate under new framework
- `reports/sexually_dimorphic/vmhvl_esr1_pr_neuron_summary.md` — already regenerated with bulk-correlation evidence; update again under new framework

---

## 6. Files in scope

| File | Change |
|---|---|
| `workflows/gen-report.md` | Restructure Step 3 prompt: Intro / Results / Methods / Discussion top-level sections; add Methods subsections |
| `src/evidencell/render.py` | `extract_node_facts()` adds `methods` block (classical_definition, expression_crosscheck_summary, annotation_transfer_summary, bulk_correlation_summary). Helper `_load_correlation_run_manifest()` (move out of inline `_resolve_run_ref_to_pmid` for reuse) |
| `src/evidencell/render.py` | `extract_node_facts()` populates a new `top_n_hits` field per BulkCorrelation evidence item, reading the run's ranked TSV |
| (optional) `src/evidencell/render.py` | Programmatic figure generation — small matplotlib helper writing PNGs to `reports/{region}/figures/` |
| `tests/test_render.py` | Coverage for new methods extraction + top_n_hits |
| `reports/hippocampus/olm_neuron_summary.md` | Regenerate as paper-style demo |
| `reports/sexually_dimorphic/vmhvl_esr1_pr_neuron_summary.md` | Regenerate as paper-style demo |
| `planning/paper_style_reports_review.md` | This doc — initial review (already committed) |

---

## 7. Open questions to resolve before coding

1. **Should Methods be a single section or a `<details>` fold?** A fold is more compact and keeps Results visible; a flat section is more paper-like. Recommend flat for paper-style screenshots.
2. **`find-candidates` parameters**: persist on edge YAML or reconstruct? **Defer** — current scope can use static text for §3.2 ("Candidates retrieved via metadata-based query at ranks 0, 1") without per-run params.
3. **Figure storage**: `reports/{region}/figures/` (proposed) or alongside reports as `reports/{region}/{node_id}_{figname}.png`? Recommend `figures/` subdir for cleanliness.
4. **Should the Discussion section repeat the headline finding?** Recommend yes — it's the key visual when screenshotted.
5. **Where does "limitations of the framework" live?** Anti-hallucination section in Methods, or its own subsection in Discussion? Recommend Methods (it's about how the analysis was done, not what was found).

---

## 8. Concrete next steps

1. Confirm scope (POC = Must have list above; Nice to have on demand).
2. Implement Methods extraction in `render.py` (no workflow change yet — see facts JSON in isolation).
3. Restructure `gen-report.md` Step 3 prompt for paper-style sections.
4. Regenerate OLM + vmhvl_esr1_pr_neuron reports; review.
5. Decide on figure scope (A only, or A + B).
6. (If B) implement matplotlib helper + integrate.
7. Final pass + commit + PR.
