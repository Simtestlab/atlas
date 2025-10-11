# Issue #16: Report Data Page

**Repository:** echo_gecko_ui  
**Status:** Closed  
**Created:** 2025-09-13  
**Updated:** 2025-09-18  
**Closed:** 2025-09-18  
**Author:** @harish-ramar  
**Assignees:** @divya-rosy  
**Labels:** `UI/UX`  

[View on GitHub](https://github.com/Simtestlab/echo_gecko_ui/issues/16)

## Description

### Overview

The Report Data screen (right side of the provided UI wireframe) is the core feature of the app, where users review, edit, and finalize scanned or retrieved report data. It is rendered in two primary scenarios:
- Immediately after the user clicks "Proceed" on the Scanned Data screen (following data extraction from an image scan).
- When viewing or editing an existing report from the app's reports list.
This screen is expected to be the most frequently used, so prioritize a clean, minimalistic, and visually intuitive design.

The Alert Page (left side of the wireframe) is a modal overlay that may appear on initial load if data validation detects potential inaccuracies (e.g., outliers in scanned values).

It prompts the user to confirm before proceeding, with "Yes" dismissing the alert and loading the report, and "No" canceling or redirecting back.

## Key UI elements from the wireframe:

### Action Buttons:
-Save: Persists changes to the database via API.
-Share: Exports the report as a PDF.
-Retake: Redirects to the scanning flow for re-capture.
-Edit: Enables inline editing of data values.

## Functionality Requirements
### Data Fetching and Rendering:
- On load, send the extracted/scanned data (from the previous screen or existing report ID) to the server via API.
- The server performs a lookup against reference data in the database (based on breed, species, weight, etc.).
- Fetch and display the reference ranges (min/max) alongside the user's data values.

### Compute and show the "Range" status visually:
1. "Within" (green) if data is between min and max.
2. "Below" (red) if data < min.
3. "Above" (red) if data > max.
  If initial validation detects potential errors (e.g., via server-side checks), display the Alert Modal before showing the full report.
 
### Editing Values:
- The "Edit" button enables an editable mode (e.g., text fields in the "Data" column).
- On edit completion (e.g., blur or confirm), send updated values to the server API.
- Re-fetch reference ranges if edits affect lookup criteria (e.g., changing weight).
- Update the table in real-time with new status indicators.

### Retake Functionality:
- Mirrors the "Retake" behavior from the Scanned Data screen: Redirects to the image capture/scanning flow, discarding current unsaved changes (with optional confirmation prompt).

### Save Functionality:
On click, validate data client-side (e.g., required fields, numeric formats).
Send the full report (metadata + measurements) to the server API for database update/creation.
Show success feedback navigate to Reports list (which is in the bottom navbar)

### Share Functionality:
- Generate a PDF export of the report using Flutter packages (e.g., pdf and printing for rendering/sharing) the PDF can be generated using the JSON file fetched by the database where the JSON contains all the values including user, patient, values obtained, reference value and result.
- Include all displayed data: Metadata, table with values/ranges/status.
- Use platform-native sharing (e.g., SharePlus package) to allow emailing, saving to files, etc.

### Note:
Design the UI with the hardcoded data initially and refer to the API documentation and implement the respective APIs needed.

## UI:

- UI needs to be updated.