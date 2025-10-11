# Issue #18: Component Grouping for Layout

**Repository:** hardware  
**Status:** Closed  
**Created:** 2025-10-01  
**Updated:** 2025-10-02  
**Closed:** 2025-10-02  
**Author:** @prabhagaran  
**Assignees:** @prabhagaran  

[View on GitHub](https://github.com/Simtestlab/hardware/issues/18)

## Description

_Group components logically based on function and signal flow to simplify PCB layout, reduce routing complexity, and improve electrical + thermal performance._

**Tasks**

- [ ]  Group Power Block components (LDOs, decoupling caps, ferrites, power connectors).
- [ ]  Group EtherCAT subsystem (PHY, magnetics, RJ45/connector, termination resistors).
- [ ]  Group Ethernet subsystem (MAC/PHY, magnetics, connector).
- [ ]  Group MCU & supporting components (crystal/oscillator, decoupling caps, reset circuit).
- [ ]  Group I/O ports (connectors + ESD protection + pull-ups).
- [ ]  Group debug/programming interface (SWD/JTAG, UART headers).
- [ ]  Mark sensitive analog / high-speed nets (differential pairs, clock lines) for careful placement.
- [ ]  Add grouping notes to docs/component_grouping.md with diagrams or screenshots.

**Deliverables**

- Annotated schematic/diagram showing grouped components.
- docs/component_grouping.md with list of groups, purpose, and placement guidelines.
- Updated PCB project with logical grouping visible in component placement view.