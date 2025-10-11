# Issue #6: Excel sheet updated with new client requirement

**Repository:** cantex_cpp  
**Status:** Open  
**Created:** 2024-11-24  
**Updated:** 2024-11-24  
**Author:** @nallasivamselvaraj  
**Assignees:** @nallasivamselvaraj  

[View on GitHub](https://github.com/Simtestlab/cantex_cpp/issues/6)

## Description


Updated client requirement for the command packet structure:

The checksum was missed previously, resulting in a 76-byte packet instead of the required 77 bytes. This issue has been resolved, and the packet now correctly includes the checksum, meeting the client's requirement.

command packet Spread sheet : https://docs.google.com/spreadsheets/d/1sSzpTP_70lhclgLvdIy5wMRZWhR028Ky/edit?gid=1570633754#gid=1570633754

@aeroramesh @sajimotrax 
