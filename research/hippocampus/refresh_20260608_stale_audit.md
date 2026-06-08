# Stale-location audit — hippocampus — 20260608

Edges whose `taxonomy_type` is NOT in current Stage A top-50 at the rank that matches the edge target's level.
(Rank-mismatch skips — e.g. supertype edge skipped at rank-0 cluster refresh — are filtered out; those are not stale.)
These need curator review — current proximity-aware scoring placed the cluster/supertype outside the candidate pool.

## Stale edges

### olm_hippocampus (rank0) — `edge_olm_to_wmb_clus_0727`

- **Graph**: `kb/graphs/hippocampus/hippocampus_OLM.yaml`
- **taxonomy_type**: `CS20230722_CLUS_0727`
- **Skip reason**: taxonomy_type not in current Stage A top-50 at matching rank

### olm_hippocampus (rank0) — `edge_olm_to_wmb_clus_0785`

- **Graph**: `kb/graphs/hippocampus/hippocampus_OLM.yaml`
- **taxonomy_type**: `CS20230722_CLUS_0785`
- **Skip reason**: taxonomy_type not in current Stage A top-50 at matching rank

### olm_hippocampus (rank0) — `edge_olm_to_wmb_clus_0788`

- **Graph**: `kb/graphs/hippocampus/hippocampus_OLM.yaml`
- **taxonomy_type**: `CS20230722_CLUS_0788`
- **Skip reason**: taxonomy_type not in current Stage A top-50 at matching rank

### olm_hippocampus (rank0) — `edge_olm_to_wmb_clus_0789`

- **Graph**: `kb/graphs/hippocampus/hippocampus_OLM.yaml`
- **taxonomy_type**: `CS20230722_CLUS_0789`
- **Skip reason**: taxonomy_type not in current Stage A top-50 at matching rank

### sst_nos1_subfamily_chamberland (rank0) — `edge_sst_nos1_to_CS20230722_CLUS_0859`

- **Graph**: `kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml`
- **taxonomy_type**: `CS20230722_CLUS_0859`
- **Skip reason**: taxonomy_type not in current Stage A top-50 at matching rank

### hpc_glu_dopa_receptor_pyramidal_hippocampus (rank1) — `edge_hpc_glu_dopa_receptor_pyramidal_hippocampus_to_supt_0069`

- **Graph**: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`
- **taxonomy_type**: `CS20230722_SUPT_0069`
- **Skip reason**: taxonomy_type not in current Stage A top-50 at matching rank


## Refresh summary

| Node | Rank0 refreshed / skipped | Rank1 refreshed / skipped |
|---|---|---|
| `dg_granule_cell` | None / None | None / None |
| `dg_mossy_cell` | None / None | None / None |
| `ca3_pyramidal_cell` | None / None | None / None |
| `ca1_pyramidal_cell` | None / None | None / None |
| `ms_dbb_glutamatergic_neuron` | None / None | None / None |
| `hpc_cajal_retzius_cell` | None / None | None / None |
| `ca1_radiatum_giant_cell` | None / None | None / None |
| `ec_layer3_pyramidal_cell_hippocampus` | 5 / 5 | 5 / 5 |
| `olm_hippocampus` | 5 / 5 | 5 / 5 |
| `pv_basket_cell_hippocampus` | 6 / 1 | 5 / 6 |
| `cck_basket_cell_hippocampus` | 5 / 2 | 6 / 5 |
| `axo_axonic_cell_hippocampus` | 5 / 1 | 6 / 5 |
| `bistratified_cell_hippocampus` | 5 / 5 | 5 / 5 |
| `olm_cell_ca1` | 5 / 1 | 5 / 5 |
| `hippocampo_septal_cell_ca1` | 5 / 1 | 5 / 5 |
| `neurogliaform_cell_hippocampus` | 5 / 2 | 6 / 5 |
| `ivy_cell_hippocampus` | 5 / 5 | 5 / 5 |
| `is_interneuron_hippocampus` | 5 / 1 | 5 / 5 |
| `oriens_oriens_cell_hippocampus` | 5 / 1 | 6 / 5 |
| `trilaminar_cell_hippocampus` | 5 / 1 | 5 / 5 |
| `vip_basket_cell_hippocampus` | 5 / 1 | 6 / 5 |
| `r_lm_cell_hippocampus` | 5 / 1 | 5 / 5 |
| `p_lm_cell_hippocampus` | 5 / 1 | 5 / 5 |
| `lth_cell_hippocampus` | 5 / 1 | 5 / 5 |
| `olm_hippocampus` | 6 / 9 | 5 / 10 |
| `chrna2_olm_subfamily_chamberland` | 6 / 0 | 5 / 6 |
| `ndnf_nkx2_1_olm_subfamily_chamberland` | 5 / 1 | 6 / 5 |
| `sst_nos1_subfamily_chamberland` | 5 / 1 | 5 / 6 |
| `sst_tac1_subfamily_chamberland` | 5 / 1 | 5 / 6 |
| `ca1_pc_hippocampus` | 5 / 1 | 6 / 5 |
| `ca2_pc_hippocampus` | 5 / 1 | 6 / 5 |
| `ca3_pc_hippocampus` | 5 / 1 | 6 / 5 |
| `dg_granule_cell_hippocampus` | 5 / 1 | 6 / 5 |
| `hilar_mossy_cell_hippocampus` | 5 / 2 | 7 / 5 |
| `dg_semilunar_granule_cell_hippocampus` | 5 / 2 | 7 / 5 |
| `subicular_pyramidal_cell_hippocampus` | 5 / 1 | 6 / 5 |
| `ec_layer2_stellate_cell_hippocampus` | 5 / 1 | 6 / 5 |
| `ec_layer2_pyramidal_cell_hippocampus` | 5 / 1 | 6 / 5 |
| `ec_layer3_pyramidal_cell_hippocampus` | 5 / 2 | 7 / 5 |
| `hpc_calretinin_glu_neuron_hippocampus` | 5 / 1 | 6 / 5 |
| `hpc_glu_dopa_receptor_pyramidal_hippocampus` | 5 / 1 | 5 / 6 |
