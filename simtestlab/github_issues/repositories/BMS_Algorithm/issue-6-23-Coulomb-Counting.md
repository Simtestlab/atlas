# Issue #6: 2.3. Coulomb Counting 

**Repository:** BMS_Algorithm  
**Status:** Closed  
**Created:** 2025-07-21  
**Updated:** 2025-09-17  
**Closed:** 2025-09-17  
**Author:** @RajavelRajendiran  
**Assignees:** @RajavelRajendiran  

[View on GitHub](https://github.com/Simtestlab/BMS_Algorithm/issues/6)

## Description

Description:
Develop a robust integrator over current, with added logic to detect and correct drift (via OCV or rest points). Handles sensor overflow, noise, and missing data.

DOD:
Add periodic OCV-based SoC correction for counter drift.

Improve integrator with adaptive sample interval handling.

Log and handle sensor dropouts or unrealistic jumps (data validation).

Combine with moving average/low-pass filter to reduce noise influence.