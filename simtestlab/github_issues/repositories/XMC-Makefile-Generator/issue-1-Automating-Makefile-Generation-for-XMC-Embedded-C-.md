# Issue #1: Automating Makefile Generation for XMC Embedded C Projects Using ARM-GCC

**Repository:** XMC-Makefile-Generator  
**Status:** Closed  
**Created:** 2025-02-18  
**Updated:** 2025-03-06  
**Closed:** 2025-03-06  
**Author:** @crmaarimuthu  
**Assignees:** @crmaarimuthu  

[View on GitHub](https://github.com/Simtestlab/XMC-Makefile-Generator/issues/1)

## Description

DOD:

1. Code Implementation
✅ Script scans the project directory and identifies C (.c), Assembly (.s, .S), and linker script (.ld) files.
✅ Generates a Makefile with correctly structured build rules.
✅ Filters unnecessary directories (e.g., Debug, Build, Docs, Libraries/CMSIS, Libraries/inc).
✅ Supports ARM-GCC toolchain for XMC microcontrollers.

2. Functionality & Features
✅ Creates object files (.o) and manages dependencies (.d files).
✅ Supports recursive scanning of directories.
✅ Automatically detects subdirectories containing source files.
✅ Ensures proper compilation and linking with generated Makefile.

3. Documentation & Usability
✅ Provides a clear README.md explaining usage, installation, and dependencies.
✅ Well-commented Python code for maintainability.
✅ Generates a clean and readable Makefile with structured rules.

4. Testing & Validation
✅ Successfully builds a sample XMC project using the generated Makefile.
✅ Ensures Makefile correctly compiles and links project files.
✅ Validates that no unnecessary files or directories are included.