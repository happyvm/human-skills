# Metadata registries

This directory contains structured metadata used when a legacy Markdown catalogue has not yet been rewritten with every current frontmatter field.

## `geography.yml`

`geography.yml` is the authoritative geographic-scope fallback for every `certifications/*.md` file present during the 2026-08-28 backfill.

Resolution order:

```text
1. frontmatter scope, if present and not `unverified`
2. metadata/geography.yml
3. unverified
```

Current file-level backfill coverage:

```text
128 certification catalogues
103 international
21 mixed
2 france
2 europe
```

`mixed` is intentionally conservative. It means the file contains credentials whose portability or jurisdiction differs materially; recommendations must use entry-level geography before treating anything as portable to France/Europe.

The registry does not make issuer nationality equivalent to scope. A US-issued vendor certification can be `international`; a US model-code inspector credential can be `national-us` at entry level.

## Entry-level geography

The 21 `scope: mixed` catalogues are also annotated at credential level.

Visible labels currently include:

```text
🇫🇷 FR
🇪🇺 EUR
🇺🇸 US
🇬🇧 UK
🇨🇦 CA
🇦🇺 AU
🇸🇬 SG
🌍 INT
🌍 INT · UK-origin
🌍 INT · US-centric
🌍 INT · US std
🌍 INT · DE-origin
🌐 REG
🌐 MIX
❓ UNV
```

`entry-geography-rules.json` contains general matching rules. `entry-geography-overrides.json` contains reviewed exceptions and organization-context rules for ambiguous abbreviations.

The maintenance tools are:

```bash
python tools/sync-geography.py --check
python tools/annotate-entry-geography.py --check
python tools/context-fill-entry-geography.py
python tools/refine-entry-geography.py --sync
python tools/audit-entry-geography.py
```

Generated review artifacts:

- `entry-geography-report.md` — coverage and distribution of visible entry-level labels;
- `entry-geography-audit.md` — strict completeness audit; it must remain at **0 missing/unverified**.

As of the 2026-08-28 completion pass, the strict audit reports **0** credential entries without verified geography.

See [`../GEOGRAPHY.md`](../GEOGRAPHY.md) for the controlled vocabulary and rules.
