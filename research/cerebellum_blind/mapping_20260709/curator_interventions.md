# Curator interventions during blind reconstruction — cerebellum_blind

Interventions are logged as first-class findings: the blind pipeline ran
autonomously; wherever a curator had to adjudicate, it is recorded here with
rationale so §4.1 can separate autonomous pipeline behaviour from human input.

## Intervention #1 — anatomy granularity coarsening (map-cell-type Stage A)

**When:** 2026-07-09, after first `find-candidates` pass returned 0 candidates
for ALL 5 classical nodes at ranks 0 and 1.

**Root cause (diagnosed, not guessed):** the blind discovery arm assigned each
node its biologically-precise laminar anatomy — molecular layer
(UBERON:0002974 → MBA:1144) for basket/stellate/MLI, Purkinje layer
(UBERON:0002979 → MBA:1145) for purkinje/candelabrum. The WMB atlas
(CCN20230722) does NOT paint cerebellar cells at laminar resolution: 0 clusters
carry anat rows on MBA:1144 or MBA:1145 (or their lobule-specific descendants),
whereas 1067 clusters paint to MBA:528 (Cerebellar cortex) and 1246 to
MBA:512 (Cerebellum). MBA:1144/1145 are descendants of MBA:528 in the anat
closure, so the region hard-prerequisite filter (candidate must have
cell_count>0 or count_in_or_near_100um>0 at/under a curator-queried term)
rejects every candidate.

**Finding:** literature-derived anatomy is laminar; atlas spatial annotation is
regional/lobular. This granularity mismatch is a real, generalisable failure
mode of the region prerequisite filter, not a mapping error. A production
curator seeing 0 candidates would coarsen the queried anatomy — which is what
this intervention does.

**Action:** added `Cerebellar cortex` (UBERON:0002129 → MBA:528) as an
ADDITIONAL `anatomical_location` entry on all 5 nodes, preserving the precise
laminar term for the record. find-candidates queries the union of a node's
anatomical_location terms, so the coarse term lets the region filter pass while
the laminar term stays on the node.

**Scope:** anatomy query granularity only. No change to markers, NT type, or any
scoring weight. The recovery measurement downstream is "recovery given a
curator-coarsened anatomy query"; the zero-candidate laminar result is reported
alongside it.
