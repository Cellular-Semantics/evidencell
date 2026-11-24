---
name: gene-id-curation
description: Record a classical marker (defining_markers, negative_markers, neuropeptides) from the name a paper uses (PV, CB, mGluR1, NeuN, PSA-NCAM) — name_in_source, plus symbol + ncbi_gene_id for the gene it means, and the antibody when the paper names one. Use when adding or editing a marker on a classical node, when a marker lacks ncbi_gene_id, or when find-candidates / Stage B reports a marker as NOT MEASURED (NO_GENE_ID / AMBIGUOUS_SYMBOL / NO_ENSEMBL_MAPPING).
---

# Skill: Gene ID curation for classical markers (#216, #244)

The one source of truth for literature marker → gene. Workflows and
`CLAUDE.md` point here instead of carrying their own copy.

## When to use

- Adding or editing a marker in `defining_markers`, `negative_markers` or
  `neuropeptides` on a classical node.
- A classical marker with no `ncbi_gene_id`.
- `find-candidates` or Stage B reports a marker as `NOT MEASURED`
  (`NO_GENE_ID`, `AMBIGUOUS_SYMBOL` or `NO_ENSEMBL_MAPPING`), or a pinned
  marker scores unexpectedly.

Out of scope: atlas markers. Their names are copied from the atlas metadata
into `name_in_source` and resolved to genes in the taxonomy DB, mechanically.

## The shape

```yaml
- name_in_source: CB          # exactly as the paper writes it — never checked
  symbol: Calb1               # official symbol of the gene, in the node's species
  ncbi_gene_id: NCBIGene:12307
  sources:
    - marker_type: PROTEIN
      antibody: {name_in_source: "anti-calbindin D-28k"}   # when the paper names it
      ...
```

`symbol` and `ncbi_gene_id` are set together or not at all. A marker with
no single gene keeps `name_in_source` only. A classical marker without an
ID is never resolved by name: it is reported `NO_GENE_ID` and scores 0.

## Step 1 — Decide what the marker is

| The paper's marker is… | Record |
|---|---|
| One gene or its protein, by symbol, protein name or abbreviation (`PV`, `CB`, `mGluR1`, `Sst`) | `name_in_source` + `symbol` + `ncbi_gene_id` (Steps 2–3) |
| An antibody or clone for one protein (`NeuN` → Rbfox3, `TuJ1` → Tubb3) | Same — the gene — plus the antibody on the source (Step 4) |
| An antibody against a modified form: glycoform or PTM (`PSA-NCAM`, `phospho-CREB`) | `name_in_source` only, antibody on the source. mRNA of the carrier gene is not a proxy |
| A whole family (`CaMKII`, `NMDA-receptor`, `GABA-A receptor`) | `name_in_source` only, antibody on the source if any. List members as separate markers only if the paper does |
| Not a marker of the cell (BrdU, EdU, tracers, injected dyes) | No marker entry. Record what it shows (birth-dating, connectivity) in the node's `notes` or the relevant property |

Other detail (epitope, why no gene) goes in the `notes` of the marker's
source entry (`MarkerSource`; `GeneDescriptor` has no `notes`).

## Step 2 — Resolve in the node's species, not the atlas's

The ID must be a gene of the **node's** species (`species` on the node, or the
graph's). A gene of a descendant species is fine on a higher-taxon node (a
mouse gene on a Murinae node).

| Node species | Command |
|---|---|
| Same as a registered taxonomy's (e.g. mouse → `CCN20230722`) | `just resolve-gene-names CCN20230722 NAME…` (offline) |
| Anything else (rat, human, macaque, …) | `just resolve-gene-names NCBITaxon:10116 NAME…` (network, Name Resolver) |

Passing a mouse taxonomy for a rat node gives a mouse gene, which the hook
rejects as the wrong species. If the node has no species yet, settle that
first from the paper (until then, `name_in_source` only).

Pass the paper's wording; several names can go in one call. If the paper
defines the name ("CB, calbindin-D28k"), you may resolve the gene it names
(`Calb1`) instead — `name_in_source` still keeps `CB`.

## Step 3 — Act on `method`

The output is JSON: one entry per name with `method`, `gene`
(`ncbi_gene_id`, `label`; locally also `symbol`, the atlas's spelling) and
`claimants`. **`symbol` in the KB is `gene.label`** — the official symbol the
hook compares against — not the atlas spelling.

| `method` | Action |
|---|---|
| `EXACT_SYMBOL`, `UNIQUE_SYNONYM`, `OVERRIDE` | Accept: `ncbi_gene_id` = `gene.ncbi_gene_id`, `symbol` = `gene.label`. |
| `CASE_INSENSITIVE_SYMBOL` | Accept, unless a caution below applies or `claimants` is non-empty (other genes list the name as a synonym — check the paper means the symbol's gene). |
| `AMBIGUOUS` | Pick **one gene from `claimants`**, never another. Quote the paper's definition if it gives one; otherwise state a rationale, in the source's `notes`. If the paper does not settle it, leave `symbol`/`ncbi_gene_id` empty and say why in the node's `notes`. |
| `NO_MATCH` | Not a name of any gene. If the paper says which gene it means, resolve that gene (Step 2). Otherwise it is one of the no-gene rows in Step 1. |

In `asta-report-ingest`, where only the synthesis report is at hand, leave
`AMBIGUOUS` unpinned and let `evidence-extraction` settle it from the primary
paper.

Every classical marker left without a gene gets a row in
`research/gene_identity_216/unresolvable_markers.tsv`
(`file  node_id  field  name_in_source  kind  reason`), `kind` one of
`GLYCOFORM`, `PTM_STATE`, `GENE_FAMILY`, `PENDING_SPECIES` (node species
unknown) or `UNSETTLED_AMBIGUITY` (the paper doesn't pick a claimant).

## Step 4 — The antibody

For PROTEIN evidence, record the antibody on the source when the paper names
it:

```yaml
antibody:
  name_in_source: "anti-NeuN clone A60"   # as the paper names it
  rrid: RRID:AB_2298772                   # only if the paper states it
```

Never look up or guess an RRID from a product name: give one only when the
paper (or its key resources table) states it. The hook rejects an RRID the
Antibody Registry doesn't know.

## Cautions

- **Region-like tokens.** A case-insensitive hit on something that reads as a
  region or other non-gene token is a red flag: `CA1` → Car1 (carbonic
  anhydrase 1), `CA3` → Car3. Check the paper uses it as a gene.
- **Pins from another species.** A marker whose `ncbi_gene_id` is not a gene
  of the atlas (a rat gene against WMB) resolves by its official `symbol`
  (rat Calb1 → mouse Calb1). Check `gene_resolution` in the discovery JSON
  when a pinned marker scores unexpectedly: `PINNED_ID` means the ID itself
  matched.

## Overrides

`kb/taxonomy/{taxonomy_id}/gene_overrides.tsv` settles a name → gene for the
**resolver** in that taxonomy (atlas metadata names, `resolve-gene-names`
suggestions). A KB marker doesn't need one: its `symbol` + `ncbi_gene_id`
record the decision. Add a row only when the same name keeps coming up:

```
name	ncbi_gene_id	symbol	rationale	reviewed_by
CB	NCBIGene:12307	Calb1	Calbindin in neuron marker panels (PV/CB/CR); claimants Calb1, Ctsb	agent-proposed (<context>); pending PR review
```

`reviewed_by` is honest: `agent-proposed …` until a person signs it off.
Rebuild the DB (`just build-taxonomy-db {taxonomy_id}`) to load it.

## What the pre-edit hook rejects

On every write to `kb/**/*.yaml` (`gene_identity.check_marker_gene_ids`,
`rrid.check_antibody_rrids`), a marker is blocked if:

- it has `symbol` without `ncbi_gene_id`, or the reverse;
- the ID does not resolve to an NCBI gene;
- the ID belongs to another species than the node's (descendants allowed);
- `symbol` is not exactly the gene's official symbol (a synonym such as `PV`
  belongs in `name_in_source`);
- an antibody `rrid` is not in the Antibody Registry.

Soft skips (write allowed, listed under "Checks NOT run"): an ID or RRID
that isn't cached while its service is unreachable, or a taxon comparison
without `conf/oak_dbs/taxslim.obo` (`just fetch-oak-dbs`).
`EVIDENCELL_SKIP_GENE_CHECK=1` / `EVIDENCELL_SKIP_RRID_CHECK=1` bypass the
checks entirely — emergency only.
