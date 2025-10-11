# Issue #288: Redesign the Canvas page to handle multiple tabs

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-07-10  
**Updated:** 2025-07-11  
**Author:** @harish-ramar  
**Labels:** `UI`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/288)

## Description

DOD: As a developer modify the existing canvas page layout to adapt to the any navbar and screen responsive

The existing page contains the reactflow canvas, sidebar with Library and Project Tree and the menubar, we have to retains those components and make them screen responsive.

Then add support for tab based navigation where the parent/initial tab should render this canvas. This task depends on the latest Navbar so a better understand of it is needed before proceeding.

Note:

1. All components should be modularized and reusable
2. Proper documentation string is mandatory
3. Initialy developer the UI with the hardcoded data but should match the current page's data structure
4. It should render the Navbar based on the page so configure it in such a way
5. Clarify any doubts before start working on this task

<img width="3399" height="1642" alt="Image" src="https://github.com/user-attachments/assets/595697f1-d249-43ad-9928-a95f0f416432" />



### **Reference**
**Canvas page**

<img width="1564" height="586" alt="Image" src="https://github.com/user-attachments/assets/6753d0fa-9bc6-405a-90fe-489917361b96" />

**Path on Navbar:**
https://mui.com/material-ui/react-breadcrumbs/#active-last-breadcrumb

**Tabs:**
https://mui.com/material-ui/react-tabs/#colored-tab

**Collaborative Avatars:**
https://mui.com/material-ui/react-avatar/#total-avatars

@aeroramesh @prabhagaran @nallasivamselvaraj 