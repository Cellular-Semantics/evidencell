"""AT-blind audit: would marker + region + NT filtering surface the
candidates that annotation transfer has identified?

Ground truth comes from edges in ``kb/graphs/**/*.yaml`` carrying
``AnnotationTransferEvidence``. For each (classical, atlas-target,
F1) triple, the audit runs ``find_candidates`` with the AT signal
disabled (no artifact, no AT bypass) and reports whether the target
appears in the top-K. The audit is *blind* in the sense that the
candidate-finding code is denied the very signal it's being audited
against.

Misses are categorised by reason — region_drop / nt_drop /
negative_score / below_topk / found — using filter-level inspection
of the candidate's anat and NT, so a miss is never just "didn't
appear, dunno why".

See ``research/validation/methods_audits/at_blind/README.md`` for the
methodology writeup, run history, and decisions informed by past
runs.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Callable

import yaml

from evidencell.paths import repo_root, taxonomy_db_path
from evidencell.taxonomy_db import (
    TaxonomyDB,
    _classical_negative_markers,
    _classical_positive_markers,
    _resolve_mba_by_name,
    load_expression_data,
)

from .base import AuditAssertion, AuditDriver, AuditOutcome


# Accession-prefix → taxonomy_level mapping used when a graph stub
# omits ``taxonomy_level`` (most do for atlas-target stubs).
_ACCESSION_PREFIX_TO_LEVEL = {
    "_CLUS_": "cluster",
    "_SUPT_": "supertype",
    "_SUBC_": "subclass",
    "_CLAS_": "class",
}
_LEVEL_TO_RANK = {"cluster": 0, "supertype": 1, "subclass": 2, "class": 3}


class ATBlindAudit(AuditDriver):
    """Audit driver implementing the AT-blind methodology described in
    the module docstring."""

    audit_id = "at_blind"

    def __init__(
        self,
        taxonomy_id: str = "CCN20230722",
        top_k: int = 10,
        f1_floor: float = 0.2,
        limit: int | None = None,
        graphs_root: Path | None = None,
        **base_kwargs,
    ):
        config = {
            "taxonomy_id": taxonomy_id,
            "top_k": top_k,
            "f1_floor": f1_floor,
            "limit": limit,
        }
        super().__init__(config=config, **base_kwargs)
        self.taxonomy_id = taxonomy_id
        self.top_k = top_k
        self.f1_floor = f1_floor
        self.limit = limit
        self.graphs_root = graphs_root or (repo_root() / "kb" / "graphs")
        self._db: TaxonomyDB | None = None
        self._expr_cache: dict[int, dict] = {}
        self._rank_to_level: dict[int, str] = {}

    # ── Preflight invariants ──────────────────────────────────────────

    def preflight(self) -> list[tuple[str, Callable[[], None]]]:
        return [
            ("taxonomy_db_exists", self._check_db_exists),
            ("taxonomy_db_fresh", self._check_db_fresh),
            ("anat_closure_built", self._check_anat_closure),
            ("uberon_resolution_coverage", self._check_uberon_resolution),
        ]

    def _check_db_exists(self) -> None:
        path = taxonomy_db_path(self.taxonomy_id)
        if not path.exists():
            raise AuditAssertion(
                f"Taxonomy DB not found at {path}. Run: "
                f"just build-taxonomy-db {self.taxonomy_id}"
            )

    def _check_db_fresh(self) -> None:
        from evidencell.taxonomy_db import taxonomy_db_freshness
        is_stale, reasons = taxonomy_db_freshness(self.taxonomy_id)
        if is_stale:
            raise AuditAssertion(
                "Taxonomy DB is stale: " + "; ".join(reasons)
                + f". Rebuild with: just build-taxonomy-db {self.taxonomy_id}"
            )

    def _check_anat_closure(self) -> None:
        db = self._get_db()
        with db._connect() as con:
            try:
                con.execute("SELECT 1 FROM anat_closure LIMIT 1").fetchone()
            except sqlite3.OperationalError:
                raise AuditAssertion(
                    "anat_closure table not built — region filtering would "
                    "be disabled. Run: just fetch-mba-ontology && "
                    f"just build-anat-closure {self.taxonomy_id}"
                )

    def _check_uberon_resolution(self) -> None:
        """For every classical node we'd audit, verify that at least one
        UBERON ID resolves to an MBA term (via xref or name fallback).

        This catches the silent-region-filter-skip failure that bit us
        on OLM (UBERON:0005371 has no MBA xref; without name fallback the
        audit would have run with no region filter, producing misleading
        miss diagnoses).
        """
        cases = self._extract_at_targets()
        unresolved: list[str] = []
        seen: set[str] = set()
        db = self._get_db()
        with db._connect() as con:
            for case in cases:
                cid = case["classical_id"]
                if cid in seen:
                    continue
                seen.add(cid)
                classical = case["classical_node"]
                uberons = [
                    loc for loc in (classical.get("anatomical_location") or [])
                    if (loc.get("id") or "").startswith("UBERON:")
                    and loc.get("compartment") not in ("AXON_TARGET", "DENDRITE")
                ]
                if not uberons:
                    continue
                resolved_any = False
                for loc in uberons:
                    aid = loc["id"]
                    rows = con.execute(
                        "SELECT anat_id FROM anat_terms WHERE uberon_id = ?",
                        (aid,),
                    ).fetchall()
                    if rows:
                        resolved_any = True
                        break
                    name = loc.get("name_in_source") or loc.get("label") or ""
                    if _resolve_mba_by_name(con, name):
                        resolved_any = True
                        break
                if not resolved_any:
                    unresolved.append(cid)
        if unresolved:
            raise AuditAssertion(
                f"{len(unresolved)} classical nodes have UBERON IDs that "
                f"resolve to no MBA term (neither xref nor name fallback) — "
                f"region filtering would silently skip for these. "
                f"Fix in YAML or extend name-fallback synonyms. Affected: "
                + ", ".join(unresolved[:10])
                + ("..." if len(unresolved) > 10 else "")
            )

    # ── Ground-truth extraction ──────────────────────────────────────

    def _extract_at_targets(self) -> list[dict]:
        """Walk ``kb/graphs/**/*.yaml`` for edges with
        ``AnnotationTransferEvidence`` pointing at the audited taxonomy.

        Each returned dict carries the classical node, the target stub,
        the AT F1 score, the graph file path, and the inferred target
        rank. Stored on the instance for reuse by preflight + run."""
        if hasattr(self, "_cases_cache"):
            return self._cases_cache  # type: ignore[attr-defined]
        out: list[dict] = []
        for yaml_path in sorted(self.graphs_root.rglob("*.yaml")):
            try:
                doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
            except Exception:
                continue
            nodes_by_id = {
                n["id"]: n for n in (doc.get("nodes") or []) if n.get("id")
            }
            for edge in doc.get("edges") or []:
                ev = edge.get("evidence") or []
                at_items = [
                    e for e in ev
                    if isinstance(e, dict)
                    and e.get("evidence_type") == "ANNOTATION_TRANSFER"
                ]
                if not at_items:
                    continue
                type_a = edge.get("type_a")
                type_b = edge.get("type_b")
                if not (type_a and type_b):
                    continue
                classical = nodes_by_id.get(type_a)
                target = nodes_by_id.get(type_b)
                if not classical or not target:
                    continue
                if classical.get("definition_basis") == "ATLAS_TRANSCRIPTOMIC":
                    continue
                if target.get("definition_basis") != "ATLAS_TRANSCRIPTOMIC":
                    continue
                if target.get("taxonomy_id") != self.taxonomy_id:
                    continue
                target_acc = target.get("cell_set_accession")
                if not target_acc:
                    continue
                best_f1 = max(
                    (float(e.get("best_f1_score") or 0.0) for e in at_items),
                    default=0.0,
                )
                if best_f1 < self.f1_floor:
                    continue
                target_level = (target.get("taxonomy_level") or "").lower()
                if not target_level:
                    for prefix, lvl in _ACCESSION_PREFIX_TO_LEVEL.items():
                        if prefix in target_acc:
                            target_level = lvl
                            break
                target_rank = _LEVEL_TO_RANK.get(target_level, 0)

                # The F1 is informative AT THE LEVEL where it was
                # computed (best_mapping_level), which can legitimately
                # differ from the edge's target accession level — e.g.
                # a curator records `best_mapping_level: SUPERTYPE` on
                # a cluster-target edge to mean "the AT signal lives at
                # the parent supertype". The audit must route this case
                # to test at the supertype rank against the supertype
                # ancestor, not at the cluster rank against the cluster.
                # Build the effective (target_accession, rank) pair
                # accordingly.
                at_bml = (at_items[0].get("best_mapping_level") or "").lower()
                if at_bml and at_bml != target_level:
                    effective_acc, effective_rank = self._ancestor_at_level(
                        target_acc, at_bml
                    )
                    if effective_acc is None:
                        # Can't walk to that level; skip rather than
                        # produce a misrouted test case.
                        continue
                    effective_level = at_bml
                else:
                    effective_acc = target_acc
                    effective_level = target_level
                    effective_rank = target_rank

                out.append({
                    "test_id": f"{type_a}|{effective_acc}",
                    "graph_file": str(
                        yaml_path.relative_to(repo_root())
                    ),
                    "classical_id": type_a,
                    "classical_node": classical,
                    "target_id": type_b,
                    "target_accession": effective_acc,
                    "edge_target_accession": target_acc,  # for traceability
                    "target_level": effective_level,
                    "target_rank": effective_rank,
                    "best_f1": best_f1,
                    "best_mapping_level": at_items[0].get("best_mapping_level"),
                    "edge_relationship": edge.get("relationship"),
                })
        if self.limit:
            out = out[: self.limit]
        self._cases_cache = out
        return out

    def collect_ground_truth(self) -> list[dict]:
        return self._extract_at_targets()

    # ── Per-case execution ───────────────────────────────────────────

    def run_test_case(self, case: dict) -> AuditOutcome:
        rank = case["target_rank"]
        classical = case["classical_node"]
        target_acc = case["target_accession"]
        markers = _classical_positive_markers(classical)
        neg_markers = _classical_negative_markers(classical)
        nt_obj = classical.get("nt_type")
        nt_type = (
            nt_obj.get("name_in_source") if isinstance(nt_obj, dict)
            else nt_obj if isinstance(nt_obj, str) else None
        )
        mba_ids = self._resolve_anat(classical)
        optional_criteria = self._sex_bias(classical)
        expression_data = self._merged_expression(rank)
        db = self._get_db()

        fc_kwargs = dict(
            nt_type=nt_type,
            markers=markers,
            negative_markers=neg_markers or None,
            rank=rank,
            optional_criteria=optional_criteria,
            expression_data=expression_data or None,
            at_hits=None,        # blind: no AT scoring
            at_bypass=None,      # blind: no AT bypass on filters
        )
        try:
            candidates = db.find_candidates(
                anat_root_ids=mba_ids if mba_ids else None,
                **fc_kwargs,
            )
        except RuntimeError:
            candidates = db.find_candidates(**fc_kwargs)

        # Search for the AT target in the result set.
        rank_in_results: int | None = None
        score: float | None = None
        candidate_detail: dict | None = None
        for i, c in enumerate(candidates):
            if c["node_id"] == target_acc:
                rank_in_results = i + 1
                score = float(c["_score"])
                candidate_detail = {
                    "score": score,
                    "region_fraction": c.get("_region_fraction"),
                    "expression_detail": c.get("_expression_detail"),
                }
                break

        expected = {
            "target_accession": target_acc,
            "target_rank": rank,
            "best_f1": case["best_f1"],
            "edge_relationship": case["edge_relationship"],
        }

        if rank_in_results is None:
            # Categorise: region_drop, nt_drop, or negative_score.
            miss_reason = self._categorise_miss(
                db=db,
                target_acc=target_acc,
                queried_mba_ids=mba_ids,
                nt_type=nt_type,
            )
            actual = {
                "in_results": False,
                "rank_in_results": None,
                "score": None,
                "n_results": len(candidates),
                "queried_mba": mba_ids,
                "miss_reason": miss_reason,
            }
            return AuditOutcome(
                test_id=case["test_id"],
                expected=expected,
                actual=actual,
                passed=False,
                reason=miss_reason,
                notes=(
                    f"Target {target_acc} not in {len(candidates)} survivors "
                    f"(queried MBA: {mba_ids})"
                ),
                metadata={"graph_file": case["graph_file"]},
            )

        in_topk = rank_in_results <= self.top_k
        actual = {
            "in_results": True,
            "rank_in_results": rank_in_results,
            "score": score,
            "n_results": len(candidates),
            "queried_mba": mba_ids,
            "candidate_detail": candidate_detail,
        }
        return AuditOutcome(
            test_id=case["test_id"],
            expected=expected,
            actual=actual,
            passed=in_topk,
            reason="found" if in_topk else "below_topk",
            notes=(
                f"Target {target_acc} at rank {rank_in_results}/"
                f"{len(candidates)} (score={score})"
            ),
            metadata={"graph_file": case["graph_file"]},
        )

    # ── Helpers ───────────────────────────────────────────────────────

    def _ancestor_at_level(
        self, accession: str, target_level: str
    ) -> tuple[str | None, int | None]:
        """Walk up the taxonomy from ``accession`` until we hit a node
        at ``target_level``. Returns ``(ancestor_accession, ancestor_rank)``
        or ``(None, None)`` if no ancestor at that level exists.

        Used by the audit when an AT evidence's ``best_mapping_level``
        differs from the edge target's level: we test the AT signal at
        the level it was computed (the ancestor), not at the edge's
        target level.
        """
        target_level = (target_level or "").lower()
        if target_level not in _LEVEL_TO_RANK:
            return None, None
        target_rank = _LEVEL_TO_RANK[target_level]
        db = self._get_db()
        with db._connect() as con:
            cur_acc = accession
            for _ in range(8):  # safety bound
                row = con.execute(
                    "SELECT parent_id, taxonomy_rank FROM nodes WHERE node_id = ?",
                    (cur_acc,),
                ).fetchone()
                if not row:
                    return None, None
                parent_id, rank = row
                if rank == target_rank:
                    return cur_acc, rank
                if not parent_id:
                    return None, None
                cur_acc = parent_id
        return None, None

    def _get_db(self) -> TaxonomyDB:
        if self._db is None:
            self._db = TaxonomyDB(taxonomy_db_path(self.taxonomy_id))
        return self._db

    def _resolve_anat(self, classical: dict) -> list[str]:
        """UBERON → MBA resolution including name fallback. Soma only."""
        db = self._get_db()
        out: list[str] = []
        with db._connect() as con:
            for loc in (classical.get("anatomical_location") or []):
                if loc.get("compartment") in ("AXON_TARGET", "DENDRITE"):
                    continue
                aid = loc.get("id", "")
                if not aid:
                    continue
                if not aid.startswith("UBERON:"):
                    out.append(aid)
                    continue
                rows = con.execute(
                    "SELECT anat_id FROM anat_terms WHERE uberon_id = ?",
                    (aid,),
                ).fetchall()
                if rows:
                    out.extend(r[0] for r in rows)
                    continue
                name = loc.get("name_in_source") or loc.get("label") or ""
                fb = _resolve_mba_by_name(con, name)
                if fb:
                    out.extend(fb)
        return out

    def _sex_bias(self, classical: dict) -> dict[str, str] | None:
        sb = classical.get("sex_bias")
        if not sb or sb == "NOT_DIMORPHIC":
            return None
        return {"sex_bias": sb.lower().split("_")[0]}

    def _merged_expression(self, rank: int) -> dict:
        """Load queried-rank + rank-0 expression data, merged."""
        merged: dict = {}
        for r in {rank, 0}:
            if r in self._expr_cache:
                merged.update(self._expr_cache[r])
                continue
            if not self._rank_to_level:
                db = self._get_db()
                with db._connect() as con:
                    rows = con.execute(
                        "SELECT DISTINCT taxonomy_level, taxonomy_rank FROM nodes "
                        "WHERE taxonomy_rank IS NOT NULL"
                    ).fetchall()
                self._rank_to_level = {row[1]: row[0] for row in rows}
            level = self._rank_to_level.get(r)
            if level:
                ed = load_expression_data(self.taxonomy_id, level)
                self._expr_cache[r] = ed
                merged.update(ed)
        return merged

    def _categorise_miss(
        self,
        db: TaxonomyDB,
        target_acc: str,
        queried_mba_ids: list[str],
        nt_type: str | None,
    ) -> str:
        """When a target isn't in find-candidates results, identify which
        filter dropped it (or whether it scored negatively)."""

        # Region check: did target lose to the region filter?
        if queried_mba_ids:
            effective: set[str] = set()
            try:
                for root in queried_mba_ids:
                    effective.update(db.get_descendants(root, include_self=True))
                expanded: set[str] = set(effective)
                for seed in queried_mba_ids:
                    for parent in db.get_anat_parents(seed):
                        expanded.update(
                            db.get_descendants(parent, include_self=True)
                        )
            except RuntimeError:
                expanded = set()

            with db._connect() as con:
                target_anat_rows = con.execute(
                    "SELECT anat_id FROM anat WHERE node_id = ?",
                    (target_acc,),
                ).fetchall()
            target_anat = {r[0] for r in target_anat_rows}
            if expanded and target_anat and not (target_anat & expanded):
                return "region_drop"

        # NT check
        if nt_type:
            with db._connect() as con:
                row = con.execute(
                    "SELECT nt_type FROM nodes WHERE node_id = ?",
                    (target_acc,),
                ).fetchone()
            target_nt = row[0] if row and row[0] else None
            if target_nt:
                nn, qt = target_nt.lower(), nt_type.lower()
                if not (nn.startswith(qt) or qt.startswith(nn)):
                    return "nt_drop"

        # Default: survived filters but score < 0 (or some unhandled case).
        return "negative_score_or_other"
