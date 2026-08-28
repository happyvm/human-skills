# Red Hat certification framework & Europe pricing — 2026

> Revue : **28 août 2026**. Cette fiche corrige deux points importants : la refonte du framework Red Hat en mai 2026 et le fait que le prix catalogue US à 500 $ ne signifie pas nécessairement « moins de 500 € » en Europe.

---

# Refonte du programme — mai 2026

Red Hat indique qu'à compter du **11 mai 2026**, son programme de certification a été réorganisé en un framework progressif structuré en **5 niveaux / tracks de spécialisation**, alignés avec ses plateformes principales :

- Red Hat Enterprise Linux ;
- OpenShift ;
- Ansible ;
- AI ;
- autres spécialisations Red Hat selon le parcours.

Un nouveau niveau **Technologist** facilite l'entrée dans le programme, tandis que la progression vers les niveaux supérieurs renouvelle automatiquement certaines certifications de niveau identique ou inférieur.

Source :

- https://www.redhat.com/en/services/training-and-certification/faq

---

# OpenShift — parcours avancé / RHCA

Le catalogue Red Hat 2026 expose une route OpenShift très structurée.

## Examens obligatoires du niveau avancé OpenShift

```text
EX280  Red Hat Certified OpenShift Administrator
EX380  Red Hat Certified Advanced System Administrator in OpenShift
```

Puis réussir **au moins trois** examens parmi une liste de spécialisations comprenant notamment :

```text
EX229  ROSA
EX282  OpenShift Networking
EX316  OpenShift Virtualization
EX336  Automating OpenShift Virtual Machine Management
EX370  OpenShift Data Foundation
EX430  OpenShift Advanced Cluster Security
EX432  OpenShift Advanced Cluster Management
EX480  MultiCluster Management
```

Source :

- https://www.redhat.com/en/services/certifications

---

# Examens particulièrement pertinents infrastructure

## EX316 — OpenShift Virtualization

Certification : **Red Hat Certified Specialist in OpenShift Virtualization**.

- OpenShift Container Platform 4.18 dans la version actuellement publiée ;
- déploiement de l'opérateur OpenShift Virtualization ;
- provisioning et administration de VM ;
- networking, storage et opérations système ;
- examen performance-based ;
- durée annoncée : **4 heures** ;
- compte pour RHCA.

Source :

- https://www.redhat.com/en/services/training/red-hat-certified-specialist-openshift-virtualization-ex316

## EX260 — Ceph Cloud Storage

Certification : **Red Hat Certified Specialist in Ceph Cloud Storage**.

Compétences :

- installation/configuration cluster Ceph ;
- RBD ;
- RADOSGW ;
- CephFS ;
- CRUSH maps ;
- tuning ;
- troubleshooting ;
- intégration OpenStack/OpenShift.

L'examen est performance-based, dure environ **3 heures** et compte pour RHCA.

Sources :

- https://www.redhat.com/en/services/training/ex260-red-hat-certified-specialist-in-ceph-cloud-storage-exam
- https://www.redhat.com/en/services/certification/rhcs-ceph-cloud-storage

## EX430 — OpenShift Advanced Cluster Security

Certification spécialisée sur **Red Hat Advanced Cluster Security for Kubernetes**.

- sécurité OpenShift/Kubernetes ;
- examen pratique ;
- durée annoncée : **4 heures** ;
- compte pour RHCA.

Source :

- https://www.redhat.com/en/services/training/ex430-red-hat-certified-specialist-openshift-advanced-cluster-security-exam

## EX267 — Red Hat Certified Developer in AI

Red Hat a actualisé EX267 autour d'**OpenShift AI**, MLOps et GenAIOps.

- OpenShift AI 3.3 / OpenShift Container Platform 4.20 dans la version publiée ;
- workbenches et data science projects ;
- S3 / data connections ;
- model serving ;
- modèles prédictifs et génératifs ;
- examen performance-based.

Jusqu'au **31 décembre 2026**, Red Hat annonce une remise de **50 %** sur le cours AI267LS, avec **une tentative EX267 incluse** dans le bundle de cours.

Sources :

- https://www.redhat.com/en/services/training/ex267-red-hat-certified-developer-in-ai
- https://www.redhat.com/en/services/training/ai267-developing-and-deploying-ai/ml-applications-on-red-hat-openshift-ai

---

# Prix Europe : attention au seuil de 500 €

Le chiffre de **500 $** souvent cité correspond au pricing US de nombreux examens individuels.

Un partenaire Red Hat/Global Knowledge affiche en Europe un **KIOSK exam voucher à 530 € HT**, couvrant notamment des examens tels que :

- EX260 Ceph ;
- EX316 OpenShift Virtualization ;
- plusieurs autres Individual Exams Red Hat.

Cela signifie qu'une classification simple « Red Hat = ≤500 » est **fausse pour un acheteur européen**.

```text
US catalogue / référence fréquente : ~500 $
Exemple EMEA partenaire :             530 € HT
Avec TVA française potentielle :      nettement > 500 € TTC
```

Sources :

- https://www.globalknowledge.com/fr-be/products/red_hat/kiosk-exam
- https://www.redhat.com/en/services/certification/individual-exams

---

# Retake inclus

Red Hat indique dans ses politiques 2026 qu'un candidat ayant acheté un **Individual Exam** et échoué à sa première tentative peut bénéficier d'**une tentative de rattrapage gratuite**, à utiliser dans la période d'éligibilité d'un an.

Cela améliore fortement le TCO réel par rapport aux vendors facturant chaque retake plein tarif.

Source :

- https://www.redhat.com/en/about/red-hat-training-policies

---

# Verdict budget

Pour un classement strict basé sur un budget individuel en France :

```text
<500 € TTC   ❌ ne pas considérer Red Hat comme garanti
~530 € HT    prix EMEA observé pour un voucher KIOSK
1 retake     inclus si première tentative échouée
```

Red Hat reste **très fort techniquement**, particulièrement EX316, EX260 et EX430, mais il faut le placer dans la tranche **500–700 € en Europe** plutôt que dans le catalogue low-cost strict.

---

# Parcours infrastructure recommandé

```text
RHCSA / socle Linux
      ↓
EX280 OpenShift Administrator
      ↓
EX380 Advanced OpenShift
      ↓
EX316 OpenShift Virtualization
EX370 OpenShift Data Foundation
EX430 Advanced Cluster Security
      ↓
RHCA-oriented OpenShift path
```

Pour un profil infrastructure/private cloud, **EX316 + EX260/EX370 + EX430** constitue une combinaison beaucoup plus différenciante qu'une simple accumulation de fundamentals cloud.
