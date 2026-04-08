# Winterer et al. 2019 Enrichment — Session Notes

> **Date**: 2026-03-25/26
> **Status**: Partially implemented, needs restart
> **Context**: Mining PMID:31420995 (PMC6973274) to enrich OLM hippocampus KB node and build first mapping edge

---

## What was done

### references.json updated
- Added 20 new primary-source quotes from Winterer 2019 full text (PMC6973274)
- All with `source_method: "primary"`, `status: "verified"`, content-hashed keys
- Categories: marker expression, identity validation (morphology, ephys), MGE origin, dataset accession, Harris comparison
- Total Winterer quotes now: 25 (5 original ASTA report + 20 new)

### proposed_kb_hippocampus.yaml updated
- `species`: set to NCBITaxon:10090 (Mus musculus)
- `target_atlas`: set to WMBv1
- `defining_markers`: added Reln, Elfn1; Chrna2 and mGluR1 gain Winterer transcript sources
- `negative_markers`: expanded from 5 (old symbols, no sources) to 7 with proper gene symbols (Pvalb, Calb1, Calb2, Cck, Vip, Ndnf, Htr3a) and Winterer transcript sources
- `neuropeptides`: Sst, Npy, Pnoc all gain Winterer transcript sources; Npy also gets protein-level confirmation (3/5 OLM cells)
- `notes`: added developmental origin (MGE), transcriptomic identity summary, dataset accessions (GSE124847, GSE99888), species difference (Npy rat vs mouse)
- `definition_references`: added PMID:31420995

### New node added: winterer_olm_2019
- `definition_basis: PRIOR_TRANSCRIPTOMIC`
- `prior_dataset_accession: GEO:GSE124847`
- Markers include MGE developmental TFs (Lhx6, Satb1, Sox6) as defining markers with modifier: ENRICHED
- Notes capture three-step identity validation protocol (transgenic pre-selection → morphological reconstruction → ephys profiling)

### New edge added: edge_olm_to_winterer_olm
- `olm_hippocampus → winterer_olm_2019`, EQUIVALENT, HIGH confidence
- 3 evidence items: MORPHOLOGY, ELECTROPHYSIOLOGY, LITERATURE (Harris comparison)
- 7 property comparisons with node_a_value/node_b_value:
  - nt_type: CONSISTENT
  - marker_Sst: CONSISTENT
  - marker_Chrna2: CONSISTENT
  - marker_Npy: APPROXIMATE (rat negative, mouse positive — species difference)
  - anatomical_location: CONSISTENT
  - electrophysiology_class: CONSISTENT
  - developmental_origin: APPROXIMATE (classical uncertain → Winterer resolves to MGE)
- 4 proposed experiments (annotation transfer + marker analysis, with dataset accessions)
- 3 unresolved questions
- Caveat: SINGLE_DATASET

---

## What was NOT captured yet

### From the paper
1. **Neurexin splice isoforms** (section 3.7) — Nrxn1/Nrxn3 ASS3 splice profiles identical between Htr3aCre-OLM and SstCre-OLM, matching MGE pattern from Lukacsovich 2019. Independent molecular confirmation of MGE origin beyond TFs.
2. **Ion channel markers** — Kcnc2, Kcnd3, Cacna1a, Cacna1g, Gria4, Syt1+/Syt2-. Quotes exist in references.json but not added to node defining_markers. Functionally important (Syt2 absence distinguishes from PV+ cells).
3. **GABA receptor subunits** — Gabra1+, Gabrg2+, Gabra5 sparse (age-dependent).
4. **POA alternative origin caveat** — discussion raises preoptic area as possible origin (POA progenitors co-express Nkx2.1 and Htr3a). Should be unresolved_question.
5. **Htr3b transgenic artefact** — likely BAC transgene insertion effect, not biology. Lower priority.

---

## Open design question: defining_markers vs functional profile

**The tension**: `defining_markers` implies "these genes define this type" (Sst, Chrna2). But scRNA-seq provides a full transcriptomic fingerprint (dozens of genes) where individual genes aren't diagnostic but the cumulative profile is highly specific for atlas matching.

**Gene categories from Winterer**:

| Category | Genes | Identity role |
|---|---|---|
| Canonical markers | Sst, Chrna2 | Defining — necessary |
| Novel markers | Npy, Reln, Pnoc, Elfn1 | Defining — newly established |
| Ion channels | Kcnc2, Kcnd3, Cacna1a, Cacna1g, Gria4 | Functional profile — consistent |
| Synaptic | Syt1+/Syt2-, Grm1, Gabra1, Gabrg2 | Functional profile — consistent |
| Developmental TFs | Lhx6, Satb1, Sox6 | Lineage — MGE constraint |
| Neurexin splice | Nrxn1/Nrxn3 ASS3 spliced-in | Lineage — independent MGE confirmation |

**Three options discussed**:

1. **Add `transcriptomic_profile` field** (new GeneDescriptor list on CellTypeNode) — carries full expression profile separately from defining markers. Node has both: small marker set for quick matching + full profile for deep comparison. Cleanest separation but requires schema change.

2. **Use `modifier` more systematically** — DEFINING for Sst/Chrna2, ENRICHED for Npy/Elfn1, CHARACTERISTIC for ion channels/synaptic genes. Everything in `defining_markers`. Field name becomes misleading and list gets very long.

3. **Leave node lean, put full profile on edge** — `MarkerAnalysisEvidence` on the `winterer_olm_2019 → wmb_cluster_X` edge carries the full gene set comparison. Node says "Sst+, Chrna2+", edge says "here's how 30 genes compared." Loses the profile on the node itself.

**Recommendation**: Option 1. A node should carry its full characterization regardless of edges. Maps to how biologists think. Defer implementation if time-constrained.

---

## Key datasets identified

| Dataset | Accession | Paper | Relevance |
|---|---|---|---|
| Winterer OLM scRNA-seq | GEO:GSE124847 | PMID:31420995 | 46 anatomically-verified OLM cells, mouse P21-28 |
| Harris hippocampal survey | GEO:GSE99888 | Harris et al. 2018 | Broader Sst/Pvalb/Cck/Vip populations, CA1 |

Both verified from paper full text (not hallucinated).

---

## Proposed experiments (on edge_olm_to_winterer_olm)

1. **ANNOTATION_TRANSFER**: MapMyCells on GEO:GSE124847 → WMBv1 (HIGH priority)
2. **ANNOTATION_TRANSFER**: MapMyCells on GEO:GSE99888 Sst subtypes → WMBv1 (HIGH priority)
3. **MARKER_ANALYSIS**: Winterer OLM marker set vs WMBv1 Sst cluster defining_markers (MEDIUM)
4. **MARKER_ANALYSIS**: MGE developmental markers as atlas cluster filter (MEDIUM)

---

## Next steps

1. Resolve the defining_markers vs functional profile schema question
2. Add neurexin MGE confirmation + POA caveat to the KB
3. Build the next edge: `winterer_olm_2019 → wmb_sst_cluster_X` (requires identifying the target WMBv1 cluster — either via atlas browser query or by running the proposed annotation transfer)
4. Consider structuring `proposed_experiments` (currently free text strings) — discussed adding a ProposedExperiment class with experiment_type, source_dataset_accession, target_atlas, method fields + anti-hallucination loop for dataset accessions

---

## Workflow observations

- **Full cite-traverse was too expensive** for this use case. Targeted paper mining (fetch one paper's full text, extract specific evidence) was more efficient for the demo goal.
- **The PRIOR_TRANSCRIPTOMIC node pattern** (from PLI/cerebellum) works well for scRNA-seq datasets. It captures: dataset provenance, the cell type claim, and separates the identity validation evidence (classical → prior-transcriptomic edge) from the atlas mapping evidence (prior-transcriptomic → atlas edge).
- **Identity validation is critical** and should be captured explicitly. Winterer is unusually strong (patch-fill-seq with morphological confirmation). Many scRNA-seq papers only have clustering-based annotation — the edge confidence should reflect this.
- **MGE origin as mapping constraint** — this is the most consequential finding for atlas mapping. Limits candidates to MGE-derived Sst+ types, excluding all CGE-derived classes.
