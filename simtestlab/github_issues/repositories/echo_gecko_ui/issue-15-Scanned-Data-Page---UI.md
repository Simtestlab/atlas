# Issue #15: Scanned Data Page - UI

**Repository:** echo_gecko_ui  
**Status:** Closed  
**Created:** 2025-09-13  
**Updated:** 2025-09-18  
**Closed:** 2025-09-18  
**Author:** @harish-ramar  
**Assignees:** @divya-rosy  
**Labels:** `UI/UX`  

[View on GitHub](https://github.com/Simtestlab/echo_gecko_ui/issues/15)

## Description

## Task Overview

<img width="957" height="1092" alt="Image" src="https://github.com/user-attachments/assets/ce513e38-869d-4956-8c2b-7aaa9394369c" />


The Scanned Page displays parsed/structured data returned by the server after an uploaded image is processed (OCR + lookup).
While OCR is in progress or not yet implemented, the page must accept injected parsed data so the UI can be developed and tested independently.

### Key responsibilities

- Accept a parsed data payload (key/value map) and render it in a readable, editable form.
- Provide a single, well-documented entrypoint to load parsed data so OCR engineers can call it when processing completes.
- Support states: loading, populated, partial/missing fields, empty (no data), and error. Allow users to review and edit parsed values before saving or continuing.
- While clicking the Retake Icon the camera should be launched again and while clicking the edit icon it should render the option to edit the values.
- Once the proceed button is clicked, it should navigate to the final lookup and report data page.

### UI:

<img width="210" height="463" alt="Image" src="https://github.com/user-attachments/assets/cd73c959-f7b3-4add-8371-8b4724f03563" />

