# Arcuate aromatase neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Arcuate hypothalamic nucleus [MBA:223] *(adjacent to kisspeptin neurons, per source)* | [1] |
| Defining markers | *Cyp19a1* | [1] |

**Notes.** Male-biased sexually dimorphic population. Defined by a single primary source (Wartenberg 2021 [1]). Part of a broader aromatase network spanning hypothalamus and amygdala (~6,000 neurons at birth). No CL term — candidate for a new CL entry. NT type and negative markers not reported.

> "We identified an aromatase neuronal network comprising ~6000 neurons in the hypothalamus and amygdala. By birth, this network has become sexually dimorphic in a cluster of aromatase neurons in the arcuate nucleus adjacent to kisspeptin neurons. We demonstrate that male arcuate aromatase neurons convert testosterone to estrogen to regulate kisspeptin neuron activity."
> — P et al. 2021, Neuronal Markers and Molecular Characteristics · [1] <!-- quote_key: 237626479_5aec04ab -->

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| SUPERTYPE | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 [CS20230722_SUPT_0486] | — | — | ⚪ UNCERTAIN | *Cyp19a1* approximate; location critically discordant | Eliminated |

---

## Eliminated candidates

### CS20230722_SUPT_0486 — 0486 PVpo-VMPO-MPN Hmx2 Gaba_5

**Supporting evidence.**
A full WMBv1 database scan found no supertype in MBA:223 (Arcuate hypothalamic nucleus) with *Cyp19a1* as a defining marker. SUPT_0486 is the best available atlas match for *Cyp19a1* expression (mean expression = 1.15 at the supertype level; child cluster CLUS_1907 carries *Cyp19a1* as a defining marker). It is the only supertype in the DB with substantive *Cyp19a1* signal.

**Marker evidence.**
*Cyp19a1* expression at the supertype level is approximate rather than defining. CLUS_1907, a child of SUPT_0486, does carry *Cyp19a1* as a primary defining marker — the strongest atlas-side *Cyp19a1* signal available. All *Cyp19a1*-expressing clusters found in the full DB scan fall in POA and periventricular zones, not in MBA:223. Evidence basis is atlas metadata only; no literature-derived marker evidence has been extracted to date.

**Concerns.**

1. *Critical anatomical discordance.* The classical type is defined in MBA:223 (Arcuate hypothalamic nucleus); SUPT_0486 spans MBA:133 (PVpo, n = 64), MBA:515 (MPN, n = 37), and MBA:272 (AVPV, n = 16) — with no cells assigned to MBA:223 in the MERFISH data. This is the principal barrier to a confident match.

2. *Single-source anatomical assignment.* The MBA:223 location for the classical type rests entirely on Wartenberg 2021 [1]. No independent replication of ARH-specific aromatase neuron identity has been integrated.

3. *Candidate ARH supertypes unassessed.* SUPT_0427 and SUPT_0428 (ARH-PVi Six6 Dopa-Gaba supertypes) have not had *Cyp19a1* expression confirmed from precomputed HDF5 stats and may be more anatomically appropriate matches.

**What would upgrade confidence.**
- Confirmation that CLUS_1907 (child of SUPT_0486) is absent from MBA:223 MERFISH voxels would definitively rule out SUPT_0486.
- *Cyp19a1* expression data for SUPT_0427 and SUPT_0428 from the precomputed HDF5 would either identify a better-localised ARH candidate or confirm that no ARH supertype expresses *Cyp19a1* — making a pan-hypothalamic aromatase identity the working hypothesis.
- Independent literature evidence (additional PMID-backed sources) establishing *Cyp19a1* expression and ARH soma location would strengthen the classical-node definition.

---

## Proposed experiments

### Atlas data query

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Query *Cyp19a1* mean expression from precomputed HDF5 stats for ARH-region supertypes | SUPT_0427, SUPT_0428, and neighbouring ARH supertypes | Expression values enabling like-for-like comparison with SUPT_0486 | Whether an ARH-localised supertype carries *Cyp19a1* signal; whether SUPT_0486 elimination is warranted |
| Retrieve MERFISH voxel assignments for CLUS_1907 | CS20230722_CLUS_1907 | Cell counts per MBA region | Determines whether any SUPT_0486 child cells land in MBA:223, and whether the anatomical discordance extends to the cluster level |

---

## Open questions

1. Do SUPT_0427 or SUPT_0428 (ARH Dopa-Gaba supertypes) show *Cyp19a1* expression in the precomputed HDF5 stats?
2. Is CLUS_1907 located exclusively in POA/periventricular zones in MERFISH data, or do any cells fall in MBA:223?
3. Does the anatomical discordance between the classical ARH assignment and the atlas POA/periventricular distribution reflect a MERFISH registration artefact at the ARH/periventricular boundary, or does it indicate that *Cyp19a1*-expressing neurons form a transcriptomically coherent pan-hypothalamic network not segregated by anatomical zone in WMBv1?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_arc_aromatase_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA | WEAK |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | P et al. 2021 | PMID:34561233 | Soma location, *Cyp19a1* defining marker |
