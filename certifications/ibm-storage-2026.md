---
title: "IBM Storage — certifications et credentials 2026"
type: certification-catalog
tier: general
domain:
  - storage-backup
scope:
  - international
tags:
  - tier/general
  - domain/storage-backup
  - scope/international
status: active
verified: 2026-08-28
---

# IBM Storage — certifications et credentials 2026

> IBM Storage a changé de génération : plusieurs anciennes certifications Spectrum sont retirées, tandis que Storage Scale, FlashSystem/Storage Virtualize et Storage Defender utilisent désormais un mélange de certifications, validations et learning paths. Vérification : 28 août 2026.

---

# Règle de méthode IBM

IBM utilise plusieurs types de credential qui ne doivent pas être confondus :

- **IBM Professional Certification** — examen Pearson VUE / certification professionnelle ;
- **IBM Validation / badge** — cours + assessment / quiz ;
- **IBM learning path** — peut contenir un bouton `Purchase Certification Exam` sans exposer le prix public ;
- **technical sales badge** — parfois réservé aux employés / partners.

Le dépôt conserve donc le type de preuve exact au lieu d'appeler tout « certification ».

**Auto-formation officielle et gratuite (IBM, toute la gamme ci-dessous) :** [IBM SkillsBuild](https://skillsbuild.org/) — 1000+ cours gratuits, dont *Introduction to IBM Storage and Cloud* (DL08015G).

---

# IBM Storage Scale Administrator — actif, mais modèle hybride

IBM publie un learning path **IBM Storage Scale Administrator**.

La page indique :

- les formations Fundamentals, Administration et Remote Data Access sont **Optional** ;
- un bouton **Purchase Certification Exam** renvoie vers Pearson VUE ;
- les Gold/Platinum Partners peuvent parfois avoir accès sans coût via Partner Plus ;
- le prix final de l'examen n'est pas affiché publiquement sur la page.

Source :

- https://www.ibm.com/training/learning-path/ibm-storage-scale-administrator-913

### Statut

```yaml
name: IBM Storage Scale Administrator
program_status: active
training_required: false / optional on learning path
exam_purchase: Pearson VUE
public_exam_price: TBD
partner_free_access: possible for eligible Partner Plus tiers
status: PRICE-OPAQUE
```

---

# Attention : badge Storage Scale ≠ certification pro

IBM/Credly publie également un badge **IBM Storage Scale Administrator** obtenu en complétant le cours d'administration et son final quiz.

Ce badge est de type **Validation**, pas nécessairement le même objet que la certification achetable via Pearson VUE.

Source :

- https://www.credly.com/org/ibm/badge/ibm-storage-scale-administrator

Le dépôt distingue donc :

```text
Course validation badge
!=
Pearson VUE professional certification path
```

---

# Spectrum Protect Plus — génération 10.1.9

## Ancien credential 10.1.5

`IBM Certified Deployment Professional - Spectrum Protect Plus V10.1.5` :

- credential code `C0001101` ;
- statut : **Expire** ;
- exam : **Withdrawn** ;
- remplacé par **C9003600**.

Source :

- https://www.ibm.com/training/certification/ibm-certified-deployment-professional-spectrum-protect-plus-v1015-C0001101

---

## Remplaçant : Spectrum Protect Plus V10.1.9

Credential :

**IBM Certified Deployment Professional - Spectrum Protect Plus V10.1.9**

- code : **C9003600** ;
- exam : **C1000-146 — IBM Spectrum Protect Plus V10.1.9 Implementation** ;
- type Credly : **Certification** ;
- niveau : Intermediate ;
- coût : Paid.

Source de credential vérifiable :

- https://www.credly.com/org/ibm-professional-certification-program/badge/ibm-certified-deployment-professional-spectrum-prot

### Prix

Le prix public actuel n'est pas suffisamment exposé dans les pages IBM indexables pour être figé sans checkout.

```yaml
exam_code: C1000-146
credential_code: C9003600
public_price: TBD
status: ACTIVE-CREDENTIAL / PRICE-OPAQUE
```

> Ne pas reprendre automatiquement le tarif IBM $200 d'autres certifications : il faut confirmer ce code précis au checkout.

---

# IBM Storage Scale — formations actuelles

Les cours actifs incluent notamment :

- H005G — Basic Administration ;
- H006G — Advanced Administration ;
- H008G — Remote Data Access ;
- variantes digitales / intensive learning.

Sources :

- https://www.ibm.com/training/course/ibm-storage-scale-advanced-administration-for-linux-H006G
- https://www.ibm.com/training/course/ibm-storage-scale-remote-data-access-H008G

Ces cours donnent également des badges de formation/validation, mais ne sont pas obligatoires sur le learning path de certification actuellement publié.

---

# FlashSystem / Storage Virtualize

IBM publie en 2026 un nouveau contenu **IBM FlashSystem Fundamentals** couvrant :

- FlashCore Modules ;
- Storage Virtualize ;
- data reduction ;
- FlashCopy ;
- replication ;
- Safeguarded Copy ;
- policy-based protection ;
- hybrid cloud integration ;
- resilience.

Source :

- https://www.ibm.com/training/course/ibm-flashsystem-fundamentals-SSFS1G

Une version digitale précédente indique explicitement qu'une nouvelle version gratuite du cours Fundamentals est disponible.

Source :

- https://www.ibm.com/training/course/ibm-flashsystem-fundamentals-digital-course-SSFS1DG

### Credential status

Au moment de la revue, les résultats officiels publics exposent surtout :

- cours ;
- badges techniques ;
- learning paths.

Aucune certification professionnelle FlashSystem 2026 avec **nom + exam code + prix public** n'a été identifiée suffisamment proprement pour être ajoutée comme examen payant.

**Statut : `BADGES/TRAINING-ACTIVE — PROFESSIONAL-CERT-TBD`.**

---

# Storage Defender

IBM Storage Defender Data Protect dispose de formations actuelles.

Exemple :

**IBM Storage Defender Data Protect Setup and Configuration — SSCH2G**

- 8 h ;
- deployment / cluster management ;
- Linux-based labs ;
- training payant via providers.

Source :

- https://www.ibm.com/training/course/ibm-storage-defender-data-protect-setup-and-configuration-SSCH2G

Au moment de la revue, la recherche publique ne montre pas encore une certification professionnelle Storage Defender avec un prix/exam code suffisamment clair.

**Statut : `TRAINING-ACTIVE / PROFESSIONAL-CERT-TBD`.**

---

# IBM Storage legacy — ne pas recopier

Beaucoup de certifications historiques IBM Storage sont retirées :

- anciennes Storage Technical Specialist ;
- Storwize Family Technical Solutions ;
- Enterprise/Midrange Storage credentials anciens ;
- Spectrum Protect Plus 10.1.5 ;
- Spectrum Protect v8.x historiques selon code/version.

Exemple officiel :

- `IBM Certified Specialist - Storage Technical V1` retiré depuis 2019.

Source :

- https://www.ibm.com/training/certification/ibm-certified-specialist-storage-technical-v1-23003306

Avant d'ajouter un credential IBM provenant d'un CV, d'un dump site ou d'un ancien guide : vérifier `Certification status` et `Exam status` sur IBM.

---

# Ce qui reste intéressant gratuitement

IBM fournit plusieurs cours / badges Storage gratuits ou peu coûteux, notamment autour de :

- FlashSystem Fundamentals ;
- Storage Scale learning assets ;
- technical essentials.

Ils doivent être classés **badge / validation**, pas professional certification, sauf examen IBM explicitement identifié.

---

# Priorités IBM Storage

1. **Storage Scale Administrator** — récupérer prix Pearson VUE exact ;
2. **Spectrum Protect Plus 10.1.9 C9003600** — confirmer prix C1000-146 ;
3. identifier le nouveau credential Storage Protect/Defender successeur ;
4. surveiller FlashSystem/Storage Virtualize professional certifications 2026 ;
5. conserver les badges Fundamentals comme compléments gratuits.

---

# À poursuivre

- Pearson VUE IBM exam catalog pour Storage Scale ;
- C1000-146 price France ;
- Storage Protect Plus 10.1.9 current retirement/replacement date ;
- Storage Protect 8.1.x successor ;
- Storage Defender professional certification ;
- FlashSystem / Storage Virtualize current exam ;
- DS8000 ;
- IBM Tape / TS7700 ;
- IBM Cloud Object Storage ;
- Storage Scale System / ESS ;
- IBM Fusion / Storage Fusion ;
- IBM Power + Storage integration.
