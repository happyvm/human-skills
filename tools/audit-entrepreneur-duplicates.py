#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CERT_DIR = ROOT / "certifications"
REPORT = ROOT / "metadata" / "entrepreneur-duplicate-audit.md"

# Marker -> canonical file. The audit only inspects markdown TABLE ROWS in
# entrepreneur catalogues; prose cross-links and root indexes are allowed.
CANONICAL = {
    "Certiport ESB": "entrepreneurship-startup-business-creation-2026.md",
    "CréActifs RS7004": "entrepreneurship-startup-business-creation-2026.md",
    "CréActifs RS7005": "entrepreneurship-startup-business-creation-2026.md",
    "SFEDI": "entrepreneurship-startup-business-creation-2026.md",
    "RS6951": "entrepreneur-essential-operations-2026.md",
    "RS7378": "entrepreneur-essential-operations-2026.md",
    "RS7380": "entrepreneur-essential-operations-2026.md",
    "RS7385": "entrepreneur-essential-operations-2026.md",
    "RS7376": "entrepreneur-essential-operations-2026.md",
    "RS6952": "entrepreneur-essential-operations-2026.md",
    "RS7377": "entrepreneur-essential-operations-2026.md",
    "RS7382": "entrepreneur-essential-operations-2026.md",
    "RS7379": "entrepreneur-essential-operations-2026.md",
    "RS7383": "entrepreneur-essential-operations-2026.md",
    "HubSpot": "entrepreneur-international-functional-credentials-2026.md",
    "Google Ads": "entrepreneur-international-functional-credentials-2026.md",
    "Xero": "entrepreneur-international-functional-credentials-2026.md",
    "QuickBooks": "entrepreneur-international-functional-credentials-2026.md",
    "AMA PCM": "entrepreneur-international-functional-credentials-2026.md",
    "Salesforce": "entrepreneur-international-functional-credentials-2026.md",
    "Scrum.org PSM I": "entrepreneur-international-functional-credentials-2026.md",
    "ASQ Six Sigma": "entrepreneur-international-functional-credentials-2026.md",
    "WorldCC": "entrepreneur-international-functional-credentials-2026.md",
    "HRCI": "entrepreneur-international-functional-credentials-2026.md",
    "IAPP": "entrepreneur-international-functional-credentials-2026.md",
    "ICC Incoterms": "entrepreneur-international-functional-credentials-2026.md",
    "ICC Export/Import": "entrepreneur-international-functional-credentials-2026.md",
    "CFI FMVA": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "CFI CBCA": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "VC University": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "WIPO Academy DL-101": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "Amazon Ads": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "Shopify": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "CICM": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "Harvard PON": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "RS7413": "entrepreneur-transfer-franchise-risk-financing-france-2026.md",
    "RIMS-CRMP": "entrepreneur-transfer-franchise-risk-financing-france-2026.md",
    "FCIB": "entrepreneur-transfer-franchise-risk-financing-france-2026.md",
    "CMA France RS6996": "entrepreneur-artisan-agri-uk-microcredentials-2026.md",
    "CMA France RS6994": "entrepreneur-artisan-agri-uk-microcredentials-2026.md",
    "RS7277": "entrepreneur-artisan-agri-uk-microcredentials-2026.md",
    "AMRAE ST046": "entrepreneur-france-practical-resources-2026.md",
    "AMRAE ST047": "entrepreneur-france-practical-resources-2026.md",
    "AFDCC": "entrepreneur-france-practical-resources-2026.md",
    "INPI Pass PI": "entrepreneur-france-practical-resources-2026.md",
    "EUIPO SME Fund": "entrepreneur-france-practical-resources-2026.md",
}

FILES = sorted(CERT_DIR.glob("entrepreneur*.md"))
violations = []
seen = {k: [] for k in CANONICAL}

for path in FILES:
    name = path.name
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not (line.startswith("|") and line.endswith("|")):
            continue
        if re.fullmatch(r"\|[\s:|-]+\|", line):
            continue
        for marker, canonical in CANONICAL.items():
            if marker.lower() in line.lower():
                seen[marker].append((name, lineno, line))
                if name != canonical:
                    violations.append((marker, canonical, name, lineno, line))

missing = []
for marker, canonical in CANONICAL.items():
    if not any(name == canonical for name, _, _ in seen[marker]):
        missing.append((marker, canonical))

out = [
    "# Entrepreneur duplicate ownership audit",
    "",
    f"- entrepreneur catalogues scanned: **{len(FILES)}**",
    f"- canonical markers checked: **{len(CANONICAL)}**",
    f"- non-canonical table occurrences: **{len(violations)}**",
    f"- canonical markers missing from owner table: **{len(missing)}**",
    "",
]

if violations:
    out += ["## Non-canonical table occurrences", ""]
    for marker, canonical, name, lineno, line in violations:
        out.append(f"- `{marker}`: `{name}:{lineno}`; owner `{canonical}` — `{line}`")
    out.append("")
else:
    out += ["## Non-canonical table occurrences", "", "Aucune.", ""]

if missing:
    out += ["## Missing canonical markers", ""]
    for marker, canonical in missing:
        out.append(f"- `{marker}` absent d'un tableau de `{canonical}`")
    out.append("")
else:
    out += ["## Missing canonical markers", "", "Aucun.", ""]

REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
print("\n".join(out))

# Duplicate ownership is a hard error. Missing markers are informational because
# some detailed credentials are intentionally described in prose rather than tables.
if violations:
    sys.exit(1)
