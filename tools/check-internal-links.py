#!/usr/bin/env python3
"""Check that relative Markdown links resolve to a real file in the repo.

Skips http(s)/mailto links and pure in-page anchors. Uses only the
standard library.

Usage:
    python tools/check-internal-links.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:")


def main() -> int:
    md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    all_files = {p.relative_to(ROOT) for p in ROOT.rglob("*") if ".git" not in p.parts}

    broken: list[tuple[Path, str]] = []
    for md in md_files:
        text = md.read_text(encoding="utf-8", errors="ignore")
        for match in LINK_RE.finditer(text):
            link = match.group(1).strip()
            if not link or link.startswith(SKIP_PREFIXES) or link.startswith("#"):
                continue
            target_str = link.split("#", 1)[0]
            if not target_str:
                continue
            target = (md.parent / target_str).resolve()
            try:
                rel_target = target.relative_to(ROOT)
            except ValueError:
                broken.append((md, link))
                continue
            if rel_target not in all_files:
                broken.append((md, link))

    if broken:
        print(f"broken internal links: {len(broken)}")
        for md, link in broken:
            print(f" - {md.relative_to(ROOT)}: {link}")
        return 1

    print(f"checked {len(md_files)} Markdown files: 0 broken internal links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
