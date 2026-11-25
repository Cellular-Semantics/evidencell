"""#244 marker migration: line edits keep formatting and give the expected shape."""

from __future__ import annotations

import yaml

from evidencell.migrate_marker_names import _expected, migrate_text

LABELS = {"NCBIGene:52897": "Rbfox3", "NCBIGene:6750": "SST"}

GRAPH = """\
nodes:
  - id: n1
    # a comment that must survive
    defining_markers:
      - symbol: NeuN
        ncbi_gene_id: "NCBIGene:52897"
        sources:
          - ref: PMID:1
            marker_type: PROTEIN
      - symbol: PSA-NCAM
      - {symbol: SST, ncbi_gene_id: "NCBIGene:6750"}
edges:
  - evidence:
      - defining_markers:
          - symbol: Prrxl1
"""


def test_block_flow_and_edge_markers():
    out = migrate_text(GRAPH, LABELS)
    assert "# a comment that must survive" in out
    assert "      - name_in_source: NeuN\n        symbol: Rbfox3\n" in out
    assert "      - name_in_source: PSA-NCAM\n" in out
    assert '{name_in_source: SST, symbol: SST, ncbi_gene_id: "NCBIGene:6750"}' in out
    assert "- name_in_source: Prrxl1" in out
    assert yaml.safe_load(out) == _expected(yaml.safe_load(GRAPH), LABELS)


def test_already_migrated_is_unchanged():
    once = migrate_text(GRAPH, LABELS)
    assert migrate_text(once, LABELS) == once


def test_taxonomy_markers_rename_only():
    text = "nodes:\n- id: a\n  markers:\n  - symbol: Ikzf1\n    category: DEFINING\n"
    assert migrate_text(text, {}) == text.replace("symbol:", "name_in_source:")
