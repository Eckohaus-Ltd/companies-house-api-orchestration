# 🧾 CHANGELOG — Eckohaus Ltd (Original) Archive API

_© 2025 Eckohaus Ltd — Internal Research and Development Record_  
_This changelog documents the evolution of the archival API repository, including metadata, workflows, and integration setup._

---

## [2025-10-20] — Initial Archive API Setup

### 🗂️ Overview
- Created **Eckohaus-Ltd-Archive-API** repository for preservation of the original  
  Eckohaus Ltd (2013 – 2021) company lineage and Companies House data.
- Established **archival configuration**, **workflows**, and **sandbox** environment.

### 📦 Additions
- Added `config/metadata.yml` for archival entity metadata (`08573397`).
- Added `.github/workflows/compliance-check-archive.yml` — quarterly verification workflow.
- Added `.github/workflows/compliance-check-archive-sandbox.yml` — mock testing workflow.
- Added `orchestration-ledger.md` — audit log for archive verification events.
- Added `CHANGELOG.md` — version tracking for archival repository setup.

### 🔧 Environment
- Sandbox API Key: `CH_API_KEY_ARCHIVE_SANDBOX`
- Live API Key: `CH_API_KEY_ARCHIVE`
- Archival Mode: **Read-only / Static Data Verification**
- Next scheduled verification: **January 2026**

---

### 🪶 Co-author Traceability
```text
Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>
```

---

Last synchronised via GitHub Actions on 2025-10-20.

---
