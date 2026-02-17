# Workflow Artifact Analysis Scripts

This directory contains analysis scripts for the Eckohaus Orchestration Pilot workflow artifacts.

## Scripts

### `artifact-analyzer.py`

Performs line-by-line analysis of workflow artifacts and generates comprehensive reports.

**Features:**
- Analyzes all workflow artifacts (CodeQL, Compliance checks)
- Extracts metadata from workflow executions
- Parses repository structure snapshots
- Identifies CodeQL security findings
- Analyzes Companies House compliance responses
- Generates detailed analysis reports

**Usage:**
```bash
python3 artifact-analyzer.py <artifact-directory>
```

**Example:**
```bash
# Download artifacts from GitHub Actions
# Then analyze them
python3 artifact-analyzer.py ./downloaded-artifacts

# Report will be saved to: ./downloaded-artifacts/analysis-report.md
```

### `comparative-analyzer.py`

Performs comparative analysis integrating CodeQL security findings with compliance check workflows.

**Features:**
- Cross-workflow comparative analysis
- Timeline-based execution tracking
- CodeQL and compliance correlation
- Repository structure and branch context integration
- Compilation and build environment analysis
- Detailed recommendations based on findings

**Usage:**
```bash
python3 comparative-analyzer.py <artifacts-dir> [--output <report-file>]
```

**Example:**
```bash
# Basic usage
python3 comparative-analyzer.py ./downloaded-artifacts

# Specify output file
python3 comparative-analyzer.py ./downloaded-artifacts --output custom-report.md

# Report will be saved to: ./downloaded-artifacts/comparative-analysis.md (or custom path)
```

## Workflow Artifacts

These scripts analyze artifacts from the following workflows:

1. **CodeQL Analysis** - Security scanning with CodeQL
2. **Compliance Check (Weekly)** - Weekly Companies House live checks
3. **Compliance Check (Live)** - On-demand Companies House live checks
4. **Compliance Check (Sandbox)** - Test environment compliance checks

## Artifact Structure

Each workflow uploads artifacts containing:

- `workflow-metadata.json` - Execution metadata (run ID, timestamp, branch, etc.)
- `repository-structure.txt` - Repository structure snapshot
- `codeql-summary.txt` - CodeQL findings summary (CodeQL workflow only)
- `*.sarif` - SARIF format security results (CodeQL workflow only)
- `response_*.json` - Companies House API responses (Compliance workflows only)

## Output Reports

### Analysis Report (`analysis-report.md`)

Contains:
- Workflow execution summary
- CodeQL security findings
- Compliance check results
- Comparative analysis across workflows
- Repository context and structure

### Comparative Analysis Report (`comparative-analysis.md`)

Contains:
- Executive summary of all workflows
- Execution timeline
- Cross-workflow correlation
- CodeQL and compliance integration
- Branch and commit coverage
- Build and compilation context
- Recommendations

## Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)

## Integration with Workflows

All workflows in `.github/workflows/` automatically:

1. Capture repository structure and metadata
2. Generate workflow-specific artifacts
3. Upload artifacts to GitHub Actions (90-day retention)
4. Update the orchestration ledger

To analyze artifacts:

1. Go to GitHub Actions → Select a workflow run
2. Download artifacts from the run
3. Extract the artifact ZIP files
4. Run the analysis scripts on the extracted directory

## Example Analysis Workflow

```bash
# 1. Download artifacts from multiple workflow runs
# (Use GitHub UI or gh CLI)

# 2. Organize artifacts in a directory
mkdir -p workflow-artifacts
cd workflow-artifacts
# Extract artifact ZIPs here

# 3. Run line-by-line analysis
python3 ../.github/scripts/artifact-analyzer.py .

# 4. Run comparative analysis
python3 ../.github/scripts/comparative-analyzer.py .

# 5. Review reports
cat analysis-report.md
cat comparative-analysis.md
```

## Notes

- All scripts are designed to be safe and read-only
- Scripts handle missing or malformed data gracefully
- Reports are generated in Markdown format for easy review
- Timestamps are in UTC for consistency

## Support

For questions or issues with the analysis scripts, contact:
- **Maintainer:** Corvin Nehal Dhali
- **Email:** info@eckohaus.co.uk

---

*Part of the Eckohaus Orchestration Pilot*  
*© 2025 Eckohaus Ltd - Internal Use Only*
