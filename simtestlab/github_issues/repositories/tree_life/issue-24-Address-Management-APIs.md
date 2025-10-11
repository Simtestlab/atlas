# Issue #24: Address Management APIs

**Repository:** tree_life  
**Status:** Closed  
**Created:** 2025-09-04  
**Updated:** 2025-09-10  
**Closed:** 2025-09-10  
**Author:** @harish-ramar  
**Assignees:** @harish-ramar  

[View on GitHub](https://github.com/Simtestlab/tree_life/issues/24)

## Description

DOD: As a developer create the APIs that is required to manage the address of the registered user

1. POST /persons/{person_id}/addresses
    * Create address for a person
    * Body: {city, pin_code, state, district, tree_name?: optional}
    * Complex flow: If tree_name provided, orders tree first, then creates address only on success
2. GET /addresses?person_id={person_id}
    * Fetch address for a specific person