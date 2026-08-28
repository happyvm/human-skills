---
title: "Structure Obsidian — human-skills"
type: moc
tags:
  - moc
  - meta
status: active
verified: 2026-08-28
---

# Structure Obsidian — human-skills

> Ce dépôt est un dossier Markdown standard : il peut être ouvert tel quel comme **vault Obsidian** (`Ouvrir un dossier comme coffre` → sélectionner la racine `human-skills`). Ce document décrit les conventions retenues pour que ça reste vrai à mesure que le catalogue grossit.

---

# 1. Pourquoi ces conventions

`human-skills` est une collection de fiches Markdown qui grandit en continu. Sans metadata structurée, la seule façon de s'y retrouver est de maintenir à la main de longues listes de liens dans `README.md` et les index — ce qui devient vite obsolète.

Objectif : garder les fichiers **plats** (pas de sur-classement en dizaines de sous-dossiers), et déporter l'organisation sur :

- une **frontmatter YAML** par fichier (metadata interrogeable) ;
- des **tags hiérarchiques** (`tier/…`, `domain/…`, `scope/…`) ;
- des **liens Markdown standards** ;
- des **notes MOC** (`README.md`, `IT-INDEX.md`, `CONSTRUCTION-BTP-INDEX.md`, `roadmap.md`, ce fichier) comme points d'entrée ;
- une distinction explicite entre **portée internationale** et **juridiction réglementaire locale**.

---

# 2. Arborescence

```text
human-skills/
├── README.md                     → MOC racine
├── IT-INDEX.md                    → MOC filtré IT-first
├── CONSTRUCTION-BTP-INDEX.md      → MOC Construction / BTP
├── roadmap.md                     → MOC séquencé
├── OBSIDIAN.md                    → conventions du vault
├── GEOGRAPHY.md                   → portée géographique / juridictions
├── certifications/               → une fiche par domaine/segment
├── research/                      → sujets à vérifier
├── sources/                       → radars et sources
└── _templates/                    → modèles de nouvelles fiches
```

Le dossier `certifications/` reste **volontairement plat**. Avec Obsidian, la navigation se fait par tags, recherche et graph view plutôt que par arborescence profonde.

---

# 3. Frontmatter

Chaque nouvelle fiche `certifications/*.md` doit utiliser au minimum :

```yaml
---
title: "Nom lisible de la fiche"
type: certification-catalog
tier: free | under-500 | over-500 | general
domain:
  - <une ou plusieurs valeurs, voir §4>
scope:
  - international | europe | france | national-us | national-uk | ... | mixed
jurisdiction:
  - FR | EU | US | GB | ...
regulatory_basis:
  - <norme / code / réglementation si pertinent>
tags:
  - tier/<valeur>
  - domain/<valeur>
  - scope/<valeur>
status: active
verified: YYYY-MM-DD
---
```

`jurisdiction` et `regulatory_basis` peuvent être des listes vides quand le credential n'est pas lié à une réglementation locale.

`research/*.md` utilise `type: research-note`, `sources/*.md` utilise `type: source-tracker`, les notes MOC utilisent `type: home` ou `type: moc`.

Champs :

- `tier` — tranche de prix dominante du fichier ;
- `domain` — une ou plusieurs valeurs du vocabulaire métier ;
- `scope` — **portabilité géographique réelle**, pas pays d'origine de l'organisme ;
- `jurisdiction` — juridiction juridique ou réglementaire pertinente ;
- `regulatory_basis` — réglementation, model code ou norme locale dont dépend réellement le credential ;
- `status` — `active`, `deprecated` ou `draft` ;
- `verified` — date de dernière vérification.

Pour un catalogue contenant plusieurs portées, utiliser :

```yaml
scope:
  - mixed
```

puis indiquer la portée **au niveau de chaque entrée ou groupe**. Un fichier `mixed` sans cette information est considéré comme incomplet.

Voir [`GEOGRAPHY.md`](GEOGRAPHY.md) pour les règles détaillées.

---

# 4. Taxonomie `domain/`

Vocabulaire contrôlé utilisé comme point de départ :

`accessibility`, `ai-infrastructure`, `business-soft-skills`, `cloud`, `construction-btp`, `data-database`, `datacenter-facilities`, `devops-automation`, `esg-sustainability`, `euc-endpoint`, `finance-risk`, `general-it`, `governance-grc`, `hr-people`, `identity-iam`, `industrial-ot`, `itsm-middleware`, `kubernetes-platform`, `language`, `lean-management`, `legal`, `linux`, `mainframe`, `network`, `observability`, `pharma-regulatory`, `project-management`, `real-estate`, `safety-occupational`, `security`, `storage-backup`, `supply-chain`, `virtualization`, `windows-infra`.

Une fiche peut porter plusieurs valeurs `domain`.

Tags `tier/` : `tier/free`, `tier/under-500`, `tier/over-500`, `tier/general`.

---

# 5. Taxonomie `scope/`

Valeurs principales :

```text
scope/international
scope/europe
scope/france
scope/national-us
scope/national-uk
scope/national-ca
scope/national-au
scope/national-nz
scope/national-de
scope/national-sg
scope/regional
scope/mixed
```

D'autres pays utilisent `scope/national-<cc>` avec le code ISO alpha-2 en minuscules.

La portée n'est **pas** l'origine :

```text
LEED : organisme US, scope international
PMP : organisme US, scope international
RICS : organisme UK, portée internationale selon qualification
ICC Building Inspector : scope national-us / US model codes
CACES : scope france
CSCS : scope national-uk
```

Voir [`GEOGRAPHY.md`](GEOGRAPHY.md).

---

# 6. Plugins recommandés (non requis)

Le dépôt fonctionne en Markdown pur sans aucun plugin. Pour exploiter la frontmatter :

- **Dataview** (`blacksmithgu/obsidian-dataview`) ;
- **Templater** ;
- **Tag Wrangler**.

Exemple Dataview :

````
```dataview
TABLE tier, domain, scope, verified
FROM "certifications"
WHERE contains(domain, "construction-btp") AND (contains(scope, "france") OR contains(scope, "international"))
SORT tier ASC
```
````

Cela permet notamment d'exclure rapidement des credentials purement US/UK d'une shortlist France.

---

# 7. Limites et migration progressive

Les fiches historiques n'ont pas toutes encore les champs `scope`, `jurisdiction` et `regulatory_basis` : la convention est introduite le **28 août 2026** et la migration se fait au fil des revues.

Priorité de migration :

```text
1. catalogues réglementaires et BTP
2. finance / assurance / compliance
3. santé-sécurité / QHSE
4. certifications techniques à portée nationale
5. catalogues IT généralement internationaux
```

Quand la portée d'une ancienne entrée n'a pas encore été vérifiée, ne pas l'inférer uniquement depuis la devise, le pays du fournisseur ou le domaine du site web.

---

# 8. Ce que ces conventions ne font pas

- elles ne suppriment pas les credentials US, UK ou nationaux ;
- elles empêchent simplement de les présenter comme universels sans avertissement ;
- elles ne convertissent pas les liens relatifs en `[[wikilinks]]` ;
- elles ne créent pas de dossier `.obsidian/` ;
- elles ne prétendent pas qu'une certification internationale donne un droit réglementaire d'exercer dans tous les pays.
