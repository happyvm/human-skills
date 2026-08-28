#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CERT_DIR = ROOT / "certifications"
REPORT = ROOT / "metadata" / "entrepreneur-duplicate-audit.md"

# Marker -> canonical file.
# The audit only treats a non-canonical TABLE ROW as a duplicate when the row
# looks like a credential detail row (nature / scope / price). Plain status or
# routing tables are allowed.
CANONICAL = {
    # Core creation
    "Certiport ESB": "entrepreneurship-startup-business-creation-2026.md",
    "CréActifs RS7004": "entrepreneurship-startup-business-creation-2026.md",
    "CréActifs RS7005": "entrepreneurship-startup-business-creation-2026.md",
    "SFEDI": "entrepreneurship-startup-business-creation-2026.md",

    # Core operations France
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

    # Portable global skills
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

    # Growth
    "CFI FMVA": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "CFI CBCA": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "VC University": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "WIPO Academy DL-101": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "Amazon Ads": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "Shopify": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "CICM": "entrepreneur-growth-finance-ecommerce-ip-2026.md",
    "Harvard PON": "entrepreneur-growth-finance-ecommerce-ip-2026.md",

    # Reprise / franchise / risk
    "RS7413": "entrepreneur-transfer-franchise-risk-financing-france-2026.md",
    "IFA Certified Franchise Executive": "entrepreneur-transfer-franchise-risk-financing-france-2026.md",
    "IFA Foundations of Franchising": "entrepreneur-transfer-franchise-risk-financing-france-2026.md",
    "RIMS-CRMP": "entrepreneur-transfer-franchise-risk-financing-france-2026.md",
    "FCIB": "entrepreneur-transfer-franchise-risk-financing-france-2026.md",

    # France practical
    "AMRAE ST046": "entrepreneur-france-practical-resources-2026.md",
    "AMRAE ST047": "entrepreneur-france-practical-resources-2026.md",
    "AFDCC": "entrepreneur-france-practical-resources-2026.md",
    "INPI Pass PI": "entrepreneur-france-practical-resources-2026.md",
    "EUIPO SME Fund": "entrepreneur-france-practical-resources-2026.md",

    # Sectoral
    "CMA France RS6996": "entrepreneur-artisan-agri-uk-microcredentials-2026.md",
    "CMA France RS6994": "entrepreneur-artisan-agri-uk-microcredentials-2026.md",
    "RS7277": "entrepreneur-artisan-agri-uk-microcredentials-2026.md",

    # Group management ownership
    "CFA Institute Private Equity Certificate": "entrepreneur-holding-lbo-impact-cooperative-governance-2026.md",
    "CFA Institute Advanced Private Equity Certificate": "entrepreneur-holding-lbo-impact-cooperative-governance-2026.md",
    "CFI FPAP": "entrepreneur-group-finance-private-credit-pmi-corpdev-2026.md",
    "ACCA CertIFR": "entrepreneur-group-finance-private-credit-pmi-corpdev-2026.md",
    "ACCA DipIFR": "entrepreneur-group-finance-private-credit-pmi-corpdev-2026.md",
    "IMAA CPMI": "entrepreneur-group-finance-private-credit-pmi-corpdev-2026.md",
    "IMAA International M&A Expert": "entrepreneur-group-finance-private-credit-pmi-corpdev-2026.md",
    "ACT Certificate in Treasury Fundamentals": "entrepreneur-treasury-cash-pooling-epm-carveout-2026.md",
    "ACT Award in International Cash Management": "entrepreneur-treasury-cash-pooling-epm-carveout-2026.md",
    "ACT Certificate in International Cash Management": "entrepreneur-treasury-cash-pooling-epm-carveout-2026.md",
    "CFI Loan Covenants": "entrepreneur-treasury-cash-pooling-epm-carveout-2026.md",
    "IMAA SCDE": "entrepreneur-treasury-cash-pooling-epm-carveout-2026.md",
    "Swift Certified Expert": "entrepreneur-bank-connectivity-sellside-procurement-facilities-fleet-2026.md",
    "Kyriba": "entrepreneur-bank-connectivity-sellside-procurement-facilities-fleet-2026.md",
    "AFP Certified Treasury Professional": "entrepreneur-bank-connectivity-sellside-procurement-facilities-fleet-2026.md",
}

FILES = sorted(CERT_DIR.glob("entrepreneur*.md"))
violations = []
seen = {k: [] for k in CANONICAL}

DETAIL_RE = re.compile(
    r"(?:\bCERT\b|\bQUAL\b|\bCOURSE\b|\bBADGE\b|\bAID\b|\bREG\b|"
    r"€|\$|£|CAD|provider-dependent|sur devis|"
    r"🇫🇷|🇪🇺|🇬🇧|🇺🇸|🌍|🌐)",
    re.IGNORECASE,
)

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
                if name != canonical and DETAIL_RE.search(line):
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
    f"- non-canonical detailed table occurrences: **{len(violations)}**",
    f"- canonical markers not found in owner table: **{len(missing)}**",
    "",
]

if violations:
    out += ["## Non-canonical detailed table occurrences", ""]
    for marker, canonical, name, lineno, line in violations:
        out.append(f"- `{marker}`: `{name}:{lineno}`; owner `{canonical}` — `{line}`")
    out.append("")
else:
    out += ["## Non-canonical detailed table occurrences", "", "Aucune.", ""]

if missing:
    out += [
        "## Canonical markers not found in an owner table",
        "",
        "Informational only: some canonical credentials are intentionally detailed in prose rather than a table.",
        "",
    ]
    for marker, canonical in missing:
        out.append(f"- `{marker}` — owner `{canonical}`")
    out.append("")
else:
    out += ["## Canonical markers not found in an owner table", "", "Aucun.", ""]

REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
print("\n".join(out))

if violations:
    sys.exit(1)
