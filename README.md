# human-skills

Catalogue vivant de **certifications, examens, credentials et attestations professionnelles**, classés par coût, domaine et valeur potentielle sur un CV.

> **Dernière revue globale : 28 août 2026**

## Objectif

Construire une base exploitable pour répondre à trois questions :

1. **Qu'est-ce que je peux passer gratuitement ?**
2. **Quelles certifications valent le coût à différents niveaux de budget ?**
3. **Dans quel ordre les passer pour construire un profil cohérent ?**

Le dépôt ne se limite pas à l'IT : cloud, infrastructure, cybersécurité, data, architecture, projet, leadership, business, langues, risque, RGPD, Lean/Six Sigma, marketing et autres domaines sont inclus.

---

## Catalogue

### Gratuit

- [`certifications/free-it.md`](certifications/free-it.md) — certifications et credentials IT gratuits, vérifiés 2026.
- [`certifications/free-non-it.md`](certifications/free-non-it.md) — management, projet, business, langues, RGPD, Lean/Six Sigma, marketing, etc.

### Moins de 500 €

- [`certifications/paid-under-500.md`](certifications/paid-under-500.md) — catalogue payant jusqu'à environ 500 € de coût d'accès au credential.

### Roadmap

- [`roadmap.md`](roadmap.md) — ordre de passage recommandé et logique de construction du profil.

### Sources communautaires

- [`sources/community-repositories.md`](sources/community-repositories.md) — dépôts GitHub et listes externes utilisés comme radar de découverte.

---

## Tranches de prix

Le catalogue est progressivement structuré selon les tranches suivantes :

```text
FREE
FREE-CONDITIONAL
< 100 €
100–250 €
250–500 €
500–1 000 €       ← prochaine étape
1 000–2 500 €
> 2 500 €
```

Le classement porte autant que possible sur le **coût total nécessaire pour obtenir le credential** et non uniquement sur le prix affiché d'un examen.

Exemple : un examen à 200 € avec une formation obligatoire à 2 000 € ne sera pas classé dans la tranche « <500 € ».

---

## Niveaux de preuve

Toutes les lignes ne se valent pas. Le dépôt distingue :

### Certification professionnelle

Examen formel, généralement surveillé ou contrôlé, délivré par un éditeur ou un organisme de certification.

Exemples :

- AWS ;
- Cisco ;
- Linux Foundation / CNCF ;
- VMware / Broadcom ;
- Palo Alto ;
- HashiCorp ;
- Scrum.org ;
- ISACA ;
- The Open Group.

### Credential appliqué

Évaluation pratique ou credential éditeur sans nécessairement suivre le modèle d'un examen proctoré classique.

Exemple : Microsoft Applied Skills.

### Digital credential / badge

Évaluation ou parcours vérifiable, utile en complément mais généralement moins fort qu'une certification professionnelle.

### Attestation / certificat de formation

Prouve qu'un parcours a été suivi et éventuellement évalué, sans être assimilé à une certification professionnelle.

Exemple : CNIL Atelier RGPD.

---

## Principe de vérification

Les anciennes listes Internet vieillissent extrêmement vite.

Chaque entrée doit donc idéalement être contrôlée ainsi :

```text
Découverte
   ↓
Source officielle actuelle
   ↓
Prix de l'examen
   ↓
Prérequis
   ↓
Formation obligatoire ?
   ↓
Frais de certification / maintenance ?
   ↓
Coût total du credential
   ↓
Date de vérification
```

Les promotions temporaires sont distinguées du tarif normal.

---

## Exemples d'anciennes informations devenues fausses

- ISC2 CC n'est plus automatiquement gratuite pour les nouveaux candidats ;
- GitLab propose désormais ses examens de certification à l'achat ;
- Sumo Logic est passé à des examens proctorés payants ;
- Redis Certified Developer a été retirée ;
- Zerto University a été décommissionnée et la formation a migré vers HPE ;
- les anciens vouchers Microsoft Ignite ne doivent pas être considérés comme permanents.

C'est pour cette raison que les dépôts communautaires sont traités comme **sources de découverte**, et non comme références de prix.

---

## Quelques rapports valeur / prix remarquables identifiés en 2026

| Credential | Coût indicatif |
|---|---:|
| Neo4j Certified Professional | **0 €** |
| KNIME L1 | **0 €** |
| CNIL Atelier RGPD | **0 €** |
| Six Sigma White Belt CSSC | **0 $** |
| HashiCorp Terraform Associate | **70,50 $** |
| GitHub Certifications | **99 $ global / tarif régional** |
| SUSE AI Deployment Specialist | **99 $** |
| AWS Solutions Architect Associate | **128 €** |
| SUSE Administrator exams | **149 $** |
| ISACA COBIT Foundation | **175 $** |
| Scrum.org PSM I | **200 $** |
| F5 Certified Administrator BIG-IP | **250 $ total online** |
| VMware/Broadcom VCP | **250 $** |
| Linux Foundation Associate family | **250 $** |
| FinOps Certified Practitioner | **~300 $** |
| Cisco CCNA | **300 $** |
| TOGAF EA Foundation | **395 $** |
| LFCS / CKA / CKAD / CKS | **445 $** |
| CSA CCSK | **445 $** |

---

## Contribution / maintenance

Pour chaque nouvelle entrée, conserver si possible :

- nom exact ;
- organisme ;
- domaine ;
- prix officiel ;
- monnaie ;
- éventuelle TVA ;
- prérequis ;
- formation obligatoire ou facultative ;
- nombre de tentatives ;
- durée / expiration ;
- URL officielle ;
- date de vérification ;
- statut : actif / conditionnel / promotion / deprecated.

L'objectif à terme est d'obtenir une **cartographie internationale des certifications professionnelles par coût et par valeur**, plutôt qu'une simple collection de liens.
