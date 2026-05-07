# Bulk-correlation evidence: KB schema design

**Date:** 2026-04-28
**Status:** Implementation in progress on this branch (`sexually_dimorophic_neurons`).

---

## Context

Two paired-bulk correlation analyses now exist (Stephens 2024 Kiss1 RP3V vs ARC; Knoedler 2022 Esr1+ TRAP-seq across BNST/MeA/POA/VMH × Male/FR/FNR). Both produced cluster rankings that should land as KB-grade evidence on `MappingEdge` entries. The pattern will recur for many more bulk datasets and needs to compose with `AnnotationTransferEvidence` and other evidence types.

## Design principles

1. **Datasets are first-class, reused across many edges.** Knoedler 2022 supports edges in 4 regions; the dataset record exists once.
2. **Correlation runs are reproducibility receipts.** Inputs + method + outputs in one YAML; re-run is `python correlate.py` in the run directory against the recorded checksums.
3. **Edge evidence is a thin pointer** at run + contrast + target accession.
4. **Tight skeleton, loose interior.** Required fields enable graph queries and cross-evidence comparison. Free-form `statistics` and `metadata` slots absorb methodological diversity (Spearman ρ → KL divergence → OT → regression β → F1) without schema churn. Schema is read by agents, written by agents — typo resistance on stat keys is low value.

## Layout

```
kb/datasets/                                    # one YAML per published bulk dataset
  PMID_37934722_stephens_2024.yaml              # tree_root: BulkDataset
  GSE183092_knoedler_2022.yaml

kb/correlation_runs/{run_id}/                   # one directory per analysis
  manifest.yaml                                 # tree_root: CorrelationRun
  correlate.py                                  # the script (KB-grade reproducibility)
  data/...                                      # inputs (or symlinks/checksums)
  output/all_correlations.tsv
  README.md                                     # tight summary, links to manifest

kb/draft/{region}/*.yaml                        # mapping edges, with new BulkCorrelationEvidence entries
kb/mappings/{region}/*.yaml
```

## Schema additions to `celltype_mapping.yaml`

### Enum

```yaml
EvidenceType:
  permissible_values:
    BULK_CORRELATION:
      description: Cluster ranking from a bulk transcriptomic correlation run.
```

### EvidenceItem subclass

```yaml
BulkCorrelationEvidence:
  is_a: EvidenceItem
  attributes:
    run_ref:           { required: true }       # CorrelationRun.id
    contrast_ref:      { required: true }       # CorrelationContrast.id within the run
    target_accession:  { required: true }       # WMBv1 cluster/supertype the evidence supports
    statistics:        { range: string }        # free-form name:value map (YAML-inline)
```

`evidence_type` (`BULK_CORRELATION`), `supports`, and `explanation` are inherited required fields — `explanation` is the LLM-handoff field the report generator narrates.

### Top-level dataset and run classes

```yaml
BulkDataset:
  tree_root: true
  attributes:
    id:               { identifier: true, required: true }
    record_type:      { required: true }       # "BulkDataset"
    source_pmid:      {}                        # PMID:NNNN
    geo_accession:    {}
    technique:        { required: true }       # "TRAP-seq", "FACS-bulk", "RiboTag", ...
    species:          {}                        # NCBITaxon CURIE
    ingested_date:    { range: date }
    description:      {}
    data_files:       { range: BulkDataFile, multivalued: true, inlined: true, inlined_as_list: true }
    pools:            { range: BulkPool,     multivalued: true, inlined: true, inlined_as_list: true }
    notes:            {}
    metadata:         { range: string }        # free-form

CorrelationRun:
  tree_root: true
  attributes:
    id:                { identifier: true, required: true }
    record_type:       { required: true }      # "CorrelationRun"
    dataset_ref:       { required: true }      # BulkDataset.id
    atlas:             { range: AtlasReference,    inlined: true, required: true }
    method:            { range: CorrelationMethod, inlined: true, required: true }
    contrasts:         { range: CorrelationContrast, multivalued: true, inlined: true, inlined_as_list: true, required: true }
    script:            { range: ScriptReference,   inlined: true }
    output:            { range: OutputReference,   inlined: true }
    caveats:           {}
    metadata:          { range: string }
```

Plus thin helper classes (`BulkPool`, `BulkDataFile`, `AtlasReference`, `CorrelationMethod`, `CorrelationContrast`, `ScriptReference`, `OutputReference`) — each ~5 fields, no required-field bloat.

## Validate.py dispatch

`src/evidencell/validate.py:linkml_validate` currently hard-codes `--target-class CellTypeMappingGraph`. Update so `target_class` is selected by the file path:

| Path | target_class |
|---|---|
| `kb/draft/{region}/*.yaml`, `kb/mappings/{region}/*.yaml` | `CellTypeMappingGraph` (existing) |
| `kb/datasets/*.yaml` | `BulkDataset` (new) |
| `kb/correlation_runs/*/manifest.yaml` | `CorrelationRun` (new) |

This is the only `src/` change needed.

## Composition with other evidence

`AnnotationTransferEvidence` and `BulkCorrelationEvidence` both subclass `EvidenceItem` and attach to `MappingEdge.edge_evidence[*]`. `gen-report` enumerates `edge_evidence` and lets the LLM synthesise prose from the type's `explanation` + type-specific stats — no special-casing per evidence type. Convergent evidence on the same target (multiple datasets, multiple methods) accumulates naturally.

## Tradeoffs accepted

- **Free-form `statistics` and `metadata` maps.** Typo resistance on stat keys is gone — `rho_a` vs `rho_A` both pass. Mitigated by ship-with-conventions in dataset descriptors and example files. The downstream consumer is the LLM; it reads context, not key names.
- **`range: string` for the free-form fields.** LinkML doesn't have a clean built-in for "any nested structure"; using `range: string` declares the slot but doesn't validate inner shape. If LinkML rejects the inline-mapping syntax, fall back to a `KeyValuePair` class with `inlined_as_simple_dict: true`.

## Out of scope (for now)

- Schema for `BulkPool` referencing `OntologyTerm` for tissue / species. Pools currently carry tissue as free string; promote to OntologyTerm in a follow-up PR if cross-graph queries on tissue need it.
- `bulk-atlas-correlate` skill — promotion deferred until 3–4 datasets validate the method.
- `gen-report` enhancements to surface BulkCorrelationEvidence in the property alignment table — current `gen-report` already enumerates `edge_evidence`; the new type will land as a row by virtue of the shared parent class.
