---
title: "Observability vendors — état des certifications 2026"
type: certification-catalog
tier: general
domain:
  - observability
scope:
  - international
tags:
  - tier/general
  - domain/observability
  - scope/international
status: active
verified: 2026-08-28
---

# Observability vendors — état des certifications 2026

> Complément au fichier `observability-sre-devops-under-500.md` pour les éditeurs dont le programme ou les prix ont fortement changé. Vérification : 28 août 2026.

---

# Vue rapide

| Provider | Credential / niveau | Prix / statut 2026 |
|---|---|---|
| Sumo Logic | Certified Fundamentals User | **100 $** |
| Sumo Logic | autres certifications | **150 $** |
| Cisco AppDynamics | Associate Administrator | **300 $** |
| Cisco AppDynamics | Associate Performance Analyst | **300 $** |
| Cisco AppDynamics | Professional Implementer | **300 $** |
| New Relic | Verified Foundation | certification active, **prix public général non exposé** |
| New Relic | APM Practitioner Associate | certification active, vouchers promo/étudiants existent |
| Dynatrace | Associate / Professional tracks | programme actif, **prix public non suffisamment exposé** |
| Grafana Labs | learning paths | pas de certification professionnelle officielle clairement tarifée trouvée |

---

# Sumo Logic — ancienne gratuité devenue payante

Les anciennes listes GitHub présentent souvent les certifications Sumo Logic comme gratuites.

En 2026, la situation officielle est :

- **toutes les formations self-paced et public live restent gratuites** ;
- les examens de certification sont désormais payants.

## Tarifs

- Certified Fundamentals User : **100 $** ;
- toutes les autres certifications : **150 $**.

Le voucher doit être utilisé dans les 12 mois.

La FAQ actuelle précise également que les anciennes certifications restent valides jusqu'à leur expiration initiale : Fundamentals deux ans, autres un an, avec renouvellement possible sous le nouveau programme.

Source :

- https://www.sumologic.com/help/docs/get-started/training-certification-faq/

### TCO

```text
Training                 0 $
Fundamentals exam      100 $
Advanced exam          150 $
```

**Valeur / prix : ⭐⭐⭐⭐** pour un environnement Sumo Logic.

---

# Cisco AppDynamics

Cisco maintient plusieurs certifications AppDynamics formelles à **300 $**.

**Auto-formation officielle :** [learn.appdynamics.com](https://learn.appdynamics.com/certifications) — AppDynamics University, learning plans self-paced (Standard/Enterprise) ou instructor-led (Premium).

## Associate Administrator — 500-425 CAAA

- prix : **300 $** ;
- 90 minutes ;
- online ou Pearson VUE ;
- configuration, administration et optimisation AppDynamics.

Source :

- https://www.cisco.com/site/us/en/learn/training-certifications/certifications/appdynamics/associate-administrator/exams-and-training.html

## Associate Performance Analyst — 500-420 CAAPA

- prix : **300 $** ;
- 90 minutes ;
- monitoring, analyse et remediation de problèmes de performance.

Source :

- https://www.cisco.com/site/us/en/learn/training-certifications/certifications/appdynamics/associate-performance-analyst/exams-and-training.html

## Professional Implementer

- prix : **300 $** ;
- déploiement de controllers, agents, analytics/EUM et APIs.

Source :

- https://www.cisco.com/site/us/en/learn/training-certifications/certifications/appdynamics/professional-implementer/exams-and-training.html

**Valeur CV : ⭐⭐⭐⭐** dans les environnements Cisco AppDynamics.

---

# New Relic — programme actif, tarification publique opaque

New Relic dispose d'un programme de certification actif.

**Auto-formation officielle et gratuite :** [learn.newrelic.com](https://learn.newrelic.com/) — New Relic University, formation self-paced ou instructor-led et certifications, entièrement gratuites.

Credentials officiellement cités :

- **New Relic Verified Foundation (NVF)** ;
- **APM Practitioner Associate (APA)** ;
- autres certifications selon programme New Relic University.

Source :

- https://newrelic.com/blog/observability/new-relic-certifications-a-guide-to-advancing-your-career-in-observability

## Verified Foundation

New Relic organise encore en 2026 des sessions officielles de préparation à Verified Foundation, preuve que l'examen reste actif.

Source :

- https://newrelic.com/jp/events/2026-09-02/nvfexm

## Prix général

Au moment de la revue, New Relic ne publie pas sur les pages publiques consultées une grille universelle claire du prix de chaque examen.

**Statut : `PRICE-OPAQUE / CHECKOUT-REQUIRED`.**

Ne pas extrapoler à partir de promotions.

---

# New Relic — gratuités conditionnelles

## Étudiants

Le programme New Relic for Students offre :

- compte étudiant ;
- contenus / ateliers exclusifs ;
- accès à des opportunités de certification.

Source :

- https://newrelic.com/students

Une session étudiante 2025 indiquait explicitement :

- Verified Foundation exam **gratuit** ;
- voucher gratuit APM Practitioner après la formation.

Source historique :

- https://newrelic.com/events/2025-07-29/foundation-certification-training-new-relic-for-students

Comme cette offre était événementielle, elle doit être classée :

`FREE-CONDITIONAL / STUDENT-EVENT`, pas `FREE-GENERAL`.

## Workshops 2026

La série New Relic University 2026 propose également un tirage au sort permettant de gagner un voucher d'examen de certification gratuit.

Source :

- https://newrelic.com/event/new-relic-university-workshop-series

Encore une fois : **promotion**, pas tarif normal.

---

# Dynatrace

Dynatrace University dispose toujours de certifications Associate / Professional et les examens actuels ont évolué vers davantage de pratique.

**Auto-formation officielle :** [Dynatrace University](https://www.dynatrace.com/service-support/education-services/) — learning paths, blueprint d'examen et practice exam ; sandbox Playground gratuit + trial 15 jours pour la pratique.

La communauté Dynatrace décrit en juin 2026 un nouvel examen Associate Managed comprenant :

- partie théorique ;
- puis plusieurs tâches hands-on dans un environnement Dynatrace.

Toutefois, la grille tarifaire publique Dynatrace consultable sans connexion expose surtout le prix de la plateforme, **pas un prix officiel suffisamment stable des examens de certification**.

Des sources tierces (non officielles) indiquent une fourchette **200–250 $ par tentative** pour Associate/Professional avec jusqu'à 3 tentatives incluses — à confirmer directement sur le portail Dynatrace University avant achat, ce chiffre n'étant pas issu du store officiel.

Source produit :

- https://www.dynatrace.com/pricing/rate-card/

**Statut prix : `PRICE-OPAQUE / UNIVERSITY-CHECKOUT`.**

Ne pas figer les anciens montants de blogs ou de forums comme prix 2026.

---

# Grafana Labs

**Auto-formation officielle et gratuite :** [learn.grafana.com](https://learn.grafana.com/) (GROT Academy, cours hands-on de 30 min) et [grafana.com/tutorials](https://grafana.com/tutorials/).

Grafana Labs publie :

- tutorials ;
- learning journeys ;
- workshops ;
- documentation ;
- training autour de Grafana, Loki, Tempo, Mimir et OpenTelemetry.

Mais la recherche 2026 n'a pas permis d'identifier une **certification professionnelle officielle avec examen et prix public** comparable à Splunk/Elastic/Datadog.

**Statut : `NO-FORMAL-CERT-FOUND`.**

Ne pas transformer un badge de cours ou completion certificate en certification professionnelle.

---

# Comparatif

```text
Datadog              100 $
Sumo Fundamentals    100 $
Sumo Advanced        150 $
Splunk               130 $
Prometheus PCA       250 $
OpenTelemetry OTCA   250 $
AppDynamics          300 $
Elastic              400–500 $
New Relic            price opaque
Dynatrace            price opaque
Grafana              no formal public exam found
```

---

# Priorités rapport coût / signal

1. **Datadog — 100 $** ;
2. **Sumo Logic — 100/150 $** si utilisé ;
3. **Splunk — 130 $** par examen de base ;
4. **Prometheus PCA / OTCA — 250 $** vendor-neutral ;
5. **AppDynamics — 300 $** ;
6. **Elastic — 400/500 $**, surtout parce que performance-based.

---

# À surveiller

- prix New Relic général hors promotions ;
- Dynatrace checkout / price list officiel ;
- nouveau programme Cisco Full-Stack Observability ;
- Grafana formal certification si lancement ;
- OpenSearch ;
- Honeycomb ;
- Chronosphere ;
- Coralogix ;
- LogicMonitor ;
- SolarWinds ;
- ScienceLogic ;
- IBM Instana ;
- IBM Turbonomic.
