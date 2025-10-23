---
title: Software Architecture of BMS
status: approved
comments: true
---



## Core BMS functions
![Core BMS functtions](bms_functions.svg)


## Software Architecture  
![Description of Image](bms_application_architecture.png)


```mermaid
  flowchart TB
  SPP[Signal Pre-processing] -- Vcell_fast[], Temperatures_fast[] --> CLV[Cell Limit Violation]
  SPP[Signal Pre-processing] -- Vcell_fast[], Temperatures_fast[] --> CL[Current Limits]
  CV((Small start)) -- CellVoltage[] --> SPP
  I((Small start)) -- Current --> SPP
  Temp((Small start)) -- Temperatures[] --> SPP
```
