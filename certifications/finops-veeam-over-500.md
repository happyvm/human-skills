# FinOps & Veeam — certifications dont le TCO dépasse souvent 500 €

> Vérifié fin août 2026. Ces deux écosystèmes illustrent bien pourquoi le **prix de l'examen seul** est insuffisant : prérequis et formation peuvent dominer le coût total.

---

# 1. FinOps Foundation

Le catalogue FinOps Foundation s'est fortement étoffé.

## Niveaux / credentials

On retrouve notamment :

- FinOps Certified Practitioner ;
- FinOps Certified Engineer ;
- FinOps Certified FOCUS Analyst ;
- certifications spécialisées AI / Technology Value ;
- FinOps Certified Professional.

## Prix publics couramment affichés en 2026

Les pages du catalogue peuvent nécessiter une authentification pour afficher l'achat. Une grille 2026 consolidée par Flexera, à revérifier au checkout FinOps Foundation, donne :

| Parcours | Prix indicatif |
|---|---:|
| Practitioner — exam only | **325 $** |
| Practitioner — self-paced + exam | **500 $** |
| Practitioner — virtual instructor-led + exam | **1 500 $** |
| Engineer — exam only | **325 $** |
| Engineer — self-paced + exam | **500 $** |
| FOCUS Analyst | **400 $** |
| FinOps Certified Professional | **1 999 $** |
| Professional + FOCUS bundle | **2 100 $** |
| Practitioner + Professional + FOCUS bundle | **2 250 $** |

Source tarifaire secondaire :

- https://www.flexera.com/blog/finops/finops-certifications/

Source officielle programme :

- https://www.finops.org/training-certification/

## Nouveau point important — Professional

La FinOps Foundation précise que le Professional n'est plus simplement un examen avancé isolé.

Pour être autorisé à passer l'examen Professional, le candidat doit avoir **actifs** :

- FinOps Certified FOCUS Analyst ;
- FinOps Certified: AI Value ;
- FinOps Certified: Technology Value.

Le parcours demande également :

- Professional Contribution ;
- réussite de l'examen ;
- accès au programme pendant 12 mois ;
- certification valide **2 ans**.

Les examens offrent **trois tentatives** selon la FAQ générale.

Source :

- https://www.finops.org/training-certification/training-faqs/

### Conséquence TCO

Le prix affiché du Professional ne doit donc pas être considéré indépendamment des credentials préalables lorsqu'on part de zéro.

À terme, calculer deux valeurs :

```text
Professional incremental cost
Professional from-zero TCO
```

---

# 2. Veeam — nouveau programme 2026

Veeam a retiré les anciens examens **VMCE** et **VMCA** et lancé une nouvelle génération basée sur :

- **VMCE+ — Veeam Certified Engineer+** ;
- **VMCSE — Veeam Certified Security Expert**.

L'ancien VMCE a été prolongé jusqu'au **31 mars 2026**, puis remplacé par VMCE+.

## VMCE+ — live depuis juin 2026

VMCE+ a été officiellement lancé le **1er juin 2026**.

Veeam indique explicitement que les formations pertinentes constituent un **hard requirement** avant l'examen.

Pour être éligible à VMCE+, le candidat doit compléter trois formations :

1. **Veeam Backup & Replication: Configure, Manage, and Recover** ;
2. **Veeam Data Platform: Monitor, Manage, Analyze (Veeam ONE)** ;
3. **Veeam Data Platform: Scale, Automate, Secure (Veeam Recovery Orchestrator)**.

Puis :

4. réussir l'examen VMCE+ proctoré.

Le programme Veeam University PRO décrit environ **55+ heures** de formation self-paced pour la séquence VMCE+.

Sources officielles :

- https://www.veeam.com/support/training/vmce-training-faq.html
- https://www.veeam.com/support/training/vmce-certification.html
- https://www.veeam.com/support/training/veeam-university-pro.html

Confirmation de lancement :

- https://community.veeam.com/vmce-study-hall-134/vmce-certification-officially-released-13397

### Exception transition

Un titulaire VMCE v12 ou une personne ayant déjà suivi la formation VBR v12/v13 peut satisfaire le prérequis VBR et n'avoir à compléter que Veeam ONE + Orchestrator avant VMCE+ selon les règles de transition publiées au lancement.

Mais l'examen VMCE+ couvre bien les trois domaines.

---

# VMCSE

VMCSE est le niveau supérieur orienté :

- sécurité ;
- résilience ;
- ransomware defense ;
- conformité ;
- Zero Trust ;
- intégration avec frameworks cybersécurité et SIEM/SOAR ;
- enterprise data protection.

**VMCE+ est un hard requirement pour VMCSE.**

Le parcours ajoute :

- **Veeam Data Platform: Enterprise Data Security** ;
- environ **16+ heures** self-paced dans la présentation University PRO ;
- puis l'examen VMCSE.

La page officielle Veeam Certification expose désormais le workflow permettant de programmer VMCE+ et VMCSE depuis le compte Veeam / Pearson Professional Assessments. Le prix public France de l'examen reste toutefois absent de la FAQ publique : vérifier dans le compte au moment de l'inscription.

---

# Coût réel Veeam

Le prix public de l'examen VMCE+/VMCSE n'est toujours pas clairement publié dans la FAQ : Veeam renvoie vers Pearson pour le tarif final régional.

Mais la partie formation suffit déjà à démontrer que le TCO dépasse très largement 500 € lorsqu'on part de zéro.

## Exemple France 2026 — formation VBR seule

Un organisme de formation français affiche en 2026 le cours officiel :

**Veeam Backup & Replication: Configure, Manage and Recover v13**

```text
Durée       4 jours / 28 h
Prix        3 440 € HT
```

Ce tarif ne couvre que **le premier des trois blocs de formation VMCE+** dans un scénario instructor-led.

Source tarifaire France :

- https://www.ittcert.fr/ContentV11/doc/pdf/programme/fr/fra/fr/VAZ.pdf

## Veeam ONE + Orchestrator

Les deux autres blocs nécessaires au VMCE+ sont proposés principalement via **Veeam University PRO eLearning** dans le modèle 2026.

Veeam indique que les tarifs PRO passent par le réseau VMAEC / partenaires et ne publie pas un tarif individuel France universel directement sur la page publique.

### Conclusion TCO VMCE+

```text
VMCE+ from zero
= VBR training
+ Veeam ONE training
+ Orchestrator training
+ exam
```

Même sans connaître le prix exact de l'examen, le simple exemple français à **3 440 € HT** pour VBR démontre que VMCE+ doit être classé comme parcours **premium / employer-funded** et non comme certification low-cost.

---

# TCO VMCSE

```text
VMCSE from zero
= VMCE+ from-zero TCO
+ Enterprise Data Security training
+ VMCSE exam
```

Le coût réel depuis zéro est donc supérieur encore au parcours VMCE+.

---

# Rubrik : contraste intéressant

À comparer avec Rubrik University, qui propose un **RCSA exam preparation learning plan gratuit** et indique que le cours instructor-led de quatre jours est recommandé mais **pas obligatoire** pour le credential RCSA.

Chez Veeam, la formation est explicitement obligatoire pour être éligible à l'examen : les deux vendors ont donc une philosophie de TCO très différente.

---

# Comparaison de philosophie

## FinOps

Le TCO augmente à cause des **credentials préalables** et de la progression de niveau.

## Veeam

Le TCO augmente à cause des **formations obligatoires**.

C'est exactement pourquoi le catalogue human-skills sépare :

```text
exam_fee
mandatory_training
mandatory_credentials
first_cycle_tco
```

---

# À compléter au checkout

## FinOps

- prix officiels live AI Value ;
- Technology Value ;
- prix exact from-zero Professional ;
- prix recertification.

## Veeam

- prix Pearson VMCE+ France ;
- prix Pearson VMCSE France ;
- abonnement Veeam University PRO individuel EMEA ;
- prix séparés Veeam ONE / Orchestrator / Enterprise Data Security ;
- durée / règles de renouvellement VMCE+ et VMCSE.
