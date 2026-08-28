---
title: "Microsoft Windows Server & hybrid infrastructure — transition 2026"
type: certification-catalog
tier: general
domain:
  - windows-infra
tags:
  - tier/general
  - domain/windows-infra
status: active
verified: 2026-08-28
---

# Microsoft Windows Server & hybrid infrastructure — transition 2026

> Windows Server, Active Directory, hybrid management et sécurité Microsoft. Vérification : 28 août 2026.

---

# Changement majeur : AZ-802 remplace AZ-800 + AZ-801

Microsoft est en train de simplifier fortement son parcours Windows Server.

## Ancien parcours — jusqu'au 30 septembre 2026

### Windows Server Hybrid Administrator Associate

Historiquement, le titre nécessite :

- AZ-800 — Administering Windows Server Hybrid Core Infrastructure ;
- AZ-801 — Configuring Windows Server Hybrid Advanced Services.

Prix France actuel :

```text
AZ-800        126 €
AZ-801        126 €
-----------------
Total         252 €
```

Mais **les deux examens seront retirés le 30 septembre 2026 à 17 h CST**.

Sources :

- https://learn.microsoft.com/fr-fr/credentials/certifications/exams/az-800/
- https://learn.microsoft.com/fr-fr/credentials/certifications/exams/az-801/
- https://learn.microsoft.com/fr-fr/credentials/support/retired-certification-exams

> Certaines sections de page peuvent encore afficher `Date de retrait : aucun` alors que l'avertissement officiel et la liste centrale de retraits donnent bien le 30/09/2026. Le dépôt retient la date de retrait officielle.

---

# Nouveau parcours — Windows Server Administrator Associate

Microsoft publie désormais :

## Microsoft Certified: Windows Server Administrator Associate

Statut au 28 août 2026 : **bêta**.

Le nouveau chemin utilise un seul examen :

### AZ-802 — Administering Windows Server

- prix France : **126 €** ;
- langue actuellement affichée : anglais pendant la phase bêta ;
- score de réussite cible : 700 ;
- pas encore de Practice Assessment pendant la bêta ;
- formation AZ-802T00 disponible à partir du **28 août 2026**.

La page Microsoft confirme explicitement qu'après le retrait d'AZ-800 et AZ-801, **AZ-802 restera comme chemin disponible pour obtenir cette certification**.

Sources :

- https://learn.microsoft.com/fr-fr/credentials/certifications/windows-server-administrator-associate/
- https://learn.microsoft.com/fr-fr/credentials/certifications/resources/study-guides/az-802
- https://learn.microsoft.com/fr-fr/training/courses/az-802t00

---

# Impact coût

## Avant

```text
AZ-800 + AZ-801
126 + 126
= 252 €
```

## Nouveau modèle

```text
AZ-802
= 126 €
```

Si le modèle reste ainsi après sortie de bêta, le ticket d'entrée du credential Windows Server professionnel est donc **divisé par deux**.

**Valeur / prix : ⭐⭐⭐⭐⭐** pour un profil infrastructure Windows.

---

# Compétences AZ-802

Le programme couvre notamment :

- Active Directory Domain Services ;
- Group Policy ;
- Windows Server security baselines ;
- Hyper-V ;
- Azure VMs ;
- containers Windows ;
- réseau local et hybride ;
- stockage / file services ;
- Windows Admin Center ;
- PowerShell remoting ;
- Azure Arc ;
- monitoring / troubleshooting ;
- haute disponibilité ;
- hybrid identity.

Source :

- https://learn.microsoft.com/fr-fr/credentials/certifications/resources/study-guides/az-802

---

# Microsoft Applied Skills — compléments gratuits

Les Applied Skills restent une excellente couche gratuite autour du titre principal, à commencer par **Administer Active Directory Domain Services** (Domain Controllers, FSMO, sites/subnets, GPO, gMSA, security, audit) et les compléments Azure networking / Azure Monitor déjà documentés dans `free-it.md`.

Catalogue complet et à jour : voir [`free-microsoft-applied-skills-2026.md`](free-microsoft-applied-skills-2026.md).

---

# Security transition : AZ-500 → SC-500

Le credential Azure Security Engineer Associate (AZ-500) est retiré le **31 août 2026**, remplacé par **Cloud and AI Security Engineer Associate — SC-500** (126 € en France). Détail complet (compétences, sources) : voir [`public-cloud-multicloud-under-500.md`](public-cloud-multicloud-under-500.md#az-500-retire-le-31-août-2026).

**Priorité : ⭐⭐⭐⭐⭐** si sécurité Microsoft/Azure.

---

# Autres certifications Microsoft infra utiles

Deux certifications role-based à 126 € sont utiles en complément d'AZ-802 mais déjà détaillées dans le catalogue multicloud : **Azure Administrator Associate — AZ-104** et **Identity and Access Administrator — SC-300**. Voir [`public-cloud-multicloud-under-500.md`](public-cloud-multicloud-under-500.md#azure-administrator-associate--az-104).

## Azure Database Administrator — DP-300

- **126 €** ;
- Azure SQL / SQL workloads ;
- renouvellement gratuit en ligne.

Source :

- https://learn.microsoft.com/fr-fr/credentials/certifications/azure-database-administrator-associate/

## Microsoft 365 Administrator — MS-102

- **126 €** ;
- tenant management ;
- Entra ID ;
- Defender ;
- Purview.

Attention : Microsoft confirme officiellement le retrait de **MS-102 le 30 novembre 2026 à 23h59 CST**.

**Successeur confirmé (officiel, Microsoft Learn) : AB-650 — Administering Microsoft 365 and AI Services (actuellement en beta)**, qui mène à la certification *Microsoft 365 Certified: AI Services Administrator Associate*. Contrairement à MS-102 (qui exigeait un second examen associate en plus), **AB-650 est un examen unique sans prérequis formel**, avec un contenu élargi à la gouvernance des services IA/Copilot/agents (35–40 % du programme).

Source :

- https://learn.microsoft.com/en-us/credentials/certifications/exams/ms-102/
- https://learn.microsoft.com/en-us/credentials/certifications/exams/ab-650/
- https://learn.microsoft.com/fr-fr/credentials/support/retired-certification-exams

---

# TCO Microsoft particulièrement favorable

Les certifications Microsoft Associate / Expert / Specialty expirent généralement chaque année, mais le renouvellement peut être effectué **gratuitement par une évaluation en ligne Microsoft Learn** pendant la fenêtre prévue.

Cela donne un schéma intéressant :

```text
AZ-802 initial exam         126 €
annual renewal exam           0 €
---------------------------------
monetary TCO 3 years        126 €
```

hors éventuel retake initial ou formation payante facultative.

C'est l'un des modèles de maintenance les moins chers du catalogue.

---

# Roadmap Windows / Microsoft infra 2026

```text
Microsoft Applied Skill AD DS       0 €
             ↓
AZ-802 Windows Server Admin       126 €
             ↓
AZ-104 Azure Administrator        126 €
             ↓
SC-300 Identity Administrator     126 €
             ↓
SC-500 Cloud & AI Security        126 €
             ↓
AZ-305 Architecture               126 €
```

Le choix doit évidemment dépendre du rôle : infrastructure, hybrid cloud, identity, security ou architecture.

---

# À poursuivre

- Hyper-V / SCVMM credentials Microsoft actuels : souvent intégrés plutôt que dédiés ;
- Azure Local / Azure Stack HCI ;
- Windows 365 / AVD ;
- Intune ;
- Defender XDR ;
- Purview ;
- Entra advanced paths ;
- SC-500 sortie de bêta / langues ;
- AZ-802 sortie de bêta / date GA ;
- AB-650 — prix exact une fois sorti de beta, et date de disponibilité générale exacte ;
- PowerShell credentials externes / vendor-neutral ;
- Windows Server 2025 focused credentials.
