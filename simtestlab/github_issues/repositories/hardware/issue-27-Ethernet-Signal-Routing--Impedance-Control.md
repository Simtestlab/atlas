# Issue #27: Ethernet Signal Routing & Impedance Control

**Repository:** hardware  
**Status:** Closed  
**Created:** 2025-10-05  
**Updated:** 2025-10-06  
**Closed:** 2025-10-06  
**Author:** @prabhagaran  
**Assignees:** @prabhagaran  

[View on GitHub](https://github.com/Simtestlab/hardware/issues/27)

## Description

**Description**
_Route all Ethernet signal traces between the MCU/PHY, magnetics, and Ethernet connector with proper impedance control and signal integrity. Ensure compliance with 100BASE-TX/1000BASE-T differential routing guidelines._

**Tasks**

- [x]  Identify all Ethernet differential pairs (TXP/TXN, RXP/RXN).
- [x]  Apply 100 Ω differential impedance routing rule.
- [x]  Keep TX/RX pairs matched in length within ±5 mils.
- [x]  Maintain uniform trace width and spacing per stackup impedance calculations.
- [x]  Minimize vias on differential pairs; if used, ensure matched count and length.
- [x]  Maintain separation between TX and RX pairs to reduce crosstalk.
- [x]  Place magnetics close to the RJ45/connector and route symmetrically.
- [x]  Add test points or stitching vias as needed for EMI/EMC grounding.
- [x]  Verify impedance and length matching with PCB tool constraints check.

**Deliverables**

- Completed Ethernet routing in PCB layout.
- DRC and impedance verification reports.
- Screenshot of routed Ethernet section (with diff pair overlay).