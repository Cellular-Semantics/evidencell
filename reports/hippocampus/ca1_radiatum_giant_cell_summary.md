# CA1 radiatum giant cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml`*

---

## Introduction

The CA1 radiatum giant cell (RGC) is a rare excitatory projection neuron with soma in CA1 stratum radiatum, first described by Kirson and Yaari (2000) [1]. RGCs are glutamatergic and notable for NMDA-receptor-dependent burst firing on synaptic activation, a property that distinguishes them from canonical CA1 pyramidal neurons. The type is defined on classical multimodal grounds (anatomy + electrophysiology + neurotransmitter); no transcriptomic discriminators have yet been entered into the knowledge base, and no atlas mapping candidates have been assessed for this node.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum radiatum (UBERON:0005372) | [1] |
| NT | glutamatergic | [1] |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / NT type / electrophysiology / morphology:** Kirson & Yaari 2000 — patch-clamp recordings from CA1 stratum radiatum giant cells in rat hippocampal slices · [1]
  > a recently discovered excitatory projection neuron, the CA1 radiatum giant cell (RGC). Glutamatergic synaptic activation, even after blocking non-NMDA receptors, fired an NMDA receptor-dependent burst of action potentials in RGCs
  > — Kirson et al. 2000, Synaptic Properties and Neurotransmitter Systems · [1] <!-- quote_key: 502543_4f78ac74 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

Curator note on the classical node records additional context not yet entered as structured sources: morphology and LTP properties were independently replicated by Christie et al. 2000 (PMID:11153713); RGC identity was confirmed in mouse with CA2 pyramidal neurons identified as a strong presynaptic input by Nasrallah et al. 2019 (PMID:30943417); a reversed HCN channel expression gradient was reported by Bullis et al. 2007. Defining molecular markers are absent, and modern transcriptomic characterisation is needed before atlas mapping can be attempted.

---

## Results

No WMBv1 mapping candidates have been assessed for this classical node — the graph carries the RGC stub and its classical-literature provenance but no `MappingEdge` entries. Without defining molecular markers entered as structured properties, the discovery query (region match + NT type + defining markers) cannot be run productively; a glutamatergic-only query against CA1 stratum radiatum would return the full CA1 pyramidal supertype set without discriminating power.

No annotation transfer figure is rendered (no AT runs cited).

<details>
<summary>### Candidates audited (full top-K)</summary>

No candidates have been audited for this node. The candidate set is empty because no `MappingEdge` entries exist in the source graph.

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The CA1 radiatum giant cell is defined here on classical multimodal grounds (`definition_basis: CLASSICAL_MULTIMODAL`): an excitatory projection neuron with soma in CA1 stratum radiatum (UBERON:0005372), glutamatergic neurotransmitter phenotype, and NMDA-receptor-dependent burst firing on synaptic activation [1]. Defining molecular markers are not yet recorded on the node.

**Atlas mapping query.** No candidate atlas clusters have been retrieved for this node. The WMBv1 taxonomy (CCN20230722) discovery query is intended to score candidates on region match, NT type, defining markers, and sex bias; with no defining markers on the classical node, the query has not been executed.

**Property alignment.** No property comparisons exist (no edges).

</details>

---

## Discussion

The CA1 radiatum giant cell is an unambiguously documented but molecularly under-characterised type. Mapping to WMBv1 will require: (i) entry of additional structured anatomy and electrophysiology sources from the replicate literature already noted on the node (Christie et al. 2000; Nasrallah et al. 2019; Bullis et al. 2007), and (ii) a targeted literature search or re-analysis of CA1 single-cell data for transcriptomic markers that distinguish RGCs from CA1 pyramidal neurons in stratum pyramidale. Once defining markers are entered, the standard discovery query can be run and candidate edges emitted.

This node is a strong candidate for a new Cell Ontology term — a rare, named, multimodally-defined CA1 excitatory projection neuron not currently covered by CL.

### What would upgrade confidence

- **Literature curation:** add structured sources from Christie et al. 2000, Nasrallah et al. 2019, and Bullis et al. 2007 to the classical node's electrophysiology, morphology, and connectivity properties.
- **Targeted marker search:** a cite-traverse for transcriptomic characterisation of CA1 stratum radiatum projection neurons; if no primary transcriptomic study exists, flag as a discovery gap rather than a curation gap.
- **Annotation transfer evidence:** when a CA1 RGC source dataset becomes available (patch-seq or Cre-driver-targeted recordings with morphology recovery), an AnnotationTransferEvidence run against WMBv1 would directly localise the type within the CA1 supertype set.

---

## References

[1] Kirson E, Yaari Y. 2000. *Unique Properties of NMDA Receptors Enhance Synaptic Excitation of Radiatum Giant Cells in Rat Hippocampus.* J. Neurosci. 20(13):4844–4854. PMID:10864941. DOI:10.1523/JNEUROSCI.20-13-04844.2000.
