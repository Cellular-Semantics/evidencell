## Steps that really require agentic judgment and what their inputs should be.

Inputs: combo of comparisions of properties + info from literature quotes.

For individual markers:  IIRC, details on nodes should be sufficient (e.g. we have evidence & transcript vs protein recorded for markers)


1. We currently have top 5 candidates at the end of mapping (although for AT hold out testing we've been using 10).  Researching all in detail might be wasteful if we can design a process to whittle down based on additional information in quotes before proceeding to generate a full report.
2. What AT labels to use:
   - check mapping of labels in AT onto lit type. Choosse most specific appropriate.
   - If multiple or grouping annotations map is there evidence that these correspond to hetereogeneous types (Winterer  OM is an example of where they do not)
2. Ranking from quotes:  
    - Strongest candidates have evidence that links cleanly to location, structure (including connectivity and projection) and function.
         - AT to patch-seq data with loc, structure and function
         - Bulk RNAseq from transgene marked cells with the loc, structure and function
         - Unique markers or marker combo confirmed as transcript markers - cleanly marking cells with correct structure, function and location in some context that is replicated with available data.
    - Next strongest: 
       - AT from single cell + spatial transcriptomics, confirming location and markers.
   - weakest AT evidence:
       - single cell ony - better if can confirm makers & gross location from dissection.

3. Subtleties/caveats from quotes + overview
    - Evidence for heterogeneity of lit type.
       - Is there strong evidence that the lit class is highly heterogeneous --> Down ranke for mapping


## Extended aims for report generation 

1. Flitering: Upstream candidate input top 5-10 best mappings from map_cell_type. Which of the top-K is worth a full report?  Agent is needed to make judgement calls to whittle down to 2-4 best candidates for report generation.  Much of the info needed for this is the same as for report generation (see above)

2. AT source-label selection / mapping
Decision: when the AT artifact has multiple labels that could pertain to the classical type, which one (or pooled set) maps?

Inputs:

AT artifact at_results.yaml source_label list + F1 matrix.
Classical node identity + lit-side evidence about subtyping.
Literature quotes about source-side cell-type definitions (e.g. Winterer's own paper text on Sst-OLM vs Htr3a-OLM split).
Cross-source marker consistency (do quotes from different papers describing "the same" source-side type agree?).
Output: chosen source_label(s); if pooled (e.g. Sst-OLM + Htr3a-OLM → "OLM-pooled"), explicit source_groups[*].rationale justifying the pool with cited quotes; if separate, the case for treating them as distinct lit_types.

Where: pre-Stage-B at the curator/pipeline boundary, OR at gen-report's pool-candidates step (which already has the cross-edge view). The current at_figures --pool A,B:NAME mechanism is the manual analog; agent-assist this.

2. Write-back to KB:
  - non-programmatic categorical scoring (confidence feeds into filtering)

  2a. confidence: 
      Decision: what confidence does this edge actually deserve?

        Inputs:

        All evidence items on the edge.
        Verbatim quotes for the LITERATURE items (modality strength: patch-seq > sc + spatial > sc alone; replication count; in-context confirmation).
        AT modality strength signal (which datasets does the AT run pool from?).
        Cross-modality convergence (do markers + location + AT + ephys all point to the same target?).
        Output: confidence + confidence_score + rationale, grounded in the evidence hierarchy you laid out:

        STRONG (HIGH): convergent multi-modal (AT-patch-seq OR transgene-marked + loc + structure + function, replicated across labs).
        MEDIUM (MODERATE): AT from sc + spatial confirming location + markers; or single-modality with strong cross-replication.
        WEAK (LOW): single-cell only, no spatial/morphology cross-confirmation; or markers + gross dissection-level location only.
        UNCERTAIN: marker contradictions across studies without resolution; AT borderline F1; documented lit-side heterogeneity without sub-call.

## What the pre-filter could look like, concretely

### Where it executes

Two plausible homes:

1. **Hybrid: deterministic Python pre-pass + LLM finalises in synth prompt.** Python step at gen-facts time applies structural cuts (no AT + no region + multiple DISCORDANT markers → auto-cut). Surfaces a `pre_filter_seed` block in facts.json marking obvious cuts. LLM in synth prompt either confirms or overrides each seed cut/keep based on quote-level evidence (modality strength + literature contradictions). Cleanest split between structural and evidence-strength judgements.

2. **Pure LLM in synth prompt.** All filter decisions happen inside the synth call. LLM reads everything and emits the pre-filter JSON block. Simpler pipeline; LLM has more to do per call; structural cuts (which are deterministic) waste LLM tokens.

### Inputs available to the filter (regardless of where it runs)

| Source | What's in it | Form |
|---|---|---|
| `discovery_score` per edge | score, rank-in-cohort, region_fraction_100um, region_count_completeness, expression_detail per gene (val + cohort_pct + applied_score + coverage), at_signal (F1 / target_level / n_cells) | structured |
| `property_comparisons` per edge | per-property alignment (CONSISTENT/APPROXIMATE/DISCORDANT/NOT_ASSESSED) + node_a/node_b values | structured |
| `evidence.ANNOTATION_TRANSFER.metrics_by_level` | F1 at each taxonomy level, with `supports_default` | structured (via `at_metrics.compute_edge_metrics`) |
| Classical node `defining_markers[*].sources[*]` | per-source `marker_type: PROTEIN \| TRANSCRIPT`, `method`, `scope`, PMID/DOI ref | structured |
| `references.json` quote bodies | verbatim text behind each `quote_key` on classical-node sources | unstructured (LLM reads) |
| `pool_candidates.json` | structurally-detected indistinguishability pairs | structured |

### Criteria to cut (three-tier evidence hierarchy translated)

| Tier | Description | Detectable from | Where |
|---|---|---|---|
| **Strongest** | AT-patch-seq with confirmed loc + structure + function; transgene-Cre + ephys/morphology + scRNA-seq; unique markers replicated across labs | LLM-reading of quote methodology + ref count + study modality | LLM only |
| **Next** | AT from sc + spatial transcriptomics confirming markers + location | structured (AT F1 ≥ 0.3 AND region_fraction_100um ≥ 0.3 AND ≥ 2 markers CONSISTENT) | could be Python |
| **Weakest** | sc-only AT; gross-dissection markers | structured (low markers + no spatial confirmation) | could be Python |
| **Cut candidates** | no AT + low region + many DISCORDANT markers | structured | Python (cheap) |

### How many to keep — policies

1. **Threshold-based + bounded [1, 5].** Keep all candidates meeting the structural quality floor (AT F1 ≥ 0.3 OR (region_fraction_100um ≥ 0.3 AND ≥ 2 markers CONSISTENT) OR discovery_score ≥ some N). Always keep at least the top-1 even if all fail the floor (curator needs to see the best candidate). Cap at 5 to bound report length. Quality-grounded; survivor count varies per case.

2. **Fixed top-3.** Always keep exactly 3 (or fewer if discovery pool is smaller). Predictable report length; arbitrary cut at #4 even when #4 is strong.

3. **Agent decides based on score distribution.** LLM picks the quality cliff. Most flexible; least predictable; harder to audit consistency across runs.

4. **Configurable per-run (PARAMS field with default 5).** Curator sets `max_survivors` in PARAMS; default 5. Lets the curator override per case (e.g. heterogeneous types might want more). Adds a knob.
