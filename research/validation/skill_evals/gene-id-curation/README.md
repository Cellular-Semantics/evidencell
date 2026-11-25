# gene-id-curation skill eval

Test cases for the `gene-id-curation` skill (`.claude/skills/gene-id-curation/SKILL.md`):
names from real quotes where the mechanical lookup (`just resolve-gene-names`) is
ambiguous, confidently wrong, or matches a region token as a gene.

## Layout

| Path | Contents | Who sees it |
|---|---|---|
| `cases/gic-NN.yaml` | The skill's input only: `name`, `taxon`, `title`, `evidence` (`source`, `quote_key`, verbatim `text`) | The agent under test |
| `answers.yaml` | Per case: expected `outcome`, `kind`, accepted genes, how the taxon was set, the lookup's own answer (baseline), and what the case tests | The scorer only |

Quotes are copied from `references/{region}/quotes/` and titles from
`references/{region}/papers/`. Expected gene IDs come from
`just resolve-gene-names`, never from memory. Taxa come from the quote, title,
abstract or MeSH terms; `taxon_basis` in `answers.yaml` records which, and flags
the one set from background knowledge.

## Running a case

Never give the agent under test a path into this directory. For each case:

1. Dispatch a fresh subagent. The prompt names the skill and gives the case's
   input inline (the contents of `cases/gic-NN.yaml`, minus `id`), and asks for
   the skill's output record.
2. Save the returned record as `runs/{run_id}/gic-NN.yaml`.
3. Void the case if the transcript shows a read of `answers.yaml` or of this
   directory.

Variants worth comparing:

- **quote only**: drop `title` from the input.
- **quote + title**: the case as written.
- **baseline**: no agent; score `resolver_baseline` from `answers.yaml`.

## Scoring

A case passes when:

- `outcome` equals the expected `outcome`;
- for `GENE`, `ncbi_gene_id` is one of `accept` (a higher taxon such as Murinae
  lists a gene per species);
- for `NO_SINGLE_GENE` and `NOT_A_GENE_PRODUCT`, `kind` equals the expected
  `kind`.

`method` and `rationale` are not scored; read them for cases that fail, and
for whether a decision rests on the quote or on field convention.
