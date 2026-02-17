# Workflow Log Analysis Integration Guide

**Eckohaus Orchestration Pilot - Repository Structure Integration**

This document provides a comprehensive guide for running line-by-line analysis of GitHub Actions workflow logs integrated with the repository folder and file structure.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Workflows Covered](#workflows-covered)
3. [Installation](#installation)
4. [Basic Usage](#basic-usage)
5. [Advanced Usage](#advanced-usage)
6. [Output Examples](#output-examples)
7. [Repository Structure Mapping](#repository-structure-mapping)
8. [Troubleshooting](#troubleshooting)

---

## Overview

The Workflow Log Analyzer performs detailed line-by-line analysis of GitHub Actions workflow execution logs, extracting key information and mapping it to the repository's folder and file structure.

**Analyzed Workflows**:
1. CodeQL Analysis (push on main)
2. Compliance Check (Companies House - Live)
3. Compliance Check (Companies House - Sandbox)
4. Compliance Check (Companies House - Weekly)

---

## Workflows Covered

### 1. CodeQL Analysis (push on main)

**File**: `.github/workflows/codeql-analysis.yml`  
**Trigger**: Push to main branch  
**Purpose**: Security scanning and vulnerability detection

**Analyzed Elements**:
- Database creation and analysis operations
- Security findings (vulnerabilities, CWE references)
- Query execution results
- Code analysis metrics

### 2. Compliance Check (Companies House - Live)

**File**: `.github/workflows/compliance-check-live.yml`  
**Trigger**: Schedule (Monday 10:00 UTC) / Manual dispatch  
**Purpose**: Live Companies House API data retrieval

**Analyzed Elements**:
- Metadata loading from `config/metadata.yml`
- Companies House API calls to live endpoint
- Response archival to `data/responses/`
- Ledger updates in `orchestration-ledger.md`
- Error handling and retry logic

### 3. Compliance Check (Companies House - Sandbox)

**File**: `.github/workflows/compliance-check.yml`  
**Trigger**: Manual dispatch  
**Purpose**: Sandbox testing of Companies House API integration

**Analyzed Elements**:
- Sandbox API endpoint interactions
- Test data handling
- Response archival to `data/sandbox_responses/`
- Configuration validation

### 4. Compliance Check (Companies House - Weekly)

**File**: `.github/workflows/compliance-check-weekly.yml`  
**Trigger**: Schedule (Monday 10:00 UTC)  
**Purpose**: Weekly compliance verification

**Analyzed Elements**:
- Similar to live workflow
- Weekly execution pattern tracking
- Long-term trend data collection

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Git repository clone
- (Optional) GitHub CLI for live log fetching

### Setup

```bash
# Clone the repository
git clone https://github.com/Eckohaus-Ltd/Eckohaus-Orchestration-Pilot.git
cd Eckohaus-Orchestration-Pilot

# Make the script executable
chmod +x scripts/analyze_workflow_logs.py

# Verify Python version
python3 --version
```

---

## Basic Usage

### Running the Analyzer

```bash
# From repository root
python3 scripts/analyze_workflow_logs.py
```

### Output

The analyzer generates:
1. **Console Output**: Summary of repository structure and analysis progress
2. **Markdown Report**: `workflow-log-analysis.md` in repository root

### Example Console Output

```
🔍 Eckohaus Orchestration Pilot - Workflow Log Analyzer
============================================================

📁 Repository Structure:
   Workflows: 3
   Config files: 1
   Live responses: 6
   Sandbox responses: 5
✅ Report saved to: /path/to/workflow-log-analysis.md

✅ Analysis complete!
```

---

## Advanced Usage

### Fetching Live Logs (GitHub API)

To analyze real workflow logs, you can extend the script with GitHub API integration:

```python
# Example: Fetch logs using GitHub CLI
import subprocess

def fetch_workflow_logs(workflow_id: str) -> str:
    """Fetch logs from GitHub Actions using gh CLI."""
    cmd = f"gh run view {workflow_id} --log"
    result = subprocess.run(
        cmd.split(),
        capture_output=True,
        text=True
    )
    return result.stdout
```

### Custom Analysis

You can customize the analysis by modifying the analyzer class:

```python
# In your script
from scripts.analyze_workflow_logs import WorkflowLogAnalyzer

analyzer = WorkflowLogAnalyzer()

# Analyze custom log content
custom_log = """
Your workflow log content here
"""

analysis = analyzer.analyze_compliance_workflow_log(
    custom_log,
    'compliance_live'
)

# Generate report
report = analyzer.generate_integrated_report([analysis])
print(report)
```

---

## Output Examples

### Sample Analysis Report Structure

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
- Line 32: metadata_load from config/metadata.yml
- Line 78: Response archived at data/responses/response_live_20251110_1012.json
- Line 89: Ledger updated at orchestration-ledger.md

#### Companies House API Interactions
- Line 65: API call to live endpoint
- Line 72: HTTP status: 200
```

---

## Repository Structure Mapping

The analyzer integrates workflow logs with the repository structure:

```
Eckohaus-Orchestration-Pilot/
│
├── .github/workflows/
│   ├── compliance-check.yml           ← Sandbox workflow
│   ├── compliance-check-live.yml      ← Live workflow
│   ├── compliance-check-weekly.yml    ← Weekly workflow
│   └── codeql-analysis.yml            ← Security scanning
│
├── config/
│   └── metadata.yml                   ← Tracked in log analysis
│                                         (company details, API config)
│
├── data/
│   ├── responses/                     ← File ops tracked
│   │   ├── response_live_20251110_1012.json
│   │   └── ...
│   └── sandbox_responses/             ← File ops tracked
│       ├── response_sandbox_20251020_0317.json
│       └── ...
│
├── orchestration-ledger.md            ← Updates tracked
│
├── scripts/
│   ├── analyze_workflow_logs.py       ← This tool
│   └── README.md                      ← Tool documentation
│
└── workflow-log-analysis.md           ← Generated report
```

### Tracked Operations

| Operation Type | Example | Mapped To |
|----------------|---------|-----------|
| Config Load | `Loading metadata from config/metadata.yml` | `config/metadata.yml` |
| API Call | `Querying Companies House LIVE API` | External API |
| File Archive | `Response archived at data/responses/` | `data/responses/*.json` |
| Ledger Update | `Ledger updated` | `orchestration-ledger.md` |
| Error | `❌ No API key detected` | Error log |

---

## Troubleshooting

### Issue: Script not finding repository structure

**Solution**: Ensure you're running from the repository root:
```bash
cd /path/to/Eckohaus-Orchestration-Pilot
python3 scripts/analyze_workflow_logs.py
```

### Issue: No workflows found

**Solution**: Verify `.github/workflows/` directory exists:
```bash
ls -la .github/workflows/
```

### Issue: Unable to fetch live logs

**Solution**: For live log fetching, install and configure GitHub CLI:
```bash
# Install GitHub CLI
brew install gh  # macOS
# or
sudo apt install gh  # Linux

# Authenticate
gh auth login
```

### Issue: Python version error

**Solution**: Ensure Python 3.8+:
```bash
python3 --version
# Should show 3.8.0 or higher
```

---

## 🔮 Future Enhancements

Planned improvements:

- [ ] Real-time log streaming and analysis
- [ ] GitHub API token integration for automated log fetching
- [ ] Workflow run comparison (diff between runs)
- [ ] Trend analysis (multiple runs over time)
- [ ] Alert generation for critical errors
- [ ] Integration with notification systems
- [ ] Export to JSON/CSV formats
- [ ] Web dashboard for visualization

---

## 📞 Support

For questions or issues:
- **Email**: info@eckohaus.co.uk
- **Repository**: https://github.com/Eckohaus-Ltd/Eckohaus-Orchestration-Pilot

---

## 🪶 Co-author Traceability

```
Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>
```

---

**Last Updated**: November 2025  
**Version**: 1.0.0  
**Maintained by**: Eckohaus Ltd
