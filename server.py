# server.py
import asyncio
import websockets

connected = set()

async def handler(websocket):
    connected.add(websocket)
    try:
        async for message in websocket:
            print("Received:", message)
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
    except:
        pass
    finally:
        connected.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("WebSocket Server running at ws://0.0.0.0:8765")
        await asyncio.Future()

asyncio.run(main())
