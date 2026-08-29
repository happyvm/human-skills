# Cross-catalog overlap analysis

> Heuristic audit of Markdown catalogue tables. Exact matches are strong signals; near matches are review candidates, not automatic duplicates.

- catalogues scanned: **97**
- credential-like table rows scanned: **1401**
- exact normalized names present in 2+ files: **82**
- specialist↔specialist file pairs with exact overlap: **12**
- conservative near-duplicate candidates: **0**

## Interpretation

- `free-it.md`, `free-non-it.md`, `paid-under-500.md`, `paid-over-500.md` are treated as intentional aggregators.
- `entrepreneur*` catalogues are excluded from cleanup ranking because canonical ownership is already enforced separately.
- A specialist↔specialist overlap is the main signal for the next dedup pass.

## Highest-overlap specialist catalogue pairs

| Shared exact names | Catalogue A | Catalogue B | Examples |
|---:|---|---|---|
| 3 | `arista-academy-certification-2026.md` | `network-datacenter-advanced-under-500.md` | Expert practical exam, Professional practical exam, Specialist practical exam |
| 3 | `ibm-enterprise-security-ai-under-500.md` | `mainframe-enterprise-software.md` | IBM Db2 13 for z/OS DBA Professional, IBM MQ 9.4 Administrator Professional, IBM z/OS v3.x Administrator Professional |
| 3 | `hpe-morpheus-private-cloud-2026.md` | `virtualization-private-cloud-under-500.md` | Nutanix NCM-MCI, Nutanix NCP-MCI, VMware VCP-VCF Architect |
| 2 | `cyber-premium-over-500.md` | `practical-cyber-under-500.md` | CPSA, CPTIA, CPIA, CRT, CRTIA, CRIA |
| 2 | `compensation-total-rewards.md` | `management-transformation-over-500.md` | GPHR, HRCI SPHR / SPHRi / GPHR |
| 2 | `cloud-native-platform-engineering-under-500.md` | `observability-sre-devops-under-500.md` | OpenTelemetry Certified Associate, Prometheus Certified Associate |
| 1 | `ai-governance-risk-safety.md` | `privacy-dpo-france.md` | IAPP AIGP |
| 1 | `actuarial-accounting-insurance.md` | `insurance-risk-designations.md` | LOMA FLMI — non-member pricing |
| 1 | `ai-infrastructure-gpu-hpc-2026.md` | `network-datacenter-advanced-under-500.md` | NVIDIA |
| 1 | `construction-btp-global-2026.md` | `construction-cost-engineering.md` | PMI Construction Professional — PMI-CP |
| 1 | `iam-devsecops-automation-under-500.md` | `virtualization-private-cloud-under-500.md` | Red Hat exam standard |
| 1 | `observability-vendor-certifications-2026.md` | `observability-vendor-low-cost-2026.md` | Sumo Logic |

## Domain-pair overlap hotspots

| Exact overlaps | Domain A | Domain B |
|---:|---|---|
| 3 | `network` | `network` |
| 3 | `mainframe` | `security` |
| 3 | `virtualization` | `virtualization` |
| 2 | `security` | `security` |
| 2 | `governance-grc` | `hr-people` |
| 2 | `kubernetes-platform` | `observability` |
| 1 | `ai-infrastructure` | `legal` |
| 1 | `finance-risk` | `finance-risk` |
| 1 | `ai-infrastructure` | `network` |
| 1 | `construction-btp` | `supply-chain` |
| 1 | `identity-iam` | `virtualization` |
| 1 | `observability` | `observability` |

## Exact duplicate-name groups — specialist files

### IAPP AIGP

- `ai-governance-risk-safety.md:32` — `| IAPP AIGP | **649 $ membre / 799 $ non-membre** | maintenance 2 ans |`
- `privacy-dpo-france.md:35` — `| IAPP AIGP | **799 $ non-member exam + maintien** | cycle 2 ans | AI governance |`

### CPSA, CPTIA, CPIA

- `cyber-premium-over-500.md:31` — `| Practitioner | CPSA, CPTIA, CPIA | **275 £** |`
- `practical-cyber-under-500.md:214` — `| Practitioner | CPSA, CPTIA, CPIA | **275 £** |`

### CRT, CRTIA, CRIA

- `cyber-premium-over-500.md:32` — `| Registered | CRT, CRTIA, CRIA | **600 £** |`
- `practical-cyber-under-500.md:215` — `| Registered | CRT, CRTIA, CRIA | **600 £** |`

### Expert practical exam

- `arista-academy-certification-2026.md:30` — `| Expert | Expert practical exam | **1 995 $** |`
- `network-datacenter-advanced-under-500.md:37` — `| Arista | Expert practical exam | **1 995 $** | ❌ >500 |`

### GPHR

- `compensation-total-rewards.md:137` — `| GPHR | 100 $ | 495 $ | **595 $** | 🌍 INT |`
- `management-transformation-over-500.md:248` — `| GPHR | 100 $ | 495 $ | **595 $** |`

### HRCI SPHR / SPHRi / GPHR

- `compensation-total-rewards.md:33` — `| HRCI SPHR / SPHRi / GPHR | 1 examen | **595 $** total application+exam | 🌐 MIX |`
- `management-transformation-over-500.md:29` — `| HRCI SPHR / SPHRi / GPHR | **595 $** application incluse | Ressources humaines |`

### IBM Db2 13 for z/OS DBA Professional

- `ibm-enterprise-security-ai-under-500.md:34` — `| IBM Db2 13 for z/OS DBA Professional | **200 $** |`
- `mainframe-enterprise-software.md:29` — `| IBM Db2 13 for z/OS DBA Professional | **200 $** | Mainframe database |`

### IBM MQ 9.4 Administrator Professional

- `ibm-enterprise-security-ai-under-500.md:32` — `| IBM MQ 9.4 Administrator Professional | **200 $** |`
- `mainframe-enterprise-software.md:30` — `| IBM MQ 9.4 Administrator Professional | **200 $** | Middleware / messaging |`

### IBM z/OS v3.x Administrator Professional

- `ibm-enterprise-security-ai-under-500.md:30` — `| IBM z/OS v3.x Administrator Professional | **200 $** |`
- `mainframe-enterprise-software.md:27` — `| IBM z/OS v3.x Administrator Professional | **200 $** | Mainframe / z/OS |`

### LOMA FLMI — non-member pricing

- `actuarial-accounting-insurance.md:405` — `| LOMA FLMI — non-member pricing | **8 500 $** | 🌍 INT |`
- `insurance-risk-designations.md:309` — `| LOMA FLMI non-member pricing | **8 500 $** | 🌍 INT |`

### Nutanix NCM-MCI

- `hpe-morpheus-private-cloud-2026.md:218` — `| Nutanix NCM-MCI | **300 $** + prerequisite |`
- `virtualization-private-cloud-under-500.md:35` — `| Nutanix NCM-MCI | **300 $** | NCP/NCM valide requis | Advanced practical lab |`

### Nutanix NCP-MCI

- `hpe-morpheus-private-cloud-2026.md:215` — `| Nutanix NCP-MCI | **200 $** |`
- `virtualization-private-cloud-under-500.md:32` — `| Nutanix NCP-MCI | **~199–200 $** | ❌ | AHV / AOS / Prism / multicloud |`

### NVIDIA

- `ai-infrastructure-gpu-hpc-2026.md:27` — `| NVIDIA | NCA AI Infrastructure & Operations | **125 $** | ✅ excellent point d'entrée |`
- `ai-infrastructure-gpu-hpc-2026.md:28` — `| NVIDIA | NCP AI Infrastructure | **400 $** | ✅ sous 500 |`
- `ai-infrastructure-gpu-hpc-2026.md:29` — `| NVIDIA | NCP AI Networking | **400 $** | ✅ sous 500 |`
- `ai-infrastructure-gpu-hpc-2026.md:30` — `| NVIDIA | NCP AI Rack & Interconnect | **400 $** | ✅ sous 500 |`
- `ai-infrastructure-gpu-hpc-2026.md:31` — `| NVIDIA | NCP AI Operations | **500 $** | ✅ limite haute, hands-on lab |`
- `network-datacenter-advanced-under-500.md:28` — `| NVIDIA | NCA AI Infrastructure & Operations | **125 $** | ✅ sous 500 |`
- `network-datacenter-advanced-under-500.md:33` — `| NVIDIA | NCP AI Networking / Infrastructure / Rack | **400 $** | ✅ sous 500 |`
- `network-datacenter-advanced-under-500.md:35` — `| NVIDIA | NCP AI Operations | **500 $** | ⚠️ exactement à la limite |`

### OpenTelemetry Certified Associate

- `cloud-native-platform-engineering-under-500.md:40` — `| OpenTelemetry Certified Associate | **250 $** | proctored QCM | ⭐⭐⭐⭐ |`
- `observability-sre-devops-under-500.md:36` — `| OpenTelemetry Certified Associate | **250 $** | CNCF |`

### PMI Construction Professional — PMI-CP

- `construction-btp-global-2026.md:56` — `| PMI Construction Professional — **PMI-CP** | CERT | management de projet construction | 🌍 INT |`
- `construction-cost-engineering.md:30` — `| PMI Construction Professional — PMI-CP | **319 $ membre / 399 $ plein tarif** | 4 modules obligatoires + 3 ans expérience |`

### Professional practical exam

- `arista-academy-certification-2026.md:29` — `| Professional | Professional practical exam | **395 $** |`
- `network-datacenter-advanced-under-500.md:32` — `| Arista | Professional practical exam | **395 $** | ✅ sous 500 |`

### Prometheus Certified Associate

- `cloud-native-platform-engineering-under-500.md:37` — `| Prometheus Certified Associate | **250 $** | proctored QCM | ⭐⭐⭐⭐ |`
- `observability-sre-devops-under-500.md:35` — `| Prometheus Certified Associate | **250 $** | CNCF |`

### Red Hat exam standard

- `iam-devsecops-automation-under-500.md:31` — `| Red Hat exam standard | **500 $ list price** | performance-based |`
- `virtualization-private-cloud-under-500.md:36` — `| Red Hat certification exam standard | **500 $ list price** | selon examen | Linux / OpenShift / Ceph |`

### Specialist practical exam

- `arista-academy-certification-2026.md:28` — `| Specialist | Specialist practical exam | **295 $** |`
- `network-datacenter-advanced-under-500.md:30` — `| Arista | Specialist practical exam | **295 $** | ✅ performance-based |`

### Sumo Logic

- `observability-vendor-certifications-2026.md:28` — `| Sumo Logic | autres certifications | **150 $** |`
- `observability-vendor-low-cost-2026.md:27` — `| Sumo Logic | Fundamentals certifications | **100 $** | ✅ sous 500 |`
- `observability-vendor-low-cost-2026.md:28` — `| Sumo Logic | Advanced certifications | **150 $** | ✅ sous 500 |`

### VMware VCP-VCF Architect

- `hpe-morpheus-private-cloud-2026.md:216` — `| VMware VCP-VCF Architect | **250 $** |`
- `virtualization-private-cloud-under-500.md:28` — `| VMware VCP-VCF Architect | **250 $** | ❌ | Private cloud architecture |`

## Near-duplicate candidates

| Similarity | Catalogue A | Entry A | Catalogue B | Entry B |
|---:|---|---|---|---|
| — | — | — | — | — |

## Largest catalogues by credential-like table rows

| Rows | Catalogue |
|---:|---|
| 116 | `paid-under-500.md` |
| 64 | `entrepreneurship-startup-business-creation-2026.md` |
| 56 | `paid-over-500.md` |
| 48 | `practical-cyber-under-500.md` |
| 40 | `tools-platforms-under-500.md` |
| 39 | `networking-wireless-ai-infra.md` |
| 37 | `entrepreneur-international-functional-credentials-2026.md` |
| 34 | `audit-finance-project-over-500.md` |
| 30 | `actuarial-accounting-insurance.md` |
| 29 | `entrepreneur-bank-connectivity-sellside-procurement-facilities-fleet-2026.md` |
| 28 | `hr-people-hrtech.md` |
| 27 | `entrepreneur-treasury-cash-pooling-epm-carveout-2026.md` |
| 26 | `network-security-adc-sase-under-500.md` |
| 25 | `business-finance-under-500.md` |
| 21 | `entrepreneur-growth-finance-ecommerce-ip-2026.md` |
| 21 | `public-cloud-multicloud-under-500.md` |
| 21 | `real-estate-property.md` |
| 19 | `cloud-native-platform-engineering-under-500.md` |
| 19 | `entrepreneur-eta-family-ess-export-regulated-2026.md` |
| 19 | `language-certifications.md` |
| 18 | `entrepreneur-france-practical-resources-2026.md` |
| 17 | `ibm-enterprise-security-ai-under-500.md` |
| 17 | `lean-it-lean-management-2026.md` |
| 17 | `network-datacenter-advanced-under-500.md` |
| 17 | `observability-sre-devops-under-500.md` |
| 16 | `compliance-aml-fpa-over-500.md` |
| 16 | `insurance-risk-designations.md` |
| 15 | `ai-engineering-mlops-agents-under-500.md` |
| 15 | `storage-data-protection-under-500.md` |
| 14 | `finance-risk-fraud-over-500.md` |

## Domain row volume

| Rows | Domain |
|---:|---|
| 264 | `entrepreneurship` |
| 252 | `finance-risk` |
| 175 | `general-it` |
| 162 | `business-management` |
| 84 | `governance-grc` |
| 81 | `governance` |
| 78 | `security` |
| 72 | `supply-chain` |
| 69 | `ai-infrastructure` |
| 60 | `network` |
| 56 | `business-soft-skills` |
| 45 | `itsm-middleware` |
| 44 | `hr-people` |
| 40 | `devops-automation` |
| 32 | `storage-backup` |
| 27 | `enterprise-software` |
| 27 | `virtualization` |
| 27 | `observability` |
| 26 | `datacenter-facilities` |
| 25 | `linux` |
| 25 | `pharma-regulatory` |
| 21 | `cloud` |
| 21 | `real-estate` |
| 20 | `esg-sustainability` |
| 20 | `legal` |
| 19 | `kubernetes-platform` |
| 19 | `language` |
| 16 | `industrial-ot` |
| 13 | `sustainability` |
| 12 | `data-database` |
| 10 | `safety-occupational` |
| 9 | `project-management` |
| 8 | `identity-iam` |
| 8 | `mainframe` |
| 5 | `accessibility` |
| 5 | `construction-btp` |
| 4 | `euc-endpoint` |
