# Adaptive Mapping Loop — Design Discussion

**Date**: 2026-04-20
**Status**: Discussion notes — not yet implemented
**Context**: Emerged from OLM hippocampus pilot where annotation transfer results
(supertype-level signal, cluster scatter) showed the initial per-cluster edge framing
was at the wrong resolution. Prompted a rethink of the overall mapping workflow.

---

## The problem with the current pipeline

The current workflow commits to cluster-level mapping hypotheses at the triage stage,
then accumulates evidence for those specific hypotheses. When annotation transfer runs
*after* detailed per-cluster edges are built, it can contradict the original framing —
as happened in the OLM case, where MapMyCells resolved cleanly to the Sst Gaba_3
supertype (F1=0.67, 43/46 cells) but placed 0/46 cells on the nominated cluster 0769.

The pipeline had no way to loop back and revise: the report, the edges, and the
evidence paragraphs were all framed around cluster 0769 as the primary candidate,
even though the data said "supertype."

---

## Proposed workflow ordering

1. **Initial triage** — taxonomy metadata + ASTA report
   - Outputs: candidate mapping region, candidate level(s) (may be supertype or
     subclass, not necessarily cluster), any high-priority bridging datasets
   - Does NOT commit to specific cluster edges yet
   - Explicitly asks: what bridging datasets exist?

2. **Annotation transfer** (if bridging datasets available — see below)
   - Run on qualifying datasets before building detailed edges
   - Outputs: the resolution level the data supports, whether subpopulations
     segregate to different clusters, which cell sets are actual mapping targets
   - If no bridging dataset: skip to step 3 with wider uncertainty on level

3. **Reassess and set edges**
   - Build edges at the resolution the data supports (may be supertype, not cluster)
   - Identify specific marker gaps that expression queries can fill
   - Consider subpopulation splitting: if source data separates subtypes (e.g.
     Sst-OLM vs Htr3a-OLM), score them separately and consider sub-nodes

4. **Expression queries** — targeted across candidate cell sets
   - Each query either confirms, narrows, or splits the mapping
   - Example: query Chrna2/Grm1/Npy expression per cluster within Sst Gaba_3
     to determine whether within-supertype resolution is achievable

5. **Report** — synthesise, document remaining gaps

---

## Dataset selection criteria for annotation transfer

Not all single-cell datasets qualify. Prioritise **bridging datasets** that
independently confirm classical type identity via a modality other than transcriptomics:

**Qualifying (bridging):**
- Morphological reconstruction + sequencing (patch-seq, post-hoc DAB fill like
  Winterer 2019 for OLM)
- Transgenic Cre-driver targeting of the specific classical type + sequencing
  (where the driver line has been validated to target the classical type)
- Spatial transcriptomics with layer/region resolution matching the classical
  type's anatomical definition

**Not qualifying (useful background, not bridging):**
- Broad regional scRNA-seq atlases (no way to identify which cells are your
  classical type without independent marker selection)
- Studies that use the same markers but don't confirm morphology/electrophysiology
- Datasets where "OLM" or equivalent is an inferred label, not experimentally confirmed

---

## Compute/resource preflight gate

Before downloading or processing any dataset, report to the user:

- Dataset accession and what makes it a bridging study
- File size (h5ad or equivalent)
- Estimated compute requirements (RAM, MapMyCells runtime)
- Whether web API is feasible (size limits) or local compute needed
- Recommendation: proceed / skip / subsample

User decides which datasets to run. This keeps the human in the loop at the
expensive step without babysitting cheaper steps. The existing `at-preflight`
recipe is the right hook for this.

Autonomy principle: steps 1–3 (triage, triage reassessment, edge framing) can
run without user approval. The preflight gate before AT is the key human checkpoint.
Further expression queries (step 4) are cheap and can be automated if the mapping
target is already set.

---

## Dataset discovery

Two layers:

**Layer 1 — ASTA report.** The ASTA prompt should explicitly request bridging
datasets: studies combining morphological/electrophysiological identification
of the classical type with sequencing or spatial transcriptomics, including
dataset accessions where available. This surfaces obvious high-value datasets
as part of the literature survey.

**Layer 2 — Triage follow-up.** ASTA may miss datasets because:
- The relevant paper was ranked low or not reached
- The accession is in a methods section, not the abstract
- A relevant spatial/patch-seq study postdates the ASTA run
- The study doesn't use the classical type name explicitly

A bounded follow-up step checks: given the candidate cell sets from taxonomy
metadata, are there known datasets that mapped to those specific clusters/supertypes?
This searches from the atlas side, not the classical-type side. One or two targeted
queries, not an open-ended literature search.

**Dataset inventory = ASTA-reported datasets + triage follow-up**, then preflight
assessment on the union before any downloads.

---

## OLM-specific observations (prompting this design)

- Annotation transfer (GSE124847 → WMBv1) resolved to Sst Gaba_3 supertype
  (F1=0.67, 43/46 cells) but placed 0/46 cells on cluster 0769 specifically
- Within-supertype scatter (cells spread across clusters 0767–0774) may reflect:
  (a) genuine OLM subpopulation heterogeneity, or (b) cluster resolution limits
  for this cell type at current atlas granularity
- Winterer 2019 identifies two OLM subtypes (Sst-OLM and Htr3a-OLM); Thulin 2025
  identifies three Sst/Pnoc subclusters. Scoring these separately in AT could
  determine whether they segregate to different clusters within Sst Gaba_3
- Implication: the edge for OLM should target Sst Gaba_3 supertype as primary
  candidate, with per-cluster resolution as an open question, not the reverse

---

## Open questions

1. **Schema**: do edges need explicit support for supertype/subclass-level targets
   (not just cluster)? S1 (rank encoding) addresses this — `rank: int` instead
   of hardcoded level names. Confirm S1 is sufficient.

2. **Subpopulation splitting**: when does the agent judge that evidence warrants
   creating sub-nodes vs. flagging heterogeneity in caveats? Needs a decision rule.

3. **Lit search placement**: not in this cycle. Lit review (M2) feeds the ASTA
   report (step 1 input), so it's upstream of the adaptive loop, not interleaved.
   Gaps identified in step 5 (report) become inputs for a future lit search cycle.

4. **Autonomy/supervision balance**: triage + reassessment can be automated;
   AT preflight is the key human gate; expression queries post-reassessment
   can be automated if mapping target is set. Still being calibrated.

5. **Compute availability**: users without sufficient local compute skip MapMyCells.
   Workflow must degrade gracefully: triage → marker queries → report, with AT
   as an optional enrichment step rather than a required gate.
