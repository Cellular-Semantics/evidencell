# cerebellum_blind — end-to-end blinded reconstruction audit

**ICBO2026 Reviewer #2 response, primary experiment.** A single blinded
end-to-end run of the full evidencell pipeline
(asta-report-ingest → survey → evidence-extraction → map-cell-type → gen-report)
on the cerebellar molecular-layer / Purkinje-layer interneuron mappings, starting
from a fresh ASTA deep-research PDF, with the committed curator-reviewed graphs
(`kb/graphs/cerebellum/CB_MLI_types.yaml`, `CB_PLI_types.yaml`) held out as sealed
ground truth (`answer_key.json`).

- **Run date:** 2026-07-09
- **Repo commit:** `8e05bb57096bf2683e9a2449a8e4d57a4590f0eb` (branch `icbo2026-revision`)
- **Taxonomy:** WMBv1 `CCN20230722` (DB built 2026-06-08; marker-union enrichment
  extended on 2026-07-09 to add cerebellar markers — see Methods)
- **Design:** single reconstruction pass (**R2.Q1 reported as single-run; no 5× stability
  sweep**, curator decision). Correction-rate metric (R2.Q2) dropped as agreed.
- **Blinding:** ground-truth graphs quarantined for all answer-sensitive steps;
  restored at teardown. Post-hoc transcript leakage audit: **clean** (see
  `../../../cerebellum_blind/leakage_audit_20260709.md`).

## Artifacts

| Artifact | Path |
|---|---|
| Answer key (sealed ground truth) | `answer_key.json` |
| Blinding harness state | `BLINDING_STATE.md` |
| Discovery arm outputs | `../../../cerebellum_blind/20260709_cerebellum_blind_report_ingest/` |
| Survey summaries | `../../../cerebellum_blind/survey_20260709/` |
| Evidence-extraction manifests | `../../../cerebellum_blind/evidence_extraction_20260709/` |
| Mapping (Stage-A discovery JSONs, recovery, verdicts) | `../../../cerebellum_blind/mapping_20260709/` |
| Curator interventions log | `../../../cerebellum_blind/mapping_20260709/curator_interventions.md` |
| gen-report reports + failed round-1 drafts | `reports/cerebellum_blind/*.md`, `../../../cerebellum_blind/gen_report_20260709/` |
| Leakage audit | `../../../cerebellum_blind/leakage_audit_20260709.md` |
| Full scoring | `../../../cerebellum_blind/scoring_20260709.json` |
| Throwaway blind KB graph (uncommitted) | `kb/graphs/cerebellum_blind/` (NOT committed) |

## Pipeline executed (all steps dispatched as isolated subagents per CLAUDE.md)

1. **asta-report-ingest** — PDF `inputs/deepsearch/ASTA_MLI_PLI.pdf` → 5 proposed
   classical/prior nodes, 45/45 references resolved (85 quotes), 4 EXACT + 1 BROAD
   CL mappings, draft KB graph (schema-corrected via one validation-correction loop).
2. **survey** — 45 ASTA corpus papers → 28 LiteratureSummary entries (16 HIGH / 11 MOD / 1 LOW).
3. **evidence-extraction** — 16 PropertySource entries across the 5 nodes.
4. **map-cell-type** (discovery) — `find-candidates` at ranks 0 (cluster) + 1 (supertype),
   top_k=50 for recovery measurement; `emit-stage-b` wrote top-5 MappingEdges/node/rank
   (50 edges + 20 atlas stubs).
5. **gen-report** — per-node synthesis + independent validation + verdict-block
   anti-hallucination check + write-back (40 verdicts).

## Findings

### 1. Discovery recall: 3/5 classical types (biology-driven miss, not system failure)

The blind ASTA report proposed **basket, stellate, candelabrum**, plus an MLI1/MLI2
transcriptomic-classes node and Purkinje (principal neuron). It did **not** propose
the two remaining PLI answer-key types, **globular** and **lugaro** — the report
framed Purkinje-layer heterogeneity as candelabrum + the transcriptomic MLI split and
did not resolve the classical globular/lugaro distinction. This is a
literature-framing limitation of the source deep-research report, not a mapping-engine
failure; it caps end-to-end recovery at the discovery stage for those two types.

### 2. Anatomy-granularity mismatch → curator intervention #1 (generalisable failure mode)

The blind pipeline assigned each node its biologically-precise **laminar** anatomy
(molecular layer UBERON:0002974→MBA:1144; Purkinje layer UBERON:0002979→MBA:1145).
WMBv1 does **not** paint cerebellar cells at laminar resolution (0 clusters on
MBA:1144/1145; 1067 on MBA:528 Cerebellar cortex). The region hard-prerequisite filter
therefore returned **0 candidates for all 5 nodes**. A logged curator coarsening to
Cerebellar cortex (UBERON:0002129) restored candidate generation. See
`curator_interventions.md #1`. **This is a real, reportable finding:** literature-derived
anatomy is laminar; atlas spatial annotation is regional — the region filter needs a
coarsening fallback when a queried term has no painted cells.

### 3. Recovery — deterministic Stage-A baseline (R2.b attribution)

Rank of the answer-key target within the top-50 `find-candidates` list (post-coarsening):

| Type (difficulty) | Cluster target | Supertype target |
|---|---|---|
| stellate (biology-hard) | 5188 @ **#1** | 1151 @ **#2** |
| candelabrum (clean) | 5178 @ **#4** | 1144 @ **#5** |
| basket (biology-hard) | 5188 @ **#3** | 1149 @ #19 |
| MLI1/MLI2 cross-cut | 5188 @ **#2** | 1151 @ **#1** |

The deterministic scorer alone ranks the correct **cluster** target into the emitted
top-5 for every discovered type. Supertype recovery is strong for stellate/candelabrum/MLI
but **deep (#19) for basket** — the transcriptomic supertype structure
(1149 Megf11/MLI1 vs 1151 Cdh22/MLI2) does not cleanly separate the basket morphology,
consistent with the curator's `CrossCuttingMatch` label.

### 4. Recovery — agent (gen-report) final pick, and where judgement helped vs hurt

| Type | Agent primary survivor | Cluster target recovered? | Supertype target recovered? |
|---|---|---|---|
| **candelabrum** | SUPT_1144 (LOW, broadMatch) | ✅ CLUS_5178 (secondary, closeMatch) | ✅ SUPT_1144 (primary) |
| **stellate** | CLUS_5188 (MODERATE, closeMatch) | ✅ CLUS_5188 (primary) | ❌ (1151 cut) |
| **MLI cross-cut** | CLUS_5188 (MODERATE, closeMatch) | ✅ CLUS_5188 (primary) | ✅ SUPT_1151 (secondary) |
| **basket** | SUPT_1151 (LOW, Uncertain) | ⚠️ CLUS_5188 (weakest survivor only) | ❌ (1149 never emitted; ranked #19) |

- **candelabrum** is the cleanest end-to-end success — both parent supertype and best
  child cluster recovered as survivors (the supertype+best-child pattern), matching the
  answer key exactly at the accession level.
- **stellate** and **MLI** — the agent promoted the correct cluster target (5188) to
  **primary** at MODERATE.
- **basket** is the weakest result and the most informative: the deterministic baseline
  ranked the true cluster (5188) at #3, but the agent's marker reasoning (Calb1 scored
  DISCORDANT on 5188 — Calb1=0.18, above the detectable floor) **demoted** 5188 to the
  weakest survivor and promoted supertype 1151 (an MLI2/Cdh22 supertype, i.e. a
  stellate-leaning target) to primary. Here the agent's judgement layer *hurt* recovery
  relative to the deterministic ranking. This is the expected consequence of the
  biology-hard cross-cutting: basket cells are a positional subset of transcriptomic
  MLI1, and no single marker cleanly anchors them.

**Attribution summary (R2.b):** the deterministic component supplies strong candidate
ranking (correct cluster in top-4 for 4/4 discovered types); the agent adds confident,
correctly-calibrated survivor selection for stellate/candelabrum/MLI, but its
marker-contradiction reasoning can mis-rank a target in genuinely cross-cutting cases
(basket).

### 5. Confidence calibration — conservative, no over-claiming

No survivor received **HIGH** (correct: no annotation-transfer or experimental
evidence was available on any edge; the "no HIGH from literature/metadata alone" rule
held). **MODERATE** was reserved for clean marker-driven cluster picks
(stellate 5188, MLI 5188/1151); **LOW** for the marker-poor candelabrum (no positive
markers) and the ambiguous basket. Predicates were one step more cautious than the
curator's where evidence was thin (candelabrum closeMatch/broadMatch vs curator
`exactMatch`; basket `UncertainRelationship` vs curator `CrossCuttingMatch` — the agent
did not recognise the cross-cutting pattern but correctly signalled uncertainty).

### 6. Anti-hallucination guard fired and worked

The independent validation + verdict-checks caught **real** errors before write-back:
- **stellate** report: 3 truncated/excerpted blockquotes (verbatim-integrity FAIL).
- **MLI** report: hallucinated `[1-context]` label, four bare author-year citations
  absent from the reference index, and a phantom accession used in prose.
- **3/4 verdict-block sets**: invalid `CaveatType` enum values the agents invented,
  ungrounded experimental-modality tokens in rationales (patch-seq, scRNA-seq,
  MapMyCells, biocytin, morphology — none grounded on metadata-only edges), and a
  marker-count miscount ("2 of 3" vs 4 comparisons).
All were resolved within one synthesis retry + one focused-correction round; final
reports pass LLM validation and the deterministic verdict check. This is direct
evidence the hallucination guard is load-bearing, not decorative.

## Caveats / threats to validity

- **Single run** — no stability/variance estimate (curator decision; R2.Q1 reported as
  single-pass). Survivor selection is LLM-driven and may vary run-to-run, as the
  stellate retry (which shifted the secondary from a supertype to CLUS_5189) illustrates.
- **No annotation-transfer arm** — the AT step (MapMyCells → F1) was out of scope for
  this discovery→mapping→report validation; all edges are metadata-only, which caps
  confidence at MODERATE and is the single largest lever for HIGH-confidence recovery.
  The curated ground truth's cluster targets were originally anchored by AT F1 (e.g.
  candelabrum PLI1→5178 F1=0.94), so the blind run's marker-only recovery of the same
  clusters is a stronger-than-expected result.
- **Marker coverage gap** — Rora and Hcn1 are absent from the ABC precomputed-stats
  marker panel, so those two classical markers scored NOT_ASSESSED; the discriminating
  markers (Sorcs3, Nxph1, Pvalb, Kcna1, Grid1, Calb1) were covered.
- **Curator intervention #1** (anatomy coarsening) is logged and reported; recovery
  numbers are "given a curator-coarsened anatomy query", with the zero-candidate laminar
  result reported alongside.

## Reproducibility

All subagent steps dispatched via the Agent tool (never inline). Deterministic steps
(`find-candidates`, `emit-stage-b`, `rationale-writeback`) are CLI recipes at the commit
above. Discovery corpus, references, summaries, discovery JSONs, reports, and verdict
write-backs are all preserved under `research/(validation/methods_audits/)cerebellum_blind/`.
The throwaway blind KB graph (`kb/graphs/cerebellum_blind/`) and blind references
(`references/cerebellum_blind/`) are intentionally NOT committed; regenerate by rerunning
the pipeline against the answer key.
