# Confidence-scoring + mapping-predicate review — survey 2026-05-24

Branch: `review/confidence-and-predicates` (off `map_cell_type_refactor_phase2_3` / Phase 2 + 3 merged).

## Purpose

Review whether Phase 2's predicate vocabulary and Phase 3's confidence policy hold up against real mappings before re-running map-cell-type + gen-report across the KB. Anchors: [#30](https://github.com/Cellular-Semantics/evidencell/issues/30) and its follow-up comments; Phase 2/3 roadmap §§4–5 in [`map_cell_type_redesign_roadmap.md`](map_cell_type_redesign_roadmap.md); regenerated reports under `reports/hippocampus/` + `reports/sexually_dimorphic/`.

Substrate: 111 MappingEdges across 7 graph files (6 hippocampus + 1 sexually_dimorphic).

---

## 1. Open policy questions

Drawn from #30 / its amendments and the roadmap. Each is a decision point this branch needs to land before the re-run.

### 1.1 Predicate selection under partial information

**Question.** When the curator (agent or human) sees a candidate match with F1 ≈ 0.65–0.8 plus partial marker / anatomy convergence, when do they pick `skos:closeMatch` vs `skos:exactMatch` vs `evidencell:PartialOverlapMatch`?

Schema descriptions today (`schema/celltype_mapping.yaml:299–325`):
- `exactMatch`: "F1 ≥ 0.8 + matching markers + matching anatomy"
- `closeMatch`: "F1 ≈ 0.65–0.8, or non-AT evidence that converges but does not yet rise to exactMatch"
- `PartialOverlapMatch`: "precision OR recall below ~0.65"

But: the F1 thresholds don't account for AT pooling (pooled F1 systematically higher than per-source, per the [AT divergence audit](at_metrics_divergence_audit_2026-05-14.md)), don't say what counts as "matching markers" (defining only? + neuropeptides? minimum count?), and conflict with the conservative-default convention from #30 amendment 1 ("default to two nodes + `skos:closeMatch`; promote to `skos:exactMatch` only when curator-confirmed or evidence is overwhelming").

**Decision needed.** A concrete rubric the report-time agent can apply deterministically, with worked examples from the 5 regenerated hippocampus reports.

### 1.2 BroadMatch + cardinality semantics — hidden 1:1 vs genuine subset

From #30 amendment ("Third mapping type"):
- `broadMatch + cardinality 1:1` = hidden 1:1 (specific cluster equals lit_type but cannot be identified yet)
- `broadMatch + cardinality 1:n` = genuine subset (lit_type subsumes multiple children)

KB usage: all 8 broadMatch edges in hippocampus carry `1:n`. None test the "hidden 1:1" case. **No worked example exists** for the hidden-1:1 reading — risk that the report-time agent doesn't reach for it.

**Decision needed.** Either find a hidden-1:1 candidate in the existing OLM mappings (the rationale on `edge_olm_to_wmb_clus_0769` already notes "the specific cluster is TBD" — could that edge be `broadMatch + 1:1` instead of `broadMatch + 1:n`?), or document the absence.

### 1.3 Directional convention — broadMatch / narrowMatch readability

From #30 comment 3 ("Glossary requirement: SKOS directional naming is unintuitive"). Glossary preamble landed in PR3 (`reports/_toc/all_taxonomies.md`). Not yet stress-tested against a reader walking the reports cold.

**Decision needed.** Pick a worked example for the glossary that's unambiguous (suggested: OLM ↔ Sst Gaba_3 supertype).

### 1.4 AT F1 threshold under broader AT availability

From roadmap §7 ("Confidence rubric and AT"). HIGH currently requires "≥1 experimental evidence type" — AT counts. After Phase 1 made AT a Stage A signal, AT is now broadly available. Should HIGH require a higher F1 floor (e.g. ≥ 0.8 pooled at the target's best rank) to guard against inflated HIGH verdicts from noisy AT?

**Decision needed.** Either bind HIGH to a numeric F1 floor in the report-time agent prompt, or document why the current "experimental evidence type" wording is sufficient.

### 1.5 Confidence ownership & curator review

Phase 3 moved verdict authority from Stage B to report time. `mapping_justification` carries `semapv:UnreviewedManualMapping` by default; curator review should promote to `semapv:ManualMappingCuration`. KB state: **102/111 edges** carry `UnreviewedManualMapping`; 9 carry `UnspecifiedMatching` (the UncertainRelationship cases); **0 carry `ManualMappingCuration`**. No edge has been curator-reviewed under the new schema.

**Decision needed.** A workflow step or skill for curator review that promotes the justification slot.

### 1.6 Ordinal ↔ numeric confidence binding (#57)

`confidence` (ordinal) and `confidence_score` (numeric) are both agent-emitted. Phase 2 design decision 3 explicitly says curator review may change the ordinal but does not back-fill numeric from ordinal. No standardised numeric floor per bin; the report-time agent picks both. Spot-check across the 12 regenerated rationales shows the agent's binding is consistent (MODERATE clusters 0.65–0.78, LOW at 0.05–0.22) but unstated.

**Decision needed.** Either codify the bin floors (HIGH ≥ 0.8, MODERATE ≥ 0.6, LOW ≥ 0.3, UNCERTAIN < 0.3 — for example) in the prompt, or accept the agent's implicit binding as good enough.

### 1.7 Region fraction as a predicate modifier

From roadmap §3.3 ("in region + distant" note). Phase 1 records `cells-in-queried-region / total-cells` but defers penalisation to Phase 2/3. KB state: every classical→atlas edge passes region filter (binary), but cluster purity / region scatter varies. Whether a low region fraction should push the predicate down from `exactMatch` toward `closeMatch` / `PartialOverlapMatch` is unresolved.

**Decision needed.** A rule like "if region fraction < 0.5, default to `PartialOverlapMatch` regardless of marker score" — or no rule, with region fraction cited in `rationale` only.

### 1.8 Reconciliation-note utilisation

KB state: **1 of 111 edges** has a `reconciliation_note` (the ivy/neurogliaform cross-edge indistinguishability case, where the report-time agent correctly used it). The field is vastly underutilised — partly because most edges haven't been through gen-report yet (only 12/111 carry a `confidence`).

**Decision needed.** Confirm reconciliation_note is the right home for cross-edge agent observations + ensure the Stage C prompt encourages it when ambiguity is real.

### 1.9 Metadata vs precomputed expression disagreement

From roadmap §7. When taxonomy metadata flags a gene as a marker but `precomputed_expression` shows it absent (or vice versa), policy is "record both, flag in PropertyComparison". Scoring policy is undecided. The `refresh_expression_pcs` tool fixed the symptom for 9 PCs; the underlying disagreement remains a real biological / curatorial signal.

**Decision needed.** Either ride with current behaviour ("report both, no scoring impact") or define a rule.

### 1.10 AT metrics provenance (deferred but blocks re-run)

From the [AT divergence audit](at_metrics_divergence_audit_2026-05-14.md): Buckets C/D/E (10+ edges across `hippocampus_GABAergic_interneurons.yaml`, `hippocampus_chamberland_subfamilies.yaml`, dentate gyrus immature neurons) have stored F1 ≪ CSV — likely wrong target row stored. If the report-time agent regenerates verdicts citing these stored F1 values, the verdicts will be wrong by construction.

**Decision needed.** Either fix C/D/E on this branch before re-running, or defer the AAC/DG/Chamberland regions out of the re-run substrate until a dedicated `refresh_at_metrics.py` lands.

### 1.11 Stage A candidate-discovery score — not currently persisted

**Question.** Should the Stage A `find_candidates` score (the integer rank-and-cut signal from `src/evidencell/taxonomy_db.py`) and its per-gene `_expression_detail` block flow forward as structured evidence on the resulting `MappingEdge`?

Current state:
- `find_candidates` produces an integer score per candidate plus `_expression_detail` (per-gene contributions, sibling/global/cohort percentiles, reliability flags, region fraction, coverage at rank ≥ 1).
- Phase 1 roadmap §3.6 commits to emitting `_expression_detail` in the JSON output — which it does (`research/{region}/discovery_candidates.json` or similar).
- **But neither the score nor `_expression_detail` is captured on the `MappingEdge`.** Stage B (map-cell-type Step 3 subagent) reads the discovery JSON as DISCOVERY_DATA but does not persist any of it. Stage C (gen-report) has no access to it at all — the gen-facts pre-pass reads the edge YAML, not the discovery artefact.
- Result: the report-time agent writing `confidence` and `rationale` cannot consult "this candidate scored 12; the next-best alternative scored 6 — strong relative-ranking signal" or "Sst contributed +3, region contributed +2, no AT signal" as inputs. The cohort context that drove inclusion in the candidate set is lost.

**Why this matters for the re-run.** Two distinct uses of the same signal:

- **Verdict triangulation.** When marker-side evidence is ambiguous, the relative-ranking signal ("this candidate dominated its cohort across most gene contributions") can tip the verdict; absence of it means the agent re-derives weaker reasoning from raw property comparisons.
- **Future scoring extensions.** ML-derived weights, ensemble scoring across multiple discovery passes, AT-pooling-aware scores, region-fraction modifiers — none of these can be evaluated against historical mappings if Stage A output isn't kept. Without a slot, every scoring experiment requires re-running discovery rather than analysing recorded scores.

**Sketch of where it could live.** Options worth weighing (not deciding here):

- **`MappingEdge.discovery_score`** — a structured slot holding the Stage A integer + `_expression_detail` + cohort rank. Keeps everything on the edge that consumed it; agent sees it at report time without extra plumbing.
- **`MappingEdge.evidence[]` entry with a new `DISCOVERY_SCORE` evidence type** — fits the existing evidence-bearing pattern; per-edge provenance is uniform with AT runs etc.
- **Separate `CandidateDiscoveryRun` record** (analogous to `AnnotationTransferRun` under `kb/annotation_transfer_runs/`), with edges pointing back via `discovery_ref`. Heavier but matches the run-artefact convention; supports re-scoring runs that produce different scores against the same source data.

Risk to flag in any design: the report-time agent must treat Stage A score as one signal among many — *not* as a re-statement of overall confidence. Stage A scores cohort-relative gene overlap; it does not see AT pooling caveats, region fraction issues at the cluster level, or literature. Schema description + prompt framing matter.

**Decision needed.** Whether to land a structural slot in this branch (small additive schema change + Stage B writes it on edge creation + gen-report reads it), or treat it as a deferred-but-named follow-up. My read: it's a *small* addition (one new optional structured field, ingested at Stage B from data that already exists in JSON) with high future-extension value. Probably worth doing on this branch since we're already touching Stage B and Stage C prompts.

---

## 2. KB substrate state — concrete findings

### 2.1 Predicate distribution (111 edges, hippocampus + sexually_dimorphic)

| Predicate | n | cardinality required? | cardinality present | notes |
|---|---|---|---|---|
| `skos:closeMatch` | 49 | recommended | 0 | all atlas-to-atlas in `wmb_to_ctx_annotation_transfer.yaml`; cardinality optional but would aid downstream consumers |
| `evidencell:PartialOverlapMatch` | 37 | no | 0 | conformant |
| `evidencell:UncertainRelationship` | 9 | no | 0 | valid Phase 2 predicate (schema line 339) — *not* a migration artefact |
| `skos:broadMatch` | 8 | yes | 8 ✅ | all `1:n`; all OLM edges; no hidden-1:1 case |
| `evidencell:CrossCuttingMatch` | 5 | no | 0 | conformant |
| `skos:exactMatch` | 3 | recommended | 0 | should be `1:1` if predicate is correct — small fix |

### 2.2 Mapping justification

| Justification | n |
|---|---|
| `semapv:UnreviewedManualMapping` | 102 |
| `semapv:UnspecifiedMatching` | 9 |
| `semapv:ManualMappingCuration` | 0 |

No edge has been curator-reviewed. **Implication:** §1.5 above needs a workflow before the next re-run produces meaningfully different output.

### 2.3 source_groups usage

Only `hippocampus_OLM.yaml` (5 edges, after this branch's Bucket-B work) and `hippocampus_GABAergic_interneurons.yaml` (5 edges, the BIC + BC fix) carry `source_groups`. The pattern is uneven — other AT evidence items with implicit pooling (e.g. Chamberland subfamily labels like `Sst_Tac1 (Chamberland per-cluster subfamily label)`) still encode the pool in free-text.

### 2.4 Verdict state

| | Hippocampus (94 edges) | Sexually dimorphic (17 edges) |
|---|---|---|
| `confidence` populated | 12 (13%) | 0 |
| `confidence` null (verdict pending) | 82 | 17 |
| Fresh `rationale_source_hash` | 11 | 0 |
| Stale `rationale_source_hash` | **1** | 0 |
| Average rationale length | ~82 words | n/a |
| `reconciliation_note` populated | 1 | 0 |

**Single stale hash:** `hippocampus_GABAergic_interneurons.yaml::edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203` — likely from this session's Bucket-B writeback touching the file. Worth investigating before the re-run.

Rationale quality on the 12 written verdicts is high (~82 words; cites F1, precomputed expression values, dataset IDs, methodological choices; no templated language). The report-time agent prompt is producing usable output.

### 2.5 Coverage

99 of 111 edges (89%) have **no rationale at all** — Phase 3 verdict-write-back has run on 12 hippocampus edges only. Sexually_dimorphic has no Phase 3 coverage yet. The re-run is the operation that will write the missing 99.

---

## 3. Recommended decision sequence for this branch

Land decisions in this order so each builds on the previous and the re-run only happens once policy is firm:

1. **Confirm § 1.5 (curator review workflow) — outline only, not implement.** Without a path to `ManualMappingCuration`, every edge stays "unreviewed". Decide what triggers the promotion (skill? skill that wraps gen-report? human review at the gate?) before re-running.
2. **Resolve § 1.1 (predicate-selection rubric)** with worked examples from the 5 regenerated hippocampus reports. Encode in the Step 3 / gen-report Stage C prompt. This is the single biggest change that would materially affect re-run output.
3. **Resolve § 1.4 (HIGH-confidence F1 floor)** — small addition to the rationale-policy section of the prompt. Test against the OLM Sst Gaba_3 edge (pooled F1=0.97; should the rubric let this go to HIGH? today it's MODERATE).
4. **Resolve § 1.6 (ordinal ↔ numeric binding)** — explicit bin floors in the prompt, or accept current implicit behaviour.
5. **Defer § 1.7 (region fraction modifier)** — agent can cite region fraction in `rationale` without it being a hard rule; revisit after a re-run.
6. **Defer § 1.8 (reconciliation_note)** — only 1 case in scope; encourage it in the prompt but don't legislate.
7. **Defer § 1.9 (metadata vs precomputed disagreement)** — orthogonal to predicate/confidence; revisit when re-running marker-heavy regions.
8. **Block on § 1.10 (AT metrics provenance) for affected regions only.** Hippocampus_GABAergic + Chamberland + dentate gyrus have known Bucket-C/D/E divergences; either fix them or exclude those nodes from the re-run. OLM, sexually_dimorphic, hippocampal glutamatergic, and the wmb_to_ctx atlas-to-atlas edges are clean and can re-run.
9. **Land § 1.11 (Stage A discovery score persistence) on this branch.** Small additive schema slot + Stage B writes it on edge creation + Stage C reads it in the gen-facts pre-pass. High future-extension value (every scoring experiment thereafter has a historical comparison surface). Worth doing before the re-run so the regenerated 99 edges carry the score, not only the 12 already-written ones.
10. **Fix § 2.1 small items** — add `mapping_cardinality: 1:1` to the 3 `exactMatch` edges. Add cardinality to the 49 `closeMatch` if we decide it's required for downstream consumers (open).
11. **Investigate § 2.4 single stale hash** before re-run.

---

## 4. Out of scope for this branch

- **Phase 4 splitting decision rule.** Needs joint atlas-side + classical-side heterogeneity work; separate workstream.
- **`refresh_at_metrics.py`.** Filed as deferred from the AT divergence audit; will eventually fix Buckets C/D/E systemically. This branch may decide to exclude affected regions from the re-run instead of waiting.
- **Schema changes.** The schema landed in Phase 2 / 3 covers all the policy questions above. We should be able to resolve everything in this branch via prompt + workflow changes + KB hand-edits. If a schema gap surfaces during the re-run, raise it as its own issue.
- **CI + pre-edit hook coverage for term validation.** Tracked separately; user is adding hooks on main and merging down.

---

## 5. Substrate decision

Per the orienting question — substrate is **hippocampus + sexually_dimorphic** (~17 graph + report pairs, 111 edges). Cerebellum (CB_MLI / CB_PLI) is the original test substrate but its AT evidence items predate the `annotation_transfer_runs/` convention and are unauditable without finding their source matrix (see audit doc § Cerebellum); excluded.
