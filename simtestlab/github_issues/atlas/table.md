# Atlas Issues - Professional Table View

<div class="issues-header">
    <div class="header-content">
        <h1>Atlas Repository Issues</h1>
        <p class="header-description">Complete overview of all GitHub issues with advanced filtering and search capabilities</p>
    </div>

</div>

<div class="table-controls">
    <div class="search-filters">
        <div class="search-box">
            <input type="text" id="issue-search" placeholder="ðŸ” Search issues..." class="search-input">
        </div>
        <div class="filter-buttons">
            <button class="filter-btn active" data-filter="all">All Issues</button>
            <button class="filter-btn" data-filter="open">Open</button>
            <button class="filter-btn" data-filter="closed">Closed</button>
        </div>
    </div>
</div>

<style>
/* Professional Issues Table Styling */
.issues-header {
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid var(--md-default-fg-color--lightest);
}

.header-content h1 {
    margin: 0 0 0.5rem 0;
    color: var(--md-default-fg-color);
}

.header-description {
    color: var(--md-default-fg-color--light);
    margin: 0;
    font-size: 0.9rem;
}



.btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.25rem;
    border: none;
    border-radius: 0.5rem;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.875rem;
    cursor: pointer;
    transition: all 0.2s ease;
}

.btn-primary {
    background: var(--md-primary-fg-color);
    color: var(--md-primary-bg-color);
}

.btn-primary:hover {
    background: var(--md-primary-fg-color--dark);
    transform: translateY(-1px);
}

.btn-secondary {
    background: var(--md-default-bg-color);
    color: var(--md-default-fg-color);
    border: 1px solid var(--md-default-fg-color--lightest);
}

.btn-secondary:hover {
    background: var(--md-default-fg-color--lightest);
}

.table-controls {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
    gap: 1rem;
}

.search-filters {
    display: flex;
    align-items: center;
    gap: 1rem;
    flex: 1;
}

.search-box {
    flex: 1;
    max-width: 300px;
}

.search-input {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 2px solid var(--md-default-fg-color--lightest);
    border-radius: 0.5rem;
    font-size: 0.875rem;
    background: var(--md-default-bg-color);
    color: var(--md-default-fg-color);
    transition: border-color 0.2s ease;
}

.search-input:focus {
    outline: none;
    border-color: var(--md-primary-fg-color);
}

.filter-buttons {
    display: flex;
    gap: 0.5rem;
}

.filter-btn {
    padding: 0.5rem 1rem;
    border: 1px solid var(--md-default-fg-color--lightest);
    background: var(--md-default-bg-color);
    color: var(--md-default-fg-color);
    border-radius: 0.375rem;
    cursor: pointer;
    font-size: 0.8rem;
    font-weight: 500;
    transition: all 0.2s ease;
}

.filter-btn:hover {
    background: var(--md-default-fg-color--lightest);
}

.filter-btn.active {
    background: var(--md-primary-fg-color);
    color: var(--md-primary-bg-color);
    border-color: var(--md-primary-fg-color);
}



/* Table Container with Horizontal Scrolling */
.table-container {
    width: 100%;
    overflow-x: auto;
    margin: 1.5rem 0;
    border-radius: 0.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    border: 1px solid var(--md-default-fg-color--lightest);
    position: relative;
}

/* Scrollbar styling */
.table-container::-webkit-scrollbar {
    height: 8px;
}

.table-container::-webkit-scrollbar-track {
    background: var(--md-default-fg-color--lightest);
    border-radius: 4px;
}

.table-container::-webkit-scrollbar-thumb {
    background: var(--md-primary-fg-color);
    border-radius: 4px;
}

.table-container::-webkit-scrollbar-thumb:hover {
    background: var(--md-primary-fg-color--dark);
}

/* Scroll Indicator */
.scroll-indicator {
    text-align: center;
    padding: 0.5rem;
    background: var(--md-default-fg-color--lightest);
    border-radius: 0.375rem 0.375rem 0 0;
    font-size: 0.8rem;
    color: var(--md-default-fg-color--light);
    font-style: italic;
    margin-bottom: -1px;
}

@media (min-width: 1200px) {
    .scroll-indicator {
        display: none;
    }
}

/* Enhanced Table Styling */
.issues-table {
    width: 100%;
    min-width: 900px; /* Minimum width to trigger horizontal scroll */
    border-collapse: collapse;
    background: var(--md-default-bg-color);
}

.issues-table th {
    background: linear-gradient(135deg, var(--md-primary-fg-color) 0%, var(--md-primary-fg-color--dark) 100%);
    color: var(--md-primary-bg-color);
    font-weight: 600;
    text-align: left;
    padding: 1rem 0.75rem;
    font-size: 0.875rem;
    letter-spacing: 0.025em;
}

.issues-table th:first-child { border-radius: 0.5rem 0 0 0; }
.issues-table th:last-child { border-radius: 0 0.5rem 0 0; }

.issues-table td {
    padding: 1rem 0.75rem;
    border-bottom: 1px solid var(--md-default-fg-color--lightest);
    vertical-align: top;
}

.issues-table tr:hover {
    background: var(--md-default-fg-color--lightest);
}

.issues-table tr:last-child td {
    border-bottom: none;
}

/* Column Widths for Horizontal Scrolling */
.issues-table th:nth-child(1), .issues-table td:nth-child(1) { 
    width: 80px; 
    text-align: center; 
    white-space: nowrap;
}
.issues-table th:nth-child(2), .issues-table td:nth-child(2) { 
    min-width: 200px; 
    max-width: 300px;
}
.issues-table th:nth-child(3), .issues-table td:nth-child(3) { 
    min-width: 250px; 
    max-width: 400px;
}
.issues-table th:nth-child(4), .issues-table td:nth-child(4) { 
    width: 100px; 
    text-align: center; 
    white-space: nowrap;
}
.issues-table th:nth-child(5), .issues-table td:nth-child(5) { 
    min-width: 120px; 
    text-align: center; 
    white-space: nowrap;
}
.issues-table th:nth-child(6), .issues-table td:nth-child(6) { 
    width: 100px; 
    text-align: center; 
    white-space: nowrap;
}
.issues-table th:nth-child(7), .issues-table td:nth-child(7) { 
    width: 100px; 
    text-align: center; 
    white-space: nowrap;
}
.issues-table th:nth-child(8), .issues-table td:nth-child(8) { 
    width: 100px; 
    text-align: center; 
    white-space: nowrap;
}

/* Responsive table text wrapping */
.issues-table td {
    word-wrap: break-word;
    overflow-wrap: break-word;
}

/* Issue Number Styling */
.issue-number {
    font-weight: 700;
    color: var(--md-primary-fg-color);
    font-size: 0.9rem;
}

/* Status Badges */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.75rem;
    font-weight: 600;
}

.status-open {
    background: #dcfce7;
    color: #15803d;
}

.status-closed {
    background: #fee2e2;
    color: #dc2626;
}

/* Enhanced Description with Read More */
.description-short {
    display: inline;
}
.description-full {
    display: none;
}
.read-more-btn, .read-less-btn {
    color: var(--md-primary-fg-color);
    cursor: pointer;
    font-weight: 600;
    text-decoration: underline;
    margin-left: 0.5rem;
    font-size: 0.8rem;
}
.read-more-btn:hover, .read-less-btn:hover {
    color: var(--md-primary-fg-color--dark);
}

.expand-description.expanded .description-short {
    display: none;
}
.expand-description.expanded .description-full {
    display: inline;
}
.expand-description.expanded .read-more-btn {
    display: none;
}
.expand-description .read-less-btn {
    display: none;
}
.expand-description.expanded .read-less-btn {
    display: inline;
}

/* Issue Link Styling */
.issue-link {
    color: var(--md-default-fg-color);
    text-decoration: none;
    font-weight: 500;
}

.issue-link:hover {
    color: var(--md-primary-fg-color);
    text-decoration: underline;
}

.github-link {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    color: var(--md-primary-fg-color);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.8rem;
}

.github-link:hover {
    text-decoration: underline;
}

/* Assignee styling */
.assignee {
    font-weight: 500;
    color: var(--md-default-fg-color);
}

/* Date styling */
.issue-date {
    color: var(--md-default-fg-color--light);
    font-size: 0.875rem;
}


</style>

<script>
function toggleDescription(id) {
    const element = document.getElementById(id);
    element.classList.toggle('expanded');
}

// Enhanced table functionality
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('issue-search');
    const filterButtons = document.querySelectorAll('.filter-btn');
    
    // Search functionality
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            filterTable(this.value.toLowerCase());
        });
    }
    
    // Filter buttons
    filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            filterButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            filterByStatus(this.dataset.filter);
        });
    });
    
    function filterTable(searchTerm) {
        const rows = document.querySelectorAll('.issues-table tbody tr');
        rows.forEach(row => {
            const text = row.textContent.toLowerCase();
            row.style.display = text.includes(searchTerm) ? '' : 'none';
        });
    }
    
    function filterByStatus(status) {
        const rows = document.querySelectorAll('.issues-table tbody tr');
        rows.forEach(row => {
            if (status === 'all') {
                row.style.display = '';
            } else if (status === 'open') {
                row.style.display = row.textContent.includes('ðŸŸ¢ Open') ? '' : 'none';
            } else if (status === 'closed') {
                row.style.display = row.textContent.includes('ðŸ”´ Closed') ? '' : 'none';
            }
        });
    }
});
</script>

<div class="table-view">
    <div class="scroll-indicator">
        <span>â† Scroll horizontally to view all columns â†’</span>
    </div>
    <div class="table-container">
        <table class="issues-table">
        <thead>
            <tr>
                <th>Issue #</th>
                <th>Title</th>
                <th>Description</th>
                <th>Project</th>
                <th>Assignee</th>
                <th>Created</th>
                <th>Status</th>
                <th>Links</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><span class="issue-number">#11</span></td>
                <td><a href="issues/11-clean-up-atlas/" class="issue-link">clean up atlas</a></td>
                <td>No description provided</td>
                <td>atlas</td>
                <td><span class="assignee">nallasivamselvaraj</span></td>
                <td><span class="issue-date">Oct 5, 2025</span></td>
                <td><span class="status-badge status-open">ðŸŸ¢ Open</span></td>
                <td><a href="https://github.com/Simtestlab/atlas/issues/11" class="github-link" target="_blank" rel="noopener">GitHub â†—</a></td>
            </tr>
            <tr>
                <td><span class="issue-number">#10</span></td>
                <td><a href="issues/10-publish-github-organization-issues-in-mkdocs/" class="issue-link">Publish GitHub Organization Issues in MkDocs</a></td>
                <td>
                    <div class="expand-description" id="desc-10">
                        <span class="description-short">User Story: Publish GitHub Organization Issues in MkDocs. As a team member, I want to automatically publish all GitHub issues...</span>
                        <span class="description-full">User Story: Publish GitHub Organization Issues in MkDocs. As a team member, I want to automatically publish all GitHub issues from our organization into MkDocs so that the documentation site always reflects the latest issues. Currently, issues from our GitHub repositories are scattered and hard to track in our documentation. We want to automate the process of fetching all issues from all repositories in the organization and generating markdown files that can be rendered by MkDocs.</span>
                        <span class="read-more-btn" onclick="toggleDescription('desc-10')">Read More</span>
                        <span class="read-less-btn" onclick="toggleDescription('desc-10')">Read Less</span>
                    </div>
                </td>
                <td>atlas</td>
                <td><span class="assignee">nallasivamselvaraj</span></td>
                <td><span class="issue-date">Oct 5, 2025</span></td>
                <td><span class="status-badge status-open">ðŸŸ¢ Open</span></td>
                <td><a href="https://github.com/Simtestlab/atlas/issues/10" class="github-link" target="_blank" rel="noopener">GitHub â†—</a></td>
            </tr>
            <tr>
                <td><span class="issue-number">#8</span></td>
                <td><a href="issues/8-fix-submodule-to-point-to-main/" class="issue-link">fix submodule to point to main</a></td>
                <td>add other submodules to atlas</td>
                <td>atlas</td>
                <td><span class="assignee">aeroramesh</span></td>
                <td><span class="issue-date">Oct 5, 2025</span></td>
                <td><span class="status-badge status-closed">ðŸ”´ Closed</span></td>
                <td><a href="https://github.com/Simtestlab/atlas/issues/8" class="github-link" target="_blank" rel="noopener">GitHub â†—</a></td>
            </tr>
        </tbody>
    </table>
    </div>
</div>
