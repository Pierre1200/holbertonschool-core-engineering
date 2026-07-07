#!/usr/bin/env python3

import os
import asyncio
import websockets


async def connect_and_send(uri, message):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response


if __name__ == "__main__":
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    response = asyncio.run(connect_and_send(uri, "Hello WebSocket"))
    print(f"{response}", end="")
