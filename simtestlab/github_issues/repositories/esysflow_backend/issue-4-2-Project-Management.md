# Issue #4: 2. Project Management

**Repository:** esysflow_backend  
**Status:** Open  
**Created:** 2025-09-25  
**Updated:** 2025-10-05  
**Author:** @nallasivamselvaraj  
**Assignees:** @nallasivamselvaraj  

[View on GitHub](https://github.com/Simtestlab/esysflow_backend/issues/4)

## Description

### Endpoint: `/api/project`

- **Method**: POST
- **Description**: Create a new project with a default "main" branch.
- **Body**:
  ```json
  {
    "project_name": "string",
    "owner_id": "string",
    "access": ["string"], // Array of user IDs with access
    "description": "string"
  }
  ```
- **Validation**: Project name must be 1-100 characters, no invalid characters, not a reserved name.
- **Response**:
  - **201 Created**:
    ```json
    {
      "project": {
        "id": "string",
        "name": "string",
        "owner_id": "string",
        "description": "string"
      },
      "branch": {
        "id": "string",
        "name": "main",
        "project_id": "string"
      }
    }
    ```
  - **400 Bad Request**: Invalid project name or parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **409 Conflict**: Project name already exists.
  - **500 Internal Server Error**: Server-side error.

- **Method**: GET
- **Description**: Get projects for a user or check project name availability.
- **Query Parameters**:
  - `user_id` (string, optional): Get projects for the specified user.
  - `check_name` (string, optional) & `owner_id` (string, optional): Check if project name is available.
- **Response**:
  - **200 OK** (List projects):
    ```json
    {
      "projects": [
        {
          "id": "string",
          "name": "string",
          "owner_id": "string",
          "description": "string"
        }
      ]
    }
    ```
  - **200 OK** (Check name availability):
    ```json
    {
      "available": boolean,
      "suggestions": ["string"]
    }
    ```
  - **400 Bad Request**: Invalid query parameters.
  - **401 Unauthorized**: Authentication required.
  - **500 Internal Server Error**: Server-side error.

- **Method**: PATCH
- **Description**: Update project details (rename, change description, add user access).
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string", // Optional
    "new_description": "string", // Optional
    "new_name": "string" // Optional
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "project": {
        "id": "string",
        "name": "string",
        "description": "string"
      }
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project not found.
  - **409 Conflict**: New name already exists.
  - **500 Internal Server Error**: Server-side error.

- **Method**: DELETE
- **Description**: Delete a project (owner only). Cascades to delete versions and branches.
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "Project deleted successfully"
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project not found.
  - **500 Internal Server Error**: Server-side error.

### Endpoint: `/api/project/members`

- **Method**: GET
- **Description**: Get project members.
- **Query Parameters**:
  - `project_id` (string, required): Project ID.
- **Response**:
  - **200 OK**:
    ```json
    {
      "members": [
        {
          "id": "string",
          "name": "string",
          "email": "string"
        }
      ]
    }
    ```
  - **400 Bad Request**: Missing project_id.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project not found.
  - **500 Internal Server Error**: Server-side error.

### Endpoint: `/api/project-members`

- **Method**: GET
- **Description**: Get project members with roles.
- **Query Parameters**:
  - `project_id` (string, required): Project ID.
- **Response**:
  - **200 OK**:
    ```json
    {
      "members": [
        {
          "id": "string",
          "name": "string",
          "role": "string" // e.g., admin, maintainer, developer
        }
      ]
    }
    ```
  - **400 Bad Request**: Missing project_id.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project not found.
  - **500 Internal Server Error**: Server-side error.

- **Method**: POST
- **Description**: Add a member to a project.
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string",
    "role": "string" // e.g., admin, maintainer, developer
  }
  ```
- **Response**:
  - **201 Created**:
    ```json
    {
      "message": "Member added successfully"
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project or user not found.
  - **500 Internal Server Error**: Server-side error.

- **Method**: PATCH
- **Description**: Update a member’s role in a project.
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string",
    "role": "string" // e.g., admin, maintainer, developer
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "Role updated successfully"
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project or user not found.
  - **500 Internal Server Error**: Server-side error.

- **Method**: DELETE
- **Description**: Remove a member from a project.
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "Member removed successfully"
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project or user not found.
  - **500 Internal Server Error**: Server-side error.### Endpoint: `/api/project`

- **Method**: POST
- **Description**: Create a new project with a default "main" branch.
- **Body**:
  ```json
  {
    "project_name": "string",
    "owner_id": "string",
    "access": ["string"], // Array of user IDs with access
    "description": "string"
  }
  ```
- **Validation**: Project name must be 1-100 characters, no invalid characters, not a reserved name.
- **Response**:
  - **201 Created**:
    ```json
    {
      "project": {
        "id": "string",
        "name": "string",
        "owner_id": "string",
        "description": "string"
      },
      "branch": {
        "id": "string",
        "name": "main",
        "project_id": "string"
      }
    }
    ```
  - **400 Bad Request**: Invalid project name or parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **409 Conflict**: Project name already exists.
  - **500 Internal Server Error**: Server-side error.

- **Method**: GET
- **Description**: Get projects for a user or check project name availability.
- **Query Parameters**:
  - `user_id` (string, optional): Get projects for the specified user.
  - `check_name` (string, optional) & `owner_id` (string, optional): Check if project name is available.
- **Response**:
  - **200 OK** (List projects):
    ```json
    {
      "projects": [
        {
          "id": "string",
          "name": "string",
          "owner_id": "string",
          "description": "string"
        }
      ]
    }
    ```
  - **200 OK** (Check name availability):
    ```json
    {
      "available": boolean,
      "suggestions": ["string"]
    }
    ```
  - **400 Bad Request**: Invalid query parameters.
  - **401 Unauthorized**: Authentication required.
  - **500 Internal Server Error**: Server-side error.

- **Method**: PATCH
- **Description**: Update project details (rename, change description, add user access).
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string", // Optional
    "new_description": "string", // Optional
    "new_name": "string" // Optional
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "project": {
        "id": "string",
        "name": "string",
        "description": "string"
      }
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project not found.
  - **409 Conflict**: New name already exists.
  - **500 Internal Server Error**: Server-side error.

- **Method**: DELETE
- **Description**: Delete a project (owner only). Cascades to delete versions and branches.
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "Project deleted successfully"
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project not found.
  - **500 Internal Server Error**: Server-side error.

### Endpoint: `/api/project/members`

- **Method**: GET
- **Description**: Get project members.
- **Query Parameters**:
  - `project_id` (string, required): Project ID.
- **Response**:
  - **200 OK**:
    ```json
    {
      "members": [
        {
          "id": "string",
          "name": "string",
          "email": "string"
        }
      ]
    }
    ```
  - **400 Bad Request**: Missing project_id.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project not found.
  - **500 Internal Server Error**: Server-side error.

### Endpoint: `/api/project-members`

- **Method**: GET
- **Description**: Get project members with roles.
- **Query Parameters**:
  - `project_id` (string, required): Project ID.
- **Response**:
  - **200 OK**:
    ```json
    {
      "members": [
        {
          "id": "string",
          "name": "string",
          "role": "string" // e.g., admin, maintainer, developer
        }
      ]
    }
    ```
  - **400 Bad Request**: Missing project_id.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project not found.
  - **500 Internal Server Error**: Server-side error.

- **Method**: POST
- **Description**: Add a member to a project.
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string",
    "role": "string" // e.g., admin, maintainer, developer
  }
  ```
- **Response**:
  - **201 Created**:
    ```json
    {
      "message": "Member added successfully"
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project or user not found.
  - **500 Internal Server Error**: Server-side error.

- **Method**: PATCH
- **Description**: Update a member’s role in a project.
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string",
    "role": "string" // e.g., admin, maintainer, developer
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "Role updated successfully"
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project or user not found.
  - **500 Internal Server Error**: Server-side error.

- **Method**: DELETE
- **Description**: Remove a member from a project.
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "Member removed successfully"
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project or user not found.
  - **500 Internal Server Error**: Server-side error.### Endpoint: `/api/project`

- **Method**: POST
- **Description**: Create a new project with a default "main" branch.
- **Body**:
  ```json
  {
    "project_name": "string",
    "owner_id": "string",
    "access": ["string"], // Array of user IDs with access
    "description": "string"
  }
  ```
- **Validation**: Project name must be 1-100 characters, no invalid characters, not a reserved name.
- **Response**:
  - **201 Created**:
    ```json
    {
      "project": {
        "id": "string",
        "name": "string",
        "owner_id": "string",
        "description": "string"
      },
      "branch": {
        "id": "string",
        "name": "main",
        "project_id": "string"
      }
    }
    ```
  - **400 Bad Request**: Invalid project name or parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **409 Conflict**: Project name already exists.
  - **500 Internal Server Error**: Server-side error.

- **Method**: GET
- **Description**: Get projects for a user or check project name availability.
- **Query Parameters**:
  - `user_id` (string, optional): Get projects for the specified user.
  - `check_name` (string, optional) & `owner_id` (string, optional): Check if project name is available.
- **Response**:
  - **200 OK** (List projects):
    ```json
    {
      "projects": [
        {
          "id": "string",
          "name": "string",
          "owner_id": "string",
          "description": "string"
        }
      ]
    }
    ```
  - **200 OK** (Check name availability):
    ```json
    {
      "available": boolean,
      "suggestions": ["string"]
    }
    ```
  - **400 Bad Request**: Invalid query parameters.
  - **401 Unauthorized**: Authentication required.
  - **500 Internal Server Error**: Server-side error.

- **Method**: PATCH
- **Description**: Update project details (rename, change description, add user access).
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string", // Optional
    "new_description": "string", // Optional
    "new_name": "string" // Optional
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "project": {
        "id": "string",
        "name": "string",
        "description": "string"
      }
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project not found.
  - **409 Conflict**: New name already exists.
  - **500 Internal Server Error**: Server-side error.

- **Method**: DELETE
- **Description**: Delete a project (owner only). Cascades to delete versions and branches.
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "Project deleted successfully"
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project not found.
  - **500 Internal Server Error**: Server-side error.

### Endpoint: `/api/project/members`

- **Method**: GET
- **Description**: Get project members.
- **Query Parameters**:
  - `project_id` (string, required): Project ID.
- **Response**:
  - **200 OK**:
    ```json
    {
      "members": [
        {
          "id": "string",
          "name": "string",
          "email": "string"
        }
      ]
    }
    ```
  - **400 Bad Request**: Missing project_id.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project not found.
  - **500 Internal Server Error**: Server-side error.

### Endpoint: `/api/project-members`

- **Method**: GET
- **Description**: Get project members with roles.
- **Query Parameters**:
  - `project_id` (string, required): Project ID.
- **Response**:
  - **200 OK**:
    ```json
    {
      "members": [
        {
          "id": "string",
          "name": "string",
          "role": "string" // e.g., admin, maintainer, developer
        }
      ]
    }
    ```
  - **400 Bad Request**: Missing project_id.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project not found.
  - **500 Internal Server Error**: Server-side error.

- **Method**: POST
- **Description**: Add a member to a project.
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string",
    "role": "string" // e.g., admin, maintainer, developer
  }
  ```
- **Response**:
  - **201 Created**:
    ```json
    {
      "message": "Member added successfully"
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project or user not found.
  - **500 Internal Server Error**: Server-side error.

- **Method**: PATCH
- **Description**: Update a member’s role in a project.
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string",
    "role": "string" // e.g., admin, maintainer, developer
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "Role updated successfully"
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project or user not found.
  - **500 Internal Server Error**: Server-side error.

- **Method**: DELETE
- **Description**: Remove a member from a project.
- **Body**:
  ```json
  {
    "project_id": "string",
    "user_id": "string"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "Member removed successfully"
    }
    ```
  - **400 Bad Request**: Invalid parameters.
  - **401 Unauthorized**: Authentication required.
  - **403 Forbidden**: Insufficient permissions.
  - **404 Not Found**: Project or user not found.
  - **500 Internal Server Error**: Server-side error.