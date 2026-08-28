---
title: "Guide de contribution — human-skills"
type: moc
tags:
  - moc
  - meta
status: active
verified: 2026-08-28
---

# Contribuer à human-skills

Ce dépôt est un catalogue Markdown vérifié, pas une simple liste de liens. Toute contribution doit passer les vérifications automatiques avant merge.

## Avant d'ouvrir une PR

1. **Nouvelle fiche `certifications/*.md`** : partir de [`_templates/certification.md`](_templates/certification.md) et suivre la frontmatter décrite dans [`OBSIDIAN.md`](OBSIDIAN.md) (`tier`, `domain`, `scope`, `tags`, `status`, `verified`).
2. **Portée géographique** : ne jamais mettre `scope: international` par défaut. Utiliser `scope: unverified` tant que la portabilité réelle du credential n'a pas été vérifiée — voir [`GEOGRAPHY.md`](GEOGRAPHY.md).
3. **Doublons** : avant d'ajouter le détail complet d'un credential (prix, TCO, prérequis) qui existe déjà dans une autre fiche, vérifier `metadata/catalog-overlap-analysis.md`. Un credential peut être *mentionné* dans plusieurs fiches, mais ses données détaillées ne doivent vivre que dans une seule fiche canonique (voir `metadata/entrepreneur-canonical-ownership.md` pour l'exemple de convention).
4. **Sources** : chaque prix ou detail doit être vérifiable depuis une source officielle citée dans la fiche, avec une date `verified:`.

## Lancer les vérifications localement

Tous les scripts sont en Python 3 standard (aucune dépendance externe).

```bash
python3 tools/sync-geography.py --check
python3 tools/annotate-entry-geography.py --check
python3 tools/audit-entry-geography.py
python3 tools/audit-entrepreneur-duplicates.py
python3 tools/check-internal-links.py

# Régénère les rapports d'overlap ; à commiter s'ils changent
python3 tools/audit-catalog-overlaps.py
python3 tools/audit-catalog-bullet-overlaps.py
```

Ce sont les mêmes commandes que celles exécutées par la CI (`.github/workflows/audit.yml`). Une PR qui les fait échouer ne sera pas mergée.

## Mettre à jour un fichier `scope: mixed`

Après avoir ajouté ou modifié des lignes dans une fiche à portée mixte :

```bash
python3 tools/annotate-entry-geography.py --sync
python3 tools/audit-entry-geography.py
```

Le premier ajoute les labels de portée manquants (🇫🇷 FR, 🌍 INT, ❓ UNV, ...), le second vérifie qu'il n'en reste aucun manquant.

## Style

- Français pour le contenu du catalogue, cohérent avec l'existant.
- Tableaux Markdown pour les entrées structurées (prix, portée) plutôt que des puces quand plusieurs credentials comparables sont listés.
- Pas d'emoji hors des labels de portée géographique contrôlés.
