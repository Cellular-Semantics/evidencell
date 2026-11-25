"""On-demand atlas expression, cached in the taxonomy SQLite DB (#189, #216).

Expression values are derived data: they come from the MapMyCells
precomputed-stats HDF5 for a taxonomy, not from the taxonomy YAML. This
module reads them one gene column at a time and caches them in two DB
tables, both keyed by Ensembl ID:

- ``node_expression(node_id, ensembl_id, mean_expression)`` — one row per
  atlas node × cached gene. Leaf (rank-0) values are the stats file's
  per-cluster means; every non-leaf node gets the n_cells-weighted mean of
  its rank-0 descendants. With ``n_cells == 1`` throughout (WMBv1) that is
  a plain, unweighted average of cluster means.
- ``expression_genes(ensembl_id, source_file, source_sha256, loaded_at)`` —
  which genes are cached and from which file.

Which gene a marker name means is not decided here: callers resolve names
through :mod:`evidencell.gene_identity` (the ``genes`` / ``gene_synonyms``
tables), and this module reads the resolved genes' stats columns. A name
that doesn't resolve is reported in ``not_measured`` with the reason
(``NO_ENSEMBL_MAPPING``: no gene of the taxonomy has that name;
``AMBIGUOUS_SYMBOL``: several do; ``NO_GENE_ID``: a curated marker with no
``ncbi_gene_id``, not resolved by name; ``PIN_NOT_IN_TAXONOMY``: a marker's
``ncbi_gene_id`` isn't a gene of the taxonomy and its official symbol isn't
exactly one; ``CONFLICTING_PINS``: markers of one node share the name but
not the gene) — a recorded gap, never a silent empty result.

``just build-taxonomy-db`` creates both cache tables empty; they fill on
use. Consumers go through :meth:`TaxonomyDB.expression`.

The stats file location comes from the existing registry: it is
``conf/mapmycells/{taxonomy_id}/{basename of stats_s3_url}`` (the URL from
``annotation_transfer/src/annotation_transfer/taxonomies.py``, which is
where ``just fetch-mapmycells`` writes it).

The cache is dropped (and reloads on use) when the stats file's sha256
changes. A stats file that differs from the one ``gene_ids.tsv.gz`` was
built from is refused: its column indices can't be trusted.

Fail closed: a gene that is not cached and cannot be loaded (stats file
missing or mismatched) raises :class:`ExpressionUnavailable` with the fix.

Stats format: ``sum`` is the per-cluster sum of expression over cells and
``n_cells`` the cell count, so a cluster mean is ``sum / n_cells``. The
WMBv1 file (``precomputed_stats_ABC_revision_230821.h5``) was built from
cluster means with ``n_cells == 1`` throughout, so its ``sum`` already is
the mean; dividing keeps files built from real cell sums correct too.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sqlite3
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING, Iterable, Mapping
from urllib.parse import urlparse

if TYPE_CHECKING:
    from evidencell.gene_identity import Gene, GeneMatch

NO_ENSEMBL_MAPPING = "NO_ENSEMBL_MAPPING"
AMBIGUOUS_SYMBOL = "AMBIGUOUS_SYMBOL"
NO_GENE_ID = "NO_GENE_ID"  # curated marker without ncbi_gene_id (#244)
PIN_NOT_IN_TAXONOMY = "PIN_NOT_IN_TAXONOMY"  # pinned gene not here, nor its symbol
CONFLICTING_PINS = "CONFLICTING_PINS"  # one name, different genes on one node

_FINGERPRINT_KEY = "expression_stats_fingerprint"


class ExpressionUnavailable(RuntimeError):
    """Expression is needed but can't be read (stats file / gene tables missing)."""


@dataclass
class ExpressionLookup:
    """Result of an expression query.

    ``values``: ``{node_id: {name: mean_expression}}`` for measured genes,
    keyed by the names the caller asked for.
    ``not_measured``: ``{name: reason}`` for names that can't be measured.
    ``genes``: ``{name: GeneMatch}`` — how each name resolved.
    ``source_file``: basename of the stats file the cache was filled from.
    """

    values: dict[str, dict[str, float]] = field(default_factory=dict)
    not_measured: dict[str, str] = field(default_factory=dict)
    genes: dict[str, GeneMatch] = field(default_factory=dict)
    source_file: str | None = None

    def for_node(self, accession: str) -> dict[str, float]:
        return self.values.get(_node_id(accession), {})

    def gene_symbol(self, name: str) -> str | None:
        """The atlas-side symbol ``name`` resolved to (the stats file's
        symbol, as used in atlas marker lists), or None."""
        m = self.genes.get(name)
        return m.gene.stats_symbol if m is not None and m.gene is not None else None


# ── File locations (registry-driven) ─────────────────────────────────────────


def _load_registry() -> dict:
    """Load ``_BUILTIN_TAXONOMIES`` from the annotation_transfer registry.

    annotation_transfer is not installed into the evidencell environment
    (the justfile reaches it via PYTHONPATH), so load the module by path.
    """
    from evidencell.paths import repo_root

    name = "_evidencell_at_taxonomies"
    if name not in sys.modules:
        path = (
            repo_root() / "annotation_transfer" / "src" / "annotation_transfer" / "taxonomies.py"
        )
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None or not path.is_file():
            raise ExpressionUnavailable(f"MapMyCells taxonomy registry not found at {path}")
        module = importlib.util.module_from_spec(spec)
        # Registered before exec: the module's dataclasses resolve their
        # annotations through sys.modules.
        sys.modules[name] = module
        try:
            spec.loader.exec_module(module)
        except Exception:
            del sys.modules[name]
            raise
    return sys.modules[name]._BUILTIN_TAXONOMIES


def stats_h5_path(taxonomy_id: str) -> Path:
    """Canonical local path of a taxonomy's precomputed-stats HDF5."""
    from evidencell.paths import repo_root

    spec = _load_registry().get(taxonomy_id)
    if spec is None or not spec.stats_s3_url:
        raise ExpressionUnavailable(
            f"No MapMyCells stats file is registered for taxonomy {taxonomy_id} "
            "(annotation_transfer/src/annotation_transfer/taxonomies.py), so atlas "
            "expression can't be read for it."
        )
    name = Path(urlparse(spec.stats_s3_url).path).name
    return repo_root() / "conf" / "mapmycells" / taxonomy_id / name


# ── Cache maintenance ────────────────────────────────────────────────────────


def _node_id(accession: str) -> str:
    return accession.split(":", 1)[-1] if ":" in accession else accession


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def _stats_sha256(con: sqlite3.Connection, stats_path: Path) -> str:
    """sha256 of the stats file, memoised in ``_meta`` by (path, size, mtime).

    Hashing a 1.4 GB file takes seconds; a stat() does not. The hash is
    recomputed only when the file's size or mtime changes.
    """
    st = stats_path.stat()
    fp = {"path": str(stats_path.resolve()), "size": st.st_size, "mtime_ns": st.st_mtime_ns}
    con.execute("CREATE TABLE IF NOT EXISTS _meta (key TEXT PRIMARY KEY, value TEXT)")
    row = con.execute("SELECT value FROM _meta WHERE key = ?", (_FINGERPRINT_KEY,)).fetchone()
    if row:
        stored = json.loads(row[0])
        if all(stored.get(k) == v for k, v in fp.items()):
            return stored["sha256"]
    sha = _sha256(stats_path)
    con.execute(
        "INSERT OR REPLACE INTO _meta VALUES (?, ?)",
        (_FINGERPRINT_KEY, json.dumps({**fp, "sha256": sha})),
    )
    return sha


def _drop_stale_cache(con: sqlite3.Connection, sha: str) -> None:
    """Drop the cache when it was filled from a different stats file release."""
    stale = con.execute(
        "SELECT COUNT(*) FROM expression_genes WHERE source_sha256 != ?", (sha,)
    ).fetchone()[0]
    if stale:
        print(
            f"  Stats file changed since the expression cache was filled — "
            f"dropping {stale} cached gene(s); they reload on use.",
            file=sys.stderr,
        )
        con.execute("DELETE FROM node_expression")
        con.execute("DELETE FROM expression_genes")
        # Committed now: if the reload below fails, the stale values must
        # not survive a rollback and be served on the next call.
        con.commit()


def ensure_genes(
    con: sqlite3.Connection,
    taxonomy_id: str,
    genes: Iterable[Gene],
    *,
    stats_path: Path,
) -> None:
    """Make sure every gene has cached expression, loading uncached genes
    from the stats HDF5 by their ``stats_col``.

    Raises :class:`ExpressionUnavailable` if any gene is uncached and the
    stats file is missing, or is not the file the gene table was built from.
    """
    from evidencell.gene_identity import gene_ids_meta

    wanted = {g.ensembl_id: g for g in genes}
    if not wanted:
        return

    have_stats = stats_path.is_file()
    sha = _stats_sha256(con, stats_path) if have_stats else None
    if sha is not None:
        _drop_stale_cache(con, sha)

    ids = sorted(wanted)
    cached = {
        r[0]
        for r in con.execute(
            f"SELECT ensembl_id FROM expression_genes WHERE ensembl_id IN ({','.join('?' * len(ids))})",
            ids,
        )
    }
    missing = [wanted[e] for e in ids if e not in cached]
    if not missing:
        return

    sample = ", ".join(g.stats_symbol for g in missing[:8]) + (" …" if len(missing) > 8 else "")
    if not have_stats:
        raise ExpressionUnavailable(
            f"Atlas expression for {len(missing)} gene(s) ({sample}) is not cached in the "
            f"{taxonomy_id} taxonomy DB and the MapMyCells stats file is missing: "
            f"{stats_path}. Run: just fetch-mapmycells {taxonomy_id}"
        )
    assert sha is not None
    meta = gene_ids_meta(con) or {}
    if meta.get("stats_sha256") and meta["stats_sha256"] != sha:
        raise ExpressionUnavailable(
            f"The {taxonomy_id} gene table (gene_ids.tsv.gz) was built from a stats file "
            f"with sha256 {meta['stats_sha256'][:12]}…, but {stats_path.name} has "
            f"{sha[:12]}…; its column indices can't be trusted. Refresh it with: "
            f"just build-gene-ids {taxonomy_id}, then just build-taxonomy-db {taxonomy_id}"
        )
    _load_genes(con, missing, stats_path=stats_path, sha=sha)


def _leaf_descendants(con: sqlite3.Connection) -> tuple[list[str], dict[str, list[str]]]:
    """Return (rank-0 node ids, {non-leaf node id: rank-0 descendant ids})."""
    rows = con.execute("SELECT node_id, parent_id, taxonomy_rank FROM nodes").fetchall()
    children: dict[str, list[str]] = {}
    rank_of: dict[str, int | None] = {}
    for node_id, parent_id, rank in rows:
        rank_of[node_id] = rank
        if parent_id:
            children.setdefault(parent_id, []).append(node_id)
    leaves = [n for n, r in rank_of.items() if r == 0]
    out: dict[str, list[str]] = {}
    for node_id, rank in rank_of.items():
        if rank == 0 or node_id not in children:
            continue
        found: list[str] = []
        stack = list(children[node_id])
        seen: set[str] = set()
        while stack:
            n = stack.pop()
            if n in seen:
                continue
            seen.add(n)
            if rank_of.get(n) == 0:
                found.append(n)
            else:
                stack.extend(children.get(n, []))
        if found:
            out[node_id] = found
    return leaves, out


def _load_genes(
    con: sqlite3.Connection,
    genes: list[Gene],
    *,
    stats_path: Path,
    sha: str,
) -> None:
    import h5py
    import numpy as np

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    source = stats_path.name

    with h5py.File(str(stats_path), "r") as f:
        col_names: list[str] = json.loads(f["col_names"][()])
        cluster_to_row: dict[str, int] = json.loads(f["cluster_to_row"][()])
        n_cells = np.asarray(f["n_cells"][:], dtype=float)
        for g in genes:
            if g.stats_col >= len(col_names) or (
                col_names[g.stats_col].split(".", 1)[0] != g.ensembl_id
            ):
                raise ExpressionUnavailable(
                    f"{stats_path.name} column {g.stats_col} is not {g.ensembl_id} "
                    f"({g.stats_symbol}); the gene table is out of step with the stats file. "
                    "Refresh it with just build-gene-ids, then just build-taxonomy-db."
                )

        # Read only the needed columns, never the whole matrix. h5py needs
        # increasing indices for a fancy selection.
        cols = sorted({g.stats_col for g in genes})
        col_pos = {c: i for i, c in enumerate(cols)}
        sums = np.asarray(f["sum"][:, cols], dtype=float)

        leaves, descendants = _leaf_descendants(con)
        leaf_row = {n: cluster_to_row[n] for n in leaves if n in cluster_to_row}
        if not leaf_row:
            raise ExpressionUnavailable(
                f"None of the taxonomy's leaf node ids appear in the stats file's "
                f"cluster_to_row ({stats_path}); is it the right file for this taxonomy?"
            )

        node_rows: list[tuple[str, str, float]] = []

        def _emit(node_id: str, rows: list[int]) -> None:
            total = n_cells[rows].sum()
            if total <= 0:
                return
            means = sums[rows].sum(axis=0) / total
            for g in genes:
                node_rows.append((node_id, g.ensembl_id, float(means[col_pos[g.stats_col]])))

        for node_id, row in leaf_row.items():
            _emit(node_id, [row])
        for node_id, leaf_ids in descendants.items():
            rows = [leaf_row[n] for n in leaf_ids if n in leaf_row]
            if rows:
                _emit(node_id, rows)

    con.executemany("INSERT OR REPLACE INTO node_expression VALUES (?, ?, ?)", node_rows)
    con.executemany(
        "INSERT OR REPLACE INTO expression_genes VALUES (?, ?, ?, ?)",
        [(g.ensembl_id, source, sha, now) for g in genes],
    )
    con.commit()
    print(
        f"  Loaded expression for {len(genes)} gene(s) from {source} into the taxonomy DB cache",
        file=sys.stderr,
    )


# ── Query ────────────────────────────────────────────────────────────────────


def query(
    con: sqlite3.Connection,
    matches: Mapping[str, GeneMatch],
    *,
    accessions: Iterable[str] | None = None,
    ranks: Iterable[int] | None = None,
) -> ExpressionLookup:
    """Read cached expression for resolved names, keyed by name.

    Restrict nodes with ``accessions`` and/or ``ranks``; with neither,
    every node is returned. Call :func:`ensure_genes` first.
    """
    from evidencell.gene_identity import AMBIGUOUS
    from evidencell.gene_identity import CONFLICTING_PINS as _CONFLICT
    from evidencell.gene_identity import NO_GENE_ID as _NO_GENE
    from evidencell.gene_identity import PIN_NOT_IN_TAXONOMY as _NOT_HERE

    reasons = {
        AMBIGUOUS: AMBIGUOUS_SYMBOL, _NO_GENE: NO_GENE_ID,
        _NOT_HERE: PIN_NOT_IN_TAXONOMY, _CONFLICT: CONFLICTING_PINS,
    }

    out = ExpressionLookup(genes=dict(matches))
    by_ensembl: dict[str, list[str]] = {}
    for name, m in matches.items():
        if m.gene is None:
            out.not_measured[name] = reasons.get(m.method, NO_ENSEMBL_MAPPING)
        else:
            by_ensembl.setdefault(m.gene.ensembl_id, []).append(name)
    if not by_ensembl:
        return out
    ens = sorted(by_ensembl)
    ens_ph = ",".join("?" * len(ens))
    row = con.execute(
        f"SELECT source_file FROM expression_genes WHERE ensembl_id IN ({ens_ph}) LIMIT 1", ens
    ).fetchone()
    out.source_file = row[0] if row else None

    sql = (
        "SELECT e.node_id, e.ensembl_id, e.mean_expression FROM node_expression e "
        f"JOIN nodes n ON n.node_id = e.node_id WHERE e.ensembl_id IN ({ens_ph})"
    )
    params: list = list(ens)
    if accessions is not None:
        ids = sorted({_node_id(a) for a in accessions if a})
        if not ids:
            return out
        sql += f" AND e.node_id IN ({','.join('?' * len(ids))})"
        params += ids
    if ranks is not None:
        rank_list = sorted(set(ranks))
        sql += f" AND n.taxonomy_rank IN ({','.join('?' * len(rank_list))})"
        params += rank_list
    for node_id, ensembl_id, val in con.execute(sql, params):
        node = out.values.setdefault(node_id, {})
        for name in by_ensembl[ensembl_id]:
            node[name] = float(val)
    return out
