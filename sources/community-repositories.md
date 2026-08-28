---
title: "Dépôts communautaires à surveiller"
type: source-tracker
tags:
  - source-tracker
status: active
verified: 2026-08-28
---

# Dépôts communautaires à surveiller

> Sources utilisées comme **radar**, jamais comme vérité. Chaque entrée trouvée dans ces dépôts doit être revérifiée sur le site officiel du fournisseur avant d'être ajoutée aux catalogues `human-skills`.
>
> **Revue initiale : 28 août 2026**

## Pourquoi ce fichier existe

Les listes communautaires de certifications vieillissent très vite :

- une promotion gratuite devient payante ;
- un examen est retiré ;
- un fournisseur change de programme ;
- un badge de cours est présenté comme une certification ;
- une gratuité réservée aux étudiants est présentée comme générale.

Le dépôt `human-skills` conserve donc la liste des **sources à fouiller** séparément de la liste des credentials effectivement validés.

---

## 1. munchy-bytes/FreeDevCertifications

https://github.com/munchy-bytes/FreeDevCertifications

### Intérêt

Probablement le dépôt le plus proche de l'idée recherchée : il vise explicitement les **professional certification exams fournis gratuitement**.

Il a notamment recensé :

- ArangoDB Certified Professional ;
- DataStax Cassandra Developer / Administrator ;
- MongoDB Associate pour étudiants ;
- Neo4j Certified Professional ;
- Neo4j Graph Data Science ;
- KNIME L1 Basic Proficiency ;
- HackerRank Skills Verification ;
- anciennes offres Microsoft / Oracle ;
- promotions ponctuelles.

### Fiabilité 2026

**⭐⭐⭐⭐ comme source d'idées / ⭐⭐ comme source de prix actuels.**

Le dépôt a le mérite de posséder une section `Deprecated free certifications`, mais certaines entrées principales sont devenues conditionnelles ou ont changé.

Exemples de revérification :

- Neo4j : **toujours réellement gratuit en 2026** ;
- MongoDB : toujours gratuit pour certains étudiants via GitHub Student Developer Pack après parcours, mais ce n'est pas une gratuité générale ;
- KNIME L1 : toujours gratuit ;
- anciennes promotions Oracle / Microsoft : ne doivent pas être recopiées sans contrôle.

---

## 2. ArslanYM/Free-Certifications

https://github.com/ArslanYM/Free-Certifications

### Intérêt

Très grosse liste historique de cours, badges et certifications gratuits.

On y trouve ou y a trouvé :

- Nutanix ;
- GitLab ;
- Oracle ;
- Microsoft ;
- Juniper ;
- Huawei ;
- Sumo Logic ;
- freeCodeCamp ;
- cPanel / Plesk ;
- Zerto ;
- Calico ;
- New Relic ;
- Codefresh GitOps ;
- Neo4j ;
- API Academy ;
- Chef ;
- Kasten ;
- etc.

### Fiabilité 2026

**⭐⭐⭐⭐⭐ comme radar / ⭐ comme catalogue prêt à l'emploi.**

Beaucoup d'offres du haut de la liste sont explicitement datées de 2020–2022 ou reposent sur des programmes qui ont changé.

Exemples déjà contrôlés :

- **GitLab** : les nouveaux examens sont payants aujourd'hui ;
- **Sumo Logic** : formation toujours gratuite mais nouveaux examens à 100–150 $ ;
- **Zerto** : Zerto University a été décommissionnée le 4 août 2025 et la formation a migré vers HPE ;
- **Calico / Tigera** : plusieurs cours Certified Calico Operator sont toujours affichés gratuits ;
- **Neo4j** : toujours gratuit.

Conclusion : excellent dépôt pour générer une file de vérification, mauvais dépôt à copier tel quel.

---

## 3. PanXProject/awesome-certificates

https://github.com/PanXProject/awesome-certificates

### Intérêt

Liste très large de certificats gratuits couvrant :

- développement ;
- IT ;
- data ;
- design ;
- business ;
- autres domaines.

### Fiabilité

**⭐⭐⭐⭐ comme source de découverte.**

La liste mélange :

- certifications professionnelles ;
- badges ;
- certificats de fin de cours ;
- MOOCs.

Il faut donc appliquer le filtre `human-skills` avant import.

---

## 4. Troy-LL/The-Free-Credential-Index

https://github.com/Troy-LL/The-Free-Credential-Index

### Intérêt

Index récent orienté credentials technologiques gratuits et vérifiables.

### Fiabilité

**⭐⭐⭐⭐ comme radar récent.**

Comme pour toute liste communautaire, les méthodes de voucher, challenges et promotions doivent être contrôlées au moment où l'utilisateur veut s'inscrire.

---

## 5. orgito1015/free-cybersecurity-certifications

https://github.com/orgito1015/free-cybersecurity-certifications

### Intérêt

Liste spécialisée cybersécurité :

- certifications ;
- cours ;
- labs ;
- plateformes d'apprentissage.

### Usage

Source intéressante pour étendre les catégories :

- SOC ;
- blue team ;
- pentest ;
- cloud security ;
- DFIR ;
- threat intelligence.

---

## 6. surajbhan-3/Free-IT-Certification-and-badges_list

https://github.com/surajbhan-3/Free-IT-Certification-and-badges_list

Liste généraliste de certifications et badges IT gratuits.

À traiter comme source secondaire de découverte.

---

# Entrées issues de ces dépôts déjà revérifiées en 2026

| Ancienne entrée communautaire | Statut au 28/08/2026 | Classement human-skills |
|---|---|---|
| Neo4j Certified Professional | ✅ gratuit | Free IT |
| Neo4j Graph Data Science Certification | ✅ gratuit | Free IT |
| KNIME L1 Basic Proficiency | ✅ gratuit | Free IT |
| MongoDB certification étudiant | ✅ gratuit sous conditions GitHub Student Pack | Free conditionnel |
| Tigera Certified Calico Operator L1 | ✅ page actuelle : Free | Free IT |
| Tigera Calico AWS Expert | ✅ page actuelle : Free | Free IT |
| Tigera Calico Azure Expert | ✅ page actuelle : Free | Free IT |
| Tigera Calico eBPF | ✅ page actuelle : Free | Free IT |
| Codefresh GitOps | 🟡 programme toujours visible ; vérifier conditions d'inscription au moment du passage | Watchlist |
| Sumo Logic Certification | ❌ plus gratuite | 100–150 $ |
| GitLab Certification | ❌ plus gratuite | Payant / prix à vérifier |
| Zerto University | ❌ ancien programme décommissionné | HPE / à réévaluer |
| Redis Certified Developer | ❌ retirée | Deprecated |
| Microsoft Ignite free exam vouchers historiques | ❌ offres historiques | Promotions uniquement |
| Nutanix gratuit 2021/2022 | ❌ offre historique | Promotions uniquement |

---

# Méthode de traitement d'une nouvelle découverte

```text
Dépôt communautaire
       ↓
Identifier le fournisseur et le credential exact
       ↓
Page officielle actuelle
       ↓
Vérifier prix + prérequis + formation obligatoire + expiration
       ↓
Classer :
  FREE
  FREE-CONDITIONAL
  <100
  100-250
  250-500
  >500
  DEPRECATED
       ↓
Ajouter date de vérification
```

Cette méthode permet d'utiliser les anciennes listes comme une **base de renseignements** sans importer leurs erreurs historiques.
