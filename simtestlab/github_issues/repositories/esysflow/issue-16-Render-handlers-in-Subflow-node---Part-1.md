# Issue #16: Render handlers in Subflow node - Part 1

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2024-11-24  
**Updated:** 2024-12-13  
**Closed:** 2024-11-30  
**Author:** @harish-ramar  
**Assignees:** @harish-ramar  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/16)

## Description

# Render Subflow Handlers:
### Render the connected port nodes in subflow while creating a new subflow (Similar to Matlab):

Currently the sub flow doesn't render any input or output handlers, because currently the inport and outport nodes are rendered automatically.

So we need to identify the inport node  and outport nodes and render them in the Subflow node.

For example:

If the following nodes are created has subflow
![Image](https://github.com/user-attachments/assets/ff200d0b-b5fe-46b9-a321-feb42e123f50)

After they are created as subflow they contain inport and outport nodes like this:
![Image](https://github.com/user-attachments/assets/9791fa27-e609-4296-a458-3aae8831225e)

So this flow contains **3 inport nodes and 1 outport node** and in the subflow node we should render these as handlers.
![Image](https://github.com/user-attachments/assets/227d1229-6a3f-4b2c-84c5-f869df88b559)
