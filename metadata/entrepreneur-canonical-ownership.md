# Entrepreneur — canonical credential ownership

> Règle de maintenance : **un credential peut être recommandé dans plusieurs fiches, mais ses données détaillées (prix, TCO, prérequis, durée, renouvellement) ne doivent vivre que dans une fiche canonique.**

## Fiches canoniques

| Famille | Fiche propriétaire |
|---|---|
| Création généraliste, micro, IBM/HP/OpenLearn, Certiport ESB, NCFE/SFEDI, BGE, CréActifs, Cnam | `certifications/entrepreneurship-startup-business-creation-2026.md` |
| CCI opérationnelles France : RS6951, RS7378, RS7380, RS7385, RS7376, RS6952, RS7377, RS7382, RS7379, RS7383 | `certifications/entrepreneur-essential-operations-2026.md` |
| HubSpot, Google, Xero, QuickBooks, AMA, Salesforce, PSM I, ASQ, WorldCC, HRCI, IAPP, ICC | `certifications/entrepreneur-international-functional-credentials-2026.md` |
| CFI FMVA/CBCA, VC University, WIPO, Amazon Ads, Shopify, CICM, Harvard PON | `certifications/entrepreneur-growth-finance-ecommerce-ip-2026.md` |
| CCI RS7413, Bpifrance Transmission, FFF, IFA, RIMS-CRMP, ARM, FCIB | `certifications/entrepreneur-transfer-franchise-risk-financing-france-2026.md` |
| IESE Search Fund, family business, ESS, V.I.E, activités réglementées | `certifications/entrepreneur-eta-family-ess-export-regulated-2026.md` |
| CCI recouvrement, AMRAE, AFDCC, INPI Prédiagnostic/Pass PI, EUIPO SME Fund, France Num e-facture, aides publiques | `certifications/entrepreneur-france-practical-resources-2026.md` |
| CMA RS6996 / RS6994, Chambres d'agriculture RS7277, radar microcredentials sectoriels | `certifications/entrepreneur-artisan-agri-uk-microcredentials-2026.md` |

## Ce qui est autorisé hors fiche canonique

```text
nom du credential
+ raison de le regarder
+ lien vers la fiche canonique
```

## Ce qui doit rester canonique

```text
prix
TCO
membership
prérequis
validité
renewal
nombre de questions
score de réussite
durée détaillée
liste exhaustive de modules
sources primaires
```

## Index

`ENTREPRENEUR-INDEX.md` est un **routeur de décision** : priorité P0/P1/P2, budget et besoin. Il ne doit pas devenir une seconde base de prix.

`GROUP-MANAGEMENT-INDEX.md` est le routeur de la couche groupe et ne doit pas réabsorber les détails du cœur Entrepreneur.

## Convention lors d'un ajout

1. choisir le propriétaire canonique ;
2. ajouter les détails uniquement là ;
3. dans les autres fiches, ajouter un cross-link ;
4. exécuter `python tools/audit-entrepreneur-duplicates.py` ;
5. exécuter l'audit géographique habituel.
