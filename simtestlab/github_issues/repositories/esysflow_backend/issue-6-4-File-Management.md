# Issue #6: 4. File Management

**Repository:** esysflow_backend  
**Status:** Open  
**Created:** 2025-09-25  
**Updated:** 2025-10-05  
**Author:** @nallasivamselvaraj  
**Assignees:** @nallasivamselvaraj  

[View on GitHub](https://github.com/Simtestlab/esysflow_backend/issues/6)

## Description

# File Management 

## /api/file
- **Method**: GET
- **Parameters**:
  - `file_id`: Identifier for the file
  - `version_id`: Identifier for the specific version of the file


## /api/upload
- **Method**: POST
- **Request**: `multipart/form-data`
  - `file`: The file to be uploaded
  - `project_id`: Identifier for the associated project
  - `owner_id`: Identifier for the file owner
  - `branch_id`: Identifier for the branch


## /api/commit
- **Method**: POST
- **Description**: Commits file changes and creates a new version of the file
