# Issue #13: EtherCAT MCU Connector Pin Mapping (Ports & Net Names)

**Repository:** hardware  
**Status:** Open  
**Created:** 2025-09-20  
**Updated:** 2025-09-20  
**Author:** @prabhagaran  
**Assignees:** @prabhagaran  

[View on GitHub](https://github.com/Simtestlab/hardware/issues/13)

## Description

**EtherCAT MCU Connector Pin Mapping (Ports & Net Names)**
**Description**
_Map all EtherCAT signals from the MCU pins to the external connector pins, assigning clear port names and net names that follow the naming convention._
**Tasks**

-  List all EtherCAT signals required (TXP/TXN, RXP/RXN, CLK, RESET_N, etc.).
-  Identify the exact MCU pins used for each signal.
-  Assign net names (e.g., ECAT_TXP, ECAT_RXN, ECAT_CLK).
-  Map them to the corresponding connector pins.
-  Update schematic sheets with port symbols and global nets.
-  Document everything in a mapping table.

**Deliverables**

- Updated schematics (MCU + connector with EtherCAT ports/nets).
- docs/ethercat_pin_map.md with a table of MCU pin → port name → net name → connector pin.