"""Tests for evidencell.extract_asta_report — deterministic ASTA PDF parser."""

from __future__ import annotations

import hashlib
import json

import pytest

from evidencell.extract_asta_report import (
    AUTHOR_KEY_RE,
    S2_CORPUS_RE,
    AstaReportExtraction,
    AuthorQuotes,
    ExtractedQuote,
    ReferenceEntry,
    Span,
    _clean_quote,
    _extract_author_key,
    _is_attribution,
    _is_quote_span,
    _is_section_header,
    _parse_sections_and_quotes,
)


# ---------------------------------------------------------------------------
# Regex tests
# ---------------------------------------------------------------------------


class TestAuthorKeyRegex:
    def test_standard(self):
        assert AUTHOR_KEY_RE.search("(Smith et al., 2020)").group(1) == "Smith et al., 2020"

    def test_two_authors(self):
        assert AUTHOR_KEY_RE.search("(Smith & Jones, 2019)").group(1) == "Smith & Jones, 2019"

    def test_single_author(self):
        assert AUTHOR_KEY_RE.search("(Kitchigina, 2010)").group(1) == "Kitchigina, 2010"

    def test_particle(self):
        assert AUTHOR_KEY_RE.search("(van Hooft et al., 2000)").group(1) == "van Hooft et al., 2000"

    def test_hyphenated(self):
        m = AUTHOR_KEY_RE.search("(Hurtado-Zavala et al., 2017)")
        assert m.group(1) == "Hurtado-Zavala et al., 2017"

    def test_no_match_short(self):
        assert AUTHOR_KEY_RE.search("(ab)") is None

    def test_no_match_no_year(self):
        assert AUTHOR_KEY_RE.search("(Smith et al.)") is None


class TestCorpusIdRegex:
    def test_standard_url(self):
        m = S2_CORPUS_RE.search("https://www.semanticscholar.org/p/12345678")
        assert m.group(1) == "12345678"

    def test_no_match(self):
        assert S2_CORPUS_RE.search("https://pubmed.ncbi.nlm.nih.gov/12345") is None


# ---------------------------------------------------------------------------
# Quote cleaning tests
# ---------------------------------------------------------------------------


class TestCleanQuote:
    def test_strip_straight_quotes(self):
        assert _clean_quote('"hello world"') == "hello world"

    def test_strip_curly_quotes(self):
        assert _clean_quote('\u201chello world\u201d') == "hello world"

    def test_collapse_whitespace(self):
        assert _clean_quote('"  multiple   spaces  here  "') == "multiple spaces here"

    def test_empty(self):
        assert _clean_quote('""') == ""

    def test_no_quotes(self):
        assert _clean_quote("plain text") == "plain text"


# ---------------------------------------------------------------------------
# Span classification tests
# ---------------------------------------------------------------------------


class TestSpanClassification:
    def test_section_header(self):
        s = Span(text="Introduction", size=16.0, is_italic=False, page=0)
        assert _is_section_header(s)

    def test_not_section_header(self):
        s = Span(text="Some text", size=11.0, is_italic=False, page=0)
        assert not _is_section_header(s)

    def test_quote_span(self):
        s = Span(text='"A verbatim quote"', size=9.0, is_italic=True, page=0)
        assert _is_quote_span(s)

    def test_not_quote_span_wrong_size(self):
        s = Span(text='"text"', size=11.0, is_italic=True, page=0)
        assert not _is_quote_span(s)

    def test_not_quote_span_not_italic(self):
        s = Span(text='"text"', size=9.0, is_italic=False, page=0)
        assert not _is_quote_span(s)

    def test_attribution(self):
        s = Span(text="(Smith et al., 2020)", size=10.0, is_italic=False, page=0)
        assert _is_attribution(s)

    def test_not_attribution_wrong_size(self):
        s = Span(text="(Smith et al., 2020)", size=11.0, is_italic=False, page=0)
        assert not _is_attribution(s)


# ---------------------------------------------------------------------------
# Author key extraction
# ---------------------------------------------------------------------------


class TestExtractAuthorKey:
    def test_standard(self):
        assert _extract_author_key("(Hooft et al., 2000)") == "Hooft et al., 2000"

    def test_no_match(self):
        assert _extract_author_key("some random text") is None


# ---------------------------------------------------------------------------
# State machine: parse sections and quotes
# ---------------------------------------------------------------------------


class TestParseSectionsAndQuotes:
    def _make_spans(self, specs: list[tuple]) -> list[Span]:
        """Build Span list from (text, size, is_italic) tuples."""
        return [Span(text=t, size=s, is_italic=it, page=0) for t, s, it in specs]

    def test_basic_extraction(self):
        spans = self._make_spans([
            ("Morphology", 16.0, False),           # section header
            ("Synthesis text here.", 11.0, False),  # synthesis (skipped)
            ("Evidence", 14.0, False),              # evidence header
            ("(Smith et al., 2020)", 10.0, False),  # attribution
            ("Paper Title Here", 11.0, False),      # title (skipped)
            ('"A verbatim quote from the paper."', 9.0, True),  # quote
        ])
        sections, quotes = _parse_sections_and_quotes(spans)
        assert "Morphology" in sections
        assert "Smith et al., 2020" in quotes
        assert len(quotes["Smith et al., 2020"].quotes) == 1
        assert quotes["Smith et al., 2020"].quotes[0].text == (
            "A verbatim quote from the paper."
        )
        assert quotes["Smith et al., 2020"].quotes[0].section == "Morphology"

    def test_no_evidence_section(self):
        spans = self._make_spans([
            ("Introduction", 16.0, False),
            ("Some synthesis text.", 11.0, False),
        ])
        sections, quotes = _parse_sections_and_quotes(spans)
        assert "Introduction" in sections
        assert len(quotes) == 0

    def test_multiple_quotes_per_paper(self):
        spans = self._make_spans([
            ("Results", 16.0, False),
            ("Evidence", 14.0, False),
            ("(Jones et al., 2021)", 10.0, False),
            ("Title", 11.0, False),
            ('"First quote."', 9.0, True),
            ('"Second quote."', 9.0, True),
        ])
        _, quotes = _parse_sections_and_quotes(spans)
        assert len(quotes["Jones et al., 2021"].quotes) == 2

    def test_evidence_block_ends_at_next_section(self):
        spans = self._make_spans([
            ("Section A", 16.0, False),
            ("Evidence", 14.0, False),
            ("(Smith et al., 2020)", 10.0, False),
            ('"Quote A."', 9.0, True),
            ("Section B", 16.0, False),
            # Italic text outside evidence block should NOT be captured
            ('"Not a quote."', 9.0, True),
        ])
        _, quotes = _parse_sections_and_quotes(spans)
        assert len(quotes) == 1
        assert len(quotes["Smith et al., 2020"].quotes) == 1


# ---------------------------------------------------------------------------
# AstaReportExtraction dataclass
# ---------------------------------------------------------------------------


class TestAstaReportExtraction:
    def test_to_dict(self):
        result = AstaReportExtraction(
            sections=["Intro"],
            extracted_quotes={"Smith et al., 2020": AuthorQuotes(
                author_key="Smith et al., 2020",
                quotes=[ExtractedQuote(text="hello", section="Intro")],
            )},
            reference_list=[ReferenceEntry(author_key="Smith et al., 2020", title="T", year=2020)],
            corpus_ids=["123"],
            total_quotes=1,
            total_papers=1,
        )
        d = result.to_dict()
        assert d["total_quotes"] == 1
        assert d["corpus_ids"] == ["123"]
        assert len(d["extracted_quotes"]) == 1

    def test_write_outputs(self, tmp_path):
        result = AstaReportExtraction(
            sections=["Intro"],
            extracted_quotes={"Smith et al., 2020": AuthorQuotes(
                author_key="Smith et al., 2020",
                quotes=[ExtractedQuote(text="hello", section="Intro")],
            )},
            reference_list=[ReferenceEntry(author_key="Smith et al., 2020", title="T", year=2020)],
            corpus_ids=["123"],
            total_quotes=1,
            total_papers=1,
        )
        result.write_outputs(tmp_path)
        assert (tmp_path / "extracted_quotes.json").exists()
        assert (tmp_path / "reference_list.json").exists()
        assert (tmp_path / "pdf_corpus_ids.json").exists()

        eq = json.loads((tmp_path / "extracted_quotes.json").read_text())
        assert "Smith et al., 2020" in eq
        assert len(eq["Smith et al., 2020"]["quotes"]) == 1


# ---------------------------------------------------------------------------
# Integration test against real PDF (if available)
# ---------------------------------------------------------------------------


OLM_PDF = "inputs/deepsearch/OLM_Neurons_asta_report.pdf"


@pytest.mark.integration
def test_olm_pdf_extraction():
    """Full extraction against the OLM neurons ASTA report."""
    from pathlib import Path

    from evidencell.extract_asta_report import extract_asta_report

    if not Path(OLM_PDF).exists():
        pytest.skip("OLM PDF not available")

    result = extract_asta_report(OLM_PDF)

    # Baseline expectations from manual verification
    assert result.total_papers == 35
    assert result.total_quotes >= 130  # 134 raw, may vary slightly
    assert len(result.corpus_ids) == 35
    assert len(result.reference_list) >= 30

    # Content-hash dedup should yield ~87 unique quotes
    seen: set[str] = set()
    for aq in result.extracted_quotes.values():
        for q in aq.quotes:
            normalized = " ".join(q.text.lower().split())
            h = hashlib.sha256(normalized.encode()).hexdigest()[:8]
            seen.add(f"{aq.author_key}_{h}")
    assert len(seen) >= 85  # ~87 expected
