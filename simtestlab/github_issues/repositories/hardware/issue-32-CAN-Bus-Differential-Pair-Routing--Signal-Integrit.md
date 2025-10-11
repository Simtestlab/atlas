# Issue #32: CAN Bus Differential Pair Routing & Signal Integrity

**Repository:** hardware  
**Status:** Closed  
**Created:** 2025-10-07  
**Updated:** 2025-10-07  
**Closed:** 2025-10-07  
**Author:** @prabhagaran  
**Assignees:** @prabhagaran  

[View on GitHub](https://github.com/Simtestlab/hardware/issues/32)

## Description

**Description**
_Route all CAN bus differential pairs (CAN_H / CAN_L) between the MCU, transceivers, and connectors with proper impedance control and signal integrity suitable for automotive communication standards (ISO 11898)._

**Tasks**

- [x]  Identify CAN signal pairs and their respective transceivers.
- [x]  Route CAN_H / CAN_L as a differential pair with 120 Ω ±10% differential impedance.
- [x]  Keep the pair length-matched (≤ 5 mil skew) and tightly coupled throughout the route.
- [x]  Minimize vias and maintain equal via count for CAN_H and CAN_L.
- [x]  Avoid sharp 90° corners — use smooth bends or 45° angles.
- [x]  Keep CAN traces short, direct, and isolated from high-speed or noisy power lines.
- [x]  Place termination resistor (120 Ω) near the connector or as per system topology.
- [x]  Ensure proper ground reference under the pair with no splits or cuts.
- [x]  Add ESD protection and common-mode choke footprints near the connector.
- [x]  Verify impedance and DRC checks after routing.

**Deliverables**

- Completed CAN differential pair routing on PCB layout.
- DRC and impedance verification report.
- Screenshot of CAN bus routing section (highlighting CAN_H and CAN_L).