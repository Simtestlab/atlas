# Issue #56: Combine initialisation functions into single Bms_Init()

**Repository:** bms_master  
**Status:** Closed  
**Created:** 2025-09-30  
**Updated:** 2025-10-03  
**Closed:** 2025-10-03  
**Author:** @crmaarimuthu  
**Assignees:** @crmaarimuthu  

[View on GitHub](https://github.com/Simtestlab/bms_master/issues/56)

## Description

DoD:

All peripheral/driver initialisations consolidated into Bms_Init().
Bms_Init() returns success/failure (bool).
No scattered init calls in main.c or tasks.
Logs available if init fails.
Build passes.