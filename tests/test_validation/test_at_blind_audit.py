"""End-to-end test of the AT-blind audit framework against a synthetic
mini-corpus. Exercises preflight, ground-truth collection, per-case
execution, and outcome categorisation without touching the real KB.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import pytest
import yaml

from evidencell.validation import ATBlindAudit, AuditAssertion


@pytest.fixture
def synthetic_corpus(tmp_path, monkeypatch):
    """Build a minimal evidencell tree at tmp_path with:

      * one taxonomy ('MINI001') with 3 cluster nodes
      * an anat table + closure (one queried region, one sibling, one distant)
      * one classical-node graph with two AT-evidenced edges: one whose
        target is the queried region (should be `found`), one whose target
        is the distant region (should be `region_drop`)
    """
    import evidencell.paths as paths_mod
    import evidencell.validation.at_blind as atb_mod

    repo = tmp_path
    (repo / "kb" / "graphs" / "test_region").mkdir(parents=True)
    (repo / "kb" / "taxonomy" / "MINI001").mkdir(parents=True)

    # Patch repo_root + taxonomy_db_path in every module that imported
    # them by name (Python copies the reference at import time, so a
    # single `setattr(paths_mod, ...)` doesn't propagate).
    fake_repo_root = lambda: repo  # noqa: E731
    fake_db_path = lambda tid: repo / "kb" / "taxonomy" / tid / f"{tid}.db"  # noqa: E731
    monkeypatch.setattr(paths_mod, "repo_root", fake_repo_root)
    monkeypatch.setattr(paths_mod, "taxonomy_db_path", fake_db_path)
    monkeypatch.setattr(atb_mod, "repo_root", fake_repo_root)
    monkeypatch.setattr(atb_mod, "taxonomy_db_path", fake_db_path)

    # We build YAML first then the DB last so the DB's _meta timestamp
    # is strictly after every YAML mtime — the freshness preflight
    # compares the two and a same-second stamp can flip stale.
    _build_yaml_files(repo)

    # ── Build the SQLite DB by hand ──────────────────────────────────
    db_path = repo / "kb" / "taxonomy" / "MINI001" / "MINI001.db"
    con = sqlite3.connect(db_path)
    con.executescript("""
    CREATE TABLE nodes (
      node_id TEXT PRIMARY KEY, short_form TEXT NOT NULL, label TEXT NOT NULL,
      taxonomy_id TEXT NOT NULL, taxonomy_level TEXT NOT NULL, taxonomy_rank INTEGER,
      parent_id TEXT, cl_id TEXT, cl_label TEXT, cell_ontology_term TEXT, nt_type TEXT,
      defining_markers_scoped TEXT, defining_markers TEXT, tf_markers TEXT,
      merfish_markers TEXT, np_markers TEXT, neighborhood TEXT, circadian_ratio REAL,
      rationale TEXT, rationale_dois TEXT, male_female_ratio REAL, n_cells INTEGER
    );
    CREATE TABLE anat (
      node_id TEXT, anat_id TEXT, anat_label TEXT, cell_count INTEGER, cell_ratio REAL
    );
    CREATE TABLE anat_terms (
      anat_id TEXT PRIMARY KEY, label TEXT NOT NULL, uberon_id TEXT
    );
    CREATE TABLE anat_hierarchy (
      parent_id TEXT NOT NULL, child_id TEXT NOT NULL,
      PRIMARY KEY (parent_id, child_id)
    );
    CREATE TABLE anat_closure (
      ancestor_id TEXT NOT NULL, descendant_id TEXT NOT NULL, depth INTEGER NOT NULL,
      PRIMARY KEY (ancestor_id, descendant_id)
    );
    CREATE TABLE _meta (key TEXT PRIMARY KEY, value TEXT);
    """)
    con.executemany(
        "INSERT INTO nodes(node_id, short_form, label, taxonomy_id, "
        "taxonomy_level, taxonomy_rank, nt_type) VALUES (?, ?, ?, ?, ?, ?, ?)",
        [
            ("CLUS_TARGET", "CLUS_TARGET", "Target cluster", "MINI001", "cluster", 0, "GABA"),
            ("CLUS_SIBLING", "CLUS_SIBLING", "Sibling cluster", "MINI001", "cluster", 0, "GABA"),
            ("CLUS_DISTANT", "CLUS_DISTANT", "Distant cluster", "MINI001", "cluster", 0, "GABA"),
        ],
    )
    # Anat: TARGET in MBA:QUERY (the queried region exactly);
    # SIBLING in MBA:SIB (sibling under same parent — would be rescued by
    # expansion); DISTANT in MBA:FAR (parent of FAR is MBA:ROOT, no
    # overlap with the queried branch).
    con.executemany(
        "INSERT INTO anat VALUES (?, ?, ?, ?, ?)",
        [
            ("CLUS_TARGET", "MBA:QUERY", "Queried region", 100, 1.0),
            ("CLUS_SIBLING", "MBA:SIB", "Sibling region", 100, 1.0),
            ("CLUS_DISTANT", "MBA:FAR", "Far away", 100, 1.0),
        ],
    )
    con.executemany(
        "INSERT INTO anat_terms VALUES (?, ?, ?)",
        [
            ("MBA:QUERY", "Queried region", "UBERON:0000999"),
            ("MBA:SIB", "Sibling region", None),
            ("MBA:FAR", "Far away", None),
            ("MBA:PARENT", "Common parent of query and sibling", None),
            ("MBA:ROOT", "Root", None),
        ],
    )
    con.executemany(
        "INSERT INTO anat_hierarchy VALUES (?, ?)",
        [
            ("MBA:PARENT", "MBA:QUERY"),
            ("MBA:PARENT", "MBA:SIB"),
            ("MBA:ROOT", "MBA:PARENT"),
            ("MBA:ROOT", "MBA:FAR"),
        ],
    )
    con.executemany(
        "INSERT INTO anat_closure VALUES (?, ?, ?)",
        [
            ("MBA:QUERY", "MBA:QUERY", 0),
            ("MBA:SIB", "MBA:SIB", 0),
            ("MBA:FAR", "MBA:FAR", 0),
            ("MBA:PARENT", "MBA:PARENT", 0),
            ("MBA:PARENT", "MBA:QUERY", 1),
            ("MBA:PARENT", "MBA:SIB", 1),
            ("MBA:ROOT", "MBA:ROOT", 0),
            ("MBA:ROOT", "MBA:PARENT", 1),
            ("MBA:ROOT", "MBA:FAR", 1),
            ("MBA:ROOT", "MBA:QUERY", 2),
            ("MBA:ROOT", "MBA:SIB", 2),
        ],
    )
    # Pin a fresh _meta entry so taxonomy_db_freshness doesn't fail.
    from datetime import datetime, timezone
    from evidencell.taxonomy_db import _SCHEMA_HASH
    con.execute(
        "INSERT INTO _meta VALUES ('taxonomy_built_at', ?)",
        (datetime.now(tz=timezone.utc).isoformat(),),
    )
    con.execute("INSERT INTO _meta VALUES ('schema_hash', ?)", (_SCHEMA_HASH,))
    con.commit()
    con.close()

    return repo


def _build_yaml_files(repo: Path) -> None:
    """Materialise taxonomy_meta + cluster.yaml + a kb/graphs/ file with
    classical node and two AT-evidenced edges. Factored out of the
    fixture so we can write YAML BEFORE the SQLite DB (so the DB's
    `_meta.taxonomy_built_at` is later than every YAML mtime — the
    freshness preflight compares the two)."""
    meta = {
        "taxonomy_id": "MINI001",
        "taxonomy_name": "Synthetic mini taxonomy",
        "species_id": "NCBITaxon:10090",
        "species_label": "Mus musculus",
        "ingest_date": "2026-05-11",
        "level_counts": {"cluster": 3},
    }
    (repo / "kb" / "taxonomy" / "MINI001" / "taxonomy_meta.yaml").write_text(
        yaml.safe_dump(meta)
    )
    cluster_yaml = {
        "taxonomy_id": "MINI001",
        "taxonomy_level": "CLUSTER",
        "taxonomy_rank": 0,
        "nodes": [
            {"id": "CLUS_TARGET", "name": "Target cluster",
             "cell_set_accession": "CLUS_TARGET",
             "taxonomy_id": "MINI001", "taxonomy_level": "CLUSTER",
             "definition_basis": "ATLAS_TRANSCRIPTOMIC", "is_terminal": True},
            {"id": "CLUS_SIBLING", "name": "Sibling cluster",
             "cell_set_accession": "CLUS_SIBLING",
             "taxonomy_id": "MINI001", "taxonomy_level": "CLUSTER",
             "definition_basis": "ATLAS_TRANSCRIPTOMIC", "is_terminal": True},
            {"id": "CLUS_DISTANT", "name": "Distant cluster",
             "cell_set_accession": "CLUS_DISTANT",
             "taxonomy_id": "MINI001", "taxonomy_level": "CLUSTER",
             "definition_basis": "ATLAS_TRANSCRIPTOMIC", "is_terminal": True},
        ],
    }
    (repo / "kb" / "taxonomy" / "MINI001" / "cluster.yaml").write_text(
        yaml.safe_dump(cluster_yaml)
    )

    classical_node = {
        "id": "lit_test",
        "name": "Test lit type",
        "definition_basis": "ARTIFICIAL",
        "defining_markers": [{"symbol": "Sst"}],
        "nt_type": {"name_in_source": "GABAergic"},
        "anatomical_location": [
            {"id": "UBERON:0000999",
             "label": "Queried region",
             "name_in_source": "Queried region",
             "compartment": "SOMA"}
        ],
    }
    target_stub_close = {
        "id": "wmb_target", "name": "Target",
        "definition_basis": "ATLAS_TRANSCRIPTOMIC",
        "taxonomy_id": "MINI001",
        "cell_set_accession": "CLUS_TARGET",
        "taxonomy_level": "cluster",
    }
    target_stub_far = {
        "id": "wmb_distant", "name": "Distant target",
        "definition_basis": "ATLAS_TRANSCRIPTOMIC",
        "taxonomy_id": "MINI001",
        "cell_set_accession": "CLUS_DISTANT",
        "taxonomy_level": "cluster",
    }
    edges = [
        {"id": "edge_lit_to_target", "type_a": "lit_test", "type_b": "wmb_target",
         "relationship": "EQUIVALENT",
         "evidence": [{"evidence_type": "ANNOTATION_TRANSFER",
                       "best_f1_score": 0.9}]},
        {"id": "edge_lit_to_distant", "type_a": "lit_test", "type_b": "wmb_distant",
         "relationship": "PARTIAL_OVERLAP",
         "evidence": [{"evidence_type": "ANNOTATION_TRANSFER",
                       "best_f1_score": 0.5}]},
    ]
    (repo / "kb" / "graphs" / "test_region" / "test.yaml").write_text(
        yaml.safe_dump({
            "nodes": [classical_node, target_stub_close, target_stub_far],
            "edges": edges,
        })
    )
    # Belt-and-braces: backdate YAML mtimes by 2 seconds so the DB build
    # timestamp is unambiguously later.
    import os
    import time
    backdate = time.time() - 2
    for p in (repo / "kb").rglob("*.yaml"):
        os.utime(p, (backdate, backdate))


def test_audit_preflight_passes_on_well_formed_corpus(synthetic_corpus):
    """The synthetic corpus is constructed so all preflight invariants pass."""
    audit = ATBlindAudit(taxonomy_id="MINI001", top_k=10, f1_floor=0.0)
    run = audit.run()
    assert run.summary_stats["n_cases"] == 2
    assert all(pa["status"] == "pass" for pa in run.preflight_assertions)


def test_audit_finds_target_in_topk(synthetic_corpus):
    """The close-region AT target (CLUS_TARGET) should appear in top-K."""
    audit = ATBlindAudit(taxonomy_id="MINI001", top_k=10, f1_floor=0.0)
    run = audit.run()
    outcomes = {o.test_id: o for o in run.outcomes}
    target_outcome = outcomes["lit_test|CLUS_TARGET"]
    assert target_outcome.passed
    assert target_outcome.reason == "found"
    assert target_outcome.actual["in_results"] is True
    # Raw evidence is preserved on the outcome — exactly the discipline
    # the framework is meant to enforce.
    assert "candidate_detail" in target_outcome.actual
    assert "score" in target_outcome.actual["candidate_detail"]


def test_audit_region_drop_for_distant_target(synthetic_corpus):
    """The distant-region target (CLUS_DISTANT) should be dropped because
    its anat doesn't overlap the queried region's closure even after
    one-level parent expansion."""
    audit = ATBlindAudit(taxonomy_id="MINI001", top_k=10, f1_floor=0.0)
    run = audit.run()
    outcomes = {o.test_id: o for o in run.outcomes}
    distant_outcome = outcomes["lit_test|CLUS_DISTANT"]
    assert not distant_outcome.passed
    assert distant_outcome.reason == "region_drop"
    assert distant_outcome.actual["in_results"] is False


def test_audit_artifact_written_to_runs_dir(synthetic_corpus):
    """Run artifact lands in the runs directory and is round-trippable JSON."""
    audit = ATBlindAudit(taxonomy_id="MINI001", top_k=10, f1_floor=0.0)
    audit.run()
    latest = audit.runs_dir / "latest.json"
    assert latest.exists()
    loaded = json.loads(latest.read_text())
    assert loaded["audit_id"] == "at_blind"
    assert loaded["summary_stats"]["n_cases"] == 2
    # Each outcome should round-trip the raw expected/actual blocks.
    for o in loaded["outcomes"]:
        assert "expected" in o and "actual" in o


def test_audit_preflight_fails_on_missing_db(tmp_path, monkeypatch):
    """If the taxonomy DB doesn't exist, preflight aborts with a specific error."""
    import evidencell.paths as paths_mod
    monkeypatch.setattr(paths_mod, "repo_root", lambda: tmp_path)
    monkeypatch.setattr(
        paths_mod,
        "taxonomy_db_path",
        lambda tid: tmp_path / "no_such_db.db",
    )
    audit = ATBlindAudit(taxonomy_id="MISSING", top_k=10, f1_floor=0.0)
    with pytest.raises(AuditAssertion, match="Taxonomy DB not found"):
        audit.run()


def test_audit_preflight_catches_uberon_resolution_gap(synthetic_corpus):
    """If a classical node has a UBERON ID that resolves to no MBA term
    (neither xref nor name fallback), preflight aborts. This is the
    OLM-style silent skip the framework is meant to surface."""

    repo = synthetic_corpus
    # Overwrite the graph with a UBERON ID that has no xref and no name match.
    graph_path = repo / "kb" / "graphs" / "test_region" / "test.yaml"
    doc = yaml.safe_load(graph_path.read_text())
    for node in doc["nodes"]:
        if node["id"] == "lit_test":
            node["anatomical_location"] = [{
                "id": "UBERON:UNREACHABLE",
                "label": "Nowhere",
                "name_in_source": "Nowhere",
                "compartment": "SOMA",
            }]
    graph_path.write_text(yaml.safe_dump(doc))

    audit = ATBlindAudit(taxonomy_id="MINI001", top_k=10, f1_floor=0.0)
    with pytest.raises(AuditAssertion, match="UBERON IDs"):
        audit.run()


def test_audit_force_preflight_records_skip(synthetic_corpus):
    """With --force-preflight, a failed invariant becomes a recorded skip
    rather than aborting the audit. The skip is visible in the artifact."""
    repo = synthetic_corpus
    graph_path = repo / "kb" / "graphs" / "test_region" / "test.yaml"
    doc = yaml.safe_load(graph_path.read_text())
    for node in doc["nodes"]:
        if node["id"] == "lit_test":
            node["anatomical_location"] = [{
                "id": "UBERON:UNREACHABLE", "label": "Nowhere",
                "name_in_source": "Nowhere", "compartment": "SOMA",
            }]
    graph_path.write_text(yaml.safe_dump(doc))

    audit = ATBlindAudit(
        taxonomy_id="MINI001", top_k=10, f1_floor=0.0,
        force_preflight=True,
    )
    run = audit.run()
    skipped = [
        pa for pa in run.preflight_assertions if pa["status"] == "skipped"
    ]
    assert any("UBERON" in pa.get("note", "") for pa in skipped), (
        "Forced preflight skip must record the failed invariant for trace"
    )
