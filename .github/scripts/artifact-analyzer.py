#!/usr/bin/env python3
"""
Eckohaus Orchestration Pilot - Artifact Analyzer
=================================================
Performs line-by-line analysis of workflow artifacts and generates
comprehensive reports integrating compliance checks with security analysis.

This script analyzes artifacts from:
- Compliance Check (Companies House - Weekly)
- Compliance Check (Companies House - Live)
- Compliance Check (Companies House - Sandbox)
- CodeQL Security Analysis

Usage:
    python3 artifact-analyzer.py <artifact-directory>
    
Output:
    - Detailed line-by-line analysis report
    - Comparative analysis across workflows
    - Integration of CodeQL findings with compliance data
"""

import os
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any, Optional
import re


class ArtifactAnalyzer:
    """Analyzes workflow artifacts and generates comprehensive reports."""
    
    def __init__(self, artifact_dir: str):
        self.artifact_dir = Path(artifact_dir)
        self.analyses = {}
        self.codeql_findings = []
        self.compliance_data = []
        
    def analyze_all(self):
        """Run comprehensive analysis on all artifacts."""
        print("🔍 Starting artifact analysis...")
        print(f"📂 Artifact directory: {self.artifact_dir}")
        
        # Discover and analyze artifacts
        self._discover_artifacts()
        
        # Perform analyses
        self._analyze_workflow_metadata()
        self._analyze_repository_structure()
        self._analyze_codeql_results()
        self._analyze_compliance_responses()
        self._perform_comparative_analysis()
        
        # Generate report
        self._generate_report()
        
        print("✅ Analysis complete!")
        
    def _discover_artifacts(self):
        """Discover all artifact files in the directory."""
        print("\n📋 Discovering artifacts...")
        
        for root, dirs, files in os.walk(self.artifact_dir):
            for file in files:
                file_path = Path(root) / file
                rel_path = file_path.relative_to(self.artifact_dir)
                print(f"  Found: {rel_path}")
                
    def _analyze_workflow_metadata(self):
        """Analyze workflow metadata from all runs."""
        print("\n📊 Analyzing workflow metadata...")
        
        metadata_files = list(self.artifact_dir.rglob("workflow-metadata.json"))
        
        for metadata_file in metadata_files:
            try:
                with open(metadata_file, 'r') as f:
                    metadata = json.load(f)
                    
                workflow_name = metadata.get('workflow', 'Unknown')
                print(f"  ✓ {workflow_name}")
                print(f"    Run ID: {metadata.get('run_id')}")
                print(f"    Timestamp: {metadata.get('timestamp')}")
                print(f"    Branch: {metadata.get('ref_name', metadata.get('ref', 'N/A'))}")
                
                if workflow_name not in self.analyses:
                    self.analyses[workflow_name] = []
                    
                self.analyses[workflow_name].append(metadata)
                
            except Exception as e:
                print(f"  ⚠ Error reading {metadata_file}: {e}")
                
    def _analyze_repository_structure(self):
        """Analyze repository structure from artifacts."""
        print("\n🗂️  Analyzing repository structure...")
        
        structure_files = list(self.artifact_dir.rglob("repository-structure.txt"))
        
        for structure_file in structure_files:
            try:
                with open(structure_file, 'r') as f:
                    content = f.read()
                    
                # Extract key information
                lines = content.split('\n')
                
                # Count files
                file_count_line = [l for l in lines if 'Total files:' in l]
                if file_count_line:
                    print(f"  Total files: {file_count_line[0].split(':')[1].strip()}")
                
                # Extract branch info
                branch_section = False
                for line in lines:
                    if '=== Branch Information ===' in line:
                        branch_section = True
                        continue
                    if branch_section and line.strip() and not line.startswith('==='):
                        if '*' in line:  # Current branch
                            print(f"  Current branch: {line.strip()}")
                        branch_section = '===' not in line
                        
            except Exception as e:
                print(f"  ⚠ Error reading {structure_file}: {e}")
                
    def _analyze_codeql_results(self):
        """Analyze CodeQL security findings."""
        print("\n🔐 Analyzing CodeQL results...")
        
        # Look for CodeQL summary files
        codeql_summaries = list(self.artifact_dir.rglob("codeql-summary.txt"))
        
        for summary_file in codeql_summaries:
            try:
                with open(summary_file, 'r') as f:
                    content = f.read()
                    
                print(f"  CodeQL Summary from {summary_file.parent.name}:")
                
                # Extract findings
                findings_section = False
                finding_count = 0
                
                for line in content.split('\n'):
                    if '=== Findings ===' in line:
                        findings_section = True
                        continue
                    if findings_section and line.strip() and line.startswith('-'):
                        finding_count += 1
                        self.codeql_findings.append(line.strip())
                        print(f"    {line.strip()}")
                        
                if finding_count == 0:
                    print("    ✓ No security findings reported")
                else:
                    print(f"    Total findings: {finding_count}")
                    
            except Exception as e:
                print(f"  ⚠ Error reading {summary_file}: {e}")
                
        # Also check for SARIF files
        sarif_files = list(self.artifact_dir.rglob("*.sarif"))
        for sarif_file in sarif_files:
            try:
                with open(sarif_file, 'r') as f:
                    sarif_data = json.load(f)
                    
                # Extract results
                for run in sarif_data.get('runs', []):
                    results = run.get('results', [])
                    if results:
                        print(f"  SARIF file {sarif_file.name} contains {len(results)} results")
                        
            except Exception as e:
                print(f"  ⚠ Error reading SARIF {sarif_file}: {e}")
                
    def _analyze_compliance_responses(self):
        """Analyze Companies House compliance responses."""
        print("\n📋 Analyzing compliance responses...")
        
        # Look for response JSON files
        response_files = []
        response_files.extend(self.artifact_dir.rglob("response_weekly*.json"))
        response_files.extend(self.artifact_dir.rglob("response_live*.json"))
        response_files.extend(self.artifact_dir.rglob("response_sandbox*.json"))
        
        for response_file in response_files:
            try:
                with open(response_file, 'r') as f:
                    response_data = json.load(f)
                    
                # Determine response type
                response_type = "Unknown"
                if "weekly" in response_file.name:
                    response_type = "Weekly"
                elif "live" in response_file.name:
                    response_type = "Live"
                elif "sandbox" in response_file.name:
                    response_type = "Sandbox"
                    
                print(f"  {response_type} response: {response_file.name}")
                
                # Extract key fields
                if isinstance(response_data, dict):
                    company_name = response_data.get('company_name', 'N/A')
                    company_number = response_data.get('company_number', 'N/A')
                    company_status = response_data.get('company_status', 'N/A')
                    
                    print(f"    Company: {company_name} ({company_number})")
                    print(f"    Status: {company_status}")
                    
                    self.compliance_data.append({
                        'type': response_type,
                        'file': response_file.name,
                        'data': response_data
                    })
                else:
                    print(f"    ⚠ Unexpected response format")
                    
            except json.JSONDecodeError:
                print(f"  ⚠ Invalid JSON in {response_file}")
            except Exception as e:
                print(f"  ⚠ Error reading {response_file}: {e}")
                
    def _perform_comparative_analysis(self):
        """Perform comparative analysis across all workflows."""
        print("\n🔬 Performing comparative analysis...")
        
        # Compare workflow executions
        workflow_count = len(self.analyses)
        print(f"  Total workflows analyzed: {workflow_count}")
        
        for workflow_name, runs in self.analyses.items():
            print(f"  {workflow_name}: {len(runs)} run(s)")
            
        # Compare compliance responses
        if self.compliance_data:
            print(f"\n  Compliance responses: {len(self.compliance_data)}")
            
            # Group by type
            by_type = {}
            for item in self.compliance_data:
                resp_type = item['type']
                if resp_type not in by_type:
                    by_type[resp_type] = []
                by_type[resp_type].append(item)
                
            for resp_type, items in by_type.items():
                print(f"    {resp_type}: {len(items)} response(s)")
                
        # Correlate CodeQL findings with compliance data
        if self.codeql_findings and self.compliance_data:
            print("\n  📊 CodeQL & Compliance Correlation:")
            print(f"    CodeQL findings: {len(self.codeql_findings)}")
            print(f"    Compliance checks: {len(self.compliance_data)}")
            print("    Integration: Security analysis performed alongside compliance verification")
            
    def _generate_report(self):
        """Generate comprehensive analysis report."""
        print("\n📄 Generating analysis report...")
        
        report_file = self.artifact_dir / "analysis-report.md"
        
        with open(report_file, 'w') as f:
            f.write("# Eckohaus Orchestration Pilot - Artifact Analysis Report\n\n")
            f.write(f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n\n")
            f.write("---\n\n")
            
            # Workflow Summary
            f.write("## Workflow Execution Summary\n\n")
            f.write("| Workflow | Runs | Latest Execution |\n")
            f.write("|----------|------|------------------|\n")
            
            for workflow_name, runs in self.analyses.items():
                latest = max(runs, key=lambda x: x.get('timestamp', ''))
                f.write(f"| {workflow_name} | {len(runs)} | {latest.get('timestamp', 'N/A')} |\n")
                
            f.write("\n")
            
            # CodeQL Findings
            f.write("## CodeQL Security Analysis\n\n")
            if self.codeql_findings:
                f.write(f"**Total Findings:** {len(self.codeql_findings)}\n\n")
                for finding in self.codeql_findings:
                    f.write(f"- {finding}\n")
            else:
                f.write("✅ No security issues detected\n")
                
            f.write("\n")
            
            # Compliance Summary
            f.write("## Compliance Check Summary\n\n")
            if self.compliance_data:
                f.write("| Type | File | Company Status |\n")
                f.write("|------|------|----------------|\n")
                
                for item in self.compliance_data:
                    status = item['data'].get('company_status', 'N/A')
                    f.write(f"| {item['type']} | {item['file']} | {status} |\n")
            else:
                f.write("No compliance data available for analysis.\n")
                
            f.write("\n")
            
            # Comparative Analysis
            f.write("## Comparative Analysis\n\n")
            f.write("### Integration Points\n\n")
            f.write("- **Security & Compliance Integration:** CodeQL analysis runs alongside compliance checks\n")
            f.write("- **Branch Context:** All workflows capture current branch and commit information\n")
            f.write("- **Repository Structure:** Consistent structure analysis across all workflow types\n")
            f.write("- **Artifact Retention:** 90-day retention for historical analysis\n\n")
            
            # Repository Context
            f.write("## Repository Context\n\n")
            structure_files = list(self.artifact_dir.rglob("repository-structure.txt"))
            if structure_files:
                f.write("Repository structure captured in all workflow runs for:\n\n")
                f.write("- File and directory hierarchy\n")
                f.write("- Branch information\n")
                f.write("- Commit metadata\n")
                f.write("- File statistics\n")
            
            f.write("\n---\n\n")
            f.write("*This report was automatically generated by artifact-analyzer.py*\n")
            
        print(f"  ✅ Report saved to: {report_file}")


def main():
    """Main entry point for the artifact analyzer."""
    if len(sys.argv) < 2:
        print("Usage: python3 artifact-analyzer.py <artifact-directory>")
        print("\nExample:")
        print("  python3 artifact-analyzer.py ./artifacts")
        sys.exit(1)
        
    artifact_dir = sys.argv[1]
    
    if not os.path.exists(artifact_dir):
        print(f"❌ Error: Directory '{artifact_dir}' does not exist")
        sys.exit(1)
        
    analyzer = ArtifactAnalyzer(artifact_dir)
    analyzer.analyze_all()


if __name__ == "__main__":
    main()
