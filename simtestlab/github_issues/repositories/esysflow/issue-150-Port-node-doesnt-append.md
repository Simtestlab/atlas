# Issue #150: Port node doesn't append

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2025-03-25  
**Updated:** 2025-05-10  
**Closed:** 2025-05-10  
**Author:** @harish-ramar  
**Assignees:** @divya-rosy  
**Labels:** `bug`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/150)

## Description

DOD: As a developer fix the port node doesn't append issue.

Reason for issue:
When a subflow is created the port nodes are appended correctly as it's state has been handled internally, but while drag and dropping it is handled separately thus results in appending issue.

Try to use zustand store to store the port node's count for inport and outport node seperately.

![Image](https://github.com/user-attachments/assets/f4ac1ad8-3ed3-4975-b7ff-ab613bb75a9b)