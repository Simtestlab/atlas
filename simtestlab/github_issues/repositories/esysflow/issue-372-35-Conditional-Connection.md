# Issue #372: 3.5 Conditional Connection

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-08-09  
**Updated:** 2025-08-09  
**Author:** @divya-rosy  
**Labels:** `UI`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/372)

## Description

DOD: Currently, only the graph node validates incoming edge connections. This validation should be extended to all nodes by including an `allowed_types` object in each node.
	When a node type is specified in this object, only that type can be connected; otherwise, the connection will be prevented, and an alert popup will notify the user. This feature will also aid in node evaluation.
