# Issue #14: Edge Selection Issue

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2024-11-22  
**Updated:** 2024-12-13  
**Closed:** 2024-11-22  
**Author:** @harish-ramar  
**Assignees:** @harish-ramar  
**Labels:** `review`, `Task Reviewed`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/14)

## Description

### Issue:
Currently the edge selection is not working as expected sometimes it is selected and sometimes not getting selected.

### As you can see in the image the nodes are selected but the edges are not highlighted.
![Image](https://github.com/user-attachments/assets/d4e0c58f-f613-430f-90dc-479bdfb8b044)

### In the second image, Both edges are selected and only the left edge is highlighted.
![Image](https://github.com/user-attachments/assets/3a82c8d5-9923-4d8d-92c4-d9f990f400e6)

### In the last image, Both edges are selected and also they are highlighted properly.
![Image](https://github.com/user-attachments/assets/50ecaf35-6980-4183-8516-a8f059973926)

### Proposed Fix:
1. First need to analyze and redefine the function that is responsible for the selection process.
2. Need to redefine the working of **OnSelectionChange() and onEdgeClick()**.

### Solved;
The issue lies in the useFlow in these lines of code which is responsible for the edge style updating, it has been infinity updating the values of the edges does results in the edge selection inconsistency and currently it has been commented out.
```
useEffect(() => { 
    const els = [...edges];
    const maped = els.map((x) => ({
      ...x,
      type: edgeStyleType,
    }));
    setEdges(maped);
  }, [edgeStyleType, edges, setEdges]);
```

@aeroramesh @sajimotrax 
