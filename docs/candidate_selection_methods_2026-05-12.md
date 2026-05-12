# Candidate cell-type selection — methods description

**Date:** 2026-05-12
**Source code:** [`src/evidencell/taxonomy_db.py`](../src/evidencell/taxonomy_db.py) — `TaxonomyDB.find_candidates`
**Recipe:** `just find-candidates <graph_file> <node_id> <taxonomy_id> <rank> <top_k>`

Paper-ready prose describing the candidate-selection pipeline as it
stands at this date. Refresh + restamp when the algorithm changes
materially.

---

For each curator-defined classical cell type, evidencell ranks
candidate transcriptomic clusters from a target taxonomy using a
two-pass scoring pipeline implemented in `find_candidates`.

**Hard prerequisite filters.** Candidates are first filtered against
the classical type's anatomy and neurotransmitter identity. Source
anatomy is supplied as UBERON terms and resolved to the relevant
Allen Atlas anatomy hierarchy (e.g. the Allen Mouse Brain Atlas for
CCN20230722) via xref tables with a name-based fallback. The set of
permitted target annotations is expanded by one parent level in the
atlas hierarchy so that sublayer-precise source annotations intersect
candidate annotations at the parent field level (e.g. *CA1 stratum
oriens* expands to include *Field CA1* and its descendants). A
candidate is retained if its own annotated anatomy terms intersect
this expanded closure. When a candidate above the leaf-cluster rank
fails this test on its own annotations, the filter falls back to the
union of anatomy annotations across its rank-0 (leaf cluster)
descendants — a workaround for an upstream percent-of-cells anatomy
cutoff that strips non-dominant regions from non-leaf nodes during
taxonomy ingest. Candidates rescued via the fallback are flagged so
downstream consumers can attribute the rescue. Neurotransmitter
prerequisite is enforced only when both source and candidate carry an
NT annotation, propagated to non-leaf ranks via majority vote across
leaves.

**Soft scoring within the surviving cohort.** For each surviving
candidate the scorer computes per-gene percentile-based scores against
the cohort distribution of all survivors (not the atlas-wide
distribution). Defining markers, neuropeptides, and negative markers
contribute equal-weight tier scores; a sibling-percentile primary
score (+2 / +1 / 0) is augmented by an absolute-expression specificity
bonus (+1 when the candidate sits in the atlas-wide top decile) and a
region-exact-match bonus (+1 when the candidate hits the strict,
non-expanded query closure). Positive-marker tier scores at non-leaf
ranks are dampened by the square root of leaf-coverage (the fraction
of rank-0 descendants with detectable expression of the queried
marker) so that a strong parent-level mean driven by a small subset
of leaves does not over-credit the parent. Cells with prior
annotation-transfer F1 evidence above level-specific thresholds enter
the result via an explicit AT-bypass that skips the prerequisite
filters, with the F1 itself binned into +3 / +2 / +1 bonus tiers.
Final scores are non-negative; survivors with score < 0 are dropped,
and results are returned as the top-K candidates ordered by score.
