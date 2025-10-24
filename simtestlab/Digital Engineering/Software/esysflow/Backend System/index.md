# Websockets and Webhooks Architecture

## Overview

This backend implements a **real-time communication system** using **FastAPI** with **WebSocket** endpoints and optional **webhook notifications**.
It is designed to handle bi-directional communication between connected clients while maintaining a reliable event flow for system monitoring and external integrations.

The system enables:

* Broadcasting messages to all connected clients
* Tracking client connections and disconnections
* Handling structured events (`ping`, `private`, `broadcast`)
* Emitting server status updates and metrics through webhook notifications

---

## Core Architecture

The backend uses two primary components:

1. **WebSocket Routes** — manage persistent client connections and real-time communication.
2. **Webhook Definitions** — define external callbacks triggered by specific system events (message broadcasts, connection updates, etc.).

```
Client (WebSocket)
   │
   │   Connects via /ws or /ws/{client_id}
   ▼
FastAPI WebSocket Router
   │
   ├── Receives messages (JSON or text)
   ├── Dispatches to handler (handle_websocket_message)
   ├── Manages ConnectionManager state
   ▼
ConnectionManager
   ├── Tracks active WebSocket connections
   ├── Broadcasts messages to all clients
   └── Notifies Webhooks on key events
```

---

## Key Components

### 1. Connection Manager

Responsible for managing active WebSocket sessions and broadcasting messages.

**Responsibilities:**

* Maintain a set of connected clients
* Broadcast messages to all or specific clients
* Handle client joins/disconnects
* Trigger webhook notifications for connection events

A simplified conceptual API:

```python
class ConnectionManager:
    async def connect(self, websocket: WebSocket): ...
    def disconnect(self, websocket: WebSocket): ...
    async def broadcast(self, message: dict): ...
```

---

### 2. WebSocket Routes

Located in `websocket_routes.py`, this component exposes the `/ws` and `/ws/{client_id}` endpoints.

* `/ws`: generic WebSocket endpoint for anonymous clients
* `/ws/{client_id}`: identifies the client and sends a personalized welcome message

When a client connects, the system:

1. Registers the connection with `ConnectionManager`
2. Listens for incoming messages
3. Processes each message asynchronously
4. On disconnection, cleans up resources and triggers related webhooks

**Example interaction flow:**

```plaintext
Client -> "Hello everyone"
Server -> Broadcasts message to all clients
Server -> Triggers message-broadcast webhook
```

---

### 3. Message Handling

`handle_websocket_message()` is responsible for processing all inbound messages.
It interprets structured JSON payloads and decides the appropriate action.

Supported message types:

| Type        | Description                                    |
| ----------- | ---------------------------------------------- |
| `broadcast` | Broadcasts message to all connected clients    |
| `ping`      | Responds with a “pong” message                 |
| `private`   | Placeholder for future private messaging logic |
| `chat`      | Default message type (general communication)   |

When a broadcast occurs, a **Webhook event** (`message-broadcast`) can also be emitted for external systems.

---

### 4. Webhook Definitions

The **webhook layer** defines REST endpoints to integrate the WebSocket system with external tools or monitoring systems.
It is not required for runtime but provides a way to **observe or log real-time events externally**.

**Defined webhook types:**

| Event                 | Trigger                                | Example Data                                                |
| --------------------- | -------------------------------------- | ----------------------------------------------------------- |
| `message-broadcast`   | When a message is broadcasted          | `{ "message": "...", "sender": "...", "timestamp": "..." }` |
| `client-connected`    | On new WebSocket connection            | `{ "client_number": 5, "total_connections": 32 }`           |
| `client-disconnected` | On client disconnect                   | `{ "remaining_connections": 31 }`                           |
| `server-status`       | On startup, shutdown, or health update | `{ "status": "running", "timestamp": "..." }`               |
| `broadcast-stats`     | Periodic broadcast statistics          | `{ "active_connections": 10, "total_messages": 200 }`       |

This allows the system to plug into dashboards, analytics tools, or monitoring services.

---

## Example Flow: Real-Time Broadcast

**Scenario:**
A client sends a broadcast message that should reach all connected clients and trigger a webhook.

```
Client A → "System update complete."
     ↓
FastAPI WebSocket endpoint
     ↓
handle_websocket_message()
     ↓
ConnectionManager.broadcast()
     ↓
All connected clients receive message
     ↓
Webhook: message-broadcast triggered
```

This ensures the message propagates in real time while maintaining event observability.

---

## Error Handling and Recovery

* **WebSocketDisconnect:** handled gracefully; connection removed and webhook triggered
* **JSONDecodeError:** fallback to plain text broadcast
* **Unexpected exceptions:** logged and connection closed safely
* **Ping/Pong heartbeat:** helps maintain active connection status

Logging is centralized, with every major event (connect/disconnect, message, error) captured for debugging or auditing.

---

## Local Development

**Run server:**

```bash
uvicorn app.main:app --reload
```

**Connect via browser or client:**

```js
const socket = new WebSocket("ws://localhost:8000/ws/user123");
socket.onmessage = (event) => console.log(event.data);
socket.send(JSON.stringify({ message: "Hello world", message_type: "chat" }));
```

**Expected behavior:**

* You receive your own message echoed as a broadcast.
* Other clients connected to the same endpoint receive it in real time.
* A webhook (if configured) is triggered for monitoring.

---

## Design Advantages

* **Real-time communication**: powered by FastAPI’s async WebSocket layer.
* **Extensible webhook layer**: allows integration with monitoring or external automation systems.
* **Scalable design**: supports multiple clients concurrently using asyncio and non-blocking I/O.
* **Event-driven architecture**: centralizes all broadcast events through structured handlers.
* **Ease of testing**: modular separation (routes, manager, webhooks, handlers) allows isolated testing.

---

## Summary

The backend WebSocket broadcast system provides a **real-time, event-driven communication layer** built on FastAPI.
It manages live client connections, synchronizes messages across users, and exposes webhook hooks for system visibility.
The design focuses on **scalability, resilience, and observability**, forming the foundation for interactive or collaborative real-time applications.
