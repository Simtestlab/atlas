# Issue #11: Existing Patient UI

**Repository:** echo_gecko_ui  
**Status:** Closed  
**Created:** 2025-09-13  
**Updated:** 2025-09-18  
**Closed:** 2025-09-18  
**Author:** @harish-ramar  
**Assignees:** @divya-rosy  
**Labels:** `UI/UX`  

[View on GitHub](https://github.com/Simtestlab/echo_gecko_ui/issues/11)

## Description

### Task Overview

The Existing Patients page displays all patients previously added by the authenticated user. Patient data is stored in a separate table, with each record linked to the user's Firebase user_id as a foreign key. This page is accessed from the Patient Page.

Refer to the UI wireframe for layout and navigation.

## Patient List Rendering

-   Fetch and display all patients for the current user from the database.
    
-   Only show patients where deleted_at is null (i.e., not deleted).
    
-   For each patient, display:
    
-   Patient Name
    
-   Patient ID
    
-   Last Modified Time
    

## Actions

-   Scan Page Navigation:  
    Clicking the patient name navigates directly to the scan page for that patient.
    
-   Edit:  
    Clicking the edit icon opens the Species details Page
    
-   Pre-fill the form with existing species/bio data for the selected patient (not an empty form like new patient flow).