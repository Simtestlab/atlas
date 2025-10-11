# Issue #18: LFP cell OCV data collection

**Repository:** bms_master  
**Status:** Open  
**Created:** 2025-09-18  
**Updated:** 2025-09-18  
**Author:** @Elfaouzo  

[View on GitHub](https://github.com/Simtestlab/bms_master/issues/18)

## Description

The purpose of this task is to collect OCV data for a given LFP cell (75Ah).
The goal is to get an OCV-charge, an OCV-discharge curve under the below conditions:
- 1C (or 75A) if possible otherwise 0.3C (25A).
- 20-25 degree C.
- 10 data points per curve.

Procedure:
Since the cells are aged differently and their capacity is unknown, one should start by choosing a cell and marking it (make it identifiable for later use).
Estimate its real capacity by discharging it to 2.5V. Then charge it to 3.65V using the same C-rate as mentioned above.
Once the real capacity is known, one can discharge it with the chosen C-rate with the known capacity/10.
Let the cell relax for 10min at every step then note the cell voltage.
Repeat for charge.

Assumption:
- The OCV curve is not age dependent.
- The OCV curve is to be used for temperatures between ~15-28 degC.