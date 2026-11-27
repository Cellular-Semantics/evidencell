"""Atlas marker sets (#274): parse, classify, attach, score checks.

Tier: fast (in-process rows; no KG, no network).
"""

from __future__ import annotations

import pytest

from evidencell.marker_sets import (
    F_BETA,
    NS_FOREST_DOI,
    YAO_DOI,
    MarkerSetError,
    NodeInfo,
    build_marker_sets,
    check_counts,
    classify,
    f_beta,
    label_gene_names,
    pair_genes,
)

SUBC = "WMB:CS20230722_SUBC_001"
SUPT = "WMB:CS20230722_SUPT_0001"
CLUS = "WMB:CS20230722_CLUS_0001"
NODES = {
    "WMB:CS20230722_CLAS_01": NodeInfo("class", None),
    SUBC: NodeInfo("subclass", "WMB:CS20230722_CLAS_01"),
    SUPT: NodeInfo("supertype", SUBC),
    CLUS: NodeInfo("cluster", SUPT),
}
GENES = {
    "NCBIGene:12350": {"label": "Car3", "taxon": "NCBITaxon:10090"},
    "NCBIGene:20204": {"label": "Satb2", "taxon": "NCBITaxon:10090"},
    "NCBIGene:14160": {"label": "Lgr5", "taxon": "NCBITaxon:10090"},
}


def _gene(curie: str, name: str) -> dict:
    return {"curie": curie, "label": f"{name} (Mmus)"}


def _row(**kw) -> dict:
    """Cluster 0001's within-subclass set, as the KG export returns it."""
    row = {
        "via_class": "PCL:0112381",
        "exemplars": [CLUS],
        "finest": [CLUS],
        "ancestors_ok": True,
        "set_id": "PCL:0143601",
        "set_label": "Lgr5 (Yao - within subclass).",
        "xref": [YAO_DOI],
        "algorithm": None,
        "precision": [0.7368421],
        "recall": ["0.28"],
        "f_beta": [0.5555556],
        "genes": [_gene("NCBIGene:14160", "Lgr5")],
    }
    row.update(kw)
    return row


def _build(rows, records=GENES, known=lambda c: set()):
    return build_marker_sets(rows, NODES, lambda ids: {i: records[i] for i in ids if i in records}, known)


# ── classify ──────────────────────────────────────────────────────────────────


@pytest.mark.parametrize(
    ("label", "xref", "algo", "want"),
    [
        ("Car3,Satb2,Lgr5 (Yao).", [YAO_DOI], None, ("AUTHOR_COMBO", "GLOBAL", "DEFINING")),
        ("Lgr5 (Yao - within subclass).", [YAO_DOI], None,
         ("AUTHOR_COMBO", "WITHIN_PARENT", "DEFINING_SCOPED")),
        ("Inhba, Tfap2b (NSforest).", [NS_FOREST_DOI], ["NSforest"],
         ("NS_FOREST", "GLOBAL", "DEFINING")),
        ("Sst, Tbr1 (CAS evidence).", None, None, None),
    ],
)
def test_classify(label, xref, algo, want):
    assert classify(label, xref, algo, "X:1") == want


def test_classify_label_and_doi_must_agree():
    with pytest.raises(MarkerSetError, match="expected"):
        classify("Lgr5 (Yao).", [NS_FOREST_DOI], None, "X:1")


def test_classify_ns_forest_needs_algorithm():
    with pytest.raises(MarkerSetError, match="disagree"):
        classify("Inhba (NSforest).", [NS_FOREST_DOI], None, "X:1")


def test_classify_unknown_label_citing_a_known_doi_fails():
    with pytest.raises(MarkerSetError, match="matches no known set kind"):
        classify("Lgr5 (Yao, v2).", [YAO_DOI], None, "X:1")


# ── label names and gene pairing ─────────────────────────────────────────────


def test_label_gene_names_strips_uniqueness_counter():
    assert label_gene_names("Fev, Gata2 2 (NSforest).") == ["Fev", "Gata2"]
    assert label_gene_names("Th 7 (Yao - within subclass).") == ["Th"]
    assert label_gene_names("Car3,Satb2,Lgr5 (Yao).") == ["Car3", "Satb2", "Lgr5"]


def test_pair_genes_keeps_label_order():
    genes = [_gene("NCBIGene:14160", "Lgr5"), _gene("NCBIGene:12350", "Car3"),
             _gene("NCBIGene:20204", "Satb2")]
    assert pair_genes("X:1", ["Car3", "Satb2", "Lgr5"], genes, lambda c: set()) == [
        ("Car3", "NCBIGene:12350"), ("Satb2", "NCBIGene:20204"), ("Lgr5", "NCBIGene:14160"),
    ]


def test_pair_genes_uses_taxonomy_names_then_elimination():
    """KG labels can be stale symbols (Lrrc7 is labelled B230334C09Rik):
    pair by the taxonomy's names, then the last one by elimination."""
    genes = [_gene("NCBIGene:242274", "B230334C09Rik"), _gene("NCBIGene:13179", "Dcn"),
             _gene("NCBIGene:1", "Gm38353")]
    names = {"NCBIGene:242274": {"Lrrc7"}}
    assert pair_genes("X:1", ["Dcn", "Lrrc7", "Gm20754"], genes, lambda c: names.get(c, set())) == [
        ("Dcn", "NCBIGene:13179"), ("Lrrc7", "NCBIGene:242274"), ("Gm20754", "NCBIGene:1"),
    ]


def test_pair_genes_refuses_to_guess():
    genes = [_gene("NCBIGene:1", "Aaa"), _gene("NCBIGene:2", "Bbb")]
    with pytest.raises(MarkerSetError, match="cannot pair"):
        pair_genes("X:1", ["Xxx", "Yyy"], genes, lambda c: set())


def test_pair_genes_count_mismatch():
    with pytest.raises(MarkerSetError, match="label names"):
        pair_genes("X:1", ["Aaa", "Bbb"], [_gene("NCBIGene:1", "Aaa")], lambda c: set())


# ── build_marker_sets ─────────────────────────────────────────────────────────


def test_within_subclass_set_on_cluster():
    sets, report = _build([_row()])
    (ms,) = sets[CLUS]
    assert ms == {
        "id": "PCL:0143601",
        "genes": [{"name_in_source": "Lgr5", "ncbi_gene_id": "NCBIGene:14160", "symbol": "Lgr5"}],
        "selection_method": "AUTHOR_COMBO",
        "context": "WITHIN_PARENT",
        "context_node": SUBC,
        "role": "DEFINING_SCOPED",
        "via_class": "PCL:0112381",
        "performance": [
            {"metric": "F_BETA", "value": 0.5555556, "beta": F_BETA},
            {"metric": "PRECISION", "value": 0.7368421},
            {"metric": "RECALL", "value": 0.28},
        ],
        "source": {"ref": YAO_DOI, "method": "marker gene combination (Yao et al. 2023)"},
    }
    assert report.counts == {("cluster", "AUTHOR_COMBO", "WITHIN_PARENT"): 1}
    assert report.scored == 1


def test_global_set_has_no_context_node():
    row = _row(set_id="PCL:0122881", set_label="Car3,Satb2,Lgr5 (Yao).",
               precision=[0.0], recall=["0.0"], f_beta=[0.0],
               genes=[_gene("NCBIGene:12350", "Car3"), _gene("NCBIGene:20204", "Satb2"),
                      _gene("NCBIGene:14160", "Lgr5")])
    (ms,) = _build([row])[0][CLUS]
    assert ms["context"] == "GLOBAL" and "context_node" not in ms
    assert [g["name_in_source"] for g in ms["genes"]] == ["Car3", "Satb2", "Lgr5"]


def test_unscored_set_has_no_performance():
    (ms,) = _build([_row(precision=None, recall=None, f_beta=None)])[0][CLUS]
    assert "performance" not in ms


def test_partial_scores_fail():
    with pytest.raises(MarkerSetError, match="has only"):
        _build([_row(recall=None)])


def test_f_beta_must_be_beta_half_of_precision_and_recall():
    """Pins beta: an F1 value (or any other beta) is refused."""
    f1 = f_beta(0.7368421, 0.28, beta=1.0)
    with pytest.raises(MarkerSetError, match="is not F\\(beta=0.5\\)"):
        _build([_row(f_beta=[f1])])


def test_cl_class_resolves_to_most_specific_exemplar():
    sets, report = _build([_row(exemplars=[CLUS, SUPT, SUBC])])
    assert list(sets) == [CLUS]
    assert report.multi_exemplar_classes == 1


def test_no_single_most_specific_exemplar_fails():
    with pytest.raises(MarkerSetError, match="no single most specific"):
        _build([_row(finest=[CLUS, SUPT])])
    with pytest.raises(MarkerSetError, match="no single most specific"):
        _build([_row(ancestors_ok=False)])


def test_exemplar_outside_taxonomy_fails():
    with pytest.raises(MarkerSetError, match="not a taxonomy node"):
        _build([_row(finest=["WMB:CS20230722_CLUS_9999"])])


def test_within_parent_needs_a_subclass_ancestor():
    with pytest.raises(MarkerSetError, match="no subclass ancestor"):
        _build([_row(finest=[SUBC], exemplars=[SUBC])])


def test_duplicate_set_fails():
    with pytest.raises(MarkerSetError, match="more than one row"):
        _build([_row(), _row()])


def test_unscored_other_kinds_are_skipped_and_counted():
    row = _row(set_id="CLM:5024424", set_label="Klk6 (CAS evidence).", xref=None,
               precision=None, recall=None, f_beta=None)
    sets, report = _build([row])
    assert sets == {}
    assert report.skipped_unscored == {"(CAS evidence).": 1}


def test_gene_without_current_id_keeps_name_only():
    records = {"NCBIGene:14160": {"missing": True, "replaced_by": None}}
    sets, report = _build([_row()], records=records)
    assert sets[CLUS][0]["genes"] == [{"name_in_source": "Lgr5"}]
    assert report.genes_without_id == ["PCL:0143601: Lgr5 (NCBIGene:14160: not a current NCBI gene)"]


def test_ensembl_gene_keeps_name_only():
    row = _row(genes=[{"curie": "ensembl:ENSMUSG00000086804", "label": "Lgr5 (Mmus)"}])
    sets, report = _build([row])
    assert sets[CLUS][0]["genes"] == [{"name_in_source": "Lgr5"}]
    assert "not an NCBI gene ID" in report.genes_without_id[0]


# ── check_counts ─────────────────────────────────────────────────────────────


def test_check_counts():
    _, report = _build([_row()])
    assert check_counts(report, {"cluster": {"AUTHOR_COMBO/WITHIN_PARENT": 1}}) == []
    assert check_counts(report, {"cluster": {"AUTHOR_COMBO/WITHIN_PARENT": 2}}) == [
        "cluster AUTHOR_COMBO/WITHIN_PARENT: built 1, expected 2"
    ]
    assert check_counts(report, None) == ["no expected_counts declared for marker sets"]
