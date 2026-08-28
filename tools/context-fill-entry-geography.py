#!/usr/bin/env python3
"""Fill missing credential geography using the nearest organization/section context."""
from pathlib import Path
import json,re

ROOT=Path(__file__).resolve().parents[1]
CERT=ROOT/'certifications'
RULES=ROOT/'metadata'/'entry-geography-rules.json'
OVR=ROOT/'metadata'/'entry-geography-overrides.json'
GEO=re.compile(r'(?:🇫🇷\s*FR|🇪🇺\s*EUR|🇺🇸\s*US|🇬🇧\s*UK|🇨🇦\s*CA|🇦🇺\s*AU|🇸🇬\s*SG|🌍\s*INT|🌐\s*(?:MIX|REG)|❓\s*UNV)')
NATURE=re.compile(r'\b(?:CERT|QUAL|ACC|REG|COURSE|ORG)\b')
TABLE_HINTS=('credential','certification','qualification','designation','désignation')


def is_mixed(text):
    if not text.startswith('---\n'): return False
    e=text.find('\n---\n',4)
    return e>0 and bool(re.search(r'(?m)^\s*-\s+mixed\s*$',text[4:e]))


def load_matchers():
    out=[]
    for item in json.loads(OVR.read_text(encoding='utf-8'))['overrides']:
        out.append((item['label'],[re.compile(p,re.I) for p in item['patterns']]))
    for item in json.loads(RULES.read_text(encoding='utf-8'))['rules']:
        out.append((item['label'],[re.compile(p,re.I) for p in item['patterns']]))
    return out


def classify(text,matchers):
    clean=re.sub(r'[`*_]','',text)
    for label,pats in matchers:
        if any(p.search(clean) for p in pats): return label
    return None


def split_row(line):
    s=line.strip()
    if not(s.startswith('|') and s.endswith('|')): return []
    return [c.strip() for c in s[1:-1].split('|')]


def join_row(cells): return '| '+' | '.join(cells)+' |'


def is_sep(cells):
    return bool(cells) and all(re.fullmatch(r':?-{3,}:?',c.replace(' ','')) for c in cells)


def context_text(heads): return ' | '.join(heads[k] for k in sorted(heads))


def main():
    m=load_matchers(); changed_files=0; unresolved=[]
    for path in sorted(CERT.glob('*.md')):
        text=path.read_text(encoding='utf-8')
        if not is_mixed(text): continue
        lines=text.splitlines(); heads={}; out=[]; i=0; file_changed=False
        while i<len(lines):
            line=lines[i]
            hm=re.match(r'^(#{1,6})\s+(.+?)\s*$',line)
            if hm:
                lvl=len(hm.group(1)); heads[lvl]=hm.group(2)
                for k in list(heads):
                    if k>lvl: heads.pop(k,None)
                out.append(line); i+=1; continue

            # Credential-oriented Markdown table without a Portée column.
            if i+1<len(lines):
                hdr=split_row(lines[i]); sep=split_row(lines[i+1])
                if hdr and is_sep(sep):
                    h=' '.join(hdr).lower()
                    candidate=any(k in h for k in TABLE_HINTS)
                    has_scope=any('portée' in c.lower() or 'portee' in c.lower() for c in hdr)
                    if candidate and not has_scope:
                        j=i+2; rows=[]
                        while j<len(lines):
                            cells=split_row(lines[j])
                            if not cells: break
                            rows.append((j,cells)); j+=1
                        if rows:
                            ctx=context_text(heads)
                            out.append(join_row(hdr+['Portée']))
                            out.append(join_row(sep+[':---:']))
                            for original_idx,cells in rows:
                                label=classify(' | '.join(cells),m) or classify(ctx+' | '+' | '.join(cells),m)
                                if not label:
                                    label='❓ UNV'
                                    unresolved.append((str(path.relative_to(ROOT)),original_idx+1,ctx,' | '.join(cells)))
                                out.append(join_row(cells+[label]))
                            file_changed=True; i=j; continue

            st=line.lstrip()
            if st.startswith(('- ','* ')) and NATURE.search(st) and not GEO.search(st):
                ctx=context_text(heads)
                label=classify(st,m) or classify(ctx+' | '+st,m)
                if label:
                    out.append(line+' — '+label); file_changed=True
                else:
                    out.append(line)
                    unresolved.append((str(path.relative_to(ROOT)),i+1,ctx,st.strip()))
                i+=1; continue

            out.append(line); i+=1

        if file_changed:
            path.write_text('\n'.join(out)+('\n' if text.endswith('\n') else ''),encoding='utf-8'); changed_files+=1
    print(f'changed_files={changed_files}')
    print(f'unresolved={len(unresolved)}')
    for p,n,c,s in unresolved:
        print(f'UNRESOLVED {p}:{n} [{c}] {s}')
    return 0

if __name__=='__main__': raise SystemExit(main())
