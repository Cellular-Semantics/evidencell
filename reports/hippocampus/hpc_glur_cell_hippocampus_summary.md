# Hippocampal GluR cell (glutamate receptor-expressing glial-neuronal hybrid cell) — WMBv1 Mapping Report
*draft · 2026-04-29 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft.** No atlas mapping candidate has been identified for this cell type. This report describes the classical type only. Expert review required before any mapping is attempted.

---

## Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | hippocampal formation [UBERON:0002421] | [1] |
| Neurotransmitter | glutamatergic (functional AMPA/kainate receptor-mediated EPSCs) | [1] |
| Defining markers | S100b (astrocytic), Cspg4 / NG2 (OPC marker) | [1] |
| Negative markers | — (none documented) | — |
| Neuropeptides | — (none documented) | — |
| CL term | — (no CL term assigned; type does not map cleanly to neuron, astrocyte, or oligodendrocyte) | — |

**Notes on identity.** GluR cells are a functionally defined hippocampal population distinguished by two features that place them outside the standard glial and neuronal classification scheme: (i) they receive direct synaptic input — both GABAergic and glutamatergic — demonstrable by patch-clamp; and (ii) they co-express classical astrocyte and OPC markers together with neuronal genes. The defining markers listed (S100b, Cspg4) are therefore identity markers rather than positive selectors for a clean lineage; they simultaneously disqualify the cell from being a pure neuron, astrocyte, or oligodendrocyte.

> "GluR cells co-expressed S100β, a common astrocyte marker, NG2, as well as neuronal genes, and hence escaped classification into neurons, astrocytes, or oligodendrocytes"
> — Jabs et al. 2005, Specialized Glutamatergic Populations · [1] <!-- quote_key: 15354140_479e5693 -->

> "All GluR cells tested expressed NG2, while about 30% of them were S100β-positive"
> — Jabs et al. 2005, Specialized Glutamatergic Populations · [1] <!-- quote_key: 15354140_75c073f3 -->

> "Sub-threshold stimulation to Schaffer collaterals resulted in stimulus-correlated, postsynaptic responses in a subpopulation of EGFP-positive cells studied with the patch-clamp technique in acute slices"
> — Jabs et al. 2005, abstract · [1] <!-- quote_key: 15354140_c1bc8ebc -->

---

## Mapping candidates

No mapping candidates have been identified for this cell type.

The GluR cell poses an unusually difficult mapping problem for the WMBv1 transcriptomic atlas (CCN20230722). Transcriptomic atlases assign cells to discrete clusters based on gene expression profiles; cells that bridge lineage compartments — expressing marker suites characteristic of both glia and neurons simultaneously — may not partition cleanly into any single cluster or even into a single subclass. The WMBv1 atlas uses a hierarchical taxonomy with class-level separation between neuronal and non-neuronal lineages; a cell that co-expresses S100b, Cspg4, and neuronal genes may map with low confidence or may be distributed across multiple lineages depending on the dominance of one expression programme over the other in any given cell. No candidate edge has been opened.

---

## What a mapping search would require

Because the GluR cell sits at the intersection of glial and neuronal gene programmes, standard `find-candidates` queries using neuronal marker sets (e.g., vGluT1/Slc17a7-based glutamatergic subclasses) are unlikely to be sufficient. A productive mapping search would require the following:

1. **Dual-programme marker cross-check.** Any candidate cluster must be evaluated both for glutamatergic receptor expression (functional AMPA/kainate input) and for co-expression of S100b and Cspg4. These are atypical combinations in a single transcriptomic cluster; if they appear in the same cluster they point strongly at a genuine GluR cell match.

2. **NG2/Cspg4-expressing cluster survey.** In WMBv1, Cspg4 (NG2) is primarily expressed in oligodendrocyte precursor lineages. A first-pass search should query the taxonomy DB for clusters in the non-neuronal branch that show high S100b co-expression — this covers the astrocyte-NG2 glia hybrid side of the GluR cell identity.

3. **Functional electrophysiology evidence.** The defining criterion is synaptic glutamatergic input, demonstrated by NBQX-sensitive EPSCs. A scRNA-seq or MERFISH atlas cluster cannot directly encode this, but patch-seq datasets anchoring transcriptomic identity to electrophysiology could identify which cluster(s) receive functional glutamatergic synaptic drive.

4. **Annotation transfer from a GluR cell dataset.** MapMyCells (WMBv1 CCN20230722) applied to a transcriptomically profiled GluR cell dataset — ideally single-cell RNA-seq of patch-clamped EGFP+ cells from hGFAP-EGFP mice — would produce an unbiased cluster assignment. No such public dataset was identified in the current evidence corpus.

5. **Literature search for NG2 glia hippocampal transcriptomics.** NG2 glia (polydendrocytes) have been characterised transcriptomically in several atlas datasets. Whether WMBv1 NG2 glia clusters carry the electrophysiological signature of GluR cells is an open question addressable by targeted literature search on "NG2 glia synapse hippocampus transcriptomics" or "polydendrocyte glutamatergic synapse single cell."

---

## Open questions

1. **Do GluR cells form a reproducible, discrete transcriptomic cluster?** The original characterisation by Jabs et al. 2005 [1] identified GluR cells by functional criteria (Schaffer collateral-evoked EPSCs in hGFAP-EGFP+ cells) in a small sample. It is unknown whether all such cells share a single transcriptomic identity or whether "GluR cell" describes a functional state that can be adopted by cells from multiple glial lineages. This is the prerequisite question for any atlas mapping effort.

2. **Is the S100b/NG2 co-expression stable at the single-cell level?** The quoted figure is that approximately 30% of NG2+ GluR cells co-express S100b [1]. Whether the remaining ~70% represent a distinct population with a different transcriptomic profile — and thus different atlas targets — is not resolved by the current evidence.

3. **What is the developmental origin of GluR cells?** If GluR cells are derived from a glial progenitor (as their NG2/S100b phenotype implies), they would be expected to cluster with non-neuronal lineages in transcriptomic atlases. If instead they derive from a neuronal progenitor that secondarily activates glial programmes, the mapping target would be in a neuronal branch. Evidence for a definitive lineage assignment is absent from the current reference set.

4. **Is the GluR cell phenotype reproducible outside the original hGFAP-EGFP transgenic mouse model?** All primary evidence comes from a single mouse line and a single laboratory. Independent replication in wild-type or alternative reporter lines is needed to establish GluR cells as a robust biological entity rather than a transgenic artefact.

---

## Evidence base

No mapping edges have been generated. The evidence base is restricted to classical type characterisation.

| Evidence type | Source | Covers | Notes |
|---|---|---|---|
| LiteratureEvidence | Jabs et al. 2005, PMID:16076898 [1] | NT type, markers (S100b, Cspg4/NG2), morphology, electrophysiology | Sole primary source; all classical node properties derive from this single publication |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Jabs et al. 2005 | [16076898](https://pubmed.ncbi.nlm.nih.gov/16076898/) | Soma location; neurotransmitter type; defining markers; morphology; electrophysiology |
