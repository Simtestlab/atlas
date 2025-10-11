# Issue #287: Design Project and Branch List with sidebar

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2025-07-10  
**Updated:** 2025-08-01  
**Closed:** 2025-08-01  
**Author:** @harish-ramar  
**Assignees:** @gurusatura  
**Labels:** `UI`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/287)

## Description

DOD: As a developer design the project and branch list with sidebar based on the page.

- As shown in the below images the page should render the projects and branch in seperate pages with the details shown. 
- Ensure the page updates the data asynchronously and dynamically supports multiple screen sizes.
- The Navbar will be handled seperately, so just focus on the page.

Project Page:
<img width="3405" height="1748" alt="Image" src="https://github.com/user-attachments/assets/ec9cd27e-f1c6-4541-a955-dabfdb04795e" />

Branch Page:
<img width="3404" height="1642" alt="Image" src="https://github.com/user-attachments/assets/c0935bb9-9489-4a0e-b536-639bcf433249" />



### Reference:
**Project page**
<img width="1694" height="582" alt="Image" src="https://github.com/user-attachments/assets/8858e890-f9fc-4ac4-9681-958148ca28f7" />

**Branch page**
<img width="1914" height="582" alt="Image" src="https://github.com/user-attachments/assets/5dafd2ff-6ca7-448d-a4b8-5fef2ba435ce" />


**SideBar:**
https://mui.com/material-ui/react-drawer/#clipped-under-the-app-bar

**List:**
https://mui.com/material-ui/react-list/#folder-list

**Table:**
https://mui.com/material-ui/react-table/#basic-table

**Search Box:**
https://mui.com/material-ui/react-text-field/#form-props

**New project and Branch container:**
https://mui.com/material-ui/react-button/#buttons-with-icons-and-label


Note:

1. All components should be modularized and reusable
2. Proper documentation string is mandatory
3. Initialy developer the UI with the hardcoded data but should match the current page's data structure
4. It should render the Navbar based on the page so configure it in such a way

@aeroramesh @prabhagaran @nallasivamselvaraj 