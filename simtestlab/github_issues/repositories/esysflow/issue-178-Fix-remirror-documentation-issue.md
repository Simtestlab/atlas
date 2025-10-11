# Issue #178: Fix remirror documentation issue

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2025-05-12  
**Updated:** 2025-05-12  
**Closed:** 2025-05-12  
**Author:** @harish-ramar  
**Assignees:** @harish-ramar  
**Labels:** `bug`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/178)

## Description

DOD: As a developer fix the remirror component (documentation window) data has not been stored and fetched from the json file.

![Image](https://github.com/user-attachments/assets/91d159c6-1c3b-49bf-969f-e29c78ead793)

- Here you can see that when existing data has been stored the edit icon is not visible.
- Also the documentation data is not stored in the JSON file. It is stored inside the component's state itself.
- Need to store the documentation data inside the JSON object itself and show the data in the properties window if existing data available with an option to edit.