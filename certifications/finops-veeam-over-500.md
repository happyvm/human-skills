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

Veeam a retiré les anciens examens **VMCE** et **VMCA** et lancé un nouveau programme basé sur :

- VMCE+ ;
- VMCSE.

## VMCE+

Veeam indique explicitement que la formation pertinente est un **hard requirement** avant l'examen.

Pour être éligible à VMCE+, le candidat doit compléter trois formations :

1. **Veeam Backup & Replication: Configure, Manage, and Recover** ;
2. **Veeam Data Platform: Monitor, Manage, Analyze (Veeam ONE)** ;
3. **Veeam Data Platform: Scale, Automate, Secure (Veeam Orchestrator)**.

Puis :

4. réussir l'examen VMCE+.

Source officielle :

- https://www.veeam.com/support/training/vmce-training-faq.html
- https://www.veeam.com/support/training/vmce-certification.html

### Exception transition

Un titulaire VMCE v12 ou une personne ayant déjà suivi la formation VBR v12/v13 peut satisfaire le prérequis VBR et n'avoir à compléter que Veeam ONE + Orchestrator avant VMCE+.

Mais l'examen VMCE+ couvre bien les trois domaines.

---

# VMCSE

VMCSE est le niveau supérieur orienté :

- sécurité ;
- résilience ;
- ransomware defense ;
- conformité ;
- enterprise data protection.

**VMCE+ est un hard requirement pour VMCSE.**

Le parcours ajoute des formations Veeam Data Platform Enterprise Data Security selon le track actif.

---

# Coût réel Veeam

Le prix public de l'examen VMCE+/VMCSE n'est pas clairement publié sur la FAQ : Veeam renvoie vers Pearson VUE pour le tarif final.

En revanche, la partie formation permet déjà de démontrer que le TCO dépasse souvent largement 500 €.

## Exemple France — Instructor-Led

Un centre de formation Veeam en France affiche la formation v13 **Veeam Backup & Replication: Configure, Manage, and Recover** autour de **3 300 € HT** pour quatre jours.

Les formations Veeam ONE et Orchestrator nécessaires au nouveau VMCE+ sont disponibles principalement via **Veeam University PRO eLearning** dans le modèle de lancement 2026.

### Modèle PRO

Veeam University PRO propose les contenus alignés sur les nouvelles certifications. Les offres passent notamment par des partenaires / distributeurs et peuvent être vendues sous forme de subscriptions multi-utilisateurs.

Le prix individuel public France n'est pas assez transparent pour figer un TCO universel.

### Conclusion

```text
VMCE+ from zero
= VBR training
+ Veeam ONE training
+ Orchestrator training
+ exam
```

Il s'agit donc clairement d'un parcours **premium**, même si le voucher d'examen lui-même reste potentiellement modéré.

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

- prix Pearson VUE VMCE+ France ;
- prix Pearson VUE VMCSE France ;
- abonnement Veeam University PRO individuel EMEA ;
- prix des nouveaux modules de formation officiels ;
- durée / renouvellement de VMCE+ et VMCSE.
