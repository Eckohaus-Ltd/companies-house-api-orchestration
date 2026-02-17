# 🧭 Eckohaus Orchestration Pilot

_© 2025 Eckohaus Ltd — Internal Research & Development Repository_  
_This repository underpins the automated compliance orchestration system integrating Eckohaus Ltd’s UK filings (Companies House, HMRC) with internal workflow automation._

---

## 🧩 Overview

The **Eckohaus Orchestration Pilot** is an internal proof-of-concept that connects Companies House data with automated audit trails and reminder systems.

It operates across **test**, **live**, and **weekly** workflows, using GitHub Actions to:
- Query Companies House APIs
- Archive and version responses as JSON
- Append entries to a persistent orchestration ledger
- Prepare for future event-sequenced automation (accounts & confirmation filings)

---

## 📂 Repository Layout (as of October 2025)
```
Eckohaus-Orchestration-Pilot/
│
├── README.md
│   → Main project overview and licence notice.
│
├── orchestration-ledger.md
│   → Event-sequenced compliance log (pre-filing, filing, post-filing).
│
├── CHANGELOG.md
│   → Versioned changelog following Keep a Changelog 1.1.0.
│
├── .github/
│   └── workflows/
│       ├── compliance-check.yml
│       ├── compliance-check-live.yml
│       └── compliance-check-weekly.yml
│       → Automated workflows for Companies House data checks.
│
├── config/
│   └── metadata.yml
│   → Company and jurisdictional metadata (UK ↔ Indonesia).
│
└── data/
├── responses/
└── sandbox_responses/
→ Archived Companies House JSON responses (live & test).
```
---

## ⚙️ Current Workflows

| Workflow | Purpose | Status |
|-----------|----------|--------|
| `compliance-check.yml` | Sandbox test workflow for CH API validation | ✅ Active |
| `compliance-check-live.yml` | Live CH data retrieval & audit logging | 🧩 In propagation stage |
| `compliance-check-weekly.yml` | Scheduled production cycle (Mon 10:00 UTC) | ⏸ Development phase |
| `codeql-analysis.yml` | Security scanning with CodeQL (push on main) | ✅ Active |

Each workflow interacts with `config/metadata.yml` for company details and API environment parameters.  
Live responses are archived in `/data/responses/` and recorded in `orchestration-ledger.md`.

### Artifact Analysis & Reporting

All workflows now include comprehensive artifact generation for line-by-line analysis:

- **Repository Structure**: Captured at each workflow execution
- **Branch & Commit Context**: Full git metadata integration
- **Workflow Metadata**: Execution details in JSON format
- **Artifact Retention**: 90 days for historical analysis

**Analysis Tools** (in `.github/scripts/`):
- `artifact-analyzer.py` - Line-by-line artifact analysis
- `comparative-analyzer.py` - Cross-workflow comparative analysis integrating CodeQL with compliance data

**Documentation**:
- [Artifact Analysis Guide](docs/ARTIFACT_ANALYSIS_GUIDE.md) - Comprehensive usage guide
- [Scripts README](.github/scripts/README.md) - Technical documentation for analysis scripts

---

## 🪶 Co-author Traceability  
```
Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator  <info@eckohaus.co.uk>
```
---

### 📜 Licence
This project is maintained under the **Eckohaus Ltd Private Use Licence**.  
Reproduction or external redistribution is not permitted without written consent.  

For further enquiries: [info@eckohaus.co.uk](mailto:info@eckohaus.co.uk)

---

_Last synchronised via GitHub Actions — October 2025_
