#!/usr/bin/env python3
"""Validate the Unwatched dataset.

Checks that data/brands.yaml is well-formed, that every brand points at a doc that exists,
that every telemetry host named in the dataset also appears in the blocklist, and that the
blocklist has no duplicates or obvious typos.

Run:  python3 tools/validate.py
Exit: 0 clean, 1 problems found.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRANDS = ROOT / "data" / "brands.yaml"
BLOCKLIST = ROOT / "network" / "dns-blocklist.txt"

HOSTNAME_RE = re.compile(r"^(?=.{1,253}$)([a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}$")
VALID_CONFIDENCE = {"high", "medium", "low"}

problems: list[str] = []
notes: list[str] = []


def fail(msg: str) -> None:
    problems.append(msg)


def load_yaml(path: Path):
    try:
        import yaml  # type: ignore
    except ImportError:
        notes.append(
            "PyYAML not installed — ran structural checks only. "
            "For full validation: python3 -m venv .venv && .venv/bin/pip install pyyaml"
        )
        return None
    try:
        return yaml.safe_load(path.read_text())
    except Exception as exc:  # noqa: BLE001
        fail(f"{path.name}: YAML does not parse: {exc}")
        return None


def parse_blocklist(path: Path) -> tuple[set[str], list[str]]:
    """Return (active hosts, commented-out hosts)."""
    active: set[str] = set()
    commented: list[str] = []
    seen: set[str] = set()
    for lineno, raw in enumerate(path.read_text().splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            body = line.lstrip("#").strip().split()
            if body and HOSTNAME_RE.match(body[0]):
                commented.append(body[0])
            continue
        host = line.split("#")[0].strip()
        if not host:
            continue
        if not HOSTNAME_RE.match(host):
            fail(f"{path.name}:{lineno}: not a valid hostname: {host!r}")
            continue
        if host in seen:
            fail(f"{path.name}:{lineno}: duplicate entry: {host}")
        seen.add(host)
        active.add(host)
    return active, commented


def main() -> int:
    if not BRANDS.exists():
        fail("data/brands.yaml is missing")
    if not BLOCKLIST.exists():
        fail("network/dns-blocklist.txt is missing")
    if problems:
        report()
        return 1

    active, commented = parse_blocklist(BLOCKLIST)
    print(f"blocklist: {len(active)} active hosts, {len(commented)} documented-but-not-blocked")

    data = load_yaml(BRANDS)
    if data is None:
        report()
        return 1 if problems else 0

    brands = data.get("brands") or []
    if not brands:
        fail("data/brands.yaml: no brands defined")

    ids: set[str] = set()
    for b in brands:
        bid = b.get("id", "<missing id>")
        if bid in ids:
            fail(f"brands.yaml: duplicate brand id {bid!r}")
        ids.add(bid)

        for field in ("id", "name", "os", "doc", "confidence"):
            if not b.get(field):
                fail(f"brands.yaml[{bid}]: missing required field {field!r}")

        conf = b.get("confidence")
        if conf and conf not in VALID_CONFIDENCE:
            fail(f"brands.yaml[{bid}]: confidence {conf!r} not in {sorted(VALID_CONFIDENCE)}")

        doc = b.get("doc")
        if doc and not (ROOT / doc).exists():
            fail(f"brands.yaml[{bid}]: doc {doc!r} does not exist")

        for host in b.get("telemetry_hosts") or []:
            if not HOSTNAME_RE.match(host):
                fail(f"brands.yaml[{bid}]: invalid hostname {host!r}")
            elif host not in active and host not in commented:
                fail(
                    f"brands.yaml[{bid}]: telemetry host {host!r} is not in the blocklist. "
                    "Add it, or comment it there with a reason."
                )

    print(f"brands: {len(brands)} entries, {sum(1 for b in brands if b.get('confidence') == 'low')} low-confidence")

    orphans = sorted(
        h for h in active
        if not any(h in (b.get("telemetry_hosts") or []) for b in brands)
    )
    if orphans:
        print(f"note: {len(orphans)} blocklist hosts are not attributed to a brand "
              "(expected for third-party trackers)")

    report()
    return 1 if problems else 0


def report() -> None:
    for n in notes:
        print(f"NOTE: {n}")
    if problems:
        print(f"\n{len(problems)} problem(s):", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
    else:
        print("\nOK — dataset is consistent.")


if __name__ == "__main__":
    sys.exit(main())
