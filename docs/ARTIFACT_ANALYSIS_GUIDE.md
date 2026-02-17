# Artifact Analysis Guide

## Overview

This guide explains how to use the workflow artifact analysis capabilities in the Eckohaus Orchestration Pilot to perform line-by-line analysis and comparative analysis across CodeQL security scans and compliance checks.

## What Gets Analyzed?

The analysis system examines artifacts from four key workflows:

1. **CodeQL Analysis** - Security scanning on push to main
2. **Compliance Check (Weekly)** - Weekly Companies House live checks
3. **Compliance Check (Live)** - On-demand Companies House live checks
4. **Compliance Check (Sandbox)** - Test environment compliance checks

## Artifact Contents

Each workflow run generates artifacts containing:

### All Workflows
- `workflow-metadata.json` - Execution metadata (run ID, timestamp, branch, commit, etc.)
- `repository-structure.txt` - Repository structure snapshot including:
  - File and directory tree
  - Branch information
  - Current commit details
  - File statistics

### CodeQL Workflow Only
- `codeql-summary.txt` - Summary of security findings
- `*.sarif` - SARIF format security results (detailed)

### Compliance Workflows Only
- `response_*.json` - Companies House API responses
- `status_code.txt` - HTTP status codes from API calls

## How to Download Artifacts

### Via GitHub Web UI

1. Navigate to the **Actions** tab in the repository
2. Select the workflow run you want to analyze
3. Scroll to the **Artifacts** section at the bottom
4. Click on the artifact name to download (e.g., `codeql-analysis-javascript-123`)
5. Extract the downloaded ZIP file

### Via GitHub CLI

```bash
# List artifacts for a specific run
gh run view <run-id> --repo Eckohaus-Ltd/Eckohaus-Orchestration-Pilot

# Download artifact
gh run download <run-id> --repo Eckohaus-Ltd/Eckohaus-Orchestration-Pilot
```

## Running Line-by-Line Analysis

### Basic Usage

```bash
# Navigate to your local clone of the repository
cd /path/to/Eckohaus-Orchestration-Pilot

# Run the analyzer on downloaded artifacts
python3 .github/scripts/artifact-analyzer.py /path/to/downloaded-artifacts
```

### Output

The analyzer generates `analysis-report.md` containing:
- Workflow execution summary
- CodeQL security findings (if any)
- Compliance check results
- Comparative analysis across workflows
- Repository context and structure

### Example

```bash
# Download artifacts to a local directory
mkdir -p ~/workflow-artifacts
cd ~/workflow-artifacts
# (Extract your downloaded artifact ZIPs here)

# Run the analysis
python3 ~/Eckohaus-Orchestration-Pilot/.github/scripts/artifact-analyzer.py .

# View the report
cat analysis-report.md
```

## Running Comparative Analysis

### Basic Usage

```bash
# Run comparative analysis
python3 .github/scripts/comparative-analyzer.py /path/to/artifacts

# Or specify custom output location
python3 .github/scripts/comparative-analyzer.py /path/to/artifacts \
    --output /path/to/custom-report.md
```

### Output

The comparative analyzer generates `comparative-analysis.md` containing:

- **Executive Summary** - High-level statistics across all workflows
- **Workflow Execution Breakdown** - Per-workflow execution counts and timestamps
- **Execution Timeline** - Chronological view of all workflow runs
- **CodeQL Security Analysis** - Aggregated security findings
- **Compliance Check Analysis** - Detailed compliance information
- **Repository Structure & Context** - Branch and commit coverage
- **Integration Analysis** - CodeQL + Compliance correlation
- **Cross-Workflow Insights** - Distribution and activity patterns
- **Compilation & Build Context** - Environment and build information
- **Recommendations** - Automated suggestions based on findings

## Analysis Use Cases

### 1. Security Audit

**Goal:** Review all CodeQL security findings

```bash
# Download all CodeQL artifacts from recent runs
# Run comparative analysis
python3 .github/scripts/comparative-analyzer.py ./codeql-artifacts

# Check the CodeQL Security Analysis section
grep -A 20 "## CodeQL Security Analysis" comparative-analysis.md
```

### 2. Compliance Tracking

**Goal:** Track Companies House status over time

```bash
# Download compliance artifacts from multiple weeks
# Run comparative analysis
python3 .github/scripts/comparative-analyzer.py ./compliance-artifacts

# View compliance status timeline
grep -A 30 "## Compliance Check Analysis" comparative-analysis.md
```

### 3. Integrated Review

**Goal:** See how security and compliance align

```bash
# Download artifacts from all workflow types
# Run comparative analysis
python3 .github/scripts/comparative-analyzer.py ./all-artifacts

# Review the integration analysis section
grep -A 20 "## Integration Analysis" comparative-analysis.md
```

## Tips for Best Results

1. **Download Multiple Runs**: Comparative analysis works best with data from multiple workflow executions
2. **Include All Workflow Types**: Mix CodeQL and compliance artifacts for comprehensive insights
3. **Regular Analysis**: Run analysis weekly to track trends over time
4. **Archive Reports**: Keep historical analysis reports for long-term trending
5. **Cross-Reference**: Use both analyzer tools for different perspectives

## Support

For questions or issues:
- **Email**: info@eckohaus.co.uk
- **Repository**: Check `.github/scripts/README.md` for technical details

---

*Eckohaus Orchestration Pilot - Artifact Analysis System*  
*© 2025 Eckohaus Ltd - Internal Use Only*
