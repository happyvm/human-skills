#!/usr/bin/env python3
"""Annotate entry-level geographic scope in mixed certification catalogues.

The file-level `scope: mixed` remains: this tool adds a visible `Portée` column
to credential-oriented Markdown tables and compact labels to credential bullets.

Rules live in metadata/entry-geography-rules.json.

Usage:
    python tools/annotate-entry-geography.py --check
    python tools/annotate-entry-geography.py --sync
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT_DIR = ROOT / "certifications"
RULES_FILE = ROOT / "metadata" / "entry-geography-rules.json"
REPORT_FILE = ROOT / "metadata" / "entry-geography-report.md"

GEO_MARKER_RE = re.compile(r"(?:🇫🇷\s*FR|🇪🇺\s*EUR|🇺🇸\s*US|🇬🇧\s*UK|🇨🇦\s*CA|🇦🇺\s*AU|🌍\s*INT|🌐\s*(?:MIX|REG)|❓\s*UNV)")
TABLE_HEADER_HINTS = {
    "credential", "certification", "certificat", "parcours", "programme",
    "qualification", "designation", "désignation", "titre", "scheme",
    "route", "exam", "examen",
}
SEPARATOR_RE = re.compile(r"^:?-{3,}:?$")


def frontmatter_scope(text: str) -> list[str]:
    if not text.startswith("---\n"):
        return []
    end = text.find("\n---\n", 4)
    if end < 0:
        return []
    fm = text[4:end].splitlines()
    out: list[str] = []
    in_scope = False
    for line in fm:
        if re.match(r"^scope\s*:\s*$", line):
            in_scope = True
            continue
        if in_scope:
            m = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if m:
                out.append(m.group(1).strip().strip("\"'"))
                continue
            if line and not line.startswith(" "):
                break
    return out


def split_row(line: str) -> list[str]:
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")):
        return []
    return [c.strip() for c in s[1:-1].split("|")]


def join_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def is_separator(line: str) -> bool:
    cells = split_row(line)
    return bool(cells) and all(SEPARATOR_RE.match(c.replace(" ", "")) for c in cells)


def normalize_header(cell: str) -> str:
    c = re.sub(r"[`*_]", "", cell).lower()
    c = (
        c.replace("é", "e").replace("è", "e").replace("ê", "e")
         .replace("à", "a").replace("ù", "u").replace("î", "i")
         .replace("ï", "i").replace("ô", "o").replace("ç", "c")
    )
    return c


class Classifier:
    def __init__(self) -> None:
        raw = json.loads(RULES_FILE.read_text(encoding="utf-8"))
        self.rules = []
        for rule in raw["rules"]:
            compiled = [re.compile(p, re.IGNORECASE) for p in rule["patterns"]]
            self.rules.append((rule["scope"], rule["label"], compiled))

    def classify(self, text: str) -> tuple[str, str, str | None]:
        clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        clean = re.sub(r"[`*_]", "", clean)
        for scope, label, patterns in self.rules:
            for pattern in patterns:
                if pattern.search(clean):
                    return scope, label, pattern.pattern
        return "unverified", "❓ UNV", None


def annotate_file(path: Path, classifier: Classifier, sync: bool) -> dict:
    text = path.read_text(encoding="utf-8")
    if "mixed" not in frontmatter_scope(text):
        return {"mixed": False}

    lines = text.splitlines()
    out: list[str] = []
    i = 0
    stats = Counter()
    unverified: list[str] = []

    while i < len(lines):
        if i + 1 < len(lines):
            header = split_row(lines[i])
            if header and is_separator(lines[i + 1]):
                normalized = [normalize_header(x) for x in header]
                candidate = any(any(hint in cell for hint in TABLE_HEADER_HINTS) for cell in normalized)
                if candidate and not any("portee" in cell for cell in normalized):
                    j = i + 2
                    rows = []
                    while j < len(lines):
                        cells = split_row(lines[j])
                        if not cells:
                            break
                        rows.append((lines[j], cells, classifier.classify(" | ".join(cells))))
                        j += 1

                    known = sum(1 for _, _, (scope, _, _) in rows if scope != "unverified")
                    if rows and known:
                        stats["tables"] += 1
                        out.append(join_row(header + ["Portée"]))
                        out.append(join_row(split_row(lines[i + 1]) + [":---:"]))
                        for original, cells, (scope, label, _) in rows:
                            stats["table_rows"] += 1
                            stats[f"scope:{scope}"] += 1
                            if scope == "unverified":
                                unverified.append(original.strip())
                            out.append(join_row(cells + [label]))
                        i = j
                        continue

        stripped = lines[i].lstrip()
        if stripped.startswith(("- ", "* ")) and ("**" in stripped or re.search(r"\b(?:CERT|QUAL|ACC|REG|COURSE|ORG)\b", stripped)):
            scope, label, _ = classifier.classify(stripped)
            if scope != "unverified" and not GEO_MARKER_RE.search(stripped):
                stats["bullets"] += 1
                stats[f"scope:{scope}"] += 1
                out.append(lines[i] + f" — {label}")
                i += 1
                continue

        out.append(lines[i])
        i += 1

    new_text = "\n".join(out) + ("\n" if text.endswith("\n") else "")
    changed = new_text != text
    if sync and changed:
        path.write_text(new_text, encoding="utf-8")

    stats["changed"] = int(changed)
    stats["unverified"] = len(unverified)
    return {"mixed": True, "changed": changed, "stats": dict(stats), "unverified_rows": unverified}


def build_report(results: dict[str, dict]) -> str:
    total = Counter()
    lines = [
        "# Entry-level geography report", "",
        "> Generated by `tools/annotate-entry-geography.py`.", "",
        "| Catalogue | Tables | Rows | Bullets | UNV |",
        "|---|---:|---:|---:|---:|",
    ]
    for path, result in sorted(results.items()):
        if not result.get("mixed"):
            continue
        s = Counter(result["stats"])
        total.update(s)
        lines.append(f"| `{path}` | {s['tables']} | {s['table_rows']} | {s['bullets']} | {s['unverified']} |")

    lines += [
        "", "## Totaux", "",
        f"- catalogues `mixed` analysés : **{sum(1 for r in results.values() if r.get('mixed'))}** ;",
        f"- tableaux credential annotés : **{total['tables']}** ;",
        f"- lignes de tableaux annotées : **{total['table_rows']}** ;",
        f"- bullets credential annotés : **{total['bullets']}** ;",
        f"- lignes restant `❓ UNV` : **{total['unverified']}**.",
        "", "### Répartition des labels appliqués", "",
    ]
    for key, value in sorted((k, v) for k, v in total.items() if k.startswith("scope:")):
        lines.append(f"- `{key.split(':', 1)[1]}` : **{value}**")

    uv = []
    for path, result in sorted(results.items()):
        for row in result.get("unverified_rows", []):
            uv.append((path, row))
    lines += ["", "## Lignes `❓ UNV` à vérifier", ""]
    if not uv:
        lines.append("Aucune.")
    else:
        for path, row in uv:
            compact = row.replace("|", r"\|")
            lines.append(f"- `{path}` — `{compact}`")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--sync", action="store_true")
    args = parser.parse_args()

    classifier = Classifier()
    results = {}
    for path in sorted(CERT_DIR.glob("*.md")):
        results[str(path.relative_to(ROOT))] = annotate_file(path, classifier, sync=args.sync)

    report = build_report(results)
    if args.sync:
        REPORT_FILE.write_text(report, encoding="utf-8")

    changed = [p for p, r in results.items() if r.get("changed")]
    unverified = sum(r.get("stats", {}).get("unverified", 0) for r in results.values())
    print(f"mixed={sum(1 for r in results.values() if r.get('mixed'))}")
    print(f"changed={len(changed)}")
    print(f"unverified={unverified}")

    if args.check and changed:
        print("Files need entry-geography sync:")
        for p in changed:
            print(f" - {p}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
