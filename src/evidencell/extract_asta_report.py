"""
extract_asta_report — deterministic pymupdf-based parser for ASTA deep research PDFs.

Replaces the LLM-based Step 1 + Step 1b of the asta-report-ingest orchestrator
with fast, reliable extraction of:
  - Verbatim quotes from Evidence subsections (italic, size ~9, delimited by "...")
  - Paper attributions (author_key) associated with each quote
  - Section structure (headers at size >= 16)
  - Semantic Scholar corpus IDs from embedded hyperlinks
  - Reference list entries from end-of-document section

Does NOT extract proposed_types (classical cell type identification) — that still
requires LLM judgement and is handled by a slimmed-down Step 1c subagent.

Usage:
  uv run python -m evidencell.extract_asta_report path/to/report.pdf [--output-dir DIR] [--pretty]

Without --output-dir: prints JSON summary to stdout.
With --output-dir: writes extracted_quotes.json, reference_list.json, pdf_corpus_ids.json.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

import fitz  # pymupdf


# ---------------------------------------------------------------------------
# Constants — empirically determined from ASTA deep research PDF format
# ---------------------------------------------------------------------------

SECTION_HEADER_MIN_SIZE = 15.5
EVIDENCE_HEADER_TEXT = "Evidence"
QUOTE_SIZE_TARGET = 9.0
ATTRIBUTION_SIZE_TARGET = 10.0
SYNTHESIS_SIZE_TARGET = 11.0
SIZE_TOLERANCE = 1.0

# Matches (Author et al., 2020) or (Author, 2020) or (Author & Jones, 2020)
AUTHOR_KEY_RE = re.compile(r"\(([^)]{3,80},\s*\d{4})\)")
S2_CORPUS_RE = re.compile(r"semanticscholar\.org/p/(\d+)")

# Quote delimiters — accept straight and curly quotes
OPEN_QUOTES = {'"', "\u201c"}
CLOSE_QUOTES = {'"', "\u201d"}


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class ExtractedQuote:
    text: str
    section: str


@dataclass
class AuthorQuotes:
    author_key: str
    quotes: list[ExtractedQuote] = field(default_factory=list)


@dataclass
class ReferenceEntry:
    author_key: str
    title: str
    year: int | None


@dataclass
class AstaReportExtraction:
    sections: list[str]
    extracted_quotes: dict[str, AuthorQuotes]
    reference_list: list[ReferenceEntry]
    corpus_ids: list[str]
    total_quotes: int
    total_papers: int

    def to_dict(self) -> dict:
        return asdict(self)

    def write_outputs(self, output_dir: Path) -> None:
        """Write the three orchestrator-expected JSON files."""
        output_dir.mkdir(parents=True, exist_ok=True)

        # extracted_quotes.json — keyed by author_key
        eq = {}
        for ak, aq in self.extracted_quotes.items():
            eq[ak] = {
                "author_key": aq.author_key,
                "quotes": [{"text": q.text, "section": q.section} for q in aq.quotes],
            }
        (output_dir / "extracted_quotes.json").write_text(
            json.dumps(eq, indent=2, ensure_ascii=False)
        )

        # reference_list.json
        rl = [{"author_key": r.author_key, "title": r.title, "year": r.year}
              for r in self.reference_list]
        (output_dir / "reference_list.json").write_text(
            json.dumps(rl, indent=2, ensure_ascii=False)
        )

        # pdf_corpus_ids.json
        (output_dir / "pdf_corpus_ids.json").write_text(
            json.dumps(self.corpus_ids, indent=2)
        )


# ---------------------------------------------------------------------------
# Span extraction
# ---------------------------------------------------------------------------


@dataclass
class Span:
    text: str
    size: float
    is_italic: bool
    page: int


def _extract_spans(doc: fitz.Document) -> list[Span]:
    """Flatten all pages into an ordered list of Span objects."""
    spans: list[Span] = []
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for sp in line["spans"]:
                    text = sp["text"]
                    if not text.strip():
                        continue
                    spans.append(Span(
                        text=text,
                        size=sp["size"],
                        is_italic=bool(sp["flags"] & 2),
                        page=page_num,
                    ))
    return spans


def _extract_corpus_ids(doc: fitz.Document) -> list[str]:
    """Extract Semantic Scholar corpus IDs from all hyperlinks in the PDF."""
    ids: set[str] = set()
    for page in doc:
        for link in page.get_links():
            m = S2_CORPUS_RE.search(link.get("uri", ""))
            if m:
                ids.add(m.group(1))
    return sorted(ids)


# ---------------------------------------------------------------------------
# Size helpers
# ---------------------------------------------------------------------------


def _is_section_header(span: Span) -> bool:
    return span.size >= SECTION_HEADER_MIN_SIZE


def _is_quote_span(span: Span) -> bool:
    return span.is_italic and abs(span.size - QUOTE_SIZE_TARGET) < SIZE_TOLERANCE


def _is_attribution(span: Span) -> bool:
    return (abs(span.size - ATTRIBUTION_SIZE_TARGET) < SIZE_TOLERANCE
            and AUTHOR_KEY_RE.search(span.text) is not None)


def _is_evidence_header(span: Span) -> bool:
    return (span.text.strip() == EVIDENCE_HEADER_TEXT
            and span.size > SYNTHESIS_SIZE_TARGET)


# ---------------------------------------------------------------------------
# Quote text cleaning
# ---------------------------------------------------------------------------


def _clean_quote(text: str) -> str:
    """Strip outer quotation marks and normalise whitespace."""
    text = text.strip()
    # Strip leading quote mark
    if text and text[0] in OPEN_QUOTES:
        text = text[1:]
    # Strip trailing quote mark
    if text and text[-1] in CLOSE_QUOTES:
        text = text[:-1]
    # Collapse internal whitespace
    text = " ".join(text.split())
    return text.strip()


def _extract_author_key(text: str) -> str | None:
    """Extract author key from an attribution span, e.g. '(Hooft et al., 2000)'."""
    m = AUTHOR_KEY_RE.search(text)
    if m:
        return m.group(1).strip()
    return None


# ---------------------------------------------------------------------------
# State machine: parse sections, evidence blocks, quotes
# ---------------------------------------------------------------------------


def _parse_sections_and_quotes(
    spans: list[Span],
) -> tuple[list[str], dict[str, AuthorQuotes]]:
    """Walk the span stream, identify sections and extract quotes with attributions."""
    sections: list[str] = []
    quotes_map: dict[str, AuthorQuotes] = {}

    current_section: str = ""
    in_evidence: bool = False
    current_author_key: str | None = None
    quote_accumulator: list[str] = []
    accumulating_quote: bool = False

    def _flush_quote() -> None:
        nonlocal accumulating_quote, quote_accumulator
        if accumulating_quote and current_author_key and quote_accumulator:
            full_text = _clean_quote(" ".join(quote_accumulator))
            if full_text:
                if current_author_key not in quotes_map:
                    quotes_map[current_author_key] = AuthorQuotes(
                        author_key=current_author_key
                    )
                quotes_map[current_author_key].quotes.append(
                    ExtractedQuote(text=full_text, section=current_section)
                )
        accumulating_quote = False
        quote_accumulator = []

    for span in spans:
        # Section header — ends evidence block
        if _is_section_header(span):
            _flush_quote()
            header_text = span.text.strip()
            # Accumulate multi-span headers (e.g. long titles across spans)
            if sections and sections[-1] == header_text:
                continue
            # Skip table of contents entries and title
            if header_text not in ("Table of Contents",):
                current_section = header_text
                if current_section not in sections:
                    sections.append(current_section)
            in_evidence = False
            current_author_key = None
            continue

        # Evidence subsection marker
        if _is_evidence_header(span):
            _flush_quote()
            in_evidence = True
            current_author_key = None
            continue

        if not in_evidence:
            # We only extract quotes from Evidence blocks
            continue

        # Paper attribution within Evidence block
        if _is_attribution(span):
            _flush_quote()
            ak = _extract_author_key(span.text)
            if ak:
                current_author_key = ak
            continue

        # Quote span (italic, small size)
        if _is_quote_span(span) and current_author_key:
            text = span.text
            if not accumulating_quote:
                # Start new quote — text should begin with a quote mark
                stripped = text.lstrip()
                if stripped and stripped[0] in OPEN_QUOTES:
                    accumulating_quote = True
                    quote_accumulator = [text]
                elif stripped and stripped[0] == '"':
                    accumulating_quote = True
                    quote_accumulator = [text]
            else:
                # Continue accumulating
                quote_accumulator.append(text)

            # Check if quote is complete (ends with closing quote mark)
            if accumulating_quote:
                joined = " ".join(quote_accumulator).rstrip()
                if joined and joined[-1] in CLOSE_QUOTES | {'"'}:
                    _flush_quote()
            continue

        # Non-quote, non-attribution span inside evidence — could be paper title
        # (hyperlinked text between attribution and quotes). Flush any pending quote.
        if accumulating_quote and not _is_quote_span(span):
            _flush_quote()

    # Final flush
    _flush_quote()
    return sections, quotes_map


# ---------------------------------------------------------------------------
# Reference list extraction (end-of-document)
# ---------------------------------------------------------------------------


def _parse_reference_list(spans: list[Span]) -> list[ReferenceEntry]:
    """Extract reference entries from the end-of-document reference list.

    ASTA reference lists are less consistently formatted than Evidence blocks.
    We use a best-effort approach: find attribution patterns and grab the
    following text as title. The corpus IDs from hyperlinks are the primary
    resolution mechanism — this is supplementary.
    """
    # Find where "References" section starts (if any)
    ref_start = None
    for i, span in enumerate(spans):
        if _is_section_header(span) and "reference" in span.text.strip().lower():
            ref_start = i
            break

    if ref_start is None:
        return []

    entries: list[ReferenceEntry] = []
    seen_keys: set[str] = set()

    # Walk from Evidence sections and collect attributions we've seen
    # Actually, walk the whole document for all attribution-style spans in evidence blocks
    # to build the reference list from the evidence attributions themselves
    # (ASTA reference lists at end of document are inconsistently formatted)

    for i in range(ref_start, len(spans)):
        span = spans[i]
        ak = _extract_author_key(span.text)
        if ak and ak not in seen_keys:
            # Extract year from the author key
            year_match = re.search(r"(\d{4})", ak)
            year = int(year_match.group(1)) if year_match else None

            # Look ahead for title text (next non-attribution span)
            title = ""
            for j in range(i + 1, min(i + 5, len(spans))):
                next_span = spans[j]
                if _is_section_header(next_span) or _is_attribution(next_span):
                    break
                if next_span.text.strip():
                    title = next_span.text.strip()
                    break

            entries.append(ReferenceEntry(author_key=ak, title=title, year=year))
            seen_keys.add(ak)

    return entries


def _build_reference_list_from_evidence(
    quotes_map: dict[str, AuthorQuotes],
    spans: list[Span],
) -> list[ReferenceEntry]:
    """Build reference list from evidence-section attributions + title text.

    More reliable than parsing the end-of-document reference list, since
    the Evidence blocks have consistent structure: attribution → title → quotes.
    """
    entries: list[ReferenceEntry] = []
    seen_keys: set[str] = set()

    in_evidence = False

    for i, span in enumerate(spans):
        if _is_section_header(span):
            in_evidence = False
            continue
        if _is_evidence_header(span):
            in_evidence = True
            continue
        if not in_evidence:
            continue

        if _is_attribution(span):
            ak = _extract_author_key(span.text)
            if ak and ak not in seen_keys:
                year_match = re.search(r"(\d{4})", ak)
                year = int(year_match.group(1)) if year_match else None

                # Next span(s) after attribution should be the paper title
                # (typically a hyperlinked span at synthesis size)
                title_parts: list[str] = []
                for j in range(i + 1, min(i + 8, len(spans))):
                    ns = spans[j]
                    if _is_quote_span(ns) or _is_attribution(ns) or _is_evidence_header(ns):
                        break
                    if _is_section_header(ns):
                        break
                    title_parts.append(ns.text.strip())

                title = " ".join(title_parts).strip()
                entries.append(ReferenceEntry(author_key=ak, title=title, year=year))
                seen_keys.add(ak)

    return entries


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------


def extract_asta_report(pdf_path: str | Path) -> AstaReportExtraction:
    """Parse an ASTA deep research PDF and extract structured data.

    Args:
        pdf_path: Path to the ASTA PDF file.

    Returns:
        AstaReportExtraction with quotes, references, corpus IDs, and sections.

    Raises:
        FileNotFoundError: If the PDF does not exist.
        RuntimeError: If pymupdf cannot open the file.
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    doc = fitz.open(str(pdf_path))

    # Phase 1: Extract all spans
    spans = _extract_spans(doc)

    # Phase 2: Extract corpus IDs from hyperlinks
    corpus_ids = _extract_corpus_ids(doc)

    # Phase 3: Parse sections and quotes
    sections, quotes_map = _parse_sections_and_quotes(spans)

    # Phase 4: Build reference list from evidence attributions
    reference_list = _build_reference_list_from_evidence(quotes_map, spans)

    # Also try end-of-document reference list for any we missed
    end_refs = _parse_reference_list(spans)
    seen_keys = {r.author_key for r in reference_list}
    for r in end_refs:
        if r.author_key not in seen_keys:
            reference_list.append(r)
            seen_keys.add(r.author_key)

    total_quotes = sum(len(aq.quotes) for aq in quotes_map.values())
    total_papers = len(quotes_map)

    doc.close()

    return AstaReportExtraction(
        sections=sections,
        extracted_quotes=quotes_map,
        reference_list=reference_list,
        corpus_ids=corpus_ids,
        total_quotes=total_quotes,
        total_papers=total_papers,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract structured data from an ASTA deep research PDF."
    )
    parser.add_argument("pdf_path", help="Path to the ASTA PDF file")
    parser.add_argument(
        "--output-dir",
        help="Write extracted_quotes.json, reference_list.json, pdf_corpus_ids.json to this dir",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    args = parser.parse_args()

    try:
        result = extract_asta_report(args.pdf_path)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.output_dir:
        result.write_outputs(Path(args.output_dir))
        print(
            f"Extracted {result.total_quotes} quotes across {result.total_papers} papers "
            f"in {len(result.sections)} sections. "
            f"{len(result.corpus_ids)} corpus IDs from hyperlinks. "
            f"{len(result.reference_list)} reference list entries."
        )
    else:
        indent = 2 if args.pretty else None
        print(json.dumps(result.to_dict(), indent=indent, ensure_ascii=False))


if __name__ == "__main__":
    main()
