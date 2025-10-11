# Issue #28: EtherCAT Differential Pair Routing & Signal Integrity

**Repository:** hardware  
**Status:** Closed  
**Created:** 2025-10-05  
**Updated:** 2025-10-10  
**Closed:** 2025-10-10  
**Author:** @prabhagaran  
**Assignees:** @prabhagaran  

[View on GitHub](https://github.com/Simtestlab/hardware/issues/28)

## Description

**Description**
_Complete the PCB routing for the EtherCAT subsystem (MCU ↔ PHY ↔ magnetics ↔ connector) with controlled impedance, length-matching, and signal-integrity practices suitable for EtherCAT performance._

Tasks

- [ ] Place MCU, EtherCAT PHY(s), magnetics, and RJ45/connector optimally (PHY between MCU & magnetics; magnetics at board edge).
- [ ]  Route all differential pairs (TX+/TX–, RX+/RX–) with target 100 Ω ±10% differential impedance.
- [ ]  Match +/– pair lengths to ≤ 5 mil skew and minimize inter-pair skew (TX vs RX) per spec (target ≤ 100 mil).
- [ ]  Minimize vias on pairs; if vias are necessary keep them symmetric and matched.
- [ ]  Ensure continuous, unbroken ground reference plane beneath differential pairs; add stitching vias around connector area as needed.
- [ ]  Route clock and control lines (MDC/MDIO/RESET) short and away from noisy power traces.
- [ ]  Add required decoupling at PHY power pins (0.1 µF + 10 µF) and ferrite bead isolation where applicable.
- [ ]  Run impedance and DRC checks; tune lengths using the PCB tool’s length tuning/serpentine features.
- [ ]  Create docs/ethercat_routing.md summarizing routing rules, final pair lengths, DRC/impedance results, and screenshots.
- [ ]  Peer review & sign-off.

**Deliverables**

- Routed PCB section with EtherCAT traces completed.
- DRC report showing differential impedance and skew compliance.
- docs/ethercat_routing.md (routing settings, pair widths/spacing, stackup references, screenshots).
- Short summary in PR describing any trade-offs or deviations.