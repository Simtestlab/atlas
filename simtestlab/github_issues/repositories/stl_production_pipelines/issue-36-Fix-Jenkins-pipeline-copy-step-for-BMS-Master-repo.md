# Issue #36: Fix Jenkins pipeline copy step for BMS Master repo

**Repository:** stl_production_pipelines  
**Status:** Open  
**Created:** 2025-09-18  
**Updated:** 2025-09-18  
**Author:** @nallasivamselvaraj  
**Assignees:** @nallasivamselvaraj  

[View on GitHub](https://github.com/Simtestlab/stl_production_pipelines/issues/36)

## Description

The pipeline fails at the stage "Copy Python Scripts to BMS_MASTER" because the folder BMS_MASTER does not exist.