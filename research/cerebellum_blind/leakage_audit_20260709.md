# Leakage transcript audit — cerebellum_blind blind reconstruction

Date: 2026-07-09. Auditor: orchestrator (post-hoc, per RESUME.md §6 + curator
leakage policy #3).

## Threat model

The blind reconstruction must recover the curator-approved WMB (`CCN20230722`)
target clusters/supertypes without the pipeline ever having been handed those
targets. Two leakage vectors:

1. **Direct** — a subagent reads the quarantined ground-truth graphs
   (`kb/graphs/cerebellum/CB_MLI_types.yaml`, `CB_PLI_types.yaml`) or the sealed
   `answer_key.json`.
2. **Indirect** — a discovery/literature subagent retrieves a paper that names a
   target cluster's classical identity in WMB accession terms, handing the atlas
   target to the pipeline before the deterministic mapping step.

**Firewall (structural):** WMB `CS20230722_*` cluster numbering is from Yao et al.
2023. The cerebellar discovery corpus (Kozareva 2021/preprint, Osorno 2022/preprint,
Lackey, Wang & Lefebvre, etc.) predates or is independent of WMB and uses its own
nomenclature (MLI1/MLI2 = class I/class II; PLI1/2/3; basket/stellate). The WMB
cluster/supertype accessions therefore cannot appear in those papers, and enter the
pipeline only at `just find-candidates` (a deterministic taxonomy-DB query), never
from literature.

## Method

Grepped all 30 dispatched subagent transcripts
(`agent-*.jsonl` under the session `subagents/` dir):

- **(1)** any reference to `CB_MLI_types`, `CB_PLI_types`, `answer_key`, or
  `cerebellum_quarantine` — across ALL transcripts.
- **(2)** any `CS20230722_(CLUS|SUPT)_NNNN` accession in the 11 **pre-mapping**
  transcripts (Step 1b proposed types; Step 2 reference resolution; Step 3 CL lookup;
  Step 3b KB proposal + schema-fix; survey fetch; the 5 evidence-extraction agents) —
  these run BEFORE map-cell-type and must not contain any atlas accession.

## Findings — NO LEAK

**(1) Direct-read check: CLEAN.** No transcript references the quarantined
ground-truth graphs, the answer key, or the quarantine directory.

**(2) Indirect / pre-mapping accession check: CLEAN of target accessions.**
No answer-key target accession — clusters 5177, 5178, 5180, 5181, 5182, 5188, 5192;
supertypes 1144, 1145, 1149, 1151 — appears in ANY pre-mapping transcript.

One benign non-target hit: the **Step 3b schema-fix** agent contains a set of
`CS20230722_CLUS_0122…/SUPT_0010…` (plus one `SUPT_1170`) accessions. These are
**hippocampus** accessions from the committed exemplar
`kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml`, which
that agent was instructed to mirror for correct YAML field shapes during the
validation-correction loop. None is a cerebellar answer-key target; the agent was
fixing schema conformance, not performing discovery or mapping. Reading a committed
exemplar graph is within scope and does not touch the ground truth.

The Kozareva 2021 and Osorno 2022 papers (and preprints) WERE retrieved and
full-text-read during survey + evidence-extraction (expected — they are the primary
cerebellar-interneuron literature). They supplied transcriptomic **class names**
(MLI1/MLI2, Sorcs3+/Nxph1+, PLI1/2/3) — which the blind pipeline used as biological
evidence — but never WMB cluster numbers. This is exactly the firewall behaviour
predicted: literature gives class identity; the atlas cluster accession is recovered
independently by the deterministic DB query.

## Conclusion

The blind reconstruction is uncompromised. Recovery of the answer-key WMB targets
(see `mapping_20260709/stage_a_recovery.json` and `verdicts_summary.json`) reflects
genuine pipeline performance, not leaked ground truth. Validity threat from the
in-corpus Kozareva/Osorno papers is nil at the atlas-target level because those
papers do not carry WMB accessions.
