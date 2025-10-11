# Issue #305: project management api

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2025-07-13  
**Updated:** 2025-07-25  
**Closed:** 2025-07-25  
**Author:** @nallasivamselvaraj  
**Assignees:** @nallasivamselvaraj  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/305)

## Description

### Implemented and suggested API


# Project Management API



----------

## Available Endpoints

### 1. Create a Project

-   **Method**: `POST`
    
-   **Endpoint**: `/api/project`
    
-   **Description**: Creates a new project instance.
    

----------

### 2. Retrieve All Projects

-   **Method**: `GET`
    
-   **Endpoint**: `/api/project`
    
-   **Description**: Fetches a list of all projects associated with the authenticated user.
    

----------

### 3. Update Project

-   **Method**: `PATCH`
    
-   **Endpoint**: `/api/project`
    
-   **Description**: Updates project information, such as adding users to the project's access control list.
    

----------

## Upcoming Endpoints

### 4. Delete a Project

-   **Method**: `DELETE`
    
-   **Endpoint**: `/api/project`
    
-   **Description**: Permanently deletes a project along with all its branches and version history.
    
-   **Request Body**:
    
    ```json
    {
      "project_id": "123456",
      "owner_id": "1234560",
      "Admin_id": "123456"
    }
    
    ```
    

----------

### 5. Get Project by ID

-   **Method**: `GET`
    
-   **Endpoint**: `/api/project?project_id=123456`
    
-   **Description**: Retrieves detailed information for a specific project by its unique ID.
    
-   **Request Body**:
    
    ```json
    {
      "project_id": "123456",
      "owner_id": "1234560"
    }
    
    ```
    

----------

### 6. Update Project Metadata

-   **Method**: `PATCH`
    
-   **Endpoint**: `/api/project`
    
-   **Description**: Enhances the existing update functionality to support editing metadata such as the project’s name and description.
    
-   **Request Body Example**:
    
    ```json
    {
      "project_id": "123456",
      "owner_id": "123456"
      "name": "New Project Name",
      "description": "Updated project description"
    }
    
    ```
    

----------

### 7. List Project Members

-   **Method**: `GET`
    
-   **Endpoint**: `/api/project/members?project_id=123456`
    
-   **Description**: Returns a list of all users who have access to the specified project.
    
-   **Query Parameters**:
    
    -   `project_id` (required): The unique identifier of the project.
        

----------
