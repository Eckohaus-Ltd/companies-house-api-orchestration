#!/usr/bin/env python3
"""
Eckohaus Orchestration Pilot - Workflow Log Analyzer
====================================================

This script performs line-by-line analysis of GitHub Actions workflow logs,
integrating them with the repository folder and file structure.

Analyzes the following workflows:
1. CodeQL Analysis (push on main)
2. Compliance Check (Companies House - Live)
3. Compliance Check (Companies House - Sandbox)
4. Compliance Check (Companies House - Weekly)

Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>
"""

import os
import sys
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class WorkflowLogAnalyzer:
    """Analyzes GitHub Actions workflow logs and integrates with repo structure."""
    
    WORKFLOWS = {
        'codeql': {
            'name': 'CodeQL Analysis',
            'file': '.github/workflows/codeql-analysis.yml',
            'event': 'push',
            'branch': 'main'
        },
        'compliance_live': {
            'name': 'Compliance Check (Companies House - Live)',
            'file': '.github/workflows/compliance-check-live.yml', 
            'event': 'schedule',
            'branch': 'main'
        },
        'compliance_sandbox': {
            'name': 'Compliance Check (Companies House - Sandbox)',
            'file': '.github/workflows/compliance-check.yml',
            'event': 'workflow_dispatch',
            'branch': 'main'
        },
        'compliance_weekly': {
            'name': 'Compliance Check (Companies House - Weekly)',
            'file': '.github/workflows/compliance-check-weekly.yml',
            'event': 'schedule',
            'branch': 'main'
        }
    }
    
    def __init__(self, repo_path: str = '.'):
        """Initialize the analyzer with repository path."""
        self.repo_path = Path(repo_path).resolve()
        self.repo_structure = self._analyze_repo_structure()
        
    def _analyze_repo_structure(self) -> Dict:
        """Analyze and document repository folder/file structure."""
        structure = {
            'workflows': [],
            'config': [],
            'data': {
                'responses': [],
                'sandbox_responses': []
            },
            'docs': [],
            'root': []
        }
        
        # Analyze workflows
        workflows_dir = self.repo_path / '.github' / 'workflows'
        if workflows_dir.exists():
            structure['workflows'] = [f.name for f in workflows_dir.glob('*.yml')]
        
        # Analyze config
        config_dir = self.repo_path / 'config'
        if config_dir.exists():
            structure['config'] = [f.name for f in config_dir.iterdir()]
        
        # Analyze data directories
        data_dir = self.repo_path / 'data'
        if data_dir.exists():
            responses_dir = data_dir / 'responses'
            if responses_dir.exists():
                structure['data']['responses'] = [
                    f.name for f in responses_dir.glob('*.json')
                ]
            
            sandbox_dir = data_dir / 'sandbox_responses'
            if sandbox_dir.exists():
                structure['data']['sandbox_responses'] = [
                    f.name for f in sandbox_dir.glob('*.json')
                ]
        
        # Root files
        for item in self.repo_path.iterdir():
            if item.is_file() and item.suffix in ['.md', '.yml', '.yaml']:
                structure['root'].append(item.name)
        
        return structure
    
    def get_latest_run_logs(self, workflow_key: str) -> Optional[Dict]:
        """
        Fetch latest workflow run logs using GitHub CLI.
        
        Note: This requires gh CLI to be installed and authenticated.
        For production use, consider using GitHub API directly with tokens.
        """
        workflow = self.WORKFLOWS.get(workflow_key)
        if not workflow:
            return None
        
        # In a real implementation, this would call GitHub API
        # For now, return a placeholder structure
        return {
            'workflow': workflow['name'],
            'status': 'placeholder',
            'message': 'GitHub API integration required for live data'
        }
    
    def analyze_compliance_workflow_log(self, log_content: str, workflow_type: str) -> Dict:
        """
        Perform line-by-line analysis of compliance workflow log.
        
        Args:
            log_content: Raw log content from workflow run
            workflow_type: Type of compliance workflow (live, sandbox, weekly)
        
        Returns:
            Dictionary with analysis results
        """
        analysis = {
            'workflow_type': workflow_type,
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'steps': [],
            'errors': [],
            'warnings': [],
            'file_operations': [],
            'api_calls': [],
            'summary': {}
        }
        
        lines = log_content.split('\n')
        current_step = None
        
        for line_num, line in enumerate(lines, 1):
            # Track step transitions
            if '##[group]' in line or 'name:' in line.lower():
                current_step = line.strip()
                analysis['steps'].append({
                    'line': line_num,
                    'step': current_step
                })
            
            # Track errors
            if '❌' in line or 'error' in line.lower() or 'failed' in line.lower():
                analysis['errors'].append({
                    'line': line_num,
                    'content': line.strip(),
                    'step': current_step
                })
            
            # Track warnings  
            if '⚠' in line or 'warning' in line.lower():
                analysis['warnings'].append({
                    'line': line_num,
                    'content': line.strip(),
                    'step': current_step
                })
            
            # Track file operations
            if any(keyword in line.lower() for keyword in ['mkdir', 'cp ', 'mv ', 'archived']):
                # Extract file paths
                if 'data/' in line:
                    analysis['file_operations'].append({
                        'line': line_num,
                        'operation': line.strip(),
                        'step': current_step
                    })
            
            # Track API calls - simple log pattern detection for analysis only
            # Note: This is log analysis, not URL sanitization
            if 'api.company-information.service.gov.uk' in line or 'api-sandbox' in line:
                analysis['api_calls'].append({
                    'line': line_num,
                    'endpoint': line.strip(),
                    'step': current_step
                })
            
            # Track metadata loading
            if 'config/metadata.yml' in line:
                analysis['file_operations'].append({
                    'line': line_num,
                    'operation': 'metadata_load',
                    'content': line.strip(),
                    'step': current_step
                })
        
        # Generate summary
        analysis['summary'] = {
            'total_lines': len(lines),
            'total_steps': len(analysis['steps']),
            'total_errors': len(analysis['errors']),
            'total_warnings': len(analysis['warnings']),
            'file_operations_count': len(analysis['file_operations']),
            'api_calls_count': len(analysis['api_calls'])
        }
        
        return analysis
    
    def analyze_codeql_workflow_log(self, log_content: str) -> Dict:
        """
        Perform line-by-line analysis of CodeQL workflow log.
        
        Args:
            log_content: Raw log content from CodeQL workflow run
        
        Returns:
            Dictionary with analysis results
        """
        analysis = {
            'workflow_type': 'codeql',
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'steps': [],
            'security_findings': [],
            'database_operations': [],
            'scan_results': [],
            'summary': {}
        }
        
        lines = log_content.split('\n')
        current_step = None
        
        for line_num, line in enumerate(lines, 1):
            # Track CodeQL specific operations
            if 'codeql' in line.lower():
                if 'database create' in line.lower():
                    analysis['database_operations'].append({
                        'line': line_num,
                        'operation': 'database_create',
                        'content': line.strip()
                    })
                elif 'database analyze' in line.lower():
                    analysis['database_operations'].append({
                        'line': line_num,
                        'operation': 'database_analyze',
                        'content': line.strip()
                    })
            
            # Track security findings
            if any(keyword in line.lower() for keyword in ['vulnerability', 'cwe-', 'severity']):
                analysis['security_findings'].append({
                    'line': line_num,
                    'finding': line.strip()
                })
            
            # Track scan results
            if 'results found' in line.lower() or 'queries run' in line.lower():
                analysis['scan_results'].append({
                    'line': line_num,
                    'result': line.strip()
                })
        
        analysis['summary'] = {
            'total_lines': len(lines),
            'database_operations_count': len(analysis['database_operations']),
            'security_findings_count': len(analysis['security_findings']),
            'scan_results_count': len(analysis['scan_results'])
        }
        
        return analysis
    
    def generate_integrated_report(self, analyses: List[Dict]) -> str:
        """
        Generate an integrated analysis report linking logs to repository structure.
        
        Args:
            analyses: List of workflow analysis dictionaries
        
        Returns:
            Formatted markdown report
        """
        report = []
        report.append("# Eckohaus Orchestration Pilot - Workflow Log Analysis Report")
        report.append(f"\n**Generated**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
        report.append("---\n")
        
        # Repository Structure Section
        report.append("## Repository Structure Integration\n")
        report.append("### Workflows")
        for wf in self.repo_structure['workflows']:
            report.append(f"- `.github/workflows/{wf}`")
        
        report.append("\n### Configuration")
        for cfg in self.repo_structure['config']:
            report.append(f"- `config/{cfg}`")
        
        report.append("\n### Data Archives")
        report.append(f"- Live responses: {len(self.repo_structure['data']['responses'])} files")
        report.append(f"- Sandbox responses: {len(self.repo_structure['data']['sandbox_responses'])} files")
        
        report.append("\n---\n")
        
        # Workflow Analysis Section
        report.append("## Workflow Analysis Results\n")
        
        for analysis in analyses:
            wf_type = analysis.get('workflow_type', 'unknown')
            report.append(f"### {wf_type.upper()} Workflow\n")
            
            summary = analysis.get('summary', {})
            report.append(f"**Lines Analyzed**: {summary.get('total_lines', 0)}")
            
            if 'total_errors' in summary:
                report.append(f"**Errors**: {summary['total_errors']}")
                report.append(f"**Warnings**: {summary['total_warnings']}")
                report.append(f"**API Calls**: {summary['api_calls_count']}")
                report.append(f"**File Operations**: {summary['file_operations_count']}")
                
                # Detail file operations with repo structure
                if analysis.get('file_operations'):
                    report.append("\n#### File Operations (Repo Structure Integration)")
                    for op in analysis['file_operations'][:10]:  # Show first 10
                        report.append(f"- Line {op['line']}: {op['operation']}")
                
                # Detail API calls
                if analysis.get('api_calls'):
                    report.append("\n#### Companies House API Interactions")
                    for call in analysis['api_calls'][:5]:  # Show first 5
                        report.append(f"- Line {call['line']}: API call detected")
            
            elif 'security_findings_count' in summary:
                report.append(f"**Security Findings**: {summary['security_findings_count']}")
                report.append(f"**Database Operations**: {summary['database_operations_count']}")
                
                # Detail security findings
                if analysis.get('security_findings'):
                    report.append("\n#### Security Findings")
                    for finding in analysis['security_findings'][:10]:
                        report.append(f"- Line {finding['line']}: {finding['finding']}")
            
            report.append("\n")
        
        report.append("---\n")
        report.append("\n_Report generated by Eckohaus Workflow Log Analyzer_")
        report.append("\n_Co-authored-by: system operator <wanda@openai.com>_")
        report.append("\n_Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>_")
        
        return '\n'.join(report)
    
    def save_report(self, report: str, filename: str = 'workflow-log-analysis.md'):
        """Save analysis report to file."""
        output_path = self.repo_path / filename
        output_path.write_text(report)
        print(f"✅ Report saved to: {output_path}")


def main():
    """Main execution function."""
    print("🔍 Eckohaus Orchestration Pilot - Workflow Log Analyzer")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = WorkflowLogAnalyzer()
    
    print(f"\n📁 Repository Structure:")
    print(f"   Workflows: {len(analyzer.repo_structure['workflows'])}")
    print(f"   Config files: {len(analyzer.repo_structure['config'])}")
    print(f"   Live responses: {len(analyzer.repo_structure['data']['responses'])}")
    print(f"   Sandbox responses: {len(analyzer.repo_structure['data']['sandbox_responses'])}")
    
    # For demonstration, create sample analyses
    # In production, these would come from actual log fetching
    sample_analyses = []
    
    # Sample compliance analysis
    sample_compliance_log = """
[2025-11-10] Loading metadata from config/metadata.yml
Debug → COMPANY_NAME: 'Eckohaus Ltd'
Debug → COMPANY_NUMBER: '12345678'
🔍 Querying Companies House LIVE API for company 12345678
HTTP status: 200
📄 Companies House LIVE API response:
🗂️ Response archived at data/responses/response_live_20251110_1012.json
✅ Ledger updated
    """
    
    compliance_analysis = analyzer.analyze_compliance_workflow_log(
        sample_compliance_log, 
        'compliance_live'
    )
    sample_analyses.append(compliance_analysis)
    
    # Generate and save report
    report = analyzer.generate_integrated_report(sample_analyses)
    analyzer.save_report(report)
    
    print(f"\n✅ Analysis complete!")
    print(f"\nTo analyze live workflow logs, ensure GitHub CLI is installed")
    print(f"and authenticated, or use GitHub API tokens.")


if __name__ == '__main__':
    main()
