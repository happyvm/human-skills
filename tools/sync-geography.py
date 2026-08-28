#!/usr/bin/env python3
"""Validate or sync geographic scope metadata for human-skills catalogues.

The registry in metadata/geography.yml is the fallback for legacy files.
This script deliberately uses only the Python standard library.

Usage:
    python tools/sync-geography.py --check
    python tools/sync-geography.py --sync
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "metadata" / "geography.yml"
CERT_DIR = ROOT / "certifications"

ALLOWED = {
    "unverified",
    "international",
    "europe",
    "france",
    "national-us",
    "national-uk",
    "national-ca",
    "national-au",
    "national-nz",
    "national-de",
    "national-sg",
    "regional",
    "mixed",
}

PATH_RE = re.compile(r'^\s{2}"(certifications/[^"]+\.md)":\s*$')
SCOPE_RE = re.compile(r'^\s{6}-\s+([a-z0-9-]+)\s*$')


def load_registry() -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    current: str | None = None
    in_scope = False

    for raw in REGISTRY.read_text(encoding="utf-8").splitlines():
        path_match = PATH_RE.match(raw)
        if path_match:
            current = path_match.group(1)
            mapping[current] = []
            in_scope = False
            continue

        if current and raw.strip() == "scope:":
            in_scope = True
            continue

        if current and in_scope:
            scope_match = SCOPE_RE.match(raw)
            if scope_match:
                mapping[current].append(scope_match.group(1))
                continue
            if raw.strip() and not raw.startswith("      "):
                in_scope = False

    return mapping


def split_frontmatter(text: str) -> tuple[list[str], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML frontmatter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("unterminated YAML frontmatter") from exc
    return lines[1:end], lines[end + 1 :]


def get_scope(front: list[str]) -> list[str]:
    values: list[str] = []
    for i, line in enumerate(front):
        if line.strip() == "scope:":
            j = i + 1
            while j < len(front):
                m = re.match(r'^\s{2}-\s+(.+?)\s*$', front[j])
                if not m:
                    break
                values.append(m.group(1))
                j += 1
            break
    return values


def replace_list_field(front: list[str], key: str, values: list[str], before: str | None = None) -> list[str]:
    start = None
    end = None
    for i, line in enumerate(front):
        if line.strip() == f"{key}:":
            start = i
            end = i + 1
            while end < len(front) and re.match(r'^\s{2}-\s+', front[end]):
                end += 1
            break

    block = [f"{key}:"] + [f"  - {v}" for v in values]
    if start is not None and end is not None:
        return front[:start] + block + front[end:]

    if before:
        for i, line in enumerate(front):
            if line.strip() == f"{before}:":
                return front[:i] + block + front[i:]

    return front + block


def sync_text(text: str, scopes: list[str]) -> str:
    front, body = split_frontmatter(text)
    front = replace_list_field(front, "scope", scopes, before="tags")

    # Keep scope tags aligned with the structured field.
    tags: list[str] = []
    tag_start = None
    tag_end = None
    for i, line in enumerate(front):
        if line.strip() == "tags:":
            tag_start = i
            tag_end = i + 1
            while tag_end < len(front):
                m = re.match(r'^\s{2}-\s+(.+?)\s*$', front[tag_end])
                if not m:
                    break
                tags.append(m.group(1))
                tag_end += 1
            break

    tags = [t for t in tags if not t.startswith("scope/")]
    tags.extend(f"scope/{s}" for s in scopes)
    if tag_start is not None and tag_end is not None:
        front = front[:tag_start] + ["tags:"] + [f"  - {t}" for t in tags] + front[tag_end:]

    return "---\n" + "\n".join(front) + "\n---\n" + "\n".join(body) + ("\n" if text.endswith("\n") else "")


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--sync", action="store_true")
    args = parser.parse_args()

    registry = load_registry()
    disk_paths = {f"certifications/{p.name}" for p in CERT_DIR.glob("*.md")}
    reg_paths = set(registry)

    problems: list[str] = []
    missing = sorted(disk_paths - reg_paths)
    stale = sorted(reg_paths - disk_paths)
    if missing:
        problems.append("missing from registry: " + ", ".join(missing))
    if stale:
        problems.append("registry entries without file: " + ", ".join(stale))

    for path, scopes in registry.items():
        if not scopes:
            problems.append(f"{path}: empty scope")
        for value in scopes:
            if value not in ALLOWED and not value.startswith("national-"):
                problems.append(f"{path}: invalid scope {value!r}")

    changed = 0
    explicit = 0
    fallback = 0
    for rel in sorted(disk_paths & reg_paths):
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        try:
            front, _ = split_frontmatter(text)
        except ValueError as exc:
            problems.append(f"{rel}: {exc}")
            continue

        current = get_scope(front)
        if current and current != ["unverified"]:
            explicit += 1
        else:
            fallback += 1

        if args.sync:
            new_text = sync_text(text, registry[rel])
            if new_text != text:
                path.write_text(new_text, encoding="utf-8")
                changed += 1

    counts = Counter(v for values in registry.values() for v in values)
    print(f"catalogues: {len(registry)}")
    print("scope counts:", ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print(f"frontmatter explicit={explicit}, registry fallback={fallback}")
    if args.sync:
        print(f"files changed={changed}")

    if problems:
        for problem in problems:
            print("ERROR:", problem)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
