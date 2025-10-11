# Issue #14: Ethernet MCU Connector Pin Mapping (Ports & Net Names)

**Repository:** hardware  
**Status:** Open  
**Created:** 2025-09-20  
**Updated:** 2025-09-20  
**Author:** @prabhagaran  
**Assignees:** @prabhagaran  

[View on GitHub](https://github.com/Simtestlab/hardware/issues/14)

## Description

**Ethernet MCU Connector Pin Mapping (Ports & Net Names)**
**Description**
_Map all Ethernet signals from the MCU pins to the external connector pins, assigning consistent port names and net names.
This mapping will ensure proper schematic clarity, PCB layout alignment, and firmware reference._
**Tasks**

- [ ]  List all Ethernet signals required (TXP/TXN, RXP/RXN, MDIO, MDC, REFCLK, RESET_N, etc.).
- [ ]  Identify the corresponding MCU pins for each signal.
- [ ]  Assign net names (e.g., ETH_TXP, ETH_RXN, ETH_MDIO).
- [ ]  Map them to the connector pins (RJ45 or automotive-grade Ethernet connector).
- [ ]  Update schematics with ports and global nets.
- [ ]  Document the mapping table in repo.

**Deliverables**

- Updated schematic sheets (MCU ↔ Ethernet PHY ↔ Connector).
- docs/ethernet_pin_map.md with full mapping.