# Issue #308: Branch API

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2025-07-13  
**Updated:** 2025-08-26  
**Closed:** 2025-08-26  
**Author:** @nallasivamselvaraj  
**Assignees:** @nallasivamselvaraj  
**Labels:** `API Call`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/308)

## Description


# Branch API 



## 1. Implemented Endpoints

### 1.1 Create Branch

- **Method:** `POST`  
- **Endpoint:** `/api/branch`  
- **Description:** Creates a new branch under a specified project.

#### Request Body

| Parameter         | Type   | Required | Description                                  |
|-------------------|--------|----------|----------------------------------------------|
| `branch_name`     | string | Yes      | Name of the branch to be created             |
| `project_id`      | string | Yes      | ID of the project where the branch belongs   |
| `origin_id`       | string | No       | ID of the origin branch (if any)             |
| `status`          | string | No       | Initial status of the branch                 |
| `current_user_id` | string | No       | ID of the user initiating the request        |

#### Success Response

```json
{
  "message": "Branch created successfully",
  "data": {
    "branch": { ... },
    "version": { ... }
  }
}
```

#### Error Response

```json
{
  "error": "Description of the error"
}
```

---

### 1.2 List Branches

- **Method:** `GET`  
- **Endpoint:** `/api/branch?project_id=...`  
- **Description:** Retrieves all branches for a specified project.

#### Query Parameters

| Parameter     | Type   | Required | Description                 |
|---------------|--------|----------|-----------------------------|
| `project_id`  | string | Yes      | ID of the target project    |

#### Success Response

```json
{
  "project_name": "Example Project",
  "branches": [ ... ]
}
```

#### Error Response

```json
{
  "error": "Description of the error"
}
```

---

### 1.3 Get Branch Details

- **Method:** `GET`  
- **Endpoint:** `/api/branch?project_id=...&branch_id=...`  
- **Description:** Retrieves metadata for a specific branch in a project.

#### Query Parameters

| Parameter     | Type   | Required | Description                 |
|---------------|--------|----------|-----------------------------|
| `project_id`  | string | Yes      | ID of the project           |
| `branch_id`   | string | Yes      | ID of the target branch     |

#### Success Response

```json
{
  "branches": [ ... ]
}
```

#### Error Response

```json
{
  "error": "Description of the error"
}
```

---

## 2. Proposed Endpoints

### 2.1 Update Branch

- **Method:** `PATCH`  
- **Endpoint:** `/api/branch`  
- **Description:** Updates details of an existing branch such as its name or status.

#### Request Body

| Parameter     | Type   | Required | Description                         |
|---------------|--------|----------|-------------------------------------|
| `branch_id`   | string | Yes      | ID of the branch to be updated      |
| `branch_name` | string | No       | New name for the branch             |
| `status`      | string | No       | New status for the branch           |

#### Success Response

```json
{
  "message": "Branch updated successfully",
  "branch": { ... }
}
```

#### Error Response

```json
{
  "error": "Description of the error"
}
```

---

### 2.2 Delete Branch

- **Method:** `DELETE`  
- **Endpoint:** `/api/branch?branch_id=...`  
- **Description:** Deletes a specified branch.

#### Query Parameters

| Parameter     | Type   | Required | Description             |
|---------------|--------|----------|-------------------------|
| `branch_id`   | string | Yes      | ID of the branch to delete |

#### Success Response

```json
{
  "message": "Branch deleted successfully"
}
```

#### Error Response

```json
{
  "error": "Description of the error"
}
```

---

### 2.3 List Branch Commits / Versions

- **Method:** `GET`  
- **Endpoint:** `/api/branch/commits?branch_id=...`  
- **Description:** Lists all commits or version history associated with a branch.

#### Query Parameters

| Parameter     | Type   | Required | Description               |
|---------------|--------|----------|---------------------------|
| `branch_id`   | string | Yes      | ID of the target branch   |

#### Success Response

```json
{
  "commits": [ ... ]
}
```

#### Error Response

```json
{
  "error": "Description of the error"
}
```

---

