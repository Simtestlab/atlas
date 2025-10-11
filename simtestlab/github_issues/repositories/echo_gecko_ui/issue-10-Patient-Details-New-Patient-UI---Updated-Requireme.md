# Issue #10: Patient Details (New Patient) UI - Updated Requirement

**Repository:** echo_gecko_ui  
**Status:** Closed  
**Created:** 2025-09-13  
**Updated:** 2025-09-18  
**Closed:** 2025-09-18  
**Author:** @harish-ramar  
**Assignees:** @divya-rosy  
**Labels:** `UI/UX`  

[View on GitHub](https://github.com/Simtestlab/echo_gecko_ui/issues/10)

## Description

## Task Overview

-   Rendered when the New Patient button is clicked on the Patient Page #6 
    
-   Allows users to enter Patient Name and Patient ID.
    

Field Requirements

-   Patient Name
-   Text field, required.
-   Patient ID
-   Text field, required.
-   Validation: Must be exactly 10 digits, numeric only (no characters).
-   Implement validation as a separate, reusable function for future configurability. As the patient ID hasn't been finalized yet so make it more configurable.

Navigation

-   Back Button:  
    Navigates back to the Patient Page.
-   Next Button:  
    On click:
    
-   Call /patient/new_patient API to create the patient.
-   On success, navigate to the Species Details page.
-   On error, log the response and remain on the current page.
    
API Calls
-   Patient ID Check:  
    When a user enters Patient ID (on field change/blur), call /patient/check_patient_id/{patient_id} API to verify if the ID already exists.
    
-   If an ID exists, display a message and prevent proceeding. Also display the name of the existing patient with the same ID.
    
-   Create New Patient:  
    On clicking Next, call /patient/new_patient API with Patient Name and ID.

-   Only navigate to the next page if the API response is successful.
    
-   Log any errors to the console.
    
-   API Function Implementation:  
    Even if actual endpoints are unavailable, implement the API call logic as separate functions.
    
-   Log mock/fake API responses to the console matching the Patient Management API structure. Refer to the [Patient Management API](https://docs.google.com/document/d/1lb0Hg7HdHCjlH8K2aNIHwEyfy_Q4DA4V2RQ7FGXTQR0/edit?tab=t.0#heading=h.u3vw894gfa6a).
    
Notes
-   Keep all API call logic in separate functions for maintainability.
-   Log all API responses to the console during development; remove logs for production.
-   Always validate Patient ID before making API calls.
-   Block navigation to the next page if API returns an error or if Patient ID is already taken.


## UI:

<img width="206" height="459" alt="Image" src="https://github.com/user-attachments/assets/6d907775-1fb3-4d89-8a8d-5ed8e7fc0877" />