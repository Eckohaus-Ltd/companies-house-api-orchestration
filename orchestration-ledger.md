# 📘 Eckohaus Orchestration Ledger  

_© 2025 Eckohaus Ltd — Internal Research & Development Record_  

This document serves as a **human-readable orchestration ledger** for the **Eckohaus Orchestration Pilot**,  
tracking milestone events, workflow runs, and compliance checks related to the Companies House API integration.  

---

## 🧭 Ledger Overview  

Each entry corresponds to a structured orchestration or compliance event.  
These include:  
- **Pre-filing** checks (account deadlines, confirmation statements)  
- **Filing** events (submissions, reminders, or reconciliations)  
- **Post-filing** validations and API-based ledger updates  

---

## 📅 Event Log  

| Date (UTC) | Event Type | Description | Notes |
|-------------|-------------|-------------|-------|
| 2025-10-19 | Initialisation | Created repository structure and metadata. | Workflows established for test and live API integrations. |
| 2025-10-19 | API Test (Sandbox) | Successful sandbox query. | Returned “Resource not found” as expected (mock response). |
| 2025-10-19 | API Live (First Run) | First live Companies House query executed. | Returned “Invalid Authorization” during key verification. |
| 2025-10-19 | API Live (Retry Scheduled) | 30-minute retry for CH API propagation. | Awaiting Companies House endpoint response (UK weekday hours). |

---

## 🗓️ Pending Orchestration Schedule  

| Target Period | Scope | Notes |
|----------------|--------|-------|
| December 2025 | Pre-filing cycle | Initial live data pull and company status validation before January 2026 deadlines. |
| Q1 2026 | Filing + confirmation events | Sync Companies House filings with HMRC PAYE + pension reconciliation. |
| Mid-2026 | API integration review | Validate CH → internal ledger data consistency for next automation phase. |

> _All future schedule entries are provisional until confirmed against Companies House and HMRC filing data._  

---

## ⚙️ Automation Metadata  

| Field | Value |
|-------|--------|
| Repository | `Eckohaus-Orchestration-Pilot` |
| Environment | Live + Sandbox |
| Primary API Key Ref | `CH_API_KEY_LIVE` |
| Sandbox API Key Ref | `CH_API_KEY` |
| Archive Directory | `/data/responses/` |
| Maintainer | Corvin Nehal Dhali |
| Audit Reviewer | System Operator (`wanda@openai.com`) |
| Status | Active (Development-linked orchestration) |

---

### 🪶 Co-author Traceability
```
Co-authored-by: system operator <wanda@openai.com>  
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>
```
---

### 🗂️ Next Steps  
- [ ] Confirm first successful live API response after Monday retry window.  
- [ ] Enable weekly cron workflow once propagation verified.  
- [ ] Extend ledger schema to include filing type (Accounts / Confirmation Statement) in v2.  
- [ ] Automate JSON parsing for CH → ledger sync summaries.  

---

📄 _Maintained internally under the [Private Use Licence](./LICENSE.md)_  
📧 _Contact: info@eckohaus.blog_  
_Last synchronised via GitHub Actions on 2025-10-19._





| 2025-10-20 03:17 UTC | Sandbox CH test check | Archived data/sandbox_responses/response_sandbox_20251020_0317.json | CH sandbox API |
| 2025-10-20 03:20 UTC | Weekly CH live check | Archived data/responses/response_live_20251020_0320.json | CH live API |
| 2025-10-20 05:49 UTC | Weekly CH live check | Archived data/responses/response_live_20251020_0549.json | CH live API |
| 2025-10-20 10:41 UTC | Weekly CH live check | Archived data/responses/response_live_20251020_1041.json | CH live API |
| 2025-10-23 01:06 UTC | Weekly CH live check | Archived data/responses/response_live_20251023_0106.json | CH live API |
| 2025-10-27 10:43 UTC | Weekly CH live check | Archived data/responses/response_live_20251027_1043.json | CH live API |
| 2025-10-30 23:58 UTC | Sandbox CH test check | Archived data/sandbox_responses/response_sandbox_20251030_2358.json | CH sandbox API |
| 2025-10-31 00:06 UTC | Sandbox CH test check | Archived data/sandbox_responses/response_sandbox_20251031_0006.json | CH sandbox API |
| 2025-10-31 00:13 UTC | Sandbox CH test check | Archived data/sandbox_responses/response_sandbox_20251031_0013.json | CH sandbox API |
| 2025-10-31 00:18 UTC | Sandbox CH test check | Archived data/sandbox_responses/response_sandbox_20251031_0018.json | CH sandbox API |
| 2025-10-31 00:29 UTC | Live CH API check | Archived data/responses/response_live_20251031_0029.json | CH live API |
| 2025-10-31 00:40 UTC | Live CH API check | Archived data/responses/response_live_20251031_0040.json | CH live API |
| 2025-10-31 00:48 UTC | Weekly CH live check | Archived data/responses/response_weekly_20251031_0048.json | CH live API |
| 2025-11-03 10:13 UTC | Live CH API check | Archived data/responses/response_live_20251103_1013.json | CH live API |
| 2025-11-03 10:28 UTC | Weekly CH live check | Archived data/responses/response_weekly_20251103_1028.json | CH live API |
| 2025-11-10 10:12 UTC | Live CH API check | Archived data/responses/response_live_20251110_1012.json | CH live API |
| 2025-11-10 10:28 UTC | Weekly CH live check | Archived data/responses/response_weekly_20251110_1028.json | CH live API |
| 2025-11-17 10:12 UTC | Live CH API check | Archived data/responses/response_live_20251117_1012.json | CH live API |
| 2025-11-17 10:28 UTC | Weekly CH live check | Archived data/responses/response_weekly_20251117_1028.json | CH live API |
| 2025-11-24 10:12 UTC | Live CH API check | Archived data/responses/response_live_20251124_1012.json | CH live API |
| 2025-11-24 10:29 UTC | Weekly CH live check | Archived data/responses/response_weekly_20251124_1029.json | CH live API |
| 2025-12-01 10:13 UTC | Live CH API check | Archived data/responses/response_live_20251201_1013.json | CH live API |
| 2025-12-01 10:30 UTC | Weekly CH live check | Archived data/responses/response_weekly_20251201_1030.json | CH live API |
| 2025-12-08 10:12 UTC | Live CH API check | Archived data/responses/response_live_20251208_1012.json | CH live API |
| 2025-12-08 10:29 UTC | Weekly CH live check | Archived data/responses/response_weekly_20251208_1029.json | CH live API |
| 2025-12-15 10:15 UTC | Live CH API check | Archived data/responses/response_live_20251215_1015.json | CH live API |
| 2025-12-15 10:33 UTC | Weekly CH live check | Archived data/responses/response_weekly_20251215_1033.json | CH live API |
| 2025-12-22 10:12 UTC | Live CH API check | Archived data/responses/response_live_20251222_1012.json | CH live API |
| 2025-12-22 10:28 UTC | Weekly CH live check | Archived data/responses/response_weekly_20251222_1028.json | CH live API |
| 2025-12-29 10:12 UTC | Live CH API check | Archived data/responses/response_live_20251229_1012.json | CH live API |
