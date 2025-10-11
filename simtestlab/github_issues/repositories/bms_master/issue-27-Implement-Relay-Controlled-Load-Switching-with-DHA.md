# Issue #27: Implement Relay-Controlled Load Switching with DHAB S/157 Current Sensor Monitoring

**Repository:** bms_master  
**Status:** Closed  
**Created:** 2025-09-20  
**Updated:** 2025-09-25  
**Closed:** 2025-09-25  
**Author:** @crmaarimuthu  
**Assignees:** @crmaarimuthu  

[View on GitHub](https://github.com/Simtestlab/bms_master/issues/27)

## Description

Definition of Done (DoD):
 Hardware digital output pin configured for relay control (ON/OFF).
 Relay switching verified (load connected and disconnected properly).
 DHAB S/157 current sensor interface implemented.
 ADC pin configured and calibrated for sensor output.
 Conversion function from sensor ADC reading → actual current (A).
 Load ON/OFF state is synchronized with relay control command.
 Current measurement validated when load is ON (compare with expected load current).
 Safety check: Relay OFF when system reset or fault occurs.