#!/usr/bin/env python3
"""Audit entry-level geography coverage in mixed catalogues.

Fails when a credential-like table row has no Portée column, or when a bullet
carrying a CERT/QUAL/ACC/REG/COURSE/ORG nature token has no geography label.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CERT_DIR = ROOT / "certifications"
REPORT = ROOT / "metadata" / "entry-geography-audit.md"
GEO = re.compile(r"(?:🇫🇷\s*FR|🇪🇺\s*EUR|🇺🇸\s*US|🇬🇧\s*UK|🇨🇦\s*CA|🇦🇺\s*AU|🌍\s*INT|🌐\s*(?:MIX|REG)|❓\s*UNV)")
NATURE = re.compile(r"\b(?:CERT|QUAL|ACC|REG|COURSE|ORG)\b")


def mixed(text: str) -> bool:
    if not text.startswith('---\n'):
        return False
    end = text.find('\n---\n', 4)
    return end > 0 and bool(re.search(r"(?m)^\s*-\s+mixed\s*$", text[4:end]))


def split_row(line: str):
    s=line.strip()
    if not(s.startswith('|') and s.endswith('|')): return []
    return [c.strip() for c in s[1:-1].split('|')]


def main():
    missing=[]
    for path in sorted(CERT_DIR.glob('*.md')):
        text=path.read_text(encoding='utf-8')
        if not mixed(text): continue
        lines=text.splitlines()
        for n,line in enumerate(lines,1):
            st=line.lstrip()
            if st.startswith(('- ','* ')) and NATURE.search(st) and not GEO.search(st):
                missing.append((str(path.relative_to(ROOT)),n,'bullet',st.strip()))
        # Tables with a credential-like first header must have Portée if they contain credential rows.
        i=0
        while i+1 < len(lines):
            hdr=split_row(lines[i]); sep=split_row(lines[i+1])
            if hdr and sep and all(re.fullmatch(r':?-{3,}:?', c.replace(' ','')) for c in sep):
                h=' '.join(hdr).lower()
                if any(k in h for k in ['credential','certification','qualification','designation','désignation']) and not any('portée' in c.lower() or 'portee' in c.lower() for c in hdr):
                    j=i+2; rows=0
                    while j<len(lines) and split_row(lines[j]): rows+=1; j+=1
                    if rows:
                        missing.append((str(path.relative_to(ROOT)),i+1,'table',lines[i].strip()))
                    i=j; continue
            i+=1
    out=['# Entry-level geography audit','',f'- missing geography annotations: **{len(missing)}**','']
    if missing:
        out += ['## Missing','']
        for p,n,k,s in missing:
            out.append(f'- `{p}:{n}` ({k}) — `{s.replace("|", "¦")}`')
    else:
        out.append('Aucune entrée credential détectée sans portée.')
    REPORT.write_text('\n'.join(out)+'\n',encoding='utf-8')
    print(f'missing={len(missing)}')
    return 1 if missing else 0

if __name__=='__main__':
    raise SystemExit(main())
