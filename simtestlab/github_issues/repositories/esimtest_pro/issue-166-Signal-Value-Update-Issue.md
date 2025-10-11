# Issue #166: Signal Value Update Issue

**Repository:** esimtest_pro  
**Status:** Open  
**Created:** 2025-02-05  
**Updated:** 2025-02-05  
**Author:** @Muralipandiyan  
**Assignees:** @Muralipandiyan  
**Labels:** `bug`  

[View on GitHub](https://github.com/Simtestlab/esimtest_pro/issues/166)

## Description

For the signal IgnKeyType_D_Act1, I set the value to 23 for the time interval from 0 to 1 with a step of 0.2. I observed the value on the screen every 0.2 seconds, and it remained 23. Later, I applied an equation to the same signal by adding another signal with some noise. However, when I returned to the same screen window to observe the signal, the value did not change as expected. I expected the values to change according to the modifications made in the plot window.

![Image](https://github.com/user-attachments/assets/ec50a43b-6813-4f0f-88be-f0b9bd237c0c)

Is it working as expected? 
@aeroramesh @AgilanArulchelvam @RajavelRajendiran @sajimotrax 