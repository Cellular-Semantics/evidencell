# Citation Traversal: Design Notes

> **Date**: 2026-03-22
> **Status**: Exploration — notes from candelabrum cell pilot
> **Context**: During the candelabrum cell lit-review pilot, we hit limitations with every available full-text retrieval and citation extraction approach. This document captures the design space, trade-offs, and a proposed portable pipeline.

---

## The problem

Citation traversal means: starting from a paper, identifying which of its references (and citers) are worth following, then recursively expanding the evidence base. This requires two capabilities:

1. **Locating relevant passages** — finding the parts of a paper that discuss the topic of interest
2. **Resolving inline citations** — mapping citation markers (e.g. `[23]`, `Smith et al., 2019`) in those passages to actual papers (DOIs, PMIDs, S2 corpus IDs)

These are distinct steps with different tool requirements.

---

## Available structured sources and what they provide

### ASTA snippet_search (Semantic Scholar)

Body-text snippets with pre-resolved inline citations. Two modes:

- **Scoped to a paper** (`paperIds` filter): returns snippets from that paper's body text, each with `refMention` objects carrying the cited paper's S2 corpus ID. This IS citation traversal — the citations are already resolved. Snippets also carry a `section` field (e.g. "Results", "Discussion") enabling section-based filtering.
- **Unscoped** (keyword query, no `paperIds`): returns snippets from any indexed paper. This is literature **discovery**, not traversal — but discovered papers can then be traversed via scoped search.

**What you get**:
- **Sections**: `snippet.section` field — can filter to e.g. Results + Discussion only
- **Inline citations**: `refMention` objects within each snippet, each with the cited paper's S2 corpus ID already resolved
- **Bibliography**: implicit — each refMention IS a resolved reference

**Strengths**:
- Pre-resolved citations — no parsing, no regex, no bibliography matching
- Section metadata for filtering
- Works at corpus scale — can search across many papers efficiently (like paperqa2 embedding retrieval, but with citation structure preserved)
- Semantic relevance ranking built in

**Limitations**:
- Not all papers have body text indexed. Osorno 2022 (PMID:35578131) had only title+abstract when searched as a seed. Coverage is improving but unpredictable.
- When body text is absent, scoped search returns only title/abstract snippets with no refMentions — silently degrades to no citation information.
- No control over snippet boundaries (they're pre-computed by S2)

**Access**: `mcp__Asta_semanticscholar__snippet_search` or S2 API directly.

### JATS XML (EuropePMC)

The gold standard for self-hosted parsing when available. Provides:

- **Sections**: `<sec sec-type="results">` with explicit type attributes
- **Inline citations**: `<xref ref-type="bibr" rid="ref-23">` linked to `<ref-list>` entries
- **Bibliography**: structured `<ref>` with DOI, PMID, title, authors

**Limitation**: EuropePMC doesn't have JATS for all papers. PMC9548381 (Osorno 2022) returned 404. Coverage is best for PMC OA subset papers deposited directly by publishers.

**Access**: `https://www.ebi.ac.uk/europepmc/webservices/rest/{PMCID}/fullTextXML`

### PMC HTML

Available for essentially all PMC papers (broader coverage than JATS). Provides:

- **Sections**: `<div>` with `id="sec-N"`, `<h2>`/`<h3>` headings
- **Inline citations**: `<a>` tags with `href="#ref-N"` or `data-rid` attributes linking to bibliography
- **Bibliography**: `<div id="ref-list-1">` with individual `<div id="ref-N">` entries containing text and sometimes DOI links

**Limitation**: Less formally structured than JATS — requires HTML-specific parsing (BeautifulSoup). Structure varies somewhat across publishers.

**Access**: `https://pmc.ncbi.nlm.nih.gov/articles/{PMCID}/` (confirmed working via WebFetch)

### PDF via PyMuPDF

Available for any downloadable PDF (broad coverage but requires the file). Provides:

- **Sections**: no explicit structure — must be inferred from font size, bold, heading patterns (heuristic, unreliable)
- **Inline citations**: preserved as text characters (`[23]`, `[23,24]`) — extractable via regex
- **Bibliography**: preserved as text — extractable via regex, but matching to DOIs/PMIDs requires title-based lookup against Semantic Scholar or CrossRef

**Limitation**: No structural markup. Citation resolution is fuzzy (regex + title matching). Already a dependency of paperqa2 (`paperqa-pymupdf`).

---

## Step 1: Locating relevant passages

Four strategies, in order of increasing local infrastructure:

### A. ASTA snippet_search (scoped to paper)

Query ASTA with topic keywords, scoped to the paper's S2 ID. Returns ranked snippets with section labels and pre-resolved refMentions.

- **Works when**: ASTA has body text for the paper. Section filtering (Results, Discussion) focuses results.
- **Advantage**: citations already resolved. Works at corpus scale — can search across many papers in a single query, like embedding retrieval but with citation structure intact. No local indexing needed.
- **Breaks when**: paper body text not indexed in ASTA (silent degradation to abstract-only).

### B. Whole-paper-to-LLM

Send the full paper text (or relevant sections) directly to the LLM and ask it to identify passages relevant to the topic that cite other papers.

- **Works when**: paper fits in context window. Osorno at ~18K tokens fits easily. Most single papers do.
- **Advantage**: simplest local approach. LLM can reason about *which* citations matter and *why*.
- **Breaks when**: processing batches of papers, or papers >100K tokens.

### C. Embedding-based chunk retrieval (paperqa2 approach)

Index paper into overlapping text chunks via sentence-transformer embeddings, retrieve top-k by cosine similarity to a query.

- **Works when**: many papers in local corpus, need to find relevant passages across all of them.
- **Advantage**: scales to large local corpora. Already implemented in `paperqa2_cyberian/retrieve_chunks.py`.
- **Problem**: chunk boundaries can split a sentence from its citation marker. A chunk saying "consistent with previous findings" is useless if `[23,24]` fell into the next chunk. Larger chunks + more overlap mitigates but doesn't eliminate this.
- **Possible mitigation**: [contextual retrieval](https://www.anthropic.com/engineering/contextual-retrieval) — prepend each chunk with LLM-generated context summarising where it sits in the document. This could preserve citation context across chunk boundaries, at the cost of an LLM call per chunk at index time.

### D. Section-aware targeted retrieval (hybrid)

Parse sections first (from JATS/HTML structure). Send only Results + Discussion sections to LLM (skip Methods boilerplate, bibliography, figure legends). Within those sections, inline citations are already resolved.

- **Works when**: structured source (JATS or HTML) is available.
- **Advantage**: focused context, no chunking boundary problems, citations pre-resolved.
- **Breaks when**: only PDF available (no section structure).

**Recommendation**: A (ASTA) as the primary approach — it combines passage finding and citation resolution in one step. When ASTA lacks body text: D (section-aware) if JATS/HTML available, B (whole-paper) for single papers with only PDF/text, C (embedding retrieval) for corpus-scale search across many local papers.

---

## Step 2: Resolving inline citations to papers

Once relevant passages are identified, citation markers must be mapped to actual papers.

| Source | Resolution method |
|--------|------------------|
| ASTA snippets | Already resolved: `refMention.citedPaper.corpusId` |
| JATS XML | Direct: `<xref rid="ref-23">` → `<ref id="ref-23">` → DOI/PMID |
| PMC HTML | Direct: `<a href="#ref-23">` → `<div id="ref-23">` → DOI/PMID |
| PDF/text | Regex: extract `[23]` → find ref 23 in bibliography section → title match against S2/CrossRef |

For ASTA, JATS, and HTML, citation resolution is mechanical. For PDF/text, regex is used **only for this mechanical extraction step** — not for finding relevant passages (that's the LLM/embedding's job).

---

## Comparison: ASTA vs local parsing

| Dimension | ASTA snippet_search | Local parsing (JATS/HTML/PDF) |
|-----------|---------------------|-------------------------------|
| Coverage | Unpredictable — depends on S2 indexing | PMC HTML very broad; PDF nearly universal |
| Section info | Yes (`snippet.section`) | JATS/HTML: yes. PDF: heuristic only |
| Citation resolution | Pre-resolved (S2 corpus IDs) | JATS/HTML: structured. PDF: regex + title match |
| Corpus-scale search | Yes — single API call across many papers | Requires local indexing (paperqa2 embeddings) |
| Offline/portable | No — requires S2 API | Yes — all local |
| Snippet boundaries | Fixed by S2, no control | Chunking strategy is configurable |
| Rate limits | S2 API limits | Only NCBI rate limits for fetching HTML |

**When to use which**:
- ASTA first for any paper — if body text is indexed, you get citation traversal for free with section filtering
- Local parsing as fallback when ASTA lacks body text, or when you need offline reproducibility
- Both can work at corpus scale: ASTA via API, local via paperqa2 embedding index

---

## Proposed portable pipeline

No Grobid server. No Docker. All pip-installable.

```
Input: paper ID (PMID, PMCID, DOI, or S2 corpus ID)
                    │
                    ▼
         ASTA snippet_search (scoped)
         body text indexed?
        ┌── yes ──────┴────── no ──┐
        ▼                          ▼
  Snippets with              Resolve to PMCID
  refMentions +              (via artl-mcp / S2)
  section labels                   │
        │                          ▼
        │               ┌─── JATS XML available? ───┐
        │               │ yes                       │ no
        │               ▼                           ▼
        │          Parse JATS XML           PMC HTML available?
        │          (lxml/etree)          ┌── yes ──┴── no ──┐
        │               │                ▼                   ▼
        │               │         Parse PMC HTML         PDF available?
        │               │        (BeautifulSoup)      ┌─ yes ─┴─ no ─┐
        │               │              │              ▼               ▼
        │               │              │         PyMuPDF text     Abstract only
        │               │              │         + regex refs     (flag gap)
        │               │              │              │
        ▼               ▼              ▼              ▼
   ┌────────────────────────────────────────────────────┐
   │  Uniform output:                                   │
   │  {                                                 │
   │    sections: {                                     │
   │      "Results": {                                  │
   │        text: "...",                                │
   │        citations: [                                │
   │          {marker: "[23]" | refMention,             │
   │           title: "...",                            │
   │           doi: "...",                              │
   │           pmid: "...",                             │
   │           s2_id: "..."}                            │
   │        ]                                           │
   │      },                                            │
   │      "Discussion": { ... }                         │
   │    },                                              │
   │    bibliography: [ ... ],                          │
   │    source: "asta" | "jats" | "pmc_html" | "pdf"   │
   │  }                                                 │
   └──────────────────┬─────────────────────────────────┘
                      │
                      ▼
   Send relevant sections to LLM:
   "Which cited papers are most relevant to {topic}?
    Return paper IDs + reasoning."
   (Skip this step for ASTA path if snippet ranking
    + refMention filtering is sufficient)
                      │
                      ▼
   Traversal candidates (DOI/PMID/S2 ID + reason)
```

### Dependencies

All pip-installable, no servers:

- `lxml` — JATS XML parsing
- `beautifulsoup4` + `lxml` — PMC HTML parsing
- `pymupdf` — PDF text extraction (already a paperqa2 dep)
- `httpx` or `requests` — fetching JATS/HTML/Unpaywall
- `re` (stdlib) — citation marker regex for PDF fallback path
- ASTA/S2 API access — for the primary path (already available via MCP)

### Relationship to existing tools

- **ASTA snippet_search**: the primary citation traversal mechanism. When body text is indexed, this is the fastest path with the richest output (pre-resolved citations + section labels + semantic ranking). The local parsing pipeline covers the gap when ASTA lacks body text.
- **artl-mcp**: continues to handle paper metadata, search, identifier resolution. Also the entry point for JATS XML retrieval (`get_europepmc_full_text` returns JATS when available).
- **paperqa2**: embedding retrieval remains useful for corpus-scale search across many local papers — e.g. when building a local evidence corpus from papers fetched via citation traversal. Complementary to ASTA: paperqa2 searches local files, ASTA searches the S2 index. Contextual retrieval could improve chunk quality.
- **Unpaywall**: OA pre-check to decide whether to persist through local fallbacks when ASTA and artl-mcp fail.

---

## Tested during pilot (2026-03-20/22)

| Approach | Paper | Result |
|----------|-------|--------|
| ASTA snippet_search (seed-scoped) | PMID:35578131 | Title+abstract only — no body text, no refMentions |
| ASTA snippet_search (unscoped, topic keywords) | "candelabrum cell" | Found Schilling 2023 review with body text + refMentions — discovery, not traversal of seed |
| artl-mcp `get_europepmc_full_text` | PMC9548381 | Empty (no JATS XML) |
| artl-mcp `get_europepmc_pdf_as_markdown` | PMC9548381 | Empty |
| JATS XML direct | PMC9548381 | 404 |
| WebFetch PMC HTML | PMC9548381 | Success (73KB text, but citation structure lost in markdown conversion) |
| paperqa2 retrieve_chunks (.txt) | PMC9548381 text | Success — 10 relevant chunks, but citation markers stripped |
| curl PDF download | PMC9548381 | Failed — PMC JS redirect gate |
| S2 get_paper references | PMID:35578131 | Success — 56 references with S2 IDs and titles |

**Key findings**:
- ASTA is the best path when it works, but coverage is unpredictable — must detect and fall back gracefully.
- PMC HTML is the most reliable local structured source for PMC papers. The pilot's mistake was converting it to markdown (losing citation structure). Parsing the HTML DOM directly would have preserved sections + resolved citations.
- The S2 reference list provides a complete bibliography even when body text is unavailable — useful for the PDF regex fallback path (match extracted `[N]` markers against known references).

---

## Open questions

1. **ASTA body-text coverage**: what fraction of papers in our domain (neuroscience, cell types) have body text indexed? Worth profiling on the existing paper catalogues to set expectations.
2. **PMC HTML structure stability**: does the HTML structure vary significantly across publishers/years? Need to test on a sample of papers to assess parser robustness.
3. **Non-PMC papers**: for papers only available as publisher PDFs (not in PMC), the PDF+regex path is the only local option. How common is this for our use case? Most neuroscience papers have PMC deposits.
4. **Contextual retrieval for paperqa2**: Anthropic's [contextual retrieval](https://www.anthropic.com/engineering/contextual-retrieval) approach prepends each chunk with LLM-generated context at index time. This could preserve citation context across chunk boundaries. Cost: one LLM call per chunk during indexing. Worth prototyping on the Osorno paper to measure improvement.
5. **Integration point**: should this be a standalone Python module in `src/evidencell/` or a shared library also usable from `paperqa2_cyberian`? Probably starts in evidencell, extracted later if needed.
6. **Rate limiting**: PMC HTML fetching at scale — what are NCBI's rate limits? May need API key or throttling for batch traversal.
