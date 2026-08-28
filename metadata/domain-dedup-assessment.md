# Domain dedup assessment — 2026-08-28

> Analyse des domaines hors cœur Entrepreneur après mise en place de la propriété canonique du parcours Entrepreneur / Group Management.

## 1. Résumé

Deux audits complémentaires sont désormais disponibles :

- `catalog-overlap-analysis.md` — lignes de tableaux ;
- `catalog-bullet-overlap-analysis.md` — credentials listés en bullets.

Snapshot :

```text
97 catalogues avec lignes de tableaux credential-like
1 397 lignes analysées
82 noms normalisés présents dans au moins 2 fichiers
13 paires specialist↔specialist avec chevauchement exact
357 bullets de credentials nommés analysés
0 doublon exact specialist↔specialist dans les bullets
```

Les agrégateurs transverses sont volontairement exclus du classement de nettoyage :

```text
free-it.md
free-non-it.md
paid-under-500.md
paid-over-500.md
tools-platforms-under-500.md
business-finance-under-500.md
```

Les fichiers `entrepreneur*` sont également exclus du ranking car ils disposent déjà d'une ownership map dédiée.

### Conclusion globale

Le dépôt n'est **pas massivement dupliqué**.

Le problème est concentré dans quelques domaines créés par couches successives :

```text
observability / Elastic
IBM enterprise / mainframe / messaging
private cloud / HPE / Nutanix / VMware
cloud-native / observability
NVIDIA AI infrastructure / network
cyber practical vs premium
HR / compensation / transformation
AI governance / privacy
insurance / actuarial
```

---

# 2. P0 — Observability / Elastic

## Fichiers concernés

- `data-database-platforms-under-500.md`
- `observability-sre-devops-under-500.md`
- `observability-vendor-certifications-2026.md`
- `observability-vendor-low-cost-2026.md`
- `tools-platforms-under-500.md` — agrégateur seulement

## Doublons confirmés

```text
Elastic Certified Analyst
Elastic SIEM Analyst
Elastic Engineer / Observability Engineer
```

Ils sont détaillés à la fois dans `data-database-platforms-under-500.md` et `observability-sre-devops-under-500.md`.

### Recommandation

Faire de la branche **Observability** le propriétaire canonique des certifications Elastic professionnelles.

Option la plus propre :

```text
observability-vendor-certifications-2026.md
    = lifecycle / prix / validité / statut vendor canonique

observability-sre-devops-under-500.md
    = shortlist par métier / routeur

observability-vendor-low-cost-2026.md
    = opportunités gratuites / low-cost ; route vers la fiche vendor

data-database-platforms-under-500.md
    = route vers Elastic pour Search / data ; pas de TCO recopié
```

**Priorité : TRÈS HAUTE.** C'est le chevauchement métier le plus net du scan.

---

# 3. P0 — IBM enterprise / mainframe / messaging

## Doublons confirmés

Entre :

- `ibm-enterprise-security-ai-under-500.md`
- `mainframe-enterprise-software.md`

on retrouve :

```text
IBM z/OS v3.x Administrator Professional
IBM Db2 13 for z/OS DBA Professional
IBM MQ 9.4 Administrator Professional
```

`enterprise-messaging-streaming-2026.md` référence aussi MQ mais utilise déjà une logique de routage plutôt que de recopier toute la fiche technique.

### Ownership proposée

```text
z/OS
Db2 for z/OS
    → mainframe-enterprise-software.md

IBM MQ
    → enterprise-messaging-streaming-2026.md

QRadar / Guardium / watsonx / IBM security & AI
    → ibm-enterprise-security-ai-under-500.md
```

Le catalogue IBM général doit devenir un **vendor overview / router** lorsqu'un credential dispose déjà d'un domaine canonique plus précis.

**Priorité : TRÈS HAUTE.**

---

# 4. P0 — Private cloud / HPE / Nutanix / VMware

## Fichiers concernés

- `hpe-certification-pricing-ai-private-cloud-2026.md`
- `hpe-morpheus-private-cloud-2026.md`
- `virtualization-private-cloud-under-500.md`
- `tools-platforms-under-500.md` — agrégateur

## Doublons confirmés

```text
Nutanix NCP-MCI
Nutanix NCM-MCI
VMware VCP-VCF Architect
```

Ils sont recopiés dans la table de comparaison HPE/Morpheus et dans le catalogue virtualization.

### Ownership proposée

```text
HPE exam pricing + HPE AI/private cloud credentials
    → hpe-certification-pricing-ai-private-cloud-2026.md

Morpheus-specific credentials
    → hpe-morpheus-private-cloud-2026.md

VMware / Nutanix / OpenStack / CloudStack / etc.
    → virtualization-private-cloud-under-500.md
```

La comparaison Morpheus peut conserver :

```text
nom
positionnement
lien canonique
```

mais pas recopier le TCO détaillé des concurrents.

**Priorité : TRÈS HAUTE.**

---

# 5. P0 — Cloud-native vs Observability

Deux credentials CNCF sont détaillés dans :

- `cloud-native-platform-engineering-under-500.md`
- `observability-sre-devops-under-500.md`

```text
Prometheus Certified Associate — PCA
OpenTelemetry Certified Associate — OTCA
```

### Ownership proposée

Ces credentials valident principalement des technologies d'observabilité :

```text
PCA / OTCA
    → observability-sre-devops-under-500.md
```

`cloud-native-platform-engineering-under-500.md` conserve une référence et explique leur place dans le profil platform engineer.

**Priorité : HAUTE.**

---

# 6. P0 — NVIDIA AI infrastructure vs networking

Le catalogue :

- `ai-infrastructure-gpu-hpc-2026.md`

et :

- `network-datacenter-advanced-under-500.md`

reprennent les parcours NVIDIA NCA/NCP AI Infrastructure / Networking / Rack / Operations.

### Ownership proposée

```text
NVIDIA AI infrastructure credential family
    → ai-infrastructure-gpu-hpc-2026.md
```

Le catalogue networking garde uniquement les credentials NVIDIA réellement pertinents pour son parcours, sous forme de routeur.

**Priorité : HAUTE.**

---

# 7. P0 — Cybersécurité practical / premium

Doublons exacts entre :

- `practical-cyber-under-500.md`
- `cyber-premium-over-500.md`

```text
CREST Practitioner : CPSA / CPTIA / CPIA
CREST Registered : CRT / CRTIA / CRIA
```

Le split tarifaire donne déjà la bonne règle d'ownership :

```text
Practitioner ~275 £
    → practical-cyber-under-500.md

Registered ~600 £ et niveaux supérieurs
    → cyber-premium-over-500.md
```

Chaque fichier peut montrer le ladder complet, mais les détails/prix du niveau non propriétaire doivent être remplacés par un cross-link.

**Priorité : HAUTE.**

---

# 8. P1 — HR / compensation / transformation

Doublons exacts :

```text
GPHR
HRCI SPHR / SPHRi / GPHR
```

entre :

- `compensation-total-rewards.md`
- `management-transformation-over-500.md`

Le repo possède également `hr-people-hrtech.md`, plus naturel comme racine HR générale.

### Ownership proposée

```text
HRCI généraliste : SPHR / SPHRi / GPHR / PHRi / etc.
    → hr-people-hrtech.md

WorldatWork / compensation / total rewards
    → compensation-total-rewards.md

transformation / change / leadership
    → management-transformation-over-500.md
```

`management-transformation-over-500.md` et `compensation-total-rewards.md` doivent ensuite router vers le owner HR au lieu de recopier application fee + exam fee.

**Priorité : HAUTE.**

---

# 9. P1 — AI governance / privacy

Doublon confirmé :

```text
IAPP AIGP
```

entre :

- `ai-governance-risk-safety.md`
- `privacy-dpo-france.md`

### Ownership proposée

```text
AIGP
    → ai-governance-risk-safety.md

CIPP/E, DPO France, privacy opérationnelle
    → privacy-dpo-france.md
```

La fiche privacy peut évidemment recommander AIGP comme complément, mais sans recopier son TCO/maintenance.

**Priorité : MOYENNE / HAUTE.**

---

# 10. P1 — Insurance / actuarial

Doublon exact :

```text
LOMA FLMI — non-member pricing
```

entre :

- `actuarial-accounting-insurance.md`
- `insurance-risk-designations.md`

### Ownership proposée

```text
SOA / IFoA / actuarial
    → actuarial-accounting-insurance.md

LOMA / CPCU / ARM / CII / insurance designations
    → insurance-risk-designations.md
```

Donc FLMI doit être canonique dans `insurance-risk-designations.md`.

**Priorité : MOYENNE.**

---

# 11. P1 — Observability vendor files

`observability-vendor-certifications-2026.md` et `observability-vendor-low-cost-2026.md` se chevauchent sur Sumo Logic et peuvent diverger avec le temps.

### Recommandation

Ne pas maintenir deux bases de prix vendor complètes.

```text
observability-vendor-certifications-2026.md
    → source canonique vendor/status/prix

observability-vendor-low-cost-2026.md
    → shortlist opportunités 0–500, sans recopier la fiche complète
```

Ou fusionner les deux si la shortlist devient trop courte pour justifier un fichier.

**Priorité : MOYENNE.**

---

# 12. P2 — Arista

Chevauchement entre :

- `arista-academy-certification-2026.md`
- `network-datacenter-advanced-under-500.md`

sur les practical exams Associate/Specialist/Professional/Expert.

### Ownership proposée

```text
Arista Academy full lifecycle / exam pricing
    → arista-academy-certification-2026.md

network-datacenter-advanced-under-500.md
    → shortlist / comparaison et liens
```

Le fichier réseau ne doit pas devenir une deuxième copie de la grille Arista.

**Priorité : MOYENNE.**

---

# 13. Chevauchements acceptables / intentionnels

## Construction / BTP

`construction-btp-global-2026.md` cite **PMI-CP** et indique déjà explicitement :

```text
Déjà détaillé : construction-cost-engineering.md
```

C'est exactement le modèle souhaité.

Le scan strict de **357 credentials en bullets** ne trouve **aucun doublon exact specialist↔specialist**.

Conclusion : **ne pas lancer une grosse dédup BTP**. Le routage existant fonctionne.

## Red Hat exam standard

La ligne `Red Hat exam standard` apparaît dans IAM et virtualization. Il s'agit d'une référence tarifaire générique, pas de deux fiches d'un même credential.

Peut être centralisée ultérieurement dans la fiche Red Hat TCO, mais faible priorité.

## Aggregators

Les répétitions dans :

```text
free-it
free-non-it
paid-under-500
paid-over-500
tools-platforms-under-500
business-finance-under-500
```

sont intentionnelles.

La règle à leur appliquer est toutefois :

```text
shortlist / prix résumé / lien
≠ copie complète de la fiche spécialiste
```

---

# 14. Domaines actuellement peu problématiques

Le scan exact ne fait pas ressortir de duplication structurelle importante pour :

```text
supply chain / procurement
pharma / clinical / regulatory
food safety / logistics
real estate
accessibility
coaching / learning
language — hors présence volontaire dans l'agrégateur business
construction specialties / site schemes
automotive / rail quality
```

Cela ne signifie pas qu'il n'existe aucun chevauchement conceptuel, mais aucune duplication exacte suffisamment forte ne justifie une passe prioritaire.

---

# 15. Problème architectural restant : les domaines sans MOC

Le cœur IT possède `IT-INDEX.md`, le BTP possède `CONSTRUCTION-BTP-INDEX.md`, et Entrepreneur possède désormais deux routeurs.

Plusieurs ensembles hors IT restent plats et sont donc plus susceptibles de recréer des doublons :

## Finance / risk / audit / insurance

Fichiers concernés notamment :

```text
finance-risk-fraud-over-500
compliance-aml-fpa-over-500
actuarial-accounting-insurance
insurance-risk-designations
business-valuation
audit-finance-project-over-500
france-amf-regulatory
```

Recommandation : créer à terme `FINANCE-RISK-INDEX.md` avec ownership explicite.

## People / HR / management

```text
hr-people-hrtech
compensation-total-rewards
coaching-learning-development
management-transformation-over-500
customer-experience
```

Recommandation : `PEOPLE-MANAGEMENT-INDEX.md` ou ownership registry équivalente.

## Governance / compliance / privacy

```text
privacy-dpo-france
ai-governance-risk-safety
iso-grc-europe-over-500
legal-contract-management
compliance-aml-fpa-over-500
governance-board-over-500
```

Recommandation : ne créer un MOC que si l'ownership map seule devient insuffisante ; éviter de multiplier les index inutiles.

---

# 16. Ordre de nettoyage recommandé

```text
1. Observability / Elastic
2. IBM mainframe / messaging / vendor overview
3. HPE / Morpheus / virtualization
4. Cloud-native PCA / OTCA
5. NVIDIA AI infrastructure
6. Cyber practical vs premium
7. HR / HRCI ownership
8. AIGP privacy / AI governance
9. Insurance / FLMI
10. Observability vendor low-cost/status consolidation
11. Arista network routing
12. Finance/Risk MOC + ownership map
```

Après ces passes, relancer :

```bash
python tools/audit-catalog-overlaps.py
python tools/audit-catalog-bullet-overlaps.py
python tools/audit-entry-geography.py
```

Objectif : ne pas viser artificiellement `0 overlap` dans tout le dépôt. Un agrégateur et un catalogue spécialiste **doivent** parfois citer la même certification. L'objectif est plutôt :

```text
1 source de vérité pour les détails
+
plusieurs routeurs possibles
```
