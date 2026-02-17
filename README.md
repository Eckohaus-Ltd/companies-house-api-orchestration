# 🗂️ Eckohaus Ltd (Original) — Archival API (2015 – 2021)

_© 2025 Eckohaus Ltd — Internal Research and Development Record_

---

### 📖 Repository Purpose
This repository serves as an **archival API reference** for the **original Eckohaus Ltd (2015 – 2021)**.  
It preserves key metadata, compliance records, and Companies House lineage prior to the company’s restructuring and relaunch in 2024.

All data in this archive is **static** and used only for documentation and research continuity within the **Eckohaus Orchestration Pilot** and future organisational APIs.

---

### 🧩 Repository Structure
```text
Eckohaus-Ltd-Archive-API/
├── README.md
│   → Repository overview and licence notice.
│
├── config/
│   └── metadata.yml
│   → Core archival metadata (Company Number, dates, jurisdiction info).
│
├── .github/
│   └── workflows/
│       └── compliance-check-archive.yml
│       → Static metadata check workflow.
│
└── data/
└── sample_archive_response.json
→ Placeholder for legacy Companies House filings or JSON snapshots.
```
---

### 🧭 Operational Notes
- This repository functions in **archival mode** only — no live API calls.  
- Historical Company Number reference (2015 – 2021): `08573397`.  
- Data represents the **first Eckohaus Ltd** entity prior to restructuring.  
- When integrated under a future **Eckohaus Organization**, this archive will serve as the **root node** of the Eckohaus lineage map.
- For detailed workflow analysis, see [workflow-log-analysis.md](workflow-log-analysis.md).

---

### 🧾 Metadata Reference
| Field | Value |
|-------|--------|
| Repository | `Eckohaus-Ltd-Archive-API` |
| Jurisdiction | United Kingdom |
| Status | Archived / Read-only |
| Maintainer | Corvin Nehal Dhali |
| API Key Ref | `CH_API_KEY_ARCHIVE` |
| Integration | Internal use only |

---

### 🪶 Co-author Traceability
```text
Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator  <info@eckohaus.co.uk>
```
---

### 🗓️ Next Steps
- [ ] Populate `data/` with archived Companies House records (PDF or JSON).  
- [ ] Cross-reference metadata with 2024 Eckohaus Ltd (API v2).  
- [ ] Add organizational link once Eckohaus Organization is registered on GitHub.

---

_Licensed for internal use only under the Eckohaus Private Use Licence._  
_Contact: info@eckohaus.co.uk_
