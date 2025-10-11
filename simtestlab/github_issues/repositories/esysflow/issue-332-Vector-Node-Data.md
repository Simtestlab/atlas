# Issue #332: Vector Node Data

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2025-07-23  
**Updated:** 2025-09-17  
**Closed:** 2025-09-17  
**Author:** @divya-rosy  
**Assignees:** @M-Barath-Vikraman  
**Labels:** `bug`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/332)

## Description

### Vector Data Synchronization

![Image](https://github.com/user-attachments/assets/052f52b7-6894-4f6a-acd3-f9ab55a6856e)

- The vector data table does not execute in sync with the vector node.
- The vector data table is not synchronized with the vector node—for example, when the vector node is deleted, the vector data table should also be removed, but it remains visible.
- This need to be executed asynchronously.

@nallasivamselvaraj @harish-ramar 