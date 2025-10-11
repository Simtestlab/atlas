# Issue #149: Port nodes renaming issue

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2025-03-23  
**Updated:** 2025-03-28  
**Closed:** 2025-03-28  
**Author:** @harish-ramar  
**Assignees:** @divya-rosy  
**Labels:** `bug`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/149)

## Description

DOD: As a developer fix the port nodes (inport/outport) renaming issues inside the InportNode component.

The function that is used to rename has been import from the useFlow hook as it can be reused among both components Inport and Outport component.

The issue may lies inside the useflow Hook may be the function is not defined properly. Kindly fix the bug and ensure the rename all the port nodes while clicking on it.

![Image](https://github.com/user-attachments/assets/1acbbbeb-a448-4e50-9682-da1d2ac34553)