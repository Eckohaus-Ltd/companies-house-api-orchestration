# Eckohaus Orchestration Pilot - Scripts

This directory contains automation and analysis scripts for the Eckohaus Orchestration Pilot repository.

---

## 📜 Available Scripts

### `analyze_workflow_logs.py`

**Purpose**: Perform line-by-line analysis of GitHub Actions workflow logs, integrating them with the repository folder and file structure.

**Analyzes the following workflows**:
1. CodeQL Analysis (push on main)
2. Compliance Check (Companies House - Live)
3. Compliance Check (Companies House - Sandbox)
4. Compliance Check (Companies House - Weekly)

**Features**:
- ✅ Line-by-line log parsing
- ✅ Repository structure integration
- ✅ Error and warning detection
- ✅ API call tracking
- ✅ File operation monitoring
- ✅ Security findings analysis (CodeQL)
- ✅ Markdown report generation

**Usage**:
```bash
# Run from repository root
python3 scripts/analyze_workflow_logs.py

# Or make it executable and run directly
chmod +x scripts/analyze_workflow_logs.py
./scripts/analyze_workflow_logs.py
```

**Output**:
- Generates `workflow-log-analysis.md` in the repository root
- Console output showing repository structure summary
- Detailed analysis of each workflow execution

**Integration Points**:
- `.github/workflows/` - Workflow definitions
- `config/metadata.yml` - Configuration metadata
- `data/responses/` - Live CH API response archives  
- `data/sandbox_responses/` - Sandbox CH API response archives
- `orchestration-ledger.md` - Event log tracking

---

## 🔧 Requirements

- Python 3.8 or higher
- Access to repository file structure
- (Optional) GitHub CLI (`gh`) for live log fetching
- (Optional) GitHub Personal Access Token for API access

---

## 📊 Analysis Capabilities

### Compliance Workflow Analysis
The script analyzes compliance workflow logs and extracts:
- **Step Tracking**: Identifies all workflow steps and their boundaries
- **Error Detection**: Flags lines containing errors or failures
- **Warning Detection**: Identifies warning messages
- **File Operations**: Tracks all file system operations (mkdir, cp, mv, etc.)
- **API Calls**: Detects and logs Companies House API interactions
- **Metadata Operations**: Tracks `config/metadata.yml` loading and parsing

### CodeQL Workflow Analysis
For CodeQL workflows, the script additionally analyzes:
- **Database Operations**: CodeQL database creation and analysis steps
- **Security Findings**: Vulnerabilities, CWE references, severity levels
- **Scan Results**: Query execution results and findings count
- **Code Analysis**: Language-specific scanning operations

---

## 🗂️ Repository Structure Integration

The analyzer maps workflow operations to the repository structure:

```
Eckohaus-Orchestration-Pilot/
├── .github/workflows/          # Workflow definitions (analyzed)
├── config/metadata.yml         # Configuration (tracked in logs)
├── data/
│   ├── responses/             # Live API responses (file ops tracked)
│   └── sandbox_responses/     # Sandbox API responses (file ops tracked)
├── orchestration-ledger.md    # Event log (referenced in analysis)
└── scripts/                   # This directory
    └── analyze_workflow_logs.py
```

---

## 📈 Sample Analysis Output

```markdown
# Eckohaus Orchestration Pilot - Workflow Log Analysis Report

**Generated**: 2025-11-11 08:00 UTC

---

## Repository Structure Integration

### Workflows
- `.github/workflows/compliance-check-live.yml`
- `.github/workflows/compliance-check.yml`
- `.github/workflows/compliance-check-weekly.yml`

### Configuration
- `config/metadata.yml`

### Data Archives
- Live responses: 6 files
- Sandbox responses: 5 files

---

## Workflow Analysis Results

### COMPLIANCE_LIVE Workflow

**Lines Analyzed**: 145
**Errors**: 0
**Warnings**: 1
**API Calls**: 2
**File Operations**: 5

#### File Operations (Repo Structure Integration)
- Line 32: metadata_load
- Line 78: Response archived at data/responses/response_live_20251110_1012.json
- Line 89: Ledger updated at orchestration-ledger.md

#### Companies House API Interactions
- Line 65: API call detected
```

---

## 🚀 Future Enhancements

Planned improvements for the analysis tool:

- [ ] Direct GitHub API integration for live log fetching
- [ ] Workflow run comparison and diff analysis
- [ ] Trend analysis across multiple runs
- [ ] Alert generation for errors and anomalies
- [ ] Integration with notification systems (email, Slack)
- [ ] JSON/CSV export options
- [ ] Custom filtering and search capabilities
- [ ] Visualization of workflow execution timelines

---

## 📝 Notes

- The script currently generates sample analyses for demonstration
- For production use with live logs, implement GitHub API token authentication
- Log data is parsed line-by-line to ensure comprehensive coverage
- All file operations are mapped to the actual repository structure
- Report generation is optimized for readability in markdown viewers

---

## 🪶 Co-author Traceability

```
Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>
```

---

**Last Updated**: November 2025  
**Maintained by**: Eckohaus Ltd
