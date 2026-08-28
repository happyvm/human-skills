# Oracle Linux / KVM / Virtualization / Engineered Systems certifications — 2026

> Revue : **28 août 2026**. Complément aux fiches OCI et Database : focus Oracle Linux, KVM/OLVM et engineered systems.

---

# Résumé

| Credential | Prix de référence | Statut |
|---|---:|---|
| Oracle Linux Virtualization Manager Associate | **245 $ / exam attempt** hors promo/subscription | ✅ actuel |
| Oracle Linux 8 Advanced System Administration | **245 $ / exam attempt** hors promo/subscription | ✅ catalogue actuel |
| Oracle Exadata Database Machine X9M Implementation Essentials | **245 $ / exam attempt** hors entitlement | ✅ catalogue actuel |
| Exadata Database Service Professional | TBD | 🆕 annoncé octobre 2026 |
| Oracle VM 3.0 for x86 Essentials | legacy / retirement 30 avril 2026 | ❌ remplacé pour OPN virtualization |

---

# 1. Prix Oracle University

Oracle indique dans sa documentation d'achat qu'un **Oracle-delivered certification exam attempt** est valorisé à :

```text
245 $ / tentative
```

Points importants :

- pas de retake gratuit sur un achat standalone ;
- une tentative doit être appliquée à chaque passage ;
- certains Learning Subscriptions incluent des tentatives ;
- Foundations et certaines opportunités Associate peuvent faire l'objet d'accès gratuits / promotions selon le programme ;
- toujours vérifier le wallet MyLearn avant achat.

Source :

- https://docs.oracle.com/en/education/customer-success/digital-learning-kit/ml-cert-faq/topics/ExamAttemptPurchases.html

---

# 2. Oracle Linux Virtualization Manager Associate

Oracle a créé un nouveau learning path et une nouvelle certification pour son stack de virtualisation actuel :

- **Oracle Linux KVM** pour le compute ;
- **Oracle Linux Virtualization Manager (OLVM)** pour le management.

La certification **Oracle Linux Virtualization Manager Associate** valide notamment :

- installation de l'engine host ;
- installation / configuration des KVM hosts ;
- storage ;
- networking ;
- users ;
- optimisation des ressources ;
- gestion des VMs ;
- events / logs ;
- HA et disaster recovery ;
- backups de VMs / data warehouse.

Source officielle :

- https://blogs.oracle.com/virtualization/new-training-to-learn-about-oracle-virtualization

## Importance 2026

L'Oracle PartnerNetwork précise que l'ancien :

```text
Oracle VM 3.0 for x86 Essentials
```

est retiré le **30 avril 2026** pour le qualifier Oracle Virtualization et que :

```text
Oracle Linux Virtualization Manager Associate
```

devient le credential requis.

Source :

- https://www.oracle.com/partnernetwork/expertise/license-hardware/linux-virtualization/

### Verdict

À environ **245 $ par tentative** hors promo/subscription, OLVM Associate est une certification intéressante pour les profils private cloud / KVM, notamment en alternative ou complément à VMware / Nutanix / OpenStack.

---

# 3. Oracle Linux 8 Advanced System Administration

Le catalogue Oracle Certification 2026 liste toujours :

- **Oracle Linux 8 Advanced System Administration**.

Oracle ne met plus autant en avant une pyramide Linux classique que certains vendors, mais ce credential reste dans le catalogue Technology Certifications.

Source :

- https://www.oracle.com/education/certification/

### Prix

Référence générique d'un exam attempt Oracle : **245 $**.

Vérifier MyLearn pour confirmer que l'examen ciblé utilise bien une tentative standard au moment de l'achat.

---

# 4. Oracle Linux KVM — stack technique actuelle

Oracle présente KVM comme son hyperviseur open source actuel et OLVM comme la couche de management.

En 2026 :

```text
Oracle Linux 8 / 9
Oracle Linux KVM
Oracle Linux Virtualization Manager 4.5
```

sont les briques à connaître.

Le HCL Oracle confirme notamment :

- OL9 support KVM ;
- UEK R8 ;
- Intel VT / AMD-V ;
- iSCSI ;
- Fibre Channel ;
- NFS ;
- third-party software-defined storage.

Source :

- https://linux.oracle.com/ords/r/oraclelinux/hardware-certifications/virtualization

---

# 5. Oracle Engineered Systems / Exadata

Le catalogue Technology Certifications liste notamment :

- **Oracle Exadata Database Machine X9M Implementation Essentials**.

Référence exam attempt Oracle : **245 $**, sous réserve du checkout MyLearn du credential exact.

Source :

- https://www.oracle.com/education/certification/

---

# 6. Nouveau : Exadata Database Service certification — octobre 2026

Oracle University a annoncé le **10 août 2026** deux nouveaux parcours à venir :

- Multicloud Foundations — prévu septembre 2026 ;
- **Exadata Database Service** — certification professional-level prévue **octobre 2026**.

Source :

- https://blogs.oracle.com/oracleuniversity/oci-certification-learning-paths-and-exams-2026-updates-now-available

### Watchlist

Dès publication : relever

```text
exam name
exam fee
free vs paid access
hands-on performance exam éventuel
validity
renewal
```

---

# 7. Oracle certifications gratuites : attention au périmètre

OCI a élargi ses certifications gratuites en 2026, particulièrement les Foundations et certains parcours cloud/AI.

Cela ne signifie pas que **tous** les examens Oracle Technology sont gratuits.

Pour Linux / OLVM / engineered systems, utiliser :

```text
245 $ standard exam attempt
```

comme budget conservateur tant que MyLearn ne montre pas une promotion ou une tentative incluse.

---

# Shortlist Oracle infrastructure

```text
0 $ / €   plusieurs OCI / Foundations selon programme
245 $     Oracle Linux Virtualization Manager Associate
245 $     Oracle Linux 8 Advanced System Administration
245 $     Exadata X9M Implementation Essentials — référence exam attempt
TBD       Exadata Database Service Professional — octobre 2026
```

## Parcours private cloud pertinent

```text
Oracle Linux / KVM / OLVM      245 $
OpenStack COA                  400 $
CloudStack                     100 $
```

OLVM est particulièrement intéressant si l'objectif est de couvrir une vraie alternative KVM enterprise en plus de Proxmox/OpenStack/Nutanix/VMware.
