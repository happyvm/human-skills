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

`human-skills` est une collection de ~130 fiches Markdown qui grandit en continu. Sans metadata structurée, la seule façon de s'y retrouver est de maintenir à la main de longues listes de liens dans `README.md` et `IT-INDEX.md` — ce qui devient vite obsolète.

Objectif : garder les fichiers **plats** (pas de sur-classement en dizaines de sous-dossiers), et déporter l'organisation sur :

- une **frontmatter YAML** par fichier (metadata interrogeable) ;
- des **tags hiérarchiques** (`tier/…`, `domain/…`) ;
- des **liens Markdown standards** (déjà utilisés dans ce dépôt, pleinement supportés par Obsidian — pas besoin de migrer vers des `[[wikilinks]]`) ;
- des **notes MOC** (`README.md`, `IT-INDEX.md`, `roadmap.md`, ce fichier) comme points d'entrée.

---

# 2. Arborescence

```text
human-skills/
├── README.md            → MOC racine (catalogue complet, gratuit → premium)
├── IT-INDEX.md           → MOC filtré IT-first
├── roadmap.md             → MOC séquencé (ordre de passage recommandé)
├── OBSIDIAN.md            → ce document (conventions du vault)
├── certifications/         → une fiche par domaine/segment de prix
├── research/                → sujets non encore assez vérifiés pour un catalogue
├── sources/                  → radars (dépôts communautaires, fiabilité, méthode)
└── _templates/                 → modèle de nouvelle fiche (Templater-compatible)
```

Le dossier `certifications/` reste **volontairement plat**. Avec Obsidian, la navigation se fait par tags, recherche et graph view plutôt que par arborescence profonde — un dossier plat de 130 fichiers avec metadata cohérente est plus facile à maintenir qu'une arborescence à 6 niveaux qu'il faudrait reclasser à chaque nouvelle fiche ambiguë (ex. un credential IAM qui est aussi DevSecOps).

---

# 3. Frontmatter

Chaque fiche `certifications/*.md` porte désormais :

```yaml
---
title: "Nom lisible de la fiche"
type: certification-catalog
tier: free | under-500 | over-500 | general
domain:
  - <une ou plusieurs valeurs, voir §4>
tags:
  - tier/<valeur>
  - domain/<valeur>
status: active
verified: YYYY-MM-DD
---
```

`research/*.md` utilise `type: research-note`, `sources/*.md` utilise `type: source-tracker`, les notes MOC (`README.md`, `IT-INDEX.md`, `roadmap.md`, `OBSIDIAN.md`) utilisent `type: home` ou `type: moc`.

Champs :

- `tier` — tranche de prix dominante du fichier. `general` quand le fichier mélange plusieurs tranches (cas fréquent : catalogues thématiques type `actuarial-accounting-insurance.md` qui vont du gratuit à plusieurs milliers d'euros).
- `domain` — une ou plusieurs valeurs de la liste contrôlée (§4). Classement automatique de première passe fait à partir du nom de fichier ; à affiner fiche par fiche si besoin (voir §6).
- `status` — `active` par défaut. Réserver `deprecated` pour une fiche dont le sujet a été retiré ou fusionné ailleurs, `draft` pour une ébauche.
- `verified` — date de dernière vérification des prix/sources, extraite du texte existant (`Vérification : …`, `Revue : …`) quand disponible, sinon date de revue globale du dépôt.

---

# 4. Taxonomie `domain/` (v1)

Vocabulaire contrôlé utilisé par le classement automatique :

`accessibility`, `ai-infrastructure`, `business-soft-skills`, `cloud`, `data-database`, `datacenter-facilities`, `devops-automation`, `esg-sustainability`, `euc-endpoint`, `finance-risk`, `general-it`, `governance-grc`, `hr-people`, `identity-iam`, `industrial-ot`, `itsm-middleware`, `kubernetes-platform`, `language`, `legal`, `linux`, `mainframe`, `network`, `observability`, `pharma-regulatory`, `project-management`, `real-estate`, `safety-occupational`, `security`, `storage-backup`, `supply-chain`, `virtualization`, `windows-infra`.

Une fiche peut porter plusieurs valeurs `domain` (ex. un credential IAM orienté DevSecOps porte `identity-iam` et `security`). La liste peut être étendue librement — c'est un vocabulaire de travail, pas un schéma figé.

Tags `tier/` : `tier/free`, `tier/under-500`, `tier/over-500`, `tier/general`.

---

# 5. Plugins recommandés (non requis)

Le dépôt fonctionne en Markdown pur sans aucun plugin. Pour exploiter la frontmatter :

- **Dataview** (`blacksmithgu/obsidian-dataview`) — permet de remplacer à terme les listes à jour à la main de `README.md`/`IT-INDEX.md` par des requêtes du type :

  ````
  ```dataview
  TABLE tier, domain, verified
  FROM "certifications"
  WHERE contains(domain, "security")
  SORT tier ASC
  ```
  ````

- **Templater** — pour instancier `_templates/certification.md` sur une nouvelle fiche (nom, date du jour, tier/domain à choisir).
- **Tag Wrangler** — pour renommer/fusionner des tags `domain/…` en masse si la taxonomie est affinée plus tard.

Aucun de ces plugins n'est un prérequis : les fichiers restent lisibles et corrects en Markdown brut (GitHub, VS Code, autre éditeur).

---

# 6. Limites connues du classement automatique

Le champ `domain` de chaque fiche a été rempli par un script à partir du **nom de fichier**, pas d'une lecture ligne à ligne du contenu. C'est un point de départ volontairement grossier :

- une fiche multi-sujets (ex. `paid-over-500.md`, `tools-platforms-under-500.md`) porte souvent `general-it` ou un domaine dominant unique alors que son contenu réel couvre plusieurs domaines ;
- 8 fiches restent classées `domain/general-it` faute de mot-clé assez spécifique dans leur nom.

Ce n'est pas bloquant : les tags peuvent être corrigés fiche par fiche au fil de l'eau, comme le reste de la maintenance des données décrite dans `README.md` (§ Maintenance des données).

---

# 7. Ce que ce changement ne fait pas

- il ne renomme aucun fichier existant (les liens Markdown déjà en place dans `README.md`/`IT-INDEX.md`/`roadmap.md` restent valides) ;
- il ne convertit pas les liens relatifs en `[[wikilinks]]` (Obsidian les résout déjà nativement, et le rendu GitHub en dépend) ;
- il ne crée pas de dossier `.obsidian/` (config locale, propre à chaque utilisateur — à ne pas versionner).
