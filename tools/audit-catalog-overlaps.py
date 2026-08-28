#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
import itertools
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
CERT_DIR = ROOT / "certifications"
REPORT = ROOT / "metadata" / "catalog-overlap-analysis.md"

# These files are intentionally broad aggregators. Repetition between an
# aggregator and a specialist catalogue is useful navigation, not necessarily
# a structural duplicate.
AGGREGATORS = {
    "free-it.md",
    "free-non-it.md",
    "paid-under-500.md",
    "paid-over-500.md",
    "tools-platforms-under-500.md",
    "business-finance-under-500.md",
}

# Entrepreneur / Group Management already has explicit canonical ownership.
# We still scan it for repository totals, but do not use it to rank the next
# cleanup domains.
ALREADY_GOVERNED_PREFIXES = ("entrepreneur",)

HEADER_WORDS = {
    "credential", "certification", "qualification", "certifications",
    "parcours", "programme", "program", "formation", "badge", "exam",
    "examen", "nom", "name", "produit", "product", "niveau", "level",
    "fonction", "function", "besoin", "domaine", "domain", "famille",
    "category", "categorie", "axe", "usage", "sujet", "solution",
    "certification / qualification", "credential / parcours",
}

GENERIC_CELLS = {
    "cloud", "cybersecurity", "cyber", "networking", "network", "storage",
    "database", "data", "finance", "risk", "management", "project",
    "marketing", "sales", "security", "governance", "compliance", "audit",
    "quality", "rh", "hr", "insurance", "sustainability", "esg",
    "construction", "btp", "linux", "windows", "ai", "ml", "devops",
    "observability", "business", "architecture", "platform", "vendor",
    "associate", "professional", "specialist", "expert", "foundational",
    "practitioner", "registered", "total", "prix officiel",
}

DETAIL_SIGNAL = re.compile(
    r"(?:\bCERT\b|\bQUAL\b|\bCOURSE\b|\bBADGE\b|\bEXAM\b|\bRESOURCE\b|"
    r"\bAID\b|\bREG\b|€|\$|£|CAD|AUD|CHF|JPY|provider-dependent|sur devis|"
    r"FREE|gratuit|renew|validit|prereq|prérequis|🇫🇷|🇪🇺|🇬🇧|🇺🇸|🌍|🌐)",
    re.IGNORECASE,
)

MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^\)]+\)")
EMOJI_SCOPE_RE = re.compile(r"[🇦-🇿]{2}|🌍|🌐|❓")
PRICE_RE = re.compile(r"(?:^|\s)(?:\d+[\d\s.,]*\s*(?:€|\$|£|CAD|AUD|CHF)|(?:€|\$|£)\s*\d+)", re.I)

@dataclass(frozen=True)
class Entry:
    file: str
    line: int
    raw: str
    name: str
    norm: str
    domains: tuple[str, ...]
    aggregator: bool
    governed: bool


def clean_md(text: str) -> str:
    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    text = re.sub(r"[*_`~]", "", text)
    text = text.replace("®", "").replace("™", "")
    text = EMOJI_SCOPE_RE.sub("", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize(text: str) -> str:
    text = clean_md(text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    text = re.sub(r"\b(?:certification|certificate|certified|credential|qualification|exam|examen)\b", " ", text)
    text = re.sub(r"\b(?:2024|2025|2026|2027)\b", " ", text)
    text = re.sub(r"[^a-z0-9+#./ -]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip(" -./")
    return text


def parse_domains(text: str) -> tuple[str, ...]:
    if not text.startswith("---\n"):
        return ()
    end = text.find("\n---", 4)
    if end < 0:
        return ()
    fm = text[4:end].splitlines()
    domains: list[str] = []
    in_domain = False
    for line in fm:
        if re.match(r"^domain\s*:\s*$", line):
            in_domain = True
            continue
        if in_domain:
            m = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if m:
                domains.append(m.group(1).strip('"\''))
                continue
            if line and not line.startswith(" "):
                break
    return tuple(domains)


def split_row(line: str) -> list[str]:
    return [clean_md(c) for c in line.strip().strip("|").split("|")]


def is_separator(line: str) -> bool:
    return bool(re.fullmatch(r"\|?[\s:|-]+\|?", line.strip()))


def is_header_row(cells: list[str]) -> bool:
    low = {c.lower().strip() for c in cells}
    if low & HEADER_WORDS:
        # A real credential can contain one of these words, but a row where
        # several cells are headers is overwhelmingly a table header.
        headerish = sum(1 for c in low if c in HEADER_WORDS or c in {"coût", "cout", "prix", "tco", "portée", "portee", "nature", "statut", "status", "utilité", "pertinence"})
        return headerish >= 2
    return False


def looks_like_name(cell: str) -> bool:
    c = clean_md(cell)
    low = c.lower().strip()
    if not c or low in HEADER_WORDS or low in GENERIC_CELLS:
        return False
    if len(c) < 4:
        return False
    if PRICE_RE.search(c) and len(re.sub(PRICE_RE, "", c).strip()) < 5:
        return False
    if re.fullmatch(r"[\d\s.,%+\-/]+", c):
        return False
    if low in {"cert", "qual", "course", "badge", "resource", "aid", "reg", "route", "legacy"}:
        return False
    return bool(re.search(r"[A-Za-zÀ-ÿ]", c))


def choose_name(cells: list[str]) -> str | None:
    # Most tables put the credential in col 1. Some use col 1 as a function
    # and col 2 as the credential. Score the first three cells and choose the
    # most credential-like one.
    candidates = []
    for idx, cell in enumerate(cells[:3]):
        if not looks_like_name(cell):
            continue
        low = cell.lower().strip()
        score = 10 - idx
        if any(tok in low for tok in ["rs", "rncp", "aws", "azure", "cisco", "oracle", "microsoft", "google", "ibm", "red hat", "vmware", "veeam", "cfa", "pmi", "isc2", "isaca", "comptia", "cncf", "linux foundation", "certified", "certificate", "professional", "associate", "expert", "specialist", "administrator", "engineer", "architect", "foundation", "practitioner", "diploma"]):
            score += 5
        if low in GENERIC_CELLS:
            score -= 10
        if low in {"fonction", "besoin", "usage", "domaine", "famille", "axe", "sujet"}:
            score -= 20
        candidates.append((score, idx, cell))
    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][2]


def collect_entries() -> list[Entry]:
    entries: list[Entry] = []
    for path in sorted(CERT_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        domains = parse_domains(text)
        aggregator = path.name in AGGREGATORS
        governed = path.name.startswith(ALREADY_GOVERNED_PREFIXES)
        for lineno, raw in enumerate(text.splitlines(), 1):
            line = raw.strip()
            if not (line.startswith("|") and line.endswith("|")) or is_separator(line):
                continue
            cells = split_row(line)
            if is_header_row(cells):
                continue
            if len(cells) < 2:
                continue
            # Focus on rows that look like actual catalogue rows rather than
            # status/watchlist tables.
            if not DETAIL_SIGNAL.search(line):
                continue
            name = choose_name(cells)
            if not name:
                continue
            norm = normalize(name)
            if len(norm) < 4 or norm in GENERIC_CELLS:
                continue
            entries.append(Entry(path.name, lineno, line, name, norm, domains, aggregator, governed))
    return entries


def near_key(norm: str) -> set[str]:
    stop = {"the", "and", "of", "in", "for", "de", "du", "des", "et", "la", "le", "les", "level", "niveau"}
    return {t for t in re.split(r"[^a-z0-9+#]+", norm) if len(t) >= 2 and t not in stop}


def main() -> None:
    entries = collect_entries()
    by_norm: dict[str, list[Entry]] = defaultdict(list)
    for e in entries:
        by_norm[e.norm].append(e)

    exact_groups = []
    for norm, group in by_norm.items():
        files = {e.file for e in group}
        if len(files) >= 2:
            exact_groups.append((norm, group))
    exact_groups.sort(key=lambda x: (-len({e.file for e in x[1]}), x[0]))

    pair_counts = Counter()
    pair_examples: dict[tuple[str, str], list[str]] = defaultdict(list)
    specialist_pair_counts = Counter()
    domain_pair_counts = Counter()

    for norm, group in exact_groups:
        unique_by_file: dict[str, Entry] = {}
        for e in group:
            unique_by_file.setdefault(e.file, e)
        for a, b in itertools.combinations(sorted(unique_by_file), 2):
            pair = (a, b)
            pair_counts[pair] += 1
            if len(pair_examples[pair]) < 8:
                pair_examples[pair].append(unique_by_file[a].name)
            ea, eb = unique_by_file[a], unique_by_file[b]
            if not ea.aggregator and not eb.aggregator and not ea.governed and not eb.governed:
                specialist_pair_counts[pair] += 1
                da = ea.domains[0] if ea.domains else "unclassified"
                db = eb.domains[0] if eb.domains else "unclassified"
                domain_pair_counts[tuple(sorted((da, db)))] += 1

    # Conservative near-duplicate detection among specialist entries only.
    unique_specialist = {}
    for e in entries:
        if e.aggregator or e.governed:
            continue
        unique_specialist.setdefault((e.file, e.norm), e)
    spec = list(unique_specialist.values())
    near = []
    for i, a in enumerate(spec):
        ta = near_key(a.norm)
        if len(ta) < 2:
            continue
        for b in spec[i + 1:]:
            if a.file == b.file or a.norm == b.norm:
                continue
            tb = near_key(b.norm)
            if len(tb) < 2:
                continue
            inter = len(ta & tb)
            union = len(ta | tb)
            if not union:
                continue
            jacc = inter / union
            if jacc < 0.75:
                continue
            ratio = SequenceMatcher(None, a.norm, b.norm).ratio()
            if ratio < 0.90:
                continue
            near.append((ratio, jacc, a, b))
    near.sort(key=lambda x: (-x[0], -x[1], x[2].name.lower()))

    file_entry_counts = Counter(e.file for e in entries)
    domain_entry_counts = Counter(d for e in entries for d in (e.domains or ("unclassified",)))

    out = [
        "# Cross-catalog overlap analysis",
        "",
        "> Heuristic audit of Markdown catalogue tables. Exact matches are strong signals; near matches are review candidates, not automatic duplicates.",
        "",
        f"- catalogues scanned: **{len({e.file for e in entries})}**",
        f"- credential-like table rows scanned: **{len(entries)}**",
        f"- exact normalized names present in 2+ files: **{len(exact_groups)}**",
        f"- specialist↔specialist file pairs with exact overlap: **{len(specialist_pair_counts)}**",
        f"- conservative near-duplicate candidates: **{len(near)}**",
        "",
        "## Interpretation",
        "",
        "- `free-it.md`, `free-non-it.md`, `paid-under-500.md`, `paid-over-500.md` are treated as intentional aggregators.",
        "- `entrepreneur*` catalogues are excluded from cleanup ranking because canonical ownership is already enforced separately.",
        "- A specialist↔specialist overlap is the main signal for the next dedup pass.",
        "",
        "## Highest-overlap specialist catalogue pairs",
        "",
        "| Shared exact names | Catalogue A | Catalogue B | Examples |",
        "|---:|---|---|---|",
    ]

    for (a, b), count in specialist_pair_counts.most_common(40):
        examples = ", ".join(pair_examples[(a, b)][:5])
        out.append(f"| {count} | `{a}` | `{b}` | {examples} |")
    if not specialist_pair_counts:
        out.append("| 0 | — | — | — |")

    out += [
        "",
        "## Domain-pair overlap hotspots",
        "",
        "| Exact overlaps | Domain A | Domain B |",
        "|---:|---|---|",
    ]
    for (a, b), count in domain_pair_counts.most_common(30):
        out.append(f"| {count} | `{a}` | `{b}` |")
    if not domain_pair_counts:
        out.append("| 0 | — | — |")

    out += [
        "",
        "## Exact duplicate-name groups — specialist files",
        "",
    ]
    shown = 0
    for norm, group in exact_groups:
        specialist = [e for e in group if not e.aggregator and not e.governed]
        files = sorted({e.file for e in specialist})
        if len(files) < 2:
            continue
        shown += 1
        name = specialist[0].name
        out.append(f"### {name}")
        out.append("")
        for e in specialist:
            out.append(f"- `{e.file}:{e.line}` — `{e.raw}`")
        out.append("")
        if shown >= 120:
            out.append("_Report truncated after 120 specialist duplicate groups._")
            break
    if shown == 0:
        out.append("Aucun groupe exact specialist↔specialist détecté.")
        out.append("")

    out += [
        "## Near-duplicate candidates",
        "",
        "| Similarity | Catalogue A | Entry A | Catalogue B | Entry B |",
        "|---:|---|---|---|---|",
    ]
    for ratio, jacc, a, b in near[:80]:
        out.append(f"| {ratio:.2f} | `{a.file}` | {a.name} | `{b.file}` | {b.name} |")
    if not near:
        out.append("| — | — | — | — | — |")

    out += [
        "",
        "## Largest catalogues by credential-like table rows",
        "",
        "| Rows | Catalogue |",
        "|---:|---|",
    ]
    for file, count in file_entry_counts.most_common(30):
        out.append(f"| {count} | `{file}` |")

    out += [
        "",
        "## Domain row volume",
        "",
        "| Rows | Domain |",
        "|---:|---|",
    ]
    for domain, count in domain_entry_counts.most_common():
        out.append(f"| {count} | `{domain}` |")

    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out[:80]))
    print(f"\nFull report: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
