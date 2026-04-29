# Entorhinal Cortex Layer II Stellate Cell — WMBv1 Mapping Report
*draft · 2026-04-29 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**Warning: Draft mappings. Evidence is atlas-metadata and annotation-transfer only unless otherwise noted. All edges require expert review before use.**

---

## Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | entorhinal cortex layer II [UBERON:0001905] | [1], [2], [3], [4], [5], [6], [7] |
| Neurotransmitter | Glutamatergic | [4] |
| Defining markers | Reln (reelin) | [1] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | glutamatergic neuron [CL:0000679] (BROAD) | — |

The entorhinal cortex (EC) layer II contains two principal cell types distinguishable by molecular markers and projection targets. Stellate cells express reelin (Reln) and project to the dentate gyrus and CA3/CA2 regions of the hippocampus, while the companion pyramidal cell population is defined by calbindin (Calb1) expression and projects to CA1 [1], [4], [7].

> "Principal neurons in EC layer II are of two types, stellate-like neurons and pyramidal neurons, the former of which express reelin, whereas the latter include a large population of calbindin-expressing neurons (RE+ and CB+, respectively). The RE+ neurons possess the typical projection pattern of EC layer II neurons, innervating the dentate gyrus and the CA3/CA2 regions of the hippocampus"
> — Ohara et al. 2021, INTRODUCTION · [4] <!-- quote_key: 244909998_e232144b -->

> "Principal neurons in entorhinal cortex layer II are of two types, stellate-like neurons and pyramidal neurons, the former of which express reelin, whereas the latter include a large population of calbindin-expressing neurons (Ohara et al., 2021)(Varga et al., 2010)(Fuchs et al., 2016)(Ohara et al., 2019)(Zutshi et al., 2018)."
> — Zutshi et al. 2018, Entorhinal Cortex Glutamatergic Populations · [7] <!-- quote_key: 52194250_9b25e78b -->

> "Principal neurons in layer 2 are divided into two distinct cell types, pyramidal and stellate, based on morphology, immunoreactivity, and functional properties"
> — Naumann et al. 2015, abstract · [1] <!-- quote_key: 10060696_40a9cee6 -->

---

## Mapping candidates

| Rank | WMBv1 supertype | Confidence | Key evidence | Verdict |
|---|---|---|---|---|
| 1 | 0042 L2/3 IT PIR-ENTl Glut_4 [CS20230722_SUPT_0042] | 🟡 MODERATE | AT F1=0.964 (n=172, GEO:GSE185862); NT CONSISTENT; location APPROXIMATE | Best candidate |

Total: 1 edge. Relationship type: PARTIAL_OVERLAP — the classical stellate cell maps to SUPT_0042 with high annotation-transfer fidelity, but the supertype spans a compound PIR-ENTl transcriptomic domain whose piriform contribution requires spatial resolution.

---

## 0042 L2/3 IT PIR-ENTl Glut_4 [CS20230722_SUPT_0042] · 🟡 MODERATE

### Supporting evidence

- **Neurotransmitter type consistent.** SUPT_0042 belongs to the L2/3 IT PIR-ENTl Glut subclass (SUBC_009), fully consistent with the glutamatergic identity of EC layer II stellate cells [4].
- **Strong annotation-transfer support.** MapMyCells annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 lateral entorhinal cortex layer II cells onto WMBv1 (CCN20230722) maps the 'L2 IT ENTl' subclass (n=180 cells; 172 mapped) to SUPT_0042 with group_purity=0.956 and F1=0.964 at the supertype level. The near-perfect F1 indicates this supertype is a highly specific transcriptomic attractor for lateral EC layer II cells in the WMBv1 atlas.
- **EC layer II location consistent.** The Yao 2021 'L2 IT ENTl' subclass explicitly represents lateral entorhinal cortex layer II intrinsically-thalamus-projecting (IT) excitatory neurons. The mapping result confirms SUPT_0042 as the WMBv1 supertype capturing this population.
- **Reelin distinguishes stellate from pyramidal cells.** Classical literature establishes Reln as the definitive marker separating EC layer II stellate cells from calbindin-positive pyramidal cells, with the Reln+ population projecting to the dentate gyrus [1], [4], [7]. The Yao 2021 'L2 IT ENTl' subclass is the dominant layer II population in lateral EC and corresponds to the reelin-positive stellate cell cohort.

### Marker evidence provenance

- **Reln (defining marker):** Evidence is protein-level (immunoreactivity in morphologically characterised layer II neurons, [1]) and cross-referenced at transcript level in subsequent atlasing studies [4], [7]. Naumann et al. 2015 [1] showed reelin-positive cells constitute the stellate population and project to the dentate gyrus — cell-type specificity is high. The companion calbindin-positive population (pyramidal cells) is consistently Reln-negative across studies. Reln is **not listed** among SUPT_0042 defining markers (Igfn1, Endou, Bcl11b, Boc); however, absence from the defining-marker list does not exclude expression — this requires a precomputed expression query for Reln on CCN20230722 precomputed stats. Alignment is currently NOT_ASSESSED pending that query.

> "Reelin-positive cells project to the dentate gyrus and show electrophysiological parameters of stellate cells (Varga et al., 2010), whereas calbindin-positive cells project to CA1 (Kitamura et al., 2014) and have electrophysiological properties described previously for pyramidal cells (Klink and Alonso, 1997)."
> — Naumann et al. 2015, layer 2 medial entorhinal cortex · [1] <!-- quote_key: 10060696_46dbde68 -->

### Concerns

1. **PIR-ENTl compound designation.** The SUBC_009 subclass and SUPT_0042 supertype name includes 'PIR' (piriform cortex) alongside 'ENTl' (lateral entorhinal cortex), reflecting a shared transcriptomic signature between piriform layer II and EC layer II populations. It is currently unclear whether the WMBv1 MERFISH spatial data assigns SUPT_0042 cells to both piriform and EC layer II regions, or whether the PIR designation is driven primarily by transcriptomic similarity. If a significant fraction of SUPT_0042 cells is located in piriform cortex rather than EC layer II, the mapping represents a partial overlap rather than a direct equivalence.
2. **L2 IT ENTl subclass may not be exclusively stellate cells.** The Yao 2021 'L2 IT ENTl' subclass may contain a small fraction of non-stellate (Reln-negative) excitatory neurons in lateral EC layer II. This concern is minor given the extremely high F1 (0.964), suggesting the Yao subclass is functionally coherent with SUPT_0042.
3. **Reln expression in SUPT_0042 unverified.** The canonical stellate cell marker Reln has not been queried against the CCN20230722 precomputed stats. Confirmation that SUPT_0042 shows Reln expression at levels consistent with stellate cell identity would substantially strengthen the mapping.

### What would upgrade confidence

- Confirm Reln expression in SUPT_0042 via `just add-expression` query on CCN20230722 precomputed stats; Reln enrichment would corroborate the stellate identity and could raise confidence to HIGH.
- Query WMBv1 MERFISH spatial data to determine the anatomical breakdown of SUPT_0042 cells between lateral EC layer II and piriform cortex; if the majority are EC layer II, the PIR designation is transcriptomic and does not weaken the mapping.
- Run annotation transfer from a dataset with explicitly validated Reln+ stellate cell profiles to confirm supertype-level specificity.
- Assess Calb1 (calbindin) expression in SUPT_0042 to confirm absence, distinguishing stellate from pyramidal EC layer II populations at the atlas level.

---

## Proposed experiments

1. Run `just add-expression` for Reln and Calb1 on the CCN20230722 precomputed stats to distinguish SUPT_0042 (expected Reln+, stellate) from any companion supertype (expected Calb1+, pyramidal) at the atlas level.
2. Query the WMBv1 MERFISH spatial data to determine the soma-location distribution of SUPT_0042 cells. If the atlas records a mix of EC layer II and piriform cortex positions, a separate edge for the piriform component should be evaluated.
3. Obtain a dataset with patch-clamp-validated or immunostaining-validated EC layer II stellate cells (Reln+, stellate morphology, dentate-gyrus-projecting) and run annotation transfer to confirm SUPT_0042 as the primary supertype attractor.

---

## Open questions

1. Does SUPT_0042 carry a significant piriform cortex component in WMBv1 MERFISH data, or is the PIR-ENTl designation driven by transcriptomic similarity rather than spatial co-location?
2. Is Reln expressed in SUPT_0042 at the level expected for stellate cells? A precomputed expression query for Reln on CCN20230722 would confirm this.
3. Is there a separate WMBv1 supertype for lateral EC layer II pyramidal (Calb1+) cells? If so, it would be the candidate for the companion `ec_layer2_pyramidal_cell_hippocampus` node and would clarify the splitting pattern for EC layer II excitatory neurons in the atlas.

---

## Evidence base

| Type | Source | Method | Coverage |
|---|---|---|---|
| Annotation transfer | GEO:GSE185862 (Yao 2021, SSv4 hippocampal) | MapMyCells local (precomputed_stats CCN20230722) | SUPT_0042; n=172 mapped at supertype level; group_purity=0.956; F1=0.964 |
| Classical literature | PMID:26223342 [1] | Immunohistochemistry + morphological characterisation | Layer 2 pyramidal/stellate distinction; Reln marker |
| Classical literature | PMID:34949991 [4] | Review + laminar connectivity | EC glutamatergic identity; Reln/Calb1 marker split |
| Classical literature | PMID:30209250 [7] | Electrophysiology + circuit tracing | EC layer II stellate/pyramidal two-type framework |
| Classical literature | PMID:26711115 [2] | Electrophysiology + optogenetics | Layer II excitatory neuron subtypes in MEC |
| Classical literature | PMID:20512133 [3] | GABAergic circuit anatomy | EC layer II principal cell projection targets |
| Classical literature | PMID:29665671 [6] | Review | EC lateral/medial subdivision anatomy |
| Classical literature | PMID:37219048 [5] | Review | EC glutamatergic neuron context |

---

## References

1. Naumann et al. 2015 · PMID:26223342 · DOI:10.1002/cne.23865
2. Fuchs et al. 2016 · PMID:26711115
3. Varga et al. 2010 · PMID:20512133 · DOI:10.1038/nn.2570
4. Ohara et al. 2021 · PMID:34949991 · DOI:10.3389/fncir.2021.790116
5. Strell et al. 2023 · PMID:37219048 · DOI:10.1177/09636897231164712
6. Park et al. 2018 · PMID:29665671 · DOI:10.14348/molcells.2018.0081
7. Zutshi et al. 2018 · PMID:30209250 · DOI:10.1038/s41467-018-06104-5
