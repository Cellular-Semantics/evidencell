# subtype_of mockups (#183): scratch, not for merging

Branch `scratch/subtype-mockups-183`, built on #238 as the PR now stands.
The schema, validator and workflow come from #238 unchanged. This branch only
rewrites real KB files to use `subtype_of`. Every edited file passes this
worktree's pre-edit hook: schema, quote keys, refs, ontology terms, and the
new parent check.

The design decided in #238 discussion:

- `subtype_of` on the child node is an **interim** home for lit-to-lit subtype
  relations. Each field maps 1:1 onto a future lit-to-lit MappingEdge (#239).
- `kind`:
  - DEFINITIONAL: the child's definition names the parent plus one criterion.
  - EMPIRICAL: the child is defined independently, and the sources report
    containment.
- `confidence`: HIGH / MODERATE / LOW, judged on the sources (two or more
  explicit / one explicit / inferred). This is not the mapping rubric.
- `sources` are `SubtypeSource`: a PropertySource plus an optional
  `evidence_type`. When it is absent, the source is literature cited by
  quote_key.
- Overlap that is not containment stays a MappingEdge.
- Existing lit-to-lit edges (OLM subfamilies, cerebellum) are **left as they
  are**.

```yaml
- id: igl_npy_geniculohypothalamic_neuron
  definition_basis: CLASSICAL_NEUROCHEMICAL
  subtype_of:
    - parent: igl_gabaergic_neuron
      kind: DEFINITIONAL
      confidence: HIGH
      sources:
        - ref: "PMID:23103793"
          quote_key: "25997395_d6b35c15"
        - ref: "PMID:27916729"
          quote_key: "27232578_7306b2da"
      notes: >
        One of two main GABAergic subpopulations of the IGL, picked out by
        NPY and projection target. Rat.
```

## Cases on this branch

| Child → parent | Before | kind | conf. | What it shows |
|---|---|---|---|---|
| IGL NPY / ENK neurons → `igl_gabaergic_neuron` | broadMatch edge + `LIT_TYPE` stub | DEFINITIONAL | HIGH | Clean case. Edges, stubs and "PARENT TYPE" notes paragraphs go away |
| `igl_gabaergic_neuron` → `lgv_igl_gabaergic_neuron` | broadMatch edge + stub | DEFINITIONAL | LOW | The source hedges the structural subdivision ("historically considered a subdivision of the VLG") |
| AD / AV / AM excitatory → `anterior_thalamic_nucleus_excitatory_neuron` | "HIERARCHY: subtype of…" in notes | DEFINITIONAL | HIGH | Defined by nucleus |
| aPVT Gck+ / CRF+ → `pvt_glutamatergic_neuron` | "SUBSET OF…" in notes | DEFINITIONAL | LOW | The marker subset of the PVT is explicit; membership of the *glutamatergic* parent is inferred |
| TRN Ecel1 shell / Spp1 core → `trn_gabaergic_neuron` | "PARENT / GRADIENT POLE: subtype of…" in notes | DEFINITIONAL | HIGH | Gradient poles: containment holds, but the poles do not cover the parent |

That is 10 files in `kb/graphs/thalamus/`.

## Left as edges

| Relation | Edge | Why it stays |
|---|---|---|
| Chrna2-OLM, Ndnf::Nkx2-1-OLM (Chamberland) → `olm_cell_ca1` | broadMatch, in `olm_cell_ca1.yaml` | Curator-authored EMPIRICAL claims. Ndnf's is contested by AT, and an edge holds that disagreement better. They migrate with #239, if at all |
| `classical_basket` / `classical_stellate` vs `mli1_kozareva` / `mli2_kozareva` | CrossCuttingMatch / UncertainRelationship | Overlap, not containment. These are never `subtype_of` |

## What an EMPIRICAL relation looks like at ingest

The Gao 2023 PVT clusters come from the #223 PVT re-ingest test; these nodes
are not on main. The clusters come from clustering PVT nuclei selected as
Slc17a6/7+ and Gad1/2−. They are contained in the glutamatergic PVT neuron by
that *selection*, not by definition. The paper's own cluster hierarchy is a
second, non-quote source:

```yaml
  - id: pvt1_gao
    definition_basis: PRIOR_TRANSCRIPTOMIC
    subtype_of:
      - parent: pvt_glutamatergic_neuron
        kind: EMPIRICAL
        confidence: MODERATE           # one study states it
        sources:
          - ref: "PMID:36867023"
            quote_key: "251021326_815dcc71"   # Slc17a6/7+, Gad1/2− selection
          - ref: "PMID:36867023"
            evidence_type: ATLAS_METADATA     # the study's cluster hierarchy
            notes: "PVT1 is one of five clusters of the glutamatergic PVT dataset"
        notes: >
          Clustering-defined (single study, mouse). Shima 2022 argues PVT
          subtypes lie on a continuum.
```

The two sources come from the same study, so confidence stays MODERATE.
`evidence_type` records the kind of support; it does not make the sources
independent.

## What the mockup shows

1. **The DEFINITIONAL cases all fit cleanly.**
   - Ten children lose prose in notes, or an edge plus a stub, with no
     information lost.
   - Hierarchy sentences move into `subtype_of.notes`; other caveats stay in
     the node's notes.
   - `igl_gabaergic_neuron`'s "SUBTYPES" paragraph goes, because children are
     computed.
2. **Confidence and kind are independent.** DEFINITIONAL can be LOW (IGL→LGv
   is hedged; aPVT rests on an inferred NT).
3. **The choice of parent matters.** aPVT→`pvt_glutamatergic_neuron` is LOW
   only because the parent is NT-qualified; a "PVT neuron" parent would be
   HIGH. Ingest picks the narrowest parent the sources support.
4. **The parent check catches typos on real files.** For example,
   `pvt_glutamatergic_neuronX` is blocked by the hook.
5. **Still to do:**
   - render `subtype_of` in `render_review` / `node_diff` (not shown there
     yet);
   - compute children from the KB index.
