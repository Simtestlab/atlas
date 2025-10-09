# Issue #10: Publish GitHub Organization Issues in MkDocs

<div class="issue-page">
    <div class="issue-header-section">
        <div class="issue-title-row">
            <h1 class="issue-title">Publish GitHub Organization Issues in MkDocs</h1>
            <span class="issue-status-badge open">🟢 Open</span>
        </div>
        
        <div class="issue-metadata">
            <div class="issue-number">#10</div>
            <div class="issue-details-grid">
                <div class="detail-item">
                    <span class="detail-label">👤 Author:</span>
                    <a href="https://github.com/nallasivamselvaraj" class="detail-value" target="_blank" rel="noopener">nallasivamselvaraj</a>
                </div>
                <div class="detail-item">
                    <span class="detail-label">📅 Created:</span>
                    <span class="detail-value">October 5, 2025 at 12:00:00 UTC</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">🔄 Updated:</span>
                    <span class="detail-value">October 5, 2025 at 12:00:00 UTC</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">🏷️ State:</span>
                    <span class="detail-value status-open">Open</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">👥 Assignees:</span>
                    <span class="detail-value">nallasivamselvaraj</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">🏷️ Labels:</span>
                    <span class="detail-value">None</span>
                </div>
            </div>
        </div>
    </div>

    <div class="issue-body-section">
        <h2>📝 Description</h2>
        <div class="issue-body">
            <h3>User Story: Publish GitHub Organization Issues in MkDocs</h3>
            
            <p><strong>Title:</strong> As a team member, I want to automatically publish all GitHub issues from our organization into MkDocs so that the documentation site always reflects the latest issues.</p>
            
            <h4>Description</h4>
            <p>Currently, issues from our GitHub repositories are scattered and hard to track in our documentation. We want to automate the process of fetching all issues from all repositories in the organization and generating markdown files that can be rendered by MkDocs. The generated markdowns should include issue title, repository, state, creation date, URL, and description.</p>
            
            <h4>Acceptance Criteria</h4>
            <ul>
                <li>A script/tool fetches all issues from all repositories in the GitHub organization, excluding pull requests.</li>
                <li>Each issue is converted into a markdown (.md) file with:
                    <ul>
                        <li>Issue title</li>
                        <li>Repository name</li>
                        <li>Issue state (open/closed)</li>
                        <li>Creation date</li>
                        <li>URL link to GitHub</li>
                        <li>Issue description/body</li>
                    </ul>
                </li>
                <li>The markdown files are saved in a structured folder (e.g., docs/github_issues/).</li>
                <li>mkdocs.yml is updated automatically or can be regenerated to include all issues in the navigation, grouped by repository.</li>
                <li>The solution should support periodic updates (e.g., via GitHub Actions) to keep MkDocs synchronized with GitHub issues.</li>
                <li>Proper error handling for API limits and pagination.</li>
            </ul>
            
            <h4>Notes / Technical Details</h4>
            <ul>
                <li>Use GitHub REST API or GitHub CLI.</li>
                <li>Use Python for automation (or another preferred language).</li>
                <li>Ensure markdown filenames are sanitized for special characters.</li>
                <li>Optional: filter issues by labels, state, or date if needed.</li>
            </ul>
        </div>
    </div>

    <div class="issue-actions-section">
        <div class="action-buttons">
            <a href="https://github.com/Simtestlab/atlas/issues/10" class="btn btn-primary" target="_blank" rel="noopener">
                <span class="btn-icon">🔗</span>
                View on GitHub
            </a>
            <a href="../" class="btn btn-secondary">
                <span class="btn-icon">📋</span>
                Back to Issues
            </a>
            <a href="../../" class="btn btn-secondary">
                <span class="btn-icon">🏠</span>
                Dashboard
            </a>
        </div>
    </div>

    <div class="issue-navigation">
        <div class="nav-links">
            <a href="../issues/11-clean-up-atlas/" class="nav-link prev">
                <span class="nav-arrow">←</span>
                <div class="nav-content">
                    <span class="nav-label">Previous Issue</span>
                    <span class="nav-title">#11 clean up atlas</span>
                </div>
            </a>
            <a href="../issues/8-fix-submodule-to-point-to-main/" class="nav-link next">
                <div class="nav-content">
                    <span class="nav-label">Next Issue</span>
                    <span class="nav-title">#8 fix submodule to point to main</span>
                </div>
                <span class="nav-arrow">→</span>
            </a>
        </div>
    </div>
</div>