# Issue #57: run_unit_test_loaded_model_error

**Repository:** esimtest_pro  
**Status:** Closed  
**Created:** 2024-12-01  
**Updated:** 2025-01-05  
**Closed:** 2025-01-05  
**Author:** @AgilanArulchelvam  
**Assignees:** @AgilanArulchelvam  

[View on GitHub](https://github.com/Simtestlab/esimtest_pro/issues/57)

## Description

DOD:

- A test case is loaded and executed using the "Run Unit Test" option.
- A new test case for a different model is created and executed within the same interface.
- Subsequently, another test case file is loaded and executed.
- The previous instance is not closed, causing the model to run in the same instance.
- This results in an error due to overlapping instances and mismatch of testcase and model  @aeroramesh  @sajimotrax 