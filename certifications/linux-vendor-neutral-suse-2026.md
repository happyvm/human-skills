# Linux vendor-neutral & SUSE — certifications 2026

> LPI, SUSE, CompTIA Linux+ et Canonical Academy. Vérification : 28 août 2026.

---

# Vue rapide

| Credential | Prix officiel / indicatif | TCO minimal |
|---|---:|---:|
| LPI Essentials | **110 €** | 110 € |
| LPI professional exam | **176 €** | selon titre |
| LPIC-1 | 2 × 176 € | **352 €** |
| LPIC-2 | 2 × 176 € | **352 €** + LPIC-1 actif |
| LPIC-3 | 176 € | **176 €** + LPIC-2 actif |
| LPI DevOps Tools Engineer | **176 €** | 176 € |
| LPI BSD Specialist | **176 €** | 176 € |
| SUSE SLES 16 Administrator | **149 $** | 149 $ |
| SUSE SLES High Availability Engineer | **195 $** | + prerequisite SCA depending path |
| SUSE SLES for SAP Applications | **149 $ par exam** | 2 exams + HA prereq |
| SUSE Multi-Linux Manager Admin | **149 $** | 149 $ |
| SUSE Edge Deployment Specialist | **149 $** | 149 $ |
| CompTIA Linux+ XK0-006 | regional / official-store opaque in crawl | partner Europe ~349 € indicative |
| Canonical Academy Ubuntu | shop exists | price to confirm in shop |

---

# Linux Professional Institute — France / Eurozone

LPI publie une grille régionale officielle.

## Essentials

- Linux Essentials — **110 €** ;
- Security Essentials — **110 €** ;
- Web Development Essentials — **110 €** ;
- Open Source Essentials — **110 €**.

## Professional / Open Technology

Chaque examen est à **176 €** dans la grille EUR :

- LPIC-1: 101 ;
- LPIC-1: 102 ;
- LPIC-2: 201 ;
- LPIC-2: 202 ;
- LPIC-3 Mixed Environment 300 ;
- LPIC-3 Security 303 ;
- LPIC-3 Virtualization and Containerization 305 ;
- LPIC-3 High Availability and Storage Clusters 306 ;
- DevOps Tools Engineer 701 ;
- BSD Specialist 702.

Source :

- https://www.lpi.org/exam-pricing/

---

# LPIC-1

LPIC-1 requiert :

- 101 ;
- 102.

Coût examen :

```text
101        176 €
102        176 €
----------------
LPIC-1     352 €
```

Formation non obligatoire.

**Valeur : ⭐⭐⭐⭐** vendor-neutral Linux.

---

# LPIC-2

LPIC-2 requiert :

- LPIC-1 actif ;
- examens 201 et 202.

Coût incrémental :

```text
201        176 €
202        176 €
----------------
LPIC-2     352 € incremental
```

Depuis zéro :

```text
LPIC-1     352 €
LPIC-2     352 €
----------------
Total      704 €
```

hors retakes.

---

# LPIC-3 — excellent coût incrémental

Une certification LPIC-3 nécessite :

- un LPIC-2 actif ;
- **un seul examen LPIC-3** dans la spécialité choisie.

Chaque examen : **176 €**.

Spécialités :

- Mixed Environment ;
- Security ;
- Virtualization and Containerization ;
- High Availability and Storage Clusters.

Le coût incrémental d'une spécialisation LPIC-3 est donc seulement :

```text
176 €
```

une fois LPIC-2 détenu.

**Valeur / coût incrémental : ⭐⭐⭐⭐⭐**.

---

# LPI DevOps Tools Engineer

- examen 701 ;
- **176 €** ;
- credential indépendant du chemin LPIC classique selon programme LPI.

Compétences :

- containers ;
- CI/CD ;
- configuration management ;
- monitoring ;
- infrastructure automation ;
- software engineering practices.

**Valeur : ⭐⭐⭐⭐**.

---

# LPI BSD Specialist

- examen 702 ;
- **176 €**.

Très niche, mais excellent signal pour BSD / Unix.

---

# Promotions événements LPI

LPI organise ponctuellement des sessions papier à tarif réduit.

Exemple FrOSCon 2026 :

- Essentials : **70 €** ;
- professional-level exams : **110 €**.

Source :

- https://www.lpi.org/event/froscon-26/

Ces prix sont `PROMO/EVENT`, pas tarifs catalogue.

---

# SUSE Linux Enterprise Server 16

## SCA in SLES 16

- **149 $** ;
- 70 questions ;
- 90 min ;
- aucun prérequis ;
- course SLE201v16 recommandé ;
- **coursework non obligatoire**.

Source :

- https://www.suse.com/training/exam/sca_sles16/

Compétences :

- shell / Bash ;
- users/groups ;
- storage ;
- networking ;
- SSH / Cockpit ;
- firewall ;
- SELinux ;
- logging ;
- troubleshooting.

**Valeur / prix : ⭐⭐⭐⭐⭐** si SUSE est utilisé.

---

# SUSE SLES 15 — version encore active

SUSE garde également le SCA SLES 15 (2025 Update) :

- **149 $** ;
- pas de prérequis ;
- coursework non obligatoire.

Source :

- https://www.suse.com/fr-fr/training/exam/sca-sles-15/

Pour un nouveau candidat, SLES 16 est naturellement à privilégier sauf contrainte de version d'entreprise.

---

# SUSE High Availability

## SCE in SUSE Linux Enterprise High Availability 15

- **195 $** ;
- 70 questions ;
- 90 min ;
- cluster / Pacemaker ;
- Hawk2 ;
- DRBD ;
- OCFS2 ;
- clustered LVM ;
- NFS HA ;
- troubleshooting.

Source :

- https://www.suse.com/training/exam/sce-sle-ha-15/

**Valeur : ⭐⭐⭐⭐⭐** pour HA Linux enterprise.

---

# SLES for SAP Applications

Le SCE SLES for SAP Applications 15 requiert :

- SCE SLE High Availability prerequisite ;
- deux examens core ;
- **149 $ chacun**.

Les cours ne sont pas obligatoires.

Source :

- https://www.suse.com/training/exam/sce-sles-sap-15/

### Exam TCO minimal du titre après prerequisite

```text
Part 1      149 $
Part 2      149 $
----------------
Increment   298 $
```

Depuis un candidat sans HA prerequisite, ajouter le coût du chemin prerequisite applicable.

---

# SUSE Multi-Linux Manager

## SCA in SUSE Multi-Linux Manager

- **149 $** ;
- aucun prérequis ;
- coursework non obligatoire ;
- gestion multi-distributions, patching, registration et Content Lifecycle Management.

Source :

- https://www.suse.com/training/exam/sca_smlm/

**Valeur : ⭐⭐⭐⭐** pour patch/config management Linux enterprise.

---

# SUSE Edge

## Certified Deployment Specialist in SUSE Edge

- **149 $** ;
- edge clusters ;
- image builder ;
- Metal3 / Cluster API ;
- Rancher ;
- telco / RAN concepts ;
- provisioning.

Source :

- https://www.suse.com/training/exam/scds-edge/

**Valeur : ⭐⭐⭐⭐** pour edge/telco/cloud-native infra.

---

# SUSE certification philosophy

SUSE précise sur ses pages que **les cours ne sont pas obligatoires** : il faut réussir l'examen et satisfaire les éventuels prérequis.

Cela rend les examens SUSE à 149–195 $ particulièrement compétitifs par rapport à des certifications qui imposent un training bundle.

---

# CompTIA Linux+ XK0-006

Le programme Linux+ XK0-006 est actif.

Le prix exact dépend de la région. Au moment de la revue, le crawler ne renvoie pas une page CompTIA store publique suffisamment propre pour figer le prix France officiel.

Des partenaires CompTIA Delivery Partner européens affichent un voucher exam-only autour de **349 €**, tandis que les références de voucher internationales indiquent un retail autour de 390–399 $ selon région.

### Statut

```yaml
exam: XK0-006
official_program: active
mandatory_training: false
france_official_price: CHECKOUT-REQUIRED
partner_eu_exam_only: ~349 EUR indicative
```

> Ne pas confondre avec les formations partenaires à plusieurs milliers d'euros : la formation n'est pas requise pour passer Linux+.

Source partenaire France à titre indicatif :

- https://www.globalknowledge.com/fr-fr/formation/comptia/systemes_d%E2%80%99exploitation/g016

---

# Canonical Academy — Ubuntu

Canonical Academy a lancé son programme de certification Ubuntu.

Le guide officiel confirme :

- achats via Academy shop ;
- examens general release planifiables jusqu'à un an après achat ;
- preview/beta/promo parfois limités à 30 jours.

Source :

- https://canonical.com/academy/exam-guide

Le track System Administrator est basé sur plusieurs examens Ubuntu.

### Statut prix

`CHECKOUT-REQUIRED` — le prix public n'est pas encore suffisamment stable/exposé pour être figé dans ce fichier.

---

# Comparatif Linux

```text
SUSE SLES Admin             149 $
LPI one pro exam            176 €
SUSE HA Engineer            195 $
LPIC-1                      352 €
CompTIA Linux+              ~349 € partner indication
LFCS                        445 $
Red Hat exam                500 $
```

Mais la difficulté et la preuve ne sont pas identiques :

- LPI/SUSE : QCM/exam knowledge ;
- CompTIA : mix knowledge / performance-based items ;
- LFCS/Red Hat : fortement pratique / performance-based.

---

# Priorité selon objectif

## Vendor-neutral Linux

1. **LFCS — 445 $** si preuve pratique prioritaire ;
2. **LPIC-1 — 352 €** si profondeur vendor-neutral ;
3. **LPIC-2 / LPIC-3** pour spécialisation avancée.

## Enterprise SUSE

1. **SLES 16 Admin — 149 $** ;
2. **HA Engineer — 195 $** ;
3. Multi-Linux Manager / SAP / Edge selon environnement.

---

# À poursuivre

- Canonical Academy exact pricing Ubuntu 26.04 ;
- CompTIA France official checkout price ;
- Oracle Linux certification ;
- AlmaLinux / Rocky Linux credentials ;
- FreeBSD Foundation certifications éventuelles ;
- Linux security vendor-neutral ;
- systemd / SELinux specific credentials ;
- SUSE Observability / Multi-Linux Manager advanced ;
- SLES 16 Engineer tracks ;
- IBM AIX already covered separately.
