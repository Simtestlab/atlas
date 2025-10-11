# Issue #1: STM32F103C8T6: Automatic Battery Heating & Cooling System using Relays and Temperature Sensor

**Repository:** Chamber-Automation-Firmware  
**Status:** Open  
**Created:** 2025-02-27  
**Updated:** 2025-06-06  
**Author:** @crmaarimuthu  
**Assignees:** @crmaarimuthu  

[View on GitHub](https://github.com/Simtestlab/Chamber-Automation-Firmware/issues/1)

## Description

Definition of Done (DoD):

✅ Hardware Setup Completed

STM32F103C8T6 wired to a temperature sensor (e.g., NTC, LM35, DS18B20).

Two relays connected for heating and cooling control.


✅ Firmware Implementation

ADC reads battery temperature accurately.

Relay control logic implemented based on defined thresholds.

GPIO toggles relays for heating and cooling.


✅ Code Quality & Documentation

Code is structured, documented, and follows best practices.

README.md includes wiring diagram and setup instructions.

Thresholds and sensor calibration can be modified easily.


✅ Testing & Validation

System responds correctly to temperature changes.

Relays switch automatically at correct thresholds.

Logs or debug outputs confirm expected behavior.


✅ GitHub Repository Setup

Project is committed and pushed to GitHub.

Includes source code, README, and hardware connections.