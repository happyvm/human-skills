---
title: "CrowdStrike Falcon Certification Program (CFCP) — 2026"
type: certification-catalog
tier: under-500
domain:
  - security
scope:
  - international
tags:
  - tier/under-500
  - domain/security
  - scope/international
status: active
verified: 2026-08-29
---

# CrowdStrike Falcon Certification Program (CFCP) — 2026

> **Angle mort comblé lors de cette revue** : CrowdStrike (leader EDR/XDR, l'un des plus gros noms de la cybersécurité d'entreprise) n'avait **aucune mention** dans tout le dépôt avant ce commit, alors qu'il dispose d'un programme de certification de personne structuré et abordable. Sourcé directement sur le guide de certification officiel CrowdStrike University (édition juillet 2026, PDF).
>
> **Vérification : 29 août 2026**

---

# Modèle de prix — identique pour les 8 certifications

```text
Prix par examen           250 $
Format                    60 questions, QCM, closed-book
Durée                     90 minutes
Tentatives                2 (24h d'attente avant la 2e)
Livraison                 Pearson (en ligne ou centre de test)
Validité                  3 ans
Badge                     Credly (partageable), certificat imprimable
```

L'achat du voucher se fait via un commercial CrowdStrike ou directement sur Pearson. Aucune formation n'est strictement obligatoire pour s'inscrire, mais CrowdStrike recommande fortement les cours associés de CrowdStrike University (accès via licence Falcon) et au moins **6 mois d'expérience en production** sur la plateforme (3 à 6 mois pour le niveau Practitioner, le plus débutant).

Source officielle :

- https://www.crowdstrike.com/content/dam/crowdstrike/marketing/en-us/documents/pdfs/crowdstrike-university/cfcp-certification-guide.pdf
- https://www.crowdstrike.com/en-us/crowdstrike-university/crowdstrike-falcon-certification-program/

---

# Vue rapide — les 8 certifications, toutes à 250 $

| Certification | Public visé | Focus |
|---|---|---|
| Falcon Practitioner (CCFP) | Débutant Falcon — security/SOC/IT analyst | Fondamentaux plateforme, MITRE ATT&CK, Charlotte AI |
| Falcon Administrator (CCFA) | Falcon admin, endpoint security admin | Gestion instance, sensors, policies, RBAC |
| Falcon Responder (CCFR) | Analyste SOC frontline | Triage détection, investigation basique |
| Falcon Hunter (CCFH) | Threat hunter, investigateur | CQL, hunting proactif, insider threat |
| SIEM Analyst (CCSA) | Analyste SIEM / threat detection | Falcon Next-Gen SIEM, CQL, correlation |
| SIEM Engineer (CCSE) | Ingénieur/architecte sécurité | Implémentation SIEM, ingestion de logs |
| Identity Specialist (CCIS) | IAM, identity threat analyst | Identity Protection, MFA/IDaaS, Zero Trust |
| Cloud Specialist (CCCS) | Cloud security engineer | CSPM, conteneurs/Kubernetes, cloud posture |

---

# Positionnement dans ce dépôt

CrowdStrike est un acteur **EDR/XDR/SIEM/cloud security** distinct des credentials pentest/red-team déjà couverts dans `practical-cyber-under-500.md` (Hack The Box, TCM, Altered Security, CREST...) — plutôt complémentaire des certifications SOC/blue-team et cloud security. Rapport valeur/prix très favorable comparé aux certifications vendor EDR équivalentes (souvent 300-600 $ ailleurs) : **250 $ uniformes**, aucun prérequis de certification en cascade (contrairement à beaucoup de tracks vendor cloud/sécurité de ce dépôt), 3 ans de validité.

**Valeur : ⭐⭐⭐⭐⭐** pour un profil déjà en poste sur un environnement Falcon (très large base installée entreprise) — CCFA/CCFR/CCFH forment un socle SOC particulièrement recherché ; ⭐⭐⭐⭐ pour CCSA/CCSE/CCIS/CCCS, plus spécialisés.

---

# À poursuivre

- remise éventuelle pour partenaires/revendeurs CrowdStrike (non documentée sur le guide consulté) ;
- disponibilité des vouchers hors circuit commercial direct (achat individuel sans licence Falcon active) — non confirmée lors de cette revue ;
- futures certifications CFCP au-delà des 8 actuelles (le programme s'est étendu significativement en 2025-2026, à resurveiller).
