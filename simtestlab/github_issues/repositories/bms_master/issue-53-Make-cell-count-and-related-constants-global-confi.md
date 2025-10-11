# Issue #53: Make cell count and related constants global config

**Repository:** bms_master  
**Status:** Closed  
**Created:** 2025-09-30  
**Updated:** 2025-09-30  
**Closed:** 2025-09-30  
**Author:** @crmaarimuthu  
**Assignees:** @crmaarimuthu  

[View on GitHub](https://github.com/Simtestlab/bms_master/issues/53)

## Description

DoD:

All constants (TOTAL_IC, CELLS_PER_IC, TOTAL_CELLS, NUM_NTC_CHANNELS) defined in bms_config.h.
No magic numbers remain in tasks or init code; everything references bms_config.h.
Project builds successfully with centralized constants.
Unit tests confirm correct cell count logic.