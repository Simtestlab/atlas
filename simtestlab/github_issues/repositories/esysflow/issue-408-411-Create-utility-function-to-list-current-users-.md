# Issue #408: 4.1.1 Create utility function to list current users, nodes and edges in a diagram

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-08-18  
**Updated:** 2025-08-21  
**Author:** @harish-ramar  
**Assignees:** @niteshkumar1710  
**Labels:** `Feature`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/408)

## Description

DOD: As a developer, I require utility functions for integration into the comment window UI of a canvas-based application. The functions must fulfill the following requirements:

1. **Node List**: The function should retrieve a list of all nodes in the current canvas, returning each node's ID and corresponding name or label.
2. **Edge List**: The function should retrieve a list of all edges in the current canvas, returning each edge's ID and corresponding name or label.
3. **User List**: The function should retrieve a list of names of all users with access to the current canvas. This functionality may require integration with a dedicated API or compatibility with an existing API to fetch user data.