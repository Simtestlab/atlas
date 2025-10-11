# Issue #19: Mutex in FreeRTOS Implementation

**Repository:** XMC4800_FreeRTOS_Tutorial  
**Status:** Closed  
**Created:** 2025-01-30  
**Updated:** 2025-08-01  
**Closed:** 2025-01-31  
**Author:** @Girivelavan  
**Labels:** `Coding`  

[View on GitHub](https://github.com/Simtestlab/XMC4800_FreeRTOS_Tutorial/issues/19)

## Description

DOD : 
- Create Mutex: Use xSemaphoreCreateMutex() to control access to a shared buffer.
- UART Task: Locks the mutex, writes received data to the shared buffer, and releases the mutex.
- CAN Task: Locks the mutex, reads from the shared buffer, transmits via CAN, and releases the mutex.
- Task Synchronization: If a task can't acquire the mutex, it waits (xSemaphoreTake()) until it's available, ensuring safe data access.


@crmaarimuthu @prabhagaran @nallasivamselvaraj @sajimotrax @aeroramesh 