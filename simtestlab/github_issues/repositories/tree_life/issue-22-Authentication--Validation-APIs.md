# Issue #22: Authentication & Validation APIs

**Repository:** tree_life  
**Status:** Closed  
**Created:** 2025-09-04  
**Updated:** 2025-09-10  
**Closed:** 2025-09-10  
**Author:** @harish-ramar  
**Assignees:** @harish-ramar  

[View on GitHub](https://github.com/Simtestlab/tree_life/issues/22)

## Description

DOD: As a developer create a API to validate and authenticate the user based on the email and phone number (if needed).

1. GET /persons/email-exists?email={email}
    * Check if email already exists in database
    * Used during registration flow
    * If the registered user is registered on the same day we should't allow the user to register
    * If the user hasn't registered on the current day we can validate the user