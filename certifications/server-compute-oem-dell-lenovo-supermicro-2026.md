---
title: "Server / compute OEM certifications — Dell, Lenovo, Supermicro — 2026"
type: certification-catalog
tier: general
domain:
  - datacenter-facilities
tags:
  - tier/general
  - domain/datacenter-facilities
status: active
verified: 2026-08-28
---

# Server / compute OEM certifications — Dell, Lenovo, Supermicro — 2026

> Revue : **28 août 2026**. Focus : certifications serveurs, compute, GPU/HPC et datacenter hardware hors HPE, déjà traité séparément.

---

# Résumé

| Vendor | Credential / programme | Prix public observé | Statut |
|---|---|---:|---|
| Dell | Proven Professional Skill Certification | **230 $ retail** | ✅ sous 500 |
| Dell Partner | même Skill Certification | **115 $** avec remise partenaire publiée | ✅ excellent si éligible |
| Lenovo | Data Center Technical Certification | prix non public clairement exposé | 🔎 employee/partner centric |
| Supermicro | Partner training / certification | prix et examen public non exposés | 🔎 portal-centric |

---

# 1. Dell Technologies / PowerEdge

Dell a un portefeuille 2026 particulièrement intéressant pour l'infrastructure physique et AI/HPC.

## Prix générique Proven Professional

La documentation Dell récente indique :

```text
Skill Certification Exam retail     230 $
Partner discounted price            115 $
```

Les Skills Certification Exams sont proctorés via **Pearson VUE**, sur site ou OnVUE.

La remise partenaire documentée utilise le programme / code partenaire actif ; elle ne doit être utilisée que par les candidats éligibles.

Source :

- https://learning.dell.com/content/dam/dell-emc/documents/en-us/How_to_Schedule_and_Take_an_Exam_Partners.pdf

---

## PowerEdge Foundations — D-PE-FN-01

Certification actuelle couvrant notamment :

- architectures et form factors PowerEdge ;
- composants serveur ;
- cooling / thermal ;
- networking ;
- maintenance ;
- troubleshooting ;
- sécurité hardware ;
- Silicon Root of Trust ;
- Secure Boot / TPM 2.0 ;
- iDRAC ;
- data protection.

Elle est adaptée aux infrastructure administrators, cloud architects, systems engineers et solution architects.

Source :

- https://learning.dell.com/content/dell/en-us/home/certification-overview/available-exams.html?exam=D-PE-FN-01

---

## PowerEdge Operate — D-PE-OE-01

Track opérationnel orienté :

- iDRAC ;
- Lifecycle Controller ;
- RACADM ;
- OpenManage / OME ;
- RAID / storage ;
- BIOS / firmware ;
- health monitoring ;
- troubleshooting ;
- OS installation ;
- server security.

Source :

- https://learning.dell.com/content/dell/en-us/home/certification-overview/available-exams.html?exam=D-PE-OE-01

---

## PowerEdge XE — AI / HPC

Dell maintient également des credentials ciblant ses serveurs GPU/HPC.

### PowerEdge XE Operate — D-PEXE-OE-00

Le credential valide l'exploitation de PowerEdge XE utilisés pour :

- high-performance computing ;
- AI ;
- Generative AI ;
- GPU infrastructure ;
- server management / monitoring.

Source :

- https://learning.dell.com/content/dell/en-us/home/certification-overview/available-exams.html?exam=D-PEXE-OE-00

### PowerEdge XE Install

L'ancien D-PEXE-IN-A-00 a été retiré le **9 juillet 2026** et remplacé le **10 juillet 2026** par **D-PEXE-IN-A-01**.

Le track porte sur installation physique, racking, cabling et GPU supportability des plateformes PowerEdge XE.

Source :

- https://learning.dell.com/content/dell/en-us/home/certification-overview/available-exams.html?exam=D-PEXE-IN-A-00

### Verdict Dell

À **230 $ retail**, Dell PowerEdge est une excellente brique pour matérialiser une compétence serveurs physiques — souvent absente des parcours cloud/VMware classiques.

Pour un partenaire éligible, **115 $** devient extrêmement compétitif.

---

# 2. Lenovo Data Center Technical Certification

Lenovo publie encore en **juillet 2026** un :

- **Lenovo Data Center Technical Certification Exam Study Guide** ;
- contenu de préparation pour les examens Data Center Technical ;
- accès via Grow@Lenovo pour employés et Lenovo 360 Learning Center pour partenaires.

Le guide est référencé autour de nombreux serveurs / stockage ThinkSystem actuels, y compris les plateformes AI/GPU.

### Problème catalogue

Le prix standalone public et l'accès candidat individuel hors écosystème Lenovo ne sont pas clairement exposés sur les pages publiques 2026.

Donc :

```text
credential live / programme actif     oui
prix public individuel                non confirmé
classification                        partner / employee centric
```

Sources :

- https://lenovopress.lenovo.com/lp1611-thinksystem-sr675-v3-server
- Lenovo course code LENU-322C-SG — Data Center Technical Certification Exam Study Guide

### À surveiller

- ThinkSystem / infrastructure ;
- AI / GPU servers ;
- Neptune liquid cooling ;
- storage ;
- Lenovo Hybrid AI / HPC.

---

# 3. Supermicro

Supermicro dispose d'un portail partenaire avec :

- training ;
- contenus AI / GPU ;
- liquid cooling ;
- rack-scale infrastructure ;
- mention explicite **Training and Support — Access Training and getting Supermicro Certified** dans MySupermicro.

Cependant, lors de la revue publique il n'a pas été possible d'identifier proprement :

- le nom d'un examen professionnel individuel actuel ;
- un blueprint public ;
- un prix public ;
- un mécanisme d'achat individuel hors portail partenaire.

### Ne pas confondre

Supermicro publie beaucoup de **NVIDIA-Certified Systems**. Cette certification concerne **le matériel/système**, pas une certification professionnelle de la personne.

```text
NVIDIA-Certified Supermicro System
!=
Supermicro Certified Professional
```

Sources :

- https://www.supermicro.com/en/mysupermicro
- https://www.supermicro.com/en/channel-portal
- https://www.supermicro.com/en/accelerators/nvidia-certified-systems

### Verdict

Supermicro reste une **watchlist portal-centric**. Pour certifier des compétences AI infrastructure sur du matériel Supermicro, les certifications NVIDIA NCA/NCP constituent aujourd'hui un signal public beaucoup plus accessible.

---

# 4. HPE — voir fiche dédiée

HPE est couvert dans :

- [`hpe-certification-pricing-ai-private-cloud-2026.md`](hpe-certification-pricing-ai-private-cloud-2026.md)

Rappel grille :

```text
HPE3    65 $
HPE2   140 $
HPE0   260 $
HPE6   260 $
HPE7   350 $
```

Le parcours Compute Solutions 2026 couvre désormais HPE Compute, Morpheus VM Essentials, OneView, OpsRamp, AI/ML, Ezmeral et containers selon options.

---

# Shortlist server / compute

```text
65 $     HPE3 exam
115 $    Dell Skill Certification — partenaire éligible
140 $    HPE2 exam
230 $    Dell Proven Professional Skill Certification retail
260 $    HPE0 / HPE6
350 $    HPE7
390 $    HPE ATP AI Solutions — combinaison d'examens documentée
?        Lenovo Data Center Technical — portal/partner
?        Supermicro professional certification — portal/partner
```

Pour un candidat individuel : **Dell PowerEdge à 230 $** est actuellement le meilleur credential serveur OEM clairement public après HPE.
