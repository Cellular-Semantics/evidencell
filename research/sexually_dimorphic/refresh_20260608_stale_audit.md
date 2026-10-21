# Stale-location audit — sexually_dimorphic — 20260608

Edges whose `taxonomy_type` is NOT in current Stage A top-50 at the rank that matches the edge target's level.
(Rank-mismatch skips — e.g. supertype edge skipped at rank-0 cluster refresh — are filtered out; those are not stale.)
These need curator review — current proximity-aware scoring placed the cluster/supertype outside the candidate pool.

## Stale edges

### avpv_kiss1_neuron (rank0) — `edge_avpv_kiss1_neuron_to_cs20230722_clus_1915`

- **Graph**: `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`
- **taxonomy_type**: `CS20230722_CLUS_1915`
- **Skip reason**: taxonomy_type not in current Stage A top-50 at matching rank

### mpoa_esr1_neuron (rank1) — `edge_mpoa_esr1_neuron_to_cs20230722_supt_0486`

- **Graph**: `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`
- **taxonomy_type**: `CS20230722_SUPT_0486`
- **Skip reason**: taxonomy_type not in current Stage A top-50 at matching rank

### bnst_crf_neuron (rank1) — `edge_bnst_crf_neuron_to_cs20230722_supt_0358`

- **Graph**: `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`
- **taxonomy_type**: `CS20230722_SUPT_0358`
- **Skip reason**: taxonomy_type not in current Stage A top-50 at matching rank

### arc_aromatase_neuron (rank1) — `edge_arc_aromatase_neuron_to_cs20230722_supt_0486`

- **Graph**: `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`
- **taxonomy_type**: `CS20230722_SUPT_0486`
- **Skip reason**: taxonomy_type not in current Stage A top-50 at matching rank


## Refresh summary

| Node | Rank0 refreshed / skipped | Rank1 refreshed / skipped |
|---|---|---|
| `avpv_kiss1_neuron` | 5 / 7 | 6 / 6 |
| `avpv_th_neuron` | 6 / 1 | 6 / 6 |
| `sdn_poa_calbindin_neuron` | 6 / 1 | 6 / 6 |
| `mpoa_esr1_neuron` | 5 / 2 | 6 / 6 |
| `vmhvl_esr1_pr_neuron` | 5 / 2 | 7 / 5 |
| `pvn_crfr1_neuron` | 5 / 1 | 6 / 5 |
| `bnst_crf_neuron` | 5 / 2 | 6 / 6 |
| `arc_aromatase_neuron` | 5 / 1 | 5 / 6 |
| `pmv_otr_neuron` | 6 / 1 | 6 / 6 |
