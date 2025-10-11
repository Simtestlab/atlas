# Issue #421: 2.4 Flow Hierarchy analyser

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-09-16  
**Updated:** 2025-09-27  
**Author:** @harish-ramar  
**Assignees:** @gurusatura  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/421)

## Description

DOD: As a developer, create a utility function that takes the `nodes` array from a React Flow canvas as input. The function should analyze the positions (x and y coordinates) of each node and generate a hierarchical structure representing the flow order. Assume a left-to-right flow direction by default, where nodes are sorted primarily by increasing x-coordinate (leftmost first). If x-coordinates are identical or very close (within a small threshold, e.g., 10 units), use y-coordinates as a secondary sort key (top-to-bottom, assuming y increases downward).

The hierarchy should be returned as a structured output, such as a nested array or object, to represent potential levels or groupings if nodes are vertically aligned (e.g., branches in a flowchart). For simplicity in flat structures, it can be a simple ordered list of node IDs or labels.

#### Input
- `nodes`: An array of node objects from React Flow, where each node has at least the following properties:
  - `id`: Unique identifier (string).
  - `position`: An object with `x` (number) and `y` (number) coordinates.
  - Optional: `data.label` or similar for display names (fallback to `id` if not present).

Example input structure:
```javascript
[
  { id: 'A', position: { x: -72874.76209874109, y: -28100.149352757056 }, data: { label: 'Node A' } },
  { id: 'B', position: { x: -71287.91841072992, y: -26552.834126154165 }, data: { label: 'Node B' } }
]
```

#### Output
- A hierarchical representation of the nodes, sorted by position.

Example output for the given positions (assuming left-to-right sorting by x):
```javascript
{
  hierarchy: ['A', 'B'],  // Ordered node IDs
}
```
Visual hierarchy representation (for console/display):
```
1. Node A
2. Node B
```