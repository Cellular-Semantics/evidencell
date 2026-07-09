# RESUME — cerebellum_blind end-to-end validation (ICBO2026 R2 revision)

**Read this first after a Claude Code restart.** It captures the full task, every
decision the curator (dosumis) made, what is done, and exactly where to pick up.

Branch: `icbo2026-revision`. Curation mode. A parallel session owns `ICBO2026_paper/`
and `kb/graphs/**` committed state — **do not edit those**; commit only
`research/validation/**`. Dispatch subagent workflow steps via the Agent tool, never
inline (CLAUDE.md rule).

Governing brief: `ICBO2026_paper/validation_session_brief.md`.

---

## Why we paused / what the restart fixes

Two MCP servers declared in `.mcp.json` were **not connected** this session:
`Asta_semanticscholar` (needed by asta-report-ingest Step 2, reference resolution) and
`ols4` (Step 3, CL lookup). Dispatched subagents inherit session MCP connectivity, so
they'd fail identically. Curator chose: **restart Claude Code to bring both servers
online, then resume the exact production pipeline** (no fallbacks — faithful to
production for the paper's reproducibility claim).

**After restart, verify the servers are live before proceeding:**
```
ToolSearch: select:mcp__Asta_semanticscholar__get_paper_batch,mcp__ols4__search,mcp__ols4__get_term
```
Both must resolve. If not, stop and tell the curator.

**Root cause (diagnosed 2026-07-09 — do NOT re-litigate):** the config is CORRECT.
`.claude/settings.local.json` injects `env.ASTA_API_KEY` and `enabledMcpjsonServers`
lists all four servers; both HTTP endpoints + the ASTA key are healthy at the wire
level (verified by direct MCP `initialize`/`tools/list`). The failure is
**intermittent connection of the two `"type":"http"` MCP servers at VS Code
extension-host startup** (stdio `artl-mcp` is reliable; ASTA + ols4 flake — ols4 is a
stateful streamable-HTTP server, sensitive to startup timing). **Reliable workaround:
launch VS Code from the CLI (`code <repo>`)** — confirmed working by curator. In-session,
`/mcp` → reconnect usually revives them without a full restart. No `.mcp.json` /
settings change is needed.

**ols4 tool-name watch-out:** the Step 3 subagent prompt calls `mcp__ols4__search` and
`mcp__ols4__get_term`, but the allow-list references `mcp__ols4__fetch`/`getChildren` —
the EBI OLS4 MCP may expose different tool names. Once ols4 is connected, check its
actual tool list (ToolSearch) and adapt the Step 3 prompt if the names differ.

---

## Task in one paragraph

Produce quantitative validation answering Reviewer #2 for ICBO2026. Primary experiment:
a **blinded end-to-end reconstruction** of the cerebellar molecular-layer / Purkinje-layer
interneuron mappings on the WMB taxonomy `CCN20230722`, starting from a fresh ASTA
deep-research PDF, with the existing curator-reviewed graphs as **held-out ground truth**.
Measure whether the full pipeline recovers the curator-approved WMB targets, and separate
the deterministic-baseline contribution from the agent's.

## Curator decisions (locked)

1. **Starting point:** fresh ASTA run (full pipeline: asta-report-ingest → survey →
   evidence-extraction → map-cell-type → gen-report), NOT the existing-nodes mapping arm.
2. **Scope:** "full run but only once" → single blind reconstruction pass. **No 5×
   stability sweep** (R2.Q1 reported as not-assessed-this-pass / single-run).
3. **Leakage policy:** Run + audit + report. Discovery fetches the real corpus fresh
   (incl. Kozareva 2021 / Osorno 2022); do a **post-hoc transcript leakage audit** and
   report any retrieval that named a target cluster's identity as a threat to validity.
   Firewall: the WMB cluster numbers exist ONLY in the sealed answer key, never in those
   papers (WMB = Yao 2023), so full-text reads can't hand over the atlas target.
4. **taxonomy_id typo:** committed cerebellum graphs say `CCN202307220` (trailing 0) —
   a typo that broke the June refresh; real taxonomy/DB is `CCN20230722`. **Flag only**;
   fix only in the blind working copy. File a dev-request for the committed-graph fix
   (separate PR); do NOT edit committed graphs here.
5. **Correction-rate metric (R2.Q2):** **DROPPED** — too hard to measure cleanly.
6. **Don't gate on papers** — skip the asta-report-ingest Step 4 human GATE; auto-write
   proposed nodes and continue.
7. **Region slug for the blind run:** `cerebellum_blind` (keeps generated nodes away
   from the committed ground truth).

---

## Environment facts (verified 2026-07-09)

- Taxonomy DB `kb/taxonomy/CCN20230722/CCN20230722.db` is **fresh** (built 2026-06-08,
  after source YAML), fully populated (5322 cluster / 1201 supertype / 338 subclass /
  34 class), `anat_closure`=10083 rows, `node_expression`=228305 rows. **No rebuild
  needed.** Preflights re-verify at runtime.
- All 8 ground-truth target accessions resolve in the DB.
- Local OAK `~/.data/oaklib/cl.db` + `uberon.db` present (hooks' term check works).

---

## DONE (durable artifacts, all on disk)

| Aim | Result | Artifact |
|---|---|---|
| R2.b deterministic baseline (`at_blind`) | find-candidates alone recovers **75.6% (59/78)** @ top-k10 (cluster 54.5 / subclass 84.6 / supertype 70.0 / class 90.9%) | `research/validation/methods_audits/at_blind/runs/latest.json` @ commit 8e05bb57 |
| R2.Q2 mapping census | **363 verdicts, ALL hippocampus** (HIGH 5 / MOD 40 / LOW 168 / UNCERTAIN 102 / REFUTED 48); other 5 regions have graphs but no gen-report verdicts | `census.json`, `scripts/census.py` |
| Ground-truth answer key | 5 classical types → WMB targets, verified in DB | `answer_key.json` |
| Blinding harness | designed + restart-safe; ground truth currently RESTORED | `BLINDING_STATE.md` |
| Discovery Step 0 | output dir + run_config | `research/cerebellum_blind/20260709_cerebellum_blind_report_ingest/run_config.json` |
| Discovery Step 1 (deterministic extraction) | **188 quotes / 45 papers / 45 corpus IDs** | same dir: `extracted_quotes.json`, `reference_list.json`, `pdf_corpus_ids.json` |

### Scoring answer key (blind run must recover these — see answer_key.json)

| Classical type | Cluster target | Supertype target | Difficulty |
|---|---|---|---|
| basket | CS20230722_CLUS_5188 | CS20230722_SUPT_1149 | cross-cutting (biology-hard) |
| stellate | 5188 or 5192 | 1149 or 1151 | distributed (biology-hard) |
| candelabrum | CS20230722_CLUS_5178 | CS20230722_SUPT_1144 | clean |
| globular | CS20230722_CLUS_5177 | CS20230722_SUPT_1144 | distributed |
| lugaro | 5180–5182 | **CS20230722_SUPT_1145** (primary) | supertype-level |

---

## RESUME — do this, in order

**0. Verify MCP servers live** (see top). Then **re-quarantine** the ground truth
(BLINDING_STATE.md § Re-quarantine) using the NEW session's scratchpad path.

**1. Finish discovery arm — asta-report-ingest** (`workflows/asta-report-ingest.md`),
region `cerebellum_blind`, PDF `inputs/deepsearch/ASTA_MLI_PLI.pdf`,
output dir `research/cerebellum_blind/20260709_cerebellum_blind_report_ingest/`.
Steps 0–1 are DONE. Continue:
   - Step 1b — proposed types (dispatch 1 subagent, model opus). No MCP.
   - Step 2 — reference resolution + merge into `references/cerebellum_blind/references.json`
     (dispatch, sonnet). **Needs Asta_semanticscholar.**
   - Step 3 — CL lookup → `cl_mappings.json` (dispatch, sonnet). **Needs ols4.**
   - Step 3b — quote validation + write `proposed_kb_cerebellum_blind.yaml` (dispatch, opus).
   - Step 4 GATE — **SKIP the human gate** (curator decision #6); auto-copy the draft to
     `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml`
     (pre-write hook fires; fix validation errors). This file is THROWAWAY (never commit).
   - Pass subagent prompts VERBATIM with variables filled (prompts are contracts).

**2. survey** (`workflows/survey.md`) — corpus_ids_file =
`research/cerebellum_blind/20260709_cerebellum_blind_report_ingest/pdf_corpus_ids.json`,
region `cerebellum_blind` → `all_summaries.json`.

**3. evidence-extraction** (`workflows/evidence-extraction.md`) — per node, summaries →
KB YAML PropertySource entries. (No paper-selection gate for ASTA survey runs.)

**4. map-cell-type** (`workflows/map-cell-type.md`) — DISCOVERY mode, per classical node,
at cluster rank (0) and supertype rank. Uses `just find-candidates <graph> <node>
CCN20230722 <rank> 50`. Emits top-K MappingEdge YAML. **Record Stage-A candidate list
(deterministic) AND the agent's final pick (full-pipeline)** for attribution (R2.b).

**5. gen-report** (`workflows/gen-report.md`) — filter top-K → ≤3 survivors + verdicts.
Single dispatched agentic session. Writes verdicts back to the throwaway blind graph.

**6. Leakage transcript audit** — inspect each dispatched subagent transcript for any
retrieval naming a target cluster's classical identity; log incidents.

**7. Score + write findings** — recovery rate (cluster + supertype rank) vs answer_key.json;
confidence calibration; divergence analysis (biology-hard vs system failure); Stage-A-vs-final
attribution. Write `README.md` (methodology + findings, per methods_audits README checklist)
+ reproducibility metadata (git commit, configs, timestamps). Assemble the paper results
bundle for §4.1 (recovery cluster+supertype, at_blind baseline, census table, stability=single-run note).

**8. Teardown** — RESTORE ground truth (BLINDING_STATE.md § Restore), confirm
`git status` clean for `kb/graphs/cerebellum/`, delete/leave-uncommitted the throwaway
`kb/graphs/cerebellum_blind/**` + `references/cerebellum_blind/**`. Commit ONLY
`research/validation/methods_audits/cerebellum_blind/**`. Pull before push (shared branch).

---

## Watch-outs

- Subagent steps MUST be dispatched via Agent tool with explicit `subagent_type`, never
  inline (CLAUDE.md). If Agent dispatch is unavailable, abort with a diagnostic.
- The pre-write hook blocks KB YAML whose quote_key/PMID aren't in the region
  references.json — so Step 2 must populate `references/cerebellum_blind/references.json`
  before Step 3b writes.
- `map-cell-type` / `find-candidates` need `taxonomy_id CCN20230722` (NOT the graphs'
  typo'd CCN202307220). The blind graph should carry the correct id.
- Do not read the quarantined ground-truth graphs into the orchestrator context to
  "help" a subagent — that breaks the blind.
