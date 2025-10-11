# Issue #366: 2.3 State Management (Project Tree)

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-08-09  
**Updated:** 2025-08-09  
**Author:** @divya-rosy  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/366)

## Description

DOD: Each flow and sub-flow should include an option to freeze, available to users with roles such as developer, admin, or owner.
	Once an item is frozen, it should become read-only. This functionality is built into React Flow; it only requires calling the appropriate function, and React Flow will handle the rest.
	Subsequently, only the user who froze the item can transition it back to an idle state. The database will store the user ID of the person who froze it, and the UI should use this data via the API to update the interface appropriately.
	Before starting this task, the developer must ensure that the state management APIs are available and understand their structure to proceed effectively. Icons can be provided to visually indicate the state of each flow to users based on the task.
