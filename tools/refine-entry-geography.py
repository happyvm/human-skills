#!/usr/bin/env python3
"""Resolve second-pass UNV geography labels in already annotated mixed catalogues."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT_DIR = ROOT / "certifications"
OVERRIDES = ROOT / "metadata" / "entry-geography-overrides.json"
REPORT = ROOT / "metadata" / "entry-geography-report.md"

LABELS = [
    "🇫🇷 FR", "🇪🇺 EUR", "🇺🇸 US", "🇬🇧 UK", "🇨🇦 CA", "🇦🇺 AU", "🇸🇬 SG",
    "🌍 INT · US std", "🌍 INT · US-centric", "🌍 INT · UK-origin",
    "🌍 INT · DE-origin", "🌍 INT", "🌐 MIX", "🌐 REG", "❓ UNV",
]


def frontmatter_mixed(text: str) -> bool:
    if not text.startswith("---\n"):
        return False
    end = text.find("\n---\n", 4)
    if end < 0:
        return False
    return bool(re.search(r"(?m)^scope:\s*\n(?:\s+-\s+.*\n)*\s+-\s+mixed\s*$", text[4:end]))


def split_row(line: str) -> list[str]:
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")):
        return []
    return [c.strip() for c in s[1:-1].split("|")]


def join_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def load_rules():
    raw = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    out = []
    for rule in raw["overrides"]:
        out.append((rule["label"], [re.compile(p, re.I) for p in rule["patterns"]]))
    return out


def resolve(text: str, rules) -> str | None:
    clean = re.sub(r"[`*_]", "", text)
    for label, patterns in rules:
        if any(p.search(clean) for p in patterns):
            return label
    return None


def refine_file(path: Path, rules, sync: bool) -> tuple[bool, list[str]]:
    text = path.read_text(encoding="utf-8")
    if not frontmatter_mixed(text):
        return False, []
    lines = text.splitlines()
    changed = False
    unresolved = []
    for idx, line in enumerate(lines):
        cells = split_row(line)
        if cells and cells[-1] == "❓ UNV":
            label = resolve(" | ".join(cells[:-1]), rules)
            if label:
                cells[-1] = label
                lines[idx] = join_row(cells)
                changed = True
            else:
                unresolved.append(line.strip())
    if sync and changed:
        path.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")
    return changed, unresolved


def scan_report() -> str:
    rows = []
    total = Counter()
    unresolved = []
    for path in sorted(CERT_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not frontmatter_mixed(text):
            continue
        lines = text.splitlines()
        tables = table_rows = bullets = unv = 0
        i = 0
        while i < len(lines):
            cells = split_row(lines[i])
            if cells and "Portée" in cells and i + 1 < len(lines):
                tables += 1
                i += 2
                while i < len(lines):
                    rcells = split_row(lines[i])
                    if not rcells:
                        break
                    table_rows += 1
                    label = rcells[-1]
                    total[label] += 1
                    if label == "❓ UNV":
                        unv += 1
                        unresolved.append((str(path.relative_to(ROOT)), lines[i].strip()))
                    i += 1
                continue
            if lines[i].lstrip().startswith(("- ", "* ")):
                for label in LABELS:
                    if label in lines[i]:
                        bullets += 1
                        total[label] += 1
                        if label == "❓ UNV":
                            unv += 1
                            unresolved.append((str(path.relative_to(ROOT)), lines[i].strip()))
                        break
            i += 1
        rows.append((str(path.relative_to(ROOT)), tables, table_rows, bullets, unv))

    out = [
        "# Entry-level geography report", "",
        "> Generated after the refinement pass.", "",
        "| Catalogue | Tables | Rows | Bullets | UNV |",
        "|---|---:|---:|---:|---:|",
    ]
    for p, t, r, b, u in rows:
        out.append(f"| `{p}` | {t} | {r} | {b} | {u} |")
    out += ["", "## Totaux", ""]
    out.append(f"- catalogues `mixed` analysés : **{len(rows)}** ;")
    out.append(f"- tableaux avec colonne `Portée` : **{sum(r[1] for r in rows)}** ;")
    out.append(f"- lignes credential annotées : **{sum(r[2] for r in rows)}** ;")
    out.append(f"- bullets credential annotés : **{sum(r[3] for r in rows)}** ;")
    out.append(f"- entrées restant `❓ UNV` : **{sum(r[4] for r in rows)}**.")
    out += ["", "### Répartition visible", ""]
    for label, count in sorted(total.items()):
        out.append(f"- `{label}` : **{count}**")
    out += ["", "## Entrées `❓ UNV` à vérifier", ""]
    if unresolved:
        for p, line in unresolved:
            out.append(f"- `{p}` — `{line.replace('|', r'\|')}`")
    else:
        out.append("Aucune.")
    return "\n".join(out) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sync", action="store_true")
    args = parser.parse_args()
    rules = load_rules()
    changed = 0
    unresolved = 0
    for path in sorted(CERT_DIR.glob("*.md")):
        ch, uv = refine_file(path, rules, args.sync)
        changed += int(ch)
        unresolved += len(uv)
    if args.sync:
        REPORT.write_text(scan_report(), encoding="utf-8")
    print(f"changed={changed}")
    print(f"unresolved={unresolved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
