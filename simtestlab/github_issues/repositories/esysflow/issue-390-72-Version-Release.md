# Issue #390: 7.2 Version Release

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-08-09  
**Updated:** 2025-08-09  
**Author:** @divya-rosy  
**Labels:** `Feature`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/390)

## Description

DOD: The current canvas allows users to commit versions, creating a new version each time and enabling users to revert to previous versions.
	This functionality needs modification so that when a version requires review, any user can tag the project owner for review, or the owner can initiate a review.
	A new version should only be created after the project owner’s approval. Once a version is reviewed and approved, it becomes read-only, and a new version is set as the current version.

<img width="583" height="444" alt="Image" src="https://github.com/user-attachments/assets/9da1ebed-2e53-4f66-a658-8ea793154113" />

When a user clicks the commit option, a dialogue box similar to the one shown below should pop-up where the user should enter the name and description for the current commit. Here the project owner will be selected as owner automatically.
	Once a version is moved to review it automatically gets frozen and when the review is done , a new version will be created as a working version for that branch.

