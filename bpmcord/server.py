import asyncio
import websockets

from utils import exceptions, Log

async def echo(websocket):
    try:
        async for message in websocket:
            Log(1, message)
    except Exception as e:
        raise exceptions.WatchDisconnected(e)
    
async def main():
    async with websockets.serve(echo, "192.168.1.2", 3476):
        await asyncio.Future()  # run forever


asyncio.run(main())
