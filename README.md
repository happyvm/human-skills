# human-skills

Catalogue vivant de **certifications, examens, credentials et attestations professionnelles**, classés par coût, domaine et valeur potentielle sur un CV.

> **Dernière revue globale : 28 août 2026**

## Objectif

Répondre à quatre questions :

1. **Qu'est-ce que je peux passer gratuitement ?**
2. **Quelles certifications valent leur coût selon mon budget ?**
3. **Quel est le vrai TCO du credential, pas seulement le prix du voucher ?**
4. **Dans quel ordre les passer pour construire un profil cohérent ?**

Le dépôt couvre IT et hors IT : cloud, infrastructure, cyber, data, architecture, observabilité, automatisation, projet, leadership, finance, business, langues, risque, RGPD, Lean/Six Sigma, marketing, supply chain, change management, audit, ressources humaines, AML/compliance et autres domaines.

---

# Catalogue

## Gratuit

- [`certifications/free-it.md`](certifications/free-it.md) — certifications et credentials IT gratuits vérifiés en 2026.
- [`certifications/free-non-it.md`](certifications/free-non-it.md) — anglais, management, projet, RGPD, Lean/Six Sigma, business, marketing, etc.

## Jusqu'à environ 500 €

- [`certifications/paid-under-500.md`](certifications/paid-under-500.md) — catalogue général.
- [`certifications/practical-cyber-under-500.md`](certifications/practical-cyber-under-500.md) — HTB, TCM, TryHackMe, BTL1, INE, BSCP et certifications hands-on.
- [`certifications/tools-platforms-under-500.md`](certifications/tools-platforms-under-500.md) — Datadog, Confluent, dbt, UiPath, HPE, IBM, ServiceNow, Elastic, MOS, Adobe, Autodesk, etc.
- [`certifications/business-finance-under-500.md`](certifications/business-finance-under-500.md) — PMI, Scrum.org, ISACA, TOGAF, Lean Six Sigma, CFA Investment Foundations, langues, business.

## Au-delà de 500 € — analyse par TCO

- [`certifications/paid-over-500.md`](certifications/paid-over-500.md) — catalogue général : ISC2, ISACA, IAPP, GIAC/SANS, OffSec, Cisco Pro/Expert, Red Hat, PECB/ISO, PeopleCert, PMI, GARP, CFA, ASQ, ASCM, TOGAF, etc.
- [`certifications/management-transformation-over-500.md`](certifications/management-transformation-over-500.md) — Prosci, SABSA, IIBA CBAP, DAMA CDMP avancé, HRCI, SAFe, FinOps, procurement / CPSM.
- [`certifications/audit-finance-project-over-500.md`](certifications/audit-finance-project-over-500.md) — IIA CIA/CRMA, IMA CMA, ACCA, IPMA France, SMaP Change, ACMP CCMP, APMG Change Management.
- [`certifications/finance-risk-fraud-over-500.md`](certifications/finance-risk-fraud-over-500.md) — CAIA, PRMIA PRM/ERM, CFE, CTP, credit/counterparty risk.
- [`certifications/compliance-aml-fpa-over-500.md`](certifications/compliance-aml-fpa-over-500.md) — CAMS, CAFS, CGSS, Advanced CAMS, ICA AML/GRC/Financial Crime et AFP FPAC.

## Roadmap

- [`roadmap.md`](roadmap.md) — logique de construction du profil et ordre de passage recommandé.

## Recherche et sources

- [`sources/community-repositories.md`](sources/community-repositories.md) — anciens et nouveaux dépôts GitHub utilisés comme **radars**, avec leur fiabilité 2026.
- [`research/over-500-watchlist.md`](research/over-500-watchlist.md) — reste à chiffrer / tarifs partenaires / programmes non encore consolidés.

---

# Tranches de prix

```text
FREE
FREE-CONDITIONAL
< 100 €
100–250 €
250–500 €
500–1 000 €
1 000–2 500 €
2 500–5 000 €
> 5 000 €
```

À partir de 500 €, le dépôt conserve autant que possible **trois montants différents** :

```text
EXAM PRICE
    Prix du voucher / examen.

FIRST-CYCLE TCO
    Ce qu'il faut réellement payer pour obtenir et activer le credential.

LONG-TERM TCO
    Maintenance, renouvellement, membership et obligations sur plusieurs années.
```

Le classement utilise donc le **coût total permettant réellement d'obtenir le credential**, pas seulement le prix marketing d'un examen.

Exemples :

```text
IAPP CIPP/E
Exam ≈ 472 € au change actuel
+ Certification Maintenance Fee obligatoire pour un non-membre
= credential actif > 500 €
```

```text
Red Hat
Exam ≈ 429 € au prix catalogue USD
× plusieurs examens obligatoires
= certains parcours > 500 €
```

```text
ACFE CFE
Exam application = 480 $
+ membership ACFE obligatoire
= TCO réel > prix du voucher
```

---

# Niveaux de preuve

## Certification professionnelle

Examen formel, généralement surveillé, pratique ou contrôlé.

Exemples : AWS, Cisco, CNCF, Red Hat, HashiCorp, Scrum.org, ISACA, HTB, TCM, TOGAF, CIA, CAMS.

## Credential appliqué

Évaluation pratique éditeur ne suivant pas nécessairement le modèle d'un examen proctoré classique.

Exemple : Microsoft Applied Skills.

## Digital credential / badge

Évaluation ou parcours vérifiable utile en complément.

## Attestation / certificat de formation

Prouve qu'un parcours a été suivi, mais n'est pas assimilé à une certification professionnelle.

Exemple : CNIL Atelier RGPD.

---

# Méthode de vérification

```text
Découverte
   ↓
Source officielle actuelle
   ↓
Prix examen
   ↓
Prix régional / TVA / devise
   ↓
Prérequis
   ↓
Formation obligatoire ?
   ↓
Licence / abonnement obligatoire ?
   ↓
Frais d'application / membership ?
   ↓
Maintenance / CPE / PDU / CPD ?
   ↓
Retakes / déplacements ?
   ↓
First-cycle TCO
   ↓
Long-term TCO
   ↓
Date de vérification
```

Les promotions temporaires sont séparées du tarif normal.

Pour convertir les prix USD en euros lors de la revue du 28 août 2026, le dépôt utilise à titre indicatif le dernier taux de référence BCE disponible au moment de la recherche :

```text
27 août 2026
1 EUR = 1,1645 USD
```

Les conversions ne remplacent jamais le prix final du checkout.

---

# Dépôts communautaires retrouvés

Plusieurs listes historiques ont servi de point de départ :

- `munchy-bytes/FreeDevCertifications` ;
- `ArslanYM/Free-Certifications` ;
- `PanXProject/awesome-certificates` ;
- `Troy-LL/The-Free-Credential-Index` ;
- `orgito1015/free-cybersecurity-certifications` ;
- `surajbhan-3/Free-IT-Certification-and-badges_list`.

Ils sont très utiles comme **sources de découverte**, mais pas comme références tarifaires : beaucoup de gratuités 2020–2022 sont aujourd'hui payantes ou retirées.

Exemples :

- GitLab : anciennes listes gratuites, examens actuels payants ;
- Sumo Logic : formation gratuite mais certification désormais 100–150 $ ;
- Redis Certified Developer : retirée ;
- Zerto University : décommissionnée et migrée vers HPE ;
- ISC2 CC : ancienne campagne gratuite terminée pour les nouveaux candidats.

---

# Quelques rapports valeur / prix remarquables en 2026

| Credential | Prix indicatif |
|---|---:|
| Neo4j Certified Professional | **0 €** |
| KNIME L1 | **0 €** |
| CNIL Atelier RGPD | **0 €** |
| CSSC Six Sigma White Belt | **0 $** |
| HashiCorp Terraform Associate | **70,50 $** |
| GitHub Certifications | **99 $ global / tarif régional** |
| Datadog | **100 $** |
| SUSE AI Deployment Specialist | **99 $** |
| AWS Solutions Architect Associate | **128 €** |
| Confluent Kafka | **150 $** |
| ISACA COBIT Foundation | **175 $** |
| Scrum.org PSM I | **200 $** |
| dbt Analytics Engineering | **200 $** |
| HTB CPTS / CDSA / COAE | **~250 $ TTC indicatif** |
| F5 Certified Administrator BIG-IP | **250 $ total online** |
| VMware/Broadcom VCP | **250 $** |
| TCM PJPT / PSAA / PAPA | **249 $** |
| Linux Foundation Associate family | **250 $** |
| Cisco CCNA | **300 $** |
| TryHackMe PT1 / SAL1 | **301 €** |
| CFA Investment Foundations | **350 $** |
| TOGAF EA Foundation | **395 $** |
| LFCS / CKA / CKS | **445 $** |
| CSA CCSK | **445 $** |
| PMI-ACP | **495 $ non-membre** |
| TCM PNPT / PSAP | **499 $** |
| IPMA Level D France | **440 € HT / ~528 € TTC** |
| CISSP | **719,04 € + maintenance** |
| CCSP | **575,04 € + maintenance** |
| Cisco CCNP | **700 $ core + concentration** |
| CIA | **990 $ membre / 1 515 $ non-membre** avant éventuel membership |
| ACMP CCMP | **595/795 $ + 21 h de formation admissible** |
| IMA CMA | **~1 715 $ première année professionnel** |
| CAMS | **2 095 $ privé + membership** |
| CAIA Charter | **2 390 $ d'examens early + membership** |
| ICA Advanced AML | **2 540 € + 220 € membership + taxes** |
| SABSA Foundation | **~3 200 € HT via AEP Europe observé** |
| Prosci Change Management | **3 386 € online / 3 810 € présentiel hors taxes** |
| ICA Diploma AML | **5 085 € + membership + taxes** |
| SANS + GIAC | **~9 k€ pour un cours + cert dans certains événements Europe** |

---

# Frontières et pièges de classement

Un montant en dollars supérieur à 500 n'implique pas automatiquement un coût supérieur à 500 €.

Exemples au change de la revue :

- 550 $ ≈ 472 € ;
- 575 $ ≈ 494 € ;
- 595 $ ≈ 511 €.

À l'inverse, une certification affichée sous 500 € HT peut dépasser le seuil pour un particulier en TTC : **IPMA Level D France = 440 € HT, soit environ 528 € TTC à 20 % de TVA**.

De même, un examen `<500 €` peut appartenir au catalogue `>500 €` si son **TCO obligatoire** dépasse le seuil à cause d'une adhésion, de plusieurs examens, d'une formation ou d'une maintenance obligatoire.

---

# Maintenance

Pour chaque nouvelle entrée, conserver si possible :

- nom exact ;
- organisme ;
- domaine ;
- prix officiel ;
- monnaie ;
- conversion EUR indicative ;
- TVA / taxes ;
- prérequis ;
- formation obligatoire ou facultative ;
- licence / abonnement requis ;
- nombre de tentatives ;
- expiration / renouvellement ;
- frais d'application ;
- membership ;
- frais de maintenance ;
- CPE / PDU / CPD ;
- coût retake ;
- déplacement éventuel ;
- first-cycle TCO ;
- three-year / long-term TCO ;
- URL officielle ;
- date de vérification ;
- statut : actif / conditionnel / promotion / deprecated / research.

À terme, le but est d'obtenir une **cartographie internationale du TCO des certifications professionnelles**, plutôt qu'une simple collection de liens.
