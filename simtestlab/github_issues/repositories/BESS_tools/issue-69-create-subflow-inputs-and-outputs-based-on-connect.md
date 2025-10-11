# Issue #69: create subflow inputs and outputs based on connectedInput object

**Repository:** BESS_tools  
**Status:** Open  
**Created:** 2024-10-25  
**Updated:** 2024-10-25  
**Author:** @harish-ramar  
**Assignees:** @harish-ramar  

[View on GitHub](https://github.com/Simtestlab/BESS_tools/issues/69)

## Description

1. Fix the node data duplication in the saved data.
2. Currently the connectedInput object has the connectedNode's Id, type, name, handle and handleId using this we need to create the subflow's input and output handlers using this data.