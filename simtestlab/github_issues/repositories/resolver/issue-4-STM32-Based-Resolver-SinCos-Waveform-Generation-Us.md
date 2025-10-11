# Issue #4: STM32-Based Resolver Sin/Cos Waveform Generation Using DAC

**Repository:** resolver  
**Status:** Open  
**Created:** 2025-03-13  
**Updated:** 2025-03-13  
**Author:** @crmaarimuthu  
**Assignees:** @crmaarimuthu  

[View on GitHub](https://github.com/Simtestlab/resolver/issues/4)

## Description

1. Initialization & Setup
 STM32 peripherals initialized: DAC
 System clock configured correctly for stable timing
 DAC channels enabled and started
2. Signal Generation
 Sinusoidal and Cosinusoidal waveforms successfully generated
 Carrier frequency 5 kHz, modulation frequency 50 Hz
 Correct amplitude scaling to match 12-bit DAC (0-4095)
3. Timing & Sampling
 Sampling rate set to 50 kHz for smooth waveforms
 Sample index reset after full cycle to prevent drift
 Frequency accuracy confirmed within ±1% error
4. DAC Output Verification
 Oscilloscope capture confirms correct sine and cosine waveforms
 No clipping, distortion, or unwanted harmonics in DAC output
 Lissajous pattern observed in XY mode, confirming quadrature signals
5. Code & Hardware Optimization
 Code runs without HAL errors or system crashes
 Efficient use of HAL DAC functions for real-time signal updates
 No unnecessary delays or blocking operations affecting real-time execution
6. Final Validation
 Continuous signal generation tested for long-term stability
 Output verified under different sampling rates and conditions
 No unexpected phase shifts, glitches, or output instability
7. Documentation & Handover
 Firmware committed to version control (GitHub or internal repository)
 Test results documented with oscilloscope screenshots
 Deployment guide created for reproducing setup on STM32 board