# Issue #13: Multi-DAC Control System with Serial Communication and FreeRTOS Integration

**Repository:** adbms_slave  
**Status:** Open  
**Created:** 2024-12-25  
**Updated:** 2025-01-07  
**Author:** @crmaarimuthu  
**Assignees:** @crmaarimuthu  

[View on GitHub](https://github.com/Simtestlab/adbms_slave/issues/13)

## Description

DOD:
Initialize and configure 8 DACs over SPI.
Update DAC values from EEPROM and display via Serial.
Process valid 4-character hex input to update EEPROM.
Ensure stable operation without crashes.
Retain EEPROM data across power cycles.
Validate task execution and inter-task communication.
Operate successfully on target hardware.