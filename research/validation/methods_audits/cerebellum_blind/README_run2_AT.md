# cerebellum_blind — RUN 2 (AT-augmented) end-to-end blinded reconstruction

**ICBO2026 R2, second pass.** Repeats the blind reconstruction with (a) two new
dedicated ASTA PLI reports (globular, Lugaro) closing the run-1 discovery gap, and
(b) the **annotation-transfer arm** wired through end-to-end via the updated
`at_source_sets` / `at-coverage` / `emit-stage-b` machinery (issues #126/#127 from main).

- Run date: 2026-07-09
- Graph (throwaway, uncommitted): `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml`
- AT run: `at_run_20260709_kozareva_cerebellum_mmc_wmbv1`
- Compare against run 1 (marker+region only): `README.md`, `scoring_20260709.json`

## What run 2 added over run 1

1. **Discovery gap closed.** Two dedicated ASTA reports (`GLobular_PLI_Asta_report.pdf`,
   `Lugaro_PLI_asta_report.pdf`) → globular + Lugaro classical nodes. (Run 1 missed both:
   globular absent from the MLI/PLI report; Lugaro only mentioned incidentally.)
2. **`at_source_sets` authored** (quote-backed, from Osorno 2022 PMID:35578131): the
   agentic source-cluster→classical-type correspondence — MLI1_1=basket, MLI1_2=stellate,
   PLI_1=candelabrum, PLI_2=globular, PLI_3=Lugaro — against dataset GEO:GSE165371.
3. **Annotation transfer ran end-to-end**, autonomously recovering the dataset from the
   paper's accessions (see "Dataset retrieval").
4. **AT folded into Stage-A + emit-stage-b**, so the AT-anchored WMB targets surface as
   edges and drive verdicts.

## Dataset retrieval (autonomous, from paper accessions)

The Kozareva 2021 data-availability statement names Broad SCP + NeMO. The retrieval agent:
- tried **Broad SCP795** → **auth-walled** (signed-in account required) → narrated as a
  blocker, not used;
- fell back to **GEO GSE165371** (anonymous NCBI FTP, `interneuron_joint` matrix) +
  cluster labels from the public **MacoskoLab/cerebellum-atlas-analysis** GitHub repo;
- subset to the 45,555 MLI+PLI interneurons; converted to MapMyCells-ready h5ad.

This is exactly the "attempt-then-punt-with-reason" behaviour: the auth wall on SCP was a
recognised blocker, and retrieval succeeded via the GEO mirror. (Provenance:
`annotation_transfer/data/kozareva2021/retrieval_attempt.json`.)

## AT reproduced the curator's ground-truth anchors (blind)

Local MapMyCells F1 (source label → best WMB target), never given the WMB targets:

| Source (classical) | Best cluster | F1 | Answer-key F1 |
|---|---|---|---|
| PLI_1 (candelabrum) | 5178 | 0.94 | 0.942 |
| PLI_2 (globular) | 5177 | 0.88 | 0.877 |
| PLI_3 (Lugaro) | SUPT_1145 | 0.96 | 0.958 |
| PLI_3 (Lugaro) | best cluster 5180 | 0.65 | 0.654 |
| MLI2 | 5192 | 1.00 | — |
| MLI1_1 (basket) | 5188 | 0.51 (cov 0.999, pur 0.34) | (cross-cutting) |

Matching the curator's independently-derived AT anchors to within rounding — strong
evidence the blind run reproduces the ground truth on the same evidence basis. Not
leakage: source labels are Kozareva/Osorno nomenclature; WMB accessions come only from
MapMyCells (see leakage audit).

## Recovery — run 1 (marker-only) vs run 2 (AT-augmented)

| Type (difficulty; curator predicate) | Run 1 | Run 2 primary verdict | Targets recovered |
|---|---|---|---|
| candelabrum (clean; exactMatch) | 5178 #4, 1144 #5; LOW | **5178 exactMatch HIGH** + 1144 broadMatch HIGH | cluster+supt ✅ |
| globular (distributed; closeMatch) | **MISSED** | **5177 exactMatch HIGH** + 1144 broadMatch | cluster+supt ✅ |
| lugaro (supertype-level; exactMatch) | **MISSED** | **SUPT_1145 broadMatch HIGH** + 5180 closeMatch | supt+cluster ✅ |
| stellate (biology-hard; Uncertain) | 5188 #1 primary MOD; supt cut | 5188 closeMatch MOD + 1149 CrossCuttingMatch | cluster+supt ✅ |
| basket (biology-hard; CrossCuttingMatch) | 5188 only weakest survivor; primary wrong (1151); LOW | 1149 broadMatch MOD (primary) + **5188 CrossCuttingMatch** MOD | cluster+supt ✅ |
| MLI1/MLI2 classes | 5188/1151 MOD | **5192 exactMatch HIGH** + 5188 closeMatch + 1151 broadMatch | ✅ |

**Headline:** run 2 recovers **all 5 answer-key types' targets as survivors** (run 1: 3/5,
with globular+Lugaro missed and basket mis-ranked). **4 types reach HIGH confidence**
(candelabrum, globular, Lugaro, MLI2) — run 1 had **zero** HIGH (marker+region can't clear
the "no HIGH without experimental evidence" bar). The AT arm is the difference.

### Basket cross-cutting resolved honestly

Run 1's marker reasoning demoted basket's true cluster (5188) because Calb1 scored
DISCORDANT. Run 2's AT shows MLI1_1 (basket) → 5188 at coverage 0.999 but purity 0.34
(MLI1_2/stellate also lands there): the pipeline now recovers 5188 for basket and labels
it **CrossCuttingMatch** — matching the curator's own predicate — because basket and
stellate share the MLI1 transcriptomic cluster. AT converts a run-1 failure into the
biologically correct cross-cutting call.

## Predicate calibration vs curator

- candelabrum: exactMatch = curator exactMatch ✓
- basket: CrossCuttingMatch (on 5188) = curator CrossCuttingMatch ✓
- globular: exactMatch vs curator closeMatch (one step stronger — AT F1 0.88 clean)
- lugaro: broadMatch@supt vs curator exactMatch@supt (AT-anchored; cluster distributed)
- stellate: closeMatch/CrossCuttingMatch vs curator Uncertain (AT gave more resolution)

## Anti-hallucination guard (run 2)

Independent validation caught real issues before writeback: a hallucinated cluster
accession (lugaro `CLUS_5181`, prose), a verbatim quote artifact (basket), invalid
`CaveatType` enums, ungrounded wet-lab modality tokens in rationales, and marker-count /
F1-on-edge mismatches across all 6 verdict sets. Fixed via 2 focused-correction rounds +
targeted edits; all 6 reports pass LLM validation and the deterministic verdict check;
60 verdicts written back; graph validates.

## Infrastructure notes (encountered + resolved)

- BKP **web MapMyCells API returned HTTP 400** (down); switched to **local**
  `cell_type_mapper` (installed via the `mapper` extra).
- Local backend needs **Ensembl gene IDs**; query h5ad used symbols → remapped via
  `conf/gene_mapping_CCN20230722.tsv` (20,390 genes).
- Rare PLI clusters (5177/5180) are marker-subtle: they only surface into Stage-A top-K
  once **AT F1 is folded in** via the per-node artifact from `just at-extract-f1`
  (`research/cerebellum_blind/at/*_f1.json`). Without it, emit-stage-b attached AT
  evidence to wrong edges. This is the key wiring lesson: `at-extract-f1` (Stage-A AT
  artifact) is required in addition to registering the run, for AT-only-discriminable
  targets to become edges.

## Reproducibility

All subagent steps dispatched via Agent tool. AT run record:
`kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/`
(manifest + f1_matrix + at_results.yaml). Scoring: `../../../cerebellum_blind/scoring_run2_20260709.json`.
Final reports snapshot: `../../../cerebellum_blind/gen_report_run2_20260709/final_reports/`.
