# Issue #39: XMC4800-Based Pack Monitoring with ADBMS2950

**Repository:** adbms_master  
**Status:** Open  
**Created:** 2025-07-10  
**Updated:** 2025-07-27  
**Author:** @crmaarimuthu  
**Assignees:** @crmaarimuthu  

[View on GitHub](https://github.com/Simtestlab/adbms_master/issues/39)

## Description

DOD:

Hardware Integration

 ADBMS2950 properly connected to XMC4800 via SPI/isoSPI.

 Required passive components, filters, and isolation implemented per ADBMS2950 datasheet.

 Voltage/current sensors connected to the pack and properly interfaced.

Firmware Development

 SPI/isoSPI communication initialized and verified with ADBMS2950.

 Wake-up, initialization, and configuration commands sent to ADBMS2950.

 Cell voltage, temperature, and pack current readings successfully received.

 Data integrity verified using PEC (Packet Error Code).

 All data stored in structured variables or buffers.

Data Processing

 Cell balancing status monitored and/or triggered.

 SOC (State of Charge), DOD (Depth of Discharge), and SOH (optional) calculated.

 Fault detection and handling implemented (OV, UV, OT, communication loss, etc.).

Communication & Interface

 UART/CAN/USB output of data for debugging/logging.

 CAN communication with external systems (optional).

 BMS status flags and fault states available over communication interface.

Testing & Validation

 Verified correct readings for all 12 cells in the pack.

 Tested communication reliability (e.g., retries, timeouts).

 Fault injection tests passed.

 Validated against reference measurements (multimeter, DMM, etc.).

Documentation

 Code is documented with comments and README.

 Schematics and hardware connections documented.

 Test reports and validation logs maintained.

Final Integration

 Integrated with main system or higher-level controller.

 Continuous monitoring for pack performance and safety.

 System runs reliably over extended period (burn-in or soak test passed).