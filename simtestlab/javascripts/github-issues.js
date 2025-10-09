// GitHub Issues Table Configuration
const TableConfig = {
    columns: {
        taskNumber: { width: '8%', align: 'center', label: 'Task #' },
        title: { width: '15%', align: 'left', label: 'Title' },
        description: { width: '35%', align: 'left', label: 'Description' },
        project: { width: '10%', align: 'center', label: 'Project' },
        assignee: { width: '12%', align: 'center', label: 'Assignee' },
        created: { width: '10%', align: 'center', label: 'Created' },
        status: { width: '8%', align: 'center', label: 'Status' },
        urlLink: { width: '12%', align: 'center', label: 'URL Link' }
    },
    styling: {
        centerTable: true,
        showBorders: true,
        alternateRows: true,
        hoverEffect: true
    }
};

// Apply table configuration
function applyTableConfig() {
    const table = document.querySelector('.issues-table');
    if (!table) return;
    
    // Apply column widths and alignment
    Object.keys(TableConfig.columns).forEach((key, index) => {
        const colIndex = index + 1;
        const config = TableConfig.columns[key];
        
        // Apply to headers
        const th = table.querySelector(`th:nth-child(${colIndex})`);
        if (th) {
            th.style.width = config.width;
            th.style.textAlign = config.align;
        }
        
        // Apply to cells
        const tds = table.querySelectorAll(`td:nth-child(${colIndex})`);
        tds.forEach(td => {
            td.style.textAlign = config.align;
        });
    });
}

// GitHub Issues Table Read More/Less Functionality
function toggleDescription(id) {
    const element = document.getElementById(id);
    if (element) {
        element.classList.toggle('expanded');
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Apply table configuration
    applyTableConfig();
    
    // Make sure all read more buttons are functional
    const readMoreBtns = document.querySelectorAll('.read-more-btn');
    const readLessBtns = document.querySelectorAll('.read-less-btn');
    
    readMoreBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const descId = this.onclick.toString().match(/desc-\d+/)[0];
            toggleDescription(descId);
        });
    });
    
    readLessBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const descId = this.onclick.toString().match(/desc-\d+/)[0];
            toggleDescription(descId);
        });
    });
});