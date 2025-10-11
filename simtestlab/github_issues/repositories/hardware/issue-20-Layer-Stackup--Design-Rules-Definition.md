# Issue #20: Layer Stackup & Design Rules Definition

**Repository:** hardware  
**Status:** Closed  
**Created:** 2025-10-02  
**Updated:** 2025-10-05  
**Closed:** 2025-10-05  
**Author:** @prabhagaran  
**Assignees:** @prabhagaran  

[View on GitHub](https://github.com/Simtestlab/hardware/issues/20)

## Description

_Define the PCB layer stackup and establish design rules/constraints (clearances, widths, impedance control, via types, etc.) for the Falcon Adaptor board. This ensures consistent electrical performance and manufacturability._

**Tasks**

- [x]  Define board stackup (number of layers, material, thickness, copper weight).
- [x]  Assign each layer’s purpose (signal, power, ground, mixed).
- [x]  Specify impedance control rules (e.g., 100 Ω diff pair for Ethernet/EtherCAT, 50 Ω single-ended).
- [x]  Define trace widths and spacing for signals, power rails, high-speed pairs.
- [x]  Set via rules (through-hole, blind/buried, microvias if needed).
- [x]  Establish clearance rules (minimum creepage/clearance, especially for power nets).
- [x]  Define component placement keep-outs (mounting holes, connectors, mechanical constraints).
- [x]  Document stackup and rules in docs/pcb_stackup_rules.md.
- [x]  Import rules into the PCB design tool (Altium/KiCad/etc.).

**Deliverables**

- docs/pcb_stackup_rules.md with final layer stackup and rule set.
- PCB project updated with stackup + design rules applied.
- Screenshots/plots showing impedance profiles or manufacturer-provided stackup confirmation.