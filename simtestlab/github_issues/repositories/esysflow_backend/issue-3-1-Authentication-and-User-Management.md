# Issue #3: 1. Authentication and User Management

**Repository:** esysflow_backend  
**Status:** Open  
**Created:** 2025-09-25  
**Updated:** 2025-09-25  
**Author:** @nallasivamselvaraj  

[View on GitHub](https://github.com/Simtestlab/esysflow_backend/issues/3)

## Description


## 1. Authentication and User Management

### `/api/auth/[...nextauth]`

- **Methods:** `GET`, `POST`
- **Description:** Handles OAuth authentication, session management, and login/logout flows.
- **Features:** Multiple providers, dynamic callbacks, session management via NextAuth.js.

### `/api/users`

- **Methods:** `GET`
- **Description:** Retrieve users with search, pagination, and filtering.
- **Parameters:**

| Parameter      | Type    | Required | Description                            |
|----------------|---------|----------|----------------------------------------|
| search         | string  | No       | Search by name/email                   |
| limit          | integer | No       | Number of users returned (default 50) |
| offset         | integer | No       | Number of users skipped (default 0)   |
| include_email  | boolean | No       | Include email in response (default false) |

- **Response Example:**

```json
{
  "data": [
    {
      "id": "1",
      "name": "Alice",
      "email": "alice@example.com"
    },
    {
      "id": "2",
      "name": "Bob",
      "email": "bob@example.com"
    }
  ],
  "pagination": {
    "total": 100,
    "limit": 50,
    "offset": 0
  }
}
