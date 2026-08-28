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

Current backfill coverage:

```text
128 certification catalogues
103 international
21 mixed
2 france
2 europe
```

`mixed` is intentionally conservative. It means the file contains credentials whose portability or jurisdiction differs materially; recommendations must use entry-level geography before treating anything as portable to France/Europe.

The registry does not make issuer nationality equivalent to scope. A US-issued vendor certification can be `international`; a US model-code inspector credential can be `national-us` at entry level.

See [`../GEOGRAPHY.md`](../GEOGRAPHY.md) for the controlled vocabulary and rules.
