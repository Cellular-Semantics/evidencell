# Marker gene IDs in the KB

How evidencell records a classical node's markers (`defining_markers`,
`negative_markers`, `neuropeptides`) and the gene each one means (#216,
#244). The name → gene lookup itself is the `gene-id-curation` skill
(`.claude/skills/gene-id-curation/SKILL.md`), which is repo-independent;
this page says how to call it and where its result goes.

## Calling the skill

- `name`: the marker as the paper writes it.
- `taxon`: the node's `species` (or the graph's). Settle it before calling;
  a node without a species gets `name_in_source` only, and a row in the
  unresolvable list (`PENDING_SPECIES`).
- `evidence`: the quote that asserts the marker (from `references.json`)
  and its PMID/DOI.

## Recording the result

```yaml
- name_in_source: CB          # the skill's `name` — never checked
  symbol: Calb1               # the skill's `symbol` (official)
  ncbi_gene_id: NCBIGene:83839
  sources:
    - marker_type: PROTEIN
      antibody: {name_in_source: "anti-calbindin D-28k"}   # the skill's `antibody`
      notes: "Paper defines CB as calbindin-D28k."          # the skill's `rationale`
      ...
```

| Skill `outcome` | KB |
|---|---|
| `GENE` | `name_in_source` + `symbol` + `ncbi_gene_id`; `rationale` in the source's `notes` when the call needed judgement (ambiguity, `PAPER_DEFINITION`, `ANTIBODY_TARGET`, higher taxon) |
| `NO_SINGLE_GENE` | `name_in_source` only, `antibody` on the source if any; row in the unresolvable list with the `kind` |
| `NOT_A_GENE_PRODUCT` | Not a marker. `EXOGENOUS_LABEL`: record what it shows (e.g. BrdU birth-dating) in the node's `notes`. `NON_GENE_TERM`: drop it, or put it where it belongs (a region in `anatomical_location`) |
| `UNRESOLVED` | `name_in_source` only; the reason in the node's `notes`; row in the unresolvable list (`UNSETTLED_AMBIGUITY` / `NO_MATCH`) |

`symbol` and `ncbi_gene_id` are set together or not at all.
`GeneDescriptor` has no `notes`; use the source's or the node's.

An antibody RRID goes in `antibody.rrid` only when the paper states it —
never looked up from a product name.

Unresolvable list: `research/gene_identity_216/unresolvable_markers.tsv`
(`file  node_id  field  name_in_source  kind  reason`).

## Workflow notes

- `asta-report-ingest` has only the synthesis report: leave `UNRESOLVED`
  ambiguous markers as `name_in_source` only;
  `evidence-extraction` settles them from the primary paper.
- Atlas markers are not curated: their metadata spelling goes in
  `name_in_source`, and the gene is resolved in the taxonomy DB.

## What the IDs do downstream

- `find-candidates` / Stage B score a marker on the atlas expression of its
  `ncbi_gene_id`. A gene of another species is matched through its official
  `symbol` (rat Calb1 → mouse Calb1); `gene_resolution` in the discovery JSON
  shows how (`PINNED_ID` = the ID itself matched).
- A classical marker without an ID is `NO_GENE_ID`: not measured, never
  resolved by its name. The `NOT MEASURED` line on stderr lists them.

## What the pre-edit hook rejects

On every write to `kb/**/*.yaml` (`gene_identity.check_marker_gene_ids`,
`rrid.check_antibody_rrids`; see `.claude/anti-hallucination-hooks.md`):

- `symbol` without `ncbi_gene_id`, or the reverse;
- an ID that is not an NCBI gene, or is from a species outside the node's;
- a `symbol` that is not exactly the gene's official symbol;
- an antibody `rrid` the Antibody Registry doesn't know.

Unchecked IDs/RRIDs (service unreachable, not cached) are allowed and listed
under "Checks NOT run". `EVIDENCELL_SKIP_GENE_CHECK=1` /
`EVIDENCELL_SKIP_RRID_CHECK=1` bypass the checks — emergency only.

## No taxonomy-wide name → gene table

A name the lookup can't settle (`CB`: Calb1 or Ctsb) is settled per marker,
from its evidence, and recorded as that marker's `symbol` + `ncbi_gene_id`.
There is no table that fixes a name to one gene for a whole taxonomy: the
same string means different things in different sources (`CB` is calbindin
in an interneuron paper and cerebellum in WMB neighbourhood names).
