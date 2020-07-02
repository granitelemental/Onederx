import json
import asyncio
import websockets
import time

from db import Data
import config


data = Data()


async def send_time(websocket, path):
    while True:
        res = data.check_if_time()
        if res:
            current_time = data.current_time()
            msg = json.dumps({"Now": current_time, "alarm": res}, indent=4)
            await websocket.send(msg)
        await asyncio.sleep(1)


start_server = websockets.serve(
    send_time, config.SOCKET_HOST, config.SOCKET_PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
