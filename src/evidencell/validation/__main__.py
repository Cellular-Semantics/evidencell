"""CLI entry for the validation framework.

Dispatches to the appropriate audit driver and writes the run artifact
under ``research/validation/methods_audits/<audit_id>/runs/``.
"""

from __future__ import annotations

import argparse
import sys

from .at_blind import ATBlindAudit
from .base import AuditAssertion


def _print_summary(run, top_k: int) -> None:
    print()
    print("=" * 64)
    print(f"AUDIT SUMMARY  audit_id={run.audit_id}  commit={run.commit[:8]}")
    print("=" * 64)
    stats = run.summary_stats
    n = stats.get("n_cases", 0)
    if not n:
        print("  No test cases collected.")
        return
    pr = stats.get("pass_rate")
    pr_pct = f"{100 * pr:.1f}%" if pr is not None else "—"
    print(f"  n={n}  pass={stats['pass_count']}  pass_rate={pr_pct}  top_k={top_k}")
    print("  Outcomes by reason:")
    for reason, count in sorted(
        stats.get("by_reason", {}).items(), key=lambda kv: -kv[1]
    ):
        pct = 100 * count / n if n else 0
        print(f"    {reason:30s}  {count:4d}  ({pct:5.1f}%)")
    by_level = stats.get("by_level")
    if by_level:
        print("  Outcomes by AT level:")
        for level, subcounts in sorted(by_level.items()):
            ln = subcounts.get("n", 0)
            lp = subcounts.get("pass_count", 0)
            lpr = (100 * lp / ln) if ln else 0
            print(f"    {level:30s}  n={ln:4d}  pass={lp:4d}  ({lpr:5.1f}%)")
    by_mono = stats.get("by_monotonicity")
    if by_mono:
        print("  Outcomes by AT F1 monotonicity (source-label purity diagnostic):")
        for tag, subcounts in sorted(by_mono.items()):
            ln = subcounts.get("n", 0)
            lp = subcounts.get("pass_count", 0)
            lpr = (100 * lp / ln) if ln else 0
            print(f"    {tag:30s}  n={ln:4d}  pass={lp:4d}  ({lpr:5.1f}%)")
    region_fb = stats.get("region_descendant_fallback_hits")
    if region_fb is not None:
        print(f"  Region filter: {region_fb} candidate(s) survived via "
              f"rank-0-descendant anat fallback (BCKG workaround).")


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="python -m evidencell.validation",
        description="Run an evidencell validation/audit driver.",
    )
    sub = parser.add_subparsers(dest="audit", required=True)

    # at-blind
    p_atb = sub.add_parser(
        "at-blind",
        help="AT-blind audit: would marker+region+NT alone surface the "
             "candidates that annotation transfer has already identified?",
    )
    p_atb.add_argument("--taxonomy", default="CCN20230722")
    p_atb.add_argument("--top-k", type=int, default=10)
    p_atb.add_argument(
        "--f1-floor", type=float, default=0.5,
        help="Only emit (level × target) test cases whose AT F1 ≥ this. "
             "Default 0.5 — candidates worth investigating. Lower it to "
             "audit weaker mappings.",
    )
    p_atb.add_argument("--limit", type=int, default=None)
    p_atb.add_argument(
        "--force-preflight", action="store_true",
        help="Continue even if a preflight invariant fails (records the "
             "skip in the run artifact). Use sparingly.",
    )

    args = parser.parse_args()

    if args.audit == "at-blind":
        audit = ATBlindAudit(
            taxonomy_id=args.taxonomy,
            top_k=args.top_k,
            f1_floor=args.f1_floor,
            limit=args.limit,
            force_preflight=args.force_preflight,
        )
        try:
            run = audit.run()
        except AuditAssertion as exc:
            print(f"PREFLIGHT FAILED: {exc}", file=sys.stderr)
            return 2
        _print_summary(run, top_k=args.top_k)
        print()
        print(
            f"Run artifact: research/validation/methods_audits/"
            f"{audit.audit_id}/runs/  (latest.json updated)"
        )
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
