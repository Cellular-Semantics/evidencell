# Gene identity backfill (#216)

These files record the gene-ID and species backfill for classical markers
in `kb/graphs`, and the `find-candidates` before/after comparison. The code
is in `src/evidencell/gene_identity.py`; see `CLAUDE.md` § "Gene IDs on
classical markers".

## Files

| File | What |
|---|---|
| `marker_resolution.tsv` | All 363 markers that carry `ncbi_gene_id`, with how each was resolved (`EXISTING` = already curated) |
| `unresolvable_markers.tsv` | The 13 markers left without an ID, with the kind and the reason |
| `species_inference.tsv` | The 66 nodes that had no species: the inferred NCBITaxon term, the organisms in their primary papers, and the PMIDs |
| `find_candidates_comparison/` | `find-candidates` top-10 output for ranks 0 and 1 on `origin/main` (86d096e, `before_*`) and on this branch (`after_*`), plus `summary.txt` |

## Marker resolution (376 entries)

| Method | n |
|---|---|
| already curated (`EXISTING`) | 53 |
| `EXACT_SYMBOL` | 252 |
| `UNIQUE_SYNONYM` (`NeuN` → Rbfox3, `Tis21` → Btg2, `mGluR1` → Grm1 …) | 35 |
| `CASE_INSENSITIVE_SYMBOL` (`DCX`, `GFAP`, `VIP` …) | 19 |
| `OVERRIDE` (`CB`, `CR`, `NOS`, `TuJ1`; see `kb/taxonomy/CCN20230722/gene_overrides.tsv`) | 4 |
| unresolvable | 13 |

Mouse genes were resolved offline against the WMB gene table. Rat genes
(3 rat nodes) were resolved through Name Resolver with the same claimant
count. The existing human IDs on the Primates nodes were kept.

Unresolvable markers. None is a single-gene transcript marker, so none can
carry an `ncbi_gene_id`. A `marker_kind` slot to record that is a schema
change and is out of scope here:

- `PSA-NCAM` ×8: a glycoform (a glycan on NCAM1, made by St8sia2/St8sia4).
- `phospho-CREB`: a phosphorylation state.
- `BrdU`: an exogenous label.
- `NMDA-receptor`, `CaMKII`: gene families. For `CaMKII`,
  `pir_immature_neuron`'s paper (PMID:29688272) used "mouse anti-CaMKII
  (Abcam)" with no isoform. Camk2a is the likely referent but is not stated.
- `Crh` on `cea_crf_neuron`: species pending (see below).

## Species inference (66 nodes)

Each node's species is the lowest common NCBITaxon (taxslim) of the
organisms in its cited **primary** papers (Europe PMC MeSH; reviews
excluded). `name_in_source` records the organisms, e.g. "Mice; Rats (MeSH
organisms of cited primary papers; inferred, #216)". Marker IDs are mouse
genes wherever the taxon contains mouse, and rat genes on the rat nodes.
The hook accepts a gene from a descendant taxon.

| Taxon | Nodes |
|---|---|
| Mus musculus | 33 |
| Murinae (mouse + rat) | 18 |
| Euarchontoglires (rodent + primate/human) | 9 |
| Rattus norvegicus | 3 |
| Boreoeutheria (+ cat) | 2 |
| left unset (`cea_crf_neuron`: one review, no organism) | 1 |

Corrections applied while vetting:

- MeSH adds the "Humans" check tag to many animal papers (e.g.
  PMID:16399667, "…adult mouse hippocampus"). "Humans" counts only when it
  is a paper's sole organism.
- Text-derived organisms (no MeSH) count only for nodes with no MeSH
  evidence at all.
- PMID:34616072 (Peng 2021, single-neuron morphology) is a mouse study but
  is MeSH-tagged Humans only. It was treated as mouse.
- **Probable mis-citation:** PMID:34250732 (Aflibercept / HUVEC
  angiogenesis) is in `lth_cell_hippocampus`'s `definition_references`. It
  is off-topic, was excluded here, and should be checked.

## Gene table: symbols

`stats_symbol` (the symbol a stats column goes by in the atlas's marker
lists) comes from the retired mygene-built `conf/gene_mapping_CCN20230722.tsv`
only when Translator still lists that symbol as one of the gene's names. Of
the 167 legacy symbols that differ from the current label, 111 are renames
(`Car8` → Ca8) and are kept. 41 were errors and now take the label: for
example, Ensembl ENSMUSG00000039542 (Ncam1) was labelled `Np65`, so before
this change a KB `Np65` marker read Ncam1 expression, and `M2R` stood for
Chrm2. Both rules match 3,091 of the 3,159 symbols in WMB's own marker
lists. The new rule gains `Chrm2` and `B930025P03Rik` and loses `Rasgef1b`
and `4930511M06Rik`: NodeNorm maps those two Ensembl IDs to other genes
(e.g. ENSMUSG00000089809 → A930011G23Rik).

## find-candidates before/after (PR #207 comparison, repeated)

Same four nodes and ranks as PR #207, top-10. Both sides are built on
86d096e, which includes #228's negative-marker gate.

| node | rank 0 | rank 1 |
|---|---|---|
| `chrna2_olm_subfamily_chamberland` | identical | identical |
| `bla_glutamatergic_principal_neuron` | identical | identical |
| `avpv_kiss1_neuron` | reordered | identical |
| `olm_cell_ca1` | **changed** | **changed** |

- **`avpv_kiss1_neuron` rank 0: a gene-identity fix.** WMB has two Kiss1
  Ensembl models. Before, the symbol join used whichever came last in the
  TSV: ENSMUSG00000116158, which has no NCBIGene record. Now the node's
  curated `NCBIGene:280287` selects ENSMUSG00000115958. Per-cluster values
  differ: 0.18 vs 0.00 in cluster 1888, 0.00 vs 0.14 in cluster 1891.
- **`olm_cell_ca1`: protein-name markers are now scored.** PR #207 held
  back `mGluR1`, `PV`, `CB`, `CR`, `NOS` and `VIP`. They now resolve
  (`UNIQUE_SYNONYM` / `OVERRIDE` / `CASE_INSENSITIVE_SYMBOL`) and score.
  The five negatives are unsourced (hand-drafted, 2026-03). Each costs
  `0768 Sst Gaba_3` (the known OLM match, still #1 at rank 0) a point,
  because those genes are detectable there. Immature-neuron clusters
  (`OB-STR-CTX Inh IMN_*`) gain a point for each one they lack, and still
  pass #228's positive-support gate on `mGluR1` / `Reln`. At rank 1,
  `1165 Astro-TE NN_5` reaches #3. Gene identity is now correct; the
  regression comes from unsourced negative markers plus negative-marker
  scoring rewarding absence. Follow-up: see the PR.
