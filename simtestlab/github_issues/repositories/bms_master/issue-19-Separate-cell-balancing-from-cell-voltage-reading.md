# Issue #19: Separate cell balancing from cell voltage reading

**Repository:** bms_master  
**Status:** Closed  
**Created:** 2025-09-18  
**Updated:** 2025-09-23  
**Closed:** 2025-09-23  
**Author:** @Elfaouzo  
**Assignees:** @crmaarimuthu  

[View on GitHub](https://github.com/Simtestlab/bms_master/issues/19)

## Description

The cell voltage readings are safety critical therefore they should be segregated and run on its own.
The cell balancing function should be run on a separate task (its own) not to interfere with cell voltage reading.