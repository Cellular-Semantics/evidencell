# Skill: CL mapping

## When to use

Use this skill whenever you set, check or act on a node's `cl_mapping`: the
Cell Ontology term a KB node is anchored to, and how closely it fits.

- `asta-report-ingest`, the classification phase: set `cl_mapping` on new nodes.
- `cl-term-request`, Step 1: decide whether a node needs a new CL term.
- Review: check a `cl_mapping` someone else wrote.

CL mapping is a judgement with consequences downstream. A BROAD mapping names the
parent a new CL term would sit under, so it shapes `cl-term-request` and the
report introduction. Do not treat it as a term lookup. For grounding anatomy,
species or other ontology terms, use `term-grounding.md`.

Mapping literature types to atlas types is a different task, done by
`workflows/map-cell-type.md`; nothing here applies to it.

---

## The shape you write

`cl_mapping` is a `CLMapping` (see the schema, or the run's
`schema_subset.yaml`):

```yaml
cl_mapping:
  cl_term:
    id: CL:4023068
    label: thalamic excitatory neuron      # the CL label, exactly
    name_in_source: PVT glutamatergic neuron  # the node's name
  mapping_type: BROAD                      # EXACT | BROAD | RELATED
  mapping_notes: >
    What was searched, which candidates were considered, and why this term
    and this mapping type were chosen.
```

The pre-edit hook checks that `id` is a CL term and that `label` is its current
label. A label from memory is the commonest rejection; copy it from the lookup.

---

## Tools

| Purpose | Tool |
|---|---|
| Search CL by name or synonym | `mcp__ols4__searchClasses(query="...", ontologyId="cl", pageSize=10)` |
| Read a term: definition, synonyms, xrefs, definition references | `mcp__ols4__fetch(id="cl+http://purl.obolibrary.org/obo/CL_XXXXXXX")` |
| Walk up to find the closest broader term | `mcp__ols4__getAncestors(ontologyId="cl", classIri="http://purl.obolibrary.org/obo/CL_XXXXXXX")` |
| Look at existing subtypes of a candidate parent | `mcp__ols4__getChildren(ontologyId="cl", classIri="...")` |

---

## Procedure

1. **Read the node first.** Name, synonyms, species, definition basis, and any
   property fields already written (location, NT type, markers). These are
   what you compare a CL definition against.

2. **Search.** Search the node's name, then each synonym, then the shape
   "{location} {transmitter} neuron" (e.g. "thalamic glutamatergic neuron").
   Collect candidates.

3. **Read each plausible candidate's definition** with `fetch`. Judge on the
   definition, never on the label alone.

4. **Decide the mapping type:**

   | Type | When |
   |---|---|
   | EXACT | The CL definition describes this population: same cells, by its location, transmitter and defining features. CL terms are mostly species-neutral; a species-specific node can still be EXACT. |
   | BROAD | No term describes this population, and a term exists that contains it. Choose the **most specific** such term: walk up with `getAncestors` from the nearest candidate until you reach one whose definition the node satisfies in full. |
   | RELATED | A term overlaps the population but neither contains it nor matches it (e.g. defined by a different criterion that cuts across it). Say what the overlap is in `mapping_notes`. Prefer BROAD to a containing term when one exists. |

   - A name or synonym match alone is never EXACT. If the definition does not
     fit, use BROAD or RELATED.
   - Every non-terminal node gets a `cl_mapping`. If nothing better fits, map
     BROAD to the nearest general term that the node does satisfy (e.g.
     "glutamatergic neuron", "neuron").
   - A node with `subtype_of` usually shares its parent's CL term as a BROAD
     mapping. That is expected, not a reason to stretch to EXACT.

5. **Write `mapping_notes`:** the searches run, the candidates rejected and why,
   and what the node would need for an EXACT match.

6. **Never change an existing `cl_mapping`.** If your lookup disagrees with one,
   report the disagreement (the calling workflow says where) and leave the file
   as it is.

---

## What the mapping means downstream

| `mapping_type` | Consequence |
|---|---|
| EXACT | No new CL term is needed. `cl-term-request` stops. |
| BROAD | A new CL term may be needed; `cl_term` is its parent. |
| RELATED | A new CL term may be needed; the parent must be chosen by a curator. |
| absent | A gap. `cl-term-request` can proceed but leaves the parent blank; add a BROAD mapping first. |

When an EXACT term exists, collect the PMIDs and DOIs in its definition
references and xrefs: they are useful seed papers.
