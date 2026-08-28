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

NOISE = re.compile(
    r"^(?:prix|price|exam|examen|retake|practice exam|final exam|membre|member|"
    r"non[- ]?member|non[- ]?membre|total|https?://|\d|[$€£])",
    re.I,
)
DETAIL = re.compile(r"(?:\bCERT\b|\bQUAL\b|\bCOURSE\b|\bBADGE\b|\bEXAM\b|🇫🇷|🇪🇺|🇬🇧|🇺🇸|🌍|🌐)", re.I)
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


def bullet_name(line: str) -> str | None:
    m = BOLD_START.match(line)
    if not m:
        return None
    name = clean(m.group(1))
    low = name.lower().strip()
    if len(name) < 4 or len(name.split()) > 20:
        return None
    if low in GENERIC or NOISE.search(name):
        return None
    # Must look like a named thing, not a price/metadata fragment.
    alpha = re.findall(r"[A-Za-zÀ-ÿ]{2,}", name)
    if not alpha:
        return None
    return name


rows = []
for path in sorted(CERT_DIR.glob("*.md")):
    text = path.read_text(encoding="utf-8")
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
        rows.append((path.name, n, name, key, raw.strip(), path.name in AGGREGATORS, path.name.startswith("entrepreneur")))

by = defaultdict(list)
for r in rows:
    by[r[3]].append(r)

pairs = Counter()
examples = defaultdict(list)
groups = []
for key, group in by.items():
    specialist = [r for r in group if not r[5] and not r[6]]
    files = sorted({r[0] for r in specialist})
    if len(files) < 2:
        continue
    groups.append((key, specialist))
    byfile = {r[0]: r for r in specialist}
    for a, b in itertools.combinations(files, 2):
        pairs[(a, b)] += 1
        if len(examples[(a, b)]) < 6:
            examples[(a, b)].append(byfile[a][2])

groups.sort(key=lambda x: (-len({r[0] for r in x[1]}), x[0]))

out = [
    "# Cross-catalog bullet overlap analysis", "",
    "> Strict companion audit for named credential bullets (`- **Name** — CERT — ...`). Price/metadata bullets are excluded.", "",
    f"- named credential-like bullets scanned: **{len(rows)}**",
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
