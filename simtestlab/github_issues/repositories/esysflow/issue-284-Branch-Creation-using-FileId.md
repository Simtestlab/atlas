# Issue #284: Branch Creation using FileId

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-07-10  
**Updated:** 2025-07-10  
**Author:** @divya-rosy  
**Assignees:** @nallasivamselvaraj  
**Labels:** `bug`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/284)

## Description

DOD: The issue here was that creating a new branch from an origin branch retained the origin branch’s fileId.
As a result, saving the flow did not create a new version.
This issue has been identified, tested, and resolved by preventing in saving the flow file using the same file Id.
