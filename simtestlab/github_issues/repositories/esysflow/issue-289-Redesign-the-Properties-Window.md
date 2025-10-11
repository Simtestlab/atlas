# Issue #289: Redesign the Properties Window

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-07-10  
**Updated:** 2025-07-10  
**Author:** @harish-ramar  
**Labels:** `UI`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/289)

## Description

DOD: Redesign the entire properties window which should render the input and output based on the node and provide option to edit and modify the existing node.

- It should show the rendered code for each node if exists with a markdown editor.
- Documentation window is in current version but it is not expected to implement here initially.
- It should have the option to rename the node and change the color of the node.
- Need option to add, remove and edit the input and output handlers
- All these changes should only modify the selected node not the entire nodes inside the library so every changes should be local to that particular node only.

Note:
1. All components should be modularized and reusable
2. Proper documentation string is mandatory
3. Initialy developer the UI with the hardcoded data but should match the current page's data structure
4. It should render the Navbar based on the page so configure it in such a way

@aeroramesh @prabhagaran @nallasivamselvaraj 