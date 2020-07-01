#!/usr/bin/env python

# WS client example

import asyncio
import websockets

import config


async def hello():
    uri = f"ws://{config.SOCKET_HOST}:{config.SOCKET_PORT}"
    async with websockets.connect(uri) as websocket:
        
        while True:
            msg = await websocket.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(hello())
