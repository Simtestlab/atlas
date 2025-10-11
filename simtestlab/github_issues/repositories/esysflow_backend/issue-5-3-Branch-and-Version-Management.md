# Issue #5: 3. Branch and Version Management

**Repository:** esysflow_backend  
**Status:** Open  
**Created:** 2025-09-25  
**Updated:** 2025-10-05  
**Author:** @nallasivamselvaraj  
**Assignees:** @nallasivamselvaraj  

[View on GitHub](https://github.com/Simtestlab/esysflow_backend/issues/5)

## Description

## 3. Branch & Version Management

### /api/branch

**Methods**: GET, POST, PATCH

#### POST – Create Branch
```json
{
  "branch_name": "string",
  "project_id": "string",
  "origin_id": "string",
  "status": "string",
  "current_user_id": "string"
}
```

#### GET – List Branches
**Parameters**:
- `project_id` (required)
- `status` (optional)

#### PATCH – Rename Branch
```json
{
  "branch_id": "string",
  "new_branch_name": "string",
  "project_id": "string"
}
```

### /api/versions

**Methods**: GET

**Parameters**:
- `project_id`
- `branch_id`

**Description**: Get all versions for a branch

### /api/version

**Methods**: GET

**Description**: Retrieve specific version details