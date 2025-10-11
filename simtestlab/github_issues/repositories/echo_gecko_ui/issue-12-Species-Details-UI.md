# Issue #12: Species Details UI

**Repository:** echo_gecko_ui  
**Status:** Open  
**Created:** 2025-09-13  
**Updated:** 2025-09-18  
**Author:** @harish-ramar  
**Assignees:** @divya-rosy  
**Labels:** `UI/UX`  

[View on GitHub](https://github.com/Simtestlab/echo_gecko_ui/issues/12)

## Description

## Species Details

<img width="1143" height="1084" alt="Image" src="https://github.com/user-attachments/assets/d37a8a34-7d69-423d-a9b6-6d9d2f2358e8" />

### Overview

-   Rendered after New Patient or Existing Patient selection. Once a new patient is created or an existing patient is selected in the list.
    
-   Loads breed and species lists from the backend/database on every page load (ensures up-to-date data).
    
-   UI must support easy updating and editing of breed/species values via backend.

-   Breed Dropdown
-   Fetch breeds from /breed/get_breeds API.
-   Display breeds in a dropdown list.
-   Ensure dropdown expands without overlapping/colliding UI components.
-   Currently supports 3 values, but should be dynamic for future updates.
-   Species Dropdown
-   On breed selection, fetch species for that breed from /species/get_species/{breed_id} API.
-   Display species in a dropdown list.
-   Avatar Image (Choose Species)
-   Render a circular avatar image at the bottom of the screen, as per UI design. Which should render the 

### Species.
-   Avatar must be scrollable.
-   Mobile view: display up to 4 avatar images in the current viewport.
-   Gender Selection
-   Radio button group for gender (Male, Female).
-   Age and Weight
-   Input fields for age (required) and weight (optional).

### Navigation
-   Cancel Button
-   Navigates back to the Patient Page.
-   Scan Button
-   On click, collect all entered bio data and make an API call to update the database.
-   Use /patient/bio_data/{patient_id} endpoint (refer to API documentation for request/response structure).
-   Navigate to the next page only if the API call is successful.
-   Log API responses and errors to the console during development.

### API Calls
-   Load Breeds
-   Function to call /breed/get_breeds and populate breed dropdown.
-   Load Species
-   Function to call /species/get_species/{breed_id} based on selected breed and populate species dropdown.
-   Update Patient Bio Data
-   On the Scan button click, call /patient/bio_data/{patient_id} API with entered details.
-   Log API responses to console (match structure from API documentation).
-   Prevent navigation on error.
-   Implement all API calls as separate functions for maintainability. 
-   If API is unavailable, mock responses and log structure to the console.

### Notes

-   All API call logic should be modular and reusable.
-   Log all API responses to the console during development; remove logs before production.
-   UI should be responsive and support mobile viewport constraints.
-   Prevent navigation if API calls fail or return errors.

## UI

<img width="210" height="463" alt="Image" src="https://github.com/user-attachments/assets/9247a536-9141-4251-8ee3-992e560c37ae" />

