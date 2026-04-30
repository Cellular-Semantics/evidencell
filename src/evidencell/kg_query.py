"""KG query utility — run Cypher files against a local neo4j bolt endpoint.

Fetches taxonomy export JSON from brain_cell_KG without manual intervention.

Usage (CLI):
  python -m evidencell.kg_query fetch <cypher_file> <taxonomy_id>
  python -m evidencell.kg_query fetch inputs/taxonomies/CCN20230722.cypher CCN20230722 \\
      --bolt-url bolt://localhost:7687

Requires the [kg] optional dependency group:
  uv sync --extra kg
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# neo4j is an optional dep — import lazily so the rest of evidencell works without it
_neo4j_available: bool | None = None


def _check_neo4j() -> None:
    global _neo4j_available
    if _neo4j_available is None:
        try:
            import neo4j  # noqa: F401
            _neo4j_available = True
        except ImportError:
            _neo4j_available = False
    if not _neo4j_available:
        raise ImportError(
            "neo4j package not installed. Install with: uv sync --extra kg"
        )


# Default bolt URL — can be overridden via env var or constructor argument
DEFAULT_BOLT_URL = "bolt://localhost:7687"


def _wrap_value(val: object) -> object:
    """Wrap neo4j Node values in {identity, labels, properties, elementId} form.

    Recurses into lists. Leaves scalars and dicts unchanged. The wrapped shape
    matches what the original VFB graph export produced and what taxonomy_db
    ingest code expects.
    """
    from neo4j.graph import Node

    if isinstance(val, Node):
        return {
            "identity": val.element_id,
            "labels": list(val.labels),
            "properties": dict(val.items()),
            "elementId": val.element_id,
        }
    if isinstance(val, list):
        return [_wrap_value(v) for v in val]
    return val


def _record_to_dict(record: object) -> dict:
    """Convert a neo4j Record to a plain dict, wrapping Node values."""
    return {key: _wrap_value(record[key]) for key in record.keys()}


class KGQueryClient:
    """Thin wrapper around the neo4j Python driver for evidencell KG queries."""

    def __init__(
        self,
        endpoint: str | None = None,
        user: str | None = None,
        password: str | None = None,
    ) -> None:
        _check_neo4j()
        self.endpoint = endpoint or os.environ.get("NEO4J_BOLT_URL", DEFAULT_BOLT_URL)
        self.user = user or os.environ.get("NEO4J_USER")
        self.password = password or os.environ.get("NEO4J_PASSWORD")
        self._driver = None

    def connect(self) -> None:
        from neo4j import GraphDatabase, basic_auth
        try:
            if self.user and self.password:
                self._driver = GraphDatabase.driver(
                    self.endpoint, auth=basic_auth(self.user, self.password)
                )
            else:
                self._driver = GraphDatabase.driver(self.endpoint)
            with self._driver.session() as session:
                session.run("RETURN 1")
        except Exception as exc:
            self._driver = None
            raise ConnectionError(
                f"Cannot connect to neo4j at {self.endpoint}: {exc}"
            ) from exc

    def test_connection(self) -> bool:
        try:
            if self._driver is None:
                self.connect()
            with self._driver.session() as session:  # type: ignore[union-attr]
                result = session.run("RETURN 1")
                return result.single()[0] == 1
        except Exception:
            return False

    def run_query(
        self, cypher: str, parameters: dict | None = None
    ) -> list[dict]:
        """Execute a Cypher statement and return all records as plain dicts.

        Node values are wrapped in the canonical {identity, labels, properties,
        elementId} shape rather than flattened to their property dicts. This
        preserves the structure the taxonomy_db ingest expects and the original
        VFB graph export used.
        """
        if self._driver is None:
            self.connect()
        with self._driver.session() as session:  # type: ignore[union-attr]
            result = session.run(cypher, parameters or {})
            return [_record_to_dict(record) for record in result]

    def close(self) -> None:
        if self._driver is not None:
            self._driver.close()
            self._driver = None

    def __enter__(self) -> "KGQueryClient":
        self.connect()
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


def fetch_taxonomy_json(
    cypher_path: Path,
    output_path: Path,
    endpoint: str | None = None,
    user: str | None = None,
    password: str | None = None,
) -> int:
    """Run a .cypher file against the KG, write results to output_path as JSON.

    Writes atomically (temp file → rename) so a partial run leaves no corrupt file.
    Returns the number of rows written.
    """
    cypher = cypher_path.read_text(encoding="utf-8").strip()
    # Strip line comments before sending to the driver
    lines = [ln for ln in cypher.splitlines() if not ln.strip().startswith("//")]
    cypher = "\n".join(lines).strip()

    client = KGQueryClient(endpoint=endpoint, user=user, password=password)
    with client:
        print(f"  Connecting to {client.endpoint}...")
        print(f"  Running query from {cypher_path.name}...")
        records = client.run_query(cypher)

    row_count = len(records)
    print(f"  Query returned {row_count:,} rows.")

    # Write atomically
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output_path.with_suffix(".json.tmp")
    with tmp_path.open("w", encoding="utf-8") as fh:
        json.dump(records, fh, ensure_ascii=False, indent=None)
    tmp_path.rename(output_path)
    print(f"  Written to {output_path}")
    return row_count


# ── CLI entry point ────────────────────────────────────────────────────────────

def _cmd_fetch(
    cypher_file: str,
    taxonomy_id: str,
    bolt_url: str | None = None,
    user: str | None = None,
    password: str | None = None,
) -> None:
    from evidencell.paths import repo_root
    cypher_path = Path(cypher_file)
    if not cypher_path.exists():
        print(f"ERROR: Cypher file not found: {cypher_path}")
        sys.exit(1)
    output_path = repo_root() / "inputs" / "taxonomies" / f"{taxonomy_id}.json"
    print(f"Fetching {taxonomy_id} taxonomy from KG → {output_path}")
    n = fetch_taxonomy_json(cypher_path, output_path, endpoint=bolt_url, user=user, password=password)
    print(f"Done. {n:,} rows written to {output_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(prog="python -m evidencell.kg_query")
    sub = parser.add_subparsers(dest="cmd")

    fetch_p = sub.add_parser("fetch", help="Fetch taxonomy JSON from KG via Cypher")
    fetch_p.add_argument("cypher_file", help="Path to .cypher file")
    fetch_p.add_argument("taxonomy_id", help="Taxonomy ID (e.g. CCN20230722)")
    fetch_p.add_argument(
        "--bolt-url", default=None,
        help=f"Neo4j bolt URL (default: {DEFAULT_BOLT_URL} or NEO4J_BOLT_URL env)"
    )
    fetch_p.add_argument("--user", default=None, help="Neo4j user (or NEO4J_USER env)")
    fetch_p.add_argument("--password", default=None, help="Neo4j password (or NEO4J_PASSWORD env)")

    args = parser.parse_args()
    if args.cmd == "fetch":
        _cmd_fetch(args.cypher_file, args.taxonomy_id, args.bolt_url, args.user, args.password)
    else:
        parser.print_help()
        sys.exit(1)
