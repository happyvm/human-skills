---
title: "Microsoft Azure Local / HCI / Windows Server 2025 credentials — 2026"
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

# Microsoft Azure Local / HCI / Windows Server 2025 credentials — 2026

> Revue : **28 août 2026**. Objectif : distinguer les vraies certifications Microsoft, les Applied Skills et les simples learning achievements autour d'Azure Local / HCI.

---

# Conclusion rapide

À la date de cette revue, **aucune certification role-based ni Microsoft Applied Skills dédiée spécifiquement à Azure Local** n'a été identifiée dans le catalogue public Microsoft Credentials.

Microsoft propose en revanche :

1. une **Azure Local Accreditation 2025** gratuite sur Microsoft Learn ;
2. une **Windows Server 2025 Accreditation 2026** gratuite qui inclut un module Azure Local ;
3. la certification **Windows Server Administrator Associate / AZ-802** pour le signal technique Windows Server hybride ;
4. plusieurs Applied Skills adjacents, mais pas un credential Azure Local standalone clairement publié.

Ne pas présenter les Accreditation Learn comme des certifications professionnelles role-based.

---

# Azure Local Accreditation 2025

Microsoft Learn publie un parcours :

**Azure Local Accreditation 2025**

- coût : **0 €** ;
- durée annoncée : environ **1 h 10** ;
- 4 modules ;
- 3 100 XP ;
- niveau débutant ;
- aucun prérequis ;
- possibilité de demander un **Achievement Code**.

Le parcours couvre notamment :

- introduction à Azure Local ;
- workloads virtualisés on-prem ;
- HCI ;
- intégration Azure ;
- positionnement produit.

### Statut

```text
Formation / accreditation Learn : oui
Achievement Code                 : oui
Certification role-based         : non
Applied Skills lab assessment    : non identifié
```

Source :

- https://learn.microsoft.com/en-us/training/paths/azure-local-accreditation-2025/

---

# Windows Server 2025 Accreditation 2026

Microsoft publie également :

**Windows Server 2025 Accreditation 2026**

- coût : **0 €** ;
- 2 300 XP ;
- environ **54 minutes** ;
- 3 modules ;
- aucun prérequis ;
- Achievement Code disponible.

Le parcours inclut explicitement :

- modernisation depuis Windows Server 2016/2019 ;
- introduction à Windows Server 2025 ;
- **When to evaluate Azure Local for private cloud scenarios**.

### Verdict

Très facile à ajouter comme achievement gratuit, mais signal technique faible comparé à une vraie certification proctored ou à un Applied Skills lab-based.

Source :

- https://learn.microsoft.com/en-us/training/paths/windows-server-2025-accreditation-2026/

---

# AZ-802 — meilleur signal Windows Server hybride 2026

Le remplacement 2026 du parcours AZ-800/AZ-801 est **AZ-802 — Windows Server Administrator**.

Pour un profil travaillant sur :

- Windows Server 2025 ;
- Hyper-V ;
- hybrid management ;
- Azure Arc ;
- Active Directory ;
- networking/storage/HA ;

AZ-802 fournit un signal plus fort que les accreditations Learn gratuites.

Prix France observé dans le catalogue Microsoft : **126 €** pour un examen role-based Microsoft de cette classe de prix.

Voir :

- [`microsoft-windows-infrastructure-2026.md`](microsoft-windows-infrastructure-2026.md)

---

# Applied Skills : différence importante

Les **Microsoft Applied Skills** sont de vrais credentials Microsoft basés sur une évaluation interactive en laboratoire portant sur des tâches réelles.

Ils sont donc plus forts qu'un simple Achievement Code Learn.

Mais cette revue n'a pas identifié d'Applied Skill public ayant **Azure Local** comme sujet principal explicite.

Source catalogue :

- https://learn.microsoft.com/en-us/credentials/applied-skills/

---

# Azure Local vs Windows Server 2025 — intérêt technique

Azure Local reste néanmoins une compétence importante pour les profils infrastructure Microsoft :

- Hyper-V VMs ;
- Storage Spaces Direct ;
- thin provisioning S2D ;
- ReFS deduplication ;
- Software-Defined Networking ;
- Network ATC ;
- secured-core ;
- GPU partitioning / HA GPU workloads ;
- Azure Arc management ;
- Azure Update Manager ;
- Azure Monitor ;
- AKS intégré ;
- Azure Migrate pour migrations VMware.

Microsoft distingue Azure Local comme une plateforme HCI cloud-connected, là où Windows Server reste un OS polyvalent et traditionnel.

Source :

- https://learn.microsoft.com/en-us/azure/azure-local/concepts/compare-windows-server

---

# État produit 2026

La branche Azure Local continue d'évoluer rapidement. La release **2607** de juillet 2026 est documentée par Microsoft comme la version 12.2607.1003.71.

Cela renforce l'intérêt de privilégier des credentials et contenus maintenus plutôt qu'une ancienne certification Azure Stack HCI devenue obsolète.

Source :

- https://learn.microsoft.com/en-us/azure/azure-local/whats-new

---

# Classement ROI Microsoft infra

```text
0 €    Azure Local Accreditation 2025       achievement
0 €    Windows Server 2025 Accreditation    achievement
126 €  AZ-802 Windows Server Administrator  certification
```

### Recommandation

```text
Windows Server 2025 Accreditation
          ↓
Azure Local Accreditation
          ↓
AZ-802
          ↓
Labs réels Azure Local / Hyper-V / S2D / Arc
```

Tant qu'un véritable **Applied Skill Azure Local** ou une certification Azure Local dédiée n'apparaît pas, **AZ-802 + pratique HCI** reste la voie la plus crédible.
