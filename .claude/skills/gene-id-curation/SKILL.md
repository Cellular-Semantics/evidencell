---
name: gene-id-curation
description: Give a classical marker (defining_markers, negative_markers, neuropeptides) an ncbi_gene_id from the name a paper uses (PV, CB, mGluR1, TuJ1). Use when adding or editing a marker on a classical node, when a marker lacks ncbi_gene_id, or when find-candidates / Stage B reports a marker as NOT MEASURED (AMBIGUOUS_SYMBOL / NO_ENSEMBL_MAPPING).
---

# Skill: Gene ID curation for classical markers (#216)

The one source of truth for literature marker → `ncbi_gene_id`. Workflows and
`CLAUDE.md` point here instead of carrying their own copy.

## When to use

- Adding or editing a marker in `defining_markers`, `negative_markers` or
  `neuropeptides` on a classical node.
- A classical marker with no `ncbi_gene_id`.
- `find-candidates` or Stage B reports a marker as `NOT MEASURED`
  (`AMBIGUOUS_SYMBOL` or `NO_ENSEMBL_MAPPING`), or a pinned marker scores
  unexpectedly.

Out of scope: atlas Ensembl IDs → genes. That side is mechanical (committed
`kb/taxonomy/{taxonomy_id}/gene_ids.tsv.gz`, the `genes` / `gene_synonyms`
tables, the resolver) and needs no curation.

## Step 1 — Pick the target: the node's species, not the atlas's

The ID must be a gene of the **node's** species (`species` on the node, or the
graph's). A gene of a descendant species is fine on a higher-taxon node (a
mouse gene on a Murinae node). Then:

| Node species | Command |
|---|---|
| Same as a registered taxonomy's (e.g. mouse → `CCN20230722`) | `just resolve-gene-names CCN20230722 NAME…` (offline) |
| Anything else (rat, human, macaque, …) | `just resolve-gene-names NCBITaxon:10116 NAME…` (network, Name Resolver) |

Passing a mouse taxonomy for a rat node gives a mouse gene, which the pre-edit
hook rejects as the wrong species. This is the most common mistake. If the
node has no species yet, settle that first from the paper.

Pass the name exactly as the paper writes it. Several names can go in one call.

## Step 2 — Act on `method`

The output is JSON: one entry per name with `method`, `gene`
(`ncbi_gene_id`, `symbol`, `label`) and `claimants`.

| `method` | Action |
|---|---|
| `EXACT_SYMBOL`, `UNIQUE_SYNONYM`, `OVERRIDE` | Accept `gene.ncbi_gene_id`. |
| `CASE_INSENSITIVE_SYMBOL` | Accept, unless a caution below applies or `claimants` is non-empty (other genes list the name as a synonym — check the paper means the symbol's gene). |
| `AMBIGUOUS` | Pick **one gene from `claimants`**, never another gene. Quote the paper's definition if it gives one (e.g. "calbindin-D28k (CB)"); otherwise state a rationale. Either goes in the `notes` of the marker's `sources` entry (`MarkerSource`; `GeneDescriptor` has no `notes` of its own). If the paper does not settle it, leave `ncbi_gene_id` empty and say why in the node's `notes`. |
| `NO_MATCH` | Not a gene name. Classify it (below), leave `ncbi_gene_id` empty, and add a row to `research/gene_identity_216/unresolvable_markers.tsv`. |

Settle `AMBIGUOUS` with the paper that asserts the marker. In
`asta-report-ingest`, where only the synthesis report is at hand, leave it empty
and let `evidence-extraction` settle it from the primary paper.

`NO_MATCH` kinds (the `kind` column of `unresolvable_markers.tsv`; columns are
`file  node_id  field  symbol  kind  reason`):

- `ANTIBODY_CLONE` — a clone name for a known protein (`TuJ1` → Tubb3). If the
  target protein is unambiguous, prefer an override (Step 3) over leaving it
  unresolved.
- `PTM_STATE` — a modification state (phospho-, acetyl-…).
- `GLYCOFORM` — a glycan on a protein (`PSA-NCAM`); the core gene's mRNA is not
  a proxy.
- `EXOGENOUS_LABEL` — a reporter, tracer or transgene (GFP, BrdU).
- `GENE_FAMILY` — several genes by design (`GABA-A receptor`); list members as
  separate markers only if the paper does.
- `NEEDS_OVERRIDE` — the paper settles the gene (`CB, calbindin-D28k`; `TuJ1`
  → Tubb3) but the name is not one of that gene's names in the node's species,
  and no override table covers the species (overrides live per taxonomy, so a
  rat or other non-atlas node has none). The hook would reject the pin. Put the
  gene's ID and the paper's wording in `reason`.
- `PENDING_SPECIES` — a real gene name, but the node's species is unknown, so
  there is no species to resolve in (Step 1). Not a `NO_MATCH` case; recorded
  here until the species is settled.

## Cautions

- **Region-like tokens.** A case-insensitive hit on something that reads as a
  region or other non-gene token is a red flag: `CA1` → Car1 (carbonic
  anhydrase 1), `CA3` → Car3. Check the paper uses it as a gene before
  accepting.
- **Pinned IDs not in the atlas fall through silently.** When a marker's
  `ncbi_gene_id` is not among the taxonomy's genes, `gene_identity.resolve_name`
  resolves the *name* instead (this is how a rat marker reaches mouse genes).
  It does not warn. When a pinned marker scores unexpectedly, check
  `gene_resolution` in the discovery JSON: `PINNED_ID` means the pin was used;
  anything else means the name decided.

## Step 3 — Propose an override when the decision applies everywhere

If a name → gene decision should hold for every node (a panel abbreviation like
`CB`, `CR`, `NOS`, or a clone like `TuJ1`), add a row to
`kb/taxonomy/{taxonomy_id}/gene_overrides.tsv`:

```
name	ncbi_gene_id	symbol	rationale	reviewed_by
CB	NCBIGene:12307	Calb1	Calbindin in neuron marker panels (PV/CB/CR); claimants Calb1, Ctsb	agent-proposed (<context>); pending PR review
```

- `rationale` names the claimants and why this one wins.
- `reviewed_by` is honest: `agent-proposed …` until a person signs it off.
- Rebuild the DB (`just build-taxonomy-db {taxonomy_id}`) to load it; the
  resolver then returns `OVERRIDE`.
- Overrides apply only to that taxonomy's species. For a node in any other
  species there is no override route yet: record `NEEDS_OVERRIDE` (Step 2).

## What the pre-edit hook rejects

On every write to `kb/**/*.yaml`, each `ncbi_gene_id` is checked
(`gene_identity.check_marker_gene_ids`). The write is blocked if the ID:

- does not resolve to an NCBI gene;
- belongs to another species than the node's (descendants allowed);
- does not match the marker's symbol (the symbol must be the gene's label, one
  of its names, or a reviewed override).

Soft skips (write allowed, reported as unchecked): the ID is not cached and
Translator NodeNormalization is unreachable, or the gene's taxon differs from
the node's and `conf/oak_dbs/taxslim.obo` is missing (`just fetch-oak-dbs`).
`EVIDENCELL_SKIP_GENE_CHECK=1` bypasses the check entirely — emergency only.

Fix these before writing: the resolver output from Steps 1–2 already tells you
the gene, species and symbol the hook will compare.
