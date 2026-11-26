# Gao et al. 2023 PVT → WMBv1 (CCN20230722): annotation transfer

**Status: mapped and scored; awaiting the F1-matrix `[GATE]`.** No
`at_source_sets` declared and no nodes created yet.

Run records (one shared MapMyCells output):

- `kb/annotation_transfer_runs/at_run_20261126_gao2023_pvt_pooled_mmc_wmbv1` (pooled "PVT"; holds `mmc_results.csv`, scripts and the reproduction recipe)
- `kb/annotation_transfer_runs/at_run_20261126_gao2023_pvt_cluster_mmc_wmbv1` (PVT1–5)
- `kb/annotation_transfer_runs/at_run_20261126_gao2023_pvt_ap_mmc_wmbv1` (paper's AP grouping)

## This directory

- `scripts/`: `fetch_inputs.sh`, `build_gao2023_h5ad.py`,
  `derive_gao2023_labels.py`. These are the working copies; the vendored
  copies are in the pooled run record's `scripts/`.
- `derived/`: derivation outputs:
  - `derivation_report.md`;
  - `phase2_identity.tsv`: PVT vs neighbour naming;
  - `phase3_leiden_diagnostic.tsv`: unsupervised re-clustering, which does
    not recover PVT1–5;
  - `pvt_assignment.tsv`: per-nucleus z-scores and margin;
  - `validation_heldout.tsv` and `marker_check.tsv`: agreement with
    Supplementary file 1c.

  The label JSONs live in the run records.

## Why the labels are derived

GEO:GSE208707 deposits counts and the paper's phase-1 labels only
("Neurons (1)…(8)"). PVT1–5 and the phase-2 neuron clusters are not
deposited. Re-derivation uses only the paper's methods and its published
markers: the Results identity markers, the Figure 1-figure supplement 2 ISH,
and the Supplementary file 1c DEG tables. Labels were frozen before the
MapMyCells output was opened.

## Quote verification (important for the PVT nodes)

The quote store held 12 ASTA-extracted Gao 2023 quotes (status `pending`).
Against the eLife version of record (Europe PMC full text, PMC10014079,
same 7 authors as the store's paper record):

- **Verbatim (2):** 251021326_f573a2e9 and 251021326_36b93bd8 (abstract).
- **Paraphrase (2), with ~60–70% of 8-word windows matching:**
  251021326_1e273142 and 251021326_867de772.
- **Not in the paper (8; no 8-word window matches):**
  251021326_815dcc71, _17100715, _6e3c6191, _ecb498e7, _3d4954d5, _5ed06f40,
  _19d51130 and _6820b736. They also contradict the paper's own data:
  - Thy1, Cxcl14, Cbln2 and Tesc are not PVT DEGs in Supplementary
    file 1c. None is in the Methods RNAscope probe list (Esr1, Col12a1,
    Insrr, Hcrtr1, Drd2, Npffr1, Npsr1, Pde3a) or in the Figure 3 ISH,
    which adds Drd3.
  - The quoted AP assignment ("PVT4, PVT2, and PVT5" anterior; PVT3
    middle) is the opposite of the paper's: PVT1/PVT2 posterior,
    PVT3/PVT4 anterior, PVT5 pan-PVT.
  The bioRxiv preprint (10.1101/2022.07.19.500649) could not be fetched
  (Cloudflare block). It has the same abstract and dataset, but a preprint
  origin cannot be ruled out entirely.

The 8 quotes feed the existing aPVT / pPVT / umbrella nodes (#253) and the
content note's PVT1–5 table. Corrections are proposed in the PR, not made
here.

Verified replacements (status `verified`, source EUROPEPMC_FULLTEXT):

| key | content |
|---|---|
| 251021326_6ecf0efa | ISH markers: Esr1 (PVT1), Col12a1 (PVT2), Npffr1 (PVT3), Hcrtr1 (PVT4), Drd3 (PVT5) |
| 251021326_d84aa264 | AP: PVT1/PVT2 pPVT; PVT3/PVT4 aPVT-biased, gradient into dorsal pPVT; PVT5 pan-PVT |
| 251021326_644f9bee | PVT4 antero-medial, PVT3 antero-lateral, PVT1 dorso-ventral pPVT, PVT2 ventral edge of pPVT |
| 251021326_1fef2fe7 | second marker set: Drd2 (PVT1), Pde3a (PVT2), Insrr (PVT3), Npsr1 (PVT4) |
| 251021326_a1d0eb44 | ≤ 30% single-cell overlap among subtype marker sets |
| 251021326_072fd9a0 | PVT structured by AP, DV and ML gradients |
| 251021326_9034ddfa | ThalamoSeq overlap: PVT1/PVT2 with PFC projectors; PVT4 auditory/visual; PVT3 prefrontal, PVT5 visual (small) |
| 251021326_a12d1cda | PL retrobead-labelled cells at the ventral edge, partially co-localised with Col12a1 |
| 251021326_f0709a5e | PVT identity markers Gck, C1ql3, Hcn1; 5,737 PVT nuclei |
| 251021326_5069b61b, _c224ece7, _9fc6bc05 | clustering phases 2 and 3 |
| 251021326_4907d87c | dissection: punches through the entire AP extent of PVT |
| 251021326_c48ad581 | 7,501 female nuclei added in revision (20,503 total) |
| 264359607_bd93f8db | Shima et al. 2023 (Cell Reports abstract): AP axis is a major variance; continuity among five types |

The three Shima quotes already in the store (264359607_8626b44b, _fa44530f
and _d839d41e) match the bioRxiv abstract, not the Cell Reports abstract
that PMID:37862168 indexes. They remain `pending`.
