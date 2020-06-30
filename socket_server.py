import json
import asyncio
import websockets
from datetime import datetime, timedelta, timezone

from db import Data
import config


data = Data()

tz = timezone(offset=timedelta(hours=0))

async def send_time(websocket, path):
    while True:
        time = json.dumps(data.current_time(), indent=4)
        res = data.check_if_time()
        msg = ""
        if res:
            res = json.dumps(res, indent=4)
            await websocket.send(res)
        else:
            msg = " It's not time yet"

        await websocket.send("Now: " + time + msg)
        await asyncio.sleep(1)


start_server = websockets.serve(send_time, config.SOCKET_HOST, config.SOCKET_PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
