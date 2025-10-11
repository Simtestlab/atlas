# Issue #422: 4.3 Create APIs and stores to update and broadcast chats

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-09-16  
**Updated:** 2025-09-24  
**Author:** @harish-ramar  
**Assignees:** @niteshkumar1710  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/422)

## Description

### DOD
As a developer, design and implement backend services, utility functions, and APIs to enable real-time group chat functionality within a project context. This chat system should allow users with access to a specific project to send, receive, store, and broadcast messages. The "group" is scoped to the project (e.g., a collaborative canvas in React Flow), and messages can reference or relate to specific nodes and edges on the canvas. The system must support real-time broadcasting to connected users, persistent storage of chat history, and access control based on project permissions.
This feature mimics a group chat in applications like Slack or Discord, but tailored to project collaboration where discussions often revolve around diagram elements (nodes/edges).
Key Requirements

### Scope and Context:

Project as Group: Each project acts as a chat room. Users must have explicit access to the project (e.g., via roles like owner, editor, viewer) to participate.
**Message Relation to Canvas**: Messages can optionally link to specific nodes or edges (e.g., via IDs). This allows for contextual discussions, such as commenting on a node's configuration or an edge's flow logic.
**Real-Time Broadcasting**: Use WebSockets or similar for instant message delivery to all connected users in the project.
**Persistence**: Store chat history in a database for retrieval (e.g., loading past messages on join or page refresh).
**Access Control**: Enforce project-level permissions; non-members cannot join or send. Any user can view the chat history irrespective of their access.