# evidencell — planned functionality

*A knowledge base for cell type mapping evidence*

---

## The problem

Transcriptomic atlases (Allen WMBv1, HMBA Basal Ganglia) are defining cell types by gene expression at unprecedented resolution. But the neuroscience literature describes cell types by anatomy, electrophysiology, and histochemistry — built up over decades.

**Bridging these two worlds is hard:**
- Mappings are implicit, scattered across papers, or asserted without evidence
- Confidence is rarely quantified — how well-supported is a given correspondence?
- Caveats are buried — mouse vs. human, adult vs. developmental, in vitro vs. in vivo
- No shared format for recording or reviewing mapping claims

---

## What is evidencell?

A structured, curated knowledge base that makes cell type mappings **explicit, evidence-grounded, and reviewable**.

Each entry records:
- **Nodes** — the classical type and the atlas cluster being related
- **Edges** — the proposed relationship (equivalent, subset, overlapping, uncertain…)
- **Evidence** — literature, atlas metadata, annotation transfer results, with verbatim quotes and references
- **Confidence** — calibrated (HIGH / MODERATE / LOW / UNCERTAIN) with explicit rationale
- **Caveats** — species, developmental stage, experimental system, registration uncertainty
- **Proposed experiments** — what would raise or resolve confidence

Inspired by [dismech](https://github.com/monarch-initiative/dismech), a LinkML-based knowledge base for disease pathophysiology.

---

## Core concepts

### Evidence graph

```
  Basket cell (classical)  ──[EQUIVALENT · HIGH]──►  NBC_1 (WMBv1 cluster)
       │
       └──[PARTIAL_OVERLAP · MODERATE]──►  NBC_2 (WMBv1 cluster)
```

### Evidence types

| Type | Example |
|---|---|
| Literature | Snippet from paper, with verbatim quote and DOI |
| Atlas metadata | Marker table, MERFISH soma location from data release |
| Annotation transfer | MapMyCells F1 score mapping primate types to WMBv1 |
| Spatial colocation | Overlap with anatomical region from CCF registration |

### Confidence decision rule

- **HIGH** — ≥2 independent evidence types including ≥1 experimental
- **MODERATE** — single experimental or multiple consistent literature sources
- **LOW** — single literature source or indirect inference
- **UNCERTAIN** — evidence insufficient or contradictory

---

## The pipeline

Five stages, each building on the last:

```
1. Taxonomy ingestion      Parse atlas data release → CellTypeNode stubs
          │
          ▼
2. Literature review       ASTA semantic search + citation traversal
          │
          ▼
3. Evidence extraction     Auto-flag papers → human weeding → extract LiteratureEvidence
          │
          ▼
4. Mapping hypotheses      Agent proposes edges, relationships, confidence, caveats
          │
          ▼
5. Mapping report          Human-readable report with proposed experiments
```

Annotation transfer results (MapMyCells, Seurat) feed back in after step 5 to raise confidence where supported.

---

## Literature review — powered by ASTA

The literature step uses **Semantic Scholar's ASTA** API:
- Seed papers identified by keyword search or existing reviews
- **Citation traversal**: for each seed, retrieve papers it cites and is cited by; retrieve verbatim snippets within those papers matching the query
- Result: `all_summaries.json` — per-snippet summaries with exact quotes, corpus IDs, and relevance scores

**Key principle**: every evidence snippet in the KB must be a **verbatim substring** of the ASTA-retrieved text. No paraphrase. Validated automatically before the YAML can be written.

**Auto-flagging** scans the paper catalogue for signals that limit generalisability — non-human species, developmental timepoints, disease context, in vitro systems — so the expert reviewer can make informed decisions at the weeding gate.

---

## Human gates

Automation handles the tedious; experts make the judgements:

| Gate | What the expert decides |
|---|---|
| **Catalogue weeding** | Which papers are relevant to this mapping? Remove irrelevant ones before extraction runs. |
| **Evidence review** | Which proposed evidence items are valid? Approve, edit, or reject each one. |
| **Mapping review** | Is the proposed relationship and confidence level correct? Are the caveats complete? |
| **PR review** | Does the submitted KB entry meet quality standards? |

No automation skips a human gate. The pipeline proposes; the expert approves.

---

## The output — mapping report

Auto-generated from KB YAML. Example: GPi shell neuron → HMBA Group:GPi Shell

**Full report includes:**
- Graph diagram (Mermaid, with confidence colour-coding)
- Node descriptions — anatomy, markers, NT type, CL mapping
- Evidence chain per edge — each piece of evidence with verbatim quote and reference
- Caveats — MERFISH registration uncertainty, taxonomy level mismatch, cross-species extrapolation
- Open questions
- **Proposed experiments** — concrete, actionable:
  - *"Run MapMyCells on this primate dataset against WMBv1; report F1 at Supertype level"*
  - *"MERFISH with probes for Sst, Tbr1, Slc17a6 in GPi to validate spatial profile"*

**Condensed report**: one paragraph per edge, suitable for publication supplement or community review.

---

## Technology stack

| Component | Technology |
|---|---|
| Schema | [LinkML](https://linkml.io) — typed, ontology-grounded, validated |
| Ontology terms | CL, UBERON, NCBITaxon via OAK |
| Literature search | ASTA (Semantic Scholar) semantic search + citation traversal |
| Validation | `linkml-validate` + OAK term validation + snippet provenance check |
| Agentic workflows | Claude Code orchestrators (multi-step, file-state, subagent-spawning) |
| Task runner | `just` (human-readable recipes) wrapping Python scripts |
| Community review | GitHub PR + automated review skill |

---

## Milestones

| | Milestone | Key output |
|---|---|---|
| **M0** | Schema hardening | Schema v0.5 + pre-edit validator hook |
| **M1** | Repo bootstrap | evidencell repo, ≥3 ported examples, taxonomy ingestion |
| **M2** | Lit review → KB | End-to-end: deepsearch → extraction → validated LiteratureEvidence |
| **M3** | Mapping hypotheses | Draft MappingEdge YAML with relationship, confidence, caveats |
| **M4** | Reports (MVP) | Human-readable reports with proposed experiments |
| **M5** | Cross-validation + community | Annotation transfer feedback, compliance scoring, GitHub workflow |

M0 and M1 can run in parallel. Community curation opens at M5 but the KB is useful to specialists from M4 onward.

---

## What this enables

- **For a new brain region**: ingest taxonomy → run literature review → generate mapping report with proposed experiments in days rather than months
- **For a new atlas release**: re-run mapping hypotheses against updated taxonomy; confidence flags where mappings may have changed
- **For the community**: public KB with explicit evidence and confidence; reviewable via GitHub PR; links to CL, UBERON, and atlas resources
- **For annotation transfer experiments**: proposed experiments in the report are concrete enough to execute; results feed back directly into the KB to raise confidence

The evidence graph model is the contribution — not duplicating the atlases, but making the reasoning that connects them explicit and reviewable.
