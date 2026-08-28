---
title: "Open-source / cloud-native storage certifications — Ceph, Longhorn, MinIO, Portworx — 2026"
type: certification-catalog
tier: general
domain:
  - storage-backup
tags:
  - tier/general
  - domain/storage-backup
status: active
verified: 2026-08-28
---

# Open-source / cloud-native storage certifications — Ceph, Longhorn, MinIO, Portworx — 2026

> Revue : **28 août 2026**. Périmètre : stockage distribué, object storage et Kubernetes storage, avec distinction entre certifications réellement actives et simples formations.

---

# Résumé

| Technologie / vendor | Credential | Prix public observé | Statut |
|---|---|---:|---|
| SUSE / Longhorn | SCA in Longhorn | **149 $** | ✅ excellent ROI |
| MinIO | Certified Administrator - Practitioner | **300 $** | ✅ sous 500 |
| Portworx / Everpure | Portworx Enterprise Professional | **300 $** affiché Academy | ✅ sous 500 |
| Red Hat / Ceph | EX260 / Ceph Cloud Storage | tarif Red Hat régional | ⚠️ France/EMEA généralement >500 € |
| Ceph Foundation / LF | certification Ceph standalone vendor-neutral | non identifiée | ❌ ne pas inventer |
| OpenEBS | certification professionnelle officielle | non identifiée | ❌ watchlist |

---

# 1. SUSE Certified Administrator in Longhorn — 149 $

Longhorn est la couche de stockage cloud-native open source de l'écosystème Rancher / SUSE Storage.

La certification **SUSE Certified Administrator (SCA) in Longhorn** est active et valide les compétences :

- architecture Longhorn ;
- installation Helm / Rancher ;
- gestion des nodes et disques ;
- volumes et resizing ;
- réplication et data locality ;
- monitoring Prometheus / Grafana ;
- snapshots ;
- backups / restore ;
- disaster recovery volumes ;
- upgrades.

## Examen

```text
Prix          149 $
Questions      70
Durée          90 min
Passing        70 %
Cours requis   non
Code           sca_lhn1_5
```

Il n'y a **aucun prérequis** et le cours LHN201 est recommandé mais non obligatoire.

Source :

- https://www.suse.com/training/exam/sca-longhorn/

### Verdict

À 149 $, c'est probablement la meilleure certification stockage Kubernetes identifiée dans ce catalogue en rapport coût / signal.

---

# 2. MinIO Certified Administrator - Practitioner — 300 $

MinIO maintient un vrai programme de certification autour de son object storage / AIStor.

La certification actuelle est :

- **MinIO Certified Administrator - Practitioner**.

Des certifications Developer et Architect sont annoncées comme futures extensions du programme.

## Examen

```text
Prix               300 $ / tentative
Durée               90 min
Questions            60 QCM
Delivery             Prometric / remote ProProctor
Training prerequisite non
Validité             3 ans
```

Le candidat doit maîtriser notamment :

- déploiement MinIO ;
- buckets ;
- versioning ;
- lifecycle ;
- replication ;
- encryption ;
- authentication ;
- sécurité ;
- administration et scaling d'un cluster de production.

La formation MinIO n'est **pas un prérequis**.

Sources :

- https://www.min.io/training/certification
- https://www.min.io/academy-faqs

## Learning Subscription

MinIO propose également une subscription individuelle autour de **700 $**, comprenant cours, labs et un voucher de certification. Elle n'est pas nécessaire pour acheter l'examen standalone à 300 $.

Source :

- https://min.io/training/learningsubscription

---

# 3. Portworx Enterprise Professional

Pure / Everpure maintient une certification **Portworx Enterprise Professional (PEP)** orientée stockage et data management Kubernetes.

Le portail Academy affiche :

```text
Portworx Enterprise Professional   300 $
```

Le portail précise que le prix final est confirmé dans le storefront d'inscription.

La préparation peut s'appuyer sur :

- Portworx Fundamentals ;
- Portworx Enterprise Administration ;
- study guide officiel ;
- expérience pratique.

La formation est décrite comme recommandée / optionnelle dans les guides de préparation ; ne pas confondre les coûteux bundles ILT avec le prix de l'examen standalone.

### Attention à une divergence documentaire

Un study guide Pure 2025 a également affiché **400 $** pour une version récente de l'examen, tandis que l'Academy visible en 2026 affiche **300 $** et demande de confirmer le tarif dans le storefront.

Pour le catalogue :

```text
reference Academy 2026    300 $
checkout final            à confirmer
```

Sources :

- https://academy.purestorage.com/student/activity/2164521-certification-pep
- https://support-be.purestorage.com/bundle/portworx_enterprise_professional_pep_12062024/raw/resource/enus/portworx_enterprise_professional_pep_12062024.pdf

### Verdict

Même avec la divergence 300/400 $, Portworx reste sous le plafond de 500 $ pour l'examen standalone.

---

# 4. Ceph — Red Hat reste le credential principal

Le credential professionnel Ceph le plus identifiable reste le parcours Red Hat autour de **Ceph Cloud Storage / EX260**.

Des certifications vérifiables Red Hat montrent encore des réussites EX260 en **2026**, ce qui confirme que le credential existe toujours dans le programme actuel.

Cependant, les tarifs Red Hat sont régionaux. Les observations EMEA utilisées dans ce dépôt montrent qu'un Individual/KIOSK exam peut dépasser **500 € HT/TTC selon canal**, donc EX260 ne doit pas être classé comme certification low-cost en France.

Sources :

- https://www.redhat.com/en/services/certification
- vérification publique Red Hat des credentials EX260

---

# 5. Ceph Foundation / Linux Foundation

Aucune certification professionnelle officielle **Ceph standalone** de type « Certified Ceph Administrator » n'a été identifiée dans le catalogue Linux Foundation / OpenInfra / Ceph Foundation lors de la revue.

Il existe beaucoup de formations Ceph et du contenu communautaire, mais :

```text
formation Ceph
!=
certification professionnelle Ceph officielle
```

Ne pas inventer un credential vendor-neutral absent du catalogue.

---

# 6. OpenEBS

OpenEBS est un projet CNCF important pour le stockage Kubernetes, mais aucune certification professionnelle officielle OpenEBS distincte n'a été identifiée lors de cette revue.

À conserver en watchlist.

---

# Shortlist stockage cloud-native / open source

```text
149 $   SUSE Certified Administrator in Longhorn
300 $   MinIO Certified Administrator - Practitioner
300 $*  Portworx Enterprise Professional — Academy, checkout à confirmer
>500€   Red Hat Ceph EX260 — cas France/EMEA typique
```

## Parcours très cohérent

```text
Longhorn       149 $
MinIO          300 $
-------------------
Total          449 $
```

Pour **449 $**, ce duo couvre à la fois :

- persistent block storage Kubernetes ;
- backup / DR cloud-native ;
- object storage S3-compatible ;
- déploiement et administration distribuée.
