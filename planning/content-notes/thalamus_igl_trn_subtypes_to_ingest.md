# IGL (NPY) and TRN subtype candidates: proposed split and deferrals

Date: 2026-11-26 · Branch: `content/thalamus-igl-trn-subtype-of` (PR #260)
Umbrellas: `trn_gabaergic_neuron` (TRN) and `igl_npy_geniculohypothalamic_neuron` (IGL; only candidates under the NPY class; evidencell_5 owns the rest of the IGL list)
Source runs: `research/thalamus/20261114_thalamus_trn_report_ingest/` (TRN_GABA.pdf), `research/thalamus/20261112_thalamus_igl_report_ingest/` (IGL.pdf)

**Status: stopped at the [GATE]. No nodes created.** The PR is draft. Part 1 (subtype_of on the
NPY node and the two TRN poles) is complete in the same PR.

Why the gate:
1. **Type vs gradient position, TRN.** The strongest new candidates are SOM+ (Clemente-Perez
   2017; Martinez-Garcia 2020) and CB+ core (Martinez-Garcia 2020). Martinez-Garcia puts CB+
   cells in the central zone and SOM+ cells at the edges. In Li 2020, every sensory sector
   contains an Spp1+ core and an Ecel1+ shell, and the cells form a continuum. So SOM+ and CB+
   probably align with the existing Ecel1+ shell and Spp1+ core poles. They could be the same
   types under another marker, or other positions on the same gradient, rather than new
   subtypes. A curator needs to decide this.
2. **Sectors cut across the gradient.** None of the full texts checked defines a cell
   population by sector. Each describes the core/shell split repeating inside a sector.
   Sector nodes would therefore be position-defined subsets of the parent that overlap both
   pole nodes. That is allowed (`SubtypeAssertion` claims no disjointness), but it is a
   modelling choice about which axis to split on.
3. **Count.** All the plausible TRN rows (SOM, PV-only, CB core, five named sectors) come to 8
   nodes, which is over 5.

**Quote status.**
- Every store quote listed below is a `pending` ASTA extract, except the Li 2020 keys
  `220696191_9b59d333`, `220696191_6604c52c` and `220696191_b7eca63f`, which are `verified`.
- Clemente-Perez 2017 (PMID:28591583) and Martinez-Garcia 2020 (PMID:32699410) have no quotes
  in `references/thalamus/`.
- The verbatim sentences cited for them in this note (marked †) were read from the full text
  by a subagent on 2026-11-26: Li 2020 = PMC7394718; Martinez-Garcia = PMC7394732;
  Clemente-Perez = PMC5557038 author manuscript. They must be re-verified under the clone's
  quote rules before ingest.
- Watch the IDs: PMID:32699410 is Martinez-Garcia, not Li (Li is PMID:32699411).

## Candidate table

Every row's proposed parent is `trn_gabaergic_neuron` (TRN) or
`igl_npy_geniculohypothalamic_neuron` (IGL). AXON_TARGET entries use MBA terms. MBA has no
subdivision of the reticular nucleus (MBA:262), so a sector or core/edge position is recorded
as MBA:262 with the position in `name_in_source`.

| # | proposed id / name | defining criterion | likely kind | source PMID · quote_keys | overlaps siblings? | decision |
|---|---|---|---|---|---|---|
| 1 | `trn_sst_neuron`: TRN somatostatin-expressing neuron | Marker: Sst (SOM-Cre transgene; PV-negative in most cases). Position: edge zones (Martinez-Garcia). AXON_TARGET: MBA:930 Parafascicular nucleus, MBA:51 Intralaminar nuclei, MBA:685 Ventral medial nucleus (Clemente-Perez); MBA:1020 Posterior complex (Martinez-Garcia). Ephys: weak or absent LTS burst | EMPIRICAL (transgene-defined; containment reported) | PMID:28591583 † (no store quote); PMID:32699410 † (no store quote); PMID:33645311 · 232077377_39d5ae3a (review); Cho 2025 preprint · 282307079_44a45345, 282307079_388b92b6 | **Yes.** 10–20% of somatosensory cells co-express PV (Clemente-Perez †). Edge position and higher-order targets suggest it largely coincides with `trn_ecel1_shell_neuron` (inference, not stated). SOM-Cre labels more central cells than SOM mRNA does, a developmental Cre history (Martinez-Garcia †). Cat and monkey: most TRN neurons are SOM-immunoreactive (2564943_ee27b032), so the subset reading is rodent-only | **GATE.** Either a new node or an alias/marker on the Ecel1 shell pole. Conflict to record: Martinez-Garcia has SOM edge cells inhibiting POm; Clemente-Perez has PV, not SOM, targeting PO |
| 2 | `trn_pvalb_only_neuron`: TRN PV+ SOM− neuron | Marker: Pvalb+ Sst−. AXON_TARGET: MBA:733 VPM, MBA:718 VPL, MBA:1020 PO (Clemente-Perez). Ephys: strong LTS burst | EMPIRICAL | PMID:28591583 † (no store quote); 232077377_39d5ae3a; 282307079_44a45345 | **Yes.** It likely coincides with the Spp1 core pole: first-order targets, high bursting (inference). Pvalb itself is near pan-TRN: Li † says "nearly all TRN neurons are Pvalb+"; Martinez-Garcia † gives 99.1%; Flores 2026 (285258741_478ed0bb) gives ~70% | **GATE** (decide together with row 1). A plain PV+ node is not proposed, because it would be close to equivalent to the parent |
| 3 | `trn_calb1_core_neuron`: TRN calbindin core neuron | Marker: Calb1 (CB). Position: central zone of somatosensory and visual TRN. AXON_TARGET: MBA:733 VPM | EMPIRICAL | PMID:32699410 † (no store quote) | **Yes.** Same core position and first-order target as `trn_spp1_core_neuron`. CB is in ~48% of somatosensory cells † | **GATE.** Most likely a correspondence with the Spp1 core pole (record Calb1 on that node, or a mapping), not a new subtype |
| 4 | `trn_visual_sector_neuron`: visual-sector TRN neuron (includes the carnivore perigeniculate nucleus) | Position: visual sector of MBA:262. AXON_TARGET: MBA:170 Dorsal part of the lateral geniculate complex (270555191_fc6c9672, 1225644_17e1883b); MBA:218 LP is plausible but has no quote | DEFINITIONAL (parent narrowed by sector) | PMID:38890758 (Campbell 2024) · 270555191_fc6c9672, 270555191_79dca22b; Hammer 2014 · 1225644_17e1883b; Sokhadze 2018 · 46889900_a83dbe7b (cholinergic timing by sector); Sanchez-Vives 1997 (PGN, cat/ferret) · 15405814_b54e66d7, 15405814_6a2f954f; ferret PGN PV+ (PMID:8815875) · 7411015_dc5df80b | Contains both core and shell cells (Li †: the core/shell split holds "within each functional modality"; Martinez-Garcia †: visual TRN is organised like somatosensory TRN). Disjoint from other sectors only as far as sector boundaries are | **Defer pending GATE.** It meets the bar (position + target + developmental and physiology data). Recommended if the curator chooses to split TRN by sector. Verify the Campbell quotes first |
| 5 | `trn_somatosensory_sector_neuron`: somatosensory-sector TRN neuron | Position: somatosensory sector of MBA:262. AXON_TARGET: MBA:733 VPM, MBA:718 VPL, MBA:1020 PO | DEFINITIONAL | Lam 2011 (PMID:21543609) · 17803026_048c557a (three input tiers from POm/VPM/VPL); Yen 1985 (cat) · 11351142_bb87302f (axons to VP and posterior nuclei); Gao 2024 · 271245495_d8c25eae ("sensory" TRN PV cells; not specific to the somatosensory sector) | As row 4 (core/shell inside the sector) | **Defer pending GATE.** It meets the bar. Recommended together with row 4 |
| 6 | `trn_auditory_sector_neuron` | Position: auditory sector. AXON_TARGET: MBA:475 Medial geniculate complex | DEFINITIONAL | Pazo 2013 · 45471682_d26faa77 (sector named only) | As row 4 | **Defer.** Name + position only, below the bar |
| 7 | `trn_limbic_sector_neuron` | Position: limbic sector. AXON_TARGET: MBA:239 Anterior group of the dorsal thalamus; MBA:362 Mediodorsal nucleus (232077377_979cc2e5 names MD inhibition) | DEFINITIONAL | Villalobos 2022 · 251108998_6032faf3; Inserra 2021 · 232077377_979cc2e5 | As row 4. May overlap row 1 (Clemente-Perez links SOM to AN/IL/PF circuits †) | **Defer.** Thin: one sector statement and one target statement |
| 8 | `trn_motor_sector_neuron` | Position: rostral (motor) sector, which receives GPe input. AXON_TARGET: MBA:629 Ventral anterior-lateral complex (no quote) | DEFINITIONAL | Villalobos 2022 · 251108998_6032faf3 | As row 4 | **Defer.** Position + input only; no target quote |
| 9 | Somatosensory tier neurons (inner/middle/outer, by POm/VPM/VPL input) | Position across TRN thickness; input-defined | DEFINITIONAL | Lam 2011 · 17803026_048c557a | Li † presents core/shell as the molecular basis of the tiers, so this is the same axis as the poles | **Defer.** Gradient axis already modelled by the poles |
| 10 | Convergent-input TRN neurons (~25% of somatosensory TRN, "searchlight") | Input pattern: multiple thalamic sources | EMPIRICAL | Lam 2011 · 17803026_048c557a | Spread through the TRN's thickness, so it cuts across the poles and tiers | **Defer.** A connectivity property with no marker or position |
| 11 | Gap-junction cluster networks (within-module vs across-thickness) | Coupling-cluster geometry + targets (FO and HO) | EMPIRICAL | Lee 2014 · 22250359_a2c2e373 | Network motifs, not cell populations | **Not a type.** Keep as a note on the parent |
| 12 | Intermediate DP/DN TRN neurons (Li 2020) | Spp1+Ecel1+ or Spp1−Ecel1− | n/a | PMID:32699411 · 220696191_9b59d333 (verified) | Middle of the gradient; mixed into both the core and the shell † | **Defer.** A gradient midpoint (same reasoning as PVT3 in the PVT note) |
| 13 | Anterior TRN neurons (propofol emergence) | Position: anterior TRN | DEFINITIONAL | Gao 2024 review · 269061517_bc699ba8 (secondary, citing Gui 2021) | Likely overlaps rows 7 and 8 | **Defer.** Secondary source and functional only |
| 14 | IGL `Type II` neuron (Thankachan & Rusak 2005) under `igl_npy_geniculohypothalamic_neuron` | Strong somatic NPY; light response suppressed, complex or none | n/a | PMID:16207879 · 9130790_8fa09d39 | The source suggests Type II corresponds to the NPY-producing class itself. Its anatomy is "IGL/VLG", so not contained in the IGL | **Not a subtype.** Possibly equivalent to the NPY node, possibly overlapping it. Already described in that node's notes |

No other candidate under `igl_npy_geniculohypothalamic_neuron` appears in IGL.pdf. Its
heterogeneity section treats the NPY/ENK split as the finest IGL-proper scheme. The
SCN-projecting cells identified antidromically (Blasiak 2013, 25997395_7e370bae) are the NPY
class itself.

## Decisions for the curator

1. **SOM / PV-only / CB (rows 1–3).** Options:
   - (a) Create SOM+ and PV-only as new EMPIRICAL children of `trn_gabaergic_neuron`, and
     record their overlap with the poles in the subtype_of notes.
   - (b) Treat them as other marker sets for the existing poles: add Sst / Calb1 to the
     Ecel1 / Spp1 nodes as markers, with sources, and record PV-only vs SOM as a
     correspondence in notes.
   - (c) Defer all three until an AT or Li-data check shows where Sst/Calb1 cells fall on the
     Spp1/Ecel1 axis.

   **Recommendation: (c), then likely (b).** The source that is verified and quantitative is
   the Li 2020 gradient. The SOM/CB results come from Cre lines with a documented
   developmental labelling artefact, and the two SOM papers disagree on the PO target.
2. **Sectors (rows 4–8).** Options:
   - (a) Create the visual and somatosensory sector nodes now; defer auditory, limbic and
     motor.
   - (b) Defer every sector node.

   **Recommendation: (a)** only if the curator wants the sector axis in the KB. Each node
   would get `subtype_of` → `trn_gabaergic_neuron` (DEFINITIONAL, LOW until the Campbell and
   Lam quotes are verified), notes stating that the core/shell poles cross-cut it, and
   AXON_TARGETs as in the table. That makes 2 nodes, within the gate limit.
3. **Primary verification.** Whichever option is chosen, add verified quotes first. That
   means Clemente-Perez 2017 (PMC5557038) and Martinez-Garcia 2020 (PMC7394732) as new papers,
   and the Li 2020 Pvalb/continuum/sector sentences. The additions to
   `references/thalamus/` are additive only.

## When resumed

- Continue `workflows/asta-report-ingest.md` from node characterisation in
  `research/thalamus/20261114_thalamus_trn_report_ingest/`:
  - new nodes are NEW;
  - `trn_gabaergic_neuron` and the pole nodes are ENRICH.
- `run_quotes.json` and `ingest_plan.yaml` do not exist in that run dir. Build them under the
  current workflow before writing.
- Once a node exists for a population, remove its description from the parent's notes: the
  "ADDITIONAL HETEROGENEITY" paragraph (sectors, tiers, gap-junction clusters) and the PV/SOM
  sentences in the "CONTRADICTION (Sst, species)" paragraph. Rows 9–14 stay described as
  deferred, with the reason.
- New anatomical_location entries use MBA terms (curator decision 2026-11-26; #263).
