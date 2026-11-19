# Skill: Term grounding

## When to use

Use this skill whenever you write an ontology term into KB YAML: species,
anatomical locations, a graph's `brain_region`, transmitter CL terms. It says
which ontology each field takes, which tool finds the term, and how to make
sure the pre-edit hook will accept it.

The node's CL anchor (`cl_mapping`) is a judgement, not a lookup: use
`cl-mapping.md` for it.

---

## Which ontology, and which tool

The schema decides the ontology. Each term field has a binding to one of the
term enums (`NCBITaxonClassTerm`, `AnatomyTerm`, `CLClassTerm`), whose
description lists what it accepts. This table says how to find terms for each.

| Field | Binding | Ontologies | Find with |
|---|---|---|---|
| `species`, a graph's `species` | `NCBITaxonClassTerm` | NCBITaxon | `mcp__ols4__searchClasses(query="Mus musculus", ontologyId="ncbitaxon")` |
| `anatomical_location`, a graph's `brain_region` | `AnatomyTerm` | MBA (mouse), DHBA or HBA (human, primate), HOMBA, UBERON (fallback) | `mcp__ols4__searchClasses(query="...", ontologyId="mba")`, or `"dhba"`, `"uberon"` |
| `nt_type.cl_terms` | `CLClassTerm` | CL | `mcp__ols4__searchClasses(query="glutamatergic neuron", ontologyId="cl")` |
| `GeneDescriptor.ncbi_gene_id` | none yet | NCBI Gene | No lookup tool is wired in yet; follow the calling workflow (ingest leaves it null). |

`mcp__ols4__fetch(id="{ontology}+{IRI}")` reads a term's definition and
synonyms when the search result alone does not settle it.

For anatomy: pick the most specific structure the sources support, in the
atlas ontology for the node's species; use UBERON when no atlas term fits or
the type spans species. `name_in_source` is the structure's name as the source
writes it.

---

## Getting past the hook

Every term is an `OntologyTerm`: `id`, `label`, `name_in_source`, all required.

- `id` must have a recognised prefix (the schema lists them) and resolve.
- `label` must be the ontology's current label, exactly. Copy it from the
  lookup result, never from memory or from the source text.
- OLS shows Allen atlas labels with a species suffix that is not part of the
  label: `Paraventricular nucleus of the thalamus  ( mouse )` is written as
  `label: Paraventricular nucleus of the thalamus`. Drop the `( mouse )`,
  `( human dev )` or similar suffix. The hook checks against the ontology
  files, which do not carry it.
- The term must fall under the binding's root (e.g. an anatomy term must be an
  anatomical entity).

To check a file before or after editing:

```bash
just validate-terms-file kb/graphs/{region}/{node_id}.yaml
```

If the hook rejects a term, it reports the id and the label it expected. Fix
the label or choose a different term; never drop the field to get past it.
