# 🧾 Changelog — Eckohaus Ltd (Original) Archival API

_All notable updates and workflow events for this repository are documented here._

---

## [2025-10-20] — ✅ Sandbox API Verification Success
**Summary:**  
First successful end-to-end run of the Companies House **sandbox integration** for  
**Eckohaus Ltd (Original, 2013–2021)** archival reference.

### 🧩 Details
- Confirmed sandbox key authentication (`CH_API_KEY_ARCHIVE_SANDBOX`)  
- Response archived under  
  `data/sandbox_responses/response_sandbox_20251020_0204.json`  
- Ledger auto-updated and committed (`commit a798f02`)  
- Verified orchestration structure and secret injection  
- Repository confirmed ready for quarterly **live archival** workflow runs

---

### 🪶 Co-author Traceability
```text
Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>
```

### 🔜 Next Step

Configure and test **`compliance-check-archive.yml`**  
using **`CH_API_KEY_ARCHIVE`** for the quarterly schedule  
(**January / April / July / October**).
