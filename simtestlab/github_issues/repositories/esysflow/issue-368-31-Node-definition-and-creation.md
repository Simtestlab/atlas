# Issue #368: 3.1 Node definition and creation

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-08-09  
**Updated:** 2025-08-09  
**Author:** @divya-rosy  
**Labels:** `UI`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/368)

## Description

DOD: We need to provide a dialogue box to define a node’s input and output handler. We need a form similar to the one shown below.
	 The user needs to ensure that the APIs to add nodes to the library exist before working on the task. Also the developer should be aware of the functionalities of the API.
	It should have the option to define multiple input and output handlers. Also a code definition editor using Monaco Editor.
	Finally it should return a JSON structure shown below. And this dialogue box is only visible to an admin user.

"nodeName": {
    "name": “Node Name",
    "type": “node type”,
    "handlers": {
      "inputs": [
        {
          "name": “input name",
          "type": “input type",
          "is_multi_input": false,
          "value": null,
          “allowed_types”: [ ]
        }
      ],
      "outputs": [
        {
          "name": “output name",
          "type": “output_type",
          "value": null,
          “allowed_types”: [ ]
        }
      ],
    },
    definition: “code definition as string”
  }

<img width="396" height="887" alt="Image" src="https://github.com/user-attachments/assets/69253a1f-c45c-40ed-b2b5-2787a9520c8d" />
