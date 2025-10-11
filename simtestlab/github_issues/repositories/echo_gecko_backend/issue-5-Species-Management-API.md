# Issue #5: Species Management API

**Repository:** echo_gecko_backend  
**Status:** Closed  
**Created:** 2025-09-13  
**Updated:** 2025-09-17  
**Closed:** 2025-09-17  
**Author:** @harish-ramar  
**Assignees:** @nallasivamselvaraj  

[View on GitHub](https://github.com/Simtestlab/echo_gecko_backend/issues/5)

## Description

### 1. Get All Breeds

Endpoint: GET /breed/get_breeds

Description: Retrieves a list of all available breeds with their unique identifiers.

Parameters: None

Response:

200 OK - Breeds retrieved successfully  
{

	"breeds": [

	{

	"breed_id": "BR001",

	"breed_name": "Golden Retriever"

	},

	{

	"breed_id": "BR002",

	"breed_name": "Persian Cat"

	},

	{

	"breed_id": "BR003",

	"breed_name": "Bulldog"

	}

	],

	"total_count": 3

}

  

500 Internal Server Error - Database error  
{
	
	"error": "Unable to retrieve breeds",

	"message": "Internal server error occurred"

}

  

----------

### 2. Get Species by Breed

Endpoint: GET /species/get_species/{breed_id}

Description: Retrieves all species associated with a specific breed ID.

Parameters:

-   breed_id (path parameter, required): Unique identifier for the breed
    

Response:

200 OK - Species found for the breed  
{

	"breed_id": "BR001",

	"breed_name": "Golden Retriever",

	"species": [

	{

	"species_id": "SP001",

	"species_name": "Canine"

	}

	],

	"total_count": 1

}

  

404 Not Found - Breed not found  
{

	"error": "Breed not found",

	"message": "No breed exists with the provided ID"

}

  

400 Bad Request - Invalid breed ID format  
{

	"error": "Invalid breed ID format"

}

  

Notes

Data Relationships:

-   Each patient can have one bio data record.
    
-   Bio data links patients to specific breeds and species.
    
-   Breeds and species have a hierarchical relationship.