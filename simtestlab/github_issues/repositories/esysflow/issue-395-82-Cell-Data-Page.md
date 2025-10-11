# Issue #395: 8.2 Cell Data Page

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-08-09  
**Updated:** 2025-08-09  
**Author:** @divya-rosy  
**Labels:** `UI`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/395)

## Description

DOD: Currently, the State of Charge (SOC) and Battery Gauge are displayed in separate windows. They will be combined into a single window, as shown in the referenced image.

<img width="1133" height="582" alt="Image" src="https://github.com/user-attachments/assets/68a83ce3-b7cc-4ccc-b8b6-3bc819e39c5e" />

Each battery gauge is designed to display the State of Charge (SOC) and voltage. The level is shown based on the SOC percentage.
When changes happen in the database the updates will be reflected asynchronously in the page without page reload.