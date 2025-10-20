# 🧾 Changelog — Eckohaus Ltd (Original) Archival API

_All notable updates and workflow events for this repository are documented here._

---

## [2025-10-20] — 🔧 Sandbox Workflow Refactor
**Summary:**  
Refined and hardened the **Companies House sandbox verification workflow**  
(`.github/workflows/compliance-check-archive-sandbox.yml`) to improve test safety  
and metadata handling consistency.

### 🧩 Details
- Added validation for secret `CH_API_KEY_ARCHIVE_SANDBOX`  
- Standardised emoji and message formatting across workflow steps  
- Restricted trigger to **manual mode only** (no scheduled runs)  
- Enhanced metadata parsing and log consistency  
- Improved ledger append behaviour for clearer commit trails  

---

### 🪶 Co-author Traceability
```text
Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>
```

✅ **Status:** Complete.  
The sandbox workflow is now validated, traceable, and production-ready for final  
transition toward live archival verification.

### 🔜 Next Step

Configure and test **`compliance-check-archive.yml`**  
using **`CH_API_KEY_ARCHIVE`** for the quarterly schedule  
(**January / April / July / October**).

---

## [2025-10-20] — 🚀 Live Archival API Workflow Activated  

**Summary:**  
Introduced and deployed the **live quarterly Companies House verification workflow**  
for **Eckohaus Ltd (Original, 2013 – 2021)** archival record continuity.  

### 🧩 Details  
- Added `.github/workflows/compliance-check-archive-live.yml`  
- Scheduled to execute **quarterly (Jan / Apr / Jul / Oct)** at **09:00 UTC**  
- Uses live key `CH_API_KEY_ARCHIVE` for authenticated API access  
- Automatically archives responses under `data/archive_responses/`  
- Appends verification summaries to `orchestration-ledger.md`  
- Completes transition from sandbox validation to live operational mode
  
---

### 🪶 Co-author Traceability
```text
Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>
```

---

<!--
## [2026-01-01] — 🗓️ First Quarterly Archive Verification
**Summary:**  
Successfully executed first scheduled quarterly Companies House archival verification.  

### 🧩 Details
- Queried CH API using `CH_API_KEY_ARCHIVE`  
- Response archived at `data/archive_responses/response_archive_20260101_0900.json`  
- Ledger auto-updated and committed (`commit abc1234`)  

### 🪶 Co-author Traceability
```text
Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>
```
-->
