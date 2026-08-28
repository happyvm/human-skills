# Rubrik & Veeam — certification data protection 2026

> Deux modèles opposés : Rubrik propose une préparation RCSA gratuite sans bootcamp obligatoire ; Veeam impose une chaîne de formations avant ses nouveaux examens VMCE+/VMCSE. Vérification : 28 août 2026.

---

# Rubrik Certified System Administrator — RCSA

Rubrik University propose deux chemins de préparation au même examen RCSA.

## Free Certification Learning Path

Le parcours gratuit comprend :

- eLearning self-paced ;
- practice exams ;
- **tentatives practice illimitées** ;
- feedback immédiat ;
- accès au chemin menant au final exam.

Source officielle :

- https://training.rubrik.com/

Rubrik indique explicitement que le bootcamp payant **n'est pas requis**.

Citation conceptuelle du modèle :

```text
FREE RCSA journey
= eLearning
+ unlimited practice exams
+ final-exam preparation path
```

---

## Paid Certification Learning Path

Rubrik propose parallèlement un bootcamp virtuel hands-on de **4 jours**.

Mais Rubrik précise qu'investir dans ce bootcamp **is not required** pour préparer/passer le RCSA.

Il ne faut donc jamais calculer :

```text
RCSA TCO = bootcamp price + exam
```

pour un candidat capable de self-study.

Source :

- https://training.rubrik.com/

---

## Prix du final RCSA

Au moment de la revue, la page publique Rubrik :

- confirme les examens de certification ;
- confirme le parcours gratuit ;
- confirme que le bootcamp est facultatif ;
- **n'affiche pas un prix public fiable du final exam**.

Rubrik University exige par ailleurs des **Rubrik Support credentials** pour accéder au portail complet.

Source :

- https://training.rubrik.com/rubrik-training

### Statut catalogue

```yaml
training_required: false
free_self_study: true
practice_exams: unlimited
final_exam_fee: TBD / portal-required
public_access: support-credential gated
status: PRICE-OPAQUE
```

> Ne pas utiliser les montants trouvés sur des blogs/forums comme tarif officiel 2026.

---

# Veeam — nouveau programme 2026

Les anciennes VMCE/VMCA sont retirées. Veeam a lancé une nouvelle génération :

- **VMCE+ — Veeam Certified Engineer+** ;
- **VMCSE — Veeam Certified Security Expert**.

Source officielle :

- https://www.veeam.com/support/training/vmce-training-faq.html
- https://www.veeam.com/support/training/vmce-certification.html

---

# VMCE+ — formation obligatoire

Veeam indique explicitement que la participation aux formations pertinentes est un **hard requirement** avant les examens.

Pour VMCE+, Veeam University PRO liste trois blocs :

1. **Veeam Backup & Replication: Configure, Manage, and Recover** ;
2. **Veeam Data Platform: Monitor, Manage, Analyze (Veeam ONE)** ;
3. **Veeam Data Platform: Scale, Automate, Secure (Veeam Recovery Orchestrator)**.

Durée totale annoncée pour le bundle self-paced : **55+ heures**.

Source :

- https://www.veeam.com/support/training/veeam-university-pro.html

### Modèle TCO

```text
VBR training
+ Veeam ONE training
+ VRO training
+ VMCE+ exam
= VMCE+ credential
```

Donc même si le voucher d'examen est raisonnable, le coût minimal n'est pas celui du voucher seul.

---

# Exception pour anciens VMCE

Le programme 2026 prévoit des équivalences de formation dans certains cas historiques.

La communication Veeam Community indique notamment qu'un détenteur de VMCE v12 / formation VBR pertinente peut être dispensé de refaire le bloc VBR selon les conditions de transition.

La source officielle à utiliser au moment de l'inscription reste le profil Veeam / University.

Source complémentaire :

- https://community.veeam.com/blogs-and-podcasts-57/vmce-certification-is-live-13449

---

# VMCSE — security expert

Le VMCSE valide notamment :

- enterprise data protection security ;
- zero trust ;
- cyber resilience ;
- compliance readiness ;
- SIEM / SOAR integration ;
- Veeam Data Platform security capabilities.

## Prérequis obligatoires

Veeam indique :

1. **détenir VMCE+** ;
2. **suivre Enterprise Data Security training** ;
3. passer VMCSE exam.

La formation Enterprise Data Security est annoncée à **16+ heures self-paced**.

Source :

- https://www.veeam.com/support/training/vmce-certification.html
- https://www.veeam.com/support/training/veeam-university-pro.html

### TCO depuis zéro

```text
VMCE+ mandatory training        55+ h
VMCE+ exam
        ↓
Enterprise Data Security       16+ h
VMCSE exam
```

Soit déjà **71+ heures de formation obligatoire**, sans compter préparation personnelle.

---

# Prix des examens Veeam

Veeam ne publie pas de tarif mondial unique.

La FAQ officielle indique :

- les prix varient selon le pays ;
- le prix final est communiqué par **Pearson VUE** ;
- l'examen n'est pas inclus dans le prix de formation.

Source :

- https://www.veeam.com/fr/support/training/vmce-training-faq.html

### Statut

```yaml
VMCE_plus_exam_fee: regional / Pearson VUE
VMCSE_exam_fee: regional / Pearson VUE
mandatory_training: true
training_price: partner/distributor/University PRO
status: REGIONAL-TCO
```

---

# Différence fondamentale Rubrik vs Veeam

## Rubrik

```text
Free eLearning
+ unlimited practice exams
+ bootcamp optional
+ final exam price portal-only
```

## Veeam

```text
Mandatory training chain
+ regional exam fee
+ prerequisite certification for VMCSE
```

Ces deux programmes illustrent pourquoi il est faux de comparer simplement un `exam_fee`.

---

# Valeur professionnelle

## Rubrik RCSA

**⭐⭐⭐⭐** à **⭐⭐⭐⭐⭐** dans un environnement Rubrik, surtout compte tenu du self-study gratuit.

## VMCE+

**⭐⭐⭐⭐⭐** dans un SI Veeam : credential éditeur avancé, mais TCO plus élevé.

## VMCSE

**⭐⭐⭐⭐⭐** pour data protection + cyber resilience / security architecture.

---

# À récupérer ensuite

- prix officiel RCSA final dans Rubrik University ;
- accès Rubrik pour candidat non-client/non-partner ;
- retake RCSA ;
- validité/renewal RCSA ;
- prix Veeam University PRO France/EMEA ;
- prix Pearson VUE VMCE+ France ;
- prix Pearson VUE VMCSE France ;
- validity / recertification VMCE+/VMCSE ;
- Veeam partner/customer discounts ;
- Rubrik Security Cloud advanced credentials ;
- Cohesity advanced certification stack ;
- Commvault 2026 advanced/expert refresh.
