# 🗂️ Eckohaus Orchestration Ledger (Archive Edition)
_© 2025 Eckohaus Ltd — Internal Research & Development Record_

---

## 📘 Overview
This ledger tracks archival verification and metadata continuity for  
**Eckohaus Ltd (Original, 2013–2021)** — the pre-restructure entity forming  
the historical foundation of the Eckohaus Orchestration framework.

Each entry below corresponds to a structured archival event recorded  
via GitHub Actions or manual verification runs.

---

## 📅 Event Log

| Date (UTC) | Event Type | Description | Notes |
|-------------|-------------|-------------|-------|
| 2025-10-20 | Archive Initialisation | Created archival metadata configuration (`config/metadata.yml`). | Establishes static dataset for Eckohaus Ltd (Company No. 08573397). |
| 2025-10-20 | Workflow Setup | Added quarterly verification workflow (`.github/workflows/compliance-check-archive.yml`). | Scheduled for January, April, July, October runs. |
| 2025-10-20 | Sandbox Workflow Setup | Added sandbox archival verification workflow (`.github/workflows/compliance-check-archive-sandbox.yml`). | Uses secret `CH_API_KEY_ARCHIVE_SANDBOX` for mock API calls and saves responses to `data/sandbox_responses/`. |
| 2025-10-20 03:35 UTC | Live Archival Workflow Activation | `.github/workflows/compliance-check-archive-live.yml` | CH Live API |
| — | — | — | — |

---

## ⚙️ Operational Context
- Repository operates in **read-only archival mode**.  
- API environment: `archive` using secret `CH_API_KEY_ARCHIVE`.  
- Sandbox key: `CH_API_KEY_ARCHIVE_SANDBOX` (mock testing).  
- Next scheduled live verification: **January 2026**.  
- All archival responses will be stored under `/data/archive_responses/` and `/data/sandbox_responses/`.  

---

### 🪶 Co-author Traceability
```text
Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>
```

---

_Last synchronised via GitHub Actions on 2025-10-20._


| 2025-10-20 03:03 UTC | Quarterly archival verification | data/archive_responses/response_archive_20251020_0303.json | CH Live API |
| 2026-01-01 09:23 UTC | Quarterly archival verification | data/archive_responses/response_archive_20260101_0923.json | CH Live API |
| 2026-02-17 06:46 UTC | Quarterly archival verification | data/archive_responses/response_archive_20260217_0646.json | CH Live API |
| 2026-02-17 06:47 UTC | Sandbox archival verification | data/sandbox_responses/response_sandbox_20260217_0647.json | CH Sandbox API |
| 2026-04-01 10:04 UTC | Quarterly archival verification | data/archive_responses/response_archive_20260401_1004.json | CH Live API |
