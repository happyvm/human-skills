# Enterprise messaging / event streaming certifications — 2026

> Revue : **28 août 2026**. Complément aux catalogues Kafka, Solace et IBM MQ : Apache Pulsar, RabbitMQ, NATS et autres stacks de messaging/event streaming.

---

# Résumé

| Écosystème | Credential | Prix observé | Statut |
|---|---|---:|---|
| Solace | plusieurs Practitioner / Architect | **0 $** | ✅ voir middleware file |
| Confluent Kafka | certification | **150 $** | ✅ déjà référencé data platforms |
| IBM MQ 9.4 | Administrator Professional | **200 $** | ✅ déjà référencé IBM |
| Apache Pulsar / StreamNative | Developer Certification Level 1 | **295 $** | ✅ mais enrollment actuellement fermé |
| RabbitMQ | certification professionnelle actuelle identifiée | non trouvée | 🔎 watchlist |
| NATS / Synadia | certification professionnelle actuelle identifiée | non trouvée | 🔎 watchlist |

---

# 1. Apache Pulsar — StreamNative Developer Certification Level 1

StreamNative Academy, société fondée autour des créateurs d'Apache Pulsar, maintient un vrai parcours :

**Apache Pulsar Developer Certification Level 1: Fundamentals**

```text
Prix affiché      295 $
Format            self-paced
Durée estimée     10–12 h
Grade minimum     80 %
Coding exam       Java / Pulsar Java client
Accès cluster     4 jours pour l'examen pratique
```

Le parcours comprend :

- 8 knowledge-check quizzes ;
- un coding examination représentant 75 % de la note ;
- publication/consommation async ;
- partitioned topics ;
- shared / key-shared subscriptions ;
- delayed messages ;
- schemas ;
- Reader API ;
- TableView ;
- acknowledgements / nacks ;
- Java Admin APIs ;
- sécurité.

### État de disponibilité

La page actuelle affiche :

```text
Current Status   Not Enrolled
Price            295 $
Course           currently closed
Enrollment       contacter StreamNative Training
```

Il s'agit donc d'un credential réel avec tarif public, mais **pas d'un examen achetable immédiatement en libre-service au moment de la revue**.

Source :

- https://courses.streamnative.io/courses/apache-pulsar-developer-certification-level-1-fundamentals/

---

# 2. StreamNative : formations gratuites et payantes

StreamNative Academy propose en parallèle :

- Getting Started with Pulsar — tutorials gratuits ;
- Getting Started with Kafka — tutorials gratuits ;
- Introduction to StreamNative and Apache Pulsar ;
- Practical Apache Pulsar Application Development — payant ;
- Pulsar Operations Training — payant ;
- Developer Certification Level 1.

Ces tutorials/cours gratuits ne doivent pas être confondus avec la certification Developer à 295 $.

Source :

- https://courses.streamnative.io/

---

# 3. RabbitMQ — pas de credential professionnel actuel confirmé

RabbitMQ reste une technologie majeure de messaging. L'offre enterprise est aujourd'hui portée notamment par **VMware Tanzu RabbitMQ** / Broadcom.

Cette revue n'a cependant pas identifié de **certification professionnelle actuelle spécifiquement RabbitMQ**, avec examen public et prix, dans les catalogues actuels Broadcom/VMware consultables publiquement.

### Classification

```text
RabbitMQ skill              très pertinent
Cours / documentation       oui
Produit enterprise          Tanzu RabbitMQ
Certification standalone    non confirmée
```

Ne pas recycler d'anciennes références VMware/Pivotal comme si elles constituaient un examen 2026 live.

Source produit actuelle :

- https://www.vmware.com/products/app-platform/tanzu-data-intelligence/rabbitmq

---

# 4. NATS / Synadia — pas de certification professionnelle confirmée

NATS est très intéressant pour :

- cloud-native messaging ;
- request/reply ;
- pub/sub ;
- JetStream ;
- edge ;
- distributed systems ;
- lightweight event-driven architectures.

Mais cette passe n'a pas identifié de programme actuel **Synadia Certified NATS Administrator/Developer** ou équivalent avec examen public.

### Verdict

NATS reste une **compétence à pratiquer**, mais ne doit pas être listé comme certification tant qu'un credential officiel n'est pas publié.

Source écosystème :

- https://www.synadia.com/
- https://docs.synadia.com/

---

# 5. Les alternatives déjà fortes dans le dépôt

## Confluent Kafka

Déjà documenté dans :

- [`data-database-platforms-under-500.md`](data-database-platforms-under-500.md)

Prix observé : **150 $**.

## IBM MQ

Déjà documenté dans :

- [`ibm-enterprise-security-low-cost-2026.md`](ibm-enterprise-security-low-cost-2026.md)

IBM MQ 9.4 Administrator Professional : **200 $**.

## Solace

Déjà documenté dans :

- [`middleware-api-integration-2026.md`](middleware-api-integration-2026.md)

Plusieurs credentials sont gratuits, notamment :

- Developer Practitioner ;
- Event Driven Architecture Practitioner ;
- Solutions Consultant ;
- Agent Mesh Practitioner.

Le niveau Event Broker Administrator Associate coûte **500 $**.

---

# 6. Classement ROI messaging / streaming

```text
0 $      Solace Developer / EDA / Agent Mesh
150 $    Confluent Kafka
200 $    IBM MQ Administrator Professional
295 $    Apache Pulsar Developer Level 1 — lorsque enrollment ouvert
500 $    Solace Event Broker Administrator Associate
?        RabbitMQ — aucun examen professionnel live confirmé
?        NATS — aucun examen professionnel live confirmé
```

---

# 7. Parcours multi-messaging recommandé

Pour obtenir du signal sur plusieurs modèles de messaging :

```text
Solace EDA Practitioner          0 $
Confluent Kafka                150 $
IBM MQ Administrator           200 $
Apache Pulsar Developer        295 $  lorsque disponible
------------------------------------
Total                          645 $
```

En restant sous 500 $ :

```text
Solace EDA Practitioner          0 $
Confluent Kafka                150 $
IBM MQ Administrator           200 $
------------------------------------
Total                          350 $
```

Cette combinaison couvre **event-driven architecture + streaming + enterprise messaging traditionnel**.

---

# Watchlist

À surveiller :

- réouverture StreamNative Pulsar Developer Certification ;
- éventuel Pulsar Operator/Admin certification ;
- future certification NATS/Synadia ;
- programme RabbitMQ/Broadcom officiel ;
- Apache ActiveMQ / Artemis ;
- Redpanda ;
- WarpStream ;
- Amazon MSK / EventBridge credentials spécifiques ;
- Azure Service Bus / Event Hubs Applied Skills ;
- Google Pub/Sub skill badges / credentials.
