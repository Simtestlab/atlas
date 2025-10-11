/**
 * GitHub-style table filtering for issue tables
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize filters for all issue tables
    initializeIssueTableFilters();
});

function initializeIssueTableFilters() {
    const tables = document.querySelectorAll('.github-issue-table');
    tables.forEach(table => {
        addFiltersToTable(table);
    });
}

function addFiltersToTable(table) {
    const container = table.parentElement;
    
    // Create filter controls container
    const filterContainer = document.createElement('div');
    filterContainer.className = 'issue-filters';
    filterContainer.innerHTML = createFilterHTML();
    
    // Insert filters before the table
    container.insertBefore(filterContainer, table);
    
    // Add event listeners
    setupFilterEventListeners(filterContainer, table);
    
    // Initialize filter state
    updateFilterCounts(table);
}

function createFilterHTML() {
    return `
        <div class="filter-controls">
            <div class="filter-group">
                <button class="filter-btn active" data-filter="all">
                    <span class="filter-icon">📄</span>
                    <span class="filter-count" data-count="all">0</span> All
                </button>
                <button class="filter-btn" data-filter="open">
                    <span class="filter-icon">🟢</span>
                    <span class="filter-count" data-count="open">0</span> Open
                </button>
                <button class="filter-btn" data-filter="closed">
                    <span class="filter-icon">🔴</span>
                    <span class="filter-count" data-count="closed">0</span> Closed
                </button>
            </div>
            
            <div class="filter-group">
                <div class="search-container">
                    <input type="text" class="search-input" placeholder="Search issues..." />
                    <span class="search-icon">🔍</span>
                </div>
            </div>
            
            <div class="filter-group">
                <select class="assignee-filter" data-filter="assignee">
                    <option value="">All assignees</option>
                </select>
                <select class="label-filter" data-filter="label">
                    <option value="">All labels</option>
                </select>
                <select class="repository-filter" data-filter="repository">
                    <option value="">All repositories</option>
                </select>
            </div>
            
            <div class="filter-group">
                <select class="sort-select">
                    <option value="updated-desc">Recently updated</option>
                    <option value="updated-asc">Least recently updated</option>
                    <option value="created-desc">Newest</option>
                    <option value="created-asc">Oldest</option>
                    <option value="title-asc">Title A-Z</option>
                    <option value="title-desc">Title Z-A</option>
                </select>
            </div>
        </div>
    `;
}

function setupFilterEventListeners(filterContainer, table) {
    // Status filter buttons
    const statusButtons = filterContainer.querySelectorAll('.filter-btn[data-filter]');
    statusButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            statusButtons.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            btn.classList.add('active');
            
            applyFilters(filterContainer, table);
        });
    });
    
    // Search input
    const searchInput = filterContainer.querySelector('.search-input');
    searchInput.addEventListener('input', debounce(() => {
        applyFilters(filterContainer, table);
    }, 300));
    
    // Dropdown filters
    const dropdownFilters = filterContainer.querySelectorAll('select[data-filter]');
    dropdownFilters.forEach(select => {
        select.addEventListener('change', () => {
            applyFilters(filterContainer, table);
        });
    });
    
    // Sort select
    const sortSelect = filterContainer.querySelector('.sort-select');
    sortSelect.addEventListener('change', () => {
        applyFilters(filterContainer, table);
    });
    
    // Populate dropdown options
    populateDropdownOptions(filterContainer, table);
}

function populateDropdownOptions(filterContainer, table) {
    const rows = Array.from(table.querySelectorAll('tbody tr'));
    
    // Collect unique assignees, labels, and repositories
    const assignees = new Set();
    const labels = new Set();
    const repositories = new Set();
    
    rows.forEach(row => {
        const assigneeCell = row.cells[4]?.textContent.trim();
        const labelCell = row.cells[5]?.textContent.trim();
        const repositoryCell = row.cells[1]?.textContent.trim();
        
        if (assigneeCell && assigneeCell !== '-') {
            assigneeCell.split(',').forEach(assignee => {
                assignees.add(assignee.trim().replace(/\+\d+$/, ''));
            });
        }
        
        if (labelCell && labelCell !== '-') {
            labelCell.split(',').forEach(label => {
                labels.add(label.trim().replace(/\+\d+$/, ''));
            });
        }
        
        if (repositoryCell) {
            repositories.add(repositoryCell);
        }
    });
    
    // Populate assignee dropdown
    const assigneeSelect = filterContainer.querySelector('.assignee-filter');
    assignees.forEach(assignee => {
        const option = document.createElement('option');
        option.value = assignee;
        option.textContent = assignee;
        assigneeSelect.appendChild(option);
    });
    
    // Populate label dropdown
    const labelSelect = filterContainer.querySelector('.label-filter');
    labels.forEach(label => {
        const option = document.createElement('option');
        option.value = label;
        option.textContent = label;
        labelSelect.appendChild(option);
    });
    
    // Populate repository dropdown
    const repositorySelect = filterContainer.querySelector('.repository-filter');
    repositories.forEach(repository => {
        const option = document.createElement('option');
        option.value = repository;
        option.textContent = repository;
        repositorySelect.appendChild(option);
    });
}

function applyFilters(filterContainer, table) {
    const rows = Array.from(table.querySelectorAll('tbody tr'));
    
    // Get filter values
    const activeStatusFilter = filterContainer.querySelector('.filter-btn.active')?.dataset.filter;
    const searchTerm = filterContainer.querySelector('.search-input').value.toLowerCase();
    const assigneeFilter = filterContainer.querySelector('.assignee-filter').value;
    const labelFilter = filterContainer.querySelector('.label-filter').value;
    const repositoryFilter = filterContainer.querySelector('.repository-filter').value;
    const sortBy = filterContainer.querySelector('.sort-select').value;
    
    // Filter rows
    let filteredRows = rows.filter(row => {
        // Status filter
        if (activeStatusFilter !== 'all') {
            const statusCell = row.cells[0]?.textContent.toLowerCase();
            const isOpen = statusCell.includes('open');
            if (activeStatusFilter === 'open' && !isOpen) return false;
            if (activeStatusFilter === 'closed' && isOpen) return false;
        }
        
        // Search filter
        if (searchTerm) {
            const rowText = Array.from(row.cells).map(cell => cell.textContent.toLowerCase()).join(' ');
            if (!rowText.includes(searchTerm)) return false;
        }
        
        // Assignee filter
        if (assigneeFilter) {
            const assigneeText = row.cells[4]?.textContent || '';
            if (!assigneeText.includes(assigneeFilter)) return false;
        }
        
        // Label filter
        if (labelFilter) {
            const labelText = row.cells[5]?.textContent || '';
            if (!labelText.includes(labelFilter)) return false;
        }
        
        // Repository filter
        if (repositoryFilter) {
            const repositoryText = row.cells[1]?.textContent || '';
            if (repositoryText !== repositoryFilter) return false;
        }
        
        return true;
    });
    
    // Sort rows
    filteredRows = sortRows(filteredRows, sortBy);
    
    // Hide all rows first
    rows.forEach(row => {
        row.style.display = 'none';
    });
    
    // Show filtered rows
    filteredRows.forEach((row, index) => {
        row.style.display = '';
        // Move to correct position
        table.querySelector('tbody').appendChild(row);
    });
    
    // Update filter counts
    updateFilterCounts(table, filteredRows);
}

function sortRows(rows, sortBy) {
    return rows.sort((a, b) => {
        switch (sortBy) {
            case 'updated-desc':
                return new Date(b.cells[5]?.textContent) - new Date(a.cells[5]?.textContent);
            case 'updated-asc':
                return new Date(a.cells[5]?.textContent) - new Date(b.cells[5]?.textContent);
            case 'title-asc':
                return (a.cells[2]?.textContent || '').localeCompare(b.cells[2]?.textContent || '');
            case 'title-desc':
                return (b.cells[2]?.textContent || '').localeCompare(a.cells[2]?.textContent || '');
            default:
                return 0;
        }
    });
}

function updateFilterCounts(table, filteredRows = null) {
    const allRows = Array.from(table.querySelectorAll('tbody tr'));
    const visibleRows = filteredRows || allRows.filter(row => row.style.display !== 'none');
    
    const openCount = visibleRows.filter(row => 
        row.cells[0]?.textContent.toLowerCase().includes('open')
    ).length;
    
    const closedCount = visibleRows.filter(row => 
        row.cells[0]?.textContent.toLowerCase().includes('closed')
    ).length;
    
    // Update counts in filter buttons
    const filterContainer = table.previousElementSibling;
    if (filterContainer && filterContainer.classList.contains('issue-filters')) {
        const allCountSpan = filterContainer.querySelector('[data-count="all"]');
        const openCountSpan = filterContainer.querySelector('[data-count="open"]');
        const closedCountSpan = filterContainer.querySelector('[data-count="closed"]');
        
        if (allCountSpan) allCountSpan.textContent = visibleRows.length;
        if (openCountSpan) openCountSpan.textContent = openCount;
        if (closedCountSpan) closedCountSpan.textContent = closedCount;
    }
}

// Utility function for debouncing
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}