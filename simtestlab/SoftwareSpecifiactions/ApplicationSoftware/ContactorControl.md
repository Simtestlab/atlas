---
comments: true
title: Contactor Control Specification
status: draft
---

# Contactor Control Specification

---

## 1. With Precharge Circuit

The aim of the precharge circuit is to align the load voltage (usually an inverter) with the battery pack voltage by energizing the inverter from the battery.  
By convention, the precharge circuit is on the positive side of the pack.

### a. Closing Sequence

When receiving a request to close the contactors, the BMS should check:  
- Ensure the contactors are open.  
- No critical fault (TBD).  

**Sequence:**  
1. Close the negative contactor.  
2. At the next tick, close the precharge contactor.  
3. Once the link voltage ≈ pack voltage (~5 V difference):  
   - Close the positive contactor.  
   - Open the precharge contactor.  
   - Each action must be one tick apart.  

If the link voltage does not reach the pack voltage within **Dt_prechgTimeOut (20 s default)**:  
- Throw a timeout error.  
- Stop the closing sequence.  

---

### b. Opening Sequence

- On opening request, wait until current < **minCurrentOpenThr (5 A default)**.  
- Then open all contactors simultaneously.  
- If current does not drop within **Dt_loCurrentTimeout (30 s default)** → open contactors anyway.  

---

### c. Error Opening

- **Critical error (cell voltage/temperature violation):** open all contactors immediately.  
- **Mild error:** open all contactors after a delay (**10 s – calibration**) to allow limits to ramp down safely.  

---

## 2. Without Precharge Circuit (Draft)

In some applications, the precharge circuit is located on the inverter side. The inverter precharges itself to reach pack voltage.  

### a. Closing Sequence

When BMS receives request to close:  
- Ensure contactors are open.  
- No critical fault (TBD).  

Then:  
- Close both negative and positive contactors simultaneously.  
- This exposes battery terminal voltage directly to the inverter.  
- Inverter aligns its own voltage internally.  

---

### b. Opening Sequence

On disconnection request:  
- Wait until current < **minCurrentOpenThr (5 A default)**.  
- Open all contactors simultaneously.  

---

# Testing

### a. Closing Sequence – Precharge Timeout

- No faults.  
- Connect PSU to link voltage, set PSU to **0 V**.  
- Send **connection request** over CAN.  
- ✅ Observe: negative + precharge contactors close.  
- ✅ Observe: after **Dt_prechgTimeOut**, all contactors open, BMS throws precharge timeout error on CAN.  

---

### b. Closing Sequence – Normal

- No faults.  
- Connect PSU to link voltage, set PSU = pack voltage.  
- Send **connection request** over CAN.  
- ✅ Observe: negative + positive contactors close, precharge opens.  

---

### c. Opening Sequence – Normal

- Contactors closed.  
- Send **disconnection request** over CAN.  
- ✅ Observe: all contactors open.  

---

### d. Critical Error – No Closing

- Contactors open, no faults.  
- Fake cell over-voltage (e.g., set \(V_{\text{max,crit}}\) from 3.8 V → 3.2 V).  
- Send **connection request** over CAN.  
- ✅ Observe: no contactor closes, BMS remains in error.  

---

### e. Critical Error – Opening

- Contactors closed.  
- Fake cell over-voltage (e.g., set \(V_{\text{max,crit}}\) from 3.8 V → 3.2 V).  
- ✅ Observe: all contactors open immediately, BMS goes to error.  

---

### f. Opening Sequence Under Load

- Contactors closed.  
- Use PSU to charge/discharge battery with **> minCurrentOpenThr** (e.g., 6 A).  
- ⚠ Do not set too high current (risk of damage).  
- Send **disconnection request** over CAN.  
- ✅ Observe: after **Dt_loCurrentTimeout (20 s)** → all contactors open, BMS throws disconnection timeout.  

```mermaid
flowchart TD
    A[Start] --> B{Check Faults?}
    B -- No --> C[Close Negative Contactor]
    C --> D[Close Precharge Contactor]
    D --> E{Link ≈ Pack Voltage?}
    E -- Yes --> F[Close Positive Contactor]
    E -- Timeout --> G[Throw Error + Open All]
