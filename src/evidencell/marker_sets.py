"""Atlas marker sets: gene combinations with method, context and scores (#274).

Source: the marker-set export of brain_cell_KG
(``inputs/taxonomies/{taxonomy_id}_marker_sets.cypher`` → ``…_marker_sets.json``,
declared as ``marker_sets.file`` in ``inputs/taxonomies/{taxonomy_id}_meta.yaml``).
One row per (marker set, class it hangs off); see the .cypher header for the
graph shape.

:func:`build_marker_sets` turns the rows into ``MarkerSet`` dicts keyed by
taxonomy node CURIE. It fails loudly (:class:`MarkerSetError`) rather than
guess:

- **Method / context** come from the set label's suffix **and** its DOI; they
  must agree. ``(Yao).`` → AUTHOR_COMBO / GLOBAL; ``(Yao - within subclass).``
  → AUTHOR_COMBO / WITHIN_PARENT (the node's subclass); ``(NSforest).`` with
  ``algorithm: NSforest`` → NS_FOREST / GLOBAL. Unscored sets with other
  labels (``(CAS evidence).``) are skipped and counted.
- **Node**: the class's single most specific exemplar cell set. A CL class can
  have 2–3 exemplar targets (the most specific one plus entailed
  ``subcluster_of`` ancestors); anything else is an error.
- **Scores**: KG values are single-element lists, recall a string. The stored
  F-beta must equal F(beta=0.5) of the set's own precision and recall — the
  check that pins beta.
- **Genes** are paired with the label's names (the source's wording,
  ``name_in_source``) by name, then by elimination. A gene named by
  ``NCBIGene:`` ID gets ``ncbi_gene_id`` + ``symbol`` (its official symbol,
  from the same lookup the pre-edit hook uses); a gene whose ID doesn't
  resolve to a current NCBI gene keeps ``name_in_source`` only and is counted.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

YAO_DOI = "https://doi.org/10.1038/s41586-023-06812-z"
NS_FOREST_DOI = "https://doi.org/10.1101/2020.09.23.308932"

# NS-Forest's F-beta. Checked against every set's own precision and recall.
F_BETA = 0.5
_F_TOLERANCE = 1e-3

# label suffix → (selection_method, context, role, expected DOI)
_KINDS: dict[str, tuple[str, str, str, str]] = {
    "(Yao).": ("AUTHOR_COMBO", "GLOBAL", "DEFINING", YAO_DOI),
    "(Yao - within subclass).": ("AUTHOR_COMBO", "WITHIN_PARENT", "DEFINING_SCOPED", YAO_DOI),
    "(NSforest).": ("NS_FOREST", "GLOBAL", "DEFINING", NS_FOREST_DOI),
}
_SOURCE_DOI = {"AUTHOR_COMBO": YAO_DOI, "NS_FOREST": NS_FOREST_DOI}
_SOURCE_METHOD = {
    "AUTHOR_COMBO": "marker gene combination (Yao et al. 2023)",
    "NS_FOREST": "NS-Forest",
}
# The level whose other cells a WITHIN_PARENT ("within subclass") set is
# chosen against.
_WITHIN_PARENT_LEVEL = "subclass"

# A gene label in the KG: "Car3 (Mmus)".
_GENE_LABEL_RE = re.compile(r"^(.*?) \([A-Z][a-z]+\)$")
# Set labels repeat a name with a counter to keep labels unique: "Th 7 (Yao …)".
_UNIQUENESS_SUFFIX_RE = re.compile(r" \d+$")


class MarkerSetError(ValueError):
    """The marker-set export breaks an ingest rule; nothing is written."""


@dataclass
class MarkerSetReport:
    """What the build did, for the ingest summary and the count check."""

    rows: int = 0
    attached: int = 0
    scored: int = 0
    skipped_unscored: Counter = field(default_factory=Counter)  # label suffix → n
    multi_exemplar_classes: int = 0
    counts: Counter = field(default_factory=Counter)  # (level, method, context) → n
    genes: int = 0
    genes_without_id: list[str] = field(default_factory=list)  # "set: name (reason)"

    def count_table(self) -> dict[str, dict[str, int]]:
        """``{level: {"METHOD/CONTEXT": n}}``, sorted, for taxonomy_meta.yaml."""
        out: dict[str, dict[str, int]] = {}
        for (level, method, context), n in sorted(self.counts.items()):
            out.setdefault(level, {})[f"{method}/{context}"] = n
        return out


def load_rows(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        rows = json.load(fh)
    if not isinstance(rows, list):
        raise MarkerSetError(f"{path}: expected a JSON list of rows")
    return rows


def _one(val: Any, what: str, set_id: str) -> Any:
    """Unwrap a KG single-element list (scalars pass through)."""
    if isinstance(val, list):
        if len(val) != 1:
            raise MarkerSetError(f"{set_id}: {what} has {len(val)} values, expected 1: {val!r}")
        return val[0]
    return val


def _score(val: Any, what: str, set_id: str) -> float:
    raw = _one(val, what, set_id)
    try:
        x = float(raw)
    except (TypeError, ValueError) as exc:
        raise MarkerSetError(f"{set_id}: {what} is not a number: {raw!r}") from exc
    if not 0.0 <= x <= 1.0:
        raise MarkerSetError(f"{set_id}: {what} {x} is outside [0, 1]")
    return x


def _performance(row: dict, set_id: str) -> list[dict]:
    """The set's F-beta / precision / recall, or [] for an unscored set.

    All three or none: a partial set of scores is an error, as is an F-beta
    that isn't F(beta=0.5) of the set's own precision and recall."""
    present = [k for k in ("precision", "recall", "f_beta") if row.get(k) is not None]
    if not present:
        return []
    if len(present) != 3:
        raise MarkerSetError(f"{set_id}: has only {present} of precision / recall / F-beta")
    precision = _score(row["precision"], "precision", set_id)
    recall = _score(row["recall"], "recall", set_id)
    fb = _score(row["f_beta"], "F-beta", set_id)
    if abs(f_beta(precision, recall) - fb) > _F_TOLERANCE:
        raise MarkerSetError(
            f"{set_id}: F-beta {fb} is not F(beta={F_BETA}) of precision {precision} "
            f"and recall {recall} ({f_beta(precision, recall):.6f})"
        )
    return [
        {"metric": "F_BETA", "value": fb, "beta": F_BETA},
        {"metric": "PRECISION", "value": precision},
        {"metric": "RECALL", "value": recall},
    ]


def f_beta(precision: float, recall: float, beta: float = F_BETA) -> float:
    b2 = beta * beta
    denom = b2 * precision + recall
    return (1 + b2) * precision * recall / denom if denom else 0.0


def classify(label: str, xref: Iterable[str] | None, algorithm: Iterable[str] | None,
             set_id: str) -> tuple[str, str, str] | None:
    """``(selection_method, context, role)``, or None for an unscored kind.

    Raises when the label suffix and the DOI (or NS-Forest's ``algorithm``)
    disagree."""
    xrefs = set(xref or [])
    algos = set(algorithm or [])
    for suffix, (method, context, role, doi) in _KINDS.items():
        if label.endswith(suffix):
            if xrefs != {doi}:
                raise MarkerSetError(
                    f"{set_id}: label {label!r} says {method} but its reference is "
                    f"{sorted(xrefs)}, expected [{doi}]"
                )
            if (method == "NS_FOREST") != ("NSforest" in algos):
                raise MarkerSetError(
                    f"{set_id}: label {label!r} and algorithm {sorted(algos)} disagree"
                )
            return method, context, role
    if xrefs & {YAO_DOI, NS_FOREST_DOI} or algos:
        raise MarkerSetError(
            f"{set_id}: label {label!r} matches no known set kind but cites "
            f"{sorted(xrefs)} / algorithm {sorted(algos)}"
        )
    return None


def label_gene_names(label: str) -> list[str]:
    """The gene names of a set label, in order: "Fev, Gata2 2 (NSforest)." →
    ["Fev", "Gata2"]."""
    body = label.rsplit(" (", 1)[0]
    body = _UNIQUENESS_SUFFIX_RE.sub("", body)
    return [t.strip() for t in body.split(",") if t.strip()]


def _kg_gene_name(label: str) -> str:
    m = _GENE_LABEL_RE.match(label or "")
    return m.group(1) if m else (label or "")


def pair_genes(
    set_id: str,
    names: list[str],
    genes: list[dict],
    known_names: Callable[[str], set[str]],
) -> list[tuple[str, str]]:
    """Pair each label name with one gene CURIE: ``[(name, curie)]`` in label
    order.

    A gene matches a name when the name is its KG label or one of
    ``known_names(curie)`` (official symbol, stats symbol); names left over
    pair by elimination only when exactly one name and one gene remain."""
    if len(names) != len(genes):
        raise MarkerSetError(
            f"{set_id}: label names {names} but {len(genes)} genes "
            f"{[g.get('curie') for g in genes]}"
        )
    free = {g["curie"]: {_kg_gene_name(g.get("label", ""))} | known_names(g["curie"])
            for g in genes}
    if len(free) != len(genes):
        raise MarkerSetError(f"{set_id}: a gene is listed twice: {genes}")
    paired: dict[str, str] = {}
    for name in names:
        hits = [c for c, ns in free.items() if name in ns]
        if len(hits) == 1:
            paired[name] = hits[0]
            del free[hits[0]]
    left = [n for n in names if n not in paired]
    if len(left) == 1 and len(free) == 1:
        paired[left[0]] = next(iter(free))
    elif left:
        raise MarkerSetError(
            f"{set_id}: cannot pair names {left} with genes {sorted(free)} "
            f"(KG labels {[g.get('label') for g in genes]})"
        )
    return [(n, paired[n]) for n in names]


@dataclass
class NodeInfo:
    """What the build needs of a taxonomy node."""

    level: str
    parent_id: str | None


def _ancestor_at(node_id: str, level: str, nodes: Mapping[str, NodeInfo]) -> str | None:
    seen: set[str] = set()
    cur: str | None = node_id
    while cur and cur not in seen:
        seen.add(cur)
        info = nodes.get(cur)
        if info is None:
            return None
        if info.level == level and cur != node_id:
            return cur
        cur = info.parent_id
    return None


def build_marker_sets(
    rows: list[dict],
    nodes: Mapping[str, NodeInfo],
    gene_records: Callable[[set[str]], dict[str, dict]],
    known_names: Callable[[str], set[str]] = lambda _c: set(),
) -> tuple[dict[str, list[dict]], MarkerSetReport]:
    """``({node CURIE: [MarkerSet dict]}, report)``.

    ``nodes``: taxonomy node CURIE → level + parent CURIE.
    ``gene_records``: NCBIGene CURIEs → ``{id: {"label": symbol} | {"missing": True, …}}``
    (IDs left out are unresolved). ``known_names``: other names a gene CURIE
    goes by in the taxonomy (for pairing only).
    """
    report = MarkerSetReport(rows=len(rows))
    seen_sets: set[str] = set()
    multi: set[str] = set()
    pending: list[tuple[str, str, dict, list[tuple[str, str]]]] = []

    for row in rows:
        set_id = row.get("set_id") or "?"
        label = row.get("set_label") or ""
        kind = classify(label, row.get("xref"), row.get("algorithm"), set_id)
        if kind is None:
            suffix = label.rsplit(" (", 1)[-1] if " (" in label else label
            report.skipped_unscored[f"({suffix}"] += 1
            if any(row.get(k) for k in ("precision", "recall", "f_beta")):
                raise MarkerSetError(f"{set_id}: skipped kind {label!r} carries scores")
            continue
        method, context, role = kind

        via_class = row.get("via_class") or "?"
        finest = row.get("finest") or []
        if len(finest) != 1 or not row.get("ancestors_ok"):
            raise MarkerSetError(
                f"{set_id}: class {via_class} exemplars {row.get('exemplars')} have no "
                f"single most specific cell set of which the others are ancestors "
                f"(finest {finest})"
            )
        if len(row.get("exemplars") or []) > 1:
            multi.add(via_class)
        node_id = finest[0]
        if node_id not in nodes:
            raise MarkerSetError(f"{set_id}: exemplar {node_id} is not a taxonomy node")
        if set_id in seen_sets:
            raise MarkerSetError(f"{set_id}: set appears on more than one row")
        seen_sets.add(set_id)

        performance = _performance(row, set_id)

        ms: dict[str, Any] = {
            "id": set_id,
            "genes": [],
            "selection_method": method,
            "context": context,
        }
        if context == "WITHIN_PARENT":
            parent = _ancestor_at(node_id, _WITHIN_PARENT_LEVEL, nodes)
            if parent is None:
                raise MarkerSetError(
                    f"{set_id}: within-{_WITHIN_PARENT_LEVEL} set on {node_id} "
                    f"({nodes[node_id].level}), which has no {_WITHIN_PARENT_LEVEL} ancestor"
                )
            ms["context_node"] = parent
        ms["role"] = role
        ms["via_class"] = via_class
        if performance:
            ms["performance"] = performance
            report.scored += 1
        ms["source"] = {"ref": _SOURCE_DOI[method], "method": _SOURCE_METHOD[method]}

        pairs = pair_genes(set_id, label_gene_names(label), row.get("genes") or [], known_names)
        pending.append((node_id, nodes[node_id].level, ms, pairs))

    ids = {c for *_, pairs in pending for _, c in pairs if c.startswith("NCBIGene:")}
    records = gene_records(ids) if ids else {}

    out: dict[str, list[dict]] = {}
    for node_id, level, ms, pairs in pending:
        for name, curie in pairs:
            g: dict[str, Any] = {"name_in_source": name}
            rec = records.get(curie)
            if not curie.startswith("NCBIGene:"):
                report.genes_without_id.append(f"{ms['id']}: {name} ({curie}: not an NCBI gene ID)")
            elif rec is None:
                report.genes_without_id.append(f"{ms['id']}: {name} ({curie}: not looked up)")
            elif rec.get("missing"):
                why = (f"replaced by {rec['replaced_by']}" if rec.get("replaced_by")
                       else "not a current NCBI gene")
                report.genes_without_id.append(f"{ms['id']}: {name} ({curie}: {why})")
            else:
                g["ncbi_gene_id"] = curie
                g["symbol"] = rec["label"]
            ms["genes"].append(g)
            report.genes += 1
        out.setdefault(node_id, []).append(ms)
        report.attached += 1
        report.counts[(level, ms["selection_method"], ms["context"])] += 1
    report.multi_exemplar_classes = len(multi)
    return out, report


def check_counts(report: MarkerSetReport, expected: Mapping[str, Mapping[str, int]] | None) -> list[str]:
    """Drift between the built counts and the declared baseline (empty = match)."""
    if expected is None:
        return ["no expected_counts declared for marker sets"]
    got = report.count_table()
    errors: list[str] = []
    for level in sorted(set(got) | set(expected)):
        g, e = got.get(level, {}), dict(expected.get(level) or {})
        for key in sorted(set(g) | set(e)):
            if g.get(key, 0) != e.get(key, 0):
                errors.append(f"{level} {key}: built {g.get(key, 0)}, expected {e.get(key, 0)}")
    return errors
