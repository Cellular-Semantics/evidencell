# Entorhinal Cortex Layer II Calbindin-Positive Pyramidal Cell

**⚠ Draft mappings — confidence labels reflect current evidence only and will be revised.**

---

## Classical type summary

| Field | Value | Source |
|---|---|---|
| Name | entorhinal cortex layer II calbindin-positive pyramidal cell | — |
| Alternate names / synonyms | EC layer II pyramidal cell; EC LII CB+ neuron; L2 IT ENTm cell | — |
| Cell ontology | pyramidal neuron (CL:0000598) — BROAD | — |
| Brain region | entorhinal cortex layer II (UBERON:0001905) | — |
| Soma location | entorhinal cortex layer II | [1], [2], [3] |
| Neurotransmitter | glutamatergic | [4] |
| Defining markers | Calb1 (calbindin; positive) | [4], [5] |
| Electrophysiology | not assessed in current evidence | — |
| Morphology | pyramidal soma; diverse excitatory projections including local intrinsic and commissural axons to layers I–II | [1] |

Entorhinal cortex layer II contains two principal excitatory cell classes: calbindin-positive (CB+) pyramidal neurons and reelin-positive (Reln+) stellate neurons. The CB+ pyramidal cell is distinguished from the stellate cell by Calb1 expression, pyramidal soma morphology, and a projection pattern that preferentially targets CA1 and commissural circuits rather than the dentate gyrus [4], [5].

> "Principal neurons in entorhinal cortex layer II are of two types, stellate-like neurons and pyramidal neurons, the former of which express reelin, whereas the latter include a large population of calbindin-expressing neurons (Ohara et al., 2021)(Varga et al., 2010)(Fuchs et al., 2016)(Ohara et al., 2019)(Zutshi et al., 2018)."
> — Varga et al. 2010, Entorhinal Cortex Glutamatergic Populations · [5] <!-- quote_key: 10189534_9b25e78b -->

These cells are arranged in a periodic, approximately hexagonal mosaic of CB+ patches across medial/caudal entorhinal cortex:

> "We confirm the existence of patches of calbindin-positive pyramidal cells across these species, arranged periodically"
> — Naumann et al. 2015, abstract · [4] <!-- quote_key: 10060696_93c3874e -->

The projection repertoire of CB+ layer II neurons is extensive and predominantly excitatory:

> "the layer II CB+ population comprises neurons with diverse, mainly excitatory projections. At least half of them originate local intrinsic and commissural projections which distribute mainly to layer I and II"
> — Ohara et al. 2019, abstract · [1] <!-- quote_key: 204538361_555db016 -->

The functional role of locally projecting layer II pyramidal cells in grid-cell network dynamics has been directly tested optogenetically:

> "optogenetically perturb locally projecting layer II pyramidal cells. We find that sharply tuned HD cells are only weakly responsive while speed, broadly tuned HD cells, and grid cells show pronounced transient excitatory and inhibitory responses"
> — Zutshi et al. 2018, abstract · [2] <!-- quote_key: 52194250_dabdef57 -->

The glutamatergic identity of this population is well supported: approximately 88% of CB+ cells in rodent entorhinal cortex are glutamatergic [4].

---

## Mapping candidates

### 0052 L2 IT ENT-po Glut_2 (CS20230722_SUPT_0052) — MODERATE

**Atlas metadata**: Supertype CS20230722_SUPT_0052 ("0052 L2 IT ENT-po Glut_2") belongs to the L2 IT ENT-po (entorhinal–postrhinal) glutamatergic subclass (SUBC_011) of the WMBv1 atlas (CCN20230722). Its reported defining markers are Ush2a and Dcn; Calb1 is not listed in the supertype metadata but absence from the metadata list does not exclude expression. Source dataset: GEO:GSE185862.

**Supporting evidence**: Annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 hippocampal cells onto WMBv1 via local MapMyCells assigns the Yao 2021 "L2 IT ENTm" subclass (n = 42 cells, medial EC layer II IT neurons — principally CB+ pyramidal cells) predominantly to SUPT_0052, with group_purity = 0.595, target_purity = 0.833, and F1 = 0.694 (n = 25 cells mapped at SUPERTYPE level). Neurotransmitter type is CONSISTENT between node and atlas (both glutamatergic). Anatomical location is APPROXIMATE: the "ENT-po" designation encompasses both medial EC and postrhinal cortex layer II, whereas the classical type is restricted to medial EC.

**Concerns**:
- The sample is small (n = 42 L2 IT ENTm cells) and statistical confidence is limited accordingly.
- SUPT_0052 and SUPT_0054 (L2 IT ENT-po Glut_4) together account for 92.8% of L2 IT ENTm cells (SUPT_0052: ~59.5%; SUPT_0054: ~33.3%), suggesting the classical EC layer II pyramidal cell population may split across these two supertypes. A second edge to SUPT_0054 would be appropriate when a larger dataset is available.
- Calb1 is the canonical marker distinguishing CB+ pyramidal cells from Reln+ stellate cells, but Calb1 expression has not been cross-checked against precomputed atlas expression data. Without this check it is not possible to confirm that the Calb1/Reln axis resolves cleanly at the SUPT_0052 level.
- The "ENT-po" label conflates medial EC and postrhinal cortex; whether SUPT_0052 is predominantly or exclusively medial EC is not established from atlas metadata alone.

**Upgrade criteria**: Confidence can be upgraded from MODERATE to HIGH if: (1) a larger medial EC layer II dataset (n ≥ 150 L2 IT ENTm cells) replicates the SUPT_0052 primary mapping with F1 ≥ 0.75; (2) Calb1 is confirmed to be differentially expressed in SUPT_0052 relative to stellate-cell supertypes in the WMBv1 precomputed expression data; and (3) the SUPT_0052 vs SUPT_0054 split is resolved — either by demonstrating a biological sub-type boundary or by formally establishing both as a split-mapping at MODERATE confidence.

---

## Proposed experiments

1. **Expand medial EC layer II representation**: Obtain a larger hippocampal/EC single-nucleus or single-cell dataset (target n ≥ 150 L2 IT ENTm cells) and rerun MapMyCells against WMBv1. This directly addresses the primary statistical concern and will clarify whether the SUPT_0052/SUPT_0054 split reflects genuine biology or sampling noise.

2. **Calb1 and Reln expression query in WMBv1**: Query precomputed expression statistics for Calb1 and Reln across all SUBT_011 (L2 IT ENT-po) supertypes and compare with neighbouring subclasses. Confirm that Calb1 is enriched in SUPT_0052 and Reln in the stellate-associated supertypes, to validate the CB+/Reln+ distinction at the atlas level.

3. **Second mapping edge to SUPT_0054**: With the expanded dataset, formally assess a second mapping edge from ec_layer2_pyramidal_cell_hippocampus to CS20230722_SUPT_0054 (L2 IT ENT-po Glut_4). If the ~33% allocation to SUPT_0054 is replicated, add a second PARTIAL_OVERLAP edge at LOW or MODERATE confidence.

---

## Open questions

1. Does Calb1 expression in WMBv1 cleanly distinguish SUPT_0052 from the stellate-cell supertypes (e.g. SUPT_0042)? Precomputed expression data for Calb1 and Reln across SUBT_011 supertypes would resolve the pyramidal/stellate distinction at the atlas level without new experiments.

2. What proportion of SUPT_0052 cells derive from medial EC versus postrhinal cortex? The "ENT-po" label deliberately pools these regions, and the boundary between them is not marked in current atlas metadata. Spatial transcriptomic data would clarify the regional composition of this supertype.

3. Does the SUPT_0052/SUPT_0054 split correspond to a biologically meaningful sub-type boundary within medial EC layer II CB+ pyramidal cells (e.g. dorsal vs. ventral EC, projection target, grid vs. non-grid identity), or does it reflect a continuous distribution captured by two adjacent supertype centroids?

4. The Ohara et al. 2021 study provides a first cell-type-based global map of EC in macaque monkeys [3]. How conserved is the CB+/Reln+ pyramidal/stellate dichotomy across species at the transcriptomic level? Cross-species atlas alignment would test whether WMBv1 "ENT-po" supertypes have clear primate counterparts.

---

## Evidence base

| Corpus ID | Authors | Year | Title | PMID/DOI |
|---|---|---|---|---|
| 204538361 | Ohara et al. | 2019 | Entorhinal Layer II Calbindin-Expressing Neurons Originate Widespread Telencephalic and Intrinsic Projections | PMID:31680885 |
| 52194250 | Zutshi et al. | 2018 | Recurrent circuits within medial entorhinal cortex superficial layers support grid cell firing | PMID:30209250 |
| 244909998 | Ohara et al. | 2021 | Laminar Organization of the Entorhinal Cortex in Macaque Monkeys Based on Cell-Type-Specific Markers and Connectivity | PMID:34949991 |
| 10060696 | Naumann et al. | 2015 | Conserved size and periodicity of pyramidal patches in layer 2 of medial/caudal entorhinal cortex | PMID:26223342 |
| 10189534 | Varga et al. | 2010 | Target-selective GABAergic control of entorhinal cortex output | PMID:20512133 |
| GEO:GSE185862 | Yao et al. | 2021 | Annotation transfer source dataset (SSv4 hippocampal cells, MapMyCells) | GEO:GSE185862 |

---

## References

[1] Ohara et al. 2019 · *Entorhinal Layer II Calbindin-Expressing Neurons Originate Widespread Telencephalic and Intrinsic Projections* · Frontiers in Systems Neuroscience · PMID:31680885

[2] Zutshi et al. 2018 · *Recurrent circuits within medial entorhinal cortex superficial layers support grid cell firing* · Nature Communications · PMID:30209250 · DOI:10.1038/s41467-018-06104-5

[3] Ohara et al. 2021 · *Laminar Organization of the Entorhinal Cortex in Macaque Monkeys Based on Cell-Type-Specific Markers and Connectivity* · Frontiers in Neural Circuits · PMID:34949991 · DOI:10.3389/fncir.2021.790116

[4] Naumann et al. 2015 · *Conserved size and periodicity of pyramidal patches in layer 2 of medial/caudal entorhinal cortex* · Journal of Comparative Neurology · PMID:26223342 · DOI:10.1002/cne.23865

[5] Varga et al. 2010 · *Target-selective GABAergic control of entorhinal cortex output* · Nature Neuroscience · PMID:20512133 · DOI:10.1038/nn.2570
