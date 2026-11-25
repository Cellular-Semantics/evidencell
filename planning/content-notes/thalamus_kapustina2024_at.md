# Kapustina 2024 ATN scRNA-seq — AT interpretation notes

Source: Kapustina et al. 2024, *The cell-type-specific spatial organization of
the anterior thalamic nuclei of the mouse brain*, Cell Rep 43:113842
(PMID:38427564, doi:10.1016/j.celrep.2024.113842).

AT runs (→ WMBv1, CCN20230722), registered 2026-11-17:
- `kb/annotation_transfer_runs/at_run_20261117_kapustina2024_atn_mmc_wmbv1/`: single label `ATN`
- `kb/annotation_transfer_runs/at_run_20261117_kapustina2024_atn_derivedk3_mmc_wmbv1/`: derived `derived_k3_{0,1,2}` (same `mmc_results.csv`)

Branch: `content/thalamus-at-kapustina2024`.

Tags: `#annotation-transfer` `#thalamus`

## The blocker: no per-cell labels in GEO

- GSE227627 provides `merged_counts` (UMI, Ensembl IDs) and `metadata`
  (well, barcode, animalId, source). It has **no cluster or nucleus column**.
- The paper's AD / AV / AM clusters therefore can't be scored as published.
- The publisher full text (STAR Methods: data and code availability) wasn't
  retrievable in-session. Europe PMC has only the abstract (not in PMC), and
  the cell.com PDF fetch was blocked.
- The ASTA MCP server wasn't available in-session either, so snippet search
  couldn't be used to look for a cluster-assignment table.

## What was done

1. `ATN` label: every QC-passed cell (912). It is declared as `at_source_sets`
   (SUPERSET) on `anterior_thalamic_nucleus_excitatory_neuron`.
2. Derived 3-group partition, neutrally named and descriptive only. It is
   **not** declared on AD / AV / AM.
   - The KB markers (Hintiryan 2025) don't name the groups independently:
     Pvalb and C1ql2 co-peak in the same group, and Rspo2 and Htr2a are
     undetected.
   - Naming the groups from their WMB landing would be circular, the same
     anti-pattern as Phillips Vis_1 → dLGN.

## Readings (WMB anatomy-based, not independent)

- AV ↔ supertype 0642 AV Col27a1 Glut_1 (clusters 2615, 2616). Strong:
  derived_k3_1 F1 0.93.
- AM ↔ 0662 TH Prkcd Grin2c Glut_9 (clusters 2676, 2674, 2675). Good:
  derived_k3_2 F1 0.80.
- AD ↔ 0641 AD Serpinb7 Glut_1 (cluster 2614). Thin: only 38 cells, with
  no separate derived group.
- Edge catches: 0652 (IAD/MD/CM), 0658 (LD), 0670 (RE).

## TODO

- [ ] F1 [GATE] review (draft PR)
- [ ] Obtain the authors' per-cell cluster assignments (STAR Methods / code
      repository / contact the Cembrowski lab). Then re-score the same
      `mmc_results.csv` as a new run and declare AD/AV/AM `at_source_sets`
      with paper quotes.
- [ ] Xenium companion GEO:GSE255953 (out of scope here). It may carry
      nucleus-annotated cells.
- [ ] map-cell-type on the four ATN nodes. No edges exist yet, so
      emit-stage-b will pick up the `ATN` AT evidence for the parent.
