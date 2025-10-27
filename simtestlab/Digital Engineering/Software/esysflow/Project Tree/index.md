# 🌳 ESYSFLOW — Project Tree Module  


---

## 📖 Table of Contents
1. [What is Project Tree?](#what-is-project-tree)
2. [Quick Start](#quick-start)
3. [Key Features](#key-features)
4. [User & Data Flow Roadmap](#user--data-flow-roadmap)
5. [File Structure](#file-structure)
6. [Important Functions & Data Movement](#important-functions--data-movement)
7. [Smart Numbering System](#smart-numbering-system)
8. [Two-Way Synchronization](#two-way-synchronization)
9. [Adding New Node Types](#adding-new-node-types)
10.  [Navigation flow of the Module](#The-overall-flow-of-the-Project-Tree-Module)

---

## 🌟 What is Project Tree?

The **Project Tree** is your workflow’s “map” — a live, interactive outline of all flows, subflows, and nodes in your simulation.  
Think of it as a **file explorer** for your engineering logic:  
- **Flows** = Folders  
- **Nodes** = Files  
- **Numbers** = Automatic, always up-to-date order

It’s always in sync with the Canvas, so what you see is what you get!

---

## 🚀 Quick Start

- **Non-technical?**  
  Just right-click a flow or subflow in the Project Tree, pick a node, and watch it appear in the canvas and tree instantly.
- **Technical?**  
  All logic is modularized, with real-time sync, deduplication, and smart numbering built-in.

---

## ✨ Key Features

- **Right-Click Node Addition:**  
  Add nodes directly from the tree, with a searchable menu.  
- **Smart Numbering:**  
  Nodes are numbered by position and connection, so your logic always makes sense.
- **Two-Way Sync:**  
  Canvas and tree update each other, instantly and safely.
- **Drag & Drop:**  
  Still love the classic way? Drag from the Library and drop on the canvas.

---

## 🗺️ User & Data Flow Roadmap

### 👤 **User Journey: What Happens Step by Step?**

#### **A. Right-Click Add Node (with Data Flow & Function Triggers)**

1. **User right-clicks** a flow/subflow in the Project Tree  
   → `handleContextMenu()` in `CustomTreeItem.tsx`  
   → Passes event to `ProjectTree.tsx`  
   → Opens context menu at mouse position

2. **User selects node type** in the context menu  
   → `handleNodeTypeSelect()` in `useProjectTreeContextMenu.tsx`  
   → Triggers `createNodeDataFromRightClick()` in `rightClickUtils.ts`  
   → Calculates canvas center, builds node data object

3. **Node data is ready**  
   → `handleRightClickDrop()` in `flowDropHandler.ts`  
   → Creates new node object (unique ID, type, position, default data from `graph.json`)

4. **Node is added to the correct tab**  
   → `createSetNodesForTab()` in `useFlow.tsx`  
   → Updates the nodes array for the specific tab

5. **Tab data changes**  
   → `useCanvasEffects.ts` (Effect 2)  
   → Syncs tab data to ReactFlow canvas

6. **Canvas state changes**  
   → `useCanvasEffects.ts` (Effect 1)  
   → Syncs ReactFlow state back to tab data (flags prevent loops)

7. **Tree rebuilds**  
   → `buildTree()` & `mapTreeDataToTreeViewItems()` in `projectTreeUtils.ts`  
   → Updates Project Tree UI, applies deduplication

8. **Numbering recalculated**  
   → `analyzePositionalHierarchy()` in `positionalHierarchyAnalyzer.ts`  
   → or `analyzeConnectionOrder()` in `flowPositionAnalysis.ts`  
   → Applies smart numbering (position or connection-based)

**Data Movement:**  
- User action → Event handler → Context menu state  
- Node type selection → Node data object (with position, type, tab)  
- Node data → Node creation → Tab nodes array  
- Tab nodes → Canvas nodes (sync)  
- Canvas nodes → Tree structure (rebuild)  
- Tree structure → UI update & numbering

---

#### **B. Drag & Drop Add Node (with Data Flow & Function Triggers)**

1. **User drags node** from Library  
   → ReactFlow drag event

2. **User drops node** on canvas  
   → ReactFlow `onDrop` handler in `canvas.tsx`  
   → Calls node creation logic

3. **Node data is ready**  
   → `handleDrop()` or similar in `flowDropHandler.ts`  
   → Creates node at drop position

4. **Node added to tab**  
   → `createSetNodesForTab()` in `useFlow.tsx`  
   → Updates tab's node list

5. **Tab data changes**  
   → `useCanvasEffects.ts`  
   → Syncs to canvas and tree (same as above)

6. **Tree rebuilds**  
   → `buildTree()` & `mapTreeDataToTreeViewItems()`  
   → Updates Project Tree UI

---

#### **C. Data Conversion & Movement (Function to Function, File to File)**

- **Node type selection** (string)  
  → `createNodeDataFromRightClick()`  
  → Returns node data object `{ type, label, position, parentId, targetTabId }`

- **Node data object**  
  → `handleRightClickDrop()`  
  → Converts to ReactFlow node object `{ id, type, position, data: {...} }`

- **ReactFlow node object**  
  → `createSetNodesForTab()`  
  → Updates tab's `nodes` array

- **Tab's nodes array**  
  → `useCanvasEffects.ts`  
  → Syncs to ReactFlow's `nodes` state

- **ReactFlow's nodes state**  
  → `buildTree()`  
  → Converts to tree structure for UI

- **Tree structure**  
  → `mapTreeDataToTreeViewItems()`  
  → Converts to UI-friendly format, deduplicates nodes

---

#### **D. Data Format Changes**

| Stage | Data Format | Example |
|-------|------------|---------|
| Node type selection | String | `"Vector"` |
| Node data object | Object | `{ type: "vector", label: "Vector", position: {x, y}, ... }` |
| ReactFlow node | Object | `{ id, type, position, data: {...} }` |
| Tab nodes array | Array | `[node1, node2, ...]` |
| Tree structure | Nested objects | `{ id, label, children: [...] }` |
| TreeView items | UI objects | `{ id, label, type, children, ... }` |

---

## 📁 File Structure

```
src/
└── modules/
    └── canvas/
        ├── components/
        │   └── canvas.tsx
        ├── hooks/
        │   ├── useCanvasPage.ts
        │   ├── useFlow.tsx
        │   └── useCanvasEffects.ts
        ├── utils/
        │   └── flowDropHandler.ts
        ├── widgets/
        │   ├── sidebar/
        │   │   └── component/
        │   │       └── sidebar.tsx
        │   └── projectTree/
        │       ├── components/
        │       │   ├── ProjectTree.tsx
        │       │   ├── CustomTreeItem.tsx
        │       │   └── ProjectTreeContextMenu.tsx
        │       ├── hooks/
        │       │   └── useProjectTreeContextMenu.tsx
        │       └── utils/
        │           ├── projectTreeUtils.ts
        │           ├── rightClickUtils.ts
        │           ├── positionalHierarchyAnalyzer.ts
        │           └── flowPositionAnalysis.ts
public/
└── data/
    └── library/
        └── graph.json
```

---

## 🔧 Important Functions & Data Movement

| Function | File | Trigger | Purpose | Data In | Data Out |
|----------|------|---------|---------|---------|----------|
| `handleContextMenu()` | CustomTreeItem.tsx | Right-click | Opens context menu | Mouse event | Context menu state |
| `handleNodeTypeSelect()` | useProjectTreeContextMenu.tsx | Node type select | Orchestrates node creation | Node type string | Node data object |
| `createNodeDataFromRightClick()` | rightClickUtils.ts | Node type select | Calculates center, builds node data | Node type, context | Node data object |
| `handleRightClickDrop()` | flowDropHandler.ts | Node data ready | Creates ReactFlow node | Node data object | ReactFlow node object |
| `createSetNodesForTab()` | useFlow.tsx | Node creation | Updates tab's nodes | Node updater | Updated tab nodes |
| `buildTree()` | projectTreeUtils.ts | Tab data changes | Builds tree structure | Tabs, nodes | Tree structure |
| `mapTreeDataToTreeViewItems()` | projectTreeUtils.ts | Tree build | Converts to UI items | Tree structure | TreeView items |
| `analyzePositionalHierarchy()` | positionalHierarchyAnalyzer.ts | Tree rebuild | Position-based ordering | Nodes | Ordered node IDs |
| `analyzeConnectionOrder()` | flowPositionAnalysis.ts | Tree rebuild | Topology-based ordering | Nodes, edges | Ordered node IDs |
| `useCanvasEffects` | useCanvasEffects.ts | State change | Two-way sync | Nodes/edges/tabs | Synced state |

---

## 🔢 Smart Numbering System

- **Position-based:**  
  Nodes are numbered top-to-bottom, then left-to-right (like reading a book).
- **Connection-based:**  
  If nodes are connected, sources always come before targets (topological sort).
- **Automatic:**  
  Numbering updates instantly as you move, connect, or add nodes.

---

## 🔄 Two-Way Synchronization

- **Canvas → Tabs:**  
  Any change on the canvas updates the stored tab data.
- **Tabs → Canvas:**  
  Switching tabs or loading data updates the canvas.
- **No infinite loops:**  
  Sync flags (`isReactFlowUpdate`, `isTabUpdate`) and deep equality checks keep updates safe and efficient.

---

## ➕ Adding New Node Types

1. Add node definition to `public/data/library/graph.json`.
2. If needed, add special logic in node implementation.
3. Node appears in right-click menu automatically (if menu reads from graph.json).
4. Test by right-clicking and dragging from Library.

---


## The overall  flow of the Project Tree Module

![Project Tree Flow Diagram](./FlowDiagram.jpg)

---


