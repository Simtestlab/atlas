# Issue #15: Port rendering inside sub flow

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2024-11-22  
**Updated:** 2024-12-13  
**Closed:** 2024-12-04  
**Author:** @harish-ramar  
**Assignees:** @harish-ramar  
**Labels:** `review`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/15)

## Description

We need to implement a subflow creation that is similar to the matlab's subsystem.

# References from matlab:

1. While creating subflow we can see in the image the edge leading to the convert and the convert as been selected and created as subflow.
![Image](https://github.com/user-attachments/assets/b913e7dd-1199-4dec-9f18-d1384dcfb910)

2. After creating it as a subflow we can note the inside the subflow the inport node as been automatically connected to an inport node and it has been externally created.
![Image](https://github.com/user-attachments/assets/eb73ce9a-ff1a-4772-8652-43970ba7c43c)
![Image](https://github.com/user-attachments/assets/b332a067-d23e-4eb9-a175-5edd6dce01e0)

# Implementation Planning:
*When these block of nodes and created as subflow:*
![Image](https://github.com/user-attachments/assets/930f74c0-7cff-4066-9c00-34f6fb25f17c)

*It is currently creating like the image shown below:*
![Image](https://github.com/user-attachments/assets/52404e65-4072-4e13-bcd4-93e33c7c62dd)

*But we need to automatically add inport nodes for the input handlers that are empty and outport nodes for the output handlers that are empty like shown in the image:*
![Image](https://github.com/user-attachments/assets/d0c9aff8-1f2d-4c13-a244-e6a70513d10f)

