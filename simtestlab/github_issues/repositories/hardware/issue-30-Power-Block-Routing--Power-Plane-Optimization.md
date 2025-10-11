# Issue #30: Power Block Routing & Power Plane Optimization

**Repository:** hardware  
**Status:** Closed  
**Created:** 2025-10-06  
**Updated:** 2025-10-07  
**Closed:** 2025-10-07  
**Author:** @prabhagaran  
**Assignees:** @prabhagaran  

[View on GitHub](https://github.com/Simtestlab/hardware/issues/30)

## Description

**Description**
_Complete the Power Block routing, ensuring optimal current flow, thermal performance, and power integrity for 5V, 3.3V, and 2.5V LDO sections. Define wide copper pours and solid return paths for stable power delivery across the board._

**Tasks**
- [x] Route all LDO outputs (5V, 3.3V, 2.5V) to their respective load sections.
- [x]  Use wide traces or copper planes for power rails depending on current demand.
- [x]  Ensure short and thick connections between LDO input/output and decoupling capacitors.
- [x]  Place decoupling capacitors as close as possible to each LDO output pin.
- [x]  Maintain a star-ground topology or low-impedance ground plane for power return.
- [x]  Separate analog and digital ground zones if applicable, with single-point connection.
- [x]  Check thermal dissipation and use thermal vias under LDO packages if needed.
- [x]  Verify voltage drop and power plane continuity through simulation or DRC checks.

**Deliverables**

- Completed Power Block routing in PCB layout.
- Screenshot of routed power area (highlighting 5V, 3.3V, 2.5V planes).
