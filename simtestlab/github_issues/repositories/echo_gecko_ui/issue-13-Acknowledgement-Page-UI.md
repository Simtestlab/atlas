# Issue #13: Acknowledgement Page UI

**Repository:** echo_gecko_ui  
**Status:** Open  
**Created:** 2025-09-13  
**Updated:** 2025-09-18  
**Author:** @harish-ramar  
**Assignees:** @divya-rosy  
**Labels:** `UI/UX`  

[View on GitHub](https://github.com/Simtestlab/echo_gecko_ui/issues/13)

## Description

## Task Overview

<img width="914" height="1092" alt="Image" src="https://github.com/user-attachments/assets/1b6c08b4-6f2b-4011-9e69-ccec167dfc9d" />

The Acknowledgement screen is shown whenever the user taps the Scan action from the Species Details page — whether creating a new patient or editing an existing one.
This screen is purely client-side (no backend or Firebase calls).

## Behavior requirements:

-   Render the acknowledgement screen each time Scan is invoked.
    
-   Show the Next button only after two conditions are met: The user has scrolled to the end of the acknowledgement content (detect via scroll position / sentinel element).
    
-   The user has checked the “Agree” checkbox. If either condition is not satisfied, the Next action must not be available (render it in a disabled state).
    
-   Clicking Next (after both conditions are met) proceeds to the scanning flow.

<img width="210" height="463" alt="Image" src="https://github.com/user-attachments/assets/7f6ed49b-619d-4a1d-bafa-885623802a16" />
