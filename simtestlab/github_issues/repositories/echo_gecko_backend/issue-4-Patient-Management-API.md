# Issue #4: Patient Management API

**Repository:** echo_gecko_backend  
**Status:** Closed  
**Created:** 2025-09-13  
**Updated:** 2025-09-16  
**Closed:** 2025-09-14  
**Author:** @harish-ramar  
**Assignees:** @nallasivamselvaraj  

[View on GitHub](https://github.com/Simtestlab/echo_gecko_backend/issues/4)

## Description

### 1. Check Patient Existence

Endpoint: GET /patient/check_patient_id/{patient_id}

Description: Validates if a patient with the specified ID exists in the system.

Parameters:

-   patient_id (path parameter, required): Unique identifier for the patient
    

Response:

200 OK - Patient found  
	{

	"exists": true,

	"patient_name": "John Doe"

}

  

404 Not Found - Patient not found  
{

	"exists": false,

	"message": "Patient not found"

}

  

400 Bad Request - Invalid patient ID format  
{

	"error": "Invalid patient ID format"

}


### 2. Create New Patient

Endpoint: POST /patient/new_patient

Description: Registers a new patient in the system. Automatically validates that the patient ID doesn't already exist before creation.

Request Body:

{

	"patient_id": "string",

	"patient_name": "string"

}

  

Validation Rules:

-   patient_id: Required, must be unique, alphanumeric
    
-   patient_name: Required, minimum 4 characters
    

Response:

201 Created - Patient successfully created  
	{

	"success": true,

	"message": "Patient registered successfully",

	"patient_id": "P12345"

}

  

409 Conflict - Patient ID already exists  
	{

	"success": false,

	"error": "Patient with this ID already exists"

}

  

400 Bad Request - Invalid input data  
{

	"success": false,

	"error": "Invalid input data",

	"details": ["patient_name is required", "patient_id must be alphanumeric"]

}

  

500 Internal Server Error - Database or server error  
{

	"success": false,

	"error": "Internal server error occurred"

}

----------

  

### 3. Create Patient Bio Data

Endpoint: POST /patient/bio_data/{patient_id}

Description: Creates bio data for a specific patient. All fields except weight are required.

Parameters:

-   patient_id (path parameter, required): Unique identifier for the patient
    

Request Body:

{

	"breed": "string",

	"species": "string",

	"gender": "string",

	"age": "number",

	"weight": "number" // optional

}

  

Here the reason for making weight optional is that the weight is used only for specific species (ex, Guinea Pig).

  
  

Validation Rules:

-   breed: Required, must be a valid breed ID or name
    
-   species: Required, must be a valid species ID or name
    
-   gender: Required, accepted values: ["Male", "Female", "Unknown"]
    
-   age: Required, must be a positive number
    
-   weight: Optional, must be a positive number if provided (in grams)
    

Response:

201 Created - Bio data successfully created  
{

	"success": true,

	"message": "Patient bio data created successfully",

	"patient_id": "P12345"

}

  

404 Not Found - Patient not found  
{

	"success": false,

	"error": "Patient not found"

}

  

409 Conflict - Bio data already exists  
{

	"success": false,

	"error": "Bio data already exists for this patient"

}

  

400 Bad Request - Invalid input data  
{

"success": false,

"error": "Invalid input data",

"details": ["breed is required", "age must be a positive number"]

}

  

----------

### 4. Get Patient Bio Data

Endpoint: GET /patient/bio_data/{patient_id}

Description: Retrieves bio data for a specific patient including breed, species, gender, age, and weight information.

Parameters:

-   patient_id (path parameter, required): Unique identifier for the patient
    

Response:

200 OK - Bio data found  
{

	"patient_id": "P12345",

	"breed": "Golden Retriever",

	"species": "Canine",

	"gender": "Male",

	"age": 5,

	"weight": 30.5,

	"last_updated": "2025-09-10T17:52:12Z"

}

  

404 Not Found - Patient or bio data not found  
{

"error": "Bio data not found",

"message": "No bio data exists for the provided patient ID"

}

  

400 Bad Request - Invalid patient ID format  
{

"error": "Invalid patient ID format"

}

  

----------

### 5. Update Patient Bio Data

Endpoint: PUT /patient/bio_data/{patient_id}

Description: Updates one or more bio data fields for a specific patient. Only provided fields will be updated.

Parameters:

-   patient_id (path parameter, required): Unique identifier for the patient
    

Request Body: (All fields optional - at least one must be provided)

{

	"breed": "string",

	"species": "string",

	"gender": "string",

	"age": "number",

	"weight": "number"

}

  

Validation Rules:

-   At least one field must be provided
    
-   gender: If provided, accepted values: ["Male", "Female", "Unknown"]
    
-   age: If provided, must be a positive number
    
-   weight: If provided, must be a positive number
    

Response:

200 OK - Bio data successfully updated  
{

	"success": true,

	"message": "Patient bio data updated successfully",

	"updated_fields": ["age", "weight"],

	"patient_id": "P12345"

}

  

404 Not Found - Patient or bio data not found  
{

"success": false,

"error": "Patient bio data not found"

}

  

400 Bad Request - Invalid input data or no fields provided  
{

"success": false,

"error": "Invalid input data",

"details": ["At least one field must be provided", "age must be positive"]

}

  

### 6. Get All Patients for a User

Endpoint: GET /patient/list?user_id={user_id}

Description: Fetch all patients that belong to a specific user. The response returns basic patient metadata that the Existing Patients page needs: patient ID, patient name, and last modified timestamp. By default only active (non-deleted) records are returned.

Response:

-   200 OK — list returned
    

{

	"user_id": "U12345",

	"total_count": 24,

	"patients": [

	{

	"patient_id": "1243567890",

	"patient_name": "Leo",

	"last_modified": "2025-05-12T13:12:00Z"

	},

	{

	"patient_id": "1243577891",

	"patient_name": "Lucy",

	"last_modified": "2025-05-09T05:17:00Z"

	}

	]

}

-   400 Bad Request — invalid parameters
    

{

	"error": "Invalid query parameters",

	"details": ["user_id is required"]

}

-   404 Not Found — no patients found
    

{

	"user_id": "U12345",

	"total_count": 0,

	"patients": []

}

-   500 Internal Server Error
    

{

"error": "Internal server error occurred"

}

  

Validation Rules & Notes:

-   user_id is required and should match the authenticated user's Firebase uid.
    
-   By default, only records with deleted_at = null are returned.
    
-   Ensure results are filtered by user_id to prevent cross-user data leakage.
    
-   Return timestamps in ISO 8601 (UTC).
    

### 7. Soft Delete Patient (set deleted_at)

Endpoint: DELETE /patient/bio_data/{patient_id}

Description: Soft-delete a patient's record by setting the deleted_at timestamp for that patient row (and/or related bio data row as applicable). The record remains in the database for retention/recovery (e.g., 30 days) and should not appear in normal list results. This endpoint does not permanently remove the record.

Path Parameters:

-   patient_id (path parameter, required): Unique identifier for the patient (string).
    

Behavior:

-   Validate that the patient exists and belongs to the authenticated user (user_id from auth context).
    
-   Update the patient record's deleted_at field to the current timestamp (UTC).
    
-   Return success only after the update is persisted.
    

Response:

-   200 OK — Soft-delete applied
    

{

	"success": true,

	"message": "Patient soft-deleted successfully",

	"patient_id": "1243567890",

	"deleted_at": "2025-09-12T12:00:00Z"

}

-   400 Bad Request — invalid patient id format
    

{

	"success": false,

	"error": "Invalid patient ID format"

}

-   403 Forbidden — user not authorized to delete this patient
    

{

	"success": false,

	"error": "Forbidden: user does not own the patient"

}

-   404 Not Found — patient not found
    

{

	"success": false,

	"error": "Patient not found"

}

-   500 Internal Server Error
    

{

	"success": false,

	"error": "Internal server error occurred"

}