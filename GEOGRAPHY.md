---
title: "Portée géographique & juridiction — human-skills"
type: moc
tags:
  - moc
  - meta
  - scope/mixed
status: active
verified: 2026-08-28
---

# Portée géographique & juridiction — human-skills

> Convention commune pour éviter de présenter comme universel un credential qui dépend d'un pays, d'une réglementation locale ou d'un corpus de normes national.

---

# 1. Deux notions différentes

Le dépôt distingue désormais systématiquement :

```text
SCOPE
  Où le credential est réellement portable / pertinent.

JURISDICTION / REGULATORY BASIS
  Loi, code, réglementation ou corpus normatif local dont dépend le credential.
```

L'origine de l'organisme ne suffit pas à déterminer la portée.

Exemples :

```text
PMI / PMP
organisme américain
scope = international
jurisdiction = none

LEED
organisme américain
scope = international
jurisdiction = scheme LEED, pas réglementation US obligatoire

ICC Building Inspector
organisme américain
scope = national-us / markets using ICC model codes
jurisdiction = US model codes

CACES
scope = france
jurisdiction = France / recommandations CNAM

RICS MRICS
organisme britannique
scope = international
jurisdiction = UK-origin professional framework
```

---

# 2. Vocabulaire contrôlé `scope`

## Portée principale

| Valeur | Signification |
|---|---|
| `international` | conçu ou reconnu pour un usage réellement multinational, sans dépendance juridique à un seul pays |
| `europe` | pertinent dans plusieurs pays européens / cadre principalement européen |
| `france` | spécifique à la France ou à son cadre réglementaire/professionnel |
| `national-us` | spécifique aux États-Unis, à leurs model codes, licences ou pratiques nationales |
| `national-uk` | spécifique au Royaume-Uni ou à ses schemes/cartes/réglementations |
| `national-ca` | Canada |
| `national-au` | Australie |
| `national-nz` | Nouvelle-Zélande |
| `national-de` | Allemagne |
| `national-sg` | Singapour |
| `national-<cc>` | autre pays, code ISO alpha-2 en minuscules |
| `regional` | valable dans une zone infra-nationale ou dans un groupe limité de juridictions |
| `mixed` | fiche catalogue contenant plusieurs portées ; la portée doit alors être indiquée au niveau des entrées |

Une fiche peut porter plusieurs valeurs lorsqu'un scheme est réellement multi-portée.

Exemple :

```yaml
scope:
  - international
  - europe
```

---

# 3. Codes courts dans les tableaux

Pour ne pas alourdir les catalogues :

```text
🌍 INT   international
🇪🇺 EUR   Europe / multi-pays européen
🇫🇷 FR    France
🇺🇸 US    États-Unis / codes ou réglementation US
🇬🇧 UK    Royaume-Uni
🇨🇦 CA    Canada
🇦🇺 AU    Australie
🇳🇿 NZ    Nouvelle-Zélande
🇩🇪 DE    Allemagne
🇸🇬 SG    Singapour
🌐 REG   autre scope régional ou multi-juridictions à préciser
```

Les emojis sont des aides visuelles ; la valeur YAML `scope` reste la donnée structurée.

---

# 4. `jurisdiction` et `regulatory_basis`

À utiliser lorsqu'une entrée dépend explicitement d'une loi, d'un code ou d'une réglementation locale.

Exemples :

```yaml
scope:
  - france
jurisdiction:
  - FR
regulatory_basis:
  - NF C 18-510
```

```yaml
scope:
  - national-us
jurisdiction:
  - US
regulatory_basis:
  - ICC model codes
```

```yaml
scope:
  - national-uk
jurisdiction:
  - GB
regulatory_basis:
  - CSCS scheme
```

`regulatory_basis` n'est **pas** obligatoire pour une certification purement professionnelle ou éditeur sans ancrage réglementaire particulier.

---

# 5. Origine ≠ portée

Un champ optionnel `origin` peut être utilisé quand cela aide à comprendre le credential :

```yaml
origin: US
scope:
  - international
```

Cela évite les raccourcis :

```text
US issuer ≠ US-only
UK chartered body ≠ UK-only market value
prix en USD ≠ certification américaine
norme ASTM/NFPA/ACI ≠ automatiquement interdite hors US
```

À l'inverse, un credential peut être commercialisé internationalement tout en restant fortement dépendant d'un code local. Dans ce cas, la dépendance doit être visible.

---

# 6. Règle pour les catalogues mixtes

Quand une fiche contient des credentials de plusieurs portées :

```yaml
scope:
  - mixed
```

et chaque tableau principal doit contenir une colonne `Portée`, ou chaque groupe doit être précédé d'un label explicite.

Exemple :

| Credential | Portée | Nature |
|---|---|---|
| PMI-CP | 🌍 INT | CERT |
| ICC Building Inspector | 🇺🇸 US | CERT |
| CACES R482 | 🇫🇷 FR | REG |
| CSCS Card | 🇬🇧 UK | REG |

Un catalogue `mixed` sans indication au niveau de l'entrée est considéré comme **incomplet**.

---

# 7. Priorité de lecture pour un utilisateur France / Europe

L'ordre recommandé dans les index est désormais :

```text
1. France
2. Europe / qualifications européennes pertinentes
3. International réellement portable
4. UK / US / autres pays si valeur internationale ou besoin explicite
5. réglementaire étranger uniquement comme référence / spécialisation
```

Un credential `national-us` ne doit donc pas apparaître dans une shortlist France sans mention explicite de sa portée et de sa valeur hors États-Unis.

---

# 8. Cas BTP particulièrement sensibles

Dans la construction, les erreurs de portée sont fréquentes :

```text
ICC / NICET / NCCCO / ATSSA / NGBS / RESNET / BPI
  → souvent US-specific ou US-centric

CSCS / CPCS / NPORS / CISRS / CITB
  → UK-specific

CACES / AIPR / SSIAP / CSPS / habilitations électriques
  → France-specific

PMI / AACE / FIDIC / buildingSMART / Autodesk / LEED / WELL
  → international ou largement portable

RICS / CIOB / ICE / IStructE / CIBSE / NEC
  → UK-origin, mais certains credentials/frameworks ont une réelle portée internationale ; préciser au cas par cas
```

Le fichier [`CONSTRUCTION-BTP-INDEX.md`](CONSTRUCTION-BTP-INDEX.md) applique cette convention au domaine BTP.

---

# 9. Maintenance

Pour chaque nouvelle entrée, vérifier dans cet ordre :

```text
credential actif ?
↓
nature CERT / QUAL / ACC / REG / COURSE / ORG
↓
scope réel
↓
juridiction / réglementation / code local éventuel
↓
portabilité France / Europe
↓
prix et TCO régional
↓
source officielle
↓
date de vérification
```

Le but n'est pas de supprimer les credentials américains, britanniques ou nationaux : il est de **ne jamais les présenter comme universels quand ils ne le sont pas**.
