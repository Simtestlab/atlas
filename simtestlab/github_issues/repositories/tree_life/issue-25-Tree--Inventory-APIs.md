# Issue #25: Tree & Inventory APIs

**Repository:** tree_life  
**Status:** Closed  
**Created:** 2025-09-04  
**Updated:** 2025-09-10  
**Closed:** 2025-09-10  
**Author:** @harish-ramar  
**Assignees:** @harish-ramar  

[View on GitHub](https://github.com/Simtestlab/tree_life/issues/25)

## Description

DOD: As a developer create APIs to handle the Inventory for the Tree Management

1. GET /trees/available
    * List trees available for ordering
    * Implements get_available_trees() RPC logic (stock_available > persons_ordered)
Order Management APIs
2. POST /orders
    * Order a tree for a person
    * Body: {tree_name, person_id}
    * Implements order_tree_safely RPC (handles concurrency)
3. POST /orders/cancel
    * Cancel a person's tree order
    * Body: {person_id}
    * Implements cancel_tree_order RPC