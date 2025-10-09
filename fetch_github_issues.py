#!/usr/bin/env python3
"""
GitHub Issues Fetcher for MkDocs Integration

Fetches GitHub issues from repositories and generates structured markdown
files that can be integrated with MkDocs.

Usage:
    python fetch_github_issues.py [--config path/to/config.yml]

Environment Variables:
    GITHUB_TOKEN: GitHub personal access token (recommended for higher rate limits)
    GITHUB_REPO: Override repository as 'owner/repo'
"""

import os
import sys
import json
import yaml
import requests
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import List, Dict, Optional
import time
import re
import argparse

try:
    from jinja2 import Environment, FileSystemLoader
    JINJA2_AVAILABLE = True
except ImportError:
    JINJA2_AVAILABLE = False
    print("Warning: Jinja2 not available. Templates will use basic string replacement.")

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# --------------------------
# Config Manager
# --------------------------
class ConfigManager:
    def __init__(self, config_path: str = None):
        self.config_path = config_path or 'config/github_issues.yml'
        self.config = self.load_config()

    def load_config(self) -> Dict:
        try:
            config_file = Path(self.config_path)
            if not config_file.exists():
                print(f"Config file not found: {self.config_path}")
                return self.get_default_config()
            with open(config_file, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            self.merge_env_variables(config)
            return config
        except Exception as e:
            print(f"Error loading config: {e}")
            return self.get_default_config()

    def merge_env_variables(self, config: Dict):
        token_var = config.get('github_api', {}).get('token_env_var', 'GITHUB_TOKEN')
        if token_var and os.getenv(token_var):
            config.setdefault('github_api', {})['token'] = os.getenv(token_var)

        if os.getenv('GITHUB_REPO'):
            repo_parts = os.getenv('GITHUB_REPO').split('/')
            if len(repo_parts) == 2:
                config.setdefault('repository', {})['owner'] = repo_parts[0]
                config.setdefault('repository', {})['name'] = repo_parts[1]

    def get_default_config(self) -> Dict:
        return {
            'repository': {
                'owner': 'Simtestlab',
                'name': 'atlas',
                'full_name': 'Simtestlab/atlas',
                'mode': 'single'
            },
            'github_api': {
                'base_url': 'https://api.github.com',
                'rate_limit_delay': 0.1,
                'per_page': 100
            },
            'output': {
                'base_dir': 'simtestlab/github_issues',
                'index_file': 'index.md',
                'dashboard_file': 'dashboard.md',
                'taskboard_file': 'taskboard.md',
                'table_file': 'table.md',
                'summary_file': 'summary.json'
            },
            'features': {
                'enable_dashboard': True,
                'enable_taskboard': True,
                'show_closed_issues': True,
                'max_recent_closed': 10
            }
        }

# --------------------------
# GitHub Issues Fetcher
# --------------------------
class GitHubIssuesFetcher:
    def __init__(self, config_path: str = None):
        self.config_manager = ConfigManager(config_path)
        self.config = self.config_manager.config

        repo_config = self.config.get('repository', {})
        self.mode = repo_config.get('mode', 'single')
        self.owner = repo_config.get('owner', 'Simtestlab')

        if self.mode == 'single':
            self.repo = f"{self.owner}/{repo_config.get('name', 'atlas')}"
            self.repositories = [self.repo]
        else:
            self.repo = None
            self.repositories = []

        api_config = self.config.get('github_api', {})
        self.token = api_config.get('token') or os.getenv('GITHUB_TOKEN')
        self.base_url = api_config.get('base_url', 'https://api.github.com')
        self.rate_limit_delay = api_config.get('rate_limit_delay', 0.1)
        self.per_page = api_config.get('per_page', 100)

        self.headers = {'Accept': 'application/vnd.github.v3+json', 'User-Agent': 'GitHub-Issues-Fetcher/2.0'}
        if self.token:
            self.headers['Authorization'] = f'token {self.token}'

        output_config = self.config.get('output', {})
        self.output_dir = Path(output_config.get('base_dir', 'simtestlab/github_issues'))
        self.setup_directory_structure(output_config)

        self.index_file = output_config.get('index_file', 'index.md')
        self.dashboard_file = output_config.get('dashboard_file', 'dashboard.md')
        self.taskboard_file = output_config.get('taskboard_file', 'taskboard.md')
        self.table_file = output_config.get('table_file', 'table.md')
        self.summary_file = output_config.get('summary_file', 'summary.json')

    def setup_directory_structure(self, output_config: Dict):
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.overview_dir = self.output_dir / "overview"
        self.repositories_dir = self.output_dir / "repositories"
        self.dashboards_dir = self.overview_dir
        self.exports_dir = self.output_dir / "exports"

        for dir_path in [self.overview_dir, self.repositories_dir, self.dashboards_dir, self.exports_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)

    # --------------------------
    # GitHub API Requests
    # --------------------------
    def make_request(self, url: str, params: Dict = None) -> Optional[Dict]:
        try:
            response = requests.get(url, headers=self.headers, params=params or {})
            if response.status_code == 403 and 'rate limit' in response.text.lower():
                reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
                sleep_time = max(0, reset_time - int(time.time()) + 10)
                print(f"Rate limit exceeded. Waiting {sleep_time} seconds...")
                time.sleep(sleep_time)
                return self.make_request(url, params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    def fetch_repository_issues(self, repo_full_name: str, state: str = 'all') -> List[Dict]:
        issues = []
        page = 1
        while True:
            url = f"{self.base_url}/repos/{repo_full_name}/issues"
            params = {'state': state, 'per_page': self.per_page, 'page': page}
            data = self.make_request(url, params)
            if not data:
                break
            page_issues = [i for i in data if 'pull_request' not in i]
            if not page_issues:
                break
            issues.extend(page_issues)
            if len(data) < self.per_page:
                break
            page += 1
            time.sleep(self.rate_limit_delay)
        return issues

    def get_repositories_to_process(self) -> List[str]:
        if self.mode == 'single':
            return [self.repo]
        elif self.mode == 'organization':
            return self.fetch_organization_repositories()
        elif self.mode == 'multiple':
            return self.config.get('repository', {}).get('repositories', [])
        else:
            raise ValueError(f"Unknown mode: {self.mode}")

    # --------------------------
    # Markdown Generation
    # --------------------------
    def sanitize_filename(self, text: str) -> str:
        text = re.sub(r'[<>:"/\\|?*]', '-', text)
        text = re.sub(r'[-\s]+', '-', text).strip('-')
        return text[:100] if len(text) <= 100 else text[:97] + '...'

    def format_issue_content(self, issue: Dict) -> str:
        created_at = datetime.fromisoformat(issue['created_at'].replace('Z', '+00:00')).strftime('%Y-%m-%d %H:%M:%S UTC')
        updated_at = datetime.fromisoformat(issue['updated_at'].replace('Z', '+00:00')).strftime('%Y-%m-%d %H:%M:%S UTC')
        labels = [label['name'] for label in issue.get('labels', [])]
        assignees = [a['login'] for a in issue.get('assignees', [])]
        state_badge = "🟢 Open" if issue['state'] == 'open' else "🔴 Closed"

        content = f"""# {issue['title']}

{state_badge} **#{issue['number']}**

| Field | Value |
|-------|-------|
| **Author** | [@{issue['user']['login']}]({issue['user']['html_url']}) |
| **Created** | {created_at} |
| **Updated** | {updated_at} |
| **State** | {issue['state'].title()} |
"""
        if assignees:
            content += f"| **Assignees** | {', '.join(assignees)} |\n"
        if labels:
            content += f"| **Labels** | {', '.join(labels)} |\n"

        content += f"\n## Body\n\n{issue.get('body', 'No description.')}\n"

        return content

    def save_issue_markdown(self, repo_dir: Path, issue: Dict):
        issues_dir = repo_dir / "issues"
        issues_dir.mkdir(parents=True, exist_ok=True)
        filename = self.sanitize_filename(f"{issue['number']}-{issue['title']}.md")
        file_path = issues_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(self.format_issue_content(issue))
        return file_path

    def save_repo_index(self, repo_dir: Path, repo_name: str, issues: List[Dict]):
        index_file = repo_dir / "index.md"
        content = f"# {repo_name} Issues\n\n"
        for issue in issues:
            issue_file = self.sanitize_filename(f"{issue['number']}-{issue['title']}.md")
            content += f"- [{issue['title']}](issues/{issue_file}) ({issue['state']})\n"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)

    def save_issues_table(self, repo_dir: Path, repo_name: str, repo_full_name: str, issues: List[Dict]):
        """Generate a comprehensive table view of all issues"""
        table_file = repo_dir / "table.md"
        content = f"""# {repo_name} Issues - Table View

<style>
/* Centralized Issues Table Configuration */
.issues-table {{
  table-layout: auto;
  width: 100%;
  margin: 0 auto;
  border-collapse: collapse;
  text-align: center;
}}

/* Column Configuration - Easily adjustable */
.issues-table th:nth-child(1) {{ width: 8%; text-align: center; }}   /* Task # */
.issues-table th:nth-child(2) {{ width: 15%; text-align: left; }}    /* Title */
.issues-table th:nth-child(3) {{ width: 35%; text-align: left; }}    /* Description */
.issues-table th:nth-child(4) {{ width: 10%; text-align: center; }}  /* Project */
.issues-table th:nth-child(5) {{ width: 12%; text-align: center; }}  /* Assignee */
.issues-table th:nth-child(6) {{ width: 10%; text-align: center; }}  /* Created */
.issues-table th:nth-child(7) {{ width: 8%; text-align: center; }}   /* Status */
.issues-table th:nth-child(8) {{ width: 12%; text-align: center; }}  /* URL Link */

.issues-table td:nth-child(1) {{ text-align: center; }}   /* Task # */
.issues-table td:nth-child(2) {{ text-align: left; }}     /* Title */
.issues-table td:nth-child(3) {{ text-align: left; }}     /* Description */
.issues-table td:nth-child(4) {{ text-align: center; }}   /* Project */
.issues-table td:nth-child(5) {{ text-align: center; }}   /* Assignee */
.issues-table td:nth-child(6) {{ text-align: center; }}   /* Created */
.issues-table td:nth-child(7) {{ text-align: center; }}   /* Status */
.issues-table td:nth-child(8) {{ text-align: center; }}   /* URL Link */

.issues-table th,
.issues-table td {{
  word-wrap: break-word;
  vertical-align: middle;
  padding: 12px 8px;
  border: 1px solid var(--md-default-fg-color--lightest);
}}

/* Description Read More/Less Functionality */
.description-short {{
  display: inline;
}}
.description-full {{
  display: none;
}}
.read-more-btn, .read-less-btn {{
  color: var(--md-primary-fg-color);
  cursor: pointer;
  font-weight: bold;
  text-decoration: underline;
  margin-left: 5px;
}}
.expand-description.expanded .description-short {{
  display: none;
}}
.expand-description.expanded .description-full {{
  display: inline;
}}
.expand-description.expanded .read-more-btn {{
  display: none;
}}
.expand-description .read-less-btn {{
  display: none;
}}
.expand-description.expanded .read-less-btn {{
  display: inline;
}}
</style>

<script>
function toggleDescription(id) {{
    const element = document.getElementById(id);
    element.classList.toggle('expanded');
}}
</script>

## Complete Issues Table

<div class="issues-table" markdown>

| Task # | Title | Description | Project | Assignee | Created | Status | URL Link |
|--------|-------|-------------|---------|----------|---------|--------|----------|
"""
        
        for issue in issues:
            # Extract description with read more functionality
            full_description = issue.get('body', 'No description')
            if full_description and full_description.strip():
                # Clean the description
                clean_description = full_description.replace('\n', ' ').replace('|', '\\|').strip()
                
                # Create short and full versions
                if len(clean_description) > 100:
                    short_description = clean_description[:100] + "..."
                    description_html = f'<div class="expand-description" id="desc-{issue["number"]}"><span class="description-short">{short_description}</span><span class="description-full">{clean_description}</span><span class="read-more-btn" onclick="toggleDescription(\'desc-{issue["number"]}\')">Read More</span><span class="read-less-btn" onclick="toggleDescription(\'desc-{issue["number"]}\')">Read Less</span></div>'
                else:
                    description_html = clean_description
            else:
                description_html = "No description provided"
            
            # Get assignee
            assignees = issue.get('assignees', [])
            assignee = assignees[0]['login'] if assignees else 'Unassigned'
            
            # Format date
            created_date = datetime.fromisoformat(issue['created_at'].replace('Z', '+00:00')).strftime('%Y-%m-%d')
            
            # Status emoji
            status_emoji = "🟢 Open" if issue['state'] == 'open' else "🔴 Closed"
            
            # GitHub URL - use the full repository name directly
            github_url = f"https://github.com/{repo_full_name}/issues/{issue['number']}"
            issue_file = self.sanitize_filename(f"{issue['number']}-{issue['title']}.md")
            
            content += f"| **#{issue['number']}** | {issue['title']} | {description_html} | {repo_name} | {assignee} | {created_date} | {status_emoji} | [GitHub]({github_url}) |\n"
        
        content += "\n</div>\n"
        
        with open(table_file, 'w', encoding='utf-8') as f:
            f.write(content)

    # --------------------------
    # Main Execution
    # --------------------------
    def run(self):
        repos = self.get_repositories_to_process()
        summary = {}
        for repo_full_name in repos:
            print(f"Fetching issues for {repo_full_name}...")
            issues = self.fetch_repository_issues(repo_full_name, state='all')
            repo_name = repo_full_name.split('/')[-1]
            repo_dir = self.output_dir / repo_name
            repo_dir.mkdir(parents=True, exist_ok=True)
            
            # Save only the table view
            self.save_issues_table(repo_dir, repo_name, repo_full_name, issues)
            
            summary[repo_name] = {'issue_count': len(issues), 'issues': [i['number'] for i in issues]}

        # Save summary JSON
        summary_file = self.exports_dir / self.summary_file
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=4)

        print(f"Done. Table view saved in {self.output_dir.resolve()}")
        print(f"Summary JSON: {summary_file.resolve()}")
        print("Generated files: table view only")

# --------------------------
# CLI
# --------------------------
def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub issues for MkDocs")
    parser.add_argument('--config', type=str, help="Path to YAML config file")
    args = parser.parse_args()

    fetcher = GitHubIssuesFetcher(config_path=args.config)
    fetcher.run()

if __name__ == "__main__":
    main()
