"""Tests for src/evidencell/parse_asta_report.py"""

import json
import sys

import pytest

from evidencell.parse_asta_report import (
    build_resolution_report,
    extract_cl_seeds,
    resolve_references,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

RESOLUTION_MAP_FULL = {
    "Smith 2020": {
        "pmid": "32000001",
        "doi": "10.1234/abc",
        "corpus_id": "11111111",
        "resolution_confidence": "HIGH",
        "title_fragment": "OLM interneuron properties",
        "year": 2020,
        "quote_count": 3,
    },
    "Jones 2018": {
        "doi": "10.5678/xyz",
        "corpus_id": "22222222",
        "resolution_confidence": "MODERATE",
        "title_fragment": "Hippocampal circuits",
        "year": 2018,
        "quote_count": 1,
    },
    "Brown 2015": {
        "corpus_id": "33333333",
        "resolution_confidence": "LOW",
        "title_fragment": "SST interneurons",
        "year": 2015,
        "quote_count": 2,
    },
    "Ghost 1999": {
        "resolution_confidence": "UNRESOLVED",
        "title_fragment": "Obscure paper",
        "year": 1999,
        "quote_count": 1,
    },
}

CL_MAPPINGS = {
    "olm_ca1": {
        "cl_term": "CL:0000000",
        "label": "oriens-lacunosum moleculare neuron",
        "mapping_type": "EXACT",
        "definition_references": ["PMID:10000001", "PMID:10000002"],
    },
    "bistratified_ca1": {
        "cl_term": "CL:0000001",
        "label": "bistratified cell",
        "mapping_type": "BROAD",
        "definition_references": ["PMID:10000002", "PMID:10000003"],
    },
    "no_refs_node": {
        "cl_term": None,
        "resolution_confidence": "CANDIDATE",
        "definition_references": [],
    },
}


# ---------------------------------------------------------------------------
# resolve_references
# ---------------------------------------------------------------------------

class TestResolveReferences:
    def test_prefers_pmid(self):
        yaml_str = 'reference: "UNRESOLVED:Smith 2020"'
        result = resolve_references(yaml_str, RESOLUTION_MAP_FULL)
        assert 'reference: "PMID:32000001"' in result

    def test_falls_back_to_doi_when_no_pmid(self):
        yaml_str = 'reference: "UNRESOLVED:Jones 2018"'
        result = resolve_references(yaml_str, RESOLUTION_MAP_FULL)
        assert 'reference: "DOI:10.5678/xyz"' in result

    def test_falls_back_to_corpus_id(self):
        yaml_str = 'reference: "UNRESOLVED:Brown 2015"'
        result = resolve_references(yaml_str, RESOLUTION_MAP_FULL)
        assert 'reference: "CorpusId:33333333"' in result

    def test_leaves_unresolved_unchanged(self):
        yaml_str = 'reference: "UNRESOLVED:Ghost 1999"'
        result = resolve_references(yaml_str, RESOLUTION_MAP_FULL)
        assert "UNRESOLVED:Ghost 1999" in result

    def test_unknown_key_left_unchanged(self):
        yaml_str = 'reference: "UNRESOLVED:Nobody 2099"'
        result = resolve_references(yaml_str, RESOLUTION_MAP_FULL)
        assert "UNRESOLVED:Nobody 2099" in result

    def test_multiple_tokens_in_one_string(self):
        yaml_str = (
            'ref_a: "UNRESOLVED:Smith 2020"\n'
            'ref_b: "UNRESOLVED:Jones 2018"\n'
        )
        result = resolve_references(yaml_str, RESOLUTION_MAP_FULL)
        assert "PMID:32000001" in result
        assert "DOI:10.5678/xyz" in result

    def test_no_tokens_unchanged(self):
        yaml_str = 'reference: "PMID:99999999"'
        result = resolve_references(yaml_str, RESOLUTION_MAP_FULL)
        assert result == yaml_str

    def test_empty_resolution_map(self):
        yaml_str = 'reference: "UNRESOLVED:Smith 2020"'
        result = resolve_references(yaml_str, {})
        assert "UNRESOLVED:Smith 2020" in result


# ---------------------------------------------------------------------------
# build_resolution_report
# ---------------------------------------------------------------------------

class TestBuildResolutionReport:
    def test_contains_summary_counts(self):
        report = build_resolution_report(RESOLUTION_MAP_FULL)
        assert "4" in report   # total
        assert "3" in report   # resolved (HIGH + MODERATE + LOW)
        assert "1" in report   # unresolved count somewhere

    def test_lists_unresolved_keys(self):
        report = build_resolution_report(RESOLUTION_MAP_FULL)
        assert "Ghost 1999" in report

    def test_all_resolved(self):
        resolved_map = {
            "Smith 2020": {"pmid": "111", "resolution_confidence": "HIGH"},
            "Jones 2018": {"pmid": "222", "resolution_confidence": "MODERATE"},
        }
        report = build_resolution_report(resolved_map)
        assert "Unresolved references" not in report
        assert "100%" in report

    def test_empty_map(self):
        report = build_resolution_report({})
        assert "0" in report

    def test_unknown_confidence_treated_as_unresolved(self):
        m = {"X 2000": {"resolution_confidence": "MYSTERY"}}
        report = build_resolution_report(m)
        assert "X 2000" in report

    def test_markdown_table_present(self):
        report = build_resolution_report(RESOLUTION_MAP_FULL)
        assert "| HIGH |" in report
        assert "| UNRESOLVED |" in report


# ---------------------------------------------------------------------------
# extract_cl_seeds
# ---------------------------------------------------------------------------

class TestExtractClSeeds:
    def test_returns_deduplicated_refs(self):
        # PMID:10000002 appears in both olm_ca1 and bistratified_ca1
        seeds = extract_cl_seeds(CL_MAPPINGS)
        assert seeds.count("PMID:10000002") == 1

    def test_all_refs_present(self):
        seeds = extract_cl_seeds(CL_MAPPINGS)
        assert "PMID:10000001" in seeds
        assert "PMID:10000002" in seeds
        assert "PMID:10000003" in seeds

    def test_empty_refs_skipped(self):
        seeds = extract_cl_seeds(CL_MAPPINGS)
        # no_refs_node contributes nothing
        assert len(seeds) == 3

    def test_empty_mappings(self):
        assert extract_cl_seeds({}) == []

    def test_node_with_no_definition_references_key(self):
        mappings = {"node_a": {"cl_term": "CL:0000001"}}
        assert extract_cl_seeds(mappings) == []


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

class TestCLI:
    def test_resolve_command(self, tmp_path):
        yaml_file = tmp_path / "proposed.yaml"
        yaml_file.write_text('reference: "UNRESOLVED:Smith 2020"\n')
        map_file = tmp_path / "resolution_map.json"
        map_file.write_text(json.dumps({
            "Smith 2020": {"pmid": "32000001", "resolution_confidence": "HIGH"}
        }))

        from evidencell import parse_asta_report
        sys.argv = ["parse_asta_report", "resolve", str(yaml_file), str(map_file)]
        import io
        from contextlib import redirect_stdout
        buf = io.StringIO()
        with redirect_stdout(buf):
            parse_asta_report.main()
        assert "PMID:32000001" in buf.getvalue()

    def test_report_command(self, tmp_path):
        map_file = tmp_path / "resolution_map.json"
        map_file.write_text(json.dumps(RESOLUTION_MAP_FULL))

        from evidencell import parse_asta_report
        sys.argv = ["parse_asta_report", "report", str(map_file)]
        import io
        from contextlib import redirect_stdout
        buf = io.StringIO()
        with redirect_stdout(buf):
            parse_asta_report.main()
        assert "Resolution Report" in buf.getvalue()

    def test_cl_seeds_command(self, tmp_path):
        cl_file = tmp_path / "cl_mappings.json"
        cl_file.write_text(json.dumps(CL_MAPPINGS))

        from evidencell import parse_asta_report
        sys.argv = ["parse_asta_report", "cl-seeds", str(cl_file)]
        import io
        from contextlib import redirect_stdout
        buf = io.StringIO()
        with redirect_stdout(buf):
            parse_asta_report.main()
        result = json.loads(buf.getvalue())
        assert "PMID:10000001" in result

    def test_unknown_command_exits(self):
        from evidencell import parse_asta_report
        sys.argv = ["parse_asta_report", "bogus"]
        with pytest.raises(SystemExit) as exc:
            parse_asta_report.main()
        assert exc.value.code == 1

    def test_missing_file_exits(self, tmp_path):
        from evidencell import parse_asta_report
        sys.argv = [
            "parse_asta_report", "resolve",
            str(tmp_path / "nonexistent.yaml"),
            str(tmp_path / "nonexistent.json"),
        ]
        with pytest.raises(SystemExit) as exc:
            parse_asta_report.main()
        assert exc.value.code == 1
