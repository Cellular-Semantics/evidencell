---
name: gene-id-curation
description: Given a gene or protein name as a source writes it (PV, CB, mGluR1, NeuN, PSA-NCAM) and a taxon, find the NCBI Gene ID and official symbol of the gene it means — or say why it names no single gene — and return a structured result with the supporting evidence. Not for mapping one gene or protein identifier to another (e.g. Ensembl → NCBI Gene).
---

# Skill: gene or protein name → NCBI Gene

## Purpose

The lookup tool (below) matches strings, and for a clear symbol or a
distinctive name (`Sst`, `PV`, `VGLUT1`) its answer is all that is needed.
This skill exists for the names it cannot settle: abbreviations that several
genes claim (`SOM` → Sst or Grhl3, `CRF` → Crh or C1ql1), and abbreviations
it maps confidently to the wrong gene (`D1` → Dio1, `GAD` → Uchl1) or to a
gene when the source means a region (`CA1`, `SP`). Its main job is to
disambiguate these, using the evidence quote first and knowledge of the
field's naming conventions where the quote leaves it open.

## Input

| Field | Required | Notes |
|---|---|---|
| `name` | yes | Exactly as the source writes it. One or several names. |
| `taxon` | yes | NCBITaxon CURIE of the organism the name refers to. Set by the caller; this skill does not infer it. A taxon above species (Rodentia, Murinae) is allowed: a gene of any descendant species is then a valid answer. |
| `evidence` | no | The sentence(s) in which the source uses the name, and the source's ID. Strongly recommended: it is what settles abbreviations and what lets a reviewer check the call. |
| `title` | no | Title of the source. Context only, e.g. it tells you a paper is about dopamine receptor neurons; never quote it as `evidence`. |

## Output

One record per name:

```yaml
name: CB                         # as given
outcome: GENE                    # GENE | NO_SINGLE_GENE | NOT_A_GENE_PRODUCT | UNRESOLVED
ncbi_gene_id: NCBIGene:83839     # GENE only
symbol: Calb1                    # GENE only: official symbol of that gene
gene_taxon: NCBITaxon:10116      # GENE only: the gene's species
method: PAPER_DEFINITION         # how the gene was reached (Steps 2–3)
kind: null                       # NO_SINGLE_GENE / NOT_A_GENE_PRODUCT / UNRESOLVED: see Step 1 and 3
antibody: null                   # when the name is an antibody or clone: the name as written
evidence: '"... CB, calbindin-D28k ..."'   # the quote relied on, verbatim
rationale: Paper defines CB as calbindin-D28k; claimants were Calb1 and Ctsb.
claimants: []                    # UNRESOLVED (ambiguous): the candidate genes
```

`symbol` is the gene's **official** symbol, never the source's wording.
Return records only; where they are stored is the caller's business.

## Step 1 — Decide what the name refers to

| The name is… | `outcome` (`kind`) |
|---|---|
| One gene or its protein, by symbol, protein name or abbreviation (`PV`, `CB`, `mGluR1`, `Sst`) | `GENE` |
| An antibody or clone for one protein (`NeuN` → Rbfox3, `TuJ1` → Tubb3) | `GENE`, with `antibody` set |
| An epitope on a modified form: glycoform or PTM (`PSA-NCAM`, `phospho-CREB`) | `NO_SINGLE_GENE` (`GLYCOFORM` / `PTM_STATE`), `antibody` set if it is one. The carrier gene's mRNA is not a proxy |
| A family (`CaMKII`, `NMDA receptor`, `GABA-A receptor`) | `NO_SINGLE_GENE` (`GENE_FAMILY`) |
| Not a product of the cell's genes (BrdU, EdU, tracers, dyes) | `NOT_A_GENE_PRODUCT` (`EXOGENOUS_LABEL`) |
| Not a gene term at all, though it looks like one (a region such as `CA1`, a cell type, an abbreviation for something else) | `NOT_A_GENE_PRODUCT` (`NON_GENE_TERM`) |

Only `GENE` names go through Steps 2–3.

## Step 2 — Look the name up in the taxon

The lookup needs a species. If `taxon` is a species, use it. If it is a
higher taxon, use the species the evidence comes from; if the evidence
doesn't say, say so in `rationale` and pick the taxon's best-studied member
(mouse for Murinae). Never use a species outside `taxon`.

Look up the name as written. Two cases look up a different name instead,
with `name` still as written:

- The evidence defines it ("CB, calbindin-D28k"): look up the gene it
  names; `method` is `PAPER_DEFINITION`.
- It is an antibody or clone whose target is well established (`TuJ1` →
  class III beta-tubulin, `NeuN` → Rbfox3): look up the target gene;
  `method` is `ANTIBODY_TARGET`, and `rationale` says what the antibody
  detects so a reviewer can check it.
- The evidence doesn't define it, but it is a standard abbreviation in the
  source's field for a gene the lookup of the name would not give (`D1` and
  `D2` for dopamine receptors, `SOM` for somatostatin): look up that gene;
  `method` is `FIELD_CONVENTION`, and `rationale` states the convention.

The gene ID and symbol still come from the lookup, never from memory.

The lookup tool is described under **Lookup tool** below.

## Step 3 — Act on the lookup `method`

| `method` | Action |
|---|---|
| `EXACT_SYMBOL` | `GENE`: take the gene's ID and official symbol. |
| `UNIQUE_SYNONYM` | `GENE`, after checking the gene fits the evidence and the field. One claimant means only that one gene lists the string, not that the source means it: `D1` → Dio1, `GAD` → Uchl1, `GABAA` → Gabrg1 are all single matches. If it doesn't fit, go back to Step 1 or 2. |
| `CASE_INSENSITIVE_SYMBOL` | `GENE`, unless a caution below applies or other genes also claim the name — then check the evidence means this one. |
| `AMBIGUOUS` | Pick **one gene from the claimants**, never another. Use the evidence first and quote it; where it doesn't define the name, the field's convention may settle it (`SOM` in a neuroscience source is Sst, not Grhl3) — say so in `rationale`. If neither settles it: `UNRESOLVED` (`AMBIGUOUS`), with the claimants. |
| `NO_MATCH` | Not a name of any gene in the species. If the evidence names the gene, look that up (Step 2). Otherwise reconsider Step 1; if still unclear, `UNRESOLVED` (`NO_MATCH`). |

Never return a gene the lookup did not produce, and never fill in an ID from
memory.

## Cautions

- **Tokens that look like genes but aren't.** A case-insensitive hit on a
  region or other non-gene token is a red flag: `CA1` → Ca1 (carbonic
  anhydrase 1, formerly Car1), `CA3` → Ca3; `SP`, `SO`, `SR` are hippocampal
  layers (stratum pyramidale, oriens, radiatum), not substance P. Use the
  evidence to check the source means a gene. This is why the evidence quote
  matters.
- **Families behind one abbreviation.** `GAD` (Gad1 + Gad2), `GABAA`,
  `nAChR`, `CaMKII` name several genes; the lookup may still return one.
  Unless the source names a subunit or isoform (`GAD67`, `CaMKIIα`), it is
  `NO_SINGLE_GENE` (`GENE_FAMILY`).
- **Field convention vs evidence.** Where the decision rests on the field's
  conventions rather than the quote, say so in `rationale`, so a reviewer
  can tell a reading of the source from background knowledge.
- **Species case.** `SST` (human style) in a mouse paper means Sst; the
  official symbol follows the gene's species, not the source.

## Lookup tool

In this repository:

| `taxon` / species | Command |
|---|---|
| The species of a local atlas taxonomy (mouse → `CCN20230722`) | `just resolve-gene-names CCN20230722 NAME…` (offline) |
| Any species | `just resolve-gene-names NCBITaxon:{species} NAME…` (network) |

It returns JSON per name: `method`, `gene` (`ncbi_gene_id`, `label` = the
official symbol), `claimants`. Use `label` as `symbol`. The network form
queries the Translator Name Resolver for that species only; it does not
search descendants of a higher taxon, hence Step 2's choice of species.
