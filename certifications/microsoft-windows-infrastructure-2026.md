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

Les Applied Skills restent une excellente couche gratuite autour du titre principal.

## Administer Active Directory Domain Services

Évaluation pratique gratuite lorsqu'indiquée 0 € dans Microsoft Learn.

Compétences :

- Domain Controllers ;
- FSMO ;
- sites / subnets ;
- users / groups ;
- GPO ;
- gMSA ;
- security ;
- audit.

Source :

- https://learn.microsoft.com/credentials/applied-skills/administer-active-directory-domain-services/

## Azure networking / Azure Monitor

Autres Applied Skills déjà documentés dans `free-it.md` :

- Configure secure access using Azure networking ;
- Deploy and configure Azure Monitor.

---

# Security transition : AZ-500 → SC-500

## AZ-500 retire le 31 août 2026

Le credential Azure Security Engineer Associate historique est en fin de vie.

Source :

- https://learn.microsoft.com/fr-fr/credentials/certifications/resources/study-guides/az-500

## Nouveau : Cloud and AI Security Engineer Associate — SC-500

- prix France : **126 €** ;
- sécurité cloud + hybride + IA ;
- identity / access / governance ;
- networking ;
- storage / databases ;
- compute ;
- security posture.

Microsoft explique explicitement que SC-500 est la transition moderne depuis AZ-500.

Sources :

- https://learn.microsoft.com/fr-fr/credentials/certifications/cloud-and-ai-security-engineer-associate/
- https://learn.microsoft.com/fr-fr/partner-center/announcements/2026-may

**Priorité : ⭐⭐⭐⭐⭐** si sécurité Microsoft/Azure.

---

# Autres certifications Microsoft infra utiles

## Azure Administrator Associate — AZ-104

- **126 €** ;
- renouvellement annuel gratuit via Microsoft Learn.

Source :

- https://learn.microsoft.com/fr-fr/credentials/certifications/azure-administrator/

## Identity and Access Administrator — SC-300

- **126 €** ;
- Entra ID ;
- authentication ;
- workload identities ;
- identity governance.

Source :

- https://learn.microsoft.com/fr-fr/credentials/certifications/identity-and-access-administrator/

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

Attention : la liste Microsoft des retraits prévoit **MS-102 le 30 novembre 2026**. Il faut donc vérifier le nouveau chemin avant inscription tardive.

Sources :

- https://learn.microsoft.com/fr-fr/credentials/certifications/exams/ms-102/
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
- successeur MS-102 ;
- PowerShell credentials externes / vendor-neutral ;
- Windows Server 2025 focused credentials.
