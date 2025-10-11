# Issue #58: First-run checks and restart main() on fatal init error

**Repository:** bms_master  
**Status:** Open  
**Created:** 2025-10-01  
**Updated:** 2025-10-08  
**Author:** @crmaarimuthu  
**Assignees:** @crmaarimuthu  

[View on GitHub](https://github.com/Simtestlab/bms_master/issues/58)

## Description

DoD:

On startup, main() calls Bms_Init().
If init fails on first boot → safe restart (main() retry or MCU reset).
If init fails again → enter fail-safe loop with error log.
Verified by forcing an init failure in the test.