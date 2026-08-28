#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import itertools
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
CERT_DIR = ROOT / "certifications"
REPORT = ROOT / "metadata" / "catalog-bullet-overlap-analysis.md"

AGGREGATORS = {
    "free-it.md", "free-non-it.md", "paid-under-500.md", "paid-over-500.md",
    "tools-platforms-under-500.md", "business-finance-under-500.md",
}

GENERIC = {
    "associate", "professional", "specialist", "expert", "foundational",
    "practitioner", "registered", "total", "certification", "course",
    "resource", "programme", "program", "formation", "credential",
}

DETAIL = re.compile(r"(?:\bCERT\b|\bQUAL\b|\bCOURSE\b|\bBADGE\b|\bEXAM\b|€|\$|£|🇫🇷|🇪🇺|🇬🇧|🇺🇸|🌍|🌐)", re.I)
BOLD_START = re.compile(r"^-\s+\*\*(.+?)\*\*")
LINK = re.compile(r"\[([^\]]+)\]\([^\)]+\)")


def clean(s: str) -> str:
    s = LINK.sub(r"\1", s)
    s = re.sub(r"[*_`~]", "", s)
    s = s.replace("®", "").replace("™", "")
    return re.sub(r"\s+", " ", s).strip()


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", clean(s))
    s = "".join(ch for ch in s if not unicodedata.combining(ch)).lower()
    s = re.sub(r"\b(?:certification|certificate|certified|credential|qualification)\b", " ", s)
    s = re.sub(r"\b(?:2024|2025|2026|2027)\b", " ", s)
    s = re.sub(r"[^a-z0-9+#./ -]+", " ", s)
    return re.sub(r"\s+", " ", s).strip(" -./")


def domains(text: str) -> tuple[str, ...]:
    if not text.startswith("---\n"):
        return ()
    end = text.find("\n---", 4)
    if end < 0:
        return ()
    out = []
    active = False
    for line in text[4:end].splitlines():
        if re.match(r"^domain\s*:\s*$", line):
            active = True
            continue
        if active:
            m = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if m:
                out.append(m.group(1).strip('"\''))
            elif line and not line.startswith(" "):
                break
    return tuple(out)


def bullet_name(line: str) -> str | None:
    m = BOLD_START.match(line)
    if m:
        return clean(m.group(1))
    if not line.startswith("- "):
        return None
    body = clean(line[2:])
    # Credential bullets in this repo usually put the name before an em dash.
    first = re.split(r"\s+[—–]\s+", body, maxsplit=1)[0].strip()
    if len(first) < 5 or len(first.split()) > 18:
        return None
    return first


rows = []
for path in sorted(CERT_DIR.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    ds = domains(text)
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line.startswith("- ") or not DETAIL.search(line):
            continue
        name = bullet_name(line)
        if not name:
            continue
        key = norm(name)
        if len(key) < 4 or key in GENERIC:
            continue
        rows.append((path.name, n, name, key, raw.strip(), ds, path.name in AGGREGATORS, path.name.startswith("entrepreneur")))

by = defaultdict(list)
for r in rows:
    by[r[3]].append(r)

pairs = Counter()
examples = defaultdict(list)
groups = []
for key, group in by.items():
    files = sorted({r[0] for r in group})
    if len(files) < 2:
        continue
    specialist = [r for r in group if not r[6] and not r[7]]
    specialist_files = sorted({r[0] for r in specialist})
    if len(specialist_files) < 2:
        continue
    groups.append((key, specialist))
    byfile = {r[0]: r for r in specialist}
    for a, b in itertools.combinations(specialist_files, 2):
        pairs[(a, b)] += 1
        if len(examples[(a, b)]) < 6:
            examples[(a, b)].append(byfile[a][2])

groups.sort(key=lambda x: (-len({r[0] for r in x[1]}), x[0]))

out = [
    "# Cross-catalog bullet overlap analysis", "",
    "> Companion audit for credential bullets (`- **Name** — CERT — ...`).", "",
    f"- credential-like bullets scanned: **{len(rows)}**",
    f"- specialist duplicate bullet groups: **{len(groups)}**",
    f"- specialist file pairs with bullet overlap: **{len(pairs)}**",
    "",
    "## Highest-overlap specialist pairs", "",
    "| Shared bullets | Catalogue A | Catalogue B | Examples |",
    "|---:|---|---|---|",
]
for (a, b), count in pairs.most_common(40):
    out.append(f"| {count} | `{a}` | `{b}` | {', '.join(examples[(a,b)])} |")
if not pairs:
    out.append("| 0 | — | — | — |")

out += ["", "## Duplicate bullet groups", ""]
for key, group in groups[:120]:
    out.append(f"### {group[0][2]}")
    out.append("")
    for r in group:
        out.append(f"- `{r[0]}:{r[1]}` — `{r[4]}`")
    out.append("")
if not groups:
    out += ["Aucun.", ""]

REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
print("\n".join(out[:100]))
print(f"\nFull report: {REPORT.relative_to(ROOT)}")
