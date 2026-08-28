---
title: "CI/CD, GitLab, Jenkins & DevOps tooling — certification status 2026"
type: certification-catalog
tier: general
domain:
  - devops-automation
tags:
  - tier/general
  - domain/devops-automation
status: active
verified: 2026-08-28
---

# CI/CD, GitLab, Jenkins & DevOps tooling — certification status 2026

> Revue : **28 août 2026**. Objectif : distinguer les vraies certifications professionnelles actives des anciens programmes, badges et contenus de formation.

---

# 1. GitLab

GitLab University expose actuellement plusieurs certifications techniques officielles :

- **GitLab Certified Git Associate** ;
- **GitLab Certified CI/CD Associate** ;
- **GitLab Certified Agile Project Management Associate** ;
- **GitLab Certified Security Specialist** ;
- **Certified GitLab Duo (AI) Associate** — nouveau track AI.

**Auto-formation officielle et gratuite :** [university.gitlab.com](https://university.gitlab.com/) — GitLab Learn, cours self-paced gratuits associés à chaque examen, dont deux certifications entièrement gratuites (GitLab 101/201).

## Format

Pour les certifications techniques, GitLab indique :

1. un knowledge exam / written assessment à réussir à **80 %** ;
2. un hands-on exam également à **80 %** ;
3. environnement de démonstration / sandbox fourni lorsque nécessaire ;
4. évaluation hands-on par GitLab Professional Services Engineers ;
5. badge numérique Credly.

Chaque certification possède un parcours de préparation **self-paced gratuit** dans GitLab University.

## Prix 2026

Prix confirmé : **150 $ par tentative d'examen**, à l'unité, sans formation obligatoire au préalable.

Pour ceux qui veulent une formation structurée en plus (facultative) : bundle self-service **650 $**, session publique instructor-led **750 $/place**.

### Verdict

**Excellent rapport signal/prix** : 150 $ pour un examen officiel sans prérequis de formation, avec parcours de préparation gratuit dans GitLab University.

Sources :

- https://university.gitlab.com/pages/certifications
- https://about.gitlab.com/professional-services/education/
- https://about.gitlab.com/blog/everyone-can-get-certified/

Sources :

- https://university.gitlab.com/pages/certifications
- https://about.gitlab.com/professional-services/education/
- https://about.gitlab.com/blog/everyone-can-get-certified/

---

# 2. CloudBees / Jenkins

CloudBees a historiquement créé les certifications :

- **Certified Jenkins Engineer (CJE)** ;
- certification CloudBees Jenkins Platform / CloudBees Jenkins Engineer selon génération du programme.

Le guide officiel CJE décrit un examen portant sur :

- concepts CI/CD / Jenkins ;
- utilisation Jenkins ;
- Continuous Delivery pipelines ;
- CD-as-code / best practices.

## Statut 2026

Le CJE n'a **pas été retiré** (seule une ancienne version de l'examen a été retirée) — l'examen actuel reste actif en 2026.

Prix observé (sources tierces cohérentes) : **99 $**. Le domaine `university.cloudbees.com` était injoignable lors de la vérification directe (DNS) — **prix à reconfirmer au checkout avant achat**, non issu du store officiel lui-même.

Guide de préparation officiel :

- https://university.cloudbees.com/path/certified-jenkins-engineer-cje-exam-preparation

De nombreux sites tiers prétendent vendre des dumps/préparations « CJE 2026 » : **ils ne constituent pas une preuve que l'examen est encore commercialisé**.

### Verdict

Classer CJE / CCJE comme **legacy / status-to-confirm**, pas comme certification 2026 low-cost certaine.

Sources officielles :

- https://www.cloudbees.com/sites/default/files/cje_study_guide_final.pdf
- https://www.cloudbees.com/newsroom/cloudbees-announces-industrys-first-certification-program-jenkins-engineers

---

# 3. GitHub

Les certifications GitHub sont déjà traitées dans le catalogue IaC / DevSecOps.

Prix de référence : **99 $** pour les examens GitHub courants lors de la revue.

Tracks utiles :

- GitHub Foundations ;
- GitHub Actions ;
- GitHub Advanced Security ;
- GitHub Administration ;
- Copilot selon catalogue actif.

Voir :

- [`iam-devsecops-automation-under-500.md`](iam-devsecops-automation-under-500.md)

---

# 4. Jenkins open source sans CloudBees

Le projet Jenkins lui-même fournit documentation, labs et communauté mais ne publie pas actuellement un programme de certification indépendant de CloudBees clairement identifiable.

Ne pas confondre :

```text
Jenkins project training/community
!=
CloudBees Certified Jenkins Engineer
```

---

# Shortlist CI/CD

```text
99 $        GitHub Actions / Administration / GHAS
checkout    GitLab CI/CD Associate / Security Specialist
legacy?     CloudBees CJE / CCJE — vérifier programme live avant achat
```

### Recommandation catalogue

Pour un signal CI/CD moderne, prioriser :

1. GitHub Actions ;
2. GitLab CI/CD Associate lorsque le tarif checkout est acceptable ;
3. Kubernetes / GitOps / Argo / platform engineering déjà couverts dans le catalogue CNCF ;
4. CloudBees/Jenkins uniquement si un besoin entreprise Jenkins le justifie et si l'examen est confirmé live.
