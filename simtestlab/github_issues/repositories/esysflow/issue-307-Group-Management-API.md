# Issue #307: Group Management API

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-07-13  
**Updated:** 2025-08-26  
**Author:** @harish-ramar  
**Assignees:** @harish-ramar  
**Labels:** `API Call`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/307)

## Description


# Group Management API Documentation

## Overview
Secure API for group management with separate creation and update operations. All endpoints require admin privileges.

---

## API Endpoints

### Base URL
```
/api/groups
```

---

### 1. Group Operations

#### Create Group
```http
POST /api/groups
```

**Request Body**:
```json
{
  "name": "string (required, unique)",
  "description": "string",
  "users": ["userId1", "userId2"]
}
```

**Validation**:
- Rejects if group name exists
- Verifies all users exist in system
- Ensures no duplicate users in request

**Response**:
```json
201 Created
{
  "id": "string",
  "name": "string",
  "description": "string",
  "createdAt": "ISO-8601 datetime",
  "users": ["userId1", "userId2"]
}
```

---

#### Update Group Metadata
```http
PATCH /api/groups/{groupId}
```

**Request Body**:
```json
{
  "name": "string",
  "description": "string (optional)"
}
```

**Notes**:
- At name field required
- Name changes are checked for uniqueness
- Does not affect group membership

**Response**:
```json
200 OK
{
  "id": "string",
  "name": "string",
  "description": "string",
  "updatedAt": "ISO-8601 datetime"
}
```

---

#### Delete Group
```http
DELETE /api/groups/{groupId}
```

**Response**: `204 No Content`

---

### 2. Membership Operations

#### Add Users to Group
```http
POST /api/groups/{groupId}/users
```

**Request Body**:
```json
{
  "userIds": ["userId1", "userId2"]
}
```

**Validation**:
- Rejects if any user already in group
- Verifies all users exist
- Returns error if group doesn't exist

**Response**:
```json
200 OK
{
  "addedUsers": ["userId1", "userId2"],
  "failedAdds": []
}
```

---

#### Remove Users from Group
```http
DELETE /api/groups/{groupId}/users
```

**Request Body**:
```json
{
  "userIds": ["userId1", "userId2"]
}
```

**Response**:
```json
200 OK
{
  "removedUsers": ["userId1", "userId2"],
  "failedRemovals": []
}
```

---

#### List Group Users
```http
GET /api/groups/{groupId}/users
```

**Query Params**:
- `limit`: number (default: 50)
- `offset`: number (default: 0)

**Response**:
```json
200 OK
{
  "users": [
    {
      "id": "string",
      "name": "string",
      "email": "string",
      "joinedAt": "ISO-8601 datetime"
    }
  ],
  "total": number
}
```

---

### 3. Group Listing

#### List All Groups
```http
GET /api/groups
```

**Query Params**:
- `search`: string (name filter)
- `sort`: "name"|"createdAt"|"userCount"
- `order`: "asc"|"desc"

**Response**:
```json
200 OK
{
  "groups": [
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "userCount": number
    }
  ],
  "total": number
}
```

---