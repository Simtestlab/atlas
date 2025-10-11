# Issue #387: 6.4 Plotting Graph

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-08-09  
**Updated:** 2025-08-09  
**Author:** @divya-rosy  
**Labels:** `Feature`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/387)

## Description

DOD: The current system only permits users to modify vector values, with changes reflected in the graph.
	We need to enhance the line plot functionality to allow data plotted directly on the graph to update the corresponding vector data. In the existing plot interface, replace the close button with a close icon.

<img width="728" height="282" alt="Image" src="https://github.com/user-attachments/assets/601cd673-0f99-4ff6-9b54-b38ad6357c26" />

Additionally, include an edit icon next to the close icon. Clicking the edit icon should present two options: editing the existing data or starting a new instance.
	If the user chooses to edit existing data, the current graph data should be retained, enabling direct editing or plotting within the graph window.
	If the user selects a new instance, the existing data should be cleared, allowing the user to plot from scratch.
	This functionality should be implemented separately without altering the current functions and hooks. And utilise the existing store to update the data asynchronously.
