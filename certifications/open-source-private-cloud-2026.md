---
title: "Open-source private cloud certifications — 2026"
type: certification-catalog
tier: general
domain:
  - virtualization
tags:
  - tier/general
  - domain/virtualization
status: active
verified: 2026-08-28
---

# Open-source private cloud certifications — 2026

> Revue : **28 août 2026**. Priorité aux certifications réellement achetables sans bundle de formation obligatoire quand le prix public est disponible.

## Résumé

| Écosystème | Credential | Prix public observé | Statut |
|---|---|---:|---|
| OpenStack | Certified OpenStack Administrator (COA) | **400 $** | ✅ sous 500 |
| Apache CloudStack / ShapeBlue | Apache CloudStack Certification by ShapeBlue | **100 $** | ✅ très bon rapport coût/signal |
| OpenNebula | OpenNebula 7.4 Certified Administrator Training | **899 €** EMEA | ❌ > 500 |
| OpenNebula | OpenNebula 7.4 Certified Expert Training | **999 €** EMEA | ❌ > 500 |

---

# OpenStack

## Certified OpenStack Administrator — COA

La **COA** reste la certification professionnelle officielle soutenue par l'OpenInfra Foundation pour OpenStack. L'infrastructure d'examen est administrée par **Mirantis**.

**Auto-formation officielle et gratuite :** cours **OS100 OpenStack Essentials** gratuit par Mirantis, via [openstack.org/marketplace/training](https://www.openstack.org/marketplace/training/).

- format : examen pratique / performance-based ;
- administration : Mirantis pour le compte de l'écosystème OpenInfra/OpenStack ;
- prix public Mirantis observé : **400 $** ;
- positionnement : exploitation quotidienne et administration d'un cloud OpenStack ;
- intérêt : rare certification vendor-neutral réellement centrée sur l'exploitation OpenStack.

### Verdict

**Très intéressante pour un profil infrastructure/private cloud.** À 400 $, elle rentre dans le plafond de 500 et offre un signal plus différenciant qu'une certification cloud hyperscaler généraliste.

Sources :

- https://training.mirantis.com/certification
- https://openinfra.org/annual-report/2023/
- https://www.openstack.org/marketplace/training/mirantis/mirantis-training-for-openstack

---

# Apache CloudStack

## Apache CloudStack Certification by ShapeBlue

ShapeBlue propose une certification technique CloudStack avec examen online proctoré.

**Auto-formation officielle :** [shapeblue.com/cloudstack-training](https://www.shapeblue.com/cloudstack-training/) — bootcamps instructor-led + labs hands-on.

- prix de l'examen : **100 $** ;
- examen disponible en complément du bootcamp, avec possibilité de certification technique CloudStack ;
- surveillance : proctoring en ligne ;
- sujets associés au bootcamp : architecture CloudStack, networking, stockage, KVM/XenServer/VMware, API, CloudMonkey, troubleshooting, Kubernetes, migration, GPU, object storage, vTPM, etc.

> Important : il s'agit d'une certification **émise par ShapeBlue autour d'Apache CloudStack**, et non d'une certification directement émise par l'Apache Software Foundation.

### Verdict

À **100 $**, c'est probablement l'un des meilleurs credentials low-cost pour quelqu'un qui veut démontrer une compétence **IaaS/private cloud open source** hors OpenStack.

Sources :

- https://www.shapeblue.com/cloudstack-training
- https://www.shapeblue.com/wp-content/uploads/2025/06/Apache-CloudStack-Certification-Exam-Requirements.pdf

---

# OpenNebula

OpenNebula dispose d'une Academy officielle et de formations certifiantes, mais les parcours certifiants dépassent actuellement le seuil de 500 €.

**Auto-formation officielle :** [OpenNebula Academy](https://opennebula.io/opennebula-academy/) — documentation, tutoriels et microlearnings gratuits en complément des sessions certifiantes payantes.

## OpenNebula 7.4 Certified Administrator Training

- prix EMEA à partir de : **899 €** ;
- prix Americas à partir de : **1 140 $** ;
- format : formation online en petit groupe, labs pratiques et certification officielle.

## OpenNebula 7.4 Certified Expert Training

- prix EMEA à partir de : **999 €** ;
- prix Americas à partir de : **1 260 $**.

OpenNebula Academy propose également un **Practitioner course gratuit**, utile comme formation d'introduction, mais à ne pas confondre avec les parcours Administrator/Expert certifiants payants.

### Verdict

Techniquement pertinent pour le private cloud européen, mais **hors budget <500 €** en achat individuel. À envisager surtout avec financement employeur.

Source :

- https://opennebula.io/opennebula-academy/

---

# Classement ROI

```text
100 $   CloudStack Certification by ShapeBlue
400 $   OpenStack COA
899 €   OpenNebula Certified Administrator Training
999 €   OpenNebula Certified Expert Training
```

Pour une stratégie private cloud à coût contenu : **CloudStack → OpenStack COA** donne deux signaux techniques complémentaires pour environ 500 $ au total.
