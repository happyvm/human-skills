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


def is_mixed(text):
    if not text.startswith('---\n'): return False
    e=text.find('\n---\n',4)
    return e>0 and bool(re.search(r'(?m)^\s*-\s+mixed\s*$',text[4:e]))


def load_matchers():
    out=[]
    # Explicit review overrides win over generic rules.
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


def main():
    m=load_matchers(); changed=0; unresolved=[]
    for path in sorted(CERT.glob('*.md')):
        text=path.read_text(encoding='utf-8')
        if not is_mixed(text): continue
        lines=text.splitlines(); heads={}; file_changed=False
        for i,line in enumerate(lines):
            hm=re.match(r'^(#{1,6})\s+(.+?)\s*$',line)
            if hm:
                lvl=len(hm.group(1)); heads[lvl]=hm.group(2)
                for k in list(heads):
                    if k>lvl: heads.pop(k,None)
                continue
            st=line.lstrip()
            if st.startswith(('- ','* ')) and NATURE.search(st) and not GEO.search(st):
                context=' | '.join(heads[k] for k in sorted(heads))
                label=classify(context+' | '+st,m)
                if label:
                    lines[i]=line+' — '+label; file_changed=True
                else:
                    unresolved.append((str(path.relative_to(ROOT)),i+1,context,st.strip()))
        if file_changed:
            path.write_text('\n'.join(lines)+('\n' if text.endswith('\n') else ''),encoding='utf-8'); changed+=1
    print(f'changed_files={changed}')
    print(f'unresolved={len(unresolved)}')
    for p,n,c,s in unresolved:
        print(f'UNRESOLVED {p}:{n} [{c}] {s}')
    return 0

if __name__=='__main__': raise SystemExit(main())
