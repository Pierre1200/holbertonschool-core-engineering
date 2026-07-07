#!/usr/bin/env python3


import asyncio
import websockets


async def main():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(f"{response}")


if __name__ == "__main__":
    asyncio.run(main())
