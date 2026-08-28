---
title: "Open networking / SONiC / AI fabrics — certification status 2026"
type: certification-catalog
tier: general
domain:
  - network
tags:
  - tier/general
  - domain/network
status: active
verified: 2026-08-28
---

# Open networking / SONiC / AI fabrics — certification status 2026

> Revue : **28 août 2026**. Objectif : identifier les credentials crédibles autour de SONiC, Ethernet AI fabrics, RoCE, DPU/SuperNIC et réseaux GPU sans inventer de certification qui n'existe pas.

---

# SONiC

## Pas de certification professionnelle officielle identifiée

À la date de cette revue, aucune **certification professionnelle officielle SONiC** clairement proposée par la SONiC Foundation ou la Linux Foundation n'a pu être identifiée dans leurs catalogues publics.

L'écosystème SONiC Foundation propose notamment :

- documentation et ressources communautaires ;
- workshops / tutorials ;
- mentorships Linux Foundation ;
- événements et contenus techniques autour du réseau ouvert.

Mais ces activités ne doivent pas être présentées comme une certification professionnelle SONiC.

### Verdict

**Watchlist.** SONiC est techniquement très pertinent pour les datacenters modernes et les fabrics IA, mais il n'existe pas aujourd'hui de credential officiel comparable à CKA, JNCIS ou NVIDIA NCP-AIN que l'on puisse recommander comme certification standalone.

Sources :

- https://sonicfoundation.dev/
- https://mentorship.lfx.linuxfoundation.org/project/0c1f4cc0-3cbd-4bf9-8ad0-8a02aac3e8dc
- https://www.linuxfoundation.org/blog/blog/sonic-foundation-advances-open-source-networking-for-the-ai-era

---

# Pourquoi SONiC reste à surveiller

La Linux Foundation présente SONiC comme une brique de plus en plus importante pour les réseaux ouverts et les infrastructures IA, avec des travaux portant notamment sur :

- montée en charge BGP ;
- EVPN / datacenter fabrics ;
- SRv6 ;
- telemetry ;
- packet trimming ;
- automatisation et opérations réseau à grande échelle.

La compétence SONiC elle-même peut donc avoir beaucoup de valeur même en l'absence de certification dédiée.

---

# Credential proxy le plus pertinent : NVIDIA NCP-AIN

Pour certifier des compétences adjacentes aux réseaux GPU/AI fabrics, le meilleur credential actuellement identifié est :

**Auto-formation officielle et gratuite :** [learn.nvidia.com](https://learn.nvidia.com/) — Deep Learning Institute, filtre « Free Courses », dont le learning path AI Networking.

## NVIDIA-Certified Professional: AI Networking — NCP-AIN

- prix : **400 $** ;
- niveau : Professional ;
- durée : environ **120 minutes** ;
- domaines couverts dans le blueprint :
  - Spectrum-X ;
  - Ethernet / RoCE ;
  - InfiniBand ;
  - BGP / EVPN ;
  - NVIDIA Cumulus Linux ;
  - NetQ ;
  - ConnectX / SuperNIC ;
  - BlueField / DPU ;
  - DOCA ;
  - Kubernetes Network Operator ;
  - automation et troubleshooting.

L'ancienne **NCP InfiniBand** a été retirée ; NVIDIA oriente désormais vers NCP-AIN pour les compétences networking liées aux infrastructures IA.

Sources :

- https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/
- https://www.nvidia.com/en-us/learn/learning-paths/ai-networking/
- https://www.nvidia.com/en-us/learn/certification/infiniband-professional/

---

# Spectrum-X / Ethernet AI fabric

L'écosystème NVIDIA Spectrum-X combine notamment :

- Spectrum switches ;
- Cumulus Linux ;
- ConnectX SuperNICs ;
- BlueField DPUs ;
- DOCA ;
- NetQ ;
- RoCE / congestion control / telemetry ;
- intégration Kubernetes et AI clusters.

Même si ce n'est pas un credential SONiC, **NCP-AIN couvre actuellement mieux le marché des AI fabrics** qu'une éventuelle formation SONiC non certifiante.

Source :

- https://docs.nvidia.com/networking/display/spectrumxvalidateddesignguide

---

# Parcours open networking / AI networking recommandé

```text
Juniper JNCIA via Open Learning        50 $
Infoblox DDI Associate                 29 $
Infoblox DDI Professional              69 $
NVIDIA NCA-AIIO                       125 $
NVIDIA NCP-AIN                        400 $
SONiC labs / community                gratuit / non certifiant
```

Pour un profil datacenter/HPC, la combinaison **Infoblox + Juniper + NCP-AIN + pratique SONiC** donne aujourd'hui plus de signal vérifiable qu'attendre une certification SONiC officielle qui n'existe pas encore.

---

# Watchlist

À surveiller :

- future certification SONiC Foundation / Linux Foundation ;
- certifications Ethernet AI fabric vendor-neutral ;
- DPU / SmartNIC / SuperNIC credentials ;
- Ultra Ethernet Consortium ;
- Open Compute Project networking ;
- NVIDIA Spectrum-X / BlueField spécialisations supplémentaires ;
- certification autour de Cumulus Linux si un programme standalone réapparaît.
