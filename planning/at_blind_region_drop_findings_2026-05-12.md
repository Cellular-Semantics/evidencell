# AT-blind audit: region_drop investigation (2026-05-12)

Quick note captured before app restart. Run artifact:
`research/validation/methods_audits/at_blind/runs/latest.json` (commit `bbff337`).

## Headline

Pass rate moved 84.2% (19 cases) → 46.9% (32 cases). **Not a regression** —
all 7 cases present in both runs hold their pass/fail reason. The drop is
because **13 newly-curated AT edges entered the test set** and 11 of them
fail with `region_drop`.

## What the region_drops have in common

All 11 region_drops are hippocampus GABAergic source nodes whose AT
target is a **cortical-MGE atlas subclass/supertype**:

| Source nodes | Target | Target label | Target anat (MBA) |
|---|---|---|---|
| olm_cell_ca1, hippocampo_septal, lth, oriens_oriens, p_lm, r_lm, hippocampo_septal_cell_ca1 (7) | `CS20230722_SUBC_053` | 053 Sst Gaba | MBA:378 (SSs), MBA:993 (MOs), MBA:985 (MOp) |
| pv_basket_cell_hippocampus | `CS20230722_SUBC_052` | 052 Pvalb Gaba | same cortical set |
| is_interneuron, vip_basket | `CS20230722_SUBC_046` | 046 Vip Gaba | MBA:962 (MOs L2/3) |
| cck_basket | `CS20230722_SUPT_0187` | 0187 Sncg Gaba_3 | MOs, MOp |
| axo_axonic | `CS20230722_SUPT_0204` | 0204 Pvalb chandelier Gaba_1 | MBA:961 (Piriform) |

Parent class for SUBC_046/052/053 is `CS20230722_CLAS_07` — literally
"**07 CTX-MGE GABA**", a pan-telencephalic MGE class whose anatomy
annotation in CCN20230722 reflects only the *dominant* (cortical) source
of cells, even though hippocampal Sst/Pvalb/Vip/CCK interneurons cluster
into the same subclasses.

## Why parent+1 region expansion can't bridge this

Source-side seeds are layer-precise UBERON soma terms only:

- `UBERON:0014548` pyramidal layer of CA1 → `MBA:407`
- `UBERON:0014550` pyramidal layer of CA3 → `MBA:495`
- `UBERON:0005381` DG granule cell layer → `MBA:632`

Expansion by one MBA parent reaches CA1 / CA3 / DG fields. The target's
annotated MBAs are SSs / MOs / MOp — a different MBA subtree whose
nearest common ancestor with CA1sp is `MBA:997` (brain). No single-parent
walk bridges this.

## Higher-level fallback also fails

`just find-candidates ... olm_cell_ca1 CCN20230722 rank=2 top_k=15` returns
14 candidates **all with score 0**. SUBC_053 is not among them — its sibling
SUBC_050 (Lamp5 Lhx6 Gaba) and SUBC_048 (RHP-COA Ndnf Gaba) survive only
because they carry **no MBA annotation at all** (treated permissively),
showing `region_fraction: 0.0`. SUBC_052/053 *do* carry MBAs (cortical)
and so fail the hard region intersection. So:

- Targets with anat = ∅ → survive region filter, score = 0 (marker pipeline didn't fire).
- Targets with cortical anat → hard-dropped.

The hard-drop happens before any marker scoring, so we can't even rank
the biological siblings.

## Two interacting curation realities, not a code bug

1. **Atlas side:** subclass-level anatomy in CCN20230722 is dominant-region,
   not all-region. Sst Gaba *does* live in hippocampus, the annotation
   doesn't say so.
2. **KB side:** our hippocampus interneuron nodes use sublayer-precise
   UBERON soma terms only — no broader anchor (e.g. UBERON:0002421
   hippocampal formation) sits on the node.

## Candidate directions (not yet decided)

- **A. Permissive expansion on source side.** When a node's anat sits
  entirely under a single broad UBERON class, auto-include the broad
  ancestor as a permissive query MBA. Cheap. May over-broaden.
- **B. Curate broader anat anchors** on classical KB nodes
  (an Ammon's horn-level entry alongside layer-specific compartments).
  Most correct long-term. Curation churn.
- **C. Treat region as soft, not hard,** when the target carries a
  pan-telencephalic class tag (e.g. CTX-MGE GABA) and source NT/markers
  align. Most biologically accurate, hardest to encode.
- **D. Treat targets with empty anat the same as targets with
  cortical-MGE class** — i.e. don't let "anat = ∅ survives, anat =
  cortical fails" be the deciding factor for cluster siblings in the
  same class.

## CRITICAL UPDATE: subclass anat is mis-rolled-up (or not rolled up at all)

Inspecting the AT evidence written on each edge, the targets at
**supertype and cluster level are correctly hippocampal**, but the
**subclass anatomy in the taxonomy DB is cortical-only**:

| Target | Level | DB anat | Hippocampus? |
|---|---|---|---|
| `SUBC_053` Sst Gaba | rank 2 | MBA:378 (SSs), MBA:993 (MOs), MBA:985 (MOp) | ❌ cortical only |
| `SUPT_0219` Sst Gaba_6 | rank 1 | DG poly, CA3 sr/so/sl/sp, **CA1 so** | ✅ all hippocampal |
| `SUPT_0216` Sst Gaba_3 | rank 1 | Prosubiculum, **CA1 so**, alveus, Subiculum, Post.Amyg | ✅ hippocampal/PHC |
| `CLUS_0771` Sst Gaba_3 | rank 0 | Prosubiculum, **CA1 so**, RSv5, alveus, Subiculum | ✅ hippocampal/PHC |

So the subclass-level anat **does not equal the union of its descendant
supertypes/clusters**. The ingest appears to record only the subclass's
own dominant-region annotation from the source JSON, not roll up from
children. SUBC_053 has 3 cortical MBAs while at least 6 of its
descendant clusters/supertypes are explicitly annotated to CA1
stratum oriens.

This is almost certainly a **taxonomy ingest bug**, not a find_candidates
bug.

Consequences:

- **Source anatomy is fine.** UBERON:0014552 (CA1 stratum oriens) maps
  to `MBA:399`, which appears directly in SUPT_0219 / SUPT_0216 /
  CLUS_0771. One-parent expansion isn't even needed.
- **The audit's expected target is the best-F1 hit across levels** —
  which is the SUBCLASS (F1≈0.98). The curator-chosen edge targets are
  the SUPERTYPES (F1≈0.5–0.8) which *would* survive region filtering.
- **find_candidates at rank=2 (subclass) intersects against the broken
  rollup**, so the right cell type is hard-dropped before scoring.

### Per-edge AT-level summary (the 6 SUBC_053 cases)

| Source | UBERON anat | Curator edge target (SUPT) | Best AT subclass | Best AT supertype | Best AT cluster |
|---|---|---|---|---|---|
| olm_cell_ca1 | CA1 so + CA1 slm | SUPT_0216 | SUBC_053 F1=0.983 | SUPT_0219 F1=0.759 / SUPT_0216 F1=0.488 | CLUS_0771 F1=0.649 |
| hippocampo_septal_cell_ca1 | CA1 so | SUPT_0216 | SUBC_053 F1=0.983 | SUPT_0219 F1=0.759 / SUPT_0216 F1=0.488 | — |
| oriens_oriens_cell_hippocampus | CA1 so | SUPT_0219 | SUBC_053 F1=0.983 | SUPT_0219 F1=0.759 | — |
| r_lm_cell_hippocampus | CA1 so | SUPT_0216 | SUBC_053 F1=0.983 | SUPT_0216 F1=0.488 | — |
| p_lm_cell_hippocampus | CA1 sp | SUPT_0219 | SUBC_053 F1=0.983 | SUPT_0219 F1=0.759 | — |
| lth_cell_hippocampus | CA1 so | SUPT_0219 | SUBC_053 F1=0.983 | SUPT_0219 F1=0.759 | — |

## Conclusions from discussion (2026-05-12)

### a. The upstream anatomy issue is real and not ours to fix quickly

The taxonomy DB's subclass-level anatomy is missing CA1/HPF entries
because there is almost certainly a **percent-of-cells cutoff applied
upstream in Brain Cell KG** to suppress long-tail noise — but that
cutoff is over-eager and strips legitimate (non-dominant) regional
distributions. Fixing this is upstream work in BCKG; we should not
try to patch it locally. Plan around it.

### b. F1 is not a useful "best level" metric across levels

F1 mechanically rises at higher taxonomic levels (broader bucket
captures more recall while precision stays acceptable). "best_f1 across
levels" therefore biases toward subclass/class hits, which is also
where the upstream anat rollup is most broken — exactly the wrong
trade-off.

Proposed change: drop "best-F1 across levels" as the audit's ground-truth
target. Instead, **report all AT hits with F1 ≥ 0.5 across levels** as
candidates worth investigating. The cutoff is permissive on purpose —
we want hits good enough to draft a mapping edge from, not hits good
enough to commit blindly.

### c. Weaker mappings still belong in reports

Weak / fragmented mappings (F1 < 0.5, low recall, high precision) are
useful to *write up* even when not used as primary mapping edges. They
describe how a heterogeneous source cluster fragments across the atlas
— which is itself a useful finding. Reports should surface them as
secondary mappings with the recall/precision asymmetry called out.

### d. Precision vs recall asymmetry: the Sst source is heterogeneous

The Yao 2021 `Sst` source label is a mixed population of OLM,
bistratified, HS, oriens-oriens, R-LM, P-LM, and LTH cells. At deeper
levels of CCN20230722 it legitimately splits across SUPT_0216,
SUPT_0219, and several clusters. This is **biological fragmentation**,
not bootstrap noise. From `f1_scores_best.csv`:

| Level | Target | n | recall (gp) | precision (tp) | F1 |
|---|---|---|---|---|---|
| class | 07 CTX-MGE GABA | 272 | 0.996 | 0.261 | 0.413 |
| subclass | 053 Sst Gaba | 265 | 0.989 | 0.978 | 0.983 |
| supertype | 0219 Sst Gaba_6 | 161 | 0.626 | 0.964 | 0.759 |
| cluster | 0786 Sst Gaba_6 | 28 | 0.130 | 1.000 | 0.230 |

Run config: `bootstrap_threshold: 0.0`, `n_cells_after_filter == 6398`
(no filtering). Every cell is assigned.

Dropping unassigned cells wouldn't help **here** — there are none.
Raising `bootstrap_threshold` would create an unassigned pile and lift
recall on the confidently-assigned remainder, but the OLM-cluster
recall loss is source heterogeneity, not low-confidence noise. The
proper response is **prefer precision (purity) over F1** when
the source label is known mixed.

### e. "Dropping unassigned cells" — is it justified per the source paper?

Yao 2021 (PMID:34004146, GSE185862) reports the SSv4 dataset as
"76,381 single-cell SSv4 transcriptomes **after the quality control (QC)
process**". The 76,381 cells we use as the source are already
QC-passed. The published taxonomy assigns every one of these cells a
cluster label — there is **no "Unassigned" or "low-quality" category
in Yao's published output** for the dataset we ingest. (Full STAR
Methods detail truncated in the PMC HTML; suppl. methods are in the
PDF / Cell supplementary if we need exact QC thresholds.)

Implication: the term "unassigned" in our prior discussion refers to
**MapMyCells** output, not to a Yao 2021 category. Two distinct things
that would shrink the source denominator and could be defended:

1. **MapMyCells bootstrap-probability filter.** Re-run with
   `bootstrap_threshold > 0` (e.g. 0.5 or 0.9). Cells whose target
   assignment is bootstrap-unstable across iterations become
   "unassigned". Dropping them is defensible as "we only count cells
   where MMC is confident about the cross-atlas placement". This
   would lift recall on the confidently-assigned remainder but would
   not fix the deeper issue (biological heterogeneity within the
   Yao Sst subclass).
2. **Subset by finer Yao cluster label, not subclass.** The Yao
   `Sst` *subclass* (n≈272) is a known mixed bag containing distinct
   Yao *clusters* (Sst Myh8, Etv1, Ctsc, …) that themselves correspond
   to OLM / bistratified / HS-type interneurons. Computing F1 against
   each fine Yao cluster individually would target the right WMBv1
   supertype/cluster and lift recall *biologically*. This is the
   right fix for the heterogeneity problem.

Neither matches the audit's current run setup (`bootstrap_threshold:
0.0`, aggregation by Yao *subclass* label). To verify (1) we need the
per-cell MMC output saved alongside `f1_scores_best.csv`; to do (2) we
need to re-aggregate by Yao cluster label.

**Justification status:** dropping is **not** justified on the basis of
Yao 2021 publishing a low-quality / unassigned tier — they don't. It
*is* justified on either of the two grounds above, but those are
analysis choices we make, not something we can claim Yao's authors
endorsed for this purpose.

### f. The patch-seq dataset with unassigned cells: Que 2021 (GSE142546)

Found it — `at_run_20260508_que2021_pvin_mmc_wmbv1`. This is the
**hippocampal PV interneuron patch-seq** dataset, with morphologically
confirmed types (hBC, vBC, hBIC, vBIC, AAC). The manifest reports:

> "88 QC-passed cells from 128 total"

— i.e. **40 of 128 cells (31%) were dropped at dataset-side patch-seq
QC** before MapMyCells. ~30% failure is the standard patch-seq
attrition rate (debris, multi-cell wells, low transcript counts).
Justification: patch-seq QC failures are uninterpretable
transcriptomes, not biologically informative for cluster assignment.
The retained 88 are the morphologically-confirmed and
transcriptomically-passing cohort — completely defensible.

`bootstrap_threshold` is 0.0 here too, so among the 88 retained cells
nothing is filtered post-MMC.

#### Que 2021 results — F1 *rises* with finer resolution

| Source | n | class F1 | subclass F1 | supertype F1 | cluster F1 |
|---|---|---|---|---|---|
| BC (basket) | 62 | 0.82 | 0.78 | 0.79 | **0.83** → CLUS_0739 |
| BIC (bistratified) | 20 | 0.37 | 0.38 | 0.38 | **0.80** → CLUS_0737 |
| AAC | 6 | 0.15 | 0.12 | 0.12 | 0.24 (n too small) |

This is the **opposite pattern** to Yao Sst: when the source label is
morphologically pure (patch-seq), cluster-level F1 is *highest*.
BIC's F1 rises from 0.38 (subclass) → 0.80 (cluster) because the
right WMB target is a single cluster (0737), not a subclass. Yao
Sst's F1 collapsed at finer levels because the source was mixed.

**General principle this exposes:**

- Morphologically pure source label → F1 *rises* with finer
  aggregation. Cluster-level F1 is the right summary.
- Coarse scRNA-seq source label (e.g. Yao subclass) → F1 *falls*
  with finer aggregation. Precision (purity) is the more
  honest summary at deep levels.
- A flat F1 ≥ 0.5 cutoff across levels correctly handles both:
  BC cluster (0.83), BIC cluster (0.80), Sst subclass (0.98), Sst
  supertype 0219 (0.76) all pass; AAC (n=6) and Sst cluster don't.

#### Follow-up to do (not in this session)

Re-aggregate the Yao 2021 run by Yao *cluster* label (Sst Myh8, Sst
Etv1, Sst Ctsc, etc.) and re-score F1. Hypothesis: finer Yao labels
will match WMBv1 cluster/supertype with much higher F1 than the
current Sst-subclass-aggregated run, mirroring the Que 2021 pattern.
This also gives us per-source-cluster mappings into KB — much closer
to literature-defined classical types than the Sst-as-a-whole
subclass label.

### g. Harris/Chamberland (GSE99888): 84% "unassigned" is *not* a QC tier

`at_run_20260506_harris_chamberland_mmc_wmbv1` (Harris 2018 CA1 IN
scRNA-seq, re-labelled with Chamberland 2024 gene-pair subfamily
rules). 3663 cells total. Per-cell subfamily counts from
`labels_chamberland_subfamily.json`:

| Subfamily | n | % |
|---|---|---|
| unassigned | 3089 | **84.3%** |
| Sst_Nos1 | 259 | 7.1% |
| Sst_Tac1 | 114 | 3.1% |
| Ndnf | 112 | 3.1% |
| Chrna2 | 89 | 2.4% |

The "unassigned" pile is **not a QC failure pile**. Harris QC-passed
all 3663 cells and assigned each a Harris Class. "Unassigned" means
the cell did not satisfy any Chamberland gene-pair criterion. Two
confounded reasons:

1. **Biological non-subfamily cells** — Harris Classes that genuinely
   aren't Chrna2-OLM / Ndnf / Sst::Nos1 / Sst::Tac1.
2. **scRNA-seq dropout** on the gene-pair markers — false negatives.

The manifest's primary result uses the per-cluster derivation
(`f1_matrix_chamberland_by_class.csv`, labels `Sst_other` / `non_Sst`
instead of `unassigned`) to address (2): apply the rules to
cluster-mean expression, dropout-robust.

**Is dropping the 3089 unassigned cells justified?**

Only with the right scoping rule. The legitimate framing is "for cells
whose Harris Class is the **parent / ambiguous Class** of the target
Chamberland subfamily, drop — those are likely dropout-affected
candidates for the subfamily". For cells whose Harris Class is a
**clearly distinct subtype** (e.g. a Pvalb-something Class when scoring
Sst::Nos1), **do not drop** — they're real precision contaminants that
should count against the subfamily's precision.

A blanket "drop unassigned" rule inflates precision artificially by
removing legitimate distinct-subtype cells from the denominator. The
per-cluster variant in this run partially encodes this nuance via
`class_to_subfamily.tsv` plus the Sst_other / non_Sst bucketing.

**Headline per-cluster (dropout-robust) results** (from manifest):

- Chrna2 → CLUS_0771 (F1 0.65, recall 0.81) — Chrna2-OLM cluster.
- Sst::Nos1 → CLUS_0859 Sst Chodl Gaba_4 (F1 0.97) — alveus
  long-range projecting; **crosses supertype** (Sst Chodl, not Sst
  Gaba), biologically consistent.
- Sst::Tac1 → Pvalb subclass (subclass-level recall 0.78) — Sst-Pvalb
  continuity for bistratified types.
- Ndnf::Nkx2-1-OLM — not resolved at any single WMBv1 cluster.

These confirm the pattern: **fine, biologically-grounded source
labels (Chamberland subfamilies, Que 2021 morphological types) produce
high cluster-level F1, often crossing subclass/supertype boundaries in
ways that make biological sense** (Sst::Nos1 → Sst Chodl, Sst::Tac1 →
Pvalb). Subclass-aggregated runs (Yao Sst as a whole) cannot deliver
this because the source label is too coarse.

### h. Bundling AT + relabel in one run is an anti-pattern

The Harris/Chamberland run conflates two distinct steps:

1. A real annotation-transfer step: Harris cells → WMBv1 via MapMyCells
   (one set of per-cell MMC assignments).
2. A relabel step: Harris Class → Chamberland subfamily via gene-pair
   rules.

The three F1 matrices (`f1_matrix_harris_class.csv`,
`f1_matrix_chamberland.csv`, `f1_matrix_chamberland_by_class.csv`) all
live under one run id, with the relabel logic encoded only in
`source_cluster_label` prose and `class_to_subfamily.tsv`. Citing one
matrix from a MappingEdge is awkward — you can't say which scoring
slice is meant without prose.

**Future structure:** two `AnnotationTransferRun` records sharing the
same `mmc_results.csv`:

- `…harris_class_mmc_wmbv1` — source label = Harris Class. Pure AT.
- `…chamberland_subfamily_mmc_wmbv1` — source label = Chamberland
  subfamily (specify per-cell or per-cluster derivation), drop policy
  explicit. The relabel rule is *the* documentation of this run.

Schema permits this — `output.relpath` is required but not unique per
run (see `schema/celltype_mapping.yaml` AnnotationTransferRun /
OutputReference). Cross-mapping (which Harris Class maps to which
Chamberland subfamily) lives in manifest notes plus `class_to_subfamily.tsv`.
Promoting Chamberland subfamilies to `CellTypeNode`s is a separate
decision tracked in the Phase 2 plan, not a precondition for the
split.

## Revised priority (2026-05-12 plan)

Execution is two phases. See `/Users/do12/.claude/plans/extend-the-findings-doc-humble-haven.md`
for the full plan; summary here:

**Phase 1 (code + cleanup).**

1. Drop `best_mapping_level` from the audit's expected-target logic.
   Expand each AT-evidenced edge into one test case per `metrics_by_level`
   entry with `f1 ≥ 0.5`. (See B1 of the plan; touches
   `src/evidencell/validation/at_blind.py`.)
2. `find_candidates` region filter at rank ≥ 1: when the candidate's
   own `anat` misses, fall back to the union of `anat` over its rank-0
   descendants before declaring `region_drop`. Workaround for the BCKG
   over-strip; **remove once BCKG ships the fix** (see § a). Touches
   `src/evidencell/taxonomy_db.py`.
3. Add `at_f1_monotonicity` diagnostic to audit outcomes —
   `rises_with_resolution` vs `falls_with_resolution` flags source-label
   purity (Que 2021 pattern vs Yao Sst pattern).
4. Sweep KB graphs to remove `best_mapping_level` / `best_target_*`
   summary fields from ANNOTATION_TRANSFER blocks; `metrics_by_level`
   is the source of truth.
5. Update `workflows/validation/at_blind.md`,
   `workflows/annotation-transfer.md`, `workflows/map-cell-type.md`.

Phase-1 audit re-run is the apples-to-apples baseline vs. current
`latest.json`.

**Phase 2 (data).** Run after Phase-1 audit baseline so deltas are
attributable.

1. Split Harris/Chamberland run into two `AnnotationTransferRun`s (§ h).
2. Re-aggregate Yao 2021 SSv4 by Yao **cluster** label, not subclass
   (§ d, § f).
3. Promote Chamberland subfamilies to `CellTypeNode`s — Chrna2-OLM,
   Ndnf-OLM, Sst::Nos1-IN long-range, Sst::Tac1-IN — with mapping
   edges to WMBv1 targets and to overlapping classical types.

**Out of scope here.** Upstream BCKG anat-rollup fix (different repo,
slower turnaround). Filing a BCKG issue is a side task; reference it
from § a once it exists.

## Quick reproduction

```bash
just validate-at-blind
just find-candidates kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml olm_cell_ca1 CCN20230722 2 15
sqlite3 kb/taxonomy/CCN20230722/CCN20230722.db "SELECT node_id,label,parent_id FROM nodes WHERE node_id IN ('CS20230722_SUBC_053','CS20230722_SUBC_052','CS20230722_SUBC_046','CS20230722_CLAS_07');"
sqlite3 kb/taxonomy/CCN20230722/CCN20230722.db "SELECT DISTINCT anat_id FROM anat WHERE node_id='CS20230722_SUBC_053';"
```
