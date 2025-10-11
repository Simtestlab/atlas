# Issue #23: Person Management APIs

**Repository:** tree_life  
**Status:** Closed  
**Created:** 2025-09-04  
**Updated:** 2025-09-10  
**Closed:** 2025-09-10  
**Author:** @harish-ramar  
**Assignees:** @harish-ramar  
**Labels:** `Iteration #1`  

[View on GitHub](https://github.com/Simtestlab/tree_life/issues/23)

## Description

DOD: As a developer create a person management APIs that is used while registration and validation after the registration of a person

1. POST /persons
    * Create new person record
    * Body: {first_name, last_name, email, phone}
2. GET /persons/{person_id}
    * Fetch person details by ID
    * Used for verification after registration
3. GET /persons/{person_id}/tree
    * Get person with their ordered tree details (joined view)
    * Calls get_person_with_tree RPC equivalent
4. GET /persons/{person_id}/has-order
    * Check if person has ordered a tree
    * Returns {hasOrdered: bool, treeId: int|null}