# Vector Node to Graph Generation Data Flow

![data flow](image%201.jpg)


## Overview
This document describes the complete data flow process in EsysFlow from selecting a vector node in the sidebar to generating interactive graphs on the canvas. The system follows a modular architecture where data flows through multiple components, APIs, and processing layers.

## System Architecture Components

### Core Files Involved
- **Sidebar Component**: `src/modules/canvas/widgets/sidebar/component/sidebar.tsx`
- **Canvas Component**: `src/modules/canvas/components/canvas.tsx`
- **Vector Node Component**: `src/components/nodes/VectorNode.tsx`
- **Graph Node Components**: `src/components/nodes/[GraphType]Node.tsx`
- **Flow Utils**: `src/modules/canvas/widgets/spreadsheet/hooks/flowUtils.ts`
- **Library API**: `src/app/api/library/route.ts`
- **Library Data**: `public/data/library/graph.json`
- **Save API**: `src/app/api/saveFlowData/route.ts`

## Phase 1: Node Library Loading

### 1.1 Application Startup
When the application loads, the sidebar component initiates the library data fetching process.

### 1.2 Library API Call
- **Endpoint**: `/api/library`
- **Purpose**: Fetches all available node definitions including vector nodes and graph types
- **Response**: Returns structured data containing node categories, types, and configurations

### 1.3 Library Data Structure
The library contains categorized nodes:
- **Data Sources**: Including Vector nodes
- **Arithmetic**: Mathematical operations
- **Graph**: Various chart types (Line Plot, Bar Chart, Pie Chart, etc.)
- **3D Graph**: Three-dimensional visualizations
- **Financial**: Financial chart types
- **Polar & Radar**: Specialized chart formats
- **Map & Geo**: Geographic visualizations

### 1.4 Graph Types Extraction
The system specifically filters graph-related categories and stores them in the graph store for later reference during plotting operations.

## Phase 2: Vector Node Selection and Drag Operation

### 2.1 User Interaction
User browses the sidebar library and locates a Vector node under the Data Sources category.

### 2.2 Drag Initiation
When user starts dragging a Vector node:
- **Event Triggered**: `onDragStart` function in sidebar component
- **Data Transfer**: Sets drag data including node label and type
- **Type Conversion**: Converts node name to camelCase format for internal processing

### 2.3 Drag Data Payload
The drag operation carries:
- **Label**: Human-readable name ("Vector")
- **Type**: Internal identifier ("vector")
- **Category**: Source category information

## Phase 3: Canvas Drop and Node Creation

### 3.1 Drop Zone Detection
Canvas component detects the drop event and validates the drop zone area.

### 3.2 Node Instantiation
- **Position Calculation**: Determines node placement coordinates
- **ID Generation**: Creates unique identifier for the new node
- **Component Selection**: Maps node type to appropriate React component
- **Initial Data**: Sets default properties and empty data structures

### 3.3 Node Registration
The new vector node is registered in the React Flow state management system and becomes part of the canvas node collection.

## Phase 4: Vector Node Configuration

### 4.1 Vector Type Selection Interface
The Vector node component renders a configuration interface allowing users to select:
- **Time Series Data**: X-axis as timestamps, Y-axis as values
- **Numeric Arrays**: X and Y coordinate pairs
- **Categorical Data**: Labels and corresponding values
- **Multi-dimensional Data**: X, Y, and Z coordinates for 3D plots

### 4.2 Data Input Methods
Users can input data through:
- **Manual Entry**: Direct typing in input fields
- **Generated Data**: Synthetic data for testing

### 4.3 Data Validation and Formatting
The system validates input data for:
- **Format Consistency**: Ensures arrays have matching lengths
- **Data Types**: Validates numeric vs string data appropriately
- **Range Validation**: Checks for reasonable value ranges
- **Array Structure**: Confirms proper array formatting

### 4.4 Internal Data Storage
Processed data is stored in the node's data structure:
- **X Values**: Array of x-coordinate or category data
- **Y Values**: Array of y-coordinate or numeric values
- **Z Values**: Optional third dimension for 3D plots
- **Labels**: Category names for categorical data
- **Metadata**: Type information, formatting preferences

## Phase 5: Graph Node Selection and Configuration

### 5.1 Graph Type Selection
User selects appropriate graph type from the library:
- **Line Plot**: For continuous data trends
- **Bar Chart**: For categorical comparisons
- **Pie Chart**: For proportion visualization
- **Scatter Plot**: For correlation analysis
- **3D Surface**: For three-dimensional data
- **Financial Charts**: For time-series financial data

### 5.2 Graph Node Placement
User drags and drops the selected graph node onto the canvas, following the same drag-and-drop pattern as vector nodes.

## Phase 6: Data Connection Establishment

### 6.1 Connection Interface
User creates data connections by:
- **Output Handle**: Clicking on vector node's output port
- **Input Handle**: Connecting to graph node's input port
- **Edge Creation**: System creates a visual connection line

### 6.2 Data Relationship Mapping
The connection establishes:
- **Source Reference**: Graph node references vector node ID
- **Data Access Path**: Direct access to vector's processed data
- **Update Propagation**: Changes in vector data automatically update graph
- **Connection Metadata**: Stores connection type and data mapping information

## Phase 7: Graph Rendering and Visualization

### 7.1 Data Processing Pipeline
When connection is established:
- **Data Extraction**: Graph node retrieves data from connected vector node
- **Format Conversion**: Converts internal data format to chart library format
- **Configuration Merge**: Combines data with graph-specific settings
- **Rendering Preparation**: Prepares data structure for visualization library

### 7.2 Chart Library Integration
The system uses Plotly.js for rendering:
- **Data Binding**: Maps vector data to chart axes and properties
- **Style Application**: Applies visual styling and theming
- **Interaction Setup**: Configures zoom, pan, and hover interactions
- **Performance Optimization**: Handles large datasets efficiently





## Data Flow Summary

### Linear Process Flow
1. **Library Loading** → System fetches available node types
2. **Node Selection** → User chooses vector node from sidebar
3. **Drag and Drop** → Node is placed on canvas
4. **Data Configuration** → User inputs or imports data
5. **Graph Selection** → User chooses appropriate chart type
6. **Connection Creation** → Data flow is established
7. **Visualization** → Graph is rendered with vector data
8. **Interaction** → User can explore and modify visualization
9. **Persistence** → Flow state is saved for future use

### Key Integration Points
- **Sidebar ↔ Canvas**: Drag and drop node creation
- **Vector ↔ Graph**: Data connection and flow
- **Canvas ↔ Storage**: State persistence and retrieval
- **Components ↔ APIs**: Data fetching and saving operations
- **UI ↔ Data**: User interaction and data manipulation





# Flow Data Extraction and JSON Storage Documentation
![json save](image%202.jpg)
## Overview

This document describes the complete data flow process for extracting flow data from the EsysFlow application and saving it as JSON files locally. The process involves multiple components working together to extract, process, and store flow hierarchy data.

## Architecture Overview

The flow data extraction and storage system consists of three main components:

1. **Flow Utils Module** - Handles data extraction and preparation
2. **Flow Hierarchy Utils** - Processes flow structure and node relationships  
3. **API Endpoint** - Handles file storage operations

## Data Flow Process

### 1. User Interaction (Save Button Click)

When a user clicks the "Save" button in the application header:

```typescript
// Location: src/components/header/index.tsx
const onFlowSave = async () => {
  // Triggered when user clicks Save button
  // Processes current flow state and initiates save operation
}
```

### 2. Flow Data Extraction

The extraction process begins by gathering flow data from active tabs:

#### 2.1 Tab Structure
```typescript
type Tab = {
  id: string;        // Unique identifier for the tab/flow
  name: string;      // Display name of the flow
  nodes: Node[];     // Array of nodes in the flow
  edges: Edge[];     // Array of edges connecting nodes
};
```

#### 2.2 Node Information Extraction
```typescript
// Location: src/modules/canvas/utils/flowHierarchyUtils.ts
export const extractNodeInfo = (node: Node): NodeInfo | null => {
  // Extracts essential node information including:
  // - Node ID and name
  // - Node type and component
  // - Input/output connections
  // - Data values and configurations
}
```

### 3. Flow Hierarchy Processing

The system processes the flow structure to understand relationships between nodes and subflows:

#### 3.1 Hierarchy Structure
```typescript
export type FlowHierarchy = {
  nodes: NodeInfo[];      // Root level nodes
  subflows: SubflowInfo[]; // Contains nested subflows
};

export type SubflowInfo = {
  id: string;
  name: string;
  nodes: NodeInfo[];
  subflows: SubflowInfo[]; // Recursive nesting support
};
```

#### 3.2 Processing Logic
```typescript
export const extractFlowHierarchy = (tabs: Tab[]): FlowHierarchy => {
  // 1. Identifies root flow (first tab)
  // 2. Maps subflow relationships
  // 3. Processes nodes recursively
  // 4. Handles circular reference prevention
  // 5. Returns structured hierarchy
}
```

### 4. Data Preparation for JSON Export

#### 4.1 Node Data Processing
The system extracts relevant data from different node types:

```typescript
// Location: src/modules/canvas/widgets/spreadsheet/hooks/flowUtils.ts
const extractNodeData = (nodes: NodeInfo[] | Node[], edges: Edge[] = []): Record<string, any> => {
  // Processes nodes to extract:
  // - Basic node information (id, name, type)
  // - Data values (x, y, z coordinates)
  // - Labels and values for charts/graphs
  // - Connection relationships between nodes
}
```

#### 4.2 Special Node Type Handling

**Graph/Plot Nodes:**
- Line plots, bar charts, Plotly graphs
- Identified by node type or component name
- Connected to data source nodes via edges

**Data Source Nodes:**
- Arithmetic nodes, data input nodes
- Contains actual data values (arrays of numbers, labels)
- Connected to visualization nodes

#### 4.3 Connection Mapping
The system maps connections between data nodes and graph nodes:

```typescript
// Identifies graph nodes
const isGraphNode = nodeType === 'linePlot' || 
                   nodeType === 'PlotlyGraph' || 
                   nodeType === 'bar' ||
                   nodeType.toLowerCase().includes('plot');

// Maps data flow connections
edges.forEach(edge => {
  if (graphNodeIds.includes(edge.target)) {
    nodeConnections[edge.source].push(edge.target);
  }
});
```

### 5. JSON Structure Generation

#### 5.1 Final JSON Format
The system generates a structured JSON format for each flow:

```json
[
  {
    "flow-id": "unique-flow-identifier",
    "flow-name": "Flow Display Name",
    "nodes": [
      {
        "id": "node-id",
        "node_name": "Node Display Name",
        "connected_graph_id": "target-graph-node-id",
        "graph_name": "Connected Graph Name",
        "x": [1, 2, 3, 4, 5],
        "y": [10, 20, 30, 40, 50],
        "labels": ["Label1", "Label2"],
        "values": [100, 200, 300]
      }
    ]
  }
]
```

#### 5.2 Data Filtering
The system applies intelligent filtering:
- **Excludes**: Graph/plot nodes from node list (they're referenced via connections)
- **Includes**: Only nodes with actual data or graph connections
- **Removes**: Duplicate nodes across multiple tabs
- **Processes**: Inport/outport nodes are skipped

### 6. API Endpoint Processing

#### 6.1 Save Flow Data API
```typescript
// Location: src/app/api/saveFlowData/route.ts
export async function POST(request: NextRequest) {
  // 1. Receives processed flow data
  // 2. Creates public/data directory if needed
  // 3. Writes JSON file with formatted data
  // 4. Returns success response with file path
}
```

#### 6.2 File Storage Location
```
project-root/
  public/
    data/
      flow-data.json        <- Main flow data file
      custom-name.json      <- User-specified filename
```


## Data Transformation Examples

### Input: React Flow Node
```typescript
{
  id: "node-123",
  type: "arithmetic",
  data: {
    name: "Data Source",
    component: "Arithmetic",
    data: {
      inputs: [
        {
          identifier: "data",
          value: {
            x: [1, 2, 3],
            y: [10, 20, 30]
          }
        }
      ]
    }
  }
}
```

### Output: JSON Node
```json
{
  "id": "node-123",
  "node_name": "Data Source",
  "connected_graph_id": "plot-456",
  "graph_name": "Line Chart",
  "x": [1, 2, 3],
  "y": [10, 20, 30]
}
```

## Integration Points

### 1. Header Component Integration
```typescript
// Save button triggers the flow data export
<button onClick={() => {
  // Extract flow hierarchy
  const hierarchy = extractFlowHierarchy(tabs);
  // Save to JSON
  saveFlowDataToJson(tabs, flowName);
}}>
  Save
</button>
```

### 2. Store Integration
The system integrates with Zustand stores for state management:
- Flow state persistence
- Node data updates
- Tab management

### 3. File System Integration
- Creates directory structure automatically
- Handles file naming conflicts
- Provides file path feedback to user

